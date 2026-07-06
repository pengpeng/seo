# Runner H SEO 竞品分析报告

> 域名：hcompany.ai | SEMrush US | 2026-07-06
> Runner H = 法国 H Company 的旗舰「computer-use」通用 Agent 平台——用一句自然语言编排子 Agent 跨浏览器/桌面/遗留系统执行多步任务，$220M 种子融资、现主打企业 on-prem 部署（闭源）

---

## 项目理解（前置）

Runner H 是巴黎 H Company（原名 "H"，2023 年由 Laurent Sifre、Charles Kantor 及三位 DeepMind 老将创立）的旗舰产品——一个 **computer-use（计算机操作）通用 Agent**：用户给一句自然语言指令，Runner H 就动态编排一组专用子 Agent，跨浏览器、文档系统、桌面/遗留系统（含无 API 的主机/mainframe）像人一样"看屏幕、点鼠标、打字"完成多步任务。它对标 OpenAI Operator/Deep Research、Anthropic Computer Use、Manus 这类深度研究 + 浏览器操作 Agent。2024 年 5 月拿下当时欧洲最大 AI 种子轮 **$220M**（Eric Schmidt、Amazon、Accel、三星等）。2025 年起在新 CEO（前 Palantir 法国 CEO）带领下**转向企业「forward-deployed engineers」on-prem 模式**，AWS Marketplace 私有报价起步 $100,000。

值得注意的**开源侧**：H 开源了 **Holo-1 / Holo-1.5**（3B 视觉语言模型，用于预测点击坐标）与 **Surfer-H-CLI**（Chrome 浏览器 Agent），Surfer-H + Holo-1 在 WebVoyager 达 92.2%。但**旗舰产品 Runner H / H Platform 本体仍是闭源 SaaS/企业合同**。

| 项目 | 内容 |
|------|------|
| 一句话定位 | computer-use 通用 Agent / 深度研究 + 浏览器·桌面自动化平台（企业级、闭源） |
| 开源 / 许可证 | **产品闭源**；仅开源底层模型 Holo-1/1.5（VLM）与 Surfer-H-CLI 浏览器 Agent |
| 主仓库 | github.com/hcompany-ai（Holo-1、Surfer-H-CLI；模型侧，非产品）|
| 核心功能 | ①自然语言编排多步任务 ②computer-use（无 API 直接操作 UI）③子 Agent 协同 + MCP 集成 ④Surfer H 浏览器 Agent ⑤Tester H 自动化软件测试 |
| 商业模式 / 定价 | 闭源 SaaS + 企业 on-prem（forward-deployed engineers）；AWS Marketplace 私有报价起 $100K；面向公众曾有 Runner H beta |
| 差异化 / 价值主张 | 全栈自有（模型+编排+Agent 一家负责）、专用小 VLM 推理成本号称低至 1/100、无需集成即可操作遗留系统 |
| 主要竞品（初判）| Manus、OpenAI Operator / Deep Research、Anthropic Computer Use、Genspark、Browser Use、UiPath（RPA） |
| Olares Market | 平替 **DeerFlow 2.0** 已上架（open-source super agent harness for deep research，见 market/reports/deerflow.md）|
| 来源 | hcompany.ai、en.wikipedia.org/wiki/H_(company)、businesswire（2025-06-03）、AWS Marketplace |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | hcompany.ai |
| SEMrush Rank | **668,926**（极低，SEO 几乎未起步）|
| 自然关键词数 | 193 |
| 月自然流量（US）| 1,939 |
| 自然流量估值 | $6,764/月 |
| 付费关键词数 | **0**（无 Google Ads 投放）|
| 月付费流量 | 0 |
| 排名 1-3 位 | 28 词 |
| 排名 4-10 位 | 34 词 |
| 排名 11-20 位 | 40 词 |

> 结论：$220M 融资的明星公司，SEO 体量却极小（自然流量不到 2K/月、193 个词、几乎全是品牌词）。原因是它**从 to-C beta 转向企业 on-prem 直销 + forward-deployed engineers**，几乎不做内容/SEO/SEM——获客靠销售与融资 PR，不靠搜索。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| hcompany.ai（主站）| 183 | 1,885 | 97.22% |
| tester.hcompany.ai | 1 | 51 | 2.63% |
| hub.hcompany.ai | 1 | 3 | 0.15% |
| portal.hcompany.ai | 8 | 0 | 0% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| h company | 1 | 720 | 47 | $3.31 | 576 | 品牌 | / |
| h ai | 1 | 320 | 69 | $5.86 | 256 | 品牌 | / |
| runner h | 1 | 880 | 24 | $4.60 | 218 | 品牌/产品 | /put-ai-to-work-for-you-with-runner-h |
| h company ai | 1 | 110 | 54 | $4.73 | 88 | 品牌 | / |
| h.ai | 1 | 90 | 55 | $5.86 | 72 | 品牌 | / |
| hcompany | 1 | 90 | 50 | $1.96 | 72 | 品牌 | / |
| holo1.5 | 1 | 260 | 24 | $0.00 | 64 | 产品 | /holo1-5-open-foundation-models… |
| the h company | 1 | 70 | 46 | $0.00 | 56 | 品牌 | / |
| runnerh | 1 | 210 | 19 | $0.00 | 52 | 品牌 | /put-ai-to-work-for-you-with-runner-h |
| h tester | 2 | 390 | 0 | $0.00 | 51 | 产品 | tester. |
| ai h | 4 | 720 | 85 | $1.53 | 46 | 品牌(泛) | / |
| h/ai | 1 | 140 | 53 | $4.71 | 34 | 品牌 | / |
| runner h ai agent | 1 | 40 | 13 | $6.33 | 32 | 产品 | /surfer-2 |
| runner h agent | 1 | 90 | 12 | $0.00 | 22 | 产品 | /put-ai-to-work-for-you-with-runner-h |
| h runner | 1 | 50 | 22 | $0.00 | 12 | 品牌 | / |
| runner h ai | 2 | 170 | 16 | $11.87 | 11 | 产品 | /put-ai-to-work-for-you-with-runner-h |
| company h | 4 | 140 | 34 | $4.02 | 9 | 品牌 | / |
| the holo | 15 | 1,600 | 77 | $0.00 | 8 | 品牌(泛) | / |
| surfer h | 2 | 50 | 32 | $0.00 | 6 | 产品 | /surfer-2 |
| holo computer | 1 | 110 | 31 | $0.64 | 2 | 产品 | /holo2 |

> 193 个词里**几乎全部是品牌词与品牌变体**（h company / runner h / holo1.5 / h tester / surfer h / hrunner…），零通用品类词进 TOP。唯一"泛词"如 `ai h`(720)、`the holo`(1600) 都是低相关误配、排名靠后。**没有任何程序化落地页、没有 guides/对比页、没有付费投放**——这是一个几乎不做 SEO 的公司。

### 付费词（Google Ads）

**无付费投放**（付费关键词 = 0）。H Company 不买 Google Ads，获客走企业直销与融资曝光。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

> **竞品发现（`domain_organic_organic`）结论：hcompany.ai 没有真实的 SEO 竞品**——共有词最多的都是 youtube/linkedin/wikipedia/crunchbase/github 等聚合站（相关度≈0），品牌太新、词太少。小域名 `runnerhai.com`（相关度 0.29，第三方蹭品牌站）、`aiagentstore.ai`/`bestaiagents.ai`/`aiagentsdirectory.com` 等 AI Agent 目录站是仅有的"同场"域名。真正的品类竞技场在下面的品类词里。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| manus alternative | 140 | **8** | $5.69 | 商业 | ⭐ 同品类头号替代词，KD 极低 |
| browser use alternative | 110 | **19** | $1.78 | 商业 | ⭐ 开源浏览器 Agent 替代 |
| manus vs genspark | 50 | **10** | $7.62 | 对比 | ⭐ 通用 Agent 对比 |
| open source manus | 50 | 42 | $7.95 | 信息 | 用户搜"开源版 Manus" |
| deerflow alternative | — | — | — | — | 无数据（我们平替品牌太新）|
| runner h alternative / runner h vs manus | 0 | — | — | — | **无搜索量**：Runner H 品牌搜索太弱，尚无替代/对比词沉淀 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| agentic ai | 90,500 | 90 | $7.80 | 信息 | 超级大词，打不动 |
| ai agents | 27,100 | 96 | $9.28 | 信息 | 超级大词 |
| deep research | 8,100 | 59 | $3.69 | 信息 | 核心品类词 |
| gemini deep research | 8,100 | 44 | $1.51 | 信息 | 大厂品牌 |
| browser use | 6,600 | 53 | $6.51 | 信息 | 开源浏览器 Agent（品牌+品类）|
| browserbase | 5,400 | **31** | $5.22 | 导航 | ⭐ 浏览器 Agent 基础设施 |
| claude computer use | 2,900 | 41 | $15.02 | 信息 | 高 CPC，对手大词 |
| openai operator | 2,400 | 72 | $5.87 | 信息 | 对手大词 |
| openai deep research | 2,400 | 68 | $4.48 | 信息 | 对手大词 |
| computer use agents | 1,300 | 58 | $0.00 | 信息 | 品类词 |
| computer use | 1,300 | 51 | $1.19 | 信息 | 品类词 |
| gptr | 1,300 | **20** | $0.05 | 导航 | ⭐ GPT-Researcher（开源深研）导航词 |
| anthropic computer use | 1,000 | 49 | $8.36 | 信息 | 对手 |
| computer use agent | 880 | 57 | $0.00 | 信息 | 品类词 |
| rpa ai | 880 | 59 | $7.52 | 信息 | RPA×AI |
| best ai agent | 720 | 51 | $8.14 | 商业 | 清单词 |
| **agentic operating system** | 720 | **26** | $8.54 | 信息 | ⭐⭐ 语义=Olares Agent-Native OS |
| gpt researcher | 590 | **30** | $2.94 | 信息 | ⭐ 开源深度研究 Agent |
| deerflow | 590 | 39 | $0.00 | 信息 | 我们的平替品牌词 |
| best deep research ai | 480 | **32** | $3.79 | 商业 | ⭐ 清单词 |
| ai rpa | 480 | 58 | $7.52 | 信息 | |
| ai deep research | 390 | 42 | $2.85 | 信息 | |
| browser use ai | 390 | **35** | $4.23 | 信息 | ⭐ |
| autonomous ai agent | 210 | 60 | $10.06 | 信息 | 高 CPC |
| local ai agent | 210 | **31** | $5.06 | 信息 | ⭐ 本地私有 Agent |
| ai research agent | 210 | **15** | $5.29 | 信息 | ⭐ 低 KD 金矿 |
| web agent | 210 | **35** | $5.53 | 信息 | ⭐ |
| ai browser automation | 140 | 50 | $8.72 | 信息 | |
| general ai agent | 140 | 65 | $5.22 | 信息 | 品类定位词 |
| local deep research | 110 | 50 | $0.00 | 信息 | 本地深研 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| runner h | 880 | **24** | $4.60 | 品牌/产品 | 对手品牌导航词 |
| h tester | 390 | 0 | $0.00 | 产品 | Tester H |
| holo1.5 | 260 | **24** | $0.00 | 产品 | 开源 VLM 模型 |
| runnerh | 210 | **19** | $0.00 | 品牌 | ⭐ |
| runner h ai | 170 | **16** | $11.87 | 产品 | ⭐ 高 CPC |
| runner h agent | 90 | **16** | $0.00 | 产品 | ⭐ |
| surfer h | 50 | **27** | $0.00 | 产品 | ⭐ 开源浏览器 Agent |
| runner h ai agent | 40 | **13** | $6.33 | 产品 | ⭐ |
| holo1 | 30 | **25** | $1.89 | 产品 | ⭐ 开源 VLM |
| tester h / holo-1 | 30 | 0 | — | 产品 | 新兴 |
| runner h review / runner h pricing / h company pricing | 0 | — | — | 商业 | **无搜索量**（品牌太新，尚无评测/定价需求沉淀）|

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source ai agent | 260 | 42 | $4.32 | 信息 | 核心信号词 |
| open source ai agent framework | 170 | 47 | $4.46 | 信息 | |
| open source deep research | 140 | 47 | $4.71 | 信息 | ⭐机会 |
| deep research open source | 140 | 52 | $0.00 | 信息 | |
| open source rpa | 140 | 41 | $4.26 | 信息 | |
| ai agent open source | 70 | 42 | $5.08 | 信息 | |
| open source manus | 50 | 42 | $7.95 | 信息 | |
| open source computer use agent | 20 | 0 | $6.58 | 新兴 | ⭐ 空白 |
| open source browser agent | 20 | 0 | $0.00 | 新兴 | 空白 |
| open source vision language model | 20 | 0 | $0.00 | 新兴 | 空白 |
| open source operator | 20 | 0 | $0.00 | 新兴 | 空白 |
| private ai agent | 20 | 0 | $5.97 | 新兴 | ⭐ 空白 |
| self hosted deep research | 30 | 0 | $0.00 | 新兴 | 空白 |
| self hosted ai agent | 10 | 0 | $4.59 | 新兴 | ⭐ 完美契合 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Runner H 是闭源、企业直销、on-prem 起价 $100K 的 computer-use Agent；Olares 侧平替 DeerFlow 2.0 是开源 super-agent deep-research harness，已上架 Olares Market，可一键自托管 + 接本地 LLM。叙事切入＝open-source / self-hosted / private「deep research & computer-use agent」，且直接呼应 Olares 的 "Agent-Native OS / 拥有你的 AI" 品牌主线。** Runner H 品牌词本身量太小、无法作为攻击面，真正的战场是 deep research / browser agent / 开源自托管品类词。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| deep research | 8,100 | 59 | $3.69 | ⭐ 品类大词，导向"self-hosted deep research agent（DeerFlow on Olares）" |
| browser use | 6,600 | 53 | $6.51 | ⭐ 开源浏览器 Agent，可上架 Olares Market + 教程 |
| **agentic operating system** | 720 | 26 | $8.54 | ⭐⭐⭐ 几乎就是 Olares 的定位（Agent-Native OS），低 KD，必占 |
| gpt researcher | 590 | 30 | $2.94 | ⭐⭐ 另一开源 deep-research Agent，"self-host GPT Researcher on Olares" |
| deerflow | 590 | 39 | $0.00 | ⭐⭐⭐ 我们平替的品牌词，做"DeerFlow 2.0 self-hosted / install on Olares" |
| best deep research ai | 480 | 32 | $3.79 | ⭐⭐ 清单文，把开源自托管 DeerFlow/GPT-Researcher 排进榜 |
| browser use ai | 390 | 35 | $4.23 | ⭐ 承接 browser-use 品类 |
| local ai agent | 210 | 31 | $5.06 | ⭐⭐ = Olares 核心用例（本地私有 Personal Agent）|
| ai research agent | 210 | **15** | $5.29 | ⭐⭐ 低 KD 金矿，"open-source AI research agent you can self-host" |
| web agent | 210 | 35 | $5.53 | ⭐ 浏览器 Agent 品类承接 |
| manus alternative | 140 | **8** | $5.69 | ⭐⭐ 极低 KD，Manus/Runner H 类闭源 Agent 的开源自托管替代 |
| open source deep research | 140 | 47 | $4.71 | ⭐⭐ 精准信号词，DeerFlow 直接命中 |
| open source ai agent | 260 | 42 | $4.32 | ⭐ 信号词，Olares Market Agent 生态承接 |
| browser use alternative | 110 | **19** | $1.78 | ⭐⭐ 低 KD，导向自托管浏览器 Agent |
| local deep research | 110 | 50 | $0.00 | ⭐ 本地深研＝隐私叙事 |
| open source rpa | 140 | 41 | $4.26 | ⭐ RPA 侧信号词 |
| open source manus | 50 | 42 | $7.95 | ⭐ "开源版 Manus/通用 Agent" |
| self hosted ai agent | 10 | 0 | $4.59 | ⭐⭐⭐ GEO：近零量、语义完美契合 Olares |
| private ai agent | 20 | 0 | $5.97 | ⭐⭐⭐ GEO：私有 Agent = Olares 卖点 |
| self hosted deep research | 30 | 0 | $0.00 | ⭐⭐⭐ GEO 占位 |
| open source computer use agent | 20 | 0 | $6.58 | ⭐⭐ GEO：computer-use 开源占位 |
| open source browser agent | 20 | 0 | $0.00 | ⭐⭐ GEO 占位 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| deep research | 8,100 | 59 | $3.69 | 信息 | 次级 | 品类大词 KD 高排不动，作导流锚点导向 self-hosted deep research 内容 |
| browser use | 6,600 | 53 | $6.51 | 信息 | 次级 | 开源浏览器 Agent 品类，承接到 Olares Market 上架 + 教程 |
| agentic operating system | 720 | 26 | $8.54 | 信息 | 主词候选 | ⭐ 几乎就是 Olares 定位（Agent-Native OS），低 KD、高 CPC，撑一篇定位/科普文 |
| deerflow | 590 | 39 | $0.00 | 信息 | 主词候选 | 我们平替的品牌词，"DeerFlow 2.0 self-hosted on Olares"权威页 |
| gpt researcher | 590 | 30 | $2.94 | 信息 | 主词候选 | 开源 deep-research Agent，自托管教程 + 对比 |
| best deep research ai | 480 | 32 | $3.79 | 商业 | 主词候选 | 清单文把开源自托管 DeerFlow/GPT-Researcher 排进榜 |
| ai research agent | 210 | 15 | $5.29 | 信息 | 主词候选 | ⭐ 低 KD 金矿，开源可自托管的 AI 研究 Agent |
| local ai agent | 210 | 31 | $5.06 | 信息 | 主词候选 | = Olares 核心用例（本地私有 Personal Agent）|
| gptr | 1,300 | 20 | $0.05 | 导航 | 次级 | GPT-Researcher 导航词，借力导流自托管教程 |
| browser use ai | 390 | 35 | $4.23 | 信息 | 次级 | browser-use 品类承接词 |
| browser use alternative | 110 | 19 | $1.78 | 商业 | 次级 | 低 KD，自托管浏览器 Agent 替代 |
| manus alternative | 140 | 8 | $5.69 | 商业 | 次级 | 极低 KD，闭源通用 Agent 的开源自托管替代（并入 Manus 报告簇）|
| open source deep research | 140 | 47 | $4.71 | 信息 | 次级 | 精准信号词，DeerFlow 直接命中 |
| open source ai agent | 260 | 42 | $4.32 | 信息 | 次级 | 信号词，Olares Agent 生态承接 |
| runner h | 880 | 24 | $4.60 | 品牌 | 次级 | 对手品牌导航词，抢不动；靠 "runner h alternative / vs" 承接（当前 0 量，先埋 GEO）|
| self hosted ai agent | 10 | 0 | $4.59 | 新兴 | GEO | 近零量语义完美契合 Olares，抢 AI Overview 引用位 |
| private ai agent | 20 | 0 | $5.97 | 新兴 | GEO | 私有 Agent = Olares 隐私叙事 |
| self hosted deep research | 30 | 0 | $0.00 | 新兴 | GEO | DeerFlow 精准占位 |
| open source computer use agent | 20 | 0 | $6.58 | 新兴 | GEO | computer-use 开源占位，对标 Surfer-H/Holo |

---

## 核心洞见

1. **品牌护城河：几乎不存在 SEO 护城河，但也没有 SEO 战场可抢。** Runner H/hcompany.ai 是 $220M 明星公司却 SEMrush Rank 68 万、193 个词、月自然流量不到 2K、零付费——因为它已**转向企业 on-prem 直销（$100K 起）+ forward-deployed engineers**，获客靠销售和融资 PR，不靠搜索。它的品牌词（runner h 880/KD24、h company 720）量小且无溢出的替代/对比词（`runner h alternative`、`runner h pricing` 均 0 量）。**结论：不值得围绕 Runner H 品牌词做承接，价值全在它所在的品类词。**

2. **可复制的打法：无。** Runner H 没有程序化落地页、没有对比页、不买大词、内容极少。反面教材——它把所有精力投在企业销售而非可被搜索发现的内容。Olares 反而应该做它没做的事：**在 deep research / computer-use / browser agent 品类词上用开源自托管叙事建内容矩阵**，填补这个"高融资但低 SEO 存在感"的品类空白。

3. **对 Olares 最关键的 3 个词：`agentic operating system`（720/KD26）、`deerflow`（590/KD39）、`ai research agent`（210/KD15）。** ①`agentic operating system` 几乎就是 Olares 的品牌定位（Agent-Native OS），低 KD 高 CPC，是把品类词与品牌叙事焊死的战略词；②`deerflow` 是我们已上架平替的品牌词，做权威自托管页可直接承接品类流量；③`ai research agent` KD 仅 15，是"开源可自托管研究 Agent"的完美入口。

4. **最大攻击面：闭源 + 企业级高门槛 + 云依赖。** Runner H 产品闭源、on-prem 需 $100K 私有合同、多租户默认云端。Olares 的差异化直击："开源、一键自托管、接本地 LLM、数据/推理不出设备、个人也能拥有 computer-use/deep-research Agent"——正好对上 `self hosted ai agent`(KD0)、`private ai agent`(KD0)、`open source deep research`(KD47) 这批信号词。

5. **隐藏低 KD 金矿：`ai research agent`（210/KD15）、`manus alternative`（140/KD8）、`browser use alternative`（110/KD19）、`agentic operating system`（720/KD26）、`gpt researcher`（590/KD30）、`best deep research ai`（480/KD32）。** 这些量>0 且 KD<35，配合 DeerFlow 2.0 / GPT-Researcher / Browser-Use 上架 Olares Market，可低成本抢占——远比 `agentic ai`(KD90)、`ai agents`(KD96) 这类超级大词划算。

6. **GEO 前瞻布局：** `self hosted ai agent`(KD0)、`private ai agent`(KD0)、`self hosted deep research`(KD0)、`open source computer use agent`(KD0)、`open source browser agent`(KD0) 目前近零量，但语义与 Olares 完美契合。建议提前发布权威内容（"self-hosted deep research agent on Olares"、"open-source computer-use agent you own"）抢 AI Overview / Perplexity 引用位——computer-use Agent 是 2026 热点，需求即将放量。

7. **与既有分析的关联：** 本报告与同区 general-agent 报告（manus / genspark / perplexity-computer / chatgpt-agent）共享 DeerFlow 2.0 平替叙事，可跨报告聚成一个"open-source self-hosted deep research / general agent"内容簇；`agentic operating system`、`local ai agent`、`ai research agent` 应补入 `olares-500-keywords` 词表的「AI Agent / Deep Research」子品类——目前该表对 computer-use / deep research agent 覆盖偏弱。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / domain_organic_organic / phrase_these / phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
