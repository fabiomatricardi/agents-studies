---
title: AI Gateways
created: 2026-04-17
last_updated: 2026-04-17
source_count: 1
status: draft
---

An AI gateway is middleware that sits between applications and LLM providers, acting as a unified interface for routing requests across multiple LLM services.

## Why Use an AI Gateway

Without a gateway, each app makes direct calls to providers (OpenAI, Anthropic, etc.). When a provider goes down or hits rate limits, the app crashes. Gateways solve this by:

1. **Unified Interface**: Single API endpoint for all LLM traffic regardless of provider
2. **Automatic Failover**: Switch to backup providers when primary fails
3. **Cost Control**: Budget limits at provider, key, or team levels
4. **Observability**: Monitor usage, latency, and costs across providers

## Examples

- [[Bifrost]]: Open-source gateway with 40x faster performance than LiteLLM
- [[LiteLLM]]: Popular open-source proxy with standardized API

## Architecture

Applications send requests to the gateway → gateway applies routing rules → forwards to selected provider → returns response to app. All provider-specific logic is handled by the gateway.

## Related Concepts

- [[LLM Providers]]: Services like OpenAI, Anthropic that provide LLM APIs
- [[Local LLMs]]: Self-hosted models that can also be routed through gateways