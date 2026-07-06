# Salesforce Agentforce SEO 竞品分析报告

> 域名：salesforce.com | SEMrush US | 2026-07-06
> Salesforce Agentforce = Salesforce 旗舰 AI Agent 平台，Salesforce CRM 原生集成，ARR $1.2B（FY27 Q1，+205% YoY），全球最大企业软件生态护体

---

## 项目理解（前置）

Salesforce Agentforce 是 Salesforce 于 2024 年 10 月正式 GA 的 AI Agent 构建与部署平台，深度集成于 Salesforce Customer 360（Sales Cloud、Service Cloud、Marketing Cloud）生态。区别于市面上模型 API 套壳产品，Agentforce 的核心竞争力在于三层架构：①**Atlas 推理引擎**（plan-act-observe-revise 多步循环）；②**Trust Layer**（PII 脱敏、零数据留存、完整审计日志）；③**Salesforce Data Cloud 原生数据层**。企业无需另建数据管道，Agentforce 直接读写 CRM 记录、工单、商机、联系人。截至 FY27 Q1（2026 年 5 月），Agentforce ARR 已达 $1.2B，关闭交易 29,000+。其最大的竞争护城河不是技术而是生态：已有 Salesforce CRM 用户可以零额外集成成本启动 Agentforce，但也因此被牢牢锁定在 Salesforce 体系内。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Salesforce CRM 原生 AI Agent 平台：Atlas 推理 + Data Cloud 数据层 + Trust Layer 安全，直接在 CRM 工作流中运行自主 Agent |
| 开源 / 许可证 | 完全闭源；无开源版本；SDK/API 向开发者开放但平台本身闭源 |
| 主仓库 | 无（闭源 SaaS）；developer.salesforce.com 提供 Agent API 文档 |
| 核心功能 | ①Agentforce Builder（低代码拖拽 Agent 构建）；②Atlas 推理引擎（多步 Plan-Act-Observe）；③预置 Agent（SDR Agent、Service Agent、Sales Agent、Coach Agent）；④Trailhead Agentforce 认证体系；⑤Agentexchange 第三方 Agent 市场；⑥Model Builder（BYO 自定义模型接入）；⑦Agentforce Vibes（vibe-coding 风格 Agent 开发，2026 年新增）；⑧MCP 协议支持 |
| 商业模式 / 定价 | 消耗制：$2/次对话（Per Conversation）或 Flex Credits（$500/10 万 credits，标准动作 $0.10/次，语音 $0.15/次）；另有按用户 Add-on（$125–$550/用户/月）；所有方案均需 Enterprise Edition 基础许可（Service Cloud ~$165/用户/月）；30 席企业 Year-1 TCO 估算 $200K–$450K+ |
| 差异化 / 价值主张 | CRM 原生零集成启动；Trust Layer 企业合规内置；Trailhead 认证生态形成专业人才护城河；Agentforce 3.0（2025 年 6 月）引入 Headless Agents + Agent API，允许脱离 Salesforce UI 运行 |
| 主要竞品（初判）| Microsoft Copilot Studio（Microsoft 生态对应品）、ServiceNow Now Assist（IT 服务场景）、Zendesk AI、Intercom Fin、Dify（开源）、Flowise（开源）、n8n（开源工作流） |
| Olares Market | 未上架（闭源）；开源平替：Dify ✅ 已上架、Flowise ✅ 已上架 |
| 来源 | [salesforce.com/agentforce](https://www.salesforce.com/agentforce/)、[myaskai.com 评测](https://myaskai.com/blog/salesforce-agentforce-complete-guide-2026)、[Salesforce FY27 Q1 业绩](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-First-Quarter-Fiscal-2027-Results/default.aspx)、[martech.org](https://martech.org/salesforce-agentforce-what-you-need-to-know/) |

---

## 流量基线（Phase 1）

> **说明**：salesforce.com 是超大型企业软件域名（Rank 660，月流量 415 万），Agentforce 是其一个子业务线，无独立域名。本报告的 Phase 1 先给出 salesforce.com 域名整体基线，再聚焦 Agentforce 相关页面的实测数据；Phase 2/3 关键词研究完全聚焦 Agentforce 相关词。

### 概览（salesforce.com 整域）

| 指标 | 数据 |
|------|------|
| 域名 | salesforce.com |
| SEMrush Rank | **660**（全球顶级企业软件站点） |
| 自然关键词数 | 761,584 |
| 月自然流量（US）| 4,158,936 |
| 自然流量估值 | **$31,916,056/月** |
| 付费关键词数 | 8,132 |
| 月付费流量 | 129,738 |
| 付费流量估值 | $1,208,715/月 |

> 月流量 $3200 万估值反映 salesforce.com 关键词的整体高 CPC 水位（CRM / 企业软件 / AI Agent 词 CPC 普遍 $10–$50+）。Agentforce 子线虽只占域名一小部分，但其词的商业价值密度极高。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.salesforce.com | 391,955 | 3,280,532 | 78.88% |
| login.salesforce.com | 2,050 | 228,403 | 5.49% |
| trailhead.salesforce.com | 130,287 | 185,674 | 4.46% |
| help.salesforce.com | 123,284 | 165,506 | 3.98% |
| developer.salesforce.com | 45,885 | 93,808 | 2.26% |
| appexchange.salesforce.com | 34,976 | 70,748 | 1.70% |
| mrbeast.salesforce.com | 631 | 28,997 | 0.70% |
| careers.salesforce.com | 3,223 | 18,920 | 0.45% |
| trailheadacademy.salesforce.com | 5,769 | 12,133 | 0.29% |
| **agentexchange.salesforce.com** | **421** | **3,038** | **0.07%** |

> **Agentforce 专属子域名 `agentexchange.salesforce.com`（类似 App Store 的 Agent 市场）目前仅有 421 关键词、3,038 流量，SEO 尚处于起步阶段——这是重大机会信号。**Trailhead 子域（130K+ 关键词）是 Salesforce Agentforce 认证词的主要流量来源，该生态已形成强护城河。

### Agentforce 主线 TOP 自然关键词（按流量排序）

以下数据来源：①过滤"agentforce"词的 resource_organic 结果；②`/agentforce/` 子路径实测数据。

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| agentforce news | 1 | 1,900 | 55 | $14.69 | 1,520 | 信息 | /agentforce/what-is-new/ |
| **salesforce agentforce pricing** | 1 | 1,300 | 38 | $17.22 | 1,040 | 商业 | /agentforce/pricing/ |
| ai assistant *(大词侧漏)* | 5 | 40,500 | 62 | $3.02 | 972 | 信息 | /agentforce/ai-assistant/ |
| salesforce agentforce partners | 1 | 1,000 | 43 | $21.02 | 800 | 商业 | agentexchange.salesforce.com/ |
| salesforce agentforce certification | 1 | 880 | 35 | $1.23 | 704 | 信息 | trailhead/agentforcespecialist |
| agentforce for sales | 1 | 880 | 37 | $0.00 | 704 | 信息 | /sales/ai-sales-agent/ |
| salesforce agentforce specialist cert. | 1 | 720 | 38 | $3.50 | 576 | 信息 | trailhead/agentforcespecialist |
| **agentforce pricing** | 1 | 590 | **25** | $16.22 | 472 | 商业 | /agentforce/pricing/ |
| agentforce logo | 1 | 590 | 39 | $0.00 | 472 | 信息 | /agentforce/ |
| multi-agent *(大词侧漏)* | 9 | 33,100 | 50 | $4.41 | 430 | 信息 | /agentforce/ai-agents/multi-agent-systems/ |
| autonomous ai agents *(大词)* | 1 | 2,400 | 60 | $7.29 | 316 | 信息 | /agentforce/ai-agents/autonomous-agents/ |
| agentforce service agent | 1 | 390 | **27** | $20.64 | 312 | 信息 | help.salesforce.com |
| agentforce ai | 1 | 390 | 54 | $12.45 | 312 | 信息 | /agentforce/ |
| agentforce headless agents | 1 | 390 | **27** | $0.00 | 312 | 信息 | developer.salesforce.com |
| agentforce trailhead | 1 | 390 | 45 | $4.98 | 312 | 商业 | trailhead |
| agentic ai *(大词侧漏)* | 6 | 90,500 | 93 | $6.00 | 271 | 信息 | /agentforce/what-is-agentic-ai/ |
| ai customer service bot | 1 | 1,000 | 69 | $52.43 | 248 | 信息 | /agentforce/chatbot/ |
| agentic ai definition *(大词)* | 6 | 18,100 | 83 | $1.16 | 235 | 信息 | /agentforce/what-is-agentic-ai/ |
| **agentforce** | 1 | 9,900 | **45** | $13.92 | 257 | 信息 | /agentforce/ |
| salesforce agentforce | 1 | 8,100 | 63 | $12.40 | 210 | 商业 | /agentforce/ |
| salesforce agentforce vibes | 1 | 260 | 33 | $16.33 | 208 | 信息 | /agentforce/developers/vibe-coding/ |
| **agentforce use cases** | 1 | 260 | **17** | $18.54 | 208 | 商业 | /agentforce/use-cases/ |
| agentforce chatbot | 1 | 260 | **23** | $20.58 | 208 | 信息 | /agentforce/ |
| **what is agentforce** | 1 | 1,300 | **31** | $7.98 | 171 | 信息 | /agentforce/ |
| agentforce sales | 1 | 320 | 40 | $15.67 | 256 | 商业 | /sales/ai-sales-agent/ |
| **agentforce builder** | 1 | 320 | **22** | $18.55 | - | 商业 | /agentforce/ |
| salesforce digital wallet | 1 | 210 | 34 | $19.18 | 168 | 信息 | /agentforce/digital-wallet/ |
| agentforce observability | 1 | 140 | **18** | $26.44 | 112 | 商业 | /agentforce/observability/ |
| agentforce contact center | 1 | 140 | 36 | $26.54 | 112 | 信息 | /news/stories/agentforce-contact-center/ |
| salesforce ai specialist certification | 1 | 320 | 39 | $2.40 | 256 | 商业 | trailhead |
| salesforce ai agent | 1 | 320 | 51 | $11.81 | 256 | 商业 | /agentforce/ |
| **salesforce ai consultant** | 1 | 1,000 | **33** | **$35.19** | 26 | 信息 | trailhead（认证/career 词） |
| ai agent platform *(大词)* | 3 | 2,400 | 50 | $13.06 | 156 | 信息 | /agentforce/ai-agents/platform/ |
| how much does agentforce cost | 1 | 40 | **26** | $18.75 | - | 信息/商业 | - |

> **重要洞察**：salesforce.com/agentforce/ 子路径已经在抢占大体量信息词——`agentic ai`（90,500/月，KD 93，排名 #6）、`ai chatbot`（90,500/月，KD 88，排名 #7）、`multi-agent`（33,100/月，KD 50，排名 #9）、`ai assistant`（40,500/月，KD 62，排名 #5）。这是一套"品类定义权"内容战略，不是在卖产品，而是在告诉搜索引擎"Salesforce = AI Agent 品类权威"。

### 付费词（Google Ads，按流量排序）

Salesforce Agentforce 的 Google Ads 策略：**占领 AI Agent 品类超大词 + 自我品牌保护 + 内容资源引流**，落地页以 Demo 和 ROI 资源为主（而非直接产品页）。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| ai agents | 1 | 27,100 | $10.30 | /agentforce/resources/grown-ups-guide-to-agents/ |
| ai agent | 1 | 22,200 | $9.28 | /agentforce/resources/grown-ups-guide-to-agents/ |
| agentforce | 1 | 14,800 | $10.44 | /agentforce/demos/overview/ |
| general sales agent | 1 | 14,800 | $2.90 | /sales/demos/agentforce-sales-demos/ |
| agentforce | 1 | 9,900 | $13.92 | /agentforce/resources/maximizing-roi-with-agentforce/ |
| salesforce agentforce | 1 | 8,100 | $12.40 | /agentforce/resources/maximizing-roi-with-agentforce/ |
| what are ai agents | 1 | 5,400 | $3.84 | /agentforce/resources/grown-ups-guide-to-agents/ |
| agentexchange | 1 | 4,400 | **$30.91** | appexchange 落地页（Agent 市场） |
| agent mode | 1 | 4,400 | $1.28 | /agentforce/demos/overview/ |
| agent ai | 1 | 4,400 | $9.28 | /agentforce/demos/overview/ |
| copilot agents | 1 | 3,600 | $4.55 | /service/demos/ai-for-customer-service/ |
| agentforce salesforce | 1 | 3,600 | $9.83 | /agentforce/demos/overview/ |
| agentic rag | 1 | 3,600 | $4.55 | /agentforce/resources/prompt-builder-guide/ |
| agent force | 1 | 2,900 | $11.97 | /sales/demos/agentforce-sales-demos/ |
| how to build an ai agent | 1 | 2,400 | $6.83 | /agentforce/resources/ |
| agentforce news | 1 | 1,900 | $15.70 | /agentforce/demos/overview/ |
| what is agentforce | 1 | 1,900 | $6.31 | /agentforce/demos/overview/ |
| salesforce agentforce pricing | 1 | 1,300 | $17.22 | 多个 Demo 落地页 |
| **agentforce builder** | 1 | 320 | **$18.55** | /agentforce/demos/overview/ |
| **agentforce sales** | 1 | 320 | **$15.67** | /form/sales/agentforce-for-sales-demos/ |

> 付费预算重点：Salesforce 用 `ai agents`（27,100）和 `ai agent`（22,200）等品类大词"收割"所有 AI Agent 认知流量，落地页是教育性内容（"大人指南"），而非产品推销——先建认知，Demo 时再转化。`agentexchange`（CPC $30.91）是最高单价词，反映 Agent 市场流量的高商业价值。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| n8n alternative | 720 | 18 | $7.45 | 商业 | ⭐ 开源工作流最大替代词；Flowise/Dify 潜在受益 |
| flowise alternatives | 50 | 14 | $0.67 | 商业 | ⭐ 直接 Olares 平替词 |
| dify alternatives | 20 | – | $7.11 | 商业 | ⭐ |
| agentforce alternatives | 20 | 0 | $26.14 | 商业 | ⭐ 极低竞争，正在成型中 |
| agentforce vs microsoft copilot | 20 | 0 | $0 | 对比 | ⭐ GEO 词 |
| agentforce competitors | 20 | 0 | $14.84 | 商业 | ⭐ GEO 词 |
| agentforce vs servicenow | 10 | 0 | $0 | 对比 | ⭐ GEO 词 |
| agentforce alternative | 10 | 0 | $0 | 商业 | ⭐ 量极小但此刻抢占成本趋近于零 |
| dify alternative | 10 | – | $5.90 | 商业 | ⭐ |

> **关键发现**：`agentforce alternative/alternatives` 总量只有 30，远低于 `sierra ai alternative`（est. 500）——说明 Agentforce 尚未在搜索用户心中形成"想找替代品"的心智。这是双刃剑：**竞争几乎为零，先发占位成本极低**，但需要等待市场教育。

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| agentic ai | 90,500 | 90+ | $7.80 | 信息 | 顶级品类词，salesforce 排 #6；Olares 内容可切教育性长尾 |
| ai agent platform | 2,400 | 54 | $10.39 | 信息 | Salesforce 排 #3（/agentforce/ai-agents/platform/） |
| ai agent builder | 2,400 | 43 | $10.85 | 信息 | 开源叙事切入口 |
| copilot studio | 27,100 | 75 | $5.96 | 信息 | Microsoft 对应竞品；Salesforce 买付费词 copilot agents |
| dify | 18,100 | 79 | $3.91 | 商业 | Olares 已有 Dify，品类对比核心词 |
| enterprise ai agent | 140 | 24 | $14.82 | 信息/商业 | ⭐ 企业级叙事；KD 低 |
| ai agent framework | 590 | 34 | $7.13 | 信息 | 开发者词 |
| build ai agent | 480 | 47 | $9.40 | 信息 | Salesforce 抢这个词（付费） |
| ai agent software | 480 | 54 | $13.61 | 信息 | |
| open source ai agent | 260 | 42 | $4.32 | 信息 | ⭐（临界 KD）Olares 切入点 |
| no code ai agent | 50 | 29 | $9.20 | 信息 | ⭐ 低代码 Agent 词 |
| self hosted ai agent | 10 | 0 | $4.59 | 信息 | ⭐⭐ GEO 前哨，语义完美契合 Olares |

### 产品 / 功能词（Agentforce 品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| agentforce | 12,100 | **23** | $11.97 | 信息 | ⭐ 品牌词 KD 仅 23，极低！写"what is agentforce"内容可切 |
| salesforce agentforce | 6,600 | 61 | $12.85 | 商业 | 高 KD，品牌词排不动 |
| agentforce pricing | 590 | **25** | $16.22 | 商业 | ⭐ 核心定价痛点词 |
| agentforce certification | 880 | 35 | $3.92 | 信息 | Trailhead 认证需求词 |
| agentforce use cases | 260 | **17** | $18.54 | 商业 | ⭐ 低 KD 高价值 |
| agentforce service agent | 390 | **27** | $20.64 | 信息 | ⭐ |
| agentforce builder | 320 | **22** | $18.55 | 商业 | ⭐ 构建工具词 |
| what is agentforce | 1,300 | **31** | $7.98 | 信息 | ⭐（临界）教育内容词 |
| agentforce sales agent | 140 | 32 | $12.22 | 信息 | |
| agentforce contact center | 140 | 36 | $26.54 | 信息 | 高 CPC |
| agentforce observability | 140 | **18** | $26.44 | 商业 | ⭐ 极低 KD + 极高 CPC |
| agentforce flex credits | 50 | 35 | $25.22 | 商业 | 定价细节词，焦虑点 |
| how much does agentforce cost | 40 | **26** | $18.75 | 信息/商业 | ⭐ 成本焦虑直接词 |
| agentforce demo | 320 | **28** | $33.03 | 商业 | ⭐ $33 CPC！最高商业意图 |
| salesforce ai consultant | 1,000 | **33** | **$35.19** | 信息/商业 | ⭐（临界）认证/职业词，CPC 极高 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| n8n alternative | 720 | 18 | $7.45 | 商业 | ⭐ 开源工作流最大替代词 |
| open source ai agent | 260 | 42 | $4.32 | 信息 | |
| dify | 18,100 | 79 | $3.91 | 商业 | Olares Market 已有 |
| flowise | 4,400 | 43 | $5.97 | 商业 | Olares Market 已有 |
| flowise alternatives | 50 | 14 | $0.67 | 商业 | ⭐ |
| no code ai agent | 50 | 29 | $9.20 | 信息 | ⭐ |
| self hosted ai agent | 10 | 0 | $4.59 | 信息 | ⭐ GEO 前哨 |
| ai workflow automation open source | 20 | – | $0 | 信息 | ⭐ GEO 前哨 |
| dify self hosted | 20 | – | $0 | 信息 | ⭐ GEO 前哨 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Agentforce 锁定在 Salesforce 生态内（必须 Enterprise Edition + $165/用户/月 Service Cloud），$2/对话 + Flex Credits 成本在规模化后可达数十万美元/年；Dify（✅ 已上架 Olares）+ Flowise（✅ 已上架 Olares）在 Olares 上提供完整的开源 AI Agent 构建能力，数据留本地、零 per-conversation 计费、无 Salesforce 许可依赖——这是 Agentforce 用户最不可能从官方渠道找到的解法。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| agentforce pricing | 590 | **25** | $16.22 | ⭐⭐⭐ 定价焦虑词；"Agentforce pricing vs self-hosted AI agent on Olares"：Dify+Flowise 零对话费 vs $2/conversation |
| what is agentforce | 1,300 | **31** | $7.98 | ⭐⭐ 教育内容词；写"What is Agentforce — and why some teams choose self-hosted alternatives"可植入 Olares 叙事 |
| agentforce use cases | 260 | **17** | $18.54 | ⭐⭐⭐ KD 极低；内容角度：同类 use case（销售助手/服务 Agent）在 Olares+Dify 上如何用自托管实现 |
| agentforce alternatives | 20 | 0 | $26.14 | ⭐⭐⭐ 目前竞争为零，先占位；Olares 是唯一"自托管 + 零许可费 + 数据留本地"的 Agentforce 平替 |
| agentforce alternative | 10 | 0 | $0 | ⭐⭐⭐ GEO 前哨；极低成本布局，等待品类教育后自动命中 |
| agentforce vs microsoft copilot | 20 | 0 | $0 | ⭐⭐ 对比词；写三方对比"Agentforce vs Copilot Studio vs Dify on Olares"，占 GEO 引用位 |
| agentforce competitors | 20 | 0 | $14.84 | ⭐⭐ GEO 词；Olares 内容中列出开源竞品矩阵，Dify/Flowise 优先 |
| open source ai agent | 260 | 42 | $4.32 | ⭐⭐ 直接切入"open source AI agent platform on Olares" |
| n8n alternative | 720 | 18 | $7.45 | ⭐⭐ n8n 用户也是 Agentforce 的潜在客户；Olares 提供 n8n 替代叙事 |
| agentforce observability | 140 | **18** | $26.44 | ⭐⭐ KD 18 + CPC $26 黄金组合；写"Agentforce observability vs self-hosted monitoring"，Olares 强调可观测性自主 |
| how much does agentforce cost | 40 | **26** | $18.75 | ⭐⭐⭐ 成本焦虑直接词；内容锚点："30 座团队用 Agentforce = Year-1 $200K+，用 Dify on Olares = $0"（数据来自 myaskai.com 评测） |
| agentforce builder | 320 | **22** | $18.55 | ⭐⭐ KD 22；写"Agentforce Builder vs Dify vs Flowise"低代码 Agent 构建工具对比 |
| self hosted ai agent | 10 | 0 | $4.59 | ⭐⭐⭐ GEO 前哨；近零量但完美契合 Olares；抢 AI Overview 引用位 |
| enterprise ai agent | 140 | **24** | $14.82 | ⭐⭐ 企业 Agent 词；叙事："enterprise AI agent without enterprise lock-in" |
| agentforce flex credits | 50 | 35 | $25.22 | ⭐ 计费机制复杂性词；Olares 叙事：无需计算 credits，自托管透明成本 |
| flowise alternatives | 50 | 14 | $0.67 | ⭐ Flowise 用户也是潜在 Olares 用户；写"Flowise on Olares"教程更直接 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| agentforce | 12,100 | **23** | $11.97 | 信息 | 主词候选 | ⭐ 品牌词 KD 仅 23，异常低——说明 Agentforce 是新品类，认知内容可切；写"what is agentforce"锚文章可排；Olares 作为对比叙事注入 |
| what is agentforce | 1,300 | **31** | $7.98 | 信息 | 主词候选 | ⭐ 临界 KD；与"agentforce"同一意图簇；写教育文章含"open source agentforce alternative"段落 |
| agentforce pricing | 590 | **25** | $16.22 | 商业 | 主词候选 | ⭐ 核心痛点词；$16 CPC 说明高商业价值；写"Agentforce pricing: real TCO vs self-hosted Dify on Olares"即刻有排名机会 |
| agentforce use cases | 260 | **17** | $18.54 | 商业 | 主词候选 | ⭐⭐ KD 17 极低 + CPC $18.54 极高；此词 Salesforce 虽排 #1 但 KD 很低，说明第三方内容也有机会；Olares 角度：写"agentforce use cases for teams without Salesforce" |
| agentforce alternatives | 20 | 0 | $26.14 | 商业 | 主词候选 | ⭐ 量小但 KD=0，CPC $26 说明有转化价值；先占后等——替代文章标题"Agentforce alternatives: open source options for non-Salesforce teams"；Olares+Dify 为核心推荐 |
| agentforce builder | 320 | **22** | $18.55 | 商业 | 主词候选 | ⭐ KD 22 低竞争；写"Agentforce Builder vs Dify vs Flowise for building AI agents"三方对比 |
| agentforce observability | 140 | **18** | **$26.44** | 商业 | 主词候选 | ⭐⭐ 隐藏金矿：KD 18 + CPC $26 = 极高价值低竞争；Olares 叙事：自托管 Agent 监控，数据留本地 |
| open source ai agent | 260 | 42 | $4.32 | 信息 | 次级 | 并入 Olares 自托管 AI Agent 对比文；Dify/Flowise on Olares 推荐 |
| agentforce service agent | 390 | **27** | $20.64 | 信息 | 次级 | ⭐ 产品功能词；并入 agentforce use cases 文章或独立写"agentforce service agent alternatives" |
| n8n alternative | 720 | 18 | $7.45 | 商业 | 次级 | ⭐ n8n 用户群与 Agentforce 潜在客户重合；并入开源工作流自托管文章 |
| how much does agentforce cost | 40 | **26** | $18.75 | 信息/商业 | 次级 | ⭐ 成本焦虑词；并入 agentforce pricing 文章；插入 TCO 对比表（$200K+ vs $0） |
| enterprise ai agent | 140 | **24** | $14.82 | 商业 | 次级 | ⭐ 企业 Agent 词；并入对比文章 |
| agentforce alternative | 10 | 0 | $0 | 商业 | GEO | ⭐⭐ 近零量 KD=0；现在布局，6–12 个月后受益；GEO 引用位先发 |
| self hosted ai agent | 10 | 0 | $4.59 | 信息 | GEO | ⭐⭐ 语义完美契合 Olares；抢 AI Overview / Perplexity 引用位 |
| agentforce vs microsoft copilot | 20 | 0 | $0 | 对比 | GEO | ⭐ 三方对比文章中作为段落处理；GEO 引用位 |
| dify self hosted | 20 | 0 | $0 | 信息 | GEO | ⭐ Olares 的 Dify 部署教程自然命中此词 |
| agentforce vs servicenow | 10 | 0 | $0 | 对比 | GEO | 并入对比文 FAQ |

---

## 核心洞见

1. **品牌护城河深但 KD 异常低——新品类定义期是最后的低成本窗口。** `agentforce` 品牌词 KD 仅 23，`agentforce use cases` KD 仅 17，`agentforce builder` KD 仅 22。对于一个 ARR $1.2B 的产品，这些数字极不寻常——原因是 Agentforce 是 Salesforce 内部强推的新品牌（2024 年 10 月 GA），市场内容生态刚起步，SEO 领域竞争者极少。**这个窗口不会持续超过 12–18 个月**：随着 Agentforce 认知扩大，竞品将迅速填充这些词。Olares 应立即布局 `agentforce use cases`（KD 17）、`agentforce builder`（KD 22）、`agentforce pricing`（KD 25）等低竞争词。

2. **Salesforce 的打法是"品类定义权内容战略"——可以学但不可正面硬刚。** Salesforce 用 /agentforce/ 子路径抢 `agentic ai`（90,500/月）、`multi-agent`（33,100/月）、`ai chatbot`（90,500/月）等超大信息词——不是靠品牌，而是靠规模化内容 + 域名权重。Olares 无法在这些顶级品类词上竞争，但可以学习这套"教育内容 → 产品转化"的落地页结构，在 Dify/Flowise 场景词上复制。

3. **对 Olares 最关键的三个词：`agentforce pricing`（590, KD 25）、`agentforce use cases`（260, KD 17）、`agentforce alternatives`（20, KD 0）。** `agentforce pricing` 是购买漏斗最高价值词：CPC $16 反映买家决策期焦虑，Olares 叙事"自托管 Dify+Flowise = $0/conversation"极具冲击力。`agentforce use cases` 量级合适且 KD 极低，写"无需 Salesforce 许可的同类 Agent 场景"最直接。`agentforce alternatives` 虽量小（20/月），但 KD=0、CPC $26 意味着转化率极高——每月就算 20 次搜索，转化 2 个用户也值得。

4. **最大攻击面：三重锁定痛点。** ①**Salesforce 生态锁定**：必须已有 Enterprise Edition（$165/用户/月），非 Salesforce 用户完全无法使用，中小企业和混合技术栈（HubSpot + AWS + Google Workspace）直接出局；②**隐性 TCO 爆炸**：30 座团队 Year-1 $200K–$450K+，Flex Credits 计费复杂（`agentforce flex credits` 词有 50/月 + CPC $25），企业财务团队普遍不适应 usage-based 模式；③**数据主权丧失**：所有 Agent 交互数据经过 Salesforce 的 Trust Layer，但仍在 Salesforce 基础设施上——监管行业（金融、医疗、政府）有明确的 on-premise 要求。这三点是 Olares + Dify/Flowise 叙事的精准切入口。

5. **隐藏低 KD 金矿：`agentforce observability`（KD 18, CPC $26）、`agentforce use cases`（KD 17, CPC $19）、`agentforce alternative`（KD 0）。** `agentforce observability` 是最意外的发现——KD 18 + CPC $26.44，Salesforce 自己用 /agentforce/observability/ 排 #1，但竞争极低，说明第三方内容几乎没有。对 Olares 的叙事是：自托管 Agent 的完整可观测性（日志、追踪、成本分析）在本地闭环，不依赖 Salesforce 的 Insights 功能。

6. **GEO 前瞻布局：** `self hosted ai agent`（KD 0）、`agentforce alternative`（KD 0）、`dify self hosted`（KD 0）、`agentforce vs microsoft copilot`（KD 0）——这四组词目前量极小但意图精准，正是 AI Overview / Perplexity 最喜欢引用的"权威对比"类内容。Salesforce 自己不会写"为什么有人应该用开源替代品而不是 Agentforce"，这就是 Olares 的 GEO 护城河：做 Salesforce 不愿做的内容。

7. **与既有分析的关联：** 本报告与 `olares-500-keywords` 中 `dify`（18,100/月）、`flowise`（4,400/月）词高度互补——这两个应用已在 Olares Market，但还没有"AI Agent 构建平台"使用场景的定位文章。Agentforce 分析揭示了一个重要缺口：当前 Dify/Flowise 报告以工具本身为主，缺少"vs 企业 AI Agent 平台"的叙事框架。建议写一篇"Agentforce vs Dify vs Flowise: Open Source AI Agent Builder Comparison"作为 Olares 的核心对比资产，一篇文章可同时覆盖 `agentforce pricing`、`agentforce alternatives`、`agentforce use cases`、`agentforce builder`、`open source ai agent` 五个 KD 低于 45 的词。

---

*数据来源：SEMrush US 数据库（domain_rank / domain_organic_subdomains / resource_organic / resource_adwords / phrase_these / phrase_related / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；企业 SaaS 类产品全球量通常为美国的 2–3 倍。Agentforce 是 2024 年 10 月新品牌，KD 数据反映的是当前竞争状态，预计 12–18 个月内随品类成熟显著上升。*
