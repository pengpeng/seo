# hardware 方向审计与重构建议：从"厂商为单元"到"具体产品为单元（一行一产品）"

> 审计日期: 2026-07-05 | AS_OF: 2026-07-05 | 基线: [devices.md](/Users/pengpeng/seo/directions/hardware/devices.md) | research: [research/](/Users/pengpeng/seo/directions/hardware/research) **8 份**芯片/品类 deep-research（按 `<NN-组>/` 分目录）

本文是 hardware 方向的审计交付：(1) 逐条列出原厂商级报告的遗漏；(2) 给出"具体产品为单元（一行一产品）"的重构建议；(3) 两条 Olares 信息 × 各单元适配总表；(4) 营销稿取舍说明；(5) 有意排除项（Intel Core Ultra / Snapdragon X）的理由。所有事实型主张见 [research/](/Users/pengpeng/seo/directions/hardware/research) 8 份报告的引证。

> **结构**：devices.md 以**一行一个具体产品**组织，`research/` 与 `reports/` 均**按组分目录**（`<NN-组>/…`，对齐 commerce/iot）。八大组见下（AI NAS 已含高端发烧机型、企业 NAS 独立成组七、个人云/NAS OS 竞品为组八）。品牌级旧报告归档 `reports/_archived/`（**19 份**：品牌 13 + 传统 NAS 5 + 综述 1）。

## 一、hardware 方向要回答的两条信息

面向"正在买/已买别家硬件"的人群，hardware 方向只讲两件事：

- **信息 A — 买 Olares One**：Olares One（$3,999：RTX 5090 Mobile 24GB + Core Ultra 9 275HX + 96GB DDR5）作为软硬一体、开箱即用的私有云整机，对标各家芯片整机与"单买一块用不满的大卡"的散装方案。
- **信息 B — 在已购设备上装 Olares**：（2026-07-05 复核 docs.olares.com）Olares **跨平台**——Linux（x86-64 裸机 ISO / script，Ubuntu 22.04-25.04·Debian 12-13）、**ARM Linux（树莓派即 ARM 路径，用同一 script）**、**macOS（Monterey 12+，含 Apple Silicon，script/Docker，有功能限制）**、**Windows（WSL2）**。**"ARM not supported" 只出现在裸机 ISO 安装器页**，不是"Mac/ARM 不能装 Olares"。Olares One 只是官方选了 x86-64 + NVIDIA 做最佳开箱体验。因此信息 B 的分层维度**不是"能不能装"（几乎都能）**，而是**"体验层级"**：① x86-64 Linux + NVIDIA = 满血裸机（全功能 + 最成熟 GPU 加速）；② x86-64 Linux + AMD（含 Ryzen AI Max APU，经 ROCm）/ Intel 核显 = 亦被加速；③ macOS/Windows = 在现有系统上跑一层（Mac 有功能限制、Apple GPU 不被加速）；④ ARM Linux = script 路径；⑤ 成品 NAS = 看固件是否锁定。**GPU 加速口径：NVIDIA 最成熟（全 app）；AMD（含 Ryzen AI Max APU / Radeon，经 ROCm）与 Intel 核显均已支持；仅 Apple GPU(Metal) 不被 Olares AI 应用加速。以 docs.olares.com / GitHub 为准。**

## 二、原 34 份报告的核心遗漏（已审计）

| # | 遗漏 | 说明 | 已由哪份 research 补上 |
|---|------|------|------------------------|
| 1 | 无"芯片→型号"单元 | Strix Halo / GB10 只作平台词散落在 5+ 份厂商报告，没把"同一芯片下不同 OEM 型号"横向拉平 | [amd-ryzen-ai-max](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/amd-ryzen-ai-max.md)（26 SKU）、[nvidia-gb10](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/nvidia-gb10.md)（8 同芯 clone）|
| 2 | NVIDIA 新品未跟 | 旧 nvidia-dgx.md 把 "RTX Spark" 误当 GB10 盒子；实际 N1X 已官方定名 RTX Spark（Windows-on-Arm 笔记本芯，Fall 2026）| [nvidia-gb10](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/nvidia-gb10.md) 第三节（N1X/N1 GEO 抢发 + 命名冲突修正）|
| 3 | dGPU 未按显存线筛 | 6 份 GPU 报告混排，缺"≥24GB 才是本地 AI 可用线"的主轴；且旧口径"24GB 跑 70B"被证需限定（70B Q4_K_M ~40-43GB）| [dgpu-24gb-plus](/Users/pengpeng/seo/directions/hardware/research/04-dgpu/dgpu-24gb-plus.md)（12 型号 + 门槛线修正）|
| 4 | NAS 按厂商而非品类 | 原组按 Synology/QNAP… 逐厂列，未以"畅销 AI NAS 品类"为轴，也未按 GPU 路径（内置/内插/eGPU）拉平 | [ai-nas](/Users/pengpeng/seo/directions/hardware/research/06-ai-nas/ai-nas.md)（含高端发烧机型，一表按内置 GPU / 可内插独显 / eGPU 接口 + 购买链接）|
| 5 | 信息 B 几乎没做 | 只有 gmktec 报告零星 `mini pc linux`；缺系统化的 `install olares on <型号>` / `<型号> local llm` 词层与"能否原生装"分层 | 9 份 research 均含"两条信息 × 适配"小节与型号级切入词（新增 `install olares on rog nuc`、`install olares on aoostar wtr max` 等）|
| 7 | 企业/机架 NAS 缺位 | 原清单只到消费/prosumer AI NAS，缺企业机架线（不同买家段）| 组七 [enterprise-nas](/Users/pengpeng/seo/directions/hardware/research/07-enterprise-nas/enterprise-nas.md)（诚实标不同买家段，只打认知词；高端发烧可插独显机型已并入组六 [ai-nas](/Users/pengpeng/seo/directions/hardware/research/06-ai-nas/ai-nas.md)）|
| 6 | 兼容性口径 | Olares 跨平台（Linux x86/ARM、macOS 含 Apple Silicon、Windows WSL2），"ARM not supported" 只限裸机 ISO；GPU 加速 NVIDIA 最成熟、AMD（含 Ryzen AI Max APU 经 ROCm）/Intel 核显亦支持、仅 Apple GPU 不被加速 | [apple-m-series](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/apple-m-series.md)（仅 Apple GPU 不被加速）、[amd-ryzen-ai-max](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/amd-ryzen-ai-max.md)（APU 经 ROCm 被加速）、[nvidia-gb10](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/nvidia-gb10.md)（arm64 script + Blackwell 受支持 → 有望 High，实测 [unverified]）|

## 三、重构后的 devices.md：八大组（一行一个具体产品）

每行 = 一个具体产品；品牌报告归档、改走产品级 backlog（⬜ 待做），已是产品/单品级的报告（GPU per-model、各 AI NAS、NAS OS、nvidia-dgx、apple-silicon）保留直链。

1. **AI 加速芯片 / SoC 平台**：`amd-ryzen-ai-max`（Strix Halo 逐产品）、`nvidia-gb10`（8 机型逐行）、`apple-m-series`（Mac Studio/mini + M5 状态）。
2. **NVIDIA RTX 5090 Mobile 游戏本（新，与 GB10 并列）**：同款 5090 Mobile 24GB 的游戏本逐机型，链 `research/rtx-5090-mobile-laptops.md`；角度"同 GPU/CPU、不同形态"。
3. **ASUS ROG NUC（新，最接近 Olares One 的 BOM）**：2025（对 CPU/内存）+ 2026（对 GPU），链 `research/rog-nuc.md`；`olares one vs rog nuc` 核心素材。
4. **≥24GB 显存 dGPU（型号为单元）**：以显存线组织 GPU per-model 报告；<24GB 卡显式降权。
5. **工作站（跨厂具体型号，不按厂商分类）**：一个"工作站"组，单元是具体型号（System76 Thelio、HP Z、Lenovo ThinkStation P、Dell Precision、ASUS ProArt Station 等）。取代原"大厂 OEM 承载机（按品牌）"表。
6. **AI NAS（含高端发烧，一行一型号）**：消费/prosumer + 高端发烧可插独显机型合为一表（UGREEN iDX/DXP、极空间、Minisforum N5 Pro/MS 系、Aoostar WTR Max、ZimaCube 2/Creator、LincStation、DIY Jonsbo/4U…），按**内置 GPU / 可内插独显 / eGPU 接口 + 购买链接**组织；**已删除"传统 NAS 厂商"整张表与"新兴品牌格局"综述行（后者归档）**。链 [ai-nas](/Users/pengpeng/seo/directions/hardware/research/06-ai-nas/ai-nas.md)。
7. **企业 / 机架 / 商用 NAS（组七）**：Synology SA·HD·RS·DVA、QNAP TDS·TVS-AIh·TS-AI、iXsystems TrueNAS、45Drives/45HomeLab；诚实标"不同买家段"，只打 `synology alternative` 类认知词。链 [enterprise-nas](/Users/pengpeng/seo/directions/hardware/research/07-enterprise-nas/enterprise-nas.md)。
8. **个人云 / NAS OS 竞品（组八）**：OS 层对标 TrueNAS/Unraid/CasaOS/Umbrel，报告在 [reports/08-nas-os/](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os)。

## 四、两条信息 × 各单元适配（总表）

> 信息 B 列说明：几乎所有单元**都能装 Olares**，差异在**体验层级**与 **GPU 加速成熟度**（NVIDIA 最成熟；AMD/Intel 亦支持、成熟度随版本；仅 Apple GPU 不被加速），非"能不能装"。

| 单元 | 信息 A（对标 Olares One） | 信息 B（在设备上装 Olares） | 最大 SEO 机会 |
|------|--------------------------|------------------------|----------------|
| [amd-ryzen-ai-max](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/amd-ryzen-ai-max.md) | 强（$1.5-2.8K 整机 vs 软硬一体私有云）| **High**（x86-64，裸机 ISO/script 满血；**APU 经 ROCm 被 Olares 加速**，1.12.4 起逐步落地）| `strix halo laptop` KD9、`mini pc linux` KD8 |
| [nvidia-gb10](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/nvidia-gb10.md) | 强（同 $3-4.7K 价位正面竞争）| **有望 High**（arm64 走 script 路径同树莓派；GPU 是 Blackwell，架构受支持；arm64/DGX OS 实测 + 整合 GPU 识别 [unverified]）| `dgx spark alternative` KD12 + `dgx spark price` 2,900/mo |
| [rtx-5090-mobile-laptops](/Users/pengpeng/seo/directions/hardware/research/02-5090-laptops/rtx-5090-mobile-laptops.md) | 强（同款 5090 Mobile 24GB/常同 275HX，但游戏本非无头常驻）| **High**（x86+NVIDIA，Windows→WSL2 或双系统 Linux，GPU 完整加速；7×24 无头不理想）| `rtx 5090 laptop llm`、`<model> vs olares one` |
| [rog-nuc](/Users/pengpeng/seo/directions/hardware/research/03-rog-nuc/rog-nuc.md) | 最强（BOM 最接近：移动 GPU + HX CPU + 小整机；差私有云 OS 层）| **High**（barebone + x86 + NVIDIA，装 Olares 即"自组 Olares One"）| `olares one vs rog nuc`、`install olares on rog nuc` |
| [apple-m-series](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/apple-m-series.md) | 强（Mac Studio 本地 LLM 王 vs 私有云 OS + x86 开放）| **可装，有限制**（macOS script/Docker，含 Apple Silicon；无分布式存储/本地节点，且 **仅 Apple GPU 不被 Olares AI 应用加速**；亦可只用 LarePass 客户端）| `mac studio vs dgx spark`（+Olares One 第三选项）、`best mac for local ai` |
| [dgpu-24gb-plus](/Users/pengpeng/seo/directions/hardware/research/04-dgpu/dgpu-24gb-plus.md) | 次要（单买用不满的大卡不如整机）| **High**（大卡天然在 x86 台式机；**主打**"大卡吃灰→装 Olares"；NVIDIA 最成熟，AMD 经 ROCm/Intel Arc 亦被加速，CUDA-only app 覆盖较窄）| `cheapest 48gb gpu for llm`、`<model> vs olares one` |
| [ai-nas](/Users/pengpeng/seo/directions/hardware/research/06-ai-nas/ai-nas.md)（含高端发烧）| 强（AI NAS 存储优先、GPU 弱或需外接、AI 闭源附加 vs 一体机 + 24GB 独显 + 开源全栈）| 只记硬件（内置 GPU / 可内插独显 / eGPU 接口 + 购买链接），不逐型号判是否装 Olares | `ai nas vs personal cloud`、`ugreen nas vs synology` KD13、`nas with gpu`、`zimacube creator vs olares one` |
| [enterprise-nas](/Users/pengpeng/seo/directions/hardware/research/07-enterprise-nas/enterprise-nas.md) | 弱（**不同买家段**：PB/HA/机架 vs 个人云一体机；只打认知词 + homelab 子群）| 只记硬件（多无内置独显但有全高 PCIe 槽可加卡 + 购买链接），不逐型号判是否装 Olares | `synology alternative`、`enterprise nas vs personal cloud`、`truenas vs synology` |
| 个人云 / NAS OS（[reports/08-nas-os](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os)）| 中（OS 层对标：TrueNAS/Unraid/CasaOS/Umbrel vs Olares 开源个人云 OS）| N/A（本身是 OS 竞品，非硬件宿主）| `zimaos vs casaos` KD7、`unraid alternative`、`truenas vs olares` |

## 五、营销稿取舍说明（数据纪律）

- **不做 tokens/s benchmark、不做精确性能对比**：能力只用"内存/显存档位"定性表述。各单元报告已遵守。
- **厂商 TOPS / "AI-native" 营销降权**：prior deep-research 曾 0-3 否决 QNAP TS-AI642 具体 NPU 数、UGREEN "96 TOPS"、TerraMaster "全球首款 AI 原生 NAS"（见 [ai-newbrands.md](/Users/pengpeng/seo/directions/hardware/reports/_archived/ai-newbrands.md)）；GEEKOM "世界最强 AI mini PC"、各家统一喊 "126 TOPS" 均属话术，只作背景。
- **兼容性只以官方为准**：Olares 能否装、GPU 能否被加速，均以 docs.olares.com / GitHub `beclab/Olares` 为准，查不到标 `[unverified]`。**平台矩阵（2026-07-05 复核）**：Linux x86-64（裸机 ISO / script）、ARM Linux（树莓派 = 官方 ARM 路径，同一 script）、macOS Monterey 12+（含 Apple Silicon，script/Docker，有功能限制）、Windows 10/11（WSL2）——**"ARM not supported" 只限裸机 ISO 安装器**，不代表 Olares 只支持 x86。**GPU 加速：NVIDIA 最成熟（Turing/Ampere/Ada/Blackwell，≥8GB，自动检测+CUDA，全 app）；AMD（含 Ryzen AI Max APU / Radeon，经 ROCm）与 Intel 核显（检测 + Windows VM passthrough）均已支持；仅 Apple GPU(Metal) 不被 AI 应用加速。** 各 app 在非 NVIDIA 上的覆盖成熟度以官方/GitHub 复核。
- **价格标"价格带 + 截至日期"**：同型号跨渠道价差极大（GMKtec 128GB 见 $1,999/$2,999 两口径；DGX Spark FE 四个月内 $3,999→$4,699），SEO 内容勿写死。

## 六、有意排除项（不单列芯片单元，仅此备注）

- **Intel Core Ultra**：虽挂 "AI PC" 名号，但本地 AI 算力不足以做正经事，且架构代际分裂（Meteor/Lunar/Arrow/Panther Lake NPU 不一），不适合作"一芯→多型号"的稳定单元。其身影仍出现在 x86 承载机型里（多数 AI NAS、部分 mini PC 用 Core Ultra），随对应型号在 dgpu/ai-nas/其它 x86 机型报告里被覆盖；不单开芯片单元。
- **Qualcomm Snapdragon X（Copilot+ PC）**：排除理由是**本地 AI 算力弱（做不了正经本地 AI）+ Adreno GPU 不在被 Olares 加速之列**（与 Apple GPU 类似，非 NVIDIA/AMD/Intel），而**不是"不能装 Olares"**（Windows on Arm 走 WSL2、或 ARM Linux 走 script 均可能装上，仅体验受限，[unverified]）。信息 A/B 都吃不到多少，故不单列。若未来需要，只在此文补一段"诚实缺口"即可。

## 七、后续（把 research 变成内容/数据）

1. **补 Semrush 数字**：各 research 的型号级候选词量/KD 尚为结构化推断，逐词用 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research) 复核（**具体产品/型号作 brand**）。
2. **优先立产品级报告（backlog，⬜ 待做）**：**ROG NUC**（BOM 最接近，最高优先）；Razer Blade 16/18、Lenovo Legion 9i、Alienware Area-51（5090 Mobile）；Framework Desktop、GMKtec EVO-X2、HP ZBook Ultra/Z2 Mini G1a（Strix Halo）；ASUS GX10/Dell Pro Max/MSI EdgeXpert/Acer GN100（GB10）；Mac Studio M4 Max/M3 Ultra、Mac mini M4 Pro（Apple）；UGREEN iDX6011 Pro、Minisforum N5 Pro、极空间 Z425（AI NAS）。写前从 [reports/_archived/](/Users/pengpeng/seo/directions/hardware/reports/_archived) 取旧品牌报告洞见去重。
3. **N1X/RTX Spark 已从 devices 移除**：命名混淆（RTX Spark 现指 Windows-on-Arm 笔记本芯，非 GB10 盒子），暂不单开报告；相关背景保留在 [nvidia-gb10](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/nvidia-gb10.md) 第三节，待官方规格明确再评估。
4. **写对比长文**：**`olares one vs rog nuc`（同 BOM/异 OS，转化意图最强）**、`dgx spark vs mac studio vs Olares One`、`gaming laptop vs headless mini PC for 24/7 local AI`、`ai nas vs personal cloud`、**`zimacube creator vs olares one`、`nas with gpu vs olares one`（组六 AI NAS 含高端）**、`synology alternative` / `enterprise nas vs personal cloud` / `truenas vs synology`（组七企业，认知词）、`zimaos vs casaos` / `truenas vs olares`（组八 NAS OS）、"大显存卡吃灰→装 Olares OS" 教程，走 [seo-content](/Users/pengpeng/seo/.cursor/skills/seo-content)。
