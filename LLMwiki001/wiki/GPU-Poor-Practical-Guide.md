---
title: GPU-Poor Practical Guide
created: 2026-04-09
last_updated: 2026-04-09
source_count: 0
status: draft
---
This page consolidates options for running AI locally without a dedicated GPU, synthesized from the knowledge base sources.

## The Reality for CPU-Only Users
Your CPU is NOT broken — it's about choosing the right format and tools. [Source: Your-CPU-is-NOT-Broken-GGUF-quantization]

## Options by Use Case

### 1. Free API Access (No Local Hardware)
- **NVIDIA NIM**: Up to 5,000 free credits, 93+ models including Llama 3.3, DeepSeek, Gemma [Source: Are-you-too-a-Poor-GPU-guy-Heres-how-to-run-400B-parameter-Models-for-free]
- **Google AI Studio**: 1,500 calls/day free for Gemma 4 models [Source: Gemma-4-on-the-Edge]

### 2. Local Running on Old Hardware
- **Best quantization format**: Q4_K_M — CPU-optimized kernels, retains 96% quality [Source: Your-CPU-is-NOT-Broken-GGUF-quantization]
- **Recommended models for CPU**:
  - Qwen3.5-0.8B (fastest, best results) [Source: Your-AI-your-rules-free-fully-local-Perplexity]
  - Qwen3.5-2B (thinking model, slightly slower) [Source: Your-AI-your-rules-free-fully-local-Perplexity]
  - Gemma 4 E2B/E4B (edge-optimized) [Source: Gemma-4-on-the-Edge]

### 3. 1-Bit Models (Warning)
- **Bonsai 8B claims**: 14x smaller, 8x faster
- **Reality**: On CPU-only, only 2.4 t/s vs 1.9 t/s for Q4_K_M — minimal difference [Source: The-smallest-8B-model-not-really-advancement]
- CPU kernels for 1-bit formats are immature; stick with Q4_K_M

### 4. Local AI Search (Perplexity Alternative)
- **Perplexica/Vane + llama.cpp**: Free, privacy-focused, runs locally [Source: Your-AI-your-rules-free-fully-local-Perplexity]
- Uses SearxNG for web search
- Best with Qwen3.5-0.8B model

## Quick Start Command (Windows)
```powershell
# 1. Download llama.cpp binaries
# 2. Download Qwen3.5-0.8B-Q6_K.gguf
# 3. Run:
.\llama-server.exe -m .\models\Qwen3.5-0.8B-Q6_K.gguf -c 4096 -ngl 0 --temp 1.0 --top-p 0.95
```

## Key Takeaways
1. Don't chase the smallest file — chase the right format (Q4_K_M)
2. IQ formats are for GPUs; K-quant is for CPUs
3. Free APIs exist (NVIDIA NIM, Google AI Studio) if local isn't fast enough
4. 30-minute queries on old hardware are normal — it's the trade-off for free/private

[Source synthesis: Combined from all 12 knowledge base sources]
