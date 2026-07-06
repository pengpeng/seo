# Supabase SEO 竞品分析报告

> 域名：supabase.com | SEMrush US | 2026-07-06
> Supabase = 开源 Firebase 替代品（Apache 2.0 BaaS，基于 PostgreSQL，支持完整自托管）

---

## 项目理解（前置）

Supabase 是一套以 PostgreSQL 为核心的开源 BaaS（Backend-as-a-Service）平台，2020 年创立，定位为 Firebase 的开源替代方案。它将关系型数据库（Postgres）、鉴权（Auth）、实时订阅（Realtime）、对象存储（Storage）、边缘函数（Edge Functions）和自动生成的 REST/GraphQL API 打包在一个平台，提供 Firebase 级别的开发者体验，同时具备 SQL 能力、数据可移植性与零 vendor lock-in。截至 2026 年主仓库 104K+ GitHub Stars，估值约 $50 亿，已完成 7 轮融资超 $5 亿。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 PostgreSQL BaaS — Firebase 替代品，支持完整自托管 |
| 开源 / 许可证 | 是，Apache 2.0（OSI 认证，无商业限制，可 fork 建竞品） |
| 主仓库 | [github.com/supabase/supabase](https://github.com/supabase/supabase)（★ ~104K） |
| 核心功能 | Postgres 数据库、Auth（含 OAuth/Magic Link/SSO）、Realtime 订阅、Storage（S3 兼容）、Edge Functions、pgvector 向量支持 |
| 商业模式 / 定价 | 云托管（Free $0 / Pro $25/项目/月 / Team $599/项目/月 / Enterprise 定制）；自托管完全免费无功能限制；Free 项目 7 天不活跃会暂停 |
| 差异化 / 价值主张 | SQL + 关系型 vs Firebase NoSQL；Apache 2.0 无锁定；自托管无用量计费；pgvector 原生 AI 向量支持；MCP 协议已支持（AI Agent 集成） |
| 主要竞品（初判）| Firebase、Appwrite、PocketBase、Neon、Hasura、Directus |
| Olares Market | 未上架（自托管版 Docker Compose 部署，8GB+ RAM 要求较高） |
| 来源 | [supabase.com](https://supabase.com)、[GitHub](https://github.com/supabase/supabase)、[devopspack.com](https://devopspack.com/supabase-open-source-firebase-alternative-postgres/)、[aitoolpick.org/blog/supabase-review-2026](https://aitoolpick.org/blog/supabase-review-2026/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | supabase.com |
| SEMrush Rank | **11,724**（全球前 1.2 万，开发者工具顶级站点） |
| 自然关键词数 | 14,384 |
| 月自然流量（US）| **193,471** |
| 自然流量估值 | **$369,611/月** |
| 付费关键词数 | 119 |
| 月付费流量 | 9,161 |
| 月付费流量估值 | $22,539 |
| 排名 1-3 位 | **1,034** 词 |
| 排名 4-10 位 | **1,608** 词 |
| 排名 11-20 位 | **1,647** 词 |

> 自然流量是付费的 **21×**，典型开发者工具口碑驱动模式。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| supabase.com（主站） | 14,240 | 189,816 | 98.11% |
| status.supabase.com | 77 | 3,584 | 1.85% |
| hackathon.supabase.com | 2 | 40 | 0.02% |
| forms / api / select.supabase.com | 51 | 31 | 0.01% |

> 主站独揽 98%+ 流量，状态页有独立 SEO 词（"is supabase down"，KD 13）。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| supabase | 1 | 90,500 | 59 | $1.81 | 72,400 | 品牌 | / |
| supabase news | 1 | 49,500 | 56 | $0 | 39,600 | 品牌/信息 | /blog |
| supbase（误拼） | 1 | 5,400 | 34 | $1.81 | 4,320 | 品牌 | / |
| supabase pricing | 1 | 4,400 | 33 | $3.30 | 3,520 | 商业 | /pricing |
| supa | 1 | 12,100 | 54 | $1.73 | 3,000 | 品牌 | / |
| supabase subscriptions | 1 | 3,600 | 45 | $4.50 | 2,880 | 商业 | /pricing |
| supabse（误拼） | 1 | 2,900 | 74 | $1.81 | 2,320 | 品牌 | / |
| supabase login | 1 | 2,400 | 31 | $0.09 | 1,920 | 导航 | / |
| supabase auth | 1 | 2,400 | 46 | $4.59 | 1,920 | 商业 | /docs/guides/auth |
| supoerbase（误拼） | 1 | 1,900 | 56 | $0 | 1,520 | 品牌 | / |
| superbase（误拼） | 1 | 5,400 | 57 | $2.16 | 1,339 | 品牌 | / |
| supabase authentication | 1 | 1,600 | 50 | $4.33 | 1,280 | 商业 | /docs/guides/auth |
| supabase status | 1 | 1,300 | 23 | $0 | 1,040 | 导航 | status.supabase.com |
| supa base（误拼） | 1 | 1,300 | 60 | $1.27 | 1,040 | 品牌 | / |
| supabase docs | 1 | 1,000 | 59 | $20.94 | 800 | 导航 | /docs |
| supabase realtime | 1 | 720 | 42 | $9.64 | 576 | 商业 | /docs/guides/realtime |
| supabase edge functions | 1 | 720 | 46 | $7.45 | 576 | 商业 | /docs/guides/functions |
| supabase nextjs | 1 | 390 | 57 | $6.21 | 312 | 信息 | /docs/guides/getting-started/quickstarts/nextjs |
| supabase self host | 1 | 390 | 53 | $4.76 | 312 | 商业 | /docs/guides/self-hosting |
| supabase python | 1 | 390 | 45 | $10.13 | 312 | 信息 | /docs/reference/python |
| supabse mcp | 1 | 480 | 32 | $0 | 384 | 信息 | /docs/guides/ai-tools/mcp |
| supabase storage | 1 | 480 | 60 | $4.16 | 384 | 商业 | /docs/guides/storage |

> 大量品牌误拼变体（supbase/supabse/supoerbase/superbase/supa base…）全部排名第 1，带来可观长尾流量。`supabase news` 居第 2，流量导向 /blog，显示内容运营是核心引擎。

### 付费词（Google Ads，按流量排序）

Supabase 广告策略精准：主要买自身品牌词 + **进攻竞品**（vibe coding 场景），以 `/solutions/vibe-coders` 落地页吸引 "firebase studio" / "bolt.diy" 等竞品的搜索流量。

| 关键词 | 月量 | CPC | 广告流量 | 落地页 |
|--------|------|-----|---------|--------|
| supabase（x3 广告位） | 90,500 | $1.82 | ~6,000 | / |
| firebase studio | 18,100 | $6.61 | 850 | /solutions/vibe-coders |
| postgres | 22,200 | $4.58 | 199 | / |
| bolt.diy | 2,400 | $4.09 | 112 | /solutions/vibe-coders |
| supabase auth | 2,400 | $4.33 | 112 | / |
| postgresql download | 4,400 | $4.54 | ~52 | / |
| post gress sql（误拼） | 1,000 | $5.04 | 47 | / |

> **关键洞察**：Supabase 购买了 `firebase studio`（Google 亲儿子 Firebase 的 AI 新产品）词 → 落地到 `/solutions/vibe-coders`，直接把 vibe-coder 人群从 Google/Firebase 截流。同时买 `bolt.diy`（Stackblitz 的开源 AI 编程工具），说明 Supabase 正在积极争夺"AI 驱动开发"场景。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| supabase vs firebase | 1,600 | 25 | $8.78 | 信息 | ⭐ 最大对比词，KD 合理 |
| firebase vs supabase | 720 | 24 | $16.79 | 信息 | ⭐ 同义变体，高 CPC 说明商业意图 |
| firebase alternatives | 590 | 32 | $6.94 | 信息 | ⭐ 开源/替代意图 |
| supabase alternatives | 590 | 16 | $5.28 | 信息 | ⭐ KD 极低，机会词 |
| neon vs supabase | 480 | 19 | $22.63 | 信息 | ⭐ CPC $22，强商业意图 |
| supabase alternative | 260 | **12** | $5.28 | 信息 | ⭐ **KD 最低**，Olares 最佳切入 |
| appwrite vs supabase | 110 | **10** | $8.87 | 信息 | ⭐ BaaS 三方对比，KD 极低 |
| pocketbase vs supabase | 110 | **11** | $0 | 信息 | ⭐ 轻量替代对比 |
| supabase vs mongodb | 170 | **10** | $260.85 | 信息 | ⭐ CPC 异常高（$260），数据库决策词 |
| supabase vs neon | 260 | 16 | $16.50 | 信息 | ⭐ Postgres 托管服务细分 |
| firebase alternative | 170 | 17 | $6.94 | 信息 | ⭐ 核心意图词 |
| firebase competitors | 70 | **12** | $6.13 | 信息 | ⭐ 低 KD 品类词 |
| open source firebase alternative | 70 | **12** | $0 | 信息 | ⭐ 自托管意图明确 |
| supabase open source firebase alternative | 70 | **12** | $0 | 信息 | ⭐ 长尾 GEO 候选 |
| supabase cheaper alternative | 40 | 20 | $0 | 信息 | ⭐ 价格敏感型 |
| better than supabase | 40 | 14 | $10.90 | 信息/商业 | ⭐ 高 CPC 隐藏意图 |
| firebase alternative self hosted | 20 | 0 | $0 | 信息 | ⭐ 极精准信号词 |
| supabase alternative self hosted | 20 | 0 | $0 | 信息 | ⭐ GEO 精准词 |
| self hosted baas | 20 | 0 | $0 | 信息 | ⭐ GEO 品类词 |

### 品类词（BaaS 整体赛道）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| appwrite | 6,600 | 59 | $1.76 | 导航 | Supabase 最强开源对手 |
| pocketbase | 2,900 | 64 | $14.01 | 导航 | 轻量单文件替代，KD 高 |
| directus | 2,400 | 65 | $6.74 | 导航 | 无头 CMS + BaaS |
| hasura | 1,900 | 49 | $6.56 | 导航 | GraphQL BaaS |
| what is supabase | 3,600 | 37 | $7.57 | 信息 | 入门教育词 |
| nhost | 260 | 40 | $11.58 | 导航 | Hasura 托管 + 开源 |
| convex backend | 170 | 31 | $14.11 | 导航 | 近年新兴竞品 |
| parse server | 170 | 26 | $0 | 信息 | ⭐ 经典开源 BaaS |
| postgres as a service | 390 | 68 | $20.34 | 商业 | 高竞争价格词 |
| backend as a service open source | 20 | 0 | $0 | 信息 | ⭐ GEO 候选 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| supabase pricing | 4,400 | 29 | $3.44 | 商业 | ⭐ 高量+低 KD 定价词 |
| supabase mcp | 4,400 | 46 | $15.14 | 信息 | AI Agent 集成新爆词 |
| supabase auth | 2,400 | 46 | $4.59 | 商业 | 核心功能词 |
| supabase realtime | 720 | 42 | $9.64 | 商业 | 实时功能词 |
| supabase free tier | 390 | 27 | $1.42 | 商业 | ⭐ 定价决策词 |
| supabase postgres | 390 | 27 | $4.59 | 商业 | ⭐ 数据库核心词 |
| supabase cost | 320 | 32 | $4.02 | 商业 | ⭐ 价格关注词 |
| supabase functions | 260 | 44 | $0 | 商业 | Edge Functions 词 |
| supabase rls | 210 | 34 | $0 | 信息/商业 | Row Level Security 教程 |
| supabase vector | 140 | 39 | $4.92 | 商业 | AI/向量搜索词 |
| supabase pgvector | 140 | 51 | $5.62 | 商业/信息 | AI 数据库竞争词 |
| supabase ai | 210 | 46 | $3.02 | 商业 | AI 功能词 |
| supabase migrate | 110 | 38 | $8.07 | 信息 | 迁移教程词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| supabase self host | 390 | 53 | $4.76 | 商业 | 核心自托管词 |
| supabase self hosted | 260 | 52 | $2.99 | 商业 | 同义变体 |
| supabase self hosting | 210 | 55 | $2.99 | 信息 | 同义变体 |
| supabase docker | 320 | 70 | $18.03 | 信息 | 技术路径词，KD 高 |
| supabase docker compose | 140 | 48 | $0 | 信息 | Docker Compose 部署词 |
| supabase local | 260 | 46 | $2.34 | 商业 | 本地开发词 |
| supabase local development | - | 30 | $0 | 信息 | ⭐ 本地开发教程 |
| can i self host supabase | 30 | 0 | $0 | 信息 | ⭐ GEO：用户疑惑词 |
| is supabase self hosted | 30 | 0 | $0 | 信息 | ⭐ GEO：认知词 |
| run supabase locally | 20 | 0 | $0 | 信息 | ⭐ GEO：技术操作词 |
| supabase gdpr | 20 | 0 | $0 | 信息 | ⭐ GEO：数据主权词 |
| supabase raspberry pi | 20 | 0 | $0 | 信息 | ⭐ GEO：边缘部署词 |
| supabase free alternative | 20 | 0 | $9.95 | 信息 | ⭐ 高 CPC 信号词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Supabase 是"开源 Firebase 替代"叙事最成功的项目，但自托管版门槛（8GB+ RAM、Docker Compose 多容器）挡住了大量个人用户；Olares One = 把这条路变成一键部署的硬件平台，Olares OS = 把零散的 Postgres/Auth/Storage 应用以 Agent-Native 方式编排起来。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| supabase alternative | 260 | 12 | $5.28 | 在 Olares 上自托管 Supabase = 数据完全自有的 Firebase 替代；Olares OS 提供更完整的"个人云 + BaaS"方案 | ⭐⭐⭐ |
| firebase alternative self hosted | 20 | 0 | $0 | GEO 精准词：Olares + Supabase self-hosted = 真正 GDPR 合规的 Firebase 替代，数据不出家门 | ⭐⭐⭐ |
| supabase alternative self hosted | 20 | 0 | $0 | 同上，专门为 Supabase 自托管用户写的 FAQ 词 | ⭐⭐⭐ |
| supabase vs firebase | 1,600 | 25 | $8.78 | 对比内容可加"第三个选项：自托管 Supabase on Olares = 无月费 + 数据主权"；合法截流 | ⭐⭐⭐ |
| firebase alternative | 170 | 17 | $6.94 | Olares 作为"你自己的 Firebase"平台叙事，强调 own your data | ⭐⭐ |
| self hosted baas | 20 | 0 | $0 | GEO：Olares 是最接近"完整 self-hosted BaaS"定义的个人云 OS | ⭐⭐⭐ |
| supabase self host | 390 | 53 | $4.76 | 虽 KD 高，但 Olares 可做"如何在 Olares 上运行 Supabase"教程内容（Olares 市场未来上架机会） | ⭐⭐ |
| can i self host supabase | 30 | 0 | $0 | FAQ 抢占 AI Overview："是的，可以用 Olares 一键部署 Supabase" | ⭐⭐⭐ |
| supabase gdpr | 20 | 0 | $0 | 数据主权叙事：GDPR 合规的 Supabase 自托管 = Olares 价值主张核心 | ⭐⭐⭐ |
| supabase raspberry pi | 20 | 0 | $0 | Olares ARM 支持（script 路径）可直接接住这批用户 | ⭐⭐ |
| appwrite vs supabase | 110 | 10 | $8.87 | 三方对比：Appwrite vs Supabase vs Olares self-hosted BaaS | ⭐⭐ |
| open source firebase alternative | 70 | 12 | $0 | 教育型内容：Supabase + Olares = 最完整的开源 Firebase 替代组合 | ⭐⭐ |
| supabase mcp | 4,400 | 46 | $15.14 | Supabase 已支持 MCP；Olares Agent-Native OS 可将 Supabase MCP 作为 Personal Agent 的后端 tool | ⭐⭐ |
| supabase free alternative | 20 | 0 | $9.95 | 高 CPC 隐藏意图：免费替代 = Olares 自托管方案无月费 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|----|------|------|--------------------------|
| supabase vs firebase | 1,600 | 25 | $8.78 | 信息 | 主词候选 | 量大 KD 合理；Olares 角度可加"第三选项：自托管免月费" |
| supabase pricing | 4,400 | 29 | $3.44 | 商业 | 主词候选 | 高量+低 KD，定价决策词；可对比 Olares self-hosted 的零月费 |
| supabase mcp | 4,400 | 46 | $15.14 | 信息 | 主词候选 | 新爆词（MCP 生态），Olares Agent-Native OS 做 MCP hub 的切入 |
| supabase alternatives | 590 | 16 | $5.28 | 信息 | 主词候选 | KD 极低，量合理；Olares 可部署 Supabase 或提供 BaaS 替代方案 |
| firebase alternatives | 590 | 32 | $6.94 | 信息 | 主词候选 | 跨域词，合并进 firebase alternative 内容簇 |
| firebase vs supabase | 720 | 24 | $16.79 | 信息 | 次级 | 并入 supabase vs firebase 内容；高 CPC 显示商业意图 |
| supabase alternative | 260 | **12** | $5.28 | 信息 | 主词候选 | **KD 12 最低机会词**；自托管叙事直接切入 |
| neon vs supabase | 480 | 19 | $22.63 | 信息 | 主词候选 | CPC $22，强商业；Postgres 托管细分对比 |
| supabase free tier | 390 | 27 | $1.42 | 商业 | 次级 | 定价关注词；Olares 自托管 = 真免费无上限 |
| supabase postgres | 390 | 27 | $4.59 | 商业 | 次级 | 数据库核心词；强化 Postgres 自托管叙事 |
| supabase cost | 320 | 32 | $4.02 | 商业 | 次级 | 价格痛点；Olares One 摊销后 BaaS 成本趋零 |
| appwrite vs supabase | 110 | **10** | $8.87 | 信息 | 主词候选 | KD 最低！三方 BaaS 对比词，含 Olares 自托管视角 |
| pocketbase vs supabase | 110 | **11** | $0 | 信息 | 主词候选 | KD 11，轻量 BaaS 对比，Olares 可同时部署两者 |
| supabase vs mongodb | 170 | **10** | $260.85 | 信息 | 次级 | CPC $260 异常，数据库选型高价值词 |
| open source firebase alternative | 70 | **12** | $0 | 信息 | 次级 | 精准意图；GEO + 内容切入点 |
| supabase self host | 390 | 53 | $4.76 | 商业 | 次级 | KD 偏高，但 Olares 部署教程价值高；待 Market 上架后升为主词 |
| self hosted baas | 20 | 0 | $0 | 信息 | GEO | 近零量精准词，抢 AI Overview 引用位 |
| supabase gdpr | 20 | 0 | $0 | 信息 | GEO | 数据主权 FAQ，Olares 欧洲用户最强痛点词 |
| can i self host supabase | 30 | 0 | $0 | 信息 | GEO | 问题词，抢 PAA/Featured Snippet |
| firebase alternative self hosted | 20 | 0 | $0 | 信息 | GEO | 意图最精准的自托管词，Olares 直接答 |
| supabase raspberry pi | 20 | 0 | $0 | 信息 | GEO | Olares ARM script 路径可直接接，FAQs |
| supabase free alternative | 20 | 0 | $9.95 | 信息 | GEO | CPC $9.95 说明有商业价值，GEO 抢占 |

---

## 核心洞见

1. **品牌护城河**：`supabase`（90,500 月量，KD 59）护城河极强，加上 Supabase 自己也在买这个词，正面竞争无意义。但品牌词之外，KD<30 的机会词数量可观（pricing KD 29、alternative KD 12、neon vs supabase KD 19 等），侧面进入完全可行。

2. **可复制的打法**：Supabase 对比/替代类内容是核心流量引擎——`/solutions/vibe-coders`（针对 firebase studio/bolt.diy）证明它在积极用 Ads + 落地页抢竞品流量。可复制路径：**① 制作对比落地页**（supabase vs firebase、appwrite vs supabase、pocketbase vs supabase）；**② 购买竞品词广告**（低量但精准）；**③ 建自托管教程内容**（/docs/guides/self-hosting 已在自然排名 #1，说明 SEO 价值被验证）。

3. **对 Olares 最关键的 3 个词**：
   - `supabase alternative`（KD 12，260/月）：**门槛最低的主词候选**，Olares 叙事 = "在 Olares 上自托管 Supabase = 真正自有的 BaaS，无月费无厂商锁定"
   - `supabase vs firebase`（KD 25，1,600/月）：**最高流量对比词**，内容可加入"第三选项：self-hosted Supabase on Olares OS"
   - `firebase alternative self hosted`（KD 0，20/月）：**GEO 精准词**，意图与 Olares 一致，抢 AI Overview / Perplexity 引用位

4. **最大攻击面**：Supabase cloud 的核心痛点是 **Free 项目 7 天暂停 + Pro $25/项目/月 + 数据存在 AWS 上**。这三个痛点直接呼应 Olares 叙事：① 自托管无暂停无月费；② 数据主权（GDPR 合规、数据不出家）；③ Olares One 一次买断，年化成本显著低于 Pro tier。

5. **隐藏低 KD 金矿**：`appwrite vs supabase`（KD 10）、`pocketbase vs supabase`（KD 11）、`supabase vs mongodb`（KD 10）——三个对比词 KD 均 ≤11，量 100-170，属于**极低竞争高意图**词，是 BaaS 领域最便宜的内容投资。

6. **GEO 前瞻布局**：`can i self host supabase`、`supabase gdpr`、`is supabase self hosted`、`self hosted baas`、`firebase alternative self hosted`、`supabase raspberry pi`——这批近零量词在 AI Overview / Perplexity 的答案框内被引用概率极高；建议写成 FAQ 段落嵌入相关对比文，边际成本为零。

7. **与既有词表的关联**：`olares-500-keywords-analysis` 中无直接 Supabase 相关词；本次分析为 Olares **补充了 BaaS/Firebase 替代赛道的完整词图**，尤其是 `supabase vs firebase`（1,600）→ `firebase alternatives`（590）→ `supabase alternative`（260）这条量级递减、KD 递减的词链，形成内容簇骨架。`supabase mcp`（4,400，KD 46）是 2026 年新出现的 MCP 集成词，与 Olares Agent-Native OS 叙事高度契合，建议列入 backlog 专项跟踪。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these × 3 批、phrase_related × 2 批、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
