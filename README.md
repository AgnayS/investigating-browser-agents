# Investigating Browser Agents

> Research repository for understanding the browser agent landscape (Q4 2025)

Based on [Reliable Agents Market Map](https://reliableagents.ai/2025-Q4)

---

## Table of Contents

1. [Browser Use Frameworks](#1-browser-use-frameworks)
2. [Low-Level/Specialized Browser Use](#2-low-levelspecialized-browser-use)
3. [Browsers as a Service](#3-browsers-as-a-service)
4. [Supporting Infrastructure](#4-supporting-infrastructure)
5. [Scraping & Crawling APIs](#5-scraping--crawling-apis)

---

## 1. Browser Use Frameworks

*Convenient abstraction layers for AI-powered browser automation*

### Browser Use

**GitHub:** https://github.com/browser-use/browser-use | **Website:** https://browser-use.com/

- Open-source Python/TypeScript library enabling AI agents to control browsers programmatically for form completion, data extraction, web scraping, and online shopping
- **Vision-based architecture**: Agents receive both DOM and visual representations, execute actions (clicks, typing, scrolling), and process feedback to refine behavior
- **Model support**: ChatBrowserUse (proprietary, 3-5x faster), OpenAI GPT-4, Google Gemini, Anthropic Claude, Azure OpenAI, DeepSeek, Ollama + full LangChain integration
- Browser Use Cloud provides stealth browsers with fingerprinting evasion and CAPTCHA resistance
- Custom tools via decorated Python functions; authentication handling with browser profile reuse
- **Installation**: `uv add browser-use` (Python >=3.11), `uvx browser-use install` for Chromium
- **Pricing**: Cloud starts at $30/month; ChatBrowserUse model $0.20/1M input, $2.00/1M output tokens
- **Community**: 73,500+ GitHub stars, 23.4k Discord members, 2,200+ dependent projects

### Magnitude.run

**GitHub:** https://github.com/magnitudedev/magnitude | **Docs:** https://docs.magnitude.run/

- Open-source, **vision-first** browser automation framework using AI for natural language commands
- Uses visually grounded LLM specifying pixel coordinates rather than numbered boxes around elements
- **Recommended model**: Claude Sonnet 4 for optimal performance; Qwen-2.5VL 72B as alternative
- Four core capabilities: **Navigate** (understands any interface), **Interact** (precise mouse/keyboard), **Extract** (structured data via Zod schemas), **Verify** (built-in test runner)
- Achieves **94% on WebVoyager benchmark**
- Vision-based interaction eliminates reliance on DOM structure - robust against layout changes
- Future-proof: extends beyond web to desktop apps and VMs
- **Installation**: `npx create-magnitude-app` or `npm i --save-dev magnitude-test`
- **Community**: 3,800+ GitHub stars, Apache 2.0 license

### SIMULAR (Agent-S)

**Website:** https://www.simular.ai/ | **GitHub:** https://github.com/simular-ai/Agent-S

- Autonomous computer company developing cross-platform AI agents across entire desktop environments (macOS, Windows, Linux)
- **Agent S3 architecture**: Combines neural and symbolic reasoning with Proactive Hierarchical Planning (PHP) and Mixture-of-Grounding (MoG)
- Operates **solely on raw screenshots** without accessibility trees - unique in the field
- **Performance**: 62.6% single-agent on OSWorld (approaching 72% human performance); won Best Paper at ICLR 2025 Agentic AI Workshop
- Products: Simular for macOS, Simular Browser (multi-tab parallel), Simular Desktop (cross-platform), Simular for Business
- Supports Azure OpenAI, Anthropic, Gemini, Open Router, vLLM inference
- **Community**: 8,621 GitHub stars, Apache 2.0 license

### Skyvern

**GitHub:** https://github.com/Skyvern-AI/skyvern | **Website:** https://www.skyvern.com/

- Automates browser workflows using LLMs and computer vision with simple API endpoints
- **Multi-agent swarm system** inspired by BabyAGI/AutoGPT - comprehends websites, plans and executes actions
- Uses vision LLMs instead of brittle XPath - works on previously unseen websites without custom code
- **Recommended models**: Anthropic Claude 3.5/3.7/4 Sonnet, Claude 4 Opus; MCP compatible
- **Performance**: 64.4% on WebBench, 85.8% on WebVoyager benchmark (5,750 real-world tasks)
- Supports 2FA (QR, email, SMS), Bitwarden integration, viewport livestreaming
- Workflow composition: browser tasks, data extraction, validation, loops, file parsing, HTTP requests, custom code
- **Pricing**: Free plan available; Cloud $0.10 per page; Enterprise custom
- Companies report 30-50% cost reductions and 99%+ accuracy vs manual processes

### Trigger.dev

**GitHub:** https://github.com/triggerdotdev/trigger.dev | **Website:** https://trigger.dev

- Open-source platform for building/deploying fully-managed AI agents and workflows in TypeScript
- **Checkpoint-resume system** enabling tasks to run indefinitely without timeouts
- Native Puppeteer support; integrates with Anchor Browser and Browserbase for server-side automation
- **No timeout limits** (unlike AWS Lambda/Vercel); automatic retries and durable execution
- Human-in-the-loop capability to pause tasks for approval; real-time streaming for LLM responses
- Configurable machines (set vCPU and RAM per task); supports scheduled cron tasks up to one year
- **Pricing**: Free ($5 monthly usage included), Starter $10, Pro $50; also self-hostable
- "BullMQ + Cron + Sentry + Kubernetes rolled into one developer-first package"

---

## 2. Low-Level/Specialized Browser Use

*Automation runtimes and specialized frameworks for fine-grained control*

### LaVague

**GitHub:** https://github.com/lavague-ai/LaVague | **Website:** https://www.lavague.ai/

- Open-source Large Action Model (LAM) framework for AI-powered web agents using natural language objectives
- **Two-component architecture**: World Model (analyzes webpage + objectives) + Action Engine (translates to executable Selenium/Playwright code)
- Defaults to OpenAI GPT-4o; uses local embeddings (bge-small-en-v1.5) for RAG to extract relevant HTML
- Employs Few-shot learning and Chain of Thought reasoning - no LLM fine-tuning required
- Multi-driver support: Selenium, Playwright, Chrome extension
- **LaVague QA**: Automates test writing by converting Gherkin specs into integration tests
- Outperforms Gemini and ChatGPT in information retrieval tasks
- **Community**: 6.2k GitHub stars

### Playwright

**Website:** https://playwright.dev | **GitHub:** https://github.com/microsoft/playwright

- Comprehensive testing framework by Microsoft for reliable end-to-end testing across all major browsers
- **Out-of-process model**: Tests run independently; uses persistent WebSocket (faster than HTTP/WebDriver)
- Cross-browser (Chromium, Firefox, WebKit) and cross-platform (Windows, Linux, macOS)
- **Auto-wait**: Automatically waits for elements to be actionable; "web-first assertions" with retry
- **Browser context isolation**: Full test isolation with minimal overhead; save/reuse auth state
- Parallel testing out of the box - **35-45% faster** than Selenium
- Tools: **Codegen** (records actions), **Inspector** (step-through debugging), **Trace Viewer** (DOM snapshots, network)
- Multi-language: TypeScript, JavaScript, Python, .NET, Java
- **Adoption**: VS Code, Microsoft, Disney+, Adobe; 15% market share, 235% YoY growth, 3.2M weekly npm downloads

### Puppeteer

**Website:** https://pptr.dev | **GitHub:** https://github.com/puppeteer/puppeteer

- JavaScript library by Google for controlling Chrome/Firefox over Chrome DevTools Protocol (CDP) or WebDriver BiDi
- **Direct protocol communication**: Bypasses WebDriver layer for quicker, more accurate interactions
- Dual packages: `puppeteer` (auto-downloads Chrome) and `puppeteer-core` (library only)
- **Headless-first design**: Defaults to invisible browser; visible mode available for debugging
- Capabilities: DOM queries, clicks, typing, network interception, screenshots, PDFs, performance metrics
- **Modern selectors**: Accessible selectors (`::-p-aria`) and text-based locators
- **2025 AI Integration**: Chrome DevTools MCP enables AI coding agents (Gemini CLI, Claude Code, Cursor) to control Chrome
- Exploring WebDriver BiDi and AI-powered self-healing tests

### Stagehand

**GitHub:** https://github.com/browserbase/stagehand | **Website:** https://www.stagehand.dev/

- Open-source AI browser automation framework by Browserbase - bridges low-level tools and high-level agents
- **Three-layer execution**: CDP Engine (low-level), `act()` (natural language single-step), `agent()` (multi-step), `extract()` (Zod schemas)
- **Hybrid AI + Code**: "Use AI when navigating unfamiliar pages, code when you know exactly what you want"
- **Self-healing & auto-caching**: Caches discovered elements, reduces LLM costs; remembers actions, adapts when sites change
- **Stagehand v3**: 44.11% faster; removes Playwright dependency; modular driver system (Puppeteer, any CDP driver)
- AI-native design: Context builder reduces token waste; self-healing execution adapts in real-time
- Preview actions before execution in production
- Also available as Python implementation (stagehand-python)
- Powers solutions for Vercel, Perplexity, Clay; Browserbase Series B at $300M valuation

---

## 3. Browsers as a Service

*Cloud infrastructure for hosting and managing browsers*

### Anchor Browser

**Website:** https://anchorbrowser.io/

- Cloud-hosted browser platform specifically for AI agents - turns fragile automation into deterministic workflows
- **Scale**: Up to 50,000 concurrent browsers per customer; unlimited sessions; any geo-location
- AI-powered: Natural language task definition with automated workload building
- **Custom Chromium fork** purpose-built to evade bot detection
- **Cloudflare Verified**: Official partnership providing verified bot status
- **Performance claims**: 12X faster, 80X fewer tokens, 23X less error-prone than competitors
- Security: SOC2 Type 2, ISO27001, HIPAA, GDPR compliance; full browser isolation
- Integrates with Okta, Azure AD; supports LangChain, multiple LLM providers
- **Pricing**: Free tier, Starter $20+/mo, Growth $1,500+/mo; usage-based ($0.09/hour, $8/GB proxy)
- Used by Groq, Composio, Google, Coinbase

### Browser.ai (Bright Data)

**Website:** https://brightdata.com/ai/agent-browser

- Serverless browsing infrastructure with built-in website unblocking
- **Proxy network**: 155M+ residential IPs across 195 countries
- Automatic unlocking: CAPTCHA solving, fingerprinting, retries, header/cookie selection, JS rendering
- Compatible with Playwright, Puppeteer, Selenium; unlimited concurrent sessions
- **AI Agent support**: Free tier 5,000 requests/month via Web MCP; supports LangChain, CrewAI, LlamaIndex
- **Performance**: 95% success rate, 100% speed score, ~2-second load times
- GUI and headless modes available
- **Pricing**: Scraping Browser $9.50/GB + $0.10/hour PAYG; Browser API $1,999/month

### Browserbase

**Website:** https://browserbase.com

- Comprehensive serverless platform for headless browsers - purpose-built for AI agents
- Spin up thousands of browsers in milliseconds with 4 vCPUs per browser
- Framework agnostic: Playwright, Puppeteer, Selenium, Stagehand, native CDP
- **Observability**: Session Inspector, Session Replay, live view iFrame embedding
- **Stagehand framework**: Open-source framework for building web agents
- **CUA Support**: 91% faster, 10x cheaper infrastructure for OpenAI/Gemini Computer Use Agent models
- Contexts API: Persist cookies and browser state across sessions
- SOC-2 Type 1 and HIPAA compliant; self-hosted options available
- **Pricing**: Free (1 browser hour), Developer $20/mo, Startup $99/mo, Scale custom

### Browserless

**Website:** https://browserless.io

- Cloud-based headless browser service - turns the web into an API
- Supports Chrome, Firefox, WebKit with both Puppeteer and Playwright
- **BrowserQL Technology**: Advanced automation with built-in anti-detection
- REST APIs for PDFs, screenshots, downloads; WebSocket endpoints for automation
- **Performance**: Screenshots ~1 second, PDFs ~2 seconds
- **Zero fingerprint strategy**: Custom-built to stay ahead of detection services
- Docker-based: Run in cloud or self-host
- **Unit-based pricing**: 1 Unit = 30 seconds browser time; Prototyping $25/mo (10,000 units)
- Free for non-commercial use

### Cua (Computer Use Anywhere)

**Website:** https://cua.browserbase.com/ | **GitHub:** https://github.com/trycua/cua

- Open-source framework for Computer-Use Agents - visual understanding and action execution
- **Vision-based interaction**: Uses vision-language models to perceive screens and reason about interfaces
- Multi-environment: Web, Windows Sandbox, cloud containers
- Works with OpenAI CUA, Anthropic Computer Use, and other AI models
- Operates through screen perception rather than DOM - robust to website changes
- Natural language control; cross-platform (desktop, browser, mobile)
- OpenAI's CUA is laser-focused on web-based tasks (vs Anthropic's broader desktop approach)
- **Pricing**: Free playground; trycua/cua open-source (MIT); Browserbase costs apply for deployment

### Hyperbrowser

**Website:** https://hyperbrowser.ai

- Internet infrastructure specifically for AI agents - instant, scalable browser infrastructure
- **AI-native APIs**: `page.ai()`, `page.extract()`, `executeTask()` for natural language automation
- **HyperAgent**: Open-source "Playwright supercharged with AI"
- Scale to **10,000+ concurrent browsers** with sub-500ms launch times
- Built-in CAPTCHA solving, proxy management, anti-bot detection, stealth mode
- MCP Support for seamless LLM connections
- **YC-backed**: Funded by Y Combinator, Accel, SV Angel
- Founded by ex-Meta engineer (Shri Sukhani)
- Credit-based pricing system; free tier available

### Kernel

**Website:** https://www.onkernel.com/

- Browser infrastructure with sandboxed, ready-to-use Chrome browsers
- **Unikernel architecture**: 300ms browser launch time - fastest in market
- Live view streaming for visual monitoring and remote control
- Session reuse: Persist cookies, auth, storage for human-like browsing
- Framework agnostic: Works with Browser Use, Magnitude, Playwright, Puppeteer
- High-performance proxies with dynamic IP rotation; automatic CAPTCHA solving
- **Team**: Co-founders from Clever (YC S12, $500M exit) and Sway Finance (YC S16)
- **Funding**: $22M Seed + Series A led by Accel, Y Combinator, Vercel Ventures
- HIPAA-compliant (SOC2 Type 2 pending)

### Steel.dev

**Website:** https://steel.dev/ | **GitHub:** https://github.com/steel-dev/steel-browser

- **Open-source** browser API for building AI apps that interact with the web
- Batteries-included: Manages sessions, pages, and browser processes automatically
- Full browser control via Puppeteer and CDP; session management with cookies/storage
- Built-in proxy chain management, Chrome extensions support, resource management
- Browser Tools: Convert pages to markdown, readability format, screenshots, PDFs
- Sessions API (stateful workflows) + Quick Actions API (direct operations)
- **Apache-2.0 license**: 6,000+ GitHub stars, active community
- Docker-based: Deploy to Railway, Render, or self-host
- **Steel Cloud** option or self-deploy; Hobby plan includes cloud browsers with basic anti-detection

---

## 4. Supporting Infrastructure

*Orchestration, state management, and authentication tools*

### Anon

**Website:** https://anon.com

- Integration platform enabling AI agents to authenticate and extract data from apps lacking APIs (~70% of enterprise software)
- **SOC 2 Type II compliant** with zero-persistence credential handling - credentials never stored
- Visual workflow builder: No-code drag-and-drop to record browser interactions
- Multi-format extraction: CSVs, PDFs, screenshots, DOM elements via REST APIs in JSON
- Auto-scaling with 99%+ uptime SLA; role-based access controls; isolated execution environments
- Four-step workflow: Authenticate -> Automate navigation -> Ingest via API -> Monitor dashboard
- Replaces expensive human ops teams, brittle DIY automation, or unreliable AI CV software

### Extruct.ai

**Website:** https://www.extruct.ai

- Deep research engine for company intelligence - delivers 50 carefully vetted companies with verified contacts
- Natural language queries analyzing thousands of data sources
- Custom data points: AWS usage, FDA approvals, SOC2 certs, tech stacks, contractor licenses, OSHA violations
- People discovery: Decision-makers with verified contacts from 20+ sources
- Industry focus: Blue collar/industrial, local SMB, deep tech, renewables, public sector
- CRM integration: Affinity, HubSpot, Attio, n8n
- Claims: Better search than Perplexity, lower pricing than Clay, more flexibility than Apollo

### Halluminate

**Website:** https://halluminate.ai

- Evaluation infrastructure, training datasets, and RL environments for AI agent reliability
- **Westworld**: Fully-simulated internet of synthetic consumer/enterprise apps where agents learn
- Managed sandboxes modeled after Salesforce, Slack, ticketing systems for safe training/testing
- **Web Bench benchmark**: 2,454 tasks across 452 live websites (expanding WebVoyager's 642 tasks on 15 sites to 5,750 tasks on 452 sites)
- Partnership with Skyvern for systematic benchmarking
- Plans to release automated evaluation harness for self-serve testing
- **YC-backed** (2024); targets Series A+ startups and enterprise ML teams

### Inngest

**Website:** https://inngest.com

- Backend workflow orchestration engine with unified durable functions for multi-step processes
- **Durable functions**: Step-based execution with deterministic replay after failures
- Automatic retry, replay for bulk recovery, bulk cancellation with concurrency management
- SDKs: JavaScript, Python, Go, Kotlin; deploy to servers or serverless
- Full visibility with live traces, metrics, alerting, step-by-step tracking
- **100K+ executions per second** with dynamic concurrency control
- SOC 2 compliance, end-to-end encryption, SSO/SAML, HIPAA BAA available
- Local dev with one CLI command: `npx inngest-cli dev`

### LangGraph

**GitHub:** https://github.com/langchain-ai/langgraph

- Low-level orchestration framework for stateful, long-running agents with failure resilience
- **Graph-based architecture**: Agents as interconnected nodes (inspired by Google Pregel, Apache Beam)
- **Durable execution**: Auto-resume from exact stopping point after interruptions
- Human-in-the-loop: Inspect and modify agent state at any point
- **Dual memory**: Short-term working memory + long-term persistent memory across sessions
- Low-level control: Developers specify architecture and prompts directly
- LangChain integration optional; works independently
- **LangSmith** for debugging/evaluation; **LangGraph Studio** for visual prototyping

### Lightpanda

**Website:** https://lightpanda.io | **GitHub:** https://github.com/lightpanda-io/browser

- **Open-source headless browser** built from scratch in Zig for AI agents
- **Performance**: 11x faster than Chrome, 9x less memory - excludes rendering engines entirely
- Architecture: Zig 0.15.2, libcurl HTTP, Netsurf HTML/DOM, V8 JS engine, Mimalloc allocator, CDP WebSocket
- Minimal stack: Pure DOM computation and script evaluation without GUI
- CDP compatible with Puppeteer and Playwright integration
- Expanding Web API coverage: DOM, XHR/Fetch, cookies, sessions, async operations
- **MIT license**; currently in Beta
- Use cases: Dynamic scraping, large-scale testing, LLM training data collection

### Morph.so

**Website:** https://cloud.morph.so

- Serverless cloud with **Infinibranch Browsers** - Chromium for massive concurrency at low cost
- **Pricing**: $0.07 per browser-hour; self-serve up to 1,024 concurrent browsers
- **Live-branching**: Fork running sessions to explore different paths without losing state
- Session snapshotting for deterministic replay and debugging
- Infinite persistence: Pause and resume workflows while maintaining stable state over hours/days
- Single API call creates session with instant CDP and connection URLs
- Live View for monitoring; compatible with Playwright and Puppeteer
- Philosophy: "The age of linear computing is behind us"

### Temporal

**Website:** https://temporal.io

- Open-source durable execution platform - applications survive failures without losing progress
- **Durable execution**: Captures state at every step; resumes exactly where stopped
- Workflows + Activities: Business logic + failure-prone operations with automatic retry/timeouts
- Built-in: Task queues, signal handling, timers, state persistence
- SDKs: Python, Go, TypeScript, Java, C#, Ruby, PHP
- Handles long-running workflows (days/months), Saga patterns, human-in-the-loop
- **Lineage**: Architects from AWS SQS, SWF, Azure Durable Functions, Uber Cadence
- **MIT license**: 17,000+ GitHub stars; used by Salesforce, NVIDIA, Twilio, Descript

---

## 5. Scraping & Crawling APIs

*Read-only web extraction that can be more economical than fully interactive agents*

### Apify

**Website:** https://apify.com

- Full-stack scraping platform with **1,600+ ready-made scrapers** ("Actors") in marketplace
- Ranked #1 in web scraping software on Capterra (97% recommendation rate)
- **Actor architecture**: Serverless microservices running seconds to hours
- Storage: Three types accessible via REST API; export as JSON, XML, CSV, Excel, HTML
- Proxy services: Smart rotation of datacenter and residential IPs
- Integrations: Make, Zapier, Slack, Airbyte, GitHub, Google Sheets
- Supports Crawlee (their library), Playwright, Puppeteer, Selenium, Scrapy
- Best for: Pre-built scrapers, marketplace solutions, flexible serverless automation

### Bright Data

**Website:** https://brightdata.com

- **Network scale**: 150M+ proxy IPs (72M residential, 1.6M datacenter, 7M mobile, 600K ISP) across 195 countries
- Web Scraper API: Auto proxy rotation, anti-bot bypass, JS rendering; 120+ ready scrapers
- Browser API: Fully managed auto-scaling browsers with unlimited concurrent sessions
- **Web Unlocker API**: Automates bypassing blocks/CAPTCHAs; pay only for successful results
- AI Integration (2025): Web MCP with 5,000 free requests/month; LangChain, CrewAI, LlamaIndex support
- **Ethical compliance**: Peer network with opt-in, zero personal data collection, industry-leading KYC
- Pricing: PAYG from $4/GB (residential); Growth plans from $499/month

### Exa.ai

**Website:** https://exa.ai

- **Meaning-based web search API** powered by embeddings rather than keyword matching
- Search types: Neural (embeddings), Fast, Auto, Deep (query expansion); 1-1000 results per request
- Content extraction: Full text, LLM highlights, AI summaries with custom JSON schemas, livecrawl
- Powerful filters: Date ranges, category (research papers, news, GitHub, PDFs), domain include/exclude
- Real-time indexing with continuous AI-powered crawling
- **MCP Server**: web_search, deep_search, get_code_context, company_research, crawling
- Integration: LangChain, LlamaIndex, CrewAI; Answer API for chat apps
- Best for: Semantic search, RAG systems, code documentation searches

### Firecrawl

**Website:** https://www.firecrawl.dev/ | **GitHub:** https://github.com/mendableai/firecrawl

- Turn entire websites into **LLM-ready markdown** or structured data
- **Open-source**: 69.6k GitHub stars, AGPL-3.0 license
- Output: Markdown, HTML, screenshots, structured data, links, metadata, images, summaries
- Endpoints: /scrape (single), /crawl (recursive), /map (rapid URL discovery), /search, /extract (AI-powered)
- Handles proxies, anti-bot, JS rendering; supports click/scroll/input actions before extraction
- Media parsing: PDFs, docx, images
- Integration: LangChain, Llama Index, Crew.ai, Dify, Flowise AI; Python and JS SDKs
- Best for: AI apps needing clean web data, comprehensive site crawling, structured extraction

### Kaizen

**Website:** https://www.kaizen.ai

- Browser automation API using sophisticated browser agents mimicking human interactions
- **Session caching**: Fast, stable connections across multiple logins; handles 2FA automatically
- API-first: Arbitrary code snippets; developers can inject custom code
- Deterministic workflows: Cached and replayed; "blocks" executed by AI computer use models
- Handles: 2FA, session management, anti-bot; no flaky bots when button positions change
- Target: Legacy portals in logistics, healthcare, financial services
- **YC-backed** (2025); founded by Kenneth Acquah and Michael Silver (MIT, Meta, Gather)
- Best for: Legacy systems without APIs, government/municipal portals, healthcare payer automation

### Parsera

**Website:** https://parsera.org

- No-code AI scraping tool using LLMs to extract visible data with natural language instructions
- Also available as lightweight Python library
- **Endpoints**: /v1/extract (URL), /v1/parse (HTML/string), /v1/extract_markdown
- Precision mode: Examines data hidden in HTML tags when standard extraction misses
- Built-in proxy with `proxy_country` parameter for geo-restricted content
- Output flexibility via alternative schema of attributes
- Deployment: Web app, local library, API for production
- Best for: Quick one-time extraction, non-coders, simple AI scraping

### Perplexity Search API (Sonar)

**Website:** https://www.perplexity.ai/api-platform

- Two models: Sonar (standard) and **Sonar Pro** with real-time web research and automatic citations
- Follows OpenAI chat completion format
- Search classifier automatically determines if web search needed based on query
- **Sonar Pro**: Leads SimpleQA benchmark (F-score 0.858); 2x more citations; 200K token context
- Features: JSON mode, search_domain_filter, search_recency_filter, return_related_questions
- **Pricing (2025)**: $5 per 1K searches, $3 per 750K input words, $15 per 750K output words
- Multi-step research: Multiple web searches synthesized into detailed answers
- Best for: Factual cited info, generative search, real-time web knowledge, chatbots with sources

### RiveterHQ

**Website:** https://riveterhq.com

- Replaces entire scraper infrastructure with single API - **parallel AI search agents**
- Each cell runs its own browsing agent: searches, clicks, reads documents, returns formatted results
- **Multi-modal**: Reads web pages, PDFs, images; follows links for better answers
- Structured outputs: Add column, write prompt, fill thousands of rows
- **Auditability**: Every result includes sources, reasoning, and agent path
- Custom API endpoints generated with one click
- **Free tier**: First 500 searches free
- Best for: Large-scale data enrichment, labeling at scale, custom data points

### Tavily

**Website:** https://www.tavily.com

- Web layer supplying enterprise agents with fast, real-time web data - **optimized for LLMs**
- APIs: Search, Extract (from URLs), Map (graph-based site mapping), Crawl (parallel traversal), Research (Beta)
- Unlike Bing/Google/SerpAPI: Reviews multiple sources to find most relevant content per source
- **Graph-based intelligence**: Hundreds of parallel paths with intelligent discovery
- Integration: LangChain, Vercel AI SDK, LlamaIndex, OpenAI, Google ADK, Anthropic, n8n, Make
- **MCP Server**: Production-ready for Claude and AI assistants
- **Pricing**: Free up to 1,000 credits/month for personal use
- Best for: AI agents needing real-time web, RAG apps, autonomous research (GPT Researcher style)

### Zyte

**Website:** https://www.zyte.com

- **All-in-one scraping API**: Automatic unblocking + managed browser + AI extraction
- Dynamic optimization: Routes requests efficiently, detects/bypasses blocks in real-time
- **AI-powered extraction**: Automatically adapts to layout changes; returns clean JSON
- Smart pricing: Tier-based from $0.13/1K (HTTP) to $1.00/1K (browser-rendered)
- Automatic data types: eCommerce products, news, jobs, real estate, search results
- **Scrapy Cloud**: Deploy, schedule, manage Scrapy spiders without own servers
- API Playground: Test with real-time samples before committing
- Best for: All-in-one solution, Scrapy users, AI-powered extraction, automated quality feeds

---

## Quick Reference: Decision Flow

```
Is interaction required? (login, form submission, file upload)
├── NO → Consider Scraping APIs (Category 5) for cheaper read-only extraction
└── YES → Go agentic:
    ├── Pick control layer (Category 1: Browser Use Frameworks)
    │   └── Browser Use, Stagehand, Skyvern based on speed vs reliability needs
    ├── Pick infrastructure (Category 3: Browsers as a Service)
    │   └── Browserbase, Anchor, Hyperbrowser based on replay/observability/anti-bot needs
    └── Pick model (Computer Use models - not covered here)
        └── Claude Computer Use, OpenAI CUA, Gemini 2.5
```

## Common Problems

| Problem | Description |
|---------|-------------|
| **CAPTCHAs & bot detection** | Cloudflare, Google, DataDome using fingerprinting and behavioral scoring |
| **Timeouts & race conditions** | Nondeterministic server responsiveness disrupts timing-dependent logic |
| **Layout & selector drift** | DOM heuristics break as sites update or randomize elements |
| **Authentication flows** | Models struggle with complex stateful interactions (login, payment) |
| **Cost & scaling** | Browsers need CPU/memory; vision loops add cost; concurrent sessions are nontrivial |

---

## Key Paper: Scaling Computer-Use Agents (bBoN)

**Paper**: "The Unreasonable Effectiveness of Scaling Agents for Computer Use" (arXiv:2510.02250, Oct 2025)
**Authors**: SIMULAR Research (same team as Agent-S)

### Core Idea

**Wide scaling**: Instead of improving one agent, run N agents in parallel and pick the best trajectory.

```
Multiple Rollouts → Behavior Narratives → Comparative Judge → Best Trajectory
```

### Results

| Method | OSWorld 100-step |
|--------|------------------|
| Previous SOTA (CoAct-1) | 59.9% |
| Agent S3 alone | 62.6% |
| Agent S3 + bBoN (N=10) | **69.9%** |
| Human performance | 72.0% |

- GPT-5 Mini: 49.8% → 60.2% with bBoN (+10.4% absolute)
- Near human-level performance achieved

### Technical Contributions

#### 1. Behavior Narratives
- **Problem**: Raw trajectories too long/noisy for judges to evaluate
- **Solution**: Convert each step into "facts" describing what actually changed
- For each transition: `(screenshot_before, action, screenshot_after)` → fact
- Visual augmentations: red circle (click), blue circle (moveTo), green circle + line (drag)
- Zoomed crops around action coordinates for fine-grained verification
- 3-second delay after actions for page loads

**Ablation (Table 4)**:
| Representation | Success Rate |
|----------------|--------------|
| Screenshots only | 56.0% |
| Naive captioning | 56.8% |
| **Behavior Narratives** | **60.2%** |

Key insight: Need **transition-level** understanding (before→after), not just state captioning.

#### 2. Comparative vs Independent Ranking
- WebJudge (independent scoring) plateaus at N=4 and drops at N=10
- bBoN (comparative MCQ) keeps scaling with more rollouts
- **Must compare trajectories head-to-head**, not score independently

#### 3. Agent S3 Improvements
- **Flat policy** instead of hierarchical Manager-Worker
  - 52% fewer LLM calls
  - 62% faster execution
  - +9.1% success rate
- **Coding agent** integrated into GUI agent's action space
  - Agent decides when to delegate to code
  - Bounded inner loop with budget B
  - Returns summary + verification checklist to GUI agent

#### 4. Mixture-of-Models
| Mixture | Success Rate | Coverage (Pass@N) |
|---------|--------------|-------------------|
| GPT-5 alone | 66.5% | 74.7% |
| GPT-5 + Gemini 2.5 Pro | **66.7%** | **78.0%** |
| All 4 models | 65.9% | 75.4% |

**Insight**: Diversity > raw capability for coverage. Best combo is two strong diverse models.

### Failure Modes (12 remaining failures)

#### 1. Vision Hallucinations (8/12)
- VLM misses fine-grained details (e.g., negative sign "-17.0" read as "17.0")
- Zooming helps but doesn't fully solve
- **Fundamental VLM limitation**

#### 2. GUI-Code Handoff Failures (4/12)
- Code agent succeeds but GUI agent doesn't verify properly
- GUI agent redoes task via GUI actions → creates verbose narrative
- **Judge biased toward verbosity** - more actions ≠ better trajectory

### Judge Accuracy

| Metric | Judge Subset | Full Set |
|--------|--------------|----------|
| Benchmark alignment | 78.4% | 69.9% |
| Human alignment | **92.8%** | 76.3% |

Gap explained by imperfect OSWorld evaluation scripts (only check one pre-defined solution).

### Generalization

| Benchmark | Baseline | + bBoN (N=3) | Gain |
|-----------|----------|--------------|------|
| WindowsAgentArena | 50.2% | 56.6% | +6.4% |
| AndroidWorld | 68.1% | 71.6% | +3.5% |

Zero-shot transfer without modification.

### Limitations

1. **Requires VM snapshots** - need repeatable initial states for parallel rollouts
2. **Shared online resources** - concurrent rollouts can interfere (e.g., same shopping cart)
3. **Not applicable to real desktops** - can't isolate side effects without VMs

### Key Design Decisions from Prompts

1. **GUI agent must close and reopen applications** after code agent modifies files (reload insufficient)
2. **Code agent must print file contents** before returning DONE (enables verification)
3. **Preserve document structure** - only change content, not formatting/layout
4. **Clean desktop rule** - close any popups/tabs opened during task
5. **Three-case reflection** - off-track, on-track, or done (no specific action suggestions)

### Implications for Research

1. **Scaling > Architecture**: Even weak models benefit massively from wide scaling
2. **Hierarchy is dead**: Flat policy beats Manager-Worker and is 2x faster
3. **Verbosity bias is real**: Judges prefer longer narratives even when wrong
4. **Vision is the bottleneck**: Fine-grained text recognition remains unsolved

---

*Research compiled from [reliableagents.ai](https://reliableagents.ai/2025-Q4) and individual tool documentation.*
