---
unit: dgpu-24gb-plus
title: ≥24GB 独显（本地 AI 可用 dGPU 分层）研究笔记
as_of: 2026-07-05
mode: Lightweight
researcher: deep-research subagent
sources_total: 13
official_ratio: ~31%
---

# dgpu-24gb-plus — 研究笔记（task-01）

## Sources

复用的现有内部报告（不覆写，作 carrier-model 行）：
- R-A. /Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-4090.md（RTX 4090 24GB）
- R-B. /Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-3090.md（RTX 3090 / 3090 Ti 24GB，双卡 48GB）
- R-C. /Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-50-series.md（RTX 5090 32GB 等）
- R-D. /Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-pro-6000.md（RTX PRO 6000 Blackwell 96GB；提及 RTX 6000 Ada 48GB）
- R-E. /Users/pengpeng/seo/directions/hardware/reports/04-dgpu/amd/radeon-high-end.md（RX 7900 XTX 24GB 等）
- R-F. /Users/pengpeng/seo/directions/hardware/reports/04-dgpu/intel/intel-arc.md（Arc Pro B60 24GB / Dual 48GB）

外部来源（WebSearch/WebFetch，2026-07-05）：
- [1] Gizchina, "Nvidia RTX Pro 6000 Blackwell Price Jumps to $13,250" — https://www.gizchina.com/nvidia/nvidia-rtx-pro-6000-blackwell-price-jumps-to-13250-55-above-launch-price
- [2] MLQ News, "Nvidia Raises RTX Pro 6000 Blackwell MSRP to $13,250" — https://mlq.ai/news/nvidia-raises-rtx-pro-6000-blackwell-msrp-to-13250-a-55-hike-in-one-year/
- [3] AMD 官方, "Radeon AI PRO Graphics"（R9700 32GB，MSRP $1,299）— https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro.html
- [4] Phoronix, "AMD Radeon AI PRO R9700 Linux Performance"（$1299、32GB GDDR6、RDNA4）— https://www.phoronix.com/review/amd-radeon-ai-pro-r9700
- [5] Wccftech, "AMD Radeon AI PRO R9700 GPU…"（W7900 48GB $3,999 launch）— https://wccftech.com/amd-radeon-ai-pro-r9700-gpu-4x-more-tops-2x-ai-performance-vs-radeon-pro-w7800/
- [6] ThePCEnthusiast, "SPARKLE Launches Intel Arc Pro B60"（24GB $799，2026-01-12 上市）— https://thepcenthusiast.com/sparkle-launches-intel-arc-pro-b60-24gb-graphics-card/
- [7] VideoCardz, "MAXSUN Arc Pro B60 Dual…48GB memory"（2×24GB 双 GPU，非单芯 48GB）— https://videocardz.com/newz/maxsun-arc-pro-b60-dual-arrives-to-first-users-two-battlemage-gpus-on-one-board-and-48gb-memory
- [8] Every Local AI, "NVIDIA RTX A6000 – 48GB Ampere Pro GPU"（MSRP $4,650，二手 $2,500-3,500）— https://everylocalai.com/hardware/nvidia-a6000
- [9] GPU101, "RTX A6000 — The Most Powerful Single-GPU Workstation Card"（二手 $1,200-2,000）— https://gpu101.com/rtx-a6000-the-most-powerful-single-gpu-workstation-card/
- [10] CraftRigs, "How Much VRAM to Run 70B Models"（Q4_K_M ≈40GB）— https://craftrigs.com/guides/how-much-vram-to-run-70b-models/
- [11] InsiderLLM, "Running 70B Models Locally — Exact VRAM by Quantization"（Q4_K_M ~43GB 含开销）— https://insiderllm.com/guides/running-70b-models-locally-vram-guide/
- [12] Olares One 官方 — https://one.olares.com/
- [13] Olares 官方文档（系统要求 x86-64 Linux）— https://docs.olares.com/

## Findings（≤10，每条带 [n]）

1. 本地 AI 显存分水岭：70B 模型 Q4_K_M 权重约 35GB、含 KV/开销约 40–43GB [10][11]；因此单卡 24GB 无法把 70B Q4 全放显存，需 offload 到内存或降到 Q2/Q3（速度、质量双降）[10][R-A]。→ "24GB 起步、48GB 舒适、96GB 富余"的分层成立。
2. NVIDIA 消费旗舰显存阶梯：3090/3090 Ti/4090 = 24GB，5090 = 32GB（GDDR7），32GB 才能把 70B Q4 更从容地放进单卡 [R-A][R-B][R-C][10]。
3. RTX PRO 6000 Blackwell 是唯一 96GB GDDR7 桌面独显，官方标价已涨到 $13,250（较 2025-03 上市 $8,565 涨 55%），第三方零售约 $10,875–$12,000 [1][2]。
4. RTX 6000 Ada（48GB GDDR6）为上代工作站卡，上市价 $6,799，二手约 $3,500–5,000 [2][8][9]。
5. RTX A6000（48GB GDDR6 ECC，Ampere）是 2026 年"最便宜的 48GB 专业卡"：MSRP $4,650，二手 $1,200–2,800，双卡 NVLink 可池化 96GB [8][9]。现有内部报告未专门覆盖，建议并入工作站族。
6. AMD Radeon AI PRO R9700（32GB GDDR6，RDNA4）2025 Q3 上市，MSRP $1,299，官方定位"本地 AI 最优显存缓冲"、主打 ROCm [3][4]。是"$1500 以下显存最大的工作站/消费卡" [3]。现有 radeon-high-end.md 未收录，建议补。
7. AMD Radeon PRO W7900（48GB GDDR6，RDNA3）上市价 $3,999，街价约 $3,500–3,800，384-bit、864 GB/s，显存缓冲比 R9700 大 [5]。
8. Intel Arc Pro B60（24GB GDDR6）2026-01-12 由 Sparkle/Maxsun 零售，MSRP $799，主打 AI 推理/工作站；每 GB 显存最便宜 [6]。
9. "Arc Pro B60 Dual 48GB"实为一板双 GPU（2×24GB，各 PCIe 5.0 x8），系统识别为两张卡，价格 ¥/£ 波动大（约 $1,200 中国 – $2,700 国际）[7]。→ 不是真正单芯 48GB，内容需说清。
10. Olares 适配锚点：大 dGPU 天然落在 x86 台式机 → 走 Olares x86-64 裸机 ISO/script（Ubuntu 22.04-25.04/Debian 12-13）高契合 [13]。GPU 加速：NVIDIA 最成熟（全 app）；AMD（ROCm）/Intel Arc 亦被加速，成熟度随版本、CUDA-only app 覆盖较窄（逐条以 docs/GitHub 复核）。（Olares 本身跨平台，不限 x86。）Olares One $3,999，RTX 5090 Mobile 24GB / Core Ultra 9 275HX / 96GB DDR5 [12]。

## Deep Read Notes

- RTX PRO 6000 涨价机制 [1][2]：96GB GDDR7 在 AI 抢内存的环境下成本+需求双推，官方 $13,250、PNY 板 $11,359、Empowered $11,999、Esaitech $10,875；单位显存价 ≈$138/GB，反而略低于 RTX 6000 Ada 的 $142/GB。启示：96GB 单卡叙事的对手是"两块二手 A6000 池化 96GB（$5–6K）"和 Olares One $3,999。
- A6000 vs 6000 Ada [8][9]：同为 48GB，A6000（Ampere）二手 $1.2–2.8K 远便宜于 6000 Ada（Ada）$3.5–5K；A6000 保留 NVLink，双卡 96GB；6000 Ada、PRO 6000 Blackwell 已取消 NVLink。→ "最便宜 48GB / 最便宜 96GB 池化"是强内容钩子。
- 24GB 现实 [10][11]：Q4_K_M 70B 需 ~40–43GB；24GB 只能 offload（1–5 tok/s）或 Q2（~17.5GB，全显存但质量掉 ~30%）。厂商/社区常说"24GB 能跑 70B"实为带 offload 或低量化——须诚实标注。

## Gaps（含 ≥1 反向复核 / counter-claim）

- G1（counter-claim）：内部报告与部分厂商口径称"24GB 单卡跑 70B Q4"，但独立来源显示 70B Q4_K_M 需 ~40–43GB，24GB 单卡实为 offload 或降量化 [10][11]。→ 分层表按"24GB=70B 需 offload/降量化；48GB=70B 舒适；96GB=120B+"更严谨。本报告采用后者。
- G2：AMD ROCm、Intel IPEX-LLM/oneAPI 的"开箱可用度"缺独立横评；R9700/B60 的实际本地推理易用性仅有厂商/单篇评测口径 [3][4][6]，生态成熟度存疑。
- G3：Arc Pro B60 Dual 的"48GB"是 2×24GB 双 GPU，需应用支持张量/层切分才能当 48GB 用 [7]；单模型能否透明用满 48GB 缺证据。
- G4：各卡"街价"波动极大（缺货溢价、二手、地区差），报告价格为区间快照，引用前需以当时零售/二手行情复核。
- G5：Olares OS 对具体 dGPU（尤其 AMD/Intel）的 GPU passthrough / 驱动支持矩阵未在本轮核实，仅确认 x86-64 Linux 系统要求 [13]。
