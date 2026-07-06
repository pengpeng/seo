# FreshRSS SEO 竞品分析报告

> 域名：freshrss.org | SEMrush US | 2026-07-06
> FreshRSS 是自托管 RSS / Atom 聚合器里社区认知最广的开源方案（GitHub ★15.4K），定位"你自己拥有的 Feedly"，品牌流量几乎等于官网全部流量，SEO 建设近乎空白，自托管信号词存在大量低 KD 空缺。

---

## 项目理解（前置）

FreshRSS 是免费、自托管的 RSS / Atom 订阅聚合器，PHP 编写，AGPL-3.0 许可，2012 年诞生，最新版 1.29.1（2026-05-20）。它定位于"你自己服务器上的 Feedly"——多用户、API 驱动（兼容 Fever / Google Reader 协议，支持 Reeder / NetNewsWire 等客户端）、可扩展（370 贡献者，Extension 生态含 LLM 分类 / Webhook）。1.29.0 新增 LLM 分类扩展（自动标签），是 AI 时代的 RSS 场景延伸。核心用户是想摆脱 Feedly/Inoreader 订阅费、保持数据私有的 RSS 重度用户与 homelab 爱好者。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自托管 RSS / Atom 聚合器，开源版 Feedly，完全由用户自己运行 |
| 开源 / 许可证 | 是，AGPL-3.0 |
| 主仓库 | https://github.com/FreshRSS/FreshRSS（★ 15.4K） |
| 核心功能 | 多用户聚合、Web 抓取生成 feed、WebSub 推送、Fever/GReader API 兼容、LLM 分类 & Webhook 扩展 |
| 商业模式 / 定价 | 完全免费自托管；无付费层；官方提供公开 demo（demo.freshrss.org） |
| 差异化 / 价值主张 | 轻量（低 PHP 依赖）、多用户、客户端生态成熟、扩展系统灵活；可跑 1M+ 文章 / 50k+ feed |
| 主要竞品（初判）| Miniflux（Go，极简）、Tiny Tiny RSS / tt-rss（PHP，功能更重）、Nextcloud News、Feedbin（托管） |
| Olares Market | 已上架 ⬜（待本报告后标 ✅） |
| 来源 | [freshrss.org](https://freshrss.org) · [GitHub](https://github.com/FreshRSS/FreshRSS) · [release 1.29.0](https://github.com/FreshRSS/FreshRSS/releases/tag/1.29.0) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | freshrss.org |
| SEMrush Rank | 943,774 |
| 自然关键词数 | 185 |
| 月自然流量（US）| 1,191 |
| 自然流量估值 | $12/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 3 词 |
| 排名 4-10 位 | 1 词 |
| 排名 11-20 位 | 19 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| freshrss.org（主域）| 184 | 1,191 | 100% |
| next.freshrss.org | 1 | 0 | ~0% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| freshrss | 1 | 1,300 | 51 | $0 | 1,040 | 导航 | /index.html |
| fresh rss | 1 | 170 | 36 | $0 | 136 | 导航 | /index.html |
| rss feed reader | 32 | 6,600 | 77 | $2.31 | 4 | 信息 | /index.html |
| feed aggregator | 9 | 260 | 85 | $1.82 | 2 | 商业 | /index.html |
| rss aggregator software | 11 | 320 | 72 | $0 | 1 | 信息 | /index.html |
| freshrss docker | 3 | 70 | 48 | $0 | 1 | 商业/导航 | /index.html |
| self hosted rss | 12 | 50 | 27 | $0 | 0 | 信息 | /index.html |
| self host rss | 12 | 50 | 24 | $0 | 0 | 信息 | /index.html |
| self hosted rss feed reader | 13 | 70 | 28 | $0 | 0 | 商业 | /index.html |
| rss reader open source | 25 | 70 | 23 | $0 | 0 | 信息 | /index.html |
| online rss feed aggregator | 29 | 140 | 73 | $0 | 0 | 信息 | /index.html |
| tiny tiny rss | 59 | 480 | 43 | $0 | 0 | 信息 | /index.html |
| rss creator | 30 | 590 | 25 | $3.28 | 0 | 商业 | /index.html |
| free rss reader | 32+ | 320 | 53 | $0 | 0 | 信息 | /index.html |
| rss aggregator | 32+ | 390 | 86 | $2.56 | 0 | 商业 | /index.html |

> 观察：全站 185 个关键词均落在同一个 URL（/index.html），无任何内容专题页；品牌词（freshrss + fresh rss）贡献了 1,176/1,191（99%）流量——非品牌词几乎零转化。`rss feed reader`（6,600/月）排名 32，流量仅 4，说明首页权重不足。

### 付费词（Google Ads）

FreshRSS 未投放任何付费广告，纯社区口碑驱动，无付费流量。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| inoreader | 4,400 | 55 | $0 | 导航 | 付费竞品大词，KD 高，难正面刚 |
| newsblur | 880 | 52 | $4.06 | 导航 | 付费竞品，CPC 高说明商业价值 |
| miniflux | 720 | 38 | $0 | 导航 | 开源竞品，KD 温和，用户群重叠 |
| tiny tiny rss | 480 | 43 | $0 | 信息 | 开源竞品，技术受众 |
| ttrss | 480 | 45 | $0 | 导航 | tt-rss 品牌变体 |
| free rss reader | 320 | 53 | $0 | 信息 | 价格敏感用户入口 |
| tt rss | 320 | 0 | $0 | 信息 | KD 极低变体 ⭐ |
| feedly vs inoreader | 170 | 16 | $0 | 信息/商业 | ⭐ KD 仅 16，比较意图，机会词 |
| inoreader vs feedly | 170 | 19 | $0 | 信息/商业 | ⭐ 同上变体 |
| feedly alternative | 140 | 23 | $0 | 信息 | ⭐ 核心攻击词，付费痛点 |
| freshrss alternative | 20 | 0 | $0 | — | ⭐ GEO 前哨 |
| miniflux alternative | 20 | 0 | $0 | — | ⭐ GEO 前哨 |
| tiny tiny rss alternative | 20 | 0 | $0 | — | ⭐ GEO 前哨 |
| google reader alternative | 20 | 0 | $0 | — | ⭐ GEO 前哨（历史词，长尾存活） |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| what is an rss reader | 49,500 | 65 | $0 | 信息 | 教育词巨量，KD 偏高，适合长文铺垫 |
| rss reader | 6,600 | 70 | $2.79 | 信息 | 品类大词，竞争激烈 |
| rss feed reader | 6,600 | 62 | $2.31 | 信息 | FreshRSS 排名 32 但零转化 |
| feed reader | 2,900 | 76 | $2.79 | 信息/商业 | 高 KD |
| rss app | 1,000 | 63 | $0.28 | 导航 | 移动端品类入口 |
| best rss reader | 590 | 50 | $1.84 | 信息 | 商业调查词，列表文 |
| rss reader app | 590 | 64 | $0 | 信息 | 移动端导向 |
| rss viewer | 390 | 31 | $0 | 信息 | KD 温和，被低估入口词 |
| rss aggregators | 480 | 84 | $2.56 | 信息 | KD 高 |
| web rss reader | 260 | 43 | $0 | 信息 | 网页端导向 |
| free rss reader website | 170 | 35 | $0 | 信息 | 可攻 |
| open source rss reader | 140 | 27 | $0 | 信息 | ⭐ 核心机会词 |
| open source rss feed reader | 140 | 25 | $0 | 信息 | ⭐ 同族变体 |
| feedly alternative open source | 20 | 0 | $0 | — | ⭐ GEO 前哨 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| freshrss | 1,300 | 51 | $0 | 导航 | 品牌主词，官网第 1 位 |
| fresh rss | 170–390 | 35–36 | $0 | 导航 | 拼写变体，官网第 1 位 |
| freshrss docker | 70 | 48 | $0 | 商业/导航 | 部署意图，排名第 3 |
| freshrss vs miniflux | 20 | 0 | $0 | — | GEO 比较前哨 ⭐ |
| freshrss raspberry pi | 20 | 0 | $0 | — | ARM 部署场景前哨 ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted rss reader | 90 | 25 | $0 | 商业 | ⭐ 核心机会词，商业意图 + 低 KD |
| self hosted rss feed reader | 70 | 28 | $0 | 商业 | ⭐ 同族 |
| self hosted rss | 70 | 30 | $0 | 信息 | ⭐ 边界词，入口 |
| self hosted feed reader | 70 | 29 | $0 | 信息 | ⭐ 同族 |
| self host rss | 50 | 24 | $0 | 信息 | ⭐ KD 极低变体 |
| rss reader open source | 70 | 23 | $0 | 信息 | ⭐ KD 23，最低竞争度开源词 |
| open source rss reader | 140 | 27 | $0 | 信息 | ⭐ 同族，量最大 |
| rss reader self hosted | 20 | 0 | $0 | — | ⭐ GEO 前哨 |
| rss self hosted | 20 | 0 | $0 | — | ⭐ GEO 前哨 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：FreshRSS 已上架 Olares Market，Olares 可以"一键部署你自己的 RSS 聚合器"切入自托管 RSS 读者圈，以隐私 + 零订阅费 + Agent 上下文统一管理为差异化叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| open source rss reader | 140 | 27 | $0 | FreshRSS 在 Olares Market，一键部署；Olares 提供持久存储 + 远程访问，"开源 RSS 阅读器的最佳 OS 底座" | ⭐⭐⭐ |
| feedly alternative | 140 | 23 | $0 | Feedly Pro $12/月 → 用 Olares 自托管 FreshRSS，永久免费，"Stop renting your feeds" | ⭐⭐⭐ |
| feedly vs inoreader | 170 | 16 | $0 | 两者都是闭源付费 → 对比文结尾推"第三选项：FreshRSS on Olares"；KD 极低 16 | ⭐⭐⭐ |
| self hosted rss reader | 90 | 25 | $0 | 商业意图 + KD 25；Olares 提供最低运维自托管体验，Market 一键装 FreshRSS | ⭐⭐⭐ |
| self hosted rss | 70 | 30 | $0 | Olares = 运行 self-hosted app 的个人云 OS；FreshRSS 是典型案例 | ⭐⭐⭐ |
| rss reader open source | 70 | 23 | $0 | Olares Market 开源 RSS 场景的直接入口词，KD 23 最易落地 | ⭐⭐⭐ |
| freshrss docker | 70 | 48 | $0 | Olares 封装了容器部署，无需手动管理 Docker；对比"手动 docker-compose" | ⭐⭐ |
| miniflux alternative | 20 | 0 | $0 | Miniflux 需 Go 环境；FreshRSS on Olares 更易部署，Olares 两个都能跑 | ⭐⭐ |
| freshrss vs miniflux | 20 | 0 | $0 | GEO 前哨：Olares Market 两者皆有，方便迁移对比 | ⭐⭐ |
| freshrss raspberry pi | 20 | 0 | $0 | Olares 支持 ARM（Raspberry Pi 4/5 via script），低功耗 homelab 场景 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| open source rss reader | 140 | 27 | $0 | 信息 | 主词候选 | KD 27 + 商业调查意图，自托管受众精准；Olares Market 直接入口，"open source RSS reader you self-host in one click" |
| feedly alternative | 140 | 23 | $0 | 信息 | 主词候选 | Feedly 付费痛点词，KD 23；FreshRSS on Olares = 开源替代 + 无运维，付费转开源的最强入口 |
| feedly vs inoreader | 170 | 16 | $0 | 信息/商业 | 主词候选 | KD 仅 16，月量 170；对比文结尾推"两者都是闭源订阅制，试试自托管 FreshRSS on Olares" |
| self hosted rss reader | 90 | 25 | $0 | 商业 | 主词候选 | 商业意图 + KD 25，转化最精准；Olares Market 一键安装是最直接的答案 |
| self hosted rss | 70 | 30 | $0 | 信息 | 次级 | 并入"self hosted rss reader"族；KD 30 边界值，作为 H2 优化 |
| self hosted rss feed reader | 70 | 28 | $0 | 商业 | 次级 | 同族并入主词文章，KD 28 |
| rss reader open source | 70 | 23 | $0 | 信息 | 次级 | KD 23 最低，并入"open source rss reader"族 |
| self host rss | 50 | 24 | $0 | 信息 | 次级 | KD 24 极低变体，并入 self-hosted 族 |
| self hosted feed reader | 70 | 29 | $0 | 信息 | 次级 | 并入 self-hosted 族 |
| rss viewer | 390 | 31 | $0 | 信息 | 次级 | 量 390 在低 KD 词里偏大，可并入品类文作为 H2 |
| freshrss | 1,300 | 51 | $0 | 导航 | 次级 | 品牌大词排不动（KD 51 + 导航意图），适合 Olares Market 页标题优化 |
| freshrss docker | 70 | 48 | $0 | 商业/导航 | 次级 | 部署意图，Olares 容器化教程 / Market 页可攻 |
| miniflux alternative | 20 | 0 | $0 | — | GEO | 近零量但意图精准；FAQ 段或结构化数据抢 AI Overview 引用位 |
| freshrss alternative | 20 | 0 | $0 | — | GEO | 同上，绑 FreshRSS 品牌做垂直覆盖 |
| freshrss vs miniflux | 20 | 0 | $0 | — | GEO | Olares Market 两个都有，写对比段 |
| freshrss raspberry pi | 20 | 0 | $0 | — | GEO | Olares ARM（Pi 4/5）+ FreshRSS，低功耗 homelab 组合场景 |
| rss reader self hosted | 20 | 0 | $0 | — | GEO | 同族前哨，确保覆盖所有拼法变体 |

---

## 核心洞见

1. **品牌护城河**：freshrss.org 月流量 1,191，其中 99%（1,176）来自品牌词（`freshrss` + `fresh rss`）。全站无任何内容专题页，所有排名均落在同一个 URL，护城河极薄，几乎没有 SEO 基础设施。**无需正面刚品牌词**——绕行非品牌词（自托管/开源信号词）胜算更大，且 FreshRSS 官网自己也没有占位。

2. **可复制的打法**：竞品 selfh.st（自托管应用目录）以 8 个公共关键词积累了 1,318 月流量，比 FreshRSS 官网还多——靠的是"按应用品类的专题页"而非品牌。可复制路径：① 写"self hosted rss reader"攻略页（KD 低、商业意图）；② "feedly vs inoreader + 开源 self-hosted 替代"对比文（KD 极低）；③ Olares Market 详情页 + 部署教程（覆盖 `freshrss docker`、`freshrss raspberry pi`）。

3. **对 Olares 最关键的词**：
   - `feedly vs inoreader`（170/月，KD 16）——KD 最低机会词，对比文结尾推 FreshRSS on Olares
   - `open source rss reader`（140/月，KD 27）——Olares Market 开源 RSS 直接入口
   - `self hosted rss reader`（90/月，KD 25）——商业意图最精准，转化最高

4. **最大攻击面**：Feedly Pro $12/月 / Inoreader $9.99/月 订阅制是核心痛点。`feedly alternative`（KD 23）和 `feedly vs inoreader`（KD 16）反映用户正在主动寻找替代——FreshRSS 官网没有相关落地页，这是正在漏流量的空白，Olares 可以直接占位。

5. **隐藏低 KD 金矿**：
   - `rss viewer`（390/月，KD 31）——在 self-hosted RSS 词里量级属于中上，KD 仅 31，是被低估的品类入口词
   - `rss reader open source`（70/月，KD 23）——最低竞争度开源词变体
   - `self host rss`（50/月，KD 24）——KD 24 极低，量小但精准
   - `inoreader vs feedly`（170/月，KD 19）——同 `feedly vs inoreader` 一样的低 KD 金矿

6. **GEO 前瞻布局**：`freshrss alternative`、`miniflux alternative`、`tt-rss alternative`、`freshrss vs miniflux`、`freshrss raspberry pi`、`feedly alternative open source` 均近零量但意图精准——在对比文/FAQ 段提前埋入，可抢 AI Overview / Perplexity 引用位，覆盖所有开源 RSS 比较场景。

7. **与既有分析的关联**：olares-500-keywords 词表中未见 `feedly alternative`（KD 23）或 `self hosted rss reader`（KD 25）这类低 KD 精准词。FreshRSS 报告新增了"自托管 RSS 阅读器"词脉，适合与未来 Miniflux、Tiny Tiny RSS 报告合并成跨报告的 **"self-hosted RSS reader"内容簇**（Olares Market 三个开源 RSS 应用的联合叙事）。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
