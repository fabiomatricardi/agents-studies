## _**The smallest 8B model ever created is not really an advancement**_ 

_Bonsai is the 1bit in the real world for the first time: but the claims are far from good. You still need a GPU or you are done!_ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 10 min read · Apr 3, 2026_ 

**==> picture [511 x 285] intentionally omitted <==**

## Let’s be clear. I have nothing against PrismML project. 

It is a fantastic idea, focused on edge computing (modern ones) but forgetting the 1-bit LLM agenda: remove the bottleneck of GPU computing, from training to inference time. 

1.7b in 1-bit quantization format, craving for Intelligence Density. 

You can read the entire whitepaper here. 

Their Caltech-backed tech shifts the efficiency frontier on GPUs (RTX 4090 hits 368 t/s) and Apple Silicon. Simply put, the claims on social are too exaggerated — CPU support is half-baked, no public benchmarks exist for it. 

Even though the initial plan outline was clear: 

_For the last decade, AI has advanced along a clear trajectory: to make smarter models, you make them bigger. More parameters, more GPUs, more power, more memory, and more cost. That approach worked. It gave us models that can reason across long contexts, solve difficult problems, and generate software, research, and creative work at remarkable quality._ 

_But it also created a deep structural constraint on the future of AI: the most capable intelligence became trapped inside massive clusters and specialized infrastructure. Yet some of the most important uses of AI are not confined to data centers. They happen on phones, laptops, vehicles, robots, secure enterprise source environments, and edge devices. — from_ 

A real revolution would be CPUs performing as good as GPUs. You may think this is sci-fi. But it is not. 

The 1-bit LLM was meant to sidestep matrix multiplications that favor GPU parallelism. Yet x86 CPU kernels for Q1_0_g128 fail, forcing inefficient fallbacks. Community forks like iltom/ll.cpp hint at fixes, but we’re not there yet. 

Imagine how many CPU there are on this planet, and the cost of them: all of this compared to the GPUs that are running the Generative AI show. Guess no one really wants to overrule the ones who are controlling the game. 

If you want to know more in details, here is the actual test, how to run it on your PC and… see it yourself. 

I run the model on my crappy 2016 old Lenovo X260, and the results are not what you would have expected… at all! 

I wonder who tested the Bonsai-8b on their machine before posting such … _outstanding news_ 

## _**The test and the idea: bottom line up front**_ 

We are in early stages, and PrismML announced they managed to Concentrate Intelligence by a 14x factor. And this is huge. 

_Concentrating intelligence means increasing the useful intelligence a model delivers per unit of size, power, and deployment footprint. This depends on several factors: the hardware the model runs on, the specifics of the workload, but, most critically, the size of the model. For this reason, at PrismML, we have focused on optimizing the Intelligence Density, the amount of intelligence a model can deliver per unit size (measured in GB). It’s a practical measure determining whether advanced AI remains locked inside expensive infrastructure or becomes source available wherever it is needed. — from_ 

derived method (proprietary, trained on TPUs) preserves capability via advanced compression math. 

It outperforms expected low-bit tradeoffs in agentic tasks and long contexts, shifting the “intelligence vs. size” Pareto frontier. Future 1-bit hardware could amplify gains by minimizing multiplications. 

The demo and benchmarks are outstanding. 

And since I don’t believe the news blindly, I tried to run it on my CPU only laptop… and believe me, If I run a 9B model with classic GGUF quants, there are really no improvements in relation to Bonsai 8B. 

I built the special llama.cpp fork for the project and run on my PC Bonsai 8B. Then I discovered that Phil Tomson on GitHub noticed the poor support for 

CPU only, and forked with his own code the repo to include AVX2, AVX512 and ROCm for AMD GPUs support to the new family of 1-bit LLM. 

With this move, finally, I was able to load the model and get some results, little faster than a similar 8b model in classic Q4_K_M quants. 

My CPU-only experience with Bonsai 8B not matching PrismML’s claims stems mainly from immature CPU support in the required software and context length overhead. Benchmarks focus on GPU/Apple Metal, where the 1.15 GB parameter footprint shines, but CPU runs hit bugs and extra RAM costs. 

## _**The long story short**_ 

PrismML’s 1-bit Bonsai 8B is an 8.2 billion parameter LLM with all weights, quantized to true 1-bit (+1 or -1) across embeddings, attention, MLPs, and the output head, requiring just 1.15 GB of memory. 

PrismML reports that it matches leading full-precision 8B models (like Qwen3 8B or Llama 3.1 8B) on benchmarks with an average score of 70.5, while being 14x smaller, 8x faster in inference, and 4–5x more energy efficient. 

This delivers over 10x higher “intelligence density” (capability per GB), and enables edge deployment on devices like iPhones (44 tokens/sec on iPhone 17 Pro Max) and Macs. 

## _**My own verification status**_ 

Independent sources like Hugging Face listings and YouTube tests confirm the model is available (Apache 2.0 licensed, GGUF/MLX formats) and its 

benchmarks align with PrismML’s reports, placing it near top 8B models at 1/14th size. 

Community discussions on Reddit and Hacker News note it requires modified llama.cpp for inference but show promising real-world speed on consumer hardware, though full third-party benchmark suites are still emerging post-launch (March 31, 2026). 

Standard Q4_K_M (~4.5 GB for 8B) is optimized for CPU with mature x86/AVX kernels, yielding 5–20 t/s depending on CPU cores. 

- 1-bit dequantization bugs: On x86 CPU, Q1_0_g128 kernels fail, producing “garbage output” and 1 t/s or less; GPU (CUDA/Metal) works fine. 

- Missing optimizations: No CPU benchmarks from PrismML — all are GPU-focused (e.g., 368 t/s RTX 4090); forks like iltom/ll.cpp add AVX2/512 CPU support. 

- Windows 11 CPU build: Loads fine, but outputs nonsense at ~1 t/s; multi/single-thread same. 

## _**How to make it work (from the Original repo)**_ 

This is the build method from the official GitHub page: 

## _**GitHub - PrismML-Eng/llama.cpp: LLM inference in C/C++**_ 

_LLM inference in C/C++. Contribute to PrismML-Eng/llama.cpp development by creating an account on GitHub._ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

```
# Clone the PrismML fork of llama.cpp (includes Q1_0_g128 kernels)
git clone https://github.com/PrismML-Eng/llama.cpp
cd llama.cpp
```

## build the project 

```
cmake -B build
```

## And compile it 

```
cmake --build build -j
```

By the way, after cloning and compiling, the llama.cpp forked folder weights something like 5 Gigabytes! 

To run the forked version of llama.cpp with the Bonsai-8B.gguf model you need to download it from here: 

## _**prism-ml/Bonsai-8B-gguf · Hugging Face**_ 

_We're on a journey to advance and democratize artificial intelligence through open source and open science._ 

**==> picture [121 x 95] intentionally omitted <==**

**==> picture [121 x 32] intentionally omitted <==**

From the terminal (adjusting your root) run: 

`C:\tests\1bit\llama.cpp\build\bin\Debug\llama-cli.exe -m .\Bonsai-8B.gguf -p "Ex`   

This is my initial result, after 15 minutes and with more than 9 Gb of RAM busy… 

Following the Reddit instructions I tried with a new repo, that support CPUs out of the box. 

## _**The forked*forked method**_ 

PrismML fork llama.cpp repo is still not mature. It covers specific GPUs and the Mac Silicon architecture, but CPU support is glitchy and unreliable. 

But… Phil Tomson forked the forked repo and magically (and mathematically) we have… 

_LLM inference in C/C++ (fork of PrismML fork that enables CPU (incl AVX2 and AVX512) and ROCm for AMD GPUs_ 

_**GitHub - philtomson/llama.cpp: LLM inference in C/C++ (fork of PrismML fork that enables CPU (incl…**_ 

**==> picture [121 x 59] intentionally omitted <==**

_LLM inference in C/C++ (fork of PrismML fork that enables CPU (incl AVX2 and AVX512) and ROCm for AMD GPUs …_ 

_github.com_ 

**==> picture [121 x 68] intentionally omitted <==**

## Now, clone the repo, and build the Relase 

```
git clone https://github.com/philtomson/llama.cpp.git
```

```
cd llama.cpp
```

Guide to Build release here, but basically you only need 2 commands: 

```
cmake -B build
cmake --build build --config Release
```

You will find the executable in the subdirectory called `build\bin\Release` . 

Or… if you have a Windows PC you can get my binaries, already compiled here: 

## _**Release Binaries x64 Windows for 1-bit llama.cpp support ·…**_ 

_LLM inference in C/C++ (fork of PrismML fork that enables CPU (incl AVX2 and AVX512) and ROCm for AMD GPUs Built from…_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

```
.\llama-cli.exe -m .\Bonsai-8B.gguf -p "Explain quantum computing in simple term
```

  

## Note the following details about the parameters in the command line: 

- `-n 250         max new tokens --temp 0.5     temperature, as suggested in the official Model card --top-p 0.85   top` _`_p, as suggested in the official Model card --top-k 20     top_`_ `k, as suggested in the official Model card -ngl 0` **`**CRITICAL**`** `remember to set it to 0 (CPU only) -st            single turn -ctk q4` _`_0`_ _**`**CRITICAL**`**_ _`the KV chache will go to F16 otherwise -ctv q4_`_ `0` **`**CRITICAL**`** `the KV chache will go to F16 otherwise --mmap         Memory Map enabled` 

## ⚠ Pay attention to `ngl` , and the `KV cache` values! 

These are the data, in terms of RAM and speed: 

## 💻 RAM: 1.1 Gb 

📈 SPEED: [ Prompt: 2.6 t/s | Generation: 2.4 t/s ] 

I tried to compare these values with a similar model: so I took this 

_**Jackrong/Qwen3.5-9B-Claude-4.6-Opus-Reasoning-Distilled-v2GGUF · Hugging Face**_ 

_We're on a journey to advance and democratize artificial intelligence through open source and open science. huggingface.co_ 

**==> picture [121 x 126] intentionally omitted <==**

Downloaded the standard Q4_K_M quants, fired my llama.cpp for x64 CPU only on Windows and: 

`.\llama-cli.exe -m C:\FABIO-AI\MODELS_medium\Qwen_Qwen3.5-9B-Q3_K_M.gguf -p "Exp`   

with the same parameters of Bonsai-8b. 

💻 RAM: 4.2 Gb 

📈 SPEED: [ Prompt: 2.9 t/s | Generation: 1.9 t/s ] 

It doesn’t look that big the difference, isn’t it? 

## _**Some numbers and comparisons**_ 

I tested all the 3 variants of the Bonsai family, and compared to a similar model size: 

Bonsai-1.7B → Qwen3–1.7B-Q4_K_M.gguf 

Bonsai-4B → Qwen3–4B-Instruct-2507-Q4_K_M.gguf _Open in app_ 

~~Bonsai-8B → Qwen_Qwen3.5–9B-Q3_K_M.gguf~~ 

You can see the numbers in the table above. 

I was honestly expecting much more, and I hope this is going to be only the start of something really revolutionary. 

Because until CPU can perform at the same level of GPUs, this kind of Artificial Intelligence will be always in the hands of the few (in terms of money, development, infrastructure, governance and power). 

Don’t trust blindly the claims! 

Verify it yourself. 

So, let me know how that worked for you! 

_Thepoorgpuguy Local Gpt Your Ai Your Rules 1 Bit Llms Llama Cpp_ 

