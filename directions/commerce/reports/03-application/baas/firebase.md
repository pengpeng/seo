# Firebase SEO 竞品分析报告

> 域名：firebase.google.com | SEMrush US | 2026-07-06
> Firebase = Google 旗下 BaaS（Backend-as-a-Service）平台，移动/Web 开发者后端一站式服务

---

## 项目理解（前置）

Firebase 是 Google 旗下的全栈 BaaS（Backend-as-a-Service）平台，2011 年创立，2014 年被 Google 收购，目前已有超过 350 万个已部署应用。它以 Firestore（NoSQL 文档数据库）、Authentication、Realtime Database、Cloud Functions、Hosting、Cloud Messaging（FCM）、Crashlytics、Analytics 为核心，将移动/Web 后端所需的基础设施全部以托管 SaaS 形式提供，开发者无需自管服务器。**Firebase 不可自托管**——这是其最大的产品限制，也是 Supabase / Appwrite / PocketBase 等开源平替的核心攻击点。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Google 旗下闭源 BaaS：Firestore + Auth + Hosting + Functions + Analytics 一体化托管 |
| 开源 / 许可证 | 部分开源：客户端 SDK（Android/iOS/JS）Apache 2.0；**后端服务完全闭源，不可自托管** |
| 主仓库 | [firebase/firebase-ios-sdk](https://github.com/firebase/firebase-ios-sdk)（★6.6K）/ [firebase/firebase-js-sdk](https://github.com/firebase/firebase-js-sdk)（★5.1K）— SDK 仓库，平台本身不开源 |
| 核心功能 | Firestore（NoSQL）、Realtime Database、Authentication、Cloud Functions、Hosting、FCM、Crashlytics、Firebase Analytics、Firebase AI Logic（Gemini）、Firebase Studio（AI IDE） |
| 商业模式 / 定价 | Spark（免费，固定配额）+ Blaze（按用量计费，读/写/删除每次计费）+ Enterprise（定制）；**Blaze 按操作计费极易超支，重读写应用成本 3-5× Supabase** |
| 差异化 / 价值主张 | 成熟移动 SDK（离线同步、iOS/Android/Flutter 最优）、Google 全球 CDN、Google Cloud 生态深度集成（BigQuery/Gemini）；唯一劣势：无自托管选项 + 供应商锁定 |
| 主要竞品（初判）| Supabase（开源 PostgreSQL BaaS）、Appwrite（开源自托管 BaaS）、PocketBase（极简自托管）、AWS Amplify、Nhost |
| Olares Market | 未上架（Firebase 闭源不可自托管；开源平替 Supabase/Appwrite 可上架）|
| 来源 | [firebase.google.com](https://firebase.google.com)、[pkgpulse.com](https://www.pkgpulse.com/guides/supabase-vs-firebase-vs-appwrite-baas-2026)、[digitalapplied.com](https://www.digitalapplied.com/blog/supabase-vs-firebase-2026-backend-comparison-guide)、[cloudyunicorn.com/review/firebase](https://www.cloudyunicorn.com/review/firebase) |

---

## 流量基线（Phase 1）

> **子域名说明**：firebase.google.com 是 google.com 的子域名，SEMrush `domain_rank` 仅追踪根域（google.com rank=0 无参考意义）；以下流量数据来自 `resource_organic` 对 firebase.google.com 的直接查询，100 条高流量词合计约 **121K US 月流量**，实际总量更高。Semrush 统计 google.com 全域关键词数约 26K（含所有子域合并）。

### 概览（估算）

| 指标 | 数据 |
|------|------|
| 域名 | firebase.google.com |
| SEMrush Rank | 子域名（归属 google.com，rank=0；firebase.google.com 独立 rank 不可查）|
| Top 100 词月流量（US）| **≥121,000**（实际全量更高）|
| 排名 1 位 | **~88 词**（品牌/导航词霸占第 1）|
| 排名 2-3 位 | **~8 词** |
| 排名 4-10 位 | **~2 词** |
| 排名 11-20 位 | **0 词**（样本中） |
| 排名 21+ | **1 词**（gemini ai，vol 3.35M，pos 23）|
| 付费关键词 | 0（Google 不在 Google 上为自家产品投广告）|
| 流量估值 | 参照同类开发者工具 CPC（$7-13），估计 $800K-$1.5M/月 |

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| firebase | 1 | 74,000 | 97 | $7.88 | 59,200 | 品牌 | / |
| firebase console | 1 | 14,800 | 78 | $8.25 | 11,840 | 品牌 | console.firebase.google.com |
| firestore | 1 | 12,100 | 76 | $5.68 | 3,000 | 品牌/信息 | /docs/firestore |
| console.firebase | 1 | 2,400 | 97 | $8.28 | 1,920 | 导航 | console.firebase.google.com |
| firebase login | 1 | 1,900 | 71 | $7.91 | 1,520 | 导航 | console.firebase.google.com |
| firebase hosting | 1 | 1,900 | 63 | $12.91 | 1,520 | 信息/商业 | /docs/hosting |
| firestore chrome plugin | 1 | 1,900 | 0 | $0 | 1,520 | 信息 | /docs/auth/web/chrome-extension |
| firbase（误拼） | 1 | 1,900 | 93 | $7.88 | 1,520 | 品牌 | / |
| firebase auth | 1 | 1,600 | 57 | $7.54 | 1,280 | 信息/商业 | /docs/auth |
| firebase authentication | 1 | 1,600 | 56 | $8.56 | 1,280 | 信息/商业 | /docs/auth |
| firebase as a database | 1 | 1,300 | 55 | $9.12 | 1,040 | 信息 | /docs/database |
| database in firebase | 1 | 1,300 | 54 | $9.12 | 1,040 | 信息 | /docs/database |
| firevase（误拼） | 1 | 1,300 | 93 | $7.88 | 1,040 | 品牌 | / |
| fire base（误拼） | 1 | 1,300 | 92 | $7.35 | 1,040 | 品牌 | / |
| firebase cli | 1 | 880 | 54 | $4.91 | 704 | 信息 | /docs/cli |
| firebase cloud messaging | 1 | 880 | 79 | $7.56 | 704 | 信息/商业 | /docs/cloud-messaging |
| firebase sum | 1 | 4,400 | 28 | $7.88 | 580 | 信息 | /docs/firestore/query-data/aggregation-queries |
| firebase storage | 1 | 720 | 56 | $13.35 | 576 | 信息/商业 | /docs/storage |
| firebase firestore | 1 | 720 | 93 | $12.69 | 576 | 品牌 | /docs/firestore |
| gcm message | 2 | 6,600 | 28 | $7.55 | 541 | 信息 | /docs/cloud-messaging |
| firebase realtime database | 1 | 590 | 62 | $9.01 | 472 | 信息 | /docs/database |
| firebase app distribution | 1 | 590 | 50 | $5.20 | 472 | 信息/商业 | /docs/app-distribution |
| firebase dynamic links | 1 | 590 | 26 | $6.50 | 472 | 信息/商业 | /docs/dynamic-links |
| **gemini ai** | **23** | **3,350,000** | **100** | **$0.31** | **469** | 商业 | /docs/ai-logic |
| firebase studio | 2 | 14,800 | 74 | $6.79 | 384 | 信息/商业 | /docs/studio |
| firebase functions | 1 | 480 | 72 | $0 | 384 | 信息 | /docs/functions |
| firebase status | 1 | 480 | 64 | $0 | 384 | 导航 | status.firebase.google.com |
| firebase mcp server | 1 | 320 | 25 | $27.55 | 256 | 信息 | /docs/ai-assistance/mcp-server |
| firebase cloud functions | 1 | 320 | 58 | $24.86 | 256 | 信息/商业 | /docs/functions |
| firebase cost | 1 | 880 | 59 | $12.45 | 218 | 信息/商业 | /pricing |
| firebase spark plan | 1 | 260 | 43 | $11.21 | 208 | 信息/商业 | /pricing |
| firebase free tier | 1 | 260 | 40 | $10.50 | 208 | 信息/商业 | /pricing |
| firebase test lab | 1 | 260 | 19 | $10.08 | 208 | 信息/商业 | /docs/test-lab |

> 品牌误拼变体（firbase/firevase/firebas/firebae/ffirebase 等）约 30+ 条，均排名第 1，流量合计约 12K/月。"gemini ai"（3.35M 月量）firebase 排第 23 位，是非品牌大词里排名最高的，说明 Firebase AI Logic 页面正在获取 AI 搜索流量的溢出。

### 付费词（Google Ads）

Firebase.google.com 未检测到付费广告投放（Google 旗下产品不需在 Google 搜索购买广告位）。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| supabase vs firebase | 1,600 | 25 | $8.78 | 对比 | ⭐ 最高量低KD对比词 |
| firebase vs supabase | 720 | 24 | $16.79 | 对比 | ⭐ 高CPC |
| firebase alternatives | 590 | 32 | $6.94 | 信息 | 主要替代词 |
| supabase alternatives | 590 | 16 | $5.28 | 信息 | ⭐ 低KD延伸词 |
| which is cheaper firebase or supabase | 390 | 34 | $0 | 对比 | 定价敏感问题 |
| realtime database | 260 | 56 | $6.16 | 信息/商业 | Firebase 核心功能词 |
| supabase alternative | 260 | 12 | $5.28 | 信息 | ⭐ 极低KD |
| firebase alternative | 170 | 17 | $6.94 | 信息 | ⭐ 低KD直接词 |
| firebase baas | 140 | 40 | $0 | 信息 | 品类定位词 |
| aws amplify vs firebase | 70 | 9 | $0 | 对比 | ⭐ 超低KD |
| firebase competitors | 70 | 12 | $6.13 | 信息 | ⭐ 低KD |
| supabase open source firebase alternative | 70 | 12 | $0 | 信息 | ⭐ 精准长尾 |
| appsync vs firebase | 50 | 5 | $0 | 对比 | ⭐ KD=5 |
| firebase auth alternatives | 40 | 13 | $5.46 | 信息 | ⭐ 功能级替代词 |
| supabase self hosted alternative | 40 | 14 | $0 | 信息 | ⭐ 自托管意图 |
| firebase dynamic links alternative | 70 | 16 | $14.25 | 信息 | ⭐ 功能替代词 |
| google firebase alternatives | 30 | 23 | $3.81 | 信息 | ⭐ |
| alternative to firebase | 30 | 27 | $8.99 | 信息 | ⭐ |
| firebase auth alternatives | 40 | 13 | $5.46 | 信息 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| baas | 4,400 | 50 | $9.81 | 信息 | BaaS品类大词 |
| backend as a service | 590 | 34 | $10.11 | 信息 | ⭐ 品类解释词 |
| firebase studio | 18,100 | 64 | $6.61 | 信息/商业 | Firebase 新 AI IDE 产品 |
| firebase hosting | 1,900 | 52 | $10.52 | 信息/商业 | 功能词高量 |
| firebase analytics | 720 | 80 | $9.41 | 信息 | 功能词高KD |
| firebase auth | 1,600 | 83 | $8.79 | 信息/商业 | 高量高KD |
| firebase realtime database | 590 | 62 | $9.01 | 信息 | |
| google firestore | 590 | 74 | $7.85 | 商业 | |
| open source baas | 20 | 0 | $0 | 信息 | ⭐ 近零量但语义完美 |
| self hosted baas | 20 | 0 | $0 | 信息 | ⭐ GEO词 |

### 产品 / 功能词（firebase 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| firebase pricing | 1,600 | 58 | $3.84 | 商业 | 高量定价词 |
| firebase studio | 18,100 | 64 | $6.61 | 信息/商业 | 新AI IDE |
| firebase cost | 880 | 59 | $12.45 | 信息/商业 | 高CPC |
| firebase hosting | 1,900 | 63 | $12.91 | 信息/商业 | 高CPC |
| firebase cloud functions | 320 | 58 | $24.86 | 信息/商业 | 极高CPC |
| firebase mcp server | 320 | 25 | $27.55 | 信息 | ⭐ 最高CPC + 低KD |
| firebase free tier | 210 | 40 | $3.76 | 信息/商业 | 定价痛点 |
| firebase blaze plan | 210 | 41 | $0 | 信息/商业 | 定价痛点 |
| firebase spark plan | 260 | 43 | $11.21 | 信息/商业 | 定价痛点 |
| firebase bandwidth pricing | 720 | 55 | $0 | 商业 | 定价敏感 |
| firebase test lab | 260 | 19 | $10.08 | 信息/商业 | ⭐ 低KD功能词 |
| firebase emulator | 260 | 41 | $0 | 商业 | 开发工具词 |
| firebase dynamic links | 590 | 26 | $6.50 | 信息/商业 | ⭐ 低KD，已弃用功能 |
| firebase crashlytics | 390 | 75 | $5.75 | 信息/商业 | 高KD |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| appwrite | 6,600 | 59 | $1.76 | 信息 | 开源BaaS竞品品牌词 |
| pocketbase | 2,900 | 64 | $14.01 | 信息 | 极简自托管BaaS |
| supabase | 90,500 | 64 | $1.82 | 信息 | 最大开源Firebase替代 |
| appwrite vs firebase | 20 | 0 | $0 | 对比 | ⭐ 近零KD，新兴词 |
| pocketbase vs firebase | 20 | 0 | $0 | 对比 | ⭐ 近零KD，新兴词 |
| open source firebase | 20 | 0 | $0 | 信息 | ⭐ GEO词 |
| self hosted firebase | 20 | 0 | $0 | 信息 | ⭐ GEO词 |
| firebase alternative open source | 20 | 0 | $5.24 | 信息 | ⭐ 精准意图 |
| firebase alternative self hosted | 20 | 0 | $0 | 信息 | ⭐ 精准意图 |
| open source baas | 20 | 0 | $0 | 信息 | ⭐ GEO词 |
| self hosted baas | 20 | 0 | $0 | 信息 | ⭐ GEO词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Firebase 是闭源不可自托管的 BaaS，其最大痛点是供应商锁定（Google 生态绑定）+ 按操作计费易超支 + NoSQL 模型限制。Olares Market 可上架 Supabase / Appwrite / PocketBase 这类开源自托管 BaaS，主打"一键部署 + 数据留本地 + 无 per-operation 计费 + 可迁移"。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| supabase | 90,500 | 64 | $1.82 | ⭐⭐ 最大开源 Firebase 替代，Olares Market 可上架（需 8GB+ RAM）|
| firebase studio | 18,100 | 64 | $6.61 | ⭐ Firebase 新 AI IDE；Olares 可对标本地 AI 开发环境（Code Server + 本地 LLM）|
| appwrite | 6,600 | 59 | $1.76 | ⭐⭐⭐ 开源自托管 BaaS，Olares Market 最优先上架候选（Docker 单容器，4GB RAM，Firebase 体验最相似）|
| supabase vs firebase | 1,600 | 25 | $8.78 | ⭐⭐⭐ KD 低量高，Olares 可写「Appwrite vs Supabase vs Firebase：自托管 BaaS 终极对比」|
| firebase pricing | 1,600 | 58 | $3.84 | ⭐ 定价敏感词，Olares 叙事："自托管 = 零 per-operation 费用，无计费上限"|
| firebase vs supabase | 720 | 24 | $16.79 | ⭐⭐ 高 CPC 对比词，内容契合度极高 |
| firebase alternatives | 590 | 32 | $6.94 | ⭐⭐ Olares Market 开源 BaaS 清单页最佳切入词 |
| pocketbase | 2,900 | 64 | $14.01 | ⭐⭐ 极简自托管 BaaS，单文件部署，Olares Market 上架极简单 |
| firebase cost | 880 | 59 | $12.45 | ⭐ 高 CPC，Firebase Blaze 超支痛点，Olares 对标"本地 BaaS 零运营成本" |
| firebase alternative | 170 | 17 | $6.94 | ⭐⭐⭐ KD=17 超低，精准意图，Olares 替代页直接切入 |
| supabase alternative | 260 | 12 | $5.28 | ⭐⭐ KD=12，Olares 可作为 Supabase 的自托管增强方案 |
| firebase competitors | 70 | 12 | $6.13 | ⭐⭐ KD=12，信息意图页切入自托管 BaaS 对比 |
| aws amplify vs firebase | 70 | 9 | $0 | ⭐⭐ KD=9 超低，Olares 三方对比（自托管 vs 云 BaaS）|
| appsync vs firebase | 50 | 5 | $0 | ⭐⭐ KD=5 极低，可写对比文顺带推 Olares 自托管方案 |
| firebase auth alternatives | 40 | 13 | $5.46 | ⭐ Olares 可上架 Authelia / Authentik（开源 SSO）对标 |
| supabase self hosted alternative | 40 | 14 | $0 | ⭐⭐ 自托管意图完全契合 Olares |
| open source firebase | 20 | 0 | $0 | ⭐⭐⭐ GEO 占位词，Olares 上架 Appwrite = "开源 Firebase 在 Olares" |
| self hosted firebase | 20 | 0 | $0 | ⭐⭐⭐ GEO 占位词，Olares 场景完美契合 |
| appwrite vs firebase | 20 | 0 | $0 | ⭐⭐⭐ GEO 新兴词，上架后可写教程文章 |
| pocketbase vs firebase | 20 | 0 | $0 | ⭐⭐⭐ GEO 新兴词，PocketBase on Olares 教程 |
| open source baas | 20 | 0 | $0 | ⭐⭐⭐ GEO 词，Olares Market BaaS 品类页 |
| self hosted baas | 20 | 0 | $0 | ⭐⭐⭐ GEO 词，语义完美契合 Olares 核心价值 |
| firebase mcp server | 320 | 25 | $27.55 | ⭐ MCP 协议词，Firebase AI Logic 功能；Olares 本地 MCP server 可对标 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| supabase vs firebase | 1,600 | 25 | $8.78 | 对比 | **主词候选** | 量+KD最佳组合；Olares 可在 Supabase on Olares 教程文中植入 Firebase 对比 |
| firebase vs supabase | 720 | 24 | $16.79 | 对比 | **主词候选** | 高 CPC 对比词，配合 supabase.md 报告写「Firebase vs Supabase vs Appwrite 自托管对比」|
| firebase alternatives | 590 | 32 | $6.94 | 信息 | **主词候选** | Olares Market BaaS 清单文的核心词 |
| firebase alternative | 170 | 17 | $6.94 | 信息 | **主词候选** | KD=17 低竞争，精准意图，量>100 达主词线 |
| supabase alternative | 260 | 12 | $5.28 | 信息 | **主词候选** | KD=12 极低，Olares 作为 Supabase 的本地化增强方案切入 |
| firebase competitors | 70 | 12 | $6.13 | 信息 | **次级** | 量 70 低于主词线但 KD=12 极低，并入替代词文章 |
| aws amplify vs firebase | 70 | 9 | $0 | 对比 | **次级** | KD=9 超低，并入三方对比文章 |
| appsync vs firebase | 50 | 5 | $0 | 对比 | **次级** | KD=5 近乎零竞争，并入对比文 |
| firebase auth alternatives | 40 | 13 | $5.46 | 信息 | **次级** | 功能级替代词，Olares Auth 叙事机会 |
| supabase self hosted alternative | 40 | 14 | $0 | 信息 | **次级** | 自托管意图，on-topic |
| firebase mcp server | 320 | 25 | $27.55 | 信息 | **次级** | MCP 协议词，CPC 极高，技术社区向 |
| firebase test lab | 260 | 19 | $10.08 | 信息/商业 | **次级** | 低 KD 功能词，测试框架话题 |
| firebase dynamic links | 590 | 26 | $6.50 | 信息 | **次级** | Firebase 即将弃用该功能，痛点词 |
| open source firebase | 20 | 0 | $0 | 信息 | **GEO** | 近零量但语义完美，抢 AI Overview / Perplexity 引用位 |
| self hosted firebase | 20 | 0 | $0 | 信息 | **GEO** | 同上，Olares + Appwrite 场景完美契合 |
| appwrite vs firebase | 20 | 0 | $0 | 对比 | **GEO** | Appwrite 上架 Olares 后写的第一篇教程词 |
| pocketbase vs firebase | 20 | 0 | $0 | 对比 | **GEO** | PocketBase on Olares 教程入口词 |
| open source baas | 20 | 0 | $0 | 信息 | **GEO** | BaaS 品类 GEO 占位，语义绝对契合 |
| self hosted baas | 20 | 0 | $0 | 信息 | **GEO** | Olares = 自托管 BaaS 最优载体 |

---

## 核心洞见

1. **Firebase 品牌护城河极深，正面硬刚无意义。** "firebase" 单词 74K 月量 KD97，品牌词及误拼变体（firbase/firevase/firebae…）30+ 条全部排名第 1，流量结构 90%+ 是品牌/导航词。Google 的 PageRank 权重 + 品牌认知双重护城，Olares 无法也不必争这些词。

2. **Firebase 的 SEO 策略是"极度专注文档 SEO"，没有程序化内容落地页。** 不同于 Lovable 的 `/guides/` 矩阵，firebase.google.com 的高流量词几乎全部落在 `/docs/`、`/products/` 等产品文档页，没有"X vs Firebase"或"Firebase alternative"类内容。这意味着这个品类的对比内容机会**完全没有被 Firebase 自己占领**——第三方站点（supabase.com、appwrite.io、blog 文章）正在吃这些流量。

3. **对 Olares 最关键的 3 个词：`appwrite`（6,600 vol）、`supabase vs firebase`（1,600 vol, KD25）、`firebase alternative`（170 vol, KD17）。** Appwrite 是功能最接近 Firebase 的开源自托管 BaaS（Firebase-like 文档 API + 多语言 functions + Docker 一键部署），上架 Olares Market 后可承接大量开源 BaaS 搜索流量。`supabase vs firebase`（KD25）是量价比最高的对比词。

4. **最大攻击面：Firebase 的"无法自托管 + 按操作计费"双重痛点。** Firebase pricing（1,600 vol）、firebase cost（880 vol）、firebase free tier（210 vol）、firebase blaze plan（210 vol）等定价词密集出现，用户对 Blaze 计划的超额账单高度敏感（参考：重读写应用成本 3-5× Supabase）。Olares 的叙事应直击："自托管 BaaS = 零 per-operation 费用 + 数据完全归你 + 无 Google 供应商绑定"。

5. **隐藏低 KD 金矿：`appsync vs firebase`（KD5）、`aws amplify vs firebase`（KD9）、`supabase alternative`（KD12）、`firebase competitors`（KD12）、`firebase auth alternatives`（KD13）。** 这些词量虽小（40-260）但 KD 极低，CPC 有意义（$5-9），且都是有明确商业意图的对比词。配合 Appwrite / PocketBase 上架，可批量低成本占位。注意：`firebase mcp server`（320 vol, KD25, CPC $27.55）是最高 CPC 低 KD 词，技术向读者价值高。

6. **GEO 前瞻布局：** `open source firebase`、`self hosted firebase`、`self hosted baas`、`open source baas`（均 KD=0，月量~20）目前近零量，但这正是 AI 搜索引擎（Perplexity / AI Overview）的典型问句。Firebase 自己不可能回答"如何自托管 Firebase"——Olares 发布权威内容（含 Appwrite on Olares 安装教程）可直接成为这类问题的 AI 引用源。

7. **与既有分析的关联：** 本报告与 [supabase.md](supabase.md)（同目录）强关联，两者共同构建"开源 BaaS 生态 on Olares"叙事。`supabase vs firebase` / `firebase alternative` 这类词从两份报告看是关键重叠词，内容层应统一在一篇"Firebase vs Supabase vs Appwrite 自托管完整对比"文章里使用，而非拆成两篇。与 `olares-500-keywords` 中"自托管"、"开源替代"词族高度互补；**BaaS 作为子品类目前在 500 词表中缺失，建议补入 `appwrite`、`firebase alternative`、`supabase vs firebase` 三词。**

---

*数据来源：SEMrush US 数据库（resource_organic / domain_organic_subdomains / phrase_these / phrase_related / phrase_fullsearch / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*注：firebase.google.com 为子域名，SEMrush domain_rank 不追踪子域名独立排名，流量数据来自 resource_organic 实际查询（仅含抓到的 100 条高流量词，实际总量更高）。*
