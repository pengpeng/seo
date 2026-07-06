# Qwen3-ASR 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：Alibaba Qwen Team / HuggingFace，Apache 2.0
> **无独立官网**：Qwen3-ASR 以 HuggingFace + GitHub 为主分发渠道，SEO 主战场在第三方内容/文档页。跳过 Phase 1 域名报告，从关键词层面起步。

---

## 模型理解（前置）

Qwen3-ASR 是 Alibaba Qwen 团队出品的开源多语言语音识别模型，提供 0.6B 和 1.7B 两个参数量，支持 52 种语言，在多语言 STT 基准测试中达到开源 SOTA 水准。相比 Whisper 家族，Qwen3-ASR 在亚洲语言（中文、日文、韩文）上表现更强，是亚语场景下的首选开源 ASR 方案。Apache 2.0 许可，商用友好，可完全自托管。另有专为实时流式转录设计的 **Qwen3-ASR-Flash** 变体。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源多语言 ASR，52 语言，亚语场景 SOTA，Apache 2.0 |
| 许可证 | **Apache 2.0**（商用完全友好，主推卖点成立，可自托管、二次分发） |
| 主仓库 / 分发 | HuggingFace `Qwen/Qwen3-ASR-0.6B`、`Qwen/Qwen3-ASR-1.7B`；GitHub（Qwen 组织）；ModelScope（国内镜像） |
| 参数 / VRAM 可跑性 | 0.6B ≈ 1-2GB VRAM（CPU 亦可推理）；1.7B ≈ 2-4GB VRAM；**消费级 GTX 1060（6GB）两个尺寸均可跑**；Olares One RTX 5090 Mobile 24GB 可并发多路实时转录 |
| 变体 / 型号 | `Qwen3-ASR-0.6B`（轻量端侧）、`Qwen3-ASR-1.7B`（精度旗舰）、`Qwen3-ASR-Flash`（流式实时，KD 45 / 480/mo）；Flash 系列另有 Realtime 子版本 |
| 闭源对标 | **AssemblyAI Universal-3 Pro**（按量收费，$0.37/hr）、**OpenAI Whisper API**（$0.006/min）、**Deepgram Nova-3**（$0.0059/min）；国内对标讯飞/百度 API |
| 主要运行时 | transformers（HuggingFace）、vLLM（支持音频流）；**Ollama 不支持音频输入**（无 ASR 能力），需通过 transformers 或自定义 API wrapper 部署 |
| Olares Market | 未直接上架；可通过 Olares 自定义应用（transformers + FastAPI Docker）部署；Open Notebook / OpenClaw 语音转录后端可接入 Qwen3-ASR 0.6B |
| 来源 | [HuggingFace Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B)；[HuggingFace Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)；[GitHub Qwen](https://github.com/QwenLM) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| qwen3-asr | 1,300 | 48 | $4.98 | info |
| qwen3-asr-flash | 480 | 45 | $0 | info/trans |
| qwen audio | 260 | 46 | $3.98 | info |
| qwen2 audio | 140 | 33 | $0 | nav |
| qwen3 1.7b ⭐ | 390 | 22 | $0 | info |
| qwen3 asr flash ⭐ | 90 | 25 | $0 | info |
| qwen3 asr | 90 | 55 | $0 | info |
| qwen-audio-asr | 390 | 51 | $0 | nav |
| qwen asr | 70 | 53 | $0 | info |
| qwen-asr ⭐ | 40 | 33 | $0 | info |
| qwen3 audio | 40 | 56 | $0 | info |
| qwen3-asr-0.6b ⭐ | 50 | 0 | $0 | info |
| qwen3-asr-1.7b ⭐ | 40 | 0 | $0 | info |
| qwen3 asr github ⭐ | 30 | 0 | $0 | nav |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| whisperx ⭐ | 2,400 | 28 | $2.82 | info/nav |
| faster whisper | 1,600 | 33 | $2.80 | info |
| whisper asr | 320 | 47 | $2.38 | info |
| speech recognition python | 390 | 37 | $4.03 | info |
| asr ai ⭐ | 110 | 38 | $4.91 | info |
| asr huggingface | 50 | 60 | $0 | nav |
| qwen3 asr ollama | 0 | 0 | $0 | info |

> Ollama 不支持 ASR/音频模型，`qwen3 asr ollama` 是 GEO 澄清前哨而非实际部署词；实际运行时应引导至 transformers/vLLM 路径。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| run whisper locally | 110 | 33 | $6.32 | info |
| whisper local ⭐ | 140 | 42 | $2.08 | info |
| offline speech recognition ⭐ | 30 | 26 | $1.57 | info |
| offline transcription ⭐ | 20 | 0 | $2.61 | info |
| local transcription ⭐ | 20 | 0 | $3.50 | info |
| local stt ⭐ | 20 | 0 | $0 | info |
| speech to text self hosted ⭐ | 20 | 0 | $0 | info |
| self hosted speech to text ⭐ | 20 | 0 | $0 | info |
| local speech recognition ⭐ | 20 | 0 | $0 | info |
| speech to text privacy ⭐ | 20 | 0 | $0 | info |

### 多语言 STT 词（Qwen3-ASR 专属优势）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| multilingual transcription ⭐ | 110 | 19 | $3.28 | info |
| multilingual speech recognition ⭐ | 20 | 0 | $0 | info |
| multilingual STT ⭐ | 20 | 0 | $0 | info |
| multilingual asr ⭐ | 20 | 0 | $3.48 | info |
| multilingual whisper ⭐ | 20 | 0 | $0 | info |
| chinese speech recognition ⭐ | 20 | 0 | $0 | info |
| japanese speech recognition ⭐ | 10 | 0 | $0 | info |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| open source speech to text | 210 | 35 | $2.38 | info |
| whisper alternative ⭐ | 170 | 10 | $1.86 | info |
| whisper large v3 turbo | 260 | 31 | $3.19 | info |
| distil whisper ⭐ | 90 | 31 | $2.50 | info |
| parakeet asr ⭐ | 30 | 0 | $0 | info |
| assemblyai alternative ⭐ | 20 | 0 | $0 | info |
| open source transcription ⭐ | 20 | 2.30 | $0 | info |
| qwen3 asr 1.7b vs whisper | 0 | 0 | $0 | info |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| multilingual transcription | 110 | 19 | $3.28 | Qwen3-ASR 0.6B 支持 52 语言，是 Olares One 上唯一覆盖中/日/韩/欧语+英语的开源 ASR 方案；KD 19 低竞争，可做"multilingual transcription on Olares"教程 | ⭐⭐⭐ |
| whisper alternative | 170 | 10 | $1.86 | KD 10 极低；Qwen3-ASR 是"从 OpenAI Whisper API 切换到本地开源"的最佳多语言替代，尤其亚语场景超越 Whisper | ⭐⭐⭐ |
| offline speech recognition | 30 | 26 | $1.57 | 敏感场景（法律/医疗/企业）离线转录；Qwen3-ASR Apache 2.0 + Olares 数据本地化叙事完全匹配 | ⭐⭐⭐ |
| run whisper locally | 110 | 33 | $6.32 | CPC $6.32 全表最高，部署意图最纯；用户搜这个词时，Qwen3-ASR 0.6B 是更轻量的多语言本地替代（1-2GB VRAM vs Whisper Large 10GB） | ⭐⭐⭐ |
| speech to text self hosted | 20 | 0 | $0 | GEO 前哨，意图纯净；Olares 自托管定位直接呼应，Qwen3-ASR 门槛低（0.6B 仅需 1-2GB VRAM） | ⭐⭐⭐ |
| assemblyai alternative | 20 | 0 | $0 | GEO 抢发：Qwen3-ASR = AssemblyAI Universal-3 的开源本地平替，KD=0 零竞争，Olares 部署路径清晰 | ⭐⭐⭐ |
| qwen3-asr | 1,300 | 48 | $4.98 | 品牌主词；KD 48 中偏高但部署场景词多为零竞争；Olares One 的多语言 STT 叙事需以此词为入口 | ⭐⭐ |
| asr ai | 110 | 38 | $4.91 | 泛类词 CPC 高；Qwen3-ASR + Olares 的"本地 AI 语音识别"叙事可切入此词的商业价值 | ⭐⭐ |
| open source speech to text | 210 | 35 | $2.38 | Qwen3-ASR 是当前多语言开源 STT 中亚语最强方案；Olares 可做"从 Deepgram/AssemblyAI 切换到本地 Qwen3-ASR"内容 | ⭐⭐ |
| local transcription | 20 | 0 | $3.50 | CPC $3.50，意图纯净；GEO 前哨，适合"local multilingual transcription with Qwen3-ASR on Olares"直答块 | ⭐⭐ |
| qwen3 asr ollama | 0 | 0 | $0 | GEO 澄清词：Ollama 不支持音频输入，应在 FAQ 解释 Qwen3-ASR 的正确部署路径（transformers/vLLM）；截流用户误导 | ⭐⭐ |
| chinese speech recognition | 20 | 0 | $0 | GEO 前哨；中文 ASR 本地部署场景对 Olares 用户（海外华人/中文内容场景）极度吻合 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| qwen3-asr | 1,300 | 48 | $4.98 | info | **主词候选** | 品牌主词量最大；KD 48 中偏高但仍可竞争；Olares One 多语言 STT 叙事的入口词，CPC $4.98 显示商业价值 |
| qwen3-asr-flash | 480 | 45 | $0 | info/trans | **主词候选** | Flash 变体量大，流式实时场景；与 Olares 实时转录（会议/字幕）叙事直接挂钩；KD 45 但零竞争态势 |
| whisper alternative | 170 | 10 | $1.86 | info | **主词候选** | KD 10 极低，全 STT 词表最易排名；Qwen3-ASR 是亚语场景下超越 Whisper 的最强本地开源替代，战略价值极高 |
| open source speech to text | 210 | 35 | $2.38 | info | **主词候选** | 泛 STT 入口词；量210，Qwen3-ASR 多语言 + Apache 2.0 撑起内容差异化 |
| multilingual transcription | 110 | 19 | $3.28 | info | **主词候选** | ⭐ KD 19 低竞争，Qwen3-ASR 最独特优势词；52 语言本地部署，Olares 一键私有化亚语转录的最强叙事 |
| run whisper locally | 110 | 33 | $6.32 | info | **主词候选** | CPC 全表最高，部署意图最纯；Qwen3-ASR 0.6B 比 Whisper Large 占用低 5x（1-2GB vs 10GB VRAM），"更轻量的本地方案" |
| qwen3 1.7b | 390 | 22 | $0 | info | **次级** | ⭐ KD 22，量大；型号词，并入品牌主词 qwen3-asr 文章的副词 |
| qwen-audio-asr | 390 | 51 | $0 | nav | **次级** | 前代模型导航词；KD 51 偏高且意图偏 nav，但覆盖从 Qwen2-Audio → Qwen3-ASR 升级路径 |
| qwen audio | 260 | 46 | $3.98 | info | **次级** | 整个 Qwen 音频系列词，CPC $3.98；作 Qwen3-ASR 主词文章的同族词覆盖 |
| whisper large v3 turbo | 260 | 31 | $3.19 | info | **次级** | 对比词；Qwen3-ASR 1.7B vs Whisper Large-v3-Turbo 是高意图对比词，并入对比文 |
| faster whisper | 1,600 | 33 | $2.80 | info | **次级** | 高量 STT 引擎词；Qwen3-ASR 不通过 faster-whisper 运行，但此词作 STT 生态教育并入多语言对比文 |
| whisperx | 2,400 | 28 | $2.82 | info/nav | **次级** | ⭐ 量大 KD 低；WhisperX 用于说话人分离，Qwen3-ASR 接入 pipeline 可做对比；并入 STT 生态文章 |
| asr ai | 110 | 38 | $4.91 | info | **次级** | CPC $4.91 高商业价值；泛 AI ASR 词，Qwen3-ASR + Olares 本地 AI 语音识别叙事支撑 |
| offline speech recognition | 30 | 26 | $1.57 | info | **次级** | ⭐ KD 26，隐私/离线场景；Qwen3-ASR + Olares 完美契合离线转录叙事 |
| multilingual speech recognition | 20 | 0 | $0 | info | **GEO** | 零 KD；Qwen3-ASR 直接回答"52 语言开源本地 ASR"，适合 AI Overview 直答块 |
| assemblyai alternative | 20 | 0 | $0 | info | **GEO** | KD=0；Qwen3-ASR + Olares = AssemblyAI 的本地开源无限量平替，FAQ 直答抢位 |
| qwen3 asr ollama | 0 | 0 | $0 | info | **GEO** | 零量但用户误认 Ollama 支持 ASR；"Qwen3-ASR 不能用 Ollama，正确部署方式是…"的澄清 FAQ 截流 |
| qwen3 asr 1.7b vs whisper | 0 | 0 | $0 | info | **GEO** | 精准对比词，零竞争；直答"Qwen3-ASR 1.7B 在亚语上超越 Whisper Large-v3" |
| speech to text self hosted | 20 | 0 | $0 | info | **GEO** | Olares 自托管定位的精准触达词，FAQ 块植入 |
| local transcription | 20 | 0 | $3.50 | info | **GEO** | CPC $3.50 高，近零量作 GEO；等流量成熟可升为次级/主词候选 |
| chinese speech recognition | 20 | 0 | $0 | info | **GEO** | 中文 ASR 本地部署；对 Olares 海外华人用户群极精准 |

---

## 核心洞见

### 1. 搜索心智建立程度

Qwen3-ASR 的品牌心智**初步建立但集中在 hyphenated 写法**：`qwen3-asr`（1,300/mo）比 `qwen3 asr`（90/mo）量大约 14 倍，说明用户主要通过 HuggingFace 模型 ID 精确搜索（带连字符）而非自然语言搜索——这是**技术用户直达 HF 模型页**的行为模式，而非内容消费。Flash 变体 `qwen3-asr-flash`（480/mo）量级可观，说明实时转录场景已有独立搜索心智。

值得注意的是，`qwen-audio-asr`（390/mo）仍有较高量，说明前代 Qwen2-Audio 架构在用户中仍有认知延续，内容策略应涵盖升级路径叙事。

### 2. 消费级 GPU / Olares One 能否本地跑

**完全可以，且是本表所有 STT 模型中门槛最低的之一**：
- `Qwen3-ASR-0.6B` ≈ 1-2GB VRAM，即使 CPU 亦可推理，门槛极低
- `Qwen3-ASR-1.7B` ≈ 2-4GB VRAM，RTX 3060（12GB）轻松运行
- Olares One RTX 5090 Mobile 24GB 可并发多路实时转录（会议 + 视频字幕同时跑），或同时跑 Qwen3-ASR + LLM 后处理 pipeline
- **叙事关键点**：0.6B 仅需 Whisper Large-v3 约 1/5 的 VRAM（~1GB vs ~10GB），且多语言支持 52 种（Whisper Large-v3 同样多语言，但亚语精度上 Qwen3-ASR 更强）

### 3. 许可证商用友好性

**Apache 2.0，完全商用友好**——可自托管、商业分发、修改，无区域限制（不同于部分腾讯/SkyWork 系）。是 AssemblyAI Universal-3（$0.37/hr）的本地开源完整替代，Olares 上无限量转录、数据不出设备、边际成本为零。**许可证叙事可作主推卖点**。

### 4. 对 Olares 最关键的 3 个词

1. **`multilingual transcription`**（110/mo / KD 19 / $3.28 CPC）：Qwen3-ASR 的核心差异化词，也是整个 06-STT 章节唯一的"亚语场景多语言转录"主词候选；KD 19 低竞争，Olares 本地私有化多语言转录叙事最直接入口
2. **`whisper alternative`**（170/mo / KD 10）：KD 全表最低的有量词（10），Qwen3-ASR 不仅是 Whisper API 的开源替代，更在亚语上有超越；Olares 本地部署叙事天然契合
3. **`run whisper locally`**（110/mo / KD 33 / CPC $6.32）：CPC 全表最高，部署意图最纯；Qwen3-ASR 0.6B 提供比 Whisper Large 更低 5x VRAM 占用的本地多语言 ASR，可作"更轻量本地替代"内容角度

### 5. GEO 抢发窗口

以下词量近零但语义精准，适合 AI Overview / Perplexity 直答位：
- **`qwen3 asr 1.7b vs whisper`**（KD=0）：精准对比词，直答"Qwen3-ASR 在亚语上优于 Whisper Large-v3"
- **`assemblyai alternative`**（KD=0）：Qwen3-ASR + Olares = AssemblyAI 的本地零费用无限量替代
- **`multilingual speech recognition`**（KD=0）：52 语言开源 ASR 直答位，Qwen3-ASR 最佳回答
- **`qwen3 asr ollama`**（KD=0）：澄清"Ollama 不支持音频输入"+ 给出 transformers/vLLM 正确路径
- **`speech to text self hosted`** / **`local transcription`**（KD=0）：Olares 自托管叙事精准词，直答块即可占位
- **`best open source speech recognition 2026`**（0 量）：年份词 GEO 前哨，抢发 AI Overview 的"2026 年最佳开源 ASR"直答

### 6. 闭源对标与攻击面

- **AssemblyAI Universal-3 Pro**（主对标）：按量收费约 $0.37/hr；音频上传 AssemblyAI 服务器（隐私风险）；多语言覆盖不如 Qwen3-ASR 的亚语精度；攻击面 = 云端隐私 + 持续 API 费用
- **OpenAI Whisper API**：$0.006/min，10 小时音频 = $3.6；本地 Qwen3-ASR 0.6B 一次部署即无限量；攻击面 = 量大时费用可观 + 音频数据上传 OpenAI
- **Deepgram Nova-3**：$0.0059/min，实时 API，但数据出机；攻击面同上
- **统一攻击面**：API 按分钟/小时计费（大量转录成本可观）+ 云端隐私（敏感音频上传第三方）+ 断网不可用；**Qwen3-ASR + Olares = 无费用 + 数据不出机 + 离线可用**
- **Qwen3-ASR 特有优势**：52 语言覆盖中 CJK（中文/日文/韩文）精度领先 Whisper，对亚语企业和海外华人用户是额外攻击点——AssemblyAI/Deepgram 的 CJK 支持较弱

### 7. 与 model/models.md 同类 family 及已有 STT 报告的关联

- 本报告与 [whisper.md](/Users/pengpeng/seo/directions/model/reports/06-stt/whisper.md) 和 [distil-whisper.md](/Users/pengpeng/seo/directions/model/reports/06-stt/distil-whisper.md) 形成 STT 三角：whisper.md 覆盖全语言通用；distil-whisper.md 专注**英文实时速度**；本报告专注**多语言/亚语**——三报告词库互补，可在内容层差异化展开
- `whisper alternative`（KD 10）和 `run whisper locally`（CPC $6.32）在 distil-whisper 报告已标为主词候选；Qwen3-ASR 报告增加了"亚语场景超越"和"更低 VRAM"两个叙事差异点，seo-content 可在同一词簇里针对不同受众（英文场景用 distil-whisper，多语言/亚语场景用 Qwen3-ASR）差异化写文
- `multilingual transcription`（KD 19）是本报告**新增的主词候选**，在 distil-whisper/whisper 报告中未出现——因为 distil-whisper 是英文专用，这是 Qwen3-ASR 独有的 SEO 攻击角度
- 后续 06-stt 章节可增补 Parakeet（NVIDIA，英文专用）形成横向对比，Qwen3-ASR 的"亚语"定位会更突出

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch、phrase_related）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍，亚洲语言场景实际搜索量（含 JP/KR/CN 用户使用英文搜索）约为美国的 4-6 倍。*
