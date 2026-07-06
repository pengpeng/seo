# Granite Speech 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：ibm-granite/granite-speech-models（GitHub），Apache 2.0
> **无独立官网**：Granite Speech 以 HuggingFace + GitHub 为主分发渠道，官方入口在 ibm.com/granite（与整个 Granite 家族共用，不做 Phase 1 域名独立流量分析），SEO 主战场在第三方内容/文档页。跳过 Phase 1 域名报告，从关键词层面起步。

---

## 模型理解（前置）

Granite Speech 3.3 是 IBM 于 2025 年 6 月 19 日发布的语音语言模型家族，提供 2B 与 8B 两个量级，支持**自动语音识别（ASR）**和**自动语音翻译（AST）**。区别于 Whisper 等端到端方案，它采用**两步设计**：第一步由 Speech 编码器转录音频为文字，第二步调用底层 Granite 3.3 Instruct LLM 进一步处理，从而保留 LLM 的推理与安全能力。8B 版在 IBM 测试中 AST 性能与 GPT-4o、Gemini 2.0 Flash 持平（CoVost 数据集），并超越 Whisper Large-v3 的英文 WER。Apache 2.0 许可，商用完全友好。

| 项目 | 内容 |
|------|------|
| 一句话定位 | IBM 出品的 2B/8B 语音-语言模型，ASR + 多语言翻译，Apache 2.0，商用友好 |
| 许可证 | **Apache 2.0**（商用友好，可自托管二次分发，主推卖点成立） |
| 主仓库 / 分发 | [GitHub ibm-granite/granite-speech-models](https://github.com/ibm-granite/granite-speech-models)（~380 ★）；HuggingFace `ibm-granite/granite-speech-3.3-8b`、`ibm-granite/granite-speech-3.3-2b`；Ollama / LMStudio / Replicate（底层 Granite Instruct LLM，非 Speech 端到端）；watsonx.ai（企业托管） |
| 参数 / VRAM 可跑性 | 2B：FP16 ~6 GB、Q8 ~4 GB、**Q4 ~2.5 GB**（4 GB 显存卡可跑，Olares One RTX 5090 Mobile 24 GB 完全够用）；8B：FP16 ~16 GB、Q8 ~9 GB、**Q4 ~5 GB**（8 GB 显存卡可跑 Q4）；消费级 RTX 4060 8 GB 可跑 8B Q4 |
| 变体 / 型号 | `granite-speech-3.3-2b`、`granite-speech-3.3-8b`（已发布）；`granite-speech-4.1-2b`（后续迭代，社区 GGUF 量化版已上 HF）；两步设计可单独只做 ASR 省 VRAM |
| 语言支持 | ASR：英、法、德、西、葡；AST：英→法/西/意/德/葡/日/中；多语言 X→英（法/德/西/葡→英） |
| 闭源对标 | **AssemblyAI**（Universal-2，$0.65/hr 流式）、**Deepgram**（Nova-3，$0.59/hr）；翻译侧对标 **OpenAI Whisper API + GPT-4o Audio**；IBM 自家历史遗产对标 **IBM Watson Speech to Text** |
| Olares Market | 未直接上架；vLLM 已支持 Granite Speech（`limit_mm_per_prompt=audio:1`），可通过 vLLM 容器在 Olares 自定义应用中部署；2B Q4 GGUF 社区量化版可通过 llama.cpp 加载 |
| 来源 | [HF granite-speech-3.3-8b](https://huggingface.co/ibm-granite/granite-speech-3.3-8b)；[HF granite-speech-3.3-2b](https://huggingface.co/ibm-granite/granite-speech-3.3-2b)；[IBM 官方发布博客](https://www.ibm.com/new/announcements/ibm-granite-3-3-speech-recognition-refined-reasoning-rag-loras)；[GitHub ibm-granite/granite-speech-models](https://github.com/ibm-granite/granite-speech-models) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| granite speech | 50 | 31 | $0 | 信息 |
| ⭐ granite speech 3.3 | 20 | 0 | $0 | 信息 |
| ⭐ ibm granite speech | 20 | 0 | $5.76 | 信息 |
| ⭐ granite speech 3.3 8b | 20 | 0 | $0 | 信息 |
| ⭐ ibm granite speech 3.3 8b | 20 | 0 | $0 | 信息 |
| ibm granite 3.3 | 30 | 0 | $0 | 信息 |
| granite 3.3 | 110 | 38 | $0 | 信息 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ⭐ ibm granite ollama | 20 | 0 | $0 | 信息 |
| granite speech vllm | 0 | — | — | — |
| granite speech local | 0 | — | — | — |
| granite speech install | 0 | — | — | — |

> 引擎组合词几乎全为近零量——模型发布不足一年，搜索心智尚在形成期，属 GEO 抢发窗口。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ⭐ speech to text self hosted | 20 | 0 | $0 | 信息 |
| ⭐ self hosted speech to text | 20 | 0 | $0 | 信息 |
| ⭐ offline speech recognition | 30 | 26 | $1.57 | 信息 |
| local speech to text | 30 | 54 | $2.37 | 商业 |
| run whisper locally | 110 | 33 | $6.32 | 信息 |
| whisper local | 140 | 42 | $2.08 | 信息 |

> "run whisper locally"（110/月）是目前本地 ASR 最强流量词，Granite Speech 可以 Whisper 平替角度切入。

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ⭐ whisper alternative | 170 | 10 | $1.86 | 信息 |
| ⭐ open source speech to text | 210 | 35 | $2.38 | 信息 |
| ⭐ ibm watson speech to text | 210 | 23 | $5.37 | 商业 |
| ⭐ best open source speech to text | 30 | 0 | $3.09 | 信息 |
| ⭐ assemblyai alternative | 20 | 0 | $0 | 信息 |
| ⭐ deepgram nova | 20 | 0 | $6.31 | 信息 |
| assemblyai vs deepgram | 20 | 0 | $6.44 | 信息 |
| ⭐ ibm speech to text | 20 | 0 | $3.45 | 信息 |
| speech recognition api | 590 | 69 | $126.55 | 商业 |
| speech to text model | 210 | 46 | $7.41 | 信息 |
| whisper asr | 320 | 47 | $2.38 | 信息 |
| automatic speech translation | 110 | 64 | $2.98 | 信息 |
| faster whisper | 1600 | 33 | $2.80 | 信息 |
| distil whisper | 90 | 31 | $2.50 | 信息 |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| ⭐ whisper alternative | 170 | 10 | $1.86 | Granite Speech = Apache 2.0 本地 Whisper 平替，Olares 一键部署 vLLM + Granite Speech 实现私有化转录 | ⭐⭐⭐ |
| ⭐ self hosted speech to text | 20 | 0 | $0 | 数据不出本机，本地 ASR；Olares 提供统一存储和私有 API 端点 | ⭐⭐⭐ |
| ⭐ speech to text self hosted | 20 | 0 | $0 | 同上，长尾变体 | ⭐⭐⭐ |
| ⭐ assemblyai alternative | 20 | 0 | $0 | Olares 自托管 Granite Speech 2B 替代 AssemblyAI 订阅费，零 API 成本 | ⭐⭐⭐ |
| ⭐ open source speech to text | 210 | 35 | $2.38 | IBM + Apache 2.0 + 本地可跑，Olares 场景天然契合 | ⭐⭐ |
| ⭐ ibm watson speech to text | 210 | 23 | $5.37 | 老 Watson STT 迁移路线：自托管新 Granite Speech，IBM 生态延续 + 隐私升级 | ⭐⭐ |
| ⭐ offline speech recognition | 30 | 26 | $1.57 | 无网络离线转录，Olares One 本地运行不依赖云端 | ⭐⭐⭐ |
| ⭐ ibm granite ollama | 20 | 0 | $0 | 底层 Granite Instruct LLM 可通过 Ollama 在 Olares 一键部署（Speech 端不支持 Ollama，需 vLLM；但可引流 Granite 系列认知） | ⭐⭐ |
| ⭐ best open source speech to text | 30 | 0 | $3.09 | 榜单型内容机会：Granite Speech 2B 作为轻量首选，配合 Olares 部署引导 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|----|------|------|--------------------------|
| open source speech to text | 210 | 35 | $2.38 | 信息 | 主词候选 | 量最大的 STT 开源词，Granite Speech/Whisper/Faster-Whisper 三角竞争，Olares 本地部署切入点 |
| ibm watson speech to text | 210 | 23 | $5.37 | 商业 | 主词候选 | ⭐ KD 23 量 210，Watson→Granite 迁移叙事，IBM 忠实用户转化机会 |
| whisper alternative | 170 | 10 | $1.86 | 信息 | 主词候选 | ⭐ KD 10 量 170，竞争最低、流量最大的对比词，Granite Speech 直接受益 |
| whisper local | 140 | 42 | $2.08 | 信息 | 次级 | 本地 Whisper 搜索心智已建立，可以 Granite Speech vs Whisper 角度写本地部署对比 |
| run whisper locally | 110 | 33 | $6.32 | 信息 | 次级 | Olares 部署教程的流量入口词，CPC $6.32 显示商业价值 |
| automatic speech translation | 110 | 64 | $2.98 | 信息 | 次级 | AST 侧流量词，Granite Speech 翻译能力切入点；KD 较高适合长文 |
| granite 3.3 | 110 | 38 | $0 | 信息 | 次级 | Granite 家族品牌词，具体落在 LLM 侧；Speech 报告可共享流量认知 |
| ibm granite model | 110 | 71 | $5.32 | 信息 | 次级 | KD 71 品牌竞争激烈，建议走长尾型号词 |
| ibm granite | 1300 | 82 | $16.31 | 信息 | 次级 | 品牌主词，KD 极高；作为内容背书词而非主攻词 |
| faster whisper | 1600 | 33 | $2.80 | 信息 | 次级 | 量最大的本地 ASR 词；Granite Speech 若做 GGUF/llama.cpp 支持可直接参与竞争 |
| granite speech | 50 | 31 | $0 | 信息 | 次级 | 模型自身品牌词量偏低；GEO/内容积累后可提升 |
| offline speech recognition | 30 | 26 | $1.57 | 信息 | 次级 | ⭐ KD 26，隐私/离线叙事契合 Olares；与 self hosted 词群合并写 |
| best open source speech to text | 30 | 0 | $3.09 | 信息 | GEO | ⭐ 零 KD，榜单型词，GEO 抢发 AI Overview 高价值 |
| self hosted speech to text | 20 | 0 | $0 | 信息 | GEO | ⭐ 零 KD 自托管词，Olares 场景直接命中，抢 AI Overview 位 |
| ibm granite speech | 20 | 0 | $5.76 | 信息 | GEO | ⭐ 零 KD，CPC $5.76 说明商业价值，搜索心智形成前抢发 |
| granite speech 3.3 | 20 | 0 | $0 | 信息 | GEO | ⭐ 零 KD，品牌+版本词，AI Overview 占位 |
| granite speech 3.3 8b | 20 | 0 | $0 | 信息 | GEO | ⭐ 零 KD，型号精准词，技术文档类页面抢发 |
| assemblyai alternative | 20 | 0 | $0 | 信息 | GEO | ⭐ 零 KD，对标 AssemblyAI 的 alternative 词，GEO 窗口 |
| assemblyai vs deepgram | 20 | 0 | $6.44 | 信息 | GEO | ⭐ 零 KD CPC $6.44，三方对比文加入 Granite Speech 自托管选项 |
| ibm granite ollama | 20 | 0 | $0 | 信息 | GEO | ⭐ 引擎组合词，Olares 一键 Ollama 部署 Granite Instruct 后续可扩展到 Speech |

---

## 核心洞见

1. **搜索心智处于萌发期，GEO 窗口开放**：品牌词"granite speech"仅 50/月，"granite speech 3.3"等型号词均在 20/月量级 KD 为 0——模型于 2025 年 6 月发布，搜索生态尚未形成。这是 AI Overview / Perplexity 抢发的黄金期，现在写技术内容有很高的 GEO 引用概率。

2. **消费级 GPU / Olares One 均可本地跑**：2B 版 Q4 约 2.5 GB VRAM，**任何 4 GB 以上显卡都能跑**，Olares One（RTX 5090 Mobile 24 GB）可跑满血 8B FP16 且留有多实例余量。两步设计还允许仅跑第一步 ASR 进一步降 VRAM 需求。本地部署叙事完全成立。

3. **Apache 2.0，主推卖点成立**：无地区限制、无商用约束，可直接在产品页主推"Apache 2.0，免费自托管，零 API 费用"。对标 AssemblyAI（$0.65/hr）和 Deepgram（$0.59/hr），年费节省估算可写进 landing page。

4. **对 Olares 最关键的 3 个词**：
   - `whisper alternative`（KD 10 / 170/月）：竞争极低、量较高，写 Granite Speech vs Whisper 本地部署对比，Olares 引导最顺畅；
   - `self hosted speech to text` / `speech to text self hosted`（KD 0）：零竞争自托管词，直接命中 Olares 场景；
   - `ibm watson speech to text`（KD 23 / 210/月）：Watson STT 老用户迁移需求，企业转化价值高，Granite Speech 作为 IBM 自家继任者天然承接。

5. **GEO 抢发窗口**：`best open source speech to text`（KD 0 / 30/月）、`assemblyai alternative`（KD 0）、`granite speech 3.3`（KD 0）、`ibm granite speech`（KD 0 / CPC $5.76）——这些词现在写技术文章，6-12 个月内有望在 AI Overview 里拿到优先引用位。

6. **闭源对标与攻击面**：
   - **AssemblyAI**（Universal-2）和 **Deepgram**（Nova-3）是主要对标——按小时/分钟计费、存在 API 速率限制、音频上传至云端；Granite Speech 本地跑零隐私顾虑、无并发限制、零边际成本。
   - **IBM Watson Speech to Text**（旧）：Granite Speech 是 IBM 官方"新一代"替代，帮助 Watson 客户平滑迁移，话术"同一 IBM，数据自己掌控"。
   - **OpenAI Whisper API**（$0.006/min）：Whisper 风格用户迁移的第二大机会词群（"whisper alternative" KD 10）。

7. **与同类 family 及 model/keywords.md 的关联**：同类 STT 报告中 [distil-whisper](/Users/pengpeng/seo/directions/model/reports/06-stt/distil-whisper.md)（英文蒸馏王）和 [parakeet-tdt](/Users/pengpeng/seo/directions/model/reports/06-stt/parakeet-tdt.md)（吞吐王）已有报告；Granite Speech 的差异定位是**多语言 ASR + AST + IBM 企业背书 + LLM 二步推理**，三者合力可写一篇"Best Open Source STT 2026"横评文章，覆盖 `open source speech to text`（210/月 KD 35）这个主词。

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
