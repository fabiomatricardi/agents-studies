---
title: Research Roadmap
created: 2026-04-09
last_updated: 2026-04-09
source_count: 0
status: draft
---
This page maps out logical next research directions based on current knowledge base gaps.

## High Priority (Aligns with Focus Areas)

### 1. RAG Implementation Guide
- **Why**: Retrieval-Augmented Generation is a major use case not covered
- **Current mentions**: Perplexica uses SearxNG for search, but no dedicated RAG page
- **Related pages**: [[Your-AI-your-rules-free-fully-local-Perplexity]]

### 2. Local Model Comparison Matrix
- **Why**: Multiple sources test different models (Qwen, Gemma, Granite, LFM) but no consolidated view
- **Current data**:
  - Qwen3.5-0.8b: Best for Perplexica, reasoning [Source: Your-AI-your-rules-free-fully-local-Perplexity]
  - Gemma 4 E2B/E4B: Edge-optimized [Source: Gemma-4-on-the-Edge]
  - Granite 4.0-h-tiny: Good but link issues [Source: Your-AI-your-rules-free-fully-local-Perplexity]
  - ByteSpeed quants: 2x faster [Source: January-2026-AI-discoveries]

### 3. Agent Frameworks Deep Dive
- **Why**: Focus area mentions "Generative AI on the Edge" — agents are key
- **Current mentions**: Opencode (multiple), Bifrost-CLI for agents
- **Gap**: No comparison of local-capable agents (Opencode, Claude Code, etc.)

## Medium Priority

### 4. Fine-tuning Locally
- **Why**: Not covered at all in knowledge base
- **Would extend**: [[AI-Frankenstein-is-alive-part-1]] (architecture knowledge)

### 5. Alternative Local UIs
- **Why**: llama.cpp mentioned but LM Studio, Ollama, text-generation-webui not covered
- **Would extend**: [[llama-cpp-restyle-workshop-for-local-AI]]

### 6. vLLM for Efficient Inference
- **Why**: Different from llama.cpp (more efficient on GPU)
- **Related to**: [[Your-CPU-is-NOT-Broken-GGUF-quantization]] (quantization deep dive)

## Current Coverage Map
| Area | Coverage | Gap |
|------|----------|-----|
| Free APIs | Good (NIM, Google AI) | Could add more |
| Local inference engines | llama.cpp only | vLLM, Ollama |
| Models tested | Scattered in articles | Need matrix |
| Agent tools | Minimal | Opencode deep dive |
| RAG | None | Perplexica-style guides |
| Quantization | Part 1 only | Parts 2-5 referenced |

## Suggested Next Sources
Based on AGENTS.md focus (AI, GenAI Edge, GPU-poor):
1. Find source on local RAG implementation
2. Find source comparing Ollama vs llama.cpp
3. Find source on fine-tuning small models
4. Find source on running agents locally (beyond Opencode)

[Source synthesis: All 13 wiki pages reviewed for gaps]
