---
task_id: 02
role: Omni 多模态研究专员（重研·核基座/发布时间、补 2026 新 SOTA）
status: complete
sources_found: 17
as_of: 2026-07-05
---

## Sources
[17] NVIDIA — Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 model card (HF) | https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 | Source-Type: official | As Of: 2026 | Authority: 10/10
[18] NVIDIA — Nemotron 3 Nano Omni Architecture docs | https://docs.nvidia.com/nemotron/nightly/nemotron/omni3/architecture.html | Source-Type: official docs | As Of: 2026 | Authority: 9/10
[19] NVIDIA Technical Blog — Nemotron 3 Nano Omni Powers Multimodal Agent Reasoning | https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[20] AR-Omni Technical Report (arXiv 2601.17761) | https://arxiv.org/html/2601.17761 | Source-Type: official/academic | As Of: 2026-01 | Authority: 8/10
[21] ModalityDance — AR-Omni GitHub | https://github.com/ModalityDance/AR-Omni | Source-Type: official | As Of: 2026-05 | Authority: 8/10
[22] Dynin-Omni Technical Report (arXiv 2604.00007v1) | https://arxiv.org/html/2604.00007v1 | Source-Type: official/academic | As Of: 2026-03 | Authority: 8/10
[23] AIDASLab — Dynin-Omni GitHub | https://github.com/AIDASLab/Dynin-Omni | Source-Type: official | As Of: 2026-03 | Authority: 7/10
[24] inclusionAI — LLaDA2.0-Uni model card (HF) | https://huggingface.co/inclusionAI/LLaDA2.0-Uni | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[25] LLaDA2.0-Uni Technical Report (arXiv 2604.20796) | https://arxiv.org/abs/2604.20796 | Source-Type: official/academic | As Of: 2026-04 | Authority: 9/10
[26] NExT-OMNI Technical Report (arXiv 2510.13721v2) | https://arxiv.org/html/2510.13721v2 | Source-Type: official/academic | As Of: 2025-10 | Authority: 8/10
[27] OpenBMB — MiniCPM-o-4_5 model card (HF) | https://huggingface.co/openbmb/MiniCPM-o-4_5 | Source-Type: official | As Of: 2026-02 | Authority: 9/10
[28] Ant Group/inclusionAI — Ming-flash-omni-2.0 model card (HF) | https://huggingface.co/inclusionAI/Ming-flash-omni-2.0 | Source-Type: official | As Of: 2026-02 | Authority: 9/10
[29] Google — Gemma 4 model card (ai.google.dev) | https://ai.google.dev/gemma/docs/core/model_card_4 | Source-Type: official | As Of: 2026 | Authority: 10/10
[30] Google Blog — Gemma 4: Our most capable open models to date | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[31] Z.ai — GLM-4.6V blog (open-source, 2025-12-08) | https://z.ai/blog/glm-4.6v | Source-Type: official | As Of: 2025-12 | Authority: 9/10
[32] Awesome Agents — Qwen3.5-Omni (Light 开源主张，与官方冲突) | https://awesomeagents.ai/news/qwen35-omni-multimodal-model/ | Source-Type: aggregator | As Of: 2026 | Authority: 4/10
[33] BuildFastWithAI — Qwen3.5-Omni Review (Light 开源主张) | https://www.buildfastwithai.com/blogs/qwen3-5-omni-multimodal-ai-review | Source-Type: third-party | As Of: 2026 | Authority: 4/10

## Findings
### 逐个核实"基座 + 发布时间"（旧候选）
- **Qwen3-Omni**：基座 Qwen3（Thinker-Talker MoE），30B-A3B，2025-09（arXiv 2509.17765），Apache 2.0。真端到端 omni（文+图+音+视→文+语音）。偏"近期"，非偏旧，保留主推。[1][2]
- **MiniCPM-o 4.5**：基座 **Qwen3-8B** + SigLip2 + Whisper-medium + CosyVoice2，9B，**2026-02-03 开源**（技术报告 2026-05-07，arXiv 2604.27393）。<12GB RAM 全双工"边看边听边说"，omni 理解超 Qwen3-Omni-30B-A3B。最新，端侧最强，升主推。[27][8]
- **Ming-flash-omni 2.0**：基座 **Ling-2.0** MoE 100B-A6B，**2026-02-11**，**MIT 许可**（GitHub 仓库 license=MIT，此前"许可待查"字段已确认）。图+文+视+音→图+文+音，含图像生成。功能最全开源 omni。[16][28]
- **Qwen3-VL**：基座 Qwen3 + SigLIP-2，2B~235B-A22B，2025-09（235B 2025-09-23），Apache 2.0，VLM 无音频。保留。[9]
- **InternVL3.5**：基座 Qwen3 + GPT-OSS + InternViT，1B~241B-A28B，**2025-08-26**，Apache 2.0，VLM 无音频。保留。[11]
- **GLM-4.5V/4.6V**：GLM-4.5V 2025-08；**GLM-4.6V 与 GLM-4.6V-Flash 9B 于 2025-12-08 开源**（MIT）。VLM 无音频。上版靠 ai-tldr 第三方，现有 z.ai 官方源。[31][13]
- **Gemma 4**（原 Gemma 3）：2026 发布（12B 2026-06-03），**许可升级为 Apache 2.0**（原 Gemma 自定义许可）。E2B/E4B/12B/26B-A4B/31B；全部支持文+图+视，E2B/E4B/12B 支持**音频输入**（ASR，≤30s），**输出仅文本**。12B 为 encoder-free 统一架构。属"感知（多模态入/文本出）"非语音 omni。[29][30]

### 新候选核实
- **NVIDIA Nemotron 3 Nano Omni-30B-A3B**（NEW，2026）：基座 Nemotron-3 Nano（Mamba2-Transformer 混合 MoE，31B 总/3B 激活）+ RADIO v2.5-H/CRADIO v4-H 视觉 + Parakeet 音频。文/图/视/音入，**仅文本出**（无语音）。256K–300K 上下文，定位 agentic 系统"感知子代理"。**权重+数据集+训练配方全开放**（NVIDIA Open Model License），有 BF16/FP8/NVFP4；NVFP4 最低跑 RTX 5090 32GB / DGX Spark / Jetson Thor；vLLM 可服务。强新增，Olares 本地 agentic 高相关。[17][18][19]
- **AR-Omni**（ModalityDance，arXiv 2601.17761，2026-01）：~7B，MIT（+Chameleon 研究许可），单 Transformer 解码器/单 token 流纯 AR，文+图+语音生成（any-to-any），实时 TTS RTF 0.88，~12GB。研究原型（GitHub 42 stars）。[20][21]
- **Dynin-Omni**（AIDAS Lab/SNU，arXiv 2604.00007，2026-03-09）：8B，首个掩码扩散 omni，基座 MMaDA-8B-MixCoT，共享离散 token 空间迭代掩码去噪，文/图/视/语音理解+生成。vLLM-Omni 可跑，GitHub 4 stars，早期。[22][23]
- **LLaDA2.0-Uni**（inclusionAI，arXiv 2604.20796，2026-04-23；FP8 2026-05-06）：16B dLLM-MoE 扩散，基座 LLaDA2.0 + SigLIP-VQ tokenizer + 扩散解码器。**仅图像+文本**（图文理解、文生图、图像编辑），**无音频/视频**→ **不算 omni**，归"统一图文生成"邻域，不入 omni 主表。BF16 ~63GB / FP8 ~33GB。[24][25]
- **NExT-OMNI**（ritzz-ai，arXiv 2510.13721，2025-10-15）：首个完全基于离散流匹配（DFM）的开源 omni，文/图/视/音 any-to-any 理解+生成，低延迟、跨模态检索强。开源 code+ckpt（github.com/ritzz-ai/Next-OMNI）。研究基线。[26]
- **Qwen3.5-Omni**（2026-03-30）：Thinker-Talker Hybrid-Attention MoE，256K、10+ 小时音频、400+ 秒 720p 视频，Plus 超 Gemini-3.1 Pro，"音视频 Vibe Coding"。**官方技术报告（arXiv 2604.15804）仅列 Plus/Flash 且"publicly accessible via API"**。开源可跑性存疑（见 Gaps）。[4]

## Deep Read Notes
### Source [17][18][19]: NVIDIA Nemotron 3 Nano Omni
Key data: 30B-A3B（31B/3B）Mamba2-Transformer 混合 MoE；CRADIO/RADIO 视觉 + Parakeet 音频；in=文/图/视/音，out=文本；256K–300K；~2× 吞吐/2.5× 省算力（vs 级联）；NVFP4 跑 RTX 5090 32GB/DGX Spark/Jetson Thor；NVIDIA Open Model License 全开放权重+数据+配方。
Key insight: NVIDIA 官方背书的开源本地多模态"感知子代理"——不是会说话的 omni，是喂给外层 agent 的统一感知层；对 Olares"本地 agentic、数据不出机"叙事极契合。
Useful for: ② 感知档主推行、`nemotron nano omni` 抢发词、Olares One/Jetson 硬件绑定叙事。

### Source [27][8]: MiniCPM-o 4.5
Key data: 9B，基座 Qwen3-8B + SigLip2 + Whisper-medium + CosyVoice2；2026-02-03 开源；Omni-Flow 全双工；<12GB RAM；omni 理解 > Qwen3-Omni-30B-A3B；语音质量更高 + 零样本音色克隆；llama.cpp/Ollama/vLLM 适配。
Key insight: 端侧真 omni 天花板，9B 打赢 30B——Olares 端侧叙事最硬证据。
Useful for: 📱端侧主推、`minicpm-o 4.5`/`minicpm-o gguf` 词。

### Source [28][16]: Ming-flash-omni 2.0
Key data: Ling-2.0 MoE 100B-A6B；2026-02-11；MIT；in=图/文/视/音，out=图/文/音（含图像生成+情感语音）；开源 omni-MLLM SOTA 自述。
Key insight: 功能最全开源 omni（唯一同时"看+听+说+画"），但 100B 属大模型档，本地需量化+多卡。
Useful for: 🏢 SOTA 标杆、`open source GPT-4o alternative` 对标、MIT 商用卖点。

### Source [4][32][33]: Qwen3.5-Omni 开源分歧
Key data: 官方 arXiv 2604.15804 只列 Plus/Flash、"publicly accessible via API"；第三方称 Light 有开源权重（Apache 2.0、sub-2B）。apidog 本地部署示例实际加载旧的 Qwen3-Omni-30B-A3B。
Key insight: Light 开源=未证实主张；写报告须标"以官方模型卡为准"。
Useful for: Gaps 相反主张、避免误宣传。

## Gaps
- **Qwen3.5-Omni Light 开源可跑性=相反主张**：官方[4] 仅 Plus/Flash + API；第三方[32][33] 称 Light 开源权重。未证实，以官方模型卡为准。（本轮记录的关键 contrary claim）
- **命名误导**：Nemotron 3 Nano "Omni"[17]、Gemma 4 含 audio[29] 均只输出文本，非语音 omni；不可等同 GPT-4o 语音全能。
- **LLaDA2.0-Uni 非 omni**：仅图+文，无音/视[24][25]，剔出 omni 主表。
- **研究级模型生态早期**：AR-Omni/Dynin-Omni/NExT-OMNI GitHub 关注度低、量化/推理链未成熟[21][23]，产品化风险高。
- **许可细则**：MiniCPM-o 商用条款、NVIDIA/Gemma 开放许可条款需对照官方模型卡（Ming=MIT 已确认[28]）。

## END
