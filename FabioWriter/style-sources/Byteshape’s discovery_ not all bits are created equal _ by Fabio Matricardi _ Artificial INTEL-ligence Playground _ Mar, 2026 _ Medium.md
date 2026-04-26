## _**Byteshape’s discovery: not all bits are created equal**_ 

_How CPUs and GPUs “think” differently about data — Not All Quantizations Are Born Equal part 2_ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 12 min read · Mar 17, 2026_ 

**==> picture [511 x 287] intentionally omitted <==**

Last time, we uncovered the uncomfortable truth that… smaller model files don’t automatically mean faster inference. 

If you tried the `Q4_K_M` experiment I suggested and saw your tokens-persecond jump, congratulations—you've already escaped the quantization trap. 

But if you’re still wondering _why_ a “smarter” 2-bit format can run slower than a “dumber” 4-bit one on your i5 or i7 laptop, you’re asking the right question. 

Today, we’re going deeper in the topic. 

By the way, this is part 2 of the series _“Not All Quantizations Are Born Equal”. You can find the entire Series links here_ 

✅ Part 1: Your CPU is NOT Broken 

👉 Part 2: Byteshape’s Discovery: Not All Bits Are Created Equal _(you are here)_ 

✅ Part 3: Pick Your Poison: A Friendly Guide to Quantization Formats 

✅ Part 4: Llama.cpp optimization for CPU: not all quantizations are born equal 

- ⏳ Part 5: _The Vulkan Advantage_ 

It is time to explore why CPUs and GPUs have fundamentally different personalities when it comes to processing quantized data, and how the research team at byteshape.com exposed a quiet scandal in the quantization world: some formats are secretly optimized for GPUs, and they’ll quietly sabotage your CPU performance. 

Don't worry! No kernel code or matrix math. This is the story of why your hardware picked a side in the quantization wars, and how to make sure you’re on the winning team. 

## _**Quick Recap: the plot so far**_ 

If you missed Part 1, here’s the TL;DR: 

GGUF is a universal format for quantized models, but not all quantization methods are equal 

- Bits per weight ≠ tokens per second: dequantization overhead can cancel out file-size savings 

- **`Q4_K_M`** is the CPU-safe default: balanced quality, CPU-optimized kernels 

- IQ formats (like `IQ2_XXS` ) can be _slower_ on CPUs despite smaller file sizes 

And finally, we want to answer the burning question: _Why?_ 

## _**Hardware Personalities: CPU vs GPU**_ 

Let’s start with a metaphor. Imagine you’re asking two different assistants to organize a library: 

## Your CPU is a meticulous librarian 🧓 

Prefers one task at a time, done thoroughly 

- Excels at complex, sequential logic 

- Has a small but fast desk (cache) for frequently used books 

Gets bogged down if you throw too many unrelated tasks at once 

## Your GPU is a warehouse robot army 🤖 

Loves doing the same simple task in parallel, thousands of times 

Has massive floor space (VRAM) but slower individual robots 

Wastes energy if tasks are not perfectly uniform 

_Small key insight: Quantization formats trigger different “kernels” (code paths). Some kernels match the librarian’s workflow. Others only the robot army understands._ 

## _**Why This Matters for Quantization**_ 

When your model runs inference, it must dequantize compressed weights on the fly. The format you choose determines _how_ that decompression happens: 

In plain English: IQ formats do “smarter” compression, but that smartness costs CPU cycles. 

## _**For personal inspiration**_ 

I have been following for years few experts in the quantization strategies. If you want to go more into details, I invite you to follow Benjamin Marie on his Substak called _The Kaitchup — AI on a Budget_ . 

**==> picture [121 x 57] intentionally omitted <==**

_huggingface.co_ 

**==> picture [121 x 69] intentionally omitted <==**

## _**kaitchup (The Kaitchup)**_ 

_Org profile for The Kaitchup on Hugging Face, the AI community building the future._ 

_huggingface.co_ 

**==> picture [121 x 126] intentionally omitted <==**

You will not regret it! 

_image from https://ncsoft.github.io/ncresearch/_ 

## _**IQ vs KQ: the Quantization family feud**_ 

Let’s meet the two main factions. 

## _**KQ (K-Quant): the CPU’s reliable friend**_ 

K-Quant formats use a grouped quantization strategy. To stay in the anlogy, it is like packing books into labeled boxes: 

```
Model weights
│
▼
┌─────────────────┐
│  Super-Blocks   │← Groups of sub-blocks
├─────────────────┤
│┌───────────┐│
```

```
││Sub-Block 1││← 16-32 weights each
││• scale s₁││← Simple scale factor
││• min m₁││
│└───────────┘│
└─────────────────┘
```

Each sub-block has its own scale factor, so decompression is fast and predictable. CPUs love this: simple math, cache-friendly access patterns. 

## _**IQ (Importance-Quant): the GPU’s secret weapon**_ 

IQ formats take compression further. They use an importance matrix to decide which weights matter most, then apply non-linear quantization: 

```
Model weights
│
▼
┌─────────────────┐
│ Importance Map  │← Pre-computed "which weights matter"
├─────────────────┤
│ Non-linear code │← Complex lookup tables
├─────────────────┤
│ Extra math steps│← More CPU cycles per weight
└─────────────────┘
```

I-quants such as `IQ2_XXS` , `IQ2_XS` , `IQ2_S` , `IQ3_XXS` , `IQ3_XS` , `IQ3_S` , `IQ3_M` , `IQ4_XS` , and `IQ4_NL` are GGUF quantization formats aimed at preserving as much quality as possible at low bitrates. 

_- - The IQ family is defined around importance matrix based reconstruction: weights are recovered using a super-block scale and an importance matrix. — from the Kaitchup by Benjamin Marie_ 

`imatrix` byte, especially when a good is available. That advantage is real, but it is not uniform across the whole family. 

IQ quants are brilliant for GPUs: massive parallelism can handle the complex lookups all at once. But for a CPU? You are asking the librarian to solve a puzzle for every single book. 

## _**Byteshape’s Smoking Gun**_ 

The team at byteshape.com didn’t focus on theories alone: they benchmarked them. And their findings were stark: 

_On GPU setup, low-bit KQ kernels are noticeably less efficient than IQ kernels. As a result, we constructed the GPU variants with a preference for IQ quantization.” [byteshape GPU blog]_ 

Translation: _If you have a GPU, IQ formats can be worth it._ 

But then came the CPU results: 

_Contrary to the behavior observed on our GPU setup, the KQ kernels outperform the IQ kernels on the Intel CPU. Accordingly, we suggest trying the KQ models first if you plan to run on CPUs.” [byteshape CPU blog]_ 

If you’re CPU-only and you downloaded an `IQ2_XXS` model because "2-bit sounds tiny," you didn't save time: you gave your CPU a harder puzzle to solve. 

## Here a take from the mentioned above Benjamin Marie Substack: 

_On modern CPUs and GPUs, K-quants generally match or beat legacy formats in throughput because you move fewer bytes for the same quality._ 

And what about the suffixes (S, M and L)? During quantization we encode a “mix levels” across tensors. Examples for Q4_K: 

`Q4_K_S` (small): Keeps almost everything at 4-bit 

- `Q4_K_M` (medium): Selectively raises precision for more sensitive tensors 

- (for example, attention value projections or final layers) using 5–6 bits 

- `Q4_K_L` (larger): Even more relaxed than Q4_K_M. 

The effective bits/weight rise accordingly, buying back quality where it matters. In practice (for you decision): 

Q4_K_M is a widely useful default for 4-bit deployments (Q4_K is also OK for large models). 

Q5_K_M is a high-quality setting that is close to imperceptible degradation for many tasks. 

Q6_K is for cases where you want “almost lossless” behavior and still want memory savings. 

Keep in mind that for most models, you won’t see much difference in quality between S, M, and L variants, unless you are dealing with small models (let’s say <8B models). 

## _**Real Numbers: what this means for your Laptop**_ 

Let’s make this concrete. Below are _the_ benchmarks I collected for a Qwen3.5–2B model on my Lenovo X260 (my 2016 old Laptop, Intel Core i5 CPU with 16GB RAM, Windows 11). Your results will vary, but the _relative_ differences hold. 

_chart by the author_ 

What this chart is telling us? 

1. The smallest file ( **`IQ2_XXS`** ) is the slowest—60% of `Q4_K_M` speed 

2. **`Q4_K_M`** hits the sweet spot: fastest TPS _and_ high quality (96%) 

3. Going bigger ( **`Q8_0`** ) doesn't help speed—it just uses more RAM for minimal quality gain 

Here’s my unpopular opinion: 

_If you’re running on CPU, ignore the “2-bit” hype. You’re paying in speed for savings you don’t need._ 

Think about it: 

- A `Q4_K_M` model is ~1.3 GB. 

- You "save" 0.6 GB. 

## But you lose almost 2 tokens per second. 

Is 0.7 GB of disk space worth waiting 2× longer for every response? For most of us: no. 

And we were using a relatively Small model (2B parameter): if you try this with a 3B or 4B model, your loss will be higher (in the next section related to the “Format Swap” experiment you will see)! 

Here my choice of best model in the Small format factor: 

- mistralai_Ministral-3–3B-Instruct-2512-Q4_K_M 

- Qwen3–4B-Instruct-2507-Q3_K_S-2.77bpw 

- granite-4.0-h-tiny-Q4_K_M 

Feel free to test them on your own Pc. 

## _**When should you use extreme quantization?**_ 

Only in two cases: 

1. RAM is your absolute bottleneck (<6GB available): Then `Q3_K_S` or `Q2_K` might be necessary to fit the model at all. And in my tests `Q3_K_S` has a wonderful speed (but quality is lower) 

2. You’re batch-processing offline and don’t care about latency: Then smaller files = more models in memory 

_“Treat memory as a constraint, not a goal. Once a model fits on your device, what matters is the tradeoff curve: TPS versus quality.” [byteshape GPU blog]_ 

In other words: Don’t optimize for file size. Optimize for your actual experience. 

_how to run the experiment_ 

## 🧪 _**Try this: the “Format Swap” experiment**_ 

Here’s a 10-minute experiment to see the CPU/GPU divide in action (even if you only have a CPU): 

1. Download three versions of the same model: 

   - `IQ2_XXS` (extreme compression) for example Ministral-3–3B-Instruct- 

   - 2512-UD-IQ2_XXS.gguf (click here to download it) from the Unsloth repo - – - - - 

   - for Ministral 3 3B Instruct 2512 GGUF. 

   - `Q4_K_M` (balanced) use this Ministral-3–3B-Instruct-2512-Q4_K_M.gguf: 

   - (click here to download) 

   - `Q4_K_S` (a little smaller) use this Ministral-3–3B-Instruct-2512- 

   - Q4_K_S.gguf (click here to download) 

   - `Q8_0` (near-lossless) use this Ministral-3–3B-Instruct-2512-Q8_0.gguf 

   - (click here to download) 

## 2. Run the model and open your browser at localhost:8080 

- use this command from the Terminal: 

- `.\llama-server.exe -m .\models\Ministral-3–3B-Instruct-2512-UD-` 

```
IQ2_XXS.gguf -t 2 -n 250 — reasoning-budget 0 -c 4096
```

3. paste this prompt in the chatbox: `Explain the difference between CPU and` 

   - `GPU inference in simple terms.` 

## 4. Plot your results in a simple table: 

```
Format    | File Size | TPS   | Quality Estimate
----------|-----------|-------|-----------------
IQ2_XXS   | 1.1  GB   | ___   | ~89%
Q4_K_M    | 2.15 GB   | ___   | ~96%
Q4_K_S    | 2.05 GB   | ___   | ~94%
Q8_0      | 3.65 GB   | ___   | ~99%
```

Ask yourself: Which format gives me the best experience for my use case? 

Why Ministral-3B? 

In my opinion this model is the best 3B LLM you can find as of today. It is able to understand the user intent, is good at coding, it is ready for function callings. 

And it runs on CPU at discrete speed (try it yourself!) 

## _I ran a test with Ministral-3–3B-Instruct-2512-Q4_K_S and I got… 4.1 tokens/second_ 

## _**But what if I have a GPU, even a modest one?**_ 

I will cover in part 4 (not yet ready) using the llama.cpp binaries for the Vulkan drivers. 

After part 1 Isaac Tigges, a Medium reader, shared with me his personal project called A.T.L.A.S (Adaptive Test-time Learning and Autonomous Specialization). Isaac is a Business Management student at Virginia Tech. He is running this project fully local, using llama.cpp: 

_The whole thing runs on llama.cpp with KV cache Q4_0 quantization, speculative decoding with a 0.6B draft model, and everything fits in ~12.9GB of 16GB VRAM..._ 

Don’t worry: we introduced KV cache quantization in Part 1, and we will talk about Speculative Decoding soon! 

But what the hell is A.T.L.A.S? 

_A.T.L.A.S achieves 74.6% LiveCodeBench pass@1 with a frozen 14B model on a single consumer GPU — up from 36–41% in V2 — through constraint-driven generation and self-verified iterative refinement. The premise: wrap a frozen smaller model in intelligent infrastructure — structured generation, energy-based verification, self-verified repair — and it can compete with frontier API models at a fraction of the cost. No fine-tuning, no API calls, no cloud. Fully self-hosted — no data leaves the machine, no API keys required, no usage metering. One GPU, one box._ 

## _**GitHub - itigges22/ATLAS: Adaptive Test-time Learning and Autonomous Specialization**_ 

_Adaptive Test-time Learning and Autonomous Specialization - itigges22/ATLAS_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**Coming Next: Your Personal Quantization Compass**_ 

So you now know _why_ some formats love GPUs and hate CPUs. But the million-dollar question remains: 

_Open in app_ 

~~_“Which format should I actually download?”_~~ 

## In Part 3 — “Pick Your Poison: A Friendly Guide to Quantization Formats”, 

we’ll cut through the noise with: 

- A simple 3-question decision tree (RAM, context length, patience) 

- Format recommendations by use case (chat, coding, long docs) 

- Quick tweaks that actually help ( `threads` , `mmap` , `KV cache` ) 

- The “I just want it to work” starter pack for Windows 

No more “let’s try this and let’s see”. 

Switch to `Q4_K_M` . Watch it fly. Then come back and tell me your TPS. 🚀 

_Series: “Not All Quantizations Are Born Equal”_ 

- ✅ Part 1: Your CPU is NOT Broken 

- ✅ Part 2: Byteshape’s Discovery: Not All Bits Are Created Equal _(you are_ 

- _here)_ 

- ⏳ Part 3: Pick Your Poison: A Friendly Guide to Quantization Formats 

- ⏳ Part 4: (NEW) The easy way for llama.cpp on little GPU with Vulkan driver 

_Subscribe to get Part 3 in your inbox next week. Or follow me on Medium for updates._ 🦥⚡ 

_Local Gpt Thepoorgpuguy Llamacpp Your Ai Your Rules Python4ai_ 

