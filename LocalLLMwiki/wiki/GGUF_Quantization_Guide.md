# GGUF Quantization Guide

## Summary

This guide explains the hidden truth about GGUF quantization: **lower bits per weight does NOT mean faster inference speed**.

The core problem: IQ formats (IQ2, IQ4, etc.) are optimized for GPUs, while K-quant formats (Q4_K_M, Q3_K_S, etc.) are optimized for CPUs.

---

## Key Takeaways

### 1. Bits Per Weight ≠ Tokens Per Second

A model labeled "Q4_K_M" means each weight uses ~4 bits instead of 16. This reduces storage by 75%, BUT inference speed depends on the dequantization algorithm, not just the bit count.

### 2. The Two Phases

| Phase | Description | Optimization |
|-------|-------------|-------------|
| **Prompt Processing** | Prefill phase, parallel computation | Compute-bound, less sensitive to quantization |
| **Text Generation** | Decode phase, sequential processing | Memory-bound, VERY sensitive to quantization |

For chat applications, decode speed matters more than prompt speed.

### 3. CPU vs GPU Optimization

| Format Type | Examples | GPU | CPU |
|-------------|----------|-----|-----|
| **IQ (Int8-quantized)** | IQ2_XXS, IQ4_N | Excellent | Poor |
| **K-quant (K-quantized)** | Q4_K_M, Q3_K_S | Good | Excellent |

**Recommendation:** For CPU users, start with Q4_K_M or Q4_K_S.

### 4. The KV Cache Issue

The KV cache (short-term memory) is **not quantized by default**. A 2B model with 16K context can consume gigabytes of RAM just for the cache.

**Solution:** Enable KV cache quantization:
```powershell
.\llama-server.exe -m model.gguf --kv-cache-type q8_0
```

---

## Quick Start for Windows Users

1. Download llama.cpp release from GitHub
2. Extract to `C:\llama`
3. Place model in `C:\llama\models`
4. Run: `.\llama-server.exe -m models\<model>.gguf -c 4096`
5. Open http://localhost:8080

**Pro Tip:** Start with Q4_K_M format:
```powershell
.\llama-server.exe -m models\Qwen3.5-2B-Q4_K_M.gguf -c 4096 --reasoning-budget 0
```

---

## Benchmark Results

**Test Case:** Qwen3.5-2B on 2016 Lenovo X260 (Intel Core i5)

| Format | File Size | Tokens/sec |
|--------|-----------|------------|
| IQ2_XXS | 1.87 GB | 1.2 |
| Q4_K_M | 4.58 GB | 11.3 |
| Q3_K_S | 2.95 GB | 12.5 |

**Surprise:** Smaller file ≠ faster speed. Q4_K_M runs 9x faster than IQ2_XXS despite being larger.

---

## Resources

- [Byteshape CPU findings](https://byteshape.com)
- [Unsloth GGUF Guide](https://unsloth.ai)
- [Llama.cpp Documentation](https://github.com/ggml-org/llama.cpp)
- [GGUF Specification](https://github.com/ggml-org/ggml)

## Related Concepts

- [GGUF Format](./GGUF.md)
- [Quantization](./Quantization.md)
- [IQ Quantization Formats](./IQ_Formats.md)
- [K-Quantization Formats](./K_Formats.md)

---

*Article source: "Your CPU is NOT Broken: the hidden Truth about GGUF quantization" by Fabio Matricardi (Mar 2026)*

*This guide is part of the series: "Not All Quantizations Are Born Equal"*

