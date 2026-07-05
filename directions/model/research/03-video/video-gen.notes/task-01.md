---
task_id: 01
role: 视频生成研究专员
status: complete
sources_found: 13
---

## Sources

[1] Alibaba Cloud — Alibaba Releases Wan2.2 to Uplift Cinematic Video Production | https://www.alibabacloud.com/press-room/alibaba-releases-wan2-2-to-uplift-cinematic | Source-Type: official (厂商新闻稿) | As Of: 2025-07 | Authority: 9/10
[2] Wan-AI (Alibaba) — Wan2.2-T2V-A14B Model Card | https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B | Source-Type: official (模型卡) | As Of: 2025-07 | Authority: 10/10
[3] Wan-AI (Alibaba) — Wan2.2-I2V-A14B README | https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B/raw/41e8532d6927aa0d6f1a082da6bacfbdcc5ce529/README.md | Source-Type: official (模型卡) | As Of: 2025-07 | Authority: 10/10
[4] ComfyUI — Wan2.2 Video Generation Official Native Workflow | https://docs.comfy.org/tutorials/video/wan/wan2_2 | Source-Type: official-adjacent (集成方文档) | As Of: 2026 | Authority: 8/10
[5] Tencent — HunyuanVideo-1.5 Model Card (HuggingFace) | https://huggingface.co/tencent/HunyuanVideo-1.5 | Source-Type: official (模型卡) | As Of: 2025-11 | Authority: 10/10
[6] Tencent — HunyuanVideo-1.5 GitHub | https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5 | Source-Type: official (代码仓) | As Of: 2026-04 | Authority: 10/10
[7] Tencent — HunyuanVideo-1.5 LICENSE (Tencent Hunyuan Community License) | https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE | Source-Type: official (许可证) | As Of: 2025-11 | Authority: 10/10
[8] Lightricks — LTX-2 GitHub | https://github.com/Lightricks/LTX-2 | Source-Type: official (代码仓) | As Of: 2026 | Authority: 10/10
[9] Lightricks — LTX-2 Model Card (HuggingFace) | https://huggingface.co/Lightricks/LTX-2 | Source-Type: official (模型卡) | As Of: 2026 | Authority: 10/10
[10] Genmo — Mochi 1 Preview Model Card | https://huggingface.co/genmo/mochi-1-preview | Source-Type: official (模型卡) | As Of: 2024-10 | Authority: 10/10
[11] THUDM/Zhipu — CogVideoX GitHub | https://github.com/zai-org/cogvideo | Source-Type: official (代码仓) | As Of: 2024-11 | Authority: 9/10
[12] Skywork — SkyReels-V2-T2V-14B-720P README | https://huggingface.co/Skywork/SkyReels-V2-T2V-14B-720P/blob/main/README.md | Source-Type: official (模型卡) | As Of: 2025 | Authority: 9/10
[13] gptproto — What Is Wan 2.7? (核实 Wan 2.5+ 是否开源) | https://gptproto.com/news/what-is-wan-2-7 | Source-Type: secondary (媒体核查) | As Of: 2026 | Authority: 5/10

## Findings

- Wan 2.2（阿里）2025-07-28 发布，Apache 2.0，是首个用 MoE 架构的开源视频模型；含 T2V-A14B、I2V-A14B、TI2V-5B 三主力型号。[1][2]
- Wan 2.2 TI2V-5B 为 5B 稠密模型，统一 T2V+I2V，用高压缩 3D VAE（4×16×16，整体压缩率 64），单张消费级 GPU 上 <9 分钟出 5 秒 720P/24fps；ComfyUI 原生 offload 下约 8GB 显存可跑，官方建议单卡 ≥24GB。[3][4]
- Wan 2.2 A14B（MoE，27B 总参 / 每步激活 14B）全精度推理需约 80GB 显存；经 GGUF/FP8 量化 + T5 CPU offload 可降到 720P ~12–16GB、480P ~6–8GB 在消费卡运行。[4][2]
- Wan 2.5/2.6/2.7 未开源，仅 API（闭源）；官方 HF/GitHub/ModelScope 上最新开源权重仍是 Wan 2.2 家族——SEO 内容农场常误标 2.7 "Apache 开源"。[13]
- HunyuanVideo-1.5（腾讯）2025-11-20 放出代码与权重，仅 8.3B 参数即达开源 SOTA 视觉质量，统一 T2V+I2V，原生 480p/720p + 内建超分到 1080p。[5][6]
- HunyuanVideo-1.5 官方最低约 14GB 显存（开启 offload），ComfyUI 目标 24GB；480p I2V step-distill 版 8–12 步、RTX 4090 上端到端 ~75 秒（提速 75%）。[5][6]
- HunyuanVideo-1.5 采用 Tencent Hunyuan Community License（非 Apache）：不适用于欧盟/英国/韩国，>1 亿 MAU 需另行授权，禁用输出训练竞品——第三方多篇误标为 Apache 2.0。[7]
- LTX-2（Lightricks，仓库 2026-01-03 建）是首个 DiT 音视频基础模型，单次扩散同步生成音频+视频，最高原生 4K@50fps、20 秒；LTX-2 为 19B，升级版 LTX-2.3 为 22B。[8][9]
- LTX-2 提供 fp8/nvfp4 量化与蒸馏版（8 步、CFG=1）；官方 FP8 checkpoint 让 22B 在 16GB 显存（RTX 3080/4080/4090）可跑，全精度约 32GB。[9]
- LTX-2 许可为 LTX-2 Community License（非 Apache）：年营收 <1000 万美元可免费商用，≥1000 万需付费商用授权——常被误标 Apache 2.0。[9]
- Mochi 1（Genmo，2024-10 preview）10B AsymmDiT，Apache 2.0，纯 T2V，848×480/~5.4s；全精度 42–60GB，bf16 变体 22GB，ComfyUI/量化可降到 12–20GB。[10]
- CogVideoX 1.5-5B（THUDM/智谱）5B，T2V + I2V，最长约 10 秒、1360×768；5B 走 CogVideoX 自定义许可（学术免费、商用需登记、<100 万访问/月），2B 版为 Apache 2.0；VAE tiling/offload 下消费级可跑。[11]
- SkyReels-V2（Skywork）首个用 AutoRegressive Diffusion-Forcing 的开源视频模型，主打"无限长"；含 1.3B-540P（消费级）/14B-540P/720P，覆盖 T2V、I2V、Diffusion Forcing、Camera Director。[12]

## Deep Read Notes

### Source [2][3]: Wan 2.2 Model Cards
- Key data: 三型号=T2V-A14B / I2V-A14B（均 MoE 27B 总/14B 激活，480P&720P）+ TI2V-5B（5B 稠密，高压缩 VAE，720P，统一 T2V/I2V）。许可 Apache 2.0。TI2V-5B 单消费卡 <9min 出 5s 720P。
- Key insight: 一个家族横跨消费级（5B）到企业级（A14B 全精度 80GB），量化后 A14B 也能落到 16GB——Olares 本地部署的"主力全能选手"。
- Useful for: 型号总表主行、"run Wan 2.2 locally / Wan 2.2 image to video" 关键词。

### Source [5][6][7]: HunyuanVideo-1.5
- Key data: 8.3B 统一 T2V+I2V，480p/720p + SR→1080p，24fps，121 帧≈5s；min ~14GB / 建议 24GB；step-distill 480p I2V 8–12 步 75s@4090；许可=Tencent Community（EU/UK/KR 排除，100M MAU 上限）。
- Key insight: 参数最小（8.3B）却号称开源 SOTA，最贴合"单张 24GB 消费卡跑 near-SOTA"叙事；但许可地域限制是 Olares 海外用户需注意的坑。
- Useful for: 消费级层主推、"HunyuanVideo local / run on 24GB" 关键词、许可对比。

### Source [8][9]: LTX-2 / LTX-2.3
- Key data: 19B（2.3=22B）DiT，单次同步音+视频，4K@50fps/20s；fp8→16GB 可跑，全精度 ~32GB；蒸馏版 8 步；许可 LTX-2 Community（$10M ARR 阈值）。
- Key insight: 唯一原生"带音频"的开源视频模型，是对标 Sora（音画同步）最直接的开源替代；但许可非 Apache，需在文中纠偏。
- Useful for: "open source video with audio / Sora alternative open source" 关键词。

### Source [10]: Mochi 1
- Key data: 10B AsymmDiT，Apache 2.0，纯 T2V，848×480/5.4s；42–60GB 全精度，22GB bf16，量化 12–20GB。
- Key insight: 干净的 Apache 2.0（EU 友好），但仅 T2V、分辨率偏低、偏慢，属"补充/许可友好"位而非质量第一梯队。
- Useful for: 许可友好替代、"Mochi 1 local" 长尾。

### Source [11]: CogVideoX 1.5-5B
- Key data: 5B，T2V+I2V，~10s、1360×768；许可 CogVideoX License（商用需登记）；2B 版 Apache 2.0；offload/tiling 消费级可跑。
- Key insight: 较早但对显存最友好、生态成熟（Diffusers 一等公民），适合低配 i2v 入门。
- Useful for: "image to video open source / run CogVideoX on 12GB"。

### Source [12]: SkyReels-V2
- Key data: AutoRegressive Diffusion-Forcing，1.3B/5B/14B，540P/720P，121f；T2V+I2V+Camera Director；基于 Wan 架构。
- Key insight: "无限长/长镜头"差异化 + 1.3B 消费级档，补足 Wan/Hunyuan 的时长短板。
- Useful for: 长视频/长镜头长尾、"SkyReels V2 local"。

## Gaps

- 相反主张候选：多篇高排名 SEO 博客（ltxworkflow / aimagicx / localaimaster）将 LTX-2 与 HunyuanVideo-1.5 标为 "Apache 2.0"，与官方 LICENSE（LTX-2 Community、Tencent Hunyuan Community）直接矛盾——本报告以官方许可证为准。
- 相反主张候选：部分博客称存在开源 "Wan 2.7 (Apache, April 2026)"，官方渠道无权重，实为 API 闭源；本报告只登记 Wan 2.2。[13]
- 各模型"消费级显存"数字多来自量化/offload 实测博客，官方通常只给全精度参考值；报告中区分"官方值"与"社区量化值"。
- 未逐一深挖 SkyReels-V2 / CogVideoX 最新小版本的精确显存曲线（Lightweight 模式，留待深调）。

## END
