# MemPalace SEO 竞品分析报告

> 域名：mempalaceofficial.com | SEMrush US | 2026-07-06
> 本地优先的 AI 记忆系统：语义向量检索 + MCP 服务器，零 API 调用，LongMemEval 96.6% R@5

---

## 项目理解（前置）

MemPalace 是一个本地优先的 AI 会话记忆系统：将对话历史以**逐字原文**方式存储，再用语义向量检索召回。它不摘要、不改写——所有内容保持原话，检索由向量引擎完成。结构上把数据组织成 Wing（人/项目）→ Room（日期/会话）→ Closet（话题）→ Drawer（逐字块）的空间层级，并在层级之上维护一个 SQLite 知识图谱记录实体关系与时间线。对外暴露 35 个 MCP 工具，可直接挂进 Claude Code、Gemini CLI、Cursor、Antigravity 等任何 MCP 客户端，实现零配置持久记忆。

2026 年 4 月创建，截至 2026-07-06 已获 **56,890 GitHub Stars**（短短 3 个月成为 AI 记忆开源生态最高 Star 项目），最新版本 v3.5.0（2026-06-23）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 本地优先 AI 记忆 + MCP 服务器，零 API，逐字存储，语义搜索 |
| 开源 / 许可证 | 是，MIT License |
| 主仓库 | [github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace)（★ ~57K） |
| 核心功能 | ① 逐字存储 + 向量检索（默认 ChromaDB，可替换）② 35 个 MCP 工具 ③ SQLite 知识图谱（含时间戳关系）④ AAAK 符号索引（LLM 一次扫描定位 drawer）⑤ Claude Code hooks 自动归档 |
| 商业模式 / 定价 | 完全免费开源，pip/Docker 安装 |
| 差异化 / 价值主张 | 不做摘要/提炼 → 零 AI 幻觉注入；结构化空间检索比平铺向量库更精确；LongMemEval Hybrid v4 达 98.6% R@5（LLM rerank 99.2%），零 API 成本 |
| 主要竞品（初判）| mem0 / OpenMemory（mem0 开源版）、supermemory、MemGPT（Letta）、Zep AI |
| Olares Market | ⬜ 未上架（见 directions/market/apps.md 第 208 行） |
| 来源 | [github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace)、[mempalaceofficial.com](https://mempalaceofficial.com)、[benchmarks](https://mempalace.github.io/mempalace/reference/benchmarks) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | mempalaceofficial.com |
| SEMrush Rank | 29,508,431（极新域名，2026-04 创建） |
| 自然关键词数 | 2 |
| 月自然流量（US） | 0（Semrush 暂无法估算） |
| 自然流量估值 | $0/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 0 词 |
| 排名 4-10 位 | 0 词 |
| 排名 11-20 位 | 0 词 |

> **注**：官网流量几乎为零，这与 GitHub（56K ★）的热度形成鲜明对比——社区发现路径目前以 GitHub、PyPI、Reddit/HN 为主，SEO 几乎是空白板，机会巨大。

### 官网仅有 2 个排名词（极早期）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| mempalace | 71 | 1,600 | 35 | $10.02 | 0 | 导航 | mempalaceofficial.com/ |
| mempalace github | 35 | 590 | 44 | $7.25 | 0 | 导航 | mempalaceofficial.com/ |

> 品牌词 1,600 月量在诞生仅 3 个月后已初现，足以证明 GitHub 社区引流的力量。付费：无。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| mem0 | 5,400 | 53 | $4.61 | 信息 | 最大竞品，KD 偏高 |
| supermemory | 2,400 | 42 | $0.18 | 信息 | 竞品，KD 中等 |
| memgpt | 1,300 | 29 | $11.81 | 信息 | ⭐ KD<30，量可观 |
| openmemory | 480 | 21 | $0 | 信息 | ⭐ mem0 开源版，低 KD 金矿 |
| zep AI | 480 | 51 | $3.90 | 信息/商业 | KD 偏高 |
| mem0 github | 480 | 51 | $0 | 导航 | 高 KD，导航词 |
| mem0 mcp | 170 | 17 | $4.91 | 信息/商业 | ⭐ 极低 KD！ |
| mem0 open source | 40 | 41 | $0 | 信息/导航 | KD 中等 |
| mem0 self hosted | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨，零竞争 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| longmemeval leaderboard | 5,400 | 30 | $0 | 信息 | ⭐ **年度最佳金矿**，mem0 排 #2 |
| LongMemEval | 320 | 32 | $0 | 信息 | ⭐ 基准词 |
| memory MCP | 480 | 39 | $3.81 | 信息 | 品类核心词 |
| memory bank MCP | 320 | 16 | $0 | 信息 | ⭐ **超低 KD！** |
| mcp memory | 320 | 23 | $3.81 | 信息 | ⭐ 品类词 |
| memory MCP server | 210 | 26 | $0 | 信息 | ⭐ |
| LLM memory | 260 | 50 | $3.99 | 信息 | KD 偏高 |
| knowledge graph memory MCP | 140 | 20 | $7.23 | 信息 | ⭐ 极低 KD，精准 |
| mcp memory server | 90 | 22 | $3.84 | 信息 | ⭐ |
| LLM long term memory | 40 | 26 | $0 | 信息 | ⭐ |
| open memory MCP | 70 | 35 | $0 | 信息/导航 | 中等 KD |
| AI memory MCP | 30 | 0 | $3.98 | 信息 | ⭐ **零 KD，GEO 必抢** |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| mempalace | 1,600 | 35 | $10.02 | 导航 | 品牌词，官网排 71 |
| mempalace github | 590 | 44 | $7.25 | 导航 | GitHub 引流词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| mem0 self hosted | 20 | 0 | $0 | 信息 | ⭐ 近零竞争，精准自托管意图 |
| open source AI memory | 10 | 0 | $0 | 信息 | ⭐ GEO 词 |
| self hosted AI memory | 0 | 0 | $0 | — | 未来词，提前布局 |
| mem0 mcp server | 30 | 0 | $6.43 | 信息/商业 | ⭐ 零 KD |

---

## Olares 关联词（Phase 3）

**核心逻辑：MemPalace 是 Olares Agent-Native OS 叙事的完美搭档——本地 LLM + 本地 AI 记忆 = 完全隐私的私人 Agent，而 Olares Market 一键安装即可让任何用户拥有这套能力。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| memory MCP | 480 | 39 | $3.81 | ⭐⭐⭐ Olares Market 上的 MemPalace 是现成的 MCP memory 服务器，配合 Ollama/任意本地 LLM，无需 API Key，完全本地闭环 |
| memory bank MCP | 320 | 16 | $0 | ⭐⭐⭐ KD 16，Olares 上一键部署 MemPalace 即是 memory bank；文章可主打"build your own memory bank MCP on Olares" |
| mcp memory | 320 | 23 | $3.81 | ⭐⭐⭐ 同上，品类核心词，Olares 作为 MCP 生态宿主平台天然契合 |
| openmemory | 480 | 21 | $0 | ⭐⭐ mem0 的开源产品；可做"MemPalace vs OpenMemory：哪个自托管 AI 记忆更好？"——Olares 两者都能装 |
| memgpt | 1,300 | 29 | $11.81 | ⭐⭐ 可做"MemGPT alternative self-hosted"，引向 MemPalace + Olares |
| knowledge graph memory MCP | 140 | 20 | $7.23 | ⭐⭐⭐ MemPalace 内置知识图谱 + MCP，KD 20，Olares 一键启动 |
| mem0 mcp | 170 | 17 | $4.91 | ⭐⭐ KD 仅 17，可做"mem0 MCP vs MemPalace MCP"对比页 |
| longmemeval leaderboard | 5,400 | 30 | $0 | ⭐⭐ Olares 可建公开 LongMemEval 排行榜页，强调在本地/隐私环境下也能达到 SOTA 基准 |
| claude code memory | 880 | 26 | $26.28 | ⭐⭐ Claude Code 用户是 MemPalace 的核心受众；Olares 作为"24×7 在线服务端"跑 MemPalace，比本地启动更可靠 |
| mem0 self hosted | 20 | 0 | $0 | ⭐⭐⭐ 精准自托管意图，GEO 必抢，Olares Market 一键安装 MemPalace 对比 mem0 SaaS |
| AI memory MCP | 30 | 0 | $3.98 | ⭐⭐⭐ 零 KD GEO 词，语义精准，抢 AI Overview / Perplexity 引用位 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| longmemeval leaderboard | 5,400 | 30 | $0 | 信息 | **主词候选** | mem0 已排 #2；MemPalace 有 96.6% 原始分 + 98.6% Hybrid，可建基准对比页；Olares 可定位为"在本地/隐私环境跑 LongMemEval SOTA"的平台入口 |
| memory bank MCP | 320 | 16 | $0 | 信息 | **主词候选** | KD 仅 16，量稳定增长，搜索者已有明确 MCP 记忆需求；Olares + MemPalace 就是"turn-key memory bank MCP server" |
| mcp memory | 320 | 23 | $3.81 | 信息 | **主词候选** | 品类核心词，低竞争，可做"best MCP memory server"品类文；与 memory MCP (480/KD39) 合并一文更强 |
| memgpt | 1,300 | 29 | $11.81 | 信息 | **主词候选** | KD<30 且量破千，可做"MemGPT alternative"对比文；MemPalace 是开源、零 API 替代；Olares 一键安装 |
| memory MCP | 480 | 39 | $3.81 | 信息 | **主词候选** | 量最大的 MCP 记忆词，KD 39 可战；与 mcp memory (KD23) 合并成篇 |
| openmemory | 480 | 21 | $0 | 信息 | **主词候选** | KD 21，mem0 官方开源版；可做 MemPalace vs OpenMemory 对比文，Olares 两者都能自托管 |
| knowledge graph memory MCP | 140 | 20 | $7.23 | 信息 | **次级** | KD 20，MemPalace 知识图谱是其差异化；并入 MCP memory 篇的知识图谱小节 |
| mem0 mcp | 170 | 17 | $4.91 | 信息/商业 | **次级** | KD 17，可作 mem0 MCP vs MemPalace MCP 对比段 |
| claude code memory | 880 | 26 | $26.28 | 信息 | **次级** | 高 CPC、量 880，Claude Code 用户正在找持久记忆方案；MemPalace 专为 Claude Code hooks 设计；Olares 提供 7×24 服务端 |
| LongMemEval | 320 | 32 | $0 | 信息 | **次级** | 与 longmemeval leaderboard 主词并入同一篇；标注 MemPalace 基准分 |
| mcp memory server | 90 | 22 | $3.84 | 信息 | **次级** | 并入 MCP memory 簇 |
| memory MCP server | 210 | 26 | $0 | 信息 | **次级** | 并入 MCP memory 簇 |
| mem0 self hosted | 20 | 0 | $0 | 信息 | **GEO** | 零竞争，Olares Market 自托管 MemPalace vs mem0 SaaS；抢 AI 搜索引用位 |
| AI memory MCP | 30 | 0 | $3.98 | 信息 | **GEO** | 零 KD 语义精准词，进 FAQ 或专题段抢 AI Overview |
| mem0 mcp server | 30 | 0 | $6.43 | 信息/商业 | **GEO** | 零 KD，竞争真空；对比段即可收割 |
| self hosted AI memory | 0 | 0 | $0 | — | **GEO** | 目前无量，但意图语义完全符合 Olares 叙事，提前布局 GEO |

---

## 核心洞见

1. **品牌护城河**：MemPalace 品牌词（mempalace, 1,600/KD35）仍是蓝海——官网才排 71 位，没有规模竞争者占据品牌词。可优先夯实官网 SEO 基础，同时在 GitHub README 增加指向官网的结构化锚文本。不建议正面刚 mem0（5,400/KD53）品牌词，差距太大；而应攻其开源弱点（openmemory/KD21、mem0 mcp/KD17）。

2. **可复制的打法**：mem0.ai 最值得学习的是"大 CPC 博文"策略——它用 claude pricing、anthropic pricing 等高 CPC 博文拉来商业意图流量，再转化为 mem0 用户。MemPalace/Olares 可复制：写 claude code memory、claude code hooks（880/KD26）等 Claude Code 用户高需求词，内嵌 MemPalace 作为解决方案。另一个可复制打法：mem0 建了 longmemeval leaderboard 页面（排 #2），MemPalace 在基准上优于 mem0，完全可以建立一个更全面的基准对比页超越它。

3. **对 Olares 最关键的词**：
   - **`memory bank MCP`**（320/KD16）：最低 KD 的大量词，完美描述 Olares + MemPalace 的组合价值——"一键部署你自己的 MCP 记忆银行"
   - **`longmemeval leaderboard`**（5,400/KD30）：量最大的可争词，且 MemPalace 基准成绩优于 mem0；Olares 作为"在你自己的设备上跑 SOTA 记忆系统"的叙事入口
   - **`mcp memory` + `memory MCP` 簇**（800/KD23-39 合计）：品类进入词，Olares 作为 MCP 生态宿主

4. **最大攻击面**：mem0 免费版有请求限制，企业版收费；OpenMemory 自托管版功能受限；supermemory 是 SaaS，数据不在用户侧。**MemPalace + Olares 的叙事切点**：完全本地、零 API 成本、零数据出境、永久免费。关键词口径："self-hosted AI memory"、"mem0 self hosted alternative"、"zero API memory MCP"。

5. **隐藏低 KD 金矿**：
   - `memory bank MCP`：KD 16，月量 320，没有明显竞争者占据 #1
   - `knowledge graph memory MCP`：KD 20，月量 140，MemPalace 内置知识图谱 + MCP 完美匹配
   - `openmemory`：KD 21，月量 480，mem0 开源版关注者与 MemPalace 目标用户高度重叠
   - `mem0 mcp`：KD 17，月量 170，搜索者正在寻找 MCP 记忆方案，MemPalace 是直接替代

6. **GEO 前瞻布局**：
   - `AI memory MCP`（30/KD0）：精准语义，进 FAQ 抢 AI Overview 引用位
   - `self-hosted AI memory`（0/KD0）：意图完全吻合，量将随"本地 AI"趋势增长
   - `mem0 self hosted`（20/KD0）：商业意图，零竞争，Olares Market 安装教程可直接收割
   - `local AI memory`：同上趋势词，现在布局 6 个月后收益

7. **与既有分析的关联**：olares-500-keywords 词表中**无任何 AI 记忆相关词**，本报告全部为新增。MemPalace 代表的 AI 记忆 / MCP 记忆层是 Olares Agent-Native OS 叙事最直接的内容落点——用户凭什么选择在 Olares 上跑 AI Agent？因为 Olares 上有 MemPalace 给 Agent 提供持久、本地、隐私的记忆。这是一条尚未有人占据的语义通道。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、phrase_this × 20+次调用、phrase_fullsearch × 3、phrase_related × 1、phrase_questions × 1、domain_organic_organic）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
