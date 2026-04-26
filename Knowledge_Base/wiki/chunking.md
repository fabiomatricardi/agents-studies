---
title: Chunking
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

Chunking is the process of splitting documents into smaller, semantically coherent pieces before embedding and storing in a vector database. It is one of the most critical yet overlooked aspects of building effective RAG systems.

## Why Chunking Matters

How you break up your documents directly affects what gets retrieved. A badly chunked document is like trying to learn from shredded newspaper—technically the info is there, but good luck making sense of it. Poor chunking = irrelevant context = bad answers. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

## Chunking Strategies

### Fixed-Size Chunking

Split by character count or token count. Simple but may break mid-sentence, losing semantic coherence.

### Semantic Chunking

Use embeddings to find natural breakpoints based on meaning rather than arbitrary sizes. More accurate but computationally heavier.

### Sentence-Based Splitting

Split at sentence boundaries. Preserves complete thoughts, better for Q&A and factual retrieval. Tools like LangChain and LlamaIndex simplify this.

### Recursive Chunking

Split by paragraphs, then sentences, then smaller units. Balances coherence with granularity.

## Best Practices

1. **Experiment** - No one-size-fits-all. Test with your actual data.
2. **Overlap** - Add slight overlap between chunks to preserve context at boundaries.
3. **Rank chunks** - Not all retrieved chunks are equally relevant; the LLM may truncate.
4. **Tune `k`** - Number of chunks retrieved (`k`) can overwhelm context or miss key info.

## Common Mistakes

- **Too small**: Lose context, miss connections
- **Too large**: Exceed context window, dilute relevance
- **Ignoring structure**: Breaking tables, code blocks, or lists mid-element

## Related Concepts

- [[RAG]]: The system chunking serves
- [[Embeddings]]: Generated from chunks
- [[Contextual Retrieval]]: Technique that enhances chunk context