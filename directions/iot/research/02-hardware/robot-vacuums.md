# 扫地机器人竞品与关键词（IoT 方向 · 品类 14）

> 研究日期: 2026-07-04 | 来源: task-01（15 源，WebSearch/WebFetch）+ 原家居分册 seed 笔记（扫地机 row）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 扫地/拖地机器人（robot vacuum / robot mop，含 LiDAR SLAM 与视觉导航）。语音中枢见品类 03；家用摄像头见品类 05；灯/插座/温控/传感器见品类 10-13。归属 IoT 新方向"硬件章"。发现笔记见 [robot-vacuums.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/robot-vacuums.notes)。

## 摘要
扫地机器人是整个 IoT 方向里**隐私最敏感、去云技术门槛却最高**的品类：LiDAR/视觉 SLAM 生成的房间边界与家具布局＝户型图（floor plan），厂商云同步即默认把你家平面图存到第三方，且已有执法/研究级实证事件（iRobot 2020 测试图经 Scale AI 泄露、Ecovacs 蓝牙劫持远程开摄像头/麦克风 + CVE-2024-52327）。市场格局在 2023–2025 完成"美系先驱→中国品牌主导"的换代：IDC 口径 Roborock（石头，688169.SH）自 2023 H2 起连续三年 RVC 出货 #1，2025 全球家用清洁机器人出货 3272 万台（+20.1%），前五 Roborock/Ecovacs/Dreame/Xiaomi/Narwal 占约 70%（Q2 2025），iRobot 跌出全球前五（第 6），并于 2026-01 进入 Chapter 11 归 Picea [N1][N2][N3][N7]。**Olares 落点**：Valetudo（root 去云、地图留本地、MQTT 接 Home Assistant，官方 49 款可 root 型号）+ 选无摄像头 LiDAR-only 型号 + IoT VLAN 防火墙阻断出网——但 root 型号矩阵随固件/PCB 版本变化，是本品类最大诚实差距 [N12][N13]。

## 1. 品类概述
扫地机器人按导航分**LiDAR SLAM**（激光雷达建图，Roborock/Dreame 高端主力）、**视觉 VSLAM/双目 + AI 避障**（含前置摄像头，Ecovacs/iRobot 部分型号）与**陀螺仪/随机**（低端）三路；按云依赖分厂商云优先（App 强绑定、地图上云、AI 物体识别在云端）与本地友好（root 后 Valetudo / Roborock Local Server）两条路线。2025 全球家用清洁机器人出货 3272 万台（+20.1%），其中扫地机（Smart Vacuum）2412 万台（+17.1%），仍占近 3/4；割草/擦窗机器人是最快增长引擎 [N2]。隐私视角下这是品类里**空间数据暴露最直接**的一类——户型图 + 可选摄像头/麦克风 + Wi-Fi 凭据，且多起研究级攻击集中于此（见第 6 节）。

## 2. 市场领导者 / top 畅销
| 口径 | 领导者 | 锚点 |
|------|--------|------|
| RVC 出货全球 #1（IDC，连续） | Roborock（石头 688169.SH） | 自 2023 H2 起 RVC 出货连续 #1，2025 H2 份额 21.7%–27.0%[u]（各口径不一） [N1][N4] |
| 销量+收入口径 #1（IDC Q1 2026） | Dreame（追觅） | 自称 IDC Q1 2026 RVC 销量与收入双第一[u]；2025 营收 >400 亿 CNY、海外占 ~80% [N6] |
| 集中度 | 前五 Roborock/Ecovacs/Dreame/Xiaomi/Narwal | Q2 2025 合计约 70% 全球出货 [N3] |
| 上市财务锚 | Roborock（688169.SH） | FY2025 营收 186.95 亿 CNY（+56.51%），归母净利 13.63 亿（-31%），RVC 销量 561.9 万台，海外收入 104.42 亿 [N4] |
| 多品类上市高增长 | SharkNinja（NYSE:SN） | FY2025 $64 亿，跨清洁/厨房/美护 [N14] |
| 出局的先驱 | iRobot Roomba | 跌出全球前五（第 6），2026-01 Chapter 11 归 Picea [N2][N3][N7] |

母公司：Roborock（688169.SH）、Ecovacs（科沃斯 603486.SH）、Dreame（追觅，拟港股 IPO）、Xiaomi（小米 1810.HK）、Narwal（云鲸）、SharkNinja（NYSE:SN）、iRobot（Picea / iRobot Safe Corp.）、Eufy（Anker 300866.SZ）[N1][N4][N7][N14]。

**置信度: Medium**（IDC 排名口径可靠，但免费公开的按品牌精确份额 % 各源不一致：Roborock 2025 H2 share 有 27.0%[PR] / 24.1%[newsroom] / 21.7%[前三季度] 三种说法[u]；"谁是全球 #1"因"出货 vs 销额"口径而异）。

## 3. 细分赛道冠军
- **全球 RVC 出货冠军**：Roborock（石头）——LiDAR SLAM 高端主力，IDC 口径美国/德国/韩国均 #1；2025 累计服务 2200 万家庭 [N1][N4]。
- **收入/增长冠军**：Dreame（追觅）——海外占 ~80%，八年 CAGR >100%，IDC Q1 2026 销量+收入双第一[u]，横向拓割草/泳池/擦窗 [N6]。
- **综合价值/性价比梯队**：Ecovacs（科沃斯，Deebot + Yeedi）——早期视觉+激光融合，但被 2024 安全事件重创信誉（见第 6 节）[N8][N15]。
- **美系品牌遗产**：iRobot Roomba——先驱品牌、认知度高，但份额与治理双承压 [N7]。
- **多品类上市高增长**：SharkNinja（NYSE:SN）——清洁只是其一环，是家居硬件里少见的高增长上市样本 [N14]。
- **去云技术冠军**：**Valetudo**（Apache-2.0，非固件而是"云替换层"，root 后地图留机内、暴露本地 HTTP + MQTT，官方 49 款可 root 型号；另有 Roborock Local Server 作更轻量替代）[N12][N13]。
- **隐私优先选型路径**：选 **LiDAR-only 无摄像头** 型号（去掉移动监控终端风险）+ Valetudo root。

**置信度: High**（去云软件冠军 Valetudo 有明确社区共识与官方型号页；Dreame"双第一"为厂商引用 IDC 口径[u]）。

## 4. VC 圈 / 资本明日之星
扫地机硬件本身非 VC 新星，资本事件集中在 IPO / 破产重组 / 多品类扩张：
- **Dreame（追觅）**：2026 开启 pre-IPO 轮，投前估值约 700 亿 CNY（$9.6B），拟释放 5%–10% 股权、单笔门槛 3.5 亿 CNY，窗口 7 月初关闭；计划 H2 2026 递交港股 IPO 申请，目标市值 150 亿 CNY（口径不一，部分源称 2027 上市）[u] [N5][N6]。
- **iRobot**：从 Amazon 并购失败（2024-01 EU 反对告吹）持续承压，2025-12 宣布战略交易、2026-01 Chapter 11，资产归 Picea / iRobot Safe Corp. [N7]。
- **SharkNinja（NYSE:SN）**：FY2025 $64 亿，多品类高增长上市样本 [N14]。
- **开源双轨**：闭源厂商云 vs **Valetudo / Roborock Local Server**（开源本地）——与摄像头品类的 Frigate 同构，构成"闭源云 AI vs 开源本地"叙事 [N12]。

**置信度: Medium**（IPO/破产事件可靠，Dreame 估值与时间表多为媒体口径[u]）。

## 5. 候选产品关键词
品牌替代：`roomba alternative`、`roborock alternative`、`ecovacs alternative`、`irobot alternative`。
去云/本地（核心机会）：`robot vacuum without cloud`、`robot vacuum no cloud`、`valetudo`、`local robot vacuum`、`robot vacuum home assistant`、`robot vacuum without app`、`robot vacuum no camera`、`robot vacuum privacy`。
选购/对比：`roborock vs roomba`、`roborock vs dreame`、`best robot vacuum no cloud`、`best robot vacuum for privacy`、`valetudo supported robots`、`rootable robot vacuum`。

> Olares Market 已有 Home Assistant 报告，`valetudo`、`robot vacuum home assistant`、`robot vacuum without cloud`、`roomba alternative` 是与现有资产最贴合的切入。精确搜索量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **户型地图＝floor plan 高敏感空间数据**：LiDAR/视觉 SLAM 建的房间边界、家具布局、房型面积上云即存第三方；融合运行时段可推断作息与在家/离家窗口。
- **iRobot 测试图像泄露（已核实）**：2020 J7 开发测试机 intimate 图像（含卫生间）发至 Scale AI 标注并在社群外泄；iRobot 确认并终止合作 [N11]。
- **Ecovacs 摄像头/麦克风被黑（已核实）**：2024 研究者证实蓝牙 ~130m 劫持可远程开摄像头/麦克风、下载地图、读 Wi-Fi 密码；ABC 在 X2 上复现；CVE-2024-52327 为云端 PIN 绕过 [N8][N9][N10]。
- **Olares 平替栈**：优先选 **LiDAR-only 无摄像头** 型号（消除移动监控终端）→ 用 **Valetudo** root 断云、地图与调度留机内 → 经 **MQTT 接入 Home Assistant on Olares** 做地图/分区/自动化 → 把扫地机放 **IoT VLAN、防火墙阻断出网（block WAN）**，远程用 Tailscale/VPN 而非厂商云 [N12][N13]。
- **诚实差距（本品类最关键）**：Valetudo root 型号是**穷举白名单**（官方 49 款），且随固件/PCB 版本失效——例如 Dreame L20 Ultra 仅序列号 R2394 可 root、R2253 同名不可；Roborock Q7 Max 约 2024 Q2 起 SkyHigh NAND 可能封堵 root；现代 Roborock（S6 起）多需**整机拆解**而非无损。买前必须对着 valetudo.cloud 官方页核对确切序列号/PCB 版本 [N13][N12]。

**置信度: High**（Valetudo 去云栈成熟、隐私事件均已核实；型号可 root 性以官方页为准）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：谁是全球 #1——Roborock（IDC "RVC 出货"口径，自 2023 H2 连续三年）vs Dreame（IDC "销量+收入"口径，Q1 2026 自称双第一）。差异来自"出货量 vs 销售额"口径与统计期；且 Roborock 2025 H2 份额在不同来源有 21.7%–27.0% 三种数字，均标[u] [N1][N3][N4][N6]。

**反方解释**：厂商云带来 AI 物体避障、跨地远程、云端地图管理/多楼层、OTA 与"开箱即用"，对非技术用户显著优于自托管；Valetudo 需匹配**精确 PCB 版本**并具备 root 知识，现代高端 Roborock 甚至需整机拆解，属硬核技术用户路径。选无摄像头型号会牺牲 AI 避障能力。因此隐私叙事应聚焦"选对可 root 型号 + LiDAR-only + 断网"，而非泛泛"所有扫地机都能去云" [N12][N13]。

**参考文献**（Source-Type · As Of）
- [N1] Roborock Becomes World's No.1 Smart Cleaning Robot (IDC). official · 2026-03. https://www.prnewswire.co.uk/news-releases/roborock-becomes-the-worlds-no-1-smart-cleaning-robot-brand-according-to-idc-302712212.html
- [N2] IDC, Global Home Cleaning Robot Market 2025. secondary-industry · 2026. https://www.idc.com/resource-center/blog/global-home-cleaning-robot-market-2025/
- [N3] SCMP/IndexBox, Chinese Robot Vacuums Dominate ~70%. secondary-industry · 2025. https://www.indexbox.io/blog/chinese-robot-vacuums-dominate-70-of-global-market/
- [N4] Roborock 2025 Annual Report (688169.SH). official · 2026-04. https://newsroom.roborock.com/gl/news/roborock-reports-56-51-revenue-growth-in-2025-q1-2026-revenue-up-23-31-
- [N5] Dreame Considers Hong Kong IPO (Bloomberg). journalism · 2026-06. https://www.bloomberg.com/news/articles/2026-06-12/chinese-robot-appliance-maker-dreame-tech-is-said-to-consider-ipo-in-hong-kong
- [N6] Dreame Eyes Hong Kong IPO, $9.6B (TNW). journalism · 2026-06. https://thenextweb.com/news/dreame-technology-hong-kong-ipo-robot-vacuum
- [N7] iRobot Strategic Transaction / Chapter 11 (Picea). official · 2025-12. https://media.irobot.com/2025-12-14-iRobot-Announces-Strategic-Transaction
- [N8] Ecovacs Robots Can Be Hacked to Spy (TechCrunch). journalism · 2024-08. https://techcrunch.com/2024/08/09/ecovacs-home-robots-can-be-hacked-to-spy-on-their-owners-researchers-say/
- [N9] ABC Reproduces Ecovacs X2 Hack. journalism · 2024-10. https://www.abc.net.au/news/2024-10-04/robot-vacuum-hacked-photos-camera-audio/104414020
- [N10] CVE-2024-52327 Ecovacs Cloud PIN Bypass (NVD). official · 2024-12. https://nvd.nist.gov/vuln/detail/CVE-2024-52327
- [N11] iRobot Test Images Leaked via Scale AI (MIT TR). journalism · 2022-12. https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/
- [N12] Hypfer/Valetudo (Cloud Replacement, FOSS). community · 2026. https://github.com/hypfer/valetudo
- [N13] Valetudo Supported Robots 2026 Matrix (privacysmarthome/valetudo.cloud). other · 2026 [u]. https://valetudo.cloud/pages/general/supported-robots/
- [N14] SharkNinja FY2025 Results. official · 2026-02. https://newsroom.sharkninja.com/sharkninja-reports-fourth-quarter-and-full-year-2025-results/
- [N15] Ecovacs 603486 Annual Report. official · 2025. http://static.cninfo.com.cn/finalpage/2026-04-25/1225188694.PDF
- 完整发现笔记见 [robot-vacuums.notes/task-01.md](/Users/pengpeng/seo/directions/iot/research/02-hardware/robot-vacuums.notes/task-01.md)。
