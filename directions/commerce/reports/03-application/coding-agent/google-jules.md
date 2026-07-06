# Google Jules SEO 竞品分析报告

> 域名：jules.google | SEMrush US | 2026-07-06
> Google Jules = 大厂旗舰异步 AI 编码 Agent（GitHub 集成、Cloud VM 运行、PR 交付，Gemini 驱动）

---

## 项目理解（前置）

Google Jules 是 Google Labs 出品的**异步 AI 编码 Agent**，用户提交任务后，Jules 将 GitHub 仓库克隆进 Google Cloud VM，由 Gemini 模型执行 bug 修复、功能开发、依赖升级、测试编写等任务，完成后输出 diff 并自动开 PR——用户不需全程守候。2026 年 3 月正式进入 Public Beta，无候补名单，全球可用。核心差异化在于**完全异步 + GitHub 原生 + 每日任务配额制**，区别于 Cursor/Windsurf 等同步 IDE 助手，与 Devin/GitHub Copilot Coding Agent 同属"后台 PR 机器"赛道。Olares 开源平替首选 OpenHands（前身 OpenDevin，MIT 协议，All Hands AI，模型无关，可完全自托管）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Google 出品的异步 AI 编码 Agent，GitHub Issue → Cloud VM → PR 全自动闭环 |
| 开源 / 许可证 | 闭源商业产品（Gemini 模型驱动） |
| 主仓库 | 无独立 GitHub 仓库；CLI 扩展通过 Gemini CLI 接入 |
| 核心功能 | Bug 修复、依赖升级、测试编写、功能实现、CI 失败自动修复、Audio Changelog |
| 商业模式 / 定价 | 免费：15 任务/天 3 并发 Gemini 2.5 Pro；Pro $19.99/月 100 任务/天 15 并发 Gemini 3 Pro；Ultra $124.99/月 300 任务/天 60 并发优先访问 |
| 差异化 / 价值主张 | 完全异步（提交即可离开）；GitHub 原生（Issue 标签触发）；同类最慷慨免费配额；CI 失败自动二次修复 |
| 主要竞品（初判）| Devin（Cognition）、GitHub Copilot Coding Agent、OpenAI Codex、Claude Code、OpenHands（开源） |
| Olares Market | 未上架（OpenHands 为开源平替，也未上架，有上架机会） |
| 来源 | [jules.google](https://jules.google/) / [FAQ](https://jules.google/docs/faq/) / [Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/jules/) / [sdd.sh Deep Dive](https://sdd.sh/2026/03/jules-deep-dive-googles-async-agent-that-closes-the-ci-loop-without-you/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | jules.google |
| SEMrush Rank | **168,440**（新产品，上线不足一年，流量仍在爬坡） |
| 自然关键词数 | 387 |
| 月自然流量（US）| 10,797 |
| 自然流量估值 | **$89,456/月** |
| 付费关键词数 | 0（无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | **71 词**（占 18%，品牌词高度集中） |
| 排名 4-10 位 | 39 词 |
| 排名 11-20 位 | 36 词 |

> 整体流量规模较小，符合"新产品爬坡"预期。品牌词（google jules / jules ai 等）贡献了流量主体；非品牌词排名当前仍在第 4-20 位候补区。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| jules.google（主站 + /docs/ 路径） | 387 | 10,797 | 100% |

> 无独立子域名分拆；文档、CLI 参考、Usage Limits 均在主域 /docs/ 路径下。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| google jules | 1 | 5,400 | 73 | $13.26 | 4,320 | 品牌/导航 | / |
| jules google | 1 | 2,400 | — | $8.68 | 1,920 | 品牌 | / |
| jules | 4 | 49,500 | 81 | $5.28 | 1,089 | 信息（泛名词） | /docs/ |
| jules ai | 1 | 1,000 | — | $6.95 | 800 | 品牌 | / |
| google jules ai | 1 | 390 | — | $5.59 | 312 | 品牌 | / |
| jule ia | 1 | 210 | — | $1.20 | 168 | 品牌（西班牙语变体） | / |
| jules coding agent | 1 | 170 | 68 | $8.14 | 136 | 品牌+品类 | / |
| jules google ai | 1 | 480 | — | $9.57 | 119 | 品牌 | / |
| jules 2 / jules 2.0 | 1 | 140 | — | — | 112 | 品牌 | / |
| google labs jules | 1 | 110 | — | — | 88 | 品牌 | / |
| jules ai google | 1 | 110 | — | $8.83 | 88 | 品牌 | / |
| google coding | 5 | 1,900 | — | $3.72 | 66 | 品类（宽泛） | / |
| juiles（误拼） | 1 | 260 | — | — | 64 | 品牌（误拼） | / |
| jules coding | 1 | 70 | — | $7.17 | 56 | 品牌+品类 | / |
| jules by google | 1 | 70 | — | $14.63 | 56 | 品牌 | / |
| google jules 2.0 | 1 | 70 | — | — | 56 | 品牌 | / |
| gemini jules | 1 | 210 | — | — | 52 | 品牌 | / |
| google coding agent | 2 | 390 | — | $12.45 | 31 | 品类 | / |
| google code agent | 2 | 210 | — | $12.45 | 27 | 品类 | / |
| google ai coding agent | 2 | 170 | — | $10.00 | 22 | 品类 | / |
| jules cli | 1 | 90 | — | — | 22 | 功能 | /docs/cli/reference/ |
| google jules pricing | 1 | 40 | 63 | — | 32 | 商业 | /docs/usage-limits/ |
| google codex | 3 | 170 | — | $2.90 | 11 | 竞品（误导向） | / |

> 核心观察：流量 99% 以上来自品牌/误拼变体词，jules.google 尚无非品牌自然流量护城河。`jules` 泛名词（49,500）排名第 4 靠的是品牌知名度，长期可能随品牌渗透上升。

### 付费词（Google Ads，按流量排序）

Google Jules **无任何付费广告投放**（adwords keywords = 0）。Google 选择完全依赖自然搜索和品牌知名度（Google 生态内部流量导入）。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| devin ai | 8,100 | 88 | $4.40 | 品牌 | 赛道标杆，KD 极高无法正面 |
| openhands | 4,400 | 53 | $4.73 | 导航 | Olares 平替主词，开源自托管 |
| windsurf vs cursor | 4,400 | 45 | $4.86 | 对比 | 相邻赛道，IDE 对比词 |
| github copilot coding agent | 880 | 65 | $3.49 | 品牌 | 最强竞品，Google 自家生态外 |
| cursor alternative | 880 | **25** | $7.34 | 商业 | ⭐ 整体 AI coding 替代词，借力 |
| opendevin | 720 | 31 | $8.17 | 导航 | OpenHands 前身，仍有搜索量 |
| swe-bench | 3,600 | 56 | $6.45 | 信息 | 赛道评测基准词 |
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐ Olares 直接机会 |
| github copilot alternative | 210 | **13** | $6.46 | 商业 | ⭐ KD 极低 |
| devin vs cursor | 210 | 30 | $5.92 | 对比 | ⭐ 赛道对比，可做多方比较文 |
| pr agent | 590 | **23** | $8.16 | 信息+商业 | ⭐ 功能词，开源 PR agent |
| autonomous coding agent | 50 | **13** | $8.73 | 信息 | ⭐ 低 KD，语义精准 |
| openhands vs cursor | 90 | **12** | — | 对比 | ⭐ 极低 KD |
| openhands vs devin | 50 | — | — | 对比 | 新兴对比词 |
| google jules alternative | 0 | — | $13.26 | 商业 | GEO 前哨（CPC 高，意图强） |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| claude code | 301,000 | 72 | $5.88 | 品牌 | 赛道最大词，Claude 制霸 |
| ai coding assistant | 9,900 | 65 | $9.27 | 信息 | 核心品类词，KD 高 |
| agentic coding tools | 1,600 | 46 | $7.59 | 信息 | 品类扩展词 |
| ai software engineer | 1,300 | 41 | $12.43 | 信息 | 高 CPC，概念词 |
| codex agent | 1,300 | 50 | $12.86 | 信息 | OpenAI 竞品品类词 |
| coding agent | 1,000 | 50 | $6.37 | 信息 | 核心品类词，难度中等 |
| agentic coding | 880 | 45 | $5.18 | 信息 | 品类关键词 |
| coding agents | 880 | **23** | $4.72 | 信息 | ⭐ 低 KD 品类词 |
| ai coding agents | 720 | **30** | $6.27 | 信息 | ⭐ KD 刚好在线 |
| swe agent | 720 | 41 | $6.83 | 信息 | 工程 agent 评测词 |
| ai code agent | 720 | 55 | $9.76 | 信息 | 高竞争 |
| agentic coding assistant | 590 | 38 | $6.22 | 信息 | 品类词 |
| ai coding agent | 590 | **36** | $6.27 | 信息 | ⭐ 核心品类词，KD 可接受 |
| best coding agent | 260 | **28** | $7.85 | 信息 | ⭐ 评测型，低 KD |
| best ai coding agent | 140 | **30** | $9.97 | 信息 | ⭐ 高 CPC + 低 KD |
| agentic ai coding assistant | 1,900 | 46 | $8.71 | 信息 | 品类长尾 |

### 产品 / 功能词（jules / google jules 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google jules | 4,400 | 73 | $13.26 | 品牌/导航 | 主品牌词，竞争极高 |
| jules ai | 1,000 | — | $6.95 | 品牌 | 品牌变体 |
| jules coding agent | 170 | 68 | $8.14 | 品牌+品类 | 半品牌词 |
| jules gemini | 170 | 62 | $16.10 | 品牌+功能 | 高 CPC（模型绑定） |
| google ai pro | 60,500 | 70 | $7.33 | 品牌 | Jules 计划绑定（Google AI 订阅） |
| google ai ultra | 9,900 | 75 | $15.39 | 品牌 | 超高 CPC，顶级订阅词 |
| google coding agent | 390 | — | $12.45 | 品类 | 品牌+品类混合 |
| google jules pricing | 40 | 63 | — | 商业 | 定价痛点词（KD 偏高） |
| google jules review | 30 | — | — | 信息 | 评测词，新兴 |
| google jules tutorial | 20 | — | — | 信息 | 教程词，新兴 |
| google labs jules | 110 | — | — | 品牌 | Labs 来源标签 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| aider | 6,600 | 51 | $5.66 | 信息+导航 | 主流开源代码 CLI，Olares 平替生态 |
| openhands | 4,400 | 53 | $4.73 | 导航 | Olares 平替核心词 |
| open hands | 2,900 | 48 | $4.73 | 信息 | openhands 变体 |
| opendevin | 720 | 31 | $8.17 | 导航 | OpenHands 前身，仍有流量 |
| open source coding agent | 210 | **20** | $5.51 | 信息 | ⭐ 自托管需求信号 |
| all hands ai | 320 | 52 | — | 信息 | All Hands AI（OpenHands 母公司） |
| openhands github | 320 | 54 | $7.15 | 导航 | 开源仓库词 |
| openhands ai | 170 | 43 | $6.12 | 信息 | |
| free ai coding agent | 30 | **25** | $6.39 | 信息 | ⭐ 明确"免费"需求信号 |
| local coding agent | 50 | **0** | $6.02 | 信息 | ⭐ 近零 KD，GEO 前哨 |
| ai coding agent open source | 30 | **0** | $5.20 | 信息 | ⭐ 近零 KD |
| self hosted coding agent | 30 | 39 | $4.25 | 信息 | 自托管需求 |
| llm coding agent | 30 | 38 | $4.16 | 信息 | 可接本地 LLM |
| opencode vs openhands | 110 | **16** | — | 对比 | ⭐ 开源生态内对比词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Google Jules 是闭源、Gemini 专有、GitHub 唯一、任务配额制；OpenHands 是 MIT 开源、模型无关（支持 Ollama 本地 LLM）、可完全自托管——Olares 上架 OpenHands 可直接承接"不想被 Google 锁定、不想消耗配额、要在私有代码库自托管 coding agent"的需求。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| openhands | 4,400 | 53 | $4.73 | ⭐⭐⭐ 开源平替核心词，OpenHands 上架 Olares Market；一键部署 vs Jules Cloud VM |
| coding agents | 880 | 23 | $4.72 | ⭐⭐⭐ 低 KD，「开源 self-hosted coding agents」清单文章绝佳切入，Olares 提供运行环境 |
| cursor alternative | 880 | 25 | $7.34 | ⭐⭐ 整体编码工具替代词，AI coding 本地化叙事（本地模型+自托管） |
| ai coding agents | 720 | 30 | $6.27 | ⭐⭐ 品类清单型，开源 vs 商业 coding agent 对比，OpenHands on Olares |
| opendevin | 720 | 31 | $8.17 | ⭐⭐ 大量用户仍用旧名搜索，可做「OpenDevin/OpenHands 在 Olares 上的安装教程」 |
| pr agent | 590 | 23 | $8.16 | ⭐⭐ 功能词低 KD，OpenHands 作为开源 PR agent 场景，Olares 自托管运行 |
| open source coding agent | 210 | 20 | $5.51 | ⭐⭐⭐ 直接命中 Olares 叙事，最强 Olares 机会词之一 |
| github copilot alternative | 210 | 13 | $6.46 | ⭐⭐ KD 极低，开源本地 coding agent 对比 Copilot 的叙事 |
| devin vs cursor | 210 | 30 | $5.92 | ⭐ 多方对比文章，引入 OpenHands（开源 Devin 替代）作第三维度 |
| openhands vs cursor | 90 | 12 | — | ⭐⭐ 极低 KD，用户已在主动对比，Olares 做运行基础设施角色 |
| best coding agent | 260 | 28 | $7.85 | ⭐⭐ 评测文章，开源视角：OpenHands + Aider on Olares |
| autonomous coding agent | 50 | 13 | $8.73 | ⭐ KD 极低，「开源自治 coding agent」场景，Olares 私有部署 |
| opencode vs openhands | 110 | 16 | — | ⭐ 开源 coding agent 生态内对比，Olares 可作两者的部署平台 |
| local coding agent | 50 | **0** | $6.02 | ⭐⭐⭐ KD=0 GEO 前哨，「在本地/私有服务器运行 coding agent」= Olares 核心叙事 |
| ai coding agent open source | 30 | **0** | $5.20 | ⭐⭐ KD=0，提前占位「开源 AI coding agent」内容 |
| google jules alternative | 0 | 0 | $13.26 | ⭐⭐ 当前量=0 但 CPC=$13.26（强商业意图），GEO 抢先布局；Jules 用户增长后转化潜力大 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| openhands | 4,400 | 53 | $4.73 | 导航 | 主词候选 | Olares 平替主品牌词，上架 OpenHands 后「在 Olares 上运行 OpenHands」教程可直接吃到 |
| coding agents | 880 | **23** | $4.72 | 信息 | 主词候选 | KD 低，开源自托管 coding agents 清单文章最佳入口；Jules 品类词 |
| ai coding agents | 720 | **30** | $6.27 | 信息 | 主词候选 | 品类词 KD 可打，开源 vs 商业评测视角，Olares 作部署底座 |
| open source coding agent | 210 | **20** | $5.51 | 信息 | 主词候选 | KD=20 直接匹配 Olares 叙事，最纯粹的 Olares 机会词 |
| cursor alternative | 880 | **25** | $7.34 | 商业 | 主词候选 | 高商业意图+低 KD，AI coding 开源本地化叙事，OpenHands/Aider on Olares |
| pr agent | 590 | **23** | $8.16 | 信息+商业 | 主词候选 | KD 低 + CPC $8，开源 PR agent 功能词，Olares 自托管运行场景 |
| best coding agent | 260 | **28** | $7.85 | 信息 | 主词候选 | 评测型主词，开源视角给 Olares 叙事留位，KD 可打 |
| github copilot alternative | 210 | **13** | $6.46 | 商业 | 主词候选 | KD=13 全场最低，商业意图强；开源本地 coding agent 替代 GitHub Copilot |
| opendevin | 720 | 31 | $8.17 | 导航 | 次级 | OpenHands 旧名仍有大量搜索，教程文章并入 openhands 词簇 |
| devin vs cursor | 210 | **30** | $5.92 | 对比 | 次级 | 对比文章拓展为三方矩阵（含 OpenHands 开源方案） |
| autonomous coding agent | 50 | **13** | $8.73 | 信息 | 次级 | KD 极低，语义精准，并入「开源自托管 coding agents」文章 |
| openhands vs cursor | 90 | **12** | — | 对比 | 次级 | KD=12 对比词，Olares 担任运行基础设施 |
| opencode vs openhands | 110 | **16** | — | 对比 | 次级 | 开源生态内对比，并入 openhands 词簇 |
| best ai coding agent | 140 | **30** | $9.97 | 信息 | 次级 | 高 CPC，并入「best coding agent」清单文章 |
| ai coding agent | 590 | **36** | $6.27 | 信息 | 次级 | 核心品类词，KD 可打，并入品类清单 |
| google jules | 4,400 | 73 | $13.26 | 品牌/导航 | 次级 | 品牌词 KD 高，不单独写文章，可作对比文中的提及词 |
| local coding agent | 50 | **0** | $6.02 | 信息 | GEO | KD=0，语义与 Olares「本地自托管」叙事完美契合，抢 AI 搜索引用位 |
| ai coding agent open source | 30 | **0** | $5.20 | 信息 | GEO | KD=0，GEO 占位「开源 AI coding agent」 |
| google jules alternative | 0 | 0 | $13.26 | 商业 | GEO | 量=0 但 CPC=$13.26，Jules 用户增长后转化率极高，提前布局 |
| self hosted coding agent | 30 | 39 | $4.25 | 信息 | GEO | 自托管需求明确，Olares 自托管 coding agent 的标签词 |

---

## 核心洞见

1. **Jules 品牌护城河浅，但"Google 背书"是最大护城河。** SEMrush Rank 168,440，流量规模远未成熟（对比 Devin/GitHub Copilot 的成熟品牌词），99% 流量来自品牌词。但 Google 不需要 SEO——它靠 Google Search/Gemini App/AI Studio 的内部流量漏斗导流，Jules 的增长路径与独立 SaaS 完全不同，不能用正常 SEO 视角评估其竞争力。结论：**无法正面抢 jules.google 的品牌词，也没必要，主战场是品类词和开源替代词**。

2. **最可复制的打法是"开源平替生态"矩阵内容。** Jules 的商业逻辑是"任务配额制 + Gemini 锁定 + GitHub 专属"，这三点都是可被开源替代的痛点。OpenHands 作为开源 Jules 替代，已有 4,400 月量，opendevin 还有 720 月量——用户在主动搜索开源替代方案。Olares 应围绕 OpenHands 构建"安装 + 对比 + 场景"的内容矩阵，这是已被验证的需求。

3. **对 Olares 最关键的 3 个词：`open source coding agent`（210, KD20）、`coding agents`（880, KD23）、`github copilot alternative`（210, KD13）。** 这三个词 KD 低、商业意图强、月量可用，且与 Olares 叙事完美契合——开源、自托管、可用本地 LLM、不烧 Google/GitHub 配额。

4. **最大攻击面：配额制 + 模型锁定 + 数据隐私 + GitHub 专属。** Jules 免费用户 15 任务/天（失败也扣配额），Pro 要 $19.99/月，且**只能用 Gemini**。OpenHands on Olares 对比叙事："无限任务次数、接 Ollama 本地模型零成本、代码不经 Google Cloud VM、支持 GitLab/自托管 Git、不限 15 任务天花板"——这正是 `google jules alternative`（CPC $13.26）这个高 CPC 词背后的用户痛点。

5. **隐藏低 KD 金矿：`github copilot alternative`（KD13）、`autonomous coding agent`（KD13）、`openhands vs cursor`（KD12）。** 三个词 KD 均≤13，月量在 50-210 之间，但 CPC 均超过 $6，说明背后商业意图真实。这类词单篇文章边际成本≈0，可批量收割。

6. **GEO 前瞻布局：`local coding agent`（KD0）、`ai coding agent open source`（KD0）、`google jules alternative`（量=0 但 CPC=$13.26）。** 这些词目前量极小，但"在私有服务器/本地运行 AI coding agent"这个需求会随 Jules 用量增长、数据隐私顾虑上升而爆发。提前发布权威内容，抢 AI Overview / Perplexity 的引用位，是高性价比的前置动作。

7. **与既有分析的关联：** 本报告与 `olares-500-keywords` 中「AI 编码」分类（cursor alternative KD25、github copilot alternative KD13）高度重叠，强化了"开源本地 coding 工具"的战略价值。OpenHands 目前未上架 Olares Market（products.md 对应行标 `⬜`），上架后将打通从 SEO 词→落地页→产品的完整漏斗。此外，`aider`（6,600 月量，KD51）作为另一个开源 coding CLI，也是值得关注的 Market 候补。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / domain_organic_organic / resource_adwords / phrase_these / phrase_related / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
