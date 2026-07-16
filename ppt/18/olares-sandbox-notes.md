# Olares Application Sandbox 笔记

> Intel 商业合作 Pitch 第 18 页的合并底稿。吸收原第 19 页 Files/Storage 与第 20 页 Network 研究；快照日期：2026-07-15。

## 使用口径

这不是当前 main 的 release note，而是面向合作方表达完整产品方向和未来 2–3 个月目标架构的 Pitch：

- 主 Slide 可以纳入已在其他分支实现、正在集成或近期交付的 WAF、Linkerd、Managed RAID 等能力。
- 团队产品判断高于单个本地 checkout；main 和本地仓库仅用于解释架构、补充证据与记录边界。
- 不使用“当前 main 未检出”否定项目能力，也不在主画面堆成熟度标签削弱商业叙事。
- 取舍标准是合作价值、架构完整性和近期交付方向。

## Part A · 沙盒整体叙事

### 为什么要沙盒（多用户系统）

沙盒的动机是 **Olares 是一个多用户系统**：多个用户、他们安装的应用、以及代表他们工作的 Agent 共享同一台设备。所以沙盒隔离的是三个对象：

| 对象 | 携带什么 | 隔离/授予口径 |
|---|---|---|
| **User** | 身份与角色 | RBAC 决定每个用户能触达什么 |
| **Application** | 网络、存储、资源信封 | 通过 Manifest 声明式授予，默认隔离 |
| **Agent** | 代表某个用户、在某个应用内行动 | 权限 = 用户角色 ∩ 宿主应用被授予的能力（delegated, bounded） |

叙事顺序：先讲"为什么要沙盒（多用户）+ 隔离哪三个对象"（进主/副标题），再回答四个连续问题：**谁能行动 → 应用如何运行 → 应用如何连接 → 应用能看到什么数据**。页面按 01 Identity → 02 Runtime & resource → 03 Network → 04 Files 展开。

- **主标题**：`Olares OS Sandboxes Every User, Application and Agent`。
- **副标题**：`One multi-user device — users, applications and Agents run side by side, isolated by default and granted only what they declare.`
- 不再单设叙事带，避免与标题/副标题重复。

四区标题统一使用问题式叙事，副标题只承担事实型能力摘要：

| # | Title | Subtitle |
|---|---|---|
| 01 | **Who can act—and on whose behalf** | Unified authentication, workload authorization and secrets custody across users, applications and Agents. |
| 02 | **How each application runs** | Isolated runtimes, reduced privileges and explicit resource envelopes. |
| 03 | **How each application connects** | Four access paths, protected by declared entrances and layered security. |
| 04 | **What data each application can see** | Olares Files applies declared scopes across persistent, connected and Agent-ready storage. |

`Cloud-native security, built for real-world networks` 与 `Governed like cloud infrastructure. Familiar like a PC. Ready for Agents.` 属于感性产品定位，放入逐字稿，不再占用主画面标题或副标题。

### 01 · Identity & authorization 三列口径

1. **Unified identity**
   - **One sign-in across the system.** Authelia 是统一认证入口（authentication），避免每个服务分别建立登录边界。
   - **Roles stay consistent everywhere.** LLDAP 是统一用户/群组目录，不表述成 authz 服务；目录中管理用户、群组以及 Admin / Member 等角色。
2. **ReBAC & Agent delegation**
   - **Every workload receives only what it needs.** Kubernetes 原生 Role / ServiceAccount 管理 workload 权限，应用不获得整台设备的 authority。
   - **People and groups keep their own boundaries.** ReBAC 面向 Search、Files、IM，按用户、群组与资源关系提供更细粒度授权；Agent 只能在 workload RBAC 与关系授权组合后的范围内行动。
3. **Secrets & key custody**
   - **Sensitive credentials stay out of applications.** 当前由 Infisical 管理 LLM API keys、Agent cookies 等 secrets，后续由 OpenBao 承接统一 secret management。
   - **Key custody can move into hardware.** 底层暴露 HSM 接口，允许用户对接第三方 HSM；对外措辞使用 hardware key custody / third-party HSM integration。

主 Slide 使用三列，每列采用 Slide 21 的文案结构：**能力标题 + 粗体引导句 + 1–2 句解释**，不单列 Agent delegation。

### Slide 18 字号与安全区

以 [ppt/design-system.md](../design-system.md) 为单一视觉事实源：

- 左右安全边距 `44px`，顶部 `24px`，底部 `18px`。
- 主标题 `28px`，副标题 `14px`；分区标题约 `16px`。
- 能力标题 `12.5–13.5px`，主画面正文不得低于 `10.5px / 1.36`。
- `01/02/03/04` kicker 不低于 `10.5px`。
- 内容放不下时删冗余并下沉到逐字稿，不允许继续用 `6.7–8.8px` 小字塞满页面。
- 主体上排按内容自然撑开，下排使用剩余高度；不通过比例行高制造空白。

### 一句话

**Olares Application Sandbox 用同一份应用契约治理网络、身份和数据：默认隔离，按需授予。**

沙盒不只等于容器：

| Boundary | 解决的问题 |
|---|---|
| **User & application** | 哪个用户拥有应用，哪些应用与用户空间相互分离 |
| **Identity & permissions** | 谁可以访问，使用什么认证强度和角色 |
| **Runtime / execution** | 应用在什么运行时边界中执行，以及声明权限如何在运行前被校验 |
| **Resource** | 应用可以消耗多少 CPU、memory 与 accelerator |
| **Secrets** | 哪些密钥和凭证可以下发给哪个应用 |
| **Network** | 应用从哪些路径进入，哪些 Web、Native、LAN 能力被允许 |
| **Storage** | 应用能挂载哪些目录，数据属于谁、是否持久、能否跨节点共享 |

### 管理层应带走的观点

1. **不是暴露设备，而是治理应用。**
2. **不是一个共享根目录，而是有所有者与耐久性边界的文件空间。**
3. **不是让用户运维网络和卷，而是由系统把策略变成 Manifest 契约。**
4. **不是限制 Agent，而是让 Agent 在明确权限内使用完整网络与文件能力。**

### Slide 合并原则

- 采用 `2×2` 四分区：左上 01 Identity & authorization，右上 02 Runtime & resource isolation，左下 03 Network，右下 04 Olares Files。
- 左右严格等分 `50 / 50`；上排内容较少，高度约 `42%`，下排 Network 与 Files 信息更多，高度约 `58%`。
- 四区采用 Editorial Matrix：Identity `2×2`、Runtime 横向三列、Network `2×2`、Files `2×3`，避免每项都成为贯穿整栏的细长条。
- 视觉依靠留白、对齐和少量 hairline 分组，不增加圆角卡片或独立背景色。
- 01 回答谁能行动、代表谁行动，以及 secrets / keys 如何托管；采用 Unified identity、ReBAC & Agent delegation、Secrets & key custody 三列。
- 02 回答应用如何隔离运行、拥有多少系统权限、可消耗多少资源。
- 03 回答应用如何被访问，以及 Olares 如何在企业级安全与现实网络兼容性之间取得平衡。
- 04 将 Olares Files 的 9 点能力压缩为 6 点，保留完整产品叙事但降低页面占比。
- Runtime、Identity、Resource、Secrets 是独立沙盒维度，不叫 Shared controls。
- Manifest 与 OPA 是贯穿四块的 Declarative policy spine：Manifest declares → OPA validates → Platform enforces；保留在逐字稿和内部笔记中，主画面不设页脚或第五个容器。
- 原网络页和存储页的产品细节进入逐字稿或本笔记，不再保留两个独立能力墙。
- 左下保留四行网络结构；Internet 主画面只表达免费域名、托管证书、自定义域名和可选反向代理，L4 Gateway / WAF 链路下沉到逐字稿与内部笔记。
- 全页只讲功能特点，统一中性配色，不使用深绿色块或任何独立配色容器；视觉靠编辑式列表、编号和细分隔线，删除多层卡片、圆角框与无效留白。

### 沙盒维度与策略层

- **Network boundary & access**：网络与通信范围，以及域名、HTTPS、VPN 和 LAN compatibility。
- **Data & filesystem boundary**：应用可见路径、挂载范围、所有权、持久性与共享方式。
- **Identity & authorization boundary**：用户、应用身份与 RBAC 授权。
- **Runtime / execution isolation**：每应用独立运行时边界，按用户分 namespace、默认非特权容器；OPA admission 在安装或运行前校验声明权限。
- **Resource governance**：CPU、memory、accelerator requests 描述需求；系统压力下由 Olares 智能驱逐 workload，维持整体稳定并保障关键服务。
- **Secrets management**：每应用作用域的密钥与凭证按声明下发，不跨沙盒共享、不打进镜像。
- **Declarative policy spine**：Manifest 负责声明，OPA 负责准入校验，平台组件负责运行时执行。

Runtime/kernel isolation 是合格沙盒的重要基础，本页以 Runtime isolation 高层口径纳入治理块，不展开内核机制。Secrets management 指应用作用域的 secret/credential 下发，不等于 LarePass Vault 的用户密码与 TOTP 管理。Network 的反向代理、域名和 VPN 是 connectivity 与 access feature，不单独作为“网络隔离”证据。

---

## Part B · Network sandbox

### B1. 四条网络路径

| Path | Pitch 能力 | Slide 表述 |
|---|---|---|
| **Internet** | 免费 Olares 域名、托管 HTTPS 证书、自定义域名、Olares Tunnel / 自建 FRP 等可选反向代理 | Domains and HTTPS come ready |
| **VPN · LarePass** | Tailscale client、本地 Headscale、LAN / P2P / relay 自动选路 | Private access without a third-party control plane |
| **Local network** | `.local` HTTP、本地标准域名、按应用启用的 Overlay Gateway | Web access plus native LAN compatibility |
| **In-cluster** | Linkerd service mesh、automatic mTLS、ServiceAccount identity、fine-grained policy、traffic metrics / audit signals | Identity-aware service mesh |

Internet 与 VPN · LarePass 是独立网络选择。LarePass 使用 Tailscale 客户端并由 Olares 本地托管 Headscale 控制面，避免依赖第三方控制平面。LAN、P2P、DERP relay 是自动选择的连接路径，不是三种产品模式。

Internet 主画面优先呈现“默认可用 + 保留选择权”：标准 Web 入口默认获得免费 Olares 域名和托管证书，也允许用户使用自定义域名及自选反向代理。安全链路仍存在，但不再用 `L4 Gateway → WAF → Identity → App` 占用主画面空间。

### B2. Web security path

目标 Web 链路：

**Network path → L4 Gateway → WAF → declared application entrance → application**

- **L4 Gateway** 汇聚 Web 流量和应用声明的原生端口。
- **WAF** 位于网关之后，为标准 Web 入口提供应用层安全防护。
- **Declared entrance** 管理域名、HTTPS、身份、Public / Private / Internal 和路由。
- WAF 不覆盖所有 Native services 或 LAN discovery。

主 Slide 不展开代理实现、WAF 规则引擎、sidecar 或组件版本。

### B3. Managed DNS/TLS lifecycle

- 系统维护标准域名、HTTPS 路由和 TLS 证书生命周期。
- 证书配置包含获取、应用和重新获取流程。
- 符合条件的入口支持自定义域名。
- `.local` 是 HTTP 局域网方式，不描述成默认 HTTPS。
- Managed DNS/TLS 只针对标准 Web 入口，不扩展为任意原生协议。

### B4. Multi-user identity

- 每个用户拥有独立应用空间和入口域名。
- Super Admin / Admin / Member 等角色承担不同管理权限。
- 系统统一身份支持 One-factor / Two-factor。
- 应用入口可选择认证强度与访问策略。
- Olares 登录 2FA 与 Vault 中保存第三方网站 TOTP 的 Authenticator 是两类能力，不能混写。

### B5. Entrance-level policy

| Policy | 对外表述 |
|---|---|
| **Public** | 面向网站、博客等公开服务 |
| **Private** | 仅已认证用户访问 |
| **Internal** | 在 VPN · LarePass 内无感访问 |
| **Enforce VPN** | 管理员收紧非公开入口的公网访问，Public 入口仍可放行 |

Enforce VPN 是管理员级策略，不是每个入口独立配置的开关，也不等于整台 Olares 只能通过 VPN 访问。

### B6. Web、Native 与 LAN compatibility

- **Web applications**：Domain · HTTPS · Identity · entrance policy。
- **Native services**：私人 VPN 与应用显式声明的端口。
- **LAN compatibility**：设备发现和局域网原生协议按应用开启。

Manifest 中与非 Web 能力相关的声明包括 `ports[]`、Tailscale ACL 接入和出站端口约束。`.local` HTTP 是本地 Web 访问路径；Overlay Gateway 则按应用启用，面向可信局域网中的智能家居、投屏、媒体和设备发现等原生协议，不表述成“第三方应用直接获得宿主机网络”。

### B7. Linkerd service mesh

- Linkerd 为纳入 mesh 的 pod 间 TCP 通信自动启用 mTLS；证书身份绑定 Kubernetes ServiceAccount，并自动轮换。
- `AuthorizationPolicy` 可对 service / port / HTTP route 设置细粒度访问规则；主画面将其压缩为 fine-grained policy。
- traffic metrics 提供流量可观测性；authorization audit mode 可把未匹配策略的请求写入日志并标记到 metrics，主画面压缩为 audit signals。
- 对外使用 **Identity-aware service mesh**：强调 workload identity、加密、授权、可观测与治理，不称为 “zero trust by default”，也不把 audit signals 表述成不可篡改的审计日志。
- Pitch 主画面可以展示 Linkerd。
- 不在主画面展开 sidecar、HTTPRoute、CIDR、证书轮换周期或 NetworkPolicy 模板。
- 当前 main 可见实现不用于否定其他分支或集成路径中的 Linkerd 能力。

### B8. Network 证据索引

#### Internet、VPN 与入口

- `docs/manual/larepass/private-network.md`
- `docs/manual/olares/settings/remote-access.md`
- `docs/manual/olares/settings/change-frp.md`
- `docs/developer/concepts/network.md`
- `docs/manual/olares/settings/manage-entrance.md`
- `docs/manual/olares/settings/custom-app-domain.md`
- `docs/developer/develop/package/manifest.md`
- `framework/bfl/pkg/apis/settings/v1alpha1/reverseproxyconf.go`
- `framework/bfl/pkg/apis/settings/v1alpha1/handler_application.go`
- `framework/l4-bfl-proxy/internal/translator/translator.go`
- `framework/l4-bfl-proxy/internal/provider/provider.go`

#### Local network

- `docs/manual/best-practices/local-access.md`
- `docs/reusables/local-domain.md`
- `docs/manual/olares/settings/overlay-gateway.md`
- `docs/use-cases/home-assistant.md`
- `docs/use-cases/stream-media.md`
- `daemon/internel/apiserver/handlers/handler_overlay_gateway_status.go`

#### 身份、隔离与 TLS

- `framework/l4-bfl-proxy/internal/xds/translator/translator.go`
- `framework/app-service/pkg/sandbox/sidecar/envoy.go`
- `framework/app-service/controllers/security_controller.go`
- `framework/app-service/pkg/security/templates.go`
- `framework/app-service/pkg/gateway/`
- `framework/bfl/pkg/watchers/network_activation/network_activation.go`
- `framework/app-service/pkg/gateway/routecontrol/entrance_tls.go`

以上是当前 main 可见证据。WAF 与 Linkerd 的项目能力可能位于其他分支或集成路径，状态以团队信息与 Pitch 目标架构为准。

---

## Part C · Olares Files

### C1. 一句话

**Applications get sandboxed storage. Users get a PC-class Files experience. Agents get one URL model across storage media.**

Universal Storage 不是把所有数据复制进一个物理存储池，而是统一 namespace、POSIX 语义、沙盒权限、跨节点操作和 Agent 数据入口。

### C1.1 Slide 产品层级

主 Slide 的右下区不应只画 Home / Data / Cache / Common，也不应复制全部 9 点能力。页面压缩为 6 点：

1. **Sandboxed spaces**：Home / Data / Cache / Common，所有权、持久性、共享边界与 Manifest grants。
2. **Cross-node data plane**：Home / Data / Common 跨节点持久；Cache 节点本地可重建。
3. **Connected storage**：合并 Sync、Cloud ecosystem、External storage & devices；覆盖设备、云盘、USB、SMB、NFS、现有 NAS，Managed RAID 为 Next。
4. **PC-grade Files & sharing**：合并 PC 级文件操作、后台任务、内部用户、公开链接和 SMB 分享。
5. **Search**：文件名、全文与图片；Search discovers，Files acts。
6. **Unified access URLs**：本地、分布式、云端与外部存储统一为 Agent-facing URL 地址模型，屏蔽后端 API 差异。

完整 9 点仍保留在本笔记后续章节作为产品能力地图，主 Slide 仅做视觉压缩。叙事收口：**Governed like cloud infrastructure. Familiar like a PC. Ready for Agents.**

### C2. 四类核心空间

| Space | Files path | Manifest permission | Owner / purpose | Durability |
|---|---|---|---|---|
| **Home** | `drive/Home/...` | `userData` | 用户文档、媒体与可授权文件 | 持久、跨节点 |
| **Data** | `drive/Data/<appName>/...` | `appData: true` | 单应用数据库、配置和私有状态 | 持久、跨节点 |
| **Cache** | `cache/<node>/<appName>/...` | `appCache: true` | 临时文件、模型中间产物和缓存 | 节点本地、可重建 |
| **Common** | `drive/Common/...` | `appCommon: true` | 多应用共享模型权重和公共素材 | 集群 RWX、跨节点 |
| **External** | `external/<node>/<volume>/...` | `externalData: true` | HDD、USB、SMB、NFS | 取决于外部介质 |

四类核心空间共同定义：

1. 数据属于用户、单个应用还是多个应用。
2. 数据需要长期保存还是可以重新生成。
3. 数据只在本节点使用还是需要跨节点共享。

应用通过 Manifest permission 获得所需挂载。沙盒边界因此包含文件作用域，不只是容器隔离。

### C3. AppData 命名陷阱

- **Chart `appData`**：应用私有持久状态，位于 `drive/Data/<appName>/...`。
- **LarePass UI “AppData” / `CACHE_ALIAS="/AppData"`**：实际指 `cache/<node>/...`，对应 Chart `appCache`，是节点本地可重建数据。
- `drive/Home/Data` 与 `drive/Home/Cache` 是 Home 下的系统目录，不等于上述应用存储。

这个差异必须保留在内部笔记和问答中。

### C4. Cross-node data plane

```text
POSIX files and directories
        ↓
JuiceFS distributed filesystem
        ↓
S3-compatible object storage
```

- JuiceFS 提供文件、目录、权限和跨节点访问语义。
- S3-compatible backend 保存对象块，可以是集群内对象存储或外部 S3、OSS、COS 等。
- Home、Data、Common 进入跨节点持久层。
- Cache 刻意保持节点本地，以换取低延迟和吞吐。
- “跨节点可见”不等于所有目录可以在任意节点任意多主写入；平台仍受调度、PVC access mode 与 master 路由约束。

### C5. Connected extensions

| Space | Product meaning | Internal implementation reference |
|---|---|---|
| **Sync** | 把电脑和移动设备上的数据接入 Files | Seafile-backed library |
| **Cloud** | Google Drive、Dropbox、S3 等账户 | rclone-backed remote |
| **External** | USB、HDD、SMB、NFS、existing NAS | node mount via terminusd |
| **Share** | 在原始数据上增加身份、权限和入口 | metadata layer, not a copied file |

表达边界：

- `70+ via rclone ecosystem` 表示 rclone 官方生态，不表示每个 provider 的 UI、OAuth、搜索、分享和写操作都同等产品化。
- Sync 与 Home 平行，不是 Home 下的普通同步文件夹。
- `SMB / NFS mount → External` 是把外部数据接入 Olares。
- `Olares directory → SMB share` 是把 Olares 目录提供给局域网客户端。
- 可以写 NFS mount，不能写内置 NFS server。
- Managed RAID storage 是 **Next**。

### C6. Unified access URLs for Agents

Agent 不需要分别学习 JuiceFS、S3、Google Drive、Dropbox、Seafile、SMB 或 NFS API。Files 将不同存储介质映射为一致的 URL 地址模型：

- URL 是 Agent-facing access contract，屏蔽本地、分布式、云端和外部存储的后端差异。
- Search 不知道地址时先发现候选；Files 校验权限后返回或使用统一 URL 执行访问与操作。
- 统一 URL 不表示所有数据被复制到同一个存储池，也不表示所有 backend 具有完全相同的搜索、分享或写入能力。
- POSIX 仍可作为 Cross-node data plane 和应用运行时的底层文件语义，但不再等同于 Agent 的统一访问接口。

### C7. Files、Search 与后台任务

- **Files**：已知路径后执行浏览、读取、上传、编辑、复制、移动、压缩、分享。
- **Search**：不知道路径时，根据文件名或内容发现候选。
- Agent 的正确顺序是 `Search discovers → Files verifies and acts`。
- POSIX 可见空间使用 search3；Sync 使用 Seafile search；Cloud 默认不进入 search3。
- 文件名索引范围较广不等于全部内容都全文索引；默认全文范围是 `Home/Documents`。
- 跨存储 Copy / Move 由后台任务组织，Sync 与 Cloud 间可能使用 Cache / UI AppData 暂存。

### C8. Sharing 与数据位置

| Sharing | Audience |
|---|---|
| **Internal** | Olares 内部用户 |
| **External** | 带权限、密码与有效期的公开访问 |
| **SMB** | 局域网客户端 |

分享元数据与原始文件内容分离，内容继续留在原存储。不同来源、单文件/目录和目标版本的限制需要单独确认。

### C9. Storage 代码边界

- Files 仓库不能证明平台备份、快照或恢复能力。
- POSIX 删除不等于 Files 提供回收站或版本历史。
- Seafile repo 访问不等于仅凭 Files 仓库可以证明完整跨设备客户端同步。
- 多节点统一接口仍存在节点路由、master 与 access mode 约束。
- 不写“所有数据统一全文搜索”。
- 不把 Olares Files 写成 NAS、NAS 替代或集中式网盘。

### C10. Storage 证据索引

#### Files 主架构与 Driver

- `/Users/pengpeng/files/cmd/backend/main.go`
- `/Users/pengpeng/files/cmd/backend/app/root.go`
- `/Users/pengpeng/files/pkg/hertz/hertz.go`
- `/Users/pengpeng/files/pkg/hertz/biz/router/register.go`
- `/Users/pengpeng/files/pkg/drivers/base/interface.go`
- `/Users/pengpeng/files/pkg/drivers/driver.go`
- `/Users/pengpeng/files/pkg/hertz/biz/handler/utils.go`

#### Userspace 与路径

- `/Users/pengpeng/files/pkg/models/file_param.go`
- `/Users/pengpeng/files/pkg/global/pvc.go`
- `/Users/pengpeng/files/pkg/common/constant.go`
- `/Users/pengpeng/files/pkg/drivers/posix/posix/posix.go`
- `/Users/pengpeng/olares/framework/app-service/pkg/appinstaller/helm_utils.go`
- `/Users/pengpeng/olares/cli/cmd/ctl/files/path.go`
- `/Users/pengpeng/olares/cli/skills/olares-shared/references/olares-platform.md`

#### Files 操作、任务与媒体

- `/Users/pengpeng/files/pkg/hertz/biz/handler/api/resources/resources_service.go`
- `/Users/pengpeng/files/pkg/hertz/biz/handler/api/tree/tree_service.go`
- `/Users/pengpeng/files/pkg/hertz/biz/handler/api/raw/raw_service.go`
- `/Users/pengpeng/files/pkg/hertz/biz/handler/upload/upload_service.go`
- `/Users/pengpeng/files/pkg/hertz/biz/handler/api/archive/archive_service.go`
- `/Users/pengpeng/files/pkg/tasks/manager.go`
- `/Users/pengpeng/files/pkg/tasks/task_paste_posix.go`
- `/Users/pengpeng/files/pkg/tasks/task_paste_sync.go`
- `/Users/pengpeng/files/pkg/tasks/task_paste_cloud.go`
- `/Users/pengpeng/files/pkg/media/api/controllers/dynamic_hls_controller.go`

#### Sync、Cloud 与 External

- `/Users/pengpeng/files/pkg/drivers/sync/sync.go`
- `/Users/pengpeng/files/pkg/drivers/sync/seahub/seaserv/service.go`
- `/Users/pengpeng/files/pkg/drivers/sync/seahub/upload.go`
- `/Users/pengpeng/files/pkg/drivers/clouds/cloud.go`
- `/Users/pengpeng/files/pkg/drivers/clouds/rclone/rclone.go`
- `/Users/pengpeng/files/pkg/integration/integration.go`
- `/Users/pengpeng/files/pkg/hertz/biz/handler/api/external/external_service.go`
- `/Users/pengpeng/files/pkg/global/external.go`
- `/Users/pengpeng/files/pkg/samba/samba.go`
- `/Users/pengpeng/files/cmd/samba/main.go`

#### Search

- `/Users/pengpeng/files/pkg/hertz/biz/handler/api/search/search_service.go`
- `/Users/pengpeng/files/pkg/drivers/sync/seahub/search.go`
- `/Users/pengpeng/search/src/server_main.rs`
- `/Users/pengpeng/search/src/monitor_main.rs`
- `/Users/pengpeng/search/src/utils/task_tool.rs`
- `/Users/pengpeng/search/src/controller/search3server/search_controller.rs`
- `/Users/pengpeng/search/src/extractor/factory.rs`

#### Agent CLI

- `/Users/pengpeng/olares/cli/cmd/ctl/search/root.go`
- `/Users/pengpeng/olares/cli/skills/olares-search/SKILL.md`
- `/Users/pengpeng/olares/cli/skills/olares-files/SKILL.md`
- `/Users/pengpeng/olares/cli/skills/olares-files/references/olares-files-paths.md`

#### 外部生态来源

- [Rclone supported backends](https://rclone.org/)
- [Rclone overview](https://rclone.org/overview/)
- [Rclone backend tiers](https://rclone.org/tiers/)
- [AgentFS GitHub](https://github.com/tursodatabase/agentfs)
- [AgentFS with FUSE](https://turso.tech/blog/agentfs-fuse)

---

## Part D · 统一术语与待确认项

### 术语

| 中文概念 | 英文固定写法 |
|---|---|
| 应用沙盒 | **Application Sandbox** |
| 网络沙盒 | **Network sandbox** |
| 沙盒化文件空间 | **Sandboxed storage** |
| Files 产品主线 | **Olares Files · Unified access URLs** |
| 应用网关 | **L4 Gateway** |
| Web 应用防火墙 | **WAF · Application-layer protection** |
| 多用户身份 | **Multi-user identity** |
| 一/二次认证 | **One-factor / Two-factor authentication** |
| 入口级策略 | **Entrance-level policy** |
| 局域网兼容能力 | **LAN compatibility** |
| 安全服务间通信 | **Secure service-to-service communication** |
| 沙盒文件空间 | **Sandboxed spaces** |
| Manifest 权限挂载 | **Manifest-gated mounts** |
| 跨节点数据面 | **Cross-node data plane** |
| Agent 统一访问 URL | **Unified access URLs** |

不用 `network isolation` 指代网络模式；隔离是基础能力。不用 `onlyVPN`，统一使用 **Enforce VPN**。

### 待确认

1. 统一 Internal 在不同网络文档中的定义。
2. 统一当前反向代理选项对 Cloudflare Tunnel 的表述。
3. 统一 Custom domain 对不同入口类型的支持边界。
4. 补齐 WAF 与 Linkerd 所在分支、配置面和交付状态的内部索引。
5. 确认 Common、Sharing、Search 与各 Cloud provider 在目标版本的具体覆盖。
6. Managed RAID 的目标能力、管理面和合作时间点。
7. **Agent 权限 = 用户角色 ∩ 宿主应用被授予的能力** 的确切实现与对外措辞需团队确认；当前无 main 证据，按 Pitch 产品判断上页，措辞保持克制（delegated, bounded）。
8. **Secrets management** 的声明字段、注入方式、运行时边界与目标版本覆盖需按合作架构确认；对外不得与 LarePass Vault（用户密码/TOTP）混写。

这些事项不影响第 18 页的 Pitch 主线，但正式产品文档或交付承诺前应按目标版本核对。
