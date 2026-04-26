---
title: llama-cli
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

llama-cli is the terminal chat application component of llama.cpp. It provides an interactive command-line interface for chatting with LLM models locally.

## Quick Start

```bash
.\llama-cli.exe -m .\models\model.gguf -c 8192
```

This starts a terminal chat session with the specified model and 8192 token context window.

## Features

- Interactive terminal chat
- Load text files and chat with documents
- Support for PDF conversion via pdf_extractor.exe
- Configure hyperparameters via command-line flags
- 100% local - no internet required

## Related Concepts

- [[llama.cpp]]: Parent project
- [[llama-server]]: Alternative component with WebUI