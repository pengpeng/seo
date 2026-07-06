# Pieces / Dust / SurrealDB SEO 竞品分析报告（AI 记忆边界案例）

> 场景词分析（无统一官方域名）| SEMrush US | 2026-07-06
> 三款融资达标但 AI memory 为子能力的边界案例产品：Pieces（开发者 OS 级记忆工具）、Dust（企业 AI 工作流平台）、SurrealDB（多模型数据库+Spectron 记忆层）——共同指向"AI 记忆层"这一新兴品类词机会。

---

## 项目理解（前置）

这三款产品融资均已达标（Pieces $35M+、Dust $60M+、SurrealDB $20M+），但 AI Memory 都不是核心产品，而是能力层。它们从不同方向切入"AI 记忆"这一新兴品类：Pieces 从开发者工作流侧（OS 级上下文捕获），Dust 从企业知识管理侧（跨工具公司记忆），SurrealDB 从数据库基础设施侧（多模型统一存储+Spectron）。这形成了一个"记忆层碎片化"的叙事机会——Olares 上的 Mem0 自托管版可作为统一的、私有的 AI 记忆层替代三者中任何云服务依赖。

### Pieces for Developers（getpieces.com）

OS 级开发者 AI 记忆工具，自动捕获开发工作流上下文，提供 LTM-2.7（长期记忆引擎），支持 MCP 协议接入 Cursor / Claude / GitHub Copilot 等 IDE 工具。

| 项目 | 内容 |
|------|------|
| 一句话定位 | OS 级 AI 开发者记忆工具——自动捕获代码、文档、对话上下文，构建可查询的个人工作流知识图谱 |
| 开源 / 许可证 | 闭源（PiecesOS 核心闭源；部分 SDK/插件 MIT） |
| 主仓库 | [github.com/pieces-app](https://github.com/pieces-app)（无单一核心仓库；开放 SDK） |
| 核心功能 | LTM-2.7 引擎（OS 级捕获，9 个月记忆）、时间线查询、MCP 集成（20+ IDE/AI 工具）、本地优先加密存储、代码片段管理 |
| 商业模式 / 定价 | 免费个人版（基础功能）；Teams 付费版（协作能力），定价未公开披露；企业版定制 |
| 差异化 / 价值主张 | 本地运行、OS 级上下文（非单 IDE 插件）、9 个月记忆历史、MCP 原生支持 |
| 主要竞品（初判）| GitHub Copilot、Cursor、Mem0、Zep、MemGPT |
| Olares Market | 未上架 |
| 来源 | [pieces.app](https://pieces.app)、[docs.pieces.app](https://docs.pieces.app)、aiagentslist.com/agents/pieces |

### Dust（dust.tt）

企业级多人协作 AI 平台，支持基于公司内部知识（Notion/Slack/GitHub/Salesforce）构建定制 AI 智能体，2026 年 5 月完成 $40M 融资。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 多人协作 AI 工作流平台——让团队和 AI 智能体共享公司知识库，无代码构建业务流程自动化 |
| 开源 / 许可证 | 部分开源（[github.com/dust-tt/dust](https://github.com/dust-tt/dust)，MIT/Apache2.0 混合），核心运行于 Dust Cloud |
| 主仓库 | github.com/dust-tt/dust |
| 核心功能 | 公司知识语义层、20+ 前沿模型切换（GPT/Claude/Gemini/Mistral）、无代码 Agent 构建、MCP 服务器接入、100+ 生产连接器 |
| 商业模式 / 定价 | Pro €29/user/mo（15 天试用）；Enterprise 定制；无免费永久版 |
| 差异化 / 价值主张 | 多模型无厂商锁定、公司级知识语义层（非简单 RAG）、SOC2 Type II、GDPR/HIPAA 就绪 |
| 主要竞品（初判）| Glean、Notion AI、Guru、Confluence AI、Microsoft Copilot for M365 |
| Olares Market | 未上架 |
| 来源 | [dust.tt](https://dust.tt)、[dust.tt/home/pricing](https://dust.tt/home/pricing)、Axios May 2026 融资报道 |

### SurrealDB（surrealdb.com）

多模型开源数据库（文档/图谱/向量/关系/时序于单一 ACID 引擎），附带 Spectron（闭源 AI 智能体记忆层）。GitHub 32.6k stars，最新版本 3.x。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AI 原生多模型数据库——单一 ACID 事务内融合向量、图谱、文档、关系数据，Spectron 提供原生 Agent 记忆层 |
| 开源 / 许可证 | 数据库引擎开源（Apache2.0/BSL）；Spectron 记忆层**闭源**（Rust 二进制） |
| 主仓库 | [github.com/surrealdb/surrealdb](https://github.com/surrealdb/surrealdb)（★ 32.6k） |
| 核心功能 | 多模型统一查询（SurrealQL）、HNSW 向量索引、图谱遍历、WASM 插件（内嵌模型推理）、Spectron Agent Memory（ACID 事务级，含三时态历史、知识图谱、混合检索）、MCP 原生支持 |
| 商业模式 / 定价 | 数据库自托管免费；SurrealDB Cloud 免费起（1GB），按需 $0.021/hr；Spectron 独立定价（邀请制）；企业版定制 |
| 差异化 / 价值主张 | 取代向量库+图数据库+文档库三件套、ACID 事务级 Agent 记忆（无一致性缝隙）、Spectron 可自托管 |
| 主要竞品（初判）| MongoDB、PostgreSQL+pgvector、Weaviate、Neo4j、Mem0（记忆层竞品） |
| Olares Market | 未上架（可自托管；未见 Olares Market 收录） |
| 来源 | [surrealdb.com](https://surrealdb.com)、[surrealdb.com/platform/spectron](https://surrealdb.com/platform/spectron)、[surrealdb.com/3.0](https://surrealdb.com/3.0) |

---

## 流量基线（Phase 1）

> **降级模式**：三款产品无统一分析域名（Dust 域名结构简单但品类词干扰严重；Pieces/SurrealDB 有官网但本报告聚焦场景词机会）。跳过 `domain_rank` / `resource_organic` 等域名级报告，直接从品牌词量级定标，再切入场景词层面分析。

### 品牌词量级基线（`phrase_these`）

| 品牌关键词 | 月量 | KD | CPC | 意图 | 备注 |
|------------|------|----|----|------|------|
| dust ai | 1,300 | 29 | $3.48 | 导航 | ⭐ KD<30，最大品牌词机会 |
| surrealdb | 1,000 | 53 | $4.50 | 导航 | 开发者社区已认知 |
| pieces ai | 480 | 50 | $0.03 | 信息/商业 | 泛 AI 搜索混杂 |
| pieces os | 480 | 46 | — | 导航 | 产品系统层认知 |
| pieces for developers | 260 | 40 | $6.88 | 导航 | 精准品牌词，CPC 高 |
| pieces desktop | 260 | 28 | $5.04 | 信息 | ⭐ KD 低，下载意图 |
| letta | 1,900 | 50 | $6.50 | 导航 | Mem0 生态中最强竞品品牌 |
| MemGPT | 1,300 | 29 | $11.81 | 信息 | ⭐ KD<30，记忆品类入口词 |
| mem0 | 5,400 | 59 | $4.16 | 信息 | 记忆品类最大独立品牌词 |
| dust.tt | 50 | 54 | $7.05 | 导航 | 精确域名词，量小 |
| pieces mcp | 50 | 10 | — | 信息/商业 | ⭐⭐ KD=10，MCP 集成入口 |
| pieces copilot | 50 | 33 | $3.23 | 导航 | 功能词 |
| pieces pricing | 70 | 18 | — | 商业/信息 | ⭐ 购买意图，KD 低 |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| glean alternative | 70 | 10 | $15.04 | 信息 | ⭐ Dust 竞品替代词，KD=10 且 CPC 极高 |
| notion AI alternative | 50 | 18 | $4.54 | 信息 | ⭐ 知识类 AI 替代 |
| confluence alternative | 210 | 23 | $7.26 | 信息 | ⭐ 企业知识平台替代词 |
| surrealdb vs mongodb | 20 | — | — | 信息 | 技术选型词 |
| surrealdb vs postgres | 20 | — | — | 信息 | 技术选型词 |
| mem0 alternative | 0 | — | — | — | GEO 前哨，量近零但语义精准 |
| zep alternative | 20 | — | $3.58 | 信息 | ⭐ 记忆层替代词 |
| pinecone alternative | 20 | — | $4.66 | 信息 | 向量库替代 |
| dust alternative | 10 | — | — | 信息 | 量极小，GEO 价值 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| AI workflow automation | 3,600 | 64 | $14.84 | 信息 | 高量高 KD，Dust 主战场 |
| build AI agents | 1,300 | 57 | $10.12 | 信息 | 平台类大词 |
| AI agents for business | 720 | 75 | $15.52 | 信息 | 竞争激烈 |
| custom AI agents | 480 | 61 | $12.40 | 信息 | Dust 核心词 |
| on device AI | 480 | 47 | $4.04 | 信息 | Pieces 的本地化叙事词 |
| enterprise AI agents | 320 | 10 | $12.07 | 信息 | ⭐⭐ KD=10，CPC 高，企业转化词 |
| agent memory | 260 | 33 | $3.55 | 信息 | ⭐ 记忆品类核心词 |
| LLM memory | 260 | 50 | $3.99 | 信息 | 记忆层技术词 |
| private AI | 1,900 | 29 | $3.58 | 信息 | ⭐ Olares 核心叙事词，KD 低 |
| open source vector database | 590 | 27 | $6.05 | 信息 | ⭐ SurrealDB/Olares 机会词 |
| multi model database | 170 | 28 | $11.00 | 信息 | ⭐ SurrealDB 核心品类词，KD 低 |
| multi-model database | 110 | 20 | $25.90 | 信息 | ⭐⭐ KD=20，CPC 极高，高价值 |
| AI agent memory | 110 | 53 | $4.31 | 信息 | 记忆品类核心词 |
| rust database | 110 | 29 | $4.69 | 信息 | ⭐ SurrealDB 技术社区词 |
| self hosted AI | 390 | 36 | $3.90 | 信息 | ⭐ Olares 叙事场景词 |
| local AI assistant | 110 | 50 | $4.31 | 信息 | Pieces 叙事词 |
| memory MCP | 480 | 39 | $3.81 | 信息 | MCP 生态记忆入口 |
| MCP memory server | 90 | 22 | $3.84 | 信息 | ⭐ KD=22，MCP 集成词 |
| no code AI agents | 140 | 17 | $7.89 | 信息 | ⭐ Dust 用户场景词，KD 低 |
| graph vector database | 50 | 21 | $4.83 | 信息 | ⭐ SurrealDB 差异化词 |
| mem0 open source | 40 | 41 | — | 信息/商业 | Olares 替代词 |
| AI memory layer | 40 | 41 | — | 信息 | 品类新词 |
| agentic memory | 210 | 36 | $4.35 | 信息 | 语义词 |
| what is persistent memory in ai agents | 50 | — | — | 信息 | 问题词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| pieces for developers | 260 | 40 | $6.88 | 导航 | 主品牌词 |
| pieces os | 480 | 46 | — | 导航 | 系统层 |
| pieces desktop | 260 | 28 | $5.04 | 信息 | ⭐ KD=28，下载入口 |
| pieces mcp | 50 | 10 | — | 信息/商业 | ⭐⭐ MCP 集成词 |
| pieces pricing | 70 | 18 | — | 商业 | ⭐ 商业意图 |
| pieces tech | 140 | 22 | $5.09 | 信息 | ⭐ 技术定位词 |
| surrealdb cloud | 20 | — | — | 导航 | 托管服务词 |
| surrealdb spectron | 20 | — | — | 信息 | 新功能词，量小待涨 |
| surrealql | 20 | — | — | 信息 | 技术词 |
| dust pricing | 50 | 9 | $8.21 | 商业 | ⭐⭐ KD=9，高 CPC，购买决策词 |
| dust app | 480 | 27 | — | 信息 | ⭐ 但意图宽泛 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| private AI | 1,900 | 29 | $3.58 | 信息 | ⭐⭐⭐ 最大自托管叙事词 |
| self hosted AI | 390 | 36 | $3.90 | 信息 | ⭐⭐ Olares 核心 |
| open source vector database | 590 | 27 | $6.05 | 信息 | ⭐⭐ SurrealDB/Olares 机会 |
| multi-model database | 110 | 20 | $25.90 | 信息 | ⭐⭐ Olares 上 SurrealDB 自托管角度 |
| mem0 open source | 40 | 41 | — | 信息 | 自托管 Mem0 入口 |
| mem0 self hosted | 20 | — | — | 信息 | ⭐ 量小但意图精准 |
| redis memory server | 20 | — | — | 信息 | Redis Agent Memory MCP 词 |
| agent memory open source | 0 | — | — | — | GEO 词 |
| self-hosted AI memory | 0 | — | — | — | GEO 词 |
| open source AI memory | 10 | — | — | 信息 | 近零量，GEO |

---

## Olares 关联词（Phase 3）

**核心逻辑：三款产品均有云服务依赖（Pieces 云同步可选但闭源、Dust 纯云、SurrealDB Cloud + Spectron 闭源），Olares 上的 Mem0 自托管版提供完整 AI 记忆层替代，无需任何第三方云服务；SurrealDB 可在 Olares 上完整自托管实现统一数据库层。**

| 关键词 | 月量 | KD | CPC | 契合度 | Olares 角度 |
|--------|------|----|----|--------|------------|
| private AI | 1,900 | 29 | $3.58 | ⭐⭐⭐ | Olares 本地优先，所有 AI 记忆层（Mem0/SurrealDB）完全离线，无数据上传 |
| enterprise AI agents | 320 | 10 | $12.07 | ⭐⭐⭐ | Olares 可替代 Dust 云——在私有云上部署 Dify/Flowise + Mem0，企业自主掌控智能体知识库 |
| self hosted AI | 390 | 36 | $3.90 | ⭐⭐⭐ | Olares 是自托管 AI 记忆层的最简路径，一键装 Mem0 + SurrealDB |
| open source vector database | 590 | 27 | $6.05 | ⭐⭐ | SurrealDB 可在 Olares 上自托管替代 Pinecone/Weaviate 等闭源向量库 |
| multi-model database | 110 | 20 | $25.90 | ⭐⭐ | SurrealDB on Olares：一张数据库满足向量/图谱/文档需求，无需多库拼接 |
| agent memory | 260 | 33 | $3.55 | ⭐⭐⭐ | Mem0 on Olares：为所有 AI Agent 提供私有、持久、可自控的记忆层 |
| MCP memory server | 90 | 22 | $3.84 | ⭐⭐ | Mem0 提供 MCP 服务器；Olares 用户可将本地 Mem0 作为 Claude/Cursor 的私有记忆后端 |
| MemGPT | 1,300 | 29 | $11.81 | ⭐⭐ | Letta（MemGPT 演进版）可自托管；Olares 提供与 Mem0 并列的记忆层选项 |
| mem0 open source | 40 | 41 | — | ⭐⭐⭐ | 直接机会：Mem0 OSS 版 + Olares 一键部署，完全替代 mem0.ai 云服务 |
| mem0 self hosted | 20 | — | — | ⭐⭐⭐ | GEO 级精准词：Olares Market 中 Mem0 自托管教程覆盖此词 |
| pieces alternative | 0 | — | — | ⭐ | GEO：Olares + Mem0 + 本地 LLM 可复制 Pieces 核心价值（隐私+记忆） |
| dust alternative | 10 | — | — | ⭐⭐ | GEO：Olares + Dify/RAGFlow + Mem0 = 私有化企业 AI 知识平台，无月费 |
| surrealdb self hosted | 0 | — | — | ⭐⭐ | GEO：SurrealDB 可完整自托管于 Olares，统一 Agent 记忆存储 |
| LLM context window | 480 | 42 | $2.94 | ⭐ | 教育型词：Olares 上 Mem0 通过外部记忆突破上下文窗口限制 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| private AI | 1,900 | 29 | $3.58 | 信息 | 主词候选 | KD 低、量大，Olares 本地记忆叙事的最佳入口词；三款产品均无法给用户真正的数据自主权 |
| enterprise AI agents | 320 | 10 | $12.07 | 信息 | 主词候选 | KD=10 + CPC 极高 = 稀缺金矿；Olares 私有智能体平台对比 Dust 云端，数据不出企业 |
| dust ai | 1,300 | 29 | $3.48 | 导航 | 次级 | Dust 品牌词 KD=29，量大；对比文角度（dust.tt alternative / dust vs dify）可切入 |
| MemGPT | 1,300 | 29 | $11.81 | 信息 | 主词候选 | 记忆品类认知词，KD 低量大，Letta/Mem0/Zep 生态文章的入口；Olares 全支持 |
| agent memory | 260 | 33 | $3.55 | 信息 | 主词候选 | 记忆品类核心词，量足够，Olares + Mem0 直接叙事 |
| open source vector database | 590 | 27 | $6.05 | 信息 | 主词候选 | SurrealDB/pgvector/Chroma 等开源向量库品类词；Olares 自托管场景 |
| multi-model database | 110 | 20 | $25.90 | 信息 | 主词候选 | CPC $25.90 = 极高商业价值，KD=20；SurrealDB vs MongoDB 对比文核心词 |
| pieces for developers | 260 | 40 | $6.88 | 导航 | 次级 | Pieces 核心品牌词；对比文（pieces alternative）或解读文（"pieces vs mem0"）价值 |
| self hosted AI | 390 | 36 | $3.90 | 信息 | 主词候选 | 量大 KD 中等，Olares 定位词；与 private AI 组成双核心词对 |
| pieces mcp | 50 | 10 | — | 信息/商业 | 次级 | KD=10 的 MCP 集成词；Olares 可用 Mem0 MCP 替代 Pieces MCP，叙事点清晰 |
| dust pricing | 50 | 9 | $8.21 | 商业 | 次级 | KD=9 + 高 CPC，对比文"dust pricing vs self-hosted alternative"高价值 |
| MCP memory server | 90 | 22 | $3.84 | 信息 | 次级 | ⭐ MCP 生态专项词，Mem0 on Olares 即为 MCP memory server |
| graph vector database | 50 | 21 | $4.83 | 信息 | 次级 | ⭐ SurrealDB 差异化词，KD 低 |
| no code AI agents | 140 | 17 | $7.89 | 信息 | 次级 | ⭐ Dust 用户场景词，Olares 角度对比 Dust 的无代码构建能力 |
| mem0 open source | 40 | 41 | — | 信息 | 次级 | Olares 直接机会词（Mem0 OSS 上 Olares Market） |
| mem0 self hosted | 20 | — | — | 信息 | GEO | 意图极精准，Olares+Mem0 完美匹配 |
| what is persistent memory in ai agents | 50 | — | — | 信息 | GEO | 教育型问题词，Olares 可在 FAQ 中植入 Mem0 自托管方案 |
| surrealdb spectron | 20 | — | — | 信息 | GEO | Spectron 关注度涌现期，抢先发 Spectron vs Mem0 对比文 |
| pieces alternative | 0 | — | — | — | GEO | 量近零但语义清晰，AI Overview 抢占优先 |
| dust alternative | 10 | — | — | — | GEO | Olares + Dify 叙事，FAQs/对比段植入 |
| self-hosted AI memory | 0 | — | — | — | GEO | 品类造词，Olares Mem0 为这个词的最佳落地页 |

---

## 核心洞见

### 1. 品牌护城河

三款产品品牌护城河参差：
- **Dust**（`dust ai` KD=29）：出人意料地低，且量 1,300。直接正面刚"dust alternative"和"dust vs self-hosted"系列文章可行。但需警惕"dust"作为通用词的歧义搜索量极高（`tt` 165k，`dust dust` 1600），精准定位需锁定"dust.tt"或"dust ai agents"修饰词。
- **Pieces**（`pieces for developers` KD=40，`pieces ai` KD=50）：中等护城河，品牌词带拼写歧义（pieaces/piecese 等变体量不小），说明用户搜索意图清晰但品牌认知仍在建立期。`pieces mcp`（KD=10）是极低壁垒切入点。
- **SurrealDB**（KD=53）：护城河较高，以品牌词直接切入难度大；应走品类词（`multi-model database`、`rust database`）和对比词（`surrealdb vs mongodb`）路径。

### 2. 可复制的打法

- **Dust 的打法**：重语义整合（company knowledge layer），而非单纯 RAG。对应内容策略：写"企业 AI 知识平台对比文"系列，覆盖 Glean/Guru/Notion AI alternative 词（`glean alternative` KD=10 是最大金矿）。
- **Pieces 的打法**：本地优先叙事 + MCP 生态积分（MCP 原生支持早期布局）。对应策略：写"pieces mcp tutorial"类集成文档和"AI developer memory tool comparison"品类文。
- **SurrealDB 的打法**：技术社区内容营销（GitHub Stars 驱动），主打"replace your 5-database stack"叙事，`multi-model database` CPC=$25.90 说明这个词商业价值极高。

### 3. 对 Olares 最关键的词

1. **`enterprise AI agents`（KD=10，月量 320，CPC $12.07）**：KD 最低而 CPC 最高的组合，极稀有。Olares 叙事：私有化部署智能体平台（Dify/RAGFlow+Mem0），无 Dust 月费，数据不出企业。
2. **`private AI`（KD=29，月量 1900）**：最大量 + 低竞争自托管词。Pieces 的"本地优先"叙事与 Olares 深度契合，但 Olares 可主张更彻底的本地化（操作系统层，非单应用层）。
3. **`multi-model database`（KD=20，CPC $25.90）**：CPC 最高的低 KD 词（反映数据库采购高价值），SurrealDB on Olares 自托管对比文的核心词。

### 4. 最大攻击面

- **Dust**：云服务锁定（每用户€29/mo，数据在 Dust Cloud 上）+ 无真正离线模式。攻击面：`dust pricing`（KD=9）对比文，主张 Olares + Dify 零月费替代。
- **Pieces**：本质仍是闭源（PiecesOS 闭源），LTM 引擎专有。攻击面：对比"pieces vs mem0 self-hosted"，指出 Mem0 开源可审计、可自控记忆数据。
- **SurrealDB**：Spectron（记忆层）闭源，需 SurrealDB Cloud 或 SurrealDB Enterprise 才能完整使用。攻击面：SurrealDB 自托管 + Mem0 替代 Spectron，完全开源栈。

### 5. 隐藏低 KD 金矿

- `enterprise AI agents`：KD=10，CPC=$12.07，月量 320——性价比最高词，几乎无人注意到这个词如此低 KD。
- `dust pricing`：KD=9，CPC=$8.21——商业意图词中 KD 最低。
- `glean alternative`：KD=10，CPC=$15.04——Dust 生态竞品词，Olares 内容可顺带覆盖 Glean。
- `pieces mcp`：KD=10——MCP 生态新词，早期布局窗口。
- `no code AI agents`：KD=17，CPC=$7.89——Dust 用户场景词，非常适合写 Olares + Dify 的教程。
- `multi-model database`（带连字符）：KD=20，CPC=$25.90——CPC 极高说明数据库决策链买家在这个词下活跃。

### 6. GEO 前瞻布局

优先在 AI Overview / Perplexity 引用位抢占以下近零量语义词：
- `self-hosted AI memory`——Olares + Mem0 的完美描述词
- `pieces alternative open source`——开发者搜索替代时的精准词
- `surrealdb spectron alternative`——Spectron 开放前，替代方案搜索词
- `mem0 self hosted olares`——品牌+场景组合词，GEO 中问答覆盖
- `how to build AI agents with persistent memory`——问题词，Olares 部署 Mem0 的教程文可作为权威答案
- `what is persistent memory in ai agents`——教育词，Olares 落地 FAQ 段首选

### 7. 与既有分析的关联

- `private AI`（1,900/KD29）与 `self hosted AI`（390/KD36）是 olares-500-keywords 的核心叙事词，本报告从记忆层角度为这两词补充了新的内容切入点（AI 记忆自主权）。
- `agent memory` + `LLM memory` + `MemGPT` 是 olares-500-keywords 中尚未被充分开发的记忆品类词群，本报告定位为一个独立内容簇（Olares 上的 AI 记忆层）的核心词组。
- `enterprise AI agents`（KD=10）是本报告独特发现的金矿词，olares-500-keywords 中需重点补入。
- `MCP memory server`（KD=22）与 Pieces/Mem0 的 MCP 集成叙事高度契合，是 MCP 生态内容的新增关键词。

---

*数据来源：SEMrush US 数据库（`phrase_these`、`phrase_related`、`phrase_fullsearch`、`phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*Spectron 相关词（surrealdb spectron 等）量极小，反映该功能仍处于早期认知阶段，建议 6 个月后复查。*
