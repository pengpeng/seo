# FastGPT SEO 竞品分析报告

> 域名：fastgpt.io（tryfastgpt.ai 为别名，流量归一） | SEMrush US | 2026-07-06
> 开源 RAG 平台 + AI Agent Builder，中国团队出品、GitHub 2.8 万星，中文市场为主；英文 SEO 几乎空白，是英语圈的先机窗口。

---

## 项目理解（前置）

FastGPT 是由 [Labring](https://github.com/labring) 团队（同时维护 Sealos 云原生 OS）于 2023 年 2 月开源的知识库 + AI Agent 构建平台。核心能力是"导入文档 → 自动切片/向量化/混合检索 → 可视化 Flow 编排 → 一键发布为问答机器人或 API"，整套流程开箱即用。它面向企业和开发者，支持 Docker Compose 自托管，也有 Sealos 云托管版。与 Dify、Flowise 同属"可视化 LLM 应用构建"赛道，但更专注知识库 RAG，Flow 编排深度次于 Dify；社区以中文用户为主。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 企业级开源 RAG 平台 + AI Agent Builder：文档进去、智能问答出来 |
| 开源 / 许可证 | 是——FastGPT Open Source License（允许商用后台服务，**禁止 SaaS 转售**；商业版需付费授权） |
| 主仓库 | [labring/FastGPT](https://github.com/labring/FastGPT)（★ ~28,800，2023-02-23 创建） |
| 核心功能 | 文档自动处理（PDF/Word/Excel/Markdown/URL）、混合检索+重排、可视化工作流（Flow）、多模型支持（OpenAI/DeepSeek/Qwen/Ollama 等）、MCP 工具集成（v4.14+）、OpenAI 兼容 API |
| 商业模式 / 定价 | 开源自托管免费；SaaS 从 $0.37/月起；商业版定价见 doc.fastgpt.io/guide/version/commercial |
| 差异化 / 价值主张 | 相比 Dify 更聚焦 RAG 与知识库精度；比 RAGFlow 有更丰富的 Flow 可视化；比 Flowise 有更完整的中文文档与 QA 拆分能力；MCP + Xinference/Ollama 原生集成 |
| 主要竞品（初判）| Dify、RAGFlow、Flowise、AnythingLLM |
| Olares Market | ⬜ 未上架（apps.md 2026-07-06 时点） |
| 来源 | [fastgpt.io](https://fastgpt.io)、[doc.fastgpt.io](https://doc.fastgpt.io/en/self-host/deploy/docker)、[GitHub labring/FastGPT](https://github.com/labring/FastGPT) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | fastgpt.io（tryfastgpt.ai 为同站别名，Semrush 无独立数据） |
| SEMrush Rank | 1,381,329 |
| 自然关键词数 | 149 |
| 月自然流量（US）| 665 |
| 自然流量估值 | $2,537/月 |
| 付费关键词数 | 0（无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 7 词 |
| 排名 4-10 位 | 10 词 |
| 排名 11-20 位 | 7 词 |

> **关键背景**：665 的月均 US 流量在同类开源工具里极低（Dify 26,694、Flowise 约 5,000+）。95% 以上的关键词是品牌词或中文词，英文 SEO 尚未起步。这既是短板，也是**进入窗口**：英语圈的 RAG 关键词竞争正在形成，但 FastGPT 自身还未布局。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| fastgpt.io | 90 | 493 | 74% |
| doc.fastgpt.io | 52 | 136 | 20% |
| cloud.fastgpt.io | 7 | 36 | 5% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| fastgpt | 1 | 1,300 | 43 | $5.23 | 322 | 导航 | fastgpt.io/en |
| fastgptplus | 1 | 590 | 47 | $2.38 | 146 | 导航 | fastgpt.io/en |
| fastgpt | 3 | 1,300 | 43 | $5.23 | 39 | 导航 | doc.fastgpt.io |
| 飞书机器人开发 | 8 | 1,300 | 29 | — | 31 | 信息 | doc.fastgpt.io/zh-CN/…/feishu |
| fastgpt | 5 | 1,300 | 43 | $5.23 | 31 | 导航 | cloud.fastgpt.io |
| rag知识库 | 6 | 880 | 18 | $3.53 | 26 | 信息 | doc.fastgpt.io/zh-CN/guide/dataset/rag |
| fastgpt api | 1 | 90 | 18 | — | 22 | 信息 | doc.fastgpt.io/en/openapi/intro |
| fast gpt | 1 | 50 | 45 | — | 12 | 导航 | fastgpt.io/en |
| rag 知识库 | 7 | 390 | 17 | $3.56 | 9 | 信息 | doc.fastgpt.io/zh-CN/guide/dataset/rag |
| fastgpt api | 3 | 90 | 18 | — | 7 | 信息 | fastgpt.io/en |
| mcp工具 | 9 | 210 | 30 | $2.29 | 4 | 信息 | doc.fastgpt.io/zh-CN/…/mcp_tools |
| xinference | 20 | 720 | 21 | $3.55 | 1 | 信息 | doc.fastgpt.io/en/self-host/custom-models/xinference |
| ollama port | 35 | 1,000 | 41 | $4.42 | 0 | 信息 | doc.fastgpt.io/en/self-host/custom-models/ollama |
| searxng search engine | 51 | 260 | 52 | $4.57 | 0 | 信息 | doc.fastgpt.io/en/…/searxng_plugin_guide |
| pdf marker | 24 | 210 | 39 | $1.17 | 0 | 信息 | doc.fastgpt.io/en/self-host/custom-models/marker |
| can ai spot the differences in two letters | 24 | 1,600 | 27 | — | 2 | 信息 | fastgpt.io/en/faq/… |

> 洞察：FAQ 页"AI 能识别两个字母的差异"等内容词排在 top 位但量小，说明 fastgpt.io 在英文长尾 FAQ 上有零散积累，但缺乏系统性的英文内容策略。核心流量几乎全来自品牌词，且大量流量实际来自中国用户搜索中文关键词。

### 付费词（Google Ads）

FastGPT 当前无 Google Ads 投放（paid_keywords = 0），无付费词数据。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| langchain alternative | 140 | 29 | $4.49 | 信息/商业 | ⭐ RAG/LLM 框架替代词，与 FastGPT 定位重叠 |
| flowise alternative | 20 | 0 | $0.68 | 商业 | ⭐ 同赛道，KD=0 空白机会 |
| ragflow alternative | 20 | 0 | $3.64 | 商业 | ⭐ 同赛道，KD=0 |
| dify alternative | 10 | 0 | $5.90 | 商业 | ⭐ Dify 高 CPC 替代词，量小但意图强 |
| fastgpt alternative | 0 | 0 | — | — | 近零量，GEO 前哨；随品牌英文传播将爆发 |
| dify vs fastgpt | 20 | 0 | — | 信息 | ⭐ 对比词，KD=0 先占 |
| fastgpt vs ragflow | 20 | 0 | — | 信息 | ⭐ 对比词，KD=0 先占 |
| open source ai agent builder | 20 | 0 | $6.06 | 商业 | ⭐ 高 CPC，KD=0 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| retrieval augmented generation | 8,100 | 95 | $3.67 | 信息 | 过热，KD=95 不打 |
| ai knowledge base | 1,900 | 48 | $17.65 | 信息/商业 | CPC 极高，竞争激烈 |
| rag pipeline | 1,900 | 57 | $3.75 | 信息 | 技术向，KD 较高 |
| rag chatbot | 720 | 47 | $2.65 | 信息/商业 | 核心品类词 |
| ai workflow builder | 590 | 50 | $8.14 | 商业 | CPC 高，偏工具向 |
| rag framework | 390 | 69 | $3.58 | 信息 | 开发者词，KD 高 |
| knowledge base chatbot | 210 | 28 | $7.87 | 商业 | ⭐ KD=28，高 CPC 机会词 |
| rag knowledge base | 140 | 36 | $6.20 | 信息 | 核心品类，可争 |
| open source knowledge base | 140 | 16 | $3.39 | 信息 | ⭐ KD=16 低竞争 |
| llm knowledge base | 90 | 10 | $3.82 | 信息 | ⭐⭐ KD=10，极低竞争金矿 |
| open source rag | 70 | 36 | $4.03 | 信息 | 开源信号词 |
| rag platform | 70 | 61 | $5.95 | 信息/商业 | KD 偏高 |
| self hosted knowledge base | 40 | 36 | $7.54 | 信息 | 自托管需求明确 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| fastgpt | 1,300 | 43 | $5.23 | 导航/品牌 | 主品牌词，自己第一位 |
| fastgptplus | 590 | 47 | $2.38 | 导航/品牌 | 商业版/Pro 版词 |
| fastgpt api | 90 | 40 | — | 信息 | 开发者集成词 |
| fastgpt github | 90 | 38 | — | 导航 | GitHub 导航词 |
| fastgpt docker | 20 | 0 | — | 信息 | ⭐ 部署词，KD=0 |
| fastgpt deepseek | 20 | 0 | — | 信息 | ⭐ 模型集成词 |
| fast gpt | 50 | 45 | — | 导航 | 拼写变体 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted ai chatbot | 30 | 4 | $3.00 | 信息 | ⭐⭐ 极低 KD，与 Olares 强相关 |
| open source chatbot builder | 30 | 0 | — | 信息 | ⭐ KD=0 |
| self hosted chatbot | 20 | 0 | $2.01 | 信息 | ⭐ KD=0 |
| self hosted rag | 20 | 0 | — | 信息 | ⭐ KD=0，精准 Olares 场景词 |
| self hosted rag chatbot | ~10 | — | — | 信息 | GEO 前哨 |
| private knowledge base ai | ~10 | — | — | 信息 | GEO 前哨 |
| private ai knowledge base | ~10 | — | — | 信息 | GEO 前哨 |
| open source llm platform | 20 | 0 | — | 信息 | ⭐ KD=0 |
| document ai chatbot | 20 | 0 | — | 信息 | ⭐ KD=0 |
| ai document search | 50 | 17 | $4.51 | 信息 | ⭐ KD=17 低竞争 |
| llm knowledge base | 90 | 10 | $3.82 | 信息 | ⭐⭐ 最优先 Olares 词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Olares 是唯一能让用户一键私有部署整个 RAG 矩阵（FastGPT + Dify + RAGFlow + Flowise）的个人云 OS，数据和推理全不出设备，最符合"Own your AI"品牌叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角色 | 契合度 |
|--------|------|----|----|------------|--------|
| llm knowledge base | 90 | 10 | $3.82 | Olares 一键部署 FastGPT/RAGFlow，本地 LLM + 知识库全私有 | ⭐⭐⭐ |
| self hosted rag | 20 | 0 | — | Olares = 自托管 RAG 的最简路径，FastGPT 是其中一个应用 | ⭐⭐⭐ |
| knowledge base chatbot | 210 | 28 | $7.87 | Olares Market 上 FastGPT/RAGFlow 对比推荐文 | ⭐⭐⭐ |
| self hosted ai chatbot | 30 | 4 | $3.00 | Olares 场景词，可做"deploy your own AI chatbot on Olares" | ⭐⭐⭐ |
| fastgpt alternative | 0 | 0 | — | 先占 GEO：Olares 支持一键部署 Dify/RAGFlow 等 FastGPT 替代品 | ⭐⭐⭐ |
| dify vs fastgpt | 20 | 0 | — | Olares 独特角度：不需要选，Market 里两个都能装，本机运行 | ⭐⭐⭐ |
| fastgpt vs ragflow | 20 | 0 | — | 同上，Olares 全家桶 RAG 矩阵叙事 | ⭐⭐⭐ |
| open source knowledge base | 140 | 16 | $3.39 | Olares Market 上多款开源知识库可选 | ⭐⭐ |
| self hosted chatbot | 20 | 0 | $2.01 | Olares 部署 FastGPT 教程词 | ⭐⭐ |
| open source rag | 70 | 36 | $4.03 | Olares 上的开源 RAG 方案概览 | ⭐⭐ |
| ai knowledge base | 1,900 | 48 | $17.65 | 高竞争但高 CPC，Olares 私有 AI 知识库叙事，长远布局 | ⭐⭐ |
| langchain alternative | 140 | 29 | $4.49 | FastGPT/RAGFlow 均为 LangChain 替代方案，Olares 一键部署 | ⭐⭐ |
| open source ai agent builder | 20 | 0 | $6.06 | Olares Market：FastGPT 即开源 AI Agent Builder | ⭐⭐ |
| private ai knowledge base | ~10 | — | — | GEO 前哨：Olares + FastGPT = 私有 AI 知识库完整方案 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| knowledge base chatbot | 210 | 28 | $7.87 | 商业/信息 | **主词候选** | KD=28 在高 CPC 品类词里是难得机会；Olares 可做"deploy your own knowledge base chatbot" 对比内容 |
| llm knowledge base | 90 | 10 | $3.82 | 信息 | **主词候选** | ⭐⭐ KD=10 全场最低竞争高价值词，Olares+FastGPT 精准场景词，必攻 |
| open source knowledge base | 140 | 16 | $3.39 | 信息 | **主词候选** | KD=16 低竞争，Olares Market 多选一落地页切入点 |
| langchain alternative | 140 | 29 | $4.49 | 信息/商业 | **主词候选** | FastGPT/RAGFlow 均为 LangChain 上层应用替代；Olares 部署更简单 |
| self hosted ai chatbot | 30 | 4 | $3.00 | 信息 | **主词候选** | KD=4 极低，量虽小但意图精准；Olares 场景文章核心词 |
| ai knowledge base | 1,900 | 48 | $17.65 | 信息/商业 | 次级 | 量大但 KD 偏高；作为主词文章的次级词布局，带入"private/self-hosted"修饰 |
| rag knowledge base | 140 | 36 | $6.20 | 信息 | 次级 | 技术向品类词，并入 llm knowledge base 或 knowledge base chatbot 文章 |
| dify vs fastgpt | 20 | 0 | — | 信息 | 次级 | KD=0，对比意图；Olares 两者都能装是最强差异化角度 |
| fastgpt vs ragflow | 20 | 0 | — | 信息 | 次级 | 同上，补全 RAG 矩阵对比文的结构词 |
| open source rag | 70 | 36 | — | 信息 | 次级 | 并入"self-hosted RAG"类文章 |
| self hosted rag | 20 | 0 | — | 信息 | 次级 | KD=0，可作为"self-hosted ai chatbot"文章的集群词 |
| self hosted chatbot | 20 | 0 | $2.01 | 信息 | 次级 | 同上归集群 |
| flowise alternative | 20 | 0 | $0.68 | 商业 | 次级 | 已有 flowise.md 报告，可交叉联动 |
| ragflow alternative | 20 | 0 | $3.64 | 商业 | 次级 | 已有 ragflow.md，交叉联动 |
| fastgpt alternative | 0 | 0 | — | 商业 | **GEO** | 近零量但搜索意图极清晰；随品牌英文扩散将爆发，现在占位赢 AI Overview |
| private ai knowledge base | ~10 | — | — | 信息 | **GEO** | 语义精准，进 FAQ/前瞻段抢 Perplexity 引用位 |
| self hosted rag chatbot | ~10 | — | — | 信息 | **GEO** | 同上，Olares 叙事完美承接 |
| private knowledge base ai | ~10 | — | — | 信息 | **GEO** | 同上 |
| open source ai agent builder | 20 | 0 | $6.06 | 商业 | **GEO** | 高 CPC 高意图，近零量但值得在 Agent Builder 相关内容中植入 |

---

## 核心洞见

1. **品牌护城河**：fastgpt.io 的品牌词（`fastgpt` 1300 vol / KD 43，`fastgptplus` 590 vol / KD 47）在 US 完全被自己锁定，无竞争威胁。但护城河止步于品牌词——品类词上 FastGPT 几乎没有任何 US 自然流量，英文 SEO 基础等于零。**结论：不需要正面刚品牌词；价值在攻击它尚未布局的品类词与对比词**。

2. **可复制的打法**：FastGPT 当前的英文内容只有分散的 FAQ 页面（`can ai spot the differences in two letters`、`how many tokens in 1000 words` 等相关性低的词），没有系统性的品类词页面或替代词落地页。**对 Olares 的参考意义**：这些词位置空缺，用"Olares 部署 FastGPT vs Dify vs RAGFlow"系列对比/替代文，可以在低竞争的位置填入。

3. **对 Olares 最关键的词**：
   - **`llm knowledge base`**（KD=10，月量 90，CPC $3.82）——所有 RAG 相关词里竞争最低、意图最精准的主词，Olares + FastGPT/RAGFlow 完美承接。
   - **`knowledge base chatbot`**（KD=28，月量 210，CPC $7.87）——高 CPC 意味着商业意图强，KD 适中可攻。
   - **`self hosted ai chatbot`**（KD=4，月量 30）——量小但 KD 极低，Olares 一键部署的核心场景词，先发布先占坑。

4. **最大攻击面**：FastGPT 的 Open Source License 明确**禁止 SaaS 转售**，意味着任何想私有部署 FastGPT 的用户不能用现成的托管服务——他们必须自己搞服务器/Docker。**Olares 的切入点**：把复杂的 Docker 部署步骤变成"一键安装"，直接命中这批自托管刚需用户。痛点词：`fastgpt docker`（KD=0）、`self hosted rag`（KD=0）、`deploy fastgpt`（GEO）。

5. **隐藏低 KD 金矿**：
   - `llm knowledge base`：KD=10，月量 90，$3.82 CPC ← **全场最优**
   - `self hosted ai chatbot`：KD=4，月量 30
   - `open source knowledge base`：KD=16，月量 140
   - `ai document search`：KD=17，月量 50
   - `self hosted chatbot` / `self hosted rag` / 系列变体：KD=0，各 20-30 量——聚成一篇可覆盖 100+ 月均量

6. **GEO 前瞻布局**：`fastgpt alternative`（US 量≈0）目前是空白，但 FastGPT 在中文社区的高知名度意味着这个词随品牌国际化会在 1-2 年内爆发。现在写进 FAQ 段和文章 schema 可提前锁定 AI Overview 引用位。其他 GEO 词：`private ai knowledge base`、`self hosted rag chatbot`、`open source ai agent builder`（高 CPC $6.06，值得抢占）。

7. **与既有分析的关联**：
   - `olares-500-keywords` 中无 FastGPT 和 `llm knowledge base` 相关词 → 纯增量。
   - RAG 矩阵现有 3 份报告（dify.md / flowise.md / ragflow.md），本报告补齐第 4 个。这 4 个品牌放一起构成 Olares 的"私有 RAG 全家桶"叙事：**在 Olares 上同时跑四款开源 RAG 工具，没有任何一家云服务商能做到这一点**——这是跨报告内容机会，推荐在 seo-content 阶段聚成"best self-hosted RAG platform 2025"系列文。
   - 中文关键词（`rag知识库` KD=18、`飞书机器人开发` KD=29、`mcp工具` KD=30）在 Semrush US 数据库里有量，说明有中国用户用 Google 搜索英文站——若 Olares 有中文落地页，这部分中文词可顺带收割。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、domain_organic_organic、phrase_these × 3、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍（FastGPT 以中文市场为主，实际全球总量可能更高但 Semrush US 数据库覆盖不足）。*
