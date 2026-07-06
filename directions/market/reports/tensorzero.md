# TensorZero SEO 竞品分析报告

> 域名：tensorzero.com | SEMrush US | 2026-07-06
> 开源 LLMOps 一体化平台（LLM 网关 + 可观测 + 评估 + 优化 + 实验）——**已于 2026-06-12 归档停维**

---

## 项目理解（前置）

TensorZero 是一个开源 LLMOps 平台，将 LLM 网关、可观测性、评估、优化（SFT/RFT）和 A/B 实验整合成一个统一栈，目标是"工业级 LLM 应用"的全链路管理。核心价值主张是从推理网关到模型微调形成闭环：用户请求数据 → 评估打分 → 自动触发 fine-tuning → 回流优化的飞轮。2025 年完成 $7.3M 种子轮（Conviction Capital 领投）。**2026-06-12 仓库被归档（read-only），官网已挂停维公告**，项目实质已停止。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 LLM 网关 + 可观测 + 优化 + 实验一体化平台（面向生产级 LLM 应用） |
| 开源 / 许可证 | 开源，Apache-2.0 |
| 主仓库 | [github.com/tensorzero/tensorzero](https://github.com/tensorzero/tensorzero)（★ 11.7k，已归档） |
| 核心功能 | 统一 LLM 推理网关（多 provider 路由/fallback）、结构化输出、请求可观测与追踪、模型评估框架、SFT/RFT 优化、A/B prompt 实验 |
| 商业模式 / 定价 | 纯开源自托管，免费；曾计划云托管版本，未落地即停维 |
| 差异化 / 价值主张 | 用"数据飞轮"将推理监控与模型优化打通；Rust 编写网关，性能强；对比 LiteLLM 多出 SFT/评估闭环 |
| 主要竞品（初判）| LiteLLM、OpenRouter（网关侧）；LangFuse、Helicone（可观测侧）；OpenPipe（优化侧） |
| Olares Market | 已收录（`apps.md` ⬜ 待研究），**项目已停维，Olares 上架时需注明版本冻结** |
| 来源 | [tensorzero.com](https://www.tensorzero.com/)（停维公告）；[GitHub 归档](https://github.com/tensorzero/tensorzero)；[种子轮博文](https://www.tensorzero.com/blog/tensorzero-raises-7-3m-seed-round-to-build-an-open-source-stack-for-industrial-grade-llm-applications/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | tensorzero.com |
| SEMrush Rank | 3,444,731 |
| 自然关键词数 | 147 |
| 月自然流量（US）| 118 |
| 自然流量估值 | $73/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 3 词 |
| 排名 4-10 位 | 26 词 |
| 排名 11-20 位 | 27 词 |

> 整体流量极低，符合早期技术产品 + 停维后流量下滑的预期。停维公告上线后，自然流量将进一步衰减。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.tensorzero.com | 147 | 118 | 100% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| tensorzero | 2 | 320 | 35 | $0 | 42 | 导航 | / |
| tensorzero | 5 | 320 | 35 | $0 | 14 | 导航 | /blog/tensorzero-raises-7-3m… |
| tensor zero | 2 | 70 | 29 | $0 | 9 | 导航 | / |
| litellm alternative ⭐ | 3 | 140 | 2 | $3.70 | 9 | 商业 | /docs/comparison/litellm |
| tensorzero | 7 | 320 | 35 | $0 | 9 | 导航 | /jobs/ |
| openai rft | 4 | 90 | 45 | $0 | 5 | 信息 | /blog/is-openai-rft-worth-it/ |
| vakzero | 12 | 1900 | 26 | $0 | 5 | 导航 | /（误触） |
| lmsysorg/sglang | 10 | 210 | 21 | $0 | 4 | 信息/商业 | /docs/integrations/model-providers/sglang |
| openrouter docker-compose | 8 | 320 | 10 | $0 | 4 | 信息 | /docs/integrations/model-providers/openrouter |
| openrouter alternative ⭐ | 8 | 170 | 8 | $3.35 | 4 | 商业 | /docs/comparison/openrouter |
| what does mtok mean | 8 | 140 | 20 | $0 | 3 | 信息 | /blog/stop-comparing-price-per-million-tokens… |
| what llm does cursor use | 7 | 210 | 31 | $8.34 | 2 | 信息 | /blog/reverse-engineering-cursors-llm-client/ |
| sglang docker | 4 | 170 | 39 | $0 | 2 | 信息 | /docs/integrations/model-providers/sglang |
| openrouter alternatives ⭐ | 13 | 320 | 3 | $3.35 | 1 | 商业 | /docs/comparison/openrouter |
| openrouter vs ⭐ | 6 | 70 | 11 | $4.40 | 2 | 信息 | /docs/comparison/openrouter |
| litellm vs openrouter | 21 | 140 | 22 | $4.57 | 0 | 信息 | /docs/comparison/openrouter |
| hyperbolic ai inference provider ⭐ | 16 | 70 | 6 | $0 | 0 | 信息 | /docs/integrations/model-providers/hyperbolic |
| batch inference | 38 | 260 | 26 | $9.16 | 0 | 信息 | /docs/gateway/guides/batch-inference |
| text generation inference openai compatible api ⭐ | 16 | 210 | 10 | $0 | 0 | 信息 | /docs/…/tgi |

> **关键洞察**：`litellm alternative`（KD 2）和 `openrouter alternative`（KD 8）是整站的 SEO 价值最高的两个词——极低 KD 配中等商业意图，TensorZero 用 `/docs/comparison/` 专页承接。随着项目停维，这两个词的竞争者将陆续消失，形成短暂真空。

### 付费词（Google Ads）

无付费投放记录。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| litellm | 14,800 | 56 | $5.42 | 信息 | 品牌护城河强，正面攻难度大 |
| openrouter vs litellm ⭐ | 260 | 20 | $0 | 信息/导航 | 低 KD 比较词 |
| litellm vs openrouter ⭐ | 140 | 22 | $4.57 | 信息 | 相同搜索意图的变体 |
| litellm alternative ⭐ | 140 | 2 | $3.70 | 商业 | **极低 KD，TensorZero 现排第 3** |
| openrouter alternative ⭐ | 170 | 8 | $3.35 | 商业 | 低 KD，已排第 8 |
| openrouter alternatives ⭐ | 320 | 3 | $3.35 | 商业 | 量更大、KD 更低 |
| langfuse | 9,900 | 59 | $6.37 | 信息 | 可观测侧领导者，难正面打 |
| helicone | 1,300 | 36 | $4.87 | 导航 | 中等难度，可观测赛道 |
| portkey ai | 260 | 53 | $3.52 | 导航 | 竞品，导航意图 |
| langsmith alternative ⭐ | 20 | 0 | $8.73 | 信息 | KD 为 0，CPC 高 |
| langfuse alternative ⭐ | 30 | 0 | $8.31 | 信息 | KD 为 0 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| llmops | 3,600 | 37 | $0.63 | 信息 | 类别主词，竞争中等 |
| ai gateway | 880 | 53 | $13.57 | 信息 | 高 CPC 意味商业价值，竞争高 |
| llm gateway ⭐ | 480 | 25 | $5.63 | 信息 | KD 适中，CPC 可观 |
| llm evaluation | 1,300 | 42 | $5.78 | 信息 | 细分市场大词 |
| llm observability ⭐ | 720 | 26 | $11.20 | 信息 | 低-中 KD，高 CPC |
| llm optimization ⭐ | 590 | 29 | $5.88 | 信息 | KD<30 边界，量适中 |
| llm fine tuning | 880 | 49 | $5.44 | 信息 | 偏难，价值高 |
| llm orchestration ⭐ | 210 | 33 | $5.24 | 信息 | 接近 KD 阈值 |
| llm routing | 170 | 52 | $4.58 | 信息 | 高 KD |
| llm ops | 320 | 43 | $5.19 | 信息 | 品类词变体 |
| open source ai gateway ⭐ | 170 | 29 | $3.71 | 信息 | **KD 刚过门槛，自托管意图强** |
| llm tracing ⭐ | 170 | 20 | $8.97 | 信息 | 低 KD，高 CPC |
| llm deployment ⭐ | 110 | 13 | $3.93 | 信息 | 低 KD |
| llm pipeline ⭐ | 70 | 16 | $5.36 | 信息 | 低 KD |
| llm structured output ⭐ | 140 | 26 | $0 | 信息 | 低 KD，功能导向 |
| prompt optimization ⭐ | 590 | 39 | $2.74 | 信息 | 接近门槛 |
| llm inference optimization ⭐ | 210 | 21 | $4.56 | 信息 | 低 KD |
| llm prompt management ⭐ | 30 | 16 | $2.92 | 信息 | 低 KD |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| tensorzero | 480 | 32 | $0 | 导航 | 品牌词，停维后会下滑 |
| what is llm gateway ⭐ | 20 | 0 | $8.95 | 信息 | KD 为 0，定义型内容机会 |
| what is an llm gateway ⭐ | 20 | 0 | $7.81 | 信息 | 同上变体 |
| llm a/b testing | 0 | 0 | $0 | — | 近零量，GEO 潜力词 |
| llm ab testing | 0 | 0 | $0 | — | 同上 |
| llm experiment tracking | 20 | 0 | $0 | — | 低 KD，次级词机会 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source llm gateway ⭐ | 20 | 0 | $3.63 | 信息 | KD 为 0，精准自托管意图 |
| open source ai gateway ⭐ | 170 | 29 | $3.71 | 信息 | 有一定量且 KD 低 |
| llm gateway open source ⭐ | 20 | 0 | $0 | — | 同上语序变体 |
| llmops open source ⭐ | 20 | 0 | $0 | — | GEO 前哨 |
| open source llmops ⭐ | 20 | 0 | $0 | — | 同上变体 |
| self-hosted llm gateway | 0 | 0 | $0 | — | 近零量，GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心逻辑：TensorZero 已停维，留下"LLMOps 自托管"词组的排名真空；Olares Market 同时上架 LiteLLM + OpenPipe 等在役替代品，可系统承接这批比较词流量。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| litellm alternative ⭐ | 140 | 2 | $3.70 | TensorZero 已停维，LiteLLM 是 Olares Market 可一键部署的在役替代，写"LiteLLM vs TensorZero + 在 Olares 上部署 LiteLLM"直接承接 | ⭐⭐⭐ |
| openrouter alternative ⭐ | 170 | 8 | $3.35 | 同逻辑，可对比 OpenRouter（闭源）vs 自托管 LLM 网关（LiteLLM/TensorZero on Olares） | ⭐⭐⭐ |
| openrouter alternatives ⭐ | 320 | 3 | $3.35 | 量更大、KD 更低，是 openrouter alternative 的高优先变体 | ⭐⭐⭐ |
| open source ai gateway ⭐ | 170 | 29 | $3.71 | Olares 可作为一站式平台运行 LiteLLM/TensorZero，是最自然的"自托管 AI 网关"落地场景 | ⭐⭐⭐ |
| llm observability ⭐ | 720 | 26 | $11.20 | Olares 内可同时跑 LangFuse + TensorZero，统一数据不出设备，强隐私叙事 | ⭐⭐ |
| llm gateway ⭐ | 480 | 25 | $5.63 | Olares Market 上 LiteLLM 填这个需求；"在 Olares 上运行 LLM 网关"是直接内容机会 | ⭐⭐ |
| llm tracing ⭐ | 170 | 20 | $8.97 | 对应 LangFuse/Helicone 等可观测工具，Olares Market 可一键部署，高 CPC 值得写 | ⭐⭐ |
| llm deployment ⭐ | 110 | 13 | $3.93 | Olares 一键部署叙事天然契合；KD 极低 | ⭐⭐ |
| open source llm gateway ⭐ | 20 | 0 | $3.63 | 精准意图，KD=0，适合做 FAQ/GEO 段落 | ⭐⭐ |
| llm inference optimization ⭐ | 210 | 21 | $4.56 | 对应 Olares One 的本地 GPU 推理叙事（Ollama + 24GB 独显跑本地模型） | ⭐⭐ |
| self-hosted llm gateway | 0 | 0 | $0 | 近零量但语义最精准；抢 AI Overview 引用位 | ⭐ |
| llm a/b testing | 0 | 0 | $0 | TensorZero 核心用例，GEO 前哨词，在"自托管 LLMOps"文章里加 FAQ 段落 | ⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| openrouter alternatives | 320 | 3 | $3.35 | 商业 | **主词候选** | 量最大 + KD 最低的替代词，TensorZero 停维后排名空缺扩大；Olares 写"openrouter alternatives"对比文，主推 LiteLLM on Olares |
| llm gateway | 480 | 25 | $5.63 | 信息 | **主词候选** | 中等 KD + 合理量 + CPC $5.6，自托管叙事天然契合；可写"best self-hosted LLM gateway"承接 |
| llm observability | 720 | 26 | $11.20 | 信息 | **主词候选** | 量最大的低-中 KD 词，CPC $11 暗示商业价值；Olares 隐私叙事（数据不出设备）是差异化角度 |
| litellm alternative | 140 | 2 | $3.70 | 商业 | **主词候选** | KD=2 是整个报告最低的有量商业词；TensorZero 已停维，留下排名真空；直接写"LiteLLM vs TensorZero" |
| openrouter alternative | 170 | 8 | $3.35 | 商业 | **主词候选** | 低 KD 高商业意图，TensorZero 已有排名但将衰退；Olares 可承接 |
| open source ai gateway | 170 | 29 | $3.71 | 信息 | **主词候选** | KD 刚过 30 边界，精准自托管意图，适合独立文章 |
| llm tracing | 170 | 20 | $8.97 | 信息 | **主词候选** | KD 低 + CPC $9，市场愿意为可观测性付费；Olares Market 上的 LangFuse/Helicone 直接回答 |
| llm deployment | 110 | 13 | $3.93 | 信息 | **主词候选** | 量过 100 软线，KD=13 极低，Olares 一键部署叙事 |
| llm inference optimization | 210 | 21 | $4.56 | 信息 | **主词候选** | KD 低 + 量合格，可用 Olares One 本地 GPU 推理的实测数据支撑 |
| openrouter vs litellm | 260 | 20 | $0 | 信息/导航 | **次级** | 作为上方对比文的 H2，量够但意图偏导航 |
| litellm vs openrouter | 140 | 22 | $4.57 | 信息 | **次级** | 同上变体，并入对比文 |
| llm structured output | 140 | 26 | $0 | 信息 | **次级** | 低 KD 功能词，并入"LLM 网关"文章的功能段 |
| llm prompt management | 30 | 16 | $2.92 | 信息 | **次级** | 量小但 KD 低，并入 LLMOps 综合文 |
| llm pipeline | 70 | 16 | $5.36 | 信息 | **次级** | KD 低，适合技术深度文 |
| what is llm gateway | 20 | 0 | $8.95 | 信息 | **次级** | KD=0，定义型 H2/FAQ，CPC 高说明意图价值 |
| open source llm gateway | 20 | 0 | $3.63 | 信息 | **次级** | KD=0，精准自托管意图，加进自托管文章 FAQ |
| self-hosted llm gateway | 0 | 0 | $0 | — | **GEO** | 近零量但语义最精准，抢 AI Overview/Perplexity 引用位 |
| llm a/b testing | 0 | 0 | $0 | — | **GEO** | TensorZero 核心用例词，AI Overview 将解释此概念 |
| llm ab testing | 0 | 0 | $0 | — | **GEO** | 同上变体 |
| llmops open source | 10 | 0 | $0 | — | **GEO** | 精准信号词，自托管 LLMOps 文章必须覆盖 |

---

## 核心洞见

1. **品牌护城河**：TensorZero 已归档停维，品牌词心智将快速消散。**不要正面刚品牌词**，而是在它留下的比较页和文档页排名上趁虚而入——`litellm alternative`（KD=2）、`openrouter alternatives`（KD=3）是整个报告里最具性价比的两个词，目前 TensorZero 占据排名但内容将停止更新、外链将腐烂。

2. **可复制的打法**：TensorZero 的最大流量来源是 `/docs/comparison/litellm` 和 `/docs/comparison/openrouter` 两个专页——**程序化对比落地页策略**。Olares 可复制此打法，针对每个 Olares Market 上架的 LLMOps 工具建立 `X vs Y + 在 Olares 上部署 X` 的对比文，低 KD 词覆盖多、边际成本低。

3. **对 Olares 最关键的词**：
   - `litellm alternative`（KD=2，月量 140，$3.70 CPC）——停维真空期最快可抢；
   - `openrouter alternatives`（KD=3，月量 320，$3.35 CPC）——量更大，同样极低 KD；
   - `open source ai gateway`（KD=29，月量 170）——自托管叙事最精准，量够写独立文章。

4. **最大攻击面**：TensorZero 已停维是最大的痛点——用户搜 `litellm alternative` / `tensorzero alternative` 时将发现文档冻结，这是 Olares 的直接进场时机。次要攻击面是"数据飞轮"需要云端同步才能做到最优，而 Olares 强调本地数据主权。

5. **隐藏低 KD 金矿**：`llm tracing`（KD=20，$8.97 CPC）、`llm deployment`（KD=13）、`llm pipeline`（KD=16）、`what is llm gateway`（KD=0，$8.95 CPC）——这几个词 CPC 高但 KD 低，说明商业意图强但内容供给不足，是典型的未被充分覆盖的蓝海词。

6. **GEO 前瞻布局**：`self-hosted llm gateway`、`llm a/b testing`、`llm ab testing`、`llmops open source` 四个词现在量接近零，但随着 AI 工具链渗透生产环境，这些精准自托管术语将成为 Perplexity/AI Overview 的高频引用点——现在写进 FAQ 段、占坑成本极低。

7. **与既有 `olares-500-keywords` 词表的关联**：LLMOps 方向在现有 500 词分析里属于技术长尾，本报告补充了**商业意图 + 极低 KD 的对比词**（KD=2/3 的替代词）和**高 CPC 可观测类词**（`llm tracing` $8.97、`llm observability` $11.20），这两类在 olares-500 里通常被低估；建议将 `litellm alternative`、`openrouter alternatives`、`open source ai gateway` 纳入下一轮关键词优先级评审。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*注：TensorZero 官网及 GitHub 仓库于 2026-06-12 归档，项目已停止维护，流量预计持续下滑，相关排名将产生空缺。*
