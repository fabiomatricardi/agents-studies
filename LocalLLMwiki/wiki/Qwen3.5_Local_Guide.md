# Qwen3.5 Local Guide

## Overview

Qwen3.5 is a series of LLMs that can be run locally using GGUF quantization formats. This guide covers how to run them using llama.cpp.

## Available Models

| Model | Description |
|-------|------------|
| Qwen3.5-0.8B | Small |
| Qwen3.5-2B | Small |
| Qwen3.5-4B | Small |
| Qwen3.5-9B | Small |
| Qwen3.5-27B-A3B | Medium |
| Qwen3.5-35B-A3B | Medium |
| Qwen3.5-122B-A10B | Medium |

## Quick Start

### Windows

1. Download llama.cpp release: `llama-b8255-bin-win-cpu-x64.zip`
2. Extract to `C:\llama`
3. Place model in `C:\llama\models`
4. Run:
```powershell
.\llama-server.exe -m models\<model>.gguf -c 4096 --reasoning-budget 0
```
5. Open http://localhost:8080

### Linux

```bash
./llama-server -m /path/to/model.gguf -c 4096 --reasoning-budget 0
```

## Recommended Quantization Formats

| Scenario | Recommended Format | Reason |
|---------|-------------------|--------|
| Balanced speed/quality | Q4_K_M | ~96% quality, excellent CPU performance |
| Limited RAM | Q3_K_S | Smaller memory footprint |
| Fastest CPU inference | Q2_K | Best CPU-optimized speed |
| High quality GPU | IQ4_N | GPU-optimized |

## Benchmark Results

**Test:** Qwen3.5-2B on Lenovo X260 (2016 i5)

| Format | File Size | Tokens/sec |
|--------|-----------|------------|
| IQ2_XXS | 1.87 GB | 1.2 |
| Q4_K_M | 4.58 GB | 11.3 |
| Q3_K_S | 2.95 GB | 12.5 |

## Optimization Tips

1. **Threads**: Set to your CPU cores - 2
2. **Context**: Start with 4096, increase if RAM allows
3. **KV Cache**: Enable quantization for long contexts:
```powershell
--kv-cache-type q8_0
```
4. **Reasoning Budget**: Disable for faster inference:
```powershell
--reasoning-budget 0
```

## Resources

- [Unsloth Documentation](https://unsloth.ai)
- [GGUF Quantization Guide](./GGUF_Quantization_Guide.md)
- [Byteshape Optimization](./Byteshape_Optimization.md)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp)

## Related Concepts

- [Quantization Formats](./Quantization_Formats.md) - IQ vs K-quant comparison
- [K-Quantization Formats](./K_Formats.md) - CPU-optimized formats
- [IQ Quantization Formats](./IQ_Formats.md) - GPU-optimized formats
- [GGUF](./GGUF.md) - Universal model format
- [Quantization](./Quantization.md) - Understanding compression
- [GGUF Quantization Guide](./GGUF_Quantization_Guide.md) - Main guide


---

*Last updated: Mar 2026*
