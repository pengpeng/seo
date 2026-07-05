---
task_id: 01
role: 智能电视 / 流媒体市场分析师
status: complete
sources_found: 14
source: 原家居分册 seed 笔记 + 本轮 Web 研究（WebSearch×3 + WebFetch×2）
as_of: 2026-07-04
---

## Sources
[N1] Omdia/Business Wire: CastOS to Dominate North America TV OS | https://www.businesswire.com/news/home/20251029451188/en/Omdia-CastOS-to-Exceed-15-Million-Shipments-Set-to-Dominate-North-Americas-TV-OS-Market | Source-Type: secondary-industry | As Of: 2025-10 | Authority: 8/10
[N2] Omdia: The smart TV OS shake-up (Amazon/Walmart) | https://omdia.tech.informa.com/blogs/2025/july/the-smart-tv-os-shakeup-amazon-walmart-and-the-coming-age-of-shoppable-media | Source-Type: secondary-industry | As Of: 2025-07 | Authority: 8/10
[N3] Pixalate Q4 2025 CTV Device Market Share Report | https://www.pixalate.com/blog/pixalates-q4-2025-connected-tv-ctv-device-market-share-report | Source-Type: secondary-industry | As Of: 2026-01 [u] | Authority: 6/10
[N4] Future Market Insights: Connected TV Market Share | https://www.futuremarketinsights.com/reports/connected-tv-market-share-analysis | Source-Type: secondary-industry | As Of: 2025-2026 [u] | Authority: 5/10
[N5] Roku FY2025 Shareholder Letter | https://image.roku.com/bWFya2V0aW5n/4Q25-Shareholder-Letter.pdf | Source-Type: official | As Of: 2026-02 | Authority: 9/10
[N6] Roku 10-K / Segment Recast (SEC) | https://www.sec.gov/Archives/edgar/data/1428439/000162828026044373/roku-20260618_d2.htm | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[N7] FTC: Vizio to Pay $2.2M ACR Settlement | https://www.ftc.gov/news-events/news/press-releases/2017/02/vizio-pay-22-million-ftc-state-new-jersey-settle-charges-it-collected-viewing-histories-11-million | Source-Type: official | As Of: 2017-02 | Authority: 10/10
[N8] Texas AG: Paxton–Samsung ACR Agreement | https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-secures-major-agreement-samsung-ensure-texans-are-protected-smart-tvs | Source-Type: official | As Of: 2026-02 | Authority: 9/10
[N9] BleepingComputer: Samsung TVs to Stop Collecting Texans' Data | https://www.bleepingcomputer.com/news/security/samsung-tvs-to-stop-collecting-texans-data-without-express-consent/ | Source-Type: journalism | As Of: 2026-02 | Authority: 7/10
[N10] Ars Technica: Why Apple TVs Are Privacy Advocates' Go-To (no ACR) | https://arstechnica.com/gadgets/2025/06/all-the-ways-apple-tv-boxes-do-and-mostly-dont-track-you/ | Source-Type: journalism | As Of: 2025-06 | Authority: 8/10
[N11] PCWorld: Samsung & LG Smart TVs Are Watching You (~500ms/~10ms) | https://www.pcworld.com/article/2918574/samsung-and-lg-smart-tvs-are-watching-you-heres-how-to-stop-it.html | Source-Type: journalism | As Of: 2024 | Authority: 7/10
[N12] Piracy Monitor: Roku Credential Stuffing 15,363 | https://piracymonitor.org/roku-hit-with-credential-stuffing-attack-locking-users-out-of-accounts/ | Source-Type: journalism | As Of: 2024-03 | Authority: 6/10
[N13] LegalReader: Florida-Roku Children's Privacy Settlement | https://www.legalreader.com/florida-roku-announce-settlement-in-childrens-digital-privacy-lawsuit/ | Source-Type: journalism | As Of: 2025 [u] | Authority: 6/10
[N14] Jellyfin: Free Software Media System | https://jellyfin.org/ | Source-Type: community | As Of: 2026-06 | Authority: 8/10

## Findings
- 北美 TV OS 出货：Omdia 1Q25 Roku 34%、Tizen 22%、Fire TV & Vizio CastOS 各 12%；全年口径 Roku 31%、Tizen 22%、Fire TV 14%、CastOS 13%。[N1][N2]
- 全球 TV OS：Android 42%（含中国分叉，装机 >2.5 亿[u]）第一、Tizen 17% 第二；2029 前 Android 仍领先。[N1]
- Walmart 2024 以 $23 亿收购 Vizio，正把 Onn 电视从 Roku 换 CastOS；Omdia 预测 CastOS 到 2029 北美出货第一（~30%），Roku 跌至 13%。[N1][N2]
- Amazon–Roku 2025 达成 DSP 联播，覆盖 8000 万认证美国家庭（全美最大登录态 CTV 足迹）。[N2]
- Pixalate Q4 2025 CTV 设备 SOV：北美 Roku 32%/Fire TV 16%/Apple 15%/Samsung 14%/LG 10%；EMEA Samsung 24%；APAC Xiaomi 15%。[N3]
- FMI：Roku+Fire TV+Chromecast 三家 ~55% 全球 CTV；Apple/Samsung/LG ~30%。[N4]
- Roku FY2025：净收入 $47.37 亿；平台 $41.45 亿（广告 $23.28 亿 +13%、订阅 $18.17 亿 +25%）；设备 $5.9 亿；全球流媒体家庭破 1 亿；流媒体时长 1456 亿小时 +15%；#1 by hours（美/加/墨）。[N5][N6]
- ACR 机制：Samsung ~500ms、LG ~10ms 截帧指纹化屏幕内容（含 HDMI 输入）转卖广告 broker。[N11]
- Vizio 2017 FTC $2.2M（未告知即对 1100 万台启用 Inscape 逐秒观看史）。[N7]
- Samsung 德州：AG Paxton 2025-12 起诉，指 ACR 藏在"Viewing Information Services"、200+ 点击 dark pattern、只说采"signatures"；2026-02 和解须明示 opt-in 同意 + 清晰披露；AG 声明将继续起诉其他厂商。[N8][N9]
- Roku 撞库 15,363 账户被接管 [N12]；佛州儿童数据和解 [N13]。
- Apple TV 4K 不预装 ACR（Apple 向 Ars 确认）、setup 默认关位置/语音/分析、tvOS 无首屏广告、tvOS 14.5+ 强制第三方 ATT；但个性化推荐/播放历史默认开、Apple 探索 Apple TV+ 广告 tier。[N10]

## Market Leaders
- 北美 TV OS：Roku ~34%（1Q25）/ Samsung Tizen ~22% / Fire TV & Vizio CastOS 各 ~12–14%。[N1][N2]
- 全球 TV OS：Android/Google TV ~42% / Tizen ~17%。[N1]
- 北美 CTV 设备 SOV：Roku 32% / Fire TV 16% / Apple 15% / Samsung 14% / LG 10%。[N3]
- 上市财务锚：Roku（NASDAQ:ROKU）FY2025 $47.4 亿、100M+ 家庭、1456 亿小时。[N5][N6]
- 无 ACR 例外：Apple TV 4K。[N10]
- 母公司：Samsung / LG / Amazon / Google / Roku / Vizio→Walmart / Hisense / Apple。[N1][N2]

## Segment Champions
- 北美 TV OS 出货：Roku TV OS（授权 TCL/Hisense/Onn）。[N2]
- 零售媒体新贵：Vizio CastOS（Walmart，2029 预测北美第一）。[N1][N2]
- 高端一体机：Samsung Tizen + LG webOS。[N1]
- 广告变现：Roku（广告 $23.3 亿，占平台 ~56%，视频曝光 +68%）。[N6]
- 全球 OS 装机：Android/Google TV。[N1]
- 流媒体棒/盒：Amazon Fire TV Stick（~31%[u]）/ Google Chromecast（~19%[u]）/ Roku（~17%[u]）。[N4]
- 隐私前端：Apple TV 4K（无 ACR）。[N10]

## VC Rising Stars
- 无独立硬件新星——大厂/平台垄断；资本重心＝"电视即零售媒体网络"。
- Walmart（Vizio/CastOS/Onn）+ Amazon（Fire TV + Amazon DSP）把电视变 RMN；Amazon-Roku 8000 万家庭 DSP 联播。[N2]
- Roku 广告栈：Roku Ads API、Roku Data Cloud、Amazon DSP/Nielsen/FreeWheel 打通。[N5][N6]
- FAST 频道（Roku Channel / Samsung TV Plus / Tubi）依赖 ACR 定向。
- 开源双轨：Jellyfin（自托管媒体库）vs 商业 TV OS 云观看画像。[N14]

## Candidate Keywords
roku alternative / fire tv alternative / google tv alternative / vizio alternative / smart tv without acr / turn off acr / disable acr samsung / smart tv spying / smart tv privacy / stop smart tv tracking / apple tv privacy / dumb tv alternative / jellyfin / self hosted media server / plex alternative / jellyfin apple tv / apple tv vs roku privacy / best streaming device privacy / samsung vs lg acr / roku data collection

## Deep Read Notes
### Source [N1][N2]: Omdia TV OS 份额
Key data: 北美 1Q25 Roku 34%/Tizen 22%/Fire TV & CastOS 各 12%；全球 Android 42%/Tizen 17%；Walmart $23 亿收购 Vizio、Onn 换 CastOS，2029 CastOS 北美第一(~30%)、Roku 跌 13%。
Key insight: 电视 OS 之争本质是零售媒体/广告数据之争；Walmart/Amazon 把电视当 RMN 入口——ACR 是这场战争的燃料。

### Source [N6]: Roku FY2025 财务
Key data: 净收入 $47.37 亿；平台 $41.45 亿（广告 $23.28 亿、订阅 $18.17 亿）；设备 $5.9 亿（毛利极薄）；1456 亿流媒体小时。
Key insight: 硬件不赚钱、广告是引擎——证明"智能电视商业模式即观看数据变现"，强化"buy a TV = buy an ad machine that watches you"叙事。

### Source [N8][N9]: Samsung 德州 ACR 和解
Key data: 2025-12 起诉 → 2026-01 TRO → 2026-02 和解；ACR 藏"Viewing Information Services"、200+ 点击 dark pattern、只说采"signatures"；须明示 opt-in + 清晰披露；AG 将继续起诉其他厂商。
Key insight: 继 Vizio(2017) 后第二个 ACR consent 执法里程碑，且门槛升级到"明示同意"；"smart tv without acr"/"turn off acr" 买家意图强。

### Source [N10]: Apple TV 无 ACR
Key data: Apple 确认 tvOS 不预装 ACR；setup 默认关位置/语音/分析；tvOS 无首屏广告；ATT 拦第三方；但 Apple TV app 个性化推荐/播放历史默认开、Apple 探索广告 tier；Enswers 创始人称技术上 Apple 可软件更新加 ACR。
Key insight: Apple TV 4K 是唯一"干净"主流前端，但非绝对——平替叙事应是"Jellyfin 自建库 + Apple TV 作前端 + 电视断网"，而非"信任 Apple"。

## Gaps
- TV OS/CTV/棒盒份额随口径（出货 vs 广告 SOV vs 装机量）差异大，多为研究机构估算，全量数据付费[u]。
- 棒/盒具体全球份额（Fire TV ~31%、Chromecast ~19%、Roku ~17%、Apple ~8%）来自单一市场报告，未交叉验证[u]。
- Fire TV/Google TV 平台层 vs OEM 层 ACR 差异未逐品牌验证[u]。
- Roku「卖观看数据」的执法证据强度低于 Vizio/Samsung 级 ACR 案；佛州 Roku 儿童和解金额（~$25M[u]）未获官方确认。
- Jellyfin 无官方 star/版本数（本报告未取 GitHub 指标）；Olares Market 仅确认有 Jellyfin 报告。
- Apple 未公布 Apple TV 4K 销量/装机绝对数。

## END
