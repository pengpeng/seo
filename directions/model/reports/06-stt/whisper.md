# Whisper 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：openai/whisper（GitHub），MIT License
> **无独立官网**：Whisper 以 GitHub + HuggingFace 为主分发渠道，SEO 主战场在第三方内容/文档页。跳过 Phase 1 域名报告，从关键词层面起步。

---

## 模型理解（前置）

OpenAI Whisper 是一个基于 Transformer 的开源自动语音识别（ASR / STT）模型，在 >5M 小时弱标注音频上训练，支持 99 种语言的转录与跨语言翻译，零样本泛化能力强。2024 年 10 月发布的 `large-v3-turbo`（仅 4 层 decoder，809M 参数，~8x 实时速度）是当前生产首选。Whisper 是 Olares 上 Open Notebook 语音笔记、OpenClaw 本地会议转录的核心 STT 引擎——私有化部署场景与 Olares 主打的隐私 + Agent-Native OS 定位完全契合。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 多语言 ASR / STT 模型，零样本强泛化，支持本地私有化部署 |
| 许可证 | **MIT**（商用友好，可自托管，无地区限制，主推卖点成立） |
| 主仓库 / 分发 | [GitHub openai/whisper](https://github.com/openai/whisper)（104k ★）；HuggingFace `openai/whisper-*`；Ollama 不直接支持（Whisper 是 encoder-decoder，非 decoder-only LLM） |
| 参数 / VRAM 可跑性 | tiny(39M/~1GB)→base(74M/~1GB)→small(244M/~2GB)→medium(769M/~5GB)→large-v3(1.55B/~10GB)→turbo(809M/~6GB)；**消费级 6GB 跑 turbo，24GB Olares One 跑 large-v3 满血** |
| 变体 / 型号 | large-v3（精度最高）、large-v3-turbo/turbo（速度优先）、distil-large-v3（英文蒸馏，756M/6.3x 实时）、tiny/base/small/medium（轻量级） |
| 闭源对标 | **Deepgram**（✅ 已报告）、**Fireflies.ai**（✅ 已报告）、OpenAI Whisper API（`/v1/audio/transcriptions`，Whisper 的云端托管版）、AssemblyAI、Otter.ai |
| 主要运行时（Olares 相关） | **faster-whisper**（CTranslate2，CUDA 最快）、**whisper.cpp**（GGUF/C++，CPU/Metal/CUDA 均支持，Docker 镜像已有）、**WhisperX**（faster-whisper + 说话人分离）；以上均可在 Olares Docker 容器中运行 |
| Olares Market | 未直接上架 Whisper 模型；Ollama 不支持 Whisper（引擎限制）；**whisper.cpp** 和 **faster-whisper** 均支持 Docker 部署，可通过 Olares 自定义应用方式承载；Open Notebook / OpenClaw 内置 Whisper 后端 |
| 来源 | [GitHub openai/whisper](https://github.com/openai/whisper)；[HF whisper-large-v3](https://huggingface.co/openai/whisper-large-v3)；[HF whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)；[distil-whisper GitHub](https://github.com/huggingface/distil-whisper) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| whisper transcription | 1,900 | 82 | $2.70 | info |
| whisper speech to text | 480 | 67 | $1.63 | info |
| whisper-large-v3 | 1,000 | 57 | $3.05 | info |
| whisper large v3 | 390 | 46 | $2.58 | info |
| whisper large-v3 | 590 | 35 | $2.58 | info |
| whisper asr | 320 | 47 | $2.38 | info |
| whisper-large-v3-turbo | 880 | 32 | $4.07 | info |
| whisper large v3 turbo | 260 | 31 | $3.19 | info |
| whisper turbo | 170 | 44 | $2.32 | info |
| whisper stt | 140 | 58 | $2.33 | info |
| whisper tiny | 110 | 40 | $1.54 | info |
| distil whisper ⭐ | 90 | 31 | $2.50 | info |
| distil-whisper ⭐ | 40 | 31 | $0 | info |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| faster-whisper ⭐ | 3,600 | 29 | $2.80 | info |
| whisperx ⭐ | 2,400 | 28 | $2.82 | info/nav |
| whisper.cpp | 2,900 | 41 | $2.80 | info |
| faster whisper ⭐ | 1,600 | 33 | $2.80 | info |
| whisper cpp | 1,600 | 34 | $2.29 | info |
| whisper-faster | 880 | 33 | $4.29 | info |
| whisper x ⭐ | 720 | 13 | $2.51 | info/trans |
| whisper desktop | 390 | 40 | $1.85 | info |
| whisper docker ⭐ | 110 | 28 | $0 | info |
| whisper ollama ⭐ | 20 | 0 | $0 | info |
| whisper vllm ⭐ | 20 | 0 | $0 | info |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| run whisper locally ⭐ | 110 | 33 | $6.32 | info |
| whisper local ⭐ | 140 | 42 | $2.08 | info |
| whisper python | 140 | 46 | $5.60 | info |
| whisper install | 140 | 63 | $3.12 | info |
| faster-whisper raspberry pi ⭐ | 30 | 0 | $0 | info |
| whisper self hosted ⭐ | 30 | 20 | $1.95 | info |
| whisper gpu ⭐ | 20 | 0 | $0 | info |
| whisper gguf ⭐ | 20 | 0 | $0 | info |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| free speech recognition software | 260 | 60 | $2.84 | info |
| open source speech recognition ⭐ | 170 | 31 | $1.99 | info |
| whisper alternative ⭐ | 170 | 10 | $1.86 | info |
| whisper alternatives ⭐ | 90 | 15 | $1.86 | info |
| openai whisper alternatives ⭐ | 30 | 17 | $2.25 | info |
| whisper ai alternatives ⭐ | 30 | 4 | $3.70 | info |
| whisper open source alternative ⭐ | 30 | 0 | $0 | info |
| whisper vs deepgram ⭐ | 20 | 0 | $0 | info |
| open source transcription ⭐ | 20 | 0 | $2.30 | info |
| local transcription ⭐ | 20 | 0 | $3.50 | info |
| offline transcription ⭐ | 20 | 0 | $2.61 | info |
| self hosted transcription ⭐ | 20 | 0 | $0 | info |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| faster-whisper | 3,600 | 29 | $2.80 | Olares 上 faster-whisper Docker 容器：NVIDIA RTX 5090 Mobile CUDA 加速，转录速度 >70x 实时；一键部署即可为 Open Notebook / OpenClaw 提供 STT 后端 | ⭐⭐⭐ |
| whisperx | 2,400 | 28 | $2.82 | WhisperX = faster-whisper + 说话人分离（diarization），Olares One 本地会议场景的完整 STT 管道，数据不出设备 | ⭐⭐⭐ |
| whisper alternative | 170 | 10 | $1.86 | Deepgram / Fireflies.ai 的本地开源平替；Olares 主打"自己的转录不用交给 SaaS" | ⭐⭐⭐ |
| run whisper locally | 110 | 33 | $6.32 | $6.32 CPC 最高，商业意图强；Olares One 24GB VRAM 跑 large-v3 满血，隐私保障，推荐用量最大的部署词 | ⭐⭐⭐ |
| whisper docker | 110 | 28 | $0 | whisper.cpp / faster-whisper 均有官方 Docker 镜像，直接在 Olares 自定义应用里 compose 即可 | ⭐⭐⭐ |
| open source speech recognition | 170 | 31 | $1.99 | Whisper 是当前开源 STT 事实标准；Olares 在"open source alternative to Deepgram"叙事里用它做落地凭证 | ⭐⭐ |
| whisper self hosted | 30 | 20 | $1.95 | 直接呼应 Olares 自托管定位，KD 极低，适合 GEO / 直答块 | ⭐⭐⭐ |
| whisper vs deepgram | 20 | 0 | $0 | Deepgram 已有报告，两者对比直接链接至 Olares 本地 vs 云 SaaS 攻击点；KD=0 抢发窗口 | ⭐⭐⭐ |
| local transcription | 20 | 0 | $3.50 | CPC 最高之一，商业意图强，搜量偏低但意图纯净；作 GEO 前哨 | ⭐⭐ |
| offline transcription | 20 | 0 | $2.61 | 隐私场景核心词，会议/法律/医疗不可联网时的首选 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| faster-whisper | 3,600 | 29 | $2.80 | info | **主词候选** | 高量低竞争 ⭐，Olares One CUDA 加速场景最直接的入口词；同族词（faster-whisper docker/raspberry pi）合计量大 |
| whisperx | 2,400 | 28 | $2.82 | info/nav | **主词候选** | KD 28 极具性价比，会议说话人分离场景；Olares 会议转录完整管道的核心词 |
| whisper.cpp | 2,900 | 41 | $2.80 | info | **主词候选** | 量大、C++ 轻量运行时，whisper.cpp Docker 在 Olares 上开箱即用；KD 41 可争 |
| openai whisper | 6,600 | 97 | $2.56 | nav | **次级** | 品牌导航词，KD 97 排不进；仅在文章元数据/intro 里提及，靠长尾词覆盖 |
| whisper transcription | 1,900 | 82 | $2.70 | info | **次级** | 高量但 KD 82 竞争激烈；作为次级词支撑上方主词候选 |
| whisper alternative | 170 | 10 | $1.86 | info | **主词候选** | KD 10 极低，虽量小但意图纯净（商业替代型）；同族合计（alternatives/openai whisper alternatives）~320，战略价值高 |
| whisper x | 720 | 13 | $2.51 | info | **主词候选** | KD 仅 13，是"whisperx"的高频变体，同一内容页可同时覆盖两词 |
| whisper-large-v3-turbo | 880 | 32 | $4.07 | info | **次级** | 型号词，CPC 高（$4.07）→高商业价值，作次级并入 faster-whisper 或 run locally 类文章 |
| run whisper locally | 110 | 33 | $6.32 | info | **主词候选** | CPC $6.32 全表最高，部署意图极纯；量偏低但意图 + Olares 契合均最强 |
| whisper docker | 110 | 28 | $0 | info | **次级** | 低 KD 部署词，与 run whisper locally 同一文章覆盖 |
| open source speech recognition | 170 | 31 | $1.99 | info | **次级** | 上接 Deepgram alternative / Fireflies alternative 的整体叙事 |
| whisper self hosted | 30 | 20 | $1.95 | info | **次级** | KD 20 低竞争，自托管 + Olares 定位直接呼应；作次级或 GEO |
| whisper vs deepgram | 20 | 0 | $0 | info | **GEO** | KD=0 零竞争，两者对比直接对接 Deepgram 报告的攻击词；适合 FAQ 直答块 |
| local transcription | 20 | 0 | $3.50 | info | **GEO** | CPC $3.50 高，意图极纯；近零量作 GEO，等流量成熟后升主词候选 |
| offline transcription | 20 | 0 | $2.61 | info | **GEO** | 隐私/合规转录场景前哨词，适合 AI Overview 直答 |
| whisper ollama | 20 | 0 | $0 | info | **GEO** | 量接近零，但用户常误以为 Ollama 支持 Whisper；抢占"whisper ollama 可以吗"类 FAQ |
| whisper ai alternatives | 30 | 4 | $3.70 | info | **GEO** | KD=4 几乎无竞争，意图是找 AI 转录替代方案，进 FAQ 或直答块 |
| self hosted transcription | 20 | 0 | $0 | info | **GEO** | 对 Olares 自托管定位极度对口的零竞争词 |

---

## 核心洞见

### 1. 搜索心智建立程度
Whisper 的搜索心智已相对成熟：`openai whisper`(6.6k) + `whisper transcription`(1.9k) + `whisper speech to text`(480) 说明直接品牌/功能词有足够体量。但**主战场已转移到运行时层**：`faster-whisper`(3.6k)、`whisper.cpp`(2.9k)、`whisperx`(2.4k) 均超过"openai whisper"相关功能词，且 KD 远低（29/41/28 vs 82/97）。搜索行为已从"Whisper 是什么"转为"如何跑更快 / 怎么部署"——内容机会集中在运行时、部署方法、硬件指导。

**关键歧义**：`whisper`(49,500 vol) 被 Whisper 社交 app 严重稀释（KD 86，混杂 nav 意图），`whisper ai`(9,900 vol) 同样混杂了两个产品，不能作主词候选。内容必须用`openai whisper`或`whisper transcription`这类精确词消歧。

### 2. 消费级 GPU / Olares One 能否本地跑
**完全可以，且优势明显**：
- `turbo` 只需 ~6GB VRAM，消费级 RTX 4060 即可 >8x 实时
- `large-v3` 需 ~10GB VRAM，Olares One 的 RTX 5090 Mobile 24GB 跑满血 large-v3 + faster-whisper 可达 >70x 实时
- whisper.cpp 额外支持 GGUF 量化 + Vulkan + AMD ROCm，覆盖 Olares 的非 NVIDIA GPU 场景
- **叙事成立**：Olares One 对 Deepgram/Fireflies 的核心攻击点是"一次性硬件投入 = 无限量转录，无 API 费用，数据不出本机"

### 3. 许可证商用友好性
**MIT 许可，商用完全友好**，可作主推卖点：自托管、二次分发、产品内嵌均无限制。与 Deepgram（按分钟计费）形成直接对比——"永远免费"叙事成立。

### 4. 对 Olares 最关键的 3 个词
1. **`faster-whisper`**（3,600 vol / KD 29）：Olares 上 CUDA 加速转录的直接入口，Open Notebook / OpenClaw 的实际后端运行时；教程类内容即可覆盖
2. **`run whisper locally`**（110 vol / KD 33 / CPC $6.32）：意图最纯、转化最高的部署词，直接承接"Stop paying Deepgram"叙事
3. **`whisper alternative`**（170 vol / KD 10）：对标 Deepgram/Fireflies 的"开源平替"进攻词，KD 极低，与已有报告交叉引用价值高

### 5. GEO 抢发窗口
以下词量近零但语义精准，适合 AI Overview / Perplexity 直答位：
- `whisper vs deepgram`（KD=0）：Deepgram 已有报告，两报告联动可以打透对比场景
- `local transcription`、`offline transcription`、`self hosted transcription`（均 KD=0）：三词叠加构成隐私转录的语义簇
- `whisper ollama`（KD=0）：大量用户不清楚 Ollama 不支持 Whisper，FAQ 直答可截流
- `whisper ai alternatives`（KD=4 / CPC $3.70）：近零竞争的商业意图词

### 6. 闭源对标与攻击面
- **Deepgram**（✅ 已有报告）：按分钟 API 计费，Nova-3 $0.0059/min；攻击点 = 高频转录场景成本、隐私（音频上云）、用量限制
- **Fireflies.ai**（✅ 已有报告）：SaaS 会议转录订阅制；攻击点 = 月费 + 录音存 Fireflies 云端
- **OpenAI Whisper API**（`/v1/audio/transcriptions`）：$0.006/min 云端版；攻击点 = 数据发出设备，无法离线
- **AssemblyAI / Otter.ai**：类似 SaaS 收费模式
- **统一攻击面**：API 费用（量大时成本可观）+ 云端隐私 + 用量上限；Olares 本地 Whisper = 一次性部署，数据不出机，无限量

### 7. 与 model/models.md 同类 family 的关联
- 同章 06-stt（本报告），后续可在同章增补其他 STT 开源模型（Wav2Vec2、NeMo、Kaldi/Vosk、Parakeet）作横向对比
- `whisper vs deepgram`（commerce 报告）、`whisper vs fireflies`（commerce 报告）可形成跨分类内容矩阵
- 与 [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 06-stt 章节对应 family 记录（Whisper）状态更新为 ✅

---

*数据来源：SEMrush US（phrase_this、phrase_these、phrase_fullsearch、phrase_related）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
