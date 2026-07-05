---
task_id: 03
role: TrueNAS/45Drives 分析师
status: complete
sources_found: 10
---

## Sources
[1] TrueNAS Compare Systems | https://www.truenas.com/systems-overview/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[2] TrueNAS R-Series（含 R-Series Data Sheet PDF, Mar 2026） | https://www.truenas.com/r-series/ | Source-Type: official | As Of: 2026-03 | Authority: 10/10
[3] TrueNAS H-Series | https://www.truenas.com/h-series/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[4] TrueNAS F-Series | https://www.truenas.com/f-series/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[5] TrueNAS M-Series Data Sheet | https://www.truenas.com/wp-content/uploads/2026/02/TrueNAS_M-Series_Data_Sheet_January_2026.pdf | Source-Type: official | As Of: 2026-02 | Authority: 10/10
[6] TrueNAS Mini（含 Mini R 规格表） | https://www.truenas.com/truenas-mini/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[7] TrueNAS for AI & ML | https://www.truenas.com/ai/ | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[8] Storinator Q30 | https://www.45drives.com/products/storage-server-storinator-q30/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[9] Storinator XL60 | https://www.45drives.com/products/storage-server-storinator-xl60/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[10] 45HomeLab HL15 | https://45homelab.com/ | Source-Type: official | As Of: 2026-07 | Authority: 10/10

## Findings
- **TrueNAS Mini R**：2U 机架，12×3.5" 热插拔（可选 2.5" 转接），Intel C3758 八核，32–64GB ECC DDR4，2×1/10GbE RJ45 + IPMI，可选 2×SFP+ 10G；最高约 216TB raw；下单可选 **TrueNAS CORE 或 SCALE**；空机约 **$2,000 起**（2022 官方博客），第三方空机约 €3,429。**出厂预装 TrueNAS、保修绑定 iX 平台**。[6][1]
- **R-Series 现役三款（单控、无 HA）**：**R20** 2U hybrid，12×3.5"+2×2.5"，6–16 核/64–192GB，2×10/25/40/100GbE + 可选 32Gb FC，最高 2.9–3.4PB raw / 8GB/s；**R50** 4U hybrid，48×3.5"+4×NVMe，最高 5–6.5PB / 10GB/s；**R60** 1U all-flash，12×NVMe，16–32 核 PCIe Gen5 + 192–384GB DDR5，2×400GbE 或 4×25/100/200GbE，最高 7PB / **60GB/s**（官方定位 AI/分析）。OS：**TrueNAS Enterprise Data Platform**。Enterprise 报价制，无公开 MSRP。**不可自装第三方系统**。[2][1]
- **R30/R40（Legacy）**：R30 曾为 1U 16×NVMe all-flash（最高约 240TB）；**已不在 2026 官方在售 lineup**（由 R20/R50/R60 取代），仅 legacy 文档留存。[2]
- **H-Series（双控 HA，2U–6U）**：**H10** 最高 1.8PB / 2GB/s / 72 盘；**H20** 3PB / 4GB/s / 114 盘；**H30** 3PB / 8GB/s / 114 盘（NAB 2025 获奖）。混合或全闪 tri-mode 盘位；网口 1G–100GbE + FC。TrueNAS Enterprise。**不可自装系统**。[3][1]
- **M-Series（双控 HA，4U–52U，任务关键）**：**M30/M40/M50/M60**；基座 4U 24 盘；CPU/RAM 约 8C/96GB → 32C/768GB；网口至 4×100GbE；最高 **30PB** raw。历史资料 M30 入门约 **$15,000 起**（2021 博客，需报价确认）。**不可自装系统**。[5][1]
- **F-Series（双控 HA，2U 全 NVMe）**：**F60** 最高 4PB / 20GB/s / 24 NVMe；**F100** 最高 10PB / 30GB/s / 24 NVMe + 最多 6 个扩展柜；网口至 6×40/100GbE + 4×32Gb FC。**不可自装系统**。[4][1]
- **TrueNAS AI（truenas.com/ai）**：定位为 AI pipeline 存储——模型缓存、**RAG 向量库**、GenAI 输出落盘；原生 **Kubernetes CSI**、开放 API；可在 appliance 内跑 **VM/Container**（边缘推理）。营销页未点名 vLLM；**vLLM/Ollama/LocalAI 等通过 TrueNAS SCALE Apps Catalog 部署**（需 GPU 配置）。Enterprise 机柜侧重存储层，本地 LLM 推理更常见于 Mini/R 系 + SCALE。[7][6]
- **45Drives Storinator Q30**：4U **30×3.5"**，Direct-Wire 无 expander，最高约 **960TB** raw；可选 AMD EPYC 8124P–8534P 或 Intel Xeon，最高 64 核 / 2TB DDR5；默认 ZFS on Linux + Houston UI，但官方强调 **open hardware / zero vendor lock-in**，可自选 CPU/RAM/OS。**可自装系统（开放硬件）**；turnkey 报价制。[8]
- **45Drives Storinator XL60**：4U **60×3.5"**，Direct-Wire，最高约 **1.92PB** raw；CPU/RAM 选项同 Q30；预装 ZFS + Houston，支持 Ceph 集群；**可自装系统（开放硬件）**。[9]
- **45HomeLab HL15**：15×3.5" toolless 直连背板，全尺寸 ATX 主板（评测为 Supermicro X11SPH-NCTF + Xeon）；最高约 480TB raw，双 10Gb 可跑满 ~2000MB/s。**三档：Chassis+Backplane $799.99 / +PSU $910 / 整机 $1,999.99**；官方 **open-platform**，评测可装 Rocky Linux、Windows Server 等。**高度适合自装 Olares（开放硬件 + 自选 OS）**。[10]

## Deep Read Notes
### Source [2]: TrueNAS R-Series
Key data: 现役 R20/R50/R60 完整盘位、CPU 核数区间、DRAM、网口速率、最大吞吐/容量；R60 为 PCIe Gen5 + DDR5 + 400GbE，定位 AI。
Key insight: R 系刻意 **单控降本**，HA 需求导向 H/M/F；R60 是 R 系向 AI 工作负载的旗舰延伸。
Useful for: 「iX 企业机架单控高密度」价格/性能锚点；**不可换 OS** 是 vs 45Drives 的关键差异。

### Source [7]: TrueNAS for AI & ML
Key data: RAG 库托管、K8s CSI、TB–30PB+ 扩展、VM/Container 本地跑 workload；R60 400Gb/s 与 AI 叙事联动。
Key insight: 官方 AI 叙事偏 **数据管道 + 主权存储**，非 turnkey LLM appliance；推理/apps 依赖 SCALE 生态。
Useful for: 「TrueNAS + 本地 AI」内容需区分 Enterprise 存储 vs SCALE Apps（vLLM GPU catalog）。

### Source [10]: 45HomeLab HL15
Key data: 15 盘 homelab 定位、三档 SKU 与 $799/$910/$1999 价格带、open-platform/可拆改。
Key insight: 45Drives 把 enterprise Direct-Wire 架构下放到 homelab，**硬件开放度远高于 TrueNAS 一体机**。
Useful for: Olares 安装场景——HL15 机箱-only 或整机均可作为「自托管 Agent 底座」叙事。

## Gaps
- **R30 是否仍售**：2026 R-Series 资料称 R30/R40 **已停产**；文档站仍保留 R30 部署指南，第三方经销商仍挂 R30 SKU——在售状态需向 iX 销售确认。[2]
- **「开放」口径冲突**：45Drives 同时宣称 **ZFS on Linux 预装 + Houston** 与 **open hardware/zero lock-in**；turnkey 默认 OS 非用户自选，但 chassis-only SKU 支持完全 DIY——与 TrueNAS「出厂即 TrueNAS、不可换 OS」形成对比。[8][10] vs [6]
- **Mini R 价格带**：官方 2022 博客「**under $2,000**」与 2026 第三方空机 **€3,429** 并存，可能含配置/区域/通胀差异，无 2026 官方标价页。[6]

## END
