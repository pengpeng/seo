# Ornith-1.0 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：DeepReinforce（deep-reinforce.com），MIT
>
> **注：** 任务说明中将出品方标注为"Kagi"，但根据 DeepReinforce 官方博客、GitHub（deepreinforce-ai/Ornith-1）、HuggingFace 模型页及多方第三方报道，Ornith-1.0 的出品方为 **DeepReinforce**（独立 AI 研究团体），非 Kagi。报告按实际来源记录。
>
> **降级模式**：Ornith-1.0 于 2026-06-25 发布，上线不足两周，所有 ornith 品牌词（ornith 1.0、ornith llm、ornith model、ornith ollama 等）在 Semrush 均返回零数据。`deep-reinforce.com` 域名数据同样尚未形成。SEO 主战场目前在 HuggingFace（deepreinforce-ai 系列）、GitHub（deepreinforce-ai/Ornith-1）与第三方内容页面；品牌词全部列为 GEO 抢发候选。

---

## 模型理解（前置）

Ornith-1.0 是 DeepReinforce 于 2026 年 6 月 25 日发布的**开源 Agentic Coding LLM 家族**，提供 9B Dense、31B Dense、35B MoE、397B MoE 四档尺寸，全系 MIT 授权，无地区限制。其核心创新是**自生脚手架（Self-Scaffolding）强化学习框架**：模型不仅生成代码解法，还在 RL 训练中同步学习生成驱动该解法的 orchestration scaffold——搜索策略、工具调用顺序、内存布局——从而在 terminal-native 编码代理任务上实现自进化，无需人工设计 harness。397B 旗舰在 Terminal-Bench 2.1（77.5）和 SWE-Bench Verified（82.4）上超越 Claude Opus 4.7（70.3 / 80.8），为同等开源模型中 SOTA。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 面向 agentic coding 的自生脚手架开源 LLM 家族，terminal-native，SWE-Bench SOTA |
| 许可证 | **MIT**（全球商用友好，无地区限制） |
| 主仓库 / 分发 | GitHub: [deepreinforce-ai/Ornith-1](https://github.com/deepreinforce-ai/Ornith-1)（★ 量级待确认）；HuggingFace: deepreinforce-ai 系列（9B/35B/397B bf16+GGUF+FP8；**31B 公开权重截至 2026-06-26 尚未上架**）；Ollama（9B tag 5.6GB，35B tag ~21GB） |
| 参数 / VRAM 可跑性 | 9B bf16 ~19GB / Q4 ~6GB；**31B bf16 ~62GB / Q4 ~20GB（Olares One 24GB 可跑 Q4，公开权重待上线）**；35B MoE Q5_K_M ~25GB（接近 24GB 上限，Ollama tag ~21GB 可跑）；397B bf16 ~400GB / FP8 ~200GB（多 GPU 集群） |
| 变体 / 型号 | Ornith-1.0-9B（Qwen 3.5 底座）/ Ornith-1.0-31B（Gemma 4 底座，Dense）/ Ornith-1.0-35B（Qwen 3.5 底座，MoE，active param ~3B/token）/ Ornith-1.0-397B（Qwen 3.5 底座，MoE） |
| 支持引擎 | vLLM、SGLang（官方文档）；Ollama、LM Studio（社区验证）；适配 Claude Code / OpenHands / OpenClaw / Hermes Agent |
| 闭源对标 | **Claude Opus 4.7**（agentic coding，按 token 计费） |
| Olares Market | 未直接上架；通过 Ollama（已在 Olares Market）可一键部署 9B/35B；31B Q4 待公开权重后同路径可用 |
| 来源 | [DeepReinforce 官博](https://deep-reinforce.com/ornith_1_0.html)、[GitHub README](https://github.com/deepreinforce-ai/Ornith-1/blob/main/README.md)、[HuggingFace 9B 卡](https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B)、[codersera 本地部署指南](https://codersera.com/blog/how-to-run-ornith-1-0-locally-2026/) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0。

> **SEO 名称污染警告**：前缀 `ornith-` 在英语中指"鸟/鸟类学"（ornithology），Semrush 中 "ornith" 的 260 月量主要来自鸟类学前缀搜索（ornitho、ornithic、ornithos 等），**不代表 Ornith 模型流量**。品牌词当前全为零量，属正常——需要 GEO 内容抢占定义权，并在标题/内容中明确 "Ornith-1.0 coding LLM" 而非单独 "ornith"。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ornith 1.0 | 0 | — | — | — |
| ornith llm | 0 | — | — | — |
| ornith model | 0 | — | — | — |
| ornith 9b | 0 | — | — | — |
| ornith 31b | 0 | — | — | — |
| ornith 35b | 0 | — | — | — |
| ornith 397b | 0 | — | — | — |
| ornith moe | 0 | — | — | — |
| deepreinforce | 10 | 0 | $0 | info |
| deepreinforce ornith | 0 | — | — | — |

> 以上均为 GEO 前哨候选，Semrush 零量 = 无历史内容可竞争，先发内容即可占据 AI 概览/Perplexity 引用位。

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| ornith ollama | 0 | — | — | — |
| ornith vllm | 0 | — | — | — |
| ornith sglang | 0 | — | — | — |
| ornith lm studio | 0 | — | — | — |
| ornith local | 0 | — | — | — |
| run ornith locally | 0 | — | — | — |

> 全为零量 GEO 前哨。对标：其他新模型（如 Qwen3-Coder）上线 3–6 个月后引擎组合词才开始有量；先发文章可截流。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| self hosted llm ⭐ | 320 | 22 | $3.12 | info |
| local llm for coding ⭐ | 170 | 41 | $3.24 | info |
| local coding agent ⭐ | 50 | 0 | $6.02 | info |
| local ai coding | 10 | 0 | $6.61 | info |
| run coding agent locally | 10 | 0 | $6.29 | info |
| ornith gguf | 0 | — | — | — |
| ornith vram | 0 | — | — | — |
| ornith install | 0 | — | — | — |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| agentic coding | 880 | 45 | $5.18 | info |
| claude code alternative ⭐ | 480 | 18 | $6.42 | info/comm |
| agentic llm | 260 | 49 | $4.68 | info |
| open source coding agent ⭐ | 210 | 20 | $5.51 | info |
| open source cursor alternative ⭐ | 210 | 28 | $2.56 | info/comm |
| open source ai coding agent ⭐ | 210 | 39 | $4.23 | info |
| local llm for coding ⭐ | 170 | 41 | $3.24 | info |
| openhands ai | 170 | 43 | $6.12 | info/nav |
| best open source coding llm ⭐ | 90 | 25 | $4.12 | info |
| open source coding assistant | 90 | 50 | $5.07 | info |
| open source copilot | 70 | 52 | $6.21 | info/comm |
| open source claude code alternative ⭐ | 50 | 19 | $3.58 | info/comm |
| local coding agent ⭐ | 50 | 0 | $6.02 | info |
| free claude alternative ⭐ | 40 | 16 | $2.13 | info/comm |
| open source swe agent | 0 | — | — | — |
| open source devin alternative | 20 | 0 | $0 | info |
| agentic coding benchmark ⭐ | 30 | 0 | $6.12 | info |
| self scaffolding llm | 0 | — | — | — |
| MIT agentic LLM | 0 | — | — | — |
| ornith vs claude | 0 | — | — | — |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | 契合度 | Olares 角度 |
|--------|------|----|----|--------|------------|
| claude code alternative | 480 | 18 | $6.42 | ⭐⭐⭐ | Ornith-1.0 via Ollama on Olares One = Claude Code 的零 API 费本地替代；MIT 授权可商用，无每 token 计费，无额度限制 |
| open source coding agent | 210 | 20 | $5.51 | ⭐⭐⭐ | Olares One 内置 Ollama，Ornith-1.0 35B/9B 一键启动，24GB GDDR7 跑满精度，完整 agentic coding 工作流在设备上闭环 |
| open source cursor alternative | 210 | 28 | $2.56 | ⭐⭐ | Ornith + OpenHands/OpenClaw 在 Olares 上可组成本地 Cursor-style 代理；数据不出机器 |
| self hosted llm | 320 | 22 | $3.12 | ⭐⭐⭐ | Olares = 一键自托管 LLM 运行时；Ornith MIT 授权意味着自托管即商用，无 ToS 限制 |
| open source claude code alternative | 50 | 19 | $3.58 | ⭐⭐⭐ | 直接对标叙事：Ornith-1.0-397B 在 SWE-Bench Verified 超 Claude Opus 4.7，MIT 免费，在 Olares 上本地跑 |
| local coding agent | 50 | 0 | $6.02 | ⭐⭐⭐ | Olares One 的核心使用场景之一；Ornith 9B/35B Ollama 部署，编码代理 24/7 在线，无云端延迟 |
| free claude alternative | 40 | 16 | $2.13 | ⭐⭐ | 经济叙事入口：一次性购买 Olares One vs 按月付费 Claude API，Ornith MIT 永久免费商用 |
| best open source coding llm | 90 | 25 | $4.12 | ⭐⭐ | Listicle/对比文入口；Ornith-1.0 是 2026 年 6 月最强开源 agentic coding 模型，可在 Olares 本地跑 |
| run coding agent locally | 10 | 0 | $6.29 | ⭐⭐⭐ | 低量但极高漏斗意图（CPC $6.29），直接捕获"想在本地建 coding agent"的决策者；Olares One 是最快路径 |
| ornith ollama | 0 | — | — | ⭐⭐⭐ | GEO 先机：零竞争，占 "ornith ollama" AI Overview 引用位；Olares = Ollama 的最简自托管宿主 |
| ornith vs claude | 0 | — | — | ⭐⭐⭐ | GEO 先机：对比型零量词，搜索意图一旦出现将是高商业价值词；Olares 角度——本地 Ornith vs 云端 Claude：无 API 费 + 数据不出设备 |
| self scaffolding llm | 0 | — | — | ⭐⭐ | GEO 先机：技术概念词，定义性内容（解释 self-scaffolding 是什么）最易被 AI 概览引用 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| claude code alternative | 480 | 18 | $6.42 | info/comm | **主词候选** | 量足（480）+ KD 极低（18）+ 高 CPC = 最佳攻击面；Ornith-1.0 在 Olares 上是 Claude Code 的开源本地替代，SWE-Bench 数据背书 |
| agentic coding | 880 | 45 | $5.18 | info | **主词候选** | 量最大，但 KD45 偏高；作为品类词适合做宽口入口文，Ornith 是该品类 2026 最强开源代表；Olares 是运行 agentic coding 工作流的本地平台 |
| self hosted llm | 320 | 22 | $3.12 | info | **主词候选** | 量 320 + KD 低（22）= 稳健主词候选；Ornith MIT 商用友好是自托管叙事的最强论据；Olares 一键跑 Ollama |
| open source coding agent | 210 | 20 | $5.51 | info | **主词候选** | 量 210 + KD20 + CPC 高 = 商业价值强；Ornith 就是"open source coding agent"的型号代表；Olares 提供零运维部署环境 |
| open source cursor alternative | 210 | 28 | $2.56 | info/comm | **主词候选** | 量 210 + 意图偏向替代/决策；Ornith + OpenHands on Olares 可构成本地 Cursor 替代方案 |
| agentic llm | 260 | 49 | $4.68 | info | **次级** | 量 260 但 KD49 偏高；适合作为 agentic coding 主词文章的次级词/H2 |
| open source ai coding agent | 210 | 39 | $4.23 | info | **次级** | KD 39 偏高，收为次级；可并入 "open source coding agent" 主词文章 |
| local llm for coding | 170 | 41 | $3.24 | info | **次级** | KD41 高；适合硬件/部署角度文章的次级词，与 Olares One 24GB 叙事天然契合 |
| best open source coding llm | 90 | 25 | $4.12 | info | **主词候选** | 量 90 略低但同族合计可上提，KD25 可攻，Ornith 是 2026 年 6 月该问题的最佳答案之一 |
| open source claude code alternative | 50 | 19 | $3.58 | info/comm | **主词候选** | 量 50 偏低但意图极纯（决策型）+ KD19 + CPC $3.58；Ornith MIT + Olares 是该词的完整答案 |
| free claude alternative | 40 | 16 | $2.13 | info/comm | **次级** | 量偏低（40）但 KD16，可并入替代类文章作为次级变体 |
| local coding agent | 50 | 0 | $6.02 | info | **主词候选** | 零 KD + CPC $6.02（意图极强）= 意图上提规则；虽量 50 仍值得独立文章；Olares + Ornith 是最直接的答案 |
| open source devin alternative | 20 | 0 | $0 | info | **次级** | 量低，但 Ornith 是 Devin 的开源替代候选，作为次级词收录 |
| agentic coding benchmark | 30 | 0 | $6.12 | info | **次级** | 技术对比内容的次级词，可用于阐述 Ornith 在 SWE-Bench / Terminal-Bench 的成绩 |
| ornith 1.0 | 0 | — | — | — | **GEO** | 品牌词，当前零量；先发内容定义"什么是 ornith 1.0"，抢 AI Overview 引用位 |
| ornith llm | 0 | — | — | — | **GEO** | 同上，搜索意图明确但尚无量；及时占位 |
| ornith ollama | 0 | — | — | — | **GEO** | 引擎组合词，零量但零竞争；Olares 是 Ollama 最优宿主，相关文档/教程率先上线即占位 |
| ornith vs claude | 0 | — | — | — | **GEO** | 对比型意图一旦成形 CPC 会很高；先发"Ornith vs Claude Opus 4.7"内容 |
| self scaffolding llm | 0 | — | — | — | **GEO** | 技术概念型，Ornith 是该概念最大开源代表；定义性内容被 AI 概览引用概率高 |
| MIT agentic LLM | 0 | — | — | — | **GEO** | 许可证角度切入，强调商用自由；Olares 商用场景叙事的 GEO 前哨 |
| run ornith locally | 0 | — | — | — | **GEO** | 部署教程型，具体操作步骤被 AI 概览收录概率高；写 Olares + Ollama 实操教程 |

---

## 核心洞见

**1. 搜索心智未建立，SEO 主战场在第三方内容和 HuggingFace**

Ornith-1.0 于 2026-06-25 发布，截至本报告（2026-07-06）仅 11 天，所有品牌/型号词在 Semrush 均为零量。`ornith` 通用词的 260 月量 99% 来自鸟类学前缀（ornitho-、ornithic 等），**对模型没有实质意义**。这是品牌命名的长期 SEO 劣势——模型名与高频自然语言前缀重叠，流量极难归因，需要始终以"Ornith-1.0 LLM"全称而非"ornith"出现在内容中。当前 SEO 机会完全来自：① HuggingFace/GitHub 模型页被第三方内容引用；② GEO（AI Overview / Perplexity）抢先占位。

**2. Ornith-1.0 可在消费级 GPU / Olares One 上本地跑——叙事成立**

- **9B Q4（~6GB）**：任何 8GB+ GPU 可跑，Olares One 完全无压力
- **35B MoE Ollama tag（~21GB）**：Olares One 24GB RTX 5090 Mobile 可跑，速度接近 9B 模型（MoE 每 token 仅激活 ~3B 参数）
- **31B Dense Q4（~20GB）**：Olares One 24GB 可跑，但官方公开权重截至 2026-06-26 尚未上线 HuggingFace，需持续关注
- **397B MoE**：需多 GPU 集群，不适合 Olares One 本地部署场景

**结论：Olares One 上最优选是 35B MoE（性能/内存最平衡）或 9B（超低资源全能入门），31B Dense Q4 一旦权重上线同样可跑。**

**3. MIT 授权是核心卖点，可大力主推**

MIT 全球商用友好，无地区限制。相比 Claude Opus 4.7 的 API 按 token 计费：
- 无 per-token 成本：长上下文（256K）agentic 工作流成本降至零
- 无额度限制：可持续高并发跑 SWE-Bench 类任务
- 无隐私风险：数据不出 Olares One 设备
- 商用无 ToS 约束：企业/SMB 无需签商业协议

**4. 对 Olares 最关键的 3 个词**

1. **`claude code alternative`**（480/KD18/CPC $6.42）——最高商业价值对比词，KD 极低，直接对标；Olares + Ornith = 零成本本地替代
2. **`open source coding agent`**（210/KD20/CPC $5.51）——品类定义词，Ornith 是该品类 SOTA，Olares 提供最简自托管环境
3. **`local coding agent`**（50/KD0/CPC $6.02）——零竞争 + 极强购买意图，Olares One 场景完美契合

**5. GEO 抢发窗口（刚发布，需立即行动）**

| 词 | 优先级 | 建议内容形式 |
|----|--------|------------|
| ornith 1.0 | 🔥 最高 | "What is Ornith-1.0? Open-source agentic coding LLM explained" 定义文 |
| ornith vs claude opus | 🔥 最高 | "Ornith-1.0 vs Claude Opus 4.7: Open-source beats closed on SWE-Bench" 对比文 |
| run ornith locally / ornith ollama | 🔥 最高 | "How to run Ornith-1.0 locally with Ollama on Olares" 实操教程 |
| self scaffolding llm | 高 | 技术定义文，解释 Self-Scaffolding RL，Ornith 作为核心案例 |
| ornith 31b / ornith 35b | 高 | 型号选择指南，31B Q4 适合 24GB 显存场景 |
| MIT agentic LLM | 中 | 许可证角度文章，强调商业自由与合规 |

**窗口时间估算**：参考同类新模型（Qwen3-Coder、GLM-4 等），GEO 引用位竞争在发布后 2–4 周内最开放；Semrush 数据 lag 约 4–8 周，此期间发布的内容有最高概率被 AI Overview 引用。

**6. 闭源对标与攻击面**

| 对标产品 | 攻击面 |
|---------|--------|
| **Claude Opus 4.7**（最直接） | Ornith-397B 在 Terminal-Bench 2.1（77.5 vs 70.3）和 SWE-Bench Verified（82.4 vs 80.8）均超越；Claude 按 token 计费，256K 上下文任务成本高；数据上传 Anthropic 服务器 |
| Claude Code（Anthropic 编码 Agent） | Ornith + OpenHands/OpenClaw 可构成本地等效替代；零 API 成本；适合需要数据隐私的企业 |
| GitHub Copilot / Cursor | 订阅制 SaaS，$10–$40/月；Ornith on Olares = 一次性硬件 + 永久零边际成本 |
| Devin（SWE-agent） | 闭源、价格高昂；Ornith 开源替代，在 Olares 本地跑完整 agentic pipeline |

**7. 与 model/models.md 同类 family 的关联**

Ornith-1.0 属于 `01-llm/` 品类，与同仓库已有报告 `qwen3-coder.md` 形成关联：
- 两者同为 2026 年 agentic coding LLM 代表，Qwen3-Coder 与 Ornith 共同构成"最强开源 coding LLM"的内容矩阵
- `ornith 35b` 底座同为 Qwen 3.5（与 Qwen3-Coder 同族），对比文可复用 Qwen 受众
- 跨报告关键词簇机会：`best open source coding llm`、`open source claude code alternative` 两者均覆盖，seo-content 阶段可合并为一篇 listicle

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
*模型技术事实来源：DeepReinforce 官方博客（deep-reinforce.com/ornith_1_0.html）、GitHub（deepreinforce-ai/Ornith-1）、HuggingFace（deepreinforce-ai/Ornith-1.0-9B）、codersera 本地部署指南、emergent.sh、explainx.ai、devops.com、marktechpost.com 第三方报道（2026-06-25）。*
