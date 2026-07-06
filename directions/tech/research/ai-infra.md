# AI 时代基础设施栈（AI Infrastructure）分类调研

> 研究日期: 2026-07-05 | 来源数: 41 | 字数: ~3600 | 模式: Standard | AS_OF: 2026-07-05 | 官方源占比: 32%

## 摘要

到 2026 年，AI 基础设施已从"调一个模型 API"收敛为一套**分层、可自托管**的生产栈——多份 landscape 用 5-6 层描述它（TURION.AI 六层：Compute / Serving / Orchestration / Data / Observability / Gateway [37]；RIVER 企业五层：Infrastructure / Data / Intelligence / Orchestration / Governance，并指出"推理已与训练分离，多数企业只跑推理不训练" [35]；O'Reilly 的 Agent 栈六层，2026 新增 MCP 工具层、记忆、eval 三个此前不存在的一等类别 [36]）。对 Olares（个人云 OS，核心用例=本地跑 Personal Agent）而言，关键结论是：**推理服务、模型网关、GPU 共享、向量库、Embedding、RAG、Agent 编排、可观测、微调、模型仓库这十类，开源侧都已有生产可用的自托管 top 产品，且几乎全部能落到消费级单卡/小集群**；每一类都有一个明确的「公有云托管叫法」作为 `X alternative` / `self-hosted X` 内容的对标锚点。Olares 已内置或 Market 已上架其中大部分（vLLM/SGLang/Ollama/llama.cpp、LiteLLM/Bifrost/TensorZero、HAMi/nvshare、Dify/RAGFlow/AnythingLLM、LLaMA Factory），向量库/Embedding/可观测评估是相对薄弱、值得补的环节。反向证据需记住：Menlo Ventures 数据称开源模型仅占企业 LLM 用量约 11%（2025，较前一年 19% 下降）[6]，即"自托管已成主流"在企业侧并不成立——但这恰是个人云"数据主权 + 一次买断"叙事的差异化空间，而非市场规模证明。

## 1. 主表：AI-infra 子类 × 开源 top × 公有云对标 × Olares

> 图例部署：📱 端侧/CPU｜💻 消费级单卡｜🏢 多卡/服务器。star 数以官方 GitHub 为准、快变，均以 AS_OF 记。

| 子类 | 开源 top 产品 | 公有云 / 闭源对标叫法 | Olares 内置 / 平替 |
|------|-------------|-------------------|-------------------|
| 推理服务（生产/GPU） | vLLM、SGLang、LMDeploy | AWS Bedrock / SageMaker、Together、Fireworks、Baseten、Modal | 内置 vLLM / SGLang（llm-init 拉起） |
| 推理服务（消费级/端侧） | llama.cpp、Ollama | Bedrock serverless、Vertex | 内置 Ollama（共享）/ llama.cpp |
| 模型网关 / 路由 | LiteLLM、Bifrost、TensorZero | OpenRouter、Vercel AI Gateway、Cloudflare AI Gateway、Portkey | 内置 LiteLLM / Bifrost / TensorZero |
| GPU 共享 / 切片 / 调度 | HAMi、nvshare、NVIDIA MIG、Kueue | 云 GPU 实例分片 / 托管调度 | 内置 HAMi / GPUBinding / nvshare |
| 向量数据库 | Qdrant、Milvus、Weaviate、pgvector、Chroma | Pinecone、Turbopuffer、Zilliz Cloud、Weaviate/Qdrant Cloud | pgvector（PostgreSQL 内置）；Qdrant/Milvus 可装 |
| Embedding / Rerank | BGE-M3、Qwen3-Embedding、Nomic Embed；BGE-reranker | Voyage AI、Cohere Embed/Rerank、OpenAI Embeddings、Gemini Embedding、Jina | 走本地推理跑 BGE-M3 / Qwen3-Embedding |
| RAG / 知识库 | RAGFlow、LlamaIndex、Haystack、AnythingLLM | Vertex AI Search、Bedrock Knowledge Bases | Market：RAGFlow / AnythingLLM / Dify |
| Agent / 工作流编排 | Dify、n8n、Flowise、LangGraph | Vertex Agent Builder、Bedrock Agents、Azure AI Foundry Agent | 内置/Market：Dify / n8n / Flowise |
| 可观测 / 评估 | Langfuse、Arize Phoenix | LangSmith、Braintrust、Helicone、W&B Weave、Datadog LLM | Market：Langfuse（+ Netdata/Grafana 底座） |
| 微调 / 训练 | LLaMA-Factory、Unsloth、Axolotl、TRL/PEFT | HF AutoTrain、Bedrock/SageMaker/Vertex fine-tune | Market：LLaMA Factory |
| 模型仓库 / 权重分发 | Hugging Face 生态、Ollama registry（OCI）、Harbor | Hugging Face Hub（公有中心） | Ollama 本地内容寻址 + 可自建私有 registry |

## 2. 推理服务与模型网关

**推理服务**分两档。生产/GPU 档：**vLLM**（Apache-2.0，官方 GitHub 约 85K star、v0.24.0/2026-06）以 PagedAttention + 连续批处理成为事实标准，OpenAI 兼容 API、200+ HF 架构、覆盖 NVIDIA/AMD/CPU/Gaudi/TPU，是唯一同时具备张量/流水/数据/专家/上下文并行的开源引擎 [1]；**SGLang**（Apache-2.0，UC Berkeley+LMSys，约 25–28K star）以 RadixAttention 前缀缓存见长，适合 agentic/共享上下文/MoE，但社区较小、仅 Linux [4][5]；**LMDeploy**（上海 AI Lab，TurboMind 引擎）在 NVIDIA 上量化/长上下文强，尤擅中文模型 [4][5]。HuggingFace TGI 已进入维护模式、仓库 2026-03 归档，官方建议改用 vLLM/SGLang [4][5]。消费级档：**Ollama**（约 174K star，mindshare 领先）本质是 **llama.cpp**（约 73K star，MIT）的封装/GUI，llama.cpp 才是覆盖 CPU/Apple Silicon 的底层引擎 [4][6]。并发是选型分水岭：64 并发下 vLLM 生成速率约为 llama.cpp 的 44 倍，单用户下两者接近 [6]。

**模型网关**：**LiteLLM**（Apache-2.0，约 52K star，Python）是自托管默认——SDK+代理、OpenAI 兼容、100+ provider、含虚拟 key/预算/负载均衡/guardrails [8][9]；**Bifrost**（Go，约 6K star）主打性能，宣称 5000 RPS 下每请求约 11µs 开销、集群模式、MCP 支持，但 provider 覆盖较窄 [8][9]；**TensorZero**（Rust，约 11.7K star）统一网关+可观测+评估，但公司 2026-06 停运、仓库归档只读（Apache 代码与社区 fork 仍在）[9]。闭源对标叫法：OpenRouter（托管市场）、Vercel/Cloudflare AI Gateway、Portkey [8]。

公有云托管推理三档：按 token serverless（Together 200+ 模型 OpenAI 兼容 / Fireworks 自研 FireAttention、FP8/FP4）、带容器控制的自动扩缩（Baseten UI / Modal 代码优先）、超大规模平台（Bedrock/SageMaker/Vertex/Azure AI Foundry）[2][3][7]。这些云 provider 底层多用 vLLM，与自托管栈同源 [7]——正是"同样引擎，自己跑省中间商"的叙事支点。

**置信度:** High（推理引擎均有官方 GitHub 背书）
**依据:** vLLM/HAMi/LLaMA-Factory 官方源直接采集，云对标有 Together/Fireworks 官方文档。
**反方解释:** star/版本各源出入大，一律以官方 GitHub 为准并标 AS_OF [6]。

## 3. GPU 共享与微调训练

**GPU 共享**：K8s 默认 GPU 调度是独占式（`nvidia.com/gpu:1`＝整卡）、无显存配额，而典型推理只用 20–40% 算力 [12]。三条共享路线：NVIDIA Time-Slicing（并发但无显存隔离，一个 Pod OOM 拖垮整卡）、MIG 硬件分区（真隔离但仅 A100/H100 等数据中心卡）、**HAMi**（CNCF Sandbox，软件层 CUDA 拦截，无需改驱动/应用）[12]。HAMi 用 `nvidia.com/gpumem`(MiB) 与 `nvidia.com/gpucores`(%) 细粒度声明、libvgpu.so 硬隔离（超配 OOM），支持 NVIDIA/Ascend/Cambricon/Hygon 等多厂商，可与 Volcano/Kueue/Koordinator 协同 [10][11][12][13]。**MIG 在消费卡不可用，正是"个人云单卡共享必须软件层拦截"的关键**——对应 Olares 内置 HAMi/GPUBinding/nvshare。

**微调/训练**三强互补：**LLaMA-Factory**（约 72K star，Apache-2.0，v0.9.5/2026-05）是 GUI 优先的统一训练枢纽，支持 100+ 模型与 SFT/PPO/DPO/继续预训练，集成 FlashAttention-2/Unsloth/Liger、对接 HF/vLLM/SGLang [16][17]；**Unsloth**（约 54K star）是速度/显存引擎，自研 Triton kernel 做到 2–5× 更快、VRAM 降 70–80%，但主打单 GPU、核心许可 LGPL（商用需注意）[14][15]；**Axolotl**（约 11K star，Apache-2.0）配置驱动、靠 FSDP/DeepSpeed 做多 GPU/多节点，适合可复现生产/RLHF [14][15]。三者可组合（LLaMA-Factory 用 Unsloth 作后端，仅慢约 6%）[15][17]；TRL/PEFT 是 HF 的对齐与参数高效微调底层库 [14]。训练与推理栈同源：LLaMA-Factory/Unsloth 均导出 GGUF 供 Ollama/vLLM 部署 [17]。

**置信度:** High
**依据:** HAMi 四条官方文档 + LLaMA-Factory 官方 GitHub。
**反方解释:** Unsloth 多 GPU/多节点弱于 Axolotl、LGPL 商用受限，"Unsloth 通吃"不成立 [14][15]。

## 4. 向量库与 Embedding/Rerank

**向量库**无单一最佳，按规模分层：**pgvector**（已有 PostgreSQL 时的默认，约 5000 万向量内低运维）、**Qdrant**（<1 亿向量的性能/过滤首选，Rust/Apache-2.0，单 Docker、约 100MB 内存跑 1M 向量、p99<15ms、综合评分居首）、**Milvus**（十亿级/K8s 分布式，但需 etcd/MinIO 多组件、自托管较重）、**Weaviate**（原生 BM25+向量混合检索）、**Chroma**（原型/本地优先）[18][19][20][21]。**Pinecone** 是闭源全托管、无自托管选项，是要对标的公有云对象；云对标叫法还有 Zilliz Cloud（Milvus 托管）、Qdrant/Weaviate Cloud、Turbopuffer（对象存储型托管向量）[19][21]。对个人云单机/小集群，**Qdrant 单容器易运维最契合**；Olares 已有 PostgreSQL 可直接用 pgvector 兜底。

**Embedding/Rerank**：**BGE-M3**（BAAI，568M，MIT）是自托管多语种（100+ 语言）事实标准，单次前向支持 dense+sparse+multi-vector(ColBERT)，单张 L4 即可生产 [22][23]；**Qwen3-Embedding-8B**（Apache-2.0）在 MTEB 第一梯队（约 70.6）、4096 维/32K 上下文，轻量档 0.6B 也是边缘 near-SOTA [22][24]；**Nomic Embed v2**（Apache-2.0，137M，首个 MoE 文本嵌入）支持 Matryoshka 截断，适合 CPU/边缘 [24]。Rerank 开源侧用 BGE-reranker 系列。闭源对标叫法：Voyage AI（精度溢价约 3×）、Cohere Embed/Rerank（端到端配套）、OpenAI text-embedding-3、Gemini Embedding、Jina v3 [22][23][24]。（本工作区另有本地部署结论见 [model/research/07-embedding/embedding.md](/Users/pengpeng/seo/directions/model/research/07-embedding/embedding.md)。）

**置信度:** Medium
**依据:** 向量库/Embedding 任务来源以 secondary/community 为主，star/MTEB 分数以官方口径校准、取定性"第一梯队"。
**反方解释:** pgvector 在 1 亿+ 向量会因磁盘 I/O 降级、recall 掉到 0.88–0.93，"pgvector 万能"不成立，大规模仍需专用库 [21]。

## 5. RAG、Agent 编排与可观测/仓库

**RAG**：**RAGFlow**（约 84K star，Apache-2.0）是自托管 RAG 引擎首选——深度文档解析（多栏 PDF/表格/扫描件）、内置 Web UI/知识库、多路召回+融合重排，2026 起升级为融合 Agent 的 context engine [25][27]；**LlamaIndex**（约 40K star，MIT）是库首选（160+ 加载器、知识图谱索引）；**Haystack**（deepset）是管线优先的合规级企业搜索；**AnythingLLM**（约 35K star）是 no-code UI 最快路径 [27][28][29]。

**Agent/工作流编排**四类定位分明：**n8n**（约 182K star，fair-code）通用自动化优先、AI 是一步；**Dify**（Apache-2.0，约 106K star）生产级 LLM 应用平台（RAG 质量强、可发布 Web app）；**Flowise**（约 51K star，基于 LangChain）可视化拖拽、3.x Agentflow 做多 Agent；**LangGraph**（MIT）代码优先状态机，内置 checkpointing/持久状态/人在环，复杂 agentic 逻辑标准 [30][31]。闭源对标：Vertex Agent Builder、Bedrock Agents、Azure AI Foundry Agent [31]。多篇推荐的自托管全栈组合是"n8n 编排 + Dify/Flowise 交互 + Qdrant/Weaviate 向量 + Ollama/vLLM 模型 + Langfuse/Grafana 可观测"[28][31]——正是本报告各子类的拼图。

**可观测/评估**：**Langfuse**（MIT，2026-01 被 ClickHouse 收购）是自托管默认——框架无关、基于 OpenTelemetry、tracing+prompt 管理+评估、可气隙部署、无 trace 上限 [32][33]；**Arize Phoenix**（Apache-2.0）评估与 agent 诊断最强 [33][34]。闭源对标：LangSmith、Braintrust（evals-in-CI）、Helicone、W&B Weave、Datadog LLM [33][34]。**模型仓库**：Hugging Face Hub 是公有中心 [41]；Ollama 用 OCI 兼容内容寻址（SHA256 去重、CDN 分块），可自建私有 registry（Docker Distribution / Harbor）做本地权重分发与数据驻留 [39][40]。

**置信度:** Medium
**依据:** RAGFlow/Dify/Langfuse 有官方 GitHub/文档，其余对比多为行业分析。
**反方解释:** 低代码 Agent 平台（n8n/Dify/Flowise）在长运行多 Agent 状态、亚秒延迟、CI 级测试场景会崩，需转 code-first（LangGraph）——"可视化平台通吃 Agent"不成立 [30]。

## 核心争议

- **自托管是否主流:** O'Reilly/TURION 描绘分层自托管栈成熟 [36][37] vs Menlo 数据称开源仅占企业 LLM 用量约 11% 且同比下降 [6]——企业侧仍以托管 API 为主，自托管是主权/成本诉求而非份额优势。
- **是否需要全 6 层:** 多数企业只跑推理、不训练 [35]，个人云用户对企业级 Governance/Feature Store 全套多为过重；Olares 应聚焦推理+RAG+Agent+可观测轻栈。
- **pgvector vs 专用向量库:** "有 PG 就够"在 <5000 万向量成立 [37]，超大规模会降级 [21]。

## 关键发现

- **发现 1（Olares 覆盖高）:** 推理（vLLM/SGLang/Ollama/llama.cpp）、网关（LiteLLM/Bifrost/TensorZero）、GPU 共享（HAMi/nvshare）、Agent 编排（Dify/n8n/Flowise）、微调（LLaMA Factory）Olares 已内置或 Market 已上架 [1][8][10][17][31]。
- **发现 2（缺口）:** 向量库（建议 Qdrant，pgvector 兜底）、Embedding/Rerank 服务化（BGE-M3/Qwen3-Embedding）、可观测评估（Langfuse）是相对薄弱、值得补的三块 [18][22][32]。
- **发现 3（差异化）:** AI-infra 底层引擎与公有云同源（云也用 vLLM）[7]，且 2026 Agent 栈新增 MCP/记忆/eval 三类一等类别 [36]——正对 Olares 的 Personal Agent + 系统级 MCP 叙事。

## 局限性与未来方向

### 本研究局限
- 无 academic 源：AI-infra 属工程实践，权威集中在官方 GitHub/文档 + 行业分析，已用官方占比（32%）与多域名补偿；star/版本快变，均标 AS_OF、以官方为准。
- 向量库/Embedding/RAG 的 star 与 MTEB 分数各源差异大，采官方口径 + 定性表述。
- 扩展类别（Feature Store/Feast、数据管道 Airflow/Dagster、GraphRAG Neo4j/Memgraph、Guardrails、记忆/MCP 协议层）仅有 landscape 综述级来源，未逐一深挖 top 产品 [35][36][37][38]，作低置信呈现。

### 未来方向
- 对 Olares 缺口三块（向量库/Embedding/可观测）各跑一次 brand-seo-research 找 `self-hosted X` / `X alternative` 词。
- 深挖 MCP/记忆栈（与 model/ 的 memory 视角、commerce #4 Memory 层交叉）作 agent-native 内容。

## 参考文献

[1] vLLM. "vllm-project/vllm". Source-Type: official. As Of: 2026-07. https://github.com/vllm-project/vllm
[2] Together AI. "Serverless Inference". Source-Type: official. As Of: 2026. https://www.together.ai/serverless-inference
[3] Fireworks AI. "Serverless Overview". Source-Type: official. As Of: 2026. https://docs.fireworks.ai/serverless/overview
[4] Fish Audio. "Open-source LLM inference engines compared 2026". Source-Type: secondary-industry. As Of: 2026. https://fish.audio/blog/open-source-llm-inference-engines-2026/
[5] Presenc AI. "Open-Weight Serving Stack Comparison 2026". Source-Type: secondary-industry. As Of: 2026. https://presenc.ai/research/open-weight-serving-stack-comparison-2026
[6] Nishil Bhave. "Local LLMs in 2026". Source-Type: journalism. As Of: 2026-06. https://medium.com/@nishilbhave/local-llms-in-2026-which-runtime-to-run-and-the-hardware-you-need-a88450dece2e
[7] Saturn Cloud. "Inference Provider Comparison Report". Source-Type: secondary-industry. As Of: 2026. https://saturncloud.io/reports/inference-provider-comparison-report/
[8] Maxim AI. "OpenRouter vs LiteLLM vs Bifrost". Source-Type: secondary-industry. As Of: 2026. https://www.getmaxim.ai/articles/openrouter-vs-litellm-vs-bifrost-ai-gateway-comparison/
[9] cuihuan. "awesome-ai-gateway". Source-Type: community. As Of: 2026. https://github.com/cuihuan/awesome-ai-gateway
[10] HAMi. "Project-HAMi/HAMi". Source-Type: official. As Of: 2026. https://github.com/Project-HAMi/HAMi/
[11] HAMi. "Heterogeneous GPU Sharing on Kubernetes". Source-Type: official. As Of: 2026. https://project-hami.io/
[12] HAMi. "GPU Virtualization Principles". Source-Type: official. As Of: 2026. https://project-hami.io/docs/core-concepts/gpu-virtualization
[13] HAMi. "How to use Kueue on HAMi". Source-Type: official. As Of: 2026. https://project-hami.io/docs/userguide/kueue/how-to-use-kueue
[14] Clore.ai. "Fine-tuning Tools Comparison". Source-Type: secondary-industry. As Of: 2026. https://docs.clore.ai/guides/comparisons/finetuning-comparison
[15] Paolo Perrone. "Unsloth vs Axolotl vs LLaMA-Factory". Source-Type: journalism. As Of: 2026. https://theaiengineer.substack.com/p/unsloth-vs-axolotl-vs-llama-factory
[16] ultraduneai. "EVAL #003 Fine-Tuning in 2026". Source-Type: community. As Of: 2026-03. https://dev.to/ultraduneai/eval-003-fine-tuning-in-2026-axolotl-vs-unsloth-vs-trl-vs-llama-factory-2ohg
[17] LLaMA-Factory. "hiyouga/LLaMA-Factory". Source-Type: official. As Of: 2026. https://github.com/hiyouga/LLaMA-Factory
[18] Qdrant. "qdrant/qdrant". Source-Type: official. As Of: 2026-07. https://github.com/qdrant/qdrant/
[19] Darshit. "The Best Vector Database in 2026". Source-Type: community. As Of: 2026. https://dev.to/darshit_01/the-best-vector-database-in-2026-qdrant-vs-pinecone-vs-weaviate-vs-milvus-vs-pgvector-3147
[20] kunalganglani. "Milvus vs Qdrant 2026". Source-Type: secondary-industry. As Of: 2026. https://www.kunalganglani.com/blog/milvus-vs-qdrant
[21] Pratik R. "Top 15 Vector Databases in 2026". Source-Type: secondary-industry. As Of: 2026. https://medium.com/@pratik-rupareliya/top-15-vector-databases-in-2026-a-production-decision-guide-from-100-enterprise-deployments-dd58a04f51a5
[22] axiomlogica. "OpenAI vs BGE/E5/Voyage/Cohere/Qwen3 Embedding". Source-Type: secondary-industry. As Of: 2026. https://axiomlogica.com/ai-ml/openai-text-embedding-3-small-vs-bge-e5-voyage-cohere-qwen3-embedding-retrieval
[23] RuleSell. "The 12 Embedding Models Worth Running (MTEB 2026)". Source-Type: secondary-industry. As Of: 2026. https://www.rulesell.com/topic/embeddings
[24] Ailog RAG. "Embedding Models 2026: Benchmark". Source-Type: secondary-industry. As Of: 2026-01. https://app.ailog.fr/en/blog/news/embedding-models-2026
[25] RAGFlow. "infiniflow/ragflow". Source-Type: official. As Of: 2026-07. https://github.com/infiniflow/ragflow
[26] Dify. "langgenius/dify". Source-Type: official. As Of: 2026-07. https://github.com/langgenius/dify
[27] OSSAlt. "Best Open Source RAG Frameworks 2026". Source-Type: secondary-industry. As Of: 2026. https://ossalt.com/guides/best-open-source-rag-frameworks-2026
[28] Clore.ai. "RAG Frameworks Comparison". Source-Type: secondary-industry. As Of: 2026. https://docs.clore.ai/guides/comparisons/rag-frameworks-comparison
[29] GIGAGPU. "Best RAG Frameworks in 2026". Source-Type: secondary-industry. As Of: 2026-04. https://gigagpu.com/best-rag-frameworks-2026/
[30] aifoss.dev. "Flowise vs n8n vs LangGraph 2026". Source-Type: secondary-industry. As Of: 2026-05. https://aifoss.dev/blog/flowise-vs-n8n-vs-langgraph-2026/
[31] jahanzaib.ai. "Flowise vs Dify vs n8n". Source-Type: secondary-industry. As Of: 2026. https://www.jahanzaib.ai/blog/flowise-vs-dify-vs-n8n-ai-agents
[32] Langfuse. "Langfuse vs LangSmith". Source-Type: official. As Of: 2026. https://langfuse.com/resources/engineering/langsmith-alternative
[33] Anhaia. "Langfuse vs LangSmith vs Phoenix vs Braintrust". Source-Type: community. As Of: 2026-04. https://dev.to/gabrielanhaia/langfuse-vs-langsmith-vs-phoenix-vs-braintrust-the-honest-2026-comparison-253p
[34] SideGuy. "LLM Observability 10-way comparison 2026". Source-Type: secondary-industry. As Of: 2026. https://www.sideguysolutions.com/shareables/llm-observability-software-10-way-comparison-2026-langfuse-langsmith-braintrust-arize-phoenix-helicone-weave-whylabs-datadog-newrelic-traceloop.html
[35] RIVER Group. "The Enterprise AI Stack in 2026". Source-Type: secondary-industry. As Of: 2026. https://rivergroup.ai/insights/the-enterprise-ai-stack-2026
[36] O'Reilly. "The AI Agents Stack 2026 Edition". Source-Type: secondary-industry. As Of: 2026. https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/
[37] TURION.AI. "The AI Infrastructure Stack 2026 Edition". Source-Type: secondary-industry. As Of: 2026. https://turion.ai/blog/ai-infrastructure-stack-2026-edition/
[38] Orca Security. "Memory in AI: MCP, A2A & Agent Context Protocols". Source-Type: secondary-industry. As Of: 2026. https://orca.security/resources/blog/bringing-memory-to-ai-mcp-a2a-agent-context-protocols/
[39] Read OSS. "Ollama Model Management & Registry Protocol". Source-Type: secondary-industry. As Of: 2026. https://readoss.com/en/ollama/ollama/model-management-storage-conversion-registry-protocol
[40] CODE Magazine. "Running LLMs Locally Using Ollama". Source-Type: secondary-industry. As Of: 2026. https://www.codemag.com/Article/264031/Running-Large-Language-Models-Locally-Using-Ollama
[41] Hugging Face. "Hub documentation". Source-Type: official. As Of: 2026. https://huggingface.co/docs/hub/index
