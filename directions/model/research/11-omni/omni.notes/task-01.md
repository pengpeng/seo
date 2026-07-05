---
task_id: 01
role: Omni 多模态研究专员
status: complete
sources_found: 16
---

## Sources
[1] Alibaba/QwenLM — Qwen3-Omni GitHub README | https://github.com/QwenLM/Qwen3-Omni | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[2] Qwen Team — Qwen3-Omni Technical Report (arXiv 2509.17765) | https://arxiv.org/html/2509.17765 | Source-Type: official/academic | As Of: 2025-09 | Authority: 10/10
[3] AI/TLDR — Qwen3-Omni: Specs, Benchmarks & Pricing | https://ai-tldr.dev/models/qwen3-omni/ | Source-Type: third-party aggregator | As Of: 2025-10 | Authority: 5/10
[4] Qwen Team — Qwen3.5-Omni Technical Report (arXiv 2604.15804) | https://arxiv.org/html/2604.15804v1 | Source-Type: official/academic | As Of: 2026-04 | Authority: 9/10
[5] The Decoder — Qwen3.5-Omni release coverage | https://the-decoder.com/qwen3-5-omni-learned-to-write-code-from-spoken-instructions-and-video-without-anyone-training-it-to/ | Source-Type: tech press | As Of: 2026-03 | Authority: 6/10
[6] OpenBMB — MiniCPM-o-2_6 model card (Hugging Face) | https://huggingface.co/openbmb/MiniCPM-o-2_6 | Source-Type: official | As Of: 2025-01 | Authority: 9/10
[7] OpenBMB — MiniCPM-o GitHub README (incl. MiniCPM-o 4.5) | https://github.com/OpenBMB/MiniCPM-o | Source-Type: official | As Of: 2026-05 | Authority: 9/10
[8] OpenBMB — MiniCPM-o 4.5 Technical Report (arXiv 2604.27393) | https://arxiv.org/html/2604.27393 | Source-Type: official/academic | As Of: 2026-04 | Authority: 9/10
[9] Qwen Team — Qwen3-VL Technical Report (arXiv 2511.21631) | https://arxiv.org/pdf/2511.21631 | Source-Type: official/academic | As Of: 2025-11 | Authority: 10/10
[10] Qwen Team — Qwen3-VL docs (model variants / cards) | https://qwenlm-qwen3-vl.mintlify.app/concepts/model-variants | Source-Type: official docs | As Of: 2025-11 | Authority: 8/10
[11] OpenGVLab — InternVL3.5 blog | https://internvl.github.io/blog/2025-08-26-InternVL-3.5/ | Source-Type: official | As Of: 2025-08 | Authority: 9/10
[12] OpenGVLab — InternVL3.5-241B-A28B model card (Hugging Face) | https://huggingface.co/OpenGVLab/InternVL3_5-241B-A28B-Instruct | Source-Type: official | As Of: 2025-08 | Authority: 9/10
[13] Zhipu/Z.ai — GLM-V GitHub README (GLM-4.6V/4.5V/4.1V) | https://github.com/zai-org/GLM-V | Source-Type: official | As Of: 2026-05 | Authority: 9/10
[14] AI/TLDR — GLM-4.5V specs (incl. GLM-4.6V) | https://ai-tldr.dev/models/glm-4-5v/ | Source-Type: third-party aggregator | As Of: 2025-12 | Authority: 5/10
[15] Google — Gemma 3 model card (ai.google.dev) | https://ai.google.dev/gemma/docs/core/model_card_3 | Source-Type: official | As Of: 2025-03 | Authority: 10/10
[16] Ant Group/inclusionAI — Ming-flash-omni 2.0 GitHub README | https://github.com/inclusionAI/Ming | Source-Type: official | As Of: 2026-02 | Authority: 9/10

## Findings
- Qwen3-Omni（Qwen3-Omni-30B-A3B）是原生端到端 omni-modal 模型，处理文本/图像/音频/视频，实时输出文本+语音；Apache 2.0；Thinker-Talker MoE，30B 总/~3B 激活。[1][2]
- Qwen3-Omni 在 36 个音频/音视频基准上 32 个开源 SOTA、22 个总体 SOTA，音频能力可比 Gemini 2.5 Pro，超过 GPT-4o-Transcribe；支持 119 文本语言、19 语音输入、10 语音输出，理论首包延迟 234ms。[2]
- Qwen3.5-Omni（2026-03-30）扩展到 256K 上下文、10+ 小时音频、400+ 秒 720p 视频；含 Plus/Flash/Light 变体，官方技术报告称 Plus 在关键音频任务超 Gemini-3.1 Pro。[4]
- 关键分歧：The Decoder 报道 Qwen3.5-Omni 发布时**未公开权重、未定许可、仅 API**；而第三方（awesomeagents/spheron）称 Light 变体 Apache 2.0 可自托管——开源可跑性存疑，需以官方模型卡为准。[5][4]
- MiniCPM-o 2.6 为端到端 omni（8B，基于 SigLip-400M + Whisper-medium + ChatTTS + Qwen2.5-7B），视觉/语音/多模态直播达 GPT-4o-202405 水平，可在 iPad 等端侧实时跑。[6]
- MiniCPM-o 4.5（9B，基于 SigLip2 + Whisper-medium + CosyVoice2 + Qwen3-8B）新增全双工多模态直播，视觉能力逼近 Gemini 2.5 Flash，OpenCompass 均分 77.6，在 omni 理解上超越 Qwen3-Omni-30B-A3B。[7][8]
- Qwen3-VL 为视觉语言模型（文本+图像+视频、**无音频**），dense 2B/4B/8B/32B + MoE 30B-A3B/235B-A22B，旗舰 235B-A22B（235B 总/22B 激活），256K 上下文，Apache 2.0。[9][10]
- InternVL3.5（OpenGVLab）1B~241B-A28B（dense+MoE，基于 Qwen3 backbone + InternViT），Apache 2.0；旗舰 241B-A28B 在开源 MLLM 中 SOTA，缩小与 GPT-5 差距。[11][12]
- GLM-4.5V（Zhipu，2025-08-11）106B-A12B MoE，MIT 许可，处理图像/视频/文档/GUI；GLM-V 仓库现含 GLM-4.6V（106B）与 GLM-4.6V-Flash（9B，端侧优化）。[13][14]
- Gemma 3（Google）4B/12B/27B 支持文本+图像多模态，128K 上下文，QAT 量化可在单张 RTX 3090 跑 27B；Gemma 许可（允许"负责任商用"，非 OSI）。[15]
- Gemma 4 扩展多模态：E2B/E4B/12B 原生支持文本+图像+视频+音频；12B 为 encoder-free 统一多模态模型（用线性投影替代视觉/音频编码器）。[15]
- Ming-flash-omni 2.0（Ant Group/inclusionAI，2026-02-11）基于 Ling-2.0，100B 总/6B 激活 MoE；输入图像+文本+视频+音频，输出图像+文本+音频，号称开源 omni-MLLM 新 SOTA，含图像生成与语音合成。[16]

## Deep Read Notes
### Source [2]: Qwen3-Omni Technical Report
Key data: 30B-A3B MoE；36 音频/音视频基准 32 开源 SOTA/22 总体 SOTA；119/19/10 语言；首包 234ms；Apache 2.0。
Key insight: 首个"无跨模态退化"的单一 omni 模型，音频强于 GPT-4o-Transcribe、Seed-ASR。
Useful for: 型号总表核心行、闭源对标（GPT-4o/Gemini 2.5 Pro）、"run qwen3-omni locally" 内容锚点。

### Source [8]: MiniCPM-o 4.5 Technical Report
Key data: 9B；全双工 omni 直播；OpenCompass 77.6；omni 理解超 Qwen3-Omni-30B-A3B；支持 llama.cpp/Ollama CPU 推理。
Key insight: 端侧全双工"边看边听边说"，9B 体量却在 omni 理解上胜 30B 级——端侧 omni 的最强候选。
Useful for: 📱端侧层级卖点、Olares One 本地实时助手叙事。

### Source [9]: Qwen3-VL Technical Report
Key data: dense 2B/4B/8B/32B + MoE 30B-A3B/235B-A22B；SigLIP-2 视觉编码器 + DeepStack + Interleaved MRoPE；256K。
Key insight: VLM（无音频），但覆盖从边缘到云的全尺寸谱系，2B/4B 是消费级/移动端最实用的视觉理解权重。
Useful for: 端侧 VLM 分层解读、"qwen3-vl 4b" 低竞争型号词。

### Source [16]: Ming-flash-omni 2.0 README
Key data: 100B-A6B MoE（Ling-2.0）；输入 image/text/video/audio，输出 image/text/audio；2026-02 发布；HF + ModelScope。
Key insight: 目前功能最全的开源 omni（含图像生成+语音输出），但 100B 体量偏"大模型层"，本地跑需较强硬件/量化。
Useful for: 🏢层级 SOTA 标杆、"open source GPT-4o alternative" 对标。

## Gaps
- Qwen3.5-Omni 开源可跑性存在**相反主张**：[5] 称仅 API/未公开权重，[4] 官方报告主打 API，第三方称 Light 变体 Apache 2.0 可自托管——写报告时须标注"以官方模型卡为准"。
- Ming-flash-omni 2.0 的精确许可证与 VRAM/量化可跑门槛未在检索片段中确认，需查 HF 模型卡 license 字段。
- MiniCPM-o 系列许可证（商用条款）未逐条核实；Gemma 为自定义许可（非 OSI），商用需读 Gemma Terms。
- 缺少统一的第三方横向 benchmark 榜单（如 OpenCompass 多模态榜）交叉验证各家"SOTA"自述。

## END
