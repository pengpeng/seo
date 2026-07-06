# FLUX / FLUX.2 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：Black Forest Labs / bfl.ai，许可证分层（4B Apache 2.0；9B/dev FLUX NCL 非商用）

---

## 模型理解（前置）

FLUX 是 Black Forest Labs（BFL）出品的文生图旗舰模型系列。FLUX.1（2024年8月发布）的 12B 参数 dev 变体凭借极高图像质量，迅速成为开源图像生成社区标准，ComfyUI 最热门工作流载体之一。FLUX.2（2025年11月–2026年1月分批发布）升级为 32B dev 旗舰 + klein 4B/9B 小模型家族，在保持高质量的同时大幅压低 VRAM 门槛，并将多图参考编辑与文字渲染列为核心能力。FLUX.1 Kontext（2025年中发布）专攻指令式图像编辑，成为流量增长最快的子产品。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 文生图 + 图像编辑，开源图像生成社区事实标准 |
| 许可证 | **FLUX.2 [klein] 4B / 4B Base：Apache 2.0（商用友好）**；FLUX.2 [klein] 9B / 9B Base、FLUX.2 [dev] 32B：FLUX Non-Commercial License（研究/个人可用，商用需授权）；FLUX.1 [schnell]：Apache 2.0；FLUX.1 [dev] / Kontext [dev]：FLUX.1-dev NCL |
| 主仓库 / 分发 | GitHub [flux](https://github.com/black-forest-labs/flux)（★25.6K）/ [flux2](https://github.com/black-forest-labs/flux2)（★2.5K）；HuggingFace（FLUX.1-dev 月下载 ~87.6万次，FLUX.2-dev 月下载 ~29.3万次）；原生 ComfyUI + Diffusers 支持 |
| 参数 / VRAM 可跑性 | **klein 4B**：8.4–13GB VRAM（FP16），8GB 可跑（GGUF/NVFP4 量化），RTX 3060/4060 及以上；**klein 9B**：19.6–21.7GB FP16，FP8 量化约 12–15GB；**dev 32B**：80GB+ FP16，量化后约 24GB（单张 4090/5090 可跑）；**FLUX.1 dev（12B）**：GGUF Q4 约 6–8GB；**Olares One（RTX 5090 Mobile 24GB）**：可满载运行 klein 4B/9B FP8 及 dev 32B 量化版，FLUX.1 dev 全精度亦可 |
| 变体 / 型号 | FLUX.1 [schnell / dev / pro]；FLUX.1 Kontext [dev / pro / max]；FLUX.1 Redux [dev]；FLUX.1 Fill [dev]；FLUX.2 [dev] 32B；FLUX.2 [klein] 4B / 4B Base / 9B / 9B Base / 9B KV；各型号均有 FP8 / NVFP4 / GGUF 量化版 |
| 闭源对标 | **Midjourney**（T2I 创意生成）、**DALL·E / GPT Image**（OpenAI，API 生成）、**Adobe Firefly**（创意套件，商用图）、Ideogram（文字排版强） |
| Olares Market | **ComfyUI 已上架**（✅ [报告](/Users/pengpeng/seo/directions/market/reports/comfyui.md)）；FLUX 模型权重通过 ComfyUI 工作流加载，是 Olares 上运行 FLUX 的主要路径 |
| 来源 | [bfl.ai/models](https://bfl.ai/models)、[GitHub flux](https://github.com/black-forest-labs/flux)、[GitHub flux2](https://github.com/black-forest-labs/flux2)、[HuggingFace FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)、[HuggingFace FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev)、[BFL Blog FLUX.2 klein](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence) |

---

## 流量基线（Phase 1）

| 指标 | 数据 |
|------|------|
| 域名 | bfl.ai |
| SEMrush Rank | 73,839 |
| 月自然流量（US） | ~27,000 |
| 自然关键词数 | 1,804 |
| 流量估值 | $32,432 / 月 |
| 付费关键词 | 0（无 SEM 投放） |

### 官网 TOP 关键词（按流量排序，前 30）

| 关键词 | 排名 | 月量 | KD | 流量 | URL |
|--------|------|------|----|------|-----|
| black forest labs | 1 | 3,600 | 65 | 2,880 | bfl.ai/ |
| flux官网 | 1 | 1,300 | 75 | 1,040 | bfl.ai/ |
| flux kontext | 1 | 6,600 | 60 | 871 | bfl.ai/models/flux-kontext |
| flux 2.0 | 1 | 2,400 | 75 | 595 | bfl.ai/models/flux-2 |
| black forest lab | 1 | 720 | 58 | 576 | bfl.ai/ |
| flux.2 | 1 | 1,900 | 74 | 471 | bfl.ai/models/flux-2 |
| flux 2 | 1 | 1,900 | 80 | 471 | bfl.ai/models/flux-2 |
| flux.2 [klein] | 1 | 1,600 | 51 | 396 | bfl.ai/models/flux-2-klein |
| playground.bfl.ai | 1 | 1,600 | 29 | 396 | playground.bfl.ai/ |
| flux playground | 1 | 1,600 | 23 | 396 | playground.bfl.ai/ |
| fux max（含拼写变体） | 6 | 18,100 | 17 | 343 | bfl.ai/models/flux-2-max |
| flux-kontext | 1 | 1,300 | 57 | 322 | bfl.ai/models/flux-kontext |
| flux2 | 1 | 1,300 | 66 | 322 | bfl.ai/models/flux-2 |
| flux.1 kontext | 1 | 1,600 | 59 | 396 | bfl.ai/models/flux-kontext |
| flux ai image generator | 3 | 3,600 | 67 | 234 | bfl.ai/models/flux-2 |
| blackforest labs | 1 | 880 | 72 | 218 | bfl.ai/ |
| flux 2 klein | 2 | 2,400 | 46 | 196 | bfl.ai/models/flux-2-klein |
| flux context | 2 | 1,300 | 46 | 171 | bfl.ai/models/flux-kontext |
| flux image generator | 1 | 1,000 | 70 | 132 | bfl.ai/models/flux-2 |
| flux model | 1 | 1,000 | 50 | 132 | bfl.ai/models/ |
| flux 2 klein | 2 | 1,000 | 45 | 132 | bfl.ai/models/flux-2-klein |

> **注**：bfl.ai 流量高度集中于品牌词（"black forest labs"贡献约 10.7%）和 Kontext 子产品词（"flux kontext" 月量 6,600，bfl.ai 占位 #1 但 CTR 摊薄约 13%）。中文品牌词"flux官网"带来 1,040 流量，说明中文用户是重要来源。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| flux ai | 12,100 | 70 | $1.40 | 混合（含非AI含义） |
| flux kontext | 5,400 | 58 | $0.63 | 信息 |
| flux.1 | 2,900 | 87 | $0.90 | 信息 |
| flux 2.0 | 2,400 | 75 | $1.06 | 信息 |
| flux.1 dev | 2,400 | 70 | $1.64 | 信息 |
| flux.2 | 1,900 | 73 | $1.01 | 信息 |
| flux 2 | 1,900 | 77 | $1.01 | 信息 |
| flux dev | 1,600 | 69 | $1.17 | 信息 |
| flux 2 klein | 1,000 | 45 | $0.84 | 信息 |
| flux model | 1,000 | 50 | $0.79 | 信息 |
| flux lora | 1,000 | 42 | $1.41 | 信息 |
| flux 1 dev | 590 | 70 | $1.36 | 信息 |
| flux 2 dev | 480 | 61 | $2.34 | 信息 |
| flux models | 480 | 48 | $0.79 | 信息 |
| flux 1 schnell | 260 | 71 | $0.91 | 信息 |
| flux image generation | 210 | 69 | $1.26 | 信息 |
| black forest labs | 3,600 | 65 | $4.71 | 导航 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| flux kontext comfyui | 1,300 | 40 | $0 | 信息 |
| comfyui flux | 390 | 49 | $0.73 | 信息 |
| flux schnell workflow comfyui | 390 | 21 | $0 | 信息 ⭐ |
| comfyui flux controlnet sketch workflow | 320 | 29 | $0 | 信息 ⭐ |
| flux.1 kontext comfyui | 320 | 47 | $0 | 信息 |
| install flux context comfyui tutorial | 320 | 38 | $0 | 信息 |
| flux comfyui | 210 | 32 | $1.12 | 信息 |
| flux workflow comfyui | 170 | 34 | $5.07 | 信息 |
| comfyui flux workflow | 140 | 49 | $2.60 | 信息 |
| flux inpaint workflow comfyui | 140 | 29 | $0 | 信息 ⭐ |
| flux comfyui workflow | 50 | 26 | $0 | 信息 ⭐ |
| flux dev comfyui | 50 | 29 | $0 | 信息 ⭐ |
| flux 2 comfyui | 40–70 | 34 | $0 | 信息 |
| flux 2 klein comfyui | 70 | 0 | $0 | 信息（GEO） |
| flux ollama | 20 | 0 | $0 | 信息（GEO） |
| flux vllm | — | — | — | （近零量，GEO 候选） |

> `flux kontext comfyui` 以 1,300 月量、KD 40 高居引擎组合词首位，是近期搜索量增长最快的子话题之一（Kontext 产品 2025 年中发布后快速起量）。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| flux on pc | 4,400 | 36 | $1.98 | 信息 ⭐ |
| run flux locally | 70 | 21 | $0 | 信息 ⭐ |
| running flux locally | 70 | 26 | $0 | 信息 ⭐ |
| how to run flux locally | 50 | 21 | $0 | 信息 ⭐ |
| flux gguf | 170 | 32 | $0 | 信息 |
| flux install | 110 | 40 | $0 | 信息 |
| flux fp8 | 90 | 38 | $0 | 信息 |
| flux nf4 | 40 | 26 | $0 | 信息 ⭐ |
| flux 1 dev quantized | — | — | — | 信息（GEO） |
| flux vram | 20 | 0 | $0 | 信息（GEO） |
| flux locally | 20 | 0 | $0 | 信息（GEO） |
| flux local | 20 | 0 | $0 | 信息（GEO） |
| flux on windows | 880 | 48 | $0 | 信息 |
| flux nunchaku | 90 | 13 | $0 | 信息 ⭐ |

> **高亮**：`flux on pc` 月量高达 4,400、KD 仅 36——这是整个本地部署词群中量价比最高的词，且竞争度远低于品牌词，是 Olares/消费级 GPU 叙事最大的流量入口。

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| midjourney alternative | 590 | 33 | $1.83 | 信息 / 商业 |
| flux vs stable diffusion | 210 | 24 | $0.49 | 信息 ⭐ |
| local image generation | 90 | 17 | $0 | 信息 ⭐ |
| flux alternative | 90 | 19 | $0 | 信息 ⭐ |
| flux nunchaku | 90 | 13 | $0 | 信息 ⭐ |
| flux vs midjourney | 30 | 19 | $6.92 | 信息 / 商业 ⭐ |
| open source midjourney alternative | 20 | 0 | $0 | 信息（GEO） |
| open source image model | 10 | 0 | $0 | 信息（GEO） |
| best open source image model | 20 | 0 | $0 | 信息（GEO） |

> **注意**：`flux alternative` 的 phrase_related 会大量命中"焊锡助焊剂"（英文 flux 多义），SEO 内容需要在标题 / H1 明确"AI image model"语境，避免被混搜意图稀释。

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| flux comfyui | 210 | 32 | $1.12 | ComfyUI 已在 Olares Market 一键部署，加载 FLUX 权重即可运行；"FLUX + ComfyUI on Olares" 是最短部署路径 | ⭐⭐⭐ |
| flux kontext comfyui | 1,300 | 40 | $0 | Kontext 指令编辑 + ComfyUI 工作流，在 Olares 上离线运行，数据不出机；量最大的引擎组合词 | ⭐⭐⭐ |
| flux on pc | 4,400 | 36 | $1.98 | Olares One（RTX 5090 Mobile 24GB）是消费级"PC"里 FLUX 最舒适的运行环境；可主打"一台电脑跑满血 FLUX" | ⭐⭐⭐ |
| run flux locally | 70 | 21 | $0 | 本地私有化核心词；Olares 提供"一键起 ComfyUI 跑 FLUX"的最短路径，且数据不离本机 | ⭐⭐⭐ |
| flux vs midjourney | 30 | 19 | $6.92 | 攻击面：Midjourney 按月收费 + 数据上云；FLUX on Olares = 本地免费跑、隐私 100% | ⭐⭐⭐ |
| flux vs stable diffusion | 210 | 24 | $0.49 | 同类对比；FLUX 架构更现代，Olares 同时支持 FLUX 与 SD，ComfyUI 覆盖全家族 | ⭐⭐ |
| local image generation | 90 | 17 | $0 | Olares 定位"本地 AI 一站式平台"；本地图像生成是 Agent 工具链重要一环 | ⭐⭐⭐ |
| flux alternative | 90 | 19 | $0 | 面向 Midjourney/Firefly 付费用户；Olares 提供"0 月费、本地跑 FLUX 替代" | ⭐⭐ |
| flux nunchaku | 90 | 13 | $0 | SVDQuant 量化可让 FLUX.2 dev 32B 压到 24GB 以内，与 Olares One GPU 完美吻合；技术深度内容机会 | ⭐⭐ |
| flux gguf | 170 | 32 | $0 | GGUF 量化让 FLUX.1 dev 在 8GB 显存卡上可跑，Olares 支持 Linux GPU 加速（NVIDIA 及 AMD） | ⭐⭐ |
| open source midjourney alternative | 20 | 0 | $0 | GEO 抢发：FLUX + Olares = "免费、开源、本地跑的 Midjourney 替代品" | ⭐⭐⭐ |
| best open source image model | 20 | 0 | $0 | GEO 抢发：FLUX.2 是 2026 年最热开源图像模型，Olares 平台叙事锚点 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| flux on pc | 4,400 | 36 | $1.98 | 信息 | **主词候选** | 本地部署词群量最大（4.4K）、KD 适中（36）；Olares One 即是最佳"PC"选型 |
| flux kontext | 5,400 | 58 | $0.63 | 信息 | **主词候选** | bfl.ai 流量第三大词；KD 较高但可围绕 Kontext 工作流出内容，带 ComfyUI Olares 角度 |
| flux kontext comfyui | 1,300 | 40 | $0 | 信息 | **主词候选** | 量大（1.3K）、KD 40，竞争可打；Olares + ComfyUI 一键运行 Kontext 指令编辑 |
| flux 2 klein | 1,000 | 45 | $0.84 | 信息 | **主词候选** | 新模型词，KD 45；klein 4B Apache 2.0 可商用，Olares One 满血跑 |
| flux model | 1,000 | 50 | $0.79 | 信息 | **主词候选** | 通用型号词，有量（1K）；作为 Olares 文章的自然覆盖词 |
| flux lora | 1,000 | 42 | $1.41 | 信息 | **次级** | LoRA 微调词，技术受众；Olares + ComfyUI 本地微调叙事入口 |
| comfyui flux | 390 | 49 | $0.73 | 信息 | **次级** | 引擎组合词，量稳（390）；指向 Olares Market ComfyUI 应用页 |
| flux gguf | 170 | 32 | $0 | 信息 | **次级** | 量化部署词；低 KD（32）适合出技术向"如何在低 VRAM 跑 FLUX"内容 |
| midjourney alternative | 590 | 33 | $1.83 | 信息/商业 | **主词候选** | 高意图、有 CPC（$1.83）；FLUX 是最强开源对标，Olares 提供本地运行 |
| flux vs stable diffusion | 210 | 24 | $0.49 | 信息 | **次级** ⭐ | KD 低（24）、量合理；同类对比文，Olares ComfyUI 同时支持两者 |
| flux alternative | 90 | 19 | $0 | 信息 | **次级** ⭐ | KD 19 极低；需在内容标题明确"AI image"区分助焊剂含义；Olares 角度：本地免费替代 Midjourney |
| flux comfyui | 210 | 32 | $1.12 | 信息 | **次级** ⭐ | KD 32，Olares Market 直接对应；最短"一键部署"内容钩子 |
| run flux locally | 70 | 21 | $0 | 信息 | **次级** ⭐ | KD 21，高意图精准词；配合 Olares One / ComfyUI 部署流程 |
| flux vs midjourney | 30 | 19 | $6.92 | 信息/商业 | **次级** ⭐ | KD 低（19）但 CPC 高（$6.92）显示强商业意图；攻击面：Midjourney 按月订阅 vs FLUX 本地免费 |
| flux nunchaku | 90 | 13 | $0 | 信息 | **GEO** ⭐ | KD 13，量小但技术受众精准；SVDQuant 让 32B dev 压到 24GB 正好匹配 Olares One |
| local image generation | 90 | 17 | $0 | 信息 | **次级** ⭐ | KD 17，无 CPC 竞争；Olares 平台"本地 AI" 叙事总入口 |
| open source midjourney alternative | 20 | 0 | $0 | 信息 | **GEO** | 近零量，AI Overview/Perplexity 抢占位；"FLUX on Olares = 开源 Midjourney 平替" |
| best open source image model | 20 | 0 | $0 | 信息 | **GEO** | 近零量但语义精准；2026 年 FLUX.2 是社区公认最强，Olares 可做 GEO 内容锚点 |
| flux 2 klein comfyui | 70 | 0 | $0 | 信息 | **GEO** | 刚发布（2026-01），搜索量建立中；GEO 抢发"FLUX.2 klein on ComfyUI / Olares" |
| flux on windows | 880 | 48 | $0 | 信息 | **次级** | 量（880）、KD 适中；Olares WSL2 路径覆盖 Windows 用户 |

---

## 核心洞见

### 1. 搜索心智是否建立

**已建立，但以品牌名和子产品名驱动，而非"FLUX.2"版本号本身。** bfl.ai 月流量 ~27K，"black forest labs"（3,600）、"flux kontext"（6,600）是最大流量来源。"flux.2"版本号词（1,900 vol）和"flux 2 klein"（1,000 vol）搜索量相对平淡，说明用户更习惯搜品牌名或子产品名（Kontext）。FLUX.1 时代的词（"flux.1"，2,900 vol）比 FLUX.2 更热，表明社区惯性仍在 FLUX.1。Kontext 是当前 bfl.ai 最重要的增长引擎，在流量贡献和词量上都超过 FLUX.2 版本词。

### 2. 消费级 GPU / Olares One 本地可跑性

**可跑，叙事成立，且窗口宽。**

- **FLUX.1 [schnell]（Apache 2.0）**：GGUF Q4 约 6–8GB，RTX 3060/4060 可跑，Olares One 24GB 完全富余。
- **FLUX.2 [klein] 4B（Apache 2.0）**：FP16 仅 8.4GB，NVFP4 更低；RTX 3060/4070 可跑，Olares One 轻松运行。
- **FLUX.2 [klein] 9B**：FP8 约 12–15GB，Olares One 24GB 可跑。
- **FLUX.2 [dev] 32B（非商用）**：全精度 80GB+，但 FP8/Nunchaku 量化后约 16–24GB，Olares One 24GB 踩着线可跑。
- **FLUX.1 [dev]（12B，非商用）**：GGUF Q4 约 6–8GB，Olares One 远超要求。

**Olares One（RTX 5090 Mobile 24GB）覆盖 FLUX 全家族的可用变体**（Apache 2.0 的 schnell/klein-4B 商用友好；dev/9B 非商用研究用途）。

### 3. 许可证是否商用友好

**分层，需在内容中明确区分：**

| 变体 | 许可 | 商用推荐度 |
|------|------|-----------|
| FLUX.1 [schnell] | Apache 2.0 | ✅ 完全商用 |
| FLUX.2 [klein] 4B / 4B Base | Apache 2.0 | ✅ 完全商用，**主推** |
| FLUX.2 [klein] 9B / dev 32B | FLUX NCL | ⚠️ 非商用（研究/个人） |
| FLUX.1 [dev] / Kontext [dev] | FLUX.1-dev NCL | ⚠️ 非商用 |

**面向 Olares 商业叙事（商用友好模型）：聚焦 FLUX.2 [klein] 4B 和 FLUX.1 [schnell]**；技术/研究用途可涵盖 dev/9B，但需标注非商用限制，避免合规风险。

### 4. 对 Olares 最关键的 2–3 个词

1. **`flux on pc`（4,400 vol，KD 36）**：量最大、KD 可竞争的本地部署词；Olares One 是最佳"个人 PC 级"运行 FLUX 的设备。内容角度："用一台机器在家跑满血 FLUX"。
2. **`flux kontext comfyui`（1,300 vol，KD 40）**：Kontext 指令编辑 × ComfyUI 工作流，正是 Olares Market 应用承载的场景；可做"Olares + ComfyUI 一键运行 FLUX Kontext"教程。
3. **`run flux locally`（70 vol，KD 21）⭐**：精准本地部署意图，KD 极低；适合作为 Olares "本地 AI" 叙事的长尾入口。

### 5. 新模型 GEO 抢发窗口

FLUX.2 [klein] 于 2026-01-15 发布，搜索量仍在建立期（`flux 2 klein comfyui` 70 vol、`flux 2 klein` 1,000 vol 但 KD 45），GEO 抢发机会窗口未关闭：

- `flux 2 klein comfyui`（KD 0，GEO）：抢占 AI Overview/Perplexity "如何在 ComfyUI 跑 FLUX.2 klein" 的引用位。
- `best open source image model 2026`（近零量，GEO）：FLUX.2 klein 发布后是该问题的最新答案，Olares 可作为"跑这个模型最简单的平台"入局。
- `open source midjourney alternative`（近零量，GEO）：语义精准，Midjourney 用户转移意图强。
- `flux nunchaku`（90 vol，KD 13，GEO 友好）：SVDQuant 量化技术词，受众精准，技术深度文可占据 AI Overview。

### 6. 闭源对标与攻击面

| 对标 | 攻击面 |
|------|--------|
| **Midjourney** | 月订阅 $10–$120；生成数据用于训练；无本地模式；API 受限 |
| **DALL·E / GPT Image** | 按 token 计费；Azure/OpenAI 合规约束；无自托管 |
| **Adobe Firefly** | Creative Cloud 捆绑；图片归 Adobe 使用条款管辖；海外合规成本高 |

**FLUX 的攻击叙事**：Apache 2.0 许可（klein 4B）= 零使用费 + 无数据上传 + 自由商用；通过 Olares + ComfyUI 在家部署 = "Stop renting Midjourney, own your image AI"。

### 7. 与 models.md 同类 family 及关联

- 同章（02-image）待调研：Ideogram 4（文字渲染强，对标 GPT Image）、Qwen-Image（Apache 2.0，文档图处理）——三者覆盖不同子场景，可共用"best open source image model"入口词。
- Olares Market ComfyUI 报告（`market/reports/comfyui.md`）已覆盖 ComfyUI 整体流量，本报告的 FLUX × ComfyUI 词是互补层。
- 与商业竞品报告：Midjourney（✅）和 Adobe Firefly（✅）已有报告，`flux vs midjourney`/`flux alternative` 内容可引用这两份报告的攻击角度，跨报告内容簇联动。

---

*数据来源：SEMrush US（domain_rank、resource_organic、phrase_this、phrase_these、phrase_related、phrase_fullsearch）| 2026-07-06*

*搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
