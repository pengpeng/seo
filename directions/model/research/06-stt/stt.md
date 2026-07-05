# 开源 STT/ASR 语音识别（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 18 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 72%

## 摘要

到 2026 年，开源 STT/ASR 已在**准确率上追平甚至反超闭源云 API**：Open ASR Leaderboard 论文的英语短音频榜上，前几名几乎全是开源模型——NVIDIA Canary-Qwen 2.5B（5.6% WER）、Qwen3-ASR 1.7B（5.76%）、IBM Granite Speech 3.3 2B（6.00%）都排在闭源 ElevenLabs Scribe v2（5.83%）与 AssemblyAI Universal-3 Pro（6.21%）之上 [3]。这对 Olares 这类"本地推理、数据归用户"的个人云是关键信号：**高质量转写不再必须上传到 Deepgram/AssemblyAI，可以完全在本地跑。**

选型的核心权衡有两条主轴：**准确率 vs 吞吐**（Conformer+LLM 解码器最准但慢，CTC/TDT 解码器快 10–100× 但略降准确率）[3][9]，以及**多语言 vs 单语专精**（多语言覆盖会牺牲单语性能）[9]。据此本报告按部署层级给出型号总表：📱 边缘级（Moonshine、Qwen3-ASR-0.6B、Whisper Tiny/Base）、💻 本地台式主力（Whisper Large v3 / Turbo、Parakeet TDT 0.6B v3、Qwen3-ASR-1.7B、Canary-Qwen 2.5B、Voxtral Mini 3B、Granite Speech 3.3 2B）、🏢 高显存（Granite Speech 3.3 8B、Voxtral Small 24B）。2026 年最重要的两个新增是 **Qwen3-ASR（Apache 2.0，52 语言，当前开源 SOTA）**与 **Moonshine（MIT，27M 起，端侧首选）**。

## 1. 型号总表（核心交付）

| 模型 | 代表型号/参数量 | 部署层级 | 许可 | 闭源对标 | 候选关键词 |
|------|----------------|----------|------|----------|-----------|
| **Moonshine** | Tiny 27M / Base 61M / Small 123M / Medium 245M（英语 + ar/uk/ja/ko/zh/vi 单语）[11][12] | 📱 边缘/CPU | MIT | Deepgram Flux / 云实时 | `on device speech to text`, `raspberry pi speech recognition`, `moonshine asr`（低竞争） |
| **Qwen3-ASR-0.6B** | 0.6B，52 语言与方言，TTFT ~92ms [4][5][6] | 📱 边缘/💻 | Apache 2.0 | AssemblyAI Universal-2 | `qwen3 asr`, `chinese speech to text open source`（低竞争） |
| **Whisper Large v3 Turbo** | 809M，99+ 语言，MIT，~6GB [1][2] | 💻 台式主力 | MIT | OpenAI gpt-4o-transcribe | `whisper large v3 turbo`, `run whisper locally`（中） |
| **Whisper Large v3** | 1.55B，99+ 语言，~10GB [1][2][3] | 💻 台式主力 | MIT | Deepgram Nova-3 | `whisper alternative`, `whisper.cpp local`（中） |
| **Distil-Whisper Large v3.5** | 756M，英语，~5GB [1][3] | 💻 台式 | MIT | — | `distil whisper`, `fast whisper transcription`（低） |
| **NVIDIA Parakeet TDT 0.6B v3** | 0.6B，25 语言，Avg WER 6.34%，RTFx ~3330 [8][3] | 💻 台式（吞吐王） | CC-BY-4.0 | Deepgram Nova-3 streaming | `parakeet tdt`, `fastest open source asr`（低竞争） |
| **NVIDIA Canary-Qwen 2.5B** | 2.5B，英语，5.63% WER（英语短音频最高）[1][2] | 💻 台式 | CC-BY-4.0 | ElevenLabs Scribe v2 | `canary qwen`, `most accurate open asr`（低） |
| **Qwen3-ASR-1.7B** | 1.7B，52 语言与方言，开源 SOTA（5.76% WER）[3][4][5][6] | 💻 台式主力 | Apache 2.0 | AssemblyAI Universal-3 Pro | `qwen3 asr 1.7b`, `best open source asr 2026`（低竞争） |
| **Mistral Voxtral Mini** | 4.7B 总（英/西/法/葡/印地/德/荷/意）[13][14][15] | 💻 台式 | Apache 2.0 | OpenAI Whisper API | `voxtral`, `open source audio understanding`（低） |
| **IBM Granite Speech 3.3 2B** | ~2B，英语 ASR + 多语言翻译，6.00% WER [16][3] | 💻 台式 | Apache 2.0 | AssemblyAI + LLM | `granite speech`, `speech translation open source`（低） |
| **IBM Granite Speech 3.3 8B** | ~9B，ASR+AST，5.85% WER [16][1][2] | 🏢 高显存 | Apache 2.0 | Deepgram + LLM | `granite speech 3.3 8b`, `enterprise open asr`（低） |
| **Mistral Voxtral Small** | 24.3B，多语言，32K 上下文 ~30–40 分钟音频 [13][14][15] | 🏢 高显存 | Apache 2.0 | ElevenLabs Scribe v2 | `voxtral 24b`, `local audio q&a`（低） |

> 注：VRAM 多为按参数量估算，各厂商官方极少公布显存官方值 [1]；量化版（whisper.cpp/GGUF、int8）按选型准则忽略，但端侧落地通常靠它们。

## 2. 分层解读（轻量 vs GPU；多语言/准确率）

### 📱 边缘/CPU 级——Moonshine 与 Qwen3-ASR-0.6B

**Moonshine（MIT）**是 2026 年端侧转写的首选。Tiny 仅 27M 参数，平均错误率比同尺寸 Whisper Tiny 低约 48%，多数场景匹配或超过 28× 大的 Whisper Medium [11]。其"变长编码"免去 Whisper 把每段 padding 到 30 秒的浪费，使每秒音频推理比 Whisper 同级快 5–15×；在树莓派 5 上 Small 流式版延迟约 527ms、Tiny 约 237ms [11]。团队还放出了 ar/uk/ja/ko/zh/vi 六个单语 Tiny 模型，证明"高质量数据下小单语模型可超大多语言模型" [11]。

**Qwen3-ASR-0.6B（Apache 2.0）**提供另一条边缘路线：52 语言与方言、TTFT 低至 92ms、并发 128 下 1 秒可转写 2000 秒音频，是准确率-效率的最佳平衡点 [4][6]。相比只做英语的 Moonshine，它把中文（含大量方言 + 粤语 + 闽南/吴语）也带到了边缘档。Whisper Tiny/Base（MIT）作为老牌兜底仍可用，但已被上述两者在同尺寸下超越 [11]。

### 💻 本地台式主力——准确率与吞吐两条线

准确率线：**Canary-Qwen 2.5B**（CC-BY-4.0）在英语短音频上是最高准确率 5.63% WER [1][2]，**Qwen3-ASR-1.7B**（Apache 2.0）是开源 SOTA、5.76% WER 且接近最强闭源 API [3][5]。两者差异在许可与多语言：Qwen3-ASR 覆盖 52 语言且 Apache 2.0 更自由，Canary-Qwen 仅英语且单段约 40 秒、长音频需自行切分 [1][2]。

吞吐线：**Parakeet TDT 0.6B v3**（CC-BY-4.0）是吞吐王，FastConformer+TDT 架构使 RTFx 达 ~3330、Avg WER 6.34%，比同榜竞品快约 3×，适合批量/实时流式 [8][3]。TDT（Token-and-Duration Transducer）在 RNN-T 上加一个"预测每个 token 覆盖几帧"的头，让解码器跳帧而非逐帧前进，以极小的准确率代价换来巨大吞吐 [10]。

多语言标准线：**Whisper Large v3 / Turbo**（MIT，99+ 语言）仍是覆盖面最广、生态最成熟（whisper.cpp 等）的选择；Turbo 809M 速度更快、准确率接近 Large v3 [1][2]。需要英语高吞吐可选 **Distil-Whisper Large v3.5** [1][3]。此外 **Voxtral Mini 3B** 与 **Granite Speech 3.3 2B**（均 Apache 2.0）把"转写 + 理解/翻译"合并进一次调用 [13][16]。

### 🏢 高显存——转写即理解

**Granite Speech 3.3 8B**（~9B，Apache 2.0）面向企业级 ASR + 语音翻译（AST，支持英↔法/德/西/葡，以及英→日/中），采用两段式设计：先转写、再显式调用底层 granite-3.3-8b-instruct 处理文本，Avg WER 5.85% [16][1]。**Voxtral Small 24B**（Apache 2.0）是语音-文本多模态 LLM，32K 上下文可处理 30–40 分钟音频，能在同一次调用里直接对音频问答/摘要，无需另接 ASR+LLM 流水线 [13][14][15]。

### 一个必须标注的口径差异

厂商博客常宣称 Canary-Qwen 2.5B 是"最准的开源模型（5.63%）"[1][2]，但这只成立于**英语短音频**。在 Open ASR Leaderboard 的多语言/长表评测中，Canary 反而只有 11.2、且开源整体仍落后闭源（Parakeet v3 10.7、Whisper Turbo 11.0、Whisper Large v3 11.2，闭源 ElevenLabs Scribe v2 以 7.32 领先）[3]。**结论：长音频 / 多语言场景，开源尚未夺冠，选型要看具体音频类型。**

### 闭源对标（云 ASR）

- **Deepgram Nova-3**：5.26% batch WER，$0.0043/min 批处理、$0.0077/min 流式，主打超低延迟语音代理 [18]。
- **AssemblyAI**：Universal-2 $0.15/hr（99+ 语言）、Universal-3 Pro $0.21/hr（~5.6% WER），富含情感/实体/摘要等分析 [19]。
- **ElevenLabs Scribe v2**：准确率标杆之一（榜单 5.83 英语 / 7.32 多语言长表）[3]。
- **Otter.ai**：$16.99/月消费级会议转写工具（非开发者 API）[17]。

对 Olares 用户，用 Qwen3-ASR-1.7B 或 Whisper Large v3 本地跑，即可在准确率相当的前提下省掉这些按分钟/小时计费的云成本，且音频不出本地。

## 3. 候选 SEO 关键词与内容切入

**型号词（低竞争、抢新词）**：`qwen3 asr` / `qwen3 asr 1.7b`、`parakeet tdt` / `parakeet tdt 0.6b v3`、`canary qwen 2.5b`、`moonshine asr`、`voxtral` / `voxtral local`、`granite speech 3.3`、`distil whisper v3.5`——这些 2025–2026 新模型词竞争度普遍低，适合抢发（GEO/型号首屏）。

**能力/意图词**：`speech to text open source`、`best open source asr 2026`、`self hosted speech to text`、`local speech recognition`、`run whisper locally`、`fastest open source asr`、`chinese speech to text open source`、`on device / raspberry pi speech recognition`。

**Alternative / 对比词（转化强）**：`deepgram alternative open source`、`assemblyai alternative`、`whisper alternative`、`otter ai alternative self hosted`、`qwen3 asr vs whisper`、`parakeet vs whisper`。

**Olares 内容切入建议**：
1. 「best open-source speech-to-text you can self-host (2026)」——总表型文章，主打"本地跑、数据不出门"，落 Qwen3-ASR/Whisper/Parakeet/Moonshine。
2. 「run Qwen3-ASR / Whisper locally on your own cloud」——how-to + Olares 一键部署叙事。
3. 「Deepgram / AssemblyAI / Otter alternative: self-hosted ASR」——用价格+隐私双卖点做替代文。
4. 「on-device speech to text: Moonshine on Raspberry Pi / Olares One」——端侧长尾。

## 关键发现（2-3）

1. **开源已在英语准确率上超越闭源云 API**：Canary-Qwen 2.5B、Qwen3-ASR 1.7B、Granite Speech 3.3 2B 均排在 ElevenLabs Scribe v2、AssemblyAI Universal-3 Pro 之上 [3]——"本地推理不必牺牲质量"是 Olares 最强的内容论点。
2. **2026 两大新王**：Qwen3-ASR（Apache 2.0，52 语言与方言，开源 SOTA，含丰富中文方言）覆盖台式主力与边缘 0.6B [4][5][6]；Moonshine（MIT，27M 起）统治端侧/CPU/树莓派 [11]。二者许可宽松，最适合打包进 Olares。
3. **选型看音频类型**：准确率选 Canary-Qwen/Qwen3-ASR，吞吐/实时选 Parakeet TDT，多语言覆盖选 Whisper，端侧选 Moonshine，"转写即问答"选 Voxtral/Granite [1][3][13]。

## 局限性

- Open ASR Leaderboard 英语短表与多语言/长表口径差异大，"最准开源"仅限英语短音频；长表/多语言开源仍落后闭源，报告中数字须带评测集口径 [3]。
- Canary-Qwen 2.5B 缺官方 model card 直读，参数/许可来自榜单与厂商博客二手 [1][2]；多数模型无官方 VRAM 数字，均按参数量估算。
- 闭源 WER 与定价随时间与套餐变动（Deepgram/AssemblyAI/Otter 价格页时效性高），引用前应复核官网 [18][19]。
- 量化版本按选型准则忽略，但端侧真正落地（whisper.cpp/GGUF/int8、ONNX）多依赖量化，后续内容需单独覆盖。

## 参考文献

[1] Northflank — Best open source STT model in 2026 (benchmarks) | https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks
[2] Gladia — Best open-source speech-to-text models in 2026 | https://www.gladia.io/blog/best-open-source-speech-to-text-models
[3] Open ASR Leaderboard 论文 | arXiv 2510.06961v4 | https://arxiv.org/html/2510.06961v4
[4] QwenLM/Qwen3-ASR (GitHub) | https://github.com/QwenLM/Qwen3-ASR
[5] Qwen/Qwen3-ASR-1.7B (Hugging Face) | https://huggingface.co/Qwen/Qwen3-ASR-1.7B
[6] Qwen3-ASR Technical Report | arXiv 2601.21337 | https://arxiv.org/html/2601.21337
[7] Alibaba Cloud — Qwen3-ASR & ForcedAligner open sourced | https://www.alibabacloud.com/blog/qwen3-asr-%26-qwen3-forcedaligner-is-now-open-sourced-robust-streaming-and-multilingual_602843
[8] NVIDIA parakeet-tdt-0.6b-v3 (Hugging Face) | https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3
[9] Hugging Face — Open ASR Leaderboard: Trends & Insights | https://huggingface.co/blog/open-asr-leaderboard
[10] NVIDIA — Accelerating Leaderboard-Topping ASR Models 10x with NeMo | https://developer.nvidia.com/blog/accelerating-leaderboard-topping-asr-models-10x-with-nvidia-nemo/
[11] moonshine-ai/moonshine (GitHub) | https://github.com/moonshine-ai/moonshine
[12] UsefulSensors/moonshine-tiny (Hugging Face) | https://huggingface.co/UsefulSensors/moonshine-tiny
[13] mistralai/Voxtral-Small-24B-2507 (Hugging Face) | https://huggingface.co/mistralai/Voxtral-Small-24B-2507
[14] Mistral AI — Voxtral | https://mistral.ai/news/voxtral/
[15] Voxtral 论文 | arXiv 2507.13264 | https://arxiv.org/html/2507.13264v1
[16] ibm-granite/granite-speech-3.3-8b (Hugging Face) | https://huggingface.co/ibm-granite/granite-speech-3.3-8b
[17] UsefulAI — 11 Best Transcription Models in 2026 | https://usefulai.com/models/ai-transcription-models
[18] Deepgram — Best Speech-to-Text APIs in 2026 | https://deepgram.com/learn/best-speech-to-text-apis-2026
[19] AssemblyAI — AssemblyAI vs Deepgram | https://www.assemblyai.com/blog/assemblyai-vs-deepgram
