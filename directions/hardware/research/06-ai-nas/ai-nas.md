# AI NAS 品类研究报告（按型号 · SEO 用）

> 研究日期: 2026-07-05 | 来源数: 32 | 字数: ~3200 | 模式: Standard | AS_OF: 2026-07-05 | 口径: 硬件为准（内置 GPU / 可否内插独显 / eGPU 接口 / 售价 / 购买链接）
>
> 本报告已合并原「高端发烧 AI NAS」（可插独显 / 大内存机型）为同一张型号表——两者本属同一品类，只是 GPU 路径不同。**不判断各机型本地 LLM 效果，也不判断能否装 Olares**（用户的钱花给 NAS 厂商，我们要的是"对比时买 Olares One"）；只穷举**具体在售型号**的硬件事实与购买入口。

## 摘要

"AI NAS" 在 2025–2026 从营销词变成真实在售品类：在网络存储上叠加本地 AI（语义搜索、相册识别、OCR、可选本地 LLM）。按 **GPU 路径** 分三类硬件形态：① **仅 iGPU/NPU**（UGREEN DXP、极空间、LincStation——存储优先，无独显扩展）；② **可内插低剖面独显 / OCuLink eGPU**（Minisforum N5 Pro、MS-A2/MS-01、Aoostar WTR Max、ZimaCube 2 Pro——NAS 机箱内 PCIe 多**无辅助供电、限 ≤75W**，重卡走 OCuLink 外接）；③ **turnkey 预装独显**（ZimaCube 2 Creator Pack，预装 RTX Pro 2000 16GB）。畅销机型绝大多数用 x86（Intel Core Ultra/N 系、AMD Ryzen），少数用 ARM SoC（QNAP TS-AI642 = RK3588）。对 Olares 的意义：这些机型是 **Olares One（$3,999 / RTX 5090 Mobile 24GB / 96GB DDR5）的直接对标**——存储盒子 + 弱 iGPU/NPU 或需外接 GPU vs 一体机 + 24GB GDDR7 独显 + 开源全栈个人云 OS。

## 一、单元定位

**AI NAS 是什么**：以存储为底座、内置本地 AI 能力的家用/prosumer 网络存储。核心 AI 功能收敛为四类——语义搜索、相册人脸/物体识别、OCR/文档分析、可选本地 LLM 聊天。[3][4][18] 置信度：高。

**GPU 路径是本品类的关键分野**（决定能否本地跑更大模型）：
- **仅 iGPU/NPU**：靠核显 + NPU，只适合小模型/识别类，无独显扩展位。
- **内插独显**：NAS 机箱内 PCIe 槽多为**低剖面、无 6/8-pin 辅助供电、≤70–75W**[1][5]，只能插 RTX 2000 Ada / A2000 级低功耗专业卡。
- **OCuLink / TB eGPU**：外接大卡（4090/5090 级）的通道，N5 Pro / WTR Max / ZimaCube 2 Pro 走这条。
- **turnkey 预装独显**：目前量产仅 ZimaCube 2 Creator Pack（预装 RTX Pro 2000 16GB）。

**对 Olares 的意义**：AI NAS = 存储优先、GPU 弱或需外接、AI 应用多闭源绑生态；Olares One = 一体机 + 24GB GDDR7 独显 + 开源全栈个人云 OS（应用商店 + 本地推理 + 远程访问）。品类越热，"AI NAS vs 个人云一体机" 的对比需求越大。置信度：高。

## 二、AI NAS 型号表（一行一型号 · 硬件口径）

列口径：**内置 GPU** = CPU 自带核显 / SoC GPU；**可内插独显** = 机箱内 PCIe 槽及其供电/尺寸限制；**eGPU 接口** = 外接 GPU 通道；**购买** = 官方产品/购买页。

| 型号 | 厂商 | 内置 GPU（iGPU/NPU）| 可内插独显（PCIe/供电）| eGPU 接口 | 内存 | 盘位 | 价格 | 购买 |
|------|------|------|------|------|------|------|------|------|
| NASync iDX6011 Pro | UGREEN | Core Ultra 7 255H（Arc iGPU + NPU）| **无内插 dGPU 槽** | OCuLink（AI 栈未走 dGPU）[8] | 64GB LPDDR5X（焊接）| 6 SATA + 2 M.2 | $1,559–2,599 | [nas.ugreen.com](https://nas.ugreen.com/) |
| NASync iDX6011 | UGREEN | Core Ultra 5 125H（Arc iGPU）| 无内插 dGPU 槽 | OCuLink | 可扩 | 6-bay | 预售 [3] | [nas.ugreen.com](https://nas.ugreen.com/) |
| NASync DXP4800 Plus | UGREEN | Pentium Gold 8505（UHD iGPU，无 NPU）| 无 | 无 | 8GB→64GB | 4 SATA + 2 M.2 | ~$599–700 [4] | [DXP4800 Plus](https://nas.ugreen.com/products/ugreen-nasync-dxp4800-plus-nas-storage) |
| ZSpace Z425 | 极空间 | Core Ultra 5 225H（Arc iGPU + NPU）| [unverified] | — | 可扩 | 8-bay（4 SATA+4 M.2）| ¥7,999 [11] | [m.zspace.cn/z425](https://m.zspace.cn/z425/) |
| ZSpace Z423 / Q2C | 极空间 | [unverified]（推测 x86 iGPU）| [unverified] | — | — | 多盘位 | 中端 | [zspace.cn](https://www.zspace.cn/) `[待补型号页]` |
| N5 Pro | Minisforum | Ryzen AI 9 HX PRO 370（Radeon 890M + NPU）| **内 PCIe x16（电 x8）LP ≤75W** | **OCuLink PCIe4**（实测外接 4090）[5] | 96GB ECC | 5 SATA + 3 M.2/U.2 | $1,019 起 / 套装 $1,597 | [N5 Pro AI NAS](https://store.minisforum.com/products/minisforum-n5-pro-ai-nas) |
| N5 / N5 Air | Minisforum | Ryzen 7 255（Radeon iGPU）| 内 PCIe x16 | OCuLink | 可扩 | 5-bay | ~$519 起 [6] | [store.minisforum.com](https://store.minisforum.com/) |
| WTR Max（AMD）| Aoostar | Ryzen 7 PRO 8845HS（Radeon 780M）| **无内槽** | **OCuLink PCIe4 x4**（eGPU 坞）[2] | 最高 128GB ECC | 11（6 SATA+5 M.2）| 裸机 $659 | [WTR Max](https://aoostar.com/products/aoostar-wtr-max-amd-r7-pro-8845hs-11-bays-mini-pc) |
| WTR Max（Intel）| Aoostar | i5-1235U（Iris Xe）| 无内槽 | OCuLink PCIe4 x4 | 96GB | 11 | 裸机 $559 | [WTR Max](https://aoostar.com/products/aoostar-wtr-max-amd-r7-pro-8845hs-11-bays-mini-pc) |
| ZimaCube 2 Standard | IceWhale | i3-1215U（UHD iGPU）| 内插 LP GPU ≤75W | TB4 eGPU | 8GB→64GB | 6 SATA + 4 M.2 | $799 [9] | [shop.zimaspace.com](https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas) |
| ZimaCube 2 Pro | IceWhale | i5-1235U（Iris Xe）| 内插 LP GPU ≤75W | TB4 eGPU | 16GB→64GB | 6 SATA + 4 M.2 | $1,299 [9] | [shop.zimaspace.com](https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas) |
| **ZimaCube 2 Creator Pack** | IceWhale | i5-1235U | **预装 RTX Pro 2000 16GB**（PCIe x4@x16，≤75W）| TB4 eGPU | 64GB | 6 SATA + 4 M.2 | $2,499 [4] | [shop.zimaspace.com](https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas) |
| MS-A2 | Minisforum | Ryzen 9 9955HX（Radeon iGPU）| **内 PCIe4 x16（电 x8）LP** | — | 96GB（实测 128GB）| 3 M.2/U.2（盘位需外接）| $639–839 [17] | [store.minisforum.com](https://store.minisforum.com/) `[待补型号页]` |
| MS-01 | Minisforum | i9-13900H（Iris Xe）| **内 PCIe x16（电 x8）半高单槽**（RTX 2000 Ada 级）| — | 64–96GB | 3 M.2 + U.2 | ~$500–750 [18] | [store.minisforum.com](https://store.minisforum.com/) `[待补型号页]` |
| LincStation N2 | LincPlus | Intel N100（UHD iGPU）| 无 | 无 | — | 6-bay 全闪（2 SATA+4 M.2）| $409–449 [14] | [LincStation N2](https://www.lincplustech.com/products/lincstation-n2-network-attached-storage.html) |
| 小米智能存储 | 小米 | [unverified] | [unverified] | — | — | 桌面盒 | ¥2,299 起 [17] | [mi.com](https://www.mi.com/) `[待补型号页]` |
| TS-AI642（对比行）| QNAP | Rockchip RK3588（ARM，Mali GPU + NPU）| 无 | 无 | 8GB（不可扩）| 6-bay | $749 | [qnap.com/ts-ai642](https://www.qnap.com/en/product/ts-ai642) |
| DS925+（对比行）| Synology | AMD Ryzen（无 iGPU）| 无 | 无 | 32GB | 4-bay | ~$640–1,029 | [synology.com/DS925+](https://www.synology.com/en-global/products/DS925+) |

> **DIY 路线（非成品，可购机箱/自组）**：**Jonsbo N6 一体**（全长独显如 RTX 3090/5060Ti，9×3.5"，机箱 [$150–200](https://www.jonsbo.com/en/products/N6Black.html)）与 **4U 机架多卡**（4×RTX 4090 / RTX Pro 6000，$8k–20k+）是自组 NAS+GPU 的两条路，适合"自建 AI 服务器"内容，但非一键购买的 NAS 型号。

物理约束提醒：**"能内插/OCuLink 接卡" ≠ "适合长期满负载"**——内槽 ≤75W 无辅助供电 + 散热受限，重负载需 OCuLink eGPU 或 DIY 大机箱。[1][5] 置信度：高（规格取自官方/权威评测，标 [unverified] 者除外）。

## 三、每型号候选 SEO 关键词

| 型号 | 候选关键词（附既有 SEMrush US 量）|
|------|------|
| UGREEN iDX6011 Pro | `ugreen idx6011 review`、`ugreen ai nas`（590）、`ugreen nas vs synology`（210, KD13）、`idx6011 vs olares one` |
| UGREEN DXP4800 Plus | `dxp4800 plus review`、`ugreen nas review`（480, KD19）、`ugreen nas vs olares` |
| 极空间 Z425 | `极空间`（4,400, KD20）、`极空间z2pro`（210, KD4）、`zspace z425 review`、`极空间 vs olares one` |
| Minisforum N5 Pro | `minisforum n5 pro`（880）、`minisforum n5 pro ai nas`（260）、`n5 pro oculink gpu`、`n5 pro vs olares one` |
| Minisforum MS-A2 / MS-01 | `minisforum ms-a2 nas`、`ms-01 gpu`、`ms-a2 vs ms-01` |
| Aoostar WTR Max | `aoostar wtr max review`、`wtr max oculink egpu`、`wtr max truenas`、`11 bay nas` |
| ZimaCube 2 / Creator | `zimacube`（880, KD43）、`zimacube 2 creator`、`zimacube rtx pro 2000`、`zimacube vs olares one` |
| LincStation N2 | `lincstation n2 review`、`all flash nas`、`n2 vs olares` |
| 小米智能存储 | `小米 nas`（170, KD23）、`xiaomi nas`（20）|
| 泛品类 | `ai nas`（量[unverified]）、`nas with gpu`、`best ai nas 2026`、`ai nas vs personal cloud` |

置信度：高（搜索量数字取自既有报告）；`ai nas` 泛词量未取到，标 [unverified] 不臆造。

## 四、对标 Olares One（消息 A · 主打）

Olares One（$3,999、RTX 5090 Mobile **24GB GDDR7**、Core Ultra 9 275HX、96GB DDR5、2TB NVMe）与本组 AI NAS 的差异点，落在**硬件形态 + 软件栈**两层：

- **GPU 层**：绝大多数 AI NAS 只有 iGPU/NPU 或需外接 GPU；唯一 turnkey 带独显的 ZimaCube 2 Creator Pack 也只有 16GB VRAM。Olares One 自带 24GB GDDR7 独显，本地推理上限更高。
- **形态层**：AI NAS 是"存储盒子 + 后加 AI"；Olares One 是"个人云一体机"，开箱即私有 AI 服务。
- **软件层**：AI NAS 的 AI 应用多闭源、绑死自家 OS（如 UGREEN Uliya 绑 UGOS）；Olares 是开源全栈个人云 OS（应用商店 + 本地推理 + 远程访问）。[2][15]

内容落点：`<model> vs olares one`、`ai nas vs personal cloud`、`nas with gpu vs olares one`、`zimacube creator vs olares one`。置信度：高；依据 [2][15] 与型号硬件事实。

> 注：本报告**不逐型号判断本地 LLM tok/s 与"能否装 Olares"**——前者是评测噪声、后者不是我们要引导的动作（用户已把钱花给 NAS 厂商，我们要的是对比时选 Olares One）。

## 五、诚实缺口

- **TOPS / "AI-native" 营销不可尽信**：厂商常把 CPU+GPU+NPU 相加（极空间 83、Minisforum 80）或单报 NPU（Minisforum 50、AMD 8845HS 16）；prior deep-research 曾 0-3 否决 QNAP TS-AI642 具体 NPU 数、UGREEN "96 TOPS"、TerraMaster "全球首款 AI 原生 NAS"。本表只记硬件事实、不引用 TOPS。[17]
- **部分型号规格 [unverified]**：极空间 Z423/Q2C、小米智能存储的确切 SoC / 内插能力未逐一核官方页；MS-01 内存上限口径不一（64–128GB）；N5 Pro 内插全长独显缺 teardown。
- **部分购买链接为品牌站首页**：iDX6011/iDX6011 Pro、MS-A2/MS-01、极空间 Z423、小米 缺型号级直链，暂链品牌站并标 `[待补型号页]`。
- **缺口**：`ai nas` / `nas with gpu` 泛词的 SEMrush 量未取到，待补 keyword_overview。

## 六、关键发现

1. **GPU 路径是品类分野**：仅 iGPU/NPU（DXP/极空间/LincStation）→ 内插 LP 独显（N5 Pro/MS 系/ZimaCube Pro）→ OCuLink eGPU（N5 Pro/WTR Max）→ turnkey 预装独显（ZimaCube Creator）。选题可按"能不能加显卡"分层。
2. **turnkey「NAS + 预装独显」目前只有 ZimaCube 2 Creator Pack**（$2,499，16GB VRAM）；其余要么无扩展、要么靠内插/OCuLink 自己加卡。[4][1]
3. **NAS 内插独显有硬约束**（≤75W 无辅助供电），重卡走 OCuLink（N5 Pro/WTR Max）或 DIY 大机箱（Jonsbo/4U）。[1][5]
4. **UGREEN 是 SEO 与产品双料头号对标**：`ugreen nas` 22,200/月、`ugreen ai nas` 590、`ugreen nas vs synology` KD 仅 13；iDX6011 Pro 硬件强但无内插 dGPU 槽、AI 软件闭源绑 UGOS。[2][8]
5. **差异化定位清晰**：AI NAS 存储优先、GPU 弱或需外接、AI 多闭源；Olares One 一体机 + 24GB GDDR7 独显 + 开源全栈个人云 OS。[2][15]

## 参考文献

[1] IceWhale — ZimaCube 2 产品页（official）— https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas
[2] XDA — Ugreen iDX6011 Pro vs Synology — https://www.xda-developers.com/ugreen-most-powerful-nas-exposes-synology/
[3] Galaxus — Ugreen AI-NAS iDX6011 / Pro 详解 — https://www.galaxus.at/en/page/ugreens-ai-nas-idx6011-and-idx6011-pro-in-detail-core-ultra-local-ai-and-up-to-196-tb-41592
[4] It's FOSS — ZimaCube 2 Review — https://itsfoss.com/zimacube-2-review/
[5] Notebookcheck — Minisforum N5 Pro review — https://www.notebookcheck.net/Minisforum-N5-Pro-World-s-first-AI-NAS-with-AMD-Ryzen-AI-9-HX-PRO-370-IFA-2025-Award-winner-review.1142209.0.html
[6] Guru3D — Minisforum N5 Pro Specs & Price — https://www.guru3d.com/story/minisforum-n5-pro-ai-nas-with-ryzen-ai-9-hx-pro-370-specs-price/
[7] NAS Compares — Aoostar WTR Max review — https://nascompares.com/review/aoostar-wtr-max-nas-review-nas-perfection/
[8] NASCompares — UGREEN iDX6011 Pro Review — https://nascompares.com/review/ugreen-idx6011-pro-ai-nas-review-real-retail-local-ai-nas/
[9] Zima Store — ZimaCube 2 — https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas
[10] Notebookcheck — ZimaCube 2 review — https://www.notebookcheck.net/ZimaCube-2-review-This-home-server-is-more-than-just-a-NAS-a-self-hosting-powerhouse.1316114.0.html
[11] 极空间官网 — Z425 — https://m.zspace.cn/z425/
[12] Need to Know IT — Synology vs QNAP vs UGREEN for AI — https://needtoknowit.com.au/blog/synology-vs-qnap-vs-ugreen-for-ai-features-australia/
[13] Synology — DiskStation DS925+ — https://www.synology.com/en-global/products/DS925+
[14] LincPlus — LincStation N2 — https://www.lincplustech.com/products/lincstation-n2-network-attached-storage.html
[15] Olares One — https://one.olares.com/
[16] Aoostar — WTR Max 产品页（official）— https://aoostar.com/products/aoostar-wtr-max-amd-r7-pro-8845hs-11-bays-mini-pc
[17] ServeTheHome — Minisforum MS-A2 Review — https://www.servethehome.com/minisforum-ms-a2-review-an-almost-perfect-amd-ryzen-intel-10gbe-homelab-system/
[18] minipc-review — Minisforum MS-01 Review — https://minipc-review.com/en/review-minisforum-ms-01-mini-pc
[19] Jonsbo — N6 NAS Case（official）— https://www.jonsbo.com/en/products/N6Black.html
[20] Minisforum — N5 Pro AI NAS 产品页（official）— https://store.minisforum.com/products/minisforum-n5-pro-ai-nas
[21] UGREEN NAS US — DXP4800 Plus（official）— https://nas.ugreen.com/products/ugreen-nasync-dxp4800-plus-nas-storage
[22] TechPowerUp — UGREEN NASync iDX6011 Pro Review — https://www.techpowerup.com/review/ugreen-nasync-idx6011-pro/

> 关联：清单 [devices.md 组六](/Users/pengpeng/seo/directions/hardware/devices.md)；企业/机架 NAS 见 [enterprise-nas.md](/Users/pengpeng/seo/directions/hardware/research/07-enterprise-nas/enterprise-nas.md)；dGPU 显存线见 [dgpu-24gb-plus.md](/Users/pengpeng/seo/directions/hardware/research/04-dgpu/dgpu-24gb-plus.md)；NAS OS 竞品见 [reports/08-nas-os/](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os)。既有产品报告：[ugreen-nas](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/ugreen-nas.md)、[zspace](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/zspace.md)、[zimaos-zimacube](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/zimaos-zimacube.md)、[minisforum（已归档）](/Users/pengpeng/seo/directions/hardware/reports/_archived/minisforum.md)。
