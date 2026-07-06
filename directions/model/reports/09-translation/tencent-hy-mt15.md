# HY-MT1.5 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：tencent（HuggingFace / GitHub），Tencent HY Community License（有地区限制）

## 模型理解（前置）

HY-MT1.5 是腾讯混元团队于 2025 年 12 月 30 日发布的**专用机器翻译**模型族，包含 1.8B 和 7B 两个尺寸，支持 33 种语言互译及 5 种方言变体（藏语、粤语、哈萨克语、蒙古语、维吾尔语）。1.8B 量化后可部署于边缘设备，0.18 秒完成约 50 token 中文输入翻译；7B 是腾讯 WMT25 冠军系统的升级版，在 Flores-200 上达到 Gemini-3.0-Pro 的 95 百分位。两款型号均支持术语干预、上下文感知翻译与格式保留翻译。2026 年 5 月后续版本 Hy-MT2（含 30B MoE 旗舰）已发布，HY-MT1.5 仍是当前 7B 以下规模的最佳开源选项之一。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 专用机器翻译模型（33 语言），1.8B 边缘 + 7B 服务端，WMT25 冠军底座 |
| 许可证 | **Tencent HY Community License**——**不适用于欧盟、英国、韩国**；其他地区个人/商用可用，但月活 >1 亿需单独授权；不可作为"商用友好"的主推卖点，建议以"本地部署规避云端合规"为切入点 |
| 主仓库 / 分发 | GitHub: [Tencent-Hunyuan/Hy-MT](https://github.com/Tencent-Hunyuan/Hy-MT)（★746）；HuggingFace: tencent/HY-MT1.5-1.8B（下载量约 26,354/月）/ HY-MT1.5-7B；提供 FP8、GPTQ-Int4、GGUF 量化变体 |
| 参数 / VRAM 可跑性 | 1.8B fp16 约 3.6 GB VRAM，Int4 量化 ~1 GB（可跑在 CPU/边缘设备）；7B fp16 约 14 GB，Int4 约 4 GB，**消费级 8 GB 显卡（Int4）可跑**；Olares One（NVIDIA RTX/≥8 GB）可流畅运行 7B-Int4 及以下所有变体 |
| 变体 / 型号 | HY-MT1.5-1.8B / 1.8B-FP8 / 1.8B-GPTQ-Int4 / 1.8B-GGUF；HY-MT1.5-7B / 7B-FP8 / 7B-GPTQ-Int4 / 7B-GGUF |
| 闭源对标 | DeepL API、Google Translate API（商业翻译 API）；Gemini-3.0-Pro（顶级 LLM 翻译基线）；Tower-Plus-72B（学术 SOTA 对标） |
| Olares Market | 未单独上架；可通过 Ollama（已在 Olares Market）或 vLLM 引擎加载 GGUF / fp8 变体；直接 Docker/transformers 部署亦可 |
| 来源 | [HF model card](https://huggingface.co/tencent/HY-MT1.5-1.8B)；[GitHub](https://github.com/Tencent-Hunyuan/Hy-MT)；[技术报告 arXiv:2512.24092](https://arxiv.org/abs/2512.24092)；[MarkTechPost 2026-01-04](https://www.marktechpost.com/2026/01/04/tencent-researchers-release-tencent-hy-mt1-5/) |

> **无独立官网**，SEO 主战场在 HuggingFace 模型页、GitHub、第三方技术媒体与内容页。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| hy-mt1.5 | 40 | 0 | $0 | — |
| hy mt1.5 | 40 | 0 | $0 | — |
| hunyuan mt | 20 | 48 | $0 | info |
| hy-mt1.5-7b | 10 | 0 | $0 | — |

*注：HY-MT1.5-1.8B、HY-MT1.5-GGUF 等具体变体词近零量，属 GEO 前哨候选。*

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| hy-mt1.5 ollama | 0 | 0 | $0 | — |
| hy-mt1.5 vllm | 0 | 0 | $0 | — |
| local llm translation ⭐ | 20 | 0 | $0 | info |
| llm machine translation ⭐ | 20 | 0 | $0 | info |
| llm for translation ⭐ | 10 | 0 | $5.34 | comm |

*引擎组合词（hy-mt + ollama/vllm）目前近零量，但语义精准，适合 GEO 抢发。"local llm translation" 是 Olares 叙事的最佳载体词。*

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| libre translate ⭐ | 260 | 23 | $3.71 | trans |
| argos translate ⭐ | 260 | 40 | $6.35 | info |
| offline machine translation ⭐ | 20 | 0 | $0 | — |
| translation without internet ⭐ | 30 | 0 | $1.01 | — |
| open source machine translation ⭐ | 20 | 0 | $0 | — |
| neural machine translation open source ⭐ | 20 | 0 | $0 | — |
| open source translation model ⭐ | 10 | 0 | $0 | — |
| translation software open source ⭐ | 10 | 0 | $0 | — |

*LibreTranslate / Argos Translate 是当前最活跃的"本地翻译"开源品牌，量各 260/月，KD 低，是竞品替代词切入点。*

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| best deepl alternatives 2025 ⭐ | 720 | 12 | $0 | info |
| google translate alternative ⭐ | 210 | 20 | $1.52 | info |
| deepl alternative ⭐ | 110 | 17 | $2.13 | info |
| google translate alternatives ⭐ | 110 | 29 | $2.19 | info |
| alternative to google translate ⭐ | 90 | 15 | $1.76 | info |
| alternatives to google translate ⭐ | 90 | 16 | $1.76 | info |
| best translation program ⭐ | 90 | 24 | $4.65 | info |
| business translation software ⭐ | 70 | 35 | $0 | info/comm |
| best machine translation | 110 | 24 | $2.37 | info |
| neural machine translation | 480 | 49 | $3 | info |
| document translation software | 210 | 32 | $3.52 | info |
| ai translation tool | 320 | 83 | $6.21 | info/comm |
| free translation api | 210 | 82 | $5.40 | info |
| deepl api | 880 | 57 | $4.72 | trans |
| machine translation software | 390 | 70 | $8.21 | info |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|------|
| best deepl alternatives 2025 ⭐ | 720 | 12 | $0 | DeepL 替代场景——在 Olares 本地部署 HY-MT1.5，零 API 费用、数据不离机；KD 仅 12 是难得低竞争高量词 | ⭐⭐⭐ |
| google translate alternative ⭐ | 210 | 20 | $1.52 | 隐私敏感用户弃用 Google Translate→自托管；Olares 一键部署本地翻译引擎 | ⭐⭐⭐ |
| local llm translation ⭐ | 20 | 0 | $0 | 直接命中"在 Olares One 本地跑翻译 LLM"叙事；近零量但意图极纯，GEO 前哨 | ⭐⭐⭐ |
| offline machine translation ⭐ | 20 | 0 | $0 | 离线场景：企业内网/敏感文件不经外网，Olares 承载完整翻译管道 | ⭐⭐⭐ |
| libre translate ⭐ | 260 | 23 | $3.71 | LibreTranslate 用户迁移：HY-MT1.5 质量远高于 LibreTranslate，可在 Olares 上替换 | ⭐⭐ |
| argos translate ⭐ | 260 | 40 | $6.35 | Argos Translate 用户对比场景，Olares 提供更易管理的部署方案 | ⭐⭐ |
| llm for translation ⭐ | 10 | 0 | $5.34 | 高 CPC 暗示商业意图；Olares 提供"用 LLM 做翻译的一键自托管路径" | ⭐⭐ |
| translation without internet ⭐ | 30 | 0 | $1.01 | 企业/政府离线翻译需求；Olares 自托管保障数据主权 | ⭐⭐ |
| open source translation model ⭐ | 10 | 0 | $0 | 近零竞争，与"在 Olares 部署开源翻译模型"叙事直接匹配 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| best deepl alternatives 2025 | 720 | 12 | $0 | info | **主词候选** | KD=12 难得；同族词（google translate alternative/deepl alternative）合计 >1,000/月；Olares 切入：本地部署 HY-MT1.5 作为零成本 DeepL 替代 |
| neural machine translation | 480 | 49 | $3 | info | 次级 | 量大但 KD=49 偏高；做同族文章里的背景词；不单独撑文章 |
| ai translation tool | 320 | 83 | $6.21 | info/comm | 次级 | KD=83 排不动；作为高商业价值次级词放进对比文 |
| machine translation software | 390 | 70 | $8.21 | info | 次级 | KD=70 难排；高 CPC 值作次级出现在对比表格中 |
| document translation software | 210 | 32 | $3.52 | info | 次级 | KD 尚可，可进"best deepl alternatives"文章的次级词 |
| deepl alternative | 110 | 17 | $2.13 | info | **主词候选** | KD=17 低，CPC=$2.13；与 best deepl alternatives 同簇；隐私导向角度强 |
| google translate alternative | 210 | 20 | $1.52 | info | **主词候选** | 量 210/月，KD=20；可独立成文或并入 DeepL alternatives 大簇 |
| best machine translation | 110 | 24 | $2.37 | info | 次级 | 量中等，KD=24 可争；作 listicle 类文章次级 |
| libre translate | 260 | 23 | $3.71 | trans | 次级 | LibreTranslate 用户发现 HY-MT1.5 的桥梁词；高 CPC 商业意图 |
| argos translate | 260 | 40 | $6.35 | info | 次级 | KD=40 中等；作对比词出现在 libre translate / deepl alternative 文章中 |
| local llm translation | 20 | 0 | $0 | info | **GEO 前哨** | 语义与 Olares"本地跑翻译 LLM"完全吻合；近零量但 AI Overview 抢位机会窗口 |
| llm machine translation | 20 | 0 | $0 | info | GEO 前哨 | 新词，抢 Perplexity / AI Overview 引用位 |
| llm for translation | 10 | 0 | $5.34 | comm | GEO 前哨 | 高 CPC 暗示高商业价值；GEO 抢发后可带来精准流量 |
| offline machine translation | 20 | 0 | $0 | — | GEO 前哨 | 企业离线/隐私场景；Olares 自托管叙事最强 |
| hy-mt1.5 | 40 | 0 | $0 | — | GEO 前哨 | 品牌词有量但偏小；新模型前期靠 GEO 抢发建心智 |
| open source translation model | 10 | 0 | $0 | info | GEO 前哨 | 近零竞争，精准命中自托管诉求 |
| translation without internet | 30 | 0 | $1.01 | — | GEO 前哨 | 离线翻译精准场景；Olares 数据主权叙事 |
| free translation api | 210 | 82 | $5.40 | info | 次级 | KD=82 不可排；但作次级出现在"替代 DeepL API"文章中捕捉高意图流量 |

---

## 核心洞见

1. **搜索心智尚未建立**：品牌词 `hy-mt1.5` 月量仅 40，`hunyuan mt` 20，模型本体词极弱。用户目前通过 HuggingFace 直达或搜索通用翻译词（machine translation、deepl alternative）发现此模型。需要靠内容（替代类文章 + GEO 植入）建立心智，而非依赖品牌词。

2. **消费级可跑，Olares One 完全覆盖**：7B-Int4 约 4 GB VRAM，消费级 8 GB 显卡可流畅运行；1.8B-GGUF 甚至可跑在 CPU 上。Olares One 的 NVIDIA GPU 配置轻松跑全系列变体，**"本地 7B 翻译模型，质量接近 Gemini-3.0-Pro"叙事成立**，是内容主轴。

3. **许可证有地区限制，不能单纯主推"商用友好"**：Tencent HY Community License 明确排除欧盟、英国、韩国。对这些地区用户应改口径为"本地部署，不依赖 Tencent 云端服务/审计"；月活>1 亿需额外授权，适合中型企业用户。SEO 叙事应强调**"自托管规避云端合规风险"**而非"Apache/MIT 商用自由"。

4. **对 Olares 最关键的 3 个词**：
   - `best deepl alternatives 2025`（月量 720，KD=12）——量最大且竞争最低，DeepL 替代场景下本地 HY-MT1.5 直接切入；
   - `google translate alternative`（月量 210，KD=20）——隐私/成本驱动的 Google 逃离族群；
   - `local llm translation`（月量 20，KD=0）——GEO 核心词，与 Olares"本地 AI OS"完全重合。

5. **GEO 抢发窗口**：`hy-mt1.5 ollama`、`hy-mt1.5 vllm`、`local llm translation`、`llm for translation`、`offline machine translation`、`open source translation model` 等词当前近零量，AI Overview / Perplexity 引用位空白。HY-MT1.5 于 2025 年底发布，内容尚稀，现在用直答块（"如何在 Olares One 上运行 HY-MT1.5？"）植入 FAQ 可抢占大量 GEO 权威位。

6. **闭源对标与攻击面**：
   - **DeepL API**（$0.03/字符）：用量大时成本高；HY-MT1.5 本地运行零边际成本，且可处理公司内部机密文件不经外部 API；
   - **Google Translate API**：隐私顾虑（数据进入 Google 训练流）；本地 HY-MT1.5 数据不离机；
   - **Gemini-3.0-Pro 翻译**：按 token 计费，1.8B 本地版在 33 语言上已超过多数商业 API；
   - 核心攻击面：**API 成本 + 数据隐私 + 离线可用性**，三点均为自托管天然优势。

7. **与同类 family 的关联**：同属 09-translation 类别；可与 LibreTranslate、Argos Translate 等开源对标做横向对比内容；`best deepl alternatives` 类文章可跨 commerce 目录下的 DeepL / Google Translate 报告取词（DeepL 品牌词量大）。`llm machine translation` 可与 LLM 章（01-llm）中的 Qwen3-Coder 等通用模型做区分：HY-MT1.5 是专用翻译模型，推理效率更高、33 语言对更准。

---

*数据来源：SEMrush US（phrase_these × 3、phrase_fullsearch × 2、phrase_related × 1、phrase_questions × 1）| 2026-07-06*  
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
