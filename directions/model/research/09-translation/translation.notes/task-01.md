---
task_id: 01
role: 翻译研究专员
status: complete
sources_found: 17
---

## Sources

[1] Tencent-Hunyuan/Hunyuan-MT (GitHub) | https://github.com/Tencent-Hunyuan/Hunyuan-MT/ | Source-Type: official (repo) | As Of: 2025-09 | Authority: 9/10
[2] Hunyuan-MT Technical Report (arXiv 2509.05209) | https://arxiv.org/html/2509.05209v1 | Source-Type: official (primary paper) | As Of: 2025-09 | Authority: 9/10
[3] Tencent open-sources Hunyuan-MT series — SiliconANGLE | https://siliconangle.com/2025/09/01/tencent-open-sources-hunyuan-mt-translation-model-series/ | Source-Type: news | As Of: 2025-09 | Authority: 6/10
[4] Tencent-Hunyuan/Hy-MT (HY-MT1.5, GitHub) | https://github.com/Tencent-Hunyuan/Hy-MT | Source-Type: official (repo) | As Of: 2025-12 | Authority: 9/10
[5] HY-MT1.5 Technical Report (arXiv 2512.24092) | https://arxiv.org/html/2512.24092 | Source-Type: official (primary paper) | As Of: 2025-12 | Authority: 9/10
[6] tencent/Hy-MT2-1.8B (Hugging Face model card) | https://huggingface.co/tencent/Hy-MT2-1.8B | Source-Type: official (model card) | As Of: 2026-05 | Authority: 9/10
[7] facebookresearch/fairseq @ nllb (GitHub) | https://github.com/facebookresearch/fairseq/tree/nllb | Source-Type: official (repo) | As Of: 2022+ (maintained) | Authority: 9/10
[8] 200 languages within a single AI model — Meta AI blog (NLLB-200) | https://ai.meta.com/blog/nllb-200-high-quality-machine-translation/ | Source-Type: official (vendor blog) | As Of: 2022 | Authority: 8/10
[9] Open-Source Translation Models 2025: Mobile & Embedded Guide — Picovoice | https://picovoice.ai/blog/open-source-translation/ | Source-Type: industry blog | As Of: 2025 | Authority: 6/10
[10] Tower+ (arXiv 2506.17080) | http://www.arxiv.org/pdf/2506.17080 | Source-Type: official (primary paper) | As Of: 2025-06 | Authority: 8/10
[11] facebook/seamless-m4t-v2-large README (Hugging Face) | https://huggingface.co/facebook/seamless-m4t-v2-large/raw/main/README.md | Source-Type: official (model card) | As Of: 2023-11 (v2) | Authority: 9/10
[12] Seamless Communication — AI at Meta | https://ai.meta.com/research/seamless-communication/ | Source-Type: official (vendor) | As Of: 2023-12 | Authority: 8/10
[13] MADLAD-400 — Hugging Face Transformers docs | https://huggingface.co/docs/transformers/main/model_doc/madlad-400 | Source-Type: official (docs) | As Of: 2023+ | Authority: 8/10
[14] google/madlad400-10b-mt (Hugging Face model card) | https://huggingface.co/google/madlad400-10b-mt | Source-Type: official (model card) | As Of: 2023 | Authority: 8/10
[15] ByteDance-Seed/Seed-X-7B (GitHub) | https://github.com/ByteDance-Seed/Seed-X-7B | Source-Type: official (repo) | As Of: 2025-07 | Authority: 8/10
[16] Seed-X: Building Strong Multilingual Translation LLM with 7B Parameters (arXiv 2507.13618) | https://arxiv.org/html/2507.13618v1 | Source-Type: official (primary paper) | As Of: 2025-07 | Authority: 8/10
[17] Best LLMs for Translation — Crowdin Blog | https://crowdin.com/blog/best-llms-for-translation | Source-Type: industry blog | As Of: 2025 | Authority: 5/10

## Findings

- Tencent Hunyuan-MT-7B（含 ensemble 版 Chimera-7B）2025-09-01 开源，7B 参数，支持 33 语言互译（含 5 个中国少数民族语言/方言），WMT25 竞赛在 31 个语言类别中 30 个夺冠。[1][2][3]
- Hunyuan-MT-7B 在 WMT25 上优于 Google Translate，且在多数语向超过 GPT-4.1 与 Claude 4 Sonnet；同规模翻译专用模型中 SOTA。[2][3]
- 2025-12-30 Tencent 升级发布 HY-MT1.5-1.8B 与 HY-MT1.5-7B（33 语言）；7B 在 FLORES-200 达 Gemini-3.0-Pro 约 95%，WMT25 XCOMET-XXL 0.6159（FLORES-200 XCOMET 0.8690），并在 WMT25/汉-少数民族语向超越 Gemini-3.0-Pro。[4][5]
- HY-MT1.5-1.8B 参数不到 7B 的三分之一，性能接近 7B；WMT25 XCOMET-XXL 0.5308，全面超越 Tower-Plus-72B、Qwen3-32B 等更大开源模型及 Microsoft/Doubao 商用 API，约达 Gemini-3.0-Pro 90%；量化后可边缘实时翻译。[4][5]
- 2026-05-21 Tencent 再发 Hy-MT2 系列（1.8B / 7B / 30B-A3B MoE，33 语言，"fast-thinking"）；1.8B 经 AngelSlim 1.25-bit 极限量化仅 440MB、推理提速 1.5x，可端侧部署；7B/30B-A3B 在 fast-thinking 模式下超越 DeepSeek-V4-Pro、Kimi K2.6。[6]
- Meta NLLB-200 是覆盖最广的翻译专用模型：单模型 200+ 语言；提供 MoE 54.5B、Dense 3.3B/1.3B、蒸馏 1.3B/600M；FLORES-101 上 BLEU 较此前 SOTA 平均提升 44%。[7][8]
- NLLB-200 采用 CC-BY-NC 4.0（禁止商用）；最小 distilled-600M 是 HF 最热门翻译模型但 ~2.5GB 仍偏大，移动端需量化。[9]
- Google MADLAD-400 基于 T5，提供 3B / 7.2B / 10.7B MT 模型，覆盖 400+ 语言，Apache 2.0（可商用）；10.7B 训练于 250B token，性能可比更大模型。[13][14]
- MADLAD-400 支持 GGUF 量化本地部署：3B Q8_0 约需 6GB VRAM，10B 8-bit 约需 11GB VRAM；2-bit GGUF 可压到 <1GB 供移动端。[9]
- Helsinki-NLP Opus-MT 为按语对拆分的数百个小模型，CC-BY 4.0（可商用），体积小、CPU 可跑，经 ctranslate2/transformers 离线运行。[9]
- Meta SeamlessM4T v2-large 为多模态翻译模型，2.3B 参数，支持语音输入 101 语言 / 文本 96 语言 / 语音输出 35 语言，含 S2S/S2T/T2S/T2T；CC-BY-NC 4.0；另有 Medium ~1.2B；衍生 SeamlessStreaming 实现 ~2 秒延迟实时翻译。[11][12]
- Unbabel Tower+ 系列 2B / 9B / 72B，翻译质量匹配或超过 GPT-4o-1120，通用能力超 Llama-3.3-70B、Qwen2.5-72B；9B 覆盖 24 语对；但已被 HY-MT1.5 在同/更小规模上反超。[10][5]
- ByteDance Seed-X 系列 7B（基于 Mistral-7B，词表扩至 65,269），支持 28 语言双向翻译，质量比肩 Gemini-2.5 与 GPT-4o，显著超越更大开源模型（如 Aya-32B）；OpenMDW 许可（较宽松），含 Instruct/PPO/RM 及 GPTQ-Int8/AWQ-Int4 量化版。[15][16]

## Deep Read Notes

### Source [5]: HY-MT1.5 Technical Report (arXiv 2512.24092)
- Key data: 1.8B WMT25 XCOMET-XXL 0.5308；7B FLORES-200 XCOMET 0.8690、WMT25 XCOMET-XXL 0.6159；7B 达 Gemini-3.0-Pro FLORES-200 的 95%，WMT25/汉-少数民族语向反超之。1.8B 约达 Gemini-3.0-Pro 90%。
- Key insight: 参数效率是主卖点——1.8B 就超越 72B 的 Tower-Plus；支持术语干预、上下文翻译、格式保留。
- Useful for: "run X locally" 型内容、Olares 本地台式级主力选型（7B）与边缘级（1.8B）。

### Source [6]: tencent/Hy-MT2-1.8B (HF)
- Key data: 1.8B/7B/30B-A3B(MoE)；1.25-bit 量化 1.8B→440MB、提速 1.5x；2026-05-21 发布；33 语言 + IFMTBench。
- Key insight: 端侧极限量化路线，440MB 可上手机/边缘；MoE 30B-A3B 是新增大模型档。
- Useful for: 📱手机/边缘级最强候选；"offline translation app / on-device translation"。

### Source [7][8]: NLLB-200 (fairseq + Meta blog)
- Key data: 200+ 语言，54.5B MoE / 3.3B / 1.3B / 600M；FLORES-101 BLEU +44% 均值。
- Key insight: 语言覆盖之王，尤其低资源语；但 CC-BY-NC 禁商用是硬约束。
- Useful for: "200 languages translation"、低资源语向、DeepL 覆盖不到的语种。

### Source [13][14]: MADLAD-400 (HF)
- Key data: T5 架构，3B/7.2B/10.7B，400+ 语言，Apache 2.0，250B token。
- Key insight: 唯一同时"覆盖广 + 商用友好 + 易量化"的组合，Olares 商用/自部署最省心。
- Useful for: "self-hosted commercial translation"、GGUF/llama.cpp 教程类内容。

### Source [11]: SeamlessM4T v2-large (HF README)
- Key data: 2.3B；语音 101 / 文本 96 / 语音输出 35；CC-BY-NC 4.0。
- Key insight: 语音翻译（S2S/S2T）差异化定位，非纯文本 MT；实时流式衍生模型。
- Useful for: "offline speech translation"、语音场景内容切入。

## Gaps

- 相反主张候选：多个第三方博客（[9][17]）仍把 NLLB-200 称为"开源翻译标杆/首选"，与一手技术报告 [5] 显示 2026 年 HY-MT1.5/Hy-MT2、Seed-X 已在质量上大幅领先相冲突——博客更新滞后，需以一手 arXiv/模型卡为准。
- Tower+ 具体开源许可（CC-BY-NC vs 商用）未在检索片段中确证，报告中标注为"待核"。
- 各模型 WMT25 成绩口径不一（夺冠数 vs XCOMET-XXL 绝对值 vs 相对 Gemini 百分比），跨模型直接横向可比性有限，引用时已标注口径。
- 未做 Semrush 实测，关键词竞争度为基于品牌新鲜度/长尾特征的判断性标注，非精确 KD 值。

## END
