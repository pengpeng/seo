---
slug: nvidia-gb10
task: task-01
role: AI 硬件生态图谱分析师
as_of: 2026-07-05
mode: Standard
queries:
  - "NVIDIA GB10 Grace Blackwell superchip DGX Spark specs 128GB unified memory 2026"
  - "GB10 DGX Spark OEM partners Asus Dell HP Lenovo MSI Gigabyte Acer list 2026"
  - "NVIDIA N1X N1 SoC MediaTek desktop consumer chip laptop 2026 rumor specs"
  - "Asus Ascent GX10 / Dell Pro Max GB10 / HP ZGX Nano G1n / MSI EdgeXpert MS-C931 price 2026"
  - "Olares OS system requirements Ubuntu 24.04 x86-64 arm64 support installation"
  - "DGX Spark run Ubuntu Linux instead of DGX OS ARM64 install own OS"
---

## Sources

[1] https://docs.nvidia.com/dgx/dgx-spark/hardware.html — DGX Spark 硬件规格官方文档 — official — As Of 2026 — 权威 10
[2] https://www.nvidia.com/en-us/products/workstations/dgx-spark/ — DGX Spark 官方产品页/规格表 — official — As Of 2026 — 权威 10
[3] https://www.backend.ai/blog/2026-02-is-dgx-spark-actually-a-blackwell — Lablup 拆解 GB10（多die/MediaTek/SM121） — secondary-industry — As Of 2026-02 — 权威 7
[4] https://learn.arm.com/learning-paths/laptops-and-desktops/dgx_spark_llamacpp/1_gb10_introduction/ — Arm 官方学习路径：GB10 架构 — official — As Of 2026 — 权威 8
[5] https://newsroom.arm.com/blog/arm-powered-nvidia-dgx-spark-ai-workstations — Arm Newsroom：8 家 OEM 机型清单 — official — As Of 2026 — 权威 8
[6] https://www.edge-ai-vision.com/2025/05/nvidia-launches-ai-first-dgx-personal-computing-systems-with-global-computer-makers/ — NVIDIA 新闻稿转载（Computex 2025 OEM 名单/上市） — official(press) — As Of 2025-05 — 权威 8
[7] https://www.banandre.com/blog/ai-mini-workstations-standardized-dgx-clones — 8 台 GB10 clone 型号/尺寸对比 — community — As Of 2026-05 — 权威 5
[8] https://forums.developer.nvidia.com/t/mixing-different-gb10-systems-in-a-dgx-spark-cluster-nvidia-lenovo-anyone-tried/367711 — NVIDIA 论坛：跨 OEM 集群实测（固件差异/可用内存 119 vs 121GB） — community — As Of 2026 — 权威 6
[9] https://insiderllm.com/guides/gb10-boxes-compared/ — GB10 全阵营价格表 + 带宽/tok 现实 + $4,699 涨价 — secondary-industry — As Of 2026-06 — 权威 6
[10] https://www.notebookcheck.net/Nvidia-N1X-officially-confirmed-to-arrive-as-the-RTX-Spark.1312010.0.html — N1X 官方定名 RTX Spark + 承载笔记本清单 — journalism — As Of 2026-06 — 权威 7
[11] https://liliputing.com/nvidias-n1-and-n1x-chips-will-bring-discrete-class-graphics-and-ai-to-windows-on-arm-laptops/ — N1X/N1 四档 SKU 规格泄露表 — journalism — As Of 2026 — 权威 6
[12] https://wccftech.com/roundup/nvidia-laptop-chips/ — N1X/N1 综述（3nm/20 核/120W TDP/6144 CUDA） — journalism — As Of 2026 — 权威 6
[13] https://tech-insider.org/nvidia-rtx-spark-superchip-2026/ — RTX Spark 三档定价（$1,799/$2,899） — secondary-industry — As Of 2026 — 权威 5
[14] https://sg.store.asus.com/asus-ascent-gx10-1tb-gx10-gg0007bn.html — ASUS 官方零售页（SKU/ARM v9.2/128G/1TB） — official(retail) — As Of 2026 — 权威 8
[15] https://www.olares.com/docs/manual/get-started/install-linux-iso — Olares 官方安装文档：x86-64 required, ARM not supported — official — As Of 2026 — 权威 10
[16] https://www.olares.com/docs/manual/help/installation.html — Olares 官方 FAQ：平台支持 — official — As Of 2026 — 权威 9
[17] https://github.com/timothystewart6/ubuntu-gb10 — 社区在 GB10 上装纯 Ubuntu 24.04 arm64 — community — As Of 2026 — 权威 6
[18] https://technotim.com/posts/ubuntu-gb10/ — 在 DGX Spark/GX10 装 Ubuntu Server arm64 教程 — community — As Of 2026 — 权威 6
[19] https://docs.nvidia.com/dgx/dgx-os-7-user-guide/installing_on_ubuntu.html — DGX OS 7 = 定制 Ubuntu 24.04（ARM64），可装于 vanilla Ubuntu — official — As Of 2026 — 权威 9
[20] https://one.olares.com/ — Olares One 官方页（价格/配置，用户提供） — official — As Of 2026 — 权威 9

## Findings

1. GB10 = NVIDIA + MediaTek 合造的多-die SoC：TSMC 3nm ARM CPU die（10×Cortex-X925 + 10×Cortex-A725，共 20 核 Armv9.2）经 NVLink-C2C 连 Blackwell GPU die，128GB LPDDR5x 统一内存共享 [1][3][4]。
2. GB10 关键规格：Blackwell GPU 48 SM / 6,144 CUDA / 5th-gen Tensor，1 PFLOP 稀疏 FP4，128GB LPDDR5x @ 273 GB/s（256-bit），4TB NVMe，ConnectX-7 200Gbps，GB10 SoC TDP 140W [1][2][9]。
3. 承载 128GB 统一内存可本地放下 ~200B 参数模型；双机经 ConnectX 可跑到 ~405B [2][5]。这是"桌面上能装下整模型"的稀缺能力 [3]。
4. 现实性能：273 GB/s 带宽远低于独显（3090 ~936、M3 Ultra ~819），token 生成受带宽限制——70B FP8 约 2-3 tok/s，属批处理/agent 编排可用、交互式聊天吃力 [9]。且存在软件层 ~100W GPU 功耗封顶（Carmack 指出，非散热限制）[9]。
5. 官方 OEM 阵营（Arm Newsroom + NVIDIA 新闻稿）：Acer Veriton GN100、Asus Ascent GX10、Dell Pro Max with GB10、Gigabyte AI TOP ATOM、HP ZGX Nano AI Station、Lenovo ThinkStation PGX、MSI EdgeXpert，加 NVIDIA DGX Spark Founders Edition，共 8 款 [5][6][7]。
6. 8 款是"同芯 clone"：同 150×150mm、同 GB10、性能差异可忽略；差异在机箱/散热/NVMe 代际/保修 [7][9]。仅 DGX Spark FE 用 Gen5 NVMe（~13GB/s vs OEM Gen4 ~7GB/s），冷加载快约 25% [9]。
7. US 直营价（2026-06）：DGX Spark FE $4,699（2026-02-23 由 $3,999 涨 18%，内存供给紧张）；MSI EdgeXpert MS-C931 $2,999(1TB)/$3,999(4TB)；Acer GN100 $2,999；ASUS GX10 ~$3,088(1TB)/$4,150(4TB)；Dell Pro Max ~$3,699(2TB) [9]。ASUS 官方 SKU：GX10-GG0007BN(1TB)、GG0032BN(4TB) [14]。
8. 全阵营均跑 NVIDIA DGX OS（基于 Ubuntu，arm64），无 Windows；DGX OS 7 本身即定制 Ubuntu 24.04（ARM64）[1][9][19]。跨 OEM 集群可混跑但固件节奏不同步（如 Gigabyte 固件落后）；实测 Gigabyte ATOM 可用内存 119GB vs 其它 121GB [8]。
9. GB10 是 ARM64 平台：社区已验证可弃 DGX OS、装纯 Ubuntu Server 24.04 arm64 + NVIDIA arm64 驱动栈（须用 Canonical 预签名内核模块，避开 Secure Boot / DKMS 坑）[17][18]。即"这台机器能跑普通 arm64 Linux"。
10. **纠正（2026-07-05 复核 docs.olares.com）**："ARM not supported" 只在**裸机 ISO 安装器**页 [15]；Olares 经 **Linux script** 支持 ARM Linux（官方树莓派 4B/5 路径用同一 script）[16]，并支持 macOS/Windows。→ 在 GB10（arm64 + DGX OS/Ubuntu arm64）上经 script 装 Olares **有望可行**；且 GB10 的 Blackwell GPU 落在 Olares 支持架构表（GB✓）。仅 arm64 script 在 DGX OS 的实测 + 整合 Blackwell 识别未官宣，标 [unverified]。不再判"不支持"。
11. N1X 已由 NVIDIA 官方定名 **RTX Spark**（Computex 2026 发布，Fall 2026 上市），面向 Windows on Arm 笔记本；GPU 6,144 CUDA、20 核 CPU（MediaTek 定制），支持 DLSS 4.5 [10][12]。这与旧报告把 "RTX Spark" 当作 GB10 mini-PC/笔记本的用法**冲突**——存在命名混淆。
12. 泄露的 N1X/N1 四档：N1X(20核/48SM/6144CUDA/45-80W)、N1X(18核/40SM/5120)、N1(12核/20SM/2560)、N1(10核/16SM/2048/18-45W)[11]；坊间定价 N1 ~$1,799、N1X ~$2,899（非 NVIDIA 官方价，PC 厂检查）[13]。承载笔记本传闻：Asus ProArt P14/P15、Dell XPS 16、HP OmniBook X14/Ultra16、Lenovo Yoga Pro 9n、Microsoft Surface Laptop Ultra、MSI Prestige N16 Flip AI [10]。

## Deep Read Notes

### InsiderLLM「GB10 Boxes Compared」[9]（DEEP）
- 全阵营同芯：20 ARM v9.2 核（10P+10E）、Blackwell 6,144 CUDA + 192 5th-gen Tensor、128GB LPDDR5X @273GB/s、~1 PFLOP 稀疏 FP4、140W TDP、ConnectX-7 200GbE、DGX OS（无 Windows）。
- 价格表（US, 2026-06）：FE $4,699（4TB Gen5）；ASUS GX10 ~$3,088(1TB)/~$4,150(4TB)；Dell Pro Max ~$3,699(2TB)；MSI MS-C931 ~$2,999(1TB)/~$3,999(4TB)；Acer GN100 $2,999(US)/£3,999(UK)；Gigabyte ATOM、Lenovo 价随地区。
- 三个决策数字：能装多大模型 / 要多快（带宽绑定）/ 需要什么软件栈（CUDA vs Windows-AMD vs macOS-MLX）。
- 反面：若工作负载 ≤24GB，二手 3090（$900-1,200）更快更便宜；128GB 统一内存档只对"装不进 24GB"的负载有意义。
- 澄清：HP Z2 Mini G1a 是 Strix Halo（AMD Ryzen AI Max+）不是 GB10——2026 多篇对比文误分类；HP 的 GB10 盒子是 ZGX Nano。
- 竞品档：Strix Halo（Ryzen AI Max+ 395）128GB 统一内存、96GB 可作 VRAM、~256GB/s、支持 Windows、$1,499-$3,999——GB10 无 Windows 时的主要平替。Mac Studio M3 Ultra 128GB ~819GB/s，$5,000-6,000。

### Techno Tim / ubuntu-gb10 [17][18]（DEEP）
- 出厂装 DGX OS（NVIDIA 托管的 Ubuntu 桌面镜像）；可改装 Ubuntu Server 24.04 **arm64**（非 amd64）——必须用 arm64 ISO 与 NVIDIA arm64 仓库。
- 驱动坑：DGX Spark 开 Secure Boot，DKMS 自编模块签名不被信任 → 用 Canonical 为 `linux-nvidia` flavour 预签名的 `linux-modules-nvidia-*-open` 包 [al-engr 佐证]。
- 结论：GB10 能跑标准 arm64 Linux；由于 Olares 经 script 支持 ARM Linux（树莓派路径），在 GB10 arm64 上装 Olares 有望可行，仅 DGX OS 实测未官宣 [unverified]。（旧结论"Olares 要求 x86-64"是把裸机 ISO 误当全部路径。）

## Gaps

- **未找到**：Olares 官方对 GB10/DGX Spark 或 arm64 的任何专门支持声明；GitHub beclab/Olares 是否有 arm64 构建分支未核（须直接查 repo，未证实前 [unverified]）。
- **未找到**：HP ZGX Nano G1n、Lenovo ThinkStation PGX、Gigabyte AI TOP ATOM 的稳定 US MSRP（多为企业报价/地区差异大）。
- **未找到**：NVIDIA 对 N1X=RTX Spark 的完整官方规格（NVIDIA 刻意少披露；多为泄露/PC 厂检查价）。
- **数据纪律**：全篇不采用具体 tok/s 作为营销结论；仅以内存档（128GB 统一）+ 带宽定性描述能力。
- **反向主张候选 1（命名混淆）**：旧报告 nvidia-dgx.md 把 "RTX Spark" 当作 GB10 的 mini-PC/笔记本平价形态；但 2026-06 官方把 N1X 消费芯定名 RTX Spark [10]——"RTX Spark" 现指 Windows-on-Arm 笔记本芯而非 GB10 盒子，旧结论需修正。
- **反向主张候选 2（是否值得买 128GB 档）**：InsiderLLM 明确"多数人不该买 GB10，二手 3090 更划算"[9]——削弱"人人需要桌面 AI 超算"的叙事，Olares One 也须回答"为何不是一张二手大显存卡"。
- **反向主张候选 3（已推翻）**：曾以为"GB10 arm64 → Olares 不支持"，实为误读裸机 ISO 页；Olares 经 script 支持 ARM Linux [16]，GB10 有望 High，仅 DGX OS 实测 [unverified]。
