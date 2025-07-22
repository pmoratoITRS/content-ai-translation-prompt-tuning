#!/usr/bin/env python3
"""
Soft Prompt Inference for Documentation Translation

This script uses trained soft prompts to translate new content.
"""

import torch
import json
from pathlib import Path
from typing import Dict, List, Optional
import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from soft_prompt_tuning import SoftPromptModel


class SoftPromptTranslator:
    """Translator using trained soft prompts"""
    
    def __init__(self, model_path: Path, device: str = 'auto'):
        self.model_path = Path(model_path)
        
        # Auto-detect device
        if device == 'auto':
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        else:
            self.device = torch.device(device)
        
        self.load_model()
    
    def load_model(self):
        """Load the trained soft prompt model"""
        # Load configuration
        with open(self.model_path / "config.json", 'r') as f:
            self.config = json.load(f)
        
        # Load tokenizer
        tokenizer_path = self.model_path / "tokenizer"
        if tokenizer_path.exists():
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.config['base_model_name'])
        
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Load base model
        model_path = self.model_path / "model"
        if model_path.exists() and not self.config.get('model_frozen', True):
            # Load fine-tuned model
            base_model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        else:
            # Load original base model
            base_model = AutoModelForSeq2SeqLM.from_pretrained(self.config['base_model_name'])
        
        # Create soft prompt model
        self.model = SoftPromptModel(
            base_model, 
            self.tokenizer, 
            self.config['soft_prompt_length']
        )
        
        # Load soft prompt embeddings
        soft_prompt_path = self.model_path / "soft_prompt_embeddings.pt"
        if soft_prompt_path.exists():
            soft_prompt_embeddings = torch.load(soft_prompt_path, map_location=self.device)
            self.model.soft_prompt_embeddings.data = soft_prompt_embeddings
        else:
            raise FileNotFoundError(f"Soft prompt embeddings not found: {soft_prompt_path}")
        
        self.model.to(self.device)
        self.model.eval()
        
        print(f"Loaded soft prompt model for {self.config['target_language']}")
        print(f"Soft prompt length: {self.config['soft_prompt_length']}")
        print(f"Device: {self.device}")
    
    def translate(self, text: str, max_length: int = 1024) -> str:
        """Translate a single text using soft prompts"""
        # Use raw text input (matching training format)
        # The soft prompts provide the translation context
        
        # Tokenize input directly (no instruction prefix needed)
        inputs = self.tokenizer(
            text,
            max_length=max_length,
            padding="max_length", 
            truncation=True,
            return_tensors="pt"
        ).to(self.device)
        
        with torch.no_grad():
            # Generate translation
            outputs = self.model(
                source_ids=inputs['input_ids'],
                source_mask=inputs['attention_mask']
            )
            
            # Decode output
            translation = self.tokenizer.decode(
                outputs[0], 
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True
            )
        
        return translation.strip()
    
    def translate_batch(self, texts: List[str], max_length: int = 1024, 
                       batch_size: int = 4) -> List[str]:
        """Translate multiple texts in batches"""
        translations = []
        
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i + batch_size]
            
            # Tokenize batch
            inputs = self.tokenizer(
                batch_texts,
                max_length=max_length,
                padding=True,
                truncation=True,
                return_tensors="pt"
            ).to(self.device)
            
            with torch.no_grad():
                # Generate translations
                outputs = self.model(
                    source_ids=inputs['input_ids'],
                    source_mask=inputs['attention_mask']
                )
                
                # Decode outputs
                batch_translations = self.tokenizer.batch_decode(
                    outputs, 
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=True
                )
            
            translations.extend([t.strip() for t in batch_translations])
        
        return translations
    
    def translate_file(self, input_file: Path, output_file: Path = None) -> str:
        """Translate a markdown file"""
        # Read input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Translate
        translation = self.translate(content)
        
        # Save if output file specified
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translation)
            print(f"Translation saved: {output_file}")
        
        return translation


class BatchSoftPromptTranslator:
    """Batch translator for processing multiple files"""
    
    def __init__(self, model_path: Path, content_dir: Path, output_dir: Path):
        self.translator = SoftPromptTranslator(model_path)
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.target_language = self.translator.config['target_language']
    
    def process_directory(self, source_lang: str = 'en'):
        """Process all files in the content directory"""
        processed_count = 0
        
        # Process topics
        topics_dir = self.content_dir / "topics" / source_lang
        if topics_dir.exists():
            output_topics_dir = self.output_dir / "topics" / self.target_language
            output_topics_dir.mkdir(parents=True, exist_ok=True)
            
            for file_path in topics_dir.glob("*.md"):
                self._process_file(file_path, output_topics_dir, "topics")
                processed_count += 1
        
        # Process changelogs
        changelogs_dir = self.content_dir / "changelogs" / source_lang
        if changelogs_dir.exists():
            output_changelogs_dir = self.output_dir / "changelogs" / self.target_language
            output_changelogs_dir.mkdir(parents=True, exist_ok=True)
            
            for file_path in changelogs_dir.glob("*.md"):
                self._process_file(file_path, output_changelogs_dir, "changelogs")
                processed_count += 1
        
        print(f"Processed {processed_count} files")
        
        # Generate summary
        self._generate_summary(processed_count)
    
    def _process_file(self, input_file: Path, output_dir: Path, content_type: str):
        """Process a single file"""
        # Determine output filename
        base_name = input_file.name.replace('.en.md', '')
        output_name = f"{base_name}.{self.target_language}.md"
        output_file = output_dir / output_name
        
        print(f"Translating {input_file.name} -> {output_name}")
        
        try:
            # Translate file
            self.translator.translate_file(input_file, output_file)
        except Exception as e:
            print(f"Error translating {input_file.name}: {e}")
    
    def _generate_summary(self, processed_count: int):
        """Generate translation summary"""
        summary = {
            'model_path': str(self.translator.model_path),
            'target_language': self.target_language,
            'base_model': self.translator.config['base_model_name'],
            'soft_prompt_length': self.translator.config['soft_prompt_length'],
            'files_processed': processed_count,
            'output_directory': str(self.output_dir)
        }
        
        summary_file = self.output_dir / f"soft_prompt_translation_summary_{self.target_language}.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        print(f"Summary saved: {summary_file}")


def main():
    parser = argparse.ArgumentParser(description='Soft prompt inference for translation')
    
    # Required arguments
    parser.add_argument('--model-path', required=True, type=Path,
                       help='Path to trained soft prompt model')
    
    # Mode selection
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--text', help='Translate a single text string')
    mode_group.add_argument('--file', type=Path, help='Translate a single file')
    mode_group.add_argument('--batch', action='store_true', 
                           help='Batch translate content directory')
    
    # Batch mode arguments
    parser.add_argument('--content-dir', type=Path,
                       help='Content directory (required for batch mode)')
    parser.add_argument('--output-dir', type=Path,
                       help='Output directory (required for batch mode)')
    
    # Optional arguments
    parser.add_argument('--output-file', type=Path,
                       help='Output file for single file translation')
    parser.add_argument('--max-length', type=int, default=1024,
                       help='Maximum sequence length')
    parser.add_argument('--device', default='auto',
                       help='Device to use (auto, cpu, cuda)')
    
    args = parser.parse_args()
    
    if args.batch:
        if not args.content_dir or not args.output_dir:
            parser.error("--content-dir and --output-dir required for batch mode")
        
        # Batch translation
        batch_translator = BatchSoftPromptTranslator(
            args.model_path, args.content_dir, args.output_dir
        )
        batch_translator.process_directory()
    
    else:
        # Single translation
        translator = SoftPromptTranslator(args.model_path, args.device)
        
        if args.text:
            # Translate text string
            translation = translator.translate(args.text, args.max_length)
            print("Translation:")
            print(translation)
        
        elif args.file:
            # Translate file
            translation = translator.translate_file(args.file, args.output_file)
            if not args.output_file:
                print("Translation:")
                print(translation)


if __name__ == "__main__":
    main() 