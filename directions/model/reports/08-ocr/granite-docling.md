# Granite-Docling 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：ibm-granite/granite-docling-258M（huggingface.co），Apache 2.0
>
> ⚠️ 无独立官网，SEO 主战场在 HuggingFace、GitHub（docling-project/docling ★62K）及 IBM 文档页；Phase 1 域名报告跳过。

## 模型理解（前置）

Granite-Docling-258M 是 IBM Research 出品的超轻量视觉-语言模型（VLM），专为端到端文档转换设计：一次推理即可完成 OCR 识别、版面分析、表格结构解析、数学公式提取，输出专属的 DocTags 标记语言（结构保留优于直出 Markdown），是构建 RAG 管线时的文档前处理首选方案之一。它是 SmolDocling-256M-preview（IBM Research × HuggingFace，2025 年 3 月）的产品化升级——语言骨干换成 Granite 165M、视觉编码器升级为 SigLIP2，性能全面超越前身。整个 Docling 生态（docling-project/docling，MIT 许可，62K GitHub stars）由 LF AI & Data Foundation 托管，已成为开源 RAG 管线的事实标准前处理工具。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 258M 超轻量 VLM，端到端文档解析（OCR+版面+表格+公式），输出 DocTags，是 RAG 管线的结构化文档前处理引擎 |
| 许可证 | **Apache 2.0**——完全商用友好，可作为 Olares 主推卖点 |
| 主仓库 / 分发 | HuggingFace [ibm-granite/granite-docling-258M](https://huggingface.co/ibm-granite/granite-docling-258M)；主框架 [docling-project/docling](https://github.com/docling-project/docling)（★62K，MIT）；IBM 文档 [ibm.com/granite/docs/models/docling](https://www.ibm.com/granite/docs/models/docling)；支持 HuggingFace transformers、vLLM、ONNX、mlx-vlm |
| 参数 / VRAM 可跑性 | **258M 参数**：CPU 可推理，A100 上约 0.35s/页；FP16 推理约 1-2 GB VRAM；消费级 GPU（RTX 3060+）或纯 CPU 均可运行。**Olares One（NVIDIA GPU）完全胜任**，甚至可在低功耗 ARM 边缘设备上部署 |
| 变体 / 型号 | granite-docling-258M（当前唯一尺寸）；前身 smoldocling-256m-preview；架构基于 IDEFICS3（SigLIP2-base-patch16-512 + Granite 165M LLM） |
| 闭源对标 | **Azure Document Intelligence**（主要竞品，按页计费）、**AWS Textract**（按页/按字段计费）、**Google Document AI**（订阅+用量）、**LlamaParse**（付费 API）、**Unstructured.io**（免费额度有限的云 API） |
| Olares Market | 无独立应用；通过 **vLLM**（Olares Market 已上架）承载推理；Docling 整套管线可通过 `docling-serve`（FastAPI，docker 镜像可用）部署为 Olares 容器服务；RAGFlow / Dify（Olares Market 已上架）可集成 Docling 作为文档解析引擎 |
| 来源 | [ibm.com/granite/docs/models/docling](https://www.ibm.com/granite/docs/models/docling)；[IBM 发布公告](https://www.ibm.com/new/announcements/granite-docling-end-to-end-document-conversion)；[HuggingFace 模型卡](https://huggingface.co/ibm-granite/granite-docling-258M)；[docling-project/docling GitHub](https://github.com/docling-project/docling)；[MarkTechPost 行业对比（2026-07-04）](https://www.marktechpost.com/2026/07/04/structured-pdf-to-json-a-guide-to-open-source-extraction-models-in-2026/) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| docling github | 880 | 63 | $5.01 | nav |
| smoldocling | 590 | 31 | $0 | info |
| granite-docling-258m ⭐ | 390 | 27 | $0 | info |
| ibm docling | 390 | 54 | $1.07 | info |
| granite docling ⭐ | 320 | 32 | $0 | info |
| docling convert chunks to json ⭐ | 260 | 29 | $0 | info |
| docling documentation | 210 | 37 | $4.82 | info |
| what is docling | 210 | 55 | $0 | info |
| docling python ⭐ | 140 | 23 | $0 | info |
| docling ocr ⭐ | 170 | 26 | $4.61 | info |
| docling pdf | 40 | 0 | $5.53 | info |
| docling document parsing | 30 | 0 | $0 | info |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| docling mcp ⭐ | 110 | 32 | $7.95 | info |
| docling api | 110 | 43 | $5.37 | info |
| docling docker ⭐ | 110 | 23 | $0 | info |
| docling serve ⭐ | 140 | 21 | $0 | info/trans |
| docling vllm ⭐ | 20 | 0 | $0 | info |
| docling langchain ⭐ | 20 | 0 | $0 | info |
| docling llamaindex ⭐ | 20 | 0 | $3.48 | info |
| docling fastapi ⭐ | 30 | 0 | $0 | info |
| granite docling vllm ⭐ | 10 | 0 | $0 | info |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| open source pdf ocr ⭐ | 40 | 37 | $1.70 | info |
| self hosted ocr ⭐ | 20 | 0 | $0 | info |
| run docling locally ⭐ | 10 | 0 | $0 | info |
| docling gpu ⭐ | 40 | 0 | $0 | info |
| docling onnx ⭐ | 10 | 0 | $0 | info |
| docling local ⭐ | 0 | 0 | $0 | info |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| docling vs llamaparse ⭐ | 10 | 0 | $6.19 | comm |
| docling vs unstructured ⭐ | 10 | 0 | $0 | comm |
| open source document intelligence ⭐ | 10 | 0 | $0 | info |
| document ai open source ⭐ | 20 | 0 | $0 | info |
| pdf to markdown ai ⭐ | 20 | 0 | $3.00 | info/comm |
| document parsing ai ⭐ | 10 | 0 | $11.68 | comm |
| document ingestion pipeline ⭐ | 20 | 0 | $8.90 | info |
| document processing pipeline ⭐ | 30 | 9 | $8.28 | info |
| pdf table extraction ⭐ | 110 | 19 | $2.22 | info |
| document layout analysis ⭐ | 50 | 31 | $5.86 | info |
| docling rag ⭐ | 30 | 21 | $7.04 | info |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|-----|-----|------------|-------|
| docling serve | 140 | 21 | $0 | `docling-serve` FastAPI 镜像可直接打包为 Olares 容器 app，一键部署本地文档转换 API 服务 | ⭐⭐⭐ |
| docling docker | 110 | 23 | $0 | Docker 镜像即 Olares 容器化路径；"本地跑 Docling REST API" 的最简入口 | ⭐⭐⭐ |
| docling mcp | 110 | 32 | $7.95 | Docling 官方 MCP server（docling-project/docling-mcp）与 Olares Agent-Native OS 定位强共振；Olares 运行本地 MCP → 文档解析能力直接注入 Personal Agent | ⭐⭐⭐ |
| docling vllm | 20 | 0 | $0 | Granite-Docling 支持 vLLM 推理，Olares Market 已上架 vLLM；一键安装 vLLM 即可挂载模型 | ⭐⭐⭐ |
| docling rag | 30 | 21 | $7.04 | RAGFlow / Dify（Olares Market 已上架）集成 Docling 作为文档解析引擎；全链路本地 RAG 无数据出境 | ⭐⭐⭐ |
| granite docling | 320 | 32 | $0 | 品牌词，Olares 可占据"本地部署 Granite-Docling 全教程"的内容位 | ⭐⭐ |
| self hosted ocr | 20 | 0 | $0 | 直接叙事锚：Olares = 自托管 OCR 基础设施，数据不出本机 | ⭐⭐⭐ |
| open source pdf ocr | 40 | 37 | $1.70 | "free alternative to Azure Document Intelligence" 叙事；Olares 托管 Docling = 零 API 费用 | ⭐⭐ |
| document processing pipeline | 30 | 9 | $8.28 | Olares 本地 AI 管线叙事：Docling → RAGFlow/Dify → Personal Agent，全程离线 | ⭐⭐⭐ |
| pdf table extraction | 110 | 19 | $2.22 | Granite-Docling 核心能力，KD 极低，内容占位机会 | ⭐⭐ |
| docling langchain | 20 | 0 | $3.48 | LangChain/LlamaIndex 集成 → Olares 本地 LLM Agent 消费文档工具 | ⭐⭐ |
| run docling locally | 10 | 0 | $0 | 直接匹配"本地运行"场景，GEO 词；全教程文绑定 Olares | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|-----|-----|------|------|--------------------------|
| docling | 8,100 | 36 | $3.84 | info | 主词候选 | 品牌词量大，KD 36 尚可攻；主打"Docling 自托管完整指南"可覆盖 Olares 部署叙事 |
| docling github | 880 | 63 | $5.01 | nav | 次级 | KD 63 难攻，导航意图，作次级收入内容 |
| smoldocling | 590 | 31 | $0 | info | 主词候选 | Granite-Docling 的前身，搜量相当，KD 31，"SmolDocling → Granite-Docling 升级指南"可同时覆盖两词 |
| granite-docling-258m ⭐ | 390 | 27 | $0 | info | 主词候选 | 精确型号词，KD 27，意图纯，适合"如何本地跑 Granite-Docling-258M"切入 |
| ibm docling | 390 | 54 | $1.07 | info | 次级 | KD 54 偏高，品牌意图，作次级辅助 |
| granite docling ⭐ | 320 | 32 | $0 | info | 主词候选 | 核心品牌词，KD 32，Olares One 部署教程首选主词 |
| docling convert chunks to json ⭐ | 260 | 29 | $0 | info | 次级 | 实际用法词，KD 29，收入 RAG 管线文章 |
| docling documentation | 210 | 37 | $4.82 | info | 次级 | 文档导航意图，作次级 |
| what is docling | 210 | 55 | $0 | info | 次级 | 科普意图，KD 55，作 FAQ/次级收入 |
| docling ocr ⭐ | 170 | 26 | $4.61 | info | 主词候选 | KD 26、CPC $4.61 高，商业价值强；"Docling vs 商业 OCR" 对比文主词候选 |
| docling serve ⭐ | 140 | 21 | $0 | info/trans | 主词候选 | KD 极低 21，REST API 部署场景，Olares 容器化路径；与"docling docker"合并覆盖 |
| docling python ⭐ | 140 | 23 | $0 | info | 次级 | 开发者集成词，KD 23，作次级收入 RAG 教程 |
| docling mcp ⭐ | 110 | 32 | $7.95 | info | 主词候选 | CPC $7.95 + KD 32，Agent 集成场景；与 Olares Agent-Native 定位强共振，独立内容机会 |
| docling api | 110 | 43 | $5.37 | info | 次级 | KD 43，API 使用意图，作次级 |
| docling docker ⭐ | 110 | 23 | $0 | info | 主词候选 | KD 23 极低，Olares 容器化自托管最直接入口 |
| pdf table extraction ⭐ | 110 | 19 | $2.22 | info | 主词候选 | KD 19 极低，Docling 核心能力场景，内容占位容易 |
| document extraction ai | 110 | 50 | $6.45 | info | 次级 | KD 50，泛品类词，作次级 |
| document layout analysis ⭐ | 50 | 31 | $5.86 | info | 次级 | 技术词，CPC $5.86，收入技术对比文 |
| document processing pipeline ⭐ | 30 | 9 | $8.28 | info | 主词候选 | KD 9 极低、CPC $8.28，意图精准；Olares 本地 AI 管线叙事核心词 |
| docling rag ⭐ | 30 | 21 | $7.04 | info | 次级 | KD 21、CPC $7.04，RAG 场景高商业价值，作次级 |
| self hosted ocr ⭐ | 20 | 0 | $0 | info | GEO | 近零量但意图精准，GEO 抢占"自托管 OCR"引用位 |
| run docling locally ⭐ | 10 | 0 | $0 | info | GEO | GEO 前哨，与 Olares 本地部署叙事强绑定 |
| docling vllm ⭐ | 20 | 0 | $0 | info | GEO | vLLM 承载路径，GEO 前哨；Olares Market vLLM 一键安装 |
| docling vs llamaparse ⭐ | 10 | 0 | $6.19 | comm | GEO | CPC $6.19 商业价值高，近零量，GEO 抢占对比位 |
| open source document intelligence ⭐ | 10 | 0 | $0 | info | GEO | "Azure Document Intelligence 平替"叙事前哨 |
| document ingestion pipeline ⭐ | 20 | 0 | $8.90 | info | GEO | CPC $8.90，高商业价值，GEO 占位 |

---

## 核心洞见

1. **搜索心智已初步建立，但主要集中在"Docling"品牌词**
   "docling" 主词月量 8,100（KD 36），流量实际锚定在 GitHub（880/月）和 IBM 文档页，而非独立域名。Granite-Docling 作为模型的品牌词（`granite docling` 320/月、`granite-docling-258m` 390/月）已有真实搜量，KD 均在 27-32，是可攻的机会窗口。前身 `smoldocling` 仍有 590/月、KD 31，说明有一批人正在追踪这条产品线的演进。

2. **258M 参数，CPU 可跑——叙事完全成立**
   258M 参数、FP16 约 1-2 GB VRAM，纯 CPU 也可推理（A100 上 0.35s/页，消费级 GPU 更无压力）。Olares One 及任何配备入门级 GPU 的 Olares 实例均可运行完整 Docling + Granite-Docling 推理管线。"本地运行 + 数据不出机" 叙事在技术上无硬门槛。

3. **Apache 2.0，商用友好，可全力主推**
   模型本身 Apache 2.0，Docling 库 MIT，无任何地区限制或使用约束。对 Olares 而言既是主推卖点（商业用途合规、可在产品中集成），也排除了腾讯/Skywork 系常见的合规风险。

4. **对 Olares 最关键的 3 个词**
   - `docling serve`（KD 21）：REST API 容器化部署路径，直接对应 Olares app 形态
   - `docling mcp`（KD 32，CPC $7.95）：MCP server 与 Olares Agent-Native OS 定位最强共振，内容价值最高
   - `document processing pipeline`（KD 9，CPC $8.28）：极低竞争、极高商业价值，是 Olares 本地 AI 基础设施叙事的杠杆词

5. **GEO 抢发窗口**
   大量引擎组合词（`docling vllm`、`docling langchain`、`docling llamaindex`）、对比词（`docling vs llamaparse`、`docling vs unstructured`）和部署词（`run docling locally`、`self hosted ocr`）均为近零量、KD 为 0，是典型 GEO 前哨。Granite-Docling 于 2025 年 9 月发布，搜索生态正在成型，此时抢占 AI Overview / Perplexity 引用位成本最低。

6. **闭源对标与攻击面**
   主要攻击面：**Azure Document Intelligence**（2,400/月，按页计费，$1.5/1000 页起）、**AWS Textract**（2,900/月，按页按字段双重计费）、**LlamaParse**（1,600/月，付费 API 5,000 页/月免费额度）。三者的共同弱点是：API 调用费用随量线性增长、数据必须上传云端（GDPR/HIPAA 合规难）、无法离线/边缘部署。Docling + Granite-Docling = **永久零 API 费用 + 数据不出本机**，对有隐私需求的企业用户（金融、医疗、法律）是强攻击点。

7. **与 OCR 方向同类报告关联**
   同属 `08-ocr` 类别的 PaddleOCR-VL（报告已有）定位为通用 OCR 引擎（100+ 语言，100M-34.5M 参数），而 Granite-Docling 定位更聚焦于"文档结构保留 + RAG 前处理"，两者互补（PaddleOCR-VL 用于 OCR，Docling 用于结构化输出），在内容层可联合撑起一篇"RAG 文档管线：如何选 OCR + 解析引擎"的 listicle。`docling mcp` + `docling serve` 也与 tech/ 方向的 MCP/Agent 基础设施词有跨报告协同机会。

---

*数据来源：SEMrush US（phrase_these × 5批、phrase_related、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
