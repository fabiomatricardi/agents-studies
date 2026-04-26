---
title: NVIDIA NIM
created: 2026-04-19
last_updated: 2026-04-19
source_count: 1
status: draft
---

NVIDIA NIM (NVIDIA Inference Microservices) provides free API access to 93+ state-of-the-art LLMs including Llama 3.3, Mistral, DeepSeek, and specialized coding/vision models. The free tier offers 1,000 initial credits (expandable to 5,000) or ~40 requests/minute rate limit for development use.

## Free Tier Structure

- **Initial Credits**: 1,000 free API credits upon joining NVIDIA Developer Program
- **Expansion**: Up to 5,000 credits with business email, includes 90-day NVIDIA AI Enterprise license
- **Rate Limits**: ~40 requests/minute for non-production development (mid-2025+)

[Source: Are you too a Poor GPU guy Here s how to run 400B.txt]

## Key Features

- **OpenAI-Compatible API**: Uses standard OpenAI format — just change base_url to `https://integrate.api.nvidia.com/v1`
- **Portability**: Same NIM container runs locally on your own NVIDIA hardware after prototyping
- **Model Diversity**: Text, vision/multimodal, coding (DeepSeek-Coder, Qwen-Coder), and reasoning models

## Integration

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="nvapi-your_API_key"
)
```

## Related Concepts

- [[GPU-Poor Solutions]]: NIM is a key free API solution for those without GPUs
- [[LLM Providers]]: NVIDIA NIM joins OpenRouter as a free API provider
- [[AI Gateways]]: Can be routed through gateways like Bifrost