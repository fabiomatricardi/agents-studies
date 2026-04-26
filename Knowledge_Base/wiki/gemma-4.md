---
title: Gemma 4
created: 2026-04-20
last_updated: 2026-04-20
source_count: 1
status: draft
---

Gemma 4 is Google's newest open-weight model family, released April 2026, focused on stronger reasoning, agentic behavior, and multimodal on-device use. Designed for the "PoorGPUguy" — users with limited hardware who want capable AI without expensive GPUs or cloud subscriptions.

## Model Family Overview

Gemma 4 spans a wide range of sizes and use cases:

| Model | Parameters | Context | Best For |
|-------|------------|---------|----------|
| Gemma-4-E2B | 2B effective | 128K | Phones, Raspberry Pi |
| Gemma-4-E4B | 4B effective | 128K | Old laptops, mini-PCs |
| Gemma-4-26B-A4B | 26B (MoE) | 256K | Desktop with GPU |
| Gemma-4-31B | 31B | 256K | High capability needs |

The "E" prefix denotes edge-optimized models — designed for efficient on-device execution.

## Key Capabilities

### Advanced Reasoning & Thinking Mode
Gemma 4 can do step-by-step reasoning and multi-step planning. Even the small E2B/E4B models support "thinking mode," enabling the model to pause and plan before responding — drastically reducing hallucinations on complex tasks like coding or logic puzzles. [Source: Gemma 4 on the Edge high performance AI for the .txt]

### Long Context Windows
- Edge models (E2B/E4B): Up to 128K tokens
- Large models (26B/31B): Up to 256K tokens

This enables feeding entire technical documentation PDFs into small hardware and getting meaningful answers.

### Multimodal Inputs
All models support text + images with variable aspect ratios. E2B/E4B also natively support audio, and some variants handle video-like sequences.

### Native System Prompt Support
The 4-series introduces built-in system-role handling — the model stays in character and follows constraints much better, even at small sizes. This was the biggest missing feature from Gemma 2.

### Function Calling
Improved coding benchmarks plus built-in function-calling support. Models can call tools and APIs within agentic pipelines without extra fine-tuning.

## Edge Deployment with llama.cpp

### Why llama.cpp?
Gemma 4 edge models run efficiently on consumer hardware using llama.cpp. The E2B and E4B models achieve ~6 tokens/second on old hardware (4-thread CPU, 16GB RAM).

### Setup Process

1. **Download GGUF models** from Unsloth repository on Hugging Face:
   - `gemma-4-E4B-it-Q3_K_S.gguf` (4B active params)
   - `gemma-4-E2B-it-Q4_K_M.gguf` (2B active params)

2. **Download llama.cpp** (latest release required — older versions may not support Gemma 4 architecture)

3. **Run the server**:
   ```
   llama-server.exe -m .\gemma-4-E4B-it-Q4_K_S.gguf -c 64000 -ngl 0 -ctk q4_0 -ctv q4_0 --mmap --temp 1.0 --top-p 0.95 --top-k 64 --port 8888 --host 0.0.0.0
   ```

Key flags:
- `--port 8888`: Listening port for the API
- `--host 0.0.0.0`: Exposes API to local network (Windows will prompt to Allow)

### Performance
On an old $100 mini-PC (Intel 6th gen, 4 threads, 16GB RAM):
- ~6 tokens/second generation speed
- Near-zero-latency offline execution
- Works over WiFi on local network

## Local Network AI Server Setup

### Step 1: Find Your IP Address
Run `ipconfig` (Windows) or `ip addr` (Linux) to get the IPv4 address — e.g., `192.168.1.75`.

### Step 2: Expose to Network
The `--host 0.0.0.0` flag makes the server accessible from other devices on the network.

### Step 3: Access Remotely
From another computer on the same network, access:
- Web UI: `http://192.168.1.75:8888`
- API endpoint: `http://192.168.1.75:8888/v1`

### Use Cases
- Run AI on old hardware, use from main computer
- Share one AI server across household devices
- Keep main computer free for other work

## Integration with Perplexica

Perplexica (local Perplexity alternative) can connect to Gemma 4 via:

1. **Local llama.cpp server** — Add connection in Settings > Models > Add Connection, point to your network address
2. **Google AI Studio API** — Use free API key (1500 calls/day) in Settings > Models > Add Connection

Google AI Studio offers Gemma 4 models for free with a Gmail account — no credit card required.

### Setting Up Google AI Studio API

1. Go to [ai.google.dev](https://ai.google.dev)
2. Sign up with Google account
3. Agree to Gemini API Additional Terms
4. Generate API key
5. Use in Perplexica: Settings > Add Connection > Gemini

The free tier allows 1500 calls/day — sufficient for personal use.

## GPU-Poor Solutions

Gemma 4 embodies the GPU-poor philosophy:

- **Hybrid approach**: Use local E2B/E4B for fast, private tasks; bridge to Google AI Studio API for heavy reasoning (free tier)
- **Hardware archaeology**: Old mini-PCs, laptops, NUCs make perfect dedicated LLM servers
- **Efficiency over brute force**: Edge models run on 4-thread CPUs at useful speeds

## Related Concepts

- [[Local LLMs]]: Self-hosted models category
- [[llama.cpp]]: Inference engine for local running
- [[llama-server]]: Local server with WebUI
- [[GPU-Poor Solutions]]: Strategies for limited hardware
- [[Perplexica]]: Local Perplexity alternative (reference only — no wiki page yet)