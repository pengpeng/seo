# task-e · OEM eGPU / OCuLink attach — Arc Pro B70 + NAS 功耗/散热/静音预算

> AS_OF 2026-07-14 · explore 子代理蒸馏笔记（只读，Lead 代写落盘）

## Sources

| # | URL | Type | As-Of | Authority |
|---|-----|------|-------|-----------|
| 1 | https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf | Official spec (Intel) | 2026-03 | 10 |
| 2 | https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html | Official (Intel) | 2026-07-14 | 10 |
| 3 | https://www.techpowerup.com/gpu-specs/arc-pro-b70.c4388 | Vendor DB (TechPowerUp) | 2026-07-14 | 8 |
| 4 | https://global.download.synology.com/.../DS923+/enu/Product_Spec_DS923+_enu.pdf | Official (Synology) | 2023 | 10 |
| 5 | https://global.download.synology.com/.../DS224+/enu/Product_Spec_DS224+_enu.pdf | Official (Synology) | 2024 | 10 |
| 6 | https://global.download.synology.com/.../DS1823xs+/enu/Product_Spec_DS1823xs+_enu.pdf | Official (Synology) | 2023 | 10 |
| 7 | https://www.qnap.com/en-us/product/ts-464/specs/hardware | Official (QNAP) | 2026-07-14 | 10 |
| 8 | https://www.qnap.com/en-us/product/ts-873a/specs/hardware | Official (QNAP) | 2026-07-14 | 10 |
| 9 | https://nascompares.com/guide/a-guide-to-choosing-the-right-ups-for-your-synology-or-qnap-nas-drive/ | Vendor guide | 2026-07-14 | 7 |
| 10 | https://www.minisforum.uk/products/minisforum-deg1 | Official (Minisforum DEG1) | 2026-07-14 | 9 |
| 11 | https://www.adt.link/product/K993G.html | Official (ADT-Link) | 2026-07-14 | 8 |
| 12 | https://www.chargerlab.com/oculink-review-of-minisforum-deg1-egpu-dock/ | Review (Chargerlab) | 2026-07-14 | 7 |
| 13 | https://pcisig.com/PCIExpress/Specs/Cable/OCuLink_1.1 | Official spec (PCI-SIG) | 2020-07-21 | 10 |
| 14 | https://www.prnewswire.com/news-releases/ugreen-expands-nasync-lineup-with-idx-series-at-ces-2026-...html | Vendor PR (UGREEN) | 2026-01-06 | 8 |
| 15 | https://nascompares.com/2026/01/21/ugreen-idx6011-pro-ai-nas-review/ | Review (NASCompares) | 2026-01-21 | 8 |
| 16 | https://github.com/pmzfx/intel-arc-pro-b70-benchmarks/blob/master/llm-benchmarks.md | Community bench (PMZFX) | 2026-04-21 | 7 |
| 17 | https://localaimaster.com/blog/egpu-local-ai-benchmarks | Review/bench (Local AI Master) | 2026-03-08 | 7 |
| 18 | https://www.virtualizationhowto.com/2026/03/i-added-an-egpu-to-my-proxmox-mini-pc-home-lab-using-oculink.../ | Review | 2026-03 | 6 |
| 19 | https://www.servethehome.com/amd-details-ryzen-ai-halo-ai-dev-mini-pc-pre-orders-in-june-for-3999/ | Journalism (STH) | 2026-06 | 7 |
| 20 | https://needtoknowit.com.au/blog/gpu-expansion-for-nas-egpu-pcie-and-ai-workloads/ | Vendor guide | 2026-07-14 | 6 |

## Findings

### A — 外接 eGPU 让 NAS OEM 不必重做主板/机箱

1. **B70 额定 TBP 160–290W（合作伙伴区间；Intel 参考卡 230W）**，PCIe Gen5 ×16 [1][2]。
2. Intel 参考 B70：双槽、267×110×39mm、1×8-pin、1020g、建议整机 PSU **550W**（额定）[3]。
3. **实测跑 Qwen3.6-35B-A3B MoE（llama.cpp SYCL）平均 ~114W**（峰 104–128W；模型驻留空闲 ~18–22W）——远低于 230W 额定 [16]。
4. **消费 2–4 盘位 NAS 用 60–120W 外置电源**（Synology DS224+ 60W [5]；DS923+ 100–120W [4]）；**4–8 盘位 90–250W**（QNAP TS-464 90W [7]；DS1823xs+/TS-873A 250W [6][8]）[9]。
5. **NAS 热/噪预算低**：DS923+ 访问 35.5W / 121 BTU·hr⁻¹、空闲 **22.9 dB(A)**[4]；DS224+ 空闲 **22 dB(A)**/60W [5]；内置一块 230W 额定 GPU 将 **+~785 BTU·hr⁻¹**（≈ DS923+ 访问热的 6.5×）且击穿 PSU 余量。
6. **OCuLink（PCI-SIG）= PCIe 直连线缆**（SFF-8611/8612）；市售坞暴露 **PCIe 4.0 ×4 = 64Gbps**，是 PCIe lane 延伸、非 Thunderbolt 隧道 [13][12]。
7. **Minisforum DEG1 坞：上行 OCuLink 4i（PCIe 4.0 ×4），下行 PCIe ×16 槽，24-pin 接买家自备 ATX/SFX PSU** → GPU 供电与散热在坞内、不在主机 [10][12]。
8. **ADT-Link OCuLink→PCIe ×16 同样需自备 ATX PSU（建议 ≥500W）**、PCIe 4.0 ×4 / 64Gbps [11]。
9. **UGREEN NASync iDX6011 Pro（CES 2026）专门加 OCuLink 口做外接 GPU 扩展**（非 Pro 版无）[14]；NASCompares 实测该 OCuLink 路径能识别外接 GPU 坞 [15]。
10. **迷你机 OEM（GMKtec EVO-X1 Pro/EVO-X3、AOOSTAR、Minisforum AI X1 Pro）已普遍上 OCuLink 做模块化外接 GPU**——与 NAS OEM 论点同构 [18]。

### B — 复用/用户好处（较轻）

11. **LLM 推理走 OCuLink 相比内置 PCIe 仅损 ~3%**（RTX 4090：138 vs 142 tok/s），因权重加载后常驻 VRAM [17]。
12. eGPU 让用户**在现有 NAS/迷你机上扩展、而非另买新塔**；坞可按需供电，非常驻内置 GPU [18]。
13. 专用 128GB 统一内存 AI 盒 list **$3,999+**（AMD Ryzen AI Halo dev kit）——增量加卡避开这一 capex 级 [19]。
14. OCuLink 坞零售 ~$80–140（仅坞体）vs $3,000+ 新 AI 整机 [17][18]。

## Gaps / 反向点

- **主流 Synology/QNAP 消费型号目前不暴露 OCuLink**；本轮仅 UGREEN iDX6011 Pro 有 [14][15][20]。
- B70 over OCuLink 电气上是 PCIe 4.0 ×4（非 5.0 ×16）；对 LLM 推理损失小（~2–3%），其他负载有别 [17]。
- 合作卡差异大：8-pin vs 16-pin、160–290W TBP——OEM 需按最坏卡定坞 PSU [1][3]。
- **OEM 下行点（诚实）**：OCuLink **不支持热插拔**、强拔伤口；线缆长度/锁扣增支持成本；DEG1/ADT-Link 的坞 PSU 需自备；旧 NAS 无 lane 引出——**外接要成立，OEM 仍需刻意把 PCIe lane 引到 SFF-8612 口（I/O 工程），但不必重做主 PSU/机箱 GPU 集成**。

## 摘要

- B70 额定 TBP 160–290W（参考 230W）、实测 LLM ~114W；NAS PSU 60–250W、空闲 ~22–24 dB——内置放不下、会击穿功耗/散热/静音预算。
- OCuLink 走原生 PCIe（4.0 ×4/64Gbps），主机只需引出 lane；坞自带 PSU + 风冷，把 GPU 功耗/散热/噪音隔离在坞里。
- 已有先例：UGREEN iDX6011 Pro NAS + 一众迷你机 OEM 都上了 OCuLink。
- 诚实边界：OEM 仍要做 OCuLink 口的 I/O 工程、非零成本；OCuLink 非热插拔；旧型号无 lane。置信度：B70 规格/NAS 预算不匹配/坞自带 PSU 高；"OEM 免重做主板"中高。
