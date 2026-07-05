# 传感器 / 网关竞品与关键词（IoT 方向 · 品类 13）

> 研究日期: 2026-07-04 | 来源: task-01（15 源，WebSearch+WebFetch）+ 原家居分册 seed 笔记（source [11] Matter / [22] SmartThings）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 智能家居传感器（门窗/PIR 人体/温湿度/水浸/烟雾/存在感应）与网关/中枢（Hub / Bridge / Border Router），及其底层协议层（Matter / Zigbee / Z-Wave / Thread）。灯/插座/温控/扫地机见品类 10-14；语音中枢见品类 03；摄像头见品类 05。归属 IoT 新方向"硬件章"。发现笔记见 [sensors-hubs.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/sensors-hubs.notes)。

## 摘要
传感器/网关是整个 IoT 方向里 **Olares 自托管平替最强、叙事最锋利的品类**——因为"Hub 是全屋数据的聚合点，几乎必然默认云同步"，而开源栈能把这个聚合点直接搬到本地。市场由三层玩家构成：① 平台级中枢——Samsung SmartThings（2025-12 已 430M 注册用户、390 partners、4,700 设备，CES 2026 宣布[N1][N2]）与 Aqara（多协议 Hub M2/M3/M100/M200，Zigbee+Thread+Matter+IR，绿米海外线）[N3][N4]；② 生态桥接器——Philips Hue Bridge（Signify，Zigbee 本地但 2023 起强制账号[N5][N6]）；③ 隐形 Thread Border Router——Amazon Echo(4th)/Echo Hub/eero、Apple HomePod mini/Apple TV 4K、Google Nest Hub(2nd)，普通家庭往往"已经拥有一个网关而不自知"[N7][N8]。协议层 Z-Wave 由 Alliance 推 800 系列 + Long Range（2026-01 CES 已 125 款 ZWLR 认证设备，Zooz 是主力 DIY 品牌）[N9][N10]。**Olares 落点极强**：Home Assistant 作**唯一 Hub**，Zigbee2MQTT（支持 5,473 款设备 / 577 厂商、15.1k stars、GPL[N11][N12]）+ SkyConnect/SLZB-06 网络协调器[N13]、ZHA、Z-Wave JS、Matter Server[N14]、以及把 Z2M 设备本地暴露成 Matter 的 Matterbridge[N15]，可完全去掉厂商云、让传感器时间序列不出局域网。

## 1. 品类概述
本品类分**传感层**（门窗磁 door/window、PIR/mmWave 人体存在 presence、温湿度 temp/humidity、水浸 leak、烟雾/CO smoke、光照/振动）与**网关层**（Hub 中枢、Bridge 桥接、Thread Border Router 边界路由）。协议上分四条：**Zigbee**（Aqara/Hue/IKEA 主力，mesh、需协调器）、**Z-Wave**（Sub-GHz、抗干扰、800 系列 + Long Range 直连[N9][N10]）、**Thread**（IPv6 mesh，Matter over Thread 的承载层，需 Border Router[N7]）、**Matter**（应用层互操作标准，over Wi-Fi 或 over Thread[N14]）。隐私视角下，单个传感器信息量看似很低，但**传感器融合 = 高精度行为画像**：门窗+PIR+温湿度时间序列可重建起床/离家/就寝/在家人数；而 **Hub 是全屋数据的单一聚合点**，一旦默认云同步，等于把整栋房子的时空事件流交给厂商——这正是自托管叙事的核心靶点。

## 2. 市场领导者 / top 畅销
| 层 | 领导者 | 锚点 |
|------|--------|------|
| 平台级中枢 | Samsung SmartThings | 2025-12 430M 注册用户、390 partners、4,700 设备；50 Matter 设备类型（Matter 1.4）[N1][N2] |
| 多协议 Hub（DIY 友好） | Aqara（绿米）Hub M2/M3/M100/M200 | M3 = Zigbee 3.0+Thread+Matter+IR，直连 64、桥接 127 设备，TBR[N3][N4] |
| 生态桥接器 | Philips Hue Bridge（Signify） | Zigbee 本地控制，但 2023 起强制 Hue 账号[N5][N6] |
| 隐形 Thread Border Router | Amazon Echo/Echo Hub/eero、Apple HomePod/TV、Google Nest Hub | "客厅里你不知道的 Thread 中枢"，随生态附赠[N7][N8] |
| 协议阵营（Z-Wave） | Z-Wave Alliance / Silicon Labs 800 + Zooz | 2026-01 已 125 款 ZWLR 认证设备，range 可达 1.5 mi[N9][N10] |

母公司/主体：Samsung（SmartThings，Aeotec 代工 Hub）、Aqara/Lumi 绿米、Signify（Philips Hue）、Amazon（Echo/eero）、Apple、Google、Silicon Labs（Z-Wave 芯片）、Zooz（The Smartest House）、IKEA（Dirigera）。

**置信度: Medium**（SmartThings 用户数官方可靠；但"注册用户"≠活跃安装量，且各家精确出货份额 % 无免费公开数据；隐形 TBR 属"能力"而非"销量"口径）。

## 3. 细分赛道冠军
- **平台级中枢冠军**：SmartThings（430M 用户 + Aeotec Smart Home Hub 2，Matter/Thread/Zigbee 三协议）——规模最大但重度云依赖[N1][N2]。
- **多协议本地 Hub 冠军**：Aqara Hub M3（Zigbee+Thread+Matter+IR+PoE，边缘自动化 + 本地 LAN 控制），绿米海外 M2/M100/M200 补全价位带[N3][N4]。
- **Zigbee 生态桥接冠军**：Philips Hue Bridge（Zigbee 本地 + 官方 API，社区可 ZHA/Z2M 直连灯珠绕开 Bridge）[N5]。
- **Z-Wave DIY 冠军**：Zooz（800 系列 + ZWLR 门窗/PIR/水浸传感器，SmartStart 配对），配 HomeSeer/Hubitat/Home Assistant[N9][N10]。
- **网络化 Zigbee 协调器冠军**：SMLIGHT SLZB-06（以太网/PoE，Z2M+ZHA+OTBR，可放最优信号位）与 Home Assistant SkyConnect/Connect ZBT-1、Sonoff Dongle-E[N13]。
- **自托管唯一 Hub 冠军（本品类最强 Olares 落点）**：**Home Assistant**——Zigbee2MQTT / ZHA / Z-Wave JS / Matter Server + Thread OTBR，把中枢彻底本地化[N11][N14]。

**置信度: High**（自托管分层冠军有强社区共识；商业侧领导者身份清晰）。

## 4. VC 圈明日之星
传感器/网关硬件本身不是 VC 热点（低毛利、协议标准化），叙事集中在**标准联盟推进**与**开源事实标准**：
- **Matter/Thread（CSA）**：SmartThings 已支持 50 个 Matter 设备类型（1.4），Thread 1.4 推跨生态凭据共享，把碎片化的多张 Thread 网合并[N2][N7]。
- **Z-Wave Long Range**：2026-01 CES 125 款 ZWLR 认证设备，从北美向 EMEA 扩，主打 MDU/大宅直连 star 拓扑[N9]。
- **Aqara "空间智能"**：IFA 2025 主打 presence/climate 多传感融合 + 边缘 Hub（M3 本地自动化、LAN 控制），从"卖传感器"转向"卖场景 AI"[N4]。
- **开源事实标准**：**Zigbee2MQTT**（5,473 设备/577 厂商、15.1k stars、GPL）[N11][N12] + **Matterbridge**（把 Z2M/Shelly 本地暴露成 Matter，接 Apple/Google/Alexa/SmartThings）[N15] 构成"闭源云中枢 vs 开源本地中枢"双轨。

**置信度: Medium**（联盟事件与开源数据可靠；"明日之星"在本品类更像标准演进而非独角兽融资）。

## 5. 候选产品关键词
品牌替代：`smartthings alternative`、`aqara alternative`、`hue bridge alternative`、`philips hue without account`、`samsung smartthings alternative`。
去云/本地（核心机会）：`local smart home hub`、`smart home hub without cloud`、`self hosted smart home`、`home assistant hub`、`zigbee2mqtt`、`zigbee coordinator`、`matter server home assistant`、`thread border router home assistant`、`z-wave js`、`local zigbee hub`。
选购/对比：`best zigbee hub`、`zigbee vs z-wave`、`zigbee vs thread`、`matter vs zigbee`、`best thread border router`、`skyconnect vs slzb-06`、`best presence sensor home assistant`、`aqara vs smartthings`、`best door sensor zigbee`。

> Olares Market 已有 Home Assistant 报告，`home assistant hub`、`zigbee2mqtt`、`local smart home hub`、`matter server home assistant` 是与现有资产最贴合的切入。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **Hub = 全屋数据聚合点**：中枢天然汇聚所有子设备的状态/事件流，多数平台（SmartThings、Aqara Home、Hue 云）默认把事件、自动化、有时含设备型号/在家状态上云——单一聚合点被攻破或被商业化，等于全屋时空画像外泄。
- **传感器融合 = 高精度行为画像（结构性风险）**：门窗 + PIR/presence + 温湿度的时间序列可高精度重建起床/离家/就寝/在家人数与旅行窗口；presence/mmWave 传感器精度已到"房间内是否有人、坐/站"级别，融合后是比单一摄像头更"无感"的长期监控。
- **强制账号 = 剥夺本地选择（Hue 教训，已核实）**：Signify 2023 起强制 Hue 账号才能用官方 App / 配 Matter，虽宣称本地控制仍可用、可防火墙断网，但"默认上云 + 隐私政策允许与 partner 共享"是行业通病[N5][N6]。
- **Thread 网碎片化 + 隐形 TBR**：普通用户的 Echo/HomePod/Nest Hub/eero 已是 Thread Border Router 却往往不自知，不同生态各建一张 Thread 网、凭据默认托管在各自厂商云[N7][N8]。
- **Olares 平替栈（本品类最强）**：**Home Assistant on Olares 作唯一 Hub**；Zigbee 传感器 → Zigbee2MQTT（+ SLZB-06/SkyConnect 网络协调器）或 ZHA，5,473 款设备本地接管[N11][N13]；Z-Wave → Z-Wave JS + Zooz 800/ZWLR USB 棒[N9]；Thread/Matter → HA Matter Server + 自建 OTBR，凭据留本地[N14]；已买的云网关 → Matterbridge 把设备本地暴露成 Matter，绕开厂商云[N15]；DIY 传感器 → ESPHome 自制门磁/温湿度/水浸，出网由防火墙阻断。

**置信度: High**（HA + Z2M/ZHA/Z-Wave JS/Matter Server 是全 IoT 方向里最成熟的自托管栈，社区共识强）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：Matter/Thread 是否真的"去中枢、更本地"——理论上 Matter over Thread 支持本地控制、多控制器共管，但实践中 commissioning 常需厂商 App/账号，Thread 凭据默认托管厂商云，跨生态凭据共享（Thread 1.4）刚起步，碎片化严重；"隐形 TBR" 让用户在不知情下把家接入某个云生态[N7][N8][N14]。另一争议：SmartThings "430M 注册用户"是累计注册还是活跃安装，口径不透明[N1]。

**反方解释**：厂商云中枢带来跨地远程、语音联动、OTA、"扫码即用"与稳定的推送，对非技术用户显著优于自托管；SmartThings/Aqara 生态成熟、设备兼容广、售后完整。Zigbee2MQTT/ZHA/Z-Wave JS 需要 USB 协调器或网络协调器、配对知识与一台常开主机（Olares 恰好补位），属技术用户路径；Matter Server/OTBR 的多控制器与 Thread 调试仍有门槛。

**参考文献**（Source-Type · As Of）
- [N1] SmartThings 430M Users (CES 2026, SamMobile). journalism · 2026-01. https://www.sammobile.com/news/smartthings-now-boasts-430-million-users-across-the-globe/
- [N2] Samsung SmartThings — Transforming Standards (CSA-IoT). official · 2025-10. https://csa-iot.org/wp-content/uploads/2025/10/samsung-smartthings-transforming-standards_into_everyday-experiences.pdf
- [N3] Aqara Hub M3 Product Page (multi-protocol / TBR / 127 devices). official · 2026[u]. https://us.aqara.com/products/hub-m3
- [N4] Aqara CES 2025 Lineup (Hub M100 / FP300 / Thread Border Routers). official · 2025-01. https://www.businesswire.com/news/home/20250106874900/en/CES-2025-Aqara-Showcases-Innovative-Smart-Home-Solutions-for-a-Seamless-Intuitive-Experience
- [N5] Philips Hue Account Mandatory (The Verge). journalism · 2023-09. https://www.theverge.com/2023/9/28/23892761/philips-hue-app-account-changes
- [N6] Hue Force Users Upload Data to Cloud (Home Assistant). community · 2023-09. https://www.home-assistant.io/blog/2023/09/22/philips-hue-force-users-upload-data-to-cloud/
- [N7] What is a Thread Border Router (Matter Alpha). other · 2025-2026[u]. https://www.matteralpha.com/explainer/thread-border-router
- [N8] Understand Smart Home Thread Support (Amazon Developer). official · 2026[u]. https://developer.amazon.com/en-US/docs/alexa/smarthome/thread-support.html
- [N9] Z-Wave Alliance — 125 ZWLR Certified Devices (CES 2026). official · 2026-01. https://z-wavealliance.org/news_p/z-wave-alliance-highlights-newly-certified-z-wave-long-range-devices/
- [N10] Introduction to Z-Wave 800 Series (Silicon Labs). official · 2025[u]. https://www.silabs.com/wireless/z-wave/introduction-to-z-wave-800-series
- [N11] Zigbee2MQTT Supported Devices (5,473 / 577 vendors). community · 2026-07. https://www.zigbee2mqtt.io/supported-devices/
- [N12] Koenkk/zigbee2mqtt GitHub (15,152 stars, GPL-3.0). community · 2026-05. https://github.com/koenkk/zigbee2mqtt/
- [N13] SMLIGHT SLZB-06 (Ethernet Zigbee coordinator, Z2M/ZHA/OTBR). official · 2026[u]. https://smlight.tech/gb/slzb-06
- [N14] Matter Integration (Home Assistant, seed [11]). official · 2026. https://www.home-assistant.io/integrations/matter/
- [N15] Matterbridge zigbee2mqtt (expose Z2M devices to Matter locally). community · 2026-03. https://github.com/Luligu/matterbridge-zigbee2mqtt
