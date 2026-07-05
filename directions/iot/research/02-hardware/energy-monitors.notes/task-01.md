---
task_id: 01
role: 能源 / 电表 / 太阳能市场分析师
status: complete
sources_found: 16
source: web research（WebSearch + WebFetch，AS_OF 2026-07-04）+ 家居分册 seed 承接源（媒体/敏感 IoT 能源行 [15][16][17][22]）
---

## Sources
[N1] MarkWide: Home Energy Monitor Market 2026–2036 | https://markwideresearch.com/home-energy-monitor-market | Source-Type: secondary-industry | As Of: 2026 [u] | Authority: 4/10
[N2] BusinessResearchInsights: Home Energy Monitor Market | https://www.businessresearchinsights.com/market-reports/home-energy-monitor-market-105462 | Source-Type: secondary-industry | As Of: 2026-06 | Authority: 5/10
[N3] Valuates/QYResearch: Global Home Energy Monitor | https://reports.valuates.com/market-reports/QYRE-Auto-9A9238/global-home-energy-monitor | Source-Type: secondary-industry | As Of: 2026 [u] | Authority: 5/10
[N4] EnergyMeterHub: Emporia Vue 3 vs Shelly EM vs Schneider | https://www.energymeterhub.com/articles/best-whole-home-energy-monitor-emporia-vue-3-vs-shelly-em-vs-schneider | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N5] Enphase: Q1 2026 Financial Results | https://investor.enphase.com/news-releases/news-release-details/enphase-energy-reports-financial-results-first-quarter-2026 | Source-Type: official | As Of: 2026-04 | Authority: 10/10
[N6] PV Tech: Enphase Q1 2026 / 25D 到期 | https://www.pv-tech.org/lower-residential-demand-after-25d-tax-credit-ends-impacts-enphases-q1-2026-revenue/ | Source-Type: journalism | As Of: 2026-04 | Authority: 7/10
[N7] AgentSolar: Most Popular Solar Batteries 2026 | https://agentsolar.ai/solar-batteries | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N8] The Energy Brief: Best Home Battery Storage 2026 | https://theenergybrief.net/article/best-home-battery-storage-for-2026-tesla-enphase-and-beyond | Source-Type: other | As Of: 2026 [u] | Authority: 4/10
[N9] Emporia Vue Local: ESPHome 本地控制指南 | https://emporia-vue-local.github.io/docs/tutorial/intro/ | Source-Type: community | As Of: 2026-01 | Authority: 7/10
[N10] GitHub: emporia-vue-local/esphome (~755 stars) | https://github.com/emporia-vue-local/esphome | Source-Type: community | As Of: 2026-01 | Authority: 8/10
[N11] MarketIntelo: NILM for Utilities Market | https://marketintelo.com/report/non-intrusive-load-monitoring-for-utilities-market | Source-Type: secondary-industry | As Of: 2025 [u] | Authority: 4/10
[N12] ResearchAndMarkets/Businesswire: North America Smart Metering 2025 | https://www.businesswire.com/news/home/20250731000744/en/ | Source-Type: secondary-industry | As Of: 2025-07 | Authority: 7/10
[N13] DataIntelo: Residential Single-Phase Smart Meter | https://dataintelo.com/report/global-residential-single-phase-electricity-smart-meter-market | Source-Type: secondary-industry | As Of: 2026 [u] | Authority: 4/10
[N14] LocalSmartHomeGuide: Shelly Pro 3EM | https://localsmarthomeguide.com/products/shelly-pro-3em/ | Source-Type: other | As Of: 2025-2026 [u] | Authority: 4/10
[N15] Shelly: Pro 3EM 官方文档 | https://automations.shelly.com/blogs/documentation/shelly-pro-3em | Source-Type: official | As Of: 2026 [u] | Authority: 8/10
[N16] SmartWattFlow: HA Energy Monitoring Guide 2026 | https://smartwattflow.com/blog/home-assistant-energy-monitoring-guide | Source-Type: other | As Of: 2026 [u] | Authority: 4/10

承接自原家居分册 seed 笔记：
[15] Enphase IQ Gateway 持续上报产/用电 | https://enphase.com/en-eu/legal/privacy-policy | policy · 2025 · 7/10
[16] Sense 用电指纹→美区服务器+AI(GDPR) | https://sense.com/gdpr/ | policy · 2025 · 7/10
[17] 智能电表 NILM 再识别(学术) | https://dbis.ipd.kit.edu/download/Buchmann2013_Article_Re-identificationOfSmartMeterD.pdf | academic · 2013-2024 · 8/10
[22] Emporia Vue→ESPHome 本地化对接 HA Energy | https://emporia-vue-local.github.io/docs/tutorial/intro | community · 2026-01 · 7/10

## Findings
- 家庭能源监测市场口径分歧极大：MarkWide $1.8B 2026 / 14.6% CAGR；Valuates/QYResearch $265M 2025→$486M 2032 / 9.2%；BusinessResearchInsights $0.3B 2026→$0.7B 2035 / 9.2%；差 5–6 倍。[N1][N2][N3]
- 家庭能源监测三主线：Sense（云 disaggregation 算法 + DTC）、Emporia（低价 16 路 CT，solar-ready 改装位）、Schneider/Square D（断路器集成，B2B 商用楼宇）。[N1][N4]
- 太阳能储能安装报价份额（AgentSolar 14.3 万报价样本）：Tesla 63.3% / Enphase 17.1% / SolarEdge 10.6%，Top3 合计 91%；30.8% 户用光伏含储能。[N7]
- Enphase（ENPH）Q1 2026 营收 $282.9M（环比 −17%），IQ 电池出货 103.1MWh，微逆 627.6MW；美区 −23%（25D 税抵 2025 底到期）、欧洲 +36%。[N5][N6]
- 智能电表/AMI 双寡头：Landis+Gyr（瑞士，FY24-25 ~$1.8B、装机 >2.4 亿只、Gridstream）+ Itron（~$2.4B、北美端点份额 64%、OpenWay Riva）；北美装机份额 Itron 35% / L+G 32% / Aclara 21%。[N12][N13]
- NILM 市场 ~$0.8B（2024），Itron/Landis+Gyr/Oracle/Siemens 覆盖 90%+ 全球电力公司装机；Sense/Bidgely/Verdigris 为专业算法方。[N11]
- 隐私：Sense ~1MHz 级采样用电指纹→云 ML 识别电器→推断作息；智能电表 NILM 可推断在家行为/再识别家庭。[16][17]
- Emporia Vue 2/3 可刷 ESPHome（emporia-vue-local，~755 stars）：UL 认证硬件 + 开源固件，5 秒级本地更新、完全离线、云停服不影响。[N9][N10]
- Shelly EM / Pro 3EM 出厂即本地：DIN 导轨三相 ~1% 精度、本地 HTTP/RPC+MQTT+Modbus、板载 60 天 1 分钟数据、HA 官方集成直喂 Energy Dashboard、无需云。[N14][N15]
- HA Energy Dashboard 是本地能源看板/自动化中枢，聚合 Shelly/Emporia(ESPHome)/智能插座。[N16]

## Market Leaders
- 家庭能源监测：Sense（云 AI）/ Emporia（超值电路级）/ Schneider·Square D（配电箱生态）。[N1][N4]
- 太阳能储能：Tesla Powerwall 3（~63.3% 报价份额）/ Enphase IQ（~17.1%，NASDAQ:ENPH）/ SolarEdge（~10.6%）/ FranklinWH。[N5][N7][N8]
- 智能电表/AMI：Landis+Gyr（营收龙头 ~$1.8B）/ Itron（端点龙头，北美 64%）/ Aclara(Hubbell) / Sensus(Xylem) / Honeywell。[N12][N13]
- 上市锚：ENPH / SEDG / TSLA / ITRI / Landis+Gyr(SIX:LAND)；Sense/Emporia/FranklinWH 私营。

## Segment Champions
- 云 AI 电器识别：Sense。[N1][16]
- 电路级性价比：Emporia Vue 3（2×200A 主 + 16 分支 CT）。[N4]
- 本地优先/HA 原生：Shelly Pro 3EM（三相），Shelly EM（单/双路预算）。[N14][N15][N16]
- 配电箱生态：Schneider Energy Monitor / Square D。[N4]
- 储能一体机：Tesla Powerwall 3 / Enphase IQ 5P / FranklinWH aPower 2。[N7][N8]
- 自托管软件栈：Home Assistant Energy Dashboard。[N16]

## VC Rising Stars
- NILM 专业算法：Sense / Bidgely / Verdigris（vs AMI 集成商 Itron/Landis+Gyr/Oracle/Siemens 90%+ 电力公司装机）。[N11]
- 储能规模玩家：Enphase(ENPH) / Tesla Energy / SolarEdge / FranklinWH；政策拐点 = 美国 25D 税抵 2025 底到期，Enphase 美区 −23%、欧洲 +36%。[N5][N6][N7]
- 开源双轨：emporia-vue-local ESPHome(~755★) + Shelly 原生本地 API + HA Energy vs 厂商云。[N9][N10][N14]

## Candidate Keywords
sense energy monitor alternative / emporia alternative / sense vs emporia / shelly em vs emporia vue / tesla powerwall alternative / home assistant energy monitor / home assistant energy dashboard / emporia vue esphome / emporia vue local / shelly em home assistant / shelly pro 3em home assistant / local energy monitor no cloud / self hosted energy monitor / energy monitor without cloud / best whole home energy monitor / best home energy monitor / emporia vue vs shelly / best solar battery 2026 / powerwall vs enphase / smart meter privacy / nilm privacy

## Deep Read Notes
### Source [N5][N6]: Enphase Q1 2026
Key data: 营收 $282.9M（环比 −17%）；IQ 电池 103.1MWh；微逆 1.41M 台/627.6MW；美区占 83%、环比 −23%；欧洲 +36%；non-GAAP 毛利 43.9%；累计装机 >520 万套/165 国。
Key insight: 25D 户用税抵到期是户用光伏拐点；欧洲储能因自消费/动态电价/VPP 成"battery-critical"。上市财务是本章最硬锚。

### Source [N9][N10]: Emporia Vue ESPHome
Key data: 支持 Vue 2/3；UL 认证硬件 + 非官方开源固件；5 秒级更新；完全离线；需 USB-serial（CH340G）首刷；~755 stars，2026-01 仍活跃。
Key insight: "买 UL 认证便宜硬件 + 刷 ESPHome 去云 + HA Energy" 是监测侧最强 Olares 平替路径，直接承接 sense/emporia alternative 意图。

### Source [N12][N13]: 智能电表 AMI
Key data: 北美装机份额 Itron 35% / Landis+Gyr 32% / Aclara 21%；端点 Itron 64%；Landis+Gyr FY24-25 ~$1.8B/>2.4 亿只；Itron ~$2.4B；Wi-SUN mesh 主流。
Key insight: 电表是电力公司资产，用户无权更换/自托管——诚实差距的根源；只能旁挂自己的 CT 监测替代。

## Gaps
- 家庭能源监测市场规模口径分歧 5–6 倍（是否含电表/储能/商用），无免费统一口径。[N1][N2][N3]
- 太阳能储能"份额"为安装报价样本（AgentSolar）而非出货口径，非严格市占。[N7]
- Sense/Emporia/FranklinWH 私营，无官方营收/份额；Top5 39% 为 2019 陈旧口径。[N3]
- 智能电表用户无法自托管 AMI，只能读电力公司聚合/interval 数据。
- Solar inverter（Tesla Powerwall/Enphase IQ）本地 API 受厂商限权，可随时收紧，无完整开源替代固件。[15]
- Sense 云 AI 电器识别体验本地栈难完全复刻（开源 NILM 精度有限）。
- Shelly EM「total_active_energy」需手动启用 disabled entity 才能进 HA Energy Dashboard；净计量需 utility meter helper。[N16]

## END
