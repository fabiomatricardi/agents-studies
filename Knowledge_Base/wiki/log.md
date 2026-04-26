---
title: Knowledge Base Log
created: 2026-04-17
last_updated: 2026-04-18
status: draft
---

## 2026-04-17

### ingest | Bifrost AI Gateway

Ingested source: "Bifrost CLI is the AI gateway for coding agents we.txt" from raw/

Created wiki pages:
- [[Bifrost]] - Main summary page for the AI gateway
- [[Bifrost-CLI]] - CLI tool for connecting coding agents
- [[AI Gateways]] - Concept page for gateway architecture
- [[Coding Agents]] - Category page for AI coding assistants
- [[LLM Providers]] - Page for LLM service providers
- [[Opencode]] - Page for the Opencode coding agent

Updated:
- [[wiki/index.md]] - Added all new pages to index

Notes:
- No contradictions detected with existing content (first entry)
- Bifrost provides 40x performance improvement over LiteLLM
- Bifrost-CLI enables zero-config setup for multiple coding agents

## 2026-04-18

### ingest | LLM Wiki Pattern

Ingested source: "Beyond RAG How Andrej Karpathy s LLM Wiki Pattern.txt" from raw/

Created wiki pages:
- [[LLM Wiki Pattern]] - Main summary page for Karpathy's architecture
- [[Knowledge Compounding]] - The principle of accumulating knowledge
- [[RAG vs LLM Wiki]] - Detailed comparison of approaches

Updated:
- [[wiki/index.md]] - Added new Knowledge Management section

Notes:
- Your knowledge base already implements the LLM Wiki pattern!
- Architecture matches: raw/, wiki/, index.md, log.md, source tracking
- No contradictions detected - validates existing approach

## 2026-04-18

### explore | Knowledge Base Gaps

Ran //wiki-explore to identify gaps and research opportunities.

Created wiki pages:
- [[Knowledge Base Gaps]] - Synthesized gaps identified during exploration

Updated:
- [[wiki/index.md]] - Added new page

Gaps identified:
- Local LLMs: No dedicated page despite multiple references
- GPU-Poor Solutions: Focus area but no page
- Edge AI: Focus area but no page
- Missing pages: RAG, vLLM, Ollama, MCP Servers

## 2026-04-18

### ingest | llama.cpp

Ingested source: "llama CPP restyle is the workshop for your Local A.txt" from raw/

Created wiki pages:
- [[llama.cpp]] - Main summary for the inference library
- [[llama-cli]] - Terminal chat interface
- [[llama-server]] - Local server with WebUI
- [[Local LLMs]] - Category page updated

Updated:
- [[wiki/index.md]] - Added Local AI pages
- [[Knowledge Base Gaps]] - Marked Local LLMs as filled

Notes:
- Fills the Local LLMs gap identified during //wiki-explore
- llama-server provides model routing (dynamic load/unload)
- OpenAI API compatible - integrates with Bifrost

## 2026-04-18

### ingest | Embeddings & RAG

Ingested source: "Blaming embeddings is blaming the entire AI game.md" from raw/ (via //wiki-pdf)

Created wiki pages:
- [[Embeddings]] - Concept page for numerical vectors
- [[Cosine Similarity]] - Semantic similarity metric
- [[RAG]] - Retrieval Augmented Generation page (fills gap)

Updated:
- [[wiki/index.md]] - Added new pages to Knowledge Management

Notes:
- Fills the RAG gap from //wiki-explore
- Aligns with existing [[RAG vs LLM Wiki]] page
- No contradictions detected
- Key insight:Embeddings are the "lingua franca" of LLMs

## 2026-04-18

### ingest | Contextual Retrieval

Ingested source: "Is RAG Dead__ Anthropic Says No.md" from raw/ (via //wiki-pdf)

Created wiki pages:
- [[Contextual Retrieval]] - Anthropic's enhanced RAG technique
- [[Re-ranking]] - Post-retrieval refinement technique

Updated:
- [[wiki/index.md]] - Added Contextual Retrieval, Re-ranking to Knowledge Management
- [[RAG]] - Added RAG enhancements section
- [[Embeddings]] - Added backlink to Contextual Retrieval

Notes:
- No contradictions detected with existing content
- 49% retrieval failure reduction complements standard RAG
- Best results: contextual retrieval + BM25 + re-ranker = 1.9% error rate
- Fills Knowledge Management gap for RAG enhancement techniques

## 2026-04-18

### ingest | RAG Implementation Guide

Ingested source: "RAG_ What Nobody Tells You When Building Your AI Assistant.md" from raw/ (via //wiki-pdf)

Created wiki pages:
- [[Chunking]] - Document splitting technique

Updated:
- [[wiki/index.md]] - Added Chunking to Knowledge Management
- [[RAG]] - Added practical implementation tips section
- [[Embeddings]] - Added model selection advice
- [[Cosine Similarity]] - Added retrieval tuning context

Notes:
- No contradictions detected with existing content
- Key insight: Chunking is "everything" - directly affects retrieval quality
- bge-small-en outperformed text-embedding-ada-002 by 2x (new embedding model comparison)
- Different vector DBs for dev vs production scaling
- Fills the practical/implementation gap in RAG knowledge

## 2026-04-18

### ingest | Hierarchical Reasoning Model

Ingested source: "This New AI is 100x Faster at Reasoning Than ChatGPT.md" from raw/ (via //wiki-pdf)

Created wiki pages:
- [[Hierarchical Reasoning Model]] - Brain-inspired tiny model with breakthrough reasoning

Updated:
- [[wiki/index.md]] - Added new AI Models & Architectures section
- [[Local LLMs]] - Added backlink to HRM

Notes:
- No contradictions detected with existing content
- HRM is 27M parameters vs GPT-1's 117M (4x smaller)
- 40.3% on ARC-AGI vs 34.5% for o3-mini-high
- Solved 55% of Sudoku-Extreme puzzles where Claude 3.7 scored 0%
- Can be trained in just 2 GPU hours
- Proves architecture matters more than size
- Directly relevant to GPU-Poor Solutions focus area

## 2026-04-18

### update | Hierarchical Reasoning Model (additional source)

Ingested source: "Hierarchical Reasoning Model_ Ultra-Efficient, Brain-Inspired AI.md" from raw/ (via //wiki-pdf)

Updated:
- [[Hierarchical Reasoning Model]] - Added technical details section

Added:
- Latent space reasoning (100x faster than token-by-token)
- Data efficiency (~1,000 examples vs millions/billions)
- Real-world applications (autonomous systems, edge AI, healthcare, finance, logistics)
- Limitations (transparency, security, untested in creative domains)
- Future directions (multi-modal, explainability modules)

Notes:
- No contradictions detected - new source validates existing page
- Additional depth for the HRM page previously created

## 2026-04-18

### ingest | AI Usage Checklist

Ingested source: "23 Questions Every Heavy AI User Should Ask.md" from raw/ (via //wiki-pdf)

Created wiki pages:
- [[AI Usage Checklist]] - 23-question monthly self-reflection framework

Updated:
- [[wiki/index.md]] - Added AI Usage Checklist to AI Tools & Agents

Notes:
- No contradictions detected with existing content
- 23 questions across 5 categories: work, skills, growth, habits, dependency
- Historical precedents: Seneca, Loyola, Franklin, Gawande (checklist principle proved)
- Monthly review culture for AI users - first of its kind in the knowledge base
- Complements [[Knowledge Compounding]] and [[LLM Wiki Pattern]]

## 2026-04-18

### explore | Knowledge Base Gaps

Ran //wiki-explore to identify gaps and opportunities.

Created:
- [[GPU-Poor Solutions]] - Strategies for limited hardware

Updated:
- [[wiki/index.md]] - Added GPU-Poor Solutions to Local AI
- [[Knowledge Base Gaps]] - Marked GPU-Poor Solutions as filled
- [[Local LLMs]] - Now references GPU-Poor Solutions

Gaps identified:
- GPU-Poor Solutions ✅ FILLED
- Edge AI (still needs source)
- Ollama (no page)
- vLLM (no page)

## 2026-04-19

### ingest | NVIDIA NIM

Ingested source: "Are you too a Poor GPU guy Here s how to run 400B.txt" from raw/

Created wiki pages:
- [[NVIDIA NIM]] - Free API for 93+ frontier models (Llama 3.3, Mistral, DeepSeek)

Updated:
- [[wiki/index.md]] - Added NVIDIA NIM to AI Infrastructure
- [[GPU-Poor Solutions]] - Added free APIs section (NVIDIA NIM, OpenRouter)
- [[llm-providers.md]] - Added NVIDIA NIM as provider

Notes:
- No contradictions detected with existing content
- Free tier: 1,000 credits (expandable to 5,000) or ~40 requests/minute
- OpenAI-compatible API - easy integration
- Portability: same NIM container runs locally on NVIDIA hardware
- Key value: Access to 400B+ parameter models without GPU
- Supports reasoning models with visible "inner monologue"

## 2026-04-20

### ingest | Gemma 4

Ingested source: "Gemma 4 on the Edge high performance AI for the .txt" from raw/

Created wiki pages:
- [[Gemma 4]] - Google's edge-optimized open models for local AI

Updated:
- [[wiki/index.md]] - Added Gemma 4 to AI Models & Architectures
- [[GPU-Poor Solutions]] - Added edge-optimized models section (Gemma 4 E2B/E4B)
- [[Local LLMs]] - Added Gemma 4 to model options

Notes:
- No contradictions detected with existing content
- Edge models (E2B/E4B): 2B/4B params, 128K context, thinking mode
- Runs on 4-thread CPU at ~6 tokens/second
- Native system prompt support (the biggest missing feature from Gemma 2)
- Long context: 128K (edge) / 256K (large) tokens
- Free API: Google AI Studio offers 1500 calls/day (Gemma 4 free)
- Network setup: Expose llama-server on local network for remote access
- Integrates with Perplexica (local Perplexity alternative)
- Fills the Edge AI gap from //wiki-explore