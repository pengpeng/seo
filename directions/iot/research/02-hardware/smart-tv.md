# 智能电视 / 流媒体（ACR）竞品与关键词（IoT 方向 · 品类 16）

> 研究日期: 2026-07-04 | 来源: 原家居分册 seed 笔记（7 源）+ 本轮 Web 研究（14 源）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 智能电视操作系统与流媒体盒/棒（smart TV OS & streaming boxes/sticks），核心议题 = ACR（automatic content recognition，自动内容识别）逐秒截帧观看追踪。软件层的流媒体服务（Netflix/Disney+ 等）不计入硬件；开源 Jellyfin 仅出现在"平替"列。归属 IoT 新方向"硬件章"。发现笔记见 [smart-tv.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-tv.notes)。

## 摘要
智能电视/流媒体是 IoT 硬件章里"商业模式即监控"最典型的品类——电视厂商已从卖硬件转向卖广告与观看数据。**ACR 对屏幕内容（含 HDMI 外接输入）以 ~500ms（Samsung）/~10ms（LG）间隔截帧指纹化，识别你在看什么并转卖给广告 broker**，这是整条价值链的引擎 [N11]。市场高度集中：北美 TV OS 由 Roku（1Q25 ~34%）、Samsung Tizen（~22%）、Amazon Fire TV 与 Vizio CastOS（各 ~12–14%）四家主导，全球则 Android/Google TV（~42% 含中国分叉）与 Tizen（~17%）领先 [N1][N2]。Walmart 2024 以 $23 亿收购 Vizio、正把 Onn 电视从 Roku 换成 CastOS，Omdia 预测 CastOS 到 2029 将成北美出货第一 [N1][N2]。上市财务锚是 Roku：FY2025 净收入 $47.4 亿、平台收入 $41.4 亿（其中广告 $23.3 亿、订阅 $18.2 亿）、全球流媒体家庭破 1 亿、年流媒体时长 1456 亿小时——硬件几乎不赚钱，钱来自 ACR + 广告 [N5][N6]。**隐私是头条**：Vizio 因 ACR 被 FTC 罚 $2.2M（2017）[N7]；Samsung 因未明示同意即启用 ACR 被德州 AG 起诉、2026-02 和解须"明示 opt-in 同意 + 清晰披露"[N8][N9]；Roku 撞库 15,363 账户 + 佛州儿童数据和解 [N12][N13]。**唯一例外：Apple TV 4K 不预装 ACR**，被隐私圈公认为最干净的流媒体前端 [N10]。**Olares 落点**：Jellyfin（自托管媒体库）+ 电视本体断 WAN / IoT VLAN 隔离 + Apple TV 4K 作唯一"智能源" [N10][N14]。

## 1. 品类概述
本品类分两层：① **TV OS/一体机**（Samsung Tizen、LG webOS、Vizio CastOS、Hisense Vidaa、Google TV/Android TV、Roku TV OS）；② **外接流媒体盒/棒**（Roku、Amazon Fire TV、Google Chromecast/TV Streamer、Apple TV 4K）。两层都以"内容入口 + 广告平台"为核心商业模式，硬件常以成本价甚至亏本出售，靠 ACR 观看数据 + CTV 广告 + FAST 频道回本。隐私视角下这是暴露面最"隐形"的一类：追踪对象不是你输入的内容，而是**屏幕上显示的一切（含游戏机、蓝光机、有线盒等 HDMI 输入）**，用户几乎无感知。全球 CTV 市场持续增长，Roku/Amazon Fire TV/Google Chromecast 三家合计约占全球 55% 份额，Apple TV/Samsung/LG 合计约 30% [N4]。

## 2. 市场领导者 / top 畅销
| 口径 | 领导者 | 锚点 |
|------|--------|------|
| 北美 TV OS（出货） | Roku ~34% / Samsung Tizen ~22% / Fire TV ~12–14% / Vizio CastOS ~12–13% | Omdia 1Q25；Roku 领跑近 6 年 [N1][N2] |
| 全球 TV OS（出货） | Android/Google TV ~42%（含中国分叉）/ Tizen ~17% | Omdia 2025；2029 前 Android 仍第一 [N1] |
| 北美 CTV 设备（SOV） | Roku 32% / Fire TV 16% / Apple 15% / Samsung 14% / LG 10% | Pixalate Q4 2025 [N3] |
| EMEA / APAC | Samsung 24%（EMEA）/ Xiaomi 15%（APAC） | Pixalate Q4 2025 [N3] |
| 上市财务锚 | Roku（NASDAQ:ROKU） | FY2025 净收入 $47.4 亿、100M+ 家庭、1456 亿流媒体小时 [N5][N6] |
| 无 ACR 例外 | Apple TV 4K | tvOS 不预装 ACR，第三方 app 须 ATT 授权 [N10] |

母公司/归属：Samsung、LG、Amazon（Fire TV）、Google（Chromecast/Google TV/Android TV）、Roku、**Vizio→Walmart**（2024 年 $23 亿收购，CastOS 将上 Onn 自有品牌）、Hisense（Vidaa）、Apple [N1][N2]。

**置信度: Medium**（TV OS/CTV 份额随口径（出货 vs 广告 SOV vs 安装量）差异大；Roku 财务为官方 10-K/股东信高可靠，其余市场份额为研究机构口径，部分需付费全量[u]）。

## 3. 细分赛道冠军
- **北美 TV OS 出货冠军**：Roku TV OS——授权给 TCL/Hisense/Onn 等价值品牌，1Q25 北美 ~34%、全球流媒体家庭 100M+ [N2][N5]。
- **零售媒体新贵**：Vizio CastOS（Walmart）——$23 亿收购后强推 Onn 自有品牌，Omdia 预测 2029 北美出货第一（~30%）[N1][N2]。
- **高端一体机冠军**：Samsung Tizen（全球出货量最大电视厂）+ LG webOS（已对第三方开放授权）[N1]。
- **广告变现冠军**：Roku——FY2025 广告收入 $23.3 亿（占平台 ~56%），视频广告曝光 +68% [N6]。
- **全球 OS 装机冠军**：Android/Google TV（含分叉，~42% 出货、装机超 2.5 亿设备[u]）[N1]。
- **流媒体棒/盒销量冠军**：Amazon Fire TV Stick 系列（棒类全球份额 ~31%[u]）+ Roku（~17%[u]）+ Google Chromecast（~19%[u]）[N4]。
- **隐私自托管前端冠军**：**Apple TV 4K**（无 ACR、tvOS 无 OS 首屏广告、ATT 拦截第三方追踪）——隐私圈事实标准 [N10]。

**置信度: Medium**（各机构棒/盒份额口径不一、多为市场报告估算[u]；Roku 广告数据官方可靠）。

## 4. VC 圈明日之星
本品类硬件由大厂/平台垄断，**没有独立硬件"新星"**——资本与战略重心集中在"电视即广告/零售媒体网络"：
- **零售媒体整合**：Walmart（Vizio/CastOS/Onn）与 Amazon（Fire TV + Amazon DSP）把电视变成 retail media network；Amazon–Roku 2025 达成 8000 万认证美国家庭的 DSP 联播，是全美最大登录态 CTV 足迹 [N2]。
- **广告栈深化**：Roku 2025 推出开放自助 Roku Ads API、Roku Data Cloud，并与 Amazon DSP/Nielsen/FreeWheel 打通 [N5][N6]。
- **FAST 频道**：免费广告支持流媒体（The Roku Channel、Samsung TV Plus、Tubi）是增长引擎，进一步依赖 ACR 定向。
- 开源侧：**Jellyfin**（GPL，自托管媒体库）与商业 TV OS 形成"自有媒体库 + 无广告 vs 云观看画像"双轨 [N14]。

**置信度: Medium**（零售媒体/广告整合趋势可靠，均为大厂战略而非 VC 融资事件）。

## 5. 候选产品关键词
品牌替代：`roku alternative`、`fire tv alternative`、`google tv alternative`、`vizio alternative`。
去 ACR / 隐私（核心机会）：`smart tv without acr`、`turn off acr`、`disable acr samsung`、`smart tv spying`、`smart tv privacy`、`stop smart tv tracking`、`apple tv privacy`、`dumb tv alternative`。
自托管媒体：`jellyfin`、`self hosted media server`、`plex alternative`、`jellyfin apple tv`。
选购/对比：`apple tv vs roku privacy`、`best streaming device privacy`、`samsung vs lg acr`、`roku data collection`。

> Olares Market 已有 Jellyfin 报告，`jellyfin`、`smart tv without acr`、`apple tv privacy`、`self hosted media server` 是与现有资产最贴合的切入。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **ACR 逐秒/~500ms 截帧指纹化转卖**：Samsung ~500ms、LG ~10ms 对屏幕内容（含 HDMI 外接输入）截帧指纹化，识别观看内容用于广告分段/转卖给数据 broker，用户多在开机 setup 时"一路 I Agree"被默认启用 [N9][N11]。
- **执法级事件**：① **Vizio FTC $2.2M**（2017）——未告知即对 1100 万台启用 Inscape 逐秒观看史 + IP 转卖 [N7]；② **Samsung 德州 2026-02 和解**——AG Paxton 2025-12 起诉其 ACR 为"数字入侵者"，用 200+ 次点击的 dark pattern 把 ACR 藏在"Viewing Information Services"名下、只说采"signatures"，和解要求**明示 opt-in 同意 + 清晰披露**，且 AG 声明将继续起诉其他厂商 [N8][N9]；③ **Roku** 撞库 15,363 账户被接管 [N12] + 佛州儿童数据和解 [N13]。
- **无 ACR 例外**：**Apple TV 4K 不预装 ACR**（Apple 向 Ars 确认），且 setup 默认关位置/语音/分析、tvOS 无首屏广告、tvOS 14.5+ 强制第三方 app ATT 授权——是唯一主流"干净"流媒体前端；但 Apple TV app 的个性化推荐/播放历史默认开、Apple 正探索广告 tier，非绝对 [N10]。
- **Olares 平替栈**：媒体库 → **Jellyfin on Olares**（GPL，自建电影/剧集/音乐库，无云观看画像、无订阅）[N14]；前端 → **Apple TV 4K** 装 Jellyfin app 作唯一"智能源"、或用 dumb display + Apple TV；网络 → **电视本体断 WAN / 划入 IoT VLAN 隔离**（关 ACR/Viewing Information Services、禁 UPnP、屏蔽 ACR 上报域名）；远程 → Tailscale/VPN 访问 Jellyfin 不端口暴露。核心叙事：**买智能电视 = 买一台会看你看什么的广告机；把电视降级为"哑屏"，智能与内容交给自托管 Jellyfin + 无 ACR 的 Apple TV**。

**置信度: High（Jellyfin + 断网/VLAN + Apple TV 是成熟且被隐私圈公认的路径）**。

## 7. 核心争议 / 反方 / 参考

**核心争议**：① "关掉 ACR 是否够"——多数 TV OS 仍在首屏、FAST 频道、语音助手层继续收集，且 ACR 开关埋得深、措辞误导（Samsung 200+ 点击 dark pattern），关闭需主动操作，普通用户几乎不会做 [N9][N11]。② "Apple TV 是否真干净"——它不预装 ACR，但 Enswers 创始人向 Ars 指出技术上 Apple 可通过软件更新加 ACR；且 Apple 正探索 Apple TV+ 广告 tier，未来存变数 [N10]。③ 份额口径之争——TV OS 出货（Roku 领跑北美、Android 领跑全球）、CTV 广告 SOV（Pixalate）、装机量三种口径给出不同"第一"[N1][N2][N3]。

**反方解释**：智能电视 ACR + 广告补贴让硬件更便宜、"免费内容 + 个性化推荐"体验对普通用户显著方便，多数人默认接受观看数据换免费。自托管路径（Jellyfin 建库 + Apple TV + VLAN 隔离）需要布线/网络隔离/媒体整理知识与额外购置 Apple TV，属技术用户路径，且会失去官方 app 的即开即用与新片同步。

**参考文献**（Source-Type · As Of）
- [N1] Omdia/Business Wire, CastOS to Dominate North America TV OS (2025 & 2029 share). secondary-industry · 2025-10. https://www.businesswire.com/news/home/20251029451188/en/Omdia-CastOS-to-Exceed-15-Million-Shipments-Set-to-Dominate-North-Americas-TV-OS-Market
- [N2] Omdia, The smart TV OS shake-up (1Q25 share; Walmart→Vizio on Onn; Amazon-Roku DSP). secondary-industry · 2025-07. https://omdia.tech.informa.com/blogs/2025/july/the-smart-tv-os-shakeup-amazon-walmart-and-the-coming-age-of-shoppable-media
- [N3] Pixalate, Q4 2025 CTV Device Market Share Report. secondary-industry · 2026-01[u]. https://www.pixalate.com/blog/pixalates-q4-2025-connected-tv-ctv-device-market-share-report
- [N4] Future Market Insights, Connected TV Market Share Analysis. secondary-industry · 2025-2026[u]. https://www.futuremarketinsights.com/reports/connected-tv-market-share-analysis
- [N5] Roku, FY2025 Shareholder Letter (100M households, #1 by hours). official · 2026-02. https://image.roku.com/bWFya2V0aW5n/4Q25-Shareholder-Letter.pdf
- [N6] Roku, 10-K/Segment Recast (net rev $4.74B, Platform $4.14B, Ad $2.33B, Sub $1.82B, 145.6B hours). official · 2026-06. https://www.sec.gov/Archives/edgar/data/1428439/000162828026044373/roku-20260618_d2.htm
- [N7] FTC, Vizio to Pay $2.2M ACR Settlement. official · 2017-02. https://www.ftc.gov/news-events/news/press-releases/2017/02/vizio-pay-22-million-ftc-state-new-jersey-settle-charges-it-collected-viewing-histories-11-million
- [N8] Texas AG, Paxton Secures Agreement with Samsung (express consent). official · 2026-02. https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-secures-major-agreement-samsung-ensure-texans-are-protected-smart-tvs
- [N9] BleepingComputer, Samsung TVs to Stop Collecting Texans' Data (lawsuit detail, 200+ clicks, VIS). journalism · 2026-02. https://www.bleepingcomputer.com/news/security/samsung-tvs-to-stop-collecting-texans-data-without-express-consent/
- [N10] Ars Technica, Why Apple TVs Are Privacy Advocates' Go-To (no ACR). journalism · 2025-06. https://arstechnica.com/gadgets/2025/06/all-the-ways-apple-tv-boxes-do-and-mostly-dont-track-you/
- [N11] PCWorld, Samsung & LG Smart TVs Are Watching You (~500ms/~10ms fingerprint). journalism · 2024. https://www.pcworld.com/article/2918574/samsung-and-lg-smart-tvs-are-watching-you-heres-how-to-stop-it.html
- [N12] Piracy Monitor, Roku Credential Stuffing 15,363 Accounts. journalism · 2024-03. https://piracymonitor.org/roku-hit-with-credential-stuffing-attack-locking-users-out-of-accounts/
- [N13] LegalReader, Florida-Roku Children's Digital Privacy Settlement. journalism · 2025[u]. https://www.legalreader.com/florida-roku-announce-settlement-in-childrens-digital-privacy-lawsuit/
- [N14] Jellyfin, Free Software Media System (self-hosted). community · 2026-06. https://jellyfin.org/
