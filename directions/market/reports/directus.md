# Directus SEO 竞品分析报告

> 域名：directus.io | SEMrush US | 2026-07-06
> 可组合数据平台（Composable Data Platform）：兼做 Headless CMS、BaaS、Admin Panel，BSL 许可，可自托管

---

## 项目理解（前置）

Directus 是一个基于已有 SQL 数据库构建 Headless CMS、BaaS 和后台管理界面的开源（BSL）平台。用户连接自己的数据库（PostgreSQL、MySQL、SQLite 等），Directus 立刻自动生成 REST + GraphQL API 和一套无代码的可视化管理界面，无需迁移数据或改变 schema。v12 原生内置 MCP Server，可让 Claude Desktop、Cursor、ChatGPT 等 AI 工具直接操作数据库内容，是目前在"AI Agent 后端"赛道里卡位最积极的 Headless CMS。Directus 已在 **Olares Market** 上架。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 连任意数据库即得 REST/GraphQL API + Admin UI + MCP Server 的可组合后端 |
| 开源 / 许可证 | BSL (Business Source License) 1.1 → 4年后转 Apache-2.0；**不允许将其作为托管服务对外销售** |
| 主仓库 | [github.com/directus/directus](https://github.com/directus/directus)（★ 36,400+） |
| 核心功能 | 即时 REST + GraphQL API；无代码 Admin Studio；原生 MCP Server；Flows 自动化；数字资产管理（DAM）；WebSocket 实时推送 |
| 商业模式 / 定价 | 自托管免费（BSL）；Directus Cloud 按项目计费（Enterprise 联系询价）；OSS 补助计划（已发 1,000+ 免费 License Key） |
| 差异化 / 价值主张 | **不替换现有数据库**——schema 不迁移、不抽象、原始 SQL 完全暴露；内置 MCP Server 是同类中最早的原生支持 |
| 主要竞品（初判） | Strapi、Payload CMS、Sanity、Contentful、Prismic |
| Olares Market | **已上架** |
| 来源 | [directus.io](https://directus.io) · [github.com/directus/directus](https://github.com/directus/directus) · [directus.io/bsl](https://directus.io/bsl) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | directus.io |
| SEMrush Rank | 1,714,322 |
| 自然关键词数 | 794 |
| 月自然流量（US）| 464 |
| 自然流量估值 | $681/月 |
| 付费关键词数 | 0（不投 Google Ads） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 23 词 |
| 排名 4-10 位 | 91 词 |
| 排名 11-20 位 | 142 词 |

> **洞见**：794 个关键词、464 月流量——对于 36K+ star、45M+ 下载的项目而言 SEO 覆盖极薄。绝大多数流量来自品牌导航词（pricing/docs/sdk），非品牌信息词几乎没有布局。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| directus.io | 720 | 457 | 98.5% |
| datadash.directus.io | 6 | 4 | 0.9% |
| community.directus.io | 63 | 3 | 0.6% |
| docs.directus.io | 3 | 0 | 0.0% |
| trust.directus.io | 2 | 0 | 0.0% |

> **洞见**：docs.directus.io 独立部署却几乎零 SEO 流量，是巨大浪费——技术文档是最容易拿长尾词的来源，Directus 放弃了这块。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| directus pricing | 1 | 90 | 12 | $0 | 72 | 商业/交易 | /pricing |
| directus sdk | 1 | 70 | 29 | $0 | 56 | 信息/商业 | /docs/guides/connect/sdk |
| directus extensions | 1 | 50 | 18 | $0 | 40 | 信息/商业 | /extensions |
| directus docs | 1 | 50 | 29 | $0 | 40 | 信息/商业 | /docs |
| directus license | 1 | 50 | 30 | $0 | 40 | 信息/商业 | /bsl |
| agency os | 4 | 480 | 17 | $6.94 | 31 | 信息 | /blog/announcing-agencyos |
| directis (拼写变体) | 1 | 70 | 19 | $0.29 | 17 | 信息 | / |
| sql database relation kinds | 3 | 170 | 21 | $0 | 11 | 信息 | /blog/5-types-of-relationships… |
| directus headless cms | 2 | 70 | 12 | $0 | 9 | 信息/商业 | /blog/what-is-headless-cms |
| agencyos | 3 | 90 | 14 | $4.25 | 7 | 信息 | /blog/announcing-agencyos |
| backend as a service baas | 7 | 320 | 33 | $10.11 | 4 | 信息 | /blog/what-is-baas |
| backend as a service providers | 7 | 210 | 29 | $16.47 | 4 | 信息 | /blog/what-is-baas |
| open source cms | 11 | 1,000 | 53 | $4.12 | 3 | 信息 | / |
| directus docker | 2 | 110 | 28 | $0 | 2 | 信息 | /docs/self-hosting/deploying |
| directus api | 3 | 110 | 22 | $0 | 1 | 商业 | /features/graphql-apis |
| directus mcp | — | 70 | 9 | $0 | — | 商业 | — |

> **洞见**：非品牌词里最有流量的是 "agency os"（480 月量，排名 4，KD 17）——Directus 一篇博文无意中拦截了这个词。内容价值被低估。

### 付费词（Google Ads）

Directus 当前在 US 数据库中 **无付费投放**。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| contentful alternative | 140 | 11 | $19.34 | 信息/导航 | ⭐ KD 极低，高 CPC 表明买家意图 |
| strapi alternative | 70 | 8 | $6.68 | 信息/导航 | ⭐ Strapi 是 Directus 最近竞品 |
| directus vs strapi | 140 | 16 | $0 | 导航 | ⭐ 对比词量不小 |
| directus alternative | 30 | 5 | $5.53 | 导航/信息 | ⭐ KD=5，极易抢占 |
| sanity alternative | 20 | 0 | $8.92 | 信息 | ⭐ 量小但 KD=0 |
| directus vs contentful | 20 | 0 | $0 | 导航 | ⭐ KD=0 |
| self-hosted headless cms | 30 | 60 | $5.08 | 信息 | KD 偏高 |
| headless cms alternative | 10 | 0 | $0 | 信息 | 量小 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| headless cms | 6,600 | 67 | $16.20 | 信息/导航 | 大词，KD 高 |
| baas | 4,400 | 50 | $9.81 | 信息 | 多义词（银行/BaaS）噪音大 |
| open source cms | 1,000 | 53 | $4.12 | 信息 | KD 偏高 |
| best headless cms | 880 | 21 | $13.30 | 导航 | ⭐ 量大+KD 低，核心机会 |
| what is headless cms | 880 | 44 | $6.54 | 信息 | 教育词 |
| composable cms | 480 | 16 | $15.21 | 信息 | ⭐ Directus 定位词，KD 低 |
| backend as a service | 590 | 34 | $10.11 | 信息 | 中等难度 |
| headless cms comparison | 210 | 24 | $0 | 信息/导航 | ⭐ 比较意图 |
| api cms | 170 | 41 | $7.36 | 信息 | 中等 |
| react cms | 1,300 | 25 | $5.84 | 导航 | ⭐ 技术栈场景词 |
| nextjs cms | 720 | 29 | $4.60 | 导航 | ⭐ 技术栈场景词 |
| decoupled cms | 720 | 25 | $10.77 | 信息 | ⭐ 等同于 headless |
| headless architecture | 720 | 29 | $2.37 | 信息 | ⭐ 技术认知词 |
| headless cms pricing | 40 | 9 | $10.66 | 商业 | ⭐ 高 CPC 买家意图 |
| cms for developers | 70 | 16 | $16.25 | 导航 | ⭐ 精准开发者词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| directus cms | 320 | 27 | $6.69 | 商业 | ⭐ 主品牌词，KD 不高 |
| directus docker | 110 | 28 | $0 | 信息 | 安装场景 |
| directus api | 110 | 22 | $0 | 商业 | ⭐ 开发者意图 |
| directus pricing | 90 | 12 | $0 | 商业/交易 | ⭐ 已自然排名 #1 |
| directus cloud | 50 | 30 | $9.19 | 商业/交易 | 托管版 |
| directus license | 50 | 30 | $0 | 信息/商业 | BSL 争议入口词 |
| directus open source | 40 | 23 | $0 | 商业 | ⭐ |
| directus mcp | 70 | 9 | $0 | 商业 | ⭐ MCP 新词，KD=9 |
| directus headless cms | 70 | 12 | $0 | 信息/商业 | ⭐ |
| what is directus | 70 | 13 | $0 | 信息 | ⭐ |
| api-first cms | 70 | 28 | $0 | 信息 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source headless cms | 590 | 80 | $5.29 | 信息 | 量大但 KD=80，极难 |
| open source backend as a service | 30 | 0 | $0 | 信息 | ⭐ KD=0，GEO 前哨 |
| self-hosted backend as a service | 20 | 0 | $0 | 信息 | ⭐ KD=0，GEO 前哨 |
| open source baas | 20 | 0 | $0 | 信息 | ⭐ KD=0 |
| self hosted baas | 20 | 0 | $0 | 信息 | ⭐ KD=0 |
| headless cms self hosted | 50 | 35 | $5.08 | 信息 | 中等 |
| strapi self hosted | 30 | 30 | $3.98 | 商业/交易 | 竞品自托管词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Directus 自身 SEO 极薄、BSL 许可争议多——Olares Market 直接提供一键部署 Directus，可在对比词、自托管词、MCP/AI Agent 场景词上抢位。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| best headless cms | 880 | 21 | $13.30 | ⭐⭐⭐ 高量低 KD；Olares Market 同时有 Directus + 多个替代品（Strapi 等），可写"best self-hosted headless CMS"榜单，Olares 一键部署是差异化 |
| directus alternative | 30 | 5 | $5.53 | ⭐⭐⭐ KD=5 极易抢占；用户寻找替代=考虑迁移，Olares 可列出 Market 内同类工具（Strapi/AppFlowy 等） |
| contentful alternative | 140 | 11 | $19.34 | ⭐⭐⭐ 高 CPC 商业意图；Directus 作为 Contentful 平替已在 Olares Market 上架，是直接内容卡位机会 |
| strapi alternative | 70 | 8 | $6.68 | ⭐⭐ 两者都在 Olares Market，可写"strapi vs directus self-hosted"对比 |
| directus vs strapi | 140 | 16 | $0 | ⭐⭐ 对比意图，量较大；两者均可 Olares 一键部署是核心亮点 |
| composable cms | 480 | 16 | $15.21 | ⭐⭐ 量大 KD 低；Directus 自身定位词，Olares 的"可组合应用生态"叙事与之完全吻合 |
| directus mcp | 70 | 9 | $0 | ⭐⭐⭐ MCP 新词 KD=9；Olares 本身 Agent-Native OS + Directus 内置 MCP Server，可写"run Directus MCP server on Olares"教程 |
| headless cms comparison | 210 | 24 | $0 | ⭐⭐ 比较意图低 KD；Olares 可做 CMS 品类比较页，推 Market 直接部署 |
| open source backend as a service | 30 | 0 | $0 | ⭐⭐ GEO 前哨；Directus = open source BaaS，Olares Market 提供部署 |
| api-first cms | 70 | 28 | $0 | ⭐ 技术用户词；Olares 上 Directus 是最典型的 API-first 后端 |
| cms for developers | 70 | 16 | $16.25 | ⭐⭐ 高 CPC 精准词；Directus on Olares 是开发者自托管首选路径 |
| self hosted baas | 20 | 0 | $0 | ⭐ GEO 前哨；Olares = self-hosted baas 基础设施 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| best headless cms | 880 | 21 | $13.30 | 导航/商业 | **主词候选** | 量大 KD 低，高 CPC 商业意图；Olares Market 可做"best self-hosted headless CMS"榜单，Directus + Strapi 均上架 |
| composable cms | 480 | 16 | $15.21 | 信息 | **主词候选** | Directus 自己的品类定位词，量合理 KD 低；Olares 的可组合应用叙事天然契合 |
| contentful alternative | 140 | 11 | $19.34 | 信息/商业 | **主词候选** | 高 CPC 买家意图，KD 超低；Directus 是 Contentful 头号平替，Olares 一键部署 |
| directus vs strapi | 140 | 16 | $0 | 导航 | **主词候选** | 量较大 KD 低；双方均在 Olares Market，对比文是天然落地页 |
| strapi alternative | 70 | 8 | $6.68 | 信息/商业 | **主词候选** | KD=8 极易；Directus 是 Strapi 最常被提及的替代品 |
| directus mcp | 70 | 9 | $0 | 商业 | **主词候选** | 新兴词 KD=9，AI Agent 场景；Directus MCP Server + Olares Agent-Native OS 完美组合 |
| headless cms comparison | 210 | 24 | $0 | 信息/导航 | **主词候选** | 量中等 KD 低；品类比较页型内容，Olares Market 多品牌横比 |
| react cms | 1,300 | 25 | $5.84 | 导航 | **主词候选** | 量大 KD 适中；技术栈组合词，Directus + React 是主流，Olares 可做集成教程 |
| directus alternative | 30 | 5 | $5.53 | 信息/商业 | **主词候选** | KD=5 最低竞争；可与 Olares Market 替代品合页 |
| directus cms | 320 | 27 | $6.69 | 商业 | 次级 | 品牌词，已有自然流量；Olares Market 落地页可补充 |
| decoupled cms | 720 | 25 | $10.77 | 信息 | 次级 | 等同 headless，量大；技术认知内容 |
| headless cms pricing | 40 | 9 | $10.66 | 商业 | 次级 | 高 CPC 低 KD，价格比较意图；Directus 自托管免费 vs Cloud 是卖点 |
| directus headless cms | 70 | 12 | $0 | 信息/商业 | 次级 | KD 低，Directus 品类认知词 |
| cms for developers | 70 | 16 | $16.25 | 导航 | 次级 | 高 CPC 精准开发者词 |
| open source backend as a service | 30 | 0 | $0 | 信息 | **GEO** | KD=0 近零量；语义完全精准，抢 AI Overview 引用位 |
| self hosted baas | 20 | 0 | $0 | 信息 | **GEO** | 同上，Olares 的"self-hosted 全栈"叙事完全覆盖 |
| directus mcp server | 0 | — | — | — | **GEO** | 近零量新词；AI Agent 搜索激增，先发占位 |
| self-hosted headless cms with mcp | 0 | — | — | — | **GEO** | 预判词；Olares + Directus MCP 的精准 GEO 卡位 |

---

## 核心洞见

1. **品牌护城河**：Directus 品牌词 KD 全部 ≤30（pricing=12、headless cms=12、cms=27），**没有真正的护城河**，内容干预可直接竞争。品牌词带来的绝大多数流量是已有用户的导航行为（pricing/docs/sdk 占 ~45% 流量），新用户发现路径几乎为零。

2. **可复制的打法**：Directus 有一篇 "AgencyOS" 博文意外截住了 "agency os"（480 月量）——它们的博客每篇都像是随机押宝。真正的机会在**系统性技术博客 + 对比落地页**（`/blog/what-is-baas` 已排 7 位拿到 BaaS 流量），Olares 可在同一意图词上做更完整的自托管叙事。`docs.directus.io` 的独立子域名流量为零，说明他们没有系统做文档 SEO——这是巨大缺口。

3. **对 Olares 最关键的词**：
   - **`best headless cms`**（880 月量 / KD 21）：量最大、KD 合理、商业意图明确，Olares Market 有多个 headless CMS 可一键部署
   - **`contentful alternative`**（140 月量 / KD 11 / CPC $19.34）：买家意图最强、KD 极低，Directus 是 Contentful 最直接平替
   - **`directus mcp`**（70 月量 / KD 9）：新兴词，AI Agent 时代的 MCP 场景，Olares Agent-Native OS 叙事核心

4. **最大攻击面**：**BSL 许可争议**——"directus license"（50 月量）直接指向 `/bsl` 页，说明用户对许可证有疑虑。BSL 禁止将 Directus 作为托管服务销售（这正是 Directus Cloud 的壁垒），但对个人自托管完全免费。Olares 的叙事：个人自托管 Directus = 完全合法 + 无限制 + 数据自有，直接击穿 BSL 焦虑。此外 "directus pricing"（90 月量 / KD 12）排第一，说明价格透明度是用户痛点。

5. **隐藏低 KD 金矿**：
   - `composable cms`（480 月量 / KD 16 / CPC $15.21）：高量低 KD，Directus 自己的定位词却没把 SEO 做好
   - `headless cms pricing`（40 月量 / KD 9）：高 CPC 低 KD，价格比较意图明确
   - `directus vs strapi`（140 月量 / KD 16）：量大低 KD，两者均在 Olares Market
   - `cms for developers`（70 月量 / KD 16 / CPC $16.25）：精准词高 CPC

6. **GEO 前瞻布局**：以下词在 AI Overview / Perplexity 的引用位竞争开始前布局：
   - "self-hosted headless cms with mcp server"
   - "open source backend as a service self-hosted"
   - "run directus on your own server with ai agent"
   - "directus mcp server setup"
   - "composable cms for ai agents"

7. **与既有分析的关联**：`headless cms`（6,600 月量）和 `open source cms`（1,000 月量）在 `olares-500-keywords` 词表中应有覆盖，但 KD 分别为 67 和 53，短期难以主攻。更现实的路径：从 `best headless cms`（KD 21）和品类 + 自托管组合词切入，借助 Olares Market 的多品牌覆盖做品类内容，而不是正面强攻单一大词。Directus 本身流量极薄（464 US/月）说明这个市场的内容供给不足——这正是 Olares 的内容机会。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
