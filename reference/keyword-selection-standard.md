# 选词标准（报告层）+ 关键词簇（内容层）

> 全项目 SEO 选词与"词→文章"映射的**单一事实源**，分两层：
>
> - **Layer 1｜报告层（说词）**：研究 skill（[brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)、[model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)）在单份报告里对每个词下判断——量/KD/意图 + **角色（主词候选/次级/GEO）**。报告**不谈文章、不聚簇**。
> - **Layer 2｜内容层（说簇）**：[seo-content](/Users/pengpeng/seo/.cursor/skills/seo-content/SKILL.md) 写文章时才把词聚成"文章簇"，且**可跨多份报告取词**。簇不落独立文件，由每篇文章的 front-matter（`target_keyword` + `secondary_keywords`）承载。
>
> 改标准改这里，skill 只引用。

## 为什么分两层

旧做法把"簇（文章单位）"写进每份报告，有两个坑：

1. **簇天然跨报告**——`best gpu for local llm` 同时命中 6 份 dGPU 报告，若每份各写一遍簇，重复度极高。
2. **报告职责被稀释**——报告该干的是"把词研究清楚、对每个词下判断"，"要写哪些文章"是下游内容规划的事。

核心纠偏：**报告只对词下判断（角色）；聚簇成文章放到 seo-content 写文时做，可跨报告。**

---

## Layer 1 · 报告层：三角色选词标准

不要孤立地问"这个词选不选"，而要问"它扮演什么角色"。判断用四要素加权：**月量 ↑ · KD ↓ · 意图/CPC（商业价值）↑ · 与 Olares 场景契合 ↑**。报告的产出是一张 **Top 关键词（含角色判断）** 词表——不是簇。

| 角色 | 定义 | 门槛 |
|------|------|------|
| **主词候选（pillar）** | 有潜力撑起一篇独立文章的头部词（是否真成一篇，留给内容层聚簇时定）| 软参考线 **US 月量 ≥ ~100**；但**同族词合计量 ≥ ~300–500 或强商业/高 CPC/战略意图可上提**；量大但排不动的品牌导航词/偏意图词**不算**主词候选 |
| **次级（secondary）** | 可并进一篇文章的同族/变体/长尾（H2/表格/正文）| 边际成本≈0：on-topic + KD 低即收，**量<50 也收** |
| **GEO 前哨（geo）** | 近零量但语义精准，抢 AI Overview / Perplexity 引用位 | 进 FAQ/直答块或前瞻段；`X alternative` 这类 KD<15 的战略词可专门 GEO 抢占 |

### 主词候选软参考分档（US 月量，意图可覆盖）

| US 月量 | 默认角色 |
|---------|---------|
| ≥ 500 | 强主词候选（能排、on-topic 前提下） |
| 100–500 | 有同族词支撑或强商业/Olares 契合 → 主词候选；否则并为次级 |
| 50–100 | 一般作次级；仅"强商业 + 近零竞争"才升主词候选 |
| < 50 | 只作次级或 GEO（战略 `X alternative` GEO 抢占例外）|

### 两条覆盖规则（比数字更重要）

- **同族合计可上提**：头部词哪怕 <100，只要它带的次级+问题词**合计 ≥ ~300–500/mo**，也配作主词候选——因为下游文章按簇产出，不按单词。
- **意图可上提 / 高量不自动达标**：强商业词（`X alternative`、`X vs Y`、`buy X`、高 CPC）或战略词（竞品 vs Olares）即使 <100 也可作主词候选；反过来，量上万但排不动的品牌导航/偏意图词（如 `nvidia`、`ollama`）不算合格主词候选。

> 量的口径提醒：搜索量为**美国月均**，技术类产品全球量通常为美国的 **3–5 倍**——US<50 实际≈全球 150–250，不等于没人搜；这类低漏斗词往往意图最纯、CPC 最高。

### ⭐ 机会标记（沿用）

Phase 2 扩词表里 `⭐ = KD<30 且量>0`，用于快速圈机会；角色划分在此基础上再做。

### 报告产出格式：Top 关键词（含角色判断）

每份报告在洞见前给一张词表（不含"文章/簇"字段）：

| 字段 | 说明 |
|------|------|
| 关键词 | 词本身 |
| 月量 / KD / CPC | US 月均量、难度、单价 |
| 意图 | info / comm / trans / nav |
| 角色 | 主词候选 / 次级 / GEO |
| 一句话判断 | 为什么这么定 + Olares 角度切入点 |

---

## Layer 2 · 内容层：关键词簇 = 文章单位（seo-content 阶段）

写文章时才聚簇，**不是报告产出**。

**1 簇 = 1 主词 + N 次级变体 + M 问题词 = 1 篇文章。** 关键点：

- **可跨报告取词**：一篇 listicle（如 `best gpu for local llm`）可从多份报告的"Top 关键词（含角色）"里各取主词候选/次级词，聚成一簇。
- **主词从报告的"主词候选"里挑**；次级从各报告的"次级"里收（含量<50 的低竞争词）；问题词从 PAA/`phrase_questions` 收作 FAQ/直答。
- **簇的成形与打分在写文时做**（seo-content Step 0），成果落在文章 front-matter，不回写报告。

聚簇时可参考的簇字段/打分（供 seo-content 判断"这簇值不值一篇"）：

| 字段 | 说明 |
|------|------|
| 主词 | 头部词（来自报告的主词候选）|
| 次级词 | 同族/变体/长尾，含量<50 的低竞争词 |
| 问题词 | 可做 FAQ/直答的问题 |
| 簇合计量 | 主词+次级+问题的 US 月量粗合计 |
| 文体 | alternative / versus / listicle |
| 打分 | ⭐⭐⭐ 簇合计量≥~500 且主词 KD<25，或 KD<15 且商业意图强；⭐⭐ 合计量中等且主词 KD<30，或高 CPC 对比/替代簇；⭐ 合计量小但精准/零竞争/GEO 前瞻 |

---

## 三、seo-content 对接

- 选题单位是**簇**（写文时聚），不是单个词：一篇 = 一个簇（主词 + 次级 + 问题词），词可跨报告收。
- 反模式是"一篇塞多个**不相关**的头部词"，**不是**"一篇只能有一个词"。
- front-matter 的 `target_keyword` = 簇主词，`secondary_keywords` = 簇次级+问题词——**簇就此成形并留痕，无需另建 article-plan 文件**。

---

*配套 skill：研究找词/定角色 → [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md) / [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)；写文章时聚簇 → [seo-content](/Users/pengpeng/seo/.cursor/skills/seo-content/SKILL.md)。*
