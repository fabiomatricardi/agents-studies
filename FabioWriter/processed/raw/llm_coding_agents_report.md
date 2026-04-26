# Open-Source LLM Coding Agents Report

Report date: 2026-04-24 UTC. This report ranks 10 open-source LLM coding agents by GitHub popularity and an original capability score that weighs model breadth, sessioning, agent features, IDE/LSP-style integration, and current project activity. GitHub repository metrics in the table were collected live from the GitHub API during report generation.

## Ranking table

| Rank | Agent | GitHub stars | Capability score | Supported models/providers | LSP / IDE integration | Multi-session | Subagents | Community activity |
|---|---|---:|---:|---|---|---|---|---|
| 1 | OpenHands [cite:19][cite:16] | 71985 | 83.8 | LLMs via LiteLLM incl. OpenAI, Anthropic, open models [cite:19][cite:16] | Not LSP-centric; sandbox/browser/tools [cite:19][cite:16] | Yes, multiple conversations/tasks [cite:19][cite:16] | Agent architecture, not marketed as subagents [cite:19][cite:16] | High |
| 2 | Open Interpreter [cite:30] | 63296 | 61.4 | OpenAI, Anthropic, local models incl. Ollama [cite:30] | No [cite:30] | Chat sessions [cite:30] | No [cite:30] | High |
| 3 | Cline [cite:7][cite:10] | 60949 | 74.9 | Anthropic, OpenAI-compatible, Gemini, Bedrock, Vertex, Ollama, LM Studio, OpenRouter and more [cite:7][cite:10] | MCP/tool integrations rather than LSP-first [cite:7][cite:10] | Task/history sessions in IDE [cite:7][cite:10] | Custom modes, MCP servers; no clear built-in subagents [cite:7][cite:10] | High |
| 4 | GPT Engineer [cite:30] | 55220 | 46.1 | OpenAI and configurable backends/community forks [cite:30] | No [cite:30] | Project iterations rather than true sessions [cite:30] | No [cite:30] | Lower |
| 5 | Aider [cite:6][cite:9] | 43874 | 68.4 | OpenAI, Anthropic, Google Gemini, DeepSeek, xAI, Ollama/OpenRouter and many APIs [cite:6][cite:9] | No dedicated LSP focus [cite:6][cite:9] | Limited; mainly one chat per repo/branch workflow [cite:6][cite:9] | No native subagents [cite:6][cite:9] | High |
| 6 | Continue [cite:17][cite:20] | 32770 | 62.2 | Anthropic, OpenAI, Azure, Gemini, Mistral, Ollama, OpenRouter, local models [cite:17][cite:20] | Strong IDE integration; context/indexing more than raw LSP marketing [cite:17][cite:20] | Workspace/chat threads depend on IDE extension [cite:17][cite:20] | No native subagents [cite:17][cite:20] | High |
| 7 | Roo Code [cite:12][cite:13][cite:15] | 23345 | 67.0 | Anthropic, OpenAI-compatible, Gemini, OpenRouter, Ollama and more [cite:12][cite:13][cite:15] | MCP/tooling focus [cite:12][cite:13][cite:15] | Yes, multi-mode workflows [cite:12][cite:13][cite:15] | Yes, mode-based specialist agents / whole dev team framing [cite:12][cite:13][cite:15] | High |
| 8 | SWE-agent [cite:29] | 19050 | 29.6 | GPT-4o, Claude Sonnet 4, open-source models [cite:29] | No; CLI/env tools for repo tasks [cite:29] | Batch runs/trajectories rather than interactive sessions [cite:29] | No [cite:29] | High |
| 9 | Plandex [cite:30] | 15289 | 48.7 | OpenAI, Anthropic, OpenRouter, local/open models [cite:30] | No explicit LSP [cite:30] | Yes, branches/plans/sessions [cite:30] | Planned/agentic execution, limited explicit subagents [cite:30] | Lower |
| 10 | OpenCode [cite:2][cite:3][cite:5] | 12184 | 36.2 | Any provider incl. Claude, GPT, Gemini; free models mentioned [cite:2][cite:3][cite:5] | Unknown/public docs not explicit [cite:2][cite:3][cite:5] | Yes (sessions) [cite:2][cite:3][cite:5] | Agents/plugins ecosystem [cite:2][cite:3][cite:5] | Lower |

## Method

Popularity rank is ordered by current GitHub stars from the project repository, while the capability score is a 100-point heuristic combining popularity, provider breadth, workflow depth, multi-session support, subagent support, IDE or LSP-style integration, and recent project activity. The score is useful for relative comparison, not as a benchmark of coding quality or model intelligence.

## Agent notes

### OpenHands

Repository: `OpenHands/OpenHands`. Current GitHub stars: 71985; forks: 9071; last push: 2026-04-24T13:36:59Z. 2025-2026 docs expanded GitHub/cloud setup and hosted usage around repo-connected autonomous tasks. [cite:19][cite:16]

Supported providers/models: LLMs via LiteLLM incl. OpenAI, Anthropic, open models. Key workflow traits: LSP/IDE integration — Not LSP-centric; sandbox/browser/tools; multi-session — Yes, multiple conversations/tasks; subagents — Agent architecture, not marketed as subagents. [cite:19][cite:16]

### Open Interpreter

Repository: `OpenInterpreter/open-interpreter`. Current GitHub stars: 63296; forks: 5509; last push: 2026-04-22T08:19:21Z. Continues positioning around computer-use and code execution rather than repo-native PR automation. [cite:30]

Supported providers/models: OpenAI, Anthropic, local models incl. Ollama. Key workflow traits: LSP/IDE integration — No; multi-session — Chat sessions; subagents — No. [cite:30]

### Cline

Repository: `cline/cline`. Current GitHub stars: 60949; forks: 6268; last push: 2026-04-24T09:22:56Z. 2025-2026 positioning highlights Plan/Act modes and MCP integration, with site claims of large developer adoption. [cite:7][cite:10]

Supported providers/models: Anthropic, OpenAI-compatible, Gemini, Bedrock, Vertex, Ollama, LM Studio, OpenRouter and more. Key workflow traits: LSP/IDE integration — MCP/tool integrations rather than LSP-first; multi-session — Task/history sessions in IDE; subagents — Custom modes, MCP servers; no clear built-in subagents. [cite:7][cite:10]

### GPT Engineer

Repository: `AntonOsika/gpt-engineer`. Current GitHub stars: 55220; forks: 7318; last push: 2025-05-14T10:15:10Z. Project remains active but is less agentically differentiated; community uses it for scaffolding and experimentation. [cite:30]

Supported providers/models: OpenAI and configurable backends/community forks. Key workflow traits: LSP/IDE integration — No; multi-session — Project iterations rather than true sessions; subagents — No. [cite:30]

### Aider

Repository: `Aider-AI/aider`. Current GitHub stars: 43874; forks: 4289; last push: 2026-04-23T20:15:20Z. 2025-2026 docs emphasize broad model support, architect/editor model split, and stronger git-centric workflows. [cite:6][cite:9]

Supported providers/models: OpenAI, Anthropic, Google Gemini, DeepSeek, xAI, Ollama/OpenRouter and many APIs. Key workflow traits: LSP/IDE integration — No dedicated LSP focus; multi-session — Limited; mainly one chat per repo/branch workflow; subagents — No native subagents. [cite:6][cite:9]

### Continue

Repository: `continuedev/continue`. Current GitHub stars: 32770; forks: 4415; last push: 2026-04-24T02:43:50Z. 2025-2026 docs emphasize AI checks as native GitHub status checks plus configurable IDE assistants. [cite:17][cite:20]

Supported providers/models: Anthropic, OpenAI, Azure, Gemini, Mistral, Ollama, OpenRouter, local models. Key workflow traits: LSP/IDE integration — Strong IDE integration; context/indexing more than raw LSP marketing; multi-session — Workspace/chat threads depend on IDE extension; subagents — No native subagents. [cite:17][cite:20]

### Roo Code

Repository: `RooCodeInc/Roo-Code`. Current GitHub stars: 23345; forks: 3101; last push: 2026-04-24T10:58:22Z. 2025 releases and 2026 cloud GitHub integration expanded autonomous PR review/fix workflows. [cite:12][cite:13][cite:15]

Supported providers/models: Anthropic, OpenAI-compatible, Gemini, OpenRouter, Ollama and more. Key workflow traits: LSP/IDE integration — MCP/tooling focus; multi-session — Yes, multi-mode workflows; subagents — Yes, mode-based specialist agents / whole dev team framing. [cite:12][cite:13][cite:15]

### SWE-agent

Repository: `SWE-agent/SWE-agent`. Current GitHub stars: 19050; forks: 2058; last push: 2026-04-20T21:22:07Z. Project messaging in 2025 highlights autonomous issue fixing in real GitHub repos with model-choice flexibility. [cite:29]

Supported providers/models: GPT-4o, Claude Sonnet 4, open-source models. Key workflow traits: LSP/IDE integration — No; CLI/env tools for repo tasks; multi-session — Batch runs/trajectories rather than interactive sessions; subagents — No. [cite:29]

### Plandex

Repository: `plandex-ai/plandex`. Current GitHub stars: 15289; forks: 1123; last push: 2025-10-03T21:49:58Z. Focus remains long-running, multi-file terminal coding tasks with plan-oriented workflows. [cite:30]

Supported providers/models: OpenAI, Anthropic, OpenRouter, local/open models. Key workflow traits: LSP/IDE integration — No explicit LSP; multi-session — Yes, branches/plans/sessions; subagents — Planned/agentic execution, limited explicit subagents. [cite:30]

### OpenCode

Repository: `opencode-ai/opencode`. Current GitHub stars: 12184; forks: 1286; last push: 2025-09-18T02:54:28Z. GitHub repo created in 2025 and project docs now include GitHub workflow integration for issue/PR execution. [cite:2][cite:3][cite:5]

Supported providers/models: Any provider incl. Claude, GPT, Gemini; free models mentioned. Key workflow traits: LSP/IDE integration — Unknown/public docs not explicit; multi-session — Yes (sessions); subagents — Agents/plugins ecosystem. [cite:2][cite:3][cite:5]

## Takeaways

Aider, Continue, Cline, OpenHands, and Open Interpreter remain the most visible open-source projects by GitHub adoption, while Roo Code and OpenCode are newer but have strong agent-oriented positioning. For terminal-first use, Aider, OpenCode, and Plandex are strong fits; for editor-native use, Cline, Roo Code, and Continue are the clearest choices; for autonomous issue resolution and repo task execution, OpenHands and SWE-agent are the most directly aligned.