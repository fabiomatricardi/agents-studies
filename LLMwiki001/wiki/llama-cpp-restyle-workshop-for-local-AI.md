---
title: llama.cpp restyle - workshop for your Local AI
created: 2026-04-09
last_updated: 2026-04-09
source_count: 1
status: reviewed
---
llama.cpp has evolved from a minimalist inference engine into a full-fledged local AI ecosystem. This article covers the restyled components (llama-cli and llama-server) that enable running, routing, and chatting with LLMs locally—all from a single ZIP file.

Key takeaways:

## What is llama.cpp?
Open-source C/C++ library for efficient LLM inference, created by Georgi Gerganov in March 2023. Designed to run large language models on consumer-grade hardware without specialized GPUs. Supports GGUF (quantized) model files.

## Quick Start
```bash
# Download llama.cpp binaries + GGUF model file
.\llama-cli.exe -m .\models\google_gemma-3-270m-it-Q8_0.gguf -c 8192
```

## Two Main Applications

### 1. llama-cli
- Full-fledged terminal application
- Interactive chat session in terminal
- Can /read text files for document Q&A
- One-liner to start chatting

### 2. llama-server
- OpenAI-compatible HTTP server
- Built-in SvelteKit WebUI (ChatGPT-like experience)
- 100% client-side and private—no data leaves your machine
- **Dynamic model switching**: Dropdown to select from all GGUF models in --models-dir
- **Chat history persistence**: Saved locally in browser
- **Hyperparameter control**: Temperature, context length, etc.
- **Multimodal support**: Image and document attachments

## Model Routing (New Feature)
Llama-server now includes router mode for dynamically loading, unloading, and switching between multiple models without restarting:
```bash
llama-server --models-dir ./my-models
```
- Multi-process architecture: each model runs in its own process
- If one model crashes, others remain unaffected
- First request auto-loads the model; subsequent requests are instant

## API Endpoints (OpenAI-Compatible)
```bash
# Chat with a model
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "model-name","messages": [{"role": "user", "content": "Hello!"}]}'

# List available models
curl http://localhost:8080/models

# Load a model
curl -X POST http://localhost:8080/models/load \
  -H "Content-Type: application/json" \
  -d '{"model": "my-model.gguf"}'

# Unload a model
curl -X POST http://localhost:8080/models/unload \
  -H "Content-Type: application/json" \
  -d '{"model": "my-model.gguf"}'
```

## PowerShell Examples
```powershell
# Chat
Invoke-WebRequest -Uri "http://localhost:8080/v1/chat/completions" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"model": "LFM2-1.2B-Q6_K","messages": [{"role": "user", "content": "Hello!"}]}'

# Load model
Invoke-WebRequest -Uri "http://localhost:8080/models/load" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body (@{ model = "LFM2-1.2B-Q6_K" } | ConvertTo-Json -Compress)

# Unload model
Invoke-WebRequest -Uri "http://localhost:8080/models/unload" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body (@{ model = "LFM2-1.2B-Q6_K" } | ConvertTo-Json -Compress)
```

## Key Benefits
- All-in-one ZIP file—extract and run
- OpenAI-compatible API for seamless tool integration
- Privacy-first: 100% local processing
- Multiple models with dynamic switching
- No cloud APIs, expensive GPUs, or complex setups needed

[Source: llama-CPP-restyle-is-the-workshop-for-your-Local-A]
