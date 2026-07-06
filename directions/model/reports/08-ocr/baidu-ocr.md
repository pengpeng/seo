# Unlimited-OCR (Baidu) 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：baidu/Unlimited-OCR（github.com/baidu/Unlimited-OCR），MIT

## 模型理解（前置）

> **无独立官网**，SEO 主战场在 GitHub / HuggingFace / 社区内容页。

Unlimited-OCR 是百度于 2026 年 6 月 18 日发布的开源端到端视觉语言 OCR 模型，核心卖点是"一次前向传播解析 40+ 页文档"（One-shot Long-horizon Parsing）。它基于 DeepSeek-OCR checkpoint 继续训练，用自研的 **Reference Sliding Window Attention（R-SWA）**替换解码器中的 MHA，使 KV cache 在整个生成过程中保持恒定——彻底解决了长文档 OCR 因 KV cache 线性增长导致的内存爆炸与速度下降问题。采用 MIT 许可，商用完全自由，原生支持 vLLM、SGLang、Ollama、llama.cpp、HuggingFace Transformers 五大引擎，部署路径与 DeepSeek-OCR 生态完全兼容。发布三周内 GitHub Stars 超 13,000，显示社区热度极高。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 端到端 OCR VLM，40+ 页单次解析，对标 Mistral OCR 的开源平替 |
| 许可证 | **MIT**——最宽松商用许可，无地区限制，可作为 Olares 主推卖点 |
| 主仓库 / 分发 | [GitHub baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)（★13,370，2026-07）；[HuggingFace baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)；[ModelScope PaddlePaddle/Unlimited-OCR](https://modelscope.cn/models/PaddlePaddle/Unlimited-OCR)；[Baidu Cloud](https://cloud.baidu.com/doc/OCR/s/fmr1p39gb) |
| 参数 / VRAM 可跑性 | **3B 总参数 / 0.5B 激活**（MoE，同 DeepSeek-OCR 架构）；BF16 推理 ~7.3 GB VRAM、INT8 ~3.6 GB、INT4 ~1.8 GB；需要 NVIDIA CUDA GPU（官方要求 CUDA 12.9+，CC≥8 即 RTX 3060+）；llama.cpp GGUF Q4 可纯 CPU 运行（30-60 s/页）；MLX 8-bit 支持 Apple Silicon ≥8 GB。**Olares One（RTX 5090 Mobile 24 GB）BF16 全精度运行无压力，单 GPU 即可批量处理长文档** |
| 变体 / 型号 | Unlimited-OCR（3B-A0.5B，BF16，当前唯一官方权重）；GGUF 量化（社区：Q4_K_M ~3.5 GB、Q8_0 ~5.5 GB）；NVFP4（~4 GB VRAM）；MLX 8-bit（Apple Silicon 专项） |
| 闭源对标 | **Mistral OCR**（API 按页计费，无自托管）；Google Document AI（数据上云）；AWS Textract（按页付费）；Azure Document Intelligence（订阅制）；Adobe Acrobat AI（月费） |
| Olares Market | 未独立上架；可通过 Ollama（Olares Market 已上架）一键部署；vLLM/SGLang 官方 Docker 镜像可在 Olares 容器内直接运行 |
| 来源 | [GitHub README](https://github.com/baidu/Unlimited-OCR)（2026-07）；[Technical Report arXiv:2606.23050](https://arxiv.org/html/2606.23050)；[AI Weekly 报道](https://aiweekly.co/alerts/baidu-releases-mit-licensed-3b-ocr-model-for-long-documents)；[Spheron VRAM 数据](https://www.spheron.network/tools/gpu-recommender/baidu/Unlimited-OCR/)；[vLLM Recipe](https://recipes.vllm.ai/baidu/Unlimited-OCR) |

---

## 关键词扩展（Phase 2）

> **无独立官网，跳过 Phase 1 域名流量分析。** 品牌词"unlimited ocr"/ "baidu unlimited ocr"当前 US 搜索量为零（模型刚发布 3 周），所有词均为 GEO 前哨或借力竞品/父模型词。

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| deepseek ocr | 3,600 | 49 | $4.94 | 信息 |
| deepseek-ocr-2 | 1,900 | 32 | $0 | 信息 ⭐ |
| deepseek-ocr 2 | 1,600 | 25 | $4.61 | 信息 ⭐ |
| deepseek ocr 2 | 390 | 32 | $4.61 | 信息 ⭐ |
| deepseek ocr model | 110 | 43 | $3.63 | 信息 |
| baidu ocr | 20 | 0 | $13.24 | 信息 ⭐ |
| unlimited ocr | 0 | — | — | — |
| baidu unlimited ocr | 0 | — | — | — |

> **说明**：Unlimited-OCR 品牌词当前 US 量为零——模型发布于 2026-06-18，尚未形成搜索心智。与其父模型 DeepSeek-OCR（3,600/月）相比，流量差距悬殊。`deepseek-ocr 2`（KD 25）是最佳进入点。

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ollama ocr | 140 | 36 | $3.31 | 信息 |
| ocr llm | 140 | 16 | $3.43 | 信息 ⭐ |
| deepseek ocr ollama | 70 | 22 | $0 | 信息 ⭐ |
| deepseek ocr api | 210 | 48 | $4.47 | 信息 |
| ollama ocr model | 20 | 0 | $0 | 信息 ⭐ |
| unlimited ocr ollama | 0 | — | — | — |
| unlimited ocr vllm | 0 | — | — | — |

> **说明**：`deepseek ocr ollama`（70/月，KD 22）是最具价值的引擎组合词——Unlimited-OCR 与 DeepSeek-OCR 均原生支持 Ollama，可以同一文章覆盖两个模型。`ocr llm`（140/月，KD 16）竞争极低，是技术科普内容的绝佳切入点。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ocr for pdf | 880 | 50 | $1.40 | 信息 |
| pdf text extraction | 590 | 33 | $1.00 | 信息 ⭐ |
| document parsing | 140 | 30 | $12.82 | 信息 ⭐ |
| open source pdf ocr | 40 | 37 | $1.70 | 信息 |
| on premise ocr | 50 | 39 | $11.95 | 信息/商业 |
| pdf ocr python | 50 | 29 | $0 | 信息 ⭐ |
| local ocr | 30 | 0 | $7.54 | 信息 ⭐ |
| self hosted ocr | 20 | 0 | $0 | 信息 ⭐ |
| open source document ai | 20 | 0 | $0 | 信息 ⭐ |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| mistral ocr | 1,900 | 39 | $5.26 | 导航 |
| mistral ocr api | 260 | 37 | $4.55 | 导航/商业 |
| mistral ocr pricing | 210 | 46 | $6.95 | 商业 |
| open source ocr | 260 | 46 | $2.75 | 信息 |
| mistral ocr alternative | 20 | 0 | $5.55 | 信息 ⭐ |
| deepseek ocr alternative | 0 | — | — | — |
| unlimited ocr vs mistral ocr | 0 | — | — | — |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|-------|
| self hosted ocr | 20 | 0 | $0 | Unlimited-OCR MIT 许可 + Olares 一键部署 = 完整自托管 OCR 栈，文档永不离本机 | ⭐⭐⭐ |
| local ocr | 30 | 0 | $7.54 | CPC $7.54 说明商业意图；"在 Olares One 上本地跑 Unlimited-OCR，RTX 5090 Mobile 24 GB，BF16 全精度秒处理整本 PDF" | ⭐⭐⭐ |
| mistral ocr alternative | 20 | 0 | $5.55 | 精准对标词：Unlimited-OCR 是免费开源的 Mistral OCR 替代，Olares 提供 one-click 部署，彻底告别 API 账单 | ⭐⭐⭐ |
| document parsing | 140 | 30 | $12.82 | 高 CPC 说明企业级需求；Olares + Unlimited-OCR 构建本地文档解析管线，数据不出内网 | ⭐⭐⭐ |
| mistral ocr pricing | 210 | 46 | $6.95 | 用户在查定价时就是买/不买的关键节点；切入"$0 per page with Unlimited-OCR on Olares" | ⭐⭐⭐ |
| deepseek ocr ollama | 70 | 22 | $0 | 低 KD 高机会：Unlimited-OCR 与 DeepSeek-OCR 同生态，Ollama 已在 Olares Market，一键可跑 | ⭐⭐⭐ |
| ollama ocr | 140 | 36 | $3.31 | Ollama 是最低摩擦的本地 OCR 部署路径；Olares Market 已有 Ollama，Unlimited-OCR 可直接 pull | ⭐⭐⭐ |
| ocr llm | 140 | 16 | $3.43 | KD 仅 16，技术科普好机会；定位 Unlimited-OCR 为"OCR + LLM 融合方案"，Olares 本地跑无 GPU 云费 | ⭐⭐⭐ |
| on premise ocr | 50 | 39 | $11.95 | 企业/合规场景，Olares 私有部署 Unlimited-OCR，满足 GDPR/数据主权要求 | ⭐⭐ |
| pdf text extraction | 590 | 33 | $1.00 | 通用需求词 KD 低；Unlimited-OCR 单次处理整个 PDF 效率远超逐页 OCR 工具 | ⭐⭐ |
| deepseek ocr-2 | 1,900 | 32 | $0 | Unlimited-OCR 是 DeepSeek-OCR 的进化版，借 DeepSeek-OCR 2 流量写"Unlimited-OCR vs DeepSeek-OCR 2"对比文 | ⭐⭐ |
| open source document ai | 20 | 0 | $0 | GEO 精准词，Unlimited-OCR = 开源 Document AI 替代，Olares 是运行宿主 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|-----|------|------|--------------------------|
| mistral ocr | 1,900 | 39 | $5.26 | 导航 | 主词候选 | 最核心对标词，量大 KD 中等；写"open source mistral ocr alternative"切入，Olares 提供免费本地部署 |
| deepseek ocr | 3,600 | 49 | $4.94 | 信息 | 主词候选 | 父模型词，量最大但 KD49 偏高；借势写"Unlimited-OCR：DeepSeek-OCR 的长文档进化版"角度 |
| deepseek-ocr-2 | 1,900 | 32 | $0 | 信息 | 主词候选 | KD 32 可攻；写 Unlimited-OCR 与 DeepSeek-OCR 2 对比，Olares One 本地跑两个模型做实测 ⭐ |
| deepseek-ocr 2 | 1,600 | 25 | $4.61 | 信息 | 主词候选 | KD 最低（25）+ 量大，最易排名的高流量词；Unlimited-OCR 文章的天然次级入口 ⭐ |
| mistral ocr api | 260 | 37 | $4.55 | 导航/商业 | 次级 | 有商业意图（查 API 定价）；切入"自托管替代 Mistral OCR API = $0/月" |
| mistral ocr pricing | 210 | 46 | $6.95 | 商业 | 次级 | CPC 高，定价词说明买意愿；Olares + Unlimited-OCR 免费对比 Mistral 收费 |
| deepseek ocr api | 210 | 48 | $4.47 | 信息 | 次级 | 用户在找 API 部署方案；Unlimited-OCR 原生支持 vLLM OpenAI 兼容接口，Olares 本地 API server |
| ocr for pdf | 880 | 50 | $1.40 | 信息 | — | KD 50，量大但竞争偏高，不建议直接攻 |
| pdf text extraction | 590 | 33 | $1.00 | 信息 | 次级 | KD 33 可作 Unlimited-OCR 应用场景文章的次级词 ⭐ |
| ollama ocr | 140 | 36 | $3.31 | 信息 | 次级 | 技术部署词；Olares Market 已有 Ollama，写"Run OCR locally with Ollama on Olares" ⭐ |
| ocr llm | 140 | 16 | $3.43 | 信息 | 次级 | KD 仅 16！技术类词中最低 KD，Unlimited-OCR 作为"OCR meets LLM"代表案例 ⭐ |
| deepseek ocr ollama | 70 | 22 | $0 | 信息 | 次级 | KD 22 低，Unlimited-OCR + Ollama 是相同部署路径，可同时覆盖两词 ⭐ |
| document parsing | 140 | 30 | $12.82 | 信息 | 次级 | CPC 高（企业级需求），KD 30 可攻；Unlimited-OCR + Olares 构建本地解析管线 ⭐ |
| on premise ocr | 50 | 39 | $11.95 | 商业 | 次级 | 高 CPC 企业合规词；Olares on-premise + Unlimited-OCR 本地推理 |
| baidu ocr | 20 | 0 | $13.24 | 信息 | GEO | KD=0，CPC $13.24（最高！），极精准品牌词；"Baidu open source OCR on Olares"内容 GEO 布局 ⭐ |
| mistral ocr alternative | 20 | 0 | $5.55 | 信息 | GEO | KD=0，明确替代意图；GEO 首选，Unlimited-OCR MIT 免费 vs Mistral OCR 付费 API ⭐ |
| self hosted ocr | 20 | 0 | $0 | 信息 | GEO | 完美 Olares 场景词，量小但与品牌叙事 100% 契合 ⭐ |
| local ocr | 30 | 0 | $7.54 | 信息 | GEO | CPC $7.54 商业意图；"local OCR with Unlimited-OCR on Olares"GEO 布局后随隐私法规趋势增量 ⭐ |
| open source document ai | 20 | 0 | $0 | 信息 | GEO | Google Document AI 开源替代，精准意图，Olares 本地运行 ⭐ |
| unlimited ocr | 0 | — | — | — | GEO | 品牌词当前零量；GEO 抢发，等搜索心智建立后收割 ⭐ |

---

## 核心洞见

### 1. 搜索心智是否建立

**尚未建立**——"unlimited ocr"和"baidu unlimited ocr"当前美国搜索量均为零。模型发布于 2026-06-18，距今不足 3 周，GitHub 已有 13,000+ Star 但尚未转化为主动搜索需求。

对比：父模型 DeepSeek-OCR 品牌词已有 3,600/月，其 2 代变体词（deepseek-ocr 2、deepseek-ocr-2）合计约 3,500/月，且 KD 在 25-32 之间——这是**目前最佳的借势入口**：写"Unlimited-OCR：DeepSeek-OCR 的长文档进化版"型文章，既截获 DeepSeek-OCR 流量，又为 Unlimited-OCR 品牌词预埋 GEO 内容。

### 2. 能否在消费级 GPU / Olares One 本地跑？ ✅

- **BF16（7.3 GB VRAM）**：Olares One（RTX 5090 Mobile 24 GB）轻松运行，单 GPU 可大批量并行处理多页文档
- **INT4（~1.8 GB VRAM）**：消费级 RTX 3060/4060 Ti（8 GB）即可运行量化版
- **CPU（GGUF Q4）**：无 GPU 用户也可跑，速度 30-60 秒/页，适合低频使用
- **Apple Silicon MLX 8-bit（~8 GB）**：8 GB M 系芯片也可跑，但苹果用户无法使用 Olares GPU 加速（苹果 GPU 不受 Olares GPU 加速支持）

**叙事成立度极高**：Olares One 24 GB 远超需求，可强调"批量处理整本 PDF，RTX 5090 Mobile 加持，单次前向传播解析 40+ 页"。

### 3. 许可证是否商用友好？ ✅ 强力主推卖点

MIT 许可，是最宽松的开源许可之一：可商用、可修改、可分发、可集成商业产品，仅需保留版权声明。无地区限制（对比同厂商 PaddleOCR 部分变体有 ARM 限制，Unlimited-OCR 无此限制）。

**直接写进文案**："MIT 许可，$0 per page，文档永不离本机——Unlimited-OCR on Olares vs. Mistral OCR API。"

### 4. 对 Olares 最关键的 2-3 个词

1. **`deepseek-ocr 2`（1,600/月，KD 25，CPC $4.61）**：当前可排名的最高流量词。Unlimited-OCR 是 DeepSeek-OCR 的进化版，文章写"Unlimited-OCR 与 DeepSeek-OCR 2 对比：长文档场景谁更快"，在 Olares One 上做真实测试，对两个词同时命中。
2. **`ocr llm`（140/月，KD 16，CPC $3.43）**：**KD 仅 16**，是整个 OCR 词库中竞争最低的有量词；Unlimited-OCR 完美契合"OCR 遇上 LLM"叙事，Olares 是本地跑这种 LLM-OCR 融合模型的最优宿主。
3. **`mistral ocr`（1,900/月，KD 39）+ `mistral ocr alternative`（20/月，KD 0）**：前者是流量入口词，后者是精准替代意图词。组合攻法：写"Mistral OCR Alternative: Run Unlimited-OCR Free on Olares"，同时覆盖两词。

### 5. 新模型 GEO 抢发窗口

Unlimited-OCR 是 2026 年 6 月最热的新开源 OCR 模型（GitHub 13K Stars，3 周内），AI Overview / Perplexity 对这类新模型的引用窗口通常在发布后 4-8 周内最活跃，**现在正是最佳抢发时机**：

- `unlimited ocr`（0/月，KD —）——建立品牌词 GEO 锚点，AI 搜索引擎引用后可快速积累权重
- `baidu ocr`（20/月，KD 0，CPC $13.24）——有量有意图，写"Baidu's Open Source OCR Model"内容即可命中
- `mistral ocr alternative`（20/月，KD 0，CPC $5.55）——替代意图明确，Unlimited-OCR MIT 免费 vs Mistral API 付费是天然对比角度
- `self hosted ocr`（20/月，KD 0）& `local ocr`（30/月，KD 0，CPC $7.54）——Olares 自托管叙事的精准落点，随隐私法规收紧搜索量将增长
- `open source document ai`（20/月，KD 0）——Google Document AI 开源替代意图，Unlimited-OCR 切入完美

### 6. 闭源对标与攻击面

| 闭源对手 | 月量 | KD | 主要攻击面 |
|---------|------|----|-----------|
| Mistral OCR | 1,900 | 39 | API-only，无法本地部署，数据上云；Unlimited-OCR MIT 免费本地跑，$0/页 |
| Google Document AI | 1,600（"document ai"词） | 73 | 数据上 Google 服务器，GDPR/数据主权压力；Unlimited-OCR 本地推理规避 |
| AWS Textract | 2,900 | 34 | 按页计费（$1.5/千页起）；Unlimited-OCR Olares 本地运行彻底零 API 成本 |
| Azure Document Intelligence | 390（"azure form recognizer"词） | 50 | 月费订阅，超额计费；本地无限制批量处理 |

**通用攻击文案**："$0 per page. Process 40+ pages in one shot. Documents never leave your machine. Unlimited-OCR on Olares vs. cloud OCR APIs."

### 7. 与同类 family 及关键词关联

- 与 [PaddleOCR-VL](./paddleocr-vl.md)（同在 08-ocr 目录）互补：PaddleOCR-VL 走文档理解/版面识别路线，Unlimited-OCR 走长文档高吞吐路线；可合写"Best Open Source OCR 2026: Unlimited-OCR vs PaddleOCR-VL"，覆盖 `paddleocr`（2,900/月）+ `deepseek-ocr`（3,600/月）两大词群
- 与 DeepSeek-OCR 关系深度绑定（技术上直接 finetune 自 DeepSeek-OCR checkpoint）；`deepseek ocr ollama`（70/月，KD 22）可同时覆盖两个模型
- 与 [BGE-M3](../07-embedding/)、[Nomic Embed](../07-embedding/) 构成 RAG 前处理链：Unlimited-OCR 解析文档 → Embedding 向量化 → 本地 LLM 推理，全链路可在 Olares 本地跑
- `ocr llm`（140/月，KD 16）是整合叙事的绝佳词：Unlimited-OCR 本身就是"LLM 驱动的 OCR"，可写技术科普内容作为整个 Olares AI 文档管线的入口文章

---

*数据来源：SEMrush US（phrase_these、phrase_this、phrase_fullsearch、phrase_related）| 2026-07-06*
*技术事实来源：[GitHub baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)（2026-07-03 last push）；[arXiv:2606.23050 Technical Report](https://arxiv.org/html/2606.23050)；[AI Weekly](https://aiweekly.co/alerts/baidu-releases-mit-licensed-3b-ocr-model-for-long-documents)；[Spheron GPU Recommender](https://www.spheron.network/tools/gpu-recommender/baidu/Unlimited-OCR/)；[vLLM Recipe](https://recipes.vllm.ai/baidu/Unlimited-OCR)；[aimadetools 本地部署指南](https://www.aimadetools.com/blog/how-to-run-baidu-unlimited-ocr-locally/)*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
