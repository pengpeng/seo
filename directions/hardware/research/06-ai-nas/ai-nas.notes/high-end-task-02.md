---
task_id: 02
role: 高端 AI NAS（Aoostar/Minisforum/DIY）分析师
status: complete
sources_found: 12
---

## Sources
[1] AOOSTAR WTR MAX 11 Bay NAS Ryzen 7 PRO 8845HS | https://aoostar.com/products/aoostar-wtr-max-amd-r7-pro-8845hs-11-bays-mini-pc | Source-Type: official | As Of: 2025-11 | Authority: 9/10
[2] Aoostar WTR Max NAS Review | https://nascompares.com/2025/06/27/aoostar-wtr-max-nas-review/ | Source-Type: secondary-industry | As Of: 2025-06 | Authority: 8/10
[3] Aoostar launches affordable 11-bay NAS with OCuLink (Intel i5-1235U variant) | https://www.notebookcheck.net/Aoostar-launches-affordable-11-bay-NAS-with-OCuLink-and-built-in-screen.1306182.0.html | Source-Type: journalism | As Of: 2026-05 | Authority: 8/10
[4] Minisforum N5 Pro AI NAS (Store) | https://store.minisforum.com/products/minisforum-n5-pro-ai-nas | Source-Type: official | As Of: 2025-12 | Authority: 9/10
[5] Minisforum N5 Pro: World's first AI NAS with AMD Ryzen AI 9 HX PRO 370 (Review) | https://www.notebookcheck.net/Minisforum-N5-Pro-World-s-first-AI-NAS-with-AMD-Ryzen-AI-9-HX-PRO-370-IFA-2025-Award-winner-review.1142209.0.html | Source-Type: secondary-industry | As Of: 2025-12 | Authority: 9/10
[6] Minisforum N5 Pro AI NAS with Ryzen AI 9 HX Pro 370 – Specs & Price | https://www.guru3d.com/story/minisforum-n5-pro-ai-nas-with-ryzen-ai-9-hx-pro-370-specs-price/ | Source-Type: journalism | As Of: 2025-11 | Authority: 7/10
[7] Minisforum MS-A2 Review - The MS-01 Killer? | https://nascompares.com/2025/04/30/minisforum-ms-a2-review-the-ms-01-killer/ | Source-Type: secondary-industry | As Of: 2025-04 | Authority: 8/10
[8] Minisforum MS-A2 Review An Almost Perfect Homelab System | https://www.servethehome.com/minisforum-ms-a2-review-an-almost-perfect-amd-ryzen-intel-10gbe-homelab-system/ | Source-Type: secondary-industry | As Of: 2025-03 | Authority: 9/10
[9] Review of the MINISFORUM MS-01 mini PC with Intel Core i9-13900H | https://minipc-review.com/en/review-minisforum-ms-01-mini-pc | Source-Type: journalism | As Of: 2025-01 | Authority: 7/10
[10] JONSBO N6 NAS Case (Official) | https://www.jonsbo.com/en/products/N6Black.html | Source-Type: official | As Of: 2025-11 | Authority: 8/10
[11] How to Build a Home AI Server for Local LLMs: The Complete 2026 Guide | https://fungies.io/how-to-build-home-ai-server-local-llms-2026/ | Source-Type: community | As Of: 2026-01 | Authority: 6/10
[12] Case Study: 4x RTX 4090 AI Workstation | https://kentino.com/blogs/ai-corner/case-study-4x-rtx-4090-ai-workstation | Source-Type: community | As Of: 2026-02 | Authority: 7/10

## Findings
- **Aoostar WTR Max（AMD 顶配）**：Ryzen 7 PRO 8845HS 8C/16T；**无内置 PCIe 槽**，GPU 仅 **OCuLink PCIe4 x4**（+ USB4，需 AG02/AG03 等 eGPU 坞）；**128GB** DDR5-5600 ECC；11 盘位（6×SATA + 5×M.2）；双 10GbE SFP+ + 双 2.5GbE；**裸机 $659**，64GB ECC 套装约 **$1,145**；**不预装 OS**，官方/评测均推 TrueNAS/Proxmox/Unraid——**裸机友好，利于自装 Olares**。[1][2]
- **Aoostar WTR Max（Intel 次顶）**：Core i5-1235U；同 OCuLink；**96GB** DDR5-4800；同 11 盘位与网络；**裸机 $559**；同样无锁定 OS。[1][3]
- **Aoostar eGPU 配套**：AG02 OCuLink 800W eGPU 坞约 **$169–219**；实测 OCuLink 可接低功耗专业卡（如 RTX 2000 Ada 20GB）跑 AI/转码。[2]
- **Minisforum N5 Pro（顶配）**：Ryzen AI 9 HX PRO 370 12C/24T + Radeon 890M + NPU；**内 PCIe x16（电 x8）+ OCuLink**；**96GB** DDR5-5600 ECC；5×3.5" SATA + 3×M.2/U.2（标称 ~144TB）；10GbE + 5GbE；官方内插示例 **RTX 4060 Laptop / Tesla P4**，Notebookcheck 实测 **OCuLink + DEG1 坞 + RTX 4090**；**裸机 $1,019**，96GB 套装 **$1,597**；预装 MinisCloud OS 但可裸机购入后 wipe——**可自装系统**。[4][5][6]
- **Minisforum N5（非 Pro）**：Ryzen 7 255 8C/16T + 780M；仍有 PCIe x16 + OCuLink + 5 盘位，但无 HX PRO 370 级 CPU/NPU；store 标价低于 N5 Pro。[4]
- **Minisforum MS-A2（小主机作 NAS + 内插独显）**：Ryzen 9 **9955HX** / **7945HX** 16C/32T；**内 PCIe4 x16 电 x8**（可 bifurcation 拆 2×x4）；**96GB** DDR5-5600（STH 实测 **128GB 非 ECC 可跑**）；3×M.2 + U.2（无多盘位 SATA，NAS 需外接）；双 10GbE SFP+ + 双 2.5GbE；**$639–839** 裸机；无 USB4/OCuLink——**纯裸机 x86 Linux 宿主，Olares 友好**。[7][8]
- **Minisforum MS-01（Intel 小主机作 NAS + 半高独显）**：Core i9-13900H / i9-12900H / i5-12600H；**内 PCIe4 x16 电 x8，仅半高单槽**（无 aux 供电）；典型卡 **RTX 2000 Ada 16GB / RTX A2000 / RTX 3050 LP**；**64–96GB** DDR5；3×M.2 + 可选 U.2；**USB4×2**；裸机约 **$500–750**；装高功耗卡需 240W 适配器——**无锁定 OS，homelab/NAS VM 常见**。[7][9]
- **DIY：Jonsbo N6（社区 NAS+GPU 一体）**：mATX/ITX；**9×3.5" 热插拔**；单卡 **275–320mm**；双 PSU 位；典型 CPU **Ryzen 9 9900** + **RTX 3090/5060 Ti 16GB** + **128GB** DDR5；Proxmox + TrueNAS Scale VM + GPU passthrough 跑 Ollama——**完全 BYO OS，Olares 最灵活**；机箱约 **$150–200**，整机 **$2,000–3,500**。[10][11]
- **DIY：4U 机架 + 旗舰/Pro 独显（70B 级）**：**SilverStone RM43-320-RS / RM44** + **EPYC/至强** 主板；**4×RTX 4090**（96GB VRAM 合计，PCIe P2P，无 NVLink）实测跑 **Llama 3.3 70B Q4**；或 **4×RTX Pro 6000 Blackwell Server Edition**（96GB×4）；预算 **$8k–$20k+**——**裸 Linux，Olares 满血 x86+NVIDIA 路径**。[11][12]
- **70B 本地 LLM VRAM 门槛（选型约束）**：70B Q4 约需 **38–40GB+ VRAM**；单 **RTX 4090/5090（24/32GB）不够全量载入**；需双卡 48GB+、四卡 96GB，或 CPU/RAM offload（2–3 tok/s 级）——影响上述 OCuLink 单卡 eGPU 方案上限。[11][12]

## Deep Read Notes
### Source [2]: Aoostar WTR Max NAS Review
Key data: Ryzen 7 PRO 8845HS 8C/16T；128GB ECC；6 SATA + 5 M.2；**无内 PCIe**，**OCuLink PCIe4 x4** 可接 NVMe 外盒或 eGPU；双 10GbE SFP+ + 双 2.5GbE；满载 ~73–89W；**不附带专有 NAS OS**。
Key insight: 11 盘位密度 + OCuLink 是「存储 NAS + 外接算力」折中；内插 HBA/独显不可行，GPU 路径只有 OCuLink/USB4 eGPU。
Useful for: Olares 叙事——WTR Max 是典型 **裸机 x86 宿主 + 大存储**，装 Olares 无固件锁；GPU 加速需外接坞额外预算。

### Source [5]: Minisforum N5 Pro Review (Notebookcheck)
Key data: Ryzen AI 9 HX PRO 370 12C/24T；**96GB ECC DDR5-5600**；5 HDD + 3 SSD；**内 PCIe x16 + OCuLink**；裸机 **$1,019**，96GB 套装 **$1,597**；实测 **RTX 4090 @ OCuLink + DEG1**。
Key insight: 唯一「原生多盘位 NAS 形态 + 内/外双 GPU 路径」量产机；内槽带宽与机箱空间限制实际卡型，重 LLM 更现实走 OCuLink 4090/5090。
Useful for: 高端 AI NAS 标杆对比；Olares 可 wipe MinisCloud 裸装。

### Source [8]: Minisforum MS-A2 Review (ServeTheHome)
Key data: Ryzen 9 9955HX 16C/32T；**PCIe4 x16 电 x8** 低-profile 扩展；**128GB 非 ECC 实测可用**；3×M.2/U.2；双 10GbE SFP+ + 双 2.5GbE；**无 USB4/OCuLink**；~1.7L 机箱。
Key insight: MS-01 的 AMD 算力升级版，适合 **Proxmox NAS VM + 内插 LP 专业卡**，而非 11 盘位一体 NAS。
Useful for: 「MS-01/MS-A2 类小主机作 NAS」路径——Olares 裸机/虚拟化均友好。

## Gaps
- **[相反主张 1 — 70B 能否单卡跑满]**：[11] 称 RTX 5090 **32GB** 可跑 70B 且「room to spare」；[12] 实测 **70B Q4 需 38–40GB VRAM**，单 4090 24GB 不够——单卡 5090/4090 OCuLink 方案对 70B 全量推理是否够用，来源矛盾。
- **[相反主张 2 — N5 Pro 内 PCIe 电气带宽]**：[6] 写 PCIe x16 槽 **电 x8**；部分零售页写 **x4**——内插独显对 LLM 带宽上限待主板规格页二次核实。
- **[相反主张 3 — WTR Max 网口数量]**：[3] Intel 版新闻写「one 10G and one 2.5G」；[1][2] 官方与 NAS Compares 均为 **2×10GbE SFP+ + 2×2.5GbE**——以 [1][2] 为准，[3] 疑似笔误。
- **MS-01 内存上限**：社区帖称 **128GB** vs 官方/评测多写 **64–96GB**——大内存 NAS VM 场景需实测。
- **N5 Pro 内插全长独显**：官方仅列 LP/笔记本级卡；用户能否内装 RTX 4090/5090 级——缺可靠 teardown，仅 OCuLink 有 [5] 基准。

## END
