# EmbeddingGemma 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：Google DeepMind / huggingface.co/google/gemma-embedding-exp-03-27，Gemma Terms of Use（商用需接受 Google 条款）

> **无独立产品页**：EmbeddingGemma 通过 HuggingFace（`google/gemma-embedding-exp-03-27`）和 Ollama 分发；Google 无独立 EmbeddingGemma 产品站，官方入口仅 Google AI blog 与 HF 模型卡。Phase 1 域名报告跳过，SEO 主战场在第三方内容页（HF 模型卡、RAG 教程站、Ollama 文档）。

---

## 模型理解（前置）

EmbeddingGemma 是 Google DeepMind 基于 Gemma 3 架构推出的专用文本嵌入模型（308M 参数），定位**消费级 CPU 可跑的轻量嵌入方案**。<200MB 内存占用使其成为目前大厂出品中 RAM 要求最低的生产级 Embedding 模型之一；MTEB 基准成绩可与 `text-embedding-3-small` 正面对位。通过 Ollama（`ollama pull gemma3-embedding`）可一键本地部署，无需 GPU，是资源受限环境（边缘设备、单节点个人云）的首选 RAG 底座。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Gemma 3 系架构、308M 参数、<200MB RAM、纯 CPU 可跑的生产级文本 Embedding 模型 |
| 许可证 | **Gemma Terms of Use**（商用 OK，但须接受 Google 条款；不可用于训练其他模型；非 Apache/MIT，**不能说"完全开源"**，宜说"免费可商用"） |
| 主仓库 / 分发 | HuggingFace: [google/gemma-embedding-exp-03-27](https://huggingface.co/google/gemma-embedding-exp-03-27)；Ollama: `ollama pull gemma3-embedding`；无独立官网 |
| 参数 / VRAM 可跑性 | 308M 参数；<200MB RAM（FP16 推理）；**CPU 即可满速运行**，无 VRAM 需求；Olares One（RTX 5090 Mobile 24GB + 96GB DDR5）上 Ollama 可零 GPU 开销跑满血推理 |
| 变体 / 型号 | `gemma-embedding-exp-03-27`（当前版本）；无明显 fp4/q4 量化变体公开发布（模型已足够小，GGUF 格式通过社区提供） |
| 闭源对标 | **OpenAI `text-embedding-3-small`**（$0.02/1M tokens，需联网，数据过 OpenAI 服务器）；`text-embedding-005`（Google 云端 API 版）；Cohere Embed v3 |
| Olares Market | Ollama（已上架）支持 `gemma3-embedding`；Dify、AnythingLLM、RAGFlow（均已上架）均内置 Ollama Embedding 配置入口 |
| 来源 | [HF 模型卡](https://huggingface.co/google/gemma-embedding-exp-03-27)、[Google AI Blog](https://ai.google.dev/gemma/docs/gemma-2/text-classification)、[Ollama library](https://ollama.com/library/gemma3-embedding)、[MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| EmbeddingGemma | 320 | 52 | $0 | 信息 |
| embedding gemma | 320 | 43 | $0 | 信息 |
| gemma embedding | 140 | 49 | $0 | 信息 |
| gemma embeddings | 90 | 49 | $0 | 信息 |
| gemma embedding model | 50 | 46 | $0 | 信息 |
| gemma text embedding | 50 | 0 | $0 | — |
| google gemma embedding model | 50 | 0 | $0 | — |
| embedding gemma dimensions ⭐ | 30 | 0 | $0 | 信息 |
| gemma 3 embedding model ⭐ | 30 | 0 | $0 | 信息 |
| google embedding gemma ⭐ | 30 | 0 | $0 | 信息 |
| gemma 3 embedding ⭐ | 20 | 0 | $0 | 信息 |
| embedded gemma ⭐ | 20 | 0 | $0 | — |
| gemma embedding models ⭐ | 20 | 0 | $0 | 信息 |
| what is embedding gemma ⭐ | 10 | 0 | $0 | 信息 |
| gemma 300m embedding ⭐ | 10 | 0 | $0 | 信息 |
| embedding gemma gguf ⭐ | 10 | 0 | $0 | 信息 |
| gemma embedding 2 ⭐ | 10 | 0 | $0 | 信息 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ollama embedding models ⭐ | 390 | 32 | $4.06 | 信息 |
| gemma embedding model ollama ⭐ | 20 | 0 | $0 | 商业 |
| gemma embedding ollama ⭐ | 20 | 0 | $0 | 商业 |
| ollama gemma 3 embedding ⭐ | 20 | 0 | $0 | 商业 |
| lm studio embedding model ⭐ | 40 | 22 | $0 | 信息 |
| lm studio text embedding ⭐ | 40 | 17 | $0 | 信息 |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| best embedding model for rag ⭐ | 140 | 29 | $2.40 | 信息 |
| local embedding model ⭐ | 50 | 27 | $0 | 信息 |
| lightweight embedding model ⭐ | 40 | 23 | $0 | 信息 |
| open source embedding model ⭐ | 30 | 0 | $1.82 | 信息 |
| small embedding model ⭐ | 20 | 0 | $0 | 信息 |
| cpu embedding model ⭐ | 20 | 0 | $0 | 信息 |
| run llm locally without gpu ⭐ | 20 | 0 | $0 | 信息 |
| run embedding model locally ⭐ | 20 | 0 | $0 | 信息 |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| text-embedding-3-small | 3,600 | 20 | $6.96 | 信息 |
| gemini embedding | 390 | 55 | $0 | 信息 |
| gemini embeddings | 390 | 31 | $0 | 信息 |
| google embedding models | 170 | 46 | $6.41 | 信息 |
| text-embedding-005 ⭐ | 90 | 27 | $0 | 信息 |
| google embedding model | 50 | 56 | $7.07 | 信息 |
| embedding gemma vs nomic-embed-text ⭐ | 20 | 0 | $0 | 对比 |
| embedding gemma vs qwen3 embedding ⭐ | 10 | 0 | $0 | 对比 |
| embedding gemma vs nomic embed text ⭐ | 10 | 0 | $0 | 对比 |
| bge-m3 vs embedding gemma ⭐ | 0 | 0 | $0 | 对比 |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| gemma embedding ollama | 20 | 0 | $0 | Olares Market 已上架 Ollama，`ollama pull gemma3-embedding` 一条命令；<200MB RAM 跑 Embedding，GPU 完全留给 LLM——最低资源占用的 Olares RAG 方案 | ⭐⭐⭐ |
| best embedding model for rag | 140 | 29 | $2.40 | Olares 上 Dify / AnythingLLM / RAGFlow 均内置 Ollama Embedding 入口；EmbeddingGemma 是 CPU-only 方案中 MTEB 成绩最强的选项，是 Olares 私有 RAG 的最小化起步方案 | ⭐⭐⭐ |
| ollama embedding models | 390 | 32 | $4.06 | Olares Market Ollama 一键安装，`gemma3-embedding` 作为嵌入端点，CPC $4.06 显示商业价值；覆盖面最广的 Olares Embedding 入口词 | ⭐⭐⭐ |
| local embedding model | 50 | 27 | $0 | 308M 参数 <200MB RAM，消费级 CPU 即可运行；在 Olares One（96GB RAM）上这是极低资源占用，可与 LLM 共存不抢资源 | ⭐⭐⭐ |
| cpu embedding model | 20 | 0 | $0 | EmbeddingGemma 是目前 Ollama 生态中 CPU-only 路线下 MTEB 成绩最强的选项；Olares 场景：无 GPU Olares 实例（如树莓派 5 装 Olares）可独立完成 RAG 向量化 | ⭐⭐⭐ |
| lightweight embedding model | 40 | 23 | $0 | KD 23 可竞争，<200MB RAM 是本词的最佳 landing anchor；Olares 叙事：最轻量的企业级 Embedding，Olares 的边缘用例（受限节点、低功耗 ARM）首选 | ⭐⭐⭐ |
| text-embedding-3-small | 3,600 | 20 | $6.96 | 闭源对标，量大 KD 低；EmbeddingGemma 是其本地自托管平替——在 Olares 上零成本、数据不出本机、消除 per-token 账单 | ⭐⭐⭐ |
| open source embedding model | 30 | 0 | $1.82 | CPC $1.82 有商业信号，KD 0；Gemma Terms 不是 Apache/MIT 但可免费商用自托管；Olares 叙事：在自己的硬件跑 Google 品质 Embedding，无需支付 API 费用 | ⭐⭐ |
| run embedding model locally | 20 | 0 | $0 | 部署意图纯；EmbeddingGemma + Ollama = 最简 CPU-only 本地 Embedding 路径；Olares Market 一键 Ollama 将部署门槛降到零 | ⭐⭐ |
| run llm locally without gpu | 20 | 0 | $0 | 最直接的 GPU-free 本地 AI 意图词；EmbeddingGemma 是证明 Olares 在无 GPU 场景下也能完整跑 RAG 的最佳例证 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| text-embedding-3-small | 3,600 | 20 | $6.96 | 信息 | 主词候选 | 闭源对标绝对主词，KD 20 可竞争，CPC $6.96 商业信号强；EmbeddingGemma 是其本地替代——Olares 上零成本、数据不出本机 |
| ollama embedding models ⭐ | 390 | 32 | $4.06 | 信息 | 主词候选 | 量 390、KD 32、CPC $4.06，是 Ollama 生态 Embedding 品类词；Olares Market Ollama 一键安装是最直接落点 |
| best embedding model for rag ⭐ | 140 | 29 | $2.40 | 信息 | 主词候选 | 量 140、KD 29、CPC $2.40，ROI 最高的场景词；EmbeddingGemma 是 CPU-only RAG 链路首选，Olares 上 Dify + Ollama 全链路私有 RAG |
| EmbeddingGemma | 320 | 52 | $0 | 信息 | 主词候选 | 品牌主词，KD 52 偏高但为自有名称，应出现在所有 EmbeddingGemma 相关内容；Olares 角度：本地部署入口词 |
| embedding gemma | 320 | 43 | $0 | 信息 | 主词候选 | 品牌词变体，KD 43；量与 EmbeddingGemma 并列，可合并覆盖；同族合计 ~1,300+/月 |
| gemma embedding | 140 | 49 | $0 | 信息 | 次级 | 品牌词变体，KD 偏高，并入主词文章 |
| gemma embeddings | 90 | 49 | $0 | 信息 | 次级 | 变体，并入主词文章 |
| local embedding model ⭐ | 50 | 27 | $0 | 信息 | 次级 | 本地部署意图词，KD 27；EmbeddingGemma <200MB RAM 是本词最佳 anchor |
| lightweight embedding model ⭐ | 40 | 23 | $0 | 信息 | 次级 | KD 23，<200MB RAM 竞争力绝对；Olares 边缘/ARM 用例的自然词 |
| lm studio embedding model ⭐ | 40 | 22 | $0 | 信息 | 次级 | KD 22 极低；LM Studio 是本地 AI 同类工具，可联合覆盖"本地 Embedding 工具"意图 |
| gemma embedding model ollama ⭐ | 20 | 0 | $0 | 商业 | 次级 | 引擎组合词，KD 0；Olares 教程的自然次级词，意图明确 |
| gemma embedding ollama ⭐ | 20 | 0 | $0 | 商业 | 次级 | 同上，拼写变体，并入教程内容 |
| cpu embedding model ⭐ | 20 | 0 | $0 | 信息 | GEO 前哨 | KD 0，GPU-free RAG 意图最纯；GEO 直答块：EmbeddingGemma = 最佳 CPU-only Embedding 模型 |
| run embedding model locally ⭐ | 20 | 0 | $0 | 信息 | GEO 前哨 | KD 0，部署意图；GEO 抢占"how to run embedding locally"直答位 |
| open source embedding model ⭐ | 30 | 0 | $1.82 | 信息 | GEO 前哨 | CPC $1.82 商业信号，KD 0；GEO 直答块：EmbeddingGemma = 最快可用的免费本地 Embedding 方案 |
| embedding gemma vs nomic-embed-text ⭐ | 20 | 0 | $0 | 对比 | GEO 前哨 | KD 0，直接对比词；GEO 先占两者差异直答（nomic=Apache 2.0 + 多语言 MoE；EmbeddingGemma=更小、Google 品质、CPU 更快） |
| embedding gemma vs qwen3 embedding ⭐ | 10 | 0 | $0 | 对比 | GEO 前哨 | KD 0；两份报告（07-embedding）联合 GEO，覆盖"哪个小模型做 RAG 更好"问题 |
| small embedding model ⭐ | 20 | 0 | $0 | 信息 | GEO 前哨 | KD 0；边缘/资源受限 RAG 场景；EmbeddingGemma 308M 参数是目前 MTEB 强模型中参数最少之一 |
| text-embedding-005 ⭐ | 90 | 27 | $0 | 信息 | 次级 | Google 云端 Embedding API，KD 27；EmbeddingGemma 是其本地自托管对应方案，可并入对比文 |
| run llm locally without gpu ⭐ | 20 | 0 | $0 | 信息 | GEO 前哨 | KD 0；EmbeddingGemma 是 GPU-free 本地 AI 叙事的最强 Embedding 例证，Olares ARM/CPU 用例的锚点 |
| embeddinggemma benchmark performance review | 110 | 38 | $0 | 信息 | 次级 | 量 110，KD 38；MTEB 评测词，可作为 EmbeddingGemma 介绍文章的次级词 |

---

## 核心洞见

**1. 搜索心智初建，品牌词量在 300-400/月但 KD 偏高**

`EmbeddingGemma`/`embedding gemma` 各有 320 vol/月，同族（含 gemma embedding/gemma embeddings 等）合计约 1,200-1,300/月——对一个纯技术嵌入模型来说量不低，但 KD 43-52 相对其体量偏高，说明 Google 品牌带来了竞争度加持。关键词的下游（型号变体词、部署词、GGUF、ollama 组合词）KD 全部为 0，是标准的**品牌认知已初建、内容生态尚未成熟**格局——内容填空机会最大。

**2. CPU-only 是核心叙事，Olares 场景成立无需任何条件**

EmbeddingGemma 308M 参数、<200MB RAM，无 VRAM 需求，**任何 Olares 节点（含树莓派 5、ARM Linux、无 GPU x86）都能运行**，不依赖 Olares One 的 RTX 5090。这是 07-embedding 已有三份报告（BGE-M3、Nomic、Qwen3-Embedding）中 RAM 最低、CPU 场景最纯的一款——叙事成立最简单，写"GPU-free RAG on Olares"直接以此为 anchor。

**3. Gemma Terms ≠ Apache/MIT，写作口径需留意**

Gemma Terms of Use 允许商用，但需接受 Google 条款，且明确**不允许用于训练其他生成模型**。内容口径：可写"免费可商用、可本地自托管"，但不能写"完全开源 Apache 2.0"。竞品对比中可强调"数据不出本机"而非许可证宽松度。这与同类报告的 Apache/MIT 叙事有差异，需分开处理。

**4. 对 Olares 最关键的 3 个词**

- `best embedding model for rag`（140 vol, KD 29, CPC $2.40）：高 ROI 场景词，Olares 私有 RAG 链路叙事的核心入口，EmbeddingGemma 是 CPU-only 路线下成绩最强选项
- `ollama embedding models`（390 vol, KD 32, CPC $4.06）：Ollama 生态品类词，量最大、CPC 有商业价值；Olares Market 安装教程自然落点
- `text-embedding-3-small`（3,600 vol, KD 20, CPC $6.96）：闭源对标主词，`text-embedding-3-small alternative` / `text-embedding-3-small local` 是内容切入点——EmbeddingGemma 是其零成本、零 API 依赖的本地替代

**5. GEO 抢发窗口——部署词与对比词均 KD 0**

EmbeddingGemma 发布于 2025 年初，搜索量仍在爬坡期，大量型号词、部署词、对比词 KD 全为 0，是完整的 GEO 抢发窗口：
- `cpu embedding model`、`run embedding model locally`（各 20 vol, KD 0）：GPU-free RAG FAQ 直答
- `embedding gemma vs nomic-embed-text`（20 vol, KD 0）：两大轻量 Embedding 直接对比，GEO 先占
- `embedding gemma vs qwen3 embedding`（10 vol, KD 0）：中文/英文场景对比，跨两份报告联合
- `small embedding model`（20 vol, KD 0）：品类词 GEO，EmbeddingGemma 308M = 当前最小高质量选项之一
- `embedding gemma gguf`（10 vol, KD 0）：社区量化版词，GGUF 用户群体搜索

**6. 闭源攻击面**

主要竞品：
- **OpenAI `text-embedding-3-small`**（3,600 vol）：$0.02/1M tokens，数据强制过 OpenAI 服务器，无离线模式；EmbeddingGemma 替代叙事：**零 API 费用、数据不出本机、CPU 即可运行**，适合任何 GDPR/隐私敏感的 RAG 场景
- **Google `text-embedding-005`**（90 vol, KD 27）：Google 自家云端版，按量计费；EmbeddingGemma 是其本地自托管对应方案，攻击面：账单不可控 vs. 本地零成本
- **Gemini Embeddings**（390 vol）：Google 旗下较新的云端嵌入系列，闭源；EmbeddingGemma 是其开放的本地对应方案，适合不想依赖云 API 的用户

**7. 与 07-embedding 已有报告的关联**

EmbeddingGemma 是 07-embedding 第四份报告，与已有三份形成完整的对比矩阵：

| 模型 | 许可证 | 参数规模 | CPU 可跑性 | 多语言 | Ollama 支持 |
|------|--------|---------|-----------|-------|------------|
| EmbeddingGemma | Gemma Terms（商用 OK） | 308M，<200MB RAM | ⭐⭐⭐ 最优 | 支持（多语言 MTEB 良好） | ✅ |
| Nomic Embed v2 | Apache 2.0 | 475M，328MB Q4 | ⭐⭐ | 100+ 语言，MoE 架构 | ✅ |
| BGE-M3 | MIT | 570M+ | ⭐ 偏重 | 100+ 语言，8192 token | ✅ |
| Qwen3-Embedding | Apache 2.0 | 0.6B/4B/8B | ⭐⭐ | 中文优先、多语言 | 部分支持 |

内容层：`embedding gemma vs nomic-embed-text`（20 vol, KD 0）和 `embedding gemma vs qwen3 embedding`（10 vol, KD 0）是两个现成的跨报告 GEO 簇切入点——"最小 CPU 部署 vs. 最开放许可 vs. 最强中文"对比文可跨 4 份报告取词。

---

*数据来源：SEMrush US（phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
