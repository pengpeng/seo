# tech/tech-stack.md — 方向 6「技术栈 / 自建单一技术」词库

> [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 6 的词库：搜单一底层技术（tailscale/headscale/frp、K3s、JuiceFS、Authelia 等）的人，往往嫌自己搭一套麻烦——Olares 把它们内置/一键化，是"更省事的选择"。
>
> **这些是长尾 SEO 机会，不是主推卖点**：可做单独技术文、"X on Olares"、"Olares uses X"、技术对比等长尾内容，但**不进品牌叙事、首屏与 campaign 文案**（主推口径见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md) 品牌口径）。已成篇的报告见 [reports/](/Users/pengpeng/seo/directions/tech/reports)。
>
> 用法：写这类内容时，先按 `.cursor/skills/brand-seo-research/` 流程用 Semrush 验证词的量/KD，再落"Olares 角度"。

## 编排 / 基础

| 术语 | Olares 角度 |
|------|-------------|
| K3s、Kubernetes | Olares 用 K3s 做底座——"个人云上的 Kubernetes"，面向想动手学云原生的用户 |
| containerd | 容器运行时，技术对比/排障长尾 |
| Calico、CoreDNS | 集群网络与 DNS，纯技术长尾 |
| Envoy Gateway | 应用入口网关，配合 entrance 权限的技术文 |

## 存储

| 术语 | Olares 角度 |
|------|-------------|
| JuiceFS | 统一分布式文件系统——跨节点存储、云原生存储对比 |
| MinIO | S3 兼容对象存储，self-hosted S3 长尾 |
| OpenEBS | 本地块存储 |
| Restic | 增量加密备份——"自动备份"技术文 |
| Seafile | 文件同步盘，Nextcloud/Dropbox 同步对比 |

## 网络 / 接入

| 术语 | Olares 角度 |
|------|-------------|
| Tailscale、Headscale | Olares 内置 Headscale = 免费自托管 Tailscale，是高价值对比切入点（报告：[headscale](/Users/pengpeng/seo/directions/tech/reports/headscale.md)；商业方 Tailscale 见 [commerce/reports/tailscale.md](/Users/pengpeng/seo/directions/commerce/reports/05-storage-privacy/privacy-vpn/tailscale.md)） |
| Cloudflare Tunnel | 内网穿透方案对比 |
| FRP | 内网穿透，中文用户长尾（报告：[frp](/Users/pengpeng/seo/directions/tech/reports/frp.md)） |

## 身份 / 安全

| 术语 | Olares 角度 |
|------|-------------|
| Authelia | 自托管 SSO/MFA——"self-hosted SSO"长尾 |
| LLDAP | 轻量 LDAP，配合 Authelia 的身份技术文 |
| Infisical | 密钥管理，self-hosted secrets manager |
| OPA (Open Policy Agent) | 准入策略/沙箱安全技术文 |
| SSO / MFA | 单点登录、多因子认证泛词 |

## 数据 / 中间件

| 术语 | Olares 角度 |
|------|-------------|
| PostgreSQL、Citus | 内置数据库/向量检索，self-hosted DB |
| KVRocks（Redis 兼容） | 持久化 KV，Redis 替代长尾 |
| MongoDB | 文档库，中间件共享技术文 |
| NATS | 消息队列 |

## GPU / AI

| 术语 | Olares 角度 |
|------|-------------|
| CUDA | x86 + NVIDIA CUDA 兼容标准 AI 应用（vs ARM AI PC） |
| HAMi、GPUBinding、nvshare | GPU 共享/切片调度技术文——多节点异构 GPU、显存切片 |
| llm-init | 一键拉起/适配任意模型与推理引擎的技术文 |
| Ollama、vLLM、llama.cpp、SGLang | 推理引擎对比 + "X on Olares" 教程（高价值，量大） |

---

*词量/KD 需用 Semrush 现查；本表只列方向，不含实时数据。*
