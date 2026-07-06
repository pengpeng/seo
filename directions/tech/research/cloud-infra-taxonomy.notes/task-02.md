---
task_id: 02
role: 云原生存储分析师
status: complete
sources_found: 5
---

## Sources
[14] MinIO — GitHub 仓库 README | https://github.com/minio/minio | Source-Type: official | As Of: 2026 | Authority: 8/10
[10] CNCF — Longhorn project page | https://www.cncf.io/projects/longhorn/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[11] CNCF — Velero project page | https://www.cncf.io/projects/velero/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[18] Chaos and Order — Distributed Storage 2026 Deep Dive | https://www.youngju.dev/blog/culture/2026-05-16-distributed-storage-minio-seaweedfs-ceph-garage-juicefs-openebs-longhorn-rook-2026-deep-dive.en | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 6/10
[19] K8sCalc — K8s Storage 2026: Longhorn vs Rook-Ceph vs OpenEBS | https://www.k8scalc.com/blog/kubernetes-storage-deep-dive | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[5] Google Cloud — 三云服务对照表 | https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison | Source-Type: official | As Of: 2024-12 | Authority: 9/10

## Findings
- MinIO 是单二进制、S3 兼容对象存储（AGPLv3），已成 S3 协议事实参考实现；社区版现仅以源码分发。[14][18]
- Ceph（经 Rook operator 上 K8s）提供对象(RGW)/块(RBD)/文件(CephFS)统一存储；Rook 是 CNCF Graduated。[18][19]
- Longhorn 2019 入 CNCF、2021-11-04 升 Incubating（非 Graduated），是 K8s 原生分布式块存储，内建 S3/NFS 备份与 UI。[10][19]
- OpenEBS 提供容器原生块存储（LocalPV 最快、Mayastor 走 NVMe-oF/SPDK 高性能）。[19]
- JuiceFS 是 POSIX 兼容分布式文件系统，以对象存储为数据后端，适合 ML 数据集共享。[18]
- Velero 2026-03-11 才进 CNCF Sandbox（Broadcom 捐赠），是 K8s 应用与 PV 的备份/迁移工具。[11]
- 对象存储：AWS S3 / Azure Blob Storage / Google Cloud Storage；块：EBS / Managed Disks / Hyperdisk(Persistent Disk)；文件：EFS / Azure Files / Filestore；备份：AWS Backup / Azure Backup / GCP Backup and DR。[5]

## Deep Read Notes
### Source [18]: 分布式存储 2026 深评
Key data: 首个自建 S3 后端→MinIO；对象+块+文件统一→Ceph+Rook；ML 数据集→JuiceFS(POSIX over S3)；K8s 通用有状态→Longhorn。
Key insight: MinIO 已成 S3 参考实现，"same code everywhere"（K8s/裸机/树莓派）。
Useful for: 存储大类开源 top + 解读。

## Gaps
- MinIO 主仓库 README 标注社区版停发预编译二进制、转向源码——长期开源姿态存疑（相反主张：MinIO 商业化可能削弱其"开源默认"地位）。
- Restic 未见独立权威页确认（Olares 内置备份用 Restic），本轮以官方组件清单为准，未反向核验其 star/采用度。

## END
