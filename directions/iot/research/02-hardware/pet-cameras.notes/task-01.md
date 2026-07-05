---
task_id: 01
role: 宠物摄像头/喂食器市场分析师
status: complete
sources_found: 17
source: WebSearch + WebFetch（2026-07-04）+ 媒体/敏感 IoT seed（task-01 源 [13][20]）
---

## Sources
[1] Interactive Pet Monitors 公司排名/份额（reportprime） | https://www.reportprime.com/interactive-pet-monitors-r3015/company | Source-Type: secondary-industry | As Of: 2024-2025 [u] | Authority: 4/10
[2] Pet Cameras Market 份额（marketintelo） | https://marketintelo.com/report/pet-cameras-market | Source-Type: secondary-industry | As Of: 2025 [u] | Authority: 4/10
[3] Automatic & Smart Pet Feeder Market（Precedence Research） | https://www.precedenceresearch.com/automatic-and-smart-pet-feeder-market | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[4] Automatic & Smart Pet Feeder Market（360iResearch） | https://www.360iresearch.com/library/intelligence/automatic-smart-pet-feeder | Source-Type: secondary-industry | As Of: 2026-02 | Authority: 5/10
[5] Smart Pet Care Market 主要玩家（growthmarketreports） | https://growthmarketreports.com/report/smart-pet-care-market-global-industry-analysis | Source-Type: secondary-industry | As Of: 2025 [u] | Authority: 4/10
[6] Furbo 零点击账户接管/预测 MAC/破损密码重置（lethalbit） | https://blog.lethalbit.com/remote-hacking-of-furbo-dog-camera/ | Source-Type: security | As Of: 2024-2025 | Authority: 7/10
[7] Furbo Mini/360 硬编码 root 密码（dead1nfluence advisories） | https://github.com/dead1nfluence/Furbo-Advisories/blob/main/Hardcoded-Password.md | Source-Type: security | As Of: 2025 | Authority: 6/10
[8] CVE-2025-11648 Furbo GATT/BLE SSRF（SentinelOne） | https://www.sentinelone.com/vulnerability-database/cve-2025-11648/ | Source-Type: security | As Of: 2025-10 | Authority: 7/10
[9] CVE-2025-11636 Furbo 360 Account Handler SSRF（SentinelOne） | https://www.sentinelone.com/vulnerability-database/cve-2025-11636/ | Source-Type: security | As Of: 2025-10 | Authority: 7/10
[10] PETKIT 隐私政策：Alibaba Cloud/Agora/第三方 SDK/Care+ 云录像 | https://m.petkit.com/app/about/policy/en.html | Source-Type: policy | As Of: 2025 | Authority: 7/10
[11] Petcube 隐私政策：云存储 + ML + 第三方 SDK | https://petcube.com/en-gb/docs/privacy-policy/ | Source-Type: policy | As Of: 2025 | Authority: 6/10
[12] Furbo/Tomofun 融资档案（PitchBook） | https://pitchbook.com/profiles/company/157938-40 | Source-Type: other | As Of: 2026 | Authority: 6/10
[13] Tomofun 背景：Victor Chang 创办、趋势科技 Steve Chang mentor（LinkedIn） | https://www.linkedin.com/company/tomofun | Source-Type: other | As Of: 2026 [u] | Authority: 5/10
[14] Furbo Indiegogo 众筹 $510K（TaiwanPlus） | https://www.taiwanplus.com/shows/tech/innovation/220708005/addressing-the-guilt-of-pet-owners-tomofun-furbo-dog-sitter-goes-global | Source-Type: journalism | As Of: 2022-07 | Authority: 6/10
[15] pricklyguy/pet-feeder-esphome（ESP32 + HA 本地喂食器） | https://github.com/pricklyguy/pet-feeder-esphome | Source-Type: community | As Of: 2025 [u] | Authority: 5/10
[16] Botmonster：$20 ESPHome DIY 喂食器 vs PetSafe/PETLIBRO | https://botmonster.com/smart-home/build-smart-pet-feeder-esphome-servo-motor/ | Source-Type: other | As Of: 2025 [u] | Authority: 4/10
[17] blakeblackshear/frigate（自托管 NVR 事实标准） | https://github.com/blakeblackshear/frigate | Source-Type: community | As Of: 2026-06 | Authority: 9/10

## Findings
- 宠物摄像头市场高度碎片化，Furbo(Tomofun) 与 Petcube 长年领跑投食摄像头细分；reportprime 口径给 Furbo ~20.3% / Petcube ~17.5% / Petkit ~11.3%（2024 营收 $32.5M/$28M/$18M）。[1][2]
- 投食摄像头(treat-tossing)子类 Furbo 18-22% 领先，Petcube 14-18%，Wyze 9-12%，Eufy 6-8%——非专属宠物玩家（Amazon Blink/Google Nest/Wyze/Eufy）用通用摄像头 + 生态挤入。[1][2]
- 智能喂食器市场口径分歧极大：360iResearch 2025 仅 ~$0.97B（窄口径，纯 app 联网），Precedence ~$2.61B→2035 $7.56B（CAGR 11.22%，APAC 主导），The Business Research ~$1.96B(2025)。以"能否自托管"看，喂食器远比摄像头缺开源平替。[3][4]
- 智能宠物护理大盘玩家：PetSafe(Radio Systems)、Sure Petcare(MSD/Antelliq)、Petkit、Petcube、Tractive(GPS)、Litter-Robot(AutoPets)、Whistle(Mars)。软件/云侧归 commerce。[5]
- Furbo 安全信誉重创：2018 起 lethalbit 披露"零点击账户接管"——预测性 MAC（Chicony B0:C0:90 前缀可爆破）+ 无设备-账户绑定 + 破损密码重置返回明文 token，可访问任意账户照片/音频。[6]
- 2025 新增 CVE：Furbo Mini/360 硬编码 root 密码（只读分区不可改，UART 拿 shell，二手设备高危）[7]；CVE-2025-11648 GATT/BLE SSRF（改 TF_FQDN.json 配置端点）[8]；CVE-2025-11636 Account Handler 远程 SSRF。[9]
- Petkit：视频经 Agora 传输、存 Alibaba Cloud，Care+ 仅事件录像 + 云端 AI 视觉分析 + 订阅自动扣款；App 内嵌微博/微信/高德等大量第三方 SDK。[10]
- Petcube：云存储 + ML + 第三方 SDK（seed 已录）。[11]
- Olares 摄像头平替成熟（Frigate + 本地 IP cam + HA），但喂食器只有 ESPHome DIY 路线（3D 打印 auger + 舵机/步进 + HA 排程），无成熟商用本地投食摄像头；treat-tossing 无开源平替。[15][16][17]

## Market Leaders
- 投食摄像头：Furbo(Tomofun，Taipei/Seattle) / Petcube(San Francisco) / Petkit(Shanghai)。[1][2]
- 通用摄像头挤入宠物场景：Amazon Blink、Google Nest、Wyze、Eufy(Anker)。[2]
- 喂食器/宠物护理大盘：PetSafe(Radio Systems)、Sure Petcare(MSD)、WOpet、Wagz、PETLIBRO、Skymee、Pawbo(Acer)。[1][5]
- GPS 追踪（相邻，非本章重点）：Tractive、Whistle(Mars)、Garmin。[5]

## Segment Champions
- 投食摄像头体验冠军：Furbo（丢零食 + 吠叫警报 + Furbo Dog Nanny 订阅 AI）。[13][14]
- 行为 AI/欧洲市场冠军：Petcube（宽角 + 夜视 + 行为分析）。[2]
- IoT 生态/喂食器一体冠军：Petkit（喂食器 + 饮水机 + 摄像头 + Care+ 云）。[10]
- 价值/入门：Wyze、WOpet、PETLIBRO。[1][16]
- 自托管平替：Frigate(+go2rtc) + Reolink/Amcrest/ONVIF 本地摄像头（摄像头侧）；ESPHome DIY 喂食器 + HA 排程（喂食器侧）。[15][16][17]

## VC Rising Stars
- Furbo/Tomofun：2014/2015 由 Victor Chang 创办、趋势科技 Steve Chang 任 mentor；2016 Indiegogo 众筹 $510K（超募 906%），PitchBook 公开档案仅见众筹一轮，无公开 Series C 估值[u]。[12][13][14]
- Petcube：VC-Backed（PitchBook 标注），曾与 Logitech 有渊源[u]。[12]
- 大盘被并购：Sure Petcare→MSD/Antelliq、Whistle→Mars、Litter-Robot→AutoPets——巨头整合宠物护理。[5]
- 开源双轨：Frigate + ESPHome DIY 喂食器 vs 各厂商云。[15][16][17]

## Candidate Keywords
furbo alternative / petcube alternative / petkit alternative / pet camera without subscription / self hosted pet camera / diy pet camera / frigate pet detection / home assistant pet camera / diy pet feeder / esphome pet feeder / automatic cat feeder home assistant / pet feeder without wifi / pet feeder no subscription / furbo vs petcube / petkit vs petlibro / best pet camera no monthly fee / pet camera privacy / furbo hacked

## Deep Read Notes
### Source [6][7][8][9]: Furbo 安全链
Key data: 零点击账户接管（预测 MAC + 破损重置 token）；硬编码 root（UART）；两枚 2025 SSRF CVE（GATT/BLE + Account Handler）。
Key insight: Furbo 是全 IoT 章少数"从 2018 一路踩到 2025"的品牌，"furbo hacked / furbo alternative"买家意图强，直接承接隐私叙事。

### Source [3][4]: 喂食器市场口径
Key data: 360iResearch $0.97B(2025) vs Precedence $2.61B→$7.56B(2035, CAGR 11.22%, APAC 主导)。
Key insight: 差异来自"纯 app 联网喂食器"vs"含基础定时分食器"；喂食器是 IoT 章里平替最弱的一类。

### Source [15][16]: ESPHome DIY 喂食器
Key data: ESP32/ESP8266 + 舵机/步进 + 3D 打印 auger，HA 排程/份量/日志，~$20 vs PetSafe ~$150。
Key insight: 本地喂食器存在但仅 DIY（需焊接/3D 打印），无成熟商用本地投食摄像头——诚实差距。

## Gaps
- 各家精确份额 % 均来自二手行研（marketintelo/reportprime 权威性偏低[u]），无 SA/TechInsights 级别一手；Furbo/Petcube/Petkit 私营营收多为估算。
- 喂食器市场规模 3-4 家口径相差 ~2.7×，取值需注明来源。
- Tomofun 无公开 VC 轮次/估值（仅众筹），Petcube 融资细节未开源核实[u]。
- 无成熟"本地投食摄像头"商用产品；treat-tossing 无开源平替；ESPHome 喂食器需硬件动手能力，非普通用户路径。
- Olares Market 仅有 Frigate/HA 报告，ESPHome 喂食器无打包 app。

## END
