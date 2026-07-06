# PaddleOCR / PaddleOCR-VL 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：PaddlePaddle/PaddleOCR（github.com/PaddlePaddle/PaddleOCR），Apache 2.0

## 模型理解（前置）

PaddleOCR 是百度飞桨（PaddlePaddle）团队开发的开源 OCR 与文档解析工具包，已成为 RAG 基础设施领域事实上的 OCR 引擎，被 RAGFlow、Dify、MinerU、Cherry Studio 等主流开源项目直接集成。工具包核心包含两个产品线：**PP-OCR 系列**（轻量级 text detection/recognition，最新 PP-OCRv6 medium 仅 34.5M 参数，能 CPU 推理，支持 100+ 语言）；**PaddleOCR-VL 系列**（0.9B 多模态 VLM，专为文档版面理解设计，在 OCR-Bench v1 等评测中以 0.9B 参数量超越 Qwen3-VL-235B 和 GPT-5.5）。两者均以 Apache 2.0 授权，可商用、可本地自托管。

| 项目 | 内容 |
|------|------|
| 一句话定位 | OCR 文档解析工具包（生产级 text OCR + VLM 文档理解），RAG 管线首选前处理引擎 |
| 许可证 | **Apache 2.0**——完全商用友好，可作为 Olares 主推卖点 |
| 主仓库 / 分发 | [GitHub PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)（★84.7K，2026-07）；HuggingFace [PaddlePaddle/PaddleOCR-VL](https://huggingface.co/PaddlePaddle/PaddleOCR-VL)；PyPI `paddleocr`；官方文档 paddleocr.ai |
| 参数 / VRAM 可跑性 | **PP-OCRv6 tiny（1.5M）/ medium（34.5M）**：CPU 可跑，无 VRAM 要求；**PaddleOCR-VL-1.6（0.9B VLM）**：FP16 ~2 GB VRAM、INT8 ~1 GB，需要 NVIDIA CC≥8（RTX 3060+）运行 vLLM/SGLang；RTX 5090 Mobile（24 GB）上可大批量并行。Olares One 完全胜任 |
| 变体 / 型号 | PP-OCRv5（多场景中文/英文/日文/手写）、PP-OCRv6（v3.7.0，50语言单模型，+4.6% 检测）、PaddleOCR-VL-1.5、PaddleOCR-VL-1.6、PP-StructureV3（表格/图表/版式）、PP-ChatOCRv4（关键信息提取） |
| 闭源对标 | **AWS Textract**（按页计费）、**Google Document AI**（API 付费）、**Azure Form Recognizer / Document Intelligence**（订阅制）、**Adobe Acrobat AI**（月费）；同类开源竞品：EasyOCR、TrOCR、Surya OCR、RapidOCR、Docling |
| Olares Market | PP-OCR/VL 尚无独立 Olares Market app；通常在 RAGFlow / Dify（Olares Market 已上架）内作为内置 OCR 引擎运行，也可直接 `pip install paddleocr` 在 Olares 容器内自行集成 |
| 来源 | [GitHub README](https://github.com/PaddlePaddle/PaddleOCR)（2026-07）；[Releases v3.7.0](https://github.com/PaddlePaddle/PaddleOCR/releases)；[PaddleOCR 3.0 Technical Report](https://arxiv.org/html/2507.05595v1)；[PaddleOCR-VL VRAM 数据](https://www.spheron.network/blog/best-open-source-ocr-vlm-self-host-gpu-cloud-2026/)；[Towards AI PaddleOCR-VL-1.5 深度评测](https://pub.towardsai.net/paddleocr-vl-1-5-a-deep-dive-into-the-0-9b-model-that-outperforms-gpt-4o-on-document-parsing-c93bac97ac1f) |

---

## 流量基线（Phase 1）

官方文档站 `paddleocr.ai` US 月流量极低（Semrush：1 次/月，71 个关键词），SEO 主战场在 GitHub、PyPI、HuggingFace 及社区内容页，而非厂商官站。以下仅记录官站基线，实际搜索量反映在关键词层。

| 指标 | 数据 |
|------|------|
| 域名 | paddleocr.ai |
| SEMrush Rank | 12,201,641（US，极低） |
| 月自然流量（US） | ~1 |
| 关键词数 | 71 |
| 流量估值 | $3/月 |

> **洞见**：官方文档站美国流量几乎为零，说明 PaddleOCR 的美国用户以 GitHub / PyPI / 搜索内容页直达为主。品牌词流量存在但分散在 GitHub、Stack Overflow、Towards AI 等第三方内容源，无法从官站单点捕获。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 品牌 / 型号词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| paddleocr | 2,900 | 42 | $4.17 | 信息 |
| paddle ocr | 1,900 | 41 | $4.17 | 信息 |
| paddleocr-vl | 1,000 | 42 | $4.36 | 信息 |
| paddlepaddle | 1,900 | 58 | $2.00 | 导航 |
| paddleocr vl | 210 | 55 | $4.36 | 信息 |
| paddleocr github | 140 | 34 | $0 | 导航 |
| paddleocr license | 140 | 26 | $0 | 信息 ⭐ |
| pip install paddleocr | 110 | 35 | $0 | 信息/交易 |
| paddleocr-vl-1.5 | 110 | 0 | $3.08 | 信息 ⭐ |
| ppocr | 90 | 24 | $0 | 导航 ⭐ |
| paddleocr-vl-1.5 | 90 | 0 | $4.13 | 信息 ⭐ |
| paddleocr demo | 70 | 28 | $4.78 | 信息 ⭐ |
| paddleocr online | 70 | 13 | $3.84 | 信息/交易 ⭐ |
| paddleocr pp-ocrv5 | 30 | 0 | $0 | 信息 ⭐ |
| paddleocr mcp server | 30 | 0 | $0 | 信息 ⭐ |
| paddleocr architecture | 50 | 0 | $0 | 信息 ⭐ |
| paddleocr multilingual | 40 | 0 | $0 | 信息 ⭐ |
| paddleocr ppstructure | 40 | 18 | $0 | 导航 ⭐ |
| paddleocr handwritten | 40 | 0 | $0 | 信息 ⭐ |
| baidu paddleocr | 30 | 0 | $0 | 导航 ⭐ |

### 引擎组合词（Olares 机会前哨）

> PaddleOCR 以 Python 库形式直接使用，无需额外推理引擎（PP-OCR 系列）；PaddleOCR-VL 才需要 vLLM/SGLang。"引擎词"此处扩展为与 RAG 工具链的组合。

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| paddleocr ollama | 10 | 0 | $0 | 信息 ⭐ |
| paddleocr api | 20 | 0 | $5.90 | 信息 ⭐ |
| paddleocr docker | 20 | 0 | $0 | 信息 ⭐ |
| docling paddleocr | 40 | 19 | $0 | 信息 ⭐ |
| paddleocr rag | 20 | 0 | $0 | 信息 ⭐ |
| ocr rag | 20 | 0 | $0 | 信息 ⭐ |
| paddleocr mcp server | 30 | 0 | $0 | 信息 ⭐ |

### 本地部署 / 隐私词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| local ocr | 30 | 0 | $7.54 | 信息 ⭐ |
| self hosted ocr | 20 | 0 | $0 | 信息 ⭐ |
| on premise ocr | 50 | 39 | $11.95 | 信息/商业 |
| paddleocr install | 20 | 0 | $0 | 信息 ⭐ |
| open source invoice ocr | 20 | 0 | $0 | 信息 ⭐ |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| paddleocr vs tesseract | 110 | 27 | $0 | 信息 ⭐ |
| rapidocr vs paddleocr | 70 | 0 | $0 | 信息 ⭐ |
| trocr vs paddleocr | 50 | 27 | $0 | 信息 ⭐ |
| docling vs paddleocr | 30 | 0 | $0 | 信息 ⭐ |
| easyocr vs paddleocr | 20 | 0 | $0 | 信息 ⭐ |
| tesseract alternative | 40 | 19 | $0 | 信息 ⭐ |
| aws textract alternative | 10 | 0 | $6.67 | 信息 ⭐ |
| mistral ocr alternative | 20 | 0 | $5.55 | 信息 ⭐ |
| google document ai alternative | 20 | 0 | $0 | 信息 ⭐ |
| open source ocr | 260 | 46 | $2.75 | 信息 |
| ocr open source | 110 | 27 | $2.75 | 信息 ⭐ |
| best ocr software | 590 | 38 | $5.01 | 商业 ⭐ |

### 文档处理 / RAG 场景词（Olares 核心场景）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| invoice ocr | 590 | 36 | $21.54 | 信息/商业 ⭐ |
| document digitization | 720 | 32 | $9.77 | 信息 ⭐ |
| receipt ocr | 210 | 26 | $8.23 | 信息 ⭐ |
| document understanding | 170 | 28 | $5.40 | 信息 ⭐ |
| document ocr | 210 | 81 | $4.73 | 信息 |
| surya ocr | 210 | 29 | $5.87 | 信息 ⭐ |
| marker pdf | 320 | 36 | $1.17 | 信息 ⭐ |
| docling | 8,100 | 36 | $3.84 | 信息 ⭐ |
| easyocr | 1,600 | 27 | $2.94 | 信息 ⭐ |
| mistral ocr | 1,900 | 39 | $5.26 | 信息 |
| pdf text extraction python | 110 | 40 | $5.46 | 信息 |

### 竞品（闭源）词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| aws textract | 2,900 | 34 | $11.85 | 导航 ⭐ |
| google document ai | 1,900 | 35 | $10.51 | 导航 ⭐ |
| document ai | 1,600 | 73 | $4.22 | 导航 |
| document intelligence | 1,000 | 46 | $6.60 | 信息 |
| aws textract pricing | 720 | 32 | $5.66 | 商业 ⭐ |
| ocr api | 390 | 48 | $4.49 | 信息 |
| azure form recognizer | 390 | 50 | $8.57 | 信息 |
| adobe acrobat ai | 480 | 50 | $1.69 | 导航 |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|-------|
| paddleocr vs tesseract | 110 | 27 | $0 | PaddleOCR 在中文/多语言/版面识别全面领先 Tesseract；Olares 可一键部署，无需配置语言包 | ⭐⭐⭐ |
| invoice ocr | 590 | 36 | $21.54 | 发票/收据本地识别，文档不出设备；对比 AWS Textract 无需按页付费 | ⭐⭐⭐ |
| document digitization | 720 | 32 | $9.77 | Olares + PaddleOCR 搭建私有文档数字化管线，银行级隐私 | ⭐⭐⭐ |
| aws textract | 2,900 | 34 | $11.85 | "AWS Textract 按页计费，PaddleOCR 在 Olares 本地运行零 API 费用" | ⭐⭐⭐ |
| aws textract pricing | 720 | 32 | $5.66 | 用 Textract 定价计算器反向说明本地部署的 TCO 优势 | ⭐⭐⭐ |
| receipt ocr | 210 | 26 | $8.23 | 本地收据识别，隐私敏感场景不上云 | ⭐⭐⭐ |
| google document ai | 1,900 | 35 | $10.51 | Google Document AI 每页计费且数据上云；PaddleOCR 本地推理同等能力 | ⭐⭐⭐ |
| document understanding | 170 | 28 | $5.40 | PaddleOCR-VL 在 Olares 本地跑文档理解，支持表格/图表/公式 | ⭐⭐⭐ |
| self hosted ocr | 20 | 0 | $0 | 精准匹配：Olares = self-hosted personal cloud，PaddleOCR = self-hosted OCR engine | ⭐⭐⭐ |
| local ocr | 30 | 0 | $7.54 | Olares 是"在家里跑的 local OCR 工厂" | ⭐⭐⭐ |
| open source invoice ocr | 20 | 0 | $0 | GEO 长尾，精准捕获财务场景开源需求 | ⭐⭐⭐ |
| ocr rag | 20 | 0 | $0 | PaddleOCR → chunking → 向量库 → LLM 全链路均可在 Olares 本地完成 | ⭐⭐⭐ |
| paddleocr mcp server | 30 | 0 | $0 | MCP 是 2025-2026 最热的 Agent 工具协议；PaddleOCR + Olares 作为本地 OCR MCP 服务器，文档 Agent 天然场景 | ⭐⭐⭐ |
| paddleocr rag | 20 | 0 | $0 | 直接对应 Olares 文档 RAG 场景（Olares = 本地 RAG 最佳运行平台） | ⭐⭐⭐ |
| docling | 8,100 | 36 | $3.84 | Docling vs PaddleOCR 是热门对比词；Olares 可以同时本地跑两个，做评测场景 | ⭐⭐ |
| easyocr | 1,600 | 27 | $2.94 | EasyOCR 是 PaddleOCR 最大 OSS 竞品；用 Olares 对比部署性能，"哪个更适合本地部署" | ⭐⭐ |
| paddleocr-vl-1.5 | 110 | 0 | $3.08 | 新模型词，GEO 抢发；Olares One RTX 5090 24GB 轻松跑全精度 | ⭐⭐ |
| aws textract alternative | 10 | 0 | $6.67 | GEO 精准词，量小但 CPC $6.67 说明商业意图强 | ⭐⭐ |
| on premise ocr | 50 | 39 | $11.95 | 企业级需求，Olares SMB 角度：机房/内网部署文档识别 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|-----|------|------|--------------------------|
| paddleocr | 2,900 | 42 | $4.17 | 信息 | 主词候选 | 核心品牌词，量足 KD 中等，SEO 可攻；Olares 角度：本地跑 PaddleOCR 文档管线 |
| aws textract | 2,900 | 34 | $11.85 | 导航 | 主词候选 | 闭源竞品品牌词 KD 仅 34，量大；写"open source aws textract alternative"文章入口 |
| paddle ocr | 1,900 | 41 | $4.17 | 信息 | 次级 | 品牌变体，配合 paddleocr 一起写 |
| google document ai | 1,900 | 35 | $10.51 | 导航 | 主词候选 | 闭源竞品 KD 35，攻"google document ai alternative"方向 |
| paddleocr-vl | 1,000 | 42 | $4.36 | 信息 | 次级 | VLM 产品词，用于"document understanding with PaddleOCR-VL"类内容 |
| document ai | 1,600 | 73 | $4.22 | 导航 | — | KD 73，不适合直接攻 |
| document digitization | 720 | 32 | $9.77 | 信息 | 主词候选 | KD 低、量不小、CPC 高说明商业价值；Olares 私有文档数字化管线 |
| aws textract pricing | 720 | 32 | $5.66 | 商业 | 主词候选 | 商业意图词 KD 仅 32；写 TCO 对比文章，引导"free with local OCR" |
| invoice ocr | 590 | 36 | $21.54 | 信息/商业 | 主词候选 | CPC $21，高商业价值；Olares 私有发票处理，文档不出设备 ⭐ |
| best ocr software | 590 | 38 | $5.01 | 商业 | 主词候选 | 综述类意图，适合"best open source OCR 2026"型文章 ⭐ |
| paddleocr vs tesseract | 110 | 27 | $0 | 信息 | 次级 | 直接对比词，KD 低，写对比文价值高 ⭐ |
| open source ocr | 260 | 46 | $2.75 | 信息 | 次级 | KD 中，配合"best open source OCR"作次级 |
| receipt ocr | 210 | 26 | $8.23 | 信息 | 主词候选 | KD 低 CPC 高，隐私场景天然契合 Olares ⭐ |
| document understanding | 170 | 28 | $5.40 | 信息 | 次级 | KD 28，可作 PaddleOCR-VL 主题文章的次级词 ⭐ |
| paddleocr-vl-1.5 | 110 | 0 | $3.08 | 信息 | GEO | 新版本词 KD=0，GEO 抢发窗口；Olares One 完整跑 VLM |
| easyocr | 1,600 | 27 | $2.94 | 信息 | 次级 | 开源竞品词，适合"paddleocr vs easyocr"型内容；作主词需独立 report |
| docling | 8,100 | 36 | $3.84 | 信息 | 次级 | 热度最高的开源文档工具词；"docling vs paddleocr"入场对比 ⭐ |
| ocr open source | 110 | 27 | $2.75 | 信息 | 次级 | 近义词，配合"open source ocr"集群 ⭐ |
| self hosted ocr | 20 | 0 | $0 | 信息 | GEO | 精准 Olares 场景词，量小但极度契合，GEO ⭐ |
| local ocr | 30 | 0 | $7.54 | 信息 | GEO | CPC $7.54 说明商业意图；GEO 布局，搜索量将增长 ⭐ |
| paddleocr mcp server | 30 | 0 | $0 | 信息 | GEO | MCP 生态新词，AI Agent 时代 OCR 接入工具；Olares = 本地 MCP server 宿主 ⭐ |
| ocr rag | 20 | 0 | $0 | 信息 | GEO | RAG 前处理场景，Olares 一站式 RAG 基础设施 ⭐ |
| aws textract alternative | 10 | 0 | $6.67 | 信息 | GEO | CPC $6.67，高意图词，GEO 布局后随量增长价值提升 ⭐ |
| open source invoice ocr | 20 | 0 | $0 | 信息 | GEO | 场景级精准长尾 ⭐ |

---

## 核心洞见

### 1. 搜索心智建立了吗？

PaddleOCR 品牌词有实质量：`paddleocr`（2,900/月）+ `paddle ocr`（1,900）+ `paddleocr-vl`（1,000），合计约 5,800，搜索心智**已建立**。但 US 官方文档站（paddleocr.ai）几乎零流量，说明用户心智更多通过 GitHub、PyPI、社区博客到达，而非官方站直达。好处是：**第三方内容（包括 Olares 博客）可以直接截获这批流量**，不需要和官方站竞争。

### 2. 能否在消费级 GPU / Olares One 本地跑？（叙事前提）✅

- **PP-OCR 系列（tiny/medium/server）**：完全可在 CPU 上跑，无 VRAM 要求——覆盖所有 Olares 安装平台（x86 Linux/ARM/macOS/Windows WSL2）。
- **PaddleOCR-VL-1.6（0.9B VLM）**：FP16 仅 ~2 GB VRAM，INT8 仅 ~1 GB。需要 NVIDIA CC≥8（RTX 3060+）。**Olares One 的 RTX 5090 Mobile（24 GB）**完全可大批量并行推理，远超最低要求。叙事成立度极高。
- 注意：PaddleOCR-VL 官方文档注明"不支持 ARM 和 CPU 推理"（VLM 组件），ARM 用户只能用 PP-OCR 系列。

### 3. 许可证是否商用友好？✅ 主推卖点

Apache 2.0，商用免费、可修改分发、可集成商业产品。远优于：
- Tesseract（Apache 2.0 但维护停滞）
- EasyOCR（Apache 2.0 但速度/精度差距大）
- 众多闭源竞品（AWS Textract/Google Document AI 按页计费）

**可作为最强卖点直接写进文案**："Apache 2.0，零授权费，在 Olares 上本地跑，彻底告别 AWS Textract 按页账单。"

### 4. 对 Olares 最关键的 2-3 个词

1. **`aws textract`（2,900/月，KD 34）**：闭源竞品品牌词但 KD 仅 34，切入点是 "PaddleOCR as free AWS Textract alternative on Olares"——直接攻击计费痛点。
2. **`invoice ocr`（590/月，KD 36，CPC $21.54）**：具体场景词，CPC 高说明用户有付费意愿；本地跑 PaddleOCR 处理发票，数据不出设备，替代高价 API。
3. **`document digitization`（720/月，KD 32）**：宽泛场景词，KD 低；Olares + PaddleOCR 构建私有文档数字化平台，对企业/SMB 有明显价值。

### 5. 新模型 GEO 抢发窗口

以下词当前 US 量接近零但语义高度契合，是 GEO（AI Overview / Perplexity / ChatGPT 搜索引用）的最佳机会：

- `paddleocr mcp server`（30/月，KD 0）——MCP 是 2025-2026 最热的 Agent 协议；Olares 作为本地 MCP 宿主，PaddleOCR 作为 OCR MCP tool，内容抢发价值极高
- `ocr rag`（20/月，KD 0）、`paddleocr rag`（20/月，KD 0）——RAG 内容每天在 AI Overview 中被引用，量会快速增长
- `self hosted ocr`（20/月，KD 0，CPC $7.54）——CPC 说明高商业意图，随隐私法规收紧量将上升
- `aws textract alternative`（10/月，KD 0，CPC $6.67）——极高商业意图，量小但 LTV 高
- `open source invoice ocr`（20/月，KD 0）——场景精准，GEO 布局

### 6. 闭源对标与攻击面

| 闭源对手 | 月量 | KD | 主要攻击面 |
|---------|------|----|-----------|
| AWS Textract | 2,900 | 34 | 按页计费（$1.5/千页起），发票/表格识别按用量叠加；PaddleOCR 本地零 API 费 |
| Google Document AI | 1,900 | 35 | 数据上 Google 服务器，GDPR 合规压力；本地部署规避 |
| Azure Form Recognizer | 390 | 50 | 月费 + 额度制，SMB 超量费用高；本地无限制处理 |
| Adobe Acrobat AI | 480 | 50 | 月订阅 $29.99+，按座位收费；Olares 上 PaddleOCR 一次部署全团队用 |

**通用攻击文案**："\$0 per page. Documents never leave your machine. PaddleOCR on Olares vs. cloud OCR."

### 7. 与同类 family 及关键词关联

- 与 [Whisper（STT）](../06-stt/whisper.md) 同为"媒体/文档输入前处理"链路，可联合叙事为"Olares 本地 AI 数据工厂"（语音→文字/图像文档→结构化数据）
- 与 [BGE-M3（Embedding）](../07-embedding/bge-m3.md) 构成完整 RAG 前处理链：PaddleOCR 解析 → BGE-M3 向量化 → 本地 LLM 推理，全程 Olares 本地
- `docling`（8,100/月，KD 36）是当前最热的文档处理词，可写"docling vs paddleocr for RAG"对比文，借 docling 流量引流 Olares + PaddleOCR 方案
- `easyocr`（1,600/月，KD 27）是 Olares 市场侧报告潜在方向（可查 market/apps.md 是否已收录 EasyOCR 相关 app）

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch、phrase_related、phrase_questions、domain_rank）| 2026-07-06*
*技术事实来源：[GitHub PaddlePaddle/PaddleOCR v3.7.0](https://github.com/PaddlePaddle/PaddleOCR)（2026-06-11）；[PaddleOCR 3.0 Technical Report arXiv:2507.05595](https://arxiv.org/html/2507.05595v1)；[Spheron 2026 OCR VLM 对比](https://www.spheron.network/blog/best-open-source-ocr-vlm-self-host-gpu-cloud-2026/)；[Towards AI PaddleOCR-VL-1.5 评测](https://pub.towardsai.net/paddleocr-vl-1-5-a-deep-dive-into-the-0-9b-model-that-outperforms-gpt-4o-on-document-parsing-c93bac97ac1f)*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
