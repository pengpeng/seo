# 开源 OCR / 文档理解（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 18 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 67%

## 摘要

到 2026 年，开源 OCR / 文档解析已经从"识字"跨到"读懂版面"：主流是端到端的**视觉语言模型（VLM）**，一次前向就同时完成版面检测、表格/公式/图表识别与阅读顺序还原，输出 Markdown/JSON。最重要的趋势是**"小模型反超"**——公开榜单头部被 sub-1.3B 的开源模型占据：PaddleOCR-VL-1.6（0.9B）以 OmniDocBench v1.6 **96.33%** 居首 [3][4]，dots.ocr（1.7B）以极小体量拿到多语 SOTA [7]，Granite-Docling 仅 **258M** 就能做保结构文档转换 [11][12]。这些模型全部开源、可本地部署，许可以 Apache 2.0 / MIT 为主，恰好落在闭源 API（Mistral OCR 4、AWS Textract、Google Document AI、Azure）价格上方——闭源做结构化提取贵 7–15× [16]，为 Olares"本地推理 + 数据不出户 + 零 per-page 费用"提供了清晰的替代叙事。本文按部署层级（📱 边缘 / 💻 本地主力 / 🏢 大 VLM）梳理型号级选型，并给出低竞争 SEO 关键词切入。

## 1. 型号总表（核心交付）

| 模型 | 代表型号/参数量 | 部署层级 | 许可 | 闭源对标 | 候选关键词 |
|------|----------------|----------|------|----------|-----------|
| **PaddleOCR-VL** | PaddleOCR-VL-1.6 / **0.9B**（ERNIE-4.5-0.3B）[3][4] | 💻 本地主力 | Apache 2.0 | Google Document AI / Mistral OCR 4 | `paddleocr vl`, `best open source document parsing 2026`, `run paddleocr-vl locally` |
| **DeepSeek-OCR** | 3B MoE / **~570M 激活**（+DeepEncoder ~380M）[1][2] | 💻 本地主力 | MIT | AWS Textract | `deepseek-ocr`, `run deepseek ocr locally`, `deepseek ocr vs textract` |
| **dots.ocr / dots.mocr** | **1.7B** LLM [7][8] | 💻 本地主力 | MIT | Google Document AI | `dots.ocr`, `dots.ocr self hosted`, `multilingual document parsing open source` |
| **olmOCR** | olmOCR-2-7B / **7B**（Qwen2.5-VL-7B 微调）[5][6][18] | 🏢 大 VLM | Apache 2.0 | Mistral OCR / GPT-4o OCR | `olmocr`, `pdf to markdown open source`, `gpt-4o ocr alternative` |
| **GOT-OCR2.0** | **~580M**（Qwen-0.5B 解码器）[9][10] | 📱 边缘 / 💻 | Apache 2.0 | AWS Textract 基础层 | `got-ocr`, `got ocr local`, `low vram ocr model` |
| **Granite-Docling** | granite-docling-258M / **258M**（Idefics3）[11][12] | 📱 边缘/CPU | Apache 2.0 | Azure Document Intelligence | `granite-docling`, `lightweight ocr model cpu`, `docling ocr` |
| **MinerU** | MinerU2.5-Pro（OpenDataLab）[13] | 💻 本地主力 | Apache 2.0 | Google Document AI | `mineru`, `pdf extraction open source` |
| **Baidu Unlimited OCR** | Unlimited OCR（开放权重）[13][17] | 💻 本地主力 | MIT | Mistral OCR 4 | `unlimited ocr`, `40 page ocr one shot` |
| **Surya OCR 2** | Surya 2 / **650M**（Datalab）[13] | 📱/💻 | 开源（查模型卡）| AWS Textract 基础层 | `surya ocr`, `surya 2 vs paddleocr` |
| **Qwen2.5-VL** | Qwen2.5-VL-7B（通用 VLM 兼做 OCR）[15] | 🏢 大 VLM | Apache 2.0 | GPT-4o / Gemini | `qwen2.5-vl ocr`, `vlm document understanding local` |

> 参数量为总参（DeepSeek-OCR 为 MoE，实际激活 ~570M）；榜单分数多为厂商自报，跨模型直接比较需自建私有集复核（见"局限性"）。

## 2. 分层解读（轻量 OCR vs 文档 VLM）

**📱 边缘 / CPU 友好（≤650M）——真正能在轻设备跑的一层。**
Granite-Docling-258M 是这一层最"新 SOTA"的代表：IBM 用 Idefics3 架构（siglip2-base 视觉编码器 + Granite 165M LLM），258M 就能保留版面、表格、公式，并输出 DocTags（利于 RAG 溯源，而非直接压成 Markdown 丢失结构）；IBM 明确后续 512M/900M 版本仍保持 <1B [11][12]。GOT-OCR2.0（~580M，Qwen-0.5B 解码器）走"OCR-2.0 统一端到端"路线，1024×1024 压到 256 image tokens，**4GB 显存消费级 GPU 即可部署**，社区还提供 CPU 版镜像 [9][10][14]。Surya OCR 2（650M）olmOCR-Bench ~83，"随处可跑" [13]。这一层是 Olares One 之外"在已有轻设备/NAS 上装 Olares 跑本地 OCR"的最佳落点。

**💻 本地主力（0.9B–3B）——精度/体量/多语的甜点区。**
PaddleOCR-VL-1.6（0.9B）是目前公开综合分最高者：OmniDocBench v1.6 96.33%、109 语言、公式/表格/图表/印章全覆盖、结构化 Markdown+JSON，且 1.6 与 1.5 架构兼容可零成本迁移；边缘场景另有 PP-OCRv5 mobile/server 双档 [3][4]。DeepSeek-OCR（3B MoE，~570M 激活，MIT）主打"光学上下文压缩"——10× 压缩下 ~97% 精度，OmniDocBench 上用 100 vision tokens 就超过 GOT-OCR2.0，单卡 A100 日产 20 万+ 页，bf16 权重 ~6.7GB、8–12GB 显存可跑标准档 [1][2]。dots.ocr（1.7B，MIT，100+ 语）把版面检测与内容识别统一进单模型，2026-03 更名 dots.mocr 并新增"图表转 SVG" [7][8]。MinerU2.5-Pro、Baidu Unlimited OCR（可一次解析 40+ 页）同处此层 [13][17]。

**🏢 大 VLM（7B+）——乱版/手写/最高鲁棒性。**
olmOCR（Allen AI，7B，基于 Qwen2.5-VL-7B 微调，Apache 2.0）定位"把 PDF 变 LLM 训练语料"的大规模批处理管线：olmOCR-Bench overall 82.3，百万页转换仅 ~176 美元（对比 GPT-4o >6240 美元/百万页），默认 FP8 + vLLM [5][6][18]。通用 Qwen2.5-VL 类模型也常被直接当 OCR 用于乱版/手写，但算力更高、数值需自验证 [15]。

**闭源对标（不可自托管，用作定价/精度参照）。**
Mistral OCR 4（2026-06-23，`mistral-ocr-latest`）olmOCR-Bench 85.20、OmniDocBench 93.07、170 语言、带 bounding box + 块分类 + 逐词置信度，$4/1000 页（batch $2）[16][17]；AWS Textract 基础 $1.50，但开启表格+表单达 $65/1000 页；Google Document AI $1.50–$30；Azure Document Intelligence Read ~$1.50、预置模型 ~$10 [16]。结论：**开源近-SOTA 在文档解析榜单已反超或逼近这些闭源 API，而闭源结构化提取贵 7–15×**——这是 Olares 本地方案最硬的省钱+隐私论据。

## 3. 候选 SEO 关键词与内容切入

- **型号词（低竞争、意图明确）**：`deepseek-ocr`、`paddleocr vl` / `paddleocr-vl 1.6`、`dots.ocr` / `dots.mocr`、`olmocr` / `olmocr 2`、`got-ocr`、`granite-docling`、`mineru ocr`、`unlimited ocr`、`surya ocr 2`。新模型词竞争度普遍低，抢发/GEO 价值高。
- **任务词（中长尾，转化好）**：`self-hosted OCR`、`open source document parsing`、`run OCR locally` / `local OCR model`、`pdf to markdown open source`、`on-premise document extraction`、`multilingual OCR self hosted`。
- **X alternative（借闭源流量，低竞争）**：`aws textract alternative open source`、`google document ai alternative`、`mistral ocr alternative`、`azure document intelligence alternative`、`gpt-4o ocr alternative`（olmOCR 成本叙事直接命中）。
- **对比词（X vs Y）**：`paddleocr-vl vs dots.ocr`、`deepseek-ocr vs paddleocr`、`olmocr vs mistral ocr`、`got-ocr vs granite-docling`。
- **Olares 落地切入**：以"在 Olares 上本地跑 X（数据不出户、零 per-page 费用）"为模板，把上面型号词 × 任务词交叉，优先写 `run deepseek-ocr / paddleocr-vl / olmocr locally` 与 `open source AWS Textract alternative` 两类。

## 关键发现（2-3）

1. **小模型反超闭源**：0.9B 的 PaddleOCR-VL-1.6（96.33% OmniDocBench v1.6）与 258M 的 Granite-Docling 证明"近-SOTA 文档解析已可在本地小设备跑"，Olares 的本地推理叙事不再需要牺牲精度 [3][11]。
2. **成本差是最强卖点**：闭源结构化提取（Textract 表格+表单 $65/1000 页）比开源本地方案贵 7–15×，olmOCR 百万页 $176 vs GPT-4o $6240 的对比极具传播力 [6][16]。
3. **许可干净、可商用**：头部开源模型集中在 Apache 2.0 / MIT（PaddleOCR、olmOCR、GOT-OCR、Granite-Docling 为 Apache；DeepSeek-OCR、dots.ocr、Unlimited OCR 为 MIT），几乎无商用限制，适合直接进 Olares 应用生态 [1][3][7][11]。

## 局限性

- **榜单分数多为厂商自报**：CodeSOTA 明确标注 PaddleOCR-VL/MinerU 的 OmniDocBench 分为 vendor/self-reported、未独立复现；且存在相反主张——AllenAI 官方 olmOCR-Bench 榜"仍封顶 ~83"，与部分第三方自报 85–87 冲突。跨模型比较务必以官方榜为准并自建私有集复核 [13][18]。
- **不可同表直比**：DeepSeek-OCR 论文以"超越 X 所用 tokens"表述、未给单一综合百分分，与 PaddleOCR 的百分制不可直接同表 [2]。
- **VRAM/CPU 数字非固定**：模型卡/教程给的显存门槛随分辨率档位、batch 与实现（FP8/bf16）变化；DeepSeek-OCR 官方不支持 Apple Silicon、需 NVIDIA CUDA + FlashAttention，边缘/CPU 可跑但慢 [1]。Lightweight 模式仅 18 源，事实型数字引用前请回官网/模型卡复核。

## 参考文献

[1] DeepSeek-OCR 模型卡 — https://huggingface.co/deepseek-ai/DeepSeek-OCR
[2] DeepSeek-OCR: Contexts Optical Compression（arXiv 2510.18234）— https://arxiv.org/pdf/2510.18234
[3] PaddleOCR-VL-1.6 模型卡 — https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6
[4] PaddleOCR GitHub — https://github.com/PaddlePaddle/PaddleOCR
[5] olmocr GitHub — https://github.com/allenai/olmocr/
[6] olmOCR 论文 PDF — https://olmocr.allenai.org/papers/olmocr.pdf
[7] dots.ocr 模型卡 — https://huggingface.co/rednote-hilab/dots.ocr
[8] dots.ocr GitHub — https://github.com/rednote-hilab/dots.ocr
[9] GOT-OCR2.0 论文（arXiv 2409.01704）— https://arxiv.org/pdf/2409.01704v1
[10] GOT-OCR2.0 GitHub — https://github.com/Ucas-HaoranWei/GOT-OCR2.0/
[11] IBM Granite-Docling 公告 — https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion
[12] granite-docling-258M 模型卡 — https://huggingface.co/ibm-granite/granite-docling-258M
[13] CodeSOTA Best OCR Model 2026 — https://www.codesota.com/ocr
[14] Spheron Best Open-Source OCR/Doc VLMs 2026 — https://www.spheron.network/blog/best-open-source-ocr-vlm-self-host-gpu-cloud-2026/
[15] Unstract Best Open Source OCR Tools 2026 — https://unstract.com/blog/best-opensource-ocr-tools/
[16] Mistral OCR 4 vs Textract vs Document AI — https://rohitraj.tech/en/notes/mistral-ocr-4-vs-textract-google-document-ai-2026
[17] VentureBeat: Mistral launches OCR 4 — https://venturebeat.com/data/mistral-launches-ocr-4-turning-document-extraction-into-a-full-enterprise-ai-play
[18] LM Studio: olmOCR 2 — https://lmstudio.ai/models/olmocr2
