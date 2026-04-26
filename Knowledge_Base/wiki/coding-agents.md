---
title: Coding Agents
created: 2026-04-17
last_updated: 2026-04-17
source_count: 1
status: draft
---

AI coding agents are AI assistants that can execute software engineering tasks. They can read, write, and modify code, run commands, and work on multi-step tasks.

## Examples

- [[Opencode]]: Interactive CLI tool for coding tasks
- Claude Code: Anthropic's coding agent
- Codex CLI: OpenAI's coding agent
- Gemini CLI: Google's coding agent

## Connecting to LLM Providers

Coding agents typically need to connect to LLM providers via API. Tools like [[Bifrost-CLI]] provide zero-config setup to connect these agents to [[AI Gateways]] like [[Bifrost]], which then route requests to various [[LLM Providers]].

## Related Concepts

- [[AI Gateways]]: Middleware for routing LLM traffic
- [[LLM Providers]]: Services providing LLM APIs
- [[Local LLMs]]: Self-hosted models for coding tasks
- [[MCP Servers]]: Tools that extend agent capabilities