# Qwen3 / Qwen3.6 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：Qwen Team / Alibaba（qwen.ai），Apache 2.0

## 模型理解（前置）

Qwen3 系列是阿里巴巴 Qwen 团队出品的旗舰开源 LLM family，覆盖 0.6B–235B 参数的密集与 MoE 模型，支持"思考模式（Thinking）"与"非思考模式"无缝切换。2026 年 4 月发布的 **Qwen3.6** 是该系列最新演进，聚焦 Agentic Coding 与长上下文，旗舰型号 Qwen3.6-27B 以 27B 密集参数在 SWE-bench 等 Coding 基准上超越百亿级 MoE 竞品，全系 Apache 2.0。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 阿里 Qwen 团队出品的开源通用 LLM family，密集 + MoE 双线，内置 Thinking 模式，最新子代 Qwen3.6 主打 Agentic Coding |
| 许可证 | **Apache 2.0**（含 Qwen3.6-27B / 35B-A3B；Qwen3 原版全系列；Qwen3.5 ≤32B）；Qwen3.5 72B+ 改用 Qwen Community License — 商用红线在 3.5 大参数档，3.6 两款开源模型当前均 Apache 2.0 |
| 主仓库 / 分发 | GitHub [`QwenLM/Qwen3.6`](https://github.com/QwenLM/Qwen3.6) ★持续增长；HuggingFace `Qwen/Qwen3.6-27B`；Ollama `ollama run qwen3:8b`；ModelScope 同步 |
| 参数 / VRAM 可跑性 | Qwen3 原版：8B → Q4 ~5-6GB（RTX 3060 12GB 可跑）；14B → ~9-10GB；30B-A3B(MoE) → ~18-20GB；32B → ~20GB；235B-A22B → ~132GB（需多卡）。Qwen3.6-27B dense → ~18GB Q4。**Olares One（RTX 5090 Mobile 24GB）可流畅跑 Qwen3-14B / 30B-A3B / 32B / Qwen3.6-27B，以 30B-A3B MoE 为最优性价比** |
| 变体 / 型号 | Qwen3：0.6B / 1.7B / 4B / **8B** / **14B** / 32B（密集）+ **30B-A3B** / **235B-A22B**（MoE）；Qwen3-2507（7月更新）；Qwen3.6：**27B**（密集）+ **35B-A3B**（MoE）；Qwen3-VL / Qwen3-Coder（专项变体）|
| 闭源对标 | **GPT-4o**（OpenAI）、**Claude 3.5 / 4.5 Sonnet**（Anthropic）、**Gemini 2.5 Pro**（Google）；Coding 场景直接对标 Claude 4.5 Opus（Qwen3.6-27B SWE-bench 超越之）|
| Olares Market | ✅ Ollama（一键部署，`qwen3:8b` / `qwen3:30b-a3b` 等直接拉）、Open WebUI、AnythingLLM 均已上架；vLLM 可手动部署 |
| 来源 | [GitHub QwenLM/Qwen3.6](https://github.com/QwenLM/Qwen3.6)；[qwen.ai](https://qwen.ai)；[HuggingFace Qwen3.6 collection](https://huggingface.co/collections/Qwen/qwen36)；[WillItRunAI VRAM guide](https://willitrunai.com/blog/qwen-3-gpu-requirements)；[InsiderLLM Qwen3 guide](https://insiderllm.com/guides/qwen3-complete-guide/) |

---

## 流量基线（Phase 1）

> 官方有独立站 `qwen.ai`（新）与 `qwenlm.github.io`（早期 GitHub Pages）两个落点，均做了查验。

| 指标 | qwen.ai（主站） | qwenlm.github.io（早期站） |
|------|---------------|--------------------------|
| SEMrush Rank | 9,801 | 209,391 |
| 月自然流量（US） | **234,947** | 8,410 |
| 关键词数 | 7,038 | 2,542 |
| 流量估值 | $754,387/月 | $19,495/月 |
| 付费词 | 0 | 0 |

**注**：qwen.ai 流量高度集中在**品牌导航词**（qwen ai、qwen chat 等），这是 Qwen Chat 产品（云端 SaaS 竞品）带来的消费型流量，与"本地部署模型"人群有本质区别——开发者/部署人群主战场在 HuggingFace、Ollama 文档、GitHub 及第三方教程站。

### qwen.ai TOP 关键词（按流量降序）

| 关键词 | 排名 | 月量 | KD | 流量 | 意图 | URL |
|--------|------|------|----|----- |------|-----|
| qwen ai | 1 | 49,500 | 97 | 39,600 | 导航 | qwen.ai/ |
| qwen | 1 | 49,500 | 99 | 39,600 | 导航 | qwen.ai/ |
| qwen chat | 1 | 18,100 | 56 | 14,480 | 导航/交易 | chat.qwen.ai/ |
| qwen ia | 1 | 6,600 | 69 | 5,280 | 导航 | qwen.ai/ |
| qween ai | 1 | 6,600 | 93 | 5,280 | 导航 | qwen.ai/ |
| qwen.ai | 1 | 6,600 | 94 | 5,280 | 导航 | qwen.ai/ |
| qwenai | 1 | 5,400 | 66 | 4,320 | 导航 | qwen.ai/ |
| quen | 1 | 5,400 | 34 | 4,320 | 导航 | qwen.ai/ |
| qwen 2.5 | 1 | 4,400 | 56 | 3,520 | 信息 | qwen.ai/ |
| qwen3 | 1 | 12,100 | 64 | 3,000 | 信息 | qwen.ai/ |
| qwen 3 | 1 | 3,600 | 76 | 2,880 | 导航 | qwen.ai/ |
| qwen code | 1 | 3,600 | 50 | 2,880 | 信息 | qwen.ai/qwencode |
| qwen image edit | 1 | 3,600 | 62 | 2,880 | 信息 | qwen.ai/blog |
| qwen3-max | — | 3,600 | 39 | — | 信息 | qwen.ai/blog |
| qwen3 coder | — | 2,900 | 56 | — | 信息 | qwen.ai/qwencode |
| qwen3-vl | — | 2,900 | 54 | — | 信息 | qwen.ai/blog |
| qwen3-8b | — | 2,900 | 35 | — | 信息 | — |
| qwen3-32b | — | 2,400 | 39 | — | 信息 | — |
| qwen 3 uncensored | — | 4,400 | 24 | — | 信息 | — |

> 流量中 ~70% 来自 qwen/qwen ai/qwen chat 等品牌导航词，这是 SaaS 用户而非本地部署人群；但 `qwen3`（12,100 流量，qwen.ai 排名 #1）显示品牌已深度绑定模型名，有利于 Olares"官网旁位"内容的关联曝光。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| qwen3 | 14,800 | 64 | $0 | 信息 |
| qwen 3 | 5,400 | 68 | $0 | 导航 |
| qwen3.5 | 5,400 | 52 | $4.56 | 信息 |
| qwen 3.5 | 3,600 | 64 | $4.31 | 信息/导航 |
| qwen3-max | 3,600 | 39 | $2.38 | 信息 |
| qwen 3 uncensored | 4,400 | 24 | $0 | 信息 ⭐ |
| qwen3-8b | 2,900 | 35 | $7.86 | 信息 ⭐ |
| qwen3-coder | 2,900 | 52 | $5.57 | 信息 |
| qwen3-vl | 2,900 | 54 | $4.86 | 信息 |
| qwen3 coder | 2,900 | 56 | $5.57 | 信息 |
| qwen3-32b | 2,400 | 39 | $9.77 | 信息 ⭐ |
| qwen3 8b | 1,000 | 48 | $5.85 | 信息 |
| qwen3 32b | 1,300 | 22 | $9.77 | 信息 ⭐ |
| qwen3 thinking | 140 | 67 | $0 | 信息 |
| qwen3 30b-a3b | 140 | 32 | $4.80 | 信息 ⭐ |
| qwen3 api | 260 | 53 | $3.44 | 信息/交易 |
| qwen3 14b | 320 | 34 | $7.63 | 信息 ⭐ |
| qwen3 235b | 320 | 43 | $1.11 | 信息 |
| qwen3 30b | 260 | 41 | $1.95 | 信息 |
| qwen 3.6 | 140 | 46 | $5.85 | 信息 |
| qwen2.5 | 2,400 | 62 | $3.47 | 信息 |
| qwen3.6 | 40 | 0 | $4.95 | — ⭐（GEO新词）|
| qwen3 2507 | 70 | 28 | $0 | 信息 ⭐ |
| qwen3 context window | 90 | 48 | $0 | 信息 |
| qwen3 multimodal | 40 | 48 | $0 | 信息 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ollama models | 14,800 | 63 | $5.27 | 信息/交易（竞争大）|
| qwen3 ollama | 260 | 48 | $0 | 商业/交易 |
| qwen ollama | 170 | 50 | $0 | 商业/交易 |
| qwen3 vllm | 140 | 40 | $0 | 信息 |
| qwen 3 ollama | 90 | 37 | $0 | 商业/交易 ⭐ |
| qwen3 gguf | 140 | 26 | $0 | 信息 ⭐ |
| qwen3 sglang | 20 | 0 | $7.27 | 信息 ⭐（GEO）|
| qwen3 comfyui | — | — | — | — |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| run llm locally | 590 | 47 | $3.50 | 信息 |
| local ai model | 260 | 41 | $2.93 | 信息 |
| qwen3 local | 20 | 0 | $0 | 信息 ⭐（GEO）|
| run qwen3 locally | 20 | 0 | $0 | 信息 ⭐（GEO）|
| qwen3 fp8 | 20 | 0 | $0 | 信息 ⭐（GEO）|
| qwen3 install | 30 | 0 | $0 | 信息 ⭐（GEO）|
| qwen3 gguf | 140 | 26 | $0 | 信息 ⭐ |
| how to run qwen3 locally | 20 | 0 | $0 | 信息 ⭐（GEO）|
| how to run qwen3 coder locally | 20 | 0 | $0 | 信息 ⭐（GEO）|

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| best open source llm | 1,000 | 21 | $3.69 | 信息 ⭐ |
| self hosted llm | 320 | 22 | $3.12 | 信息 ⭐ |
| best open source llm 2026 | 110 | 21 | $3.31 | 信息 ⭐ |
| open source chatgpt | 210 | 58 | $1.76 | 信息 |
| best local llm 2026 | 90 | 0 | $4.01 | 信息 ⭐（GEO）|
| qwen vs llama | 260 | 16 | $0 | 信息 ⭐ |
| qwen vs deepseek | 210 | 7 | $0 | 信息 ⭐ |
| run llm locally | 590 | 47 | $3.50 | 信息 |
| qwen vs claude | 40 | 10 | $0 | 信息 ⭐ |
| qwen vs gpt | 40 | 0 | $0 | 信息 ⭐（GEO）|
| qwen alternative | 10 | 0 | $8.10 | 商业 ⭐（GEO）|
| qwen3 alternative | — | — | — | — |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | 契合度 | Olares 角度 |
|--------|------|----|----|--------|-------------|
| qwen3 ollama | 260 | 48 | $0 | ⭐⭐⭐ | Olares Market 已上架 Ollama，`ollama run qwen3:30b-a3b` 一键跑，最低摩擦路径 |
| qwen3 gguf | 140 | 26 | $0 | ⭐⭐⭐ | GGUF 量化是消费级本地跑的主流格式；Olares One 24GB 跑 Q4 版本无压力 |
| qwen3 32b | 1,300 | 22 | $9.77 | ⭐⭐⭐ | Olares One RTX 5090 Mobile 24GB 可流畅跑 32B Q4；最强消费级单卡大模型叙事 |
| qwen3 30b-a3b | 140 | 32 | $4.80 | ⭐⭐⭐ | 30B-A3B MoE ~18GB Q4，Olares One 最优性价比选择（更快推理、占同等 VRAM）|
| qwen 3 ollama | 90 | 37 | $0 | ⭐⭐⭐ | 同 qwen3 ollama，另一写法；Olares Market Ollama app 即插即用 |
| best open source llm | 1,000 | 21 | $3.69 | ⭐⭐⭐ | Qwen3 在主流 benchmark 领先；Olares = 最简单的本地跑框架，2026 年"最强开源 LLM"= Qwen3.6 |
| self hosted llm | 320 | 22 | $3.12 | ⭐⭐⭐ | Olares 核心叙事——数据不出门、本地推理；与 self-hosted LLM 人群完美重合 |
| run llm locally | 590 | 47 | $3.50 | ⭐⭐ | 流量可观但 KD 偏高；Olares 可作"最简一键方案"切入 |
| qwen vs deepseek | 210 | 7 | $0 | ⭐⭐ | KD 极低；两款模型都可在 Olares 本地跑，可做双推 |
| qwen vs llama | 260 | 16 | $0 | ⭐⭐ | 同上，Olares 作"两款都支持的本地平台"叙事 |
| best open source llm 2026 | 110 | 21 | $3.31 | ⭐⭐⭐ | 2026 年词，Olares + Qwen3.6 组合是最新时效内容 |
| best local llm 2026 | 90 | 0 | $4.01 | ⭐⭐⭐ | GEO 抢发窗口；零 KD 但具体时效关键词，AI Overview 占位机会 |
| run qwen3 locally | 20 | 0 | $0 | ⭐⭐⭐ | GEO；完全契合 Olares 一键本地跑叙事 |
| qwen3 install | 30 | 0 | $0 | ⭐⭐ | GEO；Olares Market 安装教程自然落地页 |
| qwen3 local | 20 | 0 | $0 | ⭐⭐⭐ | GEO；最直接的本地部署意图词 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| best open source llm | 1,000 | 21 | $3.69 | 信息 | **主词候选** | KD 低量合格；Qwen3.6-27B 是 2026 实力竞争者，Olares 作"最简跑法"切入 |
| qwen3 32b | 1,300 | 22 | $9.77 | 信息 | **主词候选** | 月量符合 + KD 低；Olares One 24GB 正好跑 Q4，硬件叙事最强 |
| self hosted llm | 320 | 22 | $3.12 | 信息 | **主词候选** | 与 Olares"个人云"定位深度契合；可写"Self-hosted LLM guide with Olares" |
| best open source llm 2026 | 110 | 21 | $3.31 | 信息 | **主词候选** | 时效词，KD 低；2026 版 Qwen3.6 是最新竞争力，Olares + Qwen3.6 双绑定 |
| qwen3 | 14,800 | 64 | $0 | 信息 | **主词候选**（难度高） | 月量最大，但 KD 64 竞争激烈；qwen.ai #1 已占；内容辅助流量可关联至部署教程 |
| qwen3 8b | 1,000 | 48 | $5.85 | 信息 | **主词候选** | 消费级主力尺寸；KD 接近阈值但量够；可写"run qwen3 8b on your own hardware" |
| qwen3-8b | 2,900 | 35 | $7.86 | 信息 | **主词候选** | 连字符写法量更大 + KD 更低；与 qwen3 8b 合并写一篇 |
| qwen vs llama | 260 | 16 | $0 | 信息 | **主词候选** | KD 极低；两款都可在 Olares 本地跑，做"vs + 本地跑"内容 |
| qwen vs deepseek | 210 | 7 | $0 | 信息 | **主词候选** | KD 最低！既有量又 0 竞争；两款 Olares Market 都支持，是今年最值得写的对比文 |
| qwen3 ollama | 260 | 48 | $0 | 商业 | **次级** | 引擎组合词；Olares Market Ollama 一键，自然落地页 |
| qwen3 gguf | 140 | 26 | $0 | 信息 | **次级** ⭐ | GGUF 是本地 llama.cpp 主格式；KD 低，Olares 可推"GGUF via Ollama" |
| qwen3 30b-a3b | 140 | 32 | $4.80 | 信息 | **次级** ⭐ | MoE 效率标志；Olares One 最优选型词 |
| qwen 3 ollama | 90 | 37 | $0 | 商业 | **次级** ⭐ | 同 qwen3 ollama，另一写法，KD 更低 |
| qwen3 vllm | 140 | 40 | $0 | 信息 | **次级** | 高吞吐生产部署；Olares 可推 vLLM 自部署 |
| run llm locally | 590 | 47 | $3.50 | 信息 | **次级** | 流量可观；Olares 作最简路径切入，但 KD 偏高 |
| qwen3 14b | 320 | 34 | $7.63 | 信息 | **次级** ⭐ | KD 低；14B Q4 ~10GB 是 RTX 3060 16GB 甜点尺寸 |
| qwen 3 uncensored | 4,400 | 24 | $0 | 信息 | **次级** ⭐ | 量超大 + KD 低，但内容敏感；本地跑 = 无需外部审查，可以技术角度做"local = 用户自决" |
| best local llm 2026 | 90 | 0 | $4.01 | 信息 | **GEO** | 零 KD 时效词，AI Overview / Perplexity 抢发；Olares + Qwen3.6 2026 年绑定内容 |
| run qwen3 locally | 20 | 0 | $0 | 信息 | **GEO** | 直接部署意图，零竞争；Olares 一键教程极致相关 |
| qwen3 local | 20 | 0 | $0 | 信息 | **GEO** | 同上，更短写法 |
| qwen3.6 | 40 | 0 | $4.95 | — | **GEO** | 新代际词，KD 为 0 且月量已 40（会快速增长）；现在写 = 占早期 AI 引用位 |
| qwen3 2507 | 70 | 28 | $0 | 信息 | **GEO** ⭐ | 7月更新版词，有搜索量 + KD 低；版本内容时效性强 |
| qwen vs gpt | 40 | 0 | $0 | 信息 | **GEO** | 零 KD；可在"开源 vs 闭源"叙事里拿 AI Overview 引用 |
| what is qwen3 | 110 | 0 | $0 | 信息 | **GEO** | 零 KD 入门词；FAQ 页 / 文章开头可覆盖 |
| how to run qwen3 locally | 20 | 0 | $0 | 信息 | **GEO** | 教程意图完全对应 Olares 操作指南 |
| qwen alternative | 10 | 0 | $8.10 | 商业 | **GEO** | CPC $8 意味着商业价值高；量还小但 GEO 抢占有价值 |

---

## 核心洞见

**1. 搜索心智：品牌已建立，但模型部署词仍属早期**

`qwen3` 月量 14,800（US），`qwen.ai` 全站月流 234,947——品牌认知度毋庸置疑，但流量主体是 SaaS 聊天用户（qwen ai、qwen chat 等导航词占 70%+），而非"本地部署/开发者"群体。**本地部署词（qwen3 ollama 260、run qwen3 locally 20）量仍小**，说明心智分裂：知道模型的人很多，但"在自己机器上跑"的搜索量尚未爆发——这正是 Olares 内容切入的最大窗口期。

**2. 消费级可跑性：Olares One 完美契合**

- Qwen3-8B（Q4 ~5-6GB）：RTX 3060 12GB 即可 → 入门 Olares 用户
- Qwen3-14B（Q4 ~9-10GB）：RTX 4070 16GB → Olares 典型配置
- **Qwen3-30B-A3B MoE（Q4 ~18-20GB）：Olares One（24GB）最优选——MoE 推理更快、性能超 32B 密集**
- Qwen3-32B（Q4 ~20GB）：Olares One 24GB 可跑
- **Qwen3.6-27B（Q4 ~18GB）：Olares One 24GB 可跑，2026 年最强开源 Coding 模型**
- Qwen3-235B-A22B：需多卡（企业场景），不是 Olares One 主推重点

叙事核心：**Olares One 24GB 是 2026 年消费级跑 Qwen3 最强单机**。

**3. 许可证：Apache 2.0 全系开绿灯**

Qwen3 原版全系 + Qwen3.6（27B / 35B-A3B）均为 **Apache 2.0**，无地区限制、无座位数限制、可商用、可再分发。这是最干净的开源许可——可以作为**主推卖点**，尤其对比"Qwen3.5 72B+ 改 Qwen Community License"的限制升级，Qwen3.6 在开源友好度上反而是卖点。

**4. 对 Olares 最关键的 3 个词**

① **`qwen3 ollama`**（260/mo, KD 48）：Olares Market 已有 Ollama，写"如何通过 Olares 一键部署 Qwen3"的完整教程，落地页最自然；
② **`best open source llm 2026`**（110/mo, KD 21 ⭐）或 **`best open source llm`**（1000/mo, KD 21 ⭐）：整合 Qwen3.6 + Olares 叙事的"年度最强开源 LLM + 最简本地跑法"内容，KD 低流量高，是最佳主词候选；
③ **`qwen vs deepseek`**（210/mo, KD 7 ⭐）：KD 最低的有量对比词，两款都在 Olares Market 可跑，可做"为什么 2026 年选本地 LLM + 哪款更适合你"的顶层内容，带出 Olares 平台。

**5. GEO 抢发窗口**

以下词是新模型/新时效词，当前近零 KD，AI Overview / Perplexity 引用位仍在争夺中，**现在写 = 成本最低的占位机会**：

- `qwen3.6`（40/mo, KD 0）：新一代模型词，量会随知名度快速增长
- `best local llm 2026`（90/mo, KD 0）：时效年份词，现在没竞争
- `run qwen3 locally`（20/mo, KD 0）：部署教程，直接 Olares 使用场景
- `qwen3 2507`（70/mo, KD 28）：7月更新版词，有量低 KD
- `qwen vs gpt`（40/mo, KD 0）：开源 vs 闭源核心对比词
- `qwen alternative`（10/mo, CPC $8.10, KD 0）：商业意图词，现在几乎无竞争

**6. 闭源对标与攻击面**

| 闭源对标 | 攻击面 |
|----------|--------|
| **GPT-4o**（$0.005/1K input tokens）| 按量计费、数据上云、API 额度限制；Qwen3.6-27B Apache 2.0 本地跑 = 零成本推理、数据不出 |
| **Claude 4.5 Sonnet/Opus** | Anthropic 定价 $3-15/1M tokens；Qwen3.6-27B SWE-bench 已超 Claude 4.5 Opus on coding；本地 = 无 rate limit |
| **Gemini 2.5 Pro** | Google 云端专属、数据进 Google；Qwen3 = 本地隐私 + 不受账号封号风险 |
| 所有云端服务 | 速率限制 / 价格涨幅不可预期；Olares = 一次买硬件 + 终身免费推理（Olares One "$3,999 vs Stop Renting"叙事） |

**7. 与 model/models.md 同类 family 的关联**

- **DeepSeek-R1**（同 01-llm 章）：`qwen vs deepseek`（210/mo, KD 7）是直接对比词，两款都在 Olares Market 可跑，可作 Olares 平台"自选模型"叙事的核心案例对；
- **Llama 3**（同章）：`qwen vs llama`（260/mo, KD 16）同理；Qwen3 中文能力 + 多语言优势是差异化点；
- **`ollama models`**（14,800/mo, KD 63）是跨 family 共用的引擎枢纽词——任何在 Ollama 生态写内容的模型报告都应汇入该词的内容矩阵。

---

*数据来源：SEMrush US（phrase_these / phrase_this / phrase_related / phrase_questions / resource_organic / domain_rank）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
