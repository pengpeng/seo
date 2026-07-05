---
task_id: 01
role: STT 研究专员
status: complete
sources_found: 20
---

## Sources

[1] Best open source STT model in 2026 (benchmarks) | Northflank | https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks | Source-Type: vendor-blog | As Of: 2026-07 | Authority: 6/10
[2] Best open-source speech-to-text models in 2026 | Gladia | https://www.gladia.io/blog/best-open-source-speech-to-text-models | Source-Type: vendor-blog | As Of: 2026-07 | Authority: 6/10
[3] Open ASR Leaderboard: Reproducible Multilingual & Long-Form Eval (paper) | arXiv 2510.06961v4 | https://arxiv.org/html/2510.06961v4 | Source-Type: academic | As Of: 2026-05 | Authority: 9/10
[4] QwenLM/Qwen3-ASR (repo) | GitHub | https://github.com/QwenLM/Qwen3-ASR | Source-Type: official | As Of: 2026-01 | Authority: 9/10
[5] Qwen/Qwen3-ASR-1.7B (model card) | Hugging Face | https://huggingface.co/Qwen/Qwen3-ASR-1.7B | Source-Type: official | As Of: 2026-01 | Authority: 9/10
[6] Qwen3-ASR Technical Report | arXiv 2601.21337 | https://arxiv.org/html/2601.21337 | Source-Type: official-academic | As Of: 2026-01 | Authority: 9/10
[7] Qwen3-ASR & Qwen3-ForcedAligner open sourced | Alibaba Cloud Community | https://www.alibabacloud.com/blog/qwen3-asr-%26-qwen3-forcedaligner-is-now-open-sourced-robust-streaming-and-multilingual_602843 | Source-Type: official-blog | As Of: 2026-01 | Authority: 8/10
[8] nvidia/parakeet-tdt-0.6b-v3 (model card) | Hugging Face | https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3 | Source-Type: official | As Of: 2025-08 | Authority: 9/10
[9] Open ASR Leaderboard: Trends & Insights (blog) | Hugging Face | https://huggingface.co/blog/open-asr-leaderboard | Source-Type: official | As Of: 2026 | Authority: 8/10
[10] Accelerating Leaderboard-Topping ASR Models 10x with NeMo | NVIDIA Technical Blog | https://developer.nvidia.com/blog/accelerating-leaderboard-topping-asr-models-10x-with-nvidia-nemo/ | Source-Type: official-blog | As Of: 2024-08 (updated) | Authority: 8/10
[11] moonshine-ai/moonshine (repo) | GitHub | https://github.com/moonshine-ai/moonshine | Source-Type: official | As Of: 2026 | Authority: 9/10
[12] UsefulSensors/moonshine-tiny (model card) | Hugging Face | https://huggingface.co/UsefulSensors/moonshine-tiny | Source-Type: official | As Of: 2025 | Authority: 9/10
[13] mistralai/Voxtral-Small-24B-2507 (model card) | Hugging Face | https://huggingface.co/mistralai/Voxtral-Small-24B-2507 | Source-Type: official | As Of: 2025-07 | Authority: 9/10
[14] Voxtral (announcement) | Mistral AI | https://mistral.ai/news/voxtral/ | Source-Type: official | As Of: 2025-07 | Authority: 9/10
[15] Voxtral (paper) | arXiv 2507.13264 | https://arxiv.org/html/2507.13264v1 | Source-Type: official-academic | As Of: 2025-07 | Authority: 9/10
[16] ibm-granite/granite-speech-3.3-8b (model card) | Hugging Face | https://huggingface.co/ibm-granite/granite-speech-3.3-8b | Source-Type: official | As Of: 2026 | Authority: 9/10
[17] 11 Best Transcription Models in 2026 (52 evaluated) | UsefulAI | https://usefulai.com/models/ai-transcription-models | Source-Type: vendor-blog | As Of: 2026-07 | Authority: 5/10
[18] Best Speech-to-Text APIs in 2026 | Deepgram | https://deepgram.com/learn/best-speech-to-text-apis-2026 | Source-Type: vendor | As Of: 2026 | Authority: 6/10
[19] AssemblyAI vs Deepgram: Accuracy & Speed | AssemblyAI | https://www.assemblyai.com/blog/assemblyai-vs-deepgram | Source-Type: vendor | As Of: 2026 | Authority: 6/10
[20] Top Open-Source AI STT Models in 2026 | Resemble AI | https://www.resemble.ai/resources/open-source-ai-speech-to-text-models | Source-Type: vendor-blog | As Of: 2026 | Authority: 5/10

## Findings

- Qwen3-ASR (0.6B/1.7B) released 2026-01-29 under Apache 2.0, built on Qwen3-Omni; 1.7B 版本是当前开源 ASR SOTA、与最强闭源商业 API 竞争；支持 52 语言/方言。[4][5][6][7]
- Open ASR Leaderboard 论文（英语短表）榜首为 open 模型：Canary-Qwen 2.5B 5.6% WER、Qwen3-ASR 1.7B 5.76%、IBM Granite Speech 3.3 2B 6.00%，均超过闭源 ElevenLabs Scribe v2 (5.83) 与 AssemblyAI Universal-3 Pro (6.21)。[3]
- 架构规律：Conformer 编码器 + LLM 解码器最准但慢；CTC/TDT 解码器吞吐快 10–100×、略牺牲准确率。[3][9]
- NVIDIA Parakeet TDT 0.6B v3（2025-08 发布，CC-BY-4.0）Avg WER 6.34%、RTFx ~3330，支持 25 语言，是吞吐最快的一档；比同榜竞品快约 3×。[8][3]
- Whisper Large v3（1.55B, MIT, 99+ 语言）仍是多语言事实标准；Large v3 Turbo（809M, MIT）速度更快、准确率接近；Distil-Whisper Large v3.5（756M, 英语）主打吞吐。[1][2][3]
- Canary-Qwen 2.5B（NVIDIA, CC-BY-4.0）英语最高基准准确率 5.63% WER，但单段 ~40 秒、长音频需切分。[1][2]
- IBM Granite Speech 3.3（2B 与 8B, Apache 2.0）为企业级 ASR+语音翻译（AST）；8B 参数 ~9B、Avg WER 5.85%，两段式设计（先转写、再调用底层 LLM）。[16][1][2]
- Mistral Voxtral（Mini 3B / Small 24B, Apache 2.0, 2025-07）为语音-文本多模态：可转写并直接问答/摘要，32K 上下文可处理 ~30–40 分钟音频；原生多语言（英/西/法/葡/印地/德/荷/意）。[13][14][15]
- Moonshine（Moonshine AI/Useful Sensors, MIT）主打边缘/端侧：Tiny 27M、Base 61M、Small 123M、Medium 245M；变长编码使其比 Whisper Tiny/Base/Small/Medium 每秒音频快 5–15×，Raspberry Pi 5 可跑。[11][12]
- Moonshine Tiny(27M) 平均错误率比同尺寸 Whisper Tiny 低约 48%，多数情况下匹配或超过 28× 大的 Whisper Medium；已放出 ar/uk/ja/ko/zh/vi 单语版。[11]
- 多语言/长表评测中开源仍落后闭源：Whisper Large v3 Turbo 11.0、Whisper Large v3 11.2、Parakeet TDT 0.6B v3 10.7，闭源 ElevenLabs Scribe v2 7.32 领先。[3]
- 闭源对标价格：Deepgram Nova-3 $0.0043/min 批处理（5.26% batch WER）；AssemblyAI Universal-2 $0.15/hr、Universal-3 Pro $0.21/hr；Otter.ai $16.99/月消费级；均可用自托管开源模型替代以省成本。[18][19][17]

## Deep Read Notes

### Source [3]: Open ASR Leaderboard 论文 (arXiv 2510.06961v4)
- Key data（英语短表 Avg WER / RTFx）：Canary-Qwen 2.5B 5.6/4x(LLM)；Qwen3-ASR 1.7B 5.76/148；ElevenLabs Scribe v2 5.83(闭)；Granite Speech 3.3 2B 6.00/271；Phi-4 Multimodal 6.02/151；Parakeet TDT 0.6B v2 6.05/3390；AssemblyAI Universal-3 Pro 6.21(闭)；Parakeet TDT 0.6B v3 6.32/3330。多语言/长表：Scribe v2 7.32(闭)、Cohere Labs Transcribe 9.73(开)、Parakeet v3 10.7、Whisper Turbo 11.0、Whisper Large v3 11.2、Distil-Whisper v3.5 11.7。
- Key insight：最高准确率来自开源（Conformer+LLM 解码器）；TDT/CTC 换取 10–100× 吞吐但略降准确率；长表闭源仍领先。
- Useful for：型号总表 WER/RTFx 数字、分层解读的准确率-速度权衡叙事。

### Source [4][5][6][7]: Qwen3-ASR 家族（GitHub / HF / arXiv / Alibaba Cloud）
- Key data：Qwen3-ASR-1.7B 与 0.6B，52 语言与方言（含大量中国方言 + 粤语 + 闽南/吴语）；Apache 2.0；基于 Qwen3-Omni；含 Qwen3-ForcedAligner-0.6B（11 语言对齐）；0.6B TTFT 低至 92ms，并发 128 下 1 秒转写 2000 秒音频；离线/流式；可识别唱歌与带 BGM 歌曲。发布 2026-01-29。
- Key insight：1.7B 为开源 ASR SOTA 且接近顶级闭源；0.6B 是准确率-效率最佳平衡（可入手机/边缘档）。
- Useful for：多语言维度、型号词关键词、Olares 本地部署叙事。

### Source [8]: NVIDIA Parakeet TDT 0.6B v3 (Hugging Face)
- Key data：Open ASR Leaderboard Avg WER 6.34%（LS test-clean 1.93%）；RTFx ~3330；25 语言；FastConformer+TDT；CC-BY-4.0；发布 2025-08-14。
- Key insight：吞吐王，适合批量/实时流式；v3 扩到 25 语言但英语略降。
- Useful for：吞吐/低延迟层，"fastest open ASR" 关键词。

### Source [11][12]: Moonshine (GitHub / Hugging Face)
- Key data：Tiny 27M、Base 61M、Small 123M(streaming 7.84% WER)、Medium 245M(streaming 6.65% WER)；MIT；MacBook/Linux x86/树莓派 5 延迟表现优（Tiny 34ms MacBook）；变长编码免 30 秒 padding，比 Whisper 同级快 5–15×；已放出 6 个 Tiny 单语模型（ar/uk/ja/ko/zh/vi）。
- Key insight：端侧/CPU 首选；小模型可达 Whisper Medium 级准确率。
- Useful for：📱 边缘层、"on-device / Raspberry Pi speech to text" 关键词。

### Source [13][14][15]: Voxtral (HF / Mistral / arXiv 2507.13264)
- Key data：Mini 4.7B(总, 语言解码器 3.6B)、Small 24.3B；Apache 2.0；2025-07-15 发布；32K 上下文 → 30 分钟转写/40 分钟理解；原生多语言 + 自动语言识别；语音-文本 LLM 可直接问答/摘要；Voxtral Mini Transcribe 号称优于 Whisper 且价格不到一半。
- Key insight：不仅转写还能理解音频（ASR+understanding），适合"转写即问答"场景。
- Useful for：🏢 高显存层、"open source audio understanding / Whisper alternative" 关键词。

## Gaps

- 相反主张候选：厂商博客（Northflank/Gladia）称 Canary-Qwen 2.5B "最高准确率 5.63%"，但 Open ASR Leaderboard 多语言/长表 Canary 仅 11.2、且限 ~40 秒——即"最准"仅限英语短音频，长表/多语言并非最佳，需注明口径。
- Qwen3-ASR "52 语言" 与 HF 型号卡列出的 30 语言 + 方言存在计数差异（含方言合计到 52），引用时应说明"52 语言与方言"。
- 缺 Canary-Qwen 2.5B 官方 model card 直读（本次靠榜单/厂商博客二手）；VRAM 官方数字多数模型未公布，仅按参数量估算。
- 未独立核实闭源 WER（Deepgram 5.26% / Nova-3）与各家实价的时效（价格页随时变动）。

## END
