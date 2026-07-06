# MinerU 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：opendatalab/MinerU（GitHub），MinerU Open Source License（Apache 2.0 附加条款）

> **无独立官网**：MinerU 无专属品牌域名，SEO 主战场在 GitHub（opendatalab/MinerU）、HuggingFace 模型页、第三方教程/文档页。跳过 Phase 1 域名报告，直接从关键词层面做起。

---

## 模型理解（前置）

MinerU 是由上海人工智能实验室（OpenDataLab）开发的开源文档解析工具，将 PDF、DOCX、PPTX、XLSX 及图片转换为 Markdown 或 JSON，专为 LLM 预训练、RAG 管道和 Agent 工作流设计。2.5-Pro 版本（模型 `MinerU2.5-Pro-2604-1.2B`）于 2026 年 4 月随 v3.1.0 发布，采用 1.2B 参数 VLM，在 OmniDocBench v1.6 上达到 SOTA，同时支持图表解析、跨页表格合并、LaTeX 公式识别（109 语言 OCR），并新增 LangChain/Dify/FastGPT/MCP Server 原生集成。同月许可证从 AGPLv3 升级为基于 Apache 2.0 的自定义许可，大幅降低商业采用门槛。

| 项目 | 内容 |
|------|------|
| 一句话定位 | OCR/文档解析工具 — 将 PDF/Office 文档转结构化 Markdown/JSON，供 LLM·RAG·Agent 使用 |
| 许可证 | MinerU Open Source License（基于 Apache 2.0，MAU >1亿或月收入 >$2000 万需商业授权；一般自托管/企业内部用途免费）；**v3.1.0 前为 AGPLv3** |
| 主仓库 / 分发 | GitHub [opendatalab/MinerU](https://github.com/opendatalab/MinerU)（★73k+）；HuggingFace [opendatalab/MinerU2.5-Pro-2604-1.2B](https://huggingface.co/opendatalab/MinerU2.5-Pro-2604-1.2B)；pip `mineru` |
| 参数 / VRAM 可跑性 | 1.2B VLM（MinerU2.5-Pro-2604-1.2B）；vLLM 后端实测峰值 ~25GB VRAM；pipeline（传统 OCR）后端 **CPU 可运行**，无 GPU 亦可；hybrid 后端兼顾速度与质量；消费级 24GB GPU（如 Olares One 或 RTX 4090）**可运行 VLM 模式** |
| 变体 / 型号 | `MinerU2.5-Pro-2604-1.2B`（2026/04）、`MinerU2.5-Pro-2605-1.2B`（修订版，2026/05）；后端：`pipeline`、`hybrid-auto-engine`（默认）、`vlm-*`；v3.x（当前）、v3.0.0、v3.1.x |
| 闭源对标 | Google Document AI、Amazon Textract、Adobe PDF Extract API、Azure Document Intelligence、Mathpix（公式专项）、LlamaParse、Unstructured.io |
| Olares Market | 未独立上架；可通过 pip 安装，或经 LangChain/Dify/MCP Server 间接集成 Olares 工作流；pipeline 后端 CPU 模式可在无 GPU 环境运行 |
| 来源 | [GitHub README](https://github.com/opendatalab/MinerU)、[HuggingFace 模型卡](https://huggingface.co/opendatalab/MinerU2.5-Pro-2604-1.2B)、[arXiv 2604.04771](https://arxiv.org/abs/2604.04771)、[LICENSE.md](https://github.com/opendatalab/MinerU/blob/master/LICENSE.md) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

> **品牌名冲突警示**：`mineru`（月量 8100）在 Semrush 结果中 **绝大多数搜索来自《塞尔达传说：王国之泪》和《动物森友会》角色"Mineru"**（`mineru totk` 1900、`mineru amiibo` 1900、`mineru acnh` 720 等），与文档解析工具无关。真正属于工具的品牌词仅有 `mineru github`（390）、`mineru ocr`（110）、`mineru 2.5`（90）、`mineru api`（140）、`mineru mcp`（40）等。报告以下以**工具相关词**为口径。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| mineru github | 390 | 44 | $0 | 导航 |
| mineru 2.5 | 90 | 56 | $0 | 信息 |
| mineru api ⭐ | 140 | 21 | $5.96 | 信息/商业 |
| mineru ocr | 110 | 46 | $4.89 | 信息 |
| mineru mcp ⭐ | 40 | 2 | $0 | 信息 |
| mineru pdf | 30 | 31 | $5.32 | 信息 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| mineru vllm | 0* | — | — | 信息 |
| mineru langchain | 0* | — | — | 信息 |
| mineru dify | 0* | — | — | 信息 |
| mineru rag | 0* | — | — | 信息 |
| mineru mcp ⭐ | 40 | 2 | $0 | 信息 |

*近零量但语义高度契合，属 GEO 抢发候选。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| pdf data extraction | 390 | 49 | $7.75 | 信息 |
| pdf to markdown ⭐ | 1900 | 40 | $2.20 | 信息 |
| convert pdf to markdown | 480 | 43 | $2.93 | 信息 |
| ocr pdf python ⭐ | 50 | 29 | $0 | 信息 |
| extract text from pdf python ⭐ | 210 | 35 | $0 | 信息 |
| pdf text extraction python | 110 | 40 | $5.46 | 信息 |
| pdf ocr python ⭐ | 50 | 29 | $0 | 信息 |
| unstructured pdf parsing ⭐ | 40 | 20 | $0 | 信息 |
| open source ocr | 260 | 46 | $2.75 | 信息 |
| self hosted ocr ⭐ | 20 | 0 | $0 | 信息 |
| pdf rag ⭐ | 50 | 23 | $0 | 信息 |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| google document ai | 1900 | 35 | $10.51 | 信息/商业 |
| amazon textract | 1900 | 40 | $12.62 | 信息/商业 |
| azure document intelligence | 2400 | 62 | $10.48 | 信息/商业 |
| mathpix | 4400 | 49 | $0.09 | 信息/商业 |
| pymupdf | 3600 | 49 | $6.71 | 信息 |
| docling | 8100 | 36 | $3.84 | 信息 |
| llamaparse | 1600 | 33 | $12.79 | 信息/商业 |
| unstructured io | 720 | 43 | $7.63 | 信息/商业 |
| marker pdf ⭐ | 320 | 36 | $1.17 | 信息 |
| llmsherpa ⭐ | 140 | 33 | $0 | 信息 |
| docling python ⭐ | 140 | 23 | $0 | 信息 |
| document extraction ai | 110 | 50 | $6.45 | 商业 |
| google document ai alternative ⭐ | 20 | 0 | $0 | 商业 |
| open source document ai ⭐ | 20 | 0 | $0 | 信息/商业 |
| ai pdf parser | 40 | 56 | $94.24 | 商业 |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|-----|-----|-------------|--------|
| mineru mcp | 40 | 2 | $0 | MCP Server 模式可直接嵌入 Olares Agent 工作流，zero-config 接入 | ⭐⭐⭐ |
| mineru vllm | 0* | — | — | vLLM 已在 Olares Market，可一键部署后接 MinerU VLM 后端 | ⭐⭐⭐ |
| pdf rag | 50 | 23 | $0 | Olares 本地 RAG 管道：MinerU 解析→向量库→本地 LLM 全链路自托管 | ⭐⭐⭐ |
| self hosted ocr | 20 | 0 | $0 | Olares 隐私卖点：文档不离本机，0 云端数据暴露 | ⭐⭐⭐ |
| pdf to markdown | 1900 | 40 | $2.20 | pipeline 后端 CPU 可运行，Olares 无 GPU 机型亦可处理文档 | ⭐⭐ |
| open source document ai | 20 | 0 | $0 | "自建 Document AI 替代 Google/Amazon" 叙事，Olares 一键本地跑 | ⭐⭐⭐ |
| google document ai alternative | 20 | 0 | $0 | 主攻"按页计费/数据出境"痛点，MinerU + Olares = 0 费用 + 完全隐私 | ⭐⭐⭐ |
| unstructured pdf parsing | 40 | 20 | $0 | 对标 Unstructured.io（商业 SaaS），MinerU 本地部署无 API 调用费 | ⭐⭐ |
| docling python | 140 | 23 | $0 | Docling（IBM）对标：同为开源 PDF→Markdown，MinerU 公式+表格更强 | ⭐⭐ |
| marker pdf | 320 | 36 | $1.17 | Marker（另一开源竞品）对标词，流量可截取 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|-----|-----|------|------|--------------------------|
| pdf to markdown | 1900 | 40 | $2.20 | 信息 | 主词候选 | 最大流量入口；MinerU pipeline 模式 CPU 可跑，可做"best open source pdf to markdown" 文章锚词 |
| google document ai | 1900 | 35 | $10.51 | 信息/商业 | 主词候选 | 闭源对标；攻击面：按页计费 + 数据出境；"MinerU vs Google Document AI" 文章锚词 |
| amazon textract | 1900 | 40 | $12.62 | 信息/商业 | 主词候选 | 同上；企业 RAG 场景替代词 |
| convert pdf to markdown | 480 | 43 | $2.93 | 信息 | 次级 | 主词衍生；KD 偏高但无需独立文章，可并入 pdf-to-markdown 簇 |
| pdf data extraction | 390 | 49 | $7.75 | 信息 | 次级 | CPC 高，商业意图；KD 49 较难，需外链支撑 |
| mineru github | 390 | 44 | $0 | 导航 | 次级 | 纯导航词，Olares 内容用处有限，但说明工具知名度 |
| open source ocr | 260 | 46 | $2.75 | 信息 | 次级 | 宽泛品类词；MinerU 可作 OCR 方案入口 |
| marker pdf | 320 | 36 | $1.17 | 信息 | 次级 | Marker 是直接竞品（同为开源 PDF 解析）；"MinerU vs Marker" 对比词 ⭐ |
| llamaparse | 1600 | 33 | $12.79 | 信息/商业 | 主词候选 | KD 33 相对友好，CPC $12.79 说明商业意图强；"open source llamaparse alternative" 切入 |
| docling | 8100 | 36 | $3.84 | 信息 | 主词候选 | 搜索量与 MinerU 品牌词相当；IBM 开源，同赛道；"MinerU vs Docling" 对比文机会 KD 合理 ⭐ |
| extract text from pdf python | 210 | 35 | $0 | 信息 | 次级 | 开发者长尾；KD 35 可争，绑定代码示例 |
| mineru api | 140 | 21 | $5.96 | 信息/商业 | 次级 | KD 低，品牌词中最值得做内容的 ⭐ |
| mineru ocr | 110 | 46 | $4.89 | 信息 | 次级 | CPC 高但 KD 46，官方文档页自然排名 |
| mineru mcp | 40 | 2 | $0 | 信息 | GEO | KD 2，极低竞争；MCP Server 新特性，AI Overview 抢发机会 ⭐⭐⭐ |
| pdf rag | 50 | 23 | $0 | 信息 | GEO | 近零量但高增长语义场景；RAG 工作流 + Olares 全链路文章前哨 ⭐ |
| self hosted ocr | 20 | 0 | $0 | 信息 | GEO | 完全空白，Olares 隐私叙事最佳切入 ⭐ |
| google document ai alternative | 20 | 0 | $0 | 商业 | GEO | 零竞争替代词，虽量小但商业意图强，AI Overview 优先收录 ⭐ |
| open source document ai | 20 | 0 | $0 | 信息/商业 | GEO | 同上，概念词，语义锚点 ⭐ |
| mineru vllm | 0* | — | — | 信息 | GEO | 近零但强 Olares 部署词；vLLM 在 Olares Market 已上架，组合方案 ⭐⭐⭐ |
| mineru dify | 0* | — | — | 信息 | GEO | MinerU 官方支持 Dify 集成；Dify 亦可自托管，与 Olares 生态高度契合 ⭐⭐⭐ |

---

## 核心洞见

1. **搜索心智尚未独立建立——品牌词被游戏角色严重稀释**
   `mineru`（月量 8100）中约 90% 以上属于《塞尔达传说：王国之泪》角色 Mineru 及《动物森友会》相关内容（`mineru totk` 1900、`mineru amiibo` 1900 等），文档工具本身的品牌词（`mineru github` 390、`mineru ocr` 110、`mineru api` 140）相比之下极为稀少。**SEO 策略应以品类词（pdf to markdown、open source OCR）为主攻方向，而非依赖工具品牌名带流量**。

2. **消费级 GPU / Olares One 可跑性：YES（两种路径）**
   - **VLM 后端**（MinerU2.5-Pro-2604-1.2B）：峰值 ~25GB VRAM，需 RTX 4090/3090 或更高；Olares One（若含 24GB GPU）可运行，但为边际场景。
   - **pipeline 后端（传统 OCR）**：**CPU 可运行，无 GPU 亦可**，精度略低但可用；Olares 标准配置覆盖此路径，叙事成立。
   - **hybrid 后端（默认）**：自动选择最优模式，有 GPU 用 VLM、无 GPU 降级 pipeline，零配置开箱即用。

3. **许可证：Apache 2.0 基础 + 附加条款，中小企业/个人商用友好**
   v3.1.0 前为 AGPLv3（传染性强，云服务采用障碍大）；v3.1.0 后升级为自定义 Apache 2.0 附加条款：MAU <1亿 且月收入 <$2000万 的商用场景**无需单独商业授权**，仅需在产品界面注明使用了 MinerU。**对 Olares 生态内的个人/企业自托管场景，可作为主推卖点**；需在内容中准确标注"Apache 2.0-based custom license"而非直接写"Apache 2.0"。

4. **对 Olares 最关键的 2-3 个词**
   - `mineru mcp`（KD 2，月量 40）：MinerU 内置 MCP Server，可直接插入 Olares Agent 工作流——技术门槛最低的 Olares 切入点，GEO 前哨词。
   - `pdf rag`（KD 23，月量 50）：Olares 本地全链路 RAG（MinerU 解析 → 向量库 → 本地 LLM）是高价值产品故事，搜索量低但增速快，适合抢发 AI Overview 引用。
   - `open source document ai alternative`（量近零但商业意图强）：攻击 Google Document AI / Amazon Textract 的"按页计费 + 数据出境"痛点，Olares = 0 边际成本 + 100% 本地。

5. **GEO 抢发窗口**
   以下词目前 Semrush 量为 0 或极低，但语义契合度高、AI Overview 引用机会大：
   - `mineru vllm`、`mineru dify`、`mineru langchain`、`mineru rag`（均近零量）
   - `self hosted ocr`（KD 0，月量 20）
   - `google document ai alternative`（KD 0，月量 20）
   - `mineru mcp`（KD 2，月量 40）——当前最低竞争有量词
   建议在 MinerU 2.5-Pro 相关教程/对比文中植入这些词，抢占 Perplexity / AI Overview 引用位。

6. **闭源对标与攻击面**
   | 对标产品 | 月量 | 攻击面 |
   |----------|------|--------|
   | Google Document AI | 1900 | 按页计费（$65/1000页起），数据强制出境 Google Cloud |
   | Amazon Textract | 1900 | 同上，AWS 依赖，公式/多栏布局识别弱 |
   | Azure Document Intelligence | 2400 | 同上，月免费额度有限，复杂学术/科技文档准确率低于 MinerU |
   | Mathpix | 4400 | 专注公式，无 RAG 集成，月订阅制，MinerU 公式识别可达 Mathpix 同级 |
   | LlamaParse | 1600 | 基于 LlamaIndex，CPC $12.79 高商业价值，MinerU 完全免费且可离线 |
   | Unstructured.io | 720 | 商业 SaaS，开源版功能受限，MinerU 全功能开源且含 VLM 模式 |
   | Docling（IBM） | 8100 | 最直接的同赛道开源竞品；MinerU 在公式识别与多语言 OCR 上有优势 |

7. **与同类 family 关联**
   在 `directions/model/reports/08-ocr/` 已有 `paddleocr-vl.md`（PaddleOCR）。MinerU 与 PaddleOCR 的关系：MinerU 早期版本内部使用 PaddleOCR 作为 OCR 引擎，2.5-Pro 升级为自研 VLM 主导，但 pipeline 后端仍可调用 OCR 能力。两者在"open source OCR python"（`paddleocr` 2900）词池上有重叠，内容层可做横向对比文（MinerU 专注文档结构化 + LLM-ready 输出，PaddleOCR 侧重通用 OCR 引擎）。

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*品牌词"mineru"总月量 8100 中绝大多数属于游戏角色，文档工具相关词量显著低于名义值，请勿以 8100 作为工具品牌认知依据。*
