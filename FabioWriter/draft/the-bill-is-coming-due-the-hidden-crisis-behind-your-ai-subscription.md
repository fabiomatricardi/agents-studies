# The Bill is coming due: the not-so-well-hidden crisis behind AI Subscriptions... even yours!
## Thinking tokens and invisible invoices and the great reset: preparing for the 10x price jump



Last month, I sat down with our operations lead to review our overhead. We are a lean shop, just 20 people, so every line item usually has a face and a name attached to it. Lately, however, the names have been replaced by API calls.

We have 10 developers using Claude Code to speed up shipping on our Process Control Automation projects. On paper, it is a dream; in the high-stakes world of Oil & Gas, it feels like we have doubled our output on complex logic and safety protocols without hiring a single new person. But when the bill for the last 30 days hit, the efficiency felt a lot more expensive than the marketing suggested.

"I pulled the actuals," she told me, pointing to a spike that started 3 months ago. "Our Anthropic and OpenAI bill is approaching the cost of a full-time junior engineer".

The math I have been running for three months now keeps leading to the same uncomfortable place:

**The entire premise of cheap AI is a mirage.** We think we are saving money by keeping our headcount at 20, but we are actually just rebadging our payroll budget and sending it to a hyperscaler.

And the worst part? The receipts are public. The reason no one notices is because the truth is so obvious it is almost embarrassing to point out.



## I. The Cheap Token Era: A Subsidy, Not a Technology

You know that feeling of getting a powerful automation tool for less than a Netflix subscription? That is not a technological breakthrough. It is a venture capital marketing budget.

The math is jarring: OpenAI reportedly spent $22 billion in 2025 to make $13 billion in revenue. They lost $9 billion because the cost to run the GPUs (inference) was higher than what they charged us to use them.

In our world of Process Control, we understand margins. If you are selling a solution for $100 that costs you $150 to maintain, you are not a tech genius. You are just subsidized. Right now, Microsoft and Amazon are essentially paying part of our AI bill to keep us locked into their ecosystems.

### The price-per-token lie

The headlines say AI is getting cheaper because price per token is falling. But in a real-world engineering workflow, that is a distraction.

In 2023, you might have asked an AI a simple question. Today, we are using Claude Code to orchestrate entire automation workflows. A single session to debug a PLC logic error or map out a refinery's sensor network does not use one call. It uses 20. It is checking files, searching documentation, and thinking through safety protocols.

The unit price fell, but our consumption went vertical. This is the Jevons Paradox: as the tool gets more efficient, we use it so much more that our total spend actually explodes. In fact, enterprise AI spend has risen 320% even as token prices dropped.

### The tokenizer trick

Even the falling prices are not always what they seem. Anthropic recently released a model update (Opus 4.7) and kept the price per million tokens the same. But they quietly changed the tokenizer, the way the AI chops up your text into units it can process.

The result? The exact same piece of code now costs up to 35% more tokens to process than it did before. It is like a restaurant keeping the price of a burger the same but switching to a smaller bun and thinner patty. You are still hungry, so you buy two. For our team of 10 devs, these invisible changes are what turn a predictable subscription into a runaway invoice.

## II. The Daisy Chain: How Investors, Hyperscalers, and AI Labs Circulate Money

Here is something that keeps me up at night. The venture capital funding our cheap tokens is often just the same companies selling the GPUs, running the cloud, and buying the API. The money is not moving through the economy. It is circulating inside a closed loop.

Microsoft invests billions in OpenAI; OpenAI spends those billions back on Azure credits; Microsoft books that as cloud revenue; the stock goes up. Amazon and Google are doing the same with Anthropic, locking them into decade-long, $100B compute contracts. Even Nvidia is investing in its own customers so they can turn around and buy more H100s.

It is a financial daisy chain. And for a company like ours, focused on real-world physics and industrial safety, this circular economy feels incredibly fragile.

But we thought we would save money. Instead, we just moved the cost from payroll to API invoices.

In our world, an experienced engineer costs a certain amount. We thought AI would drop that cost. But what is actually happening is a cost migration.

The line item on our budget that used to say "Senior Automation Engineer" is being chipped away. But that money is not becoming profit. It is being moved into an invoice for Anthropic, a seat for Cursor, and an overage bill for GitHub. We have not eliminated the expense. We have just started paying AWS instead of a human.



## III. The Sora Tell: When Products Get Killed Because They Are Too Expensive

The crack in the facade appeared when OpenAI started throttling or shutting down access to its Sora video model. It was not about safety. It was about the bill. The compute cost to generate one minute of video was so high that no user would ever pay a sustainable price for it.

When the math breaks that badly, you do not fix the price. You hide the product.

Thinking costs are hidden. For our developers in Process Control, the hidden cost is Reasoning Tokens. New models do not just give you an answer. They think internally first. You do not see that internal dialogue, but you pay for it. You might think you are paying for a 200-word explanation of a PID loop, but the model burned 5,000 tokens thinking about it in the background.

The subsidy is the only reason this feels affordable today. It is the cost of the token minus what the investor is willing to lose to keep us hooked.

### The China comparison nobody is making

Here is something that keeps me up at night: China just told its tech sector that AI productivity comes with a labor bill the company has to pay. A court in Hangzhou ruled that you cannot fire a worker just because the model got cheaper. The company has to either find them comparable work, or pay meaningfully to part ways.

The US response? The Senate is asking nicely for companies to report AI layoffs.

Reporting. Not stopping.

We are subsidizing the destruction of jobs through below-cost compute, while China is mandating that companies actually pay for the transition. That is not a technology gap. That is a values gap.

## IV. What Happens When the Subsidy Ends

Three things will break this loop:

A Bad Funding Round: If OpenAI or Anthropic misses a milestone and a hyperscaler pulls their credits, the house of cards wobbles.

The CFO Crackdown: Eventually, someone in our industry is going to ask why the efficiency of AI has not actually improved the bottom line.

Regulatory Eyes: If the SEC decides these circular investments are actually just revenue manipulation, the party ends overnight.

Analysts estimate that to be sustainable, API prices need to rise 3x to 10x.

When that happens, the mid-tier of AI will vanish. You will either use Open Source (like Llama or DeepSeek) running locally on your own hardware for cheap, or you will pay a massive premium for Frontier Models that can handle complex industrial reasoning.

### The numbers

The price reset comes within twelve to twenty-four months.

Industry analysts already estimate API prices need to rise 3-10x to reach genuine sustainability for frontier serving, with frontier and commodity tiers bifurcating sharply.

What does that look like in practice?

Open-source distillations stay cheap. Models like Qwen, DeepSeek, and the Llama family will continue getting better and cheaper. You will be able to run solid models locally for most tasks.

The smart frontier models, the ones that actually do reasoning and long-horizon planning and reliable code generation, become expensive. Not because they are trying to gouge you, but because the actual compute cost is that high.

### What Real Tokenomics Looks Like

If, if, the industry survives the upcoming subsidy reset, here is what the math forces.

Frontier model inference at full cost lands roughly at the marginal cost of an experienced human doing the same task for the same duration. For a senior engineer task that takes 30 minutes of human time, the equivalent agentic run that delivers comparable reliability runs maybe 200K-400K input tokens and 50K-150K output tokens at realistic context utilization, across 10-20 LLM calls, on a frontier reasoning model.

At unsubsidized prices (3-10x of today), that is $20-$80 of compute. Not $0.50.

A 30-minute senior engineer task at full loaded cost is, depending on geography, $50-$120 of human time.

Half the price. Most of the capability. None of the agency. That is the real value proposition, once the subsidies clear. It is a deal, not a revolution.

Here is what I am trying to tell you: even at 3-10x pricing, AI is still valuable. But it is not the free money that the press releases implied. It is a productivity tool with real costs and real tradeoffs.

### It gets worse for the lower tiers

Customer support agents, content moderation, data entry, basic legal review, bookkeeping, transcription, the jobs the industry actually fired people from, were already low-cost-per-hour roles, often offshored.

The unsubsidized AI inference cost to do them with reliability comparable to a trained human runs uncomfortably close to the human's hourly cost in low-COL countries.

Think about it this way: a Filipino customer support agent costs maybe $5/hour fully loaded. For AI to reliably do their job, you are looking at $3-4/hour in compute costs at unsubsidized pricing. That is not a 90% savings. That is a 20-40% savings, with zero loyalty, zero judgment calls, and zero ability to handle novel situations.

The AI is 90% cheaper headline is real today only because someone else is eating most of the actual compute bill.

When that someone else stops eating it, the savings collapse.

The jobs are still gone. The tools cost almost what the labor did. The corporate margin gain that justified the layoffs evaporates.

We fired people to discover we needed fewer people who cost the same.

We just built a funnel to divert money from people to corporations for 50% or less savings while taking a huge legal, societal, emotional risk.

This is what keeps me up at night. Not the technology. The human cost dressed up as efficiency.

## V. Your Move

Three predictions. Take or leave.

A reset.

The labs and the hyperscalers are both incentivized to manage the subsidy reset, not detonate it. They want higher prices, just not all at once. Expect API prices to climb 30-50% per year for the next two years on frontier tiers, while open-source and small-model APIs hold roughly flat or fall.

The bifurcation gets sharper. The midwit pricing tier disappears. You either go frontier (expensive but capable) or commodity (cheap but limited). The middle ground that let companies pretend they were doing serious AI without spending real money is gone.

One blowup, then consolidation:

Somewhere in the next 18 months, one of the second-tier labs (not OpenAI, not Anthropic, not Google) misses a payment, fails a tranche, or gets caught in a circular-financing audit. Mistral, Cohere, AI21, xAI. Watch any of these.

The market re-rates the entire sector by 30-50% for a quarter.

The cleanup leaves three or four serious frontier labs and a long tail of distillation shops. (Distillation is the process of taking a big, expensive model and training a smaller one to mimic it. It is how we get almost frontier performance at commodity prices.)

Tokens per engineer becomes a budget line.

By end of 2027, every engineering org tracks tokens-per-engineer as a budget metric, the way they currently track AWS-spend-per-engineer. CFOs will demand caps. Engineering managers will write justification docs for token overages.

Your CTO will ask: "Why did we spend $40K on Claude last month when we are only a 10-person team?" And someone will have to answer.

The use as much AI as you want era ends quietly, replaced by use as much AI as you can justify in the post-mortem.

### What you can do

If you are a knowledge worker: do not assume your job is safe because AI is cheaper. The math is revealing itself. The companies that fired you to save money are about to discover the replacement costs almost as much.

More importantly, realize that your leverage is changing. If AI costs are going up, the companies that over-indexed on AI headcount reduction are going to find themselves in a weird spot. They reduced costs but did not actually solve the problem. You are not replaceable. You are just temporarily unfashionable.

If you are a developer: start learning the open-source stack. Ollama, llama.cpp, LM Studio, local models. The future of cheap AI is going to look a lot more like your AI running on your machine than rented AI running on someone else's cluster.

The skills that matter now are: running models locally, fine-tuning on your own data, building the infrastructure to host your own inference. These are poor GPU guy skills, the same skills I have been writing about for years. The world is catching up to why they matter.

If you are a founder or executive: re-read the numbers. The savings from AI-driven headcount reduction are already evaporating. The ones who survive will be the ones who planned for the repricing, not the ones who celebrated the press release.

Your move: build real budgets. Track actual costs. And stop pretending that the current pricing is sustainable.

### One more thing

I want to be clear about something: I am not anti-AI. I have built my entire career on the poor GPU guy premise, that you can do meaningful work with limited resources. I am using AI to write this article right now. I think it is a generational technology.

But I think it is a generational technology with real economics, not a magic trick that makes math stop applying.

The difference matters. A technology with real economics can be built on. A magic trick can only be speculated on.

Tokenomics, the idea that LLM tokens are a new asset class with their own coherent economics, was always a marketing term dressed up as a thesis. The analysts and investors who built models on falling costs forever were building on sand.

The actual economics are the same as every other compute-heavy SaaS business in history: margins compress, pricing power matters, unit economics rule.

There is no magic.

Only a few companies like Apple are playing it without risking the future, because they have been through this before with the iPhone App Store, with iCloud, with everything else. They know that sustainable businesses require sustainable margins.

The bill is coming due. The receipts are public.

Do not say nobody told you when the price hike notice lands in your inbox.

---

TL;DR: The cheap AI era is funded by a circular financing daisy chain between investors, hyperscalers, and AI labs. Per-task costs are rising even as per-token prices fall. When the subsidy ends (12-24 months), expect 3-10x price increases on frontier models. Start preparing now: learn local AI, budget for token costs, and do not assume your job is safe just because the press release said AI was cheaper.

---

Your Turn: What is your AI bill looking like? Run the numbers on your actual usage, input tokens, output tokens, and number of calls per task. You might find you are already paying more than you think. Drop a comment and let us compare notes.