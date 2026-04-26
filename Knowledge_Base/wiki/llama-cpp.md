---
title: llama.cpp
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

llama.cpp is an open-source C/C++ library for efficient LLM inference on consumer-grade hardware without requiring specialized GPUs. Created by Georgi Gerganov in March 2023, it enables anyone with a computer to run large language models locally. [Source: llama CPP restyle is the workshop for your Local A.txt]

## What It Is

A high-performance inference engine built on the ggml (General-purpose GPU Machine Learning) tensor library. It runs LLMs efficiently on CPUs and GPUs, making powerful AI accessible without expensive cloud infrastructure.

## Key Components

### llama-cli
Terminal chat application that can load text files and chat with documents locally. Quick start:
```
.\llama-cli.exe -m .\models\model.gguf -c 8192
```

### llama-server
Local HTTP server with OpenAI API-compatible endpoints. Features:
- Built-in SvelteKit WebUI (ChatGPT-like, fully local)
- Model routing: dynamic load/unload/switch between models
- 100% private - no data leaves your machine
- Hyperparameter control, chat history, multimodal support

## Why It Matters

- Makes powerful AI accessible without cloud APIs or expensive GPUs
- Every token processed locally - ideal for privacy-sensitive use cases
- OpenAI-compatible API means existing tools integrate seamlessly
- Single ZIP file - no complex setup required

## Related Concepts

- [[Local LLMs]]: Category of self-hosted models
- [[llama-cli]]: Terminal interface component
- [[llama-server]]: Local server component
- [[Bifrost]]: Can route to llama.cpp as Ollama-compatible endpoint