## _**Beyond catastrophic forgetting: how to build an LLM-Wiki for the long game**_ 

_A guide for you to turn scattered PDFs into a compounding Personal Knowledge Base using Python, Agents, and a little common sense._ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 17 min read · 4 days ago_ 

**==> picture [511 x 286] intentionally omitted <==**

If you’re anything like me (a professional who has spent a few decades navigating the shifts from floppy disks to the cloud, and now to this whirlwind of Generative AI ) you’ve probably had a few specific frustrations lately. 

And one of them is related to knowledge retention: you spend an hour “teaching” an AI (like ChatGPT or Claude) about your business, your specific coding style, or a complex research topic. 

You’re firing on all cylinders and the AI is indeed helpful until… you close the tab. And somehow, regardless of KV-cache, the next morning? It’s gone. 

You’re back to square one, explaining the same acronyms and the same _50 First Dates_ . goals. That looks to me a professional version of the movie 

We’ve been told the solution is something called RAG (Retrieval-Augmented Generation), where we dump our PDFs into a “vector database,” but let’s be honest: half the time, the AI just digs up a random sentence from page 42 (often nothing more than the footer of the original messy PDF…) that has nothing to do with the actual point. 

Then, Andrej Karpathy (the guy who helped build OpenAI and Tesla’s Autopilot) dropped a “Gist” on GitHub. It was not a complex library or a new He called it the LLM Wiki. 70-billion parameter model. It was just an idea. 

I’ve been obsessed with it for the last week, and I want to share how this concept moves us from _AI chatbots_ to building a personal digital knowledgebase. 

By the end of this article I will show you: 

the 2 main ways to implement it 

- step-by-step, how to build it yourself, with zero cents, using Opencode with free available remote models 

the tricks to make it work flawlessly even with a 2B parameter model 

In part #2 we will implement the same coding agent version using only local AI with llama.cpp running on your laptop. I will show you how to configure it manually and with the amazing duo BifrostGateway+BifrostCLI. 

And in part #3 I will guide you in the hardcore implementation style: python code and a main CLI routine. 

Seeing is believing… so here what you will do by the end of this article. 

## _**The Problem: hardwired Amnesia**_ 

Before we get to the solution, let’s look at why our current tools feel so “hollow.” 

In the standard RAG setup, the AI is acting like a researcher for few minutes. You give them access to your documents, and every time you ask a question, they run into the stacks, grab three random documents, read the index, and shout an answer back at you. They don’t take notes or learn your preferences. They just “retrieve.” 

Karpathy realized this is a massive waste of “token throughput.” If we’re paying for these high-powered models to process information, why aren’t they leaving behind a “compiled” version of what they learned? 

## _**The Solution: LLM-Wiki**_ 

- The LLM Wiki is essentially a “living” encyclopedia that your AI builds and maintains for you. Instead of looking at raw documents every time, the AI looks at Wiki Pages it has already written. 

If we want to make an analogy, you can think of it as three distinct layers of your digital office: 

1. The Basement (Raw Sources): This is where you put your messy PDFs, meeting transcripts, and long-winded emails. You never touch these. They are the “Truth,” but they are ugly. 

2. The Library (The Wiki): This is a folder full of neat Markdown files. Each file is a topic: `Project_X.md` , `Client_Y.md` , `Python_Best_Practices.md` . The AI writes these. It cross-links them. It updates them. 

3. The Boss (The Schema): This is a single file where _you_ define the rules. You tell the AI: “When you see a new name, create a bio page. When you find a date, add it to the timeline.” 

## _**Two Paths to building your Wiki (choose your fighter)**_ 

In my research, I’ve found two ways people are actually building this. Depending on whether you like to “tinker” or “talk,” one of these will speak to you. 

## _**Path A: the “Agentic Collaborator” (the No-Code/Low-Code way)**_ 

This is the approach for those of us who have discovered tools like Claude Code or Cursor. 

In this version, you don’t write a single line of Python to manage the wiki. Instead, you have a “conversation” with a coding agent. You point it at your folders and say: _“Hey, look at my ‘Schema’ file. Now, read this new article I just saved and update my Wiki accordingly.”_ 

The Agent acts as your Chief of Staff. It reads the instructions, opens the necessary Markdown files, and types the updates for you. 

- The Good: It’s incredibly flexible. If you decide tomorrow that you want every wiki page to include a “Humor” section, you just tell the Agent. 

- The Bad: It can be a bit… creative. Sometimes it might skip a step or format a link slightly wrong. It’s like having a very talented intern who occasionally gets distracted by a butterfly. 

## _**Path B: the “Pipeline Engineer” (the Python way)**_ 

For those of us who still enjoy the crisp reliability of a script, this is the “CLI” (Command Line Interface) approach. 

Instead of a chatty Agent, you build a Python toolkit. You might have a command like `python wiki.py ingest --file research.pdf` . This script uses a fixed "Prompt Template." It sends the text to the AI, gets a structured response, and uses standard Python code to save it into the right folder. 

- The Good: It’s rock solid. If you have 500 documents to process, you don’t want to “chat” about them. You want a pipeline. It’s faster and cheaper because you aren’t paying for the Agent’s conversational “overhead.” 

- The Bad: It’s rigid. If you want to change the format of your wiki, you’re opening your `.py` files and refactoring code. 

## _**Why this matters for professionals and AI enthusiasts (like us)**_ 

We’ve seen technologies come and go. We remember when “Search” meant `grep` or clicking through Yahoo! categories. We’ve lived through the bloat of Evernote and the complexity of Notion. 

The LLM-Wiki is different because it focuses on Knowledge Accumulation. 

As we get further into our careers, our value cannot be relied just in “knowing facts”: we are the ones who wants to see the connections between those facts. The LLM-Wiki is the first tool I’ve found that actually helps you map those connections automatically. It finds that the client you talked to in 2023 is actually related to the project you’re starting in 2026. It understands how the Attention mechanism is baked in the llama.cpp code and supports the KV-cache quantization. 

Let’s start with the “Agentic Collaborator” way: it is almost a No-Code/LowCode approach, everyone can use even without knowing any programming language. 

_llm-wiki locally running on my crappy Laptop with llama.cpp_ 

## _**Getting Started: a “One Afternoon” challenge**_ 

You don’t need a massive infrastructure to do this. 

1. Create a folder called `Knowledge_Base` . 

2. Inside it, create three more: `raw` , `wiki` , and `outputs` . 

## 3. Create a file called `AGENTS.md` — I will tell you later on what to put in it. 

```
C:\FABIO-AI\Knowledge_Base> tree /f
Folder PATH listing
Volume serial number is005C-8721
C:.
│   AGENTS.md
│
├───outputs
raw
├───
└───wiki
```

Now, you need a software that can understand your AGENTS. I suggest you to use `opencode` . 

Opencode is an open-source agentic framework that lets LLMs interact with your local files. It is easy to install and easy to configure. The easiest way is with Chocolatey: 

_**Chocolatey for Python & AI enthusiasts: how to turn Windows into your in-house developer…**_ 

_How a terminal-first package manager can automate your tools, tame your installs, and make reproducible AI environments…_ 

_ai.gopubby.com_ 

**==> picture [121 x 126] intentionally omitted <==**

After you have Chocolatey installed, open Powershell with Admin rights anywhere, and type: 

My suggestion, if you are on Windows, is to use GIT Bash as a terminal editor and the main reason is… 

👉 _Tip: most of the agents will try to run_ _`unix/linux` like commands to browse files, search for patterns, read your files. The Windows Terminal and Powershell struggle to parse the commands. GIT bash is fully able to understand them._ 

To install Git, following the same method described above, open Powershell with Admin rights anywhere, and type: 

```
choco install git
```

Chocolatey will also automatically add GIT to PATH, so you can call it from everywhere in Windows. 

```
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (orin powershell/cmd.exe just type `refreshenv`).
 The install of git.install was successful.
  Deployed to'C:\Program Files\Git\'
Downloading package from source 'https://community.chocolatey.org/api/v2/'
Progress: Downloading git 2.53.0.3... 100%
```

```
git v2.53.0.3 [Approved]
```

```
git package files install completed. Performing other installation steps.
```

And you are ready. 

## _**Preparations before firing up the AI agents**_ 

Before we start everything, let’s have a look to the AGENTS.md and start filling the /raw folder with few documents. I decided to put some of my articles, and other interesting ones from Medium. 

```
C:.
│   AGENTS.md
│
├───outputs
raw
├───
│       Are you too a Poor GPU guy Here s how to run 400B.txt
│       Beyond RAG How Andrej Karpathy s LLM Wiki Pattern.txt
│       Bifrost CLI is the AI gateway for coding agents we.txt
│       Chocolatey for Python AI enthusiasts how to tur.txt
│       Gemma 4 on the Edge high performance AI for the .txt
│       llama CPP restyle is the workshop for your Local A.txt
│
└───wiki
```

Back to the core file. This `AGENTS.md` file is a sophisticated "System Prompt" or "Standard Operating Procedure" (SOP) for an autonomous LLM agent. It works because it transforms a generic LLM into a disciplined librarian and researcher by establishing a clear hierarchy of data and a rigid set of behavioral constraints. 

LLMs have a limited “context window” (memory). If you asked it to “read everything,” it would forget the beginning by the time it reached the end. 

- The Index-First approach mimics how humans use a library. The LLM reads the index, identifies specific “addresses” (files), and only loads the relevant data into its active memory. This keeps its answers precise and avoids “hallucination by overwhelm.” 

## For the `AGENTS.md` mine looks like this: 

```
# Knowledge Base Schema
```

## `## Identity` 

```
This is a personal knowledge base about **Artificial Intelligence and Local AI**
It is maintained by an LLM agent. The human curates sources and asks questions.
```

## `## Architecture` 

- `raw/ contains immutable source documents. NEVER modify files in raw/.` 

- `wiki/ contains the compiled wiki. The LLM owns this directory entirely.` 

- `outputs/ contains generated reports, analyses, and query answers.` 

## `## Wiki Conventions` 

- `Every topic gets its own .md file in wiki/` 

- `Every wiki file starts with YAML frontmatter:` 

- `---` 

```
  title: [Topic Name]
  created: [Date]
  last_updated: [Date]
  source_count: [Number of raw sources that informed this page]
  status: [draft | reviewed | needs_update]
```

- _`---`_ 

- _`After frontmatter, a one-paragraph summary`_ 

- _`Use [[topic-name]] for internal links between wiki pages`_ 

- _`Every factual claim cites its source: [Source: filename.md]`_ 

- _`When new info contradicts existing content, flag explicitly:`_ 

- _`CONTRADICTION: [old claim] vs [new claim] from [source]`_ 

## _`## Index and Log`_ 

- _`wiki/index.md lists every page with a one-line description, by category`_ 

- _`wiki/log.md is append-only chronological record`_ 

- _`Log entry format: ## [YYYY-MM-DD] action | Description (Actions: ingest, query, lint, update)`_ 

## _`## Ingest Workflow`_ 

```
When processing a new source:
```

_`1. Read the full source document`_ 

_`2. Discuss key takeaways with user`_ 

_`3. Create or update a summary page in wiki/`_ 

_`4. Update wiki/index.md`_ 

_`5. Update ALL relevant entity and concept pages across the wiki`_ 

_`6. Add backlinks from existing pages to new content`_ 

_`7. Flag any contradictions with existing wiki content`_ 

_`8. Append entry to wiki/log.md`_ 

_`9. A single source should touch 10-15 wiki pages`_ 

## _`## Query Workflow`_ 

```
When answering a question:
```

_`1. Read wiki/index.md first to find relevant pages`_ 

_`2. Read all relevant wiki pages`_ 

_`3. Synthesize answer with [Source: page-name] citations`_ 

_`4. If answer reveals new insights, offer to file it back into wiki/`_ 

_`5. Save valuable answers to outputs/`_ 

## _`## Lint Workflow (Monthly)`_ 

```
Check for:
```

- _`Contradictions between pages`_ 

- _`Stale claims superseded by newer sources`_ 

- _`Orphan pages with no inbound links`_ 

- _`Concepts mentioned but never explained`_ 

- _`Missing cross-references`_ 

- _`Claims without source attribution`_ 

```
Output: wiki/lint-report-[date].md with severity levels
```

## _`## Focus Areas`_ 

## _**`**- Artificial Intelligence`**_ 

## _**`- Generative AI on the Edge`**_ 

- _**`How to run your local AI even if you are GPU poor**`**_ 

👉 _Tip: the parts in BOLD text are the ones you may want to change: every wiki is based on ne specific topic (according to Karpathy). Replace mine with your core knowledge topic, and save the file._ 

The document is organized into functional layers that mirror professional software development and data management: 

## _**The “Three-Tier” Architecture**_ 

By separating the filesystem into `raw/` , `wiki/` , and `outputs/` , you prevent data contamination. 

- Immutability: The `raw/` folder serves as the "Source of Truth." The LLM can't hallucinate or change the original text. 

- The Model’s Domain: The `wiki/` folder is the LLM’s "internal memory." Giving it total ownership over this directory empowers it to maintain consistency without asking for permission every time it creates a file. 

## _**YAML Frontmatter & Formatting**_ 

The requirement for YAML and specific link styles ( `[[topic-name]]` ) forces the LLM to output machine-readable metadata. This makes the knowledge base searchable not just for the LLM, but for other tools (like Obsidian or Logseq) you might use to view the data. 

## _**The Feedback Loops (Ingest, Query, Lint)**_ 

These aren’t just instructions; they are algorithms. 

👉 _Tip: The 10–15 Page Rule: This is the most powerful part of the file. It prevents the naive pile-up. Forcing the LLM to update 10–15 related pages per source, you ensure the knowledge base grows as a web rather than a list of disconnected summaries._ 

We will use MiniMax M2.5 free 

Open GIT Bash in your project directory (remember that we called it `Knowledge_Base` ). 

_open with Git Bash here_ 

You can see in the GIF above the main commands to know and keyboard shortcuts: 

   - `TAB` to move from Plan to Build mode 

   - `/` to get the list of built-in commands 

   - `ctrl+p` for the entire list of options 

- 👉 _Tip: we are in GIT Bahs and_ _`CTRL+V` does not work to paste text. You need to use_ _`SHIFT+INS`_ 

_click on the image to get the cheat-sheet for free_ 

## _**Quick Cheat-Sheet**_ 

In my opinion, the following 3 commands are all you need to know: 

- `/init` : Scans your repository and creates an AGENTS.md file to guide the 

- AI on your project’s specific patterns. 

- `/plan` : Ask for a refactoring proposal (e.g., “Plan a refactor for the auth 

- module to use dependency injection”). 

- `/undo` : Immediately revert the last set of refactoring changes if they are 

- incorrect. 

## 👉🎁 You get the cheat-sheet for free from my page here 

_example of the first step_ 

_process [FILENAME] from raw/. Read it fully, discuss key takeaways with me, then: create a summary page in wiki/, update wiki/index.md, update all relevant concept and entity pages, add backlinks, flag any contradictions, and append to wiki/log.md._ 

## In my example I used the following: 

```
process `Bifrost CLI is the AI gateway for coding agents we.txt` from raw/.
Read it fully, discuss key takeaways with me, then: create a summary page
in wiki/, update wiki/index.md, update all relevant concept and entity pages,
add backlinks, flag any contradictions, and append to wiki/log.md.
```

 

 

Note that for one single document, on the first run, we burned already 22k tokens! And this is the next tip: 

👉 _Tip: if you are thinking of running this local, pick a model with an available context length of at least 64k. I suggest the qwen3.5 series and the Gemma4 family with quantized KV-cache._ 

## 2️⃣ _**Start the critical loop**_ 

After you have at least 10 documents, it is time to get to work the LLM in connecting the dots and filling the gaps. This is where the LLM-wiki idea is doing its job! 

What this does: Asks your knowledge base a question and cites which wiki pages informed the answer. New connections get filed back automatically. 

You can start asking few questions on the existing wiki, with this prompt: 

_Read wiki/index.md. Based on what’s in the knowledge base, answer: “What should I research next based on what’s here?”. Cite which wiki pages informed your answer. If this reveals new connections worth preserving, create a new page in wiki/ and update the index._ 

To help you a little more, here few Questions that extract the most value: 

- “What are the three biggest gaps in this knowledge base?” 

- “Which sources disagree with each other, and on what?” 

- “What should I research next based on what’s here?” 

- “Write a 500-word briefing on [topic] using only wiki content” 

- “What connections exist between [concept A] and [concept B]?” 

This is The critical loop: good answers should be filed back into the wiki. 

A comparison, an analysis, a connection you discovered. 

These compound in the knowledge base just like ingested sources do. Every question makes the next answer better. 

## 3️⃣ _**LINT it — Run Monthly Health Checks**_ 

What this does: Runs a health check on your entire wiki. Catches errors before they compound. Suggests new sources to fill knowledge gaps. 

This is the step nobody does. It’s the step that prevents the whole system from slowly rotting. Paste this: 

_Run a full health check on wiki/ per the lint workflow in CLAUDE.md. Output to wiki/lint-report-[date].md with severity levels (_ 🔴 _errors,_ 🟡 _warnings,_ 🔵 _info). Suggest 3 articles to fill the biggest knowledge gaps._ 

When the AI writes something slightly wrong and you save it back, the next answer builds on the wrong thing. 

Two months later, you have five pages reinforcing the same error. Health checks catch this before it snowballs. 

👉 _Tip: One check per month. Ten minutes of your time. Non-negotiable if you want the system to stay trustworthy._ 

Don’t skip it. 

## 4️⃣ _**Explore it**_ 

What this does: Surfaces hidden patterns and unexpected connections across your wiki. The “what am I missing” prompt. 

_Read wiki/index.md and scan all concept pages. Find the 3 most surprising connections between topics that aren’t currently linked. For each connection: explain why it matters, which wiki pages are involved, and whether a new concept page should be created. Also identify 2 topics that appear in multiple sources but don’t have their own dedicated page yet._ 

This is where the system pays for itself. You’ll find angles and patterns that would take weeks of manual reading to spot 

## 5️⃣ _**Brief it**_ 

In the original Karpathy Gist, one of the intuitions is that you can build MARP decks, articles, executive summaries and so on. You can use tools to make the knowledge yours, with the new findings. Quoting it… 

_Obsidian’s graph view is the best way to see the shape of your wiki — what’s connected to what, which pages are hubs, which are orphans._ 

_Marp is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content._ 

_Dataview is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists._ 

_The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free._ 

Here an example of prompt: 

```
Read wiki/index.md. Write a [LENGTH]-word research brief on [TOPIC].
Use only information from the wiki. Structure it as:
```

```
Executive Summary (3 sentences), Key Findings (numbered list),
```

```
Areas of Disagreement Between Sources, Gaps in Current Knowledge,
```

```
and Recommended Next Steps. Cite wiki page names inline.
```

```
If this brief surfaces new connections, create a wiki page for it.
```

Replace [LENGTH] with 300, 500, or 1000 depending on your need. Replace [TOPIC] with whatever you’re working on. The wiki does the research. You just ask. 

Here below my test running it with Qwen3.5–2b and llama.cpp (you will get there too) 

## _**A Final Thought on “Compound Interest”**_ 

When you see the AI create that first cross-linked page — `[[Topic A]]` —you'll feel it. That "click." The realization that you’re no longer just shouting into the void of a chat window. 

You’re building a second brain that actually grows with you. 

And at our age, having a brain that doesn’t forget where it put the keys (or the project specs) is the ultimate superpower. 

We understand financial compound interest. We know that small additions over a long time lead to massive results. Knowledge work is the same. Traditional RAG systems are like a bank account that resets to zero every night. The LLM-Wiki is a high-yield savings account for your thoughts. 

The maintenance cost is nearly zero because the AI does the “grunt work.” Your job is just to curate the sources and ask the big questions. 

So, start compiling. Your 60-year-old self will thank you for the library you’re building today. 

_And give me a feedback how you managed to make it work!_ 

_Opencode Local Gpt Thepoorgpuguy Your Ai Your Rules Llm Wiki_ 

