# OpenRouter SEO 竞品分析报告

> 域名：openrouter.ai | SEMrush US | 2026-07-06
> OpenRouter = LLM API 聚合 / 路由网关——一个 OpenAI 兼容端点接入 300+ 模型、跨厂商自动路由与容灾，闭源 SaaS 品类事实标准。

---

## 项目理解（前置）

OpenRouter 是一层"LLM 统一网关"：开发者用一个 OpenAI 兼容的 API key，就能调用 OpenAI / Anthropic / Google / DeepSeek / Meta 等 300+ 模型，由 OpenRouter 负责在多家上游 provider 间做价格/延迟/可用性路由与故障切换。它把"接哪家模型、各家鉴权、限流、计费"这套碎活收敛成一个端点，靠在每次推理上抽成（约 5% 充值手续费 + BYOK 选项）赚钱。它同时靠 janitor.ai / chub.ai 等 AI 角色扮演前端把自己做成默认后端，获得大量跨界流量。

| 项目 | 内容 |
|------|------|
| 一句话定位 | LLM API 聚合/路由网关：一个 OpenAI 兼容端点接入 300+ 模型 |
| 开源 / 许可证 | **闭源** SaaS（无自托管版本）|
| 主仓库 | 无开源本体；仅提供 SDK / docs（openrouter.ai/docs）|
| 核心功能 | ① 统一 API 接 300+ 模型 ② 跨 provider 智能路由 + 容灾 ③ 用量/成本看板 ④ BYOK 自带上游 key ⑤ credits 充值计费 |
| 商业模式 / 定价 | 充值制 credits，推理按 token 走上游价 + 约 5% 手续费；BYOK 也收平台费 |
| 差异化 / 价值主张 | "一个 key 接全部模型"、免维护多家鉴权、自动挑最便宜/最快 provider、统一账单 |
| 主要竞品（初判）| LiteLLM（开源）、Portkey、Requesty、Helicone、Together AI、Eden AI、Unify |
| 公司/规模 | 公司 OpenRouter（创始人 Alex Atallah，OpenSea 联创）；ARR ~$50M、估值 ~$1.3B（公开报道，引用前复核）|
| Olares 平替 | **LiteLLM / Bifrost**——均**已在 Olares Market 上架**（[litellm](/Users/pengpeng/seo/directions/market/reports/litellm.md) / [bifrost](/Users/pengpeng/seo/directions/market/reports/bifrost.md)）|
| 来源 | openrouter.ai、openrouter.ai/docs、公开融资报道；Olares Market 见 market/apps.md |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | openrouter.ai |
| SEMrush Rank | **16,833** |
| 自然关键词数 | 23,062 |
| 月自然流量（US）| **132,650** |
| 自然流量估值 | **$482,947/月** |
| 付费关键词数 | **0**（不投 Google Ads）|
| 月付费流量 | 0 |
| 排名 1-3 位 | 1,374 词 |
| 排名 4-10 位 | 4,022 词 |
| 排名 11-20 位 | 3,177 词 |

> 与上版（2026-07-02）对比：Rank 17,056→16,833（略升）、关键词 24,029→23,062、月流量 129,694→132,650、估值 $469K→$483K。基本盘稳定，无付费投放。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| openrouter.ai（主站）| 22,992 | 132,379 | 99.80% |
| status.openrouter.ai | 60 | 267 | 0.20% |
| trust.openrouter.ai | 7 | 4 | 0% |
| multimedia-explorer / tool-playground | 1-2 | 0 | 0% |

流量几乎 100% 集中在主站——OpenRouter **没有** Lovable 那种 `docs.` / `guides.` 内容子域打法，SEO 靠的是**主站结构**（品牌词 + 海量模型词页 `/deepseek/…`、`/anthropic/…`、`/apps/…`）而非内容营销。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| openrouter | 1 | 74,000 | 63 | $3.10 | 18,352 | 品牌 | /sign-in |
| openrouter | 2 | 74,000 | 63 | $3.10 | 9,768 | 品牌 | /models |
| openrouter | 3 | 74,000 | 63 | $3.10 | 6,068 | 品牌 | /pricing |
| open router | 1 | 14,800 | 62 | $3.74 | 3,670 | 品牌 | /sign-in |
| openrouter | 5 | 74,000 | 63 | $3.10 | 2,590 | 品牌 | /chat |
| openrouter.ai | 1 | 2,900 | 75 | $3.73 | 2,320 | 导航 | / |
| openrouter.ai api | 1 | 2,900 | 70 | $5.12 | 2,320 | 集成 | /docs/quickstart |
| openrouter ai | 1 | 8,100 | 61 | $3.73 | 2,008 | 品牌 | /sign-in |
| **chub ai**（借力）| 3 | 90,500 | 47 | $1.75 | 1,629 | 品牌(第三方)| /apps/chub-ai |
| openrouter | 6 | 74,000 | 63 | $3.10 | 1,628 | 品牌 | /openrouter/free |
| **janitor ai**（借力）| 6 | 1,500,000 | 56 | $1.69 | 1,500 | 品牌(第三方)| /apps/janitor-ai |
| open router ai | 1 | 1,600 | 54 | $3.60 | 1,280 | 品牌 | /sign-in |
| openrouter api | 1 | 4,400 | 66 | $4.78 | 1,091 | 集成 | /docs/quickstart |
| openrouterai | 1 | 1,300 | 27 | $3.73 | 1,040 | 品牌 | / |
| deepseek/deepseek-r1-0528:free | 1 | 3,600 | 24 | $0 | 892 | 模型 | /deepseek/… |
| openrouter glm 4.6 | 1 | 1,000 | 33 | $0 | 800 | 模型 | /z-ai/glm-4.6 |
| openrouter models | 1 | 1,000 | 32 | $4.71 | 800 | 商业 | /models |
| deepseek | 14 | 1,220,000 | 100 | $1.35 | 732 | 模型 | /deepseek |
| openrouter api key | 1 | 880 | 26 | $3.94 | 704 | 集成 | /docs/api/reference/authentication |
| xiaomi/mimo-v2-flash:free | 1 | 1,900 | 33 | $0 | 471 | 模型 | /xiaomi/… |
| grok 4 | 5 | 33,100 | 56 | $0.86 | 430 | 模型 | /x-ai/grok-4 |
| best free openrouter ai models for programming | 1 | 1,900 | **15** | $0 | 250 | 信息 | /collections/programming |
| claude code with openrouter | 1 | 1,900 | 24 | $11.38 | 250 | 信息 | /docs/cookbook/…/claude-code-integration |
| openrouter free models | 1 | 390 | 31 | $3.23 | 312 | 商业 | /collections/free-models |
| openrouter deepseek | 1 | 390 | 29 | $3.60 | 312 | 商业 | /deepseek |
| openrouter pricing | 1 | 880 | 29 | $4.05 | 218 | 商业 | /pricing |
| free uncensored api | 1 | 880 | **9** | $0 | 218 | 信息 | /…dolphin-mistral…:free |

> 大量流量来自**品牌词多位置霸屏**（openrouter 在 /sign-in、/models、/pricing、/chat、/openrouter/free 各占一位）+ **误拼变体**（openrputer / openruter / openroute / openeouter / operouter / openrounter / openroter / penrouter…全部排名第 1）+ **模型词程序化页**（每个模型一个 URL：/deepseek/…、/z-ai/glm-4.6、/x-ai/grok-4）。

### 付费词

**OpenRouter 完全不投 Google Ads**（付费关键词 = 0）——纯靠自然流量与品牌心智，与 Lovable 的 SEM 重投打法完全相反。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| together ai | 12,100 | 66 | $5.44 | 商业 | 竞品品牌，难 |
| **litellm** | 14,800 | 56 | $5.42 | 导航 | **开源平替本体**（Olares Market 已上架）|
| bifrost | 8,100 | 61 | $0 | 导航 | 词义泛（另有同名品），产品词见下 |
| requesty | 4,400 | 30 | $7.37 | 导航 | 竞品品牌 |
| portkey | 2,400 | 41 | $2.68 | 导航 | 竞品品牌 |
| eden ai | 1,900 | 45 | $4.40 | 商业 | 竞品品牌 |
| helicone | 1,300 | 36 | $4.87 | 导航 | 竞品品牌 |
| one api | 1,000 | 36 | $4.21 | 信息 | 开源聚合（中文圈）|
| openpipe | 880 | 50 | $9.14 | 商业 | 竞品品牌 |
| unify ai | 480 | 36 | $28.20 | 信息 | 竞品，超高 CPC |
| litellm proxy | 480 | 53 | $6.67 | 集成 | LiteLLM 自托管形态 |
| **openrouter alternatives** | 320 | **3** | $3.35 | 商业 | ⭐ KD=3！|
| **openrouter vs litellm** | 260 | **20** | $0 | 对比 | ⭐ 直接切自托管 |
| **openrouter alternative** | 170 | **8** | $3.35 | 商业 | ⭐ KD=8！|
| requesty ai | 140 | **14** | $9.72 | 商业 | ⭐ 高 CPC |
| **litellm alternative** | 140 | **2** | $3.70 | 商业 | ⭐ KD=2！|
| litellm vs openrouter | 140 | 22 | $4.57 | 对比 | ⭐ 反向对比 |
| bifrost llm | 50 | **0** | $7.55 | 导航 | ⭐ 平替本体产品词 |
| portkey vs litellm | 30 | **10** | $3.43 | 对比 | ⭐ |
| openrouter alternative free | 20 | **0** | $2.31 | 商业 | ⭐ 空白 |
| free openrouter alternative | 20 | **0** | $2.22 | 商业 | ⭐ 空白 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| free large language models | 1,600 | 49 | $3.14 | 信息 | 免费模型需求 |
| ai gateway | 880 | 53 | $13.57 | 信息 | 品类大词，超高 CPC |
| free llm | 720 | 36 | $2.35 | 信息 | |
| llm router | 590 | 45 | $4.14 | 信息 | |
| **llm gateway** | 480 | **25** | $5.63 | 信息 | ⭐ 核心品类词 |
| ai router | 390 | 51 | $3.19 | 信息 | |
| **model router** | 170 | **25** | $2.39 | 信息 | ⭐ |
| llm proxy | 170 | 50 | $5.90 | 信息 | |
| **open source ai gateway** | 170 | **29** | $3.71 | 信息 | ⭐ Olares 前哨 |
| ai gateway open source | 30 | **0** | $14.75 | 信息 | ⭐ 空白 + 高 CPC |
| unified llm api | 20 | **0** | $7.58 | 信息 | ⭐ 空白 |
| llm api aggregator | 20 | **0** | $3.56 | 信息 | ⭐ 空白（品类定义词）|

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| openrouter api | 5,400 | 60 | $5.32 | 集成 | 难 |
| is openrouter reliable | 1,900 | 37 | $0 | 信息 | 可靠性顾虑（攻击面）|
| openrouter pricing | 880 | **29** | $4.05 | 商业 | ⭐ 定价痛点 |
| what is openrouter | 880 | 59 | $4.21 | 信息 | |
| openrouter api key | 880 | **26** | $3.94 | 集成 | ⭐ |
| openrouter models | 480 | 32 | $5.34 | 商业 | |
| openrouter deepseek | 480 | **29** | $2.85 | 商业 | ⭐ |
| openrouter free models | 390 | 31 | $3.23 | 商业 | |
| is openrouter free | 390 | 40 | $0 | 信息 | 定价痛点 |
| openrouter free | 320 | 47 | $6.07 | 信息 | |
| openrouter credits | 320 | 41 | $0 | 商业 | **credits 计费痛点** |
| openrouter status | 320 | **20** | $0 | 导航 | ⭐ 宕机顾虑 |
| openrouter rate limits | 210 | **16** | $0 | 信息 | ⭐ 限流痛点 |
| openrouter github | 210 | 38 | $0 | 信息 | 用户误以为开源 |
| **openrouter mcp** | 170 | **7** | $0 | 信息 | ⭐ KD=7！|
| openrouter docs | 170 | 49 | $0 | 信息 | |
| openrouter image generation | 140 | **17** | $0 | 交易 | ⭐ |
| openrouter embeddings | 140 | **7** | $0 | 集成 | ⭐ KD=7！|
| openrouter claude code | 110 | 33 | $22.98 | 信息 | 超高 CPC |
| openrouter privacy | 110 | **27** | $0 | 信息 | ⭐ 隐私痛点 |
| how to use openrouter | 90 | **26** | $0 | 信息 | ⭐ |
| openrouter cost | 90 | 32 | $1.29 | 信息 | |
| openrouter vs | 70 | **11** | $4.40 | 对比 | ⭐ |
| openrouter byok | 50 | **21** | $0 | 集成 | ⭐ 自带 key |
| openrouter n8n | 40 | **26** | $3.50 | 集成 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| litellm docker image | 320 | 31 | $0 | 信息 | LiteLLM 自托管 |
| litellm docker | 140 | 43 | $18.00 | 信息 | 部署词，高 CPC |
| litellm self hosted | 40 | **0** | $0 | 新兴 | ⭐ 空白 |
| ai gateway open source | 30 | **0** | $14.75 | 信息 | ⭐ 空白 + $14.75 |
| open source llm gateway | 20 | **0** | $0 | 新兴 | ⭐ 空白 |
| self hosted ai gateway | 20 | **0** | $2.75 | 新兴 | ⭐ 空白 |
| litellm kubernetes | 20 | **0** | $0 | 新兴 | ⭐ 空白 |
| openrouter open source | 20 | **0** | $0 | 新兴 | ⭐ 需求信号 |
| self hosted llm gateway | 0 | 0 | $0 | 新兴 | GEO 占位（语义完美）|
| self hosted openrouter | 0 | 0 | — | 新兴 | GEO 占位 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：OpenRouter 是闭源 SaaS，每次推理抽成、数据要过它的服务器、宕机时你跟着挂（`is openrouter reliable` 1,900、`openrouter status` 320）。Olares Market 已上架 LiteLLM 与 Bifrost——同样 OpenAI 兼容、同样接 100+ 模型，但自托管：BYOK 直连上游无中间抽成、数据留在你自己的 Olares、还能指向本地 Ollama 模型做到零边际成本。一句话：把"租来的路由网关"换成"你自己拥有的路由网关"。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| **litellm** | 14,800 | 56 | $5.42 | ⭐⭐⭐ 平替本体已在 Olares Market——"在 Olares 上一键自托管 LiteLLM"教程/落地页 |
| **openrouter alternatives** | 320 | **3** | $3.35 | ⭐⭐⭐ KD=3！自托管 OpenRouter 替代清单，LiteLLM/Bifrost on Olares 居首 |
| **openrouter alternative** | 170 | **8** | $3.35 | ⭐⭐⭐ KD=8！同上，单数版对比页 |
| **openrouter vs litellm** | 260 | 20 | $0 | ⭐⭐⭐ 正面对比：托管抽成 vs 自托管零抽成（Olares 部署 LiteLLM）|
| litellm vs openrouter | 140 | 22 | $4.57 | ⭐⭐⭐ 反向对比词，同页覆盖 |
| **litellm alternative** | 140 | **2** | $3.70 | ⭐⭐ KD=2！比 LiteLLM 更省心＝Olares 一键部署 + Bifrost 备选 |
| **llm gateway** | 480 | 25 | $5.63 | ⭐⭐⭐ 核心品类词：self-hosted LLM gateway 首选 = Olares |
| **openrouter mcp** | 170 | **7** | $0 | ⭐⭐ KD=7！自托管网关 + MCP，本地 Agent 直连，几乎零竞争 |
| open source ai gateway | 170 | 29 | $3.71 | ⭐⭐⭐ Olares Market 就是答案（LiteLLM/Bifrost 均开源）|
| openrouter embeddings | 140 | **7** | $0 | ⭐⭐ KD=7！本地 Embedding + 网关，数据不出设备 |
| openrouter image generation | 140 | 17 | $0 | ⭐ 本地 ComfyUI/SD + 网关，无 credits |
| openrouter privacy | 110 | 27 | $0 | ⭐⭐⭐ 直击隐私痛点：自托管＝推理与数据都不出你的 Olares |
| bifrost llm | 50 | **0** | $7.55 | ⭐⭐⭐ 平替本体产品词，KD=0，Olares Market 已上架 |
| openrouter alternative free | 20 | **0** | $2.31 | ⭐⭐⭐ "免费替代"＝自托管 + 本地模型零 API 费 |
| ai gateway open source | 30 | **0** | $14.75 | ⭐⭐ KD=0 + $14.75 CPC，纯空白 |
| self hosted ai gateway | 20 | **0** | $2.75 | ⭐⭐⭐ 语义完美，抢占 |
| open source llm gateway | 20 | **0** | $0 | ⭐⭐⭐ 语义完美，抢占 |
| litellm self hosted | 40 | **0** | $0 | ⭐⭐ 部署教程词，Olares 一键 |
| openrouter open source | 20 | **0** | $0 | ⭐⭐ 需求信号：用户找"开源版 OpenRouter"→给 LiteLLM/Bifrost on Olares |
| self hosted llm gateway / self hosted openrouter | 0 | 0 | — | ⭐⭐⭐ GEO 占位，语义与 Olares 完美契合 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| litellm | 14,800 | 56 | $5.42 | 导航 | 主词候选 | 平替本体品牌词，撑"在 Olares 上自托管 LiteLLM"教程/落地页（KD 高但目标是内容页而非抢品牌位）|
| openrouter alternatives | 320 | 3 | $3.35 | 商业 | 主词候选 | KD=3！自托管 OpenRouter 替代清单，LiteLLM/Bifrost on Olares 主打——最高性价比主词 |
| openrouter vs litellm | 260 | 20 | $0 | 对比 | 主词候选 | 托管抽成 vs 自托管零抽成对比文，同页吃 litellm vs openrouter（140）|
| openrouter alternative | 170 | 8 | $3.35 | 商业 | 主词候选 | KD=8！与复数版同簇，单/复数双落地 |
| llm gateway | 480 | 25 | $5.63 | 信息 | 主词候选 | 核心品类词，"best self-hosted LLM gateway"清单（Olares 部署 LiteLLM/Bifrost）|
| openrouter pricing | 880 | 29 | $4.05 | 商业 | 主词候选 | 定价/抽成攻击面，导向"零抽成自托管"对比 |
| litellm alternative | 140 | 2 | $3.70 | 商业 | 次级 | KD=2！并入替代簇，Bifrost/Olares 更省心 |
| openrouter mcp | 170 | 7 | $0 | 信息 | 次级 | KD=7！自托管网关 + MCP 给本地 Agent，几乎零竞争 |
| openrouter embeddings | 140 | 7 | $0 | 集成 | 次级 | KD=7！本地 Embedding + 网关，数据不出设备 |
| openrouter api key | 880 | 26 | $3.94 | 集成 | 次级 | 集成词，教程页顺带覆盖 BYOK 自托管 |
| open source ai gateway | 170 | 29 | $3.71 | 信息 | 次级 | Olares Market 即答案，并入品类清单 |
| openrouter privacy | 110 | 27 | $0 | 信息 | 次级 | 隐私痛点，自托管叙事最强共鸣点 |
| is openrouter reliable | 1,900 | 37 | $0 | 信息 | 次级 | 可靠性顾虑高量词，自托管＝不依赖别人的 status 页 |
| bifrost llm | 50 | 0 | $7.55 | 导航 | 次级 | 平替本体产品词，KD=0，Olares Market 已上架 |
| openrouter alternative free | 20 | 0 | $2.31 | 商业 | GEO | "免费替代"＝本地模型零 API 费，抢引用位 |
| self hosted llm gateway | 0 | 0 | — | 新兴 | GEO | 近零量语义完美契合 Olares，GEO 占位 |
| open source llm gateway | 20 | 0 | $0 | 新兴 | GEO | 空白词，权威内容抢 AI Overview 引用 |

---

## 核心洞见

1. **品牌护城河极硬，且靠"多位置霸屏 + 误拼变体 + 模型程序化页"三件套，不靠内容营销——正面刚品牌词无胜算。** `openrouter`（74K）在 /sign-in、/models、/pricing、/chat、/openrouter/free 各占一个排名位；`openrouter`/`open router`/`openrouter ai` 三个主品牌变体加上十几个误拼（openrputer / openruter / openroute…全排第 1）几乎垄断品牌流量。这类心智护城河 Olares 无法也不必去抢。

2. **可复制的打法是"模型词程序化页" + "第三方前端借力"，不是买大词。** OpenRouter **完全不投 Google Ads**，却靠两招吃流量：① 每个模型一个 URL（`/deepseek/deepseek-r1-0528:free`、`/z-ai/glm-4.6`、`/x-ai/grok-4`）程序化承接"模型名 + free/api"长尾；② 靠 `janitor ai`（150 万）、`chub ai`（9 万）等 AI 角色扮演前端把自己做成默认后端，反向获得跨界流量。Olares Market 完全可对每个可自托管模型/应用做同构的 "run X locally / X on Olares" 落地页矩阵。

3. **对 Olares 最关键的三个词：`openrouter alternatives`（320, KD3）、`openrouter alternative`（170, KD8）、`openrouter vs litellm`（260, KD20）。** 三者共同指向一个真实需求——用户在主动找"OpenRouter 的自托管/开源替代"。而 Olares Market **已经上架 LiteLLM 和 Bifrost 两个 OpenAI 兼容的自托管网关**，等于替代方案现成。一篇"self-hosted OpenRouter alternative（用 Olares 一键部署 LiteLLM/Bifrost）"可同时吃下这三词，KD 极低、意图极准。

4. **最大攻击面 = credits 计费 + 抽成 + 可靠性/隐私依赖。** `openrouter pricing`（880）、`openrouter credits`（320）、`is openrouter free`（390）、`openrouter rate limits`（210, KD16）、`is openrouter reliable`（1,900）、`openrouter status`（320, KD20）、`openrouter privacy`（110, KD27）、问题词 `how does openrouter make money`（70）密集出现——用户对"每次调用被抽成、限流、宕机要看它脸色、数据过它服务器"高度敏感。Olares 叙事直击此处：**自托管 = 无中间抽成、无速率闸门、不依赖别人的 status 页、推理与数据都不出你的设备**。

5. **隐藏低 KD 金矿：`litellm alternative`（KD2）、`openrouter mcp`（KD7）、`openrouter embeddings`（KD7）、`llm gateway`（KD25）、`open source ai gateway`（KD29）。** 量不大（140-480）但竞争几乎为零，且 `openrouter mcp`/`openrouter embeddings` 恰好落在 Olares 的本地 Agent + 本地向量场景上，配合已上架的 LiteLLM/Bifrost 可低成本占位。

6. **GEO 前瞻布局：`self hosted llm gateway`（KD0）、`open source llm gateway`（KD0）、`self hosted ai gateway`（KD0）、`ai gateway open source`（KD0，CPC $14.75）、`openrouter alternative free`（KD0）、`self hosted openrouter`（近零量）。** 这些词量小甚至为 0，但语义与 Olares 完美契合。发布一篇权威的 "self-hosted / open-source LLM gateway" 指南，抢 AI Overview / Perplexity 的引用位。

7. **与既有分析的关联：** 本报告的自托管网关叙事与 `olares-500-keywords` 的「本地 LLM」「AI 基础设施」分类互补，也与 tech-stack 方向的 AI 基础设施（推理 API / 网关）呼应。建议把 "self-hosted LLM gateway / OpenRouter alternative" 作为独立子品类补入 500 词表——目前该表尚缺"LLM 网关"这一层。旧报告（2026-07-02）已识别的 `openrouter alternative`（KD8）、`openrouter mcp`（KD7）、janitor/chub 借力观察，本版保留并印证；新增了 `openrouter alternatives`（KD3）、`litellm alternative`（KD2）、`llm gateway`（KD25）品类词与完整的定价/可靠性攻击面词群，并把平替从"Ollama/LiteLLM"更正为 Olares Market 现成的 **LiteLLM + Bifrost**。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / domain_organic_organic / phrase_these / phrase_related / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
