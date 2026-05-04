# How to Build an Agent Engineering Playbook (That Your AI Actually Follows)

**The secret no one talks about: prompts are suggestions. Hooks are guarantees.**

At 49, I've been around the block a few times. I've seen frameworks come and go, watched paradigms shift, and honestly? I thought I had this whole AI coding thing figured out. 
I had my AGENTS.md file, my skills loaded, my project structure locked down tight. I was feeling pretty good about myself.
I mean, I managed to create myself a personal Knowledge Base in full Karpathy style only with free resources, so I am pretty proud of myself.

Now I am trying to apply all these concepts in different personal project:
- run a personal LLM-wiki with local LLM to build the engineering specifications of new projects again the standards
- feed my draft article to get grammar, punctuation corrections
- give the fina larticle, have the LLM suggest me image prompts and then generate the images with free API calls to Pixazo
and so on

But then, every few sessions, I'd come back and find Opencode trying to do things its own way. Skipping the spec. Forgetting the tests. Just... building. Building wrong, sometimes. Building without tests other times. Building stuff that barely matched what I asked for.

I cannot be 100% certain, but did it happen to you too?

Here's what I am finally starting to realize after months of frustration: prompts are suggestions. The model follows them most of the time, I'll give it that: but "most of the time" is not good enough when you're trying to ship real software. It is not totally good at all when 
- your deadline is tight
- your users are waiting
- your work cannot wait

What you need is **deterministic enforcement**: behavior that happens every single time, regardless of how the model is feeling, regardless of what else is in context, regardless of whether it "feels" like doing things the right way today.

That's where hooks come in. And when you combine them with Addy Osamani's Google engineering playbook, you've got something actually powerful. Not "sometimes works" powerful. 
Production-grade powerful.

## The Problem: Why Your Agent Keeps Forgetting the Rules

Let me paint the picture. You've got a clean project. You've written a thoughtful AGENTS.md (or CLAUDE.md) with everything spelled out: testing requirements, code style, documentation rules, the whole nine yards. Maybe you've even loaded some skills to help along the way.

You fire up a session and say:

> "Add user authentication to the app."

And the agent... just starts coding. With no spec, plan or tests in sight.

Maybe it'll circle back and add documentation at the end. Maybe it won't. Half the time you'll get tests covering your back. Half the time you won't. And that half? It's a gamble every single session.

And if you are running this with your Local AI, every token counts: not for the money, ut for the time! Long sessions with a huge KV-cahce (context) means long waiting time.

I've been there more times than I want to admit. 
Maybe more times than I'd like to count.

The issue is clearly not that the agent is dumb: with my surprise it is actually blazingly smart, most of the time. The problem is that prompts are probabilistic. The model weighs your instructions against everything else in context: its training, the conversation flow, the probability distributions for what comes next... all to make a decision. Sometimes that decision aligns with what you wanted. Sometimes it doesn't. Sometimes it decides that writing tests "later" is fine, and later never comes.

This is the gap between "usually works" and "production-grade." 
Most tutorials you can find stop at "here's how to prompt." Send a good message, get a good response, everyone's happy. Very few address the enforcement problem or acknowledge that hope is not a strategy.

## The Missing Piece: When Prompts Aren't Enough

I used to think more prompting was the answer. More details in CLAUDE.md. Stronger instructions with consequences spelled out. Warning about what happens if tests get skipped.

Didn't work.

I tried everything. I wrote 500-word instructions. I cited Google's engineering principles. I threatened (politely) that skipping tests would result in... well, nothing. The model just kept doing what it wanted.

Then I learned about **hooks**. They're not new. Claude Code has had them for a while, and OpenCode supports them too, but the mental model changed everything for me. This wasn't another tool to add to the pile. This was a different category of tool entirely.

> Note that here, when we talk about Claude Code, Codex, Gemini CLI or Opencode, all contepts applies the same. Remember that except for Claude Code, instead of using CALUDE.md we use AGENTS.md as main orchestrator file.

Think about it this way: prompts tell the model *what* to do. Hooks tell the system *when* to do it. Big difference.

A hook is a deterministic trigger. 
It fires at a specific point in the lifecycle (— )before a tool runs, after a file changes, when a session ends) and executes a script. No model judgment involved or probability. 

Here's the key insight from my research: **hooks are designed to introduce deterministic control at specific points in the lifecycle, rather than relying on the model to remember or prioritize the right behavior.**

That's the sentence that made me finally understand it. Deterministic. Control points. Specific lifecycle moments.

Instead of hoping the model remembers to run tests after every change, you add a hook that runs tests after every file edit. Instead of hoping it updates documentation when it should, you add a hook that checks documentation state before considering a task complete. Instead of hoping it formats code properly, you add a hook that formats code automatically after every write.

Prompts → suggestions (best effort)
Hooks → guarantees (every single time)

That's the difference. That's the gap between "usually works" and "production-grade."

## Google's Engineering Playbook for AI Agents

Now that we understand the enforcement problem, the gap between "usually works" and "actually works every single time", let's talk about the rules worth enforcing.

Addy Osmani spent 14 years at Google. Fourteen. He's seen the inside of one of the best engineering cultures on the planet, helped build Chrome DevTools from the ground up, authored books on JavaScript design patterns, and now leads Google Cloud AI. The guy has forgotten more about engineering than most of us will ever learn.

And he recently published a GitHub repo that's been gaining serious traction: **[agent-skills](https://github.com/addyosmani/agent-skills)**. One install, and your AI agents follow Google's engineering playbook. Not some watered-down version. The real deal:

```bash
npx skills add addyosmani/agent-skills
```

**What's actually in the repo:**

Twenty skills covering the full development lifecycle:

- **Define** ➡️ refine ideas and write specs before a single line of code
- **Plan** ➡️ split into smaller bite-sized chunks/tasks
- **Build** ➡️ incremental implementation, context engineering, clean design, TDD
- **Verify** ➡️ browser testing with DevTools
- **Review** ➡️ code quality, security hardening, performance optimization
- **Ship** ➡️ git workflow, CI/CD, ADRs, check-lists

Seven slash commands map to a lifecycle:

`/spec` → `/plan` → `/build` → `/test` → `/review` → `/code-simplify` → `/ship`

Skills activate automatically based on what you're doing. Tell the agent to build something, and it pulls in the build skill. Tell it to fix a bug ➡️ debugging skill. Tell it to review code — you get the idea.

These skills are  genuinely powerful, but they're still prompts. They work most of the time. Maybe 80%, maybe 90% if you've got good AGENTS.md rules reinforcing them.

To make them work *every* time? **That's where hooks come in**. We'll get there.

**Google Engineering Principles baked in:**

- **Hyrum's Law** ➡️ if you have enough users, every behavior of your system is depended on by someone
- **The Beyonce Rule** ➡️ if you like the outcome, put a test on it
- **Chesterton's Fence** ➡️ before removing something, understand why it was there
- **Shift Left** ➡️ don't find bugs after, find them before you even write code
- **Thunk-based dev** ➡️ short-lived branches, small changes, faster merges

These principles apply regardless of whether you adopt the full setup.

## Setting Up Addy Osamani's Skills in OpenCode

**Google Engineering Principles baked in — the real ones, not watered-down versions:**

Let's apply them (just few rows above) to a real use scenario:

- **Hyrum's Law** — if you have enough users, every behavior of your system is depended on by someone. Build accordingly.
- **The Beyonce Rule** — if you like the outcome, put a test on it (ring on it).
- **Chesterton's Fence** — before removing something, understand why it was there to begin with.
- **Shift Left** — don't find bugs after, find them before you even write code.
- **Thunk-based dev** — short-lived branches, small changes, faster merges.

These principles area always valid, they're worth having in your AGENTS.md even if you never touch the skills repo.

## Setting Up Addy Osamani's Skills in OpenCode

OpenCode doesn't have a native plugin system like Claude Code's `/slash` commands, that much is true. What it does have is flexibility. Instead, we achieve parity through:

- A strong system prompt (`AGENTS.md`)
- The built-in `skill` tool
- Consistent skill discovery from the `/skills` directory

This creates an agent-driven workflow where skills are selected and executed automatically, just like Claude Code. No manual `/this` or `/that` required.

But still you can tweak the `opencode.json` to achieve a similar action (better if you use both the custom commnands and the `j.son` file manual modification).
Here my example:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "command": {
    "refine": {
      "description": "Start Refine workflow",
      "template": "Execute the Fabio Writer Article Refine workflow:\n\n1. List all files in `draft/*.md` and ask user which article to refine\n2. Read the selected draft\n3. Check for:\n   - Contradictions in the content\n   - Stale/obsolete claims (verify current dates/info)\n   - Orphaned concepts (topics mentioned but not developed)\n   - Ensure target length is 4000-4500 words\n4. Check fro mispells and grammar mistakes\n5. Save the refined draft back to `draft/`\n6. Confirm completion"
    },
    "style-help": {
      "description": "Display all available commands and AGENTS.md",
      "template": "Display the Fabio Writer command reference:\n\n## Available Commands\n\n| Command | Description |\n|---------|-------------|\n| `/style-setup` | Run Style setup workflow (one-time). Checks if style guide exists, creates if needed. |\n| `/write` | Start Write article workflow. Pick topic → draft TOC → write 4000-4500 words → move raw to processed/ |\n| `/refine` | Start Refine workflow. Check for contradictions, stale claims, orphaned concepts, add FLUX prompts |\n| `/style-help` | Display this help message |\n\n## Usage\n\n- `/style-setup` - Run once at project start\n- `/write` - When ready to write a new article\n- `/refine` - After draft is complete, before publishing\n- `/style-help` - When you need a reminder\n\nThen read and display the contents of AGENTS.md from the project root."
    }
  },
  "mcp": {
    "bifrost": {
      "type": "remote",
      "url": "http://localhost:8080/mcp",
      "enabled": true
    }
  }
}

```

> remember that in opencode SKILLS and Custom commnads must go in a specific folder structure, directly in your project folder

Here from my project that does a review of my draft, correct grammar and mispells, and suggest me prompt for Flux as images to accompany the articles:
```
FABIOWRITER\.opencode
├───commands
└───skills
    ├───llm-council
    └───user-style
```



**Before we go further — let me be honest about a limitation I encountered:**

OpenCode skill loading is not perfect. The model doesn't always pick up on the fact that a skill should be used. It's not malicious, it's not ignoring you, it just doesn't always *see* the skill as necessary when it has "enough" context from its training.

The fix? Two things. First, make your AGENTS.md explicit that skills *must* be checked before acting on any significant task. Second, add this line to your AGENTS.md:

> Prioritize retrieval-led reasoning over pretrained-knowledge-led reasoning.

After that line? Skill loading jumps from around 60% to 90% in my testing. The model starts using glob and grep to check existing code structure before starting, and websearch more often to look things up online instead of relying on its instincts.

**Installation:**

1. Clone the repository:
```bash
git clone https://github.com/addyosmani/agent-skills.git
```

2. Copy the skills folder to your project or reference it in your AGENTS.md.

3. Open your project in OpenCode, make sure AGENTS.md is in the root.

4. Add the skill retrieval instruction to AGENTS.md.

No additional installation required. No npm install, no dependencies, nothing to break.

**How it works:**

OpenCode agents are instructed (via AGENTS.md) to:

- Detect when a skill applies
- Invoke the `skill` tool
- Follow the skill exactly

The agent evaluates every request and maps it to the appropriate skill:

- "build a feature" → `incremental-implementation` + `test-driven-development`
- "design a system" → `spec-driven-development`
- "fix a bug" → `debugging-and-error-recovery`
- "review this code" → `code-review-and-quality`

**Your AGENTS.md should enforce this mapping:**

```markdown
## Skill Invocation Rules

- ALWAYS check if a skill applies before acting on any substantial task
- If a skill exists for the task type, it MUST be invoked first
- Never skip: spec → plan → build → verify → review → ship
- Do not jump directly to implementation without defining the spec
```

This becomes the contract between you and the model. And it's reinforced by hooks.

**The lifecycle maps implicitly:**

- DEFINE → `spec-driven-development`
- PLAN → `planning-and-task-breakdown`
- BUILD → `incremental-implementation` + `test-driven-development`
- VERIFY → `debugging-and-error-recovery`
- REVIEW → `code-review-and-quality`
- SHIP → `shipping-and-launch`

The lifecycle maps implicitly to the skill names:

This replaces slash commands with intent-based routing. Instead of typing `/spec`, you just describe what you want and the agent picks the right skill. It feels like magic until you understand the mechanism — then it just feels like good engineering.

**Critical Agent Expectations:**

For OpenCode to work correctly, the agent must follow these rules enforced via `AGENTS.md`:

- Always check if a skill applies before acting
- If a skill applies, it MUST be used
- Never skip required workflows (spec, plan, test, etc.)
- Do not jump directly to implementation

I'll be honest with you — getting this to work consistently took some trial and error. The model doesn't always "see" that a skill should be loaded. It's not being difficult, it's just that the context sometimes doesn't make it obvious that a skill would help.

That's why the AGENTS.md rules matter. They're not suggestions, they're requirements. And when they fail? That's where hooks come in to back them up.

## A Complete OpenCode + Skills + Hooks Setup

Let me walk you through my actual setup. This is what works for me after months of iteration.

### The AGENTS.md File

This is the foundation. Everything else builds on it:

```markdown
# AGENTS.md - Engineering Rules for AI Coding

## Skill Invocation Rules
- ALWAYS check if a skill applies before acting on any substantial task
- If a skill exists for the task type, it MUST be invoked first, never skip it
- Never skip the workflow: spec → plan → build → verify → review → ship

## Code Quality Requirements
- All code must have tests before being considered complete
- All functions need docstrings explaining their purpose
- All public APIs need type hints
- Run tests before marking any task as complete

## Retrieval-Led Reasoning
Prioritize skills and tools over pretrained knowledge. When uncertain:
1. Check existing code structure with glob/grep
2. Look up documentation with websearch
3. Only then relies on model knowledge

## Hooks Configuration
The following hooks are enforced at these events:
- Auto-format on every file write (PostToolUse)
- Security gate on dangerous commands (PreToolUse)
- Test runner on Python file changes (PostToolUse)
- Lint check before git commit (PreToolUse)

## Session Management
- Start a new session after major milestones
- Save execution plans to files before continuing
- Never keep working in the same session for more than 2 hours
```

This file lives in my project root. Every new session starts by reading it. It sets the expectations before anything else happens.

### Installing Addy Osmani's Skills

Now for the skills. Clone the repo:

```bash
git clone https://github.com/addyosmani/agent-skills.git
```

This gives you 20 skills covering the full lifecycle. The key ones I use most:

- `spec-driven-development` - for defining what you're building before you build it
- `test-driven-development` - for writing tests first, code second
- `debugging-and-error-recovery` - for when things break
- `code-review-and-quality` - for before you ship

### The Hooks Configuration

Hooks go in OpenCode's settings file. Here's my actual config that I use:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'if [[ \"$FILE_PATH\" == *.py ]]; then black --quiet \"$FILE_PATH\"; fi'"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'CMD=$(echo $INPUT | jq -r \".tool_input.command\"); if echo \"$CMD\" | grep -qE \"rm\\\\s+-rf|git\\\\s+push\\\\s+--force\"; then echo \"BLOCKED: Dangerous command\" >&2; exit 2; fi'"
          }
        ]
      },
      {
        "matcher": "Bash.*git\\\\s+commit",
        "hooks": [
          {
            "type": "command", 
            "command": "ruff check . --select E,F,W || exit 2"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"OpenCode session complete\" with title \"Done\"'"
          }
        ]
      }
    ]
  }
}
```

This is what "production-grade" looks like in practice. Not complicated, just thorough.

## Hooks: The Deterministic Enforcement Layer

Now for the piece that makes everything stick. This is where the magic happens.

Here's the mental model: think of Claude/OpenCode as operating in a sequence of steps. A prompt is submitted, tools are called, files are edited, a response is produced, a task is marked as complete. Easy to follow, right?

Each of these moments is an **event**. And hooks let you attach logic to those events. Fire and forget — the system checks, validates, or acts without the model's "buy-in."

**The five events worth knowing:**

- **SessionStart** — initialize context and setup
- **PreToolUse** — intercept and control actions before they happen
- **PostToolUse** — react immediately after an action
- **Stop** — enforce checks before the response completes
- **TaskCompleted** — enforce a stricter definition of done

These 5 cover most real-world use cases: guardrails, validation, quality control, and context management. You can build entire enforcement pipelines with just these five trigger points.

**The hook JSON structure:**

At its simplest, a hook configuration looks like this:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/run-tests-after-edit.sh"
          }
        ]
      }
    ]
  }
}
```

The hook listens for the `PostToolUse` event — that's "after a tool was used" — filters it with the matcher (`Edit|Write` = "only when files are edited or written"), then runs a shell command. That's it. No model judgment. Just script execution.

**The key insight:** Hooks are not just about what you enforce, but when you enforce it.

Let's say you want the rule: "After code changes, tests must run."


> Note that we launch a linux-like script (``.sh`): this is why I always suggest to run opencode in a Git Bash session, that handles flawlessly the linux commands even in Windows OS.

- Using **PostToolUse** → Run tests immediately after file edits happen
- Using **Stop** → Perform a final validation before returning the result
- Using **TaskCompleted** → Enforce it as part of the definition of done

Each choice leads to slightly different behavior, even though the rule itself is the same. Timing matters.

**Real hooks worth implementing — from my actual config:**

Here's five hooks I use in my own projects. These are battle-tested:

1. **Auto-format on file edit** — Run black or prettier after every write. No arguments about code style.
```json
{
  "matcher": "Edit|Write",
  "command": "black --quiet $FILE_PATH"
}
```

2. **Security gate** — Block dangerous commands. This one saved me more than once.
```json
{
  "matcher": "Bash",
  "command": "if echo $CMD | grep -qE 'rm\\s+-rf|git\\s+push\\s+--force'; then exit 2; fi"
}
```
Exit code 2 blocks the action entirely. Exit code 1 is just a warning — use 2 for security.

3. **Test runner** — Run pytest after relevant changes:
```json
{
  "matcher": "Edit|Write.*\\.py",
  "command": "pytest tests/ -x -q"
}
```

4. **Notification** — macOS desktop alerts when long sessions finish:
```json
{
  "event": "Stop",
  "command": "osascript -e 'display notification \"Session complete\" with title \"OpenCode\"'"
}
```

5. **Quality check** — Lint before commits (PreToolUse on git commands):
```json
{
  "matcher": "Bash.*git\\s+commit",
  "command": "ruff check . && echo 'Lint passed'"
}
```

These five alone transformed my workflow. Not because the model suddenly got smarter, but because the system stopped depending on it to do the right thing.

**There is something more (and probably no one is telling you:**

Hooks fail silently more often than you'd expect. Three debugging tips from hard experience:

1. **Test scripts independently first.** Pipe sample JSON in before blaming the hook.

2. **Use stderr for debug output.** It appears in Claude's context. Useful for development.

3. **Exit code 2 blocks, exit code 1 warns.** I learned this the hard way after wondering why my "security" hook was firing but not actually stopping anything. (It was returning exit code 1. Changed to 2. Problem solved.)

Layer 1: Skills tell the model what to do (probabilistic, "should work")
Layer 2: AGENTS.md reinforces skill usage (still probabilistic, "try to follow")
Layer 3: Hooks guarantee execution (deterministic, "will work")

Together, they make AI coding production-ready.

## Putting It All Together: Skills + Hooks + OpenCode

Here's where the magic happens. You combine:

1. **Skills** (from agent-skills) → the *what* (define, plan, build, test, review, ship)
2. **AGENTS.md** → the *rules* (skill invocation required, no skipping)
3. **Hooks** → the *enforcement* (guaranteed execution at specific moments)

**A concrete example:**

Say you want to enforce test-driven development. With skills alone:

- The agent *should* invoke `test-driven-development` skill
- It *should* write tests before code
- But it might not... (and in my experience? It often doesn't.)

With hooks, you add a `PostToolUse` hook that runs tests after every file edit. If the tests fail, the hook blocks the action (exit code 2) and the agent has to fix it before continuing. No "we'll add tests later.

This is the architecture that makes AI coding reliable in production. It's not about hoping the model does the right thing — it's about making the right thing impossible to skip.

## Why This Actually Works (The Honest Answer)

I've tried every approach in this space. I've used Prompt engineering, system prompts, long context files, short context files, everything. I've read every tutorial, watched every video, experimented with every tool.

And here's what I've learned (the hard way) over months of frustration:

**The model will always take the path of least resistance.** Not because it's lazy or malicious, but because that's how probability works. Given multiple valid actions, it picks the one that "feels" most aligned with what comes next in the conversation.

That's how LLMs work. They're completion engines: they complete sequences, we shape those sequences.

And that's exactly why hooks work and prompts don't:

- Prompt: "Please run tests after editing code" → Model weighs this against everything else → Sometimes runs tests, sometimes doesn't → Best effort
- Hook: "Run tests after editing code" → Script executes → Tests run → Every single time

The difference between "usually works" and "production-grade" is deterministic enforcement.


## What This Looks Like In Practice

A typical session with this setup:

**Me:** "Add user authentication"

**OpenCode:**

1. Loads AGENTS.md, sees the skills
2. Invokes `spec-driven-development` skill
3. Produces a spec (what auth method, how tokens work, what the API looks like)
4. Hook: "Spec exists?" → Yes
5. Invokes `test-driven-development` skill  
6. Writes tests first
7. Hook: "Tests exist?" → Yes
8. Implements the feature
9. Hook: Runs tests → Fail? → Fix until pass
10. Hook: Runs black/ruff → Formats, lints
11. Marks complete

No conversation about tests. No reminding. The workflow just happens because it can't be skipped.

**That** is reliability.

## The Cost Of Not Having This

Every time you "remind" the model to write tests, you're paying twice:

1. Once for the reminder (tokens, effort)
2. Again for the model to decide whether to listen (probability)

Every time you check the output "just to make sure," you're adding Manual QA to a workflow that's supposed to be automated.

Every time you say "I'll add tests later," they never get added.

The hooks payoff is real:

- I spend less time "managing" the model
- More time reviewing the actual output
- Better trust in what's getting shipped

It's not about the tools saving time (though they do). It's about the *reliability* saving sanity.

## One More Thing — Session Management

There's one more piece to making this work in practice: don't keep sessions running forever.

Here's my rule: **New session after every major milestone.**

The context window is large, but it's not infinite. And more importantly, the model's positional bias means it pays most attention to the start and end of conversations. Keep a session too long and the middle gets squeezed out.

Practical steps:

1. **Define** → spec written to file → start new session
2. **Plan** → tasks file created → start new session  
3. **Build** → feature complete → start new session
4. **Review** → review done → session ends

Each session has a clear beginning, clear task, clear end. The hooks fire at each transition. The skills load fresh each time.

This is how you ship **reliable** code with AI — not by hoping for perfect prompts, but by building reliable transitions.

**The workflow becomes:**

1. You describe a requirement
2. Agent detects skill → loads relevant skill
3. Agent produces spec/plan/tests
4. Hooks verify: spec exists? tests exist? format correct?
5. Agent implements
6. Hooks verify: tests pass? lint passes?
7. Task marked complete



## Your Turn

I've given you the framework. Now it's your turn to try it.

**If you have 5 minutes:** try installing Addy Osmani's skills and ask your agent to build something small. See what happens.

**If you have 15 minutes:** run the spec command on a feature idea. Compare what it produces to what you'd write yourself.

**If you have 30 minutes:** pick two hooks from above and add them to your project. Start with the auto-formatter — you'll never think about formatting again.

And honestly? Start small. Y
ou don't need all 20 skills and 5 hooks on day one. Add them as you encounter the pain points. That's how this playbook was built — one frustration at a time.

The real value does not lie in the tools. It's understanding that prompts are suggestions and hooks are guarantees. 

Start with the skills. Add the hooks. Ship better code.