---
title: LLM Wiki Pattern
created: 2026-04-21
last_updated: 2026-04-21
source_count: 1
status: draft
---

A pattern for building personal knowledge bases where the LLM builds and maintains a persistent, compounding markdown wiki instead of re-retrieving documents on every query like traditional RAG.

## What Is the LLM Wiki Pattern?

Described by Andrej Karpathy in a viral GitHub Gist (5,000+ stars in 48 hours), the LLM Wiki pattern inverts traditional RAG: instead of retrieving at query time, the LLM compiles and maintains structured knowledge continuously. [Source: Andrej Karpathy Killed RAG. Or Did He_ The LLM Wiki Pattern.md]

## Architecture: Three Layers

1. **Raw Sources** - Immutable collection of articles, papers, notes. Never modified. Source of truth.
2. **Wiki** - LLM-generated markdown files: summaries, entity pages, concept pages, cross-references. LLM owns this entirely.
3. **Schema** - Configuration (e.g., CLAUDE.md, AGENTS.md) directing agent behavior.

## Three Core Operations

1. **Ingest** - LLM reads new source, creates summary page, updates index, updates relevant concept/entity pages. One source touches 10-15 wiki pages.
2. **Query** - LLM searches index, reads relevant pages, synthesizes answer with citations. Valuable answers can be filed back as new wiki pages.
3. **Lint** - Periodic health check: contradictions, stale claims, orphan pages, missing cross-references, data gaps.

## LLM Wiki vs Traditional RAG

| Aspect | Traditional RAG | LLM Wiki |
|--------|----------------|----------|
| Operation | Query-time retrieval | Ingest-time compilation |
| Knowledge | Rediscovered each query | Pre-compiled, persistent |
| Structure | Chunks destroy context | Full synthesis preserved |
| Metaphor | Search engine | Encyclopedia |

The core insight: RAG is stateless (every query is day one), LLM Wiki compounds knowledge over time. [Source: Andrej Karpathy Killed RAG. Or Did He_ The LLM Wiki Pattern.md]

## Scalability

- Works well at personal scale (~100 articles, ~400k words)
- No RBAC, no ACID transactions, no concurrency controls
- Not an enterprise platform (yet)
- Different from RAG which handles millions of documents

## Tools

- **Obsidian** - IDE for wiki, graph view shows connections
- **qmd** - Hybrid BM25/vector search with LLM re-ranking
- **Marp** - Generate slide decks from wiki content
- **Dataview** - Query frontmatter dynamically
- **Obsidian Web Clipper** - Convert web articles to markdown

## This Wiki

This knowledge base follows the LLM Wiki pattern:
- `raw/` contains immutable sources
- `wiki/` contains LLM-maintained markdown
- `AGENTS.md` is the schema

See also: [[Knowledge_Gaps.md]], [[Markdown.md]]