# Slide 17 逐字稿 · Olares 五层架构

这一页先不比较具体功能，而是解释 Olares 到底是什么。

Olares 是一个开源、五层的个人云操作系统。它和 Android 一样，采用多层架构，把硬件资源、平台服务、应用框架、系统应用和第三方应用连接成一个整体。但它不是 Android，也不运行 Android 应用：Android 是我们理解上三层架构角色的参照；下两层则采用云原生架构，在用户自己的硬件上提供一套 local PaaS 和 IaaS。

我们从最底层开始。

第一层是 Infrastructure，可以把它理解为运行在本地硬件上的 IaaS。AWS 用 EC2、EKS、VPC、EBS 和 GPU instances 提供计算、集群、网络、存储和加速资源；Olares 使用 K3s 或 Kubernetes、containerd、Calico、CoreDNS、MinIO、HAMi、olaresd 和 olares-cli，在用户自己的设备上完成对应的资源编排。

第二层是 Platform，也就是 local PaaS。AWS 上，应用会调用 RDS、ElastiCache、SQS、S3、CloudWatch 和 AWS Backup；Olares 则提供 PostgreSQL、KVRocks、NATS、JuiceFS、Prometheus、Velero 和 TAPR。这样，应用不需要各自重复搭建数据库、消息、文件、备份和可观测系统。

第三层是 Framework。从这里开始，结构更接近 Android 的开放应用操作系统。Android Application Framework 统一处理应用权限、生命周期和系统服务；Olares Framework 承担相似的架构角色。应用通过 OlaresManifest 声明计算资源、存储、网络入口、权限和中间件依赖，系统再负责安装、升级、隔离、身份认证、SSO、路由与跨应用调用。这里对标的是能力边界，不代表兼容 Android API，也不代表复刻 AWS IAM、Cognito 或 API Gateway。

第四层是 Built-in apps，对应 Android System Apps 的角色。Desktop、Files、Market、Settings、Dashboard、Control Hub、Vault、Wise 和 Studio，把文件、密码、知识、系统管理、监控和应用开发做成开箱即用的用户体验。

第五层是 Community apps，对应 Android 第三方应用和应用分发生态的角色。聊天与模型服务、生成式图像、照片管理、文件同步、协作和智能家居等已经被 SaaS 与 AI 市场验证的工作负载，可以通过 Olares Application Chart 进入 Olares Market。用户看到的是安装一个应用，底层则继续由同一套 Framework、PaaS 和 IaaS 治理。

Open source 不是额外的第六层，而是贯穿全部五层的属性。Olares 核心仓库采用 AGPL-3.0；各层使用的第三方组件继续遵循各自的开源许可证。

这套五层架构，最终作为一套一站式产品交付给用户，也就是右栏这几件东西：Olares OS 就是左侧的整套系统；Clients 提供桌面、移动端和浏览器扩展的访问入口；Olares Space 负责域名、网络、远程访问和备份；Olares Market 让 200+ 应用一键安装；Olares CLI & Skills 则让用户用自然语言配合 agent 管理整个系统。左边讲的是"怎么构成"，右边就是用户实际拿到手的"交付物"。

回到传统 NAS。NAS 最擅长的是磁盘、卷、RAID 和网络共享；今天很多 NAS 也提供容器、虚拟机、远程访问和应用中心。但这些能力通常仍然围绕存储主线展开，应用权限、网络入口、数据库、中间件、GPU 和生命周期管理往往需要用户或 OEM 继续集成。Olares 不是否定 NAS 的存储价值，而是在保留现有硬件与存储能力的基础上，把这些分散能力提升为一套统一的应用操作系统。

这也是 Olares 与 Intel 合作的价值：同一套开源、多层 OS，可以把不同形态的 Intel 设备变成用户拥有的个人云、应用平台与本地 AI 运行环境。硬件不再只提供容量和算力，而是直接承载可安装、可治理、可持续扩展的应用与 Personal Agent 生态。
