# Cohere SEO 竞品分析报告

> 域名：cohere.com | SEMrush us | 2026-07-07
> Cohere = 企业级 LLM / 嵌入 / 重排提供商（Command 模型 + Embed + Rerank，主打企业 RAG / 私有检索；ARR ~$500M、估值 ~$7B）

---

## 项目理解（前置）

Cohere 是面向**企业**的基础模型公司，2019 年由 Aidan Gomez（Transformer 论文《Attention Is All You Need》合著者）、Nick Frosst、Ivan Zhang 创立，总部多伦多。它不做 to-C 聊天机器人，而是把 **Command（生成式 LLM）+ Embed（文本嵌入）+ Rerank（重排）** 三件套作为企业 RAG / 检索增强 / 私有部署的 API 与私有化产品卖给金融、医疗、政企客户；2025 年推出 **North**（企业 Agent 平台）。差异化是"**企业级 + 可私有部署 + 多语言 + RAG 全链路（嵌入→重排→生成）**"，而非追求消费级榜单排名。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 企业级基础模型公司：Command LLM + Embed 嵌入 + Rerank 重排，主打 RAG / 私有部署 |
| 开源 / 许可证 | **闭源商业 API**；Command / Aya 权重在 HuggingFace 以 **CC-BY-NC（非商用）** 放出，Embed / Rerank 仅 API，无开源权重 |
| 主仓库 | 无开源主仓库（SDK `cohere-ai/cohere-python` 是客户端）；模型页 huggingface.co/CohereLabs |
| 核心功能 | ① Command 系列 LLM（Command A / R / R+）② Embed 嵌入模型（Embed v4，多语言/多模态）③ Rerank 重排 ④ North 企业 Agent ⑤ 私有/VPC 部署 |
| 商业模式 / 定价 | 纯 SaaS API 按量计费（Embed / Rerank / Command 按 token 或按次）＋企业私有部署合同；有免费试用额度 |
| 差异化 / 价值主张 | 企业安全合规 + 可私有部署（VPC/on-prem）+ 多语言 + RAG 全栈（嵌入+重排+生成一体） |
| 主要竞品（初判）| OpenAI / Anthropic（生成）；嵌入&重排侧 **Voyage AI、Jina AI、OpenAI Embeddings**；开源侧 **BGE / bge-reranker、nomic-embed、sentence-transformers** |
| Olares Market | 平替 **BGE-M3 + bge-reranker** 未做成独立上架应用；可经 Ollama / text-embeddings-inference / Xinference 在 Olares 上本地跑（自托管嵌入/重排服务） |
| 来源 | cohere.com、docs.cohere.com、cohere.com/pricing、huggingface.co/CohereLabs、公开融资报道（估值/ARR）|

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | cohere.com |
| SEMrush Rank | 80,889 |
| 自然关键词数 | 4,940 |
| 月自然流量（US）| 24,438 |
| 自然流量估值 | **$109,108/月** |
| 付费关键词数 | 52 |
| 月付费流量 | 836 |
| 付费流量估值 | $2,542/月 |
| 排名 1-3 位 | 255 词 |
| 排名 4-10 位 | 553 词 |
| 排名 11-20 位 | 951 词 |

> 结构上是一个**中量级、强品牌驱动**的站点：$3999 级别的付费投放几乎可忽略（52 词/$2.5K），流量几乎全靠自然，且高度集中在品牌词。1-3 位只有 255 词、11-20 位却多达 951 词——大量词卡在第二页，说明**通用品类词排不上去**，头部流量被品牌词垄断。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| cohere.com（主站）| 4,047 | 22,277 | 91.16% |
| docs.cohere.com | 703 | 1,585 | 6.49% |
| dashboard.cohere.com | 84 | 548 | 2.24% |
| partners.cohere.com | 45 | 20 | 0.08% |
| trustcenter.cohere.com | 17 | 4 | 0.02% |
| portal.enterprise.cohere.com | 19 | 3 | 0.01% |
| 其余（status/support/shop/labscommunity）| 1-21 | 0-1 | ~0% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| cohère（音调变体） | 1 | 12,100 | 76 | $4.27 | 9,680 | 导航 | / |
| cohere ai | 1 | 2,900 | 85 | $6.83 | 2,320 | 导航 | / |
| cohere | 2 | 33,100 | 79 | $7.13 | 860 | 导航 | / |
| cohere's（变体） | 1 | 590 | 62 | — | 472 | 导航 | / |
| cohere（位置 3） | 3 | 33,100 | 79 | $7.13 | 463 | 导航 | /careers |
| cohere rerank | 1 | 480 | 39 | $10.89 | 384 | 导航 | /rerank |
| command-r | 1 | 2,400 | 51 | $3.98 | 316 | 信息 | docs…/docs/command-r |
| cohere（位置 6） | 6 | 33,100 | 79 | $7.13 | 264 | 导航 | docs…/the-cohere-platform |
| cohere api pricing | 1 | 320 | 30 | — | 256 | 导航+交易 | /pricing |
| comnorth（误拼） | 1 | 1,900 | 42 | — | 250 | 信息 | /north |
| cohere careers | 1 | 1,000 | 21 | $3.60 | 248 | 商业 | /careers |
| cohere labs | 1 | 260 | 56 | $8.62 | 208 | 导航 | /research |
| cohere company | 1 | 260 | 69 | $5.15 | 208 | 信息+导航 | / |
| cohere north | 1 | 260 | 36 | $12.22 | 208 | 导航 | /north |
| cohere news | 1 | 1,300 | 34 | — | 171 | 信息 | /newsroom |
| cohere pricing | 1 | 210 | 30 | $11.28 | 168 | 导航+交易 | /pricing |
| cohere reranker | 1 | 210 | 32 | $8.47 | 168 | 导航 | /rerank |
| compass（借力大词） | 34 | 550,000 | 83 | $0.22 | 165 | 信息+交易 | /compass |
| cohere transcribe | 1 | 590 | 31 | $2.31 | 146 | 信息+交易 | /blog/transcribe |
| what is a neural network（借力）| 17 | 90,500 | 88 | $0.54 | 135 | 信息 | /blog/what-is-a-neural-network |
| cohere provider portal（医疗污染）| 4 | 12,100 | 38 | $4.32 | 121 | 导航 | dashboard…/login |
| coheres（变体） | 2 | 2,400 | 49 | $7.13 | 105 | 信息 | / |
| ivan zhang cohere chinese founder…| 1 | 720 | 20 | — | 95 | 信息 | /about |
| cohere login | 2 | 720 | 29 | — | 95 | 导航+交易 | dashboard…/login |
| command r | 1 | 720 | 45 | $4.84 | 95 | 信息 | docs…/command-r |
| cohere health（医疗污染）| 8 | 14,800 | 34 | $5.97 | 88 | 导航 | /solutions/healthcare |
| command r+ | 1 | 320 | 37 | $3.58 | 79 | 信息 | docs…/command-r-plus |
| cohere api | 1 | 320 | 56 | $7.08 | 79 | 信息 | docs…/reference/about |
| cohere health rpa automation…（客户词）| 1 | 590 | 19 | — | 77 | 信息 | /blog/ensemble-cohere… |
| coding generation（借力）| 3 | 2,900 | 64 | $3.82 | 69 | 信息 | /blog/ai-code-generation |
| fine tune（借力）| 5 | 2,900 | 57 | $9.85 | 69 | 信息 | /blog/fine-tuning |
| cohere for ai | 1 | 70 | 42 | $7.87 | 56 | 导航+交易 | /research |
| cohere rerank documentation | 1 | 70 | 32 | — | 56 | 导航+交易 | docs…/rerank |
| cohere api key | 1 | 210 | **18** | $5.88 | 52 | 导航 | dashboard…/login |
| embedding（借力）| 9 | 5,400 | 68 | $5.25 | 48 | 信息 | /blog/embedding-models |
| cohere provider login（医疗污染）| 3 | 2,400 | 36 | $8.17 | 43 | 导航+交易 | dashboard…/login |
| command a | 1 | 320 | 46 | — | 42 | 信息 | /blog/command-a |
| large language models definition（借力）| 8 | 1,900 | 75 | $0.42 | 41 | 信息 | /blog/large-language-models |
| cohere llm university | 1 | 50 | 33 | $5.36 | 40 | 信息+导航 | /llmu |

> 洞察：① 自然流量 **90%+ 是品牌词及其误拼/音调变体**（cohère / cohere ai / coheres / cohereai…全排第 1）；② 大量博客借力词（compass 55 万、what is a neural network 9 万、embedding 5.4 万、fine tune 2.9 万）挂在第二~三页吃残量，靠内容量堆；③ **"cohere" 品牌被两家同名公司严重污染**——医疗保险公司 **Cohere Health**（cohere health 14,800 / cohere provider login 2,400 / cohere provider portal 12,100）抢走同名搜索，是 Cohere AI 的长期 SEO 隐患。

### 付费词（Google Ads，按流量排序）

投放极轻（52 词），且买的是一批**与产品几乎无关的杂词**导向 /north 落地页，像是宽泛再营销/受众测试，不是清晰的品类拦截：

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| discovaz | 1 | 3,600 | $2.67 | /north |
| ai powered answer engine | 1 | 2,400 | $6.38 | /north |
| 天工超级智能体 | 1 | 1,900 | $2.24 | /north |
| hanging face（误拼）| 2 | 5,400 | — | /customization |
| free humanize ai | 1 | 1,300 | $0.95 | /north |
| free ai tools | 5 | 5,400 | $2.80 | /north |
| enterprise search | 6 | 1,600 | $21.31 | /rerank |
| rogo ai | 4 | 3,600 | $8.30 | /solutions/financial-services |
| deepseek models | 2 | 1,000 | $4.72 | /customization |
| 嵌入模型排行榜 | 1 | 390 | — | /embed |

> 付费打法**没有可复制价值**：预算小、词杂、落地页错配。唯一有意图的信号是 `enterprise search`（$21.31 CPC）导向 /rerank——印证"企业检索/重排"是它最愿意花钱的商业场景。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| voyage ai | 1,900 | 55 | $6.53 | 导航 | 嵌入/重排最直接竞品品牌词 |
| jina ai | 1,600 | 79 | $5.70 | 导航 | 嵌入/重排竞品（有开源权重）|
| jina embeddings | 90 | 43 | — | 信息+交易 | 竞品产品词 |
| jina reranker | 50 | 33 | — | 信息+交易 | 竞品重排词 |
| cohere competitors | 30 | 0 | $8.18 | — | ⭐ 近零 KD |
| cohere alternatives | 20 | 0 | $4.08 | — | ⭐ 替代词，先发占位 |
| cohere vs openai | 20 | 0 | — | — | ⭐ 对比词 |
| cohere vs anthropic | 20 | 0 | — | — | ⭐ 对比词 |
| cohere vs mistral | 20 | 0 | — | — | ⭐ 对比词 |
| cohere alternative | 0 | 0 | — | — | 新兴，GEO 占位 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| rag | 135,000 | 95 | $2.96 | 信息 | 品类顶级大词，排不动 |
| retrieval augmented generation | 8,100 | 95 | $3.67 | 信息 | 同上 |
| semantic search | 5,400 | 71 | $3.01 | 信息 | 高量高 KD |
| enterprise search | 1,600 | **31** | $21.31 | 信息 | ⚡ 高 CPC($21)+中等 KD |
| vector embeddings | 1,300 | 69 | $2.47 | 信息 | |
| embedding models | 1,000 | **25** | $2.58 | 信息 | ⭐ 量大 KD 低，核心机会 |
| embedding model | 880 | 57 | $1.52 | 信息 | 单数版 KD 偏高 |
| enterprise llm | 260 | **20** | $8.14 | 信息 | ⭐ KD20 + 高 CPC |
| reranker | 260 | 51 | $3.56 | 信息 | 品类词 |
| best embedding model | 210 | **27** | — | 商业 | ⭐ listicle 主词 |
| rerank | 170 | **34** | — | 信息 | 品类词（临界）|
| reranking | 140 | 43 | — | 信息 | |
| best embedding model for rag | 140 | **29** | $2.40 | 商业 | ⭐ 高契合 listicle |
| text embedding | 390 | 50 | $6.27 | 信息 | |
| rerank model | 90 | 38 | — | 信息 | |
| embedding api | 50 | 51 | $3.85 | 信息 | |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| command r | 720 | 45 | $4.84 | 信息 | 模型词 |
| cohere rerank | 480 | 39 | $10.89 | 导航 | 核心差异化功能词，CPC $10.9 |
| command r+ | 390 | 39 | $3.70 | 信息 | 模型词 |
| cohere api | 320 | 56 | $7.08 | 信息 | 集成词 |
| cohere api pricing | 320 | 30 | — | 导航+交易 | 价格词 |
| cohere pricing | 260 | **26** | $7.83 | 导航 | ⭐ 价格词 KD26 |
| cohere api key | 210 | **18** | $5.88 | 导航 | ⭐ KD18 集成词 |
| cohere reranker | 210 | 32 | $8.47 | 导航 | rerank 变体 |
| cohere embeddings | 140 | 41 | $3.25 | 导航+交易 | |
| cohere command a | 110 | 50 | $9.22 | 交易 | |
| cohere embed v4 | 90 | 37 | $11.29 | 信息+交易 | 最新嵌入模型，CPC $11.3 |
| cohere command | 50 | 52 | $6.30 | 导航 | |
| cohere rerank pricing | 50 | 24 | — | 导航 | ⭐ 价格痛点词 |
| cohere embed | 40 | 46 | — | 导航+交易 | |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| **bge-m3** | 4,400 | **32** | $9.32 | 信息 | ⭐⭐ 我方平替模型本体，量大 KD 中！|
| sentence transformers | 1,900 | 64 | $8.37 | 信息+导航 | 开源嵌入生态大词 |
| bge m3（空格变体）| 590 | 47 | $9.32 | 信息 | |
| bge large | 260 | **23** | $0.75 | 商业 | ⭐ BGE 家族型号词 |
| bge-reranker | 210 | 39 | — | 信息 | 我方平替重排本体 |
| open source embedding models | 170 | **18** | $2.87 | 信息 | ⭐ 直接机会词 |
| nomic embed | 140 | **30** | — | 信息 | ⭐ 另一开源嵌入 |
| bge reranker（空格）| 140 | 36 | — | 信息 | |
| ollama embedding | 110 | 44 | — | 信息 | 本地嵌入路径词 |
| open source rag | 70 | 36 | $4.03 | 信息 | |
| bge embedding | 50 | 53 | — | 信息 | |
| local embedding model | 50 | **27** | — | 信息 | ⭐ 高契合 |
| best open source embedding model | 40 | **13** | — | 商业 | ⭐⭐ KD13 完美契合 |
| open source embedding model | 30 | 0 | $1.82 | — | ⭐ |
| open source embedding | 20 | 0 | — | — | ⭐ GEO |
| open source reranker | 20 | 0 | — | — | ⭐ GEO |
| self hosted embedding model | 20 | 0 | — | — | ⭐ GEO |
| self hosted rag | 20 | 0 | — | — | ⭐ GEO |
| bge-m3 embedding | 20 | 0 | — | — | ⭐ GEO |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Cohere 的 Embed / Rerank 是纯闭源按量计费 API，数据必须出机、企业 RAG 每次检索都要付费；Olares 上用 BGE-M3 + bge-reranker（MIT/Apache 开源，经 Ollama / text-embeddings-inference / Xinference 本地跑）搭同等 RAG 嵌入+重排链路——嵌入/重排零 API 费、无调用上限、数据不出机、还能私有部署。这正好命中 Cohere 主打的"企业私有 RAG"却把成本与主权还给用户。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| **bge-m3** | 4,400 | 32 | $9.32 | ⭐⭐⭐ 平替本体：一篇"在 Olares 上自托管 BGE-M3 嵌入服务（OpenAI 兼容 API）"教程，吃下最大开源信号词 |
| cohere rerank | 480 | 39 | $10.89 | ⭐⭐⭐ 本地重排：bge-reranker on Olares 替代 Cohere Rerank API，CPC $10.9 高商业价值 |
| bge large | 260 | 23 | $0.75 | ⭐⭐ BGE 型号词，导向 Olares 自托管嵌入 |
| cohere pricing | 260 | 26 | $7.83 | ⭐⭐⭐ 成本对比：Cohere Embed/Rerank 按量计费 vs BGE-M3 on Olares 零边际成本 |
| enterprise llm | 260 | 20 | $8.14 | ⭐⭐ 企业 LLM 私有化：Olares 本地 LLM + 本地 RAG，数据主权叙事 |
| cohere api key | 210 | 18 | $5.88 | ⭐⭐ 集成决策期用户，导向"不用 Cohere Key：本地嵌入/重排" |
| cohere reranker | 210 | 32 | $8.47 | ⭐⭐⭐ 同 cohere rerank，bge-reranker 本地替代 |
| best embedding model for rag | 140 | 29 | $2.40 | ⭐⭐⭐ listicle：best open-source self-hosted embedding for RAG（BGE-M3 领衔）|
| nomic embed | 140 | 30 | — | ⭐⭐ 开源嵌入对比，纳入 Olares 自托管清单 |
| bge-reranker | 210 | 39 | — | ⭐⭐⭐ 平替本体：Olares 自托管重排教程 |
| open source embedding models | 170 | 18 | $2.87 | ⭐⭐⭐ 直接机会：开源嵌入模型清单 + Olares 部署 |
| best embedding model | 210 | 27 | — | ⭐⭐ listicle，开源自托管方向切入 |
| embedding models | 1,000 | 25 | $2.58 | ⭐⭐ 品类主词，导向"自托管开源嵌入模型"内容 |
| local embedding model | 50 | 27 | — | ⭐⭐⭐ 语义完美契合，Olares 一键本地嵌入 |
| ollama embedding | 110 | 44 | — | ⭐⭐ Olares 内置 Ollama 跑嵌入模型教程 |
| best open source embedding model | 40 | 13 | — | ⭐⭐⭐ KD13 金矿，BGE-M3 主推 |
| open source rag | 70 | 36 | $4.03 | ⭐⭐ 自托管 RAG 全栈（嵌入+重排+LLM）on Olares |
| self hosted rag / self hosted embedding model / open source reranker | ≤20 | 0 | — | ⭐ GEO：近零量语义精准，抢 AI Overview 引用位 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| bge-m3 | 4,400 | 32 | $9.32 | 信息 | **主词候选** | 平替本体、最大开源信号词：一篇"Olares 自托管 BGE-M3 嵌入服务"能吃满全族流量 |
| embedding models | 1,000 | 25 | $2.58 | 信息 | **主词候选** | 品类主词 KD25 可排，导向开源自托管嵌入清单 |
| cohere rerank | 480 | 39 | $10.89 | 导航 | **主词候选** | 核心差异化功能词，bge-reranker on Olares 本地替代，CPC $10.9 |
| best embedding model | 210 | 27 | — | 商业 | 主词候选 | listicle 主词，best open-source self-hosted embedding（BGE-M3 领衔）|
| best embedding model for rag | 140 | 29 | $2.40 | 商业 | 主词候选 | 与上簇合并；RAG 场景纯商业意图，Olares 契合度最高 |
| enterprise llm | 260 | 20 | $8.14 | 信息 | 主词候选 | KD20+高 CPC，企业私有化 LLM+RAG 叙事，量小但强商业 |
| cohere pricing | 260 | 26 | $7.83 | 导航 | 主词候选 | 成本对比页：Cohere 按量计费 vs BGE-M3 on Olares 零边际成本 |
| bge-reranker | 210 | 39 | — | 信息 | 次级 | 平替重排本体，并入 rerank 主题文 |
| bge large | 260 | 23 | $0.75 | 商业 | 次级 | BGE 家族型号词，KD23 易收 |
| open source embedding models | 170 | 18 | $2.87 | 信息 | 次级 | KD18，并入"开源自托管嵌入"清单 |
| cohere api key | 210 | 18 | $5.88 | 导航 | 次级 | KD18 集成词，导向"不用 Cohere Key：本地嵌入/重排" |
| cohere reranker | 210 | 32 | $8.47 | 导航 | 次级 | cohere rerank 变体，并入同文 |
| nomic embed | 140 | 30 | — | 信息 | 次级 | 开源嵌入对比项 |
| local embedding model | 50 | 27 | — | 信息 | 次级 | 语义完美契合，量小但纯净 |
| best open source embedding model | 40 | 13 | — | 商业 | 次级 | KD13 金矿，listicle 收 |
| voyage ai | 1,900 | 55 | $6.53 | 导航 | 次级 | 竞品品牌词，做"Voyage/Cohere/开源嵌入对比"时借力 |
| cohere alternatives / cohere vs openai / cohere vs anthropic | 20 | 0 | — | — | GEO | 近零量 KD0 对比/替代词，先发抢直答位 |
| self hosted rag / open source reranker / self hosted embedding model | ≤20 | 0 | — | — | GEO | 语义精准近零量，GEO 前瞻占位 |

---

## 核心洞见

1. **品牌护城河：正面刚不划算，但护城河比看上去脆。** Cohere 自然流量 24.4K/月里 90%+ 是品牌词（cohère 12,100 / cohere ai 2,900 / cohere 33,100 及一堆误拼变体全排第 1），品类通用词几乎排不上第一页（rag KD95、semantic search KD71 都在两页外）。品牌词心智抢不了也不必抢；但它的品牌被同名 **Cohere Health（医疗保险）严重污染**（cohere health 14,800 / cohere provider portal 12,100 / cohere provider login 2,400），说明"cohere"这个词本身在 SEO 上并不干净——它没有 Lovable 那种独占级品牌护城河。

2. **可复制的打法：博客借力词 + 功能落地页，付费打法无价值。** 唯一值得学的是**用博客文章挂借力大词吃残量**（embedding 5.4 万、fine tune 2.9 万、what is a neural network 9 万都靠一篇博客卡在第二三页），以及 /rerank、/embed、/pricing 这类**清晰功能落地页**吃精准词。它的 Google Ads（52 词、$2.5K）买的是 discovaz、free ai tools 这类杂词导向 /north，错配严重，**没有可复制价值**——Olares 无需跟投付费。

3. **对 Olares 最关键的 3 个词：`bge-m3`（4,400, KD32）、`cohere rerank`（480, KD39, CPC $10.9）、`embedding models`（1,000, KD25）。** 第一个是我们平替模型本体、且是全表最大开源信号词——一篇"在 Olares 上自托管 BGE-M3 嵌入服务（OpenAI 兼容）"就能吃满整族流量；第二个是 Cohere 最值钱的差异化功能词，用 bge-reranker 本地替代直击；第三个是可排的品类主词。三者共同支撑"**开源自托管嵌入+重排 = 本地 RAG，零 API 费、数据不出机**"的核心叙事。

4. **最大攻击面：按量计费 + 数据出机 + 闭源。** Cohere 的 Embed / Rerank 是纯 API 按 token/按次计费、且**没有开源权重**（Command 权重虽放出但 CC-BY-NC 非商用）。企业 RAG 每次检索都要付费、数据都要送到 Cohere。攻击点很清晰：`cohere pricing`（KD26）、`cohere rerank pricing`（KD24）、`enterprise llm`（KD20, CPC $8.14）——做"Cohere Embed/Rerank 成本 vs BGE-M3 on Olares 零边际成本 + 私有部署"对比页，把它主打的"企业私有 RAG"卖点反用成 Olares 的卖点。

5. **隐藏低 KD 金矿：开源嵌入/重排词族几乎无人竞争。** `best open source embedding model`（KD13）、`open source embedding models`（KD18）、`bge large`（KD23）、`local embedding model`（KD27）、`embedding models`（KD25）——量 40–1,000、KD 全在 30 以下，且商业/信息意图纯净。相比之下品类顶词 rag/semantic search 都是 KD70–95 打不动。Olares 应集中火力做**开源自托管嵌入&重排 listicle + 型号教程**，这是低成本可排的主战场。

6. **GEO 前瞻词：`cohere alternative` / `cohere alternatives`（KD0）、`self hosted rag`、`open source reranker`、`self hosted embedding model`（均近零量 KD0）。** 语义与 Olares 完美契合，目前几乎无内容。建议提前发布权威对比/直答内容占位，抢 AI Overview / Perplexity 的生成式引用位——这些词一旦被 AI 搜索引用，转化的都是最纯的自托管意图用户。

7. **与既有分析的关联：补齐"开源嵌入/重排"子品类。** 本报告的核心机会（BGE-M3 / bge-reranker / open source embedding / local RAG）在 `olares-500-keywords` 与"本地 LLM"分类里覆盖不足——现有词表偏"跑模型/推理"，缺 **RAG 检索侧（嵌入+重排）**的开源自托管词族。建议将 `bge-m3`、`embedding models`、`best open source embedding model`、`cohere rerank` 作为独立"开源嵌入/重排"子簇补入总表；它与 model 方向的 Embedding 章、tech 方向的向量库词族天然互补，可跨报告聚簇成"自托管 RAG 全栈（嵌入→重排→本地 LLM）"内容矩阵。

---

*数据来源：SEMrush us 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_questions）| 2026-07-07*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
