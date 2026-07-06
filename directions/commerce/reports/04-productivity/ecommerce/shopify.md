# Shopify SEO 竞品分析报告

> 域名：shopify.com | SEMrush US | 2026-07-06
> 全球最大电商 SaaS 平台，市值 ~$155B，占检测电商平台市场 46% 份额；闭源、按月收费、抽取交易费，开源替代切入口清晰。

---

## 项目理解（前置）

Shopify 是 2006 年创立于加拿大的全托管电商 SaaS 平台，现已成为全球市场份额第一的电商软件（按检测域名数 46%，美国约 29%），TTM 营收 $11.56B（+30.6% YoY），市值约 $155B（2026 年 4 月）。平台从建店到支付、POS、营销自动化全打通，并于 2026 年 3 月全面开放 Agentic Storefronts，将 AI agent 购物接入每家 Shopify 商店。商业模式基于月度订阅费 + 交易抽成 + App Store 分成，锁定效应极强——迁移成本高、数据在 Shopify 云端、平台 API 深度绑定。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 全托管电商 SaaS：建店 + 支付 + 营销 + POS 一站式，零基础可上线 |
| 开源 / 许可证 | 闭源 SaaS；部分工具（Polaris、Liquid 等）开源 |
| 主仓库 | 无开源核心（Shopify/shopify 为私有仓库）|
| 核心功能 | 在线商店建站、Shopify Payments、Shopify POS、App Store（10,000+ 应用）、多渠道销售（TikTok/Amazon/社媒）、Shopify Plus 企业级功能 |
| 商业模式 / 定价 | Starter $5/月 → Basic $39 → Grow $105 → Advanced $399 → Plus $2,300+/月；在线刷卡费 2.9%+30¢ ~ 2.15%+30¢；使用第三方支付额外收 0.5%~2% |
| 差异化 / 价值主张 | 极低上手门槛、生态最完整（App Store + 主题市场）、支付与物流高度整合、多渠道统一后台 |
| 主要竞品（初判）| WooCommerce（自托管 WordPress 插件，#2 by share）、BigCommerce（中端企业级）、Adobe Commerce/Magento（企业定制）、Squarespace（创意品牌）；开源替代：**Medusa**（MIT，TS/Node，34K★）、**Saleor**（BSD-3，Python/Django，22.9K★）|
| Olares Market | Shopify 本身未上架（闭源）；**Medusa** 已上架 ✅ [(报告)](directions/market/reports/medusa.md) |
| 来源 | [shopify.com/pricing](https://www.shopify.com/pricing)、[PitchGrade 2026](https://pitchgrade.com/companies/shopify)、[TechnologyChecker 2026](https://technologychecker.io/blog/shopify-analytics-trends-insights)、[GitHub: medusajs/medusa](https://github.com/medusajs/medusa)、[GitHub: saleor/saleor](https://github.com/saleor/saleor) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | shopify.com |
| SEMrush Rank | 1,062（全球极顶级）|
| 自然关键词数 | 714,499 |
| 月自然流量（US）| 2,520,098 |
| 自然流量估值 | $10,234,501/月 |
| 付费关键词数 | 13,932 |
| 月付费流量 | 645,914 |
| 付费流量估值 | $1,968,302/月 |
| 排名 1-3 位 | 26,723 词 |
| 排名 4-10 位 | 64,025 词 |
| 排名 11-20 位 | 108,288 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.shopify.com | 459,217 | 1,804,711 | 71.61% |
| help.shopify.com | 59,737 | 316,491 | 12.56% |
| apps.shopify.com | 87,210 | 214,413 | 8.51% |
| community.shopify.com | 93,793 | 62,492 | 2.48% |
| themes.shopify.com | 6,092 | 62,441 | 2.48% |
| hardware.shopify.com | 1,864 | 16,554 | 0.66% |
| partners.shopify.com | 30 | 12,621 | 0.50% |
| changelog.shopify.com | 2,050 | 7,074 | 0.28% |
| polaris-react.shopify.com | 761 | 6,733 | 0.27% |
| collabs.shopify.com | 71 | 6,079 | 0.24% |

> **洞察**：www 主站吞 71.6% 流量，help 子域贡献 12.6%（搜索量极高的功能/操作类词，极难被外部竞争），apps 子域 8.5% 说明 App Store 生态词是重要流量入口（`autoblogger`、`pirate ship` 等 App 名也借 apps.shopify.com 排名）。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| shopify | 1 | 1,000,000 | 100 | $4.42 | 800,000 | 导航 | shopify.com/ |
| shopify login | 1 | 201,000 | 78 | $1.78 | 160,800 | 导航/交易 | store-login |
| dropshipping | 2 | 673,000 | 70 | $3.95 | 16,152 | 信息 | help/dropshipping |
| shopify customer service number | 1 | 18,100 | 49 | $2.49 | 14,480 | 导航 | contact |
| shopify admin | 1 | 14,800 | 66 | $6.69 | 11,840 | 导航/交易 | help/shopify-admin |
| shopify partner | 1 | 14,800 | 32 | $9.22 | 11,840 | 导航 | partners |
| shopify log in | 1 | 14,800 | 76 | $1.78 | 11,840 | 导航/交易 | store-login |
| shopify app store | 1 | 14,800 | 54 | $1.17 | 11,840 | 导航 | apps.shopify.com |
| shopify careers | 1 | 12,100 | 41 | $1.32 | 9,680 | 信息/导航 | careers |
| shopify themes | 1 | 9,900 | 39 | $2.73 | 7,920 | 信息/导航 | themes.shopify.com |
| shopify pos | 1 | 8,100 | 55 | $8.36 | 6,480 | 导航 | pos |
| shopify pricing | 1 | 8,100 | 46 | $3.23 | 6,480 | 导航 | pricing |
| shopify plans | 1 | 4,400 | 29 | $3.43 | 3,520 | 导航 | pricing |
| return policy | 8 | 450,000 | 79 | $1.93 | 4,050 | 信息 | blog/return-policy |
| motivational quotes | 25 | 2,240,000 | 69 | $0.03 | 3,360 | 信息 | blog/motivational-quotes |
| google business profile | 10 | 246,000 | 71 | $11.52 | 3,198 | 商业 | blog/google-business-profile |
| shopify starter plan | 1 | 6,600 | 30 | $6.42 | 5,280 | 导航 | starter |
| shopify collabs | 1 | 5,400 | 38 | $7.41 | 4,320 | 商业/导航 | collabs.shopify.com |
| shopify business name generator | 1 | 3,600 | 71 | $1.64 | 2,880 | 导航 | tools/business-name-generator |
| shopify affiliate program | 1 | 3,600 | 41 | $5.09 | 2,880 | 信息/导航 | affiliates |

> **洞察**：① 品牌词绝对统治——排名 1 的 `shopify`（1M 月量）贡献 800K 纯导航流量，无法正面竞争；② 非品牌词闯入前列的有 `dropshipping`（rank 2，KD 70），靠 help 子域的信息内容拿到；③ 信息博客策略极为激进——`motivational quotes`（2.24M 月量，rank 25）、`return policy`（450K，rank 8）、`google business profile`（246K）这类完全非电商词也在吃流量，属内容漏斗顶端 TOFU 策略，为品牌带来海量潜在商家曝光。

### 付费词（Google Ads，按流量排序）

Shopify 大量购买竞品品牌词 + POD 工具词，导向专用对比/合作落地页（`/ppc/compare/`、`/ppc/print-on-demand/`），策略极为清晰。

| 关键词 | 月量 | CPC | 流量 | 落地页 |
|--------|------|-----|------|--------|
| shopify | 1,000,000 | $4.42 | 47,000 | /ppc/online-store |
| pirate ship | 823,000 | $2.66 | 38,681 | apps.shopify.com/pirate-ship |
| dropshipping | 673,000 | $3.95 | 31,631 | /ppc/dropshipping |
| shop | 450,000 | $1.01 | 21,150 | /shop |
| what is a url | 368,000 | $0.62 | 17,296 | /blog/parts-of-a-url |
| printify | 301,000 | $1.81 | 14,147 | /ppc/print-on-demand/printify |
| squarespace | 550,000 | $4.10 | 4,950 | /ppc/compare/shopify-vs-squarespace |
| square | 673,000 | $7.61 | 6,057 | /compare/shopify-vs-square |
| printful | 135,000 | $1.31 | 6,345 | /ppc/print-on-demand/printful |
| shop pay | 110,000 | $0.95 | 5,170 | /shop-pay |
| pos | 74,000 | $10.12 | 3,478 | /pos/free-trial/sell-retail |
| amazon affiliate program | 90,500 | $2.37 | 4,253 | /blog/amazon-affiliate-marketing |
| business name generator | 49,500 | $0.88 | 2,326 | /tools/business-name-generator |
| side hustles | 49,500 | $1.53 | 2,326 | /blog/side-hustle |
| whois lookup | 74,000 | $3.93 | 3,478 | /domains |

> **洞察**：① Shopify 自购最大词（`shopify` $4.42/click，47K paid traffic）说明自身品牌词也有竞价保护；② `pirate ship`（物流服务，38K 付费流量）是拦截用户找现有集成应用的典型防御动作；③ 专建 `/ppc/compare/shopify-vs-squarespace` 类对比落地页，清晰说明竞争对手定向是核心付费策略；④ `what is a url`、`side hustles` 等通用教育词也买，打品牌认知 TOFU。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| woocommerce vs shopify | 2,900 | 31 | $3.29 | 商业/信息 | 最大对比词簇 |
| shopify alternatives | 2,400 | 28 | $5.45 | 商业/信息 | ⭐ 核心机会 |
| shopify competitors | 1,600 | 34 | $4.77 | 商业 | 高 CPC |
| bigcommerce vs shopify | 1,000 | 33 | $8.52 | 商业/信息 | 高 CPC 企业意图 |
| squarespace vs shopify | 1,000 | 26 | $4.35 | 商业/信息 | ⭐ |
| shopify alternative | 720 | 25 | $5.45 | 商业 | ⭐ 主攻目标 |
| alternatives to shopify | 480 | 30 | $5.90 | 商业 | |
| shopify vs | 320 | 34 | $5.19 | 信息 | 宽泛对比意图 |
| best shopify alternatives | 110 | 26 | $10.44 | 信息 | ⭐ CPC 极高 |
| alternative to shopify | 260 | 24 | $5.89 | 信息 | ⭐ |
| alternative for shopify | 170 | 23 | $5.02 | 信息 | ⭐ |
| shopify competitor | 170 | 29 | $4.77 | 信息 | ⭐ |
| free shopify alternative | 30 | 31 | $6.96 | 商业/信息 | |
| medusa vs shopify | 20 | 0 | $0 | - | ⭐ GEO 前哨 |
| saleor vs shopify | 20 | 0 | $0 | - | ⭐ GEO 前哨 |
| open source shopify alternative | 10 | 0 | $2.39 | - | ⭐ GEO 前哨 |
| shopify plus alternative | 10 | 0 | $8.75 | - | ⭐ GEO，高 CPC |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ecommerce platform | 6,600 | 63 | $5.62 | 商业/信息 | 强竞争，难以切入 |
| best ecommerce platform | 3,600 | 27 | $7.94 | 信息 | ⭐ KD 低！高商业价值 |
| headless ecommerce | 1,900 | 50 | $9.95 | 商业/信息 | 开发者词，Medusa/Saleor 角度 |
| composable commerce | 1,600 | 38 | $5.93 | 商业 | 企业决策者词 |
| ecommerce platform comparison | 1,300 | 57 | $10.53 | 商业/信息 | |
| woocommerce | 49,500 | 63 | $5.05 | 导航 | 品牌词 |
| bigcommerce | 33,100 | 62 | $10.46 | 导航 | 品牌词 |
| prestashop | 2,400 | 73 | $5.21 | 导航 | 开源竞品，KD 极高 |
| medusajs | 2,900 | 49 | $0.05 | 导航 | Medusa 品牌词上量 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| shopify pricing | 8,100 | 46 | $3.24 | 导航 | 定价痛点入口 |
| shopify fees | 8,100 | 47 | $3.24 | 商业 | 费用焦虑 |
| shopify plus | 2,900 | 31 | $6.77 | 导航 | ⭐ 企业升级决策词 |
| shopify plus pricing | 1,600 | 19 | $4.87 | 导航/交易 | ⭐ KD 仅 19！ |
| shopify b2b | 1,000 | 48 | $10.44 | 商业/导航 | B2B 高 CPC |
| who owns shopify | 1,300 | 45 | $10.30 | 信息 | 品牌认知/信任词 |
| shopify transaction fees | 590 | 35 | $1.59 | 商业/交易 | 费率痛点 |
| shopify checkout | 480 | 48 | $5.77 | 导航 | |
| woocommerce alternative | 110 | 20 | $3.60 | 商业 | ⭐ WC 逃离信号 |
| magento alternative | 50 | 11 | $10.05 | 商业 | ⭐ KD 仅 11，高 CPC |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source ecommerce | 720 | 69 | $4.86 | 商业/信息 | KD 高但核心词 |
| medusa.js | 1,300 | 29 | $8.43 | 导航 | ⭐ 中量低 KD，高 CPC |
| medusa js | 480 | 31 | $7.22 | 导航 | ⭐ |
| saleor | 480 | 32 | $6.71 | 导航 | ⭐ |
| medusa ecommerce | 140 | 32 | $7.38 | 导航 | ⭐ |
| self hosted ecommerce | 40 | 21 | $6.20 | 信息 | ⭐ 完美信号词 |
| magento alternative | 50 | 11 | $10.05 | 商业 | ⭐ KD 极低 |
| woocommerce alternative | 110 | 20 | $3.60 | 商业 | ⭐ |
| self hosted online store | 20 | 0 | $0 | - | ⭐ GEO |
| open source shopify | 20 | 0 | $4.80 | - | ⭐ GEO |
| self hosted shopify | 10 | 0 | $4.99 | - | ⭐ GEO |
| open source shopify alternative | 10 | 0 | $2.39 | - | ⭐ GEO |

---

## Olares 关联词（Phase 3）

**核心逻辑：Shopify 的最大痛点是费用锁定（月费+交易抽成+Plus $2,300 门槛）+ 数据存在 Shopify 云端；Olares 平台让用户一键部署 Medusa（MIT），获得同等功能的开源电商后端，零月费、零交易抽成、数据完全自控——这是 Olares 在电商赛道的核心叙事切入。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| shopify alternatives | 2,400 | 28 | $5.45 | ⭐⭐⭐ Medusa on Olares = 最直接替代，一键部署，零月费 |
| shopify alternative | 720 | 25 | $5.45 | ⭐⭐⭐ 同上，量较小但意图更精准 |
| best ecommerce platform | 3,600 | 27 | $7.94 | ⭐⭐⭐ 文章可将 Medusa+Olares 作为"最佳自托管方案"登榜 |
| open source ecommerce | 720 | 69 | $4.86 | ⭐⭐ 高 KD 难抢排名，但 Medusa on Olares 的完整 GEO 位可做 |
| shopify plus pricing | 1,600 | 19 | $4.87 | ⭐⭐⭐ KD 极低，商业意图强；用 Medusa+Olares 对比 $2,300/月封杀 |
| shopify fees | 8,100 | 47 | $3.24 | ⭐⭐ 流量大但 KD 偏高；可做 FAQ：Olares 消灭平台抽成 |
| medusa vs shopify | 20 | 0 | $0 | ⭐⭐⭐ 零 KD GEO 前哨，Olares 可直接抢引用位 |
| saleor vs shopify | 20 | 0 | $0 | ⭐⭐ 同上；Saleor 暂未上架 Olares，但可顺带提及 |
| self hosted ecommerce | 40 | 21 | $6.20 | ⭐⭐⭐ 完美信号词；Olares = 最省力的自托管电商基座 |
| medusa.js | 1,300 | 29 | $8.43 | ⭐⭐ Medusa 品牌词，高 CPC，Olares 作为最方便的部署平台 |
| saleor | 480 | 32 | $6.71 | ⭐⭐ 开源电商品牌词，可对比 Olares 部署优势 |
| woocommerce alternative | 110 | 20 | $3.60 | ⭐⭐ WC 逃离者同样是 Medusa 目标用户 |
| magento alternative | 50 | 11 | $10.05 | ⭐⭐ KD 仅 11，$10 CPC；Medusa+Olares 作为现代 Magento 替代 |
| headless ecommerce | 1,900 | 50 | $9.95 | ⭐⭐ Medusa 是 headless-first，Olares 提供基础设施 |
| shopify plus alternative | 10 | 0 | $8.75 | ⭐⭐⭐ 完美 GEO 词；面向 Plus 的 B2B 商家讲 Medusa 的 B2B 能力 |
| self hosted shopify | 10 | 0 | $4.99 | ⭐⭐⭐ 用户直接搜这个词，Olares+Medusa 就是答案 |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| shopify alternatives | 2,400 | 28 | $5.45 | 商业/信息 | **主词候选** | KD 28 低、量 2.4K、CPC $5.45 商业价值高；Olares+Medusa 是最强实质性替代，可撑一篇"Best Shopify Alternatives"主文 |
| best ecommerce platform | 3,600 | 27 | $7.94 | 信息 | **主词候选** | 量 3.6K、KD 27 异常低；$7.94 CPC 证明高商业价值；Olares+Medusa 作为开源最佳方案可入榜 |
| shopify plus pricing | 1,600 | 19 | $4.87 | 导航/交易 | **主词候选** | KD 仅 19 全报告最低大词；商业意图强；主攻 "$2,300/月 vs 自托管 $0" 对比 |
| shopify alternative | 720 | 25 | $5.45 | 商业 | **主词候选** | 单数形式量稍小但意图最精准；与 `shopify alternatives` 合并成一篇 |
| woocommerce vs shopify | 2,900 | 31 | $3.29 | 商业/信息 | **主词候选** | 最大 vs 词；可做多平台对比文，Medusa 作为第三选项自然植入 |
| headless ecommerce | 1,900 | 50 | $9.95 | 商业/信息 | 次级 | KD 50 偏高排不动主词；并入 Medusa 技术介绍文的 secondary 词 |
| composable commerce | 1,600 | 38 | $5.93 | 商业 | 次级 | 企业决策者词；并入 headless/composable 对比文 |
| shopify fees | 8,100 | 47 | $3.24 | 商业 | 次级 | 量大但 KD 47；痛点词，作为替代文的 FAQ 锚点 |
| shopify plus | 2,900 | 31 | $6.77 | 导航 | 次级 | 主要是 Shopify 自身导航词，排不动但作为内容中的对比锚点有价值 |
| medusa.js | 1,300 | 29 | $8.43 | 导航 | **主词候选** | Olares Market 已上架 Medusa；这是平替方向的直接品牌词，量够、KD 低、CPC 高 |
| medusa vs shopify | 20 | 0 | $0 | - | **GEO** | 精准意图但量极低；写一段 FAQ/比较段落抢 AI Overview/Perplexity 引用 |
| saleor vs shopify | 20 | 0 | $0 | - | **GEO** | 同上；可并入 Medusa 对比文的 appendix |
| self hosted ecommerce | 40 | 21 | $6.20 | 信息 | 次级 | 量小但意图极强，KD 低；并入自托管电商选题作为支撑词 |
| self hosted shopify | 10 | 0 | $4.99 | - | **GEO** | 用户直接搜"self-hosted Shopify"——Olares+Medusa 就是标准答案 |
| open source shopify alternative | 10 | 0 | $2.39 | - | **GEO** | 同上，语义更精准 |
| shopify plus alternative | 10 | 0 | $8.75 | - | **GEO** | 高 CPC GEO；面向 $2,300+/月 的 Plus 用户，Medusa B2B 功能可应对 |
| magento alternative | 50 | 11 | $10.05 | 商业 | 次级 | KD 仅 11！$10 CPC；Magento 逃离者也是 Medusa 目标用户 |
| woocommerce alternative | 110 | 20 | $3.60 | 商业 | 次级 | KD 低；WC 用户逃离路径与 Medusa 用户高度重合 |

---

## 核心洞见

1. **品牌护城河**：`shopify`（1M 月量，KD 100，rank 1）绝对无法正面刚——完全是品牌流量护城河。任何内容都应绕开品牌核心词，从**对比词、痛点词、品类词**三个侧翼切入。

2. **可复制的打法**：Shopify 有三套清晰可学策略：① **程序化对比落地页**（`/ppc/compare/shopify-vs-squarespace` 等），买竞品词直接截流；② **博客 TOFU 海量文章**（`motivational quotes` 2.24M 量，`return policy` 450K），靠潜在商家关心的泛话题吸引人群再转化；③ **App 关键词借力**（`pirate ship`、`printify` 等第三方工具词，借 apps.shopify.com 子域名吃流量）。Olares 可学的是"对比落地页"策略，针对 `shopify alternatives`、`shopify plus alternative` 等词建专页。

3. **对 Olares 最关键的词**：
   - `shopify alternatives`（2,400 月量，KD 28）——主攻，Medusa on Olares 最强切入
   - `shopify plus pricing`（1,600 月量，KD 19）——KD 全报告最低大词，"$2,300/月 vs 零月费" 对比杀手级
   - `self hosted shopify` / `self hosted ecommerce`（量极小但 GEO 语义完美）——抢 AI Overview 引用位

4. **最大攻击面**：Shopify 的核心痛点是**费用复合锁定**——①月费随规模直线上升；②使用第三方支付额外收 0.5%~2% 强制导向 Shopify Payments；③ $2,300/月的 Plus 门槛屏蔽大量中小企业 B2B 功能；④数据存在 Shopify 云端、GDPR 合规难度高。Olares+Medusa 的叙事是：零平台月费、零交易抽成、数据完全本地控制、B2B 功能（Medusa v2 已内置）免费使用。

5. **隐藏低 KD 金矿**：
   - `shopify plus pricing`（KD 19，商业意图强，$4.87 CPC）——最大的被忽视机会
   - `magento alternative`（KD 11，$10 CPC）——Magento 逃离者市场，Medusa 是现代 Magento 最直接替代
   - `alternative to shopify`（KD 24）、`alternative for shopify`（KD 23）——比主词 KD 还低的长尾变体

6. **GEO 前瞻布局**：以下近零量词进 FAQ/比较段落，抢 AI Overview 和 Perplexity 引用位：
   - `medusa vs shopify`（KD 0）
   - `saleor vs shopify`（KD 0）
   - `self hosted shopify`（KD 0）
   - `open source shopify alternative`（KD 0）
   - `shopify plus alternative`（KD 0，$8.75 CPC）

7. **与既有分析的关联**：olares-500-keywords 词表中暂未见 `shopify alternative` 类词，本报告补充了高商业价值的电商平台替代词簇（KD 低、CPC 高）。与已有 Medusa 报告（market/reports/medusa.md）形成上下游：Medusa 报告从产品维度切入，本报告从 Shopify 痛点维度切入，可联动互引。建议 seo-content 优先写 "Shopify Alternatives" 文章簇并在 Olares Market Medusa 页面做内链。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*项目事实来源：shopify.com/pricing、PitchGrade、TechnologyChecker.io、GitHub medusajs/medusa、GitHub saleor/saleor（均 2026 年数据）。*
