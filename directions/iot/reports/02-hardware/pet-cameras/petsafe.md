# PetSafe Smart Feed / Wopet SEO 竞品分析报告

> 域名：petsafe.net（EU/支持站；商业主站为 petsafe.com）+ wopet.com | SEMrush US | 2026-07-06
> 云依赖 WiFi 智能喂食器双雄——PetSafe 是全球最大宠物硬件集团旗下品牌，Wopet 是新兴中国品牌；两者均需 App+云才能远程控制，本报告以"ESPHome DIY 本地喂食器"作为 Olares 的切入锚。

---

## 项目理解（前置）

PetSafe 隶属 PetSafe Brands（前 Radio Systems Corporation，2024 年 3 月更名），是全球最大宠物硬件制造商，产品线覆盖电子围栏、训练项圈、宠物门、自动喂食器、饮水机等。旗舰 WiFi 喂食器 **Smart Feed 2nd Generation**（约 $135）通过"My PetSafe"App 控制，可定时 12 餐、远程即时喂食、低粮提醒，并支持 Alexa；**需要 2.4GHz WiFi 才能使用 App 功能，断网后仅维持已保存的本地时刻表**。Wopet 是面向欧美市场的中国宠物智能硬件新兴品牌，提供多款 6L WiFi 喂食器（$50-100），通过"WOpet Life"App 控制，同样需云端连接才能使用完整功能。两者均无本地 API，无法在断网时被第三方系统（如 Home Assistant）主动调用。

| 项目 | 内容 |
|------|------|
| 一句话定位 | WiFi 自动宠物喂食器，App 控制+云依赖，PetSafe（$135）vs Wopet（$50-100） |
| 开源 / 许可证 | 两者均为闭源商业产品；无官方开源仓库 |
| 主仓库 | 无；对比：ESPHome DIY 平替 [pricklyguy/pet-feeder-esphome](https://github.com/pricklyguy/pet-feeder-esphome)、[barjonas/chonk-o-matic](https://github.com/barjonas/chonk-o-matic) |
| 核心功能 | 定时投食（12-15 餐/天）；远程 Feed Now；低粮警报；慢食模式；语音播报（Wopet）；Alexa（PetSafe） |
| 商业模式 / 定价 | PetSafe Smart Feed ~$135 一次性；Wopet $50-100；PetSafe 针对 GPS 围栏等其他产品收取 Connectivity Services 订阅费 |
| 差异化 / 价值主张 | PetSafe：品牌信任度 + Alexa 集成；Wopet：性价比 + 5G/2.4G 双频 + 大容量 |
| 主要竞品（初判）| PETLIBRO、PetKit、Arf Pets、Cat Mate（离线定时器型）、Lusmo（新） |
| Olares Market | 未上架（闭源硬件）；**ESPHome + Home Assistant 为 Olares 的开源平替方向**，Home Assistant 已上架 Olares Market |
| 来源 | [petsafe.com/p/smart-feed](https://www.petsafe.com/p/smart-feed/PFD00-16828/)；[wopet.com](https://wopet.com/)；[botmonster.com/build-smart-pet-feeder-esphome](https://botmonster.com/smart-home/build-smart-pet-feeder-esphome-servo-motor/)；[petsafe.com/support/policies-and-terms/subscription-services-terms-and-conditions](https://www.petsafe.com/support/policies-and-terms/subscription-services-terms-and-conditions/) |

---

## 流量基线（Phase 1）

### 概览

#### petsafe.net（EU/支持站）

| 指标 | 数据 |
|------|------|
| 域名 | petsafe.net |
| SEMrush Rank | 218,112 |
| 自然关键词数 | 13,236 |
| 月自然流量（US）| 8,017 |
| 自然流量估值 | $5,309 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 459 词 |
| 排名 4-10 位 | 1,855 词 |
| 排名 11-20 位 | 1,464 词 |

> **注意**：petsafe.net 是 PetSafe 的支持/欧洲入口站，商业主站为 petsafe.com（13.6 万自然关键词、月流量 330,707、Rank 约 35,000 量级）。两者同属 PetSafe Brands 公司，本报告以 petsafe.net 为主研究对象，同步参考市场格局。

#### wopet.com（对比）

| 指标 | 数据 |
|------|------|
| 域名 | wopet.com |
| SEMrush Rank | 100,961 |
| 自然关键词数 | 40,195 |
| 月自然流量（US）| 19,170 |
| 自然流量估值 | $2,682 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 264 词 |
| 排名 4-10 位 | 1,801 词 |
| 排名 11-20 位 | 4,205 词 |

### 子域名流量分布（petsafe.net）

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| support.petsafe.net | 10,412 | 6,508 | 81.2% |
| www.petsafe.net | 2,617 | 1,246 | 15.5% |
| petfenceplanner.petsafe.net | 100 | 217 | 2.7% |
| www.support.petsafe.net | 88 | 46 | 0.6% |

> 支持子域占流量 81%，反映用户大量搜索操作指南与故障排查——说明**产品体验痛点集中在"用不好"而非"找不到"**，内容切入点在操作/替代类文章。

### 官网 TOP 自然关键词（petsafe.net，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| petsafe | 2 | 9,900 | 60 | $1.47 | 257 | 导航 | support.petsafe.net |
| easy walk dog harness | 3 | 6,600 | 28 | $0.44 | 125 | 信息 | support.petsafe.net |
| smart phone dog trainer | 6 | 4,400 | 16 | — | 105 | 信息 | support.petsafe.net/articles |
| easy walk harness | 7 | 9,900 | 29 | $0.44 | 89 | 信息/交易 | support.petsafe.net |
| petsafe wireless fence | 6 | 8,100 | 50 | $1.48 | 48 | 信息/交易 | support.petsafe.net |
| drinkwell pet fountain | 4 | 1,300 | 20 | $0.66 | 57 | 信息 | support.petsafe.net |
| petsafe automatic feeder | 4 | 1,300 | 24 | $0.48 | 6 | 信息/交易 | support.petsafe.net/articles |
| petsafe smart feed automatic feeder | 3 | 590 | 27 | $0.36 | 10 | 信息/交易 | support.petsafe.net/articles |
| petsafe pet feeder manual | 1 | 170 | 8 | $1.02 | 42 | 信息/交易 | petsafe.net/media/manuals |
| petsafe feeder manual | 1 | 170 | 14 | $1.02 | 42 | 信息 | petsafe.net/media/manuals |

> petsafe.net 喂食器词的流量极低（feeder 类词合计流量 <200），原因是**商业/购买流量都流向了 petsafe.com**，petsafe.net 只吃到使用手册与故障排查流量。喂食器品类的 SEO 战场实际在第三方评测站和 Amazon。

### 官网 TOP 自然关键词（wopet.com 喂食器相关，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| wopet automatic pet feeder | 2 | 1,300 | 16 | $0.27 | 106 | 信息/交易 | wopet.com/user-manual-download |
| wopet automatic pet feeder | 3 | 1,300 | 16 | $0.27 | 84 | 信息/交易 | wopet.com/shop/automatic-feeder |
| wopet auto feeder | 1 | 320 | 19 | $0.20 | 79 | 交易/导航 | wopet.com/shop/automatic-feeder |
| wopet automatic feeder | 1 | 210 | 31 | $0.22 | 52 | 交易 | wopet.com/shop |
| wopet automatic pet feeder manual | 1 | 260 | 5 | — | 34 | 信息/交易 | wopet.com/uploads/...pdf |
| wopet automatic cat feeder | 1 | 90 | 26 | $0.49 | 22 | 交易 | wopet.com/shop/automatic-feeder |
| wopet feeder | 2 | 170 | 15 | $0.29 | 22 | 交易/导航 | wopet.com/shop |
| cat with automatic feeder | 33 | 22,200 | 51 | $0.59 | 6 | 信息 | wopet.com/cats/... |

> Wopet 流量几乎全部依赖**品牌词**，非品牌类大词排名极靠后（`cat with automatic feeder` 排第 33）。说明 Wopet 在通用品类词上没有内容护城河，是典型可绕过的中型品牌。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| petlibro alternative | 30 | — | — | 信息 | ⭐ 量小但存在替代意图 |
| petsafe alternative | — | — | — | — | 几乎无量，GEO 机会 |
| wopet alternative | — | — | — | — | 几乎无量，GEO 机会 |
| best smart pet feeder | 30 | 49 | $0.94 | 信息 | 综述词，KD 高 |
| best wifi cat feeder | 30 | 33 | $0.99 | 信息 | ⭐ |
| petsafe vs petlibro | — | — | — | — | GEO 前哨 |
| wopet vs petsafe | — | — | — | — | GEO 前哨 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| automatic cat feeder | 27,100 | 44 | $0.60 | 信息 | 头部词，高竞争 |
| cat with automatic feeder | 22,200 | 48 | $0.60 | 信息 | 长尾变体，同上 |
| automatic dog feeder | 9,900 | 38 | $0.45 | 信息 | 大词 |
| auto animal feeders | 6,600 | 45 | $0.57 | 信息 | 广泛类别词 |
| microchip cat feeder | 5,400 | 34 | $0.58 | 信息 | ⭐ KD 可攻，RFID 本地控制更匹配 |
| automatic pet feeder | 5,400 | 48 | $0.57 | 信息 | 品类综述词 |
| best automatic cat feeder | 3,600 | 45 | $0.74 | 信息 | 综述词 |
| rfid cat feeder | 1,900 | 28 | $0.94 | 信息 | ⭐ KD 低，技术人群 |
| smart pet feeder | 880 | 36 | $0.53 | 信息 | 品类词 |
| wifi pet feeder | 210 | 38 | $0.67 | 信息 | 功能词 |
| automatic cat feeder with camera | 590 | 39 | $1.13 | 信息 | 附加功能词 |
| timed cat feeder | 1,900 | 50 | $0.48 | 信息 | 高竞争 |
| automatic wet food cat feeder | 1,600 | 18 | $0.69 | 信息 | ⭐ KD 低，湿粮场景 |
| wet food automatic feeder | 1,600 | 26 | $0.64 | 信息 | ⭐ |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| petsafe automatic feeder | 1,300 | 24 | $0.48 | 信息/交易 | ⭐ 中量，品牌词 |
| wopet automatic pet feeder | 1,300 | 16 | $0.27 | 信息/交易 | ⭐ KD 极低 |
| petlibro feeder | 3,600 | 47 | $0.73 | 信息/交易 | 市场占有率最高竞品 |
| wopet | 590 | 19 | $0.20 | 导航 | ⭐ 品牌词 KD 低 |
| wopet auto feeder | 320 | 19 | $0.20 | 交易 | ⭐ |
| petsafe smart feed | 210 | 30 | $0.62 | 导航 | 边界 ⭐ |
| wopet feeder | 170 | 15 | $0.29 | 交易 | ⭐ KD 极低 |
| petsafe feeder | 260 | 26 | $0.50 | 交易 | ⭐ |
| wopet cat feeder | 140 | 14 | $0.27 | 交易 | ⭐ |
| petkit feeder | 210 | 17 | $0.79 | 交易 | ⭐ |
| tuya pet feeder | 140 | 16 | $0.37 | 交易 | ⭐ 开源刷固件场景关联 |
| petsafe 5 meal feeder | 110 | 28 | $0.35 | 信息/导航 | ⭐ |
| petsafe subscription | 30 | 12 | $1.81 | 导航 | ⭐ 高 CPC，用户找退出路径 |
| petlibro subscription | 90 | 13 | $1.48 | 导航 | ⭐ 同上 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home assistant pet feeder | 20 | ~0 | — | 信息 | ⭐ GEO 前哨，技术先锋群体 |
| esphome pet feeder | 20 | ~0 | — | 信息 | ⭐ GEO 前哨 |
| pet feeder home assistant | 20 | ~0 | — | 信息 | ⭐ GEO 前哨 |
| diy automatic pet feeder | 20 | ~0 | — | 信息 | ⭐ |
| raspberry pi pet feeder | 20 | ~0 | — | 信息 | ⭐ |
| diy pet feeder | 20 | ~0 | — | 信息 | ⭐ |
| make automatic cat feeder | 20 | ~0 | — | 信息 | ⭐ |

> 自托管/开源词当前搜索量极低，但社区已有成熟 ESPHome 方案（offline-first 设计、Home Assistant 深度集成），属于**随着 Home Assistant 渗透率提升会爆发的 GEO 前哨词**。

---

## Olares 关联词（Phase 3）

**核心逻辑：PetSafe/Wopet 的云依赖 = 单点故障，ESPHome DIY 喂食器在 Olares+Home Assistant 生态里实现"完全本地、零订阅、无限自动化"，这是从"被动服务"到"自主掌控"的叙事转折点。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| home assistant pet feeder | 20 | ~0 | — | Olares 跑 Home Assistant，ESPHome 喂食器直接集成，无需云 | ⭐⭐⭐ |
| esphome pet feeder | 20 | ~0 | — | ESPHome 是 Olares 生态内推荐的 DIY IoT 固件，GEO 先手 | ⭐⭐⭐ |
| pet feeder home assistant | 20 | ~0 | — | 同上，用户意图更明确（已知 HA） | ⭐⭐⭐ |
| petsafe subscription | 30 | 12 | $1.81 | Olares+ESPHome 一次性拥有，无月费，叙事：Stop Renting | ⭐⭐⭐ |
| petlibro subscription | 90 | 13 | $1.48 | 同上，市场覆盖更广的竞品 | ⭐⭐⭐ |
| wopet automatic pet feeder | 1,300 | 16 | $0.27 | 低 KD 大量词，Wopet 平替/对比文章切入 | ⭐⭐ |
| tuya pet feeder | 140 | 16 | $0.37 | Tuya 基座喂食器可刷 ESPHome（局域网接管），Olares+HA 接管全程 | ⭐⭐ |
| rfid cat feeder | 1,900 | 28 | $0.94 | 微芯片/RFID 喂食器强调"知道是哪只猫"——本地识别 > 云推送，HA 可编写多猫策略 | ⭐⭐ |
| automatic wet food cat feeder | 1,600 | 18 | $0.69 | DIY 方案可接温控，云商品无法做到；Olares 上的 HA 自动化调度 | ⭐⭐ |
| petsafe automatic feeder | 1,300 | 24 | $0.48 | PetSafe alternative 文章切入 | ⭐⭐ |
| diy automatic pet feeder | 20 | ~0 | — | 直接教程文，Olares 跑 ESPHome + HA 组合 | ⭐⭐ |
| microchip cat feeder | 5,400 | 34 | $0.58 | 讲本地 RFID 识别 vs 云服务，Olares 隐私角度 | ⭐ |
| wifi pet feeder | 210 | 38 | $0.67 | 信息文可植入"本地 WiFi 控制 vs 云控"对比 | ⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| automatic cat feeder | 27,100 | 44 | $0.60 | 信息 | 次级 | 头部综述词，高竞争；作为长文的 H2 植入，讲本地控制方案段落 |
| microchip cat feeder | 5,400 | 34 | $0.58 | 信息 | 主词候选 | KD=34 相对可攻；讲本地 RFID 识别 vs 云端 AI 识别，隐私角度 |
| rfid cat feeder | 1,900 | 28 | $0.94 | 信息 | 主词候选 | ⭐ KD<30，量近 2K；ESPHome RFID 方案是核心素材 |
| automatic wet food cat feeder | 1,600 | 18 | $0.69 | 信息 | 主词候选 | ⭐ KD=18 极低，量 1.6K；DIY 温控投喂方案亮点 |
| smart pet feeder | 880 | 36 | $0.53 | 信息 | 次级 | 作为长文次关键词，植入本地 smart feeder 概念 |
| petsafe automatic feeder | 1,300 | 24 | $0.48 | 信息/交易 | 主词候选 | ⭐ 品牌词但 KD=24；"PetSafe alternative"文章支柱词 |
| wopet automatic pet feeder | 1,300 | 16 | $0.27 | 信息/交易 | 主词候选 | ⭐⭐ KD=16，量 1.3K；Wopet alternative/review 文章 |
| petlibro subscription | 90 | 13 | $1.48 | 导航 | 主词候选 | ⭐ KD=13，CPC 高说明用户决策痛点；"no subscription pet feeder"内容 |
| petsafe subscription | 30 | 12 | $1.81 | 导航 | 次级 | ⭐ KD=12，高 CPC；量小但商业意图极强，并入订阅对比文 |
| wopet | 590 | 19 | $0.20 | 导航 | 次级 | ⭐ 品牌词 KD=19，可做 Wopet 综合评测文把流量收进来 |
| tuya pet feeder | 140 | 16 | $0.37 | 交易 | 次级 | ⭐ KD=16；Tuya 刷 ESPHome 教程，Olares+HA 接管角度 |
| best wifi cat feeder | 30 | 33 | $0.99 | 信息 | 次级 | 综述词，KD 可接受；做最佳 WiFi 喂食器对比内容的次词 |
| home assistant pet feeder | 20 | ~0 | — | 信息 | GEO | ⭐⭐⭐ 近零量，领域早期词；抢 AI Overview 引用位关键词 |
| esphome pet feeder | 20 | ~0 | — | 信息 | GEO | ⭐⭐⭐ 同上，最精准 Olares 场景词 |
| pet feeder home assistant | 20 | ~0 | — | 信息 | GEO | ⭐⭐⭐ 同上 |
| diy automatic pet feeder | 20 | ~0 | — | 信息 | GEO | ⭐⭐ DIY 教程词，技术受众，GEO+次级 |
| petsafe smart feed | 210 | 30 | $0.62 | 导航 | 次级 | KD=30 边界；并入 PetSafe 评测文 |
| wopet cat feeder | 140 | 14 | $0.27 | 交易 | 次级 | ⭐ KD=14 极低；Wopet 文章引流词 |

---

## 核心洞见

### 1. 品牌护城河

**petsafe.net 护城河很弱**（喂食器流量<200 US/月），因为 PetSafe 是多品类宠物硬件巨头，喂食器只是其中一条线，SEO 重心在无线围栏和训练产品。真正的喂食器 SEO 战场是第三方评测站（wirecutters/goodhousekeeping 等）和 Amazon 评论，不在品牌自有域名。**Wopet 护城河更弱**——所有排名均为品牌词，任何"automatic cat feeder"品类词上的内容都可以绕过它。

### 2. 可复制的打法

- 评测站/横评文章是主流打法（"best automatic cat feeder 2026"类词由第三方评测站把持）。
- Wopet 做了少量 informational 内容（如"can I leave my cats alone for a week with an auto feeder"），但整体内容体系薄弱，容易被专业内容超越。
- **没有一家品牌商在"local control/no cloud/esphome"方向布局**——这是蓝海。

### 3. 对 Olares 最关键的词

1. **`rfid cat feeder`**（1,900/mo，KD=28）：本地 RFID 身份识别 vs 云端 AI，Olares 隐私叙事最强锚。
2. **`automatic wet food cat feeder`**（1,600/mo，KD=18）：DIY 温控喂食器（ESPHome + 温度传感器）vs 商品方案无法覆盖，差异化最清晰。
3. **`wopet automatic pet feeder`**（1,300/mo，KD=16）：覆盖 Wopet 搜索人群，KD 极低，替代文章门槛最低。

### 4. 最大攻击面

- **云依赖/断网风险**：PetSafe Smart Feed 断网后只能维持本地时刻表，不能远程触发或修改；Wopet 在电池供电时 App 完全不可用。这是"云喂食器其实是半离线产品"的关键痛点。
- **订阅蔓延**：PetSafe 对 GPS 围栏等产品收取 Connectivity Services 订阅费，用户搜索"petsafe subscription"时 CPC=$1.81（显示高商业决策焦虑）。
- **隐私与数据所有权**：两者均将喂食记录上传至厂商服务器，无本地存储选项。
- **无 API/无自动化**：无法接入 Home Assistant、IFTTT 之外的第三方系统；无法基于家中传感器、日历、天气等数据做联动喂食。

### 5. 隐藏低 KD 金矿

- `automatic wet food cat feeder`（1,600/mo，KD=18）⭐⭐——量大 KD 低，DIY 温控方案天然差异化。
- `wopet feeder`（170/mo，KD=15）、`wopet cat feeder`（140/mo，KD=14）——极低 KD，Wopet 用户是潜在迁移人群。
- `tuya pet feeder`（140/mo，KD=16）——Tuya 基座机器可刷 ESPHome，技术受众直接转化率高。
- `petsafe subscription`（30/mo，KD=12，CPC=$1.81）——量小但每次点击价值高，写"how to stop paying for petsafe subscription + alternative"类文章。

### 6. GEO 前瞻布局

以下词当前接近零量，但对应的技术社区（ESPHome/HA Reddit、Github）已在讨论，AI Overview 引用机会窗口开放：

- `home assistant pet feeder` / `esphome pet feeder` / `pet feeder home assistant`：在这三个词上发布教程文，被 Perplexity/ChatGPT 引用的可能性很高。
- `petsafe smart feed alternative`：近零量，但对应"订阅到期用户"人群，GEO 精准。
- `offline first pet feeder`：尚未出现为搜索词，但概念成立，chonk-o-matic 已有 GitHub 项目（offline-first 哲学）。
- `local smart pet feeder`：GEO 前哨，随 Matter/Home Assistant 普及有爆发潜力。

### 7. 与既有 olares-500-keywords 词表的关联

当前 olares-500-keywords 分析以 AI/云/开发工具类词为主，尚无 IoT 硬件替代类词。本次报告补充：
- **新增 IoT 替代词维度**：喂食器品类的 `rfid cat feeder`（1.9K）、`microchip cat feeder`（5.4K）是有实际搜索量的隐私/本地控制关联词。
- **ESPHome/HA 词簇**：`home assistant pet feeder`、`esphome pet feeder` 等作为 GEO 前哨词，与 Olares 的 Smart Home 场景（方向 7）深度配合。
- **订阅攻击面**：`petsafe subscription`、`petlibro subscription` 的高 CPC 表明消费者在主动逃离云订阅模型——与 Olares 的"Stop Renting. Start Owning"叙事直接对接。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_subdomains`、`domain_organic_organic`、`phrase_these`、`phrase_related`、`phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；IoT 品类全球量通常为美国的 2-4 倍。*
