## _**Your Tabs are lying to you**_ 

_How I tamed my 70-tab chaos with a 100-line Python script, and finally stopped pretending I’d “read those later”_ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 10 min read · Feb 8, 2026_ 

**==> picture [511 x 297] intentionally omitted <==**

I need to confess something uncomfortable… 

## _I’m a tab hoarder._ 

Not the cute kind with three neatly organized tabs. I’m talking _70+ tabs_ — collapsed into groups with hopeful names like “Pixazo” and “HF_news” so I 

News articles from Tuesday. GitHub repos I’ll “explore later.” That Medium post about _ByteShape models_ bookmarked next to llama.cpp documentation. Three different tabs for the same recipe because Chrome froze mid-scroll and I just… opened a new one. 

## Sound familiar? 

I believed the lie that _saving_ tabs equals _processing_ them. Browser extensions promised me to “group” or “archive” my tabs — but that’s just moving digital clutter to a different shelf. The real problem of course is not the tabs themselves. It’s that we can mistake activity for progress. 

Opening a tab feels productive. But unless we actually _digest_ what we’ve seen? It’s just noise. 

**==> picture [511 x 304] intentionally omitted <==**

## _**The Breaking Point: 2.5GB of RAM and Zero Clarity**_ 

Last Tuesday, Chrome was using 2.5GB of RAM just for my browsing session. My laptop fan sounded like a jet engine. I had six tab groups collapsed — each one a monument to good intentions I’d abandoned. 

And the brutal truth… I finally admitted while waiting 45 seconds for a tab to load: _None of those tabs represented actual learning. Just digital anxiety._ 

I’d spent an hour that morning opening tabs about local AI tools — but could _one_ I tell you concrete thing I’d learned? Nope. Just the vague feeling of “I should read more of these.” 

That’s when I snapped. I Googled: ”chrome extension that track daily browser visits time reading and can extract website content” (yes, I literally searched that exact phrase — you can see it in my JSON export). 

And that’s how I fell down a _rabbit hole_ that actually led somewhere. 

## _**A GitHub Rabbit Hole that actually paid off**_ 

I found a tiny GitHub repo called “Browsing Digest” — a Python script that promised to generate a _daily summary_ of your browsing using a local AI model. No cloud uploads. No tracking. Just a clean 2-minute digest of what you explored. 

## _**GitHub - ManashWrites/I-Made-an-AI-That-Summarizes-MyDaily-Browsing-Into-a-2-Minute-Digest**_ 

_Contribute to ManashWrites/I-Made-an-AI-That-Summarizes-MyDaily-Browsing-Into-a-2-Minute-Digest development by…_ 

**==> picture [121 x 92] intentionally omitted <==**

**==> picture [121 x 34] intentionally omitted <==**

The app is quite simple, and run in the Terminal window: 

- you install a chrome extension that keeps track of your browsing tabs, time spent on those tabs, and content. 

- at one point you export the daily logs from the extension into a `json` file, into the directory of the repository cloned on your PC 

- `ollama` 

- you fire up your local AI engine (the original app wants , but I really don’y like it), in my case `llama.cpp server` 

- you run the python script with the exported `json` as an argument. 

- You get a brand new markdown file with the daily digest of your web browsing activity 

I cloned the Repository immediately. The repo said it was easy… but on my Windows laptop I got a total meltdown with this error: 

```
UnicodeEncodeError: 'charmap' codec can't encode character '\u200e'...
```

## Translation for non-coders: 

_”Windows choked on a special character (like a left-to-right mark from an Arabic news site) when trying to send my browsing history to the AI.”_ 

I almost gave up. Another “Linux-only” tool that assumes everyone codes on 

a MacBook. But then I had a thought that changed everything: What if I used 

## AI to fix this AI tool? 

## _**The secret Google LLM nobody is talking about.**_ 

_T5Gemma series of encoder-decoder models: the smart upgrade of the T5 family_ 

_generativeai.pub_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**Why JSON keys with spaces broke my brain (and how we fixed it)**_ 

First surprise: my browser extension exported _malformed JSON_ . Keys had 

trailing spaces like `"date "` instead of `"date"` . Python couldn’t find the data it needed. 

Here’s what the raw JSON looked like (I’ve seen this in my own exports!): 

```
{
"date ": "2026-02-06 ",   // ← See the space after "date"?
"pages ": [ ... ]         // ← And here?
}
```

Instead of manually fixing dozens of files, I asked my AI assistant: 

_”How can I automatically repair JSON files where keys have accidental spaces?”_ 

It gave me this elegant recursive function: 

`def normalize_json_keys(obj): """Fix keys like "date " → "date" automatically""" if isinstance(obj, dict): return { key.strip(): normalize_json_keys(value)  # ← strip whitespace from k for key, value in obj.items() } elif isinstance(obj, list): return [normalize_json_keys(item) for item in obj] elif isinstance(obj, str): return obj.strip()  # ← also clean string values else: return obj`   

## Why this matters for beginners: 

You don’t need to understand recursion deeply to _use_ this. Just know: _”This function walks through my entire JSON file and quietly fixes messy keys/values.”_ It’s a digital cleaner that works while you sleep. 

## When the script runs, it: 

## 1. Detects malformed keys automatically 

## 2. Creates a `.json.bak` backup (so you never lose data) 

3. Repairs the file silently 

## 4. Continues processing 

No more manual cleanup. No more “why won’t this work?!” frustration. 

## _**How the script loads and prepares your browsing data**_ 

Once the JSON is repaired, the script does two important things: 

## 1. Loads your browsing history 

The `load_browsing_data()` function reads your JSON export and validates it has the required structure ( `date` and `pages` ). If your extension exports malformed data (like mine did), it repairs it silently—no crashing, no error messages that make you want to quit coding forever. 

## 2. Prepares content for the AI 

The `prepare_content_for_llm()` function: 

Sorts pages by timestamp (so your digest flows chronologically) 

- Limits each page’s content to 1,000 characters (prevents overwhelming the AI) 

- Respects a 4,000-token budget (so summaries stay focused) 

Formats everything cleanly with timestamps and domains 

```
# Simplified version of the preparation logic
for page in pages:
    title = page.get('title', 'Untitled')
    domain = page.get('domain', 'Unknown')
''
    content = page.get('content', )[:1000]  # ← Critical truncation!
    page_text = f"[{time}] {title}\nSource: {domain}\nContent: {content}"
```

- `# ... then add to content if under token budget` 

This is a thoughtful constraint. The AI doesn’t need _everything_ you saw. It needs the _essence_ . 

## _**Argparse: your friendly Command-Line butler**_ 

everything. Here’s the simple truth: `argparse` is Python’s built-in tool for making scripts feel like professional command-line tools. 

## Without it, you’d need separate scripts for every variation: 

```
summarize_default.py
```

```
summarize_custom_model.py
```

```
summarize_custom_output.py
```

## With `argparse` , one script handles all cases elegantly: 

```
parser = argparse.ArgumentParser(description="Generate a browsing digest")
parser.add_argument("input_file", help="JSON file from browser extension")
parser.add_argument("--model", "-m", default="local-model", help="AI model to us
parser.add_argument("--output", "-o", help="Custom output filename")
args = parser.parse_args()
```

  

## Now you can run: 

```
python summarize.py my-data.json          # Simple default
python summarize.py my-data.json -m qwen2.5# Custom model
python summarize.py my-data.json -o today.md # Custom output
```

## Why you should love this: 

## No need to edit the script for small changes 

Built-in `--help` flag shows all options instantly ( `python summarize.py -- help` ) 

Feels like using real tools (because it _is_ real tools) 

It’s the difference between a fragile prototype and something you’ll actually _use_ daily. 

## _**The Two-Line Windows fix that felt like a magic spell**_ 

Remember that Unicode error? 

I asked Qwen to tell me something about it for me, and how to make it work. 

The fix was shockingly simple — just two lines added to the subprocess call: 

`# BEFORE (breaks on Windows): result = subprocess.run( ["ollama", "run", model], input=prompt, capture_output=True, text=True,  #` ❌ `Windows chokes here timeout=120 ) # AFTER (works everywhere): result = subprocess.run( ["ollama", "run", model], input=prompt, capture_output=True, text=True, encoding='utf-8',      #` ✅ `Tell Windows: "Use modern text encoding" errors='replace',      #` ✅ `If a character fails, skip it gracefully timeout=120 )` 

Those two lines say: _”Hey Windows, please handle text like the rest of the world does.”_ No quantum physics degree required. Just explicit instructions where Windows needs them. 

Later, I switched to llama.cpp (more on that below), which uses HTTP requests instead of subprocess calls — eliminating this entire class of errors. 

But that two-line fix taught me something profound: most “Windows incompatibility” is just missing explicit instructions. 

_**GitHub - fabiomatricardi/your-daily-browsing-digest: summarize tour daily browsing activity locally…**_ 

_summarize tour daily browsing activity locally with llama.cpp server and chrome extension …_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**Why I switched from Ollama to llama.cpp (and why you might too)**_ 

Once the Windows issues were solved, I wanted more control. Ollama is great, but it’s a black box. 

The original GitHub Repository was using as local AI engine, Ollama. I reinstalled it on my computer only to test the original script and to fix it. 

But I really don’t like it. So I deleted all the models and Ollama itself, and moved on with Qwen to modify the existing working repo with a new AI engine. 

lightweight, transparent way to run AI models locally with an OpenAIcompatible API. 

The refactor was surprisingly simple. Instead of calling Ollama via command line: 

```
# Old way(Ollama CLI):
subprocess.run(["ollama", "run", model], input=prompt...)
```

## We now make a clean HTTP request: 

```
# New way(llama.cpp API):
response = requests.post(
"http://localhost:8080/v1/chat/completions",
    json={
"model": "local-model",
"messages": [{"role": "user", "content": prompt}]
    }
)
```

## Why this matters for mid-life learners like us: 

llama.cpp uses less RAM (runs smoothly on modest laptops — critical when Chrome’s already eating 2.5GB!) 

You control the server process explicitly ( `./llama-server.exe -m mymodel.gguf` ) 

- The API approach avoids all those pesky Windows encoding issues entirely 

It’s the same interface used by ChatGPT — so skills transfer directly 

I now run a 3B-parameter model on my 8GB RAM laptop while Chrome chugs along with 50 tabs. 

## _**Your Turn: Reclaim Your Attention in 15 Minutes**_ 

Prerequisites: 

## Python 3.8+ installed (python.org) 

`pip install requests` (one command) 

llama.cpp server running locally 

Steps: 

1)Get the complete script here (all fixes included) 

2)Install the “Browsing Digest” Chrome extension to export your history as JSON 

3)Download the ZIP archive for Windows of llama.cpp: as of today, the latest version is b7966 . Download the file and unzip it in the same directory of the Repo. 

4)Download a very good Small Model: this time I suggest you to go for the 

- – - - - latest mistralai_Ministral 3 3B Instruct 2512 Q4_K_M.gguf that you can get from the Bartowski Hugging Face Repository. Put it in the same directory of llama.cpp binaries. 

_click on the button to download the AI model_ 

## 5)Start llama.cpp server: 

```
./llama-server.exe -m mistralai_Ministral-3-3B-Instruct-2512-Q4_K_M.gguf -c 8192
```

  

## 6)Run the script: 

```
python dailyBrowsing_llamaCPP.py your-browsing-data.json
```

## You’ll get a clean `digest-2026-02-07.md` file with sections like: 

- 📚 `Browsing Digest - 2026-02-07` 

## **`**Main Themes**`** 

- `Local AI tooling for personal knowledge management` 

- `Sustainable computing practices on modest hardware` 

## **`**Key Insights**`** 

- `Tab hoarding correlates with decision fatigue (not productivity)` 

- `llama.cpp runs 7B models smoothly on 8GB RAM laptops` 

- `JSON exports often contain hidden whitespace bugs-automate repairs!` 

No cloud. No tracking. Just your own thoughts, reflected back clearly. 

## _**The real discovery: AI as a patient coding partner**_ 

What started as a quest to tame tab chaos became something deeper: proof that AI can be a judgment-free coding partner for mid-life learners. 

At 49, I don’t have time for “figure it out yourself” culture. When I hit that Unicode error, an AI didn’t mock my Windows setup or assume I knew about text encodings. It: 

## 1. Explained _why_ it happened in plain English 

## 2. Showed me _exactly_ where to add two lines 

## 3. Warned me about edge cases (”What if the character still fails? Use 

`errors='replace'` “) 

That’s the future I want: AI that meets us where we are — not as replacements for my human curiosity, but as amplifiers of it. 

_Open in app_ 

Your tabs don’t have to be chaos. With a little help — from both human ingenuity and AI patience — we can turn digital noise into daily ordered list. 

And honestly? 

Closing those 70 tabs after reading my first digest felt like taking a deep breath after holding it for hours. 

_P.S. The script is 100% offline — your browsing history never leaves your machine. Because privacy is something I will not give up on._ 

*P.P.S. If you try this and hit a wall, reply in the comments section. I’ll help you debug it. We’re all learning together. 

_Local Gpt Your Ai Your Rules Python4ai Thepoorgpuguy Ai Coding Assistant_ 

