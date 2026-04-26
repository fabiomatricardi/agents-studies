## _**Chocolatey for Python & AI enthusiasts: how to turn Windows into your in-house developer workstation**_ 

_How a terminal-first package manager can automate your tools, tame your installs, and make reproducible AI environments as easy as running a script._ 

**==> picture [25 x 25] intentionally omitted <==**

_Fabio Matricardi 9 min read · Jan 19, 2026_ 

**==> picture [511 x 280] intentionally omitted <==**

Not something that sells million of dollars (well, if ti happens is still ok though), but a tool for you or your colleagues, something that makes your daily work easier and faster. 

Sometimes we want to have everything perfectly prepared before we even start to write one line of python: look for the best programming app (IDE), fancy libraries and tools, latest trending GUI looks and feel… 

And before you even start, you give up because of all the preparations. 

## _But what if I tell you a secret?_ 

You can have your tools ready with one single software. You can even use it to rebuild your Windows, or prepare a new computer for the task. 

all from the command line 

simple and fool proof 

In this article I will present you Chocolatey (for Windows OS) and how to start using it in 5 minutes. 

If you build Python and AI applications on Windows, you already know the pattern: install Python, then Git, then VS Code or Sublime, then CUDA, then 

some obscure runtime for an LLM backend. Each one has its own website, download link, installer, and update process. 

On Linux, package managers solve this problem. On Windows, Chocolatey brings that same idea to the terminal: one command-line interface to install, upgrade, and remove most of the tools you care about. 

In the past weeks I built several personal apps in python. They are useful to me. And I did it with the help of AI. To do this you need tools (back to the above section…) 

- `opencode` (the coder app that create code and all development files by 

- itself)? 

- `docker` (to have your local AI able to use web-search) 

- a good code editor (maybe with AI assistant plugins) 

So I decided to create a series of articles about all of the above: from installation to use. And what there is better than knowing HOW to do yourself? 

As an example (of applications I built myself, for my personal use): 

- a terminal app that monitors CPU and RAM usage (useful when you start llama.cpp and the model begins to eat all your memory…) 

- a web app to create web cards to be used in my articles 

a gradio chatbot for my personal documents 

- a GUI app to load GGUF models from a list and start/stop the llama.cpp server without opening 10 different terminal windows 

- a python app that every day scan my personal study folder, looking for new PDF files and send me an email with the recap of the new additions with a ToC and short summary of the documents. 

and so on… 

## _**GitHub - chocolatey/choco: Chocolatey - the package manager for Windows**_ 

_Chocolatey - the package manager for Windows. Contribute to chocolatey/choco development by creating an account on…_ 

_github.com_ 

**==> picture [121 x 126] intentionally omitted <==**

## _**And the first tool you need to have, the one that rules them all is Chocolatey**_ 

## _**What Chocolatey is**_ 

Chocolatey is a CLI-based package manager for Windows that wraps 

traditional EXE/MSI installers, zips, and scripts into versioned packages 

- ( `.nupkg` ) that you can install with a single command. 

Instead of hunting down installers, you can run commands like: 

Chocolatey fetches the official installers or binaries, runs them with predefined, scripted parameters, and tracks them so you can upgrade later with `choco upgrade` . 

For Python and AI enthusiasts, like us, this becomes the backbone of your local stack: 

Python runtimes: `python` , `python3` , specific versions via `--version` 

- Editors/IDEs: `visualstudiocode` , `sublimetext3` , `pycharm-community` 

AI/data tooling: `cuda` , `cudnn` (via vendor tools), `ffmpeg` , `docker` , `r` , `julia` 

Dev plumbing: `git` , `cmake` , `7zip` , `make` , `curl` , `wget` . 

Chocolatey gives you an _infrastructure_ for your tools, not just another installer. 

## _**How to install Chocolatey**_ 

You should not be surprised to learn that Chocolatey must be installed from 

## the Terminal. 

In fact it is a powerful terminal based package manager, so the terminal is its home. 

execute: 

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManage
```

  

This will begin the installation process. Just follow the instructions, and in case it is required you may have to reboot. 

_NOTE: remember that whenever you install a new package (app) with Chocolatey it is recommended to do it with Administrator privileges!_ 

And it is done. 

Now you can easily install, upgrade or uninstall all future software with a simple command in the terminal. 

You can browse all the existing packages in the main repository here: 

## _**Packages**_ 

_Chocolatey is software management automation for Windows that wraps installers, executables, zips, and scripts into…_ 

_community.chocolatey.org_ 

**==> picture [121 x 126] intentionally omitted <==**

## Some examples from my PC: 

I decided to replace VSCode with SublimeText3: it is light and has a little RAM footprint (against 1Gb for VSCode…). And SublimeText3 does have a coll package to integrate GenerativeAI assistance while coding! 

With Chocolatey it is super easy. In Powershell, with Admin rights just run: 

```
choco install sublimetext3 -y
```

The `-y` flag will automatically accept the installation process, otherwise it will prompt you to do so before proceeding 

## If you don’t add the flag `-y` the terminal will ask you: 

```
The package dotnetfx wants to run 'ChocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
```

```
**Do you want to run the script?([Y]es/[A]ll scripts/[N]o/[P]rint): A**
```

I can now find SublimeText3 in the windows Start menu 

One of the cool things of using the terminal is that you can do almost everything without using the mouse and living it. Even SublimeText can be run directly from the Terminal. 

To do so you need to add it in the PATH environment variables. You need only to know what is the installation path (choco always tells you that) 

```
The install of sublimetext3 was successful.
  Deployed to'C:\Program Files\Sublime Text 3\'
```

1- click Start and type env (select _Edit the system environment variables_ ) 

Click on Environment Variables, Path and add a New line with the path of Sublime Text 3. Click OK. 

Now in a new terminal window when you type `subl` the Code editor will open. 

## _**5 reasons why the Terminal should be your best friend**_ 

_To keep it simple stupid, sometimes a terminal command is the best (and fast) solution to all your problems._ 

_generativeai.pub_ 

**==> picture [121 x 122] intentionally omitted <==**

## _**Why It’s Good To Have It In The Terminal**_ 

Python and AI work is already terminal-heavy: `pip install` , `python -m venv` , 

`docker run` , `python main.py --model llama` . Chocolatey extends that same mental model to the OS level. 

There are some key advantages of running it in the terminal: 

## Single mental model: 

Once you learn `choco install` , `choco upgrade` , `choco list` , you can 

manage browsers, editors, runtimes, and utilities the same way you manage Python libraries with `pip` 

## Automation-friendly: 

Commands are scriptable: you can drop them into PowerShell scripts, CI pipelines, VS Code tasks, or Makefiles for repeatable environments 

## Fast feedback and visibility: 

Commands like `choco outdated` or `choco list` give you a quick snapshot of your tools and their versions—something GUIs almost never provide in a single place 

You can even search if there is a package directly from the terminal. Look at this: 

Over time, you stop thinking “open browser, search, download” and start thinking “declare the state I want; the system will go there.” That’s the DevOps mindset, and it maps perfectly to serious AI work. 

## _**Why Use Chocolatey Instead of Web Installers or the Windows Store?**_ 

For a single casual app, a website or the Microsoft Store is fine. For a Python/AI setup with 10–30 tools, GUI installers don’t scale. And above all, even to plan or check for updates is a pain… 

Imagine if you want to uninstall them! 

## _**1. Reproducible Environments**_ 

If you set up a new machine or VM, you can encode your tool stack in one script: 

```
# dev-tools.ps1
choco install `
  python `
  git `
  visualstudiocode `
  sublimetext3 `
  pycharm-community `
  docker-desktop `
  cmake `
```

Run this once and your machine converges to the same baseline every time. There’s no equivalent “run this file, get all my tools” story with random web installers or Store apps. 

## _**2. Version Control for Tools**_ 

You can pin explicit versions: 

```
choco install python --version=3.12.4 -y
choco install visualstudiocode --version=1.96.0 -y
```

This matters when: 

- `venvs` 

- A new Python release subtly breaks your or compiled extensions. 

A new VS Code or CUDA release conflicts with your LLM backend. 

Store and web installers usually only give you “latest” and no easy downgrade path. 

## _**3. Centralized Updates and Clean Removal**_ 

Instead of visiting 10 websites or clicking “Update” in 10 GUIs: 

```
choco upgrade all -y
```

Uninstalls are also more predictable: `choco uninstall <package>` runs the registered uninstall logic and tracks dependencies, instead of leaving behind random artifacts in Program Files and the registry. 

## _**4. Access to Real Dev Tools**_ 

The Windows Store is mostly end-user apps; serious dev tools and niche utilities rarely live there. Chocolatey has packages for: 

- Editors/IDEs: `sublimetext3` , `visualstudiocode` , `pycharm-community` , `neovim` 

- Data/AI: `knime` , `r` , `jupyter` (via Python packages but often bootstrapped with system tools) 

- Supporting tools: `postgresql` , `redis-64` , `rabbitmq` , etc. 

For AI experimentation where you may need weird combinations of drivers, compression tools, and runtimes, this breadth is invaluable. 

For Python and AI enthusiasts, the terminal is where the real work happens: training scripts, inference servers, Docker containers, log tailing. Chocolatey extends that same mindset to system tools. 

## Declarative setup: 

A script is a declarative description of your environment. You can test it, review it, revert it, and run it on multiple machines. 

## Traceability: 

The commands that shape your system are visible in shell history and 

`.ps1` files. 

- Cross platform thinking: 

_Open in app_ 

Once you think “package manager + scripts,” it transfers directly to Linux ( `apt` , `dnf` ) and macOS ( `brew` ), which is exactly where AI infra often lives in production. 

## _**Conclusions**_ 

Hope you are thrilled. I am! 

Chocolatey simplified a lot my life, to the point that in the next article I will show you how to use it to install Docker, and then use Docker to do something you cannot even imagine (run a Linux Desktop… in your browser). 

_Thepoorgpuguy Your Ai Your Rules_ 

_Local Gpt Python4ai Chocolately_ 

