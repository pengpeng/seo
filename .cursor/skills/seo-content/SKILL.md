---
name: seo-content
description: 把 SEO 研究报告里的高机会词写成可发布、可排名的文章——对比/替代文为主（X alternative、X vs Y、best open-source self-hosted X）。当用户要"写对比文/替代文/落地页、把某个关键词做成内容、把某份竞品报告的 Top 10 落地成文章"时使用。这是把研究变成内容的一步；找词仍用 brand-seo-research / model-seo-research，懂陌生主题用 deep-research。
---

# SEO 内容生产（对比/替代文）

把一个**目标关键词 + 它所在的竞品报告**，变成一篇面向该词的可发布文章：套 Olares 品牌口径、事实可兑现、结构对搜索/AI 引擎友好。这是主线 2「方法论」的落地件——研究（找词）已由两个 SEO skill 完成，本 skill 负责**写**。

文体模板、对比表、title/meta 公式、自查清单见 [reference.md](reference.md)。

## 分工（别走错）

- 找词/competitors/搜索量 → [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)、[model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)
- 理解陌生领域/公司/技术做综述 → [deep-research](/Users/pengpeng/seo/.cursor/skills/deep-research/SKILL.md)
- **把词写成文章** → 本 skill

## 三种文体（v1，同源机制）

| 文体 | 目标词形态 | 骨架 |
|------|-----------|------|
| **Alternative**（单竞品替代）| `X alternative`、`open source X`、`self hosted X` | 讲清 X 是什么/痛点 → 开源自托管替代方案 → 为什么 Olares（一键部署+本地 LLM+数据归你）→ 迁移/上手 |
| **Versus**（对比，可三方含 Olares）| `X vs Y`、`X vs Y vs Olares` | 对称对比表 → 逐维展开 → 各自适合谁 → Olares 的第三条路 |
| **Listicle**（清单）| `best/N open-source self-hosted X`、`X alternatives` | N 个真实可选项（客观）→ 每个一段 + 在 Olares 一键部署 → 汇总选择建议 |

## Step 0 · 选题与挂载

1. **跨报告聚簇 + 定文体**：报告只给"Top 关键词（含角色判断）"词表（主词候选/次级/GEO），**簇在这里聚**——从一份或多份报告里挑一个主词候选做簇主词，把同主题的次级/GEO 词（可跨报告，如 listicle `best gpu for local llm` 从多份 dGPU 报告各取词）收成 1 簇 = 主词 + 次级 + 问题词 = 1 篇（选词/聚簇标准见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md) Layer 2），或用户直接给词。据主词词形选文体——**一篇覆盖整簇**，量小的次级/问题词进 H2/FAQ；簇最终落在 front-matter，不回写报告。
2. **读透来源报告** [directions/*/reports/](/Users/pengpeng/seo/directions)：拿它的意图/KD/CPC、**Olares 角度**、**最大攻击面**（如 Lovable 的 credits 计费、闭源、云端隐私）、竞品事实——这些直接决定文章的差异化切入。
3. **读品牌口径** [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)：大小写、向往型语气、slogan/verbatim、写作规范、**保密红线**。
4. **挂场景 + 核平替**：目标词属 [scenarios.md](/Users/pengpeng/seo/scenarios/scenarios.md) 哪个场景 → 决定能承诺什么；作为"平替"推荐的 Olares 应用/模型必须在 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md) / [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 里**确实可部署**，否则不写。

## Step 1 · SERP / 意图侦察

用 `WebSearch` 搜目标词（及主要变体），判：

- **当前谁在排前排**：标题、内容格式（清单/对比/教程）、篇幅、角度——胜出格式决定你的骨架。
- **People Also Ask / 相关搜索**：抽成 FAQ 与次级 H2。
- **是否出现 AI Overview / 精选摘要**：若有，说明该词是"直答型"，Step 4 必须放直答块抢引用位。
- **意图**：信息（怎么做/是什么）还是商业（替代/对比/定价）——决定 CTA 强度。

对竞品事实（定价、是否开源、许可证、限额）不确定时，用 `WebFetch` 核官网/文档，别凭记忆写。

## Step 2 · 内容 brief（先出 brief 再动笔）

产出一份 brief（模板见 [reference.md](reference.md)）：

- **主词 + 次级词**（次级词来自来源报告的同族词/相关词表）
- **搜索意图** 一句话
- **文体 + 大纲**（H2/H3；对齐 SERP 胜出格式）
- **对比表列**（Versus/Listicle 必备：功能、开源/许可证、部署方式、定价模型、数据归属、本地 LLM 等对称维度）
- **必提实体**（竞品名、相关开源项目、Olares 平替应用名）
- **内链**（其它 Olares 内容/应用页）+ **外链**（权威源：竞品官网、GitHub、标准文档）
- **title 候选（2-3）/ meta description / slug**
- **FAQ 题目**（3-5 个，来自 PAA，供 GEO 直答）

## Step 3 · 起草

按 brief 大纲写。硬规则：

- **品牌口径**：`Olares`/`Olares One`/`LarePass` 等大小写正确；首屏用向往型（Own your AI…）、技术语境才用 personal cloud OS；别把 Olares 说成 NAS/PC。（详见 basic/olares.md）
- **事实纪律**：只写 Olares 真能交付的能力（对照 scenarios 产品进度 + apps/models 可用性）；未发布能力不承诺、无版本号/时间表（保密红线）。
- **对竞品客观**：如实介绍其优点，不稻草人；对比表两侧维度对称、都填。差异化靠**攻击面**（来源报告里的定价/闭源/隐私痛点），而非贬低。
- **Olares 角度**：把需求导向"开源自托管 + 一键部署 + 本地 LLM 不烧额度 + 数据归你"，落到具体可部署的平替应用。
- **CTA**：指向对应 Olares Market 应用 / 部署入口。
- **语言**：默认英文（目标市场美国）；仅当目标词是中文词时写中文。

## Step 4 · SEO / GEO 优化

- **Title** ≤60 字符、含主词、靠前；**H1** 与 title 同义不重复堆词；**meta description** ≤155 字符、含主词 + 价值主张 + 隐性 CTA。
- **关键词**：主词进首段前 100 词、若干 H2；次级词/同义词自然分布——**不堆砌**。
- **GEO（抢 AI Overview / Perplexity 引用）**：关键问题用"一句话直答 + 展开"结构；文末 FAQ 用 Q/A；建议标注 `FAQPage` / `Article` schema（在文中以注释或 front-matter 提示，不必写死 JSON-LD）。
- **可读性/E-E-A-T**：对比表、要点列表、图/alt 文案建议；外链权威源、内链相关内容。

## Step 5 · 自查 + 落盘

对照 [reference.md](reference.md) 的自查清单逐条过：主词在 title/H1/首段/meta；对比对称；**事实与保密红线**（无未发布承诺、无编造数字、平替确实可部署）；内外链齐；FAQ/直答块在位。

落盘 `content/<slug>.md`，带 front-matter（见 [content/README.md](/Users/pengpeng/seo/content/README.md)）：`title / target_keyword / secondary_keywords / meta_description / slug / article_type / source_report / scenario / status`。**重写已有文章前先读旧稿**，保留仍有效的角度，去重更新。

## 反模式

关键词堆砌；对比表只夸自己/贬竞品；承诺未发布能力或写内部信息；推荐 Market 里根本没有的"平替"；编竞品定价/许可证不核实；标题党与正文不符；**一篇塞多个不相关的头部词**（正解：一篇 = 一个簇 = 主词 + 其次级/问题词，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)）。
