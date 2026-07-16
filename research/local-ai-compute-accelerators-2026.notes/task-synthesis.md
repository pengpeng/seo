---
task_id: synthesis
role: 芯片目录综合员
status: complete
sources_found: 16
---

## Findings
- 20% 窄栏必须按 dGPU / SoC 两组、每组按厂商 logo 聚合，且正文不重复厂商名。
- 紧凑 dGPU 建议：Intel Arc Pro B70/B60；NVIDIA RTX 5090/RTX PRO 6000 Blackwell；AMD Radeon AI PRO R9700。
- 用户要求“多列一些当前在售芯片”时可扩为：Intel B70/B65/B60/B50；NVIDIA RTX 5090/5080/RTX PRO 6000；AMD R9700/W7900。
- SoC 紧凑建议：Intel Core Ultra Series 3；NVIDIA GB10 Grace Blackwell；AMD Ryzen AI Max+ 395；Apple M3 Ultra/M4 Max/M5 Max。
- 扩展 SoC 可补 Intel X9 388H/X7 368H、AMD Max 390/385、Apple M4 Pro/M5 Pro。
- DGX Spark、Mac Studio、Mac mini、Framework Desktop 都是整机名，不进芯片清单。
- 命名统一：logo 已表达厂商；保留 Arc Pro/RTX PRO/Radeon/Ryzen/Core Ultra 前缀；PRO 大写；同厂商 SKU 用“·”串联。

## Source mapping
- Intel Arc Pro B-Series: task-intel [1]-[4]。
- Intel Core Ultra Series 3: task-intel [5][6]。
- NVIDIA RTX 50 / RTX PRO: task-nvidia [1]-[5]。
- NVIDIA GB10: task-nvidia [6][7]。
- AMD R9700/W7900: task-amd [1]-[5]。
- AMD Ryzen AI Max+ 395: task-amd [8]。
- Apple M3 Ultra/M4/M5: task-apple [1]-[5]。

## Gaps / risks
- 清单表达市场覆盖方向，不等于性能相同或 Olares 支持成熟度相同。
- B65 渠道证据弱于 B70；W7900 虽仍在目录但不是 AMD AI-first 主线。
- 隐藏容量后不能暗示能力等价；容量差异留 references。
- Apple GPU/Metal 当前不被 Olares AI 应用加速；Apple 仅代表资源生态目标。
- GB10 的 Olares 完整识别/调度仍不能表达为当前成熟能力。

## END
