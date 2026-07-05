---
task_id: 01
role: 网联车 / 车机市场分析师
status: complete
sources_found: 10
source: WebSearch + WebFetch（AS_OF 2026-07-04）+ 原家居分册 seed 笔记（网联车 rows）
---

## Sources
[N1] Mozilla PNI: Cars Are the Worst Category | https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/ | Source-Type: ngo | As Of: 2023-09 | Authority: 8/10
[N2] Tesla workers shared sensitive images from customer cars (Reuters) | https://www.reuters.com/technology/tesla-workers-shared-sensitive-images-recorded-by-customer-cars-2023-04-06/ | Source-Type: journalism | As Of: 2023-04 | Authority: 9/10
[N3] Automakers sharing driving behavior with insurers (NYT) | https://www.nytimes.com/2024/03/11/technology/carmakers-driver-tracking-insurance.html | Source-Type: journalism | As Of: 2024-03 | Authority: 9/10
[N4] GM quits sharing driving behavior with data brokers (NYT) | https://www.nytimes.com/2024/03/22/technology/gm-onstar-driver-data.html | Source-Type: journalism | As Of: 2024-03 | Authority: 9/10
[N5] GM axes OnStar Smart Driver after privacy complaints (Forbes) | https://www.forbes.com/sites/antoniopequenoiv/2024/04/24/general-motors-axes-onstar-smart-driver-system-after-privacy-and-insurance-complaints/ | Source-Type: journalism | As Of: 2024-04 | Authority: 7/10
[N6] Toyota 2.15M car location data exposed 10 years (BleepingComputer/Reuters) | https://www.bleepingcomputer.com/news/security/toyota-car-location-data-of-2-million-customers-exposed-for-ten-years/ | Source-Type: journalism | As Of: 2023-05 | Authority: 8/10
[N7] Automotive Telematics Market + GM OnStar 财务 (Emergen Research) | https://www.emergenresearch.com/industry-report/automotive-telematics-market | Source-Type: secondary-industry | As Of: 2025 [u] | Authority: 5/10
[N8] Connected Car Market Size (Mordor Intelligence) | https://www.mordorintelligence.com/industry-reports/connected-car-market | Source-Type: secondary-industry | As Of: 2026-01 [u] | Authority: 5/10
[N9] Bouncie vs Vyncs OBD GPS tracker (MotoTechGPS / Automoblog) | https://mototechgps.com/bouncie-vs-vyncs-2026-which-gps-tracker-should-you-buy/ | Source-Type: other | As Of: 2026 [u] | Authority: 5/10
[N10] Traccar self-hosted GPS/fleet tracking (Apache-2.0) | https://www.traccar.org/ | Source-Type: community | As Of: 2026-06 | Authority: 8/10

## Findings
- Mozilla 评汽车为史上最差隐私品类：25 品牌全不及格、84% 共享、76% 可出售、56% 应"请求"即向执法交数据；仅 Renault/Dacia 提供删除权（不在北美卖）。[N1]
- Tesla 员工 2019–2022 在内部 Mattermost 传阅客户舱内/哨兵视频（亲密场景、车库、撞骑车儿童事故），工具可显示录制地点定位，与"匿名不关联车辆"声明冲突。[N2]
- GM OnStar Smart Driver 把加速/急刹/里程卖给 LexisNexis/Verisk；车主 Dahl 保费涨 21%，披露报告含 640 次行程；GM 2024-03-20 停共享、2024-04-24 关停项目并解约两家。[N3][N4][N5]
- Toyota/Lexus 云误设 public，215 万辆 VIN/位置/行车记录仪视频公网可访问近十年(2013–2023)。[N6]
- 汽车 telematics 市场 2025 ~$49.61B（12.4% CAGR）；GM OnStar 递延收入 $5.4B（+65% YoY）、~1200 万订阅、2025 车型起 OnStar Basics 标配 8 年。[N7]
- 连网车市场 2025 ~$63.44B → 2030 ~$131.87B（15.76% CAGR，亚太最大）；软件定义汽车/订阅化/5G-V2X 驱动。[N8]
- 后装 OBD：Bouncie $90+$9/月、15s、碰撞检测、无合约；Vyncs 年费制、200+ 国、Basic 默认 60s；Geotab 车队可复用已装 OnStar 设备。[N9]
- Traccar（Apache-2.0，200+ 协议）是定位/车队唯一真开源自托管落点。[N10]

## Market Leaders
- OEM 车联网：Tesla / GM OnStar / Ford；日欧系 Toyota-Lexus(T-Connect/G-Link)、Hyundai/Kia(Bluelink)、VW(Car-Net)。[N1][N2][N6]
- OEM 订阅财务锚：GM OnStar（$5.4B 递延、~12M 订阅）。[N7]
- 后装追踪：Bouncie / Vyncs（个人+小车队）；车队 SaaS Geotab/Samsara/Verizon Connect（commerce）。[N9]
- 上市锚：TSLA / GM / F / TM(7203.T) / Hyundai(005380.KS) / VW(VOW3.DE)。
- 市场规模：连网车 ~$63.44B(2025)→$131.87B(2030)；telematics ~$49.61B(2025)。[N7][N8]

## Segment Champions
- OEM 订阅规模：GM OnStar。[N7]
- OTA/软件定义汽车叙事：Tesla（同时是隐私争议中心）。[N2]
- 后装个人/小车队：Bouncie（15s+碰撞检测+无合约）。[N9]
- 后装年费/多国：Vyncs（年费无月付、200+ 国）。[N9]
- 自托管定位/车队（唯一真开源）：Traccar。[N10]

## VC Rising Stars
- UBI/驾驶数据经纪：LexisNexis Risk Solutions、Verisk（GM 事件主角，监管/诉讼风险上升）。[N3][N4]
- 车队 SaaS：Geotab、Samsara(NYSE:IOT)、Motive（commerce）。[N9]
- 软件定义汽车/OTA 中间件：Bosch/Continental/Harman/Qualcomm/Airbiquity 争数据平台。[N8]
- 开源对照：Traccar 是定位侧唯一事实开源标准，与 OEM 车云极不对称双轨。[N10]

## Candidate Keywords
onstar alternative / bouncie alternative / vyncs alternative / tesla dashcam alternative / car privacy / is my car spying on me / connected car privacy / how to stop car sharing data / disable onstar smart driver / opt out lexisnexis driving data / self hosted gps tracker / traccar / self hosted fleet tracking / local dashcam no cloud / disable in car camera / cover tesla cabin camera / bouncie vs vyncs / best obd gps tracker / best gps tracker for car no subscription / cars worst privacy / which cars sell your data

## Deep Read Notes
### Source [N1]: Mozilla Privacy Not Included (cars)
Key data: 25/25 品牌全不及格；84% 共享、76% 可出售、56% 应请求向政府/执法交数据；Nissan/Tesla 垫底；仅 Renault/Dacia 可删除（非北美）。
Key insight: 这是本品类"隐私优先"叙事的最强锚——"cars worst privacy""which cars sell your data"是强意图揭露词。

### Source [N3][N4][N5]: GM OnStar → LexisNexis
Key data: 加速/急刹/里程卖给 LexisNexis/Verisk；Dahl 保费涨 21%、640 次行程披露；2024-03-20 停共享、2024-04-24 关停、解约两家、设首席信任与隐私官。
Key insight: 核心问题是知情同意缺失；"disable onstar smart driver""opt out lexisnexis"是可操作长尾。

### Source [N7]: Emergen Automotive Telematics
Key data: 2025 ~$49.61B、12.4% CAGR；GM OnStar 递延 $5.4B(+65% YoY)、~12M 订阅、2025 车型 OnStar Basics 标配 8 年。
Key insight: 车联网已是大厂经常性收入引擎，去数据化动机与商业模式直接冲突——平替空间小。

### Source [N10]: Traccar
Key data: Apache-2.0，200+ 协议/设备，自托管 GPS 平台。
Key insight: 网联车方向唯一真开源自托管落点，但只覆盖"定位/车队"薄层，无法替代 OEM 原厂数据链。

## Gaps
- OEM 车联网无任何完整开源自托管平替；只能关功能/拒共享/物理遮挡 + Traccar 定位自管——本品类 Olares-fit 低，成熟度 Low。
- 市场规模口径分歧大：telematics ~$10B(MarketsandMarkets) vs ~$49.6B(Emergen) vs 连网车 ~$63.4B(Mordor)/~$100.8B(TMR)——引用须注明范围[u]。
- 各 OEM 精确市占 % 缺免费权威来源；GM 订阅/递延为厂商口径。
- Hyundai/Kia Bluelink、VW Car-Net 的具体隐私事件未逐一深挖[u]。
- 后装追踪器财务/份额私营，多为评测口径[u]。
- 本地无云 dashcam 无单一开源事实标准（多为存卡硬件），未定"冠军"。

## END
