# RAG THAT WORK SERIES
https://thepoorgpuguy.substack.com/p/vip-rag-that-works-why-chunking-is

[VIP] RAG that works: why chunking is a human job - Mission #0
A 7-part guide to building retrieval systems that start with thoughtful data—not just bigger models.
DEC 03, 2025
∙ PAID

The forgotten Foundation of RAG
Why your chunks matter more than your embedding model?

A few months ago, I spent over $200 running LLM-powered “chunk optimization” experiments.

I fed the same PDF into GraphRAG, LightRAG, and a few LangChain auto-splitters. I tweaked prompts, adjusted overlap windows, even tried letting an LLM rewrite my documents into “RAG-friendly” summaries.

The result?

Worse retrieval. Confusing answers.

And a lot of wasted tokens.

Then I did something radical: I opened the PDF in a text editor, read it carefully, and drew the chunk boundaries myself.

Suddenly, retrieval worked. Not “kind of.” Not “with caveats.”

It just… worked.

That’s when I realized: the biggest bottleneck in RAG is not your model, but your data preparation.

The Illusion of model-centric RAG

We live in an age where every RAG tutorial starts the same way:

“Just plug in your embedding model and vector database!”

But this skips the most critical step: making your data retrieval-ready.

Current frameworks, for all their innovation, often treat documents as inert bags of tokens:

LangChain’s default splitters cut at fixed token counts—regardless of whether you’re mid-sentence, mid-table, or mid-legal-definition.

GraphRAG (Microsoft’s impressive framework) uses LLMs to extract entities and relationships, then builds a knowledge graph. Powerful? Yes. But it requires dozens of LLM calls per document, costs scale non-linearly, and the output is opaque… even to its creators.

LightRAG improves on this by using smaller LLM calls to summarize local context, but it still relies on stochastic reasoning to decide what belongs together.

All these approaches share a hidden assumption: that an LLM is the best judge of semantic boundaries.

💡 But here’s a secret: it’s not.

An LLM doesn’t know that a footnote belongs to the paragraph above.

It doesn’t know that a financial disclaimer applies to the entire section.

It doesn’t know that a case study illustrates the principle introduced two pages earlier.

You do.

And that’s the core idea behind this series: the best person to chunk your document is you = the domain expert.

Why Chunking is the hidden labor of RAG

Retrieval-Augmented Generation (RAG) has three stages:

Retrieval: find relevant context

Augmentation: inject that context into a prompt

Generation: produce an answer

But retrieval only works if the retrievable units (your chunks) are meaningful.

Think of chunking like indexing a book. A good index doesn’t cut entries mid-sentence. It groups concepts logically:

Climate policy → EU regulations, p. 45–48.

A bad index?

Climate, p. 45; policy, p. 46; regulations, p. 47…

… useless.

Agents wants to replace RAG, but can they? - Awakened Intelligence 2025#023
22 GIUGNO 2025
Read full story

Yet in RAG, we often hand this critical task to algorithms that have no understanding of your domain, your audience, or your intent.

The result?

Chunks that are:

Too small: missing necessary context (“USB-C” without compatibility notes)

Too large: drowning the LLM in irrelevant text

Semantically broken: half a definition + half an unrelated example

And then we blame the embedding model when retrieval fails.

AI's real guts: blaming the embeddings is blaming the entire AI game- Awakened Intelligence 2025#018
18 MAGGIO 2025

A curious narrative is gaining traction in some corners of the AI discussion: a downplaying of fundamental components like embeddings, cosine similarity, and even the well-established Retrieval Augme…

Read full story
Introducing a Human-Centered Alternative

What if we flipped the script?

Instead of asking, “How can we make LLMs better at chunking?”

We ask: “How can we make it easy for humans to chunk well?”

That’s the philosophy behind the toolkit we’ll build in this series: a modular, transparent, and iterative approach to RAG data preparation.

Our principles:

Transparent: you see every chunk before it’s used.

Auditable: every decision is recorded in structured JSON.

Efficient: no wasted LLM calls, no hidden costs.

Modular: each step is a standalone tool you can use today.

Over the next seven posts, we’ll build a Gradio application with six tabs:

Convert PDFs to clean Markdown

Manually set chunk boundaries

Inspect your chunks

Retrieve with BM25 (yes, keyword search it’s still great!)

Add local semantic search (embeddings in action)

Combine both for hybrid retrieval

Reply to a query with hybrid retrieval and with local LLM

By the end, you’ll have a full RAG prep and retrieval suite: that starts with you, not a model.

The bigger picture: RAG as a craft, not just an API

We’ve been sold a vision of RAG as plug-and-play: drop in your data, hit “embed,” and get smart answers.

But real-world RAG is more like bookbinding than button-pushing. It requires care, judgment, and iteration.

The good news? You don’t need an LLM to do this well.
You need:

Clean text (not PDF garbage)

Structured delimiters (so you can mark boundaries)

Token awareness (so chunks fit in LLM context)

A way to inspect and refine

That’s it.

And as we’ll see in the next post, the first step—converting PDFs into something usable—is where most RAG pipelines fail before they even begin.

Great RAG doesn’t start with a prompt. It starts with a paragraph break.

Next week: Why your PDFs are RAG poison—and how Markdown is the antidote.

Until next time,

Fabio – ThePoorGPUguy




---


[VIP] RAG that works - Mission #1
https://thepoorgpuguy.substack.com/p/vip-rag-that-works-mission-1
From PDF chaos to clear Markdown
DEC 10, 2025
∙ PAID

Why your RAG pipeline begins with structured text

If you’ve ever tried to build a RAG system from a PDF, you know the pain.

You upload a 50-page white paper. You run it through a PDF parser.

And what comes out?

“Figur e 3: Marke t T rend s … … … … … … … … … … … … … … … … … … T ot al Rev enue inc reased by 12% in Q3 .”

Columns are scrambled.

Tables become word salads. Headers and footers leak into body text.

Page numbers float like ghosts in the middle of sentences.

PDFs weren’t designed for machines. They were designed for printers.

And yet, we keep feeding them into RAG pipelines as if they’re clean data.

They’re not.

They’re layout artifacts—beautiful for humans, toxic for retrieval.

The Markdown Revelation

The solution is not another fancier parsing. The real solution relies on using the right intermediate format.

And to me the best candidate is Markdown.

Why Markdown?

It’s human-readable: you can open it in any text editor and understand it.

It’s structured: headers (#), lists (-), code blocks (```) preserve document hierarchy.

It’s editable: unlike HTML or XML, you don’t need special tools to tweak it.

And crucially—it supports non-rendering comments like <!-- CHUNK -->, perfect for marking boundaries without affecting display.

Most importantly: Markdown is retrieval-ready.
When your text has clean structure, deciding where to chunk becomes intuitive.

NOTE: this last important clue is the result of the latest post-training strategies of the past 2 years. In fact, before that time, many models where unable to read markdown clearly!

docling repository and quick start
Introducing Tab 1: PDF → Markdown Converter

In our Gradio app, Tab 1 solves the PDF problem in one click.

Built with Docling, an open-source, high-fidelity document converter from IBM.

Docling simplifies document processing, parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the gen AI ecosystem.

This tab, is both a standalone app, and an orchestration element. By itself it will:

Accepts a PDF upload

Converts it to clean Markdown (preserving tables, lists, headings)

Saves the output as a .md file in your working directory

No cloud APIs. No hidden costs.

Just pure, local conversion.

Here’s what changes:

A scrambled table becomes a proper Markdown table with aligned columns.

Multi-column layouts are reflowed into logical reading order.

Headers/footers/page numbers are removed or isolated.

Bold/italic formatting is preserved as **text** or *text*.

The result? A document that’s at the same time readable and chunkable.

a needle in the haystack
Why This Matters for RAG

Let’s be clear: you cannot build a good RAG system on top of PDF noise.

Consider this financial snippet:

“Total Revenue: $1.2B (see footnote 3).”

In a raw PDF extract, “footnote 3” might appear 20 lines later—or not at all.
In Docling’s Markdown output, it’s cleanly attached:

Total Revenue: $1.2B[^3]

[^3]: Excludes one-time asset sales.


Now, when you chunk, you can keep the footnote with the figure—because the structure makes it obvious.

Compare that to recursive character splitting, which might give you:

Chunk 1: “Total Revenue: $1.2B (see footn”

Chunk 2: “ote 3).”

Useless.

A Real-World Example

I tested this on a 30-page EU regulatory document.

PyPDF2 output: 42 instances of “Art. 5” scattered randomly, tables turned into “| — | — |”, page numbers in the middle of sentences.

Docling → Markdown: clean article headings (## Article 5), intact definitions, tables as proper grids.

Then I asked: “What are the reporting requirements under Article 5?”

With PyPDF2 chunks: irrelevant fragments about Article 3, page numbers, and table borders.

With Markdown chunks: the full Article 5 section—retrieved in one go.

The difference wasn’t the retriever. It was the input.

Try It Yourself

Create a working directory for this project: we will use it for the next posts too. Mine is called docling.

Inside the docling directory, open a terminal window and create a virtual environment.

python -m venv venv

And then activate the virtual environment:

.\venv\Scripts\activate

We need few libraries to install:

pip install "docling[rapidocr]" requests gradio tiktoken

docling, with the rapidocr option is our markdown wizard. This will also install onnxruntime and torch (all required because rapidocr uses a slim and really performing small model to recognize the pdf layout and characters).

gradio is the main library for the user interface.

tiktoken and requests will be used in the next parts of the series.

Important note:

The first time you run the script you will get some warnings and the app will automatically download small OCR models and fonts. This is normal. The following use will be smooth.

OCR model auto download

Main imports:

import os
import json
from pathlib import Path
from docling.document_converter import DocumentConverter
import gradio as gr

# Constants
OUTPUT_DIR = Path.cwd()

# Ensure output dir exists
OUTPUT_DIR.mkdir(exist_ok=True)
from the homepage
The Gradio practical guide

Gradio is a super cool and simple GUI app builder. You can ideally launch an app with a single line of code, really!

If you don’t know anything about HTML, CSS and JS, this is the best starting point to build web app: running easily, over the network, with login features and handful Graphic elements.

Every action in gradio is performed through a function that has inputs and outputs. They can be gradio elements (a text-box, a slider, an image…) or variables. For this project we will declare all the functions outside the main User Interface.

Here is the first function, for Tab 1:

# ----------------------------
# Tab 1: PDF to Markdown
# ----------------------------
def convert_pdf_to_md(pdf_file):
if pdf_file is None:
return “❌ No file uploaded.”

try:
converter = DocumentConverter()
result = converter.convert(pdf_file.name)
md_content = result.document.export_to_markdown()

# Derive output filename
md_filename = Path(pdf_file.name).with_suffix(’.md’).name
md_path = OUTPUT_DIR / md_filename

with open(md_path, “w”, encoding=”utf-8”) as f:
f.write(md_content)

return f”✅ Successfully converted and saved as `{md_filename}`”
except Exception as e:
return f”❌ Error: {str(e)}”


As you can see it is quite simple: this function accept as an input a pdf file (in the form of path string - def convert_pdf_to_md(pdf_file)), convert it to markdown (md_content = result.document.export_to_markdown()), save the extracted markdown into a file (with the same name but different extension), and will return a string ( ✅ Successfully converted for good result, ❌ Error: {str(e)} for errors).

If 2+2 = 4… we will need in our Gradio application at least 3 elements: one for the input (the pdf file path) and one for the output (we display a message, so it should be a text box), and finally a trigger to activate the function (a Button).

Let’s go for it

# ----------------------------
# Gradio Interface
# ----------------------------
with gr.Blocks(title=”PDF to Markdown & Chunk Editor”) as demo:
gr.Markdown(”# 📄 PDF to Markdown Converter & Chunk Editor”)

with gr.Tabs():
# ---------------- Tab 1 ----------------
with gr.Tab(”📄 Convert PDF to Markdown”):
pdf_input = gr.File(label=”Upload PDF”, file_types=[”.pdf”])
convert_btn = gr.Button(”Convert to Markdown”)
convert_output = gr.Textbox(label=”Result”, interactive=False)

convert_btn.click(
fn=convert_pdf_to_md,
inputs=pdf_input,
outputs=convert_output
)

# Launch
if __name__ == “__main__”:
demo.launch()

The gradio app definition starts here: with gr.Blocks(title=”PDF to Markdown & Chunk Editor”) as demo:

Everything inside the with statement, become part of the user interface.

Notice that we immediately declare a group of TABs with gr.Tabs():

I think this is the most useful feature in gradio, because you can build standalone applications that can interact each others, with your progression.

And every time you complete one (for a specific purpose) you can test it independently from the other ones.

Really convenient!

the structure of gradio applications

You can see the 3 elements we were talking about: pdf_input, convert_btn and convert_output.

The trigger is given when you click convert_btn: gradio will call the function (fn=convert_pdf_to_md) with the elements we decided.

If you are worried to have missed any part of the code, click on the button below: I put it in my GitHub repository too.

Download docling_1.py

It is time to run

Save your file (mine is called doclinig_1.py) and from the terminal, with the venv activated run:

(venv) PS C:\FABIO-AI\_dociling> python .\doclinig_1.py
* Running on local URL: http://127.0.0.1:7860
2025-11-27 10:28:38,192 - INFO - HTTP Request: GET http://127.0.0.1:7860/gradio_api/startup-events “HTTP/1.1 200 OK”
2025-11-27 10:28:38,687 - INFO - HTTP Request: HEAD http://127.0.0.1:7860/ “HTTP/1.1 200 OK”
* To create a public link, set `share=True` in `launch()`.
2025-11-27 10:28:39,005 - INFO - HTTP Request: GET https://api.gradio.app/pkg-version “HTTP/1.1 200 OK”

Gradio will start a web server: clicking on the link http://127.0.0.1:7860 will open your default browser, ready with your application.

Test it yourself and see with your own eyes.

A simple conversion… with a Big impact

Now that you tried yourself… does it look complicated or impossible?

And the Gradio UI? Just a file upload and a button.

But the impact is massive: you’ve just detoxed your data.

You’re not converting documents. You’re preparing them for conversation.

Next week: Why you—not an algorithm—are the best person to draw chunk boundaries.

Until next time,

Fabio – ThePoorGPUguy




---


https://thepoorgpuguy.substack.com/p/vip-rag-that-works-mission-2

[VIP] RAG that works - Mission #2
From clear Markdown to human chunking
DEC 17, 2025
∙ PAID
Why domain experts, not algorithms, should draw the lines

Last week, we turned PDF chaos into Markdown clarity.

[VIP] RAG that works - Mission #1
10 DICEMBRE 2025
Read full story

Now comes the most important step: deciding where to split that Markdown into chunks.

Most tutorials hand this task to algorithms:

“Use RecursiveCharacterTextSplitter with chunk_size=512!”

“Let an LLM summarize each paragraph!”

But here’s the truth: no algorithm knows your document like you do.

You know that:

The footnote belongs with the paragraph above.

The case study illustrates the principle on the prior page.

The legal clause ends after the semicolon—not at token 512.

An LLM guesses. You know.

I tried to explore this issue in many articles: in my first Medium article about this topic, I even tried to apply a strategy where the summary and Table of contents were always be used in the retrieval. You can have a look at it!

The Problem with Auto-Chunking

Auto-splitters operate on tokens, not meaning.

They ask: “Have we hit 512 tokens yet?”
Not: “Does this sentence complete a thought?”

The result? Chunks like:

“The system shall comply with GDPR Article 17(1), which states that data subjects have the right to…”

…cut off mid-sentence because the token counter ran out.

Or worse—chunks that mix unrelated topics because they happened to fit in 512 tokens.

LLM-based chunking tries to fix this by asking the model: “Summarize this section.” But now you’ve:

Spent $0.02 per chunk

Introduced hallucination risk

Lost the original wording (which might contain key terms for BM25)

And for what? A “clean” summary that still might not align with your retrieval needs.

Introducing Tab 2: The Chunk Editor

In our Gradio app, Tab 2 puts you in control.

Here’s how it works:

Select a Markdown file (from Tab 1 output)

Edit the text in a large textbox

Insert <!-- CHUNK --> anywhere you want a boundary

Click “Process Chunks” → get a preview + structured JSON

You see the original document in a preview pane (so you don’t lose context).
You edit a copy (so the source stays pristine).
And when you process, you get:

Token count per chunk (using tiktoken)

A preview of each chunk’s first 100 characters

A JSON file with full metadata: {filename, chunk_index, token_count, text}

This is much more than automation: it is already human augmentation.
The tool handles the bookkeeping; you handle the judgment.

A Chunking Case Study

I tested this on a product manual for a medical device.

Auto-splitter result:
Chunk 12: “To sterilize the device, use…”
Chunk 13: “…autoclave at 121°C for 15 minutes. Warning: Do not use chemical sterilants.”

The warning—critical for safety—was separated from the instruction.

Manual chunk (mine):
Kept the full instruction + warning together, because I knew they were a single safety unit.

When a nurse queried: “How do I sterilize the device?”, the manual chunk returned the complete protocol—including the warning.

The auto-splitter? Only the first half.
That’s not just inaccurate—it’s dangerous.

Why This Scales

“But I have thousands of documents!” you say.

Fair. Manual chunking doesn’t scale to millions of pages.

But it does scale to your core documents—the ones that matter most:

Legal contracts

Product manuals

Compliance guidelines

Research reports

Chunk these once, well, and reuse them forever across:

BM25 retrieval

Semantic search

Hybrid systems

Fine-tuning datasets

And for bulk documents? Use your manually chunked examples as training data for a custom splitter.

Keep a Python library for the function and move GUI in the main app

This is my general philosophy in programming: to avoid reading a 1000 lines of code, better move the helper function in an external python file. We keep in the main app only the GUI loop logic (that will call the functions when we need them).

This approach works like a charm in our application. In fact we have different tabs, like they are standalone apps.

We can easily comment both the library of functions and the GUI main app clubbing the code by TABS.

It is something like this:

docling
├───RAGworkLIB.py
└───RAGwork_Mission2.py

RAGworkLIB.py will contain all the helper functions, organized by TAB

RAGwork_Mission2.py will have all the GUI logic

For today we re-arrange the library python file: in Mission 2.1 we will go through the GUI App.

But… if you cannot wait out of curiosity (or excitement), you can try directly with the files from my GitHub repo related to Mission #2.

GitHub Repo for Mission #2

Requirements

Considering you have the same project directory docling, and already installed the Mission #1 libraries: with the venv activated run:

pip install openai

And that is all.

We need OpenAI library not for ChatGPT! We need to access a local model with llama.cpp server, to provide us the summary and main topics of the markdown files we want to chunk.

In fact, in my opinion, one chunk must always be dedicated to this initial overview of the content of the document as a whole!

Our personal library

In this section we will organize both the existing functions from Mission #1 (the ones related to the document conversion to markdown with docling) and the new functions required to analyze the document with a Local AI help, count the tokens and process the chunks.

Create a new python file: mine is called RAGworkLIB.py.

Let’s start with importing libraries and adding the old functions (the ones for TAB 1)

import os
import json
from pathlib import Path
from docling.document_converter import DocumentConverter
import gradio as gr

# Mission 2 imports
import subprocess
import threading
import time
import requests
import openai
from typing import Optional
import tiktoken

The constants below are all new exception for OUTPUT_DIR.

We set here some important global variables: the encoding used for the tiktoken, the chunk delimiter (that will tell our personal splitter where to do the work), the local server address (for llama.cpp server API endpoints) and one instance of the LLMserver (that we will start and stop only for the purpose of summary/main topics).

# Constants
OUTPUT_DIR = Path.cwd() # from Mission 1
ENCODING_NAME = “cl100k_base”
CHUNK_DELIMITER = “<!-- CHUNK -->”
API_BASE = “http://localhost:8080/v1”
# Global server variable
LLMserver = None

# Initialize tokenizer once
tokenizer = tiktoken.get_encoding(ENCODING_NAME)

Then we can insert the existing function used in Mission #1 to convert PDF documents into markdown (and save them in the project directory) with docling:

# ----------------------------
# TAB 1 Functions
# ----------------------------

def convert_pdf_to_md(pdf_file):
if pdf_file is None:
return “❌ No file uploaded.”

try:
converter = DocumentConverter()
result = converter.convert(pdf_file.name)
md_content = result.document.export_to_markdown()

# Derive output filename
md_filename = Path(pdf_file.name).with_suffix(’.md’).name
md_path = OUTPUT_DIR / md_filename

with open(md_path, “w”, encoding=”utf-8”) as f:
f.write(md_content)

return f”✅ Successfully converted and saved as `{md_filename}`”
except Exception as e:
return f”❌ Error: {str(e)}”

From now on, we will declare the functions relevant to Human Chunkning!

To keep you motivated, here how the TAB2 will look as soon as we finish (part 2 too)

Helper Functions to create chunks and support Local AI generation.

Our TAB2 contains 3 main panels:

left is dedicated to Document exploration, with an optional AI step that will read the document and generate Summary and relevant topics

center is showing the original markdown, rendered as HTML

right panel is our editor, where we can add content and set the limits for the chunking: not with a fixed strategy (character count, paragraphs or tokens) but by topic or relevance between parts with consistent content.

Let’s go through them 1 by 1:

# ----------------------------
# TAB 2 Functions
# ----------------------------

def list_markdown_files():
return [f.name for f in OUTPUT_DIR.glob(”*.md”)]

def load_markdown_file(filename):
if not filename:
return “”, “”
try:
with open(OUTPUT_DIR / filename, “r”, encoding=”utf-8”) as f:
content = f.read()
return content, content
except Exception as e:
return f”Error loading file: {e}”, “”

def update_token_count(md_text):
if not md_text:
return “0”
return str(count_tokens(md_text))

We start the list with easy functions:

list_markdown_files() simply return a python list of all the markdown files in the OUTPUT_DIR (that is the directory where we save in TAB1 the markdown files converted from PDF).
💡 note how return [f.name for f in OUTPUT_DIR.glob(”*.md”)] use the return with [ ] to create the list!

load_markdown_file(filename) load one markdown file ready to be displayed as rendered markdown and as plain text (for chunk manual delimiting)
💡 note how return “”, “” have 2 arguments: we need one for each gradio element we will use to render that text…. even if it is empty ““ !

update_token_count(md_text) this function is dedicated to update the token count widget.

Next one is to process the chunks after we decided where to put the limits:

Here the code (in text): the process_chunks(md_text, filename) function takes 2 arguments. Te text from the editable right panel (where we can add, remove and set chunks limits) and the name of the json file where to save our chunks.

def process_chunks(md_text, filename):
if not md_text or not filename:
return “⚠️ No content or filename.”, None

raw_chunks = md_text.split(CHUNK_DELIMITER)
chunks = []
total_tokens = 0
preview_lines = []

for i, chunk_text in enumerate(raw_chunks):
chunk_text = chunk_text.strip()
if not chunk_text:
continue

token_count = count_tokens(chunk_text)
total_tokens += token_count

chunk_meta = {
“filename”: filename,
“chunk_index”: i,
“token_count”: token_count,
“text”: chunk_text
}
chunks.append(chunk_meta)

# Preview line: show first 100 chars + token count
preview = f”[Chunk {i}] ({token_count} tokens)\n{chunk_text[:100]}{’...’ if len(chunk_text) > 100 else ‘’}”
preview_lines.append(preview)

# Build preview display
display_text = (
f”✅ Total chunks: {len(chunks)} | Total tokens: {total_tokens}\n\n”
+ (”\n” + “=”*60 + “\n”).join(preview_lines)
)

# Save as JSON
json_path = OUTPUT_DIR / f”{Path(filename).stem}_chunks.json”
with open(json_path, “w”, encoding=”utf-8”) as f:
json.dump(chunks, f, indent=2, ensure_ascii=False)

return display_text, str(json_path)

We simply use the string method to split text at a specific delimiter (for us is CHUNK_DELIMITER that we defined as CHUNK_DELIMITER = “<!-- CHUNK -->” in the constants section.

We add as many metadata possible (like token count for each chunk) and finally we display the results and save the json file

# Save as JSON
json_path = OUTPUT_DIR / f”{Path(filename).stem}_chunks.json”
with open(json_path, “w”, encoding=”utf-8”) as f:
json.dump(chunks, f, indent=2, ensure_ascii=False)

That is all for this week.

In the next Mission #2.1 we will close the Library section with the LLama.CPP Server functions, and move to the GUI!

The philosophy: Intentional over Automatic

We rely blindly to automation (maybe because we are a little too lazy…), but not everything should be automated.

Chunking is a semantic decision, not a syntactic one. It requires understanding of:

Domain logic

User intent

Risk (what happens if this is split wrong?)

That’s why the best RAG systems I’ve seen aren’t the ones with the fanciest embeddings—they’re the ones where a human carefully prepared the data.

An LLM sees tokens. You see meaning. Trust your judgment.

Next week: How to inspect your chunks—because if you can’t see your data, you don’t own your RAG system.

Until next time,

Fabio – ThePoorGPUguy




---


https://thepoorgpuguy.substack.com/p/vip-rag-that-works-mission-21

[VIP] RAG that works - Mission #2.1
From PDF chaos to clear Markdown - the Gradio TAB interface
DEC 23, 2025
∙ PAID

Last week we ended up with ALMOST all the helper function required for our TAB2. It is a gradio application that let you manually decide where to set the chunk limits.

And the main reason behind it…

Chunking is a semantic decision, not a syntactic one.

It requires understanding of:

Domain logic

User intent

Risk (what happens if this is split wrong?)

That’s why the best RAG systems I’ve seen aren’t the ones with the fanciest embeddings—they’re the ones where a human carefully prepared the data.

An LLM sees tokens. You see meaning. Trust your judgment.

Today we go on with the last helper functions (optionally used, if you want a local LLM to extract summary and Table of Contents from the markdown text).

And then we move to the GUI

GitHub repository for Mission #2 code

The project structure

It is something like this:

docling
├───RAGworkLIB.py
└───RAGwork_Mission2.py

RAGworkLIB.py will contain all the helper functions, organized by TAB

RAGwork_Mission2.py will have all the GUI logic

You can find all the files from my GitHub repo related to Mission #2.

GitHub Repo for Mission #2

Llama.cpp server

The last 4 functions are related to the start/stop of the llama-server and the API calls to the local AI to get the summary and ToC. We will use a small, reliable and accurate model.

I will focus the explanations on the API calls ones.

But first of all, you need to download the GGUF model and the llama.cpp binaries in the same project folder docling.

⬇️ Download the RWKV-7 Model (GGUF Format)

Go to the official RWKV model repository or Hugging Face (as linked in your README).

Download the gemma-3-270m-it model in GGUF format (e.g., gemma-3-270m-it-Q8_0.gguf).


Download GGUF file

Place the .gguf file in the root of your project folder.

💡 Tip: Quantized versions like Q8 offer best quality for local use.

⚙️ Download llama.cpp Binaries

Download the latest llama.cpp binaries (e.g., llama-cli, llama-server) for your OS from:

https://github.com/ggerganov/llama.cpp/releases

the release at time of writing is b7342 Downloads clicking here

Extract and place the binaries (llama-server or equivalent) in the same directory as your Python script (docling).

The app assumes llama.cpp tools are available locally to run the GGUF model.

Functions to load/stop the llama.cpp server

This function check only if the server is running. I will make an API call to the model endpoint to get some basic information

The next one start the LLM server for our local AI. It will try to start a new terminal window, running llama-server.exe and the gemma-3-270m-it-Q8_0.gguf for the project directory (this is why we download them into the docling directory).

Finally the last one is used to stop the process running the LLM server. We use the instance of LLMserver that contains the RAM Process ID, to precisely kill/stop only that specific process.

Functions for the API calls

These functions may look very complicated, but they are simply send prompt in the ChatML format to the llama-server API endpoints. We do so, to get the Summary and Table Of Contents.

It is optional to run them: in fact it is my personal opinion and best practice to always include a chunk containing the overall ideas of a document. If you decide that it is irrelevant… you can skip the process.

The first function is a CULT… I mean you should have seen me using it already in several other projects:

# ----------------------------
# TAB 2 - Analysis Functions
# ----------------------------
def genOS_chat(client, user_prompt, history, stops):
“”“Send prompt to local model and get response - with better error handling”“”
try:
history.append({”role”: “user”, “content”: user_prompt})

completion = client.chat.completions.create(
model=”local-model”,
messages=history,
temperature=0.3,
frequency_penalty=1.45,
max_tokens=800,
stop=stops
)
response = completion.choices[0].message.content
history.append({”role”: “assistant”, “content”: response})
return history
except Exception as e:
print(f”Chat API error: {str(e)}”)
history.append({”role”: “assistant”, “content”: f”Error: {str(e)}”})
return history

It sends Chat history to the local AI, and return the very same Chat history with the Assistant reply included.

The next one takes the markdown content of the document and makes API call with our genOS_chat() function to get back both the summary and the and 5 most important topics.

Since our gradio app is also showing the progress status of this document analysis, I had to create 1 more function dedicated only to this task.

The code looks complicated: in reality we are deciding at each step, how much progress to display.

In simple terms, this is the orchestrator function that calls all the others when we will click on “Process Document” button.

That is all for the library RAGworkLIB.py.

Let’s move to the GUI inside RAGwork_Mission2.py

The GUI with TABS

This is my general philosophy in programming: to avoid reading a 1000 lines of code, better move the helper function in an external python file. We keep in the main app only the GUI loop logic (that will call the functions when we need them).

This approach works like a charm in our application. In fact we have different tabs, like they are standalone apps.

We can easily comment both the library of functions and the GUI main app clubbing the code by TABS.

Let’s see what is inside RAGwork_Mission2.py

We start from the imports

You may notice that we are importing something from a library called RAGworkLIB… ring any bell?

Because our personal library file is in the same project directory, and it is called RAGworkLIB.py, we can import the entire file or the classes and functions inside it, simply with those few lines.

Here below the backbone structure of the gradio interface

Imagine you can simply add a new with gr.Tab(“Something new”): all the time. It means that each gr.Tab is an application that can (or cannot) work by itself.

You only need to add a new LEGO block the final masterpiece!

And the effect of this structure is something like this, where rows and columns are rendered according to a grid structure.

Tab 1, in fact, is exactly the same of Mission #1.

Moving on TAB 2…

# ----------------------------
# Gradio Interface
# ----------------------------
with gr.Blocks(title="PDF to Markdown & Chunk Editor") as demo:
gr.Markdown("# 📄 PDF to Markdown Converter & Chunk Editor")


with gr.Tabs():
# ---------------- Tab 1 ----------------
with gr.Tab("📄 Convert PDF to Markdown"):
pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
convert_btn = gr.Button("Convert to Markdown")
convert_output = gr.Textbox(label="Result", interactive=False)


convert_btn.click(
fn=convert_pdf_to_md,
inputs=pdf_input,
outputs=convert_output
)


# ---------------- Tab 2 ----------------
with gr.Tab("✂️ Chunk Editor"):
with gr.Row():
# Left column for stats and analysis
with gr.Column(scale=1):
total_tokens_display = gr.Textbox(label="Total Document Tokens", interactive=False)
summarize_btn = gr.Button("🔍 Start Document Analysis")
server_status = gr.Textbox(label="Server Status", interactive=False, value="Server not started")
analysis_status = gr.Textbox(label="Analysis Status", interactive=False, value="Ready to analyze")
summary_output = gr.TextArea(label="Document Summary", lines=10)
topics_output = gr.TextArea(label="Main Topics (5)", lines=7, value="", placeholder="Topics will appear here after analysis")
stop_server_btn = gr.Button("🛑 Stop Server", variant="stop")

# Right column for file selection and editing
with gr.Column(scale=2):
with gr.Row():
md_file_dropdown = gr.Dropdown(
choices=list_markdown_files(),
label="Select Markdown File",
interactive=True
)
refresh_btn = gr.Button("🔄 Refresh List")


with gr.Row():
original_md_preview = gr.Markdown(label="Original Preview")
editable_md = gr.Textbox(
label="Editable Markdown (Insert chunk breaks with <!-- CHUNK -->)",
lines=20,
max_lines=30
)


selected_filename = gr.State() # to track current file


def on_file_select(filename):
content, _ = load_markdown_file(filename)
token_count = update_token_count(content)
return content, content, filename, token_count


md_file_dropdown.change(
fn=on_file_select,
inputs=md_file_dropdown,
outputs=[editable_md, original_md_preview, selected_filename, total_tokens_display]
)


refresh_btn.click(
fn=lambda: gr.update(choices=list_markdown_files()),
inputs=None,
outputs=md_file_dropdown
)


process_btn = gr.Button("✂️ Process Chunks")
chunks_output = gr.Textbox(label="Processed Chunks (Preview)", lines=10)
download_json = gr.File(label="Download Chunks as JSON", visible=True)


process_btn.click(
fn=process_chunks,
inputs=[editable_md, selected_filename],
outputs=[chunks_output, download_json]
)

# Connect analysis button
def analysis_wrapper(doc_text):
# Create a progress object
progress = gr.Progress()
# Process with progress and yield the results
for status, summary, topics in process_for_analysis(doc_text, progress):
yield status, summary, topics

summarize_btn.click(
fn=analysis_wrapper,
inputs=editable_md,
outputs=[analysis_status, summary_output, topics_output],
api_name="analyze_document"
)


# Connect stop server button
stop_server_btn.click(
fn=stop_llm_server,
outputs=server_status
)


# Start server status update
def server_status_check():
global LLMserver
if LLMserver is None:
return "Server not started"

if LLMserver.poll() is None:
return f"Server running (PID: {LLMserver.pid})"
else:
return "Server stopped"


# Update server status periodically
demo.load(
fn=lambda: gr.Textbox(value=server_status_check, interactive=False),
outputs=server_status
)

view raw
tab2_gradio_docling.py hosted with ❤ by GitHub

Remember the main philosophy of gradio?

Each element can have a trigger to start an action

every action is handled by a function

every function uses input outputs arguments that can be either variables or widgets (text areas, scroller, images…)

For instance, let’s see one of the functions activated by a button click action:

When the Button is pressed, we call the function analysis_wrapper, with our editable_md gradio widget as an input, and with 3 outputs.

This also means that the original python function is expecting exactly 1 input and returning 3 outputs.

In our Gradio app, this line:

summarize_btn.click(
fn=analysis_wrapper,
inputs=editable_md,
outputs=[analysis_status, summary_output, topics_output],
api_name=”analyze_document”
)


uses the api_name=”analyze_document” parameter to assign a custom name to the API endpoint that Gradio automatically creates for this function when the app is launched.

Gradio automatically exposes every event handler (like button clicks) as a REST API endpoint when you run demo.launch(). By default, Gradio generates a generic name for this endpoint (like /predict or /predict_1, etc.), but you can use api_name to give it a meaningful, predictable, and stable name.

So with api_name=”analyze_document”, Gradio will create a POST endpoint at:

http://localhost:7860/api/analyze_document


This endpoint:

Accepts JSON input matching your inputs (in this case, the content of editable_md)

Runs your analysis_wrapper function

Returns JSON with the values for analysis_status, summary_output, and topics_output

Finally, we call the main run:

# Launch
if __name__ == “__main__”:
OUTPUT_DIR.mkdir(exist_ok=True)
demo.launch()

How to run the app

From the main project folder, with the venv activated in the terminal, run..

python .\RAGwork_Mission2.py

And you sill see something like this…

Conclusions

In TAB1 you will pick a PDF and convert is smartly into well formatted Markdown.

In TAB2 you will be able to get AI generated summary and table of content and chunk with your rules the documents.

In the next weeks, after Christmas holidays, we will keep on going with Keyword search (BM25), semantic search (Cosine Similarity) and the final RAG Q&A using fused search.

Until next time,

Fabio – ThePoorGPUguy


---



















