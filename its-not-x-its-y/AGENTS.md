# AGENTS.md

This file contains project-specific instructions for AI agents working in this codebase.

## Default Configuration

All AI agent sessions MUST reference **[about_me/about-me.md](../about_me/about-me.md)** as the default voice, style, and rules guide for all writing tasks.

Apply the profile in about-me.md silently in every response unless explicitly overridden by project-specific instructions.

## Project Context

This is the workspace for "The Poor GPU guy" - articles and code about running AI locally on old hardware (CPU only).

## Key Rules

- Verify all timeline claims before writing (dates, releases, versions) - use web search when needed
- Practical code examples MUST be tested personally before writing
- No AI vocabulary (see avoid list in about-me.md)

## Writing Standards

- 2000-3500 words per article
- First person voice, strong stances
- No empty neutrality
- Variable paragraph length

## Skills

# audit
- **audit** - Audit draft articles against Fabio Matricardi voice and style rules from about-me.md. Trigger: /audit
When the user types /audit, invoke the Skill tool with skill: "audit" before doing anything else.