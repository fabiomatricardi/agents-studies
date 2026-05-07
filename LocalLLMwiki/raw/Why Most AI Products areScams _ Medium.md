## _**Why Most AI Products are Scams**_ 

_Why AI Subscriptions Are Bad For Everyone_ 

_10 min read · 5 days ago_ 

**==> picture [17 x 18] intentionally omitted <==**

_Ignacio de Gregorio Following_ 

**==> picture [540 x 360] intentionally omitted <==**

_Image source: Author using GPT-4o_ 

A recent controversy has arisen around Anthropic’s decision to severely limit the usage for its heaviest power users, claiming some of them cost them several thousand dollars in losses every month. 

At first, you can’t blame them; they earn $200 at most per user and month, only for some of those users to cost them thousands each month. 

_But the reality is that the system is that most AI products are great products priced in a really scammy way._ 

The incentives are broken, meaning the AI market is about to suffer a painful transition to a new form of business, the only one that will make sense in the AI era: success-based. 

Hardware companies, manufacturing the chips and servers required to train and run AI. 

- Infrastructure companies, which build the data centers hosting those servers, either rent that space to Labs or use it to deploy their own AI products or services. 

- Model-layer companies, which train and run AI models, and offer them in two ways: via subscription and via API (only pay for what you use). 

Application companies, usually known as ‘AI wrappers’, are those that build their product or service on top of thirdparty AI models. 

_These layers aren’t mutually exclusive. Companies like Google and, in the medium term, OpenAI, operate across all layers._ 

And while the business model for hardware and infra companies is clear as day, you pay for what you use and only for what you use, the story is different for the model and application layers. 

In there, you are consistently getting scammed. _But why?_ 

## _**Non-determinism and Tokens**_ 

The question here is, _how is AI software charged?_ 

We’ll focus exclusively on Generative AI, products like ChatGPT, as these are the ones that end-users/companies can’t simply train themselves and thus buy from third parties. 

In this case, these models are charged based on one thing: tokens. 

_But what is a token?_ 

By definition, it’s the basic unit of semantic information in any data modality (words or subwords in text, pixels or pixel patches in images, and so on). It’s an essential piece in AI because it translates the user's data into numbers that the AI can process, as computers are unable to process text directly. Let me explain further. 

When you send the sentence _“What’s the capital of Nepal?_ ” to an AI model, the model actually sees a string of numbers, shown bottom-right in the image below in GPT-4o’s case. 

**==> picture [514 x 216] intentionally omitted <==**

These numbers are indices of the rows in a table we call the ‘embeddings table’, where each row is a word or subword (aka, token) that the model knows, and the columns of that table are the attributes of that token in numbers. 

In other words, each word in your sentence gets transformed into a set of numbers we call an ‘embedding’. These numbers are not arbitrary, but can be understood as attributes that the concept has. 

The simplest example of this would be an instance where the model only knows five things: ‘borscht’, ‘hot dog’, ‘shawarma’, ‘pizza’, and ‘salad’. Thus, to give a numerical set of values to each of the five words, we can simply assign a 1 to the shawarma for the attribute ‘shawarma’ and zero for the rest, and the same for other foods. 

**==> picture [514 x 530] intentionally omitted <==**

**==> picture [51 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source: Google<br>**----- End of picture text -----**<br>


However, this approach to discriminating between concepts is flawed, or at least suboptimal, because these elements share common attributes. 

Both the hot dog and shawarma have meat, so both are more similar to each other than salad and hot dog (salad and shawarma both have greens too, so they are closer to each other than salad and pizza). You get the gist. 

This means that we can grow the complexity of our ‘space’ of concepts to capture more nuanced relationships, like distributing them based on how ‘sandwichy’ they are: 

**==> picture [514 x 134] intentionally omitted <==**

_Source: Google_ 

Or based on a growing number of dimensions, such as ‘sandwichy’, ‘dessertness’, or ‘liquidness’ 

**==> picture [514 x 398] intentionally omitted <==**

**==> picture [51 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source: Google<br>**----- End of picture text -----**<br>


Now, grow this idea into the hundreds of thousands of dimensions, and you've got yourself a similar concept space as the one ChatGPT has. 

This ‘internal world’, known as ‘latent space’, is governed by the principle of similarity, where concepts that are similar have similar embeddings, and those that aren’t are separated. 

_This means models build an understanding of ‘what something is’ based on how similar or dissimilar it is to other known concepts, as models don’t have a physical body to ground concepts as we do, opening the question as to whether they ‘understand’ what things are or not._ 

The key point to understand is that models both process and generate these tokens, incurring an electric cost. This means Generative AI models are billed in two ways: 

1. Per the tokens that they process 

2. Per the tokens they generate 

_Usually, the latter is three times pricier than the former because the token processing stage, known as the ‘prefill stage’ is better suited for GPUs as it’s dominanted by matrix-to-matrix multiplication, where GPUs thrive and taking LLM providers closer or even over — albeit rare — the arithmetic intensity threshold of the GPU._ 

_On the other hand, token generation is matrix-to-vector multiplication-heavy, which means a higher percentage of total watthour (energy) spent is used to move data instead of crunching numbers (the latter is revenue generating, the former isn’t) because of the memory cache (KV Cache). But I digress._ 

At first, all this looks good; we have fixed prices, _right?_ Well, not quite. 

Prices are fixed per token, yes, but the number of tokens the model processes or generates is dynamic; it completely changes across different user requests. Even in cases where the input is identical, the output slightly varies, a term known as non-determinism. 

## _In layman’s terms, neither the user nor OpenAI know how much will an interaction cost._ 

And this is what takes us to Anthropic’s controversy. 

## _**Appealing to Investors is the wrong play**_ 

Although non-determinism is at the core of AI models (and we haven’t even factored in accuracy, more on that in a minute), most AI companies offer their services using fixed-priced subscriptions. 

These are easy to understand for the user, who can predict the cost of the service. It’s also super appealing to investors, who can’t get enough of monthly and annual recurrent revenue (MRR/ARR) metrics, because they give an otherwise unpredictable business — and, thus, investment — an easy excuse to ‘predict’ yearly revenues in what, in reality, is a totally unpredictable environment. 

As these projected revenues are crucial in new investment round talks (the valuation for the round is primarily measured by the multiple with regards to, you guessed it, ARR), AI companies in desperate need of cash will reach absurd levels (even illegal ones) to grow their ARR. 

All well and good, but here’s the thing: it just doesn’t make any sense. 

At the end of the day, your business, both the way you make money and spend it, is based on the unpredictable metrics of processed/generated tokens, which is how you pay your upstream suppliers (the infra guys). 

_And if you’re the infrastructure guy too, you’re still paying huge energy bills based on watts consumed in an hour, which is largely dynamic and dependent on how many tokens (and people) you’re serving._ 

## _It’s all dynamic, but priced at a fixed value._ 

_I wonder what could go wrong?_ Well, a lot goes wrong. 

## _**Operational Excellence Will be the Moat**_ 

Under the current business model, companies are forced to impose severe rate limits (how much you can actually use models), which are sometimes set based on usage or at arbitrary token values. 

For example, if you’re using Anthropic’s models in the Tier 1 setting (you haven’t spent enough to grow into better tiers), you can’t send the models input sequences larger than 30,000 tokens (~23k words). 

**==> picture [514 x 153] intentionally omitted <==**

_That sounds like a lot, but you would be surprised how quickly tokens ramp up. This is a per-minute restriction, so if you send the model three requests over 10k each in the same minute, you'll get rate-limited._ 

This is a terrible experience for the user, who can’t predict, not even for a single sequence, if it’s going to hit the rate limits, which in production settings can be a disaster (imagine your customer support chatbot runs out of tokens and ignores the customer it’s supporting). 

Alternatively, you can come across instances that seem completely absurd, such as Google offering Gemini 2.5 Pro Deep Think, arguably the smartest AI system on the planet, but only to Ultra subscription members ($300/month) and ratelimited to 5 queries a day. 

Truly terrible experience that is only justified by how early we are to this business. But being excused for being early doesn’t excuse you for improving an obviously broken system. 

But, guess what, _it gets worse!_ 

## _**Failures Are Paid too!**_ 

For both model providers and users, a certain number of generations will not be effective, meaning they won’t be relevant to the user. 

In most cases, making AI productive for the user is a game of statistical coverage, repeating several tries until you get one you’re happy with. 

In fact, models like Gemini 2.5 Pro Deep Think or o3-pro do ‘best-of-n’ sampling, in which they will run the problem several times, and give you the one that works best, based on another AI model acting as a judge to score. 

You can argue that these ‘additional inferences’ are not billed to the user; however, they are, in fact, billed, as the token prices for these models in the API skyrocket (at least for o3-pro, since Deep Think is only available via subscription). 

**==> picture [514 x 81] intentionally omitted <==**

_o3-pro, o3 with multiple tries per query, is ten times more expensive than the ‘single query’ option_ 

All things considered, the user is offered a subscription that: 

1. Is extremely overpriced for most standard users, who may only be generating $3 or $4 of cost while being billed 5 to 7 times that. 

2. Is highly underpriced to companies dealing with power users, who can spend dozens of times more than what they are paying, forcing companies like Anthropic to impose severe restrictions. 

3. Is extremely opaque for the user, who can’t ‘see’ the value of what they are getting (they don’t know how many bad calls they are being charged, whether the model enters doom reasoning — thinking for much longer than it should), or even being ‘downgraded’ to worse models without telling you, and who knows what else. 

4. You can even fall into hidden cost traps, where some tokenizers (how models break down data into tokens) are much more fine-grained (they break sequences into much smaller chunks), which means that, even though some companies may be offering more competitive token prices, their models generate many more tokens, leading to a larger total cost. 

In short, opacity, hidden costs, and unpredictability are the name of the game. 

## So, _what should companies do?_ 

## _**Operational Excellence is the Moat**_ 

Most AI companies are living on borrowed time in terms of their business model. 

Soon enough, as the model layer continues to commoditize, people will start paying closer attention to costs, especially considering how open-source models (mainly Chinese) topple most leaderboards when it comes to performance-to-cost. 

In that scenario, people will become so sensitive to pricing that, coupled with product experience (a topic for another day), pricing will be the defining factor of choice. 

This will turn the industry into a race to the bottom in prices, where only those companies offering success-based pricing (getting charged only for what is useful) will concentrate most users (both companies and end consumers). 

Being profitable while charging only a fraction of your inferences is extremely challenging, requiring real operational excellence. 

_But if we consider that AI will be a commodity, this operational excellence will be your moat, as you’ll be able to outcompete others based on price (the defining metric in commoditized environments)._ 

## _**A Cutting-Edge Technology Living In the Past**_ 

As AI increasingly eats up software, the days of opaque subscriptions, where customers willingly accept they are being scammed, will be over. 

_Usage-based pricing and, especially, success-based pricing will become the norm._ 

The consequences are huge for a company where investors are used to this recurrence, where software companies are used to high margins; all of that is gone. 

AI will not only be deflationary but also serve as a scambuster for the trillion-dollar digital software market, which has long enjoyed high barriers to entry, resulting in excessively high margins and subpar purchasing experiences. 

And none will be more exposed to this new reality than AI companies themselves, who are leading the change while still clinging to the outdated and outrageously scammy practices of the previous software era. 

## _Software companies that don’t make this turn willingly will pay the price unwillingly._ 

Conversely, those who understand this and make changes before they are forced to will immerse themselves in a journey of pain, but one in which they will come out with AI engineering expertise that will allow them to drop prices to outcompete others while still being profitable. 

In an era where everyone offers the same thing, cheaper usually represents the winning adjective. 

_This is a free, non-paywalled post you can share with Medium and also external readers, but only if you enjoyed it._ 

_I share similar thoughts in a more comprehensive and simplified manner on my LinkedIn (don’t worry, no hyperbole there either). As a reminder, you can also subscribe to my newsletter._ 

_Artificial Intelligence Technology Programming Data Science Business_ 

**==> picture [34 x 34] intentionally omitted <==**

**==> picture [59 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
Following<br>**----- End of picture text -----**<br>


## _Written by Ignacio de Gregorio_ 

_182K followers · 25 following_ 

_I break down AI in easy-to-understand language for you. Sign up here: https://thewhitebox.beehiiv.com/subscribe Business inquiries: nacho@thewhitebox.ai_ 

