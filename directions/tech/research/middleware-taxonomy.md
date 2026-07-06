# 中间件 / PaaS 深度目录（IaaS/PaaS 视角，逐项目）

> 研究日期: 2026-07-05 | 来源数: 76 | 字数: ~6800 | 模式: Standard | AS_OF: 2026-07-05 | 官方源占比: 50%

## 摘要

本报告站在 **IaaS（裸基础设施：计算/存储/网络，用户自管 OS/运行时/中间件/数据）vs PaaS（平台层：把 OS/运行时/中间件/数据库都托管，用户只写代码与数据）** 的分层视角 [5][6]，把"中间件"——即**不同应用都会依赖的第三方共享服务**（数据库、缓存、消息队列、检索、可观测等）[5]——做成一份逐项目成文的目录：每个子类给「认知 → 公有云替代 → 逐个项目介绍（定位/许可/CNCF 或成熟度[AS_OF]/KubeBlocks 或 Olares 状态）」。核心锚点：Olares 明确"对标公有云 IaaS/PaaS/SaaS 三层给开源平替"，其平台层中间件由 **KubeBlocks operator** 托管，应用在 `OlaresManifest.yaml` 的 middleware 段**声明式**依赖 postgres/redis 等，部署时系统**自动注入** host/port/username/password 到 `.Values.*` [1][11][12]。KubeBlocks 是 ApeCloud 开源的**通用型** K8s Operator（AGPL-3.0，约 3,071 star，v1.0.0 于 2025-05，AS_OF 约 35 类引擎），用一套引擎无关的 CRD 管多种有状态引擎，而非每种引擎一个专用 operator [2][3][4]。

主要结论：①**计算/编排、存储、数据库中间件、消息、平台中间件**这五大类的核心子类，开源侧都有生产可用的 top 项目，且每类都有清晰的公有云托管对标——Olares 已内置其中大多数关键项（K3s、containerd、JuiceFS/MinIO、PostgreSQL 16/KVRocks、NATS、Prometheus/OTel、Argo Workflows、Vault/Infisical）[1]。②**KubeBlocks 覆盖的是"数据库/有状态引擎"而非"存储层"与"轻量/流处理"**：它收录 MySQL/PostgreSQL/MongoDB/Redis/etcd/ZooKeeper、Kafka/RabbitMQ/Pulsar、Qdrant/Weaviate/Milvus、ClickHouse/Doris/StarRocks/ES/OpenSearch、TiDB/OceanBase/PolarDB-X 等；但存储层（Ceph/JuiceFS/Longhorn）是其底层依赖而非 addon，NATS/Flink/Spark/Storm/Trino/Presto 亦不在其托管范围 [14][15][54]。③**企业·大数据类（分布式 SQL、OLAP、SQL 查询引擎、大数据流处理）默认多节点/三副本、面向企业横扩**，对个人云（单机/小集群、面向 Personal Agent）多属过重，归"个人云非重点"，唯一个别窗口是 ClickHouse 单机（8GB+ 调优）做本地分析，而更轻的是 DuckDB/chDB [49][52][53]。反方须记：单机跑完整 K8s + KubeBlocks 是否**过度工程**缺乏第三方独立实测，是本领域最大的开放争议 [7]。

## 0. 框架：IaaS / PaaS / 中间件 与 Olares·KubeBlocks 模型

- **分层**：IaaS 提供虚拟化算力/存储/网络，用户自管 OS、运行时、中间件、应用与数据；PaaS 再往上把 OS、运行时、中间件、数据库都托管，用户只写代码与数据 [5][6]。"中间件"＝应用普遍依赖的第三方共享服务；IaaS 下需自己装管，PaaS 内置并通过 API 编排 [5]。
- **Olares 的分层平替**：基础设施层＝容器编排（Linux 默认 K3s、可选 K8s；macOS 用 minikube）+ containerd 运行时 + Calico/CoreDNS/Envoy 网络 + etcd + 本地/MinIO/S3 存储 + JuiceFS；平台层＝中间件（PostgreSQL 16、KVRocks、NATS、JuiceFS、Argo Workflows、Vault/Infisical、Prometheus/OTel），由 KubeBlocks 托管 [1]。
- **声明式中间件依赖**：应用在 `OlaresManifest.yaml` 的 middleware 段声明 postgres/redis 等依赖，系统自动把连接凭据注入 `.Values.postgres.*`/`.Values.redis.*`；PostgreSQL、Redis 预装，MongoDB/MinIO/RabbitMQ/MySQL/MariaDB 需另装 [11][12]。
- **KubeBlocks 的机制**：Addon＝含 ClusterDefinition/ComponentDefinition 等 CR 的 Helm chart，声明式描述期望态由框架 reconcile，统一处理 HA/备份/扩缩/配置等 day-2 运维 [3][4]。

**置信度:** High　**依据:** Olares 官方架构/开发者文档 + KubeBlocks 官方文档/GitHub 直接背书 [1][2][3][11][12]。
**反方解释:** 个人云/单机是否需要完整 K8s + KubeBlocks 这类企业级 operator 缺乏第三方独立"过度工程"实测，仅有官方与社区评述 [7]。

## 1. 计算 / 编排（IaaS 基座）

**认知**：容器编排是"把容器调度到一堆机器上并维持期望状态"的底座，是所有 PaaS 中间件的运行地基。**公有云替代**：AWS EKS / Azure AKS / GCP GKE（托管 K8s 控制面）[8][10]。

- **Kubernetes**（Apache-2.0，CNCF 毕业）：容器编排事实标准，生态与可移植性的基准；完整版对单机偏重 [7][8]。
- **K3s**（Rancher/SUSE，Apache-2.0，CNCF 认证）：<100MB 单二进制轻量发行版，默认用 SQLite/**Kine** 替代 etcd、直用 containerd，边缘/生产/个人云首选——**Olares Linux 默认底座** [1][7][9]。
- **k0s**（Mirantis，~230MB）：最贴近上游、零主机依赖的单二进制发行版，适合要"纯净 K8s"的场景 [7][9]。
- **MicroK8s**（Canonical，snap 打包）：addon 体系 + dqlite HA，Ubuntu/工作站友好 [7][9]。
- **RKE2**（Rancher/SUSE）：CIS 加固 + FIPS 140-2，面向企业合规 [7][8]。
- **容器运行时 containerd / CRI-O**：K8s 的 CRI 实现层，containerd 为多数发行版默认——**Olares 内置 containerd** [1][8]。

**置信度:** High　**依据:** 轻量 K8s 权威对比 + Olares 架构 [1][7][8][9]。
**反方解释:** 有观点认为个人/单机根本不需要 K8s，Cloud Run/Container Apps 式 Serverless 更省心，K3s 反而抬高运维门槛 [7]。

## 2. 存储（IaaS 基座）

**认知**：按访问模式分对象/块/分布式文件三型，是数据库与应用的持久化底座。**公有云替代**：对象 S3/Blob/Cloud Storage；块 EBS/Managed Disks/Persistent Disk；文件 EFS/Azure Files/Filestore [10][16]。注意：**KubeBlocks 消费 CSI/PV，存储层是其底层依赖而非 addon** [15]。

- **MinIO**（AGPLv3）：S3 协议事实参考实现、S3 兼容度与吞吐最佳；但社区版仓库 2026-02 被归档、转向商业版 AIStor（有社区 fork 续维），已"事实闭源"——**Olares 内置 MinIO** [1][17]。
- **Ceph**（LGPL-2.1/3.0）：统一（块+文件 CephFS+对象 RGW）存储事实标准，v20.x "Tentacle"(2026-04) 加 FastEC 缩小与 MinIO 性能差距；适合有专职存储团队的大规模企业 [16][21]。
- **Rook**（Apache-2.0，CNCF 毕业）：在 K8s 上跑 Ceph 的标准 Operator（读 CephCluster CR 起 OSD/MON/MGR/MDS），继承 Ceph 全部运维复杂度 [16][21]。
- **JuiceFS**（Apache-2.0，~14.1k star，v1.4.0-rc1/2026-06）：对象存储上的 POSIX 文件系统（数据落 S3、元数据落 Redis/MySQL/TiKV），最适合 ML 训练数据集共享/大文件读多；公有云无直接托管等价（≈EFS/FSx+S3）——**Olares 内置 JuiceFS** [18][16][1]。
- **CubeFS**（Apache-2.0，CNCF 毕业 2025-01，~5.6k star）：云原生分布式文件+对象存储，支持 POSIX/HDFS/S3，管理约 350PB（JD/NetEase/小米等），主打大数据与 AI/LLM [19][20]。
- **Longhorn**（Apache-2.0，SUSE/Rancher，v1.11.1/2026-04）：K8s 原生分布式块存储，最适合 3–20 节点通用有状态负载（数据库），无原生对象存储 [16]。
- **OpenEBS**（CNCF Sandbox）：容器附着存储（CAS），Mayastor 引擎用 NVMe-oF+SPDK，是"给数据库用的高性能 K8s PV"首选 [22][16]。

**置信度:** High（成熟度）/ Medium（MinIO 归档时间）　**依据:** 存储 2026 深评 + 官方 GitHub + CubeFS 毕业新闻 [16][18][19][20][22]。
**反方解释:** 个人/小集群未必需要重量级分布式存储——多数 2026 文建议单机优先 Longhorn 或轻量对象存储（Garage/SeaweedFS），而非 Ceph [16]；MinIO 归档细节仅第三方博客佐证，官方声明未取到 [17]。

## 3. 数据库中间件（PaaS 核心）

数据库是最典型的中间件——几乎每个应用都要一个库。以下按数据模型分子类，逐项目列出。Olares 的路线是"复用成熟单体 + KubeBlocks 托管"，共享单 PostgreSQL 16（兼全文检索+向量）+ KVRocks（Redis 兼容）为默认 [1]。

### 3.1 关系型
**公有云替代**：AWS RDS/Aurora｜Azure SQL Database｜GCP Cloud SQL/AlloyDB/Spanner [13]。
- **PostgreSQL**（PostgreSQL License）：新项目/复杂查询/JSONB/GIS/扩展生态与开放治理的首选——**Olares 共享主库**，KubeBlocks 收录（12–18 及 vanilla/supabase 变体）[23][24][15][1]。
- **Citus**（PostgreSQL 扩展）：把 PostgreSQL 变分布式（分布式 join/并行查询），最适合多租户 SaaS；托管对标 Azure Cosmos DB for PostgreSQL——**Olares 多节点用 Citus**；未见 KubeBlocks 独立 addon [23][1]。
- **MySQL**（GPLv2/商业双授权，8.4 LTS 支持到 2032）：读多 CRUD/LAMP 生态最强；KubeBlocks 收录 mysql/apecloud-mysql（含 MGR/Orchestrator）[23][15]。
- **Vitess**（Apache-2.0，CNCF 2019 毕业）：MySQL 分片编排层（YouTube/Slack/Booking 验证），托管代表 PlanetScale [25]。
- **MariaDB**（GPLv2）：独立治理的 MySQL 开源分支（Wikimedia 大规模用）；KubeBlocks 收录 mariadb addon [23][15]。

### 3.2 文档型
**公有云替代**：MongoDB Atlas/AWS DocumentDB｜Azure Cosmos DB for MongoDB｜GCP Firestore [13]。
- **MongoDB**（SSPL，8.0）：面向服务端高性能文档库（replica set+原生分片+聚合管道），DB-Engines 排名前列；KubeBlocks 收录（4.0–8.0 及 shard/mongos）——**Olares Market 可装** [26][15][1]。
- **CouchDB**（Apache-2.0，3.5.x）：多主复制+HTTP/REST+离线优先（PouchDB 同步），查询依赖预定义 view；公有云对标 IBM Cloudant；未见 KubeBlocks addon [26][27]。

### 3.3 KV / 缓存
**公有云替代**：AWS ElastiCache｜Azure Cache for Redis｜GCP Memorystore [13]。
- **Redis**（≤7.2 BSD-3；7.4–7.8 RSALv2/SSPLv1；≥8.0 三授权含 AGPLv3）：内存 KV/缓存/数据结构服务器事实标准；2024 改照催生 BSD 许可 fork **Valkey**（Linux Foundation，已成 ElastiCache/Memorystore 默认引擎）；KubeBlocks 收录 redis（含 8.x、sentinel/cluster）[28][29][15]。
- **KVRocks**（Apache-2.0，2023-06 成 ASF 顶级项目）：基于 RocksDB、兼容 Redis 协议的持久化磁盘 KV，用磁盘换内存降本——**Olares 内置 KVRocks 作 Redis 兼容层** [30][31][1]。
- **Dragonfly**（BSL 1.1，2029-03 转 Apache-2.0）：从零重写、多线程 shard-per-thread，宣称 10–25× 吞吐；托管 Dragonfly Cloud [29]。

### 3.4 向量库
**公有云替代**：Amazon OpenSearch 向量引擎/Aurora pgvector｜Azure AI Search｜Vertex AI Vector Search [20][32]。
- **Qdrant**（Rust，Apache-2.0，~29k star）：低延迟过滤搜索、单二进制轻运维；KubeBlocks 收录 qdrant（1.5.0→1.16.3）[32][33][15]。
- **Weaviate**（Go，BSD-3，~14k star）：AI-native，内置向量化模块+GraphQL+原生多租户；KubeBlocks 收录 weaviate [32][33][15]。
- **Milvus**（Go/C++，Apache-2.0，~44k star，LF AI & Data 2021 毕业、**非 CNCF**）：存算分离可扩至十亿级，支持 IVF/HNSW/DiskANN/GPU；KubeBlocks 有 milvus operator [34][32][15]。
- **pgvector**（PostgreSQL 扩展）：中小规模"已在 Postgres 上就够"的替代，免单独运维——**Olares 共享 PostgreSQL 即带向量能力** [32][1]。

### 3.5 时序库
**公有云替代**：Amazon Timestream（含 Timestream for InfluxDB）｜Azure Data Explorer｜GCP 无原生（多用 Bigtable/第三方）[45]。
- **InfluxDB**（v3.0 转 Apache-2.0+MIT）：时序库鼻祖，历史上水平集群需企业版；KubeBlocks 收录 influxdb [35][37][14]。
- **VictoriaMetrics**（Apache-2.0）：Prometheus 长期存储/PromQL 兼容、OSS 集群版免费水平扩展；KubeBlocks 收录 victoria-metrics [35][14]。
- **GreptimeDB**（Rust，Apache-2.0，v1.0 GA 2026-04）：云原生统一可观测库（指标+日志+trace 同引擎、对象存储原生）；KubeBlocks addon 列表含 greptimedb [35][36][14]。
- **TDengine**（AGPLv3，社区版含免费集群）：面向 IoT/工业物联网的高频时序 [35][37]。

### 3.6 图数据库
**公有云替代**：Amazon Neptune / Neptune Analytics（支持图+向量 GraphRAG）[44]。
- **NebulaGraph**（C++，Apache-2.0，~12.2k star，v3.8.0/2024-05）：分布式图库，用 Multi-Group Raft 自带一致性（不依赖外部 etcd/ZooKeeper），仅进入 CNCF Landscape 而非 CNCF 托管；KubeBlocks Graph 类列名但无 operator 落地 [38][14]。

### 3.7 分布式协调 / 元数据
**公有云替代**：多为托管 K8s 内置，无独立消费级服务。
- **etcd**（Apache-2.0，CNCF 毕业）：强一致分布式 KV，K8s 的默认元数据存储；KubeBlocks 提供 etcd-operator（Raft HA/快照，3.5.x/3.6.1）——**Olares 内置 etcd** [42][14][1]。
- **Kine**（"Kine is not etcd"，Apache-2.0，~2.3k star）：etcd-shim，把 etcd API 翻译成 SQLite/Postgres/MySQL/NATS，让 K8s（及 Milvus 等）用关系库替代 etcd，减少组件——K3s 默认即用它；Milvus 有换 Kine 的公开 FR（Issue #41113，open）[42][43]。
- **ZooKeeper**（Apache-2.0）：集中式配置/命名/分布式同步（Kafka<4.0、Pulsar 等曾依赖）；KubeBlocks 收录 zookeeper addon [14]。

### 3.8 全文检索
**公有云替代**：Amazon OpenSearch Service/Serverless｜Elastic Cloud｜Azure AI Search [41]。
- **Elasticsearch**（AGPLv3/SSPL/ELv2 三许可择一，9.3.3/2026-04）：基于 Lucene 的搜索/日志分析标杆；KubeBlocks 有 elasticsearch-operator（6.8→8.15）[39][41][15]。
- **OpenSearch**（纯 Apache-2.0，AWS 2021 分叉、2024 移交 Linux Foundation OSSF，3.6/2026-04）：无许可顾虑的 ES 替代；KubeBlocks 收录 opensearch——**Olares 用共享 PostgreSQL 兼全文检索，未内置 ES/OpenSearch** [40][41][14][1]。

**置信度:** High（许可/成熟度多有官方源）/ Medium（KubeBlocks 逐引擎版本、Milvus/Nebula operator 落地）
**依据:** 官方 GitHub/基金会页 + KubeBlocks addons + 2026 对比 [15][28][34][39][40][41][42]。
**反方解释:** ①"SSPL/RSALv2 是否算真开源"OSI 未承认，Redis/MongoDB 官方却称 "source available/open source options"，口径不一 [28][39][40]。②pgvector 是否已足够替代专用向量库——中小场景成立，十亿级/GPU 仍需 Milvus [32]。③个人云是否真需要专用图/时序库存疑（KubeBlocks 中 Nebula/时序多无 operator 落地）[14][38]。

## 4. 消息 / 流

### 4.1 消息队列 / 事件流
**认知**：应用间异步解耦的中枢——任务队列、事件流、日志聚合、CDC。**公有云替代**：AWS SQS·MSK·Kinesis｜Azure Service Bus·Event Hubs｜GCP Pub/Sub [60][63][12]。
- **NATS**（Go，CNCF 孵化，2026-02 提交毕业申请审核中）：极轻量单二进制，pub/sub+request/reply+streaming（JetStream）一体，核心亚毫秒延迟、三节点 JetStream 每节点 <256MB RAM——**Olares 内置 NATS 作默认 MQ**；不在 KubeBlocks 托管范围 [59][62][55][1]。
- **RabbitMQ**（MPL-2.0）：成熟 AMQP 代理，擅长任务队列/竞争消费者/复杂路由/RPC，中等吞吐、运维比 Kafka 轻；KubeBlocks 收录 rabbitmq（3.8–4.2）[55][14]。
- **Apache Kafka**（Apache-2.0，ASF 顶级）：分区式持久提交日志，事件流事实标准，4.0(2025) 移除 ZooKeeper（KRaft）；调优后单 broker ~1M msg/s，运维中等偏重；K8s 上标准 operator＝**Strimzi**（CNCF 孵化）；KubeBlocks 亦收录 kafka [55][61][14]。
- **Apache Pulsar**（Apache-2.0，ASF 顶级）：broker/BookKeeper 存算分离，原生多租户/跨地域/分层存储，组件最多最重；KubeBlocks 收录 pulsar [55][14]。

### 4.2 大数据流处理
**认知**：对无界数据流做有状态实时计算（≠消息队列）。**公有云替代**：AWS Managed Service for Apache Flink｜Azure Stream Analytics｜GCP Dataflow(Beam) [57][58]。
- **Apache Flink**（Apache-2.0）：原生逐事件流引擎，事件时间+watermark+增量 checkpoint、sub-100ms、exactly-once，适合欺诈检测/CEP/实时告警（Netflix 15,000+ 作业）[56][57][58]。
- **Apache Spark Structured Streaming**（Apache-2.0）：构建在 Spark SQL 上的 micro-batch，批流统一、复用 MLlib/Delta，延迟约 100ms–数秒，适合分析型 ETL [56][57][58]。
- **Apache Storm**（Apache-2.0）：最早的逐元组流处理器，2026 属 legacy，已被 Flink/Spark 取代 [56]。

**置信度:** High　**依据:** 官方文档 + CNCF/ASF + 2026 对比 [55][56][57][59][61][62]。
**反方解释:** 个人云/单机几乎无流处理与重型 MQ 负载证据——资源谱系 NATS < RabbitMQ < Kafka < Pulsar，Olares 内置最轻的 NATS 正与"个人云优先轻量"一致，Kafka/Pulsar/Flink/Spark 均非个人云默认 [55][59]。（NATS 是否已"毕业"以 CNCF TOC 为准，AS_OF 仍孵化 [62]。）

## 5. 平台中间件（可观测 / Serverless / Workflow / 密钥）

### 5.1 可观测
**认知**：metrics/logs/traces 三支柱，是运维应用的"眼睛"。**公有云替代**：CloudWatch·X-Ray｜Azure Monitor·App Insights｜Cloud Monitoring·Trace [10]。
- **OpenTelemetry**（Apache-2.0，CNCF 2026-05 毕业）：厂商中立的采集/导出**事实标准**，正取代各家私有 SDK/agent——**Olares 内置 OTel** [64][1]。
- **Prometheus**（Apache-2.0，CNCF 毕业）：时序指标采集+PromQL+告警金标准——**Olares 内置 Prometheus** [64][1]。
- **Jaeger**（Apache-2.0，CNCF 2019 毕业）：分布式追踪标杆，后端支持 Badger(本地)/Cassandra/ES/Kafka [66]。
- **Grafana**（Grafana Labs，非 CNCF）：可视化面板事实标准——**Olares 内置 Grafana** [65][66][1]。
- **Grafana Loki**（Grafana Labs，非 CNCF）：日志聚合，ELK 的轻量开源替代；**Grafana Tempo** 为低成本 tracing（TraceQL）——两者是"单 UI 打通 metrics→traces→logs"的关键 [66]。

### 5.2 Serverless / FaaS
**认知**：请求驱动、按需扩缩（含 scale-to-zero）的函数/服务运行层。**公有云替代**：AWS Lambda｜Azure Functions｜GCP Cloud Functions·Cloud Run [67]。
- **Knative**（Apache-2.0，CNCF 2025-09 毕业）：含 Serving(自动扩缩/scale-to-zero)+Eventing(CloudEvents)+Functions，Google Cloud Run 底层即基于它；缺点是重（常需 Istio/Kourier）[67][68]。
- **OpenFaaS**（社区版 MIT，非 CNCF）：开发者体验好（简洁 CLI/20+ 模板），但 scale-to-zero/SSO 多在 Pro 商业版 [67][69]。
- **Fission**（Apache-2.0，CNCF Sandbox）：暖池架构 <100ms 冷启动，社区较小 [67]。

### 5.3 工作流编排
**认知**：把多步任务编成可调度/可重试/可恢复的流程。**公有云替代**：AWS Step Functions｜GCP Cloud Workflows｜Azure Logic Apps [70]。
- **Argo Workflows**（Apache-2.0，CNCF 2022 毕业，~16.8k star）：K8s 原生、以容器为 step 的 DAG/step 引擎，适合 CI/CD、ML 训练、并行批处理——**Olares 内置 Argo Workflows**；配套 **Argo Events** 做事件驱动触发 [75][76][1]。
- **Temporal**（MIT，~19.7k star）：主打"持久化执行"——用普通代码写可跨崩溃/重试/长等待存活的有状态业务流 [70][71]。
- **Apache Airflow**（Apache-2.0，~45k star）：数据工程批处理 ETL/ELT 调度霸主（Python DAG + 海量 operator，Cloud Composer/MWAA 均基于它）[70][71]。

### 5.4 密钥 / 配置管理
**认知**：集中存取密钥/证书/凭据并做审计与轮换。**公有云替代**：AWS Secrets Manager·KMS｜Azure Key Vault｜GCP Secret Manager [72][74]。
- **HashiCorp Vault**（2023 起 BUSL/BSL，2025 被 IBM 以 $64 亿收购）：杀手锏＝动态密钥（短 TTL 临时凭据）+审计+细粒度策略，缺点是重、成关键路径 HA [72][74]。
- **OpenBao**（MPL-2.0，OpenSSF/Linux Foundation）：Vault 的 API 兼容开源分叉，为"因 BUSL 离开 Vault"提供最低迁移摩擦 [73]。
- **Infisical**（核心 MIT，开放核心）：主打开发者体验（UI/CLI/按人环境/版本），适合小团队——**Olares 内置 Vault/Infisical** [72][73][1]。
- **External Secrets Operator（ESO）**（Apache-2.0）：不是存储后端而是同步器，把 Vault/OpenBao/云库同步进 K8s Secret，是 K8s 重度环境事实标准 [72][73]。

**置信度:** High（CNCF 状态/许可多有官方公告）/ Medium（部分 star 与 Grafana/Loki 许可版本号）
**依据:** CNCF 公告/项目页 + 官方 GitHub + 2026 对比 [64][68][75][76][73]。
**反方解释:** 个人云是否需要完整 LGTM（Loki/Grafana/Tempo/Mimir）全链、Knative（需 Istio）、多副本 Vault HA——多数 homelab 讨论认为对单用户属过度工程，更可能只用 Prometheus+单面板/日志 + K8s 原生 Secret+etcd 加密；未见针对"个人云最小充分栈"的第三方实测 [72]。

## 6. 企业 / 大数据（个人云非重点）

**认知**：面向企业级横向扩展、高并发、TB–PB 级的重型引擎，默认多节点/三副本，与个人云"单机/小集群就近服务"的诉求错位——**列此存目，个人云非重点**。

### 6.1 分布式 SQL（NewSQL）
**公有云替代**：Amazon Aurora DSQL / Google Cloud Spanner [46]。
- **TiDB**（Apache-2.0，MySQL 兼容，Raft，HTAP，8.5.4/2025-11）：自动分片+HTAP+云原生；KubeBlocks 收录 tidb [46][47][15]。
- **OceanBase 社区版**（MulanPubL-2.0，非 Apache-2.0；新库 seekdb 才 Apache-2.0）：Paxos 三副本、MySQL+Oracle 双兼容，金融级极高并发/替 Oracle；KubeBlocks 收录 oceanbase-ce [48][15]。
- **PolarDB-X**（阿里云，Apache-2.0）：MySQL 兼容、存算分离；KubeBlocks 收录 polardb-x [15]。

### 6.2 OLAP 数仓
**公有云替代**：Amazon Redshift｜Azure Synapse｜GCP BigQuery [49]。
- **ClickHouse**（Apache-2.0）：单进程二进制、shared-nothing、MergeTree，强在高基数单表扫描/写入吞吐/压缩/运维简单，弱在多表 JOIN 与频繁 upsert；**唯一个别可用于个人云的重型引擎**（单机 4 核 8GB+ 调优做本地日志/时序分析）；KubeBlocks 收录 clickhouse [49][52][15]。
- **Apache Doris**（Apache-2.0，ASF 顶级）：FE+BE MPP+CBO，主键模型支持真 upsert/delete，强在多表 JOIN/高并发用户面分析；KubeBlocks 收录 [49][15]。
- **StarRocks**（Apache-2.0，Linux 基金会，早期 Doris 血统重写）：综合领先在 JOIN/upsert/并发；KubeBlocks 收录 starrocks-ce [49][15]。

### 6.3 分布式 SQL 查询引擎（联邦 / 数据湖）
**公有云替代**：AWS Athena/EMR｜GCP BigQuery(外部表)｜Azure Synapse Serverless [50][51]。
- **Trino**（Apache-2.0，Trino 软件基金会，原 PrestoSQL）：连接器最广（30+：Hive/Iceberg/Delta/Hudi/PG/ES/Kafka…）、迭代最快，2026 联邦/湖仓查询默认首选 [50][51]。
- **Presto**（Apache-2.0，Meta 维护 PrestoDB）：稳定、商业支持清晰，纯 OLAP 略慢于 Trino [50][51]。
- **Impala**（Cloudera）：MPP 绕过 MapReduce，强在 HDFS/Hive/Kudu 低延迟 BI [50]。
- **Hive**（Apache-2.0，2008）：HiveQL 编译成 MapReduce/Tez/Spark，如今主要用于重批量 ETL，延迟高 [51]。
- **共同点**：本身不存数据、需外部 Hive Metastore/数据湖/多源，是"大数据平台上的查询层"，与个人云错位；**KubeBlocks 明确不托管 Presto/Trino**（官方建议改用 Doris/StarRocks 同步后查询）[51][54]。

**置信度:** High（架构/许可）/ Medium（单节点最小内存无官方硬下限）
**依据:** 2026 OLAP/查询引擎对比 + KubeBlocks 官方回复 + Altinity 单机实测 [49][51][52][54]。
**反方解释:** ClickHouse 单机"也很能打"——配好的单台服务器能扛传统库跪掉的负载；个人数据分析未必用不上轻量 OLAP，但更常用零基础设施的 **DuckDB/chDB**（进程内、直查 Parquet），故"OLAP 完全不适合个人云"应修正为"重型集群不适合，轻量单机/嵌入式有真实场景" [52][53]。

## 核心争议

- **争议 1（过度工程）:** Olares 在单机跑完整 K8s + KubeBlocks 是"复用云原生事实标准带来一致性/可扩展/可移植" [1][3] 还是"对单用户过度工程、抬高资源与运维开销"——缺乏第三方独立实测，是本领域最大开放问题 [7]。
- **争议 2（是否真开源）:** Redis(≤7.2 前)/MongoDB 的 SSPL、Elasticsearch 的 SSPL/ELv2 均非 OSI 认可，官方却表述为"source available/open source" [28][39][40]；这正是 Valkey、OpenSearch 分叉与云厂商改用它们的根因。
- **争议 3（企业引擎 vs 个人云）:** 分布式 SQL/OLAP/查询引擎/流处理默认多节点、面向企业 [46][49][51]；但 ClickHouse 单机、DuckDB/chDB 证明"轻量单机分析"在个人云有真实窗口 [52][53]。
- **争议 4（Longhorn/NATS 状态）:** Longhorn CNCF 级别来源冲突（Incubating vs Graduated）、NATS 是否已毕业（AS_OF 仍孵化）——均以 CNCF 官方为准、标不确定 [16][62]。

## 关键发现

- **发现 1（分层平替完整）:** Olares 五大类核心子类都有内置件或对应开源件，且每类都有清晰公有云对标——这是"把公有云 IaaS/PaaS 一次装齐、数据归用户"叙事的技术底座 [1][10][13]。
- **发现 2（KubeBlocks 是中间件层的关键抓手）:** "一个 operator 管所有数据库/中间件 + OlaresManifest 声明式依赖 + 自动注入凭据"是方向 6 里最硬的技术差异点，SEO 上可做 "KubeBlocks alternative"、"self-hosted DBaaS"、"database operator" 及各引擎 "X on Olares" 长尾 [2][3][11][12]。
- **发现 3（缺口与取舍）:** Olares 未内置 ES/OpenSearch（用 PostgreSQL 全文检索兜底）、专用图/时序库、完整可观测追踪全链、Serverless；企业·大数据类刻意不作重点——多属进阶/企业长尾 [1][14]。
- **发现 4（轻量优先的路线）:** Olares 选 K3s(默认 Kine)、KVRocks(磁盘换内存)、NATS(最轻 MQ)、Infisical/Vault，体现"个人云优先轻量单体"的一致取舍，而非堆企业级重组件 [1][30][42][59]。

## 局限性与未来方向

### 本研究局限
- **Olares 内置情况以官方架构/开发者文档为准**，未逐一核验最新版本组件清单；ES/图/时序是否 Market 有上架、可观测全链是否内置存不确定。
- **CNCF 级别 / star / 版本 / 许可为快变数据**（AS_OF 2026-07-05）：Longhorn 级别、MinIO 归档时间、NATS 毕业状态、SSPL 口径均有来源冲突，已标不确定，引用前以 cncf.io / 官方为准。
- **KubeBlocks 逐引擎 addon 版本与 operator 落地**（Milvus/Nebula/时序）未全部取到官方矩阵；无 academic 源（工程领域，用官方占比 50% 补偿）。
- **企业·大数据单节点最小可运行内存**缺官方硬下限对照，个人云可行性靠架构推断。

### 未来方向
- 对 Olares 已内置的高价值中间件（JuiceFS、KVRocks、NATS、Argo Workflows、pgvector）各做一篇 "self-hosted X / X on Olares" 长尾内容；对 KubeBlocks 做一篇 "self-hosted DBaaS / database operator" 主题文。
- 反向核验 Olares 官方最新组件清单，确认 ES/OpenSearch、图/时序、可观测追踪的内置/上架状态，补齐"缺口"判断。
- 与 [cloud-infra-taxonomy.md](/Users/pengpeng/seo/directions/tech/research/cloud-infra-taxonomy.md)（宽 7 大类）、[ai-infra.md](/Users/pengpeng/seo/directions/tech/research/ai-infra.md)（AI 基础设施）保持分工：本文深挖中间件/PaaS + 计算/存储底座，避免重复登记。

## 参考文献

[1] Olares. "System architecture". Source-Type: official. As Of: 2026-07. https://docs.olares.com/developer/concepts/system-architecture.html
[2] ApeCloud. "apecloud/kubeblocks". Source-Type: official. As Of: 2026-07. https://github.com/apecloud/kubeblocks
[3] KubeBlocks. "Introduction". Source-Type: official. As Of: 2026-06. https://kubeblocks.io/docs/preview/user_docs/overview/introduction
[4] KubeBlocks. "How to Manage Database Clusters Without a Dedicated Operator". Source-Type: official. As Of: 2026-06. https://kubeblocks.io/blog/how-to-manage-database-clusters-without-a-dedicated-operator
[5] IBM. "IaaS, PaaS, SaaS: What's the difference?". Source-Type: secondary-industry. As Of: 2026-06. https://www.ibm.com/think/topics/iaas-paas-saas
[6] Google Cloud. "PaaS vs IaaS vs SaaS". Source-Type: official. As Of: 2026-06. https://cloud.google.com/learn/paas-vs-iaas-vs-saas
[7] DEV Community. "The Definitive Guide to Lightweight Kubernetes". Source-Type: community. As Of: 2025-12. https://dev.to/pendelabhargavasai/the-definitive-guide-to-lightweight-kubernetes-kind-minikube-microk8s-k3s-vcluster-k0s-and-3be1
[8] SFEIR Institute. "Kubernetes Distributions Comparison Table 2026". Source-Type: secondary-industry. As Of: 2026-01. https://institute.sfeir.com/en/kubernetes-training/table-comparison-distributions-kubernetes-2026/
[9] Pickuma. "K3s vs MicroK8s vs k0s". Source-Type: secondary-industry. As Of: 2026-01. https://pickuma.com/for-dev/k3s-vs-microk8s-vs-k0s-lightweight-kubernetes-small-teams/
[10] cloudai.pt. "AWS vs Azure vs Google Cloud: Comprehensive Service Comparison". Source-Type: secondary-industry. As Of: 2026-01. https://cloudai.pt/aws-vs-azure-vs-google-cloud-comprehensive-service-comparison/
[11] Olares. "System-injected runtime values". Source-Type: official. As Of: 2026-06. https://www.olares.com/docs/developer/develop/app-sys-injected-variables
[12] Olares. "Middleware in Olares". Source-Type: official. As Of: 2026-06. https://www.olares.com/docs/developer/develop/mw-overview
[13] Pluralsight. "AWS vs Azure vs GCP cloud comparison: Databases". Source-Type: secondary-industry. As Of: 2026-01. https://www.pluralsight.com/resources/blog/cloud/aws-vs-azure-vs-gcp-cloud-comparison-databases
[14] KubeBlocks. "Supported Addons". Source-Type: official. As Of: 2026-06. https://kubeblocks.io/docs/preview/user_docs/overview/supported-addons
[15] ApeCloud. "apecloud/kubeblocks-addons". Source-Type: official. As Of: 2026-06. https://github.com/apecloud/kubeblocks-addons
[16] youngju.dev. "Distributed Storage 2026 Deep Dive". Source-Type: secondary-industry. As Of: 2026-05. https://www.youngju.dev/blog/culture/2026-05-16-distributed-storage-minio-seaweedfs-ceph-garage-juicefs-openebs-longhorn-rook-2026-deep-dive.en
[17] LLMS3. "What Survived MinIO: The Post-Archive S3 Server Landscape". Source-Type: community. As Of: 2026-05. https://llms3.com/blog/what-survived-minio-may-2026
[18] juicedata. "juicedata/juicefs". Source-Type: official. As Of: 2026-06. https://github.com/juicedata/juicefs
[19] cubefs. "cubefs/cubefs". Source-Type: official. As Of: 2026. https://github.com/cubefs/cubefs
[20] InfoQ. "CubeFS Graduates from CNCF". Source-Type: journalism. As Of: 2025-03. https://www.infoq.com/news/2025/03/cubefs-cncf-graduation/
[21] OneUptime. "How to Compare Ceph vs MinIO for Object Storage". Source-Type: secondary-industry. As Of: 2026-03. https://oneuptime.com/blog/post/2026-03-31-rook-compare-ceph-vs-minio-object-storage/view
[22] openebs. "openebs/openebs". Source-Type: official. As Of: 2026. https://github.com/openebs/openebs
[23] Patotski. "Postgres vs MySQL in 2026". Source-Type: community. As Of: 2026. https://patotski.com/blog/postgres-vs-mysql/
[24] UpCloud. "PostgreSQL vs MySQL: Comprehensive Guide". Source-Type: secondary-industry. As Of: 2026. https://upcloud.com/global/blog/postgresql-vs-mysql-practical-guide-modern-workloads/
[25] CNCF. "Vitess". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/vitess/
[26] OneUptime. "MongoDB vs CouchDB: Document DB Comparison". Source-Type: secondary-industry. As Of: 2026-03. https://oneuptime.com/blog/post/2026-03-31-mongodb-mongodb-vs-couchdb-document-database-comparison/view
[27] Better Stack. "CouchDB vs MongoDB". Source-Type: secondary-industry. As Of: 2026. https://betterstack.com/community/guides/databases/couchdb-vs-mongodb/
[28] Redis. "Licenses". Source-Type: official. As Of: 2026. https://redis.io/legal/licenses/
[29] FlowVerify. "Redis, Valkey, or Dragonfly: how to decide". Source-Type: secondary-industry. As Of: 2026. https://www.flowverify.co/blog/redis-valkey-dragonfly-2026
[30] Apache. "apache/kvrocks". Source-Type: official. As Of: 2026. https://github.com/apache/kvrocks
[31] Apache. "ASF Announces Apache Kvrocks as TLP". Source-Type: official. As Of: 2023-06. https://news.apache.org/foundation/entry/the-apache-software-foundation-announces-new-top-level-project-apache-kvrocks
[32] builderai. "Qdrant vs Milvus vs Weaviate vs LanceDB". Source-Type: secondary-industry. As Of: 2026-05. https://builderai.tools/blog/vector-database-benchmarks-qdrant-milvus-weaviate-lancedb
[33] elest.io. "Qdrant vs Weaviate vs Milvus". Source-Type: secondary-industry. As Of: 2026. https://blog.elest.io/qdrant-vs-weaviate-vs-milvus-which-vector-database-for-your-rag-pipeline/
[34] LF AI & Data. "Milvus". Source-Type: official. As Of: 2026. https://lfaidata.foundation/projects/milvus/
[35] Tiger Data. "The Best Time-Series Databases Compared". Source-Type: secondary-industry. As Of: 2026. https://www.tigerdata.com/learn/the-best-time-series-databases-compared
[36] Greptime. "GreptimeDB as an Alternative to InfluxDB". Source-Type: official. As Of: 2026-04. https://greptime.com/tech-content/2025-04-15-influxdb-comparison-greptimedb
[37] InfluxData. "InfluxDB vs TDengine". Source-Type: official. As Of: 2026. https://www.influxdata.com/comparison/influxdb-vs-tdengine/
[38] vesoft-inc. "vesoft-inc/nebula". Source-Type: official. As Of: 2026-05. https://github.com/vesoft-inc/nebula
[39] Elastic. "FAQ on Software Licensing". Source-Type: official. As Of: 2026. https://www.elastic.co/pricing/faq/licensing
[40] OpenSearch. "FAQ". Source-Type: official. As Of: 2026. https://opensearch.org/faq/
[41] BigData Boutique. "OpenSearch vs Elasticsearch Compared 2026". Source-Type: secondary-industry. As Of: 2026-05. https://bigdataboutique.com/blog/opensearch-vs-elasticsearch-compared
[42] k3s-io. "k3s-io/kine". Source-Type: official. As Of: 2026-04. https://github.com/k3s-io/kine
[43] milvus-io. "Use kine as a replacement of etcd (Issue #41113)". Source-Type: official. As Of: 2025-04. https://github.com/milvus-io/milvus/issues/41113
[44] AWS. "Amazon Neptune". Source-Type: official. As Of: 2026. https://aws.amazon.com/neptune/
[45] AWS. "Amazon Timestream". Source-Type: official. As Of: 2026. https://aws.amazon.com/timestream/
[46] PingCAP. "TiDB vs OceanBase 2026 Comparison Guide". Source-Type: secondary-industry. As Of: 2026-01. https://www.pingcap.com/compare/tidb-vs-oceanbase/
[47] Wikipedia. "TiDB". Source-Type: other(reference). As Of: 2025-11. https://en.wikipedia.org/wiki/TiDB
[48] OceanBase. "Database Overview". Source-Type: official. As Of: 2026-01. https://oceanbase.github.io/docs/user_manual/quick_starts/en-US/chapter_01_overview_of_the_oceanbase_database/overview
[49] iotdigitaltwinplm. "ClickHouse vs Doris vs StarRocks: OLAP ADR 2026". Source-Type: secondary-industry. As Of: 2026-05. https://iotdigitaltwinplm.com/clickhouse-vs-doris-vs-starrocks-olap-adr-2026/
[50] Ksolves. "Trino vs. Presto: Which to Use in 2026". Source-Type: secondary-industry. As Of: 2026-01. https://www.ksolves.com/blog/big-data/trino-vs-presto
[51] iotdigitaltwinplm. "Trino vs Presto vs Apache Spark 2026". Source-Type: secondary-industry. As Of: 2026-05. https://iotdigitaltwinplm.com/trino-vs-presto-vs-apache-spark-lakehouse-query-engines-2026/
[52] Altinity. "Deploying Single-Node ClickHouse on Small Servers". Source-Type: secondary-industry. As Of: 2026-02. https://altinity.com/blog/deploying-single-node-clickhouse-on-small-servers
[53] Tinybird. "Best ClickHouse alternatives in 2026". Source-Type: secondary-industry. As Of: 2026-04. https://www.tinybird.co/blog/clickhouse-alternatives
[54] ApeCloud. "KubeBlocks Discussion #7464 (no Presto/Trino support)". Source-Type: official. As Of: 2024-06. https://github.com/apecloud/kubeblocks/discussions/7464
[55] BackendBytes. "Kafka vs RabbitMQ vs NATS vs SQS". Source-Type: community. As Of: 2026-01. https://backendbytes.com/articles/message-queue-comparison/
[56] DesignGurus. "Kafka Streams vs Apache Flink vs Apache Storm". Source-Type: secondary-industry. As Of: 2026-01. https://www.designgurus.io/blog/kafka-streams-apache-flink-apache-storm
[57] Confluent. "Spark Streaming vs Apache Flink". Source-Type: secondary-industry. As Of: 2026-01. https://www.confluent.io/compare/spark-streaming-vs-flink/
[58] Onehouse. "Flink vs Kafka Streams vs Spark Structured Streaming". Source-Type: secondary-industry. As Of: 2026-01. https://www.onehouse.ai/blog/apache-spark-structured-streaming-vs-apache-flink-vs-apache-kafka-streams-comparing-stream-processing-engines
[59] NATS. "JetStream". Source-Type: official. As Of: 2026-06. https://docs.nats.io/nats-concepts/jetstream
[60] AWS. "Amazon MSK". Source-Type: official. As Of: 2026-06. https://aws.amazon.com/msk/
[61] CNCF. "Strimzi". Source-Type: official. As Of: 2026-06. https://www.cncf.io/projects/strimzi/
[62] CNCF TOC. "NATS Graduation Application (Issue #2042)". Source-Type: official. As Of: 2026-02. https://github.com/cncf/toc/issues/2042
[63] Google Cloud. "What is Pub/Sub?". Source-Type: official. As Of: 2026-06. https://docs.cloud.google.com/pubsub/docs/overview
[64] CNCF. "CNCF Announces OpenTelemetry's Graduation". Source-Type: official. As Of: 2026-05. https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/
[65] Grafana Labs. "Grafana Labs joins the CNCF Governing Board". Source-Type: official. As Of: 2026-06. https://grafana.com/blog/grafana-labs-joins-the-cncf-governing-board-as-a-platinum-member-of-the-open-source-foundation/
[66] Ajit Singh. "Distributed Tracing: Jaeger vs Tempo vs Zipkin". Source-Type: community. As Of: 2026-01. https://singhajit.com/distributed-tracing-jaeger-vs-tempo-vs-zipkin/
[67] DevOpsBoys. "Knative vs OpenFaaS vs Fission: Serverless on Kubernetes 2026". Source-Type: secondary-industry. As Of: 2026-01. https://devopsboys.com/blog/knative-vs-openfaas-vs-fission-serverless-kubernetes-2026
[68] CNCF. "Knative". Source-Type: official. As Of: 2026-06. https://www.cncf.io/projects/knative/
[69] Palark. "Overview of self-hosted serverless frameworks for Kubernetes". Source-Type: secondary-industry. As Of: 2025-12. https://palark.com/blog/open-source-self-hosted-serverless-frameworks-for-kubernetes/
[70] xgrid. "Temporal vs Airflow vs Argo: Workflow Orchestration Guide". Source-Type: secondary-industry. As Of: 2026-01. https://www.xgrid.co/resources/temporal-vs-airflow-vs-argo-workflow-orchestration/
[71] pracdata. "State of Workflow Orchestration Systems 2025". Source-Type: secondary-industry. As Of: 2025-12. https://www.pracdata.io/p/state-of-workflow-orchestration-ecosystem-2025
[72] rkssh. "Kubernetes Secrets Management in 2026: Vault vs ESO vs Infisical". Source-Type: community. As Of: 2026-01. https://rkssh.com/blog/kubernetes-secrets-management-vault-eso-infisical
[73] Jorijn Schrijvershof. "HashiCorp Vault vs OpenBao: thorough comparison". Source-Type: community. As Of: 2026-04. https://jorijn.com/en/blog/hashicorp-vault-vs-openbao/
[74] GitGuardian. "Top 16 Secrets Management Tools and Platforms for 2026". Source-Type: secondary-industry. As Of: 2026-01. https://blog.gitguardian.com/top-secrets-management-tools/
[75] CNCF. "CNCF Announces Argo has Graduated". Source-Type: official. As Of: 2022-12. https://www.cncf.io/announcements/2022/12/06/the-cloud-native-computing-foundation-announces-argo-has-graduated/
[76] argoproj. "argoproj/argo-workflows". Source-Type: official. As Of: 2026-07. https://github.com/argoproj/argo-workflows/
