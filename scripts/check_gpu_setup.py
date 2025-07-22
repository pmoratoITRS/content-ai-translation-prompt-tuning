#!/usr/bin/env python3
"""
GPU Setup Verification Script

This script checks if your environment is properly configured for GPU training.
Run this before starting training to verify your setup.
"""

import torch
import sys
from torch.cuda.amp import autocast, GradScaler


def check_pytorch_version():
    """Check PyTorch version"""
    print(f"🔍 PyTorch version: {torch.__version__}")
    if torch.__version__ < "1.12.0":
        print("⚠️  Warning: PyTorch version is older than 1.12.0")
        print("   Consider upgrading for better performance")
    else:
        print("✅ PyTorch version is compatible")


def check_cuda_availability():
    """Check CUDA availability and version"""
    if torch.cuda.is_available():
        print(f"✅ CUDA is available")
        print(f"   CUDA version: {torch.version.cuda}")
        print(f"   GPU count: {torch.cuda.device_count()}")
        
        for i in range(torch.cuda.device_count()):
            gpu_props = torch.cuda.get_device_properties(i)
            memory_gb = gpu_props.total_memory / 1024**3
            print(f"   GPU {i}: {gpu_props.name} ({memory_gb:.1f}GB)")
        
        return True
    else:
        print("❌ CUDA is not available")
        print("   Training will run on CPU (much slower)")
        return False


def check_mixed_precision():
    """Check mixed precision support"""
    try:
        # Test autocast
        with autocast():
            x = torch.randn(2, 3, device='cuda' if torch.cuda.is_available() else 'cpu')
            y = x * 2
        
        # Test GradScaler
        scaler = GradScaler()
        print("✅ Mixed precision (AMP) is supported")
        return True
    except Exception as e:
        print(f"❌ Mixed precision test failed: {e}")
        return False


def check_memory_efficiency():
    """Test memory efficiency features"""
    if torch.cuda.is_available():
        print("\n🧪 Testing GPU memory features:")
        
        # Test memory pinning
        try:
            x = torch.randn(1000, 1000, pin_memory=True)
            print("✅ Memory pinning works")
        except Exception as e:
            print(f"⚠️  Memory pinning issue: {e}")
        
        # Test non_blocking transfer
        try:
            if torch.cuda.is_available():
                x = torch.randn(100, 100)
                x_gpu = x.to('cuda', non_blocking=True)
                print("✅ Non-blocking GPU transfer works")
        except Exception as e:
            print(f"⚠️  Non-blocking transfer issue: {e}")


def recommend_settings():
    """Recommend optimal settings based on hardware"""
    print("\n💡 Device Selection Options:")
    print("   --device auto     # Auto-detect best device (default)")
    print("   --device gpu      # Force GPU if available") 
    print("   --device cpu      # Force CPU training")
    print("   --force-cpu       # Force CPU even if GPU available")
    
    if not torch.cuda.is_available():
        print("\n💡 Recommended CPU settings (auto-adjusted when using --device cpu):")
        print("   --device cpu")
        print("   # Additional optimizations:")
        print("   --batch-size 2")
        print("   --gradient-accumulation-steps 2") 
        print("   --max-examples 500")
        print("   --dataloader-workers 2")
        return
    
    gpu_memory_gb = torch.cuda.get_device_properties(0).total_memory / 1024**3
    
    print(f"\n💡 Recommended GPU settings for {gpu_memory_gb:.1f}GB GPU:")
    print("   --device gpu      # Or use --device auto (default)")
    
    if gpu_memory_gb < 8:
        print("   # Conservative settings for smaller GPU")
        print("   --batch-size 8")
        print("   --gradient-accumulation-steps 4")
        print("   --max-length 512")
        print("   --max-examples 3000")
    elif gpu_memory_gb < 16:
        print("   # Standard settings (these are now the defaults)")
        print("   --batch-size 16") 
        print("   --gradient-accumulation-steps 2")
        print("   --max-length 1024")
        print("   --max-examples 5000")
    else:
        print("   # High-performance settings")
        print("   --batch-size 32")
        print("   --gradient-accumulation-steps 1") 
        print("   --max-length 1024")
        print("   --max-examples 10000")
    
    print("   --dataloader-workers 4")
    if check_mixed_precision():
        print("   # Mixed precision enabled by default")
    else:
        print("   --no-mixed-precision")


def main():
    print("🚀 GPU Setup Verification for Soft Prompt Tuning")
    print("=" * 50)
    
    check_pytorch_version()
    print()
    
    cuda_available = check_cuda_availability()
    print()
    
    if cuda_available:
        check_mixed_precision()
        check_memory_efficiency()
    
    recommend_settings()
    
    print("\n" + "=" * 50)
    if cuda_available:
        print("🎯 Your system is ready for GPU training!")
        print("Run the training script with the recommended settings above.")
    else:
        print("⚠️  GPU not available. Training will be slower on CPU.")
        print("Consider using a machine with NVIDIA GPU for better performance.")


if __name__ == "__main__":
    main() 