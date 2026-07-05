---
task_id: 01
role: 图像生成研究专员
status: complete
sources_found: 14
---

## Sources

[1] Black Forest Labs — flux2 (GitHub README) | https://github.com/black-forest-labs/flux2 | Source-Type: official | As Of: 2026-01 | Authority: 10/10
[2] Black Forest Labs — FLUX.2: Frontier Visual Intelligence (blog) | https://bfl.ai/blog/flux-2 | Source-Type: official | As Of: 2025-11 | Authority: 10/10
[3] QwenLM — Qwen-Image (GitHub README) | https://github.com/QwenLM/Qwen-Image | Source-Type: official | As Of: 2026-02 | Authority: 10/10
[4] Qwen — Qwen-Image-Edit-2511 (Hugging Face model card) | https://huggingface.co/Qwen/Qwen-Image-Edit-2511 | Source-Type: official | As Of: 2025-12 | Authority: 10/10
[5] HiDream-ai — HiDream-O1-Image (GitHub README) | https://github.com/HiDream-ai/HiDream-O1-Image | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[6] ComfyUI — HiDream-O1-Image Native Workflow (docs) | https://docs.comfy.org/tutorials/image/hidream/hidream-o1 | Source-Type: official | As Of: 2026-05 | Authority: 9/10
[7] Tongyi-MAI — Z-Image (GitHub README) | https://github.com/Tongyi-MAI/Z-Image | Source-Type: official | As Of: 2026-02 | Authority: 10/10
[8] Tongyi-MAI — Z-Image-Turbo (Hugging Face model card) | https://huggingface.co/Tongyi-MAI/Z-Image-Turbo | Source-Type: official | As Of: 2025-11 | Authority: 10/10
[9] NVIDIA — FLUX.2 Image Generation Models Now Released (blog) | https://blogs.nvidia.com/blog/rtx-ai-garage-flux-2-comfyui/ | Source-Type: official-vendor | As Of: 2025-11 | Authority: 9/10
[10] NVIDIA NIM — qwen-image-edit (model page) | https://build.nvidia.com/qwen/qwen-image-edit | Source-Type: official-vendor | As Of: 2026-04 | Authority: 8/10
[11] Thunder Compute — Flux ComfyUI: The Complete Guide (July 2026) | https://www.thundercompute.com/blog/flux-comfyui-ai-image-generation | Source-Type: secondary | As Of: 2026-07 | Authority: 7/10
[12] Local AI Master — FLUX VRAM Requirements by GPU (2026) | https://localaimaster.com/blog/flux-vram-requirements-by-gpu | Source-Type: secondary | As Of: 2026 | Authority: 6/10
[13] The AI Bench — Local AI for Image generation | https://theaibench.ai/use-cases/image/ | Source-Type: secondary | As Of: 2026-05 | Authority: 6/10
[14] aifoss.dev — Flux vs SDXL vs SD 3.5 2026 | https://aifoss.dev/blog/flux-vs-sdxl-vs-sd35-2026/ | Source-Type: secondary | As Of: 2026 | Authority: 6/10

## Findings

- FLUX.2 [dev] 是 32B 开放权重文生图+图像编辑统一模型（2025-11-25 发布），BFL 称其为"当前最强开放权重图像模型"，但满精度需 >80GB 显存，FP8 ~32GB、Q4 GGUF ~19GB（24GB 卡需卸载文本编码器）→ 高显存/企业级；许可为非商用。[1][2][9][12]
- FLUX.2 [klein] 家族（2026-01-15 发布）是消费级答案：4B 蒸馏版 ~8–13GB 显存、~4 步亚秒出图、Apache 2.0（可商用）；9B 版 ~29GB（量化 ~16GB）、非商用许可。[1][11][12]
- Qwen-Image 是 20B MMDiT 基础模型（Apache 2.0），以复杂文本渲染（尤其中文）和图像编辑见长；2025-12-31 的 Qwen-Image-2512 在 AI Arena 万轮盲测中为最强开源模型；2026-02-10 又发布 Qwen-Image-2.0（更强排版/2K 分辨率/更小更快、统一生成与编辑）。[3]
- Qwen-Image-Edit-2511（2025-12-23 权重发布，Apache 2.0，20B）主打图像编辑：多图输入、角色一致性、几何推理、原生 2560×2560；社区 FP8 可低至 6GB 显存运行；被广泛视作 Nano Banana Pro 的开源平替。[3][4][10]
- HiDream-O1-Image（8B，MIT，2026-05-08 开源）采用像素级统一 Transformer（无外部 VAE/文本编码器），支持文生图+指令编辑+主体个性化，最高 2048×2048；FP8 ~10GB（12GB 卡可跑）、BF16 17–20GB；在多个基准超过 FLUX.2 dev(32B) 与 Qwen-Image(20B)，参数少 3–7 倍。[5][6][13]
- HiDream-O1-Image 被 The AI Bench 列为 Artificial Analysis T2I Arena 上 #1 开放权重模型（Elo 1184，2026-05 榜）；另有 HiDream-O1-Image-Pro（200B+）为闭源/API 级旗舰对照项。[13][5]
- Z-Image-Turbo（6B，Apache 2.0，2025-11-26/27 发布）是蒸馏版，仅 8 NFE、无 CFG、H800 上亚秒出图，16GB 消费卡舒适运行；FP8 ~8GB、GGUF 6GB；擅长写实与中英双语文本。[7][8][12]
- Z-Image 家族还含 Z-Image（base，2026-01-27 发布，50 步）、Z-Image-Omni-Base 与 Z-Image-Edit（待发布，编辑向）。[7][8]
- 许可格局碎片化：FLUX.2 dev 非商用、FLUX.2 klein 4B Apache 2.0 但 9B 非商用；HiDream-O1 为 MIT（可商用）；Qwen-Image 全系 Apache 2.0；SD 3.5 为 Stability Community License；SANA 为 NVIDIA NSCL v2 非商用。[13]
- SDXL(1.0, 3.5B, 2023)在 2026 仍是 8GB 显存段落地首选，凭借 CivitAI 上数千 LoRA/ControlNet 生态；纯出图质量已落后 FLUX/新模型，但特定域微调 checkpoint 仍能局部胜出。[14]
- SD 3.5（Large 8B / Medium 2.5B，2024-10，Stability Community License 商用年营收 ≤$1M 可用）介于 SDXL 与 FLUX 之间：文本渲染优于 SDXL，但生态薄、社区牵引力弱，多被建议在 SDXL 或 FLUX 之间二选一时跳过。[14]
- 本地运行主流栈为 ComfyUI（原生支持 HiDream-O1、FLUX、Qwen 系列）；FP8/GGUF 量化是把大模型塞进消费卡的关键手段，NVIDIA 与 BFL/ComfyUI 合作把 FLUX.2 显存需求降 ~40%。[1][6][9]

## Deep Read Notes

### Source [1][2]: Black Forest Labs FLUX.2 (GitHub + blog)
Key data: FLUX.2 [dev] 32B（2025-11-25）；FLUX.2 [klein] 4B/9B（2026-01-15），4B ~8GB、Apache 2.0，9B 非商用。统一 T2I + 单/多参考图编辑于一个 checkpoint。
Key insight: BFL 把产品线做成谱系（pro/flex 闭源 API → dev/klein 开放权重），klein 4B 是"多数人第一个能真正本地跑的 FLUX.2 权重"。
Useful for: 型号总表主推行、"run FLUX.2 locally"关键词、闭源对标（自家 pro API + Midjourney）。

### Source [3][4]: Qwen-Image / Qwen-Image-Edit-2511
Key data: Qwen-Image 20B Apache 2.0；Qwen-Image-2512（2025-12-31）为最新可跑 T2I；Qwen-Image-2.0（2026-02-10）更小更快、2K；Edit-2511 20B、2560×2560、多图、社区 FP8 6GB。DiffSynth 可 4GB 显存逐层卸载。
Key insight: Qwen 系是"文本渲染 + 编辑"双强，且全系 Apache 2.0，是商用最干净的高质量选择；Edit-2511 直接对标 Nano Banana Pro。
Useful for: 图像编辑分层、多语言/文本渲染切入、"Qwen Image Edit locally"关键词。

### Source [5][6][13]: HiDream-O1-Image
Key data: 8B、MIT、像素级 UiT、2048×2048、文生图+编辑+个性化+分镜；Full 50 步 / Dev 28 步；FP8 ~10GB、BF16 17–20GB。基准上以少 3–7 倍参数超 FLUX.2 dev 与 Qwen-Image。The AI Bench 记为 AA T2I Arena #1 开放权重（Elo 1184）。
Key insight: 效率型 SOTA——8B 达到甚至超过 20–32B 模型，MIT 许可利于商用，是"消费级顶配"的旗手。
Useful for: "best open source image generator 2026" 抢答、消费级主推、MIT 商用卖点。

### Source [7][8][12]: Z-Image / Z-Image-Turbo
Key data: 6B、Apache 2.0；Turbo 蒸馏版 8 NFE、无 CFG、亚秒、16GB 舒适 / FP8 8GB / GGUF 6GB；中英双语文本、写实强。家族含 base、Omni-Base、Edit（待发）。
Key insight: 速度/门槛型日常主力，Apache 2.0 可商用，是低显存段（6–8GB）的强候选。
Useful for: 边缘/轻量层、"fast local image generation"、"Z-Image Turbo ComfyUI" 关键词。

### Source [9][11][12]: FLUX.2 VRAM / 部署
Key data: FLUX.2 dev 满精度需 90GB 载入、lowVRAM 仍需 64GB；NVIDIA+ComfyUI 的 FP8 降 ~40% 显存、提速 ~40%；klein 4B 8–13GB、9B 29GB(量化16GB)。
Key insight: 量化 + 权重流式卸载是消费卡跑大模型的必需路径。
Useful for: 部署层级判定、VRAM 表、"FLUX.2 VRAM requirements" 关键词。

### Source [14]: Flux vs SDXL vs SD 3.5 (2026)
Key data: SDXL 3.5B、8GB、生态最深；SD 3.5 Large 8.1B / Medium 2.5B、Community License；SD 3.5 生态薄，建议多数场景二选一时跳过。
Key insight: 传统 SD 系已从"主力"退为"生态/低显存兜底"；新一代（FLUX.2 klein、Z-Image、HiDream）接棒消费级主推。
Useful for: 剔除过期判断（SDXL 保留为生态位、SD3.5 降级）、"SDXL alternative 2026" 关键词。

## Gaps

- 相反主张候选：BFL 官方[2]称 FLUX.2 dev"以显著优势超越所有开放权重替代"，而 HiDream-ai[5]/The AI Bench[13] 的基准显示 8B HiDream-O1-Image 在多项指标反超 FLUX.2 dev(32B)——榜单口径/时间点不同，需注明基准来源与日期，勿断言唯一 SOTA。
- HiDream-O1-Image-Pro（200B+）疑为闭源/API 旗舰，未确认是否有开放权重；报告中标注为"对照/未开放"。
- 缺独立第三方（非厂商）盲测榜单原始页（如 Artificial Analysis / LMArena 官方）直接引用，当前经 The AI Bench 转述——如需强断言应补一手榜单。
- 具体 SEO 搜索量/竞争度未取 Semrush 数字（Lightweight 未做量化关键词研究），关键词为定性候选，标注"待 Semrush 验证"。

## END
