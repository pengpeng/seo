# Strava SEO 竞品分析报告

> 域名：strava.com | SEMrush US | 2026-07-06
> 全球最大运动社交网络，180M 注册用户，以 GPS 分段排行榜把跑步/骑行数据锁进闭源订阅平台。

---

## 项目理解（前置）

Strava 是一个面向耐力运动员的 GPS 运动追踪与社交网络平台，创立于 2009 年，核心逻辑是"分段（Segment）排行榜"——把全球任意一段道路/山路的骑行/跑步时间做成公开竞速榜，驱动用户粘性与社交分享。2025 年收入约 $415M，用户估值 $2.2B，已于 2025 年初申请 IPO。平台**完全闭源**，数据全存在 Strava 服务器；订阅费 $79.99/年（个人）或 $11.99/月，免费层于 2024 年已大幅收窄（Group Challenges 移至付费、分段排行榜仅显示 Top 10）。2024-2025 年两度收紧 API——先禁止第三方向他人展示用户数据、再向开发者收 $11.99/月 API 访问费——触发大量隐私与数据主权讨论，直接喂大了自托管替代方案的搜索需求。

| 项目 | 内容 |
|------|------|
| 一句话定位 | GPS 运动追踪 + 运动社交网络，分段排行榜为核心驱动力 |
| 开源 / 许可证 | **闭源 SaaS**，无公开代码库 |
| 主仓库 | 无（闭源） |
| 核心功能 | GPS 追踪（48 种运动）、分段排行榜、社交动态/Kudos、路线构建、表现分析（Fitness & Freshness / CTL/ATL）、配速计算器、Heatmap |
| 商业模式 / 定价 | 免费基础层；个人订阅 $79.99/yr 或 $11.99/mo；家庭 $139.99/yr（最多 4 人）；Strava+Runna 捆绑 $149.99/yr；开发者 API $11.99/mo |
| 差异化 / 价值主张 | 分段排行榜（社交竞速）、最大运动员社区（180M）、全平台设备兼容（Garmin/Apple Watch/Wahoo 等直接同步）、全球 Heatmap 热力图 |
| 主要竞品（初判）| Garmin Connect（设备捆绑）、Nike Run Club（免费跑步）、Apple Fitness+（硬件捆绑）、TrainingPeaks（训练计划）、Komoot/RideWithGPS（路线）；自托管层：Endurain、FitTrackee、OpenTracks |
| Olares Market | **未上架**（OpenTracks / Endurain 均未列入，待补） |
| 来源 | [strava.com/pricing](https://www.strava.com/pricing)、[The Verge API 报道](https://www.theverge.com/2024/11/19/24301056/strava-api-ai-data-sharing-policy-change-fitness-tracking)、[Endurain GitHub](https://github.com/endurain-project/endurain)、[iot.md 已有研究](/Users/pengpeng/seo/directions/iot/iot.md) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | strava.com |
| SEMrush Rank | 7,023 |
| 自然关键词数 | 55,524 |
| 月自然流量（US）| 332,943 |
| 自然流量估值 | $156,288 /月 |
| 付费关键词数 | 50 |
| 月付费流量 | 14,529 |
| 月付费花费 | $1,938 |
| 排名 1-3 位 | 2,337 词 |
| 排名 4-10 位 | 5,591 词 |
| 排名 11-20 位 | 8,307 词 |

> **解读**：流量高度集中于品牌导航词（strava、strava login 前二合计贡献 175K+ 流量，占总量 53%），非品牌词依赖配速计算器（pace calculator 等工具页）引入信息流量。付费投放极少（$1,938/月），几乎全打自家品牌词引流到 /get-started。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.strava.com | 28,541 | 293,307 | 88.1% |
| support.strava.com | 10,592 | 23,976 | 7.2% |
| stories.strava.com | 11,655 | 6,878 | 2.1% |
| status.strava.com | 93 | 2,133 | 0.6% |
| developers.strava.com | 244 | 1,403 | 0.4% |
| labs.strava.com | 174 | 1,399 | 0.4% |
| press.strava.com | 748 | 1,310 | 0.4% |
| shop.strava.com | 202 | 1,129 | 0.3% |
| communityhub.strava.com | 2,301 | 617 | 0.2% |

> stories.strava.com 11,655 个关键词，但流量仅 6,878——典型的内容分发子域（博客/故事），SEO 效率低于主站。support.strava.com 的 7.2% 流量是高价值信号：大量用户通过帮助中心搜索"如何取消/导出/连接 Garmin"——这类信息词是我们的切入口。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|-----|-----|------|------|-----|
| strava | 1 | 201,000 | 80 | $0.07 | 160,800 | 导航 | /（品牌首页） |
| strava login | 1 | 18,100 | 65 | $0.00 | 14,480 | 导航 | /login |
| strava sign | 1 | 12,100 | 67 | $0.00 | 9,680 | 导航 | /login |
| stra | 1 | 49,500 | 46 | $4.38 | 6,534 | 导航 | /（错拼） |
| pace calculator | 5 | 74,000 | 47 | $1.29 | 3,256 | 信息 | /running-pace-calculator |
| strava heatmap | 1 | 3,600 | 32 | $2.01 | 2,880 | 导航/信息 | /maps/global-heatmap |
| strava subscription | 1 | 2,900 | 50 | $0.09 | 2,320 | 导航/商业 | /subscribe |
| strava pace calculator | 1 | 2,400 | 24 | $0.00 | 1,920 | 信息 | /running-pace-calculator |
| marathon pace chart | 2 | 18,100 | 27 | $1.46 | 1,484 | 信息 | /running-pace-calculator |
| strava family plan | 1 | 1,300 | 21 | $1.79 | 1,040 | 商业 | /family |
| strava api | 1 | 1,300 | 34 | $0.00 | 1,040 | 信息 | developers.strava.com |
| half marathon pace calculator | 1 | 3,600 | 49 | $0.39 | 892 | 信息 | /running-pace-calculator |
| strava student discount | 1 | 1,000 | 35 | $0.00 | 800 | 商业 | /student |
| strava pricing | 1 | 1,000 | 38 | $1.17 | 800 | 商业 | /pricing |
| apple watch strava app | 1 | 880 | 27 | $1.13 | 704 | 信息 | support.strava.com |
| trail running routes near me | 4 | 14,800 | 24 | $1.93 | 518 | 商业/本地 | /routes/trail-running/usa/washington |
| strava global heatmap | 1 | 590 | 29 | $0.00 | 472 | 信息 | /maps/global-heatmap |
| strava runna | 1 | 590 | 37 | $1.92 | 472 | 信息 | /strava-runna |
| strava flyby | 1 | 590 | 30 | $0.00 | 472 | 信息 | labs.strava.com/flyby |
| strava routes | 1 | 590 | 40 | $0.29 | 472 | 信息/商业 | /athlete/routes |
| streaks | 4 | 9,900 | 41 | $9.94 | 435 | 信息 | support.strava.com |
| strava route builder | — | 880 | 29 | $2.38 | — | 信息/商业 | — |
| strava beacon | — | 260 | 31 | $0.00 | — | 信息 | — |

> **关键观察**：配速计算器（`pace calculator` 74K 月量，CPC $1.29）是 Strava 少数几个有高量非品牌词的工具型落地页；`trail running routes near me`（14,800）是本地化内容程序化生成的路线页——两者都是"工具/内容拦截"打法。`strava heatmap`（KD 32，CPC $2.01）是罕见的功能词有广告价值的例子。

### 付费词（Google Ads）

主要打自家品牌词（strava / strava app / strava sign 等），**全部导向 /get-started 注册落地页**。整月付费花费仅约 $1,938，说明 Strava 几乎不靠 SEM 获客——依赖设备合作（Garmin/Apple Watch 生态）与口碑/社区。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| strava | 201,000 | $0.08 | /get-started |
| strava app | 14,800 | $0.76 | /get-started |
| cycling app | 720 | $1.60 | /get-started |
| strava bike app | 880 | $0.54 | /get-started |
| strava subscriber | 480 | $0.68 | /get-started |
| strava cycling | 260 | $0.64 | /get-started |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| strava vs garmin | 480 | 29 | $0.00 | 信息 | ⭐ 比较词，低 KD |
| strava vs nike run club | 320 | 26 | $0.00 | 信息 | ⭐ |
| nike run club vs strava | 170 | 26 | $0.00 | 信息 | ⭐ |
| strava vs apple fitness | 140 | 22 | $0.00 | 信息 | ⭐ |
| strava alternative | 140 | 14 | $1.14 | 信息 | ⭐ CPC 高表明商业价值 |
| strava alternatives | 70 | 10 | $0.00 | 信息 | ⭐ |
| garmin connect vs strava | 90 | 8 | $0.00 | 信息 | ⭐ 极低 KD |
| alternative to strava | 30 | 22 | $1.64 | 信息/信息 | ⭐ |
| open source strava alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ 近零 KD |
| self hosted strava alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ |
| strava alternative cycling | 20 | 0 | $0.00 | 信息 | ⭐⭐ |
| strava alternative running | 20 | 0 | $0.00 | 信息 | ⭐⭐ |
| strava heatmap alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ |
| strava route builder alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ |
| free strava alternatives | 30 | 0 | $0.58 | 信息 | ⭐⭐ |
| best strava alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| fitness tracking app | 1,300 | 86 | $1.78 | 信息 | 高 KD，品牌统治 |
| workout tracking app | 1,300 | 63 | $1.12 | 信息 | 高 KD |
| best fitness tracker app | 720 | 75 | $1.80 | 信息 | 综合榜单词 |
| free fitness tracker | 260 | 84 | $1.16 | 信息 | 高 KD |
| gps fitness tracker | 210 | 76 | $0.50 | 信息 | 高 KD |
| running apps | 4,400 | 30 | $1.29 | 信息 | ⭐ 边缘可竞争 |
| run tracker | 3,600 | 57 | $0.80 | 信息 | 中 KD |
| running app | 3,600 | 53 | $1.29 | 信息 | 中 KD |
| free running apps | 1,600 | 31 | $0.85 | 信息 | ⭐ |
| open source fitness tracker | 70 | 35 | $0.00 | 信息 | ⭐ Olares 核心词 |
| open source running app | 20 | 0 | $0.00 | 信息 | ⭐⭐ |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| strava cost | 1,300 | 33 | $0.03 | 信息 | ⭐ 高量付费疑虑 |
| is strava free | 2,900 | 32 | $1.36 | 信息 | ⭐ 大量 |
| strava price | 390 | 50 | $0.03 | 信息 | 中 KD |
| strava pricing | 1,000 | 38 | $1.17 | 商业 | 中 KD，有 CPC |
| how much is strava premium | 880 | 42 | $0.02 | 信息 | 中 KD |
| strava premium worth it | 40 | 32 | $0.00 | 信息 | ⭐ |
| is strava premium worth it | 480 | 29 | $0.00 | 信息 | ⭐ |
| cancel strava subscription | 140 | 21 | $0.00 | 信息 | ⭐ 取消意图强 |
| strava cancel subscription | 50 | 20 | $0.00 | 信息 | ⭐ |
| how to cancel strava subscription | 260 | 64 | $0.00 | 信息 | 高 KD（Strava 官方主导） |
| does strava cost money | 320 | 29 | $1.57 | 信息 | ⭐ |
| how to delete strava account | 720 | 29 | $0.00 | 信息 | ⭐ 强退出意图 |
| strava data export | 20 | 0 | $0.00 | 信息 | ⭐⭐ |
| strava heatmap | 3,600 | 32 | $2.01 | 信息 | ⭐ 功能词有价值 |
| strava route builder | 880 | 29 | $2.38 | 信息/商业 | ⭐ |
| strava beacon | 260 | 31 | $0.00 | 信息 | ⭐ |
| strava kudos | 720 | 37 | $0.00 | 信息 | 品牌词 |
| strava api | 1,300 | 34 | $0.00 | 信息 | 开发者群体 |
| strava club | 140 | 30 | $0.46 | 信息 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|-----|-----|------|------|
| opentracks | 390 | 27 | $0.65 | 信息 | ⭐ 有量+低 KD，Android GPS 录制 |
| endurain | 40 | 11 | $0.00 | 信息 | ⭐ 极低 KD，自托管核心词 |
| open source fitness tracker | 70 | 35 | $0.00 | 信息 | ⭐ |
| open source strava alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ GEO 级 |
| self hosted strava alternative | 20 | 0 | $0.00 | 信息 | ⭐⭐ GEO 级 |
| self hosted fitness tracking | 20 | 0 | $0.00 | 信息 | ⭐⭐ GEO 级 |
| open source running app | 20 | 0 | $0.00 | 信息 | ⭐⭐ GEO 级 |
| strava data export | 20 | 0 | $0.00 | 信息 | ⭐⭐ 数据迁移意图 |
| strava data privacy | 20 | 0 | $0.00 | 信息 | ⭐⭐ 隐私焦虑词 |
| fittrackee | 0 | 0 | $1.05 | — | 有 CPC 说明有付费竞争，近零量 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Strava 是"社交锁定 + 订阅收费 + 你的 GPS 数据喂它的 AI"三件套——Olares 上的 Endurain 把这三件事全颠倒：数据自托管、路线分析本地跑、$0 订阅费。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|-----|-----|-------------|--------|
| strava alternative | 140 | 14 | $1.14 | Endurain on Olares = 自托管 Strava 替代，一键部署，$0/年 vs $79.99 | ⭐⭐⭐ |
| strava alternatives | 70 | 10 | $0.00 | 同上，变体词并入同一文章 | ⭐⭐⭐ |
| open source strava alternative | 20 | 0 | $0.00 | Endurain (AGPL v3) 在 Olares Market = 精准命中 | ⭐⭐⭐ |
| self hosted strava alternative | 20 | 0 | $0.00 | 同上 | ⭐⭐⭐ |
| opentracks | 390 | 27 | $0.65 | OpenTracks（Android）本地录制 → 同步到 Olares 上的 Endurain，构成完整自托管链路 | ⭐⭐⭐ |
| endurain | 40 | 11 | $0.00 | Endurain 部署教程/Olares 一键安装指南 | ⭐⭐⭐ |
| strava vs garmin | 480 | 29 | $0.00 | Garmin 数据可直接同步到 Endurain/Olares，跳过 Strava 订阅 | ⭐⭐ |
| garmin connect vs strava | 90 | 8 | $0.00 | 同上，三角对比：Garmin + Olares Endurain vs Strava Premium | ⭐⭐ |
| strava vs nike run club | 320 | 26 | $0.00 | 第三选项：自托管 Olares 不绑任何平台 | ⭐⭐ |
| is strava premium worth it | 480 | 29 | $0.00 | $79.99/年 vs 部署 Endurain 一次性成本（$0 订阅）= 痛点对比 | ⭐⭐⭐ |
| cancel strava subscription | 140 | 21 | $0.00 | 取消后去哪里？Endurain on Olares + 数据迁移教程 | ⭐⭐⭐ |
| strava data export | 20 | 0 | $0.00 | 导出 Strava 历史 → 批量导入 Endurain（FIT/GPX 支持）| ⭐⭐⭐ |
| open source fitness tracker | 70 | 35 | $0.00 | Endurain 是最接近 Strava 体验的开源自托管选项 | ⭐⭐⭐ |
| how to delete strava account | 720 | 29 | $0.00 | 删账号前先导出数据 → 迁移到 Endurain on Olares | ⭐⭐ |
| self hosted fitness tracking | 20 | 0 | $0.00 | Olares = 最简单的自托管健身数据平台（无需 VPS 配置）| ⭐⭐⭐ |
| strava data privacy | 20 | 0 | $0.00 | Olares 数据留在自己设备，GPS 路线不上云、不喂训练 AI | ⭐⭐⭐ |
| does strava cost money | 320 | 29 | $1.57 | 有 CPC，付费疑虑词，切入点：$0 自托管替代 | ⭐⭐ |
| free running apps | 1,600 | 31 | $0.85 | ⭐ 自托管 = 永久免费，Olares 一键部署 Endurain | ⭐⭐ |
| strava heatmap alternative | 20 | 0 | $0.00 | Endurain 本地 Heatmap 功能 + Olares 本地存储 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|-----|-----|------|------|--------------------------|
| strava alternative | 140 | 14 | $1.14 | 信息 | **主词候选** | 低 KD + 有 CPC（$1.14）表明高商业价值；Olares/Endurain 精准命中；簇合计（+alternatives+free+cycling+running 等变体）≈ 500+，撑一篇 |
| strava alternatives | 70 | 10 | $0.00 | 信息 | 次级（并入 strava alternative 文章）| 同族变体，KD 10，并入主篇 |
| strava vs garmin | 480 | 29 | $0.00 | 信息 | **主词候选** | 480 月量 + KD 29，三角对比文（Strava/Garmin/Olares Endurain）有撑头的量 |
| garmin connect vs strava | 90 | 8 | $0.00 | 信息 | 次级 | KD 极低，并入 vs garmin 对比文 |
| strava vs nike run club | 320 | 26 | $0.00 | 信息 | **主词候选** | 320 量 + KD 26，"三选一"对比机会（+ Olares 自托管第三选项）|
| nike run club vs strava | 170 | 26 | $0.00 | 信息 | 次级 | 同簇变体，并入 strava vs nike run club 文章 |
| is strava premium worth it | 480 | 29 | $0.00 | 信息 | **主词候选** | 480 量，强烈的付费疑虑意图，完美 Olares 切入（$0 自托管对比） |
| opentracks | 390 | 27 | $0.65 | 信息 | **主词候选** | 390 量 + KD 27，OpenTracks 自身有搜索量；可写"OpenTracks + Endurain + Olares 完整自托管跑步追踪"教程 |
| strava cost | 1,300 | 33 | $0.03 | 信息 | **主词候选** | 高量（1,300）！KD 33 偏高但非不可攻；与 is strava free（2,900）、strava pricing（1,000）组成付费疑虑大簇（总量 5,000+）|
| is strava free | 2,900 | 32 | $1.36 | 信息 | **主词候选** | 最高量非品牌信息词，CPC $1.36，与 strava cost 同簇 |
| endurain | 40 | 11 | $0.00 | 信息 | 次级 | KD 11，小量但极低竞争；Olares 部署教程可拿 Featured Snippet |
| cancel strava subscription | 140 | 21 | $0.00 | 信息 | 次级 | 退出意图强，KD 21，并入替代文"取消后迁移到 Endurain" |
| how to delete strava account | 720 | 29 | $0.00 | 信息 | 次级 | 720 量 + KD 29，退出漏斗词，"删除前先导出数据"切入 |
| open source fitness tracker | 70 | 35 | $0.00 | 信息 | 次级 | 70 量，KD 35 偏高但 Olares/Endurain 精准，纳入自托管文章 |
| strava data export | 20 | 0 | $0.00 | 信息 | GEO | 近零量，但语义精准——数据迁移起点；Endurain 支持 FIT/GPX 批量导入，抢 AI Overview/Perplexity 引用 |
| self hosted strava alternative | 20 | 0 | $0.00 | 信息 | GEO | 语义与 Olares 完美对齐，进文章 FAQ 抢引用位 |
| open source strava alternative | 20 | 0 | $0.00 | 信息 | GEO | 同上 |
| self hosted fitness tracking | 20 | 0 | $0.00 | 信息 | GEO | 同上，进自托管文 FAQ |
| strava data privacy | 20 | 0 | $0.00 | 信息 | GEO | 隐私焦虑词，进"为什么自托管运动数据"文章 FAQ |
| strava heatmap alternative | 20 | 0 | $0.00 | 信息 | GEO | 进 Endurain/Olares Heatmap 功能对比段 |
| does strava cost money | 320 | 29 | $1.57 | 信息 | 次级 | CPC $1.57 是异常值（第三方广告主在买），量 320，并入付费疑虑大簇 |
| strava vs apple fitness | 140 | 22 | $0.00 | 信息 | 次级 | 并入 vs 对比文族 |

---

## 核心洞见

### 1. 品牌护城河：无法正面刚，但退出意图词可绕开

strava 品牌词 KD 80-98，160,800 月流量全是导航词——不可能抢。但品牌的护城河本质来自"分段排行榜社区"，而非搜索词优势。**可攻击的是品牌外圈**：退出词（how to delete strava account 720/KD29、cancel strava subscription 140/KD21）、付费疑虑词（is strava premium worth it 480/KD29）、替代词（strava alternative 140/KD14）。这些词 Strava 官方很难防守（它不可能写"怎么取消我的订阅"然后自荐替代方案）。

### 2. 可复制的打法：工具页 + 内容矩阵

Strava 的非品牌流量几乎全来自**配速计算器工具页**（pace calculator 74K、marathon pace chart 18K、trail running routes near me 14.8K）——这是"工具型内容带自然量"的教科书案例。另一个值得关注的是 **support.strava.com** 贡献 7.2% 流量，说明"如何连接 Garmin 到 Strava"类型的帮助文章（1,300 月量）流量可观且 KD 低——**教程类内容是低 KD 切入口**。

### 3. 对 Olares 最关键的词

**A. `strava alternative`（140/KD14/$1.14 CPC）**——核心攻击词。KD 仅 14，有广告主 CPC（$1.14）证明商业价值；变体族（alternatives + free + cycling + running + open source 等）合计 500+ 月量，撑一篇替代文。Olares 上的 Endurain 是唯一能提供"完整 Strava 体验 + 数据自主"的自托管选项。

**B. `is strava premium worth it` + `strava cost` 疑虑簇**——总月量 5,000+（strava cost 1,300 + is strava free 2,900 + strava pricing 1,000 + is strava premium worth it 480 + does strava cost money 320），KD 29-38 区间。这类词的用户正在**主动权衡是否付钱**——Olares 自托管 = 永久 $0 是最有力的反论点。

**C. `opentracks`（390/KD27）**——最大的"低量有效词"。OpenTracks 是 MIT 许可的 Android GPS 录制 app，本身没有后端；与 Endurain（Olares 上的后端）组合成"手机录制 → 自托管服务器存储分析"完整链路，教程类文章可拿 Featured Snippet。

### 4. 最大攻击面：订阅涨价 + API 收费 + 数据主权焦虑

- **2024-2025 API 双收紧**：先禁止第三方展示用户数据给他人（2024.11），再向开发者收 $11.99/月 API 费（2025）——用户搜索 `strava api` 1,300 月量，开发者生态不满持续发酵。
- **免费层收窄**：Group Challenges（2024.8 移至付费）是外部公开批评热点，推动 `strava alternative free`、`free strava alternatives` 搜索量出现。
- **数据主权**：用户 GPS 路线全存 Strava 服务器，按新 API 条款 Strava 禁止第三方用于 AI 训练——**但 Strava 自己的 AI（Athlete Intelligence）在用这些数据**。这个双标是隐私叙事的核心矛盾点。Olares 的"GPS 数据留在自己的硬件、路线分析本地跑"是直接反论。

### 5. 隐藏低 KD 金矿

- `garmin connect vs strava`（90/KD8）——竟然只有 KD 8，几乎没有竞争。Garmin 用户是 Strava 最大用户群之一（直接 API 同步），这个比较词是"Garmin 用户犹豫是否付 Strava 订阅"的关键时刻。
- `strava data export`（20/KD0）——近零量但零竞争，"如何从 Strava 导出所有 GPS 数据并迁入 Endurain"是数据迁移教程的完美 FAQ 锚点。
- `endurain`（40/KD11）——Endurain 本身搜索量低但极低竞争，早期占领有利于等项目增长后受益。

### 6. GEO 前瞻布局（抢 AI Overview / Perplexity 引用位）

以下词近零量但语义精准，进文章 FAQ 或独立段落，争取被 AI 问答引用：

- **"self hosted strava alternative"** — Endurain + OpenTracks + Olares 三者组合的精准描述
- **"open source fitness tracker self hosted"** — Olares Market 上线 Endurain 后的标准答案
- **"strava data privacy concerns"** — Strava 新 API 条款"禁第三方用于 AI 训练但自家在用"的矛盾
- **"how to migrate from strava to self hosted"** — 完整迁移教程（FIT 导出 → Endurain 批量导入）
- **"endurain olares"** — 品牌+平台词，早期内容可抢引用位

### 7. 与既有分析的关联

- **olares-500-keywords** 中无 Strava 相关词——本报告为新增词域，零重叠。
- **iot.md 已有条目**（第 38 行）：Strava ⬜ 待调研，本报告完成此条目。
- 与 **health-platforms 调研**联动：Apple HealthKit / Google Health 的数据导出词（export apple health data）与 strava data export 同属"退出 + 数据迁移"词族，可联合建立"健身数据主权"内容集群。
- `opentracks`（390/KD27）与 `gadgetbridge`（已在 iot.md 中提及为 Garmin 替代）构成"开源运动硬件+软件完整自托管栈"叙事——共同支撑 Olares 的健身数据主权定位。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；健康/生活方式类产品全球量通常为美国的 3-5 倍。*
