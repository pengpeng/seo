# Recraft AI SEO 竞品分析报告

> 域名：recraft.ai | SEMrush US | 2026-07-06
> 矢量优先的 AI 设计平台：全球唯一生产级 SVG 矢量生成 + 品牌一致性图像，定位设计师与创意团队

---

## 项目理解（前置）

Recraft AI 是一家总部位于旧金山的 AI 设计平台，于 2025 年 5 月完成 $30M Series B（Accel 领投，Khosla Ventures / Madrona 跟投），累计融资 $42.25M，拥有 400 万用户、$5M+ ARR。其核心差异化在于**全球唯一的生产级原生 SVG 矢量生成**——不是光栅转矢量，而是模型直接输出可编辑 SVG，专为设计师工作流设计，目标场景涵盖图标、标志、品牌插图与营销素材。最新模型为 V4.1（2026 年 5 月发布），自研闭源，不基于 Stable Diffusion。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 面向设计师的 AI 图像/矢量生成平台，强调品牌一致性与 SVG 原生输出 |
| 开源 / 许可证 | 闭源，专有模型，无公开代码库 |
| 主仓库 | 无（非开源）；API 文档见 recraft.ai/docs |
| 核心功能 | SVG/矢量原生生成、光栅图像生成、品牌风格复用（上传参考图即可）、AI 图像矢量化（raster→SVG）、背景移除、创意放大 |
| 商业模式 / 定价 | 免费（每日 credits 重置，公开生成无商业权）；Basic ~$12/月（1,000 credits，私有+商业权）；Advanced / Pro 更高用量；API 单独计费（$1/1,000 单位，V4 矢量 300 单位/张） |
| 差异化 / 价值主张 | 行业唯一"生产级矢量生成"（直接输出可编辑 SVG）；品牌风格锁定（一次建风格，批量复用）；Recraft V3 在 ImagenHub 等 benchmark 上击败 DALL-E / Midjourney |
| 主要竞品（初判） | Midjourney（艺术质量）、Adobe Firefly（设计师生态）、VectorMagic / Vectorizer.ai（矢量化工具）、Kittl（设计模板平台） |
| Olares Market | 未上架（Recraft 是商业 SaaS；开源平替见 ComfyUI，已在 Olares Market） |
| 来源 | [recraft.ai](https://www.recraft.ai)、[TechCrunch Series B](https://techcrunch.com/2025/05/05/a-stealth-ai-model-beat-dall-e-and-midjourney-on-a-popular-benchmark-its-creator-just-landed-30m/)、[定价说明](https://www.recraft.ai/blog/pricing-update)、[API 文档](https://www.recraft.ai/docs/api-reference/getting-started) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | recraft.ai |
| SEMrush Rank | 53,843 |
| 自然关键词数 | 14,919 |
| 月自然流量（US）| 38,028 |
| 自然流量估值 | $47,810/月 |
| 付费关键词数 | 1（仅 1 个拼写错误词，实际≈零付费投放） |
| 月付费流量 | 3 |
| 排名 1-3 位 | 255 词 |
| 排名 4-10 位 | 1,065 词 |
| 排名 11-20 位 | 3,058 词 |

**关键判断**：14,919 个自然词中约 255 个在前 3，占比仅 1.7%——说明 Recraft 以品牌词主导排名，品类大词（ai logo generator #12、image upscaler #12）尚难打入前列；存在大量非品牌词机会空白。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.recraft.ai | 14,913 | 38,028 | 100% |
| feedback.recraft.ai | 3 | 0 | — |
| recraft.ai（根域） | 2 | 0 | — |

流量几乎 100% 集中在主站，无独立文档站 / 博客子域贡献。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| recraft | 1 | 12,100 | 56 | $1.19 | 9,680 | 品牌 | recraft.ai/ |
| recraft ai | 1 | 6,600 | 52 | $1.64 | 5,280 | 品牌 | recraft.ai/ |
| recraft.ai | 1 | 2,400 | 76 | $1.64 | 1,920 | 品牌/导航 | recraft.ai/ |
| recraft.ai vectorizer | 1 | 1,900 | 32 | $0.90 | 1,520 | 品牌/导航 | recraft.ai/ai-image-vectorizer |
| recraft v3 | 1 | 880 | 63 | $1.04 | 704 | 品牌 | recraft.ai/ |
| рекрафт（俄语） | 1 | 880 | 33 | $0 | 704 | 品牌 | recraft.ai/ |
| кускфае（乌克兰语键盘打法） | 1 | 1,900 | 33 | $0.08 | 471 | 品牌 | recraft.ai/ |
| ai logo generator | 12 | 49,500 | 87 | $1.70 | 445 | 信息 | recraft.ai/generate/logos |
| reccraft（拼写错误） | 1 | 1,600 | 36 | $1.27 | 396 | 品牌 | recraft.ai/ |
| recraft.ia（拼写错误） | 1 | 1,600 | 47 | $1.37 | 396 | 品牌 | recraft.ai/ |
| image upscaler | 12 | 49,500 | 82 | $0.77 | 346 | 信息 | recraft.ai/image-upscaler |
| recraf（拼写错误） | 1 | 390 | 51 | $1.27 | 312 | 品牌 | recraft.ai/ |
| recraft login | 1 | 320 | 31 | $0 | 256 | 导航 | recraft.ai/auth/login |
| vector ai | 3 | 2,400 | 66 | $0.75 | 196 | 信息 | recraft.ai/ai-vector-generator |
| recraft ai image vectorizer | 1 | 210 | 23 | $1.42 | 168 | 品牌 | recraft.ai/ai-image-vectorizer |
| recraft ai logo | 1 | 210 | 54 | $1.65 | 168 | 品牌 | recraft.ai/generate/logos |
| recraft ai image generator | 1 | 210 | 59 | $1.38 | 168 | 品牌 | recraft.ai/ |
| ai raster to vector free | 1 | 590 | 62 | $0 | 146 | 信息 | recraft.ai/ai-image-vectorizer |
| recraft vectorizer | 1 | 170 | 29 | $0 | 136 | 品牌 | recraft.ai/ai-image-vectorizer |
| vectorised ai | 3 | 1,600 | 58 | $0.75 | 131 | 信息 | recraft.ai/ai-vector-generator |
| ai logo | 10 | 9,900 | 78 | $1.49 | 128 | 信息 | recraft.ai/generate/logos |
| ai generated logo | 8 | 9,900 | 75 | $1.70 | 128 | 信息 | recraft.ai/generate/logos |
| icon generator | 5 | 2,900 | 65 | $1.64 | 127 | 信息 | recraft.ai/generate/icons |
| recraft ai icon generator | 1 | 140 | 31 | $2.30 | 112 | 品牌 | recraft.ai/generate/icons |
| recraft v4 | 1 | 140 | 18 | $1.77 | 112 | 品牌 | recraft.ai/ |
| ai icon generator | 3 | 1,300 | 61 | $1.39 | 106 | 信息 | recraft.ai/generate/icons |
| twitch banner maker | 4 | 1,600 | 30 | $0.70 | 104 | 信息 | recraft.ai/generate/twitch-banners |
| artificial intelligence icon generator | 2 | 720 | 42 | $1.40 | 95 | 信息 | recraft.ai/generate/icons |
| hoodie designer | 8 | 3,600 | 34 | $0 | 86 | 信息 | recraft.ai/generate/hoodies |
| ai logos | 7 | 3,600 | 78 | $1.49 | 86 | 信息 | recraft.ai/generate/logos |
| ai vector graphics | 4 | 1,300 | 62 | $0.76 | 84 | 信息 | recraft.ai/ai-vector-generator |
| art in balance | 8 | 3,600 | 27 | $0 | 79 | 信息 | recraft.ai/blog/balance-in-art-tips |

**程序化落地页观察**：recraft.ai 已布局 `/generate/<品类>/` 路径（logos、icons、twitch-banners、hoodies、book-illustration 等），是典型的**内容程序化扩张**策略，但流量尚低——多数页面仍在 4-10 名或更靠后。

### 付费词（Google Ads，按流量排序）

几乎无付费投放——仅检测到 1 个词（"recrft"，一个拼写变体，导向 /background-remover），付费流量约 3。Recraft 依赖产品口碑与有机增长，不做搜索广告。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| midjourney alternative | 590 | 33 | $1.83 | 信息 | ⭐ 竞品对比首选，Recraft 本身是答案之一 |
| canva alternative | 1,000 | 30 | $1.90 | 信息 | ⭐ KD 低，Recraft/ComfyUI 均可入答案 |
| midjourney free alternative | 590 | 29 | $1.13 | 信息 | ⭐ 免费替代意图，Olares+ComfyUI 完美切入 |
| adobe firefly alternative | 170 | 12 | $1.51 | 信息 | ⭐ KD 极低，高 CPC，商业意图强 |
| comfyui alternative | 170 | 7 | $2.19 | 信息 | ⭐ KD 最低，Olares 机会词 |
| stable diffusion alternative | 70 | 11 | $2.62 | 信息/商业 | ⭐ 小量但 KD 很低 |
| runway ml alternative | 40 | 10 | $2.61 | 信息 | ⭐ 低 KD，视频 AI 替代搜索 |
| recraft alternative | 20 | 0 | $0 | 信息 | ⭐ GEO 级，KD=0，Olares 可捕获 |
| recraft ai alternative | 20 | 0 | $0 | 信息 | ⭐ GEO 级，KD=0 |
| recraft vs midjourney | 30 | 0 | $0 | 信息 | ⭐ 对比词，GEO |
| midjourney vs recraft | 20 | 0 | $0 | 信息 | ⭐ 对比词，GEO |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai image generator | 823,000 | 92 | $0.94 | 信息 | 超大品类词，KD 难 |
| ai photo generator | 165,000 | 83 | $0.86 | 信息 | 大品类，难 |
| ai image generator free | 110,000 | 87 | $0.81 | 信息 | 大品类，难 |
| ai logo generator free | 12,100 | 83 | $1.58 | 信息 | Recraft 排 #12，CPC 高 |
| best ai image generator | 27,100 | 76 | $1.72 | 信息 | Recraft 尚未进前页 |
| ai illustration generator | 1,600 | 87 | $1.71 | 信息 | KD 很高 |
| icon generator | 2,900 | 65 | $1.64 | 信息 | Recraft 排 #5 |
| ai icon generator | 1,300 | 61 | $1.39 | 信息 | Recraft 排 #3 |
| ai vector generator | 590 | 58 | $1.92 | 信息 | 核心细分词，Recraft 弱势 |
| vector art generator | 390 | 63 | $1.38 | 信息 | 中等 KD |
| image to vector ai | 320 | 58 | $1.23 | 信息 | 矢量化场景词 |
| svg generator ai | 170 | 48 | $1.60 | 信息 | 核心差异化词，KD 可接受 |
| ai svg generator | 140 | 48 | $1.55 | 信息 | 与上词近同，合并 |
| ai image vectorizer | 90 | 52 | $1.25 | 信息 | Recraft 工具页有排名 |
| ai vector art | 90 | 58 | $1.17 | 信息 | 小量，KD 偏高 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| recraft | 12,100 | 56 | $1.19 | 品牌 | 主品牌词，#1 |
| recraft ai | 6,600 | 52 | $1.64 | 品牌 | 品牌变体，#1 |
| recraft.ai vectorizer | 1,900 | 32 | $0.90 | 品牌 | 工具页入口，#1 |
| recraft v3 | 880 | 63 | $1.04 | 品牌 | 版本词，#1 |
| recraft login | 320 | 31 | $0 | 导航 | #1 |
| recraft pricing | 110 | 36 | $0 | 商业 | #1，定价页 |
| recraft api | 110 | 36 | $2.40 | 商业 | #1，API 入口 |
| recraft ai free | 110 | 52 | $1.42 | 商业 | #1，免费层查询 |
| recraft ai icon generator | 140 | 31 | $2.30 | 品牌 | #1，图标工具 |
| recraft v4 | 140 | 18 | $1.77 | 品牌 | #1，KD=18 最低 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| comfyui | 49,500 | 63 | $4.00 | 信息/商业 | ComfyUI 已在 Olares Market |
| stable diffusion | 74,000 | 100 | $0.81 | 信息 | KD=100，极难 |
| local ai image generator | 480 | 26 | $1.32 | 信息 | ⭐ KD 低，Olares 最直接机会 |
| comfyui vs automatic1111 | 260 | 22 | $0 | 信息 | ⭐ 对比内容，Olares 可插入 |
| comfyui alternative | 170 | 7 | $2.19 | 信息 | ⭐ KD 最低，高 CPC |
| open source image generator | 110 | 44 | $0.79 | 信息 | 中等 KD |
| ai vector generator free | 140 | 56 | $1.59 | 信息 | 矢量生成免费需求 |
| stable diffusion alternative | 70 | 11 | $2.62 | 信息 | ⭐ KD 极低 |
| ai image generation open source | 20 | 0 | $0 | 信息 | ⭐ GEO 级，KD=0 |
| self hosted image generator | 20 | 0 | $0 | 信息 | ⭐ GEO 级，完美 Olares 词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Recraft 的护城河是原生 SVG 矢量生成，ComfyUI on Olares 在光栅图像生成上是有力替代，但矢量输出方面需诚实标注差距——内容应聚焦"本地/自托管图像生成"叙事，而非夸大矢量平替能力。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| local ai image generator | 480 | 26 | $1.32 | ComfyUI on Olares = 本地、离线、无月费 AI 图像生成；提及 Recraft 为付费在线替代 | ⭐⭐⭐ |
| midjourney alternative | 590 | 33 | $1.83 | 合集文章：Recraft（矢量特长）、ComfyUI on Olares（自托管、无审查、免月费）均为 Midjourney 替代方案，各有侧重 | ⭐⭐⭐ |
| midjourney free alternative | 590 | 29 | $1.13 | "免费本地方案"叙事：ComfyUI on Olares 硬件买断后零边际成本，Recraft 免费层有 credits 限制 | ⭐⭐⭐ |
| comfyui alternative | 170 | 7 | $2.19 | KD=7 极稀缺；内容可从"ComfyUI 替代方案"切入，反向推介 Olares 作为 ComfyUI 最佳部署平台 | ⭐⭐⭐ |
| adobe firefly alternative | 170 | 12 | $1.51 | 同上，合集文章覆盖 Recraft（矢量/设计）、ComfyUI on Olares（自托管）；KD=12 易切入 | ⭐⭐ |
| recraft alternative | 20 | 0 | $0 | 直接机会：GEO 覆盖"Recraft 平替"搜索，答案包括 ComfyUI on Olares（光栅图像方向）；诚实说明矢量功能差距 | ⭐⭐ |
| comfyui vs automatic1111 | 260 | 22 | $0 | Olares 同时支持 ComfyUI + A1111；比较文章末尾推介 Olares 一键启动两者 | ⭐⭐⭐ |
| stable diffusion alternative | 70 | 11 | $2.62 | KD=11，高 CPC；Olares + ComfyUI 是自托管 SD 工作流的理想平台 | ⭐⭐ |
| open source image generator | 110 | 44 | $0.79 | 内容列举开源方案，ComfyUI on Olares 为主推 | ⭐⭐ |
| ai image generation open source | 20 | 0 | $0 | GEO 前哨，AI Overview 引用位 | ⭐⭐⭐ |
| self hosted image generator | 20 | 0 | $0 | GEO 前哨，与 Olares 定位完美匹配 | ⭐⭐⭐ |
| canva alternative | 1,000 | 30 | $1.90 | 合集文章（Recraft、ComfyUI on Olares、开源设计工具），量大 KD 可接受 | ⭐⭐ |

> **重要叙事备注**：Recraft 的原生 SVG 矢量生成目前在开源生态中没有等效替代——ComfyUI/Stable Diffusion 输出光栅图像，无法直接生成可编辑 SVG。内容应诚实标注：针对"品牌插图（光栅）、AI 图像生成、logo 草图"等用例，ComfyUI on Olares 是有竞争力的自托管替代；针对"SVG 矢量图标、可缩放 logo、编辑矢量图形"等用例，Recraft 有真实技术壁垒，应如实说明。

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| local ai image generator | 480 | 26 | $1.32 | 信息 | **主词候选** | KD=26，量适中；Olares 叙事完美对位，ComfyUI on Olares = 本地 AI 图像生成标杆 |
| midjourney alternative | 590 | 33 | $1.83 | 信息 | **主词候选** | KD=33 可打；Recraft（矢量特长）与 ComfyUI on Olares（自托管）合并入同一合集文 |
| midjourney free alternative | 590 | 29 | $1.13 | 信息 | **主词候选** | KD=29，"免费/本地"意图直接命中 ComfyUI on Olares 叙事 |
| canva alternative | 1,000 | 30 | $1.90 | 信息 | **主词候选** | KD=30，量最大；Recraft（设计侧）+ ComfyUI on Olares（创作侧）均可入文 |
| comfyui alternative | 170 | 7 | $2.19 | 信息 | **主词候选** | KD=7 全批最低，反向切入：内容目标为"ComfyUI 替代方案"，实际推介 Olares 作为 ComfyUI 最佳托管平台 |
| adobe firefly alternative | 170 | 12 | $1.51 | 信息 | **主词候选** | KD=12 低 + CPC $1.51，Recraft 与 ComfyUI on Olares 均为替代方案 |
| comfyui vs automatic1111 | 260 | 22 | $0 | 信息 | **主词候选** | KD=22，Olares 同时支持两者，文章末推介 Olares 部署 |
| ai vector generator | 590 | 58 | $1.92 | 信息 | **次级** | KD 偏高，但是核心品类词；Recraft 是该词的领先商业答案；ComfyUI 目前无原生矢量输出，需诚实标注 |
| stable diffusion alternative | 70 | 11 | $2.62 | 信息/商业 | **次级** | KD=11 极低 + CPC 最高；小量可并入替代合集 |
| recraft alternative | 20 | 0 | $0 | 信息 | **次级** | 量小但 KD=0；直接面对"Recraft 替代"搜索者；ComfyUI on Olares 是诚实但有限的答案 |
| svg generator ai | 170 | 48 | $1.60 | 信息 | **次级** | SVG 生成核心词；Recraft 商业答案；开源侧目前无等效工具（如实标注） |
| ai icon generator | 1,300 | 61 | $1.39 | 信息 | **次级** | KD 偏高；Recraft 已排 #3；ComfyUI 可生成图标光栅图但非 SVG |
| open source image generator | 110 | 44 | $0.79 | 信息 | **次级** | Olares + ComfyUI 是标准答案；并入自托管内容 |
| ai image generation open source | 20 | 0 | $0 | 信息 | **GEO** | KD=0 零竞争；AI Overview / Perplexity 引用位，Olares 答案完美匹配 |
| self hosted image generator | 20 | 0 | $0 | 信息 | **GEO** | KD=0；精准匹配 Olares 定位，抢 AI Overview 引用 |
| recraft ai alternative | 20 | 0 | $0 | 信息 | **GEO** | KD=0；品牌对比词，GEO 前哨覆盖 |
| brand illustration ai | 0 | — | — | — | **GEO** | 近零量但语义精准；Recraft 的品牌叙事词，AI Overview 可引用 Olares 侧内容对比 |

---

## 核心洞见

1. **品牌护城河**：Recraft 的品牌关键词（"recraft"/"recraft ai"/"recraft.ai"）贡献约 **44%** 的自然流量（~17,000/38,028），且几乎全部拿到 #1 位置，品牌心智牢固。正面刚"recraft"品牌词没有意义——但品牌词本身说明它在矢量设计师圈已建立认知，Olares 内容应围绕"替代"角度切入，而非品牌对打。

2. **可复制的打法**：Recraft 走的是**程序化落地页**路线（`/generate/logos`、`/generate/icons`、`/generate/twitch-banners`、`/generate/hoodies`…）——已建立品类-品牌词排名基础设施，但非品牌流量很低，多数品类词在第 2 页。这意味着内容机会仍开放：竞争对手尚未形成绝对壁垒，Olares 可以"替代/合集"类内容切入同一词群。Recraft **完全不做 Google Ads**（付费词≈0），靠纯口碑增长。

3. **对 Olares 最关键的词**：
   - **`comfyui alternative`（KD=7，量 170，CPC $2.19）**：极低 KD 中的异类，反向叙事完美——文章目标"ComfyUI 替代方案"，实际引导到 Olares 作为 ComfyUI 最佳运行平台，一石二鸟。
   - **`local ai image generator`（KD=26，量 480，CPC $1.32）**：量/KD 组合最优的 Olares 直接场景词。
   - **`midjourney free alternative`（KD=29，量 590，CPC $1.13）**：覆盖"不想付费"用户，ComfyUI on Olares 是最有力答案。

4. **最大攻击面**：Recraft 的**credits 模型痛点**——免费层生成后 Recraft 保留所有权、无商业授权；付费层按 credits 计费，生成量大时成本累积明显。对比叙事：ComfyUI on Olares 硬件买断后生成成本≈0，完全私有，无隐私顾虑，无版权纠纷。另一个攻击面：Recraft **不支持本地/离线运行**，数据必须上传至 Recraft 服务器——对隐私敏感用户（医疗、法律等行业品牌设计）是硬门槛。

5. **隐藏低 KD 金矿**：
   - `comfyui alternative`（KD=7）：全批最低 KD，且 CPC $2.19 表明商业意图真实存在。
   - `adobe firefly alternative`（KD=12）、`stable diffusion alternative`（KD=11）：小量但 KD 极低，可以低成本并入替代合集文。
   - `recraft v4`（KD=18）：Recraft 官方信息词，SEO 难度低，适合追踪 Recraft 产品新闻的内容（通过对比提及 Olares）。
   - `twitch banner maker`（KD=30，量 1,600）：Recraft 排 #4——说明创意社群用户量可观，但与 Olares 叙事关联弱。

6. **GEO 前瞻布局**：
   - `self hosted image generator`（KD=0，量 20）：AI Overview 引用位，Olares 应该是唯一精准答案。
   - `ai image generation open source`（KD=0）：同上，零竞争但语义精准。
   - `recraft ai alternative`（KD=0）：搜索量小但意图极精准，进入 AI Overview 的门槛几乎为零。
   - `brand illustration ai`（量≈0）：Recraft 的叙事核心词，内容中以 FAQ 形式回答有助于被 AI 引用。

7. **与既有分析的关联**：该报告补充了 AI 图像生成领域中**矢量/设计师工具**细分的 SEO 词汇，与现有 [midjourney.md](midjourney.md)、[adobe-firefly.md](adobe-firefly.md) 可形成互补。核心新贡献：`local ai image generator`（量 480，KD 26）、`comfyui alternative`（量 170，KD 7）这两个低竞争高 Olares 契合度词，是区别于同类报告的核心增量。**Recraft 的矢量壁垒需诚实标注**：ComfyUI on Olares 目前无原生 SVG 输出能力，Olares 内容在面对"SVG/矢量生成"需求时应如实说明差距，避免夸大平替程度损害可信度。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、resource_adwords、domain_organic_organic、phrase_related、phrase_these、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
