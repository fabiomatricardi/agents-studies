---
title: llama-server
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

llama-server is the local HTTP server component of llama.cpp. It provides OpenAI API-compatible endpoints and a built-in WebUI for chatting with models in your browser.

## Starting the Server

```bash
.\llama-server.exe --models-dir .\models\
```

Then open http://127.0.0.1:8080 in your browser.

## Features

- Built-in SvelteKit WebUI - ChatGPT-like interface
- Model routing - dynamic load/unload/switch between multiple models
- Full OpenAI API compatibility (/v1/chat/completions, /v1/models)
- 100% client-side and private - no data leaves your machine
- Chat history persistence (saved locally in browser)
- Hyperparameter control (temperature, context length)
- Multimodal support (images, documents, PDFs)
- Multi-process architecture - one model crash doesn't affect others

## API Endpoints

- `POST /v1/chat/completions` - Chat with a model
- `GET /v1/models` - List available models
- `POST /v1/models/load` - Load a model
- `POST /v1/models/unload` - Unload a model to free memory

## Related Concepts

- [[llama.cpp]]: Parent project
- [[llama-cli]]: Terminal interface alternative
- [[Local LLMs]]: Category of self-hosted models