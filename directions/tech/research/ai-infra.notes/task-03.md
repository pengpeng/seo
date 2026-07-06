---
task_id: 03
role: 向量检索与 Embedding/Rerank 分析师
status: complete
sources_found: 10
---

## Sources
[1] Top 15 Vector Databases in 2026 (Medium, Pratik R.) | https://medium.com/@pratik-rupareliya/top-15-vector-databases-in-2026-a-production-decision-guide-from-100-enterprise-deployments-dd58a04f51a5 | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[2] Vector Database Comparison 2026 at Scale (TopReviewed.ai) | https://topreviewed.ai/blog/vector-database-comparison-2026-pinecone-vs-qdrant-vs-pgvector-vs-weaviate-at-scale | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[3] The Best Vector Database in 2026 (dev.to, Darshit) | https://dev.to/darshit_01/the-best-vector-database-in-2026-qdrant-vs-pinecone-vs-weaviate-vs-milvus-vs-pgvector-3147 | Source-Type: community | As Of: 2026 | Authority: 5/10
[4] Milvus vs Qdrant 2026 (kunalganglani.com) | https://www.kunalganglani.com/blog/milvus-vs-qdrant | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[5] Vector Database Complete Comparison (data-dynamics.io) | https://www.data-dynamics.io/en/blog/vector-database-comparison | Source-Type: secondary-industry | As Of: 2026 | Authority: 4/10
[6] OpenAI vs BGE/E5/Voyage/Cohere/Qwen3 Embedding (axiomlogica) | https://axiomlogica.com/ai-ml/openai-text-embedding-3-small-vs-bge-e5-voyage-cohere-qwen3-embedding-retrieval | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[7] The 12 Embedding Models Worth Running MTEB-Graded 2026 (RuleSell) | https://www.rulesell.com/topic/embeddings | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[8] Embedding Models 2026: Benchmark (Ailog RAG) | https://app.ailog.fr/en/blog/news/embedding-models-2026 | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 5/10
[9] Best Embedding Models 2026 (pecollective) | https://pecollective.com/tools/best-embedding-models/ | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 4/10
[10] The Best Open-Source Embedding Models 2026 (BentoML) | https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10

## Findings
- 开源向量库无单一"最佳"，按规模/基建分层：pgvector（已有 PostgreSQL 时的默认，~50M 向量内低运维）、Qdrant（<100M 向量的性能/过滤首选）、Milvus（十亿级/K8s 分布式）、Weaviate（原生 BM25+向量混合检索）、Chroma（原型/本地优先）。[1][3][5]
- Qdrant（Rust，Apache-2.0）综合评分居首（性能+价格+DX），单 Docker 容器、~100MB 内存跑 1M 向量、p99<15ms；过滤检索用 HNSW+payload index 表现"excellent"。[3][4]
- Milvus（Go/C++，Apache-2.0）为十亿级分布式而生，但需 etcd/MinIO 等多组件，自托管运维较重。[3][4]
- Pinecone 是闭源全托管 SaaS（无自托管选项），零运维但成本随规模上升、有厂商锁定与数据主权顾虑——是自托管栈要对标的公有云对象。[1][5]
- 云对标叫法：Pinecone（纯托管）、Zilliz Cloud（Milvus 托管）、Qdrant Cloud / Weaviate Cloud（各自云版）、Turbopuffer（对象存储型托管向量）、AWS/GCP/Azure 的托管向量检索。[1][4]
- Embedding：BGE-M3（BAAI，568M，MIT）是自托管多语种（100+ 语言）事实标准，单次前向支持 dense+sparse+multi-vector(ColBERT)，单张 L4 GPU 即可生产，成本仅 GPU 租金。[6][7][10]
- Qwen3-Embedding-8B（Apache-2.0）在 MTEB 登顶（~70.6），4096 维、32K 上下文，长多语种文档优势明显，代价是 8B 需更多显存；轻量档 Qwen3-Embedding-0.6B 也是边缘 near-SOTA。[6][8][10]
- Embedding 公有云对标叫法：Voyage AI（voyage-3-large，检索精度溢价 ~3×）、Cohere embed-v4（与 rerank 配套、多模态）、OpenAI text-embedding-3-small/large（英文高量默认，~$0.02/1M）、Google Gemini Embedding、Jina Embeddings v3。[6][7][8]
- Nomic Embed v2（Apache-2.0，137M，首个 MoE 文本嵌入）多语种、Matryoshka 可截断到 256 维，适合 CPU/边缘高吞吐低成本。[8][10]
- Rerank 在开源侧常用 BGE-reranker 系列；商业侧对标 Cohere Rerank——embed+rerank 端到端流水是 Cohere 的强项。[7][9]
- 自托管判据：量 >10M embeddings/月、数据主权、或有 MLOps 能力时自托管（Qwen3/BGE-M3）；低量/急上线/无基建团队用 API（Gemini/OpenAI）。[8]

## Deep Read Notes
### Source [3]: dev.to Best Vector DB 2026
Key data: Qdrant p50 4.2ms/p99 11ms/recall 0.98；pgvector p50 28ms；单 Docker vs Milvus 需 etcd+MinIO；Qdrant Cloud 1M~$25/mo vs Pinecone ~$70/mo。
Key insight: Qdrant 在"单容器易运维+过滤性能+价格"三重占优，最契合个人云单机/小集群。
Useful for: 向量库子类 top1 + Olares 平替（Qdrant 单容器易装）。

### Source [6]: axiomlogica embedding retrieval
Key data: 三锚点——OpenAI text-embedding-3-small（$0.02/1M 托管默认）、BGE-M3（自托管多语种）、Voyage（精度溢价）；BGE-M3 1024 维固定/8192 上下文，Qwen3-8B 4096 维/32K。
Key insight: 明确"workload-dependent、无普适最优"，自托管胜在语言覆盖+方法灵活+主权。
Useful for: Embedding 子类开源 vs 闭源对标表。

## Gaps
- 本任务来源以 secondary-industry/community 为主，官方（Qdrant/Milvus/BAAI GitHub）未直接取源；报告需在 P3 用其他任务的官方源平衡官方占比，star 数等以官方口径为准并降置信度。
- 各来源 MTEB 分数/排名口径不一（Qwen3-8B 70.6 vs 榜单波动），采定性"第一梯队"表述。
- 相反主张候选：pgvector 在 100M+ 向量会因磁盘 I/O 明显降级、recall 掉到 0.88–0.93——"pgvector 万能"不成立，大规模仍需专用库。[2]
- 交叉参考：工作区已有 embedding 深度报告 directions/model/research/07-embedding/embedding.md（EmbeddingGemma-300m、Qwen3-Embedding、Nomic 等本地部署结论），报告可引其结论。

## END
