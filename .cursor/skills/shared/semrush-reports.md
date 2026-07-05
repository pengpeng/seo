# Semrush report 速查表（共享）

[brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md) 与 [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md) 共用的 Semrush report 速查。唯一权威，改这里即可，两个 skill 都指向本文件。

工作流恒为：**discovery 工具（无参）→ `get_report_schema(report)` → `execute_report(report, params)`**。参数以 `get_report_schema` 实际返回为准（常见 `database`、`domain`/`phrase`、`display_limit`、`display_offset`、`display_sort`、`display_filter`）。默认 `database=us`；探索性查询 `display_limit=30-50`；搜索量为美国月均。

## 流量基线（Phase 1，有独立官网时）

| 用途 | discovery 工具 | report | 备注 |
|------|---------------|--------|------|
| 单日快照：Rank、关键词数、流量、成本 | `domain_overview` | `domain_rank` | 一行当前指标 |
| 全区域 Rank / 全球排名 | `domain_overview` | `domain_ranks` | 多区域 |
| Rank 历史趋势（月度） | `domain_overview` | `resource_rank_history` | 一次返回全时序，勿循环 |
| 全量自然关键词（position/vol/KD/CPC/traffic/URL） | `organic_research` | `resource_organic` | 主力表，按 traffic 降序 |
| 子域名流量分布 | `organic_research` | `domain_organic_subdomains` | 如 docs./blog. |
| 按页面聚合的流量 | `organic_research` | `resource_organic_unique` | 找带流量的落地页 |
| 付费词（Google Ads） | `paid_search_research` | `resource_adwords` | position/CPC/vol/traffic；多数开源模型无付费 |
| 广告文案 + 落地页 | `paid_search_research` | `resource_adwords_unique` | 看"买大词导向哪个页" |
| 付费历史 | `paid_search_research` | `domain_adwords_historical` | 近 12 月 |

## 关键词扩展（Phase 2）

| 用途 | discovery 工具 | report | 备注 |
|------|---------------|--------|------|
| 单词摘要（vol/CPC/竞争/KD） | `keyword_research` | `phrase_this` | 单个词 |
| 批量词摘要 | `keyword_research` | `phrase_these` | `phrase` 分号分隔，最多 100；型号词/引擎组合词批量查 |
| 语义相关词 | `keyword_research` | `phrase_related` | 扩词主力 |
| broad match / 长尾变体 | `keyword_research` | `phrase_fullsearch` | 抓 `<x> local/vram/fp8/install` 类长尾 |
| 问题词 | `keyword_research` | `phrase_questions` | 信息意图选题，如 "how to run X locally" |
| 批量 KD | `keyword_research` | `phrase_kdi` | 分号分隔 |
| 某词的 SERP 域名 | `keyword_research` | `phrase_organic` / `phrase_adwords` | 看谁在排名/投放（常是 HF/Reddit/教程站） |

## 竞品发现（Phase 2 前置）

| 用途 | discovery 工具 | report | 备注 |
|------|---------------|--------|------|
| 自然竞品域名 | `competitors_research` | `domain_organic_organic` | 相关度+共有词数+流量 |
| 付费竞品域名 | `competitors_research` | `domain_adwords_adwords` | |
| 多域名关键词 gap（≤5 域名） | `competitors_research` | `domain_domains` | 共有/独有/缺失词 |
| 外链竞品 | `competitors_research` | `backlinks_competitors` | |

> 历史报告脚注里出现的 `phrase_these / phrase_related / resource_organic / resource_adwords / domain_organic_subdomains / domain_rank` 均为上表 report，可直接沿用。
