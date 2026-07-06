# Exa SEO 竞品分析报告

> 域名：exa.ai | SEMrush US | 2026-07-06
> Exa = AI-native 语义搜索 API——面向 AI Agent 的联网工具，估值 $2.2B，2026 年成为 AI Agent 搜索基础设施的事实标准

---

## 项目理解（前置）

Exa（前身 Metaphor）是一家专为 AI Agent 构建的搜索引擎公司，提供语义搜索 API、网页内容抓取和深度研究功能。与传统搜索 API（SerpAPI、Bing Search API）不同，Exa 用神经网络嵌入模型索引全网，以向量语义而非关键词匹配进行检索，天然契合 LLM 的工作方式。核心客户包括 Cursor、Cognition（Devin）、HubSpot、Monday.com 及全球 5,000 家以上的 AI 公司。2026 年 5 月完成 a16z 领投的 $250M Series C，估值达 $2.2B，不到一年内估值翻逾 3 倍（Series B 时为 $700M）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 面向 AI Agent 的语义搜索 API，联网工具市场的基础设施层 |
| 开源 / 许可证 | **闭源 SaaS**；无公开主仓库 |
| 主仓库 | —（exa-py / exa-js SDK 有开源 wrapper，核心引擎闭源） |
| 核心功能 | Search（语义搜索/180ms 极低延迟）、Contents（网页全文）、Deep Search（多步研究）、Monitors（定时监控）、Agent（异步深度研究）、Websets（结构化公司/人员数据库） |
| 商业模式 / 定价 | Free tier 20K requests/月；Search $7/1K；Contents $1/1K pages；Deep Search $12-15/1K；Monitors $15/1K；Enterprise 自定义 |
| 差异化 / 价值主张 | 1）语义 > 关键词（向量检索，更懂 LLM 意图）；2）延迟最低（<180ms Instant）；3）Highlights 去噪（专训模型提取相关片段，节省 90% Token）；4）ZDR（Zero Data Retention）；5）专为 MCP/Agent 工具调用优化 |
| 主要竞品（初判）| Tavily（同赛道，AI 搜索 API）、SerpAPI、Brave Search API、Bing Search API、Jina AI（内容提取）、Perplexity API |
| Olares Market | SearXNG ✅ [已上架](/Users/pengpeng/seo/directions/market/apps.md)；Firecrawl ✅ [已上架](/Users/pengpeng/seo/directions/market/apps.md)（均可自托管，共同构成 Exa 的开源平替组合） |
| 来源 | [exa.ai](https://exa.ai)、[exa.ai/pricing](https://exa.ai/pricing)、[exa.ai/blog/announcing-series-c](https://exa.ai/blog/announcing-series-c)、[bloomberg.com](https://www.bloomberg.com/news/articles/2026-05-20/andreessen-backed-ai-search-startup-exa-valued-at-2-2-billion)、[a16z.com](https://a16z.com/announcement/investing-in-exa/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | exa.ai |
| SEMrush Rank | **48,921**（中等，早期成长阶段；开发者 API 工具的正常区间）|
| 自然关键词数 | 19,967 |
| 月自然流量（US）| 42,210 |
| 自然流量估值 | $81,954/月 |
| 付费关键词数 | **0**（完全依赖自然流量，无 Google Ads 投放）|
| 月付费流量 | 0 |
| 排名 1-3 位 | 560 词 |
| 排名 4-10 位 | 3,924 词 |
| 排名 11-20 位 | 3,841 词 |

> **关键信号**：零付费广告——Exa 完全靠口碑（开发者社区/AI 公司推荐）和 SEO 自然增长。与 Lovable（付费流量 283K，远超自然）的"重投广告"策略完全相反。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| exa.ai（主站） | 19,075 | 41,628 | 98.62% |
| websets.exa.ai | 789 | 409 | 0.97% |
| twitterwrapped.exa.ai | 15 | 118 | 0.28% |
| auth.exa.ai | 7 | 22 | 0.05% |
| companyresearcher.exa.ai | 19 | 16 | 0.04% |
| roastmywebsite.exa.ai | 5 | 13 | 0.03% |
| 其余（demo / dashboard / chat / codingdemo 等）| <30 | <5 | <0.01% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| exa | 1 | 9,900 | 60 | $3.22 | 7,920 | 品牌 | / |
| exa ai | 1 | 3,600 | 51 | $2.23 | 2,880 | 品牌 | / |
| e x a | 1 | 880 | 50 | $2.75 | 704 | 品牌(变体) | / |
| exa search | 1 | 720 | 42 | $2.72 | 576 | 品牌 | / |
| exa.ai | 1 | 720 | 50 | $2.23 | 576 | 品牌 | / |
| exa websets | 1 | 480 | 49 | $3.90 | 384 | 品牌 | /websets |
| **doordash company address** | 1 | 1,300 | 29 | $1.40 | 322 | 信息 | /websets/directory/doordash-offices |
| exa api | 1 | 390 | 25 | $4.35 | 312 | 品牌/信息 | / |
| walgreens corporate address | 1 | 1,000 | 62 | $0 | 248 | 信息 | /websets/directory/walgreens-offices |
| **exa mcp** | 1 | 1,000 | 20 | $3.78 | 248 | 信息 | /docs/reference/exa-mcp |
| exa api key | 1 | 260 | 18 | $2.93 | 208 | 品牌/商业 | / |
| uber corporate address | 1 | 720 | 39 | $0 | 178 | 信息 | /websets/directory/uber-offices |
| exa labs | 1 | 210 | 44 | $3.02 | 168 | 品牌 | / |
| exa careers | 1 | 210 | 22 | $0 | 168 | 招聘 | /careers |
| doordash address | 7 | 6,600 | 30 | $0 | 158 | 信息 | /websets/directory/doordash-offices |
| exa web search | 1 | 170 | 35 | $3.17 | 136 | 品牌 | / |
| exa people search | 1 | 170 | 0 | $5.87 | 136 | 品牌/功能 | /docs/reference/verticals/people |
| exa pricing | 1 | 170 | 21 | $3.64 | 136 | 商业 | /pricing |
| websets | 1 | 170 | 18 | $3.34 | 136 | 品牌/品类 | /websets |
| exa ai search | 1 | 170 | 52 | $3.06 | 136 | 品牌 | /search |
| stripe office locations | 1 | 1,000 | 37 | $0 | 132 | 信息 | /websets/directory/stripe-offices |
| paypal corporate headquarters | 6 | 5,400 | 27 | $0 | 129 | 信息 | /websets/directory/paypal-offices |
| exa search api | 1 | 140 | 24 | $4.69 | 112 | 品牌/信息 | / |
| netflix hq | 4 | 4,400 | 38 | $0 | 105 | 信息 | /websets/directory/netflix-offices |
| **best api search company's homepage** | 23 | 60,500 | 26 | $0 | 90 | 信息 | / |
| exa search mcp | 1 | 110 | 36 | $3.20 | 88 | 信息 | /docs/reference/exa-mcp |
| exa ai api | 1 | 110 | 32 | $2.63 | 88 | 品牌 | / |
| exa playground | 1 | 70 | 36 | $2.87 | 56 | 品牌 | / |
| exa code | 1 | 70 | 30 | $0 | 56 | 品牌/信息 | /blog/exa-code |
| exa ai careers | 1 | 70 | 16 | $0 | 56 | 招聘 | /careers |

> **程序化落地页洞察**：`/websets/directory/` 下有大量公司办公室地址页（DoorDash、Walgreens、Uber、Netflix、Stripe、PayPal、SpaceX 等），排名高量大词如 `doordash address`（6,600/月）、`paypal corporate headquarters`（5,400/月）。这是 Exa Websets 做公司数据库的 SEO 副产品——与 Lovable 的 `/guides/` 程序化落地页异曲同工。
>
> **意外发现**：`best api search company's homepage` 月量 60,500、KD 26，Exa 排名 23——此词极其高量，若进前 10 将带来大幅流量跳升。

### 付费词（Google Ads）

Exa 当前**无 Google Ads 投放**（付费关键词数 = 0）。完全依靠开发者口碑、内容营销和自然 SEO。这与同期估值 $2.2B 的 SaaS 工具形成鲜明对比。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| tavily | 9,900 | 59 | $3.60 | 商业/信息 | 最强直接竞品，量大但 KD 适中 |
| serpapi | 9,900 | 56 | $3.07 | 商业 | 传统搜索 API 老品牌 |
| serp api | 5,400 | 67 | $3.07 | 商业 | 品类通用词 |
| brave search api | 4,400 | 41 | $1.75 | 商业 | 隐私向搜索 API |
| jina ai | 1,600 | 79 | $5.70 | 商业 | 内容提取竞品 |
| serper.dev | 320 | 32 | $2.18 | 商业 | ⭐ 轻量 SerpAPI 替代 |
| you.com api | 480 | 30 | $0 | 商业 | ⭐ |
| tavily search api | 320 | 29 | $3.03 | 商业/信息 | ⭐ 竞品产品词 |
| perplexity alternative | 90 | 11 | $2.83 | 商业 | ⭐ 极低 KD |
| firecrawl alternative | 50 | 10 | $7.58 | 商业 | ⭐ 极低 KD，Olares 直接机会 |
| tavily alternative | 30 | 6 | $6.97 | 商业 | ⭐ 极低 KD |
| jina ai alternative | 20 | 0 | $0 | 商业 | ⭐ 新兴 |
| exa alternative | 20 | 0 | $0 | 商业 | ⭐ 新兴，量极小 |
| exa ai alternative | 20 | 4 | $4.38 | 商业 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| search api | 1,300 | 59 | **$51.62** | 信息 | 超高 CPC，商业价值极高 |
| ai search tool | 590 | 76 | $3.63 | 信息 | KD 极高 |
| web search api | 320 | 54 | $14.47 | 信息 | 高 CPC |
| llm search | 260 | 33 | $5.00 | 信息 | ⭐ |
| web search mcp | 210 | 30 | $2.93 | 信息 | ⭐ MCP 新兴词，快速增长 |
| openai web search | 140 | 32 | $5.82 | 信息 | ⭐ |
| ai search api | 90 | 39 | $15.56 | 信息 | 高 CPC |
| web search api for llm | 40 | 15 | $16.67 | 信息 | ⭐ 极低 KD + 超高 CPC |
| search api for ai | 30 | 0 | $6.93 | 信息 | ⭐ 新兴 |
| llm web search | 20 | 0 | $4.05 | 信息 | ⭐ 新兴 |
| search grounding | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| grounding api | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| **exa mcp** | 1,000 | **20** | $3.78 | 信息 | ⭐ 量/KD 最佳比，MCP 工具页已排第 1 |
| exa websets | 480 | 57 | $3.90 | 商业 | 品牌功能词 |
| exa api | 390 | 25 | $4.35 | 信息 | ⭐ |
| exa search api | 140 | 24 | $4.69 | 信息 | ⭐ |
| exa pricing | 170 | 21 | $3.64 | 商业 | ⭐ 定价痛点词 |
| exa search mcp | 90 | 20 | $4.59 | 信息 | ⭐ |
| exa api key | 260 | 18 | $2.93 | 商业 | ⭐ |
| exa people search | 170 | 0 | $5.87 | 功能 | ⭐ |
| exa documentation | 20 | 0 | $0 | 信息 | 品牌导航词 |
| exa neural search | 20 | 0 | $0 | 信息 | ⭐ GEO 方向 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| firecrawl | 18,100 | 63 | $4.34 | 信息 | 平替组合核心词，Olares 已上架 |
| searxng | 8,100 | 64 | $1.67 | 信息 | 平替组合核心词，Olares 已上架 |
| crawl4ai | 4,400 | 46 | $5.18 | 信息 | 开源爬虫替代 |
| web scraping api | 1,300 | 46 | $6.96 | 信息 | 广义爬虫需求 |
| firecrawl api | 880 | 34 | $5.85 | 商业 | ⭐ 可切入：Firecrawl on Olares |
| open source search engine | 390 | 61 | $2.08 | 信息 | 高 KD |
| jina reader | 320 | 35 | $4.97 | 商业 | ⭐ 内容提取竞品/替代 |
| searxng docker | 260 | 40 | $3.22 | 信息 | 部署教程词 |
| web crawler python | 320 | 31 | $1.92 | 信息 | ⭐ |
| self hosted search engine | 110 | 32 | $0 | 信息 | ⭐ 自托管信号词 |
| open source web crawler | 110 | 38 | $2.92 | 信息 | |
| searxng api | 140 | **20** | **$49.73** | 商业 | ⭐⭐ 超高 CPC + 极低 KD，绝佳机会 |
| firecrawl alternative | 50 | **10** | $7.58 | 商业 | ⭐⭐ 极低 KD，Olares 直接机会 |
| open source search api | 20 | 0 | $0 | 信息 | ⭐ 新兴 |
| self hosted search | 20 | 0 | $0 | 信息 | ⭐ 新兴 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Exa 是闭源按量付费 API（$7/1K 次起），面向 AI Agent 的搜索工具。Olares Market 已同时上架 SearXNG（自托管搜索引擎）和 Firecrawl（开源爬虫/内容提取），两者组合可复现 Exa 的核心能力——搜索 + 内容提取——且数据自有、无 API 调用成本、可用本地 Agent 无限调用。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| firecrawl | 18,100 | 63 | $4.34 | ⭐⭐⭐ Olares Market 已上架，"自托管 Firecrawl 替代 Exa Contents" |
| searxng | 8,100 | 64 | $1.67 | ⭐⭐⭐ Olares Market 已上架，"自托管搜索引擎替代 Exa Search" |
| crawl4ai | 4,400 | 46 | $5.18 | ⭐⭐ 开源爬虫，可作 Olares 第三方应用候选 |
| web scraping api | 1,300 | 46 | $6.96 | ⭐⭐ 自托管爬虫组合（Firecrawl on Olares）叙事入口 |
| web search mcp | 210 | 30 | $2.93 | ⭐⭐⭐ MCP 工具词快速增长；SearXNG MCP server 可在 Olares 自托管 |
| zoominfo alternative | 720 | 30 | $33.13 | ⭐⭐ Exa Websets 竞争的赛道；Olares 可托管开源 B2B 数据工具 |
| firecrawl api | 880 | 34 | $5.85 | ⭐⭐ "Firecrawl on Olares" 安装教程词 |
| clearbit alternative | 210 | **3** | $18.21 | ⭐⭐⭐ KD=3 极低 + 高 CPC；公司数据 API 替代，Olares 自托管方案 |
| b2b data api | 210 | **12** | $14.40 | ⭐⭐ 极低 KD + 高商业价值 CPC |
| searxng api | 140 | **20** | **$49.73** | ⭐⭐⭐ KD 极低 + CPC 最高（$49.73），部署在 Olares 的 SearXNG 可提供 API |
| perplexity alternative | 90 | 11 | $2.83 | ⭐⭐ 低 KD，"开源自托管 Perplexity 替代" 叙事（SearXNG + Firecrawl）|
| tavily alternative | 30 | 6 | $6.97 | ⭐⭐ 极低 KD，对比页切入（Exa/Tavily 闭源 vs Olares 自托管）|
| firecrawl alternative | 50 | **10** | $7.58 | ⭐⭐ 直接指向 Firecrawl on Olares |
| self hosted search engine | 110 | 32 | $0 | ⭐⭐ 自托管搜索引擎，SearXNG on Olares |
| web search api for llm | 40 | **15** | $16.67 | ⭐⭐⭐ 极低 KD + 超高 CPC；"本地 LLM + SearXNG 联网搜索" 方案 |
| exa alternative | 20 | 0 | $0 | ⭐ 新兴，量小，GEO 占位 |
| open source search api | 20 | 0 | $0 | ⭐ GEO 前哨 |
| self hosted search | 20 | 0 | $0 | ⭐ GEO 前哨 |
| search grounding | 20 | 0 | $0 | ⭐ GEO 前哨，LLM grounding 方向 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| firecrawl | 18,100 | 63 | $4.34 | 信息 | 次级 | Olares Market 已上架，"Firecrawl on Olares"教程词，KD 虽高但已有产品支撑 |
| searxng | 8,100 | 64 | $1.67 | 信息 | 次级 | Olares Market 已上架，品类词 KD 高，靠已有报告借力 |
| crawl4ai | 4,400 | 46 | $5.18 | 信息 | 主词候选 | 开源 AI 爬虫快速增长，可作 Olares Market 上架机会词 |
| brave search api | 4,400 | 41 | $1.75 | 商业 | 次级 | 搜索 API 品类词，导向 Exa vs 开源替代对比 |
| web scraping api | 1,300 | 46 | $6.96 | 信息 | 主词候选 | 自托管爬虫（Firecrawl on Olares）叙事，量足 + KD 适中 |
| search api | 1,300 | 59 | $51.62 | 信息 | 次级 | CPC 极高（$51.62），主词竞争激烈但可作对比页次级词 |
| **exa mcp** | 1,000 | **20** | $3.78 | 信息 | **主词候选** | KD=20 + 月量 1,000，"SearXNG MCP on Olares vs Exa MCP" 对比教程 |
| exa websets | 480 | 57 | $3.90 | 商业 | 次级 | 品牌词，导向 Websets 替代（开源公司数据）|
| exa api | 390 | 25 | $4.35 | 信息 | 主词候选 | KD=25，API 介绍/对比页，Olares 自托管搜索 API 替代入口 |
| zoominfo alternative | 720 | 30 | $33.13 | 商业 | 主词候选 | KD=30 + 超高 CPC，Exa Websets 竞争的赛道；自托管公司数据方案 |
| firecrawl api | 880 | 34 | $5.85 | 商业 | 主词候选 | 量大+KD 适中，"自托管 Firecrawl API"使用教程，直接 Olares 机会 |
| jina reader | 320 | 35 | $4.97 | 商业 | 次级 | 内容提取竞品，"Firecrawl on Olares vs Jina" 对比页次级词 |
| exa search api | 140 | 24 | $4.69 | 信息 | 主词候选 | KD=24 + 开发者意图，对比页入口"Exa Search API vs SearXNG API" |
| web search mcp | 210 | 30 | $2.93 | 信息 | **主词候选** | MCP 工具词高速增长，KD=30，"SearXNG MCP Server on Olares"可直接承接 |
| **searxng api** | 140 | **20** | **$49.73** | 商业 | **主词候选** | KD=20 + CPC $49.73（全表最高），Olares 运行的 SearXNG 可暴露 API 端点，商业价值极高 |
| clearbit alternative | 210 | **3** | $18.21 | 信息 | **主词候选** | KD=3 极低 + CPC $18，Exa Websets 的竞争场景，Olares 自托管数据富集方案 |
| b2b data api | 210 | **12** | $14.40 | 信息/商业 | **主词候选** | KD=12 + 高 CPC，Websets 品类词，自托管 B2B 数据 API 叙事 |
| web search api for llm | 40 | **15** | $16.67 | 信息 | **主词候选** | KD=15 + CPC $16.67，技术决策词，"本地 LLM + SearXNG 联网"精准覆盖 |
| perplexity alternative | 90 | 11 | $2.83 | 商业 | 次级 | 低 KD，"开源自托管 Perplexity/Exa 替代" 对比页次级词 |
| tavily alternative | 30 | 6 | $6.97 | 商业 | 次级 | 极低 KD，"Exa/Tavily vs SearXNG+Firecrawl 自托管对比" |
| firecrawl alternative | 50 | 10 | $7.58 | 商业 | 次级 | KD=10，直指 Firecrawl on Olares |
| self hosted search engine | 110 | 32 | $0 | 信息 | 次级 | SearXNG on Olares 教程可承接 |
| exa alternative | 20 | 0 | $0 | 商业 | GEO | 量极小但语义精准，GEO 布局"Exa 开源自托管替代方案" |
| search grounding | 20 | 0 | $0 | 信息 | GEO | LLM grounding 新兴词，"Olares Agent + SearXNG 实现搜索 Grounding" |
| open source search api | 20 | 0 | $0 | 信息 | GEO | 空白词，GEO 先发优势 |
| web search api for agents | 10 | 0 | $9.06 | 信息 | GEO | 高 CPC + 零量，Agent 时代核心词，抢先占位 |

---

## 核心洞见

1. **品牌护城河：无法正面刚，但护城河比想象中浅。** Exa 主要流量来自品牌词（exa/exa ai 合计约 10,800 月量），KD 50-60，无法抢。但与 Lovable（品牌词 10 万月量）相比，Exa 的品牌词量级远小——说明它仍是开发者口耳相传的早期工具，非大众认知的成熟产品。这意味着**品类词竞争窗口仍然开放**，现在布局的 SEO 内容还来得及。

2. **可复制的打法——程序化公司数据落地页（Websets 目录）。** Exa 的 `/websets/directory/` 系列页面（DoorDash/Uber/Netflix 办公室地址）排名了大量月量 1,000-6,600 的高频公司信息词，这是一套程序化 SEO 矩阵，用产品本身的数据驱动 SEO。虽然这些词与 Olares 叙事不直接相关，但其打法值得参考：Olares Market 可对每个上架应用建"X on Olares"安装教程程序化页面，复制同样的矩阵效应。

3. **对 Olares 最关键的三个词**：
   - `searxng api`（140，KD=20，CPC=$49.73）——全表 CPC 最高 + KD 极低，Olares 上运行的 SearXNG 天然可提供 API 端点，写一篇"How to use SearXNG as a Search API on Olares"即可承接。
   - `web search mcp`（210，KD=30）——MCP 工具生态快速崛起，SearXNG 有 MCP Server 实现，Olares 可做"自托管 MCP Search Server"方案，直接对位 Exa MCP。
   - `clearbit alternative`（210，KD=3，CPC=$18.21）——Exa Websets 在争夺公司数据富集市场，但这里有极低 KD 的替代词可切入，Olares 自托管开源 CRM/数据工具的叙事可嵌入其中。

4. **最大攻击面——每次调用都要付钱。** Exa 的定价虽有 Free tier，但 Search $7/1K、Deep Search $12-15/1K 的用量计费模式在 AI Agent 时代极具杀伤力——Agent 单次任务可能发起数百次搜索，成本快速堆叠。Olares 的叙事："本地 Agent + SearXNG（自托管，零 API 成本）= 无限搜索调用"是直击痛点的差异化。`web search api for llm`（KD=15，CPC=$16.67）这类词的搜索者正在评估成本方案，是最佳切入口。

5. **隐藏低 KD 金矿——Websets 带出的 B2B 数据替代词。** `clearbit alternative`（KD=3）、`b2b data api`（KD=12）、`contact enrichment api`（KD=10）、`hunter.io alternative`（KD=8）——这些词的 KD 极低但 CPC 很高（$10-18），是 Exa Websets 竞争的赛道意外漏出的机会词。即便 Olares 没有直接对应产品，也可用"自托管数据富集方案对比"内容覆盖。

6. **GEO 前瞻布局。** `exa alternative`（KD=0）、`search grounding`（KD=0）、`web search api for agents`（KD=0，CPC=$9.06）、`open source search api`（KD=0）、`llm web search`（KD=0）——这些词目前近零量，但随 AI Agent 普及将快速增长。建议提前发布"What is Grounding in LLMs（SearXNG on Olares 实战）"、"Open-source Exa Alternative: SearXNG + Firecrawl on Olares"等内容，抢 Perplexity/AI Overview 的引用位。

7. **与既有分析的关联。** 本报告补充了 `olares-500-keywords` 目前尚缺的"AI Agent 搜索工具"子品类。SearXNG 和 Firecrawl 报告（market/ 目录下已有）提供了大量具体词，本报告的新增高价值词（`clearbit alternative`、`b2b data api`、`searxng api`、`web search mcp`、`web search api for llm`）与 Agent 工具方向高度互补，建议合并进"AI Agent 联网工具"词簇统一规划。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / domain_organic_organic / phrase_these / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
