# From Toy AI to Production: the MCP Problem No One Talks About and how to save 90% on Costs"

**==> picture [800x400] intentionally omitted <==**

## The Moment Everything Fell Apart

I need to confess something.

Three months ago, I sat staring at my Claude usage bill and I swear I felt my soul leave my body. I hit the token limits every single day, for one month. And it was only me!
I cannot even imagine if I had to work on a team project in my Company...

That's when I knew — something had gone terribly wrong with how I'd set up my MCP infrastructure.

And there is also an embarrassing part: I tried to connect only eight MCP servers. It was a test, an experiment, my way to understand what MCP are and if they are really usefule. But eight: that's supposed to be simple, right? That's supposed to be the easy version?

So I did my studies. One step back, some goolge search on good sources, and I got a glimpse of my naive understanding of the whole thing. I want to remove this struggle for you. The naked truth behind what was happening is in reality quite simple: every single prompt, every single request, was carrying 150 tool definitions in context. Every. Single. One. We'reTalking About 150 definitions getting injected before my model even saw what I actually wanted to ask.

This is the MCP problem no one talks about. The one hiding in plain sight.

And today, I'm going to tell you exactly how I fixed it — and how you can save yourself the same nightmare.

Let's go.

## But Wait — What Even Is MCP?

I know. I'm already diving into the enterprise stuff and some of you might be thinking "okay, slow down — what even is this thing?"

Fair point. Let me back up.

**MCP** stands for **Model Context Protocol**. It's the open standard that Anthropic released in late 2024 that lets AI models talk to external tools, databases, and services. To borrow the questionable (but super used everywhere anlogy) MCP simplify and server as a standard, the same way USB-C lets your laptop talk to anything with a port.

Think about that comparison for a second. Before USB-C, you needed a different cable for your phone, a different one for your camera, a different one for your printer. It was a mess that, frankly, we just accepted.

MCP does the same thing for AI. Before MCP, if you wanted your AI to access GitHub, you needed custom code for that integration. Want it to access Slack? New custom integration. Want it to talk to your database? You guessed it — more custom code.

This is what people call the **N×M problem**. If you have 5 AI applications and 10 data sources, you need 50 custom integrations. Each one needs maintenance, security updates, documentation. It doesn't scale. Add one new AI tool and you need 10 more integrations.

With MCP, you build one integration per tool, and *any* MCP-compatible AI can use it. You connect your database once, and now Claude, or Cursor or even Opencode can access it. Cursor can access it. Your custom agent can access it. Any of them.

That's the basic idea. Simple right? And honestly it can be a real revolution once you understand it.

## The Three Building Blocks

Now that I've convinced you MCP matters, let me tell you what it actually *does*. Because this part matters for understanding how your AI talks to tools.

MCP servers expose three types of capabilities — called **primitives**:

**1. Tools** — These are executable functions with side effects. When an AI calls a tool, something changes in the external system. Creating tickets, sending emails, updating databases, running deployments — all tools.

A tool might be:
- Creating tickets in Jira or Linear
- Sending messages to Slack
- Updating database records
- Running tests or deployments
- send emails or create calendar items

Tools require careful security consideration since they can modify real systems. You don't want your AI accidentally deleting your entire database or send spam emails because of a misunderstood prompt.

**2. Resources** — These represent data that AI agents can read. Files, database records, API responses, configuration files, anything structured. Resources are passive — the AI retrieves them but doesn't modify the underlying data.

A resource might be:
- Documentation pages from your knowledge base
- Customer records from your CRM
- Configuration files from your codebase
- Metrics from your analytics dashboard

**3. Prompts** — These are reusable templates for AI interactions. They help standardize how users or systems interact with AI agents for specific tasks. If we port this to the Agents harness world (Claude Code, Cursor, Opencode et alii) they are skills: "canned workflows" that wrap up multiple tools and resources into a single invocation.

For example, a "generate test cases" prompt might always include certain instructions and context about your testing standards, making the AI's output more consistent.

These three primitives — Tools, Resources, and Prompts — are how MCP servers expose their capabilities. Every MCP server you connect will expose some combination of these three things.

## The Architecture No One Explains Properly

Here's where most tutorials lose people. Let me try to do what they couldn't.

MCP has three main components:

**1. The MCP Host** — This is your AI application. Claude Desktop. Cursor. Your custom tool. It's where you're actually working.

**2. The MCP Client** — This is the connector inside the host that maintains the actual connection to your servers. It translates what your AI wants into what the server understands.

**3. The MCP Server** — This is the external service exposing capabilities. Could be a GitHub server, a database server, a file system server, whatever.

The communication happens through something called JSON-RPC 2.0 messages —Structured, predictable format for requests and responses. The protocol supports both:

- **Local connections (stdio)** — For processes running on the same machine. Fast, synchronous.
- **Remote connections (HTTP with SSE)** — For servers running elsewhere. Enables real-time data streaming.

This matters because it determines where your servers live and how fast they respond. But we're getting ahead of ourselves.

Because Here's The Thing Nobody Warned Me About

When you connect your first MCP server, everything feels great. Single server, 10 tools, smooth as butter. Your model can call GitHub. Life is good.

Then you connect another server. And another. And another.

And here's where it falls apart: **every single MCP tool from every connected server gets injected into the model's context on every single request.**

I don't think people realize this. I certainly didn't.

So let's do the math:
- Server 1: 10 tools × your prompts = 10 tool definitions every request
- Server 2: 15 tools
- Server 3: 20 tools
- ...
- Server 8: 30+ tools

You're now sending 150+ tool definitions before your model even sees your actual question.

At that scale, token cost is not anymore a rounding error: it's the majority of your spend. Your actual prompt becomes the minority of the context.

And the usual advice people give is to "trim your tool list." Honestly? That's not a solution. 
That's a tradeoff. 
You're giving up capability to control cost. You're choosing between having what you need and being able to afford to need it.

That's not a choice anyone should have to make.

This is exactly where Bifrost came into my story.

## The Bifrost Moment

Bifrost started as an LLM gateway — a unified layer to manage AI providers, keys, routing, and costs. We talked about it several time here and here. 
Teams ranging from Fortune 100s across pharma, healthcare, and finance to global top hedge funds adopted it as the foundational layer for their AI infrastructure.

As those teams moved from single-model calls to full agent workflows, they started wiring MCP servers through it. Then ten more.

The gateway handled it. But as MCP adoption scaled, two problems kept surfacing (and also I lived both of them, even if I am nothing but a hobbist):

**Problem #1: No control.** Which tools is this agent allowed to call? Who's calling what? Can a customer-facing workflow reach the same internal APIs as your admin tooling?

**Problem #2: Exploding cost.** Token usage grew in ways that weren't obvious until the bill showed up.

Bifrost built what they call **MCP Gateway** to solve both. This is where my story changed.

## The Gateway That Actually Works

Let me walk you through what Bifrost MCP Gateway does and why it matter to me.

### Virtual Keys: Scoped Access for Every Consumer

When a new engineer joins your team, you shouldn't hand them unrestricted access to every system your company runs. You scope their access, audit what they do, track what it costs.

MCP Gateway does the same thing — with **virtual keys**.

You issue scoped credentials to every consumer of your gateway: a user, a team, a customer integration. Each key carries a specific set of tools it's allowed to call.

The scoping works at the tool level, not just the server level. You can allow a key to call `filesystem_read` but not `filesystem_write` from the same server. If your key is provisioned for a customer-facing agent, it simply *cannot* reach your internal admin tooling.

This alone would have saved me. I am not yet even talking about a team of developers, and ven myself, I had been  accidentally hitting production APIs from test environments. 
Imagine a customer-facing workflows reaching internal tools. It would be governance nightmare.

Not anymore.

### MCP Tool Groups: Governing Tools at Org Scale

Virtual keys handle the one-credential-one-scope case. But at scale, you're managing access across teams, customers, users, and providers — not individual keys.

This is what **MCP Tool Groups** are for.

A tool group is a named collection of tools from one or more MCP servers. You define which tools it includes and attach it to any combination of virtual keys, teams, customers, or users.

Bifrost resolves the right set at request time with no database queries. Everything's indexed in memory and synced across cluster nodes automatically.

If a request matches multiple groups, Bifrost merges and deduplicates the allowed tools. The model *only ever sees what it's supposed to see*.

### Audit Logging for Every Single Tool Call

Every tool execution is a first-class log entry. For each call you get:

- The tool name
- The server it came from
- Arguments passed in
- Result returned
- Latency
- The virtual key that triggered it
- The parent LLM request that initiated the agent loop

This is what production looks like. You can pull up any agent run and trace exactly which tools it called, in what order, and what came back. Or filter by virtual key to audit what a specific team or customer has been running.

Content logging can be disabled per environment if needed. But you still capture tool name, server, latency, and status without logging arguments or results.

### Per-Tool Cost Tracking

Let's focus on a team scenarion. There is something that most teams don't realize: MCP costs aren't just token costs.

If your tools call paid external APIs, search services, enrichment endpoints, or code execution environments — each invocation has a price.

Bifrost tracks cost at the tool level using a pricing config you define per MCP client.

These show up in logs alongside LLM token costs, giving you a complete picture of what each agent run actually costs — not just the model portion.

But all of this? It was only half my problem.

## The Security Side Nobody Talks About

Before I move on, let me address something important: MCP introduces real security considerations that you need to think about before connecting random servers to your AI.

I've talked to teams who've discovered several security risks the hard way:

**Tool Poisoning:** Malicious actors can embed hidden instructions in tool descriptions that manipulate AI behavior. The AI might execute unintended actions based on these hidden prompts.

**Prompt Injection:** Attackers craft inputs that cause the AI to bypass security controls or exfiltrate sensitive data. This remains the #1 LLM security risk according to OWASP.

**Token Theft:** Many MCP implementations store API tokens insecurely. Over 53% of open-source MCP servers use static credentials like API keys that rarely rotate.

**Excessive Permissions:** Servers often grant broader access than necessary. An AI might get read-write access to an entire database when it only needs to query specific tables.

The Bifrost gateway helps with these through:

- **OAuth 2.1** — Prefer OAuth over static API keys. OAuth provides better token management, expiration, and scope control.

- **Least Privilege** — Grant only the minimum permissions needed. Start with read-only access and add write capabilities only where required.

- **Input Validation** — Never trust data from AI agents. Validate and sanitize all parameters before executing operations.

- **Monitoring** — Log all AI agent actions. Track which tools get called, what data gets accessed, and any unusual patterns.

- **Human-in-the-Loop** — For sensitive operations, require human approval before executing. The AI can draft the action, but a person confirms it.

This is why virtual keys matter so much. You can scope exactly what each AI agent can access — and nothing more.

## The Real Problem: The Default Execution Model

The default MCP execution model has a cost problem. I lived it.

Let's say you connect 5 servers with 30 tools each. You're sending **150 tool definitions** before the model even sees your prompt.

At that scale, token cost is the majority of your spend.

The usual advice is to "trim your tool list" — which I've already told you isn't a solution. It's giving up capability to control cost.

So Bifrost built something different. They call it **Code Mode**.

## The Paradigm Shift: Code Mode

The idea of having agents write code to interact with MCP tools rather than calling them directly isn't new. Cloudflare explored it with a TypeScript runtime. Anthropic's engineering team wrote about it showing context dropping from 150,000 tokens to 2,000 for a Google Drive to Salesforce workflow.

Bifrost found the approach compelling enough to build it natively — with two differences:

1. They chose Python over JavaScript because LLMs are inherently trained on more Python data than JavaScript.

2. They added a dedicated documentation tool to the meta-tool set to further reduce the context.

Instead of dumping every tool definition into context, Code Mode exposes your MCP servers as a virtual filesystem of lightweight Python stub files.

The model reads only what it needs, writes a short script to orchestrate the tools, and Bifrost executes it in a sandboxed Starlark interpreter.

### The Four Meta-Tools

Code Mode provides four meta-tools to the AI:

| Meta-tool | What it does |
|----------|-------------|
| `listToolFiles` | Discover which servers and tools are available |
| `readToolFile` | Load the Python function signatures for a specific server or tool |
| `getToolDocs` | Fetch detailed documentation for a specific tool before using it |
| `executeToolCode` | Run the orchestration script against live tool bindings |

Instead of loading 150 tool definitions, the model loads a stub file, writes a few lines of code, and runs it. The context stays small regardless of how many MCP servers you have connected.

### What This Looks Like in Practice

Take a multi-step workflow: look up a customer, check their order history, apply a discount, send a confirmation.

**Classic MCP** — full tool list in context on every single turn:

Each turn carries the full tool list. The tokens stack up fast. Every intermediate result flows back through the model.

**Code Mode** — model reads what it needs, writes once, executes once:

The model submits something like this:

```python
customer = crm.lookup_customer(email="john@example.com")
orders = crm.get_order_history(customer_id=customer["id"], limit=5)
discount = billing.calculate_discount(customer_tier=customer["tier"], order_count=len(orders))
billing.apply_discount(customer_id=customer["id"], discount_pct=discount["pct"], order_count=len(orders))
email.send_confirmation(to=customer["email"], discount_pct=discount["pct"])
```

Bifrost executes this in the Starlark sandbox, calling each tool in sequence. The model never sees the intermediate results — it only gets the final output. The full tool list never touches the context.

Same task. **90% reduction in cost. 40% faster.**

### The Real Impact — My extimated Numbers

Bifrost ran benchmarks with Code Mode on and off, scaling tool count to measure how savings change as MCP footprint grows.

| Round | Tools | Servers | Code Mode OFF | Code Mode ON | Change |
|-------|------|--------|--------------|--------------|--------|
| 1 | 96 | 6 | $104.04 | $46.06 | −55.7% |
| 2 | 251 | 11 | $180.07 | $29.80 | −83.4% |
| 3 | 508 | 16 | $377.00 | $29.00 | −92.2% |

The savings aren't linear — they compound as you add MCP servers. With around 500 tools attached, you save more than 90% of your tokens.

Classic MCP loads every tool definition on every request, so connecting more servers makes the problem worse. Code Mode's cost is bounded by what the model *actually reads*, not by how many tools exist.

The benchmarks also confirm that accuracy isn't traded away. Pass rate held at 100% in both modes.

**But what does "pass rate" actually mean here?**

In these benchmarks, "pass rate" means the percentage of test queries that were completed successfully without errors. Both Classic MCP and Code Mode achieved essentially perfect completion rates — meaning Code Mode doesn't sacrifice reliability for cost savings.

The benchmarks also showed:
- **Input tokens dropped 58-93%** depending on tool count
- **LLM turns reduced 3-4x** — Fewer back-and-forth exchanges
- **Latency improved 40%** — Fewer turns means faster completion

This is the part that sold me. I could either:

- Keep Classic MCP and accept that every tool definition loads on every request, paying exponentially more as we scale
- Enable Code Mode and cut costs by 90%+ while keeping the same capabilities

No brainer.

## Real-World Use Cases

Let me give you a few examples of where MCP Gateway and Code Mode actually matter in production:

### Use Case 1: E-Commerce Assistant

A multi-step workflow: look up a customer, check their order history, apply a discount, send a confirmation.

**Classic MCP flow:**
- Turn 1: Prompt + search query + [all 150 tool definitions]
- Turn 2: Prompt + search result + [all 150 tool definitions]
- Turn 3: Prompt + customer data + [all 150 tool definitions]
- Turn 4: Prompt + order history + [all 150 tool definitions]
- Turn 5: Prompt + discount calculation + [all 150 tool definitions]
- Turn 6: Prompt + confirmation result + [all 150 tool definitions]

Total: 6 LLM calls. ~600+ tokens in tool definitions alone.

**Code Mode flow:**
- Turn 1: Prompt + 4 tools (listToolFiles, readToolFile, getToolDocs, executeToolCode)
- Turn 2: Prompt + server list + 4 tools
- Turn 3: Prompt + selected definitions + 4 tools + [EXECUTES CODE in sandbox]
        [customer lookup, order history, discount calculation, email send all happen in sandbox]
- Turn 4: Prompt + final result + 4 tools

Total: 3-4 LLM calls. ~50 tokens in tool definitions.

The model writes one Python script. All orchestration happens inside the sandbox. Only the compact result returns to the model.

### Use Case 2: Developer Workflows

Development teams use MCP servers to give AI agents access to:
- GitHub repositories for code search and PR creation
- Jira or Linear for ticket management
- CI/CD systems for build and deployment status
- Documentation sites for technical reference
- Email client
- Calendar tasks
- ticket booking

A developer can ask their AI: "Find all TODO comments in the auth module, create tickets for each, and link them to the relevant code."

With Classic MCP, that's 4+ tool calls, each dragging all tool definitions. With Code Mode, one script executes everything in the sandbox.

### Use Case 3: Financial Analysis

Financial institutions use MCP to connect AI agents to:
- Database servers exposing client portfolios and risk metrics
- CRM servers for client interaction history
- Document servers for searching memos and contracts
- Compliance tools for regulatory checks

An analyst might ask: "Show me clients in the Northeast with over $1M AUM whose risk scores increased 10%+ last quarter, plus their account manager's last note."

The AI coordinates across multiple MCP servers to compile this answer. In Classic MCP, that's dozens of tool definitions on every turn. In Code Mode, one script, one result.

## Setting It Up — My Actual Experience

Here's the honest truth about what it took to get this running:

### Step 1: Add an MCP Client

Navigate to the MCP section in the Bifrost dashboard and add your first MCP server. Give it a name, choose the connection type (HTTP, SSE, or STDIO), and enter the endpoint or command.

For HTTP and SSE servers, you can add any headers the upstream server requires like API keys, auth tokens, or custom metadata directly in the UI.

Once saved, Bifrost connects to the server, discovers its tools, and starts syncing them on the configured interval.

### Step 2: Enable Code Mode

Open the client settings and toggle Code Mode on. That's it. No schema changes, no redeployment.

From that point on, instead of injecting every tool definition into context, Bifrost exposes the four meta-tools, and the model navigates the tool catalog on demand. Token usage drops immediately.

### Step 3: Set Tools to Auto-Execute

By default, tool calls require manual approval. To let the agent loop run autonomously, open the auto-execute settings and add the tools you want to allowlist.

You can allowlist at the tool level: `filesystem_read` can be auto-executed while `filesystem_write` stays behind an approval gate.

In Code Mode, `listToolFiles`, `readToolFile`, and `getToolDocs` are always auto-executable since they're read-only. `executeToolCode` becomes auto-executable only when every tool the generated script calls is on your auto-executable list.

### Step 4: Restrict Access with Virtual Keys

Go to the Virtual Keys section and create a key for who you want to scope: a user, a team, a customer integration.

Under MCP settings, select which tools that key is allowed to call. The scoping is per-tool, not per-server — you can grant `crm_lookup_customer` without granting `crm_delete_customer` from the same server.

Any request with that key will only see the tools it's been granted. The model never receives definitions for tools outside its scope.

### Step 5: Connect Opencode to Bifrost MCP Gateway

Bifrost exposes all connected MCP servers through a single `/mcp` endpoint. To connect Opencode, open your opencode MCP settings and add Bifrost as an MCP server using that URL.

Opencode will discover every tool from every MCP server connected to Bifrost, governed by the virtual key you configure through a single connection. Add new MCP servers to Bifrost and they appear in Claude Code automatically.

### Bonus: Bifrost CLI

If you want to launch coding agents like Opencode, Claude Code, Codex CLI, or Gemini CLI through Bifrost, the CLI handles everything automatically.

It configures keys, base URLs, and model settings so every request routes through Bifrost from the first session. No manual configuration files or environment variables to manage.

The CLI:

- Auto-configures your gateway connection
- Supports tabbed sessions for working with multiple agents simultaneously
- Automatically registers Bifrost's MCP server when launching Opencode
- Stores virtual keys securely in your OS keyring

One command: `npx @maximhq/bifrost-cli`

You're ready to code in under 60 seconds.

## A Honest Ending

I wish I could tell you I figured this out on my own. I didn't.

I wasted three months and hundreds of dollars because I didn't understand what was happening under the hood. I assumed "connecting MCP servers" meant "make them available" — not "inject everything into every single context."

This is happening no tonly to hobbist like me. Most teams are making this same mistake right now. They're wondering why their AI costs are exploding. They're wondering why adding tools makes everything slower. They're wondering why their model seems to "forget" things between turns.

The answer: you're probably not using anything like Code Mode. You're paying for tool definitions to be loaded over and over and over again for every single request.

That's not a model problem. That's an infrastructure problem.

Bifrost MCP Gateway — or something like it — is the layer that handles both. It gives you:

- **Scoped access** via virtual keys
- **Tool governance** with MCP Tool Groups
- **Full audit trails** for every tool call
- **Per-tool cost visibility** alongside LLM usage
- **Code Mode** to cut context cost without cutting capability

All behind a single `/mcp` endpoint.

This is where the industry is heading. Agents aren't just calling models anymore. They're orchestrating systems. And that needs infrastructure.

When your LLM call and your tool calls flow through the same gateway, you get a complete picture of every agent run. Model tokens and tool costs together, under a single access control model, in one audit log.

This is what production looks like. This is what I should have had from day one.

## TL;DR — The Bottom Line

If you're running MCP in production:

1. **Default MCP is a cost trap** — Every tool definition loads on every request. At 500+ tools, you're spending more on tools than prompts.

2. **Code Mode is the fix** — Instead of loading everything, the model reads what it needs, writes orchestration code, and executes it in a sandbox. 90%+ token savings demonstrated.

3. **Virtual keys + audit logging = governance** — You wouldn't run production without access control. Your AI agents shouldn't either.

4. **There's a platform for this now** — Bifrost MCP Gateway is purpose-built for production AI systems. The open-source version handles enough for most teams.

The future of AI isn't just smarter models. It's smarter **infrastructure** around those models. MCP is the connector. And you need a gateway to manage it at scale.

Don't wait until your $4,200 bill arrives to figure this out. Trust me — I learned it the hard way (even if my bill was not that big).

**==> picture [600x300] intentionally omitted <==**

---

## Your Turn

Try this:

1. Run `npx @maximhq/bifrost-cli` and see what your current setup looks like
2. Check how many tools you're actually exposing vs. how many you use regularly
3. Calculate token costs in your last 30-day billing cycle

The gap between those numbers is probably your optimization opportunity.

Now go fix it before next month's bill shows up.

---

## FLUX Prompts

### Section: The Architecture No One Explains Properly
> FLUX prompt: A clean technical diagram showing MCP host, client, and server architecture connecting to various external tools like GitHub, Database, and Slack. Clean minimalist style with pastel colors, labeled arrows showing communication flow.

### Section: The Paradigm Shift: Code Mode
> FLUX prompt: Split visualization showing Classic Mode (left) with icon cloud of 150+ tool definitions vs Code Mode (right) with just 4 meta-tools and a code sandbox. Style: infographic with warm orange to cool blue color gradient highlighting the contrast.