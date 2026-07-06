# 参考：Semrush report 速查 + 模型报告输出模板

## 一、Semrush report 速查表

见共享速查 [../shared/semrush-reports.md](/Users/pengpeng/seo/.cursor/skills/shared/semrush-reports.md)。模型研究**以 `keyword_research` 系列为主力**（很多模型无官网 → 跳过 Phase 1 域名报告，直接扩词）；有厂商官网时才用 `domain_rank` / `resource_organic` 打底，并注意剥离真正属于本模型的词。型号词/引擎组合词用 `phrase_these` 批量查，`<model> local/vram/fp8` 类长尾用 `phrase_fullsearch`。

---

## 二、模型报告输出模板

```markdown
# <Family> 模型 SEO 关键词调研报告
> SEMrush US | <date> | 来源：<出品方 / 域名>，<许可证>

## 模型理解（前置）

<2-4 句：模态 + 定位 + 出品方 + 差异化>

| 项目 | 内容 |
|------|------|
| 一句话定位 | 模态 + 定位 |
| 许可证 | Apache/MIT / 自定义 / 有地区限制 |
| 主仓库 / 分发 | GitHub（★）、HuggingFace、Ollama/ComfyUI |
| 参数 / VRAM 可跑性 | 尺寸/量化变体；消费级 / Olares One 能否跑 |
| 变体 / 型号 | 版本、尺寸、专项变体 |
| 闭源对标 | 替代哪个商业产品 |
| Olares Market | 已上架引擎（Ollama/ComfyUI/vLLM…）/ 未上架 |
| 来源 | 模型卡 / GitHub / 文档链接 |

---

## 流量基线（Phase 1）  ← 无官网则删除本节，抬头注明"无独立官网"

| 指标 | 数据 |
|------|------|
| 域名 | <domain> |
| SEMrush Rank | |
| 月自然流量（US） | |
| 关键词数 | |
| 流量估值 | $<n>/月 |

### 官网 TOP 关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | 流量 | URL |
|--------|------|------|----|------|-----|
| … | | | | | |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| … | | | | |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| | | | | | 主词候选 | |

---

## 核心洞见

1. 搜索心智是否建立（品牌/型号词有量还是全靠 HF/Ollama 直达）
2. 消费级 GPU / Olares One 能否本地跑（叙事前提）
3. 许可证是否商用友好（能否主推）
4. 对 Olares 最关键的 2-3 个词
5. 新模型 GEO 抢发窗口
6. 闭源对标与攻击面
7. 与 model/models.md 同类 family 及 model/keywords.md 的关联

---

*数据来源：SEMrush US（<列出实际用到的 report 名>）| <date>*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
```
