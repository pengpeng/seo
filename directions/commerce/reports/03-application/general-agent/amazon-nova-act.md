# Amazon Nova Act SEO 竞品分析报告

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> AWS 旗舰浏览器 AI 操作 Agent，$4.75/小时的企业级 UI 工作流自动化服务

---

## 项目理解（前置）

Amazon Nova Act 是 AWS 于 2025 年 re:Invent 大会正式 GA 的浏览器操作 Agent 服务，使用自研 Nova 2 Lite 模型，允许开发者用自然语言 + Python 构建可批量部署、企业级可靠性（>90% 任务成功率）的浏览器 UI 自动化 Agent 舰队。与 Anthropic Computer Use / OpenAI Operator 相比，Nova Act 定位是"生产环境浏览器自动化"而非"通用电脑操作"——当前仅支持浏览器（不含桌面 GUI），但与 Amazon Bedrock AgentCore、Strands Agents、CloudWatch、IAM 深度集成，走企业部署路线。对应的 Olares 开源平替是 **DeerFlow 2.0**（自托管深度研究 Agent，具备网页浏览与信息提取能力）以及可在 Olares 上部署的 browser-use（开源浏览器操作库）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AWS 托管的企业级浏览器 UI 自动化 Agent 服务（computer use 子集） |
| 开源 / 许可证 | SDK 为 Apache-2.0 开源；服务本体闭源，仅限 AWS 托管 |
| 主仓库 | [github.com/aws/nova-act](https://github.com/aws/nova-act)（★ 911，Python SDK） |
| 核心功能 | 浏览器 UI 工作流自动化、HITL 人工干预、Agent 舰队管理、Bedrock AgentCore 集成、MCP/Tool 调用 |
| 商业模式 / 定价 | 按 Agent 时长计费：$4.75/agent hour（HITL 等待时间不计费）；开发期可免费用 SDK + Playground |
| 差异化 / 价值主张 | AWS 全球基础设施可靠性 + 原生 IAM/CloudWatch 集成 + 90%+ 任务可靠率；与 Strands Agents 框架开箱即用 |
| 主要竞品（初判）| Browser Use（开源）、Browserbase（云托管）、OpenAI Operator、Anthropic Computer Use、Skyvern、Stagehand |
| Olares Market | 未上架；DeerFlow 2.0 / browser-use 为 Olares 侧开源平替 |
| 来源 | [官网](https://aws.amazon.com/nova/act/)、[定价页](https://aws.amazon.com/nova/pricing/)、[GitHub SDK](https://github.com/aws/nova-act)、[GA 博客](https://aws.amazon.com/blogs/aws/build-reliable-ai-agents-for-ui-workflow-automation-with-amazon-nova-act-now-generally-available/) |

---

## 流量基线（Phase 1）

> 降级模式：Amazon Nova Act 无独立域名（使用 aws.amazon.com），跳过域名流量报告，直接从关键词层分析。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 产品 / 品牌词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| nova act | 1,300 | 67 | $0 | 信息/商业 | 最高量品牌词，KD 67 护城河中等 |
| amazon nova act | 720 | 66 | $6.65 | 商业 | 有人投广告，CPC $6.65 |
| computer use agent | 880 | 57 | $0 | 信息 | 品类核心词，Nova Act 主战场 |
| aws nova act | 210 | 70 | $1.59 | 商业 | 强品牌绑定，KD 高 |
| ai browser agent | 260 | 68 | $7.00 | 信息 | 高 CPC 商业意图明显 |
| bedrock agentcore | 1,300 | 49 | $3.40 | 商业 | ⭐ Nova Act 配套服务词，KD 中等 |
| nova act sdk | 140 | 54 | $0 | 信息 | 开发者查文档入口 |
| nova act github | 40 | 53 | $0 | 导航 | GitHub 仓库直达词 |
| nova act bedrock | 30 | — | $0 | 信息 | 长尾集成词 |
| nova act pricing | 20 | — | $0 | 商业 | ⭐ 价格敏感词，GEO 机会 |
| amazon nova act sdk | 40 | 57 | $0 | 信息 | 开发者文档词 |
| what is amazon nova act | 20 | — | $0 | 信息 | ⭐ GEO 前哨词 |

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| browser use | 6,600 | 53 | $6.51 | 信息 | 最大竞品词，开源 browser-use 吃主量 |
| browserbase | 5,400 | 31 | $5.22 | 商业 | ⭐ 竞品 Browserbase，KD 31 可攻 |
| claude computer use | 2,900 | 41 | $15.02 | 信息 | ⭐ Anthropic 侧高 CPC 词 |
| openai operator | 2,400 | 72 | $5.87 | 商业 | OpenAI 竞品，KD 高 |
| anthropic computer use | 1,000 | 49 | $8.36 | 信息 | ⭐ 高 CPC 替代意图词 |
| openai computer use | 390 | 50 | $15.45 | 信息/商业 | ⭐ 极高 CPC，商业意图强 |
| browser use alternative | 110 | 19 | $1.78 | 信息 | ⭐⭐ KD 19 低竞争，对比文首选 |
| playwright alternative | 70 | 10 | $5.54 | 信息 | ⭐⭐ KD 10，传统脚本迁移词 |
| puppeteer alternative | 40 | 11 | $5.40 | 信息 | ⭐⭐ KD 11，迁移意图 |
| skyvern alternative | 0 | — | $7.54 | 商业 | GEO 前哨，有人出价但量近零 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai automation tools | 2,400 | 56 | $9.83 | 信息/导航 | 超级大词，CPC $9.83 |
| browser use github | 720 | 45 | $0 | 导航 | ⭐ browser-use 开源流量 |
| agentic browser | 880 | 38 | $5.00 | 信息 | ⭐ 新兴品类词，KD 尚低 |
| agent browser | 1,900 | 42 | $5.93 | 信息 | ⭐ 高量且 KD 中等 |
| browser agent | 1,600 | 52 | $5.93 | 信息 | 品类核心词 |
| computer use | 1,300 | 51 | $1.19 | 信息 | Anthropic 起源词 |
| computer use agents | 1,300 | 58 | $0 | 信息 | 复数品类词 |
| vision agent | 320 | 34 | $4.46 | 信息 | ⭐ 多模态操作 Agent |
| multimodal agent | 110 | 43 | $4.65 | 信息 | 品类上位词 |
| playwright ai | 590 | 42 | $6.52 | 信息 | 传统测试框架 + AI 词 |
| deerflow | 590 | 39 | $0 | 信息/导航 | ⭐ Olares 平替 DeerFlow 品牌词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source ai agent | 260 | 42 | $4.32 | 信息 | ⭐ 开源 Agent 入口词 |
| local ai agent | 210 | 31 | $5.06 | 信息 | ⭐ 本地部署意图，KD 31 |
| open source rpa | 140 | 41 | $4.26 | 信息 | ⭐ RPA 替换词，Olares 可接 |
| deep research open source | 140 | 52 | $0 | 信息 | DeerFlow 最直接机会词 |
| open source computer use agent | 20 | — | $6.58 | 信息 | ⭐ GEO 前哨，高 CPC 商业意图 |
| self hosted browser automation | 20 | — | $0 | 信息 | ⭐ 直接 Olares 平替词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Nova Act = 闭源 AWS 锁定 + $4.75/小时计费；Olares 的切入是"自托管深度研究与网页 Agent，数据留本地，永不按小时计费"——DeerFlow 2.0 做研究调研，browser-use 可做 UI 自动化，全部跑在自己硬件上。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合 |
|--------|------|----|----|-----------|------|
| browser use alternative | 110 | 19 | $1.78 | browser-use 开源版可装 Olares，对比"托管 vs 自托管"成本 | ⭐⭐⭐ |
| open source computer use agent | 20 | — | $6.58 | DeerFlow + browser-use 是 Nova Act 的开源平替，自托管无按时计费 | ⭐⭐⭐ |
| self hosted browser automation | 20 | — | $0 | Olares 运行 browser-use/Playwright，完全本地 | ⭐⭐⭐ |
| local ai agent | 210 | 31 | $5.06 | Olares 跑 DeerFlow 2.0 = 本地 AI Agent，数据不出家门 | ⭐⭐⭐ |
| open source ai agent | 260 | 42 | $4.32 | DeerFlow 2.0 + Olares Market 路线，开源托管无锁定 | ⭐⭐⭐ |
| deerflow | 590 | 39 | $0 | DeerFlow 是 Olares 侧主角，搜量 590 有一定受众 | ⭐⭐⭐ |
| deep research open source | 140 | 52 | $0 | DeerFlow 2.0 = 开源深度研究 Agent，Olares 一键跑 | ⭐⭐⭐ |
| open source rpa | 140 | 41 | $4.26 | RPA 场景 → 开源 browser-use / DeerFlow 组合替代 Nova Act | ⭐⭐ |
| playwright alternative | 70 | 10 | $5.54 | 传统 Playwright 脚本迁移到 AI Agent，Olares 可跑 browser-use | ⭐⭐ |
| browserbase alternative | 20 | — | $5.49 | Browserbase 用户找替代 → Olares 自托管远程浏览器 | ⭐⭐ |
| agentic browser | 880 | 38 | $5.00 | 新兴品类词，Olares 可参与品类叙事 | ⭐⭐ |
| nova act pricing | 20 | — | $0 | 价格敏感词，对比 Nova Act $4.75/hr vs Olares 一次性部署 | ⭐⭐ |
| anthropic computer use | 1,000 | 49 | $8.36 | 高 CPC 词，Olares + DeerFlow 做开源对比文获取商业流量 | ⭐ |
| claude computer use | 2,900 | 41 | $15.02 | 超高 CPC，写"claude computer use vs open source"文章机会 | ⭐ |
| aws bedrock agent | 170 | 57 | $6.15 | AWS 锁定词，反叙事"不想被 AWS 锁定？" | ⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|----|------|------|--------------------------|
| claude computer use | 2,900 | 41 | $15.02 | 信息 | 主词候选 | ⭐ KD 41 + 超高 CPC $15，与 Nova Act / Olares 开源平替对比文的锚点词 |
| browser use | 6,600 | 53 | $6.51 | 信息 | 主词候选 | 最大竞品品牌词，开源 browser-use；写"browser-use vs Nova Act"拦截迁移流量 |
| computer use agent | 880 | 57 | $0 | 信息 | 主词候选 | Nova Act 所在品类词，信息意图宜做深度解析文 |
| bedrock agentcore | 1,300 | 49 | $3.40 | 商业 | 主词候选 | Nova Act 配套服务词，可借势写 AWS 生态 vs 开源方案对比 |
| agentic browser | 880 | 38 | $5.00 | 信息 | 主词候选 | ⭐ 新品类词 KD 38，值得参与叙事争品类心智 |
| openai computer use | 390 | 50 | $15.45 | 信息/商业 | 主词候选 | ⭐ CPC $15.45 最高，开源替代文拦截商业意图 |
| nova act | 1,300 | 67 | $0 | 信息/商业 | 次级 | KD 67 护城河较高，不做主攻，做品牌提及词 |
| amazon nova act | 720 | 66 | $6.65 | 商业 | 次级 | 品牌核心词，KD 66 难排，做对比/FAQ 页侧翼渗透 |
| deerflow | 590 | 39 | $0 | 信息/导航 | 次级 | ⭐ Olares 平替品牌词，KD 39 可排；与 Nova Act 对比文中做内链 |
| open source ai agent | 260 | 42 | $4.32 | 信息 | 次级 | ⭐ Olares 核心叙事词，"开源 AI Agent" 在 Market 上架 |
| local ai agent | 210 | 31 | $5.06 | 信息 | 次级 | ⭐ KD 31 低，本地 Agent 意图直接匹配 Olares |
| browser use alternative | 110 | 19 | $1.78 | 信息 | 次级 | ⭐⭐ KD 19 超低，替代文首选，Olares 自托管方案直接接盘 |
| playwright alternative | 70 | 10 | $5.54 | 信息 | 次级 | ⭐⭐ KD 10，脚本迁移意图，门槛最低攻击面 |
| open source rpa | 140 | 41 | $4.26 | 信息 | 次级 | ⭐ RPA 用户寻开源替代，DeerFlow + browser-use 可承接 |
| nova act pricing | 20 | — | $0 | 商业 | GEO | ⭐ 价格敏感词近零量，"Nova Act 多少钱 vs 开源免费" 进 FAQ 抢引用位 |
| open source computer use agent | 20 | — | $6.58 | 信息 | GEO | ⭐ 极小量高 CPC，精准开源意图，DeerFlow / browser-use 前瞻布局 |
| self hosted browser automation | 20 | — | $0 | 信息 | GEO | ⭐ 直接 Olares 场景词，进教程文 H2 抢 AI Overview 引用 |
| skyvern alternative | 0 | — | $7.54 | 商业 | GEO | 有人出价但量 ≈ 0，语义精准，抢 AI 引用位 |
| what is amazon nova act | 20 | — | $0 | 信息 | GEO | 信息类问题词，进 FAQ 段落 |

---

## 核心洞见

1. **品牌护城河**：`nova act`（KD 67）/ `amazon nova act`（KD 66）护城河较高，正面攻品牌词性价比低。Nova Act 是 AWS 大树品牌背书，中小内容方难以正面竞争。**建议侧翼打法**：抢品类词（`computer use agent` / `agentic browser`）和竞品对比词（`claude computer use` / `browser use alternative`），而非品牌词本身。

2. **可复制的打法**：Nova Act 的 CPC 均值偏低（主词基本 $0 投放），但品类词 `claude computer use`（CPC $15.02）、`openai computer use`（$15.45）的商业意图极强——这说明"computer use" 对比赛道有高付费意愿。内容策略：**写"X computer use vs 开源 Agent"系列对比文**（`claude computer use` / `anthropic computer use` 为锚点），侧面建立 Olares/DeerFlow 的开源替代心智。

3. **对 Olares 最关键的词**：
   - `browser use alternative`（KD 19，月量 110）——最低竞争、最直接的开源平替入口；
   - `local ai agent`（KD 31，月量 210）——Olares 自托管叙事的精准锚点；
   - `deerflow`（KD 39，月量 590）——Olares 平替 DeerFlow 2.0 的自有品牌词，可先拿下。

4. **最大攻击面**：**闭源锁定 + 按小时计费**。$4.75/agent hour 的计费模式对高并发或长时任务代价昂贵；数据需流经 AWS（数据主权问题）。Olares + browser-use/DeerFlow = 一次部署、无计量费、数据留本地——`nova act pricing`（GEO）词中直接对比即是最尖锐的攻击点。

5. **隐藏低 KD 金矿**：`playwright alternative`（KD 10，月量 70）和 `puppeteer alternative`（KD 11，月量 40）——传统脚本开发者寻求 AI 升级，KD 几乎无壁垒，且 CPC 超 $5 说明有商业价值。写"从 Playwright 迁移到 AI Agent"教程，自然带出 browser-use 开源方案在 Olares 上的部署。

6. **GEO 前瞻布局**：
   - `open source computer use agent`（近零量，CPC $6.58）——精准开源意图，答案型内容放 FAQ 抢 AI Overview；
   - `self hosted browser automation`（近零量）——直接 Olares 部署词，进教程 H2；
   - `skyvern alternative`（量 ≈ 0，CPC $7.54 说明商业有人关注）——竞品生态前瞻布局；
   - `what is amazon nova act`——产品认知词进入 AI 引用池，结合开源对比建立认知。

7. **与既有分析的关联**：`ai automation tools`（月量 2,400，KD 56）已是跨报告大词，`computer use`（月量 1,300）与 Anthropic/OpenAI 的 computer use 报告共享流量——建议在 commerce 层做"computer use agent 品类总索引页"统筹 Nova Act / Claude / OpenAI Operator 三篇报告的内链，集中权重。`deerflow` 词（590/mo，KD 39）是 Olares 自身平替产品的品牌词，应尽快占位避免他人抢先。

---

*数据来源：SEMrush US 数据库（phrase_these × 3批次、phrase_related × 2、phrase_fullsearch、phrase_questions × 2）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
