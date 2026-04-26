_**AI Frankenstein is alive — part 1** Meet the new brains behind tomorrow’s Intelligence_ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 9 min read · Feb 16, 2026_ 

**==> picture [511 x 394] intentionally omitted <==**

Imagine stitching together parts from different creatures — not to make a monster, but to build something smart, hopefully fast, and more useful than anything that came before. 

That’s not a horror story anymore. It’s how today’s most advanced AI systems are being built. 

For years, the world of artificial intelligence has revolved around a single kind of brain: the large language model, or LLM. 

You’ve likely used one — whether it’s ChatGPT, Gemini, or Claude. These models are astonishingly good at conversation, writing, and even coding. But under the hood, they all share a critical limitation: they think one word at a time, like a writer forced to type with one hand while never able to look back, never revising, just forging ahead. 

This “one-word-at-a-time” design made sense in the early days of AI. It was predictable and scalable. But as we move beyond chatbots and into realworld applications, like diagnosing medical records, summarizing legal briefs, or generating real-time reports from live data, we’re hitting a wall. 

_These models are slow, expensive to run, and sometimes brittle when faced with structured tasks._ 

But recently we entered a new era of AI: one where there is no single “best” architecture. Instead, researchers and companies are assembling custom AI brains (hybrids, specialists, and parallel experts and thinkers) each engineered for a specific kind of intelligence. 

## _**AI Frankenstein is alive — part 2**_ 

_The AI that writes like a sculptor: how Text Diffusion Models are revisiting Text Generation_ 

_medium.com_ 

**==> picture [121 x 103] intentionally omitted <==**

Far from being a science fiction short story, this is happening right now, in labs and open-source projects around the world. 

And the result? 

A quiet shift in how machines understand and generate language. 

This series — _AI Frankenstein is Alive_ — explores that revolution. 

Over the next four posts (this one is included…), we’ll meet three . groundbreaking new model architectures that are challenging the _status quo_ They’re faster, smarter, more efficient, and, in many ways, more human-like in how they think. 

## _**They’re also, in the best sense of the word, Frankensteinian: stitched together from the most promising parts of earlier ideas, but alive with new purpose.**_ 

Let’s begin by meeting the three new “creatures” reshaping the near future of Generative AI. 

## _**The End of the One-Size-Fits-All AI**_ 

For the past five years, if you said “AI language model,” almost everyone imagined something like GPT — a decoder-only Transformer trained to predict the next word in a sentence. 

And for good reason: this architecture scaled beautifully. Throw more data and more compute at it, and it got dramatically better. 

But scaling has its limits. As these models grow, so do their costs — in energy, in time, and in infrastructure. More importantly, they’re not always the right tool for the job. 

Ask a decoder-only model to summarize a 50-page report, and it will _try_ . But it wasn’t designed for that. It was designed for open-ended creation, not precise transformation. 

Now, a shift is underway. 

Rather than building ever-larger versions of the same model, researchers are asking: _What if we design different brains for different tasks?_ 

The answer is a new wave of specialized architectures, each optimized for speed, efficiency, structure, or reasoning. We are finally moving from a single universal Swiss Army knife to a curated toolbox: a scalpel for surgery, a wrench for plumbing, a chisel for sculpture. 

## _**And if you think about it… it is simply practical!**_ 

Businesses need AI that’s fast enough for real-time customer service. Doctors need models that can accurately extract facts from patient histories. 

_The old one-size-fits-all model is giving way to task-aware, purpose-built intelligence._ 

And at the heart of this shift are three powerful new designs. 

## _**1. The Sculptor AI: Diffusion Language Models**_ 

Imagine an artist shaping a statue from a block of marble. They don’t start with the left ear, then the right eye, then the nose. They see the whole form at once and refine it gradually, chipping away excess, smoothing contours, adjusting proportions. The final piece emerges not in a sequence, but as a whole. 

This is the essence of diffusion language models — the first major challenger to the “one-word-at-a-time” paradigm. Instead of generating text left to right, a diffusion model starts with pure noise (a jumble of random symbols) and iteratively _refines the entire output at once_ , like an artist polishing their sculpture. 

The result? 

## Blazing speed and built-in self-correction. 

Because it works on all words simultaneously, it can generate a paragraph in the time a traditional model writes a sentence. 

And if it realizes halfway through that the opening phrase doesn’t fit, it can revise it (something autoregressive models simply can’t do without starting over). 

Projects like LLaDA and Dream are pioneering this approach in the opensource world. And now, Google has entered the race with Gemini Diffusion, a research model that reportedly generates 10,000 tokens in just 12 seconds — a speed previously thought impossible for high-quality text generation. 

A faster and _more flexible_ AI, one that can edit, revise, and restructure on the fly. In our next post, we’ll discuss more about how diffusion models work, why they’re so revolutionary, and what open-source tools like dLLM are doing to make this technology accessible to everyone. 

## _**2. The Bilingual Translator: Revamped Encoder-Decoder Models**_ 

Before the rise of GPT, the dominant AI architecture for language tasks was the encoder-decoder model. You can think of it like a sort of Google Translate in its early days. One part (the _encoder_ ) reads and fully understands your input. The other part (the _decoder_ ) uses that understanding to craft a precise output. 

## _**Inside the Matrix: cracking the Code of sequence models with Encoders base LLMs**_ 

_Dive into the rabbit hole of AI architecture, where information flows like Morpheus’ code, revealing the secrets behind…_ 

_ai.plainenglish.io_ 

**==> picture [121 x 126] intentionally omitted <==**

This two-stage process fell out of favor during the LLM boom because it was harder to scale (and more expensive to train). But it turns out it was ahead of its time. 

## _**The secret Google LLM nobody is talking about.**_ 

_T5Gemma series of encoder-decoder models: the smart upgrade of the T5 family_ 

_generativeai.pub_ 

**==> picture [121 x 126] intentionally omitted <==**

Now, with modern techniques, the encoder-decoder is making a stunning comeback, especially for tasks like summarization, question answering, and translation. 

Why? 

Because it’s inherently more efficient. For the same amount of computing power, it consistently outperforms decoder-only models. One study found it delivers 4.7 times higher throughput on everyday devices. 

In mid-2025, Google supercharged this revival with T5Gemma, a clever family of models that _repurposes_ its existing Gemma 2 AI (a decoder-only model) into a full encoder-decoder system. 

Instead of training from scratch, Google “adapted” the brains of its best models, saving time, energy, and cost. Even more ingeniously, T5Gemma allows the encoder and decoder to be _different sizes_ : say, a powerful 9- billion-parameter encoder paired with a lean 2-billion-parameter decoder — perfect for input-heavy tasks like reading long documents. 

T5Gemma doesn’t just bring back an old idea; it reimagines it for the modern age. And as we’ll explore in Post #3, this strategy could be the key to making high-performance AI accessible to everyone, not just tech giants. 

## _**3. The Modular Superbrain: Hybrid MoE + Mamba-2 Models**_ 

Now imagine an AI that doesn’t just have one brain, but a whole team of specialists. When you ask it a coding question, the “programming expert” wakes up. When you request a poem, the “creative writer” takes over. The others stay asleep, saving energy. 

This is the idea behind Mixture of Experts (MoE) — and it’s at the core of the most ambitious new architecture: hybrid models that combine MoE, Mamba-2 state-space layers, and traditional Transformer attention. 

Traditional Transformers struggle with long documents because their memory use explodes as text gets longer. Mamba-2, a breakthrough from 2024, solves this by using a different kind of memory — one that scales _linearly_ , not quadratically. It can handle 100,000+ words with ease. 

But Mamba is not that perfect at capturing fine-grained details. So the newest hybrid models — like IBM’s Granite 4.0 — use a 9:1 ratio: nine layers of efficient Mamba processing, punctuated by one layer of high-precision Transformer attention. 

The result? 

A model that can be both fast and accurate, massive… but efficient. 

Granite 4.0 also uses MoE to keep costs down: a 32-billion-parameter model that activates only 9 billion at a time. For enterprises, this means powerful AI without the astronomical bills. 

In Post #4, we’ll unpack how Granite 4.0 works, why IBM built it this way, and what it means for the future of business AI. 

## _**Why This Matters: Beyond Benchmarks and Buzzwords**_ 

In my opinion these three trends are not abstractions or academic curiosities. They represent a practical, human-centered shift in AI design. 

- Speed means real-time help in education, healthcare, and customer service. 

- Efficiency means lower energy use, smaller carbon footprints, and AI that runs on your phone — not just in a data center. 

- Task-specific design means fewer hallucinations, more reliability, and models that understand _what you’re trying to do_ , not just what words come next. 

Most importantly, this shift is making artificial intelligence easy to access for everyone. Open-source projects like dLLM are making cutting-edge research accessible to students, startups, and independent developers. Google and IBM are releasing models with open weights. 

Innovation is no longer locked behind corporate walls. 

## _**The Frankenstein Metaphor Revisited**_ 

Mary Shelley’s _Frankenstein_ was not a tale of evil science — it was a warning about abandonment. The creature wasn’t monstrous because it was assembled; it became dangerous because its creator rejected it. 

Today’s AI “creatures” are also assembled, stitched together from diffusion, encoders, decoders, Mamba layers, and expert modules. 

_Open in app_ 

But this time, the creators are not walking away. They’re building with intention, transparency, and collaboration. And maybe, even if these new hybrids are nothing more than a step toward another innovative architecture, the efforts to gift the world community is real. 

The real monster would be to cling to a single, outdated architecture just because it’s familiar. The future belongs to those willing to experiment, to combine, to adapt. 

AI Frankenstein is alive 

And this is not as a warning, but a promise. 

## _**What’s Next**_ 

In the next article (part #2), we’ll step into the studio of the AI sculptor. We’ll explore how diffusion language models turn noise into meaning, spotlight pioneering open-source projects like LLaDA and ModernBERT-large-chatv0, and examine Google’s groundbreaking Gemini Diffusion. You’ll see how this new paradigm doesn’t just write faster, it really _thinks_ differently. 

