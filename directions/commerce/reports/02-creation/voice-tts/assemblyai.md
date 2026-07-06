# AssemblyAI SEO 竞品分析报告

> 域名：assemblyai.com | SEMrush us | 2026-07-07
> AssemblyAI = 面向开发者的**语音识别（STT）+ 语音理解 API**——把音频转文字 + 说话人分离/摘要/情感等模型能力打包成一套云端 API，按用量计费。估值约 $300M / 累计融资 $158M。

---

## 项目理解（前置）

AssemblyAI 是一家开发者优先的语音 AI 公司，核心产品是一套 STT/语音理解云 API：上传音频 → 返回转写文本 + 说话人分离（diarization）、自动章节、摘要、情感分析、内容审核，以及基于 LLM 的音频问答（LeMUR）。它把"训练/托管语音大模型"这件重活抽象成一条 REST/SDK 调用，卖给要在产品里加语音功能的工程团队（会议记录、呼叫中心、播客、字幕、医疗转写等）。它是闭源商业 API，最大的开源对立面就是 OpenAI 的 **Whisper**——这也是它自己买词、做对比页（`/compare/whisper-vs-assemblyai`）主动防守的对象。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开发者向语音识别 + 语音理解 API（STT-as-a-Service） |
| 开源 / 许可证 | ❌ 闭源商业 SaaS（模型不开放，仅 API/SDK） |
| 主仓库 | 无开源本体；GitHub 仅 SDK/示例（`AssemblyAI/assemblyai-python-sdk` 等） |
| 核心功能 | ① STT 转写（Universal 模型）② 说话人分离 ③ 摘要/自动章节 ④ 情感/实体/内容审核 ⑤ LeMUR（LLM 音频问答） |
| 商业模式 / 定价 | 按用量计费，STT 约 **$0.12–0.37/小时音频**（异步/实时不同档），语音理解功能叠加计费 |
| 差异化 / 价值主张 | 单一 API 拿到"转写 + 理解"全套、准确率与企业级 SLA、开箱即用无需自训模型 |
| 主要竞品（初判）| Deepgram、Gladia、Speechmatics、Rev AI、Google/AWS STT；开源侧 OpenAI Whisper |
| Olares Market | 平替**已上架**：`whisper-api`（WhisperX 之上的 FastAPI 服务）、`whisper-webui`、`speaches`（OpenAI 兼容 TTS/STT server） |
| 来源 | assemblyai.com（官网/pricing/compare）、GitHub SDK、Semrush 竞品报告 |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | assemblyai.com |
| SEMrush Rank | 158,881（SEO 偏弱，中长尾体量） |
| 自然关键词数 | 3,882 |
| 月自然流量（US）| 11,542 |
| 自然流量估值 | **$70,085/月** |
| 付费关键词数 | 216 |
| 月付费流量 | 4,214 |
| 排名 1-3 位 | 179 词 |
| 排名 4-10 位 | 580 词 |
| 排名 11-20 位 | 688 词 |

> 读数：只有 179 个词进前三，却有 688 个词卡在 11-20 位——大量内容"排到第二页上不来"。自然流量估值 $70K/月但 rank 15 万开外，说明流量高度集中在少数高价词与品牌词上，而非靠体量。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.assemblyai.com（主站）| 3,745 | 11,496 | 99.60% |
| assemblyai.com（裸域）| 134 | 46 | 0.40% |
| status.assemblyai.com | 3 | 0 | 0% |

> 结构极简：几乎全部流量在主站，没有独立 docs./blog. 子域分流——博客、文档、compare 页都挂在 `www` 下的子目录（`/blog/`、`/docs/`、`/compare/`、`/products/`、`/features/`）。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| assembly ai | 1 | 2,900 | 59 | $7.24 | 2,320 | 品牌 | / |
| assemblyai | 1 | 2,400 | 67 | $7.83 | 1,920 | 品牌 | / |
| assembly ia（变体）| 1 | 1,600 | 35 | $3.06 | 1,280 | 品牌 | / |
| automatic speech recognition | 1 | 5,400 | 63 | $3.94 | 712 | 信息 | /blog/what-is-asr |
| assemby ai（误拼）| 1 | 210 | 66 | — | 168 | 品牌 | / |
| assemblyia（误拼）| 1 | 140 | 66 | $7.83 | 112 | 品牌 | / |
| assembly ai playground | 1 | 110 | 23 | $7.15 | 88 | 信息 | /playground |
| assembly ai pricing | 1 | 110 | 25 | $6.05 | 88 | 商业 | /pricing |
| assembleai（误拼）| 1 | 110 | 54 | $9.02 | 88 | 品牌 | / |
| correct speaker label（借力）| 5 | 3,600 | **18** | — | 86 | 信息 | /blog/speaker-diarization… |
| speaker label in transcription（借力）| 2 | 3,600 | **15** | — | 86 | 信息 | /blog/speaker-diarization… |
| assemble ai（变体）| 3 | 1,300 | 65 | $6.07 | 84 | 信息 | / |
| ai powered playgrounds（借力）| 1 | 590 | **12** | — | 77 | 信息 | /blog/6-best-ai-playgrounds |
| automatic speech recognition system | 1 | 480 | 60 | — | 63 | 信息 | /blog/what-is-asr |
| llm use cases（借力）| 2 | 720 | 30 | $4.09 | 59 | 信息 | /blog/llm-use-cases |
| conversation analytics software（借力）| 2 | 720 | 28 | — | 59 | 信息 | /blog/conversation-intelligence… |
| diffusion model（借力）| 5 | 4,400 | 57 | $3.93 | 57 | 信息 | /blog/diffusion-models… |
| dalle 2（借力）| 7 | 2,400 | 79 | $0.99 | 52 | 信息 | /blog/how-dall-e-2… |
| diarization（借力）| 5 | 2,400 | 34 | **$47.48** | 52 | 信息 | /blog/top-speaker-diarization… |
| conversational intelligence software | 3 | 720 | 33 | $19.44 | 46 | 信息 | /blog/conversation-intelligence… |
| make a python voice assistant（借力）| 4 | 1,900 | 23 | — | 45 | 信息 | /blog/real-time-ai-voice-bot-python |
| diffusion artificial intelligence（借力）| 2 | 320 | 41 | $1.09 | 42 | 信息 | /blog/diffusion-models… |
| assembly ai api | 1 | 50 | 20 | $7.16 | 40 | 商业 | / |
| assemblyai speaker diarization | 1 | 50 | 20 | — | 40 | 信息 | /features/speaker-diarization |
| sales call transcript analysis metrics（借力）| 2 | 480 | **6** | — | 39 | 信息 | /blog/call-center-metrics |
| florence-2（借力）| 7 | 1,900 | 47 | — | 36 | 信息 | /blog/florence-2… |
| chapter auto | 1 | 260 | 30 | — | 34 | 信息 | /docs/speech-understanding/… |
| assembly ai stt | 1 | 40 | 22 | $7.04 | 32 | 商业 | /products/speech-to-text/ |
| speech to text api（借力）| 4 | 720 | 58 | **$126.55** | 31 | 信息 | /blog/the-top-free-speech-to-text-apis… |
| dragon medical small practice（借力）| 6 | 720 | **5** | — | 25 | 信息 | /blog/dragon-medical-alternatives |
| speaker diarization | 6 | 720 | 44 | $40.28 | 21 | 信息 | /blog/top-speaker-diarization… |
| voice recognition api | 5 | 590 | 70 | **$126.55** | 20 | 商业 | / |
| sentiment analysis api（借力）| 2 | 260 | 20 | $7.55 | 21 | 信息 | /blog/best-apis-for-sentiment… |
| assemblyai pricing | 1 | 70 | **11** | $6.12 | 17 | 商业 | /pricing |

> 自然流量结构：① **品牌词 + 海量误拼变体**（assembly ai / assemblyai / assembly ia / assemby ai / assembleai / asembly ai…全部第 1）撑起约一半流量；② 一批**博客"借力词"**——用 ASR/diarization/DALL-E/diffusion/Florence-2 等技术解说文截获与产品无关的信息流量；③ 真正的商业/产品词（api、pricing、stt）量都很小（50–110/mo），但 KD 极低（11–25）。

### 付费词（Google Ads，按流量排序）

AssemblyAI 在**买竞品名 + 品类大词**，几乎全部导向 `/compare/<竞品>-vs-assemblyai` 与产品页——这是它最值得抄的打法：

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| whisper ai | 1 | 9,900 | $1.90 | **/compare/whisper-vs-assemblyai** |
| deepgram | 2 | 22,200 | $5.35 | **/compare/deepgram-vs-assemblyai** |
| gladia | 1 | 5,400 | $1.65 | /products/ |
| ai transcription | 1 | 5,400 | $2.93 | /speech-to-text-api |
| whisper openai | 1 | 2,400 | $2.43 | /compare/whisper-vs-assemblyai |
| diarization | 1 | 2,400 | $47.48 | /explore/speaker-diarization |
| speaker label in transcription | 1 | 2,900 | — | /explore/speaker-diarization |
| transcript ai | 1 | 1,900 | $2.33 | /speech-to-text-api |
| best speech to text | 2 | 2,400 | — | /speech-to-text-api |
| speech to text ai | 1 | 720 | $5.77 | /speech-to-text-api |
| speaker diarization | 1 | 720 | $40.28 | /explore/speaker-diarization |

> 打法：**买对手品牌词（deepgram 22K、whisper ai 9.9K、gladia 5.4K）导向自建对比页**——用户搜竞品，先被 AssemblyAI 的 "X vs AssemblyAI" 页拦截。这套 `/compare/` + `/explore/` 程序化落地页正是 Olares 可复制的模式（见核心洞见 2）。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deepgram | 22,200 | 58 | $5.35 | 品牌 | 头号竞品品牌词 |
| whisper ai | 9,900 | 81 | $1.90 | 信息 | 开源对立面（含消费级 Whisper app 混淆）|
| gladia | 4,400 | 41 | $3.57 | 品牌 | 竞品 |
| rev ai | 2,400 | 48 | $4.03 | 品牌 | 竞品 |
| speechmatics | 1,600 | 33 | $9.02 | 品牌 | 竞品 |
| deepgram pricing | 590 | 32 | $14.71 | 商业 | 对手定价词 |
| deepgram vs whisper | 50 | **21** | $15.09 | 对比 | ⭐ 三方对比切入 |
| speech to text open source | 50 | 36 | $2.01 | 信息 | |
| assemblyai vs deepgram | 20 | **0** | $6.44 | 对比 | ⭐ |
| deepgram vs assemblyai | 20 | **0** | $18.56 | 对比 | ⭐ 高 CPC |
| whisper vs assemblyai | 20 | **0** | — | 对比 | ⭐ |
| assemblyai vs whisper | 20 | **0** | — | 对比 | ⭐ |
| whisper vs deepgram | 20 | **0** | — | 对比 | ⭐ |
| assemblyai alternative | 20 | **0** | — | 商业 | ⭐ |
| deepgram alternative | 0 | **0** | $17.10 | 商业 | ⭐ 高 CPC 近零量 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| speech to text | 22,200 | 82 | $1.38 | 信息 | 品类超级大词 |
| transcribe audio to text | 18,100 | 52 | $2.36 | 信息 | |
| audio transcription | 12,100 | 50 | $1.63 | 信息 | |
| audio to text | 12,100 | 50 | $1.38 | 信息 | |
| video transcription | 9,900 | 74 | $1.07 | 信息 | |
| transcribe audio | 6,600 | 37 | $1.63 | 信息 | |
| automatic speech recognition | 5,400 | 64 | $3.03 | 信息 | ASR 术语词 |
| ai transcription | 5,400 | 64 | $3.36 | 信息 | |
| transcription software | 2,900 | 70 | $3.56 | 商业 | |
| subtitle generator | 2,400 | 58 | $1.25 | 信息 | |
| transcription service | 2,400 | 88 | $8.04 | 商业 | |
| dictation software | 1,900 | 41 | $3.08 | 商业 | |
| conversation intelligence | 1,600 | 41 | $8.40 | 信息 | |
| speech analytics | 1,600 | 50 | $7.93 | 信息 | |
| speech ai | 1,300 | 77 | $1.20 | 信息 | |
| best transcription software | 880 | 40 | $6.21 | 商业 | |
| speech to text api | 720 | 58 | **$126.55** | 信息 | 全组最高 CPC |
| text to speech api | 720 | 47 | $4.66 | 信息 | |
| speaker diarization | 720 | 44 | $40.28 | 信息 | 高 CPC |
| speech recognition api | 590 | 69 | **$126.55** | 信息 | 高 CPC |
| meeting transcription | 590 | 85 | $4.82 | 信息 | |
| voice recognition api | 590 | 70 | **$126.55** | 商业 | 高 CPC |
| call transcription | 590 | 29 | $4.50 | 信息 | ⭐ |
| podcast transcription | 480 | **19** | $1.93 | 信息 | ⭐ |
| real time transcription | 260 | 45 | $3.63 | 信息 | |
| best speech to text api | 90 | 36 | $9.50 | 信息 | |
| transcription api | 90 | 38 | $58.66 | 信息 | 高 CPC |
| voice ai api | 70 | 38 | $3.68 | 信息 | |
| free speech to text api | 110 | 31 | $2.40 | 信息 | |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| assembly ai pricing | 110 | 25 | $6.05 | 商业 | ⭐ |
| assemblyai pricing | 70 | **11** | $6.12 | 商业 | ⭐ 全组最低 KD |
| assembly ai playground | 110 | 23 | $7.15 | 信息 | ⭐ |
| assembly ai api | 50 | 20 | $7.16 | 商业 | ⭐ |
| assemblyai speaker diarization | 50 | 20 | — | 信息 | ⭐ |
| assemblyai playground | 50 | 28 | $17.36 | 信息 | ⭐ 高 CPC |
| assembly ai stt | 40 | 22 | $7.04 | 商业 | ⭐ |
| assemblyai api | 30 | 40 | $7.08 | 商业 | |
| assemblyai transcription | 30 | 24 | $9.76 | 商业 | ⭐ |
| assemblyai speech to text | 30 | 0 | $7.06 | 商业 | ⭐ |
| assemblyai python | 20 | 0 | — | 信息 | ⭐ |
| assemblyai sentiment analysis | 20 | 0 | $4.42 | 信息 | ⭐ |
| assemblyai free | 20 | 0 | — | 商业 | ⭐ |
| lemur assemblyai | 20 | 0 | — | 信息 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| openai whisper | 6,600 | 97 | $2.56 | 品牌 | 开源模型旗舰词（难） |
| faster whisper | 1,600 | 33 | $2.80 | 信息 | ⭐ 高性能引擎 |
| faster-whisper | 3,600 | **29** | $2.80 | 信息 | ⭐ |
| whisper.cpp | 2,900 | 41 | $2.80 | 信息 | 本地推理引擎 |
| whisperx | 2,400 | **28** | $2.82 | 信息 | ⭐ Olares whisper-api 底座 |
| whisper cpp | 1,600 | 34 | $2.29 | 信息 | |
| whisper api | 1,300 | 60 | $4.21 | 信息 | |
| openai whisper api | 1,300 | 50 | $5.09 | 信息 | |
| whisper large v3 | 390 | 46 | $2.58 | 信息 | 型号词 |
| open source speech to text | 210 | 35 | $2.38 | 信息 | |
| whisper self hosted | 30 | **0** | $1.95 | 信息 | ⭐ 精准 |
| local speech to text | 30 | 54 | $2.37 | 信息 | |
| local whisper | 20 | **0** | — | 信息 | ⭐ |
| self hosted speech to text | 20 | **0** | — | 信息 | ⭐ 语义完美契合 |
| open source transcription | 20 | **0** | $2.30 | 信息 | ⭐ |
| asr api | 10 | **0** | $6.27 | 商业 | ⭐ |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：AssemblyAI 是闭源、按音频时长（约 $0.12–0.37/小时）计费的云 STT API；Olares Market 已上架 `whisper-api`（WhisperX + FastAPI，REST 接口）、`speaches`（OpenAI 兼容 STT/TTS server）、`whisper-webui`——在自己的 Olares 上跑本地 Whisper，得到一个可直接替换 AssemblyAI 调用的 STT 端点，转写次数/时长无限、零按量计费、音频不出设备。** `⭐⭐⭐/⭐⭐/⭐` 标契合度。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| ⭐⭐⭐ speech to text api | 720 | 58 | **$126.55** | 全报告最高 CPC——企业为 STT API 付出极高单价。Olares 上 Whisper API/Speaches 给你一个 OpenAI 兼容的本地 STT 端点，调用无限、零成本 |
| ⭐⭐⭐ whisperx | 2,400 | **28** | $2.82 | Olares `whisper-api` 就是 WhisperX 之上的 FastAPI 服务——"一键在 Olares 上部署 WhisperX，得到带说话人分离的本地转写 API" |
| ⭐⭐⭐ faster-whisper | 3,600 | **29** | $2.80 | "在 Olares 上跑 faster-whisper 本地转写"教程，性能级替代 AssemblyAI 异步转写 |
| ⭐⭐⭐ assemblyai pricing | 70 | **11** | $6.12 | KD=11！采购决策词：AssemblyAI $0.12–0.37/小时 vs Whisper on Olares 一次部署零边际成本 |
| ⭐⭐⭐ whisper self hosted | 30 | **0** | $1.95 | "自托管 Whisper"教程，Olares Market 一键安装 whisper-api，REST 接口替代 AssemblyAI |
| ⭐⭐⭐ self hosted speech to text | 20 | **0** | — | 语义完美契合，抢"自托管 STT"直答位 |
| ⭐⭐⭐ deepgram vs assemblyai | 20 | **0** | $18.56 | 对比页加第三选项：Deepgram vs AssemblyAI vs 本地 Whisper（Olares，永久免费）|
| ⭐⭐⭐ assemblyai alternative | 20 | **0** | — | "AssemblyAI 开源替代"= Whisper on Olares，正面接需求 |
| ⭐⭐ deepgram vs whisper | 50 | **21** | $15.09 | 高 CPC 三方对比词，落点在"Whisper 可本地跑、Deepgram/AssemblyAI 不行" |
| ⭐⭐ open source speech to text | 210 | 35 | $2.38 | 品类清单页，Whisper/WhisperX/faster-whisper + Olares 部署 |
| ⭐⭐ whisper cpp | 1,600 | 34 | $2.29 | 本地推理引擎，CPU 也能跑，Olares 低门槛部署角度 |
| ⭐⭐ podcast transcription | 480 | **19** | $1.93 | 场景词：在自己 Olares 上批量转写播客，不按分钟付费 |
| ⭐⭐ call transcription | 590 | 29 | $4.50 | 场景词：呼叫/会议本地转写，数据合规不外传 |
| ⭐ open source transcription | 20 | **0** | $2.30 | GEO 占位 |
| ⭐ local whisper | 20 | **0** | — | GEO 占位 |
| ⭐ whisper语音识别 | 1,600 | **21** | — | 中文词：面向中文用户"本地跑 Whisper 做语音识别" |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| speech to text api | 720 | 58 | **$126.55** | info | 主词候选 | CPC 全报告最高！Whisper API/Speaches on Olares = 本地 OpenAI 兼容 STT 端点，无限调用零成本 |
| faster-whisper | 3,600 | 29 | $2.80 | info | 主词候选 | 低 KD 高性能引擎，"在 Olares 上部署 faster-whisper 本地转写" |
| whisperx | 2,400 | 28 | $2.82 | info | 主词候选 | Olares `whisper-api` 底座，直接对应产品，KD28 可排 |
| whisper cpp | 1,600 | 34 | $2.29 | info | 次级 | CPU 本地推理，低门槛部署 |
| open source speech to text | 210 | 35 | $2.38 | info | 主词候选 | 品类清单页 + Olares 一键部署，承接"开源 STT"需求 |
| podcast transcription | 480 | 19 | $1.93 | info | 主词候选 | 场景词低 KD，本地批量转写不按分钟计费 |
| call transcription | 590 | 29 | $4.50 | info | 次级 | 呼叫/会议本地转写，合规角度 |
| assemblyai pricing | 70 | 11 | $6.12 | comm | 主词候选 | KD=11！采购决策词，成本对比一篇可排第一 |
| deepgram pricing | 590 | 32 | $14.71 | comm | 次级 | 对手定价词，导向本地零成本 |
| deepgram vs whisper | 50 | 21 | $15.09 | 对比 | 次级 | 高 CPC 三方对比，Whisper 可本地跑是差异点 |
| assemblyai alternative | 20 | 0 | — | comm | 次级 | 开源替代直接接需求 |
| deepgram vs assemblyai | 20 | 0 | $18.56 | 对比 | 次级 | 加第三选项 Whisper on Olares |
| whisper self hosted | 30 | 0 | $1.95 | info | 主词候选 | 自托管 Whisper 教程，Olares Market 一键装 |
| self hosted speech to text | 20 | 0 | — | info | GEO | 近零量语义完美契合，抢直答位 |
| assemblyai vs whisper | 20 | 0 | — | 对比 | GEO | 品牌方自己都在做的对比，反向占位 |
| whisper语音识别 | 1,600 | 21 | — | info | 次级 | 中文本地语音识别，面向中文用户 |

---

## 核心洞见

1. **品牌护城河：弱，可绕不可正刚。** SEMrush Rank 158,881、月自然流量仅 11.5K，自然词近一半是品牌词与海量误拼变体（assembly ai / assembly ia / assemby ai / assembleai…全部第 1）。品牌心智那部分抢不动也不必抢；但除了品牌词，它在通用品类/产品词上几乎没有稳固排名（688 个词卡在第二页），**非品牌内容空间对 Olares 几乎无阻力**。

2. **最该抄的打法：`/compare/<竞品>-vs-assemblyai` 程序化对比页 + 买对手品牌词。** AssemblyAI 花钱买 `deepgram`（22K）、`whisper ai`（9.9K）、`gladia`（5.4K），全部导向自建的 "X vs AssemblyAI" 对比页拦截需求。Olares 完全可以同构做一套 **"AssemblyAI vs Whisper（本地）"/"Deepgram vs Whisper on Olares"** 对比页矩阵——而且这些对比词 KD 普遍为 0，自然排名成本极低。

3. **对 Olares 最关键的 3 个词：`speech to text api`（720, KD58, CPC $126.55）、`faster-whisper`（3,600, KD29）、`whisperx`（2,400, KD28）。** 第一个是全报告乃至同批报告里最高 CPC 的词，说明 STT API 的商业价值极高，而 Olares 上 `whisper-api`/`speaches` 提供的正是"OpenAI 兼容的本地 STT 端点"——一次部署、无限调用、零按量费。后两个直接对应 Olares Market 已上架应用的底层引擎（`whisper-api` = WhisperX），KD 低到可排，是"应用词 + 部署教程词"双吃的入口。

4. **最大攻击面：按音频时长计费 + 数据外传。** `assemblyai pricing`（KD11）、`deepgram pricing`（KD32）、`assemblyai vs deepgram`（$18.56 CPC）密集出现，说明用户对 STT API 的**用量计费高度敏感**。Olares 叙事直击两点：① 一次部署零边际成本（大批量转写播客/呼叫记录不再按分钟烧钱）；② 音频不出设备（医疗/法律/呼叫中心的合规刚需）——这正好呼应 `call transcription`、`podcast transcription` 等场景词。

5. **隐藏低 KD 金矿：开源引擎词族。** `faster-whisper`（KD29, 3.6K）、`whisperx`（KD28, 2.4K）、`whisper cpp`（KD34, 1.6K）量不小且 KD 远低于品类大词（`speech to text` KD82、`openai whisper` KD97 打不动）。配合 Olares Market 已上架的 `whisper-api`/`speaches`，每个引擎一篇"在 Olares 上部署 X"教程即可低成本抢占。

6. **GEO 前瞻布局：** `self hosted speech to text`（KD0）、`whisper self hosted`（KD0）、`local whisper`（KD0）、`assemblyai alternative`（KD0）、`assemblyai vs whisper`（KD0）目前近零量，但语义与 Olares 完美契合。提前发布权威的"自托管 STT / AssemblyAI 开源替代"内容占位，抢 AI Overview / Perplexity 引用位——这批词后续会在内容层聚进"self-hosted STT"簇。

7. **与既有分析的关联：** 本报告的"本地 Whisper 替代云 STT API"叙事，与 voice-tts 目录下的 TTS 侧（Fish Speech、OpenedAI Speech、Speaches）互为镜像——STT + TTS 可合并成一条"在 Olares 上自建完整语音栈（转写 + 合成），替代 AssemblyAI/ElevenLabs 等按量计费 API"的主线，补入 `olares-500-keywords` 词表中目前偏薄的"本地语音"品类。

---

*数据来源：SEMrush us 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-07*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
