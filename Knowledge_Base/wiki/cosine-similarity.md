---
title: Cosine Similarity
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Cosine similarity is a metric that measures the cosine of the angle between two vectors. It determines how semantically similar two pieces of text are by comparing their embedding vectors. [Source: Blaming embeddings is blaming the entire AI game.md]

## How It Works

- Value closer to 1: vectors point in same direction = high semantic similarity
- Value near 0: little similarity
- Value near -1: opposite meanings

## In RAG

Cosine similarity is the workhorse that powers the "Retrieval" in RAG:
1. Query is embedded into a vector
2. Search vector database of embedded document chunks
3. Retrieve chunks with highest cosine similarity to query

## Why It Matters

For efficiently sifting through millions/billions of vectorized chunks, cosine similarity is robust, efficient (no wasted tokens), and effective.

It powers every recommendation system - the same principle that gives you "you might also like" suggestions.

## Related Concepts

- [[Embeddings]]: The vectors being compared
- [[RAG]]: Uses cosine similarity for retrieval