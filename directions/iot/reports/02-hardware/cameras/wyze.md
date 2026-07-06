# Wyze SEO 竞品分析报告

> 域名：wyze.com | SEMrush US | 2026-07-06
> 美国最大预算安防摄像头品牌，$30 起的 Wi-Fi 摄像头 + 可选云订阅，核心竞争力是极低硬件定价与本地 microSD 录像。

---

## 项目理解（前置）

Wyze 由前亚马逊工程师于 2017 年创立，核心使命是"让普通家庭用上高端安防摄像头"。旗舰产品 Wyze Cam v4（$36）以 2.5K 分辨率和彩色夜视媲美百元以上竞品，并支持本地 microSD 录像（无需订阅）。商业变现靠可选的 Cam Plus 订阅（$2.99/月/台）解锁连续录制和 AI 检测，不订阅基础功能仍可用。Wyze 曾发生 2022/2024 两次安全/隐私事件，引发用户对云依赖的担忧——这正是 Olares 本地方案的进入窗口。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 全美最便宜的 Wi-Fi 安防摄像头，$30 起，订阅可选 |
| 开源 / 许可证 | 闭源商业产品；社区有 wz_mini_hacks（MIT）和 docker-wyze-bridge（MIT）两个第三方开源项目 |
| 主仓库 | 官方无开源仓库；[mrlt8/docker-wyze-bridge](https://github.com/mrlt8/docker-wyze-bridge)（社区，1.5k+ ★）；[gtxaspec/wz_mini_hacks](https://github.com/gtxaspec/wz_mini_hacks)（社区，2k+ ★） |
| 核心功能 | 2.5K HD 实时查看；本地 microSD 录像（无需订阅）；双向音频；AI 人物/车辆/宠物检测（Cam Plus 付费）；Alexa/Google Home 集成 |
| 商业模式 / 定价 | 硬件一次购买（$30–$100）+ 可选 Cam Plus 订阅（$2.99/月/台 或 $9.99/月无限台）；无强制订阅 |
| 差异化 / 价值主张 | 同级最低价；本地 microSD 兜底存储；最大优势就是价格——别的大品牌（Ring/Arlo）订阅贵 3-5 倍 |
| 主要竞品（初判）| Ring（亚马逊）、Blink（亚马逊）、Arlo、eufy（Anker）、Reolink |
| Olares Market | 未上架（Wyze 为闭源硬件）；但 **[Frigate NVR 已上架](../../../market/reports/frigate-nvr.md)**，是接入 Wyze 摄像头的后端 |
| 来源 | [wyze.com](https://www.wyze.com/)；[dumbswitches.com Wyze v4 评测](https://www.dumbswitches.com/wyze-cam-v4-review/)；[securitycompasshq.com](https://www.securitycompasshq.com/reviews/wyze)；[pvrblog.com](https://pvrblog.com/brands/wyze/)；GitHub wz_mini_hacks wiki |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | wyze.com |
| SEMrush Rank | 5,685 |
| 自然关键词数 | 76,052 |
| 月自然流量（US）| 413,454 |
| 自然流量估值 | $159,051 / 月 |
| 付费关键词数 | 0（无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 3,987 词 |
| 排名 4-10 位 | 8,920 词 |
| 排名 11-20 位 | 8,590 词 |

> Wyze 完全不投 Google Ads，靠品牌流量 + 自然 SEO 驱动获客，品牌词护城河极深。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.wyze.com | 23,928 | 336,184 | 81.3% |
| my.wyze.com | 253 | 32,904 | 8.0% |
| forums.wyze.com | 35,001 | 27,226 | 6.6% |
| support.wyze.com | 15,354 | 15,459 | 3.7% |
| global.wyze.com | 559 | 981 | 0.2% |
| ca.wyze.com | 918 | 404 | 0.1% |

> `forums.wyze.com` 收录 35,001 个关键词（约为主站的 1.5 倍），是大量用户故障排查、RTSP 配置、订阅取消讨论的落地点——也是 Olares 内容最容易切入的长尾场景。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| wyze | 1 | 110,000 | 69 | $0.19 | 88,000 | 导航 | wyze.com/ |
| wyze camera | 1 | 49,500 | 50 | $0.28 | 39,600 | 导航 | wyze.com/ |
| wyze cam v3 | 1 | 14,800 | 61 | $0.28 | — | 信息 | wyze.com/products/wyze-cam |
| wyze login | 1 | 14,800 | 46 | $0.05 | 11,840 | 导航 | my.wyze.com/ |
| wyze cam | 1 | 12,100 | 46 | $0.28 | 9,680 | 导航 | wyze.com/ |
| wyze cam v4 | 1 | 12,100 | 58 | $0.29 | — | 信息 | wyze.com/products/wyze-cam |
| wyze cameras | 1 | 8,100 | 46 | $0.28 | 6,480 | 信息/导航 | wyze.com/ |
| wyze outdoor camera | 1 | 6,600 | 33 | $0.33 | 5,280 | 商业/交易 | wyze.com/collections/battery-cameras |
| wyze doorbell | 1 | 5,400 | 34 | $0.31 | 4,320 | 商业/交易 | wyze.com/collections/video-doorbells |
| wyze security camera | 1 | 5,400 | 56 | $0.58 | 4,320 | 商业/交易 | wyze.com/collections/smart-cameras |
| wyze labs security camera | 1 | 5,400 | 44 | $0.58 | 4,320 | 商业/交易 | wyze.com/ |
| wyze cam plus subscription | 1 | 1,900 | 24 | $0.22 | — | 信息/交易 | wyze.com/... |
| wyze cam og | 1 | 1,900 | 26 | $0.30 | — | 信息 | wyze.com/products/wyze-cam-og |
| wyze cam plus | 1 | 1,300 | 21 | $0.37 | — | 商业/交易 | wyze.com/... |
| wyze cam pan | 1 | 2,400 | 50 | $0.28 | — | 信息 | wyze.com/products/wyze-cam-pan |
| wyze security system | 1 | 1,600 | 42 | $2.96 | 1,280 | 商业 | wyze.com/collections/home-monitoring |
| wyze robot vacuum | 1 | 3,600 | 31 | $0.58 | 2,880 | 商业/交易 | wyze.com/products/wyze-robot-vacuum |
| wyze thermostat | 1 | 2,900 | 35 | $0.71 | 2,320 | 商业/交易 | wyze.com/products/wyze-thermostat |

### 付费词（Google Ads，按流量排序）

Wyze 当前在美国市场**零付费投放**（Adwords Keywords = 0，Adwords Traffic = 0）。完全依靠品牌自然流量和产品口碑获客。竞品 Ring/Arlo 均大量投放 Google Shopping Ads，Wyze 没有参与付费竞争。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| wyze vs ring | 590 | 23 | $1.31 | 商业/信息 | ⭐ 最高量竞品对比词 |
| wyze vs blink | 480 | 23 | $1.37 | 商业/信息 | ⭐ 同亚马逊系竞品 |
| blink vs wyze | 320 | 19 | $0.83 | 信息 | ⭐ 反向问法同一搜索意图 |
| ring vs wyze | 260 | 25 | $0.99 | 商业/信息 | ⭐ |
| eufy vs wyze | 210 | 10 | $5.54 | 信息 | ⭐ KD 极低、CPC 高 |
| wyze vs eufy | 170 | 14 | $0.96 | 信息 | ⭐ |
| wyze vs arlo | 90 | 16 | $1.21 | 信息 | ⭐ |
| arlo vs wyze | 70 | 9 | $0.00 | 信息 | ⭐ KD=9 |
| reolink vs wyze | 70 | 10 | $0.61 | 信息 | ⭐ |
| wyze vs reolink | 20 | 0 | $0.00 | — | ⭐ 近零 KD |
| wyze alternative | 30 | 9 | $1.57 | 商业 | ⭐ 极低 KD，Olares 主攻 |
| wyze cam alternative | 20 | 0 | $0.69 | — | ⭐ 近零 KD |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| security camera without subscription | 3,600 | 42 | $1.71 | 商业 | 大量词；Wyze 本地 SD 卡就是答案 |
| frigate nvr | 3,600 | 36 | $3.84 | 信息/交易 | 已上架 Olares Market，高 CPC |
| home assistant frigate | 320 | 27 | $0.00 | 信息 | ⭐ 技术受众 |
| security camera local storage | 480 | 23 | $1.46 | 商业 | ⭐ Olares 叙事直接对应 |
| home assistant camera | 320 | 32 | $1.52 | 商业 | 技术社区词 |
| best cheap security camera | 320 | 42 | $2.53 | 商业 | 高 KD，流量大 |
| open source security camera | 140 | 28 | $3.40 | 信息/商业 | ⭐ Frigate 叙事入口 |
| self hosted security camera | 50 | 14 | $1.65 | 商业 | ⭐ KD=14，Olares 精准匹配 |
| best outdoor security camera no subscription | 40 | 49 | $1.52 | 商业 | 高 KD |
| cheap security camera no subscription | 10 | 0 | $3.64 | — | ⭐ 零 KD |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| wyze cam v3 | 14,800 | 61 | $0.28 | 信息 | 最搜硬件型号；KD 高、品牌词 |
| wyze cam v4 | 12,100 | 58 | $0.29 | 信息 | 新旗舰型号 |
| wyze cam pan | 2,400 | 50 | $0.28 | 信息 | 云台型号 |
| wyze cam plus subscription | 1,900 | 24 | $0.22 | 信息/交易 | ⭐ 订阅管理高意图 |
| wyze cam og | 1,900 | 26 | $0.30 | 信息 | ⭐ OG 支持官方 RTSP 固件 |
| wyze cam outdoor | 1,600 | 27 | $0.36 | 交易 | ⭐ |
| wyze cam plus | 1,300 | 21 | $0.37 | 商业/交易 | ⭐ 订阅评估词 |
| docker wyze bridge | 590 | 16 | $0.00 | 信息 | ⭐ 技术社区核心工具词 |
| wyze rtsp | 480 | 9 | $0.00 | 信息 | ⭐ KD=9，本地流关键词 |
| wyze home assistant | 390 | 18 | $0.00 | 信息 | ⭐ 自托管用户意图 |
| wyze cam rtsp | 170 | 19 | $0.00 | 信息/商业 | ⭐ |
| wyze cam home assistant | 170 | 17 | $0.00 | 信息 | ⭐ |
| wyze cam v3 rtsp | 90 | 14 | $0.00 | 信息/商业 | ⭐ 具体型号 RTSP |
| wyze cam v4 rtsp | 90 | 12 | $0.00 | 商业/交易 | ⭐ KD=12 |
| wyze cam without subscription | 50 | 5 | $0.41 | 商业 | ⭐ KD=5，意图极明确 |
| wyze floodlight | 880 | 30 | $0.26 | 商业/交易 | ⭐ 临界低 KD |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| frigate nvr | 3,600 | 36 | $3.84 | 信息/交易 | Olares Market 已上架；核心后端 |
| docker wyze bridge | 590 | 16 | $0.00 | 信息 | ⭐ 无需固件修改的 RTSP 桥接工具 |
| wyze rtsp | 480 | 9 | $0.00 | 信息 | ⭐ KD 最低的高价值词 |
| wyze home assistant | 390 | 18 | $0.00 | 信息 | ⭐ 自托管用户信号 |
| home assistant frigate | 320 | 27 | $0.00 | 信息 | ⭐ 技术整合受众 |
| security camera local storage | 480 | 23 | $1.46 | 商业 | ⭐ Olares 叙事锚点 |
| wyze cam rtsp | 170 | 19 | $0.00 | 信息/商业 | ⭐ |
| wyze cam home assistant | 170 | 17 | $0.00 | 信息 | ⭐ |
| wyze cam v3 rtsp | 90 | 14 | $0.00 | 信息/商业 | ⭐ |
| wyze cam v4 rtsp | 90 | 12 | $0.00 | 商业/交易 | ⭐ |
| wyze cam without subscription | 50 | 5 | $0.41 | 商业 | ⭐ KD=5，极强意图 |
| self hosted security camera | 50 | 14 | $1.65 | 商业 | ⭐ |
| open source security camera | 140 | 28 | $3.40 | 信息/商业 | ⭐ Frigate 角度 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Wyze 的痛点（订阅费用 + 数据隐私 + 云依赖）与 Olares 平台上 Frigate NVR 的价值主张完美对应——$30 Wyze 硬件 + Olares 上的 Frigate = 真正的本地 AI 检测，零月费。**

按月量降序。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|------------|--------|
| security camera without subscription | 3,600 | 42 | $1.71 | Wyze Cam v3/v4 + RTSP 固件 + Olares 上的 Frigate = 零订阅本地 AI 检测 | ⭐⭐⭐ |
| frigate nvr | 3,600 | 36 | $3.84 | Frigate 已上架 Olares Market；Wyze 是最便宜的 RTSP 摄像头源 | ⭐⭐⭐ |
| wyze rtsp | 480 | 9 | $0.00 | Wyze Cam v3 RTSP 固件 → 接入 Olares Frigate；KD=9 是最容易的切入点 | ⭐⭐⭐ |
| security camera local storage | 480 | 23 | $1.46 | Olares NVR 本地存储（无云依赖）+ Wyze 廉价硬件 = 完整本地方案 | ⭐⭐⭐ |
| docker wyze bridge | 590 | 16 | $0.00 | Docker Wyze Bridge 可部署在 Olares 上，无需修改固件即获 RTSP 流 | ⭐⭐⭐ |
| wyze home assistant | 390 | 18 | $0.00 | 自托管用户从 HA 迁移到 Olares；Frigate 在两平台都可跑 | ⭐⭐⭐ |
| wyze vs ring | 590 | 23 | $1.31 | Wyze+Olares 本地方案 vs Ring 云订阅；隐私、成本双赢叙事 | ⭐⭐⭐ |
| wyze alternative | 30 | 9 | $1.57 | KD=9 极低；Olares+Frigate 是拒绝云依赖的终极替代方案 | ⭐⭐⭐ |
| home assistant frigate | 320 | 27 | $0.00 | Frigate on Olares = HA 用户的一键替代；技术社区受众精准 | ⭐⭐ |
| wyze cam rtsp | 170 | 19 | $0.00 | 配置教程词；Olares 可作为 Frigate 的宿主平台 | ⭐⭐ |
| wyze cam home assistant | 170 | 17 | $0.00 | 同上；Olares 平台整合叙事 | ⭐⭐ |
| wyze cam v3 rtsp | 90 | 14 | $0.00 | v3 是最成熟 RTSP 固件机型；Olares + Frigate 教程切入 | ⭐⭐ |
| wyze cam v4 rtsp | 90 | 12 | $0.00 | v4 新机型 RTSP 支持教程 + Olares Frigate 配置 | ⭐⭐ |
| wyze cam without subscription | 50 | 5 | $0.41 | KD=5 最低；Olares Frigate 替代 Cam Plus 的核心叙事 | ⭐⭐⭐ |
| self hosted security camera | 50 | 14 | $1.65 | Olares 是最完整的自托管 NVR 宿主平台 | ⭐⭐⭐ |
| open source security camera | 140 | 28 | $3.40 | Frigate（开源）+ Olares（开源）+ Wyze 廉价硬件 | ⭐⭐ |
| wyze cam plus subscription | 1,900 | 24 | $0.22 | 订阅评估词；可切入"用 Olares+Frigate 替代 Cam Plus"叙事 | ⭐⭐ |
| eufy vs wyze | 210 | 10 | $5.54 | 对比文；eufy 支持本地 HomeBase，Wyze+Olares 更灵活 | ⭐⭐ |
| wyze vs blink | 480 | 23 | $1.37 | Blink 依赖 Amazon 云；Wyze+Olares 完全私有化 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|----|------|------|--------------------------|
| security camera without subscription | 3,600 | 42 | $1.71 | 商业 | 主词候选 | 量大、KD 中，Wyze+Olares 本地 NVR 是最强落地答案 |
| frigate nvr | 3,600 | 36 | $3.84 | 信息/交易 | 主词候选 | 已在 Olares Market，CPC $3.84 显示商业价值高；跨 Wyze 报告复用 |
| wyze vs ring | 590 | 23 | $1.31 | 商业/信息 | 主词候选 | 量最大的竞品对比词；可写"Wyze+Olares vs Ring 云"对比文 |
| wyze vs blink | 480 | 23 | $1.37 | 商业/信息 | 主词候选 | Blink 同为亚马逊系；订阅/隐私叙事相似，可并入对比文 |
| docker wyze bridge | 590 | 16 | $0.00 | 信息 | 主词候选 | ⭐ KD=16 机会词；技术受众直接导向 Olares 部署教程 |
| wyze rtsp | 480 | 9 | $0.00 | 信息 | 主词候选 | ⭐ KD=9 最低竞争高意图词；Wyze RTSP+Frigate 教程首选 |
| security camera local storage | 480 | 23 | $1.46 | 商业 | 主词候选 | ⭐ 量足 KD 中，Olares 本地存储叙事直接命中 |
| wyze home assistant | 390 | 18 | $0.00 | 信息 | 主词候选 | ⭐ HA 迁移 Olares 的核心词；受众与 Olares 高度重叠 |
| home assistant frigate | 320 | 27 | $0.00 | 信息 | 主词候选 | ⭐ 技术受众聚合词；Olares 作为 Frigate 宿主的落地文章 |
| wyze cam plus subscription | 1,900 | 24 | $0.22 | 信息/交易 | 主词候选 | ⭐ 订阅评估意图；可切"替代 Cam Plus 的本地方案"落地文 |
| wyze vs eufy | 170 | 14 | $0.96 | 信息 | 次级 | ⭐ KD=14 机会，可并入对比文附加段 |
| eufy vs wyze | 210 | 10 | $5.54 | 信息 | 次级 | ⭐ KD=10，CPC 高；可并入对比文 |
| wyze cam rtsp | 170 | 19 | $0.00 | 信息/商业 | 次级 | ⭐ 教程型词；并入 wyze rtsp 主文 |
| wyze cam home assistant | 170 | 17 | $0.00 | 信息 | 次级 | ⭐ 并入 wyze home assistant 主文 |
| wyze cam v3 rtsp | 90 | 14 | $0.00 | 信息/商业 | 次级 | ⭐ 型号级长尾，并入 RTSP 教程主文 |
| wyze cam v4 rtsp | 90 | 12 | $0.00 | 商业/交易 | 次级 | ⭐ v4 新型号，并入 RTSP 教程主文 |
| wyze cam without subscription | 50 | 5 | $0.41 | 商业 | 次级 | ⭐ KD=5 最低，意图精准；并入本地方案主文 |
| self hosted security camera | 50 | 14 | $1.65 | 商业 | 次级 | ⭐ 量小但精准；并入 Frigate/本地 NVR 主文 |
| wyze alternative | 30 | 9 | $1.57 | 商业 | 次级 | ⭐ KD=9，CPC $1.57；量小但高意图，并入对比文 |
| open source security camera | 140 | 28 | $3.40 | 信息/商业 | 次级 | ⭐ Frigate 叙事入口；并入 Frigate on Olares 文章 |
| wyze cam plus cancel | — | — | — | — | GEO | 量极小；FAQ 段"用 Olares+Frigate 取代 Cam Plus 再取消" |
| wyze cam local storage | 0 | 0 | — | — | GEO | 近零量；抢 AI Overview"Wyze 本地存储怎么配置"引用位 |
| cheap security camera self hosted | — | — | — | — | GEO | 语义精准；自然语言搜索/Perplexity"最便宜的自托管摄像头" |
| wyze frigate olares | — | — | — | — | GEO | 近零量；精准抢"Wyze + Frigate + Olares 如何配置"引用位 |
| best budget security camera no subscription | 20 | 0 | — | — | GEO | ⭐ KD=0，商业意图；Olares 本地 NVR 角度完美命中 |

---

## 核心洞见

1. **品牌护城河**：Wyze 品牌词（"wyze" 110K/月，"wyze camera" 49.5K/月）KD 均在 46-69，排名 1 且全是自有 URL，无法正面刚。但**非品牌词（替代/对比/RTSP/本地存储）KD 普遍 < 30**，全是可攻击区域。竞品词"wyze vs ring"（590/月，KD=23）是量最大的可攻击主词。

2. **可复制的打法**：Wyze 主站靠大量产品页面（/products/、/collections/）做品牌流量承接；`forums.wyze.com` 收录 35K 关键词（6.6% 流量）说明用户生成内容（故障排查/配置讨论）贡献显著流量——Olares 应在**技术教程词**（RTSP 配置、Frigate 接入）上切入同类流量。Wyze 零付费投放意味着非品牌词竞争相对开放。

3. **对 Olares 最关键的 2-3 个词**：
   - `wyze rtsp`（480/月，KD=9）：最低竞争、最高技术意图，Wyze RTSP 固件 → Olares Frigate 配置的核心入口词
   - `docker wyze bridge`（590/月，KD=16）：技术社区词，Olares 上部署 Docker Wyze Bridge 的教程直接对应此词
   - `security camera without subscription`（3,600/月，KD=42）：量最大的非品牌词，Olares+Frigate 是最完整的回答

4. **最大攻击面**：Wyze 的三大痛点——**订阅费**（Cam Plus $2.99-9.99/月）、**数据隐私**（2022/2024 安全事件）、**云依赖**（断网/服务器故障则 AI 检测失效）。对应词："wyze cam plus subscription"（1,900/月，KD=24）、"wyze cam without subscription"（50/月，KD=5）、"wyze security breach"（70/月，KD=29）。叙事角度：Olares+Frigate 彻底解决三个痛点。

5. **隐藏低 KD 金矿**：
   - `wyze rtsp`：480/月，KD=9（**最宝贵**，技术意图明确但竞争极低）
   - `wyze cam without subscription`：50/月，KD=5（意图极精准）
   - `arlo vs wyze`：70/月，KD=9
   - `eufy vs wyze`：210/月，KD=10
   - `wyze cam v4 rtsp`：90/月，KD=12

6. **GEO 前瞻布局**：
   - `"wyze cam frigate olares"` / `"wyze frigate nvr setup"` / `"wyze cam without internet"` — 抢 Perplexity / AI Overview 引用位
   - `"cheap security camera no subscription self hosted"` — 长尾自然语言查询，Olares 能给最完整答案
   - `"cancel wyze cam plus use local ai instead"` — 意图=取消订阅 → 转向 Olares 本地方案

7. **与既有分析的关联**：
   - `olares-500-keywords` 词表中"self-hosted NVR"类词量极小（现实流量在具体品牌+功能词上），本报告补充了 Wyze 生态的精准长尾（RTSP、docker-wyze-bridge、wyze home assistant）——这批词 KD 低、技术受众明确，应优先用于 Olares 技术博客内容
   - Frigate NVR 报告已在 `market/reports/frigate-nvr.md`，本报告的词表（wyze rtsp、docker wyze bridge、security camera without subscription）应与 Frigate 报告交叉聚簇，写"Wyze + Frigate + Olares"组合文章时引用两份报告

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、phrase_these）| 2026-07-06*
*所有搜索量为美国月均；IoT/家居类产品全球量通常为美国的 2-4 倍。*
