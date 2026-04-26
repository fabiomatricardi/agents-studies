Published July 30, 2025 

**==> picture [24 x 24] intentionally omitted <==**

Written by **Grant Harvey** 

**The tiny Hierarchical Reasoning Model mimics the brain’s structure to solve complex tasks in a single pass — no internet-scale pretraining, just smart design and strategic thinking.** 

**==> picture [253 x 142] intentionally omitted <==**

Image: Adobe/Limitless Visions 

A new AI model from Singapore-based Sapient Intelligence is challenging the “bigger is better” mantra dominating today’s AI model development, and it’s doing it by copying a trick from the human brain or, at least, how we think the brain works. 

Meet the Hierarchical Reasoning Model (HRM), a tiny 27M-parameter design that solves complex reasoning puzzles that leave today’s massive AI models completely stumped. 

The problem with models like ChatGPT, according to the researchers, is that they’re architecturally “shallow.” They rely on Chain-of-Thought (CoT) prompting — basically, talking themselves through a problem step-by-step — as a crutch. But with CoT, one wrong turn can derail the whole process. HRM takes a different approach. 

## **How HRM works like your brain** 

HRM copies the brain’s hierarchical structure with two interconnected modules: 

- A **high-level “planner”** that thinks slowly and strategically like when you plan your next chess move. 

- A **low-level “worker”** that executes rapid calculations like when you instantly recognize a face. 

Think of it like having a brilliant manager directing a lightning-fast assistant. This structure allows HRM to “think” deeply about a problem in a single forward pass, learning to reason from just a handful of examples without pre-training on the entire internet. 

## **The results are jaw-dropping** 

On the ARC-AGI benchmark, which is basically an IQ test for AI, HRM went head-to-head with top-tier models and dominated. 

**o3-mini-high (OpenAI):** 34.5% 

**HRM (27M parameters):** 40.3% 

On Sudoku-Extreme puzzles, HRM solved 55% of them. Claude 3.7 and OpenAI’s o3-mini-high? They scored 0%. On 30×30 mazes, HRM found the optimal path 74.5% of the time. The others? 0% again. 

Now, we realize Claude 3.7 and o3-mini-high models are not the frontier, frontier models, but HRM is also tiny in comparison. Do you see where this is going? GPT-1, the O.G. GPT model, had 117 million parameters… that’s four times more than HRM. 

In fact, HRM’s design is so lean that one of its creators, Guan Wang, said it can be trained to solve pro-level Sudoku in just two GPU hours. 

## **Why this matters** 

HRM proves that architecture matters more than size. The implications are massive: 

- **Cheaper AI deployment** — better AI that runs on a single GPU. 

- **Faster training** — hours instead of months. 

- **Better reasoning** without expensive compute. 

- **Open-source.** You can grab the code here and train your own! 

While skeptics argue HRM’s skills are too narrow, its early-stage performance suggests that brain-inspired designs could unlock powerful reasoning at a fraction of the cost. 

And this is just one idea like this. There’s also Sakana’s continuous thought machines method (GitHub), 1-bit LLM “bitnets” (GitHub), and even diffusion models, which Google is experimenting with. 

At their current stages, all of these architectures are impressive in theory but still need to be scaled out of the “shiny object syndrome” zone where they live today. 

But TBH, unless an incredibly well-funded competitor flies out of stealth with untold billies, the next “holy stinking wow” AI model from someone outside of the major players (US or Chinese) will probably be built on some new architecture like this. 

This could be a glimpse into a future where advanced AI isn’t confined to massive data centers but finally runs efficiently on a local machine. 

**Editor’s note:** This content originally ran in our sister publication, The Neuron. To read more from The Neuron, sign up for its newsletter here. 

