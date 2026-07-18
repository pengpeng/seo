# 用户愿意付费的场景 — Olares 场景选择（隐私 × TCO）

> 一页 PPT 的底稿。**下方 English 表格 + Why Olares 是上 Figma 的正文**（面向海外）；中文表降为「工作底稿」备查。
> 第 3 列＝**付费验证**（对标市场 / 真实 ARR / 估值），不是市场报告的估算 TAM；价格/回本按重度档测算。溯源见 [research/scenario-pricing-2026-07.notes/registry.md](../research/scenario-pricing-2026-07.notes/registry.md)。快照 2026-07，会变，发布前复核。

---

## Slide copy (English — PPT-facing)

### Headline

**Where users already pay for the cloud — and Olares wins locally.**
Seven scenarios that pass both bars: proven paid demand in the cloud × good-enough local models on a 24GB personal cloud.

### The seven scenarios

| Scenario | Leading paid apps | Proof of willingness-to-pay | Local on Olares | Why Olares |
|----------|-------------------|-----------------------------|-----------------|------------|
| **Personal Agent** | OpenClaw, Hermes, Claude Code, Codex | Priced against the **white-collar wage bill (~$40–50T)**, not software budgets. **Claude Code >$2.5B ARR, Codex 5M+ weekly users** | Local LLM (Qwen-27B class) + OpenClaw / Hermes, runs in 24GB, Olares CLI preinstalled | An agent that drives your whole system needs full context — and the more it knows you, the less that context should ever leave your machine. On Olares the model and data stay local, so it can act with total access while nothing leaks to a cloud vendor. |
| **App deployment** | Lovable, Manus | **Lovable ~$500M ARR** ($6.6B val), **Manus ~$2B acquisition price** | Local LLM + Agent Skills (e.g. `olares-chart`): one prompt builds, packages and deploys the app to your own Olares — no Kubernetes | Cloud app builders meter you by credit/token, so heavy iteration keeps getting pricier. On Olares you build, refine and deploy as much as you want at no extra cost; your code stays local and ships to your own domain. |
| **Audio** | Granola, Otter, Wispr Flow, ElevenLabs, Plaud | **ElevenLabs $500M ARR** ($11B val), **Otter $100M ARR, Plaud $100M** software ARR | Local transcription / translation / speech synthesis & cloning (a full open speech stack), fits in 24GB | Meeting recordings and dictation are some of the most sensitive audio you own, yet they default to the cloud. Olares keeps the entire speech pipeline on-device, so nothing reaches a third-party server — a level of privacy cloud services can't match. |
| **Image** | Midjourney, Ideogram, GPT-Image | **Midjourney ~$500M revenue, ~20M users** (largely bootstrapped) | Open image models + ComfyUI workflows; Olares One renders ~15–20s per image (video quality still weak locally) | Cloud tools bill per image, so cost spirals as volume grows. Locally the marginal cost is ~zero and your assets, face models and brand material never leave — high-volume creators pay off the hardware in a few months. |
| **Smart home** | Alexa+, Google Home, Ring, Nest | **Alexa 600M+ devices installed**; Ring / Nest / Google Home subscription base | Home Assistant hub + local camera AI / recording + local LLM for natural-language control | Cameras and locks are the most privacy-sensitive part of a home, yet they keep failing users (Ring's $5.8M FTC fine, Eufy secretly uploading to AWS, Wemo bricked when the cloud shut down). A local hub avoids all of that at the root — and won't brick when a vendor pulls the plug. |
| **AI companion** | Character.AI, Chai, Replika, Talkie | **Character.AI ~$2.5B val** (Google's $2.7B tech license + acqui-hire, not an acquisition), **Chai $80M ARR** ($2.4B val) | SillyTavern + local LLM, runs character chat in 24GB (real-time avatars are a direction, not a current feature) | Your most intimate conversations shouldn't be subject to platform censorship or sit on someone else's servers. On Olares you set the model, persona and content boundaries yourself, and the chat history never leaves home. |
| **Private workspace** | Microsoft 365, Google Workspace, Slack, Notion | **Microsoft 365 450M+ paid seats**, **Notion $600M ARR** ($11B val), **Slack ~$3B revenue** | Local IM + document collaboration + local LLM for knowledge-base Q&A / deep research | Email, docs and the knowledge base all sit on a vendor's cloud — and bolting on AI means shipping that knowledge base to a cloud model too. Olares keeps both the data and the agent inside your network, hitting data sovereignty and compliance head-on, with predictable cost when a team shares one box. |

> This slide is the table only — no gates recap, no price, no Why-Olares footer (cost/TCO and the summary pitch live on separate slides). The per-row "Why Olares" column carries the message.

---

## 工作底稿（中文，备查）

### 两道闸（上一页）

一个场景值得做，必须**同时**过两道闸：

1. **公有云上已被验证"愿意大量付费"** —— 成熟商业产品、真实 ARR、真实订阅账单。
2. **个人云硬件（24GB NVIDIA 5090 Mobile）上，本地开源模型已够用** —— 用户接受本地质量，不必回云端。

两个都满足，Olares 才有故事：**把一笔一直在涨的云订阅，换成一台买断的硬件 + 数据不出门。**

### 场景表（中文）

| 场景 | 典型应用 | 付费验证（对标市场 / ARR / 估值） | 本地方案 | Olares 优势 |
|------|----------|-----------------------------------|----------|-------------|
| **Personal Agent** | OpenClaw、Hermes、Claude Code、Codex | 对标白领劳动力盘 **~$40–50T**（AI Agent 按劳动力而非软件预算算）；付费佐证 **Claude Code ARR >$2.5B、Codex 5M+ 周活** | 本地 LLM（Qwen 27B 级）+ OpenClaw / Hermes，24GB 跑得动、预装 Olares CLI | 能操作你整台系统的 Agent 需要全部上下文，而它越懂你、这份上下文就越不该外泄；Olares 上模型和数据都在本机，它能全权行动却不向云厂商泄露一个字。 |
| **应用部署** | Lovable、Manus | **Lovable ~$500M ARR**（估值 $6.6B）、**Manus 收购价约 $2B** | 本地 LLM + Agent Skills（如 `olares-chart`）：一句话生成、打包并部署应用到自己的 Olares，不用懂 K8s | 云端应用生成平台按 credit/token 计费，反复迭代越来越贵；在 Olares 上可以不限次数地生成、修改和部署，代码留在本地并发布到自己的域名。 |
| **音频** | Granola、Otter、Wispr Flow、ElevenLabs、Plaud | **ElevenLabs $500M ARR**（估值 $11B）、**Otter $100M ARR、Plaud 软件 $100M ARR** | 本地转录 / 翻译 / 语音合成与克隆（一整套开源语音模型），24GB 可跑 | 会议录音、口述是你最敏感的语音，却默认全上了云；Olares 把整套语音处理放在本机、内容不进第三方服务器——这层私密性云服务给不了。 |
| **图片** | Midjourney、Ideogram、GPT-Image | **Midjourney 营收 ~$500M、~20M 用户**（几乎全自筹） | 开源出图模型 + ComfyUI 工作流，Olares One 出图 ~15–20 秒/张（视频本地效果一般） | 云端按张计费，量一大就失控；本地边际成本≈0、素材和脸模不外传，高频出图几个月就摊平硬件。 |
| **智能家居** | Alexa+、Google Home、Ring、Nest | **Alexa 600M+ 设备装机**；Ring / Nest / Google Home 订阅盘 | Home Assistant 做中枢 + 本地摄像头 AI / 录像 + 本地 LLM 自然语言控设备 | 摄像头、门锁是家里隐私最敏感的一面却屡屡出事（Ring 被 FTC 罚 $5.8M、Eufy 偷传 AWS、Wemo 关云即变砖）；本地中枢从根规避，还不怕厂商停服变砖。 |
| **情感陪伴** | Character.AI、Chai、Replika、Talkie | **Character.AI 估值 ~$2.5B**（Google $2.7B 技术授权 + acqui-hire，非收购）、**Chai $80M ARR**（估值 $2.4B） | SillyTavern + 本地 LLM，24GB 跑角色对话（实时数字人为方向，非现功能） | 最私密的对话既怕被平台审查、又怕存在别人服务器上；本地你自己定模型、人设和内容边界，聊天记录不出家门。 |
| **私人办公** | Microsoft 365、Google Workspace、Slack、Notion | **Microsoft 365 450M+ 付费席**、**Notion $600M ARR**（估值 $11B）、**Slack 营收 ~$3B** | 本地 IM + 文档协作 + 本地 LLM 做知识库问答 / Deep Research | 邮件、文档、知识库全押在厂商云，接 AI 还得把知识库喂给云端模型；Olares 让数据和 Agent 都留在企业内网，直击数据主权/合规，团队合用一台成本还可预测。 |

> 回本量级（重度档，仅供参考）：图片高频出图 ~2–3 月摊平硬件；其余场景不主打回本，主打长期更省 + 成本可预测，以及云端给不了的隐私/主权。测算见 registry。

### Why Olares（中文）

- **省钱**：云 AI 按月/按次/按 token 收费，越用越贵；Olares 一次买断、开源模型跑在自己显卡上，之后几乎不再多花钱——把上涨曲线拍平，不是省几块钱。
- **安心**：录音、摄像头、私密对话、公司知识库这些最不该上云的，现在恰恰都在云上（Ring、Eufy、Wemo 前车之鉴）；Olares 上模型和数据都在自己机器里，不出门、不进别人训练数据、不会因厂商倒闭或改政策而消失。
- **省心**：不用懂 Kubernetes、不用配显卡驱动，一句话交给 Agent。
- **一句话**：一台买断的、数据归你、用大白话就能指挥的私人 AI。

> Own your AI. Own your world.

---

## 待核实数据（对外发布前复核）

- **付费验证＝真实 ARR/估值/劳动力盘**（非市场报告 TAM）：ARR/估值多为公司 PR 或二手口径，逐项来源见 [registry](../research/scenario-pricing-2026-07.notes/registry.md)。
- **Personal Agent 劳动力盘 ~$40–50T**：是行业框架口径（Benioff「digital labor $3–12T」、蔡崇信「白领工资盘 ~$50T」），**非精确 TAM**，只作"对标的是劳动力而非软件"的量级参照。
- **智能家居回本弱**：Alexa+ 对 Prime 免费、家庭订阅仅 ~$10–30/mo —— 此列以隐私硬事实为主，别当省钱主力。
- **实时数字人（Unreal 渲染）**：属产品**方向/规划**，非已发布能力，涉保密红线，别写成现有功能。
- **Claude Code / Codex 归类**：本页按"操作整机的通用 Agent"归到 Personal Agent；应用部署行只列 Lovable 和 Manus。

## 来源

- 付费验证 + 价格 + 回本溯源登记：[research/scenario-pricing-2026-07.notes/registry.md](../research/scenario-pricing-2026-07.notes/registry.md)
- [Olares 定位 + Olares One 规格](../basic/olares.md) · [场景总览](../scenarios/scenarios.md) · [方向与平台能力](../directions/directions.md)
- [Olares One 第一方实测](../directions/hardware/research/olares-one-benchmarks.md) · 应用部署＝Agent Skills（如 `olares-chart`，一句话生成 + 打包 + 部署）
- 竞品报告：[Lovable](../directions/commerce/reports/03-application/vibe-coding/lovable.md) · [Manus](../directions/commerce/reports/03-application/general-agent/manus.md) · [ElevenLabs](../directions/commerce/reports/02-creation/voice-tts/elevenlabs.md) · [Midjourney](../directions/commerce/reports/02-creation/image/midjourney.md) · [Ideogram](../directions/commerce/reports/02-creation/image/ideogram.md) · [Character.AI](../directions/commerce/reports/03-application/companion/character-ai.md) · [Chai](../directions/commerce/reports/03-application/companion/chai.md) · [Microsoft 365](../directions/commerce/reports/04-productivity/office-suite/microsoft-365.md) · [Slack](../directions/commerce/reports/04-productivity/im/slack.md) · [Notion](../directions/commerce/reports/04-productivity/notes/notion.md)
- [Home Assistant](../directions/market/reports/home-assistant.md) · [智能家居系统](../directions/iot/research/01-systems/smart-home-systems.md)

数据快照：**2026-07**。价格、估值、ARR、用户数变动快，对外发布前复核。
