## _**Your CPU is NOT Broken: the hidden Truth about GGUF quantization**_ 

_Bits per weight are not tokens per second — Not All Quantizations Are Born Equal part 1_ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 12 min read · Mar 13, 2026_ 

**==> picture [511 x 287] intentionally omitted <==**

Last month, I did what any curious AI enthusiast would do: I downloaded a “tiny” 2-bit quantized model, fired it up on my low-range i5 laptop, and waited for the magic. 

**==> picture [511 x 353] intentionally omitted <==**

By the way… these are the specs of my Lenovo X260 

**==> picture [556 x 188] intentionally omitted <==**

_this is a 2016 laptop_ 

My fan sounded like a jet engine. My cursor blinked. And I blinked back, confused. 

## _“Wait… isn’t a smaller model supposed to run_ faster _?”_ 

If you’ve ever felt this frustration — downloading a “4-bit GGUF” expecting lightning speed, only to watch your CPU chug like it’s running Windows 95 — you’re not alone. And more importantly: 

## _your CPU is NOT broken_ 

The problem is not your hardware. It’s the quantization format you chose. 

In this first part of a three-part series, I’ll walk you through the hidden truth about GGUF quantization: why “bits per weight” doesn’t equal “tokens per second,” and how to pick a format that actually respects your CPU. 

No jargon or kernel debugging. Just practical truths for Windows users (but it is valid also on Linux PC) who want their local AI to _work_ . 

By the way, this is part 1 of the series _“Not All Quantizations Are Born Equal”. You can find the entire Series links here_ 

## 👉 Part 1: Your CPU is NOT Broken _(you are here)_ 

✅ Part 2: Byteshape’s Discovery: Not All Bits Are Created Equal 

✅ Part 3: Pick Your Poison: A Friendly Guide to Quantization Formats 

## ✅ Part 4: Llama.cpp optimization for CPU: not all quantizations are born 

## equal 

- ⏳ Part 5: _The Vulkan Advantage_ 

_- image from https://github.com/ggml org/ggml/blob/master/docs/gguf.md_ 

## _**GGUF 101: the “Universal Adapter”**_ 📦 _**for quantized models**_ 

Let’s start simple. 

Imagine you’re packing for a move. You could: 

- Throw everything loosely into boxes (fast to pack, takes up lots of space) 

- Vacuum-seal each item (takes forever to pack, but fits in a tiny truck) 

Quantization is like that second option. It “compresses” a model’s weights into fewer bits — shrinking file size and RAM usage. But just like vacuum. sealing, there’s a cost: _unpacking takes work_ 

This is GGUF (GPT-Generated Unified Format). Think of it as a universal adapter plug for quantized models. It lets you run the same model file across different tools — llama.cpp, Ollama, LM Studio — without recompiling anything. 

## But… there is a BUT: not all adapters are equally efficient. 

A GGUF file is NOT just “a smaller model.” It’s a model + a specific _packing strategy_ . And some strategies are optimized for GPUs, not CPUs. 

## _**Windows Quick Start (super easy**_ 

If you’re on Windows and want to try this yourself, we need to get the engine running first. We’ll use PowerShell to start the server, which gives you a nice chat interface in your browser. 

1. Download the latest llama.cpp release from GitHub (look for `llamab<version>-bin-win-x64.zip` ). At the time I am writing this article we are at release b8255. So, assuming you have a Laptop not older than mine, you - - - - - 

can download llama b8255 bin win cpu x64.zip 

2. Extract it to `C:\llama` 

3. Place your `.gguf` model in `C:\llama\models.` For example, let’s take the latest Qwen-3.5_2B from the Unsloth repo on Hugging Face: download in – - 

the `models` subfolder Qwen3.5 2B Q4_K_M.gguf 

4. Open PowerShell and run: 

```
cd C:\llama
```

   - `.\llama-server.exe -m models\Qwen3.5–2B-Q4_K_M.gguf -c 4096` 

1. Open `http://localhost:8080` in your browser 

## This is a reasoning model: if you want to avoid wasting tokens add at the end **`--reasoning-budget 0`** : 

```
-
.\llama-server.exe -m .\models\Qwen3.52B-Q4_K_M.gguf -c 4096--reasoning-budge
```

  

For hyper-parameters optimization you can refer to the Qwen3.5 unsloth page here: 

## _**Qwen3.5 - How to Run Locally Guide | Unsloth Documentation**_ 

_Run the new Qwen3.5 LLMs including Medium: Qwen3.5-35B-A3B, 27B, 122B-A10B, Small: Qwen3.5-0.8B, 2B, 4B, 9B and…_ 

_unsloth.ai_ 

**==> picture [121 x 126] intentionally omitted <==**

## 🔢 _**Bits Per Weight**_ **≠** _**Tokens Per Second**_ 

Here’s where things get interesting. 

Let’s have a look at the table from llama.cpp quantize README.md. This table answers one question: 

_If I quantize Llama-3.1–8B different ways, what do I actually gain or lose?_ 

The answer has four parts: 

## 1. bits/weight → How tightly packed is each number? 

2. size (GiB) → How much disk/RAM does it need? 

3. prompt processing t/s → How fast does it read your question? 

4. text generation t/s → How fast does it write its answer? 

Let’s break it down like we’re reading a nutrition label. 🏷 

## _**Understanding the Columns**_ 

```
bits/weight
```

_“How many digital switches store each model number?”_ 

Lower = more compression (2.0 bits = extreme, 16 bits = original) 

But: Not all bits are equal. IQ2 at 2.38 bits does more complex math than Q4 at 4.66 bits. 

```
size (GiB)
```

_“How much space does this model take on your disk/RAM?”_ 

Directly tied to bits/weight, but not perfectly (metadata adds overhead) 

Rule of thumb: `size ≈ (bits/weight × 8B weights) ÷ 8 bits/byte` 

## _**prompt processing t/s @ 512**_ 

_“How fast does the model read a 512-token prompt?”_ 

This is the prefill phase: parallel computation, compute-bound 

Higher = faster “thinking time” before it starts replying 

CPU insight: Less sensitive to quantization format (mostly math, not memory) 

```
text generation t/s @ 128
```

_“How fast does the model generate 128 tokens of response?”_ 

This is the decode phase: sequential, memory-bound 

Higher = snappier chat experience 

CPU insight: VERY sensitive to quantization format (memory bandwidth + dequantization cost) 

💡 _Key insight: For chat, text generation speed matters more than prompt speed. You wait once for prefill, but you wait for every token during decode._ 

## _**What the Data actually tells us**_ 

Let me highlight the patterns I see as a CPU-only user: 

Wait — Q2_K is faster than Q4_K_M? Yes! But there is a BUT…: 

## _**Prompt processing: the surprise**_ 

## Notice something weird? 

```
F16 (16-bit, 14.96 GB): 923 t/s prompt speed
Q8_0 (8.5-bit, 7.95 GB): 865 t/s
Q4_K_M (4.9-bit, 4.58 GB): 822 t/s
IQ1_S (2.0-bit, 1.87 GB): 859 t/s
```

## Prompt speed ⚡ doesn’t drop much with quantization! Why? 

Prefill is compute-bound, not memory-bound 

Modern CPUs have enough FLOPS to handle dequantization on the fly 

The bottleneck is math, not data movement 

💡 _Takeaway: If you only care about prompt speed (e.g., batch processing), even extreme quantization works fine. But for chat? Decode speed is king._ 

## _**To recap**_ 

When you see a model labeled `Q4_K_M` , the "4" means: _"Each weight is stored using ~4 bits instead of the usual 16."_ That's a 4× reduction in storage. Great for download size. Great for RAM. 

But inference is not only about storage. 

## _It’s about computation._ 

Every time your model generates a token, it must: 

1. Load the quantized weights from RAM 

2. Dequantize them (unpack the compressed values back to usable numbers) 

3. Run the math 

4. Repeat 

That “dequantization” step? It’s not free. And some formats make it _much_ more expensive than others. 

_Reducing the size of data doesn’t automatically speed things up… When your workload matches these ‘golden paths’, you get peak performance. Step outside them, and you hit slowdowns. — from_ 

_byteshape_ 

## _**Byteshape’s smoking gun**_ 

The team at byteshape.com ran extensive benchmarks across CPUs and GPUs. Their findings flipped the script! 

They found that cutting just 1.2 bits per weight could make inference 13% slower on an RTX 5090 — because the dequantization overhead outweighed the memory savings. 

And for CPU users? The news is even clearer: 

_“Contrary to the behaviour observed on our GPU setup, the KQ kernels outperform the IQ kernels on the Intel CPU. Accordingly, we suggest trying the KQ models first if you plan to run on CPUs.” — [byteshape CPU blog]_ 

_Tested on my Laptop — benchmarks. Your results will vary._ 

Notice something? The smallest file ( `UD-IQ2_XXS` ) is the _slowest_ . The "medium-sized" `Q3_K_S` is the fastest, together with `Q4_K_S` . 

That’s the plot twist. 

## 🗂 _**The KV Cache cameo**_ 

Before we wrap, a quick note on something that often gets overlooked: the KV cache. 

The KV cache is your model’s short-term memory. When you ask a question, the model doesn’t just “know” the answer: it looks back at the conversation so far. To avoid recomputing everything each time, it caches “keys and values” for previous tokens. 

## The thing is: the KV cache is not quantized by default. 

So even if your model weights are tiny (4-bit), a long conversation (say, 16K tokens) can still eat up gigabytes of RAM just for the cache. 

_More context = more cache = more RAM pressure._ 

If you _do_ need long contexts on a CPU, you can quantize the KV cache too (we’ll cover this in Part 3): 

```
.\llama-server.exe -m models\Qwen3.5–2B-Q8_0.gguf -c 8192 --kv-cache-type q8_0
```

This trades a tiny bit of quality for huge RAM savings. 

## _**Your first Win: the “just works” format**_ 

Okay, so what should you actually download? 

If you’re on a mid-range i5/i7 laptop and just want something that runs well: 

_Start with_ `Q4_K_M` _._ 

Why? Three reasons: 

1. CPU-optimized kernels: K-quant formats use simpler dequantization math that CPUs handle efficiently [byteshape CPU blog] 

2. Balanced quality: Retains ~96% of the original model’s performance while cutting file size by ~75% 

3. Community default: It’s the most tested, most recommended format for a 

   - reason 

## _You don’t need the smallest file. You need the right format._ 

## 🧪 _**Try This Yourself (5-Minute Experiment)**_ 

Want to see this in action on _your_ machine? We’re going to use Python to measure the speed. It’s the standard tool for AI work, and it lets us get precise numbers. 

Prerequisites: Make sure you have Python installed. If not, grab it from python.org. 

- 1️⃣ Download two versions of the same model: 

One ending in `IQ2_XXS` (if available) 

One ending in `Q4_K_M` 

For my tests I downloaded the models from the official Unlsoth repo of Qwen3.5–2B-GGUF 

## _**unsloth/Qwen3.5-2B-GGUF · Hugging Face**_ 

_We're on a journey to advance and democratize artificial intelligence through open source and open science._ 

_huggingface.co_ 

**==> picture [121 x 126] intentionally omitted <==**

Qwen3.5–2B-UD-IQ2_XXS.gguf (click here to download) 

Qwen3.5–2B-Q4_K_M.gguf (click here to download) 

`import subprocess import os from pathlib import Path # CONFIGURATION MODEL_FILENAME = "Qwen3.5-2B-UD-IQ2_XXS.gguf" # MODEL_FILENAME = "Qwen3.5-2B-Q4_K_M.gguf" MODEL_DIR = Path("models") MODEL_PATH = MODEL_DIR / MODEL_FILENAME # Get absolute path of the script's directory to find the exe reliably SCRIPT_DIR = Path(__file__).parent.resolve() CLI_PATH = SCRIPT_DIR / "llama-cli.exe" PROMPT = "Explain Generative AI in simple terms." TOKENS_TO_GENERATE = 128 THREADS = 2 # your CPU threads capacity -2 def run_benchmark(): # 1. Check if files exist before running if not CLI_PATH.exists(): print(f"` ❌ `Error: CLI executable not found at {CLI_PATH}") return if not MODEL_PATH.exists(): print(f"` ❌ `Error: Model file not found at {MODEL_PATH}") print(f"   Check if the filename has a special dash character (– vs -)") return print(f"` 🚀 `Starting benchmark for {MODEL_FILENAME}...") print(f"   Looking for model at: {MODEL_PATH}") print("-" * 40) # 2. Construct command list cmd = [ str(CLI_PATH), "-m", str(MODEL_PATH), "-p", PROMPT, "-n", str(TOKENS_TO_GENERATE), "-t", str(THREADS), "-st" # Requested flag: ensures CLI closes after -n tokens ] # 3. Run llama-cli try:` 

```
        subprocess.run(cmd)
```

`print("-" * 40) print("` ✅ `Benchmark complete. Check the output above for llama.cpp inter except Exception as e: print(f"` ❌ `Execution Error: {e}") print("   Tip: If you get 'unknown argument' for --exit-after-generation if __name__ == "__main__": run_benchmark()` 

## 3️⃣ Edit the `MODEL_PATH` in the script to match your file. 

## 4️⃣ Run it twice (once for each model): 

```
python benchmark.py
```

_test with IQ2_XXS_ 

## 5️⃣ Compare the tokens/sec. I’d bet money the `Q4_K_M` wins. 

```
Test with Q4_K_M
```

## _**Coming next: the secret war between CPUs and GPUs**_ 

So why _do_ IQ formats love GPUs but hate CPUs? What’s happening under the hood that makes the same file run 4× faster on one chip and crawl on another? 

In Part 2 , “Byteshape’s Discovery: Not All Bits Are Created Equal” — we’ll open the black box and see: 

How CPUs and GPUs “think” differently about data 

Why “smart” compression can backfire on sequential hardware 

Real benchmark tables you can use to pick your next download _Open in app_ 

Until then: if your local AI feels slow, don’t blame your CPU. Blame the quantization format. Then switch to `Q4_K_M` or to `Q4_K_S` and watch it fly. 

Your laptop will thank you. 🦥⚡ 

_Series: “Not All Quantizations Are Born Equal”_ 

- ✅ Part 1: Your CPU is NOT Broken _(you are here)_ 

- ⏳ Part 2: Byteshape’s Discovery: Not All Bits Are Created Equal 

- ⏳ Part 3: Pick Your Poison: A Friendly Guide to Quantization Formats 

_Subscribe to get Part 2 in your inbox next week. Or follow me on Medium for updates._ 🚀 

