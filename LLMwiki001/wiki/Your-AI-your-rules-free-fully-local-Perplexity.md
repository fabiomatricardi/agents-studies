---
title: Your AI your rules - free fully local Perplexity app
created: 2026-04-09
last_updated: 2026-04-09
source_count: 1
status: reviewed
---
This article guides users through setting up Perplexica (now renamed to Vane) - an open-source, self-hosted AI answering engine that functions as a free, privacy-focused alternative to Perplexity AI. It uses SearxNG for web searches and local LLMs via llama.cpp server.

Key takeaways:

## What is Perplexica/Vane?
Open-source AI-powered search engine inspired by Perplexity AI. Features:
- Uses SearxNG for web searches (local, no API key needed)
- Supports local LLMs via Ollama or cloud providers
- Delivers cited answers with source references
- Privacy-focused, runs 100% locally
- Includes focus modes: Academic, YouTube, Reddit, Wolfram Alpha, Writing Assistant
- Search modes: Speed (fast), Balanced (everyday), Quality/Deep Research (thorough analysis)

## Installation via Docker
```bash
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```
Then access at http://localhost:3000/

## Connecting llama.cpp Server
Perplexica doesn't include llama.cpp by default. Steps:

**1. Install llama.cpp binaries**
- Download latest CPU-only binaries from official GitHub

**2. Download model**
- Recommended: Qwen3.5-0.8B-Q6_K.gguf (best for CPU-only users)

**3. Run llama-server**
```bash
.\llama-server.exe -m .\Qwen_Qwen3.5-0.8B-Q6_K.gguf --mmap -ngl 0 -t 2 -c 32288 --host 0.0.0.0 --port 8888 --reasoning-budget -1 -fa on --temp 1.0 --top-k 20 --top-p 0.95 --presence-penalty 1.5 -a qwen3.5-0.8
```

**4. Configure in Perplexica**
- Settings > Models > Manage Connections > + Add Connection
- Choose OpenAI
- Base URL: http://host.docker.internal:8888
- Model name: qwen3.5-0.8 (from -a flag)

**5. Add to Chat models and set as default**

## Best Small Language Models for Perplexica
| Model | Verdict |
|-------|---------|
| Qwen3.5-0.8b | Recommended - best results, needs 25k+ context |
| Qwen3.5-2b | Recommended - thinking model, better but slower |
| Gemma-3n-E2B-it | Good, consistent links, possibly needs uncensored version |
| Granite-4.0-h-tiny | Good, worked in one shot |
| Trinity-Nano-Preview | Good but no reasoning traces |
| LFM-2.5-1.2b-instruct | Not recommended |
| Ministral-3-3B | Not good for this use case |
| Granite-3.1-3b-a800m | Not good, hallucinating |

## Performance Notes
- One query can take up to 30 minutes on old hardware
- High token usage - increase context window to 32k tokens
- Slower than cloud alternatives but free and private
- No surprise bills - runs locally on your hardware

[Source: Your-AI-your-rules-a-free-fully-local-Perplexity]
