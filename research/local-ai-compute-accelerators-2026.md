# 2026 本地 AI 加速计算芯片图谱：dGPU 与统一内存 SoC

> 研究日期: 2026-07-15 | 来源数: 24 | 字数: ~3200 | 模式: Standard | AS_OF: 2026-07-15 | 官方源占比: 83.3%

## 摘要

本报告为 Olares × Intel PPT 第 21 页的「加速计算资源」栏建立一份芯片级清单。目标不是比较绝对性能，也不是声明 Olares 已完整支持所有硬件，而是回答一个更窄的问题：截至 2026-07，Intel、NVIDIA、AMD、Apple 各有哪些仍属于当前产品目录或已正式发布、具备本地 AI 能力、适合出现在市场资源图谱中的 dGPU 或统一内存 SoC。

结论是：第一栏应继续采用 **dGPU 在上、SoC 在下** 的结构，并按公司 logo 聚合芯片名。dGPU 扩展清单为 Intel `Arc Pro B70 · B65 · B60 · B50`、NVIDIA `RTX 5090 · RTX 5080 · RTX PRO 6000 Blackwell`、AMD `Radeon AI PRO R9700 · Radeon PRO W7900`；SoC 清单为 Intel `Core Ultra X9 388H · X7 368H`、NVIDIA `GB10 Grace Blackwell`、AMD `Ryzen AI Max+ 395 · Max 390 · Max 385`、Apple `M3 Ultra · M4 Pro · M4 Max · M5 Pro · M5 Max`。[1][5][9][11][13][15][17][18][19][20][21][22]

这里的“当前”指厂商仍维护正式产品/规格页，且已有发布、销售或部分渠道证据；不等于所有地区稳定现货。清单按用户要求不显示容量，但容量、内存架构、软件兼容性和 Olares 集成成熟度差异仍然存在，不能把同一画面理解为性能或支持程度等价。[24]

## 一、方法与筛选口径

研究把候选分为两类：

1. **Discrete GPU**：独立 PCIe GPU，使用专用显存；包含消费旗舰与主动散热工作站 SKU。
2. **SoC / unified memory**：CPU、GPU、NPU 等位于同一平台并共享系统内存，或以统一内存作为本地 AI 的主要资源优势。

“当前目录或已发布”采用三层证据：官方当前产品目录或 ARK/规格页是第一层；正式上市公告是第二层；主流渠道商品页是第三层。只存在旧发布稿、二手库存或整机传闻的型号不进入主清单。厂商官方产品页仍在线并不自动等于库存稳定，因此 B65、W7900 等项只能被理解为“当前目录/部分渠道”，而不是全球持续现货。[1][4][7][8][17]

筛选还遵守四条版面规则：只列芯片或 accelerator SKU，不列整机；公司 logo 已表达厂商，文字不重复厂商名；不显示显存或统一内存数字；美国合作材料不加入国产 GPU/NPU。

**置信度: High**

**依据:** 24 个 approved 来源中 20 个为官方来源，覆盖 Intel、NVIDIA、AMD、Apple 当前产品页、规格和发布信息。

**反方解释:** “芯片名”并非完全同一命名层级：Arc Pro/RTX/Radeon 是显卡 SKU，Core Ultra Series 3 是处理器系列，GB10 和 Apple M 系列更接近 SoC。幻灯片表达的是可管理资源图谱，而不是半导体 die taxonomy。

## 二、dGPU：当前本地 AI 主线

### 2.1 Intel Arc Pro B-Series

Intel 当前 Arc Pro B-Series 工作站目录已经包含 B70、B65、B60、B50 四款；旧研究只收录 B60，已不适合 2026 版本的 Intel 合作材料。[1] B70 的 ARK 状态为 launched、发布日期 Q1 2026，并有官方 datasheet 与美国零售渠道证据，因此是清单中的首要型号。[2][3][8] B65 已进入正式目录并有 2026-03 datasheet，但广泛零售可购性证据弱于 B70；它可以在完整家族行中出现，但不应单独承担“主力在售”的叙事。[1][4][7]

因此 slide 采用 `Arc Pro B70 · B65 · B60 · B50`。这种写法对 Intel 受众更完整，也能展示 Olares 资源抽象面对的是一个持续扩展的家族，而不是单一型号。

### 2.2 NVIDIA GeForce 与 RTX PRO

NVIDIA 当前桌面 Blackwell GeForce 世代由 RTX 50 系列组成，RTX 5090 与 RTX 5080 均有正式发布和上市证据。[9][10] 对本地 AI 来说，RTX 5090 是消费旗舰；RTX 5080 的资源档位更低，但仍是当前 Blackwell 桌面 SKU，适合用户要求的扩展清单。

工作站端的 `RTX PRO 6000 Blackwell` 是当前高端专业主线。官方把它拆成 Server、Workstation、Max-Q Workstation 三个版本；主 slide 只保留家族名，references 明确其本地工作站语境，不把被动散热 Server Edition 当成个人桌面卡。[11][12]

因此 slide 采用 `RTX 5090 · RTX 5080 · RTX PRO 6000 Blackwell`。RTX 4090、3090 仍有二手或旧渠道价值，但属于上一代资源，不进入“当前主线”。

### 2.3 AMD Radeon

`Radeon AI PRO R9700` 是 AMD 当前 AI-first 工作站 dGPU，官方直接面向本地 AI 推理、开发和显存密集型负载，而不是从游戏用途间接推断其 AI 能力。[15][16] 它应成为 AMD dGPU 行的第一项。

`Radeon PRO W7900` 仍有 AMD 当前工作站产品页，资源能力也仍有现实价值，但属于 RDNA 3 较老一代，不再代表 AMD 的 AI-first 品牌主线。[17] 因用户希望“多列一些当前目录中的芯片”，W7900 可以作为第二项保留；其角色是专业补充，而不是 2026 新一代旗舰，2026-07 渠道库存未单独核验。

因此 slide 采用 `Radeon AI PRO R9700 · Radeon PRO W7900`。RX 7900 XTX 虽具备 ROCm/本地 AI 实用性，但主要是 2022 游戏产品，不进入这一页。

**置信度: High（型号存在与正式定位）；Medium（全球库存稳定性）**

**依据:** Intel/NVIDIA/AMD 均有当前官方目录；B70 另有零售证据，AMD 动态产品页的抓取可访问性相对较弱。[1][2][8][9][10][11][15][16][17]

**反方解释:** 如果主题改为“二手市场最值得跑本地 AI 的 GPU”，RTX 3090/4090、W7900、7900 XTX 的优先级会显著上升；本报告只服务“当前产品图谱”。

## 三、SoC 与统一内存平台

### 3.1 Intel Core Ultra Series 3

`Core Ultra Series 3` 是 Panther Lake 的正式系列名，而不是一颗单一芯片。官方 quick reference 显示，集成 Arc B390 的代表 SKU 包括 Core Ultra X9 388H、Core Ultra X7 368H/358H；Core Ultra 5 338H 集成 Arc B370。[5] Intel 于 2026-01 发布该系列，并明确以 AI PC 与 edge platform 定位，消费整机从 2026-01-27 起销售。[6]

用户希望展示“芯片名字”而不是产品名，因此 slide 不写 Panther Lake 整机，也不只写泛化系列；采用两个代表芯片 `Core Ultra X9 388H · Core Ultra X7 368H`。这比错误写法 `Core Ultra X9 386H` 更准确——386H 正式属于 Core Ultra 9，不带 X。

### 3.2 NVIDIA GB10 Grace Blackwell

NVIDIA 对该平台的正式芯片命名是 `GB10 Grace Blackwell Superchip`：它集成 Blackwell GPU、Grace Arm CPU 与 coherent unified memory，是 SoC，不是 dGPU。[13][14] `DGX Spark`、Project DIGITS 以及各 OEM 小型工作站都是搭载 GB10 的产品，不能与芯片名并列。

为了窄栏可读性，slide 写 `GB10 Grace Blackwell`，删除现稿里的 `/ DGX Spark`。

### 3.3 AMD Ryzen AI Max 300

`Ryzen AI Max+ 395` 是 AMD 当前统一内存 APU 的旗舰正式名称，集成 Radeon 8060S GPU 与 NPU。[18] AMD 官方家族资料还覆盖 `Ryzen AI Max 390` 与 `Ryzen AI Max 385`，三者构成比单一 395 更完整的当前芯片梯队。[22]

因此 slide 采用 `Ryzen AI Max+ 395 · Max 390 · Max 385`。不把 `Max+ PRO 395` 与消费线 395 并列，以免同一架构在窄栏中重复。

### 3.4 Apple Silicon

Apple 当前桌面高端仍由 M4 Max 与 M3 Ultra 跨代共存，M3 Ultra 并未因为代际编号较旧而停售；当前 Mac 产品矩阵也保留 M4 Pro。[20][21][23] M5 Pro 与 M5 Max 已于 2026-03 在笔记本产品线上销售，并明确面向专业本地 AI 工作流。[19] 基础 M4/M5 也能跑本地 AI，但不符合本页“高价值加速资源”的筛选重点。

因此 slide 采用 `M3 Ultra · M4 Pro · M4 Max · M5 Pro · M5 Max`。它表达 Apple Silicon 是重要的本地 AI 资源生态，不代表 Olares 当前使用 Apple GPU/Metal 加速；后者必须留在 references 作为支持成熟度边界。[24]

**置信度: High**

**依据:** 四家均有官方规格或当前销售页面；GB10 和 Apple 命名边界清晰，AMD 家族有官方 quick reference。[5][6][13][14][18][19][20][21][22]

**反方解释:** 隐藏容量后，统一内存 SoC 看起来像同一能力层级，但它们在带宽、可供 GPU 使用的内存、驱动生态和模型速度上差异很大。幻灯片只能表达资源类别与市场覆盖。

## 四、PPT 最终清单与命名规范

### dGPU（上）

- Intel logo：`Arc Pro B70 · B65 · B60 · B50`
- NVIDIA logo：`RTX 5090 · RTX 5080 · RTX PRO 6000 Blackwell`
- AMD logo：`Radeon AI PRO R9700 · Radeon PRO W7900`

### SoC · unified memory（下）

- Intel logo：`Core Ultra X9 388H · X7 368H`
- NVIDIA logo：`GB10 Grace Blackwell`
- AMD logo：`Ryzen AI Max+ 395 · Max 390 · Max 385`
- Apple logo：`M3 Ultra · M4 Pro · M4 Max · M5 Pro · M5 Max`

命名统一使用一个厂商 logo 加一串 SKU；正文不重复 Intel/NVIDIA/AMD/Apple；同厂商型号用 `·` 连接；`PRO` 保持全大写；删除所有容量、整机名和 `/` 别名表达。

## 五、核心争议（强制反向复核）

1. **清单会不会被理解为 Olares 已全部支持？** 会。资源图谱与当前产品能力不是一回事。Olares 的硬件与应用支持成熟度因厂商、运行时和具体应用而异，Apple GPU/Metal 当前不被 Olares AI 应用加速。因此 main slide 只展示市场资源方向，不是兼容清单；具体支持必须另以 Olares 官方资料核验。[24]
2. **产品页是否等于稳定在售？** 不等于。B65、B50/B60、W7900 的证据强度低于 B70、RTX 5090、R9700。报告用“当前目录/部分渠道”而非“全球稳定现货”。
3. **不显示容量是否误导？** 有风险。B50、B70、RTX PRO 6000、GB10、M3 Ultra 处在完全不同的资源档；本页不做性能比较，容量和可跑模型规模必须在后续页或 notes 中解释。
4. **为何保留 W7900、B50 等次级型号？** 因用户本轮目标是填充市场图谱、展示仍销售的芯片，而非只选每家旗舰。它们的存在提高生态覆盖度，但不应在口播里被称为 2026 主力。

## 六、关键发现

- **发现 1：** Intel dGPU 目录必须从“B60 only”更新为 B70/B65/B60/B50 完整家族。[1][2][3][4]
- **发现 2：** GB10 是芯片，DGX Spark 是整机；资源栏应只写 GB10 Grace Blackwell。[13][14]
- **发现 3：** 当前市场已经形成三条资源路线：PCIe dGPU、x86 统一内存 APU/AI PC SoC、Arm/Apple 统一内存 SoC；这个分类描述市场资源路线，不代表 Olares 当前已统一管理这些硬件。
- **发现 4：** 面向 Intel 的 slide 采用扩展清单是合理的，但 Olares 当前支持成熟度必须与市场资源图谱明确解耦。

## 局限性与未来方向

### 本研究局限

- 厂商没有全球实时库存 API；“在售”是 2026-07 时点的目录与渠道判断。
- AMD 部分动态产品页 WebFetch 超时，虽然有官方索引正文和既有研究交叉，仍降低了库存时效判断置信度。
- 本报告未比较 tokens/s、功耗、价格或单位成本；这些指标不能从型号数量推导。
- 只研究 Intel、NVIDIA、AMD、Apple，按 Intel 合作材料边界未纳入国产 GPU/NPU。

### 未来方向

1. 每季度复核 Intel Arc Pro B 系、Apple M 系和 NVIDIA/AMD 工作站产品页。
2. 在下一轮内容中按“当前 Olares 支持 / 目标适配 / 市场资源”三种状态分层。
3. 若该 slide 后续加入容量或性能，再单独建立统一的容量、带宽、可用内存和 runtime 口径。

## 参考文献

[1] Intel. “Intel Arc Pro B-Series overview.” Source-Type: official. As Of: 2026-07-15. https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html  
[2] Intel. “Intel Arc Pro B70 ARK.” Source-Type: official. As Of: Q1 2026. https://www.intel.com/content/www/us/en/products/sku/245797/intel-arc-pro-b70-graphics/specifications.html  
[3] Intel. “Intel Arc Pro B70 datasheet.” Source-Type: official. As Of: 2026-03. https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf  
[4] Intel. “Intel Arc Pro B65 datasheet.” Source-Type: official. As Of: 2026-03. https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b65-gpu.pdf  
[5] Intel. “Core Ultra Series 3 Quick Reference Guide.” Source-Type: official. As Of: 2026-01-05. https://cdrdv2.intel.com/v1/dl/getContent/871380?fileName=Intel+Core+Ultra+Series+3+Processors+-+Quick+Reference+Guide+v1.pdf&view=true  
[6] Intel. “Core Ultra Series 3 launch.” Source-Type: official. As Of: 2026-01-05. https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a  
[7] ServeTheHome. “Intel Arc Pro B70/B65 launch.” Source-Type: secondary-industry. As Of: 2026. https://www.servethehome.com/intel-announces-arc-pro-b70-and-b65-video-cards-big-battlemage-brings-big-memory-for-ai-workstations/  
[8] Micro Center. “ASRock Intel Arc Pro B70 listing.” Source-Type: secondary-industry. As Of: 2026-07-15. https://www.microcenter.com/product/708790/asrock-intel-arc-pro-b70-creator-single-fan-32gb-gddr6-pcie-50-graphics-card  
[9] NVIDIA. “Blackwell GeForce RTX 50 Series.” Source-Type: official. As Of: 2025-01. https://nvidianews.nvidia.com/news/nvidia-blackwell-geforce-rtx-50-series-opens-new-world-of-ai-computer-graphics  
[10] NVIDIA. “RTX 5090 and 5080 availability.” Source-Type: official. As Of: 2025-01. https://www.nvidia.com/en-us/geforce/news/rtx-5090-5080-out-now/  
[11] NVIDIA. “RTX PRO 6000 Blackwell Series.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/  
[12] NVIDIA. “RTX PRO 6000 Blackwell Max-Q.” Source-Type: official. As Of: 2026-07-15. https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-max-q/  
[13] NVIDIA. “Grace Blackwell on every desk.” Source-Type: official. As Of: 2025-01. https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Puts-Grace-Blackwell-on-Every-Desk-and-at-Every-AI-Developers-Fingertips/default.aspx  
[14] NVIDIA. “DGX Spark hardware overview.” Source-Type: official. As Of: 2026-07-15. https://docs.nvidia.com/dgx/dgx-spark/hardware.html  
[15] AMD. “Radeon AI PRO R9700.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html  
[16] AMD. “Radeon AI PRO Graphics.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro.html  
[17] AMD. “Radeon PRO W7900.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html  
[18] AMD. “Ryzen AI Max+ 395.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-plus-395.html  
[19] Apple. “M5 Pro and M5 Max.” Source-Type: official. As Of: 2026-03. https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/  
[20] Apple. “Current Mac Studio lineup.” Source-Type: official. As Of: 2026-07-15. https://www.apple.com/mac-studio/  
[21] Apple. “M4 Pro and M4 Max.” Source-Type: official. As Of: 2024-10. https://www.apple.com/newsroom/2024/10/apple-introduces-m4-pro-and-m4-max/  
[22] AMD. “Ryzen Consumer Master Quick Reference Guide.” Source-Type: official. As Of: 2026-07-15. https://www.amd.com/content/dam/amd/en/documents/partner-hub/ryzen/ryzen-consumer-master-quick-reference-competitive.pdf
[23] Apple. “Current Mac lineup.” Source-Type: official. As Of: 2026-07-15. https://www.apple.com/mac/mac-does-that/  
[24] Olares. “Governed product and platform reference.” Source-Type: internal-governed. As Of: 2026-07. /Users/pengpeng/seo/basic/olares.md
