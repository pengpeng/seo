# Cline SEO 竞品分析报告

> 域名：cline.bot | SEMrush US | 2026-07-06
> Cline = 开源 AI 编码 Agent（Apache 2.0）——VSCode 插件 + CLI + SDK 三形态，BYOK 无锁定，融资 $32M / 估值 $110M

---

## 项目理解（前置）

Cline 是 2024 年 7 月诞生于 Anthropic 黑客松的开源 AI 编码 Agent，现已成长为最受欢迎的 VSCode 编码代理之一（GitHub ★63K+，8M+ 用户）。它以"自带 API Key，代码不出基础设施"为核心差异，对抗 Cursor 的封闭订阅 + Copilot 的大厂锁定。2025 年 7 月完成 $27M Series A，总融资 $32M，估值 $110M。2026 年 5 月推出 Cline SDK（@cline/sdk），将 Agent 运行时从 VSCode 扩展中解耦，开源 CLI 与 Kanban 已迁移，VSCode/JetBrains 扩展正在迁移。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 AI 编码 Agent：IDE 扩展 + CLI + SDK，BYOK，无供应商锁定 |
| 开源 / 许可证 | Apache 2.0（VSCode 扩展 + SDK + CLI；JetBrains 闭源，待迁移） |
| 主仓库 | [github.com/cline/cline](https://github.com/cline/cline)（★ 63,878） |
| 核心功能 | 自主计划-执行 Agent 循环；文件创建/编辑；终端命令执行；浏览器交互；MCP 工具扩展；Memory Bank（跨会话记忆）；子代理（Subagents）；.clinerules 自定义规则 |
| 商业模式 / 定价 | 个人免费（BYOK，只付 API 费）；Teams $20/用户/月（前 10 席免费）；Enterprise 定制（SSO、审计日志、VPC 部署） |
| 差异化 / 价值主张 | 完全透明的 API 成本（无隐藏定价）；任意模型（Claude / GPT / Gemini / Ollama / LM Studio）；代码留本地；开源 SDK 可自建扩展；Human-in-the-loop 精细审批 |
| 主要竞品（初判）| Cursor（闭源 IDE 订阅，$20/月）、GitHub Copilot（大厂集成）、Windsurf（Codeium，闭源 IDE）、Roo Code（VSCode 扩展）、Kilo Code（VSCode）、Continue.dev（开源）、Aider（CLI） |
| Olares Market | 未上架（可通过 Ollama 接入本地模型自用） |
| 来源 | [cline.bot](https://cline.bot)、[GitHub](https://github.com/cline/cline)、[Sacra](https://sacra.com/c/cline/)、[Forbes](https://www.forbes.com/sites/rashishrivastava/2025/07/31/cline-has-raised-27-million-to-help-developers-control-their-ai-spend/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | cline.bot |
| SEMrush Rank | **81,889**（较年轻域名，处于高速增长期） |
| 自然关键词数 | 2,332 |
| 月自然流量（US）| 24,120 |
| 自然流量估值 | **$122,704/月** |
| 付费关键词数 | 3（几乎不投广告） |
| 月付费流量 | 42 |
| 排名 1-3 位 | 163 词 |
| 排名 4-10 位 | 276 词 |
| 排名 11-20 位 | 292 词 |

> 注：cline.bot 域名 2024 年才建立，处于 SEO 快速成长阶段。流量集中于品牌词（主词 `cline` 单词贡献 14,480 流量，占总流量 60%+），非品牌词潜力尚未充分开发。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| cline.bot（主站）| 1,511 | 21,237 | 88.05% |
| docs.cline.bot | 812 | 2,778 | 11.52% |
| app.cline.bot | 8 | 105 | 0.44% |
| trust.cline.bot | 1 | 0 | 0% |

> docs.cline.bot 贡献 11.5% 流量——Memory Bank、MCP、Rules 等功能文档词是主力。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| cline | 1 | 18,100 | 70 | $5.41 | 14,480 | 品牌 | / |
| cline memory bank | 1 | 1,000 | 35 | $0 | 800 | 功能 | /docs/features/memory-bank |
| kline code | 1 | 720 | 79 | $2.70 | 576 | 品牌混淆 | / |
| cline cli | 1 | 720 | 62 | $6.10 | 576 | 产品 | /cli |
| cline coding | 1 | 390 | 71 | $7.07 | 312 | 品牌 | / |
| cline for students | 1 | 390 | 21 | $0 | 312 | 商业 | / |
| cline bot | 1 | 320 | 56 | $6.21 | 256 | 品牌 | / |
| cline rules | 1 | 320 | 24 | $10.24 | 256 | 功能 | /docs/customization/cline-rules |
| cline mcp | 1 | 260 | 41 | $8.40 | 208 | 功能/集成 | /docs/mcp/mcp-overview |
| cline pricing | 1 | 260 | 46 | $7.52 | 208 | 商业 | /pricing |
| cli | 9 | 33,100 | 68 | $13.32 | 165 | 信息 | /cli |
| memory bank | 1 | 1,000 | 31 | $0.23 | 132 | 功能 | /docs/best-practices/memory-bank |
| cline vs cursor | 2 | 1,300 | 23 | $1.34 | 106 | 对比 | /blog/best-ai-coding-assistant-2025… |
| cline logo | 1 | 170 | 33 | $1.56 | 136 | 品牌 | /brand |
| cline ai | 1 | 2,900 | 52 | $4.61 | 75 | 品牌 | / |
| cline kanban | 1 | 140 | 24 | $7.38 | 112 | 产品 | /cli |
| cline mcp servers | 1 | 140 | 37 | $8.87 | 112 | 集成 | /docs/mcp/mcp-overview |
| cline subagents | 1 | 140 | 30 | $5.12 | 112 | 功能 | /docs/features/subagents |
| cline coding agent | 1 | 140 | 39 | $6.19 | 112 | 品牌/品类 | / |
| .clinerules | 1 | 320 | 23 | $0 | 79 | 功能 | /docs/customization/cline-rules |
| cline login | 1 | 110 | 46 | $0.80 | 88 | 导航 | app.cline.bot |
| cline company | 1 | 110 | 32 | $0 | 88 | 品牌 | / |
| cline docs | 1 | 110 | 47 | $4.67 | 88 | 导航 | docs.cline.bot |
| cline extension | 1 | 90 | 34 | $7.36 | 72 | 产品 | / |
| lm studio cline | 1 | 50 | 29 | $0 | 40 | 集成 | /docs/running-models-locally/lm-studio |
| cline workspace | 1 | 50 | 37 | $0 | 40 | 功能 | /docs/features/multiroot-workspace |

> `cli` (33,100 vol) 排名第 9 显示 Cline CLI 页面在通用词里意外曝光，但 KD 68 排不上去；`kline code` 是品牌名混淆流量。

### 付费词（Google Ads，按流量排序）

Cline **几乎不投 Google Ads**（仅 3 词，42 月度付费流量），全押品牌 SEO 与开发者口碑增长，与 Cursor/Lovable 的大规模投放策略截然不同。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| kline code | 1 | 720 | $2.70 | /security-aviation-aerospace |
| kline code | 4 | 720 | $2.70 | /security-aviation-aerospace |
| clinebot | 1 | 90 | $2.25 | /security-aviation-aerospace |

> 三词均指向 `/security-aviation-aerospace` 安全行业页，显示 Cline 正在拓展企业/航天安全场景，而非常规 SEM 投放。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| cline vs cursor | 1,300 | 23 | $1.34 | 对比 | ⭐ Cline 自己在排名 #2 |
| cursor alternatives | 1,300 | 23 | $7.34 | 商业 | ⭐ 可覆盖"Cline 作为 Cursor 平替" |
| cursor alternative | 880 | 25 | $7.34 | 商业 | ⭐ |
| roo cline | 880 | 35 | $3.40 | 导航/信息 | 竞品混合搜索 |
| cursor vs cline | 590 | 22 | $0 | 对比 | ⭐ |
| roo code vs cline | 480 | 21 | $6.78 | 对比 | ⭐ |
| cursor ai alternative | 480 | 18 | $4.59 | 商业 | ⭐ |
| cline vs roo code | 260 | 19 | $0 | 对比 | ⭐ |
| open source cursor alternative | 210 | 28 | $2.56 | 商业 | ⭐ |
| cursor app free replacement | 210 | 20 | $0 | 商业 | ⭐ |
| cline vs copilot | 210 | 28 | $3.83 | 对比 | ⭐ |
| github copilot alternative | 210 | 13 | $6.46 | 商业 | ⭐ KD=13！高 CPC |
| aider vs cline | 140 | 23 | $4.34 | 对比 | ⭐ |
| cline vs continue | 140 | 10 | $3.57 | 对比 | ⭐ KD=10 |
| roo vs cline | 170 | 14 | $12.44 | 对比 | ⭐ 超高 CPC |
| free cursor alternative | 170 | 25 | $2.63 | 商业 | ⭐ |
| kilo code vs cline | 110 | 16 | $5.38 | 对比 | ⭐ |
| alternative to cursor | 110 | 20 | $7.46 | 商业 | ⭐ |
| cline alternatives | 90 | 8 | $5.55 | 商业 | ⭐ KD=8！ |
| cline vs windsurf | 90 | 21 | $0 | 对比 | ⭐ |
| cline vs github copilot | 90 | 10 | $2.41 | 对比 | ⭐ KD=10 |
| cline vs aider | 70 | 25 | $12.16 | 对比 | ⭐ |
| cline alternative | 50 | 14 | $5.87 | 商业 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai coding assistant | 9,900 | 65 | $9.27 | 信息 | 大品类，KD 太高 |
| ai code assistant | 8,100 | 56 | $9.27 | 信息 | |
| coding agent | 1,000 | 50 | $6.37 | 信息 | 中等 KD |
| ai coding tool | 1,000 | 50 | $9.15 | 信息 | |
| agentic ai coding assistant | 1,900 | 46 | $8.71 | 信息 | 新兴品类词 |
| ai coding agent | 590 | 36 | $6.27 | 信息 | |
| ai code agent | 720 | 55 | $9.76 | 信息 | |
| best coding agent | 260 | 28 | $7.85 | 商业 | ⭐ |
| open source coding agent | 210 | 20 | $5.51 | 信息 | ⭐ 核心 Olares 品类词 |
| best ai coding tool | 210 | 32 | $5.89 | 商业 | |
| best ai coding agent | 140 | 30 | $9.97 | 商业 | |
| open source ai coding agent | 210 | 39 | $4.23 | 信息 | |
| ai pair programmer | 110 | 47 | $3.65 | 信息 | |

### 产品 / 功能词（cline 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| cline memory bank | 1,000 | 35 | $0 | 功能 | 文档锚词，Cline 独有特性 |
| cline cli | 720 | 62 | $6.10 | 产品 | CLI 独立产品词 |
| cline for students | 390 | 21 | $0 | 商业 | ⭐ 学生定价词 |
| cline rules | 320 | 24 | $10.24 | 功能 | ⭐ 高 CPC，规则定制 |
| .clinerules | 320 | 23 | $0 | 功能 | ⭐ 功能词 |
| cline mcp | 260 | 41 | $8.40 | 集成 | MCP 集成词 |
| cline pricing | 260 | 46 | $7.52 | 商业 | 定价词 |
| cline intellij | 260 | 33 | $2.32 | 产品 | JetBrains 扩展词 |
| cline ai | 2,900 | 52 | $4.61 | 品牌 | 品牌变体 |
| cline kanban | 140 | 24 | $7.38 | 产品 | ⭐ 看板功能词 |
| cline subagents | 140 | 30 | $5.12 | 功能 | 子代理功能 |
| cline mcp servers | 140 | 37 | $8.87 | 集成 | MCP 服务器集成 |
| cline coding agent | 140 | 39 | $6.19 | 品类 | 品牌+品类合体词 |
| cline ollama | 90 | 23 | $0 | 集成 | ⭐ Olares 核心词！ |
| cline extension | 90 | 34 | $7.36 | 产品 | VSCode 扩展词 |
| cline vs code | 210 | 50 | $2.33 | 产品 | |
| memory bank | 1,000 | 31 | $0.23 | 功能 | ⭐ 通用词 Cline 排 #1 |
| lm studio cline | 50 | 29 | $0 | 集成 | ⭐ 本地模型集成词 |
| cline local model | 30 | 0 | $0 | 集成 | ⭐ 新兴，完美 Olares 词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| cline open source | 170 | 50 | $2.60 | 信息 | 用户在确认 Cline 是否开源 |
| open source coding agent | 210 | 20 | $5.51 | 信息 | ⭐ 最佳入口词 |
| open source cursor alternative | 210 | 28 | $2.56 | 商业 | ⭐ 直接指向 Cline |
| cline ollama | 90 | 23 | $0 | 集成 | ⭐ 本地模型用 Cline |
| local coding agent | 50 | 0 | $6.02 | 信息 | ⭐ KD=0 空白地带 |
| self hosted coding agent | 30 | 39 | $4.25 | 信息 | |
| local llm coding agent | 30 | 0 | $0 | 信息 | ⭐ GEO 词 |
| cline local model | 30 | 0 | $0 | 集成 | ⭐ GEO 词 |
| ai coding agent open source | 30 | 0 | $5.20 | 信息 | ⭐ GEO 词 |
| ollama coding agent | 20 | 0 | $6.56 | 信息 | ⭐ GEO 词 |
| github copilot self hosted | 20 | 0 | $0 | 信息 | 开源替代信号 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Cline 本身开源 Apache 2.0，其 BYOK 架构天然契合 Olares 的"代码 + 模型不出自己基础设施"理念——Olares 上跑 Ollama，Cline 配置本地端点，零 API 费用、完全隐私、不受 API 涨价影响。同时 Olares 可上架同品类开源替代：OpenHands、Continue.dev、Aider，覆盖"cline alternative"/"open source coding agent"词族。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| cline vs cursor | 1,300 | 23 | $1.34 | ⭐⭐⭐ Cline（开源 BYOK + Olares 本地模型）vs Cursor（$20/月订阅），Olares 把 Cline 的低成本优势最大化 |
| cursor alternative | 880 | 25 | $7.34 | ⭐⭐⭐ Cline on Olares = 最佳 Cursor 开源平替，本地模型零 API 成本 |
| cursor alternatives | 1,300 | 23 | $7.34 | ⭐⭐⭐ 清单文章机会，Cline/Roo Code/Continue.dev on Olares |
| roo code vs cline | 480 | 21 | $6.78 | ⭐⭐ Roo Code 同为开源 VSCode 扩展，均可接 Olares Ollama |
| cursor ai alternative | 480 | 18 | $4.59 | ⭐⭐ 开源替代词，导向 Cline + Olares 方案 |
| open source coding agent | 210 | 20 | $5.51 | ⭐⭐⭐ 核心入口词，Olares Market 可上架 Cline SDK + OpenHands |
| github copilot alternative | 210 | 13 | $6.46 | ⭐⭐⭐ KD=13，高 CPC，Cline（开源 + 本地模型）是 Copilot 最佳平替 |
| open source cursor alternative | 210 | 28 | $2.56 | ⭐⭐ 直指 Cline，结合 Olares 本地部署 |
| cline vs continue | 140 | 10 | $3.57 | ⭐⭐ KD=10，Continue.dev 也可上架 Olares Market |
| roo vs cline | 170 | 14 | $12.44 | ⭐⭐ $12.44 超高 CPC，Roo Code 同样开源可接本地模型 |
| cline ollama | 90 | 23 | $0 | ⭐⭐⭐ 直接对应 Olares + Ollama 方案，"cline with ollama on Olares" 教程 |
| cline alternatives | 90 | 8 | $5.55 | ⭐⭐⭐ KD=8 极低，Olares 上的开源编码代理清单 |
| cline alternative | 50 | 14 | $5.87 | ⭐⭐ KD=14，开源替代文章 |
| local coding agent | 50 | 0 | $6.02 | ⭐⭐⭐ KD=0 完全空白，Olares + Ollama + Cline 场景精确命中 |
| cline local model | 30 | 0 | $0 | ⭐⭐⭐ GEO 占位词，"how to use cline with local model on Olares" |
| local llm coding agent | 30 | 0 | $0 | ⭐⭐ GEO 词，完美 Olares + Ollama 场景 |
| ollama coding agent | 20 | 0 | $6.56 | ⭐⭐⭐ KD=0，GEO 抢位，Olares 是最完整的 Ollama 本地运行方案 |
| ai coding agent open source | 30 | 0 | $0 | ⭐⭐ GEO 词 |
| openhands | 4,400 | 53 | $4.73 | ⭐ OpenHands = Cline 同类最大开源替代，待上架 Olares Market |
| roo code | 12,100 | 43 | $7.79 | ⭐ Roo Code 品牌词，同类开源可与 Cline 互相导流 |
| aider ai | 1,000 | 37 | $6.19 | ⭐ Aider = 纯 CLI 开源编码代理，Olares 终端方向 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| cline vs cursor | 1,300 | 23 | $1.34 | 对比 | **主词候选** | KD 23 低，Cline 自身排 #2；Olares + Cline + Ollama vs Cursor $20/月是最强叙事切入点 |
| cursor alternatives | 1,300 | 23 | $7.34 | 商业 | **主词候选** | 与 `cursor alternative`（880）合计 2,180，KD23/25，Cline 是最佳开源 Cursor 平替，可做"N best cursor alternatives"清单页 |
| cursor alternative | 880 | 25 | $7.34 | 商业 | 次级 | 与 cursor alternatives 并入同一文章簇，KD 25 可打 |
| roo code vs cline | 480 | 21 | $6.78 | 对比 | **主词候选** | 与 `cline vs roo code`（260）合计 740，KD 19-21，两者都开源可接 Ollama；可做 Olares 上同类比较 |
| cursor ai alternative | 480 | 18 | $4.59 | 商业 | 次级 | 并入 cursor alternative 簇 |
| open source coding agent | 210 | 20 | $5.51 | 信息 | **主词候选** | KD 20，Olares Market 开源编码代理清单（Cline / OpenHands / Roo Code / Aider）的核心入口词 |
| github copilot alternative | 210 | 13 | $6.46 | 商业 | **主词候选** | KD=13 极低 + CPC $6.46，Cline 是 Copilot 最佳开源平替；与 `cline vs github copilot`（90, KD10）合并 |
| cline memory bank | 1,000 | 35 | $0 | 功能 | 次级 | Cline 独有特性词，已排 #1；`memory bank`（1,000 vol, KD31）额外曝光机会，可在文档/博客深化 |
| cline rules | 320 | 24 | $10.24 | 功能 | 次级 | ⭐ KD 24，CPC $10.24 最高；Cline 自定义规则功能，`.clinerules`（320, KD23）同族 |
| cline mcp | 260 | 41 | $8.40 | 集成 | 次级 | MCP 集成词，KD 偏高，但 CPC 高、商业意图强；`cline mcp servers`（140）同族 |
| coding agent | 1,000 | 50 | $6.37 | 信息 | 次级 | KD 50 偏高，作为品类大词带在文章中，不独立打 |
| roo vs cline | 170 | 14 | $12.44 | 对比 | **主词候选** | KD=14 + CPC $12.44（报告最高），roo cline（880, KD35）显示混合搜索热度高 |
| cline vs continue | 140 | 10 | $3.57 | 对比 | 次级 | KD=10 超低，并入"cline alternative"对比文章 |
| cline ollama | 90 | 23 | $0 | 集成 | **主词候选** | KD 23，直接命中 Olares 场景；`lm studio cline`（50, KD29）+ `cline local model`（30, KD0）同族，合计 170+，适合"Cline + Ollama on Olares"教程文 |
| cline alternatives | 90 | 8 | $5.55 | 商业 | 次级 | KD=8 最低，并入 cline alternative 文章 |
| cline alternative | 50 | 14 | $5.87 | 商业 | 次级 | 并入，量小但 KD 低 |
| local coding agent | 50 | 0 | $6.02 | 信息 | GEO | KD=0 完全空白，GEO 布局；语义精准 = Olares + Ollama + Cline |
| ollama coding agent | 20 | 0 | $6.56 | 信息 | GEO | KD=0，GEO 占位；"run cline with ollama on Olares" 场景标准词 |
| local llm coding agent | 30 | 0 | $0 | 信息 | GEO | KD=0，GEO 词；本地 LLM 运行编码代理 |
| ai coding agent open source | 30 | 0 | $0 | 信息 | GEO | KD=0，GEO 词 |

---

## 核心洞见

1. **品牌护城河：适度，对比词比护城河更有价值。** `cline` 主词（18,100 vol, KD70）霸榜 #1，品牌心智扎实；但品牌词流量集中（60%+）、非品牌词比例低，说明 Cline 的 SEO 仍以品牌驱动为主，未系统化布局品类词。对比词（`cline vs cursor` 1,300 vol, KD23）是比品牌词更有价值的攻击面——Cline 自己在排名 #2，说明这类词完全可打。

2. **可复制的打法——对比博客 + BYOK/成本叙事。** Cline 唯一的非品牌 Top 词是 `cline vs cursor`（blog 文章排 #2），揭示了有效打法：用"X vs Cline"对比文带来商业意图流量。Cline 完全不投 SEM，说明它依赖内容/开发者社区增长。可以复制 Lovable 的"guides + use-case 落地页矩阵"到"Cline on Olares + 本地模型"系列教程。

3. **对 Olares 最关键的 3 个词：`cline ollama`（90, KD23）、`open source coding agent`（210, KD20）、`github copilot alternative`（210, KD13）。** 前者直接命中"Cline 配本地模型"场景（Olares 提供 Ollama 基础设施），KD 仅 23；中者是 Olares Market 开源编码代理清单的最佳入口；后者 KD=13 + CPC $6.46，是全报告商业价值最高的低竞争词。

4. **最大攻击面：Cursor 的高价订阅制 vs Cline 的 BYOK 透明定价。** `cursor alternative`（880, KD25, CPC $7.34）、`cursor app free replacement`（210, KD20）等词直接指向 Cursor 用户的定价痛点。Cline 的差异化叙事"不烧固定订阅、不锁模型、代码不出本地"与 Olares 的"自托管 + 隐私"叙事高度共鸣——这是整条叙事的最强联结点。

5. **隐藏低 KD 金矿：对比词族群。** `cline vs continue`（KD10）、`cline vs github copilot`（KD10）、`roo vs cline`（KD14）、`github copilot alternative`（KD13）、`cline alternative`（KD14）——这些词 KD 都在 10-14，CPC 多超 $5，是低竞争高商业价值的绝佳机会。尤其 `roo vs cline`（170 vol）CPC $12.44，单词报告中最高。

6. **GEO 前瞻布局：Olares + Ollama + Coding Agent 词族。** `local coding agent`（KD0）、`ollama coding agent`（KD0）、`local llm coding agent`（KD0）、`cline local model`（KD0）、`ai coding agent open source`（KD0）当前近零量，但语义精准命中 Olares 场景。随着本地 LLM 成本持续下降、开发者隐私意识提升，这类词会快速增长。现在发布权威内容，抢 AI Overview / Perplexity 引用位，成本极低。

7. **与既有分析的关联/补充：** `olares-500-keywords` 分类 8"AI 编码助手"含 `cursor alternative`（KD25）、`github copilot alternative`（KD13）、`local ai coding agent`（KD21）——本报告中均得到 Semrush 实测数据印证，并新增了"cline 视角"（`cline vs cursor` / `cline ollama` / `roo code vs cline`）这一更具体的词族。旧词表的 `continue vs cursor`（90, KD22）与本报告的 `cline vs continue`（140, KD10）互补，建议在 seo-content 阶段合并为"AI 编码 Agent 品类对比"内容簇。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
