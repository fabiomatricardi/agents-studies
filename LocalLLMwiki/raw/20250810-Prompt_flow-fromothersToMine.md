## FROM EXISTING ARTICLES to blog posts
The workflow and automated chain of prompts

### 1 - read and wait for instructions

>read the following article and be ready for further instructions. when you finish reading say "I am ready"
>
>[start of article]
Why Most AI Products are Scams
A recent controversy has arisen around Anthropic’s decision to severely limit the usage for its heaviest power users, claiming some of them cost them several thousand dollars in losses every month.
At first, you can’t blame them; they earn $200 at most per user and month, only for some of those users to cost them thousands each month.
But the reality is that the system is that most AI products are great products priced in a really scammy way.
The incentives are broken, meaning the AI market is about to suffer a painful transition to a new form of business, the only one that will make sense in the AI era: success-based.
How AI Companies Make (Lose) Money
The AI industry is divided into four layers:
Hardware companies, manufacturing the chips and servers required to train and run AI.
Infrastructure companies, which build the data centers hosting those servers, either rent that space to Labs or use it to deploy their own AI products or services.
Model-layer companies, which train and run AI models, and offer them in two ways: via subscription and via API (only pay for what you use).
Application companies, usually known as ‘AI wrappers’, are those that build their product or service on top of third-party AI models.
These layers aren’t mutually exclusive. Companies like Google and, in the medium term, OpenAI, operate across all layers.
And while the business model for hardware and infra companies is clear as day, you pay for what you use and only for what you use, the story is different for the model and application layers.
In there, you are consistently getting scammed. But why?
Non-determinism and Tokens
The question here is, how is AI software charged?
We’ll focus exclusively on Generative AI, products like ChatGPT, as these are the ones that end-users/companies can’t simply train themselves and thus buy from third parties.
In this case, these models are charged based on one thing: tokens.
But what is a token?
By definition, it’s the basic unit of semantic information in any data modality (words or subwords in text, pixels or pixel patches in images, and so on). It’s an essential piece in AI because it translates the user's data into numbers that the AI can process, as computers are unable to process text directly. Let me explain further.
When you send the sentence “What’s the capital of Nepal?” to an AI model, the model actually sees a string of numbers, shown bottom-right in the image below in GPT-4o’s case.
These numbers are indices of the rows in a table we call the ‘embeddings table’, where each row is a word or subword (aka, token) that the model knows, and the columns of that table are the attributes of that token in numbers.
In other words, each word in your sentence gets transformed into a set of numbers we call an ‘embedding’. These numbers are not arbitrary, but can be understood as attributes that the concept has.
The simplest example of this would be an instance where the model only knows five things: ‘borscht’, ‘hot dog’, ‘shawarma’, ‘pizza’, and ‘salad’. Thus, to give a numerical set of values to each of the five words, we can simply assign a 1 to the shawarma for the attribute ‘shawarma’ and zero for the rest, and the same for other foods.
However, this approach to discriminating between concepts is flawed, or at least suboptimal, because these elements share common attributes.
Both the hot dog and shawarma have meat, so both are more similar to each other than salad and hot dog (salad and shawarma both have greens too, so they are closer to each other than salad and pizza). You get the gist.
This means that we can grow the complexity of our ‘space’ of concepts to capture more nuanced relationships, like distributing them based on how ‘sandwichy’ they are:
Or based on a growing number of dimensions, such as ‘sandwichy’, ‘dessertness’, or ‘liquidness’
Now, grow this idea into the hundreds of thousands of dimensions, and you've got yourself a similar concept space as the one ChatGPT has.
This ‘internal world’, known as ‘latent space’, is governed by the principle of similarity, where concepts that are similar have similar embeddings, and those that aren’t are separated.
This means models build an understanding of ‘what something is’ based on how similar or dissimilar it is to other known concepts, as models don’t have a physical body to ground concepts as we do, opening the question as to whether they ‘understand’ what things are or not.
Okay, so what?
The key point to understand is that models both process and generate these tokens, incurring an electric cost. This means Generative AI models are billed in two ways:
Per the tokens that they process
Per the tokens they generate
Usually, the latter is three times pricier than the former because the token processing stage, known as the ‘prefill stage’ is better suited for GPUs as it’s dominanted by matrix-to-matrix multiplication, where GPUs thrive and taking LLM providers closer or even over — albeit rare — the arithmetic intensity threshold of the GPU.
On the other hand, token generation is matrix-to-vector multiplication-heavy, which means a higher percentage of total watthour (energy) spent is used to move data instead of crunching numbers (the latter is revenue generating, the former isn’t) because of the memory cache (KV Cache). But I digress.
At first, all this looks good; we have fixed prices, right? Well, not quite.
Prices are fixed per token, yes, but the number of tokens the model processes or generates is dynamic; it completely changes across different user requests. Even in cases where the input is identical, the output slightly varies, a term known as non-determinism.
In layman’s terms, neither the user nor OpenAI know how much will an interaction cost.
And this is what takes us to Anthropic’s controversy.
Appealing to Investors is the wrong play
Although non-determinism is at the core of AI models (and we haven’t even factored in accuracy, more on that in a minute), most AI companies offer their services using fixed-priced subscriptions.
These are easy to understand for the user, who can predict the cost of the service. It’s also super appealing to investors, who can’t get enough of monthly and annual recurrent revenue (MRR/ARR) metrics, because they give an otherwise unpredictable business — and, thus, investment — an easy excuse to ‘predict’ yearly revenues in what, in reality, is a totally unpredictable environment.
As these projected revenues are crucial in new investment round talks (the valuation for the round is primarily measured by the multiple with regards to, you guessed it, ARR), AI companies in desperate need of cash will reach absurd levels (even illegal ones) to grow their ARR.
All well and good, but here’s the thing: it just doesn’t make any sense.
At the end of the day, your business, both the way you make money and spend it, is based on the unpredictable metrics of processed/generated tokens, which is how you pay your upstream suppliers (the infra guys).
And if you’re the infrastructure guy too, you’re still paying huge energy bills based on watts consumed in an hour, which is largely dynamic and dependent on how many tokens (and people) you’re serving.
It’s all dynamic, but priced at a fixed value.
I wonder what could go wrong? Well, a lot goes wrong.
Operational Excellence Will be the Moat
Under the current business model, companies are forced to impose severe rate limits (how much you can actually use models), which are sometimes set based on usage or at arbitrary token values.
For example, if you’re using Anthropic’s models in the Tier 1 setting (you haven’t spent enough to grow into better tiers), you can’t send the models input sequences larger than 30,000 tokens (~23k words).
That sounds like a lot, but you would be surprised how quickly tokens ramp up. This is a per-minute restriction, so if you send the model three requests over 10k each in the same minute, you'll get rate-limited.
This is a terrible experience for the user, who can’t predict, not even for a single sequence, if it’s going to hit the rate limits, which in production settings can be a disaster (imagine your customer support chatbot runs out of tokens and ignores the customer it’s supporting).
Alternatively, you can come across instances that seem completely absurd, such as Google offering Gemini 2.5 Pro Deep Think, arguably the smartest AI system on the planet, but only to Ultra subscription members ($300/month) and rate-limited to 5 queries a day.
Truly terrible experience that is only justified by how early we are to this business. But being excused for being early doesn’t excuse you for improving an obviously broken system.
But, guess what, it gets worse!
Failures Are Paid too!
For both model providers and users, a certain number of generations will not be effective, meaning they won’t be relevant to the user.
In most cases, making AI productive for the user is a game of statistical coverage, repeating several tries until you get one you’re happy with.
In fact, models like Gemini 2.5 Pro Deep Think or o3-pro do ‘best-of-n’ sampling, in which they will run the problem several times, and give you the one that works best, based on another AI model acting as a judge to score.
You can argue that these ‘additional inferences’ are not billed to the user; however, they are, in fact, billed, as the token prices for these models in the API skyrocket (at least for o3-pro, since Deep Think is only available via subscription).
o3-pro, o3 with multiple tries per query, is ten times more expensive than the ‘single query’ option
All things considered, the user is offered a subscription that:
Is extremely overpriced for most standard users, who may only be generating $3 or $4 of cost while being billed 5 to 7 times that.
Is highly underpriced to companies dealing with power users, who can spend dozens of times more than what they are paying, forcing companies like Anthropic to impose severe restrictions.
Is extremely opaque for the user, who can’t ‘see’ the value of what they are getting (they don’t know how many bad calls they are being charged, whether the model enters doom reasoning — thinking for much longer than it should), or even being ‘downgraded’ to worse models without telling you, and who knows what else.
You can even fall into hidden cost traps, where some tokenizers (how models break down data into tokens) are much more fine-grained (they break sequences into much smaller chunks), which means that, even though some companies may be offering more competitive token prices, their models generate many more tokens, leading to a larger total cost.
In short, opacity, hidden costs, and unpredictability are the name of the game.
So, what should companies do?
Operational Excellence is the Moat
Most AI companies are living on borrowed time in terms of their business model.
Soon enough, as the model layer continues to commoditize, people will start paying closer attention to costs, especially considering how open-source models (mainly Chinese) topple most leaderboards when it comes to performance-to-cost.
In that scenario, people will become so sensitive to pricing that, coupled with product experience (a topic for another day), pricing will be the defining factor of choice.
This will turn the industry into a race to the bottom in prices, where only those companies offering success-based pricing (getting charged only for what is useful) will concentrate most users (both companies and end consumers).
Being profitable while charging only a fraction of your inferences is extremely challenging, requiring real operational excellence.
But if we consider that AI will be a commodity, this operational excellence will be your moat, as you’ll be able to outcompete others based on price (the defining metric in commoditized environments).
A Cutting-Edge Technology Living In the Past
As AI increasingly eats up software, the days of opaque subscriptions, where customers willingly accept they are being scammed, will be over.
Usage-based pricing and, especially, success-based pricing will become the norm.
The consequences are huge for a company where investors are used to this recurrence, where software companies are used to high margins; all of that is gone.
AI will not only be deflationary but also serve as a scambuster for the trillion-dollar digital software market, which has long enjoyed high barriers to entry, resulting in excessively high margins and subpar purchasing experiences.
And none will be more exposed to this new reality than AI companies themselves, who are leading the change while still clinging to the outdated and outrageously scammy practices of the previous software era.
Software companies that don’t make this turn willingly will pay the price unwillingly.
Conversely, those who understand this and make changes before they are forced to will immerse themselves in a journey of pain, but one in which they will come out with AI engineering expertise that will allow them to drop prices to outcompete others while still being profitable.
In an era where everyone offers the same thing, cheaper usually represents the winning adjective.
>
> [end of article]


---

### 2 - Analysis
> what are the 3 key points? is there any critique or special angle form the author?

The article presents a sharp, critical perspective on the current business models of AI companies, arguing that they are fundamentally flawed and unsustainable. Here are the three key points, followed by the author’s critique and special angle:

Three Key Points:
AI is priced based on tokens, but token usage is non-deterministic and unpredictable
Generative AI models are billed per token (input and output), but the number of tokens consumed varies significantly per request—even for identical inputs—due to the non-deterministic nature of AI generation.
This creates a misalignment: users and providers cannot predict costs, yet most companies charge via fixed subscriptions (like $20/month), which don’t reflect actual resource usage.
Current pricing models are broken and favor investor optics over sustainability
AI companies use subscription models primarily to appeal to investors, who value predictable Monthly Recurring Revenue (MRR) and Annual Recurring Revenue (ARR) for higher valuations.
This leads to artificial pricing that doesn’t reflect real costs, resulting in financial losses for providers when power users consume far more than they pay for—hence Anthropic’s rate-limiting controversy.
The future of AI pricing must be success-based and operationally efficient
The author argues that the only sustainable model is success-based pricing, where users pay only for useful, successful outputs—not for failed attempts or excessive token use.
This requires extreme operational excellence (efficiency in inference, model optimization, infrastructure) to remain profitable while charging less.
As AI models become commoditized (especially with open-source and Chinese models), price and efficiency will become the main competitive advantages.
Author’s Critique and Special Angle:
Critique:
The author strongly criticizes AI companies for perpetuating a scam-like system—not necessarily through intentional fraud, but through opaque, misleading pricing that hides real costs, penalizes users for failed generations, and exploits investor-driven revenue models. The term “scam” is used provocatively to highlight how users are overcharged for low-value interactions, while companies risk collapse due to cost-revenue imbalances.
Special Angle:
The article frames the issue not just as a technical or economic problem, but as a necessary evolution in the software business model. It positions AI as a "scambuster" for the broader software industry, which has long relied on high-margin, low-transparency subscription models. The author suggests that AI will force a reckoning: only companies that embrace transparency, efficiency, and user-aligned pricing (i.e., paying for outcomes, not usage) will survive.
Additionally, the author emphasizes non-determinism and hidden costs (like best-of-n sampling, KV cache inefficiencies, and tokenizer differences) as underdiscussed technical realities that undermine current pricing—giving the argument a unique blend of technical depth and business insight.
In short:
The article argues that AI is too dynamic to be sold like traditional software, and the industry must move from subscription-based scams to success-based fairness, or face collapse in a commoditized future.

---

### 3 - rewrite it into a blog post.
> rewrite it into a blog post.
> write in first person. avoid jargon, the audience is non experts but enthusiasts in AI.
start with a strong hook that uncover a common pain point with the readers
use humor facts or jokes, sometimes, to keep the reader attention.
conclude inviting the readers to think about going local: to use a local LLM with easy tools like llama.cpp and amazing existing open-source models.



**Why You’re Probably Getting Scammed by Your Favorite AI (And Why I Switched to Running AI at Home)**

Let me guess: you’ve been using an AI tool—maybe ChatGPT, Gemini, or Claude—and at some point, you asked it something simple like, “Summarize this article,” and it responded… with the energy of a philosophy PhD writing their final thesis. Pages. Of. Text. And you thought: *“Did I just get charged for that?”*

Yeah. Me too.

And here’s the uncomfortable truth: **you probably did**—even if you’re on a $20/month plan. Worse? That over-the-top response might’ve cost the company *hundreds of times* more to generate than what you paid. And yet… they still let you do it. Until now.

Recently, Anthropic—maker of Claude—started *slamming the brakes* on its heaviest users. Some folks were apparently costing them *thousands of dollars a month* while paying just a few hundred. So they clamped down with brutal rate limits. Understandable? Sure. But also a giant red flag: **something is deeply broken in how we pay for AI.**

And honestly? Most AI products today aren’t scams in the shady, “I sold you a fake Rolex” way. They’re scams in the *“I sold you a luxury cruise… but you’re stuck on a rowboat with a snorkel”* kind of way.

Let me explain.

---

### The Bait-and-Switch of AI Subscriptions

You sign up for a “premium” AI plan. It says “unlimited access” or “priority access” or some other phrase that sounds like freedom, but feels more like a golden cage.

But here’s the twist: **AI doesn’t work like Netflix.**

When you stream *Stranger Things*, Netflix knows exactly how much bandwidth it costs to send you that data. It’s predictable. AI? Not even close.

Every time you ask a question, the AI has to *think*—and that thinking burns electricity. And the longer it thinks, the more it costs. But you don’t pay per “thought.” You pay per month. Flat rate.

So what happens when someone asks the AI to analyze 100 pages of legal documents, generate code, and then write a Shakespearean sonnet about it? *Cue the CFO having a panic attack.*

The company might make $200 from that user… while spending $3,000 in computing power. That’s not a business. That’s a charity with better branding.

---

### Why “Unlimited” Always Comes With a Catch

To survive, AI companies slap on sneaky limits:

- “You can only send 30,000 tokens per minute.” (What’s a token? Great question. It’s like a word, but not. Think of it as AI calories. And yes, some AIs are *extremely* hungry.)
- “You can only make 5 queries per day.” (Yes, Google’s *most powerful* AI, Gemini Ultra, lets you ask it five questions a day. Five. That’s less than my nephew asks me about dinosaurs.)

And here’s the kicker: **even when the AI messes up, you still pay.**

Imagine going to a restaurant, ordering a steak, getting served burnt toast, and the waiter says, “Great! That’ll be $40.” You’d walk out. But with AI? You ask a question, get a useless answer, try again, and again—each time burning tokens—until *finally* it gets it right. And you’re charged for *all* of it.

Some AIs even run *multiple versions* of your request in the background, pick the best one, and throw the rest away. Fancy! But that means they’re doing 5x the work… and passing those costs onto you, one way or another.

---

### The Investor Mirage

Why do companies do this? Blame investors.

In Silicon Valley, the magic words are **“recurring revenue.”** It sounds stable. Predictable. Safe. So startups sell subscriptions, pump up their annual revenue numbers, and raise millions.

But here’s the dirty secret: **they don’t know how much it actually costs to serve you.**

It’s like running a pizza shop where every customer orders “one pie,” but some get a slice and others demand 100 pizzas with gold leaf. And you’re charging both $20.

Investors love the story. Reality? Not so much.

---

### The Future: Pay for What *Works*, Not What Burns

The only sustainable way forward? **Pay for success, not usage.**

Imagine paying only when the AI gives you a *good* answer. Not for every failed attempt, not for the times it rambles like your uncle at Thanksgiving. Just for the wins.

This will force AI companies to become *insanely* efficient. To optimize every line of code, every watt of power. Because if they’re only getting paid for 1 out of 5 responses, they better make that 1 count—and do it cheaply.

And when that happens, the companies with the best tech *and* the leanest operations will win. Everyone else? They’ll be the Blockbusters of AI.

---

### But Here’s the Plot Twist: You Don’t Need to Wait

You know what’s wild? **You can already run powerful AI on your own laptop. For free. No subscriptions. No tokens. No shady billing.**

Tools like **llama.cpp** let you run state-of-the-art open-source models (like Mistral, Llama, or Phi) *locally*—right on your machine. No internet needed. No tracking. No limits.

And these models? They’re *really* good. Good enough to write emails, summarize documents, help with coding, even chat like a real assistant. And yes, they’re not quite GPT-4 level… but they’re closing the gap fast—and they’re free.

I’ve been using a 7-billion-parameter model on my MacBook. It’s not instant, but it’s *mine*. I can ask it anything, as many times as I want, and the only thing I’m paying for is my electricity bill (and honestly, my wife is more annoyed by the fan noise than the power bill).

---

### Final Thought: Who’s Really in Control?

We’ve spent years giving our data, our attention, and our money to tech giants who treat AI like a luxury spa—exclusive, expensive, and full of hidden fees.

But AI doesn’t have to be that way.

It can be **yours**. On your terms. In your hands.

So next time you’re frustrated by rate limits, vague pricing, or AI that just won’t *listen*—ask yourself:  
**Why am I paying for this… when I could be running it myself?**

The future of AI isn’t in the cloud.  
It’s on your desk.  
And it’s free.

Go try **llama.cpp**. Or **LM Studio**. Or **Ollama**.  
Download a model. Fire it up.  
See what happens when *you* own the intelligence.

You might just realize:  
The best AI product isn’t something you subscribe to.  
It’s something you *run*.