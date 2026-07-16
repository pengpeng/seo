# Olares 五层架构

> Intel 合作 PPT 第 17 页。中文 Slide 文案初稿；先完善表格内容，再制作英文版与 HTML。

---

## Slide copy

### 标题

**Olares：一个开源、五层的个人云操作系统**

上三层参考 Android 的开放应用架构；下两层在用户硬件上提供云原生 PaaS 与 IaaS。

### 五层架构

| Olares 层 | 对标能力 / 服务 | 开源与 Olares 自研组件 | 介绍 |
|----------|-----------------|------------------------|------|
| **Community apps** | Android 第三方应用与 Google Play；ChatGPT、Midjourney、Google Photos、Google Drive、Notion 等 SaaS / AI 产品 | LLM engine bases、LobeChat、Dify、ComfyUI、Immich、Nextcloud、Home Assistant；Olares Market 与 Application Charts | 通过统一应用格式承接开放的本地 SaaS 与 AI 生态 |
| **Built-in apps** | Android System Apps；Google Drive / Dropbox、1Password、Pocket / Feedly、云管理控制台与应用商店 | Desktop、Files、Market、Settings、Dashboard、Control Hub、Vault、Wise、Studio | 提供开箱即用的文件、系统管理、监控、知识与开发体验 |
| **Framework** | Android Application Framework、权限与生命周期；AWS IAM / Cognito、API Gateway、App Runner / Elastic Beanstalk | OlaresManifest、app-service、system-server、bfl、Authelia、LLDAP、OPA | 统一治理应用生命周期、权限、身份、网络入口与跨应用调用 |
| **Platform · PaaS** | AWS RDS、ElastiCache、SQS / SNS、S3 / EFS、CloudWatch、AWS Backup | PostgreSQL、KVRocks、NATS、JuiceFS、Prometheus、Restic、Velero、TAPR | 为应用提供可复用的数据、中间件、文件、备份与可观测服务 |
| **Infrastructure · IaaS** | AWS EC2、EKS、VPC、EBS / EFS、GPU instances | K3s / Kubernetes、containerd、Calico、CoreDNS、etcd、Helm、MinIO、HAMi、olaresd、olares-cli | 统一编排计算、存储、网络、节点与加速资源 |

### 收口

**类 Android 的开放应用操作系统 + 开源云原生 PaaS / IaaS，运行在用户自己的硬件上。**

---

## 工作底稿

- 架构图按自下而上展示：Infrastructure → Platform → Framework → Built-in apps → Community apps。
- HTML 视觉稿保持四列表格；通过横向分隔和背景层次区分上三层应用 OS 与下两层云原生底座，不再增加独立的架构参照列。
- `Open source · AGPL-3.0` 是贯穿五层的属性，不单独作为一层。
- Android、SaaS / AI 产品与 AWS 服务均为架构参考或功能类比，不表示 Android 应用兼容、API 兼容或实现相同。
- 本页不呈现 NAS 对比；相关判断只进入逐字稿。
