# dots.ocr / dots.mocr 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：rednote-hilab（小红书 AI 研究团队），MIT License
>
> **注**：dots.ocr 由 rednote-hilab（小红书/Xiaohongshu 研究团队）发布，不属于 Bytedance/Doubao 团队。该模型在基准测试中**优于** Doubao 系列（doubao-1.5/1.6），常被混淆为"Doubao 模型"。2026.03 正式更名为 dots.mocr。
>
> **无独立官网，SEO 主战场在 HuggingFace 页面、GitHub README 及第三方技术内容。**

---

## 模型理解（前置）

dots.ocr（现更名为 dots.mocr）是一款专注文档解析的多语言 VLM，统一了版面检测与内容识别（文字/表格/公式/阅读顺序），以 1.7B 参数在 OmniDocBench 和 XDocParse 基准上超越 Gemini-2.5-Pro 及 Doubao-1.5/1.6，是 2025 年文档 OCR 领域最受关注的开源模型之一。由小红书 AI 研究团队 rednote-hilab 主导，MIT 协议商用无限制，从 vLLM 0.11.0 起原生支持，GitHub 累计 ~9,000 ★，是 Google Document AI / Azure Document Intelligence 的有力开源替代。

| 项目 | 内容 |
|------|------|
| 一句话定位 | OCR / 文档解析 VLM；多语言版面检测 + 内容识别一体化，100+ 语言 |
| 许可证 | **MIT License**（商用友好，无地区限制） |
| 主仓库 / 分发 | [GitHub](https://github.com/rednote-hilab/dots.ocr)（~8,977★，802 forks）；[HuggingFace rednote-hilab/dots.ocr](https://huggingface.co/rednote-hilab/dots.ocr) → 已更名 [dots.mocr](https://huggingface.co/rednote-hilab/dots.mocr)；vLLM 0.11.0 原生集成 |
| 参数 / VRAM 可跑性 | 1.7B 参数；vLLM 以 `--gpu-memory-utilization 0.9` 单卡部署；约 4-6GB 显存即可，**8GB 消费级 GPU / Olares One 均可本地运行** |
| 变体 / 型号 | dots.ocr（首发，2025-07）→ dots.ocr.base（2025-10，基础 VLM）→ dots.mocr（2026-03 更名，正式版）→ dots.mocr-svg（SVG 专项变体） |
| 闭源对标 | Google Document AI、Azure Document Intelligence、AWS Textract、Adobe PDF Extract API；性能上亦超越 Doubao-1.5/Gemini-2.5-Pro |
| Olares Market | vLLM 已上架 Olares Market；dots.mocr 可通过 vLLM 一键部署（无需额外插件） |
| 来源 | [GitHub README](https://github.com/rednote-hilab/dots.ocr)；[HuggingFace 模型页](https://huggingface.co/rednote-hilab/dots.ocr)；[arXiv 2512.02498](https://arxiv.org/abs/2512.02498)；[vLLM PR #24645](https://github.com/vllm-project/vllm/pull/24645) |

---

## 流量基线（Phase 1）

无独立官网，跳过域名报告。SEO 主战场为 HuggingFace 模型页、GitHub README 与第三方技术博客/文档站。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| dots.ocr | 2,400 | 40 | $5.84 | info |
| dots ocr | 390 | 36 | $3.72 | info |
| dots ocr model | 10 | 0 | — | info |
| dots.mocr | <10 | — | — | info |
| dots mocr | <10 | — | — | info |

> dots.mocr 因更名时间较短（2026-03），搜索量尚未建立，是 GEO 抢发候选。

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ocr llm | 140 | 16 | $3.43 | info ⭐ |
| document parsing vllm | 0 | — | — | info |
| dots ocr vllm | 0 | — | — | info |
| ocr vllm | 0 | — | — | info |

> `ocr llm` 是引擎组合词里最强的机会：KD 仅 16，月量 140，捕捉"把 VLM 跑成 OCR 服务"的意图，与 Olares+vLLM 部署路径完美吻合。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| local ocr | 30 | 0 | $7.54 | info ⭐ |
| self-hosted ocr | 20 | 0 | — | info ⭐ |
| ocr docker | 20 | 0 | — | info ⭐ |
| dots ocr local | 0 | — | — | info |
| dots ocr install | 0 | — | — | info |
| run dots ocr locally | 0 | — | — | info |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| google document ai | 1,900 | 35 | $10.51 | comm |
| azure document intelligence | 2,400 | 62 | $10.48 | comm |
| easyocr | 1,600 | 27 | $2.94 | info ⭐ |
| llamaparse | 1,600 | 33 | $12.79 | comm |
| paddleocr | 2,900 | 42 | $4.17 | info |
| docling | 8,100 | 36 | $3.84 | info |
| tesseract ocr | 5,400 | 74 | $3.37 | info |
| surya ocr | 210 | 29 | $5.87 | info ⭐ |
| marker pdf | 320 | 36 | $1.17 | info |
| tesseract alternative | 40 | 19 | — | info ⭐ |
| google document ai alternative | 20 | 0 | — | comm ⭐ |
| document ai alternative | 20 | 0 | $4.81 | comm ⭐ |
| surya ocr alternative | 0 | — | — | info |
| docling alternative | 0 | $4.76 | — | info |

### 生态 / 应用场景词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| invoice ocr | 590 | 36 | $21.54 | info/comm |
| ocr for pdf | 880 | 50 | $1.40 | info |
| ocr python | 720 | 39 | $1.37 | info |
| open source ocr | 260 | 46 | $2.75 | info |
| receipt ocr | 210 | 26 | $8.23 | info ⭐ |
| ocr model | 480 | 55 | $6.03 | info |
| best ocr model | 110 | 47 | $2.75 | info |
| document parsing | 140 | 30 | $12.82 | comm ⭐ |
| document understanding | 170 | 28 | $5.40 | info ⭐ |
| ocr llm | 140 | 16 | $3.43 | info ⭐ |
| document layout analysis | 50 | 31 | $5.86 | info |
| multilingual ocr | 20 | 0 | $4.97 | info ⭐ |
| ocr benchmark | 140 | 41 | $6.71 | info |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| ocr llm | 140 | 16 | $3.43 | dots.mocr via vLLM 一键部署；Olares Market 已有 vLLM 引擎，搜 "run VLM as OCR service locally" 的用户直接命中 | ⭐⭐⭐ |
| self-hosted ocr | 20 | 0 | — | 零竞争；Olares = 最简 self-host 路径（vLLM+dots.mocr），主打"数据不出本机" | ⭐⭐⭐ |
| local ocr | 30 | 0 | $7.54 | CPC $7.54 说明商业价值高；Olares One 4-6GB 显存轻松跑 1.7B | ⭐⭐⭐ |
| google document ai alternative | 20 | 0 | — | 战略 GEO 词；Google Document AI 按页计费（约 $65/1000 页），dots.mocr 本地零 API 费用 | ⭐⭐⭐ |
| document ai alternative | 20 | 0 | $4.81 | 同上，覆盖 Azure/AWS/Adobe 整类替代意图 | ⭐⭐⭐ |
| multilingual ocr | 20 | 0 | $4.97 | 100+ 语言是 dots 核心卖点，本地跑无语言限制、不涉及数据出境合规 | ⭐⭐⭐ |
| dots.ocr | 2,400 | 40 | $5.84 | 品牌主词，覆盖品牌认知流量；Olares 角度=部署教程/how-to 内容 | ⭐⭐ |
| dots ocr | 390 | 36 | $3.72 | 同上，拼写变体 | ⭐⭐ |
| tesseract alternative | 40 | 19 | — | KD 仅 19；Tesseract 用户是最自然的迁移受众，dots.mocr 精度大幅超越 | ⭐⭐ |
| receipt ocr | 210 | 26 | $8.23 | 高 CPC 商业场景；私有化 receipt/invoice 解析（财务隐私）is a natural Olares fit | ⭐⭐ |
| document parsing | 140 | 30 | $12.82 | 高 CPC；Olares 角度=搭建内部文档处理 pipeline | ⭐⭐ |
| document understanding | 170 | 28 | $5.40 | 语义理解场景，Personal Agent 组件（RAG 前置解析） | ⭐⭐ |
| surya ocr | 210 | 29 | $5.87 | 同是开源 OCR，可对比叙事；dots.mocr 在多语言/表格解析上更强 | ⭐ |
| easyocr | 1,600 | 27 | $2.94 | 量大 KD 低；EasyOCR 用户群大量为 Python 本地部署受众，可引流 | ⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| dots.ocr | 2,400 | 40 | $5.84 | info | 主词候选 | 品牌主词，有量有 CPC；KD 40 偏高但品牌词可打；Olares 部署教程页锚点 |
| docling | 8,100 | 36 | $3.84 | info | 主词候选 | 最高量开源文档解析词；dots.mocr 对比/替代角度，"docling vs dots.mocr" 可成文 |
| google document ai | 1,900 | 35 | $10.51 | comm | 主词候选 | CPC $10.51 商业价值高；"open source google document ai alternative" GEO 切入 |
| paddleocr | 2,900 | 42 | $4.17 | info | 次级 | 同类开源 OCR 最大量词；可做对比次级词 |
| easyocr | 1,600 | 27 | $2.94 | info | 次级 ⭐ | KD 低量大；EasyOCR 用户为本地部署受众，dots.mocr alternative 切入 |
| llamaparse | 1,600 | 33 | $12.79 | comm | 次级 | CPC 最高；PDF 解析场景，Olares 角度=本地跑 dots.mocr 替代付费 LlamaParse |
| azure document intelligence | 2,400 | 62 | $10.48 | comm | 次级 | KD 62 过高作主词；作次级覆盖商业替代意图 |
| ocr for pdf | 880 | 50 | $1.40 | info | 次级 | 高量场景词；作内容次级 |
| invoice ocr | 590 | 36 | $21.54 | comm | 次级 | CPC $21.54 最高；财务 OCR 场景，私有化强需求 |
| dots ocr | 390 | 36 | $3.72 | info | 次级 | dots.ocr 拼写变体，与主词共用内容 |
| surya ocr | 210 | 29 | $5.87 | info | 次级 ⭐ | 同类开源竞品，dots 在表格和多语言上更强；对比文次级 |
| receipt ocr | 210 | 26 | $8.23 | comm | 次级 ⭐ | KD 低 CPC 高；Olares 私有化账单解析场景 |
| marker pdf | 320 | 36 | $1.17 | info | 次级 | PDF 解析开源工具；可并入对比内容 |
| document understanding | 170 | 28 | $5.40 | info | 次级 ⭐ | KD 低；RAG 前置文档解析是 Olares Personal Agent 场景 |
| ocr llm | 140 | 16 | $3.43 | info | 次级 ⭐ | **KD 仅 16**；"用 VLM 做 OCR" 精准命中 dots.mocr+vLLM 组合；Olares 最强次级词 |
| document parsing | 140 | 30 | $12.82 | comm | 次级 ⭐ | 高 CPC；内部文档处理 pipeline 场景 |
| open source ocr | 260 | 46 | $2.75 | info | 次级 | 通用替代意图，作次级收 |
| tesseract alternative | 40 | 19 | — | info | GEO ⭐ | KD 19，Tesseract 是最大开源 OCR 存量用户群；GEO 抢位 |
| google document ai alternative | 20 | 0 | — | comm | GEO ⭐ | KD=0 战略 GEO 词；CPC 语境商业意图强，零竞争抢 AI Overview 引用 |
| document ai alternative | 20 | 0 | $4.81 | comm | GEO ⭐ | 同上，覆盖 Azure/AWS 替代意图 |
| self-hosted ocr | 20 | 0 | — | info | GEO ⭐ | KD=0；Olares 自托管叙事核心词，GEO 抢占 |
| local ocr | 30 | 0 | $7.54 | info | GEO ⭐ | CPC $7.54 + KD=0；本地跑 OCR 的高价值 GEO 词 |
| multilingual ocr | 20 | 0 | $4.97 | info | GEO ⭐ | 100+ 语言是 dots 核心差异化；GEO 抢占 |
| dots.mocr | <10 | — | — | info | GEO | 新品牌名搜索量未建立；GEO 抢发锁定新名称 |
| dots mocr svg | 0 | — | — | info | GEO | SVG 专项变体，垂直场景 GEO 前哨 |
| document parsing vllm | 0 | — | — | info | GEO | 精准技术长尾；vLLM+dots.mocr 部署 how-to 的 GEO 词 |

---

## 核心洞见

1. **搜索心智已初步建立**：`dots.ocr` 月量 2,400 对一个 2025-07 才发布的模型来说超出预期，说明 GitHub 9K★ 和 vLLM 原生集成带来了持续的搜索流入。更名后的 `dots.mocr` 尚无量，是 GEO 抢先布局的窗口。

2. **消费级 GPU / Olares One 完全可跑**：1.7B 参数模型显存需求约 4-6GB，8GB 显存单卡即可服务。vLLM 官方 docker image（v0.11.0+）直接部署，命令行一行搞定。Olares One 与消费级 NVIDIA GPU 均在支持范围内，叙事完全成立。

3. **MIT 协议，商用可主推**：无任何地区或商业用途限制，可作"免费自托管替代 Google Document AI / Azure Document Intelligence"的主力卖点。

4. **对 Olares 最关键的 3 个词**：
   - `ocr llm`（140/mo, KD 16）：最低竞争、最精准意图，捕获"把 VLM 做 OCR 服务"用户；vLLM on Olares 一键跑。
   - `google document ai alternative`（20/mo, KD 0）：零竞争战略 GEO，攻击 Google 按页计费痛点（约 $65/1000 页）。
   - `self-hosted ocr`（20/mo, KD 0, CPC $7.54）：高商业价值 + 零竞争，Olares 自托管叙事最精准锚点。

5. **GEO 抢发窗口**：`dots.mocr`（新品牌名）、`document parsing vllm`、`multilingual ocr`、`self-hosted ocr`、`local ocr` 均近零量，但语义精准，适合抢占 AI Overview / Perplexity 引用位。更名（dots.ocr→dots.mocr）刚发生 4 个月，内容窗口期未关闭。

6. **闭源对标与攻击面**：
   - **Google Document AI**：按页计费（~$65/1000 页），数据上传 Google 云，有 GDPR/数据出境合规风险 → dots.mocr 本地免费、私有。
   - **Azure Document Intelligence**：企业定价复杂（~$10/1000 页基础，表单分析更贵），API 限速，需 Azure 账号 → dots.mocr 本地无限速。
   - **LlamaParse**：$0.003/页付费，面向 RAG 场景 → dots.mocr MIT 无费用，可嵌入 Olares 本地 RAG pipeline。
   - **共同攻击面**：付费 API、数据出云、额度限制；dots.mocr 本地部署三点全解决。

7. **同类家族关联**：OCR 模型同类在 [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 08-ocr 章节，同组已有 PaddleOCR-VL 报告（[paddleocr-vl.md](paddleocr-vl.md)）。两者可组成"open source OCR"内容簇——PaddleOCR-VL 主打中文/移动端，dots.mocr 主打多语言/文档结构解析，不直接重叠。surya ocr（210/mo, KD 29）是另一个潜在对比词，三者可形成"best open source OCR 2026" listicle 的核心候选。

---

*数据来源：SEMrush US（phrase_these × 3 批次）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
