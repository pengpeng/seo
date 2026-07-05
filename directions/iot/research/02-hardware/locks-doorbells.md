# 智能门锁 / 视频门铃竞品与关键词（IoT 方向 · 品类 07）

> 研究日期: 2026-07-04 | 来源: task-01（14 源）+ 家居分册 seed（task-02 + registry）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 智能门锁 + 视频门铃。纯摄像头见品类 05；报警套装见品类 06。归属 IoT 新方向"硬件章"。发现笔记见 [locks-doorbells.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/locks-doorbells.notes)。

## 摘要
智能门锁是"传统门锁巨头主导 + Matter 生态重构"的格局：全球前五（ASSA ABLOY、Allegion、dormakaba、SALTO、Fortune Brands）合计约 50–55% 收入 [N4]。北美 consumer 版图在 2023 年重组——ASSA ABLOY 把美加 Yale/August 卖给 Fortune Brands（$800M），2024 又收 Level 补回高端 Apple Home Key 能力，与 Allegion/Schlage 形成三足鼎立 [N1][N3]。视频门铃则由 Amazon Ring 事实主导（美国户内 ~40%），Nest 次之 [N8][N9]。VC 侧多为并购/IPO 收尾（Level→ASSA ABLOY、SwitchBot/OneRobotics 港交所 IPO ~$206M、Nuki 有 Allegion 战投）。**Olares 落点**：门锁本身缺 Frigate 级统一开源方案，但 HA + Matter/Z-Wave/Zigbee 本地控制 + 物理钥匙备份可去云；门铃侧 Aqara G410（本地 microSD/NAS/RTSP→HA）是最强"本地友好门铃"平替叙事，直接对标 Ring/Nest 云订阅。隐私上门铃是最敏感视角（Ring 警局共享 2025 以 Axon 回归、FTC 访问权），门锁有 Chirp/August API 硬编码凭证 CVSS 9.1 前科。

## 1. 品类概述
智能门锁（deadbolt/retrofit/lever）+ 视频门铃是家庭出入口的两类联网设备。门锁卖点是无钥匙 + 远程授权，门铃卖点是访客视频。二者在"无订阅/本地/Matter 生态"上与 Olares 叙事高度交叉。隐私视角：门铃是最敏感的对外视角（含公共人流），门锁掌握进出时间日志与生物特征。

## 2. 市场领导者 / top
| 子类 | 领导者 | 锚点 |
|------|--------|------|
| 门锁全球收入 | ASSA ABLOY / Allegion / Fortune Brands | 前五合计 ~50–55% [N4] |
| 门锁北美零售 | Schlage（Allegion）、Yale/August（Fortune Brands）、Kwikset Halo（Spectrum） | Schlage/Yale/Kwikset reviews 领先 [N6][N14] |
| 视频门铃 | Ring（Amazon） | 全球 24–31%[u]、美国户内 ~40%[u] [N8][N9] |
| 视频门铃 #2 | Nest（Google） | 全球 ~18–19%[u]、美国 ~24%[u] [N8][N9] |

母公司：ASSA ABLOY（瑞典）、Allegion（NYSE:ALLE）、Fortune Brands（NYSE:FBIN）、Spectrum Brands、Amazon、Google、Anker（eufy）、Lumi United（Aqara/小米生态）。

**置信度: Medium**（门锁份额为咨询机构收入估算，口径差异大；门铃份额多为第三方[u]）。

## 3. 细分赛道冠军
- **主流零售冠军**：Schlage Encode（Allegion，big-box 货架深度）、Yale Assure Lock 2、August Wi-Fi（Fortune Brands）[N6][N13][N14]。
- **Matter/Apple 生态冠军**：Aqara U100/U200 + Matter、Level Lock+（Home Key，2024 归 ASSA ABLOY）、Nuki 3.0/Ultra（欧洲，Allegion 战投）[N1][N12]。
- **超值/retrofit 冠军**：SwitchBot Lock（免换锁体）、Wyze Lock Bolt、Ultraloq U-Bolt Pro（U-tec）[N6][N10]。
- **视频门铃冠军**：Ring（美国 ~40% 户内）；Nest（Google Home 整合）[N8][N9]。
- **本地友好门铃冠军**：Aqara G410——2K + 端侧人脸（无订阅）+ Matter Controller/Thread BR/Zigbee Hub + microSD 512GB/NAS/HKSV/RTSP→HA（hardwire），~$130[u]；上代 G4 同为 HKSV + 本地存储 [N2]。

**置信度: High**（分层冠军明确，Aqara G410 有官方规格支撑）。

## 4. VC 圈明日之星
门锁/门铃独立新星稀缺，多为并购/IPO：
- **Level Lock**：2024-09 ASSA ABLOY 收购（2023 销售 ~$16M），Level M 拆为 Ambient Property Technologies [N1]。
- **SwitchBot / OneRobotics**：2025-12 港交所 IPO ~$206M；2025-05 Series C 估值 41 亿元；2024 营收 6.1 亿元、2025H1 首次盈利 [N10]。
- **Nuki**：Series B $23.52M（累计 $25.77M），投资者含 Allegion——传统巨头借战投卡位 Matter 门锁 [N12]。
- **Seam API**：YC 2020 Seed $125K，smart lock/门禁统一 API（30+ 品牌），2026-02 新增 Ultraloq [N11]。
- **Lockly**：无公开 VC，CES 2025 扩品（Visage 人脸、Home Key、Matter hub）；收入估算矛盾[u]。

**置信度: Medium**（并购/IPO 事件可靠，估值/收入多 [u]）。

## 5. 候选产品关键词
门锁品牌替代/对比：`august lock alternative`、`schlage encode vs yale assure lock`、`nuki smart lock`、`ultraloq u-bolt pro`、`wyze lock bolt`。
门锁选购：`best smart lock`、`best smart lock homekit`、`matter smart lock`、`best budget smart lock`、`level lock home key`。
无订阅/本地（核心机会）：`smart lock without subscription`、`home assistant smart lock`、`video doorbell no subscription`。
门铃品牌替代/选购：`best video doorbell`、`ring doorbell alternative`、`eufy video doorbell`、`aqara g410`、`aqara g4 vs g410`。

> `aqara g410`、`ring doorbell alternative`、`home assistant smart lock` 与 Olares/HA 直接契合。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **门铃风险（seed registry）**：Ring 门铃 = 最敏感对外视角；警局共享 2024 停后 2025 以 Axon/Flock 回归；Ring/Nest TOS 允许"紧急"无 warrant 交片 [seed task-02 / registry]。
- **门锁风险**：云远程开锁；2024 Chirp + August API 硬编码凭证 CVSS 9.1；Ultraloq Air/小米门锁进出日志上云 [seed task-02]。
- **Olares 平替栈**：门铃用 Aqara G410（本地 microSD/NAS + RTSP→Frigate + HA），或 Reolink/Amcrest PoE 门铃 → Frigate；门锁用 HA + Matter/Z-Wave/Zigbee 本地控制（避 Ultraloq Air 云、避 Mi Home 云），物理钥匙备份；远程用 Tailscale/VPN [seed task-02]。
- **诚实差距**：门锁无 Frigate 级统一开源 NVR 方案，自托管成熟度 ★★☆☆☆；Aqara 仍有 Aqara 云（可最小化但非零）[seed]。

**置信度: High**（平替存在，门锁差距已诚实标注）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：门锁"第一"取决于口径——FMI 称 Yale/Schlage Tier-1 占 45%[u]，IMARC/ReportPrime 称 ASSA ABLOY 全球 revenue 第一，差异来自全球 vs 北美 residential、revenue vs brand mindshare，以及 2023 Fortune Brands 收购后 ASSA ABLOY 北美权重下降 [N4][N5][N6]。

**反方解释**：Ring/Nest 云门铃的"移动推送 + 云 AI + 与摄像头/报警联动"体验对普通用户显著优于自托管；智能门锁的云远程/生物识别便利也是主要卖点。自托管门锁/门铃是隐私优先者选择，门锁尤其缺成熟统一方案 [N2][seed]。

**参考文献**（Source-Type · As Of）
- [N1] ASSA ABLOY, acquires Level Lock. official · 2024-09. https://www.assaabloy.com/group/en/news-media/press-releases/id.afc35a05fa7b69a0
- [N2] Aqara, Doorbell Camera Hub G410. official · 2025-07. https://www.aqara.com/eu/news-eu-2/aqara-expands-security-camera-portfolio-with-first-doorbell-camera-hub/
- [N3] Fortune Brands, Yale/August acquisition. official · 2023-06. https://ir.fbin.com/news-releases/news-release-details/fortune-brands-completes-acquisition-emtek-and-schaub-premium
- [N4] IMARC, Smart Lock Market. secondary-industry · 2025-06. https://www.imarcgroup.com/smart-lock-market
- [N5] Future Market Insights, Smart Lock Share. secondary-industry · 2025-06. https://www.futuremarketinsights.com/reports/smart-lock-market-share-analysis
- [N6] ReportPrime, Electronic Home Locks Companies. secondary-industry · 2024-12. https://www.reportprime.com/electronic-home-locks-r1354/company
- [N7] Grand View Research, Smart Lock Market. secondary-industry · 2024-12. https://www.grandviewresearch.com/industry-analysis/smart-lock-market
- [N8] MarketIntelo, Video Doorbell Market. secondary-industry · 2025-06. https://marketintelo.com/report/video-doorbell-market
- [N9] Secure IoT House, The Doorbell Surveillance State. journalism · 2026-02. https://secure-iot-house.ghost.io/the-doorbell-surveillance-state.../
- [N10] Caixin, OneRobotics HK IPO. journalism · 2025-12. https://www.caixinglobal.com/2025-12-31/smart-home-startup-onerobotics-lands-206-million-in-hk-ipo...
- [N11] CB Insights, Seam. secondary-industry · 2025-12. https://www.cbinsights.com/company/seam
- [N12] The Company Check, Nuki Home Solutions. secondary-industry · 2024-12. https://www.thecompanycheck.com/company/b/nuki-home-solutions/
- [N13] CE Pro, ASSA ABLOY Sells Yale & August. journalism · 2023-05. https://www.cepro.com/news/assa-abloy-sell-yale-august-smart-locks-business-fortune-brands/110246/
- [N14] IndexBox, Smart Door Lock Brands US. secondary-industry · 2025-06. https://www.indexbox.io/store/united-states-smart-door-lock-marketplace-brand-report/