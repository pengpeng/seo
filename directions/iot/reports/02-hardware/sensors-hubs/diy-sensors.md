# DIY Smart Home Sensors（ESPHome / Zigbee2MQTT）SEO 竞品分析报告

> 域名：esphome.io（主）+ zigbee2mqtt.io（次） | SEMrush US | 2026-07-06
> 品类：DIY 智能传感器（门窗/PIR/mmWave/温湿度/水浸）——纯本地、无订阅、ESP32/Zigbee 固件两翼，与 Home Assistant 深度绑定

---

## 项目理解（前置）

ESPHome 是由 Open Home Foundation（Nabu Casa 主导）维护的开源固件框架，用户无需 C++ 即可用 YAML 为 ESP32/ESP8266/RP2040 等微控制器定义传感器逻辑、OTA 升级与 Home Assistant 原生 API 集成。Zigbee2MQTT（Z2M）将 Zigbee 设备通过 MQTT 暴露给任意智能家居平台，无需厂商专属 Hub。两者共同构成 DIY 本地传感器生态的基础设施——ESPHome 覆盖 Wi-Fi 路径，Z2M 覆盖 Zigbee 低功耗路径，均与 Home Assistant 深度集成，支持 5,473+ 款 Zigbee 设备。Olares Market 已上架 Home Assistant，ESPHome 设备可通过 HA on Olares 直接管理，形成"边缘传感器 → 本地 HA → Olares Agent"完整私有链路。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源固件框架（ESPHome）+ Zigbee-MQTT 桥（Z2M），让廉价微控制器/Zigbee 模块成为纯本地智能传感器 |
| 开源 / 许可证 | ESPHome: MIT；Zigbee2MQTT: GPL-3.0 |
| 主仓库 | [esphome/esphome](https://github.com/esphome/esphome)（★ ~9k）；[Koenkk/zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt)（★ ~15.2k） |
| 核心功能 | YAML 定义固件、本地 HA native API、OTA 空中升级、ESPHome Zigbee 组件（2026.5.0 原生支持 ESP32-H2/C6 + nRF52）；Z2M 支持 5,473+ 设备 |
| 商业模式 / 定价 | 完全免费开源；硬件成本 $5–30（ESP32 + 传感器模块）；无订阅 |
| 差异化 / 价值主张 | **零云依赖**：数据只在局域网流转；可修复/可定制；成本极低；与 HA 深度整合无任何账号墙 |
| 主要竞品（初判）| Tasmota（固件竞品）、ZHA（Zigbee 协调器竞品）、Aqara Hub / SONOFF 商业方案（即买即用）、Apollo Automation / Everything Presence One（成品 ESPHome 设备商） |
| Olares Market | HA on Olares 已上架；ESPHome 设备通过 HA 管理；Z2M 以 HA Add-on 形态运行 |
| 来源 | [esphome.io](https://esphome.io)；[esphome.io/changelog/2026.5.0](https://esphome.io/changelog/2026.5.0/)；[github.com/esphome/esphome](https://github.com/esphome/esphome)；[github.com/Koenkk/zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt)；[zigbee2mqtt.io](https://www.zigbee2mqtt.io) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | esphome.io | zigbee2mqtt.io |
|------|-----------|----------------|
| 域名 | esphome.io | zigbee2mqtt.io |
| SEMrush Rank | 111,136 | 479,289 |
| 自然关键词数 | 4,198 | 902 |
| 月自然流量（US）| 17,268 | 3,025 |
| 自然流量估值 | $7,327/月 | $1,843/月 |
| 付费关键词数 | 0 | 0 |
| 月付费流量 | 0 | 0 |

> 两站均零广告投放，是典型的开源社区文档站。esphome.io 月流量 17k+ 与估值偏低（$7.3k），说明词库以零 CPC 的技术/品牌词为主；真实商业价值通过带动 HA 生态而非广告变现。

### 子域名流量分布（esphome.io）

| 子域名 | 说明 | 代表流量词 |
|--------|------|----------|
| esphome.io | 主文档站，组件参考 | esphome (5,280)、esphome presence sensor (96) |
| web.esphome.io | 在线刷机工具 | esphome online flasher (800)、esphome flasher (312) |
| devices.esphome.io | 设备目录（型号页） | esp32relay x1 (218)、esphome devices (168) |

### esphome.io TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| esphome | 1 | 6,600 | 51 | $1.73 | 5,280 | 导航 | esphome.io/ |
| esp home | 1 | 1,900 | 28 | $1.73 | 1,520 | 导航 | esphome.io/ |
| esp io | 1 | 1,600 | 65 | $0 | 1,280 | 导航 | esphome.io/ |
| esphome online flasher | 1 | 1,000 | 40 | $0 | 800 | 导航 | web.esphome.io/ |
| esphome bluetooth proxy | 1 | 590 | 45 | $1.20 | 472 | 功能 | …/bluetooth_proxy/ |
| esphome web | 1 | 590 | 28 | $0 | 472 | 导航 | web.esphome.io/ |
| esphome flasher | 1 | 390 | 37 | $0 | 312 | 导航 | web.esphome.io/ |
| sun direction esp | 1 | 1,900 | 48 | $0 | 250 | 信息 | …/components/sun/ |
| esp32relay x1 | 1 | 880 | 18 | $0 | 218 | 信息 | devices.esphome.io/ |
| esphome ota password | 1 | 260 | 0 | $0 | 208 | 信息 | …/ota/esphome/ |
| esphome device builder | 1 | 210 | 47 | $0 | 168 | 信息 | …/getting_started_hassio/ |
| esphome devices | 1 | 210 | 29 | $0.39 | 168 | 导航 | devices.esphome.io/ |
| esphome home assistant | 1 | 170 | 23 | $0 | 136 | 信息 | …/getting_started_hassio/ |
| esphome projects | 1 | 140 | 22 | $0 | 112 | 信息 | esphome.io/projects/ |
| esphome zigbee | 1 | 140 | 21 | $0 | 112 | 信息 | …/components/zigbee/ |
| esphome homeassistant | 1 | 140 | 25 | $0 | 112 | 信息 | …/getting_started_hassio/ |
| esphome presence sensor | 1 | 390 | 15 | $0 | 96 | 商业 | …/components/sensor/ld2410/ |
| hlk-ld2420 | 2 | 720 | 22 | $0 | 95 | 信息 | …/sensor/ld2420/ |
| home assistant esphome | 1 | 110 | 27 | $0 | 88 | 信息 | …/getting_started_hassio/ |
| bme280 | 6 | 1,900 | 28 | $0.87 | 57 | 信息 | …/cookbook/bme280_environment/ |

> **关键观察**：品牌词（esphome / esp home / esp io）占总流量 >60%，牢不可破。`sun direction esp` 因组件文档带来 250 流量——证明**组件型文档页对非品牌词有意外渗透**。`hlk-ld2420`（mmWave 模块型号）排第 2 位，说明**型号词是低 KD 自然流量来源**。非品牌类场景词（`home assistant door sensor` / `zigbee motion sensor` 等）在 esphome.io 几乎没有专题内容，是最大攻击面。

### zigbee2mqtt.io TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | 流量 | 意图 |
|--------|------|------|----|------|------|
| zigbee2mqtt | 1 | 1,900 | 37 | 1,520 | 导航 |
| zigbee 2 mqtt | 1 | 390 | 49 | 312 | 导航 |
| home assistant zigbee2mqtt | 1 | 140 | 20 | 112 | 信息 |
| zigbee mqtt | 1 | 110 | 31 | 88 | 信息 |
| zigbee devices | 3 | 1,300 | 16 | 84 | 信息 |
| z2m | 1 | 210 | 17 | 52 | 导航 |
| zigbee2mqtt home assistant | 2 | 390 | 28 | 31 | 信息 |
| sonoff snzb-06p | 4 | 390 | 11 | 11 | 信息 |

> Z2M 流量较小但品牌护城河同样稳固；`zigbee devices`（KD 16，1,300 月量）只排第 3，有可切入空间。

### 付费词（Google Ads）

两站均无任何付费投放。开源社区靠口碑、GitHub、YouTube 教程引流，不打广告。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 有机竞争域名（Top 5）

| 域名 | 相关度 | 共同词 | 月流量 |
|------|--------|--------|--------|
| home-assistant.io | 0.05 | 459 | 369,622 |
| espressif.com | 0.11 | 185 | 63,225 |
| randomnerdtutorials.com | 0.08 | 161 | 14,436 |
| m5stack.com | 0.06 | 67 | 18,318 |
| tasmota.github.io | 0.08 | 62 | 2,861 |
| apolloautomation.com | 0.05 | 32 | 2,328 |

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| zha vs zigbee2mqtt | 210 | 16 | $0 | 信息 | ⭐ 两种 Zigbee 协调器对比 |
| zigbee2mqtt vs zha | 110 | 7 | $0 | 信息 | ⭐ KD 7，对比文极易排名 |
| tasmota vs esphome | 90 | 16 | $0 | 商业 | ⭐ 固件选型对比 |
| esphome vs tasmota | 20 | 0 | $0 | — | ⭐ |
| esphome alternative | 20 | 0 | $0 | — | ⭐ GEO 前哨 |
| zigbee2mqtt alternative | 20 | 0 | $0 | — | ⭐ GEO 前哨 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| smart home sensors | 1,000 | 39 | $1.76 | 商业 | 高量，竞争适中 |
| mmwave sensor | 720 | 15 | $0.40 | 信息/商业 | ⭐ 低 KD、高量 |
| presence sensor | 720 | 33 | $0.57 | 商业 | 存在感知大词 |
| everything presence one | 720 | 16 | $1.63 | 信息 | ⭐ ESPHome 设备品牌词，KD 低 |
| apollo automation | 720 | 31 | $0 | 导航 | ESPHome 生态成品商 |
| door and window sensors | 590 | 19 | $5.28 | 商业 | ⭐ CPC $5.28，高商业价值 |
| home assistant door sensor | 480 | 12 | $1.29 | 商业 | ⭐ KD 12！商业意图 |
| zigbee coordinator | 480 | 27 | $0.43 | 商业 | ⭐ 基础设施词 |
| zigbee motion sensor | 480 | 9 | $0.37 | 商业 | ⭐ KD 9！全场景最低竞争之一 |
| temperature sensor home assistant | 390 | 16 | $0.42 | 信息 | ⭐ |
| zigbee temperature sensor | 320 | 12 | $0.43 | 商业 | ⭐ |
| home assistant temperature sensor | 320 | 18 | $0.47 | 信息 | ⭐ |
| contact sensor | 320 | 20 | $2.12 | 信息 | ⭐ CPC 高 |
| home assistant motion sensor | 210 | 9 | $0.52 | 商业 | ⭐ KD 9！ |
| zigbee water sensor | 210 | 12 | $0.44 | 商业 | ⭐ 漏水报警场景强 |
| human presence sensor | 260 | 19 | $0.88 | 商业 | ⭐ mmWave 趋势词 |
| mmwave presence sensor | 170 | 21 | $0.37 | 商业 | ⭐ |
| home assistant sensors | 170 | 13 | $0.45 | 信息 | ⭐ |
| home assistant presence detection | 140 | 16 | $0.57 | 信息 | ⭐ |
| apollo msr 2 | 210 | 19 | $0 | 信息 | ⭐ 成品设备型号 |
| hlk-ld2410 | 30 | 14 | $0.83 | 信息 | ⭐ mmWave 模块型号词 |
| apollo msr-2 | 90 | 5 | $0 | 信息 | ⭐⭐ KD **5**！极稀有 |

### 产品 / 功能词（ESPHome 品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| esphome presence sensor | 390 | 15 | $0 | 商业 | ⭐ esphome.io #1，但无专题教程 |
| what is esphome | 140 | 24 | $0 | 信息 | ⭐ 入门词 |
| esphome zigbee | 140 | 21 | $0 | 信息 | ⭐ 2026.5.0 新特性词 |
| esphome home assistant | 210 | 41 | $0 | 信息 | HA 整合核心词 |
| esphome docker | 110 | 33 | $0 | 信息 | 进阶安装词 |
| esp32 home assistant | 260 | 23 | $0.65 | 信息 | ⭐ |
| esp32 temperature sensor | 210 | 9 | $0.48 | 信息 | ⭐ KD 9！ |
| tasmota vs esphome | 90 | 16 | $0 | 商业 | ⭐ 固件选型对比 |
| hlk-ld2420 | 720 | 22 | $0 | 信息 | ⭐ 型号词带流量（已被 esphome.io 组件页排名） |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| home assistant local | 590 | 30 | $0 | 信息 | 本地化需求强 |
| home automation open source | 390 | 45 | $0.42 | 信息 | 大词，竞争较高 |
| open source smart home platform | 170 | 34 | $0 | 信息 | 自托管主题词 |
| open source smart home | 210 | 41 | $0 | 信息 | |
| local home automation | 20 | 0 | $3.43 | — | ⭐ CPC $3.43 高意图信号，GEO |
| smart home without cloud | 20 | 0 | $0.67 | — | ⭐ Olares 核心叙事，GEO |
| privacy smart home | 20 | 0 | $0 | — | ⭐ GEO |

---

## Olares 关联词（Phase 3）

**核心逻辑：ESPHome/Z2M 设备数据通过 Home Assistant on Olares 管理，形成「传感器→本地 HA→Olares AI Agent」私有链路。Olares 差异化叙事 = "装一个 Olares，买几个 ESP32 传感器或 Zigbee 模块，数据永远不出家门，Agent 掌握全屋上下文"——对位商业 Zigbee 方案（订阅 + 云依赖）的反叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| zigbee motion sensor | 480 | 9 | $0.37 | Z2M+HA on Olares 管理任何 Zigbee PIR，无需厂商 Hub；KD 最低 | ⭐⭐⭐ |
| home assistant door sensor | 480 | 12 | $1.29 | HA on Olares 一键部署；ESPHome DIY 门磁 $5，零订阅 | ⭐⭐⭐ |
| esphome presence sensor | 390 | 15 | $0 | ESPHome mmWave → HA on Olares 自动化，全本地存在感知 | ⭐⭐⭐ |
| temperature sensor home assistant | 390 | 16 | $0.42 | BME280/DHT22 + ESPHome + HA on Olares，$5 传感器命中高意图词 | ⭐⭐⭐ |
| zigbee temperature sensor | 320 | 12 | $0.43 | Aqara/Sonoff 温湿传感器 → Z2M on Olares，无需品牌 Hub | ⭐⭐⭐ |
| home assistant motion sensor | 210 | 9 | $0.52 | KD 极低；ESPHome PIR/mmWave + HA on Olares | ⭐⭐⭐ |
| esp32 temperature sensor | 210 | 9 | $0.48 | ESPHome + Olares HA；KD 9，最易排名的入门硬件教程词 | ⭐⭐⭐ |
| zigbee water sensor | 210 | 12 | $0.44 | 漏水报警场景；Z2M on Olares 实时告警，零订阅零云依赖 | ⭐⭐ |
| everything presence one | 720 | 16 | $1.63 | Apollo/EP1 成品 ESPHome 设备 → HA on Olares 管理；最易上手的 mmWave 方案 | ⭐⭐ |
| mmwave sensor | 720 | 15 | $0.40 | mmWave + ESPHome + HA on Olares = 完全本地占用感知，Agent 感知"有人在家" | ⭐⭐ |
| human presence sensor | 260 | 19 | $0.88 | 同上，Olares Agent 占用上下文应用场景 | ⭐⭐ |
| zha vs zigbee2mqtt | 210 | 16 | $0 | Olares 推荐 Z2M（更完整、设备支持更广），文章可做对比引流 | ⭐⭐ |
| zigbee2mqtt vs zha | 110 | 7 | $0 | 同族，KD 7；Z2M on Olares 对比叙事 | ⭐⭐ |
| apollo msr-2 | 90 | 5 | $0 | KD 5！成品 ESPHome 评测文极易排名，设备经 HA on Olares 管理 | ⭐⭐ |
| tasmota vs esphome | 90 | 16 | $0 | 两者均可与 HA on Olares 集成；Olares = 两者通吃的平台层 | ⭐⭐ |
| esphome zigbee | 140 | 23 | $0 | 2026.5.0 新特性，ESPHome 原生 Zigbee；Z2M on Olares 互补叙事 | ⭐⭐ |
| zigbee2mqtt home assistant | 390 | 28 | $0 | Z2M+HA on Olares 全栈部署教程词 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| everything presence one | 720 | 16 | $1.63 | 信息 | **主词候选** | 量最高+KD 低，ESPHome 成品设备，HA on Olares 直接管理；最大单词机会 |
| mmwave sensor | 720 | 15 | $0.40 | 信息/商业 | **主词候选** | 高量低 KD，ESPHome mmWave 栈是 Olares 本地 AI 占用感知的传感器前端 |
| home assistant door sensor | 480 | 12 | $1.29 | 商业 | **主词候选** | KD 12 + CPC $1.29 商业意图强；ESPHome $5 门磁 + HA on Olares 教程直接切入 |
| zigbee motion sensor | 480 | 9 | $0.37 | 商业 | **主词候选** | KD **9**！全品类最低竞争高量词；Z2M+HA on Olares 完整本地方案 |
| temperature sensor home assistant | 390 | 16 | $0.42 | 信息 | **主词候选** | 簇合计（+320 变体）量大；BME280+ESPHome 入门教程，Olares 本地 HA 落地 |
| esphome presence sensor | 390 | 15 | $0 | 商业 | **主词候选** | esphome.io 已 #1 但无专题教程；LD2410/2450 变体丰富，Olares 切入 HA 教程角度 |
| zigbee temperature sensor | 320 | 12 | $0.43 | 商业 | **主词候选** | KD 12，Z2M on Olares 无需品牌 Hub；品类词簇的温湿度核心词 |
| home assistant motion sensor | 210 | 9 | $0.52 | 商业 | **主词候选** | KD **9**！ESPHome PIR/mmWave + HA on Olares；极易排名 |
| esp32 temperature sensor | 210 | 9 | $0.48 | 信息 | **主词候选** | KD **9**！最易入门的 ESPHome 教程词；Olares HA 本地数据存储 |
| zigbee water sensor | 210 | 12 | $0.44 | 商业 | **主词候选** | KD 12，漏水报警场景强，"零订阅警报"叙事清晰 |
| human presence sensor | 260 | 19 | $0.88 | 商业 | **主词候选** | mmWave 趋势词，Olares Agent 占用感知上下文应用 |
| zha vs zigbee2mqtt | 210 | 16 | $0 | 信息 | **主词候选** | KD 16 对比文，Olares 推荐 Z2M（设备支持更广、MQTT 更灵活） |
| zigbee2mqtt home assistant | 390 | 28 | $0 | 信息 | **次级** | KD 偏高（28），并入 Z2M+HA on Olares 部署教程 |
| esphome zigbee | 140 | 21 | $0 | 信息 | **次级** | 2026.5.0 新特性词，时间窗口内写可吃早期流量 |
| home assistant presence detection | 140 | 16 | $0.57 | 信息 | **次级** | 并入 mmWave/presence 主题文 |
| what is esphome | 140 | 24 | $0 | 信息 | **次级** | 入门词，教程前置段落 |
| zigbee2mqtt vs zha | 110 | 7 | $0 | 信息 | **次级** | 同族 zha vs zigbee2mqtt，并入同篇 |
| tasmota vs esphome | 90 | 16 | $0 | 商业 | **次级** | 固件选型对比，Olares 平台兼容两者 |
| apollo msr-2 | 90 | 5 | $0 | 信息 | **次级** | KD **5**，ESPHome 设备评测并入 mmWave/presence 主题 |
| hlk-ld2410 | 30 | 14 | $0.83 | 信息 | **次级** | 型号词，并入 mmWave 教程长尾 |
| local home automation | 20 | 0 | $3.43 | — | **GEO** | CPC $3.43 暗示高商业意图；近零量，适合 FAQ 抢 AI Overview |
| smart home without cloud | 20 | 0 | $0.67 | — | **GEO** | Olares 核心叙事词，FAQ 段抢引用位 |
| home assistant esphome no cloud | 0 | — | — | — | **GEO** | 语义精准组合，适合 FAQ 前瞻段 |

---

## 核心洞见

1. **品牌护城河**：esphome.io 在品牌词（esphome / esp home / esp io）上 #1 垄断，合计流量 >8,000/月，无法正面竞争。但 **esphome 的 SEO 覆盖仅限组件文档和品牌词**——非品牌类传感器场景词（"home assistant door sensor" KD 12、"zigbee motion sensor" KD 9、"temperature sensor home assistant" KD 16）esphome.io 几乎**没有专题内容**，是最大可切入缺口。

2. **可复制的打法**：esphome.io 靠组件文档页（`/components/sensor/ld2420/`）意外排在 `hlk-ld2420` 等型号词上，说明**型号+用途组合页（`xxx esphome`、`xxx home assistant`）是低 KD 的自然流量来源**。Olares 可复制这个打法：为每类传感器（LD2410 mmWave、BME280 温湿度、SNZB 系列门磁水浸）写 "[传感器型号/品牌] + HA on Olares 部署教程"，用设备文档页吃型号词长尾。

3. **对 Olares 最关键的 3 个词**：
   - `zigbee motion sensor`（480/mo, KD 9）——KD 最低的高量商业词，Z2M+HA on Olares 完整本地方案，无需 Aqara/SmartThings Hub；
   - `home assistant door sensor`（480/mo, KD 12）——KD 极低、CPC $1.29 高商业价值，DIY $5 门磁 + Olares 教程直接切入；
   - `everything presence one`（720/mo, KD 16）——全报告流量最大的低 KD 词，ESPHome 成品 mmWave 传感器，HA on Olares 开箱管理。

4. **最大攻击面**：**商业 Zigbee 方案（Aqara / SONOFF / SmartThings）要订阅 + 云依赖**。词组如 `home assistant door sensor`（KD 12）、`zigbee water sensor`（KD 12）、`zigbee temperature sensor`（KD 12）的买家意图本质是"找不依赖厂商 Hub 的方案"。Olares 的叙事（ESPHome/Z2M + HA on Olares，一次性硬件 $5-30，数据永不出家门）直接命中这个痛点，且比商业方案便宜 90%+。

5. **隐藏低 KD 金矿**：
   - `apollo msr-2`：KD **5**，月量 90，ESPHome mmWave 设备评测，几乎无竞争；
   - `zigbee2mqtt vs zha`：KD **7**，月量 110，对比文基本无对手；
   - `home assistant motion sensor`、`esp32 temperature sensor`：KD 均为 **9**，月量 200+；
   - `zigbee water sensor`：KD **12**，月量 210，"漏水报警 + 零订阅"叙事强；
   - `door and window sensors`：KD **19** 但 CPC $5.28，高商业价值词。

6. **GEO 前瞻布局**：`local home automation`（CPC $3.43 高意图，量 20）、`smart home without cloud`（量 20）、`home assistant esphome no cloud`（近零量）——语义精准，极适合在"ESPHome + HA on Olares"文章的 FAQ 段落抢 AI Overview / Perplexity 引用位，契合 Olares "Own your AI, own your sensors" 叙事。ESPHome 2026.5.0 原生 Zigbee 支持（ESP32-H2/C6）是时间窗口词——现在写 `esphome zigbee`（KD 21，140 月量）内容可吃早期流量红利。

7. **与既有分析的关联**：DIY 传感器品类补充了 IoT 方向中"具体传感器型号词 + HA 集成词"的缺口，`home assistant door sensor`、`zigbee motion sensor`、`esphome presence sensor` 等词与已有 HA/自托管词集群互补，可共用"local home automation stack"主题文章簇（跨报告聚簇）。特别注意：iot.md 中 sensors-hubs 已记录 Apollo / Everything Presence One 品牌词（`everything presence one` 720/mo KD 16），应纳入同一内容簇统一规划。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
