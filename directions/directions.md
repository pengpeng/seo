# directions.md — 主线1：方向（事实 → 洞见）

> 回答"往哪打"。这里是对**市场事实**的了解与由此产生的洞见：哪些人已经在为哪些 AI 产品付费、Olares 用什么资产去承接、机会在哪。产品进度见 [scenarios.md](/Users/pengpeng/seo/scenarios/scenarios.md)。
>
> 数据来源：commerce/model/market/hardware/privacy/tech/iot 各 `reports/` 下的 Semrush 竞品报告 + 汇总词库 [reference/olares-500-keywords-analysis-2026-07-03.md](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md)。搜索量为**美国月均**，技术类产品全球量通常为美国的 3-5 倍。

---

## 0. 我方产品事实（我们能拿出来打的能力）

写任何方向的内容前，先记住 Olares 实际能提供什么。品牌叙事见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md) 品牌口径，这里只列"事实型能力"。

### 对外能力（讲内容准确即可）

Olares 把云计算复杂度包进一层"像手机一样简单"的外壳，对外是一整套能力：

1. **统一存储与文件**：跨设备统一文件系统，随处访问、同步、可挂载外部云盘。
2. **内置数据库与中间件**：应用开箱即用生产级数据库/缓存/消息队列，无需自搭。
3. **单点登录 + 零配置网络**：一次登录访问所有应用；自动域名、免费 HTTPS、VPN、内网穿透全自动。
4. **GPU 与本地 AI 管理**：统一管理 GPU、本地托管大模型，多应用共享算力。
5. **内置系统应用**：Desktop 桌面/启动器 ｜ Files 文件（同步+挂载云盘）｜ Vault 密码管理（1Password 替代）｜ Market 应用市场 ｜ Wise 本地优先 AI 阅读器 ｜ Settings ｜ Control Hub 可视化集群控制台 ｜ Studio 开发/部署 ｜ Profile 个人主页。

> 底层用到的具体开源组件（K3s / JuiceFS / Authelia 等）不进品牌首屏，但它们本身是**方向 6**的长尾词库，收在 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)。

### Agent / 资源语言能力（写开发者与 Agent 内容时用）

- 声明式契约：每个 app = **Helm chart + `OlaresManifest.yaml`（OAC）**，声明元数据、entrance（public/private/internal）、权限、中间件依赖、GPU 模式、环境变量。
- 校验/打包：`olares-cli chart lint | package | from-compose`。
- `olares-cli` 三模式：Host / **User（^1.12.5，任意机器远程操作）** / **In-cluster（^1.12.6，app 容器内直接操作系统，权限由 OlaresManifest 界定）**。
- 官方 **Agent Skills**（olares-shared/files/market/settings/dashboard/cluster/chart/publish/search）+ **系统级 MCP 支持（v1.12）**。
- LLM 托管是"应用模式"：通过 `llm-init` 基础 chart 跑 Ollama / vLLM / llama.cpp / SGLang；共享应用（如 Ollama）装一次，其他 app 服务注入消费。
- 面向 Agent 入口：`npx @olares/cli install`（装 CLI + Skills）→ Olares ID 登录 → 自然语言驱动。

### 生态资产：Market 应用速查（做 "X on Olares / X alternative" 选题）

- **AI Agent**：OpenClaw、NemoClaw、Hermes Agent、OpenCode、Claude Code、DeerFlow、TradingAgents、Paperclip、NOFX
- **AI 工作台 / RAG**：Open WebUI、LobeChat、AnythingLLM、Open Notebook、Dify、Vane(Perplexica)
- **模型服务 / 网关**：Ollama（共享）、LiteLLM、Bifrost、TensorZero、LLMFit
- **生成式媒体**：ComfyUI、Stable Diffusion WebUI、ACE-Step、Whisper-WebUI、Speaches、IndexTTS2、Duix.Avatar
- **具身/机器人**：Isaac Lab
- **媒体娱乐**：Jellyfin、Immich、Navidrome、Komga、*Arrs、Steam Headless
- **生产力/设计**：Plane、Excalidraw、Penpot、Stirling PDF、Karakeep、Nextcloud
- **开发工具**：JupyterHub、Firecrawl、Context7、Hoppscotch、SearXNG、Studio
- **虚拟机/容器**：Windows VM、macOS VM、redroid（云 Android）
- **实用/安全/网络**：Falco、PDFMathTranslate、YT-DLP

---

## 七个方向

每个方向：**市场事实 → 已验证付费竞品 → 对应 Olares 资产 → 洞见 → 关联词库分类/报告**。

### 方向 1：用户已付费的商业 AI 产品

**市场事实**：用户已经为云端 AI 订阅持续付费——ChatGPT/Claude 对话、Lovable/Manus 自然语言造应用、Cursor/Copilot/Devin 编码、Midjourney/Runway 出图。这些是需求已被验证、且用户带着"月费在涨"痛点的入口。

**已验证付费竞品**：ChatGPT、Claude、Lovable、Manus、Cursor、GitHub Copilot、Devin、Windsurf、Tabnine。

**对应 Olares 资产**：Open WebUI + Ollama（对话）、Market 里的 Agent/vibe-coding 应用、Continue.dev（编码）、Olares One（本地算力）。核心叙事：把"每月续费的智能"变成"一次买断、本地拥有"。

**洞见**：
- 大词（chatgpt alternative 18,100/KD47、cursor alternative 880/KD25）难但价值高，作为 6-12 月权威内容；真正立即能赢的是低 KD 平替词：`tabnine self-hosted`（KD=0）、`github copilot alternative`（KD=13）、`open source chatgpt alternative`（KD=19）。
- 编码词普遍高 CPC（$6-13），商业意图强：`devin pricing` $13.19、`ai software engineer` $12.43，适合做 D 级线索内容。
- Lovable 洞见：其成本随项目膨胀，正好反衬 Olares "本地模型不涨价、无中间商加价"。

**关联**：500 词分类 1（ChatGPT 替代 35 词）、分类 8（AI 编码 20 词）、分类 14（借力大词）；商业竞品清单与报告见 [commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md) 与 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)（OpenAI/Anthropic/Midjourney/ElevenLabs/Zapier 等产品）；另 [commerce/reports/lovable.md](/Users/pengpeng/seo/directions/commerce/reports/03-application/vibe-coding/lovable.md)（vibe coding）、[market/reports/claude-code.md](/Users/pengpeng/seo/directions/market/reports/claude-code.md)、[market/reports/codex-cli.md](/Users/pengpeng/seo/directions/market/reports/codex-cli.md)。

---

### 方向 2：Olares Market 支持的应用（部分是商业版平替）

**市场事实**：大量成熟商业 SaaS 都有可自托管的开源平替，且这些平替本身就有稳定搜索需求。Olares Market 已上架其中很多，装即可用。

**已验证付费/对标**：Google Photos→Immich、Notion→AppFlowy、Obsidian→AppFlowy/Drive、Slack→Mattermost/Rocket.Chat、Plex→Jellyfin、1Password/Bitwarden→Vault、Zapier→n8n/Activepieces、Perplexity→Perplexica、GitHub→Gitea。

**对应 Olares 资产**：见 §0 生态速查——这些平替大多已在 Market，转化路径清晰（选题→安装教程→Market 一键装）。

**洞见**：
- 这是**最高杠杆**方向：低 KD 平替 + 对比词极多。金矿词：`open webui alternative`（KD=4）、`activepieces vs n8n`（KD=4）、`keepassxc vs bitwarden`（KD=3）、`zerotier alternative`（KD=5）、`logseq alternative`（KD=6）、`mattermost vs slack`（KD=8）、`perplexity alternative`（KD=11）、`librechat vs open webui`（KD=12）。
- 品牌大词（jellyfin 8,100/KD71、n8n 60,500/KD82、dify 8,100/KD56）不硬刚，用其低 KD 平替/对比长尾承接。
- olares.com 现有唯一跑出的非品牌内容就是**具体应用部署教程**（FlareSolverr、DUIX），印证"X on Olares 教程"是当前最有效内容。

**关联**：500 词分类 3（Open WebUI 30）、分类 4（Ollama 25）、分类 5（ComfyUI 25）、分类 6（n8n/工作流 20）、分类 7（Market 应用对标 70）；报告见 [market/reports/](/Users/pengpeng/seo/directions/market/reports)（open-webui、dify、immich、jellyfin、n8n、nocodb、penpot、nextcloud、gitea 等）与清单 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md)。

---

### 方向 3：模型（LLM、图片、音视频）

**市场事实**：本地/开源模型热度高，用户想"在自己机器上跑 X 模型"。图像/视频/音频类平替词 KD 普遍极低。

**已验证付费/对标**：云对话（ChatGPT/Claude）、云出图（Midjourney、GPT-Image、Nano Banana）、语音（ElevenLabs、Suno、Udio）、数字人（HeyGen、Synthesia、D-ID）。开源侧模型：Qwen、GLM、Gemma、Kimi、FLUX、HiDream、Ideogram、Wan、Kokoro TTS。

**对应 Olares 资产**：Ollama/vLLM/llama.cpp/SGLang（LLM 托管）、ComfyUI + FLUX（出图）、ACE-Step（音乐）、Kokoro/IndexTTS（TTS）、Whisper（STT）、Duix.Avatar（数字人）+ Olares One 本地算力。

**洞见**：
- 音视频平替词是**低 KD 富矿**：`comfyui local`（KD=0）、`udio alternative`（KD=4）、`d-id alternative`（KD=7）、`comfyui alternative`（KD=7）、`elevenlabs alternative`（KD=9）、`heygen alternative`（KD=13）、`synthesia alternative`（KD=12，CPC $26）。
- 本地 LLM 词偏中难（local llm 2,900/KD39），但 `private gpt`（KD=18）、`best local llm`（KD=23）、`self hosted ai starter kit`（KD=9）可切入。
- 具体型号词（qwen 3.6、glm 5.2、hidream 等）适合做"在 Olares 上部署 X 模型"教程，抢新模型发布窗口；型号与候选词见各模态 deep-research 底稿 [model/research/](/Users/pengpeng/seo/directions/model/research)。

**关联**：500 词分类 2（本地 LLM 45）、分类 13（AI 图像/视频/音频 30）；模型清单 [model/models.md](/Users/pengpeng/seo/directions/model/models.md)（11 模态章，只收开源可本地跑的 2026 near-SOTA 型号），模态调研 [model/research/](/Users/pengpeng/seo/directions/model/research) 与逐型号报告 [model/reports/](/Users/pengpeng/seo/directions/model/reports)（research/reports 两级、11 章）；应用报告 [market/reports/](/Users/pengpeng/seo/directions/market/reports) 下 `comfyui.md`、`ollama.md`、`vllm.md`、`sglang.md`、`llamacpp.md`。

---

### 方向 4：加速硬件设备与整机

**市场事实**："本地 AI 硬件"是新兴热区：AI mini PC、workstation、Strix Halo、DGX Spark 等词量涨、KD 常偏低。同时传统 NAS 用户在找替代。

**已验证付费/对标**：DGX Spark、AMD Ryzen AI Max+ 395（Strix Halo）、Framework Desktop、Minisforum/Beelink mini PC；NAS：Synology、QNAP、TrueNAS、Unraid、CasaOS、Umbrel、ZimaOS。

**对应 Olares 资产**：**Olares One**（x86 + NVIDIA CUDA 本地 AI 一体机）。关键规格见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md) 的 Olares One 一节（以 https://one.olares.com/ 为准）。本方向对人群讲**两条信息**：**A 买 Olares One**（软硬一体私有云整机），**B 在已购设备上装 Olares**（把已有算力变成随处可用的私有 AI 服务）。**平台口径（已纠正）**：Olares **跨平台**——Linux x86-64（ISO/script）、ARM Linux（树莓派路径）、macOS（含 Apple Silicon，script/Docker，有限制）、Windows（WSL2）；"ARM not supported" 只限裸机 ISO。**Olares One 只是官方选了 x86-64 + NVIDIA 求最佳体验**，不代表 Mac/ARM 不能装。差异在体验层级；**GPU 加速：NVIDIA 最成熟（全 app），AMD（含 Ryzen AI Max APU，经 ROCm）/ Intel 核显均已支持，唯 Apple GPU 不被加速**（成熟度随版本，以 docs/GitHub 为准）。

成本叙事（官方）：**"Stop Renting. Save 96% on Your AI Stack."**——订阅一年约 $6,456/人 vs Olares One 约 $22.2/月/人（$3,999 / 5 人 / 3 年）。其它：可跑 Steam、可装 Windows 应用（VM+RDP）、可挂 NAS 做存储。

**洞见**：
- 硬件方向低 KD 金矿密集：`ai server build`（KD=2）、`ai server price`（KD=4）、`ai workstation build`（KD=6）、`best gpu for llm`（KD=8）、`strix halo laptop`（KD=9）、`dgx spark alternative`（KD=12）、`home ai server`（KD=14）、`linux mini pc`（KD=14）。
- NAS 替代词购买意图强且 KD 低：`synology alternative`（260/KD=7）、`synology vs qnap`（KD=14）、`mini pc linux`（KD=8）。
- 定位纪律：Olares One 是**个人云而非 PC**（常在线、随处访问的服务），别写成 AI PC/NAS。
- **结构升级：改为"具体产品为单元"（一行一产品），research/reports 按组分目录（`<NN-组>/…`，对齐 commerce/iot）**——芯片/品类深度调研（穷举承载型号 SKU + 每型号候选词 + 两条信息适配）落 [hardware/research/](/Users/pengpeng/seo/directions/hardware/research)，**8 份**（八组）：`01-ai-soc`（`amd-ryzen-ai-max` Strix Halo x86→装 High、APU 经 ROCm 被加速；`nvidia-gb10` DGX Spark + 8 OEM，arm64 走 script + Blackwell 受支持→有望 High 实测 [unverified]；`apple-m-series` Mac Studio/mini 含 M5 状态，macOS 可装有限制、Apple GPU 不被加速）、`02-5090-laptops`（`rtx-5090-mobile-laptops` 同款 5090 Mobile 游戏本）、`03-rog-nuc`（`rog-nuc` 最接近 Olares One 的 BOM）、`04-dgpu`（`dgpu-24gb-plus` ≥24GB dGPU，NVIDIA 最成熟/AMD·Intel 亦支持）、`06-ai-nas`（`ai-nas` AI NAS 含高端发烧，按内置 GPU/可内插独显/eGPU 接口 + 购买链接）、`07-enterprise-nas`（`enterprise-nas` 企业·机架·商用 NAS，认知词段）；组八个人云/NAS OS 竞品无 research、报告在 `reports/08-nas-os/`；审计与重构依据见 [gap-analysis](/Users/pengpeng/seo/directions/hardware/research/gap-analysis.md)。

**关联**：500 词分类 9（AI 硬件 40）、分类 12（NAS/存储 30）；硬件竞品清单（**具体产品为单元，一行一产品**）见 [hardware/devices.md](/Users/pengpeng/seo/directions/hardware/devices.md)；芯片/品类 deep-research 见 [hardware/research/](/Users/pengpeng/seo/directions/hardware/research)（**8 份**，按 `<NN-组>/` 分目录 + gap-analysis）；Semrush 报告见 [hardware/reports/](/Users/pengpeng/seo/directions/hardware/reports)（按 `<NN-组>/<细类>/` 分目录：GPU per-model、各 AI NAS、NAS OS、nvidia-dgx、apple-silicon 等保留直链；**19 份**已归档至 `reports/_archived/`——品牌 13 + 传统 NAS 5 + 综述 1，产品级报告走 backlog）。

---

### 方向 5：隐私

**市场事实**：隐私/去 Google/合规是长期稳定需求，且部分词商业价值极高（CPC $10+）。

**已验证付费/对标**：Proton、Tuta、SimpleLogin、Internxt、Tresorit、CryptPad、Brave、DuckDuckGo、Bitwarden、1Password。

**对应 Olares 资产**：数据不出设备的整体架构、Vault（密码）、Drive（加密存储/同步）、自托管邮件/别名、SearXNG、本地 AI（数据不上云）。

**洞见**：
- 高价值合规词是企业线索入口（与 [scenarios.md](/Users/pengpeng/seo/scenarios/scenarios.md) 场景 8 企业化需求重叠）：`gdpr compliant ai`（KD=0，CPC $11）、`private cloud security`（KD=9，CPC $10.94）。
- 中低 KD 隐私词：`privacy tools`（KD=25）、`data ownership`（KD=22）、`tailscale alternative`（KD=19）、`self hosted password manager`（KD=29）、`bitwarden alternative`（KD=19）。
- 超大流量教育词借力：`anonymous browsing`（673,000）、`private browser`（27,100）、`private email`（18,100）——用"匿名浏览/加密邮件不够，本地 AI 才是完整隐私"叙事间接截获。
- 品牌绑定："own your data"是官方 mission，天然契合隐私方向。

**关联**：500 词分类 11（隐私/GDPR 40）、分类 14 借力大词（隐私类）；隐私竞品清单与报告见 [privacy/services.md](/Users/pengpeng/seo/directions/privacy/services.md) 与 [privacy/reports/](/Users/pengpeng/seo/directions/privacy/reports)（tuta、simplelogin、cryptpad、internxt、tresorit、gdpr、duckduckgo、startpage、brave、privacy-keywords）；商业隐私 SaaS 见 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)（proton、bitwarden、1password、keepassxc、vaultwarden）。

---

### 方向 6：技术栈 / 自建单一技术

**市场事实**：很多人只想要**一个具体的底层技术**——自托管 Tailscale（Headscale）、内网穿透（FRP/ngrok/Cloudflare Tunnel）、自建 SSO、自搭 K8s、self-hosted S3/DB 等。这些词有稳定搜索量，且搜的人往往卡在"自己搭一套太麻烦"（配置、维护、踩坑）。Olares 把这些能力**内置/一键化**，正好承接"我不想折腾、要个省事的方案"。

**已验证付费/对标**：Tailscale（商业控制器）、ngrok（内网穿透 SaaS）、Cloudflare Tunnel；自建侧：Headscale、FRP，以及 K3s/JuiceFS/MinIO/Authelia 等组件。

**对应 Olares 资产**：内置 **Headscale**（免费自托管 Tailscale）、零配置内网穿透与免费 HTTPS、单点登录（Authelia/LLDAP）、开箱即用数据库/中间件、K3s 底座、统一存储（JuiceFS/MinIO）。核心叙事：**"这些技术你本来要一个个搭，Olares 装一次全给你。"**

**洞见**：
- **headscale（2,900/mo，KD=33，CPC=$6.70）是最大机会**：用户在为 Tailscale 替代付费搜索，Olares 内置 Headscale 是最直接的免费答案；`komga tailscale`（1,900/KD=4）这类"某应用 + 远程访问"的组合词几乎零竞争，一篇"在 Olares 上用 Headscale 访问 X"即可承接。
- **FRP 是中文富矿**：`frp面板`（260/KD=4）、`frp教程`（1,600/KD=17）、`内网穿透 frp`（390/KD=18）低 KD 高量；英文侧 `frp install`（KD=7）、`cloudflare tunnel alternative`（KD=13，CPC=$6.86）、`frp windows`（KD=1）都可切入。
- **技术栈组件长尾**：K3s/JuiceFS/Authelia/MinIO 等做 "self-hosted X"、"X on Olares"、"Olares uses X" 技术文——量小但精准、KD 普遍低，且喂给 GEO（AI Overview/Perplexity）效果好。
- **纪律**：这些是**长尾/技术文**，不进品牌首屏与 campaign（口径见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md) 品牌口径与写作规范）。

**关联**：技术栈词库见 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)，报告见 [tech/reports/](/Users/pengpeng/seo/directions/tech/reports)（headscale、frp）；商业方 Tailscale / Ngrok 归 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)（tailscale、ngrok）。

---

### 方向 7：IoT / 家居 / 穿戴设备

**市场事实**：家居与穿戴设备正在"AI 化 + 订阅化"——语音中枢升级到 agentic（Alexa+ $19.99/月、Gemini for Home $10/月）、摄像头 / 门铃 / 安防绑定云订阅、健康环 / 恢复带靠月费变现（Oura 估值 $11B、Whoop $10.1B）、AI 录音硬件（Plaud 软件 ARR $100M+）把真实世界对话变成云端记忆。这些设备是隐私最敏感面：常开麦克风、对外视角、24h 生物特征、全天录音，且屡有执法级事件（Ring FTC $5.8M、Eufy 上传 AWS + NY AG $450K、语音助手听录音和解）与"云关停即变砖"教训（Wemo 2026-01）。

**已验证付费/对标**：Alexa/Echo、Google Home/Nest、SmartThings、Apple Home；Ring、Nest Cam、Arlo、Wyze、Eufy、EZVIZ；ADT、SimpliSafe、Vivint；Schlage、Yale/August、Aqara、Ring/Nest 门铃；Plaud（AI 录音硬件）；Apple Watch、Garmin、Oura、Whoop、Abbott/Dexcom CGM、Sonos。（会议记录软件 Granola/Otter/Fireflies 等归 commerce，不在本方向重复。）

**对应 Olares 资产**：**HA on Olares**（家居中枢 / 语音 / 安防 / 门锁的唯一本地中枢）、**Frigate + go2rtc**（摄像头 / 门铃本地 NVR，接 Reolink/ONVIF/Aqara G410）、**Music Assistant + Snapcast + Squeezelite**（多房间音频）、**OpenClaw + Whisper + Ollama**（AI 录音 / ambient 记忆的自托管路径）、**Gadgetbridge / Nightscout / Fasten OnPrem**（可穿戴 / CGM / 健康记录去云）。核心叙事：把"常开麦克风 + 对外视角 + 贴身生物特征 + 云订阅"变成"本地中枢、无月费、数据不出设备"。

**洞见**：
- 摄像头（Frigate）与家居中枢（HA）是自托管**最成熟**的落点，直接承接 Ring/Wyze/Eufy 隐私丑闻叙事：`security camera without subscription`、`frigate nvr`、`ring alternative`、`home assistant alarm system`、`no monthly fee security system`。
- "无订阅 / 本地 / 数据不出设备"是全方向共性金句——`sonos alternative self hosted`、`smart lock without subscription`、`aqara g410`、`local voice assistant`、`self hosted meeting transcription` 竞争低且与 Olares 直接契合。
- AI 录音 / ambient 记忆是**差异化最强**方向：它正是 Personal Agent 的核心用例（OpenClaw + 本地转写摘要），而独立硬件窗口正在关闭（Limitless→Meta、Bee→Amazon、Humane 关停）。
- **诚实纪律**：门锁、智能环 / CGM / 血压、专用录音吊坠形态存在硬缺口（无 Frigate 级统一方案 / 无等价开源传感器 / Gadgetbridge 不支持 Apple Watch），写内容不做过度承诺。

**关联**：IoT 竞品清单见 [iot/iot.md](/Users/pengpeng/seo/directions/iot/iot.md)；品类 deep-research 底稿见 [iot/research/](/Users/pengpeng/seo/directions/iot/research)（系统章 smart-home-systems / health-platforms；硬件章 voice-hub / smart-speakers / cameras / home-security / locks-doorbells / ai-recorders / wearables / smart-lighting / smart-plugs / thermostats / sensors-hubs / robot-vacuums / smart-appliances / smart-tv / baby-monitors / pet-cameras / safety-trackers / connected-cars / energy-monitors / smart-glasses 共 22 份）；针对关键词的 brand-seo 结果落 [iot/reports/](/Users/pengpeng/seo/directions/iot/reports)；开源平替本体归 [market/reports/](/Users/pengpeng/seo/directions/market/reports)（home-assistant、frigate、immich 等）。
