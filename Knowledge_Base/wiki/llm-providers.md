---
title: LLM Providers
created: 2026-04-17
last_updated: 2026-04-17
source_count: 1
status: draft
---

LLM providers are services that offer access to large language models via API. They each have their own strengths, pricing models, and limitations.

## Major Providers

- OpenAI (GPT models)
- Anthropic (Claude models)
- Google Gemini
- AWS Bedrock
- Azure OpenAI
- Groq (fast inference)
- OpenRouter (aggregates multiple providers)
- NVIDIA NIM (free API for 93+ models)

## Integration with AI Gateways

[[AI Gateways]] like [[Bifrost]] provide a unified interface to connect to multiple LLM providers simultaneously. This allows:
- Automatic failover when one provider fails
- Rate limiting per provider
- Cost optimization by routing to cheaper options
- Testing different models without code changes

## Self-Hosted Options

- [[Local LLMs]]: Models like llama.cpp running on personal hardware
- vLLM: High-performance inference server
- Ollama: User-friendly local model runner

## Related Concepts

- [[AI Gateways]]: Unified interface for multiple providers
- [[Bifrost]]: Specific gateway implementation
- [[Local LLMs]]: Alternative to API-based providers
- [[NVIDIA NIM]]: Free API provider option