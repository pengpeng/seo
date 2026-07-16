---
task_id: nvidia
role: NVIDIA 本地 AI 加速芯片目录分析师
status: complete
sources_found: 9
---

## Sources
[1] NVIDIA Blackwell GeForce RTX 50 Series Opens New World of AI Computer Graphics | https://nvidianews.nvidia.com/news/nvidia-blackwell-geforce-rtx-50-series-opens-new-world-of-ai-computer-graphics | Source-Type: official | As Of: 2025-01 | Authority: 9/10
[2] GeForce RTX 5090 & GeForce RTX 5080 Out Now | https://www.nvidia.com/en-us/geforce/news/rtx-5090-5080-out-now/ | Source-Type: official | As Of: 2025-01 | Authority: 9/10
[3] NVIDIA RTX PRO 6000 Blackwell Series | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/ | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[4] GeForce RTX 5060 Desktop Family | https://www.nvidia.com/en-us/geforce/news/rtx-5060-desktop-family-laptop-5060-coming-soon/ | Source-Type: official | As Of: 2025-04 | Authority: 9/10
[5] NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-max-q/ | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[6] NVIDIA Puts Grace Blackwell on Every Desk | https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Puts-Grace-Blackwell-on-Every-Desk-and-at-Every-AI-Developers-Fingertips/default.aspx | Source-Type: official | As Of: 2025-01 | Authority: 9/10
[7] DGX Spark Hardware Overview | https://docs.nvidia.com/dgx/dgx-spark/hardware.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[8] NVIDIA RTX PRO 6000 Blackwell Workstation Edition | https://www.bhphotovideo.com/c/product/1895402-REG/nvidia_900_5g144_2200_000_rtx_pro_6000_blackwell.html | Source-Type: secondary-industry | As Of: 2026-07-15 | Authority: 6/10
[9] NVIDIA RTX PRO 6000 Blackwell Workstation Edition | https://www.microcenter.com/product/711665/nvidia-rtx-pro-6000-blackwell-workstation-edition-single-fan-ai-workstation-graphics-card-(oem) | Source-Type: secondary-industry | As Of: 2026-07-15 | Authority: 6/10

## Findings
- 当前 GeForce 桌面 Blackwell 系列含 RTX 5090、5080、5070 Ti、5070、5060 Ti、5060，均为 dGPU。[1][4]
- 本地 AI 主 slide 优先 RTX 5090；其余消费 SKU 容量较低，扩充清单时可列但不宜喧宾夺主。[1][2][4]
- RTX PRO 6000 Blackwell 有 Server、Workstation、Max-Q Workstation 三个正式版本；工作站两版适合本地 AI，Server 版不适合桌面 slide。[3][5]
- RTX PRO 6000 Blackwell 工作站版截至 2026-07 仍有官方购买入口和零售商品页，但库存因地区而异。[3][8][9]
- 正式芯片名是 NVIDIA GB10 Grace Blackwell Superchip；DGX Spark 是搭载它的整机，不应列为芯片名。[6][7]
- RTX 4090/3090 属旧代渠道或二手库存，不应放进“当前在售主力芯片”清单。[1][2]

## Deep Read Notes
### Source [1]: NVIDIA Blackwell GeForce RTX 50 Series
Key data: 官方列出 5090/5080/5070 Ti/5070，并确认 Blackwell 与 FP4 本地 AI 能力。
Key insight: RTX 5090 是当前 GeForce 旗舰；4090 只作为前代对照。
Useful for: dGPU 正式命名和代际取舍。

### Source [3]: NVIDIA RTX PRO 6000 Blackwell Series
Key data: 系列含 Server、Workstation、Max-Q Workstation 三版。
Key insight: Workstation/Max-Q 面向工作站，Server 面向被动散热机架。
Useful for: 工作站 GPU 选择及 Server 排除。

### Source [6]: NVIDIA Puts Grace Blackwell on Every Desk
Key data: GB10 集成 Blackwell GPU、20 核 Arm CPU 与统一内存。
Key insight: GB10 是 SoC 名；DGX Spark/Project DIGITS 是产品名。
Useful for: SoC 分类和命名。

## Gaps
- NVIDIA 没有全球实时在售 SKU 清单；“在售”由官方产品页、购买入口与零售页面综合判断。
- 若口径扩大到二手/旧渠道，4090/3090 仍有实用价值，但不属于当前主力世代。

## Slide recommendation
- dGPU: GeForce RTX 5090; RTX PRO 6000 Blackwell Workstation Edition。空间允许时补 RTX 5080。
- SoC: GB10 Grace Blackwell Superchip。
- 排除: DGX Spark（整机）、RTX PRO 6000 Server Edition、RTX 4090/3090（旧代）。

## END
