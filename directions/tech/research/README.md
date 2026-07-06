# tech/research/ — 方向 6 分类底稿索引

方向 6「基础设施与中间件」的 deep-research 底稿都在这里。分类总表 [../tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md) 的逐项目认知/许可/CNCF/KubeBlocks 状态从这三份底稿归一而来。三份底稿**分工不重叠**、各自带 `.notes/`（子代理原始笔记 `task-*.md` + 去重来源登记 `registry.md`）。

## 三份底稿

| 底稿 | 范围 | 源数 | 分工边界 |
|------|------|------|------|
| [middleware-taxonomy.md](/Users/pengpeng/seo/directions/tech/research/middleware-taxonomy.md) | IaaS/PaaS 视角逐项目深挖**中间件**：计算/编排、存储、网络、数据库、消息流、平台中间件、企业大数据，含 KubeBlocks/Olares 状态与个人云适配取舍 | 76 | 平台/数据/消息层的"应用依赖的第三方服务" |
| [cloud-infra-taxonomy.md](/Users/pengpeng/seo/directions/tech/research/cloud-infra-taxonomy.md) | CNCF landscape × AWS/Azure/GCP 服务的 7 大类映射 | 见其 `.notes/registry.md` | 云原生分类框架与三云等价物 |
| [ai-infra.md](/Users/pengpeng/seo/directions/tech/research/ai-infra.md) | AI 基础设施栈逐项目（推理/网关/GPU 共享/Agent 沙盒/评估微调等） | 见其 `.notes/registry.md` | AI 专属基础设施 |

> `.notes/` 是过程产物（子代理笔记 + 来源登记），正文以三份 `*.md` 为准；底稿正文不因每轮微调重写。

## 二轮核实来源（AS_OF 2026-07-05）

本轮对 tech-stack.md 精修新增/修正的关键事实，出处登记如下，供溯源：

- **KubeBlocks 收录引擎**（校正 KB 标记）：[官方 supported-addons](https://kubeblocks.io/docs/preview/user_docs/overview/supported-addons)——据此补 mariadb/nebula/tdengine/minio 等、去 Doris/Citus/Vitess/CouchDB/KVRocks/NATS 等未收录项。
- **Zot** 镜像仓库（CNCF Sandbox，Olares 选用）：[project-zot.github.io](https://zot.dev/) / CNCF landscape。
- **SoftHSM2 / PKCS#11**：OpenDNSSEC SoftHSM 项目；HSM auto-unseal 见 HashiCorp Vault / OpenBao PKCS#11 seal 文档。
- **授权 ReBAC**：SpiceDB(AuthZed)、OpenFGA(CNCF Sandbox, Auth0/Okta)、Permify、Ory Keto 官方仓库/文档；Olares 走 OPA 策略、非 ReBAC 路线。
- **Agent 沙盒**：E2B(Firecracker)、microsandbox(libkrun)、Daytona、AerolVM 官方仓库；隔离底座 gVisor/Firecracker/Kata/libkrun。
- **Agent 记忆**：Mem0、Zep/Graphiti、Letta(MemGPT)、Cognee、Memobase 官方仓库（均 Apache-2.0）；底层多为向量库+知识图谱，见 2026 多篇横评（Mem0 vs Zep vs Letta vs Cognee）。
- **ZeroTier 许可**：核心 MPL-2.0、控制器 1.16 起 source-available（官方仓库 LICENSE）。

## 怎么用

- 重跑/新增底稿：走 `.cursor/skills/deep-research/` 流程，产出落本目录，`.notes/registry.md` 记来源、避免与已有底稿重复登记。
- 事实型数字（版本/许可/CNCF 级别/KB 收录）为快变数据，引用前以官网/CNCF/KubeBlocks 文档复核。
