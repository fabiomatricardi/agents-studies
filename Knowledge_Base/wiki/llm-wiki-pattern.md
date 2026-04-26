---
title: LLM Wiki Pattern
created: 2026-04-18
last_updated: 2026-04-18
source_count: 1
status: draft
---

The LLM Wiki pattern, proposed by Andrej Karpathy, is a knowledge management architecture that compiles knowledge at ingest time rather than at query time. Unlike traditional RAG systems that re-retrieve and re-synthesize the same raw chunks on every query, the LLM Wiki synthesizes knowledge into interlinked markdown pages once, and queries run against this pre-organized, cross-referenced knowledge base. This creates a compounding effect where each subsequent source enriches existing pages rather than starting from zero. [Source: Beyond RAG How Andrej Karpathy s LLM Wiki Pattern.txt]

## Core Concept

The fundamental shift is from **stateless retrieval** to **stateful, compounding knowledge**. Every query in traditional RAG starts from zero - the same question asked three months later triggers the exact same retrieval and synthesis. The LLM Wiki pattern inverts this: knowledge is compiled once, and queries benefit from all accumulated understanding.

## Architecture

### Layer 1: Raw Sources
Immutable source documents (papers, articles, transcripts) that serve as the ground truth. Equivalent to your `raw/` directory. These are never modified - you can always re-derive the wiki from scratch.

### Layer 2: The Wiki
LLM-maintained markdown files - one per concept/topic/entity. Each page has YAML frontmatter with title, tags, provenance (which sources contributed), and last-updated timestamp. Pages cross-reference using [[slug]] notation. Your `wiki/` directory follows this exact pattern.

### Layer 3: Schema (Governance)
JSON file defining the page universe: which concepts the wiki tracks, their slugs, titles, and descriptions. The schema is the contract between human intent and LLM execution. This maps to your focus areas in AGENTS.md.

## Four Core Operations

### Init
Bootstrap directory structure from schema template.

### Ingest
The most important operation - knowledge compounding happens here:
1. **Route**: Determine which wiki pages are relevant to the source
2. **Synthesize**: Rewrite each relevant page, preserving existing knowledge while integrating new material
3. **Embed**: Re-embed updated pages for the vector index
4. **Update Index/Log**: Regenerate index.md and append to log.md

### Query
Standard RAG mechanics over synthesized wiki pages instead of raw chunks. With `--save`, valuable answers can be filed back as new wiki pages - completing the compounding loop.

### Lint
Health checks: orphaned pages, broken cross-references, stale embeddings, missing provenance. With `--deep`, checks for factual contradictions between pages.

## Comparison to Traditional RAG

See [[RAG vs LLM Wiki]] for detailed comparison.

## Your Knowledge Base

Your knowledge base at `C:\FABIO-AI\Knowledge_Base` already follows this pattern:
- `raw/` = immutable sources
- `wiki/` = LLM-maintained markdown with YAML frontmatter
- `wiki/index.md` = auto-updated catalog
- `wiki/log.md` = append-only operation record
- `.ingested-files.txt` = provenance tracking

This source validates your architecture - you are implementing the LLM Wiki pattern!

## Related Concepts

- [[Knowledge Compounding]]: The principle that knowledge accumulates over time
- [[RAG vs LLM Wiki]]: Comparison of retrieval approaches
- [[AI Gateways]]: Related infrastructure pattern
- [[Knowledge Bases]]: General category