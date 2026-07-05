# 语音中枢 / 语音助手竞品与关键词（IoT 方向 · 品类 03）

> 研究日期: 2026-07-04 | 来源: task-01（14 源）+ 家居分册 seed（task-01 + registry）| 模式: Lightweight | AS_OF: 2026-07-04 | 视角: 隐私优先 + Olares 自托管落点
>
> 品类 = 语音助手平台 + 承载语音的中枢端点（Echo/Nest Hub/HomePod）。纯音质音箱见品类 04 smart-speakers。归属 IoT 新方向"硬件章"。发现笔记见 [voice-hub.notes/](/Users/pengpeng/seo/directions/iot/research/02-hardware/voice-hub.notes)。

## 摘要
家居语音中枢正经历"三巨头 AI 化升级"：Alexa+（6 亿+ Alexa 设备 + Prime 捆绑 + agentic 任务）、Gemini for Home（2025-10 不可逆替换 Google Assistant + $10/月 Premium）、Siri（传与 Google Gemini 合作升级）。Amazon 把"已有家居 footprint + 品牌熟悉度"当核心 moat，Google 把竞争从"命令准确率"升级到"整屋语义理解 + 摄像头叙事"。开源侧可核实的冠军栈是 **Home Assistant Voice PE（$59 官方硬件）+ Assist + Wyoming 协议**（连接 openWakeWord/Whisper/Piper），Willow 为 ESP32 自托管补充。VC 热点不在"家居中枢"本身，而在语音基础设施（ElevenLabs $3.3B、Deepgram $1.3B）与下一代情感对话硬件（Sesame AI）。语音中枢是**结构性最高隐私暴露面**（常开麦克风），三大助手均有误唤醒/人工听录音和解；Echo 2025-03 起取消本地处理是真实倒退。Olares 落点是 HA Voice PE + 本地 Assist pipeline，语音不出局域网。

## 1. 品类概述
语音中枢 = 语音助手平台（Alexa/Gemini/Siri/Bixby）+ 承载它的中枢硬件（Echo、Nest Hub、HomePod）。它是全屋交互入口，也是常开麦克风的采集点。品类正从"语音命令"转向"agentic AI"（叫车、点餐、整屋自动化生成），付费墙上移（Alexa+ $19.99/月，Gemini Home Premium $10/月）[N2][N4]。隐私视角下，语音中枢是家居里暴露面最大的单点。

## 2. 市场领导者 / top 平台
| 平台 | 母公司 | 规模/战略锚点 |
|------|--------|----------------|
| Amazon Alexa / Alexa+（Echo） | Amazon | 6 亿+ 累计 Alexa 设备；97% 可支持 Alexa+；tens of millions opt-in；Prime 捆绑 [N1][N2][N3] |
| Google Gemini for Home（Nest） | Alphabet | 2025-10 全面替换 Assistant（不可逆）；免费保媒体/家居控制，Premium $10/月解锁 Live+摄像头 AI [N4][N5] |
| Apple Siri（HomePod） | Apple | Siri 主战场在 iPhone/Watch；HomePod 音箱份额远小于 Echo/Nest；传与 Gemini 合作升级 [N1][N12] |
| Samsung Bixby / SmartThings | Samsung | 随 Galaxy/家电分发；语音 MAU 公开数据少 [u] |

> 份额口径冲突：手机 Siri vs 音箱 Alexa 口径混用致全球份额区间 19%–84%[u]。更准框架可能是"**Alexa 赢音箱、Google/Apple 赢手机**"（美国口径 Alexa ~7700 万 / Google Assistant ~9200 万）[N12][u]。

**置信度: Medium**（大厂战略与设备量可靠，份额口径混乱）。

## 3. 细分赛道冠军
- **大厂云语音（消费家居）冠军**：Alexa（音箱/ambient 主导）；Google 以 Gemini 反击 [N1][N4]。
- **音质 + 轻量语音**：Sonos Voice Control（音乐/系统控制，强调隐私，可与 Alexa/Google 同设备并存；Sonos 1700 万+ 家庭、FY2025 营收 $14.43 亿）[N11]。
- **豪宅/定制集成语音冠军**：Josh.ai（经销商渠道、隐私优先、深度集成 Control4）[N8]。
- **开源本地语音冠军**：Home Assistant Voice PE + Assist（官方 $59 硬件入口）；Wyoming 协议连接 openWakeWord/Whisper/Piper；Willow（ESP32 自托管，对标 Echo/Google Home）[N9][N10][N13]。

**置信度: High**（分层冠军明确，开源栈可核实）。

## 4. VC 圈明日之星
语音赛道 2024 全球 VC ~$21 亿（约 2023 年 8 倍）[N14]，但热点在**基础设施/对话层**而非家居中枢：
- **ElevenLabs**：2025-01 Series C $180M @ **$3.3B**（TTS/配音/语音 Agent 基础设施）[N6]。
- **Deepgram**：2026-01 Series C $130M @ **$1.3B**（STT/TTS/Voice Agent，支持 self-hosted/on-prem）[N7]。
- **Sesame AI**：2025-02 Series A $47.5M（a16z），情感对话 CSM，开源 CSM-1b，目标音频眼镜硬件 [N12]。
- **SoundHound AI**（NASDAQ:SOUN）：FY2025 营收 ~$169M，连续收购 conversational AI 资产 [u]。
- **Josh.ai**：累计 $22M，2020 后资本停滞——豪宅语音赛道热度有限 [N8]。

**置信度: Medium**（基础设施轮次可靠，家居中枢专属新星稀缺）。

## 5. 候选产品关键词
品牌替代：`alexa alternative`、`google assistant alternative`、`alexa plus alternative`、`josh.ai alternative`、`rhasspy alternative`。
迁移/对比：`gemini for home vs google assistant`、`sonos voice control`。
本地/隐私（核心机会）：`offline voice assistant`、`local voice assistant`、`private voice assistant`、`self hosted voice assistant`、`open source voice assistant`、`best self hosted smart home voice control`。
产品/技术长尾：`home assistant voice`、`home assistant voice pe`、`wyoming protocol voice assistant`、`whisper voice assistant raspberry pi`、`local wake word detection openwakeword`。

> 精确 Semrush 量留后续 brand-seo-research。"local/offline/private voice assistant"是隐私叙事强、竞争相对低的核心切入。

## 6. 隐私风险 + Olares 自托管平替
- **风险共性**：常开麦克风 = 结构性风险；误唤醒 + 带屏摄像头看护扩大采集面。三大北美助手均有和解：Alexa 2019 合同工听录音、Google Assistant $68M、Siri $95M；Echo 2025-03 起取消本地处理，即使选"不保存"语音仍必上云 [seed task-01 / registry]。
- **Olares 平替栈**：麦克风卫星（ESP32+ESPHome / HA Voice PE）→ Wyoming → HA on Olares（Wake: openWakeWord/microWakeWord；STT: Whisper 或 Speech-to-Phrase；NLU: HA Assist / Ollama；TTS: Piper）。在 HA 之上跑本地 LLM Personal Agent = 开放域问答的自托管路径 [seed task-01]。
- **诚实差距**：开放域问答与 Alexa+/Gemini 有明显差距；中文 wake word/STT 社区弱；购物/日历/外卖需自建 skill [seed task-01 Gaps]。

**置信度: High**（自托管语音栈成熟度分层清晰）。

## 7. 核心争议 / 反方 / 参考

**核心争议**：不存在单一"全球语音助手第一"——按智能音箱 Alexa 领先，按手机装机 Siri/Google Assistant 领先。内容须锚定场景口径。

**反方解释**：Alexa+/Gemini for Home 的 agentic 能力（自然语言整屋自动化、跨服务任务）目前明显领先自托管；HA Voice PE 的"fully-local"仅在家居句式（Speech-to-Phrase）体验完整，开放域需接 Ollama+大模型，运维门槛高 [N4][N9]。

**参考文献**（Source-Type · As Of）
- [N1] TechCrunch, 97% of devices support Alexa+. journalism · 2026-01. https://techcrunch.com/2026/01/12/amazon-says-97-of-its-devices-can-support-alexa/
- [N2] TechCrunch, Alexa+ costs $19.99. journalism · 2025-02. https://techcrunch.com/2025/02/26/amazon-alexa-costs-19-99-free-for-prime-members/
- [N3] Amazon, Alexa Plus free with Prime. official · 2025. https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us
- [N4] Google Blog, Gemini for Home launch. official · 2025-10. https://blog.google/products-and-platforms/devices/google-nest/gemini-for-home-launch/
- [N5] Google Support, Gemini for Home voice assistant. official · 2025-10. https://support.google.com/googlehome/answer/16618650
- [N6] Reuters, ElevenLabs $3.3B valuation. journalism · 2025-01. https://www.reuters.com/technology/artificial-intelligence/voice-ai-startup-elevenlabs-closes-new-funding-round-33-billion-valuation-2025-01-30/
- [N7] SiliconANGLE, Deepgram raises $130M. journalism · 2026-01. https://siliconangle.com/2026/01/13/real-time-voice-ai-unicorn-deepgram-raises-130m/
- [N8] Tracxn, Josh.ai profile & funding. other · 2026. https://tracxn.com/d/companies/joshai/
- [N9] Home Assistant, Voice Preview Edition. official · 2024-12. https://www.home-assistant.io/voice-pe
- [N10] GitHub, OHF-Voice/wyoming. community · 2026-05. https://github.com/OHF-Voice/wyoming
- [N11] SEC, Sonos Q4/FY2025 results. official · 2025-11. https://www.sec.gov/Archives/edgar/data/1314727/000131472725000083/final4q25earningspressrele.htm
- [N12] Contrary Research, Sesame AI. secondary-industry · 2025-07. https://research.contrary.com/company/sesame-ai
- [N13] GitHub, HeyWillow/willow. community · 2026-02. https://github.com/HeyWillow/willow
- [N14] Landbase, Fastest Growing Voice AI Platforms. secondary-industry · 2026-02. https://www.landbase.com/blog/fastest-growing-voice-ai-platforms-companies