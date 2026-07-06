# Deepgram SEO 竞品分析报告

> 域名：deepgram.com | SEMrush us | 2026-07-07
> Deepgram = 企业级实时语音 AI API 平台（STT / TTS / 语音 Agent），"Voice AI economy" 头部玩家；2026-01 完成 $130M C 轮、估值 $1.3B、累计融资 $215M+。

---

## 项目理解（前置）

Deepgram 是面向开发者/企业的**实时语音 AI API 平台**：核心是高精度、低延迟的语音转文字（STT），并已扩张到语音合成（TTS）、端到端语音对话（STS）与语音 Agent。2015 年由三位密歇根大学物理学家创立（YC W2016，最初做暗物质探测器的波形分析），据称已处理 5 万年音频、转写超 1 万亿词，服务 200,000+ 开发者、1,300+ 组织（NASA、Spotify、Twilio、Citibank、Vapi、Granola）。产品线：Nova-3（STT）、Aura-2（企业级 TTS）、Flux（对话式语音识别，专攻打断处理）、Voice Agent API、Saga（Voice OS）。**关键：Deepgram 明确提供 cloud API 与 self-hosted / on-prem API 两种交付**——它自己就在打"自托管"这张牌（面向企业合规），但仍是闭源商业授权。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 企业级实时语音 AI API 平台（STT 起家 → 全语音栈），Voice AI 赛道独角兽 |
| 开源 / 许可证 | ❌ 闭源商业 SaaS（模型不开源）；提供闭源 self-hosted/on-prem 部署（企业合同） |
| 主仓库 | 无开源本体；有开源 SDK / 集成示例（github.com/deepgram，非模型权重） |
| 核心功能 | Nova-3 STT、Aura-2 TTS、Flux 对话式识别、Voice Agent API、说话人分离/实时转录 |
| 商业模式 / 定价 | 按用量计费（STT 约 $0.0043+/分钟起）；付费/成长/企业档；自托管走企业合同 |
| 差异化 / 价值主张 | 端到端深度学习自研模型、极致低延迟、企业级准确率与价格；可自托管满足合规 |
| 主要竞品（初判）| AssemblyAI、OpenAI Whisper、Google Cloud STT/TTS、ElevenLabs、Cartesia、Speechmatics、Vapi、Gladia |
| Olares Market | Deepgram 本体未上架（也无需）；平替已上架 → **Whisper API（WhisperX）/ Whisper-WebUI / Speaches（OpenAI 兼容 STT+TTS，含 Kokoro）** |
| 来源 | deepgram.com、developers.deepgram.com、BusinessWire/TechCrunch（2026-01 C 轮）、Olares [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | deepgram.com |
| SEMrush Rank | 64,930 |
| 自然关键词数 | 7,466 |
| 月自然流量（US）| 31,100 |
| 自然流量估值 | **$186,831/月** |
| 付费关键词数 | **689** |
| 月付费流量 | **16,872** |
| 付费流量估值 | $47,374/月 |
| 排名 1-3 位 | 189 词 |
| 排名 4-10 位 | 601 词 |
| 排名 11-20 位 | 866 词 |

> 与 2026-07-02 旧快照相比：自然流量基本持平（31,100 vs 30,994），但**本轮明确抓到付费流量（689 词 / 16,872 流量 / $47K）**——这是旧报告漏掉的最大变化，也是本次核心新发现（见付费词与洞见 2）。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| deepgram.com（主站）| 6,588 | 29,266 | 94.10% |
| developers.deepgram.com | 747 | 1,567 | 5.04% |
| status.deepgram.com | 4 | 112 | 0.36% |
| console.deepgram.com | 24 | 79 | 0.25% |
| playground.deepgram.com | 35 | 64 | 0.21% |
| flux.deepgram.com | 9 | 10 | 0.03% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| deepgram | 1 | 27,100 | 42 | $4.79 | 21,680 | 品牌 | / |
| deepgram news | 1 | 1,900 | 39 | $16.91 | 1,520 | 信息 | /company/newsroom |
| deepgram pricing | 1 | 590 | 46 | $7.71 | 472 | 商业 | /pricing |
| deepgram api | 1 | 480 | 27 | $14.79 | 384 | 商业 | / |
| deepgram flux | 1 | 390 | 26 | $9.41 | 312 | 信息 | developers…/docs/flux（新产品）|
| deepgram api key | 1 | 390 | 35 | $14.91 | 312 | 商业 | developers…/create-additional-api-keys |
| deepgram ai | 1 | 260 | 46 | $8.84 | 208 | 信息 | / |
| deppgram（误拼）| 1 | 260 | 53 | $5.35 | 208 | 品牌 | / |
| deepgram company | 2 | 1,300 | 32 | $8.42 | 171 | 信息 | / |
| deepgram api key free | 1 | 210 | 25 | $17.19 | 168 | 商业 | developers… |
| deep gram（分开）| 1 | 210 | 54 | $18.72 | 168 | 品牌 | / |
| deepgram transcription | 1 | 170 | 25 | $9.48 | 136 | 商业 | / |
| deepgram careers | 1 | 480 | 14 | $1.73 | 119 | 招聘 | /careers |
| deepgram nova-3 | 1 | 140 | 37 | $6.23 | 112 | 信息 | developers…（最新 STT 模型）|
| deepgram tts | 1 | 140 | 20 | $11.09 | 112 | 信息 | /（TTS）|
| deepgram stt | 1 | 140 | 50 | $12.07 | 112 | 信息 | / |
| deepgram status | 1 | 140 | 9 | $0.00 | 112 | 信息 | status. |
| deepgram funding | 1 | 140 | 30 | $0.00 | 112 | 信息 | /learn/press-release-series-c |
| deegram（误拼）| 1 | 390 | 67 | $10.13 | 96 | 品牌 | / |
| endpointing（技术词）| 1 | 390 | 20 | $8.37 | 96 | 信息 | developers…/endpointing |
| deepgram speech to text | 1 | 110 | 43 | $5.58 | 88 | 商业 | / |
| deepgram docs | 1 | 110 | 56 | $15.03 | 88 | 信息 | developers…/home |
| speechgen.io（合作词）| 3 | 1,000 | 10 | $1.58 | 82 | 商业 | /voice-ai-apps/speechgen |
| free transcription | 5 | 2,400 | 50 | $1.99 | 72 | 信息 | /free-transcription |
| deepgram models | 1 | 90 | 50 | $7.48 | 72 | 信息 | developers…/docs/model |
| podcastle.ai（合作）| 2 | 720 | 20 | $3.02 | 59 | 信息 | /voice-ai-apps/podcastle |
| diarization | 4 | 2,400 | 34 | $47.48 | 57 | 信息 | developers…/diarization（CPC$47）|
| deepgram nova 3 | 1 | 210 | 19 | $6.23 | 52 | 信息 | developers… |
| ttmaker（合作）| 4 | 1,600 | 18 | $1.28 | 48 | 商业 | /voice-ai-apps/ttsmaker |
| online transcription tool | 3 | 590 | 74 | $2.61 | 48 | 信息 | /free-transcription |
| pipecat（开源框架）| 5 | 1,900 | 38 | $5.73 | 45 | 信息 | developers…/pipecat-integration |
| ntts（神经 TTS）| 4 | 5,400 | 28 | $0.47 | 43 | 信息 | /ai-glossary/neural-text-to-speech-ntts |
| deepgram login | 1 | 170 | 38 | $14.21 | 42 | 导航 | console…/login |
| podcastle ai（合作）| 2 | 1,600 | 35 | $3.02 | 41 | 信息 | /voice-ai-apps/podcastle |
| deepgram playground | 1 | 50 | 35 | $23.91 | 40 | 信息 | playground. |
| deepgram cost | 1 | 50 | 42 | $6.56 | 40 | 商业 | /pricing |
| deepgram voice agent api | 1 | 50 | 31 | $8.72 | 40 | 商业 | /product/voice-agent-api（新产品）|
| speech in speech（技术词）| 20 | 27,100 | 53 | $3.49 | 40 | 信息 | /learn/what-is-speech-to-speech |
| f2 score（借力词）| 1 | 140 | 20 | $0.00 | 34 | 信息 | /ai-glossary/f2-score |
| ai-coustics（合作）| 2 | 1,300 | 47 | $0.00 | 33 | 信息 | /voice-ai-apps/aicoustics |
| deepgram api pricing | 1 | 40 | 33 | $11.88 | 32 | 商业 | /pricing |
| deepgram aura 2 | 1 | 30 | 27 | $12.02 | 24 | 信息 | /learn/introducing-aura-2（企业 TTS）|
| deepgram asr | 1 | 30 | 20 | $12.58 | 24 | 商业 | / |
| deepgram startup program | 1 | 30 | 13 | $43.39 | 24 | 商业 | /startup-program |
| deepgram voice agent | 1 | 90 | 30 | $13.02 | 22 | 商业 | /product/voice-agent-api |
| expectation maximization（术语借力）| 12 | 8,100 | 37 | $0.58 | 24 | 信息 | /ai-glossary/expectation-maximization |

> 自然侧 90% 流量靠 `deepgram` 品牌词（27,100/mo，21,680 流量）+ 大量误拼变体（deppgram/deegram/deepgra/deep gram），其余是文档词（developers.）、术语词（/ai-glossary/、/learn/）与"合作应用词"（/voice-ai-apps/*，见洞见 4）。

### 付费词（Google Ads，按流量排序）—— 本轮最大新发现

**Deepgram 在大规模投放通用大词，几乎全部导向程序化 `/compare/X-vs-deepgram` 对比落地页与品类落地页**——这是一套被验证的 SEM + 程序化对比页打法：

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| text to speech free | 1 | 33,100 | $0.90 | /text-to-speech-api |
| ai voice | 1 | 27,100 | $1.06 | /voice-agent-api-deepgram |
| deepgram | 1 | 22,200 | $5.35 | /voice-ai-platform · /contact-us |
| application whisper | 2 | **18,100** | $1.32 | **/compare/openai-vs-deepgram** |
| elevenlabs text to speech | 1 | 12,100 | $1.41 | /compare/elevenlabs-vs-deepgram |
| audio to text | 1 | 12,100 | $1.51 | /the-top-rated-speech-to-text-api |
| google cloud text-to-speech | 1 | 6,600 | $4.45 | /compare/google-vs-deepgram |
| superwhisper | 1 | **6,600** | $1.94 | **saga.deepgram.com** |
| speech speech to text | 1 | 6,600 | $1.64 | /the-top-rated-speech-to-text-api |
| cartesia | 1 | 5,400 | $0.00 | /compare/cartesia-vs-deepgram |
| google speech-to-text | 1 | 4,400 | $1.76 | /compare/google-vs-deepgram |
| faster-whisper | 1 | **3,600** | $2.67 | **/compare/openai-vs-deepgram** |
| whisper web | 1 | 3,600 | $2.39 | /compare/openai-vs-deepgram |
| logiciel dragon speaking | 1 | 3,600 | $2.97 | /nuance-vs-deepgram |
| google cloud text to speech | 1 | 2,900 | $4.45 | /compare/google-vs-deepgram |

> **关键：Deepgram 花钱买 `application whisper`（18,100）、`faster-whisper`、`whisper web`、`superwhisper` 这些 Whisper/开源相关词，直接导向 `/compare/openai-vs-deepgram`**——它把"搜开源 Whisper 的人"当成付费获客目标。这正是 Olares 平替叙事的反向战场（见洞见 2）。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| elevenlabs alternative | 480 | **9** | $6.16 | 商业 | ⭐ 邻近赛道（TTS）|
| whisper alternative | 170 | **10** | $1.86 | 商业 | ⭐ |
| deepgram vs whisper | 50 | **21** | $15.09 | 对比 | ⭐ CPC$15，核心对比词 |
| deepgram vs elevenlabs | 50 | **0** | $16.71 | 对比 | ⭐ |
| deepgram vs openai | 50 | **20** | $0.00 | 对比 | ⭐ |
| deepgram alternatives | 30 | **2** | $12.03 | 商业 | ⭐ |
| deepgram vs assemblyai | 20 | **0** | $18.56 | 对比 | ⭐ CPC$18 |
| deepgram vs google | 20 | 0 | $0.00 | 对比 | ⭐ |
| whisper vs deepgram | 20 | 0 | $0.00 | 对比 | ⭐ |
| assemblyai alternative | 20 | 0 | $0.00 | 商业 | ⭐ |
| assemblyai vs deepgram | 20 | 0 | $6.44 | 对比 | ⭐ |
| deepgram alternative | 0 | 0 | $17.10 | 商业 | CPC$17，量待涨 |

**自然竞品（`domain_organic_organic`）**：assemblyai.com（共有 126 词）、vapi.ai、speechmatics.com、gladia.io、smallest.ai、murf.ai、pipecat.ai、livekit.io、meetjamie.ai、speechnotes.co。**付费竞品词还打到 Nuance（Dragon）、Google、ElevenLabs、Cartesia、OpenAI**。

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| text to speech | 246,000 | 87 | $0.39 | 信息 | 超级大词，排不动 |
| speech to text | 22,200 | 82 | $1.38 | 信息 | 超级大词 |
| audio to text | 12,100 | 50 | $1.38 | 信息 | Deepgram 付费在买 |
| transcribe audio | 6,600 | 37 | $1.63 | 商业 | |
| ntts（神经 TTS）| 5,400 | 28 | $0.47 | 信息 | ⭐ 术语借力词 |
| diarization | 2,400 | 34 | $47.48 | 信息 | CPC$47！低 KD 技术词 |
| free transcription | 2,400 | 50 | $1.99 | 信息 | |
| speech to text api | 720 | 58 | **$126.55** | 信息 | **CPC$126！企业 STT 采购词** |
| speaker diarization | 720 | 44 | $40.28 | 信息 | CPC$40 |
| speech recognition api | 590 | 69 | **$126.55** | 信息 | CPC$126 |
| text to speech api | 720 | 47 | $4.66 | 信息 | |
| tts api | 320 | 49 | $3.69 | 信息 | |
| real time transcription | 260 | 45 | $3.63 | 信息 | |
| transcription api | 90 | 38 | $58.66 | 信息 | CPC$58 |
| voice ai api | 70 | 38 | $3.68 | 信息 | |
| stt api | 20 | **0** | **$125.23** | 信息 | ⭐ KD0 + CPC$125，全组最高性价比 |

### 产品 / 功能词（deepgram 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deepgram pricing | 590 | 32 | $14.71 | 商业 | 定价词，CPC$14 |
| deepgram api | 480 | **27** | $14.79 | 商业 | ⭐ |
| deepgram flux | 390 | **26** | $9.41 | 信息 | ⭐ 新产品 |
| deepgram api key | 390 | 35 | $14.91 | 商业 | |
| deepgram ai | 260 | 46 | $8.84 | 信息 | |
| deepgram api key free | 210 | **25** | $17.19 | 商业 | ⭐ CPC$17 |
| deepgram transcription | 170 | **25** | $9.48 | 商业 | ⭐ |
| deepgram nova-3 / nova 3 | 210 | 19 | $6.23 | 信息 | ⭐ 最新 STT 模型 |
| deepgram tts | 140 | **20** | $11.09 | 信息 | ⭐ TTS 线 |
| deepgram stt | 140 | 50 | $12.07 | 信息 | |
| deepgram voice agent | 90 | 30 | $13.02 | 商业 | 语音 Agent |
| deepgram sdk | 90 | 34 | $16.31 | 信息 | |
| deepgram cost | 50 | 42 | $6.56 | 商业 | |
| deepgram voice agent api | 50 | 31 | $8.72 | 商业 | 新产品 |
| deepgram api pricing | 40 | 33 | $11.88 | 商业 | |
| deepgram asr | 30 | **20** | $12.58 | 商业 | ⭐ |
| is deepgram free / deepgram free | 20 | 0 | $0.00 | 信息 | 攻击面（免费质疑）|

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| whisper.cpp | 2,900 | 41 | $2.80 | 信息 | 开源 STT 引擎 |
| whisperx | 2,400 | **28** | $2.82 | 信息 | ⭐ **Olares Market「Whisper API」即基于 WhisperX** |
| kokoro tts | 2,400 | 64 | $2.58 | 信息 | 本地 TTS 明星模型 |
| coqui tts | 1,900 | 39 | $2.27 | 信息 | 开源 TTS |
| faster whisper | 1,600 | 33 | $2.80 | 信息 | 开源 STT 引擎 |
| whisper api | 1,300 | 60 | $4.21 | 信息 | **Olares「Whisper API」直接对标** |
| piper tts | 1,300 | **25** | $2.88 | 信息 | ⭐ 轻量本地 TTS |
| vosk | 1,300 | 40 | $2.86 | 信息 | 离线 STT |
| speaches | 720 | 50 | $4.06 | 信息 | **Olares Market 已上架（OpenAI 兼容 STT+TTS）** |
| open source tts | 260 | 32 | $5.48 | 商业 | |
| open source text to speech | 260 | 49 | $1.41 | 信息 | |
| open source speech to text | 210 | 35 | $2.38 | 信息 | 核心信号词 |
| bark tts | 210 | **27** | $2.24 | 信息 | ⭐ |
| parler tts | 170 | **30** | $3.93 | 信息 | ⭐ |
| kokoro tts github | 170 | 49 | $0.00 | 信息 | 找部署 |
| ollama whisper | 170 | **20** | $8.42 | 信息 | ⭐ 本地栈 |
| whisper stt | 140 | 58 | $2.33 | 信息 | |
| whisper local | 140 | 42 | $2.08 | 信息 | |
| run whisper locally | 110 | 33 | $6.32 | 信息 | 本地部署意图明确 |
| install whisper | 110 | 36 | $3.12 | 信息 | |
| whisper docker | 110 | **28** | $0.00 | 信息 | ⭐ 部署词 |
| distil whisper | 90 | 31 | $2.50 | 信息 | |
| whisper self hosted | 30 | 0 | $1.95 | 信息 | 语义完美 |
| open source transcription | 20 | 0 | $2.30 | 信息 | |
| open source stt | 20 | 0 | $0.00 | 信息 | |
| deepgram self hosted | 20 | 0 | $9.55 | 信息 | 攻击面（连它自己都强调自托管）|
| self hosted speech to text | 20 | 0 | $0.00 | 信息 | GEO 占位 |
| self hosted text to speech | 20 | 0 | $0.00 | 信息 | GEO 占位 |
| self hosted tts | 20 | 0 | $0.00 | 信息 | GEO 占位 |
| local speech to text / local transcription | 20-30 | 0-54 | $2.4 | 信息 | GEO |
| offline speech to text | 20 | 0 | $2.01 | 信息 | GEO |

> 相关信息词（问题词，`phrase_questions`）："what is speech to text"（390）、"how to do speech to text"（320）、"how does text to speech work"（260）等——适合放进本地转录教程/术语页做信息意图承接。

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Deepgram 是闭源、按分钟计费的语音 API（连它自己都在卖"自托管"给企业合规）；Olares 用 Market 已上架的 Whisper API（WhisperX）/ Whisper-WebUI / Speaches（OpenAI 兼容、含 Kokoro TTS）把整条语音栈搬到本地——本地 STT/TTS、无按分钟计费、音频与转写不出机、无 API Key/额度限制。** ⭐⭐⭐ = 契合度最高。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| ⭐⭐⭐ whisperx | 2,400 | **28** | $2.82 | Olares Market「Whisper API」即基于 WhisperX，一键装、本地转写；"whisperx on Olares / 自托管 WhisperX" |
| ⭐⭐⭐ faster whisper | 1,600 | 33 | $2.80 | 高性能本地 STT 引擎教程，导向 Olares 一键部署 |
| ⭐⭐⭐ piper tts | 1,300 | **25** | $2.88 | 轻量本地 TTS，KD25，配 Speaches on Olares |
| ⭐⭐⭐ open source speech to text | 210 | 35 | $2.38 | "best open-source self-hosted STT" 清单，落 Olares Whisper API |
| ⭐⭐⭐ deepgram vs whisper | 50 | **21** | $15.09 | 旗舰对比文："Deepgram（云/按分钟）vs Whisper on Olares（本地/零边际成本）"，CPC$15 |
| ⭐⭐⭐ stt api | 20 | **0** | **$125.23** | 先占！"self-hosted STT API"＝Speaches/Whisper API on Olares，OpenAI 兼容端点、CPC 全组最高 |
| ⭐⭐⭐ self hosted speech to text | 20 | **0** | $0.00 | 语义完美、KD0，权威内容占位（GEO）|
| ⭐⭐ whisper api | 1,300 | 60 | $4.21 | Olares Market「Whisper API」应用词直接命中；"自托管 Whisper API" |
| ⭐⭐ kokoro tts | 2,400 | 64 | $2.58 | Speaches on Olares 内置 Kokoro，"本地 Kokoro TTS 部署"教程 |
| ⭐⭐ whisper.cpp | 2,900 | 41 | $2.80 | 本地 STT 引擎科普 → Olares 一键方案 |
| ⭐⭐ coqui tts | 1,900 | 39 | $2.27 | 开源 TTS 部署，配 Olares |
| ⭐⭐ speaches | 720 | 50 | $4.06 | **Market 已上架应用词**，"Speaches on Olares：OpenAI 兼容本地 STT+TTS" |
| ⭐⭐ open source tts | 260 | 32 | $5.48 | 开源 TTS 清单，落 Speaches/Kokoro on Olares |
| ⭐⭐ ollama whisper | 170 | **20** | $8.42 | 本地 AI 栈（Ollama+Whisper）教程，Olares 全家桶 |
| ⭐⭐ whisper docker | 110 | **28** | $0.00 | 部署意图，Olares 比裸 Docker 更省心 |
| ⭐⭐ deepgram alternatives | 30 | **2** | $12.03 | KD2！"open-source self-hosted Deepgram alternative"＝Whisper+Kokoro on Olares |
| ⭐⭐ deepgram self hosted | 20 | 0 | $9.55 | 攻击面：它自托管仍闭源+企业合同；Olares 开源、个人可用、零门槛 |
| ⭐ deepgram pricing | 590 | 32 | $14.71 | 价格对比：$0.0043+/分钟 vs Whisper on Olares 本地零边际成本 |
| ⭐ deepgram api | 480 | **27** | $14.79 | "本地 STT API 替代 Deepgram API"，无额度/无 Key |
| ⭐ whisper alternative | 170 | **10** | $1.86 | 反向：把找 Whisper 替代的人接回"本地部署 Whisper on Olares" |
| ⭐ run whisper locally | 110 | 33 | $6.32 | 强本地意图，Olares 一键 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| whisper.cpp | 2,900 | 41 | $2.80 | 信息 | 次级 | 本地 STT 引擎科普词，导向 Olares 一键部署 |
| whisperx | 2,400 | 28 | $2.82 | 信息 | 主词候选 | KD28 + Olares Market 已有 Whisper API（WhisperX），应用词/教程双吃 |
| kokoro tts | 2,400 | 64 | $2.58 | 信息 | 主词候选 | 本地 TTS 明星，Speaches on Olares 内置 Kokoro，教程带部署 |
| diarization | 2,400 | 34 | $47.48 | 信息 | 主词候选 | 低 KD 高 CPC 技术词，建术语页 + 本地语音 Agent（Whisper+分离）|
| coqui tts | 1,900 | 39 | $2.27 | 信息 | 次级 | 开源 TTS 部署，配 Olares |
| pipecat | 1,900 | 38 | $5.73 | 信息 | 次级 | 实时语音 Agent 框架，Pipecat+Whisper+Kokoro 本地栈 |
| faster whisper | 1,600 | 33 | $2.80 | 信息 | 主词候选 | 高性能本地 STT，"faster-whisper 自托管"教程，Olares 部署 |
| whisper api | 1,300 | 60 | $4.21 | 信息 | 主词候选 | Olares Market「Whisper API」应用词直接命中；自托管 Whisper API |
| piper tts | 1,300 | 25 | $2.88 | 信息 | 主词候选 | KD25 轻量本地 TTS，Speaches on Olares |
| vosk | 1,300 | 40 | $2.86 | 信息 | 次级 | 离线 STT，本地方案清单 |
| speaches | 720 | 50 | $4.06 | 信息 | 主词候选 | Market 已上架应用词，OpenAI 兼容本地 STT+TTS on Olares |
| deepgram pricing | 590 | 32 | $14.71 | 商业 | 主词候选 | 价格攻击面：按分钟计费 vs Whisper on Olares 本地零边际成本 |
| deepgram api | 480 | 27 | $14.79 | 商业 | 次级 | 本地 STT API 替代，无额度/无 Key |
| open source tts | 260 | 32 | $5.48 | 商业 | 主词候选 | best open-source TTS 清单，落 Speaches/Kokoro on Olares |
| open source speech to text | 210 | 35 | $2.38 | 信息 | 主词候选 | best open-source self-hosted STT 清单，落 Olares Whisper API |
| ollama whisper | 170 | 20 | $8.42 | 信息 | 次级 | 本地 AI 栈教程，Olares 全家桶 |
| whisper alternative | 170 | 10 | $1.86 | 商业 | 次级 | KD10，反向接回"本地部署 Whisper on Olares" |
| deepgram tts | 140 | 20 | $11.09 | 信息 | 次级 | Kokoro/Piper on Olares 本地 TTS 替代 Aura-2 |
| deepgram vs whisper | 50 | 21 | $15.09 | 对比 | 主词候选 | 旗舰对比文，云按分钟 vs 本地零成本，CPC$15 |
| deepgram alternatives | 30 | 2 | $12.03 | 商业 | 主词候选 | KD2！open-source self-hosted Deepgram 替代＝Whisper+Kokoro on Olares |
| deepgram vs elevenlabs | 50 | 0 | $16.71 | 对比 | 次级 | 加入本地 TTS 三方对比，CPC$16 |
| stt api | 20 | 0 | $125.23 | 信息 | 主词候选 | KD0+CPC$125！先占"self-hosted STT API"＝Speaches on Olares |
| deepgram vs assemblyai | 20 | 0 | $18.56 | 对比 | GEO | 三方对比加 Whisper on Olares，进直答/FAQ |
| self hosted speech to text | 20 | 0 | $0.00 | 信息 | GEO | 语义完美 KD0，权威内容抢 AI 引用位 |
| deepgram self hosted | 20 | 0 | $9.55 | 信息 | GEO | 攻击其"闭源自托管"，Olares 开源个人可用 |
| whisper docker | 110 | 28 | $0.00 | 信息 | 次级 | 部署词，Olares 比裸 Docker 更省心 |

---

## 核心洞见

1. **品牌护城河：正面刚品牌词无意义，但品类护城河很薄。** `deepgram`（27,100）及海量误拼变体霸榜第 1，靠的是品牌心智——Olares 抢不到也不必抢。但 Deepgram 的**品类词几乎排不动**（text to speech KD87、speech to text KD82 全在别人手里），它自己也主要靠品牌词+付费买量+程序化对比页获客。真正的战场是**开源/自托管长尾**（whisperx、faster whisper、piper tts、open source stt…），这里 KD 普遍 25-40、Deepgram 无自然覆盖，是 Olares 的空档。

2. **本轮最大新发现＝Deepgram 的付费 + 程序化 `/compare/` 打法，且它在买 Whisper 词。** 它投放 `application whisper`（18,100）、`faster-whisper`、`whisper web`、`superwhisper` 等开源相关词，全部导向 `/compare/openai-vs-deepgram`——把"搜开源 Whisper 的人"当成付费获客目标。这既暴露了它的焦虑（开源 Whisper 是真实威胁），也给了 Olares 一套现成打法：**做同构的 `X vs Y` / `deepgram vs whisper` / `whisper alternative` 对比页，但落点是"本地部署 Whisper+Kokoro on Olares，零按分钟计费"**，从自然侧截住同一批人。

3. **对 Olares 最关键的 3 个词：`whisperx`（2,400/KD28）、`stt api`（20/KD0/CPC$125）、`deepgram alternatives`（30/KD2）。** whisperx 因 Olares Market 已上架「Whisper API」（基于 WhisperX）而可"应用词+教程"双吃、KD 可打；stt api 是 KD0 却 CPC$125 的极端性价比词，先占"self-hosted STT API＝Speaches on Olares"；deepgram alternatives KD 仅 2，直接写"开源自托管 Deepgram 替代"。三者共同指向一条内容主线：**用 Whisper API / Speaches / Whisper-WebUI 把整条语音栈本地化**。

4. **最大攻击面：按分钟计费 + 闭源"伪自托管"。** `deepgram pricing`（590/CPC$14.71）、`deepgram cost`、`is deepgram free`、`deepgram api key free` 密集出现，说明用户对其**用量计费**敏感；而 `deepgram self hosted`（KD0）揭示它虽宣传自托管，但仍是**闭源 + 企业合同**。Olares 叙事应双管齐下："Whisper on Olares＝本地零边际成本、无按分钟计费、无 API Key/额度" + "真正开源、个人即可自托管，不用签企业合同"。全品类词 CPC 极高（speech to text api / speech recognition api $126、diarization $47、transcription api $58），说明企业 STT 采购客单价极高——这类"降本"内容即便排名靠后 ROI 也高。

5. **隐藏低 KD 金矿：`deepgram alternatives`（KD2）、`whisper alternative`（KD10）、`elevenlabs alternative`（KD9）、`deepgram vs whisper`（KD21）、`bark tts`（KD27）、`piper tts`（KD25）、`whisper docker`（KD28）、`ollama whisper`（KD20）。** 竞争几乎为零且意图精准（要么找替代、要么要本地部署），配合 Olares Market 现成应用（Whisper API / Speaches / Whisper-WebUI），是低成本可抢的一批。

6. **GEO 前瞻布局：** `self hosted speech to text`、`self hosted text to speech`、`self hosted tts`、`open source stt`、`whisper self hosted`、`offline speech to text`、`deepgram self hosted`、`deepgram vs assemblyai` —— 目前近零量但语义与 Olares 完美契合。建议提前发权威内容占 AI Overview / Perplexity 引用位（"最好的自托管开源语音转文字方案"这类问题的直答）。

7. **与既有分析的关联：** 本报告的"本地语音栈（STT+TTS+语音 Agent）"叙事补齐了 `olares-500-keywords` 中语音/转录品类的缺口——whisperx / faster whisper / piper tts / kokoro tts / speaches 等词均直接对应 Olares Market 已上架应用（[whisper-api](/Users/pengpeng/seo/directions/market/reports/whisper-api.md)、[whisper-webui](/Users/pengpeng/seo/directions/market/reports/whisper-webui.md)、[speaches](/Users/pengpeng/seo/directions/market/reports/speaches.md)），建议将"本地语音/STT-TTS"作为独立子品类补入词表，并与 Pipecat 实时语音 Agent 场景串联。

---

*数据来源：SEMrush us 数据库（domain_rank / domain_organic_subdomains / resource_organic / resource_adwords / domain_organic_organic / phrase_these / phrase_related / phrase_fullsearch / phrase_questions）| 2026-07-07*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
