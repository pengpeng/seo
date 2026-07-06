# Amp SEO 竞品分析报告

> 域名：ampcode.com | SEMrush US | 2026-07-06
> Amp = Sourcegraph 分拆的前沿 AI 编码 Agent（CLI + IDE 扩展），多模型路由 + 无溢价按用量计费，2025 年 12 月独立公司

---

## 项目理解（前置）

Amp 由 Sourcegraph 联合创始人 Quinn Slack 与 Beyang Liu 于 2025 年 12 月从 Sourcegraph 剥离成立独立公司 Amp, Inc.，定位"前沿编码 Agent 研究实验室"。产品以 CLI 与 VS Code 系 IDE 扩展双形态提供，核心差异化在于：自动在 Claude Opus / GPT-5.5 / Gemini 等前沿模型间路由（按任务选最优），零溢价透传 API 成本，并内建 Librarian 子代理（可搜索公开 GitHub 及私有仓库）。前身 Sourcegraph Cody 个人/免费计划已于 2025 年 7 月全面停止，Amp 为其正式接班人。据报道 Amp 在分拆时已实现盈利，短暂尝试广告支持免费层（$10/天），于 2026 年 3 月撤广告并保留免费用量。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 前沿 AI 编码 Agent：CLI + IDE 扩展，多模型自动路由，零溢价按用量计费 |
| 开源 / 许可证 | **闭源**（商业产品；Sourcegraph Cody 曾有 Apache-2.0 扩展快照，Amp 本体不开源） |
| 主仓库 | 无公开主仓库（插件生态开放，核心闭源） |
| 核心功能 | ① CLI + VSCode 系 IDE 扩展；② 多模型自动路由（Opus 4.8 / GPT-5.5 / Haiku 等）；③ Librarian 子代理（GitHub 全局代码搜索）；④ 远程 Orb 沙盒执行；⑤ 插件 API（事件钩子 / 自定义工具 / 策略部署）；⑥ 线程持久化 + 远程控制（passkey 认证） |
| 商业模式 / 定价 | 免费层：$10/天额度（仅交互式，非 API/自动化）；个人 pay-as-you-go：零溢价，最低 $5 充值；企业：一次性 $1,000 起，含 SSO / 零数据留存 / BYOK 区域端点 |
| 差异化 / 价值主张 | 多模型自动路由；opinionated 设计哲学（敢杀功能）；据报盈利；Plugin API；远程可控 Agent Orb |
| 主要竞品（初判）| Claude Code（Anthropic）、Cursor（Anysphere）、GitHub Copilot CLI、Aider（开源）、OpenCode（开源） |
| Olares Market | **未上架**（闭源 SaaS；开源平替 OpenCode ✅ 已上架，Aider 可 Olares 自托管） |
| 来源 | [ampcode.com](https://ampcode.com/)、[ampcode.com/manual](https://ampcode.com/manual)、[Sourcegraph 博客 - 分拆公告](https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies)、[Wikipedia - Sourcegraph](https://en.wikipedia.org/wiki/Sourcegraph) |

---

## 流量基线（Phase 1）

### 概览

> ampcode.com 2025 年 12 月才从 sourcegraph.com 独立，是一个极新的域名，SEO 积累从零开始。与之对比，OpenCode（opencode.ai）已达 86,280 月流量、Sourcegraph.com 有 8,737 月流量。

| 指标 | 数据 |
|------|------|
| 域名 | ampcode.com |
| SEMrush Rank | **270,173**（新域名，尚未进入前 20 万） |
| 自然关键词数 | 703 |
| 月自然流量（US）| **6,207** |
| 自然流量估值 | **$35,607/月** |
| 付费关键词数 | 0（无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 57 词 |
| 排名 4-10 位 | 60 词 |
| 排名 11-20 位 | 77 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| ampcode.com（主站） | 703 | 6,207 | 100% |

> 无独立子域名流量（docs/blog 等均并入主站）。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| ampli code | 1 | 1,600 | 45 | $7.02 | 1,280 | 品牌(误触) | / |
| amp agent | 1 | 1,000 | 64 | $8.24 | 800 | 品牌/信息 | / |
| amp code | 1 | 880 | 53 | $3.14 | 704 | 品牌 | / |
| amp ai | 1 | 720 | 25 | $5.15 | 178 | 信息 | / |
| ampcode | 1 | 590 | 39 | $3.14 | 472 | 品牌 | / |
| amp blog | 1 | 480 | 26 | $0.00 | 119 | 品牌 | /chronicle |
| sourcegraph amp | 1 | 480 | 48 | $5.21 | 119 | 品牌 | / |
| amp coder | 1 | 390 | 38 | $7.02 | 312 | 品牌 | / |
| amp plugin | 1 | 390 | 48 | $1.05 | — | 功能 | / |
| ampcode cli | 1 | 320 | 42 | $8.89 | 256 | 品牌/功能 | / |
| amp pricing | 1 | 320 | 59 | $0.67 | 256 | 商业 | / |
| amp model | 1 | 320 | 23 | $0.39 | 42 | 功能 | /models |
| amp coding agent | 1 | 260 | 50 | $7.23 | 208 | 品牌 | / |
| amp labs | 1 | 260 | 50 | $0.00 | — | 品牌 | /news/amp-labs |
| gpt-5.3-codex | 4 | 720 | 48 | $21.50 | 46 | 信息 | /news/gpt-5.3-codex |
| amp vs claude code | **2** | 140 | **13** | $17.15 | 11 | 对比 | /threads/… |
| amp code agent | 1 | 140 | 28 | $7.23 | 112 | 品牌 | / |
| am code | 1 | 480 | 15 | $0.00 | 63 | 误搜 | / |
| amcoder | 27 | 14,800 | 12 | $0.43 | 22 | 误搜 | / |
| amp free | 1 | 110 | 45 | $0.00 | 27 | 信息 | /free |
| oracle amp | 1 | 40 | 14 | $8.78 | 9 | 商业 | /news/oracle |
| amp login | 13 | 1,300 | 29 | $0.00 | 9 | 导航 | /auth/sign-in |
| opencode vs claude code | — | 1,600 | 23 | $8.28 | — | 对比 | — |

> **重要洞察**：`amcoder`（月量 14,800，KD 12）排在 ampcode.com 第 27 名，说明有大量"打错字"用户流向本站但没有实质转化——这是品牌曝光漏斗里一个真实的低竞争词，但需要注意用户意图是否与 Amp 匹配。另外，`gpt-5.3-codex`（720 月量，CPC $21.50）由 Amp 新闻页引流，说明"头条新闻 + 新模型发布" 是 Amp 当前获得非品牌流量的主要路径。

### 付费词（Google Ads）

**无投放**。Amp 目前完全依赖自然搜索，无 Google Ads 预算。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| claude code | 301,000 | 72 | $5.88 | 品牌 | 品类最大词，Amp 主要竞品 |
| opencode | 40,500 | 58 | $6.39 | 导航 | 开源替代，Olares 已上架 |
| aider | 6,600 | 51 | $5.66 | 品牌/信息 | 开源替代，git-native CLI |
| sourcegraph cody | 1,300 | 64 | $5.39 | 品牌 | Amp 前身，已停止个人版 |
| claude code vs cursor | 6,600 | 38 | $10.60 | 对比 | 高量对比词，Amp 可出现 |
| cursor vs claude code | 4,400 | 30 | $11.69 | 对比 | ⭐ 竞品对比大词 |
| windsurf vs cursor | 4,400 | 45 | $4.86 | 对比 | 品类对比词 |
| cursor vs copilot | 1,900 | 32 | $6.78 | 对比 | ⭐ |
| opencode vs claude code | 1,600 | 23 | $8.28 | 对比 | ⭐ Amp 直接相关 |
| claude code free | 1,600 | 34 | $9.79 | 信息 | ⭐ 定价痛点词 |
| claude code pricing | 14,800 | 39 | $5.05 | 商业 | 定价对比机会 |
| claude code alternative | 480 | **18** | $6.42 | 商业 | ⭐ 超低 KD！ |
| claude code alternatives | 320 | **18** | $3.62 | 商业 | ⭐ |
| cursor alternative | 880 | **25** | $7.34 | 商业 | ⭐ |
| github copilot alternative | 210 | **13** | $6.46 | 商业 | ⭐⭐ 极低 KD！ |
| aider vs cursor | 210 | **9** | $4.17 | 对比 | ⭐⭐ KD=9 极低 |
| opencode vs aider | 210 | **14** | $0.00 | 对比 | ⭐⭐ |
| claude code vs windsurf | 260 | **25** | $9.95 | 对比 | ⭐ |
| claude code vs copilot | 590 | **17** | $8.43 | 对比 | ⭐ |
| amp vs claude code | 140 | **13** | $17.15 | 对比 | ⭐⭐ Amp 已排名 #2，极高 CPC |
| open source claude code | 210 | **30** | $13.63 | 信息 | ⭐ 开源替代词 |
| open source claude code alternative | 50 | **19** | $3.58 | 信息 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai coding assistant | 9,900 | 65 | $9.27 | 信息 | 品类大词，高 KD |
| ai coding tool | 1,000 | 50 | $9.15 | 信息 | |
| coding agent | 1,000 | 50 | $6.37 | 信息 | |
| ai coding agent | 590 | **36** | $6.27 | 信息 | ⭐ |
| agentic coding assistant | 590 | **38** | $6.22 | 信息 | ⭐ |
| agentic coding | 880 | 45 | $5.18 | 信息 | |
| what is agentic coding | 480 | **36** | $3.34 | 信息 | ⭐ |
| best coding agent | 260 | **28** | $7.85 | 信息 | ⭐ |
| best ai coding agent | 140 | **30** | $9.97 | 信息 | ⭐ |
| ai pair programming | 720 | **38** | $5.63 | 信息 | ⭐ |
| terminal coding agent | 10 | 0 | $5.66 | 信息 | GEO |
| cli coding agent | 30 | 0 | $5.83 | 信息 | GEO |
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐⭐ |
| coding agent cli | 20 | 0 | — | 信息 | GEO |

### 产品 / 功能词（Amp 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| amp agent | 1,000 | 64 | $8.24 | 信息 | 品牌词，已排名 #1 |
| ampcode | 590 | 39 | $3.14 | 品牌 | 已排名 #1 |
| amp cli | 210 | 44 | $6.50 | 功能 | |
| amp model | 320 | **23** | $0.39 | 功能 | ⭐ /models 页 |
| sourcegraph amp | 320 | 58 | $4.99 | 品牌 | |
| amp ai coding | 70 | **34** | $6.16 | 信息 | ⭐ |
| amp pricing | 170 | 45 | $1.05 | 商业 | |
| amp vs claude code | 140 | **13** | $17.15 | 对比 | ⭐⭐ 已排 #2，强战略词 |
| amp labs | 260 | 50 | $0.00 | 品牌 | 企业计划相关 |
| amp enterprise | 90 | **26** | $2.93 | 商业 | ⭐ |
| amp free | 110 | 45 | $0.00 | 信息 | |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| aider | 6,600 | 51 | $5.66 | 品牌 | 最大开源替代品牌词 |
| opencode | 40,500 | 58 | $6.39 | 导航 | 最大开源替代品牌词（Olares 已上架）|
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐⭐ KD=20 |
| aider open source | 110 | **26** | $5.35 | 信息 | ⭐ |
| open source coding assistant | 90 | 50 | $5.07 | 信息 | |
| self hosted coding agent | 30 | **39** | $4.25 | 信息 | 信号词 |
| local llm coding agent | 30 | 0 | $5.12 | 信息 | GEO |
| opencode self hosted | 10 | 0 | $0.00 | 信息 | GEO |
| aider self hosted | 0 | — | — | — | GEO（近零量） |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Amp 是闭源 SaaS + 透传 API 成本的 pay-as-you-go 模式；Olares Market 已上架 OpenCode（MIT 开源），并可运行 Aider——两者可对接本地 Ollama 模型（Qwen2.5-Coder 等），实现"零云服务费 + 代码不出本地 + 私有部署"的完整对立叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| opencode | 40,500 | 58 | $6.39 | ⭐⭐ OpenCode 已上架 Olares Market，"Amp 开源平替一键部署" |
| aider | 6,600 | 51 | $5.66 | ⭐⭐ 用 Olares 自托管 Aider + 本地 Ollama，零 API 费用 |
| claude code vs cursor | 6,600 | 38 | $10.60 | ⭐ Olares 可切入：开源自托管是第三条路 |
| cursor vs claude code | 4,400 | 30 | $11.69 | ⭐ |
| agentic coding | 880 | 45 | $5.18 | ⭐ "本地 agentic coding with OpenCode on Olares" |
| cursor alternative | 880 | 25 | $7.34 | ⭐⭐ 开源替代 Cursor，Olares 部署 |
| opencode vs claude code | 1,600 | 23 | $8.28 | ⭐⭐⭐ 直接场景：OpenCode on Olares vs 云端 Amp/Claude Code |
| aider vs cursor | 210 | **9** | $4.17 | ⭐⭐⭐ KD=9 极低，"在 Olares 跑 Aider 替代 Cursor/Amp" |
| claude code alternative | 480 | **18** | $6.42 | ⭐⭐⭐ 核心攻击词：OpenCode on Olares = 免费本地 Claude Code 平替 |
| github copilot alternative | 210 | **13** | $6.46 | ⭐⭐ Olares 部署 OpenCode/Aider，自托管 Copilot 平替 |
| open source coding agent | 210 | **20** | $5.51 | ⭐⭐⭐ 直接命中 Olares Market 上的 OpenCode |
| amp vs claude code | 140 | **13** | $17.15 | ⭐⭐ Amp 已在 #2，可写"Amp vs Claude Code vs OpenCode（Olares）"三方对比 |
| open source claude code | 210 | **30** | $13.63 | ⭐⭐ "开源 Claude Code = OpenCode，Olares 一键装" |
| opencode vs aider | 210 | **14** | $0.00 | ⭐⭐ 两款 Olares 平替的对比，吃双份词 |
| aider open source | 110 | **26** | $5.35 | ⭐ |
| self hosted coding agent | 30 | 39 | $4.25 | ⭐⭐ 直接描述 Olares 场景 |
| local llm coding agent | 30 | 0 | $5.12 | ⭐ GEO 占位 |
| terminal coding agent | 10 | 0 | $5.66 | GEO |
| opencode self hosted | 10 | 0 | — | GEO |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|----|------|------|--------------------------|
| claude code alternative | 480 | **18** | $6.42 | 商业 | **主词候选** | KD18 超低，高商业意图；Olares 核心攻击词——OpenCode on Olares = 免费本地 Claude Code 平替 |
| opencode vs claude code | 1,600 | **23** | $8.28 | 对比 | **主词候选** | 月量大+KD低，直接场景：OpenCode on Olares vs 云端 Amp/Claude Code |
| cursor vs claude code | 4,400 | **30** | $11.69 | 对比 | **主词候选** | 月量极大，CPC $11.7；开源自托管是第三条路叙事入口 |
| claude code vs cursor | 6,600 | 38 | $10.60 | 对比 | **主词候选** | 同上，量更大，KD 偏高但 CPC 极高值得打 |
| open source coding agent | 210 | **20** | $5.51 | 信息 | **主词候选** | KD=20，直接命中 Olares Market 上的 OpenCode |
| aider vs cursor | 210 | **9** | $4.17 | 对比 | **主词候选** | KD=9 极低金矿，"在 Olares 跑 Aider" 可切入；簇合计量可观 |
| github copilot alternative | 210 | **13** | $6.46 | 商业 | **主词候选** | KD=13 极低+高商业意图，Olares 开源替代路径 |
| opencode vs aider | 210 | **14** | $0.00 | 对比 | **主词候选** | 两款 Olares 平替对比，一篇文章吃双词 |
| amp vs claude code | 140 | **13** | $17.15 | 对比 | **主词候选** | KD=13 + CPC $17，Amp 已排 #2 但流量极少；可做"Amp vs Claude Code vs OpenCode"三方对比 |
| claude code free | 1,600 | 34 | $9.79 | 信息 | 次级 | 定价痛点词；"用 OpenCode on Olares 永久免费"叙事 |
| claude code alternatives | 320 | **18** | $3.62 | 商业 | 次级 | 与 claude code alternative 同簇 |
| cursor alternative | 880 | **25** | $7.34 | 商业 | 次级 | 跨报告词（Cursor 报告主词），此处次级引流 |
| what is agentic coding | 480 | **36** | $3.34 | 信息 | 次级 | 内容布道词，带出 OpenCode on Olares |
| aider open source | 110 | **26** | $5.35 | 信息 | 次级 | Olares 开源路径引流词 |
| open source claude code alternative | 50 | **19** | $3.58 | 信息 | 次级 | 低量但意图精准，并入主词簇 |
| best coding agent | 260 | **28** | $7.85 | 信息 | 次级 | 清单型词，带出开源自托管方向 |
| self hosted coding agent | 30 | 39 | $4.25 | 信息 | 次级 | Olares 场景词，量小但语义精准 |
| terminal coding agent | 10 | 0 | $5.66 | 信息 | GEO | 近零量，完美描述 Olares+OpenCode/Aider 场景，抢引用位 |
| local llm coding agent | 30 | 0 | $5.12 | 信息 | GEO | 本地 LLM + Olares 叙事 GEO 布局 |
| opencode self hosted | 10 | 0 | — | 信息 | GEO | 近零量，语义与 Olares 完美契合 |
| aider self hosted | 0 | — | — | — | GEO | 0 量但抢先布局，Olares 场景词 |
| cli coding agent | 30 | 0 | $5.83 | 信息 | GEO | 前沿词，Amp/OpenCode/Aider 共同场景 |

---

## 核心洞见

1. **品牌护城河极弱，"amp"品牌严重歧义——正面硬刚意义不大。** ampcode.com 月流量仅 6,207（US），SEMrush Rank 270,173，是一个月龄不足 7 个月的极新域名。更关键的是，"amp"这个词本身极度歧义：amp.dev（Google AMP 标准）、amp.ai（另一个 AI 产品）、amptab.com 都在争抢同一 SERP 空间。Amp 的大部分关键词流量来自品牌误搜（ampli code、amcoder 等），品类词占比极低。Olares 不需要正面与 Amp 竞争，而应聚焦其品类词和替代词。

2. **真正可复制的打法：抢"Claude Code alternative"低 KD 对比词生态。** Amp 靠新闻页（`/news/gpt-5.3-codex`）获取 `gpt-5.3-codex` 词的非品牌流量（46 次），说明"新模型发布 + 测评报告"路径有效，但天花板很低。真正的机会在 Claude Code alternative（KD18）/ cursor alternative（KD25）/ github copilot alternative（KD13）等词——Amp 自己连这些词都还没打，Olares 可以抢先布局。

3. **对 Olares 最关键的 3 个词：`claude code alternative`（480, KD18）、`opencode vs claude code`（1,600, KD23）、`aider vs cursor`（210, KD9）。** 这三个词 KD 全部低于 25，且直接指向 Olares Market 上的 OpenCode 与 Aider。搜索 "claude code alternative" 的用户在找付费替代方案，Olares 的叙事是："OpenCode + Olares = 在你自己的服务器上跑一个永久免费、代码不出门的 Claude Code"。

4. **最大攻击面：API 成本与数据隐私。** Amp 的商业模式是透传 API 成本——零溢价听起来很好，但用户跑一个复杂任务可能花 $5-$20 美元（Claude Opus 4.8 每百万 token 约 $15）。这与 Lovable 的 credits 如出一辙。Olares 叙事直击痛点："本地 Qwen2.5-Coder / 接 Ollama = 无限次 coding agent，无 API 账单，代码永不上云"。`claude code free`（1,600, KD34）/ `claude code pricing`（14,800, KD39）等词是很好的导流词。

5. **隐藏低 KD 金矿：`aider vs cursor`（KD9）和 `github copilot alternative`（KD13）。** `aider vs cursor` 月量 210 但 KD 仅 9，说明还没有强内容方在深耕这个词；`github copilot alternative` KD13 + 商业意图明确，是极低竞争的高价值词。两个词都可以用 Olares 上的 OpenCode / Aider 切入。

6. **GEO 前瞻布局：** `terminal coding agent`（KD0）、`local llm coding agent`（KD0）、`opencode self hosted`（KD0）、`aider self hosted`（0量）、`cli coding agent`（KD0）这些词目前搜索量极低，但语义与 Olares 场景高度契合。建议在 OpenCode 的 Olares 安装教程、Aider on Olares 文章里提前写入这些词，抢 AI Overview / Perplexity 引用位。

7. **与既有分析的关联：** 本报告揭示的 `claude code alternative`（KD18）/ `github copilot alternative`（KD13）与 `olares-500-keywords` 里已有的 `cursor alternative`、`tabnine self-hosted` 等词高度互补。建议建立一个"AI 编码 Agent 对比"词簇，以 OpenCode on Olares 为核心落地页，同时接住 Amp / Claude Code / Cursor / Copilot 的替代词流量——这些词分散在多份报告（claude-code.md 已完成），可在 seo-content 阶段跨报告聚簇为一篇"Best Open Source Claude Code / Cursor Alternative"清单文章。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / domain_organic_organic / phrase_these / phrase_related / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
