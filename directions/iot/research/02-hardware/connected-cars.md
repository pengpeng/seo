# 网联车 / 车机竞品与关键词（IoT 方向 · 品类 20）

> 研究日期: 2026-07-04 | 来源: task-01（10 源，WebSearch + WebFetch）+ 原家居分册 seed 笔记（网联车 rows）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 网联车 / 车机（connected cars & telematics）：OEM 车联网（Tesla / OnStar / FordPass / T-Connect 等）、车载 telematics 单元与后装 OBD-II 追踪器（Bouncie / Vyncs）。舱内摄像头/哨兵 dashcam 归本品类隐私要点；家用摄像头见品类 05 cameras。归属 IoT 新方向"硬件章"。发现笔记见 [connected-cars.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/connected-cars.notes)。

## 摘要
网联车是整个 IoT 方向里**隐私最差、Olares 平替最弱**的品类——Mozilla *Privacy Not Included* 直接把汽车评为"有史以来最差的产品品类"，25 个主流品牌全部不及格、84% 会共享(share)、76% 声称可出售(sell)个人数据 [N1]。执法/丑闻密度极高：Tesla 员工 2019–2022 在内部 Mattermost 私聊传阅客户舱内/哨兵(Sentry)摄像头视频（含"亲密场景"、车库、撞到骑车儿童的事故片段），且可看到录制地点定位 [N2]；GM OnStar Smart Driver 把加速/急刹/里程等驾驶行为(driving behavior)卖给 LexisNexis / Verisk，被 NYT 曝光后有车主保费上涨 21%，GM 于 2024-03-20 停止共享、2024-04-24 全线关停该项目 [N3][N4][N5]；Toyota / Lexus 因云配置错误使 215 万辆车的 VIN/位置/行车记录仪视频公网可访问近十年 [N6]。市场层面这是软件定义汽车(software-defined vehicle)与订阅化的大厂博弈：连网车市场 2025 约 $63.4B、2030 约 $131.9B（15.76% CAGR）[N8]，汽车 telematics 2025 约 $49.6B [N7]，GM OnStar 递延收入达 $5.4B（同比 +65%）、订阅数破 1200 万 [N7]。**Olares 落点（诚实）：无完整开源平替。** 只能做局部对冲——关闭/物理遮挡舱内摄像头、用本地存卡的 dashcam（不上云）、后装追踪/车队用 **Traccar**（Apache-2.0）自托管替代 OEM/后装云。**成熟度: Low（本品类是低 Olares-fit 赛道，如实标注）。**

## 1. 品类概述
网联车按数据链路分三层：① **OEM 嵌入式车联网**——Tesla、GM OnStar、Ford(FordPass/Ford Connected)、Toyota/Lexus(T-Connect/G-Link)、Hyundai/Kia(Bluelink/Kia Connect)、VW(Car-Net/We Connect)，出厂即带蜂窝模块，做远程控制、OTA、eCall、导航、UBI(usage-based insurance)数据；② **车载摄像头**——舱内(cabin)驾驶员监控 + 外向 dashcam/哨兵，视频默认可回传 OEM 云；③ **后装 telematics**——OBD-II 插入式追踪器(Bouncie / Vyncs / Spytec / MOTOsafety)与车队方案(Geotab/Samsara，归 commerce)。共性：位置(location)、行车行为、有时含舱内音视频与生物特征，长期存 OEM/broker 云，用户几乎无删除权（Mozilla 称仅 Renault/Dacia 提供全量删除，且不在北美销售）[N1]。这是本方向暴露面最广、监管救济最弱的一类——**软件与数据服务侧属 commerce 方向；OSS 仅出现在"平替"列**。

## 2. 市场领导者 / top 畅销
| 层 | 领导者 | 锚点 |
|------|--------|------|
| OEM 车联网（美/全球口径） | Tesla / GM OnStar / Ford | Mozilla 25 品牌全不及格；Tesla、Nissan 垫底 [N1][N2] |
| OEM 订阅财务锚 | GM OnStar | 递延收入 $5.4B（+65% YoY）、~1200 万订阅；2025 车型起 OnStar Basics 标配 8 年 [N7] |
| 日系/欧系代表 | Toyota/Lexus(T-Connect/G-Link)、Hyundai/Kia(Bluelink)、VW(Car-Net) | Toyota 215 万辆数据泄露 10 年 [N6] |
| 后装 OBD 追踪 | Bouncie / Vyncs | Bouncie $90 设备 + $9/月、15s 更新、碰撞检测；Vyncs 年费制、200+ 国 [N9] |
| 车队/商用 telematics | Geotab / Samsara / Verizon Connect（commerce） | Geotab 可复用 70% 卡车已装 OnStar 设备 [N9] |

母公司/上市锚：Tesla(NASDAQ:TSLA)、GM(NYSE:GM)、Ford(NYSE:F)、Toyota(7203.T/NYSE:TM)、Hyundai(005380.KS)、VW(VOW3.DE)。市场规模：连网车 2025 ~$63.44B → 2030 ~$131.87B（15.76% CAGR，亚太最大）[N8]；汽车 telematics 2025 ~$49.61B（12.4% CAGR）[N7]。

**置信度: Medium**（Mozilla 评级、GM 订阅财务、市场规模区间可靠；各家精确市占 % 因口径而异，市场规模不同机构 $10B–$100B 差异大[u]）。

## 3. 细分赛道冠军
- **OEM 订阅规模冠军**：**GM OnStar**（~1200 万订阅、$5.4B 递延收入），是把车联网做成经常性收入的样板 [N7]。
- **OTA / 软件定义汽车叙事冠军**：**Tesla**——车队级 OTA 与舱内外摄像头一体化，但也是隐私争议中心 [N2]。
- **后装个人/小车队追踪冠军**：**Bouncie**（15s 实时更新、碰撞检测、Alexa/Google 集成、无合约，$9/月）[N9]。
- **后装年费/多国冠军**：**Vyncs**（年费制无月付、200+ 国、OBD 诊断细，Basic 默认 60s）[N9]。
- **自托管定位/车队冠军（唯一真开源落点）**：**Traccar**（Apache-2.0，200+ 协议/设备，自托管 GPS 平台，可替代 OEM/后装云做车辆/车队自管）[N10]。

**置信度: High**（分层冠军有评测/财报/社区共识；仅 Traccar 属真正开源自托管，其余均为闭源云服务）。

## 4. VC 圈明日之星
网联车硬件由大厂主导，"新星"集中在数据/软件与保险科技侧（多属 commerce，非硬件）：
- **UBI / 驾驶数据经纪**：LexisNexis Risk Solutions、Verisk——把 OEM 驾驶行为转成保险风险分的中间层，正是 GM 事件主角，监管与诉讼风险上升 [N3][N4]。
- **车队 SaaS**：Geotab、Samsara(NYSE:IOT)、Motive——telematics 平台化，向 AI 摄像头/安全评分延伸（commerce）[N9]。
- **软件定义汽车 / OTA 中间件**：连网车市场向 5G/V2X、订阅化迁移，Bosch/Continental/Harman/Qualcomm/Airbiquity 等 Tier-1 争 OTA 与数据平台份额 [N8]。
- **开源对照**：几乎无消费级"车机自托管"新星；**Traccar** 是定位侧唯一事实开源标准，与 OEM 云形成"闭源车云 vs 开源自管"极不对称的双轨 [N10]。

**置信度: Medium**（赛道方向可靠；具体估值/融资多为二手口径，且主体在软件/保险侧而非车机硬件[u]）。

## 5. 候选产品关键词
品牌替代：`onstar alternative`、`bouncie alternative`、`vyncs alternative`、`tesla dashcam alternative`。
隐私/去云（核心机会）：`car privacy`、`is my car spying on me`、`connected car privacy`、`how to stop car sharing data`、`disable onstar smart driver`、`opt out lexisnexis driving data`、`self hosted gps tracker`、`traccar`、`self hosted fleet tracking`、`local dashcam no cloud`、`disable in car camera`、`cover tesla cabin camera`。
选购/对比：`bouncie vs vyncs`、`best obd gps tracker`、`best gps tracker for car no subscription`、`cars worst privacy`、`which cars sell your data`。

> 与现有资产最贴合的是 `self hosted gps tracker` / `traccar` / `car privacy`（Olares Market 若有 Traccar 报告可直接承接）。多数关键词是"揭露 + 局部对冲"意图而非"完整平替"，转化路径弱于 cameras 品类。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **舱内/哨兵视频被内部滥用**：Tesla 员工 2019–2022 在内部 Mattermost 传阅客户车摄像头视频（含亲密场景、车库、撞到骑车儿童的事故），7 名前员工称工具可显示录制地点定位——与其"录像匿名、不关联车辆"的隐私声明冲突 [N2]。
- **驾驶行为→保险歧视**：GM OnStar Smart Driver 把加速/急刹/里程卖给 LexisNexis/Verisk，车主 Kenn Dahl 保费涨 21%，LexisNexis 消费者披露报告含 640 次行程明细；GM 2024-03-20 停止共享、2024-04-24 关停项目并解约两家 broker [N3][N4][N5]。
- **OEM 云配置错误大规模泄露**：Toyota/Lexus 因数据库误设为 public，215 万辆车 VIN/位置/行车记录仪视频公网可访问近十年(2013–2023) [N6]。
- **系统性最差隐私**：Mozilla 25 品牌全不及格、84% 共享、76% 可出售、56% 应"请求"即向执法/政府交数据；仅 Renault/Dacia 提供删除权（不在北美卖）[N1]。
- **后装追踪器**：Bouncie/Vyncs 等 OBD 追踪本身把实时位置/行程上传厂商云——便利与隐私同源 [N9]。
- **Olares 平替栈（诚实差距：无完整平替）**：
  - **OEM 车联网无自托管替代**——只能在 App/账户里关驾驶评分(disable Smart Driver / UBI)、拒绝数据共享、必要时断蜂窝模块（多数车不可行）。
  - **舱内摄像头**：关闭/物理遮挡(cover cabin camera)，避免哨兵上云。
  - **行车记录**：改用**本地存卡、无云的 dashcam**（不接 OEM/厂商云）。
  - **定位/车队**：**Traccar** on Olares（Apache-2.0，200+ 协议）+ 自选 OBD/GPS 硬件，替代 Bouncie/Vyncs/OEM 车联网云，做车辆/车队自管，数据不出自有服务器 [N10]。
  - 编排：可接 Home Assistant on Olares 做告警/geofence。

**置信度: High（"问题诊断 + 局部对冲"可靠）· Low（无完整开源车机/车联网平替，见第 7 节）。**

## 7. 核心争议 / 反方 / 参考

**核心争议**：网联车**没有完整的开源自托管平替**——OEM 车联网深度耦合车辆硬件与蜂窝，用户无法自托管车云；能自托管的只有"定位/车队"这一薄层(Traccar) 与"本地 dashcam"，其余只能靠关功能、拒共享、物理遮挡。因此本品类是 IoT 方向里 **Olares-fit 最低**、成熟度应如实标 **Low** 的赛道 [N1][N10]。市场规模口径分歧大（telematics ~$10B vs 连网车 ~$63B–$100B），引用时须注明范围[u]。

**反方解释**：车联网换来的是 OTA 安全更新、eCall/自动碰撞求救、被盗找回、远程解锁与导航——这些是真实的安全/便利价值，纯"断网车"会牺牲救援与召回响应。UBI/驾驶评分对安全驾驶者可降保费；GM 事件的核心问题是**知情同意(consent)缺失**而非功能本身。后装 Traccar 自管需要硬件、服务器与网络知识，属技术用户路径，且无法覆盖 OEM 已采集的原厂数据。

**参考文献**（Source-Type · As Of）
- [N1] Mozilla *Privacy Not Included: Cars Are the Worst Category. ngo · 2023-09. https://www.mozillafoundation.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/
- [N2] Tesla Workers Shared Sensitive Images Recorded by Customer Cars (Reuters). journalism · 2023-04. https://www.reuters.com/technology/tesla-workers-shared-sensitive-images-recorded-by-customer-cars-2023-04-06/
- [N3] Automakers Are Sharing Consumers' Driving Behavior With Insurance Companies (NYT). journalism · 2024-03. https://www.nytimes.com/2024/03/11/technology/carmakers-driver-tracking-insurance.html
- [N4] General Motors Quits Sharing Driving Behavior With Data Brokers (NYT). journalism · 2024-03. https://www.nytimes.com/2024/03/22/technology/gm-onstar-driver-data.html
- [N5] GM Axes OnStar Smart Driver After Privacy Complaints (Forbes). journalism · 2024-04. https://www.forbes.com/sites/antoniopequenoiv/2024/04/24/general-motors-axes-onstar-smart-driver-system-after-privacy-and-insurance-complaints/
- [N6] Toyota: Car Location Data of 2.15M Customers Exposed for 10 Years (BleepingComputer). journalism · 2023-05. https://www.bleepingcomputer.com/news/security/toyota-car-location-data-of-2-million-customers-exposed-for-ten-years/
- [N7] Automotive Telematics Market (Emergen Research; GM OnStar $5.4B 递延/12M 订阅). secondary-industry · 2025[u]. https://www.emergenresearch.com/industry-report/automotive-telematics-market
- [N8] Connected Car Market Size (Mordor Intelligence). secondary-industry · 2026-01[u]. https://www.mordorintelligence.com/industry-reports/connected-car-market
- [N9] Bouncie vs Vyncs OBD GPS Tracker (MotoTechGPS / Automoblog). other · 2026[u]. https://mototechgps.com/bouncie-vs-vyncs-2026-which-gps-tracker-should-you-buy/
- [N10] Traccar 自托管 GPS/车队追踪(Apache-2.0). community · 2026-06. https://www.traccar.org/
