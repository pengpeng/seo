# Shelly EM / Pro 3EM SEO 竞品分析报告

> 域名：shelly.com | SEMrush US | 2026-07-06
> Shelly Group SE（FRA:SLYG）旗下智能家居平台，EM/Pro 3EM 是其能源监测产品线——原生本地 RPC/MQTT API，无云强依赖，Home Assistant 官方集成首选。

---

## 项目理解（前置）

Shelly Group SE（前身 Allterco，保加利亚公司，FRA 上市）以无需 Hub、出厂即可关闭云服务的本地优先智能家居设备著称，累计出货 23M+ 台（FY2025 营收 €1.497 亿，+40.3%）。**Shelly EM（Gen3，单相/双相，2×50A CT）** 和 **Shelly Pro 3EM（DIN 导轨，三相，3×120A CT，支持 LAN+Wi-Fi+BT）** 是其能源监测主力产品，两者均通过 Gen2+ HTTP RPC API 提供无云本地读数，60 天 1 分钟历史数据存设备端，JSON/CSV 导出，MQTT WebSocket 全支持。在竞品中唯一兼顾"消费级价格（~$30-$80）+ 真本地 API + HA 官方集成 + 无订阅"四要素。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 本地优先智能家居平台，EM/Pro 3EM 是其零订阅能源计量设备 |
| 开源 / 许可证 | 固件部分闭源；**Shelly Scripting 脚本** 可定制；Gen2+ RPC API 完全公开 |
| 主仓库 | 无主开源仓库；社区工具见 [robeertm/shelly-energy-analyzer](https://github.com/robeertm/shelly-energy-analyzer) |
| 核心功能 | 双相/三相实时能耗计量、本地 RPC HTTP API、MQTT、60 天设备端历史、HA 官方集成、无订阅 |
| 商业模式 / 定价 | 硬件一次性购买：Shelly EM Gen3 ~$30–40；Pro 3EM ~$80–100；无月费/云订阅 |
| 差异化 / 价值主张 | 消费级价位下的**真本地 API**——Emporia Vue 云依赖、Sense 云 ML 必须在线、IotaWatt 需 SD 卡；Shelly EM 断网照常记录 |
| 主要竞品（初判） | Emporia Vue 3（emporiaenergy.com）、Sense（sense.com）、IotaWatt（iotawatt.com）、Eyedro（eyedro.com） |
| Olares Market | 未上架（硬件设备，无需上架）；**Home Assistant** 已在 Olares Market，是 Shelly EM 的软件端入口 |
| 来源 | [shelly.com/products/shelly-pro-3em-x1](https://www.shelly.com/products/shelly-pro-3em-x1)、[kb.shelly.cloud](https://kb.shelly.cloud/knowledge-base/shelly-pro-3em)、[energymeterhub.com](https://www.energymeterhub.com/articles/shelly-em-vs-emporia-vue-3) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | shelly.com（主力流量子域：us.shelly.com） |
| SEMrush Rank | 93,479 |
| 自然关键词数 | 5,149 |
| 月自然流量（US）| 20,879 |
| 自然流量估值 | $14,895/月 |
| 付费关键词数 | 35 |
| 月付费流量 | 5,680 |
| 付费流量估值 | $2,183/月 |
| 排名 1-3 位 | 385 词 |
| 排名 4-10 位 | 306 词 |
| 排名 11-20 位 | 388 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| us.shelly.com | 2,592 | 18,822 | 90.2% |
| www.shelly.com | 2,401 | 2,030 | 9.7% |
| corporate.shelly.com | 46 | 15 | 0.1% |
| 其余子域（portal/automations/asia 等）| — | <10 | — |

> us.shelly.com 承接了 90% 以上美国流量，为独立美国站架构；能源类关键词几乎全从此子域排名。

### 官网 TOP 自然关键词（流量前列，含能源子集）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| shelly | 1 | 33,100 | 61 | $0.29 | 860 | 商业/导航 | shelly.com/ |
| shelly relay | 1 | 1,000 | 38 | $0.18 | 800 | 商业 | collections/relays |
| shelly usa | 1 | 880 | 40 | $0.33 | 704 | 导航 | us.shelly.com/ |
| shelly wall display | 1 | 880 | 29 | $0.21 | 704 | 商业 | docs |
| shelly 1 | 1 | 590 | 39 | $0.22 | 472 | 商业 | shelly-1-gen4 |
| **shelly em** | **1** | **480** | **20** | **$0.27** | **384** | 导航/交易 | shelly-em-gen3-50a |
| smart plug | 3 | 9,900 | 26 | $0.33 | 346 | 信息/商业 | collections/smart-plugs |
| shelly smart switch | 1 | 390 | 39 | $0.24 | 312 | 商业 | smart-switches-dimmers |
| shelly plug | 1 | 390 | 28 | $0.22 | 312 | 商业 | shelly-plug-us |
| shelly switch | 1 | 320 | 23 | $0.19 | 256 | 商业 | smart-switches-dimmers |
| — 能源子集（URL = collections/smart-energy-monitoring）— | | | | | | | |
| shelly energy monitor | 1 | 70 | 20 | $0.19 | 56 | 信息 | smart-energy-monitoring |
| smart energy monitor home | 7 | 720 | 27 | $0.65 | 17 | 信息 | smart-energy-monitoring |
| energy monitoring device | 4 | 260 | 29 | $0.81 | 9 | 信息 | smart-energy-monitoring |
| wifi energy meter | 1 | 70 | 11 | $1.06 | 9 | 信息 | energy-metering |
| wireless energy monitor | 1 | 70 | 21 | $0.00 | 9 | 信息 | smart-energy-monitoring |
| energy consumption monitor | 9 | 720 | 27 | $0.73 | 6 | 信息 | smart-energy-monitoring |
| smart energy meter | 7 | 1,600 | 46 | $0.99 | 30 | 信息 | energy-metering |

**洞察**：shelly.com 的能源监测集合页面（`/collections/smart-energy-monitoring`）流量极低（合计约 150/月），相比品牌词（860）和 relay 词（800）小得多。这说明 Shelly 的能源计量能力**被品牌整体叙事淹没**——没有专属 SEO 内容针对"home assistant energy monitor"、"local energy monitor"这类长尾词，留下大量空白给第三方内容站。

### 付费词（Google Ads）

Shelly.com 购买 35 个付费词，以品牌/relay 类词为主（`relay` 月量 74,000，KD64，估计是战略性买量）。能源监测方向未见付费投放，说明此赛道尚未被 Shelly 自身认真经营。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| emporia vue | 2,900 | 34 | $0.57 | 商业/交易 | 最大竞品，云优先 |
| sense energy monitor | 1,600 | 34 | $0.67 | 导航/信息 | AI 设备检测，纯云 |
| iotawatt | 880 | 33 | $0.58 | 导航 | 开源竞品，量小但精准 |
| emporia vue 3 | 1,300 | 16 | $0.51 | 商业 | ⭐ 最新版竞品，KD 仅 16 |
| eyedro energy monitor | 30 | 7 | $0.84 | 导航/交易 | ⭐ 小众竞品，KD 极低 |
| shelly em alternative | 10 | 0 | $0.00 | — | ⭐ 零 KD，替代文切入点 |
| emporia vue alternative | 20 | 0 | $0.71 | — | ⭐ 零 KD，抢先建锚点 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| electricity usage monitor | 1,900 | 22 | $0.73 | 信息 | ⭐ 大量低 KD，首选品类词 |
| home energy monitor | 1,600 | 29 | $0.77 | 信息 | ⭐ 核心品类词 |
| power monitor | 1,300 | 34 | $1.08 | 信息 | 泛用词 |
| energy monitoring system | 1,000 | 28 | $1.41 | 信息 | ⭐ |
| whole home energy monitor | 880 | 28 | $0.49 | 商业 | ⭐ |
| home energy monitoring system | 720 | 26 | $1.50 | 信息 | ⭐ 高 CPC，B2B 倾向 |
| smart home energy monitor | 720 | 23 | $0.65 | 商业/信息 | ⭐ |
| energy consumption monitor | 720 | 27 | $0.73 | 信息 | ⭐ |
| smart energy monitor home | 720 | 27 | $0.65 | 信息 | ⭐ |
| home energy monitoring | 480 | 25 | $0.67 | 信息 | ⭐ |
| best home energy monitor | 480 | 28 | $0.72 | 信息 | ⭐ |
| home power monitor | 480 | 28 | $0.67 | 信息 | ⭐ |
| home electricity monitor | 390 | 27 | $0.67 | 商业/信息 | ⭐ |
| home energy monitors | 480 | 24 | $0.77 | 信息 | ⭐ |
| home assistant energy monitor | 210 | 25 | $0.57 | 商业 | ⭐ 核心 Olares 切入词 |
| smart energy monitor | 140 | 12 | $0.94 | 信息 | ⭐ 低 KD！ |
| three phase energy meter | 110 | 14 | $2.19 | 商业/信息 | ⭐ Pro 3EM 对应词，KD 低+CPC 高 |
| home assistant energy dashboard | 140 | 20 | $0.00 | 商业 | ⭐ |
| solar energy monitor | 140 | 27 | $1.01 | 信息 | ⭐ PV 扩展场景 |
| zigbee home energy monitor | 90 | 6 | $0.38 | 商业/信息 | ⭐ KD 极低 |
| 3 phase energy monitor | 50 | 6 | $2.03 | 信息 | ⭐ KD 极低+CPC 高 |
| diy home energy monitor | 40 | 0 | $0.00 | — | ⭐ 零 KD |
| best home assistant energy monitor | 40 | 0 | $0.00 | — | ⭐ 零 KD，精准匹配 |
| din rail energy meter | 30 | 0 | $0.00 | — | ⭐ Pro 3EM 精准词 |
| eyedro energy monitor | 30 | 7 | $0.84 | 导航/交易 | ⭐ |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| shelly em | 590 | 13 | $0.31 | 导航/交易 | ⭐ 品牌词，KD 仅 13！ |
| shelly pro 3em | 390 | 17 | $0.29 | 商业 | ⭐ |
| shelly 3em | 210 | 12 | $0.37 | 商业 | ⭐ KD 最低 |
| shelly home assistant | 140 | 26 | $0.15 | 商业 | ⭐ 集成词 |
| shelly power monitor | 110 | 27 | $0.18 | 信息 | ⭐ |
| shelly energy monitor | 70 | 20 | $0.19 | 信息 | ⭐ |
| shelly 3 phase energy meter | 30 | 8 | $0.79 | 商业 | ⭐ KD 极低 |
| shelly power monitoring | 40 | 26 | $0.18 | 商业 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home assistant energy dashboard | 140 | 20 | $0.00 | 商业 | ⭐ Olares HA 集成点 |
| shelly em home assistant | 20 | 0 | $0.00 | — | ⭐ 零 KD，精准 |
| energy dashboard home assistant | 20 | 0 | $0.00 | — | ⭐ 零 KD |
| diy home energy monitor | 40 | 0 | $0.00 | — | ⭐ 动手族目标 |
| best home assistant energy monitor | 40 | 0 | $0.00 | — | ⭐ 精准商业意图 |
| zigbee home energy monitor | 90 | 6 | $0.38 | 商业/信息 | ⭐ HA 生态词 |
| home energy monitor open source | 0 | 0 | $0.00 | — | GEO 词，量近零但语义强 |
| energy monitor no subscription | 0 | 0 | $0.00 | — | GEO 词，痛点直击 |
| self hosted energy monitoring | 0 | 0 | $0.00 | — | GEO 词 |
| local energy monitor home assistant | 0 | 0 | $0.00 | — | GEO 词，精准 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Shelly EM 是硬件，Olares 是承载 Home Assistant 的本地 OS——"Shelly EM → 本地 RPC → HA on Olares → Energy Dashboard"构成完整零云能源监测栈，攻击 Emporia Vue（云依赖）和 Sense（云 ML）的最大痛点。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| best home assistant energy monitor | 40 | 0 | $0.00 | Olares 上的 HA + Shelly EM 是最完整的本地方案，零 KD 可抢先占位 | ⭐⭐⭐ |
| home assistant energy monitor | 210 | 25 | $0.57 | HA 运行在 Olares 上，Shelly EM 本地直连，无云账号，Energy Dashboard 全功能可用 | ⭐⭐⭐ |
| shelly em home assistant | 20 | 0 | $0.00 | 精准教程词：如何在 Olares 上的 HA 集成 Shelly EM | ⭐⭐⭐ |
| emporia vue alternative | 20 | 0 | $0.71 | Emporia 云强依赖 → Shelly EM + HA on Olares 是本地替代，数据不出家门 | ⭐⭐⭐ |
| diy home energy monitor | 40 | 0 | $0.00 | DIY 极客受众，Olares + HA + Shelly EM 构建无云监测栈，高度契合 | ⭐⭐⭐ |
| home assistant energy dashboard | 140 | 20 | $0.00 | HA Energy Dashboard 运行在 Olares 上，内容角度 = "如何在 Olares 设置 HA 能源面板" | ⭐⭐⭐ |
| shelly em alternative | 10 | 0 | $0.00 | 反向切入：其他设备（如 IotaWatt/Zigbee）+ HA on Olares 都能做到类似功能 | ⭐⭐ |
| 3 phase energy monitor | 50 | 6 | $2.03 | Pro 3EM → HA on Olares，三相监测+太阳能/EV 充电自动化，KD 6 极低 | ⭐⭐⭐ |
| zigbee home energy monitor | 90 | 6 | $0.38 | Zigbee CT 传感器（如 SMLIGHT）+ Zigbee2MQTT on Olares，同样路径 | ⭐⭐ |
| smart energy monitor | 140 | 12 | $0.94 | KD 12，泛品类词，Olares 搭配多种本地监测硬件都能实现 | ⭐⭐ |
| electricity usage monitor | 1,900 | 22 | $0.73 | 量最大的低 KD 词，主攻信息意图，Olares 角度 = 本地实时用电可视化 | ⭐⭐ |
| three phase energy meter | 110 | 14 | $2.19 | Pro 3EM 精准对应，DIN 导轨 + HA on Olares，工商业/三相家庭场景 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| electricity usage monitor | 1,900 | 22 | $0.73 | 信息 | 主词候选 | 量大 KD 低，信息意图，Olares 角度=本地可视化所有用电数据 |
| home energy monitor | 1,600 | 29 | $0.77 | 信息 | 主词候选 | 核心品类词，KD29 尚可，Olares HA + Shelly EM 的自然锚点 |
| home energy monitoring system | 720 | 26 | $1.50 | 信息 | 主词候选 | CPC 高暗示商业价值，Olares = 完整本地系统 |
| smart home energy monitor | 720 | 23 | $0.65 | 商业/信息 | 主词候选 | KD 23，Shelly EM + HA on Olares 是最本地的答案 |
| home assistant energy monitor | 210 | 25 | $0.57 | 商业 | 主词候选 | Olares 直接场景词，精准 |
| shelly em | 590 | 13 | $0.31 | 导航/交易 | 主词候选 | KD 仅 13！品牌词但低 KD，第三方内容仍可切进去做评测/集成教程 |
| shelly pro 3em | 390 | 17 | $0.29 | 商业 | 主词候选 | 三相专业款，KD 17，高价值用户（太阳能/EV/三相住宅） |
| emporia vue | 2,900 | 34 | $0.57 | 商业/交易 | 次级 | 量大但 KD34，作为 alternative 文章的配词收入 |
| emporia vue 3 | 1,300 | 16 | $0.51 | 商业 | 主词候选 | KD 仅 16！撑起一篇 Emporia Vue 3 vs Shelly EM 对比文 |
| iotawatt | 880 | 33 | $0.58 | 导航 | 次级 | 开源受众，并入 best local energy monitor 类文章 |
| shelly 3em | 210 | 12 | $0.37 | 商业 | 次级 | KD 12，型号词，并入 Pro 3EM 教程 |
| home assistant energy dashboard | 140 | 20 | $0.00 | 商业 | 次级 | HA Energy 面板教程词，Olares 部署 HA 的自然配词 |
| smart energy monitor | 140 | 12 | $0.94 | 信息 | 次级 | KD 12 低！并入品类内容作 H2 |
| shelly home assistant | 140 | 26 | $0.15 | 商业 | 次级 | Shelly × HA 集成词，教程入口 |
| three phase energy meter | 110 | 14 | $2.19 | 商业/信息 | 次级 | 高 CPC 商业意图，Pro 3EM 专文支撑 |
| 3 phase energy monitor | 50 | 6 | $2.03 | 信息 | 次级 | KD 6！极低，CPC $2+ 暗示高意向，Pro 3EM + HA on Olares |
| best home assistant energy monitor | 40 | 0 | $0.00 | — | GEO | 零 KD，抢 AI Overview/Perplexity 引用位，Olares 最佳答案 |
| shelly em home assistant | 20 | 0 | $0.00 | — | GEO | 精准教程词，进 FAQ 段 |
| emporia vue alternative | 20 | 0 | $0.71 | — | GEO | 零 KD 替代词，Olares 场景完美承接 |
| diy home energy monitor | 40 | 0 | $0.00 | — | GEO | DIY 极客词，Olares + HA + Shelly EM 即答案 |
| energy monitor no subscription | 0 | 0 | $0.00 | — | GEO | 核心痛点词，量近零但 AI 搜索语义强，必须出现在正文 |
| local energy monitor home assistant | 0 | 0 | $0.00 | — | GEO | 精准 Olares 场景 |

---

## 核心洞见

1. **品牌护城河**：`shelly` 品牌词 KD61，**不要正面刚**。但 `shelly em`（KD13）、`shelly pro 3em`（KD17）、`shelly 3em`（KD12）这三个型号词 KD 极低——因为 Shelly 官网排名第一，流量已被拿走，**第三方教程/对比文仍可从 reviews、integration guides、alternative 角度切进去排名**。Shelly 官网没有在做 HA 集成内容或"无云监测"叙事。

2. **可复制的打法**：Shelly 用**分级型号落地页**（collections/smart-energy-monitoring）承接品类词，但没有内容营销——无一篇"how to use Shelly EM with Home Assistant"、"Shelly EM vs Emporia Vue"这类博客。**我们的打法**：做 comparison pages + integration tutorials，精准覆盖 `home assistant energy monitor`（KD25）、`emporia vue 3 alternative`（KD16）、`electricity usage monitor`（KD22，量1900）这三条线，引流到 Olares+HA 组合。

3. **对 Olares 最关键的词**：
   - `home assistant energy monitor`（210/月，KD25）——直接说 HA on Olares 就是最佳本地能源监测方案
   - `electricity usage monitor`（1,900/月，KD22）——量最大的可攻词，Olares+Shelly EM 完整回答
   - `best home assistant energy monitor`（40/月，KD0）——零 KD，GEO 必抢，Olares 直接命名

4. **最大攻击面**：**云依赖痛点**——Emporia Vue 官网明文说"数据流经 Emporia 云"，Sense 需云 ML 才能识别设备。`energy monitor no subscription`、`energy monitor without cloud`、`emporia vue alternative`（KD0）都是零竞争词，语义精准对应 Shelly EM + Olares 的本地无云方案。CPC 高词（`home energy monitoring system` $1.50、`3 phase energy monitor` $2.03）暗示商业购买意向强。

5. **隐藏低 KD 金矿**：
   - `electricity usage monitor`：1,900/月 + KD22——量最大的低 KD 品类词，Shelly.com 未认真争取
   - `emporia vue 3`：1,300/月 + KD16——竞品型号词，KD 低于预期，可做 Emporia Vue 3 vs Shelly EM 对比文
   - `smart energy monitor`：140/月 + KD12——KD12 极低，纯品类词
   - `3 phase energy monitor`：50/月 + KD6 + CPC$2.03——Pro 3EM 精准词，极低 KD 高商业意向
   - `zigbee home energy monitor`：90/月 + KD6——HA 生态词，KD 极低

6. **GEO 前瞻布局**（近零量但 AI 搜索语义强，抢 AI Overview/Perplexity 引用位）：
   - `best home assistant energy monitor`（KD0）
   - `energy monitor no subscription`（KD0）——Sense/Emporia 的核心痛点
   - `local energy monitoring home assistant`（KD0）
   - `shelly em esphome home assistant`（KD0）——深度技术词，极客受众
   - `shelly pro 3em home assistant solar`（KD0）——三相+光伏场景
   - `self hosted energy monitoring`（KD0）——Olares 生态关键词

7. **与既有 olares-500-keywords 的关联**：`home assistant energy monitor` 是 iot.md 已标注的核心机会词（第 275 行）。本报告额外发现 `electricity usage monitor`（1,900/月，KD22）是量级更大的未开垦词；`emporia vue 3`（1,300/月，KD16）是前文未覆盖的高价值竞品词。`shelly em`（590/月，KD13）本身也是低 KD 可做的型号词，之前 iot.md 仅作为方向词列出，本报告确认其 KD 13 具备主词价值。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_related、phrase_fullsearch、phrase_these、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
