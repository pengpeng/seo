# NeuTTS 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：neuphonic.com（Neuphonic），Apache 2.0（Air）/ NeuTTS Open License 1.0（Nano）

## 模型理解（前置）

NeuTTS 是 Neuphonic 出品的开源、端侧 TTS 语音语言模型系列，代表作 **NeuTTS Air**（约 0.5B，Apache 2.0）和 **NeuTTS Nano**（约 120M，NeuTTS OL）。两款模型均基于 LLM backbone（Air 基于 Qwen 0.5B）+ NeuCodec 神经音频编解码器，支持**仅需 3 秒参考音频的即时声音克隆**，无需 GPU、无需联网，可在手机、笔记本甚至树莓派上实时推理。Air 于 2025 年 10 月开源，GitHub 约 6,048 ★，已提供 GGUF 量化（Q4/Q8），直接走 llama.cpp 推理路径。核心对标是 **ElevenLabs 和 Play.ht** 等按用量计费的云端 TTS/声音克隆 API。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 端侧 TTS + 即时声音克隆语音语言模型（LLM backbone + 神经音频编解码器） |
| 许可证 | Air：Apache 2.0（商用友好，可完全自托管）；Nano：NeuTTS Open License 1.0（研究/有限商用免费，高营收商用须付费） |
| 主仓库 / 分发 | GitHub `neuphonic/neutts`（~6,048 ★，2025-10 创建）；HuggingFace `neuphonic/neutts-air`（79.7k 下载）；GGUF 量化版单独托管在 HF |
| 参数 / VRAM 可跑性 | Air：~360M active / ~552M 含 Embedding；Nano：~120M active / ~229M 含 Embedding。纯 CPU 推理，GGUF Q4/Q8，**无需 GPU**；Nano 在 Galaxy A25 5G（CPU）达 45 tokens/s，RTX 4090 达 19,268 tokens/s。Olares One 完全可跑（x86 CPU 足够） |
| 变体 / 型号 | NeuTTS-Air（英语）；NeuTTS-Nano（英语、西班牙语、法语、德语、乌尔都语、日语、韩语、中文、葡萄牙语） |
| 闭源对标 | ElevenLabs（按字符/分钟计费）、Play.ht（SaaS 配额）；开源生态内竞争：Kokoro、Coqui XTTS、Piper、F5-TTS |
| Olares Market | 未上架。无 Ollama 原生支持（Ollama 暂不支持 TTS 模型）；可通过 Python pip 包 `neutts` + llama-cpp-python 本地部署 |
| 来源 | [GitHub README](https://github.com/neuphonic/neutts)；[HuggingFace 模型卡](https://huggingface.co/neuphonic/neutts-air)；[MarkTechPost 报道 2025-10-02](https://www.marktechpost.com/2025/10/02/neuphonic-open-sources-neutts-air-a-748m-parameter-on-device-speech-language-model-with-instant-voice-cloning/) |

---

## 流量基线（Phase 1）

| 指标 | 数据 |
|------|------|
| 域名 | neuphonic.com |
| SEMrush Rank | 4,629,849 |
| 月自然流量（US） | 58 |
| 关键词数 | 19 |
| 流量估值 | $408/月 |

### 官网 TOP 关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | 流量 | URL |
|--------|------|------|----|------|-----|
| neuphonic | 1 | 70 | 37 | 56 | neuphonic.com/ |
| neuvoice | 8 | 50 | 16 | 1 | neuphonic.com/ |
| ophonic | 27 | 1,000 | 40 | 1 | neuphonic.com/ |
| neutts air | 17 | 390 | 13 | 0 | neuphonic.com/ |
| neutts-air | 21 | 260 | 20 | 0 | neuphonic.com/ |
| neutts | 19 | 140 | 22 | 0 | neuphonic.com/ |
| neutts | 25 | 140 | 22 | 0 | neuphonic.com/models/neutts-nano |
| neuttsair | 18 | 30 | 18 | 0 | neuphonic.com/ |
| neurotts | 21 | 40 | 18 | 0 | neuphonic.com/ |
| auphonic ai | 36 | 210 | 35 | 0 | neuphonic.com/ |
| phonic ai | 15 | 90 | 41 | 0 | neuphonic.com/ |
| livekit tts | 23 | 40 | 17 | 0 | docs.neuphonic.com/integrations/livekit |

> 注：流量极低，官网在核心词（neutts air 390 量）上排名 17，未能进 top 10，说明品牌 SEO 基本处于起步阶段。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| neutts air ⭐ | 320 | 13 | $0 | I |
| neutts-air ⭐ | 210 | 14 | $0 | I |
| neutts ⭐ | 140 | 22 | $2.43 | I |
| neuttsair ⭐ | 30 | 18 | $10.96 | I |
| neurotts ⭐ | 40 | 18 | $0 | I |
| neutts nano | 0 | — | — | — |

> 说明：Nano 尚无独立搜索量；brand 词量级在 140–320，属于新兴模型早期水平。

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| tts llama.cpp | 0 | — | — | — |
| gguf tts | 0 | — | — | — |
| neutts ollama | 0 | — | — | — |
| neutts python | 0 | — | — | — |

> 说明：NeuTTS 走 llama-cpp-python 路径，但对应组合词尚无 Semrush 收录量——属 GEO 抢发空白地带。Ollama 暂不原生支持 TTS 模型，无 `neutts ollama` 词。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| on device tts ⭐ | 20 | 0 | $0 | I |
| on-device tts ⭐ | 20 | 0 | $0 | I |
| on device text to speech ⭐ | 20 | 0 | $0.18 | I |
| self hosted tts ⭐ | 20 | 0 | $0 | I |
| offline tts ⭐ | 20 | 0 | $0 | I |
| offline voice cloning ⭐ | 20 | 0 | $0 | I |
| embedded tts ⭐ | 20 | 0 | $0 | I |
| raspberry pi tts ⭐ | 20 | 0 | $0 | I |
| local voice cloning ⭐ | 20 | 0 | $2.38 | I |
| run elevenlabs locally ⭐ | 20 | 0 | $0 | I |
| local tts model ⭐ | 10 | 0 | $0 | I |

> 说明：所有本地部署类词 KD 均为 0，月量 10–20——绝对量低但竞争为零，是 GEO / 技术文的理想切入点。

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| free voice cloning | 1,000 | 56 | $1.39 | I |
| voice cloning ai | 1,600 | 69 | $1.48 | I/C |
| voice cloning software | 390 | 63 | $1.91 | I |
| elevenlabs alternative ⭐ | 480 | 9 | $6.16 | I |
| open source tts ⭐ | 260 | 32 | $1.41 | I |
| free tts api ⭐ | 260 | 28 | $5.80 | I/C |
| open source voice cloning ⭐ | 140 | 35 | $2.23 | I |
| tts with voice cloning ⭐ | 20 | 0 | $0 | I |
| open source elevenlabs ⭐ | 30 | 0 | $7.60 | I |
| open source elevenlabs alternative ⭐ | 20 | 0 | $0 | I |
| elevenlabs alternative open source ⭐ | 20 | 0 | $0 | I |
| coqui tts alternative ⭐ | 20 | 0 | $0 | I |
| best tts model ⭐ | 70 | 10 | $4.55 | I |
| voice cloning model ⭐ | 10 | 0 | $2.90 | I |
| best voice cloning model ⭐ | 20 | 0 | $4.29 | I |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|-----|-------------|
| elevenlabs alternative ⭐⭐⭐ | 480 | 9 | $6.16 | KD 极低（9）量 480——"Run ElevenLabs-quality TTS locally on Olares"是完美攻击面；Air Apache 2.0 可无限制商用，Olares One 纯 CPU 可跑 |
| open source tts ⭐⭐⭐ | 260 | 32 | $1.41 | 类别主词；强调"本地运行、数据不出设备"，Olares One 硬件直接跑，无云依赖 |
| free tts api ⭐⭐ | 260 | 28 | $5.80 | 可自托管 Neuphonic API 服务器于 Olares，向内网应用提供 TTS；Apache 2.0 无配额 |
| on device tts ⭐⭐⭐ | 20 | 0 | $0 | GEO 前哨词；直接对应 Olares "本地 Agent 配音"场景，声音克隆 + 无联网 |
| self hosted tts ⭐⭐⭐ | 20 | 0 | $0 | 自托管叙事完美契合 Olares；Neuphonic On-Prem 方案 + Olares = 企业级隐私合规 |
| offline voice cloning ⭐⭐ | 20 | 0 | $0 | 数据不出本机；Personal Agent 个性化声音场景，Olares 上无网推理 |
| open source elevenlabs alternative ⭐⭐⭐ | 20 | 0 | $0 | GEO 空白词，CPC $0 无付费竞争；直接对标 ElevenLabs 商业产品——这是 Olares + NeuTTS Air 的核心叙事 |
| run elevenlabs locally ⭐⭐⭐ | 20 | 0 | $0 | 搜索意图即"摆脱 ElevenLabs SaaS"；Olares One 部署 NeuTTS Air 是字面答案 |
| embedded tts ⭐⭐ | 20 | 0 | $0 | 嵌入式/边缘 AI 应用场景；Olares 连接 IoT / 智能家居设备时的声音输出层 |
| raspberry pi tts ⭐⭐ | 20 | 0 | $0 | 树莓派即可跑，Olares One 远超树莓派；"更强性能 + 完整 OS"是升级叙事 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| elevenlabs alternative | 480 | 9 | $6.16 | I | 主词候选 | 量 480，KD 仅 9——TTS 领域最低竞争度高价值词；NeuTTS Air Apache 2.0 + 本地运行是正面回答，Olares 作为部署平台 |
| neutts air | 320 | 13 | $0 | I | 主词候选 | 品牌核心词，官网当前排名 17，提升空间大；应入 title/H1 |
| neutts-air | 210 | 14 | $0 | I | 主词候选 | 拼写变体，量大于 neutts，需并入内容覆盖 |
| open source tts | 260 | 32 | $1.41 | I | 主词候选 | 类别词，量 260，KD 32 可争；NeuTTS Air 在 open-source TTS 里的差异化是 Apache 2.0 + 声音克隆 + 无 GPU |
| free tts api | 260 | 28 | $5.80 | I/C | 主词候选 | 商业意图词，KD 28，量 260；Olares 自托管 Neuphonic API = 无限免费调用 |
| open source voice cloning | 140 | 35 | $2.23 | I | 次级 | 量 140，KD 35；可作对比文支撑词 |
| neutts | 140 | 22 | $2.43 | I | 次级 | 品牌根词，支撑词，辅助 neutts air |
| best tts model | 70 | 10 | $4.55 | I | 次级 | KD 10 极低，量 70；适合"best on-device TTS 2026"型测评文 |
| neuphonic | 70 | 37 | $7.24 | N | 次级 | 厂商品牌词，品牌直达流量，现已 rank #1 |
| on device tts | 20 | 0 | $0 | I | GEO | 量低但 KD=0；AI Overview / Perplexity 抢占位 |
| self hosted tts | 20 | 0 | $0 | I | GEO | 同上；Olares 自托管叙事前置词 |
| open source elevenlabs alternative | 20 | 0 | $0 | I | GEO | KD=0，CPC=0；近零竞争，语义最精准——Olares + NeuTTS Air 完美答案 |
| run elevenlabs locally | 20 | 0 | $0 | I | GEO | 搜索意图直接对齐 Olares 部署场景 |
| offline voice cloning | 20 | 0 | $0 | I | GEO | 数据隐私型用户的精准词；Olares Personal Agent 场景 |
| embedded tts | 20 | 0 | $0 | I | GEO | IoT / 边缘设备场景，Olares One 可充当中枢 |
| coqui tts alternative | 20 | 0 | $0 | I | GEO | Coqui 已停止维护，用户正在迁移；NeuTTS Air 是最佳继任者之一 |

---

## 核心洞见

1. **搜索心智建立程度**：NeuTTS Air 于 2025-10 开源，到 2026-07 品牌词（neutts / neutts air）已有 140–320 US 月量，比大多数新发布模型快。但官网 neuphonic.com 排名 17，流量约 58/月——搜索量被 HuggingFace（79.7k 下载）和 GitHub 截流，品牌官网 SEO 几乎为零。主战场依然是 HF/GitHub 第三方内容页。

2. **消费级 / Olares One 能否本地跑**：**完全可以**，且优势极强。Air 纯 CPU（llama-cpp-python + GGUF Q4/Q8），无 GPU 要求。Nano 在低端安卓手机（Galaxy A25）达 45 tokens/s，Olares One x86 CPU 性能远超手机，实时推理无障碍。是目前主流开源 TTS 模型中**对低配硬件最友好**的选项之一。

3. **许可证主推性**：NeuTTS Air（Apache 2.0）可作**主推卖点**——完全商用、可自托管、无使用配额、代码可修改，是对抗 ElevenLabs 按字符收费的最直接武器。NeuTTS Nano（NeuTTS OL）限制较多，高营收商用须联系 Neuphonic，不可作无条件主推，适合"研究 / 个人项目"场景的覆盖。

4. **对 Olares 最关键的 2-3 个词**：
   - `elevenlabs alternative`（480 量，KD 9）——最高价值机会词，Olares 部署 NeuTTS Air 是字面答案
   - `open source elevenlabs alternative` / `run elevenlabs locally`（GEO，KD=0）——意图最精准，AI Overview 抢占位
   - `self hosted tts` / `on device tts`（GEO，KD=0）——Olares 自托管叙事入口词

5. **GEO 抢发窗口**：`open source elevenlabs alternative`、`run elevenlabs locally`、`on device tts`、`self hosted tts`、`offline voice cloning`、`embedded tts` 均月量 0–20、KD=0，Semrush 无收录竞争——是 AI Overview / Perplexity 的空白地带。NeuTTS Air（Apache 2.0）语义高度契合，立即发 GEO 内容可低成本占位。

6. **闭源对标与攻击面**：
   - **ElevenLabs**：按字符/分钟计费（Creator $22/mo 起），存在月度配额，音频数据上云。NeuTTS Air 攻击面：免费（Apache 2.0）、离线、声音克隆 3 秒起（ElevenLabs 同等功能在 $99/mo 计划）。
   - **Play.ht**：API 调用计费、配额限制，无本地部署选项。同攻击逻辑。
   - **Coqui XTTS**：项目已停止维护（Coqui Inc. 2024 年停运），大量用户正在寻找替代——`coqui tts alternative`（20 量，KD 0）是 GEO 进入口。

7. **与同类 family 关联**：同属 `05-tts` 类的 Piper（1,300 量，KD 25）无声音克隆能力，F5-TTS（1,300 量，KD 50）声音克隆但更偏研究用，Kokoro（2,400 量，KD 64）商用最受欢迎但许可证严格（Apache 2.0 for inference only）。NeuTTS Air 在"声音克隆 + Apache 2.0 + 无 GPU"三交集里几乎无竞争对手，是 Olares Personal Agent 配音层的首选。

---

*数据来源：SEMrush US（phrase_this、phrase_these、phrase_fullsearch、phrase_related、phrase_kdi、domain_rank、resource_organic）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
