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
   - count the words: ask user if he wants to keep current count or reach the target lenght of 3000-3500 words
4. Save the refined draft back to `draft/`
5. Generate image prompts from the refined article:
   - Read the entire article and identify each section
   - For each section, create 2 distinct image prompts that convey the section's message
   - Follow the format of `prompts.json` in the project root: `[{ "id": 1, "prompt": "..." }, ...]`
   - Save to `draft/_prompts.json` (use the same filename as the original article)
6. Ask user for output filename for image generation (e.g., "newimages")
7. Run the image generation command:
   ```
   python bulk_gen.py <output_filename>.png --file .\draft\_prompts.json --password pippo
   ```
8. Confirm completion with:
   - Refined article location
   - Prompts JSON location
   - Generated images confirmation