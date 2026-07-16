---
task_id: amd
role: AMD 本地 AI 加速芯片目录分析师
status: complete_with_fetch_limitations
sources_found: 11
---

## Sources
[1] AMD Radeon AI PRO R9700 | https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[2] AMD Radeon AI PRO Graphics | https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[3] Radeon AI PRO R9700 Workstations Arrive July 23 | https://www.amd.com/en/blogs/2025/amd-radeon-ai-pro-r9700-to-be-available-in-workstation.html | Source-Type: official | As Of: 2025-07 | Authority: 9/10
[4] AMD Radeon PRO Graphics for Professionals | https://www.amd.com/en/products/graphics/workstations.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[5] AMD Radeon PRO W7900 | https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[6] AMD Radeon RX 7900 XTX | https://www.amd.com/en/products/graphics/desktops/radeon/7000-series/amd-radeon-rx-7900xtx.html | Source-Type: official | As Of: 2022-12 / accessed 2026-07-15 | Authority: 10/10
[7] AMD Radeon RX 7000 Series | https://www.amd.com/en/products/graphics/desktops/radeon/7000-series.html | Source-Type: official | As Of: 2026-07-15 | Authority: 9/10
[8] AMD Ryzen AI Max+ 395 | https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[9] AMD Radeon AI PRO R9700S | https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700s.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[10] Use ROCm on Radeon GPUs | https://rocm.docs.amd.com/projects/radeon-ryzen/en/docs-6.0.2/index.html | Source-Type: official | As Of: ROCm 6.0 | Authority: 9/10
[11] AMD Ryzen Consumer Master Quick Reference Guide | https://www.amd.com/content/dam/amd/en/documents/partner-hub/ryzen/ryzen-consumer-master-quick-reference-competitive.pdf | Source-Type: official | As Of: 2026-07-15 | Authority: 9/10

## Findings
- Radeon AI PRO R9700 是 RDNA 4、Radeon AI PRO R9000 系列当前 AI-first dGPU，AMD 明确定位本地 AI 推理和开发。[1][2]
- R9700 自 2025 年进入工作站和独立显卡渠道，2026-07 仍在 AMD 当前 AI PRO 产品线。[2][3]
- R9700S 是被动散热企业版，不宜替代 R9700 成为桌面 slide 主项。[9]
- Radeon PRO W7900 仍有当前产品页，但已不是 AMD AI-first 主线；RX 7900 XTX 仍在目录但为 2022 游戏定位。[4][5][6][7]
- Ryzen AI Max+ 395 是正式非 PRO 名称，集成 Radeon 8060S 与 NPU，适合统一内存 SoC 主项。[8]
- Max+ 395 与 PRO 变体不应无说明并列成两个架构；通用 slide 选非 PRO 名称更简洁。[8]
- 当前 Ryzen AI Max 300 消费家族还包括 Ryzen AI Max 390 与 Ryzen AI Max 385，可用于扩展版芯片清单。[11]

## Deep Read Notes
### Source [1]: AMD Radeon AI PRO R9700
Key data: RDNA 4、AI PRO R9000 系列，官方定位 local AI inference/development。
Key insight: 这是 AMD 2026 本地 AI dGPU 主线，而非从图形用途间接推断。
Useful for: dGPU 首选和正式名称。
Retrieval note: 产品页 WebFetch 超时；依据搜索索引正文。

### Source [8]: AMD Ryzen AI Max+ 395
Key data: 16 核 Zen 5、Radeon 8060S、NPU、统一内存平台。
Key insight: 正式 SKU 名含“Max+”；适合 SoC 分类。
Useful for: SoC 推荐和命名消歧。
Retrieval note: 产品页 WebFetch 超时；依据搜索索引正文。

### Source [10]: Use ROCm on Radeon GPUs
Key data: 高端 Radeon 可运行 PyTorch、ONNX Runtime 和 ROCm。
Key insight: W7900/7900 XTX 有 AI 实用性，但不能证明它们仍是 2026 主力。
Useful for: 旧款排除的反向复核。

## Gaps
- AMD 多个产品页 WebFetch 超时；可访问性低于其他厂商，时效判断需降级。
- W7900/7900 XTX 有产品页不等于库存稳定；若强调“大容量仍可用”，W7900 可作为次级项。

## Slide recommendation
- dGPU: Radeon AI PRO R9700。
- SoC: Ryzen AI Max+ 395。
- 空间充足时可把 Radeon PRO W7900 放次级，但不建议让它代表 AMD 2026 主线。
- 排除: R9700S（服务器/被动散热）、RX 7900 XTX（旧代游戏主线）。

## END
