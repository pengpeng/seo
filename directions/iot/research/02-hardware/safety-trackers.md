# 儿童 / 老人看护竞品与关键词（IoT 方向 · 品类 19）

> 研究日期: 2026-07-04 | 来源: task-01（15 源）+ 原家居分册 seed 笔记（[12][21]）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 人身安全追踪（personal safety tracker）：儿童 GPS 手表（kids GPS watch）、老人跌倒/医疗告警（elderly fall / medical alert）、通用物品/人员追踪器（item / person tracker）；含少量个人 GPS/OBD 资产追踪。家用摄像头见品类 05 cameras，网联车/车机见品类 20。归属 IoT 新方向"硬件章"。发现笔记见 [safety-trackers.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/safety-trackers.notes)。

## 摘要
人身安全追踪是 IoT 里"隐私诉求"与"救援刚需"最尖锐对撞的一类——买家（家长 / 子女）主动交出孩子/老人的**持续位置、语音、轨迹**以换取"随时可联系 + SOS 派警"。市场三分：① 儿童 GPS 手表高度碎片化，Garmin（Bounce）以约 12.4% 份额领先，VTech ~11.8%、Xplora（挪威）在北欧/德国强势并向美国扩张，另有 Verizon GizmoWatch、华为、TickTalk、AngelSense、Jiobit 等区域/细分玩家 [N1][N2]；上市锚点 Xplora 儿童表年销约 50 万只、订阅基数 47.6 万、ARR ~NOK 366M，并复制打法进军银发（Doro Aurora/Leva）[N3]。② 老人医疗告警是订阅型服务生意：Medical Guardian（最佳综合/最快响应）、Bay Alarm Medical（最佳性价比，$19.95/月起）、Life Alert（老牌但需 3 年合约、无自动跌倒检测）三分天下，跌倒检测普遍是 $5–15/月加购 [N5][N6][N7][N8]；Apple Watch 的免费内置跌倒检测（Fall Detection）是对专业告警系的降维打击[u]。③ 物品/人员追踪 Apple AirTag 以约 69% 份额统治 $1B+ smart-tag 市场，Samsung SmartTag 超越 Tile（Life360 子公司）居次 [N9][N10]。**隐私红线**：STALK 研究 6 款儿童表 4 款可被陌生人远程监听/定位/伪造轨迹，专业告警系天然收集持续位置 [N13][N14]。**Olares 落点**：定位 = Traccar（Apache-2.0，200+ 协议、2000+ 设备）自托管，配可控 tracker/手机客户端 [N11][N15]；跌倒 = HA + 60GHz mmWave（Seeed MR60FDA2 + ESPHome，$24.90）本地检测 [N12]。**诚实差距**：自托管方案无专业 24×7 派警坐席与 SOS 通话，开源跌倒检测仍以商业 SaaS 为主流、mmWave 非医疗器械。

## 1. 品类概述
本章按"看护对象 + 触发方式"聚合四类：① 儿童 GPS 手表（LTE + GPS，语音通话、SOS、地理围栏、家长 App，多数含月费 SIM）；② 老人医疗告警（PERS，in-home 基站 / mobile GPS pendant，24×7 监控坐席 + 可选自动跌倒检测）；③ 物品/人员追踪器（AirTag/Tile/SmartTag 为 BLE 众包定位无月费；Jiobit/AngelSense 为 LTE 实时定位有月费）；④ 个人 GPS/OBD 资产追踪（Bouncie/Vyncs 等，车辆定位）。共性：位置/语音/轨迹为最敏感数据类型，默认长期存厂商云；服务型（告警/家庭定位）比硬件更赚钱，行业整体向订阅收敛。

## 2. 市场领导者 / top 畅销
| 子品类 | 领导者 | 锚点 |
|------|--------|------|
| 儿童 GPS 手表（premium） | Garmin Bounce | 全球约 12.4% 份额，GPS 精度 + School Mode [N1][N2] |
| 儿童表（区域/上市锚） | Xplora（挪威）/ VTech | Xplora 北欧 ~9.8–11%、儿童表年销 ~50 万只、订阅 47.6 万、ARR ~NOK 366M；VTech ~11.8% [N1][N2][N3] |
| 儿童表（运营商/亚太） | Verizon GizmoWatch / Huawei | Verizon 北美 ~21%[u]、Huawei 亚太 ~9.7% [N1][N2] |
| 老人医疗告警 | Medical Guardian / Bay Alarm Medical / Life Alert | Medical Guardian 最佳综合+最快响应（~8s），Bay Alarm $19.95–27.95/月最佳性价比，Life Alert $49.95/月+3 年合约无自动跌倒 [N5][N6][N7][N8] |
| 消费级免费跌倒 | Apple Watch Fall Detection | 内置免费自动跌倒→紧急呼叫，冲击专业告警[u] |
| 物品/人员追踪（BLE） | Apple AirTag / Samsung SmartTag / Tile | AirTag 约 69% 份额领跑 $1B+ 市场，Samsung 超 Tile 居次，Tile 属 Life360 [N9][N10] |
| 实时人员追踪（LTE） | Jiobit（Life360）/ AngelSense | 面向儿童/特需/老人的月费实时定位 [N2] |

母公司/上市：Garmin（NYSE:GRMN）、Xplora（OSE:XPLRA，含 Doro 银发线）、Apple（AAPL）、Samsung、Life360（NASDAQ:LIF，持 Tile + Jiobit）；Medical Guardian / Bay Alarm Medical / AngelSense 私营[u]。

**置信度: Medium**（份额 % 多来自二手市场报告口径不一、部分厂商私营财务缺失；Xplora/上市玩家财务较可靠）。

## 3. 细分赛道冠军
- **儿童 GPS 手表冠军**：Garmin Bounce（GPS 精度 + School Mode + 无摄像头，主打户外家庭）[N1][N2]；Xplora（Goplay 运动激励 + GDPR 合规，欧洲最强）[N1][N3]；Verizon GizmoWatch（运营商渠道，北美）[N1]。
- **老人医疗告警冠军**：Medical Guardian（最快响应 ~8s、跌倒检测 20 测中 18，最佳综合）；Bay Alarm Medical（$19.95 起、免费配偶监护，最佳性价比）；MobileHelp/Lively（预算/GPS 便携）[N5][N6][N7]。
- **物品追踪冠军（无月费）**：Apple AirTag（Find My 众包网络，iOS 生态锁定）；Samsung SmartTag（Galaxy 生态）；Tile / Chipolo（跨平台）[N9][N10]。
- **实时人员追踪冠军（有月费）**：Jiobit（Life360，儿童/特需）、AngelSense（特需/老人，含双向通话）[N2]。
- **自托管定位软件栈冠军**：**Traccar**（Apache-2.0，200+ 协议 / 2000+ 设备，实时+围栏+告警）> Dawarich（偏个人轨迹历史，不支持硬件 GPS）；OsmAnd/Traccar Client 把手机变 tracker [N11][N15]。
- **自托管跌倒检测**：HA + Seeed MR60FDA2 60GHz mmWave（ESPHome 无代码接入，$24.90，非医疗器械）[N12]。

**置信度: High（分层冠军有评测/社区共识）· Low（自托管跌倒仍非成熟医疗级）**。

## 4. VC 圈明日之星
本章硬件多由大厂 + 老牌告警商主导，"新星"集中在服务化与生态：
- **订阅化家庭定位**：Life360（NASDAQ:LIF）收购 Tile + Jiobit，把"物品 + 人员 + 家庭"打包成订阅生态，是资本市场最热的整合叙事 [N10]。
- **儿童表服务化**：Xplora 明确"1 百万订阅"路线（订阅 +33% y/y、ARR ~NOK 366M），并把儿童表打法复制到银发（Doro Aurora/Leva + Doro Connect）[N3]。
- **消费级免费跌倒**：Apple Watch / Galaxy Watch 内置免费自动跌倒检测，正把"专业告警订阅"往下挤[u]。
- **开源双轨**：Traccar（自托管定位事实标准）+ HA mmWave 跌倒 vs 各厂商云 [N11][N12]。

**置信度: Medium**（Life360/Xplora 事件与财务可靠，"免费跌倒挤压订阅"为趋势判断[u]）。

## 5. 候选产品关键词
品牌替代：`life360 alternative`、`airtag alternative`、`tile alternative`、`jiobit alternative`、`angelsense alternative`、`medical guardian alternative`。
去云/自托管（核心机会）：`self hosted gps tracker`、`traccar`、`self hosted life360`、`self hosted location tracking`、`open source gps tracker`、`home assistant fall detection`、`mmwave fall detection`、`diy medical alert`、`gps tracker no subscription`、`gps tracker without monthly fee`。
选购/对比：`best kids gps watch`、`garmin bounce vs xplora`、`best medical alert system`、`medical guardian vs bay alarm`、`airtag vs tile`、`best gps tracker for elderly`、`kids smartwatch privacy`。

> Olares Market 已有 HA 报告、本方向已把 Traccar 列为定位平替，`self hosted gps tracker`、`traccar`、`home assistant fall detection`、`life360 alternative` 是与现有资产最贴合的切入。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **儿童表可被陌生人监听/定位**：STALK（学术，2020）测 6 款儿童 GPS 表，**4 款可被陌生人远程监听环境音、定位、伪造轨迹或截获通话**；CBS（2018）亦报道多款儿童表"易被黑" [N13][N14]。位置 + 语音 + 家长手机号一并暴露。
- **专业告警系天然持续采集位置**：mobile PERS / GPS pendant 为实现"任何地点派警"必须持续上报 GPS + 蜂窝定位到坐席后台，属长期存储的高敏数据 [N5][N7]。
- **物品追踪被滥用于跟踪**：AirTag/Tile 众包定位曾被用于 stalking，虽厂商加了反跟踪告警，但小体积 + 全球 Find My 网络本质上是"可被反向用于监控人"的工具 [N9][N10]。
- **家庭定位订阅生态数据集中**：Life360（含 Tile/Jiobit）把家庭成员实时位置 + 历史轨迹集中于单一厂商云，曾被曝出售位置数据的行业争议[u]。
- **Olares 平替栈**：定位 → **Traccar on Olares**（Apache-2.0，200+ 协议）+ 自选便宜 GPS tracker / 手机装 Traccar Client/OsmAnd，位置数据只进自己服务器，围栏/到离校告警本地触发；家庭定位 → Traccar 多用户 + HA 通知替代 Life360；跌倒 → **HA + Seeed MR60FDA2 60GHz mmWave**（ESPHome 无代码，$24.90）本地检测→HA 自动化推送/触发家人电话/本地警报，无视频、无云、无月费 [N11][N12][N15]；远程访问走 Tailscale/VPN 不暴露端口。

**置信度: High（自托管定位栈成熟）· Low（自托管跌倒无专业派警坐席、mmWave 非医疗认证）· 差距见第 7 节**。

## 7. 核心争议 / 反方 / 参考

**核心争议**：安全追踪的价值内核是"**别人替我盯着 + 出事有人来救**"——纯自托管能拿回位置数据主权，却**无法复制 24×7 专业监控坐席、SOS 双向通话与自动派警**。老人跌倒的 OSS 侧尤其薄弱：mmWave（MR60FDA2）可检测跌倒事件，但只是"安全监测补充非认证医疗器械"，误报/漏报与响应链都得自己搭，主流可靠方案仍是 Medical Guardian/Bay Alarm 这类商业 SaaS [N7][N12]。物品追踪的"全球 #1"归属亦有口径差异：AirTag 按购买份额 ~69% 领先，但其网络效应仅在 iPhone 生态内成立 [N9][N10]。

**反方解释**：对多数家长/子女而言，儿童表/告警系的"开箱即用 + 一键 SOS + 有人接警"体验，价值远高于"数据不出户"；专业告警系的持续定位正是救援前提，自托管牺牲了这条命脉。Traccar/HA mmWave 需要 VPS/服务器、ESPHome 烧录、网络与自动化知识，属技术用户路径；且 Apple Watch 免费内置跌倒 + 紧急呼叫，对普通用户比 DIY 更省心[u]。

**参考文献**（Source-Type · As Of）
- [N1] Verified Market Research: Top Kids' Smartwatch Brands（Garmin 12.4%/Xplora/VTech/Verizon）. secondary-industry · 2025-2026[u]. https://www.verifiedmarketresearch.com/blog/best-kids-smartwatch-brands/
- [N2] MarketIntelo: GPS Kids Watch Market（Garmin 12.4%/VTech 11.8%/Huawei 9.7%/Apple 8.5%/Samsung 7.2%/Xplora/Jiobit/AngelSense）. secondary-industry · 2025[u]. https://marketintelo.com/report/gps-kids-watch-market
- [N3] Xplora Q4 2025 Investor Presentation（Kids ~500k units/yr、订阅 476k、ARR ~NOK 366M、Doro Senior）. official · 2026-01. https://storage.mfn.se/0531801d-b8d2-4e6d-a3ae-eb430671012c/xplora-q4-2025-presentation.pdf
- [N4] Market Research Future: US Kids Smartwatch Market. secondary-industry · 2025[u]. https://www.marketresearchfuture.com/reports/us-kids-smartwatch-market-13699
- [N5] MedicalAlertReview: Best Medical Alert Systems 2026（定价/跌倒加购表）. other · 2026. https://medicalalertreview.com/best-medical-alert-systems
- [N6] NCOA: Best Medical Alert Systems 2026（Medical Guardian 最佳综合；75% 购买者因跌倒/急救）. secondary-industry · 2026. https://www.ncoa.org/product-resources/medical-alert-systems/best-medical-alert-systems/
- [N7] The Senior List: 7 Best Medical Alert Systems 2026（响应时间、跌倒检测实测）. other · 2026. https://www.theseniorlist.com/medical-alert-systems/best/
- [N8] Forbes Health: Best Medical Alert Systems（20 provider/70+ device 实测）. journalism · 2025. https://www.forbes.com/health/medical-alert-systems/best-medical-alert-systems/
- [N9] Parks Associates: Smart Tag Adoption 12%（Apple 69%、Samsung 超 Tile 居次）. official · 2025-03. https://www.prnewswire.com/news-releases/smart-tag-adoption-rises-to-12-in-us-internet-households-up-from-7-in-q3-2022-302396564.html
- [N10] AInvest: AirTag $1B+ 市场 69% 份额、Tile 请求国会审查. journalism · 2026[u]. https://www.ainvest.com/news/apple-airtag-update-strategic-move-billion-dollar-market-2601/
- [N11] Traccar GitHub（Apache-2.0、200+ 协议、2000+ 设备）. community · 2026-07. https://github.com/traccar/traccar
- [N12] Seeed MR60FDA2 60GHz mmWave 跌倒检测 + ESPHome/HA（$24.90）. community · 2025. https://wiki.seeedstudio.com/ha_with_mr60fda2/
- [N13] STALK：6 款儿童表 4 款可远程监听/定位（学术）. academic · 2020. https://www.hb.fh-muenster.de/opus4/frontdoor/deliver/index/docId/12354/file/Saatjohann_et_al-2020-STALK.pdf
- [N14] CBS：儿童 GPS 表易被黑（陌生人定位）. journalism · 2018. https://www.cbsnews.com/news/gps-watches-for-kids-are-easily-hacked/
- [N15] Dawarich vs Traccar（自托管定位对比）. community · 2026[u]. https://dawarich.app/docs/comparisons/vs-traccar/
