## _**Bifrost CLI is the AI gateway for coding agents we were waiting for**_ 

_The secret weapon for your AI applications in 2026_ 

**==> picture [25 x 24] intentionally omitted <==**

_Fabio Matricardi 17 min read · Apr 9, 2026_ 

If you’re like me, you’ve probably spent countless hours looking for free API LLM providers and juggling with OpenRouter keys, NVIDIA NIM credentials, Groq free models and self-hosted llama.cpp or Ollama instances. 

In many small Companies I can see the same pattern: they pay a subscription to Anthropic or Google and then they start chasing the costs. 

It’s exhausting, right? 

Well, what if I told you there’s a tool that can handle all this chaos for you while you sip your coffee and watch your AI apps work like it is intended to be? 

## _**GitHub - maximhq/bifrost: Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive…**_ 

_Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+…_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

In my weekly browsing for cool GitHub project I find the solution, and it is called Bifrost: the AI gateway that’s making 2026 the best year yet for experimenting with large language models, and send them to production. 

In this article we will go through: 

## `TABLE OF CONTENTS` 

- `-----------------` 

`1. What the heck is a Gateway and why you may need one` 

`2. Bifrost is the AI Gateway that just works` 

`3. The witchcraft  of Fallbacks and seamless provider Switching` 

`4. Taking Control of Your Budget and Rate Limits` 

`5. Bifrost vs Bifrost-CLI: The Dynamic Duo` 

`6. How to make them work on your PC` 

- `Pre-requisites (node and Opencode)` 

- `Install Bifrost` 

- `Configure Providers and Models` 

- `install Bifrost-CLI` 

`7. Test Python app to chat with Bifrost` 

`8. Conclusions` 

By the end of this article you will have Bifrost and Bifrost-CLI installed, and start an Opencode session with Zero manual configuration… ready to code. 

## _**What is an AI Gateway and why you may need one?**_ 

Alright, let’s start with the basics. A gateway in the AI world is essentially a traffic cop that sits between your applications and all those fancy LLM providers. 

Instead of each app making direct calls to OpenAI, Google Gemini, 

Anthropic, or your self-hosted instances, they all talk to the gateway first. You tell the Gateway what you want, and it figures out which LLM in the team should work on it. 

In the old days (well, few months ago in reality…), you’d hardcode your API endpoints into your applications. When your primary provider went down or ran out of credits, your app crashed. 

Game over. 

With a gateway, if one provider goes offline, the gateway can automatically switch to another without you having to touch a single line of code. Your AI infrastructure can have a reliable backup plan. 

Imagine you’re building a chatbot for your startup. You want to use OpenAI because it’s reliable, but you don’t want to be completely dependent on them. You also have a self-hosted vLLM instance running locally for testing. Without a gateway, you’d have to write complex logic to handle failovers, rate limits, and key rotations. With Bifrost, the gateway handles all of this for you while you focus on building features instead of infrastructure. 

## _**Bifrost is the AI Gateway that just works**_ 

I tried myself to build a similar project, and many other are doing the same on GitHub: but when a professional team focus all efforts toward that specific goal, something amazing is born (and it will be always better than your own side project). 

Bifrost is that amazing thing. 

It is an open-source AI gateway developed by Maxim. It’s designed to be the single point of entry for all your LLM traffic, routing requests to multiple providers including OpenAI, Anthropic, AWS Bedrock, Google Vertex, Azure, and more. I managed to make it work in 2 minutes with my llama.cpp server, running on the quite old Lenovo X260. 

The coolest part? 

You can keep using your existing OpenAI SDKs and just change the base URL to point to Bifrost instead. 

Looking back at their story we can discover a common pattern: you havce a problem, think of a way to solve it, you make an amazing product… and then you share it with the world. 

This is exactly what happened at Maxim: they were building AI evaluation and observability tools for enterprise teams. Internally, they needed a gateway to route across multiple LLM providers; and every existing option was either too slow at scale or too rigid: and they kept hitting performance walls. 

So, those guys built Bifrost in pure Go, obsessing over performance at every layer. Then, they benchmarked it — 11µs overhead at 5,000 RPS, 40x faster than LiteLLM. 

At that point, they realized this was not anymore an internal tool, it was something every AI team needed. That’s why Maxim open-sourced it. 

On the other hand, Bifrost-CLI is an interactive terminal tool that connects your favorite coding agents — Claude Code, Codex CLI, Gemini CLI, and Opencode — to your Bifrost gateway with zero manual configuration. Instead of setting environment variables, editing config files, and looking up provider paths, you just run `bifrost` and pick your agent, model, and go. 

What it does for you: 

- Automatically configures base URLs, API keys, and model settings for each agent 

- Fetches available models from your Bifrost gateway’s `/v1/models` endpoint 

- Installs missing agents via npm if needed 

- Auto-attaches Bifrost’s MCP server to Claude Code for tool access 

- Launches agents inside a persistent tabbed terminal UI so you can switch sessions without re-running the CLI 

- Shows per-tab activity badges so you can tell when a session is progressing, idle, or has sent an alert 

- Stores your selections securely (virtual keys go to your OS keyring, never plaintext on disk) 

For personal use, Bifrost is perfect for hobbyists and curious minds like me who want to experiment with different models without worrying about breaking their projects. Want to test how Claude performs compared to Gemini or GPT-5.3 on your coding assistant? Just configure Bifrost to route some traffic to Anthropic and Google while keeping most requests on OpenAI. No code changes required! 

For enterprise use, Bifrost becomes even more powerful. Companies can set up virtual keys for different teams, departments, or customers, each with its own rate limits and budget caps. This means marketing can experiment with AI-generated content without draining the engineering team’s budget. It’s like having separate _credit cards_ for different departments: everyone gets what they need without overspending. 

## _**The witchcraft of Fallbacks and seamless provider Switching**_ 

Now let’s talk about the real _magic_ : fallbacks and seamless provider switching. This is where Bifrost shines. When you configure Bifrost (with a clean looking web-interface, running on your computer), you can define a primary provider and multiple fallback options. If your primary provider goes down, hits its rate limit, or runs out of credits, Bifrost automatically routes the request to the next provider in line. 

**==> picture [556 x 220] intentionally omitted <==**

_here the limits I set on the free-tier Providers configured on my Laptop_ 

Here’s how it works in practice: 

1. Your app sends a request to Bifrost’s endpoint 

2. Bifrost checks its routing rules and tries the primary provider 

3. If the primary fails, Bifrost moves to the first fallback 

4. If that fails too, it tries the second fallback, and so on 

The beauty of this system is that your application doesn’t know or care which provider ultimately handles the request. From your app’s perspective, it’s just getting responses from Bifrost. The details of which provider served the request are completely transparent to your code. 

**==> picture [556 x 303] intentionally omitted <==**

_from the dashboard you can monitor all the edetails_ 

This setup is particularly useful for mission-critical applications. Imagine you’re running a customer support chatbot that needs to be available 24/7. With Bifrost, you can configure multiple providers across different regions and cloud providers. If one service goes down, traffic automatically shifts to another without any downtime. 

You can have _multiple escape routes_ in case of an emergency. 

## _**Taking Control of Your Budget and Rate Limits**_ 

One of the biggest headaches when working with LLMs is managing costs. It’s easy to rack up hundreds of dollars in charges without realizing it, 

This is where Bifrost’s budget and rate limit controls come in handy. 

With Bifrost, you can set budgets at multiple levels: 

Per provider: Limit how much you spend on each provider 

Per key: Control spending for specific API keys 

Per virtual key: Set budgets for different teams or projects 

For example, you might configure Bifrost like this: 

Primary provider: OpenAI (high quality, higher cost) 

Fallback 1: Anthropic (good quality, moderate cost) 

Fallback 2: Self-hosted llama.cpp (lower quality, much cheaper) 

You can then set rate limits so that if OpenAI hits its TPM (tokens per minute) limit, requests automatically shift to Anthropic. If you exceed your budget for Anthropic, traffic falls back to your self-hosted instance. This way, you get the best quality while keeping costs under control. 

The best part? None of this requires changing your application code. 

You configure these rules in Bifrost, and your apps continue to work as usual. 

## _**Bifrost vs Bifrost-CLI: The Dynamic Duo**_ 

Now let’s talk about Bifrost and Bifrost-CLI. These two tools work together to make getting started almost zero-config. 

Bifrost is the gateway itself, the service that runs in the background and handles all your routing, fallbacks, and monitoring. Bifrost-CLI is the command-line interface that makes it incredibly easy to set up and manage your gateway. 

Here’s why this combination is so powerful: 

- Bifrost: The brain. It’s what’s actually doing the work. It can run anywhere — on your local machine, in Docker, or in Kubernetes. You point your applications to Bifrost, and it takes care of everything else. 

- Bifrost-CLI: The helper. It’s what you use to configure Bifrost, check its status, and manage your settings. It’s designed to be intuitive and userfriendly, so you don’t need to dive into complex configuration files. 

_Shortly we will pair Bifrost-CLI with Opencode: in 5 minutes you can start your AI assisted coding session._ 

## _**How to make them work on your PC**_ 

And here we go. Let’s setup Bifrost Gateway, fire up Bifrost-CLI and get ready to vibe-code with Opencode. 

## _**Pre-requisites (node and Opencode)**_ 

There are 2 main ways to install Bifrost: one is with a Docker image, the second one is with `npm` . In this article I will show you the steps realted to ® Node.js ( `npm` ): for the docker image you can follow the steps in the official documentation, and get some inspiration from my previous article here. 

`NPM` At its core, (Node Package Manager) is a package manager for JavaScript, and it comes bundled with `Node.js` . Its primary function is to help you manage project dependencies seamlessly. With NPM, you can easily install, update, and remove packages, making it an indispensable tool for Node. js developers. 

Before installing it consider that node.js requires (later) to install as well: 

chocolatey 

python 

Visual Studio Build tools 

If you are used to build projects and do some programming, probably you already have many of those. Consider otherwise to install them by yourself before running the node.js installer: as of today I don’t know what version of Python you are getting, so it may disrupt your existing setup. 

Download the installer from the official page and run it. 

**==> picture [511 x 36] intentionally omitted <==**

## _**Node.js - Download Node.js®**_ 

_Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web…_ 

_nodejs.org_ 

**==> picture [121 x 90] intentionally omitted <==**

## The procedure is quite straight forward… 

**==> picture [276 x 215] intentionally omitted <==**

**==> picture [275 x 214] intentionally omitted <==**

**==> picture [273 x 214] intentionally omitted <==**

**==> picture [275 x 214] intentionally omitted <==**

You can verify if everything is correctly done with one single command. Open a terminal, everywhere and run: 

For Opencode: if you have already installed there is nothing more to do. If you don’t have it, Bifrost-CLI will do it for you! 

## _**Install Bifrost**_ 

After you have installed node.js, open the terminal everywhere and run: 

```
# Install and run locally
npx -y @maximhq/bifrost
```

**==> picture [359 x 103] intentionally omitted <==**

**==> picture [191 x 103] intentionally omitted <==**

The first time the command will download the binaries and run the Gataway 

on `localhost:8080` . 

**==> picture [556 x 276] intentionally omitted <==**

## _**Configure Providers and Models**_ 

This step is mandatory, before even doing anything. 

Bifrost is a Gateway, so we need to give it some destinations. In my case, I have few free API keys with Openrouter and NVIDIA NIM, and I will show you how to setup llama.cpp server faking the Ollama endpoint. 

_Note: for free on OpenRouter you have 50 calls per day, that will become 1000 if you top up 11 credits (around 14 Euros)._ 

**==> picture [556 x 254] intentionally omitted <==**

Go to Model Providers to Add a new Provider. You need the API key (your secret one) and the Model you want to use. 

Let’s try to add Groq (that also provide free API calls to frontier LLM): 

**==> picture [556 x 295] intentionally omitted <==**

- You can check the rate limits here (https://console.groq.com/docs/rate limits). There are also the models with free tier calls listed there. 

Noticed that I also assigned a weight (0.6 is 60%) because it is used in the fallbacks, rules or upon rate limits are reached. 

So we have one remote model (at least): let’s add a local one. 

## _**Llama.cpp faking Ollama**_ 

Here my personal magic. I love llama.cpp, so I wanted to serve the super – new, small and agentic fine-tuned, LFM2.5 350m. I want also to be 

I created a new folder called `BIFROST` , and downloaded there: 

llama.cpp binaries for Windows (llama-b8635-bin-win-cpu-x64.zip) 

– - Download LFM2.5 350M Q8_0.gguf from the official Hugging Face Model card 

Unzip the llama.cpp archive (llama-b8635-bin-win-cpu-x64.zip) in the project directory 

_all the files in the same directory_ 

Now we have already everything. From the terminal, in the project directory run: 

```
.\llama-server.exe -m .\LFM2.5-350M-Q8_0.gguf --temperature 0.1 --top-k 50 --rep
```

**==> picture [556 x 283] intentionally omitted <==**

_local LLM running on my PC_ 

This will expose the API endpoints at the same port of Ollama, for a model we called LFM2.5–350m ( `-a LFM2.5–350m` ). As per the hyperparameters, I used the ones suggested by LiquidAI here. 

Now we can add a new Provider (Ollama) and point to our model. Important things to consider here: 

Ollama is without API keys 

- you need to point the base-url to `http://localhost:11434` the same we set on the terminal 

- When calling the model we will point to `ollama/LFM2.5–350m` 

## _**Is everything running?**_ 

Well, before me move to Bifrost-CLI to run Opencode, we want to make sure that everything is working. Let’s write a quick python app that will send a request to the Bifrost Gateway, calling the different models. 

This app will call the specified model ONLY if you did not yet set Budgets &Limits: in fact, when you have limits, the gateway will handle automatically the routing and fallbacks of the models. 

It is 90 lines, but it can be done in 20. 

I put here the option quite useful: 

you can select what model you want to call 

```
MODELS = [
"mistral/codestral-2405",
"openrouter/qwen/qwen3.6-plus-preview:free",
"ollama/LFM2.5-350m"
]
```

the app anyway always point to the Bifrost Gateway 

```
BASE_URL = "http://localhost:8080/v1/chat/completions"
```

There are 3 main functions: one to select the target model from the given list (remove the ones you don’t have in your configuration); one to get the user 

I called this file `bifrost_test.py` 

`# bifrost_test.py import requests import json # ── Configuration ────────────────────────────── BASE_URL = "http://localhost:8080/v1/chat/completions" MODELS = [ "mistral/codestral-2405", "openrouter/qwen/qwen3.6-plus-preview:free", "ollama/LFM2.5-350m" ] # ─────────────────────────────────────────────── def select_model(): """Display model menu and return selected model ID""" print("\n` 📦 `Available models:") for i, model in enumerate(MODELS, 1): print(f"  {i}. {model}") while True: try: choice = input("\n` 👉 `Select a model (1-3): ").strip() idx = int(choice) - 1 if 0 <= idx < len(MODELS): return MODELS[idx] print("` ❌ `Invalid number. Please enter 1, 2, or 3.") except ValueError: print("` ❌ `Please enter a valid number.") def get_user_prompt(): """Get multi-line or single-line prompt from user""" print("\n` ✍ `Enter your prompt (press Enter twice to send, or type /send to lines = [] while True: line = input() if line.strip() == "/send" or (line == "" and lines): break lines.append(line) return "\n".join(lines).strip()` 

`def stream_response(model: str, prompt: str): """Send request and stream tokens""" payload = { "model": model, "messages": [{"role": "user", "content": prompt}], "stream": True } print(f"\n` 🤖 `Streaming response from `{model}`...\n") try: resp = requests.post( BASE_URL, headers={"Content-Type": "application/json"}, json=payload, stream=True, timeout=60 ) resp.raise_for_status() for line in resp.iter_lines(): if not line: continue decoded = line.decode("utf-8").strip() if not decoded.startswith("data:"): continue data_str = decoded[5:].strip()  # Remove "data:" prefix if data_str == "[DONE]": break try: chunk = json.loads(data_str) token = chunk.get("choices", [{}])[0].get("delta", {}).get("cont if token: print(token, end="", flush=True) except json.JSONDecodeError: continue print("\n\n` ✅ `Stream complete.") except requests.exceptions.ConnectionError: print("\n` ❌ `Error: Could not connect to server. Is it running on", BASE_ except requests.exceptions.Timeout: print("\n` ❌ `Error: Request timed out.") except requests.exceptions.RequestException as e: print(f"\n` ❌ `Request error: {e}")` 

`# ── Main Execution ───────────────────────────── if __name__ == "__main__": print("` 🚀 `Bifrost Chat Client (Streaming)\n")` 

```
    selected_model = select_model()
    user_prompt = get_user_prompt()
```

`if not user_prompt: print("` ⚠ `Empty prompt. Exiting.") else: stream_response(selected_model, user_prompt)` 

Remember that you need the requests library installed. If you don’e have it run from the terminal: 

```
pip install requests
```

To run the app, from the terminal run: 

```
python bifrost_test.py
```

**==> picture [556 x 272] intentionally omitted <==**

Now that everything is working fine… let’s move to OpenRouter and Bifrost- 

CLI 

## _**Install Bifrost-CLI**_ 

Bifrost-CLI is the bridge tool between your coding agent and the Gateway. It is designed to make the connection effortless. 

It works out-of-the-box with: 

**==> picture [556 x 170] intentionally omitted <==**

_if you don’t have any installed, Bifrost will do it for you_ 

## _If a harness isn’t installed, the CLI will offer to install it via npm for you._ 

To install it you need one command, and to add the new program to PATH. 

_the installation_ 

## Installation: as simple as a command 

We know already the node.js instructions: here the one for Bifrost-CLI: 

```
npx -y @maximhq/bifrost-cli
```

_System Property > Environment variables > Path > Add new_ 

You may have noticed that in the terminal you are asked to “To complete installation, add the following directory to PATH: 

Go to System Property > Environment variables > Path > Add new and add the new path (in my case `C:\Users\fabio\bifrost\bin` ). 

Now if you open a new terminal window, everywhere, you can simply run 

```
bifrost
```

Remember that the Gateway must be running (usually in another terminal window (or in the Docker if you used that installation) 

When you run Bifrost-CLI, the interface is text based, similar to Opencode and Claude code. 

The CLI guides you through an interactive setup flow: 

Step 1 — Base URL: Enter your Bifrost gateway URL. If you’re running locally, this is typically `http://localhost:8080` . 

Step 2 — Virtual Key (optional): If your Bifrost gateway has virtual key authentication enabled, enter your virtual key here. Otherwise, press Enter to skip. 

_step 3 and 4_ 

Step 4 — Select a Model: The CLI fetches available models from your Bifrost gateway and presents a searchable list. Type to filter, arrow keys to navigate: 

_You can type any model name manually — even if it’s not in the list. Just type the full model identifier and press Enter._ 

Step 5 — Launch: Review your configuration in the summary screen. Press Enter to launch, or use the shortcut keys to adjust any setting. 

**==> picture [280 x 151] intentionally omitted <==**

**==> picture [269 x 151] intentionally omitted <==**

_And remember: if a harness isn’t installed, the CLI will offer to install it via npm for you._ 

And you are ready to code. 

**==> picture [556 x 276] intentionally omitted <==**

## _**But set your limits**_ 

It is one of the coolest feature of Bifrost. So, start setting your Budgets and Limits. Here my example: 

_the limits I set_ 

## _**Conclusions: Bifrost is the Zero-Config Magic**_ 

So why is Bifrost particularly relevant in 2026? 

The AI models, applications and agents have evolved dramatically. We’re no longer in the early days when everyone used a single provider (and was super expensive). Today, there are dozens of LLM providers, each with its own strengths, pricing, and limitations. This diversity is great for innovation, but it creates complexity for developers. 

Bifrost solves this complexity providing a unified interface to all these providers, with easy visual connections. You can experiment with new providers, test different models, and optimize your costs without being _Open in app_ locked into an sin le vendor. y g 

For individual developers and hobbyists, Bifrost means you can focus on building amazing applications instead of infrastructure. You don’t need to worry about provider outages or credit limits — Bifrost handles that for you. For companies, Bifrost provides enterprise-grade reliability and governance without requiring massive engineering investment. 

The best part? Bifrost is open-source. This means the community can contribute to its development, fix bugs, and add new features. 

It also means you can self-host it anywhere you want, giving you complete control over your data and infrastructure. 

Just like we did few minutes ago. 

_Bifrost Bifrost Cli Ai Gateway Coding Agents Local Gpt_ 

