---
task_id: 01
role: 智能插座/开关市场分析师
status: complete
sources_found: 16
---

## Sources
[N1] Belkin: Wemo Support Ending（云 2026-01-31 关停） | https://www.belkin.com/my/support-article?articleNum=335419 | Source-Type: official | As Of: 2026-01 | Authority: 9/10
[N2] The Verge: Belkin Wemo devices go offline | https://www.theverge.com/tech/870890/belkin-wemo-cloud-services-shut-down | Source-Type: journalism | As Of: 2026-01 | Authority: 8/10
[N3] CNET: Belkin Ending Support for Wemo | https://www.cnet.com/home/smart-home/belkin-is-ending-support-for-wemo-smart-home-devices-heres-what-that-means-for-you/ | Source-Type: journalism | As Of: 2026-01 | Authority: 8/10
[N4] Shelly Group FY2025 Results（€149.7M, +40.3%） | https://corporate.shelly.com/en/news/shelly-group-significantly-increases-revenue-and-profitability-in-fy-2025 | Source-Type: official | As Of: 2026-02 | Authority: 10/10
[N5] Shelly "No cloud required" 本地控制 | https://shelly.com/ | Source-Type: official | As Of: 2026 | Authority: 7/10
[N6] Shelly Network Design Guide Gen2+（本地 MQTT/WebSocket） | https://kb.shelly.cloud/knowledge-base/network-design-guide-for-shelly-gen2-devices | Source-Type: official | As Of: 2026 | Authority: 8/10
[N7] The Gadgeteer: 8 Smart Plugs 2026 | https://the-gadgeteer.com/2026/07/02/smart-plugs-everyday-problems/ | Source-Type: other | As Of: 2026-07 | Authority: 5/10
[N8] SmartHomeExplorer: 5 Best Smart Plugs 2026 | https://www.smarthomeexplorer.com/guides/best-smart-plugs-worth-buying-2026 | Source-Type: other | As Of: 2026 | Authority: 5/10
[N9] Local Smart Home Guide: Smart Plug Comparisons | https://localsmarthomeguide.com/compare/categories/plug/ | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N10] modernhomecompass: Energy Monitoring Plugs Offline | https://modernhomecompass.com/en/energy-monitoring-smart-plugs-matter-home-assistant-guide | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N11] tecnoyfoto: Sonoff HA Local Integration Guide 2026 | https://tecnoyfoto.com/en/sonoff-home-assistant-local-integration-guide-2026 | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N12] AlexxIT: SonoffLAN 本地控制（GitHub） | https://github.com/AlexxIT/SonoffLAN | Source-Type: community | As Of: 2026 | Authority: 7/10
[N13] Big Iron: ESPHome vs Tasmota vs WLED | https://www.bigiron.cc/guides/esphome-vs-tasmota-vs-wled | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N14] JPK.io: Lutron Caseta Review 2026 | https://jpk.io/home-automation/lutron-caseta-review/ | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N15] HomeTechTested: Best Smart Light Switches 2026 | https://www.hometechtested.com/blog/best-smart-light-switches-2026/ | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N16] Bees Lighting: Matter over Thread vs Proprietary Hubs | https://www.beeslighting.com/blogs/ideas-advice-blog/smart-lighting-matter-over-thread-vs-proprietary-hubs | Source-Type: other | As Of: 2026 [u] | Authority: 4/10

## Findings
- 无单一霸主，品类高度碎片：Wi-Fi 畅销 Kasa/Tapo，本地商业 Shelly，墙面开关 Lutron，DIY Sonoff。[N7][N8][N14]
- Belkin 2026-01-31 关停 Wemo 云（2025-07 首宣）；仅 Thread 型号（WLS0503/WSC010/WSP100/WDC010）+ 事前配好的 HomeKit 型号存活，其余变哑，或走 PyWeMo 接 HA；提供部分退款。[N1][N2][N3]
- Shelly Group SE（原 Allterco Robotics，2015 索非亚创立，法兰克福 SLYG）FY2025 营收 €149.7M（+40.3%），累计 23M+ 台，安装商 5,300+，核心卖点 "no cloud required"。[N4][N5]
- TP-Link Kasa KP125M ~$20，Matter + 计量，"works with everything"；Tapo P115 便宜计量装（无 Matter）。[N7][N8]
- Lutron Caséta：专有 Clear Connect 434MHz、接近零丢包、无需零线、$80 Smart Bridge 带 50–75 台、Pico 遥控、至 2026 中无原生 Matter、生态锁定。[N14][N15][N16]
- Sonoff 本地三路：SonoffLAN 免刷机（断网仍可控）、Tasmota（MQTT 通用）、ESPHome（HA 原生加密 API）；Zigbee 型号走 ZHA/Z2M，新 Matter 型号（MINIR4M）走 HA Matter。[N11][N12][N13]
- Shelly Plus/Plug S（Gen3）出厂带本地 REST API + MQTT，无需云账号，0.1W/1s 计量，HA 集成 2022.6 进核心——公认最适合 HA。[N9][N10]
- Wi-Fi Matter "伪本地"：Kasa 默认经厂商基础设施路由 Matter，需 app 里显式开本地模式再配 HA。[N10]
- ESPHome 2026.5.0 推 Device Builder + Tasmota→ESPHome OTA 转换。[N13]

## Market Leaders
- Wi-Fi 畅销/全能：TP-Link Kasa / Tapo（KP125M ~$20，Matter + 计量）。[N7][N8]
- 本地控制财务锚：Shelly Group SE（SLYG）FY2025 €149.7M +40.3%，23M+ 台。[N4][N5]
- 墙面开关/调光可靠性：Lutron Caséta（Clear Connect 434MHz，无零线）。[N14][N15][N16]
- DIY/可刷机：Sonoff（ITEAD）SonoffLAN/Tasmota/ESPHome。[N11][N12][N13]
- Alexa 入门：Amazon Smart Plug；Apple/Thread 隐私向：Eve Energy。[N7][N10]
- 云关停反面教材：Belkin Wemo（2026-01-31）。[N1][N2][N3]
- 母公司：TP-Link/Belkin/Shelly Group SE/ITEAD/Lutron/Amazon/Eve/Aqara/Meross/Govee/Emporia/Zooz。[N4][N7][N8][N14]

## Segment Champions
- Wi-Fi/Matter：Kasa KP125M（计量 + 跨生态）；Tapo P115 便宜计量。[N7][N8]
- 本地优先商业：Shelly Plus/Plug S（原生 REST/MQTT，无需云账号）。[N9][N10]
- 墙面开关/调光：Lutron Caséta（专有 434MHz，专业标准，无 Matter）。[N14][N15][N16]
- 可刷机/DIY：Sonoff + SonoffLAN/Tasmota/ESPHome；Athom 出厂预刷 ESPHome。[N11][N12][N13]
- Zigbee/Z-Wave 本地：Sengled/ThirdReality（Zigbee）、Zooz ZEN04/ZEN15（Z-Wave）、Aqara、frient。[N9][N10]
- Apple/Thread 隐私：Eve Energy（Thread + Matter，本地存储，无订阅）。[N7][N10]

## VC Rising Stars
- Shelly Group SE（SLYG）：本品类罕见高增长上市纯玩家，FY2025 +40.3%，卖点即 "no cloud"。[N4][N5]
- 开源事实标准（真正"明日之星"在软件）：ESPHome（2026.5.0 Device Builder + Tasmota→ESPHome OTA）、Tasmota、SonoffLAN、Zigbee2MQTT，归 Open Home Foundation 生态。[N12][N13]
- 反向信号：Belkin 放弃 Wemo 品类，纯 Wi-Fi 云插座模型难续，资本向"本地 + 能量管理软件"迁移。[N1][N4]

## Candidate Keywords
wemo alternative / kasa alternative / lutron caseta alternative / aqara smart plug alternative / amazon smart plug alternative / smart plug without cloud / local smart plug / smart plug home assistant / best smart plug home assistant / shelly plug / sonoff home assistant / tasmota / esphome / smart switch without cloud / matter smart plug / best smart plug 2026 / best smart plug energy monitoring / shelly vs sonoff / kasa vs tapo / lutron caseta vs kasa / best smart light switch / zigbee smart plug / best smart plug no neutral wire / energy monitoring smart plug home assistant

## Deep Read Notes
### Source [N1][N2][N3]: Wemo 云关停
Key data: Belkin 2026-01-31 关停 Wemo 云（2025-07 首宣）；app 停更、远程/Alexa/Google 全失效；仅 Thread 型号（WLS0503/WSC010/WSP100/WDC010）+ 事前配好 HomeKit 的型号存活；其余变哑或走 PyWeMo 接 HA；提供部分退款。
Key insight: 云依赖硬件的"智能"= 厂商存续依赖，是 Olares 本地栈叙事最锋利的锚点。

### Source [N4][N5]: Shelly FY2025
Key data: Shelly Group SE（原 Allterco Robotics，2015 索非亚，法兰克福 SLYG）FY2025 €149.7M（+40.3%），累计 23M+ 台，安装商 5,300+，2026 扩能量监测/智能锁/AI；核心卖点 "no cloud required"，MQTT/REST/WebSocket 本地。
Key insight: 证明"本地优先 + 能量管理软件"是插座品类可盈利、可增长的路径，与 Olares 自托管方向一致。

### Source [N10]: Wi-Fi Matter 伪本地
Key data: Kasa 默认经厂商基础设施路由 Matter，需 app 显式开本地模式再配 HA，否则计量延迟 5–15s。
Key insight: "支持 Matter" ≠ "真本地"，是选购去云插座的关键实操坑。

## Gaps
- 各品牌无 brand-seo 报告；HA/ESPHome/Tasmota 仅零散 market 资产。
- 无 2026 免费的按品牌精确出货份额 %；畅销排名多为评测媒体口径[u]（[N7][N8][N9][N13][N14][N15][N16]）。
- Kasa/Tapo/Aqara/Meross/Govee/Emporia 私营或大厂内嵌，无独立财务。
- Lutron 私营（10,000+ 员工），无公开营收；Sonoff/ITEAD 无公开财务。
- Wi-Fi Matter 各型号"真本地"边界缺实测矩阵（哪些默认绕云）。[N10]

## END
