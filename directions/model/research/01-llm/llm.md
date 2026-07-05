# 开源 LLM（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 30 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 63%

## 摘要

2026 年年中，开源 LLM 在编码/agentic 与长上下文两条主线上持续逼近甚至局部反超闭源前沿，且几乎全部提供开放权重可本地部署。当前格局：**Qwen 系**以 Qwen3.6-27B（dense）与 35B-A3B（MoE）稳坐 24GB 单卡"甜点位"，是消费级本地部署最强全能选择，Apache 2.0 无商用门槛 [1][20]；**Z.ai GLM-5.2**（744B-A40B，MIT，1M 上下文/IndexShare）与 **DeepSeek V4**（Pro 1.6T / Flash 284B，MIT，1M 上下文）代表可自托管前沿旗舰，需多卡/服务器 [4][5][6][7]；**Kimi K2.7 Code**（1T-A32B，Modified MIT，基于 K2.6、thinking-token 减 ~30%）把开源 agentic 编码推到领先，SWE 系基准贴近 Claude Opus 4.8/GPT-5.5 [8][9]；**MiniMax M3**（428B-A23B，1M 上下文/MSA，原生多模态）是首个把"前沿编码 + 百万上下文 + 原生多模态"三件套集齐的开放权重模型，但许可为 **MiniMax Community License**（非 MIT/Apache，商用有条件）[10][11][12]；**Ornith-1.0**（DeepReinforce，MIT，9B→397B 四档，自生成 RL scaffold）以 397B 在 Terminal-Bench 2.1 / SWE-Bench Verified 达同级开源 SOTA、追平 Claude Opus 4.7，且 9B 可边缘部署 [13][14][15]。**Gemma 4**（Apache 2.0，E2B→31B 五档）仍是唯一横跨手机到台式的多模态全家桶 [16][17]；**Llama 4**（2025-04）已明显落后、Behemoth 搁置 [18][19]。对 Olares（个人云 OS，核心用例本地跑 Personal Agent）而言，**💻 本地台式级（≈7B–70B，Olares One 24GB）是主战场**，Qwen3.6-27B / Qwen3-Coder-30B-A3B / Gemma 4 26B-A4B / Ornith-1.0-31B 是首推主力；企业级旗舰用于"可自托管前沿替代"叙事，端侧小模型（Gemma 4 E4B、Qwen3-4B、Ornith-1.0-9B）用于"手机/边缘离线 agent"切入。

## 1. 型号总表（核心交付）

| 模型 family | 代表型号/尺寸(忽略量化) | 部署层级 | 许可 | 闭源对标 | 候选关键词 |
|---|---|---|---|---|---|
| **Gemma 4** | E2B / E4B | 📱 手机/边缘 | Apache 2.0 | Gemini Nano | `gemma 4 e4b on device`、`run gemma 4 on phone` |
| **Qwen3.x 小** | Qwen3-4B-Instruct-2507 | 📱 手机/边缘 | Apache 2.0 | GPT-4o mini / Gemini Nano | `qwen3 4b local`、`qwen 4b tool calling` |
| **Qwen 3.6** | Qwen3.6-27B (dense)、35B-A3B (MoE) | 💻 本地台式（主力） | Apache 2.0 | GPT-5 级 / Claude Sonnet | `run qwen3.6 27b locally`、`best local LLM 24GB VRAM` |
| **Qwen3-Coder** | Coder-30B-A3B（另 480B-A35B 大档） | 💻 本地台式 → 🏢 | Apache 2.0 | Claude Sonnet（coding） | `qwen3 coder local`、`qwen3 coder vs claude` |
| **Gemma 4 中大** | 12B、26B-A4B (MoE)、31B (dense) | 💻 本地台式 | Apache 2.0 | Gemini Flash | `gemma 4 31b local`、`gemma 4 vs qwen` |
| **Ornith-1.0** | 9B-Dense / 31B-Dense / 35B-MoE / 397B-MoE | 📱→🏢（9B📱・31B/35B💻・397B🏢） | MIT | Claude Opus 4.7（agentic coding） | `ornith 1.0 self-hosted`、`ornith 9b coding local`、`open source claude code model` |
| **GLM-5.2** | GLM-5.2 (744B-A40B) | 🏢 企业级 | MIT | GPT-5.5 / Claude Opus 4.8 | `GLM-5.2 self-hosted`、`GLM-5.2 vs GPT-5.5`、`run GLM-5.2 locally` |
| **DeepSeek V4** | V4-Flash (284B-A13B)、V4-Pro (1.6T-A49B) | 🏢 企业级 | MIT | Claude / Gemini（长上下文 agent） | `deepseek v4 flash vram`、`run deepseek v4 locally` |
| **Kimi K2.7 Code** | K2.7 Code (1T-A32B) | 🏢 企业级 | Modified MIT | GPT-5.5 / Claude Opus 4.8（agentic 编码） | `kimi k2.7 code self-hosted`、`kimi k2.7 vs claude code` |
| **MiniMax M3** | M3 (428B-A23B) | 🏢 企业级 | MiniMax Community License | Claude Opus（多模态 agent/coding） | `minimax m3 self-hosted`、`minimax m3 vs claude`、`open source multimodal agent LLM` |
| **Qwen3-Coder 大** | Coder-480B-A35B | 🏢 企业级 | Apache 2.0 | Claude Sonnet（agentic coding） | `qwen3 coder 480b`、`open source claude code model` |
| **Llama 4（渐旧）** | Scout 109B-A17B、Maverick 400B-A17B | 🏢 企业级 | Llama 4 社区许可（非 OSI） | GPT-4.5 / Gemini | `llama 4 scout local`、`llama 4 vs qwen` |

> 排序：按部署层级（📱→💻→🏢），层内按 Olares 相关热度。本轮已剔除 Qwen 3.5、Phi-4、Granite 4.1、Mistral 四个 family；GLM 只保留 5.2；MiniMax M2 由 M3 取代、Kimi K2 由 K2.7 Code 取代。DeepSeek R1、Llama 3.x、Qwen 2.5 等过期项亦不收录 [21]。

## 2. 分层解读

### 📱 手机/边缘级（≈4B–9B）
代表：**Gemma 4 E2B/E4B**、**Qwen3-4B-Instruct-2507**、**Ornith-1.0-9B**。
能力与门槛：Gemma 4 E4B 在 Q4 量化下仅约 4.5GB 内存、128K 上下文、原生 audio，与 Qualcomm/MediaTek/Pixel 深度适配可完全离线运行，是端侧 agent/tool-calling 首选 [17][23][24]；Qwen3-4B 在工具调用原生准确率领先、Apache 2.0 干净 [24]。本轮新增的 **Ornith-1.0-9B（MIT）** 把"编码专用小模型"推到新高度：SWE-Bench Verified 69.4、Terminal-Bench 2.1 43.1，接近 4 倍体量的 Qwen 3.5-35B（70.0），却可跑在笔记本/边缘设备上——靠的是训练期让模型自生成 agentic scaffold 而非堆参数 [13][14][15]。这一层对 Olares 的价值在"边缘节点/隐私优先的轻 agent"叙事。注意 4B 类实际需 ≥8GB RAM 才不被移动 OS 杀进程 [23]。

### 💻 本地台式级（≈7B–70B，主力主推）
代表：**Qwen3.6-27B (dense)**、**Qwen3.6-35B-A3B (MoE)**、**Qwen3-Coder-30B-A3B**、**Gemma 4 31B / 26B-A4B**、**Ornith-1.0-31B / 35B-MoE**。
这是 **Olares One 24GB 的甜点位、也是本报告主推层**。第三方 24GB 评测中 Qwen3.6-27B 以 Intelligence Index 45.8、TAU2 94.2% 拿下最强全能，Q4 约 16.8GB、Q6 约 22.5GB 可单卡跑；Gemma 4 31B 领跑编码/科学任务；35B-A3B（MoE）在 llama.cpp 达约 65 tok/s、追求速度首选 [20][1][21]。编码专用则用 Qwen3-Coder-30B-A3B（256K 上下文、MoE 稀疏）[2][3]，或本轮新增的 **Ornith-1.0-31B（MIT）**——其自生成 scaffold 训练法让中等尺寸也拿到强 agentic 编码分（35B-MoE Terminal-Bench 2.1 达 64.2，高于 Qwen 3.5-397B 的 53.5）[14][15]。门槛低（单张 24GB 消费卡即可）、许可以 Apache 2.0 / MIT 为主可商用，是 Olares "run X locally / self-hosted X" 内容与产品捆绑的核心。

### 🏢 企业级（≈100B–1T+）
代表：**GLM-5.2 (744B-A40B, MIT)**、**DeepSeek V4-Flash/Pro (284B/1.6T, MIT, 1M 上下文)**、**Kimi K2.7 Code (1T-A32B, Modified MIT)**、**MiniMax M3 (428B-A23B, MiniMax Community License, 1M 上下文/多模态)**、**Ornith-1.0-397B (MIT)**、**Qwen3-Coder-480B-A35B (Apache 2.0)**、**Llama 4 (渐旧)**。
这一层是"可自托管的前沿旗舰"，性能对标 GPT-5.5 / Claude Opus 4.8，但需多卡或服务器：
- **GLM-5.2** 744B-A40B、MIT，2026-06-13 发布、06-16 开放 MIT 权重；引入 IndexShare（每 4 层共享一个 sparse-attention indexer，1M 上下文下 per-token FLOPs 降 2.9×），首次在"稳定 1M 上下文"上支撑长程任务，Terminal-Bench 2.1 达 81.0、居 Artificial Analysis 开源智力指数榜首（51，总榜第 5）；建议 8 卡张量并行 [4][5]。
- **DeepSeek V4-Pro/Flash** 均 1M 上下文、MIT；1M 下 Pro 仅 V3.2 的 27% FLOPs、10% KV，Flash（13B active）量化后可单 80GB / 2×48GB 落地，是"能落地的 V4" [6][7][27]。
- **Kimi K2.7 Code**（本轮替代 K2）：1T-A32B、256K（262,144）上下文、Modified MIT，基于 K2.6 重训编码/agentic 奖励，thinking-token 较 K2.6 减 ~30%、强制 thinking 模式，Kimi Code Bench v2 从 K2.6 的 50.9 升到 62.0（Claude Opus 4.8 67.4、GPT-5.5 69.0），原生 INT4、~595GB 权重，可 vLLM/SGLang/KTransformers 自托管 [8][9]。
- **MiniMax M3**（本轮替代 M2）：428B-A23B MoE、1M 上下文（MiniMax Sparse Attention/MSA，1M 下 per-token 计算仅 M2 的 1/20、prefill 9×/decode 15× 提速）、原生多模态（文/图/视频），SWE-bench Verified 80.5、Video-MME v2 85.4、MMMU-Pro 78.1；是首个集齐"前沿编码 + 百万上下文 + 原生多模态"的开放权重模型。**许可为 MiniMax Community License（非 MIT/Apache）：个人/研究免费，商用须显著标注 "Built with MiniMax M3"，年营收 >$2000 万须事先获书面授权，否则仅需一次性备案** [10][11][12]。
- **Ornith-1.0-397B**（MIT）：397B-MoE，post-trained on Gemma 4 + Qwen 3.5，256K 上下文，Terminal-Bench 2.1 77.5 / SWE-Bench Verified 82.4，追平 Claude Opus 4.7（70.3 / 80.8）、SWE-Bench Verified 上仅次于 Claude Opus 4.8（87.6）；Terminal-Bench 上被更大的 GLM-5.2-744B（81.0）反超，故"开源 SOTA"限于同级尺寸。单节点 8×80GB（TP8）可服务 [13][14][15]。
对 Olares 而言，这层服务"高端发烧/多卡工作站/企业机架"用户与"开源前沿替代闭源 API"的 GEO 叙事；许可上 GLM/DeepSeek/Ornith 最宽松（MIT），Qwen Apache 2.0，Kimi 为轻量署名 Modified MIT，**MiniMax M3 商用有真实条件（写对比/替代文时须单列）**，Llama 4 非 OSI 且渐旧 [11][19]。

## 3. 候选 SEO 关键词与内容切入

- **型号词（品牌流量，中高竞争）**：`qwen3.6 27b`、`glm-5.2`、`deepseek v4`、`kimi k2.7 code`、`minimax m3`、`ornith 1.0`、`gemma 4`。适合承接型号发布期搜索峰值。
- **"run X locally / self-hosted X"（Olares 核心切入，多为低竞争长尾）**：`run qwen3.6 27b locally`、`GLM-5.2 self-hosted`、`run deepseek v4 locally`、`kimi k2.7 code self-hosted`、`minimax m3 self-hosted`、`ornith 1.0 self-hosted`、`self-hosted coding LLM 2026`。**低竞争、意图强、与 Olares "本地部署"高度契合，优先做。**
- **"X vs Y"（对比，低-中竞争）**：`qwen3.6 vs gemma 4`、`GLM-5.2 vs GPT-5.5`、`deepseek v4 vs claude`、`kimi k2.7 vs claude code`、`ornith 1.0 vs qwen3 coder`、`minimax m3 vs claude`。
- **"X alternative"（替代闭源，中竞争但高转化）**：`open source claude code alternative`、`open source claude opus alternative`、`self-hosted multimodal agent LLM`。
- **硬件/可跑性长尾（极低竞争，Olares One 强相关）**：`best local LLM 24GB VRAM 2026`、`deepseek v4 flash vram`、`qwen3.6 27b vram`、`ornith 9b coding local`、`gemma 4 e4b on device`。**这批数字型长尾竞争最低、与 Olares One 硬件卖点直接绑定，最值得批量铺。**

## 关键发现

- **24GB 甜点位仍由 Qwen3.6-27B 统治，Ornith-1.0-31B 成新对手**：两者都可单卡跑、许可干净（Apache 2.0 / MIT），"best local LLM 24GB / run Qwen3.6 locally / self-hosted coding LLM" 是最高性价比的内容矩阵。[20][1][14]
- **"自生成 scaffold" 让小模型打大模型**：Ornith-1.0 靠训练期联合优化 solution + scaffold，让 9B 在 SWE-Bench Verified（69.4）逼近 4 倍体量模型、397B 追平 Claude Opus 4.7；这是"MIT 开源 + 可边缘部署的强编码模型"的新叙事支点。[13][14][15]
- **许可分化必须写进对比/替代文**：GLM-5.2 / DeepSeek V4 / Ornith-1.0 为 MIT，Qwen 为 Apache 2.0（均可商用无门槛）；Kimi K2.7 为"超大规模才需署名"的 Modified MIT；**MiniMax M3 为 MiniMax Community License——商用须署名、年营收 >$2000 万须事先授权**，是"self-hosted 商用无忧"叙事里唯一需要提醒读者的例外。[11][8][14][4]
- **MoE + 稀疏注意力让"前沿模型本地化"门槛骤降**：GLM-5.2 的 IndexShare、DeepSeek V4 的 CSA+HCA、MiniMax M3 的 MSA 把 1M 上下文的 FLOPs/KV 降到旧版的 1/4~1/20，V4-Flash 甚至可 2×48GB 落地，"可自托管前沿"从口号变现实。[4][6][12][25]

## 局限性

- 时点为 AS_OF 2026-07-05；模型版本迭代极快（GLM 已到 5.2、Kimi 到 K2.7 Code、MiniMax 到 M3），发布/尺寸/基准以官方模型卡为准，引用前复核。
- **基准多为厂商自报**：Kimi K2.7 Code 的编码提升全部来自 Moonshot 自有测试集，缺发布时的独立 SWE-bench/LiveCodeBench 复核 [8][9]；Ornith-1.0 与 MiniMax M3 的对比表亦为官方发布，独立复现有限 [13][15][10]。
- **"开源 SOTA / 综合第一" 存在口径分歧**：Ornith-1.0-397B 的 SOTA 仅限"同级尺寸开源"，Terminal-Bench 上被更大的 GLM-5.2-744B 反超 [15][29]；GLM-5.2 据二手源居 Artificial Analysis 开源智力指数第一（51），M3 更强调多模态与长上下文，两者"谁是开源综合第一"取决于榜单与口径，对比文中应注明 [4]。
- 本报告为 Lightweight 模式，未覆盖：逐模型完整基准表、量化后精度损失、多语种/长上下文实测、推理引擎（vLLM/SGLang/llama.cpp/MLX）逐一实测吞吐。Omni 多模态模型按要求不在此列（M3 的多模态仅作 family 说明）。

## 参考文献

[1] Alibaba Qwen — Qwen3.6 官方仓库 | Source-Type: official | As Of: 2026-04 | https://github.com/QwenLM/Qwen3.6
[2] Alibaba Qwen — Qwen3-Coder 官方仓库 | Source-Type: official | As Of: 2026-06 | https://github.com/QwenLM/Qwen3-Coder/
[3] Alibaba Qwen — Qwen3-Coder 官方博客 | Source-Type: official | As Of: 2025-07 | https://qwenlm.github.io/blog/qwen3-coder/
[4] Z.ai (Zhipu) — GLM-5.2 官方博客 | Source-Type: official | As Of: 2026-06 | https://z.ai/blog/glm-5.2
[5] Z.ai (Zhipu) — GLM-5 官方仓库（README 覆盖 5.2） | Source-Type: official | As Of: 2026-06 | https://github.com/zai-org/glm-5
[6] DeepSeek — DeepSeek-V4-Pro 官方模型卡 | Source-Type: official | As Of: 2026-04 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
[7] DeepSeek — DeepSeek-V4 技术报告 (arXiv) | Source-Type: academic | As Of: 2026-06 | https://arxiv.org/html/2606.19348
[8] Moonshot AI — Kimi K2.7 Code 官方模型卡 (HF) | Source-Type: official | As Of: 2026-06 | https://huggingface.co/moonshotai/Kimi-K2.7-Code
[9] Moonshot AI — Kimi K2.7 Code 官网资源页 | Source-Type: official | As Of: 2026-06 | https://www.kimi.com/resources/kimi-k2-7-code
[10] MiniMax — MiniMax-M3 官方模型卡 (HF) | Source-Type: official | As Of: 2026-06 | https://huggingface.co/MiniMaxAI/MiniMax-M3
[11] MiniMax — MiniMax-M3 LICENSE (HF) | Source-Type: official | As Of: 2026-06 | https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE
[12] MiniMax — MiniMax M3 官方博客 | Source-Type: official | As Of: 2026-06 | https://www.minimax.io/blog/minimax-m3
[13] DeepReinforce — Ornith-1.0-397B 官方模型卡 (HF) | Source-Type: official | As Of: 2026-06 | https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B
[14] DeepReinforce — Ornith-1 GitHub README | Source-Type: official | As Of: 2026-06 | https://github.com/deepreinforce-ai/Ornith-1/blob/main/README.md
[15] DeepReinforce — Ornith-1.0 官方博客 | Source-Type: official | As Of: 2026-06 | https://deep-reinforce.com/ornith_1_0.html
[16] Google — Gemma 4 官方博客 | Source-Type: official | As Of: 2026-04 | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
[17] Google — Gemma 4 官方文档 | Source-Type: official | As Of: 2026-04 | https://ai.google.dev/gemma/docs/core
[18] Meta — Llama 4 官方博客 | Source-Type: official | As Of: 2025-04 | https://ai.meta.com/blog/llama-4-multimodal-intelligence/
[19] Meta — Llama 4 MODEL_CARD | Source-Type: official | As Of: 2025-04 | https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md
[20] LocalLLM.in — Best Local LLMs 24GB VRAM 2026 | Source-Type: secondary-industry | As Of: 2026-05 | https://localllm.in/blog/best-local-llms-24gb-vram
[21] WillItRunAI — 16/24/32GB VRAM 指南 | Source-Type: secondary-industry | As Of: 2026-04 | https://willitrunai.com/blog/what-can-you-run-on-16gb-24gb-32gb-vram
[22] DeepInfra — V4 Flash vs Qwen3.6 vs GLM-4.6 | Source-Type: secondary-industry | As Of: 2026-05 | https://deepinfra.com/blog/deepseek-v4-flash-vs-qwen3-6-vs-glm-4-6
[23] Labellerr — 7 Best SLM Under 10B 2026 | Source-Type: secondary-industry | As Of: 2026-05 | https://www.labellerr.com/blog/best-small-language-models-under-10b-parameters/
[24] Ertas AI — On-Device Tool Calling 2026 | Source-Type: secondary-industry | As Of: 2026-03 | https://www.ertas.ai/blog/on-device-tool-calling-2026-qwen3-gemma4-phi4
[25] Sebastian Raschka — LLM 架构进展 | Source-Type: secondary-industry | As Of: 2026-05 | https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures
[26] DigitalApplied — Gemma4 vs Llama4 vs Mistral Small 4 | Source-Type: secondary-industry | As Of: 2026-04 | https://www.digitalapplied.com/blog/gemma-4-vs-llama-4-vs-mistral-small-4-comparison
[27] Hugging Face — DeepSeek-V4 博客 | Source-Type: secondary-industry | As Of: 2026-04 | https://huggingface.co/blog/deepseekv4
[28] AI Weekly — MiniMax open-sources M3 报道 | Source-Type: journalism | As Of: 2026-06 | https://aiweekly.co/alerts/minimax-open-sources-m3-428b-multimodal-moe-with-1m-context
[29] MarkTechPost — DeepReinforce Releases Ornith-1.0 报道 | Source-Type: journalism | As Of: 2026-06 | https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/
[30] Kili Technology — MiniMax M3 许可与数据分析 | Source-Type: secondary-industry | As Of: 2026-06 | https://kili-technology.com/blog/data-story-minimax-m3
