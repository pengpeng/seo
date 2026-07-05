---
task_id: 02
role: LLM 研究专员（增量刷新）
status: complete
sources_found: 12
as_of: 2026-07-05
scope: 新增 MiniMax M3 / Kimi K2.7 Code / Ornith-1.0；GLM 收敛到 5.2；删除 Qwen3.5/Phi-4/Granite4.1/Mistral
---

## Sources
[1] MiniMax-M3 官方模型卡 (HF) | https://huggingface.co/MiniMaxAI/MiniMax-M3 | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[2] MiniMax-M3 LICENSE (HF) | https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[3] MiniMax M3 官方博客 | https://www.minimax.io/blog/minimax-m3 | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[4] Kimi K2.7 Code 官方模型卡 (HF) | https://huggingface.co/moonshotai/Kimi-K2.7-Code | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[5] Kimi K2.7 Code 官网资源页 | https://www.kimi.com/resources/kimi-k2-7-code | Source-Type: official | As Of: 2026-06 | Authority: 8/10
[6] Ornith-1.0-397B 官方模型卡 (HF) | https://huggingface.co/deepreinforce-ai/Ornith-1.0-397B | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[7] Ornith-1 GitHub README | https://github.com/deepreinforce-ai/Ornith-1/blob/main/README.md | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[8] DeepReinforce Ornith-1.0 官方博客 | https://deep-reinforce.com/ornith_1_0.html | Source-Type: official | As Of: 2026-06 | Authority: 8/10
[9] GLM-5.2 官方博客 (Z.ai) | https://z.ai/blog/glm-5.2 | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[10] AI Weekly — MiniMax open-sources M3 报道 | https://aiweekly.co/alerts/minimax-open-sources-m3-428b-multimodal-moe-with-1m-context | Source-Type: journalism | As Of: 2026-06 | Authority: 6/10
[11] MarkTechPost — Ornith-1.0 报道 | https://www.marktechpost.com/2026/06/25/deepreinforce-releases-ornith-1-0-an-open-source-coding-model-family-that-learns-its-own-rl-scaffolds/ | Source-Type: journalism | As Of: 2026-06 | Authority: 6/10
[12] Kili Technology — MiniMax M3 许可数据分析 | https://kili-technology.com/blog/data-story-minimax-m3 | Source-Type: secondary-industry | As Of: 2026-06 | Authority: 6/10

## Findings
- MiniMax M3：428B 总 / ~23B 激活 MoE，1M 上下文（MiniMax Sparse Attention/MSA，1M 下 per-token 计算约 M2 的 1/20、prefill 9×/decode 15× 提速），原生多模态（文/图/视频），2026-06 开源发布。SWE-bench Verified 80.5、MMMU-Pro 78.1、Video-MME v2 85.4、Claw-Eval 74.5。三种 thinking 模式（enabled/adaptive/disabled）。[1][3][10]
- **MiniMax M3 许可 = MiniMax Community License（HF 元数据 license: other / license_name: minimax-community）——非 MIT/Apache**：个人/研究免费；商用须显著标注 "Built with MiniMax M3"，年营收 >$2000 万美元须事先书面授权（api@minimax.io），否则仅需一次性备案。属"open-weight 但商用有条件"。[2][12]
- Kimi K2.7 Code：1T 总 / 32B 激活 MoE（384 experts，8+1 shared，61 层，MLA + MoonViT 400M 视觉编码器），256K（262,144）上下文，Modified MIT，2026-06-12 发布，基于 K2.6。thinking-token 较 K2.6 减 ~30%、强制 preserve_thinking。Kimi Code Bench v2：K2.6 50.9 → K2.7 62.0（GPT-5.5 69.0 / Claude Opus 4.8 67.4）。原生 INT4、~595GB 权重。Model ID `moonshotai/Kimi-K2.7-Code`。[4][5]
- Ornith-1.0（DeepReinforce）：MIT，2026-06（MarkTechPost 报道 06-25）；四档 9B-Dense / 31B-Dense / 35B-MoE / 397B-MoE，post-trained on Gemma 4 + Qwen 3.5，256K 上下文；核心是 RL 联合优化 solution rollout + scaffold（自生成 harness）。397B：Terminal-Bench 2.1 77.5 / SWE-Bench Verified 82.4（≈ Claude Opus 4.7 70.3/80.8，SWE-V 仅次 Opus 4.8 87.6）；9B：Terminal-Bench 2.1 43.1 / SWE-Bench Verified 69.4（可边缘部署）。SOTA 限"同级尺寸开源"。[6][7][8][11]
- GLM-5.2：744B-A40B、MIT，2026-06-13 发布、06-16 开放权重；IndexShare（每 4 层共享 sparse-attention indexer，1M 上下文 per-token FLOPs 降 2.9×）+ 改进 MTP；稳定 1M 上下文、双 thinking effort（High/Max）。Terminal-Bench 2.1 81.0、SWE-bench Pro 62.1；二手源称居 Artificial Analysis 开源智力指数第一（51，总榜第 5）。取代此前报告的 GLM-5/5.1。[9]
- 删除项落实：Qwen 3.5、Phi-4、Granite 4.1、Mistral 四个 family 已从型号总表与正文移除；MiniMax M2 由 M3 取代、Kimi K2 Thinking 由 K2.7 Code 取代。

## Deep Read Notes
### Source [1]/[2]/[3]: MiniMax M3（HF 模型卡 + LICENSE + 官方博客）
Key data: ~428B/~23B active，1M 上下文靠 MSA；官方博客称 M3 是"首个同时具备前沿编码 + 百万上下文 + 原生多模态的开放权重模型"。HF README front-matter 明确 `license: other / license_name: minimax-community / license_link: LICENSE`。LICENSE 正文：非商用免费；商用须 (1) 显著展示 "Built with MiniMax M3"，(2) 年营收 >$2000 万须事先书面授权，否则一次性备案。
Key insight: 能力强但许可是本轮唯一"商用有真实门槛"的模型——所有"self-hosted 商用无忧"内容都要把 M3 单列说明。多模态仅作 family 说明，不纳入 Omni 章。
Useful for: 🏢 企业级；`minimax m3 self-hosted`、`minimax m3 license`、`open source multimodal agent LLM`。

### Source [4]/[5]: Kimi K2.7 Code（HF 模型卡 + kimi.com）
Key data: 1T-A32B、256K、Modified MIT、2026-06-12、基于 K2.6；thinking-token 减 ~30%、强制 thinking；架构与 K2.5/K2.6 相同，部署可直接复用（vLLM/SGLang/KTransformers）。基准全为 Moonshot 自有集，发布时无独立 SWE-bench。
Key insight: 定位"编码/agentic 专用刷新版"而非通用聊天；效率（少 30% 推理 token）是主卖点，长 agentic 运行显著省成本。
Useful for: 🏢 企业级 agentic 编码；`kimi k2.7 code self-hosted`、`kimi k2.7 vs claude code`。

### Source [6]/[7]/[8]: Ornith-1.0（HF 397B 卡 + GitHub README + 官方博客）
Key data: 四档 9B/31B/35B-MoE/397B-MoE，post-trained on Gemma 4 + Qwen 3.5，MIT，256K；自生成 scaffold 的 RL。397B 单节点 8×80GB（TP8）；9B 可笔记本/边缘。对比表含 Qwen3.5-397B / GLM-5.2-744B / MiniMax-M3-428B / DeepSeek-V4-Pro / Claude Opus 4.7/4.8。
Key insight: "自写 harness" 让小模型打大模型——9B SWE-V 69.4 逼近 4× 体量；MIT + 可边缘部署是强内容支点。SOTA 说法须限定"同级尺寸开源"，Terminal-Bench 被更大 GLM-5.2 反超。
Useful for: 跨层（9B 📱→💻、397B 🏢）；`ornith 1.0 self-hosted`、`ornith 9b coding local`、`open source claude code model`。

### Source [9]: GLM-5.2（Z.ai 官方博客）
Key data: 744B-A40B、MIT、1M 上下文、IndexShare 降 FLOPs 2.9×、双 thinking effort；SWE-bench Pro 62.1、Terminal-Bench 2.1 81.0；2026-06-13 发布、06-16 开放 MIT 权重。
Key insight: 本轮 GLM 收敛到唯一在售旗舰 5.2；"稳定 1M 上下文 + MIT" 是可自托管前沿的强叙事。
Useful for: 🏢 企业级；`GLM-5.2 self-hosted`、`GLM-5.2 vs GPT-5.5`、`run GLM-5.2 locally`。

## Gaps
- 厂商自报基准占多数（Kimi K2.7 全自有集、Ornith/M3 对比表官方发布），发布期缺独立第三方复核；对比文需注明测试口径。[4][11][10]
- "开源综合第一" 有口径冲突：二手源（lushbinary）称 GLM-5.2 居 Artificial Analysis 开源智力指数第一（51），而 M3 强调多模态+长上下文、Ornith 强调同级编码 SOTA——三者"第一"取决于榜单维度，报告中已按维度分别表述。
- MiniMax M3 精确开源日期口径不一（官方博客称 06 月发布，GitHub 仓库 2026-06-01 创建、07-01 最近推送；任务给定 06-15），报告统一记为 "2026-06 开源"。
- Ornith-1.0-397B HF 卡自称 "lightweight member... 单 GPU 部署"，但 serving recipe 实为 8×80GB TP8，卡内文案自相矛盾；以 recipe 为准记 8×80GB。

## END
