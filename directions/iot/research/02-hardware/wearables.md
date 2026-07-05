# 健康手环 / 可穿戴设备竞品与关键词（IoT 方向 · 品类 09）

> 研究日期: 2026-07-04 | 来源: task-01（13 源）+ 家居分册 seed（task-04 + registry）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 健康可穿戴硬件（手表/手环/环/CGM/血压秤）。健康软件平台见品类 02；AI 录音硬件见品类 08。归属 IoT 新方向"硬件章"。发现笔记见 [wearables.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/wearables.notes)。

## 摘要
健康可穿戴是大厂主导 + 高估值订阅新星并存的成熟品类。智能手表 Apple Watch 居首（Q1 2026 出货份额 23%），但按"wearable band"年度口径小米以 18% 反超苹果 [N1][N7]。运动 GPS 由 Garmin 稳守（FY2025 $7.25B、Fitness +33%）[N5]。真正的资本热点在两处：**智能环**（Oura 出货占 ~74%、估值 $11B、2026-05 机密 IPO）与**订阅恢复带**（Whoop 估值 $10.1B）[N2][N3][N4]。CGM 是 Abbott/Dexcom 双寡头（美国 48.5% vs 44.7%），血压/秤由 Omron（累计 >4 亿台）与 Withings（2025 盈利）领衔 [N8][N9][N13][N6]。**Olares 落点**：手环去云用 Gadgetbridge（BLE→本地 SQLite，不支持 Apple Watch），CGM 用 Nightscout 自托管，数据聚合与 Agent 层跑在 Olares；但无等价开源智能环/CGM 传感器/血压完全本地栈——差距需诚实标注。隐私上是最私密数据（生物特征），且向保险/雇主 B2B2C 货币化。

## 1. 品类概述
健康可穿戴含智能手表、性价比手环、健康环、运动 GPS 表、恢复订阅带、CGM、智能血压/秤。它是健康数据的采集端（软件平台见品类 02）。2025 全球 wearable band 出货 >2 亿台 [N7]，智能环 >400 万台 [N4]。隐私视角：24h 贴身生物特征 + 医疗数据，受 HIPAA/GDPR 约束但云同步、保险捆绑带来新流向。

## 2. 市场领导者 / top 畅销
| 子类 | 领导者 | 锚点 |
|------|--------|------|
| 智能手表（全球） | Apple Watch | Q1 2026 出货份额 23%（+21%）[N1] |
| wearable band（年度口径） | Xiaomi 18% > Apple 17% > Huawei 16% | Omdia 2025 [N7] |
| 运动 GPS | Garmin（NASDAQ:GRMN） | FY2025 $7.25B、Fitness $2.36B(+33%) [N5] |
| 智能环 | Oura | H1 2025 出货 ~74%、估值 $11B [N4][N2] |
| 恢复订阅 | Whoop | 估值 $10.1B、bookings $1.1B run rate [N3] |
| CGM | Abbott / Dexcom | 美国 48.5% / 44.7% [N8] |
| 血压/秤 | Omron / Withings | Omron >4 亿累计；Withings 2025 盈利 [N13][N6] |

> Samsung smartwatch 份额跌至 5%（-28%）；中国 Huawei 占本土 ~40% [N1]。

**置信度: Medium**（smartwatch vs wearable band 口径不同；智能环出货 vs 收入份额差异大 [u]）。

## 3. 细分赛道冠军
- **智能手表冠军**：Apple Watch（Q1 2026 23%）[N1]。
- **性价比手环冠军**：Xiaomi（2025 wearable band 18% 全球第一）[N7]。
- **运动 GPS 冠军**：Garmin（FY2025 Fitness $2.36B，强在 sport/outdoor）[N5]。
- **健康环冠军**：Oura（74% H1 2025，硬件 + $5.99/月；Dexcom 2024 战投 $75M）[N4][N2]。
- **恢复订阅冠军**：Whoop（screenless + 订阅，Abbott/Mayo 战投）[N3]。
- **CGM 冠军**：Abbott Libre（全球）+ Dexcom G7（美国 #2）；均推 OTC（Lingo/Stelo）[N8][N9]。
- **血压/秤冠军**：Omron（家用 BP 全球 #1）；Withings（clinical-grade 联网）[N13][N6]。

**置信度: High**（分层冠军有厂商财报与机构数据支撑）。

## 4. VC 圈明日之星
- **Oura**：2025-10 Series E $900M @ ~$11B（Fidelity）；累计 >$1.5B；2026-05 机密 IPO；2025 收入 ~$1B（2024 ~$500M）[N2]。
- **Whoop**：2026-03 Series G $575M @ $10.1B（Abbott/Mayo/QIA/Mubadala）；累计 ~$900M；前轮 2021 $3.6B [N3]。
- **Ultrahuman**：2026-03 Series C ~$48M（Rs 400 Cr），累计股权 >$60M；2025-09 ITC 裁 Oura 专利胜诉致 Ring Air 美国禁售 [N11]。
- **RingConn**：2024-08 Angel（未披露），H1 2025 份额 5%，卷入 Oura 专利案 [N4][u]。
- **Withings**：2019 以来 €61M，2025 首次全年盈利——health hardware 盈利标杆 [N6]。

**置信度: Medium**（Oura/Whoop 事件可靠，RingConn/部分数字 [u]）。

## 5. 候选产品关键词
品牌替代：`oura ring alternative`、`whoop alternative`、`fitbit alternative`、`garmin alternative`、`ultrahuman ring alternative`、`librelink alternative`、`withings scale alternative`。
对比：`amazfit vs garmin`、`xiaomi band vs fitbit`、`samsung galaxy ring vs oura`、`ringconn vs oura`、`dexcom g7 vs abbott libre`、`google fitbit air vs whoop`。
选购：`best fitness tracker`、`best health ring`、`omron blood pressure monitor wifi`。
自托管（核心机会）：`gadgetbridge`、`open source smartwatch`、`self hosted fitness tracker`、`nightscout cgm`。

> `gadgetbridge`、`nightscout cgm`、`self hosted fitness tracker` 与 Olares 数据主权叙事直接契合。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **风险共性（seed task-04）**：24h 贴身生物特征；健康/生物特征 B2B2C 货币化（Oura 经保险/雇主、Whoop Life ECG/血压、CGM regulated PHI）；智能眼镜第一视角监控（Ray-Ban Meta 默认存云 1 年）。
- **Olares 平替栈**：手环去云用 Gadgetbridge（BLE 直连小米/Amazfit/Garmin→本地 SQLite）；CGM 用 Nightscout（自托管血糖曲线，配 xDrip+/Loop）；运动轨迹用 OpenTracks/Endurain；聚合与 Agent 层跑在 Olares，数据不出设备 [seed task-04]。
- **诚实差距**：无等价开源智能环/CGM 传感器/血压完全本地栈；Gadgetbridge 不支持 Apple Watch；Nightscout 错误配置可致血糖数据公网可访问（需 API_SECRET/HTTPS）[seed task-04 Gaps]。

**置信度: High**（平替存在但差距明确，社区共识）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：谁是"可穿戴第一"取决于品类定义——smartwatch 口径 Apple 23%（Counterpoint），全体 wearable/band 口径小米反超（Omdia/IDC）；智能环 Oura 出货 74% vs 收入份额 28–32%[u]。内容须声明"出货 vs 收入 / smartwatch vs band"口径 [N1][N4][N7]。

**反方解释**：大厂可穿戴的临床级传感器、FDA 认证功能（ECG/血压/房颤）、生态整合与订阅服务，是自托管栈无法替代的；Gadgetbridge/Nightscout 属隐私优先者选择，运维门槛高、覆盖不全（尤其 Apple Watch/CGM/血压）[N2][seed]。

**参考文献**（Source-Type · As Of）
- [N1] 9to5Mac/Counterpoint, Apple Watch +21% Q1 2026. journalism · 2026-06. https://9to5mac.com/2026/06/18/apple-watch-shipments-surged-21-during-q1-2026-per-report/
- [N2] CNBC, Oura confidential IPO. journalism · 2026-05. https://www.cnbc.com/2026/05/21/oura-smart-ring-ipo-filing.html
- [N3] TechCrunch, Whoop $10B valuation. journalism · 2026-03. https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/
- [N4] Omdia, Smart Rings ecosystem. secondary-industry · 2025-11. https://omdia.tech.informa.com/blogs/2025/nov/empowering-the-health-and-fitness-ecosystem-with-smart-rings
- [N5] Garmin, FY2025 results. official · 2026-02. https://www8.garmin.com/aboutGarmin/invRelations/reports/2025_Q4_Earnings_Press_Release.pdf
- [N6] PR Newswire, Withings 2025 profitability. official · 2026-06. https://www.prnewswire.com/news-releases/the-buyback-pays-off-withings-confirms-full-year-profitability-for-2025...
- [N7] Business Wire, Omdia Xiaomi Reclaims Band Crown. secondary-industry · 2026-02. https://www.businesswire.com/news/home/20260227981313/en/
- [N8] Yahoo/GlobalData, Dexcom 2025 revenues $4.66bn. journalism · 2026-01. https://finance.yahoo.com/news/dexcom-reports-2025-revenues-4-171045525.html
- [N9] Mordor, CGM Market Share. secondary-industry · 2025-12. https://www.mordorintelligence.com/industry-reports/continuous-glucose-monitoring-market
- [N10] SAG, Global Smart Ring Q1 2026. secondary-industry · 2026-04. https://smartanalyticsglobal.com/mart-ring-market-q1-2026-oura-leadership-growth-outlook/
- [N11] YourStory, Ultrahuman Series C. journalism · 2026-03. https://yourstory.com/2026/03/ultrahuman-closes-rs-400-cr-series-c-round
- [N12] Google, Fitbit Air. official · 2026-05. https://blog.google/products-and-platforms/devices/fitbit/fitbit-air/
- [N13] OMRON, 400M BP Monitors Sold. official · 2025-09. https://healthcare.omron.com/news-media/press-release/omron-healthcare-exceeds-400m-blood-pressure-monitors-sold