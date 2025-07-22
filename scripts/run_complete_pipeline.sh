#!/bin/bash
"""
Complete Soft Prompt Tuning Pipeline

This script demonstrates the complete workflow:
1. Preprocess golden data (masking)
2. Train soft prompts
3. Test inference

Run with: bash scripts/run_complete_pipeline.sh [target_language]
"""

set -e  # Exit on any error

# Configuration
TARGET_LANGUAGE=${1:-"fr"}  # Default to French
CONTENT_DIR="content"
MASKED_DIR="content_masked"
MODEL_DIR="models/soft-prompts-${TARGET_LANGUAGE}"

echo "🚀 Starting Complete Soft Prompt Tuning Pipeline"
echo "=================================================="
echo "Target Language: ${TARGET_LANGUAGE}"
echo "Content Directory: ${CONTENT_DIR}"
echo "Masked Directory: ${MASKED_DIR}"
echo "Model Output: ${MODEL_DIR}"
echo ""

# Step 1: Check if content directory exists
if [ ! -d "${CONTENT_DIR}" ]; then
    echo "❌ Content directory not found: ${CONTENT_DIR}"
    echo "Please ensure your golden dataset is in the content/ directory"
    exit 1
fi

# Step 2: Preprocess golden data
echo "📝 Step 1: Preprocessing golden data..."
echo "======================================="
python scripts/preprocess_golden_data.py \
    --content-dir "${CONTENT_DIR}" \
    --output-dir "${MASKED_DIR}" \
    --languages en "${TARGET_LANGUAGE}" \
    --verbose

if [ $? -ne 0 ]; then
    echo "❌ Preprocessing failed!"
    exit 1
fi

echo ""
echo "✅ Preprocessing completed successfully!"
echo ""

# Step 3: Check GPU availability and recommend settings
echo "🔍 Step 2: Checking GPU setup..."
echo "================================"
python scripts/check_gpu_setup.py

echo ""

# Step 4: Train soft prompts
echo "🧠 Step 3: Training soft prompts..."
echo "==================================="

# Determine device preference
if command -v nvidia-smi >/dev/null 2>&1; then
    echo "NVIDIA GPU detected, using GPU training..."
    DEVICE="gpu"
    BATCH_SIZE=16
    MAX_EXAMPLES=5000
else
    echo "No NVIDIA GPU detected, using CPU training..."
    DEVICE="cpu"
    BATCH_SIZE=4
    MAX_EXAMPLES=1000
fi

# Train the model
python scripts/soft_prompt_tuning.py \
    --content-dir "${MASKED_DIR}" \
    --target-language "${TARGET_LANGUAGE}" \
    --output-dir "${MODEL_DIR}" \
    --device "${DEVICE}" \
    --batch-size "${BATCH_SIZE}" \
    --max-examples "${MAX_EXAMPLES}" \
    --use-masked-data \
    --num-epochs 10

if [ $? -ne 0 ]; then
    echo "❌ Training failed!"
    exit 1
fi

echo ""
echo "✅ Training completed successfully!"
echo ""

# Step 5: Test inference
echo "🧪 Step 4: Testing inference..."
echo "==============================="

# Create a test input
TEST_INPUT="This is a test message with [SHORTCODE_1] and some normal text that should be translated."

echo "Test input: ${TEST_INPUT}"
echo ""

python scripts/soft_prompt_inference.py \
    --model-path "${MODEL_DIR}" \
    --text "${TEST_INPUT}"

if [ $? -ne 0 ]; then
    echo "❌ Inference test failed!"
    exit 1
fi

echo ""
echo "🎉 Complete pipeline finished successfully!"
echo "=========================================="
echo ""
echo "📁 Files created:"
echo "  - Masked data: ${MASKED_DIR}/"
echo "  - Trained model: ${MODEL_DIR}/"
echo "  - Preprocessing summary: ${MASKED_DIR}/preprocessing_summary.json"
echo ""
echo "🔧 Next steps:"
echo "  1. Test your model with real content:"
echo "     python scripts/soft_prompt_inference.py --model-path ${MODEL_DIR} --file your_file.md"
echo ""
echo "  2. Batch translate content:"
echo "     python scripts/soft_prompt_inference.py --model-path ${MODEL_DIR} --batch --content-dir content --output-dir translated"
echo ""
echo "  3. Fine-tune training parameters and retrain if needed"
echo ""
