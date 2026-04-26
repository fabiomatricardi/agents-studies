---
description: Start Write article workflow
---

Execute the Fabio Writer Article Writing workflow:

1. Read ALL files from `raw/*.md` to understand available topics
2. Identify 2-3 distinct topics/themes from the raw sources
3. Present the topics to the user and ask them to pick ONE
4. After user picks:
   - Draft a Table of Contents (3-5 sections)
   - Write a 4000-4500 word article following the style in `outputs/fabio_matricardi_style.md` (if it exists, otherwise use default Fabio Matricardi tone)
   - Save draft to `draft/` directory
5. After draft is written:
   - Move the used raw source files from `raw/` to `processed/`
6. Confirm completion with word count and file location