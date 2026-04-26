---
title: Bifrost
created: 2026-04-17
last_updated: 2026-04-17
source_count: 1
status: draft
---

Bifrost is an open-source AI gateway developed by Maxim that serves as a unified entry point for routing LLM traffic across multiple providers. It provides automatic fallback switching when providers fail or hit rate limits, budget controls at multiple levels (provider, key, virtual key), and claims 40x performance improvement over LiteLLM with 11μs overhead at 5,000 RPS. The gateway runs locally and provides a web dashboard for configuration, supporting providers including OpenAI, Anthropic, AWS Bedrock, Google Vertex, Azure, and self-hosted instances like llama.cpp. [Source: Bifrost CLI is the AI gateway for coding agents we.txt]

## Key Concepts

- [[AI Gateways]]: Unified interfaces for routing traffic across multiple LLM providers
- [[Bifrost-CLI]]: Companion CLI tool for zero-config setup of coding agents
- [[LLM Providers]]: Services like OpenAI, Anthropic, Groq that provide LLM APIs
- [[Local LLMs]]: Self-hosted models like llama.cpp running on personal hardware
- [[Coding Agents]]: AI assistants like Claude Code, Opencode that can execute coding tasks

## Features

### Automatic Fallbacks
When the primary provider fails, hits rate limits, or runs out of credits, Bifrost automatically routes requests to configured fallback providers. This is transparent to the application.

### Budget & Rate Limits
Control spending at multiple levels:
- Per provider: limit spend on each LLM service
- Per key: control spending for specific API keys
- Per virtual key: set budgets for different teams/projects

### Performance
Built in Go, optimized for high throughput with 11μs overhead at 5K RPS - 40x faster than LiteLLM.

### Compatibility
Works with existing OpenAI SDKs - just change the base URL to point to Bifrost instead of the provider directly.

## Use Cases

**Personal/Hobbyist**: Experiment with different models (Claude vs Gemini vs GPT) without code changes. Route traffic to different providers to compare quality vs cost.

**Enterprise**: Set up virtual keys for different teams/departments with separate rate limits and budget caps. Ensure 24/7 availability with multi-provider fallbacks.

## Related Tools

- [[Bifrost-CLI]]: Terminal tool that connects coding agents (Claude Code, Codex CLI, Gemini CLI, Opencode) to Bifrost with zero manual configuration
- [[Opencode]]: Coding agent that can be launched via Bifrost-CLI
- [[LiteLLM]]: Alternative AI gateway solution
- [[llama.cpp]]: Local LLM server that can integrate with Bifrost as an Ollama-compatible endpoint