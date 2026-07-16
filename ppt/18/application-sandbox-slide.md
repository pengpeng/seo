# Olares 应用沙盒

> Intel 合作 PPT 第 18 页。中文 Slide 文案、版式规格与逐字稿。

---

## Slide copy

### 标题

主标题：**Sandboxes Every User, Application and Agent**（`Sandboxes` 绿色高亮）

副标题：One multi-user device — users, applications and Agents run side by side, isolated by default and granted only what they declare.

### 左上 · 01 · Identity & authorization

**Who can act—and on whose behalf**

副标题：Unified authentication, workload authorization and secrets custody across users, applications and Agents.

| Capability | Product feature |
|---|---|
| **Unified identity** | **One sign-in across the system.** Authelia 为用户和应用提供一致的认证入口，避免每个服务各自建立登录边界。<br><br>**Roles stay consistent everywhere.** LLDAP 维护统一用户与群组目录，让 Admin、Member 等角色跨应用保持一致。 |
| **ReBAC & Agent delegation** | **Every workload receives only what it needs.** Olares 使用 Kubernetes 原生 Roles 与 ServiceAccounts 将权限绑定到应用，而不是暴露整台设备的权限。<br><br>**People and groups keep their own boundaries.** ReBAC 让 Search、Files 和 IM 按用户、群组与资源关系授权，Agent 也只能在组合后的范围内行动。 |
| **Secrets & key custody** | **Sensitive credentials stay out of applications.** Infisical 当前管理 LLM API keys 与 Agent cookies，后续由 OpenBao 承接统一 secret management。<br><br>**Key custody can move into hardware.** 底层 HSM 接口允许用户在需要更强保护时接入第三方 HSM。 |

### 右上 · 02 · Runtime & resource isolation

**How each application runs**

副标题：Isolated runtimes, reduced privileges and explicit resource envelopes.

| Capability | Product feature |
|---|---|
| **Runtime boundary** | **Each application gets its own runtime.** 应用不与宿主机环境直接共享执行边界。<br><br>**Users remain separated.** 按用户划分的 namespace 将 workload 与 service identity 留在其所有者空间内。 |
| **Reduced privilege** | **Privilege starts low.** 应用默认运行在非特权容器中，而不是获得宿主机级访问。<br><br>**Policy is checked before execution.** OPA admission 在应用安装或运行前校验其声明的权限。 |
| **Resource envelope** | **Capacity is declared up front.** CPU、memory 与 accelerator requests 告诉调度器应用需要什么。<br><br>**The system protects itself under pressure.** 当资源紧张时，Olares 会智能驱逐 workload，维持整体稳定并保障关键服务运行。 |

### 左下 · 03 · Network boundary & access

**How each application connects**

副标题：Four access paths, protected by declared entrances and layered security.

| Network path | Product feature |
|---|---|
| **Internet** | **Domains and HTTPS come ready.** 每个 Web 入口获得免费 Olares 域名与托管证书，也支持自定义域名和用户选择的反向代理。 |
| **VPN · LarePass** | **Private access without a third-party control plane.** LarePass 使用 Tailscale 客户端与 Olares 本地托管的 Headscale，优先 LAN 或 P2P 直连，必要时回退 relay。 |
| **Local network** | **Local compatibility stays intact.** `.local` HTTP 提供 Web 访问；按应用启用的 Overlay Gateway 承载设备发现、投屏和媒体设备等局域网原生协议。 |
| **In-cluster** | **Identity-aware service mesh.** 自动 mTLS 与 ServiceAccount 身份保护每个 workload；细粒度策略、指标和审计信号让东西向流量可观测、可治理。 |

在遵循 cloud-native networking best practices、提供 enterprise-grade security 的同时，保留家庭网络、传统协议和不同远程接入方式所需的兼容性与灵活性。

### 右下 · 04 · Data & filesystem boundary

**What data each application can see**

副标题：Olares Files applies declared scopes across persistent, connected and Agent-ready storage.

| Capability | Product feature |
|---|---|
| **Sandboxed spaces** | **Every path has an owner.** Home、Data、Cache 和 Common 定义所有权、持久性与共享方式；应用只挂载声明获准的路径。 |
| **Cross-node data plane** | **Persistent data follows the cluster.** Home、Data 和 Common 跨节点保持可用；Cache 留在本地并可安全重建。 |
| **Connected storage** | **Existing data stays where it is.** Sync、云盘、USB、SMB、NFS 和现有 NAS 接入同一文件世界；Managed RAID 为 Next。 |
| **PC-grade Files & sharing** | **Users keep familiar file operations.** Files 支持浏览、预览、编辑、移动和压缩，并直接通过用户、公开链接或 SMB 分享原始数据。 |
| **Search** | **Discovery comes before action.** Search 按文件名、全文或图片发现候选，Files 再校验权限并执行操作。 |
| **Unified access URLs** | **Agents use one address model.** 无论后端是本地、分布式、云端还是外部存储，Files 都通过统一 URL 模型暴露数据，Agent 无需分别适配各后端 API。 |

---

## 逐字稿

先说为什么需要沙盒。Olares 是一个多用户系统：多个用户、他们安装的应用、以及代表他们工作的 Agent 共享同一台设备。所以沙盒隔离的其实是三个对象——User、Application、Agent。用户拥有身份与角色，RBAC 决定他能触达什么；应用在自己被授予的网络、存储和资源信封内运行；Agent 代表某个用户、在某个应用内行动，权限是二者的交集。默认全部隔离，需要的能力再按 Manifest 显式授予。

沙盒不只是容器，而是四个连续问题：**谁能行动、应用如何运行、应用如何连接、应用能看到什么数据。**

第一块是 Identity & authorization。Authelia 提供统一认证入口，LLDAP 集中管理用户、群组和角色。授权分成两层：Kubernetes Role / ServiceAccount 管 workload 权限，ReBAC 管 Search、Files、IM 中用户、群组与资源的关系；Agent delegation 不是额外获得万能权限，而是只能在两层授权组合后的范围内行动。Infisical 当前管理 LLM API keys 与 Agent cookies，后续由 OpenBao 承接，并通过底层 HSM 接口支持第三方硬件密钥托管。

第二块是 Runtime & resource isolation。每个应用运行在独立 runtime 和按用户划分的 namespace 中，并默认使用非特权容器；OPA admission 在安装或运行前校验应用声明的权限。CPU、内存与加速设备 requests 描述资源需求，而在系统发生压力时，Olares 会智能驱逐 workload，以维持整体稳定并保障关键服务。

第三块是网络边界。它的产品定位是 **Cloud-native security, built for real-world networks**：遵循云原生安全实践，但不牺牲家庭网络、传统协议和远程接入的兼容性。Internet、VPN · LarePass、Local network 和 In-cluster 是四条独立路径。Internet 的 Reverse proxy 不只是穿透：每个标准应用入口都可以获得免费 Olares 域名、HTTPS 和托管证书，同时支持自定义域名及用户选择的反向代理。LarePass 使用 Tailscale 客户端与设备本地托管的 Headscale 控制面，在直连与 relay 间自动选路；`.local` HTTP 与 Overlay Gateway 分别承载本地 Web 访问和局域网原生协议；Linkerd service mesh 则通过自动 mTLS、ServiceAccount workload identity、细粒度授权、流量指标和审计信号治理集群内的东西向流量。

第四块是数据与文件边界。它的产品体验是 **Governed like cloud infrastructure. Familiar like a PC. Ready for Agents.** Olares Files 把沙盒空间、跨节点数据面、Sync / Cloud / External、PC 级操作、分享、搜索和 Unified access URLs 收敛成六项能力。应用只能看到声明获准的数据；无论后端是本地盘、分布式存储、云盘、SMB 还是 NFS，Agent 都通过统一 URL 地址模型访问，无需适配各存储 API。

贯穿四块的是同一条策略主线：Manifest declares → OPA validates → Platform enforces。

---

## 版式规格

- 画布为 `1280×720`，`header 64px / 主体 1fr`，不设独立叙事带；多用户 why 与三对象由主/副标题承载。
- 主体采用 `2×2` 四分区：左上 01 Identity、右上 02 Runtime & resource、左下 03 Network、右下 04 Files。
- 左右严格等分 `50 / 50`；上排内容较少，高度约占 `42%`，下排 Network 与 Files 信息更多，约占 `58%`。
- 每个分区使用 Editorial Matrix，而不是横向长条列表：Identity `2×2`、Runtime 横向三列、Network `2×2`、Files `2×3`。
- 能力块之间主要依靠留白、对齐与少量细线分组，不使用卡片、背景色或每行贯穿整栏的分隔线。
- Files 从 9 点压缩成 6 点；Sync / Cloud / External 合并为 Connected storage，Sharing 与 PC-grade Files 合并。
- 不设置页脚；Declarative policy 只保留在逐字稿与内部笔记中，不再占用主画面。
- 全页只讲功能特点，统一中性配色，不使用深绿色块或任何独立配色容器。
- 主要依赖字重、编号、细分隔线与对齐建立层级，不堆圆角卡片。
- HTML 与最终导出全部使用英文，中文 MD 仅作为事实源。

## 事实边界

- 本页是 Intel 商业合作 Pitch，表达完整产品方向和未来 2–3 个月目标架构。
- 免费独立域名与托管 HTTPS/证书限定为标准应用 Web 入口。
- WAF 保护标准 Web 路径，不覆盖所有原生协议。
- Enforce VPN 是管理员收紧非公开入口公网访问的策略；Public 服务仍可公开。
- `.local` 使用 HTTP。
- Home、Data、Common 属于跨节点持久数据面；Cache 为节点本地可重建空间。
- Files 是统一文件数据面，不表述为 NAS 或集中式网盘。
- Managed RAID storage 标为 **Next**。

## 研究依据

完整网络、身份、资源、Files、代码/docs 索引与产品边界见 [olares-sandbox-notes.md](./olares-sandbox-notes.md)。
