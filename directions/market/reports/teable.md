# Teable SEO 竞品分析报告

> 域名：teable.ai（主域）/ teable.io（营销页） | SEMrush US | 2026-07-06
> Teable 是 PostgreSQL 原生的开源 Airtable 替代品，2.0 版本定位为 AI Database Agent，AGPL 社区版免费自托管，付费版解锁 AI 字段与企业自动化。

---

## 项目理解（前置）

Teable 由 teableio 团队于 2022 年创建，核心卖点是"真正的 Postgres"：数据直接存入标准 SQL 表，而非在数据库上建一层抽象——这意味着任何 Postgres 工具都可以直接读写 Teable 数据，同时支持百万行级性能、实时协作、REST API、多视图与自动化流程。GitHub 仓库 `teableio/teable` 现有 **~21K stars**，主要语言 TypeScript，最新发布于 2026-05-25（release.2026-05-22）。2.0 版本将定位从"电子表格数据库"升级为"AI Database Agent"，主站迁至 teable.ai，并新增 AI 字段/AI Chat/App Builder 功能。商业模式为 SaaS（teable.ai）+ 开源自托管双轨：社区版 AGPL 免费；企业版含 AI、权限矩阵、高级自动化，需付费（定价见 teable.ai/pricing）。目标用户为重视数据可迁移性与 Postgres 生态兼容的开发者团队、中小企业和希望 Airtable 自托管替代的个人。

来源：[GitHub teableio/teable](https://github.com/teableio/teable)、[teable.ai](https://teable.ai)、[ossalt.com/guides](https://ossalt.com/guides/how-to-self-host-teable-modern-airtable-alternative-2026)

| 项目 | 内容 |
|------|------|
| 一句话定位 | PostgreSQL 原生的开源 Airtable 替代 / AI Database Agent |
| 开源 / 许可证 | 是，AGPL-3.0（Community Edition）；Enterprise Edition 闭源付费 |
| 主仓库 | [github.com/teableio/teable](https://github.com/teableio/teable)（~21K ★） |
| 核心功能 | 真 Postgres 存储、实时协作、多视图（Grid/Kanban/Calendar/Form/Gallery）、REST API、自动化、AI 字段（付费）、App Builder（2.0） |
| 商业模式 / 定价 | 社区版免费自托管；SaaS 免费套餐（200 credits）；Business 版含 AI 功能，定价见官网 |
| 差异化 / 价值主张 | 数据直接存标准 Postgres 表（可 JOIN 任意 PG 工具）；百万行性能；2.0 AI-native 转型；vs NocoDB 更现代 UI，vs Baserow 无行数限制 |
| 主要竞品（初判）| NocoDB、Baserow、Airtable（SaaS）、APITable/Apitable |
| Olares Market | ⬜ 未上架（`directions/market/apps.md` 当前为 ⬜） |
| 来源 | [teable.ai](https://teable.ai)、[GitHub README](https://github.com/teableio/teable/blob/develop/README.md)、[cloudzy 对比](https://cloudzy.com/blog/best-self-hosted-airtable-alternatives/) |

---

## 流量基线（Phase 1）

> **注意**：Teable 有两个域名——`teable.io`（营销主页，几乎无 SEO 权重）和 `teable.ai`（产品主域，实际流量所在）。以下数据以 `teable.ai` 为准，并附 teable.io 说明。

### 概览

| 指标 | 数据 |
|------|------|
| 主域名 | teable.ai（产品主域） |
| SEMrush Rank | 741,845 |
| 自然关键词数 | 101 |
| 月自然流量（US）| 1,679 |
| 自然流量估值 | $1,553/月 |
| 付费关键词数 | 2 |
| 月付费流量 | 21 |
| 付费流量成本 | $18/月 |
| 排名 1-3 位 | 3 词 |
| 排名 4-10 位 | 6 词 |
| 排名 11-20 位 | 1 词 |
| — | — |
| teable.io（营销页）| SEMrush Rank 19,672,207；6 个词；流量 ≈ 0 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| teable.ai | 74 | 1,565 | 93.2% |
| help.teable.ai | 21 | 114 | 6.8% |
| app.teable.ai | 2 | 0 | 0% |
| community.teable.ai | 3 | 0 | 0% |
| dev.teable.ai | 1 | 0 | 0% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| teable | 1 | 1,900 | 50 | $0.94 | 1,520 | 导航 | teable.ai |
| chatable ai | 9 | 4,400 | 38 | $0.61 | 105 | 信息 | help.teable.ai/en/basic/ai/ai-chat |
| teblee（品牌误拼）| 5 | 390 | 12 | $0.91 | 17 | 信息 | teable.ai |
| teable github | 2 | 170 | 25 | $0 | 4 | 导航/信息 | teable.ai |
| teabl（品牌误拼）| 1 | 30 | 17 | $0.91 | 3 | 信息 | teable.ai |
| table ai | 6 | 70 | 45 | $7.09 | 2 | 信息 | teable.ai |
| teatable | 4 | 140 | 35 | $0.74 | 1 | 导航/信息 | teable.ai |
| airtable to postgres | 21 | 50 | 10 | $0 | 0 | 信息 | blog.teable.io |
| airtable postgres | 15 | 70 | 17 | $0 | 0 | 信息 | blog.teable.io |

> **关键发现**：1,679 月流量中，1,520（90.5%）来自品牌词 `teable` 自身排名第 1。`chatable ai` 排名第 9 带来 105 次流量，实为语义近邻误捡（help.teable.ai 的 AI Chat 功能页被这个词抓到）。Teable 在任何品类词上均无排名。

### 付费词（Google Ads）

Teable 正在小规模投放自有品牌词，付费规模极小（$18/月）。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| teable | 2 | 1,600 | $0.91 | teable.ai |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| airtable alternatives | 1,000 | 17 | $8.03 | 信息 | ⭐ KD=17，Teable/NocoDB/Baserow 都在抢 |
| airtable competitors | 480 | 23 | $9.45 | 信息 | ⭐ CPC 极高，商业意图强 |
| airtable alternative | 320 | 18 | $7.23 | 信息 | ⭐ 核心品类词，Teable 目前未排名 |
| apitable | 320 | 28 | $0 | 导航 | ⭐ 同品类竞品，中国团队 |
| alternatives to airtable | 210 | 16 | $8.53 | 信息 | ⭐ KD=16！全场最低竞争对比词 |
| airtable vs | 210 | 24 | $8.71 | 信息 | ⭐ 系列对比词入口 |
| nocodb | 2,400 | 44 | $7.05 | 导航 | 直接竞品，已有报告 |
| baserow | 2,400 | 40 | $8.82 | 导航 | 直接竞品 |
| airtable vs baserow | 30 | 6 | $5.56 | 信息 | ⭐⭐⭐ KD=6！极低竞争对比词 |
| teable vs nocodb | 0 | 0 | $0 | — | GEO 前哨，用户开始问但量未起 |
| teable vs baserow | 0 | 0 | $0 | — | GEO 前哨 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| spreadsheet database | 260 | 26 | $8.42 | 信息 | ⭐ Teable 核心形态词 |
| free database app | 260 | 25 | $2.03 | 信息/商业 | ⭐ 自托管免费定位契合 |
| back end databases no code | 210 | 16 | $0 | 信息/商业 | ⭐⭐ KD 极低 |
| best database software for startups | 210 | 18 | $0 | 信息 | ⭐⭐ 低 KD + 商业意图 |
| best database softwares | 320 | 26 | $8.77 | 信息 | ⭐ 泛需求词 |
| open source airtable | 90 | 30 | $5.54 | 信息 | ⭐ 直接需求词 |
| airtable open source | 70 | 25 | $5.79 | 信息 | ⭐ 同义变体 |
| open source airtable alternative | 50 | 18 | $4.49 | 信息 | ⭐ 精准需求词 |
| airtable postgres | 50 | 12 | $2.46 | 信息 | ⭐⭐ KD=12！Teable 正好契合 |
| airtable self hosted | 40 | 18 | $3.67 | 信息 | ⭐ 精准需求 |
| self hosted airtable | 40 | 18 | $4.78 | 信息 | ⭐ 同义变体 |
| airtable clone | 20 | 0 | $6.40 | — | ⭐ 量小但 CPC 高，商业意图 |
| airtable alternative self hosted | 20 | 0 | $0 | — | ⭐ Teable 的精准客群词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| teable | 1,900 | 50 | $0.94 | 导航 | 主品牌词，pos 1，但 KD=50 护城河中等 |
| teable github | 170 | 25 | $0 | 导航/信息 | 开发者入口词 |
| teable pricing | 0 | 0 | $17.30 | — | CPC 极高说明购买意图，量未起 |
| teable api | 10 | 0 | $13.90 | 信息 | 开发者集成词，CPC 高 |
| teable review | 0 | 0 | $0 | — | GEO 前哨 |
| teable mcp | 0 | 0 | $0 | — | GEO 前哨，MCP 新兴词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted apps | 260 | 38 | $3.85 | 信息 | 泛自托管需求 |
| airtable self hosted | 40 | 18 | $3.67 | 信息 | ⭐ 精准需求 |
| self hosted airtable | 40 | 18 | $4.78 | 信息 | ⭐ 精准需求变体 |
| open source airtable alternative | 50 | 18 | $4.49 | 信息 | ⭐ |
| airtable alternative self hosted | 20 | 0 | $0 | — | ⭐ Olares 一键部署 Teable 的精准词 |
| no code database open source | 20 | 0 | $0 | — | ⭐ |
| airtable to postgres | 50 | 10 | $0 | 信息 | ⭐⭐ KD=10，Teable 博客已排名但未吃到流量 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Teable 是 Olares Market 的高价值缺口——PostgreSQL 原生自托管电子表格，Olares 一键部署解决用户"想要 Airtable 自托管但配置太复杂"的痛点，同时 Teable 的 AI 功能（AI 字段/AI Chat）可用 Olares 本地 LLM 驱动。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| airtable alternatives | 1,000 | 17 | $8.03 | ⭐⭐⭐ KD=17，Olares Market 可以 "Airtable alternatives you can self-host" 为角度，Teable/NocoDB 双上架 |
| airtable alternative | 320 | 18 | $7.23 | ⭐⭐⭐ 同上，核心品类词 |
| alternatives to airtable | 210 | 16 | $8.53 | ⭐⭐⭐ KD=16，全场最低 KD 的对比词，Olares 做"10 best Airtable alternatives you can self-host" |
| airtable competitors | 480 | 23 | $9.45 | ⭐⭐ CPC 极高，Olares 自托管竞品对比页切入 |
| spreadsheet database | 260 | 26 | $8.42 | ⭐⭐ Teable on Olares = 自有 spreadsheet database，无月费 |
| airtable postgres | 50 | 12 | $2.46 | ⭐⭐⭐ KD=12，Teable 博客排名但无流量，Olares 可以"Teable + Postgres on Olares" 教程抢 |
| airtable self hosted | 40 | 18 | $3.67 | ⭐⭐ Olares 一键自托管 Airtable 替代，直接落地 |
| self hosted airtable | 40 | 18 | $4.78 | ⭐⭐ 同义变体 |
| open source airtable alternative | 50 | 18 | $4.49 | ⭐⭐ Teable on Olares，AGPL 真正开源 |
| airtable alternative self hosted | 20 | 0 | $0 | ⭐⭐⭐ 量小但 KD=0，超精准词，Olares 一页即可 |
| airtable vs baserow | 30 | 6 | $5.56 | ⭐⭐⭐ KD=6 全场最低！加入 Teable 三方对比，Olares 一键部署全家桶 |
| airtable to postgres | 50 | 10 | $0 | ⭐⭐ Teable 博客已在排名但零流量，Olares 可以 "Migrate Airtable to Teable on Olares" 抢 |
| teable self hosted | 0 | 0 | $0 | ⭐⭐⭐ GEO 前哨，Olares 最直接的 install/deploy 词 |
| teable vs nocodb | 0 | 0 | $0 | ⭐⭐ GEO 前哨，对比词早布局 |
| teable docker | 0 | 0 | $0 | ⭐⭐ GEO 前哨，Olares 简化 docker 部署 |
| teable mcp | 0 | 0 | $0 | ⭐ GEO 前哨，AI 新兴词 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|----|------|------|--------------------------|
| airtable alternatives | 1,000 | 17 | $8.03 | 信息 | 主词候选 | KD=17 + 月量 1K + CPC $8，首选主词；Olares "top Airtable alternatives you can self-host"，Teable 为核心案例 |
| airtable competitors | 480 | 23 | $9.45 | 信息 | 主词候选 | CPC 极高商业意图，KD 可接受；与 "airtable alternatives" 同簇 |
| airtable alternative | 320 | 18 | $7.23 | 信息 | 主词候选 | 核心品类单数形，与上两词同主题簇 |
| alternatives to airtable | 210 | 16 | $8.53 | 信息 | 次级 | KD=16 全场最低，并入替代词簇 |
| spreadsheet database | 260 | 26 | $8.42 | 信息 | 主词候选 | 量 260 + KD 26 + CPC $8.42，Teable on Olares 教程/对比文的主词 |
| open source airtable alternative | 50 | 18 | $4.49 | 信息 | 次级 | 量小但精准，并入 alternatives 簇 |
| airtable postgres | 50 | 12 | $2.46 | 信息 | 次级 | KD=12 低竞争，Teable 差异化技术词，blog 教程适合 |
| airtable self hosted | 40 | 18 | $3.67 | 信息 | 次级 | 精准自托管需求词，并入 alternatives 簇 |
| self hosted airtable | 40 | 18 | $4.78 | 信息 | 次级 | 同义变体，同簇 |
| airtable open source | 70 | 25 | $5.79 | 信息 | 次级 | 另一变体，KD 可打 |
| airtable vs baserow | 30 | 6 | $5.56 | 信息 | 次级 | ⭐⭐⭐ KD=6 全场最低！并入对比词，扩展为三方（含 Teable）对比 |
| airtable alternative self hosted | 20 | 0 | $0 | — | 次级 | 量极小但精准，进 FAQ 段 |
| airtable to postgres | 50 | 10 | $0 | 信息 | 次级 | Teable 技术差异化词，KD=10，迁移教程用 |
| teable | 1,900 | 50 | $0.94 | 导航 | — | 品牌导航词，pos 1 已守住，KD=50 排不动暂不算主词 |
| teable github | 170 | 25 | $0 | 导航/信息 | 次级 | 开发者入口，品牌词聚 |
| teable self hosted | 0 | 0 | $0 | — | GEO | 量零但语义精准，Olares deploy Teable 页首选 GEO 词 |
| teable vs nocodb | 0 | 0 | $0 | — | GEO | 对比类问题，进 FAQ |
| teable pricing | 0 | 0 | $17.30 | — | GEO | CPC $17 说明强购买意图，量起前抢 GEO 位 |
| teable mcp | 0 | 0 | $0 | — | GEO | Agent/MCP 新兴词，Olares + Teable MCP 前哨 |
| airtable clone | 20 | 0 | $6.40 | — | GEO | CPC $6.4 + 量小，搜索者在做选型，进对比文 FAQ |

---

## 核心洞见

1. **品牌护城河**：Teable 品牌词 `teable` 月量 1,900、KD=50、pos 1——护城河中等偏弱（KD 不高说明市场还没形成强竞争），且 90% 的流量依赖这一个词，品牌认知极度集中。Semrush 找到的"竞品"几乎全是品牌误拼噪音（usetable.ai、theaitable.org），说明 Teable 在 SEO 生态里还是孤岛。**结论：目前难以正面刚其品牌词，但品类词完全是空白地带**。

2. **可复制的打法**：Teable 自己没有任何程序化落地页、没有品类词布局（`airtable alternative` 无排名）、博客文章排名但无流量（`airtable postgres` 排名 15 位但流量 0）。**可复制打法：品类对比文**——Teable 的对手（NocoDB、Baserow）自己也没占住 `airtable alternatives`（KD=17），这是整个品类的集体缺失，Olares 可以用"X best Airtable alternatives you can self-host" 系列文切入。

3. **对 Olares 最关键的词**：
   - `airtable alternatives`（1,000/mo，KD 17，CPC $8）：月量最高 + KD 最低的主词，Teable on Olares 可作核心案例
   - `airtable vs baserow`（30/mo，KD **6**）：KD 超低对比词，可以扩展成三方对比（Teable vs NocoDB vs Baserow on Olares）
   - `airtable postgres`（50/mo，KD **12**）：Teable 技术差异化词，Olares + Teable 教程可占位

4. **最大攻击面**：Airtable 本身有明显定价痛点（免费版仅 1,200 行、付费 $20/用户/月），但搜索者用 `airtable alternatives`（$8.03 CPC）、`airtable competitors`（$9.45 CPC）来表达这个痛点——CPC 极高证明商业意图强。Teable 自己没有写"为什么不用 Airtable"的内容，Olares 可以从"Airtable 太贵、数据不归你"切入。

5. **隐藏低 KD 金矿**：
   - `airtable vs baserow`（KD=6）：全表最低竞争对比词，三工具一起讲
   - `alternatives to airtable`（KD=16）：与 "airtable alternatives" 同义但更口语，KD 更低
   - `back end databases no code`（KD=16，210/mo）：Teable 精确覆盖这个场景但无人排名
   - `best database software for startups`（KD=18，210/mo）：用量+KD 完美，Teable on Olares 的创业团队 story
   - `airtable to postgres`（KD=10，50/mo）：技术迁移词，Teable 博客有文章但流量为 0，空手可抢

6. **GEO 前瞻布局**：`teable self hosted`、`teable vs nocodb`、`teable pricing`（CPC $17 购买意图极强）、`teable mcp`——这些词量几乎为 0 但 CPC/语义信号明确，用户在 AI Overview/Perplexity 里已经在问，进 FAQ 段可提前抢引用位。`teable mcp` 对应 Olares Agent-Native OS 叙事，Teable 作为 Agent tool 的故事。

7. **与既有 olares-500-keywords 的关联**：本次最有价值的补充是**Airtable 替代品这一垂类的品类词集群**（`airtable alternatives`/`alternative`/`alternatives to airtable`，合计 1,530/mo，KD 均在 16-18），以及**KD 极低的自托管方向**（`airtable self hosted`/`self hosted airtable`，共 80/mo，KD=18）。这些词在 NocoDB 报告中已提及但未完整覆盖——Teable 与 NocoDB 可联合写一篇 "best open source Airtable alternatives for self-hosting" 覆盖整个簇。**与 NocoDB 报告的差异**：NocoDB 是已在 Olares Market 上架的应用，Teable 尚未上架——上架后机会词 `teable self hosted`（KD=0）、`teable docker` 的 Olares 版教程可以直接 rank。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related、phrase_questions、resource_adwords）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
