---
title: Knowledge Compounding
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Knowledge compounding is the principle that each piece of ingested information should make existing knowledge richer, not just different. In the [[LLM Wiki Pattern]], this is enforced by the synthesis step: "Preserve and extend existing content — never discard information already on the page." [Source: Beyond RAG How Andrej Karpathy s LLM Wiki Pattern.txt]

## How It Works

When a new source is ingested:
1. The LLM reads the existing wiki page
2. It reads the new source material
3. It rewrites the complete page, integrating new information while preserving everything already there
4. Each subsequent source makes pages denser with cross-references and accumulated understanding

## The Compounding Loop

The pattern includes a `--save` flag for queries: when a synthesized answer represents new, valuable knowledge, it can be automatically filed back as a new wiki page. Future sessions benefit immediately from this captured knowledge.

## Benefits

- **Deeper answers**: A wiki that has ingested 50 papers answers questions with integrated understanding from all 50, not just the most similar chunks
- **Faster/cheaper queries**: Synthesis happens once at ingest, not every query
- **Cross-referential density**: Pages accumulate [[slug]] links to related concepts
- **Explicit provenance**: Every page tracks which sources contributed to it

## Contrast with Traditional RAG

In traditional RAG, every query starts from zero. The same question asked months later re-embeds the query, retrieves the same chunks, and synthesizes the same answer. Nothing was learned from previous interactions.

## Related Concepts

- [[LLM Wiki Pattern]]: The architecture that enables knowledge compounding
- [[RAG vs LLM Wiki]]: Comparison of retrieval approaches