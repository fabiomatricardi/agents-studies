# The Bill Is Coming Due: The Hidden Crisis Behind Your AI Subscription

## A story I couldn't ignore

Last month, I got a call from a friend who's a CFO at a mid-size SaaS company. He's been on a cost-cutting tear since Q3, having "AI-optimized" his engineering team down from 50 to 32 people. The board loved it. The stock popped 8% on the "efficiency gains."

But something was eating at him.

"I pulled the actual bills," he told me, voice tight. "We're spending $180K/month on Claude and ChatGPT licenses now. That's up from $40K in January. And that's not even counting what we're spending on Cursor, GitHub Copilot, and the weird shadow IT stuff people are running on their personal cards."

I asked him about the headcount savings. "We let 18 people go. Average fully-loaded cost was probably $180K each. So... $3.2M in annual savings. But the AI bill alone is $2.1M now, and it's growing 15% month-over-month."

He paused. "Where did the savings go?"

That's the question. That's what I've been trying to answer for three months now, pulling at threads that keep leading to the same uncomfortable place:

**The entire premise of "cheap AI" is a mirage.** A full-blown financial structure that would make Enron blush.

And the worst part? The receipts are public. Anyone can look. The reason no one does is because the truth is so obvious it's almost embarrassing to point out.

## I. The "Cheap Token" Era Is a Subsidy, Not a Technology

You know that warm feeling you get when you use ChatGPT or Claude? That sense that something magical landed in your lap—for less than the cost of a Netflix subscription?

That's venture capital with a marketing budget.

Here's the math that kept me up at night:

OpenAI did roughly **$13 billion in revenue in 2025** and spent about **$22 billion** to do it. Net loss: **$9 billion.** By September 2025, the company had paid Microsoft **$8.67 billion** just for inference compute on Azure. By November, the leaked figure was **$12 billion.**

Let me say that again, slowly: the biggest, most successful, most valuable AI company on earth is paying more for the GPUs to answer your prompt than it is charging you for the prompt.

Not for training. For *answering*. The thing that's supposed to be the easy, profitable, scale-it-out part.

That's the bleeding wound.

But wait, it gets worse. Let's break down what that $12 billion actually represents. Every time you send a prompt to ChatGPT, here's what happens on the backend: the model loads your context into attention mechanisms that scale quadratically with token count (O(n²) complexity, for the techies). Then it runs through multiple layers of neural network processing. Then it generates tokens one by one, each requiring the same full pass.

This is why we talk about "tokens per second" as the metric that actually matters. Not the price per million tokens. The price per completed task.

Anthropic's story rhymes. Revenue hit about $14B by February 2026, up from $1B annualized in late 2024. Beautiful, right? But. Gross margin printed **~40% for 2025**, after the company quietly walked back its own 50% target because inference costs landed **23% over plan**.

The company now plans roughly **$19B in 2026 spend** (training plus inference) against an annualized revenue base that, if growth pauses, doesn't cover it.

Here's what I think most people miss: the "inference" part is supposed to be the good part. Training is the expensive, one-time cost where you throw billions at GPU clusters for weeks. Inference is supposed to be the cash register—low marginal cost, high margins, infinite scale.

But it's not working out that way.

### The price-per-token lie

So when you see headlines like "AI inference costs have fallen 280x in two years"—here's what's actually happening:

**Per-token prices fell. Per-task token consumption *exploded*.**

A 2023-era chat completion took maybe 800 tokens round-trip. You typed a question, you got an answer. Simple.

A 2026-era agentic workflow takes 10 to 20 LLM calls, each with reasoning chains, tool calls, retrieved context, and re-prompts. You're not just chatting anymore—you're orchestrating.

Let me give you a real example from my own work. I use Claude Code to help write these articles. A simple article might involve 50-100 tool calls—reading files, searching for context, writing drafts, editing sections. Each of those tool calls involves LLM inference.

A single Claude Code session that closes a real production bug burns **five-figure token counts.** Not five figures in the output. Five figures in tokens processed—input plus output, plus thinking tokens, plus context.

A three-agent team configuration—you know, the trendy "multi-agent" setup everyone's bragging about—uses **7x the tokens** of a single agent. Because they're coordinating, sharing context, debating with each other.

The unit got cheaper. The unit count went vertical.

**Net result: enterprise AI spend rose 320%** over the same window where token prices fell 280x.

Let me say that again: prices fell 280x, spending rose 320%. Cost migration with better PR.

Inference now eats **85% of the enterprise AI budget.** Substitution scaling faster than efficiency—which is the textbook recipe for Jevons-paradox cost explosion. (That's when making something more efficient leads to *more* consumption, not less. Like how more fuel-efficient cars led to more driving, not less.)

### The tokenizer trick

But here's the part that really got me: even the "price per token" numbers are being manipulated.

Remember when Anthropic released Opus 4.7 and everyone celebrated the "same pricing"? What they didn't mention was that Opus 4.7 has an **up to 35% increase in token count** simply because they changed the tokenizer.

Wait, what's a tokenizer? Here's the simplified version: before your text goes into the AI model, it gets chopped up into "tokens"—the basic units the model understands. Different models use different tokenization methods. Some are efficient, some are wasteful.

Anthropic switched to a new tokenizer in 4.7, and the same text now produces 35% more tokens. Same price per million tokens. Same model. But your bill goes up 35%.

They mentioned it. Buried in the release notes. The analysis from Ramp and OpenRouter showed the actual cost increase: **12-27% more** for the "same" model at the "same" prices.

This is like a restaurant switching to smaller portions and charging the same price, then being surprised when customers notice they're still hungry.

## II. The Daisy Chain: How Investors, Hyperscalers, and AI Labs Circulate Money

Here's the part that makes my skin crawl.

The "venture capital" and "strategic investment" funding the cheap-token era are often the *same companies* selling the GPUs. Or running the cloud. Or buying the API. Sometimes all three.

The money isn't moving through the system. It's circulating *inside* the system.

Let me trace one thread:

**Microsoft committed $13 billion to OpenAI.** Most of the training spend was Azure credits, non-cash. Microsoft "invests" $13B; OpenAI "spends" most of it back on Azure; Microsoft books the burn as cloud revenue; the cloud-revenue chart goes up; the stock goes up; the next round gets justified.

Then OpenAI signed an incremental **$250 billion in Azure contracts**, plus a 20% revenue share to Microsoft. Microsoft kicks ~20% back from Bing and Azure OpenAI Service.

Around and around.

**Amazon and Google have committed $13B in Anthropic.** Then announced up to $25B more, in exchange for Anthropic's pledge of more than **$100B in AWS spend over a decade** and a Trainium-only path through Trainium 4 across up to 5 gigawatts of capacity.

Read that as: cash now, locked-in compute revenue forever, vendor lock to Amazon's chips, and a story that lifts AWS's AI narrative. Anthropic is independent, but also a long-tenor revenue annuity for Amazon.

**Nvidia owns or has invested in CoreWeave, OpenAI, xAI, Wayve, Mistral, and a parade of others.** Nvidia's investees turn around and buy Nvidia GPUs.

OpenAI's $122B "funding round" at $852B post-money? Roughly $37B is what anyone would honestly call clean venture capital with no vendor relationship. The rest is Amazon buying a customer, Nvidia buying a buyer, and SoftBank tranching $30B to a vendor whose technology SoftBank is also distributing through its own portfolio.

That's a **daisy chain.**

### The "we fired humans, still bill is the same" moment

In April 2026, Bryan Catanzaro, an Nvidia VP, told Axios on the record: "For my team, the cost of compute is far beyond the costs of the employees."

Let me translate: their GPU bill is bigger than their payroll.

Jensen Huang spent the GTC 2026 keynote pitching the idea of paying employees in AI tokens *on top* of salary, because the tokens-per-engineer line item is now bigger than the headcount line item for some teams.

Think about that for a second. The CEO of Nvidia—the company selling the GPUs—is literally suggesting that employees should be compensated in tokens instead of cash. Not because tokens are valuable, but because the *compute* that generates the tokens costs more than the *people* using them.

A levels.fyi survey put a top-quartile US software engineer at $375K base, plus another $100K in token consumption at full-load AI tooling: **$475K loaded.** About 20% of the cost of an engineer is now compute.

We didn't replace the human. We **rebadged the cost.** The line item that used to say "salary, $200K" now says "salary, $150K + Anthropic invoice, $80K + Cursor seat, $4K + token overage, $30K."

The total didn't drop. It just stopped going to a person and started going to a hyperscaler.

The W-2 became an AWS invoice.

Here's what I want you to take away from this section: the reason AI seems "cheap" isn't because it's efficient. It's because someone else is absorbing the difference. When that stops, the real prices emerge.

## III. The Sora Tell: When Products Get Killed Because They're Too Expensive

The first crack in the facade was in the product, not the API pricing.

OpenAI shut down or aggressively throttled free access to Sora video in multiple regions. The reason wasn't "safety." The reason wasn't "research."

The reason was the per-generation cost, on a frontier video model with long sampling chains and giant context, was so far above any plausible price the user would pay that the only solution was: **stop letting users use it.**

Let me put some numbers on this. Generating one minute of Sora-quality video requires thousands of inference steps, each processing frames in parallel through the model. The compute cost per minute is estimated somewhere between **$1-3** at current API pricing—which is way more than anyone would ever pay. Even at $0.10/minute, nobody's using it enough to move the revenue needle.

When the math breaks badly enough on a single product, you don't fix the math. You hide the product.

**Sora's shutdown is the canary.**

### The real price gap

And it's not just Sora. Look at the API pricing from the other direction: Claude Opus 4.6 lists at $5 per million input tokens and $25 per million output tokens. Sounds reasonable.

Until you stack it next to this:

A B200 GPU running an open source 120B model can hit ~$0.02 per million tokens at decent batch utilization. That's the theoretical number under ideal conditions.

Now add reality: giant context window and reasoning chains, at low batch sizes, with KV cache pressure, with tail latency targets, with safety classifiers, with retrieval, with tool calls?

**The cost-per-million can balloon by 50x to 100x.**

Frontier inference is not the same animal as commodity inference.

Let me make this concrete. You might think "well, I'll just use the cheap model." But here's what happens in practice:

OpenAI's latest models have what's called "thinking tokens" or "reasoning tokens" where the model does internal computation before outputting. That reasoning process generates tokens you're paying for—but you never see them. They're invisible. They can be 10x or 20x the visible output tokens.

So when you think you're paying for 500 tokens of output, you're actually paying for 10,000 tokens of invisible reasoning. The model is "thinking" before it answers.

Most people have no idea this is happening.

What we end up seeing today is the subsidized cost. It's the cost of generating a token *minus what the investor is willing to eat* to keep you using the product.

The difference is the subsidy.

And the subsidy has a name. Several names, actually.

### The China comparison nobody's making

Here's something that keeps me up at night: China just told its tech sector that AI productivity comes with a labor bill the company has to pay. A court in Hangzhou ruled that you can't fire a worker just because the model got cheaper—the company has to either find them comparable work, or pay meaningfully to part ways.

The US response? The Senate is asking nicely for companies to *report* AI layoffs.

Reporting. Not stopping.

We're subsidizing the destruction of jobs through below-cost compute, while China is mandating that companies actually pay for the transition. That's not a technology gap—that's a values gap.

## IV. What Happens When the Subsidy Ends

Three things can break the loop. Any one of them is enough to trigger a repricing.

**1. A bad funding round.**

OpenAI raises $122B at $852B. Great headline. But the structure is heavy on contingent capital, vendor commitments, and milestone-gated tranches. If a tranche slips because OpenAI misses a target, or if a hyperscaler renegotiates because cloud demand softens, the daisy chain breaks at one link—which means the loop breaks at all links.

Each company in the chain priced itself off the assumption that the next link would honor its commitment.

Here's what happens in that scenario: Microsoft has $13B of "invested" capital that's really Azure credits. If OpenAI misses a milestone, those credits stop flowing. Microsoft's AI revenue drops. Their stock drops. The next funding round gets harder. The whole house of cards wobbles.

**2. A cooling enterprise market.**

Most enterprise AI deployments today are pilots. A McKinsey-flavored slide deck and three engineers in a corner. That's the reality behind the "AI transformation" headlines.

If a serious recession lands—and the odds are higher than people think—CFOs cut "experimental AI line items" by 30%. Inference revenue falls before inference cost does (because compute is a take-or-pay contract—you've reserved the GPUs regardless of whether you use them).

Margins go from "bad" to "terminal" overnight.

Think about what happened to cloud spending in 2022-2023. Same pattern: companies overbought capacity in 2021, then "rightsized" in 2022. The hyperscalers survived, but barely. AI doesn't have that buffer.

**3. A regulatory whack (least likely but who knows).**

Antitrust eyes are already on the circular deals. The FTC, SEC, and EU competition authorities have begun asking pointed questions about whether vendor-equity-for-compute arrangements constitute revenue inflation.

If a regulator forces hyperscalers to mark Azure-credit "investments" as deferred revenue rather than partner equity, the entire revenue line on Microsoft's AI segment gets restated. So does the valuation it supports.

This is the "black swan" scenario, but it's less unlikely than people think. The EU has already fined Google $2.7B for shopping comparison bias. The FTC has been hunting bigger game. And the circular financing between OpenAI/Microsoft, Anthropic/Amazon, and Nvidia/its investees is so obviously problematic that regulators would love to make an example of it.

### Pick any one of these

The price reset comes within **twelve to twenty-four months.**

Industry analysts already estimate API prices need to rise **3–10x** to reach genuine sustainability for frontier serving, with frontier and commodity tiers bifurcating sharply.

What does that look like in practice?

**Open-source distillations stay cheap.** Models like Qwen, DeepSeek, and the Llama family will continue getting better and cheaper. You'll be able to run solid models locally for most tasks.

**The smart frontier models**—the ones that actually do reasoning and long-horizon planning and reliable code generation—**become expensive.** Not because they're trying to gouge you, but because the actual compute cost is that high.

### What Real Tokenomics Looks Like

If, *if*, the industry survives the upcoming subsidy reset, here's what the math forces.

Frontier model inference at full cost lands roughly at the marginal cost of an experienced human doing the same task for the same duration. For a senior engineer task that takes 30 minutes of human time, the equivalent agentic run that delivers comparable reliability runs maybe 200K-400K input tokens and 50K-150K output tokens at realistic context utilization, across 10–20 LLM calls, on a frontier reasoning model.

At unsubsidized prices (3–10x of today), that's **$20-$80 of compute.** Not $0.50.

A 30-minute senior engineer task at full loaded cost is, depending on geography, **$50-$120 of human time.**

**Half the price. Most of the capability. None of the agency.** That's the real value proposition, once the subsidies clear. It is a deal. It is not a revolution.

Here's what I'm trying to tell you: even at 3-10x pricing, AI is still valuable. But it's not the "free money" that the press releases implied. It's a productivity tool with real costs and real tradeoffs.

### It gets worse for the lower tiers

Customer support agents, content moderation, data entry, basic legal review, bookkeeping, transcription—the jobs the industry actually fired people from—were already low-cost-per-hour roles, often offshored.

The unsubsidized AI inference cost to do them with reliability comparable to a trained human runs uncomfortably close to the human's hourly cost in low-COL countries.

Think about it this way: a Filipino customer support agent costs maybe $5/hour fully loaded. For AI to reliably do their job, you're looking at $3-4/hour in compute costs at unsubsidized pricing. That's not a 90% savings. That's a 20-40% savings—with zero loyalty, zero judgment calls, and zero ability to handle novel situations.

The "AI is 90% cheaper" headline is real today only because someone else is eating most of the actual compute bill.

When that someone else stops eating it, the savings collapse.

The jobs are still gone. The tools cost almost what the labor did. The corporate margin gain that justified the layoffs evaporates.

We fired people to discover we needed fewer people who cost the same.

We just built a funnel to divert money from people to corporations for 50% or less savings while taking a huge legal, societal, emotional risk.

This is what keeps me up at night. Not the technology—it's the human cost dressed up as efficiency.

## V. Your Move

Three predictions. Take or leave.

**A reset, not a crash.**

The labs and the hyperscalers are both incentivized to manage the subsidy reset, not detonate it. They want higher prices—just not all at once. Expect API prices to climb **30–50% per year** for the next two years on frontier tiers, while open-source and small-model APIs hold roughly flat or fall.

The bifurcation gets sharper. The midwit pricing tier disappears—you either go frontier (expensive but capable) or commodity (cheap but limited). The middle ground that let companies pretend they were doing serious AI without spending real money? Gone.

**One blowup, then consolidation.**

Somewhere in the next 18 months, one of the second-tier labs (not OpenAI, not Anthropic, not Google) misses a payment, fails a tranche, or gets caught in a circular-financing audit. Mistral, Cohere, AI21, xAI—watch any of these.

The market re-rates the entire sector by **30–50%** for a quarter.

The cleanup leaves three or four serious frontier labs and a long tail of distillation shops. (Distillation is the process of taking a big, expensive model and training a smaller one to mimic it. It's how we get "almost frontier" performance at commodity prices.)

**"Tokens per engineer" becomes a budget line.**

By end of 2027, every engineering org tracks tokens-per-engineer as a budget metric, the way they currently track AWS-spend-per-engineer. CFOs will demand caps. Engineering managers will write justification docs for token overages.

Your CTO will ask: "Why did we spend $40K on Claude last month when we're only a 10-person team?" And someone will have to answer.

The "use as much AI as you want" era ends quietly, replaced by "use as much AI as you can justify in the post-mortem."

### Here's what I think you should do

**If you're a knowledge worker:** don't assume your job is safe because AI is "cheaper." The math is revealing itself. The companies that fired you to save money are about to discover the replacement costs almost as much.

More importantly, realize that your leverage is changing. If AI costs are going up, the companies that over-indexed on AI headcount reduction are going to find themselves in a weird spot—they reduced costs but didn't actually solve the problem. You're not replaceable. You're just temporarily unfashionable.

**If you're a developer:** start learning the open-source stack. Ollama, llama.cpp, LM Studio, local models. The future of "cheap AI" is going to look a lot more like "your AI" running on your machine than "rented AI" running on someone else's cluster.

The skills that matter now are: running models locally, fine-tuning on your own data, building the infrastructure to host your own inference. These are "poor GPU guy" skills—the same skills I've been writing about for years. The world is catching up to why they matter.

**If you're a founder or executive:** re-read the numbers. The savings from AI-driven headcount reduction are already evaporating. The ones who survive will be the ones who planned for the repricing, not the ones who celebrated the press release.

Your move: build real budgets. Track actual costs. And stop pretending that the current pricing is sustainable.

### One more thing

I want to be clear about something: I'm not anti-AI. I've built my entire career on the "poor GPU guy" premise—that you can do meaningful work with limited resources. I'm using AI to write this article right now. I think it's a generational technology.

But I think it's a generational technology *with real economics*, not a magic trick that makes math stop applying.

The difference matters. A technology with real economics can be built on. A magic trick can only be speculated on.

Tokenomics, the *idea* that LLM tokens are a new asset class with their own coherent economics, was always a marketing term dressed up as a thesis. The analysts and investors who built models on "falling costs forever" were building on sand.

The actual economics are the same as every other compute-heavy SaaS business in history: margins compress, pricing power matters, unit economics rule.

There is no magic.

Only a few companies like Apple are playing it without risking the future—because they've been through this before with the iPhone App Store, with iCloud, with everything else. They know that sustainable businesses require sustainable margins.

The bill is coming due. The receipts are public.

Don't say nobody told you when the price hike notice lands in your inbox.

---

**TL;DR:** The "cheap AI" era is funded by a circular financing daisy chain between investors, hyperscalers, and AI labs. Per-task costs are rising even as per-token prices fall. When the subsidy ends (12-24 months), expect 3-10x price increases on frontier models. Start preparing now: learn local AI, budget for token costs, and don't assume your job is safe just because the press release said AI was cheaper.

---

**Your Turn:** What's your AI bill looking like? Run the numbers on your actual usage—input tokens, output tokens, and number of calls per task. You might find you're already paying more than you think. Drop a comment and let's compare notes.