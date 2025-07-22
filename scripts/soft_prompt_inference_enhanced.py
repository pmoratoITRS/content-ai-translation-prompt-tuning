#!/usr/bin/env python3
"""
Enhanced Soft Prompt Inference with Additional Instructions

This script supports adding custom instructions/rules during inference
while leveraging the base translation capability from soft prompts.
"""

import torch
import json
from pathlib import Path
from typing import Dict, List, Optional
import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from soft_prompt_tuning import SoftPromptModel

class EnhancedSoftPromptTranslator:
    """Enhanced translator with support for additional instructions"""
    
    def __init__(self, model_path: Path):
        self.model_path = Path(model_path)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
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
        base_model = AutoModelForSeq2SeqLM.from_pretrained(self.config['base_model_name'])
        
        # Create soft prompt model
        self.model = SoftPromptModel(base_model, self.tokenizer, self.config['soft_prompt_length'])
        
        # Load soft prompt embeddings
        soft_prompt_path = self.model_path / "soft_prompt_embeddings.pt"
        soft_prompt_embeddings = torch.load(soft_prompt_path, map_location=self.device)
        self.model.soft_prompt_embeddings.data = soft_prompt_embeddings
        
        self.model.to(self.device)
        self.model.eval()
        
        # Language names for instructions
        self.lang_names = {'fr': 'French', 'de': 'German', 'nl': 'Dutch'}
        self.target_lang_name = self.lang_names.get(self.config['target_language'], self.config['target_language'])
        
        print(f"Loaded enhanced soft prompt model for {self.config['target_language']}")
        print(f"Soft prompt length: {self.config['soft_prompt_length']}")
        print(f"Device: {self.device}")
    
    def translate(self, text: str, instruction: str = None, style: str = None, 
                 preserve_formatting: bool = False, max_length: int = 1024) -> str:
        """
        Translate text with optional additional instructions
        
        Args:
            text: Text to translate
            instruction: Custom instruction (e.g., "use formal tone")
            style: Predefined style ("formal", "casual", "technical", "marketing")
            preserve_formatting: Whether to preserve markdown/HTML formatting
            max_length: Maximum input length
        """
        # Build the complete input with instructions
        input_text = self._build_input_with_instructions(text, instruction, style, preserve_formatting)
        
        # Tokenize input
        inputs = self.tokenizer(
            input_text,
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
    
    def _build_input_with_instructions(self, text: str, instruction: str = None, 
                                     style: str = None, preserve_formatting: bool = False) -> str:
        """Build input text with additional instructions"""
        
        # Start with base translation instruction
        parts = [f"translate English to {self.target_lang_name}"]
        
        # Add style-specific instructions
        style_instructions = {
            'formal': 'use formal tone and professional language',
            'casual': 'use casual, conversational tone', 
            'technical': 'preserve technical terms and use precise terminology',
            'marketing': 'use engaging, persuasive language',
            'documentation': 'use clear, instructional language for technical documentation',
            'ui': 'use concise, user-friendly language for interface elements'
        }
        
        if style and style in style_instructions:
            parts.append(style_instructions[style])
        
        # Add formatting preservation instruction
        if preserve_formatting:
            parts.append('preserve markdown formatting and special syntax')
        
        # Add custom instruction
        if instruction:
            parts.append(instruction.strip())
        
        # Build final instruction
        if len(parts) == 1:
            # Just basic translation
            full_instruction = f"{parts[0]}: {text}"
        else:
            # Multiple instructions
            instruction_part = ", ".join(parts)
            full_instruction = f"{instruction_part}: {text}"
        
        return full_instruction
    
    def translate_with_examples(self, text: str, examples: List[Dict[str, str]], **kwargs) -> str:
        """
        Translate with few-shot examples
        
        Args:
            text: Text to translate
            examples: List of {"english": "...", "french": "..."} examples
            **kwargs: Additional arguments for translate()
        """
        # Build few-shot prompt
        example_parts = []
        for ex in examples[:3]:  # Limit to 3 examples to avoid context overflow
            example_parts.append(f"English: {ex['english']}")
            example_parts.append(f"{self.target_lang_name}: {ex[self.config['target_language']]}")
        
        if example_parts:
            examples_text = "\n".join(example_parts)
            full_text = f"Examples:\n{examples_text}\n\nTranslate: {text}"
        else:
            full_text = text
        
        return self.translate(full_text, **kwargs)


def main():
    parser = argparse.ArgumentParser(
        description='Enhanced Soft Prompt Inference with Additional Instructions',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:

  # Basic translation
  python scripts/soft_prompt_inference_enhanced.py \\
    --model-path models/soft-prompts/fr \\
    --text "Hello world"

  # With style instruction
  python scripts/soft_prompt_inference_enhanced.py \\
    --model-path models/soft-prompts/fr \\
    --text "Configure the database settings" \\
    --style technical

  # With custom instruction
  python scripts/soft_prompt_inference_enhanced.py \\
    --model-path models/soft-prompts/fr \\
    --text "Click the submit button" \\
    --instruction "use imperative form for UI actions"

  # With formatting preservation
  python scripts/soft_prompt_inference_enhanced.py \\
    --model-path models/soft-prompts/fr \\
    --text "**Bold** and `code` text" \\
    --preserve-formatting

  # Multiple instructions
  python scripts/soft_prompt_inference_enhanced.py \\
    --model-path models/soft-prompts/fr \\
    --text "API endpoint configuration" \\
    --style technical \\
    --instruction "keep acronyms in English" \\
    --preserve-formatting
        """
    )
    
    parser.add_argument('--model-path', type=str, required=True,
                       help='Path to the trained soft prompt model')
    parser.add_argument('--text', type=str, required=True,
                       help='Text to translate')
    
    # Instruction options
    parser.add_argument('--instruction', type=str,
                       help='Custom instruction (e.g., "use formal tone")')
    parser.add_argument('--style', type=str, 
                       choices=['formal', 'casual', 'technical', 'marketing', 'documentation', 'ui'],
                       help='Predefined style')
    parser.add_argument('--preserve-formatting', action='store_true',
                       help='Preserve markdown/HTML formatting')
    
    # Generation options
    parser.add_argument('--max-length', type=int, default=1024,
                       help='Maximum input length')
    
    args = parser.parse_args()
    
    # Create translator
    translator = EnhancedSoftPromptTranslator(args.model_path)
    
    # Translate with instructions
    translation = translator.translate(
        text=args.text,
        instruction=args.instruction,
        style=args.style,
        preserve_formatting=args.preserve_formatting,
        max_length=args.max_length
    )
    
    # Output results
    print("Translation:")
    print(translation)
    
    # Show the constructed instruction for debugging
    if args.instruction or args.style or args.preserve_formatting:
        input_text = translator._build_input_with_instructions(
            args.text, args.instruction, args.style, args.preserve_formatting
        )
        print(f"\nFull instruction used:")
        print(f"'{input_text}'")


if __name__ == "__main__":
    main() 