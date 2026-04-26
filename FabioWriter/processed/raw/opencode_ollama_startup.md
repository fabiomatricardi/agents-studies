OpenCode installs easily via a one-line script and pairs seamlessly with Ollama for local models, supporting any compatible LLM without cloud dependency. This setup works on Linux, macOS, and Windows, ideal for your Turin-based dev environment with tools like Ubuntu or Docker. [opencode](https://opencode.ai/docs/models/)

## Prerequisites
Install Ollama first for local models:
```
curl -fsSL https://ollama.com/install.sh | sh
```
Then pull a model (e.g., efficient for your AI benchmarking):
```
ollama pull gemma2:9b  # Or qwen2.5:14b, llama3.2:11b based on hardware
```
Test interactively: `ollama run gemma2:9b`. [dev.classmethod](https://dev.classmethod.jp/en/articles/ollama-opencode-setup/)

## Installation
Run the official installer (adds to PATH automatically):
```
curl -fsSL https://opencode.ai/install.sh | sh
```
Reload shell: `source ~/.bashrc` (or equivalent for zsh/fish/PowerShell). For Windows (your preferred platform), use WSL/Ubuntu or the desktop beta from opencode.ai. [youtube](https://www.youtube.com/watch?v=M635TVoiLYw)

## Local Model Setup
Create global config at `~/.config/opencode/opencode.json` (or project-local `.opencode/opencode.json`):
```
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "gemma2:9b": {
          "name": "Gemma2 9B Local"
        }
      }
    }
  }
}
```
OpenCode auto-installs the SDK package. [poncardas](https://poncardas.com/blog/how-to-run-local-ai-models-ollama-opencode/)

## Usage
Start in a project dir: `opencode` (select your Ollama model via `/models`). Ensure Ollama service runs: `ollama serve &`. For Docker (your habit), containerize Ollama and expose port 11434. Test with a prompt like "Explain this codebase" – responses use local model only. [youtube](https://www.youtube.com/watch?v=DC5R3iHzlXs)


Pull Qwen-3.5-2B and Gemma-4-E2B via Ollama for lightweight local models suited to your Python/AI projects and benchmarking workflows. These small models (2B params) run efficiently on modest hardware like your Windows/Linux setups, with strong coding performance in OpenCode tests. [youtube](https://www.youtube.com/watch?v=HOQkuYRwlVI)

## Prerequisites (Updated)
Ensure Ollama is installed and running:
```
ollama serve
```
Pull the models (exact tags from Ollama library):
```
ollama pull qwen2.5-coder:3b  # Qwen 3.5 2B variant (qwen2.5-coder:3b or qwen3:2b if available)
ollama pull gemma2:2b         # Gemma-4-E2B (gemma2:2b or gemma4:e2b quantized)
```
Verify: `ollama list`. [haimaker](https://haimaker.ai/blog/gemma-4-ollama-opencode-setup/)

## Installation
Same as before—no changes needed:
```
curl -fsSL https://opencode.ai/install.sh | sh
source ~/.bashrc
```


## Local Model Config (Adjusted)
Edit `~/.config/opencode/opencode.json`:
```
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen2.5-coder:3b": {
          "name": "Qwen 3.5 2B Local"
        },
        "gemma2:2b": {
          "name": "Gemma 4 E2B Local"
        }
      }
    }
  }
}
```
Adjust tags if exact "qwen-3.5-2b" or "gemma-4-e2b" differs (check `ollama search qwen` or `ollama search gemma`). [dev](https://dev.to/grovertek/running-gemma-4-locally-with-ollama-and-opencode-2h6)

## Usage
Run `opencode`, then Ctrl+P > Switch Model > Select from Ollama list (e.g., "Qwen 3.5 2B Local"). For your GUI prefs, integrate into VS Code via LSP or use the desktop app. Test efficiency with a PySide6 snippet benchmark. [reddit](https://www.reddit.com/r/LocalLLaMA/comments/1ssdim1/tested_how_opencode_works_with_selfhosted_llms/)


The curl-based CLI install script does not work natively on Windows due to lacking bash/curl by default. Instead, use WSL (Ubuntu/Alpine for your prefs), PowerShell, or the official desktop app—perfect for your Windows 11 + Docker/PowerShell workflow. [docs.ollama](https://docs.ollama.com/integrations/opencode)

## Windows Options
### Option 1: WSL (Recommended for Linux-like Experience)
Enable WSL2: `wsl --install -d Ubuntu` in admin PowerShell, then reboot. [youtube](https://www.youtube.com/watch?v=gFTrWRpSQIs)
Inside WSL Ubuntu:
```
curl -fsSL https://ollama.com/install.sh | sh
curl -fsSL https://opencode.ai/install.sh | sh
source ~/.bashrc
```
Access from Windows PowerShell: `wsl opencode` (adds to PATH). [youtube](https://www.youtube.com/watch?v=DC5R3iHzlXs)

### Option 2: Desktop App (Simplest, No CLI)
Download from https://opencode.ai/download (MSI/EXE for Windows). [opencode](https://opencode.ai)
- Install Ollama from https://ollama.com/download (native Windows preview). [youtube](https://www.youtube.com/watch?v=gFTrWRpSQIs)
- Launch OpenCode desktop > Settings > Providers > Add Ollama (auto-detects http://localhost:11434). [youtube](https://www.youtube.com/watch?v=gFTrWRpSQIs)

### Option 3: PowerShell CLI (Native)
Install Ollama via EXE from ollama.com.
For OpenCode CLI:
```
irm https://opencode.ai/install.ps1 | iex
```
Reload: `$env:PATH += ";$env:LOCALAPPDATA\Programs\opencode"` (or restart Terminal). [generativeai](https://generativeai.pub/free-ai-coding-with-opencode-ollama-on-windows-aab1510e1978)

## Model/Config Steps
Identical across options—pull models and edit `%USERPROFILE%\.config\opencode\opencode.json` (Windows path). [poncardas](https://poncardas.com/blog/how-to-run-local-ai-models-ollama-opencode/)
```
ollama pull qwen2.5-coder:3b
ollama pull gemma2:2b
```
Run: `opencode` or desktop launch. For Docker: Run Ollama container, expose port, use host config. [youtube](https://www.youtube.com/watch?v=HOQkuYRwlVI)