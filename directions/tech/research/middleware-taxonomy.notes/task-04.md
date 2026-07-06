---
task_id: 04
role: 企业/大数据分析引擎分析师
status: complete
sources_found: 18
---

## Sources
[1] TiDB vs OceanBase 2026 Comparison Guide | https://www.pingcap.com/compare/tidb-vs-oceanbase/ | Source-Type: vendor(PingCAP) | As Of: 2026-01 | Authority: 6/10
[2] Best Distributed SQL Databases 2026 | https://www.pingcap.com/compare/best-distributed-sql-databases/ | Source-Type: vendor(PingCAP) | As Of: 2026-01 | Authority: 6/10
[3] TiDB | https://en.wikipedia.org/wiki/TiDB | Source-Type: reference | As Of: 2025-11 | Authority: 8/10
[4] OceanBase Database Overview | https://oceanbase.github.io/docs/user_manual/quick_starts/en-US/chapter_01_overview_of_the_oceanbase_database/overview | Source-Type: official | As Of: 2026-01 | Authority: 9/10
[5] OceanBase Open-Sources seekdb (Apache 2.0) | https://www.prnewswire.com/apac/news-releases/oceanbase-unveils-and-open-sources-ai-native-database-seekdb-at-2025-annual-conference-302618360.html | Source-Type: press-release | As Of: 2025-11 | Authority: 6/10
[6] ClickHouse vs Doris vs StarRocks: OLAP ADR 2026 | https://iotdigitaltwinplm.com/clickhouse-vs-doris-vs-starrocks-olap-adr-2026/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[7] ClickHouse vs StarRocks for OLAP Workloads | https://oneuptime.com/blog/post/2026-03-31-clickhouse-vs-starrocks-olap-workloads/view | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 6/10
[8] ClickHouse vs Apache Doris for Real-Time Analytics | https://oneuptime.com/blog/post/2026-03-31-clickhouse-clickhouse-vs-apache-doris-for-real-time-analytics/view | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 6/10
[9] Trino vs. Presto: Which to Use in 2026 | https://www.ksolves.com/blog/big-data/trino-vs-presto | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[10] Trino vs Presto vs Apache Spark 2026 | https://iotdigitaltwinplm.com/trino-vs-presto-vs-apache-spark-lakehouse-query-engines-2026/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[11] Impala vs Trino | https://medium.com/@pulumatirambabu/impala-vs-trino-choosing-the-right-distributed-sql-engine-for-big-data-6dc03f6a3679 | Source-Type: community | As Of: 2025-10 | Authority: 5/10
[12] Hive vs Impala vs Presto (SQL-on-Hadoop) | https://projectsbasedlearning.com/bigdata-hadoop/comparing-sql-on-hadoop-technologies-hive-vs-impala-vs-presto-for-big-data-analytics/ | Source-Type: community | As Of: 2025-09 | Authority: 5/10
[13] Deploying Single-Node ClickHouse on Small Servers | https://altinity.com/blog/deploying-single-node-clickhouse-on-small-servers | Source-Type: vendor(Altinity) | As Of: 2026-02 | Authority: 8/10
[14] Configure ClickHouse for Low Memory Environments | https://pulse.support/kb/clickhouse-low-memory-configuration | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[15] Best ClickHouse alternatives in 2026 (DuckDB/chDB) | https://www.tinybird.co/blog/clickhouse-alternatives | Source-Type: vendor(Tinybird) | As Of: 2026-04 | Authority: 6/10
[16] apecloud/kubeblocks README | https://github.com/apecloud/kubeblocks/blob/main/README.md | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[17] Supported Addons | KubeBlocks Docs | https://kubeblocks.io/docs/preview/user_docs/overview/supported-addons | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[18] KubeBlocks Discussion #7464 (no Presto/Trino support) | https://github.com/apecloud/kubeblocks/discussions/7464 | Source-Type: official | As Of: 2024-06 | Authority: 7/10

## Findings
- 分布式 SQL（NewSQL）三家核心均为开源、横向扩展、强一致：TiDB（PingCAP，MySQL 兼容，Raft，HTAP，Apache 2.0，Go/Rust，2017 首发，稳定版 8.5.4/2025-11），公有云替代 Amazon Aurora DSQL / Google Cloud Spanner。[1][2][3]
- OceanBase 社区版走 MulanPubL-2.0（非 Apache 2.0；只有其新 AI-native 库 seekdb 从第一天起 Apache 2.0），C++ 编写，Paxos 三副本、MySQL+Oracle 双兼容，定位金融级极高并发 OLTP / 替 Oracle。[4][5]
- PolarDB-X（阿里云开源社区版）为 MySQL 兼容、存算分离的分布式 SQL，Apache 2.0，KubeBlocks 收录为 `polardb-x` addon。[17]
- 选型判据：替 Oracle/金融级 OLTP 选 OceanBase；要自动分片+HTAP+云原生 K8s 运维选 TiDB；三家 + CockroachDB 的二级索引写基准结果因分区/并发/索引类型而异，官方数字需自测。[1]
- OLAP 数仓三家（ClickHouse / Apache Doris / StarRocks）核心层均列式、向量化、Apache 2.0，上层叠加商业云；StarRocks 由早期 Doris 血统 fork 后重写查询引擎（Linux 基金会），Doris 为 ASF 顶级项目。[6]
- ClickHouse 单进程二进制、shared-nothing、MergeTree，强在高基数单表扫描与写入吞吐、压缩、运维简单；弱在多表 JOIN 与频繁 upsert（靠 ReplacingMergeTree + FINAL，合并前可能读到重复）。[6][7][8]
- Doris / StarRocks 为 FE(前端规划)+BE(后端执行) MPP + CBO 架构，主键模型支持真正 upsert/delete，强在多表 JOIN、高并发用户面分析、物化视图透明改写；代价是多节点、需管 tablet/副本，运维更重。[6][7]
- 作者定性加权矩阵（1-5，满分155）：ClickHouse 122、Doris 122、StarRocks 132——StarRocks 综合领先在 JOIN/upsert/并发，ClickHouse 领先在单表扫描/写入吞吐/运维简单/生态。[6]
- 分布式 SQL 查询引擎（联邦/数据湖）：Trino（Trino 软件基金会，原 PrestoSQL）连接器最广（Hive/Iceberg/Delta/Hudi/PG/MySQL/ES/Kafka 等 30+）、开放治理、迭代最快，是 2026 联邦/湖仓查询默认首选。[9][10]
- Presto（Meta 维护的 PrestoDB）稳定、商业支持路径清晰，但纯 OLAP 略慢于 Trino、Iceberg 特性落后 6-12 个月；新项目普遍推荐 Trino。[9][10]
- Impala（Cloudera）MPP、绕过 MapReduce，强在 HDFS/Hive/Kudu 低延迟 BI，适合 on-prem Hadoop 生态；Hive（2008，HiveQL 编译成 MapReduce/Tez/Spark）如今主要用于重批量 ETL，延迟高。[11][12]
- 这四个查询引擎本身不存数据、需要外部 Hive Metastore / 数据湖 / 多数据源，本质是"大数据平台上的查询层"，与个人云单机就近分析的需求错位。[10][11][12]
- KubeBlocks 收录数仓 ClickHouse、Doris(starrocks-ce/doris)、StarRocks、ElasticSearch/OpenSearch，以及分布式 SQL 的 tidb、oceanbase-ce、polardb-x；但明确不支持 Presto/Trino 这类跨库查询引擎（官方回复：可改用 Doris/StarRocks 同步数据后查询）。[16][17][18]
- 个人云资源画像：ClickHouse 单节点可跑但"非轻量"，实用地板约 4 核 8GB SSD（4GB 勉强启动、2GB 仅能 boot），低内存需大量调优（mark/uncompressed cache、后台合并池、min_bytes_for_wide_part）；纯个人/本地/嵌入式分析的标准平替是 DuckDB（进程内、零基础设施、直查 Parquet），或 chDB（Python 内嵌 ClickHouse）。[13][14][15]

## Deep Read Notes
### Source [6]: ClickHouse vs Doris vs StarRocks OLAP ADR 2026
Key data: 加权矩阵满分155——ClickHouse 122/Doris 122/StarRocks 132；ClickHouse MergeTree 稀疏索引默认 8192 行/granule；三家均已加存算分离(对象存储+BE本地缓存)；显式排除 DuckDB(单机/进程内)、Pinot/Druid(仅追加流)、云数仓(Snowflake/BigQuery/Redshift，按查询开销与成本不合)。
Key insight: 三家 2026 特性清单已趋同，真正差异藏在"各自会退化的工作负载"——单表扫描选 ClickHouse、JOIN/upsert/高并发选 MPP(StarRocks/Doris)；ClickHouse 的 `FINAL` 去重是"upsert 税"。三节点 ClickHouse 一名工程师即可运维，FE/BE MPP 天然更重。
Useful for: 支撑"OLAP 数仓大类"选型/架构/个人云非重点判断整节。

### Source [13]: Deploying Single-Node ClickHouse on Small Servers (Altinity)
Key data: "ClickHouse 不轻量但可调到最小硬件：4+核、8GB+RAM、SSD"；实用地板 8GB(4GB 勉强)；8GB VM 上默认配置数小时即 OOM，元凶是后台 merge 而非查询。
Key insight: 单节点 ClickHouse 对开发/中低负载生产可用，但要在个人云小机器稳定跑需系统调优；这印证"重型引擎里 ClickHouse 单机是唯一个别场景可用的候选"，且需限制。
Useful for: 支撑"个人云适配：ClickHouse 单机个别可用 / DuckDB 更合适"取舍。

### Source [18]: KubeBlocks Discussion #7464
Key data: Maintainer 明确 KubeBlocks 不支持 Presto/Trino 等跨库查询引擎；建议改用 Doris/StarRocks 把数据同步进数仓再查；ClickHouse addon 早在 2024-06 已支持。
Key insight: Olares 的 KubeBlocks 中间件层天然覆盖数仓/NewSQL 引擎，但联邦查询引擎(Trino/Presto/Impala/Hive)不在其托管范围——从平台能力上也印证这类引擎属"企业·大数据，个人云非重点"。
Useful for: 支撑 KubeBlocks 收录矩阵 + 查询引擎排除结论。

## Gaps
- 取舍结论：分布式 SQL（TiDB/OceanBase/PolarDB-X）与 MPP 数仓（Doris/StarRocks）默认三副本/多节点、面向企业级横扩与高并发，个人云单机/小集群基本用不上，应归"企业·大数据，个人云非重点"；联邦查询引擎（Trino/Presto/Impala/Hive）依赖外部湖/Metastore/多源，个人云更无场景，且 KubeBlocks 亦不托管。唯一个别可用窗口＝ClickHouse 单机（8GB+ 调优）做本地日志/时序分析，但对个人 Personal Agent 更推荐 DuckDB/chDB 这类零基础设施嵌入式方案。
- 相反主张候选：ClickHouse 单机"也很能打"——Altinity 称单台配好的服务器能扛传统库跪掉的负载[13]，且个人数据分析未必用不上 OLAP（本地 Parquet/日志/时序聚合 DuckDB 常与 ClickHouse 单机性能相当甚至更快[15]），说明"OLAP 完全不适合个人云"这一简单结论需被"轻量单机 OLAP 有真实个人场景"修正。
- 未找到：TiDB/OceanBase/PolarDB-X 与 Doris/StarRocks 在"真正单节点最小可运行内存"的官方硬性下限对照数据（多为集群推荐值），个人云可行性仍靠架构推断而非厂商实测。

## END
