# 开源 Embedding / Reranker（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 14 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 71%

## 摘要

面向 Olares 本地 RAG / 向量检索，2026 年"接近 SOTA、且能在自有硬件上跑"的开源文本 Embedding 已足够成熟，可全面替代 OpenAI / Cohere / Gemini 的闭源 Embedding API。三条主线清晰：

- **质量优先 / 主推**：**Qwen3-Embedding**（0.6B / 4B / 8B，Apache 2.0），8B 于 2025-06-05 在 MTEB multilingual 排名 No.1（均分 70.58），且同系配套 **Qwen3-Reranker**，是自部署最省心的一条龙方案。[1][2][3][5]
- **端侧 / 手机级**：Google **EmbeddingGemma-300m**（308M，量化后 <200MB RAM，2K 上下文），官称"<500M 参数下 MTEB 最高的开源多语言模型"，专为离线设备 RAG 设计。[6][7]
- **多语言 + 混合检索生产首选**：BAAI **BGE-M3**（1024 维 / 8192 上下文 / MIT），单模型同时给 dense + sparse + multi-vector（ColBERT）三种向量，配 **bge-reranker-v2-m3** 组成官方推荐的 hybrid + rerank 流水线。[9][10]

对 Olares 而言，Embedding/Reranker 是"本地推理 + 本地 RAG"叙事的关键零件：数据不出设备、无按量 API 费、可离线，恰是隐私云 OS 的天然卖点。

## 1. 型号总表（核心交付）

| 模型 | 代表型号 / 参数量 | 部署层级 | 许可 | 闭源对标 | 候选关键词 |
|------|------------------|---------|------|---------|-----------|
| **Qwen3-Embedding** | 0.6B(1024维) / 4B(2560维) / **8B(4096维, MTEB 70.58 No.1)**；32K 上下文 [2][3][5] | 📱0.6B / 💻4B / 🏢8B | Apache 2.0 | text-embedding-3-large / Gemini Embedding | `qwen3 embedding`、`qwen3 embedding local`（低竞争推测） |
| **Qwen3-Reranker** | 0.6B / 4B / 8B，cross-encoder，32K [3] | 💻0.6B–4B / 🏢8B | Apache 2.0 | Cohere Rerank | `qwen3 reranker`（低竞争推测） |
| **EmbeddingGemma** | 308M，768维(MRL→128)，2K 上下文，<200MB RAM [6][7] | 📱手机/边缘 | Gemma 条款（允许商用） | text-embedding-3-small | `embeddinggemma`、`on-device embedding`、`offline RAG`（低竞争推测） |
| **BGE-M3** | ~0.6B，1024维，8192 上下文，dense+sparse+ColBERT [9] | 💻本地主力 | MIT | text-embedding-3-large / Cohere Embed v3 | `bge-m3`（4,400/mo, KD=32, CPC $9.32）、`bge m3 rag`＊ |
| **bge-reranker-v2-m3** | cross-encoder，多语言，基于 bge-m3 [10] | 💻本地主力 | MIT/Apache | Cohere Rerank | `bge reranker`、`bge-reranker-v2-m3`（低竞争推测） |
| **Nomic Embed Text v2** | ~0.5B，MoE，~100 语言 [12][14] | 📱边缘 | Apache 2.0 | text-embedding-3-small | `nomic embed`、`nomic embed alternative`（低竞争推测） |
| **GTE-Qwen2-7B-instruct** | ~7B，MTEB ≈70.2 [11][12] | 🏢大模型 | Apache 2.0 | text-embedding-3-large | `gte-qwen2`（低竞争推测） |
| **E5-Mistral-7B-instruct** | ~7B，长文档强 [12][13] | 🏢大模型 | MIT | text-embedding-3-large | `e5 mistral embedding`（低竞争推测） |
| **Stella-en-1.5B-v5** | ~1.5B，英文强，MTEB ≈69.4 [12] | 💻本地主力 | MIT | text-embedding-3-large | `stella embedding`（低竞争推测） |
| **NV-Embed-v2** | ~7B，英文 SOTA ≈72 [11][12] | 🏢大模型 | **CC-BY-NC（非商用）** | text-embedding-3-large | 慎用（许可受限） |
| **KaLM-Embedding-Gemma3-12B** | ~11.76B，MMTEB 天花板 ≈72.3 [11] | 🏢大模型 | 社区许可 | Gemini Embedding | `kalm embedding`（低竞争推测） |
| **mxbai-embed-large-v1** | ~0.3B，英文轻量 [12] | 📱边缘 | Apache 2.0 | text-embedding-3-small | `mxbai embed`（低竞争推测） |

＊`bge m3` 数据来自本仓库 [models.md](/Users/pengpeng/seo/directions/model/models.md) 快照（带横线写法量约为不带的 7.5×，标题统一用 `bge-m3`）。其余型号词竞争度为定性推测，未做 Semrush 核验。
部署层级：📱手机/边缘（超轻量 CPU / 量化可跑）｜💻本地台式（主力）｜🏢大模型（7B+，需较强 GPU/显存）。

## 2. 分层解读（Embedding vs Reranker；多语言 / MTEB）

**Embedding vs Reranker 的分工**：Embedding 是 bi-encoder，把 query 与文档各自映射成向量做粗召回（快、可预建索引）；Reranker 是 cross-encoder，把 query+文档拼在一起精算相关性分，精度更高但只能对候选做重排。BAAI 官方与 Qwen 都推荐"**hybrid retrieval（dense+sparse）粗召回 → reranker 精排**"的二段式流水线，这正是 Olares 本地 RAG 的标准架构。[9][10]

**📱 手机 / 边缘级**：**EmbeddingGemma-300m** 是最正统选择——308M、量化后 <200MB RAM、EdgeTPU 上 <22ms、2K 上下文、100+ 语言，官方生态覆盖 llama.cpp / Ollama / MLX / LiteRT / transformers.js / LM Studio，专为离线设备 RAG 打造。[6][7] **Qwen3-Embedding-0.6B** 是"边缘级 near-SOTA"的另一强项：在 MMTEB 上仅次于闭源 Gemini-Embedding，参数却只有 0.6B，且 Apache 2.0 无商用限制。[1][3] 轻量补充：Nomic Embed Text v2（MoE，~100 语言）、mxbai-embed-large。

**💻 本地台式级（主力）**：**BGE-M3** 是多语言 + 长文档（8192 tokens）+ 混合检索的生产首选，MIT 许可最宽松，单模型出 dense/sparse/ColBERT 三种向量；配 **bge-reranker-v2-m3** 精排。[9][10] **Qwen3-Embedding-4B** 质量更高（MTEB 69.45），搭 **Qwen3-Reranker-0.6B/4B** 组成同源一条龙。Stella-1.5B 为英文场景的高性价比选项。

**🏢 大模型级**：**Qwen3-Embedding-8B**（MTEB multilingual 70.58，2025-06-05 No.1）为开源顶配质量档；GTE-Qwen2-7B、E5-Mistral-7B 各有所长；**KaLM-Embedding-Gemma3-12B** 被列为 MMTEB 天花板（≈72.3）；NV-Embed-v2 英文最强但 **CC-BY-NC 非商用**，商用需绕开。[11][12]

**闭源对标**：OpenAI `text-embedding-3-large / -small`、Google Gemini Embedding、Cohere Embed multilingual v3.0、Voyage。开源侧已可在多语言检索上打平甚至反超（Qwen3-8B / KaLM-12B），且省去按 token 计费与数据外发——对隐私优先的自部署是决定性优势。[1][13]

## 3. 候选 SEO 关键词与内容切入

- **型号词（低竞争，抢占型）**：`qwen3 embedding`、`qwen3 reranker`、`embeddinggemma`、`bge-reranker-v2-m3`、`nomic embed`、`stella embedding`。新模型词竞争普遍低，适合早占位（对标本仓库 `ace step 1.5` / `trellis 2` 的零竞争打法）。
- **已验证高价值词**：`bge-m3`（4,400/mo，KD=32，**CPC $9.32** 商业价值高）——做 "bge-m3 本地 RAG 教程 / bge-m3 vs OpenAI embeddings" 落地页。[models.md]
- **场景词**：`best embedding model 2026`、`best open source embedding model`、`local RAG embedding`、`on-device embedding`、`offline RAG`、`self-hosted vector search`——绑 Olares 本地推理叙事。
- **X alternative / vs 词（对比文金矿）**：`openai embedding alternative`、`text-embedding-3-large alternative`、`cohere rerank alternative`、`bge-m3 vs qwen3 embedding`、`embeddinggemma vs bge-m3`。
- **内容切入**：把型号总表落成一篇 "Best Open-Source Embedding & Reranker Models for Local RAG (2026)" 枢纽文 + 每个主推型号一篇 "run X locally on Olares" 教程，互链到 Olares 本地 RAG 场景页。

## 关键发现

1. **Qwen3-Embedding 是自部署的默认答案**：Apache 2.0 全系（含 Reranker）、0.6B→8B 覆盖手机到服务器、8B MTEB 多语言 No.1，一个家族即可覆盖 Olares 的边缘到主力全部档位。[1][2][3][5]
2. **端侧 RAG 已成立**：EmbeddingGemma 用 <200MB RAM 把高质量多语言 embedding 塞进手机/笔电，"数据不出设备的离线 RAG"从口号变成可落地——正中 Olares 隐私云卖点。[6][7]
3. **许可是选型隐雷**：NV-Embed-v2、jina-v3、SFR/Linq-Mistral 为 **CC-BY-NC 非商用**；EmbeddingGemma 走 Gemma 条款（非 Apache，尽管部分第三方误标）。推荐主推 Apache/MIT 的 Qwen3、BGE-M3、Nomic、GTE-Qwen2。[7][11][12]

## 局限性

- **榜单时效**："No.1 / 天花板"随 MTEB/MMTEB 版本与日期变动（Qwen3-8B 为 2025-06-05 口径，KaLM-12B 为另一榜单天花板），引用需带截止日期。[3][11]
- **第三方均分未逐一官方复核**：NV-Embed-v2、Stella、KaLM 等的 MTEB 均分来自汇总榜（[11][12]），部分未回到官方论文/模型卡二次核对。
- **搜索量为定性推测**：除 `bge-m3` 外的关键词竞争度未经 Semrush 核验，正式立项前应跑 model-seo-research 补数字。
- **EmbeddingGemma 许可存冲突**：官方为 Gemma 条款 [7]，个别第三方称已 Apache 2.0 [12][13]，以官方为准。

## 参考文献

[1] Qwen3 Embedding 论文 — https://arxiv.org/pdf/2506.05176
[2] QwenLM/Qwen3-Embedding (GitHub) — https://github.com/QwenLM/Qwen3-Embedding
[3] Qwen 官方博客 Qwen3 Embedding — https://qwenlm.github.io/blog/qwen3-embedding/
[4] Qwen3-Embedding-0.6B 模型卡 — https://huggingface.co/Qwen/Qwen3-Embedding-0.6B
[5] Qwen3-Embedding-8B README — https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/README.md
[6] Introducing EmbeddingGemma (Google Developers Blog) — https://developers.googleblog.com/en/introducing-embeddinggemma/
[7] EmbeddingGemma model overview (Google AI for Developers) — https://ai.google.dev/gemma/docs/embeddinggemma
[8] Welcome EmbeddingGemma (Hugging Face Blog) — https://huggingface.co/blog/embeddinggemma
[9] BAAI/bge-m3 模型卡 — https://huggingface.co/BAAI/bge-m3
[10] BAAI/bge-reranker-v2-m3 模型卡 — https://huggingface.co/BAAI/bge-reranker-v2-m3
[11] MTEB Leaderboard 2026 (CodeSOTA) — https://www.codesota.com/benchmarks/mteb
[12] Best Open-Weight Embedding Models 2026 (Presenc AI) — https://presenc.ai/research/best-open-weight-embedding-models-2026
[13] Embedding Model Comparison 2026 (KnowledgeSDK) — https://knowledgesdk.com/blog/embedding-model-comparison-2026
[14] Best Open-Source Embedding Models 2026 (BentoML) — https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models
