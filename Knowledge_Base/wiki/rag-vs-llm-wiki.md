---
title: RAG vs LLM Wiki
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

A comparison between traditional Retrieval-Augmented Generation (RAG) and the [[LLM Wiki Pattern]] for knowledge management.

## Traditional RAG

| Aspect | Behavior |
|--------|----------|
| Knowledge retention | None - every query starts from zero |
| Synthesis | Happens at query time, every time |
| Storage | Vector store with embedded chunks |
| Query behavior | Same query on day 1 and day 1000 produces identical quality answer |
| Maintenance | Minimal - add documents, they're automatically indexed |

## LLM Wiki Pattern

| Aspect | Behavior |
|--------|----------|
| Knowledge retention | Accumulates - each source enriches existing pages |
| Synthesis | Happens once at ingest time |
| Storage | Human-readable markdown files with YAML frontmatter |
| Query behavior | Answers improve as wiki matures, drawing on synthesized knowledge |
| Maintenance | Active - requires schema design, lint checks, periodic re-ingestion |

## Trade-offs

### RAG Advantages
- Simpler to build - no schema design required
- Cheaper initial setup
- Handles dynamic/changing sources well
- Good for real-time knowledge

### RAG Disadvantages
- Never gets "smarter" - same query, same quality
- No cross-referential understanding between documents
- Opaque embeddings are hard to debug
- Quality degrades with large context windows

### LLM Wiki Advantages
- Knowledge compounds over time
- Faster/cheaper queries as wiki matures
- Human-readable, version-controllable
- Explicit provenance tracking
- Cross-referential density emerges naturally

### LLM Wiki Disadvantages
- Ingest is expensive (many LLM calls per source)
- Synthesis quality depends on model capability
- Schema design is non-trivial work
- Stale page risk if routing misses updates
- Not designed for real-time knowledge streams

## When to Use Each

**Use RAG when:**
- Working with dynamic, frequently changing sources
- Need simple setup with minimal maintenance
- Query volume is high but corpus is small
- Don't need accumulated understanding

**Use LLM Wiki when:**
- Knowledge should grow and improve over time
- Working with curated, stable sources (papers, articles)
- Need provenance and audit trails
- Building long-term knowledge management systems

## Your Implementation

Your knowledge base at `C:\FABIO-AI\Knowledge_Base` uses the LLM Wiki pattern, validating this architecture as suitable for persistent, compounding knowledge.

## Related Concepts

- [[LLM Wiki Pattern]]: The full pattern architecture
- [[Knowledge Compounding]]: The core principle
- [[RAG]]: Traditional retrieval-augmented generation