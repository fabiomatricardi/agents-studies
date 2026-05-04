# The Secret Behind AI Pricing Most People Ignore | Medium

Member-only story

# The Secret Behind AI Pricing Most People Ignore

[

![Ignacio de Gregorio](https://miro.medium.com/v2/resize:fill:64:64/1*p6kCCpNZARkVEYv4OCH7GQ@2x.jpeg)

](/@ignacio.de.gregorio.noblejas?source=post_page---byline--22f009da22bd---------------------------------------)

[Ignacio de Gregorio](/@ignacio.de.gregorio.noblejas?source=post_page---byline--22f009da22bd---------------------------------------)

Following

9 min read

·

2 days ago

886

13

Listen

Share

More

![](https://miro.medium.com/v2/resize:fit:1000/1*_qNL25isYWV562VWNx-2sw.png)
Source: Author using AI

A few weeks ago, I wrote an article explaining how the price hikes were coming.

Some people disagreed, **but it has only taken a few weeks to prove me right**, even faster than I expected.

However, AI Labs are doing so in a way that goes over most people's heads, and what I believe is a rather shady tactic. They should be more transparent about this, but aren’t, **so my goal today is to fix that**.

Let me explain a trick Anthropic, Claude’s creator, **is using to charge you more** by explaining to you one of the most fundamentally misunderstood components of modern AI.

## The Component Nobody Knows About

Few people know that between you and your favorite AI model lies a component known as a **tokenizer**.

But to understand what it is and why it’s so important to your overall costs, we need to understand what tokens are.

### What is a token?

You may have noticed that everything in Generative AI is measured in ‘tokens’.

_But what are these things?_

In short, **it’s the fundamental unit of semantic meaning for AI models**. It’s the way systems such as ChatGPT ‘break down’ data into components it understands.

In text, that means breaking it down into words. A token has its intrinsic meaning (the word has a meaning by itself), and that meaning will be contextualized once each token is mixed with the other tokens in the sequence.

> For example, ‘bank’ can mean several things depending on the context, from a financial institution to the sloping ground that borders the watercourse of a river.

Importantly, tokens aren’t necessarily complete words; **they can be a couple of letters or even just a single character**. Furthermore, different models use different tokenization methods.

For instance, as you can see below, GPT-4o breaks the sequence above into a string of tokens, with each token getting assigned a number.

![](https://miro.medium.com/v2/resize:fit:700/0*ti-2rP9B1ONEE6Z1)
Source: Tiktokenizer

This number is a row ID; it’s the row number on an embedding table that turns the word, like ‘red’, into a set of numbers that define what ‘red’ is to the model.

![](https://miro.medium.com/v2/resize:fit:700/0*qrmewYwYAwpsEwAf)
Source: Author

_And what do those numbers mean?_ In isolation, not much. **But relative to other tokens, they mean a lot**.

As models don’t interact with the real world, **the understanding they build about real-world concepts is mostly relative**, not ‘tacit’, meaning what ‘red’ is not measured by real examples of ‘red’, **but ‘what it is’ relative to other concepts the model knows.**

Which is to say, these strings of numbers each concept gets assigned are relative semantic distances to other concepts.

Namely, ‘dog’ and ‘cat’, both mammals, domesticated, four-legged, hairy animals, will have more similar numbers than ‘dog’ and ‘pigeon’, and these two, being both animals, will be closer to each other than ‘dog’ and ‘door.’

![](https://miro.medium.com/v2/resize:fit:700/0*I9orGo9uLMKs_wSP.png)
Source

The significance of each number can be more intuitively understood through the image below; they represent global attributes, or dimensions, that we can use to categorize concepts, such as ‘dessertness’ and ‘sandwichness’, to classify desserts.

The model might not fully understand what a shawarma is, but it knows it’s closer to a hot dog than to an apple strudel.

![](https://miro.medium.com/v2/resize:fit:700/1*5FVm1yCVJjmxqR7ik_a_9Q.png)
Source: Google

> That’s how models build understanding; they understand what something is by comparing it to other “known knowns.”

Overall, Generative AI models treat data as a sequence of tokens that, combined, explain the overall meaning.

This can be applied to text, images (breaking them into image patches/groups of pixels), audio via spectrograms… You name it.

![](https://miro.medium.com/v2/resize:fit:700/1*L6ymi47j1-bynvAbTn5OLQ.png)
Source: Author

The main reason for doing this is that **AI models**, just like any machine, **can only “understand” numbers**.

Thus, this tokenization process, breaking down world data into chunks the models can understand, **is done so we can turn something that can’t be processed into a sequence of semantic units of meaning the model “understands.”**

And although there has been a lot of research on changing this, the reality is that, today, this tokenizer, the component that breaks data into tokens, **is external to the actual model.**

![](https://miro.medium.com/v2/resize:fit:700/1*suzhMMMXxD91YXC35Osy4w.png)
Source: Author

_But why is this so relevant?_

Well, because the tokenizer not only plays a technological role, **it also largely influences how expensive a model is**.

### The sizes and number of tokens matter

When you send ‘_What’s today’s news on the Iran war?_’ to ChatGPT, these words are broken down into tokens and fed to the model only then.

![](https://miro.medium.com/v2/resize:fit:700/1*SMIdoKGGo5dyEyqMyzihsg.png)
Source: tiktokenizer using GPT-4o’s tokenizer

The model sees all eight tokens above at once, and processes them in parallel, doing two operations several times:

1.  **Attention**. Each token can “talk” to tokens before it. ‘War’ can “talk” to ‘Iran’ to realize that we’re talking about the Iran War, not the Napoleonic Wars. This is done because, as mentioned, meaning is contextualized. Although ‘War’ has a meaning in itself, it feeds from the context ‘Iran’ to know what war we’re talking about.
2.  **MLP**. Based on the first neural network, [dating back to the 1950s](https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/a/27637/files/2016/03/rosenblatt-1957.pdf) (yes, AI is not precisely “new” in some areas), this lets the model add information to every single token based on its own knowledge. For example, it may add to ‘Iran’ information about its decades-long feud with the US, information that is not present in the sequence but is valuable to contextualize the question.

Models like Claude or Gemini are concatenations of these two operations, progressively building enough understanding for the model to know ‘what comes next.’

![](https://miro.medium.com/v2/resize:fit:700/1*m6zW6NKQIdlQ2VnJka9hyA.png)
Source: Author

Both are token-level computations, meaning the amount of computation they require is proportional to the number of tokens they are fed.

> This introduces a latent surprise most people and enterprises don’t realize when they are choosing ‘x’ or ‘y’ model; **token count matters as much as token prices.**

While everyone is familiar with token prices (models are priced based on the tokens they process and generate), this masks an issue: **the model’s behavior and tokenization matter just as much, if not more**.

Just look at the example we’ve been discussing. If we use Meta’s Llama 3 tokenizer instead of OpenAI's tokenizer, **the exact same text sequence is tokenized into 10 tokens instead of 8**.

![](https://miro.medium.com/v2/resize:fit:700/1*poo-cKpm6i4pH3LueUMj3Q.png)
Source: tiktokenizer using Llama 3’s tokenizer

This means that, for the same model, **if it gets fed 10 tokens instead of 8, the sequence is roughly 20% more expensive to process**.

And worse, because the one tokenizing into 10 has more compressed tokens, the cost of generating the exact same output response will also be higher.

> The reason is what we explained before: **both attention and MLP operations scale with the token count**. Specifically, attention has a ‘big O’ complexity of O(L²) where L is the number of tokens.
> 
> MLPs, on the other hand, have complexity O(2\*L), which is ~ O(L), again with ‘L’ being the number of tokens.

> In plain English, the amount of computational effort both operations need grows with the number of tokens.

![](https://miro.medium.com/v2/resize:fit:700/1*Ign2Y92O_ZxnPrk9bgh38w.png)
Source: Author

And here’s where Anthropic played dirty.

> My newsletter explains AI in first principles and in words you can understand, for those allergic to hype but hungry for knowledge. Join today.

[

## Subscribe | TheWhiteBox by Nacho de Gregorio

### The newsletter to stay ahead of the curve in AI

thewhitebox.beehiiv.com

](https://thewhitebox.beehiiv.com/subscribe?source=post_page-----22f009da22bd---------------------------------------)

## Anthropic’s new tokenizer

The root of the issue is that Anthropic’s new model, **Opus 4.7,** has an up to **35% increase in token count** simply because it changed the tokenizer from Opus 4.6.

> This is most likely because Opus 4.7 is a distillation of Mythos, an entirely new model, but that’s another story.

[And while Anthropic did mention this](https://www.anthropic.com/news/claude-opus-4-7), they “failed” to mention that this could imply a cost increase, for obvious reasons.

And for other obvious reasons, [**_people have started putting this to the test_**](https://openrouter.ai/announcements/opus-47-tokenizer-analysis?utm_source=thewhitebox.beehiiv.com&utm_medium=newsletter&utm_campaign=playing-dirty-the-mythos-lie-prices&_bhlid=632e841da053ffcffb383880ccd69065687a8914) and, to the surprise of nobody, **the model is much more expensive**, up to 27% more relative to Opus 4.6, **despite having the same token pricing ($5/$25 per million input and output tokens)**.

[**_Ramp made a similar analysis and drew the same conclusions_**](https://x.com/rahulgs/status/2048830174524063752?utm_source=thewhitebox.beehiiv.com&utm_medium=newsletter&utm_campaign=playing-dirty-the-mythos-lie-prices&_bhlid=2acf01a92848db33fd0eb22372fc73f655fc383e); Opus 4.7 is just overall more expensive, **despite GPT-5.5 having a higher output token price of $30 vs $25**.

![](https://miro.medium.com/v2/resize:fit:700/0*XTJTLNo_4Ir_zMzI)
Source: Ramp

And just like that, with a simple change that most customers aren’t sophisticated enough to understand because, well, except for analysts like me, nobody should be forced to understand tokenizers to use AI models, **your bill has increased by 12–27% with a single model change** for mostly marginal improvements that do not, in God’s green Earth, justify the price hike.

## Shady tactics kill goodwill

All this was inevitable. **AI is much more expensive than we were led to believe**, and the subsidies were due to end at some point.

And that someday is now.

**The hole in these companies’ balance sheets is enormous**, to the tune of hundreds of billions, over a lifespan much shorter than that of traditional IT assets.

_Revenues?_ At best, **at $100 billion a year for all companies in the mix** (of course, excluding Hyperscaler revenues, which are mostly circular and no real money is actually being transacted).

> To be clear, revenue growth is impressive, but the AI buildout spending growth still far outpaces revenue, at least in nominal terms.

These companies, especially those like Anthropic and OpenAI that are going public this year, have to make money no matter what.

I understand that, **but the shady tactics I’m seeing can come back to bite eventually**; this is not how you keep customers in the long run, and I’m seeing a clear ‘vibe change’ from the hardcore followers these companies had just months ago.

I can’t blame anyone for wanting to make more money; **I can definitely give my opinion on how you choose to do it.**

And the more I read about this stuff, the more convinced I become that enterprises are going to have none of this and **will start migrating massively to open-source once they become sophisticated enough** (in reality, the barrier to open-source is much lower than people think).

You can just appear to announce an almost 30% price hike, while companies nowadays can say _“thanks, but no”_ and move toward open source.

For all these reasons, I fear much of the revenue growth we’re seeing, which is coming mostly from enterprises, might be short-lived as, to me, **private models will only make sense in iterative workflows like coding or agent-based systems**, where even marginal improvements in intelligence matter.

_Is that a trillion-dollar market?_ Let’s just hope it is, because otherwise all these companies are spending billions only for enterprises to say, ‘yeah, thanks, but we’re going with the open-source solution that exists because of you, but it’s much, much cheaper than you are.’

Because thinking frontier AIs, which, in my honest opinion, **will continue to rise in price for years**, can be automation tools that can be profitably used to read your emails, is like _“killing flies with cannonballs”_, as my grandfather used to say, is absolute lunacy.

> I share similar thoughts in a more comprehensive and simplified manner on my [LinkedIn](https://www.linkedin.com/in/ignacio-de-gregorio-noblejas/) (don’t worry, no AI-generated content there either). As a reminder, you can also [subscribe to my newsletter](https://thewhitebox.beehiiv.com/subscribe), and follow my enterprise-AI focused [Medium](/@theimperative) and [Substack](https://substack.com/@theimperativeai).

## Embedded Content