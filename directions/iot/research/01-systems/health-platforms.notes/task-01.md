---
task_id: 01
role: 个人健康数据平台分析师
status: complete
sources_found: 15
---

## Sources
[1] The State of Fitness Tracking in 2026 | https://www.corahealth.app/state-of-fitness-tracking-2026 | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 7/10
[2] Strava Revenue and Usage Statistics (2026) | https://www.businessofapps.com/data/strava-statistics/ | Source-Type: secondary-industry | As Of: 2026-01 | Authority: 6/10
[3] Strava 12th Annual Year in Sport Trend Report | https://press.strava.com/articles/strava-releases-12th-annual-year-in-sport-trend-report-2025 | Source-Type: official | As Of: 2025-12 | Authority: 8/10
[4] How Many Active Garmin Connect Users Are There in 2026? | https://the5krunner.com/2026/05/01/garmin-connect-users-2026/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 6/10
[5] Samsung Health Android Analytics | https://appgoblin.info/apps/com.sec.android.app.shealth | Source-Type: other | As Of: 2026-06 | Authority: 5/10
[6] Fitbit Brand Retires as Google Health App Signals Platform Play | https://themeridiem.com/consumer-tech/2026/5/7/fitbit-brand-retires-as-google-health-app-signals-platform-play | Source-Type: journalism | As Of: 2026-05 | Authority: 6/10
[7] Introducing the Google Health app | https://blog.google/products-and-platforms/products/google-health/google-health-app/ | Source-Type: official | As Of: 2026-05 | Authority: 9/10
[8] Function Health raises $298M Series B at $2.5B valuation | https://hlth.com/insights/news/function-health-raises-298m-series-b-at-2-5b-valuation-2025-11-25 | Source-Type: journalism | As Of: 2025-11 | Authority: 7/10
[9] Whoop's valuation just tripled to $10 billion | https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/ | Source-Type: journalism | As Of: 2026-03 | Authority: 9/10
[10] Superpower Raises $30 Million | https://www.forbes.com/sites/dariashunina/2025/04/22/superpower-raises-30m-to-launch-worlds-first-health-super-app/ | Source-Type: journalism | As Of: 2025-04 | Authority: 8/10
[11] Ultrahuman closes Rs 400 Cr Series C round | https://yourstory.com/2026/03/ultrahuman-closes-rs-400-cr-series-c-round | Source-Type: journalism | As Of: 2026-03 | Authority: 6/10
[12] fastenhealth/fasten-onprem | https://github.com/fastenhealth/fasten-onprem | Source-Type: community | As Of: 2026-07 | Authority: 7/10
[13] Levels $38M Series A | https://www.levels.com/blog/levels-38m-series-a-driven-by-member-and-community-alignment-to-solve-metabolic-health-crisis | Source-Type: official | As Of: 2022-04 | Authority: 8/10
[14] Apple Watch Running Statistics 2026 | https://www.runifyapp.com/blog/apple-watch-running-statistics | Source-Type: other | As Of: 2026-01 | Authority: 4/10
[15] How Apple is empowering people with their health information | https://www.apple.com/newsroom/2022/07/how-apple-is-empowering-people-with-their-health-information/ | Source-Type: official | As Of: 2022-07 | Authority: 9/10

## Findings
- Apple HealthKit 是 iOS 侧事实上的健康数据聚合层，Apple 未公布 Health app MAU，HealthKit 已有数万 App 接入。[15][1]
- 2026 年全球约 553M 活跃可穿戴装机基座。[1]
- Strava 2025 年底 180M 注册用户、$415M 收入、估值 $2.2B；Apple Watch 2025 成 Strava 最常用设备。[2][3]
- Garmin Connect 无官方披露，第三方估 2026-05 约 45M（区间 42–49M）。[4]
- Samsung Health Google Play 累计 2.2B+ 安装，第三方估 MAU ~23.3M；另有报告写 95M MAU，口径冲突。[5][u]
- 2026-05-19 Fitbit app 全面 rebrand 为 Google Health app，约 40M 活跃 Fitbit 用户迁移。[6][7]
- Function Health 2025-11 Series B $298M、估值 $2.5B，累计 $350M，device-agnostic 聚合 + AI 解读。[8]
- Whoop 2026-03 Series G $575M、估值 $10.1B，2.5M+ members，2025 bookings run rate $1.1B。[9]
- Superpower 2025-04 Series A $30M，估值 >$300M[u]，100+ biomarkers，$499/年。[10]
- Ultrahuman 2026-03 Series C ~$48M（~₹400Cr）[u]，累计 ~$149M[u]，2025 营收 ~$64M[u]。[11]
- Fasten OnPrem（~2.8K stars）已停直连 EHR，退化为 FHIR 存储/可视化。[12]
- Nightscout 仍是 CGM 社区自托管事实标准；新一代 Nocturne/OwnChart 出现。[12]

## Market Leaders
- Apple Health/HealthKit：无官方 MAU；Apple Watch 累计出货超 200M[u]；Counterpoint 估 Apple 占全球 smartwatch 出货 ~28–32%。[14][1]
- Samsung Health：Google Play 2.2B+ 安装；MAU 第三方估 23.3M[u] vs 报告 95M[u]。[5]
- Google Health app（原 Fitbit）+ Health Connect：Fitbit 2021 $2.1B 收购；2026-05 rebrand 后 ~40M 活跃。[6][7]
- Garmin Connect：Garmin Ltd.；活跃用户估 ~45M。[4]
- Strava：独立公司，2025 估值 $2.2B；180M 注册用户；2025 收入 $415M。[2][3]
- Huawei Health / Zepp / Withings Health Mate：硬件配套 app，无可靠全球 MAU。[Gap]

## Segment Champions
- iOS 聚合冠军：Apple HealthKit（2014 起中心化存储，锁定效应最强）。[1][15]
- Android 聚合冠军：Google Health Connect（API）+ Google Health app（消费端）。[7]
- Samsung 生态冠军：Samsung Health。[5]
- 运动社交/训练聚合冠军：Strava（180M 注册，跨设备写入）。[2][3]
- 耐力运动硬件平台冠军：Garmin Connect。[4]
- 开源自托管 PHR 冠军：Fasten OnPrem + Nightscout（T1D CGM）；新兴 OwnChart。[12]
- 血检/长寿聚合新兴冠军：Function Health（$2.5B）与 Superpower。[8][10]

## VC Rising Stars
- Function Health：2025-11 Series B $298M @ $2.5B，累计 $350M；160+ 检测项。[8]
- Whoop：2026-03 Series G $575M @ $10.1B，累计 ~$900M；2.5M+ members；2025 bookings $1.1B run rate。[9]
- Superpower：2025-04 Series A $30M，估值 >$300M[u]，$499/年。[10]
- Ultrahuman：2026-03 Series C ~$48M[u]，累计 ~$149M[u]；Ring + CGM + Blood Vision。[11]
- Levels：2022-04 Series A $38M @ $300M；2024–2026 未见新轮。[13][Gap]

## Candidate Keywords
apple health alternative / google fit alternative / samsung health alternative / health connect alternative / garmin connect alternative / strava alternative / self hosted health dashboard / open source health tracker / personal health record self hosted / nightscout self hosted / export apple health data / apple healthkit export xml / fasten health alternative / unified health dashboard app / wearable data aggregation app / best health data app / metabolic health app / longevity blood test app

## Deep Read Notes
### Source [1]: State of Fitness Tracking 2026
Key data: IDC 估 2023 全球 553M 活跃可穿戴；Apple Watch smartwatch 份额 ~28–32%；Health Connect 接入落后 HealthKit。
Key insight: "坐在 HealthKit/Health Connect 之上的第三方 app"是跨硬件中立合成层机会，与 Olares 个人 Agent/数据聚合叙事高度相关。

### Source [9]: Whoop $10B valuation
Key data: Series G $575M @ $10.1B；2.5M+ members；2025 bookings $1.1B run rate；Abbott 入资。
Key insight: 订阅+硬件模式下 bookings 比 MAU 更支撑估值；Whoop 向"personal health platform"扩张（血检 Advanced Labs）。

### Source [8]: Function Health $298M Series B
Key data: $298M @ $2.5B；累计 $350M；50M+ lab tests；对标 Superpower/Neko/InsideTracker。
Key insight: 竞争焦点是 device-agnostic 聚合 + AI 临床解读；强调 HIPAA、不卖数据。

## Gaps
- 未找到 Huawei Health/Zepp/Withings Health Mate/Gyroscope/Welltory 全球 MAU；Apple Health app MAU；Health Connect 独立 MAU。
- 数字冲突：Samsung Health MAU 23.3M vs 95M[u]；Apple Watch 90M DAU vs 170M+ active install[u]。
- 相反主张：Garmin Connect 官方长期写"35M+"vs 第三方模型 45M——"平台披露 vs 第三方估算"方法论。

## END
