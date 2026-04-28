# LLM-wiki local & local LLM: part 2 | by Fabio Matricardi | Artificial INTEL-ligence Playground | Apr, 2026 | Medium

Member-only story

Featured

# LLM-wiki local & local LLM: part 2

## How to implement LLM-Wiki with opencode and llama.cpp, all tricks included

[

![Fabio Matricardi](https://miro.medium.com/v2/resize:fill:64:64/1*p4ShYlP7zymOUeIZ5DSbfg.png)

](/@fabio.matricardi?source=post_page---byline--88ecfa2cf6c2---------------------------------------)

[Fabio Matricardi](/@fabio.matricardi?source=post_page---byline--88ecfa2cf6c2---------------------------------------)

17 min read

·

1 day ago

37

Listen

Share

More

![](https://miro.medium.com/v2/resize:fit:700/1*NRrO9owPLMQCaJVgzaVNLw.png)
my miniPC is now my personal Knowkedge base repository

In [part 1 (see link below)](/artificial-intel-ligence-playground/beyond-catastrophic-forgetting-how-to-build-an-llm-wiki-for-the-long-game-8cea92f3868c) we explored the LLM-Wiki concept and the two main application strategies. In 10 minutes you were able to get it started on your PC using the free models available in opencode.

[

## Beyond catastrophic forgetting: how to build an LLM-Wiki for the long game

### A guide for you to turn scattered PDFs into a compounding Personal Knowledge Base using Python, Agents, and a little…

medium.com

](/artificial-intel-ligence-playground/beyond-catastrophic-forgetting-how-to-build-an-llm-wiki-for-the-long-game-8cea92f3868c?source=post_page-----88ecfa2cf6c2---------------------------------------)

Today we will learn

-   all the **tips and tricks** to run LLM-wiki using llama.cpp
-   how to run llama-server from your PC or another PC in your network
-   how to create Custom commands from opencode. Something like: when you type `//wiki-list` opencode will scan the `/raw` folder for all the available text files not yet ingested, asked you to select one of them and start the knowledge-base process.

Let’s start

## Why go local and the 2 main application strategies

In Part 1, we used **Opencode** with remote models to prove the concept. It’s fast, it’s free, and it gets the job done.

But if you’re serious about building a “Personal Knowledge Base for the long game,” eventually you have to ask yourself: **_Where does my brain actually live?_**

And what happens if my previously free AI is not free anymore?

![](https://miro.medium.com/v2/resize:fit:700/1*mvVWiDOZpWMgRCCZKZCBqw.png)

## The case for “Going Local”

Moving your LLM-Wiki from the cloud to your own hardware it is not only an option for privacy enthusiasts; I strongly believe that is related to **sovereignty and sustainability**.

-   **Data Privacy:** Your business strategies, personal research, and “messy basement” PDFs never leave your machine. There’s no risk of a provider training their next model on your proprietary insights.
-   **Zero Cost:** Once you’ve downloaded a model like **Gemma 4** or **Qwen 3.5**, you are not paying anymore per token. You can run a “Lint” command on a 500-page wiki without checking your credit card balance.

> **👉 Tip**: be ready for long waiting session. Unless you have a computer with a dedicated GPU or a shared NPU like the Intel AI-PC, long context required for the LLM-Wiki will take long time to process it

-   **The “50 First Dates” Insurance:** Remote APIs can change, deprecate, or go down. Running **llama.cpp** locally, you ensure that ten years from now, you still have the “engine” required to read and update your digital library.

![](https://miro.medium.com/v2/resize:fit:700/1*D78hA6lppq190neZX3yOQA.png)

## The 2 Main Application Strategies (Recap)

In the previous article, we defined two distinct ways to interact with your wiki. As we move into the local implementation, you’ll need to decide which “fighter” fits your workflow best:

### 1\. The “Agentic Collaborator” (No-Code/Low-Code)

This is the **conversation-first** approach. You treat the AI like a Chief of Staff. Using tools like Opencode, you point the agent at your `AGENTS.md` (the SOP — _Standard Operating Procedure_) and simply say: _"Process this new research paper."_

-   **Best for:** High-level synthesis, discovering unexpected connections, and users who prefer a collaborative “chat” experience.
-   **Limits**: it is token expensive. If your LLM is powered by an old CPU, you need long time to process the huge context

### 2\. The “Pipeline Engineer” (The Python Way)

This is the **automation-first** approach. Instead of chatting, you use scripts. You run a command, and the Python pipeline handles the “`ingest → summarize → cross-link`” workflow with clinical precision.

-   **Best for:** Bulk processing (e.g., turning 100 PDFs into wiki pages overnight) and those who want a rigid, repeatable format every single time.
-   **The Local Twist:** We will implement a **Python CLI** that handles the heavy lifting — specifically converting those messy PDFs into clean text before handing them off to the LLM.

So, do you want a chatty intern or a silent assembly line?

Running these strategies locally gives you total control over the “schema” of your knowledge.

![](https://miro.medium.com/v2/resize:fit:1000/1*w5MbL1BIEu4H6JMbYxk0PQ.gif)
llm-wiki with custom commands — created by me

> **👉 Tip**: by the end of this article I will show you how to create some custom commands. In the example above you can see that when I type `//wiki-help` I get the list of the custom commands I created myself, improving the previous AGENTS.md

If you are curious I created the following Custom commands:

\- \`//wiki-list\`    - Lists unprocessed source files in raw/ for ingestion  
\- \`//wiki-explore\` - Finds gaps and research opportunities in the   
                     knowledge base  
\- \`//wiki-lint\`    - Runs monthly health checks on the wiki  
\- \`//wiki-help\`    - Lists all available commands (this command)

![](https://miro.medium.com/v2/resize:fit:700/1*Xz2AHJ0lr883EUkYQFNAVw.png)

## What you need for LLM-wiki fully local

I will list all of them out because these are the tools to have. And since I have written already other articles as tutorials for step-by-step installation, I will reference them here

### 1️⃣ opencode

I put installation steps [in this article here](/artificial-intel-ligence-playground/beyond-catastrophic-forgetting-how-to-build-an-llm-wiki-for-the-long-game-8cea92f3868c)

### 2️⃣ llama.cpp binaries

At the time of this write-up, we are at [release b8849](https://github.com/ggml-org/llama.cpp/releases/tag/b8849).

Download the binaries ZIP archive and unzip them in a dedicated folder (I called mine `llama-cpp`)

-   if you are a Windows user you can either download the CPU only version or the Vulkan driver version (this will enable you to use a GPU if you have any, without installing dedicated CUDA/Intel or AMD drivers). I talked about the [Vulkan drivers here](/generative-ai/vulkan-driver-the-missing-bridge-between-software-and-hardware-3c3fde7b1a35) and [here](/artificial-intel-ligence-playground/the-vulkan-advantage-modern-intel-ai-hardware-changes-the-quantization-game-903bfe9c9371).
-   [llama-b8849-bin-win-cpu-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b8849/llama-b8849-bin-win-cpu-x64.zip)
-   [llama-b8849-bin-win-vulkan-x64.zip](https://github.com/ggml-org/llama.cpp/releases/download/b8849/llama-b8849-bin-win-vulkan-x64.zip)

### 3️⃣ a model in GGUF format

The quantized model must be one that supports agents and tool calls. From low resources hardware, up to good consumer GPU, here the models you can use (I tested them all)

CPU only

-   Qwen3.5–2b — GGUF from [unsloth HF repo](https://huggingface.co/unsloth/Qwen3.5-2B-GGUF)
-   Gemma-4-E2B-it — GGUF from [unsloth HF repo](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF)

Low end GPU

-   Gemma-4-E4B-it — GGUF from [unsloth HF repo](https://huggingface.co/unsloth/gemma-4-E4B-it-GGUF)
-   Qwen3.5–4b — GGUF from [unsloth HF repo](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF)
-   Qwen3.5–9B — GGUF from [byteshape HF repo](https://huggingface.co/byteshape/Qwen3.5-9B-GGUF)

Good Consumer GPU/Intel AI-PC

-   Gemma-4–26B-A4B-it — GGUF from [unsloth HF repo](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF)
-   Qwen3–30B-A3B-Instruct-2507 — GGUF from [byteshape HF repo](https://huggingface.co/byteshape/Qwen3-30B-A3B-Instruct-2507-GGUF)

Download your preferred model GGUF in the same directory where you extracted the llama.cpp binaries (I called mine `llama-cpp`)

![](https://miro.medium.com/v2/resize:fit:700/1*sDqF8Qybn2yJnsFlFHra1Q.png)

### 4️⃣ Running the model with llama-server

This is the easy part. `opencode` is shipped with out-of-the-box configuration available for `Ollama`. And since I like llama.cpp the most, **we will fake the Ollama ports with llama-server and get the job done**.

Here the example, using the smallest model in the list: qwen3.5–2b

Open the terminal and run:

.\\llama-server.exe -m .\\Qwen3.5-2B-Q4\_K\_M.gguf -c 64000 -ngl 0 -ctk q4\_0 -ctv q4\_0 --mmap --port 11434 --jinja 

The key parameters here are:

-   `--port 11434` this is the listening port of the API that is used by default by Ollama
-   `-c 64000` means our context window available is set to 64k tokens
-   `-ngl 0` means no GPU layers
-   `-ctk q4_0 -ctv q4_0` tells llama-cpp to quantize the KV-cache. This is crucial becuase the context is huge and it will erode you RAM and compute power
-   `--jinja` explicitly tells llama-cpp to use jinja template engine for chat and for the structured format to be used for tools usage and calls.

> **👉 Tip:** the `--jinja` explicitly is crucial! Do not forget to flag it, otherwise even a Huge model will not be able to work well with Agents tools like Claude-CLI, opencode and all the others!

If you are using another computer in your network to serve the model, change the address like here below to `0.0.0.0` but first check what is the IP address of your PC (I have my miniPC running at [http://192.160.1.70)](http://192.160.1.75\)) running in the terminal `ipconfig`.

![](https://miro.medium.com/v2/resize:fit:1000/1*xEywYKzsXGoi_kFTW5SWIQ.gif)
my miniPC running at http://192.160.1.70

.\\llama-server.exe -m .\\Qwen3.5-2B-Q4\_K\_M.gguf -c 64000 -ngl 0 -ctk q4\_0 -ctv q4\_0 --mmap --port 11434 --host 0.0.0.0 --jinja

-   `--host 0.0.0.0` here the tell to expose the API to the network. in fact you can see that Windows is asking if you **Allow** llama-server.exe to the Network (**say Allow**)

![](https://miro.medium.com/v2/resize:fit:1000/1*fu1yI9De38oZFKw7mkzs3g.png)
AGENTS.md and opencode.json in your folder

### 5️⃣ `opencode.json` configuration in your LLM-wiki folder

Create a file called `opencode.json` that will contain the configuration for _opencode_ only in relation to this project. Since the configuration file is in the local directory, it will have the precedence over the global settings, as [written in the docs](https://opencode.ai/docs/rules/#precedence).

> You can specify custom instruction files in your `opencode.json` or the global `~/.config/opencode/opencode.json`. This allows you and your team to reuse existing rules rather than having to duplicate them to AGENTS.md.
> 
> When opencode starts, it looks for rule files in this order:
> 
> Local files by traversing up from the current directory (`AGENTS.md`, `CLAUDE.md`)
> 
> Global file at `~/.config/opencode/AGENTS.md`
> 
> Claude Code file at `~/.claude/CLAUDE.md` (unless disabled)

Here is what you will get once the `opencode.json` is correctly configured and placed in the project directory.

![](https://miro.medium.com/v2/resize:fit:1000/1*mCM-YqDFxq6B5yU9fNNz0Q.gif)

### Local use or local network use

If it is running on your Laptop directly, create a file called `opencode.json` with this configuration:

{  
  "$schema": "https://opencode.ai/config.json",  
  "provider": {  
    "ollama": {  
      "npm": "@ai-sdk/openai-compatible",  
      "name": "Ollama (local)",  
      "options": {  
        "baseURL": "http://127.0.0.1:11434/v1"  
      },  
      "models": {  
        "qwen3.5-2b": {  
          "name": "qwen3.5-2b"  
        }  
          
// Add more models here as needed  
      }  
    }  
  }  
}

> **👉 Tips**: Remember to adjust the reference name and aliases in the `models` section of the JSON.

If you are running the model from another PC in your network (as explained in the previous section) change the `baseURL` to match the one you got with `ipconfig`.

{  
  "$schema": "https://opencode.ai/config.json",  
  "provider": {  
    "ollama": {  
      "npm": "@ai-sdk/openai-compatible",  
      "name": "Ollama (local)",  
      "options": {  
        "baseURL": "http://192.168.1.70:11434/v1"  
      },  
      "models": {  
        "qwen3.5-2b": {  
          "name": "qwen3.5-2b"  
        }  
          
// Add more models here as needed  
      }  
    }  
  }  
}

Look back at the GIF at the beginning of this section, to see how to make your local LLM active in the opencode session.

Go to `/connect` and go to the Other, up to the bottom and select Ollama.

![](https://miro.medium.com/v2/resize:fit:648/1*URN-ol10Eio6s14a-sb2yw.png)

After you have created a connection to Ollama, you can proceed with the configuration.

![](https://miro.medium.com/v2/resize:fit:772/1*eseuMU0RxTv3wCsHiniBzg.png)

![](https://miro.medium.com/v2/resize:fit:723/1*aIwim04pWGktN-ia19EgVw.png)

-   run `opencode` in the project directory
-   type `/models` to get the list of the models actually available
-   move to qwen3.5–2b Ollama (local)

## LLM-wiki + local LLM with llama-server

We are ready

Now, let’s try to ingest the first document in the LLM-wiki, the same way we did in part 1 using MiniMax.

> process \`2025–09–27 13.40.33 Text to LoRA AI That Fine Tunes Other AI Using Ju.txt\` from raw/. Read it fully, discuss key takeaways with me, then: create a summary page in wiki/, update wiki/index.md, update all relevant concept and entity pages, add backlinks, flag any contradictions, and append to wiki/log.md.

![](https://miro.medium.com/v2/resize:fit:1000/1*KmUwX-TPaW-4AV5iAQxKuw.gif)
session with qwen3.5–2b running on llama-server

To be noted:

-   every session is **token extensive**: first ingestion, before getting to the document can be already 10k
-   **time consuming**: without a GPU the prefilling time gets longer (to understand a large context)
-   sometimes **small models cannot understand perfectly the queries** or get the right file (initially it couldn’t find it)

> **👉 Tip**: most of the agents will try to run `unix/linux` like commands to browse files, search for patterns, read your files. The Windows Terminal and Powershell struggle to parse the commands. GIT bash is fully able to understand them.

I explained how to run Git Bash (and install it) in part 1.

![](https://miro.medium.com/v2/resize:fit:1000/1*Ai4w17otN0mTuYhsEiLZ4g.gif)
how to create Custom Commands and why

## How to add Custom Commands

Finally I will show you how to add Custom Commands, something like: when you type `//wiki-explore` opencode will start the critical loop over the knowledge-base, find gaps and inconsistencies.

In part 1 I explained to you how to use all the prompts for the different layers of the LLM-wiki.

> Adding custom commands can be useful, because you can automate the process: the prompts can be baked into the AGENTS.md definition!

You don’t have anymore to copy/paste the prompts yourself.

Here are the steps (and the small video is above the section title…):

-   Switch back to MiniMax free
-   go in plan mode
-   paste something like this:

> I want to add a \`Custom command\` in the AGENTS.md  
> It is called \`//wiki-explore\`. The critical loop: good answers should be filed back into the wiki.  
> A comparison, an analysis, a connection you discovered.  
> These compound in the knowledge base just like ingested sources do.  
> Every question makes the next answer better.  
> \`//wiki-explore\` will call the following prompt:  
> “””Read wiki/index.md. Based on what’s in the knowledge base, answer: “What should I research next based on what’s here?”. Cite which wiki pages informed your answer. If this reveals new connections worth preserving, create a new page in wiki/ and update the index.
> 
> Questions that extract the most value:  
> → “What are the three biggest gaps in this knowledge base?”  
> → “Which sources disagree with each other, and on what?”  
> → “What should I research next based on what’s here?”  
> → “Write a 500-word briefing on \[topic\] using only wiki content” “””

-   when the model comes to a quite good understanding, switch to Build mode and tell it to implement.

> **👉 Tip:** remember to **Plan** the new `custom command` and switch to **Build** when you are ready. _Do not try to add it in Build mode directly!!!_

Let’s add another Custom Command: this time I will show you how easy is to remove the pain to copy/paste from a boilerplate (or your personal notes) a prompt to the Agents CLI.

Let’s automate the Lint process!

> I want to add another custom command called \`//wiki-lint\`.  
> Why this matters: when the AI writes something slightly wrong and you save it back, the next answer builds on the wrong thing.  
> Two months later, you have five pages reinforcing the same error. Health checks catch this before it snowballs.  
> One check per month. Ten minutes of your time. Non-negotiable if you want the system to stay trustworthy.
> 
> \`//wiki-lint\` will call the following prompt:  
> “””Run a full health check on wiki/ per the lint workflow in CLAUDE.md. Output to wiki/lint-report-\[date\].md with severity levels (🔴 errors, 🟡 warnings, 🔵 info). Suggest 3 articles to fill the biggest knowledge gaps. “””

Similarly as before, the Agent will ask you few questions and finally when you are ready and satisfied, switch to Build and tell the model to proceed with the implementation.

Probably the ingest command will be the most useful. I asked opencode to plan for it with this prompt:

> I want to add a \`Custom command\` in the AGENTS.md  
> It is called \`//wiki-list\` and must lists unprocessed source files in raw/ directory for ingestion.  
> For this an additional file called \`.ingested-files.txt\` must be crated. This file must be updated every time  
> a new file has been processed from the \`/raw\` directory. \`.ingested-files.txt\` contains the list of all the documents already ingested in the LLM-wiki
> 
> This is the expected Behavior:  
> 1\. Scan \`raw/\*.txt\` and \`raw/\*.md\` for source files  
> 2\. Read \`.ingested-files.txt\` to get already-ingested filenames  
> 3\. Return list of unprocessed files with numbers  
> 4\. Ask user which file to process (by number)  
> 5\. If user confirms, execute the ingestion prompt:  
> \`\`\`  
> process \[FILENAME\] from raw/. Read it fully, discuss key takeaways with me, then: create a summary page in wiki/, update wiki/index.md, update all relevant concept and entity pages, add backlinks, flag any contradictions, and append to wiki/log.md.  
> \`\`\`  
> As follow up Tracking: After successful ingestion, append \`\[FILENAME\]\` to \`.ingested-files.txt\`

I believe this is the most useful one. Without it you should have to check your raw folder, cross check with the documents you already ingested, copy/paste from the the previous article the prompt (changing first the filename) and then proceed.

With this tweak, you run the Custom Command and the Agent will display to you ONLY the documents not yet ingested, and it will ask you if you want to start the process.

![](https://miro.medium.com/v2/resize:fit:1000/1*8udfLtNmnvABQqecH_vHIA.gif)

As last command I suggest you to add a //wiki-help. I did it for myself:

> Add another custom command called \`//wiki-help\`  
> this command must list all the available custom commands with a small description like this one (as a reference):
> 
> \- \`//wiki-list\` — List unprocessed sources for ingestion  
> \- \`//wiki-explore\` — Find gaps and research opportunities  
> \- \`//wiki-lint\` — Monthly health checks

## The new AGENTS.md

If you want to peek at my modified AGENTS.md after the session to add the mentioned above Custom Commands, here you have it:

\# Knowledge Base Schema  
  
\## Identity  
This is a personal knowledge base about Artificial Intelligence and Local AI.  
It is maintained by an LLM agent. The human curates sources and asks questions. The LLM does everything else.  
  
\## Architecture  
\- raw/ contains immutable source documents. NEVER modify files in raw/.  
\- wiki/ contains the compiled wiki. The LLM owns this directory entirely.  
\- outputs/ contains generated reports, analyses, and query answers.  
  
\## Wiki Conventions  
\- Every topic gets its own .md file in wiki/  
\- Every wiki file starts with YAML frontmatter:  
  ---  
  title: \[Topic Name\]  
  created: \[Date\]  
  last\_updated: \[Date\]  
  source\_count: \[Number of raw sources that informed this page\]  
  status: \[draft | reviewed | needs\_update\]  
  ---  
\- After frontmatter, a one-paragraph summary  
\- Use \[\[topic-name\]\] for internal links between wiki pages  
\- Every factual claim cites its source: \[Source: filename.md\]  
\- When new info contradicts existing content, flag explicitly:  
  > CONTRADICTION: \[old claim\] vs \[new claim\] from \[source\]  
  
\## Index and Log  
\- wiki/index.md lists every page with a one-line description, by category  
\- wiki/log.md is append-only chronological record  
\- Log entry format: ## \[YYYY-MM-DD\] action | Description  
  (Actions: ingest, query, lint, update)  
  
\## Ingest Workflow  
When processing a new source:  
1\. Read the full source document  
2\. Discuss key takeaways with user  
3\. Create or update a summary page in wiki/  
4\. Update wiki/index.md  
5\. Update ALL relevant entity and concept pages across the wiki  
6\. Add backlinks from existing pages to new content  
7\. Flag any contradictions with existing wiki content  
8\. Append entry to wiki/log.md  
9\. Append filename to .ingested-files.txt  
10\. A single source should touch 10-15 wiki pages  
  
\## Query Workflow  
When answering a question:  
1\. Read wiki/index.md first to find relevant pages  
2\. Read all relevant wiki pages  
3\. Synthesize answer with \[Source: page-name\] citations  
4\. If answer reveals new insights, offer to file it back into wiki/  
5\. Save valuable answers to outputs/  
  
\## Lint Workflow (Monthly)  
Check for:  
\- Contradictions between pages  
\- Stale claims superseded by newer sources  
\- Orphan pages with no inbound links  
\- Concepts mentioned but never explained  
\- Missing cross-references  
\- Claims without source attribution  
Output: wiki/lint-report-\[date\].md with severity levels  
  
\## Focus Areas  
\- Artificial Intelligence   
\- Generative AI on the Edge  
\- How to run your local AI even if you are GPU poor  
  
\## Custom Commands  
  
\### //wiki-list  
Lists unprocessed source files in raw/ directory for ingestion.  
  
\*\*Usage:\*\* \`/wiki-list\`  
  
\*\*Behavior:\*\*  
1\. Scan \`raw/\*.txt\` and \`raw/\*.md\` for source files  
2\. Read \`.ingested-files.txt\` to get already-ingested filenames  
3\. Return list of unprocessed files with numbers  
4\. Ask user which file to process (by number)  
5\. If user confirms, execute the ingestion prompt:  
   \`\`\`  
   process \[FILENAME\] from raw/. Read it fully, discuss key takeaways with me, then: create a summary page in wiki/, update wiki/index.md, update all relevant concept and entity pages, add backlinks, flag any contradictions, and append to wiki/log.md.  
   \`\`\`  
  
\*\*Tracking:\*\* After successful ingestion, append \`\[FILENAME\]\` to \`.ingested-files.txt\`  
  
\### //wiki-explore  
Explores the knowledge base to find gaps, contradictions, and research opportunities.  
  
\*\*Usage:\*\* \`//wiki-explore\`  
  
\*\*Behavior:\*\*  
1\. Read wiki/index.md to understand current knowledge structure  
2\. Analyze the wiki to answer: "What should I research next based on what's here?"  
3\. Cite which wiki pages informed the answer  
4\. If new connections or insights are worth preserving, create a new page in wiki/  
5\. Update wiki/index.md if new pages are created  
  
\*\*Value questions to explore:\*\*  
\- "What are the three biggest gaps in this knowledge base?"  
\- "Which sources disagree with each other, and on what?"  
\- "What should I research next based on what's here?"  
\- "Write a 500-word briefing on \[topic\] using only wiki content"  
  
\### //wiki-lint  
Runs monthly health checks on the wiki to catch errors before they snowball.  
  
\*\*Usage:\*\* \`//wiki-lint\`  
  
\*\*Behavior:\*\*  
1\. Run full health check on wiki/ per the Lint Workflow section in AGENTS.md  
2\. Output to wiki/lint-report-\[date\].md with severity levels:  
   - 🔴 errors: Critical issues (broken links, missing provenance, contradictions)  
   - 🟡 warnings: Structural issues (orphans, missing cross-references)  
   - 🔵 info: Suggestions and recommendations  
3\. Suggest 3 articles to fill the biggest knowledge gaps  
  
\*\*Why it matters:\*\* When AI writes something slightly wrong and you save it back, the next answer builds on the wrong thing. Two months later, you have five pages reinforcing the same error. Health checks catch this before it snowballs.  
\*\*Frequency:\*\* Monthly - non-negotiable to keep the system trustworthy.  
  
\### //wiki-pdf  
Display list of all commands with their descriptions  
  
\*\*Usage:\*\* \`//wiki-help\`  
  
\*\*Behavior:\*\*  
1\. Read AGENTS.md Custom Commands section  
2\. Display list of all commands with their descriptions  
  
\*\*Available commands:\*\*  
\- \`//wiki-list\` - Lists unprocessed source files in raw/ for ingestion  
\- \`//wiki-explore\` - Finds gaps and research opportunities in the knowledge base  
\- \`//wiki-lint\` - Runs monthly health checks on the wiki  
\- \`//wiki-help\` - Lists all available commands (this command)

## Conclusions

Taking your LLM-Wiki local is both a technical flex and t **digital permanence**. Moving away from volatile APIs and into a self-hosted `llama-server` environment, you’ve essentially built a "brain in a box" that doesn't require a subscription to think.

We’ve covered a lot of ground today:

-   **The Power of Local:** Why data sovereignty and zero-token costs are worth the extra “pre-filling” wait times.
-   **The Hardware Reality:** How to squeeze maximum performance out of CPUs and GPUs using quantization tricks like `KV-cache` compression.
-   **Automation via AGENTS.md:** Turning a standard chat interface into a specialized terminal with custom commands like `//wiki-lint` and `//wiki-list`.

Your wiki is no longer just a collection of Markdown files; it’s an active, self-correcting ecosystem that you own entirely.

Did you managed to make it work?

Drop me your feedbacks in the comment section!

Now still have the PDF problem to solve: we can ingest text/markdown files, but nothing related to the worst nightmare of LLM.

> In part 3 (coming soon) I will show you how to use a hybrid approach (not only agent, not fully pipeline): we will use python to create a CLI app to convert messy PDF into clean and organized Markdown and then process them into the LLM-wiki.

And we will create a custom command for it too!

If this story provided value and you wish to show a little support, you could:

1.  Clap a lot of times for this story
2.  Highlight the parts more relevant to be remembered (it will be easier for you to find them later and for me to write better articles)
3.  **Join my** [**totally free weekly Substack newsletter here**](https://thepoorgpuguy.substack.com/about)
4.  Follow me on Medium
5.  Follow my publication [https://medium.com/artificial-intel-ligence-playground](https://medium.com/artificial-intel-ligence-playground)

If you want to read more, here are some ideas:

_Part 1 of the series_

[

## Beyond catastrophic forgetting: how to build an LLM-Wiki for the long game

### A guide for you to turn scattered PDFs into a compounding Personal Knowledge Base using Python, Agents, and a little…

medium.com

](/artificial-intel-ligence-playground/beyond-catastrophic-forgetting-how-to-build-an-llm-wiki-for-the-long-game-8cea92f3868c?source=post_page-----88ecfa2cf6c2---------------------------------------)

_Bifrost and Bifrost-CLI_

[

## Bifrost CLI is the AI gateway for coding agents we were waiting for

### The secret weapon for your AI applications in 2026

blog.stackademic.com

](https://blog.stackademic.com/bifrost-cli-is-the-ai-gateway-for-coding-agents-we-were-waiting-for-8543a2ddd57a?source=post_page-----88ecfa2cf6c2---------------------------------------)

_Local llm over your personal network_

[

## Gemma 4 on the Edge: high-performance AI for the “PoorGPUguy”

### The ultimate guide to Local AI: hosting Gemma 4 on your home Network

medium.com

](/artificial-intel-ligence-playground/gemma-4-on-the-edge-high-performance-ai-for-the-poorgpuguy-05a979c71b41?source=post_page-----88ecfa2cf6c2---------------------------------------)

_Cited articles_

[

## Vulkan Driver: the missing Bridge between Software and Hardware

### With Vulkan make the best out of your hardware for AI in not HARD anymore

generativeai.pub

](https://generativeai.pub/vulkan-driver-the-missing-bridge-between-software-and-hardware-3c3fde7b1a35?source=post_page-----88ecfa2cf6c2---------------------------------------)

[

## Is the AI future a Mixture of Experts?

### The release of Open Mixture Of Expert with OLMoE is the new road ahead for Large Language Models, not a Hype. And here…

ai.plainenglish.io

](https://ai.plainenglish.io/is-the-ai-future-a-mixture-of-experts-6da85f1616ce?source=post_page-----88ecfa2cf6c2---------------------------------------)

[

## Stick to the truth my dear AI!

### How to tame your small language model and teach how to say “I don’t know” — part 1

generativeai.pub

](https://generativeai.pub/stick-to-the-truth-my-dear-ai-49f0ff6bbe97?source=post_page-----88ecfa2cf6c2---------------------------------------)

## Embedded Content