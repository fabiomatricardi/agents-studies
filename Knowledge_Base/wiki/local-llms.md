---
title: Local LLMs
created: 2026-04-18
last_updated: 2026-04-18
source_count: 2
status: draft
---

Local LLMs are large language models that run on personal hardware instead of cloud APIs. They provide privacy, cost control, and offline capability for AI workloads.

## Running Local LLMs

### llama.cpp
Open-source C/C++ library for efficient LLM inference on consumer hardware. Provides llama-cli (terminal) and llama-server (WebUI/API).

### Gemma 4
Google's edge-optimized open-weight model family (E2B/E4B) designed for phones, Raspberry Pi, and old mini-PCs. Supports 128K context, thinking mode, and multimodal inputs. Achieves ~6 tokens/second on 4-thread CPUs. [Source: Gemma 4 on the Edge high performance AI for the .txt]

### vLLM
High-performance inference server for production workloads.

### Ollama
User-friendly local model runner with model library.

## GGUF Format

GGUF (GGML Unified Format) is the standard quantized model format used by llama.cpp. Quantization reduces model size while preserving quality.

## Getting Started

1. Download llama.cpp binaries for your OS
2. Download a GGUF model (e.g., from Hugging Face)
3. Run locally with no internet required

## Related Concepts

- [[llama.cpp]]: Primary tool for running local LLMs
- [[llama-cli]]: Terminal interface
- [[llama-server]]: Local server with WebUI
- [[LLM Providers]]: Cloud alternatives
- [[Hierarchical Reasoning Model]]: Tiny 27M parameter model that runs on a single GPU, proving architecture matters more than size
- [[Gemma 4]]: Google's edge-optimized models for limited hardware