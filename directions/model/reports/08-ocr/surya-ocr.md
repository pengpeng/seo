# Surya OCR 2 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：datalab.to（Vikas Paruchuri / Datalab Team），代码 Apache 2.0 / 权重 modified OpenRAIL-M

## 模型理解（前置）

Surya OCR 2（v0.20.0，2026-05-27）是 Datalab 出品的 650M 参数 VLM，一个模型覆盖四项文档任务：全页 OCR、版面分析（layout）、阅读顺序检测、表格识别，支持 91 种语言，在 olmOCR-bench 以 83.3% 分数位居 3B 以下参数最佳。推理后端为 vLLM（NVIDIA GPU）或 llama.cpp（CPU/Apple Silicon），GitHub 仓库约 21K⭐。其 650M 参数量使它能在消费级硬件上运行，直接对标 AWS Textract 等云端 OCR 付费 API——"自托管替代"叙事完整。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 650M 参数多语言文档 OCR VLM，单模型四任务（OCR/版面/顺序/表格），3B 以下最优 |
| 许可证 | 代码 Apache 2.0；模型权重 modified OpenRAIL-M（研究/个人/营收<$5M 的初创免费；商业授权需单独签约）|
| 主仓库 / 分发 | [GitHub datalab-to/surya](https://github.com/datalab-to/surya)（~21K ⭐）、[HuggingFace datalab-to/surya-ocr-2](https://huggingface.co/datalab-to/surya-ocr-2)、PyPI `surya-ocr` |
| 参数 / VRAM 可跑性 | 650M；vLLM 路线需 NVIDIA GPU（GGUF 量化版可在 8GB 显存通过降批次跑通）；llama.cpp 路线支持 CPU 和 Apple Silicon（M1 测得 ~0.1 pages/s，较新 M 系列更快）；**Olares One（NVIDIA GPU）可跑**，Apple Silicon 无 GPU 加速（llama.cpp 走 Metal 但速度较慢）|
| 变体 / 型号 | Surya OCR 2（主力，650M）；Chandra OCR 2（Datalab 商业高精度版，5.3B，API-only）；检测子模型单独 torch（轻量，无需后端）|
| 闭源对标 | AWS Textract（基础层）、Google Vision OCR / Document AI、Azure OCR、Nanonets |
| Olares Market | 未直接上架；需通过 vLLM（NVIDIA）或 llama.cpp 手动部署；Olares 已支持 vLLM 容器化引擎 |
| 来源 | [GitHub README](https://github.com/datalab-to/surya)、[Datalab 官方博客](https://www.datalab.to/blog/surya-2)、[HuggingFace 模型卡](https://huggingface.co/datalab-to/surya-ocr-2) |

---

## 流量基线（Phase 1）

| 指标 | 数据 |
|------|------|
| 域名 | datalab.to |
| SEMrush Rank | 1,007,760 |
| 月自然流量（US） | 1,082 |
| 关键词数 | 120 |
| 流量估值 | $4,127/月 |
| 付费关键词 | 3（$128/月）|

**注**：datalab.to 是初创公司站，流量总量小；但 Surya OCR 相关词（surya ocr、surya-ocr、datalab surya）合计贡献约 83 次点击/月，占站点流量约 7.7%——说明品牌词已初步建立搜索入口，但仍以导航意图为主，信息/商业意图流量极少。

### 官网 TOP 关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | 流量 | URL |
|--------|------|------|----|------|-----|
| datalab | 1 | 1,600 | 62 | 396 | datalab.to/ |
| data lab | 1 | 1,000 | 59 | 248 | datalab.to/ |
| datalab center | 1 | 320 | 20 | 79 | datalab.to/ |
| datalabs | 1 | 170 | 63 | 42 | datalab.to/ |
| chandra ocr | 2 | 260 | 40 | 34 | datalab.to/blog/introducing-chandra |
| surya ocr | 2 | 210 | 21 | 34 | datalab.to/blog/surya-2 |
| surya-ocr | 2 | 210 | 22 | 27 | datalab.to/blog/surya-2 |
| datalab surya | 2 | 170 | 20 | 22 | datalab.to/platform |
| mathematical ocr | 5 | 140 | 16 | 6 | datalab.to/blog/cracking-math-ocr |
| marker ocr | 3 | 40 | 28 | 3 | datalab.to/ |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| surya ocr | 210 | 29 | $5.87 | 导航 |
| surya-ocr | 210 | 27 | $5.87 | 导航 |
| datalab surya | 170 | 20 | $0 | 导航 ⭐ |
| surya ocr example use case | 50 | 0 | $0 | 信息 ⭐ |
| suryaocr | 40 | 25 | $0 | 导航 ⭐ |
| surya train | 40 | 22 | $0 | 信息 ⭐ |
| surya ocr github | 20 | 0 | $0 | 导航 ⭐ |
| surya layout | 20 | 0 | $0 | 信息 ⭐ |
| surya ocr vs paddleocr | 20 | 0 | $0 | 信息 ⭐ |
| surya ocr description | 40 | 0 | $0 | 信息 ⭐ |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| surya ocr vllm | 0 | — | — | — |
| surya ocr docker | 0 | — | — | — |
| surya ocr llama.cpp | 0 | — | — | — |

> 所有引擎组合词当前搜索量为零，属典型 GEO 抢发词；参考类似成熟模型（如 easyocr 月量 1,600，paddleocr 2,900），一旦 Surya OCR 2 被主流 OCR 基础设施整合，量级有 10-100× 增长空间。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| local ocr | 30 | 0 | $7.54 | — ⭐ |
| self hosted ocr | 20 | 0 | $0 | — ⭐ |
| ocr open source python | 20 | 0 | $0 | — ⭐ |
| open source ocr model | 10 | 0 | $4.28 | — ⭐ |
| run ocr locally | 0 | — | — | — |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| easyocr | 1,600 | 27 | $2.94 | 信息 ⭐ |
| aws textract | 2,900 | 34 | $11.85 | 商业 |
| open source ocr | 260 | 46 | $2.75 | 信息 |
| chandra ocr | 260 | 40 | $2.96 | 导航 |
| nanonets ocr | 210 | 32 | $4.42 | 商业 |
| docling ocr | 170 | 26 | $4.61 | 信息 ⭐ |
| handwriting ocr | 720 | 19 | $3.53 | 信息 ⭐ |
| pdf text extraction | 590 | 33 | $1.00 | 信息 |
| marker pdf | 320 | 36 | $1.17 | 信息 |
| tesseract alternative | 40 | 19 | $0 | 信息 ⭐ |
| best open source ocr | 50 | 39 | $4.02 | 信息 |
| aws textract alternative | 10 | 0 | $6.67 | 信息 ⭐ |
| surya ocr vs paddleocr | 20 | 0 | $0 | 信息 ⭐ |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| surya ocr | 210 | 29 | $5.87 | Surya OCR 2 可在 Olares One（NVIDIA GPU）以 vLLM 运行，5页/秒吞吐；数据本地处理，零隐私泄露 | ⭐⭐⭐ |
| easyocr | 1,600 | 27 | $2.94 | "EasyOCR vs Surya OCR 2" 对比文：Surya OCR 2 精度更高（83.3% vs ~60%+），同样可在消费级 GPU 本地跑 | ⭐⭐⭐ |
| self hosted ocr | 20 | 0 | $0 | Olares 提供一键部署 vLLM 容器，Surya OCR 2 在其上即为完整自托管 OCR 平台 | ⭐⭐⭐ |
| aws textract alternative | 10 | 0 | $6.67 | 高 CPC（$6.67）、零 KD，GEO 窗口极佳；叙事：自托管替代 AWS Textract，零 API 费用，数据不出本地 | ⭐⭐⭐ |
| local ocr | 30 | 0 | $7.54 | 高 CPC、低 KD；Olares One + Surya OCR 2 = 即插即用本地 OCR 解决方案 | ⭐⭐⭐ |
| open source ocr | 260 | 46 | $2.75 | KD 46 偏高，但与 Olares "开源自托管"核心主张完全契合；可用于栏目页 / GEO 展示词 | ⭐⭐ |
| handwriting ocr | 720 | 19 | $3.53 | Surya OCR 2 支持手写识别，且 KD 极低；Olares 打"家庭/企业本地手写文档数字化" | ⭐⭐ |
| document layout analysis | 50 | 31 | $5.86 | Surya OCR 2 的 layout 能力对 RAG/个人 Agent 场景意义重大；"在 Olares 上本地做文档结构化" | ⭐⭐ |
| pdf text extraction | 590 | 33 | $1.00 | 量大（590），Surya 的 vLLM 路线可作为 PDF pipeline 核心；适合 Olares 文件服务 + OCR 结合的内容 | ⭐⭐ |
| docling ocr | 170 | 26 | $4.61 | Docling 是 IBM 出品的文档解析工具，与 Surya 定位类似；可写对比文切入"docling vs surya" | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| surya ocr | 210 | 29 | $5.87 | 导航 | 主词候选 | 品牌主词，量 210、KD 29；Olares 落地页 / 博客锚点，结合 self-hosted 叙事 |
| easyocr | 1,600 | 27 | $2.94 | 信息 | 主词候选 | 同类老牌词，量大（1,600）、KD 低（27）；"Surya OCR 2 vs EasyOCR" 对比文机会，引导本地部署叙事 |
| handwriting ocr | 720 | 19 | $3.53 | 信息 | 主词候选 | 量 720、KD 极低（19）；Surya 支持手写，Olares 可做"本地手写识别"文章，直接 top-3 可期 |
| pdf text extraction | 590 | 33 | $1.00 | 信息 | 主词候选 | 量 590、KD 33；PDF pipeline + Surya OCR 2 + Olares 文件存储的场景教程，长期流量来源 |
| datalab surya | 170 | 20 | $0 | 导航 | 次级 | KD 20、量 170；导航意图，适合官方文档/教程页而非 Olares 主导内容 |
| surya-ocr | 210 | 27 | $5.87 | 导航 | 次级 | 拼写变体，与 surya ocr 合并覆盖；次级词出现在代码示例/安装教程 |
| docling ocr | 170 | 26 | $4.61 | 信息 | 次级 | KD 26 ⭐；IBM Docling vs Surya OCR 2 对比内容，Olares 角度：都能自托管 |
| open source ocr | 260 | 46 | $2.75 | 信息 | 次级 | KD 偏高（46），量 260；作为文章 H2 / 元描述关键词，而非主打标题词 |
| surya ocr vllm | 0 | 0 | — | — | GEO | 搜索量当前为零；vLLM 整合是 Surya OCR 2 核心运行路线，GEO 抢占 AI Overview 先发优势 |
| self hosted ocr | 20 | 0 | $7.54 | — | GEO | KD 0、CPC $7.54（付费竞争存在需求），GEO 落地时机；Olares 自托管 OCR 场景 |
| aws textract alternative | 10 | 0 | $6.67 | 信息 | GEO | 量小但 CPC 极高（$6.67），用户付费意愿强；GEO 内容植入"Surya OCR 2 on Olares 替代 Textract" |
| surya ocr vs paddleocr | 20 | 0 | $0 | 信息 | GEO | 当前零量，是高潜力垂直对比词；GEO 抢发可覆盖精度/语言支持/部署难度三维度 |
| local ocr | 30 | 0 | $7.54 | — | GEO | KD 0 + 高 CPC，意味着付费需求存在但 SEO 尚无竞争；Olares + Surya OCR 2 场景文 |
| mathematical ocr | 140 | 16 | $1.55 | 信息 | 次级 | KD 16 极低，量 140；Surya 支持数学公式 OCR，适合 Olares 学术文档场景 |

---

## 核心洞见

1. **搜索心智已初步建立，但极度品牌导向**
   "surya ocr"（210）+ "surya-ocr"（210）+ "datalab surya"（170）合计月量约 590，在开源 OCR 工具中属于中等水平（对比 easyocr 1,600、paddleocr 2,900）。datalab.to 域名流量多来自通用"datalab"导航词，Surya 专有词贡献占比约 7.7%，说明 Surya OCR 2 尚在爬坡期——距 2026-05-27 发布仅约 5 周，搜索量仍处早期积累阶段。

2. **消费级 GPU / Olares One 完全可跑，Apple Silicon 可以运行但慢**
   650M 参数 + GGUF 量化，8GB VRAM 可通过降批次跑通（官方测试 RTX 5090 达 5.35 pages/s）。Olares One（NVIDIA GPU）走 vLLM 路线，性能最优；Apple Silicon 走 llama.cpp + Metal，M1 约 0.1 pages/s，较新芯片有改善。叙事成立。

3. **许可证有条件可用：初创免费，商业需洽谈**
   代码 Apache 2.0 可完全自由分发，但**模型权重为 modified OpenRAIL-M**——个人用户与营收 <$5M 的初创可免费使用，大型商业客户需向 Datalab 付费授权。Olares 内容可面向个人/初创诉求主推，不建议在企业场景中笼统宣称"完全免费"；竞品 Tesseract 是纯 Apache 2.0，差异要在文章中说清楚。

4. **Olares 最关键的 2-3 个词**
   - `easyocr`（1,600，KD 27）：写"Surya OCR 2 vs EasyOCR"对比文，流量最大、竞争可攻，切入本地部署叙事
   - `handwriting ocr`（720，KD 19）：KD 极低，Surya 有真实手写支持能力，Olares 场景具体（本地手写笔记/文档数字化）
   - `self hosted ocr` / `local ocr`（量小但 KD=0，CPC 高）：GEO 优先占领，配合 Olares One "一键跑 Surya OCR"教程

5. **GEO 抢发窗口**
   以下词当前搜索量为零或极低，是最近 5 周内随 Surya OCR 2 发布涌现的语义查询：`surya ocr vllm`、`surya ocr docker`、`surya ocr 2`、`surya ocr vs paddleocr`、`aws textract alternative surya`。这些词极可能出现在 Perplexity / AI Overview 的推荐回答中——发布"Surya OCR 2 on Olares：替代 AWS Textract 的本地文档 OCR 方案"类 GEO 内容，可提前锁定引用位。

6. **闭源对标与攻击面**
   主对标 AWS Textract（月量 2,900、CPC $11.85，付费意愿强烈）：Textract 按页计费（$1.5/1000 页），对高吞吐场景成本高；Surya OCR 2 本地跑边际成本接近零，且数据不离本地。次要对标：Google Document AI（1,900，CPC $10.51）、Azure OCR（480，CPC $6.84）、Nanonets（210，KD 32，商业竞争更直接）。攻击点：按量付费 vs. 固定硬件成本、云端隐私合规风险 vs. 本地处理。

7. **同类 family 关联**
   同在 [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 08-ocr 类别下，目前仅有 [paddleocr-vl.md](paddleocr-vl.md) 已完成研究。PaddleOCR 月量（2,900）远大于 Surya 当前值（210），但 Surya OCR 2 在精度/轻量化/多语言方向叙事更强，两篇报告可互为内链（"Surya vs PaddleOCR 对比"）。建议 seo-content 阶段组合 `easyocr`（1,600）+ `surya ocr`（210）簇写一篇对比文，优先覆盖 EasyOCR 的现有用户。

---

*数据来源：SEMrush US（phrase_this、phrase_these、phrase_fullsearch、phrase_related、domain_rank、resource_organic）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
