# Prompt Tuning Approach for Multilingual Translation

## 🎯 **Prompt Tuning vs Fine-tuning**

**Prompt Tuning Benefits:**
- ✅ No model training required - immediate deployment
- ✅ Lower cost - pay per inference only
- ✅ Faster iteration - modify prompts instantly
- ✅ Use latest models (GPT-4o, Claude 3.5 Sonnet)
- ✅ Easy A/B testing of different prompt strategies

## 🚀 **Prompt Engineering Strategy**

### **Core Prompt Template**
```
You are a professional technical translator specializing in Hugo-based documentation.

CRITICAL RULES:
1. Preserve ALL [SHORTCODE_N] tokens exactly as written
2. Translate only content marked with "TRANSLATE_THIS:"
3. Remove "TRANSLATE_THIS:" markers from output
4. Maintain JSON structure and formatting
5. Provide accurate technical translations

TARGET LANGUAGE: {target_language}

EXAMPLES:
{few_shot_examples}

NOW TRANSLATE:
{content_to_translate}
```

### **Few-Shot Example Selection Strategy**

**Dynamic Example Selection:**
- Select 3-5 most relevant examples based on content similarity
- Include variety: JSON frontmatter, shortcodes, technical terms
- Balance example complexity and length

## 📝 **Implementation Scripts**

### **1. Prompt Builder Script**
```python
import json
import random
from typing import List, Dict

class PromptTuningTranslator:
    def __init__(self, dataset_path: str):
        """Initialize with your existing masked datasets"""
        self.examples = self._load_examples(dataset_path)
        
    def _load_examples(self, dataset_path: str) -> List[Dict]:
        """Load examples from your existing datasets"""
        examples = []
        with open(dataset_path, 'r', encoding='utf-8') as f:
            for line in f:
                examples.append(json.loads(line))
        return examples
    
    def select_examples(self, content: str, target_lang: str, n_examples: int = 4) -> List[Dict]:
        """Select most relevant examples for few-shot prompting"""
        
        # Filter by target language
        lang_examples = [ex for ex in self.examples 
                        if f"Translate English to {target_lang}" in ex['input']]
        
        # Simple relevance scoring (you can enhance this)
        scored_examples = []
        for ex in lang_examples:
            score = 0
            # Prefer examples with similar shortcode count
            content_shortcodes = content.count('[SHORTCODE_')
            ex_shortcodes = ex['input'].count('[SHORTCODE_')
            score += max(0, 5 - abs(content_shortcodes - ex_shortcodes))
            
            # Prefer examples with similar length
            length_similarity = 1 - abs(len(content) - len(ex['input'])) / max(len(content), len(ex['input']))
            score += length_similarity * 3
            
            scored_examples.append((score, ex))
        
        # Sort by score and return top N
        scored_examples.sort(key=lambda x: x[0], reverse=True)
        return [ex for _, ex in scored_examples[:n_examples]]
    
    def build_prompt(self, content: str, target_language: str) -> str:
        """Build optimized prompt with few-shot examples"""
        
        # Select relevant examples
        examples = self.select_examples(content, target_language)
        
        # Format examples
        example_text = ""
        for i, ex in enumerate(examples, 1):
            # Clean the input to remove the instruction part
            input_content = ex['input'].split('\n\n', 1)[1] if '\n\n' in ex['input'] else ex['input']
            example_text += f"Example {i}:\nINPUT:\n{input_content}\n\nOUTPUT:\n{ex['output']}\n\n---\n\n"
        
        # Build final prompt
        prompt = f"""You are a professional technical translator specializing in Hugo-based documentation.

CRITICAL RULES:
1. Preserve ALL [SHORTCODE_N] tokens exactly as written
2. Translate only content marked with "TRANSLATE_THIS:"
3. Remove "TRANSLATE_THIS:" markers from output
4. Maintain JSON structure and formatting exactly
5. Provide accurate technical translations for {target_language}

EXAMPLES:
{example_text}

NOW TRANSLATE THE FOLLOWING CONTENT TO {target_language.upper()}:

{content}

TRANSLATION:"""
        
        return prompt

# Usage example
translator = PromptTuningTranslator('dataset-fr.jsonl')
prompt = translator.build_prompt(masked_content, 'French')
```

### **2. Model Interface Scripts**

**OpenAI GPT-4o Interface:**
```python
import openai
from typing import Optional

class GPT4oTranslator:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.model = "gpt-4o-2024-08-06"
    
    def translate(self, prompt: str, temperature: float = 0.1) -> str:
        """Translate using GPT-4o with prompt tuning"""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a professional technical translator. Follow the instructions exactly."
                },
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()

# Usage
gpt_translator = GPT4oTranslator("your-api-key")
result = gpt_translator.translate(prompt)
```

**Claude 3.5 Sonnet Interface:**
```python
import anthropic

class ClaudeTranslator:
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"
    
    def translate(self, prompt: str, temperature: float = 0.1) -> str:
        """Translate using Claude 3.5 Sonnet with prompt tuning"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()

# Usage
claude_translator = ClaudeTranslator("your-api-key")
result = claude_translator.translate(prompt)
```

### **3. Complete Pipeline Script**
```python
def translate_with_prompt_tuning(
    english_content: str, 
    target_language: str,
    model_choice: str = "gpt4o"
) -> str:
    """Complete translation pipeline using prompt tuning"""
    
    # Step 1: Apply masking (using your existing preprocessor)
    from generateJSONL_PT import TranslationPreprocessor
    
    preprocessor = TranslationPreprocessor()
    masked_content = preprocessor.process_document(english_content, is_output=False)
    
    # Step 2: Build optimized prompt
    prompt_builder = PromptTuningTranslator(f'dataset-{target_language.lower()[:2]}.jsonl')
    prompt = prompt_builder.build_prompt(masked_content, target_language)
    
    # Step 3: Translate using selected model
    if model_choice == "gpt4o":
        translator = GPT4oTranslator("your-openai-key")
    elif model_choice == "claude":
        translator = ClaudeTranslator("your-anthropic-key")
    
    translated_content = translator.translate(prompt)
    
    # Step 4: Post-process and unmask
    # (You'll need to implement unmasking logic here)
    final_content = unmask_content(translated_content, preprocessor.mapping)
    
    return final_content

# Example usage
english_md = """
{
  "title": "TRANSLATE_THIS: Two-factor authentication setup",
  "summary": "TRANSLATE_THIS: How to setup 2FA"
}

The {{< AppElement type="button" >}} Setup {{< /AppElement >}} button...
"""

french_result = translate_with_prompt_tuning(english_md, "French", "gpt4o")
```

## 🎛️ **Optimization Strategies**

### **1. Prompt Variations for A/B Testing**
```python
PROMPT_TEMPLATES = {
    "detailed": """You are a professional technical translator...[detailed instructions]""",
    "concise": """Translate to {language}, preserve [SHORTCODE_N], remove TRANSLATE_THIS:""",
    "examples_first": """Here are examples:\n{examples}\n\nNow translate:""",
    "rules_first": """Rules:\n1. Preserve shortcodes\n2. Translate marked content\n\nExamples:\n{examples}"""
}

def test_prompt_variations(content: str, target_language: str):
    """Test different prompt templates"""
    results = {}
    for template_name, template in PROMPT_TEMPLATES.items():
        prompt = build_prompt_with_template(content, target_language, template)
        result = translate(prompt)
        results[template_name] = result
    return results
```

### **2. Dynamic Example Selection Enhancement**
```python
def enhanced_example_selection(content: str, examples: List[Dict]) -> List[Dict]:
    """Enhanced example selection based on multiple factors"""
    
    # Factor 1: Content type similarity (changelog vs topic)
    content_type = "changelog" if "/changelog/" in content else "topic"
    
    # Factor 2: Complexity similarity (shortcode count, length)
    content_complexity = calculate_complexity(content)
    
    # Factor 3: Technical term overlap
    content_terms = extract_technical_terms(content)
    
    scored_examples = []
    for ex in examples:
        score = 0
        
        # Type similarity
        ex_type = "changelog" if "/changelog/" in ex['input'] else "topic"
        if content_type == ex_type:
            score += 10
        
        # Complexity similarity
        ex_complexity = calculate_complexity(ex['input'])
        complexity_diff = abs(content_complexity - ex_complexity)
        score += max(0, 10 - complexity_diff)
        
        # Technical term overlap
        ex_terms = extract_technical_terms(ex['input'])
        overlap = len(content_terms.intersection(ex_terms))
        score += overlap * 2
        
        scored_examples.append((score, ex))
    
    scored_examples.sort(key=lambda x: x[0], reverse=True)
    return [ex for _, ex in scored_examples[:4]]
```

## 📊 **Quality Validation for Prompt Tuning**

### **Automated Quality Checks**
```python
def validate_prompt_tuning_output(original: str, translated: str) -> Dict[str, bool]:
    """Validate translation quality for prompt tuning"""
    
    checks = {
        "shortcodes_preserved": validate_shortcode_preservation(original, translated),
        "no_translate_this_markers": "TRANSLATE_THIS:" not in translated,
        "json_structure_valid": validate_json_structure(translated),
        "reasonable_length": 0.5 <= len(translated)/len(original) <= 2.0,
        "contains_translation": len(translated.strip()) > 50
    }
    
    return checks

def batch_quality_test(test_cases: List[str], target_language: str) -> float:
    """Test prompt tuning quality on batch of examples"""
    passed = 0
    total = len(test_cases)
    
    for content in test_cases:
        result = translate_with_prompt_tuning(content, target_language)
        checks = validate_prompt_tuning_output(content, result)
        if all(checks.values()):
            passed += 1
    
    return passed / total
```

## 🎯 **Expected Results with Prompt Tuning**

### **Advantages over Fine-tuning:**
- ✅ **Immediate deployment** - no training time
- ✅ **Easy iteration** - modify prompts instantly
- ✅ **Cost-effective** - no training costs
- ✅ **Latest models** - use cutting-edge capabilities

### **Quality Expectations:**
- **Structure Preservation**: 95%+ (slightly lower than fine-tuning)
- **Translation Quality**: 90%+ (depends on base model capability)
- **Consistency**: Good with temperature=0.1
- **Speed**: Fast inference, no warm-up time

### **When to Use Prompt Tuning vs Fine-tuning:**
- **Prompt Tuning**: Rapid prototyping, testing, lower volume
- **Fine-tuning**: Production scale, maximum consistency, high volume 