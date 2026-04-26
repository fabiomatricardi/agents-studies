---
title: Your CPU is NOT Broken - the hidden Truth about GGUF quantization
created: 2026-04-09
last_updated: 2026-04-09
source_count: 1
status: reviewed
---
This article explains the often misunderstood relationship between GGUF quantization formats and actual token generation speed. The key insight: "bits per weight" does NOT equal "tokens per second" - smaller file sizes don't always mean faster performance on CPUs.

Key takeaways:

## The Problem
- User downloads a "tiny" 2-bit quantized model expecting fast performance
- Gets only 1.2 tokens per second on an old i5 laptop
- Frustration leads to thinking "CPU is broken"
- Reality: The quantization format is the problem, not the hardware

## What is GGUF?
GGUF (GPT-Generated Unified Format) is like a "universal adapter" for quantized models. It lets you run the same model across different tools (llama.cpp, Ollama, LM Studio) without recompiling.

**But**: Not all adapters are equally efficient. Some strategies are optimized for GPUs, not CPUs.

## The Key Insight: Bits Per Weight ≠ Tokens Per Second

### Understanding the Metrics
- **bits/weight**: How tightly packed each number is (lower = more compression)
- **size (GiB)**: Disk/RAM space required
- **prompt processing t/s**: How fast it reads your question (prefill phase - compute-bound)
- **text generation t/s**: How fast it writes its answer (decode phase - memory-bound)

### Critical Finding
For chat, **text generation speed matters more than prompt speed**. You wait once for prefill but for every token during decode.

### The Plot Twist
**Q2_K is faster than Q4_K_M in some cases, but IQ formats (like IQ2_XXS) are SLOWER on CPUs!**

The smallest file (UD-IQ2_XXS) is the slowest. The "medium-sized" Q3_K_S is the fastest, together with Q4_K_S.

## Why IQ Formats Fail on CPU
- IQ formats are optimized for GPUs (parallel computation)
- On CPUs (sequential), the dequantization overhead outweighs memory savings
- K-quant formats use simpler dequantization math that CPUs handle efficiently

> "Contrary to the behaviour observed on our GPU setup, the KQ kernels outperform the IQ kernels on the Intel CPU. Accordingly, we suggest trying the KQ models first if you plan to run on CPUs." — Byteshape

## CPU User Recommendations

### Start with Q4_K_M
Three reasons:
1. **CPU-optimized kernels**: K-quant formats use simpler dequantization math
2. **Balanced quality**: Retains ~96% of original model's performance, cuts file size by ~75%
3. **Community default**: Most tested and recommended format

### You don't need the smallest file. You need the right format.

## KV Cache Consideration
The KV cache (short-term memory) is NOT quantized by default. A long conversation (16K tokens) can eat gigabytes of RAM even with tiny model weights.

To quantize KV cache:
```bash
.\llama-server.exe -m models\Qwen3.5-2B-Q8_0.gguf -c 8192 --kv-cache-type q8_0
```

## Quick Test: 5-Minute Benchmark Experiment
1. Download two versions: IQ2_XXS and Q4_K_M
2. Run benchmark script comparing tokens/sec
3. Q4_K_M will likely win on CPU

## The Takeaway
If your local AI feels slow, don't blame your CPU. Blame the quantization format. Switch to Q4_K_M or Q4_K_S and watch it fly.

[Source: Your-CPU-is-NOT-Broken-the-hidden-Truth-about-GGU]
