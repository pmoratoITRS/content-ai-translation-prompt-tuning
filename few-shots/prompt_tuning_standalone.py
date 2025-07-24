#!/usr/bin/env python3
"""
Standalone Prompt Tuning Translator
Complete implementation for few-shot prompting with your existing datasets
"""

import json
import re
import os
from typing import List, Dict, Optional
from dataclasses import dataclass

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
                
        print(f"✅ Loaded {len(examples)} examples from {filename}")
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
        
        print(f"🎯 Selected {len(selected)} examples for {target_language}")
        print(f"   Relevance scores: {[round(s, 1) for s, _ in scored_examples[:n_examples]]}")
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
            example_text += f"INPUT:\n{ex.input_content[:500]}{'...' if len(ex.input_content) > 500 else ''}\n\n"
            example_text += f"OUTPUT:\n{ex.output_content[:500]}{'...' if len(ex.output_content) > 500 else ''}\n\n"
        
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

# Simple masking for demo (inline version)
def apply_basic_masking(content: str) -> str:
    """Apply basic masking to content for demo purposes"""
    # This is a simplified version - use your full preprocessor for production
    
    # Mock shortcode masking
    shortcode_pattern = re.compile(r'\{\{<\s*([^>]+)\s*>\}\}')
    counter = 1
    
    def replace_shortcode(match):
        nonlocal counter
        result = f"[SHORTCODE_{counter}]"
        counter += 1
        return result
    
    content = shortcode_pattern.sub(replace_shortcode, content)
    
    # Add TRANSLATE_THIS markers for titles in JSON
    if content.strip().startswith('{'):
        try:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if '"title":' in line and 'TRANSLATE_THIS:' not in line:
                    # Extract title value and add marker
                    title_match = re.search(r'"title":\s*"([^"]+)"', line)
                    if title_match:
                        old_title = title_match.group(1)
                        new_title = f"TRANSLATE_THIS: {old_title}"
                        lines[i] = line.replace(f'"{old_title}"', f'"{new_title}"')
            content = '\n'.join(lines)
        except:
            pass
    
    return content

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

# Demo and testing functions
def demo_prompt_generation():
    """Demo showing how prompts are generated"""
    
    # Sample content (like your 2fa-setup.en.md)
    sample_content = """{
  "title": "TRANSLATE_THIS: Two-factor authentication setup",
  "summary": "TRANSLATE_THIS: How to setup two-factor authentication (2FA) with TOTP for Uptrends."
}

For setting up two-factor authentication, an [TRANSLATE_THIS: account administrator]([SHORTCODE_1]) first needs to configure settings.

In Uptrends, go to [SHORTCODE_2] Account setup > Account settings [SHORTCODE_3] and check one of the options at **Two-factor authentication setting**.

![TRANSLATE_THIS: screenshot 2FA account setting](/img/content/scr_2fa-authentication-setting.min.png)"""

    print("🚀 PROMPT TUNING DEMO")
    print("=" * 60)
    
    # Initialize translator
    translator = PromptTuningTranslator(".")
    
    # Test with different languages
    for language in ['French', 'German', 'Dutch']:
        print(f"\n📋 Building prompt for {language}...")
        
        try:
            prompt = translator.build_prompt(sample_content, language, "detailed")
            
            print(f"✅ Prompt generated successfully!")
            print(f"   Length: {len(prompt):,} characters")
            print(f"   Examples used: {prompt.count('=== EXAMPLE')}")
            
            # Show first part of prompt
            print(f"\n📝 Prompt preview ({language}):")
            print(prompt[:300] + "...\n" if len(prompt) > 300 else prompt)
            
        except Exception as e:
            print(f"❌ Error generating prompt for {language}: {e}")

def test_with_actual_api(api_key: str, model_choice: str = "gpt4o"):
    """Test with actual API call (uncomment when ready)"""
    
    sample_content = """{
  "title": "TRANSLATE_THIS: Performance metrics for individual transaction steps",
  "summary": "TRANSLATE_THIS: How to enable performance metrics for transaction monitoring"
}

Would you like to show the performance metrics [TRANSLATE_THIS: Core Web Vitals]([SHORTCODE_1]) of individual steps?"""
    
    print("🧪 TESTING WITH ACTUAL API")
    print("=" * 60)
    
    translator = PromptTuningTranslator(".")
    
    # Build prompt
    prompt = translator.build_prompt(sample_content, "French", "detailed")
    
    if model_choice == "gpt4o":
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            
            response = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": "You are a professional technical translator. Follow instructions exactly."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=2000
            )
            
            result = response.choices[0].message.content.strip()
            
            print("✅ Translation successful!")
            print(f"📝 Result:\n{result}")
            
            # Validate
            validation = validate_translation(sample_content, result)
            print(f"\n🔍 Validation:")
            for check, passed in validation.items():
                print(f"   {check}: {'✅' if passed else '❌'}")
                
        except ImportError:
            print("❌ OpenAI library not installed. Run: pip install openai")
        except Exception as e:
            print(f"❌ API error: {e}")
    
    elif model_choice == "claude":
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            
            response = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                temperature=0.1,
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.content[0].text.strip()
            
            print("✅ Translation successful!")
            print(f"📝 Result:\n{result}")
            
            # Validate
            validation = validate_translation(sample_content, result)
            print(f"\n🔍 Validation:")
            for check, passed in validation.items():
                print(f"   {check}: {'✅' if passed else '❌'}")
                
        except ImportError:
            print("❌ Anthropic library not installed. Run: pip install anthropic")
        except Exception as e:
            print(f"❌ API error: {e}")

if __name__ == "__main__":
    # Run demo
    demo_prompt_generation()
    
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS:")
    print("1. Review the generated prompts above")
    print("2. Test with actual API by uncommenting test_with_actual_api()")
    print("3. Adjust prompt_style ('detailed', 'concise', 'rules_first')")
    print("4. Fine-tune example selection based on results")
    
    # Uncomment to test with actual API
    # test_with_actual_api("your-api-key-here", "gpt4o")  # or "claude" 