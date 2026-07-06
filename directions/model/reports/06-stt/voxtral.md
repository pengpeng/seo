# Voxtral 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：mistral.ai（官方页）+ HuggingFace，Apache 2.0
> **有官方页但无独立域名**：Voxtral 托管于 mistral.ai 主站（`/news/voxtral/`），SEO 流量与 Mistral 其他产品混合。Phase 1 跳过域名流量基线（混杂无法剥离），直接从关键词层面起步。

---

## 模型理解（前置）

Voxtral 是 Mistral AI 于 2025 年 7 月发布的多模态音频模型系列（论文 arXiv:2507.13264），支持**语音转写、多语言翻译、音频理解与问答**。家族现包含四条产品线：用于批量转写的 Voxtral Mini Transcribe 2（基于 Mini 3B/~5B 实际参数）、用于对话理解的 Voxtral Small 24B、用于实时流式转写的 Voxtral Mini 4B Realtime（2602，Apache 2.0 开源）以及 Voxtral 4B TTS（文本转语音，2603）。全系 Apache 2.0，可本地自托管，是 Whisper API 与 ElevenLabs Scribe 的高性价比开源替代。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 语音转写 + 音频理解多模态模型；Whisper API / ElevenLabs Scribe 的开源对标，性价比超半价 |
| 许可证 | **Apache 2.0**（商用友好，可自托管、二次分发，主推卖点成立） |
| 主仓库 / 分发 | [HF mistralai/Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)（~251K 月下载量）；[HF mistralai/Voxtral-Small-24B-2507](https://huggingface.co/mistralai/Voxtral-Small-24B-2507)；GitHub llama.cpp 已合并支持（2025 年下半年）；Ollama 支持尚在 Feature Request 阶段（#11432） |
| 参数 / VRAM 可跑性 | Mini 3B（实际含音频编码器约 4.7-5B 参数）**≈ 9.5 GB VRAM**（bf16/fp16），消费级 RTX 4060 Ti 16GB 可跑，**Olares One 24GB 可舒适运行**；Small 24B **≈ 55 GB VRAM**（bf16），需多卡或高端配置；Mini 4B Realtime ≥16 GB VRAM；TTS 4B ≥16 GB VRAM |
| 变体 / 型号 | Voxtral-Mini-3B-2507（批量转写/理解）、Voxtral-Small-24B-2507（高精度转写/理解）、Voxtral-Mini-4B-Realtime-2602（实时流式，Apache 2.0）、Voxtral-4B-TTS-2603（文本转语音）；32K 上下文 = 最长 40 分钟音频 |
| 闭源对标 | **OpenAI Whisper API**（$0.006/min，Mini Transcribe 成本不足其一半）、**ElevenLabs Scribe**（Small 精度持平，价格不足其一半）、AssemblyAI、Deepgram |
| Olares Market | **vLLM ✅ 已在 Olares Market**（Voxtral 官方推荐的部署引擎，需 vLLM ≥0.10.0）；Ollama 暂不支持；可通过 vLLM 在 Olares 一键部署 Voxtral Mini |
| 来源 | [mistral.ai/news/voxtral/](https://mistral.ai/news/voxtral/)；[HF Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)；[arXiv 2507.13264](https://arxiv.org/abs/2507.13264) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| voxtral tts | 170 | 35 | $4.48 | info/comm |
| voxtral 4b tts 2603 | 170 | 0 | $0.33 | comm ⭐ |
| mistral voxtral | 90 | 42 | $3.91 | info/nav |
| voxtral mini | 90 | 34 | $0 | info ⭐ |
| voxtral realtime | 50–70 | 0 | $0 | info ⭐ |
| voxtral ai | 50 | 0 | $6.80 | info ⭐ |
| voxtral small | 40–70 | 0 | $0 | info ⭐ |
| voxtral 3b | 20 | 0 | $0 | info ⭐ |
| voxtral api | 20 | 0 | $0 | info ⭐ |
| voxtral mini transcribe | 20 | 0 | $0 | info ⭐ |
| voxtral transcription | 20 | 0 | $0.12 | info ⭐ |
| voxtral speech to text | 30 | 0 | $0 | info ⭐ |
| voxtral transcribe | 30 | 0 | $0.02 | info ⭐ |
| voxtral models | 30 | 0 | $0.03 | info ⭐ |
| mistral transcription | 30 | 0 | $0.10 | info ⭐ |
| voxtral paper | 40 | 0 | $0 | info ⭐ |
| voxtral supported languages | 30 | 0 | $0 | info ⭐ |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| vllm voxtral | 20 | 0 | $0 | info ⭐ |
| voxtral vllm | 20 | 0 | $0.33 | info ⭐ |
| voxtral huggingface | 20–40 | 0 | $0 | nav ⭐ |
| voxtral github | 30 | 0 | $0 | nav ⭐ |
| voxtral ollama | 0 | 0 | $0 | info（无量，GEO 候补） |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| run voxtral locally | 10 | 0 | $0 | info ⭐ |
| voxtral local | <10 | 0 | $0 | info（GEO 候补） |
| voxtral vram | <10 | 0 | $0 | info（GEO 候补） |
| voxtral install | <10 | 0 | $0 | info（GEO 候补） |
| local audio transcription | 20 | 0 | $3.77 | info ⭐ |
| self hosted speech to text | 20 | 0 | $0.33 | info ⭐ |
| audio transcription open source | 20 | 0 | $2.49 | info ⭐ |
| local transcription | 20 | 0 | $3.50 | info ⭐ |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| whisper api | 1,300 | 60 | $4.21 | info/comm |
| openai whisper | 6,600 | 97 | $2.56 | nav |
| elevenlabs scribe | 260 | 32 | $5.69 | comm ⭐ |
| transcription model | 480 | 39 | $1.79 | info |
| speech recognition api | 590 | 69 | $126.55 | comm |
| transcription api | 90 | 38 | $58.66 | comm |
| open source speech recognition | 170 | 31 | $1.99 | info ⭐ |
| whisper large v3 | 390 | 46 | $2.58 | info |
| open source speech to text | 210 | 35 | $2.38 | info ⭐ |
| voxtral vs whisper | 20 | 0 | $0 | info ⭐ |
| open source elevenlabs | 30 | 0 | $7.60 | info ⭐ |
| open source whisper | 20 | 0 | $3.84 | info ⭐ |
| local speech to text | 30 | 0 | $2.37 | info ⭐ |
| open source asr | 20 | 0 | $0 | info ⭐ |
| audio understanding model | 20 | 0 | $0.33 | info ⭐ |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-------------|--------|
| voxtral vllm / vllm voxtral | 20+20 | 0 | $0 | vLLM 已在 Olares Market，Voxtral Mini 可在 Olares 一键部署 | ⭐⭐⭐ |
| run voxtral locally | 10 | 0 | $0 | 直接对接"Olares One 本地跑 Voxtral Mini"叙事，隐私保护不出机 | ⭐⭐⭐ |
| self hosted speech to text | 20 | 0 | $0.33 | Olares = 自托管平台，Voxtral 是最新一代 STT 选择 | ⭐⭐⭐ |
| local audio transcription | 20 | 0 | $3.77 | Olares One 24GB 跑 Voxtral Mini，会议记录/本地转写场景 | ⭐⭐⭐ |
| open source elevenlabs | 30 | 0 | $7.60 | Voxtral（含 TTS 4B）可作 ElevenLabs 开源平替，CPC 高有商业意图 | ⭐⭐⭐ |
| voxtral vs whisper | 20 | 0 | $0 | 攻击面：Voxtral Mini Transcribe 精度优于 Whisper，成本不足一半 | ⭐⭐⭐ |
| open source speech to text | 210 | 35 | $2.38 | 流量较大，Voxtral 是 2025 年最新开源 STT，Olares 承载场景清晰 | ⭐⭐ |
| elevenlabs scribe | 260 | 32 | $5.69 | Voxtral Small 精度持平 Scribe 但价格不足一半；可做 alternative 文章 | ⭐⭐ |
| open source speech recognition | 170 | 31 | $1.99 | Apache 2.0 + 本地部署，Olares Agent 语音输入前端 | ⭐⭐ |
| audio understanding model | 20 | 0 | $0.33 | Voxtral 独特能力——不只转写，可直接回答音频内容问题，Olares Agent 用例 | ⭐⭐ |
| local speech to text | 30 | 0 | $2.37 | 低竞争、有商业意图，CPC $2.37 证明有购买行为 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| voxtral | 390 | 61 | $0 | info | 主词候选 | 品牌主词，KD 61 偏高但流量由自身内容撑；品牌词通常可排，适合官方页+教程内容 |
| voxtral tts | 170 | 35 | $4.48 | info/comm | 主词候选 | TTS 产品线独立热点，CPC 高有商业意图；可写"Voxtral TTS 本地部署"独立文章 |
| voxtral 4b tts 2603 | 170 | 0 | $0.33 | comm | 次级 | 型号精确词，量高但意图已在主词覆盖范围内；KD=0 GEO 机会极强 |
| elevenlabs scribe | 260 | 32 | $5.69 | comm | 主词候选 | 闭源对标词，KD 32 可攻，商业意图强；"Voxtral vs ElevenLabs Scribe"或"ElevenLabs Scribe alternative"主词 |
| transcription model | 480 | 39 | $1.79 | info | 主词候选 | 类目词，流量大；Voxtral 是 2025 最新 SOTA，可做 listicle 类内容 |
| open source speech to text | 210 | 35 | $2.38 | info | 主词候选 | 需求明确的品类词，KD 35 可攻；Olares 可自托管 Voxtral 即核心叙事 |
| open source speech recognition | 170 | 31 | $1.99 | info | 主词候选 | 同上，KD 31 低竞争；Apache 2.0 + 本地部署是核心角度 |
| whisper api | 1,300 | 60 | $4.21 | info/comm | 次级 | 量大但 KD 60 难攻头部；作次级词放进"Whisper API 替代"文章中 |
| mistral voxtral | 90 | 42 | $3.91 | info/nav | 次级 | 品牌+型号组合，适合入门文 secondary；Olares vLLM 部署场景 |
| voxtral mini | 90 | 34 | $0 | info | 次级 | 边缘尺寸词，KD 34；适合"Voxtral Mini 消费级本地跑"的 H2 部分 |
| voxtral vs whisper | 20 | 0 | $0 | info | 次级/GEO | 对比词近零 KD；首选 GEO 抢发，嵌入 "Voxtral vs Whisper" 段落 |
| open source elevenlabs | 30 | 0 | $7.60 | info | GEO | KD=0 且 CPC $7.60 异常高，战略意图强；GEO 抢占"open source ElevenLabs"问题答案 |
| voxtral vllm | 20 | 0 | $0 | info | GEO | 引擎组合词，部署文档场景；Olares vLLM 一键部署 Voxtral 的入口词 |
| run voxtral locally | 10 | 0 | $0 | info | GEO | 完美契合 Olares 叙事；近零量是新模型正常态，AI Overview 抢占窗口 |
| self hosted speech to text | 20 | 0 | $0.33 | info | GEO | 隐私/离线场景，Olares 平台定位与此完全吻合 |
| local audio transcription | 20 | 0 | $3.77 | info | GEO | CPC $3.77 证明转化意图；Olares One 24GB GPU 运行 Voxtral Mini 的精准叙事词 |
| audio understanding model | 20 | 0 | $0.33 | info | GEO | Voxtral 差异化能力词（不只转写，可理解+问答）；GEO 前哨，AI Overview 待占 |
| voxtral realtime | 50–70 | 0 | $0 | info | 次级 | Realtime 产品线词；适合流式转写场景段落；KD=0 低竞争 |

---

## 核心洞见

1. **搜索心智刚建立，品牌词有初步量但 KD 偏高**：`voxtral` 390/月、KD 61——说明品牌词已被竞争内容占据一定位置，但绝对量尚小，适合通过官方内容 + 高质量教程建立权威。型号词（`voxtral mini`、`voxtral small`、`voxtral realtime`）KD 普遍为 0，大量词是 GEO 抢发理想目标。

2. **Voxtral Mini 可在 Olares One 本地跑，叙事成立**：Mini 3B（约 9.5 GB VRAM）运行于消费级 RTX 4060 Ti 16GB，Olares One 搭载 RTX 5090 Mobile 24GB，运行 Mini 有充足余量，可同时处理并发转写请求。Small 24B 需约 55 GB VRAM，Olares One 单卡不支持，需多卡或高端工作站。主推场景以 Mini 为核心。

3. **Apache 2.0 许可，商用自托管主推无障碍**：无地区限制、无商用禁令，可作为 Whisper API / ElevenLabs Scribe 的完全可自托管替代来主推——是 Olares 叙事最强卡点。

4. **对 Olares 最关键的 3 个词**：
   - `voxtral vllm`（20/月，KD 0）：vLLM 在 Olares Market，部署路径最短；
   - `open source elevenlabs`（30/月，KD 0，CPC $7.60）：高商业意图 + 零竞争，GEO 价值极高；
   - `self hosted speech to text`（20/月，KD 0）：与 Olares 平台定位完美契合的部署类词。

5. **GEO 抢发窗口**：`voxtral` 家族大量词处于 KD=0 近零量状态（`run voxtral locally`、`voxtral local`、`voxtral vram`、`audio understanding model`、`voxtral ollama`）——这是 2025 年发布的新模型典型窗口。现在发布结构化的"如何在 Olares/本地跑 Voxtral"内容，可快速占据 AI Overview 和 Perplexity 引用位，待搜索量上涨时已具备内容权重。

6. **闭源对标与攻击面**：
   - **OpenAI Whisper API**（6,600/月导航词，$0.006/min）：Voxtral Mini Transcribe 精度超越 Whisper Large-v3，价格不足一半，且可完全本地运行避免云端隐私风险；
   - **ElevenLabs Scribe**（260/月，KD 32，CPC $5.69）：Voxtral Small 精度持平，价格不足一半，是 alternative 内容最有价值的攻击词；
   - **AttackFace**：按分钟收费、额度限制、音频数据上传云端——这三点正是 Voxtral 本地自托管的核心卖点。

7. **与同类 family 关联**：同在 06-stt 分组下，`distil-whisper`（MIT, 英文快转）、`whisper`（MIT, 多语言）、`qwen3-asr`（Apache 2.0, 52 语言）均已有报告。Voxtral 差异化在于：**音频理解（不只转写，可直接回答音频内容的问题）** + Apache 2.0 + Mistral AI 背书；可与 Qwen3-ASR 形成"Apache 2.0 开源 STT 对决"内容簇，与 Whisper 形成"Whisper vs Voxtral 新旧迭代"内容角度。`voxtral tts`（170/月）是独立 TTS 产品线，与 TTS 类报告（如 Piper）也有关联。

---

*数据来源：SEMrush US（phrase_this、phrase_these、phrase_fullsearch、phrase_related、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
