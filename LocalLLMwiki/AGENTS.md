# Knowledge Base Schema

## Identity
This is a personal knowledge base about Artificial Intelligence and Local AI.
Maintained by an LLM agent. The human curates sources and asks questions. The LLM does everything else.

## Architecture
- raw/ contains immutable source documents. NEVER modify files in raw/.
- wiki/ contains the compiled wiki. The LLM owns this directory entirely.
- outputs/ contains generated reports, analyses, and query answers.

## Wiki Conventions
- Every topic gets its own .md file in wiki/
- Every wiki file starts with YAML frontmatter:
  ---
  title: [Topic Name]
  created: [Date]
  last_updated: [Date]
  source_count: [Number of raw sources that informed this page]
  status: [draft | reviewed | needs_update]
  ---
- After frontmatter, a one-paragraph summary
- Use [[topic-name]] for internal links between wiki pages
- Every factual claim cites its source: [Source: filename.md]
- When new info contradicts existing content, flag explicitly:
  > CONTRADICTION: [old claim] vs [new claim] from [source]

## Index and Log
- wiki/index.md lists every page with a one-line description, by category
- wiki/log.md is append-only chronological record
- Log entry format: ## [YYYY-MM-DD] action | Description
  (Actions: ingest, query, lint, update)

## Ingest Workflow
When processing a new source:
1. Read the full source document
2. Discuss key takeaways with user
3. Create or update a summary page in wiki/
4. Update wiki/index.md
5. Update ALL relevant entity and concept pages across the wiki
6. Add backlinks from existing pages to new content
7. Flag any contradictions with existing wiki content
8. Append entry to wiki/log.md
9. A single source should touch 10-15 wiki pages

## Query Workflow
When answering a question:
1. Read wiki/index.md first to find relevant pages
2. Read all relevant wiki pages
3. Synthesize answer with [Source: page-name] citations
4. If answer reveals new insights, offer to file it back into wiki/
5. Save valuable answers to outputs/

## Lint Workflow (Monthly)
Check for:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Concepts mentioned but never explained
- Missing cross-references
- Claims without source attribution
Output: wiki/lint-report-[date].md with severity levels

## Focus Areas
- Artificial Intelligence 
- Generative AI on the Edge
- How to run your local AI even if you are GPU poor

## Custom Commands

### //wiki-pdf
Convert a PDF to markdown.

Process:
1. Glob all `raw/*.pdf` files
2. Display numbered list to user
3. User selects one
4. Run `python ingest-pdf.py '<path>' -output-dir .\raw\`
5. Delete original PDF from raw/
6. Read and display the generated markdown file

### //wiki-explore
Answer: "What should I research next based on what's here?"

Process:
1. Read wiki/index.md to understand current knowledge base
2. Answer the research question by synthesizing existing wiki pages
3. Cite sources using [Source: page-name] format
4. If new connections/insights emerge, create a new wiki page in wiki/
5. Update wiki/index.md with any new entries
6. Log action in wiki/log.md

The critical loop: good answers compound in the knowledge base just like ingested sources do. Every question makes the next answer better.

Example high-value questions:
- "What are the three biggest gaps in this knowledge base?"
- "Which sources disagree with each other, and on what?"
- "Write a 500-word briefing on [topic] using only wiki content"