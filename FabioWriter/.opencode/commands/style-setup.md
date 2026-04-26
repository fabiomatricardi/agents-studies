---
description: Run Style setup workflow (one-time)
---

Execute the Fabio Writer Style Setup workflow:

1. Check if `outputs/fabio_matricardi_style.md` exists
2. IF it exists:
   - Inform the user: "Style guide already exists at outputs/fabio_matricardi_style.md"
   - Ask: "Do you want to regenerate it, or use the existing one?"
   - If user wants to regenerate → proceed with step 3
   - If user wants to keep existing → confirm and stop
3. IF it does NOT exist:
   - Read ALL files from `style-sources/*.md`
   - Analyze each for: tone, word patterns, structure, first-person usage, colloquialisms
   - Create `outputs/fabio_matricardi_style.md` with the style guide
   - Confirm completion to user

Use the author's persona: "I" perspective, fellow learner tone, encouraging, admits limitations, "Poor-GPUguy" identity.