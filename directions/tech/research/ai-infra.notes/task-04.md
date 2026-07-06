---
task_id: 04
role: RAG 框架与 Agent 编排分析师
status: complete
sources_found: 10
---

## Sources
[1] Best Open Source RAG Frameworks 2026 (OSSAlt) | https://ossalt.com/guides/best-open-source-rag-frameworks-2026 | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[2] infiniflow/ragflow (GitHub) | https://github.com/infiniflow/ragflow | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[3] RAG Frameworks Comparison (Clore.ai) | https://docs.clore.ai/guides/comparisons/rag-frameworks-comparison | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[4] RAG Framework Comparison (agentwiki.org) | https://agentwiki.org/rag_framework_comparison | Source-Type: community | As Of: 2026 | Authority: 5/10
[5] Best RAG Frameworks in 2026 (GIGAGPU) | https://gigagpu.com/best-rag-frameworks-2026/ | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 5/10
[6] Flowise vs n8n vs LangGraph 2026 (aifoss.dev) | https://aifoss.dev/blog/flowise-vs-n8n-vs-langgraph-2026/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 5/10
[7] Flowise vs Dify vs n8n (jahanzaib.ai) | https://www.jahanzaib.ai/blog/flowise-vs-dify-vs-n8n-ai-agents | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[8] Dify vs n8n vs Flowise enterprise 2026 (AdTools.org) | https://adtools.org/buyers-guide/dify-vs-n8n-vs-flowise-which-is-best-for-enterprise-software-teams-in-2026 | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 4/10
[9] n8n vs Flowise vs Dify 2026 (open-techstack) | https://open-techstack.com/blog/n8n-vs-flowise-vs-dify-2026/ | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 5/10
[10] n8n vs Dify vs Flowise UX Review (rapidclaw.dev) | https://rapidclaw.dev/blog/low-code-ai-agent-platforms-compared-2026 | Source-Type: secondary-industry | As Of: 2026 | Authority: 4/10

## Findings
- RAGFlow（infiniflow，84,161 stars，Apache-2.0，Go/Python/TS）是自托管 RAG 引擎首选：深度文档解析（多栏 PDF/表格/图/扫描件）、内置 Web UI/知识库管理、多路召回+融合重排，2026 起融合 Agent 能力做"context engine"。[1][2]
- LlamaIndex（~40K stars，MIT）是文档密集型 RAG 的库首选：160+ 文档加载器、LlamaParse、复杂索引/检索策略、知识图谱索引，适合自建知识库开发者。[1][4][5]
- Haystack（deepset，~18–20K stars，Apache-2.0）是管线优先的生产级企业搜索/QA 框架，声明式组件、可溯源、评估内置，适合合规敏感行业。[1][3][4]
- AnythingLLM（~35K stars）是 no-code RAG UI 首选：桌面/Docker 一键，上传文档即聊，适合非开发者最快路径。[1]
- LangChain（~90–98K stars，MIT）是通用 LLM 编排框架，RAG 只是其一环，最灵活但学习曲线中等；DSPy 走程序化 prompt 优化路线。[1][3][5]
- Agent/工作流编排四类定位分明：n8n（182K+ stars，fair-code）通用自动化优先（400+ SaaS、触发/调度/重试），AI 是其中一步。[7]
- Dify（Apache-2.0，star 各源差异大 55K–106K）是生产级 LLM 应用平台：chatbot/RAG/多 Agent，含 prompt 编排、知识摄取、模型路由、可发布 Web app，非技术团队友好。[7][8][9]
- Flowise（Apache-2.0，~51–53K stars，Node.js）是基于 LangChain 的可视化拖拽画布，3.x Agentflow 做多 Agent 编排+分支循环、OpenTelemetry 追踪、Graph RAG，最快原型路径。[6][7]
- LangGraph（MIT）是代码优先的 Python 状态机库（无 UI）：有向图定义 Agent，内置 checkpointing/持久状态/崩溃恢复/人在环，控制粒度最细，生产复杂 agentic 逻辑标准。[6][10]
- 公有云/闭源对标：Vertex AI Agent Builder、AWS Bedrock Agents、Azure AI Foundry Agent Service（托管 Agent 平台）；托管 RAG 有 Vertex AI Search、Amazon Bedrock Knowledge Bases。[8]
- 典型自托管组合被多篇推荐："n8n 编排 + Dify/Flowise 交互逻辑 + Qdrant/Weaviate 向量 + Ollama/vLLM 本地模型 + Langfuse/Grafana 可观测"——正是 AI-infra 全栈拼图。[3][8]

## Deep Read Notes
### Source [2]: infiniflow/ragflow GitHub
Key data: 84,161 stars / 470 contributors / 51 releases / 最新 v0.26.3(2026-07-02)；Apache-2.0；多路召回+融合重排；可配置 LLM 与 embedding；agentic-retrieval/context-engine 定位。
Key insight: 从"RAG 引擎"升级为"融合 Agent 的 context engine + 预置 Agent 模板"，覆盖个人到大企业。
Useful for: RAG 子类 top1 + Olares RAGFlow 平替。

### Source [7]: jahanzaib.ai Flowise vs Dify vs n8n
Key data: n8n 182K+ stars/7 年/最低 300MB RAM；Dify 106K+ stars/最低 4GB(8GB 荐)；Flowise 51K+/~1GB；Dify RAG 质量"Best（混合检索+重排）"。
Key insight: 三者自托管全免费，差异在定位（自动化 vs AI 应用平台 vs 可视化链）与资源占用，个人云选型看用途。
Useful for: Agent 编排子类对比 + Olares Dify 内置论证。

## Gaps
- star 数各源差异极大（RAGFlow 12K/36K/49K vs 官方 84K；Dify 55K/75K/80K/106K），一律以能取到的官方 GitHub 数为准、其余标"约"并降置信度。
- Dify/n8n 已在 commerce 方向登记（SaaS 视角），本报告从 infra 自托管视角列，需标注交叉。
- 公有云 Agent 平台（Vertex Agent Builder 等）未取官方文档源，采定性对标表述。
- 相反主张候选：低代码 Agent 平台（n8n/Dify/Flowise）在"长运行多 Agent 状态、亚秒延迟、CI 级测试"场景会崩，需转 code-first（LangGraph/CrewAI）——削弱"可视化平台通吃 Agent"叙事。[10]

## END
