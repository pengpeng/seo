---
task_id: 01
role: OCR 研究专员
status: complete
sources_found: 18
---

## Sources

[1] deepseek-ai/DeepSeek-OCR · Hugging Face（模型卡）| https://huggingface.co/deepseek-ai/DeepSeek-OCR | Source-Type: official | As Of: 2025-10 | Authority: 10/10
[2] DeepSeek-OCR: Contexts Optical Compression（arXiv 2510.18234）| https://arxiv.org/pdf/2510.18234 | Source-Type: official/academic | As Of: 2025-10 | Authority: 10/10
[3] PaddlePaddle/PaddleOCR-VL-1.6 · Hugging Face（模型卡）| https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6 | Source-Type: official | As Of: 2026-05 | Authority: 10/10
[4] PaddlePaddle/PaddleOCR（GitHub README）| https://github.com/PaddlePaddle/PaddleOCR | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[5] allenai/olmocr（GitHub README）| https://github.com/allenai/olmocr/ | Source-Type: official | As Of: 2026-01 | Authority: 10/10
[6] olmOCR: Unlocking Trillions of Tokens in PDFs（论文 PDF, allenai.org）| https://olmocr.allenai.org/papers/olmocr.pdf | Source-Type: official/academic | As Of: 2025-02 | Authority: 10/10
[7] rednote-hilab/dots.ocr · Hugging Face（模型卡）| https://huggingface.co/rednote-hilab/dots.ocr | Source-Type: official | As Of: 2025-07 | Authority: 9/10
[8] rednote-hilab/dots.ocr（GitHub README）| https://github.com/rednote-hilab/dots.ocr | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[9] General OCR Theory: Towards OCR-2.0（GOT arXiv 2409.01704）| https://arxiv.org/pdf/2409.01704v1 | Source-Type: official/academic | As Of: 2024-09 | Authority: 9/10
[10] Ucas-HaoranWei/GOT-OCR2.0（GitHub）| https://github.com/Ucas-HaoranWei/GOT-OCR2.0/ | Source-Type: official | As Of: 2025-02 | Authority: 9/10
[11] IBM Granite-Docling: End-to-end document understanding（IBM 官方公告）| https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion | Source-Type: official | As Of: 2025-09 | Authority: 10/10
[12] ibm-granite/granite-docling-258M · Hugging Face（模型卡）| https://huggingface.co/ibm-granite/granite-docling-258M | Source-Type: official | As Of: 2025-09 | Authority: 10/10
[13] Best OCR Model 2026: Unlimited OCR vs Surya vs Mistral（CodeSOTA 榜单）| https://www.codesota.com/ocr | Source-Type: third-party | As Of: 2026-06 | Authority: 6/10
[14] Best Open-Source OCR and Document VLMs to Self-Host on GPU Cloud 2026（Spheron Blog）| https://www.spheron.network/blog/best-open-source-ocr-vlm-self-host-gpu-cloud-2026/ | Source-Type: third-party | As Of: 2026 | Authority: 6/10
[15] Best Open Source OCR Tools & Models for Developers in 2026（Unstract Blog）| https://unstract.com/blog/best-opensource-ocr-tools/ | Source-Type: third-party | As Of: 2026 | Authority: 6/10
[16] Mistral OCR 4 vs AWS Textract vs Google Document AI（rohitraj.tech）| https://rohitraj.tech/en/notes/mistral-ocr-4-vs-textract-google-document-ai-2026 | Source-Type: third-party | As Of: 2026-06 | Authority: 6/10
[17] Mistral launches OCR 4（VentureBeat）| https://venturebeat.com/data/mistral-launches-ocr-4-turning-document-extraction-into-a-full-enterprise-ai-play | Source-Type: media | As Of: 2026-06 | Authority: 7/10
[18] olmOCR 2（LM Studio 模型页, 含 olmOCR-Bench 分表）| https://lmstudio.ai/models/olmocr2 | Source-Type: third-party | As Of: 2025-10 | Authority: 7/10

## Findings

- DeepSeek-OCR 为开源 MIT 模型：DeepEncoder（~380M）+ DeepSeek3B-MoE-A570M 解码器（3B 总参、~570M 激活），10× 压缩下 OCR 精度 ~97%，在 OmniDocBench 上以 100 vision tokens 超过 GOT-OCR2.0（256 tokens/页），单张 A100-40G 可日处理 20 万+ 页。[1][2]
- DeepSeek-OCR 本地部署：bf16 权重约 6.7GB，8–12GB VRAM 可跑标准档，Gundam 平铺档建议 40GB；官方 2025-10-23 起被 vLLM 上游支持；不官方支持 Apple Silicon，需 NVIDIA CUDA + FlashAttention。[1][4-external]
- PaddleOCR-VL-1.6（0.9B，NaViT 动态分辨率编码器 + ERNIE-4.5-0.3B 语言模型）2026-05-28 发布，OmniDocBench v1.6 达 96.33% 新 SOTA，支持 109 种语言与公式/表格/图表/印章，Apache 2.0，结构化输出 Markdown/JSON。[3][4]
- olmOCR（Allen AI，Apache 2.0）基于 7B VLM（olmOCR-2-7B 为 Qwen2.5-VL-7B 微调），把 PDF 转干净 Markdown，百万页转换约 176 美元，olmOCR-Bench overall 82.3；需 GPU。[5][6][18]
- dots.ocr（RedNote/小红书 HILab，MIT）1.7B LLM 统一版面检测+内容识别，支持 100+ 语言，2025-07-30 发布，2026-03-19 更名 dots.mocr（新增图表转 SVG）。[7][8]
- GOT-OCR2.0（约 580M，Qwen-0.5B 解码器，Apache 2.0）端到端 OCR-2.0，1024×1024→256 image tokens，可在 4GB 显存消费级 GPU 部署，社区提供 CPU 版本。[9][10]
- Granite-Docling-258M（IBM，Apache 2.0）超紧凑 258M VLM（Idefics3 架构：siglip2-base 视觉编码器 + Granite 165M LLM），输出 DocTags 保留版面/表格/公式，面向 RAG；IBM 计划后续 ~512M/900M 版本但保持 <1B。[11][12]
- 2026 榜单（CodeSOTA）：sub-1.3B 开源 VLM 领跑文档解析——PaddleOCR-VL-1.6 OmniDocBench v1.6 96.33（厂商自报），MinerU2.5-Pro（OpenDataLab, Apache 2.0）95.69，Baidu Unlimited OCR（MIT）93.92 且可一次解析 40+ 页，Surya OCR 2（Datalab, 650M）olmOCR-Bench 83.3。[13]
- 闭源对标 Mistral OCR 4（2026-06-23 发布，mistral-ocr-latest）OmniDocBench 93.07、olmOCR-Bench 85.20、170 语言，$4/1000 页（batch $2），带 bounding box、块分类、逐词置信度。[16][17]
- 云闭源定价梯度：AWS Textract 基础 $1.50/1000 页，开启表格+表单 AnalyzeDocument 达 $65/1000 页；Google Document AI $1.50–$30；Azure Document Intelligence Read ~$1.50、预置模型 ~$10。[16]
- Spheron 自托管对照表：PaddleOCR-VL-1.6 0.9B/Apache/100+ 语；DeepSeek-OCR ~3B MoE/MIT；dots.ocr ~1.7B/MIT；GOT-OCR 2.0 ~580M/Apache（<3GB VRAM）；Granite-Docling 258M/Apache（主打 EN + Docling JSON）。[14]
- Unstract 场景推荐：分类默认打印文本用 PaddleOCR；快速原型用 EasyOCR；版面感知开源 VLM 起步选 dots.OCR 或 DeepSeek-OCR；乱版/手写走 olmOCR / Qwen2.5-VL 类（算力更高，需自验证数值）。[15]

## Deep Read Notes

### Source [1][2]: DeepSeek-OCR
Key data: 3B MoE（~570M 激活）+ DeepEncoder（~380M）；权重 ~6.7GB bf16；10× 压缩 97% 精度、20× 压缩 ~60%；OmniDocBench 上 100 tokens 超 GOT-OCR2.0，<800 tokens 超 MinerU2.0；A100-40G 日产 20 万+ 页。Key insight: "光学压缩"路线把 OCR 变成 LLM 长上下文压缩工具，token 效率是核心卖点。Useful for: "run DeepSeek-OCR locally"、"DeepSeek OCR alternative to Textract" 内容。

### Source [3][4]: PaddleOCR-VL
Key data: 0.9B（ERNIE-4.5-0.3B LLM）；OmniDocBench v1.6 96.33% SOTA；109 语言；1.6 与 1.5 架构兼容零成本迁移；PP-OCRv5 提供 mobile/server 双档（mobile 面向边缘/CPU）。Key insight: 目前公开榜单最高综合分且体量最小之一——"小模型 + 高精度 + 100+ 语言"最适合本地主力。Useful for: "PaddleOCR VL"、"best open source document parsing 2026"。

### Source [5][6][18]: olmOCR
Key data: 7B（Qwen2.5-VL-7B 微调）；olmOCR-mix 26 万页训练；百万页 $176（对比 GPT-4o >$6240/百万页）；olmOCR-Bench overall 82.3；默认 FP8、vLLM 管线；Apache 2.0。Key insight: 定位"把 PDF 变 LLM 训练语料"的大规模批处理管线，成本叙事极强。Useful for: "olmOCR"、"PDF to markdown open source"、"GPT-4o OCR alternative"。

### Source [7][8][9][10]: dots.ocr & GOT-OCR2.0
Key data: dots.ocr 1.7B/MIT/100+ 语，统一 layout+OCR，2026-03 更名 dots.mocr 增 SVG；GOT-OCR2.0 ~580M/Apache，4GB 显存可跑、有 CPU 版。Key insight: 这两者覆盖"紧凑但强"与"极省显存"两个生态位。Useful for: "dots.ocr"、"got-ocr local"、低配自托管长尾词。

### Source [11][12]: Granite-Docling-258M
Key data: 258M，Idefics3（siglip2-base-patch16-512 + Granite 165M）；输出 DocTags 而非直接 Markdown，利于 RAG 溯源；Apache 2.0；计划 512M/900M 但保持 <1B。Key insight: 唯一真正"边缘/CPU 友好"的近-SOTA 文档 VLM，且与 Docling 管线原生集成。Useful for: 📱 层级、"granite-docling"、"lightweight OCR model CPU"。

### Source [13][14][15][16][17]: 榜单/对照/闭源
Key data: PaddleOCR-VL-1.6 96.33 > MinerU2.5-Pro 95.69 > Unlimited OCR 93.92（OmniDocBench v1.6，多为厂商自报）；Mistral OCR 4 olmOCR-Bench 85.20/OmniDoc 93.07/$4·$2 页；Textract 表格+表单 $65/1000 页。Key insight: 开源近-SOTA 已在文档解析榜单反超或逼近闭源 API，而闭源结构化提取贵 7–15×——Olares 本地自托管的省钱+隐私叙事成立。Useful for: "X alternative"、"self-hosted OCR"、成本对比段落。

## Gaps

- OmniDocBench/olmOCR-Bench 分数多为厂商自报（CodeSOTA 明确标注 vendor/self-reported、未独立复现）；相反主张候选：AllenAI 官方 olmOCR-Bench 榜"仍封顶在 ~83"，与部分第三方自报 85–87 冲突，跨报告引用需以官方榜为准。[13][18]
- DeepSeek-OCR 未在 OmniDocBench 给出单一综合分（论文以"超越 X 所用 tokens"表述），与 PaddleOCR 的百分制不可直接同表比较。[2][13]
- 各模型 VRAM 数字来自模型卡/教程，随分辨率档位与 batch 变化，非固定阈值。[1]

## END
