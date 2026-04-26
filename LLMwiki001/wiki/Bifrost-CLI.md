---
title: Bifrost-CLI
created: 2026-04-09
last_updated: 2026-04-09
source_count: 1
status: reviewed
---
Bifrost-CLI is an interactive terminal tool that connects coding agents like Opencode, Claude Code, Codex CLI, and Gemini CLI to the Bifrost AI gateway with zero manual configuration. It automatically handles base URLs, API keys, model settings, and agent installation while providing a persistent tabbed terminal UI for managing multiple agent sessions.

Key capabilities include:
- Auto-configuration of base URLs, API keys, and model settings for each coding agent
- Fetching available models from the Bifrost gateway's /v1/models endpoint
- Installing missing agents via npm when needed
- Auto-attaching Bifrost's MCP server to Claude Code for tool access
- Launching agents in a persistent tabbed terminal UI with session switching
- Per-tab activity badges showing progress, idle status, or alerts
- Secure storage of virtual keys in OS keyring (never plaintext on disk)

Bifrost-CLI works with the Bifrost gateway to provide seamless provider switching, fallback handling, and budget/rate limit controls without requiring application code changes. This enables zero-configuration AI-assisted coding sessions with Opencode and other agents.

[Source: Bifrost-CLI-is-the-AI-gateway-for-coding-agents-we]