# Multilingual Technical Translation with Prompt Tuning

## Overview
This project implements a sophisticated translation system for technical documentation using prompt tuning/fine-tuning to preserve Hugo shortcodes and maintain translation quality.

## Model Selection & Approach

### Primary Recommendation: OpenAI GPT-4o Fine-tuning

**Rationale:**
- Superior multilingual capabilities (EN→FR/DE/NL)
- Excellent structure preservation with complex masking
- Fine-tuning support for domain-specific learning
- Consistent output format for post-processing
- Strong technical documentation understanding

### Dataset Characteristics
- **Size**: 345 examples per language (1,035 total)
- **Complexity**: ~7 shortcodes + ~7 translation markers per example
- **Quality**: Professional human translations
- **Domain**: Technical documentation (Hugo-based)

## Implementation Workflow

### Phase 1: Fine-tuning Setup
1. **Prepare datasets** using `generateJSONL_PT.py`
2. **Upload to OpenAI** for fine-tuning
3. **Train separate models** for each language or single multilingual model
4. **Evaluate performance** on validation set

### Phase 2: Inference Pipeline
```
English Content → Masking → Fine-tuned Model → Translated Output → Unmasking → Final Content
```

### Phase 3: Quality Assurance
- Structure preservation validation
- Translation quality assessment
- A/B testing against baseline

## Alternative Approaches

### Backup Option 1: Claude 3.5 Sonnet + Few-shot
- Use 5-10 examples in prompt for each translation
- Good for immediate testing without fine-tuning costs
- Requires careful prompt engineering

### Backup Option 2: GPT-3.5-turbo Fine-tuning
- More cost-effective option
- May require larger dataset for same quality
- Good for budget-conscious implementations

## Expected Outcomes
- **Structure Accuracy**: 99%+ preservation of shortcodes and formatting
- **Translation Quality**: Human-level accuracy for technical content
- **Consistency**: Reliable output format for automated post-processing
- **Scalability**: Handles complex technical documentation reliably