# Browser Agents Setup

Minimal setup for three browser automation agents: **browser-use**, **magnitude**, and **skyvern**.

## Prerequisites

- Python 3.11+ (for browser-use, skyvern)
- Node.js 18+ / Bun (for magnitude)
- [uv](https://docs.astral.sh/uv/) - fast Python package manager
- Copy `.env.example` to `.env` in the root and add your API keys

```bash
cp .env.example .env
```

---

## browser-use (Python)

Uses LLMs to control a browser via natural language. Opens a local browser you can watch.

```bash
cd src/browser-use

# Create venv & install
uv venv
uv pip install browser-use python-dotenv

# Install browser
uv run playwright install chromium

# Run
uv run python main.py
```

**Requires:** `BROWSER_USE_API_KEY` or `OPENAI_API_KEY` or `GEMINI_API_KEY` in `.env`

---

## magnitude (TypeScript)

High-level browser agent with structured actions. Opens a local browser you can watch.

```bash
cd src/magnitude

# Install (bun or npm)
bun install
# or: npm install

# Run
bun start
# or: npm start
```

**Requires:** `ANTHROPIC_API_KEY` in `.env`

---

## skyvern (Python)

Browser automation via cloud API. Runs headless on Skyvern's servers.

```bash
cd src/skyvern

# Create venv & install
uv venv
uv pip install skyvern python-dotenv

# Run
uv run python main.py
```

**Requires:** `SKYVERN_API_KEY` in `.env` - get from [app.skyvern.com/settings](https://app.skyvern.com/settings)

**View results:** Tasks run async - view recordings at [app.skyvern.com/tasks](https://app.skyvern.com/tasks)

---

## Quick Reference

| Agent | Language | Browser | Install | Run |
|-------|----------|---------|---------|-----|
| browser-use | Python | Local | `uv pip install browser-use python-dotenv` | `uv run python main.py` |
| magnitude | TypeScript | Local | `bun install` | `bun start` |
| skyvern | Python | Cloud | `uv pip install skyvern python-dotenv` | `uv run python main.py` |
