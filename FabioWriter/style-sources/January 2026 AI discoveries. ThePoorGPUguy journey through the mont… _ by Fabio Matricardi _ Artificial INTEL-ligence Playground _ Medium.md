## _**January 2026 AI discoveries**_ 

_ThePoorGPUguy journey through the month: ideas, projects and practical tips. Free image generation and blazing fast llama.cpp with 30B model on my crappy Laptop._ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 9 min read · Jan 24, 2026_ 

**==> picture [511 x 297] intentionally omitted <==**

_image generated with https://github.com/fabiomatricardi/Pixazo-free-image-generation_ 

I have been exploring a lot in the past month, but I have not time to write down properly an article for every new know-how I would like to share. So today I want at least to give you some bites 😁 . 

```
1) Opencode
```

- `2) Chocolatey - one tool to rule them all!` 

```
3) Llama.cpp optimization for CPU poor guy
```

```
4) Free image generation API - Pixazo.ai
```

If you have a poor GPU laptop (like me) but you want to use AI locally with python to run useful projects (for yourself), you are the reader, and I am writing for you. Step by step project, learning python and AI while building something practical 

But… as you may know, writing is a hobby for me: I take it seriously, but I work already 12 hours a day offshore (and write in the so called free time…). 

That being said, I cannot but share with you at least a preview of what is about to come: be certain that a proper article will be published soon. 

Without further ado… let’s see what AI new entries in this month have brought to us! 

## _**1) Opencode**_ 

I finally tried `opencode` . My personal rejection to whatever was including the word agents was removed as soon as I watched a youtube video about it. 

OpenCode is an open source agent that helps you write and run code with any AI model. It’s available as a terminal-based interface, desktop app, or IDE extension. 

Opencode explores your existing project or start a new project and run the programming, testing and documentation for you. It can read existing files, create new files and directories, install dependencies and test its own code. 

_You have just hired… for free a programmer._ 

An article will come soon here on Medium, explaining you from A to Z how to start using it with Zero costs. In fact I will show you how to use opencode with the free available Zen models (grok-1, GML-4.7 and so on), with your free Openrouter.ai API key, and even with llama.cpp running your model locally. 

## _**2) Chocolatey — one tool to rule them all!**_ 

If you build Python and AI applications on Windows, you already know the pattern: install Python, then Git, then VS Code or Sublime, then CUDA, then some obscure runtime for an LLM backend. Each one has its own website, download link, installer, and update process. 

On Linux, package managers solve this problem. On Windows, Chocolatey brings that same idea to the terminal: one command-line interface to install, upgrade, and remove most of the tools you care about. 

As I told you, in the past weeks I built several personal apps in python. They are useful to me. And I did it with the help of AI. To do this you need tools (back to the above section…) 

`opencode` (the coder app that create code and all development files by itself)? 

`docker` (to have your local AI able to use web-search) 

a good code editor (maybe with AI assistant plugins) 

You can read more here: 

## _**Chocolatey for Python & AI enthusiasts: how to turn Windows into your in-house developer...**_ 

_How a terminal-first package manager can automate your tools, tame your installs, and make reproducible AI environments…_ 

_ai.gopubby.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**3) Llama.cpp optimization for CPU poor guy**_ 

You know that I am a big fan of llama.cpp, and that to me this project is the biggest innovation in Generative AI for the past 2 years. 

run a I discovered few days ago a team of crazy engineers that managed to 30B Qwen Model with a Raspberry Pi… in Real Time! 

A part from the Mission Impossible feat, the ByteShape team discovered that for CPU some quantization formats are slowing the inference time quite a lot! For example, a standard Q4 model can be slower than a Q5 (that is bigger). Using the same principle, they developed special quants that are Memory efficient. 

I couldn’t believe the statements from ByteShape guys, so I decided to test them myself, and I measured the performances comparing the scores on my 

I will write a full article soon, for now follow me in few steps to test it on your PC too in 5 minutes. 

On their Hugging Face Repository, you can find the special quantization GGUF files ready for the miracle: I tested both Qwen3–4B-Instruct-2507GGUF and Qwen3–30B-A3B-Instruct-2507-GGUF. 

Download the latest llama.cpp binaries for Windows in X64 (no GPU support or Vulkan driver support). extract them in one directory. 

In the same directory download the standard Q4_K_M from the official repositories, and: 

– - - - - - Qwen3 30B A3B Instruct 2507 Q3_K_S 2.70bpw.gguf 

– - - - - Qwen3 4B Instruct 2507 Q3_K_S 2.77bpw.gguf 

The comparison is between the standard Q4_K_M and their special BitPerWeight quantization. For both of them I took screenshots from the llama.cpp web interface using this simple prompt: 

_explain what is science in 5 paragraphs_ 

from the terminal, we ensure flash-attention is on, no GPU layers and context length of 8192 tokens. 

```
#normal quants
```

```
.\llama-server.exe -m Qwen_Qwen3-4B-Instruct-2507-Q6_K.gguf -c 8192 -fa on -ngl
```

```
.\llama-server.exe -m Qwen3-4B-Instruct-2507-Q3_K_S-2.77bpw.gguf  -c 8192 -fa on
```

## _**Qwen_Qwen3–4B-Instruct-2507-Q6_K.gguf**_ 

 

 

prefill: 46 tokens per second 

generation: 10 tokens per second 

## _**Qwen3–4B-Instruct-2507-Q3_K_S-2.77bpw.gguf**_ 

prefill: 64 tokens per second 

generation: 21 tokens per second 

In relation to the huge 30B-A3B, I only wanted to test how good was in prefill: this is a huge model so I was expecting a big lag time to first token, after reading a long prompt. And I have only 16Gb of RAM so I cannot accomodate a 18.7 Gb of GGUF there! 

See yourself: 

```
.\llama-server.exe -m Qwen3-30B-A3B-Instruct-2507-Q3_K_S-2.70bpw.gguf -c 8192 -f
```

_530 tokens in the prompt, prefill in only 8 seconds!_ 

Generation 

_27 tokens per second_ 

If you want to know more about llama.cpp beauties, check this article here: 

## _**llama.CPP restyle is the workshop for your Local AI**_ 

_From LLM routing to full working Chat application: all in one ZIP file. And here is how._ 

_medium.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**4) Free image generation API — Pixazo.ai**_ 

I use image generation models almost every day. I use them to visualize the content of my articles and blog posts. 1 image is worth 1000 words, when you want to understand a new concept. 

In the past i shared with you several methods to use free available online tools to generate images: 

_**I stumbled on this free tiny Image Generator — and it changed how I create**_ 

**==> picture [121 x 56] intentionally omitted <==**

_No sign-up, no tracking, just a simple link that turns words into images. I was surprised how free the web could still…_ 

_generativeai.pub_ 

**==> picture [121 x 71] intentionally omitted <==**

Unfortunately even my last hero (together.ai) removed the free API access to Flux.1-Schnell. 

Also Nano-babana was removed from openrouter free API models. 

## _**Free image generation with OpenRouter and Gemini Nanobanana**_ 

_A new pair for amazing feats!_ 

_generativeai.pub_ 

**==> picture [121 x 126] intentionally omitted <==**

This week I discovered Pixazo.ai 

Pixazo is an online service to create AI Images, Videos and Audio Online. When you register (for free) you can get an API key (for free) and use Flux.1Schnell. 

There are 2 more models you can access for free, with the very same single API key: 

How to use it? 

Register for free and create an API key here. 

Install the following dependencies: 

## Open your ipython and run this: 

```
#Pixazo free API with flux-schnell
from PIL import Image
import requests
from io import BytesIO
import datetime
```

```
def download_image(image_url):
    response = requests.get(image_url)
print('Image ready')
    my_img = Image.open(BytesIO(response.content))
return my_img
```

```
def generate_timestamp_filename():
"""Generates a unique filename for a PNG file using the current timestamp.""
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp_str}_Pai_Image.png"
return filename
```

```
fname = generate_timestamp_filename()
prompt = input('/IMAGINE ')
print(f'Generating your image in file {fname}')
print('Calling the endpoint...')
url = "https://gateway.pixazo.ai/flux-1-schnell/v1/getData"
```

```
example = "Picture a sleek, futuristic car racing through a neon-lit cityscape,
headers = {
"Content-Type": "application/json",
"Cache-Control": "no-cache",
"Ocp-Apim-Subscription-Key": "xxxx"#<----YOUR PIZAZO API KEY
}
data = {
"prompt": prompt,
"num_steps": 4,
```

```
"seed": 15,
"height": 640,
"width": 1024
}
```

```
response = requests.post(url, json=data, headers=headers)
image_url = response.json()['output']
print('Downloading image...')
downloadedimage = download_image(image_url)
downloadedimage.show()
print('Saving your image...')
downloadedimage.save(fname)
print('All done!')
```

When you run it, a http requests is sent to the API endpoint with your prompt. You will get a byte-stream back, and Pillow will show it to you and save the image file. 

_image created running on ipython the code above_ 

You can change the size (but remember only to use multiple of 64) without exceeding the maximum size of 1024x1024. 

I also created a GUI interface (using opencode !) and I put it as an executable in my GitHube repository: feel free to use it. 

The repo is here: 

_Open in app_ 

_**GitHub - fabiomatricardi/Pixazo-free-image-generation: CLI and tkinter app to generate images for…**_ 

_github.com_ 

## And the executable is here: 

_**Release First release - Windows binaries · fabiomatricardi/Pixazo-free-image-generation**_ 

_CLI and tkinter app to generate images for free with Flux-Schnell and pixazo api - Release First release - Windows…_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

_Thepoorgpuguy Local Gpt Your Ai Your Rules_ 

