# AMD Radeon 高端独显（本地 AI）调研
> SEMrush US | 关键词数据待跑 | 来源：AMD 官方公开规格（快照，引用前需核实）

## 定位

AMD 高端消费独显在本地 LLM 上的最大卖点是**同价位更大显存**（RX 7900 XTX 24GB、RX 9070 XT 16GB），配合 ROCm / Vulkan 在 Ollama、llama.cpp 上可用。生态不如 CUDA 成熟，但对"省成本 + 大显存"的用户是重要选项——内容切入点是 ROCm 部署与"AMD 能不能跑本地大模型"。

## 规格与本地 LLM 能力（公开快照）

| 型号 | 系列 | 显存 | MSRP | 实际价 | 本地 LLM 能力 |
|------|------|------|------|--------|-------------|
| **RX 7900 XTX** | RDNA 3 | 24GB | $900 | $800（降价） | ⭐⭐⭐⭐⭐ 24GB 极强，70B Q4 |
| **RX 9070 XT** ⭐性价比 | RDNA 4 | 16GB | $600 | $750-800 | ⭐⭐⭐⭐ 30B Q4，16GB 大优势 |
| RX 9070 | RDNA 4 | 16GB | $550 | $680+ | ⭐⭐⭐⭐ 同上 |
| RX 7800 XT | RDNA 3 | 16GB | $400 | $380 | ⭐⭐⭐⭐ 30B Q4 |

> 市场：AMD Radeon 份额从约 10.6% 升至约 19.1%；RX 9070 XT 被称 2025 年度性价比最佳。

## 关键词数据（Semrush 待跑）

候选词（跑 `phrase_these` / `phrase_related` / `phrase_questions`）：
- 型号词：`rx 7900 xtx` / `rx 9070 xt` / `radeon 9070`
- 本地部署/引擎词：`amd gpu llm` / `7900 xtx llm` / `rocm ollama` / `run llm on amd gpu` / `amd stable diffusion`
- 对比/替代词：`7900 xtx vs 4090 llm` / `9070 xt vs 5070 ai` / `amd vs nvidia local llm` / `best amd gpu for ai`
- 问题词：`can amd gpu run ollama` / `does rocm work with llama.cpp`

## Olares 关联角度（待补）

- "AMD 也能跑本地大模型"：ROCm on Olares 部署教程（差异化，NVIDIA 内容已多）。
- 大显存性价比选卡（7900 XTX 24GB vs 4090）→ Olares 落地。

## 核心洞见（待补）

- 数据跑完后补：AMD/ROCm 词的量与 KD、CUDA 生态劣势对内容策略的影响、Olares 切入词。

---
*规格为公开快照，引用前需核实；关键词量/KD/CPC 待 Semrush 重跑（GPU 型号作 brand，见 [.cursor/skills/brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)）。*
