# How to Use OpenCode to Build Your Personal Learning Playground: The Instruction Stack That Changed Everything

I need to confess something. For months, I treated my AI coding assistant like a fancy autocomplete. I'd type a prompt, it would write some code, and I'd manually fix whatever it got wrong. Rinse and repeat. It felt productive at the time, but I was leaving 80% of the tool's potential on the table.

That changed when I finally understood the instruction stack — that layered system of configuration files, skills, and commands that turns a dumb chatbot into something that actually knows your project, your preferences, and your workflows. I'm talking about AGENTS.md, Skills, Commands, and how they all interconnect. Most tutorials skip over this entirely, which is why I almost gave up.

I've been using Claude Code for a while, and honestly,

These concepts that work in Claude Code also apply to OpenCode. Once you see the pattern, you can't unsee it. And honestly, that's when everything started to actually work.

## The Moment Everything Clicked

I remember debugging yet another broken implementation. This time a refactor that went sideways because I hadn't explained my naming conventions to the AI. It used camelCase everywhere, but my codebase is snake_case. Every file needed fixing. Forty-seven files. That's when I snapped.

That's when I had a thought: there's got to be a better way. And there was.

The secret is understanding that your AI assistant starts every session with zero knowledge of your project. Not your build commands. Not your architecture. Not the quirks that make your code base unique. Nothing. It's like hiring a senior engineer who's incredibly talented but has never seen your codebase. You get to explain everything, every single time.

Until you learn how to give it a memory.

That's what the instruction stack does. It gives your AI permanence. Context that survives between sessions. Rules it actually follows. And once you set it up correctly, you stop repeating yourself. Month one is the work. Month two is the compound. By month three, your AI runs your project workflows the way you'd run them yourself — because you took thirty minutes once to write down exactly how that looks.

One thing you might not know: you don't need Claude Code to use these principles. OpenCode supports the same concepts, and in some ways, it's even more flexible. Let me show you exactly how it works.

## Understanding OpenCode's Architecture

Before we get into the instruction files, you need to understand what you're actually working with. OpenCode isn't just a chatbot with a terminal. It's an agent orchestration framework — which is a fancy way of saying it's a system that manages the loop between reasoning and execution.

The architecture has layers:

**The Core**: This is where your prompts go and your code comes out. The main agent (called the Primary Agent) handles the conversation flow and makes decisions.

**The Tools**: Read, Write, Edit, Glob, Grep, Bash. Your AI can manipulate files, run commands, and search through your codebase.

**The Memory Layer**: This is where AGENTS.md lives. It's loaded automatically at the start of every session, giving your agent context about your project.

**The Extensibility Layer**: Skills, Commands, and Hooks. These are modular additions that customize how your agent behaves.

Each layer solves a specific problem. Most developers only use the first two. That's fine, but it leaves roughly 80% of the tool on the table.

The simple version:

```
OpenCode Architecture
        │
        ▼
┌─────────────────────────────┐
│    User Interaction       │  ← prompts, commands, files
├─────────────────────────────┤
│   Primary Agent (Brain)    │  ← reasoning, decision-making
├─────────────────────────────┤
│   Tool Access Layer       │  ← Read/Write/Edit/Grep/Bash
├─────────────────────────────┤
│  Memory System           │  ← AGENTS.md auto-loaded
├─────────────────────────────┤
│ Extensibility (Skills/   │  ← modular capabilities
│  Commands/Hooks)          │
└─────────────────────────────┘
```

This matters because it tells you where to invest your time. The top layers are where you interact. The bottom layers determine how well your agent performs. The instruction stack sits right in the middle, and it sits at the highest-impact point in the entire system.

## The AGENTS.md File: Your Project's Memory

In Claude Code, this file is called CLAUDE.md. In OpenCode, it's AGENTS.md. Same concept, different name. And honestly, this is the single most important file you'll create for your project.

What most people get wrong: they treat AGENTS.md like a wish list. They write what they want the AI to be — experienced, thoughtful, careful — rather than what they need it to know.

A wish list doesn't change behavior. A technical brief does.

The file lives in your project root and gets loaded automatically at the start of every session. OpenCode considers it the definitive source for everything that comes after. If you get it right, you can brief a senior engineer about your project in just thirty seconds. If you get it wrong or omit it, you risk spending an hour with the AI trying to figure out your build commands, refactoring files you didn't specify, and committing a confusing mess.

The five sections that actually work:

After going through dozens of production AGENTS.md files from open-source projects and community best practices, every effective file covers exactly these five things:

### Section 1: Critical Commands

The AI doesn't know how to build, test, or lint your specific project. Tell it.

```markdown
## Commands
- Dev: `npm run dev`
- Build: `npm run build`
- Test single file: `npm test -- path/to/file`
- Test all: `npm test`
- Lint: `npm run lint:fix`
- Type check: `npx tsc --noEmit`
```

Short and specific. Without this section, the AI will attempt `npm test` on a project that uses `pnpm vitest` and spend three turns debugging a command that was never going to work. This section alone saves significant time on every single session.

### Section 2: Architecture Map

The AI starts every session with zero knowledge of your codebase. Give it a map — not a full directory tree, just enough to know where things live and what belongs where.

```markdown
## Architecture
- src/lib/services/      → all business logic
- src/components/       → stateless UI components only
- src/lib/store/         → global state (Zustand)
- src/app/api/           → API routes, no business logic here
- Database access only through Server Actions or API routes
```

This prevents the AI from putting business logic in a UI component, dropping state management in the wrong folder, or creating an API route that does things API routes in your project shouldn't do. One section, five lines, eliminates an entire class of architectural mistakes.

### Section 3: Hard Rules

This is the most important section in the file. Every rule here should pass a single test:

_Would removing this line cause the AI to make a mistake?_

If the answer is no, the line doesn't belong here.

```markdown
## Rules
- NEVER commit .env files or secrets
- All async calls must use try/catch
- Use functional components only, no class components
- Prefix commits: feat:, fix:, docs:, refactor:
- All PRs must pass `npm run verify` before merge
- IMPORTANT: run type check after every code change
```

Two things worth noticing here:

First, negative rules are just as important as positive ones. "Never commit .env files" prevents a potentially catastrophic mistake, while "Use functional components" avoids a stylistic issue. Both are essential.

Second, emphasis markers actually work. OpenCode's own documentation confirms that prefixing a rule with `IMPORTANT` meaningfully improves how reliably the AI follows it. Use `IMPORTANT` for the one rule the AI keeps breaking in your project.

Keep this section under fifteen rules. More than that and the important ones get diluted.

### Section 4: Workflow Preferences

This section answers the question: how do you want the AI to behave while it works?

```markdown
## Workflow
- Ask clarifying questions before starting complex tasks
- Make minimal changes, don't refactor unrelated code
- Run tests after every change, fix failures before moving on
- Create separate commits per logical change, not one giant commit
- When unsure between two approaches, explain both and let me choose
```

The second line — "make minimal changes, don't refactor unrelated code" — is often what people wish they'd included after the AI rewrote an entire file just to modify one function. The fifth line stops the AI from making architectural choices on its own.

These are workflow agreements, not personal characteristics. They influence behavior in ways you'll see right away.

### Section 5: What NOT to Include

Equally important is what you leave out. These things actively hurt your AGENTS.md by consuming instruction budget without contributing value:

```markdown
## Don't include:
- Personality instructions ("be a senior engineer")
- Code formatting rules your linter already handles
- @-imports that embed entire docs into every session
- Duplicate rules (if global says "run tests," project doesn't repeat it)
- Anything the AI will learn on its own via auto memory
```

That last point is underrated. OpenCode maintains its own notes at memory files. Run `/memory` in any session to see what it has already learned about your project from previous sessions. Don't waste AGENTS.md lines documenting things the AI figured out after one hour of work.

**The Mindset Shift That Makes This Click**

People treat AGENTS.md like a wish list. They write what they want the AI to be instead of what they need it to know.

A wish list doesn't change behavior. A technical brief does.

Focus on stack, commands, architecture, rules, and workflow. Everything else is noise vying for attention with the essential instructions. Keep it within eighty lines. Review it if the AI makes an error. Add a rule each time you identify a mistake you've already fixed twice.

A production-ready AGENTS.md template you can copy and adapt. Under sixty lines. Covers everything the AI needs, nothing it doesn't:

```markdown
# AGENTS.md

## Project
[One line: what this project does and who uses it]

## Stack
[Framework, language, database, deployment target]

## Commands
- Dev: `[command]`
- Build: `[command]`
- Test single: `[command] -- [path]`
- Test all: `[command]`
- Lint: `[command]`
- Type check: `[command]`

## Architecture
- [folder] → [what lives here]
- [folder] → [what lives here]
- [folder] → [what lives here]
- [file]   → [what this file does]

## Rules
- [Rule that prevents a specific mistake]
- [Rule that prevents a specific mistake]
- [Rule that prevents a specific mistake]
- IMPORTANT: [The one rule AI keeps breaking]

## Workflow
- [How you want AI to approach tasks]
- [Commit conventions]
- [Testing expectations]
- [When to ask vs when to act]

## Out of scope
- [Things AI should not touch]
- [Files that are manually maintained]
- [Integrations AI shouldn't modify]
```

Delete sections that don't apply to your project.

## Skills: Your Modular Toolbox

Skills are modular instruction packages that extend your AI's capabilities. Think of them like plugins or extensions for an AI agent. Some are community-built. Some you write yourself. Once you start customizing your agent workflow with the right skills, you'll wonder how you ever worked without them.

In OpenCode, Skills use a specific format. They're defined in YAML frontmatter with a description that tells OpenCode when to load them:

```yaml
---
name: skill-name-with-hyphens
description: Guides agents through [task/workflow]. Use when [specific trigger conditions].
---
```

**Why Skills Matter**

Without skills, you're starting from zero every session. With skills, you're starting from a foundation. The difference is everything.

What Skills accomplish:

They encode domain knowledge. If you work with a specific framework, database, or workflow, Skills teach the AI how to navigate your specific environment. Your company's CLI tools, your team's naming conventions, your infrastructure quirks — Skills capture all of it.

**They enforce consistency.** A Skill is a contract. It tells the AI exactly how to approach a task. No guessing. No assumptions. Just a repeatable process that works every time.

**They compound over time.** Every time you add a new workflow to your Skills — how to query specific metric namespaces, how to filter by your team's service tags, how to format alerts for your on-call channel — your future self gets faster.

**The Meta-Skill: Knowing What to Skill-ify**

After building and using Skills for a few months, a pattern emerged. The best candidates for Skills are:

**Repetitive workflows** — Anything you do weekly that requires remembering syntax or options. Code review, deployment checklists, monitoring queries.

**High-context tasks** — Things that require knowledge your agent doesn't have by default. Your company's CLI tools, your team's naming conventions, your infrastructure quirks.

**Output formatting** — How you want information presented. Token efficiency matters. The more concisely your AI communicates, the faster the responses and the lower your costs.

**Safety rails** — Things you want the agent to always check. A Skill that reminds OpenCode to run tests before committing. A Skill that invokes adversarial review to catch edge cases.

## Commands: Your Shortcuts

Commands are slash-initialized shortcuts that trigger specific workflows. In OpenCode, you invoke them with `/command-name`. They're essentially prompts saved for frequently-used tasks.

Commands do one of two things: invoke subagents for complex workflows or run simple bash scripts for utility operations. They get saved to configuration and are available across sessions.

What makes them powerful:

```markdown
/create-skill    → Invokes interactive skill creation
/validate-skill  → Comprehensive validation
/list-skills    → Shows all available skills
/refactor        → Runs refactoring workflow
/explain         → Explains code patterns
/security       → Runs security audit
```

Most commands either invoke subagents or run simple scripts. They're the fastest way to start frequently-used workflows. Instead of typing "Can you help me create a skill?" or explaining what you want, you just type `/create-skill` and the workflow starts immediately.

How this works in practice:

**Before understanding Commands:**
- "Can you help me create a skill for our deployment workflow?"
- [Explain workflow in detail]
- [Wait for AI to understand]
- [Refine based on clarifications]
- Minutes wasted

**After using Commands:**
- `/deploy-workflow [environment]`
- AI immediately executes the workflow
- Seconds saved, focus maintained

## The Complete Instruction Stack

The layers fit together like this:

```
┌─────────────────────────────────────────┐
│           Your Conversations            │
├─────────────────────────────────────────┤
│  Commands (/slash commands, quick actions)  │
├─────────────────────────────────────────┤
│  Skills (auto-triggered by context)     │
├─────────────────────────────────────────┤
│  AGENTS.md (memory, auto-loaded)        │
├─────────────────────────────────────────┤
│  OpenCode Core                        │
└─────────────────────────────────────────┘
```

Each layer has a different trigger mechanism, activation timing, and scope. Understanding when each loads is the key to building a personalized AI setup.

**AGENTS.md loads first** — it's the foundation. Every session starts here. It's your project brief.

**Skills load when needed** — triggered by context matching. Your description tells OpenCode when to invoke each skill. They're modular, loaded on demand.

**Commands load on invocation** — triggered explicitly by you. They're shortcuts, not auto-loading.

This hierarchy matters because it follows the principle of progressive disclosure. Start simple. Add complexity only when proven necessary.

## Comparing with Claude Code

Now, here's what you actually wanted to know: how do these concepts map to Claude Code?

| Concept | OpenCode | Claude Code |
|---------|---------|------------|
| Instruction file | AGENTS.md | CLAUDE.md |
| Auto-loading | By default | By default |
| Location hierarchy | Project root, home dir | Project, ~/.claude/, local |
| Skills | SKILL.md format | Native skill format |
| Commands | /slash commands | Native slash commands |
| Hooks | In settings.json | settings.json |

The architectures are remarkably similar. Both support:

- Instruction files that load every session
- Skills for modular capabilities
- Commands for shortcuts
- Subagents for parallel work
- Context management

The key difference is philosophy: OpenCode tends toward more explicit configuration while Claude Code handles more automagically. Both approaches have merit.

If you're wondering which to choose:

- **OpenCode** wins if you want maximum control, transparent configuration, and don't mind being explicit
- **Claude Code** wins if you want things to just work with less configuration overhead

Either way, the instruction stack concepts transfer. Learn them once, apply everywhere.

## The Lines With the Highest Impact

After testing various configurations, these particular lines led to the greatest enhancement in output quality — each addressing a common, predictable error:

```markdown
IMPORTANT: run type check after every code change
  → prevents AI from shipping broken types silently
Make minimal changes, don't refactor unrelated code
  → prevents AI from rewriting your entire file for a one-line fix
Create separate commits per logical change
  → prevents the 47-file monster commit
When unsure, explain both approaches and let me choose
  → prevents AI from making architectural decisions for you
```

Observe the pattern: each line is associated with the mistake it avoids. That's the test. If you cannot identify the mistake a rule prevents, then that rule likely doesn't belong in the file.

## Subagents: Parallel Workhorse

Subagents let you run multiple specialized AI instances simultaneously, each with its own context window, system prompt, tool permissions, and even model.

Your main session stays clean and high-level. The heavy work — deep research, security audits, test generation — happens in isolated contexts that hand back concise summaries.

Think of it this way: without subagents, you're stuck doing one thing at a time. With subagents, you can tackle multiple directions simultaneously. One agent writes code while another researches an API while a third runs tests. Parallel execution, singular focus.

**Creating a Subagent**

You define subagents in their own files with frontmatter that specifies their purpose, allowed tools, and model:

```yaml
---
name: code-reviewer
description: Reviews code for style, correctness, security, and performance.
tools: Read, Grep, Glob, Bash
model: sonnet
---
```

The tools line is critical. By default, subagents inherit all tools from the main session. Scope them deliberately. A research subagent doesn't need Write access. A code reviewer doesn't need Bash access to production.

**The Two-Agent Review Pattern**

This is one of the highest-impact techniques in this entire setup:

**Session A** implements a feature. It has all the context, made all the tradeoffs, took some shortcuts because you were moving fast.

**Session B** starts fresh. It has none of that context. It reads the diff cold. It will surface every shortcut, every assumption, every thing Session A took for granted. It's the most honest code review you'll ever get.

## Common Failure Modes

After months of iteration, these patterns kept coming up. What breaks most configurations:

### The 80/20 Rule Destroyer

People treat AGENTS.md like a comprehensive manual. They dump their entire engineering wiki into it, every convention, every process, every possible thing the AI might need to know.

AGENTS.md has an instruction budget. Most models can reliably handle 150-200 instructions at once. Your AI already receives instructions from its system prompt. Adding three hundred lines to AGENTS.md doesn't give you more compliance — it causes the AI to start dropping instructions entirely.

The fix: treat AGENTS.md as a thin layer, not an encyclopedia. Every line must earn its place.

### The Skill That Never Loads

You wrote a Skill. You described when to use it. And nothing happens.

This is usually a description problem. Your description is too vague. Compare:

**Doesn't work:**
```yaml
description: Provides information about testing
```

**Actually works:**
```yaml
description: Testing context for Python pytest workflows. Use when writing tests,
  running test suites, or debugging test failures. Do NOT load for frontend
  work or documentation tasks.
```

The difference is specificity and boundaries. You need to tell the AI what the Skill contains, when to load it, and when NOT to load it.

### The Command That Won't Shortcut

Your Command runs, but it takes five messages to set up. What's the point?

Commands work best when they need zero context. The ideal Command looks like:

```
/security-audit
```

And the AI immediately knows what to do, with no clarification needed.

If you find yourself explaining the same context before running a Command, that context belongs in the Command definition itself.

## Hooks: Automated Quality Gates

Hooks are where OpenCode starts feeling like infrastructure rather than just a tool. They're shell commands that run automatically at specific lifecycle points — before or after OpenCode writes a file, runs a command, or ends a session.

The key insight: hooks don't rely on the AI's judgment. They run whether the AI wants them to or not. That's the point.

What makes hooks powerful:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "npm run lint:fix"
          }
        ]
      }
    ]
  }
}
```

This simple hook runs your linter every time OpenCode writes a file. No manual intervention. No hoping the AI remembers to lint. It just happens.

Common hook use cases:

- **Post-write linting**: Automatically format code after writing
- **Pre-command validation**: Check if it's safe to run a command
- **Session summaries**: Capture what was done when session ends
- **Security scanning**: Detect potential secrets before they're committed

The best hooks are the ones you forget are there. They just work in the background, keeping your project healthy without asking for attention.

## Real-World Patterns That Work

Let me share three configurations I actually use:

### Pattern One: The Test-Driven Developer

```yaml
# AGENTS.md excerpt
## Rules
- Write tests BEFORE writing implementation
- Run tests after every change
- All PRs must pass test suite before merge
- IMPORTANT: never skip tests for speed
```

This seems obvious. But without it, the AI will happily write implementation code and skip the tests entirely because it wants to "move fast." The explicit rule changes the behavior.

### Pattern Two: The Minimalist

Some of my best configurations are the shortest. Forty lines. That's it.

```markdown
# Project name
## Stack
- React, TypeScript, Vite
- Vitest, Testing Library

## Commands
- Dev: `npm run dev`
- Test: `npm test`

## Architecture
- src/components/ → React components only
- src/lib/ → utilities, no business logic

## Rules
- Use functional components, no classes
- Test coverage required for new features
```

That's everything the AI needs. Nothing it doesn't.

### Pattern Three: The Enterprise Setup

```yaml
# Shared across teams: committed to git
## Project
- Enterprise CRM, team of 15 developers

## Stack
- Python 3.11, Django 4.2
- PostgreSQL 15, Redis
- Deployed to AWS ECS

## Commands
- Dev: `docker-compose up`
- Test: `pytest --cov`
- Deploy: `make deploy staging`

## Architecture
- api/ → Django REST endpoints
- services/ → business logic (no HTTP)
- models/ → Django ORM models only

## Rules
- NEVER import from services into api
- All endpoints require auth
- IMPORTANT: type check before commit
```

This is the pattern that scales. The same AGENTS.md works whether you're a new team member or a senior engineer. It's the team contract.

## The Bigger Picture

What separates the amateurs from the pros:

**Amateurs:** "I'll give the AI a task and see how it does."

**Pros:** "I'll design a system where the AI operates effectively with minimum supervision."

That's an infrastructure mindset applied to AI tooling. You invest time upfront — writing a tight AGENTS.md, setting up Skills, defining Commands — and that investment compounds on every session.

The developers shipping the most with OpenCode aren't the best prompters. They're the best system designers. They think about where context degrades and preempt it. They think about which quality gates should be automatic versus human-reviewed. They think about which parts of a task can run in parallel versus serially.

The analogy that fits best: it's not about being a better driver. It's about building a better road.

## Your Turn

What I'd actually change in my workflow tomorrow: open my AGENTS.md, strip out every rule the AI could figure out by reading the codebase, ensure the four behavioral lines are present if they're not already there, and judge every future rule I'm tempted to add by one question:

Does this shape how the AI thinks, or just what it does?

If it's the latter, it probably doesn't belong in the file.

The AI will keep getting smarter. The tools will keep getting more powerful. The bottleneck will stay behavioral until the AI learns to manage its own judgment. And until then, these configuration patterns will keep doing more per character than any feature announcement.

Start small. Start now. Your future self will thank you.

## TL;DR

- Your AI starts with zero knowledge. AGENTS.md fixes that.
- Keep AGENTS.md under eighty lines. Focus on commands, architecture, rules, and workflow.
- Skills are modular. Commands are shortcuts. Both worth having.
- Four lines matter most: clarify before acting, minimize changes, verify outputs, ask when unsure.
- The instruction stack transfers between OpenCode and Claude Code. Learn once, apply everywhere.

Now go build your playground.

---

## Progressive Disclosure: When Complexity Actually Helps

Progressive disclosure changed how I think about the instruction stack. The idea comes from user interface design. Instead of showing every option at once, you show what's needed, and reveal more as context requires.

Applied to AI configuration:

**Tier One: The Bare Essentials**
- Your AGENTS.md has the build command
- One hard rule
- Total: under thirty lines

This covers eighty percent of sessions. Quick questions, simple edits, exploration.

**Tier Two: Task-Specific Instructions**
- A Skill for testing
- A Command for deployments
- A subagent for code review

These load only when needed. Your base config stays small.

**Tier Three: Situational Complexities**
- Environment-specific overrides
- Complex multi-step workflows
- Edge case handling

You don't need Tier Two on day one. You build toward it as you discover your patterns.

Don't build the full system before you need it.

**The test:** does this configuration make my daily work easier, or am I preparing for problems I don't have?

## Practical Example: My Setup

Let me walk through my actual OpenCode setup. This is what I use for my side projects:

```
.claude/
├── AGENTS.md              # 52 lines
├── settings.json         # hooks, basic config
├── commands/
│   └── create-skill.md    # custom command I use constantly
├── skills/
│   └── tdd-workflow/     # test-first methodology
└── agents/
    └── code-reviewer.md  # subagent for reviews
```

That's it. The full directory is under two hundred lines across all files.

I didn't build all this at once. I built it as I needed it:

1. Started with just AGENTS.md
2. Day three: added a Command for skill creation because I was typing the prompt too often
3. Week two: extracted the TDD workflow into a Skill after noticing the pattern
4. Month two: added the code reviewer subagent for parallel review

The compound is real.

**==> picture [dimensions] intentionally omitted <==**

---

**Next Steps**

1. Run `/init` in your main project
2. Delete seventy percent of what it generates
3. Add ONE rule: something the AI keeps getting wrong in your codebase
4. Save the file
5. Start your next session and notice the difference