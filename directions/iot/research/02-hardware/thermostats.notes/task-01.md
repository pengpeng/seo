---
task_id: 01
role: 温控/暖通市场分析师
status: complete
sources_found: 14
---

## Sources
[N1] Future Market Insights: Smart Thermostat Market Share | https://www.futuremarketinsights.com/reports/smart-thermostat-market | Source-Type: secondary-industry | As Of: 2026 [u] | Authority: 5/10
[N2] Parks Associates: Smart Thermostat Market Assessment 2025 | https://www.parksassociates.com/blogs/energy-pr/market-for-smart-thermostats-will-reach-unit-sales-of-81-million-in-2030-with-annual-revenues-exceeding-11-billion | Source-Type: secondary-industry | As Of: 2025 [u] | Authority: 7/10
[N3] IndexBox: US Smart Thermostat Market | https://www.indexbox.io/store/united-states-kw-smart-thermostat-840-market-analysis-forecast-size-trends-and-insights/ | Source-Type: secondary-industry | As Of: 2026 [u] | Authority: 5/10
[N4] Generac to Acquire ecobee (press) | https://investors.generac.com/news-releases/news-release-details/generac-acquire-ecobee-inc | Source-Type: official | As Of: 2021-11 | Authority: 10/10
[N5] Generac 10-Q (ecobee 净购买价 $735.6M) | https://investors.generac.com/static-files/8259d531-f04f-4e11-b9f7-9fbb812f2b51 | Source-Type: official | As Of: 2022 | Authority: 10/10
[N6] Globe and Mail: ecobee sells to Generac | https://www.theglobeandmail.com/business/article-smart-thermostat-pioneer-ecobee-facing-growing-threats-from-amazon/ | Source-Type: journalism | As Of: 2021-11 | Authority: 8/10
[N7] tado° 550 万台 + 盈利 (IP Group plc) | https://www.ipgroupplc.com/news-and-events/portfolio-news/2026/2026-03-26 | Source-Type: official | As Of: 2026-03 | Authority: 8/10
[N8] tado° secures €30M from Panasonic | https://www.tado.com/en/press/tado-secures-30-million-euro-funding-from-panasonic | Source-Type: official | As Of: 2025-03 | Authority: 9/10
[N9] TechCrunch: Tado raises $46.9M after IPO falters | https://techcrunch.com/2023/01/26/european-smart-thermostat-startup-tado-raises-46-8m-after-ipo-plans-falter/ | Source-Type: journalism | As Of: 2023-01 | Authority: 8/10
[N10] Google Nest 温控 Home/Away 采集 | https://support.google.com/googlenest/answer/17077697 | Source-Type: official | As Of: 2025-10 | Authority: 8/10
[N11] KartoffelToby/better_thermostat GitHub | https://github.com/KartoffelToby/better_thermostat/ | Source-Type: community | As Of: 2026 | Authority: 8/10
[N12] ESPHome OpenTherm (olegtarasov) | https://github.com/olegtarasov/esphome-opentherm | Source-Type: community | As Of: 2026 | Authority: 7/10
[N13] Home Assistant: Generic Thermostat 集成 | https://www.home-assistant.io/integrations/generic_thermostat/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[N14] LinknLink: Best IR Blasters for HA 2026 | https://www.linknlink.com/blogs/guides/best-ir-blasters-home-assistant-2026 | Source-Type: other | As Of: 2026 [u] | Authority: 4/10

## Findings
- 北美温控市场高度集中：Top5（Nest/ecobee/Honeywell/Emerson/JCI）约 65–75% 单位销量。[N3]
- 行业口径份额：Nest 20–25%、ecobee 15–20%、Honeywell Home 12–17%、Emerson 8–12%、JCI 5–9%。[N1]
- 美国渗透率 16–17% internet households；预计 2030 年美国年销 810 万台、年收入 >$11 亿；近购上升品牌为 Sensi。[N2]
- ecobee 2021-12 被 Generac 收购，最高 $770M（现金 $200M + 股票 $450M + 业绩对价 $120M），净购买价 $735.6M。[N4][N5][N6]
- Amazon 2021 推 $60 智能温控器压价，直接冲击 ecobee/Nest 溢价定位；ecobee 北美份额曾报 ~3.25%[u]。[N6]
- tado°（慕尼黑，2011 创立）连接 550 万台温控器、>100 万户，2024 营收 ~$80M[u]，2026-03 宣布经营盈利。[N7]
- tado° 2025-03 获松下 €30M（累计融资 ~$280M[u]）；2023 IPO/SPAC 搁置后转向盈利路线；投资方含 Amazon/Siemens/E.On。[N8][N9]
- Nest Home/Away 融合运动传感 + 手机 GPS + 其他设备推断在家离家。[N10]
- 本地栈：generic_thermostat（sensor+switch 本地轮询）、Better Thermostat（TRV + 外部温感 + 开窗停暖 + MPC/PID/TPI）、ESPHome OpenTherm（2024.11 进核心，ESP32 作 master + PID 控锅炉）。[N13][N11][N12]
- IR 空调：Sensibo/Cielo 云 API 导向；本地替代 Broadlink RM4 + SmartIR 或 ESPHome IR。[N14]

## Market Leaders
- 北美 #1：Google Nest（Alphabet）——份额 20–25%，学习型图腾。[N1]
- 学习型 #2：ecobee（Generac 旗下）——份额 15–20%。[N1][N4]
- 专业安装/新建：Honeywell Home（Resideo）——份额 12–17%，承包商 + 安防/DERMS。[N1][N2]
- 价值/上升：Emerson Sensi——份额 8–12%。[N1][N2]
- 欧洲龙头：tado°——550 万台、>100 万户、2024 ~$80M、2026 盈利。[N7]
- 空调 IR：Sensibo（特拉维夫）/ Cielo——云 API 导向。[N14]
- 母公司：Alphabet / Generac(GNRC) / Resideo(REZI) / Emerson(EMR) / Johnson Controls(JCI) / Amazon / tado°(私营) / Sensibo(私营)。[N1][N4][N8]

## Segment Champions
- 学习型/AI 节能：Nest（time-of-use 电价优化）、ecobee（占用感知 + 能耗分析）。[N1]
- 专业安装/可靠性：Honeywell Home（Resideo）。[N2]
- 欧洲多系统：tado°（vendor-agnostic，燃气/油/热泵/地暖/暖气片 TRV，动态电价 aWATTar，降暖气 22%）。[N7][N8]
- 空调 IR：Sensibo Sky / Cielo Breez。[N14]
- 本地/自托管：HA generic_thermostat + Better Thermostat + ESPHome OpenTherm；IR 用 Broadlink/ESPHome/SmartIR。[N11][N12][N13][N14]

## VC Rising Stars
- tado°：2023 IPO 搁置 → 2025 松下 €30M → 2026-03 经营盈利 + 员工虚拟股权（欧洲家居能源少见独立盈利样本）。[N7][N8][N9]
- ecobee → Generac 子公司（2021），从独立玩家转能源巨头智能家居入口。[N4][N6]
- Amazon $60 温控器下场压价（云巨头把温控当数据/服务入口）。[N6]
- Resideo/Honeywell Home 2025 推商用级温控 + BMS/DERMS/需求响应。[N2]
- 开源双轨：HA / Better Thermostat / ESPHome OpenTherm vs 厂商云学习算法。[N11][N12][N13]

## Candidate Keywords
nest thermostat alternative / ecobee alternative / honeywell thermostat alternative / tado alternative / sensibo alternative / local smart thermostat / smart thermostat without cloud / home assistant thermostat / generic thermostat home assistant / better thermostat / esphome thermostat / esphome opentherm / diy smart thermostat / zigbee trv home assistant / control ac home assistant / broadlink home assistant / nest vs ecobee / best smart thermostat / best thermostat home assistant / opentherm vs on off thermostat / sensibo vs broadlink / best zigbee trv

## Deep Read Notes
### Source [N4][N5][N6]: Generac 收购 ecobee
Key data: 2021-12 完成；最高 $770M（现金 $200M + 股票 $450M + 业绩对价 $120M）；10-Q 披露净购买价 $735.6M（现金 $225.5M + 股票 $420.8M + 对价 $89.4M）；作价约 ecobee 过去 12 个月营收 4.5x；ecobee 时有 200 万联网家庭、520 员工。
Key insight: 温控独立玩家在云巨头（Google/Amazon）夹击下难独存，转投能源/发电巨头寻求 DER/需求响应协同——温控正从"设备"变"电网节点"。

### Source [N7][N8]: tado° 盈利 + 松下投资
Key data: 550 万台温控器、>100 万户；2025-03 松下 €30M、累计 ~$280M；vendor-agnostic 兼容燃气/油/热泵/地暖/暖气片 TRV；宣称平均降暖气 22%；2022 收购 aWATTar（动态电价）。
Key insight: 欧洲路线（多系统 + 动态电价 + 热泵优化）与北美"学习型温控"路线不同；节能算法是其护城河，也是本地栈最难平替的一块。

### Source [N11][N12][N13]: 本地温控栈
Key data: generic_thermostat = sensor + switch 本地轮询（heat/cool/off、cold/hot tolerance、min_cycle_duration、preset away/eco）；Better Thermostat = TRV + 外部温感 + 开窗停暖 + 天气 + MPC/PID/TPI/AI-time 算法；ESPHome OpenTherm 2024.11 进核心，ESP32 作 OpenTherm master + PID 直控锅炉 setpoint（占用现有温控位，不能与原温控共存）。
Key insight: "到点控温 + 开窗停暖 + presence 联动"可完全本地复刻；但商业自适应学习（Nest Learning、tado° 22%）属训练出的商业 IP，本地只能 PID/MPC 近似——这是本品类诚实差距。

## Gaps
- 无免费公开的按品牌精确出货份额 %（Parks/FMI/IndexBox 完整数据付费；份额为区间估计）。[N1][N2][N3]
- Sensibo/Cielo/Mysa 私营财务无官方数字（媒体/CB Insights 口径[u]）。[N14]
- ecobee 独立营收自被 Generac 收购后并入合并报表，无单列近期数字。[N5]
- tado° 2024 营收 ~$80M 为 CB Insights 口径[u]，无官方年报。[N7]
- 各品牌无 brand-seo 报告；HA 仅 market 报告。
- 商业节能学习算法实际节能率（22% / Nest 宣称）缺独立第三方实测对照[u]。

## END
