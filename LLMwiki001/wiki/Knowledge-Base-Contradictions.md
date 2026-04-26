---
title: Knowledge Base Contradictions
created: 2026-04-09
last_updated: 2026-04-09
source_count: 0
status: draft
---
This page tracks apparent contradictions between knowledge base sources.

## 1. Quantization Speed Claims

### Claim A: ByteShape Special Quants (January-2026-AI-discoveries)
- **Content**: Qwen3-4B with ByteShape Q3_K_S bpw quantization shows dramatic speedups: 10→21 tokens/sec generation (2x faster)
- **Source**: [[January-2026-AI-discoveries]]

### Claim B: 1-bit Bonsai vs Q4_K_M (The-smallest-8B-model-not-really-advancement)
- **Content**: Bonsai 8B (1-bit) = 2.4 t/s vs Qwen3.5-9B (Q4_K_M) = 1.9 t/s — "minimal difference"
- **Source**: [[The-smallest-8B-model-not-really-advancement]]

### Resolution
These are NOT actually contradicting:
- **ByteShape quants** are specialized Q3_K_S "bits per weight" (bpw) format — still 3-bit, NOT 1-bit
- **1-bit Bonsai** uses true 1-bit quantization (Q1_0_g128)
- The 2x speedup is only achievable with bpw quants on CPU, NOT with 1-bit models

> CONTRADICTION CLARIFIED: ByteShape's "special quants" are different from 1-bit models. The 2x speedup claim applies to bpw formats, not to Bonsai-style 1-bit quantization. [Source: Your-CPU-is-NOT-Broken-GGUF-quantization]

## 2. Model Size vs Speed Assumptions

### Assumption in Many Articles
- Smaller model = faster on CPU

### Reality (Your-CPU-is-NOT-Broken-GGUF-quantization)
- IQ formats (smaller file) can be SLOWER than K-quant (larger file)
- Example: UD-IQ2_XXS (smallest) is slowest; Q3_K_S or Q4_K_S is fastest
- **Key insight**: "You don't need the smallest file. You need the right format."

> CONTRADICTION CLARIFIED: Common assumption (smaller = faster) is FALSE for IQ formats on CPU. K-quant formats are optimized for CPU, IQ for GPU.

## 3. "Best Small Language Models" Recommendations

### Gemma-4-on-the-Edge
- Recommends Gemma 4 E2B/E4B for edge devices

### Your-AI-your-rules-free-fully-local-Perplexity
- Tested Gemma-3n-E2B-it for Perplexica: "overall quite good, but does not get the right results in one shot"
- Recommends Qwen3.5-0.8b as "smallest and surprisingly one of the best"

> NOT A CONTRADICTION: Different use cases (general edge AI vs Perplexica search). Qwen3.5 excels at reasoning/tool-calling needed for Perplexica; Gemma may work better for general tasks.

## Summary
The knowledge base is internally consistent when examined carefully. Key clarifications:
1. ByteShape quants ≠ 1-bit models — different technologies
2. Smaller file ≠ faster — IQ formats fail on CPU, use Q4_K_M
3. "Best model" depends on use case — Perplexica needs reasoning; general use may differ

[Source synthesis: All 12 knowledge base sources reviewed for contradictions]
