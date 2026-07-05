# 智能家电竞品与关键词（IoT 方向 · 品类 15）

> 研究日期: 2026-07-04 | 来源: task-01（13 源，WebSearch + WebFetch）+ 原家居分册 seed 笔记 | 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 大白电（washers/dryers 洗衣干衣、dishwashers 洗碗机、fridges 冰箱、ovens/cooktops 烤箱灶具）联网型号及其厂商生态平台。扫地机器人见品类 14；语音中枢见品类 03；HVAC/温控见品类 12。只收面向海外市场的硬件品牌，剔除中国内销定位。归属 IoT 新方向"硬件章"。发现笔记见 [smart-appliances.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-appliances.notes)。

## 摘要
智能家电是 Olares 自托管**成熟度最低**的品类——直说：本品类**没有成熟的完全本地栈**。市场由两大韩系生态平台领跑：**Samsung SmartThings** 与 **LG ThinQ**（VMR 估份额各约 18–19%[u]），欧洲高端为 **BSH（Bosch/Siemens/Gaggenau/Thermador，Home Connect）€15.0B** 与 **Miele（Miele@home）€5.16B**，美国为 **Whirlpool（$15.5B，NYSE:WHR）** 与 **GE Appliances**（Haier 旗下但美国品牌，北美连续 4 年 #1，母公司 Haier Smart Home FY2025 RMB 302.35B）[7][8][9][10]。品类核心事实：**联网率极低**——Ars Technica 引 2023 年 LG 卖出的智能家电"不到一半"真正联网[5]，说明用户对"家电联网价值"并不买账。隐私上正在恶化：Samsung Family Hub 冰箱 2025-11-03 起在美国 idle 门屏推广告，标志"家电即广告位"[5][6]。**Olares 落点（诚实）**：仅 **BSH Home Connect 可经 hcpy 本地无云**（BSH 系统设计上允许本地 TLS-PSK 连接）[11][12]；LG/Samsung/Whirlpool 无本地 API，HA 集成一律走厂商云；其余靠 **ESPHome 外接功率/门磁传感器推断"洗衣完成/门开"** 状态。成熟度: **low**。

## 1. 品类概述
大白电分两类联网姿态：① **厂商云 + 生态平台**（SmartThings / ThinQ / Home Connect / Miele@home，几乎全部主流品牌），控制、状态、OTA 均经跨国云 + 账号绑定；② **无 Wi-Fi 传统家电 + 外挂推断**（用功率计量插座/门磁/振动传感器旁路读状态，不碰厂商云）。与灯/插座/传感器（品类 10 本地成熟）不同，白电的 SoC、电机、程序逻辑封闭在厂商固件里，**极少开放本地 API**——这是本品类自托管薄弱的根因。隐私视角下，洗衣/洗碗/冰箱的**使用时段序列 = 作息画像**（何时在家做饭、何时洗衣、冰箱开合频率），加上 OTA + 账号绑定的跨国云同步，单账号即可长期重建家庭生活节律。

## 2. 市场领导者 / top 畅销
| 口径 | 领导者 | 锚点 |
|------|--------|------|
| 生态平台（韩系双雄） | Samsung SmartThings / LG ThinQ | VMR 估份额 ~18.5% / ~18.7%[u]；全品类 Wi-Fi + AI [1][2][3] |
| 欧洲高端（内置/独立） | BSH（Bosch/Siemens/Gaggenau/Thermador） | FY2025 turnover €15.0B，北美再增份额 [7] |
| 欧洲家族高端 | Miele（Miele@home） | FY2025 turnover €5.16B（+2.3%），家族独资 [10] |
| 美国上市锚 | Whirlpool（NYSE:WHR） | FY2025 净销售 ~$15.5B，~90% 收入在美洲 [8] |
| 美国 #1 / 母公司全球 #1 | GE Appliances（Haier 旗下美国品牌） | 北美连续 4 年 #1；Haier Smart Home FY2025 RMB 302.35B [9] |
| 价值搅局者 | Midea | 美国认知度 3 年从 5% → 14.2% [4] |

母公司/品牌组合：Samsung Electronics、LG Electronics、BSH（Bosch 全资）、Miele（Miele+Zinkann 家族）、Whirlpool（Whirlpool/KitchenAid/Maytag/JennAir/Amana/InSinkErator）、Haier Smart Home（600690.SH / 06690.HK；Haier/GE Appliances/Fisher & Paykel/Candy/Casarte）[7][8][9][10]。

**置信度: Medium**（财务锚均官方可靠；按品牌精确市场份额 % 缺免费公开数据，VMR 数字为估算[u]，全球/北美 #1 因口径而异）。

## 3. 细分赛道冠军
- **洗衣/干衣 AI 冠军**：LG ThinQ（AI 洗涤剂投放、负载/织物识别）与 Samsung Bespoke AI Laundry [2][3]。
- **冰箱交互屏冠军**：Samsung Family Hub（嵌入式 Android 平板门屏、食材识别、Bixby 语音）——也是"广告位"争议主角 [5][6]。
- **烤箱/内置高端冠军**：BSH（Bosch/Gaggenau/Thermador）与 Miele（Steam/networked Sense 烹饪系统）[7][10]。
- **本地可控冠军（唯一像样）**：**BSH Home Connect** → hcpy/hcpy2 首次云登录取密钥后**纯本地 websocket→MQTT**→HA，是白电里唯一"厂商设计允许无云"的路径 [11][12][13]。
- **通用外挂法（跨所有品牌）**：**ESPHome + 功率计量插座 / 门磁 / 振动传感器**，推断"洗衣/洗碗完成""冰箱门开"等状态，完全不碰厂商云——这是本品类最普适的 Olares 落点。

**置信度: High**（分层与"仅 BSH 可本地"的判断有社区与官方文档共识）。

## 4. VC 圈明日之星
智能家电本身**不是 VC 热点**，几乎无独立初创；资本动作集中在巨头并购与平台整合：
- **LG × Athom（Homey）**：2024 年末 LG 收购 Athom，把 Homey 的本地优先自动化引擎并入 ThinQ 生态 [1]。
- **Haier 全球化并购**：集齐 GE Appliances / Fisher & Paykel / Candy / Casarte 七大品牌，FY2025 首破 RMB 3000 亿 [9]。
- **标准侧（真正的"明日之星"是协议）**：Matter 逐步接入白电，但当前仍以品牌云 + 平台为主；一旦 Matter 对洗衣/洗碗/冰箱落地本地控制，将是本品类去云的最大变量 [2][3]。
- **开源侧**：仅小众社区项目（osresearch/hcpy、HA Home Connect 集成），无商业化明星——与摄像头（Frigate + 多家 AI 初创）形成鲜明对比 [11][12]。

**置信度: Medium**（并购事件与"VC 冷淡"判断可靠；具体估值/份额多为媒体或估算口径[u]）。

## 5. 候选产品关键词
品牌/平台替代：`lg thinq alternative`、`samsung smartthings appliance alternative`、`smart appliance without cloud`。
去云/本地（核心机会，但需求量小）：`home connect home assistant`、`bosch home connect local`、`hcpy home connect`、`local smart appliance control`、`control smart appliance offline`、`home assistant washing machine`、`home assistant dishwasher notification`、`esphome washing machine done sensor`、`matter appliances home assistant`。
隐私/广告痛点（内容切入）：`smart fridge without ads`、`turn off samsung fridge ads`、`do smart appliances spy on you`。

> 与现有资产最贴合的切入是 `home connect home assistant` / `home assistant washing machine` / `smart appliance without cloud`（Olares Market 已有 Home Assistant 报告）。但本品类整体搜索需求与自托管可行性都弱于摄像头/照明，建议作长尾补充而非主推。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **使用时段 = 作息画像**：洗衣/洗碗/冰箱的开机时刻与频率序列可重建"何时在家、何时做饭、何时旅行"；单账号跨国云即长期存这份生活节律。
- **OTA + 账号绑定的跨国云同步**：控制、状态、固件全经厂商云（SmartThings / ThinQ / Home Connect）；HA 官方 Home Connect 集成本身也走 developer.home-connect.com 云 OAuth + server-sent events [11]。
- **家电即广告位（已核实）**：Samsung Family Hub 冰箱 2025-11-03 起在美国 idle 门屏推"promotions and curated advertisements"（$1,800–$3,000+ 机型），可 Settings→Advertisements 关闭或切 Art/Album 主题规避；Samsung 称"contextual/non-personal、不收集个人信息"，但趋势令人警惕 [5][6]。
- **低联网率的另一面**：Ars 引 2023 年 LG 智能家电联网率 <50%[5]——用户本能地不联网，正是"无云也能用"叙事的天然受众。
- **Olares 平替栈（诚实分级）**：
  - **最佳（仅 BSH）**：Bosch/Siemens Home Connect → **hcpy/hcpy2 本地无云**（TLS-PSK，首次云登录取密钥后纯本地）→ MQTT → HA on Olares [11][12][13]。
  - **有限（LG/Samsung/Whirlpool）**：无本地 API，只能经 HA 的 SmartThings / Home Connect **云集成**接入（仍依赖厂商云，仅把编排/通知留本地）[11]。
  - **最普适（任意品牌，含无 Wi-Fi 老家电）**：**ESPHome 外接功率计量插座 / 门磁 / 振动传感器**推断状态；防火墙/DNS 阻断家电出网与 `samsungads.com` 等广告域。
- **诚实差距**：本品类**无成熟的完全本地控制栈**——只有 BSH 一家可真本地，其余均绕不开厂商云；相比摄像头（Frigate）、照明/插座（Zigbee2MQTT/Shelly）的成熟本地方案，智能家电是 IoT 各品类里 Olares 落点**最弱**的一个。

**置信度: High**（"仅 BSH 可本地、整体成熟度 low"有官方文档 + 社区项目 + 集成清单交叉印证）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：谁是"全球 #1"——按生态/份额是 Samsung 与 LG（VMR 估各 ~18%[u]）；按母公司大白电零售量是 Haier Smart Home（Euromonitor 连续多年全球 #1，含 GE Appliances）[1][9]。差异来自"生态平台份额"vs"整机零售量"、以及是否把 GE Appliances 计入 Haier。

**反方解释**：厂商云 + 生态平台带来跨地远程启停、AI 洗涤/食材建议、能耗错峰、语音联动与 OTA，对普通用户"开箱即用"体验显著优于任何自托管方案；而白电本地栈几乎不存在（仅 BSH 一家、且需命令行取密钥），ESPHome 外挂只能读状态、不能控机。因此本品类对绝大多数用户而言"云是唯一现实选项"——Olares 的价值主要在**编排/通知留本地 + 阻断广告与出网**，而非完全去云。

**参考文献**（Source-Type · As Of）
- [1] Verified Market Research: Top 7 Smart Appliance Brands（份额估算[u]）. secondary-industry · 2026. https://www.verifiedmarketresearch.com/blog/top-smart-appliance-companies/
- [2] Fortune Business Insights: Smart Home Appliances Market. secondary-industry · 2025. https://www.fortunebusinessinsights.com/smart-home-appliances-market-106267
- [3] Research Nester: Connected Home Appliances Market. secondary-industry · 2026. https://www.researchnester.com/reports/connected-home-appliances-market/811
- [4] YouGov 2026 US Consumer Electronics Rankings. secondary-industry · 2026. https://yougov.com/en-us/articles/54107-samsung-leads-2026-us-consumer-electronics-rankings-as-generational-gaps-emerge-in-brand-value
- [5] Ars Technica: Samsung 强推冰箱广告. journalism · 2025-09. https://arstechnica.com/gadgets/2025/09/samsung-forces-ads-onto-fridges-is-a-bad-sign-for-other-appliances/
- [6] The Verge: Family Hub 冰箱广告 11-03 上线. journalism · 2025-10. https://www.theverge.com/report/806797/samsung-family-hub-smart-fridge-ads-opt-out
- [7] BSH Home Appliances FY2025 turnover €15.0B. official · 2026-03. https://press.bsh-group.com/pressreleases/demonstrating-resilience-investing-in-the-future-bsh-asserts-itself-with-a-turnover-of-15-euro-billion-in-2025-in-a-challenging-environment-3439937
- [8] Whirlpool FY2025 Results（净销售 $15.5B）. official · 2026-01. https://www.prnewswire.com/news-releases/whirlpool-corporation-announces-fourth-quarter-and-full-year-results-provides-2026-guidance-302673163.html
- [9] Haier Smart Home FY2025（RMB 302.35B；GE Appliances 北美 #1）. official · 2026-03. https://www.haier.com/global/press-events/news/20260402_288863.shtml
- [10] Miele Business Year 2025 turnover €5.16B. official · 2026. https://www.miele.de/en/m/miele-business-year-2025-moderate-growth-despite-headwinds-8148.htm
- [11] Home Assistant: Home Connect 集成（Bosch/Siemens，官方云 API）. official · 2026. https://www.home-assistant.io/integrations/home_connect/
- [12] osresearch/hcpy：BSH Home Connect 本地无云控制. community · 2026. https://github.com/osresearch/hcpy
- [13] HA 社区：Home Connect 本地 MQTT bridge（cloudless）. community · 2026. https://community.home-assistant.io/t/homeconnect-elegant-solution-based-on-a-mqtt-bridge-local-no-cloud/687153
- 完整 13 源与深读笔记见 [smart-appliances.notes/task-01.md](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-appliances.notes/task-01.md)。
