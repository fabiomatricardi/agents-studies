---
title: GPU-Poor Solutions
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

GPU-Poor Solutions covers strategies and technologies for running capable AI on limited or no GPU hardware. This is a focus area for the knowledge base — powerful AI doesn't require expensive hardware.

## Why It Matters

Most AI deployment guidance assumes access to expensive GPUs. But:
- Consumer hardware is limited
- Cloud costs add up
- Privacy benefits of local AI require feasible local running

## Strategies

### 1. Model Architecture

**Hierarchical Reasoning Model (HRM)** — 27M parameters matching or exceeding large models on reasoning tasks. Trains in 2 GPU hours, runs on a single GPU. [Source: Hierarchical Reasoning Model.md]

Key insight: Architecture matters more than size.

### 2. Edge-Optimized Models

**Gemma 4 (E2B/E4B)** — Google's edge-optimized models (2B/4B effective parameters) that run on phones, Raspberry Pi, and old mini-PCs. Supports 128K context, thinking mode, and multimodal inputs. Achieves ~6 tokens/second on 4-thread CPUs. [Source: Gemma 4 on the Edge high performance AI for the .txt]

### 2. Quantization

Reduce model precision (FP16 → INT8 → INT4 → INT2) to shrink size while preserving capability.

- **GGUF format** — Standard quantized format for llama.cpp
- **1-bit "bitnets"** — Extremely quantized models

### 3. Efficient Inference

- **llama.cpp** — C/C++ inference library optimized for CPU
- **llama-server** — Local server with dynamic model loading
- **vLLM** — High-performance inference server (for when you do have a GPU)

### 4. Edge AI

HRM demonstrates that reasoning tasks can run on:
- Autonomous drones
- Lightweight diagnostic devices
- Real-time robotics
- Remote sensing systems

### 5. Free APIs

- **NVIDIA NIM** — Free API access to 93+ frontier models (Llama 3.3, Mistral, DeepSeek)
- **OpenRouter** — Aggregates multiple free and paid providers

### 6. Local Model Runners

- **Ollama** — User-friendly model library
- **llama-cli** — Terminal interface
- **llama-server** — WebUI/API

## Comparison

| Approach | Hardware | Best For |
|----------|----------|----------|
| HRM | Single GPU | Reasoning tasks |
| Gemma 4 E2B/E4B | 4-thread CPU | Edge AI, old hardware |
| NVIDIA NIM | API (free) | Frontier models (no hardware) |
| Quantized GGUF | CPU/Multi-core | General text |
| llama.cpp | CPU | Production inference |
| Ollama | CPU/GPU | Ease of use |
| vLLM | GPU server | High throughput |

## Related Concepts

- [[Local LLMs]]: Running AI locally
- [[llama.cpp]]: Inference engine
- [[Hierarchical Reasoning Model]]: Architecture breakthrough
- [[GGUF Format]]: Quantized model format
- [[NVIDIA NIM]]: Free API for 93+ frontier models