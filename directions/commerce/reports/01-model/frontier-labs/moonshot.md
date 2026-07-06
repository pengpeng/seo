# Moonshot AI / Kimi SEO 竞品分析报告

> 域名：kimi.ai（英文开发者/API 平台）| SEMrush US | 2026-07-06
> 中国 AI 独角兽 Moonshot AI 的全球开发者入口——以超长上下文 + 开放权重（Kimi K2 系列）为核心差异化，ARR >$200M，估值 $20B。

---

## 项目理解（前置）

Moonshot AI 是北京 AI 实验室，旗舰产品 Kimi 是面向全球的长上下文 AI 助手与开发者平台。2026 年 1 月发布 Kimi K2.5（1 万亿参数 MoE，32B 激活），成为年度编程/Agent 任务的标杆开源权重之一，20 天内收入超过 2025 全年总和，直接将 ARR 推至 $200M 以上。kimi.ai 是英文开发者 API 入口，主力消费者聊天界面在 kimi.com；面向中文市场的官方域名是 moonshot.cn。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 超长上下文、Agentic 编程 AI——中国 AI 实验室里商业化速度最快的 |
| 开源 / 许可证 | 开放权重，Modified MIT License（100M MAU 或 $20M 收入以上需协商） |
| 主仓库 | [moonshotai/Kimi-K2](https://github.com/moonshotai/kimi-k2)（★ ~10.9K）；权重 [moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) |
| 核心功能 | 256K 上下文（1T 参数 MoE）/ Agent Swarm（最多 300 子代理并行）/ Kimi Code CLI / 多模态 MoonViT / Claude Code & OpenCode 兼容 |
| 商业模式 / 定价 | 消费者订阅：Adagio 免费→Moderato $19→Allegretto $39→Allegro $99→Vivace $199/月；API：K2.6 $0.95/M input，$4.00/M output（缓存命中 $0.16）|
| 差异化 / 价值主张 | GPT-5.4 价格的 4-17×优惠 + 开放权重可自托管 + Agent Swarm 并行多代理编排 |
| 主要竞品（初判） | ChatGPT / Claude / Gemini（商业闭源）；DeepSeek / Qwen（开放权重中国竞品）|
| Olares Market | 未上架（Kimi K2 权重可在 Ollama on Olares 运行；平台层对应 Ollama） |
| 来源 | [HuggingFace 模型卡](https://huggingface.co/moonshotai/Kimi-K2.6)；[TechCrunch 融资报道](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/)；[deepinfra 技术解析](https://deepinfra.com/blog/kimi-k2-6-model-overview)；[saaszap 产品评测](https://saaszap.com/moonshot-ai-review/) |

> **⚠ 重要注意**：kimi.ai 是 Moonshot 的**开发者/API 平台**，US 流量以 API 开发者词为主；主力消费者端在 kimi.com（另域名，US 流量约 128K/月，已被 Semrush 视为 kimi.ai 的自然竞品）。本报告以 kimi.ai 为主域名，洞见部分兼顾 kimi.com 数据。

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | kimi.ai（含 platform.kimi.ai） |
| SEMrush Rank | 227,779 |
| 自然关键词数 | 1,148 |
| 月自然流量（US） | 7,607 |
| 自然流量估值 | $20,565/月 |
| 付费关键词数 | 0（无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 78 词 |
| 排名 4-10 位 | 61 词 |
| 排名 11-20 位 | 71 词 |

> kimi.ai US 自然流量为 7,607/月，体量不大，因为主流量在 kimi.com（US ~128K/月）；kimi.ai 是 API developer 域名，词以 API Key / 定价 / 文档为主，单词 CPC 普遍 $2-5 以上，流量估值/词量比极高。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| platform.kimi.ai | 1,147 | 6,888 | 90.6% |
| kimi.ai（根域） | 1 | 719 | 9.4% |

> platform.kimi.ai 几乎占全部流量，对应 API 控制台 + 文档站。品牌词 `kimi.ai`（月量 2,900）在根域排第 1，流量 719。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| kimi api | 1 | 3,600 | 35 | $3.50 | 2,880 | 商业 | platform.kimi.ai |
| kimi.ai | 1 | 2,900 | 72 | $0.83 | 719 | 导航 | kimi.ai |
| kimi api key | 1 | 720 | 23 | $2.72 | 576 | 导航/交易 | platform.kimi.ai/console/api-keys |
| kimi k2 api | 1 | 590 | 42 | $3.05 | 472 | 商业/交易 | platform.kimi.ai |
| kimi k2 api pricing | 1 | 1,000 | 20 | $3.20 | 248 | 交易 | platform.kimi.ai/docs/pricing/chat |
| kimi官网 | 5 | 3,600 | 59 | $0.61 | 158 | 商业/交易 | platform.kimi.ai |
| kimi model | 1 | 590 | 67 | $3.93 | 146 | 导航 | platform.kimi.ai/docs/models |
| kimi api pricing | 1 | 170 | 23 | $2.95 | 136 | 交易 | platform.kimi.ai/docs/pricing/chat |
| kimi platform | 1 | 170 | 50 | $0.00 | 136 | 商业/交易 | platform.kimi.ai |
| kimi ai api | 1 | 140 | 52 | $2.53 | 112 | 商业 | platform.kimi.ai |
| kimi.ai | 5 | 2,900 | 72 | $0.83 | 101 | 导航 | platform.kimi.ai |
| kimi2 api | 1 | 110 | 56 | $3.05 | 88 | 商业/交易 | platform.kimi.ai |
| kimi-cc | 1 | 320 | 36 | $0.00 | 79 | 信息 | platform.kimi.ai/docs/guide/agent-support |
| kimi-k2.5 api | 1 | 90 | 59 | $3.15 | 72 | 商业 | platform.kimi.ai |
| kimi k2 pricing | 1 | 260 | 15 | $3.90 | 64 | 交易 | platform.kimi.ai/docs/pricing/chat |
| kimi k2 claude code | 1 | 260 | 42 | $0.00 | 64 | 信息 | platform.kimi.ai/docs/guide/agent-support |
| kimi k2.5 api | 1 | 2,400 | 36 | $2.95 | 62 | 商业 | platform.kimi.ai |
| kimi k2.5 api pricing | 1 | 70 | 46 | $3.20 | 56 | 交易 | platform.kimi.ai/docs/pricing/chat |
| kimi k2 thinking api | 1 | 70 | 47 | $2.27 | 56 | 商业/交易 | platform.kimi.ai |
| kimi models | 1 | 320 | 61 | $3.93 | 42 | 信息 | platform.kimi.ai/docs/models |
| kimi k2 5 api key | 1 | 50 | 41 | $2.45 | 40 | 商业 | platform.kimi.ai |
| kimi moonshot api | 1 | 50 | 54 | $4.34 | 40 | 商业 | platform.kimi.ai |
| moonshot kimi api | 1 | 50 | 52 | $5.07 | 40 | 商业/交易 | platform.kimi.ai |
| kimi status | 3 | 480 | 0 | $0.00 | 39 | 信息 | platform.kimi.ai/docs/guide/faq |
| kimi k2.5 pricing | 1 | 260 | 30 | $3.13 | 34 | 交易 | platform.kimi.ai/docs/pricing/chat |
| kimi k2 price | 1 | 140 | 23 | $3.90 | 34 | 交易 | platform.kimi.ai/docs/pricing/chat |
| kimi-k2-turbo-preview | 2 | 480 | 11 | $0.00 | 31 | 信息 | platform.kimi.ai/docs/guide |
| claude code kimi | 1 | 110 | 37 | $12.85 | 27 | 信息 | platform.kimi.ai/docs/guide/agent-support |
| kimi cc | 1 | 110 | 46 | $0.00 | 27 | 商业 | platform.kimi.ai/docs/guide/agent-support |
| kimi console | 1 | 110 | 22 | $6.16 | 27 | 商业/交易 | platform.kimi.ai/console |
| kimi2；kimi ia | 11/7 | 8,100/4,400 | 85/77 | $3.06/$0.83 | 14/26 | 商业 | platform.kimi.ai/docs（排名低）|
| how to use kimi k2.5 with openclaw | 1 | 320 | 13 | $0.00 | 11 | 信息 | platform.kimi.ai/docs/guide/use-kimi-in-openclaw |

> **洞察**：`kimi2`（8,100/月，KD 85）和 `kimi ia`（4,400/月）在 kimi.ai 排名第 11-13 位，错失大量流量——这些高量词的主战场是 kimi.com。高 CPC 词集中在 API Pricing（$3-5）、Claude Code 集成（$12.85）。

### 付费词（Google Ads）

kimi.ai 无任何付费搜索投放（Paid Keywords = 0）。流量 100% 来自 SEO。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| chatgpt alternative | 18,100 | 47 | $1.31 | 信息 | 大类词，竞争激烈 |
| kimi vs chatgpt | 110 | 9 | $6.85 | 信息 | ⭐ 低 KD + 高 CPC，极优质对比词 |
| kimi vs claude | 90 | 0 | $11.43 | 信息 | ⭐ KD=0，$11.43 超高 CPC，黄金词 |
| claude alternative | 260 | 18 | $3.12 | 信息 | ⭐ 中量低 KD |
| deepseek alternative | 390 | 12 | $3.27 | 信息 | ⭐ 同中国 AI 赛道，可对标 |
| chinese llm | 390 | 19 | $3.14 | 信息 | ⭐ 低 KD，Olares 布局点 |
| best chinese ai | 210 | 23 | $1.56 | 信息 | ⭐ 低 KD，中国 AI 品类词 |
| kimi vs deepseek | 40 | 22 | $0.00 | 信息 | ⭐ 低 KD，可覆盖开源权重比较 |
| kimi alternative | 30 | 0 | $3.91 | 信息 | ⭐ KD=0，对 Olares 价值极高 |
| kimi ai alternative | 20 | 0 | $4.00 | 信息 | ⭐ KD=0，量小但意图极准 |
| open source chatgpt alternative | 30 | 19 | $2.34 | 信息 | ⭐ 低 KD，自托管叙事切入 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kimi | 60,500 | 79 | $0.42 | 商业 | 品牌大词，排不动 |
| kimi k2.5 | 49,500 | 78 | $1.24 | 信息 | 品牌模型词，KD 高 |
| kimi ai | 22,200 | 86 | $0.88 | 商业 | 品牌词，KD 极高 |
| kimi k2 | 22,200 | 92 | $1.65 | 信息 | 模型词，KD=92 |
| moonshot ai | 5,400 | 81 | $1.32 | 商业 | 品牌词，KD 高 |
| kimi k2 thinking | 2,900 | 64 | $1.89 | 商业 | 功能词，中等竞争 |
| kimi code | 1,900 | 67 | $4.43 | 商业 | 编程助手词，KD 高 |
| kimi for coding | 1,900 | 45 | $4.73 | 信息/商业 | 编程场景词 |
| kimi agent | 260 | 32 | $1.89 | 信息 | ⭐ 中量，可做 agent 叙事 |
| long context llm | 90 | 37 | $8.16 | 信息 | ⭐ 低量高 CPC，超高意图 |
| china ai chatbot | 70 | 46 | $2.43 | 信息 | 中国 AI 品类词 |
| best free ai assistant | 140 | 34 | $2.15 | 信息 | ⭐ 低 KD，场景词 |
| local ai chatbot | 210 | 43 | $3.44 | 信息 | 本地 AI 场景词 |
| open source ai assistant | 170 | 49 | $3.26 | 信息 | 开源 AI 品类词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kimi api | 3,600 | 35 | $3.50 | 商业 | ⭐ kimi.ai 已排 #1，核心流量词 |
| kimi k2 api | 320 | 17 | $2.86 | 交易 | ⭐ KD=17，kimi.ai 已排 #1 |
| kimi k2 api pricing | 1,000 | 20 | $3.20 | 交易 | ⭐ kimi.ai 已排 #1 |
| kimi k2 pricing | 260 | 15 | $3.90 | 交易 | ⭐ KD=15，已排 #1 |
| kimi k2 huggingface | 320 | 73 | $0.00 | 商业 | HuggingFace 模型词 |
| kimi k2 model | 320 | 70 | $2.90 | 信息 | 模型信息词 |
| moonshot kimi | 260 | 70 | $0.99 | 信息 | 品牌关联词 |
| kimi k2 benchmark | 30 | 18 | $2.60 | 信息 | ⭐ 低 KD，技术评测词 |
| kimi k2 download | 90 | 35 | $1.56 | 信息 | ⭐ 部署信号词 |
| kimi open source | 110 | 47 | $6.34 | 信息 | 高 CPC，开源查询词 |
| is kimi ai safe | 140 | 20 | $0.00 | 信息 | ⭐ 低 KD，信任信号词 |
| is kimi ai free | 110 | 0 | $2.16 | 信息 | ⭐ KD=0，定价意图词 |
| kimi subscription | 90 | 0 | $4.35 | 交易 | ⭐ KD=0，定价词 |
| kimi ai review | 70 | 17 | $2.86 | 信息 | ⭐ 低 KD，评测词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kimi k2 ollama | 210 | 39 | $3.41 | 信息/商业 | ⭐ 核心部署词，Olares 直接切入 |
| run llm locally | 590 | 47 | $3.50 | 信息 | 本地运行 LLM 大类词 |
| kimi k2 local | 50 | 34 | $0.95 | 信息 | ⭐ 本地部署词 |
| run kimi k2 locally | 30 | 24 | $0.99 | 信息 | ⭐ 精确操作词，KD=24 |
| kimi k2 gguf | 40 | 0 | $0.00 | 信息/商业 | ⭐ KD=0，量化部署词 |
| kimi k2 vllm | 30 | 0 | $0.00 | 信息 | ⭐ KD=0，vLLM 部署词 |
| self hosted long context llm | 30 | 0 | $0.00 | 信息 | ⭐ KD=0，精准 Olares 场景词 |
| kimi k2 coding | 50 | 42 | $2.17 | 信息 | 编程场景词 |
| self hosted ai assistant | 20 | 0 | $4.37 | 信息 | ⭐ KD=0，高 CPC，精准自托管词 |
| open weight llm | 20 | 0 | $0.00 | 信息 | ⭐ KD=0，开放权重品类词 |
| privacy focused ai | 20 | 0 | $6.60 | 信息 | ⭐ KD=0，超高 CPC，隐私词 |
| kimi k2 vs deepseek | 50 | 6 | $0.00 | 信息 | ⭐ KD=6，开源对比词 |
| kimi k2 free | 50 | 25 | $1.13 | 信息 | ⭐ 免费使用意图 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Kimi K2 开放权重（Modified MIT）可在 Ollama on Olares 本地运行，数据完全私有，无中国服务器、无审查担忧——同时享受 256K 超长上下文，这是当前 Olares 本地大模型叙事中 context window 最长的可跑权重。** 叙事切入点有三轴：① 本地部署实操词（how to run / ollama / vllm）；② 数据隐私/审查规避词（is kimi safe / censored / china）；③ 对比闭源付费词（kimi vs claude / chatgpt alternative）。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| kimi k2 ollama | 210 | 39 | $3.41 | Olares + Ollama = 一键跑 Kimi K2，无需云服务器；Data stays local | ⭐⭐⭐ |
| kimi vs chatgpt | 110 | 9 | $6.85 | Kimi K2 本地 vs ChatGPT 云：隐私 + 成本 + 零审查——Olares 提供完整基础设施 | ⭐⭐⭐ |
| kimi vs claude | 90 | 0 | $11.43 | KD=0，CPC $11；本地 Kimi K2 vs Claude API：无订阅费、数据不外传 | ⭐⭐⭐ |
| kimi alternative | 30 | 0 | $3.91 | 最想要的对比词；Olares + Kimi K2 = Kimi 的自托管平替 | ⭐⭐⭐ |
| run kimi k2 locally | 30 | 24 | $0.99 | 操作型词，Olares 步骤文（install Ollama → pull kimi-k2 → run）精准覆盖 | ⭐⭐⭐ |
| self hosted long context llm | 30 | 0 | $0.00 | GEO 前哨；Olares + Kimi K2 = 256K context、完全自托管 | ⭐⭐⭐ |
| kimi k2 local | 50 | 34 | $0.95 | 本地运行意图，Olares 落地页直接切入 | ⭐⭐⭐ |
| deepseek alternative | 390 | 12 | $3.27 | 中量 + 低 KD；Kimi K2 on Olares = DeepSeek 的开源替代方案 | ⭐⭐⭐ |
| chinese llm | 390 | 19 | $3.14 | 中国 LLM 品类词；Olares 叙事：中国开源 LLM 的最佳本地运行方案 | ⭐⭐⭐ |
| is kimi ai safe | 140 | 20 | $0.00 | 信任/隐私意图；Olares 答案：本地跑 K2 则数据不经任何云服务器 | ⭐⭐⭐ |
| kimi k2 gguf | 40 | 0 | $0.00 | KD=0；量化 GGUF 部署词，Olares + KTransformers 叙事 | ⭐⭐ |
| kimi k2 vllm | 30 | 0 | $0.00 | KD=0；vLLM 部署词，可布局技术教程 | ⭐⭐ |
| self hosted ai assistant | 20 | 0 | $4.37 | KD=0，CPC $4.37；Olares 一键部署 Kimi K2 作为私有 AI 助手 | ⭐⭐⭐ |
| open weight llm | 20 | 0 | $0.00 | 开放权重品类认知词；GEO 前哨 | ⭐⭐ |
| privacy focused ai | 20 | 0 | $6.60 | KD=0，CPC $6.60；本地运行 = 隐私最佳，Olares 切入点 | ⭐⭐⭐ |
| kimi k2 vs deepseek | 50 | 6 | $0.00 | KD=6；两大中国开源权重对比，Olares 两者都能跑 | ⭐⭐ |
| best chinese ai | 210 | 23 | $1.56 | 中量 + 低 KD；Olares 叙事：本地运行中国最强开源 AI | ⭐⭐ |
| long context llm | 90 | 37 | $8.16 | 高 CPC 品类词；Kimi K2 on Olares = 256K 本地长上下文方案 | ⭐⭐ |
| kimi ai china | 20 | 0 | $0.83 | GEO；Olares 回答中国 AI 数据隐私顾虑 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| kimi vs chatgpt | 110 | 9 | $6.85 | 信息 | **主词候选** | KD=9 + CPC $6.85，强商业意图覆盖规则上提；Olares 叙事：本地 Kimi K2 vs ChatGPT 订阅费 |
| deepseek alternative | 390 | 12 | $3.27 | 信息 | **主词候选** | 中量低 KD；Kimi K2 on Olares = DeepSeek 替代方案，同一批用户群 |
| chinese llm | 390 | 19 | $3.14 | 信息 | **主词候选** | 中量低 KD；Olares 可运行中国最顶级开源 LLM，唯一完整本地化方案 |
| kimi k2 ollama | 210 | 39 | $3.41 | 信息/商业 | **主词候选** | 月量 210 + 同族合计（kimi k2 local/run locally/gguf）≥~350，部署意图极纯；Olares 直接切入 |
| best chinese ai | 210 | 23 | $1.56 | 信息 | **主词候选** | 中量低 KD；品类词，Olares 叙事：在 Olares 上跑中国最强开源 AI |
| kimi vs claude | 90 | 0 | $11.43 | 信息 | **主词候选** | KD=0 + CPC $11.43，战略级词；Olares 一次性购买 vs Claude 永久订阅 |
| kimi alternative | 30 | 0 | $3.91 | 信息 | **主词候选** | KD=0 + 强商业/Olares 切入意图，上提；Kimi K2 on Olares = Kimi 自托管版 |
| run kimi k2 locally | 30 | 24 | $0.99 | 信息 | **主词候选** | 同族（kimi k2 local + kimi k2 ollama）合计 ≥~300；操作型词，Olares 步骤文 |
| is kimi ai safe | 140 | 20 | $0.00 | 信息 | **主词候选** | 低 KD，中量；信任/隐私意图——Olares 答案：本地运行数据不出设备 |
| kimi api | 3,600 | 35 | $3.50 | 商业 | 次级 | kimi.ai 已排 #1 获大量流量；导入 API 开发者后续看 Olares 本地替代 |
| kimi k2 api pricing | 1,000 | 20 | $3.20 | 交易 | 次级 | kimi.ai 已排 #1；定价痛点=本地运行省钱的切入口 |
| kimi k2 pricing | 260 | 15 | $3.90 | 交易 | 次级 | kimi.ai 已排 #1；定价对比文辅助词 |
| kimi k2 benchmark | 30 | 18 | $2.60 | 信息 | 次级 | 低 KD，可并入 kimi vs chatgpt 对比文 |
| kimi ai review | 70 | 17 | $2.86 | 信息 | 次级 | 低 KD，并入 kimi alternative 文章 |
| kimi k2 free | 50 | 25 | $1.13 | 信息 | 次级 | 免费意图 + 本地运行 = 零订阅叙事 |
| kimi k2 download | 90 | 35 | $1.56 | 信息 | 次级 | 下载/部署词，并入本地运行文章 |
| self hosted long context llm | 30 | 0 | $0.00 | 信息 | GEO | 近零量但极准；Olares + Kimi K2 = 256K 自托管方案，抢 AI Overview 引用位 |
| kimi k2 gguf | 40 | 0 | $0.00 | 信息 | GEO | KD=0；量化部署词，FAQ 覆盖 |
| kimi k2 vllm | 30 | 0 | $0.00 | 信息 | GEO | KD=0；vLLM 部署词，技术前瞻段 |
| self hosted ai assistant | 20 | 0 | $4.37 | 信息 | GEO | KD=0，CPC $4.37，高价值；Olares 自托管 AI 助手定义词 |
| privacy focused ai | 20 | 0 | $6.60 | 信息 | GEO | KD=0，CPC $6.60；本地 LLM 隐私叙事，Perplexity 引用位 |
| is kimi ai censored | 0 | 0 | $0.00 | 信息 | GEO | 零量但高搜索意图；Olares 答案：本地权重无审查 |
| kimi ai china | 20 | 0 | $0.83 | 信息 | GEO | 中国 AI 数据隐私顾虑词；Olares 正面回答 |

---

## 核心洞见

1. **品牌护城河**：Kimi / Kimi K2 品牌词 KD 全在 78-92，几乎无法正面攻。kimi.ai 是 API 平台，品牌词流量集中在 kimi.com（另站）。Olares **不需要打品牌词**——切入点是部署词（KD 0-39）+ 对比词（KD 0-22）+ 隐私词（KD 0-20）。

2. **可复制的打法**：kimi.ai 的打法是"API 文档 SEO"——platform.kimi.ai 贡献 90% 流量，靠 `/docs/pricing/`、`/docs/models`、`/docs/guide/agent-support` 等功能文档页各自排名具体词。每次发布新模型（K2.5→K2.6）就自动产生新文档词（`kimi-k2.5 api pricing` / `kimi k2.6 quickstart`）——程序化内容扩词策略。

3. **对 Olares 最关键的词**：
   - **`kimi k2 ollama`**（210/月，KD 39）：已有真实搜索量的本地部署词，Olares + Ollama 直接对应
   - **`kimi vs chatgpt`**（110/月，KD 9）：最重要的对比词，CPC $6.85，Olares 叙事切入最自然
   - **`deepseek alternative / chinese llm`**（各 390/月，KD 12/19）：中国开源 LLM 品类词，量更大且 KD 低，Olares 可做中国最强开源模型的本地部署平台叙事

4. **最大攻击面**：
   - **数据隐私 / 审查顾虑**：`is kimi ai safe`（140/月，KD 20）、`is kimi ai censored`（GEO 词）——中国 AI 产品的天然弱点，Olares 本地运行 = 数据不经任何云服务器，无审查
   - **订阅费痛点**：Kimi Allegretto $39/月起才解锁 Agent Swarm + Kimi Code；API $0.95/M input 按量计费——Olares + Kimi K2 本地运行 = 零 API 费用
   - **VRAM 门槛**：K2 INT4 权重需 ~640GB VRAM（多 GPU 集群），本地运行门槛极高——这是一把双刃剑：量化版（GGUF / KTransformers）降低门槛但性能有所折损

5. **隐藏低 KD 金矿**：
   - `kimi vs claude`（KD=0，$11.43 CPC）——目前几乎无竞争，月量 90，CPC 极高
   - `kimi alternative`（KD=0，$3.91）；`kimi ai alternative`（KD=0，$4.00）
   - `self hosted ai assistant`（KD=0，CPC $4.37）；`privacy focused ai`（KD=0，CPC $6.60）
   - `kimi k2 gguf`（KD=0）；`kimi k2 vllm`（KD=0）——技术部署词，Olares 教程文章制高点

6. **GEO 前瞻布局**：
   - `"is kimi k2 censored?"` / `"does kimi collect data locally?"` / `"kimi k2 vs deepseek privacy"` ——这类隐私对比问题在 Perplexity / AI Overview 里有极高引用机会
   - `"self hosted long context llm 2026"` / `"run 256k context model locally"` ——Olares 可通过 FAQ 段抢占 AI Overview 引用位
   - `"how to run kimi k2 locally with ollama"` ——已出现在 phrase_questions 词表（0 量但语义极准）

7. **与既有分析的关联**：
   - kimi.ai 与 `olares-500-keywords` 现有词表的关联：`kimi k2 ollama`（210）、`chinese llm`（390）、`deepseek alternative`（390）均为新补充词，现有词表中无此品类
   - kimi.ai 的 SEO 体量（7,607 US 流量）远小于 kimi.com（~128K），说明 Moonshot 把 SEO 精力放在消费者侧；**API 开发者词的竞争真空**（kimi.ai 大量 KD<30 词已排 #1 但没有 Olares 相关内容做引流）是短期机会

---

*数据来源：SEMrush US 数据库（`domain_rank`, `resource_organic`, `domain_organic_subdomains`, `domain_organic_organic`, `phrase_these`, `phrase_related`, `phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
