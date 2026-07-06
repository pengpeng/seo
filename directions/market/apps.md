# market/apps.md — Olares Market 应用清单

> 从 [terminus-apps/](/Users/pengpeng/terminus-apps)（`beclab/apps` 本地克隆）的 365 个 manifest 收敛去重而来，共 **175** 个用户可见品牌应用。每个应用的 brand-seo-research 报告放在 [reports/](/Users/pengpeng/seo/directions/market/reports)。用途/对标见各条；写新报告走 `.cursor/skills/brand-seo-research/`。

**去重规则**：版本变体保留最新（v3>v2>无后缀）；模型服务变体（`ollama*`/`vllm*`/`sglang*`/`llamacpp*`/`xinference*` 共 68 个）折叠为 5 个引擎品牌，型号清单见 [model/keywords.md](/Users/pengpeng/seo/directions/model/keywords.md)；剔除 test*/`*client`/`*share`/`*fusion`/`*pure`/`*forcluster` 等伴生 chart 与纯中间件/数据库。

状态：✅ 已有报告 ｜ ⬜ 待做

## 模型服务 / 推理引擎（5）

| 应用 | 说明 | 报告 |
|------|------|------|
| Ollama | 本地大模型运行引擎（含 40+ 预置模型变体） | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/ollama.md) |
| vLLM | 高吞吐 LLM 推理引擎 | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/vllm.md) |
| SGLang | 高性能 LLM 推理引擎 | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/sglang.md) |
| llama.cpp | 轻量本地 LLM 推理 | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/llamacpp.md) |
| Xinference | 一站式模型部署 / 推理框架 | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/xinference.md) |

## AI（7）

| 应用 | 说明 | 报告 |
|------|------|------|
| DeepSeek-OCR2 WebUI V3 | Ready-to-use DeepSeek-OCR-2 Web UI | ✅ [报告](directions/market/reports/deepseek-ocr2-webui.md) |
| Fish Speech | SOTA Open Source TTS | ✅ [报告](directions/market/reports/fish-speech.md) |
| KoboldCpp | 本地 LLM 推理与角色扮演前端 | ✅ [报告](directions/market/reports/koboldcpp.md) |
| OpenedAI Speech | An OpenAI API compatible text to speech server using Coqui AI and/or piper TTS as the backend. | ✅ [报告](directions/market/reports/openedai-speech.md) |
| Rembg | Rembg is a tool to remove images background | ✅ [报告](directions/market/reports/rembg.md) |
| Whisper API | FastAPI service on top of WhisperX | ✅ [报告](directions/market/reports/whisper-api.md) |
| Whisper-WebUI | A Web UI for easy subtitle using whisper model. | ✅ [报告](directions/market/reports/whisper-webui.md) |

## 生产力 / 协作（58）

| 应用 | 说明 | 报告 |
|------|------|------|
| AFFiNE | Open-source alternative for Notion, Miro and Airtable. | ✅ [报告](reports/affine.md) |
| Agent Zero | Agentic AI Framework | ✅ [报告](directions/market/reports/agent-zero.md) |
| AI Router | AI Router | ✅ [报告](directions/market/reports/ai-router.md) |
| Answer | A Q&A platform software for teams at any scales. | ✅ [报告](directions/market/reports/answer.md) |
| BISHENG | Open LLM devops platform for next generation Enterprise AI applications | ✅ [报告](directions/market/reports/bisheng.md) |
| Blinko | An open-source, self-hosted personal AI note tool prioritizing privacy | ✅ [报告](directions/market/reports/blinko.md) |
| Cloudreve | Self-hosted file management system with muilt-cloud support. | ✅ [报告](directions/market/reports/cloudreve.md) |
| DeerFlow 2.0 | DeerFlow 2.0 is an open-source super agent harness for deep research. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/deerflow.md) |
| Dify | The Innovation Engine for GenAI Applications | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/dify.md) |
| Docmost | Open-source collaborative wiki and documentation software. | ✅ [报告](directions/market/reports/docmost.md) |
| Documenso | The Open Source DocuSign Alternative. | ✅ [报告](directions/market/reports/documenso.md) |
| Excalidraw | Virtual whiteboard for sketching hand-drawn like diagrams | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/excalidraw.md) |
| FastGPT | A knowledge-based platform built on the LLMs | ✅ [报告](reports/fastgpt.md) |
| Flowise | Drag & drop UI to build your customized LLM flow | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/flowise.md) |
| Formbricks | Open Source Qualtrics Alternative | ✅ [报告](directions/market/reports/formbricks.md) |
| Freqtrade | Free, open source crypto trading bot | ✅ [报告](directions/market/reports/freqtrade.md) |
| FreshRSS | A free, self-hostable feed aggregator. | ✅ [报告](reports/freshrss.md) |
| Grafana | Grafana is a multi-platform open source analytics and interactive visualization web application. | ✅ [报告](directions/market/reports/grafana.md) |
| Hermes Agent | The agent that grows with you | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/hermes-agent.md) |
| IsaacLab | Unified framework for robot learning built on NVIDIA Isaac Sim | ✅ [报告](directions/market/reports/isaaclab.md) |
| Langfuse | Open source LLM engineering platform | ✅ [报告](reports/langfuse.md) |
| Leantime | Leantime is a goals focused project management system for non-project managers. | ✅ [报告](directions/market/reports/leantime.md) |
| Listmonk | High performance, self-hosted, newsletter and mailing list manager with a modern dashboard | ⬜ |
| Mattermost | An open source platform for secure collaboration across the entire software development lifecycle. | ✅ [报告](reports/mattermost.md) |
| MaxKB | Ready-to-use, flexible RAG Chatbot | ⬜ |
| Medusa | The world's most flexible commerce platform. | ⬜ |
| Memos | Effortlessly craft your impactful content. | ⬜ |
| MTranServer | A high-performance offline translation server with minimal resource requirements | ⬜ |
| n8n | n8n is an extendable workflow automation tool. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/n8n.md) |
| Nextcloud | The productivity platform that keeps you in control | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/nextcloud.md) |
| NocoBase | Extensibility-first, open-source, no-code platform | ⬜ |
| NocoDB | Open Source Airtable Alternative. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/nocodb.md) |
| NOFX | Your personal AI trading assistant. Any market. Any model. | ⬜ |
| Novel | Notion-style WYSIWYG editor with AI-powered autocompletion | ⬜ |
| Obsidian LiveSync | Obsidian sync server. | ✅ [报告](reports/obsidian-livesync.md) |
| Odoo | All your business on one platform. | ⬜ |
| OnlyOffice | Run your private office with the ONLYOFFICE | ✅ [报告](reports/onlyoffice.md) |
| Open Notebook | A powerful open-source, AI-powered note-taking/research platform that respects your privacy | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/open-notebook.md) |
| OpenClaw | Personal AI Assistant with Multi-channel Inbox Support | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/openclaw.md) |
| Paperclip | Open-source orchestration platform for AI agent companies. | ⬜ |
| PDFMathTranslate | PDF scientific paper translation with preserved formats. | ⬜ |
| Plane | Open Source JIRA, Linear, Monday, and Asana Alternative | ✅ [报告](reports/plane.md) |
| Qinglong | Timed Task Management Platform | ⬜ |
| Radicale | Free and Open-Source CalDAV and CardDAV Server | ⬜ |
| RAGFlow | An open-source RAG engine based on deep document understanding. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/ragflow.md) |
| Rallly | Open-source scheduling and collaboration tool designed to make organizing events and meetings easier | ⬜ |
| Refly | The Open-Source Agentic Workspace for Human-AI Collaboration. | ⬜ |
| RNA Sequencing | An end-to-end GPU-powered workflow for scRNA-seq using RAPIDS | ⬜ |
| SearXNG | Search without being tracked. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/searxng.md) |
| SeaTable | SeaTable is a no-code database and app-building platform. | ⬜ |
| SimpleMindMap | A simple and powerful mind mapping library for the Web. | ⬜ |
| solidtime | Modern open-source time-tracking app | ⬜ |
| Stirling-PDF | A locally hosted one-stop shop for all your PDF needs. | ⬜ |
| Teable | The Next Gen Airtable Alternative: No-Code Postgres | ✅ [报告](reports/teable.md) |
| TradingAgents | Multi-Agents LLM Financial Trading Framework | ⬜ |
| Twenty | The #1 Open-Source CRM - A modern alternative to Salesforce | ⬜ |
| Vane | Vane (previously Perplexica) is an AI-powered answering engine. | ✅ [报告](reports/vane.md) |
| Wise | Your Digital Secret Garden | ⬜ |

## 开发者工具（28）

| 应用 | 说明 | 报告 |
|------|------|------|
| Appsmith | Platform to build admin panels, internal tools, and dashboards | ⬜ |
| AstrBot | Easy-to-use Multi-platform LLM Chatbot & Development Framework | ⬜ |
| Bytebase | World's most advanced database DevOps and CI/CD for Developer, DBA and Platform Engineering teams. | ⬜ |
| Claude Code | Anthropic's official agentic coding CLI that lives in your terminal | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/claude-code.md) |
| Code Server | VS Code in the browser | ⬜ |
| Coder | Self-Hosted Cloud Development Environments. | ⬜ |
| Codex CLI | OpenAI's lightweight coding agent that runs in your terminal | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/codex-cli.md) |
| Context7 | Up-to-date code documentation for LLMs and AI code editors | ⬜ |
| Crawl4AI | Open-source LLM Friendly Web Crawler & Scrape | ⬜ |
| Directus | A composable data platform to build your Headless CMS, BaaS, and more. | ⬜ |
| Falco | Cloud Native Runtime Security tool for detecting abnormal behavior. | ⬜ |
| Gitea | Git with a cup of tea! | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/gitea.md) |
| GitLab | A web-based Git repository management tool. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/gitlab.md) |
| Hasura | Blazing fast, instant realtime GraphQL APIs on your DB with fine grained access control, also trigger webhooks on database events. | ⬜ |
| Hoppscotch | Open source API development ecosystem. | ⬜ |
| JupyterHub | Deploying JupyterHub on Olares | ⬜ |
| LangBot | Production-grade platform for building agentic IM bots | ⬜ |
| LLaMA Factory | Easily fine-tune 100+ large language models with zero-code CLI and Web UI | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/llama-factory.md) |
| LLMFit | Web Dashboard for hardware-aware LLM recommendations | ⬜ |
| Metabase | Business Intelligence and Embedded Analytics tool that lets everyone work with data | ⬜ |
| NemoClaw | NVIDIA NemoClaw - AI Coding Agent with Sandbox Isolation | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/nemoclaw.md) |
| Netdata | High-performance, open-source observability platform | ⬜ |
| OpenCode | The open source AI coding agent | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/opencode.md) |
| redroid | Remote-Android, a multi-arch, GPU enabled, Android in Cloud solution. | ⬜ |
| ShowDoc | A tool greatly applicable for an IT team to share documents online | ⬜ |
| Studio | Olares 应用开发 / 部署工作台 | ⬜ |
| Uptime Kuma | A fancy self-hosted monitoring tool | ✅ [报告](reports/uptime-kuma.md) |
| XYBotV2 | Feature-rich WeChat Bot framework | ⬜ |

## 创意 / 设计 / 媒体生成（13）

| 应用 | 说明 | 报告 |
|------|------|------|
| ACE-Step 1.5 | The most powerful local music generation model that outperforms most commercial alternatives | ⬜ |
| ComfyUI | The most powerful and modular stable diffusion GUI and backend. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/comfyui.md) |
| EchoMimic | 音频驱动的数字人 / 口型生成 | ⬜ |
| FaceFusion | Industry leading face manipulation platform | ⬜ |
| Ghost | Independent technology for modern publishing, memberships, subscriptions and newsletters. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/ghost.md) |
| Halo | Powerful and easy-to-use open source website building tool | ⬜ |
| HeyGem | 本地数字人视频生成（HeyGen 平替） | ⬜ |
| Hunyuan3D | 腾讯混元 3D 模型生成 | ⬜ |
| Jaaz | AI design agent, local alternative for Lovart | ⬜ |
| Owncast | A free and open source live video and web chat server for use with existing popular broadcasting software. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/owncast.md) |
| Penpot | Penpot is the web-based open-source design tool that bridges the gap between designers and developers. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/penpot.md) |
| WeChat Markdown Editor | A minimalist Markdown editor for WeChat | ⬜ |
| WordPress | Blog Tool, Publishing Platform, and CMS | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/wordpress.md) |

## 娱乐 / 媒体库（19）

| 应用 | 说明 | 报告 |
|------|------|------|
| Astral | Nostr client made with Quasar. | ⬜ |
| AudioBookShelf | A self-hosted audiobook and podcast server. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/audiobookshelf.md) |
| Bazarr | A companion subtitle manager to Sonarr and Radarr. | ⬜ |
| Bluesky PDS | Bluesky Personal Data Server | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/bluesky-pds.md) |
| Calibre | Web app for browsing, reading and downloading eBooks stored in a Calibre database. | ⬜ |
| Calibre-Web | Web app for browsing, reading and downloading eBooks stored in a Calibre database | ⬜ |
| Hubble | An official Farcaster Hub implementation | ⬜ |
| Jellyfin | The Free Software Media System | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/jellyfin.md) |
| Komga | A media server for your comics, mangas, BDs, magazines and eBooks. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/komga.md) |
| Lidarr | A music collection manager for Usenet and BitTorrent users | ⬜ |
| Mastodon | Your self-hosted, globally interconnected microblogging community | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/mastodon.md) |
| Miniflux | Miniflux is a minimalist and opinionated feed reader. | ⬜ |
| Navidrome | Your Personal Streaming Service | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/navidrome.md) |
| Prowlarr | Integration of various PVR applications | ⬜ |
| Radarr | A movie collection manager for Usenet and BitTorrent users. | ⬜ |
| Sickchill | SickChill is an automatic Video Library Manager for TV Shows. | ⬜ |
| SillyTavern | LLM Frontend for Power Users | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/sillytavern.md) |
| Sonarr | Smart PVR for newsgroup and bittorrent users. | ⬜ |
| Steam Headless | A Headless Steam Service | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/steam-headless.md) |

## 生活 / 家居 / 健康（11）

| 应用 | 说明 | 报告 |
|------|------|------|
| Firefly III | A personal finances manager | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/firefly-iii.md) |
| Frigate NVR | NVR with realtime local object detection for IP cameras | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/frigate-nvr.md) |
| Home Assistant | Awaken your home | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/home-assistant.md) |
| HomeBox | A continuation of HomeBox the inventory and organization system built for the Home User | ⬜ |
| Immich | High performance self-hosted photo and video management solution. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/immich.md) |
| Mealie | A Place For All Your Recipes | ⬜ |
| MiGPT | Connect your Xiaomi Smart Speaker to ChatGPT and Doubao, and turn it into your personal voice assistant. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/migpt.md) |
| MiGPT-TTS | TTS module for MiGPT | ⬜ |
| PhotoPrism | AI-Powered Photos App for the Decentralized Web | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/photoprism.md) |
| Photoview | Photo gallery for self-hosted personal servers | ⬜ |
| TREK | A self-hosted, real-time collaborative travel planner | ⬜ |

## 实用工具 / 网络 / 存储（34）

| 应用 | 说明 | 报告 |
|------|------|------|
| AdGuard Home | Network-wide ads & trackers blocking DNS server | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/adguard-home.md) |
| AnythingLLM | The all-in-one AI app you were looking for | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/anythingllm.md) |
| Bifrost | The Fastest Enterprise AI Gateway | ⬜ |
| Chromium | The open-source projects behind the Google Chrome browser | ⬜ |
| Deluge | A lightweight and free BitTorrent client. | ⬜ |
| Firecrawl | Empower your AI apps with clean data from any website | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/firecrawl.md) |
| Firefox | Firefox Browser | ⬜ |
| FlareSolverr | Proxy server to bypass Cloudflare and DDoS-GUARD protection. | ⬜ |
| Jackett | API Support for your favorite torrent trackers | ⬜ |
| JDownloader 2 | Free, open-source download management tool with web browser access. | ⬜ |
| JSON Hero | Make reading and understand JSON files easy. | ⬜ |
| Karakeep | A self-hostable bookmark-everything app with AI-based automatic tagging and search. | ⬜ |
| LibreChat | Enhanced ChatGPT Clone with Agents, MCP, and Multi-Model Support | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/librechat.md) |
| LibreSpeed | Free and Open Source Speedtest. | ⬜ |
| LiteLLM | Call 100+ LLMs in OpenAI format | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/litellm.md) |
| LobeChat | An open-source, modern-design AI chat framework. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/lobechat.md) |
| LocalAI | The free, Open Source alternative to OpenAI, Claude and others. | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/localai.md) |
| MacOS | Run MacOS on Olares | ⬜ |
| Magic Pig Demo | A cute digital pig that brings joy and fun to your daily interactions. Experience delightful animations, playful cursor-following behavior, and interactive fun that brightens up your day. | ⬜ |
| MemPalace | Local-first AI memory with semantic search and an MCP server | ⬜ |
| Metube | Self-hosted YouTube downloader | ⬜ |
| ntfy | Push notifications made easy | ⬜ |
| Nzbget | Efficient Usenet downloader. | ⬜ |
| Open WebUI | User-friendly WebUI for LLMs | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/open-webui.md) |
| PaddleOCR | Text Recognition & Doc Parsing Toolkit | ⬜ |
| qBittorrent | Free BitTorrent downloader | ⬜ |
| Rsshub | A extensible RSS feed generator | ⬜ |
| Speaches | OpenAI-compatible TTS/STT server | ⬜ |
| TensorZero | Open-source stack for industrial-grade LLM applications | ⬜ |
| Transmission | Transmission is a cross-platform BitTorrent client | ⬜ |
| WeWe RSS | More elegant WeChat Official Account subscription method. | ⬜ |
| Windows | Run Windows on Olares | ✅ [报告](/Users/pengpeng/seo/directions/market/reports/windows-vm.md) |
| Windows ARM64 | Run Windows ARM64 on Olares | ⬜ |
| YT Navigator | AI-powered YouTube content explorer | ⬜ |

---
> 报告覆盖：50/175 已有。其余增量补齐；待跑排期见 [directions/backlog.md](/Users/pengpeng/seo/directions/backlog.md)。
> **平台竞品**：`reports/` 另有 [seafile.md](/Users/pengpeng/seo/directions/market/reports/seafile.md)、[yunohost.md](/Users/pengpeng/seo/directions/market/reports/yunohost.md) 两份"个人云平台"竞品（Nextcloud 同类），不占本清单应用计数。
