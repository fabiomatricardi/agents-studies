# Quantization Formats Comparison

## IQ vs K-Quant Formats

This page compares the two main types of GGUF quantization formats.

---

## IQ Quantization (GPU-Optimized)

**IQ** stands for **Int8-quantized** formats using complex dequantization algorithms.

### Characteristics
- **Algorithm**: Complex multi-step dequantization
- **Best for**: NVIDIA GPUs (RTX 3000/4000/5000 series)
- **CPU Performance**: Very poor
- **Quality**: Higher theoretical quality, but CPU cannot utilize it

### Common IQ Formats

| Format | Bits | CPU Score | GPU Score |
|-------|------|-----------|-----------|
| IQ2_XXS | 2.0 | Very Slow | Fast |
| IQ2_XXS | 2.38 | Very Slow | Very Fast |
| IQ4_N | 4.0 | Slow | Good |
| IQ8_0 | 8.0 | Medium | Very Good |

**Note:** IQ formats are 2-9x slower on CPU than on GPU.

---

## K-Quantization (CPU-Optimized)

**K-quant** formats use **K-quantized** algorithms with simpler dequantization.

### Characteristics
- **Algorithm**: Simple linear dequantization
- **Best for**: CPUs (Intel, AMD, Apple Silicon)
- **CPU Performance**: Excellent
- **Quality**: High quality with ~95-96% of original performance

### Common K-Quant Formats

| Format | Bits | File Size | CPU Score | GPU Score |
|-------|------|-----------|-----------|-----------|
| Q2_K | 2.0 | 1.91 GB | Very Fast | Fast |
| Q3_K_S | 3.0 | 2.95 GB | Fast | Good |
| Q3_K_M | 3.5 | 3.60 GB | Very Fast | Good |
| Q4_K_S | 4.0 | 4.29 GB | Very Fast | Very Good |
| **Q4_K_M** | **4.5** | **4.58 GB** | **Best** | Very Good |
| Q8_0 | 8.0 | 6.63 GB | Fast | Excellent |

---

## Benchmark Summary

**Test:** Qwen3.5-2B on Lenovo X260 (2016 i5 laptop)

| Format | File Size | Tokens/sec | Relative Speed |
|--------|-----------|------------|----------------|
| IQ2_XXS | 1.87 GB | 1.2 | **100%** (slowest) |
| Q4_K_M | 4.58 GB | 11.3 | **942%** |
| Q3_K_S | 2.95 GB | 12.5 | **1042%** |

**Key Finding:** Larger file (Q4_K_M) runs 9x faster than smaller file (IQ2_XXS)

---

## Decision Guide

### Choose IQ formats when:
- You have an NVIDIA GPU (RTX 3000/4000/5000 series)
- You need maximum theoretical quality
- You have plenty of RAM

### Choose K-quant formats when:
- You're on CPU-only (Windows, Linux, Mac)
- You want balanced quality/speed
- You have limited RAM

### Quick Recommendations

| Hardware | Recommended Format | Reason |
|---------|-------------------|--------|
| CPU (Intel/AMD) | **Q4_K_M** | Best CPU-optimized balance |
| CPU (limited RAM) | Q3_K_S | Smaller memory footprint |
| GPU (RTX 4000+) | IQ4_N or IQ2 | GPU-optimized |
| GPU (RTX 3000+) | Q4_K_M | Better CPU fallback |

---

## Resources

- [Byteshape CPU findings](https://byteshape.com)
- [Byteshape GPU findings](https://byteshape.com)
- [GGUF Quantization Guide](./GGUF_Quantization_Guide.md)
- [Llama.cpp Documentation](https://github.com/ggml-org/llama.cpp)

## See Also

- [K-Quantization Formats](./K_Formats.md) - CPU-optimized formats
- [IQ Quantization Formats](./IQ_Formats.md) - GPU-optimized formats
- [GGUF](./GGUF.md) - Universal model format
- [Quantization](./Quantization.md) - Understanding compression

---

*Source: "Not All Quantizations Are Born Equal" series by Fabio Matricardi*
