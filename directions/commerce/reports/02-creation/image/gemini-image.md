# Google Gemini Image（Imagen）SEO 竞品分析报告

> 场景词分析（功能子集，非域名整体）| SEMrush US | 2026-07-06
> Google Gemini 图像生成（Imagen 系列）= Google 旗下闭源商业 AI 图像生成能力，集成于 Gemini 聊天界面与独立产品 ImageFX，面向消费者与开发者（Vertex AI / Gemini API 两条路线）

---

## 项目理解（前置）

Google 的 AI 图像生成能力以两个品牌出现：**Gemini**（聊天界面内联图像生成）与 **Imagen 系列**（当前已到 Imagen 4 / Gemini 3 Pro Image，后者即官方营销名"Nano Banana Pro"）。消费者入口是 gemini.google.com 与独立产品 [ImageFX](https://imagefx.google/)；开发者走 Gemini API / Vertex AI。核心优势是深度集成 Google 生态（搜索接地、Gmail、Workspace）、多轮对话式编辑与 4K 输出；劣势是审查严格（platform-flag risk 28%）、审美风格不如 Midjourney、闭源无法私有部署、免费额度极低（3 张/天）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Google 闭源 AI 图像生成套件，Gemini 聊天 + Imagen 模型 + ImageFX 独立产品三线并行 |
| 开源 / 许可证 | 闭源；仅 Gemma 文本模型开源，Imagen 系列无开源版本 |
| 主仓库 | 无公开仓库（Vertex AI / Google AI Studio 闭源托管） |
| 核心功能 | 文生图（1K/2K/4K）、多轮对话编辑、最多 14 张参考图融合、文字渲染、Grounding with Search |
| 商业模式 / 定价 | 免费 3 图/天；AI Plus $7.99/月；AI Pro $19.99/月（约 100 图/天）；AI Ultra ~$30/月（1000 图/天）；API 按 token/图：Imagen 3 Fast $0.02、Standard $0.04；Gemini 3 Pro Image $0.134（1K/2K）、$0.24（4K） |
| 差异化 / 价值主张 | Google 生态闭环（Gmail 草稿配图、Google Slides）、多轮对话图像编辑、4K 输出、Grounding with Google Search 保真当下事实 |
| 主要竞品（初判）| Midjourney（美学）、OpenAI GPT Image / DALL-E（文字渲染+准确度）、Flux（本地/开源）、Stable Diffusion / ComfyUI（完全可控）|
| Olares Market | 未上架（闭源服务）；Olares 平替路线：ComfyUI + FLUX.1 / SD 3.5 本地部署 |
| 来源 | [ai.google.dev/gemini-api/docs/image-generation](https://ai.google.dev/gemini-api/docs/image-generation)、[docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro-image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro-image)、[intuitionlabs.ai/articles/ai-image-generation-pricing-google-openai](https://intuitionlabs.ai/articles/ai-image-generation-pricing-google-openai) |

---

## 流量基线（Phase 1）

> **降级模式**：gemini.google.com 为 Google 旗舰域（SEMrush Rank 极高，月流量数千万），直接分析整站数据意义不大。本报告专注**图像生成细分词**，跳过域名整体流量报告，直接从 Phase 2 关键词层面展开。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词；⭐⭐ = KD<15 且量>0 的金矿词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| midjourney alternative | 590 | 33 | $1.83 | 信息/品类 | 主力替代词，CPC 高 |
| midjourney alternative free | 390 | 31 | $1.16 | 信息 | 价格痛点明显 |
| comfyui alternative | 170 | **7** | $2.19 | 信息 | ⭐⭐ 极低 KD，CPC $2.19 |
| stable diffusion alternative | 70 | 11 | $2.62 | 信息 | ⭐⭐ KD 超低 |
| flux alternative | 90 | 19 | $0 | 信息 | ⭐ 低 KD |
| gemini vs midjourney | 20 | 0 | $0 | 信息 | GEO 级，比较意图强 |
| imagen vs midjourney | 20 | 0 | $0 | 信息 | GEO |
| imagen 3 vs midjourney | 20 | 0 | $0 | 信息 | GEO |
| imagen 4 vs midjourney | 20 | 0 | $0 | 信息 | GEO |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai image generator | 823,000 | 92 | $0.94 | 品类 | 超大词，KD 极高，不可直攻 |
| free ai image generator | 110,000 | 92 | $0.98 | 信息/品类 | 同上 |
| ai photo editor | 135,000 | 87 | $0.76 | 品类 | 编辑品类词 |
| best ai image generator | 27,100 | 76 | $1.72 | 商业 | 高商业意图 |
| image generator | 74,000 | 90 | $0.97 | 品类 | KD 90，极难 |
| ai image editing | 3,600 | 72 | $0.76 | 信息 | 编辑细分 |
| ai image generator no sign up | 3,600 | 70 | $0.71 | 信息 | 隐私/便利信号 |
| open source image generator | 110 | 44 | $0.79 | 信息 | ⭐ 小众但意图精准 |
| local ai image generator | 480 | **26** | $1.32 | 信息 | ⭐ 低 KD，Olares 直接机会 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| gemini image generator | 18,100 | 62 | $1.27 | 信息 | 品牌核心词，量最大 |
| google ai image generator | 18,100 | 55 | $1.20 | 信息 | 非品牌路径，KD 55 |
| gemini ai image generator | 8,100 | 66 | $1.08 | 品牌 | 品牌修饰 |
| google imagen | 8,100 | 88 | $1.15 | 品牌/导航 | KD 88，Google 护城河 |
| imagen ai | 8,100 | 69 | $1.12 | 品牌 | 混合品牌+品类 |
| imagen 3 | 5,400 | **44** | $1.13 | 信息 | ⭐ 型号词，KD 合理 |
| imagen 4 | 5,400 | **40** | $0 | 信息 | ⭐ 新型号，CPC $0（无付费竞争）|
| google imagefx | 5,400 | 61 | $1.57 | 品牌/导航 | ImageFX 独立产品 |
| google image generator | 6,600 | 66 | $1.16 | 信息/品类 | 部分流向 Google |
| imagenfx | 4,400 | 80 | $1.21 | 品牌 | ImageFX 拼写变体 |
| imagen fx | 3,600 | 63 | $1.21 | 品牌/信息 | ImageFX 分词 |
| gemini image generation | 3,600 | 74 | $1.23 | 信息 | 生成场景词 |
| google imagen 3 | 1,600 | **42** | $1.22 | 信息 | ⭐ 型号+品牌组合，KD 低于主词 |
| gemini-3-pro-image-preview | 1,600 | **31** | $1.78 | 信息/商业 | ⭐ 开发者/API 词，CPC 高 |
| google gemini image generation | 2,900 | 86 | $1.27 | 信息 | KD 偏高 |
| can gemini generate images | 2,400 | 62 | $1.57 | 信息 | 功能确认词 |
| gemini ai image generator free | 1,300 | **48** | $1.12 | 品牌/商业 | ⭐ 价格信号 |
| gemini 2.0 flash image generation | 590 | **46** | $1.23 | 信息 | ⭐ 型号功能词 |
| gemini prompts for image generation | 320 | **31** | $1.17 | 信息 | ⭐ 教程类，低 KD |
| gemini image generation api | 210 | **31** | $2.63 | 信息 | ⭐ 开发者词，CPC $2.63 高 |
| gemini flash image | 210 | **24** | $1.01 | 信息 | ⭐ KD 24，极低竞争 |
| gemini not generating images | 170 | **31** | $0 | 信息 | ⭐ 痛点词（Gemini 限额触达） |
| why can't gemini generate images | 140 | **30** | $0 | 信息 | ⭐ 同上，用户挫败 |
| why can't gemini generate images anymore | 140 | **22** | $0 | 信息 | ⭐⭐ KD 22，限制痛点词 |
| gemini ai image generator nsfw | 1,300 | 18 | $0 | 信息 | ⭐ KD 极低（内容过滤痛点，Olares 无审查可说） |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| comfyui | 49,500 | 63 | $4.00 | 信息 | Olares 平替主词，CPC 极高说明价值 |
| stable diffusion | 74,000 | 100 | $0.81 | 信息 | 超大词，KD 满分 |
| flux schnell | 880 | 66 | $0.80 | 信息 | Flux 系列词 |
| comfyui flux | 390 | 49 | $0.73 | 信息 | ComfyUI+Flux 组合 |
| comfyui online | 260 | 44 | $1.10 | 信息 | 在线版 ComfyUI |
| run stable diffusion locally | 260 | **23** | $1.59 | 信息 | ⭐ 低 KD，本地部署意图明确 |
| comfyui vs stable diffusion | 140 | **8** | $0 | 信息 | ⭐⭐ KD 8，低竞争教育词 |
| local ai image generator | 480 | **26** | $1.32 | 信息 | ⭐ 核心 Olares 攻击词 |
| open source image generator | 110 | **44** | $0.79 | 信息 | ⭐ 开源意图 |
| midjourney alternative free | 390 | 31 | $1.16 | 信息 | ⭐ 价格痛点 + Olares 叙事入口 |
| run flux locally | 70 | **21** | $0 | 信息 | ⭐ 极低 KD，本地 Flux |
| run comfyui locally | 20 | 0 | $0 | 信息 | GEO，精准本地意图 |
| self-hosted ai image generator | 0 | 18 | $0 | 信息 | GEO（量极小，语义精准） |
| private ai image generator | 70 | 74 | $1.13 | 信息 | 隐私意图强，KD 偏高 |

---

## Olares 关联词（Phase 3）

**核心叙事**：Gemini Image 的核心痛点是限额（免费仅 3 图/天）、闭源不可控、图像数据上传 Google 云、内容审查严格。Olares 提供 ComfyUI + FLUX.1 / SD 3.5 完全本地运行——无限生成、数据不离设备、无 Google 审查、支持 LoRA 自定义风格。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-------------|--------|
| local ai image generator | 480 | 26 | $1.32 | Olares 一键跑 ComfyUI/Flux，完全本地、无限制 | ⭐⭐⭐ |
| run stable diffusion locally | 260 | 23 | $1.59 | Olares 本地部署 SD，7×24 无头自用，无 Google 审查 | ⭐⭐⭐ |
| why can't gemini generate images anymore | 140 | 22 | $0 | Gemini 限额触发→Olares 无额度限制对比 | ⭐⭐⭐ |
| gemini not generating images | 170 | 31 | $0 | 同上，限制痛点；导流"本地无限制方案" | ⭐⭐⭐ |
| why can't gemini generate images | 140 | 30 | $0 | 同上 | ⭐⭐⭐ |
| comfyui alternative | 170 | 7 | $2.19 | Olares 上的 ComfyUI 一键安装，无需 Python 环境 | ⭐⭐⭐ |
| run comfyui locally | 20 | 0 | $0 | GEO：Olares 最简单的本地 ComfyUI 方式（一键安装） | ⭐⭐⭐ |
| midjourney alternative free | 390 | 31 | $1.16 | ComfyUI + FLUX.1 on Olares = 零订阅、本地无限图 | ⭐⭐⭐ |
| run flux locally | 70 | 21 | $0 | Olares Market 的 ComfyUI 预置 FLUX 节点 | ⭐⭐⭐ |
| self-hosted ai image generator | 0 | 18 | $0 | GEO：Olares = 自托管 AI 图像生成平台（ComfyUI 后端） | ⭐⭐⭐ |
| gemini image generation api | 210 | 31 | $2.63 | 开发者词；Olares 可跑本地 API endpoint（ComfyUI API 模式） | ⭐⭐ |
| gemini prompts for image generation | 320 | 31 | $1.17 | 内容词；文章可对比 Gemini prompts vs ComfyUI workflows | ⭐⭐ |
| comfyui vs stable diffusion | 140 | 8 | $0 | 教育词；Olares 都支持，告知用户 ComfyUI 是 SD 的 GUI 前端 | ⭐⭐ |
| gemini ai image generator nsfw | 1,300 | 18 | $0 | 内容限制痛点；Olares 本地无审查（谨慎措辞） | ⭐⭐ |
| open source image generator | 110 | 44 | $0.79 | Olares 跑开源 FLUX / SD 作为 Imagen 开源替代 | ⭐⭐ |
| imagen 3 | 5,400 | 44 | $1.13 | 对比词：Imagen 3 vs FLUX.1 local；Olares 跑 FLUX 媲美质量 | ⭐⭐ |
| imagen 4 | 5,400 | 40 | $0 | 同上，新型号；FLUX.1 / SD 3.5 是其开源对标 | ⭐⭐ |
| google imagen 3 | 1,600 | 42 | $1.22 | 对比文入口：Google Imagen 3 vs 本地 FLUX on Olares | ⭐⭐ |
| gemini-3-pro-image-preview | 1,600 | 31 | $1.78 | 开发者搜索词；Olares ComfyUI API 是本地替代 | ⭐⭐ |
| gemini flash image | 210 | 24 | $1.01 | 低 KD；教程文可提供本地方案对比 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| google ai image generator | 18,100 | 55 | $1.20 | 信息 | 主词候选 | 量大，KD 55 可竞争，非 Google 品牌导航词——可写"Google AI Image Generator vs Open Source Alternatives"，Olares 作终极方案 |
| gemini image generator | 18,100 | 62 | $1.27 | 信息 | 主词候选 | 品牌量大但 KD 62；可做对比文切入，侧重 Gemini 限制 vs 本地无限制 |
| imagen 3 | 5,400 | 44 | $1.13 | 信息 | 主词候选 | KD 44 相对友好，型号词有研究意图；适合写"Imagen 3 Review & Open Source Alternatives" |
| imagen 4 | 5,400 | 40 | $0 | 信息 | 主词候选 | KD 40，CPC $0 说明无付费广告竞争，搜索者多为研究/对比意图；早布局红利高 |
| local ai image generator | 480 | 26 | $1.32 | 信息 | 主词候选 | ⭐ KD 26，Olares 直接场景词；量虽不大但意图极精准，转化价值高 |
| midjourney alternative free | 390 | 31 | $1.16 | 信息 | 主词候选 | ⭐ 价格痛点词；ComfyUI on Olares = 最佳免费替代 |
| can gemini generate images | 2,400 | 62 | $1.57 | 信息 | 次级 | 功能确认词，可并入 Gemini Image 综述文章 |
| gemini ai image generator free | 1,300 | 48 | $1.12 | 品牌/商业 | 次级 | 价格信号词；可在对比文中作"Gemini 免费额度分析" |
| google imagen 3 | 1,600 | 42 | $1.22 | 信息 | 次级 | ⭐ KD 42，并入 Imagen 3 主词文章 |
| gemini-3-pro-image-preview | 1,600 | 31 | $1.78 | 信息/商业 | 次级 | ⭐ 开发者词，高 CPC；并入 API 对比内容 |
| gemini 2.0 flash image generation | 590 | 46 | $1.23 | 信息 | 次级 | ⭐ 型号功能词，并入 Gemini Image 综述 |
| gemini prompts for image generation | 320 | 31 | $1.17 | 信息 | 次级 | ⭐ 教程意图；可用来对比 Gemini prompts vs ComfyUI workflows |
| gemini image generation api | 210 | 31 | $2.63 | 信息 | 次级 | ⭐ 开发者词，CPC 高；Olares 本地 API 替代叙事入口 |
| gemini flash image | 210 | 24 | $1.01 | 信息 | 次级 | ⭐ KD 仅 24，低竞争，并入 Gemini 型号对比 |
| why can't gemini generate images | 140 | 30 | $0 | 信息 | 次级 | ⭐ 痛点词；联合"anymore"变体（140+140=280量），导流本地无限制方案 |
| why can't gemini generate images anymore | 140 | 22 | $0 | 信息 | 次级 | ⭐⭐ KD 仅 22，最低竞争痛点词；文章结尾引出 ComfyUI/Olares |
| comfyui alternative | 170 | 7 | $2.19 | 信息 | 次级 | ⭐⭐ KD 仅 7！CPC $2.19；ComfyUI on Olares = 最简安装路径 |
| comfyui vs stable diffusion | 140 | 8 | $0 | 信息 | 次级 | ⭐⭐ KD 8，教育词；Olares 都支持，是选择起点 |
| run stable diffusion locally | 260 | 23 | $1.59 | 信息 | 次级 | ⭐ KD 23；Olares 教程词直接对应 |
| run flux locally | 70 | 21 | $0 | 信息 | 次级 | ⭐ KD 21；Olares FLUX 本地部署教程 |
| gemini ai image generator nsfw | 1,300 | 18 | $0 | 信息 | GEO | KD 极低，内容过滤痛点；可在 Olares 叙事中谨慎提及"无云端审查" |
| self-hosted ai image generator | 0 | 18 | $0 | 信息 | GEO | 量近零但语义极精准；抢 AI Overview/Perplexity 引用位 |
| run comfyui locally | 20 | 0 | $0 | 信息 | GEO | 量极小；Olares 文档/FAQ 覆盖，抢引用位 |
| imagen vs midjourney | 20 | 0 | $0 | 信息 | GEO | 比较意图强；在对比文中作 FAQ 段 |
| imagen 3 vs midjourney | 20 | 0 | $0 | 信息 | GEO | 同上 |

---

## 核心洞见

1. **品牌护城河**：Gemini 图像词（`gemini image generator` 18,100 / KD 62）已建立用户心智，品牌导航词（`google imagen` KD 88）几乎无法正面刚。但**非品牌路径**（`google ai image generator` KD 55、`imagen 3` KD 44、`imagen 4` KD 40）留有可攻空间——尤其是型号词和功能词，Google 自身内容并不一定已覆盖所有角度。

2. **可复制的打法**：目前 AI 图像生成竞争者（Midjourney、Adobe Firefly、OpenAI）都在写大词（`best ai image generator` KD 76）。Olares 应避开拥挤赛道，走**痛点 + 本地路线**：痛点词（`why can't gemini generate images anymore` KD 22、`gemini not generating images` KD 31）量虽小但意图明确，用户正在寻找替代；叠加教程词（`run stable diffusion locally` KD 23、`run flux locally` KD 21）做本地方案落地。

3. **对 Olares 最关键的词**：
   - `local ai image generator`（480 / KD 26）——直接场景词，转化最高
   - `why can't gemini generate images anymore`（140 / KD 22）——痛点词，触发替代诉求
   - `midjourney alternative free`（390 / KD 31）——价格痛点，ComfyUI on Olares 完全匹配

4. **最大攻击面**：Gemini 图像有**三重痛点**：① 免费额度仅 3 图/天（触发"not generating"/"can't generate"搜索）；② 内容审查严格（`nsfw` 词 1,300 量 KD 仅 18）；③ 图像数据上传 Google 云（隐私焦虑）。本地 ComfyUI + FLUX 一次性解决三个痛点，这是 Olares 最清晰的进攻角度。

5. **隐藏低 KD 金矿**：
   - `comfyui alternative`（170 / KD **7**）——KD 极低却 CPC $2.19，说明商业价值高但竞争者少
   - `comfyui vs stable diffusion`（140 / KD **8**）——教育词，Olares 可做"选型指南"
   - `why can't gemini generate images anymore`（140 / KD **22**）——痛点词，无付费竞争（CPC $0）
   - `gemini flash image`（210 / KD **24**）——型号词低竞争
   - `gemini image generation api`（210 / KD **31** / CPC **$2.63**）——开发者词，高价值低竞争

6. **GEO 前瞻布局**：以下词近零量但语义精准，适合写进 FAQ/前瞻段抢 AI Overview 引用位：
   - `self-hosted ai image generator`——Olares = self-hosted ComfyUI platform
   - `run comfyui locally`——Olares 一键安装 ComfyUI 的教程段
   - `imagen vs midjourney` / `imagen 3 vs midjourney`——对比 FAQ，植入 FLUX on Olares 作第三选项
   - `private ai image generator`——Olares 隐私叙事的锚点词

7. **与既有分析的关联**：`olares-500-keywords` 词表中 ComfyUI 相关词已有收录；本报告补充了 Imagen/Gemini 图像侧的**痛点词簇**（"不能生成图像"类，总量约 600，KD 22-31）与**型号对比词**（`imagen 3` / `imagen 4` KD 40-44）。建议在 ComfyUI 相关内容中**同时挂 Imagen/Gemini 痛点词**，扩大同一篇内容的语义覆盖。Olares 在 `local ai image generator`（KD 26）这个精准词上有明显机会，与既有的 `self-hosted` 叙事高度呼应。

---

*数据来源：SEMrush US 数据库（phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
