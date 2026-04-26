---
title: Embeddings
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Embeddings are dense numerical vector representations of text that capture semantic meaning. They are the foundational building blocks that allow LLMs to understand language. [Source: Blaming embeddings is blaming the entire AI game.md]

## What They Are

At the heart of any GPT model lies the embeddings layer - the initial gateway through which all textual input must pass to be understood by the machine.

## How They Work

1. **Tokenization**: Input text is broken into tokens (words or sub-word units)
2. **Vector transformation**: Tokens are converted into dense numerical vectors via the embedding layer
3. **Semantic encoding**: Similar meanings get similar vector representations - "King" and "Queen" are closer in vector space than "King" and "Carburetor"

## Key Functions

- **Numerical representation**: Converts symbolic language into mathematical format
- **Capturing semantic meaning**: Encodes nuance, context, and relationships
- **Dimensionality reduction**: More efficient than one-hot encoding

## The "Lingua Franca" of LLMs

To downplay embeddings is to ignore the very mechanism that allows an LLM to begin understanding language. They're not optional - they're the core machinery.

## Related Concepts

- [[Cosine Similarity]]: Measures similarity between embeddings
- [[RAG]]: Uses embeddings for retrieval
- [[RAG vs LLM Wiki]]: Discusses retrieval approaches
- [[Contextual Retrieval]]: Technique that enhances embeddings with context