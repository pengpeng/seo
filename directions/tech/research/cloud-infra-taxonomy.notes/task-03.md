---
task_id: 03
role: 云原生网络/接入分析师
status: complete
sources_found: 5
---

## Sources
[15] Cilium — GitHub 仓库 | https://github.com/cilium/cilium/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[6] Kubernetes SIG — Gateway API Implementations | https://gateway-api.sigs.k8s.io/docs/implementations/list/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[20] Chaos and Order — K8s Network Policy & Service Mesh | https://www.youngju.dev/blog/kubernetes/2026-03-14-kubernetes-network-policy-service-mesh-istio-cilium.en | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 6/10
[21] lucaberton — Istio vs Cilium vs Linkerd 2026 | https://lucaberton.com/blog/service-mesh-istio-ambient-cilium/ | Source-Type: community | As Of: 2026 | Authority: 5/10
[5] Google Cloud — 三云服务对照表 | https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison | Source-Type: official | As Of: 2024-12 | Authority: 9/10

## Findings
- Cilium 是 eBPF CNI，2023-10 从 CNCF 毕业；可整合 Service Mesh（sidecarless），并作为 Gateway API 合规数据面（Cilium 1.19 过 v1.4.0 conformance）。[15][6][21]
- Istio、Linkerd、Cilium 均为 CNCF Graduated 的 service mesh/网络项目。[20][21][6]
- Linkerd 是首个 CNCF 毕业 service mesh，唯一不基于 Envoy（用 Rust 微代理），主打轻量与自动 mTLS。[6][21]
- Envoy Gateway 是 Envoy 子项目，用于管理 Envoy 网关，是 Gateway API 实现之一；Calico 的 Gateway API 实现也构建在 Envoy Gateway 上。[6]
- Calico 是主流 CNI/网络与安全方案（Tigera 主导），支持 L3/L4 NetworkPolicy 与 Gateway API。[20][6]
- 网络接入公有云对应：VPC↔VNet↔VPC；负载均衡 ELB↔Azure LB↔Cloud Load Balancing；DNS Route 53↔Azure DNS↔Cloud DNS；VPN 站点 AWS VPN↔Azure VPN↔Cloud VPN；GCP 有 managed Cloud Service Mesh（≈AWS App Mesh）。[5]

## Deep Read Notes
### Source [6]: Gateway API 官方实现清单
Key data: Cilium(CNCF Graduated，Gateway API v1.4.0 conformance)、Envoy Gateway、Istio、Linkerd(首个毕业 mesh)、Calico(基于 Envoy Gateway) 均在册。
Key insight: Envoy Gateway 是 Olares Envoy Gateway 内置组件的上游，权威确认其 Gateway API 定位。
Useful for: 网络/接入大类 Ingress/网关与 mesh 行。

## Gaps
- 隧道/VPN 类（Headscale/frp/Cloudflare Tunnel/WireGuard）非 CNCF landscape 核心项，公有云无 1:1 等价（最接近为托管站点到站点 VPN 或零信任接入如 IAP/Verified Access）——已在 tech/reports 有 headscale、frp 专文。
- 相反主张：2026 sidecar mesh 式微，个人云是否真需要 service mesh 存疑；Olares 未内置 Istio/Linkerd，可能是刻意取舍而非缺口。

## END
