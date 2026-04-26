---
title: The smallest 8B model ever created is not really an advancement
created: 2026-04-09
last_updated: 2026-04-09
source_count: 1
status: reviewed
---
This article critically examines PrismML's Bonsai 8B model - a 1-bit quantized LLM that claims to be a breakthrough in "intelligence density." The author tests it on CPU-only hardware and finds the claims are exaggerated for CPU users.

Key takeaways:

## What is Bonsai (PrismML's 1-bit model)
- 8.2 billion parameters quantized to true 1-bit (+1 or -1)
- Requires only 1.15 GB of memory
- Claims: 14x smaller, 8x faster, 4-5x more energy efficient
- Benchmarks: 70.5 average score, matching Qwen3 8B or Llama 3.1 8B
- Targets: iPhones (44 t/s on iPhone 17 Pro Max), Macs, edge devices
- Licensed: Apache 2.0, available in GGUF/MLX formats

## The Claimed Innovation
"Intelligence Density" - concentrating intelligence per unit of size/power:
- 1-bit quantization historically degrades reasoning
- PrismML's Caltech-derived method claims to preserve capability via advanced compression
- Shifts "intelligence vs size" Pareto frontier

## The Reality Check (CPU-only testing)

**Author's test on Lenovo X260 (2016, CPU only):**
| Model | RAM Usage | Prefill Speed | Generation Speed |
|-------|-----------|---------------|------------------|
| Bonsai-8B (1-bit) | 1.1 GB | 2.6 t/s | 2.4 t/s |
| Qwen3.5-9B (Q4_K_M) | 4.2 GB | 2.9 t/s | 1.9 t/s |

**Conclusion**: "It doesn't look that big the difference, isn't it?"

## Why CPU Support is Poor
- **x86 CPU kernels fail**: Q1_0_g128 kernels produce "garbage output" at ~1 t/s
- **No official CPU benchmarks**: All PrismML benchmarks focus on GPU/Apple Metal (e.g., 368 t/s on RTX 4090)
- **Context length overhead**: CPU runs hit bugs and extra RAM costs
- **Windows 11 CPU build**: Loads but outputs nonsense
- **Mature CPU support**: Standard Q4_K_M (~4.5 GB) is optimized with x86/AVX kernels, yielding 5-20 t/s

## Forks to Enable CPU Support
1. **PrismML-Eng/llama.cpp**: Original fork with Q1_0_g128 kernels (GPU-focused)
2. **philtomson/llama.cpp**: Fork that adds AVX2, AVX512, and ROCm for AMD GPUs

## The Author's Verdict
- **On GPU**: Claims hold up - works well on RTX 4090, Apple Silicon
- **On CPU**: No real improvement over standard quantization
- **The problem**: "Until CPU can perform at the same level of GPUs, this kind of AI will always be in the hands of the few"

## Critical Takeaway
Don't trust blind claims - verify yourself. The gap between GPU benchmarks and CPU reality is significant. For CPU-poor users, standard Q4_K_M quantization may be a better choice than 1-bit models.

[Source: The-smallest-8B-model-ever-created-is-not-really-a]
