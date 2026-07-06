# 云基础设施分类图：CNCF Landscape × 公有云服务 → Olares 映射底稿

> 研究日期: 2026-07-05 | 来源数: 28 | 字数: ~4300（含 7 张映射表） | 模式: Standard | AS_OF: 2026-07-05 | 官方源占比: 54%

## 摘要

本报告把 CNCF Cloud Native Landscape 的项目分类与三大公有云（AWS/Azure/GCP）的服务分类归一到 7 个基础设施大类，为 Olares（个人云操作系统）产出一张「大类 → 子类 | 开源 top | 公有云叫法 | Olares 内置/平替」的映射底稿。方法上以 CNCF 官方项目页/毕业公告、CNCF Landscape、Google Cloud 官方三云对照表、Gateway API 官方实现清单为权威锚点（官方源占比 54%），行业对比文补足开源 top 与采用度。核心结论：Olares 在**计算/编排、存储、网络接入、数据/中间件、身份/安全**五大类的核心子类已有内置组件或对应开源件（K3s、containerd、Calico、CoreDNS、Envoy Gateway、JuiceFS、MinIO、OpenEBS、Restic、Headscale、FRP、Authelia、LLDAP、Infisical、OPA、PostgreSQL/Citus、KVRocks、MongoDB、NATS 等），覆盖度高；主要缺口集中在**可观测的追踪/APM 链**（Olares 以 Netdata/Grafana 为主，未确认内置 Prometheus/Loki/Jaeger 全链）、**Service Mesh**（未内置 Istio/Linkerd，可能为个人云场景的刻意取舍）、**GitOps/镜像仓库/Serverless FaaS**（ArgoCD/Flux/Harbor/Knative 类未内置）。风险：CNCF 成熟度与 star 数为快变数据，引用前须以官网复核；个别来源对 Longhorn、Milvus 成熟度存在标注分歧，报告中已标注并以 CNCF 官方为准。

## 1. 计算 / 编排

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| 容器编排 | **Kubernetes**（CNCF Graduated 2018，事实标准）；**k3s**（CNCF Graduated，单二进制轻量发行版）[3][4] | EKS | AKS | GKE [5][16] | ✅ 内置 **K3s**（个人云底座）|
| 容器运行时 | **containerd**（CNCF Graduated，多数发行版默认；Docker 自 K8s 1.24 起不再作直接运行时）[1][17] | (Fargate 底层) | (AKS 默认 containerd) | (GKE 默认 containerd) | ✅ 内置 **containerd** |
| Serverless / FaaS | **Knative**（CNCF Graduated 2025-10，K8s 原生 Serverless）[2]；OpenFaaS（非 CNCF）| Lambda / Fargate / App Runner | Azure Functions / Container Apps | Cloud Run / Cloud Run functions [5] | ⬜ 缺口（未内置 Knative/FaaS 层）|

**解读:** Olares 用 K3s + containerd 直接复用云原生编排事实标准，二者均为 CNCF 毕业项目，编排层"血统"与公有云托管 K8s（EKS/AKS/GKE）一致，差异只在"谁托管控制面"。Serverless/FaaS 是明确缺口——Knative 是 CNCF 唯一毕业的 Serverless 层[2]，但个人云单机场景对 scale-to-zero FaaS 的刚需较弱。

**置信度:** High
**依据:** K8s/containerd/Knative 的 CNCF 状态均有官方页/毕业公告直接背书[1][2][3]；三云映射来自 GCP 官方对照表[5]。
**反方解释:** 有观点认为个人/单机场景根本不需要 K8s，Cloud Run/Container Apps 式 Serverless 更省心，Olares 选 K3s 反而增加了运维复杂度[5]。

## 2. 存储

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| 对象存储 | **MinIO**（S3 协议事实参考实现，单二进制）[14][18]；Ceph RGW [19] | S3 | Blob Storage | Cloud Storage [5] | ✅ 内置 **MinIO** |
| 块存储 | **OpenEBS**（容器原生，LocalPV/Mayastor）；**Longhorn**（CNCF Incubating，K8s 原生分布式块存储）[10][19] | EBS | Managed Disks | Hyperdisk / Persistent Disk [5] | ✅ 内置 **OpenEBS** |
| 分布式文件 | **JuiceFS**（POSIX over 对象存储）；CephFS [18][19] | EFS | Azure Files | Filestore [5] | ✅ 内置 **JuiceFS** |
| 备份 | **Restic**（增量加密备份）；**Velero**（CNCF Sandbox 2026-03，K8s 应用/PV 备份迁移）[11] | AWS Backup | Azure Backup | Backup and DR / Backup for GKE [5] | ✅ 内置 **Restic**（+ 文件同步用 **Seafile**）|

**解读:** 存储是 Olares 覆盖最完整的大类：对象(MinIO)、块(OpenEBS)、分布式文件(JuiceFS)、备份(Restic) 四个子类各有内置件，且都对齐 S3/EBS/EFS 三云模型。MinIO 已成"S3 参考实现，同一份代码跑遍 K8s/裸机/树莓派"[18]，与个人云"数据归用户"叙事天然契合。

**置信度:** High
**依据:** Longhorn/Velero 成熟度有 CNCF 官方页直接确认[10][11]；MinIO 定位有官方仓库 README 背书[14]；子类划分与开源 top 有 2026 深评交叉[18][19]。
**反方解释:** MinIO 社区版已转为"仅源码分发、停发预编译二进制"[14]，其长期开源姿态存疑，未来 Olares 若需可能要评估 SeaweedFS/Garage 等替代[18]。

## 3. 网络 / 接入

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| CNI | **Cilium**（CNCF Graduated 2023，eBPF）；**Calico**（主流 CNI，Tigera）[15][20] | VPC CNI | Azure CNI | VPC-native (Dataplane V2=Cilium) [5][20] | ✅ 内置 **Calico** + **CoreDNS**(DNS) |
| Ingress / 网关 | **Envoy**（CNCF Graduated；Envoy Gateway 为其子项目）；Nginx Ingress [6] | ELB / API Gateway | App Gateway / Azure LB | Cloud Load Balancing [5] | ✅ 内置 **Envoy Gateway** |
| Service Mesh | **Istio**、**Linkerd**（首个毕业 mesh，Rust）、**Cilium Mesh**——均 CNCF Graduated [6][21] | App Mesh | (Istio add-on) | Cloud Service Mesh (managed Istio) [5] | ⬜ 缺口（未内置 mesh）|
| 隧道 / VPN | **Headscale**（自托管 Tailscale）、**frp**、**WireGuard**、Cloudflare Tunnel（非 CNCF）| Site-to-Site VPN / (IAP) | Azure VPN | Cloud VPN / (IAP) [5] | ✅ 内置 **Headscale** + **FRP** |

**解读:** 网络大类 Olares 覆盖 CNI(Calico)、DNS(CoreDNS)、网关(Envoy Gateway)、远程接入(Headscale+FRP) 四个关键子类。Envoy Gateway 是 CNCF Envoy 的官方子项目，Gateway API 实现之一[6]。隧道/VPN 是 Olares 相对公有云的**差异化优势**：Headscale=免费自托管 Tailscale、FRP=内网穿透，公有云无 1:1 等价（最接近为托管站点 VPN 或零信任接入 IAP）。Service Mesh 是缺口。

**置信度:** High（CNI/网关/mesh 状态）/ Medium（隧道类公有云映射为近似）
**依据:** Cilium/Istio/Linkerd 的 Graduated 状态与 Envoy Gateway 定位由 Gateway API 官方清单确认[6][15]。
**反方解释:** 2026 sidecar mesh 已式微[21]，个人云是否需要 service mesh 存疑——Olares 不内置 Istio/Linkerd 可能是刻意取舍而非能力缺失。

## 4. 数据 / 中间件

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| 关系型 | **PostgreSQL**（开源事实主力）[5] | RDS / Aurora | Azure DB for PostgreSQL / Azure SQL | Cloud SQL / AlloyDB [5] | ✅ 内置 **PostgreSQL / Citus** |
| 文档型 | **MongoDB**（文档库主流）[5] | DocumentDB / DynamoDB | Cosmos DB | Firestore / Datastore [5] | ✅ 内置 **MongoDB** |
| KV / 缓存 | **Redis** / **Valkey**（Apache-2.0 分叉，drop-in）；KVRocks [22] | ElastiCache | Azure Cache | Memorystore [5] | ✅ 内置 **KVRocks**（Redis 兼容）|
| 流 / 消息 | **Kafka**（K8s 上经 **Strimzi**，CNCF Incubating）、**NATS**（CNCF Incubating）、RabbitMQ [12][1] | Kinesis / MSK / MQ | Event Hubs / Service Bus | Pub/Sub [5] | ✅ 内置 **NATS** |
| 向量库 | **Qdrant**（Rust，过滤/性价比首选）、**Milvus**（十亿级）、**Weaviate**（混合检索）；pgvector（复用 Postgres）[22][28] | (pgvector on RDS / OpenSearch) | Azure AI Search | Vertex AI Vector Search [22] | ✅ 平替 **pgvector on PostgreSQL/Citus** |

**解读:** 数据大类 Olares 五个子类均有内置件覆盖，走的是"复用成熟单体中间件"路线而非全部上 CNCF 项目——关系(PostgreSQL/Citus)、文档(MongoDB)、KV(KVRocks，Redis 兼容)、消息(NATS)。向量库无独立内置件，但可用 **pgvector on PostgreSQL/Citus** 覆盖多数个人/中等规模场景（<50–100M 向量），无需引入 Qdrant/Milvus[22]。

**置信度:** Medium-High
**依据:** 三云数据服务映射来自 GCP 官方[5]；Strimzi/NATS 的 CNCF Incubating 有官方确认[1][12]；向量库 top 与 Valkey 定位有 2026 对比背书[22]。
**反方解释:** 把向量库单列为基础设施子类有争议——部分观点认为 pgvector 即足够，且 MongoDB/PostgreSQL/Redis/Qdrant 多非 CNCF 托管项目，"top"依据是采用度而非 CNCF 状态[22]。

## 5. 身份 / 安全

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| SSO / IAM | **Keycloak**（唯一 CNCF Incubating IdP，企业级重型）；**ZITADEL**（Go 云原生）；**Authelia**（25MB forward-auth 网关）[23] | IAM / Identity Center | Microsoft Entra ID | Cloud IAM / Identity Platform [5] | ✅ 内置 **Authelia + LLDAP** |
| 密钥 / Secrets | **Infisical**（MIT）、**OpenBao**（Vault 的 MPL-2.0 分叉）、HashiCorp Vault（BSL）；ESO(CNCF)[24] | Secrets Manager / KMS | Key Vault | Secret Manager / Cloud KMS [5] | ✅ 内置 **Infisical**（+ 密码 **Vault**，见注）|
| 策略 | **OPA (Open Policy Agent)**、**Kyverno**——均 CNCF Graduated [1][24] | AWS Config / Organizations | Azure Policy | Org Policy Service [5] | ✅ 内置 **OPA** |
| 运行时安全 | **Falco**（CNCF Graduated，运行时威胁检测事实标准）；cert-manager、SPIFFE/SPIRE(Graduated)[1][24] | GuardDuty / Security Hub | Defender for Cloud | Security Command Center [5] | ⬜ 缺口（未确认内置 Falco）|

**解读:** Olares 身份/安全走"轻量 forward-auth + 策略"路线：Authelia(idle ~25MB)+LLDAP 做 SSO/目录，Infisical 做密钥，OPA 做准入策略[23][24]。相比公有云 IAM/Entra ID 的托管全家桶，Olares 覆盖了 SSO、密钥、策略三个子类；运行时安全(Falco)是缺口。

**置信度:** Medium-High
**依据:** Keycloak CNCF Incubating、OPA/Falco Graduated 有 CNCF 官方确认[1]；SSO/密钥选型有 2026 对比背书[23][24]；三云映射来自 GCP 官方[5]。
**反方解释:** Authelia 缺 SAML/多租户/完整 IdP 能力[23]，企业级 SSO 场景需 Keycloak/ZITADEL——Olares 内置 Authelia 对企业是"够用但非完备"。
**注（不确定）:** 用户组件清单同时列 Infisical(密钥管理)与"Vault(密码)"；此处"Vault"更可能指 Olares 面向用户的**密码管理器**而非 HashiCorp Vault，二者角色不同，引用前须以 Olares 官方组件文档复核 [unverified]。

## 6. 可观测

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| 指标 | **Prometheus**（CNCF Graduated 2018，指标金标准）+ **Grafana**（可视化）[7][25] | CloudWatch | Azure Monitor | Cloud Monitoring [5] | 🟡 部分：内置 **Grafana**（+ **Netdata**）|
| 日志 | **Loki**（Grafana LGTM 之 L）、**OpenObserve**（一体化）[25] | CloudWatch Logs | Azure Monitor Logs | Cloud Logging [5] | ⬜ 缺口（未确认 Loki 全链）|
| 追踪 | **Jaeger**（CNCF Graduated 2019）、**Tempo**；采集统一用 **OpenTelemetry**（CNCF Graduated 2026-05）[8][9] | AWS App Signals / X-Ray | Application Insights | Cloud Trace [5] | ⬜ 缺口（未内置 Jaeger/Tempo）|
| APM / 一体化 | **SigNoz**、**OpenObserve**（metrics+logs+traces 单平台）[25] | (X-Ray + CloudWatch) | Application Insights | Cloud Trace + Monitoring [5] | ⬜ 缺口 |

**解读:** 可观测是 Olares 覆盖最弱的大类。Olares 以 **Netdata + Grafana** 提供主机/资源级监控，能满足单机个人云的基本"看健康"需求，但**未确认内置完整 Prometheus 指标库、Loki 日志、Jaeger/Tempo 追踪、OpenTelemetry 采集**这条云原生可观测全链。三云则各有 CloudWatch/Azure Monitor/Cloud Operations 全家桶[5]。

**置信度:** Medium
**依据:** Prometheus/Jaeger/OpenTelemetry 的 Graduated 状态有 CNCF 官方页/公告直接确认[7][8][9]；Olares 侧仅确认 Netdata/Grafana，全链内置情况未反向核验（见 Gaps）。
**反方解释:** 个人云是否需要完整 LGTM/追踪链存疑[25]——Netdata 单点即可满足单机可观测，重型 APM 属"缺口但非必需"，把它算作硬缺口可能高估了需求。

## 7. CI-CD / 应用交付

| 子类 | 开源 top（为何 top） | AWS | Azure | GCP | Olares 内置/平替 |
|------|------|------|------|------|------|
| GitOps | **Argo CD**、**Flux**——均 CNCF Graduated [13][26] | CodePipeline / CodeDeploy | Azure DevOps / GitHub | Cloud Deploy / Config Sync [5] | ⬜ 缺口（未内置 GitOps）|
| 包管理 | **Helm**（CNCF Graduated）[26] | (CloudFormation) | (ARM/Bicep) | (Deployment Manager) [5] | 🟡 内部使用（应用以 chart 打包）|
| 镜像仓库 | **Harbor**（CNCF Graduated）[26] | ECR | ACR | Artifact Registry [5] | ⬜ 缺口（未内置 Harbor）|
| 自托管 PaaS | **Coolify**（~57.3k star）、**Dokploy**（~35k）、CapRover（~15.1k）——Heroku 式体验 [27] | App Runner / Elastic Beanstalk | App Service | Cloud Run / App Engine [5] | 🟡 **Olares Market 本身即应用交付层**（定位重叠，非内置这些工具）|

**解读:** CI-CD/应用交付是 Olares 与云原生工具**定位重叠**而非简单缺失的大类：Olares 本身通过 **Market + 一键安装**充当个人云的应用交付平台，与 Coolify/Dokploy 这类自托管 PaaS 是竞品/平替关系[27]；应用以 chart 形式打包（内部用 Helm 语义）。但面向"K8s 运维党"的 GitOps(ArgoCD/Flux) 与私有镜像仓库(Harbor) 未内置，是真缺口。

**置信度:** Medium-High
**依据:** ArgoCD/Flux/Helm/Harbor 的 Graduated 状态有 Flux 官方与行业清单确认[13][26]；PaaS star 数来自 2026 对比[27]；三云 CI/CD 映射来自 GCP 官方[5]。
**反方解释:** 自托管 PaaS 热度源于云成本回迁潮[27]，Olares 的 Market 一键装模式可能已覆盖大多数个人用户的"应用交付"需求，GitOps/Harbor 属"面向进阶运维用户的长尾"而非核心缺口。

## 核心争议

- **争议 1（Longhorn 成熟度）:** 行业文一度称 Longhorn 为"CNCF Graduated"[18]，但 CNCF 官方项目页明确为 **Incubating（2021-11-04 升级，至今未毕业）**[10]。本报告以官方为准记 Incubating。
- **争议 2（Milvus 成熟度）:** dibi8 正文称 Milvus 为"CNCF-graduated"，其自附引用却指向 Milvus 的 CNCF **Incubation** 页[28]，来源自相矛盾；本报告对 Milvus 的 CNCF 状态标注为**不确定**，不作毕业断言，引用前须以 cncf.io 复核 [unverified]。
- **争议 3（K3s 之于个人云是福是累）:** 一方认为复用 K8s 事实标准带来生态与可移植性[3][4]；另一方认为个人单机场景 Serverless(Cloud Run 式) 更省心，K3s 抬高了运维门槛[5]。

## 关键发现

- **发现 1（覆盖高的五大类）:** 计算/编排、存储、网络接入、数据/中间件、身份/安全的核心子类，Olares 基本都有内置组件或对应开源件——存储(MinIO/OpenEBS/JuiceFS/Restic)与数据(PostgreSQL/Citus、MongoDB、KVRocks、NATS)覆盖尤其完整。[5][10][14][18][22]
- **发现 2（差异化优势 = 隧道/接入）:** Headscale(自托管 Tailscale)+FRP(内网穿透) 是 Olares 相对公有云的**独特能力**，公有云无 1:1 等价，是"随时随地在线、数据归用户"叙事的有力技术支点。[5]
- **发现 3（主要缺口 = 可观测全链 + Serverless + GitOps/镜像仓库 + Mesh）:** 可观测的日志/追踪/APM 链（Olares 仅 Netdata/Grafana）、Serverless FaaS(Knative)、GitOps(ArgoCD/Flux)、私有镜像仓库(Harbor)、Service Mesh(Istio/Linkerd) 均未内置——但多数属"面向进阶 K8s 运维用户的长尾"，对个人云主用户群的刚性存疑。[7][9][13][21][26]
- **发现 4（Olares 的路线取舍）:** Olares 在编排/运行时/CNI/网关直接复用 CNCF 毕业事实标准（K3s/containerd/Calico/Envoy Gateway），在数据/身份则偏好轻量成熟单体（MongoDB/KVRocks/Authelia）而非重型 CNCF 项目（如 Keycloak）——是"够用、轻量、一键"的产品化取舍。[1][3][23]

## 局限性与未来方向

### 本研究局限
- **Olares 内置情况以用户提供清单 + 工作区 tech-stack 文档为准**，未逐一反向核验 Olares 官方最新组件文档；可观测全链、Falco、"Vault"（密码器 vs HashiCorp Vault）等处已标注不确定。
- **CNCF 成熟度/star 为快变数据**：本报告 AS_OF 2026-07-05，Longhorn/Strimzi/NATS/Milvus 等状态与 star 会随时间变化，引用前须以 cncf.io / landscape.cncf.io 复核。
- **公有云映射为"功能近似"而非严格等价**：隧道/VPN、向量库、Service Mesh 等在公有云无 1:1 对应，表中为最接近服务；GCP 官方对照表[5]最后更新为 2024-12，个别新服务名可能已变。
- **未展开 AI/GPU infra**（按要求另有专文），也未覆盖 CDN、WAF、消息通知、工作流编排等次要子类。

### 未来方向
- **高优先级:** 反向核验 Olares 官方组件文档，确认可观测链（是否内置 Prometheus/Loki/OTel）、备份(Restic/Velero)、密钥/密码(Infisical/Vault) 的准确内置状态，补齐第③列。
- **中优先级:** 为"Olares 已内置"的高价值子类（Headscale、JuiceFS、MinIO、Authelia、KVRocks）各做一篇"X on Olares / self-hosted X"长尾内容（对齐 tech/tech-stack.md 方向 6）。
- **中优先级:** 把本表升级为用户要求的完整"大类→子类｜top 开源｜三云叫法｜Olares 内置/平替"落地页底稿，并补 star/采用度实时数字（用 Semrush/GitHub API）。
- **低优先级:** 评估缺口子类（Knative/ArgoCD/Harbor/Falco）是否值得作为 Olares Market 上架应用或内置项。

## 参考文献
[1] CNCF. "Graduated and Incubating Projects". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/
[2] CNCF. "Cloud Native Computing Foundation Announces Knative's Graduation". Source-Type: official. As Of: 2025-10. https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/
[3] CNCF. "Kubernetes | CNCF". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/kubernetes/
[4] CNCF. "CNCF Interactive Landscape". Source-Type: official. As Of: 2026. https://landscape.cncf.io/
[5] Google Cloud. "Compare AWS and Azure services to Google Cloud". Source-Type: official. As Of: 2024-12. https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison
[6] Kubernetes SIG-Network. "Gateway API — Implementations". Source-Type: official. As Of: 2026. https://gateway-api.sigs.k8s.io/docs/implementations/list/
[7] CNCF. "Prometheus | CNCF". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/prometheus/
[8] CNCF. "Cloud Native Computing Foundation announces Jaeger graduation". Source-Type: official. As Of: 2019-10. https://www.cncf.io/announcements/2019/10/31/cloud-native-computing-foundation-announces-jaeger-graduation/
[9] CNCF. "CNCF Announces OpenTelemetry's Graduation". Source-Type: official. As Of: 2026-05. https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/
[10] CNCF. "Longhorn | CNCF". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/longhorn/
[11] CNCF. "Velero | CNCF". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/velero/
[12] CNCF. "Strimzi | CNCF". Source-Type: official. As Of: 2026. https://www.cncf.io/projects/strimzi/
[13] Flux. "Flux Documentation". Source-Type: official. As Of: 2026. https://fluxcd.io/flux/
[14] MinIO. "minio/minio (GitHub README)". Source-Type: official. As Of: 2026. https://github.com/minio/minio
[15] Cilium. "cilium/cilium (GitHub)". Source-Type: official. As Of: 2026. https://github.com/cilium/cilium/
[16] cloudjobs.io. "AWS vs Azure vs GCP Service Mapping: The Complete Comparison Chart (2026)". Source-Type: secondary-industry. As Of: 2026. https://cloudjobs.io/insights/articles/aws-vs-azure-vs-gcp-comparison-2026
[17] Civo. "The CNCF Landscape Explained". Source-Type: secondary-industry. As Of: 2026. https://www.civo.com/academy/kubernetes-introduction/cncf-and-its-landscapes
[18] Chaos and Order (youngju.dev). "Distributed Storage 2026 Deep Dive". Source-Type: secondary-industry. As Of: 2026-05. https://www.youngju.dev/blog/culture/2026-05-16-distributed-storage-minio-seaweedfs-ceph-garage-juicefs-openebs-longhorn-rook-2026-deep-dive.en
[19] K8sCalc. "Kubernetes Storage 2026: Longhorn vs Rook-Ceph vs OpenEBS Compared". Source-Type: secondary-industry. As Of: 2026. https://www.k8scalc.com/blog/kubernetes-storage-deep-dive
[20] Chaos and Order (youngju.dev). "Complete Guide to Kubernetes Network Policy and Service Mesh". Source-Type: secondary-industry. As Of: 2026-03. https://www.youngju.dev/blog/kubernetes/2026-03-14-kubernetes-network-policy-service-mesh-istio-cilium.en
[21] lucaberton. "Istio vs Cilium vs Linkerd 2026: Service Mesh Comparison". Source-Type: community. As Of: 2026. https://lucaberton.com/blog/service-mesh-istio-ambient-cilium/
[22] Firecrawl. "Best Vector Databases in 2026: A Complete Comparison Guide". Source-Type: secondary-industry. As Of: 2026. https://www.firecrawl.dev/blog/best-vector-databases
[23] authhost. "Authentik vs. Authelia vs. Keycloak 2026: SSO Comparison for Self-Hosters". Source-Type: secondary-industry. As Of: 2026. https://authhost.de/en/blog/authentik-vs-authelia-vs-keycloak
[24] Infisical. "Open Source Secrets Management for DevOps in 2026". Source-Type: secondary-industry. As Of: 2026. https://infisical.com/blog/open-source-secrets-management-devops
[25] OpenObserve. "Top 10 Open Source Observability Tools in 2026". Source-Type: secondary-industry. As Of: 2026. https://openobserve.ai/blog/top-10-open-source-observability-tools/
[26] Octopus Deploy. "8 Notable Argo CD Alternatives". Source-Type: secondary-industry. As Of: 2026. https://octopus.com/devops/argo-cd/argo-cd-alternatives/
[27] dev.to (Deploynix). "Self-Hosted PaaS Showdown 2026: Coolify vs Dokploy vs CapRover vs Deploynix". Source-Type: community. As Of: 2026-06. https://dev.to/deploynix/self-hosted-paas-showdown-2026-coolify-vs-dokploy-vs-caprover-vs-deploynix-46l3
[28] dibi8. "Milvus/Zilliz 2026: Deployment Guide". Source-Type: community. As Of: 2026. https://dibi8.com/resources/data-science/zilliz-milvus-vector-database-scale/
