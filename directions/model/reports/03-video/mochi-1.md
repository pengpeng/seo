# Mochi 1 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：Genmo AI（genmo.ai），Apache 2.0

## 模型理解（前置）

Mochi 1 是 Genmo AI（前身 genmo.ai）于 2024 年 10 月开源的纯文本转视频（t2v）扩散 Transformer 模型，参数量 10B。以流畅的运动质量著称，在同期开源 t2v 模型中以运动逼真度为核心卖点区别于 HunyuanVideo（注重视觉保真度）和 LTX-Video（注重推理速度）。许可证为 Apache 2.0，是当时业界最宽松的视频生成大模型开源协议，无地区限制、无商业条款附加。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 10B 纯 t2v 扩散 Transformer，高运动质量，Apache 2.0 |
| 许可证 | **Apache 2.0**（商用完全自由，业界最宽松级别）|
| 主仓库 / 分发 | GitHub [genmoai/mochi](https://github.com/genmoai/mochi)（★ 数千）；HuggingFace `genmoai/mochi-1-preview`；ComfyUI 自定义节点（stable-diffusion-art 有专项教程）|
| 参数 / VRAM 可跑性 | 10B；bf16 约 20GB VRAM；fp8 量化可降至约 12–16GB；**Olares One（24GB VRAM）可全精度运行**；高端消费级 GPU（RTX 3090/4090/5090）可跑 |
| 变体 / 型号 | 仅 `mochi-1-preview`（截至 2026-07），无 i2v / turbo / 尺寸细分变体 |
| 闭源对标 | Runway Gen-3 Alpha（按秒计费）、Sora（OpenAI，订阅制）、Kling（快手，中国服务条款）|
| Olares Market | ComfyUI 已上架（引擎路径），无 Mochi 1 专属应用；可通过 ComfyUI + Mochi 自定义节点一键跑 |
| 来源 | GitHub genmoai/mochi；HuggingFace genmoai/mochi-1-preview；genmo.ai 官网；stable-diffusion-art.com/mochi-comfyui/ |

---

## 流量基线（Phase 1）

> genmo.ai 有独立官网，故做域名基线。注意：genmo.ai 流量几乎全部来自 Mochi 1 相关词，不存在多产品混杂稀释问题。

| 指标 | 数据 |
|------|------|
| 域名 | genmo.ai |
| SEMrush Rank | 619,913 |
| 月自然流量（US） | 2,150 |
| 关键词数 | 217 |
| 流量估值 | $4,736 / 月 |

### 官网 TOP 关键词（按流量排序，前 15 位）

| 关键词 | 排名 | 月量 | KD | 流量（US/mo） | URL |
|--------|------|------|----|--------------|-----|
| genmo ai | 1 | 1,000 | 59 | 800 | genmo.ai/ |
| mochi1 | 3 | 3,600 | 25 | 295 | genmo.ai/ |
| genmo.ai | 1 | 170 | 54 | 136 | genmo.ai/ |
| alpha.genmo | 1 | 170 | 42 | 136 | genmo.ai/ |
| mochi ai | 2 | 880 | 31 | 116 | genmo.ai/ |
| genmo mochi 1 | 1 | 140 | 42 | 112 | genmo.ai/ |
| mochi1 (blog) | 7 | 3,600 | 25 | 79 | genmo.ai/blog |
| ginimo | 4 | 1,300 | 25 | 57 | genmo.ai/ |
| genmo | 1 | 1,900 | 49 | 49 | genmo.ai/ |
| genmo ia | 1 | 50 | 35 | 40 | genmo.ai/ |
| genmo mochi 1 ai video generator | 1 | 50 | 50 | 40 | genmo.ai/ |
| mochi 1 | 3 | 390 | 22 | 11 | genmo.ai/ |
| mochi ai video | 2 | 70 | 19 | 9 | genmo.ai/ |
| mochi-1 | 3 | 110 | 28 | 9 | genmo.ai/ |
| open source video generation models | 10 | 210 | 29 | 3 | genmo.ai/ |

> **洞见**：genmo.ai 全站流量极低（2,150/月），但关键词质量尚可。`mochi1`（3,600量）给域名带去 295 + 79 = 374 次点击，是最大流量词，但排名 #3，被 mochi1ai.com（第三方聚合站）截流。`mochi ai`（880量）需注意：该词的语义主要指向 character chat AI（eMochi 等应用），genmo.ai 靠 Mochi 1 视频模型蹭到 #2 位，但搜索者意图对齐度不稳定。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| mochi1 | 3,600–4,400 | 25–47 | $6.91 | nav |
| mochi 1 | 390 | 22 | $0.91 | info |
| ⭐ genmo mochi 1 | 170 | 43 | $1.23 | trans |
| mochi-1 | 110 | 28 | $0.99 | info |
| ⭐ mochi ai video | 90 | 17 | $0.72 | info |
| mochiai | 70 | 5 | $5.48 | info |
| mochi1 ai | 30 | 32 | $0.94 | nav |
| ⭐ mochi 1 ai | 30 | 19 | $0.75 | info |
| ⭐ mochi ai video generator | 30 | 13 | $0.86 | info |
| genmo mochi | 20 | 0 | $1.19 | — |
| ⭐ mochi 1 comfyui | 20 | 0 | $0 | — |
| mochi 1 huggingface | 20 | 0 | $0 | — |

> **注意**：`mochi1` 在 Semrush 不同查询中出现 3,600 与 4,400 两个量级，原因是 resource_organic 数据与 phrase_these 数据采集时间窗略有差异；取实际使用中位值约 3,600–4,400。该词的高 CPC（$6.91）来源复杂：部分来自 Mochi Health（减重 GLP-1 服务平台，同名词高竞争）混入付费竞价，但 SERP 前三位已被 mochi1ai.com / genmoai/mochi GitHub / genmo.ai 占据，说明搜索意图在该词上已基本"属于"视频模型社区。

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ⭐ mochi comfyui | 20 | 0 | $0 | — |
| ⭐ mochi 1 comfyui | 20 | 0 | $0 | — |
| ⭐ mochi local | 20 | 0 | $0 | — |

> Mochi 1 无 Ollama / vLLM 支持（视频模型，不走 LLM 推理路径）。ComfyUI 是主要部署引擎，HuggingFace Diffusers 是代码级部署路径。这两个词量极低但近零竞争，属 GEO 前哨。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| mochi 1 huggingface | 20 | 0 | $0 | — |
| mochi local | 20 | 0 | $0 | — |
| mochi 1 comfyui | 20 | 0 | $0 | — |
| mochi github | 20 | 0 | $0 | — |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| open source video generation models | 210 | 29 | $1.43 | info |
| ⭐ open source sora | 50 | 23 | $0 | info |
| ⭐ runway ml alternative | 40 | 10 | $2.61 | info |
| open source text to video | 40 | 51 | $1.60 | info |
| ⭐ open source sora alternative | 20 | 0 | $0 | — |
| runway alternative | 10 | 0 | $3.39 | — |

**同类开源视频模型的对比参照：**

| 关键词 | 月量 | KD | CPC |
|--------|------|----|----|
| wan video | 3,600 | 74 | $0.72 |
| hunyuanvideo | 1,900 | 61 | $0.81 |
| cogvideox | 2,400 | 38 | $0.78 |
| ltx video | 2,400 | 31 | $1.51 |
| cogvideo | 1,300 | 32 | $0.93 |

> Mochi 1 的品牌词量（`mochi1` ~4,400）与 HunyuanVideo（1,900）、CogVideoX（2,400）在同一量级，但落后于 Wan Video（3,600 + `wan2.1` 1,300）。LTX Video（2,400）是最接近的竞品（同属 Apache 2.0，更轻量）。

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|-------|
| mochi 1 | 390 | 22 | $0.91 | 本地部署完整指南：ComfyUI on Olares One（24GB VRAM 全精度）或 fp8 量化在消费级 GPU 上跑；Apache 2.0 零商业限制 | ⭐⭐⭐ |
| mochi comfyui | 20 | 0 | $0 | ComfyUI 已在 Olares Market，Mochi 1 节点一步安装；GEO 抢发：AI Overview 首选的一步部署答案 | ⭐⭐⭐ |
| mochi local | 20 | 0 | $0 | 数据不出设备、无 API 限速、永久可用——本地 AI 叙事核心 | ⭐⭐⭐ |
| runway ml alternative | 40 | 10 | $2.61 | Runway Gen-3 按秒计费（约 $0.05/s），Mochi 1 on Olares = 一次付硬件费用永久免费；Apache 2.0 无版权风险 | ⭐⭐⭐ |
| open source video generation models | 210 | 29 | $1.43 | Olares 平台可一站部署多个开源视频模型（Mochi 1、CogVideoX、LTX-Video），做"本地视频生成全家桶"叙事 | ⭐⭐ |
| open source sora alternative | 20 | 0 | $0 | Sora 仅限 ChatGPT Plus 订阅、无商业独立许可；Mochi 1 on Olares = 自建、自有、零订阅 | ⭐⭐⭐ |
| open source sora | 50 | 23 | $0 | GEO 定位：Perplexity / AI Overview 被问"open source Sora"时，引用 Mochi 1 的 Olares 部署路径 | ⭐⭐ |
| mochi ai video generator | 30 | 13 | $0.86 | 低 KD + 商业意图，指向"我想用它生成视频"——部署 how-to 的最佳入口词 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断 |
|--------|------|----|----|------|------|-----------|
| mochi1 | 3,600–4,400 | 25–47 | $6.91 | nav | 主词候选 | 最高量品牌词；注意 mochi1ai.com 第三方站抢 #1 位，genmo.ai 排 #3；Olares 内容可以作为第三方部署指南竞争这个词 |
| mochi 1 | 390 | 22 | $0.91 | info | 主词候选 | KD 22 + 信息意图；部署指南（ComfyUI on Olares）绝佳落地词；genmo.ai 当前 #3 但流量只 11 |
| open source video generation models | 210 | 29 | $1.43 | info | 主词候选 | 品类 listicle 机会词；KD 29 可攻；Olares 可做"在单台设备上部署多款开源视频模型"叙事 |
| genmo mochi 1 | 170 | 43 | $1.23 | trans | 次级 | 高交易意图但 KD 43 偏高；作为主词的次级佐证词 |
| mochi-1 | 110 | 28 | $0.99 | info | 次级 | 拼写变体，与 `mochi 1` 合并进一篇 |
| mochi ai video | 90 | 17 | $0.72 | info | 次级 | KD 17，极低竞争；意图明确（想生成视频）；并入部署指南 |
| runway ml alternative | 40 | 10 | $2.61 | info | 主词候选（战略） | KD 10 + CPC $2.61 高商业价值；Mochi 1 on Olares = 零订阅 Runway 替代；主攻替代文 |
| open source sora | 50 | 23 | $0 | info | 次级 | CPC $0 但意图纯净、GEO 价值高；作为对比替代文的 FAQ 锚词 |
| mochi ai video generator | 30 | 13 | $0.86 | info | 次级 | KD 13，低竞争入口词；并入部署 how-to |
| mochi comfyui | 20 | 0 | $0 | — | GEO | 近零竞争；AI Overview / Perplexity 的 ComfyUI 安装问答前沿阵地 |
| mochi local | 20 | 0 | $0 | — | GEO | 本地部署意图；FAQ 块直答 |
| open source sora alternative | 20 | 0 | $0 | — | GEO | 战略替代词；KD 0 + Sora 月量 9,900 作背书；GEO 抢发首选 |
| mochi 1 comfyui | 20 | 0 | $0 | — | GEO | 具体型号 + 引擎组合，意图极精准；直答格式最优 |
| genmo mochi | 20 | 0 | $1.19 | — | 次级 | 品牌+型号拼写，并入主词文章 |

---

## 核心洞见

**1. 搜索心智：已建立但量级有限，与同类模型对比居中**

`mochi1`（3,600–4,400）是已建立的独立心智词，SERP 已被视频模型生态（GitHub、HuggingFace、genmo.ai）占据。但与 Wan Video（3,600）、CogVideoX（2,400）、HunyuanVideo（1,900）相比，品牌量级相当，无明显领先。主要痛点：mochi1ai.com 等第三方站抢了 #1 位，官方 genmo.ai 站排 #3，流量仅 ~370/月；**Olares 可作为第三方"Mochi 1 部署权威"内容角色**，而非依赖 genmo.ai 自身 SEO 势能。

**2. VRAM 可跑性：Olares One 可全精度运行，叙事前提成立**

10B 模型在 bf16 下约需 20GB VRAM；fp8 量化可降至约 12–16GB。Olares One（RTX 5090 Mobile，24GB GDDR7）可全精度运行。消费级 RTX 3090（24GB）、RTX 4090（24GB）亦可全精度。RTX 4080（16GB）需 fp8。这一硬件门槛高于 LTX-Video（更轻量），但目标用户（Olares One 用户）完全覆盖——**"24GB VRAM 全精度运行 Mochi 1"是硬件卖点叙事的精准锚点**。

**3. 许可证是最强差异化卖点，可全力主推**

Apache 2.0 是视频生成领域最宽松的许可级别：
- Wan Video（3,600量）：腾讯 Wan Video License（有商业限制条款）
- HunyuanVideo：Tencent Hunyuan Community License（同上）
- LTX-Video：Apache 2.0（竞争对手，但参数量更小、运动质量逊色）
- CogVideoX：Apache 2.0

Mochi 1 + Apache 2.0 = **可商用、无地区限制、本地推理完全私有**，是自托管视频生成的顶级合规选项。**许可证卖点应在所有 Olares 相关内容中强打**。

**4. 对 Olares 最关键的 3 个词**

- `mochi 1`（390，KD 22）——核心部署指南主词，KD 低、意图信息、竞争可攻；
- `runway ml alternative`（40，KD 10，$2.61 CPC）——高商业价值替代词，打"零订阅本地视频生成"；
- `open source video generation models`（210，KD 29）——品类 listicle 主词，Olares 可做多模型横向对比。

**5. GEO 抢发窗口**

以下词量近零但语义精准，AI Overview / Perplexity 在直答这类问题时无权威内容可引用：
- `mochi comfyui` / `mochi 1 comfyui` — ComfyUI 安装步骤直答
- `mochi local` / `run mochi 1 locally` — 本地部署 FAQ
- `open source sora alternative` — Sora 替代品问答
- `apache 2.0 video generation model` — 许可证专项问答

这类词通过 FAQ 块 / 直答段可在 AI Overview 中抢占引用位，与搜索量高低无关。

**6. 闭源对标与攻击面**

| 对标 | 攻击点 |
|------|--------|
| Runway Gen-3 Alpha | 按秒计费（约 $0.05/s）；隐私（云端生成）；商业视频受版权条款约束 |
| Sora（OpenAI）| 仅限 ChatGPT Plus 订阅；无独立 API / 商业许可；输出归属模糊 |
| Kling（快手）| 中国服务条款；数据主权风险；未公开许可证细节 |
| Pika | 付费套餐限额；云端 |

Mochi 1 on Olares 的核心攻击叙事：**一次硬件投入 vs. 永续订阅费；Apache 2.0 vs. 专有条款；数据不出设备 vs. 云端服务器**。

**7. 同类 family 关联（model/models.md 03-video 章）**

- HunyuanVideo（已有报告）：量级相当，但许可证逊色，VRAM 更高
- Wan Video（量 > Mochi 1）：快手出品，许可证有限制，是 Mochi 1 在中文生态的最大竞品
- LTX-Video（Apache 2.0，轻量）：Mochi 1 的最直接开源竞品——同协议、低门槛，但运动质量弱于 Mochi 1
- CogVideoX（Apache 2.0，2,400量）：同协议，但 Zhipu 出品，VRAM 需求类似

Mochi 1 的内容差异点：**Apache 2.0 + 运动质量最优 + Olares One 硬件天然匹配（24GB VRAM）**，三点合一在同类模型中无重复竞争者。

---

*数据来源：SEMrush US（phrase_this, phrase_these, phrase_related, phrase_fullsearch, phrase_questions, phrase_organic, domain_rank, resource_organic）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
*注：`mochi ai`（880）的搜索意图主要指向 eMochi 等 AI character chat 应用，非视频生成模型，Olares 内容不宜以该词作主词。*
