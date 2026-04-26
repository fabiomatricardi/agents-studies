## _**Gemma 4 on the Edge: highperformance AI for the “PoorGPUguy”**_ 

_The ultimate guide to Local AI: hosting Gemma 4 on your home Network_ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 13 min read · Apr 8, 2026_ 

_119_ 

**==> picture [511 x 279] intentionally omitted <==**

Google released Gemma4 few days ago, and finally I am back in love with these models. 

After Gemma2, I stopped using them: and I moved to Qwen, because it was giving to me enough Context Length for document analysis and Agents capabilities. 

But now, even the small Gemma-4-E2B can do everything. 

I am a PoorGPUguy, so I always bet on Small Language Models with brilliant capabilities. And Gemma4 is my new bet! 

In this article I will show you how to use an old computer as a local AI server: and how to test bigger models with Google AI Studio, for free. 

**==> picture [511 x 320] intentionally omitted <==**

## _**Gemma-4**_ 

’ ­ ­ Gemma 4 is Google s newest open weight model family, focused on stronger reasoning, agentic behavior, and multimodal on­device use. 

## _**Main new capabilities**_ 

- Advanced reasoning and “thinking” mode: Gemma­4 can do step­by­step reasoning, multi­step planning, and is optimized for agentic workflows (e.g., autonomous tool use and workflows). 

- Long context windows: Up to 128K tokens for the small E2B/E4B edge models and 256K tokens for the 26B/31B versions, enabling very long­context tasks. 

- Multimodal inputs: All models support text plus images (with variable aspect ratios and multiple token budgets); E2B/E4B also natively support audio, and some variants handle video­like sequences. 

- Stronger coding and function calling: Improved coding benchmarks plus built­in function­calling support, letting models call tools and APIs within agentic pipelines without extra fine­tuning. 

- Native system­prompt support: The 4­series now has built­in `system` ­role handling, which makes instruction and behavior control more consistent and developer­friendly. This is, in my opinion, the greatest feature (and I was waiting for it). 

- Edge­optimized small models (E2B/E4B): Highly efficient 2B­ and 4B­effective­parameter models designed for phones, Raspberry Pi, and similar hardware, with multimodal reasoning and near­zero­latency offline execution. 

Gemma­4 is a faster­reasoning, long­context, multimodal, agentic­ready family that runs efficiently even on mobile and edge devices. 

The main missing features in the already amazing gemma2–2b-it are: context and system message. 

In modern use of LLM, agentic capabilities and structure outputs go together, and for this you need a system message and a wide context length. 

```
gemma-2-2b-it
```

- Strong chat/instruction­following, optimized for small­footprint deployment (e.g., endpoints, simple chatbots). 

- Pure text­to­text; no native multimodal or advanced “thinking” mode; weaker coding and math than later generations. 

```
gemma-3n-E2B
```

- Mixture­of­Experts­style design: 5B total parameters but behaves like a 2B­footprint model, tuned for on­device efficiency. 

- Text­only, but with better reasoning and instruction­following than Gemma­2­2B, aimed at “on­device” but not yet multimodal or agentic. 

```
gemma-4-E2B
```

- Multimodal: supports text + images (and audio­like or video­like behavior in broader Gemma­4 family) with up to long context (e.g., 32K– 128K­range). 

Designed for advanced reasoning (“thinking mode”), function­calling, 

and agentic workflows on phones/Raspberry Pi–class devices. 

We can easily run the Edge models of the family on our hardware, with llama.cpp. But if you want to try the 26B/31B versions you can opt for the free API or Playground on Google AI studio… for free! 

_Google AI Studio_ 

## _**Google AI Studio free API and playground**_ 

Google offers a rich Integrated Environment to play with the Google Models (text, audio, images and videos) directly on Google AI Studio. 

If you have a gmail address or a Google account, the sign-up session is easy and straight forward. 

But you need to agree to the Gemini API Additional Terms of Service: for some reasons you need to agree that you _“are a developer building with Google AI Studio and Gemini API for professional or business purposes…”_ 

Up to you to decide: I am using it for personal projects where proprietary data is not involved (mainly we-searches, comparisons and exploration of new topics). 

You gain access to the Playground where you can start chatting immediately, change models (in my case I want to test the high tier of Gemma4: the 31B and the MoE). You can also set the depth of the thinking level (Minimal, High) 

You can also generate an API key to use the models from your PC in many applications like Perplexica, LMStudio, Opencode, Open Claude. 

The API key in the free tier allows you to have up to 1500 calls per day! 

The Rate limits are all here 

## _**Rate limits | Gemini API | Google AI for Developers**_ 

_We have updated our Terms of Service. Rate limits regulate the number of requests you can make to the Gemini API within…_ 

_ai.google.dev_ 

**==> picture [121 x 126] intentionally omitted <==**

## - In specific, the Gemma 4 models are basically free 

_screenshot from https://ai.google.dev/gemini-api/docs/pricing#gemma-4_ 

Later on I will show you how to configure your local Perplexica into a powerhouse, using Gemma4-MoE with the free API calls. 

## _**MiniPC as Local AI server**_ 

I have an old Beelink mini-PC, cost me 100$ 4 years ago. It is a low-tier computer, with Intel 6 generation CPU, no dedicated GPU and 16 Gb of RAM. And the CPU has only 4 threads. 

But… this miniPC I am not using anymore, can run at decent speed even Gemma4-E4B quantized. 

_6 tokens/second in generation with my GGUF Runner and Inspector_ 

The idea is simple: 

you can use an old Laptop (an old MacBook with Linux) or an old PC 

connect it to your local network, even in WiFi, 

run the model with llama.cpp server and few tricks 

And get a _remote_ , fully local AI, not slowing down your own working Computer. 

## _**Running Gemma-4-E4B on your old hardware**_ 

It is super easy. 

## _**1) you need the model**_ 

I suggest you to download the GGUF models from the Unsloth repository dedicated to Gemma4 on Hugging Face: 

- - - - 4 E4B it gemma Q3_K_S.gguf related to the 4b active parameters 

- - - - 4 E2B it gemma Q4_K_M.gguf related to the 2b active parameters 

Download in a new project directory: I called mine `GoogleAIstudio` . 

## _**2) you need llama.cpp**_ 

Get the latest binaries of llama.cpp. An old version you may already have is not granted to be working. 

Here below what happen when I tried to run it with version b8429… 

_llama.cpp version b8429_ 

_gemma4 model architecture UNKNOWN_ 

Go for the latest! 

At the time of this article b8705 is the last release. 

## _**Release b8705 · ggml-org/llama.cpp**_ 

_model : support step3-vl-10b (#21287) feat: support step3-vl-10b use fused QKV && mapping tensor in tensor_mapping.py…_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

I am on windows, so I download the binaries for CPU only X64 architecture: 

## - - - - - llama b8705 bin win cpu x64.zip 

Extract the ZIP archive in the same directory (mine is called `GoogleAIstudio` ). 

Open the terminal in the same directory and run: 

- `.\llama-server.exe -m .\gemma-4-E4B-it-Q4_K_S.gguf -c 64000 -ngl 0 -ctk q4_0 -ct` 

-  

## The key parameters here are: 

- `--port 8888` this is the listening port of the API 

- `--host 0.0.0.0` here the tell to expose the API to the network. in fact you 

- can see that Windows is asking if you Allow llama-server.exe to the Network (say Allow) 

## Want to know more about the other flags? 

Running a local LLM server shouldn’t feel like guesswork. The `llama.cpp` server is a powerful, lightweight tool, but its long list of parameters can be overwhelming. 

This downloadable cheat sheet is your essential reference guide to cut through the complexity. I have consolidated the most critical command-line flags into one, color-coded infographic, making it simple to find the perfect configuration for your hardware and use case. 

You need to know your IP address on the old computer 

As I did in the small video above, open a new terminal and run this command: 

```
ipconfig
```

You will get information about all the network adapter on your PC, something like this 

```
Wireless LAN adapter Wi-Fi 2:
```

```
   Connection-specific DNS Suffix  . : nexxt
```

```
   IPv6 Address. . . . . . . . . . . : 2001:b07:6440:da7b:3542:8fe1:62f7:1c9
   Temporary IPv6 Address. . . . . . : 2001:b07:6440:da7b:205b:32ec:4099:deb3
   Temporary IPv6 Address. . . . . . : 2001:b07:6440:da7b:4d8b:a209:4120:d0b5
   Link-local IPv6 Address . . . . . : fe80::eec7:e9e9:80cf:a71d%5
```

```
   IPv4 Address. . . . . . . . . . . : 192.168.1.75
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::5a76:acff:fe04:9220%5
                                       192.168.1.254
```

My miniPC IP address is the one labeled “IPv4 Address”: `192.168.1.75` . This is the address of the llama-server on the network, with API exposed on port 8888… 

 `http://192.168.1.75:8888` 

 

## _**Test the local Network Model — The interactive way**_ 

I created a small CLI app to give you immediately the idea of how good these models are. In alternative, the built-in Web-chat of llama-cpp is already available. 

And you can run it even from another computer on the network (simply put in your browser the `IP:port` in my case `http://192.168.1.75:8888` ) 

For the CLI app we need few libraries, that is a good idea to install globally. 

Open the terminal and run: 

```
pip install openai rich
```

Imports 

We need `rich` to render the Markdown in the terminal, and the `openai` library to handle the API calls for the `chat.completion` . 

```
import sys
import time
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
# Initialize Rich Console
console = Console()
client = OpenAI(
    base_url="http://192.168.1.75:8888/v1",  #adjust with your IP
    api_key="sk-no-key-required"
)
```

Note that the `base_url` must be according to your network setup and the IP address you discovered in the previous step. 

## _**User input function**_ 

I want to allow long text copy/paste in the terminal, so I created a function to allow multi line support. The input is accepted at the end, only after pressing 

```
def get_multiline_input():
    console.print("\n[bold cyan]User[/bold cyan] [dim](Ctrl+D/Z to send, 'exit'
    contents = []
try:
whileTrue:
            line = sys.stdin.readline()
ifnot line:
break
            contents.append(line)
except EOFError:
pass
return"".join(contents).strip()
```

  

## _**Response function**_ 

Because we send the API call with the streaming option, we will start printing the response almost immediately, keeping a small buffer to render the Markdown in the terminal: 

```
def chat():
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use Markdown
    ]
```

```
    console.print(Panel.fit("[bold reverse] Local LLM Chat [/bold reverse]\nConn
# Here the main loop
whileTrue:
        user_text = get_multiline_input()
```

```
if user_text.lower() in ['exit', 'quit']:
            console.print("[yellow]Closing session...[/yellow]")
break
ifnot user_text:
continue
```

```
        messages.append({"role": "user", "content": user_text})
# start timer for the KPI
try:
            start_time = time.time()
            ttft_time = None
            response = client.chat.completions.create(
                model="gemma",
                messages=messages,
                temperature=1.0,
                stream=True
            )
```

```
            console.print("\n[bold magenta]Assistant:[/bold magenta]")
# I use rich.live to render the console
            full_response = ""
with Live(console=console, refresh_per_second=10, vertical_overflow=
for chunk in response:
# Capture Time to First Token
if ttft_time isNone:
                        ttft_time = time.time() - start_time
                    content = chunk.choices[0].delta.content
if content:
                        full_response += content
                        live.update(Markdown(full_response))
            total_time = time.time() - start_time
# Display performance metrics in a small table
            stats_table = Table(show_header=False, box=None, padding=(0, 2))
            stats_table.add_row(
f"[dim]TTFT: {ttft_time:.2f}s[/dim]",
f"[dim]Total: {total_time:.2f}s[/dim]",
f"[dim]Speed: {len(full_response.split()) / total_time:.1f} word
            )
            console.print(stats_table)
            messages.append({"role": "assistant", "content": full_response})
except Exception as e:
            console.print(f"\n[bold red]Error:[/bold red] {e}")
```

```
if __name__ == "__main__":
    chat()
```

My file is called `ATEST_remoteGemma4.py` . To use the python app, from the 

terminal run: 

```
python .\ATEST_remoteGemma4.py
```

And here it is what is going to happen… 

You can find the entire code in my GitHub repo too: 

_**GitHub - fabiomatricardi/Gemma4-E2B-and-llama.cpp: A CLI app and gradio app to chat with Gemma4-E2B…**_ 

_A CLI app and gradio app to chat with Gemma4-E2B GGUF and model served by a miniPC in the LAN …_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**Where to use it — Perplexica and gemma-4–26B-A4B-it-GGUF**_ 

You can call it in a CLI app or easily connect it to LMStudio, or even Opencode (your local AI agents stack). 

But today I will show you how to use it with Perplexica, a local version of the famous Perplexity. 

If you don’t know yet how to install it on your PC , you can read my article about it. 

## _**Your AI your rules: a free fully local Perplexity app on your PC**_ 

_How to use Perplexica with llama.cpp server and forget about any monthly fee_ 

_blog.stackademic.com_ 

**==> picture [121 x 126] intentionally omitted <==**

Now we check only the configuration of the model. 

When your vane/Perplexica is already running (for me in the Docker container), launch the browser and click on the ⚙ Settings icon: 

_settings > Models > Add Connection_ 

Now we want the Gemini connection (that is good also for the GoogleAIstudio API), using the API key we created 5 minutes ago. 

You will see that Perplexica already scanned all the available models: I highlighted the Gemma4 ones. 

## _Remember to check what are the models with a free tier!!_ 

_**Gemini Developer API pricing | Gemini API | Google AI for Developers** Gemini Developer API Pricing ai.google.dev_ 

**==> picture [121 x 126] intentionally omitted <==**

For now, I can see only Gemma4 for free. 

Go back to the home page of Perplexica, switch Model to the one in the new Connection we just configured, and run your query 

## _**Filling the Gaps: Why Gemma 4 is a Game Changer**_ 

Before we wrap up, let’s look at why the jump from Gemma 2 to Gemma 4 matters for the “PoorGPUguy.” 

- The System Prompt revolution: in previous versions, you had to “hack” instructions into the user message. Gemma 4’s native system-role support means the model actually _stays_ in character and follows constraints much better, even at small sizes. 

- Context that breathes: moving from the cramped 8K context of older small models to 128K in the E2B/E4B series changes everything. You can 

now feed an entire technical documentation PDF into a 4-thread mini-PC and get meaningful answers. 

The “Thinking” advantage: the new reasoning mode is for all of them. Even the edge models can now “pause” and plan, which drastically reduces hallucinations during complex tasks like coding or logic puzzles. 

## _**Conclusions**_ 

We often think that to stay on the “bleeding edge” of AI, we need to spend thousands on the latest GPUs or monthly subscriptions. Gemma 4 proves the opposite. 

Combining Google’s efficient open-weights, the lightweight power of llama.cpp, and a bit of “hardware archaeology” with an old mini-PC, you can build a private AI powerhouse for the cost of a few watts of electricity. 

## Here is the bottom line: 

1. Don’t throw away old tech: that 6th-gen Intel NUC or dusty MacBook is a perfect candidate for a dedicated LLM server. 

2. Hybrid is the way: use the Local Edge models (E2B/E4B) for private, fast, everyday tasks, and bridge to the Google AI Studio API for the “heavy lifting” reasoning tasks — all for $0. 

3. Agents are the future: with native function calling and system prompts, Gemma 4 is finally ready to move beyond “chatting” and start _doing_ work inside apps like Perplexica. 

I’m back in love with Gemma because it feels like Google is finally building for the developer who values efficiency over brute force. So, go dust off that old laptop, grab the GGUF files, and start building your own local AI empire. 

What are you going to run on your “new” old server? Let me know in the comments! 

_Thepoorgpuguy Local Gpt Your Ai Your Rules Gemma 4 Python4ai_ 

