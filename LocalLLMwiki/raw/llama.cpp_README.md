philtomson/llama.cpp: LLM inference in C/C++ (fork of PrismML fork that enables CPU (incl AVX2 and AVX512) and ROCm for AMD GPUs
https://github.com/philtomson/llama.cpp
llama.cpp



Manifesto / ggml / ops

LLM inference in C/C++

Recent API changes
Changelog for libllama API
Changelog for llama-server REST API
Hot topics
guide : using the new WebUI of llama.cpp
guide : running gpt-oss with llama.cpp
[FEEDBACK] Better packaging for llama.cpp to support downstream consumers 🤗
Support for the gpt-oss model with native MXFP4 format has been added | PR | Collaboration with NVIDIA | Comment
Multimodal support arrived in llama-server: #12898 | documentation
VS Code extension for FIM completions: https://github.com/ggml-org/llama.vscode
Vim/Neovim plugin for FIM completions: https://github.com/ggml-org/llama.vim
Hugging Face Inference Endpoints now support GGUF out of the box! ggml-org#9669
Hugging Face GGUF editor: discussion | tool
Quick start

Getting started with llama.cpp is straightforward. Here are several ways to install it on your machine:

Install llama.cpp using brew, nix or winget
Run with Docker - see our Docker documentation
Download pre-built binaries from the releases page
Build from source by cloning this repository - check out our build guide

Once installed, you'll need a model to work with. Head to the Obtaining and quantizing models section to learn more.

Example command:

# Use a local model file
llama-cli -m my_model.gguf

# Or download and run a model directly from Hugging Face
llama-cli -hf ggml-org/gemma-3-1b-it-GGUF

# Launch OpenAI-compatible API server
llama-server -hf ggml-org/gemma-3-1b-it-GGUF
Description

The main goal of llama.cpp is to enable LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware - locally and in the cloud.

Plain C/C++ implementation without any dependencies
Apple silicon is a first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks
AVX, AVX2, AVX512 and AMX support for x86 architectures
RVV, ZVFH, ZFH, ZICBOP and ZIHINTPAUSE support for RISC-V architectures
1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use
Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP and Moore Threads GPUs via MUSA)
Vulkan and SYCL backend support
CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity

The llama.cpp project is the main playground for developing new features for the ggml library.

Models
Bindings
UIs
Tools
Infrastructure
Games
Supported backends
Backend Target devices
Metal Apple Silicon
BLAS All
BLIS All
SYCL Intel and Nvidia GPU
MUSA Moore Threads GPU
CUDA Nvidia GPU
HIP AMD GPU
ZenDNN AMD CPU
Vulkan GPU
CANN Ascend NPU
OpenCL Adreno GPU
IBM zDNN IBM Z & LinuxONE
WebGPU [In Progress] All
RPC All
Hexagon [In Progress] Snapdragon
VirtGPU VirtGPU APIR
AMD GPU support (ROCm/HIP)

The HIP backend supports running Bonsai Q1_0_g128 models on AMD GPUs via ROCm/HIP. The Q1_0_g128 CUDA kernels are compiled transparently by the HIP toolchain — no separate HIP-specific kernel code is needed.

Requirements
ROCm 6.x+ with hipBLAS and rocBLAS (including device libraries for your GPU target). See docs/build.md for the current HIP/ROCm build requirements.
Note for RDNA4 GPUs (gfx1151, Radeon 8060S / Ryzen AI MAX+): rocBLAS kernels for gfx1151 first appear in ROCm 7.2. Earlier ROCm versions can build but will fall back to slower generic kernels.
The easiest way to get a fully configured environment is to use the rocm/pytorch:rocm7.2_ubuntu24.04_py3.12_pytorch_release_2.10.0 Docker image, which includes gfx1151 support
Build
HIPCXX=$(hipconfig -l)/clang HIP_PATH=$(hipconfig -R) \
cmake -B build-hip \
-DGGML_HIP=ON \
-DGPU_TARGETS=gfx1151 \
-DCMAKE_BUILD_TYPE=Release \
-DGGML_CUDA_FA=OFF
cmake --build build-hip --config Release -j$(nproc)

Replace gfx1151 with your GPU's architecture. Find yours with:

rocminfo | grep gfx | head -1 | awk '{print $2}'
Run
build-hip/bin/llama-cli -m /path/to/Bonsai-8B.gguf -ngl 99 -p "your prompt"

-ngl 99 offloads all layers to the GPU. On an integrated GPU (APU) that shares system memory, the full model fits in the GPU address space.

Docker

If your system ROCm installation is partial, build and run inside the Docker image:

docker run --rm \
--device /dev/kfd --device /dev/dri \
--group-add video --group-add render \
-v /path/to/llama.cpp:/llama.cpp \
-v /path/to/models:/models \
rocm/pytorch:rocm7.2_ubuntu24.04_py3.12_pytorch_release_2.10.0 \
bash -c "
pip install cmake -q && cd /llama.cpp && \
HIPCXX=\$(hipconfig -l)/clang HIP_PATH=\$(hipconfig -R) \
cmake -B build-hip -DGGML_HIP=ON -DGPU_TARGETS=gfx1151 \
-DCMAKE_BUILD_TYPE=Release -DGGML_CUDA_FA=OFF && \
cmake --build build-hip -j\$(nproc) && \
build-hip/bin/llama-cli -m /models/Bonsai-8B.gguf -ngl 99 -p 'Hello'
"
Obtaining and quantizing models

The Hugging Face platform hosts a number of LLMs compatible with llama.cpp:

Trending
LLaMA

You can either manually download the GGUF file or directly use any llama.cpp-compatible models from Hugging Face or other model hosting sites, such as ModelScope, by using this CLI argument: -hf <user>/<model>[:quant]. For example:

llama-cli -hf ggml-org/gemma-3-1b-it-GGUF

By default, the CLI would download from Hugging Face, you can switch to other options with the environment variable MODEL_ENDPOINT. For example, you may opt to downloading model checkpoints from ModelScope or other model sharing communities by setting the environment variable, e.g. MODEL_ENDPOINT=https://www.modelscope.cn/.

After downloading a model, use the CLI tools to run it locally - see below.

llama.cpp requires the model to be stored in the GGUF file format. Models in other data formats can be converted to GGUF using the convert_*.py Python scripts in this repo.

The Hugging Face platform provides a variety of online tools for converting, quantizing and hosting models with llama.cpp:

Use the GGUF-my-repo space to convert to GGUF format and quantize model weights to smaller sizes
Use the GGUF-my-LoRA space to convert LoRA adapters to GGUF format (more info: ggml-org#10123)
Use the GGUF-editor space to edit GGUF meta data in the browser (more info: ggml-org#9268)
Use the Inference Endpoints to directly host llama.cpp in the cloud (more info: ggml-org#9669)

To learn more about model quantization, read this documentation

llama-cli
A CLI tool for accessing and experimenting with most of llama.cpp's functionality.
Run in conversation mode

Models with a built-in chat template will automatically activate conversation mode. If this doesn't occur, you can manually enable it by adding -cnv and specifying a suitable chat template with --chat-template NAME

llama-cli -m model.gguf

# > hi, who are you?
# Hi there! I'm your helpful assistant! I'm an AI-powered chatbot designed to assist and provide information to users like you. I'm here to help answer your questions, provide guidance, and offer support on a wide range of topics. I'm a friendly and knowledgeable AI, and I'm always happy to help with anything you need. What's on your mind, and how can I assist you today?
#
# > what is 1+1?
# Easy peasy! The answer to 1+1 is... 2!
Run in conversation mode with custom chat template
Constrain the output with a custom grammar
llama-server
A lightweight, OpenAI API compatible, HTTP server for serving LLMs.
Start a local HTTP server with default configuration on port 8080
llama-server -m model.gguf --port 8080

# Basic web UI can be accessed via browser: http://localhost:8080
# Chat completion endpoint: http://localhost:8080/v1/chat/completions
Support multiple-users and parallel decoding
Enable speculative decoding
Serve an embedding model
Serve a reranking model
Constrain all outputs with a grammar
llama-perplexity
A tool for measuring the perplexity 1 (and other quality metrics) of a model over a given text.
Measure the perplexity over a text file
llama-perplexity -m model.gguf -f file.txt

# [1]15.2701,[2]5.4007,[3]5.3073,[4]6.2965,[5]5.8940,[6]5.6096,[7]5.7942,[8]4.9297, ...
# Final estimate: PPL = 5.4007 +/- 0.67339
Measure KL divergence
llama-bench
Benchmark the performance of the inference for various parameters.
Run default benchmark
llama-bench -m model.gguf

# Output:
# | model | size | params | backend | threads | test | t/s |
# | ------------------- | ---------: | ---------: | ---------- | ------: | ------------: | -------------------: |
# | qwen2 1.5B Q4_0 | 885.97 MiB | 1.54 B | Metal,BLAS | 16 | pp512 | 5765.41 ± 20.55 |
# | qwen2 1.5B Q4_0 | 885.97 MiB | 1.54 B | Metal,BLAS | 16 | tg128 | 197.71 ± 0.81 |
#
# build: 3e0ba0e60 (4229)
llama-simple
A minimal example for implementing apps with llama.cpp. Useful for developers.
Basic text completion
Contributing
Contributors can open PRs
Collaborators will be invited based on contributions
Maintainers can push to branches in the llama.cpp repo and merge PRs into the master branch
Any help with managing issues, PRs and projects is very appreciated!
See good first issues for tasks suitable for first contributions
Read the CONTRIBUTING.md for more information
Make sure to read this: Inference at the edge
A bit of backstory for those who are interested: Changelog podcast
Other documentation
cli
completion
server
GBNF grammars
Development documentation
How to build
Running on Docker
Build on Android
Performance troubleshooting
GGML tips & tricks
Seminal papers and background on the models

If your issue is with model generation quality, then please at least scan the following links and papers to understand the limitations of LLaMA models. This is especially important when choosing an appropriate model size and appreciating both the significant and subtle differences between LLaMA models and ChatGPT:

LLaMA:
Introducing LLaMA: A foundational, 65-billion-parameter large language model
LLaMA: Open and Efficient Foundation Language Models
GPT-3
Language Models are Few-Shot Learners
GPT-3.5 / InstructGPT / ChatGPT:
Aligning language models to follow instructions
Training language models to follow instructions with human feedback
XCFramework

The XCFramework is a precompiled version of the library for iOS, visionOS, tvOS, and macOS. It can be used in Swift projects without the need to compile the library from source. For example:

// swift-tools-version: 5.10
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
name: "MyLlamaPackage",
targets: [
.executableTarget(
name: "MyLlamaPackage",
dependencies: [
"LlamaFramework"
]),
.binaryTarget(
name: "LlamaFramework",
url: "https://github.com/ggml-org/llama.cpp/releases/download/b5046/llama-b5046-xcframework.zip",
checksum: "c19be78b5f00d8d29a25da41042cb7afa094cbf6280a225abe614b03b20029ab"
)
]
)

The above example is using an intermediate build b5046 of the library. This can be modified to use a different version by changing the URL and checksum.

Completions

Command-line completion is available for some environments.

Bash Completion
$ build/bin/llama-cli --completion-bash > ~/.llama-completion.bash
$ source ~/.llama-completion.bash

Optionally this can be added to your .bashrc or .bash_profile to load it automatically. For example:

$ echo "source ~/.llama-completion.bash" >> ~/.bashrc
Dependencies
yhirose/cpp-httplib - Single-header HTTP server, used by llama-server - MIT license
stb-image - Single-header image format decoder, used by multimodal subsystem - Public domain
nlohmann/json - Single-header JSON library, used by various tools/examples - MIT License
miniaudio.h - Single-header audio format decoder, used by multimodal subsystem - Public domain
subprocess.h - Single-header process launching solution for C and C++ - Public domain
Footnotes

https://huggingface.co/docs/transformers/perplexity ↩

About

LLM inference in C/C++ (fork of PrismML fork that enables CPU (incl AVX2 and AVX512) and ROCm for AMD GPUs