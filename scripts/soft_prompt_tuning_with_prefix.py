#!/usr/bin/env python3
"""
Soft Prompt Tuning with T5 Instruction Prefix

This version adds instruction prefixes to improve T5 compatibility.
"""

import torch
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
from dataclasses import dataclass
import logging
import math

# Import the main classes from the original script
from soft_prompt_tuning import (
    SoftPromptConfig, SoftPromptModel, SoftPromptTrainer
)

class TranslationDatasetWithPrefix(Dataset):
    """Dataset for paired English-Translation content with T5 instruction prefix"""
    
    def __init__(self, source_texts: List[str], target_texts: List[str], 
                 tokenizer, target_language: str, max_length: int = 1024):
        self.source_texts = source_texts
        self.target_texts = target_texts
        self.tokenizer = tokenizer
        self.max_length = max_length
        
        # Language name mapping for natural instructions
        self.lang_names = {
            'fr': 'French',
            'de': 'German', 
            'nl': 'Dutch'
        }
        self.target_lang_name = self.lang_names.get(target_language, target_language)
    
    def __len__(self):
        return len(self.source_texts)
    
    def __getitem__(self, idx):
        source = self.source_texts[idx]
        target = self.target_texts[idx]
        
        # Add T5 instruction prefix to source
        prefixed_source = f"translate English to {self.target_lang_name}: {source}"
        
        # Tokenize source with prefix
        source_encoding = self.tokenizer(
            prefixed_source,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        
        # Tokenize target (no prefix needed)
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


class SoftPromptTrainerWithPrefix(SoftPromptTrainer):
    """Extended trainer that uses instruction prefixes"""
    
    def prepare_data(self) -> Tuple[DataLoader, DataLoader]:
        """Prepare training and validation data loaders with prefixes"""
        english_texts, translated_texts = self.load_paired_data()
        
        # Split into train/validation
        split_idx = int(len(english_texts) * (1 - self.config.validation_split))
        
        train_english = english_texts[:split_idx]
        train_translated = translated_texts[:split_idx]
        val_english = english_texts[split_idx:]
        val_translated = translated_texts[split_idx:]
        
        # Create datasets WITH PREFIX
        train_dataset = TranslationDatasetWithPrefix(
            train_english, train_translated, 
            self.tokenizer, self.config.target_language, self.config.max_length
        )
        val_dataset = TranslationDatasetWithPrefix(
            val_english, val_translated,
            self.tokenizer, self.config.target_language, self.config.max_length
        )
        
        self.logger.info(f"📊 Dataset sizes: Train={len(train_dataset)}, Validation={len(val_dataset)}")
        
        # Create data loaders
        train_loader = DataLoader(
            train_dataset, 
            batch_size=self.config.batch_size, 
            shuffle=True,
            num_workers=self.config.dataloader_num_workers,
            pin_memory=self.config.pin_memory
        )
        val_loader = DataLoader(
            val_dataset, 
            batch_size=self.config.batch_size, 
            shuffle=False,
            num_workers=self.config.dataloader_num_workers,
            pin_memory=self.config.pin_memory
        )
        
        return train_loader, val_loader


def main():
    parser = argparse.ArgumentParser(
        description='Soft Prompt Tuning with T5 Instruction Prefix',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Train with instruction prefix (recommended for T5)
  python scripts/soft_prompt_tuning_with_prefix.py \\
    --content-dir content_masked \\
    --target-language fr \\
    --output-dir models/soft-prompts-prefix/fr \\
    --use-masked-data \\
    --device gpu \\
    --batch-size 16 \\
    --num-epochs 25 \\
    --learning-rate 0.05
        """
    )
    
    parser.add_argument('--content-dir', type=str, required=True, 
                       help='Directory containing the content')
    parser.add_argument('--target-language', type=str, required=True, 
                       choices=['fr', 'de', 'nl'], help='Target language')
    parser.add_argument('--output-dir', type=str, required=True, 
                       help='Directory to save the trained model')
    parser.add_argument('--use-masked-data', action='store_true',
                       help='Use preprocessed masked data instead of raw content')
    
    # Training parameters
    parser.add_argument('--batch-size', type=int, default=16, help='Batch size')
    parser.add_argument('--num-epochs', type=int, default=25, help='Number of epochs')
    parser.add_argument('--learning-rate', type=float, default=0.05, help='Learning rate')
    parser.add_argument('--soft-prompt-length', type=int, default=30, help='Soft prompt length')
    parser.add_argument('--max-examples', type=int, default=2000, help='Maximum training examples')
    
    # Device and optimization
    parser.add_argument('--device', type=str, default='auto', 
                       choices=['auto', 'gpu', 'cuda', 'cpu'], help='Device to use')
    parser.add_argument('--force-cpu', action='store_true', help='Force CPU usage')
    
    # Verification and debugging
    parser.add_argument('--verify-pairs', action='store_true', help='Enable detailed pair verification')
    parser.add_argument('--verify-only', action='store_true', help='Only verify pairs, don\'t train')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Set up logging
    if args.verbose or args.verify_pairs:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    # Create configuration
    config = SoftPromptConfig(
        target_language=args.target_language,
        batch_size=args.batch_size,
        num_epochs=args.num_epochs,
        learning_rate=args.learning_rate,
        soft_prompt_length=args.soft_prompt_length,
        max_examples=args.max_examples,
        device_preference=args.device,
        force_cpu=args.force_cpu
    )
    
    # Create trainer with prefix support
    trainer = SoftPromptTrainerWithPrefix(config, args.content_dir, args.output_dir)
    trainer.use_masked_data = args.use_masked_data
    trainer.verify_pairs = args.verify_pairs
    
    if args.verify_only:
        print("🔍 Verification completed. Exiting without training.")
        return
    
    # Train the model
    trainer.train()
    
    print(f"✅ Training completed! Model saved to: {args.output_dir}")
    print(f"\n🧪 Test your model:")
    print(f"python scripts/soft_prompt_inference.py \\")
    print(f"  --model-path {args.output_dir} \\")
    print(f"  --text \"Your English text here\"")


if __name__ == "__main__":
    main() 