---
task_id: 01
role: 3D 生成研究专员
status: complete
sources_found: 22
---

## Sources

[1] microsoft/TRELLIS.2 (GitHub) | https://github.com/microsoft/TRELLIS.2 | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[2] microsoft/TRELLIS.2-4B (Hugging Face 模型卡) | https://huggingface.co/microsoft/TRELLIS.2-4B | Source-Type: official | As Of: 2025-12 | Authority: 10/10
[3] microsoft/TRELLIS (GitHub README) | https://github.com/microsoft/TRELLIS | Source-Type: official | As Of: 2025 | Authority: 10/10
[4] Tencent-Hunyuan/Hunyuan3D-2.1 (GitHub README) | https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1 | Source-Type: official | As Of: 2025-10 | Authority: 10/10
[5] Hunyuan3D 2.1 Community License (GitHub LICENSE) | https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/blob/main/LICENSE | Source-Type: official | As Of: 2025-06 | Authority: 10/10
[6] Hunyuan3D-2.1 Python API / VRAM (DeepWiki) | https://deepwiki.com/Tencent-Hunyuan/Hunyuan3D-2.1/3.1-python-api | Source-Type: third-party-docs | As Of: 2025 | Authority: 6/10
[7] bytedance/Hi3DGen (GitHub) | https://github.com/bytedance/Hi3DGen | Source-Type: official | As Of: 2025 | Authority: 9/10
[8] VAST-AI-Research/TripoSR (GitHub) | https://github.com/vast-ai-research/triposr | Source-Type: official | As Of: 2024 | Authority: 10/10
[9] TripoSR 技术报告 (arXiv 2403.02151) | https://arxiv.org/abs/2403.02151 | Source-Type: official-academic | As Of: 2024-03 | Authority: 9/10
[10] Stability-AI/stable-fast-3d (GitHub) | https://github.com/Stability-AI/stable-fast-3d | Source-Type: official | As Of: 2024 | Authority: 10/10
[11] stabilityai/stable-fast-3d (Hugging Face 模型卡) | https://huggingface.co/stabilityai/stable-fast-3d | Source-Type: official | As Of: 2024-08 | Authority: 10/10
[12] Introducing Stable Fast 3D (Stability AI 官方博客) | https://stability.ai/news-updates/introducing-stable-fast-3d | Source-Type: official | As Of: 2024-08 | Authority: 9/10
[13] stepfun-ai/Step1X-3D (GitHub) | https://github.com/stepfun-ai/Step1X-3D | Source-Type: official | As Of: 2025-05 | Authority: 9/10
[14] Step1X-3D Installation Guide / VRAM (DeepWiki) | https://deepwiki.com/stepfun-ai/Step1X-3D/3-installation-guide | Source-Type: third-party-docs | As Of: 2025 | Authority: 6/10
[15] DreamTechAI/Direct3D-S2 (GitHub) | https://github.com/DreamTechAI/Direct3D-S2 | Source-Type: official | As Of: 2025 | Authority: 9/10
[16] wgsxm/PartCrafter (GitHub) | https://github.com/wgsxm/PartCrafter | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[17] Best Image to 3D Models on HuggingFace (2026) (trellis2.app) | https://trellis2.app/blog/best-image-to-3d-models-huggingface | Source-Type: third-party-blog | As Of: 2026 | Authority: 5/10
[18] Trellis 2 vs Hunyuan 3D (3DAI Studio) | https://www.3daistudio.com/blog/trellis-2-vs-hunyuan-3d-differences-explained | Source-Type: third-party-blog | As Of: 2026 | Authority: 5/10
[19] Hunyuan3D 2.1 Guide (Clore.ai docs) | https://docs.clore.ai/guides/3d-generation/hunyuan3d | Source-Type: third-party-docs | As Of: 2025 | Authority: 6/10
[20] Benchmarking 3D Asset Generation: TripoSR vs SOTA (axiomlogica) | https://axiomlogica.com/ai-ml/benchmarking-triposr-production-3d-generation-pipelines | Source-Type: third-party-blog | As Of: 2025 | Authority: 5/10
[21] When Did TRELLIS 2 Come Out? (trellis2.app) | https://trellis2.app/blog/when-did-trellis-2-come-out | Source-Type: third-party-blog | As Of: 2026 | Authority: 5/10
[22] Best AI 3D Model Generators in 2026 (trellis2.app) | https://trellis2.app/blog/best-ai-3d-model-generator | Source-Type: third-party-blog | As Of: 2026 | Authority: 5/10

## Findings

- TRELLIS.2-4B 是微软 2025-12 发布的图生 3D 新 SOTA：40 亿参数 flow-matching transformer + "field-free" 稀疏体素 O-Voxel VAE，输出带 PBR 材质的 mesh，分辨率 512³–1536³，MIT 许可。[1][2]
- TRELLIS.2 硬件门槛：官方要求 NVIDIA GPU ≥24GB、目前仅 Linux、CUDA 12.4；H100 上 512³≈3s / 1024³≈17s / 1536³≈60s；社区报告 RTX 4070 16GB 用 RAM offload 可在 512³ 出图。[2][17]
- 初代 TRELLIS（微软）用统一 SLAT 结构隐变量 + Rectified Flow Transformer，可解码为辐射场 / 3D Gaussian / mesh；型号有 image-large 1.2B、text-base 342M、text-large 1.1B、text-xlarge 2.0B，MIT 许可，同时支持文生与图生。[3]
- Hunyuan3D 2.1（腾讯，2025-06-13）是首个"生产就绪、全开源含训练代码"的 3D 资产生成系统：两段式 = Shape v2.1（3.3B 图生形状）+ Paint v2.1（2B PBR 纹理），支持文生/图生/多视图。[4][19]
- Hunyuan3D 2.1 显存：形状生成 10GB、纹理生成 21GB、形状+纹理合计 29GB；开 low_vram_mode（CPU offload）约 15GB，社区门槛 16–24GB（RTX 3090/4090）。[4][6][19]
- Hunyuan3D 2.1 用的是 Tencent Hunyuan 3D 2.1 Community License（非标准开源）：<100 万月活可免费商用，超过需邮件申请；不适用于欧盟/英国/韩国。[5]
- Hi3DGen（字节跳动，ICCV 2025，MIT）主打"以法线图为中间表示"的高保真几何生成，架构基于 TRELLIS（trellis-normal 权重），偏几何精度、少纹理。[7]
- TripoSR（VAST AI × Stability，MIT，2024-03）是最轻量的前馈单图重建：权重约 1.2GB、默认 6GB 显存（4GB 可跑，--chunk-size 降显存），A100 上 <0.5s 出 mesh。[8][9][20]
- Stable Fast 3D / SF3D（Stability AI，2024-08）基于 TripoSR，1.01B 参数、约 6–7GB 显存、~0.5s 出带 UV 展开与 PBR 材质的 game-ready mesh；Stability Community License（年营收 <100 万美元可商用）。[10][11][12]
- Step1X-3D（StepFun，2025-05）全开源：几何 1.3B（VAE-DiT，输出 watertight TSDF）+ 纹理 3.5B（SD-XL），50 步约 152s、需 27–29GB 显存，偏高显存高保真。[13][14]
- Direct3D-S2（DreamTech，NeurIPS 2025）用 Spatial Sparse Attention 做 gigascale 生成，可在 1024³ 分辨率训练/推理，1024 设置约 24GB 显存。[15]
- PartCrafter（NeurIPS 2025，MIT）从单图一次性生成多个语义部件（无需预分割），可对部件独立编辑，适合可拆解资产。[16]
- 闭源对标：Meshy（3D 打印友好）、Tripo（一体化/最快 ~10s）、Rodin（专业输出）、Luma、Hitem3D（多视图重建）——开源侧 TRELLIS.2 / Hunyuan3D 被评为最接近这些商业产品的免费替代。[17][18][22]

## Deep Read Notes

### Source [1][2]: microsoft/TRELLIS.2 + TRELLIS.2-4B 模型卡
- Key data: 4B 参数；O-Voxel "field-free" 稀疏体素；输出 mesh+PBR（BaseColor/Metallic/Roughness/Opacity）；分辨率 512³–1536³；H100 512³≈3s、1024³≈17s、1536³≈60s；MIT；GitHub 创建 2025-11-26，星标 ~8.5k；arXiv 2512.14692（2025-12-16）。
- Key insight: 目前公认的开源图生 3D 天花板，且是 MIT，直接可商用；但只做单图输入、无文生，且官方要求 24GB/Linux。
- Useful for: "型号总表"顶格项、消费级 offload 说明、SEO 型号词。

### Source [4][5][6]: Hunyuan3D 2.1（README + LICENSE + DeepWiki）
- Key data: Shape-v2-1 3.3B、Paint-v2-1 2B；VRAM 10/21/29GB，low_vram≈15GB；支持 text+image+multi-view；Community License，<1M MAU 可商用、排除 EU/UK/KR；HuggingFace 3M+ 下载。
- Key insight: 唯一同时覆盖文生+图生+多视图、且带完整训练代码的主流开源系统；但许可有地域与 MAU 限制，非纯开源。
- Useful for: 文生 3D 分层、许可风险提示、闭源替代切入。

### Source [8][9][10][11][12]: TripoSR / SF3D
- Key data: TripoSR 1.2GB 权重、6GB（最低 4GB）显存、<0.5s、MIT；SF3D 1.01B、6–7GB、~0.5s、UV 展开+PBR+delighting、Stability Community License。
- Key insight: 轻量/消费级层的主力，SF3D 是 game-ready 首选但许可有营收上限，TripoSR 是纯 MIT 的入门与快速原型基线。
- Useful for: 📱 轻量层、低竞争"run X locally"关键词。

### Source [13][14][15][16]: Step1X-3D / Direct3D-S2 / PartCrafter
- Key data: Step1X-3D 几何1.3B+纹理3.5B、27–29GB；Direct3D-S2 SSA、1024³、~24GB；PartCrafter 部件级、MIT、NeurIPS 2025。
- Key insight: 2025–2026 新一批开源模型往"高分辨率/部件可控/高保真几何"走，多数落在高显存层，是补 SOTA 的关键增量。
- Useful for: 高显存层补新、结构化/可编辑资产内容切入。

## Gaps

- 相反主张候选：第三方博客（trellis2.app）多为带自身产品导流的内容农场式对比，其"最佳/最快"排名与官方基准口径不完全一致，需以官方模型卡的参数/显存为准。
- Hunyuan3D 更高版本（2.5 / 3.0 / 3.5）在第三方平台（3D AI Studio）被提及为"更快、8K PBR"，但未确认是否有开源可本地跑的权重发布，故本报告仅登记确证开源的 2.1。
- 各模型显存数字来自官方 README 或 DeepWiki，实际峰值随分辨率/octree/batch 变化，消费级"可跑"多依赖 offload/量化（量化版按要求忽略）。

## END
