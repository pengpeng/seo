# 个人健康系统 / 平台竞品与关键词（IoT 方向 · 品类 02）

> 研究日期: 2026-07-04 | 来源: task-01（15 源）+ 家居分册 seed（task-04 + registry）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 个人健康"系统/平台"（聚合与呈现健康数据的软件层，非单个手环硬件；手环/手表/环见品类 09 wearables）。归属 IoT 新方向"系统章"。发现笔记见 [health-platforms.notes/](/Users/pengpeng/seo/directions/iot/research/01-systems/health-platforms.notes)。

## 摘要
个人健康平台是三大 OS 级聚合层（Apple HealthKit、Google Health Connect/Google Health app、Samsung Health）+ 一个跨设备运动社交冠军（Strava，180M 注册）+ 一批 VC 高估值新星（Whoop $10.1B、Function Health $2.5B、Superpower、Ultrahuman）的格局。核心结构性事实：**大厂把健康数据锁进 OS 聚合层**（HealthKit 2014 起中心化，longitudinal 锁定最强），而消费级**跨平台统一标准缺位**（FHIR 主要在临床侧）。这给"坐在 HealthKit/Health Connect 之上的中立聚合层"留下产品空间——恰是 Olares 个人 Agent + 数据主权叙事的落点。隐私侧最敏感的是健康数据的 B2B2C 货币化（保险/雇主 opt-in 共享）与 Fitbit→Google Health 的数据主权迁移。自托管冠军 Fasten OnPrem（FHIR PHR）与 Nightscout（T1D CGM）存在，但覆盖有限。

## 1. 品类概述
"个人健康系统"指聚合心率、睡眠、运动、经期、血糖、血压、体重、biomarker 的软件平台，向用户与第三方 App 提供统一读写。它区别于手环硬件：谁做聚合层，谁就掌握 longitudinal 健康画像。2026 年全球约 553M 活跃可穿戴设备为这些平台供数据 [N1]。隐私视角下这是**最私密数据类别**（生物特征 + 医疗 PHI），受 HIPAA/GDPR 约束但云生态、保险报销、研究去标识化带来新流向。

## 2. 市场领导者 / top 平台
| 平台 | 母公司 | 规模锚点 | 口径 |
|------|--------|----------|------|
| Apple Health / HealthKit | Apple | 无官方 MAU；Apple 占全球 smartwatch 出货 ~28–32%[u]；数万 App 接入 [N1][N14][N15] | 生态/出货估 |
| Samsung Health | Samsung | Google Play 2.2B+ 安装；MAU 估 23.3M[u]（另有报告 95M[u]） [N5] | 安装/估算 |
| Google Health app（原 Fitbit）+ Health Connect | Alphabet | Fitbit 2021 $2.1B 收购；2026-05 rebrand，~40M 活跃迁移 [N6][N7] | 活跃用户 |
| Garmin Connect | Garmin | 活跃用户估 ~45M（区间 42–49M）[N4] | 第三方估 |
| Strava | 独立 | 180M 注册、2025 收入 $415M、估值 $2.2B [N2][N3] | 注册用户 |

> Huawei Health / Zepp / Withings Health Mate 为硬件配套 app，无可靠全球 MAU（Gap）。

**置信度: Medium**（Apple/Samsung 无官方 MAU，多为第三方估且互相冲突）。

## 3. 细分赛道冠军
- **iOS 聚合冠军**：Apple HealthKit（2014 起中心化存储，锁定效应最强）[N1][N15]。
- **Android 聚合冠军**：Google Health Connect（系统 API）+ Google Health app（消费端 UI，2026-05 由 Fitbit app 升级）[N7]。
- **Samsung 生态冠军**：Samsung Health（Galaxy 默认入口）[N5]。
- **运动社交/训练聚合冠军**：Strava（跨 Garmin/Apple Watch/COROS/Whoop/Oura 写入）[N2][N3]。
- **耐力运动硬件平台冠军**：Garmin Connect [N4]。
- **开源自托管 PHR 冠军**：Fasten OnPrem（FHIR PHR 可视化）+ Nightscout（T1D CGM 社区标准）；新兴 OwnChart/Nocturne [N12]。
- **血检/长寿聚合新兴冠军**：Function Health（$2.5B）与 Superpower 争夺 biomarker + wearable 聚合叙事 [N8][N10]。

**置信度: High**（分层冠军有多源共识）。

## 4. VC 圈明日之星
- **Whoop**：2026-03 Series G $575M @ **$10.1B**，累计 ~$900M，2.5M+ members，2025 bookings run rate $1.1B；向"personal health platform"扩张（Advanced Labs 血检）[N9]。
- **Function Health**：2025-11 Series B $298M @ **$2.5B**，累计 $350M，50M+ lab tests，160+ 检测项，强调 device-agnostic + AI 解读、不卖数据 [N8]。
- **Superpower**：2025-04 Series A $30M，估值 >$300M[u]，100+ biomarkers，$499/年 [N10]。
- **Ultrahuman**：2026-03 Series C ~$48M[u]，累计 ~$149M[u]，2025 营收 ~$64M[u]；Ring + CGM + Blood Vision [N11]。
- **Levels**：2022-04 Series A $38M @ $300M，CGM 代谢健康；2024–2026 未见新轮（Gap）[N13]。

**置信度: Medium**（Whoop/Function 事件可靠，Superpower/Ultrahuman 估值多 [u]）。

## 5. 候选产品关键词
平台替代：`apple health alternative`、`google fit alternative`、`samsung health alternative`、`health connect alternative`、`garmin connect alternative`、`strava alternative`、`fasten health alternative`。
自托管/开源：`self hosted health dashboard`、`open source health tracker`、`personal health record self hosted`、`nightscout self hosted`。
数据导出（高意图技术词）：`export apple health data`、`apple healthkit export xml`。
聚合/垂直：`unified health dashboard app`、`wearable data aggregation app`、`best health data app`、`metabolic health app`、`longevity blood test app`。

> 精确 Semrush 量留后续 brand-seo-research。数据导出词买家意图强、竞争低，适合先切入。

## 6. 隐私风险 + Olares 自托管平替
- **风险共性**：健康/生物特征 B2B2C 货币化——Oura 经保险/雇主捆绑、Fitbit/Google Health Enterprise 允许 opt-in 下雇主/保险获取、Withings RPM 面向医疗机构 [seed task-04]。Fitbit 账户迁 Google，Google 成 data controller [seed task-04]。
- **Olares 平替栈**：手环去云用 Gadgetbridge（BLE→本地 SQLite，不支持 Apple Watch）；CGM 用 Nightscout（自托管血糖曲线，配 xDrip+/Loop）；医疗记录用 Fasten OnPrem（本地 FHIR PHR）；运动轨迹用 Traccar/OpenTracks；聚合与 Agent 层跑在 Olares 上，数据不出设备 [seed task-04]。
- **诚实差距**：无等价开源智能环/CGM 传感器/血压完全本地栈；Gadgetbridge↔HA 官方路径不成熟；Fasten 已停直连 EHR（仅手动归档）[N12][seed Gaps]。

**置信度: High**（平替存在但差距明确，社区共识）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：Garmin Connect 用户规模——官方/LinkedIn 长期写"35M+"，第三方模型估 45M[N4]；Samsung Health MAU 23.3M vs 95M[u]。平台方无披露动机，写内容须用"估算"措辞。

**反方解释**：大厂健康平台的临床级集成（Apple Health Records、Samsung/Google 与医院对接）与合规投入远超自托管；对普通用户，自托管健康栈运维门槛高、覆盖不全，属隐私优先者的选择而非主流替代 [N1][N12]。

**参考文献**（Source-Type · As Of）
- [N1] Cora Health, State of Fitness Tracking 2026. secondary-industry · 2026-04. https://www.corahealth.app/state-of-fitness-tracking-2026
- [N2] Business of Apps, Strava Statistics 2026. secondary-industry · 2026-01. https://www.businessofapps.com/data/strava-statistics/
- [N3] Strava Press, Year in Sport 2025. official · 2025-12. https://press.strava.com/articles/strava-releases-12th-annual-year-in-sport-trend-report-2025
- [N4] the5krunner, Garmin Connect Users 2026. secondary-industry · 2026-05. https://the5krunner.com/2026/05/01/garmin-connect-users-2026/
- [N5] AppGoblin, Samsung Health analytics. other · 2026-06. https://appgoblin.info/apps/com.sec.android.app.shealth
- [N6] The Meridiem, Fitbit Brand Retires. journalism · 2026-05. https://themeridiem.com/consumer-tech/2026/5/7/fitbit-brand-retires-as-google-health-app-signals-platform-play
- [N7] Google Blog, Introducing the Google Health app. official · 2026-05. https://blog.google/products-and-platforms/products/google-health/google-health-app/
- [N8] HLTH, Function Health $298M Series B. journalism · 2025-11. https://hlth.com/insights/news/function-health-raises-298m-series-b-at-2-5b-valuation-2025-11-25
- [N9] TechCrunch, Whoop $10B valuation. journalism · 2026-03. https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/
- [N10] Forbes, Superpower Raises $30M. journalism · 2025-04. https://www.forbes.com/sites/dariashunina/2025/04/22/superpower-raises-30m-to-launch-worlds-first-health-super-app/
- [N11] YourStory, Ultrahuman Series C. journalism · 2026-03. https://yourstory.com/2026/03/ultrahuman-closes-rs-400-cr-series-c-round
- [N12] GitHub, fastenhealth/fasten-onprem. community · 2026-07. https://github.com/fastenhealth/fasten-onprem
- [N13] Levels, $38M Series A. official · 2022-04. https://www.levels.com/blog/levels-38m-series-a-driven-by-member-and-community-alignment-to-solve-metabolic-health-crisis
- [N14] Runify, Apple Watch Running Statistics 2026. other · 2026-01. https://www.runifyapp.com/blog/apple-watch-running-statistics
- [N15] Apple Newsroom, empowering people with health information. official · 2022-07. https://www.apple.com/newsroom/2022/07/how-apple-is-empowering-people-with-their-health-information/