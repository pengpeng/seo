# dig-12 · 语音赛道再拆（4 子类）+ 语音输入法 · 发现蒸馏笔记

**AS_OF=2026-07-04** · 只做发现+财务，不做最终分类。门槛：ARR>$50M｜估值>$200M｜融资>$20M｜大厂旗舰。

## Sources（节选）
官方博客(ElevenLabs/Bland/Observe) / TechCrunch/Forbes/Bloomberg / PRNewswire / CBInsights / Tracxn / SEC-IR 等。

## Products

### 1. TTS / 语音生成 / 语音克隆
| 名称 | 公司 | 域名 | 财务 | 命中 |
|------|------|------|------|------|
| ElevenLabs | ElevenLabs | elevenlabs.io | ARR >$500M；估值 $11B；融资 $781M | 全中 |
| Cartesia | Cartesia | cartesia.ai | 融资 ~$191M | 融资✓ |
| Hume AI | Hume AI | hume.ai | 融资 $74M；估值 $219M（2026-01 Google 挖走团队） | 融资✓估值✓ |
| Speechmatics | Speechmatics | speechmatics.com | 融资 $90.6M | 融资✓ |
| Deepgram | Deepgram | deepgram.com | 估值 $1.3B；融资 >$215M | 估值✓融资✓ |
| AssemblyAI | AssemblyAI | assemblyai.com | 估值 $300M；融资 $158M | 估值✓融资✓ |
| Play.HT/PlayAI | Meta | play.ht(已关停) | Meta 收购(2025-07) | 大厂旗舰 |
| Resemble AI | Resemble | resemble.ai | 融资 $25M | 融资✓(临界) |
| Amazon Polly / Google TTS / Azure Speech | 大厂 | — | 大厂旗舰 | 大厂旗舰 |
| Murf AI | Murf | murf.ai | 融资 $11.5M | **未达标** |

### 2. 会议转录 / 会议助手
| 名称 | 公司 | 域名 | 财务 | 命中 |
|------|------|------|------|------|
| Otter.ai | Otter | otter.ai | ARR >$100M；融资 ~$70M | ARR✓融资✓ |
| Fireflies.ai | Fireflies | fireflies.ai | 估值 >$1B；融资 ~$19–20M | 估值✓ |
| Granola | Granola | granola.ai | 估值 $1.5B；融资 $192M | 估值✓融资✓ |
| Gong | Gong | gong.io | ARR >$500M；估值 ~$7.2B | ARR✓估值✓ |
| Read AI | Read AI | read.ai | 估值 $450M；融资 $81M | 估值✓融资✓ |
| Fathom | Fathom | fathom.video | 融资 ~$22M | 融资✓(临界) |
| MS Copilot in Teams / Google Meet / Zoom AI Companion | 大厂 | — | 大厂旗舰 | 大厂旗舰 |

### 3. 语音输入法 / 听写（新增，重点）
| 名称 | 公司 | 域名 | 财务 | 命中 |
|------|------|------|------|------|
| **Wispr Flow**（=「Flow」） | Wispr | wisprflow.ai | 融资 $81M；估值 $700M；传闻 $260M 轮 @ ~$2B[u] | 融资✓估值✓ |
| Apple Dictation | Apple | apple.com | OS 级端侧听写 | 大厂旗舰 |
| Gboard Rambler | Google | google.com/gboard | Gemini 驱动键盘听写(2026 夏) | 大厂旗舰 |
| Windows Speech / Copilot dictation | Microsoft | microsoft.com | 系统级语音输入 | 大厂旗舰 |
| **未达标长尾**：Typeless、Aqua Voice、Willow、Superwhisper、Monologue、TalkTastic、Laxis、Voibe、VoiceInk | — | — | 均 <$20M 或零融资 | 未达标 |

> 结论：独立 VC 赛道几乎被 Wispr Flow 一家垄断；最大威胁来自 Apple/Google 免费内置。

### 4. 语音 Agent / Voicebot（企业电话/客服）
| 名称 | 公司 | 域名 | 财务 | 命中 |
|------|------|------|------|------|
| Vapi | Vapi | vapi.ai | 估值 ~$500M；融资 $72M | 估值✓融资✓ |
| PolyAI | PolyAI | poly.ai | 估值 $750M；融资 ~$204M | 估值✓融资✓ |
| Bland AI | Bland | bland.ai | 融资 >$100M | 融资✓ |
| Parloa | Parloa | parloa.com | 估值 $3B；融资 >$560M | 估值✓融资✓ |
| Observe.AI | Observe.AI | observe.ai | 融资 $214M | 融资✓ |
| Uniphore | Uniphore | uniphore.com | 估值 $2.5B；Series F $260M | 估值✓融资✓ |
| Retell AI | Retell | retellai.com | 融资 $5.1M；Sacra 估 ARR ~$60M[u] | ARR[u] |
| Sierra | Sierra | sierra.ai | 估值 ~$15B；ARR ~$150M；融资 ~$950M | 全中 |
| Decagon | Decagon | decagon.ai | 估值 $4.5B；融资 ~$481M | 估值✓融资✓ |
| SoundHound AI(SOUN) | SoundHound | soundhound.com | FY2025 收入 $169M | 上市规模 |
| Amazon Connect / Google CCAI / Nuance(MS) | 大厂 | — | 大厂旗舰 | 大厂旗舰 |

## 平替（Olares 侧）
- TTS/克隆：**Kokoro / Fish Speech / CosyVoice**
- STT/听写/会议：**Whisper / Speaches**（+ Open Notebook 会议笔记）
- Voicebot：无直接平替（可自建 Whisper+Kokoro+Dify 语音 pipeline）

## Gaps
- Murf/Play.HT 未达或被收购；听写长尾（Superwhisper 自报 7 位数收入等）需按增速而非财务门槛跟踪。
- 命名污染：Typeless 有同名 messaging API 公司($26M) 需排除；Aqua 融资口径分歧。
- 待补：中国听写（讯飞/百度/搜狗语音输入，大厂旗舰）。
- 子类边界：Deepgram/AssemblyAI/Speechmatics 可独立成「Speech API」；Sierra/Decagon 全渠道 Agent 非纯 voicebot（与通用/CX Agent 重叠）。
