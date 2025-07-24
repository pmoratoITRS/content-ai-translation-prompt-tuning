#!/usr/bin/env python3
"""
Prompt Tuning Translator
Uses your existing masked datasets for few-shot prompting with GPT-4o or Claude 3.5 Sonnet
"""

import json
import random
import re
import os
from typing import List, Dict, Optional
from dataclasses import dataclass

# Import your existing preprocessor
from generateJSONL_PT import TranslationPreprocessor

@dataclass
class TranslationExample:
    input_content: str
    output_content: str
    complexity_score: float
    content_type: str  # 'changelog' or 'topic'

class PromptTuningTranslator:
    def __init__(self, dataset_dir: str = "."):
        """Initialize with your existing masked datasets"""
        self.dataset_dir = dataset_dir
        self.examples = {
            'French': self._load_examples('dataset-fr.jsonl'),
            'German': self._load_examples('dataset-de.jsonl'), 
            'Dutch': self._load_examples('dataset-nl.jsonl')
        }
        
    def _load_examples(self, filename: str) -> List[TranslationExample]:
        """Load and analyze examples from dataset"""
        filepath = os.path.join(self.dataset_dir, filename)
        examples = []
        
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found")
            return examples
            
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line)
                
                # Extract content without instruction
                input_content = data['input'].split('\n\n', 1)[1] if '\n\n' in data['input'] else data['input']
                
                example = TranslationExample(
                    input_content=input_content,
                    output_content=data['output'],
                    complexity_score=self._calculate_complexity(input_content),
                    content_type='changelog' if '/changelog/' in input_content else 'topic'
                )
                examples.append(example)
                
        print(f"Loaded {len(examples)} examples from {filename}")
        return examples
    
    def _calculate_complexity(self, content: str) -> float:
        """Calculate content complexity score"""
        score = 0
        score += content.count('[SHORTCODE_') * 2  # Shortcode complexity
        score += content.count('TRANSLATE_THIS:') * 1  # Translation markers
        score += len(content) / 100  # Length factor
        score += content.count('\n') * 0.5  # Structure complexity
        return score
    
    def select_best_examples(self, content: str, target_language: str, n_examples: int = 4) -> List[TranslationExample]:
        """Select most relevant examples for few-shot prompting"""
        
        if target_language not in self.examples:
            raise ValueError(f"No examples available for {target_language}")
        
        lang_examples = self.examples[target_language]
        if not lang_examples:
            return []
        
        content_complexity = self._calculate_complexity(content)
        content_type = 'changelog' if '/changelog/' in content else 'topic'
        content_shortcodes = content.count('[SHORTCODE_')
        
        scored_examples = []
        for ex in lang_examples:
            score = 0
            
            # Content type similarity (high weight)
            if ex.content_type == content_type:
                score += 15
            
            # Shortcode count similarity
            ex_shortcodes = ex.input_content.count('[SHORTCODE_')
            shortcode_diff = abs(content_shortcodes - ex_shortcodes)
            score += max(0, 10 - shortcode_diff)
            
            # Complexity similarity
            complexity_diff = abs(content_complexity - ex.complexity_score)
            score += max(0, 10 - complexity_diff / 2)
            
            # Length similarity
            length_ratio = min(len(content), len(ex.input_content)) / max(len(content), len(ex.input_content))
            score += length_ratio * 5
            
            # Avoid very short or very long examples
            if 200 < len(ex.input_content) < 2000:
                score += 5
                
            scored_examples.append((score, ex))
        
        # Sort by score and return top N
        scored_examples.sort(key=lambda x: x[0], reverse=True)
        selected = [ex for _, ex in scored_examples[:n_examples]]
        
        print(f"Selected {len(selected)} examples for {target_language} (scores: {[round(s, 1) for s, _ in scored_examples[:n_examples]]})") 
        return selected
    
    def build_prompt(self, content: str, target_language: str, prompt_style: str = "detailed") -> str:
        """Build optimized prompt with few-shot examples"""
        
        examples = self.select_best_examples(content, target_language)
        
        if not examples:
            return self._build_zero_shot_prompt(content, target_language)
        
        # Format examples
        example_text = ""
        for i, ex in enumerate(examples, 1):
            example_text += f"=== EXAMPLE {i} ===\n"
            example_text += f"INPUT:\n{ex.input_content}\n\n"
            example_text += f"OUTPUT:\n{ex.output_content}\n\n"
        
        if prompt_style == "detailed":
            prompt = f"""You are a professional technical translator specializing in Hugo-based documentation for software monitoring tools.

CRITICAL TRANSLATION RULES:
1. Preserve ALL [SHORTCODE_N] tokens exactly as written - never translate or modify them
2. Translate only content marked with "TRANSLATE_THIS:" 
3. Remove "TRANSLATE_THIS:" markers from the output completely
4. Maintain exact JSON structure and formatting
5. Provide accurate, professional {target_language} translations
6. Keep technical terminology consistent and precise
7. Preserve all URLs, code snippets, and technical identifiers unchanged

EXAMPLES OF CORRECT TRANSLATIONS:
{example_text}

NOW TRANSLATE THE FOLLOWING CONTENT TO {target_language.upper()}:

{content}

TRANSLATED OUTPUT:"""

        elif prompt_style == "concise":
            prompt = f"""Translate to {target_language}. Rules: Preserve [SHORTCODE_N], remove TRANSLATE_THIS:, maintain JSON structure.

Examples:
{example_text}

Translate:
{content}

Output:"""
        
        else:  # rules_first
            prompt = f"""RULES:
1. Preserve [SHORTCODE_N] exactly
2. Translate TRANSLATE_THIS: content, remove markers
3. Maintain JSON structure
4. Professional {target_language} translation

{example_text}

Translate to {target_language}:
{content}

Translation:"""
        
        return prompt
    
    def _build_zero_shot_prompt(self, content: str, target_language: str) -> str:
        """Fallback prompt without examples"""
        return f"""You are a professional technical translator. Translate the following English content to {target_language}.

CRITICAL RULES:
1. Preserve ALL [SHORTCODE_N] tokens exactly as written
2. Translate only content marked with "TRANSLATE_THIS:" and remove the markers
3. Maintain exact JSON structure and formatting
4. Provide accurate {target_language} translations

Content to translate:
{content}

Translation:"""

class ModelInterface:
    """Base class for model interfaces"""
    def translate(self, prompt: str, temperature: float = 0.1) -> str:
        raise NotImplementedError

class GPT4oTranslator(ModelInterface):
    def __init__(self, api_key: str):
        try:
            import openai
            self.client = openai.OpenAI(api_key=api_key)
            self.model = "gpt-4o-2024-08-06"
        except ImportError:
            raise ImportError("Please install openai: pip install openai")
    
    def translate(self, prompt: str, temperature: float = 0.1) -> str:
        """Translate using GPT-4o with prompt tuning"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a professional technical translator. Follow the instructions exactly and provide only the translated content."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=2500
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"GPT-4o translation failed: {str(e)}")

class ClaudeTranslator(ModelInterface):
    def __init__(self, api_key: str):
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
            self.model = "claude-3-5-sonnet-20241022"
        except ImportError:
            raise ImportError("Please install anthropic: pip install anthropic")
    
    def translate(self, prompt: str, temperature: float = 0.1) -> str:
        """Translate using Claude 3.5 Sonnet with prompt tuning"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2500,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            raise Exception(f"Claude translation failed: {str(e)}")

def translate_with_prompt_tuning(
    english_content: str, 
    target_language: str,
    model_choice: str = "gpt4o",
    api_key: str = None,
    prompt_style: str = "detailed",
    dataset_dir: str = "."
) -> str:
    """
    Complete translation pipeline using prompt tuning
    
    Args:
        english_content: Raw English markdown content
        target_language: 'French', 'German', or 'Dutch'
        model_choice: 'gpt4o' or 'claude'
        api_key: API key for the chosen model
        prompt_style: 'detailed', 'concise', or 'rules_first'
        dataset_dir: Directory containing your dataset files
    """
    
    # Step 1: Apply masking using your existing preprocessor
    print(f"🔄 Step 1: Applying masking to content...")
    preprocessor = TranslationPreprocessor()
    masked_content = preprocessor.process_document(english_content, is_output=False)
    
    # Step 2: Build optimized prompt
    print(f"🔄 Step 2: Building prompt for {target_language}...")
    prompt_builder = PromptTuningTranslator(dataset_dir)
    prompt = prompt_builder.build_prompt(masked_content, target_language, prompt_style)
    
    # Step 3: Translate using selected model
    print(f"🔄 Step 3: Translating with {model_choice}...")
    if model_choice == "gpt4o":
        translator = GPT4oTranslator(api_key)
    elif model_choice == "claude":
        translator = ClaudeTranslator(api_key)
    else:
        raise ValueError("model_choice must be 'gpt4o' or 'claude'")
    
    translated_content = translator.translate(prompt)
    
    # Step 4: Basic validation
    print(f"🔄 Step 4: Validating output...")
    if not translated_content or len(translated_content.strip()) < 50:
        raise Exception("Translation output is too short or empty")
    
    if "TRANSLATE_THIS:" in translated_content:
        print("⚠️  Warning: TRANSLATE_THIS markers found in output")
    
    print("✅ Translation completed successfully!")
    return translated_content

def validate_translation(original: str, translated: str) -> Dict[str, bool]:
    """Validate translation quality"""
    
    original_shortcodes = set(re.findall(r'\[SHORTCODE_\d+\]', original))
    translated_shortcodes = set(re.findall(r'\[SHORTCODE_\d+\]', translated))
    
    checks = {
        "shortcodes_preserved": original_shortcodes == translated_shortcodes,
        "no_translate_markers": "TRANSLATE_THIS:" not in translated,
        "reasonable_length": 0.3 <= len(translated)/len(original) <= 3.0,
        "not_empty": len(translated.strip()) > 50,
        "json_structure": translated.strip().startswith('{') if original.strip().startswith('{') else True
    }
    
    return checks

# Example usage and testing
if __name__ == "__main__":
    # Example usage
    sample_content = """{
  "title": "TRANSLATE_THIS: Two-factor authentication setup",
  "summary": "TRANSLATE_THIS: How to setup two-factor authentication (2FA) with TOTP for Uptrends."
}

For setting up two-factor authentication, an [TRANSLATE_THIS: account administrator]([SHORTCODE_1]) first needs to configure settings.

Click the {{< AppElement type="button" >}} Setup {{< /AppElement >}} button to begin."""

    print("🚀 Prompt Tuning Translation Example")
    print("=" * 50)
    
    # Initialize translator (this will load your existing datasets)
    translator = PromptTuningTranslator(".")
    
    # Build prompt (you can test this without API calls)
    prompt = translator.build_prompt(sample_content, "French", "detailed")
    
    print("📝 Generated Prompt:")
    print(prompt[:500] + "..." if len(prompt) > 500 else prompt)
    print("\n" + "=" * 50)
    
    # Uncomment to test with actual API (requires API key)
    # result = translate_with_prompt_tuning(
    #     sample_content, 
    #     "French", 
    #     model_choice="gpt4o",  # or "claude"
    #     api_key="your-api-key-here"
    # )
    # print("🎯 Translation Result:")
    # print(result) 