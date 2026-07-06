# Gemma 4（Google DeepMind）模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：ai.google.dev/gemma，Apache 2.0

## 模型理解（前置）

Gemma 4 是 Google DeepMind 于 2026 年 4 月发布的多模态开源模型家族，支持文本、图像、音频（E2B/E4B/12B）输入，生成文本输出。以"每参数智能"为核心设计目标，31B Dense 在 Arena AI 排行榜（发布时）位列开源模型 #3，26B MoE 位列 #6，凭借紧凑体积超越 20 倍参数量的闭源竞品。Gemma 系列历史下载量超 4 亿次，HuggingFace 有 100,000+ 社区变体；全系 Apache 2.0 许可证，商用完全无壁垒。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 多模态轻量开源 LLM 家族（文本/图像/音频），从边端手机到工作站全尺寸覆盖 |
| 许可证 | **Apache 2.0**，商用友好，无地区限制 |
| 主仓库 / 分发 | HuggingFace（`google/gemma-4-*`）、Ollama（`ollama run gemma4`）、Kaggle；GGUF/vLLM/SGLang/LM Studio 均支持 |
| 参数 / VRAM 可跑性 | E2B（2.3B有效）5.7GB（8-bit）→ 8GB VRAM 可跑；E4B（4.5B）8.9GB；12B 13.4GB（8-bit）→ 16GB 消费 GPU；26B MoE 14.4GB（4-bit）→ 16GB GPU；31B Dense 17.5GB（4-bit）→ **Olares One（RTX 5090 Mobile 24GB）全系覆盖** |
| 变体 / 型号 | E2B（手机/边端）、E4B（高端笔记本）、12B Unified（音视频统一编码器）、26B MoE（4B 活跃参数）、31B Dense |
| 闭源对标 | **Gemini Nano / Flash**（Google 付费 API 轻量模型）；**GPT-4o mini**（OpenAI 付费 API）|
| Olares Market | Ollama 已在 Olares Market → `ollama run gemma4` 即可本地跑 Gemma 4；vLLM / SGLang 亦可部署 |
| 来源 | [ai.google.dev/gemma/docs/core](https://ai.google.dev/gemma/docs/core)、[blog.google/gemma-4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)、[HuggingFace google/gemma-4-31B](https://huggingface.co/google/gemma-4-31B)、[Ollama library/gemma4](https://ollama.com/library/gemma4) |

---

## 流量基线（Phase 1）

> ai.google.dev/gemma/ 是 Google 开发者平台子目录，Semrush 在 google.dev 域名级聚合数据。以下为 google.dev 全域名指标；Gemma 子目录贡献的流量通过 resource_organic 单独提取（见下方关键词表）。

| 指标 | 数据 |
|------|------|
| 域名 | google.dev（ai.google.dev/gemma/ 所在根域） |
| SEMrush Rank | 0（超出 Semrush 评分范围，属顶级域名） |
| 月自然流量（US） | 253,143（全域名） |
| 关键词数 | 52,805（全域名） |
| 流量估值 | $592,807/月（全域名） |

### Gemma 子目录 TOP 关键词（ai.google.dev/gemma/，按流量降序，resource_organic）

| 关键词 | 排名 | 月量 | KD | 流量 | URL |
|--------|------|------|----|------|-----|
| gemma | 2 | 27,100 | 81 | 596 | /gemma/docs |
| gemma 4 | 5 | 12,100 | 64 | 423 | /gemma/docs/core |
| gemma 3n | 1 | 1,900 | 53 | 250 | /gemma/docs/gemma-3n |
| gemma ai | 3 | 4,400 | 88 | 193 | /gemma/docs |
| gemma 4 ai | 2 | 2,900 | 54 | 127 | /gemma/docs/core |
| gemma 4 google ai model | 1 | 390 | 0 | 96 | /gemma/docs/core |
| paligemma | 1 | 720 | 45 | 95 | /gemma/docs/paligemma |
| gemma models | 2 | 1,000 | 82 | 82 | /gemma/docs |
| gemma 4 models | 1 | 590 | 52 | 77 | /gemma/docs/core |
| llama.cpp | 11 | 9,900 | 50 | 49 | /gemma/docs/integrations/llamacpp |
| gemma 3 | 6 | 2,400 | 69 | 45 | /gemma/docs/get_started |
| gemma 4 benchmarks | 1 | 320 | 37 | 42 | /gemma/docs/core/model_card_4 |
| gemma 4 api | 2 | 320 | 36 | 42 | /gemma/docs/core/gemma_on_gemini_api |

> **数据说明**：resource_organic 显示 "gemma 4" 月量 12,100（KD 64，官网 pos 5）；phrase_these 批量查询同一词返回 590（KD 24）。两组来自 Semrush 不同报告（resource_organic 含语义宽匹配，phrase_these 为精确词）。Phase 2 关键词扩展以 phrase_these 实际调用值为准，并在 Top 词表中注明。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| gemma 3 | 2,900 | 83 | $4.73 | I |
| gemma4 | 2,400 | 57 | $4.70 | I |
| gemma 3n | 1,900 | 63 | $2.42 | I |
| gemma models | 720 | 72 | $2.86 | I |
| gemma 2 | 720 | 74 | $4.14 | I |
| gemma 4 models | 590 | 52 | $6.24 | I |
| gemma 3 27b ⭐ | 590 | 44 | $0 | I |
| gemma-3-12b ⭐ | 590 | 42 | $0 | I |
| gemma 4 ⭐ | 590* | 24 | $0 | I |

> *phrase_these 显示 590，KD 24；resource_organic 显示实际月量约 12,100，KD 64（新品词搜索量正在积累，详见 Phase 1 注）。

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| ollama gemma 4 ⭐ | 1,300 | 0 | $9.95 | I |
| gemma 4 ollama ⭐ | 480 | 0 | $8.59 | I |
| ollama gemma ⭐ | 260 | 38 | $0 | I,N |
| ollama gemma 3 ⭐ | 260 | 37 | $0 | I |
| gemma 3 ollama ⭐ | 170 | 39 | $0 | I |
| gemma ollama ⭐ | 140 | 45 | $0 | I,C |
| gemma 3n ollama | 140 | 59 | $0 | I,C |
| gemma-4 ollama ⭐ | 110 | 0 | $8.59 | I |
| gemma vllm ⭐ | 20 | 0 | $0 | I |
| gemma sglang ⭐ | 20 | 0 | $0 | I |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| local llm ⭐ | 2,900 | 39 | $5.37 | I |
| run llm locally | 590 | 47 | $3.50 | I |
| self hosted llm ⭐ | 320 | 22 | $3.12 | I |
| how to run gemma locally ⭐ | 40 | 0 | $0 | I |
| gemma local ⭐ | 30 | 0 | $0 | I |
| how to run gemma 4 locally ⭐ | 30 | 0 | $3.30 | I |
| running gemma locally ⭐ | 30 | 0 | $0 | I |
| run gemma locally ⭐ | 20 | 0 | $0 | I |
| run gemma 4 locally ⭐ | 20 | 0 | $0 | I |
| gemma gguf ⭐ | 20 | 0 | $0 | I |
| gemma install ⭐ | 20 | 0 | $0 | I |
| gemma vram ⭐ | 20 | 0 | $0 | I |
| gemma quantization ⭐ | 20 | 0 | $0 | I |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| best open source llm ⭐ | 1,000 | 21 | $3.69 | I |
| gemma vs llama ⭐ | 90 | 15 | $0 | I |
| gemma api | 90 | 56 | $4.65 | T |
| gemma vs llama 3 ⭐ | 20 | 0 | $0 | I |
| gemma vs mistral ⭐ | 20 | 0 | $0 | I |
| gemma vs gpt ⭐ | 20 | 0 | $0 | I |
| gemma alternative ⭐ | 10 | 0 | $0 | I |
| open source gemini alternative ⭐ | 10 | 0 | $0 | I |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | 契合度 | Olares 角度 |
|--------|------|-----|-----|--------|------------|
| ollama gemma 4 | 1,300 | 0 | $9.95 | ⭐⭐⭐ | Olares Market 一键装 Ollama → `ollama run gemma4`，零配置本地跑多模态 LLM；KD=0 最高优先 |
| gemma 4 ollama | 480 | 0 | $8.59 | ⭐⭐⭐ | 同上；CPC=$8.59 证明有真实商业需求，Olares = 最简路径，主打"一次点击，永久本地" |
| self hosted llm | 320 | 22 | $3.12 | ⭐⭐⭐ | Olares 平台天然定位，Gemma 4 Apache 2.0 是自托管 LLM 的最强开源选手之一 |
| how to run gemma locally | 40 | 0 | $0 | ⭐⭐⭐ | 纯部署意图，KD=0；Olares + Ollama = 最简本地 Gemma 方案，step-by-step 教程入口 |
| run gemma 4 locally | 20 | 0 | $0 | ⭐⭐⭐ | 明确针对 Gemma 4，GEO 抢发候选；Olares One 24GB 可无压力运行全系型号 |
| best open source llm | 1,000 | 21 | $3.69 | ⭐⭐ | Gemma 4 31B 当前 Arena #3 开源模型；Olares 平台推荐旗舰 LLM，写综述文带 Olares 跑法 |
| local llm | 2,900 | 39 | $5.37 | ⭐⭐ | 平台级大盘词；Olares 作为本地 LLM 运行环境，Gemma 4 作为推荐首选多模态模型 |
| gemma vs llama | 90 | 15 | $0 | ⭐⭐ | 对比意图，KD=15；Olares 同时支持 Gemma 4 和 Llama 4（均通过 Ollama），对比文可两组受众兼顾 |
| gemma ollama | 140 | 45 | $0 | ⭐⭐ | 历史稳定词，引擎组合；Olares Market Ollama 是分发入口 |
| gemma vllm | 20 | 0 | $0 | ⭐⭐ | vLLM 在 Olares 亦可部署；教程中展示 Ollama + vLLM 双引擎选项 |
| open source gemini alternative | 10 | 0 | $0 | ⭐ | GEO 窗口词；Gemma 4 = Google 自己的 Gemini 平替，Olares 提供本地运行 |
| gemma alternative | 10 | 0 | $0 | ⭐ | 早期词，GEO 阶段；目标用户是想用 Gemini API 但需零成本/完全离线者 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|-----|-----|------|------|--------------------------|
| local llm | 2,900 | 39 | $5.37 | I | 主词候选 | KD 可进、量大；Olares 平台 + Gemma 4 双入口，适合"2026 最佳本地 LLM 完整指南"综述文 |
| best open source llm | 1,000 | 21 | $3.69 | I | 主词候选 | ⭐ KD 低、月量千级；Gemma 4 31B Arena #3，写"最佳开源 LLM"横评文，Olares 作为推荐运行平台 |
| gemma | 27,100 | 81 | $4.05 | I | 主词候选 | 品牌词流量大但 KD=81，Olares 不与官网正面竞争；可作聚合文章的信号词捎带 |
| gemma 4 | 590* | 24 | $0 | I | 主词候选 | ⭐ *KD 仅 24（phrase_these）；resource_organic 显示实际流量约 12,100 月量（pos 5）；新品词量在快速爬升，是写 Gemma 4 专题的核心词 |
| ollama gemma 4 | 1,300 | 0 | $9.95 | I | 次级 | ⭐⭐⭐ **最高优先 Olares 词**，KD=0+月量 1,300；Olares Market Ollama 教程的首选入口词 |
| gemma 4 ollama | 480 | 0 | $8.59 | I | 次级 | ⭐⭐⭐ KD=0，CPC=$8.59 证明商业价值；与 `ollama gemma 4` 共用一篇部署教程即可覆盖 |
| self hosted llm | 320 | 22 | $3.12 | I | 次级 | ⭐ Olares 平台定位词，Gemma 4 作为推荐模型，适合"自托管私有 LLM 完整指南" |
| run llm locally | 590 | 47 | $3.50 | I | 次级 | 量不错 KD=47，通用词；Gemma 4 E2B/E4B 最轻，适合消费级入门推荐 |
| gemma vs llama | 90 | 15 | $0 | I,0 | 次级 | ⭐ KD 极低，对比意图；Olares 同时支持两模型，写对比文兼顾两组受众 |
| ollama gemma | 260 | 38 | $0 | I,N | 次级 | 历史词稳定；作为引擎组合词系列的流量入口 |
| gemma ollama | 140 | 45 | $0 | I,C | 次级 | 历史词，引擎组合；可复用 Ollama 教程带流量 |
| how to run gemma locally | 40 | 0 | $0 | I | 次级 | ⭐ 部署意图词，KD=0；Olares + Ollama 是最简答案，step-by-step 教程标准词 |
| run gemma 4 locally | 20 | 0 | $0 | I | GEO | ⭐ KD=0，明确 Gemma 4 部署意图；GEO 抢发，Olares One 全系支持的最强论据 |
| gemma alternative | 10 | 0 | $0 | I | GEO | 早期词，GEO 窗口开放；目标用户是想替换 Gemini API 且需完全离线/自部署者 |
| open source gemini alternative | 10 | 0 | $0 | I | GEO | ⭐ 攻击面词，Gemma 4 = Google 自己的 Gemini 开源平替；Olares 本地运行加持 |
| gemma vs gpt | 20 | 0 | $0 | I | GEO | Gemma 4 Apache 2.0 vs GPT 付费 API，GEO 候选；主打"零 API 成本+完全离线" |
| gemma vllm | 20 | 0 | $0 | I | GEO | 引擎组合词，GEO 候选；Olares 可部署 vLLM 跑 Gemma 4 |
| gemma gguf | 20 | 0 | $0 | I | GEO | 量化词，KD=0；帮用户选合适量化版本（E4B GGUF 在 Ollama 默认拉取） |
| gemma 4 vs llama 4 | 10 | 0 | $0 | I | GEO | 新一代对比词，GEO 抢发窗口最宽；两者均可在 Olares 通过 Ollama 跑 |

---

## 核心洞见

1. **搜索心智已初步建立，「gemma 4」词量在快速积累**：品牌词 "gemma" 月量 27,100（KD 81），说明 Gemma 系列整体认知良好。"gemma 4" 的 phrase_these 显示 590（KD 24），而 resource_organic 实际带量约 12,100（pos 5）——差异反映新品词搜索量尚在爬升、Semrush 精确词库更新滞后于 SERP 实际流量。**KD=24 是极低难度，内容机会窗口已打开**。

2. **Olares One 全系可跑，叙事成立**：Gemma 4 VRAM 梯队（E2B 5.7GB → 12B 13.4GB → 31B 17.5GB 4-bit）全部在 Olares One（RTX 5090 Mobile 24GB GDDR7）覆盖范围内；消费级 16GB GPU 也能流畅跑到 12B（8-bit）或 26B MoE（4-bit）；E2B 甚至纯 CPU 可跑。Gemma 4 是当前消费硬件上 VRAM 门槛最低的高性能开源多模态 LLM 之一。**本地部署叙事完全成立**。

3. **Apache 2.0 = 主推优势**：无地区限制、无商用壁垒，可直接作为"免费开源 Gemini/GPT 替代"叙事核心。攻击面：Gemini Flash/Nano 按 token 计费 vs Gemma 4 零成本本地推理；云端数据上传 vs 完全离线隐私；API 额度限制 vs 无限本地调用。

4. **对 Olares 最关键的 3 个词**：
   - `ollama gemma 4`（1,300 量，KD 0）— **首选**，Olares Market Ollama 部署教程的最高优先入口词
   - `gemma 4 ollama`（480 量，KD 0，CPC $8.59）— 并列首位，高 CPC 验证真实工具需求
   - `best open source llm`（1,000 量，KD 21）— 平台级词，Gemma 4 作为 Olares 推荐旗舰 LLM，适合横评综述

5. **GEO 抢发窗口显著**：`gemma alternative`、`run gemma 4 locally`、`open source gemini alternative`、`gemma 4 vs llama 4`、`gemma vs gpt` 等词当前月量 10-30、KD=0——Gemma 4 发布于 2026 年 4 月，搜索词正在形成但尚无强内容占位。这是 AI Overview / Perplexity 引用位的黄金抢发期，结合 Olares 本地部署视角写教程/对比文可快速抢占。

6. **闭源对标与攻击面**：
   - **Gemini Flash / Nano**：同出自 Google DeepMind，但付费 API；攻击点 = Gemma 4 同出身开源版，Apache 2.0 可完全离线、数据不出机。"open source gemini alternative" KD=0 可直接抢。
   - **GPT-4o mini**：OpenAI 付费 API；攻击点 = $0 边际成本 vs 按量计费、本地延迟 < 云端 RTT、无速率限制。"gemma vs gpt" KD=0 GEO 候选。

7. **与同章其他报告关联**：Gemma 4 归入 `01-llm` 章，与 Llama 4、Qwen 3、DeepSeek V4 形成"主流开源 LLM"矩阵。Ollama 路径已是跨所有 LLM 的通用门户（Ollama 在 Olares Market 已上架），教程内容共用引擎组合词簇——`ollama gemma 4`、`ollama llama 4`、`ollama qwen 3` 可统一在"Olares + Ollama 本地 AI 平台"专题下分发，互相带流量。Gemma 4 Ollama 已超 1,250 万次下载，社区基础极强。

---

*数据来源：SEMrush US（domain_rank、resource_organic、phrase_this、phrase_these、phrase_related、phrase_fullsearch）| 2026-07-06*  
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
