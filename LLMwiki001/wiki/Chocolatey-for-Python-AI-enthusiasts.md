---
title: Chocolatey for Python AI enthusiasts
created: 2026-04-09
last_updated: 2026-04-09
source_count: 1
status: reviewed
---
Chocolatey is a CLI-based package manager for Windows that brings Linux-style package management to Windows, enabling automated installation, upgrading, and removal of software from the terminal. For Python and AI enthusiasts, it serves as the backbone for building reproducible development environments.

Key takeaways:

## What Chocolatey Does
- Wraps traditional EXE/MSI installers, zips, and scripts into versioned packages installable via single commands
- Examples: `choco install python visualstudiocode git -y`
- Fetches official installers, runs them with predefined parameters, and tracks them for future upgrades

## Installation
Open PowerShell as Administrator and run:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

## Key Commands
- `choco install <package> -y` - Install a package (auto-confirm)
- `choco upgrade <package>` - Upgrade a package
- `choco upgrade all -y` - Upgrade all packages
- `choco uninstall <package>` - Remove a package
- `choco list` - List installed packages
- `choco outdated` - Check for outdated packages

## Why It Matters for AI Development
1. **Reproducible Environments**: Encode your tool stack in one script for consistent machine setups
2. **Version Control**: Pin specific versions (e.g., `choco install python --version=3.12.4 -y`)
3. **Centralized Updates**: Single command updates all managed packages
4. **Access to Dev Tools**: Packages for editors, AI/data tooling (cuda, ffmpeg, docker), and dev plumbing (git, cmake, 7zip)

## Common AI Development Stack
```
choco install python git visualstudiocode cuda cmake ffmpeg docker-desktop -y
```

Chocolatey extends the terminal-first mental model already used for Python (pip, venv) to the operating system level, making it ideal for setting up reproducible AI development environments.

[Source: Chocolatey-for-Python-AI-enthusiasts-how-to-tur]
