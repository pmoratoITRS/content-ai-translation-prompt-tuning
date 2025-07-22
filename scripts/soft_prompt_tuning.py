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
    
    # Soft prompt parameters
    soft_prompt_length: int = 20  # Number of learned prompt tokens
    learning_rate: float = 0.3    # Higher LR for prompt tokens
    model_learning_rate: float = 1e-5  # Lower LR for model (if unfrozen)
    
    # Training parameters
    num_epochs: int = 10
    batch_size: int = 2  # Reduced for CPU training
    max_length: int = 512  # Reduced for CPU training  
    warmup_steps: int = 100
    freeze_model: bool = True  # Only train prompt embeddings
    
    # Data parameters
    max_examples: int = 200  # Reduced for CPU training
    validation_split: float = 0.1


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
                max_length=1024,
                num_beams=4,
                early_stopping=True,
                do_sample=True,
                temperature=0.1
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
        
        # Move to GPU if available
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        if self.device.type == 'cpu':
            self.logger.warning("⚠️  Training on CPU - this will be slower")
            self.logger.info("💡 Consider reducing batch_size and max_examples for CPU training")
            
        self.model.to(self.device)
        self.logger.info(f"Using device: {self.device}")
        
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
        """Load paired files from directories"""
        english_texts = []
        translated_texts = []
        
        for en_file in en_dir.glob("*.en.md"):
            # Find corresponding translated file
            base_name = en_file.name.replace('.en.md', '')
            target_file = target_dir / f"{base_name}.{self.config.target_language}.md"
            
            if target_file.exists():
                try:
                    with open(en_file, 'r', encoding='utf-8') as f:
                        english_content = f.read().strip()
                    
                    with open(target_file, 'r', encoding='utf-8') as f:
                        translated_content = f.read().strip()
                    
                    # Skip empty files
                    if english_content and translated_content:
                        english_texts.append(english_content)
                        translated_texts.append(translated_content)
                
                except Exception as e:
                    self.logger.warning(f"Error loading {en_file.name}: {e}")
        
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
        
        # Create data loaders
        train_loader = DataLoader(
            train_dataset, batch_size=self.config.batch_size, shuffle=True
        )
        val_loader = DataLoader(
            val_dataset, batch_size=self.config.batch_size, shuffle=False
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
        """Train for one epoch"""
        self.model.train()
        total_loss = 0
        
        progress_bar = tqdm(self.train_loader, desc="Training")
        
        for batch in progress_bar:
            # Move batch to device
            batch = {k: v.to(self.device) for k, v in batch.items()}
            
            # Forward pass
            outputs = self.model(
                source_ids=batch['source_ids'],
                source_mask=batch['source_mask'],
                target_ids=batch['target_ids'],
                target_mask=batch['target_mask']
            )
            
            loss = outputs.loss
            
            # Backward pass
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            self.scheduler.step()
            
            total_loss += loss.item()
            progress_bar.set_postfix({'loss': f'{loss.item():.4f}'})
            
            # Clear cache to prevent memory accumulation
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            else:
                # For CPU training, force garbage collection
                import gc
                gc.collect()
        
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
    parser = argparse.ArgumentParser(description='Soft prompt tuning for translation')
    
    # Model and data
    parser.add_argument('--model-name', default='t5-small',
                       help='Base model for soft prompt tuning')
    parser.add_argument('--content-dir', required=True, type=Path,
                       help='Path to content directory with golden data')
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
    parser.add_argument('--num-epochs', type=int, default=10,
                       help='Number of training epochs')
    parser.add_argument('--batch-size', type=int, default=4,
                       help='Training batch size')
    parser.add_argument('--max-examples', type=int, default=1000,
                       help='Maximum number of training examples')
    parser.add_argument('--no-freeze-model', action='store_true',
                       help='Also fine-tune model parameters')
    
    args = parser.parse_args()
    
    # Create configuration
    config = SoftPromptConfig(
        model_name=args.model_name,
        target_language=args.target_language,
        content_dir=args.content_dir,
        output_dir=args.output_dir,
        soft_prompt_length=args.soft_prompt_length,
        learning_rate=args.learning_rate,
        model_learning_rate=args.model_learning_rate,
        num_epochs=args.num_epochs,
        batch_size=args.batch_size,
        max_examples=args.max_examples,
        freeze_model=not args.no_freeze_model
    )
    
    # Initialize trainer and start training
    trainer = SoftPromptTrainer(config)
    trainer.train()


if __name__ == "__main__":
    main() 