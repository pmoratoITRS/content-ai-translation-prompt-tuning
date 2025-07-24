#!/usr/bin/env python3
"""
Soft Prompt Tuning for Documentation Translation

This script implements soft prompt tuning using your golden data pairs.
The model learns continuous prompt embeddings from your human translations.
"""

import os
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torch.cuda.amp import autocast, GradScaler
from transformers import (
    AutoTokenizer, AutoModelForSeq2SeqLM, 
    get_linear_schedule_with_warmup
)
from torch.optim import AdamW
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import argparse
from dataclasses import dataclass
from tqdm import tqdm
import logging


@dataclass
class SoftPromptConfig:
    """Configuration for soft prompt tuning"""
    model_name: str
    target_language: str
    content_dir: Path
    output_dir: Path
    
    # Device selection
    device_preference: str = 'auto'  # 'auto', 'gpu', 'cuda', 'cpu'
    force_cpu: bool = False
    
    # Soft prompt parameters
    soft_prompt_length: int = 20  # Number of learned prompt tokens
    learning_rate: float = 0.3    # Higher LR for prompt tokens
    model_learning_rate: float = 1e-5  # Lower LR for model (if unfrozen)
    
    # Training parameters (will be auto-adjusted based on device)
    num_epochs: int = 15
    batch_size: int = 16
    max_length: int = 1024
    warmup_steps: int = 500
    freeze_model: bool = True  # Only train prompt embeddings
    gradient_accumulation_steps: int = 2
    
    # Data parameters
    max_examples: int = 5000
    validation_split: float = 0.1
    
    # Device-specific parameters (will be auto-adjusted)
    mixed_precision: bool = True
    dataloader_num_workers: int = 4
    pin_memory: bool = True
    
    def auto_adjust_for_device(self, device_type: str) -> None:
        """Auto-adjust parameters based on the selected device"""
        if device_type == 'cpu':
            # CPU-optimized parameters
            self.batch_size = min(self.batch_size, 4)  # Don't exceed 4 for CPU
            self.gradient_accumulation_steps = max(self.gradient_accumulation_steps, 2)  # Maintain effective batch size
            self.max_length = min(self.max_length, 512)  # Shorter sequences for CPU
            self.max_examples = min(self.max_examples, 1000)  # Fewer examples for CPU
            self.warmup_steps = min(self.warmup_steps, 100)  # Fewer warmup steps
            self.dataloader_num_workers = min(self.dataloader_num_workers, 2)  # Fewer workers for CPU
            self.mixed_precision = False  # No mixed precision on CPU
            self.pin_memory = False  # No memory pinning for CPU
        else:
            # GPU parameters - keep as specified or use defaults
            # Mixed precision only available on CUDA-capable GPUs
            if device_type == 'cuda':
                self.mixed_precision = self.mixed_precision  # Keep user preference
                self.pin_memory = self.pin_memory  # Keep user preference
            else:
                self.mixed_precision = False
                self.pin_memory = False


class TranslationDataset(Dataset):
    """Dataset for paired English-Translation content"""
    
    def __init__(self, source_texts: List[str], target_texts: List[str], 
                 tokenizer, max_length: int = 1024):
        self.source_texts = source_texts
        self.target_texts = target_texts
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.source_texts)
    
    def __getitem__(self, idx):
        source = self.source_texts[idx]
        target = self.target_texts[idx]
        
        # Tokenize source and target
        source_encoding = self.tokenizer(
            source,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        
        target_encoding = self.tokenizer(
            target,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        
        return {
            'source_ids': source_encoding['input_ids'].squeeze(),
            'source_mask': source_encoding['attention_mask'].squeeze(),
            'target_ids': target_encoding['input_ids'].squeeze(),
            'target_mask': target_encoding['attention_mask'].squeeze()
        }


class SoftPromptModel(nn.Module):
    """Model with learnable soft prompts"""
    
    def __init__(self, base_model, tokenizer, soft_prompt_length: int = 20):
        super().__init__()
        self.base_model = base_model
        self.tokenizer = tokenizer
        self.soft_prompt_length = soft_prompt_length
        
        # Get model's embedding dimension
        self.embed_dim = base_model.config.d_model
        
        # Initialize soft prompt embeddings
        self.soft_prompt_embeddings = nn.Parameter(
            torch.randn(soft_prompt_length, self.embed_dim) * 0.1
        )
        
        # Freeze base model parameters if specified
        self.freeze_model_params()
    
    def freeze_model_params(self):
        """Freeze all model parameters except soft prompts"""
        for param in self.base_model.parameters():
            param.requires_grad = False
    
    def unfreeze_model_params(self):
        """Unfreeze model parameters for joint training"""
        for param in self.base_model.parameters():
            param.requires_grad = True
    
    def get_soft_prompt_embeds(self, batch_size: int):
        """Get soft prompt embeddings for a batch"""
        return self.soft_prompt_embeddings.unsqueeze(0).expand(
            batch_size, self.soft_prompt_length, self.embed_dim
        )
    
    def forward(self, source_ids, source_mask, target_ids=None, target_mask=None):
        batch_size = source_ids.shape[0]
        
        # Get input embeddings
        input_embeds = self.base_model.get_input_embeddings()(source_ids)
        
        # Get soft prompt embeddings
        soft_prompt_embeds = self.get_soft_prompt_embeds(batch_size)
        
        # Concatenate soft prompts with input embeddings
        combined_embeds = torch.cat([soft_prompt_embeds, input_embeds], dim=1)
        
        # Extend attention mask for soft prompts
        soft_prompt_mask = torch.ones(
            batch_size, self.soft_prompt_length, 
            device=source_mask.device, dtype=source_mask.dtype
        )
        combined_mask = torch.cat([soft_prompt_mask, source_mask], dim=1)
        
        # Forward pass through model
        if target_ids is not None:
            # Training mode
            outputs = self.base_model(
                inputs_embeds=combined_embeds,
                attention_mask=combined_mask,
                labels=target_ids
            )
            return outputs
        else:
            # Inference mode
            outputs = self.base_model.generate(
                inputs_embeds=combined_embeds,
                attention_mask=combined_mask,
                max_new_tokens=100,  # Generate up to 100 new tokens
                num_beams=2,  # Reduce beam size for speed
                early_stopping=True,
                do_sample=False,  # Use greedy decoding for consistency
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                decoder_start_token_id=self.tokenizer.pad_token_id,  # T5 specific
                repetition_penalty=1.1  # Prevent repetition
            )
            return outputs


class SoftPromptTrainer:
    """Trainer for soft prompt tuning"""
    
    def __init__(self, config: SoftPromptConfig):
        self.config = config
        self.setup_logging()
        
        # Initialize tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        base_model = AutoModelForSeq2SeqLM.from_pretrained(config.model_name)
        self.model = SoftPromptModel(
            base_model, self.tokenizer, config.soft_prompt_length
        )
        
        # Device selection logic
        self.device = self._select_device()
        
        # Auto-adjust parameters based on device
        self.config.auto_adjust_for_device(self.device.type)
        self.logger.info(f"📝 Parameters auto-adjusted for {self.device.type.upper()} training")
            
        self.model.to(self.device)
        self.logger.info(f"Using device: {self.device}")
        
        # Setup mixed precision training
        self.scaler = GradScaler() if self.config.mixed_precision and self.device.type == 'cuda' else None
        if self.scaler:
            self.logger.info("🚀 Mixed precision training enabled")
        elif self.config.mixed_precision and self.device.type == 'cpu':
            self.logger.warning("Mixed precision requested but not available on CPU")
        
        # Log training configuration
        if self.device.type == 'cuda':
            # Check GPU memory and provide recommendations
            gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / 1024**3
            self.logger.info(f"🎯 GPU Training Configuration:")
            self.logger.info(f"  - GPU: {torch.cuda.get_device_name(0)} ({gpu_memory_gb:.1f}GB)")
            self.logger.info(f"  - Batch size: {self.config.batch_size}")
            self.logger.info(f"  - Gradient accumulation steps: {self.config.gradient_accumulation_steps}")
            self.logger.info(f"  - Effective batch size: {self.config.batch_size * self.config.gradient_accumulation_steps}")
            self.logger.info(f"  - Max sequence length: {self.config.max_length}")
            self.logger.info(f"  - Max training examples: {self.config.max_examples}")
            self.logger.info(f"  - Data loader workers: {self.config.dataloader_num_workers}")
            self.logger.info(f"  - Memory pinning: {self.config.pin_memory}")
            self.logger.info(f"  - Mixed precision: {self.config.mixed_precision}")
            
            # Provide memory-based recommendations
            if gpu_memory_gb < 8:
                self.logger.warning("⚠️  Low GPU memory detected. Consider:")
                self.logger.info("   --batch-size 8 --gradient-accumulation-steps 4 --max-length 512")
            elif gpu_memory_gb >= 24:
                self.logger.info("🚀 High GPU memory available. You could increase:")
                self.logger.info("   --batch-size 32 --gradient-accumulation-steps 1 --max-length 1024")
        else:
            self.logger.info(f"🖥️  CPU Training Configuration:")
            self.logger.info(f"  - Batch size: {self.config.batch_size}")
            self.logger.info(f"  - Gradient accumulation steps: {self.config.gradient_accumulation_steps}")
            self.logger.info(f"  - Effective batch size: {self.config.batch_size * self.config.gradient_accumulation_steps}")
            self.logger.info(f"  - Max sequence length: {self.config.max_length}")
            self.logger.info(f"  - Max training examples: {self.config.max_examples}")
            self.logger.info(f"  - Data loader workers: {self.config.dataloader_num_workers}")
            self.logger.info(f"  - Mixed precision: {self.config.mixed_precision} (CPU doesn't support)")
            self.logger.warning("⚠️  CPU training will be significantly slower than GPU")
            self.logger.info("💡 To force GPU: --device gpu (or remove --force-cpu)")
            
        # Show device selection made
        device_choice = "auto-detected" if self.config.device_preference == 'auto' else "user-specified"
        self.logger.info(f"🔧 Device selection: {device_choice} → {self.device}")
        
        # Load and prepare data
        self.train_loader, self.val_loader = self.prepare_data()
        
        # Setup optimizer and scheduler
        self.setup_training()
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def _select_device(self) -> torch.device:
        """Select device based on user preference and availability"""
        cuda_available = torch.cuda.is_available()
        
        # Handle force CPU flag
        if self.config.force_cpu:
            self.logger.info("🔧 Force CPU mode enabled")
            return torch.device('cpu')
        
        # Handle device preference
        device_pref = self.config.device_preference.lower()
        
        if device_pref == 'cpu':
            self.logger.info("🔧 CPU training requested by user")
            return torch.device('cpu')
        
        elif device_pref in ['gpu', 'cuda']:
            if cuda_available:
                self.logger.info("🚀 GPU training requested and CUDA is available")
                return torch.device('cuda')
            else:
                self.logger.warning("⚠️  GPU training requested but CUDA not available")
                self.logger.info("🔄 Falling back to CPU training")
                return torch.device('cpu')
        
        elif device_pref == 'auto':
            if cuda_available:
                self.logger.info("🎯 Auto-detected CUDA GPU - using GPU training")
                return torch.device('cuda')
            else:
                self.logger.info("🔍 No CUDA GPU detected - using CPU training")
                return torch.device('cpu')
        
        else:
            self.logger.warning(f"Unknown device preference: {device_pref}")
            return torch.device('cuda' if cuda_available else 'cpu')
    
    def load_paired_data(self) -> Tuple[List[str], List[str]]:
        """Load paired English-translation data from golden dataset"""
        english_texts = []
        translated_texts = []
        
        # Load from topics
        en_topics_dir = self.config.content_dir / "topics" / "en"
        target_topics_dir = self.config.content_dir / "topics" / self.config.target_language
        
        if en_topics_dir.exists() and target_topics_dir.exists():
            en_texts, target_texts = self._load_pairs_from_dir(en_topics_dir, target_topics_dir)
            english_texts.extend(en_texts)
            translated_texts.extend(target_texts)
        
        # Load from changelogs
        en_changelogs_dir = self.config.content_dir / "changelogs" / "en"
        target_changelogs_dir = self.config.content_dir / "changelogs" / self.config.target_language
        
        if en_changelogs_dir.exists() and target_changelogs_dir.exists():
            en_texts, target_texts = self._load_pairs_from_dir(en_changelogs_dir, target_changelogs_dir)
            english_texts.extend(en_texts)
            translated_texts.extend(target_texts)
        
        self.logger.info(f"Loaded {len(english_texts)} paired examples for {self.config.target_language}")
        
        # Limit data size if specified
        if len(english_texts) > self.config.max_examples:
            english_texts = english_texts[:self.config.max_examples]
            translated_texts = translated_texts[:self.config.max_examples]
            self.logger.info(f"Limited to {self.config.max_examples} examples")
        
        return english_texts, translated_texts
    
    def _load_pairs_from_dir(self, en_dir: Path, target_dir: Path) -> Tuple[List[str], List[str]]:
        """Load paired files from directories with verification"""
        english_texts = []
        translated_texts = []
        
        # Get all English files and sort for consistent processing
        en_files = sorted(list(en_dir.glob("*.en.md")))
        
        # Track pairing statistics
        pairs_found = 0
        pairs_missing = 0
        pairs_empty = 0
        pairs_loaded = 0
        
        self.logger.info(f"🔍 Verifying file pairs in {en_dir.parent.name}/{en_dir.name} → {target_dir.parent.name}/{target_dir.name}")
        self.logger.info(f"Found {len(en_files)} English files to process")
        
        for en_file in en_files:
            # Extract base name and construct target file path
            base_name = en_file.name.replace('.en.md', '')
            target_file = target_dir / f"{base_name}.{self.config.target_language}.md"
            
            self.logger.debug(f"Looking for pair: {en_file.name} → {target_file.name}")
            
            if target_file.exists():
                pairs_found += 1
                try:
                    # Load both files
                    with open(en_file, 'r', encoding='utf-8') as f:
                        english_content = f.read().strip()
                    
                    with open(target_file, 'r', encoding='utf-8') as f:
                        translated_content = f.read().strip()
                    
                    # Verify both files have content
                    if not english_content:
                        self.logger.warning(f"⚠️  Empty English file: {en_file.name}")
                        pairs_empty += 1
                        continue
                    
                    if not translated_content:
                        self.logger.warning(f"⚠️  Empty translated file: {target_file.name}")
                        pairs_empty += 1
                        continue
                    
                    # Additional content verification
                    en_word_count = len(english_content.split())
                    target_word_count = len(translated_content.split())
                    
                    # Warn if there's a huge discrepancy (might indicate pairing issues)
                    if en_word_count > 0 and target_word_count > 0:
                        ratio = max(en_word_count, target_word_count) / min(en_word_count, target_word_count)
                        if ratio > 3.0:  # More than 3x difference
                            self.logger.warning(f"⚠️  Large content size difference in {base_name}: EN={en_word_count} words, {self.config.target_language.upper()}={target_word_count} words")
                    
                    # Files look good, add to dataset
                    english_texts.append(english_content)
                    translated_texts.append(translated_content)
                    pairs_loaded += 1
                    
                    self.logger.debug(f"✅ Loaded pair: {en_file.name} ↔ {target_file.name} (EN: {en_word_count} words, {self.config.target_language.upper()}: {target_word_count} words)")
                
                except Exception as e:
                    self.logger.error(f"❌ Error loading pair {en_file.name} ↔ {target_file.name}: {e}")
                    pairs_empty += 1
            else:
                pairs_missing += 1
                self.logger.warning(f"❌ Missing translation: {en_file.name} → {target_file.name} (not found)")
        
        # Summary statistics
        self.logger.info(f"📊 Pairing Summary for {en_dir.parent.name}/{en_dir.name}:")
        self.logger.info(f"  ✅ Pairs found: {pairs_found}")
        self.logger.info(f"  ✅ Pairs loaded: {pairs_loaded}")
        self.logger.info(f"  ❌ Missing translations: {pairs_missing}")
        self.logger.info(f"  ⚠️  Empty/error files: {pairs_empty}")
        
        if pairs_missing > 0:
            self.logger.warning(f"⚠️  {pairs_missing} English files are missing their {self.config.target_language.upper()} translations")
        
        if pairs_loaded == 0:
            self.logger.error(f"❌ No valid file pairs loaded from {en_dir}")
        
        return english_texts, translated_texts
    
    def prepare_data(self) -> Tuple[DataLoader, DataLoader]:
        """Prepare training and validation data loaders"""
        english_texts, translated_texts = self.load_paired_data()
        
        # Split into train/validation
        split_idx = int(len(english_texts) * (1 - self.config.validation_split))
        
        train_english = english_texts[:split_idx]
        train_translated = translated_texts[:split_idx]
        val_english = english_texts[split_idx:]
        val_translated = translated_texts[split_idx:]
        
        # Create datasets
        train_dataset = TranslationDataset(
            train_english, train_translated, self.tokenizer, self.config.max_length
        )
        val_dataset = TranslationDataset(
            val_english, val_translated, self.tokenizer, self.config.max_length
        )
        
        # Create data loaders with GPU optimizations
        train_loader = DataLoader(
            train_dataset, 
            batch_size=self.config.batch_size, 
            shuffle=True,
            num_workers=self.config.dataloader_num_workers,
            pin_memory=self.config.pin_memory,
            persistent_workers=True if self.config.dataloader_num_workers > 0 else False
        )
        val_loader = DataLoader(
            val_dataset, 
            batch_size=self.config.batch_size, 
            shuffle=False,
            num_workers=self.config.dataloader_num_workers,
            pin_memory=self.config.pin_memory,
            persistent_workers=True if self.config.dataloader_num_workers > 0 else False
        )
        
        self.logger.info(f"Training samples: {len(train_dataset)}")
        self.logger.info(f"Validation samples: {len(val_dataset)}")
        
        return train_loader, val_loader
    
    def setup_training(self):
        """Setup optimizer and learning rate scheduler"""
        # Different learning rates for soft prompts vs model parameters
        param_groups = [
            {
                'params': [self.model.soft_prompt_embeddings],
                'lr': self.config.learning_rate  # Higher LR for soft prompts
            }
        ]
        
        if not self.config.freeze_model:
            param_groups.append({
                'params': [p for n, p in self.model.base_model.named_parameters()],
                'lr': self.config.model_learning_rate  # Lower LR for model
            })
        
        self.optimizer = AdamW(param_groups)
        
        # Calculate total training steps
        total_steps = len(self.train_loader) * self.config.num_epochs
        
        self.scheduler = get_linear_schedule_with_warmup(
            self.optimizer,
            num_warmup_steps=self.config.warmup_steps,
            num_training_steps=total_steps
        )
    
    def train_epoch(self):
        """Train for one epoch with gradient accumulation and mixed precision"""
        self.model.train()
        total_loss = 0
        
        progress_bar = tqdm(self.train_loader, desc="Training")
        accumulation_steps = self.config.gradient_accumulation_steps
        
        for step, batch in enumerate(progress_bar):
            # Move batch to device with non_blocking for faster transfer
            batch = {k: v.to(self.device, non_blocking=True) for k, v in batch.items()}
            
            # Forward pass with mixed precision
            with autocast(enabled=self.scaler is not None):
                outputs = self.model(
                    source_ids=batch['source_ids'],
                    source_mask=batch['source_mask'],
                    target_ids=batch['target_ids'],
                    target_mask=batch['target_mask']
                )
                
                loss = outputs.loss / accumulation_steps  # Scale loss for accumulation
            
            # Backward pass
            if self.scaler:
                self.scaler.scale(loss).backward()
            else:
                loss.backward()
            
            # Gradient accumulation - only step optimizer every N steps
            if (step + 1) % accumulation_steps == 0:
                if self.scaler:
                    self.scaler.step(self.optimizer)
                    self.scaler.update()
                else:
                    self.optimizer.step()
                
                self.scheduler.step()
                self.optimizer.zero_grad()
            
            total_loss += loss.item() * accumulation_steps  # Unscale for logging
            progress_bar.set_postfix({
                'loss': f'{loss.item() * accumulation_steps:.4f}',
                'step': f'{step + 1}/{len(self.train_loader)}',
                'lr': f'{self.scheduler.get_last_lr()[0]:.2e}'
            })
        
        # Handle remaining gradients if batch doesn't divide evenly
        if len(self.train_loader) % accumulation_steps != 0:
            if self.scaler:
                self.scaler.step(self.optimizer)
                self.scaler.update()
            else:
                self.optimizer.step()
            self.optimizer.zero_grad()
        
        return total_loss / len(self.train_loader)
    
    def validate(self):
        """Validate the model"""
        self.model.eval()
        total_loss = 0
        
        with torch.no_grad():
            for batch in tqdm(self.val_loader, desc="Validation"):
                batch = {k: v.to(self.device) for k, v in batch.items()}
                
                outputs = self.model(
                    source_ids=batch['source_ids'],
                    source_mask=batch['source_mask'],
                    target_ids=batch['target_ids'],
                    target_mask=batch['target_mask']
                )
                
                total_loss += outputs.loss.item()
        
        return total_loss / len(self.val_loader)
    
    def train(self):
        """Main training loop"""
        self.logger.info("Starting soft prompt tuning...")
        self.logger.info(f"Soft prompt length: {self.config.soft_prompt_length}")
        self.logger.info(f"Model frozen: {self.config.freeze_model}")
        
        best_val_loss = float('inf')
        
        for epoch in range(self.config.num_epochs):
            self.logger.info(f"Epoch {epoch + 1}/{self.config.num_epochs}")
            
            # Training
            train_loss = self.train_epoch()
            
            # Validation
            val_loss = self.validate()
            
            self.logger.info(f"Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}")
            
            # Save best model
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                self.save_model(f"best_soft_prompt_{self.config.target_language}")
                self.logger.info("Saved new best model")
        
        # Save final model
        self.save_model(f"final_soft_prompt_{self.config.target_language}")
        self.logger.info("Training completed!")
    
    def save_model(self, name: str):
        """Save the soft prompt model"""
        save_path = self.config.output_dir / name
        save_path.mkdir(parents=True, exist_ok=True)
        
        # Save soft prompt embeddings
        torch.save(
            self.model.soft_prompt_embeddings.data,
            save_path / "soft_prompt_embeddings.pt"
        )
        
        # Save model state dict if not frozen
        if not self.config.freeze_model:
            self.model.base_model.save_pretrained(save_path / "model")
        
        # Save tokenizer
        self.tokenizer.save_pretrained(save_path / "tokenizer")
        
        # Save config
        config_dict = {
            'base_model_name': self.config.model_name,
            'target_language': self.config.target_language,
            'soft_prompt_length': self.config.soft_prompt_length,
            'embed_dim': self.model.embed_dim,
            'model_frozen': self.config.freeze_model
        }
        
        with open(save_path / "config.json", 'w') as f:
            json.dump(config_dict, f, indent=2)
        
        self.logger.info(f"Model saved to {save_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Soft prompt tuning for translation with automatic CPU/GPU optimization',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Recommended: Use preprocessed (masked) data with auto-device detection
  python soft_prompt_tuning.py --content-dir content_masked --target-language fr --output-dir models/fr --use-masked-data

  # Force GPU training with masked data
  python soft_prompt_tuning.py --device gpu --content-dir content_masked --target-language fr --output-dir models/fr --use-masked-data

  # Force CPU training with raw data (not recommended)
  python soft_prompt_tuning.py --device cpu --content-dir content --target-language fr --output-dir models/fr
  
  # Quick test with smaller dataset
  python soft_prompt_tuning.py --content-dir content_masked --target-language fr --output-dir models/fr-test --use-masked-data --max-examples 100
  
  # Verify file pairs without training
  python soft_prompt_tuning.py --content-dir content_masked --target-language fr --output-dir models/fr --verify-only --verbose
  
  # Training with detailed pair verification
  python soft_prompt_tuning.py --content-dir content_masked --target-language fr --output-dir models/fr --use-masked-data --verify-pairs --verbose

IMPORTANT: Run preprocess_golden_data.py first to create masked data for optimal training results.
        """
    )
    
    # Model and data
    parser.add_argument('--model-name', default='t5-small',
                       help='Base model for soft prompt tuning')
    parser.add_argument('--content-dir', required=True, type=Path,
                       help='Path to content directory with golden data (use content_masked for preprocessed data)')
    parser.add_argument('--target-language', required=True, choices=['fr', 'de', 'nl'],
                       help='Target language')
    parser.add_argument('--output-dir', required=True, type=Path,
                       help='Output directory for trained soft prompts')
    
    # Soft prompt parameters
    parser.add_argument('--soft-prompt-length', type=int, default=20,
                       help='Number of soft prompt tokens')
    parser.add_argument('--learning-rate', type=float, default=0.3,
                       help='Learning rate for soft prompts')
    parser.add_argument('--model-learning-rate', type=float, default=1e-5,
                       help='Learning rate for model (if unfrozen)')
    
    # Training parameters
    parser.add_argument('--num-epochs', type=int, default=15,
                       help='Number of training epochs')
    parser.add_argument('--batch-size', type=int, default=16,
                       help='Training batch size')
    parser.add_argument('--max-examples', type=int, default=5000,
                       help='Maximum number of training examples')
    parser.add_argument('--gradient-accumulation-steps', type=int, default=2,
                       help='Number of steps for gradient accumulation')
    parser.add_argument('--no-freeze-model', action='store_true',
                       help='Also fine-tune model parameters')
    
    # Device selection
    parser.add_argument('--device', choices=['auto', 'gpu', 'cuda', 'cpu'], default='auto',
                       help='Device to use for training (auto, gpu/cuda, cpu)')
    parser.add_argument('--force-cpu', action='store_true',
                       help='Force CPU training even if GPU is available')
    
    # Data preprocessing
    parser.add_argument('--use-masked-data', action='store_true',
                       help='Indicates that content directory contains preprocessed (masked) data')
    
    # GPU optimization parameters
    parser.add_argument('--no-mixed-precision', action='store_true',
                       help='Disable mixed precision training')
    parser.add_argument('--dataloader-workers', type=int, default=None,
                       help='Number of workers for data loading (auto-detected if not specified)')
    parser.add_argument('--no-pin-memory', action='store_true',
                       help='Disable memory pinning for faster GPU transfer')
    
    # Debugging and verification
    parser.add_argument('--verify-pairs', action='store_true',
                       help='Enable detailed verification of English-Translation file pairs')
    parser.add_argument('--verify-only', action='store_true',
                       help='Only verify file pairs and exit (no training)')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose logging including file pair details')
    
    args = parser.parse_args()
    
    # Setup logging level based on verbosity
    if args.verbose or args.verify_pairs:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Auto-determine dataloader workers if not specified
    dataloader_workers = args.dataloader_workers
    if dataloader_workers is None:
        # Auto-select based on device preference
        if args.force_cpu or args.device == 'cpu':
            dataloader_workers = 2  # Conservative for CPU
        else:
            dataloader_workers = 4  # Standard for GPU
    
    # Create configuration
    config = SoftPromptConfig(
        model_name=args.model_name,
        target_language=args.target_language,
        content_dir=args.content_dir,
        output_dir=args.output_dir,
        device_preference=args.device,
        force_cpu=args.force_cpu,
        soft_prompt_length=args.soft_prompt_length,
        learning_rate=args.learning_rate,
        model_learning_rate=args.model_learning_rate,
        num_epochs=args.num_epochs,
        batch_size=args.batch_size,
        max_examples=args.max_examples,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        freeze_model=not args.no_freeze_model,
        mixed_precision=not args.no_mixed_precision,
        dataloader_num_workers=dataloader_workers,
        pin_memory=not args.no_pin_memory
    )
    
    # Initialize trainer
    trainer = SoftPromptTrainer(config)
    
    # If verify-only mode, just check pairs and exit
    if args.verify_only:
        print(f"\n✅ File pair verification completed!")
        print(f"📊 Total examples available: {len(trainer.train_loader.dataset) + len(trainer.val_loader.dataset)}")
        print(f"📊 Training examples: {len(trainer.train_loader.dataset)}")
        print(f"📊 Validation examples: {len(trainer.val_loader.dataset)}")
        return
    
    # Start training
    trainer.train()


if __name__ == "__main__":
    main() 