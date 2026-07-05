---
name: brand-seo-research
description: 用 Semrush 研究一个品牌/关键词的 SEO——流量基线、关键词扩展、找出与 Olares 相关的词并输出洞见。当用户要分析某个品牌/产品的网站流量、自然/付费关键词、竞品，或要为 Olares 找内容机会时使用。
---

# 品牌 SEO 研究

给定一个品牌名或关键词，用 Semrush（MCP `user-semrush`）产出一份四阶段竞品分析报告，并在其前置一段项目理解。目标详略参照黄金样例 [commerce/reports/lovable.md](/Users/pengpeng/seo/directions/commerce/reports/03-application/vibe-coding/lovable.md)。**流量/关键词数据必须来自真实的 Semrush 调用**；前置的项目理解用公开来源（官网 / GitHub / 文档），需标注来源——两者都禁止凭常识编造。

report 名与参数速查见 [reference.md](reference.md)；完整输出模板见同文件末尾。

## Step 0 · 预检

1. **确认 Semrush 已登录**：先跑一次轻量调用（`domain_overview` 工具 → `domain_rank`，或 `keyword_research` → `phrase_this`）。若返回鉴权/权限错误，停下并提示用户登录 Semrush，不要继续编数据。
2. **判断输入类型**：
   - 有独立官网（品牌）→ 走完整流程 Step 1-5。
   - 纯场景词 / 无官网（如 Steam Headless、某个 Docker 镜像）→ **降级模式**：项目理解（Step 1）仍要做（先讲清这项技术/场景是什么），但跳过 Step 2 的域名报告，直接从 Step 3 的关键词层面做起，报告抬头注明"场景词分析（无独立官网）"。
3. **默认参数**：`database=us`；探索性查询 `display_limit=30-50`；搜索量为美国月均。
4. 工作流固定为：discovery 工具 → `get_report_schema(report)` → `execute_report`。report 名以 discovery/schema 返回为准。

## Step 1 · 项目理解（前置调研，非 Semrush）

进 Semrush 之前，先用**独立搜索**（web 搜索 + 抓取官网 / GitHub / 文档）把这个品牌/项目搞清楚。它给整份报告定调：抬头的"一句话品牌定位"、关键词意图打标、Phase 3 的"Olares 角度"都由它推导。

逐条查明并标注来源：

- **一句话是什么**：品类 + 定位（它解决什么问题、给谁用）。
- **是否开源**：许可证 + 主仓库（GitHub URL 与 star 量级）；闭源则注明。
- **核心功能**：3-5 点。
- **目标用户 / 典型场景**。
- **商业模式与定价**：开源 / 免费 / SaaS / 自托管；主要价格档。
- **差异化与价值主张**：为什么用户选它（vs 竞品的独特点）。
- **主要竞品（初判）**：手工列 2-4 个，供 Phase 2 的 `competitors_research` 印证/修正。
- **是否已在 Olares Market**：查 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md)。

产出：2-4 句项目介绍 + 一张关键事实表（模板见 [reference.md](reference.md) 的"项目理解（前置）"小节），来源随手标注。

## Step 2 · 流量基线（Phase 1）——尽可能全面

| 目的 | 工具 → report |
|------|---------------|
| SEMrush Rank、自然/付费关键词数、月流量、流量估值、付费流量 | `domain_overview` → `domain_rank` |
| 子域名流量分布 | `organic_research` → `domain_organic_subdomains` |
| 全量 TOP 自然关键词（排名/月量/KD/CPC/流量/意图/URL） | `organic_research` → `resource_organic` |
| 付费词 + 广告落地页 | `paid_search_research` → `resource_adwords`、`resource_adwords_unique` |

- 排名分布（1-3 / 4-10 / 11-20 词数）来自 `resource_organic` 按 position 分档统计。
- 自然关键词表按**流量**降序，逐词标 URL 与意图（品牌/导航/信息/商业/集成/品类）。特别留意：品牌误拼变体、插件/版本号/型号带流量、程序化落地页（`/guides/`、`/solutions/use-case/`）——这些是最重要的洞察来源。
- 付费词重点看"买什么超级大词 + 导向哪个落地页"。

## Step 3 · 关键词扩展（Phase 2）

1. **竞品发现**（新增环节，别靠手工联想）：`competitors_research` → `domain_organic_organic`（自然竞品）、`domain_adwords_adwords`（付费竞品）。拿到竞品域名后可回头补充对比词。
2. **扩词**：`keyword_research` →
   - `phrase_these` / `phrase_this`：竞品/替代词、品类词的量/KD/CPC。
   - `phrase_related`：语义相关词探底。
   - `phrase_fullsearch`：broad match / 长尾变体。
   - `phrase_questions`：问题词（信息意图内容选题）。
   - `phrase_kdi`：批量补 KD。
3. **固定分组输出**（按月量降序）：
   - 竞品 / 替代词（X alternative、X vs Y）
   - 品类词
   - 产品 / 功能词（品牌前缀）
   - **开源 / 自托管信号词**（Olares 机会前哨，即使量小也要列）
4. 标注 `⭐ = KD<30 且量>0` 的机会词。

## Step 4 · Olares 关联词（Phase 3）

从 Step 3 的词里筛"KD 低 + 与 Olares 场景契合"的词，每词加一列【Olares 角度】。至少覆盖：

- `X alternative` / `X vs Y` 对比（Olares 一键部署/同时支持两者）
- `self-hosted` / `open source X`（Olares Market 直接机会）
- Market 已上架应用的应用词、教程词、集成词
- 中文词（若该品牌有中文用户群）
- 用 `⭐⭐⭐ / ⭐⭐ / ⭐` 标契合度。

## Step 5 · 洞见 + Top 10 行动清单

**Top 10 打分**（写清依据，不要拍脑袋）：综合评分由四要素决定——月量越大越好、KD 越低越好、CPC 越高（商业价值）越好、与 Olares 场景契合度越高越好。分档：
- ⭐⭐⭐ = 量可观（≥1000）且 KD<25，或 KD 极低（<15）且商业意图强。
- ⭐⭐ = 量中等且 KD<30，或高 CPC 对比/替代词。
- ⭐ = 量小但精准、零竞争、或 GEO 前瞻词。

每行给"关键词 / 月量 / KD / 评分 / 一句话内容方向"。

**核心洞见**固定回答这几问：
1. 品牌护城河（品牌词心智）——能否正面刚？
2. 有什么可复制的打法（程序化落地页、买大词、内容带流量）？
3. 对 Olares 最关键的 2-3 个词是什么？
4. 最大攻击面（定价/闭源/credits 等痛点词）？
5. 隐藏低 KD 金矿？
6. GEO 前瞻词（近零量但语义契合，抢 AI Overview/Perplexity 引用位）？
7. 与既有 `olares-500-keywords` 词表的关联/补充？

## 输出约定

- 文件命名 `<brand>.md`（无前缀、无日期，git 记录变更历史；同名报告直接覆盖更新），按归类落目录：Market/可自部署项目→`directions/market/reports/`；商业付费竞品→`directions/commerce/reports/`（清单 [commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md)）；隐私/安全→`directions/privacy/reports/`；底层技术栈/自建单一工具→`directions/tech/reports/`。开源模型请改用 [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)。
- **产出后回写清单状态**：在对应清单里把该项标 `✅`（沿用清单现有 `✅ / ⬜` 记号）——[commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md)、[hardware/devices.md](/Users/pengpeng/seo/directions/hardware/devices.md)、[privacy/services.md](/Users/pengpeng/seo/directions/privacy/services.md)、[tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)。
- **重写已存在的报告前，先读现有同名报告（git 历史 / 当前文件）与相关洞见文档**：非重复的旧洞见尽量保留、去重合并；若不认可旧观点，明确指出并给出依据——不要每次重跑把有价值的历史判断冲掉。
- 抬头：`> 域名：<domain> | SEMrush <database> | <date>` + 一句话品牌定位。
- 结尾脚注：`数据来源：SEMrush <db> 数据库（列出实际用到的 report 名）| <date>` 及"搜索量为美国月均，技术类产品全球量通常为美国的 3-5 倍"。
- 表格与分节顺序严格套用 [reference.md](reference.md) 的模板。
