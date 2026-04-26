---
title: Re-ranking
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Re-ranking is a post-retrieval refinement technique that improves RAG accuracy by re-evaluating initially retrieved chunks using a specialized reranking model, rather than relying on embedding similarity alone.

## Overview

In standard RAG, embeddings determine relevance. Re-ranking adds a second stage where retrieved candidates are re-scored using a dedicated reranking model that better understands query-document relationships. [Source: Is RAG Dead__ Anthropic Says No.md]

## How It Works

1. Initial retrieval fetches top-N chunks (typically 20) using embedding similarity
2. Re-ranking model evaluates each chunk against the query
3. Model reorders chunks by true relevance
4. Top results are passed to LLM for generation

## Performance

Anthropic found that combining contextual retrieval with re-ranking dropped error rate from 5.7% to 1.9% — the best result in their benchmarks.

## Implementation Tips

- Retrieve more candidates than needed initially (e.g., 20)
- Use Cohere's reranking API or similar services
- Works best in combination with contextual retrieval
- Test with actual data for accurate benchmark

## Related Concepts

- [[RAG]]: The retrieval system re-ranking enhances
- [[Contextual Retrieval]]: Complements re-ranking for best results
- [[Embeddings]]: Powers the initial retrieval stage