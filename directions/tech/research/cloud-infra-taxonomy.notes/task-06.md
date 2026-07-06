---
task_id: 06
role: 可观测 + CI/CD 应用交付分析师
status: complete
sources_found: 6
---

## Sources
[7] CNCF — Prometheus project page | https://www.cncf.io/projects/prometheus/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[8] CNCF — Jaeger graduation announcement | https://www.cncf.io/announcements/2019/10/31/cloud-native-computing-foundation-announces-jaeger-graduation/ | Source-Type: official | As Of: 2019-10 | Authority: 9/10
[9] CNCF — OpenTelemetry graduation announcement | https://www.cncf.io/announcements/2026/05/21/cloud-native-computing-foundation-announces-opentelemetrys-graduation-solidifying-status-as-the-de-facto-observability-standard/ | Source-Type: official | As Of: 2026-05 | Authority: 10/10
[25] OpenObserve — Top 10 Open Source Observability Tools 2026 | https://openobserve.ai/blog/top-10-open-source-observability-tools/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[13] Flux — Official documentation | https://fluxcd.io/flux/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[26] Octopus Deploy — 8 Notable Argo CD Alternatives | https://octopus.com/devops/argo-cd/argo-cd-alternatives/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[27] dev.to (Deploynix) — Self-Hosted PaaS Showdown 2026 | https://dev.to/deploynix/self-hosted-paas-showdown-2026-coolify-vs-dokploy-vs-caprover-vs-deploynix-46l3 | Source-Type: community | As Of: 2026-06 | Authority: 5/10
[5] Google Cloud — 三云服务对照表 | https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison | Source-Type: official | As Of: 2024-12 | Authority: 9/10

## Findings
- 指标：Prometheus 2018-08-09 CNCF Graduated，云原生指标金标准；常配 Grafana 可视化。[7][25]
- 日志：Grafana Loki（LGTM 栈之 L）与 OpenObserve（单应用一体化 logs/metrics/traces）是主流；OpenObserve 支持 SQL/PromQL。[25]
- 追踪：Jaeger 2019-10 CNCF Graduated（Uber 起源）；Grafana Tempo 为 LGTM 栈追踪组件。[8][25]
- OpenTelemetry 2026-05-21 graduation，成为指标/日志/追踪统一采集的事实标准框架。[9]
- APM/一体化：SigNoz 与 OpenObserve 提供 metrics+logs+traces 单平台（底层 ClickHouse/对象存储）。[25]
- GitOps：Argo CD 与 Flux 均 CNCF Graduated；Flux 由 Source/Kustomize/Helm/Notification/Image 多控制器组成，支持 Helm、OCI、Harbor webhook。[13][26]
- 包管理 Helm、镜像仓库 Harbor 均 CNCF Graduated；自托管 PaaS（非 K8s 路线）Coolify(~57.3k star)/Dokploy(~35k)/CapRover(~15.1k) 提供 Heroku 式体验。[26][27]
- 公有云对应：CI/CD AWS CodePipeline·CodeBuild↔Azure DevOps·GitHub↔Cloud Build·Cloud Deploy；镜像仓库 ECR↔ACR↔Artifact Registry；监控 CloudWatch↔Azure Monitor↔Cloud Monitoring；日志 CloudWatch Logs↔Azure Monitor Logs↔Cloud Logging；追踪 AWS App Signals↔App Insights↔Cloud Trace。[5]

## Deep Read Notes
### Source [9]: OpenTelemetry graduation（CNCF 官方）
Key data: 2026-05-21 Observability Summit 宣布毕业；统一 metrics/logs/traces 采集；与 K8s/Fluentd/Jaeger/Prometheus 深度整合。
Key insight: OTel 已从"零散信号"转向"统一遥测编织"，是新一代可观测底座。
Useful for: 可观测大类"采集框架"补充行。

## Gaps
- Olares 监控用 Netdata/Grafana；是否内置完整 Prometheus/Loki/Jaeger 链未从官方文档反向核验，报告中按"部分内置/以 Grafana+Netdata 呈现"标注。
- 相反主张：个人云是否需要完整 LGTM/追踪链存疑；Netdata 单点即可满足单机可观测，重型 APM 属"缺口但非必需"。
- Coolify/Dokploy 与 Olares 的关系是"竞品/平替"而非内置——Olares 自身就是应用交付平台（Market + 一键装），定位重叠。

## END
