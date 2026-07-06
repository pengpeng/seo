---
task_id: 05
role: 可观测/评估 + 模型仓库 + AI-infra landscape 分析师
status: complete
sources_found: 13
---

## Sources
[1] Langfuse vs LangSmith vs Phoenix vs Braintrust (dev.to, Anhaia) | https://dev.to/gabrielanhaia/langfuse-vs-langsmith-vs-phoenix-vs-braintrust-the-honest-2026-comparison-253p | Source-Type: community | As Of: 2026-04 | Authority: 5/10
[2] AI Observability 2026 (web3aiblog) | https://www.web3aiblog.com/blog/ai-observability-platforms-compared-langsmith-langfuse-braintrust-helicone-phoenix-june-2026 | Source-Type: secondary-industry | As Of: 2026-06 | Authority: 4/10
[3] LLM Observability 10-way comparison (SideGuy) | https://www.sideguysolutions.com/shareables/llm-observability-software-10-way-comparison-2026-langfuse-langsmith-braintrust-arize-phoenix-helicone-weave-whylabs-datadog-newrelic-traceloop.html | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[4] Best LLM Observability Tools 2026 (tinyctl.dev) | https://tinyctl.dev/roundups/llm-observability-tools/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 5/10
[5] Langfuse vs LangSmith (Langfuse 官方) | https://langfuse.com/resources/engineering/langsmith-alternative | Source-Type: official | As Of: 2026 | Authority: 7/10
[6] The Enterprise AI Stack in 2026 (RIVER Group) | https://rivergroup.ai/insights/the-enterprise-ai-stack-2026 | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[7] The AI Agents Stack 2026 Edition (O'Reilly) | https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 8/10
[8] The AI Infrastructure Stack 2026 Edition (TURION.AI) | https://turion.ai/blog/ai-infrastructure-stack-2026-edition/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[9] The Data + AI Stack Explained (Medium, Krishna) | https://medium.com/@codebykrishna/the-data-ai-stack-explained-e3c6032380f1 | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 4/10
[10] Memory in AI: MCP, A2A & Agent Context Protocols (Orca Security) | https://orca.security/resources/blog/bringing-memory-to-ai-mcp-a2a-agent-context-protocols/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[11] Ollama Model Management & Registry Protocol (Read OSS) | https://readoss.com/en/ollama/ollama/model-management-storage-conversion-registry-protocol | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[12] Building a Private Ollama Model Registry (Markaicode) | https://markaicode.com/build-private-ollama-model-registry/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 4/10
[13] Running LLMs Locally Using Ollama (CODE Magazine) | https://www.codemag.com/Article/264031/Running-Large-Language-Models-Locally-Using-Ollama | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10

## Findings
- Langfuse（MIT，2026-01 起被 ClickHouse 收购）是自托管 LLM 可观测/评估的开源事实默认：框架无关、基于 OpenTelemetry、含 tracing+prompt 管理+评估，可完全气隙自托管、无 trace 保留上限。[1][2][5]
- Arize Phoenix（Apache-2.0，基于 OpenInference/OTel）是评估深度与 RAG/agent 诊断最强的开源替代，多步 agent trace/工具调用图视图最细，是 Arize AX 商业版的开源面。[1][3]
- 公有云/闭源对标叫法：LangSmith（LangChain 官方托管，闭源 SaaS，深度绑 LangChain/LangGraph）、Braintrust（闭源，evals-in-CI 专精、部署阻断质量门）、Helicone（一行代理最快接入）、W&B Weave、Datadog/New Relic LLM 模块。[1][2][3]
- greenfield 团队最小后悔默认＝Langfuse 自托管；若 CI 文化要"每个 PR 跑全量 eval"再加 Braintrust。[1]
- AI-infra 2026 已从"消费模型"收敛为分层生产栈；多份 landscape 用 5-6 层：TURION.AI＝Compute/Serving/Orchestration/Data/Observability/Gateway 六层。[8]
- RIVER Group 企业栈五层＝Infrastructure/Data/Intelligence/Orchestration/Governance；并指出"推理已与训练分离，多数企业只跑推理不训练"。[6]
- O'Reilly Agent 栈六层，2026 新增三类此前不存在的独立类别：MCP 协议/工具层、记忆(memory)作为一等公民、eval——"agent 栈≠LLM 栈"。[7]
- 新增 AI-infra 类别（超出 10 个必覆盖子类）：①特征存储 Feature Store（Feast 开源 vs Tecton/Databricks Feature Store，解决 train-serve skew）②数据/工作流管道（Airflow/Dagster/Prefect/Temporal）③知识图谱 GraphRAG（Neo4j/Memgraph/Dgraph 开源，对标 Amazon Neptune）④Guardrails 安全护栏（PII 脱敏/注入检测，2026 已并入网关层，非独立产品）⑤记忆/上下文栈（向量+全文+图+KV Redis+事件日志分层）⑥MCP/A2A 协议层。[6][7][8][9][10]
- 向量库市场 2025 约 $32 亿、年增 24%；2026 共识：pgvector+pgvectorscale 在 <5000 万向量已生产可用，专用库只在更大规模才"挣得位置"。[9][8]
- 模型仓库/权重分发：Hugging Face Hub 是公有中心（默认下载缓存 `~/.cache/huggingface/hub/`）；Ollama 用内容寻址、OCI 兼容协议（blobs+manifests、SHA256 去重、CDN 分块下载），可自建私有 registry（Docker Distribution v2 / Harbor）实现本地权重分发与数据驻留。[11][12][13]
- Ollama 亦支持直接跑 HF 上的 GGUF 模型，本地 registry 与 HF Hub 形成"公有中心 + 私有分发"两层。[13]

## Deep Read Notes
### Source [7]: O'Reilly The AI Agents Stack 2026
Key data: 六层栈；MCP 标准化工具连接（整个 tools 层因它而新生）；memory 成一等公民（episodic 向量库 / semantic 知识图谱 / operational KV）；pgvector 成"不需专用库时的默认"。
Key insight: "agent 需要跨多步状态管理、协议化工具访问、跨会话记忆、护栏"——这是与 chatbot(仅需推理+RAG) 根本不同的基建问题，正对 Olares 的 Personal Agent 用例。
Useful for: 报告"新增类别"+关键发现（Olares agent-native 叙事）。

### Source [11]: Read OSS Ollama registry protocol
Key data: `ollama pull` 走 OCI 镜像规范；Layer=SHA256 digest 作内容地址+文件名；共享底座权重的模型自动去重；push 采 manifest-last 保证原子可见。
Key insight: 本地模型分发已工程化成"Docker for models"，自建 registry 即可完全脱离外部依赖、合规数据驻留。
Useful for: 模型仓库子类 + Olares 本地 registry 平替论证。

## Gaps
- HF Hub 官方文档未直接取源（用 Ollama/HF 缓存路径的二手描述），HF 作为"公有中心"是常识性事实，置信度仍高但标注来源为二手。
- Feature Store/GraphRAG/Guardrails/Memory 为增补类别，各只有 landscape 综述级来源，未逐一深挖开源 top 产品的 star/性能，报告中作"扩展类别"低置信呈现。
- 相反主张候选：并非所有团队都需要 6 层全栈——RIVER 指出多数企业只跑推理、不训练，重训练/微调/特征存储层对纯推理个人用户可能过重；Olares 个人云无需企业级 Governance/Feature Store 全套。[6]

## END
