---
task_id: 02
role: 存储系统与 OLTP 数据库中间件分析师
status: complete
sources_found: 28
---

## Sources
[1] What Survived MinIO: The Post-Archive S3 Server Landscape, May 2026 | LLMS3 | https://llms3.com/blog/what-survived-minio-may-2026 | Source-Type: 独立博客/榜单 | As Of: 2026-05 | Authority: 5/10
[2] The Post-MinIO Landscape — Self-Hosted S3 Branches Out | LLMS3 | https://llms3.com/guides/the-post-minio-landscape | Source-Type: 独立博客/指南 | As Of: 2026-05 | Authority: 5/10
[3] Distributed Storage 2026 Deep Dive (MinIO/Ceph/JuiceFS/OpenEBS/Longhorn/Rook…) | https://www.youngju.dev/blog/culture/2026-05-16-distributed-storage-minio-seaweedfs-ceph-garage-juicefs-openebs-longhorn-rook-2026-deep-dive.en | Source-Type: 长文对比博客 | As Of: 2026-05 | Authority: 6/10
[4] Storage Comparison — Ceph vs MinIO vs Longhorn | https://kb.ekarisky.com/storage/comparisons/storage-comparison/ | Source-Type: 个人知识库 | As Of: 2026-04 | Authority: 5/10
[5] How to Compare Ceph vs MinIO for Object Storage | https://oneuptime.com/blog/post/2026-03-31-rook-compare-ceph-vs-minio-object-storage/view | Source-Type: 厂商博客 | As Of: 2026-03 | Authority: 5/10
[6] Postgres vs MySQL in 2026 (Viktar Patotski) | https://patotski.com/blog/postgres-vs-mysql/ | Source-Type: 技术博客 | As Of: 2026 | Authority: 6/10
[7] PostgreSQL vs MySQL: Comprehensive Guide (UpCloud) | https://upcloud.com/global/blog/postgresql-vs-mysql-practical-guide-modern-workloads/ | Source-Type: 厂商博客 | As Of: 2026 | Authority: 6/10
[8] Postgres vs MySQL 2026: Independent Decision Guide | https://postgresvsmysql.com/ | Source-Type: 决策指南站 | As Of: 2026 | Authority: 5/10
[9] atryx/postgres-vs-mysql (GitHub) | https://github.com/atryx/postgres-vs-mysql | Source-Type: GitHub repo | As Of: 2026 | Authority: 5/10
[10] MongoDB vs CouchDB: Document DB Comparison (OneUptime) | https://oneuptime.com/blog/post/2026-03-31-mongodb-mongodb-vs-couchdb-document-database-comparison/view | Source-Type: 厂商博客 | As Of: 2026-03 | Authority: 5/10
[11] CouchDB vs MongoDB | Better Stack Community | https://betterstack.com/community/guides/databases/couchdb-vs-mongodb/ | Source-Type: 厂商社区指南 | As Of: 2026 | Authority: 6/10
[12] Redis vs MongoDB (2026) | ZTABS | https://ztabs.co/compare/redis-vs-mongodb | Source-Type: 厂商对比页 | As Of: 2026-04 | Authority: 5/10
[13] MongoDB, CouchDB, PostgreSQL JSON Compared (dasroot) | https://dasroot.net/posts/2026/01/mongodb-couchdb-and-postgresql-json/ | Source-Type: 技术博客 | As Of: 2026-01 | Authority: 5/10
[14] 84+ Key-Value Databases Ranked (1bench.dev) | https://1bench.dev/databases/key-value | Source-Type: 榜单站 | As Of: 2026-06 | Authority: 5/10
[15] Supported Addons | KubeBlocks (官方文档) | https://kubeblocks.io/docs/preview/user_docs/overview/supported-addons | Source-Type: 官方文档 | As Of: 2026 | Authority: 9/10
[16] apecloud/kubeblocks README (官方) | https://github.com/apecloud/kubeblocks/blob/main/README.md | Source-Type: 官方 repo | As Of: 2026 | Authority: 9/10
[17] apecloud/kubeblocks-addons (官方) | https://github.com/apecloud/kubeblocks-addons | Source-Type: 官方 repo | As Of: 2026 | Authority: 9/10
[18] juicedata/juicefs (GitHub 官方) | https://github.com/juicedata/juicefs | Source-Type: 官方 repo | As Of: 2026-06 | Authority: 9/10
[19] cubefs/cubefs (GitHub 官方) | https://github.com/cubeFS/cubefs | Source-Type: 官方 repo | As Of: 2026 | Authority: 9/10
[20] CubeFS Graduates from CNCF (InfoQ) | https://www.infoq.com/news/2025/03/cubefs-cncf-graduation/ | Source-Type: 新闻 | As Of: 2025-03 | Authority: 8/10
[21] Redis, Valkey, or Dragonfly: how to decide (FlowVerify) | https://www.flowverify.co/blog/redis-valkey-dragonfly-2026 | Source-Type: 技术博客 | As Of: 2026 | Authority: 6/10
[22] Redis vs Valkey vs Dragonfly 2026 (DevToolsWatch) | https://devtoolswatch.com/en/redis-vs-valkey-vs-dragonfly-2026 | Source-Type: 技术博客 | As Of: 2026 | Authority: 6/10
[23] DragonflyDB v1.38 (Hivebook) | https://www.hivebook.wiki/wiki/dragonflydb-v138-multi-threaded-shared-nothing-redis-compatible-in-memory-store | Source-Type: wiki | As Of: 2026-04 | Authority: 5/10
[24] Licenses | Redis (官方法务页) | https://redis.io/legal/licenses/ | Source-Type: 官方 | As Of: 2026 | Authority: 9/10
[25] apache/kvrocks (GitHub 官方) | https://github.com/apache/kvrocks | Source-Type: 官方 repo | As Of: 2026 | Authority: 9/10
[26] ASF Announces TLP Apache Kvrocks | https://news.apache.org/foundation/entry/the-apache-software-foundation-announces-new-top-level-project-apache-kvrocks | Source-Type: 官方新闻 | As Of: 2023-06 | Authority: 8/10
[27] Vitess | CNCF (官方项目页) | https://www.cncf.io/projects/vitess/ | Source-Type: 官方 | As Of: 2026 | Authority: 9/10
[28] openebs/openebs (GitHub 官方) | https://github.com/openebs/openebs | Source-Type: 官方 repo | As Of: 2026 | Authority: 9/10

## Findings
- JuiceFS 是"对象存储上的 POSIX 文件系统"：数据落 S3 等对象存储、元数据落 Redis/MySQL/TiKV，Apache-2.0，14.1k star，最新 v1.4.0-rc1(2026-06)，最适合 ML 训练数据集共享与大文件读多场景；无 CNCF 归属，公有云无直接托管等价物（可视为 EFS/FSx + S3 组合）。[18][3]
- MinIO 社区版仓库 2026-02 被归档、转向商业版 AIStor，OSS 许可为 AGPLv3（社区另有 pgsty/minio fork 续维），对应公有云为 AWS S3/Azure Blob/GCS；纯对象存储、S3 兼容度与吞吐最佳但已"事实闭源"。[1][2][4]
- Rook 是 CNCF 已毕业(graduated)的 Ceph on Kubernetes Operator，"在 K8s 上跑 Ceph 的标准方式"，读 CephCluster CR 起 OSD/MON/MGR/MDS；代价是继承 Ceph 全部运维复杂度。[3][5]
- Ceph 是统一(块+文件 CephFS+对象 RGW)存储事实标准，LGPL-2.1/3.0，最新 v20.2.x "Tentacle"(2026-04) 加 FastEC 缩小与 MinIO 性能差距；适合有专职存储团队的大规模企业，公有云等价 AWS EBS/S3、IBM Storage Ceph。[4][2]
- Longhorn 是 Kubernetes 原生分布式块存储、Apache-2.0、v1.11.1(2026-04)、由 SUSE/Rancher 维护，最适合 3–20 节点集群的通用有状态负载(数据库)，无原生对象存储；公有云等价 AWS EBS/Azure Disk/GCP PD。[4][3]
- CubeFS 2025-01 从 CNCF 毕业(graduated)，Apache-2.0、5.6k star，云原生分布式文件+对象存储，支持 POSIX/HDFS/S3，管理约 350PB、用于 JD/NetEase/Shopee/OPPO/小米，主打大数据与 AI/LLM。[19][20]
- OpenEBS 是 CNCF Sandbox 级容器附着存储(CAS)，其 Mayastor 引擎用 NVMe-oF+SPDK，是"给数据库用的高性能 K8s PV"首选。[28][3]
- PostgreSQL 主打新项目/复杂查询/JSONB/GIS/扩展生态与开放治理，社区+宽松许可(PostgreSQL License)；水平分片靠 Citus 扩展但工具链更分散，公有云为 AWS RDS/Aurora PostgreSQL、Azure Database for PostgreSQL、GCP Cloud SQL/AlloyDB。[6][7][9]
- Citus 把 PostgreSQL 变成分布式数据库(分布式 join/并行查询)，最适合多租户 SaaS；对应公有云托管为 Azure Cosmos DB for PostgreSQL(原 Hyperscale Citus)。[6][7][9]
- MySQL 8.4 LTS(支持到 2032-04)由 Oracle 双授权(GPLv2/商业)，读多 CRUD/LAMP 生态最强；水平分片经 Vitess 最成熟(YouTube/Slack/Booking 验证)。公有云 AWS RDS/Aurora MySQL、Azure Database for MySQL、GCP Cloud SQL。[6][8][4]
- Vitess 是 CNCF 已毕业(2018 收录、2019-11 毕业)的 MySQL 分片编排层，把多分片抽象成单一逻辑 schema，托管服务代表 PlanetScale；MariaDB 11.x 是 GPLv2、独立治理的 MySQL 开源分支(Wikimedia 大规模使用)。[27][6][8]
- MongoDB 8.0 (SSPL) 是面向服务端高性能的文档库：replica set 主从复制+原生分片+聚合管道，DB-Engines 2026-04 排 #5；公有云 MongoDB Atlas、AWS DocumentDB、Azure Cosmos DB for MongoDB。CouchDB 3.5.x (Apache-2.0) 主打多主复制+HTTP/REST+离线优先(PouchDB 同步)，查询依赖预定义 view，公有云等价 IBM Cloudant。[12][10][11][13]
- Redis：≤7.2 为 BSD-3、7.4–7.8 双授权 RSALv2/SSPLv1、≥8.0 三授权(RSALv2/SSPLv1/AGPLv3)；2024-03 改照催生 Linux Foundation 的 BSD 许可 fork Valkey(AWS/Google/Oracle 支持，已成 ElastiCache/Memorystore 默认引擎)。公有云 AWS ElastiCache、Azure Cache for Redis、GCP Memorystore、Redis Cloud。[24][21][22][14]
- Apache Kvrocks 2023-06 成为 Apache 顶级项目(TLP)，基于 RocksDB、兼容 Redis 协议的分布式磁盘 KV，用磁盘换内存降本扩容；Dragonfly 是从零重写、多线程 shard-per-thread 架构、BSL 1.1(2029-03-01 转 Apache-2.0)，宣称 10–25x 吞吐，托管为 Dragonfly Cloud。[25][26][22][23]
- KubeBlocks 官方收录 35 类引擎(30+ addon)：关系型 mysql/apecloud-mysql/mariadb、postgresql/vanilla-postgresql/orioledb；NoSQL 有 mongodb(含 shard/mongos)、redis(含 8.x)、etcd、zookeeper；但存储层(JuiceFS/Ceph/Rook/Longhorn/CubeFS/OpenEBS)及 Citus/Vitess/CouchDB/KVRocks/Dragonfly 均未见独立 addon。[15][16][17]

## Deep Read Notes
### Source [3]: Distributed Storage 2026 Deep Dive
Key data: Rook=CNCF Graduated；场景推荐表：ML 训练数据集共享→JuiceFS(POSIX over S3)、数据库高性能 PV→OpenEBS Mayastor(NVMe-oF+SPDK)、通用有状态→Longhorn、企业块+文件+对象→Ceph+Rook；预测 OpenEBS/Longhorn/Rook 三者中两者将收敛为单一标准。
Key insight: 存储已按"访问模式"细分——个人/小集群自托管对象存储更适合 Garage/SeaweedFS 而非重量级 Ceph；JuiceFS 的价值在元数据放 Redis/TiKV 从而超越底层对象存储的元数据性能。
Useful for: 支撑"存储系统"分节的选型矩阵与 Olares 个人云"是否需要分布式存储"判断。

### Source [24]: Licenses | Redis (官方)
Key data: 明确列出 Redis ≤7.2=BSD-3；7.4–7.8=RSALv2 或 SSPLv1；≥8.0.0=RSALv2 或 SSPLv1 或 AGPLv3；Redis Stack/各模块(RediSearch/RedisJSON…)历史许可逐版本表。
Key insight: "Redis 是否开源"的答案取决于版本——8.0 起因加入 AGPLv3 才重新含 OSI 认可选项，但 SSPL/RSALv2 仍是 source-available 而非 OSI 开源，这是云厂商坚持用 Valkey 的根因。
Useful for: 支撑 KV/缓存分节的许可争议与"SSPL 是否算真开源"的 Gap。

### Source [17]: apecloud/kubeblocks-addons (官方)
Key data: mongodb addon 覆盖 4.0–8.0 及 shard/mongos 变体；mysql 覆盖 5.7.44–8.4.x 及 mgr/orc 变体；postgresql 覆盖 12–18；redis 覆盖 5.0–8.4；另有 vanilla-postgresql/supabase。
Key insight: KubeBlocks 收录的是"数据库引擎"而非"存储层"——它消费 CSI/PV，因此 Ceph/JuiceFS/Longhorn 等属其底层依赖而非 addon；分片能力靠 apecloud-mysql/mongodb-shard 自带，而非 Vitess/Citus。
Useful for: 支撑每个项目"KubeBlocks 是否支持"结论与报告的收录矩阵。

## Gaps
- Longhorn CNCF 级别存在来源冲突：[4] 与首轮综述称 "Incubating"，而 [3] 称 "Graduated"——需以 CNCF 官网 landscape 核实(本轮未直接取到官方项目页)。
- MinIO"社区版停发预编译二进制/许可争议"为相反主张候选：多篇 2026 文([1][2][4])断言 2026-02 OSS 仓库归档、转 AIStor 商业版，但均为第三方博客，未取到 MinIO 官方声明原文佐证归档时间与范围。
- "SSPL 是否算真开源"存在相反解读：OSI 未承认 SSPL/RSALv2 为开源许可，但 Redis/MongoDB 官方将其表述为"source available / open source options"([24][12])——口径需谨慎。
- 未搜到 KubeBlocks 明确收录 Citus/Vitess/CouchDB/KVRocks/Dragonfly 的证据(推断为"不支持")；也未取到 KubeBlocks 官方对 MariaDB 支持特性(Vscale/Backup 等)的逐项矩阵。
- 个人云(Olares)是否需要分布式存储属开放问题：多数 2026 文([3])建议单机/小集群优先 Longhorn 或轻量对象存储，未见针对"单用户个人云"场景的权威结论。

## END
