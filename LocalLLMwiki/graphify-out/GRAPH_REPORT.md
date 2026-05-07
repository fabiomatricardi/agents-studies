# Graph Report - wiki  (2026-05-07)

## Corpus Check
- 14 files · ~3,712 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 14 nodes · 31 edges · 5 communities (3 shown, 2 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.63)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Quantization & Model Guides|Quantization & Model Guides]]
- [[_COMMUNITY_Core Concepts|Core Concepts]]
- [[_COMMUNITY_Wiki Patterns|Wiki Patterns]]
- [[_COMMUNITY_AI Philosophy|AI Philosophy]]
- [[_COMMUNITY_AI Philosophy|AI Philosophy]]

## God Nodes (most connected - your core abstractions)
1. `Quantization Formats` - 8 edges
2. `Gguf Quantization Guide` - 7 edges
3. `Quantization` - 7 edges
4. `Gguf` - 6 edges
5. `K Formats` - 6 edges
6. `Index` - 5 edges
7. `Knowledge Gaps` - 5 edges
8. `Qwen3.5 Local Guide` - 5 edges
9. `Iq Formats` - 4 edges
10. `Llm Wiki Pattern` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Llm Wiki Pattern` --conceptually_related_to--> `Markdown`  [INFERRED]
  wiki/LLM_Wiki_Pattern.md → wiki/Markdown.md
- `Gguf Quantization Guide` --references--> `Gguf`  [EXTRACTED]
  wiki/GGUF_Quantization_Guide.md → wiki/GGUF.md
- `K Formats` --references--> `Gguf`  [EXTRACTED]
  wiki/K_Formats.md → wiki/GGUF.md
- `Markdown` --conceptually_related_to--> `Gguf`  [INFERRED]
  wiki/Markdown.md → wiki/GGUF.md
- `Quantization Formats` --references--> `Gguf`  [EXTRACTED]
  wiki/Quantization_Formats.md → wiki/GGUF.md

## Communities (5 total, 2 thin omitted)

### Community 0 - "Quantization & Model Guides"
Cohesion: 0.8
Nodes (6): Gguf Quantization Guide, Iq Formats, K Formats, Quantization Formats, Qwen3.5 Local Guide, Index

### Community 1 - "Core Concepts"
Cohesion: 1.0
Nodes (3): Gguf, Markdown, Quantization

### Community 2 - "Wiki Patterns"
Cohesion: 1.0
Nodes (3): Knowledge Gaps, Llm Wiki Pattern, Log

## Knowledge Gaps
- **2 isolated node(s):** `Stop Chasing Ai Benchmarks Be The Benchmark`, `The Smallest 8B Model Ever Created Is Not Really A`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Quantization` connect `Core Concepts` to `Quantization & Model Guides`, `Wiki Patterns`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Why does `Knowledge Gaps` connect `Wiki Patterns` to `Quantization & Model Guides`, `Core Concepts`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Why does `Quantization Formats` connect `Quantization & Model Guides` to `Core Concepts`, `Wiki Patterns`?**
  _High betweenness centrality (0.092) - this node is a cross-community bridge._
- **What connects `Stop Chasing Ai Benchmarks Be The Benchmark`, `The Smallest 8B Model Ever Created Is Not Really A` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._