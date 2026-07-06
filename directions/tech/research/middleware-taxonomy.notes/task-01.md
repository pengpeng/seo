---
task_id: 01
role: 云基础设施分层与 PaaS 中间件框架分析师
status: complete
sources_found: 13
---

## Sources
[1] Olares system architecture | Olares Docs | https://docs.olares.com/developer/concepts/system-architecture.html | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[2] apecloud/kubeblocks (GitHub repo) | https://github.com/apecloud/kubeblocks | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[3] Introduction | KubeBlocks Docs | https://kubeblocks.io/docs/preview/user_docs/overview/introduction | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[4] How to Manage Database Clusters Without a Dedicated Operator? | KubeBlocks Blog | https://kubeblocks.io/blog/how-to-manage-database-clusters-without-a-dedicated-operator | Source-Type: official | As Of: 2026-06 | Authority: 8/10
[5] Iaas, Paas, Saas: What's the difference? | IBM | https://www.ibm.com/think/topics/iaas-paas-saas | Source-Type: secondary-industry | As Of: 2026-06 | Authority: 8/10
[6] PaaS vs IaaS vs SaaS | Google Cloud | https://cloud.google.com/learn/paas-vs-iaas-vs-saas | Source-Type: official | As Of: 2026-06 | Authority: 8/10
[7] The Definitive Guide to Lightweight Kubernetes (KIND/Minikube/MicroK8s/K3s/Vcluster/k0s/RKE2) | DEV Community | https://dev.to/pendelabhargavasai/the-definitive-guide-to-lightweight-kubernetes-kind-minikube-microk8s-k3s-vcluster-k0s-and-3be1 | Source-Type: community | As Of: 2025-12 | Authority: 6/10
[8] Kubernetes Distributions Comparison Table 2026 | SFEIR Institute | https://institute.sfeir.com/en/kubernetes-training/table-comparison-distributions-kubernetes-2026/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[9] K3s vs MicroK8s vs k0s: lightweight Kubernetes for small teams in 2026 | Pickuma | https://pickuma.com/for-dev/k3s-vs-microk8s-vs-k0s-lightweight-kubernetes-small-teams/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[10] AWS vs. Azure vs. Google Cloud: Comprehensive Service Comparison | cloudai.pt | https://cloudai.pt/aws-vs-azure-vs-google-cloud-comprehensive-service-comparison/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[11] System-injected runtime values | Olares Docs | https://www.olares.com/docs/developer/develop/app-sys-injected-variables | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[12] Middleware in Olares | Olares Docs | https://www.olares.com/docs/developer/develop/mw-overview | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[13] AWS vs Azure vs GCP cloud comparison: Databases | Pluralsight | https://www.pluralsight.com/resources/blog/cloud/aws-vs-azure-vs-gcp-cloud-comparison-databases | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 7/10

## Findings
- IaaS 提供虚拟化的算力/存储/网络，用户自管 OS、运行时、中间件、应用与数据；PaaS 再往上把 OS、运行时、中间件、数据库都托管，用户只写代码与数据。[5][6]
- "中间件"＝应用普遍依赖的第三方共享服务（数据库、消息队列、缓存、Web 服务器等）；IaaS 下需自己装管，PaaS 内置并通过 API 编排。[5]
- 容器编排以 Kubernetes 为标准，衍生轻量发行版：K3s（Rancher/SUSE，CNCF 认证，<100MB 单二进制，默认 SQLite/kine 替代 etcd，直用 containerd，边缘/生产）、k0s（Mirantis，~170MB，最贴近上游、零主机依赖）、MicroK8s（Canonical，snap 打包，addon 体系，dqlite HA，Ubuntu/工作站）、RKE2（Rancher/SUSE，CIS 加固 + FIPS 140-2，企业合规）。[7][8][9]
- 容器运行时层为 containerd 与 CRI-O；三大公有云托管 K8s 分别为 AWS EKS、Azure AKS、GCP GKE。[8][9]
- KubeBlocks 是 ApeCloud 开源的通用型 K8s Operator，用统一引擎无关的 CRD（Cluster 等）管理多种有状态引擎的生命周期与 day-2 运维，而非每种引擎一个专用 operator。[2][3]
- KubeBlocks 通过 Addon 机制扩展引擎：Addon 就是含 ClusterDefinition/ComponentDefinition/ComponentVersion 等 CR 的 Helm chart，声明式描述期望状态由框架 reconcile；截至 AS_OF 支持约 35 类引擎。[2][3][4]
- KubeBlocks 覆盖 RDBMS(MySQL/PostgreSQL)、缓存(Redis)、NoSQL(MongoDB)、消息队列(Kafka/Pulsar/RabbitMQ/RocketMQ)、向量库(Milvus/Qdrant/Weaviate)、数仓(ClickHouse/ES/Doris/StarRocks)。[2][3]
- KubeBlocks 许可 AGPL-3.0，语言 Go，创建于 2022-08，v1.0.0 于 2025-05-28 发布；AS_OF 2026-07 约 3,071 stars、80+ releases、最新 v1.1.0-beta.7(2026-06)。[2]
- Olares 对标公有云 IaaS/PaaS/SaaS 分层：基础设施层含容器编排(Linux 默认 K3s、可选 K8s；macOS 用 minikube)、containerd 运行时、Calico/CoreDNS/Envoy 网络、etcd、本地/S3/MinIO 存储、JuiceFS。[1]
- Olares 平台层中间件由 KubeBlocks 托管：关系库 PostgreSQL 16（全应用共享单实例、按账户隔离、兼全文检索+向量库）、KVRocks(Redis 兼容、基于 RocksDB 的持久化 KV)、NATS(消息队列)、JuiceFS(分布式文件系统)、Argo Workflows(工作流)、Vault/Infisical(密钥)、Prometheus/OpenTelemetry(可观测)。[1]
- Olares 中间件依赖为声明式：应用在 OlaresManifest.yaml 的 middleware 段声明 postgres/redis 等依赖，部署时系统自动把 host/port/username/password 等连接凭据注入 values.yaml（.Values.postgres.* / .Values.redis.*）；PostgreSQL、Redis 预装，MongoDB/MinIO/RabbitMQ/MySQL/MariaDB 需另装。[11][12]
- 公有云 PaaS 分类叫法：关系库 AWS RDS/Aurora｜Azure SQL Database｜GCP Cloud SQL/AlloyDB/Spanner；消息队列 AWS SQS｜Azure Service Bus/Queue Storage｜GCP Pub/Sub；事件总线 AWS EventBridge｜Azure Event Grid｜GCP Eventarc；NoSQL AWS DynamoDB｜Azure Cosmos DB｜GCP Firestore。[10][13]

## Deep Read Notes
### Source [1]: Olares system architecture (WebFetch 全文)
Key data: PostgreSQL 16 单实例共享+按账户隔离、兼全文检索/向量；KVRocks(RocksDB)、NATS、JuiceFS、Argo Workflows、Vault(基于 Padloc)/Infisical、Prometheus；Linux 默认 K3s、macOS minikube、运行时 containerd、etcd、Calico/CoreDNS/Envoy。
Key insight: Olares 明确"对标公有云 IaaS/PaaS/SaaS 三层给开源平替"，平台层＝中间件层；多节点用 Citus，PostgreSQL 未来或下沉到基础设施层。
Useful for: 支撑"Olares 中间件架构"整节 + IaaS/PaaS 分层锚点。

### Source [2]: apecloud/kubeblocks GitHub
Key data: AGPL-3.0；~3,071 stars/272 forks；创建 2022-08-22；35 类引擎；latest v1.1.0-beta.7(2026-06-24)；110 contributors。
Key insight: 单套 operator 代码 + 统一 CRD 管多引擎，是"通用数据库 operator"区别于单引擎 operator 的核心卖点。
Useful for: KubeBlocks 成熟度/许可/公司 事实锚点。

### Source [4]: KubeBlocks blog — 无专用 operator 管数据库
Key data: Addon = 含框架 CR 的 Helm chart；Lifecycle Actions 分三组；China Mobile Cloud 2 个月接入自研+开源库；~30 社区贡献 addon。
Key insight: 低代码 DBaaS 开发模型——开发者只写 YAML/脚本描述期望态，框架负责 reconcile 与备份/HA/配置管理。
Useful for: 支撑 KubeBlocks Addon 机制小节。

### Source [7]: DEV Community 轻量 K8s 权威对比
Key data: K3s(Rancher,2019,512MB,<100MB)、MicroK8s(Canonical,2018,540MB,snap)、k0s(Mirantis,2020,1GB,~230MB)、RKE2(Rancher,2021,4GB,~300MB,FIPS 140-2)。
Key insight: 无单一"最佳"轻量 K8s——K3s 赢边缘/生产、MicroK8s 赢 Ubuntu、k0s 赢零依赖贴上游、RKE2 赢合规。
Useful for: 支撑"容器编排大类"发行版定位/许可小节。

## Gaps
- 相反主张候选：个人云/单机场景是否真需要 Kubernetes + KubeBlocks 这类企业级 operator——K3s/RKE2 对比文与 homelab 讨论普遍认为单节点用 K8s 已属"重"，KubeBlocks 面向多引擎 DBaaS 更偏企业级；Olares 在单机跑完整 K8s + KubeBlocks 是否过度工程（资源开销 vs. 一致性/可扩展收益）缺乏第三方独立评测，仅有官方与社区评述，未搜到系统的"过度工程"反方实测数据。

## END
