# Petkit SEO 竞品分析报告

> 域名：petkit.com | SEMrush US | 2026-07-06
> 智能宠物设备品牌：喂食器 + 饮水机 + 猫砂盆 + 摄像头（Agora/Alibaba Cloud）+ Care+ 云订阅生态

---

## 项目理解（前置）

Petkit（上海 PETKIT TECHNOLOGY）是中国供应链背景的智能宠物 IoT 品牌，产品线覆盖自动猫砂盆（PuraMax/Purobot 系列）、智能喂食器（YumShare Solo/Dual、Fresh Element 系列）、宠物饮水机（Eversweet 系列）和带摄像头喂食器。App 体系统一，Care+ 订阅（$4.99/月）解锁云端录像回看、AI 行为分析和扩展数据历史；视频传输走 Agora RTC，数据存 Alibaba Cloud。竞品行研口径给 Petkit 约 11% 宠物摄像头市场份额（2024 营收约 $18M，二手数据[u]）。**Olares 平替**：摄像头侧 = Frigate + 本地 IP cam + Home Assistant（已有 [Frigate 市场报告](../../market/reports/frigate-nvr.md)）；喂食器侧 = ESPHome DIY（技术路线，无商用本地平替，treat-tossing 更无开源对应）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 中国供应链智能宠物 IoT 生态：猫砂盆 + 喂食器 + 饮水机 + 摄像头 + Care+ 云订阅 |
| 开源 / 许可证 | 闭源；App 内嵌 Agora SDK + 微博/微信/高德等第三方 SDK |
| 主仓库 | 无官方开源仓库；社区集成 `homeassistant-petkit`（非官方） |
| 核心功能 | 自动猫砂盆（AI 摄像头健康监测）、带摄像头喂食器（1080p + 双向音频）、饮水机、Care+ 云录像与 AI 行为分析 |
| 商业模式 / 定价 | 硬件一次性：喂食器 $99–$159，猫砂盆 $399–$599；Care+ 订阅 $4.99/月，解锁云端录像回看 |
| 差异化 / 价值主张 | 全品类 IoT 生态整合（单 App 管全部设备）+ AI 猫砂盆健康洞察 + 喂食器摄像头分餐识别 |
| 主要竞品（初判）| petlibro.com（喂食器直接竞品）、furbo.com（投食摄像头）、petcube.com、whisker.com（Litter-Robot）|
| Olares Market | 未上架（摄像头平替 Frigate NVR 已上架；ESPHome 可在 Olares 上自托管） |
| 来源 | [petkit.com](https://www.petkit.com)、[PETKIT 隐私政策](https://m.petkit.com/app/about/policy/en.html)、APKMirror（App 描述）、品类调研 [pet-cameras.md](../../../research/02-hardware/pet-cameras.md) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | petkit.com |
| SEMrush Rank | 57,491 |
| 自然关键词数 | 5,432 |
| 月自然流量（US）| 35,457 |
| 自然流量估值 | $48,144/月 |
| 付费关键词数 | 36 |
| 月付费流量 | 1,166 |
| 付费流量估值 | $2,379/月 |
| 排名 1–3 位 | 636 词 |
| 排名 4–10 位 | 744 词 |
| 排名 11–20 位 | 1,114 词 |

**结构洞察**：petkit.com 流量主体由猫砂盆（litter box）和饮水机（water fountain）驱动，喂食器/摄像头关键词仅占次要位置。品牌在 1–3 位排名数量（636）远低于 11–20 位（1,114），说明大量非品牌品类词仍在第二页徘徊，内容潜力大。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.petkit.com | 3,807 | 32,403 | 91.4% |
| petkit.com | 1,533 | 2,991 | 8.4% |
| instructions.petkit.com | 73 | 58 | 0.2% |
| support.petkit.com | 11 | 5 | <0.1% |

### 官网 TOP 自然关键词（按流量排序，前 30）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| petkit | 1 | 5,400 | 49 | $2.25 | 4,320 | 导航/商业 | / |
| petkit litter box | 1 | 1,900 | 30 | $1.78 | 1,520 | 导航/交易 | /collections/automatic-cat-litter-box |
| water drinking fountain cats | 1 | 22,200 | 45 | $0.94 | 1,443 | 信息 | /collections/pet-water-fountain |
| automatic litter box | 5 | 49,500 | 39 | $1.51 | 1,188 | 信息 | /collections/automatic-cat-litter-box |
| petkit pura max | 1 | 1,300 | 30 | $1.85 | 1,040 | 导航 | /products/petkit-puramax-2 |
| automatic cat feeder | 4 | 27,100 | 47 | $0.59 | 948 | 信息 | /collections/automatic-pet-feeder |
| petkit water fountain | 1 | 1,000 | 39 | $1.11 | 800 | 交易 | /collections/pet-water-fountain |
| petkit puramax 2 | 1 | 1,000 | 25 | $2.23 | 800 | 导航/交易 | /products/petkit-puramax-2 |
| cat feeder | 1 | 5,400 | 31 | $0.63 | 712 | 信息 | /collections/automatic-pet-feeder |
| auto cat litter box | 1 | 5,400 | 35 | $1.44 | 712 | 信息 | /collections/automatic-cat-litter-box |
| auto litter box | 2 | 8,100 | 50 | $1.51 | 664 | 信息 | /collections/automatic-cat-litter-box |
| automatic cat litter box | 2 | 27,100 | 37 | $1.44 | 650 | 信息 | /collections/automatic-cat-litter-box |
| automatic kitty litter pan | 2 | 8,100 | 52 | $1.44 | 526 | 信息 | /collections/automatic-cat-litter-box |
| cat water dispenser | 1 | 2,900 | 45 | $0.71 | 382 | 信息 | /collections/pet-water-fountain |
| cat box automatic | 2 | 4,400 | 35 | $1.44 | 360 | 信息 | /collections/automatic-cat-litter-box |
| best automatic litter box | 9 | 14,800 | 47 | $1.86 | 192 | 信息 | /collections/automatic-cat-litter-box |
| automatic cat feeder with camera | 1 | 590 | 14 | $0.74 | 146 | 信息 | /collections/automatic-pet-feeder |
| petkit purobot ultra | 1 | 260 | 32 | $1.92 | 208 | 导航 | /products/purobot-ultra |
| petkit eversweet water fountain | 1 | 170 | 21 | $0.93 | 136 | 导航 | /collections/pet-water-fountain |
| pet feeder | 1 | 1,600 | 38 | $1.06 | 211 | 信息 | /collections/automatic-pet-feeder |
| auto animal feeders | 5 | 6,600 | 52 | $0.60 | 158 | 信息/导航 | /collections/automatic-pet-feeder |
| cat water fountain | 8 | 40,500 | 47 | $0.94 | 162 | 信息 | /collections/pet-water-fountain |
| petkit feeder | 1 | 210 | 17 | $0.79 | 168 | 交易 | /collections/automatic-pet-feeder |
| petkit automatic litter box | 1 | 210 | 23 | $1.68 | 168 | 交易 | /collections/automatic-cat-litter-box |
| petkit purobot max pro | 1 | 170 | 32 | $2.40 | 136 | 导航/交易 | /products/purobot-max-pro-2... |
| cat food auto feeder | 1 | 480 | 53 | $0.83 | 119 | 信息 | /collections/automatic-pet-feeder |
| pet cam feeder | 1 | 90 | 13 | $0 | ~72 | 信息 | /collections/automatic-pet-feeder |
| petkit fresh element 1 | 1 | 320 | 26 | $0 | 256 | 导航/交易 | /products/fresh-element-solo |
| petkit puramax | 1 | 320 | 32 | $1.86 | 256 | 导航/交易 | /products/petkit-puramax-2 |
| petkit eversweet | 1 | 140 | 24 | $1.15 | 112 | 导航 | /collections/pet-water-fountain |

**关键发现**：petkit.com 在 `automatic cat feeder with camera`（KD=14，月量 590）排名第 1，占据了低竞争大词首位——是 Olares 最值得切入的品类词之一。

### 付费词（Google Ads，按流量排序）

Petkit 付费投放策略集中于品牌词防御（约 30 个词，全为 petkit 品牌前缀），付费流量共 1,166/月，$2,379 花费。几乎不投非品牌品类词，说明其依赖自然排名获取品类流量。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| petkit | 1 | 5,400 | $2.25 | /（×3 广告组） |
| petkit litter box | 1 | 1,900 | $1.74 | /products/petkit-puramax-2 |
| petkit water fountain | 1 | 1,000 | $1.11 | /collections/pet-water-fountain |
| petkit litter box | 2 | 1,900 | $1.78 | /collections/automatic-cat-litter-box |
| petkit pura max 2 | 2 | 720 | $2.11 | /products/petkit-puramax-2 |
| petkit discount code | 1 | 90 | $7.33 | /collections/all |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| furbo | 18,100 | 54 | $1.92 | 导航 | 投食摄像头市场领导者，护城河深 |
| petlibro | 27,100 | 48 | $2.54 | 导航/商业 | 喂食器最大竞品，流量 76K/月 |
| petcube | 3,600 | 59 | $0.72 | 导航 | 宠物摄像头竞品 |
| petkit vs litter robot | 70 | 14 | $1.55 | 信息 | ⭐ 猫砂盆对比词 |
| petkit vs petlibro | 20 | 0 | $1.80 | 信息 | ⭐ 喂食器对比词 |
| furbo alternative | 20 | 0 | $1.76 | 信息 | ⭐ 对比切入点 |
| petcube alternative | 20 | 0 | — | 信息 | ⭐ 对比切入点 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| automatic litter box | 49,500 | 39 | $1.51 | 信息 | Petkit 已排名第 5，竞争激烈 |
| automatic cat feeder | 27,100 | 47 | $0.60 | 信息 | 大品类词，Petkit 排名第 4 |
| cat water fountain | 40,500 | 47 | $0.94 | 信息 | 排名第 8，仍有上升空间 |
| pet camera | 9,900 | 46 | $0.87 | 信息 | 通用宠物摄像头 |
| microchip cat feeder | 5,400 | 34 | $0.58 | 信息 | 高价值喂食器细分 |
| best pet camera | 1,600 | 41 | $0.96 | 信息 | 评测型信息词 |
| smart pet feeder | 880 | 36 | $0.53 | 信息 | 智能喂食器类目 |
| automatic cat feeder with camera | 590 | 14 | $0.74 | 信息 | ⭐ **极低 KD，Petkit 排名第 1，核心词** |
| indoor pet camera | 590 | 34 | $1.06 | 信息 | ⭐ 室内宠物摄像头 |
| dog camera treat dispenser | 590 | 22 | $0.80 | 信息 | ⭐ 投食摄像头细分 |
| cat feeder camera | 390 | 36 | $0.75 | 信息/导航 | 喂食器+摄像头组合词 |
| best pet camera without subscription | 480 | 24 | $0.68 | 信息 | ⭐ **无订阅摄像头，Olares 核心** |
| pet camera no subscription | 390 | 18 | $0.70 | 信息 | ⭐ **低 KD，高意图，主词候选** |
| rfid cat feeder | 1,900 | 28 | $0.94 | 信息 | ⭐ 低 KD 大量，技术型用户 |
| automatic pet feeder with camera | 260 | 14 | $0.99 | 信息 | ⭐ 极低 KD，长尾变体 |
| wyze pet camera | 170 | 16 | $0.48 | 交易 | ⭐ 平价竞品 |
| pet monitoring camera | 110 | 36 | $0.84 | 信息 | 宠物监控通用词 |
| pet feeder with camera | 210 | 19 | $0.70 | 信息 | ⭐ 低 KD |
| pet camera without subscription | 90 | 29 | $0.84 | 信息 | ⭐ 明确意图词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| petkit litter box | 1,900 | 18 | $1.84 | 导航/交易 | ⭐ 低 KD 品牌产品词，大量 |
| petkit pura max | 1,300 | 30 | $1.85 | 导航 | 旗舰猫砂盆，CPC 高 |
| petkit puramax 2 | 1,000 | 28 | $1.73 | 导航/交易 | ⭐ |
| petkit fresh element 1/2 | 1,600/1,900 | 26/30 | — | 导航/交易 | ⭐ 喂食器型号词 |
| petkit water fountain | 1,000 | 39 | $1.11 | 交易 | 竞争较高 |
| petkit purobot ultra | 260 | 39 | $1.68 | 导航/交易 | 竞争较高 |
| petkit feeder | 210 | 17 | $0.79 | 交易 | ⭐ 低 KD |
| petkit pura x | 480 | 17 | $1.37 | 导航 | ⭐ 低 KD |
| petkit auto litter box | 260 | 24 | $1.50 | 信息 | ⭐ |
| petkit app | 90 | 6 | $1.17 | 导航 | ⭐ 极低 KD，App 满意度切入 |
| petkit care plus | 30 | 13 | $1.34 | 信息 | ⭐ 订阅词，投诉信号 |
| petkit purobot max pro | 170 | 32 | $2.40 | 导航/交易 | AI 摄像头旗舰 |
| petkit vs litter robot | 70 | 14 | $1.55 | 信息 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| frigate nvr | 3,600 | 36 | $3.84 | 信息/交易 | Olares Market 已上架，高 CPC 信号 |
| frigate home assistant | 720 | 28 | — | 信息 | ⭐ 低 KD，HA 生态词 |
| open source nvr | 720 | 28 | $4.56 | 信息 | ⭐ 高 CPC 表示商业意图 |
| home assistant frigate | 320 | 27 | — | 信息 | ⭐ 进阶 HA 用户 |
| wyze cam home assistant | 170 | 17 | — | 信息 | ⭐ Wyze 替代路径 |
| home assistant camera | 320 | 32 | $1.52 | 商业 | HA 摄像头集成 |
| esphome pet feeder | 20 | 0 | — | 信息 | ⭐ 极低 KD，DIY 喂食器信号 |
| home assistant cat feeder | 20 | 0 | — | 信息 | ⭐ |
| pet feeder home assistant | 20 | 0 | — | 信息 | ⭐ |
| self hosted camera | 40 | 0 | — | 信息 | ⭐ |

---

## Olares 关联词（Phase 3）

**核心逻辑：Petkit 的云依赖（Agora 传输 + Alibaba Cloud 存储 + Care+ 订阅）是最明确的叙事攻击面；Frigate（已在 Olares Market）+ 本地 IP cam + HA 构成完整摄像头平替栈；喂食器侧 ESPHome 属技术路线，需诚实标注。**

按月量降序。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| automatic cat feeder with camera | 590 | 14 | $0.74 | Petkit YumShare 摄像头需 Care+ 回看录像；Frigate on Olares 可全本地替代摄像头部分 | ⭐⭐⭐ |
| pet camera no subscription | 390 | 18 | $0.70 | 核心痛点词：Petkit Care+ $4.99/月；Frigate + 本地 IP cam = 零订阅 | ⭐⭐⭐ |
| best pet camera without subscription | 480 | 24 | $0.68 | 同上，评测型信息词；Olares + Frigate 是最直接答案 | ⭐⭐⭐ |
| frigate nvr | 3,600 | 36 | $3.84 | Frigate 已在 Olares Market，高 CPC = 用户有明确方案意图 | ⭐⭐⭐ |
| frigate home assistant | 720 | 28 | — | 部署栈词：HA on Olares + Frigate 本地宠物检测 | ⭐⭐⭐ |
| open source nvr | 720 | 28 | $4.56 | 高 CPC 开源意图；Frigate 是最强答案，Olares 一键部署 | ⭐⭐⭐ |
| automatic pet feeder with camera | 260 | 14 | $0.99 | KD 极低；Petkit/Petlibro 产品词变体，Olares 可做对比内容 | ⭐⭐⭐ |
| pet feeder with camera | 210 | 19 | $0.70 | 同上，长尾变体，撑同一篇文章 | ⭐⭐⭐ |
| pet camera without subscription | 90 | 29 | $0.84 | 明确无订阅意图，Frigate + Olares 完整答案 | ⭐⭐⭐ |
| petkit care plus | 30 | 13 | $1.34 | 用户主动搜订阅细节，是痛点信号；可切入"跳过 Care+" 的内容 | ⭐⭐⭐ |
| home assistant frigate | 320 | 27 | — | HA 用户进阶栈，Olares 做一键部署差异化 | ⭐⭐ |
| wyze cam home assistant | 170 | 17 | — | Wyze 用户转 HA 路径；Olares 可做无缝整合教程 | ⭐⭐ |
| frigate home assistant | 720 | 28 | — | HA + Frigate 生态词；与 Olares Home Assistant 组合展示 | ⭐⭐ |
| petkit vs litter robot | 70 | 14 | $1.55 | 对比词，KD 低；可切"两者都云依赖，Frigate+HA 零月费" | ⭐⭐ |
| esphome pet feeder | 20 | 0 | — | GEO 前哨：ESPHome DIY 喂食器 + Olares HA 自动化排程 | ⭐⭐ |
| home assistant cat feeder | 20 | 0 | — | GEO 前哨，极低 KD，Olares + HA 完整场景 | ⭐⭐ |
| petkit app | 90 | 6 | $1.17 | App 用户疑问词（KD=6），可做 Home Assistant 替代 App 的内容 | ⭐ |
| self hosted camera | 40 | 0 | — | GEO 前哨，长尾自托管词 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| automatic cat feeder with camera | 590 | 14 | $0.74 | 信息 | **主词候选** | KD 极低（14）、量 590、Petkit 排名 #1；Olares 可做"带摄像头喂食器 + 不依赖云"对比文，Frigate 补充摄像头侧 |
| pet camera no subscription | 390 | 18 | $0.70 | 信息 | **主词候选** | KD=18、量 390；直击 Petkit Care+ 痛点；Frigate on Olares = 零月费本地宠物摄像头完整答案 |
| best pet camera without subscription | 480 | 24 | $0.68 | 信息 | **主词候选** | 量 480、KD 24；评测型词，Olares + Frigate 自然进入 best-of 推荐位 |
| frigate nvr | 3,600 | 36 | $3.84 | 信息/交易 | **主词候选** | 量大、CPC 高（$3.84）= 商业意图强；Frigate 已在 Olares Market，是最直接品牌词变体 |
| open source nvr | 720 | 28 | $4.56 | 信息 | **主词候选** | KD=28、CPC=$4.56（信号极强）；Frigate = 答案，Olares 一键部署是差异化 |
| frigate home assistant | 720 | 28 | — | 信息 | **主词候选** | 量 720、KD 28；栈词，Olares = HA + Frigate 一体化部署平台 |
| automatic pet feeder with camera | 260 | 14 | $0.99 | 信息 | 次级 | KD 极低；可并入"automatic cat feeder with camera"文章簇 |
| pet feeder with camera | 210 | 19 | $0.70 | 信息 | 次级 | 同上，长尾变体 |
| pet camera without subscription | 90 | 29 | $0.84 | 信息 | 次级 | 并入"pet camera no subscription"文章 |
| rfid cat feeder | 1,900 | 28 | $0.94 | 信息 | 次级 | KD 低、量大；非 Petkit 专属但喂食器技术词，可穿插 |
| dog camera treat dispenser | 590 | 22 | $0.80 | 信息 | 次级 | ⭐ 低 KD，Furbo/Petkit 竞品词 |
| petkit litter box | 1,900 | 18 | $1.84 | 导航/交易 | 次级 | 品牌词为主，KD 低可蹭品牌流量；内容以"litter box + subscription cost" 角度切 |
| petkit care plus | 30 | 13 | $1.34 | 信息 | 次级 | KD 极低，订阅投诉信号，适合 FAQ 段 |
| petkit feeder | 210 | 17 | $0.79 | 交易 | 次级 | 品牌型号词，KD 低 |
| petkit app | 90 | 6 | $1.17 | 导航 | 次级 | KD=6，App 投诉/替代场景 |
| petkit vs litter robot | 70 | 14 | $1.55 | 信息 | 次级 | 对比词，KD=14 |
| wyze cam home assistant | 170 | 17 | — | 信息 | 次级 | Wyze→HA 路径，拉 Olares 部署优势 |
| home assistant cat feeder | 20 | 0 | — | 信息 | GEO | HA 喂食器自动化精准词，ESPHome + Olares HA |
| esphome pet feeder | 20 | 0 | — | 信息 | GEO | DIY 喂食器关键词，零 KD，抢 AI Overview 引用 |
| pet feeder home assistant | 20 | 0 | — | 信息 | GEO | 同上，略微变体 |
| self hosted pet camera | 20 | 0 | — | 信息 | GEO | 极精准意图词，Frigate + Olares 完整答案 |
| petkit agora sdk | — | — | — | — | GEO | 技术词：Petkit 视频走 Agora，Olares 本地替代叙事，AI 引用位 |
| petkit care plus cancel | — | — | — | — | GEO | 订阅取消意图，投诉信号强，切换路径内容 |

---

## 核心洞见

1. **品牌护城河**：Petkit 品牌词（5,400 月量，KD=49，CPC=$2.25）心智较强但远未达 Furbo/Petlibro 量级。**正面打品牌词得不偿失**（KD 48+，竞争激烈）；最佳策略是从**品类词切入**（feeder with camera、pet camera no subscription），再在内容中对比 Petkit 的 Care+ 订阅成本。

2. **可复制的打法**：Petkit 在低竞争品类词（`automatic cat feeder with camera` KD=14，`petkit feeder` KD=17，`petkit litter box` KD=18）排名第 1——说明这个品牌通过**精准产品页 + 自然排名**，而非内容策略获取流量。Olares 可复制其**品类词精准落地页**模式，用"无 Care+月费 + 本地视频不出设备"为核心差异化。

3. **对 Olares 最关键的 3 个词**：
   - `pet camera no subscription`（月量 390，KD=18）——最直接的 Petkit Care+ 痛点词
   - `automatic cat feeder with camera`（月量 590，KD=14）——超低 KD，喂食器摄像头品类词
   - `frigate nvr`（月量 3,600，KD=36，CPC=$3.84）——Olares Market 已有 Frigate，高 CPC 证实商业意图

4. **最大攻击面**：**Care+ 订阅成本（$4.99/月，约 $60/年）+ Agora/Alibaba Cloud 云传输**。用户痛点清晰——搜 `petkit care plus`、`pet camera no subscription`、`best pet camera without subscription` 的用户都在寻找替代。内容叙事：Petkit 硬件拍摄的画面经 Agora 路由到 Alibaba Cloud，云订阅到期即失去历史录像；Frigate on Olares = 全本地，无云传输，无月费，历史录像永久本地存储。

5. **隐藏低 KD 金矿**：
   - `automatic cat feeder with camera`（KD=14，月量 590）⭐⭐⭐
   - `automatic pet feeder with camera`（KD=14，月量 260）⭐⭐⭐
   - `pet feeder with camera`（KD=19，月量 210）
   - `rfid cat feeder`（KD=28，月量 1,900）——侧面切入技术用户
   - `dog camera treat dispenser`（KD=22，月量 590）
   - `petkit app`（KD=6，月量 90）——App 投诉信号，极低 KD

6. **GEO 前瞻布局**：
   - `esphome pet feeder` / `home assistant cat feeder`（月量 20，KD=0）——进 FAQ 段，抢 AI Overview 引用位（"ESPHome + Olares Home Assistant 是否可以替代 Petkit 喂食器？"）
   - `petkit agora sdk`（近零量）——技术叙事，吸引开发者/隐私意识用户（"Petkit 使用 Agora SDK 传输视频到中国云，如何本地替代？"）
   - `self hosted pet camera`（近零量，KD=0）——完整 Olares 落点
   - `petkit care plus cancel`——订阅取消意图，切换路径叙事

7. **与既有 olares-500-keywords 的关联**：与 [cameras/ring.md](cameras/ring.md)、[cameras/arlo.md](cameras/arlo.md) 等摄像头报告的 Frigate 词簇高度重叠（`frigate nvr`、`home assistant frigate`）。本报告补充了**宠物垂类**的特有词：`automatic cat feeder with camera`、`pet camera no subscription`（KD 极低）——这两个词在通用摄像头报告中未单独出现，建议与 Frigate 主词合并为一个"宠物自托管摄像头"内容簇，与 Ring/Arlo 替代文区分垂类。

---

**诚实差距标注**：摄像头侧平替（Frigate + 本地 IP cam）成熟度高；喂食器侧**仅 ESPHome DIY**（需焊接/3D 打印），无成熟商用本地平替；**treat-tossing 功能（丢零食）完全无开源平替**。内容应如实标注，避免夸大自托管喂食器的可行性。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、resource_adwords、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
