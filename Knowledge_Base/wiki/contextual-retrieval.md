---
title: Contextual Retrieval
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Contextual Retrieval is a preprocessing technique by Anthropic that prepends relevant context to each document chunk before embedding, solving the "lost context" problem in standard RAG systems. It achieves up to 49% reduction in retrieval failures when combined with existing techniques.

## Overview

Standard RAG systems struggle with context loss when documents are chunked. Each chunk loses information about where it came from, making retrieval less accurate. Contextual Retrieval solves this by having an LLM generate contextual metadata for each chunk before embedding. [Source: Is RAG Dead__ Anthropic Says No.md]

## How It Works

1. Break documents into chunks (typically a few hundred tokens each)
2. For each chunk, use an LLM to generate a contextual statement describing where the chunk fits in the document
3. Prepend this context to the original chunk
4. Generate embeddings for these enriched chunks
5. Store in vector database with BM25 index

Example:
- Original chunk: "Revenue grew by 3% over the previous quarter"
- Contextualized: "This chunk is from a filing on Acme Corporation's performance in Q2 2023. Revenue grew by 3% over the previous quarter"

## Performance

Anthropic's benchmarks show:
- 35% reduction in retrieval failures with contextual embeddings alone (5.7% → 3.7%)
- 49% reduction when combined with contextual BM25
- 1.9% error rate with re-ranker added

## Trade-offs

- Chunks grow by 50-100 tokens
- Processing costs ~$1.02/million tokens (prompt caching reduces by 90%)
- Increased storage overhead
- Best with efficient models like Claude Haiku for context generation

## When to Use

- Large knowledge bases (200K+ tokens) where long-context LLMs are impractical
- Documents with multiple entities, time periods, or contexts
- High accuracy requirements (legal, financial documents)

## When to Skip

- Small knowledge bases (under 200K tokens) — use long-context LLMs instead
- Already well-structured documents with clear context
- Uniform content where chunks are self-contained

## Implementation Tips

1. Customize context prompts for different document types
2. Best embedding models: Google Gemini Text-004, Voyage embeddings
3. Use re-ranking for best results (retrieve 20 chunks, rerank to best 5)
4. Test with actual data — benchmarks vary by document type

## Related Concepts

- [[RAG]] - The broader retrieval system this technique enhances
- [[Embeddings]] - Vector representations this technique improves
- [[Re-ranking]] - Post-retrieval refinement that complements contextual retrieval