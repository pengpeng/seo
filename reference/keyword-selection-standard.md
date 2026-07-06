# 选词标准 + 关键词簇（文章单位）

> 全项目 SEO 选词与"词→文章"映射的**单一事实源**。研究 skill（[brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)、[model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)）产出报告的 Phase 2/3 与"Top 关键词簇"、内容 skill（[seo-content](/Users/pengpeng/seo/.cursor/skills/seo-content/SKILL.md)）选题都以本文件为准。改标准改这里，skill 只引用。

## 为什么需要它

旧做法只到"标 ⭐ 机会词 + 扁平 Top 10"，有两个坑：

1. **量小的词看起来"没必要选"**——其实量<50、KD 低的词该作次级/GEO 收割，只是没地方放。
2. **产物是扁平 Top 10，读起来"一词一文"**——没有把词聚成"文章簇"，于是量小的词无处安放、也低估了"一篇覆盖多个词"的常态。

核心纠偏：**把"选词"和"选文章"分开**。先给每个词定角色，再把词聚成簇，一簇 = 一篇。

---

## 一、三角色选词标准

不要孤立地问"这个词选不选"，而要问"它扮演什么角色"。判断用四要素加权：**月量 ↑ · KD ↓ · 意图/CPC（商业价值）↑ · 与 Olares 场景契合 ↑**。

| 角色 | 定义 | 门槛 |
|------|------|------|
| **主词（pillar）** | 撑起一篇独立文章的头部词 | 软参考线 **US 月量 ≥ ~100**；但**簇合计量 ≥ ~300–500 或强商业/高 CPC/战略意图可上提**；量大但排不动的品牌导航词/偏意图词**不算**主词 |
| **次级词（secondary）** | 并进一篇本来就要写的文章（H2/表格/正文） | 边际成本≈0：on-topic + KD 低即收，**量<50 也收** |
| **GEO 前哨（geo）** | 近零量但语义精准，抢 AI Overview / Perplexity 引用位 | 进 FAQ/直答块或前瞻段；`X alternative` 这类 KD<15 的战略词可专门 GEO 抢占 |

### 主词软参考分档（US 月量，意图可覆盖）

| US 月量 | 默认角色 |
|---------|---------|
| ≥ 500 | 可直接单独成一篇（能排、on-topic 前提下） |
| 100–500 | 有簇支撑或强商业/Olares 契合 → 主词；否则并为次级 |
| 50–100 | 一般作次级；仅"强商业 + 近零竞争"才升主词 |
| < 50 | 只作次级词或 GEO，基本不单独成文（战略 `X alternative` GEO 抢占例外）|

### 两条覆盖规则（比数字更重要）

- **簇合计可上提**：头部词哪怕 <100，只要它带的次级+问题词簇**合计 ≥ ~300–500/mo**，就配得上一篇。**文章按簇产出，不按单词。**
- **意图可上提 / 高量不自动达标**：强商业词（`X alternative`、`X vs Y`、`buy X`、高 CPC）或战略词（竞品 vs Olares）即使 <100 也可成主词；反过来，量上万但排不动的品牌导航/偏意图词（如 `nvidia`、`ollama`）不算合格主词。

> 量的口径提醒：搜索量为**美国月均**，技术类产品全球量通常为美国的 **3–5 倍**——US<50 实际≈全球 150–250，不等于没人搜；这类低漏斗词往往意图最纯、CPC 最高。

### ⭐ 机会标记（沿用）

Phase 2 扩词表里 `⭐ = KD<30 且量>0`，用于快速圈机会；角色划分在此基础上再做。

---

## 二、关键词簇 = 文章单位

**1 簇 = 1 主词 + N 次级变体 + M 问题词 = 1 篇规划文章。**

研究报告的产出从「Top 10 词」升级为「**Top 关键词簇**」。每簇给出：

| 字段 | 说明 |
|------|------|
| 主词 | 头部词（按上面的主词标准选） |
| 次级词 | 同族/变体/长尾，逗号分隔（含量<50 的低竞争词） |
| 问题词 | PAA/`phrase_questions` 里可做 FAQ/直答的问题 |
| 簇合计量 | 主词+次级+问题的 US 月量粗合计（判断这簇值不值一篇的关键） |
| 主词 KD | 头部词难度 |
| 评分 | ⭐⭐⭐ / ⭐⭐ / ⭐（见下） |
| 文体 | alternative / versus / listicle |
| 一句话方向 | 这簇文章打什么角度、Olares 切入点 |

### 簇评分（综合月量合计 × 主词 KD × 意图 × Olares 契合）

- **⭐⭐⭐** = 簇合计量可观（≥ ~500）且主词 KD<25，或 KD 极低（<15）且商业意图强。
- **⭐⭐** = 簇合计量中等且主词 KD<30，或高 CPC 的对比/替代簇。
- **⭐** = 簇合计量小但精准、零竞争、或 GEO 前瞻簇。

---

## 三、下游（seo-content）对接

- 选题单位是**簇**，不是单个词：一篇 = 一个簇（主词 + 次级 + 问题词）。
- 反模式是"一篇塞多个**不相关**的头部词"，**不是**"一篇只能有一个词"。
- front-matter 的 `target_keyword` = 簇主词，`secondary_keywords` = 簇次级+问题词。

---

*配套 skill：研究找词 → [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md) / [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)；写文章 → [seo-content](/Users/pengpeng/seo/.cursor/skills/seo-content/SKILL.md)。*
