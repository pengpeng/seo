# Roku SEO 竞品分析报告

> 域名：roku.com | SEMrush US | 2026-07-06
> 北美 #1 流媒体 TV OS 与设备品牌；商业模式以广告平台为核，ACR（自动内容识别）是核心隐私攻击面，Jellyfin + Apple TV 4K 是唯一无 ACR 的私有化平替路径。

---

## 项目理解（前置）

Roku 是美国最大的流媒体 TV 操作系统与设备品牌，2002 年创立，2017 年纳斯达克上市（NASDAQ: ROKU）。它的商业模式以"平台"为核心——硬件（Streaming Stick / Ultra / Roku TV）是获客渠道，真正的利润来自广告（The Roku Channel、Roku Ads Manager）和订阅分成。FY2025 总营收 $47.4 亿，其中 Platform 段占比 ~87%，设备段几近保本。100M 全球流媒体家庭、北美 CTV 设备 36% 市场份额（Pixalate Q1 2026 SOV），是广告主进入客厅的最大单一入口。

**核心隐私痛点**：ACR（Automatic Content Recognition）在开启时约每 500ms 截帧指纹，识别天线直播、cable box、HDMI 设备上的内容，用于广告定向。ACR 是"opt-in"，但即便关闭，Roku 仍收集用户在流媒体应用、The Roku Channel、主屏幕的完整互动和观看数据。使用 Roku 必须注册账号并激活设备，数据不可回避。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 北美 #1 流媒体 TV OS；广告平台是主业，硬件是获客工具 |
| 开源 / 许可证 | 闭源；Roku OS 不开放；Channel SDK 有开放文档但不开源 |
| 主仓库 | 无官方开源仓库；开发者 SDK 文档：developer.roku.com |
| 核心功能 | 流媒体设备 OS（Streaming Stick / Ultra / Roku TV）、The Roku Channel（免费+付费内容）、Channel Store（500+ 频道）、Roku Smart Home（安防摄像头）、Roku Ads Manager（B2B 广告平台）、ACR 数据变现 |
| 商业模式 / 定价 | 硬件 $29–$99（设备端）；平台收入：CTV 广告收入分成 + 订阅分成（Netflix/Hulu/Disney+ 等） |
| 差异化 / 价值主张 | 北美最大 CTV 广告库存；中立第三方平台（不推自家订阅）；免费内容（The Roku Channel）；简单易用的 UI |
| 主要竞品（初判）| Amazon Fire TV、Google TV（Android TV）、Samsung Tizen OS、LG webOS、Apple TV 4K |
| Olares Market | Roku 本身不可自托管；**Jellyfin**（开源媒体服务器，✅ 已上架，[报告](/Users/pengpeng/seo/directions/market/reports/jellyfin.md)）是核心私有化平替 |
| 来源 | roku.com/what-is-roku、developer.roku.com/docs/features-overview、Parks Associates 2026-04-22、Pixalate Q1 2026 CTV、docs.roku.com/api/v1/published/userprivacypolicy/en/us |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | roku.com |
| SEMrush Rank | #573 |
| 自然关键词数 | 1,320,850 |
| 月自然流量（US）| 4,798,827 |
| 自然流量估值 | $5,280,616/月 |
| 付费关键词数 | 1,753 |
| 月付费流量 | 113,626 |
| 月付费花费 | $669,281 |
| 排名 1-3 位 | 51,140 词 |
| 排名 4-10 位 | 162,438 词 |
| 排名 11-20 位 | 256,642 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 月流量 | 占比 |
|--------|---------|------|------|
| www.roku.com | 702,563 | 3,214,566 | 67.0% |
| therokuchannel.roku.com | 316,535 | 611,040 | 12.7% |
| support.roku.com | 142,679 | 550,490 | 11.5% |
| channelstore.roku.com | 125,565 | 286,261 | 6.0% |
| my.roku.com | 7,364 | 67,035 | 1.4% |
| developer.roku.com | 7,951 | 13,260 | 0.3% |
| photostreams.roku.com | 275 | 12,657 | 0.3% |
| newsroom.roku.com | 4,339 | 8,097 | 0.2% |
| advertising.roku.com | 1,566 | 5,212 | 0.1% |

**关键观察**：
- The Roku Channel（12.7%）和 Channel Store（6.0%）合计近 20% 流量——内容发现是仅次于主站的第二大流量柱。
- support.roku.com 11.5%：大量 "how to…" 和客服词（如 roku remote not working）说明用户操作摩擦高，是竞争文章的切入点。
- advertising.roku.com 流量极小但极具战略价值——Roku 在此用付费广告高价狙击广告主（详见付费词）。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| roku | 1 | 1,000,000 | 74 | $0.53 | 800,000 | 导航 | /roku.com/ |
| roku tv | 1 | 246,000 | 48 | $0.27 | 196,800 | 导航/商业 | /roku.com/ |
| roku remote | 1 | 201,000 | 44 | $0.66 | 160,800 | 商业 | /products/accessories |
| roku channel | 1 | 165,000 | 77 | $1.92 | 132,000 | 导航 | therokuchannel.roku.com/ |
| roku login | 1 | 165,000 | 41 | $2.00 | 132,000 | 导航 | /roku.com/ |
| roku account | 1 | 165,000 | 51 | $2.62 | 132,000 | 导航 | support.roku.com/manage-account |
| thetvapp | 6 | 1,000,000 | 41 | $2.03 | 30,000 | 信息 | channelstore/thetvapp |
| tvapp | 8 | 1,220,000 | 47 | $1.74 | 29,280 | 信息 | channelstore/thetvapp |
| rolu（误拼） | 1 | 27,100 | 63 | $0.53 | 21,680 | 导航 | /roku.com/ |
| roku tv remote | 1 | 27,100 | 44 | $0.81 | 21,680 | 商业 | /mobile-app |
| the tv app | 4 | 301,000 | 38 | $2.03 | 19,565 | 信息 | channelstore/thetvapp |
| roku customer service number | 1 | 22,200 | 58 | $2.60 | 17,760 | 信息/导航 | /about/contact |
| roku customer service | 1 | 18,100 | 47 | $2.45 | 14,480 | 信息/导航 | /about/contact |
| paramount plus | 9 | 2,740,000 | 93 | $2.24 | 13,700 | 导航 | channelstore/paramount-plus |
| roku channel store | 1 | 14,800 | 52 | $2.36 | 11,840 | 导航 | channelstore.roku.com/ |
| roku streaming device | 1 | 9,900 | 76 | $0.25 | 7,920 | 商业 | /products/players |
| roku smart tv | 1 | 8,100 | 54 | $0.22 | 6,480 | 商业 | /products/roku-tv |
| roku live tv | 1 | 8,100 | 57 | $1.79 | 6,480 | 信息 | therokuchannel/live-tv |
| roku smart home | 1 | 5,400 | 44 | $0.24 | 4,320 | 商业 | /products/smart-home |
| roku photo streams | 1 | 5,400 | 35 | $3.93 | 4,320 | 信息 | photostreams.roku.com/ |

**关键观察**：
- `thetvapp`/`tvapp`（合计超 2,200,000 月量！）是 Roku Channel Store 意外截到的超大流量词，说明第三方内容聚合页可以骑大词——这正是程序化落地页策略的极致体现。
- 误拼变体（rolu/ruku/roko）均排 #1，品牌防御无死角。
- 客服词占 5 条前 20，说明用户操作摩擦大（setup/remote/account/billing 问题频繁），是"第三方教程 + 平替引导"页面的自然切入点。

### 付费词（Google Ads）

Roku 的 Google Ads 策略分两条完全不同的线：

**1. newsroom.roku.com（异常）**：Top paid 词 "roku"（1M）、"roku tv"（246K）、"roku remote"、"roku ultra"、"roku streaming stick" 等均指向 newsroom.roku.com 搜索结果页，URL 含 `+1-844-314-4198 For Roku Support` 字样——这是 **广告欺诈（tech support scam）劫持了 Roku newsroom 子域名的 SEO/SEM**，Roku 自身未授权此类广告，需排除。

**2. advertising.roku.com（核心战略）**：真正的付费投放面向 **B2B 广告主**。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| advertisement | 110,000 | $11.89 | /solutions/advertise/ads-manager |
| ctv | 27,100 | $14.58 | /solutions/advertise/ads-manager |
| youtube ads | 12,100 | $39.11 | /solutions/advertise/ads-manager |
| bing ads | 12,100 | $67.49 | /solutions/advertise/ads-manager |
| microsoft ads | 12,100 | $50.78 | /solutions/advertise/ads-manager |
| facebook ads | 40,500 | $23.36 | /solutions/advertise/ads-manager |
| linkedin ads | 9,900 | $25.50 | /solutions/advertise/ads-manager |
| tiktok ads manager | 22,200 | $25.01 | /solutions/advertise/ads-manager |
| roku city | 14,800 | $0 | /ad-types/destinations/roku-city |

**洞见**：Roku 花费约 $669K/月的付费预算，几乎全部用于抢夺"打算在 YouTube/Facebook/TikTok 投广告"的品牌主，告诉他们"CTV 比社交媒体更有效"——这是一个极度聪明的 B2B 获客策略，跟消费者关系不大。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| roku vs fire stick | 2,400 | 38 | $0.15 | 信息 | 最大对比词 |
| roku vs apple tv | 1,600 | 22 ⭐ | $0.09 | 信息 | 低 KD，Apple TV = 无 ACR 平替切入 |
| roku alternatives | 590 | 37 | $0.22 | 信息 | 核心平替词 |
| roku vs chromecast | 590 | 15 ⭐ | $0.10 | 信息 | 极低 KD |
| fire stick alternative | 260 | 22 ⭐ | $0.33 | 信息 | 跨平替（与 Roku 同类）|
| apple tv 4k vs roku | 140 | 26 ⭐ | $0.07 | 信息 | 直接切入 ACR 隐私叙事 |
| roku alternative | 140 | 57 | $0.22 | 信息 | 单数变体，KD 偏高 |
| is roku worth it | 140 | 50 | $0.16 | 信息 | 用户决策词 |
| plex vs roku | 20 | 0 ⭐ | $0 | — | GEO 前哨 |
| jellyfin vs roku | 0 | 0 | $0 | — | GEO 前哨，搜索量尚未成型 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| best streaming device | 6,600 | 56 | $0.31 | 商业 | 品类主词 |
| streaming box | 6,600 | 43 | $0.42 | 商业 | 品类 |
| streaming stick | 3,600 | 63 | $0.41 | 商业 | 品类 |
| cord cutting | 2,900 | 24 ⭐ | $1.23 | 信息 | 剪线族进入点，KD 低 |
| streaming media player | 1,900 | 45 | $0.38 | 商业 | 品类 |
| best streaming stick | 1,300 | 53 | $0.31 | 商业 | 品类 |
| cord cutter | 1,300 | 74 | $1.00 | 信息 | 品类 |
| ad free streaming | 720 | 69 | $0.97 | 信息 | 隐私/厌广意图 |
| streaming without subscription | 40 | 54 | $0 | 信息 | 免费流媒体 |
| streaming without ads | 20 | 0 ⭐ | $1.59 | 信息 | 低竞争，高 CPC 暗示强商业意图 |
| smart tv without ads | 50 | 27 ⭐ | $0 | 信息 | 直接隐私痛点 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| plex | 450,000 | 93 | $0.78 | 导航 | 自托管媒体生态大词（非 Roku 品牌但高度相关）|
| jellyfin | 49,500 | 76 | $3.48 | 导航 | Roku 平替生态主词 |
| kodi | 40,500 | 84 | $0.18 | 导航 | 老牌开源播放器 |
| emby | 14,800 | 59 | $0 | 导航 | Jellyfin 原型 |
| jellyfin server | 3,600 | 64 | $1.81 | 信息 | 部署主词 |
| jellyfin vs plex | 4,400 | 32 | $0 | 信息 | 自托管两大阵营对比 |
| plex media server | 22,200 | 47 | $0.48 | 信息 | Plex 部署主词 |
| plex vs jellyfin | 2,400 | 27 ⭐ | $0 | 信息 | 低 KD，高量 |
| jellyfin apple tv | 1,300 | 48 | $0 | 信息 | Jellyfin 客户端词 |
| roku photo streams | 5,400 | 35 | $3.93 | 信息/商业 | Roku 自家功能（高 CPC 异常）|
| roku acr | 50 | 26 ⭐ | $0 | 信息 | ACR 隐私核心词 |
| roku privacy settings | 50 | 39 | $0 | 信息 | 隐私设置词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| plex alternative | 1,600 | 33 | $0 | 信息 | 自托管生态门户词 |
| home media server | 1,300 | 31 | $0.53 | 信息 | 家庭服务器部署 |
| emby vs jellyfin | 880 | 11 ⭐ | $0 | 信息 | KD 极低，高价值对比词 |
| jellyfin roku | 880 | 39 | $0 | 信息 | Jellyfin 跑在 Roku 上 |
| jellyfin vs emby | 480 | 12 ⭐ | $0 | 信息 | KD 极低 |
| jellyfin android tv | 390 | 43 | $0 | 信息 | Jellyfin 客户端 |
| jellyfin alternative | 210 | 33 | $0 | 信息 | 平替词 |
| plex nas | 720 | 50 | $0.35 | 信息 | NAS 部署 |
| nas media server | 260 | 15 ⭐ | $1.05 | 商业 | 极低 KD，高 CPC |
| jellyfin nas | 110 | 23 ⭐ | $0 | 信息 | 低 KD，NAS 场景 |
| open source media server | 110 | 25 ⭐ | $0 | 信息 | 低 KD |
| jellyfin on raspberry pi | 140 | 16 ⭐ | $0 | 信息 | 极低 KD，家用部署 |
| kodi alternative | 140 | 13 ⭐ | $0 | 信息 | KD 最低之一 |
| self hosted media server | 70 | 45 | $0 | 信息 | 精准词 |
| stream from nas | 70 | 13 ⭐ | $0.41 | 信息 | 极低 KD |
| private streaming | 90 | 9 ⭐ | $2.15 | 信息 | KD=9！高 CPC，语义精准 |
| streaming media server | 170 | 39 | $2.51 | 信息 | 高 CPC 暗示商业价值 |
| cord cutting guide | 50 | 23 ⭐ | $0 | 信息 | 低竞争入门词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Roku = ACR + 强制账号 + 广告追踪；Jellyfin on Olares + Apple TV 4K = 数据不出门、无内容指纹、无平台账号、媒体库完全自主——这是对 Roku 商业模式的根本性替代，而非功能缺失的妥协方案。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| plex | 450,000 | 93 | $0.78 | ⭐⭐ 品牌词不可抢，但 Plex 用户迁 Jellyfin on Olares 的需求真实（Plex 引入 Plexpass 付费墙后） |
| jellyfin | 49,500 | 76 | $3.48 | ⭐⭐⭐ Olares Market 已上架，一键部署 Jellyfin 服务器；搜索量=49,500，远超所有平替词 |
| kodi | 40,500 | 84 | $0.18 | ⭐⭐ Kodi 用户是最成熟的自托管受众，可内容引导至 Jellyfin on Olares |
| emby | 14,800 | 59 | $0 | ⭐⭐ Emby 商业化后流失用户，Jellyfin（Emby fork）是直接受益者 |
| jellyfin server | 3,600 | 64 | $1.81 | ⭐⭐⭐ 核心部署词，内容主线：Olares 一键跑 Jellyfin 服务器，无需手动配置 |
| jellyfin vs plex | 4,400 | 32 | $0 | ⭐⭐⭐ KD32 高量对比词；叙事：Jellyfin on Olares = 免费+无隐私妥协 |
| roku vs fire stick | 2,400 | 38 | $0.15 | ⭐⭐ 引流词：两者都有 ACR，真正的隐私选项是 Apple TV 4K + Jellyfin on Olares |
| plex vs jellyfin | 2,400 | 27 | $0 | ⭐⭐⭐ KD27 低，量大；Olares 角度：Jellyfin 零付费墙，Olares 提供服务端 |
| roku vs apple tv | 1,600 | 22 | $0.09 | ⭐⭐⭐ KD22 极低！Apple TV 4K = 无 ACR，搭配 Jellyfin on Olares 构成完整私有方案 |
| plex alternative | 1,600 | 33 | $0 | ⭐⭐⭐ 平替词，Jellyfin on Olares 是当前最主流答案 |
| home media server | 1,300 | 31 | $0.53 | ⭐⭐⭐ 信息意图，Olares 一键变家庭媒体服务器 |
| jellyfin apple tv | 1,300 | 48 | $0 | ⭐⭐⭐ 核心搭档词：Jellyfin server on Olares + Apple TV 4K 客户端 = 完整方案 |
| emby vs jellyfin | 880 | 11 | $0 | ⭐⭐⭐ KD=11，极低竞争！Olares 可收割 Emby 迁移流量 |
| jellyfin roku | 880 | 39 | $0 | ⭐⭐ Roku 用户已在寻找 Jellyfin，说明平替需求存在 |
| plex nas | 720 | 50 | $0.35 | ⭐⭐ NAS 场景迁移词，Olares 替代 Synology/Unraid 跑 Plex |
| cord cutting | 2,900 | 24 | $1.23 | ⭐⭐ KD24 入门词；剪线用户是 Olares 精准受众（拒绝订阅经济） |
| jellyfin vs emby | 480 | 12 | $0 | ⭐⭐⭐ KD=12，超低竞争 |
| nas media server | 260 | 15 | $1.05 | ⭐⭐⭐ KD=15，CPC=$1.05，商业意图，Olares One 直接满足 |
| jellyfin on raspberry pi | 140 | 16 | $0 | ⭐⭐ KD=16，Olares 跑在 RPi 上也可（script 路径） |
| kodi alternative | 140 | 13 | $0 | ⭐⭐⭐ KD=13！Olares Market 一键装 Jellyfin/Plex 替代 Kodi |
| jellyfin nas | 110 | 23 | $0 | ⭐⭐⭐ KD=23，NAS 场景，Olares 是 Jellyfin NAS 的最佳容器 |
| open source media server | 110 | 25 | $0 | ⭐⭐⭐ 语义精准，Olares + Jellyfin 是教科书式答案 |
| roku vs chromecast | 590 | 15 | $0.10 | ⭐⭐ KD=15，对比词，三者中只有 Apple TV 4K 无 ACR |
| stream from nas | 70 | 13 | $0.41 | ⭐⭐⭐ KD=13，NAS 流媒体，Olares One 场景完美匹配 |
| private streaming | 90 | 9 | $2.15 | ⭐⭐⭐ **KD=9，全批最低！** CPC=$2.15 暗示真实商业意图，Olares 核心定位词 |
| smart tv without ads | 50 | 27 | $0 | ⭐⭐⭐ 隐私痛点精准词，叙事：Apple TV 4K + Jellyfin = 广告零侵扰 |
| roku acr | 50 | 26 | $0 | ⭐⭐⭐ ACR 关键词，搜索者已有隐私意识，最精准的 Olares 目标用户前哨 |
| streaming without ads | 20 | 0 | $1.59 | ⭐⭐ GEO 前哨：零 KD，高 CPC，值得占位 |
| jellyfin vs roku | 0 | 0 | $0 | ⭐⭐⭐ GEO 前哨：搜索量尚未成型但语义最精准；主动创建对比内容抢 AI 引用位 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| jellyfin | 49,500 | 76 | $3.48 | 导航 | 次级 | 品牌词不可抢；但 Olares Market 一键部署语境下可借力做"Jellyfin on Olares"系列页面 |
| best streaming device | 6,600 | 56 | $0.31 | 商业 | 次级 | KD56 偏高但量大；可在"best streaming device without tracking"变体中嵌入 |
| streaming box | 6,600 | 43 | $0.42 | 商业 | 次级 | 品类词，与 Roku 同竞争格局，可做硬件对比 |
| jellyfin vs plex | 4,400 | 32 | $0 | 信息 | 主词候选 | KD32、量 4,400，Ollares 的服务端叙事天然嵌入 |
| cord cutting | 2,900 | 24 | $1.23 | 信息 | 主词候选 | KD24，剪线族是 Olares 精准受众，可做"完全剪线指南：Jellyfin + Apple TV 4K" |
| roku vs fire stick | 2,400 | 38 | $0.15 | 信息 | 主词候选 | 量大，可楔入"两者都有 ACR，真正无追踪选项"叙事 |
| plex vs jellyfin | 2,400 | 27 | $0 | 信息 | 主词候选 | KD27，量合计（vs jellyfin vs plex）近 7K，是最大自托管对比词群 |
| roku vs apple tv | 1,600 | 22 | $0.09 | 信息 | 主词候选 | **KD=22，最佳 Roku 对比词**；切入 Apple TV 4K（无 ACR）+ Jellyfin on Olares |
| plex alternative | 1,600 | 33 | $0 | 信息 | 主词候选 | Plex 付费墙迁移词，Ollares Jellyfin 直接承接 |
| home media server | 1,300 | 31 | $0.53 | 信息 | 主词候选 | KD31，高意图，Olares One = 即插即用家庭媒体服务器 |
| jellyfin apple tv | 1,300 | 48 | $0 | 信息 | 次级 | Jellyfin + Apple TV 4K 方案词，嵌入对比文 |
| emby vs jellyfin | 880 | 11 | $0 | 信息 | 主词候选 | **KD=11，最低 KD 主词**！Emby 迁移词，Olares 跑 Jellyfin 收割 |
| jellyfin vs emby | 480 | 12 | $0 | 信息 | 次级 | KD=12，与 emby vs jellyfin 并入同一篇 |
| plex nas | 720 | 50 | $0.35 | 信息 | 次级 | NAS 部署词，Olares One 场景 |
| nas media server | 260 | 15 | $1.05 | 商业 | 主词候选 | KD=15，CPC=$1.05，商业意图；Olares One = 家庭 NAS + AI 媒体服务器 |
| roku alternatives | 590 | 37 | $0.22 | 信息 | 主词候选 | 核心平替词，量 590，可写"Best Roku Alternatives Without Tracking" |
| cord cutting guide | 50 | 23 | $0 | 信息 | 次级 | KD=23，嵌入剪线文章 |
| kodi alternative | 140 | 13 | $0 | 信息 | 主词候选 | KD=13！可独立写"Best Kodi Alternatives"收割旧版 Kodi 用户迁移需求 |
| open source media server | 110 | 25 | $0 | 信息 | 次级 | KD=25，嵌入 Jellyfin/Olares 教程文 |
| jellyfin nas | 110 | 23 | $0 | 信息 | 次级 | KD=23，NAS 场景词 |
| stream from nas | 70 | 13 | $0.41 | 信息 | 次级 | KD=13，Olares 场景精准 |
| private streaming | 90 | 9 | $2.15 | 信息 | 主词候选 | **KD=9，整批最低！** CPC=$2.15，Olares "Own Your AI" 叙事直接落地词 |
| smart tv without ads | 50 | 27 | $0 | 信息 | 次级 | 隐私痛点词，并入对比文 |
| roku acr | 50 | 26 | $0 | 信息 | 次级 | 精准隐私词，指向已有意识的用户 |
| apple tv 4k vs roku | 140 | 26 | $0.07 | 信息 | 次级 | ACR 对比词，Apple TV 4K 是推荐方案组件 |
| jellyfin vs roku | 0 | 0 | $0 | — | GEO | 尚无搜索量，主动创建对比内容，抢 AI Overview 引用位 |
| plex vs roku | 20 | 0 | $0 | — | GEO | 同上，GEO 前哨 |
| streaming without ads | 20 | 0 | $1.59 | 信息 | GEO | 零 KD，CPC 高，值得布局 |

---

## 核心洞见

1. **品牌护城河**：极强，不可正面刚。`roku` 单词 100 万月量，全部核心品牌词（roku tv / roku remote / roku login / roku account）均排名 #1 且 KD 40-80。品牌词护城河=无法破坏，唯一可切入的路径是"Roku + 痛点词（ACR / ads / tracking / alternative）"和"平替生态词（Jellyfin / Apple TV / cord cutting）"。

2. **可复制的打法**：Roku 最大的非品牌流量是 **Channel Store 程序化落地页**（`thetvapp`/`tvapp` 合计超百万量、`paramount plus`/`2 broke girls` 等大词被 channelstore 页截获）——这正是 **Olares Market 应用详情页可复制的模板**：每个应用/频道一页，吃"X on Roku / X streaming"类词。另外 support.roku.com 大量 how-to 词（`roku remote not working` 33K）是第三方教程的天然机会。

3. **对 Olares 最关键的 3 个词**：
   - `private streaming`（**KD=9**，CPC=$2.15）：全批最低 KD，语义最精准；
   - `emby vs jellyfin`（**KD=11**）/ `jellyfin vs emby`（**KD=12**）：超低竞争，大量 Emby 迁移用户是 Jellyfin on Olares 的精准受众；
   - `roku vs apple tv`（KD=22，量 1,600）：切入 ACR 隐私叙事的最优对比词，Apple TV 4K（无 ACR）+ Jellyfin on Olares = 完整方案。

4. **最大攻击面**：**ACR 数据变现 + 强制账号**。Roku 的核心商业模式依赖持续收集用户观看数据——即使用户关闭 ACR，Roku 仍通过流媒体应用互动、主屏幕行为、广告曝光收集数据（来源：Roku Privacy Policy）。"No content fingerprinting, no Roku account required, your media stays yours"是 Jellyfin on Olares 的完整反叙事。2026 年另一攻击面：**Walmart 宣布在 Onn TV 上用 Vizio SmartCast OS 替换 Roku**，Roku OEM 渠道面临蚕食，用户信任度存疑。

5. **隐藏低 KD 金矿**：
   - `private streaming` KD=9、`kodi alternative` KD=13、`stream from nas` KD=13、`emby vs jellyfin` KD=11——这四个词量虽不大（10-880）但竞争几乎为零，且意图极精准（想自托管媒体的用户）；
   - `nas media server` KD=15，CPC=$1.05——有商业意图，量 260，Olares One 场景完美匹配；
   - `roku vs chromecast` KD=15——量 590，可在对比文中引导至无 ACR 方案；
   - `cord cutting` KD=24、量 2,900——剪线受众是 Olares 精准人群，切入点是"剪线但不让 Roku 追踪你"。

6. **GEO 前瞻布局**：
   - `jellyfin vs roku`（量=0）：是最语义精准的对比词，尚无成熟搜索量，主动创建对比内容可抢 Perplexity / AI Overview 引用位；
   - `streaming device without tracking` / `smart tv without acr` / `does roku acr work when tv off`：这类隐私意识词即将爆发（参考 Samsung Tizen 2026 年德州 ACR 和解新闻的流量效应），提前布局；
   - `ollares jellyfin` / `jellyfin olares`：Olares 自有品牌词，GEO 层抢占。

7. **与既有分析的关联**：
   - Jellyfin 已有 Olares Market 报告（[directions/market/reports/jellyfin.md](/Users/pengpeng/seo/directions/market/reports/jellyfin.md)），本报告补充了"Roku 平替"叙事维度，两份报告可交叉内链；
   - `cord cutting`（KD24/2,900）和 `home media server`（KD31/1,300）与方向 7（IoT 隐私）的"smart home without cloud"叙事完全一致；
   - Olares IoT iot.md 中 Apple TV 4K 已被标注为"唯一无 ACR 主流盒"，本报告提供了 `roku vs apple tv` 的关键词证据；
   - `nas media server`（KD=15）与 hardware 方向的 AI NAS 报告有交集，可在 NAS 对比文中一并覆盖。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、resource_adwords、phrase_these、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；IoT/流媒体类产品全球量通常为美国的 2-4 倍。*
*市场份额数据：Parks Associates Streaming Video Tracker 2026-04-22（Roku OS 28% US broadband households）；Pixalate Q1 2026 CTV Market Share Report（Roku 36% SOV 北美）。*
