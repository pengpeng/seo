# Shelly SEO 竞品分析报告

> 域名：shelly.cloud | SEMrush US | 2026-07-06
> Shelly Group SE（XETRA: SLYG）——本地优先智能家居硬件品牌，以原生 MQTT/REST API、无云可运行、实时能源计量为核心差异化；SDAX 成分股（2026-04 入选），FY2025 营收 €149.7M。

---

## 项目理解（前置）

Shelly（隶属 Allterco Robotics）是保加利亚 IoT 硬件公司，2010 年创立，总部索非亚；旗下 Shelly 品牌专注于**本地优先的智能开关/插座/能源计量设备**。产品出厂即可完全本地运行（无需注册云账号），原生支持 MQTT 和 REST/HTTP API，是 Home Assistant 社区公认的"金标准"可编程智能插座。FY2025 营收 €149.7M（+40.3% YoY），累计 23M+ 设备销量，并于 2026 年 4 月入选法兰克福交易所 SDAX 指数。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 本地优先智能家居硬件（插座/开关/能源计量），原生 MQTT/REST，无云可跑 |
| 开源 / 许可证 | 硬件闭源；设备端脚本（Mongoose JS）开放；API 文档公开 |
| 主仓库 | 无官方开源主仓；API 文档：shelly-api-docs.shelly.cloud |
| 核心功能 | ① 本地 HTTP/REST/MQTT 控制（出厂可关云）② 设备端 JavaScript 脚本 ③ 实时能源计量（电压/电流/功率/电量）④ Matter/Zigbee/Z-Wave 等多协议（Gen4+）⑤ 全兼容 HA/Google/Alexa/MQTT |
| 商业模式 / 定价 | 纯硬件销售；插座类 $15–35，能源计量类 $30–80，Pro 系列 $50+；App 基础功能免费，Premium €2.99/月 |
| 差异化 / 价值主张 | 唯一兼顾"消费级价格 + 专业级本地 API + 能源计量"的上市品牌；Gen4 同时支持 Matter + MQTT 双栈 |
| 主要竞品（初判）| Sonoff（Itead）、TP-Link Kasa、Meross、Eve（Thread/Apple HomeKit）、Tasmota 兼容设备 |
| Olares Market | 未直接上架（但 Home Assistant 已在 Olares Market，Shelly 设备作为 HA 感知层接入） |
| 来源 | [shelly.cloud](https://shelly.cloud)、[corporate.shelly.com](https://corporate.shelly.com/en)、[shelly-api-docs.shelly.cloud](https://shelly-api-docs.shelly.cloud)、Yahoo Finance SLYG.F |

---

## 流量基线（Phase 1）

### 概览

Shelly 欧洲电商主站为 shelly.com（或 shelly.cloud 同内容），美国用户主要通过亚马逊购买。shelly.cloud 的美国 SEO 流量以产品知识库为主，品类意向词几乎未覆盖——这恰好是内容切入的大机会。

| 指标 | 数据 |
|------|------|
| 域名 | shelly.cloud |
| SEMrush US 自然关键词数 | ~2,280（各子域合计） |
| 月自然流量（US 估算）| ~3,540 |
| 主要流量来源 | kb.shelly.cloud（产品手册 75%） |
| 排名 1–3 位 | 主要为品牌型号 KB 词 |
| 付费词 | 美国几乎无 Google Ads 投放 |

### 子域名流量分布

| 子域名 | 关键词数 | 月流量（US）| 占比 |
|--------|---------|------------|------|
| kb.shelly.cloud | 1,394 | 2,655 | 75% |
| support.shelly.cloud | 249 | 317 | 9% |
| control.shelly.cloud | 33 | 311 | 9% |
| community.shelly.cloud | 431 | 163 | 5% |
| my.shelly.cloud | 5 | 43 | 1% |
| shelly-api-docs.shelly.cloud | 146 | 35 | 1% |

> **洞察**：75% 的 US 流量来自 KB（产品手册、配线图、固件说明）——产品文档 SEO 打法。API 文档子域（shelly-api-docs）只有 35 流量，意味着开发者/集成词极度欠挖。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| plus smoke | 1 | 5,400 | 27 | $0 | 1,339 | 信息 | kb.shelly.cloud/shelly-plus-smoke |
| shelly 2pm gen3 calibration fails | 1 | 1,600 | 11 | $0 | 211 | 信息 | support.shelly.cloud/... |
| shelly | 4 | 33,100 | 61 | $0.29 | 165 | 品牌/导航 | control.shelly.cloud |
| shelly plus 1 | 1 | 390 | 17 | $0.28 | 96 | 信息/商业 | kb.shelly.cloud/shelly-plus-1 |
| shelly dimmer 2 | 1 | 390 | 21 | $0.41 | 96 | 信息/商业 | kb.shelly.cloud/shelly-dimmer-2 |
| shelly cloud | 1 | 320 | 52 | $0.06 | 79 | 导航 | control.shelly.cloud |
| shelly rgbw2 | 1 | 210 | 10 | $0.27 | 52 | 信息/商业 | kb.shelly.cloud/shelly-rgbw2 |
| shelly dimmer | 3 | 390 | 17 | $0.27 | 31 | 信息 | kb.shelly.cloud/shelly-dimmer-gen3 |
| shelly 3em | 2 | 210 | 12 | $0.37 | 27 | 信息/商业 | kb.shelly.cloud/shelly-3em |
| shelly plus add-on | 2 | 210 | 11 | $0.41 | 27 | 信息/商业 | kb.shelly.cloud/shelly-plus-add-on |
| shelly login | 1 | 110 | 27 | $0 | 27 | 导航 | control.shelly.cloud |
| shelly pro 1 | 2 | 140 | 7 | $0.32 | 18 | 信息/商业 | kb.shelly.cloud/shelly-pro-1 |
| shelly em | 2 | 480 | 20 | $0.27 | 12 | 信息/商业 | kb.shelly.cloud/shelly-em |
| shelly plug s | 2 | 140 | 25 | $0.42 | 18 | 信息/商业 | kb.shelly.cloud/shelly-plug-s |
| shelly scripting | 1 | 40 | 7 | $0 | 9 | 信息 | shelly-api-docs.shelly.cloud/... |

> **洞察**：Shelly 对自身品牌型号词排名强劲（多处 #1），但品类意向词（"smart plug energy monitoring"、"home assistant smart plug"）几乎无覆盖。最高流量关键词 "plus smoke"（烟雾探测器）证明其文档 SEO 覆盖宽泛，但这不是 Olares 角度的核心机会。

### 付费词（Google Ads）

Shelly.cloud 在美国几乎无 Google Ads 付费投放，符合其"欧洲品牌、美国靠社区口碑/亚马逊"的分销策略。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kasa smart plug | 8,100 | 71 | $0.31 | 信息/商业 | TP-Link Kasa，美国最大竞品，高 KD 难攻 |
| sonoff s31 | 590 | 16 | $0.45 | 信息/商业 | ⭐ Sonoff 能源计量插座，主要直接竞品 |
| shelly vs sonoff | 20 | 0 | — | 信息 | ⭐ 近零 KD；全球量约 60–100（3–5x 美国） |
| sonoff vs shelly | 20 | 0 | — | 信息 | ⭐ 同义词，可合并写一篇对比文 |
| sonoff alternative | 20 | 0 | — | 信息 | ⭐ Shelly 是 Sonoff 最自然的本地升级方向 |
| shelly tasmota | 20 | 0 | — | 信息 | ⭐ Tasmota 刷机用户转 Shelly 原生 API 的迁移信号 |
| shelly alternative | 0 | 0 | — | — | 目前无量，GEO 前哨 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| smart plug with energy monitoring | 590 | 24 | $0.34 | 商业 | ⭐ Shelly 最强品类词，KD 仅 24 |
| matter smart plug | 480 | 15 | $0.36 | 信息/商业 | ⭐ Gen4 Matter 天然切入；KD 15 |
| home assistant smart plug | 210 | 23 | $0.42 | 商业 | ⭐ 精准集成意图 |
| energy monitoring smart plug | 260 | 28 | $0.44 | 信息/商业 | ⭐ |
| smart plug energy monitor | 210 | 24 | $0.34 | 信息/商业 | ⭐ |
| smart plugs with energy monitoring | 210 | 23 | $0.44 | 商业 | ⭐ |
| zigbee smart plug | 390 | 7 | $0.40 | 商业 | ⭐⭐⭐ KD 极低！Shelly BLU Gateway 可切入 |
| smart energy monitor home | 720 | 27 | $0.65 | 商业 | ⭐ 家庭能源计量大词 |
| home assistant energy monitor | 210 | 25 | $0.57 | 信息 | ⭐ |
| home assistant energy monitoring | 70 | 26 | $0.57 | 信息 | ⭐ 精准，CPC 高（$0.57 说明有商业价值） |
| home assistant energy dashboard | 140 | 20 | — | 信息 | ⭐ Shelly EM 数据的最终展示层 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| shelly em | 590 | 20 | $0.27 | 信息/商业 | ⭐ 能源计量旗舰型号，KD 仅 20 |
| shelly plug | 390 | 29 | $0.37 | 信息/商业 | ⭐ |
| shelly pro 3em | 390 | 17 | $0.29 | 信息/商业 | ⭐ 三相能源计量，KD 17 |
| shelly smart plug | 260 | 16 | $0.34 | 信息 | ⭐⭐ KD 极低 16，可快速排名 |
| shelly 1pm | 260 | 40 | $0.23 | 信息 | 功率计量开关型号，KD 偏高 |
| shelly home automation | 260 | 40 | $0.42 | 商业 | 品牌场景词，KD 偏高 |
| shelly plus 2pm | 210 | 24 | $0.28 | 信息/商业 | ⭐ |
| shelly gen4 | 140 | 31 | $0.24 | 信息/商业 | 新品，Matter + MQTT 双栈 |
| shelly home assistant | 140 | 26 | $0.15 | 信息 | ⭐ 核心集成词 |
| shelly plug s | 140 | 25 | $0.42 | 信息/商业 | ⭐ 明星插座型号 |
| shelly zigbee | 110 | 13 | $0.20 | 信息 | ⭐ BLU 网关 Zigbee 词 |
| shelly power monitoring | 40 | 26 | $0.18 | 信息/商业 | ⭐ |
| shelly scripting | 40 | 6 | — | 信息 | ⭐⭐⭐ KD 极低 6，开发者词 |
| shelly 2pm gen3 | 40 | 13 | $0.30 | 信息/商业 | ⭐ |
| shelly local api | 20 | 0 | — | 信息 | ⭐ 技术词，GEO 前哨 |
| shelly mqtt | 20 | 0 | — | 信息 | ⭐ |
| shelly energy monitoring | 10 | 0 | — | 信息 | ⭐ GEO 前哨 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home assistant automation | 390 | 40 | $2.35 | 信息 | HA 使用核心词，CPC 高 |
| home assistant mqtt | 390 | 29 | — | 信息 | ⭐ Shelly MQTT 最稳定集成路径 |
| home assistant installation | 480 | 42 | $4.29 | 信息/导航 | HA 入门高意向，$4.29 CPC |
| home assistant energy dashboard | 140 | 20 | — | 信息 | ⭐ Shelly EM 数据的展示终端 |
| home assistant open source | 210 | 77 | — | 导航 | 品牌词，KD 极高 |
| self hosted home automation | 20 | 0 | — | 信息 | ⭐ 精准意图，GEO 前哨 |
| home automation local control | 20 | 0 | — | 信息 | ⭐ |
| local smart home | 20 | 0 | — | 信息 | ⭐ |

---

## Olares 关联词（Phase 3）

**核心逻辑：Shelly 是 Olares 感知层的最佳硬件搭档——原生本地 MQTT/REST、无需云依赖、内置能源计量，配合 Olares Market 上的 Home Assistant，构成"硬件接入 → 本地自动化 → 能源看板 → Agent 感知"完整闭环。Olares 提供 HA 运行环境，Shelly 提供最佳设备侧 API，组合叙事天然契合"拥有你的 AI，也拥有你的家"。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| shelly home assistant | 140 | 26 | $0.15 | ⭐⭐⭐ Olares Market 已有 HA，一键部署 + Shelly 设备自动发现；可写 "Install Home Assistant + Shelly on Olares" 教程页 |
| home assistant smart plug | 210 | 23 | $0.42 | ⭐⭐⭐ Olares HA + Shelly Plug S = 本地能源自动化完整方案；Olares 提供持久存储和 Agent 可读的电量历史 |
| smart plug with energy monitoring | 590 | 24 | $0.34 | ⭐⭐ 品类大词；叙事：Shelly 插座 + Olares 上的 HA Energy Dashboard = 本地能源数据自主权 |
| home assistant energy monitoring | 70 | 26 | $0.57 | ⭐⭐⭐ Shelly EM/Pro 3EM + HA Energy Dashboard on Olares，完全本地，数据不出设备 |
| home assistant energy dashboard | 140 | 20 | — | ⭐⭐⭐ 最终展示层；Shelly 实时功率 → HA Energy → Olares 上的持久化看板 |
| home assistant mqtt | 390 | 29 | — | ⭐⭐ Olares 可自托管 MQTT broker（Mosquitto），Shelly + MQTT + HA = 全本地无云链路 |
| shelly mqtt | 20 | 0 | — | ⭐⭐ 开发者词；Olares MQTT broker + Shelly 三件套教程 |
| shelly local api | 20 | 0 | — | ⭐⭐ GEO：Olares Agent 可通过 Shelly Local REST API 读取电量数据，本地推理分析用电异常 |
| self hosted home automation | 20 | 0 | — | ⭐⭐⭐ GEO：Olares 是自托管家居中枢的最佳运行环境，Shelly 是感知层首选硬件 |
| shelly scripting | 40 | 6 | — | ⭐ Shelly 设备端脚本 + Olares Agent = 边缘 + 云端推理协同（设备端预过滤，Olares 端做 LLM 推理） |
| zigbee smart plug | 390 | 7 | $0.40 | ⭐⭐ KD 仅 7；Shelly BLU Gateway + Zigbee2MQTT on HA on Olares = 全本地 Zigbee 插座方案 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| smart plug with energy monitoring | 590 | 24 | $0.34 | 商业 | 主词候选 | ⭐ 量大 KD 低；Shelly Plug S/1PM 是最佳答案，Olares HA 做统一能源看板 |
| shelly em | 590 | 20 | $0.27 | 信息/商业 | 主词候选 | ⭐ 品牌+型号词，KD 仅 20；Shelly EM + HA on Olares = 本地能源仪表盘教程最佳切入 |
| zigbee smart plug | 390 | 7 | $0.40 | 商业 | 主词候选 | ⭐⭐⭐ KD 极低 7！Shelly BLU Gateway + Zigbee2MQTT + HA on Olares，全本地 Zigbee 方案 |
| shelly plug | 390 | 29 | $0.37 | 信息/商业 | 主词候选 | ⭐ 有量有商业意图；Olares 视角 = Shelly Plug 本地控制最佳搭档 |
| shelly pro 3em | 390 | 17 | $0.29 | 信息/商业 | 主词候选 | ⭐ 三相能源计量型号词，KD 17；目标用户 = 电力监控 + HA 深度用户 |
| matter smart plug | 480 | 15 | $0.36 | 信息/商业 | 主词候选 | ⭐ 2025–2026 热词；Shelly Gen4 = 唯一兼顾 Matter + MQTT 双栈的大众品牌 |
| home assistant smart plug | 210 | 23 | $0.42 | 商业 | 主词候选 | ⭐ Shelly 是 HA 社区首推插座；Olares 跑 HA + Shelly 部署教程，双品牌合力 |
| shelly smart plug | 260 | 16 | $0.34 | 信息 | 主词候选 | ⭐⭐ KD 极低 16，可快速排名；Olares + HA 教程角度切入 |
| energy monitoring smart plug | 260 | 28 | $0.44 | 信息/商业 | 主词候选 | ⭐ 品类词入口；Shelly + Olares 能源管理叙事 |
| home assistant energy monitoring | 70 | 26 | $0.57 | 信息 | 主词候选 | ⭐ 量小但意图精准 + CPC 高；Shelly EM 数据 + HA Energy Dashboard on Olares 是最完整的本地方案 |
| shelly home assistant | 140 | 26 | $0.15 | 信息 | 主词候选 | ⭐ 精准集成词；"Shelly + Home Assistant on Olares" 是天然教程落地页 |
| home assistant mqtt | 390 | 29 | — | 信息 | 次级 | Shelly MQTT 是 HA 集成最稳定路径；并入 Shelly+HA 教程覆盖 |
| home assistant energy dashboard | 140 | 20 | — | 信息 | 次级 | ⭐ KD 20；Shelly 功率 → HA Energy；可并入能源监控主文 |
| shelly scripting | 40 | 6 | — | 信息 | 次级 | ⭐⭐⭐ KD 极低 6；开发者词；Olares Agent 调 Shelly 脚本 API 实现本地智能 |
| shelly vs sonoff | 20 | 0 | — | 信息 | 次级 | ⭐ 近零 KD；对比文切入，Olares 两者均支持但 Shelly 无需刷机 |
| shelly local api | 20 | 0 | — | 信息 | GEO | 近零量，语义精准；FAQ 植入：Shelly Local REST API + Olares Agent 读取电量 |
| shelly energy monitoring | 10 | 0 | — | 信息 | GEO | 近零量；FAQ 段植入即可 |
| self hosted home automation | 20 | 0 | — | 信息 | GEO | ⭐⭐⭐ 意图极精准；Olares = 自托管家居中枢首选，抢 AI Overview 引用位 |
| smart plug no cloud | ~0 | — | — | 信息 | GEO | 无量但高价值；Shelly + Olares 叙事核心词，抢引用位 |
| shelly mqtt | 20 | 0 | — | 信息 | GEO | 可在 HA + Shelly + MQTT broker on Olares 教程中覆盖 |

---

## 核心洞见

1. **品牌护城河**：品牌词 "shelly" 搜索量 33,100/月，但有严重"人名污染"（Shelly 是常见英文女名，话题类搜索占多数）。品牌型号词（Shelly EM、Shelly Pro 3EM 等）低 KD 且排名好攻；而品类意向词（"smart plug with energy monitoring"、"home assistant smart plug"）Shelly 在美国几乎没有内容覆盖——这是最大内容空白，Olares 可占据。

2. **可复制的打法**：Shelly 靠 KB 文档（产品手册、配线图、型号说明）获取了 75% 的 US 流量——产品文档 SEO 打法。可复制到 Olares 侧：为每个 Shelly 型号写"如何在 Olares HA 上配置 Shelly XXX"的结构化教程文章集（程序化落地页模式），用 HA + Shelly 组合词拦截 Shelly 官网未覆盖的意向流量。

3. **对 Olares 最关键的词**：
   - `shelly home assistant`（140/mo, KD 26）：最直接的教程词，指向"在 Olares 上部署 HA + 接入 Shelly 设备"
   - `home assistant smart plug`（210/mo, KD 23）：品类意向词，推荐 Shelly 为 HA 最佳搭档
   - `smart plug with energy monitoring`（590/mo, KD 24）：最大商业意图词，Shelly + Olares 是完整本地答案

4. **最大攻击面**：云依赖痛点。Belkin Wemo 云关停（2026-01-31）是最真实的警示案例——`wemo alternative`、`smart plug without cloud` 等词群因此产生迁移需求。内容打法：Wemo 弃用 → 迁移到 Shelly + HA on Olares，叙事核心是"本地优先，数据不依赖他人续费"。

5. **隐藏低 KD 金矿**：
   - `zigbee smart plug`（390/mo, KD **7**）：最低 KD + 商业意图强；Shelly BLU Gateway 桥接 Zigbee，Olares + Zigbee2MQTT + HA 全本地
   - `shelly scripting`（40/mo, KD **6**）：开发者词，极低 KD，Shelly 设备端 JS API 文档稀缺，可写 Olares Agent + Shelly 脚本协同教程
   - `shelly pro 1`（140/mo, KD **7**）：型号文档词，竞争几乎为零

6. **GEO 前瞻布局**：
   - `smart plug no cloud` / `shelly local rest api` / `self hosted home automation`：AI Overview/Perplexity 已开始回答此类 DIY 问题，在这些词的 FAQ 段植入"Olares + HA + Shelly = 完整本地链路"可抢引用位
   - Shelly Gen4 + Matter + HA 联动是 2025–2026 热点话题，可早布局 `matter smart plug home assistant`（量小但快速上升中）

7. **与既有分析的关联**：iot.md 已标注 Shelly 为"本地控制细分冠军"，核心机会词 `smart plug without cloud`、`smart plug home assistant`、`shelly`、`shelly vs sonoff` 已预判正确。本报告补充了三个有量低 KD 词：`smart plug with energy monitoring`（590/mo, KD 24）、`matter smart plug`（480/mo, KD 15）、`zigbee smart plug`（390/mo, KD **7**）；并揭示 Shelly 美国 SEO 流量极低（~3,540/mo）、品类意向词覆盖空白大——适合内容侧主动攻入而非跟随 Shelly 官网打法。

---

*数据来源：SEMrush US 数据库（resource_organic、domain_organic_subdomains、phrase_these、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
