---
task_id: 01
role: 高端 AI NAS（ZimaCube/UGREEN 顶配）分析师
status: complete
sources_found: 9
---

## Sources
[1] ZimaCube 2 Personal Cloud Home NAS | https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[2] ZimaCube 2 : Open NAS for AI & Self-Hosting（IceWhale 发布稿）| https://shop.zimaspace.com/blogs/zima-campaign-hub/zimacube-2-open-nas-ai-self-hosting | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[3] Zimacube 2 NAS Revealed - Everything We Know | https://nascompares.com/news/zimacube-2-nas-revealed-everything-we-know/ | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 8/10
[4] ZimaCube 2 Review: Combining Self-hosting, NAS and Local AI | https://itsfoss.com/zimacube-2-review/ | Source-Type: journalism | As Of: 2026-06 | Authority: 8/10
[5] ZimaCube 2 review: self-hosting powerhouse | https://www.notebookcheck.net/ZimaCube-2-review-This-home-server-is-more-than-just-a-NAS-a-self-hosting-powerhouse.1316114.0.html | Source-Type: journalism | As Of: 2026-06 | Authority: 8/10
[6] ZimaCube 2 Pro Review - ServeTheHome | https://www.servethehome.com/zimacube-2-pro-review-intel-marvell-asmedia/ | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 8/10
[7] UGREEN NASync iDX6011 Pro Review (techreviewer.de) | https://en.techreviewer.de/ugreen-nasync-idx6011-pro-test/ | Source-Type: journalism | As Of: 2026-05 | Authority: 7/10
[8] UGREEN iDX6011 Pro AI NAS Review – REAL Retail Local AI NAS? | https://nascompares.com/review/ugreen-idx6011-pro-ai-nas-review-real-retail-local-ai-nas/ | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 9/10
[9] Ugreen NASync iDX6011 Pro Review | TechPowerUp | https://www.techpowerup.com/review/ugreen-nasync-idx6011-pro/ | Source-Type: journalism | As Of: 2026-05 | Authority: 8/10

## Findings
- **ZimaCube 2 Creator Pack（系列顶配）**：Intel Core i5-1235U（10C/12T）；64GB DDR5-4800；1TB PCIe Gen4 系统盘；**预装 NVIDIA RTX Pro 2000（16GB VRAM）**；6×SATA + 第7位 4×M.2 NVMe（~3200 MB/s）；**PCIe 4.0 x4（物理 x16）+ PCIe 3.0 x2（物理 x8）**；10GbE + 2×2.5GbE；双 Thunderbolt 4；247W 电源；**$2,499**。[1][2][3]
- **ZimaCube 2 Pro（可自插独显顶配，不含 GPU）**：同 i5-1235U；出厂 16GB DDR5（**SODIMM 可扩至 64GB**）；256GB 系统 SSD；扩展/网络/PCIe 同 Creator；需自购 **低剖面单/双槽 GPU，TDP <75W**；**$1,299**。[1][3][6]
- **ZimaCube 2 Standard（入门顶配）**：Intel Core i3-1215U（6C）；8GB DDR5（**可扩至 64GB**）；256GB SSD；6×SATA + 第7位 4×M.2（~800 MB/s）；**仅 2×2.5GbE（无 10GbE）**；双 PCIe 槽位同架构；双 TB4；**$799**。[1][3][5]
- **ZimaCube 本地 LLM 能力（有 GPU 证据）**：Pro 评测机自插 **NVIDIA RTX 2000 Ada 16GB**，Ollama + Open WebUI；**7B、13B 全量驻留 VRAM、无 spillover**，响应「够快」；**32B+ 开始吃紧，量化版仍可跑**；DeepSeek-R1、Qwen、Llama 实测；**无 GPU 时仅 CPU 推理，慢且模型受限**。[4]
- **ZimaCube GPU/扩展约束**：官方 PCIe 槽 **无辅助供电**，仅支持 **低剖面 ≤75W**；更高功耗需 **TB4 外接 eGPU 坞**；Notebookcheck 报 **70W GPU/PCIe 上限**。[1][5]
- **UGREEN NASync iDX6011 Pro 满配**：Intel **Core Ultra 7 255H**（16C/16T，最高 5.1GHz）；**64GB LPDDR5X 8533（焊接，不可扩）**；集成 **Intel Arc 140T** + **NPU**（厂商宣称合计 **96 TOPS**）；6×SATA（最高 **196TB** 标称）+ 2×M.2 PCIe4 + **128GB 系统 SSD**；**PCIe Gen4 x8 ×1（内）+ OCuLink ×1（Pro 独占，可接 GPU 坞）**；双 10GbE；双 TB4；3.71" 触摸屏；UGOS Pro。[7][8][9]
- **UGREEN 本地 LLM（有 tok/s 证据）**：内置 **Uliya** 助手；本地 **Qwen3 4B** 约 **~8 tok/s**；**Uliya-v 2B** 视觉模型约 **~16 tok/s**；首装需下载 ~9.7GB 模型；**NPU 实测几乎未用，多走 CPU**；UGOS 内 **不可自装第三方 LLM**，更大模型需 Docker/VM/换 OS（TrueNAS/Unraid/Proxmox 可装）。[7][8]
- **UGREEN OCuLink/eGPU vs 内置 AI**：NAS Compares 实测 **OCuLink GPU 坞可被识别**，但当前 Uliya 本地 AI **主要依赖 CPU/NPU/iGPU，未优化走外接独显**；内 PCIe x8 更适合网卡/存储扩展卡。[8]
- **价格带（AS_OF 2026-07-05）**：ZimaCube 2 三档 **$799 / $1,299 / $2,499**；UGREEN iDX6011 Pro **Super Early Bird $1,559**（Kickstarter）、Early Bird $1,819、**MSRP $2,599**。[1][7][8]
- **对比结论**：**可内插独显跑 Ollama 的 turnkey 顶配 = ZimaCube 2 Creator Pack**（16GB VRAM，13B 级流畅）；**UGREEN iDX6011 Pro** 算力在 CPU/大内存/NPU，**满配无内插 dGPU 槽**，本地 LLM 官方仅 **4B 级 ~8 tok/s**，硬件余量需 Docker/换 OS 或 OCuLink eGPU 才能对标 ZimaCube+独显。[4][7][8]

## Deep Read Notes
### Source [4]: ZimaCube 2 Review (It's FOSS)
Key data: 评测机为 Pro + 自购 RTX 2000 Ada 16GB；Ollama/Open WebUI/AnythingLLM；7B & 13B 全 VRAM；32B+ 需量化；无 GPU = CPU 慢推理。
Key insight: ZimaCube 的 LLM 能力 **不来自内置 OS LLM**，而来自 **开放 PCIe + 用户自装 GPU + Ollama 生态**。
Useful for: ZimaCube Pro/Creator 本地 LLM **模型规模上限（13B 全精度舒适区）** 的唯一定量体验源；Creator Pack 可类推（同 16GB VRAM GPU）。

### Source [7]: UGREEN iDX6011 Pro (techreviewer.de)
Key data: Qwen3 4B **~8 tok/s**；Uliya-v 2B **~16 tok/s**；NPU 几乎闲置；智能搜索/相册 AI 不稳定；64GB 焊接；Idle 45–55W、负载 70–90W+。
Key insight: **硬件远超 UGOS AI 软件成熟度**——96 TOPS 营销 vs 实测 CPU 为主、仅 4B 官方模型。
Useful for: iDX6011 Pro **满配内存/AI 性能/token 速率** 与 **价格/功耗** 基准。

### Source [8]: UGREEN iDX6011 Pro (NAS Compares)
Key data: 完整规格/定价表；OCuLink GPU 坞识别成功；AI 层「未完成」；RAID5+缓存 ~950/670 MB/s；NVMe ~5.5–6 GB/s。
Key insight: Pro 的 **OCuLink/PCIe 是 homelab 扩展 story**，但 **出厂 AI 不依赖独显**；Kickstarter 购买路径增加交付/功能风险。
Useful for: **PCIe/OCuLink 能力**、**MSRP $2,599**、以及 **「NAS 插/接 GPU 不等于 LLM 已优化」** 的权威反证。

## Gaps
- **ZimaCube Creator Pack 预装 RTX Pro 2000 无独立 tok/s benchmark**；现有 LLM 证据来自 Pro + RTX 2000 Ada 自装 [4]，Creator 仅官方宣称「local LLM inference」[2]，需补 Creator 开箱 Ollama 基准。
- **[相反主张] NAS 插独显受散热/供电/物理限制**：ZimaCube PCIe **无 6/8-pin 辅助供电**，内插 GPU **≤70–75W 低剖面** [1][5]；更高 TDP 只能 TB4 eGPU [1]。UGREEN 虽有 OCuLink，但 **AI 栈未走 dGPU**——「能插/能认卡」≠「适合长期满负载 LLM」。[8]
- **UGREEN 64GB LPDDR5X 焊接不可升级** vs ZimaCube 64GB SODIMM 可扩：iDX6011 Pro 换 OS 跑 70B 量化仍受 **64GB 硬顶**。[7][8]
- **UGREEN 本地模型库封闭**（测试期仅 2 个官方模型）[7]；与 ZimaCube 开放 Ollama 任意拉模型形成产品哲学差异。
- **Kickstarter vs 零售**：iDX6011 Pro 评测多基于众筹/预发布机 [8]；2026-07 零售现货价格、AI OTA 成熟度待复核。

## END
