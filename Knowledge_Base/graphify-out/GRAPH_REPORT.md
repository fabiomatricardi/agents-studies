# Graph Report - ./wiki  (2026-05-07)

## Corpus Check
- Corpus is ~9,498 words - fits in a single context window. You may not need a graph.

## Summary
- 36 nodes · 65 edges · 8 communities (5 shown, 3 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.74)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_RAG & Knowledge Management|RAG & Knowledge Management]]
- [[_COMMUNITY_Coding Agents|Coding Agents]]
- [[_COMMUNITY_LLM Integration & Providers|LLM Integration & Providers]]
- [[_COMMUNITY_GPU-Poor & Reasoning|GPU-Poor & Reasoning]]
- [[_COMMUNITY_llama.cpp Ecosystem|llama.cpp Ecosystem]]
- [[_COMMUNITY_AI Search|AI Search]]
- [[_COMMUNITY_Knowledge Base Gaps|Knowledge Base Gaps]]
- [[_COMMUNITY_Knowledge Base Log|Knowledge Base Log]]

## God Nodes (most connected - your core abstractions)
1. `Bifrost` - 9 edges
2. `Local LLMs` - 9 edges
3. `RAG` - 9 edges
4. `GPU-Poor Solutions` - 9 edges
5. `Bifrost-CLI` - 8 edges
6. `llama.cpp` - 7 edges
7. `LLM Providers` - 6 edges
8. `Coding Agents` - 6 edges
9. `Gemma 4` - 6 edges
10. `llama-server` - 5 edges

## Surprising Connections (you probably didn't know these)
- `llama.cpp` --semantically_similar_to--> `LLM Providers`  [INFERRED] [semantically similar]
  wiki/bifrost.md → wiki/ai-gateways.md
- `Chain of Thought` --conceptually_related_to--> `RAG`  [INFERRED]
  wiki/chain-of-thought.md → wiki/chunking.md
- `Bifrost` --conceptually_related_to--> `Ollama`  [INFERRED]
  wiki/bifrost.md → wiki/gpu-poor-solutions.md
- `RAG` --semantically_similar_to--> `Knowledge Compounding`  [INFERRED] [semantically similar]
  wiki/chunking.md → wiki/ai-usage-checklist.md
- `LLM Wiki Pattern` --semantically_similar_to--> `RAG`  [INFERRED] [semantically similar]
  wiki/ai-usage-checklist.md → wiki/chunking.md

## Hyperedges (group relationships)
- **RAG System Components** — chunking, embeddings, contextual_retrieval, cosine_similarity, re_ranking, rag [EXTRACTED 1.00]
- **Local AI Infrastructure** — llama_cpp, llama_server, ollama, gemma_4, local_llms, gpu_poor_solutions [EXTRACTED 1.00]
- **Reasoning Approaches** — chain_of_thought, hierarchical_reasoning_model, contextual_retrieval [INFERRED 0.85]
- **llama.cpp Ecosystem Components** — llama_cpp, llama_cli, llama_server [EXTRACTED 1.00]
- **LLM Wiki Pattern Architecture** — llm_wiki_pattern, knowledge_compounding, rag_vs_llm_wiki [EXTRACTED 1.00]
- **RAG Enhancement Pipeline** — rag, re_ranking [EXTRACTED 1.00]

## Communities (8 total, 3 thin omitted)

### Community 0 - "RAG & Knowledge Management"
Cohesion: 0.4
Nodes (10): AI Usage Checklist, Chunking, Contextual Retrieval, Cosine Similarity, Embeddings, Knowledge Compounding, LLM Wiki Pattern, RAG (+2 more)

### Community 1 - "Coding Agents"
Cohesion: 0.38
Nodes (7): AI Gateways, Bifrost-CLI, Claude Code, Codex CLI, Coding Agents, Gemini CLI, MCP Servers

### Community 2 - "LLM Integration & Providers"
Cohesion: 0.4
Nodes (6): Bifrost, LiteLLM, LLM Providers, NVIDIA NIM, Ollama, Opencode

### Community 3 - "GPU-Poor & Reasoning"
Cohesion: 0.4
Nodes (5): Chain of Thought, GGUF Format, GPU-Poor Solutions, Hierarchical Reasoning Model, vLLM

### Community 4 - "llama.cpp Ecosystem"
Cohesion: 1.0
Nodes (4): llama-cli, llama.cpp, llama-server, Local LLMs

## Knowledge Gaps
- **9 isolated node(s):** `LiteLLM`, `Claude Code`, `Codex CLI`, `Gemini CLI`, `Perplexica` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Hierarchical Reasoning Model` connect `GPU-Poor & Reasoning` to `llama.cpp Ecosystem`?**
  _High betweenness centrality (0.407) - this node is a cross-community bridge._
- **Why does `RAG` connect `RAG & Knowledge Management` to `GPU-Poor & Reasoning`?**
  _High betweenness centrality (0.402) - this node is a cross-community bridge._
- **Why does `Chain of Thought` connect `GPU-Poor & Reasoning` to `RAG & Knowledge Management`?**
  _High betweenness centrality (0.387) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `RAG` (e.g. with `Chain of Thought` and `LLM Wiki Pattern`) actually correct?**
  _`RAG` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `LiteLLM`, `Claude Code`, `Codex CLI` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._