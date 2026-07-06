# Wan 2.2 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：Wan-AI / github.com/Wan-Video/Wan2.2，Apache 2.0
> 无独立官网，SEO 主战场在 HuggingFace / GitHub / ComfyUI 社区内容页（降级模式，跳过 Phase 1 域名报告）

## 模型理解（前置）

Wan 2.2 是阿里云 Wan-AI（通义万相）团队于 2025 年 7 月 28 日发布的开源视频生成模型套件，采用 Diffusion Transformer（DiT）+ Flow Matching 架构，旗舰 A14B 系列引入时间维度双专家 MoE（Mixture-of-Experts），总参 27B 但每步推理仅激活 14B，在保持推理成本的同时大幅提升质量。轻量版 TI2V-5B 搭载高压缩比 Wan2.2-VAE（64x 总压缩率），单张 RTX 4090（24GB）即可在 9 分钟内生成 5 秒 720p@24fps 视频，是 Sora 关停后最热门的本地可跑开源视频生成模型，ComfyUI 已深度集成并有专属自定义节点。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 T2V/I2V/S2V 视频生成套件，MoE A14B + 消费级 5B，Sora 本地平替 |
| 许可证 | **Apache 2.0**（商用友好，可无限制自托管与商业部署） |
| 主仓库 / 分发 | GitHub `Wan-Video/Wan2.2`（★ 16.5k）、HuggingFace `Wan-AI/`、ModelScope |
| 参数 / VRAM 可跑性 | TI2V-5B：8–12GB FP16 / 6–8GB FP8 → **消费级 RTX 3060/4070 可跑**；A14B：24–48GB FP8 / 12–24GB GGUF Q5 → **Olares One（24GB）可跑 480p，TI2V-5B 可跑 720p** |
| 变体 / 型号 | T2V-A14B（文生视频 MoE）、I2V-A14B（图生视频 MoE）、TI2V-5B（统一 T2V+I2V 高压缩）、S2V-14B（语音驱动视频） |
| 闭源对标 | Sora（关停）/ Kling / Runway / Pika |
| Olares Market | ComfyUI ✅ 已上架（[报告](/Users/pengpeng/seo/directions/market/reports/comfyui.md)）；Wan 2.2 通过 ComfyUI 工作流部署，无需独立 Olares 应用 |
| 来源 | [GitHub Wan2.2](https://github.com/Wan-Video/Wan2.2)、[HuggingFace Wan-AI](https://huggingface.co/Wan-AI)、[NYU RITS 综述](https://rits.shanghai.nyu.edu/ai/wan2-2-alibabas-open%E2%80%91source-breakthrough-in-ai-video-generation/)、[ComfyUI 部署指南](https://www.thundercompute.com/blog/wan-2-2-comfyui-ai-video-model) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。Intent：0=Commercial / 1=Informational / 2=Navigational / 3=Transactional。

### 品牌 / 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| wan ai | 8,100 | 78 | $1.22 | 2（导航） |
| wan 2.2 | 14,800 | 61 | $0.78 | 1 |
| wan video | 3,600 | 74 | $0.72 | 2 |
| wan2.2 | 5,400 | 59 | $0.61 | 1 |
| wan 2.2 animate | 4,400 | 39 | $0.63 | 1 |
| wan2.2 animate | 3,600 | 39 | $0.45 | 1 |
| wan 2.5 | 3,600 | 31 | $1.12 | 1 |
| wan animate | 1,900 | 39 | $0.89 | 1 |
| wan ai video | 880 | 63 | $0.99 | 2 |
| wan 2.2 i2v | 320 | 43 | $1.08 | 1 |
| wan 2.2 a14b ⭐ | 320 | 31 | $0.00 | 1 |
| wan 2.2 huggingface | 320 | 66 | $1.22 | 2 |
| wan2.2 ti2v 5b ⭐ | 260 | 42 | $0.00 | 1 |
| wan 2.2 5b ⭐ | 260 | 40 | $1.12 | 1 |
| wan image to video | 480 | 52 | $1.13 | 1 |
| wan2.2 s2v ⭐ | 590 | 39 | $1.02 | 1 |
| wan s2v ⭐ | 210 | 42 | $1.17 | 1 |
| wan2.2 i2v | 1,600 | 55 | $0.90 | 1 |
| wan2.2 t2v | 720 | 52 | $0.00 | 1 |
| wan i2v | 720 | 65 | $0.95 | 1 |
| wan 2.2 t2v ⭐ | 110 | 25 | $0.74 | 1 |
| wan 14b ⭐ | 70 | 25 | $0.00 | 1 |
| wan vace ⭐ | 1,300 | 35 | $0.36 | 1 |
| wan video generation | 170 | 71 | $1.10 | 1 |
| wan video model | 170 | 75 | $1.25 | 1 |
| wan 2.1 | 6,600 | — | $0.86 | 1 |
| wan2.2 nsfw ⭐ | 1,600 | 30 | $1.41 | 1 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| wan2.2 comfyui ⭐ | 1,600 | 34 | $0.82 | 1 |
| wan comfyui ⭐ | 210 | 35 | $0.93 | 1 |
| wan2.1 comfyui | 1,900 | 45 | $0.00 | 1 |
| comfyui video generation ⭐ | 170 | 30 | $1.39 | 1 |
| wan 2.2 diffusers | 20 | — | $0.00 | 1 |
| wan diffusers | 20 | — | $0.00 | 1 |

*注：`wan2.2 ollama` 月量为 0——Wan 2.2 不走 Ollama，ComfyUI 是唯一主流引擎路径。*

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| wan2.2 gguf ⭐ | 1,600 | 32 | $0.00 | 1 |
| wan 2.2 gguf ⭐ | 390 | 29 | $0.00 | 1 |
| wan2.2 fp8 ⭐ | 480 | 40 | $0.00 | 1 |
| wan 2.2 fp8 ⭐ | 90 | 28 | $0.00 | 1 |
| run wan 2.2 locally ⭐ | 260 | 28 | $0.00 | 1 |
| wan 2.2 local ⭐ | 170 | 32 | $2.58 | 1 |
| wan 2.2 install ⭐ | 170 | 33 | $0.00 | 1 |
| wan 2.2 vram ⭐ | 30 | — | $0.00 | 1 |
| how to run wan 2.2 locally ⭐ | 170 | — | $1.66 | 1 |
| how to install wan 2.2 comfyui ⭐ | 90 | — | $0.00 | 1 |
| how to install wan 2.2 ⭐ | 70 | — | $0.00 | 1 |
| is wan 2.2 free ⭐ | 90 | — | $1.28 | 1 |
| what is wan 2.2 ⭐ | 110 | — | $0.54 | 1 |
| how to use wan 2.2 ⭐ | 140 | — | $1.05 | 1 |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| sora alternative ⭐⭐ | 210 | 11 | $1.09 | 1 |
| open source sora ⭐ | 50 | 23 | $0.00 | 1 |
| open source video generation ⭐ | 30 | 24 | $1.65 | 1 |
| ai video generator open source ⭐ | 30 | 15 | $1.40 | 1 |
| wan vs hunyuan ⭐ | 50 | 5 | $0.00 | 1 |
| wan vs kling ⭐ | 30 | — | $0.00 | 1 |
| wan video alternative ⭐ | 10 | — | $0.00 | 1 |
| free video generation ai | 210 | 86 | $1.26 | 0 |
| run wan locally ⭐ | 20 | — | $0.00 | 1 |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|-----|-----|-------------|--------|
| wan2.2 comfyui | 1,600 | 34 | $0.82 | Olares Market 已上架 ComfyUI，一键安装即可导入 Wan 2.2 工作流——最简部署路径 | ⭐⭐⭐ |
| run wan 2.2 locally | 260 | 28 | $0.00 | 直接映射「在自己的设备上本地跑 Wan」；Olares One（24GB）满足 A14B 需求 | ⭐⭐⭐ |
| wan2.2 gguf | 1,600 | 32 | $0.00 | GGUF 量化让 A14B 在 8–16GB GPU 上可跑，拓宽 Olares 非旗舰用户覆盖 | ⭐⭐⭐ |
| wan 2.2 local | 170 | 32 | $2.58 | 本地部署核心词；Olares = 私有化部署的完整方案，数据不出机 | ⭐⭐⭐ |
| sora alternative | 210 | 11 | $1.09 | Sora 关停后流量溢出，Wan 2.2 是最直接的本地开源平替，KD 极低 | ⭐⭐⭐ |
| open source video generation | 30 | 24 | $1.65 | 顶部意图词，吸引寻找闭源替代方案的用户，导向 Olares 本地 AI 叙事 | ⭐⭐⭐ |
| wan2.2 fp8 | 480 | 40 | $0.00 | FP8 精度是 24GB GPU（Olares One）运行 A14B 的关键技术词 | ⭐⭐ |
| wan 2.2 install | 170 | 33 | $0.00 | 部署教程类；可示范「Olares + ComfyUI 一键安装 Wan 2.2」流程 | ⭐⭐ |
| wan comfyui | 210 | 35 | $0.93 | 同 wan2.2 comfyui，更宽泛；覆盖跨版本 Wan 系列 ComfyUI 用户 | ⭐⭐ |
| ai video generator open source | 30 | 15 | $1.40 | 品类顶部词，KD=15 极低，可作进入点，导流至 Wan 2.2+Olares 叙事 | ⭐⭐ |
| wan vs hunyuan | 50 | 5 | $0.00 | 超低 KD，对比类 GEO 抢发；可拓展为「自托管视频模型横评」内容 | ⭐⭐ |
| wan 2.2 vram | 30 | — | $0.00 | 硬件配置型长尾，Olares One 规格表可直接回答；GEO 抢发位 | ⭐⭐ |
| wan 2.2 a14b | 320 | 31 | $0.00 | 型号精确词，受众明确（知道旗舰型号的高意向用户） | ⭐⭐ |
| wan2.2 nsfw | 1,600 | 30 | $1.41 | 高流量，KD 低；Olares 本地部署天然解决云端内容审查问题（隐私叙事） | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|-----|-----|------|------|---------------------------|
| wan 2.2 | 14,800 | 61 | $0.78 | 信息 | 主词候选 | 品牌主词，量大但 KD=61 中高；做教程/对比锚点页 |
| wan ai | 8,100 | 78 | $1.22 | 导航 | 次级 | 导航意图，竞争激烈；适合品牌内容而非单独排名 |
| wan2.2 | 5,400 | 59 | $0.61 | 信息 | 主词候选 | "wan 2.2" 拼写变体，同量级；与主词合并优化 |
| wan 2.2 animate | 4,400 | 39 | $0.63 | 信息 | **主词候选 ⭐** | KD 仅 39 但月量 4,400——animate 功能词叠加品牌，性价比最高的主词机会 |
| wan2.2 animate | 3,600 | 39 | $0.45 | 信息 | **主词候选 ⭐** | 同上拼写变体；合并可获近万搜索量，KD<40 |
| wan 2.5 | 3,600 | 31 | $1.12 | 信息 | 次级 | 下一代版本预期词，KD 低；GEO 前哨（Wan 2.5 尚未发布） |
| wan2.2 i2v | 1,600 | 55 | $0.90 | 信息 | 次级 | 图生视频功能词，有量；与 I2V-A14B 教程挂钩 |
| wan2.2 comfyui | 1,600 | 34 | $0.82 | 信息 | **次级 ⭐** | KD=34 低，月量 1,600；Olares ComfyUI 一键部署叙事锚点 |
| wan2.2 gguf | 1,600 | 32 | $0.00 | 信息 | **次级 ⭐** | 量化部署词，KD=32；Olares 低 VRAM 用户入口 |
| wan2.2 nsfw | 1,600 | 30 | $1.41 | 信息 | 次级 | 隐私/本地部署强动机词，KD=30；内容尺度需自行评估 |
| wan2.2 s2v | 590 | 39 | $1.02 | 信息 | 次级 | 语音驱动视频，差异化功能；S2V-14B 是 Wan 独有卖点 |
| wan2.2 fp8 | 480 | 40 | $0.00 | 信息 | 次级 | 精度/推理词；受众是知道 fp8 的进阶用户 |
| wan image to video | 480 | 52 | $1.13 | 信息 | 次级 | 功能描述词；竞争稍高，适合长文覆盖 |
| wan 2.2 gguf | 390 | 29 | $0.00 | 信息 | **次级 ⭐** | 与 wan2.2 gguf 合并优化，KD<30 |
| wan 2.2 i2v | 320 | 43 | $1.08 | 信息 | 次级 | 型号精确词，有量；受众知道型号的高意向用户 |
| wan 2.2 a14b | 320 | 31 | $0.00 | 信息 | **次级 ⭐** | KD=31，型号精确词；Olares One 规格直接对应 |
| wan 2.2 huggingface | 320 | 66 | $1.22 | 导航 | 次级 | 导航意图（找 HF 页面），KD 高；写 HF 直达指南时覆盖 |
| run wan 2.2 locally | 260 | 28 | $0.00 | 信息 | **次级 ⭐** | KD=28，部署类教程核心词；Olares「一键跑」叙事完美对应 |
| wan 2.2 5b | 260 | 40 | $1.12 | 信息 | 次级 | TI2V-5B 的自然语言指称；消费级用户首选型号 |
| wan2.2 ti2v 5b | 260 | 42 | $0.00 | 信息 | 次级 | 精确型号词，与 wan 2.2 5b 合并 |
| sora alternative | 210 | 11 | $1.09 | 信息 | **主词候选 ⭐⭐** | KD=11 极低！Sora 关停后流量溢出，最易突破的对比攻击词 |
| wan comfyui | 210 | 35 | $0.93 | 信息 | **次级 ⭐** | 跨版本 Wan ComfyUI 词，与 wan2.2 comfyui 合并 |
| wan s2v | 210 | 42 | $1.17 | 信息 | 次级 | S2V 功能词，独特差异化；适合专题内容 |
| free video generation ai | 210 | 86 | $1.26 | 商业 | 次级 | 量大 KD=86，竞争极高；仅作覆盖词 |
| how to use wan 2.2 | 140 | — | $1.05 | 信息 | 次级 | 问题词；教程/入门文章自然覆盖 |
| how to run wan 2.2 locally | 170 | — | $1.66 | 信息 | **次级 ⭐** | 部署教程核心问题词；CPC 高说明有商业价值 |
| wan 2.2 local | 170 | 32 | $2.58 | 信息 | **次级 ⭐** | CPC=$2.58 高，KD=32，部署意图明确 |
| wan vace | 1,300 | 35 | $0.36 | 信息 | 次级 | VACE（视频编辑功能）新词，有增长趋势 |
| wan 2.2 install | 170 | 33 | $0.00 | 信息 | 次级 ⭐ | 安装教程词；与 how to install 合并 |
| comfyui video generation | 170 | 30 | $1.39 | 信息 | 次级 ⭐ | 品类词，KD=30；Wan 2.2 是最好的 ComfyUI 视频答案 |
| open source sora | 50 | 23 | $0.00 | 信息 | **GEO ⭐** | 量少但 KD=23，AI Overview / Perplexity 抢发位 |
| open source video generation | 30 | 24 | $1.65 | 信息 | **GEO ⭐** | 品类信息词，KD=24；内容覆盖后可持续引流 |
| ai video generator open source | 30 | 15 | $1.40 | 信息 | **GEO ⭐** | KD=15，Olares 最易拿到 AI Overview 引用位 |
| wan vs hunyuan | 50 | 5 | $0.00 | 信息 | **GEO ⭐** | KD=5 极低，横评词；GEO 抢发后可占据 AI 问答引用 |
| wan vs kling | 30 | — | $0.00 | 信息 | **GEO ⭐** | 近零量但语义明确，Sora/Kling 用户迁移路径词 |
| wan video alternative | 10 | — | $0.00 | 信息 | **GEO ⭐** | 零量 GEO 候选，抢占 Perplexity / AI Overview 回答 |
| wan 2.2 vram | 30 | — | $0.00 | 信息 | **GEO ⭐** | 硬件选型问题词；Olares One 规格表直接命中 |
| is wan 2.2 free | 90 | — | $1.28 | 信息 | GEO | Apache 2.0 问题词，问答覆盖即可 |

---

## 核心洞见

### 1. 搜索心智是否建立

**已基本建立，且还在加速。** "wan 2.2" US 月均 14,800，"wan2.2" 5,400，"wan ai" 8,100——核心品牌词合计已超 28,000/月（US）。Trend 数据显示自 2025 年 7 月发布后持续在高位，2026 年 Q1-Q2 仍保持 ≥0.54 相对指数（与高峰相比）。搜索心智已成立，不需要靠 HuggingFace/Ollama 直达引流——用户已经在主动搜索 Wan 品牌词。

### 2. 消费级 GPU / Olares One 能否本地跑

**完全可以，且是核心叙事。**

- **TI2V-5B**：RTX 3060（12GB）即可运行 480p，RTX 4070（12-16GB）可跑 720p FP16；Olares One（RTX 5090 Mobile 24GB）可流畅跑 720p。
- **A14B 旗舰**：需要 24GB（FP8 精度）或 12-16GB（GGUF Q5）；Olares One（24GB）可运行 480p FP8——正好踩在边界上，480p 生成可行，720p 旗舰品质需 48GB。
- **关键结论**：Olares One 是「能跑 Wan 2.2 的最小主流消费级配置」，叙事完全成立。Olares 平台 NVIDIA GPU 支持最成熟（CUDA 全覆盖），ComfyUI 已上架 Olares Market，部署路径最短。

### 3. 许可证是否商用友好

**是，Apache 2.0，可直接主推。** 无地区限制，无商业条款，任何场景均可自托管部署和商业使用——这是与 Kling、Runway、Pika 等闭源商业模型的本质差异，也是 Olares「数据主权」叙事的天然武器。

### 4. 对 Olares 最关键的 2-3 个词

1. **`wan2.2 comfyui`**（1,600/月，KD=34）：Olares Market 已有 ComfyUI，一键安装即可导入 Wan 2.2 工作流——这是 Olares 区别于"手动搭环境"的最直接部署差异点。
2. **`sora alternative`**（210/月，KD=11）：Sora 关停后流量持续溢出（Trend 最近一个月达到峰值 1.00），KD 极低——最容易拿到排名的品类入口词，Wan 2.2 是最强的本地 Sora 平替。
3. **`run wan 2.2 locally`**（260/月，KD=28）：部署叙事核心词，CPC 为 $0 但流量精准——搜索此词的用户就是 Olares 的目标用户（想在自己硬件上跑视频 AI 的人）。

### 5. 新模型 GEO 抢发窗口

以下词量少但语义精准，AI Overview / Perplexity 引用位尚未被权威内容占据，属于**立即可操作的 GEO 机会**：

| 词 | 量 | KD | 抢发理由 |
|---|---|---|---------|
| ai video generator open source | 30 | 15 | KD=15，品类顶部词，最易拿 AI 引用 |
| wan vs hunyuan | 50 | 5 | KD=5，无人写横评；Wan 胜 Hunyuan 的对比分析 |
| open source sora | 50 | 23 | Sora 关停叙事，GEO 引用价值高 |
| open source video generation | 30 | 24 | 品类词，答案型内容 |
| wan 2.2 vram | 30 | — | 硬件选型问答，Olares One 规格直接命中 |
| wan video alternative | 10 | — | 近零量但意图精准；抢占 Perplexity 直接回答 |
| wan vs kling | 30 | — | 对比型，Kling 仍活跃，攻击面清晰 |

### 6. 闭源对标与攻击面

- **Sora**（OpenAI，已于 2025 年关停）：最大攻击面是「关停即失去访问权」，Wan 2.2 本地部署永久可用。
- **Kling**（快手，月订阅 $9.9–$29.9）：按月收费 + 有内容审查 + 视频有水印；Wan 2.2 本地无限次生成 + 无水印 + Apache 2.0。
- **Runway Gen-3/4**（$12–$76/月）：高质量但云端限额；本地 Wan A14B 一次性算力投入后无边际成本。
- **Pika 2.2**（$8–$70/月）：同上，限额制云服务。
- **通用攻击面**：所有闭源方均有「token/分钟计费 → 超量停生成」「云端内容过滤无法绕过」「隐私风险」三个痛点，Wan 2.2 + Olares 全部解决。

### 7. 与 model/models.md 同类 family 的关联

- **同章（03-video）**：SkyReels-V2（Wan 架构衍生，暂无报告）；两者可写横评簇。
- **闭源对标已有报告**：Sora ✅、Runway ✅、Pika ✅——可从这三份报告的高机会词反向引流到 Wan 2.2 对比内容。
- **跨章关联**：ComfyUI 在 market/reports ✅，Wan 2.2 通过 ComfyUI 部署——文章可跨引。
- **Keyword 簇建议**（给 seo-content 层）：`wan comfyui + run wan 2.2 locally + wan 2.2 install` 可聚合为「如何在本地用 Olares 跑 Wan 2.2」教程簇；`sora alternative + open source sora + wan vs sora` 可聚合为「Sora 本地开源替代方案」对比簇。

---

*数据来源：SEMrush US（phrase_these × 4 批次、phrase_related、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
