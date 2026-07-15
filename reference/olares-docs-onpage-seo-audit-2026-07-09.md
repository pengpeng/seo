# Olares docs 页面级（on-page）SEO 审计 + 修改建议

> 审计对象：`Olares/docs`（VitePress 站点，线上路径 `https://www.olares.com/docs/`）。
> 关注面：**只看现有页面的 on-page SEO**——`<title>`/H1、meta `description`、`keywords`，以及它们与 [keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md) 三角色框架的对齐。**不含**新建页面、站点结构、内链、结构化数据（那些属另一轮）。
> 口径：本文档只给"改哪、改成什么、为什么"，不直接改 docs。搜索量为**美国月均**，技术类全球量通常为 US 的 3–5 倍。
> AS_OF：2026-07-09。

---

## 0. 一句话结论

**docs 的 SEO 底子已经很好**——基础设施层（canonical / noindex / sitemap / og:url）在 [config.mts](/Users/pengpeng/Olares/docs/.vitepress/config.mts) 已做完，`use-cases/`（~91 页真实页）几乎全有 `description`、H1 大多是"动作 + 产品名"的强意图写法。剩下的都是**收尾型增量**，四件事按 ROI 排序：

1. **P0**｜给 ~14 个高漏斗 `manual/` 页补 `description`（安装/激活/登录/FAQ/排障——这些是搜索最先命中的入口页，却恰好缺 meta 描述）。
2. **P1**｜给 ~16 个 `use-cases/` 页补 `keywords`（ollama、dify、stable-diffusion、ace-step 等热门页在缺）。
3. **P1**｜重写 4 个"裸产品名"H1（`comfyui`、`openclaw`、`stable-diffusion`、`xinference`）——它们的 `<title>` 现在就是光秃秃一个词，浪费了权重最高的 on-page 信号。
4. **P2**｜按每个 app 的**主词**（来自 `directions/*/reports/`）微调 `title`/`description`/`keywords`，把 `X alternative` / `X vs Y` / `self-hosted X` / `run X locally` 这类高意图词种进去。

> 纠偏说明：初审曾以为 `use-cases/jellyfin.md`"无 H1、无 frontmatter"——**错误**。Jellyfin 实际在 [use-cases/stream-media.md](/Users/pengpeng/Olares/docs/use-cases/stream-media.md)，H1「Build your private media server with Jellyfin」+ 完整 frontmatter，本身已优化到位。真正的问题是 **URL slug 是 `stream-media` 而非 `jellyfin`**（见 §6）。

---

## 1. 现状审计（真实计数）

### 1.1 `description`（= VitePress meta description）覆盖

| 目录 | md 总数 | 缺 description | 说明 |
|------|--------|---------------|------|
| `use-cases/` | 93 | 2 | 仅 `remote.reusables.md` / `wise.reusables.md`，均被 `srcExclude`——**真实页 91/91 全覆盖** ✅ |
| `one/` | 53 | 1 | 仅 `reusables-reset-ssh.md`（excluded）——**真实页全覆盖** ✅ |
| `manual/` | 147 | 16（~14 真实页）| **本轮 P0**：多为高漏斗入口页，见 §4 |
| `developer/` | 151 | ~60 | 多为 CLI reference / tutorial，SEO 价值低——**P3，不急** |

### 1.2 `keywords`（`head > meta[name=keywords]`）覆盖

- `use-cases/`：~74/91 有；**16 个真实页缺**：
  `ace-step`、`comfyui-launcher`、`deerflow`、`dify`、`duix-avatar`、`host-cloud-android`、`llm-base-apps`、`ollama`、`pdfmathtranslate`、`play-games-directly`、`stable-diffusion`、`stirling-pdf`、`stream-game`、`windows`、`windows-intel-gpu-passthrough`、`windows-issues`。
- 其中 `ollama`、`dify`、`stable-diffusion`、`ace-step` 是**方向 2/3 的核心引流页**，优先补。

> 注：`keywords` meta 对 Google 排名权重≈0，但 docs 站内搜索是 **Algolia**，且部分聚合/GEO 抓取会读它；成本极低、保持一致性有价值，作为 P1 而非 P0。

### 1.3 H1 / `<title>` 意图对齐

VitePress 默认 `<title>` = `H1 文本 + " | Olares"`，所以 **H1 就是 title 标签**，是页面权重最高的 on-page 信号。

- **绝大多数 use-cases H1 已是强意图写法**（"动作 + 产品名"），示例：
  `Download and run local AI models via Ollama`、`Set up Open WebUI for local AI chat`、`Stream your music library with Navidrome`、`Build your private media server with Jellyfin`。这是正确范式，保持。
- **裸产品名 H1（需重写，P1）**：
  | 文件 | 现 H1（= title 主体）| 问题 |
  |------|------|------|
  | `use-cases/comfyui.md` | `ComfyUI` | title 无意图词，等于放弃排名 |
  | `use-cases/openclaw.md` | `OpenClaw` | 同上 |
  | `use-cases/stable-diffusion.md` | `Stable Diffusion` | 同上，且 SD 是大词 |
  | `use-cases/xinference.md` | `Xinference` | 同上 |
- **泛化子页 H1（无产品/品牌词，P2）**：子页 title 变成 `Enable web search | Olares`、`Manage packages | Olares`、`Import photos from NAS | Olares`，缺品牌锚点。涉及：`openwebui-search`、`openwebui-knowledge`、`openwebui-multiuser`、`openclaw-integration`（Discord）、`openclaw-channel-whatsapp`、`openclaw-skills`、`openclaw-enable-sandbox`、`nemoclaw-google-workspace`、`opencode-packages`、`immich-import-from-nas` 等。建议在 H1 或 `titleTemplate` 里补上产品名（见 §6）。

---

## 2. 页面级 SEO 标准（docs 页的目标模板）

把三角色框架落到"一个 docs 页该怎么写头部"。**一页一个主意图**，不堆砌。

```yaml
---
# description = meta description：150–160 字符，含主词，动作导向，能独立成句
description: "Install <App> on Olares to <主价值>. <一句差异点：一键部署 / 本地运行 / 数据归你>."
head:
  - - meta
    - name: keywords
      # keywords = 次级 + GEO 变体，5–8 个，逗号分隔
      content: Olares, <App>, self-hosted <App>, <App> alternative, run <App> locally, <App> on Olares
---
# <动作> <App>（H1 = title：含产品名 + 主词意图；避免裸产品名）
```

| 头部字段 | 角色映射 | 规则 |
|---------|---------|------|
| **H1 / `<title>`** | **主词（pillar）** | "动作 + 产品名"，把 `self-hosted X` / `run X locally` / `X alternative` 的意图植入。**禁止裸产品名。** |
| **`description`** | 主词 + 1 个次级 | 150–160 字符、含主词、动作句、点出 Olares 差异（一键装/本地/数据归你） |
| **`keywords`** | **次级 + GEO** | `X self-hosted`、`X vs Y`、`X on Olares`、`private/local X`、`X alternative`（KD<15 的战略替代词优先） |

**护栏**：① 一页只主打一个意图，别把无关头部词塞一起；② 关键词自然融入正文首段，不做可见堆砌；③ 保持文档可读性优先——docs 首先是给用户看的。

---

## 3. 主词从哪来

每个 app 的主词/次级/KD 取自 `directions/market/reports/<app>.md` 的 **"Top 关键词（含角色判断）"** 表（角色 = 主词候选 / 次级 / GEO），聚合视图见 [reference/directions-keyword-roles.html](/Users/pengpeng/seo/reference/directions-keyword-roles.html)。写头部时：**H1/description 取主词候选，keywords 取次级 + GEO**。§5 已把最高价值的十余个 app 提炼好，可直接用。

---

## 4. 分优先级建议

### P0 — 给高漏斗 manual 页补 `description`
这些是"了解/安装 Olares"的搜索入口，缺 meta 描述会让 SERP 摘要随机截取正文，点击率受损。逐个补（用页面主题 + 主动作句）：

- [manual/what-is-olares.md](/Users/pengpeng/Olares/docs/manual/what-is-olares.md)、[manual/feature-overview.md](/Users/pengpeng/Olares/docs/manual/feature-overview.md)、[manual/release-notes.md](/Users/pengpeng/Olares/docs/manual/release-notes.md)
- `manual/get-started/`：`install-and-activate-olares`、`activate-olares`、`log-in-to-olares`、`manage-olares-container`、`installation-troubleshooting`、`gpu-requirements`
- `manual/help/`：`faqs`、`troubleshooting-guide`、`index`
- `manual/olares/settings/`：`single-gpu`、`multi-gpu`

> `manual/what-is-olares` / `feature-overview` 承接 `what is olares` / 品牌认知词，`description` 应含一句最新品牌口径（个人云操作系统 / 数据归你），口径以 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md) 为准。

### P1 — 补 `keywords` + 重写裸名 H1
- 给 §1.2 列出的 16 个 use-case 页补 `keywords`（模板见 §2，主词见 §5）。
- 重写 4 个裸名 H1（`comfyui`/`openclaw`/`stable-diffusion`/`xinference`）为强意图 H1（见 §5）。

### P2 — 按主词微调 title/description/keywords
- 对 §5 表中"当前头部未含高价值意图词"的页，按建议列微调。重点把 `X alternative`/`X vs Y`/`self-hosted X` 这类 KD 低、意图强的词补进 `description`/`keywords`。
- 泛化子页 H1 补产品名（§1.3、§6）。

### P3 / 暂缓 — developer 目录
`developer/install/cli/*`、`develop/advanced/*` 等约 60 页缺 `description`，但多是开发者 reference，搜索价值低、量大。**不投**，或后续用模板批量补，不占本轮。

---

## 5. 高价值 app 头部映射表（现状 → 目标）

> 主词/KD 来自 `directions/market/reports/`。"建议 keywords" = 在现有基础上**补**的高价值词。KD 为 US。

| 文件 | 当前 H1 | 目标主词（报告） | 建议 H1（title） | description 要点 | 建议补入 keywords |
|------|---------|----------------|-----------------|-----------------|------------------|
| `comfyui.md` | **ComfyUI**（裸名）| comfyui workflow 1,900/27；comfyui portable 1,300/24；**comfyui alternative 170/KD7** | `Run ComfyUI locally on Olares for AI image generation` | 一键部署 ComfyUI + 模型，本地出图、数据自留 | comfyui alternative, self-hosted comfyui, comfyui on olares, comfyui workflow |
| `stable-diffusion.md` | **Stable Diffusion**（裸名）| （并入 comfyui 生态词）run/self-host SD | `Run Stable Diffusion locally on Olares` | 本地跑 SD WebUI，无按次付费 | stable diffusion webui, self-hosted stable diffusion, run stable diffusion locally, stable diffusion on olares |
| `openclaw.md` | **OpenClaw**（裸名）| personal agent / self-hosted agent 叙事 | `Run OpenClaw as your self-hosted personal AI agent` | 本地个人 Agent，数据不出设备 | self-hosted ai agent, personal ai agent, openclaw on olares, local ai agent |
| `xinference.md` | **Xinference**（裸名）| 推理引擎自托管 | `Serve models with Xinference on Olares` | 一键起本地推理服务 | self-hosted inference, xinference on olares, local model serving |
| `ollama.md` | Download and run local AI models via Ollama ✅ | **private llm 720/27**；ollama vs lm studio 1,000/24；ollama vs llama.cpp 1,000/20 | 保持 | 已好；补主词到 description | private llm, run llama locally, ollama vs lm studio, self-hosted llm, ollama on olares |
| `openwebui.md` | Set up Open WebUI for local AI chat ✅ | open webui 8,100/34；**open webui alternative 140/KD4** | 保持 | 补 "self-hosted ChatGPT" 叙事 | open webui alternative, self-hosted chatgpt, open webui on olares |
| `dify.md` | Customize your local AI assistant using Dify ✅ | dify ollama 210/20；**dify vs n8n 140/KD13**；dify 源码部署 | 保持 | 补 "self-hosted Dify / RAG" | dify self hosted, dify vs n8n, dify ollama, dify on olares（**当前缺 keywords，整块补**）|
| `immich.md` | Manage photos with Immich | **immich vs google photos 70/KD11**；immich hardware acceleration 320/12；immich synology 210/21 | `Self-host your photos with Immich (Google Photos alternative)` | 点出 Google Photos 替代 + 数据归你 | google photos alternative, immich vs google photos, immich synology, immich on olares |
| `stream-media.md`（Jellyfin）| Build your private media server with Jellyfin ✅ | **jellyfin vs plex 4,400/32**；jellyfin plugins 1,900/18；plex alternative 1,600/33 | 保持 | 补 "Plex alternative" | jellyfin vs plex, plex alternative, jellyfin remote access（另见 §6 slug）|
| `navidrome.md` | Stream your music library with Navidrome ✅ | home music server 140/KD6；navidrome alternatives 50/KD6；install navidrome on synology 170/KD9 | 保持 | 补 "self-hosted Spotify / 家庭音乐服务器" | self-hosted spotify, home music server, navidrome on synology |
| `home-assistant.md` | Build your smart home hub with Home Assistant ✅ | home assistant raspberry pi 8,100/21；home assistant docker 1,600/36 | 保持 | 补 RPi/Docker 迁移意图 | home assistant on olares, home assistant docker, home assistant raspberry pi |
| `plane.md` | Manage projects with Plane | **jira alternatives 1,900/33**（CPC$11.89）；asana alternatives 1,600/27；open source jira alternative 140/24 | `Manage projects with Plane, an open-source Jira alternative` | 点出 Jira/Asana 开源替代 | open source jira alternative, self-hosted project management, jira alternative, plane on olares |
| `perplexica.md`（Vane）| Set up a privacy-focused AI search engine with Vane | **perplexity alternatives 170/KD10**；perplexica 1,000/28；perplexity ai alternative 90/KD8 | `Self-host a Perplexity alternative (Vane) on Olares` | 同时含 Perplexity alternative + Perplexica（旧名仍是最大流量入口）| perplexity alternative, perplexica, self-hosted perplexity, vane on olares |
| `anythingllm.md` | Build a local knowledge base with AnythingLLM ✅ | anything ai 1,000/17；anythingllm ollama 70/23 | 保持 | 补 "local RAG / private knowledge base" | self-hosted rag, anythingllm ollama, private knowledge base |
| `lobechat.md` | Build your local AI agent with LobeHub (LobeChat) ✅ | lobechat 1,900/KD15 | 保持 | 保持 | self-hosted lobechat, lobechat on olares |

> `n8n` 计划中列过，但 `use-cases/` **没有 n8n 页**（仅 `directions` 有报告）——属内容缺口，超出本轮 on-page 范围，记录备查。

---

## 6. 横切建议（非逐页）

1. **`one/` 与 `use-cases/` 主题重叠**：`comfyui`、`open-webui`(openwebui)、`ace-step`、`deerflow`、`windows` 在两个目录各有一页，讲同一 app。虽然 `one/` 面向 Olares One 硬件、`use-cases/` 面向通用安装，语义不同，但**对同一品牌词构成内部竞争**。建议：
   - 明确分工——`use-cases/*` 主打"self-host X / run X"通用意图（对外拉新），`one/*` 主打"X on Olares One"设备意图；
   - 两页 `description`/H1 用**不同意图词**（如 use-cases 用 `run comfyui`，one 用 `comfyui on olares one`），避免自我蚕食；
   - 若确有一页是另一页子集，考虑在弱页 frontmatter 加 `noindex: true`（[config.mts](/Users/pengpeng/Olares/docs/.vitepress/config.mts) 已支持该开关），把权重收敛到主页。

2. **URL slug ≠ 品牌词**：部分高价值页 slug 是泛描述而非 app 名，弱化了 URL 的关键词信号：
   `stream-media`（Jellyfin）、`stream-game`（Steam Headless）、`play-games-directly`（Steam）、`arrs`（*arr，尚可）。
   `perplexica`（Vane）**反而应保留**——报告显示旧名 `perplexica`(1,000/mo) 仍是最大单词流量入口。
   改 slug 需配 301 重定向（`_redirects.nginx` 已在用），属结构调整、优先级低于头部，但 Jellyfin 这类大词页值得单独评估。

3. **泛化子页 title 补品牌**：§1.3 列的子页 title 缺产品名。两种做法：① 直接在 H1 补（`Enable web search in Open WebUI`）；② 用分组 `titleTemplate` 注入父产品名。前者更简单可控，推荐。

4. **VitePress/实现注意（改稿时）**：
   - `description` 走 frontmatter 即生成 meta description，无需手写 `head`；
   - canonical / og:url / noindex 由 [config.mts](/Users/pengpeng/Olares/docs/.vitepress/config.mts) 的 `transformPageData` 统一注入，**逐页别再手写 canonical**；
   - 该文件注释明确警告：`transformPageData` 用 frontmatter 注入是为了**不移动源文件行号**（避免破坏 `<!--@include-->` 的行区间）。因此补 `keywords`/`description` 时，对被别处 `@include` 引用的文件要留意行号影响（`reusables` 类已 excluded，一般安全）；
   - 无需设站点级 `titleTemplate`（默认 `| Olares` 已合适）。

---

## 7. 落地顺序小结

| 步骤 | 内容 | 页数量级 | 影响面 |
|------|------|---------|--------|
| P0 | manual 高漏斗页补 `description` | ~14 | 品牌/安装入口 SERP 摘要 |
| P1 | use-cases 补 `keywords` + 重写 4 裸名 H1 | 16 + 4 | 站内搜索一致性 + 大词 title |
| P2 | 按 §5 主词微调 title/description/keywords + 子页补品牌 | ~14 + ~10 | 高意图词排名 |
| P3 | developer reference（暂缓/模板批量）| ~60 | 低 |

> 本轮**不含**：新建缺口页（n8n 等）、slug 改名 + 重定向、内链与结构化数据、GEO 直答块——这些属后续轮次。
