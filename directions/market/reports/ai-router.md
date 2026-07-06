# AI Router SEO 竞品分析报告（场景词分析，无独立官网）

> 域名：无独立官网（Olares 一方应用）| SEMrush US | 2026-07-06
> AI Router 是 Olares 官方出品的 LLM 网关，在 Olares 系统内统一路由本地模型与云端 AI API。

---

## 项目理解（前置）

AI Router（应用 ID：`llmgatewayv3`）是 Olares 自研的 LLM 网关应用，直接内嵌于 Olares Market，作为 Productivity 分类下的一方应用分发。它暴露单一 OpenAI 兼容端点，将来自 Open WebUI、Dify、代码助手等前端应用的请求路由到后端——无论是 Olares 本地运行的 Ollama/vLLM/SGLang，还是 OpenAI、Anthropic、Google 等云端提供商。底层由前端（Next.js）+ 后端（Go）+ PostgreSQL 组成，镜像为 `beclab/llm-gateway-frontend:v2.0.3` / `beclab/llm-gateway-backend:v2.0.3`。源码仓库 `github.com/beclab/llm-gateway` 当前为私有，未在 GitHub 公开索引。

与同在 Olares Market 上架的同类竞品（LiteLLM、Bifrost、TensorZero）相比，AI Router 定位更偏**Olares 原生集成**：可自动发现 Olares Market 已安装的模型应用（通过内部 `appstore-svc` 接口同步提供商列表），无需手动填写端点 URL。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Olares 原生 LLM 网关——单端点路由本地模型与云端 AI 提供商 |
| 开源 / 许可证 | 源码私有（Apache-2.0 授权声明，源码仓库未公开）|
| 主仓库 | `github.com/beclab/llm-gateway`（私有，未公开 star）|
| 核心功能 | OpenAI 兼容端点；多提供商路由（Ollama/vLLM/云端）；Web UI 管理；PostgreSQL 状态持久化；Metrics 端点 |
| 商业模式 / 定价 | 随 Olares 免费；仅 admin 用户可安装（`onlyAdmin: true`）|
| 差异化 / 价值主张 | 与 Olares Market 深度集成，自动同步已安装模型应用；无需手动配置内部端点；共享安装（`shared: true`），集群内其他应用可直接访问 |
| 主要竞品（初判）| LiteLLM、Bifrost、TensorZero（均在 Olares Market 上架）；OpenRouter（云端托管）；Portkey |
| Olares Market | ✅ 已上架（`llmgatewayv3`，版本 v2.0.3）|
| 来源 | `terminus-apps/llmgatewayv3/OlaresManifest.yaml`；`olares.com/docs/use-cases/bifrost`；Olares Market UI |

---

## 关键词扩展（Phase 2）

> AI Router 无独立域名，Phase 1 域名流量基线跳过。以下直接从品类词/竞品词层面做关键词扩展。
> ⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| litellm alternative | 140 | 2 | $3.70 | info | ⭐⭐⭐ 极低 KD，强商业意图 |
| openrouter alternative | 170 | 8 | $3.35 | info | ⭐⭐⭐ KD 极低，月量可观 |
| litellm vs openrouter | 140 | 22 | $4.57 | info/comm | ⭐ 比较词，CPC 高 |
| portkey vs litellm | 30 | 10 | $3.43 | comm | ⭐ 低 KD，对比意图 |
| routellm | 590 | 40 | $1.02 | nav | RouteLLM（LMSYS 研究项目） |
| open source ai gateway | 170 | 29 | $3.71 | info | ⭐ Olares 直接机会 |
| open source llm gateway | 20 | 0 | $0 | info | ⭐ 极低 KD |
| litellm self hosted | 40 | 0 | $0 | info | ⭐ Olares 场景精准 |
| self hosted ai gateway | 20 | 0 | $4.92 | info | ⭐ 精准 Olares 场景词 |
| ai gateway self hosted | 30 | 0 | $4.92 | info | ⭐ 同上变体 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai gateway | 880 | 53 | $13.57 | info | 头部品类词，KD 高，CPC 极高 |
| llm router | 590 | 45 | $4.14 | info | 核心品类，KD 中等 |
| llm gateway | 480 | 25 | $5.63 | info | ⭐ KD 低，核心定义词 |
| ai router | 390 | 51 | $3.19 | info | 与 App 同名，KD 偏高 |
| llm proxy | 170 | 50 | $5.90 | info | KD 偏高 |
| llm routing | 170 | 52 | $4.58 | info | 技术概念词 |
| model router | 170 | 25 | $2.39 | info/nav | ⭐ KD 低 |
| ai model gateway | 30 | 30 | $9.19 | info | ⭐ 勉强入线，CPC 高 |
| llm load balancing | 20 | 0 | $6.34 | info | ⭐ 极低 KD，负载均衡场景 |
| llm gateways | 70 | 21 | $5.63 | info | ⭐ llm gateway 复数变体 |
| llm api gateway | 30 | 0 | $5.24 | info | ⭐ 极低 KD |

### 产品 / 功能词（相关品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| litellm | 14800 | 56 | $5.42 | nav | LiteLLM 品牌导航词，竞争最强 |
| openrouter | 60500 | 57 | $2.92 | nav/trans | OpenRouter 品牌词，不可正面刚 |
| portkey ai | 260 | 53 | $3.52 | nav | Portkey 品牌导航词 |
| helicone | 1300 | 36 | $4.87 | nav | 可观测平台 |
| tensorzero | 480 | 32 | $0 | nav | Olares Market 同类竞品 |
| bifrost ai gateway | 90 | 0 | $2.34 | nav | ⭐ Olares 另一原生网关品牌词 |
| litellm docker | 140 | 43 | $18.00 | info | 部署教程词，CPC 极高 |
| litellm proxy | 480 | 53 | $6.67 | trans | LiteLLM 使用词 |
| llm cost optimization | 40 | 16 | $6.48 | info | ⭐ 低 KD，高 CPC |
| openai proxy | 90 | 56 | $4.42 | info | OpenAI 代理词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| litellm alternative | 140 | 2 | $3.70 | info | ⭐⭐⭐ 核心机会，Olares AI Router 正面竞争 |
| openrouter alternative | 170 | 8 | $3.35 | info | ⭐⭐⭐ 自托管替代 OpenRouter 的需求 |
| self hosted ai gateway | 20 | 0 | $4.92 | info | ⭐ 精准意图，量小但转化高 |
| open source ai gateway | 170 | 29 | $3.71 | info | ⭐ Olares Market 直接入口 |
| local ai gateway | 0 | 0 | $0 | — | GEO：本地 AI 网关概念 |
| self hosted llm gateway | 0 | 0 | $0 | — | GEO：精准自托管场景 |
| llm gateway open source | 20 | 0 | $3.63 | info | ⭐ 极低 KD |
| is llm gateway open source | 0 | 0 | $0 | — | GEO 问题词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：AI Router 是 Olares 体系内的原生 LLM 网关，核心叙事切入点是"私有化部署 + 零配置集成 Olares 模型"——对标有管理负担的 LiteLLM self-hosted 和不可私有化的 OpenRouter。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| litellm alternative | 140 | 2 | $3.70 | ⭐⭐⭐ Olares AI Router 作为 LiteLLM 在 Olares 上的轻量原生替代，零手动配置、自动发现模型 |
| openrouter alternative | 170 | 8 | $3.35 | ⭐⭐⭐ 不想付 OpenRouter 溢价 → 用 Olares AI Router 自建网关，API Key 不离机 |
| open source ai gateway | 170 | 29 | $3.71 | ⭐⭐ Olares Market 一键安装，对比 LiteLLM/Bifrost 等 open-source 选项 |
| llm gateway | 480 | 25 | $5.63 | ⭐⭐ 品类定义词，介绍 Olares 上的 LLM 网关生态（AI Router/LiteLLM/Bifrost）|
| litellm vs openrouter | 140 | 22 | $4.57 | ⭐⭐ 对比文中加入"第三选项：Olares AI Router 完全自托管"叙事 |
| self hosted ai gateway | 20 | 0 | $4.92 | ⭐⭐⭐ 精准场景词，Olares = 一键安装自托管 AI 网关 |
| llm cost optimization | 40 | 16 | $6.48 | ⭐⭐ 本地模型路由 = 零 API 费用，Olares 一站式成本优化 |
| llm gateway kubernetes | 20 | 0 | $0 | ⭐ Olares 基于 K8s，天然支持 K8s 部署，技术诉求吻合 |
| bifrost ai gateway | 90 | 0 | $2.34 | ⭐⭐ Olares 提供 AI Router/LiteLLM/Bifrost 三选一，差异化对比内容 |
| tensorzero | 480 | 32 | $0 | ⭐ TensorZero 也在 Olares Market，对比帖/选型指南机会 |
| local llm gateway | 0 | 0 | $0 | ⭐ GEO：Olares = 完整本地 LLM 栈（模型+网关+前端一体）|
| self hosted llm gateway | 0 | 0 | $0 | ⭐ GEO：精准 FAQ 词，Olares AI Router 抢引用位 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| litellm alternative | 140 | 2 | $3.70 | info | **主词候选** | KD=2 极低、CPC $3.70、明确替代意图——Olares AI Router 作为零手动配置的 LiteLLM 替代可直接切入 |
| openrouter alternative | 170 | 8 | $3.35 | info | **主词候选** | KD=8、量 170、替代意图明确——核心诉求是不想依赖云端代理，Olares 自建网关最直接的答案 |
| open source ai gateway | 170 | 29 | $3.71 | info | **主词候选** | KD<30 刚好入线，量 170——可写 Best Open Source AI Gateways，Olares Market 一键安装选项列首位 |
| llm gateway | 480 | 25 | $5.63 | info | **主词候选** | 品类定义词 KD=25，量 480，CPC $5.63 高——写 LLM Gateway 概念解析 + Olares 上的网关选项对比 |
| litellm vs openrouter | 140 | 22 | $4.57 | info/comm | **主词候选** | KD=22，对比词量 140——文章中引入"第三方案：Olares AI Router 完全私有化"叙事 |
| llm router | 590 | 45 | $4.14 | info | **次级** | 量 590 但 KD=45 偏高——作为 llm gateway 文章的次级词，或并入 llm gateway 簇 |
| llm gateways | 70 | 21 | $5.63 | info | **次级** | llm gateway 复数变体，KD=21，量 70——llm gateway 文章自然收录 |
| model router | 170 | 25 | $2.39 | info | **次级** | KD=25，CPC 偏低，技术词——并入 llm gateway/router 内容 |
| portkey vs litellm | 30 | 10 | $3.43 | comm | **次级** | 量小但对比意图强，KD=10——并入 litellm alternative 文章 |
| llm cost optimization | 40 | 16 | $6.48 | info | **次级** | KD=16，CPC $6.48 高商业价值——本地模型路由零费用叙事 |
| open source llm gateway | 20 | 0 | $3.63 | info | **次级** | KD=0，量小但变体词，并入 open source ai gateway 文章 |
| self hosted ai gateway | 20 | 0 | $4.92 | info | **次级** | KD=0 CPC $4.92，精准场景词，量小——并入 open source ai gateway 或 litellm alternative 文章 |
| bifrost ai gateway | 90 | 0 | $2.34 | nav | **次级** | KD=0，Olares 另一原生网关——Olares AI 网关对比选型文章的次级词 |
| self hosted llm gateway | 0 | 0 | $0 | info | **GEO** | 零量但精准，抢 AI Overview FAQ 引用位 |
| local ai gateway | 0 | 0 | $0 | info | **GEO** | 零量但语义精准，Olares 本地 AI 栈一体化叙事 |
| what is llm gateway | 20 | 0 | $7.81 | info | **GEO** | 定义型问答词，进 FAQ 块——Olares 文档/博客抢引用位 |
| what is llm router | 30 | 0 | $0 | info | **GEO** | 同上，llm router 定义词 |
| is llm gateway open source | 0 | 0 | $0 | info | **GEO** | 用户决策问题，Olares AI Router = Apache-2.0 的直接回答 |

---

## 核心洞见

1. **品牌护城河**：AI Router 无独立品牌，品类词（`ai router` KD=51、`ai gateway` KD=53）被 LiteLLM、OpenRouter、Portkey 把持，正面刚基本不可行。策略应是**借道竞品品牌词**——切 `litellm alternative`（KD=2）、`openrouter alternative`（KD=8）这类替代意图词，把 Olares AI Router 定位为"本地优先、零配置"的差异化选项。

2. **可复制的打法**：LiteLLM 的大流量来自教程/部署词（`litellm docker` CPC=$18、`litellm proxy`），反映用户在搭建自托管网关时的运维摩擦。Olares 的打法是**用"一键安装"对冲 LiteLLM 的运维复杂度**——内容策略以"vs LiteLLM"/"vs OpenRouter"对比文为主，突出零手动配置、自动发现 Olares 已安装模型。

3. **对 Olares 最关键的词**：
   - `litellm alternative`（KD=2，量 140）——切入成本最低、意图最纯
   - `openrouter alternative`（KD=8，量 170）——自建需求，Olares 完整方案
   - `open source ai gateway`（KD=29，量 170）——品类入口词，Olares Market 直接受益

4. **最大攻击面**：OpenRouter 的痛点是**数据经由第三方代理、API Key 上传云端**；LiteLLM self-hosted 的痛点是**需要 PostgreSQL + Redis + Docker 运维**。Olares AI Router 的叙事切入点：*"API Key 不离机、模型不上云、一键安装无运维"*。`llm cost optimization`（KD=16，CPC=$6.48）是高价值攻击词——本地模型路由 = 零 API 费用。

5. **隐藏低 KD 金矿**：
   - `litellm alternative` KD=2（！）量 140，月均全球估算约 420–700——最低成本、最高潜力
   - `open source llm gateway` KD=0，量 20——长尾真空地带
   - `self hosted ai gateway` KD=0，`llm api gateway` KD=0——运维/架构决策词，CPC 高
   - `bifrost ai gateway` KD=0，量 90——Olares 自有网关对比内容机会

6. **GEO 前瞻布局**：`self hosted llm gateway`、`local ai gateway`、`is llm gateway open source`、`what is llm gateway` 均为零量/低量但意图精准的问答型词——适合进 Olares 博客/文档 FAQ 段落，抢 Perplexity/AI Overview 引用位。"Can I run an LLM gateway completely offline on my own hardware?"等问题句型可嵌入产品文档。

7. **与既有分析的关联**：`olares-500-keywords` 与 `yiguo-keyword-plan` 中对 Olares 的定位集中于 personal cloud / self-hosted；AI Router 在此基础上开辟了 **LLM gateway/router** 这一新子品类——补充了 `llm gateway`、`litellm alternative`、`openrouter alternative` 等之前未覆盖的技术决策词。与 LiteLLM 报告（如已有）协同时，可共享 `litellm alternative` 簇作为跨报告内容选题。

---

*数据来源：SEMrush US 数据库（`phrase_these`、`phrase_related`、`phrase_fullsearch`、`phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
