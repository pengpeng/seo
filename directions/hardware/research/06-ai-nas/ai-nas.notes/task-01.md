---
unit: ai-nas
type: category (by product/model, not vendor)
as_of: 2026-07-05
mode: Lightweight
task: task-01
sources_total: 18
official_ratio: ~50%
---

## Sources

[1] techreviewer.de — UGREEN NASync iDX6011 Pro Review (2026) — https://en.techreviewer.de/ugreen-nasync-idx6011-pro-test/ （第三方评测）
[2] XDA Developers — I tested Ugreen's most powerful NAS (iDX6011 Pro) — https://www.xda-developers.com/ugreen-most-powerful-nas-exposes-synology/ （第三方评测）
[3] Galaxus — Ugreen AI-NAS iDX6011 / iDX6011 Pro in detail — https://www.galaxus.at/en/page/ugreens-ai-nas-idx6011-and-idx6011-pro-in-detail-core-ultra-local-ai-and-up-to-196-tb-41592 （零售/媒体）
[4] UGREEN NAS US 官网 — NASync DXP4800 Plus 产品页 — https://nas.ugreen.com/products/ugreen-nasync-dxp4800-plus-nas-storage （官方）
[5] Minisforum Store 官网 — N5 Pro AI NAS 产品页 — https://store.minisforum.com/products/minisforum-n5-pro-ai-nas （官方）
[6] Notebookcheck — Minisforum N5 Pro review — https://www.notebookcheck.net/Minisforum-N5-Pro-World-s-first-AI-NAS-with-AMD-Ryzen-AI-9-HX-PRO-370-IFA-2025-Award-winner-review.1142209.0.html （第三方评测）
[7] NAS Compares — Aoostar WTR Max review — https://nascompares.com/review/aoostar-wtr-max-nas-review-nas-perfection/ （第三方评测）
[8] androidtvbox.eu — Aoostar WTR Max Intel i5-1235U 版 — https://androidtvbox.eu/aoostar-wtr-max-intel-1235u-nas-11-disk/ （媒体）
[9] Zima Store 官网 — ZimaCube 2 产品页 — https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas （官方）
[10] Notebookcheck — ZimaCube 2 review — https://www.notebookcheck.net/ZimaCube-2-review-This-home-server-is-more-than-just-a-NAS-a-self-hosting-powerhouse.1316114.0.html （第三方评测）
[11] 极空间官网 — Z425 产品页 — https://m.zspace.cn/z425/ （官方）
[12] Need to Know IT — Synology vs QNAP vs UGREEN for AI — https://needtoknowit.com.au/blog/synology-vs-qnap-vs-ugreen-for-ai-features-australia/ （第三方分析）
[13] Synology 官网 — DiskStation DS925+ — https://www.synology.com/en-global/products/DS925+ （官方）
[14] LincPlus 官网 — LincStation N2 产品页 — https://www.lincplustech.com/products/lincstation-n2-network-attached-storage.html （官方）
[15] Olares One 官网 — https://one.olares.com/ （官方）
[16] Olares Docs 官网 — https://docs.olares.com/ （官方）
[17] 内部 Deep Research 报告 ai-newbrands.md（113 agent 验证）— 小米智能存储定价、QNAP TS-AI642 = RK3588、被否决 TOPS 说法 — /Users/pengpeng/seo/directions/hardware/reports/_archived/ai-newbrands.md
[18] UGREEN NAS CA 官网 — AI NAS 功能介绍 — https://nas-ca.ugreen.com/pages/ugreen-ai-nas-feature-introduction （官方）

（SEO 搜索量数字全部来自既有报告的 SEMrush US 数据：ugreen-nas.md / zspace.md / minisforum.md / zimaos-zimacube.md / ai-newbrands.md）

## Findings

1. UGREEN NASync iDX6011 Pro：Intel Core Ultra 7 255H（16C/16T），64GB LPDDR5X（不可扩展），6 SATA bay（最高 196TB），双 10GbE，双 TB4，PCIe Gen4 x8，OCuLink，前置 3.71" 触摸屏，UGOS Pro；本地 AI 管线 "Uliya"（Qwen3 4B FP16，~8 tok/s）+ MCP tool-calling 可控制 Docker/媒体/系统；"super early bird" $1,559。[1][2][3]
2. UGREEN iDX6011（基础版）：Intel Core Ultra 5 125H（14C）；同系列 AI 功能。x86。[3]
3. UGREEN DXP4800 Plus：Intel Pentium Gold 8505（5C，x86 12代），8GB DDR5（可扩至 64GB），4-bay SATA + 2 M.2，10GbE+2.5GbE，UGOS Pro，AI Photo Magic + semantic search，无独立 NPU；美区约 $599–$700。[4][2]
4. Minisforum N5 Pro：AMD Ryzen AI 9 HX PRO 370（Zen5/5c，12C/24T，5.1GHz），Radeon 890M，最高 96GB DDR5 ECC，5 SATA bay + 3 M.2/U.2（最高 ~144–150TB），10GbE+5GbE，PCIe x16 + OCuLink，预装 MinisCloud OS；NPU 官方标 50 TOPS（营销页也出现 80 TOPS 全平台合计）；barebone $1,019（美区 store 促销 $899）。[5][6]
5. Aoostar WTR Max：AMD Ryzen 7 PRO 8845HS（8C/16T，Zen4，NPU 16 TOPS）或 Intel i5-1235U 版；11 盘位（6 SATA + 5 M.2），双 10GbE + 双 2.5GbE，USB4，OCuLink；不带专有 OS，主推 TrueNAS/Proxmox/Unraid；AMD 版 $659–$699，Intel 版 $559。[7][8]
6. ZimaCube 2 / 2 Pro：Intel Core i3-1215U（标准，$799）/ i5-1235U（Pro，$1,299 含 10GbE；Creator Pack $2,499 含 RTX Pro 2000），6 SATA bay + 第 7 位 4×M.2，双 TB4，ZimaOS；AI 走自托管应用 / GPU 模组而非内置 LLM。[9][10]
7. 极空间 ZSpace Z425：Intel Core Ultra 5 225H（14C，4.9GHz）+ Arc 130T GPU + AI Boost NPU，官方标 83 TOPS（GPU 63 + NPU 13 + CPU 7），8 盘位（4 SATA + 4 M.2），10GbE + 1GbE，双 TB4；"AI Space" 自然语言语义搜索，全部本地计算不上云；¥7,999。[11][17]
8. LincStation N2：Intel N100（4C，Alder Lake-N），16GB LPDDR5（不可扩展），6-bay 全闪（2 SATA + 4 M.2 NVMe），10GbE，附 Unraid Starter License，可装 TrueNAS；$409–$449。非 AI-native，纯存储盒。[14]
9. QNAP TS-AI642：Rockchip RK3588 ARM SoC，6-bay，NPU（厂商宣称 6 TOPS，具体数字曾被 deep-research 否决）；ARM 架构本身非障碍（Olares 经 script 支持 ARM Linux），真正障碍是 QTS 固件锁定 → 实务 Low/[unverified]。[12][17]
10. Synology DS925+：AMD Ryzen（x86-64 嵌入式，媒体报 R1700/V1500B 说法不一 [unverified]），4-bay，无 NPU/独显，DSM 7.3 本地相册 AI（人脸/物体/语义搜索），~$640（澳区报价高至 $1,029）；无 PCIe，GPU 推理需 QNAP。DSM 锁定，实务上难装第三方 OS。[13][12]
11. 小米智能存储：2026-07-01 众筹，¥2,299（4TB）起；SoC 未确认 [unverified]。[17]

## Deep Read Notes

- **UGREEN iDX6011 Pro（[2] XDA 全文）**：Uliya 不只是 chatbot，是带 tool-calling 的完整 NAS 管理助手，底层用 MCP 在 UGOS 内置应用间派发动作（找并播放电影、按描述找照片、找歌设睡眠定时、搜 Docker 镜像/容器、调风扇转速、切电源策略、查设备/用户信息）；Qwen3 4B 本地跑，查询与文件内容不出设备；另有 Uliya-v 2B 视觉模型（~16 tok/s）做图像识别。**这是目前最接近 "NAS 上的 Agent" 的产品，与 Olares 的 Personal Agent 叙事正面重叠——但 Uliya 绑死 UGOS 生态、闭源。** [2]
- **iDX6011 Pro 实测短板（[1] techreviewer）**：AI 首装要下载数 GB 模型/服务；智能搜索经常无结果或不可靠；相册识别质量不及 Google/Apple/Synology Photos；本地 Qwen ~8 tok/s，比云模型慢且不精。→ 印证"营销 AI-native 与实际体验有落差"。[1]
- **ZimaCube 2（[10] Notebookcheck）**：定位"不止是 NAS，是自托管强机"，标准版换掉 N100 上 i3-1215U，支持双 TB4/eGPU；Pro/Creator 才有更强 AI/3D 扩展。**AI 靠开放应用生态与可选 GPU，而非内置 LLM——和 Olares 路线最像，且同为中国团队 IceWhale（ZimaOS/CasaOS）。** [10][9]
- **Aoostar WTR Max**：几乎"裸机 + BYO-OS"，官方直接教用户装 TrueNAS/Proxmox/Unraid[7]——**天然的 Olares OS x86 安装宿主，且 11 盘位存储密度极高。** [7][8]

## Gaps

- **"AI-native" / TOPS 营销普遍不可尽信**：厂商 TOPS 常把 CPU+GPU+NPU 相加（极空间 83、Minisforum 80）或只报 NPU（Minisforum 50、AMD 8845HS 16）；deep-research 曾 0-3 否决 QNAP TS-AI642 具体 NPU 数、UGREEN "96 TOPS"、TerraMaster "全球首款 AI 原生 NAS"。本报告只作定性引用。[17]
- **[反向复核 1]** UGREEN Uliya 的 MCP tool-calling 是否为常态可用功能，还是评测机的早期版本？多篇提到智能搜索不稳定[1]，需追踪 OTA 更新（官方注明多项 AI 功能 2025-12–2026-06 才 OTA 补齐 [18]）。
- **[反向复核 2]** 小米智能存储、极空间 Z423/Q2C 的确切 SoC 架构（x86 还是 ARM）未逐一核到官方规格页，Olares OS 适配标 [unverified]。
- **[反向复核 3]** Synology DS925+ 具体 CPU 型号第三方说法不一（R1700 / V1500B / V1600B）[13][12]；且即便是 x86-64，DSM 锁定下能否实际安装 Olares OS 未验证，实务判 Low/None。
- SEMrush "ai nas" 泛词本身的搜索量未在既有报告中取到确切数字，需补一次 keyword_overview（当前留空，不臆造）。
