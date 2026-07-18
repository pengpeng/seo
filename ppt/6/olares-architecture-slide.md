# One Complete Personal Cloud Solution, Powered by a Five-Layer OS

> Intel 合作 PPT 第 6 页。中文 Slide 文案初稿。已并入原第 7 页（One-Stop Solution 产品家族）：左侧＝一站式解决方案，右侧＝五层架构。

---

## Slide copy

### 标题

**One Complete Personal Cloud Solution, Powered by a Five-Layer OS**

Olares 将用户所需的一切，与开源、云原生的应用操作系统整合在一起，并运行在用户自己的硬件上。

### 左侧 · 一站式解决方案

- **Olares OS** — 开源的五层操作系统（即右侧整套架构）。
- **Clients** — 桌面、移动端与浏览器扩展。
- **Olares Space** — 管理域名、网络、远程访问与备份。
- **Olares Market** — 200+ 应用一键安装。
- **Olares CLI & Skills** — 用自然语言配合 agent 管理 Olares 系统。

### 右侧 · 五层架构（各层提供什么）

| Olares 层 | 该层提供什么 | 页面上的图标 chips |
|----------|------------------------|------------------------|
| **Community apps** | 200+ 应用，共享同一套运行环境；AI、生产力、媒体与智能家居应用均可从 Olares Market 一键安装 | LobeChat、Dify、ComfyUI、Immich、Nextcloud、Home Assistant |
| **Built-in apps** | 开箱即用：文件、身份、知识、监控、系统管理与应用开发共享一套体验 | Desktop、Files、Market、Settings、Dashboard、Control Hub、Vault、Wise |
| **Framework** | 应用成为受治理的系统公民：生命周期、权限、SSO、网络入口与跨应用调用统一管理 | Lifecycle、Identity & SSO、Permissions、Networking、App Manifest |
| **Platform · PaaS** | 共享服务替代重复搭建：应用可复用数据、中间件、文件、备份与可观测 | PostgreSQL、KVRocks、NATS、JuiceFS、Prometheus、Velero |
| **Infrastructure · IaaS** | 硬件变成可调度的资源平面：计算、存储、网络、节点与加速统一编排 | Kubernetes、K3s、containerd、Helm、MinIO、HAMi |

上三层为类 Android 的开放应用 OS，下两层为云原生资源底座。右侧以"各层价值介绍"为主，chips 只保留可辨识的图标+名称工具；纯文字内部标识符（OlaresManifest、app-service、system-server、bfl、TAPR、olaresd、olares-cli）从页面移除，保留在 [references.md](./references.md)。

### 收口

**类 Android 的开放应用操作系统 + 开源云原生 PaaS / IaaS，运行在用户自己的硬件上。**

---

## 工作底稿

- 已并入原第 7 页（One-Stop Solution）：五个产品从原独立页移到本页左栏，作为"交付产物"，与右侧五层架构平行呈现。
- chips 去掉白色药丸背景（透明、无白底无边框）：app 图标显示为小圆角贴片，stack logo 为透明标识，各自带名称标签。Framework 补 Envoy（网关 / 网络入口，app-gateway / l4-bfl-proxy 在用）；Platform 补 KVRocks（KV 缓存）。
- **架构参照**列（Android / AWS 类比）从主画面移除，保留在 [references.md](./references.md) 与逐字稿中；各层"提供什么"价值文案是右侧主要内容，代表性实现只保留可辨识的图标 chips，纯文字内部标识符移入 references。
- 架构图按自上而下展示：Community apps → Infrastructure；依赖顺序为 Infrastructure → Platform → Framework → Built-in apps → Community apps。
- 双栏采用设计规范"侧栏 + 主表"布局：左为一站式交付产物面板，右为五层架构表；通过侧边线与背景层次区分上三层应用 OS 与下两层云原生底座。
- `Open source · AGPL-3.0` 是贯穿五层的属性，不单独作为一层。
- Android、SaaS / AI 产品与 AWS 服务均为架构参考或功能类比，不表示 Android 应用兼容、API 兼容或实现相同。
- 本页不呈现 NAS 对比；相关判断只进入逐字稿。
