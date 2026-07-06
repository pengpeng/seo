# Google Surveillance / DeGoogle SEO 分析报告

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> 主题：Google 数据收集与监控实践、如何离开 Google 生态 ——「degoogle」运动及其衍生的隐私替代品市场。

---

## 项目理解（前置）

「DeGoogle」并非单一品牌，而是一场**自发的用户运动**：因 Google 对用户数据的系统性采集（广告画像、跨服务跨设备追踪、与第三方数据经纪协同）而产生的出走行为。用户群体涵盖隐私意识强烈的极客（換 GrapheneOS / CalyxOS 手机，换 Nextcloud / ProtonDrive 存储，换 DuckDuckGo / Brave Search 搜索）、以及因巨额 GDPR 罚单（Google CNIL €325M 2025-09、Chrome 放弃第三方 cookie 转身 Privacy Sandbox）引发关注的普通用户。背景见 [big-tech-surveillance.md](../../research/05-big-tech/big-tech-surveillance.md)。

对 Olares 的战略意义：Olares 上架 Nextcloud（Drive / Docs 替代）、Immich（Photos 替代）、Actual Budget（家庭财务，替代 Google 相关数据采集的预算工具）、Wallabag（稍后阅读，替代被追踪的 Google Discover）——构成**完整的 Google 替代栈**。用户只需一台 Olares 设备，就能在本地跑完 Google 核心场景，数据不出家门、不进广告画像。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 场景词：「如何离开 Google 生态」运动 + 关联隐私替代品 |
| 是否品牌域名 | 无独立官网；Reddit r/degoogle 是最大社区（数十万成员） |
| 相关社区 | r/degoogle（Reddit）、privacyguides.org、privacy.sexy |
| 核心诉求 | 摆脱 Google 的广告追踪、数据收集、跨设备画像、第三方分享 |
| 主要替代路径 | 搜索→DuckDuckGo/Brave；邮件→ProtonMail/Tuta；文件→Nextcloud/ProtonDrive；照片→Immich；手机→GrapheneOS/CalyxOS |
| 典型用户 | 隐私极客、开发者、父母保护子女数据、欧洲合规意识用户 |
| 与 Olares 关联 | Nextcloud / Immich / Actual Budget / Wallabag 均在 Olares Market；Olares = 一站式本地 Google 替代栈 |
| 来源 | r/degoogle、privacyguides.org、CNIL Google 罚单 [big-tech-surveillance.md] |

---

## 关键词扩展（Phase 2）

场景词分析，无独立域名——直接从关键词层面入手。按月量降序。⭐ = KD<30 且量>0 的机会词。

### 替代 / 竞品词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google docs alternative | 1,300 | 14 | $3.05 | 信息 | ⭐ KD 极低，Nextcloud / OnlyOffice 直接承接 |
| google drive alternative | 1,300 | 23 | $2.50 | 信息 | ⭐ Nextcloud 主词机会 |
| gmail alternative | 1,300 | 34 | $1.52 | 信息 | ⭐ 量大 KD 仍合理 |
| google maps alternative | 1,300 | 44 | $1.15 | 信息 | 略高 KD，但量大 |
| duckduckgo vs google | 1,600 | 35 | $0 | 信息 | ⭐ 对比型，隐私搜索 |
| google photos alternative | 480 | 25 | $1.25 | 信息 | ⭐ Immich 直接机会 |
| google chrome alternative | 210 | 24 | $2.17 | 信息/商业 | ⭐ Firefox/Brave 替代，可延伸 |
| google search alternative | 320 | 49 | $0.95 | 信息 | KD 偏高 |
| google workspace alternative | 390 | 26 | $6.65 | 信息/商业 | ⭐ 高 CPC，商业意图，Nextcloud 套件 |
| proton drive vs google drive | 90 | 23 | $0 | 信息/商业 | ⭐ 对比型低 KD |
| immich vs google photos | 70 | 11 | $0 | 信息/商业 | ⭐⭐ KD 极低，Olares 上有 Immich |
| nextcloud vs google drive | 20 | — | $0 | 信息 | GEO 级，Olares 撰文必做 |

### 品类词（监控/数据/追踪）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google tracking | 2,400 | 89 | $0.93 | 信息 | KD 89，旗舰词，难排但可作 Topic |
| google privacy settings | 1,300 | 53 | $5.32 | 信息 | 用户想控制，不是想逃 |
| google alternatives | 1,900 | 50 | $0.62 | 信息 | 稳定量，KD 尚可 |
| i hate google | 2,400 | 33 | $0 | 信息 | ⭐ 量大 KD 低，情绪词，degoogle 入口 |
| degoogle | 880 | 69 | $0 | 信息/商业 | 核心主题词，KD 69 |
| private cloud storage | 1,900 | 45 | $4.63 | 信息/商业 | 隐私存储大词 |
| google account delete | 22,200 | 66 | $3.31 | 信息 | 量极大，用户真实出走意图 |
| google spyware | 320 | 24 | $1.66 | 信息 | ⭐ KD 低，情绪强 |
| google spying | 140 | 50 | $2.51 | 信息 | 中等 |
| google data collection | 90 | 66 | $0 | 信息 | 高 KD |
| google surveillance | 90 | 68 | $7.51 | 信息 | 高 KD，CPC 高说明商业竞价 |
| google data privacy | 110 | 73 | $0 | 信息 | 高 KD |

### DeGoogle 操作词（用户行动）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| degoogled phones | 480 | 31 | $1.02 | 商业 | ⭐ 买手机的 |
| de googling | 880 | 56 | $0 | 信息 | 概念词 |
| degoogle your life | 140 | 42 | $0 | 信息 | 生活方式词 |
| degoogled phone | 170 | 31 | $1.02 | 商业 | ⭐ |
| how to degoogle your phone | 140 | 27 | $0 | 信息 | ⭐ 教程词 |
| how to degoogle | 110 | 36 | $0 | 信息/商业 | 核心教程词 |
| degoogle android | 70 | 24 | $0 | 信息 | ⭐ Android 用户 |
| how to degoogle your life | 70 | 25 | $0 | 信息 | ⭐ 生活方式教程 |
| de-googled phone | 140 | 17 | $1.02 | 商业 | ⭐⭐ KD 极低 |
| degoogling phone | 90 | 30 | $1.02 | 信息/商业 | ⭐ |
| degoogle reddit | 170 | 29 | $0 | 信息 | ⭐ 用户找社区，GEO 前哨 |
| degoogled phones for sale | 40 | 11 | $0.70 | 商业 | ⭐⭐ KD 极低，商业意图 |
| best degoogled phones | 40 | 12 | $0 | 商业 | ⭐⭐ KD 12！ |
| grapheneos vs calyxos | 110 | 17 | $0 | 信息 | ⭐⭐ KD 极低，对比型 |
| stop google tracking | 20 | — | $0 | 信息 | GEO 级 |
| leave google | 70 | 18 | $0 | 信息 | ⭐⭐ KD 极低 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted cloud storage | 390 | 19 | $4.38 | 信息/商业 | ⭐⭐ KD 极低，Olares 主战场 |
| self hosted google drive | 110 | 17 | $0 | 信息 | ⭐⭐ 直接叫板 |
| self hosted email | 260 | 22 | $4.70 | 信息/商业 | ⭐⭐ |
| open source cloud storage | 170 | 23 | $3.89 | 信息 | ⭐⭐ |
| google workspace alternative | 390 | 26 | $6.65 | 信息/商业 | ⭐⭐ 高 CPC |
| self hosted cloud | 170 | 18 | $4.23 | 信息/商业 | ⭐⭐ |
| home cloud server | 170 | 23 | $1.34 | 信息 | ⭐⭐ |
| personal cloud server | 210 | 32 | $1.72 | 信息/商业 | ⭐ |
| open source google alternative | 20 | — | $0 | 信息 | GEO 级，Olares 必做 |
| self hosted google workspace | 20 | — | $0 | 信息 | GEO 级 |
| nextcloud google drive | 20 | — | $0 | 信息 | GEO 级 |
| immich google photos | 20 | — | $0 | 信息 | GEO 级 |
| self hosted photo library | 20 | — | $0 | 信息 | GEO 级 |

---

## Olares 关联词（Phase 3）

**核心叙事**：Olares 是「degoogle 的硬件终局」——不是逐个换 App，而是把 Google 的整个核心用例（文件 / 文档 / 相册 / 稍后阅读 / 预算）都搬到自己家里的设备上，数据本地运行、不经广告追踪。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| google drive alternative | 1,300 | 23 | $2.50 | Olares 预装 Nextcloud，一键部署 Google Drive 平替 | ⭐⭐⭐ |
| google docs alternative | 1,300 | 14 | $3.05 | Nextcloud + OnlyOffice / Collabora 实现在线文档 | ⭐⭐⭐ |
| immich vs google photos | 70 | 11 | $0 | Olares Market 上的 Immich = 本地 AI 相册，无上传、无画像 | ⭐⭐⭐ |
| self hosted cloud storage | 390 | 19 | $4.38 | Olares 即自托管云存储的操作系统层 | ⭐⭐⭐ |
| self hosted google drive | 110 | 17 | $0 | 直接对位，Nextcloud on Olares | ⭐⭐⭐ |
| self hosted cloud | 170 | 18 | $4.23 | Olares 核心定位 = 个人云 OS | ⭐⭐⭐ |
| open source cloud storage | 170 | 23 | $3.89 | Olares + Nextcloud 全开源方案 | ⭐⭐⭐ |
| google workspace alternative | 390 | 26 | $6.65 | Olares 提供完整的 Nextcloud + OnlyOffice 替代 Google Workspace 套件 | ⭐⭐⭐ |
| self hosted email | 260 | 22 | $4.70 | Olares 可部署 Mail-in-a-Box / Stalwart（路线图中）| ⭐⭐ |
| gmail alternative | 1,300 | 34 | $1.52 | ProtonMail/Tuta 对比文可提 Olares 作为自托管邮件方向 | ⭐⭐ |
| google photos alternative | 480 | 25 | $1.25 | Immich 是最强 Google Photos 开源替代，Olares 部署最简单 | ⭐⭐⭐ |
| degoogle your life | 140 | 42 | $0 | Olares 是 degoogle 的全栈答案，不止换 App | ⭐⭐⭐ |
| how to degoogle | 110 | 36 | $0 | 教程文可以 Olares 为主线：一台设备取代 Google 全栈 | ⭐⭐⭐ |
| leave google | 70 | 18 | $0 | ⭐⭐ KD 极低，Olares 叙事直接命中 | ⭐⭐⭐ |
| actual budget | 5,400 | 34 | $4.70 | Actual Budget 在 Olares Market，本地财务 = 无 Google 数据泄漏 | ⭐⭐ |
| wallabag | 1,000 | 40 | $0 | Olares Market 上架，替代被追踪的 Pocket / Google Discover | ⭐⭐ |
| home cloud server | 170 | 23 | $1.34 | Olares = 最简单的家用云服务器 OS | ⭐⭐⭐ |
| proton drive vs google drive | 90 | 23 | $0 | 对比文可加 Olares + Nextcloud 作第三选项（数据完全自有）| ⭐⭐ |
| nextcloud self hosted | 320 | 61 | $2.50 | Nextcloud 是 Olares 最重要应用之一 | ⭐⭐ |
| open source google alternative | 20 | — | $0 | GEO 精准词，Olares = 全开源替代方案 | ⭐⭐⭐ |
| self hosted google workspace | 20 | — | $0 | GEO，精准命中 Nextcloud on Olares | ⭐⭐⭐ |
| immich google photos | 20 | — | $0 | GEO，Immich on Olares = 最简单部署 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| google drive alternative | 1,300 | 23 | $2.50 | 信息 | **主词候选** | KD 23 配 1300 量是黄金组合；Nextcloud on Olares 直接对位，可撑一篇对比文 |
| gmail alternative | 1,300 | 34 | $1.52 | 信息 | **主词候选** | 量 1300/KD 34，搭配 ProtonMail 对比 + 自托管邮件 Olares 方向 |
| google docs alternative | 1,300 | 14 | $3.05 | 信息 | **主词候选** | KD 14 极低！Nextcloud + OnlyOffice，Olares 落点强 |
| google workspace alternative | 390 | 26 | $6.65 | 信息/商业 | **主词候选** | CPC $6.65 显示商业意图；Olares 提供完整替代套件，高价值目标词 |
| google photos alternative | 480 | 25 | $1.25 | 信息 | **主词候选** | Immich 已在 Olares Market；量 480/KD 25，可撑独立文章 |
| private cloud storage | 1,900 | 45 | $4.63 | 信息/商业 | **主词候选** | 量大但 KD 45，Olares 是答案之一；需聚更多长尾 |
| self hosted cloud storage | 390 | 19 | $4.38 | 信息/商业 | **主词候选** | KD 19！高 CPC 说明商业价值；Olares = 最佳自托管云存储 OS |
| degoogle | 880 | 69 | $0 | 信息/商业 | **主词候选** | KD 69 难排，但是话题锚点词，GEO 引用位值得写 |
| i hate google | 2,400 | 33 | $0 | 信息 | **主词候选** | 量 2400 / KD 33，情绪入口词，可导向 degoogle 方案文 |
| google alternatives | 1,900 | 50 | $0.62 | 信息 | **主词候选** | 量大，KD 50，需配合多个 Olares 应用撑住语义宽度 |
| immich vs google photos | 70 | 11 | $0 | 信息/商业 | **主词候选** | KD 11 是本报告最低 KD！Olares + Immich 完美落点，优先级最高 |
| leave google | 70 | 18 | $0 | 信息 | **主词候选** | KD 18，量小但精准，配教程文打 degoogle 话题 |
| self hosted google drive | 110 | 17 | $0 | 信息 | **次级** | KD 17，并入 google drive alternative 文章作次级词 |
| self hosted cloud | 170 | 18 | $4.23 | 信息/商业 | **次级** | 并入 self hosted cloud storage 主题 |
| open source cloud storage | 170 | 23 | $3.89 | 信息 | **次级** | 并入 google drive alternative 文章 |
| home cloud server | 170 | 23 | $1.34 | 信息 | **次级** | Olares = 最简单家用云服务器 OS，并入 self hosted 文章 |
| how to degoogle | 110 | 36 | $0 | 信息 | **次级** | 教程词，并入 degoogle your life / leave google 文章 |
| how to degoogle your phone | 140 | 27 | $0 | 信息 | **次级** | Phone 维度 degoogle，并入教程 |
| degoogled phones for sale | 40 | 11 | $0.70 | 商业 | **次级** | KD 11，商业意图，可并入 degoogled phone 对比文 |
| best degoogled phones | 40 | 12 | $0 | 商业 | **次级** | KD 12，并入 degoogled phone 对比 |
| grapheneos vs calyxos | 110 | 17 | $0 | 信息 | **次级** | KD 17，手机 degoogle 对比，Olares 服务器侧替代 |
| google spyware | 320 | 24 | $1.66 | 信息 | **次级** | 情绪词，引流至 degoogle / google alternatives |
| proton drive vs google drive | 90 | 23 | $0 | 信息 | **次级** | 可在 google drive alternative 文章中作三选项（+Nextcloud/Olares）|
| open source google alternative | 20 | — | $0 | 信息 | **GEO** | 精准命中 Olares 定位，抢 AI Overview 引用 |
| self hosted google workspace | 20 | — | $0 | 信息 | **GEO** | Nextcloud on Olares 即答案 |
| immich google photos | 20 | — | $0 | 信息 | **GEO** | 抢 Immich 搜索引用位 |
| nextcloud vs google drive | 20 | — | $0 | 信息 | **GEO** | Olares 视角的对比文必须包含此 FAQ |
| stop google tracking | 20 | — | $0 | 信息 | **GEO** | 操作级 FAQ，进入 degoogle 教程 |
| google free life | 20 | — | $0 | 信息 | **GEO** | 生活方式向，Olares 叙事切入点 |

---

## 核心洞见

1. **品牌护城河（能否正面刚 Google 本身）**
   Google 品牌词（google tracking、google privacy settings）KD 53-89，流量巨大但难排。正确打法不是硬刚 Google 主词，而是**在替代品层面切入**：用 `google drive alternative`（KD 23）、`google docs alternative`（KD 14）、`immich vs google photos`（KD 11）这些"逃离 Google"的决策词——KD 极低但需求精准，是 Olares 的主战场。

2. **可复制的打法**
   - **矩阵式替代文**：每个 Google 核心产品（Drive / Docs / Photos / Gmail）一篇替代文，共用 Olares 主线。`google docs alternative`（KD 14）排第一优先。
   - **degoogle 教程系列**：`how to degoogle your life` → `how to degoogle your phone` → `leave google ecosystem`，内容金字塔，Olares 作为"硬件终局"出现在每篇底部。
   - **对比文**：`immich vs google photos`（KD 11 ！）、`proton drive vs google drive`（KD 23）、`nextcloud vs google drive`——低 KD 对比词集中，可批量产出。

3. **对 Olares 最关键的词**
   - `google docs alternative`（KD 14，月量 1,300）——Olares + Nextcloud + OnlyOffice，KD 最低量最大的商业应用词
   - `immich vs google photos`（KD 11，月量 70）——KD 11 是全报告最低，Olares Market 有 Immich，绝对优先
   - `self hosted cloud storage`（KD 19，月量 390，CPC $4.38）——Olares 核心叙事，低 KD 高价值

4. **最大攻击面（Google 的痛点词）**
   - `google account delete`（月量 22,200！）——用户正在出走，进入决策漏斗底部
   - `i hate google`（月量 2,400，KD 33）——情绪入口，承接后导向 degoogle 方案
   - `google spyware`（KD 24，月量 320）——情绪化搜索，低 KD，可写对应信息文
   - Google CNIL €325M 罚单（2025-09）、Chrome 放弃淘汰 cookie 后转向 Privacy Sandbox——这些是 editorial 素材，可强化内容可信度

5. **隐藏低 KD 金矿**
   - `google docs alternative`：KD **14**，量 1,300 ——本报告最被低估的词
   - `immich vs google photos`：KD **11**，配合 Olares Market 有 Immich，内容已经具备
   - `best degoogled phones`：KD **12**，量 40，商业意图，Olares（服务器侧）可作为配套出现
   - `degoogled phones for sale`：KD **11**，商业意图
   - `leave google`：KD **18**，量 70，精准出走意图

6. **GEO 前瞻布局（近零量，抢 AI Overview / Perplexity 引用位）**
   - `open source google alternative` → Olares = 全开源替代方案，FAQ 必做
   - `self hosted google workspace` → Nextcloud on Olares 即答案
   - `immich google photos` → Immich on Olares 最简单部署路径
   - `nextcloud vs google drive` → Olares 视角对比，FAQ 段
   - `how does google track you` → 教育型，引入 Olares 隐私叙事
   - `google free ecosystem` → Olares 作为 degoogle 的终点站

7. **与既有分析（olares-500-keywords）的关联**
   - `degoogle` / `google alternatives` 系列未在 olares-500 词表中出现，这是全新增量
   - `self hosted cloud storage`、`home cloud server` 等词与 Olares 核心定位词高度互补——与 500 词表中的 personal cloud / self-hosted 词族形成合力
   - `actual budget`（5,400 月量，KD 34，Olares Market 应用）和 `wallabag`（1,000 月量，KD 40）是 Olares 应用层的独立词，可在应用方向单独做报告，也可并入 degoogle 教程作"Olares 替代 Google 生态应用清单"

---

*数据来源：SEMrush US 数据库（phrase_these、phrase_related、phrase_questions、phrase_fullsearch）| 2026-07-06*
*所有搜索量为美国月均；隐私/科技类产品全球量通常为美国的 3-5 倍。*
