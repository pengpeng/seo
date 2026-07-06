# Tencent Hy-MT2 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：Tencent Hunyuan Team / github.com/Tencent-Hunyuan/Hy-MT2，许可证见下
>
> **无独立官网**——SEO 主战场在第三方内容/文档页（HuggingFace、GitHub、arxiv、技术博客）；跳过 Phase 1 域名报告，直接从关键词层面做起。

---

## 模型理解（前置）

Hy-MT2 是腾讯 Hunyuan 团队于 2026 年 5 月发布的"快思考"多语言机器翻译模型家族，涵盖 1.8B / 7B / 30B-A3B（MoE）三个尺寸，支持 33 种语言互译并可有效遵从多语言翻译指令。1.8B 款通过自研 AngelSlim 1.25-bit 极限量化可压缩至 440 MB 存储，适合设备端（on-device）场景；7B 及 30B-A3B 模型在快思考模式下据官方测评超越 DeepSeek-V4-Pro、Kimi K2.6 等开源模型，1.8B 整体表现也超过 Microsoft Translator 和 Doubao 商业 API。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 多语言机器翻译（33 语种）+ 指令跟随 + 快思考，面向复杂真实场景 |
| 许可证 | **混合/过渡中**：1.8B 已确认为 Apache License 2.0；7B/30B GitHub 仓库最新提交（c30b36c，"renew license"）改为 Apache 2.0，但 HuggingFace 30B-A3B 页面仍显示 Tencent HY Community License（含"本协议不适用于欧盟"地区限制、100M MAU 商业阈值条款）。**实际部署前须以 HuggingFace model card LICENSE.txt 为准**；当前最稳妥判断：1.8B 商用友好，30B 存在合规不确定性。 |
| 主仓库 / 分发 | GitHub [Tencent-Hunyuan/Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2)（~477★）；HuggingFace `tencent/Hy-MT2-{1.8B,7B,30B-A3B}`；ModelScope 同步；GGUF 变体（llama.cpp）和 FP8 变体均有发布 |
| 参数 / VRAM 可跑性 | 1.8B FP8: ~1GB VRAM / AngelSlim 1.25-bit: 440MB 存储（CPU 可跑）；7B FP8: ~4GB VRAM（8GB 消费显卡可跑）；30B-A3B MoE 激活参数 3B，FP8 约 ~4-6GB VRAM（8GB 卡可跑）。**Olares One（NVIDIA GPU）全部可运行**，1.8B 甚至纯 CPU 可跑。 |
| 变体 / 型号 | Hy-MT2-1.8B、Hy-MT2-1.8B-FP8、Hy-MT2-1.8B-GGUF（1.25-bit AngelSlim）；Hy-MT2-7B、Hy-MT2-7B-FP8、Hy-MT2-7B-GGUF；Hy-MT2-30B-A3B、Hy-MT2-30B-A3B-FP8 |
| 闭源对标 | **DeepL**（主要对标，付费 API 订阅制）、**Microsoft Translator**（Azure 按量计费）、**Doubao 翻译**（字节系商业 API）；官方论文自称 1.8B 综合超越 Microsoft 与 Doubao，7B/30B 超越 DeepSeek-V4-Pro/Kimi K2.6 |
| Olares Market | 未上架。翻译模型可通过 llama.cpp（GGUF）或 vLLM（FP8）以自定义方式部署；Ollama 暂无官方支持，GGUF 可手动 `ollama create` |
| 来源 | [HuggingFace model card](https://huggingface.co/tencent/Hy-MT2-1.8B)；[GitHub README](https://github.com/Tencent-Hunyuan/Hy-MT2)；[arxiv 2605.22064](https://arxiv.org/abs/2605.22064)；[LICENSE.txt (1.8B)](https://huggingface.co/tencent/Hy-MT2-1.8B/blob/main/LICENSE.txt)；[LICENSE.txt (30B)](https://huggingface.co/tencent/Hy-MT2-30B-A3B/blob/main/LICENSE.txt) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| tencent hunyuan | 1,300 | 50 | $0.85 | I |
| tencent hunyuan video | 170 | 50 | $1.00 | I |
| tencent ai model | 70 | 62 | $0 | I |
| hunyuan model | 50 | 70 | $0 | I |
| hunyuan mt | 20 | 48 | $0 | I |
| hunyuan llm | 20 | 0 | $0 | — |
| tencent open source | 20 | 0 | $0 | I |
| hy-mt2（及所有具体型号词） | 0 | — | — | 新模型，尚无搜索量 |

*注：hy-mt2、hy mt2、hunyuan mt2、hy-mt2 1.8b/7b/30b 等品牌专有词在 Semrush US 均无可测量搜索量，属典型新模型 GEO 前哨状态。*

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ollama translation ⭐ | 20 | 0 | $0 | I |
| local llm translation ⭐ | 20 | 0 | $0 | I |
| translation llm | 10 | 0 | $6.10 | I |

*注：无 ComfyUI 适配（翻译模型，非图像生成）；vLLM 部署走通用 LLM 关键词覆盖。*

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| offline translator | 320 | 32 | $0.60 | C |
| translate without internet ⭐ | 50 | 31 | $1.01 | I |
| libretranslate api | 50 | 50 | $3.37 | I |
| on-device translation ⭐ | 20 | 0 | $0 | I |
| offline translation api ⭐ | 20 | 0 | $0 | I |
| self hosted translation ⭐（通配） | <10 | — | — | — |
| gdpr translation ⭐ | 20 | 0 | $0 | I |
| private translation ⭐ | 10 | 0 | $0 | I |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| deepl translate | 246,000 | 97 | $2.14 | C/I |
| deepl translator | 60,500 | 93 | $2.14 | C |
| microsoft translator | 40,500 | 65 | $0.96 | I/C |
| best online translator | 480 | 45 | $1.79 | C |
| deepl vs google translate ⭐ | 480 | 37 | $1.53 | I |
| neural machine translation | 480 | 49 | $3.00 | I |
| google translate api | 1,600 | 54 | $7.70 | I/C |
| deepl api | 880 | 57 | $4.72 | I/C |
| lingvanex | 590 | 59 | $1.07 | C |
| libre translate ⭐ | 260 | 23 | $3.71 | C |
| argos translate ⭐ | 260 | 40 | $6.35 | I |
| ctranslate2 ⭐ | 260 | 30 | $0 | I |
| best deepl alternatives ⭐ | 720 | 12 | $0 | C |
| deepl alternative ⭐ | 110 | 17 | $2.13 | C |
| google translate alternative ⭐ | 210 | 20 | $1.52 | C |
| translation api free ⭐ | 70 | 26 | $5.40 | I/C |
| best translation api ⭐ | 40 | 24 | $5.80 | C |
| machine translation api | 40 | 33 | $0 | I |
| deepl open source ⭐ | 20 | 0 | $0 | I |
| free deepl alternative ⭐ | 20 | 0 | $0 | C |
| yandex translate api ⭐ | 70 | 27 | $0 | I |
| open source machine translation ⭐ | 20 | 0 | $0 | I |
| deepl vs microsoft translator ⭐ | 20 | 0 | $0 | I |
| nllb model ⭐ | 20 | 0 | $0 | I |
| multilingual translation model ⭐ | 20 | 0 | $0 | I |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| best deepl alternatives | 720 | 12 | $0 | 开源可自部署 + 无 API 限额，Hy-MT2-1.8B（Apache 2.0）是最轻量的本地 DeepL 替代方案 | ⭐⭐⭐ |
| deepl alternative | 110 | 17 | $2.13 | 同上；KD 极低、有商业意图，适合以 Olares One 跑 1.8B 或 7B 的场景文 | ⭐⭐⭐ |
| offline translator | 320 | 32 | $0.60 | Olares 本地部署场景：翻译请求不出设备，GDPR/数据主权友好 | ⭐⭐⭐ |
| translate without internet | 50 | 31 | $1.01 | 同上；长尾但精准，表达离线翻译需求 | ⭐⭐⭐ |
| google translate alternative | 210 | 20 | $1.52 | 内容桥梁：从免费替代 Google Translate 引流至自托管方案 | ⭐⭐ |
| libre translate | 260 | 23 | $3.71 | 当前自托管翻译最热词，Hy-MT2 质量远超 LibreTranslate，可做 comparison 文 | ⭐⭐⭐ |
| ctranslate2 | 260 | 30 | $0 | CTranslate2 是 LibreTranslate/ArgosTranslate 底层引擎，技术用户搜索；可对比 Hy-MT2 GGUF 推理性能 | ⭐⭐ |
| argos translate | 260 | 40 | $6.35 | 同类开源竞品，Hy-MT2 质量更强；可做对比/替代文章 | ⭐⭐ |
| ollama translation | 20 | 0 | $0 | GEO 前哨：Hy-MT2 GGUF 可手动导入 Ollama，Olares Market 可做一键引擎 | ⭐⭐ |
| gdpr translation | 20 | 0 | $0 | 合规场景：本地跑翻译模型 = 数据不出设备，天然 GDPR 友好 | ⭐⭐⭐ |
| on-device translation | 20 | 0 | $0 | 1.8B AngelSlim 440MB = 设备端可跑，Olares One 部署成本极低 | ⭐⭐ |
| translation api free | 70 | 26 | $5.40 | 自托管后 = 无限量免费调用，面向个人/小团队高机会词 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| best deepl alternatives | 720 | 12 | $0 | C | **主词候选** | KD 最低、意图最准的高价值词；可写"Best DeepL Alternatives 2026（含自托管 Hy-MT2）"，Olares One 一键部署叙事，吸引付费 DeepL 用户流失流量 |
| deepl alternative | 110 | 17 | $2.13 | C | **主词候选** | KD 17 对比词，可与 best deepl alternatives 合并进同一篇文章的次级词 |
| google translate alternative | 210 | 20 | $1.52 | C | **主词候选** | 大众替代需求入口；内容中引出"还有更私密的选择——本地跑 Hy-MT2" |
| libre translate | 260 | 23 | $3.71 | C | **主词候选** | 自托管翻译第一大词；Hy-MT2 vs LibreTranslate 对比文主词，质量 + 隐私双维度 |
| offline translator | 320 | 32 | $0.60 | C | **主词候选** | 离线翻译流量稳定；可写 Olares 本地翻译场景文 |
| ctranslate2 | 260 | 30 | $0 | I | **次级** | 技术用户搜索；适合作为 Hy-MT2 本地部署技术文的锚点（CTranslate2 为 baseline 对比） |
| argos translate | 260 | 40 | $6.35 | I | **次级** | 另一主流开源对比；KD 40 略高但可作为 alternatives roundup 中的比较维度 |
| deepl vs google translate | 480 | 37 | $1.53 | I | **次级** | 高意图对比词；可在文末引出"若想完全不依赖云端，还有 Hy-MT2 本地方案" |
| translation api free | 70 | 26 | $5.40 | I/C | **次级** | 商业意图强（CPC $5.40）；自托管后无限量 = 直接回答"free translation api"，适合技术教程文 |
| tencent hunyuan | 1,300 | 50 | $0.85 | I | **次级** | 品牌词流量存在但 KD 高；用于旗下产品介绍文的品牌关联锚点 |
| ollama translation | 20 | 0 | $0 | I | **GEO** | 搜索量极低，但 GGUF+Ollama 组合技术真实存在；抢 AI Overview 引用 |
| gdpr translation | 20 | 0 | $0 | I | **GEO** | 企业合规场景，意图精准；本地翻译 GDPR 叙事的语义锚 |
| on-device translation | 20 | 0 | $0 | I | **GEO** | 随移动 AI 普及可能爆发；1.8B 440MB 是最强有力的回答案例 |
| hy-mt2（所有型号词） | 0 | — | — | — | **GEO** | 模型刚发布，搜索量待积累；率先发布教程 + HuggingFace spaces 内容，抢 GEO 首位 |
| deepl open source | 20 | 0 | $0 | I | **GEO** | 直接的需求表达："DeepL 有没有开源版"；Hy-MT2 就是最准确的答案 |
| multilingual translation model | 20 | 0 | $0 | I | **GEO** | 技术综述类搜索；Hy-MT2 是 2026 最新最小的 33-语言开源模型 |

---

## 核心洞见

1. **搜索心智尚未建立（GEO 抢发窗口）**
   Hy-MT2 于 2026 年 5 月发布，所有品牌/型号专有词（hy-mt2、hunyuan mt2、hy-mt2 7b 等）在 Semrush US 均无可测量搜索量。"hunyuan mt" 仅 20/月，"tencent hunyuan" 1,300/月（混合多个 Hunyuan 产品）。搜索心智完全未建立，是典型的 GEO 抢发窗口——率先覆盖的内容将在 AI Overview / Perplexity 结果中获得早期权重优势。

2. **消费级 GPU / Olares One 完全可跑（叙事前提成立）**
   - 1.8B AngelSlim 1.25-bit：440MB 存储，CPU 可运行，Olares One 零负担
   - 7B FP8：~4GB VRAM，8GB 消费显卡即可
   - 30B-A3B MoE（激活 3B）：FP8 约 4-6GB VRAM，消费 GPU 可接受
   三档尺寸全部可在 Olares One 硬件规格范围内运行，"本地私有翻译"叙事技术上完全成立。

3. **许可证混合，需区分尺寸主推**
   1.8B 已确认 Apache 2.0，可作商用友好主推；7B/30B 的 HuggingFace 页面 LICENSE.txt 存在与 GitHub 最新提交不一致的情况——30B HF 页面仍含地区限制（"不适用于欧盟"）和 100M MAU 商业阈值。内容层面建议：**主推 1.8B（Apache 2.0，安全无争议）**，7B/30B 作为性能对比维度，企业自托管场景加注"核查最新 LICENSE"免责说明。

4. **对 Olares 最关键的 2-3 个词**
   - **`best deepl alternatives`**（720/月，KD 12）：付费用户流失流量最集中的词，KD 极低，最大写作机会
   - **`libre translate`**（260/月，KD 23）：自托管翻译第一大词，Hy-MT2 质量远超 LibreTranslate，Olares 本地部署 vs LibreTranslate 是天然的对比文切入点
   - **`offline translator`**（320/月，KD 32）：隐私/离线场景主词，与 Olares 数据主权叙事完全契合

5. **GEO 抢发窗口：模型专有词全部是 GEO 候选**
   hy-mt2、hy-mt2 1.8b、hy-mt2 gguf、hunyuan translation model 等词目前搜索量为零，但模型已有 arxiv 论文（引用量增长中）、GitHub 477★，社区关注已在上升。率先在 dev.to、Hacker News、Reddit r/LocalLLaMA 发布"How to run Hy-MT2 locally"教程，可抢占 Perplexity/ChatGPT Search 直接引用位。

6. **闭源对标与攻击面**
   - **DeepL**（主攻）：Pro 计划 $25-30/月，API 按字符计费（$5.49/100 万字符），月度额度限制严格；本地部署 Hy-MT2 = 无限次、无额度、数据不出设备
   - **Microsoft Translator**：Azure 认知服务按量计费，企业预算高；对标词 `microsoft translator api`（90/月）尚有机会
   - **Doubao 翻译**：字节 API，国内向，海外开发者认知弱——对 Hy-MT2 的国际内容来说可忽略
   - 攻击面：月度 API 费用 + 额度墙 + 数据隐私（云端处理），三个维度 Olares 本地部署均有优势

7. **与同类 family 关联**
   在 `model/models.md` 09-translation 章，Hy-MT2 是目前唯一覆盖的专用翻译模型 family。关联词与 `model/keywords.md` 可参考：`self-hosted AI`、`local LLM`（跨报告主词），翻译赛道特有机会词（`deepl alternative`、`libre translate`、`offline translator`）应作为本报告的独立主词候选登记。

---

*数据来源：SEMrush US（phrase_these × 5、phrase_related × 2、phrase_fullsearch × 1、phrase_questions × 1）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
