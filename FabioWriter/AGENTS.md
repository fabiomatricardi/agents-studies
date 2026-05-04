# Fabio Writer

## Directories
- `raw/` - source docs (read-only, move to processed/ after use)
- `style-sources/` - author's past articles (read first for style)
- `draft/` - LLM owns article drafts
- `outputs/` - final outputs and style guide
- `processed/` - archived raw sources

## Workflow

### 1. Style setup (one-time)
- If `outputs/fabio_matricardi_style.md` exists → use it
- If missing → read all `style-sources/*.md`, analyze for tone, word patterns, structure, first-person usage → create style guide

### 2. Write article
- Read raw sources → identify 2-3 topics → user picks → draft TOC → write 3000-3500 words → move raw to processed/

### 3. Refine
- Check for contradictions, stale claims, orphaned concepts
- Target length: 3000-3500 words
- ask user if he wants to keep current count or reach the target lenght

### 4. Word count
- Use the word counter CLI to check article length:
```bash
python .\word_counter.py .\draft\[filename].md
```
- Target: 3000-3500 words
- The tool strips Markdown syntax (links, images, headers, bullets) before counting
