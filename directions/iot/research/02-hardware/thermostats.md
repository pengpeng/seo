# 温控 / 暖通竞品与关键词（IoT 方向 · 品类 12）

> 研究日期: 2026-07-04 | 来源: task-01（14 源）+ 原家居分册 seed 笔记（[9] Nest Home/Away）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 智能温控/暖通（smart thermostat / HVAC control）：学习型温控器、Wi-Fi 温控器、TRV 恒温阀、空调 IR 控制器、热泵/锅炉优化器。语音中枢见品类 03；传感器/网关见品类 13。归属 IoT 新方向"硬件章"。发现笔记见 [thermostats.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/thermostats.notes)。

## 摘要
温控是家居 IoT 里"云智能 vs 本地栈"张力最典型的品类。北美市场高度集中：五大品牌（Google Nest、ecobee、Honeywell Home/Resideo、Emerson Sensi、Johnson Controls）约占 65–75% 单位销量 [N3]，行业口径份额 Nest 20–25%、ecobee 15–20%、Honeywell 12–17% [N1]，美国智能温控器渗透率约 16–17% internet households、预计 2030 年美国年销 810 万台、年收入超 $11 亿 [N2]。资本侧：ecobee 2021 年被发电机厂商 Generac 以最高 $770M（净购买价 $735.6M）收购 [N4][N5]；欧洲龙头 tado° 已连接 550 万台温控器、2026 年宣布经营盈利、2025 年获松下 €30M 战略投资，IPO 曾多次搁置 [N7][N8][N9]。**隐私要害**：温控器把"在家/离家"（Nest Home/Away 融合运动传感 + 手机 GPS 推断）、作息、建筑供暖类型都变成长期时间序列 [N10]。**Olares 落点（诚实）**：HA generic_thermostat / Better Thermostat + ESPHome OpenTherm 控锅炉 + Broadlink/ESPHome IR 替 Sensibo，本地栈可用；但商业厂商的**节能学习/自适应算法（Nest Learning、tado° 22% 节能）难以完全平替** [N11][N12][N13][N14]。

## 1. 品类概述
温控/暖通分四条产品线：① 学习型/AI 温控器（Nest、ecobee，主打自适应节能与占用感知）；② 专业安装渠道 Wi-Fi 温控器（Honeywell Home、Emerson Sensi，靠 HVAC 承包商分销）；③ 欧洲多设备系统（tado°、Netatmo，兼容燃气锅炉/油暖/热泵/地暖/暖气片 TRV，vendor-agnostic）；④ 空调 IR 控制器（Sensibo、Cielo，把普通分体空调联网）。协议上分云优先（Nest/ecobee/Sensibo 云 API）与本地友好（Zigbee TRV、OpenTherm、Z-Wave、Matter、ESPHome）两路。隐私视角下，单个温控器信息量看似低，但 HVAC 数据直接暴露作息（起床/睡眠/离家窗口）+ 建筑信息（供暖方式、隔热、面积），且 Home/Away 是跨设备行为画像的核心推断源 [N10]。

## 2. 市场领导者 / top 畅销
| 口径 | 领导者 | 锚点 |
|------|--------|------|
| 北美份额 #1 | Google Nest（Alphabet） | 行业口径份额 20–25%；Nest Learning 为品类图腾 [N1] |
| 学习型 #2 | ecobee（Generac 旗下） | 份额 15–20%；2021 被 Generac 收购最高 $770M [N1][N4] |
| 专业安装/新建渠道 | Honeywell Home（Resideo） | 份额 12–17%，主攻承包商 + 安防/DERMS 集成 [N1][N2] |
| 价值/上升 | Emerson Sensi | 份额 8–12%，近购销量"on the upswing" [N1][N2] |
| 欧洲龙头 | tado°（慕尼黑） | 连接 550 万台、>100 万户、2024 营收 ~$80M、2026 盈利 [N7] |
| 空调 IR 细分 | Sensibo（特拉维夫）/ Cielo | AC/热泵联网控制，云 API 导向 [N14] |

母公司/归属：Alphabet（Nest）、Generac（NYSE:GNRC，ecobee）、Resideo（NYSE:REZI，Honeywell Home 授权）、Emerson（NYSE:EMR，Sensi）、Johnson Controls（NYSE:JCI，Lux/Lynx）、Amazon（Ring/Amazon 温控器 $60 入门）、tado°（私营，松下/E.ON/Siemens/Amazon 投资）、Sensibo（私营）[N1][N2][N4][N8]。

**置信度: Medium**（Parks/FMI/IndexBox 三方对份额区间一致，但免费公开的按品牌精确出货 % 缺失，口径以北美为主）。

## 3. 细分赛道冠军
- **学习型/AI 节能冠军**：Google Nest（自适应学习 + time-of-use 电价优化）、ecobee（占用感知 + 远程温感 + 能耗分析）[N1]。
- **专业安装/可靠性冠军**：Honeywell Home（Resideo）——承包商信任 + 新建工程 + 安防/DERMS 一体 [N2]。
- **欧洲多系统冠军**：tado°——vendor-agnostic，兼容燃气/油/热泵/地暖/暖气片 TRV，动态电价（收购 aWATTar），宣称平均降暖气消耗 22% [N7][N8]。
- **空调 IR 冠军**：Sensibo Sky / Cielo Breez——把传统分体空调变智能，AC 场景体验强，但云 API 导向、价格高 [N14]。
- **本地/自托管栈冠军**：**Home Assistant** 作编排中枢——`generic_thermostat`（sensor + switch 控加热/制冷，本地轮询）[N13] + **Better Thermostat**（TRV + 外部温感 + 开窗停暖 + MPC/PID/TPI 算法）[N11] + **ESPHome OpenTherm**（自 ESPHome 2024.11 进核心，ESP32 作 OpenTherm master 直控锅炉 + PID）[N12]；IR 空调用 **Broadlink RM4 / ESPHome IR / SmartIR** 替 Sensibo [N14]。

**置信度: High**（自托管分层冠军有社区共识；节能算法冠军属商业侧）。

## 4. VC 圈明日之星
温控硬件本身不是新 VC 热点，事件集中在并购、盈利与巨头下场：
- **tado°**：2023 IPO/SPAC 搁置后转向盈利，2025 获松下 €30M（累计融资 ~$280M），2026-03 宣布经营盈利 + 员工虚拟股权，是欧洲家居能源管理少见的"独立走向盈利"样本 [N7][N8][N9]。
- **ecobee → Generac**：2021 被 Generac 收购（作为独立子公司），从"被 Amazon 挤压的独立玩家"转为发电机/能源巨头的智能家居入口 [N4][N6]。
- **Amazon 下场**：2021 推 $60 智能温控器压价，直接冲击 ecobee/Nest 溢价定位，是"云巨头把温控当数据/服务入口"的信号 [N6]。
- **Resideo/Honeywell Home**：2025 推商用级温控线接 BMS，DERMS + 需求响应（demand response）成新增长轴 [N2]。
- 开源侧事实标准 **Home Assistant** + **Better Thermostat** / **ESPHome OpenTherm** 构成"闭源云学习算法 vs 开源本地控制"双轨 [N11][N12][N13]。

**置信度: Medium**（并购/融资/盈利事件可靠，Sensibo 等私营财务多为媒体口径[u]）。

## 5. 候选产品关键词
品牌替代：`nest thermostat alternative`、`ecobee alternative`、`honeywell thermostat alternative`、`tado alternative`、`sensibo alternative`。
去云/本地（核心机会）：`local smart thermostat`、`smart thermostat without cloud`、`home assistant thermostat`、`generic thermostat home assistant`、`better thermostat`、`esphome thermostat`、`esphome opentherm`、`diy smart thermostat`、`zigbee trv home assistant`、`control ac home assistant`、`broadlink home assistant`。
选购/对比：`nest vs ecobee`、`best smart thermostat`、`best thermostat home assistant`、`opentherm vs on off thermostat`、`sensibo vs broadlink`、`best zigbee trv`。

> Olares Market 已有 Home Assistant 报告，`home assistant thermostat`、`nest thermostat alternative`、`esphome opentherm`、`local smart thermostat` 是与现有资产最贴合的切入。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **Home/Away = 在家离家推断（核心风险）**：Nest 温控器融合自带运动传感 + 手机 GPS + 家中其他设备判断 Home/Away，单个温控器即可重建长期作息与离家窗口，属高价值行为数据 [N10]。
- **HVAC 数据 = 作息 + 建筑画像**：制热/制冷时间序列暴露起床/睡眠/工作/旅行；供暖类型（燃气/热泵/地暖）、面积、隔热质量、电价套餐都可从曲线反推——温控云本质是"住户与建筑的能耗档案"。
- **空调 IR 控制器上云**：Sensibo/Cielo 云 API 导向，AC 使用曲线（何时在房、开关频率）默认过厂商云 [N14]。
- **云依赖 = 功能/存续依赖**：温控智能多绑定厂商云与订阅（能源报告、需求响应），云端策略变化即影响可用性——与插座章（品类 11）Wemo 云关停同构风险。
- **Olares 平替栈**：HA on Olares 作编排中枢；燃气/OpenTherm 锅炉 → **ESPHome OpenTherm**（ESP32 作 master + PID 直控，2024.11 进核心）[N12]；简单继电器加热/制冷 → **generic_thermostat**（sensor + switch 本地轮询）[N13]；暖气片/地暖 TRV → Zigbee2MQTT/ZHA 接 Zigbee TRV + **Better Thermostat**（外部温感 + 开窗停暖 + MPC/PID/TPI，去厂商云）[N11]；分体空调 → **Broadlink RM4 / ESPHome IR / SmartIR** 本地发码替 Sensibo [N14]；占用/节能 → ESPHome mmWave/PIR 传感器做本地 presence，替代 Nest Home/Away 的云推断 [N14]。
- **诚实差距**：本地栈能复刻"到点控温 + 开窗停暖 + presence 联动"，但 **Nest Learning / tado° 的自适应节能学习算法（宣称 22% 节能）属商业 IP，本地栈只能用 PID/MPC/TPI 近似，难完全平替**；OpenTherm 需接线知识、Broadlink 需 SmartIR 学码，属技术用户路径 [N11][N12][N14]。

**置信度: High**（本地温控栈成熟；节能学习算法差距为已知诚实项）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：温控"智能"到底值不值云——厂商叙事是自适应学习省能耗（Nest/tado° 宣称两位数节能）、需求响应参与电网调度；反方是这些收益多可由本地 schedule + presence + PID 近似，而云换来的是行为数据外流与订阅锁定。此外份额口径以北美为主，欧洲（tado°/Netatmo/Drayton）与亚太格局不同 [N1][N2][N7]。

**反方解释**：商业温控的"开箱即用 + 自动学习 + 手机远程 + 语音 + 能源报告 + 需求响应返利"体验对非技术用户显著优于自托管；ESPHome OpenTherm 需要接线与 OpenTherm 适配板、Better Thermostat 需 Zigbee 协调器与调参、Broadlink 需 SmartIR 学码，均属技术用户路径。且 Nest/tado° 的自适应节能算法是多年数据训练的商业 IP，本地 PID/MPC 难完全对标 [N11][N12][N14]。

**参考文献**（Source-Type · As Of）
- [N1] Future Market Insights, Smart Thermostat Market Share（Nest 20–25% / ecobee 15–20% / Honeywell 12–17%）. secondary-industry · 2026[u]. https://www.futuremarketinsights.com/reports/smart-thermostat-market
- [N2] Parks Associates, Smart Thermostat Market Assessment 2025（8.1M 台 2030、$1.1B、渗透率 16–17%、Top10 品牌）. secondary-industry · 2025[u]. https://www.parksassociates.com/blogs/energy-pr/market-for-smart-thermostats-will-reach-unit-sales-of-81-million-in-2030-with-annual-revenues-exceeding-11-billion
- [N3] IndexBox, US Smart Thermostat Market（Top5 65–75% 单位销量）. secondary-industry · 2026[u]. https://www.indexbox.io/store/united-states-kw-smart-thermostat-840-market-analysis-forecast-size-trends-and-insights/
- [N4] Generac to Acquire ecobee（最高 $770M）. official · 2021-11. https://investors.generac.com/news-releases/news-release-details/generac-acquire-ecobee-inc
- [N5] Generac 10-Q, ecobee 净购买价 $735.6M. official · 2022. https://investors.generac.com/static-files/8259d531-f04f-4e11-b9f7-9fbb812f2b51
- [N6] Globe and Mail, ecobee sells to Generac（Amazon $60 温控器压价、ecobee NA 份额 ~3.25%[u]）. journalism · 2021-11. https://www.theglobeandmail.com/business/article-smart-thermostat-pioneer-ecobee-facing-growing-threats-from-amazon/
- [N7] tado° 连接 550 万台并盈利（IP Group plc）. official · 2026-03. https://www.ipgroupplc.com/news-and-events/portfolio-news/2026/2026-03-26
- [N8] tado° secures €30M from Panasonic. official · 2025-03. https://www.tado.com/en/press/tado-secures-30-million-euro-funding-from-panasonic
- [N9] TechCrunch, Tado raises $46.9M after IPO plans falter. journalism · 2023-01. https://techcrunch.com/2023/01/26/european-smart-thermostat-startup-tado-raises-46-8m-after-ipo-plans-falter/
- [N10] Google Nest 温控 Home/Away 采集. official · 2025-10. https://support.google.com/googlenest/answer/17077697
- [N11] KartoffelToby/better_thermostat（TRV + 外部温感 + MPC/PID/TPI）. community · 2026. https://github.com/KartoffelToby/better_thermostat/
- [N12] ESPHome OpenTherm（olegtarasov/esphome-opentherm，2024.11 进核心）. community · 2026. https://github.com/olegtarasov/esphome-opentherm
- [N13] Home Assistant, Generic Thermostat 集成. official · 2026. https://www.home-assistant.io/integrations/generic_thermostat/
- [N14] LinknLink, Best IR Blasters for Home Assistant 2026（Sensibo 云 API、Broadlink RM4、ESPHome IR）. other · 2026[u]. https://www.linknlink.com/blogs/guides/best-ir-blasters-home-assistant-2026
- 完整发现笔记见 [thermostats.notes/task-01.md](/Users/pengpeng/seo/directions/iot/research/02-hardware/thermostats.notes/task-01.md)。
