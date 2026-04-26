---
title: Bifrost-CLI
created: 2026-04-17
last_updated: 2026-04-17
source_count: 1
status: draft
---

Bifrost-CLI is an interactive terminal tool that connects coding agents to a Bifrost gateway with zero manual configuration. Instead of setting environment variables, editing config files, and looking up provider paths, users simply run `bifrost` and pick their agent, model, and go.

## What It Does

- Automatically configures base URLs, API keys, and model settings for each agent
- Fetches available models from the Bifrost gateway's /v1/models endpoint
- Installs missing agents via npm if needed
- Auto-attaches Bifrost's MCP server to Claude Code for tool access
- Launches agents inside a persistent tabbed terminal UI
- Shows per-tab activity badges for session status (progressing, idle, alert)
- Stores selections securely (virtual keys go to OS keyring, never plaintext)

## Supported Agents

Bifrost-CLI works out-of-the-box with:
- [[Opencode]]
- Claude Code
- Codex CLI
- Gemini CLI

If a harness isn't installed, the CLI will offer to install it via npm.

## Usage

1. Ensure Bifrost gateway is running
2. Run `bifrost` command
3. Enter gateway URL (e.g., http://localhost:8080)
4. Enter virtual key if enabled
5. Select coding agent
6. Select model from available options
7. Launch and start coding

## Related Concepts

- [[Bifrost]]: The AI gateway that Bifrost-CLI connects to
- [[Coding Agents]]: AI coding assistants that Bifrost-CLI can launch
- [[MCP Servers]]: Model Context Protocol servers that Bifrost-CLI auto-attaches to Claude Code