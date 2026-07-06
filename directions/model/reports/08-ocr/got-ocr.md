# GOT-OCR2.0 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：StepFun（阶跃星辰）+ UCAS，Apache 2.0
> 无独立官网，SEO 主战场在 GitHub / HuggingFace / 第三方内容页。

## 模型理解（前置）

GOT-OCR2.0（General OCR Theory）是 StepFun（阶跃星辰）联合中科院大学（UCAS）与旷视（Megvii）于 2024 年 9 月发布的统一端到端 OCR 模型，580M 参数，将文字、数学公式、表格、图表、乐谱、分子式、几何图形等所有"人工光学信号"统一纳入单一框架处理（即"OCR-2.0"理论）。相较于传统 Tesseract 等 OCR-1.0 系统，GOT 用 encoder-decoder 架构（高压缩编码器 + Qwen-0.5B 解码器）实现跨场景统一，发布当周 HuggingFace 流行榜 #1，2024 年 12 月模型下载量突破 100 万次，2025 年 2 月正式合入 HuggingFace Transformers 官方库。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 统一端到端 OCR-2.0 模型；覆盖文字 / 公式 / 表格 / 图表 / 乐谱 / 分子式 |
| 许可证 | Apache 2.0（2024 年 10 月已明确，旧 README "研究仅限" 措辞已删除）—— **商用友好，可主推** |
| 主仓库 / 分发 | GitHub [Ucas-HaoranWei/GOT-OCR2.0](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)（★ 8.1k）；HuggingFace [stepfun-ai/GOT-OCR2_0](https://huggingface.co/stepfun-ai/GOT-OCR2_0)（1M+ 下载）；[stepfun-ai/GOT-OCR-2.0-hf](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf)（官方 Transformers 集成版） |
| 参数 / VRAM 可跑性 | ~580M 参数；FP16 最低 4GB VRAM，推荐 6GB+；RTX 3060 / Olares One（NVIDIA GPU）均可跑 |
| 变体 / 型号 | GOT-OCR2.0（单一版本）；支持 slice / whole-page 两种输入模式；动态分辨率与多页 OCR；region-level 坐标/颜色交互模式 |
| 闭源对标 | AWS Textract（基础层）、Google Cloud Vision API、Azure AI Document Intelligence；公式/表格层可对标 Mathpix |
| Olares Market | 未上架；现阶段通过 HuggingFace Transformers + Python/CUDA 直接部署，无 Ollama/ComfyUI 生态集成 |
| 来源 | [arXiv:2409.01704](https://arxiv.org/abs/2409.01704)；[GitHub README](https://github.com/Ucas-HaoranWei/GOT-OCR2.0)；[HF Model Card](https://huggingface.co/stepfun-ai/GOT-OCR-2.0-hf)；[HF Transformers 文档](https://huggingface.co/docs/transformers/main/model_doc/got_ocr2) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| got ocr2.0 | 320 | 31 | $0 | info |
| got-ocr2.0 | 320 | 31 | $0 | info |
| got ocr | 50 | 30 | $0 | info |
| got-ocr 2.0 ⭐ | 50 | 0 | $0 | info |
| got ocr model ⭐ | 20 | 0 | $0 | info |
| general ocr theory ⭐ | 10 | 0 | $0 | info |

> 注："got-ocr2.0" 与 "got ocr2.0" Semrush 返回相同月量（320），为同一搜索意图的格式变体，内容中建议同时覆盖。

### 引擎组合词（Olares 机会前哨）

GOT-OCR2.0 目前无主流 Ollama / ComfyUI / vLLM 集成，搜索量暂未形成；Semrush 该维度未返回有效数据。以下为生态最近切入点词（量虽小，属 GEO 前哨）：

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ocr llm ⭐ | 140 | 16 | $3.43 | info/comm |
| llm ocr ⭐ | 110 | 20 | $4.21 | info/comm |
| ocr transformer ⭐ | 20 | 0 | $0 | info |

> "ocr llm" / "llm ocr" 是 LLM+OCR 结合的类别词，GOT 的 Qwen decoder 架构与此语义高度契合，是最具 Olares 叙事空间的入口词。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| pdf ocr python ⭐ | 50 | 29 | $0 | info |
| local ocr ⭐ | 30 | 0 | $7.54 | info |
| self hosted ocr ⭐ | 20 | 0 | $0 | info |
| ocr offline ⭐ | 20 | 0 | $0 | info |
| image to text python ⭐ | 50 | 21 | $0 | info |

> "local ocr" CPC $7.54 在零量 KD 词里属于高商业价值信号，值得抢 GEO 位。

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| open source ocr | 260 | 46 | $2.75 | comm |
| easyocr ⭐ | 1,600 | 27 | $2.94 | info/comm |
| surya ocr ⭐ | 210 | 29 | $5.87 | comm |
| ocr open source ⭐ | 110 | 27 | $2.75 | comm |
| best open source ocr | 50 | 39 | $4.02 | comm |
| doctr ocr | 70 | 31 | $4.11 | info |
| aws textract alternative ⭐ | 10 | 0 | $6.67 | comm |
| best open source ocr models ⭐ | 30 | 0 | $0 | comm |

> easyocr（KD 27，月量 1,600）是同赛道开源竞品中流量最高且竞争度最低的词，是文章定题的优质锚点。

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| ocr llm ⭐⭐⭐ | 140 | 16 | $3.43 | GOT 用 Qwen decoder 做 LLM 级 OCR 输出；Olares 可本地部署整个管道，数据不上云 |
| llm ocr ⭐⭐⭐ | 110 | 20 | $4.21 | 同上；KD 极低，适合快速建立 Olares "本地 LLM-OCR" 叙事 |
| local ocr ⭐⭐⭐ | 30 | 0 | $7.54 | 580M 模型 4GB 显存可跑，Olares One 完整支持；强调"图片不出本机" |
| self hosted ocr ⭐⭐ | 20 | 0 | $0 | 自托管叙事：零 API 费、无额度限制、数据隐私；对比 AWS Textract 按页计费 |
| aws textract alternative ⭐⭐ | 10 | 0 | $6.67 | GOT 替代 Textract 基础层；Apache 2.0 免费本地跑，攻 Textract 每千页 $1.5 收费痛点 |
| best ocr models open source ⭐⭐ | 30 | 0 | $0 | Olares 一键部署开源 OCR 模型，GOT 作为 580M 轻量高能之选 |
| ocr offline ⭐⭐ | 20 | 0 | $0 | 离线/离线优先场景：敏感文档（法律/医疗）不可上传公有云 |
| best ocr models ⭐⭐ | 170 | 22 | $2.75 | Listicle 入口词；GOT 凭多任务能力（含公式/表格）在对比文中有差异化 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| got-ocr2.0 | 320 | 31 | $0 | info | 主词候选 | 品牌主词，月量够格，KD 31 可攻；Olares 角度：本地跑 GOT-OCR2.0 教程页的锚词 |
| easyocr | 1,600 | 27 | $2.94 | info/comm | 主词候选 | 同赛道开源竞品，KD 低量大；可做 "GOT-OCR vs EasyOCR" 对比文，借 easyocr 流量引至 Olares |
| aws textract pricing | 720 | 32 | $5.66 | trans | 主词候选 | 高 CPC 高购买意图，直击 Textract 成本痛点；Olares 叙事：本地跑 GOT 彻底免去 API 费 |
| open source ocr | 260 | 46 | $2.75 | comm | 主词候选 | 品类头部词，KD 偏高但商业价值明确；作为入口词可配 GOT-OCR 本地部署内容 |
| best ocr models | 170 | 22 | $2.75 | comm | 主词候选 ⭐ | KD 22 量尚可，listicle 主词；GOT 在公式/表格上有差异化，Olares 可一键部署 |
| ocr llm | 140 | 16 | $3.43 | info/comm | 主词候选 ⭐ | KD 仅 16，GOT 的 LLM-decoder 架构天然命中此词；Olares 叙事：本地运行 LLM-OCR 管道 |
| llm ocr | 110 | 20 | $4.21 | info/comm | 主词候选 ⭐ | 同义词，KD 20，与 ocr llm 同簇；两词并入一篇文章效率最高 |
| surya ocr | 210 | 29 | $5.87 | comm | 次级 ⭐ | 同赛道新兴竞品；可作"开源 OCR 横评"次级词，KD 低 CPC 高说明商业意图强 |
| optical character recognition companies | 210 | 22 | $0 | info | 次级 ⭐ | 行业格局词；KD 仅 22，适合 Olares "开源替代商业 OCR 服务商" 叙事文的次级词 |
| ocr vendors | 110 | 17 | $12.86 | comm | 次级 ⭐ | KD 17 且 CPC $12.86 极高商业信号；Olares 本地方案对标 OCR 服务商采购决策 |
| ocr open source | 110 | 27 | $2.75 | comm | 次级 ⭐ | "open source ocr" 变体；并入同类文章次级词列表 |
| best ocr tool | 110 | 25 | $7.56 | comm | 次级 ⭐ | KD 25 CPC 高；listicle 次级词，GOT 以轻量高能入选 |
| aws textract | 2,900 | 34 | $11.85 | comm | 次级 | 月量大但 KD 34；作为对比文中的竞品主角词，GOT vs Textract 攻击点：免费 + 本地 |
| pdf ocr python | 50 | 29 | $0 | info | 次级 ⭐ | 开发者教程需求，GOT 的 Python 调用极简；适合技术文章次级词 |
| local ocr | 30 | 0 | $7.54 | info | GEO ⭐ | KD 0 CPC 高，Olares 本地 OCR 叙事最直接的入口；抢 AI Overview 位 |
| self hosted ocr | 20 | 0 | $0 | info | GEO ⭐ | 自托管叙事词，与 Olares 定位完全契合 |
| aws textract alternative | 10 | 0 | $6.67 | comm | GEO ⭐ | 战略替代词，KD 0 高 CPC；GOT+Olares = 免费本地 Textract 替代方案，应优先抢 AI 引用位 |
| best ocr models open source | 30 | 0 | $0 | comm | GEO ⭐ | 零竞争品类榜词，GOT 轻量多能应占一席 |
| got ocr | 50 | 30 | $0 | info | GEO | 品牌变体，量小但应有内容覆盖确保自己排名 |
| general ocr theory | 10 | 0 | $0 | info | GEO | 论文/技术词，学术流量，FAQ/直答块覆盖 |

---

## 核心洞见

1. **搜索心智尚在建立**：GOT-OCR2.0 品牌词（got-ocr2.0）月量 320，有基本心智，但远未成气候——同赛道 easyocr 达 1,600、paddle ocr 达 1,900。大量搜索流量集中在"open source ocr"、"best ocr models"等品类词，GOT 尚未进入这些词的主流认知。HuggingFace 1M+ 下载与 GitHub 8k star 表明技术社区认可度远高于自然搜索现状，有追赶空间。

2. **消费级 GPU / Olares One 可跑：叙事成立**：580M 参数，FP16 仅需 4GB VRAM（推荐 6GB+），RTX 3060 / 3070 等消费级显卡均可流畅运行。Olares One 标配 NVIDIA GPU 完全覆盖需求。580M 远小于同赛道 olmOCR（7B），是"不牺牲精度的最轻量化选择"叙事核心。

3. **Apache 2.0 商用友好，可主推**：2024 年 10 月已明确删除旧 README 中"research only"措辞，切换为完整 Apache 2.0。无地区限制，无商业使用附加条款。可在 Olares 内容中直接强调"免费商用、本地部署、零许可费"。

4. **对 Olares 最关键的 2-3 个词**：
   - `ocr llm`（KD 16，月量 140）：GOT 的 LLM-decoder 架构让它天然命中这个上升词；KD 极低，现在建内容可快速占位。
   - `aws textract alternative`（KD 0，CPC $6.67）：战略 GEO 词，攻击 Textract 按页计费痛点，Olares 本地部署= 零变量成本。
   - `local ocr`（KD 0，CPC $7.54）：CPC 高意味着本地部署有真实商业价值，Olares "图片不出本机"叙事天然命中。

5. **GEO 抢发窗口**：GOT-OCR2.0 于 2025 年 2 月才正式合入 HF Transformers，大量组合词（`got ocr tutorial`、`local ocr`、`self hosted ocr`、`aws textract alternative`）在 Semrush 呈零量 or 近零量——正是 AI Overview / Perplexity 引用位的真空期。建议优先产出"Run GOT-OCR2.0 locally"、"GOT-OCR vs AWS Textract"直答内容抢占 GEO 位，而非等自然流量。

6. **闭源对标与攻击面**：
   - **AWS Textract**（KD 34，$11.85 CPC，月量 2,900）：Textract 按文档页数收费（Basic tier ~$0.0015/页），大批量文档处理成本快速累积；GOT+Olares = 一次性部署、无限次调用。
   - **Google Cloud Vision / Azure Document Intelligence**：数据必须上云，对法律/医疗/财务等敏感文档场景是合规障碍；GOT 本地运行天然规避。
   - **Mathpix**（公式识别细分）：Mathpix 订阅制，GOT 的公式识别能力免费本地可跑。

7. **与同类 family 的关联**：与 [PaddleOCR-VL](../paddleocr-vl.md) 同属 08-ocr 章，两者有互补——PaddleOCR-VL 主打 109 语言 OmniDocBench 榜首，GOT-OCR2.0 主打统一多任务（含公式/乐谱/分子式）且更轻量（580M vs 0.9B）。内容层可做横评 listicle（best open source ocr models）将两者同时纳入，共享词流量。`ocr llm` 与 `llm ocr` 这两个低 KD 新兴词，目前 models.md 中无其他模型直接命中，GOT 是最适合的主角。

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch、phrase_related、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
