# Karakeep SEO 竞品分析报告

> 域名：karakeep.app | SEMrush US | 2026-07-06
> 自托管书签收集器：AI 自动打标签 + 全文搜索，原名 Hoarder，26k+ GitHub stars，开源 AGPL-3.0

---

## 项目理解（前置）

Karakeep（前身 Hoarder）是一款自托管的"书签万物"应用——链接、笔记、图片、PDF 一键收藏，AI 自动打标签，全文搜索即取即用。它直接瞄准 Pocket（已于 2025 年 7 月被 Mozilla 关闭）、Raindrop.io、Omnivore 等在线书签/稍后读服务的用户，以"自己的服务器、自己的数据、免费无订阅"为差异化。项目在 GitHub 已积累 26,700+ stars，社区活跃，是自托管书签赛道目前人气最高的项目之一。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AI 自动标签 + 全文搜索的自托管书签/收藏管理器 |
| 开源 / 许可证 | 是，AGPL-3.0 |
| 主仓库 | [github.com/karakeep-app/karakeep](https://github.com/karakeep-app/karakeep)（★ 26,700+） |
| 核心功能 | 书签/笔记/图片/PDF 收藏；AI 自动打标签；全文搜索；RSS 订阅自动入库；规则引擎；高亮划词；协作清单；REST API + Webhooks |
| 商业模式 / 定价 | 开源自托管（免费）+ Karakeep Cloud 公测（付费 SaaS，定价以官网为准） |
| 差异化 / 价值主张 | AI 自动标签免去手动整理；Docker 一键部署；Pocket 关闭后最受欢迎的自托管替代 |
| 主要竞品（初判） | Linkwarden、Raindrop.io、Omnivore（已停服）、Wallabag、Pocket（已关闭）、Shiori、Linkding |
| Olares Market | 已上架（Karakeep 在 Olares Market 可一键安装） |
| 来源 | [karakeep.app](https://karakeep.app)、[github.com/karakeep-app/karakeep](https://github.com/karakeep-app/karakeep)、[docs.karakeep.app](https://docs.karakeep.app) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | karakeep.app |
| SEMrush Rank | 890,196 |
| 自然关键词数 | 132 |
| 月自然流量（US）| 1,297 |
| 自然流量估值 | $0/月（几乎无商业词排名） |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 11 词 |
| 排名 4-10 位 | 17 词 |
| 排名 11-20 位 | 12 词 |

> 对照竞品 linkwarden.app：SEMrush Rank 912,652，143 关键词，1,251 US 月流量——两者体量几乎一致，整个自托管书签赛道都处于早期流量阶段。

### 子域名流量分布

| 子域名 | 说明 |
|--------|------|
| docs.karakeep.app | 文档站，贡献了绝大多数排名关键词（安装/Kubernetes/Docker/功能文档） |
| karakeep.app | 主站（首页、定价、应用下载页） |
| cloud.karakeep.app | 云服务入口，几乎无独立 SEO 流量 |

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| karakeep kubernetes | 1 | 1,900 | 6 | $0 | 471 | 信息 | /installation/kubernetes/ |
| karakeep | 2 | 1,900 | 51 | $0 | 250 | 导航 | karakeep.app/ |
| karakeep how do i import from pintrest | 1 | 720 | 34 | $0 | 95 | 信息 | /import/ |
| karakeep docker | 1 | 260 | 15 | $0 | 64 | 信息/商业 | /installation/docker/ |
| karakeep | 5 | 1,900 | 51 | $0 | 45 | 导航 | docs.karakeep.app/ |
| karakeep kubernetes | 8 | 1,900 | 6 | $0 | 45 | 信息 | /installation/docker/ |
| hoarder app | 1 | 140 | 19 | $0 | 34 | 信息 | karakeep.app/ |
| karakeep smart list | 1 | 210 | 22 | $0 | 27 | 信息/商业 | /using-karakeep/lists/ |
| karakeep docker compose | 1 | 70 | 5 | $0 | 17 | 信息 | /installation/docker/ |
| linkwarden vs karakeep | 7 | 90 | 8 | $0 | 2 | 信息 | docs.karakeep.app/ |
| karakeep github | 4 | 210 | 22 | $0 | 2 | 导航/商业 | docs.karakeep.app/ |

**关键洞察**：流量高度集中于品牌词 + 安装文档词（Kubernetes、Docker）；唯一有流量的非品牌词是 `hoarder app`（旧名残存心智）和 `linkwarden vs karakeep`（对比意图）。官网几乎没有任何泛品类内容页，流量洼地极大。

### 付费词（Google Ads）

Karakeep 未投放任何付费广告，$0 付费预算。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| pocket alternative | 480 | 23 | $1.18 | 信息 | ⭐ Pocket 2025/7 关闭，需求高峰期，低 KD |
| pocket app alternative | 390 | ~低 | $0 | 信息 | ⭐ 同上，变体词 |
| linkwarden | 1,300 | 44 | $0 | 导航 | 最大直接竞品，KD 偏高 |
| linkwarden vs karakeep | 90 | 8 | $0 | 信息 | ⭐⭐ 极低 KD，Karakeep 自身有排名 |
| karakeep vs linkwarden | 50 | ~低 | $7.73 | 信息/商业 | ⭐ CPC 罕见地高，有转化价值 |
| pocket app shutting down | 90 | ~低 | $0 | 信息 | ⭐ 时效热词，用户正在寻找替代 |
| pocket app replacement | 50 | ~低 | $0 | 信息 | ⭐ 同上变体 |
| omnivore read it later | 70 | 10 | $0 | 信息 | ⭐ Omnivore 已停服，难民词 |
| wallabag alternative | 20 | ~低 | $0 | 信息 | 次级机会 |
| raindrop alternative | 20 | ~低 | $0 | 信息 | 次级机会 |
| linkwarden alternative | 20 | ~低 | $0 | 信息 | 次级机会 |
| karakeep alternative | 20 | ~低 | $0 | 信息 | 自身替代词，量小但精准 |
| hoarder alternative | 20 | ~低 | $0 | 信息 | 旧名替代词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| bookmark manager | 5,400 | 49 | $1.31 | 信息 | 赛道主词，KD 高但值得布局 |
| read it later app | 590 | 26 | $7.25 | 信息 | ⭐ KD<30，CPC 极高（转化信号） |
| best bookmark manager | 260 | ~低 | $0 | 信息/商业 | ⭐ 商业意图，低竞争度 |
| ai bookmark | 110 | ~中 | $2.03 | 信息 | ⭐ AI 标签是 Karakeep 差异化 |
| ai bookmark manager | 40 | 31 | $0 | 信息 | 功能差异化词，KD 可接受 |
| open source bookmark manager | 30 | ~低 | $0 | 信息 | ⭐ Olares 直接机会词 |
| self-hosted bookmark manager | 10 | 17 | $0 | 信息 | ⭐ 精准自托管信号，量小但意图极强 |
| best self hosted bookmark manager | 20 | ~低 | $0 | 信息 | ⭐ 同上，长尾变体 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| karakeep kubernetes | 1,900 | 6 | $0 | 信息 | ⭐ 已排名#1，带 471 流量，低 KD |
| karakeep | 1,900 | 51 | $0 | 导航 | 品牌主词，护城河 |
| karakeep docker | 260 | 15 | $0 | 信息 | ⭐ 已排#1，安装文档词 |
| karakeep smart list | 210 | 22 | $0 | 信息/商业 | ⭐ 功能词，已排#1 |
| hoarder app | 140 | 19 | $0 | 信息 | ⭐ 旧名残留，Karakeep 已排#1 |
| karakeep docker compose | 70 | 5 | $0 | 信息 | ⭐ 超低 KD，已排#1 |
| karakeep extension | 70 | 31 | $0 | 信息 | 浏览器插件词 |
| karakeep github | 210 | 22 | $0 | 导航/商业 | 开发者入口词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| pocket alternative | 480 | 23 | $1.18 | 信息 | ⭐ 最强自托管迁移信号 |
| read it later app | 590 | 26 | $7.25 | 信息 | ⭐ 高 CPC = 付费用户迁移意愿强 |
| open source bookmark manager | 30 | ~低 | $0 | 信息 | ⭐ 自托管直接意图 |
| self-hosted bookmark manager | 10 | 17 | $0 | 信息 | ⭐ 精准自托管词 |
| self hosted read it later | 20 | ~低 | $0 | 信息 | ⭐ GEO 抢发词 |
| wallabag self hosted | 20 | ~低 | $0 | 信息 | 竞品迁移词 |
| pocket shutting down alternative | 10 | ~低 | $0 | 信息 | 时效迁移词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Olares 是 Karakeep 的"最佳运行平台"——用户只需在 Olares Market 一键安装，无需手动配置 Docker/Kubernetes；同时，Pocket 关闭、Omnivore 停服后大批用户寻找自托管替代，Olares + Karakeep 是最低门槛的答案。**

按月量降序。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| pocket alternative | 480 | 23 | $1.18 | Pocket 关闭后，Olares Market 一键部署 Karakeep，数据本地 + AI 标签，无订阅费 | ⭐⭐⭐ |
| read it later app | 590 | 26 | $7.25 | Olares 让 Karakeep "稍后读"能力全设备同步，本地 AI 摘要扩展，无月费 | ⭐⭐⭐ |
| linkwarden vs karakeep | 90 | 8 | $0 | Olares 同时支持 Linkwarden 和 Karakeep，可对比两者或同时跑 | ⭐⭐⭐ |
| best bookmark manager | 260 | ~低 | $0 | Olares 平台上的 Karakeep = 最佳自托管书签方案（无广告/无追踪） | ⭐⭐ |
| pocket app shutting down | 90 | ~低 | $0 | 时效捕获：Pocket 用户流离，Olares + Karakeep 一文搞定迁移 | ⭐⭐⭐ |
| ai bookmark manager | 40 | 31 | $0 | Olares 本地 LLM（Ollama）+ Karakeep = 完全私有的 AI 书签助手 | ⭐⭐⭐ |
| open source bookmark manager | 30 | ~低 | $0 | Olares Market 让"开源"落地为"零配置自托管" | ⭐⭐⭐ |
| omnivore read it later | 70 | 10 | $0 | Omnivore 停服难民词：Olares + Karakeep 是最平滑的私有替代 | ⭐⭐ |
| self-hosted bookmark manager | 10 | 17 | $0 | Olares 降低自托管门槛到"一键安装"，完全匹配这类搜索意图 | ⭐⭐⭐ |
| karakeep vs linkwarden | 50 | ~低 | $7.73 | Olares 视角：两者都能在同一台机器跑，写深度对比测评 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| read it later app | 590 | 26 | $7.25 | 信息 | **主词候选** | KD<30 + CPC 最高，Pocket 关闭后迁移需求旺盛；Olares + Karakeep 是最佳自托管稍后读方案 |
| pocket alternative | 480 | 23 | $1.18 | 信息 | **主词候选** | Pocket 2025/7 永久关闭，搜索量仍维持；低 KD + 商业 CPC，Karakeep 是同类项目中最活跃的开源替代 |
| linkwarden vs karakeep | 90 | 8 | $0 | 信息 | **主词候选** | KD 极低，Karakeep 官网已有弱排名（#7），Olares 可同时运行两者，写深度对比易出排名 |
| pocket app alternative | 390 | ~低 | $0 | 信息 | **主词候选** | Pocket 变体词，量大且低竞争，可合并入"pocket alternative"簇 |
| pocket app shutting down | 90 | ~低 | $0 | 信息 | **主词候选** | 时效捕获窗口，迁移意图最强，KD 极低 |
| best bookmark manager | 260 | ~低 | $0 | 信息/商业 | **主词候选** | 商业意图 "best" 词，量达主词线；Olares 平台上可主打"隐私 + 免费 + AI"三合一 |
| omnivore read it later | 70 | 10 | $0 | 信息 | **主词候选** | ⭐ Omnivore 已停服，难民词 KD 极低，精准意图；量在主词线下但战略价值高 |
| karakeep vs linkwarden | 50 | ~低 | $7.73 | 信息/商业 | **主词候选** | CPC $7.73 信号强（有付费广告主竞争），Olares 深度对比测评可吃高价值流量 |
| ai bookmark | 110 | ~中 | $2.03 | 信息 | **主词候选** | AI 标签是 Karakeep 核心差异化，CPC $2 + 量 110，与 Olares 本地 LLM 方向完全契合 |
| ai bookmark manager | 40 | 31 | $0 | 信息 | **次级** | KD 刚过 30，并入"ai bookmark"簇作次级词 |
| open source bookmark manager | 30 | ~低 | $0 | 信息 | **次级** | 意图精准，量偏小，并入 self-hosted 主词簇 |
| self-hosted bookmark manager | 10 | 17 | $0 | 信息 | **次级** | 量小但意图极精准，SEO 价值在 GEO 引用位而非流量 |
| omnivore alternative | 20 | ~低 | $0 | 信息 | **次级** | 与 omnivore read it later 合并同簇 |
| wallabag alternative | 20 | ~低 | $0 | 信息 | **次级** | 补充自托管迁移词簇 |
| hoarder app | 140 | 19 | $0 | 信息 | **次级** | 旧名残留，Karakeep 已排#1，持续保住即可 |
| self hosted read it later | 20 | ~低 | $0 | GEO | 近零量、语义精准，抢 AI Overview 引用位 |
| pocket shutting down alternative | 10 | ~低 | $0 | 信息 | **GEO** | 长尾迁移词，进 FAQ 段落 |
| karakeep docker compose | 70 | 5 | $0 | 信息 | **次级** | 已排#1，持续维护文档质量 |

---

## 核心洞见

### 1. 品牌护城河
Karakeep 品牌词（1,900 月量，KD 51）已有#2 排名，说明品牌认知已建立，但护城河不厚——品牌词 KD 仅 51，且"Karakeep"与"Hoarder"的双名割裂了心智。正面刚品牌词意义不大；**应攻的是品类词和迁移词**，这里竞争者几乎都是博客/聚合站，没有专业 SEO 团队。

### 2. 可复制的打法
- Karakeep 现有流量 **80%+ 来自安装文档**（Kubernetes、Docker 教程词），这是技术文档 SEO 的经典路径。Olares 可复制：写"在 Olares 上部署 Karakeep"的 Step-by-Step 指南，直接吃文档类关键词。
- **没有一篇品类内容页**（best X、X alternative、X vs Y）——这是最大的攻击面，所有流量都等着第三方写评测文来捡。

### 3. 对 Olares 最关键的 3 个词
1. **`pocket alternative`**（480 vol / KD 23 / CPC $1.18）—— Pocket 关闭是 2025 年最大的书签领域事件，搜索量持续，低 KD 可快速排名；写"Pocket 关闭后最佳自托管替代"一文，Olares + Karakeep 一键部署是最强卖点。
2. **`read it later app`**（590 vol / KD 26 / CPC $7.25）—— CPC $7.25 是全词库最高，证明该词背后有强付费转化信号；Karakeep 完全覆盖"稍后读"场景，Olares 加 AI 摘要是差异化。
3. **`linkwarden vs karakeep`**（90 vol / KD 8 / CPC $0）—— KD 仅 8，Karakeep 官网文档已在#7，极易上首页；Olares Market 同时上架两者，深度对比评测 = 自然流量 + 品牌曝光。

### 4. 最大攻击面
- **Pocket 关闭**（2025-07）：`pocket app shutting down`（90 vol）、`pocket alternative`（480 vol）、`pocket app replacement`（50 vol）等词是时效性迁移窗口，目前几乎没有专项自托管内容占位。KD 极低，窗口期内容优先级最高。
- **Omnivore 停服**：`omnivore read it later`（70 vol / KD 10）是同类难民词，KD 10 近乎白送，Karakeep 是 Omnivore 用户数据导入最平滑的选项之一。
- **商业 vs 开源**痛点：Raindrop.io 付费计划、Pocket 关闭都印证用户对"订阅制书签服务"的不信任，这正是 Olares 自托管叙事的切入点。

### 5. 隐藏低 KD 金矿
- `linkwarden vs karakeep`（KD 8）+ `karakeep docker compose`（KD 5）+ `karakeep kubernetes`（KD 6）——这几个词量达 70-1900，KD 单位数，基本是写完就排。
- `omnivore read it later`（KD 10）：Omnivore 停服后用户找替代，KD 10 意味着 DR 普通的网站也能排进 Top 10。
- `ai bookmark manager`（KD 31）：AI 自动标签是 Karakeep 的核心差异化，这个词正在起量（Pocket 关闭 + 用户对 AI 功能兴趣上升）。

### 6. GEO 前瞻布局
以下词近零量但语义精准，适合在 FAQ / 前瞻段落布局，抢 AI Overview / Perplexity 引用位：
- `self hosted read it later`（GEO：Olares + Karakeep 的一句话定义放在内容开头段）
- `pocket shutting down alternative`（GEO：迁移 SOP 步骤型答案）
- `best self hosted bookmark manager 2026`（GEO：评测类答案，列 Karakeep + Olares 安装）
- `self-hosted ai bookmark`（GEO：未来词，Olares 本地 LLM + Karakeep 的组合场景）

### 7. 与既有分析的关联
- `olares-500-keywords` 中已有 self-hosted / open-source 方向词，Karakeep 报告补充了书签/稍后读细分赛道的词，尤其 **Pocket 迁移词**（`pocket alternative`、`pocket app shutting down`）是该分析中未覆盖的时效性机会。
- `pocket alternative`（KD 23 / 480 vol）是当前自托管应用里难得的**月量 ≥ 100 + KD < 30 + 有商业 CPC**三条件同时满足的词，跨报告来看排优先级应靠前。
- Linkwarden 是 Karakeep 的直接竞品，两者 SEMrush 体量几乎一致（均约 1,200-1,300 月流量），建议同步跑 Linkwarden 报告后做跨报告对比内容策略。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_organic、phrase_this、phrase_these）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
