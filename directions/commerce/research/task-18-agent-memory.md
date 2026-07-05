# dig-18 · Agent 记忆层 / Memory 基础设施赛道 · 发现蒸馏笔记

**AS_OF=2026-07-04** · 赛道定义：给 AI Agent 提供长期记忆/上下文持久化/知识图谱记忆的基础设施或 API（≠笔记软件，≠向量数据库）。只做发现+财务。门槛：ARR>$50M｜估值>$200M｜融资>$20M｜大厂旗舰。

## Sources（节选）
TechCrunch/PRNewswire/Tech.eu / PitchBook/CBInsights/Tracxn/Caplight / 官方博客(Cognee/LangChain/MongoDB/Redis/SurrealDB) / GitHub。

## Products
| 名称 | 公司 | 域名 | 开源? | 财务 | 命中 | 定位 |
|------|------|------|------|------|------|------|
| **Mem0** | Mem0 Inc. | mem0.ai | 是(Apache2.0+云) | 融资 $24M；ARR ~$1M(2024)[u] | **融资✓** | 开发者向 agent memory API，最接近 pure-play |
| **Engram** | Engram | engram.com | 否 | 融资 $98M；估值 ~$600M[u] | **融资✓估值✓** | 企业 learned memory layer（预压缩组织知识进模型） |
| Zep | Zep | getzep.com | 否(Graphiti 开源) | 融资 ~$2.3M | 未达标 | 企业 Context Lake + Graph RAG memory |
| Graphiti | Zep | github.com/getzep/graphiti | **是** | 归 Zep ~$2.3M | 未达标 | 开源时序 context graph 引擎 |
| Letta(原 MemGPT) | Letta | letta.com | **是** | 融资 $10M；估值 $70M | 未达标 | 有状态 agent OS，分层自编辑记忆 |
| Cognee | Cognee | cognee.ai | **是**+云 | 融资 $7.5M(累计~$9M) | 未达标 | 开源 graph memory engine |
| Supermemory | Supermemory | supermemory.ai | 部分开源 | 融资 $2.6M | 未达标 | Universal Memory API |
| Memobase | memodb-io | memobase.ai | **是** | $0 | 未达标 | profile-based 用户长期记忆 |
| Memories.ai | Memories.ai | memories.ai | 否 | 融资 $16M | 未达标(差$4M) | 视觉记忆模型（可穿戴/机器人），非通用 memory API |
| Pieces LTM | Pieces | pieces.app | 否 | 融资 ~$25.5M；估值 ~$35.5M | **融资✓**(边界:开发者 workflow memory) | 开发者桌面长期记忆 |
| SurrealDB 3.0 | SurrealDB | surrealdb.com | **是** | 融资 $44M 累计 | **融资✓**(边界:DB 重定位) | AI-native 多模型 DB 主打 persistent memory |
| LangGraph Store + LangMem | LangChain | langchain.com | 框架开源/平台商业 | 融资 $125M；估值 $1.25B | **估值✓**(memory 为子能力) | agent 平台内置 cross-thread 长期记忆 |
| MongoDB Store / Redis Agent Memory Server | MongoDB / Redis | — | 集成开源 | 上市公司，无独立 SKU ARR | 大厂旗舰 | Atlas/Redis 作 agent memory backend |
| Dust | Dust | dust.tt | 否 | 融资 >$60M | **融资✓**(边界:企业 agent OS) | 企业 multiplayer agent 平台，memory 为子模块 |
| Hyperspell | Hyperspell | hyperspell.com | 否 | 融资 ~$1.5–2M | 未达标 | 企业 workspace 连接器→agentic memory network |

## 赛道结论（回答用户直觉）
**用户直觉大体正确**：纯"Agent Memory 抽象层"独立公司几乎没跑成大盘商业；**全程未见任何一家披露 ARR>$50M**。但 2025–2026 已有少数**跨过融资门槛**：
- **Mem0 $24M**（最接近 pure-play）、**Engram $98M/~$600M 估值**（enterprise learned-memory 模型路线）；边界达标：SurrealDB $44M、Pieces ~$25.5M、Dust >$60M；LangChain $1.25B（memory 是子能力）。
- 大厂已把 memory 做成**平台能力/feature**（Redis/MongoDB/LangGraph），独立 memory SaaS 空间被挤压——standalone 定价是最大结构性风险。

**建议**：单独设一个小类 `Agent 记忆 / Memory 层`，仅收 **Mem0、Engram**（+ 边界注 Pieces/Dust/SurrealDB），并明确标注"赛道尚早、无 ARR>$50M 赢家"。Mem/Mem0 从 #36 笔记类删除。

## 平替（Olares 侧）
Mem0 OSS(Apache2.0) / Letta(MemGPT) / Cognee / Graphiti / Redis Agent Memory Server / Memobase — 均可自托管。

## Gaps
- Charmonium 查无对应公司（疑误拼）；Memories.ai 是视觉记忆非通用 memory API。
- ARR 全线缺失，门槛1 对 pure-play 无法核实（可能均未达标）。
- Engram $600M 估值仅 secondary 媒体，需后续轮次确认。
- 待补：memU、A-MEM、ChatGPT Memory 等闭源大厂内置（非独立 vendor）。
