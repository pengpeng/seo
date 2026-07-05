---
task_id: 01
role: Embedding 研究专员
status: complete
sources_found: 14
---

## Sources

[1] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models（论文）| https://arxiv.org/pdf/2506.05176 | Source-Type: official/paper | As Of: 2025-06 | Authority: 10/10
[2] QwenLM/Qwen3-Embedding（官方仓库）| https://github.com/QwenLM/Qwen3-Embedding | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[3] Qwen 官方博客 — Qwen3 Embedding | https://qwenlm.github.io/blog/qwen3-embedding/ | Source-Type: official | As Of: 2025-06 | Authority: 10/10
[4] Qwen/Qwen3-Embedding-0.6B · Hugging Face（模型卡）| https://huggingface.co/Qwen/Qwen3-Embedding-0.6B | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[5] Qwen/Qwen3-Embedding-8B README · Hugging Face | https://huggingface.co/Qwen/Qwen3-Embedding-8B/blob/main/README.md | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[6] Introducing EmbeddingGemma — Google Developers Blog | https://developers.googleblog.com/en/introducing-embeddinggemma/ | Source-Type: official | As Of: 2025-09 | Authority: 10/10
[7] EmbeddingGemma model overview — Google AI for Developers | https://ai.google.dev/gemma/docs/embeddinggemma | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[8] Welcome EmbeddingGemma — Hugging Face Blog | https://huggingface.co/blog/embeddinggemma | Source-Type: official/vendor | As Of: 2025-09 | Authority: 9/10
[9] BAAI/bge-m3 · Hugging Face（模型卡）| https://huggingface.co/BAAI/bge-m3 | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[10] BAAI/bge-reranker-v2-m3 · Hugging Face | https://huggingface.co/BAAI/bge-reranker-v2-m3 | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[11] MTEB Leaderboard 2026: Best Embedding Models for RAG — CodeSOTA | https://www.codesota.com/benchmarks/mteb | Source-Type: third-party | As Of: 2026 | Authority: 6/10
[12] Best Open-Weight Embedding Models 2026 — Presenc AI | https://presenc.ai/research/best-open-weight-embedding-models-2026 | Source-Type: third-party | As Of: 2026 | Authority: 6/10
[13] Which Embedding Model Should You Use in 2026? — KnowledgeSDK | https://knowledgesdk.com/blog/embedding-model-comparison-2026 | Source-Type: third-party | As Of: 2026 | Authority: 5/10
[14] The Best Open-Source Embedding Models in 2026 — BentoML | https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models | Source-Type: vendor | As Of: 2026 | Authority: 6/10

## Findings

- Qwen3-Embedding 系列（0.6B / 4B / 8B）为 2025-06 开源发布，Apache 2.0；8B 在 MTEB multilingual 排名 No.1，均分 70.58（截至 2025-06-05）。[1][2][3][5]
- Qwen3-Embedding 三档规格：0.6B（28 层，32K 上下文，1024 维）｜4B（36 层，2560 维）｜8B（36 层，4096 维），全系支持 MRL 可变维度与指令感知。[2][3][4]
- Qwen3 同时发布 Reranker（cross-encoder）0.6B / 4B / 8B，Apache 2.0；4B/8B 在 MTEB-R / MMTEB-R 上超过 bge-reranker-v2-m3、jina/gte reranker。[3]
- 支持 100+ 自然语言 + 编程语言，覆盖检索、代码检索、分类、聚类、bitext mining。[2][3]
- EmbeddingGemma 为 Google DeepMind 2025-09 发布的端侧模型，308M 参数（约 100M 模型 + 200M embedding），基于 Gemma 3。[6][7][8]
- EmbeddingGemma 量化后可 <200MB RAM 运行，EdgeTPU 上 <22ms；2K 上下文；MRL 输出维度 768→512/256/128；100+ 语言；官称"<500M 参数下 MTEB 排名最高的开源多语言模型"。[6][7]
- BGE-M3（BAAI）：1024 维，8192 上下文，100+ 语言，单模型同时支持 dense / sparse（类 BM25 词权）/ multi-vector（ColBERT）三种检索，MIT 许可。[9]
- BAAI 官方推荐 RAG 流水线：hybrid retrieval（dense+sparse）+ re-ranking；cross-encoder reranker 精度高于 bi-encoder embedding。[9]
- bge-reranker-v2-m3 基于 bge-m3，轻量多语言 cross-encoder；BAAI 另有 v2-gemma（gemma-2b）、v2-minicpm-layerwise 更强档。[10]
- 开源第一梯队（MTEB v2 均分，第三方汇总）：KaLM-Embedding-Gemma3-12B ≈72.3（天花板）、Qwen3-Embedding-8B ≈70.6、NV-Embed-v2 ≈72（英文强，CC-BY-NC）、GTE-Qwen2-7B ≈70.2、Stella-1.5B ≈69.4、E5-Mistral-7B ≈66.6、BGE-M3 ≈68。[11][12]
- 闭源对标：OpenAI text-embedding-3-large/small、Google Gemini Embedding、Cohere Embed multilingual v3.0；Qwen3-Embedding-0.6B 仅次于 Gemini-Embedding 而参数仅 0.6B。[1][13]
- 轻量/边缘候选：EmbeddingGemma-300m、Qwen3-Embedding-0.6B、Nomic Embed Text v2（~0.5B，MoE，Apache 2.0，~100 语言）、mxbai-embed-large（Apache）。[6][12][14]
- 许可分布：Apache 2.0（Qwen3 系列、GTE-Qwen2、Nomic v2、mxbai、Stella）｜MIT（BGE 系列、E5-Mistral）｜CC-BY-NC 非商用（NV-Embed-v2、jina-v3、SFR/Linq-Mistral）｜Gemma 条款（EmbeddingGemma）。[11][12][14]

## Deep Read Notes

### Source [1][2][3][4][5]: Qwen3 Embedding（论文 + 官方仓库/博客/HF）
- Key data: MTEB(multi) 8B=70.58 / 4B=69.45 / 0.6B=64.33（官方 HF 表）；MTEB-R 检索项 8B=61.69、4B=60.86、0.6B=56.00；Reranker 4B MTEB-R=69.76、8B=69.02，均显著高于 bge-reranker-v2-m3（57.03）。
- Key insight: 0.6B 以亚十亿参数逼近闭源 Gemini-Embedding，是"边缘/手机级 near-SOTA"的最强候选；全系 Apache 2.0 无商用限制，对自部署最友好。
- Useful for: 型号总表主推行、"Qwen3 Embedding local"/"Qwen3 Reranker" 关键词、Olares 本地 RAG 默认推荐。

### Source [6][7][8]: EmbeddingGemma（Google 官方 + HF blog）
- Key data: 308M 参数、2K 上下文、768 维（MRL→128）、<200MB RAM（量化）、EdgeTPU <22ms、100+ 语言。
- Key insight: 明确定位手机/平板/笔电端侧离线 RAG，官方生态齐全（llama.cpp / Ollama / MLX / LiteRT / transformers.js / LM Studio），是📱层最正统的"最佳 <500M 开源多语言"模型。
- Useful for: 📱边缘层主推、"on-device embedding"/"offline RAG"/"embeddinggemma" 关键词。

### Source [9][10]: BGE-M3 / bge-reranker-v2-m3（BAAI 官方 HF）
- Key data: BGE-M3 1024 维 / 8192 上下文 / 100+ 语言 / dense+sparse+ColBERT 三合一 / MIT；reranker-v2-m3 基于 bge-m3 的多语言 cross-encoder。
- Key insight: BGE-M3 是"混合检索 + 长文档"生产首选，MIT 许可最宽松；官方明确 hybrid+rerank 二段式流水线，正好是 Olares 本地 RAG 的标准架构。
- Useful for: 💻主力层、"bge-m3"（已知 4,400 月搜 / KD=32 / CPC $9.32）、"bge reranker" 教程。

### Source [11][12][13][14]: 第三方 MTEB 汇总与选型指南
- Key data: 开源均分梯队与许可矩阵；闭源对标名单；分场景推荐（端侧→EmbeddingGemma，多语言→BGE-M3，质量优先→Qwen3-8B）。
- Key insight: MTEB 只作 shortlist，落地需按语料/延迟/许可再筛；量化 + reranker 后小模型常反超。CC-BY-NC 模型（NV-Embed-v2、jina-v3）商用受限，需在报告中明确标注。
- Useful for: 部署层级划分、许可栏、闭源对标栏、"best embedding model 2026"/"local RAG" 关键词。

## Gaps
- 相反主张：EmbeddingGemma 许可存在冲突——Google 官方文档为 Gemma 使用条款（允许责任性商用）[7]，而部分第三方（Presenc/KnowledgeSDK）称"现已 Apache 2.0"[12][13]。以官方 Gemma 条款为准，Apache 说法存疑。
- 相反主张：排行榜"第一"随时间/榜单版本变动——KaLM-Embedding-Gemma3-12B 被列为 MMTEB 天花板 [11]，而 Qwen3-8B 官称 2025-06-05 MTEB multilingual No.1 [3]；二者榜单口径不同，需注明"截至日期 + 榜单版本"。
- 缺 Semrush 精确搜索量：除 bge-m3（来自本仓库 models.md 快照）外，其余型号词竞争度为定性推测，未做 Semrush 核验。
## END
