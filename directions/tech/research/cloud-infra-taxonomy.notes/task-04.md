---
task_id: 04
role: 数据/中间件分析师
status: complete
sources_found: 4
---

## Sources
[5] Google Cloud — 三云服务对照表 | https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison | Source-Type: official | As Of: 2024-12 | Authority: 9/10
[12] CNCF — Strimzi project page | https://www.cncf.io/projects/strimzi/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[22] Firecrawl — Best Vector Databases in 2026 | https://www.firecrawl.dev/blog/best-vector-databases | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[29] dibi8 — Milvus/Zilliz 2026 部署指南 | https://dibi8.com/resources/data-science/zilliz-milvus-vector-database-scale/ | Source-Type: community | As Of: 2026 | Authority: 4/10
[1] CNCF — Graduated and Incubating Projects | https://www.cncf.io/projects/ | Source-Type: official | As Of: 2026 | Authority: 10/10

## Findings
- 关系型：PostgreSQL 为开源事实主力；公有云托管为 AWS RDS/Aurora / Azure Database for PostgreSQL·Azure SQL / Google Cloud SQL·AlloyDB。[5]
- 文档型：MongoDB；公有云对应 AWS DocumentDB/DynamoDB / Azure Cosmos DB / Google Firestore·Datastore。[5]
- KV/缓存：Redis 及其 Apache-2.0 分叉 Valkey（2024 改协议后 Linux Foundation 维护，drop-in 替代）；公有云 AWS ElastiCache / Azure Cache / Google Memorystore(for Valkey/Redis)。[22][5]
- 流/消息：Kafka（K8s 上经 Strimzi operator，Strimzi 2024-02-08 升 CNCF Incubating）、NATS（CNCF Incubating）、RabbitMQ；公有云 AWS Kinesis/MSK·MQ / Azure Event Hubs·Service Bus / Google Pub/Sub。[12][5][1]
- 向量库：Qdrant(Rust，过滤/性价比首选)、Milvus(十亿级分布式)、Weaviate(原生混合检索)；pgvector 适合已用 Postgres(<50M 向量)。[22][29]
- 向量检索公有云化程度低，最接近为托管检索/AI 搜索（如 Azure AI Search、Vertex AI Vector Search）或走 pgvector on RDS/Cloud SQL。[22]

## Deep Read Notes
### Source [22]: Best Vector Databases 2026
Key data: Qdrant(Rust，最佳免费档，<50M)、Weaviate(hybrid BM25+vector)、Milvus(十亿级自建)、pgvector+pgvectorscale(<100M，用现有 Postgres)。Valkey 为 Redis 的 Apache-2.0 分叉。
Key insight: 个人/小规模自建的"最少后悔"默认是 Qdrant 或 pgvector（复用 Postgres）。
Useful for: 数据大类向量库行 + Olares(Citus/PG 走 pgvector) 平替解读。

## Gaps
- Milvus 的 CNCF 成熟度存在来源分歧：dibi8 正文称"CNCF-graduated"，其引用却指向 Incubation 页——需在报告中标注不确定并降级。[29]
- Qdrant、Weaviate、MongoDB、PostgreSQL、Redis、RabbitMQ 均非 CNCF 托管项目（CNCF 里数据类主要是 TiKV/Vitess 等），"top"依据为采用度/star 而非 CNCF 状态。
- 相反主张：把向量库单列为基础设施子类有争议，部分观点认为它只是 Postgres 扩展(pgvector)即可覆盖多数场景。

## END
