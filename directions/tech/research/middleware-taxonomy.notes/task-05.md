---
task_id: 05
role: 消息队列与流处理中间件分析师
status: complete
sources_found: 17
---

## Sources
[1] Kafka vs RabbitMQ vs NATS 2026 | pdpspectra | https://pdpspectra.com/blog/kafka-rabbitmq-nats-2026/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[2] Message Queue — Kafka, RabbitMQ, NATS, SQS, Pulsar | Systems Explained | https://systeminternals.dev/system-design/message-queue/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[3] Kafka vs RabbitMQ vs NATS vs SQS | BackendBytes | https://backendbytes.com/articles/message-queue-comparison/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[4] Kafka Streams vs Apache Flink vs Apache Storm | DesignGurus | https://www.designgurus.io/blog/kafka-streams-apache-flink-apache-storm | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[5] Kafka vs Flink vs Spark Streaming: What Nobody Tells You | Medium (Körükcü) | https://alper-korukcu.medium.com/kafka-vs-flink-vs-spark-streaming-what-nobody-tells-you-before-you-pick-one-aa83c26a287a | Source-Type: community | As Of: 2026-01 | Authority: 5/10
[6] Spark Streaming vs Apache Flink | Confluent | https://www.confluent.io/compare/spark-streaming-vs-flink/ | Source-Type: vendor | As Of: 2026-01 | Authority: 7/10
[7] Flink vs Kafka Streams vs Spark Structured Streaming | Onehouse | https://www.onehouse.ai/blog/apache-spark-structured-streaming-vs-apache-flink-vs-apache-kafka-streams-comparing-stream-processing-engines | Source-Type: vendor | As Of: 2026-01 | Authority: 7/10
[8] JetStream | NATS Docs | https://docs.nats.io/nats-concepts/jetstream | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[9] NATS.io and JetStream: Cloud-Native Messaging Explained | cloudrps | https://cloudrps.com/blog/nats-messaging-jetstream-explained/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[10] NATS JetStream vs Kafka | timderzhavets | https://timderzhavets.com/blog/nats-jetstream-vs-kafka-choosing-the-right-persistent/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[11] Amazon MSK (Managed Streaming for Apache Kafka) | AWS | https://aws.amazon.com/msk/ | Source-Type: official | As Of: 2026-06 | Authority: 8/10
[12] Messaging Services Comparison | CloudToolStack | https://cloudtoolstack.com/learn/multi-cloud-messaging-comparison | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 7/10
[13] Supported Addons | KubeBlocks | https://kubeblocks.io/docs/preview/user_docs/overview/supported-addons | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[14] apecloud/kubeblocks-addons | GitHub | https://github.com/apecloud/kubeblocks-addons | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[15] Strimzi | CNCF | https://www.cncf.io/projects/strimzi/ | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[16] NATS Graduation Application (Issue #2042) | cncf/toc GitHub | https://github.com/cncf/toc/issues/2042 | Source-Type: official | As Of: 2026-02 | Authority: 9/10
[17] What is Pub/Sub? | Google Cloud Docs | https://docs.cloud.google.com/pubsub/docs/overview | Source-Type: official | As Of: 2026-06 | Authority: 8/10

## Findings
- Apache Kafka=分区式持久提交日志，事件流/日志聚合/CDC 的事实标准；4.0(2025-03) 彻底移除 ZooKeeper，KRaft 成唯一协调方式；调优后单 broker ~1M msg/s，运维中等偏重（分区/rebalance/heap 调优）；许可 Apache-2.0，属 ASF 顶级项目而非 CNCF。[1][2][3]
- Strimzi 是 Kafka on K8s 的事实标准 operator（滚动重启/扩容/topic 再平衡/TLS 轮换），Red Hat 2017 起、2019-08 入 CNCF Sandbox、2024-02-08 升 Incubating；CNCF 页面 ~768 stars、健康分 85。[3][15]
- RabbitMQ=成熟 AMQP 消息代理，擅长任务队列/竞争消费者/复杂路由(exchange/binding)/RPC，中等吞吐(~50K msg/s/节点)，运维比 Kafka 轻；3.9 起加 Streams、4.x 用 quorum queue 默认提升持久性；许可 MPL-2.0。[1][2][3]
- NATS=Go 写的极轻量单二进制，pub/sub+request/reply+streaming(JetStream) 一体，核心亚毫秒延迟、非持久核心可达 ~10M msg/s；JetStream(NATS 2.2 引入)用 Raft 加持久化/重放/consumer group；三节点 JetStream 集群每节点 <256MB RAM。[1][2][8][9]
- NATS 属 CNCF：2018-03-15 入孵化，2026-02 提交毕业申请、TOC 审核中(pending)——即 AS_OF 仍为 Incubating（部分博客称"graduated"不准确）。[16][9]
- Apache Pulsar=计算(broker)与存储(BookKeeper bookies)分离的分布式消息+流平台，原生多租户/跨地域复制/分层存储，适合多租户 SaaS/PaaS，但组件多(broker+bookie+ZooKeeper)、运维重；许可 Apache-2.0，ASF 顶级项目。[1][2][3]
- Apache Storm=最早的逐元组(record-at-a-time)流处理器，已被 Flink/Spark 取代，2026 属 legacy，仅在已有 Storm 拓扑时保留；语义历史上 at-least-once(需 Trident/幂等 sink)。[4][5]
- Apache Spark Structured Streaming=构建在 Spark SQL 上的 micro-batch 引擎，批流统一、复用 MLlib/Delta/DataFrame 生态；延迟下限较高(生产约 100ms–数秒)，适合批量重、可容忍秒级延迟的分析型 ETL。[4][5][6][7]
- Apache Flink=原生 event-at-a-time 流引擎，事件时间+watermark+增量 checkpoint，稳定 sub-100ms 延迟、TB 级状态、exactly-once，适合欺诈检测/CEP/实时告警；Netflix 跑 15,000+ Flink 作业，Uber 由 Spark 迁 Flink。[4][5][6][7]
- KubeBlocks 消息队列类 addon 收录 kafka / rabbitmq / pulsar 三者(统一 CRD 管生命周期与 day-2)；Kafka 支持 2.7–3.9(KRaft combine/broker/controller 组件)、RabbitMQ 支持 3.8–4.2、Pulsar 支持 2.11/3.0/4.0.6(broker+bookkeeper+zookeeper+proxy)。KubeBlocks 未收录 NATS/Flink/Spark/Storm。[13][14]
- 公有云托管替代：Kafka→AWS MSK / Azure Event Hubs(Kafka 兼容端点) / GCP 用 Confluent；流数据→AWS Kinesis Data Streams / Azure Event Hubs / GCP Pub/Sub；队列→AWS SQS / Azure Service Bus / GCP Pub/Sub；流处理→AWS Managed Service for Apache Flink(原 Kinesis Analytics) / Azure Stream Analytics / GCP Dataflow(Apache Beam)。[11][12][17]
- 资源占用谱系(个人云关键):NATS/JetStream 单二进制 <256MB/节点最轻→RabbitMQ 中等→Kafka(KRaft 后省掉 ZK 但仍需 broker+分区调优)偏重→Pulsar(broker+bookie+ZK 多组件)最重；三节点自托管月成本 NATS ~$300–800 < RabbitMQ ~$500–1500 < Kafka ~$1500–5000。[3][10]
- Olares 平台层已内置 NATS 作为消息队列中间件（见 task-01），与"个人云优先轻量"取向一致；Kafka/Pulsar/流处理引擎均非个人云默认负载。[3][8]

## Deep Read Notes
### Source [8]: JetStream | NATS Docs (全文)
Key data: JetStream 内建于 nats-server 二进制；用"NATS 优化的 Raft"做分布式仲裁，达到即时一致性(非最终一致)；支持 queueing(消费即走)与 streaming(按需重放)两种 QoS；retention 策略 limits/work-queue/interest；delivery 语义 at-most-once/at-least-once/(受限)exactly-once；无第三方依赖、自愈、水平扩展。
Key insight: JetStream 把"消息总线+持久层"合一——一个二进制、一套 subject 模型、一条连接即可从 fire-and-forget 平滑升到持久可重放流，这正是个人云"最小运维面"诉求的技术根据。
Useful for: 支撑"NATS/JetStream 定位＋为何 Olares 选它作内置 MQ"小节。

### Source [3]: Kafka vs RabbitMQ vs NATS vs SQS | BackendBytes (全文)
Key data: 运维复杂度 Kafka 中(仅 KRaft，4.0 移除 ZooKeeper)>RabbitMQ 中>NATS 低>SQS 无;三节点自托管月成本 Kafka $1500–5000 / RabbitMQ $500–1500 / NATS $300–800;工作负载映射表(有序可重放流→Kafka;更简单流→NATS JetStream;竞争消费任务队列→RabbitMQ;RPC→NATS)。
Key insight: 明确"Kafka 的运维复杂度只有高吞吐或重放需求才划算，简单任务派发用 RabbitMQ/SQS"——是"Kafka 对单机/个人云过重"这一反方主张的直接依据。
Useful for: 支撑资源占用/成本谱系与"何时选哪个"决策表。

### Source [13]: Supported Addons | KubeBlocks (全文)
Key data: Message Queues 分类只列 kafka/rabbitmq/pulsar；v0.9.0 特性矩阵 kafka 3.3.2、rabbitmq 3.8.14–3.13.2(带 Expose/Failover/Switchover)、pulsar 2.11.2/3.0.2；addons 仓库另示 kafka 到 3.9.0、rabbitmq 到 4.2.1、pulsar 到 4.0.6。
Key insight: KubeBlocks 只把三大"重"MQ 纳入统一 operator，轻量 NATS 与所有流处理引擎(Flink/Spark/Storm)都不在其托管范围——印证 KubeBlocks 面向企业级有状态引擎、与个人云内置 NATS 是两条路线。
Useful for: 支撑"KubeBlocks 是否支持"逐项判定与 Olares 平替对照。

## Gaps
- 相反主张：个人云/单机是否真需要流处理引擎——Flink/Spark/Storm/Pulsar 均为集群级、面向 TB 级状态与多租户，homelab/单机语境几乎无实际负载证据；未搜到"个人云跑 Flink/Kafka"的第三方实测或成功案例。
- 相反主张(NATS 状态歧义)：cloudrps[9] 称 NATS 为 CNCF "graduated project"，但 CNCF TOC 官方 issue[16] 显示截至 2026-02 仍是 Incubating、毕业申请审核中；若审核在 AS_OF 前通过则表述需更新，未搜到 2026-07 前已正式毕业的确认公告。
- 未找到 KubeBlocks 是否有 NATS addon 的明确"否定"官方声明(仅其分类表未列出，属间接推断)。

## END
