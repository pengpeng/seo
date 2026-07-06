# Z-Wave / Zooz SEO 竞品分析报告

> 域名：getzooz.com | SEMrush US | 2026-07-06
> Z-Wave 800 + Long Range 智能家居协议生态的核心设备品牌；代表 Silicon Labs 开放标准在本地控制高端市场的最强生态入口。

---

## 项目理解（前置）

Z-Wave 是由 Silicon Labs 授权、Z-Wave Alliance 维护的 Sub-GHz（908 MHz，美国）无线协议，专为智能家居设计：低延迟、高可靠、不与 Wi-Fi / Zigbee 争频段。Z-Wave 800（ZG23 芯片）是当前最新世代，支持 Z-Wave Long Range（ZWLR）——星形拓扑直连、无需中继、覆盖最远 1.5 英里、单网络最多 4000 设备。截至 2026 年 1 月 CES，ZWLR 已有 125 款认证设备，覆盖 30+ 品类，80% 在途认证产品均含 ZWLR。

Zooz（getzooz.com，总部 Flanders, NJ）是 ZWLR 生态中产品线最全的消费品牌：灯光开关/调光器、插座、传感器、中继器、USB 控制棒（ZST39 800LR）与 Z-Box Hub，均全量 800 LR 阵容，且兼容 Home Assistant + Z-Wave JS——这是与 Olares 场景最直接的交汇点。

**Olares 平替角色**：Z-Wave JS UI（开源，MIT 许可）+ Zooz ZST39 800LR USB 棒 + Home Assistant on Olares，构成完整本地 Z-Wave 控制栈——数据零出云，在 Olares Market 一键部署 HA 后再挂 USB 棒即可。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Z-Wave 800 / Long Range 生态设备品牌 + 开放协议栈（Silicon Labs 授权标准） |
| 开源 / 许可证 | **Z-Wave JS**：开源 MIT；**Z-Wave 协议本身**：闭源，硅基授权；**Zooz 硬件**：商业闭源 |
| 主仓库 | [zwave-js/zwave-js-ui](https://github.com/zwave-js/zwave-js-ui)（★ ~4k），[zwave-js/node-zwave-js](https://github.com/zwave-js/node-zwave-js)（★ ~3k） |
| 核心功能 | 本地 Sub-GHz 网状/星形控制；800 系列 50% 更长电池续航；ZWLR 超远距直连；S2 安全加密；SmartStart QR 快速配对；兼容 Home Assistant / Hubitat / HomeSeer |
| 商业模式 / 定价 | Zooz 硬件零售（$10–$60 / 件）；Z-Wave JS 免费开源；ZST39 USB 棒约 $40；Z-Box Hub 约 $100 |
| 差异化 / 价值主张 | 零云依赖（本地控制）；跨品牌兼容（4500+ Z-Wave 认证设备）；ZWLR 打破「需要 mesh 中继」限制；5 年延保（Zooz 注册设备） |
| 主要竞品（初判）| Aeotec（USB 棒/传感器）、Jasco/GE（灯控）、Shelly Wave（继电器）、Schlage/Yale（门锁）、SmartThings Hub（平台层）、Zigbee/Thread/Matter（协议竞争） |
| Olares Market | ⬜ 未上架（Z-Wave JS UI 未独立收录；Home Assistant 已在 Market，USB 棒透传需手动配置） |
| 来源 | [getzooz.com](https://www.getzooz.com/)、[silabs.com/wireless/z-wave/introduction-to-z-wave-800-series](https://www.silabs.com/wireless/z-wave/introduction-to-z-wave-800-series)、[z-wavealliance.org CES 2026 新闻](https://z-wavealliance.org/news_p/z-wave-alliance-highlights-newly-certified-z-wave-long-range-devices/)、[home-assistant.io/integrations/zwave_js](https://www.home-assistant.io/integrations/zwave_js/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | getzooz.com |
| SEMrush Rank | 384,452 |
| 自然关键词数 | 2,698 |
| 月自然流量（US）| 4,012 |
| 自然流量估值 | $1,002 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1–3 位 | 96 词 |
| 排名 4–10 位 | 257 词 |
| 排名 11–20 位 | 275 词 |

> **洞察**：Zooz 绝不买广告，完全靠自然搜索。流量极度集中在品牌词（「zooz zen72 firmware」单词贡献 ~18%），非品牌词空间大但未被挖掘。$1,002 流量估值相对体量很低，说明 CPC 溢价词（锁/恒温器等）未被开垦。

### 子域名流量分布

| 子域名 | 关键词数 | 月流量 | 占比 |
|--------|---------|------|------|
| www.getzooz.com（产品官网） | 1,301 | 2,154 | **53.7%** |
| www.support.getzooz.com（知识库） | 1,397 | 1,858 | **46.3%** |

> **洞察**：支持知识库贡献了接近一半流量——用户在搜 firmware changelog / config parameter 等长尾技术词。Z-Wave JS 社区内容同样是长尾引流利器。

### 官网 TOP 自然关键词（按流量排序，前 30 词）

| 关键词 | 排名 | 月量 | KD | CPC | 月流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| zooz zen72 firmware update | 1 | 1,900 | 10 | $0 | 471 | 信息 | support.getzooz.com/kb/... |
| zooz | 2 | 12,100 | 26 | $0.08 | 314 | 导航 | getzooz.com/ |
| zooz zen72 firmware update（第二 URL）| 2 | 1,900 | 10 | $0 | 250 | 信息 | support.getzooz.com/kb/... |
| zooz 800 series z-wave long range usb stick | 3 | 1,600 | 24 | $0 | 131 | 信息+商业 | getzooz.com/zooz-zst39-... |
| zooz dimmer | 1 | 110 | 26 | $0.68 | 88 | 商业 | getzooz.com/zooz-zen77-... |
| zooz switch | 2 | 480 | 12 | $0.70 | 63 | 商业 | getzooz.com/switches-and-plugs/ |
| zooz switches | 2 | 390 | 26 | $0.57 | 51 | 商业 | getzooz.com/switches-and-plugs/ |
| zooz smart switch | 2 | 320 | 20 | $0.49 | 42 | 商业 | getzooz.com/switches-and-plugs/ |
| zooz 800 series z-wave long range heavy duty wall switch | 2 | 320 | 12 | $0 | 42 | 信息+商业 | getzooz.com/ |
| zooz zwave 800 | 2 | 260 | 13 | $0.64 | 34 | 信息+商业 | getzooz.com/zooz-zst39-... |
| zooz 800 series z-wave long range dimmer & scene controller | 3 | 390 | 7 | $0 | 31 | 信息 | getzooz.com/zen35-... |
| 3 button zwave scene control switch | 3 | 390 | 1 | $0 | 31 | 商业 | getzooz.com/zooz-zen32-... |
| zooz 800 series z-wave long range usb stick（FAQ）| 5 | 1,600 | 24 | $0 | 38 | 信息 | support.getzooz.com/kb/... |
| zooz 800 series config parameters | 1 | 210 | 10 | $0 | 27 | 信息 | support.getzooz.com/kb/... |
| zooz zen55 | 2 | 210 | 11 | $0.78 | 27 | 信息+商业 | getzooz.com/zooz-zen55-... |
| zst39 lr | 1 | 110 | 15 | $0 | 27 | 信息+商业 | getzooz.com/zooz-zst39-... |
| zooz zen18 | 1 | 110 | 9 | $0 | 27 | 信息 | getzooz.com/zooz-zse18-... |
| zooz zen15 | 1 | 110 | 7 | $0.45 | 27 | 信息+商业 | getzooz.com/zooz-zen15-... |
| zooz z wave | 2 | 210 | 10 | $0.66 | 27 | 商业 | getzooz.com/ |
| zac36 | 2 | 210 | 9 | $0 | 27 | 信息 | getzooz.com/zooz-zac36-... |
| zooz titan | 2 | 210 | 2 | $0.97 | 27 | 商业 | getzooz.com/zooz-zac36-... |
| z-box hub | 4 | 320 | 13 | $1.55 | 20 | 信息+商业 | getzooz.com/hubs-and-network/ |
| zooz zwave | 2 | 140 | 17 | $0.69 | 18 | 商业 | getzooz.com/ |
| zooz zen34 | 2 | 140 | 10 | $0.49 | 18 | 信息+商业 | getzooz.com/zooz-zen34-... |
| zooz zen32 | 2 | 140 | 14 | $0.49 | 18 | 信息+商业 | getzooz.com/zooz-zen32-... |
| zooz relay | 2 | 110 | 2 | $0.61 | 14 | 商业 | getzooz.com/smart-relays/ |
| zooz scene controller | 2 | 110 | 15 | $0.55 | 14 | 信息+商业 | getzooz.com/zooz-zen32-... |
| zooz zen51 | 1 | 30 | 12 | $0.72 | 24 | 信息+商业 | getzooz.com/zooz-zen51-... |
| zst39 lr firmware | 1 | 70 | 5 | $0 | 17 | 信息 | support.getzooz.com/kb/... |
| zooz 800 | 3 | 210 | 18 | $0.58 | 17 | 信息+商业 | getzooz.com/zooz-zst39-... |

> **打法洞察**：Zooz 靠精确的产品型号词（zen72 / zen35 / zst39 / zac36）霸占长尾，知识库（firmware changelog / config parameter）是另一大流量柱。付费广告完全缺位。

### 付费词（Google Ads）

**无付费投放。** Zooz 为 100% 自然流量驱动品牌，无任何广告词。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且月量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| z-wave vs zigbee | 590 | **21** | $0.04 | 信息 | ⭐ 协议比较主战场；KD 低、稳定需求 |
| z-wave vs matter | — | **13** | $0 | 信息 | ⭐⭐ 热点协议对比，Matter 普及带动流量 |
| z-wave vs zigbee vs matter | — | **0** | $0 | 信息 | ⭐⭐⭐ 三协议三选一，GEO 前哨 |
| best smart home hubs | 33,100 | 高 | $0.27 | 商业 | 竞争激烈，大词 |
| smartthings z wave hub | 260 | 中 | $0.46 | 商业 | SmartThings 用户迁移需求 |
| zigbee hubs | 480 | 中 | $0.34 | 商业 | 跨协议比较 |
| best zigbee hub | 260 | 高 | $0.39 | 商业 | 量可观，KD 高 |
| best z wave hub | 260 | **23** | $0.37 | 商业 | ⭐ KD 低，有 CPC，决策词 |
| aeotec z stick 7 | 70 | — | $0.51 | 商业 | Zooz 直接竞品 USB 棒关键词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| z-wave | 3,600 | 37 | $0.56 | 信息+商业 | 品类总词，竞争中等 |
| zwave | 3,600 | — | $0.56 | 信息+商业 | 拼写变体，量等同 |
| z-wave hub | 1,300 | **18** | $0.34 | 商业 | ⭐ 量大 KD 低，品类决策词 |
| smart home hub | 9,900 | 高 | $1.16 | 商业 | 广义品类，竞争极激烈 |
| home automation hub | 6,600 | 高 | $1.16 | 商业 | 广义，高 KD |
| z-wave controller | 720 | **18** | $0.41 | 信息+商业 | ⭐ KD 低、技术用户 |
| z-wave devices | 320 | — | $0.39 | 信息 | 品类调研词 |
| z-wave thermostat | 320 | **8** | $0.47 | 商业 | ⭐⭐ 极低 KD，高 CPC |
| z-wave switch | 90 | **14** | $0.55 | 商业 | ⭐ 低 KD，直接设备词 |
| z-wave motion sensor | 70 | 高 | $0.36 | 商业 | 竞争一般 |
| z-wave lock | 50 | 高 | $0.78 | 商业 | CPC 高，安全品类 |
| what is z-wave | 590 | 30 | $0.16 | 信息 | ⭐ 入门教育词 |
| z-box hub | 260 | **13** | $1.55 | 信息+商业 | ⭐⭐ KD 极低，CPC 高，Zooz 专属产品 |

### 产品 / 功能词（Zooz 品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| zooz | 12,100 | 33 | $0.08 | 导航 | 品牌主词，Zooz 自占 |
| zooz 800 series z-wave long range usb stick | 1,600 | 24 | $0 | 信息+商业 | ⭐ USB 棒主产品词，Zooz 排 3 位 |
| zooz zen72 | 70 | **11** | $0.74 | 信息+商业 | ⭐⭐ 单型号，KD 极低 |
| zooz dimmer | 110 | 26 | $0.68 | 商业 | ⭐ 调光器产品词 |
| zooz switch | 480 | 12 | $0.70 | 商业 | ⭐⭐ KD 极低，CPC 高 |
| zooz smart switch | 320 | 20 | $0.49 | 商业 | ⭐ 低 KD |
| z-box hub | 260 | **13** | $1.55 | 信息+商业 | ⭐⭐ Zooz Hub 产品词 |
| zooz smart plug | 50 | — | $0.46 | 商业 | 产品词 |
| zooz zen34 | 140 | 10 | $0.49 | 信息+商业 | ⭐⭐ 遥控器产品词，KD 10 |
| zooz relay | 110 | **2** | $0.61 | 商业 | ⭐⭐⭐ KD=2！干接点继电器，Olares 本地自动化强场景 |
| zooz zst39 | 30 | — | $0.60 | 信息 | USB 棒型号词 |
| zooz home assistant | 20 | — | $0 | 信息 | Olares 场景词，集成教程 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| z-wave js ui | 880 | **28** | $0 | 信息 | ⭐⭐ 开源 Z-Wave 服务端，核心 Olares 入口词 |
| zwave js | 210 | 36 | $0 | 信息 | Z-Wave JS 驱动核心词 |
| z-wave js | 260 | 35 | $0 | 信息 | 同上变体 |
| home assistant z wave | 210–480 | — | $0.49 | 信息 | HA Z-Wave 集成词 |
| zwave home assistant | 170 | 58 | $0.49 | 信息 | 竞争偏高，但相关 |
| home assistant z-wave | 70 | 57 | $0.73 | 信息 | 集成官方词 |
| home assistant z wave hub | 70 | **18** | $0.56 | 信息 | ⭐ 低 KD，Olares 直接角度 |
| self-hosted home automation | 20 | — | $0 | 信息 | ⭐ GEO 前哨，近零量但高语义精度 |
| smart home local control | 20 | — | $0 | 信息 | ⭐ 本地控制信号词 |
| z-wave home automation | 10 | — | $0.84 | 信息+商业 | 高 CPC，小众但精准 |

---

## Olares 关联词（Phase 3）

**核心叙事切入点：Z-Wave 本地控制栈（Z-Wave JS UI + 800LR USB 棒）运行在 Olares 上，彻底消灭云依赖——你的 Z-Wave 网络数据永远不离开你自己的设备。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|------|
| z-wave js ui | 880 | 28 | $0 | Olares Market → HA → Z-Wave JS UI 是标准安装路径，「在 Olares 一键部署 Z-Wave JS UI」可做独立教程 | ⭐⭐⭐ |
| z-wave hub | 1,300 | 18 | $0.34 | 「Home Assistant on Olares + USB 棒 = 本地 Z-Wave Hub」，无订阅费、数据不出家门 | ⭐⭐⭐ |
| best z wave hub | 260 | 23 | $0.37 | 对比文可列：Hubitat / SmartThings / Zooz Z-Box / HA-on-Olares；Olares 唯一零云 SaaS 费方案 | ⭐⭐⭐ |
| z-wave vs zigbee | 590 | 21 | $0.04 | 对比文尾部可点出 HA on Olares 同时支持 Z-Wave + Zigbee（两棒并插），比单协议 hub 更灵活 | ⭐⭐ |
| home assistant z wave hub | 70 | 18 | $0.56 | 直接角度：Olares 是跑 HA 的最佳本地 OS，Z-Wave 配置开箱即用 | ⭐⭐⭐ |
| z-box hub | 260 | 13 | $1.55 | Zooz Z-Box vs HA on Olares 对比：Z-Box = 封闭硬件；Olares = 开放平台、可随时升级 GPU | ⭐⭐ |
| zooz zen72 | 70 | 11 | $0.74 | 「Zooz ZEN72 + Home Assistant on Olares 配置指南」——设备型号教程，流量精准 | ⭐⭐ |
| zooz relay | 110 | 2 | $0.61 | KD=2 极稀少，「Zooz ZEN51 干接点继电器 + HA on Olares 本地控制老设备」教程机会 | ⭐⭐⭐ |
| zooz home assistant | 20 | — | $0 | 小词但精准：整合教程直接覆盖 | ⭐⭐ |
| self-hosted home automation | 20 | — | $0 | GEO 词：「Olares 是最完整的自托管家居自动化平台」——抢 AI Overview 引用 | ⭐⭐⭐ |
| smart home local control | 20 | — | $0 | GEO 词：本地控制叙事，与 Olares 「数据不出门」核心主张完美吻合 | ⭐⭐⭐ |
| z-wave vs matter | — | 13 | $0 | 高时效对比词：Matter 是 Wi-Fi/Thread，Z-Wave 是 Sub-GHz；文章末尾切入 HA on Olares 同时支持两者 | ⭐⭐ |
| z-wave vs zigbee vs matter | — | 0 | $0 | GEO 金矿：KD=0，三协议选择困难文，HA on Olares 答案是「三协议全收」 | ⭐⭐⭐ |
| zwave2mqtt | 210 | — | $0 | MQTT 桥接教程词，在 Olares 上跑 MQTT broker + Z-Wave JS = 完整本地 IoT 栈 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| z-wave hub | 1,300 | 18 | $0.34 | 商业 | **主词候选** | 量大+KD 低+有 CPC；「HA on Olares = 最灵活 Z-Wave Hub」是核心切入落地页 |
| z-wave js ui | 880 | 28 | $0 | 信息 | **主词候选** | 量大+KD<30+零成本；开源自托管栈教程，Olares 一键部署场景最直接 |
| z-wave vs zigbee | 590 | 21 | $0.04 | 信息 | **主词候选** | 稳定比较需求，KD 低；结尾推 HA on Olares 同时支持两协议 |
| z-wave | 3,600 | 37 | $0.56 | 信息+商业 | 次级 | 量大但 KD 中等；作为 hub 落地页 / 协议入门文的次级词 |
| zooz | 12,100 | 33 | $0.08 | 导航 | 次级 | 品牌导航词，量大但 Zooz 自占；不值得作主词，作品牌认知段 |
| zooz 800 series z-wave long range usb stick | 1,600 | 24 | $0 | 信息+商业 | **主词候选** | USB 棒型号搜索量可观+KD<30；「ZST39 LR + HA on Olares 配置指南」独立文章 |
| what is z-wave | 590 | 30 | $0.16 | 信息 | **主词候选** | 入门教育词，软参考线上限；Z-Wave 协议综述文结尾切 Olares local stack |
| best z wave hub | 260 | 23 | $0.37 | 商业 | **主词候选** | KD 低+决策意图+有 CPC；核心对比文选题 |
| z-wave controller | 720 | 18 | $0.41 | 信息+商业 | **主词候选** | 量超线+KD 低；USB 棒推荐文 / ZST39 评测 |
| z-box hub | 260 | 13 | $1.55 | 信息+商业 | **主词候选** | KD 极低+CPC 最高（$1.55）；Z-Box vs HA-on-Olares 对比文 |
| z-wave thermostat | 320 | 8 | $0.47 | 商业 | **主词候选** | KD=8 极低！高 CPC；Z-Wave 恒温器推荐 + HA on Olares 自动化教程 |
| z-wave switch | 90 | 14 | $0.55 | 商业 | 次级 | 量偏低但 KD 低；并入 hub 文或 Zooz 设备推荐文 |
| zooz relay | 110 | **2** | $0.61 | 商业 | 次级 | KD=2 全库最低！Zooz 干接点继电器 + HA on Olares 本地老设备接入 |
| zooz dimmer | 110 | 26 | $0.68 | 商业 | 次级 | KD<30，并入 Zooz 设备推荐文 |
| z-wave vs matter | — | 13 | $0 | 信息 | 次级 | KD=13，时效性强，协议对比文侧栏/FAQ |
| z-wave vs zigbee vs matter | — | 0 | $0 | 信息 | **GEO** | KD=0 近零量；抢 AI Overview「三协议一把讲清楚」段落引用 |
| self-hosted home automation | 20 | — | $0 | 信息 | **GEO** | 近零量但语义精准；Olares 最强 GEO 钩词 |
| smart home local control | 20 | — | $0 | 信息 | **GEO** | 与 Olares「数据零出云」叙事直接对应 |
| zooz home assistant | 20 | — | $0 | 信息 | **GEO** | 精准集成场景词；教程文 FAQ 段 |
| home assistant z wave hub | 70 | 18 | $0.56 | 信息 | 次级 | KD 低；并入「HA on Olares Z-Wave 配置」文章 |

---

## 核心洞见

1. **品牌护城河（能否正面刚）**
   Zooz 品牌词（zooz, zooz zen72, zooz zst39…）由其自身知识库/官网高密度占据，KD 10–26，正面抢排名意义不大。但**技术教程词**（「zooz home assistant」、「zooz relay home assistant」）几乎无人认真做，KD 极低（甚至 2–7），是 Olares 可直接切入的空档。
   
2. **可复制的打法**
   - Zooz 自己靠「型号词 + firmware/config parameter 长尾」积累了接近一半流量（support.getzooz.com 46.3%）。同样的策略对 Olares：写「Z-Wave JS UI 配置完全指南」「ZEN72 在 Home Assistant 上的高级参数优化」，把技术教程流量引到 Olares 平台。
   - 竞品层（thesmartesthouse.com, aeotec.com）的共同特征是产品评测/对比文——这类文章可以嵌入 Olares 本地部署的 call-to-action。
   - 无人做 `best z-wave hub` 完整对比（KD 23，月量 260）——这是 Olares 的**最直接行动词**。

3. **对 Olares 最关键的 3 个词**
   - **`z-wave hub`**（1,300 量，KD 18）：「Home Assistant on Olares = 你自己的 Z-Wave Hub」核心落地页
   - **`z-wave js ui`**（880 量，KD 28）：开源 Z-Wave 控制器部署教程，Olares 一键部署 HA 后最直接下一步
   - **`best z wave hub`**（260 量，KD 23，CPC $0.37）：对比决策文，Olares 在「零月费、零云依赖」维度完胜所有付费 hub

4. **最大攻击面（痛点词）**
   - **Z-Box Hub vs HA on Olares**：Z-Box Hub 是 Zooz 自己的闭源 hub，$100 硬件 + 应用生态受限；CPC $1.55 说明用户在对比购买，Olares 提供开放平台对比文价值极高。
   - **云依赖痛点**：SmartThings / Ring Alarm / Alarm.com 都需要云订阅；Z-Wave 本地控制 + Olares = 无订阅、永久控制权——这是情绪出口。
   - **固件 OTA 控制**：Zooz ZEN72 firmware update（月量 1,900！）说明用户关心固件更新，Z-Wave JS UI on Olares 可本地 OTA，无需依赖 Zooz 服务器。

5. **隐藏低 KD 金矿**
   - **`zooz relay`** KD = **2**（月量 110，CPC $0.61）：近乎无竞争的商业词，干接点继电器 + HA 本地控制老设备场景，技术受众高转化。
   - **`z-wave thermostat`** KD = **8**（月量 320，CPC $0.47）：恒温器品类词，KD 极低，Z-Wave 恒温器推荐 + HA on Olares 自动化。
   - **`z-box hub`** KD = **13**，CPC = **$1.55**（月量 260）：KD 低但用户意图强（买 hub），竞争意味着高商业价值被低估。
   - **`3 button zwave scene control switch`** KD = **1**（月量 390）：几乎 0 竞争的产品词，Zooz ZEN32 专属场景，HA on Olares 本地场景控制教程直接锁定。

6. **GEO 前瞻布局**（近零量，抢 AI Overview / Perplexity 引用位）
   - **`z-wave vs zigbee vs matter`**（KD=0）：三协议选型困难，大量用户问 AI 助手「该用哪个协议？」，一篇结构化对比文 + FAQ 可吃 AI Overview 引用。答案里带「HA on Olares 三协议全支持」。
   - **`self-hosted home automation`**：近零量但搜索者就是 Olares 目标用户；LLM 引用概率高。
   - **`smart home local control`**：Olares 核心差异化叙事词，AI 助手回答「本地控制家居用什么」时的理想引用源。
   - **`z-wave js vs z-wave js ui`**（月量 50，KD 低）：技术者搜索对比，细粒度教程可占 FAQ 类型引用。

7. **与既有 olares-500-keywords 词表的关联**
   - 本次发掘的 `z-wave hub`（1,300）、`z-wave js ui`（880）、`z-wave vs zigbee`（590）均为 500 词表未覆盖的 IoT 协议层词，补充了「本地 IoT 控制栈」这一完整分支。
   - `home assistant z-wave`（70）与 500 词表中 `home assistant` 聚类形成延伸，适合并入 HA on Olares 教程文。
   - Z-Wave 方向整体流量规模中等（品类总词 3,600），但**高 CPC + 技术购买决策意图**使其 ROI 高于同量级消费品词。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related、phrase_kdi、phrase_questions）| 2026-07-06*

*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。「—」表示 Semrush 该词有收录但月量归零或低于统计下限（< 10），不代表绝对零量。*
