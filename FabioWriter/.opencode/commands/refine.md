---
description: Start Refine workflow
---

Execute the Fabio Writer Article Refine workflow:

1. List all files in `draft/*.md` and ask user which article to refine
2. Read the selected draft
3. Check for:
   - Contradictions in the content
   - Stale/obsolete claims (verify current dates/info)
   - Orphaned concepts (topics mentioned but not developed)
   - Ensure target length is 4000-4500 words
4. Add FLUX prompts at the end of the draft:
   - Create 2 FLUX prompts per TOC section
   - Place in a "## FLUX Prompts" section with "### Section: [Section Name]" labels
   - Format:
     ```markdown
     ## FLUX Prompts

     ### Section: [Section Name]
     > FLUX prompt: <prompt>

     > FLUX prompt: <prompt>
     ```
5. Save the refined draft back to `draft/`
6. Confirm completion