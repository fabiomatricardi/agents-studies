---
description: Display all available commands and AGENTS.md
---

Display the Fabio Writer command reference:

## Available Commands

| Command | Description |
|---------|-------------|
| `/style-setup` | Run Style setup workflow (one-time). Checks if style guide exists, creates if needed. |
| `/write` | Start Write article workflow. Pick topic → draft TOC → write 4000-4500 words → move raw to processed/ |
| `/audit` | Audit draft article against VOICE DNA rules. Lists draft/*.md files and lets you select which to audit. |
| `/refine` | Start Refine workflow. Check contradictions, stale claims, orphaned concepts → generate image prompts → run bulk_gen.py |
| `/style-help` | Display this help message |

## Usage

- `/style-setup` - Run once at project start
- `/write` - When ready to write a new article
- `/audit` - When you want to audit a draft against VOICE DNA rules
- `/refine` - After draft is complete, before publishing
- `/style-help` - When you need a reminder

## Project Context (AGENTS.md)

Display the contents of AGENTS.md below. Read it and summarize the key workflow points for the user.