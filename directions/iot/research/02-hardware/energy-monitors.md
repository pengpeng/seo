# 能源 / 电表 / 太阳能竞品与关键词（IoT 方向 · 品类 21）

> 研究日期: 2026-07-04 | 来源: task-01（16 源 web research）+ 原家居分册 seed 笔记（能源行）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 家庭能源监测（whole-home energy monitor / 电路级 CT 监测）、太阳能与储能（solar/storage、微逆/混合逆变器、家庭电池）、智能电表/AMI（smart meter / advanced metering infrastructure）。EV 充电、智能插座见其他品类。归属 IoT 新方向"硬件章"。发现笔记见 [energy-monitors.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/energy-monitors.notes)。

## 摘要
能源是 IoT 章里"监测侧 Olares 平替极强、发电/电表侧诚实差距明显"的分裂品类。三条子赛道各有巨头：家庭能源监测（home energy monitor）由 **Sense**（disaggregation 算法 + DTC 品牌）、**Emporia**（低价电路级 CT）、**Schneider/Square D**（配电箱生态）主导，市场口径分歧大（$0.27B–$1.8B、CAGR 9%–15%）[N1][N2][N3]；太阳能/储能由 **Tesla Powerwall**（安装报价份额 ~63.3%）、**Enphase IQ**（~17.1%，NASDAQ:ENPH，Q1 2026 营收 $282.9M）、**SolarEdge**（~10.6%）领跑 [N5][N6][N7]；智能电表/AMI 由 **Landis+Gyr**（全球营收龙头 ~$1.8B、装机 >2.4 亿只）与 **Itron**（~$2.4B）双寡头，北美装机份额 35%/32% [N11][N12][N13]。**隐私核心**：Sense 高分辨率（~1MHz 级采样）用电指纹 → 云 ML 识别电器 → 推断作息 [seed 16]；智能电表 NILM 可推断在家行为、再识别家庭 [seed 17]；Enphase/Tesla 持续把产/用电上报云 [seed 15]。**Olares 落点（监测强）**：HA Energy Dashboard + Emporia Vue（刷 ESPHome 去云）/ Shelly EM·Pro 3EM（原生本地 RPC/MQTT），电路级本地监测规避 NILM 云推理 [N9][N10][N14][N15][N16]。**诚实差距**：智能电表用户无法自托管 AMI（只能读聚合数据）；solar inverter 本地读数受厂商限权，Tesla/Enphase 可随时收紧 API。

## 1. 品类概述
本章按"数据链路"分三层：① **家庭能源监测**——CT 钳夹在总线/分支电路，测功率/用电，云 App 或本地 dashboard 呈现，Sense 型走"1 个总监测 + 云 AI 拆分电器"，Emporia 型走"16 路电路级 CT + 便宜硬件"[N1][N4]；② **太阳能/储能**——微逆（Enphase）、混合逆变器 + 家庭电池（Tesla Powerwall 3、SolarEdge、FranklinWH），逆变器/网关持续上报产/用电到厂商云 [N5][N7][seed 15]；③ **智能电表/AMI**——电力公司资产，Landis+Gyr/Itron 的 RF-mesh/Wi-SUN 端点把 15/30 分钟（乃至更细）interval data 回传，用户无权更换或自托管 [N12][N13]。共性隐私风险：**用电曲线本身即行为数据**，分辨率越高越能还原"谁在家、用什么电器、作息如何"。监测层可完全本地化，发电层部分本地化，电表层几乎不可自托管。

## 2. 市场领导者 / top 畅销
| 子赛道 | 领导者 | 锚点 |
|------|--------|------|
| 家庭能源监测（云 AI） | Sense（Sense Labs，私营） | disaggregation 算法 + DTC 品牌；2019 Top5 合计 >39% 份额 [N1][N3] |
| 家庭能源监测（超值电路级） | Emporia（Emporia Energy，US 私营） | Vue 3 16-CT kit，solar-ready 零售改装位 [N1][N4] |
| 家庭能源监测（配电箱生态） | Schneider Electric / Square D | 断路器集成 + B2B 渠道，锚定商用楼宇 [N1][N4] |
| 太阳能储能（量） | Tesla Powerwall 3 | 安装报价份额 ~63.3%（14.3 万+ 报价样本）[N7][N8] |
| 太阳能微逆/储能（上市锚） | Enphase（NASDAQ:ENPH） | Q1 2026 营收 $282.9M、IQ 电池出货 103.1MWh；份额 ~17.1% [N5][N7] |
| 太阳能储能（#3） | SolarEdge | 安装报价份额 ~10.6% [N7] |
| 智能电表/AMI（全球营收龙头） | Landis+Gyr（瑞士 Zug） | FY24-25 营收 ~$1.8B、装机 >2.4 亿只，Gridstream 平台 [N13] |
| 智能电表/AMI（北美端点龙头） | Itron（NASDAQ:ITRI） | 2024 营收 ~$2.4B、北美端点份额 64%，OpenWay Riva [N12][N13] |

母公司/上市：Enphase（NASDAQ:ENPH）、SolarEdge（NASDAQ:SEDG）、Tesla（NASDAQ:TSLA）、Itron（NASDAQ:ITRI）、Landis+Gyr（SIX:LAND）；Sense/Emporia/FranklinWH 私营。

**置信度: Medium**（上市财务与北美电表份额可靠；家庭能源监测市场口径分歧极大[u]，太阳能份额为安装报价样本非出货口径[u]）。

## 3. 细分赛道冠军
- **云 AI 电器识别冠军**：**Sense**——单点高分辨率采样 + 云 disaggregation，"看一个总电流猜出每个电器"体验最强，但强依赖云 ML [N1][seed 16]。
- **电路级性价比冠军**：**Emporia Vue 3**（2×200A 主 CT + 最多 16 分支 CT），"哪条电路在耗电"回答最干净，官方 App 云优先 [N4]。
- **本地优先/HA 原生冠军**：**Shelly Pro 3EM**（DIN 导轨三相、~1% 精度、本地 HTTP/RPC + MQTT + Modbus、板载 60 天 1 分钟数据、HA 官方集成直喂 Energy Dashboard、无需云）；单/双路预算位为 **Shelly EM** [N14][N15][N16]。
- **配电箱生态冠军**：**Schneider Energy Monitor / Square D**——监测贴近面板控制与未来负载管理硬件 [N4]。
- **储能一体机冠军**：**Tesla Powerwall 3**（集成混合逆变器、可直管 6 路组串）vs **Enphase IQ 5P**（5kWh 模块化、微逆可靠性）vs **FranklinWH aPower 2**（长时停电 + 发电机联动）[N7][N8]。
- **自托管软件栈冠军**：**Home Assistant Energy Dashboard**——聚合 Shelly/Emporia(ESPHome)/智能插座为本地能源看板与自动化中枢 [N16]。

**置信度: High**（各层冠军有评测与社区共识；本地栈 Shelly/Emporia+HA 组合成熟）。

## 4. VC 圈明日之星
硬件多大厂主导，"新星"集中在算法与去云社区：
- **NILM 专业算法方**：**Sense、Bidgely、Verdigris**——深耕负载拆分 ML，技术性能领先，但与电力公司 AMI 集成商（Itron/Landis+Gyr/Oracle Utilities/Siemens，覆盖 90%+ 全球电力公司）形成"专业算法 vs 装机规模"竞争 [N11]。
- **储能规模玩家**：Enphase（ENPH）与 Tesla Energy 是微逆/储能规模方；SolarEdge、FranklinWH 紧随 [N5][N7]。政策敏感——美国 25D 户用清洁能源税收抵免 2025 底到期，Enphase Q1 2026 美区营收环比 −23%，欧洲反而 +36%（储能自消费/动态电价驱动）[N6]。
- **开源双轨**：emporia-vue-local ESPHome（~755 stars）与 Shelly 原生本地 API + HA Energy 构成"开源本地 vs 厂商云"双轨 [N9][N10][N14]。

**置信度: Medium**（赛道热度与政策拐点可靠，具体私营估值/份额多为口径估计[u]）。

## 5. 候选产品关键词
品牌替代：`sense energy monitor alternative`、`emporia alternative`、`sense vs emporia`、`shelly em vs emporia vue`、`tesla powerwall alternative`（弱，储能难自托管）。
去云/本地（核心机会）：`home assistant energy monitor`、`home assistant energy dashboard`、`emporia vue esphome`、`emporia vue local`、`shelly em home assistant`、`shelly pro 3em home assistant`、`local energy monitor no cloud`、`self hosted energy monitor`、`energy monitor without cloud`。
选购/对比：`best whole home energy monitor`、`best home energy monitor`、`sense vs emporia vue`、`emporia vue vs shelly`、`best solar battery 2026`、`powerwall vs enphase`、`smart meter privacy`、`nilm privacy`。

> Olares Market 已有 Home Assistant 报告，`home assistant energy monitor`、`emporia vue esphome`、`shelly em home assistant`、`sense vs emporia` 是与现有资产最贴合的切入。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **用电指纹 → 云 ML 识别电器**：Sense 以高分辨率采样把总电流指纹化，上传美区服务器用 AI 识别具体电器并推断作息；用电曲线即行为数据 [seed 16]。
- **智能电表 NILM 再识别**：AMI interval data 经 NILM（non-intrusive load monitoring）可推断在家/离家、电器种类、家庭再识别；Landis+Gyr Gridstream、Itron DI 均在边缘/平台集成 NILM，用户无权拒收或自托管电表 [N11][seed 17]。
- **发电侧持续上报**：Enphase IQ Gateway、Tesla Powerwall 网关默认持续把产/用电上报厂商云，本地 API 受厂商限权、可随时收紧 [seed 15]。
- **Olares 平替栈（监测侧强）**：
  - **电路级监测** → Emporia Vue 2/3 刷 **ESPHome**（emporia-vue-local，UL 认证硬件 + 开源固件，5 秒级本地更新、完全离线、Emporia 云停服不影响）→ **HA Energy Dashboard** on Olares [N9][N10][N16]。
  - **原生本地** → **Shelly EM / Pro 3EM**（出厂即本地 RPC/MQTT，HA 官方集成直喂 Energy Dashboard，无需云；板载 60 天数据）[N14][N15]。
  - **编排** → Home Assistant on Olares 统一用电看板 + 分时电价/负载自动化，数据不出局域网 [N16]。
- **诚实差距**：① 智能电表（AMI）是电力公司资产，用户**无法自托管**，只能读电力公司提供的聚合/interval 数据（或旁挂自己的 CT 监测替代）；② solar inverter 本地读数因厂商（Tesla/Enphase）限权而脆弱，无完整开源替代逆变器固件；③ Sense 的"云 AI 电器识别"体验本地栈难以完全复刻（NILM 开源实现精度有限）。

**置信度: High（监测侧本地栈成熟）· Low（电表/逆变器无完整自托管平替）**。

## 7. 核心争议 / 反方 / 参考

**核心争议**：家庭能源监测市场规模口径分歧极大——MarkWide 报 2026 $1.8B / 14.6% CAGR，QYResearch/Valuates 报 2025 $265M / 9.2% CAGR、BusinessResearchInsights 报 2026 $0.3B，差 5–6 倍，源于是否把智能电表/储能/商用监测计入"home energy monitor"[N1][N2][N3]。太阳能储能"份额"多为安装报价样本（AgentSolar 14.3 万报价）而非出货口径，Tesla 63.3% 应视作报价热度而非严格市占 [N7]。

**反方解释**：Sense 的云 disaggregation 换来"无需逐电路布线即知每个电器耗电"的独特体验，多数用户接受用电数据上云换便利；智能电表由电力公司统一部署，用户既无选择权也不必自维护；Powerwall/IQ 的云 VPP（virtual power plant）能参与需求响应拿返利，纯本地会牺牲这一收益。自托管栈（Emporia 刷 ESPHome / Shelly + HA Energy）需要面板 CT 安装、固件刷写与 HA 配置知识，属技术用户路径；电表与逆变器则只能"网络隔离 + 旁挂本地监测"而非真正替代。

**参考文献**（Source-Type · As Of）
- [N1] MarkWide, Home Energy Monitor Market 2026–2036（$1.8B/14.6%）. secondary-industry · 2026[u]. https://markwideresearch.com/home-energy-monitor-market
- [N2] BusinessResearchInsights, Home Energy Monitor Market（$0.3B 2026）. secondary-industry · 2026-06. https://www.businessresearchinsights.com/market-reports/home-energy-monitor-market-105462
- [N3] Valuates/QYResearch, Global Home Energy Monitor（$265M 2025，Top5>39%）. secondary-industry · 2026[u]. https://reports.valuates.com/market-reports/QYRE-Auto-9A9238/global-home-energy-monitor
- [N4] EnergyMeterHub, Emporia Vue 3 vs Shelly EM vs Schneider. other · 2026[u]. https://www.energymeterhub.com/articles/best-whole-home-energy-monitor-emporia-vue-3-vs-shelly-em-vs-schneider
- [N5] Enphase, Q1 2026 Financial Results（$282.9M）. official · 2026-04. https://investor.enphase.com/news-releases/news-release-details/enphase-energy-reports-financial-results-first-quarter-2026
- [N6] PV Tech, Enphase Q1 2026 / 25D 到期影响. journalism · 2026-04. https://www.pv-tech.org/lower-residential-demand-after-25d-tax-credit-ends-impacts-enphases-q1-2026-revenue/
- [N7] AgentSolar, Most Popular Solar Batteries 2026（Tesla 63.3% / Enphase 17.1%）. other · 2026[u]. https://agentsolar.ai/solar-batteries
- [N8] The Energy Brief, Best Home Battery Storage 2026. other · 2026[u]. https://theenergybrief.net/article/best-home-battery-storage-for-2026-tesla-enphase-and-beyond
- [N9] Emporia Vue Local, ESPHome 本地控制指南. community · 2026-01. https://emporia-vue-local.github.io/docs/tutorial/intro/
- [N10] GitHub, emporia-vue-local/esphome（~755 stars）. community · 2026-01. https://github.com/emporia-vue-local/esphome
- [N11] MarketIntelo, NILM for Utilities Market（Itron/Landis+Gyr 领跑；Sense/Bidgely/Verdigris 专业方）. secondary-industry · 2025[u]. https://marketintelo.com/report/non-intrusive-load-monitoring-for-utilities-market
- [N12] ResearchAndMarkets/Businesswire, North America Smart Metering 2025（Itron 35% / L+G 32% 装机）. secondary-industry · 2025-07. https://www.businesswire.com/news/home/20250731000744/en/
- [N13] DataIntelo, Residential Single-Phase Smart Meter（Landis+Gyr ~$1.8B/>2.4 亿只；Itron ~$2.4B）. secondary-industry · 2026[u]. https://dataintelo.com/report/global-residential-single-phase-electricity-smart-meter-market
- [N14] LocalSmartHomeGuide, Shelly Pro 3EM 本地 API/HA 集成. other · 2025-2026[u]. https://localsmarthomeguide.com/products/shelly-pro-3em/
- [N15] Shelly, Pro 3EM 官方文档（本地 RPC/MQTT，60 天板载数据）. official · 2026[u]. https://automations.shelly.com/blogs/documentation/shelly-pro-3em
- [N16] SmartWattFlow, Home Assistant Energy Monitoring Guide 2026. other · 2026[u]. https://smartwattflow.com/blog/home-assistant-energy-monitoring-guide
- 承接源（家居分册 seed）：[16] Sense 用电指纹→云 ML(GDPR) https://sense.com/gdpr/ ；[17] 智能电表 NILM 再识别(学术) https://dbis.ipd.kit.edu/download/Buchmann2013_Article_Re-identificationOfSmartMeterD.pdf ；[15] Enphase IQ Gateway 持续上报(policy) https://enphase.com/en-eu/legal/privacy-policy ；[22] Emporia Vue→ESPHome 本地化 https://emporia-vue-local.github.io/docs/tutorial/intro 。完整见发现笔记 [energy-monitors.notes/task-01.md](/Users/pengpeng/seo/directions/iot/research/02-hardware/energy-monitors.notes/task-01.md)。
