# Google Analytics SEO 竞品分析报告

> 域名：analytics.google.com（谷歌子域名，无独立 SEO 数据，已降级为关键词层面分析）| SEMrush US | 2026-07-06
> Google Analytics（GA4）是全球市占率最高（~81%）的网站分析平台，免费+企业版双轨，GDPR 合规争议是其最大公关弱点。

---

## 项目理解（前置）

Google Analytics 4（GA4）是 Google 推出的第四代网站与 App 分析平台，于 2023 年 7 月强制替换 Universal Analytics。它采用基于事件（event-based）的数据模型，与 Google Ads、Search Console、BigQuery 深度集成，是当前 Web 分析类工具的绝对市场领导者（W3Techs 数据：在所有可识别分析工具中市占率约 81.4%，2026 年 6 月）。

标准版完全免费，企业版（Analytics 360）起步价约 $50,000/年。其最大争议是 GDPR 合规性——奥地利（2022.01）、法国（2022.02）、意大利（2022.06）数据保护局均曾裁定 Universal Analytics 违反 GDPR；GA4 依赖 Consent Mode 和 EU-US 数据隐私框架维持合法性，仍被视为隐私合规的高风险选项。这一背景直接催生了 Plausible、Umami、Matomo 等隐私友好型分析工具的崛起。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 全球最大网站分析平台（免费+GA360），深度绑定 Google 广告生态 |
| 开源 / 许可证 | 闭源，Google 自有产品 |
| 主仓库 | 无公开 GitHub 仓库 |
| 核心功能 | 事件追踪、受众分析、转化漏斗、BigQuery 原始数据导出、Google Ads 归因、Consent Mode v2 |
| 商业模式 / 定价 | 标准版免费；Analytics 360 $12,500/月起（约 $50K–$200K+/年），通过 GMP 经销商购买 |
| 差异化 / 价值主张 | 免费 + Google Ads 最深归因集成；BigQuery 免费导出；AI 预测受众 |
| 主要竞品（初判）| Plausible、Matomo、Umami、Fathom Analytics、Microsoft Clarity |
| Olares Market | 未上架（商业闭源）；Olares 平替：Plausible（已知可部署）、Umami（已知可部署） |
| 来源 | [analytics.google.com](https://analytics.google.com)、[GA4 官方文档](https://support.google.com/analytics/answer/11202874)、[W3Techs 市占率 2026-06](https://w3techs.com/technologies/comparison/ta-googleanalytics,ta-matomo,ta-plausible)、[SaaSCompared 评测](https://saascompared.com/product/google-analytics) |

---

## 流量基线（Phase 1）

### 概览

analytics.google.com 是纯 Web App 入口（需登录），Semrush 无独立有机关键词数据。google.com 主域有机排名约 5,500 万关键词、月流量 5.54 亿，但 analytics 子域不参与有机搜索竞争。**本报告以关键词层面分析为主**。

| 指标 | 数据 |
|------|------|
| 目标域名 | analytics.google.com（谷歌子域名） |
| Semrush 自然关键词 | 无独立数据（降级关键词层面） |
| analytics.google.com 月流量 | 无 SEO 数据（纯 App 登录页） |
| google.com 主域 Semrush Rank | #1 全球 |
| Plausible.io 对照 | Rank #102,308；自然词 1,929；月流量 ~18,892；排名 1-3 共 187 词 |
| Umami.is 对照 | Rank #1,734,063；自然词 223；月流量 ~455 |
| 数据说明 | GA 自身不做内容 SEO；关键词竞争发生在第三方比较/评测内容层 |

### 竞品生态对照（Plausible.io TOP 自然词节选）

> 注：此处展示 Plausible.io 的有机排名，是理解 GA alternative 词系竞争格局的关键参照。

| 关键词 | 排名 | 月量 | KD | 流量贡献 | URL |
|--------|------|------|----|---------|----|
| plausible | 1 | 49,500 | 59 | 1,287 | plausible.io/ |
| plausible analytics | 1 | 1,300 | 41 | 1,040 | plausible.io/ |
| simple analytics | 4 | 40,500 | 46 | 324 | plausible.io/ |
| google analytics alternative | **2** | **1,600** | **21** | 131 | plausible.io/ |
| plausible analytics pricing | 1 | 110 | 23 | 88 | plausible.io/docs/subscription-plans |
| analytics websites | 1 | 320 | 89 | 79 | plausible.io/ |

*Plausible 仅凭 ~1,929 个自然词、18,892 月流量，就在 KD=21 的 `google analytics alternative` 词上拿到第 2 位——证明该词完全可攻。*

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google analytics alternative | 1,600 | 21 | $10.48 | 信息/商业 | ⭐ 核心攻击词，竞争最弱的大词 |
| google analytics alternatives | 1,300 | 22 | $9.64 | 信息/商业 | ⭐ 同族变体，合计量 ~2,900 |
| plausible vs umami | 880 | 12 | $0 | 信息/商业 | ⭐ KD 极低，Olares 两者都托管 |
| alternatives to google analytics | 260 | 25 | $8.53 | 信息 | ⭐ 同族 |
| google analytics competitors | 320 | 20 | $12.62 | 信息 | ⭐ 评测/对比意图 |
| best web analytics tools | 260 | 23 | $17.97 | 商业 | ⭐ 高 CPC，商业意图强 |
| matomo vs google analytics | 170 | 34 | $11.05 | 信息 | 稍高 KD |
| alternative google analytics | 170 | 20 | $9.64 | 信息/商业 | ⭐ 同族变体 |
| best google analytics alternative | 50 | 17 | $8.51 | 商业 | ⭐ KD 极低强商业 |
| ga4 alternative | 40 | **5** | $12.26 | 商业 | ⭐ **KD=5 最低竞争高意图词** |
| google analytics 4 alternatives | 40 | 15 | $0 | 信息/商业 | ⭐ |
| alternatives to google analytics 4 | 30 | 15 | $14.91 | 信息 | ⭐ |
| free google analytics alternative | 70 | 27 | $5.23 | 信息/商业 | ⭐ |
| open source alternatives to google analytics | 40 | 31 | $6.54 | 商业 | 自托管意图 |
| google analytics 4 attribution vs alternatives | 40 | 0 | $0 | 信息 | ⭐ 长尾 |
| google analytics alternatives free | 50 | 23 | $5.23 | 信息/商业 | ⭐ |
| google analytics vs alternatives 2026 | 170 | 0 | $0 | 信息 | ⭐ 时效性词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| website analytics | 3,600 | 76 | $9.31 | 信息 | KD 高，品类大词 |
| web analytics tools | 1,600 | 91 | $13.72 | 信息 | KD 极高 |
| web analytics dashboard | 390 | 28 | $9.54 | 信息 | ⭐ 低 KD 品类词 |
| analytics dashboard | 1,000 | 32 | $11.19 | 信息 | 可攻 |
| analytics tool for website | 320 | 67 | $13.72 | 信息 | KD 高 |
| free web analytics | 390 | 39 | $5.58 | 商业 | 中等 |
| cookieless analytics | 110 | 26 | $16.63 | 信息/商业 | ⭐ 高 CPC，隐私角度 |
| gdpr compliant analytics | 140 | 30 | $12.85 | 信息/商业 | ⭐ GDPR 合规角度 |
| privacy analytics | 140 | 26 | $3.58 | 商业 | ⭐ 隐私意图强 |
| website traffic analytics | 1,300 | 73 | $5.48 | 商业 | KD 高 |
| simple web analytics | 260 | 37 | $8.06 | 商业 | 中等，Plausible/Umami 卖点 |
| best web analytics | 110 | 38 | $11.12 | 商业 | 中等 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google analytics | 301,000 | 96 | $6.24 | 信息/导航 | 品牌防守词，不可攻 |
| ga4 | 18,100 | 100 | $5.96 | 导航 | 纯品牌词 |
| google analytics 4 | 8,100 | 100 | $5.46 | 导航/信息 | 纯品牌词 |
| google analytics gdpr | 260 | 36 | $13.34 | 信息 | ⭐ 痛点词，可攻 |
| google analytics privacy | 70 | 30 | $0 | 信息 | ⭐ 痛点词 |
| google analytics tutorial | 390 | 81 | $3.82 | 信息 | KD 高 |
| google analytics data | 170 | 97 | $5.10 | 信息 | KD 极高 |
| google analytics data retention | 30 | 0 | $0 | 信息 | ⭐ 痛点词（免费版仅 14 月） |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| plausible | 40,500 | 57 | $9.94 | 商业 | 竞品主词，量巨大 |
| plausible analytics | 1,300 | 41 | $9.67 | 商业 | 竞品次级词 |
| umami analytics | 720 | 26 | $8.99 | 商业 | ⭐ Olares 直接机会词 |
| matomo analytics | 720 | 21 | $6.30 | 商业 | ⭐ 可部署替代 |
| fathom analytics | 1,000 | 52 | $9.12 | 商业 | 闭源，不适合 Olares |
| open source analytics | 170 | 66 | $10.69 | 信息 | KD 偏高 |
| open source web analytics | 90 | 68 | $4.04 | 信息 | KD 高 |
| self hosted analytics | 40 | 52 | $3.60 | 信息 | KD 中等 |
| self hosted web analytics | 20 | 0 | $5.86 | — | ⭐ KD=0 |
| hipaa analytics | 30 | 13 | $6.59 | 信息/商业 | ⭐ 合规场景低 KD |
| plausible docker | 20 | 0 | $0 | 信息 | ⭐ 安装教程词 |
| umami docker | 20 | 0 | $0 | 信息 | ⭐ 安装教程词 |
| google analytics blocked by adblock | 20 | 0 | $0 | 信息 | ⭐ GA 痛点，自托管解法 |
| analytics without cookies | 30 | 0 | $0 | 信息 | ⭐ 隐私切入 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Olares 同时内置 Plausible 和 Umami 两款开源分析工具，用户无需自行配置 Docker 栈，一键部署即得隐私友好的 Google Analytics 替代方案——这在"plausible vs umami 哪个好"类词上有天然落地 URL。**

按月量降序。⭐⭐⭐ / ⭐⭐ / ⭐ 标契合度。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-------------|
| google analytics alternative | 1,600 | 21 | $10.48 | ⭐⭐⭐ 落地页：「在 Olares 一键部署 Plausible/Umami 替代 GA」；Plausible 已排名第 2 |
| google analytics alternatives | 1,300 | 22 | $9.64 | ⭐⭐⭐ 同族，纳入同一文章 |
| plausible vs umami | 880 | 12 | $0 | ⭐⭐⭐ **最佳攻击点**：Olares 同时托管两者，可写部署+对比指南 |
| umami analytics | 720 | 26 | $8.99 | ⭐⭐⭐ Olares Market 直接上架词 |
| matomo analytics | 720 | 21 | $6.30 | ⭐⭐ Matomo 可自托管，Olares 可部署 |
| alternatives to google analytics | 260 | 25 | $8.53 | ⭐⭐⭐ 同族替代词 |
| best web analytics tools | 260 | 23 | $17.97 | ⭐⭐ 高 CPC，Olares 可作为「拥有自己的分析工具」叙事 |
| google analytics gdpr | 260 | 36 | $13.34 | ⭐⭐ GDPR 痛点 → Plausible/Umami 天然无 Cookie，无需同意横幅 |
| gdpr compliant analytics | 140 | 30 | $12.85 | ⭐⭐ Plausible/Umami 默认无 Cookie，合规成本为零 |
| privacy analytics | 140 | 26 | $3.58 | ⭐⭐ Olares 隐私主线叙事 |
| cookieless analytics | 110 | 26 | $16.63 | ⭐⭐ Plausible/Umami 均无 Cookie，高 CPC 商业意图 |
| best google analytics alternative | 50 | 17 | $8.51 | ⭐⭐⭐ KD=17，「自托管版 best alternative」= Olares |
| ga4 alternative | 40 | **5** | $12.26 | ⭐⭐⭐ **KD=5 惊人低竞争**，「GA4 搞不懂？Olares 一键换 Plausible」 |
| hipaa analytics | 30 | 13 | $6.59 | ⭐⭐ 医疗合规场景，自托管是唯一解 |
| google analytics privacy | 70 | 30 | $0 | ⭐⭐ GA 隐私争议 → 自托管替代叙事 |
| google analytics blocked by adblock | 20 | 0 | $0 | ⭐⭐ 广告拦截器屏蔽 GA → 自托管绕过 adblocker |
| plausible docker | 20 | 0 | $0 | ⭐ Olares 原生一键安装，比手动 Docker 简单 |
| umami docker | 20 | 0 | $0 | ⭐ 同上 |
| self hosted web analytics | 20 | 0 | $5.86 | ⭐⭐ KD=0，精准安装意图 |
| google analytics vs plausible | 20 | 0 | $8.23 | ⭐⭐ 精准对比词，GEO 前瞻 |
| self hosted google analytics alternative | 20 | 0 | $0 | ⭐⭐⭐ 语义最精准，抢 AI Overview 引用位 |
| analytics without cookies | 30 | 0 | $0 | ⭐⭐ GEO 词，隐私角度 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| google analytics alternative | 1,600 | 21 | $10.48 | 信息/商业 | **主词候选** | 核心攻击词，KD=21 可攻，Plausible.io 仅凭 1929 个词就拿到排名 #2；Olares 落地：「一键部署 Plausible/Umami 替代 GA」 |
| google analytics alternatives | 1,300 | 22 | $9.64 | 信息/商业 | **主词候选** | 与上词合计约 2,900 月量，合并主词簇 |
| plausible vs umami | 880 | 12 | $0 | 信息/商业 | **主词候选** | KD=12 全集最低大词，Olares 同时托管两者，可写深度对比+部署指南 |
| umami analytics | 720 | 26 | $8.99 | 商业 | **主词候选** | Olares Market 直接产品词，KD<30 可攻 |
| matomo analytics | 720 | 21 | $6.30 | 商业 | **主词候选** | 开源 GA 替代，KD=21，Olares 可部署 |
| alternatives to google analytics | 260 | 25 | $8.53 | 信息 | 次级 | 并入 alternative 主文，补充长尾 |
| google analytics competitors | 320 | 20 | $12.62 | 信息 | 次级 | 评测意图，并入对比文章 |
| best web analytics tools | 260 | 23 | $17.97 | 商业 | 次级 | 高 CPC，作为对比文章副词 |
| gdpr compliant analytics | 140 | 30 | $12.85 | 信息/商业 | 次级 | GDPR 角度，并入 privacy analytics 文章 |
| cookieless analytics | 110 | 26 | $16.63 | 信息/商业 | 次级 | 高 CPC，并入隐私/cookieless 文章 |
| google analytics gdpr | 260 | 36 | $13.34 | 信息 | 次级 | GA 痛点词，引出自托管替代叙事 |
| best google analytics alternative | 50 | 17 | $8.51 | 商业 | 次级 | 强商业意图 + KD=17，纳入 alternative 文章 |
| ga4 alternative | 40 | **5** | $12.26 | 商业 | 次级 | KD=5 异常低，高 CPC，纳入 ga4 替代词段 |
| privacy analytics | 140 | 26 | $3.58 | 商业 | 次级 | 隐私叙事核心词 |
| hipaa analytics | 30 | 13 | $6.59 | 信息/商业 | 次级 | 医疗合规场景，自托管唯一解 |
| google analytics privacy | 70 | 30 | $0 | 信息 | 次级 | GA 痛点，引导隐私替代 |
| web analytics dashboard | 390 | 28 | $9.54 | 信息 | 次级 | ⭐ 品类词中 KD 最低，并入品类文章 |
| self hosted web analytics | 20 | 0 | $5.86 | 导航 | **GEO** | KD=0，精准安装意图，抢 AI Overview 引用位 |
| google analytics vs plausible | 20 | 0 | $8.23 | 信息/商业 | **GEO** | 精准对比词，FAQ 段落 |
| self hosted google analytics alternative | 20 | 0 | $0 | 信息 | **GEO** | 语义最精准，AI 搜索引用 |
| google analytics blocked by adblock | 20 | 0 | $0 | 信息 | **GEO** | 痛点词，自托管绕过 adblocker 角度 |
| analytics without cookies | 30 | 0 | $0 | 信息 | **GEO** | 隐私叙事，AI Overview 前瞻 |
| plausible docker | 20 | 0 | $0 | 信息 | **GEO** | Olares 安装词，FAQ「在 Olares 上部署 Plausible」 |
| umami docker | 20 | 0 | $0 | 信息 | **GEO** | 同上 |

---

## 核心洞见

1. **品牌护城河**：`google analytics`（301K/mo，KD 96）、`ga4`（18K，KD 100）是坚不可摧的品牌防守词——正面刚品牌词无意义。真正的攻击面在「alternative / 替代 / GDPR / 隐私」词系，KD 均在 15-30，Plausible.io 以极小规模的网站已验证可拿到 #2 排名，Olares 有充分条件复制。

2. **可复制的打法**：Plausible.io 的核心打法是 **内容 + 功能对比页**——以 `/blog/backlinks-seo-guide`（SEO 教程）撬动大量流量，同时主页 `/` 直接排在 `google analytics alternative` 第 2 位。值得学习：用一两篇高质量深度指南（「Plausible vs Umami 深度对比」「如何在不使用 Google Analytics 的情况下追踪网站流量」）切入 KD<25 的词，带出自托管部署教程，再链向 Olares Market。

3. **对 Olares 最关键的 3 个词**：
   - `plausible vs umami`（880/mo，KD 12）——Olares 同时托管两者，天然有资格写这篇对比，竞争最小
   - `google analytics alternative`（1,600/mo，KD 21）——流量最大的可攻词，Olares 一键部署叙事的主入口
   - `ga4 alternative`（40/mo，KD **5**）——KD=5 全集最惊人，$12.26 CPC 说明商业价值极高，极易抢到排名

4. **最大攻击面**：GA 的三大痛点词——**GDPR 合规**（`google analytics gdpr` 260/mo，KD 36；`gdpr compliant analytics` 140/mo，KD 30），**数据隐私**（免费版 14 个月数据留存限制），**广告拦截器**（`google analytics blocked by adblock`，KD 0）——均对应「自托管 + 无 Cookie」的 Plausible/Umami 解决方案。这是 Olares 的天然进攻弹药。

5. **隐藏低 KD 金矿**：
   - `ga4 alternative`（KD=5，$12.26 CPC）——商业意图最强的词中 KD 最低
   - `plausible vs umami`（KD=12，880/mo）——有量有意图，对比词中最无防守
   - `hipaa analytics`（KD=13）——医疗合规场景，自托管是唯一解，完全无竞争
   - `best google analytics alternative`（KD=17）——「best」限定词降低了竞争
   - `google analytics 4 alternatives`（KD=15）、`alternatives to google analytics 4`（KD=15）

6. **GEO 前瞻布局**：以下近零量词适合写入 FAQ 段落以抢 AI Overview / Perplexity 引用位：
   - `self hosted google analytics alternative`（精准描述 Plausible/Umami on Olares）
   - `google analytics vs plausible`（对比 FAQ）
   - `analytics without cookies`（隐私合规前瞻）
   - `google analytics blocked by adblock`（痛点 → 自托管解法）
   - `plausible docker` / `umami docker`（安装教程词）

7. **与既有分析的关联**：olares-500-keywords-analysis 中未包含 web analytics 类词汇，本报告是新增词系。`privacy`（隐私）叙事与 Olares 整体品牌方向高度吻合（Olares 官方定位含隐私数据自主），`google analytics alternative` 词系可与 [privacy/reports/](/Users/pengpeng/seo/directions/privacy/reports) 中的隐私分析方向联动，形成「隐私优先 + 自托管 + Olares 一键部署」的内容矩阵。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*analytics.google.com 为纯 Web App 子域名，Semrush 无自然关键词数据，已按 Skill 规则降级为关键词层面分析；W3Techs 市占率数据截至 2026 年 6 月 25 日。*
