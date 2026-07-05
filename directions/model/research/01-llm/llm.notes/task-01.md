---
task_id: 01
role: LLM 研究专员
status: complete
sources_found: 25
---

## Sources
[1] Qwen3.6 官方仓库 (QwenLM/Qwen3.6) | https://github.com/QwenLM/Qwen3.6 | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[2] Qwen3-Coder 官方仓库 (QwenLM/Qwen3-Coder) | https://github.com/QwenLM/Qwen3-Coder/ | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[3] Qwen3-Coder 官方博客 | https://qwenlm.github.io/blog/qwen3-coder/ | Source-Type: official | As Of: 2025-07 | Authority: 9/10
[4] GLM-5 官方博客 (Z.ai) | https://z.ai/blog/glm-5 | Source-Type: official | As Of: 2026-02 | Authority: 9/10
[5] GLM-5 官方仓库 (zai-org/GLM-5) | https://github.com/zai-org/glm-5 | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[6] Kimi K2 Thinking 官方模型卡 (HF) | https://huggingface.co/moonshotai/Kimi-K2-Thinking | Source-Type: official | As Of: 2026-01 | Authority: 9/10
[7] Kimi K2 官方仓库 (moonshotai/kimi-k2) | https://github.com/moonshotai/kimi-k2 | Source-Type: official | As Of: 2026-01 | Authority: 8/10
[8] Llama 4 官方博客 (Meta) | https://ai.meta.com/blog/llama-4-multimodal-intelligence/ | Source-Type: official | As Of: 2025-04 | Authority: 9/10
[9] Llama 4 MODEL_CARD (meta-llama) | https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md | Source-Type: official | As Of: 2025-04 | Authority: 9/10
[10] Gemma 4 官方博客 (Google) | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[11] Gemma 4 官方文档 (Google AI for Developers) | https://ai.google.dev/gemma/docs/core | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[12] DeepSeek-V4-Pro 官方模型卡 (HF) | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[13] DeepSeek-V4 技术报告 (arXiv) | https://arxiv.org/html/2606.19348 | Source-Type: academic | As Of: 2026-06 | Authority: 9/10
[14] MiniMax-M2 官方模型卡 (HF) | https://huggingface.co/MiniMaxAI/MiniMax-M2 | Source-Type: official | As Of: 2025-10 | Authority: 9/10
[15] MiniMax-M2 LICENSE (GitHub) | https://github.com/MiniMax-AI/MiniMax-M2/blob/main/LICENSE | Source-Type: official | As Of: 2025-10 | Authority: 9/10
[16] Best Local LLMs for 24GB VRAM 2026 (LocalLLM.in) | https://localllm.in/blog/best-local-llms-24gb-vram | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 6/10
[17] What Can You Run on 16/24/32GB VRAM (WillItRunAI) | https://willitrunai.com/blog/what-can-you-run-on-16gb-24gb-32gb-vram | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 6/10
[18] DeepSeek V4 Flash vs Qwen3.6 vs GLM-4.6 (DeepInfra) | https://deepinfra.com/blog/deepseek-v4-flash-vs-qwen3-6-vs-glm-4-6 | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 6/10
[19] 7 Best Small Language Models Under 10B 2026 (Labellerr) | https://www.labellerr.com/blog/best-small-language-models-under-10b-parameters/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 6/10
[20] On-Device Tool Calling 2026 (Ertas AI) | https://www.ertas.ai/blog/on-device-tool-calling-2026-qwen3-gemma4-phi4 | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 5/10
[21] Kimi K2 Thinking 报道 (VentureBeat) | https://develop.venturebeat.com/ai/moonshots-kimi-k2-thinking-emerges-as-leading-open-source-ai-outperforming | Source-Type: journalism | As Of: 2026-01 | Authority: 7/10
[22] What Is Kimi K2.6 (Verdent) | https://www.verdent.ai/guides/what-is-kimi-k2-6 | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 5/10
[23] DeepSeek-V4 HF 博客 | https://huggingface.co/blog/deepseekv4 | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 7/10
[24] Gemma 4 vs Llama 4 vs Mistral Small 4 (DigitalApplied) | https://www.digitalapplied.com/blog/gemma-4-vs-llama-4-vs-mistral-small-4-comparison | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 5/10
[25] LLM 架构进展 mHC/压缩注意力 (Sebastian Raschka) | https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10

## Findings
- Qwen3.6-27B（dense）是当前 24GB 单卡本地最强全能模型，Intelligence Index 45.8、TAU2 94.2%，Apache 2.0。[16][1]
- Qwen3.6-35B-A3B（MoE，3B active）主打推理吞吐，消费级卡 65–90 tok/s，同为 Apache 2.0。[1][16][17]
- Qwen3-Coder 有 480B-A35B、30B-A3B、Coder-Next（80B-A3B）三档，256K 原生上下文（可外推 1M），SWE-bench 对标 Claude Sonnet 4。[2][3]
- GLM-5 系列 744B-A40B MoE，MIT 许可，集成 DeepSeek Sparse Attention 降本，对标 GPT-5.2/Claude Opus；已迭代到 GLM-5.2（1M 上下文，2026-06）。[4][5]
- DeepSeek V4 双档：Pro 1.6T-A49B、Flash 284B-A13B，均 1M 上下文、MIT；1M 上下文下 Pro 仅需 V3.2 的 27% FLOPs、10% KV cache。[12][13]
- Kimi K2 Thinking 1T-A32B，原生 INT4 QAT、256K 上下文、Modified MIT，HLE/BrowseComp 达开源 SOTA；已有 K2.6（2026-04）。[6][21][22]
- MiniMax M2 230B-A10B MoE，Modified MIT，SWE-bench Verified 69.4，主打 coding/agentic，10B active 部署成本低。[14][15]
- Gemma 4 五档（E2B/E4B/12B/26B-A4B/31B），Apache 2.0；31B 为 Arena 第 3 开源模型、26B 第 6，256K 上下文。[10][11]
- Gemma 4 E4B Q4 约 4.5GB、128K 上下文、原生 audio，适合手机离线 agent/tool-calling。[19][11][20]
- Llama 4 Scout 109B-A17B / Maverick 400B-A17B（2025-04），Llama 社区许可（非 OSI 开源），Behemoth 未发布已搁置，已落后 2026 前沿。[8][9][24]
- 端侧小模型三强：Qwen3-4B-Instruct-2507、Gemma 4 E4B、Phi-4-mini（3.8B，MIT），均可手机 Q4 运行；Granite 4.1 8B（Apache 2.0）为企业友好端侧选择。[20][19]
- 需剔除的过期模型：DeepSeek R1、Llama 3.x、Qwen 2.5 已被 2026 新版取代。[17][19]

## Deep Read Notes
### Source [1]/[16]: Qwen3.6 官方仓库 + LocalLLM.in 24GB 评测
Key data: Qwen3.6-27B（dense）2026-04-22 发布、35B-A3B（MoE）2026-04-16 发布，均在 HF/ModelScope。24GB 卡评测中 27B Intelligence Index 45.8、Coding 由 Gemma 4 31B（38.7）领先；35B-A3B 在 llama.cpp 65.6 tok/s。
Key insight: 27B dense 是 Olares One 24GB 甜点位的"日常主力"，35B-A3B 是速度党首选；两者都 Apache 2.0，可商用。
Useful for: 💻 本地台式级主推；"best local LLM 24GB VRAM"、"run Qwen3.6 locally" 内容。

### Source [4]/[5]: GLM-5（Z.ai）
Key data: GLM-5 744B-A40B、256 experts/8 activated、200K 上下文、28.5T tokens、MIT；DSA 降长上下文成本；GLM-5.2 已达 1M 上下文（2026-06-13）。vLLM/SGLang 可自部署（8 卡 TP）。
Key insight: MIT 许可 + 744B 前沿性能，是"可自托管的前沿旗舰"典型，但需多卡/服务器（企业级）。
Useful for: 🏢 企业级；"GLM-5 self-hosted"、"GLM-5 vs GPT-5"。

### Source [12]/[13]: DeepSeek V4（模型卡 + arXiv）
Key data: V4-Pro 1.6T-A49B、V4-Flash 284B-A13B，均 1M 上下文、MIT；混合注意力 CSA+HCA、mHC、Muon 优化器；1M 上下文 Pro 仅 V3.2 27% FLOPs/10% KV，Flash 10% FLOPs/7% KV。Flash 量化后可单 80GB GPU / 2×48GB 跑。
Key insight: Flash 是"能落地的 V4"，长上下文 agent 场景性价比高；Pro 需 4×80GB+，纯企业级。
Useful for: 🏢 企业级 + 长上下文 agent；"DeepSeek V4 Flash VRAM"、"run DeepSeek V4 locally"。

### Source [6]/[21]: Kimi K2 Thinking
Key data: 1T-A32B MoE、原生 INT4 QAT、256K 上下文、Modified MIT（>1 亿 MAU 或 >$2000 万/月营收须标注 "Kimi K2"）；HLE/BrowseComp SOTA，稳定 200–300 次连续工具调用。
Key insight: 开源 agentic 推理领头羊，超过 MiniMax M2 与部分闭源；INT4 原生降低部署门槛但仍为 1T 级企业硬件。
Useful for: 🏢 企业级 agentic；"Kimi K2 Thinking local"、"open source alternative to GPT-5"。

### Source [10]/[11]: Gemma 4（Google）
Key data: 五档 E2B/E4B/12B/26B-A4B/31B，Apache 2.0，256K（31B）；31B Arena 第 3 开源、26B 第 6；E2B/E4B 与 Qualcomm/MediaTek/Pixel 合作可手机离线；E4B Q4 4.5GB。
Key insight: 唯一横跨手机→本地台式的 Apache 2.0 全家桶，对标 Gemini Nano/Flash，端侧多模态最强。
Useful for: 📱 边缘 + 💻 本地；"Gemma 4 E4B on device"、"Gemma 4 vs Llama 4"。

## Gaps
- Mistral 2026 新版（Mistral Small 4 / Medium 3）缺官方一手源，仅二手对比文（[24]），置信度较低，报告中标注为待核。
- IBM Granite 4.1 具体尺寸/发布日仅二手源（[19]），未取到官方模型卡。
- 相反主张候选：DeepInfra [18] 与 HF 博客 [23] 均指出 DeepSeek V4 基准"competitive but not SOTA"，与部分"V4 redefines SOTA"（[13] Pro-Max 模式）口径不同——SOTA 与否取决于是否开 Think Max/Pro-Max 及具体基准。
- "Ornith" 等题目示例模型未在检索中出现，未收录（避免编造）。

## END
