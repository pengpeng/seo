# 2026 本地开放模型、AI Runtime 与企业加速资源：Slide 21 研究报告

> 研究日期: 2026-07-15 | 来源数: 80 | 字数: ~8,000 | 模式: Standard | AS_OF: 2026-07-15 | 官方源占比: 93.8%

## 执行摘要

Slide 21 应讲清一条可验证的本地 AI 栈：上层是**九个核心模型 + 六个补充模型**组成的 3×5 model grid，中层是 Olares Market 中九个承担 inference、model serving 或 generative workflow execution 的 AI runtimes，底层是 2023–2026 Intel AI PC 产品线、当前企业 dGPU 与 Olares allocation modes。这里的“本地”不是“任何下载得到的权重都能塞进 24GB GPU”，也不是“Market 有 chart 就等于当前版本已验证”，而是型号、运行时和硬件边界能够形成可追溯组合。

九个核心模型为 Gemma 4、Qwen3、Ornith 1.0、FLUX.2、Wan2.2、Hunyuan3D 2.1、Qwen3-ASR、ACE-Step 1.5、BGE-M3；新增两行为 Qwen3-TTS、Baidu Unlimited-OCR、Tencent Hy-MT2、Z-Image、Ideogram 4、MiniCPM-o 4.5，补齐 TTS、文档、翻译、设计图像与实时 omni。[45][47][48][50][57][58][59] **Gemma 4 已经由 Google 官方模型卡、产品总览和 release log 核验发布**，不是占位名称。[1][2][3] DeepSeek V4 和 MiniMax M3 也确实已经发布权重并提供本地 serving 路径，但其最小公开变体仍是数百 B 总参数、面向多卡工作站或数据中心的规模，因此因**本地硬件适配**而排除，不应误写为“未发布”“闭源”或“只能 API”。[13][14][15][16]

九项 Market packages 为 llama.cpp、vLLM、SGLang、Ollama、LocalAI、Xinference、KoboldCpp、Speaches 与 ComfyUI。[34][35][36][37][38][39][71][73][79] 前七项以通用模型执行/服务为主，Speaches 补充语音服务，ComfyUI 承担生成式工作流。KoboldCpp 的审计 chart 适用 Olares `>=1.12.3-0,<1.12.6`，Market 收录不应被泛化为所有系统版本兼容。[79][80] Allocation chips 应使用 **Time slicing / Memory slicing / Exclusive** 三种准确名称。硬件栏同时展示 Intel Core Ultra Series 1–3 与当前 Panther Lake SKU，强调平台覆盖但不暗示每个 SKU 已完成 Olares 验证。[60][61][62][63]

最重要的边界有三条：第一，Hunyuan3D 2.1 使用 bespoke community license，不能与 Apache 2.0/MIT 画等号。[9] 第二，Wan2.2 TI2V-5B 的官方实践下限是 **≥24GB VRAM**，24GB 只是边界配置。[7] 第三，显存区间只适合做规划提示；context、resolution、batching、quantization、offload 及并发流程都会改变实际需求。

## 1. 方法论与范围

本研究以 2026-07-15 为信息截止日，综合九个调查任务与定向补充核验：模型目录、模型发布与本地可运行性、企业 dGPU、Olares runtime/allocation code、Intel AI PC 时间线、Intel 展示 taxonomy、Market runtime inventory、九项 shortlist 与反向复核。来源按 URL 或本地官方代码路径去重后统一编号。最终 80 个 Approved 来源包含 75 个 official、1 个 academic、2 个 secondary-industry 和 2 个 journalism；16 个内部清单、旧 SEO 报告、Slide 与图标索引列为 Dropped。来源结构满足 Standard 数量、域名、官方占比、集中度与类型多样性质量门，但仍未包含九项 runtime 的统一 install/model-load/API smoke test。

冲突处理遵循以下顺序：

1. 发布方模型卡、官方仓库和许可证优先于内部模型清单。
2. GPU 厂商 live catalog 的世代分层优先于旧公告；公告用于补日期，不用来覆盖当前目录。
3. Olares 当前代码和 Manifest 用于确认枚举、默认值与 chart coverage；用户文档用于显示文案。
4. 当文档与代码不完全同步时，能力描述标为 **code-level support**，不外推为所有应用、所有后端都具备同等成熟度。

本报告中的 “Open & open-weight models” 是有意采用的宽口径：它覆盖 Apache 2.0/MIT 权重，也覆盖允许下载与本地运行、但附有 bespoke terms 的 source-available/open-weight 模型。“推荐”只表示适合 Slide 21 的本地 AI 展示，不构成许可证法律意见、性能承诺或采购建议。

**置信度: High（事实映射）；Medium（Standard 工作流合规性）**

**依据:** 80 个 Approved 来源已在登记中去重并标注来源类型、时效、权威分与任务；官方占比 93.8%，来源类型多样性质量门通过。

**反方解释:** 官方模型卡能证明发布状态与标称能力，却不能替代跨 runtime、跨 GPU 的独立 benchmark；硬件规划数字仍需按实际 workflow 验证。

## 2. 九个核心与六个补充 Open & open-weight models

### 2.1 文本、Agent 与多模态理解

1. **Gemma 4 · E4B — 多模态理解与推理。** Google release log 记录 Gemma 4 首批型号于 2026-03-31 发布，并在 2026-06-03 增加 12B Unified；官方卡确认 E4B 支持 text/image/audio 输入、reasoning、function calling 与本地 checkpoint，权重为 Apache 2.0。[1][2][3] E4B 官方 Q4 加载内存约 4.5GB、8-bit 约 8.9GB，Slide 可给出“规划 8–12GB VRAM”的保守运行边界，为上下文和 runtime 留余量。[2]

2. **Qwen3 · 4B — 通用文本与推理。** Qwen 官方发布材料确认 Qwen3 family、Apache 2.0 权重、thinking/non-thinking 设计，以及 Ollama、LM Studio、llama.cpp 等本地路径；4B 作为紧凑变体比超大旗舰更符合单机展示。[4] 官方来源未给出统一 VRAM 下限，硬件标注应由目标 runtime、量化和 context 的实测结果决定。

3. **Ornith 1.0 · 9B — Agentic coding 与工具调用。** 发布方模型页提供 MIT 权重、约 19GB 的 BF16 说明，以及官方 GGUF 的 llama.cpp/Ollama 本地路径。[5] 量化运行的实际内存仍取决于 GGUF 档位、context 与 KV cache，官方来源未给出统一的消费级 VRAM 下限。

这三项按角色分开：Qwen3 负责通用文本推理，Ornith 负责 Agentic coding/tool use，Gemma 4 负责多模态理解。它们不是三个同质化“大模型 Logo”，也不需要借超大旗舰制造能力错觉。

### 2.2 图像、视频与 3D 生成

4. **FLUX.2 · klein 4B — 图像生成与编辑。** 发布方模型卡给出 Apache 2.0 权重与约 13GB VRAM 的官方指引，因此 Slide 应按 16GB GPU 规划，而不是把权重参数量直接等同于峰值显存。[6]

5. **Wan2.2 · TI2V-5B — 文/图生视频。** 官方模型卡覆盖 720p text-to-video 与 image-to-video，并明确给出至少 24GB VRAM 的运行方案；该方案本身已经使用 model/T5 offload 与 dtype 转换。[7] 因而本报告将 **≥24GB** 定为实践下限。24GB GPU 是“刚好进入官方路径”的边界，不代表高分辨率、长视频或并发时仍有充足余量。

6. **Hunyuan3D · 2.1 — 图生 3D 与 PBR 纹理。** 官方仓库发布 shape 与 texture pipeline、权重和训练代码；默认显存参考约为 shape 10GB、texture 21GB、两者完整运行 29GB。[8] 它使用腾讯自定义 Hunyuan Community License，包含地域、用途、notice 与规模条件，因此必须明确标注 **bespoke license**，不能写成 Apache 2.0、MIT 或笼统的“完全开源”。[9]

三项生成模型的显存口径不可合并：FLUX.2 的约 13GB、Wan2.2 的 ≥24GB、Hunyuan3D 完整默认流程约 29GB 来自不同 workload。把它们统一写成“8–16GB 可跑”会同时低估视频和完整 3D pipeline。

### 2.3 语音、音乐与 RAG 工具模型

7. **Qwen3-ASR · 0.6B — 语音识别。** 官方模型卡支持 streaming/offline ASR，覆盖 30 种语言和 22 种中文方言，权重为 Apache 2.0。[10] 官方卡未给出固定 VRAM 下限，并明确指出 batching、长音频与 forced aligner 会影响内存，应按目标 backend 实测。

8. **ACE-Step · 1.5 2B DiT — 音乐生成。** 官方安装与模型指南给出本地路径：DiT-only 模式要求至少 4GB VRAM，LLM+DiT 至少 6GB；4B XL DiT 需要至少 12GB 并启用 offload。[11] 为避免混淆，Slide 应明确写 2B DiT，而不是来源中不存在的 “standard” 变体名。

9. **BGE-M3 · 568M — 本地 RAG embedding。** 官方模型卡给出 MIT 许可、1024 维输出、8192 token context，并在同一模型内支持 dense、sparse 与 multi-vector retrieval；可通过 FlagEmbedding、sentence-transformers 或 Transformers 本地运行。[58]

以上九项构成核心跨模态组合。为了提高主画面信息密度，Slide 21 再加入下面六项角色互补、具备官方本地路径的模型。

### 2.4 新增两行：TTS、文档、翻译、轻量生成与 Omni

10. **Qwen3-TTS · 0.6B — TTS 与声音克隆。** 官方模型卡发布 12Hz 0.6B Base checkpoint，许可为 Apache 2.0，并提供本地 Transformers 路径；官方未给固定显存下限，因此 Slide 不显示数字。[45]

11. **Baidu Unlimited-OCR · 3B-A0.5B — OCR 与文档解析。** 百度官方仓库与模型卡提供 MIT 权重、Transformers、vLLM 和 SGLang 本地路径，重点面向一次处理多页长文档；主画面缩写为 `Baidu OCR`。[57]

12. **Tencent Hy-MT2 · 1.8B — 本地翻译。** 官方 1.8B checkpoint 为 Apache 2.0，并提供 GGUF / llama.cpp 路径；1.25-bit 版本官方标注约 440MB storage，但 storage 不能直接等同运行内存。[47]

13. **Z-Image Turbo · 6B — 轻量快速图像生成。** 官方模型卡为 Apache 2.0，采用 8-step 路径，并明确说明可在 16GB VRAM 内运行。[48]

14. **Ideogram 4 · 9.3B — 设计图像与文字渲染。** 官方技术说明确认其为开放权重图像模型，并提供 FP8 与 NF4 checkpoint；NF4 版可在单张 24GB CUDA GPU 上运行。公开权重使用 Ideogram 4 Non-Commercial License，商业部署需匹配相应授权，因此主画面采用中性的 `Models` 标题。[59]

15. **MiniCPM-o 4.5 · 9B — 实时 Omni。** 官方模型卡覆盖图像、音频、语音输入与生成，权重/代码为 Apache 2.0；官方 llama.cpp 路径约需 12GB GPU memory，而完整 PyTorch 路径更高。[50]

这六项用于增加角色覆盖与视觉密度，不改变“下载权重不等于任意硬件均具备实用体验”的总体边界。

**置信度: High（发布、角色与许可）；Medium（粗略硬件区间）**

**依据:** 每个推荐 family 都有发布方控制的模型卡、仓库或官方文档；Gemma 4、FLUX.2、Wan2.2、Hunyuan3D 与 ACE-Step 具备较直接的内存指引。[1][2][3][6][7][8][11]

**反方解释:** 参数量、权重文件大小与推理峰值显存并非同一指标；未提供直接显存数字的模型，其区间是保守工程估算，量化、context 和后端变化可能使结果明显偏移。

## 3. 已发布但排除：DeepSeek V4 与 MiniMax M3

**DeepSeek V4 已发布但排除。** 官方 V4-Flash 模型卡给出 284B total / 13B active；V4-Pro 为 1.6T total / 49B active，官方 DSpark 部署示例使用 4×GB300 节点。[13][14] MoE 的 active parameters 不能替代 resident weights 来判断单卡适配。即便每 token 只激活部分专家，大量权重仍需驻留或通过复杂 offload/分布式 topology 提供。因此，DeepSeek V4 属于“可私有部署的 open-weight 数据中心模型”，不属于保守的单消费级 GPU 示例。

**MiniMax M3 已发布但排除。** 官方模型卡提供权重及 SGLang、vLLM、Transformers、KTransformers 等 serving 说明；模型约 428B total / 23B active，拥有 1M context，并采用 MiniMax Community License。[15][16] 它可以在服务器或高端多卡工作站本地部署，但没有可信的紧凑单 GPU 路径，故因 local hardware fit 而排除。

这两项的排除原则只回答 Slide 21 的展示边界，不否定它们的发布状态、开放权重或企业私有部署价值。准确措辞应是：**“released open-weight models, omitted because their smallest variants remain datacenter/workstation scale.”**

**置信度: High**

**依据:** 参数规模、权重状态、许可证与 serving topology 均来自两家发布方的一手模型/部署卡。[13][14][15][16]

**反方解释:** 极端量化、CPU/NVMe offload 或多张大显存工作站卡可以实现“本地运行”；但可启动不等于达到 Slide 所暗示的实用单机交互体验。

## 4. 九个 Olares Market AI runtimes

主画面按 3×3 展示九个有 Olares Market Manifest 的产品，但 `AI runtimes` 是宽口径，包含 inference engine、model server、runner 与 generative workflow engine：

1. **llama.cpp** — portable GGUF engine 与轻量 API server；Engine Base chart 声明 CPU、NVIDIA、GB10，覆盖 amd64/arm64。[34]
2. **vLLM** — 高吞吐 OpenAI-compatible model server；chart 声明 CPU、NVIDIA、GB10，覆盖 amd64/arm64。[35]
3. **SGLang** — 面向低延迟、prefix-heavy 与 agentic serving 的 runtime；chart 声明 CPU、NVIDIA、GB10，覆盖 amd64/arm64。[36]
4. **Ollama** — 本地模型 runner、模型生命周期与 API daemon；虽使用 llama.cpp 等底层，但属于不同产品层。[37][78]
5. **LocalAI** — multi-backend、multi-modal OpenAI-compatible server；当前 Olares chart 仅声明 NVIDIA/amd64，不能继承 upstream 更广的硬件支持。[71][74]
6. **Xinference** — multi-model serving platform；当前 chart 仅声明 NVIDIA/amd64。[39]
7. **KoboldCpp** — 基于 llama.cpp 的单文件 GGUF inference engine/server，提供 Kobold 与 OpenAI-compatible API；审计到的 Olares chart 依赖范围为 `>=1.12.3-0,<1.12.6`。[79][80]
8. **Speaches** — OpenAI-compatible STT/TTS server；v3 chart 声明 CPU、NVIDIA、GB10，覆盖 amd64/arm64。[73][76]
9. **ComfyUI** — image/video/audio/3D generative workflow inference engine；不是通用 LLM server，但能与本页多模态模型形成真实执行路径。[38][77]

这九项不共享一个兼容矩阵。`Olares Market package` 只证明 chart 在 `bad4b06` checkout 中存在；Manifest 可能使用版本上限、旧 engine image 或更窄 accelerator 声明，不等于任意系统版本安装成功或在每种硬件上完成 model-load/API smoke test。主画面只写 `AI runtimes`，不附统一硬件 badge。

OpenVINO 不应成为第十项。EmbeddingGemma Manifest 证明 OpenVINO IR/ONNX 可作为具体应用 backend，但核心 compute mode 列表中不存在名为 `openvino` 的 allocation mode。[40][43] 它应与 CUDA、ROCm 一起出现在靠近硬件的 backend enablement 层。

**置信度: High（chart 存在、类别与声明矩阵）；Medium（目标系统版本端到端可用性）**

**依据:** 九项均直接核对 OlaresManifest，并用 upstream 官方文档与独立 runtime landscape 复核类别。[34][35][36][37][38][39][71][73][74][76][77][78][79][80]

**反方解释:** 若 `AI runtimes` 被严格解释为可互换的通用 LLM inference servers，Speaches 与 ComfyUI 不应并列；但本页覆盖图像、视频、音频和 3D 模型，因此采用“模型执行软件”的宽口径。KoboldCpp 是真实推理引擎，但 chart 的 Olares 版本上限意味着它不能代表当前所有发行版的兼容性。

## 5. 当前企业 dGPU 紧凑清单

### 当前目录 / 已宣布

- **Intel：Arc Pro B70 · B65 · B60 · B50。** Intel 当前 B-Series 页面同时列出四个型号；B70/B65 于 2026-03-25 正式发布。[17][18]
- **NVIDIA 分三层：Consumer `RTX 5090 · RTX 5080 · RTX 4090 · RTX 3090`；Workstation `RTX PRO Blackwell 6000 · 5000`；Data center `B200 · H200`。** GeForce 官方页面确认 5090/5080、4090、3090 分属 Blackwell、Ada、Ampere 消费卡；professional desktop catalog 确认 6000/5000 属于工作站层；DGX B200 与 H200 官方数据中心页面确认后两者属于 data-center 资源层。[21][51][52][53][54][55][56]
- **AMD：Radeon AI PRO R9700 · R9600（announced/cataloged）。** AMD workstation catalog 将 Radeon AI PRO R9000（RDNA 4）与 Radeon PRO W7000（RDNA 3）分层；R9700、R9600 均有官方产品页，但 R9600 页面明确标注 “Not available for purchase”。[24][25][26]

### Older generation

- Intel：Arc Pro A60 · A50。两者官方 ordering 页已标记 retired and discontinued，因此只可作为旧代参照。[19][20]
- NVIDIA：RTX 6000 Ada Generation · RTX 5000 Ada Generation。当前目录仍保留 Ada，但不能与 Blackwell 混写为同一当前世代。[21]
- AMD：Radeon PRO W7900 · W7800。它们仍有工作站价值，但属于 W7000/RDNA 3 旧代层。[24][28]

两个命名 caveat 必须保留。其一，RTX PRO 6000 Blackwell family 包含 Server、Workstation 与 Max-Q Workstation editions；紧凑列表可以使用 family 名，但不能暗示 passive Server Edition 是桌面工作站卡。[23] 其二，R9600 有产品页与专用驱动 release notes，但产品页明确标注尚不可购买；因此只能写 announced/cataloged，不能写 shipping 或 “widely available”。[26][27]

**置信度: High（型号、世代与 R9600 未开售状态）**

**依据:** 型号与世代均来自三家厂商 live catalog、产品页或公告。[17][18][21][22][24][25][26][28]

**反方解释:** “在当前目录”不必然等于所有地区现货，也不表示旧代已经失去采购价值；清单的目标是压缩 Slide 信息，不是完整 SKU 或渠道数据库。

### Intel 2023–2026 AI PC 产品线

面向 Intel pitch，Slide 采用 **series/codename 覆盖**，不再列单独 SKU。Intel 从 2023 年 Core Ultra Series 1 开始，把 CPU、GPU 与 NPU 的平台级 AI 能力作为 AI PC 主线；Series 2 扩展为 Lunar Lake 移动平台以及 Arrow Lake H/HX/U/S 等系列，Series 3 则以 Intel 18A 的 Panther Lake 为当前焦点。[60][64][65][66][67]

建议压缩为三行：

- **Core Ultra Series 1** — Meteor Lake · 2023
- **Core Ultra Series 2** — Lunar Lake + Arrow Lake · 2024–25
- **Core Ultra Series 3** — Panther Lake · 2026。[61]

这比只写 `Core Ultra 9/7` 更稳定，也比罗列所有 200V/200H/200HX/200U/200S SKU 更符合单页 pitch 的认知负荷原则。[69][70] 主画面按 pitch 采用 **SoC · Unified memory** 作为紧凑分类；它表达集成计算和统一资源管理视角，不是跨三代的物理封装断言。Lunar Lake 的 on-package memory 是特殊实现，后续家族不能被一并描述为 Apple 式 unified memory。[66][68]

**置信度: High（系列、代号、日期与 SKU）；Medium（Slide taxonomy）**

**依据:** 产品时间线与型号来自 Intel official naming、launch、press-kit 与 ARK；表达方式由 journalism、technical-jargon 与 assertion-evidence 研究做反向复核。[60][61][62][63][64][65][66][67][68][69][70]

**反方解释:** codename 对硬件团队更有辨识度，SKU 对采购团队更具体；混合写法无法覆盖每个 form factor，但能避免将同一 Series 2 下差异明显的 Lunar Lake 与 Arrow Lake 混成单一架构。此处表示 Olares 面向 Intel 集成计算平台的产品叙事，不是逐 SKU 兼容认证。

## 6. Allocation mode chips 与切换生命周期

Slide 应使用以下三个 chips：

- **Time slicing** — `NVIDIA dGPU only`
- **Memory slicing** — `NVIDIA dGPU · GB10 · Intel/AMD iGPU/APU · Moore SoC`
- **Exclusive** — `All accelerator modes`
  - muted sub-chip：`Apple M · Intel/AMD dGPU: exclusive only`

Olares 用户文档使用 sentence-case 的 **Time slicing、Memory slicing、Exclusive**；后端枚举为 `TimeSlice`、`MemorySlice`、`Exclusive`，CLI 当前显示 title-case “Time Slicing / Memory Slicing”。对外 Slide 应跟随文档，对工程注释才使用 enum。[29][30][31][41]

可用模式与默认值来自 app-service：`nvidia` 支持三种模式并默认 TimeSlice；`nvidia-gb10`、`intel`、`amd`、`moore-soc` 支持 MemorySlice/Exclusive 并默认 MemorySlice；CPU fallback 只有 MemorySlice，但 CPU 不是 accelerator chip；`apple-m`、`intel-gpu`、`amd-gpu` 当前只暴露 Exclusive。[31][32][43] 中文 Olares One 指南把 Time slicing 称为默认，但代码表明这个默认只适用于 NVIDIA dGPU，不应泛化到 GB10 或统一内存加速器。[32][42]

模式切换是管理员操作，且会打断已绑定应用。处理流程为：先校验目标模式并预检所有 bound apps 是否可停止；若任一应用阻塞，变更在 mutation 前中止；否则逐应用提交 `StopOp` 并立即删除 allocation/HAMi binding（不等待停止状态完成），再写入新 share-mode annotation；之后需要 resume 和重新绑定。[30][32][33][44] 代码展示了 preflight，但后续逐应用 stop/delete 并非可见的数据库事务，因此不能声称中途基础设施故障具备原子 rollback。

当前英文文档尚未完整覆盖代码中的 AMD/Intel/Moore support types。故这些 chips 表示 **code-level allocation support**，而不是所有 Olares AI 应用在 AMD、Intel、Moore 上都与 NVIDIA 具有相同成熟度。[30][32]

**置信度: High（枚举、默认值与切换流程）；Medium（端到端硬件成熟度）**

**依据:** 文案来自用户文档，能力矩阵与默认值来自当前代码，生命周期来自 API handler 与 device-mode mutation。[29][30][31][32][33][41][42][43][44]

**反方解释:** 代码已暴露某个 mode 不代表驱动、容器镜像和每个应用都完成验证；未来文档同步或 chart 更新可能改变可见范围。

## 7. 重要 Caveats 与核心争议

1. **“Open” 不是单一法律状态。** 十五项中多数使用 Apache 2.0 或 MIT；Hunyuan3D 2.1 与 Ideogram 4 使用带条件的权重许可。Slide 标题采用中性的 **Models**，避免暗示十五项全部满足同一 OSI 定义。[1][4][5][6][7][9][10][57][58][59]
2. **Gemma 4 已核验。** 其发布日期、型号、多模态能力和本地 checkpoint 均有 Google 官方证据；若内部旧资料与之冲突，应更新旧资料，而不是降格 Gemma 4。[1][2][3]
3. **DeepSeek V4 / MiniMax M3 已发布但不推荐进模型网格。** 排除基于 resident weights、服务拓扑和单机硬件 fit，不基于发布状态。[13][14][15][16]
4. **Wan2.2 的实践下限是 ≥24GB。** 8–12GB 说法与官方 TI2V-5B recipe 冲突；24GB 还依赖 offload，并非宽裕余量。[7]
5. **Hunyuan3D 完整流程高于 shape-only。** 约 10GB 只对应 shape；texture 约 21GB，完整默认流程约 29GB。[8]
6. **显存数字不是性能承诺。** context、batch size、resolution、video length、KV cache、并发、quantization、dtype、offload 与 runtime 会改变峰值；CPU fallback 也可能以明显降低速度为代价。
7. **Olares package coverage 不等于 upstream coverage。** 九项产品必须按各自 Manifest 描述，不能共享一个兼容 badge；KoboldCpp chart 还带有明确的 Olares 版本上限。[34][35][36][37][38][39][71][73][79]
8. **Allocation mode 不等于完整应用支持。** AMD/Intel/Moore 的代码级 mode 已存在，但 app chart、驱动和模型算子覆盖仍可能不同。[30][32]
9. **“Current catalog” 不等于现货，也不等于当前世代。** NVIDIA catalog 跨多代；AMD R9600 的官方产品页明确标注尚不可购买。[21][26]
10. **Core Ultra 系列覆盖不等于逐 SKU 认证。** Series 1–3 表示 Intel AI PC 时间线与平台方向，不是已完成 Olares 兼容测试的 SKU 白名单。[60][61]
11. **Slide 分类不等于跨代统一内存实现。** `SoC · Unified memory` 是面向 pitch 的资源分类；Lunar Lake 的 on-package memory 不能泛化到后续 Intel 家族。[66][68]

## 核心争议

- **争议 1：权重可下载是否等于适合本地 AI appliance？** DeepSeek V4 与 MiniMax M3 证明答案是否定的：open-weight/local serving 与单消费级 GPU fit 是两个维度。[13][14][15][16]
- **争议 2：24GB 是否足以覆盖全部推荐模型？** 24GB 可进入 Wan2.2 官方 offload 路径，却不能覆盖 Hunyuan3D 默认完整 shape+texture 的约 29GB；“可运行”还必须绑定具体 workflow。[7][8]
- **争议 3：代码支持是否能直接写成产品支持？** Olares 代码包含 AMD/Intel/Moore modes，但文档和九个 chart 的覆盖并不统一；最准确的说法是代码级 allocation support，按应用核对端到端成熟度。[30][32][34][35][36][37][38][39][71][73][79]
- **争议 4：目录中的型号是否都是 2026 当前代？** NVIDIA live catalog 同时保留 Blackwell 与 Ada/Ampere，Intel A60/A50 甚至已标记 discontinued；必须显式分代。[19][20][21]
- **争议 5：九个 Market logo 是否意味着九个同类、同成熟度 runtime？** 否。Speaches 是语音 server，ComfyUI 是 generative workflow engine，KoboldCpp chart 有系统版本上限；统一点是它们都执行或服务模型，而不是 API、兼容矩阵和成熟度相同。[38][73][76][77][79][80]

**置信度: High（争议所述事实）；Medium（性能与端到端成熟度判断）**

**依据:** 争议均映射到发布方、厂商目录、许可证、Olares 代码或 Manifest；性能与成熟度未经过独立 benchmark。

**反方解释:** 官方代码与目录足以证明能力或型号存在，但不足以证明所有硬件、应用与地区都已达到同一可用状态。

## 关键发现

- Slide 21 可以用十五个角色互补、具备可信本地路径的模型覆盖文本、Agent、多模态理解、设计图像、视频、3D、ASR、TTS、音乐、文档、翻译、RAG 与实时 omni，而无需用超大旗舰填充视觉位。[1][4][5][6][7][8][10][11][45][47][48][50][57][58][59]
- Gemma 4 的真实性与本地适配已经官方核验；DeepSeek V4、MiniMax M3 也已发布，但应因本地硬件 fit 排除。[1][2][3][13][14][15][16]
- 九个 Olares Market AI runtimes 的角色和 Manifest coverage 不同；KoboldCpp 的 chart 适用版本需单独核对，OpenVINO 属于 backend 层而不是第十项产品。[34][35][36][37][38][39][40][43][71][73][79]
- Intel SoC 栏覆盖 Core Ultra Series 1–3，不列单独 SKU；`SoC · Unified memory` 是面向 pitch 的紧凑资源分类，不是所有 Intel AI PC 采用同一物理内存架构的断言。[60][61][66][68]
- 硬件栏应压缩为 Intel B70/B65/B60/B50、AMD R9700/R9600，并把 NVIDIA 明确拆成 Consumer 5090/5080/4090/3090、Workstation RTX PRO Blackwell 6000/5000、Data center B200/H200；R9600 仍需标明尚不可购买。[17][21][24][26][51][52][53][54][55][56]
- Allocation mode 的准确表达是 Time slicing、Memory slicing、Exclusive；切换会向 bound apps 提交停止操作并立即清除绑定，并非等待完成的 drain 或 live migration。[29][30][31][32][33][44]

## 局限性与未来方向

### 本研究局限

本研究不包含跨十五模型、九 runtime 与全部 accelerator 的实机 benchmark，也不核验全球渠道库存。模型显存数字混合了发布方直接数据与保守规划估算，不能比较为统一 benchmark。Olares 证据来自两个本地 checkout 的指定 commit；后续代码、文档或 chart 变化会使矩阵过时。许可证描述仅用于内容准确性，不替代法律审查。

来源结构仍高度偏向 official，这是解决发布状态、型号、许可证和代码行为冲突的合理选择；新增 academic、industry-secondary 与 journalism 来源解决了表达 taxonomy 和行业分类的反向复核，但性能、稳定性和实际吞吐仍没有统一独立 benchmark。

### 未来方向

优先级 P0：在目标 24GB NVIDIA 设备上对 Wan2.2 TI2V-5B、Hunyuan3D shape/texture 与 FLUX.2 klein 做统一冷启动、峰值 VRAM、生成时长测试。

优先级 P1：按九个 Olares chart 建 CPU/NVIDIA/GB10/AMD/Intel 的自动化安装与 smoke-test 矩阵，并在目标 Olares 版本核对 KoboldCpp 的 install、model-load 与 API health，区分 Manifest 声明和端到端通过。

优先级 P1：每次 Slide 发布前重新抓取 Intel、NVIDIA、AMD live catalog，并确认 R9600 的正式 availability。

优先级 P2：对 Hunyuan Community License 的展示文案做法务复核，确保 “open-weight” 与商用限制描述准确。

## 参考文献

[1] Google. “Gemma 4 model card.” Source-Type: official. As Of: 2026-07-15. https://ai.google.dev/gemma/docs/core/model_card_4
[2] Google. “Gemma model overview and inference memory requirements.” Source-Type: official. As Of: 2026-07-15. https://ai.google.dev/gemma/docs/core
[3] Google. “Gemma releases.” Source-Type: official. As Of: 2026-07-15. https://ai.google.dev/gemma/docs/releases
[4] Qwen. “Qwen3: Think Deeper, Act Faster.” Source-Type: official. As Of: 2026-07-15. https://qwenlm.github.io/blog/qwen3/
[5] DeepReinforce. “Ornith-1.0-9B model card and official GGUF.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B
[6] Black Forest Labs. “FLUX.2 [klein] 4B model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
[7] Wan-AI. “Wan2.2-TI2V-5B model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B
[8] Tencent Hunyuan. “Hunyuan3D-2.1 repository.” Source-Type: official. As Of: 2026-07-15. https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1
[9] Tencent Hunyuan. “Hunyuan3D-2.1 license.” Source-Type: official. As Of: 2026-07-15. https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/blob/main/LICENSE
[10] Qwen. “Qwen3-ASR-0.6B model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/Qwen/Qwen3-ASR-0.6B
[11] ACE-Step. “ACE-Step 1.5 installation and model guide.” Source-Type: official. As Of: 2026-07-15. https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md
[12] Qwen. “Qwen3-Embedding-0.6B model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
[13] DeepSeek. “DeepSeek-V4-Flash model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/README.md
[14] DeepSeek. “DeepSeek-V4-Pro-DSpark deployment card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark
[15] MiniMax. “MiniMax-M3 model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/README.md
[16] MiniMax. “MiniMax-M3 license.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE
[17] Intel. “Arc Pro B-Series overview.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html
[18] Intel. “Arc Pro B70/B65 commercial launch.” Source-Type: official. As Of: 2026-03-25. https://newsroom.intel.com/client-computing/intel-core-ultra-series-3-with-vpro-powers-next-gen-pcs-on-18a
[19] Intel. “Arc Pro A60 ordering.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/products/sku/235979/intel-arc-pro-a60-graphics/ordering.html
[20] Intel. “Arc Pro A50 ordering.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/products/sku/230316/intel-arc-pro-a50-graphics/ordering.html
[21] NVIDIA. “RTX PRO desktop GPU catalog.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/
[22] NVIDIA. “RTX PRO Blackwell workstation announcement.” Source-Type: official. As Of: 2025-03-18. https://nvidianews.nvidia.com/news/nvidia-blackwell-rtx-pro-workstations-servers-agentic-ai
[23] NVIDIA. “RTX PRO 6000 Blackwell Series.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/
[24] AMD. “Workstation graphics catalog.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations.html
[25] AMD. “Radeon AI PRO R9700.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html
[26] AMD. “Radeon AI PRO R9600.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9600.html
[27] AMD. “Radeon AI PRO R9600 driver release notes.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-SI-AI-PRO-R9600.html
[28] AMD. “Radeon PRO W7000 workstation catalog.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations/radeon-pro.html
[29] Olares. “Olares One: Manage accelerator resources.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/docs/one/gpu.md
[30] Olares. “Manual: Manage accelerator resources.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/docs/manual/olares/settings/gpu-resource.md
[31] Olares. “Compute support-type wire constants.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/framework/app-service/pkg/compute/types.go
[32] Olares. “Available support types and defaults.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/framework/app-service/pkg/compute/store.go
[33] Olares. “Device mode-switch API and app-stop flow.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/framework/app-service/pkg/apiserver/handler_compute_resources.go
[34] Olares Apps. “llama.cpp Engine Base manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/llamacppllmbasev3/OlaresManifest.yaml
[35] Olares Apps. “vLLM Engine Base manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/vllmllmbasev3/OlaresManifest.yaml
[36] Olares Apps. “SGLang Engine Base manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/sglangllmbasev3/OlaresManifest.yaml
[37] Olares Apps. “Ollama Engine Base manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/ollamallmbasev3/OlaresManifest.yaml
[38] Olares Apps. “ComfyUI shared app manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/comfyuisharev3/OlaresManifest.yaml
[39] Olares Apps. “Xinference shared app manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/xinferencev3/OlaresManifest.yaml
[40] Olares Apps. “EmbeddingGemma OpenVINO/ONNX backend manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/embeddinggemmav3/OlaresManifest.yaml
[41] Olares. “CLI accelerator support-type display labels.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/cli/cmd/ctl/settings/compute/common.go
[42] Olares. “Chinese Olares One GPU mode guide.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/docs/zh/one/gpu.md
[43] Olares. “Canonical compute modes.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/framework/app-service/pkg/utils/gpu_types.go
[44] Olares. “Compute device share-mode mutation.” Source-Type: official. As Of: 2026-07-10 (`6f2b93e`). /Users/pengpeng/Olares/framework/app-service/pkg/compute/device_mode.go
[45] Qwen. “Qwen3-TTS-12Hz-0.6B-Base model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base
[46] PaddlePaddle. “PaddleOCR-VL-1.6 model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6
[47] Tencent. “Hy-MT2-1.8B model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/tencent/Hy-MT2-1.8B
[48] Tongyi-MAI. “Z-Image-Turbo model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
[49] Stability AI. “Stable Fast 3D model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/stabilityai/stable-fast-3d
[50] OpenBMB. “MiniCPM-o 4.5 model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/openbmb/MiniCPM-o-4_5
[51] NVIDIA. “GeForce RTX 5090.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/
[52] NVIDIA. “GeForce RTX 5080.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/
[53] NVIDIA. “DGX B200.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/data-center/dgx-b200/
[54] NVIDIA. “H200 GPU.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/data-center/h200/
[55] NVIDIA. “GeForce RTX 4090.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/
[56] NVIDIA. “GeForce RTX 3090 family.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/
[57] Baidu. “Unlimited-OCR model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/baidu/Unlimited-OCR
[58] BAAI. “BGE-M3 model card.” Source-Type: official. As Of: 2026-07-15. https://huggingface.co/BAAI/bge-m3
[59] Ideogram. “Ideogram 4.0 technical details.” Source-Type: official. As Of: 2026-07-15. https://ideogram.ai/blog/ideogram-4.0/
[60] Intel. “Intel Core Ultra processor names and numbers.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/support/articles/000097596/processors/intel-core-ultra-processors.html
[61] Intel. “Core Ultra Series 3 launch and Panther Lake positioning.” Source-Type: official. As Of: 2026-01-05. https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a
[62] Intel. “Core Ultra X9 388H specifications.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/products/sku/245526/intel-core-ultra-x9-processor-388h-18m-cache-up-to-5-10-ghz/specifications.html
[63] Intel. “Core Ultra X7 368H specifications.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/products/sku/245523/intel-core-ultra-x7-processor-368h-18m-cache-up-to-5-00-ghz/specifications.html
[64] Intel. “Core Ultra Series 2 press kit.” Source-Type: official. As Of: 2026-07-15. https://newsroom.intel.com/press-kit/press-kit-core-ultra-series-2
[65] Intel. “Core Ultra Series 1 AI PC launch.” Source-Type: official. As Of: 2023-12-14. https://newsroom.intel.com/client-computing/core-ultra-client-computing-news-1
[66] Intel. “Lunar Lake architecture fact sheet.” Source-Type: official. As Of: 2024-06-04. https://download.intel.com/newsroom/2024/client-computing/Lunar-Lake-Architecture-Fact-Sheet.pdf
[67] Ars Technica. “Core Ultra Series 2 mobile portfolio analysis.” Source-Type: journalism. As Of: 2025-01-06. https://arstechnica.com/gadgets/2025/01/intel-rounds-out-core-ultra-200-laptop-cpus-with-new-but-less-advanced-models/
[68] PCWorld. “Lunar Lake package memory does not extend across later families.” Source-Type: journalism. As Of: 2024-10-31. https://www.pcworld.com/article/2507953/lunar-lakes-integrated-dram-wont-happen-again-intel-ceo-says.html
[69] Nielsen Norman Group. “Technical jargon.” Source-Type: secondary-industry. As Of: 2020-09-15. https://www.nngroup.com/articles/technical-jargon/
[70] Garner et al. “Assertion-evidence slide structure and cognitive load.” Source-Type: academic. As Of: 2009-11. http://writing.engr.psu.edu/Garner_et_al_2009.pdf
[71] Olares Apps. “LocalAI manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/localai/OlaresManifest.yaml
[72] Olares Apps. “OpenLLM manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/openllm/OlaresManifest.yaml
[73] Olares Apps. “Speaches v3 manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/speachesv3/OlaresManifest.yaml
[74] LocalAI. “LocalAI overview.” Source-Type: official. As Of: 2026-07-15. https://localai.io/docs/overview/index.html
[75] BentoML. “OpenLLM repository and serving documentation.” Source-Type: official. As Of: 2026-07-15. https://github.com/bentoml/OpenLLM
[76] Speaches. “Speaches model-server repository.” Source-Type: official. As Of: 2026-07-15. https://github.com/speaches-ai/speaches
[77] Comfy. “ComfyUI documentation.” Source-Type: official. As Of: 2026-07-15. https://docs.comfy.org/
[78] RunLocalAI. “Local AI inference runtime landscape.” Source-Type: secondary-industry. As Of: 2026-05. https://www.runlocalai.co/maps/inference-runtimes-2026
[79] Olares Apps. “KoboldCpp manifest.” Source-Type: official. As Of: 2026-07-03 (`bad4b06`). /Users/pengpeng/terminus-apps/koboldcpp/OlaresManifest.yaml
[80] LostRuins. “KoboldCpp repository and API documentation.” Source-Type: official. As Of: 2026-07-15. https://github.com/LostRuins/koboldcpp
