---
task_id: 06
role: 平台中间件（可观测/Serverless/工作流/密钥）分析师
status: complete
sources_found: 18
---

## Sources
[1] CNCF Announces OpenTelemetry's Graduation | CNCF | https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/ | Source-Type: official | As Of: 2026-05 | Authority: 10/10
[2] Grafana Labs joins CNCF Governing Board | Grafana Labs | https://grafana.com/blog/grafana-labs-joins-the-cncf-governing-board-as-a-platinum-member-of-the-open-source-foundation/ | Source-Type: official | As Of: 2026-06 | Authority: 8/10
[3] Distributed Tracing: Jaeger vs Tempo vs Zipkin | Ajit Singh | https://singhajit.com/distributed-tracing-jaeger-vs-tempo-vs-zipkin/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[4] End-to-End Observability with Prometheus/Grafana/Loki/OTel/Tempo | DEV Community | https://dev.to/improving/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-and-tempo-3fpf | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[5] Knative vs OpenFaaS vs Fission: Serverless on Kubernetes 2026 | DevOpsBoys | https://devopsboys.com/blog/knative-vs-openfaas-vs-fission-serverless-kubernetes-2026 | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[6] Knative | CNCF | https://www.cncf.io/projects/knative/ | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[7] Overview of self-hosted serverless frameworks for Kubernetes | Palark | https://palark.com/blog/open-source-self-hosted-serverless-frameworks-for-kubernetes/ | Source-Type: secondary-industry | As Of: 2025-12 | Authority: 6/10
[8] Temporal vs Airflow vs Argo: Workflow Orchestration Guide | xgrid | https://www.xgrid.co/resources/temporal-vs-airflow-vs-argo-workflow-orchestration/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[9] Airflow vs Temporal: Scheduling vs Durable Execution (2026) | Modern DataTools | https://www.modern-datatools.com/compare/airflow-vs-temporal | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[10] State of Workflow Orchestration Systems 2025 | pracdata | https://www.pracdata.io/p/state-of-workflow-orchestration-ecosystem-2025 | Source-Type: secondary-industry | As Of: 2025-12 | Authority: 7/10
[11] Kubernetes Secrets Management in 2026: Vault vs ESO vs Infisical | rkssh | https://rkssh.com/blog/kubernetes-secrets-management-vault-eso-infisical | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[12] HashiCorp Vault Alternatives: 8 Secrets Managers Compared (2026) | wetheflywheel | https://wetheflywheel.com/en/comparisons/hashicorp-vault-alternatives/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[13] HashiCorp Vault vs OpenBao: thorough comparison | Jorijn Schrijvershof | https://jorijn.com/en/blog/hashicorp-vault-vs-openbao/ | Source-Type: community | As Of: 2026-04 | Authority: 7/10
[14] Top 16 Secrets Management Tools and Platforms for 2026 | GitGuardian | https://blog.gitguardian.com/top-secrets-management-tools/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 7/10
[15] CNCF Announces Argo has Graduated | CNCF | https://www.cncf.io/announcements/2022/12/06/the-cloud-native-computing-foundation-announces-argo-has-graduated/ | Source-Type: official | As Of: 2022-12 | Authority: 10/10
[16] Argo | CNCF | https://www.cncf.io/projects/argo/ | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[17] argoproj/argo-workflows (GitHub) | https://github.com/argoproj/argo-workflows/ | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[18] argoproj/argo-events (GitHub) | https://github.com/argoproj/argo-events | Source-Type: official | As Of: 2026-07 | Authority: 9/10

## Findings
- 【可观测】OpenTelemetry（OTel，Apache-2.0）2026-05-21 CNCF 毕业，是厂商中立的 metrics/logs/traces 采集与导出标准，已成"事实标准"，与 K8s/Jaeger/Prometheus 深度集成；公有云替代＝各家 SDK/agent 但 OTel 正取代之。[1]
- 【可观测】Prometheus（Apache-2.0）是 CNCF 毕业项目（与 Kubernetes/Envoy 同级），负责时序指标采集+PromQL 查询+告警；公有云替代＝AWS CloudWatch / Azure Monitor / Google Cloud Monitoring。[1][3]
- 【可观测】Jaeger（Apache-2.0，Uber 2015 开源、2017 捐 CNCF、2019 毕业）是分布式追踪标杆，存储后端支持 Badger(本地)/Cassandra/ES/Kafka；公有云替代＝AWS X-Ray / Google Cloud Trace。[3]
- 【可观测】Grafana 与 Grafana Loki 均由 Grafana Labs 维护、非 CNCF 项目（Grafana Labs 为 CNCF 白金董事）；Grafana＝可视化面板，Loki＝日志聚合（与 Prometheus/Grafana 无缝集成，为 ELK 的轻量开源替代）；公有云替代＝CloudWatch Logs / Managed Grafana。[2][3][4]
- 【可观测·可提】Grafana Tempo（Go，2020，非 CNCF）是低成本高吞吐 tracing，支持 TraceQL 与 Loki/Prometheus 原生关联，是"单 UI 打通 metrics→traces→logs"的关键；VictoriaMetrics 为 Prometheus 兼容的高压缩长存储替代。[3][4]
- 【Serverless】Knative（Apache-2.0）2022-03 入 CNCF Incubating、2025-09-11 毕业；含 Serving（请求驱动自动扩缩含 scale-to-zero）、Eventing（CloudEvents 异步路由）、Functions 三组件，Google Cloud Run 底层即基于它；缺点是重（常需 Istio/Kourier 入口）。[5][6]
- 【Serverless】OpenFaaS（社区版 MIT）主打开发者体验：简洁 CLI、20+ 语言模板、友好网关；但 scale-to-zero、SSO、精细自动扩缩多为 OpenFaaS Pro 商业版功能，OSS 版默认只缩到 1 副本；非 CNCF。[5][7]
- 【Serverless·可提】Fission（Apache-2.0，源自 Platform9，现 CNCF Sandbox）以暖池架构实现 <100ms 冷启动、社区较小；三者公有云替代＝AWS Lambda / Google Cloud Functions·Cloud Run / Azure Functions。[5]
- 【工作流】Argo（含 Argo Workflows/Events/CD/Rollouts）2020-03 入 CNCF Incubating、2022-12-06 毕业；Argo Workflows（Apache-2.0，~16.8k star[2026-07]）是 K8s 原生、以容器为 step 的 DAG/step 引擎，适合 CI/CD、ML 训练、并行批处理；公有云替代＝AWS Step Functions / Google Cloud Workflows。[15][16][17]
- 【工作流·可提】Argo Events（Apache-2.0，~2.7k star，最新 v1.9.10[2026-01]）是事件驱动依赖管理，可由 20+ 事件源（webhook/S3/cron/Kafka/PubSub/SQS）触发 Workflows 等 10 类动作。[18]
- 【工作流·可提】Temporal（MIT，~19.7k star）主打"持久化执行"——用普通代码（Go/Java/TS/Python/.NET）写可跨崩溃/重试/长等待存活的有状态业务流；Apache Airflow（Apache-2.0，~45k star）是数据工程批处理 ETL/ELT 调度霸主（Python DAG + 海量 operator，Cloud Composer/MWAA 均标准化于它）。三者取向不同：Airflow=定时数据管道、Argo=K8s 原生容器作业、Temporal=关键业务持久流。[8][9][10]
- 【密钥】HashiCorp Vault 2023 起改用 BUSL/BSL 许可（含竞争条款）、2025 被 IBM 以 $64 亿收购成 IBM 产品；杀手锏＝动态密钥（按需生成短 TTL 临时凭据）+ 审计日志 + 细粒度策略，缺点是重、成关键路径 HA 服务；公有云替代＝AWS Secrets Manager / Azure Key Vault / GCP Secret Manager。[11][14]
- 【密钥】OpenBao（MPL-2.0，OpenSSF/Linux Foundation 治理）是 Vault 的 API 兼容开源分叉，为"因 BUSL 许可离开 Vault"提供最低迁移摩擦，已补齐开源命名空间/PKCS#11 HSM auto-unseal/Transform 引擎等企业空白；官方 K8s 同步方案已统一到 ESO（自研 operator 于 2026-02 归档）。[12][13]
- 【密钥】Infisical（核心 MIT，开放核心模式）主打开发者体验（UI/CLI/按人环境/版本/访问申请），适合小团队；External Secrets Operator（Apache-2.0）不是存储后端而是同步器，把 Vault/OpenBao/AWS/GCP/Azure 等外部库同步进 K8s 原生 Secret，是 K8s 重度环境的事实标准（配合 etcd 静态加密）。[11][13][14]

## Deep Read Notes
### Source [11]: Kubernetes Secrets Management 2026 (rkssh, WebFetch 全文)
Key data: K8s Secret 仅 base64、存 etcd、有集群权限即可读。决策矩阵——<10 人无合规：Infisical(hosted)+ESO；10–50 人 SOC2/HIPAA：ESO+AWS Secrets Manager；50+ ISO27001/SOC2 II：Vault HA；气隙/受监管：Vault on-prem。
Key insight: 主流模式＝"外部密钥库为唯一真源 + operator 同步进 K8s Secret + 应用无改动读 Secret"；最低底线是开 etcd 静态加密。ESO 优点是不新增关键基础设施，缺点是密钥最终仍落 etcd。
Useful for: 支撑"密钥/配置管理"整节 + 个人云"是否需要完整 Vault"的规模分档。

### Source [13]: Vault vs OpenBao (Jorijn, WebFetch 全文)
Key data: Vault=BUSL 1.1（IBM 所有，含竞争条款）；OpenBao=MPL 2.0（OpenSSF）。OpenBao 官方 K8s 路径＝ESO 的 OpenBao provider；其 openbao-secrets-operator 于 2026-02-20 归档，未发版，TSC 决定统一到 ESO 社区共建。
Key insight: 对内部自用二者差别小；对"做产品/含密钥管理功能的厂商/开源优先组织"，MPL 2.0 才是安全地基（BUSL 附加授权有实际法律风险）。OpenBao 已补齐 Vault Enterprise 最痛的几处空白。
Useful for: 支撑 Olares 内置 Vault/Infisical 的许可与选型论证（Olares 面向个人+开源，倾向 MPL/MIT）。

### Source [6]: Knative | CNCF
Key data: 2022-03-02 入 CNCF Incubating，2025-09-11 升 Graduated；三组件 Serving/Eventing/Functions；Google Cloud Run 底层。
Key insight: Knative 是"开发者向 serverless 应用层"，是 K8s 应用构造的补充而非完整 FaaS；毕业标志其成为 K8s serverless 事实层。
Useful for: 支撑 Serverless/FaaS 大类的成熟度锚点。

## Gaps
- 相反主张候选：个人云/单机场景是否真需要完整 LGTM（Loki/Grafana/Tempo/Mimir）可观测全链与 Serverless 框架——多数 self-hosted/homelab 讨论认为 Knative（需 Istio）、完整分布式追踪、多副本 Vault HA 对单用户属重度过度工程，个人云更可能只用 Prometheus+单一面板/日志与 K8s 原生 Secret+etcd 加密；但未搜到针对"个人云可观测/密钥最小充分栈"的第三方实测基准，仅有企业向对比与官方口径。
- 未拿到：Prometheus/Jaeger/Knative 各自精确 star[2026-07] 与 Loki/Grafana 具体许可版本号（业界普遍记 Grafana/Loki 为 AGPLv3，但本轮搜索未直接命中官方 LICENSE 页确认）。

## END
