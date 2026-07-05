---
task_id: 02
role: QNAP 企业/机架+AI 分析师
status: complete
sources_found: 9
---

## Sources
[1] TS-AI642 | 6-Bay Tower AI NAS | https://www.qnap.com/en/product/ts-ai642 | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[2] TDS-h2489FU R2 | Dual-CPU U.2 NVMe all-flash rackmount NAS | https://www.qnap.com/en/product/tds-h2489fu%20r2 | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[3] Qsirch | The AI-powered search engine for your NAS | https://www.qnap.com/en/software/qsirch | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[4] QNAP Launches TS-h2477AXU-RP (24-bay ZFS NAS) | https://www.qnap.com/en/news/2025/qnap-launches-ts-h2477axu-rp-24-bay-zfs-nas-optimized-for-high-speed-storage-and-resilient-backup | Source-Type: official | As Of: 2025-11 | Authority: 9/10
[5] QNAP Launches TVS-AIh1688ATX AI NAS with 36 TOPS | https://www.qnap.com/en/news/2025/qnap-launches-tvs-aih1688atx-ai-nas-with-36-tops-for-ai-and-virtualization | Source-Type: official | As Of: 2025-10 | Authority: 9/10
[6] TVS-h674 | ZFS NAS with 10/25GbE expandability | https://www.qnap.com/en/product/tvs-h674 | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[7] TS-h765eU | Compact 1U short-depth rackmount NAS | https://www.qnap.com/en/product/ts-h765eu | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[8] QNAP TDS-h2489FU R2 Availability and Pricing | https://www.storagereview.com/news/qnap-tds-h2489fu-r2-flagship-nas-for-demanding-workloads | Source-Type: journalism | As Of: 2025-05 | Authority: 7/10
[9] QNAP US Store (TS-AI642 / TVS-h674 / TS-h2477AXU-RP) | https://store.qnap.com/ | Source-Type: official | As Of: 2026-07 | Authority: 8/10

## Findings
- **TS-AI642-8G-US**（TS-AI 系唯一在售型号）：6-bay 塔式；ARM RK3588（Cortex-A76/A55 八核 2.2/1.8 GHz）+ Mali-G610；**NPU 厂商宣称 6 TOPS（存疑/偏低，第三方称不足以对标 Copilot+ 40 TOPS 档）**；8 GB 不可扩；1×2.5GbE + PCIe Gen3×2（可升 10GbE）；双 4K HDMI；**固件 QTS**（非 QuTS hero）；QuMagie/QVR Face/Qsirch OCR 加速；**$749** [1][9]
- **TVS-AIh1688ATX**（2025-10 高端 AI 塔式）：12×3.5" SATA + 4×2.5" U.2 NVMe/SATA；Intel Core Ultra 7/9（Ultra 9 最高 24C/24T @5.6 GHz）；**厂商宣称合计最高 36 TOPS（CPU+GPU+NPU，存疑/未独立披露 NPU TOPS）**；DDR5 ECC 至 192 GB；2×10GbE + 2×2.5GbE，PCIe 可扩 25/100GbE、TB5；**QuTS hero**；SKU 例 TVS-AIH1688ATX-U9-48G-US **~$5,199** [5][9]
- **TDS-h2489FU R2**（旗舰双路全闪机架）：2U；16×U.2 NVMe + 8×U.2 NVMe/SATA 混插（计 24 槽）；双 Intel Xeon Silver 4300（4309Y/4314 等 SKU）；DDR4 ECC RDIMM 至 1 TB；**标配 4×2.5GbE + 预装双口 25GbE SFP28**（iSER/SR-IOV），可扩 100GbE；4×PCIe Gen4；**QuTS hero**（可切 QTS）；SKU 定价 **$10,999–$29,999**（64G–1TB 内存档）[2][8]
- **TS-h2490FU**（单路 EPYC 全闪）：2U 24×U.2 NVMe；AMD EPYC 7232P/7252 或 7302P；4×25GbE SFP28 SmartNIC 内置；5×PCIe Gen4；RAM 至 4 TB；**QuTS hero**；4K 随机读 **厂商宣称 >661K IOPS**；渠道价 **~$8,999–$16,799** [2][9]
- **TS-h3077AFU**（高密度 SATA 全闪）：30×2.5" SATA；AMD Ryzen 5 7000；DDR5 至 192 GB；3×PCIe Gen4（100GbE）；**QuTS hero**；4K 随机读 **厂商宣称 >1.6M IOPS**；store 档 **~$7,099+** [2][9]
- **TS-h2477AXU-RP-R7-32G-US**（2025-11 企业 SATA 机架）：4U 24×3.5" SATA；AMD Ryzen 7 PRO 7000 8C/16T；32 GB DDR5（至 192 GB）；2×2.5GbE + 2×10GbE，PCIe 可扩 25GbE/GPU；双 M.2 PCIe Gen5 + 3×PCIe Gen4；冗余电源；**QuTS hero**；**$7,299**（CDW ~$7,146）[4][9]
- **TVS-h674 / TVS-h874**（TVS-h 高端塔式 QuTS hero）：6-bay / 8-bay；Intel Core i3-12100 / i5-12400 / i7（874）；UHD 730 + **可选 Google Edge TPU（QM2，非板载 NPU）**；2×2.5GbE + 2×PCIe Gen4（25GbE）；Intel OpenVINO 加速 QuMagie；**QuTS hero**（可迁 QTS）；**$1,899–$2,349** [6][9]
- **TS-h765eU-8G**（短深 1U 边缘/企业机架）：4×3.5" SATA + 3×E.1S/M.2 2280（合计 7 槽 hybrid）；Intel Atom x7405C 4C；8 GB DDR5 In-Band ECC（至 16 GB）；2×2.5GbE，E1.S 模块可升 10GbE；**QuTS hero**（可切 QTS）；Qsirch RAG 宣传；无官方 MSRP [7]
- **TS-h 机架 QuTS hero 存量线**（高密度/10GbE，多 SKU）：TS-h987XU-RP（9-bay 1U Xeon E-2334）；TS-h1277AXU-RP / TS-h1677AXU-RP（12/16-bay 2U Ryzen）；TS-h1887XU-RP / TS-h2287XU-RP / TS-h3087XU-RP（18/22/30-bay 2–4U Xeon）；TS-h1090FU / TS-h1290FX（10/12-bay 1–2U 全闪，1290FX **内置 2×25GbE**）；均 **QuTS hero + ZFS** [2][4]
- **本地 AI 软件栈**：QuMagie（人脸/物体/地点 AI 相册）；QNAP AI Core（图像识别引擎，依赖 NPU/OpenVINO/Edge TPU）；Qsirch 关键词+OCR+**AI Semantic Search（仅 x86，≥8 GB，QTS 5.0.1+/QuTS hero h5.0.1+）**；Qsirch **RAG Search Beta**（x86+ARM，Qsirch 5.6+，云/本地 LLM）；QVR Face/Human/Smart Search 监控 AI [1][3][5][7]

## Deep Read Notes
### Source [1]: TS-AI642
Key data: 唯一 TS-AI 型号；RK3588 ARM 八核；厂商宣称 6 TOPS NPU；6×3.5"/2.5" SATA；QTS 5.x；NPU 宣称 QuMagie 图像识别 3×、QVR 10 路实时人脸、Qsirch OCR 1.2×；可扩 TL-D1600S 至 ~350 TB。
Key insight: QNAP 将 "AI NAS" 锚定在边缘相册/监控 OCR，非 LLM 训练；TOPS 营销远低于 PC AI PC 基准。
Useful for: ARM+NPU 入门 AI NAS 对标 Olares 边缘推理场景；价格带 <$800。

### Source [2]: TDS-h2489FU R2
Key data: 双 Xeon Silver 4314 展示配置；24 U.2 混插；4K 随机读 **厂商宣称 >1M IOPS**；25GbE 标准 + 100GbE 扩展；PB 级 JBOD；双机 HA（RTO ≤90s）；5 年保修。
Key insight: QNAP 企业全闪三梯队：双路 Xeon（TDS-R2）> 单路 EPYC 24 槽（2490FU）> Ryzen SATA 高密度（3077AFU）。
Useful for: 25GbE/100GbE 企业存储竞品矩阵、QuTS hero 旗舰定价锚点。

### Source [3]: Qsirch
Key data: AI Semantic Search 限 **64-bit x86**；RAG Beta 支持 x86+ARM；OCR 加速路径：Intel OpenVINO（TS-464 2.6×）vs NPU（TS-AI642 1.2×）。
Key insight: QNAP 软件 AI 分层——ARM NPU 做相册/监控；语义搜索与 RAG 仍偏 x86；TS-AI642 产品页写 "Qsirch NPU 加速" 实际主要指 OCR。
Useful for: Olares 语义搜索/本地 RAG 内容角度；澄清 TS-AI vs TVS-AIh vs TVS-h 软件能力差异。

## Gaps
- **盘位命名冲突**：TS-h765eU 官方硬件规格为 **4×SATA + 3×E1.S**（合计 7 槽 hybrid）[7]，但 QNAP 新闻稿标题写 **"4-bay"**，StorageReview 称 **"7-bay hybrid"**——对外口径不统一。
- **AI 能力宣传冲突**：TS-AI642 官方页强调 Qsirch「NPU 加速」[1]，但 Qsirch 官方要求 **AI Semantic Search 仅 x86 NAS** [3]；TS-AI642 仅能跑关键词/OCR/RAG（5.6+），语义图搜需 TVS-h/TVS-AIh 等 x86 机型——营销页与软件兼容表不一致。
- **25GbE 规格存疑**：TDS-h2489FU R2 产品对比表写 TS-h2490FU 为 **4×25GbE 内置** [2]，而 StorageNewsletter 对 R2 自身描述为 **4×2.5GbE + 2×25GbE 预装**——同系列不同页面 network 口数量需以 hardware PDF 二次核验。

## END
