## _**RAG that works: why chunking is a human job — Mission #0**_ 

_A 7-part guide to building retrieval systems that start with thoughtful data — not just bigger models._ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 6 min read · Jan 27, 2026_ 

**==> picture [511 x 358] intentionally omitted <==**

## _**The forgotten Foundation of RAG**_ 

A few months ago, I spent over $200 running LLM-powered “chunk optimization” experiments. And thankfully they were free credits I received through a partner program. 

I fed the same PDF into GraphRAG, LightRAG, and a few LangChain autosplitters. I tweaked prompts, adjusted overlap windows, even tried letting an LLM rewrite my documents into “RAG-friendly” summaries. 

The result? 

Worse retrieval. Confusing answers. 

And a lot of wasted tokens. 

Then I did something radical: I opened the PDF in a text editor, read it carefully, and drew the chunk boundaries myself. 

Suddenly, retrieval worked. Not “kind of.” Not “with caveats.” 

It just… worked. 

That’s when I realized: the biggest bottleneck in RAG is not your model, but your data preparation. 

## _**The Illusion of model-centric RAG**_ 

We live in an age where every RAG tutorial starts the same way: 

“Just plug in your embedding model and vector database!” 

Current frameworks, for all their innovation, often treat documents as inert bags of tokens: 

- LangChain’s default splitters cut at fixed token counts — regardless of whether you’re mid-sentence, mid-table, or mid-legal-definition. 

- GraphRAG (Microsoft’s impressive framework) uses LLMs to extract entities and relationships, then builds a knowledge graph. Powerful? Yes. But it requires dozens of LLM calls per document, costs scale nonlinearly, and the output is opaque… even to its creators. 

- LightRAG improves on this by using smaller LLM calls to summarize local context, but it still relies on stochastic reasoning to decide what belongs together. 

All these approaches share a hidden assumption: _that an LLM is the best judge_ . _of semantic boundaries_ 

## 💡 _**The truth is… it’s not.**_ 

An LLM doesn’t know that a footnote belongs to the paragraph above. 

It doesn’t know that a financial disclaimer applies to the entire section. 

It doesn’t know that a case study illustrates the principle introduced two pages earlier. 

You do. 

document is you = the domain expert. 

## _**Why Chunking is the hidden labor of RAG**_ 

Retrieval-Augmented Generation (RAG) has three stages: 

1. Retrieval: find relevant context 

2. Augmentation: inject that context into a prompt 

3. Generation: produce an answer 

But retrieval only works if the retrievable units (your chunks) are meaningful. 

Think of chunking like indexing a book. A good index doesn’t cut entries mid-sentence. It groups concepts logically: 

```
Climate policy → EU regulations, p. 45–48.
```

A bad index? 

```
Climate, p. 45; policy, p. 46; regulations, p. 47…
```

## _**The spectacular fail of AI Agents no one is expecting**_ 

_Replacing RAG with expensive LLM calls is a step sideways, not a leap forward_ 

_generativeai.pub_ 

**==> picture [121 x 113] intentionally omitted <==**

Yet in RAG, we often hand this critical task to algorithms that have no understanding of your domain, your audience, or your intent. 

The result? 

Chunks that are: 

- Too small: missing necessary context (“USB-C” without compatibility notes) 

- Too large: drowning the LLM in irrelevant text 

Semantically broken: half a definition + half an unrelated example 

And then we blame the embedding model when retrieval fails. 

## _**Blaming embeddings is blaming the entire AI game**_ 

_Who keeps underrating the power of cosine similarity and RAG missed the core of Generative AI as a whole._ 

_medium.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**Introducing a Human-Centered Alternative**_ 

What if we flipped the script? 

## _**We ask: “How can we make it easy for humans to chunk well?”**_ 

That’s the philosophy behind the toolkit we’ll build in this series: a modular, transparent, and iterative approach to RAG data preparation. 

Our principles: 

Transparent: you see every chunk before it’s used. 

Auditable: every decision is recorded in structured JSON. 

Efficient: no wasted LLM calls, no hidden costs. 

Modular: each step is a standalone tool you can use today. 

Over the next seven posts, we’ll build a Gradio application with six tabs: 

## 1. Convert PDFs to clean Markdown 

2. Manually set chunk boundaries 

3. Inspect your chunks 

4. Retrieve with BM25 (yes, keyword search it’s still great!) 

5. Add local semantic search (embeddings in action) 

## 6. Combine both for hybrid retrieval 

7. Reply to a query with hybrid retrieval and with local LLM 

By the end you’ll have a full RAG prep and retrieval suite: that starts with you, not a model. 

## _**The bigger picture: RAG as a craft, not just an API**_ 

We’ve been sold a vision of RAG as plug-and-play: drop in your data, hit “embed,” and get smart answers. 

But real-world RAG is more like bookbinding than button-pushing. It requires care, judgment, and iteration. 

## The good news? You don’t need an LLM to do this well. 

You need: 

Clean text (not PDF garbage) 

Structured delimiters (so you can mark boundaries) 

_Open in app_ 

~~Token awareness (so chunks fit in LLM context)~~ 

A way to inspect and refine 

That’s it. 

And as we’ll see in the next post, the first step — converting PDFs into something usable — is where most RAG pipelines fail before they even begin. 

## Great RAG doesn’t start with a prompt. It starts with a paragraph break. 

_Next Mission: Why your PDFs are RAG poison — and how Markdown is the antidote._ 

