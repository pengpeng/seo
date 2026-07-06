# iot/iot.md — IoT / 家居 / 穿戴竞品清单

> **闭源家居 / 穿戴硬件与生态**竞品清单（系统章：智能家居系统、个人健康平台；硬件章：语音中枢、音箱、摄像头、安防、门锁门铃、AI 录音硬件、健康可穿戴、照明、插座开关、温控、传感器网关、扫地机、家电、智能电视、婴儿监视、宠物摄像头、看护追踪、网联车、能源、智能眼镜），对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 7。AS_OF：2026-07-04。
>
> **归属**：这批多为闭源硬件 + 云生态（与 commerce 的软件 SaaS、hardware 的算力整机都不同），单列为 IoT 方向。偏软件、且已在 [commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md) 收录的产品（ElevenLabs、Deepgram、Otter、Fireflies、Granola 等）不在此重复；可自部署的开源平替（Home Assistant、Frigate、Music Assistant、Gadgetbridge、Nightscout 等）归 [market/](/Users/pengpeng/seo/directions/market)，此处只作「Olares 平替」列引用。
> **入选门槛**：面向**海外市场**的硬件 / 生态品牌（中国内销专属产品不列，中国起源但海外在售的如 EZVIZ/Aqara/SwitchBot/小米手环保留）；且满足其一——品类内装机 / 出货 / 注册领先 ｜ 细分赛道公认冠军 ｜ VC 明日之星（估值 / 融资显著或近 2 年并购 / IPO）。停滞、多年无出货、被收购且无独立对手的品牌不列。
> **两列口径**：`调研`列（章节标题 ✅）指向 [research/](/Users/pengpeng/seo/directions/iot/research) 的品类 deep-research 底稿；`报告`列 ⬜=待做**针对关键词的 brand-seo**（走 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)），产出落 [reports/](/Users/pengpeng/seo/directions/iot/reports)。目录树与命名见 [README.md](/Users/pengpeng/seo/directions/iot/README.md)。冲突 / 存疑数字标 `[u]`。
> **视角**：隐私优先——家居 / 穿戴是隐私最敏感面（常开麦克风、对外视角、24h 生物特征），每类均给出「数据不出设备」的 Olares 自托管落点。

---

## 一、系统章（软件中枢 / 聚合层）

> 系统层不是单个硬件，而是"谁做中枢 / 聚合，谁就掌握全屋行为或全量健康画像"——隐私视角下的最高敏感聚合点。

### 1. 智能家居系统 / 平台 — 调研 ✅ [smart-home-systems](/Users/pengpeng/seo/directions/iot/research/01-systems/smart-home-systems.md)
| 产品 / 平台 | 母公司 | 市场地位 / 事件 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Alexa（Home 编排面） | Amazon | 6 亿+ 累计 Alexa 设备；控制平台使用率 40% 居首 | HA on Olares（唯一本地中枢） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/alexa.md) |
| Google Home / Gemini for Home | Alphabet | 800M+ 连接设备；2025-10 全面 AI 化 | HA on Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/google-home.md) |
| SmartThings | Samsung | 4.3 亿+ 注册用户（2025-12） | HA on Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/smartthings.md) |
| Apple Home / HomeKit | Apple | 无官方装机；第三方估美 2026 ~23.5%[u] | HA on Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/apple-home.md) |
| Home Assistant | Open Home Foundation | 200 万+ 活跃家庭（本身即开源冠军） | **HA on Olares（自托管，双形态）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/home-assistant.md) |
| Hubitat | Hubitat | $150 级本地规则引擎、无订阅（prosumer 冠军） | HA on Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/hubitat.md) |
| Homey Pro | Athom（LG 2024 收 80%，~$61M[u]） | $399、50,000+ 设备、多协议 | HA on Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/homey-pro.md) |
| SwitchBot | OneRobotics | 2025-12 港交所 IPO $210.7M；向平台 / API 延伸 | HA on Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/switchbot.md) |
| Aqara | 绿米联创 | 2026-03 递表港交所；海外占比 66.5%；估值推算 ~$526M | HA on Olares（Zigbee2MQTT） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/smart-home-systems/aqara.md) |

> **细分冠军**：开源自托管=Home Assistant（+ 欧洲 KNX 备选 openHAB）；prosumer 本地中枢=Hubitat / Homey Pro；大厂云生态=Alexa（设备）/ Google Home（连接数）/ SmartThings（注册）/ Apple Home（隐私叙事）。**VC / 事件**：Homey→LG、SwitchBot IPO、Aqara IPO 递表。**争议**：谁"第一"取决于口径（设备出货 vs 连接设备 vs 注册用户），HA 是唯一可核实的"活跃自托管"冠军。HA 已有 [market 报告](/Users/pengpeng/seo/directions/market/reports)（302K 月流量基线）。

### 2. 个人健康系统 / 平台 — 调研 ✅ [health-platforms](/Users/pengpeng/seo/directions/iot/research/01-systems/health-platforms.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Apple Health / HealthKit | Apple | iOS 聚合层，longitudinal 锁定最强 | Fasten OnPrem（FHIR PHR） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/health-platforms/apple-health.md) |
| Google Health app + Health Connect | Alphabet | 原 Fitbit（2021 $2.1B 收购），~40M 活跃迁移 | Fasten OnPrem / Gadgetbridge | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/health-platforms/google-health.md) |
| Samsung Health | Samsung | Google Play 2.2B+ 安装；Galaxy 默认入口 | Fasten OnPrem | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/health-platforms/samsung-health.md) |
| Garmin Connect | Garmin | 活跃用户估 ~45M | OpenTracks / Traccar | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/health-platforms/garmin-connect.md) |
| Strava | 独立 | 180M 注册、2025 收入 $415M、估值 $2.2B | OpenTracks / Endurain | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/health-platforms/strava.md) |
| Function Health | Function Health | 2025-11 Series B $298M @ **$2.5B**；device-agnostic | 聚合层跑在 Olares | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/01-systems/health-platforms/function-health.md) |

> **细分冠军**：iOS 聚合=Apple HealthKit；Android=Google Health Connect；运动社交=Strava；耐力硬件=Garmin Connect；血检 / 长寿聚合新兴=Function Health；开源自托管 PHR=Fasten OnPrem + Nightscout（T1D CGM）。**去重**：Whoop / Ultrahuman 归第 9 类（硬件）。**争议 / 差距**：Apple/Samsung 无官方 MAU（多为第三方估）；无等价开源智能环 / CGM / 血压完全本地栈，Gadgetbridge 不支持 Apple Watch——诚实标注。数据导出词（`export apple health data`）买家意图强、竞争低。

---

## 二、硬件章（终端设备）

> 终端设备是数据采集点。常开麦克风（语音中枢 / 音箱）、对外视角（摄像头 / 门铃 / 婴儿 / 宠物）、24h 生物特征（可穿戴 / 录音 / 眼镜）、以及"时间序列即行为画像"的外围执行器与传感层（灯 / 插座 / 温控 / 传感器 / 扫地机 / 家电 / 电视 ACR / 看护 / 车联网 / 能源）——本章按细类逐一给出品牌与 Olares 落点。细类 3-9 为常开传感终端，10-22 为外围与敏感 IoT。

### 3. 语音中枢 / 语音助手 — 调研 ✅ [voice-hub](/Users/pengpeng/seo/directions/iot/research/02-hardware/voice-hub.md)
| 产品 / 平台 | 母公司 | 市场地位 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Alexa / Alexa+（Echo） | Amazon | 6 亿+ Alexa 设备；Alexa+ $19.99/月、Prime 捆绑 | HA Voice PE + Assist | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/voice-hub/alexa-echo.md) |
| Gemini for Home（Nest） | Alphabet | 2025-10 不可逆替换 Assistant；Premium $10/月 | HA Voice PE + Assist | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/voice-hub/gemini-for-home.md) |
| Siri（HomePod） | Apple | 主战场 iPhone/Watch；传与 Gemini 合作 | HA Voice PE + Ollama | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/voice-hub/siri.md) |
| Bixby / SmartThings | Samsung | 随 Galaxy / 家电分发 | HA Voice PE | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/voice-hub/bixby.md) |
| Sonos Voice Control | Sonos | 音乐 / 系统控制，隐私向，可与 Alexa 并存 | HA Voice PE | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/voice-hub/sonos-voice.md) |

> **细分冠军**：大厂云语音=Alexa / Gemini；音质+轻量=Sonos Voice；开源本地=**HA Voice PE + Assist**（Wyoming 连 openWakeWord/Whisper/Piper）+ Willow（ESP32）。**风险 / 差距**：常开麦克风=最高暴露面（三大助手均有听录音和解，Echo 2025-03 取消本地处理）；自托管开放域问答与 Alexa+/Gemini 有明显差距。核心机会词 `local/offline/private voice assistant`。（语音基建 ElevenLabs/Deepgram 属软件，归 [commerce](/Users/pengpeng/seo/directions/commerce/products.md)；豪宅集成 Josh.ai 2020 后停滞不列。）

### 4. 智能音箱 / 无线音频 — 调研 ✅ [smart-speakers](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-speakers.md)
| 产品 / 平台 | 母公司 | 市场地位 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Echo Dot（入门量王） | Amazon | Alexa 生态份额 36.12%（2025）；<$50 主力 | Music Assistant + Snapcast | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/echo-dot.md) |
| Nest Audio | Alphabet | $100 内音质向 | Music Assistant + Snapcast | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/nest-audio.md) |
| HomePod / mini | Apple | premium 单箱 + 多房间（Apple TV） | Music Assistant | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/homepod.md) |
| Sonos | Sonos | FY2025 $14.43 亿、1700 万+ 家庭（premium/多房间冠军） | **Music Assistant + Snapcast + Squeezelite** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/sonos.md) |
| JBL / Bose / UE | Samsung(Harman) / Bose / Logitech | 便携蓝牙梯队（JBL ~17.8% 收入） | 普通音箱串流 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/jbl-bose-ue.md) |
| Bluesound | Lenbrook | 发烧 hi-fi 无线流媒体（BluOS） | Music Assistant | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/bluesound.md) |
| Nothing / CMF | Nothing | 2025-09 Series C $2 亿 @ $13 亿；设计向大众硬件 | — | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-speakers/nothing-cmf.md) |

> **细分冠军**：入门=Echo Dot；premium=Sonos Era 100 / HomePod 2 / Echo Studio；多房间=Sonos；便携=JBL/UE/Bose；发烧=Bluesound；**自托管多房间开源栈=Music Assistant + Snapcast + Squeezelite**（"sonos alternative self hosted"的技术冠军）。**VC**：音箱本身几无独立新星，看点在 Nothing/CMF、Victrola（收 KLH）。核心机会词 `sonos alternative self hosted`、`multiroom audio self hosted`。（中国内销专属的小米 / 百度 / 天猫精灵不列。）

### 5. 家用摄像头 — 调研 ✅ [cameras](/Users/pengpeng/seo/directions/iot/research/02-hardware/cameras.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Ring | Amazon | 美国 / 全球口径连续 #1（门铃 halo + Alexa + 云订阅） | **Frigate + Reolink/ONVIF** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/ring.md) |
| Nest Cam | Alphabet | Google Home #2 | Frigate + PoE cam | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/google-nest-cam.md) |
| EZVIZ | Hikvision | 全球含 APAC 2023 份额 > Ring 2 倍 | Frigate | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/ezviz.md) |
| Arlo | Arlo（NYSE:ARLO） | FY2025 $529M、5.7M 付费账户、订阅毛利 ~84% | Frigate | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/arlo.md) |
| Wyze | Wyze | $30–40，累计融资 $146M、估值 ~$582M[u] | Frigate | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/wyze.md) |
| Eufy | Anker | HomeBase 本地 AI（隐私信誉受损） | Frigate | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/eufy.md) |
| Reolink | Reolink | PoE/电池/ONVIF/RTSP（Frigate 最常用源） | **Reolink → Frigate（本地无订阅）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/reolink.md) |
| UniFi Protect | Ubiquiti（NYSE:UI） | 本地 NVR、无订阅、prosumer 冠军 | UniFi 本地 / Frigate | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/unifi-protect.md) |

> **细分冠军**：云订阅生态=Ring / Nest；超值=Wyze / Tapo；本地 RTSP 无订阅=Reolink；prosumer 零订阅=UniFi Protect；**自托管 NVR 软件栈=Frigate**（~34k stars，内置 go2rtc，深度 HA 集成）。**VC 趋势**：不投新硬件摄像头，转投"摄像头之上的 AI 层"（B2B 软件如 Plumerai/Lumana/Coram，非本清单目标）。**风险**：执法级事件集中于此（Ring FTC $5.8M、Eufy 上传 AWS + NY AG $450K、Wyze 串号）。**Olares 落点极强**，Frigate 已有 [market 报告](/Users/pengpeng/seo/directions/market/reports)。核心机会词 `security camera without subscription`、`frigate nvr`、`ring alternative`。

### 6. 家庭安防系统 — 调研 ✅ [home-security](/Users/pengpeng/seo/directions/iot/research/02-hardware/home-security.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| ADT | ADT（NYSE:ADT） | 610 万订户、FY2025 $51.29 亿（专业监控规模冠军） | HA + 传感器 + Frigate | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/adt.md) |
| Vivint | NRG | ~190–200 万订户[u]，垂直整合 | HA + 传感器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/vivint.md) |
| SimpliSafe | SimpliSafe（GTCR） | 无合约标杆；2025-11 收购 EV >$25 亿 | HA + Z-Wave/Zigbee 传感器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/simplisafe.md) |
| Ring Alarm | Amazon | 品牌认知 43%、DIY 新购 28% | HA + Frigate（自监控） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/ring-alarm.md) |
| Wyze Home Monitoring | Wyze | ~$10/月超值 | HA + 传感器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/wyze.md) |
| Cove | Cove | ~$17.99/月，含 cellular；累计 $11.6M | HA + 传感器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/cove.md) |
| Abode | Nice S.p.A. | HomeKit/Matter/Z-Wave 多协议 | HA（Alarmo） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/home-security/abode.md) |

> **细分冠军**：专业监控=ADT + Vivint；DIY 自监控=Ring；DIY+可选 pro=SimpliSafe；超值=Wyze；budget pro=Cove；smart home/HomeKit 集成=Abode / Aqara。**结构转变**：camera-first（camera 61% vs alarm 30%）+ DIY 自装超专业安装（49% vs 42%）+ 无合约最强偏好（71%）。**差距**：自托管无 UL 认证 24/7 人工派警。核心机会词 `no monthly fee security system`、`home assistant alarm system`、`self hosted alarm system`。

### 7. 智能门锁 / 视频门铃 — 调研 ✅ [locks-doorbells](/Users/pengpeng/seo/directions/iot/research/02-hardware/locks-doorbells.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Schlage（Encode） | Allegion（NYSE:ALLE） | 北美零售领先 | HA + Z-Wave/Zigbee 本地控制 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/schlage.md) |
| Yale / August | Fortune Brands（NYSE:FBIN） | 2023 从 ASSA ABLOY 购入（$800M） | HA + Matter | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/yale-august.md) |
| ASSA ABLOY / Level | ASSA ABLOY | 门锁全球收入 #1；2024 收 Level 补 Home Key | HA + Matter | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/assa-abloy.md) |
| Aqara U100 / U200 | 绿米联创 | Matter/Apple Home Key 生态冠军 | HA + Matter | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/aqara-lock.md) |
| Nuki | Nuki | 欧洲；Series B $23.5M（Allegion 战投） | HA + Matter | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/nuki.md) |
| SwitchBot Lock / Ultraloq | OneRobotics / U-tec | retrofit 超值；SwitchBot 2025-12 IPO ~$206M | HA + 本地控制 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/switchbot-lock.md) |
| Ring 门铃 | Amazon | 视频门铃全球 24–31%[u]、美国户内 ~40% | Aqara G410 → Frigate/HA | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/ring-doorbell.md) |
| Nest 门铃 | Alphabet | 视频门铃 #2 | Frigate + PoE 门铃 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/nest-doorbell.md) |
| Aqara G410（本地门铃冠军） | 绿米联创 | 2K + 端侧人脸 + microSD/NAS/RTSP→HA | **Aqara G410（本地 + RTSP→Frigate）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/locks-doorbells/aqara-g410.md) |

> **细分冠军**：主流零售锁=Schlage/Yale/August；Matter/Apple 生态=Aqara/Level/Nuki；retrofit=SwitchBot/Ultraloq；视频门铃=Ring（美国 ~40%）/ Nest；**本地友好门铃冠军=Aqara G410**（无订阅、RTSP→HA）。**VC / 事件**：Level→ASSA ABLOY、SwitchBot IPO、Nuki（Allegion 战投）。**风险 / 差距**：门铃是最敏感对外视角（Ring 警局共享 2025 以 Axon 回归）；门锁有 Chirp/August 硬编码凭证 CVSS 9.1；**门锁无 Frigate 级统一开源方案**（自托管成熟度 ★★☆☆☆）。核心机会词 `aqara g410`、`ring doorbell alternative`、`home assistant smart lock`。

### 8. AI 录音硬件 / ambient 记忆 — 调研 ✅ [ai-recorders](/Users/pengpeng/seo/directions/iot/research/02-hardware/ai-recorders.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Plaud（品类唯一独立冠军） | Plaud | 2M+ 出货、软件 ARR $100M+、整体年化 ~$250M[u]，融资仅 ~$5M | **OpenClaw + Whisper + Ollama** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/ai-recorders/plaud.md) |

> **格局**：独立 AI 录音硬件创业窗口正在关闭——Limitless→Meta、Bee→Amazon、Humane 关停（设备 brick），唯 **Plaud** 以极端资本效率跑通规模化，成为品类唯一值得对标的独立硬件品牌。软件会议记录（Granola/Otter/Fireflies）属软件、归 [commerce](/Users/pengpeng/seo/directions/commerce/products.md)，不在此重复。**Olares 落点极强且差异化**：ambient 记忆 = Personal Agent 核心用例（OpenClaw + 本地 Whisper/Ollama，数据不出 Olares）。**风险**：全天录音 + 旁人未同意（one-party vs all-party 法冲突）。核心机会词 `plaud alternative`、`self hosted meeting transcription`、`meeting transcription without bot`。

### 9. 健康手环 / 可穿戴 — 调研 ✅ [wearables](/Users/pengpeng/seo/directions/iot/research/02-hardware/wearables.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Apple Watch | Apple | 智能手表全球 #1（Q1 2026 出货 23%） | Gadgetbridge（不支持 Apple Watch） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/apple-watch.md) |
| 小米手环 | 小米 | wearable band 年度口径全球第一（18%），全球在售 | **Gadgetbridge（BLE→本地）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/mi-band.md) |
| Garmin | Garmin（NASDAQ:GRMN） | 运动 GPS 冠军，FY2025 $7.25B | Gadgetbridge / OpenTracks | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/garmin.md) |
| Oura | Oura | 智能环出货 ~74%、估值 **$11B**、2026-05 机密 IPO | — | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/oura.md) |
| Whoop | Whoop | 恢复订阅冠军、估值 **$10.1B** | — | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/whoop.md) |
| Ultrahuman | Ultrahuman | 智能环挑战者；Series C ~$48M[u]；Ring + CGM | Gadgetbridge / Nightscout | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/ultrahuman.md) |
| Fitbit（Air） | Alphabet | 并入 Google Health | Gadgetbridge | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/fitbit.md) |
| Abbott Libre / Dexcom | Abbott / Dexcom | CGM 双寡头（美国 48.5% / 44.7%） | **Nightscout（自托管 CGM）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/cgm.md) |
| Omron / Withings | Omron / Withings | 血压 / 秤（Omron >4 亿累计；Withings 2025 盈利） | HA 集成 + 本地存储 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/omron-withings.md) |

> **细分冠军**：智能手表=Apple Watch；性价比手环=小米；运动 GPS=Garmin；健康环=Oura；恢复订阅=Whoop；CGM=Abbott/Dexcom；血压=Omron/Withings。**VC**：资本热点在智能环（Oura $11B、IPO）与订阅带（Whoop $10.1B）；Ultrahuman vs Oura 专利战致 Ring Air 美国禁售。**风险 / 差距**：24h 生物特征 B2B2C 货币化（保险 / 雇主）；无等价开源智能环 / CGM 传感器 / 血压完全本地栈——Gadgetbridge 不支持 Apple Watch，Nightscout 错配可致数据公网可访问。核心机会词 `oura ring alternative`、`gadgetbridge`、`nightscout cgm`、`self hosted fitness tracker`。

### 10. 智能照明 — 调研 ✅ [smart-lighting](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-lighting.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Philips Hue / WiZ | Signify（AMS:LIGHT） | 生态冠军；集团 FY2025 €57.65 亿、联网灯点 1.67 亿、控制口径 ~13.7%[u] | HA + Hue Bridge 本地 API v2 / ZHA / Zigbee2MQTT | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-lighting/philips-hue.md) |
| LIFX | Feit Electric | 无桥 Wi-Fi 高端、原生 LAN protocol（2022 被 Feit 收购） | HA 直连 LAN | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-lighting/lifx.md) |
| Nanoleaf | OneRobotics（SwitchBot 母公司） | 模块灯板；2026-05 ~$40.3M 被收购、FY2025 $30.9M | ESPHome / WLED（像素灯带） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-lighting/nanoleaf.md) |
| Govee | Govee（Shenzhen Intellirocks） | RGBIC/灯带 Amazon 走量；cloud-first，多型号仅云 | `govee_light_local`（基础）或换板刷 WLED | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-lighting/govee.md) |
| TP-Link Kasa / Tapo 灯 | TP-Link | 生态平价灯泡/灯带 | ESPHome / Tasmota | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-lighting/tp-link-tapo-lights.md) |
| DIY 像素灯带（WS2812B 等） | 开源 | WLED ~18.2k stars 事实标准 | **WLED / ESPHome（纯本地）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-lighting/diy-led-strips.md) |

> **细分冠军**：Zigbee 生态=Philips Hue（Bridge 本地 mesh）；无桥 Wi-Fi 本地=LIFX；DIY 灯带=**WLED**（可寻址像素事实标准）；编排=**HA 作唯一 Hub**。**VC / 事件**：Nanoleaf→OneRobotics（~$40.3M）、LIFX→Feit（老并购），照明是"红海 + 并购整合"非风投新星。**风险 / 差距**：灯光时间序列=作息画像；**Hue 自 2023 强推账号上云**、Govee 多型号仅云可用；Govee RGBIC/DreamView/music mode 无本地平替。核心机会词 `philips hue without account`、`local smart lighting`、`wled`、`smart bulbs home assistant`。（中国内销专属 Yeelight 不列。）

### 11. 智能插座 / 开关 — 调研 ✅ [smart-plugs](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-plugs.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| TP-Link Kasa / Tapo | TP-Link | Wi-Fi 畅销/全能（KP125M ~$20、Matter + 计量） | HA（Matter 本地模式）/ Tasmota | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/tp-link-kasa.md) |
| Shelly | Shelly Group SE（FRA:SLYG，原 Allterco） | 本地控制财务锚 FY2025 €1.497 亿 +40.3%、累计 23M+ 台、出厂可关云 | **Shelly 原生本地 MQTT/REST** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/shelly.md) |
| Lutron Caséta | Lutron（私营） | 墙面开关/调光可靠性冠军（Clear Connect 434MHz、无零线；至 2026 中无原生 Matter） | HA（Caséta 本地集成） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/lutron-caseta.md) |
| Sonoff | ITEAD | DIY / 可刷机冠军 | SonoffLAN 免刷机 / Tasmota / ESPHome | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/sonoff.md) |
| Amazon Smart Plug | Amazon | Alexa 生态入门 | HA + 本地插座替代 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/amazon-smart-plug.md) |
| Eve Energy | Eve Systems | Apple/Thread 隐私向、本地存储无订阅 | HA Matter Server 本地 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/eve-energy.md) |
| Belkin Wemo（反面教训） | Belkin | 2026-01-31 云关停、非 Thread/HomeKit 型号变哑 | 换 Shelly / Zigbee 插座 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-plugs/belkin-wemo.md) |

> **细分冠军**：Wi-Fi 全能=Kasa（Matter+计量）；本地优先=**Shelly**（原生 MQTT/REST）；墙面开关=Lutron Caséta；可刷机=Sonoff（SonoffLAN / Tasmota / ESPHome）；Apple/Thread=Eve。**VC / 事件**：Shelly Group（唯一高增长上市纯玩家，卖点 no-cloud）；Belkin 弃 Wemo=纯 Wi-Fi 云插座模型难续。**风险 / 差距**：计量插座功率时序=用电作息画像；**Wemo 云关停=功能剥夺**；Wi-Fi Matter 多默认绕云需手动开本地模式。核心机会词 `smart plug without cloud`、`smart plug home assistant`、`shelly`、`shelly vs sonoff`。

### 12. 温控 / 暖通 — 调研 ✅ [thermostats](/Users/pengpeng/seo/directions/iot/research/02-hardware/thermostats.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Google Nest | Alphabet | 北美份额 #1（~20–25%[u]）；Nest Learning 品类图腾 | HA + ESPHome OpenTherm / generic_thermostat | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/thermostats/google-nest.md) |
| ecobee | Generac（NYSE:GNRC） | 学习型 #2（~15–20%[u]）；2021 被 Generac 最高 $770M 收购 | HA + Zigbee TRV / Better Thermostat | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/thermostats/ecobee.md) |
| Honeywell Home | Resideo（NYSE:REZI） | 专业安装渠道（~12–17%[u]） | HA generic_thermostat | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/thermostats/honeywell.md) |
| Emerson Sensi | Emerson（NYSE:EMR） | 价值/上升（~8–12%[u]） | HA + ESPHome | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/thermostats/emerson-sensi.md) |
| tado° | tado°（私营；松下战投） | 欧洲龙头 550 万台、2024 ~$80M[u]、2026 盈利 | HA + Zigbee TRV + Better Thermostat | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/thermostats/tado.md) |
| Sensibo / Cielo | Sensibo / Cielo | 空调 IR 细分（云 API 导向） | Broadlink RM4 / ESPHome IR / SmartIR | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/thermostats/sensibo.md) |

> **细分冠军**：学习型/AI 节能=Nest / ecobee；专业安装=Honeywell Home；欧洲多系统=tado°；空调 IR=Sensibo；自托管栈=**HA + ESPHome OpenTherm + Better Thermostat**。**VC / 事件**：ecobee→Generac、tado° 转盈利 + 松下 €30M、Amazon $60 温控器压价。**风险 / 差距**：Nest Home/Away 融合运动+GPS 推断在家离家；HVAC 曲线暴露作息+建筑画像；**Nest/tado° 自适应节能学习算法（~22%）本地栈只能 PID/MPC 近似**。核心机会词 `local smart thermostat`、`home assistant thermostat`、`esphome opentherm`、`nest vs ecobee`。

### 13. 传感器 / 网关 — 调研 ✅ [sensors-hubs](/Users/pengpeng/seo/directions/iot/research/02-hardware/sensors-hubs.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| SmartThings | Samsung | 平台级中枢；2025-12 430M 注册、Matter 1.4（50 设备类型） | **HA on Olares（唯一本地 Hub）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/sensors-hubs/smartthings.md) |
| Aqara Hub M2 / M3 / M100 | 绿米 | 多协议 Hub（Zigbee+Thread+Matter+IR）、海外线 | HA + Zigbee2MQTT | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/sensors-hubs/aqara-hub.md) |
| Philips Hue Bridge | Signify | Zigbee 本地桥（2023 起强制账号） | ZHA / Zigbee2MQTT 直连绕桥 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/sensors-hubs/philips-hue-bridge.md) |
| Thread Border Router（Echo/HomePod/Nest Hub/eero） | Amazon / Apple / Google | 隐形 TBR（随生态附赠，凭据托管厂商云） | HA Matter Server + 自建 OTBR | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/sensors-hubs/thread-border-router.md) |
| Z-Wave 800 / Long Range（Zooz 等） | Silicon Labs / Zooz | 协议阵营（2026-01 已 125 款 ZWLR 认证） | Z-Wave JS + USB 棒 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/sensors-hubs/z-wave.md) |
| DIY 传感器（门窗/PIR/mmWave/温湿度/水浸） | 开源 | ESPHome 自制 | **ESPHome / Zigbee2MQTT（本地）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/sensors-hubs/diy-sensors.md) |

> **细分冠军**：平台级=SmartThings（规模最大、重云）；多协议本地 Hub=Aqara M3；Z-Wave DIY=Zooz；网络化 Zigbee 协调器=SLZB-06 / SkyConnect；**自托管唯一 Hub=Home Assistant**（Z2M 支持 5,473 款设备）——本品类是全 IoT 方向 Olares 平替最强的一类。**风险**：Hub=全屋数据单一聚合点；传感器融合=高精度行为画像；Hue 强制账号；隐形 TBR 把家默认接入某云生态。核心机会词 `local smart home hub`、`zigbee2mqtt`、`home assistant hub`、`matter server home assistant`。

### 14. 扫地机器人 — 调研 ✅ [robot-vacuums](/Users/pengpeng/seo/directions/iot/research/02-hardware/robot-vacuums.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Roborock | Roborock（688169.SH） | RVC 出货连续全球 #1；FY 营收 186.95 亿 +56.51% | **Valetudo（root 去云，地图留本地）** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/robot-vacuums/roborock.md) |
| Dreame | Dreame | 收入口径领先；拟港股 IPO 估值 ~$9.6B[u] | Valetudo（部分型号）/ 选无摄像头型号 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/robot-vacuums/dreame.md) |
| Ecovacs | Ecovacs（603486.SH） | 全球前五；**蓝牙劫持开摄像头/麦克风 + CVE-2024-52327** | 选无摄像头型号；HA MQTT + 防火墙断网 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/robot-vacuums/ecovacs.md) |
| iRobot Roomba | iRobot（2026-01 Chapter 11 归 Picea） | 曾龙头、已跌出前五；2020 测试图经 Scale AI 泄露 | Valetudo（老型号） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/robot-vacuums/irobot.md) |
| SharkNinja | SharkNinja（NYSE:SN） | FY2025 高增长多品类 | 选无摄像头型号 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/robot-vacuums/sharkninja.md) |
| Eufy | Anker | HomeBase 本地 AI（隐私信誉受损） | Valetudo / 防火墙断网 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/robot-vacuums/eufy-vacuum.md) |

> **细分冠军**：出货=Roborock（连续 #1）；收入=Dreame；去云技术冠军=**Valetudo**（root，地图不出云）。**VC / 事件**：Dreame 拟港股 IPO、iRobot Chapter 11 归 Picea、SharkNinja 多品类高增长。**风险 / 差距**：**LiDAR/视觉 SLAM 户型地图=最敏感空间数据**；Ecovacs 可被远程开麦克风摄像头；**Valetudo 可 root 型号矩阵随固件/PCB 变化**是本品类最大差距。核心机会词 `robot vacuum without cloud`、`valetudo`、`roborock vs roomba`、`robot vacuum privacy`。（小米 OEM 等中国内销专属不列。）

### 15. 智能家电 — 调研 ✅ [smart-appliances](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-appliances.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Bosch / Siemens Home Connect | BSH（FY2025 €15B） | **唯一可真本地**（hcpy / TLS-PSK） | **hcpy 本地 + HA** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-appliances/bosch-home-connect.md) |
| LG ThinQ | LG | 白电大厂生态、无本地 API | HA 有限集成（经云）/ ESPHome 外接传感器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-appliances/lg-thinq.md) |
| Samsung（SmartThings 家电） | Samsung | Family Hub 冰箱（2025-11 上广告争议） | HA 有限集成（经云） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-appliances/samsung-appliances.md) |
| Whirlpool | Whirlpool（NYSE:WHR，$15.5B） | 北美白电巨头、无本地 API | ESPHome 外接功率/门磁 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-appliances/whirlpool.md) |
| GE Appliances | Haier 旗下 | 北美 #1 | ESPHome 外接传感器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-appliances/ge-appliances.md) |
| Miele | Miele（€5.16B） | 高端 | HA 有限集成 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-appliances/miele.md) |

> **细分冠军**：真本地=**仅 BSH Home Connect（hcpy）**；其余（LG/Samsung/Whirlpool）无本地 API，只能 HA 经云或 ESPHome 外接功率/门磁传感器推断状态。**风险 / 差距**：洗衣/洗碗/冰箱使用时段=作息；OTA+账号绑定跨国云同步；Samsung 冰箱推广告。**成熟度 low**——本方向 Olares 自托管**最弱**的品类，写内容须诚实标注。核心机会词 `home connect home assistant`、`hcpy`、`smart appliance without cloud`。（中国内销专属海尔/美的定位不单列。）

### 16. 智能电视 / 流媒体（ACR）— 调研 ✅ [smart-tv](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-tv.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Roku | Roku（NASDAQ:ROKU） | 北美 TV-OS ~34% #1；FY2025 $47.4 亿、100M 家庭；撞库 15,363 | **Jellyfin** + Apple TV | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/roku.md) |
| Samsung Tizen | Samsung | 北美 TV-OS ~22%[u]；**德州 2026 ACR 和解须明示同意** | Jellyfin + TV 断网 / VLAN | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/samsung-tizen.md) |
| LG webOS | LG | ~10ms 截帧指纹 | Jellyfin + 关 Live Plus | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/lg-webos.md) |
| Amazon Fire TV | Amazon | 生态观看/广告 ID | Jellyfin + Apple TV | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/amazon-fire-tv.md) |
| Google TV | Alphabet | 全球 Android TV ~42%[u]；广告画像 | Jellyfin + Apple TV | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/google-tv.md) |
| Vizio SmartCast | Walmart（$23 亿收购） | **FTC 2017 ACR $2.2M**；CastOS 2029 拟北美 #1 | Jellyfin | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/vizio.md) |
| Apple TV 4K（无 ACR 例外） | Apple | 无 ACR，第三方须 ATT 授权 | **外接 Apple TV 4K 作唯一智能源** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-tv/apple-tv.md) |

> **细分冠军**：北美 TV-OS #1=Roku；媒体自托管=**Jellyfin** + Apple TV 4K（唯一无 ACR 主流盒）。**风险**：**ACR 逐秒/~500ms 截帧指纹化转卖**（含 HDMI）；Vizio FTC $2.2M、Samsung 德州 2026 和解、Roku 撞库 + 佛州儿童数据和解。**差距**：TV 本体 ACR 只能靠断网/VLAN 规避，非移除。核心机会词 `smart tv without acr`、`turn off acr`、`jellyfin`、`apple tv privacy`。

### 17. 婴儿监视器 — 调研 ✅ [baby-monitors](/Users/pengpeng/seo/directions/iot/research/02-hardware/baby-monitors.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Owlet | Owlet（NYSE:OWLT） | FY2025 $105.7M +35.4%；Q4 Circana 41% 金额份额 | Frigate + 本地 IP cam（无生命体征） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/baby-monitors/owlet.md) |
| Nanit | Nanit | 云 AI 婴儿监控；$50M 成长轮 | Frigate + 本地 IP cam | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/baby-monitors/nanit.md) |
| Cubo Ai | Cubo Ai | 云存储非 E2EE | Frigate + IP cam | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/baby-monitors/cubo-ai.md) |
| Miku | Miku | 无接触呼吸监测（状态存疑[u]） | 无生命体征开源平替 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/baby-monitors/miku.md) |
| VTech / Infant Optics | VTech / Infant Optics | 非 Wi-Fi DECT 基线（隐私更优） | 非联网基线本身即隐私向 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/baby-monitors/vtech.md) |
| 白牌（TRENDnet 类） | 多 OEM | FTC 2013 ~700 路公开；被黑语音骚扰 | Frigate + RTSP + VLAN 隔离 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/cameras/trendnet-whitebrand.md) |

> **细分冠军**：出货/份额=Owlet；智能云 AI=Nanit/Cubo；隐私基线=非 Wi-Fi DECT（VTech/Infant Optics）；自托管=**Frigate + 本地 IP cam**。**风险**：视频/呼吸经云解密非 E2EE；FTC TRENDnet ~700 路公开、白牌被黑语音骚扰。**差距（诚实标注）**：**无成熟开源"呼吸/心率/血氧"婴儿监测平替**——生命体征无法自托管。核心机会词 `baby monitor without wifi`、`self hosted baby monitor`、`baby monitor privacy`。

### 18. 宠物摄像头 / 喂食器 — 调研 ✅ [pet-cameras](/Users/pengpeng/seo/directions/iot/research/02-hardware/pet-cameras.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Furbo | Tomofun | 抛零食摄像头领先；**零点击账户接管 + 硬编码凭证 + 2025 SSRF CVE** | Frigate + 本地 IP cam + HA | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/pet-cameras/furbo.md) |
| Petcube | Petcube | 云录像 + ML + 第三方 SDK | Frigate + IP cam | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/pet-cameras/petcube.md) |
| Petkit | Petkit | 摄像头/喂食器（Agora/Alibaba Cloud SDK、Care+ 订阅） | Frigate + IP cam；喂食器 ESPHome DIY | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/pet-cameras/petkit.md) |
| PetSafe / Wopet 等喂食器 | PetSafe 等 | 自动喂食器（多云依赖） | ESPHome DIY 喂食器 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/pet-cameras/petsafe.md) |

> **细分冠军**：抛食摄像头=Furbo；云录像=Petcube/Petkit；摄像头自托管=**Frigate + 本地 IP cam + HA**。**风险**：Furbo 从 2018 零点击接管一路踩到 2025 SSRF CVE，是最强隐私叙事；Petkit/Petcube 云录像 + 第三方 SDK。**差距（诚实标注）**：摄像头可完全自托管，但**喂食器/treat-tossing 无成熟商用本地平替**，仅 ESPHome DIY（需焊接/3D 打印）。核心机会词 `furbo alternative`、`pet camera without subscription`、`frigate`。

### 19. 儿童 / 老人看护 — 调研 ✅ [safety-trackers](/Users/pengpeng/seo/directions/iot/research/02-hardware/safety-trackers.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| 儿童 GPS 表（Garmin Bounce / Xplora / TickTalk） | Garmin / Xplora 等 | 碎片化（Garmin Bounce ~12.4%[u]）；STALK 研究多款可远程监听 | Traccar 自托管定位 + 可控 tracker | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/wearables/garmin.md) |
| 老人告警（Medical Guardian / Bay Alarm / Life Alert） | 告警 SaaS | 订阅制、持续采集位置 | HA + mmWave 跌倒（非医疗级） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/safety-trackers/elder-alert.md) |
| Apple Watch Fall Detection | Apple | 跌倒/GPS/Medical ID 传 Apple & 911 | HA + mmWave（折中） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/safety-trackers/apple-watch-safety.md) |
| 物品 / 人追踪（AirTag / Tile / Jiobit） | Apple / Life360 | AirTag smart-tag ~69% 统治 | Traccar / 自选 GPS | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/safety-trackers/airtag.md) |

> **细分冠军**：儿童表=Garmin Bounce（碎片化）；老人告警订阅=Medical Guardian / Bay Alarm；物品追踪=AirTag（~69%）；自托管定位=**Traccar**（Apache-2.0，200+ 协议）。**风险**：STALK 研究 6 款儿童表 4 款可远程监听/定位；告警系收集持续位置。**差距（诚实标注）**：**开源无 24×7 派警坐席与 SOS 双向通话**，mmWave 跌倒非医疗认证。核心机会词 `self hosted gps tracker`、`traccar`、`kids gps watch privacy`。

### 20. 网联车 / 车机 — 调研 ✅ [connected-cars](/Users/pengpeng/seo/directions/iot/research/02-hardware/connected-cars.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Tesla | Tesla（NASDAQ:TSLA） | **员工传阅舱内/哨兵视频（Reuters）** | 无完整平替；关舱内摄像头、本地 Dashcam 无云 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/connected-cars/tesla.md) |
| GM OnStar | GM | **→LexisNexis 驾驶数据影响保费**；2024-03 停止共享 | 拒绝驾驶评分 app；Traccar 自管 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/connected-cars/gm-onstar.md) |
| Ford / Toyota-Lexus / Hyundai-Kia / VW | 各 OEM | **Mozilla 评汽车最差隐私（25 品牌全不及格、76% 可出售）** | 无完整平替；Traccar 车队自管 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/connected-cars/automakers-privacy.md) |
| 后装 OBD（Bouncie / Vyncs） | Bouncie / Vyncs | 位置/行程长期存云、与 UBI 保险打通 | Traccar + 自购 GPS | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/connected-cars/obd-tracker.md) |

> **细分冠军**：无自托管冠军——本品类 **Olares-fit 最低、成熟度 low**。**风险**：Tesla 员工传阅舱内视频；Mozilla「汽车最差隐私品类」；GM→LexisNexis 卖驾驶数据；Toyota/Lexus 230 万车数据暴露约 10 年。**差距（诚实标注）**：OEM 车联网**无完整开源平替**，只能关舱内摄像头 + 本地无云 dashcam + Traccar 自管。核心机会词 `car privacy`、`self hosted gps tracker`、`connected car data`。

### 21. 能源 / 电表 / 太阳能 — 调研 ✅ [energy-monitors](/Users/pengpeng/seo/directions/iot/research/02-hardware/energy-monitors.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Sense | Sense（Sense Labs） | 家庭能源 AI；高分辨率用电指纹→云 ML 识别电器 | HA Energy + Emporia Vue（ESPHome 去云） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/energy-monitors/sense-energy.md) |
| Emporia Vue | Emporia | 电路级监测、可刷 ESPHome | **Emporia Vue（ESPHome 本地）+ HA Energy** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/energy-monitors/emporia.md) |
| Shelly EM / Pro 3EM | Shelly Group SE | 原生本地计量 | **Shelly EM 本地 + HA Energy** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/energy-monitors/shelly-em.md) |
| Tesla Powerwall | Tesla | 储能安装口径 ~63%[u]；持续上报云 | HA 本地可读数据（厂商可限权） | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/connected-cars/tesla.md) |
| Enphase IQ | Enphase（NASDAQ:ENPH） | 微逆龙头 Q1 2026 $282.9M；IQ Gateway 上报云 | HA 集成本地读数 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/energy-monitors/enphase.md) |
| 智能电表 / AMI | Landis+Gyr / Itron / 公用事业 | **NILM 推断在家行为/再识别**；用户不可自托管 | 旁挂 CT 监测替代；仅读聚合数据 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/energy-monitors/smart-meter.md) |

> **细分冠军**：家庭能源 AI=Sense；电路级本地监测=**Emporia Vue（ESPHome）/ Shelly EM + HA Energy**；储能/微逆=Tesla Powerwall / Enphase。**风险**：Sense 用电指纹→云 ML 识别电器；智能电表 NILM 再识别在家行为。**差距（诚实标注）**：监测侧极强，但 **AMI 智能电表不可自托管**、**逆变器（Powerwall/Enphase）本地读数受厂商限权**。核心机会词 `home assistant energy monitor`、`emporia vue esphome`、`shelly em`、`sense alternative`。

### 22. 智能眼镜 / 第一视角 — 调研 ✅ [smart-glasses](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-glasses.md)
| 产品 / 平台 | 母公司 | 市场地位 / 融资 | Olares 平替（开源） | 报告 |
|------|------|---------|------------|------|
| Ray-Ban Meta | Meta（× EssilorLuxottica） | 2025 售 7M+、**IDC Q1 2026 份额 69.2%**；「Hey Meta」默认存云 1 年、2025-04 取消 opt-out | 无完整平替；记忆侧 OpenClaw + Whisper | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-glasses/ray-ban-meta.md) |
| Amazon Echo Frames | Amazon | 音频眼镜 | 无完整平替 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-glasses/echo-frames.md) |
| Snap Spectacles / SPECS | Snap | AR 第一视角 | 无完整平替 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-glasses/snap-spectacles.md) |
| Xreal（Aura 等） | Xreal | AR 显示路线 | 无完整平替 | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-glasses/xreal.md) |
| Brilliant Labs Frame | Brilliant Labs | **唯一开源硬件方向（MIT）** | **Brilliant Labs Frame（开源）+ 本地转写** | ✅ [报告](/Users/pengpeng/seo/directions/iot/reports/02-hardware/smart-glasses/brilliant-labs.md) |

> **细分冠军**：份额=Ray-Ban Meta（IDC 69.2% 一家独大）；开源硬件=**Brilliant Labs Frame（唯一 MIT 方向）**。**风险**：第一视角摄像+麦克风；「Hey Meta」语音默认存云 1 年、2025-04 取消 opt-out、旁人无从同意、LED 争议引 CA/PA 立法。**差距（诚实标注）**：**无完整开源平替**（camera-glasses 社交隐私 + 显示光学 + 零售无 OSS 对手），成熟度 low；记忆侧同 品类 8（OpenClaw + Whisper）。核心机会词 `ray-ban meta alternative`、`open source smart glasses`、`brilliant labs frame`。

---

## 统计与下一步

- **主清单**：2 大类（系统章 / 硬件章）/ 22 细类，收录面向海外市场的硬件 / 生态品牌。
- **两类产出**：品类 deep-research 底稿见 [research/](/Users/pengpeng/seo/directions/iot/research)（22 份，已就位）；针对关键词的 **brand-seo** 结果落 [reports/](/Users/pengpeng/seo/directions/iot/reports)（按 `<章>/<细类>/<brand>.md`，本轮留空占位）。
- **Olares 平替总览**：HA on Olares（家居中枢 / 语音 / 安防 / 门锁 / 灯 / 插座 / 温控 / 传感器）、Frigate（摄像头 / 门铃 / 婴儿 / 宠物）、Music Assistant + Snapcast（多房间音频）、Valetudo（扫地机去云）、Jellyfin（媒体规避 ACR）、Traccar（定位 / 看护 / 车联网）、HA Energy + Emporia Vue / Shelly EM（能源）、WLED / ESPHome / Zigbee2MQTT / Shelly（去云设备）、OpenClaw + Whisper + Ollama（AI 录音 / 眼镜记忆）、Gadgetbridge / Nightscout / Fasten OnPrem（健康）。这些开源平替多已在 Market，报告归 [market/](/Users/pengpeng/seo/directions/market)。
- **成熟度分层**：摄像头（Frigate）、家居中枢 / 传感器 / 灯 / 插座（HA + Zigbee2MQTT/ESPHome/WLED/Shelly）、扫地机（Valetudo）、能源监测（Emporia/Shelly EM）自托管最成熟；门锁、智能环 / CGM / 血压、婴儿生命体征、智能家电、网联车、智能电表、智能眼镜存在硬缺口或无完整平替，写内容须诚实标注。
- **下一步**：从本清单挑品牌，逐个走 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)（以产品官网为 brand，找 Olares 结合点），产出落到对应细类 `reports/` 子目录，再回填本清单平替 / 状态。优先切入"无订阅 / 本地 / 自托管"核心机会词。
