# Devin SEO 竞品分析报告

> 域名：cognition.ai | SEMrush US | 2026-07-07
> Devin（Cognition 出品）= 首个"自主 AI 软件工程师"Agent，能独立接任务、写代码、跑测试、开 PR；主品类词 `ai software engineer` / `autonomous coding agent` 的定义者。

---

## 项目理解（前置）

Devin 是 Cognition AI（成立于 2023 年，创始人 Scott Wu）推出的**自主 AI 软件工程师 Agent**——不同于 Copilot/Cursor 这类"补全/结对编程"的编辑器插件，Devin 主打**端到端自主完成一个工程任务**：给它一个需求，它自己规划、写代码、运行、调试、开 Pull Request。2024 年 3 月以"the first AI software engineer"病毒式出圈。2025 年 Cognition **收购了 AI 编辑器 Windsurf**（`windsurf acquisition`），把 Windsurf 的 IDE、SWE 系列自研模型（`swe-1`/`swe 1.5`）与 DeepWiki 等工具并入 Devin 产品线。当前 ARR 约 $492M、估值约 $26B（数据随融资变化，引用前以官方为准）。

Devin 的品牌资产分布在**两个域名**：`cognition.ai`（公司站 + 博客，承接融资/收购/团队/研究叙事）与 `devin.ai`（产品站 + 文档 + 付费投放落地页，承接产品词与买量）。二者需合并看待。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自主 AI 软件工程师 Agent（端到端接单写代码，非补全式插件）|
| 开源 / 许可证 | **闭源**商业 SaaS（无公开仓库；对照开源阵营是 OpenHands / OpenDevin）|
| 主仓库 | 无（闭源）|
| 核心功能 | 自主任务执行（plan→code→test→PR）｜Windsurf IDE（收购而来）｜DeepWiki 代码库理解｜SWE 系列自研模型（swe-1 / swe 1.5）｜Codemaps / SWE-grep 等工具 |
| 商业模式 / 定价 | 订阅制 + 用量（ACU/credits）；曾以 $500/月团队版闻名，后推 self-serve 低价档（`new-self-serve-plans-for-devin`）|
| 差异化 / 价值主张 | "全自主"叙事 + SWE-bench 成绩背书 + 收购 Windsurf 补齐 IDE 入口 |
| 主要竞品（初判）| Cursor（编辑器）、GitHub Copilot、Cline、**OpenHands（开源自托管平替）**、aider |
| Olares Market | Devin 本身闭源不可上架；**Olares 平替 = OpenHands（当前 Olares Market 未上架 → 上架机会）** |
| 来源 | cognition.ai、devin.ai、docs.devin.ai、GitHub All-Hands-AI/OpenHands |

---

## 流量基线（Phase 1）

Devin 用两个域名运营，需合并看。**`devin.ai` 才是流量主体**（产品站，且是唯一投付费广告的域名），`cognition.ai` 是公司/博客站。

### 概览（两域名对比）

| 指标 | cognition.ai（公司站）| devin.ai（产品站）|
|------|------|------|
| SEMrush Rank | 225,521 | **87,378** |
| 自然关键词数 | 1,126 | **2,331** |
| 月自然流量（US）| 7,702 | **22,475** |
| 自然流量估值 | $21,982/月 | **$91,774/月** |
| 付费关键词数 | 0 | **1,315** |
| 月付费流量 | 0 | **35,259**（＞自然流量）|
| 排名 1-3 位 | 159 词 | **303 词** |
| 排名 4-10 位 | 169 词 | 262 词 |
| 排名 11-20 位 | 143 词 | 238 词 |

> 合计约 3.0 万月自然流量 + 3.5 万月付费流量。相较 Lovable（自然流量估值 $579K/月）、Cursor 级玩家，Devin 的**自然 SEO 体量并不大**——它靠品牌事件（收购 Windsurf、DeepWiki 发布）与**买量**撑场，而非程序化 SEO 内容矩阵。

### 子域名流量分布（cognition.ai）

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| cognition.ai（主站/博客）| 1,107 | 7,687 | 99.81% |
| old.cognition.ai | 1 | 14 | 0.18% |
| trust.cognition.ai | 18 | 1 | 0.01% |

> devin.ai 的文档在子目录 `docs.devin.ai`（deepwiki / cli / zh 中文文档均在此），承接了相当一部分教程/功能词。

### 官网 TOP 自然关键词（合并两域名，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| multi-agent | 3 | 33,100 | 50 | $4.41 | 2,151 | 信息(借力) | cognition.ai/blog/multi-agents-working |
| windsurf ai | 1 | 12,100 | 51 | $5.28 | 1,597 | 品牌(收购) | devin.ai/desktop/ |
| deepwiki | 1 | 6,600 | 55 | $5.44 | 1,636 | 品牌(工具) | docs.devin.ai/…/deepwiki |
| windsurf | 7 | 60,500 | 47 | $3.58 | 1,331 | 品牌(收购) | devin.ai/blog/windsurf-launch |
| cognition labs | 1 | 880 | 72 | $1.34 | 704 | 品牌 | cognition.ai/ |
| deep wiki | 1/2 | 2,900 | 58 | $5.44 | 719 | 品牌(工具) | docs.devin.ai/…/deepwiki |
| davin（误拼）| 1 | 2,900 | 32 | $1.18 | 382 | 品牌(误拼) | devin.ai/ |
| windsurf ide | 1 | 2,900 | 39 | $6.12 | 382 | 品牌(收购) | devin.ai/desktop/ |
| swe-1 | 1 | 2,400 | 20 | $0.00 | 316 | 品牌(自研模型)| devin.ai/blog/windsurf-wave-9-swe-1 |
| windsurf acquisition | 1 | 1,900 | 50 | $0.00 | 250 | 信息(事件) | cognition.ai/blog/windsurf |
| devin | 1 | 12,100 | 59-81 | $5.81 | 314 | 品牌 | devin.ai/ |
| windsurf acquired | 1 | 1,300 | 56 | $0.00 | 171 | 信息(事件) | cognition.ai/blog/windsurf |
| devon ai（误拼）| 1/3 | 1,300 | 60 | $4.71 | 322 | 品牌(误拼) | devin.ai/ |
| cognitive ai | 2 | 1,600 | 48 | $7.31 | 131 | 品类混淆 | cognition.ai/ |
| autonomous ai software engineer | 1/2 | 720 | 39 | $0.00 | 178 | 品类 | devin.ai/ |
| opendevin | 2 | 720 | 31 | $8.17 | 95 | 品牌(开源平替)| devin.ai/ |
| devin是什么 | 1 | 720 | 21 | $0.00 | 95 | 品牌(中文) | docs.devin.ai/zh/…/devin-intro |
| deepwiki mcp | 1 | 720 | 17 | $0.00 | 178 | 功能 | docs.devin.ai/…/deepwiki-mcp |
| cognition ai valuation | 1 | 260 | 37 | $0.00 | 34 | 信息(财务) | cognition.ai/blog/funding… |
| codemaps | 1 | 260 | 27 | $14.96 | 64 | 品牌(工具) | cognition.ai/blog/codemaps |
| kevin-32b | 1 | 260 | 19 | $0.00 | 64 | 品牌(研究) | cognition.ai/blog/kevin-32b |
| devin ai pricing | 1 | 260 | 21 | $4.97 | 208 | 商业(定价) | devin.ai/pricing/ |
| devin pricing | 2 | 320 | 22 | $13.19 | 21 | 商业(定价) | cognition.ai/blog/new-self-serve-plans |
| devin review | 1 | 210 | 39 | $5.20 | 168 | 评测 | devin.ai/review |
| swe 1.5 | 1 | 170 | 26 | $0.00 | 22 | 品牌(自研模型)| cognition.ai/blog/swe-1-5 |
| devin cli | 1 | 140 | 34 | $7.25 | 112 | 功能 | docs.devin.ai/cli |
| devin 2.0 | 1 | 140 | 38 | $6.86 | 112 | 品牌 | devin.ai/ |

> 大量长尾为**品牌误拼变体**（davin / devon ai / devian ai / devin ia / cognation / congnition…）与 **Windsurf 收购衍生词**——即 Devin 自然流量的两大来源是"品牌好奇 + 收购事件"，而非品类内容。

### 付费词（Google Ads，devin.ai，按流量排序）

**Devin 的核心增长打法是买量**：直接竞价**竞品大词与品类大词**，导向 3 类程序化落地页——`/switch/cursor`（竞品迁移页）、`/lp/coding-agent-v2`（品类落地页）、`/desktop/`（IDE 入口页）。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| cursor | 3 | **165,000** | $1.30 | devin.ai/switch/cursor |
| cursor ai | 2 | 90,500 | $5.54 | devin.ai/switch/cursor |
| windsurf | 1 | 60,500 | $3.58 | devin.ai/desktop/ |
| cognition | 1 | 49,500 | $1.93 | devin.ai/ |
| ai agents | 2 | 27,100 | $9.28 | devin.ai/lp/coding-agent-v2 |
| devin | 1 | 12,100 | $6.00 | devin.ai/ |
| coding ai | 1 | 9,900 | $7.85 | devin.ai/lp/coding-agent-v2 |
| best ai for coding | 1 | 9,900 | $7.97 | devin.ai/lp/coding-agent-v2 |
| ai coding assistant | 1 | 9,900 | $9.37 | devin.ai/lp/coding-agent-v2 |
| ai coding | 1 | 8,100 | $7.88 | devin.ai/lp/coding-agent-v2 |
| ai code assistant | 1 | 8,100 | $9.27 | devin.ai/lp/coding-agent-v2 |
| best ai for code | 1 | 6,600 | $7.97 | devin.ai/desktop/ |
| code ai | 1 | 6,600 | $7.85 | devin.ai/lp/coding-agent-v2 |

> 关键情报：**Devin 花钱抢的是 `cursor`（16.5 万）这个竞品品牌词**，用 `/switch/cursor` 迁移页承接——典型的"截胡竞品流量"打法；再用 `/lp/coding-agent-v2` 承接所有品类大词（ai coding assistant / best ai for coding，CPC $8-9 极高）。自然 SEO 打不动这些大词，它选择直接买。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| devin | 12,100 | 81 | $5.81 | 品牌 | 品牌词，正面刚无胜算 |
| devin ai | 8,100 | 88 | $4.40 | 品牌 | 品牌词 |
| cognition ai | 5,400 | 69 | $7.31 | 品牌 | 公司名 |
| cognition devin | 480 | 64 | $4.07 | 品牌 | |
| devin vs cursor | 210 | **30** | $5.92 | 对比 | ⭐ 对比页机会 |
| devin ai review | 110 | 41 | $8.80 | 评测 | |
| devin ai alternative | 50 | **17** | $6.24 | 商业 | ⭐ 平替入口 |
| openhands vs devin | 50 | **0** | $0.00 | 对比 | ⭐ 开源平替直球 |
| devin vs copilot | 20 | **0** | $0.00 | 对比 | ⭐ |
| devin vs openhands | 20 | **0** | $0.00 | 对比 | ⭐ 开源平替直球 |
| devin alternatives | 20 | **0** | $9.74 | 商业 | ⭐ 高 CPC |
| devin ai vs github copilot | 20 | **0** | $0.00 | 对比 | ⭐ |
| devin alternative | 10 | **0** | $5.84 | 商业 | ⭐ |

### 品类词（AI software engineer / autonomous coding agent）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai software engineer | 1,300 | 41 | **$12.43** | 信息 | 品类定义词，CPC 极高 |
| coding agent | 1,000 | 50 | $6.37 | 信息 | |
| coding agents | 880 | **23** | $4.72 | 信息 | ⭐ |
| autonomous ai software engineer | 720 | 39 | $0.00 | 品类 | Devin 自造品类词 |
| ai coding agents | 720 | **30** | $6.27 | 信息 | ⭐ |
| ai coding agent | 590 | 36 | $6.27 | 信息 | |
| agentic coding assistant | 590 | 38 | $6.22 | 信息 | |
| devin ai agent | 260 | 61 | $4.54 | 品牌 | |
| ai agent for coding | 210 | 46 | $5.53 | 信息 | |
| best ai coding agent | 140 | **30** | $9.97 | 信息 | ⭐ 高 CPC |
| autonomous coding agent | 50 | **13** | $8.73 | 信息 | ⭐ 低 KD |
| best autonomous coding agent | 20 | **0** | $8.69 | 信息 | ⭐ |
| ai software engineer agent | 20 | **0** | $10.52 | 信息 | ⭐ 高 CPC |
| autonomous software engineer | 20 | **0** | $0.00 | 信息 | ⭐ |

### 产品 / 功能词（devin 前缀 + 自研工具）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deepwiki | 6,600 | 55/60 | $5.44 | 功能 | Devin 发布的独立工具，意外流量王 |
| swe-1 | 2,400 | **20** | $0.00 | 模型 | ⭐ 自研模型 |
| deep wiki | 2,900 | 58 | $5.44 | 功能 | |
| deepwiki mcp | 720 | **17** | $0.00 | 功能 | ⭐ MCP 长尾 |
| devin是什么 | 720 | **21** | $0.00 | 中文 | ⭐ 中文品类 |
| devin pricing | 320 | **22** | **$13.19** | 商业 | ⭐ 定价痛点，CPC 极高 |
| devin ai pricing | 260 | **21** | $4.97 | 商业 | ⭐ 定价痛点 |
| codemaps | 260 | **27** | $14.96 | 功能 | ⭐ 最高 CPC |
| kevin-32b | 260 | **19** | $0.00 | 研究 | ⭐ 论文/模型词 |
| devin review | 210 | 39 | $5.20 | 评测 | |
| swe 1.5 | 170 | **26** | $0.00 | 模型 | ⭐ |
| devin 2.0 | 140 | 38 | $6.86 | 品牌 | |
| devin cli | 70-140 | **34** | $7.25-10.33 | 功能 | ⭐ |
| devin api | 90 | 36 | $4.96 | 功能 | |
| swe grep | 70 | **21** | $0.00 | 功能 | ⭐ |
| devin acu | 30 | **20** | $3.74 | 定价 | ⭐ 用量单位痛点 |
| devin ai cost | 30 | **0** | $7.03 | 商业 | ⭐ |
| devin free | 20 | **0** | $0.00 | 商业 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| openhands | 4,400 | 53 | $4.73 | 品牌 | **头号开源平替**（All-Hands-AI）|
| aider | 6,600 | 51 | $5.66 | 品牌 | 开源 CLI 编码 Agent |
| cline | 18,100 | 78 | $5.76 | 品牌 | 开源 VS Code Agent（量最大）|
| cline ai | 3,600 | 83 | $4.93 | 品牌 | |
| goose ai | 2,400 | **40** | $8.39 | 品牌 | Block 开源 Agent |
| open claude | 2,400 | 49 | $4.53 | 品牌 | |
| aider ai | 1,000 | **37** | $6.19 | 品牌 | ⭐ |
| opendevin | 720 | 31 | $8.17 | 品牌 | OpenHands 前身，高 CPC |
| swe agent | 720 | 41 | $6.83 | 品牌 | 开源（Princeton）|
| sweagent | 480 | **37** | $0.00 | 品牌 | ⭐ |
| all hands ai | 320 | 52 | $0.00 | 品牌 | OpenHands 公司名 |
| open source ai agent | 260 | 42 | $4.32 | 信息 | |
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐ 语义完美契合 |
| openhands ai | 170 | 43 | $6.12 | 品牌 | |
| best open source coding agent | 50 | **0** | $6.47 | 信息 | ⭐ |
| local coding agent | 50 | **0** | $6.02 | 信息 | ⭐ |
| self hosted coding agent | 30 | 39 | $4.25 | 信息 | |
| devin open source / open source devin | 20 | **0** | $0.00 | 信息 | ⭐ 用户直搜"开源版 Devin" |
| openhands docker / openhands install | 20 | **0** | $0.00 | 教程 | ⭐ 部署意图 |
| open source ai coding | 20 | **0** | $5.48 | 信息 | ⭐ |
| self hosted ai coding assistant | 10 | **0** | $4.18 | 信息 | ⭐ |
| self hosted ai agent | 10 | **0** | $4.59 | 信息 | ⭐ |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Devin 闭源 + 按 ACU/credits 计费 + $500/月起、任务与代码全在 Cognition 云端跑；Olares 的对应叙事 = 在自己的 Olares 上自托管 OpenHands（开源自主编码 Agent），接本地 LLM——无席位费、无 credits 限额、代码与仓库不出机、数据主权归你。** OpenHands 当前**未在 Olares Market 上架 → 直接上架机会**。契合度 ⭐⭐⭐ / ⭐⭐ / ⭐。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| openhands | 4,400 | 53 | $4.73 | ⭐⭐⭐ 上架 OpenHands 到 Olares Market +「自托管 OpenHands」教程，承接开源平替流量主体 |
| aider | 6,600 | 51 | $5.66 | ⭐⭐ 轻量 CLI Agent，配本地 LLM 在 Olares 上跑，零 API 成本 |
| opendevin | 720 | 31 | $8.17 | ⭐⭐⭐ OpenHands 前身词，KD31 CPC$8，直接导向「在 Olares 上跑 OpenHands（原 OpenDevin）」|
| devin是什么 | 720 | **21** | $0.00 | ⭐⭐ 中文认知词，科普后引出"开源自托管平替 OpenHands on Olares" |
| open source coding agent | 210 | **20** | $5.51 | ⭐⭐⭐ 语义完美，KD20，best open-source coding agent 清单页（Olares 部署）|
| devin ai alternative | 50 | **17** | $6.24 | ⭐⭐⭐ 平替直球词，KD17 |
| openhands vs devin | 50 | **0** | $0.00 | ⭐⭐⭐ 对比页黄金位：闭源 SaaS vs 自托管开源，Olares 一键部署 OpenHands |
| devin vs openhands | 20 | **0** | $0.00 | ⭐⭐⭐ 同上，反向变体 |
| devin alternatives | 20 | **0** | $9.74 | ⭐⭐ KD0 + CPC$9.74，替代清单页 |
| best open source coding agent | 50 | **0** | $6.47 | ⭐⭐⭐ KD0 清单页，OpenHands/aider/swe-agent on Olares |
| local coding agent | 50 | **0** | $6.02 | ⭐⭐⭐ "本地编码 Agent" = Olares 核心叙事，KD0 |
| autonomous coding agent | 50 | **13** | $8.73 | ⭐⭐ 品类词 KD13，导向自托管自主 Agent |
| open source devin / devin open source | 20 | **0** | $0.00 | ⭐⭐⭐ 用户直搜"开源版 Devin"，KD0 占位 |
| openhands docker / openhands install | 20 | **0** | $0.00 | ⭐⭐⭐ 部署意图词，「在 Olares 上一键部署 OpenHands」教程 |
| self hosted coding agent | 30 | 39 | $4.25 | ⭐⭐ 自托管信号 |
| self hosted ai coding assistant | 10 | **0** | $4.18 | ⭐⭐ KD0 语义精准，GEO 占位 |
| self hosted ai agent | 10 | **0** | $4.59 | ⭐⭐ KD0，Olares Agent 叙事 |

### 新兴 / GEO 方向（量≤20 或 KD=0）

`open source ai software engineer`、`run openhands locally`、`self hosted devin`、`open source autonomous agent`、`open source ai coding` —— 目前近零量，但与 Olares"拥有你的 AI + 数据不出机 + 跑 Personal Agent"叙事高度契合，适合提前发布权威内容，抢 AI Overview / Perplexity 的引用位。

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| openhands | 4,400 | 53 | $4.73 | 品牌 | 主词候选 | 开源平替流量主体，上架 Olares Market +「自托管 OpenHands」教程一篇 |
| aider | 6,600 | 51 | $5.66 | 品牌 | 主词候选 | 轻量 CLI Agent + 本地 LLM on Olares，零 API 成本，独立教程 |
| ai software engineer | 1,300 | 41 | $12.43 | 信息 | 主词候选 | 品类定义词 CPC$12，"自托管的 AI 软件工程师"角度切入 |
| opendevin | 720 | 31 | $8.17 | 品牌 | 主词候选 | OpenHands 前身，KD31/CPC$8，导向 OpenHands on Olares |
| open source coding agent | 210 | 20 | $5.51 | 信息 | 主词候选 | best open-source coding agent 清单页（Olares 部署），语义完美 |
| coding agents | 880 | 23 | $4.72 | 信息 | 次级 | 低 KD 品类词，并入清单/科普文 |
| ai coding agents | 720 | 30 | $6.27 | 信息 | 次级 | 同上，复数变体借力 |
| autonomous ai software engineer | 720 | 39 | $0.00 | 品类 | 次级 | Devin 自造品类词，导向开源自主 Agent |
| devin是什么 | 720 | 21 | $0.00 | 中文 | 主词候选 | 中文认知词，KD21，科普 + OpenHands 平替引流 |
| devin pricing | 320 | 22 | $13.19 | 商业 | 主词候选 | 定价痛点，CPC$13.19，"Devin $500/月 vs OpenHands 自托管零席位费" |
| devin ai pricing | 260 | 21 | $4.97 | 商业 | 次级 | 与 devin pricing 同簇 |
| devin vs cursor | 210 | 30 | $5.92 | 对比 | 次级 | 对比页，可扩成三方对比（含开源自托管）|
| best ai coding agent | 140 | 30 | $9.97 | 信息 | 主词候选 | 清单页 CPC$9.97，best open-source self-hosted coding agent |
| devin ai alternative | 50 | 17 | $6.24 | 商业 | 主词候选 | 平替直球词，KD17，Olares 平替落地页 |
| autonomous coding agent | 50 | 13 | $8.73 | 信息 | 次级 | 品类词 KD13，并入清单 |
| openhands vs devin | 50 | 0 | $0.00 | 对比 | 主词候选 | 对比页黄金位：闭源 SaaS vs 自托管开源，Olares 一键部署 |
| local coding agent | 50 | 0 | $6.02 | 信息 | 次级 | "本地编码 Agent"= Olares 核心叙事，KD0 |
| best open source coding agent | 50 | 0 | $6.47 | 信息 | 次级 | KD0 清单页，OpenHands/aider/swe-agent on Olares |
| open source devin | 20 | 0 | $0.00 | 信息 | GEO | 用户直搜"开源版 Devin"，KD0 提前占位 |
| self hosted ai agent | 10 | 0 | $4.59 | 信息 | GEO | 近零量语义完美契合 Olares，GEO 抢引用位 |

---

## 核心洞见

1. **品牌护城河：Devin 的自然流量护城河比想象中浅，正面刚品牌词没意义但品类叙事仍有空间。** 合计约 3 万月自然流量，主要来自**品牌好奇（devin/大量误拼 davin/devon）+ 收购 Windsurf 事件词 + DeepWiki 独立工具**三块，并非靠品类内容矩阵。品牌词 `devin`（KD81）/`devin ai`（KD88）打不动也不必打；真正能抢的是它**没有系统占据的品类词与替代词**。

2. **可复制的打法有两条，且都被验证有效：**（a）**"截胡竞品 + 品类大词"买量 → 程序化落地页**：Devin 花钱竞价 `cursor`（16.5 万）、`ai coding assistant`（CPC$9.37）等，导向 `/switch/cursor` 迁移页与 `/lp/coding-agent-v2` 品类页。Olares 可低成本复制 `/switch/<竞品>` 与 `X alternative` 落地页矩阵（自然 SEO 侧，不必买量）。（b）**发布独立工具带流量**：`deepwiki`（6,600）、`swe-1`（2,400，KD20）证明"发布一个有价值的独立工具/模型"能带来意外的自然流量——这点旧报告已指出，予以保留。

3. **对 Olares 最关键的 3 个词：`openhands`（4,400, KD53）、`opendevin`（720, KD31）、`devin ai alternative`（50, KD17）。** 用户在主动搜索**开源、自托管的 Devin 替代品**，而 OpenHands（前身 OpenDevin）正是这条需求的落点。**OpenHands 目前未在 Olares Market 上架**——上架它 + 配「自托管 OpenHands / OpenHands on Olares」教程，即可同时吃下"品牌词 + 前身词 + 替代词 + 部署词"四层流量。这是本报告最高优先级动作。

4. **最大攻击面 = 定价与"云端跑"两点。** `devin pricing`（320, **KD22, CPC$13.19**）、`devin ai pricing`（260, KD21）、`devin acu`（30，用量单位 ACU 痛点）、`devin ai cost`/`devin free`（KD0）密集出现，说明用户对 Devin 的 **$500/月 + ACU/credits 计费高度敏感**。Olares 叙事直击："自托管 OpenHands + 本地 LLM = 无席位费、无 credits 限额、代码与私有仓库不出机"。定价词是低 KD 高 CPC 的黄金战场。

5. **隐藏低 KD 金矿：`open source coding agent`（210, KD20）、`autonomous coding agent`（50, KD13）、`openhands vs devin`/`devin vs openhands`（各 50/20, KD0）、`best open source coding agent`（50, KD0）、`local coding agent`（50, KD0）。** 量虽小但语义与 Olares 完美契合、竞争几乎为零，配合 OpenHands 上架可近乎零成本抢占。中文侧 `devin是什么`（720, KD21）是被忽视的高性价比认知词。

6. **GEO 前瞻布局：** `open source ai software engineer`、`self hosted ai agent`（KD0）、`run openhands locally`、`self hosted devin`、`open source autonomous agent` 目前近零量，但精准对应 Olares"拥有你的 AI + 数据不出机 + 跑 Personal Agent"叙事。建议提前发布权威长文占位，抢生成式引擎（AI Overview / Perplexity）引用。

7. **与既有分析的关联：** 本报告与 `olares-500-keywords` 的「AI 编码」分类（cursor alternative、github copilot alternative、tabnine self-hosted）互补——但 500 词表偏"编辑器/补全"侧，缺**"自主编码 Agent（autonomous coding agent / AI software engineer）"这一新兴子品类**。建议将 OpenHands / aider / swe-agent 作为"开源自托管自主编码 Agent"独立簇补入 500 词表，与同目录 [windsurf](/Users/pengpeng/seo/directions/commerce/reports/03-application/ide/windsurf.md)（编辑器侧，现归 Cognition）交叉引用。

> Windsurf（现属 Cognition）的编辑器侧分析见 [windsurf](/Users/pengpeng/seo/directions/commerce/reports/03-application/ide/windsurf.md)。

---

*数据来源：SEMrush US 数据库（domain_rank / domain_organic_subdomains / resource_organic / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-07*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
