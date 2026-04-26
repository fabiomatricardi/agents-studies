# GGUF (GPT-Generated Unified Format)

**GGUF** is the universal adapter format for quantized LLMs. It allows running the same model file across different tools like llama.cpp, Ollama, LM Studio, and others without recompilation.

## Key Properties

- **Universal compatibility**: Works across multiple inference platforms
- **Quantization-aware**: Stores model weights in compressed bit representations
- **Flexible**: Supports various quantization formats (Q, IQ, etc.)
- **Portable**: Same file can run on different hardware

## Common Extensions

- `*.gguf` - Standard quantized model files
- Quantization formats vary per file (Q4, Q8, IQ2, etc.)

---

## Related Resources

- [GGUF Documentation](./GGUF_Quantization_Guide.md)
- [Quantization Formats](./Quantization_Formats.md)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp)

## See Also

- [K-Quantization Formats](./K_Formats.md) - CPU-optimized formats
- [IQ Quantization Formats](./IQ_Formats.md) - GPU-optimized formats
- [Quantization](./Quantization.md) - Understanding quantization
- [Quantization Formats](./Quantization_Formats.md) - Detailed comparison
- [Qwen3.5 Local Guide](./Qwen3.5_Local_Guide.md) - Running Qwen3.5 locally


---

*See [GGUF Quantization Guide](./GGUF_Quantization_Guide.md) for detailed explanation.*
