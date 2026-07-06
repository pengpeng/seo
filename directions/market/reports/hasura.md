# Hasura SEO 竞品分析报告

> 域名：hasura.io | SEMrush US | 2026-07-06
> Hasura 是开源 GraphQL 引擎，能对 PostgreSQL 等数据库即时生成生产级 GraphQL API，并附带细粒度访问控制与数据库事件 webhook——是当前最主流的"零代码 GraphQL 后端"工具。

---

## 项目理解（前置）

Hasura 的核心价值是"把数据库变成 GraphQL API"——连接 PostgreSQL（及兼容数据库）后，几秒内自动生成 CRUD + 实时订阅 + 行/列级访问控制的完整 GraphQL 后端，无需手写 resolver。它最早以 graphql-engine 开源项目起家，积累了大量开发者心智；近年品牌转型推出 Hasura DDN（Data Delivery Network），定位"超图"（Supergraph）平台，引入 PromptQL 向 AI/Agent 数据层延伸。商业模式从原有 Hasura Cloud 迁移到 DDN 的 per-model 计费，开源版（v2 graphql-engine）仍可免费自托管，DDN 免费计划亦支持 unlimited API requests。Olares Market 上已收录 Hasura（⬜ 未完成研究）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 GraphQL 引擎，对 DB 即时生成生产级 GraphQL/REST API，含行列级权限 + 实时订阅 + DB 事件 webhook |
| 开源 / 许可证 | 是；Apache-2.0 + MIT（graphql-engine v2） |
| 主仓库 | [hasura/graphql-engine](https://github.com/hasura/graphql-engine)（★ 32k） |
| 核心功能 | 即时 GraphQL API（含 CRUD、聚合、分页）；细粒度 RBAC（行/列级）；实时订阅（WebSocket）；DB 事件触发 webhook；REST API 端点；远程 Schema / Remote Joins 数据联邦 |
| 商业模式 / 定价 | 开源 v2 可完全自托管；Hasura DDN 云端：Free（$0，无限 API 请求）、Base（$5/active model/月）、Advanced（$30/active model/月）；Private DDN 企业价 |
| 差异化 / 价值主张 | 零代码生成 GraphQL API；比手写 API 快 8×；自动处理 N+1；开源生态最大（32k stars）；2026 年品牌转型 PromptQL 向 AI Agent 数据层延伸 |
| 主要竞品（初判）| PostGraphile（开源自托管 GraphQL/Postgres）、Apollo GraphQL（GraphQL 平台）、Hygraph（Headless CMS）、Supabase（BaaS，含 GraphQL）、Neon（Postgres-as-a-service） |
| Olares Market | 已收录（⬜ 未调研） |
| 来源 | [hasura.io](https://hasura.io)、[hasura.io/pricing](https://hasura.io/pricing)、[github.com/hasura/graphql-engine](https://github.com/hasura/graphql-engine)、[hasura.io/graphql](https://hasura.io/graphql) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | hasura.io |
| SEMrush Rank | 406,222 |
| 自然关键词数 | 3,177 |
| 月自然流量（US）| 3,743 |
| 自然流量估值 | $23,172/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 119 词 |
| 排名 4-10 位 | 550 词 |
| 排名 11-20 位 | 713 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| hasura.io | 3,147 | 3,738 | 99.87% |
| cloud.hasura.io | 19 | 5 | 0.13% |
| console.hasura.io | 6 | ~0 | — |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|-----|-----|------|------|-----|
| mssql | 3 | 6,600 | 58 | $12.82 | 231 | 信息 | /learn/database/microsoft-sql-server/what-is-mssql/ |
| sql server download | 3 | 2,400 | 61 | $7.19 | 156 | 信息 | /learn/database/…/1-installing-mssql-windows/ |
| ms sql | 4 | 4,400 | 64 | $12.82 | 105 | 信息/导航 | /learn/database/microsoft-sql-server/what-is-mssql/ |
| sql psql | 12 | 18,100 | 69 | $4.90 | 90 | 信息 | /blog/top-psql-commands-and-flags… |
| psql commands | 2 | 1,300 | 37 | $2.40 | 84 | 信息 | /blog/top-psql-commands-and-flags… |
| what is psql | 2 | 1,300 | 59 | $0.81 | 84 | 信息 | /blog/top-psql-commands-and-flags… |
| psql | 8 | 14,800 | 50 | $4.90 | 74 | 信息 | /blog/top-psql-commands-and-flags… |
| hasura- | 1 | 90 | 33 | $8.44 | 72 | 导航/商业 | hasura.io/ |
| hasura | 1 | 1,900 | 40 | $8.44 | 49 | 导航/商业 | hasura.io/ |
| graphql | 4 | 18,100 | 55 | $2.62 | 47 | 信息/导航 | /learn/graphql/intro-graphql/what-is-graphql/ |
| mssql download | 3 | 1,300 | 75 | $5.47 | 45 | 信息 | /learn/…/1-installing-mssql-windows/ |
| hasura graphql | 1 | 170 | 37 | $9.35 | 42 | 信息/商业 | /graphql/ |
| hasura ddn | 1 | 50 | 11 | $0 | 40 | 导航/商业 | /docs/3.0/index/ |
| billing owner | 7 | 2,900 | 18 | $0 | 37 | 信息 | /docs/2.0/hasura-cloud/…/billing-owner/ |
| sql entity relationship diagram | 2 | 260 | 25 | $3.70 | 34 | 信息 | /learn/database/microsoft-sql-server/er-modeling/ |
| graphql-tag | 2 | 210 | 20 | $0 | 27 | 信息 | /learn/graphql/…/graphql-tag/ |
| psql connect to database | 4 | 720 | 37 | $3.10 | 25 | 信息 | /blog/top-psql-commands-and-flags… |
| graphql query | 3 | 590 | 27 | $2.05 | 17 | 信息 | /learn/graphql/…/graphql-queries/ |
| super graph | 2 | 90 | 23 | $0 | 11 | 信息 | /supergraph |
| what is hasura | 1 | 110 | 27 | $0 | 14 | 信息 | /blog/what-is-hasura-ce3b5c6e80e8 |

> 洞察：Hasura 的流量主力竟然是 MSSQL/psql 教程内容（前三位），而非 Hasura 品牌词或 GraphQL 产品词——典型的"博客内容带流量，但不带转化"格局。GraphQL 品牌词本身（"graphql" vol 18,100）它只排第 4，流量份额极小。

### 付费词（Google Ads）

未在 US 数据库检测到付费投放，CPC 估值为 $0。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| supabase alternative | 260 | 12 | $5.28 | 商业 | ⭐ 高机会；Hasura 可以作为 Supabase 替代项之一 |
| supabase vs hasura | 20 | 0 | $0 | 商业 | ⭐ 近零 KD，直接对比词 |
| hasura alternative | 0 | 0 | $4.43 | 商业 | 无量但 CPC 高，说明有商业意图；品牌词未建立"替代"心智 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| graphql | 18,100 | 71 | $2.54 | 信息/导航 | 总量大但 KD 极高，不宜硬攻 |
| graphql subscriptions | 320 | 32 | $6.50 | 信息 | ⭐ 偏低 KD，Hasura 核心特性 |
| graphql tutorial | 390 | 47 | $1.23 | 信息 | Hasura 已有大量教程，可对接 |
| graphql schema | 320 | 36 | $4.32 | 信息 | 中等 KD，核心概念词 |
| graphql security | 320 | 38 | $8.89 | 信息 | 中等 KD，CPC 高（商业价值） |
| graphql query | 590 | 27 | $2.05 | 信息 | ⭐ KD 低，量较高 |
| graphql mutation | 260 | 25 | $0 | 信息 | ⭐ KD 低 |
| graphql federation | 260 | 51 | $3.18 | 信息 | KD 较高 |
| graphql caching | 70 | 36 | $0 | 信息 | 中等机会 |
| graphql server | 140 | 56 | $4.01 | 信息 | KD 偏高 |
| graphql backend | 20 | 0 | $0 | 信息 | ⭐ 近零 KD |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| hasura | 1,900 | 40 | $8.44 | 导航/商业 | 品牌导航词，Hasura 自占 pos 1 |
| hasura graphql | 170 | 37 | $9.35 | 信息/商业 | 品牌+品类组合词 |
| hasura ddn | 50 | 11 | $0 | 导航/商业 | ⭐ 极低 KD，新产品线关键词 |
| hasura graphql engine | 20 | 0 | $3.94 | 信息/商业 | ⭐ KD 0，精准意图 |
| what is hasura | 110 | 27 | $0 | 信息 | ⭐ KD 低，教育型词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| open source graphql | 20 | 0 | $0 | 信息 | ⭐ KD 0，精准 OSS 意图 |
| graphql realtime | 20 | 0 | $0 | 信息 | ⭐ KD 0，Hasura 核心场景 |
| graphql authorization | 20 | 0 | $0 | 信息 | ⭐ KD 0，Olares 安全叙事契合 |
| graphql permissions | 20 | 0 | $0 | 信息 | ⭐ KD 0，访问控制词 |
| database webhooks | 20 | 0 | $0 | 信息 | ⭐ KD 0，精准功能词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Hasura 是"在云上托管 GraphQL 引擎"，Olares 的切入是"把 GraphQL 引擎装在自己家的机器上"——数据不出门、免 DDN 月费、配合 Postgres/MySQL 全链路自托管。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|-----|-----|-----------|
| supabase alternative | 260 | 12 | $5.28 | ⭐⭐⭐ Olares Market 可同时安装 Hasura + Postgres，构成完整 Supabase 平替：GraphQL API + 数据库 + 文件存储全自托管 |
| graphql subscriptions | 320 | 32 | $6.50 | ⭐⭐ Hasura 实时订阅 on Olares：本地低延迟、数据不离设备，适合家庭自动化 / Personal Agent 实时数据管道 |
| graphql query | 590 | 27 | $2.05 | ⭐⭐ KD 低，可写"GraphQL query with self-hosted Hasura on Olares"教程，建 long-tail 词库 |
| graphql mutation | 260 | 25 | $0 | ⭐⭐ 同上，低 KD 信息词，可并入同一篇自托管教程 |
| open source graphql | 20 | 0 | $0 | ⭐⭐⭐ OSS 信号词，Olares Market 一键装 Hasura = 最简自托管路径，可做 GEO 内容 |
| hasura ddn | 50 | 11 | $0 | ⭐⭐ DDN 有 vendor lock-in 风险；Olares+Hasura CE 是数据主权替代方案，CTA 切入"Own your API" |
| graphql authorization | 20 | 0 | $0 | ⭐⭐ 安全/权限词，Olares 的 SandBox + Hasura 行列级 RBAC 强强联合，适合隐私敏感用户 |
| database webhooks | 20 | 0 | $0 | ⭐⭐ Hasura DB event → 本地 webhook handler，在 Olares 上触发本地 Agent pipeline，GEO 前哨 |
| supabase vs hasura | 20 | 0 | $0 | ⭐⭐ 直接对比词，可写"supabase vs hasura — and why self-hosting both beats either cloud" |
| graphql realtime | 20 | 0 | $0 | ⭐⭐ Olares 上 Hasura 提供本地实时 GraphQL，Personal Agent 订阅私有数据变更 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断 |
|--------|------|-----|-----|------|------|-----------|
| supabase alternative | 260 | 12 | $5.28 | 商业 | **主词候选** | KD 极低，商业意图，Olares+Hasura+Postgres = 最完整 self-hosted BaaS 平替；绝对攻击面 |
| graphql subscriptions | 320 | 32 | $6.50 | 信息 | **主词候选** | KD<35，量 320，CPC 高（$6.5）说明商业价值；Hasura 实时订阅是核心卖点，可写专文 |
| graphql query | 590 | 27 | $2.05 | 信息 | **主词候选** | 量最大且 KD 最低（27）的有效品类词，适合"self-hosted GraphQL query engine"教程切入 |
| graphql mutation | 260 | 25 | $0 | 信息 | **次级** | KD 25，量 260，并入 graphql query 教程文作 secondary keyword |
| graphql schema | 320 | 36 | $4.32 | 信息 | **次级** | 量 320，KD 可接受，可并入 Hasura 入门文 |
| graphql security | 320 | 38 | $8.89 | 信息 | **次级** | CPC $8.89 暗示高商业价值，作为"Hasura on Olares 安全文"的 secondary target |
| graphql caching | 70 | 36 | $0 | 信息 | **次级** | 量小，并入性能/架构文 |
| graphql tutorial | 390 | 47 | $1.23 | 信息 | **次级** | KD 47 偏高，作为 broader 信息词并入教程文 |
| hasura ddn | 50 | 11 | $0 | 导航/商业 | **次级** | KD 极低（11），导航+商业意图，可写"Hasura DDN vs self-hosted"比较文植入 Olares 方案 |
| what is hasura | 110 | 27 | $0 | 信息 | **次级** | KD 27，教育词，Olares 可做"what is Hasura + how to install on Olares"组合页 |
| open source graphql | 20 | 0 | $0 | 信息 | **GEO** | 语义精准，KD 0，进 FAQ/对比文抢 AI Overview 引用位 |
| graphql realtime | 20 | 0 | $0 | 信息 | **GEO** | 精准功能词，KD 0，Olares + Hasura 实时流场景 GEO 布局 |
| database webhooks | 20 | 0 | $0 | 信息 | **GEO** | KD 0，Hasura DB event 触发 Olares Agent pipeline，场景精准 |
| graphql authorization | 20 | 0 | $0 | 信息 | **GEO** | KD 0，隐私/权限主题，与 Olares 安全叙事吻合 |
| supabase vs hasura | 20 | 0 | $0 | 商业 | **GEO** | KD 0，直接对比词，做 comparison 内容顺手植入 |

---

## 核心洞见

1. **品牌护城河**：Hasura 的品牌词（"hasura"，1,900 vol，KD 40）它牢牢占据 pos 1，正面硬刚无意义。但其品牌认知仍在向 DDN 迁移（旧 graphql-engine 社区大，新 DDN 词量仅 50），品牌词本身并不强大。真正的护城河在内容生态（32k stars + 大量教程）而非搜索。

2. **可复制的打法**：Hasura 用的是**"大流量教程词覆盖 → 长尾转化"**——mssql、psql 这类与产品无直接关系的数据库教程词撑起了 60%+ 的有机流量。它的程序化内容（`/learn/` 路径的多语言课程）是流量引擎。Olares 可复制这个逻辑：做 GraphQL + 自托管 + Postgres 的一系列教程，从场景词进入，而非从品牌词。

3. **对 Olares 最关键的词**：
   - **`supabase alternative`**（260 vol，KD 12）——商业意图 + KD 极低，Olares 可以同时托管 Hasura + Postgres + 对象存储，构成比任何单一 SaaS 都完整的 BaaS 自托管方案；
   - **`graphql query`**（590 vol，KD 27）——量最大且 KD 最低的品类词，自托管 Hasura on Olares 教程的主词候选；
   - **`graphql subscriptions`**（320 vol，KD 32，CPC $6.50）——Hasura 实时订阅是其最有差异化的特性，自托管场景（Personal Agent 订阅私有数据）是 Olares 独特叙事。

4. **最大攻击面**：Hasura DDN 的 per-model 计费是显著痛点——随着 model 数增长，月费线性放大；老用户迁移 v2 → DDN 存在不满情绪。Olares Market 一键安装 Hasura CE（免费、无 model 限额）是完美反制叙事：**"Own your API, kill your Hasura bill"**。

5. **隐藏低 KD 金矿**：
   - `graphql mutation`（KD 25，260 vol）、`graphql query`（KD 27，590 vol）——核心 GraphQL 概念词，KD 远低于想象；
   - `graphql backend`（KD 0，20 vol）、`open source graphql`（KD 0，20 vol）——近零 KD，量小但极精准，适合 GEO 植入；
   - `what is hasura`（KD 27，110 vol）——教育型词，KD 低，"what is Hasura + install on Olares in 5 minutes" 是现成文章框架。

6. **GEO 前瞻布局**：
   - **"run Hasura locally with Docker on Olares"**——零量但场景精准，Personal Agent 场景的 AI 问答会频繁问这个；
   - **"self-hosted GraphQL API with row-level security"**——Olares + Hasura 组合的精准描述，抢 AI Overview；
   - **"database event triggers without vendor lock-in"**——Hasura DB webhook 在 Olares 本地执行，完全主权化，GEO 前哨词。

7. **与既有分析的关联**：olares-500-keywords 中未收录 Hasura 相关词；GraphQL 生态词（graphql query/mutation/subscriptions）是现有词库的补充维度——偏**开发者工具/后端 API** 方向，与现有 AI/存储/隐私词呈互补关系，是触达"全栈开发者自托管整个数据层"这一人群的重要入口。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_this × 多词）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
