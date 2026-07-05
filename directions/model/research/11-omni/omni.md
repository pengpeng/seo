# 开源 Omni / 多模态（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 30 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 83% | 轮次: task-01 + task-02（重研·核基座/发布时间、补 2026 新 SOTA）

## 摘要

到 2026 年年中，开源多模态已经分裂成**四条**技术路线，都能在本地运行、且逼近甚至局部超越闭源旗舰。关键是先把"Omni"这个词拆清楚——**真正端到端、能"说话"（语音输出）的 Omni 很少，大多数号称 Omni 的模型其实只是"多模态入 + 文本出"的感知模型或 VLM**：

1. **真端到端 Omni（文/图/音/视入，文本+语音出）**——阿里 **Qwen3-Omni-30B-A3B**（Apache 2.0，2025-09）、蚂蚁 **Ming-flash-omni 2.0**（100B-A6B，MIT，2026-02，含图像生成+语音）、面壁 **MiniCPM-o 4.5**（9B，2026-02，端侧全双工"边看边听边说"）。这是唯一能对标 GPT-4o 语音全能的一档。[1][2][16][27][28]
2. **多模态感知（文/图/音/视入，仅文本出）**——**NVIDIA Nemotron 3 Nano Omni-30B-A3B**（2026，NVIDIA Open Model License）和 **Gemma 4**（2026，Apache 2.0，E2B~31B）。名字带"Omni/audio"但**不会说话**，定位是 agentic 系统里的"感知子代理"。[17][18][19][29][30]
3. **全能视觉语言 VLM（文/图/视入，无音频）**——**Qwen3-VL**（2B~235B）、**InternVL3.5**（1B~241B）、**GLM-4.6V/4.6V-Flash**（106B/9B，MIT）。[9][11][31]
4. **前沿研究级 any-to-any（扩散 / 统一 AR，生态未成熟）**——**Qwen3.5-Omni**（2026-03，Plus/Flash 闭源 API，Light 开源存疑）、**NExT-OMNI**（离散流匹配）、**Dynin-Omni**（8B 掩码扩散）、**AR-Omni**（单解码器 AR）。方向前沿但多为研究原型，权重/工具链未成熟，暂作观察。[4][20][22][26]

对 Olares 的核心结论：**端侧 omni 的最优解是 MiniCPM-o 4.5（9B，<12GB RAM，超越 30B 的 Qwen3-Omni）**；台式级主推 **Qwen3-Omni-30B-A3B**（真语音全能）与 **Nemotron 3 Nano Omni**（NVFP4 可跑 RTX 5090 / DGX Spark / Jetson Thor，本地 agentic 感知）；VLM 主力 Qwen3-VL / InternVL3.5 / GLM-4.6V-Flash。许可上 GLM/Ming（MIT）、Qwen/InternVL/Gemma 4（Apache 2.0）商用最干净，可作主推卖点。

## 1. 型号总表（核心交付，含基座 / 发布时间）

> 分档 = 真 Omni（说话）→ 感知（多模态入/文本出）→ VLM（无音频）→ 研究级 any-to-any。"→" 左为输入模态、右为输出模态。

| 模型 | 基座 / 发布时间 | 代表型号 / 参数量 | 支持模态（入 → 出） | 部署层级 | 许可 | 闭源对标 | 候选关键词（低竞争*） |
|------|---------------|------------------|--------------------|---------|------|---------|----------|
| **① MiniCPM-o 4.5** | Qwen3-8B + SigLip2 + Whisper-medium + CosyVoice2 / **2026-02** | 9B | 文+图+音+视 → **文+语音**（全双工实时） | 📱 端侧（<12GB RAM）/ 💻 | 开源权重（MiniCPM 模型许可，商用读模型卡） | GPT-4o / Gemini 2.5 Flash | `minicpm-o 4.5`*, `minicpm-o gguf`*, `minicpm-o ollama`* |
| **① Qwen3-Omni** | Qwen3（Thinker-Talker MoE）/ **2025-09** | 30B-A3B | 文+图+音+视 → **文+语音** | 💻 台式（量化）/ 🏢 | Apache 2.0 | GPT-4o / Gemini 2.5 Pro | `qwen3-omni`*, `run qwen3-omni locally`*, `qwen3-omni vllm`* |
| **① Ming-flash-omni 2.0** | Ling-2.0 MoE / **2026-02** | 100B-A6B | 图+文+视+音 → **图+文+音**（含图像生成） | 🏢（量化+多卡） | MIT | GPT-4o / Gemini | `ming-flash-omni`*, `ming omni`* |
| **② Nemotron 3 Nano Omni** | Nemotron-3 Nano（Mamba2-Transformer 混合 MoE）+ RADIO/CRADIO 视觉 + Parakeet 音频 / **2026** | 30B-A3B（31B 总 / 3B 激活） | 文+图+视+音 → **仅文本** | 💻（NVFP4：RTX 5090 32G / DGX Spark / Jetson Thor）/ 🏢 | NVIDIA Open Model License（开放权重+数据+配方） | GPT-4o 感知 / Gemini | `nemotron nano omni`*, `nemotron 3 omni`*, `nemotron omni vllm`* |
| **② Gemma 4** | Gemma 4（12B 为 encoder-free 统一架构）/ **2026**（12B 2026-06-03） | E2B/E4B/12B/26B-A4B/31B | 文+图+视（全部）+音（E2B/E4B/12B）→ **仅文本** | 📱（E2B/E4B）/ 💻（12B/26B/31B） | Apache 2.0 | Gemini Nano / GPT-4o 感知 | `gemma 4`*, `gemma 4 12b`*, `gemma 4 audio`* |
| **③ Qwen3-VL** | Qwen3 + SigLIP-2 / **2025-09** | dense 2B/4B/8B/32B + MoE 30B-A3B/235B-A22B | 文+图+视（**无音频**）→ 文 | 📱（2B/4B）/ 💻（8B/32B）/ 🏢（235B） | Apache 2.0 | GPT-4o / Gemini | `qwen3-vl`*, `qwen3-vl 4b`*, `qwen3-vl 8b`* |
| **③ InternVL3.5** | Qwen3 + GPT-OSS + InternViT / **2025-08** | 1B~241B-A28B（dense + MoE） | 文+图+视（无音频）→ 文 | 📱（1B/2B）/ 💻（4B/8B）/ 🏢（241B） | Apache 2.0 | GPT-5 / GPT-4o | `internvl3.5`*, `internvl 8b`* |
| **③ GLM-4.6V / 4.6V-Flash** | GLM / **2025-12** | 106B-A12B + Flash 9B | 文+图+视+PDF（无音频）→ 文；GUI agent | 🏢（106B）/ 💻（9B Flash） | MIT | Gemini 2.5 Flash | `glm-4.6v`*, `glm-4.6v flash`* |
| **④ Qwen3.5-Omni** | Qwen（Thinker-Talker HA-MoE）/ **2026-03** | Plus ~30B-A3B / Flash / Light | 文+图+音+视 → 文+语音；256K | 🏢（Plus/Flash 闭源 API）；Light 开源**存疑** | Plus/Flash 仅 API；Light 权重开源仅第三方主张，官方报告未证实 | Gemini 3.1 Pro | `qwen3.5-omni`, `qwen3.5 omni light` |
| **④ NExT-OMNI** | 离散流匹配（DFM）/ **2025-10** | 研究原型 | 文+图+视+音 any-to-any（理解+生成） | 💻/🏢（研究级） | 开源 code+ckpt | 统一多模态研究基线 | `next-omni`, `discrete flow matching omni` |
| **④ Dynin-Omni** | MMaDA-8B-MixCoT（掩码扩散）/ **2026-03** | 8B | 文+图+视+语音（理解+生成）| 💻（研究级） | 开源 | 首个 8B 掩码扩散 omni | `dynin-omni`, `masked diffusion omni` |
| **④ AR-Omni** | 单 Transformer 解码器（含 Chameleon 组件）/ **2026-01** | ~7B（~12GB） | 文+图+语音生成（any-to-any，实时 TTS）| 💻（研究级） | MIT（+ Chameleon 研究许可） | GPT-4o（纯 AR 路线）| `ar-omni`, `autoregressive any-to-any` |

\* 型号词/组合词竞争度普遍低（新模型，本报告未跑 Semrush，标记为"待验证低竞争"候选，取词逻辑见第 3 节）。

**本轮相对上版的变动**：新增 ② 档 **Nemotron 3 Nano Omni** 与 ④ 档三个研究级 any-to-any（NExT-OMNI / Dynin-Omni / AR-Omni）；**Gemma 3 → Gemma 4**（许可从 Gemma 自定义许可升级为 **Apache 2.0**，且明确为"文本出"感知模型）；**剔除 MiniCPM-o 2.6**（被 4.5 取代）与作为独立行的 **Gemma 3**（旧）；**LLaDA2.0-Uni 不入 omni 主表**（仅图+文、无音/视，属"统一图文生成"，见局限性）。

## 2. 分层解读

### 📱 手机 / 边缘级（最贴合 Olares 端侧叙事）

- **MiniCPM-o 4.5（9B）**——端侧真 omni 最强候选，基座 Qwen3-8B + SigLip2 + Whisper-medium + CosyVoice2，2026-02-03 开源。官方 Omni-Flow 统一流式框架实现"边看边听边说"全双工，可主动提醒；**<12GB RAM** 即可在 MacBook / 消费卡本地实时跑，视觉逼近 Gemini 2.5 Flash，**omni 理解超越 30B 的 Qwen3-Omni-30B-A3B**、语音质量更高，支持零样本音色克隆。llama.cpp / Ollama / vLLM 均已适配。[27][3][8]
- **Gemma 4 E2B / E4B**——Google 端侧路线，Apache 2.0，2 亿次下载生态；原生带**音频输入**（ASR/语音翻译，≤30s）+ 图像 + 视频（≤60s），128K 上下文，可完全离线跑在手机 / 树莓派 / Jetson Orin Nano。**输出仅文本**，属感知而非语音 omni。[29][30]
- **Qwen3-VL 2B/4B、InternVL3.5 1B/2B**——纯视觉语言（无音频），内存小、单卡可跑，适合本地图片问答、OCR、文档理解。[9][11]

### 💻 本地台式级（主力）

- **Qwen3-Omni-30B-A3B**（Apache 2.0，2025-09）——真端到端 omni，36 个音频/音视频基准 32 个开源 SOTA、22 个总体 SOTA，音频可比 Gemini 2.5 Pro、超 GPT-4o-Transcribe，理论首包 234ms。3B 激活 MoE 量化后可落高端消费卡/Olares One。[1][2]
- **NVIDIA Nemotron 3 Nano Omni-30B-A3B**（2026，NEW）——Mamba2-Transformer 混合 MoE（31B/3B 激活）+ RADIO/CRADIO 视觉 + Parakeet 音频，文/图/视/音入、**文本出**。定位 agentic 系统的"感知子代理"，一个模型替掉分裂的视觉+语音+语言栈；视频推理较级联管线约 2× 吞吐 / 2.5× 省算力，256K–300K 上下文。**权重+数据集+训练配方全开放**（NVIDIA Open Model License），NVFP4 量化最低可跑 **RTX 5090 32GB / DGX Spark / Jetson Thor**——本地隐私 agentic 的强新选。[17][18][19]
- **GLM-4.6V-Flash（9B）**（MIT，2025-12-08）——Zhipu 为本地/低延迟出的轻量 VLM，擅长文档 / GUI agent；旗舰 GLM-4.6V（106B）偏云端。原生多模态工具调用，128K。[31][13]
- **Qwen3-VL 8B/32B、InternVL3.5 8B/38B**——VLM 主力尺寸，单卡（16GB+）到多卡覆盖。[9][11]
- **Gemma 4 12B / 26B-A4B / 31B**——12B 为 encoder-free 统一架构（线性投影替代视觉/音频编码器，降延迟），12B 起支持音频入，256K 上下文。[29][30]

### 🏢 大模型（云端 / 强硬件）

- **Ming-flash-omni 2.0（100B-A6B，MIT）**（2026-02-11）——功能最全的开源 omni：图+文+视+音入，**图+文+音出**（含图像生成 + 情感语音合成），号称开源 omni-MLLM 新 SOTA。基座 Ling-2.0。体量大，本地需量化+多卡。[16][28]
- **InternVL3.5-241B-A28B**、**Qwen3-VL-235B-A22B**、**GLM-4.6V 106B**——开源 VLM 天花板，缩小与 GPT-5 / Gemini 3 的差距。[11][9][31]

### 🔬 研究级 any-to-any（观察，暂不主推）

- **Qwen3.5-Omni**（2026-03-30）——Thinker-Talker Hybrid-Attention MoE，256K、10+ 小时音频、400+ 秒 720p 视频，Plus 在关键音频任务超 Gemini-3.1 Pro，含"音视频 Vibe Coding"新能力。但**官方技术报告只列 Plus/Flash 且明确"仅通过 API 访问"**，第三方（awesomeagents/buildfastwithai）称有 Light 开源权重——**未获官方模型卡证实，不宜作"已开源可本地跑"宣传**。[4][5][32][33]
- **NExT-OMNI**（2025-10，arXiv 2510.13721）——首个完全基于离散流匹配（DFM）的开源 omni，文/图/视/音 any-to-any，低延迟、跨模态检索强；已开源 code+ckpt，研究基线。[26]
- **Dynin-Omni**（2026-03，8B）——首个 8B 掩码扩散 omni，基座 MMaDA-8B-MixCoT，共享离散 token 空间做迭代掩码去噪，文/图/视/语音理解+生成。可经 vLLM-Omni 跑，但 GitHub 关注度低、工具链早期。[22][23]
- **AR-Omni**（2026-01，~7B，MIT）——单解码器、单 token 流纯 AR，文/图/语音生成，实时 TTS（RTF 0.88），~12GB 显存。含 Chameleon 研究许可组件，研究原型。[20][21]

## 3. 候选 SEO 关键词与内容切入

> 本报告为 Lightweight，未跑 Semrush；以下为按 model-seo-research 取词逻辑推导的**候选关键词框架**，竞争度需后续用 Semrush 验证。

- **型号 / 版本词**（新模型多为零竞争 GEO 抢发位）：`minicpm-o 4.5`、`qwen3-omni`、`ming-flash-omni`、`nemotron nano omni`、`gemma 4`、`qwen3-vl 4b`、`internvl3.5`、`glm-4.6v flash`、`qwen3.5-omni`。
- **引擎组合词**（Olares 一键部署前哨）：`qwen3-omni vllm`、`minicpm-o ollama`、`nemotron omni vllm`、`qwen3-vl ollama`、`ming-flash-omni vllm`。
- **本地部署 / 硬件词**：`run qwen3-omni locally`、`minicpm-o gguf`、`nemotron omni rtx 5090`、`gemma 4 on device`、`local multimodal model`、`self-hosted omni model`。
- **对比 / 替代词**（闭源攻击面）：`open source GPT-4o alternative`、`GPT-4o voice alternative self-hosted`、`gemini 2.5 flash alternative`、`qwen3-omni vs gpt-4o`、`minicpm-o vs gpt-4o`、`open source multimodal model`。
- **Olares 角度**：端侧 omni（MiniCPM-o 4.5）→"本地实时语音+视觉助手，数据不出本机"；agentic 感知（Nemotron Nano Omni）→"一个开源模型替掉视觉+语音+语言栈，可在自有硬件跑"；Apache/MIT 模型（Qwen/InternVL/GLM/Ming/Gemma 4）→"商用友好、可自托管的 GPT-4o 替代"。

## 关键发现（2-3）

1. **"Omni"是被滥用的营销词，必须区分"会说话"与否**：真正端到端、文本+语音输出的开源 omni 只有 Qwen3-Omni、MiniCPM-o 4.5、Ming-flash-omni 2.0（及研究级 AR-Omni/Dynin-Omni）；而 NVIDIA **Nemotron 3 Nano Omni** 与 **Gemma 4** 虽吃音频、却**只输出文本**，是"感知子代理"而非 GPT-4o 语音替代。内容与关键词须据此分档，不能把感知模型/VLM 当全能语音 omni 宣传。[17][29][1][27]
2. **端侧 9B 已能打赢 30B omni，且许可/生态正在成熟**：MiniCPM-o 4.5（9B，<12GB RAM）在 omni 理解上超越 Qwen3-Omni-30B-A3B、语音质量更高，llama.cpp/Ollama/vLLM 全适配——本地实时多模态助手不再需要大显卡，是 Olares 端侧叙事最强证据。[27][8][3]
3. **2026 新增两条线值得押注**：一是 NVIDIA 亲自下场的开源 **Nemotron 3 Nano Omni**（权重+数据+配方全开、NVFP4 跑 RTX 5090/Jetson Thor，agentic 感知）——这是"NVIDIA 官方背书的本地多模态"稀缺卖点；二是扩散/统一 AR 的 any-to-any 前沿（NExT-OMNI、Dynin-Omni、AR-Omni、LLaDA2.0-Uni）——方向新颖、GEO 抢发窗口大，但生态未成熟，先占词、暂不作主推。[17][19][26][22]

## 局限性 / 相反主张（Gaps）

- **Qwen3.5-Omni 开源可跑性存在相反主张（核心分歧）**：官方技术报告（arXiv 2604.15804）只列 **Plus / Flash** 两个变体、并写明"publicly accessible via API"；第三方站点（awesomeagents、buildfastwithai）却称存在 **Light** 开源权重（Apache 2.0、HF 可自托管，且推测 sub-2B）。有教程演示"本地部署 Qwen3.5-Omni"时实际加载的仍是旧的 `Qwen/Qwen3-Omni-30B-A3B-Instruct`。**以官方模型卡为准；在证实前不宜宣传 Qwen3.5-Omni 已开源可本地跑。**[4][5][32][33]
- **"Omni"命名误导**：Nemotron 3 Nano **Omni** 与 Gemma 4（含 audio）均为**文本输出**，无语音合成；宣传时不可等同 GPT-4o 语音全能。[17][18][29]
- **LLaDA2.0-Uni 不是 omni**：16B dLLM-MoE 扩散模型，仅支持**图像+文本**（图文理解、文生图、图像编辑），无音频/视频，应归"统一图文生成"邻域，本报告未入 omni 主表。[24][25]
- **研究级模型工具链未成熟**：NExT-OMNI / Dynin-Omni / AR-Omni GitHub 关注度低（4~42 stars）、量化与推理生态早期，产品化落地风险高，仅作观察/占词。[21][23]
- **许可需逐条核实**：MiniCPM-o 商用条款、Nemotron/Gemma 各自开放许可细则、Ming（MIT，已确认）——宣传前对照官方模型卡。
- **未跑 Semrush**：关键词为逻辑推导候选，量/KD/CPC 需后续验证。
- **"SOTA"多为厂商自述**，缺统一第三方横向榜单交叉验证；数字型事实随版本更新，引用前以官网/模型卡为准。

## 参考文献

[1] Alibaba/QwenLM — Qwen3-Omni GitHub README — https://github.com/QwenLM/Qwen3-Omni
[2] Qwen Team — Qwen3-Omni Technical Report (arXiv 2509.17765) — https://arxiv.org/html/2509.17765
[3] AI/TLDR — Qwen3-Omni Specs & Benchmarks — https://ai-tldr.dev/models/qwen3-omni/
[4] Qwen Team — Qwen3.5-Omni Technical Report (arXiv 2604.15804) — https://arxiv.org/pdf/2604.15804
[5] The Decoder — Qwen3.5-Omni release coverage — https://the-decoder.com/qwen3-5-omni-learned-to-write-code-from-spoken-instructions-and-video-without-anyone-training-it-to/
[8] OpenBMB — MiniCPM-o 4.5 Technical Report (arXiv 2604.27393) — https://arxiv.org/html/2604.27393
[9] Qwen Team — Qwen3-VL Technical Report (arXiv 2511.21631) — https://arxiv.org/pdf/2511.21631
[11] OpenGVLab — InternVL3.5 blog / GitHub — https://internvl.github.io/blog/2025-08-26-InternVL-3.5/
[13] Zhipu/Z.ai — GLM-V GitHub README — https://github.com/zai-org/GLM-V
[16] Ant Group/inclusionAI — Ming GitHub README (Ming-flash-omni 2.0) — https://github.com/inclusionAI/Ming
[17] NVIDIA — Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 model card (Hugging Face) — https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
[18] NVIDIA — Nemotron 3 Nano Omni Architecture docs — https://docs.nvidia.com/nemotron/nightly/nemotron/omni3/architecture.html
[19] NVIDIA Technical Blog — Nemotron 3 Nano Omni Powers Multimodal Agent Reasoning — https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/
[20] AR-Omni — A Unified Autoregressive Model for Any-to-Any Generation (arXiv 2601.17761) — https://arxiv.org/html/2601.17761
[21] ModalityDance — AR-Omni GitHub — https://github.com/ModalityDance/AR-Omni
[22] Dynin-Omni — Omnimodal Unified Large Diffusion Language Model (arXiv 2604.00007) — https://arxiv.org/html/2604.00007v1
[23] AIDASLab — Dynin-Omni GitHub — https://github.com/AIDASLab/Dynin-Omni
[24] inclusionAI — LLaDA2.0-Uni model card (Hugging Face) — https://huggingface.co/inclusionAI/LLaDA2.0-Uni
[25] LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation (arXiv 2604.20796) — https://arxiv.org/abs/2604.20796
[26] NExT-OMNI: Any-to-Any Omnimodal Foundation Models with Discrete Flow Matching (arXiv 2510.13721) — https://arxiv.org/html/2510.13721v2
[27] OpenBMB — MiniCPM-o-4_5 model card (Hugging Face) — https://huggingface.co/openbmb/MiniCPM-o-4_5
[28] Ant Group/inclusionAI — Ming-flash-omni-2.0 model card (Hugging Face) — https://huggingface.co/inclusionAI/Ming-flash-omni-2.0
[29] Google — Gemma 4 model card (ai.google.dev) — https://ai.google.dev/gemma/docs/core/model_card_4
[30] Google Blog — Gemma 4: Our most capable open models to date — https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
[31] Z.ai — GLM-4.6V blog (open-source) — https://z.ai/blog/glm-4.6v
[32] Awesome Agents — Qwen3.5-Omni（Light 开源权重主张，与官方冲突）— https://awesomeagents.ai/news/qwen35-omni-multimodal-model/
[33] BuildFastWithAI — Qwen3.5-Omni Review（Light 开源主张）— https://www.buildfastwithai.com/blogs/qwen3-5-omni-multimodal-ai-review
