# RTX 50 系（Blackwell 消费卡）本地 AI GPU 调研
> SEMrush US | 关键词数据待跑 | 来源：NVIDIA 官方公开规格（快照，引用前需核实）

## 定位

NVIDIA 2025-2026 年的当前购买主力，Blackwell 架构、GDDR7。对本地 LLM 而言显存是硬门槛：5090（32GB）是最强消费卡，5080/5070 Ti（16GB）够跑 30B，5060（8GB）鸡肋。这批用户"已买卡、找场景"，是 Olares OS 的高意图人群。

## 规格与本地 LLM 能力（公开快照）

| 型号 | 显存 | MSRP | 实际成交价（2026/7） | 本地 LLM 能力 |
|------|------|------|-----------------|-------------|
| **RTX 5090** | 32GB GDDR7 | $2,499 | $3,500-5,000（缺货溢价） | ⭐⭐⭐⭐⭐ 最强消费卡，70B Q4 流畅 |
| RTX 5080 | 16GB GDDR7 | $999 | $1,200+ | ⭐⭐⭐⭐ 30B 流畅 |
| RTX 5070 Ti | 16GB GDDR7 | $749 | $830+ | ⭐⭐⭐⭐ 30B 流畅 |
| RTX 5070 ⭐销量最高 | 12GB GDDR7 | $599 | 约 MSRP | ⭐⭐⭐ 13B 流畅 |
| RTX 5060 Ti | 16GB GDDR7 | ~$449 | 约 MSRP | ⭐⭐⭐⭐ 30B Q4 |
| RTX 5060 ⭐出货量第一 | 8GB GDDR7 | $319 | 约 MSRP | ⭐ 8GB 偏小，仅 7B |

> 市场：NVIDIA RTX 系列 Q2 2025 出货 1090 万张（市占率约 94%）；5070 已进 Steam 前 5，5060 出货量冠军但显存受限。

## 关键词数据（Semrush 待跑）

候选词（跑 `phrase_these` / `phrase_related` / `phrase_questions`）：
- 型号词：`rtx 5090` / `rtx 5080` / `rtx 5070` / `5090` / `rtx 5060 ti`
- 本地部署/引擎词：`rtx 5090 llm` / `rtx 5090 local ai` / `rtx 5090 ollama` / `rtx 5090 vram` / `best rtx 50 for llm`
- 对比/替代词：`5090 vs 4090` / `5080 vs 5070 ti llm` / `rtx 5090 vs mac studio` / `rtx 5090 vs dgx spark`
- 参考锚点（nvidia-dgx.md 已见）：`5090`（74,000/mo，KD≈37）、`rtx 5090`（110,000/mo，KD≈46）、`5080`/`5070`（49,500/mo，KD≈41）——型号词 KD 偏低，内容层竞争不高。

## Olares 关联角度（待补）

- "在 RTX 5090 上把本地大模型变成随处可访问的私有 AI 服务"——OS 层叙事，而非再买硬件。
- 5060/5070 显存不够的教育内容（量化 / 显存需求 / 模型选择）导流。

## 核心洞见（待补）

- 数据跑完后补：型号词 KD 洼地是否可截获、`X vs Olares One/OS` 机会、5090 高意图用户转化路径、GEO 抢发窗口。

---
*规格为公开快照，引用前需核实；关键词量/KD/CPC 待 Semrush 重跑（GPU 型号作 brand，见 [.cursor/skills/brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)）。*
