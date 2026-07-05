# AI 录音硬件 / ambient 记忆设备竞品与关键词（IoT 方向 · 品类 08）

> 研究日期: 2026-07-04 | 来源: task-01（12 源）+ 家居分册 seed（task-04 + registry）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = AI 录音卡片/吊坠/录音耳机 + AI 会议记录软件对照。健康手环/穿戴见品类 09。归属 IoT 新方向"硬件章"。发现笔记见 [ai-recorders.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/ai-recorders.notes)。

## 摘要
这是 2025–2026 变化最剧烈的品类：独立 AI 录音硬件创业窗口正在关闭——**Limitless 被 Meta 收（2025-12）、Bee 被 Amazon 收（2025-07）、Humane 关停（HP $116M 收资产、设备 brick）**，唯有 **Plaud** 以"硬件入口 + 订阅"跑通规模化（2M+ 出货、软件 ARR $100M+、Sacra 估整体年化 ~$250M[u]，累计融资仅 ~$5M）成为品类唯一独立冠军 [N1][N2][N4][N5][N8]。软件会议记录侧则是高估值三强：Granola（$1.5B）、Fireflies（$1B+）、Otter（$100M ARR）[N3][N6][N7]。硬件新锐 Pocket（YC W26，$27M 年化）在挑战 [N11]。**Olares 落点极强且差异化**：ambient 记忆 + 转写摘要正是 Personal Agent 的核心用例——OpenClaw + Whisper 本地 STT + Ollama 摘要 + 本地存储，可替代"专用录音吊坠 + 云转写"，数据不出 Olares。隐私上这是最高风险面（全天录音 + 旁人未同意 + 无录音指示灯 + 音频上云）。

## 1. 品类概述
AI 录音硬件指卡片/吊坠/胸针/录音耳机等 ambient 采集设备，配云 AI 转写摘要；软件侧是会议记录 App（Granola/Otter/Fireflies）与 OS 内置（Apple Intelligence、Pixel Recorder）。品类价值是"把真实世界对话变成可检索记忆"。隐私视角：全天录音含未同意第三方语音，美国 one-party vs 欧盟/英国 all-party 同意法冲突，Fieldy 无录音指示灯加剧风险 [seed task-04]。

## 2. 市场领导者 / top 产品
| 类型 | 领导者 | 锚点 |
|------|--------|------|
| 独立硬件规模化冠军 | Plaud | 2M+ 出货、软件 ARR $100M+、整体年化 ~$250M[u]，融资仅 ~$5M [N1][N2] |
| 软件会议记录（估值） | Granola | $1.5B 估值、$192M 融资 [N3] |
| 软件会议记录（ARR） | Otter.ai | $100M ARR、35M+ 用户 [N6] |
| 软件会议记录（盈利独角兽） | Fireflies.ai | $1B+ 估值、盈利 [N7] |
| 大厂 ambient 记忆 | Meta（收 Limitless）/ Amazon（收 Bee） | talent+tech 吸收 [N4][N5] |

**置信度: Medium**（Plaud 官方 vs Sacra 口径并存；软件估值可靠，Plaud 估值/Tencent 投资为传闻 [u]）。

## 3. 细分赛道冠军
- **独立硬件规模化冠军**：Plaud（Note/NotePin/Note Pro，$159–$189 + $99–$240/年；~50% 用户升级付费）[N1][N2]。
- **硬件新锐挑战者**：Pocket（YC W26，Sacra 估 $27M 年化、35K+ 出货，2026-06 Accel 领投 $11M）[N11]。
- **被大厂吸收（ambient 硬件）**：Limitless→Meta（2025-12）、Bee→Amazon（2025-07）[N4][N5]。
- **软件会议记录冠军**：Granola（估值最高）/ Otter（ARR 最清晰）/ Fireflies（盈利独角兽）[N3][N6][N7]。
- **情感陪伴子带**：Friend（$99 吊坠、$8.5M 融资，2025 延期，非会议笔记）[N10]。
- **失败/转型对照**：Humane（brick）、Rabbit R1（集成 OpenClaw，转向 universal AI controller，非纯录音）[N8][N9]。
- **中端硬件对照**：Fieldy 3（$299、7 天续航、$9.99/月，无录音指示灯）[N12]。

**置信度: High**（冠军与并购格局有一手媒体共识）。

## 4. VC 圈明日之星
- **Plaud**：2025-04 convertible note $4.75M（Carbide）；Tencent 传闻 @$1B→$2B[u]——极端资本效率（低融资 vs 高营收）[N2]。
- **Granola**：2026-03 Series C $125M @ $1.5B；2025-05 Series B $43M @ $250M；累计 $192M；<3 年独角兽 [N3]。
- **Pocket（YC W26）**：2026-06 $11M（Accel+YC）；硬件赛道最亮新锐 [N11]。
- **Otter.ai**：累计 ~$73M（2021 Series B $50M）[N6]。
- **Fireflies.ai**：累计 ~$20M；2025-06 $1B+ tender offer；盈利 [N7]。
- **被收购退出**：Limitless（$33M+→Meta）、Bee（~$7M→Amazon）、Humane（~$230–240M→HP $116M 资产，反面教材）[N4][N5][N8]。

**置信度: Medium**（软件轮次可靠，Plaud 估值传闻 [u]）。

## 5. 候选产品关键词
硬件品牌替代：`plaud alternative`、`limitless pendant alternative`、`fieldy alternative`、`pocket ai recorder`。
软件替代：`granola alternative`、`otter ai alternative`、`fireflies ai alternative`、`apple intelligence meeting summary`。
品类/选购：`ai voice recorder`、`best ai note taker`、`ai meeting notes`、`ai wearable recorder`、`ai pendant recorder`、`best ai transcription device`、`ai note taking hardware`、`ambient ai memory device`。
自托管（核心机会）：`self hosted meeting transcription`、`open source ai voice recorder`、`whisper transcription self hosted`、`meeting transcription without bot`。

> 自托管转写词与 Olares Personal Agent 叙事最贴合，竞争低。精确量留后续 brand-seo-research。

## 6. 隐私风险 + Olares 自托管平替
- **风险共性（seed task-04）**：全天录音 + 旁人未同意是最高风险面；音频上云转写；Fieldy 无录音指示灯；美国 one-party vs 欧盟/英国 all-party 同意法冲突。
- **Olares 平替栈**：OpenClaw（多渠道私人 Agent）+ Whisper 本地 STT + Ollama 本地摘要 + 本地存储，构成 ambient 记忆的自托管路径，数据不出 Olares；替代"专用录音吊坠 + 云转写"[seed task-04]。会议记录侧可自托管 Whisper + LLM，替代 Otter/Fireflies 的云 bot。
- **诚实差距**：无专用吊坠硬件（需自备录音工作流/手机）；Olares 侧"ambient 录音→本地记忆"端到端教程缺失 [seed Gaps]。

**置信度: High**（自托管转写技术成熟，硬件形态是缺口）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：Plaud 到底多大——官方 $100M 软件 ARR vs Sacra 整体年化 ~$250M[u]，$500M 2026 目标未官方确认，Tencent 投资/$1B–$2B 估值仅传闻 [N1][N2][u]。写内容须区分"软件 ARR"与"整体年化"口径。

**反方解释**：Plaud 的成功（AI 硬件 volume 仅次于 Ray-Ban Meta）证明品类可规模化；但 Humane 失败、Friend 延期/低出货、Limitless 被收，都表明独立 pendant 形态面临隐私反弹、社交摩擦、retention 难题——多数用户可能更接受手机 App/OS 内置而非专用吊坠 [N4][N8][N10]。

**参考文献**（Source-Type · As Of）
- [N1] TechCrunch, Plaud $100M ARR, 2M+ shipped. journalism · 2026-06. https://techcrunch.com/2026/06/16/plaud-says-its-software-business-topped-100m-in-arr-after-shipping-over-2m-ai-notetakers/
- [N2] Sacra, Plaud revenue & funding. secondary-industry · 2026-06. https://sacra.com/c/plaud/
- [N3] TechCrunch, Granola $125M @ $1.5B. journalism · 2026-03. https://techcrunch.com/2026/03/25/granola-raises-125m-hits-1-5b-valuation.../
- [N4] TechCrunch, Meta acquires Limitless. journalism · 2025-12. https://techcrunch.com/2025/12/05/meta-acquires-ai-device-startup-limitless/
- [N5] TechCrunch, Amazon acquires Bee. journalism · 2025-07. https://techcrunch.com/2025/07/22/amazon-acquires-bee-the-ai-wearable-that-records-everything-you-say/
- [N6] Business Wire, Otter.ai $100M ARR. official · 2025-12. https://www.businesswire.com/news/home/20251222704206/en/
- [N7] Business Wire, Fireflies $1B Valuation. official · 2025-06. https://www.businesswire.com/news/home/20250612531860/en/
- [N8] TechCrunch, Humane AI Pin dead, HP $116M. journalism · 2025-02. https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m/
- [N9] Rabbit, DLAM/OpenClaw update. official · 2026-01. https://www.rabbit.tech/blog/first-major-update-of-2026-dlam-openclaw-and-a-surprise
- [N10] TechCrunch, Friend delays shipments. journalism · 2025-01. https://techcrunch.com/2025/01/20/friend-delays-shipments-of-its-ai-companion-pendant/
- [N11] Sacra, Pocket at $27M annualized. secondary-industry · 2026-02. https://sacra.com/research/pocket-at-27m-annualized-revenue/
- [N12] Fieldy, Wearable AI Note Taker. official · 2026-04. https://www.fieldy.ai/