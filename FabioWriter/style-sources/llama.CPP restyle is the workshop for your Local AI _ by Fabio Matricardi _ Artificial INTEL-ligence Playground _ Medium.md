## _**llama.CPP restyle is the workshop for your Local AI**_ 

_From LLM routing to full working Chat application: all in one ZIP file. And here is how._ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 10 min read · Jan 2, 2026_ 

**==> picture [511 x 394] intentionally omitted <==**

In the past 24 months, everyone with a computer was able to run a local AI: nothing has been so powerful! 

Now llama.cpp got a full restyle for its main components: 

- the llama-cli is a full fledged terminal app, you can even load a text file and chat with the document. 

- the llama-server can act as a model router: it recognize all the models you have and load/unload them at request 

- llama-server has a fully compatible OpenAI API endpoints 

- llama-server now has a convenient web-chat, with configuration, hyperparameters, chat history and conversation, model routing siwtch, documents and images can be attached to the conversation 

Want to know more? 

## _**Summary and Table of Contents**_ 

In this article we will explore what llama.cpp is, and how to use the 2 main applications to run Generative AI models locally, on your PC: llama-cli and llama-server. Both of them got a beautiful restyle, giving a nice look to the already practical and efficient tool. 

```
Table Of Contents
```

- `-----------------` 

- `But…. what is Llama.cpp?` 

- `Let's run an AI on our computer` 

- `Quick start: one line on your terminal` 

- `Llama-cli is all you need` 

- `Llama-server is a local server-farm for LLM` 

- `call the APIs from the windows terminal` 

- `Conclusions` 

## _**But…. what is Llama.cpp?**_ 

Llama.cpp is an open-source C/C++ library designed for efficient inference of large language models (LLMs), particularly those based on Meta’s Llama architecture. 

Its main goal is to enable LLM inference with minimal setup and state-ofthe-art performance across a wide range of hardware — both locally and in the cloud — without requiring specialized GPUs or dependencies 

Gerganov, owning a MacBook, didn’t have a way to run LLM. So guess what? He found a way to make it possible in March 2023! 

Gerganov started to work in late 2022 to developed the underlying ggml - (General purpose GPU Machine Learning) tensor library, and then built Llama.cpp to run large language models efficiently on consumer-grade hardware, especially CPUs. 

The motivation was to make powerful AI models more accessible, portable, and cost-effective, bypassing the need for expensive cloud infrastructure or 

## high-end GPUs 

During the months, the official GitHub repository found new contributors, and the project accelerated expanding supported models, CPU/GPU compliance, and architectures. 

## _**New in llama.cpp: Model Management**_ 

_A Blog post by ggml.ai on Hugging Face_ 

_huggingface.co_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**llama.cpp/tools/server at master · ggml-org/llama.cpp**_ 

_LLM inference in C/C++. Contribute to ggml-org/llama.cpp development by creating an account on GitHub._ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**Let’s run an AI on our computer**_ 

To have a full powerful AI running Locally on your PC you need only 2 things: 

the llama.cpp ZIP file with the binary (executable) for your Operating System: I used Windows x64 (CPU) for Windows OS 64 bit 

a GGUF (quantized) file with the weights of your model: for example the - – - - – - slim gemma 3 270m it Q8_0.gguf or the new amazing LFM2 1.2B Q6_K.gguf 

## _**ggml-org (ggml.ai)**_ 

_Org profile for ggml.ai on Hugging Face, the AI community building the future._ 

_huggingface.co_ 

**==> picture [121 x 126] intentionally omitted <==**

Following the example above download the binaries Windows x64 (CPU) in the same directory (mine is called `llamacpp` ) 

- – - - Download the model 3 270m it gemma Q8_0.gguf and put it into a 

subdirectory (mine is called `models` ) 

– - Download the model LFM2 1.2B Q6_K.gguf and put it into a subdirectory (mine is called `models` ) 

```
llamacpp
└───models
```

Extract the ZIP archive in the main `llamacpp` directory. You should have something like this: 

## _**Quick start: one line on your terminal**_ 

To start using a Large Language Model on your PC all you need is 1 

command from your terminal. From the main project directory ( `llamacpp)` , open the terminal and run: 

```
-
.\llama-cli.exe -m .\models\google_gemma-3270m-it-Q8_0.gguf -c8192
```

this will start a terminal chat interactive session with gemma3–270m and 8192 tokens context window. 

## _**Llama-cli is all you need**_ 

Llama-cli can also /read a text file. You can use the method I explained in this article to do it also for PDFs, without leaving your pc 

## _**The quickest (and unsophisticated) way to chat with your documents locally**_ 

_Private Documents must be processed locally - in your Private Local AI. And here is how._ 

_open.substack.com_ 

**==> picture [121 x 126] intentionally omitted <==**

I created a portable PDF to TXT on the fly converter, so that you can load it with llama-cli without any issues. 

The link to the file called pdf_extractor.exe is here. 

## _**Llama-server is a local server-farm for LLM**_ 

The New WebUI is a ChatGPT experience, Fully Local. 

The latest version of llama-server now includes a built-in, SvelteKit-based WebUI that transforms your local machine into a private, ChatGPT-like chat interface — no internet required. 

Once you start the server (e.g., `.\llama-server.exe --models-dir .\models\` ), simply open your browser to `http://127.0.0.1:8080` and you’re greeted with a clean, responsive chat window. 

Key features of the new WebUI include: 

- Dynamic model switching: A dropdown menu lets you select from all `--models-dir` 

- GGUF models in your . The first time you pick a model, it loads automatically in the background—no restart needed. 

- Chat history persistence: Conversations are saved locally in your browser, allowing you to resume sessions later. 

- Hyperparameter control: Adjust temperature, context length, and other inference settings directly from the UI. 

- Multimodal support: Recent builds also enable image and document attachments. 

- Full OpenAI API compatibility: The same backend powers both the WebUI and API endpoints, so your apps and scripts work interchangeably. 

Critically, this WebUI is 100% client-side and private — no data leaves your machine. Unlike hosted alternatives, every token is processed locally, making it ideal for sensitive or confidential use cases. 

And you can upload images, text files an even PDF! 

As one user put it: 

## _Grab a model._ 

Running a local LLM server shouldn’t feel like guesswork. The `llama.cpp` server is a powerful, lightweight tool, but its long list of parameters can be overwhelming. 

_Get the CheatSheet for free_ 

This downloadable cheat sheet is your essential reference guide to cut through the complexity. I have consolidated the most critical command-line flags into one, color-coded infographic, making it simple to find the perfect configuration for your hardware and use case. 

load, unload, and switch between multiple models without restarting. 

_Reminder: llama.cpp server is a lightweight, OpenAI-compatible HTTP server for running LLMs locally._ 

This feature was a popular request to bring Ollama-style model management to llama.cpp. It uses a multi-process architecture where each model runs in its own process, so if one model crashes, others remain unaffected. 

Start the server in router mode pointing to a local directory of GGUF files: 

```
llama-server --models-dir ./my-models
```

## I tried like this 

```
PS E:\llamaCPP_router> .\llama-server.exe --models-dir .\models\
```

## And got beautifully 

```
oad_backend: loaded RPC backend from E:\llamaCPP_router\ggml-rpc.dll
ggml_vulkan: Found 1 Vulkan devices:
```

```
ggml_vulkan: 0 = Intel(R) Graphics (Intel Corporation) | uma: 1 | fp16: 1 | bf16
....
load_backend: loaded Vulkan backend from E:\llamaCPP_router\ggml-vulkan.dll
load_backend: loaded CPU backend from E:\llamaCPP_router\ggml-cpu-alderlake.dll
srv   load_models: Available models (3) (*: custom preset)
srv   load_models:     LFM2-1.2B-Q6_K
srv   load_models:     ibm-granite.granite-4.0-h-1b.Q6_K
srv   load_models:     zen-nano-0.6b.i1-Q6_K
main: starting router server, no model will be loaded in this process
start: binding port with default address family
main: router server is listening on http://127.0.0.1:8080
```

 

 

## _**GitHub - fabiomatricardi/llamaCPP-server-router: new commands for llama.cpp server router option**_ 

_new commands for llama.cpp server router option. Contribute to fabiomatricardi/llamaCPP-server-router development by…_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

Here some terminal based commands, for Windows Powershell users, to test the endpoints (including the ones to load/unload models): 

## _**Chat with a specific model**_ 

```
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "ggml-org/gemma-3-4b-it-GGUF:Q4_K_M",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

On the first request, the server automatically loads the model into memory (loading time depends on model size). Subsequent requests to the same model are instant since it’s already loaded. 

## If you are using windows terminal, PowerShell style 

```
Invoke-WebRequest -Uri "http://localhost:8080/v1/chat/completions" `
-Method POST `
```

```
-Headers @{ "Content-Type" = "application/json" } `
```

- `-Body '{"model": "LFM2-1.2B-Q6_K","messages": [{"role": "user", "content": "Hell` 

  

## Getting something like this 

```
StatusCode        : 200
StatusDescription : OK
Content           : {"choices":[{"finish_reason":"stop","index":0,"message":{"ro
                    can I help you
                    today?"}}],"created":1765551259,"model":"LFM2-1.2B-Q6_K","sy
RawContent        : HTTP/1.1 200 OK
                    Transfer-Encoding: chunked
                    Access-Control-Allow-Origin:
                    Keep-Alive: timeout=5, max=100
                    Content-Type: application/json; charset=utf-8
                    Server: llama.cpp
                    {"choices":[{"finish_rea...
Forms             : {}
Headers           : {[Transfer-Encoding, chunked], [Access-Control-Allow-Origin,
                    [Content-Type, application/json; charset=utf-8]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 603
```

```
curl http://localhost:8080/models
```

Returns all discovered models with their status ( `loaded` , `loading` , or `unloaded` ). 

```
PS E:\llamaCPP_router> curl http://localhost:8080/models
StatusCode        : 200
StatusDescription : OK
Content           : {"data":[{"id":"LFM2-1.2B-Q6_K","object":"model","owned_by":
                    he":false,"path":".\\models\\LFM2-1.2B-Q6_K.gguf","status":{
                    ro...
RawContent        : HTTP/1.1 200 OK
                    Access-Control-Allow-Origin:
                    Keep-Alive: timeout=5, max=100
                    Content-Length: 1104
                    Content-Type: application/json; charset=utf-8
                    Server: llama.cpp
                    {"data":[{"id":"LFM2-1.2B-Q6_K...
Forms             : {}
Headers           : {[Access-Control-Allow-Origin, ], [Keep-Alive, timeout=5, ma
                    [Content-Type, application/json; charset=utf-8]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 1104
```

  

## _**Manually load a model**_ 

```
curl -X POST http://localhost:8080/models/load \
```

- `-H "Content-Type: application/json" \` 

- `-d '{"model": "my-model.gguf"}'` 

## But for windows users you must change few things, as described here below: 

```
Invoke-WebRequest -Uri"http://localhost:8080/models/load" -Method POST -Headers
```

  

## or 

```
Invoke-WebRequest -Uri"http://localhost:8080/models/load" -Method POST -Headers
```

  

## or 

```
Invoke-WebRequest -Uri"http://localhost:8080/models/load" -Method POST -Headers
```

  

## _**Unload a model to free VRAM**_ 

```
curl -X POST http://localhost:8080/models/unload \
```

- `-H "Content-Type: application/json" \` 

✅ _Recommended PowerShell Version (using_ _`Invoke-WebRequest` ). Replace_ _`"mymodel.gguf"` with each of your actual model names:_ 

_**1. Unload**_ `LFM2-1.2B-Q6_K` 

```
Invoke-WebRequest -Uri"http://localhost:8080/models/unload" -Method POST -Heade
```

  

## _**2. Unload**_ `ibm-granite.granite-4.0-h-1b.Q6_K` 

```
Invoke-WebRequest -Uri"http://localhost:8080/models/unload" -Method POST -Heade
```

  

_**3. Unload**_ `zen-nano-0.6b.i1-Q6_K` 

```
Invoke-WebRequest -Uri"http://localhost:8080/models/unload" -Method POST -Heade
```

## 🔄 _**Or use a reusable function (if you’re doing this often)**_ 

`- function Unload Model { param([string]$ModelName) $body = @{ model = $ModelName } | ConvertTo-Json -Compress Invoke-WebRequest -Uri "http://localhost:8080/models/unload" -Method POST -H }`   

## Then run: 

```
Unload-Model "LFM2-1.2B-Q6_K"
```

```
Unload-Model "ibm-granite.granite-4.0-h-1b.Q6_K"
Unload-Model "zen-nano-0.6b.i1-Q6_K"
```

These commands will become quite useful in your Python application: In fact you don’t need anymore a psutils Popen PID to know how to start/stop a service. 

An API call will be enough! 

## _**Conclusions**_ 

_Open in app_ 

With its newly restyled llama-cli and llama-server, you no longer need cloud APIs, expensive GPUs, or complex setups to run state-of-the-art language models. 

Whether you’re chatting with a document via the terminal, routing between multiple quantized models on the fly, or interacting through a sleek browser interface, everything now fits in a single ZIP file on your PC. 

This is our personal way to regain back privacy and control 

You own your data, your hardware, and your AI experience. 

And with OpenAI-compatible endpoints, existing tools and workflows integrate seamlessly. In 2025, running a powerful, private, and flexible AI assistant locally isn’t the future — it’s your Tuesday afternoon. 

Your AI, Your Rules! 

_Your Ai Your Rules_ 

_Local Gpt Thepoorgpuguy Llama Cpp_ 

