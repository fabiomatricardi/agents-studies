# K-Quantization Formats (CPU-Optimized)

**K-quant formats** (Q2, Q3, Q4, Q8) use simpler dequantization algorithms that are optimized for CPU processing. They balance quality and speed better on CPU hardware.

## Format Overview

| Format | Bits | File Size | CPU | GPU | Quality |
|--------|------|-----------|-----|-----|---------|
| Q2_K | 2.0 | ~0.5x | Very Good | Good | ~85% |
| Q3_K_S | 3.0 | ~0.7x | Excellent | Good | ~93% |
| Q3_K_M | 3.5 | ~0.8x | Very Good | Good | ~95% |
| Q4_K_S | 4.0 | ~1.0x | Excellent | Good | ~96% |
| Q4_K_M | 4.5 | ~1.1x | Excellent | Very Good | ~96% |
| Q8_0 | 8.0 | ~1.5x | Very Good | Excellent | ~98% |

## Why CPUs Love K-Quant

1. **Simpler dequantization**: Linear math operations CPU handles efficiently
2. **Memory-bandwidth friendly**: Better handles sequential token generation
3. **Balanced quality**: Maintains ~95-96% of original model performance

## Best CPU Choices

| Use Case | Recommended Format |
|----------|-------------------|
| Fastest speed | Q2_K or Q3_K_S |
| Best balance | **Q4_K_M** |
| Better quality | Q8_0 |
| Memory limited | Q3_K_S |

---

## Quick Start

```powershell
.\llama-server.exe -m models\<Q4_K_M_model>.gguf -c 4096
```

---

## See Also

- [Quantization](./Quantization.md)
- [GGUF](./GGUF.md)
- [IQ Formats](./IQ_Formats.md)

---

*Source: [GGUF Quantization Guide](./GGUF_Quantization_Guide.md)*

## See Also

- [Quantization](./Quantization.md) - Understanding quantization
- [IQ Quantization Formats](./IQ_Formats.md) - GPU-optimized alternative
- [GGUF Quantization Guide](./GGUF_Quantization_Guide.md) - Benchmark comparisons
- [Quantization Formats](./Quantization_Formats.md) - IQ vs K-quant comparison
- [Qwen3.5 Local Guide](./Qwen3.5_Local_Guide.md) - Model-specific recommendations
