---
task_id: 03
role: 向量/时序/图/检索/协调类数据中间件分析师
status: complete
sources_found: 21
---

## Sources
[1] Qdrant vs Milvus vs Weaviate vs LanceDB: Vector DB Comparison | https://builderai.tools/blog/vector-database-benchmarks-qdrant-milvus-weaviate-lancedb | Source-Type: 第三方对比长文 | As Of: 2026-05 | Authority: 6/10
[2] Vector Database Comparison for RAG: Qdrant vs Weaviate vs Milvus (Lushbinary) | https://lushbinary.com/blog/vector-database-comparison-rag-qdrant-weaviate-milvus/ | Source-Type: 第三方对比长文 | As Of: 2026-05 | Authority: 5/10
[3] Qdrant vs Weaviate vs Milvus: Which Vector Database (elest.io) | https://blog.elest.io/qdrant-vs-weaviate-vs-milvus-which-vector-database-for-your-rag-pipeline/ | Source-Type: 厂商博客对比 | As Of: 2026 | Authority: 6/10
[4] The Best Time-Series Databases Compared (Tiger Data) | https://www.tigerdata.com/learn/the-best-time-series-databases-compared | Source-Type: 厂商对比长文 | As Of: 2026 | Authority: 7/10
[5] 5 InfluxDB Alternatives in 2026 (Basekick Labs) | https://basekick.net/blog/influxdb-alternatives-2026 | Source-Type: 第三方对比长文 | As Of: 2026 | Authority: 6/10
[6] GreptimeDB as an Alternative to InfluxDB (Greptime) | https://greptime.com/tech-content/2025-04-15-influxdb-comparison-greptimedb | Source-Type: 官方厂商博客 | As Of: 2026-04 | Authority: 7/10
[7] InfluxDB vs TDengine (InfluxData) | https://www.influxdata.com/comparison/influxdb-vs-tdengine/ | Source-Type: 官方厂商对比 | As Of: 2026 | Authority: 7/10
[8] FAQ on Software Licensing (Elastic) | https://www.elastic.co/pricing/faq/licensing | Source-Type: 官方文档 | As Of: 2026 | Authority: 9/10
[9] OpenSearch vs Elasticsearch Compared 2026 (BigData Boutique) | https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared | Source-Type: 第三方对比长文 | As Of: 2026-05 | Authority: 8/10
[10] FAQ (OpenSearch 官方) | https://opensearch.org/faq/ | Source-Type: 官方文档 | As Of: 2026 | Authority: 9/10
[11] vesoft-inc/nebula (GitHub) | https://github.com/vesoft-inc/nebula | Source-Type: 官方 GitHub | As Of: 2026-05 | Authority: 9/10
[12] Supported Databases (KubeBlocks 官方) | https://kubeblocks.io/databases | Source-Type: 官方文档 | As Of: 2026 | Authority: 9/10
[13] apecloud/kubeblocks (GitHub) | https://github.com/apecloud/kubeblocks | Source-Type: 官方 GitHub | As Of: 2026 | Authority: 9/10
[14] Supported Addons (KubeBlocks 官方) | https://kubeblocks.io/docs/preview/user_docs/overview/supported-addons | Source-Type: 官方文档 | As Of: 2026 | Authority: 9/10
[15] Milvus – LFAI & Data (基金会官网) | https://lfaidata.foundation/projects/milvus/ | Source-Type: 官方基金会 | As Of: 2026 | Authority: 9/10
[16] Use kine as a replacement of etcd (milvus Issue #41113) | https://github.com/milvus-io/milvus/issues/41113 | Source-Type: 官方 GitHub Issue | As Of: 2025-04 | Authority: 8/10
[17] k3s-io/kine (GitHub) | https://github.com/k3s-io/kine | Source-Type: 官方 GitHub | As Of: 2026-04 | Authority: 9/10
[18] Managed Graph Database – Amazon Neptune (AWS) | https://aws.amazon.com/neptune/ | Source-Type: 官方产品页 | As Of: 2026 | Authority: 9/10
[19] Time-Series Database – Amazon Timestream (AWS) | https://aws.amazon.com/timestream/ | Source-Type: 官方产品页 | As Of: 2026 | Authority: 9/10
[20] Choosing a database for generative AI apps (AWS DB Blog) | https://aws.amazon.com/blogs/database/key-considerations-when-choosing-a-database-for-your-generative-ai-applications/ | Source-Type: 官方博客 | As Of: 2026 | Authority: 8/10
[21] apecloud/kubeblocks-addons (GitHub) | https://github.com/apecloud/kubeblocks-addons | Source-Type: 官方 GitHub | As Of: 2026 | Authority: 9/10

## Findings
- Qdrant：Rust 写的向量库，Apache 2.0，主打低延迟过滤搜索/单二进制轻运维，GitHub ~29k star；KubeBlocks 有 qdrant addon（覆盖 1.5.0→1.16.3 多版本）。[1][3][21]
- Weaviate：Go 写的 AI-native 向量库，BSD 3-Clause，内置向量化模块+GraphQL+原生多租户，~14k star；KubeBlocks 收录 weaviate addon 但无独立 operator 落地页。[1][3][14]
- Milvus：Go/C++ 云原生分布式向量库，Apache 2.0，存算分离可扩至十亿级、支持 IVF/HNSW/DiskANN/GPU 加速，~44k star；是 LF AI & Data 基金会 2021-06 毕业项目（非 CNCF）；KubeBlocks 有 milvus addon/operator（2.3.2、2.5.13）。[1][4][15][21]
- pgvector 作为 PostgreSQL 内置扩展被公认"已在 Postgres 上就足够"的替代，适合中小规模、不想单独运维专用向量库的团队。[2]
- InfluxDB：2013 年发布的时序库鼻祖，v3.0 转为 Apache 2.0 + MIT 双许可；历史上水平集群（clustering）需企业版。[4][7]
- VictoriaMetrics：Apache 2.0，Prometheus 长期存储/PromQL 兼容，OSS 集群版免费水平扩展，另有专有企业版；KubeBlocks 有 victoria-metrics addon。[4][5][14]
- GreptimeDB：Rust 写的云原生统一可观测库（指标+日志+trace 同引擎、对象存储原生），Apache 2.0（OSS）+ 专有企业版，v1.0 GA 于 2026-04-14；KubeBlocks addons 列表含 greptimedb 但暂无 operator 落地页。[5][6][14]
- TDengine：TAOS Data 2017 年推出，面向 IoT/工业物联网，社区版 AGPLv3、含免费水平集群，另有商业许可。[4][7]
- NebulaGraph：C++ 分布式图数据库，Apache 2.0，可 SaaS 后端部署，用 Multi-Group Raft 自带一致性（不依赖外部 etcd/ZooKeeper），~12.2k star，仅进入 CNCF Database Landscape 但非 CNCF 托管项目；最新 v3.8.0（2024-05）。[11]
- KubeBlocks 图 DB 类列了 Neo4j / Nebula Graph，但均无 operator 落地页（尚未成熟收录）。[14]
- etcd：强一致分布式 KV 存储，CNCF 毕业项目，KubeBlocks 归到 Cache/KV 类并提供 etcd-operator（Raft HA/自动选主/快照备份，覆盖 3.5.x、3.6.1）。[13][14][21]
- Kine（"Kine is not etcd"）：Apache 2.0 etcd-shim，把 etcd API 翻译成 SQLite/Postgres/MySQL/NATS，让 k8s 用关系库替代 etcd，~2.3k star；Milvus 有把 etcd 换成 Kine 的公开 feature request（Issue #41113，仍 open），但 milvus-operator 官方文档写明"目前只支持 etcd 存元数据"。[16][17][3]
- ZooKeeper：Apache 集中式配置/命名/分布式同步服务，被 KubeBlocks 收录（zookeeper addon，归 Cache/KV 类）。[14]
- Elasticsearch：2010 年基于 Lucene，2021 年 7.11 从 Apache 2.0 转 SSPL+Elastic License 2.0，2024-09 又加 AGPLv3，现为 AGPLv3/SSPL/ELv2 三许可（用户择一），最新 9.3.3（2026-04）；托管仅 Elastic Cloud（AWS/GCP/Azure）；KubeBlocks 有 elasticsearch-operator（多版本 6.8→8.15）。[8][9][21]
- OpenSearch：AWS 2021-04 从 Elasticsearch 7.10.2 分叉，纯 Apache 2.0，2024-09 移交 Linux Foundation 下的 OpenSearch Software Foundation 治理，最新 3.6（2026-04）；托管 = Amazon OpenSearch Service/Serverless；KubeBlocks 收录 opensearch addon（归 Search/OLAP 类）。[9][10][14]
- 公有云托管替代：向量→Amazon OpenSearch(向量引擎)/Aurora pgvector、Azure AI Search、Vertex AI Vector Search；时序→Amazon Timestream(含 Timestream for InfluxDB)；图→Amazon Neptune / Neptune Analytics(支持图+向量 GraphRAG)；检索→Amazon OpenSearch Service。[18][19][20]

## Deep Read Notes
### Source [9]: OpenSearch vs Elasticsearch Compared 2026 (BigData Boutique)
Key data: Elasticsearch 9.3.3 与 OpenSearch 3.6 均为 2026-04、同用 Lucene 10；2021-01 起 7.11 转 SSPL/ELv2，AWS fork 7.10.2 建 OpenSearch，2024-09 移交 OSSF/Linux Foundation；OpenSearch 向量维度上限 16000（Faiss）对比 Elasticsearch 4096（Lucene HNSW）。
Key insight: 对"把搜索引擎当内嵌后端"的自部署场景，Elasticsearch 三许可实际几乎零风险；只有"以托管服务对外售卖"才触发 SSPL/AGPL 顾虑——这正是 OpenSearch 分叉的核心动机。
Useful for: 全文检索小节（许可争议 + Olares 该选哪个）、Gaps 相反主张。

### Source [4]: The Best Time-Series Databases Compared (Tiger Data)
Key data: 关键分水岭是"水平扩展是否要企业版"——InfluxDB 历史上把 clustering 锁在企业层，VictoriaMetrics 与 TDengine 提供免费集群；许可矩阵：InfluxDB 3.0=Apache2.0+MIT、VictoriaMetrics=Apache2.0、TDengine=AGPL3.0、QuestDB/Druid/ClickHouse=Apache2.0。
Key insight: 时序库选型先按查询语言（SQL vs PromQL）和"是否已在 Prometheus 生态"分流：Prometheus 长存选 VictoriaMetrics，统一可观测选 GreptimeDB，IoT 高频选 TDengine/QuestDB。
Useful for: 时序数据库小节（定位/何时选/许可）。

### Source [15][16]: Milvus 基金会与 Kine 依赖
Key data: Milvus 由 Zilliz 于 2020-01 捐入、2021-06 毕业于 LF AI & Data（非 CNCF）；Milvus 元数据当前仅支持 etcd，Issue #41113（2025-04，open）提议用 Kine 把元数据换成 Postgres/MySQL/Aurora 以去 etcd、做无状态化。
Key insight: 向量库"是否 CNCF"要精确——Milvus 属 LF AI & Data 而非 CNCF；Kine 是把 etcd 依赖降级成关系库的通用路径，对个人云这种"少组件"部署很有价值。
Useful for: 协调/元数据小节（etcd↔Kine 关系）、向量库成熟度标注。

## Gaps
- 相反主张：Elasticsearch 2024 加 AGPLv3 后"技术上已重新算开源"，与"SSPL/ELv2 仍非 OSI 认可、禁止托管"并存——是否算"真开源"社区口径不一（[8] vs [10]）。
- 相反主张：pgvector 是否已足够替代专用向量库——[2] 认为已在 Postgres 上"足够"，但十亿级/GPU 加速场景仍需 Milvus，边界未有统一结论。
- 个人云是否真需要专用图/时序库存疑：NebulaGraph/Neo4j 在 KubeBlocks 仍无 operator 落地页、GreptimeDB/InfluxDB 时序 addon 也无 operator 页，成熟度与"个人云刚需"均未验证。
- 未拿到 etcd/ZooKeeper 的 GitHub star 量级与 CNCF 毕业确切日期的一手页面（本轮靠常识与 KubeBlocks 描述，未单独 fetch 官方）。
- 未找到 KubeBlocks 明确"支持 TDengine / NebulaGraph"的正式 addon 证据（仅在 Graph DB landscape 列名但无 operator）。

## END
