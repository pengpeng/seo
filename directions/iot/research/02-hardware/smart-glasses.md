# 智能眼镜 / 第一视角竞品与关键词（IoT 方向 · 品类 22）

> 研究日期: 2026-07-04 | 来源: task-01（14 源）+ 原家居分册 seed 笔记（智能眼镜 row）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 智能眼镜 / 第一视角可穿戴（first-person wearables）：相机+麦克风音频眼镜（Ray-Ban Meta / Echo Frames）、单目 HUD 显示眼镜（Meta Ray-Ban Display / Even Realities）、真 AR / 光学透视眼镜（Snap Specs / Xreal / Viture / Rokid）、开源硬件（Brilliant Labs Frame/Halo）。**独立 AI 录音吊坠/卡片见品类 08 ai-recorders（Plaud 类不在此重复）**；健康穿戴见品类 09 wearables。归属 IoT 新方向"硬件章"。发现笔记见 [smart-glasses.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-glasses.notes)。

## 摘要
智能眼镜是 2025–2026 增长最猛、也是 Olares 平替最薄弱的 IoT 硬件品类。**Meta × EssilorLuxottica 一家独大**：2025 单年售出 7M+ 副（Ray-Ban + Oakley 双品牌），是 2023–2024 两年合计 2M 的 3 倍多，累计约 9M；IDC 口径 Meta 2026Q1 全球份额 **69.2%**，第 2–5 名（RayNeo 3.4% / 小米 3.1% / Viture 2.5% / XREAL 2.0%）合计不足 12% [N1][N2][N3]。护城河不在设备本身，而在 EssilorLuxottica 全球最大验光零售网 + 30 亿社交图谱 + 广告补贴硬件 [N3]。品类正分叉为三条路线：**音频/相机眼镜**（Ray-Ban Meta、Amazon Echo Frames）、**单目 HUD**（$799 Meta Ray-Ban Display、$599 Even Realities G1）、**真 AR/光学透视**（$2,195 Snap Specs、Xreal Aura Android XR）。**隐私是本品类最尖锐面**：第一视角相机+麦克风，「Hey Meta」语音默认存云 up to 1 年且 2025-04 起**取消 opt-out**（只能手动删）；旁人无从同意，LED 录制指示灯被监管质疑无效、且可被贴胶带/改装绕过，加州 SB1130、宾州 HB2603 已立法拟强制 [N5][N6][N11][N12][N13]。**Olares 落点（诚实）：无完整开源平替**——记忆侧可用 OpenClaw + 本地 Whisper 转写做 ambient 记忆自托管；硬件侧 **Brilliant Labs Frame/Halo（MIT 开源）是唯一开源方向**，但仍是开发者玩具，非 Ray-Ban Meta 的日用替代。**成熟度: Low**。

## 1. 品类概述
智能眼镜按"是否有显示 + 是否有相机"分三档：① **音频/相机眼镜**——Ray-Ban Meta（相机+麦克风+扬声器，第一视角拍照/录像/Live AI）、Amazon Echo Frames（纯音频 Alexa，无相机无显示，$269）；② **单目 HUD 显示眼镜**——Meta Ray-Ban Display（$799，右镜片小显示 + 神经腕带手势）、Even Realities G1（$599 波导绿色单色文字，无相机无扬声器，导航/翻译/提词）、Rokid；③ **真 AR / 光学透视**——Snap Specs（$2,195 独立无 puck 全彩 51° AR）、Xreal Aura（Android XR、外接算力 puck、70° FOV）、Viture（观影向 OST）。IDC：无显示智能眼镜 2026Q1 出货 ~2.25M（同比 +167%，一个季度接近 2024 全年），FY2026 预计 13.6M，ASP ~$376（2030 压到 ~$229）；OST 显示眼镜 CAGR 41.9% 是 XR 增速最快段 [N3]。隐私视角下这是暴露面最直接的品类：设备戴在第一视角、常态在公共/半私密场合采集他人影像与语音，且**几乎无成熟自托管平替**（对比同章摄像头 Frigate、录音硬件 Whisper 的成熟栈）。

## 2. 市场领导者 / top 畅销
| 档位 | 领导者 | 锚点 |
|------|--------|------|
| 绝对领导者 | Ray-Ban / Oakley Meta（Meta × EssilorLuxottica） | 2025 售 7M+、累计 ~9M；IDC 2026Q1 份额 69.2% [N1][N2][N3] |
| 单目 HUD 旗舰 | Meta Ray-Ban Display | $799，右镜片显示 + 神经腕带；因美国"空前需求"推迟国际发布 [N1][N4] |
| 纯音频/智能家居 | Amazon Echo Frames（3rd Gen） | $269，Alexa 音频眼镜，无相机无显示 [N14] |
| 极简 HUD | Even Realities G1 | $599 波导单色文字，无相机无扬声器 [N13] |
| 真 AR（独立） | Snap Specs | $2,195，独立无 puck，51° 全彩，2026 秋发 [N8] |
| 显示/Android XR | Xreal（Aura）/ Viture / RayNeo | Aura 外接 puck、70° FOV；RayNeo 3.4%、Viture 2.5%、XREAL 2.0% [N3][N9] |
| 开源硬件 | Brilliant Labs Frame / Halo | MIT 开源，$349，开发者向 [N7] |

母公司/阵营：Meta（Ray-Ban/Oakley，EssilorLuxottica 制造）、Amazon（Echo Frames，Alexa）、Snap（Specs，Lens Studio）、Google/三星（Android XR，Gemini）、小米/华为/RayNeo（中国阵营）。

**置信度: Medium**（Meta 出货量与 IDC 份额有一手财报/机构口径；Counterpoint 2025H1 曾给 Meta ~73% 全球份额[u]，口径与 IDC 略异；challenger 精确出货多为季度机构估算）。

## 3. 细分赛道冠军
- **绝对畅销冠军**：Ray-Ban Meta（相机+音频，日用无违和的"不怕被人看见戴"设计是关键）[N1][N3]。
- **纯音频/智能家居冠军**：Amazon Echo Frames（Alexa 生态，无相机→隐私争议最小的一支）[N14]。
- **单目 HUD 旗舰**：Meta Ray-Ban Display（$799 + 神经腕带 sEMG 手势，量产受限于供给）[N1][N4]。
- **极简显示/无相机冠军**：Even Realities G1（$599 波导绿字，翻译/提词/导航；无相机=隐私更友好但功能窄）[N13]。
- **真 AR 独立冠军**：Snap Specs（$2,195，5 代 Spectacles + 十年 Lens Studio 开发者生态；抢在 Meta/Apple/Google 前发独立 AR）[N8][N3]。
- **Android XR / 显示眼镜**：Xreal Aura（外接 puck、70° FOV，Google Gemini 深度集成）；Viture（观影向 OST）；RayNeo（低价显示）[N3][N9]。
- **开源硬件冠军（唯一）**：Brilliant Labs Frame（nRF52840 + FPGA + 640×400 微 OLED，Lua OS，固件/SDK/原理图 MIT 开源，$349，Python/Flutter SDK）；后继 Halo（骨传导 + Narrative 记忆，Q1 2026 起发）[N7]。

**置信度: High**（分层冠军有评测/机构共识；开源属性以官方文档/GitHub 一手确认）。

## 4. VC 圈明日之星
本品类由大厂主导，"新星"是**平台之争**而非小硬件融资：
- **Google Android XR**：Gemini 已在用户邮件/照片/日历里，眼镜端"AI 已认识你"——被 IDC 视为 Meta 最结构性的威胁；Xreal Aura 为其首发硬件之一 [N3][N9]。
- **Snap**：十年 Lens Studio + 5 代 Spectacles 的光学/热/社交学习，独立 AR Specs 抢跑；引入 Claude Code/Codex/Cursor 的 agentic Lens 开发 [N8][N3]。
- **中国阵营**：小米/华为/阿里/RayNeo 以价格+量施压，且自研 AI 能力在追赶西方模型 [N3]。
- **开源侧**：Brilliant Labs（Frame→Halo）是唯一把"开源硬件 + 本地记忆"讲成产品叙事的玩家，规模极小但对 Olares 叙事最贴合 [N7]。
- 增长信号：无显示眼镜 2026Q1 +167% YoY、OST 显示眼镜 CAGR 41.9%——ASP 2030 压到 ~$229，硬件差异化让位于软件/AI/服务 [N3]。

**置信度: Medium**（IDC 份额/增速可靠；Counterpoint 份额与厂商路线图为机构/媒体口径[u]，未官方逐一确认）。

## 5. 候选产品关键词
品牌替代：`ray-ban meta alternative`、`meta glasses alternative`、`echo frames alternative`、`snap specs alternative`、`xreal alternative`。
开源/隐私（核心机会）：`open source smart glasses`、`open source ai glasses`、`brilliant labs frame`、`smart glasses without cloud`、`smart glasses privacy`、`self hosted ai glasses assistant`、`local ai glasses`。
选购/对比：`best smart glasses`、`best ai glasses`、`ray-ban meta vs xreal`、`even realities g1 vs ray-ban meta`、`snap specs vs ray-ban display`、`smart glasses with display`、`ar glasses`。
隐私/合规：`smart glasses recording light`、`are smart glasses always recording`、`ray-ban meta privacy`、`delete ray-ban meta voice recordings`。

> 与 Olares 现有资产最贴合的是记忆/转写侧词（`self hosted ai glasses assistant`、`local ai glasses`）复用 OpenClaw + Whisper 叙事，以及 `open source smart glasses` / `brilliant labs frame` 承接开源硬件唯一方向。品类主词（`best smart glasses`）竞争高、Olares 无对位硬件，宜做"隐私科普 + 开源方向"而非"平替导购"。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **第一视角常态采集**：相机+麦克风戴在眼前，在公共/半私密场合持续采集**他人**影像与语音，旁人无从事前同意——被 The Verge 称为"luxury surveillance" [N12]。
- **语音默认存云、取消 opt-out**：Meta 2025-04 起「Hey Meta」语音转录与录音**默认存云 up to 1 年**用于训练 AI，且**移除了关闭存储的选项**，用户只能在 Meta AI App 里逐条手动删；误唤醒("false wakes")90 天内删 [N5][N6]。注意范围：Meta 称主动拍的照片/视频存在手机相册、不用于训练；争议主要在语音 [N5]。
- **LED 指示灯失效争议**：录制 LED 是 Meta"已告知旁人"的核心论据，但爱尔兰/意大利监管自 2021 起质疑其有效性；LED 可被贴胶带/硬件改装绕过（虽有遮挡即停录的保护，已被部分用户破解）[N12]。加州 **SB1130**（Wearable Device Privacy Protection Act，2026-02）拟把"营业场所偷录 + 禁售禁用指示灯的改装件"入罪；宾州 **HB2603**（2026-06）拟强制显示录制指示灯并禁止禁用 [N11][N12][N13]。
- **两方同意法冲突**：全天/随手录音在美国 one-party vs 欧盟/英国及部分州 all-party 同意法下冲突（与品类 08 录音硬件同源风险）。
- **Olares 平替栈（诚实——无完整平替）**：
  - **记忆/转写侧（唯一可自托管）**：OpenClaw（多渠道私人 Agent）+ 本地 Whisper STT + Ollama 摘要 + 本地存储，把"第一视角对话→可检索记忆"留在 Olares，替代眼镜云转写；但需自备录音工作流/手机，非眼镜硬件替代。
  - **开源硬件方向（唯一开源）**：Brilliant Labs Frame/Halo（MIT，固件/SDK/原理图开源）可接自选后端模型，是唯一"不锁厂商云"的眼镜硬件；但仍是开发者原型，显示/相机/续航远逊 Ray-Ban Meta [N7]。
  - **显示/AI 软件层**：Meta AI、Gemini、Snap OS 等眼镜端 AI 属闭源商业（Software→commerce 方向），本品类不做软件平替登记；OSS 仅出现在本"平替"列。
- **诚实差距**：**无任何完整开源平替可日用替代 Ray-Ban Meta**——相机眼镜的社交隐私、显示光学、EssilorLuxottica 零售网都无开源对位；Olares 只能承接"记忆自托管 + 开源硬件科普"，不能承接"买哪副眼镜"。

**置信度: High（差距判断可靠——本品类是全 IoT 方向平替最薄弱的一类）**。

## 7. 核心争议 / 反方 / 参考

**核心争议**：智能眼镜是"日用可穿戴计算的下一代入口"还是"常态化旁人监控"？Meta 的 LED + "用语音/手势提示旁人 + 有人反对就停录"是**行为约束**而非**技术强制**，监管（爱尔兰/意大利）与州立法（CA SB1130 / PA HB2603）正把自愿功能改成强制义务 [N11][N12][N13]。份额口径也有分歧：IDC 2026Q1 Meta 69.2% vs Counterpoint 2025H1 ~73%[u]，随中国阵营与 Google/Snap 入场，"Others"（19.8%）会继续扩大 [N3]。

**反方解释**：Ray-Ban Meta 的成功证明品类可规模化（AI 硬件出货仅次于自己、7M/年），"不怕被看见戴"的时尚化是关键；对多数用户，云 AI + 社交分享的开箱体验远优于任何自托管路径。开源侧 Brilliant Labs 出货极小、体验被评"disappointing stepping stone"，说明**开源硬件短期无法承接主流需求**——Olares 的诚实定位是"隐私科普 + 记忆自托管 + 开源方向背书"，而非导购平替。

**参考文献**（Source-Type · As Of）
- [N1] CNBC, EssilorLuxottica triples Meta AI glasses sales (7M in 2025). journalism · 2026-02. https://www.cnbc.com/2026/02/11/ray-ban-maker-essilorluxottica-triples-sales-of-meta-ai-glasses.html
- [N2] UploadVR, Meta & EssilorLuxottica Sold 7M Smart Glasses in 2025. journalism · 2026-02. https://www.uploadvr.com/meta-essilorluxottica-sold-7-million-smart-glasses-in-2025/
- [N3] IDC, Smart Glasses Surge — Q1 2026 share & forecast. secondary-industry · 2026. https://www.idc.com/resource-center/blog/smart-glasses-surge-the-xr-market-is-rewriting-its-own-rules/
- [N4] Bloomberg, Meta/EssilorLuxottica discuss doubling output to 20M+. journalism · 2026-01. https://www.bloomberg.com/news/articles/2026-01-13/meta-said-to-discuss-doubling-ray-ban-glasses-output-after-surge-in-demand
- [N5] The Verge, Meta removes opt-out of voice recording storage. journalism · 2025-04. https://www.theverge.com/news/658602/meta-ray-ban-privacy-policy-ai-training-voice-recordings
- [N6] Meta, Voice Controls Privacy Notice (up to one year). official · 2025. https://www.meta.com/legal/ai-glasses/voice-controls-privacy-notice/
- [N7] Brilliant Labs, Frame Hardware Docs + frame-codebase (MIT/open). official/community · 2026. https://docs.brilliant.xyz/frame/hardware/
- [N8] Snap Newsroom, Introducing SPECS AR Glasses ($2,195, standalone). official · 2026-06. https://newsroom.snap.com/introducing-specs-augmented-reality-glasses
- [N9] Wareable, Xreal Aura Android XR reservations open (tethered puck). journalism · 2026-06. https://www.wareable.com/wearable-tech/xreal-aura-glasses-reveal-awe-2026-pre-orders-open-details
- [N11] CA Senate, SB1130 Wearable Device Privacy Protection Act. official · 2026-02. https://sd29.senate.ca.gov/news/reyes-proposes-clear-protections-against-secret-recordings-using-wearable-technology
- [N12] The Verge, Privacy laws can't keep up with 'luxury surveillance'. journalism · 2026. https://www.theverge.com/tech/807834/meta-smart-glasses-privacy-laws-wearables
- [N13] PetaPixel, PA HB2603 recording-light bill / Even Realities G1 refs. journalism · 2026-06. https://petapixel.com/2026/06/10/smart-glasses-in-pennsylvania-may-soon-legally-require-a-visible-recording-light/
- [N14] PCMag, Amazon Echo Frames (3rd Gen) review ($269, audio-only). journalism · 2025-11. https://uk.pcmag.com/wearables/150025/amazon-echo-frames-3rd-gen
- 完整 14 源见发现笔记 [smart-glasses.notes/task-01.md](/Users/pengpeng/seo/directions/iot/research/02-hardware/smart-glasses.notes/task-01.md)。
