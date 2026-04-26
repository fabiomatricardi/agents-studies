# Quantization

**Quantization** is the process of compressing model weights from higher precision (16-bit/FP16) to lower bit representations (2-bit, 4-bit, 8-bit).

## What It Does

- Reduces file size
- Reduces RAM usage
- Enables running larger models on consumer hardware
- **Trade-off**: Computation cost during inference

## The Hidden Cost

Quantization is like vacuum-sealing items:
- **Benefit**: Fits more in a smaller container
- **Cost**: Takes longer to unpack/use

## Common Quantization Formats

- **Q (K-quantized)**: CPU-optimized (Q2, Q4, Q8)
- **IQ (Int8-quantized)**: GPU-optimized (IQ2, IQ4, IQ8)

**Key insight:** Lower bits ≠ faster inference. CPU-friendly formats (K-quant) are faster than GPU-optimized formats (IQ-quant) on CPU hardware.

---

## Related Resources

- [GGUF Format](./GGUF.md)
- [Quantization Formats Guide](./Quantization_Formats.md)
- [Byteshape Optimization](./Byteshape_Optimization.md)

---

## See Also

- [K-Quantization Formats](./K_Formats.md) - CPU-optimized (Q4_K_M, Q3_K_S)
- [IQ Quantization Formats](./IQ_Formats.md) - GPU-optimized (IQ2, IQ4)
- [GGUF Quantization Guide](./GGUF_Quantization_Guide.md) - Detailed benchmarks
- [Quantization Formats](./Quantization_Formats.md) - IQ vs K-quant comparison
- [Qwen3.5 Local Guide](./Qwen3.5_Local_Guide.md) - Model-specific recommendations

---

*Source: "Your CPU is NOT Broken: the hidden Truth about GGUF quantization" by Fabio Matricardi*
