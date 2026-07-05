---
task_id: 01
role: 智能家电市场分析师
status: complete
sources_found: 13
mode: Lightweight（WebSearch + WebFetch，AS_OF 2026-07-04）
---

## Sources
[1] Verified Market Research: Top 7 Smart Appliance Brands（份额表） | https://www.verifiedmarketresearch.com/blog/top-smart-appliance-companies/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 4/10 [u]
[2] Fortune Business Insights: Smart Home Appliances Market | https://www.fortunebusinessinsights.com/smart-home-appliances-market-106267 | Source-Type: secondary-industry | As Of: 2025 | Authority: 5/10
[3] Research Nester: Connected Home Appliances Market（LG ThinQ ON @IFA2024） | https://www.researchnester.com/reports/connected-home-appliances-market/811 | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[4] YouGov 2026 US Consumer Electronics Rankings | https://yougov.com/en-us/articles/54107-samsung-leads-2026-us-consumer-electronics-rankings-as-generational-gaps-emerge-in-brand-value | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[5] Ars Technica: Samsung 强推冰箱广告 | https://arstechnica.com/gadgets/2025/09/samsung-forces-ads-onto-fridges-is-a-bad-sign-for-other-appliances/ | Source-Type: journalism | As Of: 2025-09 | Authority: 8/10
[6] The Verge: Family Hub 冰箱广告 11-03 上线 | https://www.theverge.com/report/806797/samsung-family-hub-smart-fridge-ads-opt-out | Source-Type: journalism | As Of: 2025-10 | Authority: 8/10
[7] BSH Home Appliances FY2025 turnover €15.0B | https://press.bsh-group.com/pressreleases/demonstrating-resilience-investing-in-the-future-bsh-asserts-itself-with-a-turnover-of-15-euro-billion-in-2025-in-a-challenging-environment-3439937 | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[8] Whirlpool FY2025 Results（净销售 $15.5B，NYSE:WHR） | https://www.prnewswire.com/news-releases/whirlpool-corporation-announces-fourth-quarter-and-full-year-results-provides-2026-guidance-302673163.html | Source-Type: official | As Of: 2026-01 | Authority: 9/10
[9] Haier Smart Home FY2025（营收 RMB 302.35B；GE Appliances 北美 #1） | https://www.haier.com/global/press-events/news/20260402_288863.shtml | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[10] Miele Business Year 2025 turnover €5.16B | https://www.miele.de/en/m/miele-business-year-2025-moderate-growth-despite-headwinds-8148.htm | Source-Type: official | As Of: 2026 | Authority: 9/10
[11] Home Assistant: Home Connect 集成（Bosch/Siemens，官方云 API） | https://www.home-assistant.io/integrations/home_connect/ | Source-Type: official | As Of: 2026 | Authority: 9/10
[12] osresearch/hcpy：BSH Home Connect 本地无云控制 | https://github.com/osresearch/hcpy | Source-Type: community | As Of: 2026 | Authority: 7/10
[13] HA 社区：Home Connect 本地 MQTT bridge（cloudless） | https://community.home-assistant.io/t/homeconnect-elegant-solution-based-on-a-mqtt-bridge-local-no-cloud/687153 | Source-Type: community | As Of: 2026 | Authority: 6/10

## Findings
- 智能家电竞争由两大韩系生态平台领跑：Samsung SmartThings 与 LG ThinQ，二者在洗衣机/冰箱/烤箱/洗碗机全线铺 Wi-Fi + AI。[2][3][4]
- 份额口径（VMR，付费源估算[u]）：Samsung 18.5%、LG 18.7%、BSH(Bosch/Siemens) 10.6%、Haier 15%(est)、Whirlpool 6.2%。精确份额缺免费公开数据。[1]
- 财务锚（FY2025）：Haier Smart Home RMB 302.35B（首破 3000 亿，含 GE Appliances，北美连续 4 年 #1）；Whirlpool 净销售 ~$15.5B（NYSE:WHR，~90% 收入在美洲）；BSH €15.0B；Miele €5.16B。[7][8][9][10]
- 美国口径消费者考虑度：Samsung #1、LG 紧随；Midea 三年内认知度从 5% 升至 14.2%；Whirlpool 在 Gen X / Boomer 仍前二。[4]
- 联网率极低：Ars 报道 2023 年 LG 卖出的智能家电中"不到一半"真正联网——采用障碍是本品类核心事实。[5]
- Samsung Family Hub 冰箱 2025-11-03 起在美国 idle 封面屏推广告（$1,800–$3,000+ 机型），可关闭/切 Art 模式规避；标志"家电即广告位"趋势。[5][6]
- 本地栈：BSH Home Connect 是少见的"厂商设计上允许本地无云"平台（TLS-PSK），hcpy/hcpy2 可 OAuth 取密钥后本地 websocket→MQTT；但 LG/Samsung/Whirlpool 无本地 API，HA 集成走云。[11][12][13]

## Market Leaders
- 生态平台：Samsung SmartThings / LG ThinQ（韩系双雄，全品类联网 + AI）。[2][3][4]
- 欧洲高端：BSH（Bosch/Siemens/Gaggenau/Thermador，Home Connect）€15B；Miele（Miele@home）€5.16B 独立家族企业。[7][10]
- 美国：Whirlpool（Whirlpool/KitchenAid/Maytag/JennAir/Amana）$15.5B；GE Appliances（Haier 旗下但美国品牌，北美 #1）。[8][9]
- 价值搅局者：Midea（认知度快速上升，海外扩张）。[4]

## Segment Champions
- 洗衣/干衣 AI：LG ThinQ（AI 洗涤剂投放/负载识别）、Samsung Bespoke AI Laundry。[2][3]
- 冰箱交互屏：Samsung Family Hub（Android 平板门屏，食材识别）。[5][6]
- 烤箱/内置高端：BSH（Bosch/Gaggenau/Thermador）、Miele（Steam/Sense 联网烹饪）。[7][10]
- 本地可控冠军（唯一像样）：BSH Home Connect → hcpy 本地无云 → HA/MQTT。[11][12][13]
- 通用外挂法：ESPHome + 功率计量插座 / 门磁 / 振动传感器推断"洗衣完成/门开"，不碰厂商云。[workspace seed]

## VC Rising Stars
- 智能家电本身非 VC 热点，几乎无独立初创；动作集中于巨头并购与平台整合。
- LG 2024 末收购 Athom（Homey），把本地优先自动化引擎并入 ThinQ 生态。[VMR smart hub blog]
- Haier 通过收购集齐 GE Appliances / Fisher & Paykel / Candy / Casarte 七大品牌全球化。[9]
- 标准侧：Matter 逐步接入白电（当前仍以品牌云 + 平台为主），为未来跨品牌本地控制留口。[2][3]
- 开源侧仅有小众社区项目（hcpy、HA Home Connect），无商业化明星。[11][12]

## Candidate Keywords
lg thinq alternative / samsung smartthings appliance alternative / home connect home assistant / smart appliance without cloud / local smart appliance control / home assistant washing machine / home assistant dishwasher notification / hcpy home connect / bosch home connect local / control smart appliance offline / smart fridge without ads / turn off samsung fridge ads / esphome washing machine done sensor / matter appliances home assistant

## Deep Read Notes
### Source [5][6]: Samsung Family Hub 冰箱广告
Key data: 2025-11-03 起美国 idle 封面屏推广告，机型 $1,800–$3,000+；可 Settings→Advertisements 关闭或切 Art/Album 主题规避；Samsung 称"contextual/non-personal、不收集个人信息"。Ars 引：2023 年 LG 智能家电联网率 <50%。
Key insight: 屏幕家电（冰箱门屏）是新广告位；联网即让厂商获用户数据 + 广告收入。低联网率说明用户对"联网价值"不买账——正是本地/无云叙事切入点。

### Source [11][12][13]: 本地控制现状
Key data: HA 官方 Home Connect 集成走 developer.home-connect.com 云 OAuth + server-sent events（云）；BSH 系统设计上允许本地无云（TLS-PSK），社区 hcpy/hcpy2 首次云登录取密钥后可纯本地 websocket→MQTT。
Key insight: BSH 是白电里唯一"本地友好"厂商；LG/Samsung/Whirlpool 无本地 API，HA 集成均依赖厂商云。故本品类本地成熟度 = low。

## Gaps
- 各品牌无 brand-seo 报告；关键词精确量（volume/KD）留后续 brand-seo-research。
- 按品牌精确市场份额 % 缺免费公开数据（VMR 数字为估算[u]）。
- SmartThings / ThinQ 注册用户与"活跃联网家电数"缺官方口径。
- Matter 对白电（洗衣/洗碗/冰箱）的实际本地控制边界缺实测矩阵。
- hcpy 支持的 BSH 型号清单随固件变化，未对照。

## END
