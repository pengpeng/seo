---
task_id: 01
role: 传感器/网关市场分析师
status: complete
sources_found: 15
source: WebSearch + WebFetch（>=6 源）+ 原家居分册 seed 笔记（source [11] Matter / [22] SmartThings）
---

## Sources
[N1] SmartThings 430M Users (CES 2026, SamMobile) | https://www.sammobile.com/news/smartthings-now-boasts-430-million-users-across-the-globe/ | Source-Type: journalism | As Of: 2026-01 | Authority: 7/10
[N2] Samsung SmartThings — Transforming Standards (CSA-IoT PDF) | https://csa-iot.org/wp-content/uploads/2025/10/samsung-smartthings-transforming-standards_into_everyday-experiences.pdf | Source-Type: official | As Of: 2025-10 | Authority: 9/10
[N3] Aqara Hub M3 Product Page | https://us.aqara.com/products/hub-m3 | Source-Type: official | As Of: 2026 [u] | Authority: 8/10
[N4] Aqara CES 2025 Lineup (Hub M100 / FP300 / Border Routers) | https://www.businesswire.com/news/home/20250106874900/en/CES-2025-Aqara-Showcases-Innovative-Smart-Home-Solutions-for-a-Seamless-Intuitive-Experience | Source-Type: official | As Of: 2025-01 | Authority: 8/10
[N5] Philips Hue Account Mandatory (The Verge) | https://www.theverge.com/2023/9/28/23892761/philips-hue-app-account-changes | Source-Type: journalism | As Of: 2023-09 | Authority: 8/10
[N6] Hue Force Users Upload Data to Cloud (Home Assistant) | https://www.home-assistant.io/blog/2023/09/22/philips-hue-force-users-upload-data-to-cloud/ | Source-Type: community | As Of: 2023-09 | Authority: 7/10
[N7] What is a Thread Border Router (Matter Alpha) | https://www.matteralpha.com/explainer/thread-border-router | Source-Type: other | As Of: 2025-2026 [u] | Authority: 5/10
[N8] Understand Smart Home Thread Support (Amazon Developer) | https://developer.amazon.com/en-US/docs/alexa/smarthome/thread-support.html | Source-Type: official | As Of: 2026 [u] | Authority: 8/10
[N9] Z-Wave Alliance — 125 ZWLR Certified Devices (CES 2026) | https://z-wavealliance.org/news_p/z-wave-alliance-highlights-newly-certified-z-wave-long-range-devices/ | Source-Type: official | As Of: 2026-01 | Authority: 8/10
[N10] Introduction to Z-Wave 800 Series (Silicon Labs) | https://www.silabs.com/wireless/z-wave/introduction-to-z-wave-800-series | Source-Type: official | As Of: 2025 [u] | Authority: 8/10
[N11] Zigbee2MQTT Supported Devices (5,473 / 577 vendors) | https://www.zigbee2mqtt.io/supported-devices/ | Source-Type: community | As Of: 2026-07 | Authority: 8/10
[N12] Koenkk/zigbee2mqtt GitHub (15,152 stars, GPL-3.0) | https://github.com/koenkk/zigbee2mqtt/ | Source-Type: community | As Of: 2026-05 | Authority: 9/10
[N13] SMLIGHT SLZB-06 (Ethernet Zigbee coordinator, Z2M/ZHA/OTBR) | https://smlight.tech/gb/slzb-06 | Source-Type: official | As Of: 2026 [u] | Authority: 6/10
[N14] Matter Integration (Home Assistant, seed [11]) | https://www.home-assistant.io/integrations/matter/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[N15] Matterbridge zigbee2mqtt (expose Z2M to Matter locally) | https://github.com/Luligu/matterbridge-zigbee2mqtt | Source-Type: community | As Of: 2026-03 | Authority: 7/10

## Findings
- SmartThings 2025-12 达 430M 注册用户、390 partners、4,700 设备（CES 2026 宣布，2024-09 时为 350M，一年 +80M）；CSA PDF 口径 425M+、支持 50 个 Matter 1.4 设备类型，Aeotec Smart Home Hub 2 2025 秋上市。[N1][N2]
- Aqara 多协议 Hub 线：M3（Zigbee 3.0+Thread+Matter+IR+PoE，直连 64、桥接 127，Matter Bridge + Controller + TBR，边缘自动化 + LAN 本地控制）、M2、入门 M100（USB-A 供电）、M200（+360° IR），绿米海外在售保留。[N3][N4]
- Aqara IFA 2025 主打"空间智能"：presence FP300 / climate W100 多传感融合，从卖传感器转向卖场景 AI。[N4]
- Philips Hue Bridge：Zigbee 本地控制 + 官方/HomeKit API，但 Signify 2023-09 起强制 Hue 账号才能用 App / 配 Matter；本地控制仍可用、可防火墙断网但失去 OTA/远程。[N5][N6]
- Thread Border Router 广泛"隐形"内置于 Amazon Echo(4th)/Echo Hub/Echo Show/eero、Apple HomePod mini/HomePod(2nd)/Apple TV 4K、Google Nest Hub(2nd)/Nest Hub Max/Nest Wifi；部分 Nanoleaf 灯也是 TBR；不同生态各建独立 Thread 网，Thread 1.4 才推跨生态凭据共享。[N7][N8]
- Z-Wave：Silicon Labs 800 系列 + Long Range（star 拓扑、直连 hub、range 可达 1.5 mi、10 年币电池）；2026-01 CES Alliance 宣布 125 款 ZWLR 认证设备，Zooz/Jasco 为主力，向 EMEA 扩。[N9][N10]
- 支持 ZWLR 的 hub：2GIG Edge、Qolsys IQ、Aeotec(SmartThings)、Hubitat C-8 Pro、HomeSeer HS4、Ring Alarm Pro、Home Assistant（配 Zooz ZST39 LR / Aeotec Z-Stick 7 USB 棒）。[N9]
- 开源自托管栈：Zigbee2MQTT 支持 5,473 款设备 / 577 厂商，15,152 stars，GPL-3.0，最新 2.10.1；网络协调器 SMLIGHT SLZB-06（以太网/PoE，Z2M+ZHA+OTBR）与 HA SkyConnect/ZBT-1、Sonoff Dongle-E。[N11][N12][N13]
- HA Matter 集成（seed [11]）支持本地 Matter over Wi-Fi/Thread，可自建 OTBR；Z2M 无原生 Matter，需 Matterbridge 把 Z2M/Shelly 本地暴露成 Matter 给 Apple/Google/Alexa/SmartThings。[N14][N15]

## Market Leaders
- 平台级中枢：Samsung SmartThings（430M 用户，Aeotec 代工 Hub 2）。[N1][N2]
- 多协议 DIY Hub：Aqara/绿米 Hub M2/M3/M100/M200。[N3][N4]
- 生态桥接：Philips Hue Bridge（Signify）。[N5]
- 隐形 Thread Border Router：Amazon Echo/eero、Apple HomePod/TV、Google Nest Hub。[N7][N8]
- 协议阵营：Zigbee（Aqara/Hue/IKEA）、Z-Wave（Silicon Labs 800 + Zooz/Jasco）、Thread/Matter（CSA）。[N9][N10][N14]

## Segment Champions
- 平台级中枢：SmartThings（规模最大、重云）。[N1][N2]
- 多协议本地 Hub：Aqara Hub M3（边缘自动化 + LAN 控制）。[N3][N4]
- Zigbee 桥接：Hue Bridge（社区可 ZHA/Z2M 直连灯珠绕开）。[N5]
- Z-Wave DIY：Zooz 800/ZWLR。[N9][N10]
- 网络 Zigbee 协调器：SMLIGHT SLZB-06 / HA SkyConnect / Sonoff Dongle-E。[N13]
- 自托管唯一 Hub（最强 Olares 落点）：Home Assistant（Z2M/ZHA/Z-Wave JS/Matter Server/OTBR）。[N11][N14]

## VC Rising Stars
- Matter/Thread（CSA）：SmartThings 50 Matter 设备类型；Thread 1.4 跨生态凭据共享。[N2][N7]
- Z-Wave Long Range：CES 2026 125 款 ZWLR，向 EMEA 扩。[N9]
- Aqara "空间智能"：presence/climate 多传感 + 边缘 Hub。[N4]
- 开源事实标准：Zigbee2MQTT（5,473 设备/15.1k stars）+ Matterbridge = "闭源云中枢 vs 开源本地中枢"双轨。[N11][N15]

## Candidate Keywords
smartthings alternative / aqara alternative / hue bridge alternative / philips hue without account / local smart home hub / smart home hub without cloud / self hosted smart home / home assistant hub / zigbee2mqtt / zigbee coordinator / matter server home assistant / thread border router home assistant / z-wave js / local zigbee hub / best zigbee hub / zigbee vs z-wave / zigbee vs thread / matter vs zigbee / best thread border router / skyconnect vs slzb-06 / best presence sensor home assistant / aqara vs smartthings / best door sensor zigbee

## Deep Read Notes
### Source [N1][N2]: SmartThings 规模
Key data: 2025-12 430M 注册用户（2024-09 为 350M）、390 partners、4,700 设备；CSA PDF 425M+、50 个 Matter 1.4 设备类型、"Hub Everywhere"策略把 Hub 内嵌进 TV/soundbar/appliance；Aeotec Hub 2 2025 秋（Matter/Thread/Zigbee）。
Key insight: 规模最大的中枢 = 最大的单一数据聚合点；"注册用户"口径可能高估活跃安装。是"local smart home hub"叙事的头号对标。

### Source [N5][N6]: Hue 强制账号
Key data: Signify 2023-09 宣布用官方 App / 配 Matter 必须登录 Hue 账号；本地控制仍在、可防火墙断网但失 OTA/远程；隐私政策允许存储并与 partner 共享数据。
Key insight: 即使"本地能用"的 Bridge 也在把入口云化——`philips hue without account` / `hue bridge alternative` 是精准长尾。

### Source [N7][N8]: 隐形 Thread Border Router
Key data: Echo(4th)/Echo Hub/eero、HomePod mini/Apple TV 4K、Nest Hub(2nd) 皆内置 TBR；不同生态各建独立 Thread 网，凭据托管各自云；Thread 1.4 才推跨生态共享。
Key insight: 用户"已经拥有一个云网关而不自知"，是隐私叙事的强钩子；HA 自建 OTBR 把 Thread 凭据留本地是差异点。

## Gaps
- 各中枢/传感器品牌无 brand-seo 报告；HA 仅 market 报告（见 seed [22]）。
- 未找到免费的按品牌精确出货份额 %（SmartThings/Aqara/Hue 装机量口径不一）。
- SmartThings "430M 用户"为注册累计口径，活跃安装量未披露[u]。
- Aqara 海外营收/份额、Zooz(The Smartest House) 私营财务缺公开数据[u]。
- Matter over Thread commissioning 的本地边界（哪些 Hub 强制账号/云）缺实测矩阵[N14]。
- Thread 1.4 跨生态凭据共享的真实落地进度待跟踪[N7]。

## END
