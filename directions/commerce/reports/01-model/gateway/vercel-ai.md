# Vercel AI Gateway SEO 竞品分析报告

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> Vercel 平台的托管 AI 请求路由层：统一 API 接入 100+ 模型、自动故障转移、ZDR 合规路由，深度绑定 Vercel 生态，无开源版本。

---

## 项目理解（前置）

Vercel AI Gateway 是 Vercel（估值 $9.3B）平台的内置 AI 基础设施层，于 2024-2025 年间逐步推出并在 2026 年成熟。它在应用代码与 AI 模型提供商之间插入一层代理，向开发者暴露单一 OpenAI 兼容端点，背后可路由到 Anthropic、Google、Meta、Mistral 等 100+ 模型，同时提供自动 fallback、花费监控与 ZDR（零数据留存）合规路由。**它不是独立产品/域名，而是 vercel.com 的功能模块**，无独立官网，因此本报告走降级模式（场景词分析）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Vercel 生态内嵌的托管 LLM Gateway：一个 key、100+ 模型、零 markup、自动 fallback |
| 开源 / 许可证 | 闭源，完全 SaaS；Vercel AI SDK 本身开源（Apache 2.0）但 Gateway 是专有服务 |
| 主仓库 | 无独立仓库；AI SDK：[github.com/vercel/ai](https://github.com/vercel/ai)（★ 10k+） |
| 核心功能 | 统一 API 代理（OpenAI / Anthropic / Google / Meta…）、自动故障转移/fallback、ZDR 合规路由、BYOK（带自有 key 无 markup）、per-key 预算与 per-user 配额、Dashboard 可观测性 |
| 商业模式 / 定价 | 按需付费；购买 AI Gateway Credits，按 provider 原价扣费零 markup；高级功能额外计费：ZDR 团队级 $0.10/1k 请求，Provider 白名单 $0.10/1k 成功请求，Custom Reporting $0.075/1k 写 + $5/1k 查 |
| 差异化 / 价值主张 | 与 Vercel AI SDK / Next.js 深度集成，零配置上手；无 token markup；ZDR 合规路由；BYOK 支持 |
| 主要竞品（初判）| LiteLLM（开源自托管）、OpenRouter（托管聚合）、Portkey（托管+OSS）、Cloudflare AI Gateway |
| Olares Market | LiteLLM ✅ 已上架；AI Router ✅ 已上架（均为自托管平替） |
| 来源 | [vercel.com/ai-gateway](https://vercel.com/ai-gateway)、[vercel.com/docs/ai-gateway/pricing](https://vercel.com/docs/ai-gateway/pricing)、[llmversus.com LLM Gateway Comparison 2026](https://llmversus.com/blog/llm-gateway-comparison-2026) |

---

## 关键词扩展（Phase 2）

> 场景词分析模式——跳过域名流量基线，直接从关键词层面入手。
> ⭐ = KD<30 且量>0 的机会词。按月量降序。

### 品类词（核心战场）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| vercel ai sdk | 5,400 | 69 | $3.78 | 信息/品牌 | Vercel 生态入口词，KD 高 |
| ai sdk | 4,400 | 47 | $7.84 | 信息 | 通用 SDK 词，混合意图 |
| vercel ai | 2,900 | 85 | $3.49 | 品牌 | 母品牌词，KD 极高 |
| portkey | 2,400 | 41 | $2.68 | 品牌/商业 | 竞品品牌词 |
| litellm | 14,800 | 56 | $5.42 | 信息 | 核心竞品，量最大 |
| llm observability ⭐ | 720 | 26 | $11.20 | 信息 | 高 CPC，KD 低，Gateway 功能词 |
| vercel ai gateway | 1,000 | 47 | $5.31 | 信息 | 产品品牌词 |
| AI gateway | 880 | 53 | $13.57 | 信息 | 品类主词，CPC 高 |
| cloudflare ai gateway | 880 | 47 | $4.96 | 商业/信息 | 竞品词 |
| LLM router | 590 | 45 | $4.14 | 信息 | 品类变体 |
| LLM gateway ⭐ | 480 | 25 | $5.63 | 信息 | **KD 仅 25，主要品类词，首选目标** |
| AI router | 390 | 51 | $3.19 | 信息 | 品类变体 |
| portkey ai | 260 | 53 | $3.52 | 商业 | 竞品词 |
| AI proxy | 210 | 42 | $2.65 | 信息 | 品类词 |
| LLM proxy | 170 | 50 | $5.90 | 信息 | 品类词 |
| LLM routing | 170 | 52 | $4.58 | 信息 | 功能词 |
| open source ai gateway ⭐ | 170 | 29 | $3.71 | 信息 | **KD 低，自托管信号词** |
| ai api management ⭐ | 110 | 38 | $0 | 信息 | 企业功能词 |
| portkey ai gateway ⭐ | 110 | 27 | $2.69 | 信息/品牌 | 竞品+品类组合 |
| openai proxy | 90 | 56 | $4.42 | 信息 | 具体实现词 |
| AI model gateway ⭐ | 30 | 30 | $9.19 | 信息 | 低量但高 CPC，精准 |
| self-hosted AI gateway ⭐ | 20 | 0 | $2.75 | 信息 | **KD=0，自托管信号词** |
| open source LLM gateway ⭐ | 20 | 0 | $0 | 信息 | KD=0，纯机会词 |

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| openrouter alternative ⭐ | 170 | 8 | $3.35 | 商业 | **KD=8，极低竞争，高机会** |
| litellm alternative ⭐ | 140 | 2 | $3.70 | 商业 | **KD=2，极低竞争，首选攻击词** |
| litellm vs openrouter ⭐ | 140 | 22 | $4.57 | 商业/信息 | 对比词，KD 低 |
| vercel ai gateway vs openrouter ⭐ | 170 | 5 | $0 | 商业/信息 | **KD=5，产品对比词，极好机会** |
| ai gateway alternative | — | — | — | 商业 | 量极小，待补充 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| vercel ai gateway | 1,000 | 47 | $5.31 | 信息 | 产品主词 |
| vercel gateway ⭐ | 110 | 42 | $8.48 | 信息/商业 | 功能入口词 |
| vercel ai pricing ⭐ | 110 | 30 | $0 | 商业 | 定价查询，KD 适中 |
| vercel ai gateway models | 70 | 0 | $5.84 | 信息 | KD=0，具体功能词 |
| vercel ai gateway vs openrouter | 170 | 5 | $0 | 信息 | 对比词 |
| ai-sdk vercel | 260 | 67 | $6.13 | 信息/品牌 | KD 高 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| litellm | 14,800 | 56 | $5.42 | 信息 | 最大自托管替代品 |
| litellm proxy | 480 | 53 | $6.67 | 信息/导航 | LiteLLM 功能词 |
| what is litellm ⭐ | 480 | 33 | $3.78 | 信息 | 教育型词，KD 中等 |
| google adk litellm ⭐ | 480 | 25 | $0 | 信息 | 集成词，KD 低 |
| litellm gemini ⭐ | 480 | 11 | $0 | 信息 | **KD=11，极好机会** |
| litellm docker image ⭐ | 320 | 31 | $0 | 信息 | 部署词 |
| litellm docker | 140 | 43 | $18 | 信息 | 部署词，CPC 极高 |
| litellm alternative ⭐ | 140 | 2 | $3.70 | 商业 | **最低 KD 机会词** |
| litellm self hosted ⭐ | 40 | 0 | $0 | 信息 | KD=0 |
| llm cost optimization ⭐ | 40 | 16 | $6.48 | 信息 | 省钱叙事词 |
| self-hosted AI gateway ⭐ | 20 | 0 | $2.75 | 信息 | KD=0 |
| open source LLM gateway ⭐ | 20 | 0 | $0 | 信息 | KD=0 |
| llm load balancing ⭐ | 20 | 0 | $6.34 | 信息 | KD=0，高 CPC |

---

## Olares 关联词（Phase 3）

**核心叙事**：Vercel AI Gateway 是云锁定方案（必须在 Vercel 平台），而 LiteLLM + AI Router 在 Olares 上提供同等能力（统一 API、fallback、费用追踪），且数据完全在本地，零 platform markup。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| litellm alternative | 140 | 2 | $3.70 | Olares 一键部署 LiteLLM = Vercel AI Gateway 的完全自托管替代，无云锁定、零 markup | ⭐⭐⭐ |
| open source LLM gateway | 20 | 0 | $0 | LiteLLM on Olares 是最易部署的 OSS LLM Gateway，Market 直接安装 | ⭐⭐⭐ |
| self-hosted AI gateway | 20 | 0 | $2.75 | Olares Market 已有 LiteLLM：自托管 AI Gateway 零运维方案 | ⭐⭐⭐ |
| vercel ai gateway vs openrouter | 170 | 5 | $0 | 三方对比可加第四个选项：LiteLLM on Olares（自托管，数据主权） | ⭐⭐⭐ |
| litellm | 14,800 | 56 | $5.42 | Olares Market 已上架 LiteLLM，可作为 LiteLLM 部署教程的叙事入口 | ⭐⭐ |
| LLM gateway | 480 | 25 | $5.63 | "LLM Gateway self-hosted on Olares"：LiteLLM + Olares 是比 Vercel AI Gateway 更便宜、更私密的选择 | ⭐⭐⭐ |
| open source ai gateway | 170 | 29 | $3.71 | LiteLLM 是开源 AI Gateway 代表，Olares 提供一键部署 | ⭐⭐⭐ |
| llm observability | 720 | 26 | $11.20 | LiteLLM on Olares 内置 Dashboard 可观测性，无需额外 SaaS 订阅 | ⭐⭐ |
| ai spend management | 140 | 26 | $16.89 | Olares 上的 LiteLLM 支持 virtual key + budget 追踪，相比 Vercel AI Gateway 更透明可控 | ⭐⭐ |
| litellm vs openrouter | 140 | 22 | $4.57 | Olares 叙事：LiteLLM on Olares vs OpenRouter = 完全自托管 vs SaaS，数据主权维度 | ⭐⭐ |
| what is litellm | 480 | 33 | $3.78 | LiteLLM 教育词，可落地到"如何在 Olares 上部署 LiteLLM"教程 | ⭐⭐ |
| litellm gemini | 480 | 11 | $0 | LiteLLM on Olares 支持 Gemini 接入，KD 极低，流量可观 | ⭐⭐ |
| google adk litellm | 480 | 25 | $0 | 集成词：Olares 上 LiteLLM + Google ADK 的完整方案 | ⭐⭐ |
| llm load balancing | 20 | 0 | $6.34 | LiteLLM on Olares 支持多 provider 负载均衡，KD=0 | ⭐⭐ |
| llm cost optimization | 40 | 16 | $6.48 | 核心叙事：自托管 LLM Gateway on Olares = 零 platform fee = 最优 cost optimization | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| LLM gateway | 480 | 25 | $5.63 | 信息 | **主词候选** | KD 仅 25，品类核心词；Olares 叙事：LiteLLM on Olares 是最易部署的自托管 LLM Gateway |
| open source LLM gateway | 20 | 0 | $0 | 信息 | **主词候选** | KD=0，量小但意图极精准；Olares Market 直接命中，值得独立布局 |
| litellm alternative | 140 | 2 | $3.70 | 商业 | **主词候选** | KD=2 极低竞争，商业意图明确；Olares 可作为"在自己服务器跑 LiteLLM"的落地 |
| vercel ai gateway vs openrouter | 170 | 5 | $0 | 信息/比较 | **主词候选** | KD=5，对比文章天然入口；可扩展为三方+Olares/LiteLLM 四向对比 |
| openrouter alternative | 170 | 8 | $3.35 | 商业 | **主词候选** | KD=8，自托管叙事切入点；OpenRouter 无法自托管而 LiteLLM on Olares 可以 |
| llm observability | 720 | 26 | $11.20 | 信息 | **主词候选** | 量大 KD 低，高 CPC 说明商业价值；LiteLLM on Olares 内置可观测性 |
| self-hosted AI gateway | 20 | 0 | $2.75 | 信息 | **主词候选** | KD=0，意图精准；Olares + LiteLLM 完美命中 |
| open source ai gateway | 170 | 29 | $3.71 | 信息 | **主词候选** | KD<30，量合理；LiteLLM on Olares 的核心身份 |
| AI gateway | 880 | 53 | $13.57 | 信息 | 次级 | 量最大但 KD 53，可并入 LLM gateway 文章的二级词；CPC 高说明竞争激烈 |
| litellm vs openrouter | 140 | 22 | $4.57 | 商业/信息 | **主词候选** | KD 22，对比意图；可扩展加入 Olares/自托管维度 |
| llm cost optimization | 40 | 16 | $6.48 | 信息 | 次级 | 量小但 KD 低，CPC 高；Olares 自托管省 platform fee 叙事 |
| litellm gemini | 480 | 11 | $0 | 信息 | **主词候选** | KD=11，量 480，集成词机会词；Olares 上 LiteLLM 接 Gemini 的教程 |
| what is litellm | 480 | 33 | $3.78 | 信息 | 次级 | 教育词，KD 适中；可作为 LiteLLM on Olares 教程的锚词 |
| ai spend management | 140 | 26 | $16.89 | 商业 | 次级 | KD<30，CPC 极高（$16.89）；Olares 叙事：virtual key + budget 自主管控 |
| portkey ai gateway | 110 | 27 | $2.69 | 信息/品牌 | 次级 | 竞品词，KD 低；可并入 LLM Gateway 对比文 |
| llm load balancing | 20 | 0 | $6.34 | 信息 | GEO | KD=0，高 CPC，近零量；适合 FAQ/技术段落，抢 AI Overview 引用位 |
| litellm self hosted | 40 | 0 | $0 | 信息 | GEO | KD=0，自托管精准词；Olares Market 直接落地 |
| vercel ai gateway models | 70 | 0 | $5.84 | 信息 | GEO | KD=0，具体功能词；对比文章中的技术细节段落 |
| google adk litellm | 480 | 25 | $0 | 信息 | 次级 | KD 低，集成词；Olares Agent 叙事（ADK + LiteLLM on Olares） |

---

## 核心洞见

1. **品牌护城河**：Vercel AI Gateway 自身品牌词（`vercel ai gateway` 月量 1,000，KD 47）和 Vercel 母品牌（`vercel ai` 月量 2,900，KD 85）都是高 KD 词，**正面刚 ROI 极低**。真正的机会在品类词（`LLM gateway` KD=25）和竞品对比词（`litellm alternative` KD=2、`vercel ai gateway vs openrouter` KD=5）。

2. **可复制的打法**：Vercel 自身靠 AI SDK 生态（`vercel ai sdk` 月量 5,400）带动 Gateway 认知；对我们而言，最优打法是**把 LiteLLM on Olares 打成"自托管 AI Gateway"的标准答案**——通过极低 KD 的对比词和自托管词吃长尾，再借助 `what is litellm`（480/月，KD 33）等教育词做漏斗顶部。

3. **对 Olares 最关键的词**：
   - `litellm alternative`（月量 140，KD=2）——最低竞争、商业意图最明确
   - `LLM gateway`（月量 480，KD=25）——品类主词，KD<30 可攻
   - `vercel ai gateway vs openrouter`（月量 170，KD=5）——对比词，可直接扩展为四向对比

4. **最大攻击面**：Vercel AI Gateway 的最大痛点是**云锁定**（必须在 Vercel 平台部署，无法自托管）和**依赖 Vercel 基础设施**（数据离不开 Vercel）。这正好对应"self-hosted AI gateway"（KD=0）和"open source LLM gateway"（KD=0）这两个零竞争词，以及更广的"data sovereignty / privacy"叙事。另一个攻击面：Vercel AI Gateway 无 evals 集成、无 prompt management——而 LiteLLM + Olares 可与 Langfuse（Olares Market 待上架）集成形成更完整的 MLOps 栈。

5. **隐藏低 KD 金矿**：
   - `litellm gemini`（月量 480，KD=11）——量大 KD 极低，LiteLLM 集成词里最大机会
   - `litellm vs openrouter`（月量 140，KD=22）——对比词，KD<25
   - `google adk litellm`（月量 480，KD=25）——Agent 集成词，与 Olares Personal Agent 叙事高度契合
   - `llm load balancing`（月量 20，KD=0）——近零量但高 CPC（$6.34），技术段落用
   - `mosaic ai gateway / databricks ai gateway`（月量 90/210，KD 13/21）——企业级竞品词，KD 低

6. **GEO 前瞻布局**：
   - `how to monitor llm activity through AI gateway`（近零量）——监控/可观测性问答段落
   - `self-hosted LLM gateway vs managed`——托管 vs 自托管对比，AI Overview 热门问题类型
   - `llm gateway kubernetes`（月量 20，KD=0）——Olares 基于 K8s，原生技术匹配
   - `ai gateway enterprise`——企业自托管需求词，Olares/LiteLLM 可满足，适合 GEO 问答
   - `open source LLM gateway`（KD=0）——Olares Market + LiteLLM 直接命中，抢 Perplexity 引用

7. **与既有分析的关联**：`olares-500-keywords` 中已有 Vercel 和 AI 基础设施相关词；本报告新增补充：**LLM gateway 品类词（KD=25）、litellm alternative（KD=2）、litellm gemini（KD=11）** 三个高优先级词，均与 Olares Market 已上架的 LiteLLM 直接挂钩。另外，OpenRouter 报告（已在 gateway/ 目录）聚焦于 OpenRouter 品牌词；本报告补充了品类词和自托管信号词维度，两者可联合布局一篇"AI Gateway 完全对比：Vercel vs OpenRouter vs LiteLLM（自托管）"文章。

---

*数据来源：SEMrush US 数据库（phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
