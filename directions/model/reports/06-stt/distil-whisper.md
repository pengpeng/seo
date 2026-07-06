# Distil-Whisper 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：huggingface/distil-whisper（GitHub），MIT License
> **无独立官网**：Distil-Whisper 以 HuggingFace + GitHub 为主分发渠道，SEO 主战场在第三方内容/文档页。跳过 Phase 1 域名报告，从关键词层面起步。

---

## 模型理解（前置）

Distil-Whisper 是 Hugging Face 出品的 Whisper 蒸馏版——以 Whisper Large-v3 为教师模型，对英文语音任务进行学生-教师蒸馏训练，采用交叉熵 + KL 散度联合损失。旗舰型号 `distil-large-v3.5`（756M 参数）**比 Whisper Large-v2 快 6x，词错率仅增加 1%**，是面向实时转录场景（会议记录、语音命令、字幕生成）的首选部署型号。MIT 许可，商用友好，可在 faster-whisper 引擎下运行，Olares One 的 RTX 5090 Mobile 跑满血 distil-large-v3.5 可达 >300x 实时速度。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Whisper Large-v3 的英文蒸馏版，6x 提速、1% WER 损失，专为实时英文转录优化 |
| 许可证 | **MIT**（商用友好，可自托管、二次分发，主推卖点成立） |
| 主仓库 / 分发 | [GitHub huggingface/distil-whisper](https://github.com/huggingface/distil-whisper)（4.1k ★）；HuggingFace `distil-whisper/distil-large-v3.5`、`distil-whisper/distil-large-v3`、`distil-whisper/distil-medium.en`；支持 faster-whisper 引擎加载 |
| 参数 / VRAM 可跑性 | distil-large-v3.5（756M）≈ 4-6GB VRAM；distil-medium.en（394M）≈ 2-3GB VRAM；**消费级 RTX 4060（8GB）跑满血型号 >100x 实时**；Olares One 24GB RTX 5090 Mobile 可达 >300x 实时，适合并发多路转录 |
| 变体 / 型号 | distil-large-v3.5（旗舰英文）、distil-large-v3（前代英文）、distil-medium.en（轻量英文）；均为**英文专用**，多语言需回用父模型 Whisper |
| 闭源对标 | **OpenAI Whisper API**（`/v1/audio/transcriptions`，$0.006/min）、**Deepgram**（✅ 已报告）、**AssemblyAI**；Groq 也托管 distil-whisper 作为推理加速端点 |
| 主要运行时（Olares 相关） | **faster-whisper**（CTranslate2，GPU/CPU 均支持 distil-whisper 权重）；whisper.cpp 暂不原生支持 distil-whisper 权重格式；WhisperX 支持（底层用 faster-whisper） |
| Olares Market | 未直接上架 Distil-Whisper；Ollama 不支持 Whisper 系列（引擎限制）；可通过 faster-whisper Docker 容器在 Olares 自定义应用中部署；Open Notebook / OpenClaw 后端可换接 faster-whisper+distil-large-v3.5 |
| 来源 | [GitHub huggingface/distil-whisper](https://github.com/huggingface/distil-whisper)；[HF distil-large-v3.5](https://huggingface.co/distil-whisper/distil-large-v3.5)；[Distil-Whisper 论文](https://arxiv.org/abs/2311.00430) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| whisper large v3 | 390 | 46 | $2.58 | info |
| distil whisper ⭐ | 90 | 31 | $2.50 | info |
| distil-whisper ⭐ | 40 | 31 | $0 | info |
| distil whisper large v3 ⭐ | 20 | 0 | $0 | info |
| distil whisper v3 ⭐ | 20 | 0 | $0 | info |
| distil whisper groq ⭐ | 20 | 0 | $0 | info |
| distilled whisper ⭐ | 20 | 0 | $0 | info |
| whisper distillation ⭐ | 20 | 0 | $0 | info |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| faster-whisper ⭐ | 3,600 | 29 | $2.80 | info |
| whisperx ⭐ | 2,400 | 28 | $2.82 | info/nav |
| faster-whisper-xxl | 2,400 | 41 | $2.16 | info |
| faster whisper ⭐ | 1,600 | 33 | $2.80 | info |
| whisper ollama ⭐ | 20 | 0 | $0 | info |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| fast whisper | 590 | 50 | $2.80 | info |
| whisper local ⭐ | 140 | 42 | $2.08 | info |
| run whisper locally ⭐ | 110 | 33 | $6.32 | info |
| offline speech recognition ⭐ | 30 | 26 | $1.57 | info |
| local transcription ⭐ | 20 | 0 | $3.50 | info |
| local stt ⭐ | 20 | 0 | $0 | info |
| speech to text self hosted ⭐ | 20 | 0 | $0 | info |
| self hosted speech to text ⭐ | 20 | 0 | $0 | info |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| open source speech to text ⭐ | 210 | 35 | $2.38 | info |
| whisper alternative ⭐ | 170 | 10 | $1.86 | info |
| real time speech to text | 210 | 72 | $8.42 | info |
| faster whisper vs whisper ⭐ | 20 | 0 | $0 | info |
| assemblyai alternative ⭐ | 20 | 0 | $0 | info |
| open source transcription ⭐ | 20 | 0 | $2.30 | info |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| faster-whisper | 3,600 | 29 | $2.80 | Distil-Whisper 主要通过 faster-whisper 引擎运行；Olares One RTX 5090 Mobile 24GB 跑 distil-large-v3.5 可达 >300x 实时，Open Notebook / OpenClaw 语音转录后端最优解 | ⭐⭐⭐ |
| run whisper locally | 110 | 33 | $6.32 | CPC $6.32 全表最高，部署意图最纯；Olares 主打"数据不出本机 + 零 API 费"，distil-large-v3.5 仅需 4-6GB VRAM，门槛比 Whisper Large-v3 低一半 | ⭐⭐⭐ |
| whisper alternative | 170 | 10 | $1.86 | KD 10 极低；distil-whisper 是"自托管替代 OpenAI Whisper API / Deepgram"最强牌——速度更快、成本更低、数据不出设备 | ⭐⭐⭐ |
| whisperx | 2,400 | 28 | $2.82 | WhisperX 底层用 faster-whisper，可换接 distil-large-v3.5；Olares 会议转录（说话人分离 + 字幕 + 时间轴）完整 pipeline，无需订阅 Otter.ai / Fireflies | ⭐⭐⭐ |
| offline speech recognition | 30 | 26 | $1.57 | 隐私敏感场景（法律/医疗/企业）离线转录首选；distil-whisper MIT 授权 + Olares 数据本地化叙事完全契合 | ⭐⭐⭐ |
| open source speech to text | 210 | 35 | $2.38 | distil-whisper 是当前英文开源 STT 速度性价比最高方案；Olares 可落"从 Deepgram/AssemblyAI 切换到本地开源 STT"的内容 | ⭐⭐ |
| real time speech to text | 210 | 72 | $8.42 | CPC $8.42 全表最高，意图极纯且商业价值极高；distil-whisper 6x 速度加速正好打 real-time 场景；KD 72 需配主词候选写精品内容 | ⭐⭐ |
| local transcription | 20 | 0 | $3.50 | GEO 前哨，意图纯净；适合"local transcription with distil-whisper on Olares"FAQ 直答块 | ⭐⭐ |
| speech to text self hosted | 20 | 0 | $0 | 零竞争，Olares 自托管定位直接呼应；作 GEO / 直答块覆盖 | ⭐⭐ |
| assemblyai alternative | 20 | 0 | $0 | GEO 抢发：distil-whisper = AssemblyAI 的开源本地平替，KD=0 零竞争，Olares 上部署路径清晰 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| faster-whisper | 3,600 | 29 | $2.80 | info | **主词候选** | 高量低竞争 ⭐；distil-whisper 的主要运行时，Olares CUDA 加速场景直接入口；同族词（faster whisper/faster-whisper-xxl）合计量 >7,600 |
| whisperx | 2,400 | 28 | $2.82 | info/nav | **主词候选** | KD 28，量大；WhisperX 底层支持 distil-large-v3.5，Olares 会议转录完整 pipeline 核心词 |
| whisper alternative | 170 | 10 | $1.86 | info | **主词候选** | KD 10 极低，商业替代意图纯净；distil-whisper 是对 OpenAI Whisper API / Deepgram 最有力的开源平替，战略价值高 |
| open source speech to text | 210 | 35 | $2.38 | info | **主词候选** | 英文开源 STT 头部词；量中等，distil-whisper 速度优势撑起内容 |
| run whisper locally | 110 | 33 | $6.32 | info | **主词候选** | CPC $6.32 全表最高，部署意图极纯；distil-large-v3.5 VRAM 门槛比 large-v3 低 40%，更适合"just run locally"叙事 |
| real time speech to text | 210 | 72 | $8.42 | info | **次级** | CPC 最高但 KD 72 竞争激烈；作次级支撑 faster-whisper 或 whisper alternative 类文章，强调 distil-whisper 6x 加速 |
| faster whisper | 1,600 | 33 | $2.80 | info | **次级** | `faster-whisper` 的拼写变体，同一内容页可覆盖；与主词候选 `faster-whisper` 合并处理 |
| distil whisper | 90 | 31 | $2.50 | info | **次级** | 品牌心智词，量偏低；作 intro/标题副词支撑 faster-whisper 类文章，不宜单独作文 |
| whisper local | 140 | 42 | $2.08 | info | **次级** | 部署词，与 `run whisper locally` 同一文章覆盖 |
| offline speech recognition | 30 | 26 | $1.57 | info | **次级** | ⭐ KD 低，隐私/离线场景；与 `whisper alternative` 或 `self hosted transcription` 文章并入 |
| faster whisper vs whisper | 20 | 0 | $0 | info | **GEO** | KD=0 零竞争；distil-whisper 对比原版 Whisper 的性能对比 FAQ，直答"6x 快" |
| assemblyai alternative | 20 | 0 | $0 | info | **GEO** | KD=0；distil-whisper + Olares 是 AssemblyAI 的本地开源平替，适合 FAQ / AI Overview 直答 |
| local transcription | 20 | 0 | $3.50 | info | **GEO** | CPC $3.50 高，意图纯净；近零量作 GEO，等流量成熟升主词候选 |
| speech to text self hosted | 20 | 0 | $0 | info | **GEO** | 对 Olares 自托管定位极度对口的零竞争词；作 FAQ 块 |
| distil whisper groq | 20 | 0 | $0 | info | **GEO** | Groq 托管 distil-whisper 为推理加速端点，此词说明用户正在探索不同部署路径；可在文章里对比 Groq API vs Olares 本地 |
| whisper ollama | 20 | 0 | $0 | info | **GEO** | 大量用户误以为 Ollama 支持 Whisper 系列；FAQ "distil-whisper 能用 Ollama 跑吗"抢占直答位 |

---

## 核心洞见

### 1. 搜索心智建立程度

Distil-Whisper 的品牌词搜索量极低（`distil whisper` 仅 90/月，`distil-whisper` 40/月），搜索心智基本**未独立建立**——用户更多从"faster-whisper"（3,600/月）、"whisperx"（2,400/月）等运行时/工具名进入。相比 Whisper 主品牌，distil-whisper 更像是一个"技术参数选项"而非独立 brand，知道它的用户多是已经在折腾 faster-whisper 的开发者。

内容策略应以"faster-whisper + distil-large-v3.5"作叙事主轴，而非主推 "distil whisper" 品牌词——后者量太低。

### 2. 消费级 GPU / Olares One 能否本地跑

**完全可以，且 distil-whisper 比父模型门槛更低**：
- `distil-large-v3.5`（756M）≈ 4-6GB VRAM，消费级 RTX 4060（8GB）即可以 >100x 实时速度运行
- Olares One 的 RTX 5090 Mobile 24GB 可并发多路实时转录（会议 + 语音命令同时跑）
- 通过 faster-whisper 引擎，AMD ROCm 路径亦可在 Olares 上调度（1.12.4+）
- **叙事关键点**：distil-whisper 将"需要 10GB VRAM 跑 large-v3"降低到"4-6GB 即可"，让更多设备进入本地实时 STT 的行列

### 3. 许可证商用友好性

**MIT 许可，与 Whisper 父模型一致**，商用完全友好，可作主推卖点。相比 OpenAI Whisper API 的 $0.006/min 计费，Distil-Whisper + Olares 一次部署、无限量转录、数据不出机的叙事成立。

### 4. 对 Olares 最关键的 3 个词

1. **`faster-whisper`**（3,600/月 / KD 29）：Distil-Whisper 在 Olares 上的实际运行时，也是这整个 STT 加速生态的流量入口；部署教程直接可做
2. **`whisper alternative`**（170/月 / KD 10）：KD 极低、意图最纯；distil-whisper 是"告别 Deepgram / OpenAI Whisper API 云端收费"最有力的本地开源替代，Olares 在此叙事里有天然主场
3. **`run whisper locally`**（110/月 / KD 33 / CPC $6.32）：CPC 全表最高，意图最纯的部署词；distil-large-v3.5 低 VRAM 需求让"run locally"更实惠

### 5. GEO 抢发窗口

以下词量近零但语义精准，适合 AI Overview / Perplexity 直答位：
- `faster whisper vs whisper`（KD=0）：distil-whisper 对比原版 Whisper 的"6x 快但精度几乎相同"是精准 FAQ，直答块立等可抢
- `assemblyai alternative`（KD=0）：distil-whisper + Olares = AssemblyAI 的开源本地平替，零竞争直答位
- `speech to text self hosted`（KD=0）：Olares 自托管定位的语义精确触达词
- `distil whisper groq`（KD=0）：Groq vs Olares 本地的对比，用户在这里明确搜索不同部署路径
- `whisper ollama`（KD=0）：澄清"Ollama 不支持 Whisper 系列"的 FAQ 可以截流大量误解用户

### 6. 闭源对标与攻击面

- **OpenAI Whisper API**（`/v1/audio/transcriptions`）：$0.006/min，高频用量成本可观；distil-whisper 本地等价精度（~1% WER 差），但速度更快、无费用、不上云；攻击面 = 每分钟计费、数据上传 OpenAI 服务器、断网不可用
- **Deepgram**（✅ 已有报告）：Nova-3 $0.0059/min，按量收费；Olares 本地 distil-whisper 一次性部署 = 边际成本归零
- **AssemblyAI**：类似 SaaS 订阅/按量收费；隐私政策下音频存云端，攻击面同上
- **Groq + distil-whisper**：Groq 也托管 distil-whisper，速度极快但仍属云端 API（数据出机）；对比点 = "云端 Groq vs 本地 Olares"，前者极速但有隐私/费用顾虑，后者数据本地且无限量
- **统一攻击面**：API 费用（量大时可观）+ 云端隐私（音频上传第三方）+ 断网不可用；Olares 本地 distil-whisper = 无费用 + 数据不出机 + 离线可用

### 7. 与 model/models.md 同类 family 及 whisper.md 的关联

- 本报告与 [whisper.md](/Users/pengpeng/seo/directions/model/reports/06-stt/whisper.md) 高度互补：父报告覆盖全语言/全尺寸，distil-whisper 报告专注**英文实时速度优化场景**——两报告词库叠加，内容层可分开写文（`faster-whisper + distil-large-v3.5 local`、`distil-whisper vs whisper large-v3`）
- `whisper alternative`（KD 10）、`run whisper locally`（CPC $6.32）两词在父报告已标为主词候选；distil-whisper 报告加强了"6x 速度 + 更低 VRAM"的叙事角度，seo-content 可在同一词簇里差异化展开
- 后续 06-stt 章节可增补 Parakeet（NVIDIA，英文专用）、Wav2Vec2、NeMo 形成横向对比

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch、phrase_related、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
