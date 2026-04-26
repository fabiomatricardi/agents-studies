---
title: RAG
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

RAG (Retrieval Augmented Generation) is an architecture that connects LLMs to external knowledge sources to make them more factual, up-to-date, and relevant. [Source: Blaming embeddings is blaming the entire AI game.md]

## How It Works

1. User poses a query
2. Query is embedded and searched via cosine similarity against vector database
3. Most relevant chunks are retrieved
4. Chunks + query are fed as augmented context to LLM
5. LLM generates response

## Why RAG Matters

RAG solves key LLM limitations:

- **Knowledge cutoff**: Access information newer than training date
- **Limited context window**: Draw from vast external repositories on demand
- **Proprietary data**: Access company confidential / NDA-protected data
- **Reduce hallucinations**: Ground responses in retrieved documents, enable citations

## RAG vs ICL

In-Context Learning (ICL) complements RAG - they're not replacements:
- ICL processes what RAG retrieves
- RAG provides relevant content; ICL helps the model understand how to use it
- ICL cannot overcome context window limitations for vast knowledge bases

## RAG Enhancements

### Contextual Retrieval

Anthropic's contextual retrieval technique prepends context to each chunk before embedding, reducing retrieval failures by up to 49%. [Source: Is RAG Dead__ Anthropic Says No.md]

### Re-ranking

Post-retrieval refinement using reranking models further improves accuracy. [Source: Is RAG Dead__ Anthropic Says No.md]

## Practical Implementation Tips

### Chunking

How documents are split directly affects retrieval quality. Poor chunking produces irrelevant context, leading to bad answers. Use semantic chunking or sentence-based splits — tools like LangChain and LlamaIndex simplify this. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

### Embedding Models

Not all embeddings perform equally. Switching from text-embedding-ada-002 to bge-small-en improved relevance by 2x in tests. Different models suit different document types. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

### Vector Databases

- **FAISS**: Fast, good for dev, but no filtering
- **Chroma**: Better features, but slower
- **Pinecone/Weaviate**: Production scaling with metadata filtering

Tune retrieval with different `k` values, similarity thresholds. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

### Context Window Limits

Even with 128k context, stuffing too many chunksconfuses the model or truncates important data. Rank chunks by relevance and be selective. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

### Latency

Pipeline includes: splitting → embedding → DB search → LLM generation. Cache results, use async calls, consider local vector DBs during dev. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

### Evaluation

No single accuracy metric exists. Track: retrieval quality, faithfulness, hallucination rate, user satisfaction. Use tools like RAGAS or LangChain's eval module. [Source: RAG_ What Nobody Tells You When Building Your AI Assistant.md]

## Related Concepts

- [[Embeddings]]: Power the retrieval
- [[Cosine Similarity]]: Finds relevant documents
- [[RAG vs LLM Wiki]]: Comparison of RAG vs LLM Wiki pattern
- [[Contextual Retrieval]]: Anthropic's enhanced RAG technique
- [[Re-ranking]]: Post-retrieval refinement
- [[Chunking]]: Document splitting technique