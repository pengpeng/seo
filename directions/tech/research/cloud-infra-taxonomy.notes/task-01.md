---
task_id: 01
role: 编排/计算生态图谱分析师
status: complete
sources_found: 6
---

## Sources
[1] CNCF — Graduated and Incubating Projects | https://www.cncf.io/projects/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[2] CNCF — Knative graduation announcement | https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/ | Source-Type: official | As Of: 2025-10 | Authority: 10/10
[3] CNCF — Kubernetes project page | https://www.cncf.io/projects/kubernetes/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[4] Civo — The CNCF Landscape Explained | https://www.civo.com/academy/kubernetes-introduction/cncf-and-its-landscapes | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[5] Google Cloud — Compare AWS/Azure to Google Cloud | https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison | Source-Type: official | As Of: 2024-12 | Authority: 9/10
[6] cloudjobs.io — AWS vs Azure vs GCP Service Mapping 2026 | https://cloudjobs.io/insights/articles/aws-vs-azure-vs-gcp-comparison-2026 | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10

## Findings
- Kubernetes 于 2018-03-06 从 Incubating 升为 CNCF Graduated，是编排事实标准。[3]
- containerd 是 CNCF Graduated 容器运行时，也是 k3s 等多数发行版的默认运行时；Docker 自 K8s 1.24 起不再作为直接运行时。[1][4]
- k3s 是 CNCF Graduated、单二进制的轻量 K8s 发行版，运行完整 K8s API，二进制 <100MB。[4]
- Knative 于 2025-10-08 graduation，是 K8s 原生的 Serverless/事件驱动应用层；采用 Gateway API 简化网络栈。[2]
- 托管 K8s：AWS EKS / Azure AKS / Google GKE。[5][6]
- Serverless 容器：AWS Fargate(+App Runner) / Azure Container Apps(+ACI) / Google Cloud Run。[5][6]
- FaaS：AWS Lambda / Azure Functions / Google Cloud Run functions(前 Cloud Functions)。[5][6]

## Deep Read Notes
### Source [5]: GCP 官方三云服务对照表
Key data: GKE↔EKS↔AKS；Cloud Run↔App Runner/Fargate/Lambda↔Container Apps/ACI；Cloud Run functions↔Lambda↔Azure Functions；Artifact Registry↔ECR↔ACR。
Key insight: 唯一一手官方三云映射，覆盖 compute/serverless/存储/网络/数据/身份/可观测全线。
Useful for: 全部 7 大类的公有云列。

## Gaps
- 相反主张候选：有观点认为个人/单机场景不需要 K8s，Cloud Run/Container Apps 式 Serverless 更合适——即 Olares 选 K3s 增加了运维复杂度。
- OpenFaaS 未见 CNCF 收录（非 CNCF 项目），Knative 才是 CNCF 毕业的 Serverless。

## END
