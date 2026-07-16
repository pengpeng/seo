---
task_id: audit
role: 反向复核员
status: complete
sources_found: 0
---

## Findings
- Critical: 市场图谱容易被误读为全部已被 Olares 同等支持；Apple GPU 当前不被加速，Intel/AMD/GB10 路径成熟度也不同。
- High: 产品页存在不等于全球稳定库存；在售应理解为官方当前目录 + 至少部分渠道可购的时点判断。
- High: 不能混用芯片/SKU、系列和整机名；DGX Spark、Mac Studio 必须删除。
- High: W7900 仍 AI-capable 且有目录，若题设是“仍在售”不能说它淘汰；只可因版面或时代代表性降级。
- Medium: 隐藏容量会模糊资源能力；主画面按用户要求不显示，但 references 必须说明能力不可等价。
- Medium: B50/B65、服务器被动散热 SKU 不适合代表高价值本地 AI 桌面主线。

## Recommended correction
- 主 slide 可以扩展型号，但必须采用“资源覆盖方向”而非“当前支持清单”的口径。
- dGPU 以 B70/B60、RTX 5090/RTX PRO 6000、R9700 为核心；B65/B50、RTX 5080、W7900 可作为次级补充。
- SoC 以 Series 3、GB10、Ryzen AI Max+ 395、M3 Ultra/M4 Max/M5 Max 为核心。

## Boundary text
Hardware examples represent currently offered AI-capable accelerator classes, not equivalent performance or uniform Olares support. Availability, memory architecture, software compatibility and Olares integration maturity vary by SKU and system; Apple GPU/Metal acceleration is not currently used by Olares AI applications.

## END
