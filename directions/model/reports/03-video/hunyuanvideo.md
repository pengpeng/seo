# HunyuanVideo 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：Tencent Hunyuan / github.com/Tencent-Hunyuan/HunyuanVideo-1.5，Tencent Hunyuan Community License（排除 EU/UK/KR）
> 无独立官网，SEO 主战场在 HuggingFace / GitHub / ComfyUI 社区内容页（降级模式，跳过 Phase 1 域名报告）

## 模型理解（前置）

HunyuanVideo-1.5 是腾讯 Hunyuan 团队于 2025 年 11 月 20 日发布的开源视频生成模型，以 8.3B 参数（相比原始 13B 版大幅精简）实现了 T2V（文生视频）+ I2V（图生视频）统一生成，原生支持 480p/720p 输出并内置分步蒸馏超分辨率网络可上采样至 1080p。架构上引入 SSTA（Selective and Sliding Tile Attention）新型注意力机制以及 Qwen 2.5-VL 7B + byT5 字形感知双文本编码器，在消费级 GPU（官方最低 14GB 显存，可开 offloading）上即可本地运行，是 Sora/Kling/Runway 等闭源商业视频平台的开源可自托管替代。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 T2V/I2V 视频生成模型，8.3B，支持 1080p SR，Sora/Kling 本地平替 |
| 许可证 | **Tencent Hunyuan Community License**（**排除 EU/UK/KR 商业部署**；个人研究与非商业自托管不受限，引用前以官方 LICENSE 为准） |
| 主仓库 / 分发 | GitHub `Tencent-Hunyuan/HunyuanVideo-1.5`、HuggingFace `tencent/HunyuanVideo-1.5`、ComfyUI 原生支持 |
| 参数 / VRAM 可跑性 | 8.3B；FP16 全精度：~24–28GB（RTX 4090/3090 边界）；FP8+CPU offload：~10–12GB（RTX 4070 12GB 可跑）；GGUF Q4+offload：~8–10GB（RTX 4060 Ti 可跑）；**Olares One（RTX 5090 Mobile 24GB）：FP16 舒适跑 720p → 内置 SR 上采样 1080p，是最小满血消费级配置** |
| 变体 / 型号 | T2V（文生视频）、I2V（图生视频）、Avatar（数字人）、Foley（视频音效生成）；SR Step Distilled（720→1080p 超分）；CFG Distilled 快速版（8/12 步生成） |
| 闭源对标 | Sora（OpenAI，2025 年停服）/ Kling AI（快手，月订阅）/ Runway Gen-3 Alpha（月订阅）/ Pika 2.2 |
| Olares Market | ComfyUI ✅ 已上架（[报告](/Users/pengpeng/seo/directions/market/reports/comfyui.md)）；HunyuanVideo-1.5 通过 ComfyUI 原生节点部署，无需独立 Olares 应用 |
| 来源 | [GitHub Tencent-Hunyuan/HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)、[HuggingFace tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5)、[LocalAI Master 部署指南](https://localaimaster.com/blog/hunyuan-video-guide)、[WillItRunAI VRAM 指南](https://willitrunai.com/blog/hunyuanvideo-1-5-vram-requirements) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。Intent：0=商业 / 1=信息 / 2=导航 / 3=交易。

### 品牌 / 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| hunyuan video | 2,900 | 61 | $0.81 | 1 |
| hunyuanvideo | 1,900 | 61 | $0.81 | 1,0 |
| hunyuanvideo-1.5 | 880 | 45 | $0.85 | 1 |
| hunyuanvideo-i2v ⭐ | 880 | 29 | $0.00 | 1 |
| hunyuanvideo-avatar | 720 | 48 | $1.04 | 0 |
| hunyuan image to video | 720 | 56 | $0.98 | 1 |
| hunyuan video 1.5 | 720 | 47 | $1.62 | 1 |
| hunyuan video 1.5 nsfw ⭐ | 480 | 25 | $0.00 | 1 |
| hunyuanvideo-foley | 480 | 39 | $0.00 | 1 |
| tencent video animation | 590 | 44 | $1.06 | 1 |
| hunyuan video avatar ⭐ | 320 | 34 | $1.07 | 1 |
| chinese ai video generator ⭐ | 390 | 33 | $0.96 | 1 |
| chinese ai video generator free ⭐ | 320 | 22 | $0.67 | 1 |
| hunyuan ai video | 170 | 53 | $0.89 | 1 |
| tencent hunyuan video | 170 | 50 | $1.00 | 1 |
| hunyuanvideo 1.5 | 140 | 39 | $0.85 | 1 |
| hunyuan 1.5 | 70 | 45 | $0.96 | 1 |
| hunyuan video i2v ⭐ | 70 | 18 | $0.00 | 1 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| hunyuan video comfyui ⭐ | 260 | 32 | $0.00 | 1 |
| hunyuan video 1.5 comfyui | 10 | 0 | $0.00 | 1 |

*注：`hunyuan video ollama` / `hunyuan video vllm` 月量为 0——HunyuanVideo 是视频扩散模型，不走 Ollama/vLLM 文本推理路径；ComfyUI 是唯一主流本地引擎。*

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| hunyuan video gguf ⭐ | 590 | 28 | $0.00 | 1 |
| hunyuan video local ⭐ | 40 | 27 | $0.00 | 1 |
| hunyuan video fp8 | 20 | 0 | $0.00 | — |
| hunyuan video vram | 20 | 0 | $0.00 | — |

*注：`run hunyuanvideo locally`、`hunyuanvideo install`、`hunyuan video 1.5 local` 等长尾词月量为 0——属 GEO 抢发候选，AI Overview / Perplexity 引用位尚空。*

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| free ai video generator | 74,000 | 83 | $1.12 | 1 |
| local ai video generator ⭐ | 390 | 26 | $1.43 | 1 |
| sora alternative ⭐ | 210 | 11 | $1.09 | 1 |
| open source sora ⭐ | 50 | 23 | $0.00 | 1 |
| wan vs hunyuan ⭐ | 50 | 5 | $0.00 | 1,0 |
| open source video generation ⭐ | 30 | 24 | $1.65 | 1 |
| kling alternative | 20 | 0 | $2.31 | — |
| sora alternative open source | 20 | 0 | $2.34 | — |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|-----|-----|-------------|--------|
| hunyuan video comfyui | 260 | 32 | $0.00 | Olares Market 已上架 ComfyUI，一键安装即可加载 HunyuanVideo-1.5 工作流——比手搭 Python 环境快 95%；是 Olares 对"本地视频 AI"最短部署路径的具体示范 | ⭐⭐⭐ |
| hunyuan video gguf | 590 | 28 | $0.00 | GGUF 量化让 8.3B 模型在 8–12GB GPU 上可跑，大幅拓宽 Olares 非旗舰用户的覆盖面（RTX 4060/4070 也能用）；KD=28 是本组最高量+低 KD 词 | ⭐⭐⭐ |
| sora alternative | 210 | 11 | $1.09 | Sora 2025 年已停服，需求外溢明显；KD=11 极低——本组最容易拿到排名的品类入口词。Olares = 本地部署平台，HunyuanVideo-1.5 = Sora 开源替代，叙事完美闭环 | ⭐⭐⭐ |
| local ai video generator | 390 | 26 | $1.43 | 品类直接意图词，KD=26，CPC=$1.43 显示商业价值；Olares 「本地 AI 一体机」叙事天然命中——不租订阅、不限用量、数据不出设备 | ⭐⭐⭐ |
| hunyuan video local | 40 | 27 | $0.00 | 部署意图明确；搜索此词的用户就是 Olares 目标用户（想在自己设备上跑视频 AI），Olares One 24GB 是最舒适的消费级方案 | ⭐⭐⭐ |
| chinese ai video generator free | 320 | 22 | $0.67 | KD=22 超低，可攻可守；HunyuanVideo-1.5 是"中国团队出品 + 开源免费"的最强具身，Olares 作为本地部署平台放大"free"优势（无 token 上限） | ⭐⭐⭐ |
| hunyuanvideo-i2v | 880 | 29 | $0.00 | 图生视频功能词，KD=29 出人意料地低；I2V 是 1.5 版新增能力，Olares 本地部署可无审查地跑任意图片 → 视频生成 | ⭐⭐ |
| hunyuan video 1.5 nsfw | 480 | 25 | $0.00 | 高流量 + KD=25 低；Olares 本地部署天然解决云端内容限制，是隐私叙事（数据不出本机）的强动机词 | ⭐⭐ |
| wan vs hunyuan | 50 | 5 | $0.00 | KD=5 极低，零竞争；可产出「自托管视频模型横评：Wan 2.2 vs HunyuanVideo-1.5」，GEO 抢发后锁定 AI Overview / Perplexity 引用位，对应 Olares 「一键切换模型」叙事 | ⭐⭐ |
| open source sora | 50 | 23 | $0.00 | Sora 叙事延伸，KD=23，AI 问答引用价值高；Olares 可作为「运行开源 Sora 平替的平台」定位出现 | ⭐⭐ |
| open source video generation | 30 | 24 | $1.65 | 品类信息词，KD=24，CPC 高说明有商业意图；内容覆盖后可持续引流至 Olares + HunyuanVideo 组合方案 | ⭐⭐ |
| chinese ai video generator | 390 | 33 | $0.96 | 腾讯 + 开源 + 本地这三点叠加，在"Chinese AI"叙事里差异明显；KD=33，在比较类内容里可自然覆盖 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|-----|-----|------|------|---------------------------|
| hunyuan video | 2,900 | 61 | $0.81 | 信息 | 主词候选 | 品牌主词，量大但 KD=61 偏高；适合做锚点教程/对比页，难单独冲排名 |
| hunyuanvideo | 1,900 | 61 | $0.81 | 信息,商业 | 主词候选 | 与 "hunyuan video" 的拼写变体，合并优化；量级与 KD 同量级 |
| hunyuanvideo-1.5 | 880 | 45 | $0.85 | 信息 | 主词候选 | 连字符版 GitHub 风格型号词，月量=880，KD=45 可争；1.5 版精确受众 |
| hunyuanvideo-i2v ⭐ | 880 | 29 | $0.00 | 信息 | **次级 ⭐** | 量=880、KD=29——功能词中最具性价比，I2V 是 1.5 版核心差异点 |
| hunyuan video 1.5 | 720 | 47 | $1.62 | 信息 | 主词候选 | CPC=$1.62 高，说明竞争者愿为此词付费；对应 1.5 版本介绍类文章 |
| hunyuan video gguf ⭐ | 590 | 28 | $0.00 | 信息 | **次级 ⭐** | KD=28，量=590，是本地部署组最高流量词；Olares 低 VRAM 用户入口，优先级高 |
| hunyuan video 1.5 nsfw ⭐ | 480 | 25 | $0.00 | 信息 | 次级 | KD=25 低，量=480；隐私部署动机词，内容尺度需评估 |
| hunyuanvideo-foley | 480 | 39 | $0.00 | 信息 | 次级 | Foley 音效生成变体，独特功能差异；KD=39，适合垂直专题 |
| chinese ai video generator ⭐ | 390 | 33 | $0.96 | 信息 | 次级 | 带"中国"标签的视频生成器词，KD=33，可作进入点覆盖 |
| local ai video generator ⭐ | 390 | 26 | $1.43 | 信息 | **主词候选 ⭐** | KD=26，CPC=$1.43，月量=390；本地部署顶部词，品类机会最高的非品牌词 |
| chinese ai video generator free ⭐ | 320 | 22 | $0.67 | 信息 | **次级 ⭐** | KD=22 极低，量=320；「开源免费+本地」叙事命中，Olares 最易拿排名的特色词 |
| hunyuan video comfyui ⭐ | 260 | 32 | $0.00 | 信息 | **次级 ⭐** | KD=32，月量=260；Olares Market ComfyUI 一键部署叙事的直接入口词 |
| sora alternative ⭐ | 210 | 11 | $1.09 | 信息 | **主词候选 ⭐⭐** | KD=11 全表最低！Sora 停服后流量溢出，HunyuanVideo-1.5 是本地 Sora 平替首选；最易突破的对比攻击词 |
| hunyuan video local ⭐ | 40 | 27 | $0.00 | 信息 | 次级 ⭐ | 部署意图精准，KD=27；搜索者=Olares 目标用户，内容对应部署教程 |
| open source sora ⭐ | 50 | 23 | $0.00 | 信息 | **GEO ⭐** | 量少但 KD=23，AI Overview 引用位尚空；可和 "sora alternative" 合页覆盖 |
| wan vs hunyuan ⭐ | 50 | 5 | $0.00 | 信息,商业 | **GEO ⭐** | KD=5 极低，横评词空位；与 wan-2.md 交叉，做「两大开源视频模型横评+Olares 统一部署」内容，GEO 抢发后锁位 |
| open source video generation ⭐ | 30 | 24 | $1.65 | 信息 | **GEO ⭐** | 品类信息词，KD=24，CPC 高；答案型内容命中后可持续引流 |
| sora alternative open source | 20 | 0 | $2.34 | 信息 | **GEO ⭐** | 近零量但 CPC=$2.34 极高说明有商业意图；AI Overview 抢发后可截获高价值用户 |
| run hunyuanvideo locally | 0 | — | $0.00 | — | **GEO ⭐** | 当前零量，语义精准；随 1.5 版本传播增长可预期；Perplexity/ChatGPT 引用位抢发 |

---

## 核心洞见

### 1. 搜索心智是否建立

**已初步建立，但体量比 Wan 2.2 小 4–5 倍，且仍在增长期。** "hunyuan video" US 月均 2,900，"hunyuanvideo" 1,900，"hunyuan video 1.5" 720——品牌词合计约 7,000/月（US），远低于 Wan 2.2 的 28,000+。HunyuanVideo 在中国社区影响更强，英文搜索生态尚未充分爆发。然而有一个异常值：**"hunyuanvideo-i2v" 月量达 880，KD 仅 29**——I2V（图生视频）功能的搜索心智已经独立形成，这是 1.5 版本的核心差异化入口。

### 2. 消费级 GPU / Olares One 能否本地跑

**完全可以，且 Olares One 是最舒适的消费级配置。**

- **FP16 全精度**：需 24–28GB；RTX 4090 踩边界，Olares One（RTX 5090 Mobile 24GB GDDR7）可流畅运行 720p → 内置 SR 上采样至 1080p。
- **FP8 + CPU text encoder offload**：约 10–12GB；RTX 4070 12GB / 4070 Ti Super 16GB 可跑。
- **GGUF Q4 + offload**：约 8–10GB；RTX 4060 Ti 16GB 可跑。
- **关键结论**：Olares One 是「按官方推荐规格运行 HunyuanVideo-1.5 的最小消费级整机配置」，可直接做 FP16 720p + SR 1080p，无需量化妥协。叙事完全成立。Olares 平台 NVIDIA GPU 支持最成熟（CUDA 全覆盖），ComfyUI 已上架 Olares Market，部署路径最短。

### 3. 许可证是否商用友好

**有条件友好，需在内容中明确注明地区限制。** Tencent Hunyuan Community License 明确**排除 EU、UK、KR** 的商业部署用途。对 Olares 的含义：
- **内容策略**：不宜在面向 EU/UK/KR 受众的文章中强推「用 Olares 跑 HunyuanVideo 做商业项目」，但**个人自用/研究场景不受限**；
- **叙事侧重**：强调「本地部署 = 私有化使用、数据不出机」，规避云端 token 限制，而不是「商业友好可自由再分发」；
- **对比角度**：与 Wan 2.2（Apache 2.0）相比，许可证是 HunyuanVideo 的弱点——在对比文中需如实说明；Olares 用户若要无限制商用，Wan 2.2 是更安全的选择。

### 4. 对 Olares 最关键的 2-3 个词

1. **`sora alternative`**（210/月，KD=11）：全表 KD 最低的有量词；Sora 停服后流量溢出窗口仍在，HunyuanVideo-1.5 + Olares = 「本地运行、永久可用的 Sora 替代方案」，攻击面最清晰。
2. **`local ai video generator`**（390/月，KD=26，CPC=$1.43）：品类顶部词，KD 低且 CPC 高，说明商业意图真实；Olares「本地 AI 一体机」定位天然命中，不需要月订阅、数据不出设备。
3. **`hunyuan video gguf`**（590/月，KD=28）：本地部署组最高量词，KD=28 可攻；GGUF 量化拓宽到 8–12GB GPU 用户，覆盖比 24GB 旗舰更宽的 Olares 用户群。

### 5. 新模型 GEO 抢发窗口

以下词量少但语义精准，AI Overview / Perplexity / ChatGPT 引用位尚未被权威内容占据：

| 词 | 量 | KD | 抢发理由 |
|---|---|---|---------|
| wan vs hunyuan | 50 | 5 | KD=5 全表最低；两大顶流开源视频模型横评，Olares 可作统一部署平台出现 |
| open source sora | 50 | 23 | Sora 停服叙事，AI 问答高引用价值 |
| sora alternative open source | 20 | 0 | 近零量但 CPC=$2.34，商业意图强；AI Overview 抢先位 |
| chinese ai video generator free | 320 | 22 | KD=22，量=320 不算小；腾讯出品+开源+本地 = 差异化答案 |
| open source video generation | 30 | 24 | 品类词，答案型内容命中后持续引流 |
| run hunyuanvideo locally | 0 | — | 现在零量，随模型传播增长可预期；Perplexity 引用位先占 |
| hunyuan video vram | 20 | 0 | 硬件选型问答，Olares One 规格表直接命中 |

### 6. 闭源对标与攻击面

- **Sora**（OpenAI，2025 年已停服）：最大攻击面是「产品关停即失去所有访问权」；HunyuanVideo-1.5 本地部署 = 永久可用。
- **Kling AI**（快手，$9.9–$29.9/月）：按月计费 + 云端内容审查 + 生成有水印；Olares 本地无限次生成、无水印、无审查。
- **Runway Gen-3 Alpha**（$12–$76/月）：高质量但算力限额；本地 24GB GPU 一次性投入后无边际成本。
- **通用攻击面**：三者均有「token/分钟计费导致超量停生成」「云端内容过滤无法绕过」「视频数据上传云端隐私风险」三个痛点；HunyuanVideo-1.5 + Olares 全部解决。
- **注意**：HunyuanVideo-1.5 的许可证限制（EU/UK/KR）是 Wan 2.2（Apache 2.0）相比的弱点，在与 Wan 2.2 对比时需如实说明。

### 7. 与 model/models.md 同类 family 及跨报告关联

- **同章（03-video）竞品**：Wan 2.2 ✅ 已有报告——"wan vs hunyuan"（KD=5）是两份报告的共同 GEO 抢发点，可写「开源视频模型大横评：Wan 2.2 vs HunyuanVideo-1.5」。
- **闭源对标**：Sora / Runway / Kling 若在 commerce/reports 已有报告，可反向从那些报告的高机会词引流至 HunyuanVideo 对比内容。
- **跨章关联**：ComfyUI 在 market/reports ✅——与 Wan 2.2 共享同一 ComfyUI 部署路径，可合并为「ComfyUI 视频生成模型一站安装」教程覆盖多个词。
- **Keyword 簇建议**（给 seo-content 层）：`sora alternative + open source sora + local ai video generator` 可聚合为「Sora 停服后的本地视频 AI 替代方案」对比簇；`hunyuan video comfyui + hunyuan video gguf + hunyuan video local` 可聚合为「在 Olares 上本地运行 HunyuanVideo-1.5」部署教程簇；`wan vs hunyuan + open source video generation` 可聚合跨报告横评簇。

---

*数据来源：SEMrush US（phrase_these × 4 批次、phrase_related × 1 批次、phrase_questions、phrase_fullsearch）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
