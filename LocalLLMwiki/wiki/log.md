## 2026-04-21
### Ingest: LLM Wiki Pattern
- **Source**: Andrej Karpathy Killed RAG. Or Did He_ The LLM Wiki Pattern.md (converted from PDF)
- **Key Takeaway**: Pattern for personal knowledge bases where LLM compiles and maintains persistent markdown wiki. 3 layers: raw → wiki → schema. 3 ops: ingest, query, lint.
- **Related**: [[LLM_Wiki_Pattern.md]], [[Knowledge_Gaps.md]] (backlinks added), [[index.md]] (page added)

## 2026-04-20
### Explored: Knowledge base gaps
- **Command**: //wiki-explore
- **Key Finding**: Three biggest gaps identified (Byteshape_Optimization.md missing, no inference engine alternatives, no hardware-specific guides)
- **Action**: Created Knowledge_Gaps.md with prioritized research list
- **Related**: index.md, Quantization_Formats.md

## Mar 13, 2026
### Added: AI Frankenstein is alive — part 1
- **Source**: "AI Frankenstein is alive part 1" by Fabio Matricardi
- **Key Takeaway**: The future of AI is **modular and specialized**, moving away from single, monolithic decoder-only models. Innovation is happening through assembling specialized components (Sculptor Diffusion Models, Encoder-Decoder Architectures, and Modular MoE) to create purpose-built intelligence for specific tasks (speed, efficiency, reasoning).
- **Implication**: The focus shifts from simply scaling parameters to **Intelligence Density**—how much useful capability a model provides per unit of size and power. This validates the need for specialized architectures and efficient quantization methods (like K-quant) to make powerful AI accessible on edge devices.
- **Related Concepts**: This work directly connects to the core theme of the wiki:
    - **Architecture:** New models like Diffusion Models (Sculptor AI) and Hybrid MoE/Mamba-2 models are the new frontier.
    - **Efficiency:** The push for efficiency (reducing cost/energy) is driven by the need for specialized brains, which directly relates to the need for efficient quantization ([Quantization](./Quantization.md)).
    - **Philosophy**: The "Frankenstein" metaphor represents the necessary combination of specialized components to solve complex, real-world problems efficiently.
- **Contradiction Check**: This reinforces the earlier theme: don't chase single, large models; instead, focus on building a *system* of specialized, efficient components tailored to specific tasks, which is the essence of the "Benchmark = You" philosophy.

This entry is integrated into the overall narrative of building a system of specialized AI components.
## 2025-09-27
### Added: Text-to-LoRA (T2L)
- **Source**: Text to LoRA AI That Fine Tunes Other AI Using Ju.txt by Kevin François
- **Key Takeaway**: A hypernetwork-based system that generates bespoke LoRA adapters on the fly from task descriptions in seconds, replacing per-task fine-tuning. SFT-training enables zero-shot generalization, while reconstruction training compresses known adapters.
- **Implication**: Democratizes model specialization, enabling on-the-fly AI customization and reducing the need for data science teams.
- **Related Concepts**: Hypernetworks, LoRA, parameter-efficient fine-tuning, task embeddings
- **Backlinks**: See wiki/index.md for T2L reference

This entry is integrated into the overall narrative of advanced AI specialization techniques.

