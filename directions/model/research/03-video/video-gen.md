# 开源视频生成（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 13 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 92%

## 摘要

截至 2026-07-05，开源视频生成已经出现真正"接近闭源 SOTA、且能在单张消费级 GPU 上本地跑"的机型，这对 Olares（个人云操作系统、本地推理）是高价值内容与部署方向。市场由三股力量领跑：**Wan 2.2**（阿里，Apache 2.0，全能主力，从 5B 消费级到 A14B 企业级）[1][2]、**HunyuanVideo-1.5**（腾讯，8.3B 即达开源 SOTA，24GB 消费卡可跑）[5][6]、**LTX-2 / 2.3**（Lightricks，唯一原生"音画同步"，对标 Sora）[8][9]。补充梯队有 **Mochi 1**（Genmo，干净 Apache 2.0，EU 友好）[10]、**CogVideoX 1.5-5B**（智谱，显存最友好的 i2v 入门）[11]、**SkyReels-V2**（Skywork，主打"无限长/长镜头"）[12]。

一个必须纠偏的事实：多篇高排名 SEO 博客把 LTX-2 与 HunyuanVideo-1.5 标为 "Apache 2.0"，并宣称存在开源 "Wan 2.7"——均与官方许可证/发布渠道矛盾。官方口径是：LTX-2 走 **LTX-2 Community License**（$10M 营收阈值）[9]，HunyuanVideo-1.5 走 **Tencent Hunyuan Community License**（排除 EU/UK/KR）[7]，Wan 2.5/2.6/2.7 均为 **闭源 API**、开源权重止步 Wan 2.2 [13]。本报告一律以官方源为准。

对 Olares 的核心结论：**Wan 2.2 TI2V-5B、HunyuanVideo-1.5、LTX-2.3（FP8）** 三者构成"单卡 12–24GB 本地跑 near-SOTA 视频生成"的黄金组合，也是 SEO 内容与"run X locally"落地页的首选切入点。

## 1. 型号总表（核心交付）

| 模型 | 代表型号/参数量 | 部署层级(显存) | 许可 | 闭源对标 | 候选关键词 |
|------|------|------|------|------|------|
| **Wan 2.2** (阿里) | TI2V-5B（5B 稠密，统一 T2V+I2V）；T2V-A14B / I2V-A14B（MoE 27B 总/14B 激活） | 💻 5B：官方建议 24GB，ComfyUI offload ~8GB，5s 720P <9min[3][4]；🏢 A14B 全精度 ~80GB，量化后 720P ~12–16GB[4] | Apache 2.0[2] | Kling / Sora / Runway | run Wan 2.2 locally；Wan 2.2 image to video；Wan 2.2 5B ComfyUI |
| **HunyuanVideo-1.5** (腾讯) | 8.3B（统一 T2V+I2V，480p/720p + SR→1080p，~5s/121f） | 💻 官方 min ~14GB / 建议 24GB；480p I2V step-distill 8–12 步、~75s@4090[5][6] | Tencent Hunyuan Community（排除 EU/UK/KR，100M MAU 上限）[7] | Sora / Kling | HunyuanVideo local；run HunyuanVideo on 24GB；HunyuanVideo 1.5 i2v |
| **LTX-2 / LTX-2.3** (Lightricks) | LTX-2=19B；LTX-2.3=22B（DiT，音画同步单次扩散，4K@50fps/20s） | 💻 官方 FP8 → 16GB（3080/4080/4090）；🏢 全精度 ~32GB[9] | LTX-2 Community（<$10M ARR 免费商用）[9] | Sora（音画同步）/ Runway | open source video with audio；Sora alternative open source；LTX-2 local |
| **Mochi 1** (Genmo) | 10B（AsymmDiT，纯 T2V，848×480/~5.4s） | 🏢/💻 全精度 42–60GB；bf16 22GB；量化 12–20GB[10] | Apache 2.0[10] | Runway / Sora | Mochi 1 local；Apache 2.0 text to video |
| **CogVideoX 1.5-5B** (智谱/THUDM) | 5B（T2V + I2V，~10s，1360×768） | 💻 offload/tiling ~12–16GB[11] | CogVideoX License（商用需登记；2B 版 Apache 2.0）[11] | Pika / Runway | image to video open source；run CogVideoX on 12GB |
| **SkyReels-V2** (Skywork) | 1.3B-540P / 14B-540P/720P（AR Diffusion-Forcing，T2V+I2V，"无限长"） | 📱 1.3B 消费级；🏢 14B 高显存[12] | 见官方 repo（Wan 架构衍生） | Kling / Runway（长视频） | SkyReels V2 local；open source long video generation |

> 层级图例：💻 消费级（单张 12–24GB，主力）｜🏢 高显存/企业级（40GB+ 或多卡）｜📱 轻量。

## 2. 分层解读（t2v vs i2v；消费级 vs 高显存）

**消费级 × 全能（首推 Olares 主力）——Wan 2.2 TI2V-5B。** 5B 稠密单模型同时覆盖 t2v 与 i2v，用高压缩 3D VAE（4×16×16、整体压缩率 64），单张消费卡 <9 分钟出 5 秒 720P/24fps；ComfyUI 原生 offload 下甚至能挤进 ~8GB 显存[3][4]。Apache 2.0 无地域限制，是"人人可在自己 Olares 上跑"的最佳默认选项。

**消费级 × near-SOTA 质量——HunyuanVideo-1.5。** 仅 8.3B 参数即宣称"开源 SOTA 视觉质量与运动连贯性"，统一 t2v/i2v，原生 480p/720p 再内建超分到 1080p；官方最低 ~14GB、建议 24GB，蒸馏版把 480p i2v 压到 8–12 步、4090 上 ~75 秒[5][6]。唯一要提醒的是许可：**不适用于 EU/UK/韩国**、>1 亿 MAU 需另授权[7]——面向海外用户的落地页要写清这点。

**消费级 × 带音频（差异化）——LTX-2.3。** 它是唯一"单次扩散同步生成音频+视频"的开源模型，最高 4K@50fps、20 秒；官方 FP8 checkpoint 让 22B 模型在 16GB 卡上可跑，蒸馏版 8 步快速出片[8][9]。这直接对标 Sora 的"音画一体"卖点，是极稀缺的内容角度。注意许可是 LTX-2 Community（<$10M 营收免费商用），**非 Apache**[9]。

**高显存/企业级——Wan 2.2 A14B、Mochi 1 全精度、SkyReels-V2 14B。** Wan A14B（MoE 27B 总/14B 激活）全精度需约 80GB，属多卡/企业段，但经 GGUF/FP8 + T5 offload 也能落到 720P ~12–16GB[4]，可作为"进阶质量"内容。Mochi 1 是干净 Apache 2.0、EU 友好，但仅 t2v、分辨率偏低且慢，定位"许可友好补充"[10]。SkyReels-V2 以 AutoRegressive Diffusion-Forcing 主打"无限长/长镜头"，14B 高显存、1.3B 消费级[12]。

**i2v 专项。** i2v（图生视频）是 Olares"把本地相册/素材动起来"的高频用例：主力 = Wan 2.2 I2V-A14B / TI2V-5B、HunyuanVideo-1.5 I2V（step-distill 最快）；显存最友好的入门 = CogVideoX 1.5-5B-I2V[11]。

## 3. 候选 SEO 关键词与内容切入

**型号词（低竞争、易排名，优先）**：`run Wan 2.2 locally`、`Wan 2.2 image to video`、`Wan 2.2 5B ComfyUI`、`HunyuanVideo 1.5 local` / `run HunyuanVideo on 24GB`、`LTX-2 local` / `LTX-2 with audio`、`CogVideoX image to video`、`Mochi 1 local`、`SkyReels V2 local`。这些"型号 + locally/ComfyUI/VRAM"长尾竞争度最低，最契合 Olares 部署叙事。

**能力/对比词（中竞争、高转化）**：`best open source video generation model 2026`、`open source text to video`、`image to video open source local`、`open source video generation with audio`。

**闭源替代词（高意图）**：`open source Sora alternative`（→ LTX-2 音画同步 + Wan/Hunyuan 质量）、`open source Kling alternative`（→ Wan 2.2 / SkyReels 长视频）、`Runway alternative self-hosted`、`Pika alternative open source`（→ CogVideoX）。

**内容切入建议**：① "在自己的 Olares 上本地跑 Wan 2.2（t2v + i2v 全流程）"教程页；② "开源 Sora 替代：LTX-2 本地音画同步视频生成"角度文；③ "12–24GB 显存能跑哪些开源视频模型（2026 对照表）"——直接复用本报告型号总表；④ 许可澄清文（LTX/Hunyuan 非 Apache），抢"licensing 混淆"的信息差流量。

## 关键发现（2-3）

1. **"单卡消费级跑 near-SOTA 视频"已成立**：Wan 2.2 TI2V-5B（~8–24GB）、HunyuanVideo-1.5（~14–24GB）、LTX-2.3 FP8（16GB）三者把门槛压到主流 12–24GB 显卡区间[3][5][9]——这正是 Olares 一体机 / 用户已购设备的甜蜜点，是最强的"本地推理"内容与部署主线。
2. **许可是被行业普遍写错的关键差异**：只有 Wan 2.2 与 Mochi 1 是真·Apache 2.0；LTX-2（Community $10M 阈值）与 HunyuanVideo-1.5（Tencent Community，排除 EU/UK/KR）都不是[7][9][10]。面向海外/商用的落地页必须据实标注，既是合规也是差异化流量。
3. **音画同步是唯一"开源已能对标 Sora"的稀缺角度**：LTX-2 是当前唯一原生一次性生成同步音频+视频的开源模型[8][9]，`open source video with audio` / `Sora alternative` 是低竞争高意图的内容金矿。

## 局限性

- Lightweight 模式：每个型号未做逐版本、逐分辨率的显存/耗时基准实测，消费级显存数字多来自量化/offload 的社区实践（报告已区分"官方值"与"社区量化值"）；投产前应以目标 GPU 实测为准。
- 事实型数字（参数量、显存、时长、许可条款）会随小版本更新变化，引用前请回官网/模型卡复核。
- SkyReels-V2、CogVideoX 的最新小版本与精确显存曲线未深挖，如需重点做这两条线建议升级为标准深调。
- 未覆盖纯特效/风格化的老一代（AnimateDiff、Open-Sora 等）——按选型准则"剔除过期"处理，仅在需要历史对照时再补。

## 参考文献

[1] Alibaba Cloud — Alibaba Releases Wan2.2 | https://www.alibabacloud.com/press-room/alibaba-releases-wan2-2-to-uplift-cinematic
[2] Wan-AI — Wan2.2-T2V-A14B Model Card | https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B
[3] Wan-AI — Wan2.2-I2V-A14B README | https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B
[4] ComfyUI — Wan2.2 Official Native Workflow | https://docs.comfy.org/tutorials/video/wan/wan2_2
[5] Tencent — HunyuanVideo-1.5 Model Card (HF) | https://huggingface.co/tencent/HunyuanVideo-1.5
[6] Tencent — HunyuanVideo-1.5 GitHub | https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
[7] Tencent — HunyuanVideo-1.5 LICENSE | https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE
[8] Lightricks — LTX-2 GitHub | https://github.com/Lightricks/LTX-2
[9] Lightricks — LTX-2 Model Card (HF) | https://huggingface.co/Lightricks/LTX-2
[10] Genmo — Mochi 1 Preview Model Card | https://huggingface.co/genmo/mochi-1-preview
[11] THUDM/Zhipu — CogVideoX GitHub | https://github.com/zai-org/cogvideo
[12] Skywork — SkyReels-V2-T2V-14B-720P README | https://huggingface.co/Skywork/SkyReels-V2-T2V-14B-720P/blob/main/README.md
[13] gptproto — What Is Wan 2.7?（Wan 2.5+ 是否开源核查）| https://gptproto.com/news/what-is-wan-2-7
