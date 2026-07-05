---
slug: rog-nuc
task: task-01
role: AI 硬件生态图谱分析师
as_of: 2026-07-05
mode: Standard
queries:
  - "ASUS ROG NUC 2025 NUC15JNK Core Ultra 9 275HX RTX 5080 96GB liter price specs"
  - "ASUS ROG NUC 16 2026 NUC16JNK Core Ultra 9 290HX Plus RTX 5090 Laptop 128GB"
  - "ROG NUC barebone install linux self-configure memory ssd"
  - "Olares One BOM RTX 5090 Mobile 275HX 96GB vs ROG NUC"
---

## Sources

[1] https://rog.asus.com/us/desktops/mini-pc/rog-nuc-2025/ — ROG NUC (2025) NUC15JNK 官方页：Core Ultra 9 275HX、最高 RTX 5080 Laptop（亦 5060/5070/5070Ti）、DDR5-6400、2.5L（282.4×187.7×56.5mm）、三风扇、$2,799 起 — official(retail) — As Of 2026 — 权威 9
[2] https://www.newegg.com/asus-rog-nuc-barebone-systems-mini-pc-intel-core-ultra-9-275hx/p/2SW-000N-00128 — Newegg：275HX + RTX 5080 16GB GDDR7 + 32GB DDR5 + 2TB，Max Memory 96GB，330W PSU，$4,399 — retail — As Of 2026 — 权威 7
[3] https://www.microcenter.com/product/697039/asus-rog-nuc-(2025)-rnuc15jnk9x28aau-mini-gaming-pc — Micro Center：RNUC15JNK9X28AAU，275HX/5080 16GB/32GB/2TB，$2,899.99 — retail — As Of 2026 — 权威 7
[4] https://videocardz.com/newz/razer-blade-18-2026-laptop-pricing-reaches-6999-with-rtx-5090-and-128gb-ram — 提及 "ASUS ROG NUC 16 Edition gets GeForce RTX 5090 Laptop GPU (Jun 03)"、"ROG NUC 16 (2026) 275HX/290HX Plus + RTX 5080, >$4,000 (May 15)" — journalism — As Of 2026-06 — 权威 6
[5] https://rog.asus.com/uk/desktops/mini-pc/rog-nuc-2025/wtb/ — ROG NUC (2025) UK SKU：5070Ti/5080 Laptop + Intel Graphics、Max 96GB(48GB×2 DDR5-5600)、含 16GB DDR5-6400 CSODIMM×2、1-4TB M.2 PCIe4/5、3.12kg、£3,499.99 — official(retail) — As Of 2026 — 权威 8
[6] https://rog.asus.com/uk/desktops/mini-pc/rog-nuc-2025/ — ROG NUC 16 (NUC16JNK) 预览：Up to RTX 5080 Laptop 16GB、Up to Core Ultra 9 290HX Plus、Up to 128GB DDR5-6400、2TB (Gen5+Gen4) — official(retail) — As Of 2026 — 权威 8
[7] https://one.olares.com/ — Olares One BOM（$3,999 / 5090 Mobile 24GB / 275HX / 96GB 可扩 128GB / 2TB） — official — As Of 2026 — 权威 9
[8] https://docs.olares.com/ — Olares 安装平台矩阵 + GPU 加速口径 — official — As Of 2026 — 权威 9

## Findings

1. ROG NUC (2025) NUC15JNK：Core Ultra 9 **275HX**（24 核，5.4GHz）、最高 **RTX 5080 Laptop 16GB GDDR7**（亦 5060/5070/5070Ti）、最高 **96GB** DDR5-6400（2×SODIMM）、双 M.2（PCIe4.0+5.0）最高 4TB、**2.5L**（282.4×187.7×56.5mm，3.12kg）、330W、TB4、2.5GbE、Wi-Fi7、Windows 11 [1][2][3][5]。
2. 价格：US estore $2,799 起（低 GPU 档）；5080/32GB/2TB 配置 Micro Center $2,899、Newegg $4,399；UK £3,499.99 [1][2][3][5]。→ 因 GPU 档跨度大，价格 $2,799–$4,399 区间。
3. ROG NUC 16 (2026) NUC16JNK：最高 Core Ultra 9 **290HX Plus**、ASUS 页列到 RTX 5080 16GB，VideoCardz 报有 **RTX 5090 Laptop 24GB** 版、最高 **128GB** DDR5-6400、2TB(Gen5+Gen4)，>$4,000 [4][6]。5090 顶配以官方页为准 [unverified]。
4. Olares One BOM：$3,999 / RTX 5090 Mobile 24GB / 275HX / 96GB(扩 128GB) / 2TB [7]。
5. BOM 对位：**2025 版 = CPU(275HX)+内存上限(96GB) 与 Olares One 同款，GPU 差一档（5080 16GB vs 5090 24GB，少 8GB 显存）**；**2026 版 = GPU(5090 24GB) 同款，CPU 更新一代（290HX Plus）**。合起来两维度都对上。
6. ROG NUC 是 barebone（可自配内存/SSD、可自装系统）+ x86 + NVIDIA → Olares 信息 B 的样板宿主；装 Olares（WSL2 或裸机 Linux）后 ≈ 自组 Olares One。
7. 差异不在硬件而在软件/定位：ROG NUC 出厂 Windows 11 游戏取向、无私有云服务层；Olares One 软硬一体私有云 OS + 面向 AI 常驻/无头服务。

## Deep Read Notes

### ASUS 官方 ROG NUC (2025) [1][5]（DEEP）
- 三风扇 + Unified Vapor Chamber，支持五屏 4K，HDMI 2.1 ×2 + DP 2.1 ×2。
- 内存：含 16GB DDR5-6400 CSODIMM×2，Max 96GB（48GB DDR5-5600 SODIMM×2）——注意最高档降频到 5600。
- 存储：1-4TB M.2 2280 NVMe PCIe4.0x4 或 PCIe5.0x4。
- 型号后缀多：RNUC15JNK9X28AAU（5080/32GB/2TB）、9X389A3 等。

### ROG NUC 16 (2026) [4][6]（DEEP）
- ASUS 预览：Up to 290HX Plus / Up to RTX 5080 16GB / Up to 128GB / 2TB(Gen5+Gen4) / Windows 11。
- VideoCardz：ROG NUC 16 Edition 有 RTX 5090 Laptop GPU 变体（Jun 03 报道）；起售 >$4,000（May 15）。
- → 2026 版是拿到"5090 24GB 同款 GPU"的对标机型；顶配 5090/128GB 需官方页最终确认。

## Gaps

- **未验证**：ROG NUC 16 (2026) 5090 24GB 顶配的官方 SKU/定价（VideoCardz 报道 vs ASUS 页当前列 5080）——标 [unverified]，落地以 rog.asus.com 为准。
- **未验证**：关键词搜索量/KD（未跑 Semrush）。
- **波动**：各配置 MSRP 随 GPU 档/渠道/地区跳变大。
- **反向主张 1（2025 GPU 差一档）**：5080 16GB vs 5090 24GB，显存差 8GB，本地 AI 硬差距——2025 版不能打"同款 GPU"。
- **反向主张 2（价格非稳定卖点）**：低 GPU 档 $2,799 起，配到位接近/超 $3,999；须按同配置比。
- **反向主张 3（能装 Olares 何必买 One）**：正是 A/B 分工——DIY/已有盒子走 B，要开箱软硬一体走 A。
