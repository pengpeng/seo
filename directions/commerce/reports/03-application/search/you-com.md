# You.com SEO 竞品分析报告（Search 维度）

> 域名：you.com | SEMrush US | 2026-07-06
> You.com = AI 搜索引擎 + 企业 AI 平台（ARR $50M+，估值 $1.5B），旗下 YouChat 是隐私优先、多模型、多 Agent 的 AI 搜索产品，B2B 核心护城河是 Search API（服务 DuckDuckGo、Windsurf、Harvey 等）
>
> **⚠️ 注意**：You.com 旗下 ARI 深度研究 Agent 的报告已单独收录于 [`general-agent/ari.md`](../../general-agent/ari.md)。本报告聚焦 **Search 产品维度**：YouChat 消费者搜索、隐私搜索、Search API、以及对 Olares Market 上 Vane（前 Perplexica）+ SearXNG 的开源平替视角。

---

## 项目理解（前置）

You.com 于 2021 年 11 月由斯坦福 NLP 学者 Richard Socher 与 Bryan McCann 创立，最初以"不追踪用户的 AI 搜索引擎"切入市场，与 Perplexity、Brave Search 等同属第一批 AI 搜索新星。其核心差异化不在于自建索引（底层依赖 Bing、Google、Brave 的搜索 API），而在于**多模型切换**（可选 GPT-4、Claude、Gemini 等）+ **多 Agent 工作台**（Research / Code / Write / Image 30+ Agent）+ **隐私承诺**（Zero Data Retention，无广告定向）。随着 AI 搜索赛道竞争加剧，You.com 于 2024-2025 年明显向 B2B/Developer 转型，Search API 成为主要护城河——DuckDuckGo 将其 AI 搜索能力构建在 You.com API 之上，月查询量超 10 亿次。2025 年 9 月 $100M Series C 融资（估值 $1.5B），确认了「AI 搜索基础设施提供商」的新定位。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 隐私优先、多模型 AI 搜索引擎 + 企业 Search API 基础设施 |
| 开源 / 许可证 | **闭源，Proprietary**（底层 Search API 付费开放调用） |
| 主仓库 | 无公开 GitHub（消费端产品在 you.com；API 文档在 you.com/docs/welcome）|
| 核心功能 | YouChat（多模型对话搜索）、多 Agent 工作台（Research/Code/Write/Image）、Web Search API、Contents API、Finance Research API、Zero Data Retention |
| 商业模式 / 定价 | Free → Pro（~$20/月）→ Team（$25/seat/月，按年）→ Enterprise（自定义）；API：Web Search $5/1000 calls，Contents $1/1000 pages，Research API 按调用量计 |
| 差异化 / 价值主张 | 1. 隐私承诺（无广告定向）2. 多模型切换（不绑定单一 LLM）3. 搜索 + 生产力一体工作台 4. B2B API 生态（DuckDuckGo/Windsurf 已集成）|
| 主要竞品（初判）| Perplexity AI、Brave Search、Kagi、ChatGPT Search、Google AI Mode |
| Olares Market | **未上架**（闭源 SaaS）；开源平替：**Vane（前 Perplexica）✅ 已上架**、**SearXNG ✅ 已上架** |
| 来源 | [you.com](https://you.com)、[Series C 公告](https://you.com/resources/series-c)、[Series B 公告](https://you.com/resources/50m-series-b)、[The New Stack 报道](https://thenewstack.io/how-you-com-survived-chatgpt-with-a-pivot-to-enterprise-ai/)、[Perplexity vs You.com 2026 对比](https://perplexityaimagazine.com/perplexity-hub/perplexity-vs-you-com-ai-search-comparison-2026/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | you.com |
| SEMrush Rank | **37,163**（与 Perplexity 的 1,121 差距 30 倍；Search SEO 显著落后于估值）|
| 自然关键词数 | 2,319 |
| 月自然流量（US）| 56,773 |
| 自然流量估值 | $41,311/月 |
| 付费关键词数 | 157 |
| 月付费流量 | 15,081 |
| 月付费成本 | $32,814 |
| 排名 1-3 位 | 159 词 |
| 排名 4-10 位 | 372 词 |
| 排名 11-20 位 | 371 词 |

> **结构性洞察**：You.com 的 SEMrush Rank 37,163 与 $1.5B 估值严重脱节。自然流量中约 **65%+ 来自「you」系列误触/误拼词**（KD=100，无法主动争取），真正搜索引擎类意图词流量极少。这侧面印证了 You.com 的商业路径以 B2B API 销售为主，SEO 并非核心获客渠道。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| you.com（主站） | 2,176 | 56,681 | 99.84% |
| home.you.com | 99 | 72 | 0.13% |
| support.you.com | 35 | 12 | 0.02% |
| about.you.com | 4 | 8 | 0.01% |
| imgs.you.com | 4 | 0 | — |
| learn.you.com | 1 | 0 | — |

> 子域名几乎无独立 SEO 贡献，全站 SEO 集中在主站；`learn.you.com` 虽有内容但几乎无自然流量，教程 SEO 尚未成型。

### 官网 TOP 自然关键词（按流量排序，聚焦 Search 维度）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| you（误触） | 6 | 6,120,000 | 100 | $0.01 | 36,720 | 导航(误触) | / |
| you.com | 1 | 2,900 | 75 | $4.49 | 2,320 | 品牌 | / |
| you com | 1 | 2,400 | 69 | $4.49 | 1,920 | 品牌 | / |
| you（signin） | 18 | 6,120,000 | 100 | $0.01 | 1,836 | 导航 | /signin |
| you' | 6 | 135,000 | 100 | $0.01 | 810 | 误触 | / |
| you .com | 1 | 1,000 | 74 | $2.31 | 800 | 品牌 | / |
| you.ai | 1 | 590 | 84 | $3.09 | 472 | 品牌 | / |
| **you.com api** | **1** | **480** | **30** | **$0.00** | **384** | 商业/开发者 | /docs/welcome |
| you con | 1 | 320 | 62 | $4.20 | 256 | 误拼 | / |
| you char | 2 | 1,900 | 41 | $0.00 | 250 | 信息 | / |
| **you chat** | **1** | **880** | **54** | **$1.67** | **218** | 功能/信息 | /?chatMode=default |
| **youchat** | **1** | **1,600** | **47** | **$2.56** | **211** | 品牌/功能 | /?chatMode=default |
| you ia | 1 | 260 | 64 | $4.23 | 208 | 品牌 | / |
| **you.com student discount** | **1** | **170** | **18** | **$0.00** | **136** | 商业 | /pricing |
| **you search** | **1** | **170** | **47** | **$0.00** | **136** | 导航/品牌 | / |
| youai | 1 | 480 | 28 | $3.24 | 119 | 品牌 | /?chatMode=default |
| youcom | 1 | 4,400 | 52 | $4.49 | 114 | 品牌 | / |
| ai site | 2 | 3,600 | 87 | $2.32 | 108 | 信息 | / |
| you.com funding | 1 | 90 | 40 | $0.00 | 72 | 信息 | /resources/series-c |
| **you search engine** | **1** | **110** | **41** | **$3.35** | **88** | 品牌/信息 | / |
| you.com com careers | 1 | 90 | 17 | $0.00 | 72 | 信息 | /careers |

> **Search 维度发现**：自然词中与搜索产品直接相关的词极少且量小：`youchat`（1600，KD 47）、`you chat`（880，KD 54）是 You.com 搜索/对话产品最有辨识度的词；`you.com api`（480，KD 30）是唯一兼具量与低 KD 的高价值词；`you.com student discount`（KD 18）是最低竞争定价词。与 Perplexity 相比，You.com 在 AI 搜索品类词（ai search engine、best ai search engine）上几乎无自然排名，说明其搜索产品 SEO 内容体系完全未建设。

### 付费词（Google Ads，按流量排序）

You.com 的付费策略核心是**截流 AI 工具 API 开发者**，主要投竞品搜索 API 词，将流量导向 `/docs/welcome` 文档页，目标受众是寻找替代搜索/数据 API 的开发者。

| 关键词 | 排名 | 月量 | CPC | 流量 | 落地页 |
|--------|------|------|-----|------|--------|
| deep seek | 1 | 135,000 | $1.57 | 6,345 | /docs/welcome |
| deepseek ai | 1 | 60,500 | $1.31 | 2,843 | / |
| brave search engine | 1 | 14,800 | $2.65 | 695 | /docs/welcome |
| deepsearch | 1 | 14,800 | $0.79 | 695 | /docs/welcome |
| deepsearch ai | 1 | 8,100 | $1.18 | 380 | /docs/welcome |
| deepseek-v3 | 1 | 5,400 | $6.03 | 253 | / |
| brave search api | 1 | 4,400 | $1.75 | 206 | /docs/welcome |
| web scraping python | 1 | 3,600 | $1.75 | 169 | /docs/welcome |
| tavily | 2 | 9,900 | $3.60 | 128 | /docs/welcome |
| exa | 2 | 9,900 | $3.22 | 128 | / |
| brave api | 1 | 2,900 | $1.61 | 136 | /docs/welcome |
| serpapi | 3 | 9,900 | $3.07 | 89 | / |
| **perplexity.ai api** | **1** | **1,900** | **$8.09** | **89** | /docs/welcome |
| **gpt-5 api** | **1** | **1,900** | **$30.94** | **89** | / |
| **perplexity api** | **2-3** | **5,400** | **$6.80–11.94** | **70–89** | /docs/welcome |

> **付费策略洞察**：1. You.com 花最多预算截流的是 DeepSeek 系词（合计 ~$0.7/click 的 AI 爆红流量），性价比极高；2. `brave search engine`（$2.65）被投放到 /docs/welcome，说明 You.com 把 Brave Search 视为搜索 API 的直接竞争者；3. `perplexity api`（CPC $8.09-11.94）和 `gpt-5 api`（$30.94）是本赛道高价值 B2B 词，You.com 正在激进抢占这类开发者流量；4. `tavily`（$3.60）和 `exa`（$3.22）说明 You.com 把自己定位为 AI Agent 搜索基础设施替代方。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| brave search engine | 18,100 | 69 | $0.38 | 信息/导航 | 强竞品品牌词，难进；You.com 已投付费 |
| kagi search | 2,900 | 73 | $0.00 | 导航 | 高端付费搜索竞品 |
| duckduckgo alternative | 720 | 38 | $3.00 | 商业 | 中 KD，量不错，You.com API 是 DDG 后台 |
| alternative to google search | 320 | 36 | $0.95 | 商业 | ⭐ KD 36，有搜索平替意图 |
| google search alternative | 320 | 49 | $0.95 | 商业 | 同上，稍难 |
| perplexity alternative | 90 | **11** | $2.83 | 商业 | ⭐⭐ **KD=11 极低**，Olares Vane+SearXNG 直接攻占 |
| perplexity alternative open source | 20 | **0** | $0.00 | 商业 | ⭐ 完全空白，开源替代词 |
| open source perplexity alternative | 20 | **0** | $0.00 | 商业 | ⭐ 同上变体 |
| perplexica alternative | 20 | **0** | $0.00 | 信息 | ⭐ Vane 关联词，KD=0 |
| searxng alternative | 20 | **0** | $0.00 | 信息 | ⭐ SearXNG 关联词，KD=0 |
| you.com alternative | 10 | **0** | $0.00 | 商业 | ⭐ KD=0，战略占位词 |
| you.com vs perplexity | 10 | **0** | $0.00 | 商业 | ⭐ KD=0，对比词 |
| brave search alternative | 10 | **0** | $0.00 | 商业 | ⭐ KD=0 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai search engine | 12,100 | **78** | $1.48 | 信息/商业 | 品类最大词，KD 太高，作次级 |
| private search engine | 6,600 | 69 | $1.11 | 信息 | 隐私搜索品类词，竞争激烈 |
| best ai search engine | 1,600 | 49 | $2.07 | 商业 | ⭐ KD 49，商业意图，Olares 清单文可做 |
| ai search engine free | 1,300 | 47 | $1.16 | 商业 | ⭐ KD 47，免费平替意图 |
| kagi search | 2,900 | 73 | $0.00 | 导航 | 竞品品牌 |
| ai powered search | 1,000 | 55 | $4.22 | 信息 | 高 CPC，B2B 信号 |
| perplexica | 1,000 | **28** | $5.37 | 信息 | ⭐⭐ KD=28，Olares Market 应用词！Vane |
| privacy search engine | 480 | 63 | $0.81 | 信息 | 较难 |
| ai web search | 320 | 63 | $2.36 | 商业 | 较难 |
| open source search engine | 390 | 61 | $2.08 | 信息 | 较难，但 Olares 叙事可用 |
| self hosted search engine | 110 | **32** | $0.00 | 信息 | ⭐ KD=32，自托管场景，Olares 核心词 |
| best ai search | 140 | 43 | $2.15 | 商业 | 中 KD，商业意图 |
| duckduckgo alternative | 720 | 38 | $3.00 | 商业 | 隐私搜索切换意图 |
| search without google | 20 | **0** | $0.00 | 商业 | ⭐ 完全空白，Olares 叙事词 |
| ai search no tracking | 0 | 0 | — | 商业 | GEO 词（量零，语义精准）|

### 产品 / 功能词（you.com 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| youchat | 1,600 | 47 | $2.56 | 品牌/功能 | You.com 搜索对话产品标志词 |
| you.com api | 480 | **30** | $0.00 | 商业/开发者 | ⭐ KD=30，开发者 API 词，Olares 叙事：搭建私有 Search API |
| youai | 480 | **28** | $3.24 | 品牌 | ⭐ KD=28，低竞争品牌词 |
| you.com search | 40 | 39 | $0.00 | 品牌 | 搜索产品直达词 |
| you.com pricing | 10 | **23** | $0.00 | 商业 | ⭐ KD=23，定价对比词 |
| you.com review | 10 | 35 | $0.00 | 信息 | 低 KD 评测词 |
| you.com search engine | 10 | 0 | $0.00 | 品牌 | ⭐ KD=0，完全空白 |
| you.com search api | 10 | 0 | $0.00 | 商业 | ⭐ 开发者词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| searxng | 8,100 | 64 | $1.67 | 信息 | Olares Market 已上架，量大但 KD 高 |
| perplexica | 1,000 | **28** | $5.37 | 信息 | ⭐⭐ Olares Market 应用（Vane），KD 极低，CPC 高！ |
| open source search engine | 390 | 61 | $2.08 | 信息 | 较难攻 |
| self hosted search engine | 110 | **32** | $0.00 | 信息 | ⭐ Olares 核心词 |
| open source ai search | 20 | **0** | $1.73 | 信息 | ⭐ 完全空白，但有 CPC 说明有商业价值 |
| perplexity alternative open source | 20 | **0** | $0.00 | 商业 | ⭐ 完全无竞争 |
| self hosted perplexity | 10 | **0** | $0.00 | 信息 | ⭐ GEO 词，核心叙事词 |
| self hosted ai search | 0 | 0 | — | 信息 | GEO 词（量近零，语义完美）|

### API / 开发者词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| search api | 1,300 | 59 | **$51.62** | 商业 | CPC 超高，开发者买词刚需 |
| web search api | 320 | 54 | **$14.47** | 商业 | 高 CPC，B2B |
| ai search api | 90 | **39** | **$15.56** | 商业 | ⭐ KD 39，CPC $15，开发者词 |
| llm search api | 30 | **27** | $4.57 | 商业 | ⭐ KD=27 低，LLM 搜索 API 新词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：You.com 是闭源云端 SaaS 搜索，承诺"Zero Data Retention"但数据仍流经其服务器，广告商业模式天然限制了真正的隐私性；Vane（前 Perplexica）+ SearXNG 在 Olares 上实现"本地 AI 搜索：搜索过程不出机器、数据无法被第三方收集、模型可接 Ollama 本地跑"——主打隐私不打折 + 开源零订阅费用两连击。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|------|
| perplexica | 1,000 | 28 | $5.37 | ⭐⭐⭐ Olares Market 已有 Vane（前 Perplexica），一键安装开源 AI 搜索；KD 极低，CPC 高说明商业价值大 | ⭐⭐⭐ |
| best ai search engine | 1,600 | 49 | $2.07 | ⭐⭐ 「Best open-source AI search engine on Olares」清单内容，Vane+SearXNG 双双上榜 | ⭐⭐⭐ |
| ai search engine free | 1,300 | 47 | $1.16 | ⭐⭐ 免费版 You.com 有限制；Vane+SearXNG = 真免费（自托管），Olares 叙事切入 | ⭐⭐ |
| perplexity alternative | 90 | **11** | $2.83 | ⭐⭐⭐ KD=11 极低，Vane（Perplexica）是最知名的"开源 Perplexity 平替"，Olares 一键部署 | ⭐⭐⭐ |
| self hosted search engine | 110 | 32 | $0.00 | ⭐⭐⭐ Olares 核心叙事词：SearXNG 是 Olares 官方市场上架的自托管搜索引擎 | ⭐⭐⭐ |
| searxng | 8,100 | 64 | $1.67 | ⭐⭐ Olares Market 已上架，量大（全球约 25k-40k 月量）；KD 高但 Olares 教程/集成文章可攻长尾 | ⭐⭐ |
| duckduckgo alternative | 720 | 38 | $3.00 | ⭐⭐ 隐私搜索切换者；Olares+SearXNG = 比 DDG 更彻底的隐私（本地跑，无任何第三方）| ⭐⭐ |
| alternative to google search | 320 | 36 | $0.95 | ⭐⭐ 自托管搜索文内次级词；Olares 可做「真正不依赖 Google 的搜索方案」叙事 | ⭐⭐ |
| you.com alternative | 10 | **0** | $0.00 | ⭐⭐⭐ KD=0，完全空白；Vane+SearXNG on Olares = You.com 完整私有化替代，立即占位 | ⭐⭐⭐ |
| open source ai search | 20 | **0** | $1.73 | ⭐⭐⭐ 完全无竞争，有 CPC（$1.73）说明有商业价值；Olares 核心叙事词，立即占位 | ⭐⭐⭐ |
| perplexity alternative open source | 20 | **0** | $0.00 | ⭐⭐⭐ KD=0，直接对应 Vane 是 Perplexica 的分支，Olares 叙事最精准 | ⭐⭐⭐ |
| self hosted perplexity | 10 | **0** | $0.00 | ⭐⭐⭐ GEO 词，语义完美；Vane on Olares = self-hosted Perplexity | ⭐⭐⭐ |
| you.com search engine | 10 | **0** | $0.00 | ⭐⭐ KD=0，You.com 自己都没占此词，可布局「you.com search engine alternative」 | ⭐⭐ |
| search without google | 20 | **0** | $0.00 | ⭐⭐ GEO 词，Olares+SearXNG 可接多搜索引擎（Bing/Brave/DDG）而不依赖 Google | ⭐⭐ |
| self hosted ai search | 0 | 0 | — | ⭐⭐⭐ GEO 词，语义完美，AI Overview/Perplexity 回答此类问题时，Olares 应是首引 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| **perplexica** | **1,000** | **28** | **$5.37** | 信息 | **主词候选** | ⭐⭐ KD=28，量 1000，CPC $5.37；Olares Market 有 Vane（前 Perplexica），写安装教程/Vane review 可直接命中 |
| best ai search engine | 1,600 | 49 | $2.07 | 商业 | 次级 | 品类大词，KD 49 中等，作「best open-source AI search」清单次级词，列入 Vane/SearXNG |
| ai search engine free | 1,300 | 47 | $1.16 | 商业 | 次级 | 免费意图，Vane+SearXNG 是真免费（自托管），可作相关文章次级词 |
| **perplexity alternative** | **90** | **11** | **$2.83** | 商业 | **主词候选** | ⭐⭐ KD=11 极低！Vane 是最对位的开源 Perplexity 平替，Olares 一键部署，可单篇出文 |
| duckduckgo alternative | 720 | 38 | $3.00 | 商业 | 次级 | 隐私搜索切换意图；与 self-hosted 搜索文联动，作次级词 |
| alternative to google search | 320 | 36 | $0.95 | 商业 | 次级 | 隐私搜索叙事的次级词；与 SearXNG on Olares 文章联动 |
| **self hosted search engine** | **110** | **32** | **$0.00** | 信息 | **主词候选** | ⭐ KD=32，量 110，Olares + SearXNG 最直接落地词，可单独建一篇 |
| you.com api | 480 | 30 | $0.00 | 商业 | 次级 | 开发者词，KD=30；配合「build your own search API with SearXNG」叙事 |
| youai | 480 | 28 | $3.24 | 品牌 | 次级 | KD=28，You.com 品牌词，作 you.com alternative 文章次级词 |
| **perplexica alternative** | **20** | **0** | **$0.00** | 商业 | **主词候选** | KD=0，量虽小但语义精准；GEO 布局，且随 Vane 知名度上升量会增长 |
| **open source ai search** | **20** | **0** | **$1.73** | 信息 | **主词候选** | ⭐ KD=0，有 CPC（$1.73 说明有商业价值）；Olares 核心叙事词，立即占位 |
| **perplexity alternative open source** | **20** | **0** | **$0.00** | 商业 | **主词候选** | KD=0，与「perplexity alternative」可同篇，Vane 是答案 |
| open source search engine | 390 | 61 | $2.08 | 信息 | 次级 | KD 61 较难，作开源搜索综述文次级词 |
| you.com pricing | 10 | 23 | $0.00 | 商业 | 次级 | ⭐ KD=23，定价对比词，与「you.com alternative」联动 |
| you.com alternative | 10 | **0** | $0.00 | 商业 | 次级 | KD=0，量小；与 perplexica、Vane 叙事捆绑作次级词 |
| you.com search engine | 10 | **0** | $0.00 | 品牌 | 次级 | KD=0，搜索维度品牌词，You.com 自己都没占 |
| self hosted perplexity | 10 | **0** | $0.00 | 信息 | GEO | 语义极准，量接近零；提前布局，等 Vane 知名度起来收流量 |
| self hosted ai search | 0 | 0 | — | 信息 | GEO | 量零，语义完美；抢 AI Overview/Perplexity 引用位 |
| search without google | 20 | **0** | $0.00 | 商业 | GEO | 隐私搜索前瞻词，Olares+SearXNG 叙事贴合 |
| open source perplexity alternative | 20 | **0** | $0.00 | 商业 | GEO | 与 perplexity alternative open source 合并，GEO 布局 |

---

## 核心洞见

1. **品牌护城河：You.com 搜索端 SEO 几乎是白纸，与其 B2B API 护城河完全脱节。** SEMrush Rank 37,163 vs Perplexity 的 1,121；自然关键词 2,319 条，65%+ 是「you」这个字的误触导流——You.com 作为搜索引擎在 SEO 层面**几乎不存在**。搜索产品相关词里，KD 低于 50 且月量过百的词只有 `youchat`（1600，KD 47）和 `you.com api`（480，KD 30），真正的品类词（ai search engine、best ai search engine）一个排名也没进前 100。这意味着 Olares 可以在 You.com Search 相关词上零压力竞争占位。

2. **You.com 真实打法：付费截流 API 开发者，不靠搜索内容 SEO。** 付费端用 $1.57/click 买「deep seek」（13.5 万月量）、$8.09 买「perplexity.ai api」、$30.94 买「gpt-5 api」——全部打向 `/docs/welcome` 文档页，目标是 AI 开发者而非普通搜索用户。其 SEO 内容没有针对「ai search engine」相关词建立任何生产规模，几乎把搜索 SEO 市场拱手相让。

3. **对 Olares 最关键的词：`perplexity alternative`（KD=11）、`perplexica`（KD=28）、`self hosted search engine`（KD=32）。** 三个词都与 Olares Market 已上架的 Vane（前 Perplexica）+ SearXNG 直接对应，KD 低、商业意图明确、CPC 偏高（说明 B2B 价值）。尤其 `perplexity alternative`（90 量，KD=11）是本赛道最优质的单词主词候选——Vane on Olares = 答案。

4. **最大攻击面：隐私承诺不可验证 + 定价不透明。** You.com 的"Zero Data Retention"是云端 SaaS 的承诺，数据仍流经其服务器；Team/Enterprise 定价不透明（custom）且按 seat 计费贵。Olares 叙事完全反向：**Vane + SearXNG 在本地跑，搜索日志从未离开用户设备，不存在"承诺"只有"不可能泄露"；订阅费 $0（一次性硬件 + 电费）**。这个叙事在 `privacy search engine`、`self hosted search engine`、`search without google` 等词上最有杀伤力。

5. **隐藏低 KD 金矿：全部是开源/自托管维度的词。** `you.com alternative`（KD=0）、`open source ai search`（KD=0，但有 CPC $1.73）、`perplexity alternative open source`（KD=0）、`self hosted perplexity`（KD=0）、`you.com search engine`（KD=0）——You.com 自己连品牌词都没认真建设 SEO 内容，Olares 可以在这些词上以极低成本全线占位。

6. **GEO 前瞻布局词（近零量语义精准，抢 AI Overview / Perplexity 引用位）：** `self hosted ai search`、`self hosted perplexity alternative`、`open source you.com alternative`、`vane ai search`、`perplexica on olares`、`ai search without tracking`。这些词目前几乎零搜索量，但当 AI 搜索用户在 Perplexity/ChatGPT 里问"隐私 AI 搜索有什么开源替代"时，结构化内容能被引用。Vane + SearXNG 组合是最完整的 self-hosted AI search stack 答案。

7. **与既有分析的关联：** 本报告与 ARI 报告形成 You.com 全貌（ARI = 企业深度研究 Agent 维度；本报告 = Search 消费者/API 维度）。`searxng`（8100，KD 64）在 SearXNG 自身的 market reports 中已有详细分析；`perplexica` 词对应 Vane 应用报告（建议补跑 `vane.md`）。与 `olares-500-keywords` 的关联：500 词表缺乏「self-hosted search engine」维度，本报告的 `perplexity alternative`（KD=11）+ `perplexica`（KD=28）+ `self hosted search engine`（KD=32）可作为补充候选词，填补隐私/自托管搜索这一空白分支。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these（4 批次，含 you.com 品牌词、AI 搜索品类词、开源/自托管词、API/开发者词）| phrase_related（ai search engine 扩展词））| 2026-07-06*
*项目理解来源：[you.com](https://you.com)、[Series C 公告](https://you.com/resources/series-c)、[Series B 公告](https://you.com/resources/50m-series-b)、[The New Stack](https://thenewstack.io/how-you-com-survived-chatgpt-with-a-pivot-to-enterprise-ai/)、[perplexityaimagazine.com You.com 对比](https://perplexityaimagazine.com/perplexity-hub/perplexity-vs-you-com-ai-search-comparison-2026/)*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
