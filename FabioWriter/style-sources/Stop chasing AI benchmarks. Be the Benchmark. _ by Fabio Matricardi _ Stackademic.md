## _**Stop chasing AI benchmarks. Be the Benchmark.**_ 

_In a world of endless AI releases and shiny leaderboards, the smartest strategy is simple: treat benchmarks as signals, and make yourself the final judge._ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 9 min read · Jan 15, 2026_ 

**==> picture [511 x 267] intentionally omitted <==**

_Photo by Mark Owen Wilkinson Hughes on Unsplash_ 

I believe you have noticed this too. There is no new week without a new model release in the Generative AI community. 

While this is exciting, and showing how much attention and focus is given to the AI innovations, it is also disturbing. Is really this new State Of The Art (or claimed so) model the real breakthrough? Is it going to change the way we live and work for good? 

The reality is different. 

## _**They are all the same, sort of…**_ 

Most new AI models feel incremental, overhyped, and largely interchangeable in day­to­day use, so it is no longer worth tracking every release (unless you are a geek like me). 

New LLMs, multimodal models, and copilots now arrive in a _release flood_ , too fast for anyone to read, test, and reflect on each one meaningfully. 

_And I will give you my practical feedback shortly…_ 

Many releases are marketed as revolutionary but are in fact small tweaks, like 1.1–2.3% benchmark gains or slightly better data or context length. 

For developers using APIs or chatbots, the experience of different modern LLMs often feels the same, with only minor stylistic differences between models. 

If you never tried it, I mean to run flagship models through API, you can use for free OpenRouter (as of today there are 32 top notch free models you can use), as I explained here: 

## _**30 ways to build a prototype AI app with no budget**_ 

_Learn how you can have free API calls at not costs and create powerful app with top-notch Generative AI models._ 

_generativeai.pub_ 

**==> picture [121 x 126] intentionally omitted <==**

When you start using those Big models (and somehow for Small Language Models there is a real gap) you realize that the real impact is small while the headlines are dramatic, the gap between perceived and actual change keeps growing. 

_few of the Big shots models you can use for free on OpenRouter.ai_ 

Early breakthroughs like ChatGPT, Palm or T5 felt genuinely surprising, but new models that are “10% better at reasoning” or “2x faster” do not create the same excitement anymore. 

Constant small updates turn reading model news into routine content consumption rather than true learning or discovery. 

## _So what is left, worth your time?_ 

## _Photo by_ Антон Дмитриев _on Unsplash_ 

## _**The AI good for you**_ 

I don’t know what you use AI for. But it is almost certain you don’t need a 400­billion­parameter model to get it done. 

Swayed by hype cycles and glossy leaderboard screenshots, many people keep jumping from one “SOTA” model to the next without ever asking the only question that matters: did this actually make my work better? Benchmarks are particularly dangerous here, because they look objective while often encoding someone else’s priorities, someone else’s data, and even someone else’s AI as the judge. 

_As shown in recent human­centered evaluations of LLMs, there is a consistent mismatch between benchmark metrics and real­world use, especially for everyday_ - _writing and review tasks. —_ Evaluating LLM Metrics Through Real World Capabilities ( _arXiv:2505.08253v1)_ 

Most of these tests score how well a model performs on a narrow, artificial task under lab conditions, not how it behaves inside your messy inbox, your codebase, your documents, or your creative process. They rarely measure the things you really care about: fewer mistakes in client emails, faster research for your thesis, less time wrestling with spreadsheets, or more consistent tone in your writing. 

_Industry analysis shows that leaderboard­optimized models often generalize poorly, because they are tuned to narrow tasks rather than the complex scenarios_ 

That is why, at the end of the day, the only benchmark that is both honest and useful is you. Your tasks, your constraints, your risk tolerance, and your sense of “this is good enough” are the real evaluation suite every model has to pass. 

You must be the benchmark because no global leaderboard, model card, or glossy metric knows what actually matters in your real work and life. 

## _**The trap of external metrics**_ 

Benchmarks are useful, but they are blunt instruments. They compress rich, messy performance into a single number that often hides where a tool shines or fails for you specifically. 

They are usually designed around what is easy to test at scale, not what is meaningful for your daily decisions, workflows, or creativity. 

Recent work on LLM evaluation shows that public benchmarks systematically miss many of the tasks people actually use AI for and underweight criteria like clarity, relevance, and efficiency. 

Combined with evidence that leaderboard­optimized models often generalize poorly to messy real world scenarios, this strongly suggests that only user­defined, task based evaluation can reliably tell whether an AI work better. model truly makes _your_ 

I strongly suggest to run your own tests. 

And If you don’t know where or how to start, here is my 2 cents. 

_one of my personal Benchmarks — from source_ 

## _**The ultimate AI Benchmark: You**_ 

Fifteen months ago I started on Medium a series of articles I am really proud of. I called them RBYF — Revised Benchmark with You as a Feedback. 

## _**RBYF: Qwen2.5–3B-instruct is damn good.**_ 

_Revised Benchmark with You as a Feedback: the brand new 3B model from Alibaba Qwen is an amazing model, and I can prove… ai.gopubby.com_ 

**==> picture [121 x 126] intentionally omitted <==**

The project started because I needed it: I don’t have a powerful computer, and I don’t have a dedicated GPU. So I had (and still have) to pick a Small Language Model carefully, knowing what it could do for me (speed and accuracy). 

## _**GitHub - fabiomatricardi/YouAreTheBenchmark: Personal Catalog of prompt templates for NLP tasks**_ 

_Personal Catalog of prompt templates for NLP tasks - fabiomatricardi/YouAreTheBenchmark_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

In my GitHub repository, I report my personal test performed over 20 Small Language Models. This repo is a Python-based toolkit for evaluating and organizing LLM prompt templates across many small/medium open models, with human-in-the-loop quality scoring. 

- It serves as a personal catalog of prompt templates for a broad range of NLP tasks, meant for manual and semi-automated benchmarking of local models. 

- The core idea is “You Are The Benchmark”: a script runs prompts through a model, while the human rates generations using a qualitative 0–5 scale. 

I decided the tasks (or if you prefer the LLM skills) and I am using a qualitative matrix to evaluate the output. This app goes through one prompt for each task: at the end of each generation, the user can score the result from 0 to 5 and leave a comment. 

_here my score table from Qwen2.5–3b-instruct_ 

At the core, the idea is simple: 

## _“Better on average” does not mean “better for you.”_ 

A model that tops leaderboards can still hallucinate on your niche domain, struggle with your language mix, or break your existing stack. 

A carefully selected Small Language Model might integrate cleanly with your data, match your risk tolerance, and fit your budget, making it the real upgrade in your daily routine work or hobby. 

_Your constraints, habits, and goals redefine what “state of the art” actually looks like._ 

## _**Designing your own benchmark**_ 

To become the benchmark, turn your real use into a test suite. 

Decide the tasks or skills you usually need: if your normal use of Generative AI is for summarization, open Q&A or learning, you don’t need even more than 8 Billion parameter model. 

_here the main tasks (skills) I want to test on Small Language Models_ 

Track a few concrete outcomes: time saved on a task, error rate on real documents, number of revisions needed, user satisfaction on your team (if you have one…). 

Run small, honest experiments: same task, different tools, same constraints, and then record what felt reliable and understandable… to you! 

And set your score system: here is mine, just to give you an example: 

```
Qualitative Matrix to be applied by the Human (YOU)
```

```
1 - Bad generation quality
   - User intent not considered
   - output format not good
   - made up information.
2 - Sufficient generation quality
   - User intent considered
   - output format not good
   - barely coherent.
3 - Acceptable generation quality.
   - Instruction followed with some mistakes
   - output format not fully compliant
   - reply content acceptable
4 - Average generation quality
   - Instruction followed
   - output format acceptable, min mistakes
   - reply content accurate
5 - Perfect generation quality.
   - Instruction followed
   - output format compliant
   - reply content accurate
```

_If a tool scores high on paper but low in your logs, your metric wins._ 

Emergent abilities and tiny leaderboard gains often create the illusion of sudden leaps: this is what you usually get from the weekly announcements in the AI community. 

In reality, many of these jumps come from how we define and score tasks, not from magical new intelligence. 

When you anchor on your own metrics, you stop chasing hype spikes and start noticing steady, compounding improvements that actually matter to you! 

You move from “What does the benchmark say?” to “Did this make my real work better?” 

Don’t get me wrong: we need a baseline, a common ground to evaluate the performance of Generative AI models. Being the benchmark does not mean to ignore the public metrics; it means to put them in their place. 

Use public benchmarks as a filter, not a verdict: they tell you what to try, not what to trust. Let your experience, data, and discomfort speak loudly: if something feels off, that is a signal your metric is missing from the public ones. 

## _**Conclusions**_ 

Meaningful progress often happens quietly in areas like data pipelines, evaluation, inference optimization, and reliability, rather than in flashy model announcements. 

If you like following the news… probably it’s better to ignore most new model updates and instead track long­term trends and a few trusted signals, aiming for fewer but deeper insights. 

And these are mostly in the ArXiv papers! 

For example, since I am an active user in HuggingFace, I also subscribed to receive the Daily Paper Digest. 

Research papers are the foundation studies for the future of LLM and Generative AI. And Artificial Intelligence is not limited to Generative AI, by the wa … _Open in app_ y 

If there is one habit worth keeping in this release flood, it is to treat public benchmarks as signals, not as orders. They can point you toward promising tools, but only your own tasks, constraints, and annoyances can tell you whether something is actually an upgrade. 

Designing and running your personal benchmark turns AI from a spectacle you watch into an instrument you tune: you stop chasing marginal leaderboard gains and start tracking whether your emails get clearer, your code breaks less, and your learning gets faster. In that sense, “state of the art” stops being a number on a leaderboard and becomes the quiet moment when a model reliably makes your real life easier. 

So follow the papers, skim the leaderboards, enjoy the announcements if you like them — but never outsource your judgment to them. 

You are the one doing the work, so you must be the benchmark. 

_Your AI, Your Rules!_ 

_Metrics And Analytics_ 

