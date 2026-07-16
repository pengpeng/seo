# Slide 6 参考资料

> 用于核查“Olares 五层架构 + 交付产物”主画面与逐字稿。本页已并入原第 7 页（One-Stop Solution）。Olares 代码仓库快照：2026-07。Android、SaaS / AI 产品和 AWS 仅用于架构参考或功能类比，不表示 Android 应用兼容、API 兼容或实现相同。

## 总体定位

- Olares 是开源个人云操作系统，核心仓库采用 AGPL-3.0：
  - [Olares README](/Users/pengpeng/Olares/README.md)
  - [LICENSE](/Users/pengpeng/Olares/LICENSE)
- 官方架构将系统拆为 Infrastructure、Platform、Application framework 与 System applications；本页将 Market 中的第三方应用单列为 Community apps，形成面向演示的五层视图：
  - [Olares system architecture](/Users/pengpeng/Olares/docs/developer/concepts/system-architecture.md)
- 仓库目录对应 Infrastructure、Platform、Framework、Apps 与 CLI：
  - [Infrastructure README](/Users/pengpeng/Olares/infrastructure/README.md)
  - [Platform README](/Users/pengpeng/Olares/platform/README.md)
  - [Framework README](/Users/pengpeng/Olares/framework/README.md)
  - [Apps README](/Users/pengpeng/Olares/apps/README.md)

## 交付产物（并入自原第 7 页）

右栏"交付产物"列出 Olares 一站式方案的五个产品，与左侧五层架构平行呈现：

- **Olares OS** — 开源的五层操作系统，即左侧整套架构。
- **Clients** — 桌面、移动端与浏览器扩展。
- **Olares Space** — 管理域名、网络、远程访问与备份。
- **Olares Market** — 200+ 应用一键安装。
- **Olares CLI & Skills** — 用自然语言配合 agent 管理 Olares 系统。

截图取自 `assets/olares-one-stop-solution-assets/`（olares_os / clients / olares_space / olares_market / olares_cli）。

## 五层依据与能力类比

### 1. Infrastructure

- **Olares**：K3s / Kubernetes、containerd、Calico、CoreDNS、etcd、Helm、MinIO、Restic、GPU 管理、`olaresd` 与 `olares-cli` 共同编排节点、计算、网络、存储和加速资源。
- **AWS 功能类比**：EC2 / accelerated computing instances、EKS、VPC、EBS / EFS。
- 依据：
  - [Infrastructure README](/Users/pengpeng/Olares/infrastructure/README.md)
  - [System architecture · Infrastructure](/Users/pengpeng/Olares/docs/developer/concepts/system-architecture.md#infrastructure)
  - [Amazon EC2](https://aws.amazon.com/ec2/)
  - [Amazon EKS](https://aws.amazon.com/eks/)
  - [Amazon VPC](https://aws.amazon.com/vpc/)
  - [Amazon EBS](https://aws.amazon.com/ebs/)
  - [Amazon EFS](https://aws.amazon.com/efs/)
  - [EC2 accelerated computing instances](https://aws.amazon.com/ec2/instance-types/accelerated-computing/)

### 2. Platform

- **Olares**：平台层提供数据库、KV 缓存、消息、文件系统、工作流、可观测性、应用运行时与备份能力。主要组件包括 PostgreSQL、KVRocks、NATS、JuiceFS、Prometheus、TAPR 与 Velero。
- **AWS 功能类比**：RDS、ElastiCache、SQS / SNS、S3 / EFS、CloudWatch、AWS Backup。
- 依据：
  - [Platform README](/Users/pengpeng/Olares/platform/README.md)
  - [System architecture · Platform](/Users/pengpeng/Olares/docs/developer/concepts/system-architecture.md#platform)
  - [Amazon RDS](https://aws.amazon.com/rds/)
  - [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
  - [Amazon SQS](https://aws.amazon.com/sqs/)
  - [Amazon SNS](https://aws.amazon.com/sns/)
  - [Amazon S3](https://aws.amazon.com/s3/)
  - [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
  - [AWS Backup](https://aws.amazon.com/backup/)

### 3. Framework

- **Android 架构参考**：对应 Android Application Framework 对应用暴露统一系统服务、权限与生命周期管理的角色；不表示兼容 Android APK 或 Android API。
- **Olares**：`app-service` 负责应用生命周期与资源分配；`system-server` 管理跨应用权限与路由；Authelia / LLDAP 提供认证、MFA 与 SSO；OPA 提供集群准入策略。应用通过 `OlaresManifest.yaml` 声明入口、权限、依赖、中间件与加速资源。
- **AWS 功能类比**：IAM / Cognito、API Gateway、App Runner / Elastic Beanstalk。
- 依据：
  - [Android platform architecture](https://developer.android.com/guide/platform)
  - [Android application fundamentals](https://developer.android.com/guide/components/fundamentals)
  - [Framework README](/Users/pengpeng/Olares/framework/README.md)
  - [OlaresManifest specification](/Users/pengpeng/Olares/docs/developer/develop/package/manifest.md)
  - [Network isolation](/Users/pengpeng/Olares/docs/developer/concepts/network.md)
  - [app-service README](/Users/pengpeng/Olares/framework/app-service/README.md)
  - [Open Policy Agent in Olares](/Users/pengpeng/Olares/platform/open-policy-agent/README.md)
  - [AWS IAM](https://aws.amazon.com/iam/)
  - [Amazon Cognito](https://aws.amazon.com/cognito/)
  - [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
  - [AWS App Runner](https://aws.amazon.com/apprunner/)
  - [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

### 4. Built-in apps

- **Android 架构参考**：对应 Android System Apps 作为系统能力的默认用户入口；不表示两者应用集合或实现相同。
- **Olares**：预装系统应用包括 Desktop、Files、Wise、Vault、Market、Settings、Dashboard、Control Hub 与 Studio。
- **产品体验类比**：文件与同步、密码管理、阅读与知识管理、系统控制台、应用商店；不是对 Dropbox、Google Drive、1Password、Pocket / Feedly 等产品的 API 兼容声明。
- 依据：
  - [Android platform architecture](https://developer.android.com/guide/platform)
  - [Apps README](/Users/pengpeng/Olares/apps/README.md)
  - [System architecture · System applications](/Users/pengpeng/Olares/docs/developer/concepts/system-architecture.md#system-applications)

### 5. Community apps

- **Android 架构参考**：对应第三方应用与应用分发生态的角色；Google Play 是功能类比，不是 Olares 的开源组件。
- **Olares**：Olares Market 为社区应用提供安装、卸载与升级入口；应用使用 Olares Application Chart 与 OlaresManifest 分发。
- **SaaS / AI 工作负载类比**：本地应用覆盖聊天与模型服务、生成式图像、照片管理、文件同步、知识协作与智能家居等类别。示例包括 LobeChat / Dify、ComfyUI、Immich、Nextcloud、Home Assistant 与 Olares 的 LLM engine bases。
- 依据：
  - [Android platform architecture](https://developer.android.com/guide/platform)
  - [Olares Market](https://market.olares.com/)
  - [Olares community app catalog](https://github.com/beclab/apps)
  - [Olares README · Features](/Users/pengpeng/Olares/README.md#features)
  - [OlaresManifest specification](/Users/pengpeng/Olares/docs/developer/develop/package/manifest.md)
  - [Framework Market](/Users/pengpeng/Olares/framework/market/README.md)
  - [Shared apps and LLM engine bases](/Users/pengpeng/Olares/docs/zh/manual/olares/market/shared-apps.md)

## 类比边界

- `Android-inspired` 指多层应用操作系统的角色划分：Application Framework → System Apps → third-party apps；不表示可运行 Android APK。
- `AWS equivalent capabilities` 指能力类别可对照，不表示 Olares 复刻 AWS 产品、兼容其 API，或具备相同规模与 SLA。
- ChatGPT、Midjourney、Google Photos、Dropbox / Google Drive、Notion、Home Assistant Cloud 等只用于说明已被 SaaS / AI 验证的工作负载类别。
- `Open source` 是贯穿五层的系统属性，不是第六层；第三方组件仍分别遵循其自身许可证。

## 逐字稿中的 NAS 安全表述

可以对外使用：

- Olares 的定位是个人云操作系统，而传统 NAS 首先解决网络存储与磁盘可靠性。
- Olares 把应用生命周期、权限、网络入口、平台服务和加速资源纳入统一系统。
- Olares 可以挂载现有 SMB / NFS 存储，因此可以与 NAS 共存，而非要求 OEM 放弃现有存储能力。
- 上述内容只进入逐字稿，不进入本页主画面。

避免使用：

- “传统 NAS 没有容器、虚拟机或远程访问。”
- “所有 NAS 第三方应用都以 root 运行。”
- “Olares 单节点具备与 RAID 相同的磁盘故障保护。”
- “Olares 所有 AI / Agent 平台能力均已完整产品化。”

参考比较：

- [Compare Olares and NAS](https://blog.olares.com/compare-olares-and-nas/)
- [Olares 产品与品牌口径](/Users/pengpeng/seo/basic/olares.md)

## 英文措辞

- 使用：`Olares is an open-source, multi-layer personal cloud operating system.`
- 不使用：`Olares is an open-sourced, multi-layered operating system.`
- `open-source` 是形容词；`open-sourced` 容易被理解为“后来才开放源码”。
