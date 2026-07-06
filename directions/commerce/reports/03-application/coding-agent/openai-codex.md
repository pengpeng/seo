# OpenAI Codex / Codex CLI SEO 竞品分析报告

> **降级模式（无独立域名）**：openai.com 为超大综合域名，跳过 Phase 1 域名流量基线，直接以关键词为核心展开分析。
> 域名：openai.com（Codex 无独立域名）| SEMrush US | 2026-07-06
> OpenAI Codex 是 OpenAI 旗下 AI 编码 Agent 产品线——包含云端 Codex Cloud（chatgpt.com/codex）与开源 CLI（Apache 2.0），捆绑 ChatGPT 订阅，是云端 coding agent 赛道的商业产品锚点。

---

## 项目理解（前置）

OpenAI Codex 是一个双态产品：**Codex Cloud**（chatgpt.com/codex）是云端自主编码 Agent，集成于 ChatGPT 订阅；**Codex CLI**（github.com/openai/codex，Apache 2.0，Rust 编写）是可本地运行的轻量终端编码 Agent。两者共用 ChatGPT 账号，CLI 亦支持通过 `--oss` flag 连接本地 Ollama 模型。2026 年 4 月发布以来已积累约 90K GitHub Stars，Terminal-Bench 2.1 基准排名第一。

| 项目 | 内容 |
|------|------|
| 一句话定位 | OpenAI 旗下 AI 编码 Agent，云端 Cloud + 本地 CLI 双态，捆绑 ChatGPT 订阅 |
| 开源 / 许可证 | CLI 部分开源（Apache-2.0）；云端 Codex 模型闭源 |
| 主仓库 | [github.com/openai/codex](https://github.com/openai/codex)（★ ~90K，2025-04 创建） |
| 核心功能 | 终端 TUI 交互式编码、多文件读写运行、内核级沙箱（Landlock/Seatbelt）、Cloud Task 云端自主执行、GitHub 代码审查 & Auto-PR、MCP 扩展、子 Agent 并行、Web 搜索、Ollama 本地模型（--oss） |
| 商业模式 / 定价 | 捆绑 ChatGPT Plus（$20/月）/ Pro（$200/月）/ Business / Edu / Enterprise；API Key 模式按 token 计费（需自备 key，无 Cloud 功能）；Pro 用户专享 GPT-5.3-Codex-Spark 快速模型（research preview） |
| 差异化 / 价值主张 | 内核级沙箱安全隔离（领先竞品）；Terminal-Bench 2.1 第一；GitHub 原生集成（Auto-PR、Issues）；与 ChatGPT 账号/模型生态深度绑定 |
| 主要竞品（初判）| Claude Code（Anthropic）、Gemini CLI（Google）、OpenCode（开源，75+ 模型）、Aider（开源，git-native）、Cursor、GitHub Copilot |
| Olares Market | 未上架（Olares 平替：OpenCode、Aider 均已在 Olares Market） |
| 来源 | [developers.openai.com/codex](https://developers.openai.com/codex) · [github.com/openai/codex](https://github.com/openai/codex) · [amux.io/blog](https://amux.io/blog/best-terminal-ai-coding-agents-2026/) · [wetheflywheel.com](https://wetheflywheel.com/en/guides/open-source-ai-coding-agents-2026/) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| codex vs claude code | 5,400 | **28** | $32.94 | 对比 | ⭐ 高量低 KD，CPC 极高 |
| claude code vs codex | 2,900 | 45 | $30.66 | 对比 | 同一对比词的倒置变体 |
| codex cli vs claude code | 480 | **15** | $27.41 | 对比 | ⭐ KD=15 超低 |
| openai codex vs claude code | 390 | 32 | $36.18 | 对比 | 高 CPC |
| codex vs cursor | 480 | **20** | $1.68 | 对比 | ⭐ 低 KD，CPC 很低 |
| codex vs gemini cli | 110 | **16** | $36.83 | 对比 | ⭐ KD=16，CPC 极高 |
| codex vs claude code vs gemini cli | 140 | **17** | $39.29 | 对比 | ⭐ 三方对比，CPC 最高 |
| gemini cli vs claude code vs codex | 110 | 0 | $281.13 | 对比 | 新兴，CPC 异常高 |
| codex vs github copilot | 90 | 35 | $12.81 | 对比 | |
| opencode vs codex | 40 | **15** | $14.75 | 对比 | ⭐ KD=15，Olares 直接机会 |
| aider vs opencode | 110 | **9** | $5.09 | 对比 | ⭐ KD=9，Olares 两者皆支持 |
| claude code alternative | 480 | **18** | $6.42 | 商业 | ⭐ Olares Market 的竞品入口 |
| cursor alternative | 880 | **25** | $7.34 | 商业 | ⭐ |
| github copilot alternative | 210 | **13** | $6.46 | 商业 | ⭐⭐ KD=13，CPC 高 |
| codex alternative | 30 | 0 | $13.97 | 商业 | ⭐ 近零 KD，需求刚刚萌芽 |
| openai codex alternative | 20 | 0 | $13.34 | 商业 | ⭐ GEO 级别，提前占位 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai coding assistant | 9,900 | 65 | $9.27 | 信息 | 品类大词，KD 高 |
| ai code editor | 2,400 | 47 | $8.10 | 信息 | |
| swe-bench | 3,600 | 56 | $6.45 | 信息 | benchmark 类，有技术内容机会 |
| best ai coding assistant | 1,300 | 50 | $8.91 | 信息 | 清单类内容 |
| ai coding tool | 1,000 | 50 | $9.15 | 信息 | |
| ai coding agent | 590 | **36** | $6.27 | 信息 | ⭐ KD<40 可竞争 |
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐ Olares 机会核心词 |
| ai pair programmer | 110 | 47 | $3.65 | 信息 | |
| best ai coding agent | 140 | **30** | $9.97 | 信息 | ⭐ 刚过 KD30 门槛 |
| best terminal coding agent | 10 | 0 | $8.18 | 信息 | ⭐ 近零竞争 |

### 产品 / 功能词（Codex 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| codex cli | 18,100 | 57 | $19.87 | 导航 | 核心品牌词 |
| openai codex | 14,800 | 76 | $28.26 | 品牌 | 高 KD，品牌护城河深 |
| chatgpt codex | 6,600 | 45 | $23.14 | 品牌 | |
| what is codex | 6,600 | 45 | $22.22 | 信息 | |
| openai codex cli | 5,400 | 57 | $23.59 | 品牌 | |
| codex pricing | 1,900 | **20** | $15.39 | 商业 | ⭐ KD=20，定价痛点词 |
| codex cli installation | 1,300 | 40 | $10.99 | 信息 | |
| codex cli mcp | 880 | 34 | $11.55 | 功能 | |
| codex desktop app | 880 | 35 | $49.66 | 导航 | CPC 极高 |
| codex cli resume | 720 | 39 | $30.83 | 功能 | |
| codex cli github | 720 | 52 | $23.71 | 功能 | |
| install codex cli | 480 | **30** | $11.27 | 信息 | ⭐ 刚过门槛 |
| codex cli mcp server | 480 | 47 | $28.45 | 功能 | 高 CPC |
| codex cli save chat | 390 | **27** | $0 | 功能 | ⭐ KD=27，零 CPC |
| codex cli plan mode | 210 | 38 | $16.21 | 功能 | |
| codex cli pricing | 110 | **32** | $13.29 | 商业 | |
| how to install codex cli | 110 | **28** | $11.31 | 信息 | ⭐ 安装教程词 |
| how much does openai codex cost | 210 | 34 | $20.52 | 商业 | |
| codex free | 90 | 45 | $11.22 | 商业 | 免费意图 |
| is codex cli free | 70 | 0 | $330.18 | 商业 | ⭐ KD=0，CPC 极高 |
| codex cli review | 30 | **19** | $14.34 | 评测 | ⭐ 低 KD 评测词 |
| codex vs claude code vs gemini cli | 140 | **17** | $39.29 | 对比 | ⭐ 三方对比，顶级 CPC |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐ 核心前哨词 |
| aider open source | 110 | **26** | $5.35 | 信息 | ⭐ |
| opencode vs codex | 40 | **15** | $14.75 | 对比 | ⭐ Olares 两端都能打 |
| self hosted coding agent | 30 | 39 | $4.25 | 信息 | |
| local llm coding agent | 30 | 0 | $5.12 | 信息 | ⭐ 近零竞争 |
| ollama coding agent | 20 | 0 | $6.56 | 信息 | ⭐ 近零竞争 |
| open source coding assistant | 90 | 50 | $5.07 | 信息 | KD 偏高 |
| codex cli open source | 20 | 0 | $67.22 | 信息 | ⭐ CPC 异常高 |
| self-hosted ai coding | 0 | 0 | $6.92 | 新兴 | GEO 级别 |
| github copilot alternative open source | 20 | 0 | $0 | 商业 | ⭐ GEO 占位 |
| local github copilot | 20 | 0 | $0 | 商业 | GEO |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Codex CLI 开源但锁定 OpenAI 模型（API-key 模式可绕开但无 Cloud 功能）；Olares Market 已有 OpenCode（75+ 模型提供商，含本地 Ollama）和 Aider（git-native，100+ 模型）作为真正模型无关的平替——主攻"codex vs"对比词 + 开源自托管词 + pricing 痛点词。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| codex vs claude code | 5,400 | **28** | $32.94 | ⭐⭐⭐ 对比页核心词；OpenCode on Olares = 同时支持 OpenAI + Claude + 75 家，一次部署全覆盖 |
| codex pricing | 1,900 | **20** | $15.39 | ⭐⭐⭐ 定价痛点词 KD=20；Olares + OpenCode：$0 平台费 + 自选最便宜模型 |
| codex vs cursor | 480 | **20** | $1.68 | ⭐⭐ KD=20；Olares 一键跑 OpenCode（多 session）vs Codex 需订阅 |
| codex cli vs claude code | 480 | **15** | $27.41 | ⭐⭐⭐ KD=15，高 CPC；Olares：终端 agent 全对比，OpenCode 无厂商绑定 |
| claude code alternative | 480 | **18** | $6.42 | ⭐⭐ Olares Market 直接入口词 |
| codex vs gemini cli | 110 | **16** | $36.83 | ⭐⭐⭐ KD=16，CPC $36；三方对比页，Olares 上 OpenCode 可跑所有模型 |
| codex vs claude code vs gemini cli | 140 | **17** | $39.29 | ⭐⭐⭐ 三方对比词，CPC 最高；Olares 一键多 Agent 同时跑 |
| github copilot alternative | 210 | **13** | $6.46 | ⭐⭐⭐ KD=13，Copilot 替代需求旺，OpenCode / Aider on Olares |
| open source coding agent | 210 | **20** | $5.51 | ⭐⭐ 泛需求词，Olares Market 列表页 + OpenCode/Aider 教程 |
| opencode vs codex | 40 | **15** | $14.75 | ⭐⭐ Olares Market 同时托管两侧，中立对比叙事 |
| aider vs opencode | 110 | **9** | $5.09 | ⭐⭐⭐ KD=9！Olares 两者同时提供，帮用户做选择 |
| codex alternative | 30 | 0 | $13.97 | ⭐⭐ 近零竞争，GEO + 内容占位 |
| local llm coding agent | 30 | 0 | $5.12 | ⭐⭐ Olares + Ollama + OpenCode 完整本地方案 |
| ollama coding agent | 20 | 0 | $6.56 | ⭐⭐ Olares + Ollama + Aider/OpenCode 教程，抢 GEO |
| codex cli open source | 20 | 0 | $67.22 | ⭐ CPC=$67，用户在找开源替代，Olares 教程 |
| self-hosted ai coding | 0 | 0 | $6.92 | ⭐ GEO 前哨，提前占位 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| codex vs claude code | 5,400 | 28 | $32.94 | 对比 | **主词候选** | KD28 + 量大 + CPC 极高，标准主词；OpenCode on Olares = 模型无关的第三选项 |
| codex pricing | 1,900 | 20 | $15.39 | 商业 | **主词候选** | KD=20 的定价痛点词；Olares 上 OpenCode/Aider = $0 平台费 + 自选廉价模型 |
| codex cli vs claude code | 480 | 15 | $27.41 | 对比 | **主词候选** | KD=15 超低 + CPC 极高，对比文核心；Olares 作为中立第三方 |
| codex vs gemini cli | 110 | 16 | $36.83 | 对比 | **主词候选** | KD=16 + CPC $36，三方对比切入；Olares 上 OpenCode 可跑所有三家模型 |
| codex vs claude code vs gemini cli | 140 | 17 | $39.29 | 对比 | **主词候选** | 三方对比词 KD=17，CPC 全场最高；Olares 多 Agent 并行叙事 |
| open source coding agent | 210 | 20 | $5.51 | 信息 | **主词候选** | KD=20，Olares Market 清单页核心词；OpenCode + Aider 双平替 |
| github copilot alternative | 210 | 13 | $6.46 | 商业 | **主词候选** | KD=13，Copilot 替代需求大；OpenCode / Aider on Olares 无厂商绑定 |
| ai coding agent | 590 | 36 | $6.27 | 信息 | **主词候选** | KD36 尚可竞争；Olares 自托管 AI coding agent 清单词 |
| codex cli | 18,100 | 57 | $19.87 | 导航 | 次级 | KD57 偏高，品牌导航词，量大作为语境引流 |
| openai codex | 14,800 | 76 | $28.26 | 品牌 | 次级 | KD76 打不动，但应在对比文中出现以吸引流量 |
| aider vs opencode | 110 | 9 | $5.09 | 对比 | 次级 | KD=9 极低，Olares 同时提供两者的中立对比页 |
| claude code alternative | 480 | 18 | $6.42 | 商业 | 次级 | KD=18，与 codex alternative 同聚一篇 |
| cursor alternative | 880 | 25 | $7.34 | 商业 | 次级 | KD=25，可与 codex/claude code alternative 合并 |
| opencode vs codex | 40 | 15 | $14.75 | 对比 | 次级 | KD=15，Olares Market 对比叙事支撑词 |
| how to install codex cli | 110 | 28 | $11.31 | 信息 | 次级 | 安装教程词，低 KD，可作为教程引流入 Olares |
| codex cli review | 30 | 19 | $14.34 | 评测 | 次级 | KD=19 低竞争评测词，带 Olares 平替比较 |
| best terminal coding agent | 10 | 0 | $8.18 | 信息 | GEO | 近零量但精准，抢 AI Overview 引用位 |
| local llm coding agent | 30 | 0 | $5.12 | 信息 | GEO | Olares + Ollama + OpenCode/Aider 完整本地方案 |
| ollama coding agent | 20 | 0 | $6.56 | 信息 | GEO | Olares + Ollama 本地 coding agent 教程抢占 |
| self-hosted ai coding | 0 | 0 | $6.92 | 新兴 | GEO | 近零量，提前布局等待爆发 |
| codex alternative | 30 | 0 | $13.97 | 商业 | GEO | CPC 高，语义精准，进 FAQ/前瞻段 |

---

## 核心洞见

1. **品牌护城河极深，正面硬刚无意义**：`openai codex`（KD76）、`codex cli`（KD57）、`codex`（KD76，135K 月量但含大量法律/税务 codex 歧义）均被 openai.com 牢牢控制，Olares 不应花力气争抢品牌词。`codex pricing`（KD20）是护城河最薄弱的缺口——定价痛点词 KD 仅 20，说明用户对 ChatGPT 订阅制度感到困惑，是最值得先打的单词。

2. **"codex vs" 对比词族是绝佳攻击面**：`codex vs claude code`（5,400/月，KD28，CPC $32.94）是本份报告发现的单个最高价值词——量大、KD 中低、CPC 极高（买词者知道这词能转化）。同族还有 `codex cli vs claude code`（KD15）、`codex vs gemini cli`（KD16）、`codex vs claude code vs gemini cli`（KD17），三个均在 KD≤20 区间，而且 CPC 高达 $27–$39，商业意图极强。Olares 作为"同时跑 OpenCode + Aider + 多模型"的中立平台，在这些对比词上有天然叙事优势。

3. **对 Olares 最关键的三个词**：① `codex vs claude code`（5,400，KD28）——高量低 KD 对比词，Olares 主打"无厂商绑定"第三选项；② `codex pricing`（1,900，KD20）——定价痛点词，Olares 上 OpenCode 零平台费可直接对比；③ `github copilot alternative`（210，KD13）——KD=13 几乎全场最低之一，Copilot 替代需求量稳且高 CPC，OpenCode/Aider on Olares 是天然落地页。

4. **最大攻击面：模型锁定 vs 订阅定价**：Codex CLI 虽然开源，但核心场景（Cloud Task、GitHub 集成、自动 PR）强依赖 OpenAI 账号且无 Cloud 功能版不支持本地模型；ChatGPT Plus/Pro 订阅价 $20–$200/月。`is codex cli free`（KD0，CPC $330！）和 `codex cli open source`（KD0，CPC $67）这两个问题词的异常高 CPC 揭示：**用户对 Codex "开源但要付费"的逻辑高度困惑**——这正是 Olares + OpenCode（真正免费自托管 + 75 家模型提供商）的差异化叙事切入点。

5. **隐藏低 KD 金矿**：`aider vs opencode`（KD=9）、`github copilot alternative`（KD=13）、`opencode vs codex`（KD=15）、`codex cli vs claude code`（KD=15）——这四个词 KD 均在 15 以下，Olares 有很强的排名胜算。尤其是 `aider vs opencode`（KD=9）：Olares Market 同时提供 Aider 和 OpenCode 两者，可以做一篇中立对比文，顺带植入"在 Olares 上同时试用两者"的 CTA。

6. **GEO 前瞻布局**：`local llm coding agent`（KD0）、`ollama coding agent`（KD0）、`best terminal coding agent`（KD0）、`self-hosted ai coding`（量≈0）——这些词目前竞争几乎为零，但语义与 Olares "本地 AI + Ollama + 开源 coding agent" 的叙事完美契合。建议提前发布权威内容，抢 AI Overview / Perplexity 引用位。另：中文词 `codex 安装`（1,300/月，KD41）和 `codex安装`（均为中文 UTF-8，同量）说明中文用户对安装教程需求旺盛，中文内容也有机会。

7. **与既有分析的关联**：本报告的"开源 coding agent"叙事与 [OpenCode 市场报告](/Users/pengpeng/seo/directions/market/reports/opencode.md)、[Claude Code 商业报告](/Users/pengpeng/seo/directions/commerce/reports/03-application/coding-agent/claude-code.md) 高度互补：OpenCode 报告已发现 `opencode vs claude code`（1,600/月，KD23）；本报告新增 `codex vs claude code`（5,400/月，KD28）。**三报告合并后，"coding agent 对比" 词族总量达 1 万月搜以上，均 KD<45**，可聚成一个高价值内容簇（"Best Terminal Coding Agents 2026：Codex vs Claude Code vs OpenCode vs Aider"）。与 `olares-500-keywords` 分析的关联：该词表中 "AI 编码" 品类目前以 Cursor/GitHub Copilot 为主，缺少 "terminal coding agent" 和 "open source coding agent" 这一子品类——本报告所发现的对比词族建议补入词表。

---

*数据来源：SEMrush US 数据库（phrase_these / phrase_related / phrase_questions / phrase_fullsearch）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
