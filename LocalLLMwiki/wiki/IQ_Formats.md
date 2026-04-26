# IQ Quantization Formats (GPU-Optimized)

**IQ formats** (IQ2, IQ4, IQ8) are optimized for GPU inference but perform poorly on CPUs due to complex dequantization overhead.

## Format Overview

| Format | Bits | File Size | GPU | CPU |
|--------|------|-----------|-----|-----|
| IQ2_XXS | 2.0 | ~0.5x | Excellent | Poor |
| IQ2_XXS | 2.38 | ~0.6x | Very Good | Very Poor |
| IQ4_N | 4.0 | ~1.0x | Good | Fair |
| IQ8_0 | 8.0 | ~1.5x | Excellent | Fair |

## Why CPUs Hate IQ Formats

1. **Complex dequantization**: IQ formats require expensive unpacking
2. **Memory bandwidth bottleneck**: Sequential CPU processing can't keep up
3. **Compute-bound workloads**: CPU math-heavy operations slow down

## When to Use

- **Avoid on CPU-only systems**
- **Best for**: NVIDIA RTX 4000/5000 series GPUs
- **Not recommended**: Intel/AMD CPUs, integrated graphics

---

## Alternatives

- **Q4_K_M**: Better CPU/GPU balance
- **Q3_K_S**: Smaller CPU-optimized alternative
- **Q8_0**: High quality for both CPU/GPU

---

*See [GGUF Quantization Guide](./GGUF_Quantization_Guide.md) for benchmark comparison.*

## See Also

- [K-Quantization Formats](./K_Formats.md) - Alternative CPU-optimized option
- [Quantization](./Quantization.md) - Understanding quantization
- [GGUF Quantization Guide](./GGUF_Quantization_Guide.md) - Detailed comparisons
- [Quantization Formats](./Quantization_Formats.md) - IQ vs K-quant comparison
- [Qwen3.5 Local Guide](./Qwen3.5_Local_Guide.md) - Model-specific recommendations
