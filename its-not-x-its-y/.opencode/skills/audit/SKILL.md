---
name: audit
description: Audit draft articles against Fabio Matricardi voice and style rules from about-me.md
trigger: /audit
---

# /audit

Audit draft articles (.txt, .md) in the drafts/ folder against the voice, style, and writing rules from about_me/about-me.md.

## Usage

```
/audit                    # scan drafts/ and audit selected file
```

## What You Must Do

Follow these steps in order. Do not skip steps.

### Step 1 - Scan drafts/ directory

Find all `.txt` and `.md` files in the `drafts/` subdirectory. Use glob with pattern `drafts/*.{txt,md}`. Do NOT scan nested subdirectories.

If no files found, report "No draft files found in drafts/" and stop.

### Step 2 - User file selection

Present the found files to the user in a numbered list. Use the `question` tool to let them pick ONE file.

Example prompt: "Pick a file to audit:"

### Step 3 - Read the content

Read the selected file content using the `read` tool. Store the full content in memory for analysis.

### Step 4 - Load writing rules

Read the about_me/about-me.md file to extract the complete set of writing rules. Use path: `about_me/about-me.md`

### Step 5 - Audit the content

Perform a comprehensive audit checking ALL of the following categories:

#### 5.1 Hook Check
- Must start with personal identification: "Yes, I have been there too!" or "Damn, this happened to me too."
- Avoid: generic introductions that could apply to any article
- Location: first paragraph

#### 5.2 Stance Check
- Must take a strong stance or contrarian position
- Never write neutral pieces
- If no clear opinion, flag as inconsistency

#### 5.3 AI Vocabulary Scan
Scan for these forbidden words (exact match, case-insensitive):

```
revolutionize, supercharge, unlock, future-proof, 10x, game-changer, cutting-edge, delve, realm, harness, tapestry, paradigm, synergy, leverage, pivotal, meticulously, groundbreaking, democratize, seamless, scalable, robust, breakthrough, empower, streamline, frictionless, elevate, adaptive, effortless, data-driven, insightful, proactive, mission-critical, visionary, disruptive, reimagine, unprecedented, intuitive, leading-edge, synergize, accelerate, state-of-the-art, dynamic, immersive, predictive, transparent, proprietary, integrated, plug-and-play, turnkey, versatile, transformative, pioneering, trailblazing, unleash, holistic, garner, accentuate, showcase, boast, underscore, highlight, emphasize, commendable, testament, innovative, vibrant, unparalleled, intricate, intricacies
```

Additionally scan for:
- "It's not this, it's that" (binary framing pattern)
- Triad pattern: three adjectives/phrases in a row like "speed, efficiency, and innovation"

#### 5.4 Punctuation Check
- No em-dashes in non-dialogue content (signals AI generation)
- Heavy colon and semicolon use encouraged (Italian grammar influence)
- No contractions in formal writing

#### 5.5 Voice Check
- First person dominant ("I")
- Shifts to "you" for reader involvement
- Uses "we" in step-by-step practical sections
- Rhetorical questions for transitions between sections

#### 5.6 Structure Check
- BLUF: Bottom Line Up Front - give key takeaway first
- Ends with CTA + engagement question ("write in the comments what you think")
- Variable paragraph length - never uniform (signals AI)

#### 5.7 Word Count Check
- Should be 2000-3500 words
- 2000 words is sweet spot

#### 5.8 Technical Content Check
- Code examples must be practical/tested
- Jargon: explain once, then use correct term
- Write for beginners - assume reader can't code
- Images and GIFs required in technical articles

#### 5.9 Verification Check
- Claims about dates, releases, versions, features must be accurate
- Verify timeline claims - errors destroy credibility

#### 5.10 Header Style Check
- No capitalized headings (check for Title Case headers)

#### 5.11 Citation Check
- Use blockquotes for citations from philosophers, scientists (Asimov, etc.)
- Set apart, don't weave in

#### 5.12 Signature Patterns Check
Check for these preferences:
- References to "Poor GPU guy" or "The Poor GPU guy"
- Phrases from phrase bank: "If it works don't touch it", "Test it 10 times", "Be the benchmark", "Your AI your rules", etc.
- Self-deprecation humor
- References to background (teacher, former priest) when relevant

### Step 6 - Generate Report

Create a comprehensive audit report with:

1. **File analyzed**: filename
2. **Word count**: X words
3. **Inconsistencies by category**: Each issue with:
   - Category name
   - Specific issue description
   - Line number (if applicable)
   - Severity: CRITICAL / MAJOR / MINOR

4. **Summary**: Brief summary of overall compliance

5. **Score** (0-5):
   - **0**: Completely not compliant - major rule violations throughout
   - **1**: Very little compliant - most rules violated
   - **2**: Compliant but many AI signals - some AI vocabulary or patterns detected
   - **3**: Good but still many style/tone discrepancies - minor issues remain
   - **4**: Overall good - minor improvements possible
   - **5**: Fully compliant with Fabio Matricardi voice and style

Scoring criteria:
- AI vocabulary: -0.5 per major word found
- Missing hook: -1
- No stance: -1
- Em-dashes: -0.5
- Triad pattern: -0.5
- Binary framing ("It's not this, it's that"): -0.5
- Uniform paragraph length: -0.5
- Missing CTA: -0.5
- Word count outside 2000-3500: -0.5
- Contractions: -0.25 per instance
- Capitalized headings: -0.25 per instance

Calculate: Start at 5, subtract penalties, round to nearest 0.5.

### Step 7 - Save Report

Save the report to `drafts/audit-report-{filename}.md`

Format:
```markdown
# Audit Report: {filename}

**Date**: {YYYY-MM-DD}
**Word Count**: {X} words
**Score**: {X}/5 - {rating}

---

## Inconsistencies

### {Category}
- **{Severity}**: {description} (Line {N})

---

## Summary

{2-3 sentence summary}

---

## Recommendations

1. {Actionable recommendation}
```

### Step 8 - Display Results

Print the final score and summary to the user. Offer to show full report or answer questions.