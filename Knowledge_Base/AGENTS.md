# Knowledge Base Schema

## Identity
This is a personal knowledge base about Artificial Intelligence and Local AI.
It is maintained by an LLM agent. The human curates sources and asks questions. The LLM does everything else.

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
9. Append filename to .ingested-files.txt
10. A single source should touch 10-15 wiki pages

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

### //wiki-list
Lists unprocessed source files in raw/ directory for ingestion.

**Usage:** `/wiki-list`

**Behavior:**
1. Scan `raw/*.txt` and `raw/*.md` for source files
2. Read `.ingested-files.txt` to get already-ingested filenames
3. Return list of unprocessed files with numbers
4. Ask user which file to process (by number)
5. If user confirms, execute the ingestion prompt:
   ```
   process [FILENAME] from raw/. Read it fully, discuss key takeaways with me, then: create a summary page in wiki/, update wiki/index.md, update all relevant concept and entity pages, add backlinks, flag any contradictions, and append to wiki/log.md.
   ```

**Tracking:** After successful ingestion, append `[FILENAME]` to `.ingested-files.txt`

### //wiki-explore
Explores the knowledge base to find gaps, contradictions, and research opportunities.

**Usage:** `//wiki-explore`

**Behavior:**
1. Read wiki/index.md to understand current knowledge structure
2. Analyze the wiki to answer: "What should I research next based on what's here?"
3. Cite which wiki pages informed the answer
4. If new connections or insights are worth preserving, create a new page in wiki/
5. Update wiki/index.md if new pages are created

**Value questions to explore:**
- "What are the three biggest gaps in this knowledge base?"
- "Which sources disagree with each other, and on what?"
- "What should I research next based on what's here?"
- "Write a 500-word briefing on [topic] using only wiki content"

### //wiki-lint
Runs monthly health checks on the wiki to catch errors before they snowball.

**Usage:** `//wiki-lint`

**Behavior:**
1. Run full health check on wiki/ per the Lint Workflow section in AGENTS.md
2. Output to wiki/lint-report-[date].md with severity levels:
   - 🔴 errors: Critical issues (broken links, missing provenance, contradictions)
   - 🟡 warnings: Structural issues (orphans, missing cross-references)
   - 🔵 info: Suggestions and recommendations
3. Suggest 3 articles to fill the biggest knowledge gaps

**Why it matters:** When AI writes something slightly wrong and you save it back, the next answer builds on the wrong thing. Two months later, you have five pages reinforcing the same error. Health checks catch this before it snowballs.
**Frequency:** Monthly - non-negotiable to keep the system trustworthy.

### //wiki-pdf
Converts PDF sources to markdown for ingestion.

**Usage:** `//wiki-pdf`

**Behavior:**
1. Scan `raw/*.pdf` for PDF files
2. Return list of unprocessed PDFs with numbers
3. Ask user which PDF to convert (by number)
4. Run: `python ingest-pdf.py '[FILENAME]' --output-dir .\raw`
5. Show converted markdown output
6. Delete original PDF from raw/
7. Ask user if they want to process the converted file (same as //wiki-list workflow)

**Note:** `ingest-pdf.py` must be in knowledge base root.



### //wiki-help
Lists all available custom commands with brief descriptions.
**Usage:** `//wiki-help`

**Behavior:**
1. Read AGENTS.md Custom Commands section
2. Display list of all commands with their descriptions

**Available commands:**
- `//wiki-list` - Lists unprocessed source files in raw/ for ingestion
- `//wiki-explore` - Finds gaps and research opportunities in the knowledge base
- `//wiki-lint` - Runs monthly health checks on the wiki
- `//wiki-pdf` - Converts PDF sources to markdown for ingestion
- `//wiki-help` - Lists all available commands (this command)
- `/graphify` - Turn any folder into a knowledge graph with community detection

### //graphify
Turns any folder into a knowledge graph with community detection and audit trail.

**Usage:** `/graphify [path] [--options]`

**Behavior:**
1. Invoke the Skill tool with `skill: "graphify"` — pass through the full invocation
2. Follows the workflow in .opencode/skills/graphify/SKILL.md

**Options:**
- `--mode deep` - Thorough extraction, richer INFERRED edges
- `--update` - Incremental: re-extract only new/changed files
- `--cluster-only` - Re-run clustering on existing graph
- `--no-viz` - Skip visualization, just report + JSON
- `--svg` - Also export graph.svg
- `--neo4j` - Generate cypher.txt for Neo4j import

**Query subcommands:**
- `/graphify query "<question>"` - BFS traversal to answer questions
- `/graphify path "NodeA" "NodeB"` - Find shortest path between concepts
- `/graphify explain "<concept>"` - Plain-language explanation of a node
