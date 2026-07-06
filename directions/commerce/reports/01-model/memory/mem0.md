# Mem0 SEO 竞品分析报告

> 域名：mem0.ai | SEMrush US | 2026-07-06
> Mem0 = Agent 持久记忆层（Memory-as-a-Service）——开源 SDK（Apache 2.0）+ 托管 API 双形态，AI agent 领域最接近"纯 memory 初创"的公司，融资 $24M

---

## 项目理解（前置）

Mem0（读作"mem-zero"）是一个面向 AI agent 与 LLM 应用的智能持久记忆层。它在每次对话后自动提取、压缩和存储关键事实，在后续交互时精准检索注入 prompt，使 AI agent 能跨会话记住用户偏好和上下文——同时大幅减少 token 消耗（只传入相关记忆而非完整历史）。三种使用形态：Python/TypeScript 库（本地开发）、自托管服务器（Docker Compose，FastAPI + PostgreSQL/pgvector + Neo4j）、托管云 API（app.mem0.ai）。YC-backed，2025 年 10 月完成 $24M 融资（$3.9M 种子 + $20M A 轮，Basis Set Ventures 领投）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AI agent 持久记忆层：跨会话记忆管理，降 token 成本，支持开源自托管或托管 API |
| 开源 / 许可证 | ✅ Apache 2.0 |
| 主仓库 | [github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)（★ 60K+，Fork 7K+，355 次发布，v2.0.11） |
| 核心功能 | 自动记忆提取与压缩；向量 + 知识图谱双存储（Qdrant/pgvector + Neo4j）；user_id / agent_id / run_id 三级隔离；多框架集成（LangChain / CrewAI / LlamaIndex）；MCP 服务器支持 |
| 商业模式 / 定价 | Hobby 免费（10K 存/1K 取）；Starter $19/mo（50K/5K）；Growth $79/mo（200K/20K）；Pro $249/mo（500K/50K + 图谱 + 无限项目）；Enterprise 定制 + 私有部署 + SSO |
| 差异化 / 价值主张 | 最大社区（60K★）+ 最全集成生态；三形态覆盖所有部署需求；SOC 2 Type 1 + HIPAA 合规；AWS Agent SDK 独家 memory 合作方 |
| 主要竞品（初判）| Zep（专注 agent 记忆图谱）、Letta（有状态 agent 框架）、Cognee（知识图谱 memory）、LangMem（LangChain 官方 memory 扩展） |
| Olares Market | 未上架（`mem0.ai` 仅托管版；开源 SDK 可 Olares 自托管）|
| 来源 | [mem0.ai](https://mem0.ai)、[github.com/mem0ai/mem0](https://github.com/mem0ai/mem0)、[docs.mem0.ai](https://docs.mem0.ai)、[rywalker.com/research/mem0](https://rywalker.com/research/mem0) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | mem0.ai |
| SEMrush Rank | **223,673**（成长期，品牌认知建立中） |
| 自然关键词数 | 2,055 |
| 月自然流量（US）| 7,781 |
| 自然流量估值 | $30,618/月 |
| 付费关键词数 | 0（未投 Google Ads） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 56 词 |
| 排名 4-10 位 | 496 词 |
| 排名 11-20 位 | 458 词 |

> 流量结构特征：品牌词（mem0 系列）占据绝对主导；但 blog 区贡献了大量非品牌流量——**claude 定价系列文章**（claude pricing / claude plans / claude code pricing 等）持续引流，属于"竞品定价内容钩子"打法，显示 Mem0 正在用高 CPC 的 AI 工具定价词扩大顶部流量漏斗。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| mem0.ai（主站） | 1,732 | 6,646 | 85.41% |
| docs.mem0.ai | 316 | 1,101 | 14.15% |
| app.mem0.ai | 5 | 33 | 0.42% |
| twitter.mem0.ai | 1 | 1 | 0.01% |
| chrome.mem0.ai | 1 | 0 | 0.00% |

> docs 子域贡献 14% 流量，说明文档 SEO 已初具规模，但仍有很大提升空间。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| mem0 | 2 | 6,600 | 53 | $4.61 | 871 | 品牌 | mem0.ai/ |
| longmemeval leaderboard | 2 | 5,400 | 32 | $0 | 712 | 信息 | blog/ai-memory-benchmarks-in-2026 |
| claude pricing | 7 | 22,200 | 57 | $8.54 | 532 | 商业 | blog/anthropic-claude-pricing |
| mem0（docs）| 4 | 6,600 | 53 | $4.61 | 429 | 品牌 | docs.mem0.ai/introduction |
| claude plans | 7 | 9,900 | 60 | $9.14 | 297 | 信息/商业 | blog/anthropic-claude-pricing |
| mem0（platform overview）| 6 | 6,600 | 53 | $4.61 | 231 | 品牌 | docs.mem0.ai/platform/overview |
| mem | 8 | 27,100 | 78 | $1.92 | 189 | 信息 | mem0.ai/ |
| mem0 ai | 1 | 210 | 56 | $3.62 | 168 | 品牌 | mem0.ai/ |
| anthropic claude pro pricing | 7 | 6,600 | 45 | $0 | 158 | 商业 | blog/anthropic-claude-pricing |
| memory ai | 1 | 590 | 62 | $3.41 | 146 | 信息 | mem0.ai/ |
| claude price | 4 | 3,600 | 35 | $8.54 | 126 | 商业 | blog/anthropic-claude-pricing |
| how much does claude cost | 4 | 2,400 | 25 | $5.05 | 84 | 信息 | blog/anthropic-claude-pricing |
| claude code pricing | 11 | 18,100 | 60 | $4.68 | 72 | 商业 | blog/anthropic-claude-pricing |
| claude pricing plans | 5 | 1,900 | 65 | $7.79 | 66 | 商业 | blog/anthropic-claude-pricing |
| memory user | 1 | 260 | 23 | $0 | 64 | 信息 | docs/core-concepts/memory-types |
| mem0 agno integration | 1 | 260 | 20 | $0 | 64 | 信息 | docs/integrations/agno |
| openmemory | 2 | 480 | 21 | $0 | 63 | 导航 | mem0.ai/openmemory |
| open memory | 2 | 480 | 33 | $0 | 63 | 信息 | mem0.ai/openmemory |
| grok pricing | 8 | 2,900 | 32 | $3.75 | 63 | 商业 | blog/xai-grok-api-pricing |
| claude code plans | 8 | 2,400 | 43 | $9.12 | 57 | 信息 | blog/anthropic-claude-pricing |
| mem0 mcp | 1 | 210 | 23 | $0 | 52 | 信息/商业 | docs/platform/mem0-mcp |
| claude ai pricing | 5 | 8,100 | 44 | $4.59 | 48 | 商业 | blog/anthropic-claude-pricing |
| grok api | 12 | 6,600 | 49 | $5.03 | 46 | 信息 | blog/xai-grok-api-pricing |
| mem0 open source | 1 | 40 | 41 | $0 | 32 | 信息/商业 | docs/open-source/overview |
| openmemory mcp | 2 | 260 | 27 | $0 | 34 | 信息 | mem0.ai/openmemory |
| grok api pricing | 4 | 1,000 | 19 | $7.16 | 30 | 信息 | blog/xai-grok-api-pricing |
| memory types | 5 | 1,000 | 46 | $0 | 30 | 信息 | docs/core-concepts/memory-types |
| claude code memory | 7 | 880 | 26 | $26.28 | 26 | 信息/商业 | blog/how-memory-works-in-claude-code |
| mem0 funding | 1 | 90 | 34 | $0 | 22 | 信息 | mem0.ai/series-a |
| memzero | 2 | 170 | 49 | $0 | 22 | 品牌 | mem0.ai/ |
| mem0 openclaw | 1 | 90 | 24 | $0 | 22 | 信息/商业 | docs/integrations/openclaw |
| ai memory | 2 | 720 | 53 | $3.88 | 25 | 信息 | mem0.ai/ |
| mem0 api | 1 | 50 | 35 | $0 | 40 | 商业 | docs/api-reference |
| mem0 pricing | 1 | 50 | 22 | $5.08 | 40 | 商业 | mem0.ai/pricing |
| claude code memory | 7 | 880 | 26 | $26.28 | 26 | 信息/商业 | blog/how-memory-works-in-claude-code |

> **blog 的"定价内容钩子"**：`claude pricing`、`claude plans`、`grok pricing` 等高 CPC 词来自 Mem0 博客发布的第三方 AI 定价分析文章——用竞品词引流，再转化为 Mem0 平台用户。每篇文章流量估值达数千美元/月，是小型 AI 初创的典型流量杠杆策略。

### 付费词（Google Ads）

Mem0 当前**零付费广告投入**，完全依赖自然搜索和内容营销。对 Olares 来说，这意味着竞品词 CPC 未被 Mem0 主动推高。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| chatgpt memory | 1,300 | 59 | $0 | 信息 | ChatGPT 记忆功能相关，需求量大 |
| cognee | 880 | 35 | $2.66 | 导航 | 知识图谱 memory 竞品 |
| langmem | 590 | 31 | $0 | 信息/商业 | LangChain 官方 memory 扩展 |
| langchain memory | 590 | 32 | $0 | 信息 | 框架内置记忆方案 |
| openmemory | 480 | 21 | $0 | 导航 | ⭐ Mem0 自家开源平台（已排名 #2）|
| zep memory | 260 | 40 | $2.67 | 信息/导航 | 直接竞品 Zep |
| crewai memory | 110 | 14 | $0 | 信息 | ⭐ CrewAI 内置记忆，框架选型词 |
| mem0 vs zep | 10 | 0 | $0 | 信息 | ⭐ 直接对比词，极低 KD |
| letta memory | 50 | 0 | $10.52 | 信息 | ⭐ Letta 框架记忆，高 CPC |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai agent memory | 110 | 53 | $4.31 | 信息 | 品类核心词，竞争中等 |
| mcp memory | 320 | 23 | $3.81 | 信息 | ⭐ MCP 记忆协议，快速增长词 |
| ai memory | 720 | 53 | $3.88 | 信息 | 品类大词，Mem0 已排 #2 |
| memory ai | 590 | 62 | $2.72 | 信息 | Mem0 已排 #1（docs 词） |
| agent memory | 260 | 33 | $3.55 | 信息 | ⭐ 低 KD 品类词 |
| agentic memory | 210 | 36 | $4.35 | 信息 | 新兴品类术语 |
| ai memory layer | 40 | 41 | $0 | 信息 | 品类细分描述词 |
| memory as a service | 20 | 0 | $5.53 | 信息 | ⭐ Mem0 商业模式词 |
| longmemeval leaderboard | 5,400 | 32 | $0 | 信息 | ⭐ Mem0 已排 #2，benchmark 场 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| mem0 | 6,600 | 53 | $4.61 | 品牌 | 核心品牌词，Semrush #2 |
| mem0 ai | 210 | 56 | $3.62 | 品牌 | 已排 #1 |
| mem0 mcp | 210 | 17 | $4.91 | 信息/商业 | ⭐ 已排 #1，极低 KD 高 CPC |
| openmemory mcp | 260 | 27 | $0 | 信息 | ⭐ Mem0 开源 MCP 产品词 |
| mem0 open source | 40 | 41 | $0 | 信息/商业 | 开源版路径词，已排 #1 |
| mem0 agno integration | 260 | 20 | $0 | 信息 | ⭐ 集成词，已排 #1 |
| mem0 openclaw | 90 | 24 | $0 | 信息/商业 | ⭐ 编辑器集成词 |
| mem0 pricing | 50 | 22 | $5.08 | 商业 | ⭐ 已排 #1，高 CPC |
| mem0 api | 50 | 35 | $0 | 商业 | 开发者功能词，已排 #1 |
| mem0 funding | 90 | 34 | $0 | 信息 | 融资新闻词，已排 #1 |
| mem0 github | 480 | 51 | $0 | 导航/商业 | GitHub 导航词 |
| mem0 python | 30 | 0 | $0 | 信息 | ⭐ 教程类词 |
| mem0 tutorial | 20 | 0 | $0 | 信息 | ⭐ 教程类词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open memory | 480 | 33 | $0 | 信息 | ⭐ Mem0 已排 #2，开源记忆叙事词 |
| openmemory | 480 | 21 | $0 | 导航 | ⭐ Mem0 开源平台词，自托管路径 |
| mem0 open source | 40 | 41 | $0 | 信息/商业 | 开源文档入口 |
| self-hosted ai memory | 0 | 0 | $0 | — | GEO 前哨：近零量但语义精准 |
| open source ai memory | 10 | 0 | $0 | 信息 | ⭐ 极低 KD，机会词 |
| agent memory open source | 0 | 0 | $0 | — | GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心叙事切入**：Mem0 开源版（Apache 2.0）可通过 Docker Compose 完整自托管，Olares 作为 Personal Cloud OS 可一键承载整套 FastAPI + pgvector + Neo4j 栈，为本地 AI Agent 提供完全属于用户自己的私有记忆层——数据不出设备，告别云端 API credits 消耗，与 Letta / Cognee 形成"开源 memory 全家桶"叙事。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| openmemory | 480 | 21 | $0 | Mem0 官方开源平台（OpenMemory），Olares 可直接一键部署整套自托管栈 | ⭐⭐⭐ |
| open memory | 480 | 33 | $0 | 同上，Olares 承载本地 memory dashboard + API | ⭐⭐⭐ |
| mem0 open source | 40 | 41 | $0 | Olares + Mem0 开源版 = 个人 AI 记忆基础设施教程核心词 | ⭐⭐⭐ |
| self-hosted ai memory | 0 | 0 | $0 | GEO：Olares 自托管 AI 记忆层，抢 AI Overview 引用位 | ⭐⭐⭐ |
| ai agent memory | 110 | 53 | $4.31 | Olares 上的本地 AI agent（Dify/n8n）+ Mem0 记忆层组合 | ⭐⭐⭐ |
| mcp memory | 320 | 23 | $3.81 | Mem0 MCP server 可在 Olares 上自托管，供 Claude/Cursor 等调用 | ⭐⭐⭐ |
| mem0 mcp | 210 | 17 | $4.91 | Olares 托管 Mem0 MCP 服务，为 AI 编辑器提供本地记忆 | ⭐⭐⭐ |
| agent memory | 260 | 33 | $3.55 | Olares 上跑本地 agent（n8n/AutoGPT）+ Mem0 持久记忆 | ⭐⭐⭐ |
| crewai memory | 110 | 14 | $0 | CrewAI + Mem0 on Olares：本地多智能体记忆方案 | ⭐⭐⭐ |
| open source ai memory | 10 | 0 | $0 | Olares Market 可集成 Mem0 开源版教程词 | ⭐⭐⭐ |
| mem0 vs zep | 10 | 0 | $0 | 对比词：两者均可在 Olares 上自托管，Olares = 两者的部署平台 | ⭐⭐ |
| letta memory | 50 | 0 | $10.52 | Letta 也是 Olares 平替候选，高 CPC 显示商业价值 | ⭐⭐ |
| langchain memory | 590 | 32 | $0 | LangChain + Mem0 on Olares：Python 开发者本地 AI stack | ⭐⭐ |
| agentic memory | 210 | 36 | $4.35 | Olares 作为 agent-native OS，内置/集成 agentic memory 叙事 | ⭐⭐ |
| memory as a service | 20 | 0 | $5.53 | Olares 把 Mem0 "服务化"到个人私有云，去中心化 MaaS | ⭐⭐ |
| agent memory open source | 0 | 0 | $0 | GEO：Olares + Mem0 开源版 = 个人私有 agent 记忆层 | ⭐⭐ |
| longmemeval leaderboard | 5,400 | 32 | $0 | Mem0 主导的 benchmark，可引用支撑 Olares 上 AI memory 质量叙事 | ⭐ |
| chatgpt memory | 1,300 | 59 | $0 | 类比叙事：Olares + Mem0 = 你自己的 ChatGPT Memory，数据本地 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| chatgpt memory | 1,300 | 59 | $0 | 信息 | 主词候选 | 量最大的 memory 信息词；KD 59 偏高但内容可切"ChatGPT memory vs Mem0 self-hosted"角度；Olares 叙事：自己的私有 ChatGPT Memory |
| mcp memory | 320 | 23 | $3.81 | 信息 | 主词候选 | ⭐ KD 低、量适中、CPC 不低；MCP 协议与 Mem0 MCP 结合是高热度趋势词；Olares 上自托管 Mem0 MCP server |
| openmemory | 480 | 21 | $0 | 导航 | 主词候选 | ⭐ Mem0 官方开源 memory 平台词，KD 极低；Olares 一键部署 OpenMemory 是最直接的机会 |
| open memory | 480 | 33 | $0 | 信息 | 主词候选 | ⭐ 与 openmemory 近似词，KD 低量可观；Olares 承载开放记忆层叙事 |
| ai agent memory | 110 | 53 | $4.31 | 信息 | 主词候选 | 品类核心词，量+CPC 均可观；Olares agent-native OS 叙事的核心支撑词 |
| agent memory | 260 | 33 | $3.55 | 信息 | 主词候选 | ⭐ KD 低、量中等、CPC 较高，是"self-hosted agent memory"的根词 |
| longmemeval leaderboard | 5,400 | 32 | $0 | 信息 | 主词候选 | ⭐ Mem0 已排 #2，这是 AI memory benchmark 领域的制高点词；量大 KD 低组合极佳 |
| langchain memory | 590 | 32 | $0 | 信息 | 主词候选 | ⭐ 量中等 KD 低，框架生态词；Olares + LangChain + Mem0 Python stack 教程 |
| agentic memory | 210 | 36 | $4.35 | 信息 | 次级 | 新兴术语，量还小；Olares agent-native 叙事支撑词 |
| crewai memory | 110 | 14 | $0 | 信息 | 次级 | ⭐ KD 极低，框架内置词；Olares 上 CrewAI + Mem0 本地化教程 |
| mem0 mcp | 210 | 17 | $4.91 | 信息/商业 | 次级 | ⭐ Mem0 自有词已排 #1；但作为 Olares "MCP on Personal Cloud" 叙事补充词价值高 |
| openmemory mcp | 260 | 27 | $0 | 信息 | 次级 | ⭐ 品牌功能词，Olares 托管 MCP 服务场景 |
| mem0 open source | 40 | 41 | $0 | 信息/商业 | 次级 | 自托管路径入口词，量小但 Olares 场景完全契合 |
| letta memory | 50 | 0 | $10.52 | 信息 | 次级 | ⭐ KD 0、高 CPC，Letta 作为 Mem0 的 Olares 平替之一，高价值对比词 |
| mem0 vs zep | 10 | 0 | $0 | 信息 | 次级 | ⭐ 对比词，KD 0；Olares 同时托管两者的内容切入点 |
| self-hosted ai memory | 0 | 0 | $0 | — | GEO | 语义精准、近零量；Olares 自托管 AI 记忆层，抢 AI Overview/Perplexity 引用位 |
| agent memory open source | 0 | 0 | $0 | — | GEO | 同上，Olares + Mem0 开源版核心叙事 |
| memory as a service | 20 | 0 | $5.53 | 信息 | GEO | 商业模式术语词，抢引用位；Olares = 个人私有 MaaS |
| open source ai memory | 10 | 0 | $0 | 信息 | GEO | ⭐ 极低 KD，Olares Market 集成叙事前哨 |
| how to build ai agents with memory | 0 | 0 | $0 | 信息 | GEO | 问题型 GEO 词；"Olares + Mem0 + n8n" 教程锚点 |

---

## 核心洞见

1. **品牌护城河**：mem0 品牌词已建立中等认知（KD 53，月量 6,600），但排名 #2（#1 是 GitHub 仓库），说明品牌锁定尚不稳固。不适合正面刚品牌词；**关键词攻击面应在"品类词 + 开源信号词"**，Mem0 自己在这些词上投入不足。

2. **可复制的打法**：Mem0 博客用**"竞品 AI 工具定价内容"**钩流量（claude pricing / grok pricing 等高 CPC 词），是 SEO 流量杠杆策略的经典操作——单篇文章月估值数千美元。此外，它通过 `longmemeval leaderboard`（月量 5,400，KD 32）占据 AI memory benchmark 的内容高地，建立行业权威。这两种打法可复制。

3. **对 Olares 最关键的词**：
   - **`openmemory` / `open memory`**（480 量，KD 21/33）：Mem0 官方开源平台产品词，KD 极低，Olares 一键部署 OpenMemory 的最直接内容机会；
   - **`mcp memory` / `mem0 mcp`**（320/210 量，KD 23/17）：MCP 记忆协议是 2026 年最热 AI 工具趋势，Olares 托管 Mem0 MCP server 为 AI 编辑器（Claude Code/Cursor）提供本地记忆层是极强的场景叙事；
   - **`agent memory`**（260 量，KD 33，CPC $3.55）：Olares agent-native OS + Mem0 持久记忆的核心品类词，竞争适中。

4. **最大攻击面**：Mem0 的**定价台阶**（免费→$19→$79→$249）是核心痛点——特别是 Pro 才开放 Graph Memory（$249/月），且 API credits 上限令人沮丧。Olares 上的 Mem0 开源版全功能零 credits，是"用户拥有自己的记忆层"最强叙事。另一攻击面：Mem0 托管版**数据主权问题**（SOC2/HIPAA 合规说明数据在云端），对隐私敏感用户（医疗、法律、个人 AI）是天然缺口。

5. **隐藏低 KD 金矿**：
   - `crewai memory`（110 量，**KD 14**）：CrewAI 是热门 multi-agent 框架，Mem0 是其最常配对的 memory 层，KD 极低；
   - `mem0 mcp`（210 量，**KD 17**，CPC $4.91）：已是产品词但有更大内容空间；
   - `letta memory`（50 量，KD 0，CPC $10.52）：竞品词但 KD 为零、CPC 极高，显示高商业价值需求；
   - `longmemeval leaderboard`（**5,400 量，KD 32**）：量大 KD 低罕见组合，Mem0 已排 #2 说明可争第一，且可以此为锚写"AI memory benchmark 2026"权威内容。

6. **GEO 前瞻布局**：`self-hosted ai memory`、`agent memory open source`、`how to build ai agents with memory`、`how to add memory to ai agent`——这些近零量词正是 AI Overview / Perplexity 被高频问的问题，提前布局可抢引用位。Olares 叙事：在个人云上用 Mem0 开源版构建私有 agent 记忆基础设施。

7. **与既有分析的关联**：olares-500-keywords 中无 memory 相关词，本报告为 Olares 补充了**AI agent 基础设施**这一新词域——尤其是 `mcp memory`、`openmemory`、`agent memory` 等新兴词，与 Olares agent-native OS 品牌升级方向高度契合。`mem0 mcp` 的 MCP 协议词群（mcp memory 320量/KD23）是本次研究中发现的最具战略价值的新词族。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_related、phrase_these、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
