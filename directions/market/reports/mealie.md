# Mealie SEO 竞品分析报告

> 域名：mealie.io | SEMrush US | 2026-07-06
> 自托管食谱管理器领域的开源领军者，Paprika 等付费 app 的免费自托管替代首选。

---

## 项目理解（前置）

Mealie 是一款自托管食谱管理与膳食计划应用，后端基于 Python（FastAPI），前端为 Vue，通过 REST API 暴露全部数据，并支持从任意网址一键抓取导入食谱。项目定位"现代家庭食谱管理"，目标用户是希望把食谱从 Paprika、RecipeKeeper 等付费 app 或分散网页迁移到自己服务器的家庭用户和 HomeLab 爱好者。核心差异化在于：完全自托管 + 开放 API + 购物清单自动聚合 + Home Assistant 集成，且永久免费——直接打 Paprika（$4.99 买断、无自托管）的付费痛点。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自托管食谱管理器与膳食计划工具，Docker 一键部署 |
| 开源 / 许可证 | 是，AGPL-3.0 |
| 主仓库 | https://github.com/mealie-recipes/mealie（★ 12,600+） |
| 核心功能 | URL 抓取导入食谱、膳食计划、购物清单、多用户 / 家庭组、OpenAI 集成、Home Assistant webhook、REST API |
| 商业模式 / 定价 | 完全免费自托管；无云版、无付费订阅 |
| 差异化 / 价值主张 | 数据完全自有、开放 API 可对接 Agent / HA、永久免费替代付费食谱 app |
| 主要竞品（初判）| Paprika（付费 app）、Tandoor（开源）、RecipeKeeper（付费）、CookLang |
| Olares Market | 已上架（⬜ 待调研状态，本报告填补） |
| 来源 | https://mealie.io / https://github.com/mealie-recipes/mealie / https://docs.mealie.io |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | mealie.io |
| SEMrush Rank | 418,621 |
| 自然关键词数 | 164 |
| 月自然流量（US）| 3,605 |
| 自然流量估值 | $7,000/月 |
| 付费关键词数 | 0（无投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 20 词 |
| 排名 4-10 位 | 21 词 |
| 排名 11-20 位 | 20 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| mealie.io | 38 | 3,117 | 86.5% |
| docs.mealie.io | 119 | 456 | 12.6% |
| demo.mealie.io | 7 | 32 | 0.9% |

> docs 子域名承载了绝大多数关键词但流量占比仅 12.6%——安装/配置文档词量多但搜索量小，主站靠品牌词撑流量。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| mealie | 1 | 3,600 | 34 | $2.37 | 2,880 | 导航 | mealie.io/ |
| mealie docker | 1 | 210 | 24 | $0 | 168 | 信息 | docs: installation-checklist |
| mealie docker compose | 1 | 210 | 16 | $0 | 168 | 信息 | docs: installation-checklist |
| mealie app | 1 | 110 | 47 | $1.27 | 88 | 信息 | mealie.io/ |
| meali（拼写变体） | 1 | 70 | 22 | $0 | 56 | 导航 | mealie.io/ |
| mealie openai | 1 | 70 | 26 | $0 | 56 | 信息 | docs: ai-providers |
| mealie meal | 2 | 390 | 28 | $0 | 51 | 信息 | mealie.io/ |
| mealie login | 1 | 40 | 6 | $0 | 32 | 导航 | demo.mealie.io/ |
| self hosted recipe manager | 2 | 170 | 9 | $0 | 22 | 信息 | docs.mealie.io/ |
| mealio（变体） | 2 | 140 | 40 | $1.72 | 18 | 信息 | mealie.io/ |
| mealee（拼写变体） | 1 | 70 | 22 | $0.14 | 17 | 信息 | mealie.io/ |
| self hosted recipe app | 2 | 70 | 15 | $0 | 9 | 信息 | docs.mealie.io/ |
| mealie github | 2 | 210 | 34 | $0 | 5 | 导航 | docs.mealie.io/ |
| open source recipe manager | 3 | 40 | 32 | $0 | 2 | 信息 | docs.mealie.io/ |
| swag reverse proxy | 4 | 70 | 15 | $0 | 4 | 信息 | docs: community-guide/swag |
| mealie port | 1 | 70 | 21 | $0 | 1 | 信息 | docs: installation |
| recipe scaling app | 16 | 30 | 22 | $1.86 | 0 | 信息 | mealie.io/ |

### 付费词（Google Ads）

无投放——Mealie 是纯社区/开源项目，0 付费关键词。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| paprika alternative | 1,600 | 22 | $0.01 | 信息 | ⭐ Paprika 最大的付费痛点词；KD 低量大 |
| paprika recipe manager | 2,400 | 46 | $1.11 | 商业 | 高 KD，可作次级 |
| tandoor recipes | 720 | 28 | $0.31 | 信息 | ⭐ Tandoor 是 Mealie 的同类开源对手 |
| tandoor recipe | 320 | 26 | $0.31 | 信息 | ⭐ 同上变体 |
| mealie vs tandoor | 110 | 1 | $0 | 信息/其它 | ⭐ 超低 KD 对比词，直接可攻 |
| recipe keeper alternative | 20 | 0 | $0 | — | 次级，RecipeKeeper 用户迁移意图 |
| mealie alternative | 20 | 0 | $0 | — | 次级，反向防守 |
| grocy alternative | 10 | 0 | $0 | — | GEO，家庭自托管工具切换意图 |
| nextcloud cookbook alternative | 20 | 0 | $0 | — | GEO，迁移 Nextcloud 用户 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| recipe organizer app | 480 | 55 | $1.14 | 信息 | 高 KD，次级 |
| recipe box app | 260 | 43 | $1.26 | 信息 | 次级 |
| recipe management app | 50 | 35 | $2.73 | 信息 | 次级 |
| recipe collection app | 50 | 43 | $1.30 | 信息 | 次级 |
| open source recipe manager | 40 | 32 | $0 | 信息 | ⭐ 接近低 KD 边界，Mealie 已排名 #3 |
| recipe manager app | 140 | 30 | $1.33 | 信息 | ⭐ 边界，商业意图有 CPC |
| recipe software | 320 | 34 | $1.44 | 信息 | 次级 |
| recipe database | 260 | 44 | $1.40 | 信息 | 次级 |
| recipe saver app | 480 | 71 | $1.34 | 信息 | KD 太高，跳过 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| mealie docker compose | 210 | 16 | $0 | 信息 | ⭐ 已排名 #1；安装教程词 |
| mealie docker | 210 | 24 | $0 | 信息 | ⭐ 已排名 #1 |
| mealie openai | 70 | 26 | $0 | 信息 | ⭐ AI 集成词，新兴上升 |
| mealie meal | 390 | 28 | $0 | 信息 | ⭐ 量最大的非品牌功能词 |
| home assistant mealie | 20 | 0 | $0 | 信息 | ⭐ HA 集成词，GEO |
| mealie self hosted | 20 | 0 | $0 | 信息 | ⭐ 自托管定位词，GEO |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted recipe manager | 170 | 9 | $0 | 信息 | ⭐ Mealie 已排名 #2；KD 9 极低 |
| self hosted recipe app | 70 | 15 | $0 | 信息 | ⭐ 同类低 KD 词 |
| online recipe book | 590 | 27 | $1.50 | 信息 | ⭐ 自托管≈私有在线食谱书 |
| personal recipe book | 590 | 25 | $1.34 | 其它 | ⭐ 私人食谱存档意图 |
| meal planner self hosted | 20 | 0 | $0 | — | GEO |
| open source meal planner | 20 | 0 | $0 | — | GEO |
| recipe manager docker compose | 20 | 0 | $0 | — | GEO，安装教程意图 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Mealie 是 Olares Market 已上架的自托管食谱应用，Olares 让"一键部署 Mealie"成为可能，打 Paprika/RecipeKeeper 的付费+数据不自有痛点。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| paprika alternative | 1,600 | 22 | $0.01 | Mealie on Olares = 免费、自托管、数据不出门的 Paprika 替代；Olares Market 一键安装 | ⭐⭐⭐ |
| self hosted recipe manager | 170 | 9 | $0 | Olares 是运行 Mealie 最简单的方式，无需手动管 Docker | ⭐⭐⭐ |
| mealie vs tandoor | 110 | 1 | $0 | 对比文：Olares Market 同时收录两者，可帮用户选择或并行使用 | ⭐⭐⭐ |
| online recipe book | 590 | 27 | $1.50 | Mealie on Olares = 私有在线食谱书，随时随地访问且数据自有 | ⭐⭐ |
| personal recipe book | 590 | 25 | $1.34 | 同上；强调"你的食谱永远属于你"叙事与 Olares 品牌契合 | ⭐⭐ |
| tandoor recipes | 720 | 28 | $0.31 | Tandoor 用户可在 Olares 上同时跑 Mealie（对比/共存内容） | ⭐⭐ |
| self hosted recipe app | 70 | 15 | $0 | Olares Market 直接机会词；教程文切入 | ⭐⭐⭐ |
| home assistant mealie | 20 | 0 | $0 | Mealie + Home Assistant 在 Olares 上联动（HA 亦在 Market 中） | ⭐⭐ |
| mealie self hosted | 20 | 0 | $0 | GEO：Olares 作为 Mealie 的理想自托管平台 | ⭐⭐ |
| mealie docker compose | 210 | 16 | $0 | 教程词；Olares 让用户不需要手写 docker-compose | ⭐⭐ |
| open source meal planner | 20 | 0 | $0 | GEO 前哨：Olares Market 含 Mealie 膳食计划功能 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| paprika alternative | 1,600 | 22 | $0.01 | 信息 | **主词候选** | 全场最大机会：量大 KD 低，Paprika 付费且无自托管，Mealie on Olares 是完美替代；可写独立对比文 |
| self hosted recipe manager | 170 | 9 | $0 | 信息 | **主词候选** | Mealie 已排名 #2，KD 仅 9；Olares 部署教程能吃到这个词的长尾流量 |
| mealie vs tandoor | 110 | 1 | $0 | 信息 | **主词候选** | KD=1 近似零难度；Olares Market 同时支持两者，写对比文直接落地 |
| online recipe book | 590 | 27 | $1.50 | 信息 | **主词候选** | KD 27 量 590；私有在线食谱书叙事与 Olares"数据自有"品牌完全契合 |
| personal recipe book | 590 | 25 | $1.34 | 其它 | **主词候选** | 同上；两词可合并一篇文 |
| tandoor recipes | 720 | 28 | $0.31 | 信息 | **主词候选** | Tandoor 是开源竞品，量 720 KD 28；可写"Mealie vs Tandoor on Olares" |
| mealie docker compose | 210 | 16 | $0 | 信息 | 次级 | 已排名 #1；Olares 免 docker-compose 安装教程可引用 |
| self hosted recipe app | 70 | 15 | $0 | 信息 | 次级 | KD 15 低；与 self hosted recipe manager 合并写 |
| recipe software | 320 | 34 | $1.44 | 信息 | 次级 | KD 34 略高；并入品类文作次级词 |
| open source recipe manager | 40 | 32 | $0 | 信息 | 次级 | Mealie 已排名 #3；并入 self-hosted 文 |
| mealie openai | 70 | 26 | $0 | 信息 | 次级 | AI 集成词；Olares 本地 LLM 叙事补充词 |
| home assistant mealie | 20 | 0 | $0 | 信息 | GEO | HA + Mealie 在 Olares 联动场景，抢 AI Overview 引用位 |
| mealie self hosted | 20 | 0 | $0 | 信息 | GEO | Olares 作为 Mealie 自托管平台的精准 GEO 词 |
| meal planner self hosted | 20 | 0 | $0 | 信息 | GEO | 膳食计划自托管场景词 |
| open source meal planner | 20 | 0 | $0 | 信息 | GEO | 同上，进 FAQ 段 |
| recipe keeper alternative | 20 | 0 | $0 | 信息 | GEO | RecipeKeeper 迁移意图；Mealie on Olares 作替代 |

---

## 核心洞见

1. **品牌护城河**：Mealie 品牌词（"mealie"，3,600 vol，KD 34）牢固——它自己排名 #1，没有品牌混战。对 Olares 没有直接冲击；我们不该拿品牌词打，而是占非品牌长尾。

2. **可复制的打法**：Mealie 的流量几乎 100% 靠品牌词和极少数安装词（docker compose/port），没有任何内容矩阵——这是最大的空档。竞品类（paprika alternative 1,600 vol）和品类类（online recipe book 590 vol，personal recipe book 590 vol）完全无人深耕，直接可切入。

3. **对 Olares 最关键的词**：
   - **paprika alternative**（1,600 / KD 22）——量最大、竞争最低、付费痛点最明确的机会词。
   - **self hosted recipe manager**（170 / KD 9）——Mealie 已站上 #2，Olares 教程文可一起吃这个词。
   - **mealie vs tandoor**（110 / KD 1）——KD 近似零，对比文写了就能排，Olares Market 同时支持两者是天然叙事。

4. **最大攻击面**：Paprika 是最大攻击对象——$4.99 买断、数据不导出、无 API、无自托管。"paprika alternative" KD 22 意味着任何有一定 DA 的站写好这篇文都能进前 10。Olares + Mealie = 免费 + 随处访问 + 数据自有，三点直打 Paprika 痛点。

5. **隐藏低 KD 金矿**：`self hosted recipe manager`（KD 9）和 `self hosted recipe app`（KD 15）是两个极低竞争词，Mealie 已在其中排名 #2；一篇专门的 Olares 部署教程能稳固并提升这两个词的排名，零额外成本。另外 `mealie vs tandoor`（KD 1）是少见的有实际搜索量（110）却几乎无竞争的对比词，立竿见影。

6. **GEO 前瞻布局**：`home assistant mealie`、`mealie self hosted`、`open source meal planner`、`meal planner self hosted` 均是月量 <30 的精准词——进 FAQ 或文章末尾段，可在 Perplexity / AI Overview 被引用。Mealie + Home Assistant + Olares 的三角整合场景，是区别于所有通用对比文的独特角度。

7. **与既有分析的关联**：`olares-500-keywords` 中以隐私/自托管为主线，Mealie 作为厨房数字化的落地应用（食谱、购物、膳食），填补了"生活方式类自托管"这一块缺口。与 Grocy（家庭物品管理）、Home Assistant（智能家居）可构成"家庭 OS"内容簇，互相引流。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
