# Implementation Guide: Fine-tuning for Multilingual Translation

## 🎯 **RECOMMENDED APPROACH: Single Multilingual Model**

### Why Single Model vs. Separate Models?

**✅ Single Multilingual Model (Recommended):**
```json
{
  "input": "Translate English to French:\n\n{content with masking}",
  "output": "{french translation with preserved masking}"
}
{
  "input": "Translate English to German:\n\n{content with masking}",
  "output": "{german translation with preserved masking}"
}
```

**Benefits:**
- More training data per model (1,035 examples vs 345)
- Better generalization across languages
- Easier deployment and maintenance
- Cost-effective (1 model vs 3)

## 🚀 **Step-by-Step Implementation**

### Step 1: Prepare Combined Dataset
```bash
# Combine all language datasets
cd /path/to/content-ai-translation
python3 -c "
import json

# Combine datasets
combined_data = []
languages = [('fr', 'French'), ('de', 'German'), ('nl', 'Dutch')]

for lang_code, lang_name in languages:
    with open(f'dataset-{lang_code}.jsonl', 'r') as f:
        for line in f:
            data = json.loads(line)
            # Ensure instruction includes target language
            if not data['input'].startswith(f'Translate English to {lang_name}:'):
                data['input'] = f'Translate English to {lang_name}:\n\n' + data['input'].split('\n\n', 1)[1]
            combined_data.append(data)

# Save combined dataset
with open('combined_multilingual_dataset.jsonl', 'w') as f:
    for item in combined_data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f'Combined dataset created: {len(combined_data)} examples')
"
```

### Step 2: Create Train/Validation Split
```python
# Create 90/10 split for training/validation
import json
import random

with open('combined_multilingual_dataset.jsonl', 'r') as f:
    data = [json.loads(line) for line in f]

random.seed(42)
random.shuffle(data)

split_point = int(len(data) * 0.9)
train_data = data[:split_point]
val_data = data[split_point:]

with open('train_multilingual.jsonl', 'w') as f:
    for item in train_data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

with open('val_multilingual.jsonl', 'w') as f:
    for item in val_data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"Training: {len(train_data)}, Validation: {len(val_data)}")
```

### Step 3: Upload and Fine-tune (OpenAI API)
```python
import openai

# Upload training file
with open('train_multilingual.jsonl', 'rb') as f:
    training_file = openai.File.create(
        file=f,
        purpose='fine-tune'
    )

# Upload validation file
with open('val_multilingual.jsonl', 'rb') as f:
    validation_file = openai.File.create(
        file=f,
        purpose='fine-tune'
    )

# Create fine-tuning job
fine_tune_job = openai.FineTuningJob.create(
    training_file=training_file.id,
    validation_file=validation_file.id,
    model="gpt-4o-2024-08-06",  # Latest GPT-4o model
    hyperparameters={
        "n_epochs": 3,  # Start with 3 epochs
        "batch_size": 1,
        "learning_rate_multiplier": 0.1
    }
)

print(f"Fine-tuning job created: {fine_tune_job.id}")
```

### Step 4: Inference Script
```python
def translate_content(content, target_language, model_id):
    """
    Translate masked content using fine-tuned model
    
    Args:
        content: English content with masking applied
        target_language: 'French', 'German', or 'Dutch'
        model_id: Your fine-tuned model ID
    """
    
    prompt = f"Translate English to {target_language}:\n\n{content}"
    
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,  # Low temperature for consistency
        max_tokens=2000
    )
    
    return response.choices[0].message.content

# Example usage
english_content = """
{
  "title": "TRANSLATE_THIS: Two-factor authentication setup",
  "summary": "TRANSLATE_THIS: How to setup two-factor authentication (2FA)"
}

The [TRANSLATE_THIS: account administrator]([SHORTCODE_1]) needs to configure settings.
"""

french_result = translate_content(english_content, "French", "ft:gpt-4o:your-org:model-name")
```

## 🔍 **Quality Validation Strategy**

### 1. Structure Preservation Test
```python
def validate_structure(original, translated):
    """Ensure all shortcodes are preserved"""
    import re
    
    original_shortcodes = set(re.findall(r'\[SHORTCODE_\d+\]', original))
    translated_shortcodes = set(re.findall(r'\[SHORTCODE_\d+\]', translated))
    
    return original_shortcodes == translated_shortcodes

### 2. Translation Quality Metrics
- BLEU score against human translations
- Manual evaluation of technical terminology
- Consistency checks across similar content

### 3. End-to-End Pipeline Test
1. Mask original content → 2. Translate → 3. Unmask → 4. Compare structure
```

## 🎛️ **Hyperparameter Recommendations**

### For Your Dataset Size (1,035 examples):
- **Epochs**: 3-5 (start with 3)
- **Batch Size**: 1-2 
- **Learning Rate**: 0.1-0.3x default
- **Temperature**: 0.1 (for consistency)

### Cost Estimation:
- **Training**: ~$100-200 for GPT-4o fine-tuning
- **Inference**: ~$0.01-0.02 per translation (depending on length)

## 🛡️ **Fallback Strategy**

If fine-tuning doesn't meet quality thresholds:

1. **Increase dataset size** (aim for 500+ examples per language)
2. **Try few-shot prompting** with Claude 3.5 Sonnet
3. **Hybrid approach**: Fine-tune + few-shot examples
4. **Ensemble**: Combine multiple model outputs 