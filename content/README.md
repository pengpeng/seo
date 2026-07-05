# content/ — 可发布文章

[seo-content](/Users/pengpeng/seo/.cursor/skills/seo-content/SKILL.md) skill 的落盘目录：把竞品报告里的高机会词写成的对比/替代文（`X alternative`、`X vs Y`、`best self-hosted X`）。主线 2「方法论/落地」的产出。

- 每篇文章：`content/<slug>.md`（`<slug>` 全小写短横线，含主词根，如 `lovable-alternative`、`replit-vs-lovable`、`best-self-hosted-vibe-coding`）；无日期前缀，git 记录变更；同题覆盖更新。
- 每篇带 front-matter：

```yaml
---
title: <文章标题>
target_keyword: <主关键词>
secondary_keywords: [<次级词>, ...]
meta_description: <≤155 字符>
slug: <slug>
article_type: alternative | versus | listicle
source_report: directions/<cat>/reports/<x>.md
scenario: <scenarios.md 场景号或名>
schema: Article | FAQPage
status: draft | ready | published
---
```

## 与其它目录的区别

- `content/`（本目录）＝**成品文章**（对外可发布）。
- `directions/*/reports/`＝**SEO 竞品研究**（找词/竞品数据，brand/model-seo-research 产出）。
- `research/`＝**通用深度调研**（懂主题/市场/公司，deep-research 产出）。

> 写作口径、事实纪律与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)；选题的"场景↔产品"原则见 [scenarios.md](/Users/pengpeng/seo/scenarios/scenarios.md)。
