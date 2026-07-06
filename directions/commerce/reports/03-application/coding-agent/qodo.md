# Qodo SEO 竞品分析报告

> 域名：qodo.ai | SEMrush US | 2026-07-06
> Qodo（原 CodiumAI）= AI 代码质量 Agent，融合 PR 审查 + 单元测试生成 + IDE 助手，开源底座 PR-Agent 已捐给社区，商业旗舰产品 Qodo 2.0 以多 Agent 架构领跑 AI Code Review 基准测试。

---

## 项目理解（前置）

Qodo（前身 CodiumAI，2024 年品牌迁移）是一家以"代码质量 Agent"为核心的以色列 AI DevTools 公司，融资 $120M（a16z 领投）。其旗舰产品 Qodo 2.0（2026 年 2 月发布）采用多 Agent 架构对 PR 进行深度审查，在第三方基准测试中 F1 得分 60.1%，领先第二名 9%。

产品线包含三件套：**Qodo Gen**（IDE 插件，VS Code/JetBrains，代码 + 测试生成）、**Qodo Merge**（Git 平台 PR 审查，GitHub/GitLab/Bitbucket/Azure DevOps）、**Qodo CLI**（命令行工具）。其开源前身 PR-Agent 已捐给社区，作为独立项目维护在 [github.com/The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)，可自托管、免费。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AI 代码质量 Agent：PR 多 Agent 审查 + IDE 测试生成 + CLI，企业级代码治理 |
| 开源 / 许可证 | 商业闭源（SaaS）；PR-Agent 开源分支独立维护（Apache 2.0，已捐给社区） |
| 主仓库 | [github.com/qodo-ai/pr-agent](https://github.com/qodo-ai/pr-agent)（社区维护，210+ contributors；官方商业版在 qodo.ai） |
| 核心功能 | 多 Agent PR 审查（bug / 安全 / 规范 / 测试覆盖四路专家 Agent）、IDE 代码 + 测试生成、Context Engine（多仓库感知）、Rules Miner（从 PR 历史自动挖掘编码规范）、PR Knowledge System |
| 商业模式 / 定价 | Free（个人）；Teams $30/用户/月（年付，含 2500 credits/月）；Enterprise 定制（约 $45+/用户/月，含 SSO、私有化部署、多仓库感知） |
| 差异化 / 价值主张 | 唯一将 PR 审查 + 测试生成 + IDE 助手集于一体的平台；多 Agent 架构 F1 最高；支持 air-gapped 私有化部署；PR-Agent 开源基础可自托管 |
| 主要竞品（初判）| CodeRabbit、GitHub Copilot（code review 功能）、Greptile、Augment Code |
| Olares Market | 未上架（PR-Agent 开源版本理论上可作为 Olares App 打包，但目前无官方 chart） |
| 来源 | [qodo.ai](https://www.qodo.ai)、[docs.qodo.ai](https://docs.qodo.ai)、[github.com/qodo-ai/pr-agent](https://github.com/qodo-ai/pr-agent)、[aicodereview.cc/blog/qodo-pricing](https://aicodereview.cc/blog/qodo-pricing/)、[rebrand article](https://aicodereview.cc/blog/codiumai-to-qodo/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | qodo.ai |
| SEMrush Rank | **108,298**（中等规模，SEO 仍在建设阶段） |
| 自然关键词数 | 7,336 |
| 月自然流量（US）| **17,754** |
| 自然流量估值 | $24,569/月 |
| 付费关键词数 | 80 |
| 月付费流量 | 1,334 |
| 付费流量成本 | $2,920/月 |
| 排名 1-3 位 | 75 词 |
| 排名 4-10 位 | 251 词 |
| 排名 11-20 位 | 835 词 |

> 旧域名 codium.ai：SEMrush Rank 1,380,363，仅剩 71 个关键词、666 月流量——品牌迁移后旧域流量基本归零，所有认知都在向 qodo.ai 重建。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.qodo.ai | 7,242 | 17,466 | 98.38% |
| docs.qodo.ai | 92 | 288 | 1.62% |
| qodo-merge-docs.qodo.ai | 1 | 0 | 0% |
| release-notes.command.qodo.ai | 1 | 0 | 0% |

> 流量极度集中于主站，docs 子域仅 1.62%——文档 SEO 有明显提升空间。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| qodo | 1 | 14,800 | 87 | $0.05 | 11,840 | 品牌 | / |
| qodo ai | 1 | 1,600 | 67 | $5.52 | 1,280 | 品牌 | / |
| qodo gen | 1 | 880 | 37 | $5.90 | 218 | 品牌/产品 | / |
| qodo merge | 1 | 320 | 43 | $4.50 | 256 | 品牌/产品 | docs…/code-review |
| qodogen | 1 | 320 | 23 | $6.24 | 256 | 品牌(误拼) | / |
| qodo ai code review | 1 | 170 | 27 | $7.14 | 136 | 品牌+功能 | / |
| qodo company | 1 | 170 | 53 | $0.00 | 136 | 品牌 | / |
| qodo ai coding assistant | 1 | 140 | 59 | $0.00 | 112 | 品牌 | / |
| codium | 3 | 3,600 | 67 | $4.82 | 108 | 品牌迁移 | / |
| codium ai | 2 | 1,300 | 65 | $4.42 | 106 | 品牌迁移 | / |
| qodo pricing | 1 | 110 | 27 | $6.58 | 88 | 商业 | /pricing/ |
| qodo formerly codiumai | 1 | 90 | 60 | $8.04 | 72 | 品牌迁移 | / |
| codiumai | 2 | 590 | 50 | $4.42 | 48 | 品牌迁移 | / |
| best ai for coding | 11 | 9,900 | 50 | $8.85 | 49 | 品类 | /blog/best-ai-coding-assistant-tools/ |
| qodo cli | 1 | 50 | 38 | $7.08 | 40 | 产品 | /features/qodo-cli/ |
| qodo code review | 1 | 50 | 31 | $4.49 | 40 | 品牌+功能 | / |
| cline vs cursor | 6 | 1,300 | 23 | $1.34 | 39 | 信息/对比 | /blog/cline-vs-cursor/ |
| pr agent | 4 | 590 | 23 | $8.16 | 12 | 品牌/产品 | docs…/code-review |
| augment code vs cursor | 4 | 1,000 | 9 | $7.97 | 22 | 对比 | /blog/augment-code-vs-cursor/ |
| windsurf vs cursor | 11 | 4,400 | 50 | $4.18 | 22 | 对比 | /blog/windsurf-vs-cursor/ |
| roo code vs cline | 4 | 480 | 21 | $6.78 | 21 | 对比 | /blog/roo-code-vs-cline/ |
| mcp server | 39 | 40,500 | 61 | $3.49 | 12 | 信息 | /blog/what-is-mcp-server/ |
| reusability | 10 | 4,400 | 28 | $1.01 | 22 | 信息 | /glossary/code-reusability/ |

> **注意**：流量 Top 1 的 `qodo`（月量 14,800，KD 87）独占 66% 自然流量——品牌词牢固但搜索量本身偏小；品牌迁移词（codium/codiumai）仍贡献约 250 流量，说明旧品牌认知尚未完全迁移。博客内容（coding assistant 对比、vs cursor 系列）正在为非品牌流量破局。

### 付费词（Google Ads，按流量排序）

买词规模较小（80 词，月花 $2,920），聚焦于企业级落地页和竞争对手场景词，主要导向 `/qodo-merge-lp-enterprise/` 和 `/features/qodo-git/` 落地页。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| qodo | 1 | 14,800 | $0.05 | /（自身品牌保护） |
| claude code review | 1 | 1,900 | $6.22 | /qodo-merge-lp-enterprise/ |
| qodo ai | 1 | 1,600 | $5.52 | /（品牌保护） |
| qodo gen | 1 | 880 | $5.90 | /（品牌保护） |
| secure code review | 1 | 480 | $8.12 | /qodo-merge-lp-enterprise/ |
| best gpt for coding | 1 | 390 | $8.68 | /ai-code-review-lp/ |
| greptile | 5 | 2,900 | $3.35 | /qodo-merge-lp-enterprise/（截竞品流量）|
| ai code review | 3 | 1,600 | $8.86 | /features/qodo-git/ |
| ai code review tools | 2 | 720 | $9.22 | /features/qodo-git/ |
| github ai code review | 1 | 260 | $6.08 | /git-integrations-ai-code-review/ |
| gitlab code review | 1 | 210 | $9.43 | /git-integrations-ai-code-review/ |
| is claude code good | 1 | 260 | $16.93 | /qodo-merge-lp-enterprise/（截 Claude 流量）|

> **打法**：主买"截流"策略——竞品词（greptile、claude code）+ 高 CPC 企业词（secure code review $8.12、ai code review $8.86）定向企业落地页；claude code review 系列词多条，说明在押注 Claude Code 普及带来的代码审查需求。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| coderabbit | 9,900 | 76 | $2.23 | 品牌 | 品类最大竞品，KD 很高 |
| github copilot alternative | 210 | 13 | $6.46 | 信息 | ⭐ KD 极低，高价值 |
| coderabbit alternative | 50 | 0 | $8.63 | 信息 | ⭐ 近乎零 KD，直接机会 |
| qodo vs coderabbit | 30 | 0 | $7.42 | 信息 | ⭐ 零 KD 对比词 |
| coderabbit vs qodo | 20 | 0 | $9.37 | 信息 | ⭐ 零 KD 对比词 |
| greptile alternative | 0 | 0 | $19.95 | 信息 | GEO 前哨（高 CPC 信号） |
| sourcegraph cody alternative | 10 | 0 | $0 | 信息 | ⭐ 低 KD |
| codium ai vs github copilot | 10 | 0 | $0 | 信息 | ⭐ 品牌迁移对比词 |
| qodo vs github copilot | 20 | 0 | $0 | 信息 | ⭐ 零 KD |
| qodo vs cursor | 50 | 14 | $0 | 信息 | ⭐ KD 低，VS 系列 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai coding assistant | 9,900 | 65 | $9.27 | 信息 | 大类词，竞争激烈 |
| ai code review | 1,900 | 45 | $9.54 | 信息 | 核心品类词，KD 中等 |
| code review tools | 1,000 | 35 | $8.49 | 信息 | ⭐ KD 中低，商业意图 |
| automated code review | 320 | 25 | $6.67 | 信息 | ⭐ 低 KD，自动化需求 |
| ai code review tools | 720 | 45 | $9.22 | 信息 | 品类列表词 |
| ai code analysis | 210 | 26 | $7.84 | 信息 | ⭐ 低 KD，细分功能 |
| best ai code review tools | 170 | 26 | $7.57 | 信息 | ⭐ 低 KD，比较意图 |
| code review automation | 110 | 9 | $8.90 | 信息 | ⭐⭐ KD 极低！高价值 |
| ai pull request review | 50 | 34 | $9.46 | 信息 | ⭐ 低 KD |
| ai unit testing | 70 | 31 | $7.08 | 信息 | ⭐ 低 KD |
| ai test generation | 20 | 0 | $9.42 | 信息 | ⭐ 近零 KD |
| ai testing tool | 210 | 57 | $8.29 | 信息 | 竞争略高 |
| github copilot code review | 590 | 53 | $5.55 | 信息 | 竞品功能词 |
| ai software testing | 590 | 54 | $10.38 | 信息/商业 | 高 CPC |
| gitlab ai code review | 170 | 23 | $4.29 | 信息 | ⭐ KD 低，平台词 |
| bitbucket ai code review | 110 | 28 | $4.41 | 信息 | ⭐ KD 低，平台词 |
| ai code review github | 90 | 40 | $5.21 | 信息 | 平台词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| qodo | 14,800 | 87 | $0.05 | 品牌 | 核心品牌词 |
| qodo ai | 1,600 | 67 | $5.52 | 品牌 | 品牌+类别 |
| qodo gen | 880 | 37 | $5.90 | 品牌/产品 | ⭐ IDE 插件产品词 |
| codium ai | 1,300 | 65 | $4.42 | 品牌迁移 | 旧品牌仍有量 |
| codiumai | 590 | 50 | $4.42 | 品牌迁移 | 旧品牌流量残留 |
| codium | 3,600 | 67 | $4.82 | 品牌迁移 | 量大但 KD 高 |
| qodo merge | 320 | 43 | $4.50 | 品牌/产品 | PR 审查产品线 |
| pr-agent | 110 | 18 | $8.16 | 品牌/工具 | ⭐ 开源底座关键词 |
| pr agent | 590 | 23 | $8.16 | 品牌/工具 | ⭐ KD 低，高 CPC |
| qodo pricing | 110 | 27 | $6.58 | 商业 | ⭐ 购买意图 |
| qodo cli | 50 | 38 | $7.08 | 产品 | CLI 工具词 |
| qodogen | 320 | 23 | $6.24 | 品牌误拼 | ⭐ 低 KD，品牌兜底 |
| is qodo free | 20 | 0 | $0 | 商业 | ⭐ 零 KD，FAQ 机会 |
| is qodo gen free | 20 | 0 | $0 | 商业 | ⭐ 零 KD，FAQ 机会 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source ai code review | 30 | 25 | $3.82 | 信息 | ⭐ 低 KD，直接机会 |
| open source code review tool | 10 | 0 | $4.12 | 信息 | ⭐ 零 KD |
| open source code review ai | 20 | 0 | $3.39 | 信息 | ⭐ 零 KD |
| pr agent self hosted | 0 | 0 | $0 | 信息 | GEO 前哨，有搜索意图 |
| self-hosted code review | 0 | 0 | $0 | 信息 | GEO 前哨 |
| pr-agent docker | 0 | 0 | $0 | 信息 | GEO（有 Docker 部署需求）|
| best open source ai | 480 | 39 | $3.27 | 信息 | 宽泛开源词，KD 中等 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Qodo 商业版闭源且按用量收费（credits 制），PR-Agent 开源版已捐给社区可自托管，Olares 可切入"在自己的服务器上跑 PR-Agent / 无 credits 限制 / 数据不出境"叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| open source ai code review | 30 | 25 | $3.82 | ⭐⭐⭐ Olares 上一键部署 PR-Agent（Qodo 的开源前身），无限量跑 PR 审查，对 Qodo Pro $30/用户/月有强替代叙事 |
| open source code review tool | 10 | 0 | $4.12 | ⭐⭐⭐ 零 KD，直接写"PR-Agent on Olares"教程可抢排名 |
| pr agent self hosted | 0 | 0 | $0 | ⭐⭐⭐ GEO 前哨：PR-Agent 是 Qodo 开源底座，Olares 提供自托管一键部署 + LLM API 自带（可接本地模型）|
| self-hosted code review | 0 | 0 | $0 | ⭐⭐⭐ GEO：Olares 是代码审查自托管最简方案（PR-Agent + 本地 LLM）|
| github copilot alternative | 210 | 13 | $6.46 | ⭐⭐ KD 极低，Olares 可定位为"让 PR-Agent（Qodo 开源版）在本地跑"的 Copilot 替代路径 |
| code review automation | 110 | 9 | $8.90 | ⭐⭐⭐ KD=9！Olares 可以打"自托管代码审查自动化"，接 PR-Agent 到 GitHub/GitLab webhook |
| coderabbit alternative | 50 | 0 | $8.63 | ⭐⭐ 零 KD，写 PR-Agent（Qodo 开源）vs CodeRabbit 对比，Olares 自托管角度 |
| automated code review | 320 | 25 | $6.67 | ⭐⭐ 低 KD，Olares + PR-Agent 场景教程 |
| ai code review open source | 30 | 25 | $3.82 | ⭐⭐ 同上，长尾版本 |
| qodo vs coderabbit | 30 | 0 | $7.42 | ⭐⭐ 零 KD 对比词，可写含 Olares 自托管维度的全对比文 |
| pr agent | 590 | 23 | $8.16 | ⭐⭐ 品牌词低 KD，Olares 教程"PR-Agent on Olares"可切入 |
| gitlab ai code review | 170 | 23 | $4.29 | ⭐⭐ KD 低，平台词，Olares 上的 PR-Agent 支持 GitLab |
| bitbucket ai code review | 110 | 28 | $4.41 | ⭐ 支持 Bitbucket，Olares 自托管可打 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| ai code review | 1,900 | 45 | $9.54 | 信息 | 主词候选 | 品类核心词，KD 中等可攻，Qodo 本身在此词排名不靠前，Olares + PR-Agent 可建独立内容切入 |
| code review automation | 110 | **9** | $8.90 | 信息 | 主词候选 | ⭐ KD 极低仅 9，高 CPC $8.90 说明强商业意图，Olares 自托管 PR-Agent 完美匹配"自动化"叙事 |
| github copilot alternative | 210 | **13** | $6.46 | 信息 | 主词候选 | ⭐ KD=13 超低，月量 210，Olares + PR-Agent 可作为"不依赖 GitHub 的替代方案"切入 |
| automated code review | 320 | 25 | $6.67 | 信息 | 主词候选 | ⭐ KD 低，Qodo Merge/PR-Agent 核心用例，Olares 自托管可写文章 |
| coderabbit alternative | 50 | **0** | $8.63 | 信息 | 主词候选 | ⭐ 零 KD，强商业意图，CodeRabbit 是 Qodo 最大竞品，机会极高 |
| pr agent | 590 | 23 | $8.16 | 信息/品牌 | 主词候选 | ⭐ Qodo 的开源底座，月量 590 + KD 低，"PR-Agent on Olares"可撑一篇文章 |
| open source ai code review | 30 | 25 | $3.82 | 信息 | 主词候选 | ⭐ Olares 直接机会：PR-Agent 是开源 AI 代码审查的代名词，Olares 提供最简自托管 |
| ai code review tools | 720 | 45 | $9.22 | 信息 | 次级 | 列表词，适合"top N ai code review tools"文章并入 |
| best ai code review tools | 170 | 26 | $7.57 | 信息 | 次级 | ⭐ 低 KD，合适并入品类对比文 |
| ai code analysis | 210 | 26 | $7.84 | 信息 | 次级 | ⭐ 细分功能词，Olares + PR-Agent 可覆盖 |
| gitlab ai code review | 170 | 23 | $4.29 | 信息 | 次级 | ⭐ 低 KD，平台集成词，PR-Agent 原生支持 GitLab |
| bitbucket ai code review | 110 | 28 | $4.41 | 信息 | 次级 | ⭐ 低 KD，PR-Agent 支持 Bitbucket |
| ai pull request review | 50 | 34 | $9.46 | 信息 | 次级 | ⭐ 功能描述词，on-topic |
| qodo vs coderabbit | 30 | 0 | $7.42 | 信息 | 次级 | 零 KD 对比词，可并入对比文 |
| qodo pricing | 110 | 27 | $6.58 | 商业 | 次级 | ⭐ 购买意图强，可在对比文章中覆盖 |
| code review automation | 110 | 9 | $8.90 | 信息 | 主词候选（见上）| 单独列出强调极低 KD |
| pr agent self hosted | 0 | 0 | $0 | 信息 | GEO | 自托管 PR-Agent 搜索意图明确，Olares 一键部署是完美落地 |
| self-hosted code review | 0 | 0 | $0 | 信息 | GEO | Olares 角度最强，AI Overview 抢占"如何自托管代码审查" |
| pr-agent docker | 0 | 0 | $0 | 信息 | GEO | Docker 部署是 PR-Agent 主要方式，Olares 有 OCI 容器层可简化 |
| is qodo free | 20 | 0 | $0 | 商业 | 次级 | FAQ 词，零 KD，可快速排名 |
| qodo vs cursor | 50 | 14 | $0 | 信息 | 次级 | ⭐ KD=14，VS 系列词，Qodo 专注代码质量而非生成 |

---

## 核心洞见

1. **品牌护城河**：`qodo`（月量 14,800，KD 87）牢牢占据第一，但绝对体量偏小——竞品 CodeRabbit（9,900）、Cursor AI（90,500）数量级差异显著，说明 Qodo 品牌心智仍在建设期。不建议正面打品牌词，应绕行至品类词 + 竞品比较词。旧品牌词（codium/codiumai，约 5,490 合计月量）仍在为 Qodo 导流但认知碎片化，说明品牌迁移 SEO 工作还未完成。

2. **可复制的打法**：Qodo 的博客开始用"X vs Y"系列文章（cline vs cursor、windsurf vs cursor、augment code vs cursor）在非品牌词上蹭热搜——这是低成本流量引入策略，值得复制。但文章用了开发者工具对比的热度，却导流到 Qodo 产品，逻辑略牵强。付费侧"截流 claude code review、greptile"关键词到企业落地页，CPC 高达 $6-17，说明企业转化路径明确。

3. **对 Olares 最关键的词**：
   - `code review automation`（月量 110，**KD=9**，CPC $8.90）——低竞争 + 高商业价值金矿
   - `open source ai code review` / `coderabbit alternative`——Olares 上自托管 PR-Agent 的直接着陆词
   - `github copilot alternative`（月量 210，KD=13）——超低 KD 大量词，PR-Agent 是真实可替代方案

4. **最大攻击面**：Qodo 的 credits 制（每用户 2500 credits/月）是主要痛点——高频 PR 团队会超额。PR-Agent 开源版（Qodo 的技术前身）可自托管且无限量；Olares 可打"同样 AI 能力，零 credits 限制，数据不出境"。另一痛点：CodeRabbit 在 free tier 对开源项目免费，Qodo 的 free tier 功能有限。

5. **隐藏低 KD 金矿**：
   - `code review automation`（KD=9！月量 110，CPC $8.90）——全品类最低 KD 高价值词
   - `coderabbit alternative`（KD=0，月量 50，CPC $8.63）——零 KD 直接机会
   - `github copilot alternative`（KD=13，月量 210）——超低 KD 相对大量词
   - `open source code review tool`（KD=0，月量 10）——零 KD，极长尾但精准

6. **GEO 前瞻布局**：
   - `pr agent self hosted`（零量，但搜索意图明确）——Olares 可写"How to self-host PR-Agent on Olares"抢 AI Overview
   - `self-hosted code review`（零量）——将成为 AI Privacy/Compliance 需求热词
   - `pr-agent docker`（零量）——技术极客部署词，Olares 简化 Docker 流程可引用
   - `how to review ai generated code`（月量 10）——AI coding 普及后必增的问题词
   - `is qodo free`（月量 20，KD=0）——价格透明 FAQ，零门槛排名

7. **与既有分析的关联**：与 `olares-500-keywords` 词表的关联主要在 DevTools 自托管方向——本报告发现的 `code review automation`（KD=9）和 `coderabbit alternative`（KD=0）是此前未覆盖的超低 KD 词，补充了 coding agent 品类的自托管需求缺口。与 devin.md 报告的 coding agent 方向互补：Devin 对应 Agent 自主编程，Qodo/PR-Agent 对应代码审查质量保证，两者受众重叠（DevOps/工程团队）但场景不同。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
