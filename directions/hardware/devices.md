# hardware/devices.md — 加速硬件 / 整机 / NAS 竞品清单（具体产品为单元）

> 对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 4。本方向面向"正在买 / 已买别家硬件"的人群，只讲两条信息：**A 买 Olares One**（软硬一体、开箱即用的私有云整机），**B 在已购设备上装 Olares**（把已有算力变成随处可用的私有 AI 服务）。
>
> **结构：一行 = 一个具体产品**（不再用"厂商为单元"或合并写法）。芯片/品类的深度调研在 [research/](/Users/pengpeng/seo/directions/hardware/research)（穷举承载型号 SKU + 每型号候选 SEO 词 + 两条信息适配）。**报告策略已改为"基于产品"**：旧的品牌级 Semrush 报告移入 [reports/_archived/](/Users/pengpeng/seo/directions/hardware/reports/_archived)，产品行的"报告"列标 ⬜ 待做（写产品报告时可从 `_archived/` 取旧洞见）；已是产品/单品级的报告（GPU per-model、各 NAS、OS 竞品）仍直接链接。方向审计见 [research/gap-analysis.md](/Users/pengpeng/seo/directions/hardware/research/gap-analysis.md)。

**Olares One 规格（对标基准）**：$3,999｜RTX 5090 Mobile 24GB GDDR7｜Intel Core Ultra 9 275HX｜96GB DDR5（可扩 128GB）｜2TB NVMe（[one.olares.com](https://one.olares.com/)）。

**信息 B 平台矩阵（2026-07 复核 [docs.olares.com](https://docs.olares.com/)）**：Olares **跨平台**——Linux x86-64（裸机 ISO / script，Ubuntu 22.04-25.04·Debian 12-13）、**ARM Linux（树莓派即官方 ARM 路径，同一 script）**、**macOS Monterey 12+（含 Apple Silicon，script/Docker，有功能限制）**、**Windows 10/11（WSL2）**。"ARM is not currently supported" 只限裸机 ISO 安装器；**Olares One 只是官方选了 x86-64 + NVIDIA 做最佳开箱体验**。故信息 B 差异不在"能不能装"（几乎都能），而在**体验层级**。

**GPU 加速口径（2026-07 复核 docs.olares.com + GitHub beclab/Olares）**：**NVIDIA** 自动检测 + CUDA、Turing→Blackwell、≥8GB，覆盖全部 AI 应用（Ollama/ComfyUI/SD），**最成熟**；**AMD**（含 Ryzen AI Max APU / Radeon，经 ROCm）**已支持**；**Intel 核显**（检测 + Windows VM iGPU passthrough）**已支持**；**仅 Apple GPU(Metal) 不被 Olares AI 应用加速**（macOS 为 Docker 层）。引用前以官方/GitHub 为准。

---

## 组一：AI 加速芯片 / SoC 平台

以芯片为线，**每行一个具体产品**。深度调研（穷举 SKU + 每型号候选词）见各 `research/<slug>.md`。

### 1. AMD Ryzen AI Max（"Strix Halo"）→ [research/amd-ryzen-ai-max.md](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/amd-ryzen-ai-max.md)

128GB 统一内存 APU，全员 **x86-64 → 信息 B High 适配**（裸机 ISO/script 原生装；**APU 经 ROCm 被 Olares 加速**）。research 穷举约 26 个 OEM SKU，下面列可购/预售的代表机型（一行一产品）。

| 产品 | OEM | 形态 | 场景 | 产品报告 |
|------|-----|------|------|----------|
| EVO-X2 (AI) | GMKtec | mini PC | 旗舰 Strix Halo（`gmktec evo-x2` 4,400/mo）| ⬜ 待做 |
| Framework Desktop | Framework | 4.5L 桌面 | 开放/Linux 一等公民，叙事最契合 | ⬜ 待做 |
| GTR9 Pro | Beelink | mini PC | homelab / model-serving | ⬜ 待做 |
| MS-S1 Max | Minisforum | SFF AI PC | 大内存 + 扩展 | ⬜ 待做 |
| Z2 Mini G1a | HP | 迷你工作站 | 商用紧凑工作站 | ⬜ 待做 |
| ZBook Ultra G1a | HP | 移动工作站（笔记本）| 官方列 Ubuntu 24.04，承接 `strix halo laptop` KD9 | ⬜ 待做 |
| ROG Flow Z13 (2025) | ASUS | 二合一平板 | 唯一平板形态 | ⬜ 待做 |
| AI Workstation 300 | Corsair | SFF | 桌面 AI 工作站 | ⬜ 待做 |
| AI BOX-A395 | ASRock | mini PC | AI BOX 整机 | ⬜ 待做 |
| Magnus EAMAX | Zotac | mini PC | 迷你整机 | ⬜ 待做 |
| NEX395 | Aoostar | mini PC | 迷你整机 | ⬜ 待做 |

> 其余 SKU（Sapphire、NIMO、GEEKOM A9 Mega、PELADN YO1/BOSGAME M5、及中国厂商 LCFC/Linglong 等）见 research 第二节。最大 SEO 机会：`strix halo laptop`（590/mo，**KD9**）、`mini pc linux`（320/mo，**KD8**）。

### 2. NVIDIA GB10（Grace Blackwell）→ [research/nvidia-gb10.md](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/nvidia-gb10.md)

128GB 统一内存"个人 AI 超算" SoC，8 款同芯机型，US $2,999–$4,699。**arm64 / DGX OS（Ubuntu 24.04 arm64）→ 信息 B 有望 High**：arm64 走 Olares script 路径（同树莓派），GPU 是 Blackwell（架构受支持 GB✓）；仅 arm64 在 DGX OS 实测 + 整合 GPU 识别 [unverified]（内容用"有望/预计"表述）。信息 A 与 Olares One 同价位正面竞争。

| 产品 | OEM | 价格带(US) | 场景 | 产品报告 |
|------|-----|-----------|------|----------|
| DGX Spark Founders Edition | NVIDIA | $4,699 | 品牌词最大（`dgx spark alternative` **KD12**）| ✅ [nvidia-dgx](/Users/pengpeng/seo/directions/hardware/reports/01-ai-soc/gb10/nvidia-dgx.md) |
| Ascent GX10 | ASUS | ~$3,088–4,150 | 唯一前置电源键/铝壳 | ⬜ 待做 |
| Pro Max with GB10 | Dell | ~$3,699 | 企业保修线 | ⬜ 待做 |
| EdgeXpert MS-C931 | MSI | ~$2,999–3,999 | 最便宜入门 | ⬜ 待做 |
| Veriton GN100 | Acer | $2,999 | 散热最佳 | ⬜ 待做 |
| AI TOP ATOM | Gigabyte | 随地区 | 固件更新较慢 | ⬜ 待做 |
| ZGX Nano AI Station G1n | HP | ~$3,000–4,000 | 商用线 | ⬜ 待做 |
| ThinkStation PGX | Lenovo | 随地区 | 商用线 | ⬜ 待做 |

### 3. Apple Silicon M 系（Mac Studio / Mac mini）→ [research/apple-m-series.md](/Users/pengpeng/seo/directions/hardware/research/01-ai-soc/apple-m-series.md)

统一内存 = 消费端本地 LLM 王（M3 Ultra 512GB 单机跑 671B）。**macOS 路径 → 信息 B 可装、有限制**（无分布式存储/本地节点；Apple GPU 不被 Olares AI 应用加速；也可只用 LarePass 客户端）。信息 A 为主。

**M5 世代状态（AS_OF 2026-07，以 apple.com 为准）**：M5 已在 **MacBook Pro** 落地——MacBook Pro 14″ **M5**（2025-10）、14/16″ **M5 Pro / M5 Max**（2026-03）；但**桌面机尚未上 M5**：Mac Studio 仍 M3 Ultra / M4 Max，Mac mini 仍 M4 / M4 Pro，**Mac mini M5 截至 2026-07 未官宣**（业界预计 2026 秋，[unverified]）。本组仍以桌面（Studio/mini）为本地 LLM 单元，M5 Mac mini/Studio 出货后补行。

| 产品（在售） | 芯片 | 场景 | 产品报告 |
|--------------|------|------|----------|
| Mac Studio M3 Ultra | M3 Ultra（最高 512GB）| 大模型旗舰，`mac studio vs dgx spark` | ✅ [apple-silicon](/Users/pengpeng/seo/directions/hardware/reports/01-ai-soc/apple-silicon/apple-silicon.md) |
| Mac Studio M4 Max | M4 Max（最高 128GB）| 价格甜点 | ✅ [apple-silicon](/Users/pengpeng/seo/directions/hardware/reports/01-ai-soc/apple-silicon/apple-silicon.md) |
| Mac mini M4 Pro | M4 Pro（最高 64GB，273 GB/s）| 本地 LLM 甜品 | ✅ [apple-silicon](/Users/pengpeng/seo/directions/hardware/reports/01-ai-soc/apple-silicon/apple-silicon.md) |
| Mac mini M4 | M4（最高 32GB，120 GB/s）| 性价比入门 | ✅ [apple-silicon](/Users/pengpeng/seo/directions/hardware/reports/01-ai-soc/apple-silicon/apple-silicon.md) |
| Mac mini M5 | M5（[unverified]，预计 2026 秋）| 出货后补 | ⬜ 待做 |

---

## 组二：NVIDIA RTX 5090 Mobile 游戏本 → [research/rtx-5090-mobile-laptops.md](/Users/pengpeng/seo/directions/hardware/research/02-5090-laptops/rtx-5090-mobile-laptops.md)

与 GB10、Apple 并列的一类"承载 Olares One 同款 GPU"的整机。**RTX 5090 Mobile = 24GB GDDR7**，与 Olares One 完全同款；多数还搭 **Core Ultra 9 275HX**（与 Olares One 同 CPU）。差别在形态：游戏本带屏、非 7×24 无头服务器、散热/续航取向不同。**信息 A 强对标**（同 GPU/CPU，讲"为什么无头私有云盒子比游戏本更适合常驻 AI"）；信息 B 也成立（Windows→WSL2 或双系统 Linux，NVIDIA GPU 被完整加速）。价格 $3,999–$6,999。

| 产品 | OEM | CPU（常见）| 最高内存 | 价格带(US) | 产品报告 |
|------|-----|-----------|----------|-----------|----------|
| ROG Strix SCAR 16 | ASUS | Core Ultra 9 275HX | 64GB | ~$4,299–5,630 | ⬜ 待做 |
| ROG Strix SCAR 18 | ASUS | Core Ultra 9 275HX | 64GB | ~$4,300+ | ⬜ 待做 |
| ROG Zephyrus G16 | ASUS | Core Ultra 9 285H | 64GB | 较薄轻旗舰 | ⬜ 待做 |
| Razer Blade 16 (2026) | Razer | Core Ultra 9 / Ryzen AI 9 | 64GB | ~$4,900 | ⬜ 待做 |
| Razer Blade 18 (2026) | Razer | Core Ultra 9 290HX Plus | 128GB DDR5-6400 | 最高 ~$6,999 | ⬜ 待做 |
| Legion Pro 7i Gen10 | Lenovo | Core Ultra 9 275HX | 64GB | ~$3,999 起 | ⬜ 待做 |
| Legion 9i 18 (2026) | Lenovo | Core Ultra 9 290HX Plus | 最高 192GB | ~$4,000–5,200 | ⬜ 待做 |
| Titan 18 HX AI | MSI | Core Ultra 9 275HX | 96–128GB | ~$5,000+（4TB 起）| ⬜ 待做 |
| Raider 18 HX AI | MSI | Core Ultra 9 275HX | 64GB | 高端 | ⬜ 待做 |
| Stealth 18 HX AI | MSI | Core Ultra 9 275HX | 64GB | ~$4,399 | ⬜ 待做 |
| Omen Max 16 | HP | Core Ultra 9 275HX | 64GB | 相对亲民 | ⬜ 待做 |
| Area-51 (18) | Alienware/Dell | Core Ultra 9 290HX Plus | 64GB | ~$3,600 起 | ⬜ 待做 |
| Aorus Master 16/18 | Gigabyte | Core Ultra 9 275HX | 64GB | 高端 | ⬜ 待做 |

> 全系 5090 Mobile = 24GB GDDR7、175W TGP 档。角度：`rtx 5090 laptop llm`、`<model> vs olares one`、"游戏本 vs 无头私有 AI 盒子"。

---

## 组三：ASUS ROG NUC（最接近 Olares One 的 BOM）→ [research/rog-nuc.md](/Users/pengpeng/seo/directions/hardware/research/03-rog-nuc/rog-nuc.md)

ROG NUC 是把"5090/5080 Mobile + Core Ultra HX + 大内存"塞进 <3L 迷你盒子的产品，**BOM 与 Olares One 最接近**——同为"移动 GPU + HX CPU + 小体积整机"，是 `olares one vs rog nuc` 型对比文的核心素材。差异点：ROG NUC 跑 Windows/游戏取向、无 Olares 的私有云 OS 层（多应用 + 远程访问 + 备份 + 开源）。

| 产品 | CPU | GPU | 最高内存 | 体积/价格 | 与 Olares One 对位 | 产品报告 |
|------|-----|-----|----------|-----------|-------------------|----------|
| ROG NUC (2025) NUC15JNK | Core Ultra 9 275HX | 最高 RTX 5080 Laptop | 96GB DDR5-6400 | <3L / ~$3,199 | **CPU、内存完全同款**（GPU 差一档）| ⬜ 待做 |
| ROG NUC 16 (2026) | Core Ultra 9 290HX Plus | 最高 RTX 5090 Laptop 24GB | 待核 | >$4,000 | **GPU 完全同款**（CPU 更新一代）| ⬜ 待做 |

> 两代合起来正好从两个维度贴住 Olares One（2025 版对 CPU/内存，2026 版对 GPU）。核 ROG NUC 顶配 GPU/内存以官网为准 [unverified]。

---

## 组四：≥24GB 显存 dGPU（型号为单元）→ [research/dgpu-24gb-plus.md](/Users/pengpeng/seo/directions/hardware/research/04-dgpu/dgpu-24gb-plus.md)

以显存线组织：**24GB 是本地 AI 入场券，48GB 才舒适跑 70B，96GB 富余 120B+**（70B Q4_K_M 约需 40-43GB）。大卡天然在 x86 台式机 → **信息 B High**，主打"大卡吃灰→装 Olares 变 7×24 私有 AI 服务器"。GPU 加速：**NVIDIA 最成熟/全 app；AMD 经 ROCm、Intel 经其驱动亦被支持**（成熟度随版本，ComfyUI/SD 等需 CUDA 的应用在非 NVIDIA 上覆盖较窄）。

| GPU | 显存 | tier | 切入词 | 产品报告 |
|-----|------|------|--------|----------|
| RTX 3090 / 3090 Ti | 24GB | 消费/二手 | 二手 24GB 性价比 / dual 3090 | ✅ [rtx-3090](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-3090.md) |
| RTX 4090 | 24GB | 消费/停产 | rtx 4090 local llm | ✅ [rtx-4090](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-4090.md) |
| RTX 5090 | 32GB | 消费 | rtx 5090 llm / 5090 vs 4090 | ✅ [rtx-50-series](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-50-series.md) |
| RTX A6000 / 6000 Ada / PRO 6000 Blackwell | 48 / 48 / 96GB | 工作站 | cheapest 48gb gpu for llm / vs dgx spark | ✅ [rtx-pro-6000](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-pro-6000.md) |
| Radeon RX 7900 XTX / AI PRO R9700 / PRO W7900 | 24 / 32 / 48GB | 消费+工作站 | amd gpu llm / rocm ollama | ✅ [radeon-high-end](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/amd/radeon-high-end.md) |
| Intel Arc Pro B60 / B60 Dual | 24 / 48GB(2×24) | AI/工作站 | intel arc llm / 最便宜大显存 | ✅ [intel-arc](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/intel/intel-arc.md) |

> **显式降权（<24GB，不入本地 AI 可用层）**：RTX 5080/5070 系（8-16GB）、RX 9070 XT/7800 XT（16GB）、Arc B580/B570（10-12GB）——16GB 上限约 30B Q4，仅作"为什么 16GB 不够"导流内容。

---

## 组五：工作站（跨厂具体型号，装 Olares 即团队级私有 AI 服务器）

不按厂商分类，统一"工作站"一组，**单元是具体型号**。这些是配大显存专业卡（映射组四）或 Strix Halo（映射组一）的整机；对 Olares 的意义是"已有一台强算力工作站 → 装 Olares 变随处可访问的团队级私有 AI 服务器"。SKU 以官网在售为准 [部分待核]。

| 型号 | OEM | 说明 | 产品报告 |
|------|-----|------|----------|
| Thelio Mira Premium / Elite | System76 | Linux 工作站（Ryzen 9 9950X + RTX 5070/5070 Ti），Pop!_OS 原生 | ⬜ 待做 |
| Thelio Prime | System76 | SFF Linux 工作站（可选 RTX 50 系）| ⬜ 待做 |
| Z2 Mini G1a | HP | Strix Halo 迷你工作站（亦见组一）| ⬜ 待做 |
| Z4 / Z6 / Z8 Fury G5（塔式）| HP | 专业塔式工作站（大显存专业卡）| ⬜ 待做 |
| ThinkStation P3 / P5 / P7 / PX | Lenovo | 专业塔式/机架工作站 | ⬜ 待做 |
| Precision 3000 / 5000 / 7000（塔式/移动）| Dell | 专业工作站线 | ⬜ 待做 |
| ProArt Station | ASUS | 创作者工作站 | ⬜ 待做 |

> 游戏本/掌机（Ally X / Legion Go / MSI Claw 等）不是目标场景，不列入。

---

## 组六：AI NAS（含高端发烧，一行一型号）→ [research/ai-nas.md](/Users/pengpeng/seo/directions/hardware/research/06-ai-nas/ai-nas.md)

"AI NAS" 已成真实在售品类（存储 + 本地 AI）。**只看硬件事实**：内置 GPU（iGPU/NPU）、能否内插独显（NAS 内 PCIe 多 ≤75W 无辅助供电）、eGPU 接口（OCuLink/TB）、售价、购买入口。对标 Olares One（$3,999 / RTX 5090 Mobile **24GB GDDR7** / 96GB DDR5）：AI NAS 多为存储盒子 + 弱 iGPU/NPU 或需外接 GPU；Olares One = 一体机 + 24GB 独显 + 开源全栈个人云 OS（信息 A 差异点）。

| 型号 | 厂商 | 内置 GPU | 可内插独显（PCIe）| eGPU 接口 | 价格 | 购买 | 报告 |
|------|------|----------|-------------------|-----------|------|------|------|
| NASync iDX6011 Pro | UGREEN | Core Ultra 7 255H（Arc+NPU）| 无内插 dGPU 槽 | OCuLink | $1,559–2,599 | [nas.ugreen.com](https://nas.ugreen.com/) | ✅ [ugreen-nas](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/ugreen-nas.md) |
| NASync DXP4800 Plus | UGREEN | Pentium Gold 8505（UHD）| 无 | 无 | ~$599–700 | [DXP4800 Plus](https://nas.ugreen.com/products/ugreen-nasync-dxp4800-plus-nas-storage) | ✅ [ugreen-nas](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/ugreen-nas.md) |
| Z425 | 极空间 | Core Ultra 5 225H（Arc+NPU）| [unverified] | — | ¥7,999 | [m.zspace.cn/z425](https://m.zspace.cn/z425/) | ✅ [zspace](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/zspace.md) |
| Z423 / Q2C | 极空间 | [unverified] iGPU | [unverified] | — | 中端 | [zspace.cn](https://www.zspace.cn/) | ✅ [zspace](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/zspace.md) |
| N5 Pro | Minisforum | Ryzen AI 9 HX PRO 370（Radeon 890M+NPU）| 内 PCIe x16(电 x8) LP ≤75W | **OCuLink**（实测 4090）| $1,019 起 | [N5 Pro](https://store.minisforum.com/products/minisforum-n5-pro-ai-nas) | ⬜ 待做 |
| N5 / N5 Air | Minisforum | Ryzen 7 255（Radeon）| 内 PCIe x16 | OCuLink | ~$519 起 | [store.minisforum.com](https://store.minisforum.com/) | ⬜ 待做 |
| WTR Max | Aoostar | 8845HS（Radeon 780M）/ i5-1235U | 无内槽 | **OCuLink PCIe4 x4** | 裸机 $559/$659 | [WTR Max](https://aoostar.com/products/aoostar-wtr-max-amd-r7-pro-8845hs-11-bays-mini-pc) | ⬜ 待做 |
| ZimaCube 2 / 2 Pro | IceWhale | i3-1215U / i5-1235U | 内插 LP GPU ≤75W | TB4 eGPU | $799 / $1,299 | [shop.zimaspace.com](https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas) | ✅ [zimaos-zimacube](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/zimaos-zimacube.md) |
| ZimaCube 2 Creator Pack | IceWhale | i5-1235U + **预装 RTX Pro 2000 16GB** | 已装 LP 独显 ≤75W | TB4 eGPU | $2,499 | [shop.zimaspace.com](https://shop.zimaspace.com/products/zimacube-2-personal-cloud-nas) | ✅ [zimaos-zimacube](/Users/pengpeng/seo/directions/hardware/reports/06-ai-nas/ai-nas/zimaos-zimacube.md) |
| MS-A2 | Minisforum | Ryzen 9 9955HX（Radeon）| 内 PCIe4 x16(电 x8) LP | — | $639–839 | [store.minisforum.com](https://store.minisforum.com/) | ⬜ 待做 |
| MS-01 | Minisforum | i9-13900H（Iris Xe）| 内 PCIe x16(电 x8) 半高单槽 | — | ~$500–750 | [store.minisforum.com](https://store.minisforum.com/) | ⬜ 待做 |
| LincStation N2 | LincPlus | Intel N100（UHD）| 无 | 无 | $409–449 | [LincStation N2](https://www.lincplustech.com/products/lincstation-n2-network-attached-storage.html) | ⬜ 待做 |
| 小米智能存储 | 小米 | [unverified] | [unverified] | — | ¥2,299 起 | [mi.com](https://www.mi.com/) | ⬜ 待做 |
| TS-AI642（对比，亦见组六）| QNAP | RK3588 ARM（Mali+NPU）| 无 | 无 | $749 | [qnap.com](https://www.qnap.com/en/product/ts-ai642) | ⬜ 待做 |
| DS925+（对比）| Synology | AMD Ryzen（无 iGPU）| 无 | 无 | ~$640–1,029 | [synology.com](https://www.synology.com/en-global/products/DS925+) | ⬜ 待做 |

> **DIY 路线（非成品，自组）**：Jonsbo N6 一体（全长独显 RTX 3090/5060Ti，9×3.5"，机箱 [$150–200](https://www.jonsbo.com/en/products/N6Black.html)）、4U 机架多卡（4×RTX 4090 / RTX Pro 6000）——"自建 AI 服务器"选题用，非一键购买型号。物理提醒：NAS 内 PCIe 多 ≤75W 无辅助供电，重卡走 OCuLink/eGPU 或 DIY 机箱。

---

## 组七：企业 / 机架 / 商用 NAS → [research/enterprise-nas.md](/Users/pengpeng/seo/directions/hardware/research/07-enterprise-nas/enterprise-nas.md)

**与 Olares One 不是同一买家段**（PB 级容量 / 双控 HA / 25-100GbE / 报价制，面向 IT 采购）——只在 `synology alternative` 类**认知词**与 homelab 子群里有位置；其"AI"多为识别 + 云 API + 语义搜索，**非本地大模型**。GPU：企业机架/塔式机型多**无内置独显但有全高 PCIe 槽可加卡**（不同于 mini NAS 的 ≤75W 限制），仅 Synology DVA 系内置 GTX 1650。

| 产品 | 厂商 | 形态 / 盘位 | GPU / 可插卡 | 价格 | 购买 | 报告 |
|------|------|-------------|--------------|------|------|------|
| SA6400 | Synology | 2U / 12（扩 108）| 无内置；PCIe 可扩 | 报价制 | [SA6400](https://www.synology.com/en-us/products/SA6400) | ⬜ 待做 |
| HD6500 | Synology | 4U / 60（扩 300）| 无内置；PCIe 可扩 | 报价制 | [HD6500](https://www.synology.com/en-us/products/HD6500) | ⬜ 待做 |
| RS6426xs+ | Synology | 3U / 16（扩 64）| **PCIe Gen4×2 可接 GPU** | 报价制 | [RS6426xs+](https://www.synology.com/en-us/products/RS6426xs+) | ⬜ 待做 |
| DVA3221 | Synology | 4 盘 NVR | **内置 GTX 1650** | ~ | [DVA 系](https://www.synology.com/en-global/products/DVA) | ⬜ 待做 |
| TDS-h2489FU R2 | QNAP | 2U / 24 U.2 全闪 | 无内置；PCIe 可扩 | $10,999–29,999 | [TDS-h2489FU R2](https://www.qnap.com/en/product/tds-h2489fu%20r2) | ⬜ 待做 |
| TVS-AIh1688ATX | QNAP | 塔式 12+4，Core Ultra | iGPU+NPU；PCIe 可扩（TB5）| ~$5,199 | [发布稿](https://www.qnap.com/en/news/2025/qnap-launches-tvs-aih1688atx-ai-nas-with-36-tops-for-ai-and-virtualization) | ⬜ 待做 |
| TS-AI642 | QNAP | 6 盘塔式，RK3588 ARM | SoC Mali+NPU；无 PCIe | $749 | [TS-AI642](https://www.qnap.com/en/product/ts-ai642) | ⬜ 待做 |
| TrueNAS R60 | iXsystems | 1U 全闪 PCIe Gen5 | PCIe 可加 GPU | 报价制 | [R-Series](https://www.truenas.com/r-series/) | ⬜ 待做 |
| TrueNAS Mini R | iXsystems | 2U / 12 入门机架 | PCIe 可扩 | 定价见官网 | [TrueNAS Mini](https://www.truenas.com/truenas-mini/) | ⬜ 待做 |
| Storinator XL60 | 45Drives | 4U / 60 开放硬件（~1.92PB）| **全高 PCIe 可加多卡** | 报价制 | [Storinator XL60](https://www.45drives.com/products/storage-server-storinator-xl60/) | ⬜ 待做 |
| HL15 | 45HomeLab | 15 盘 open-platform（ATX）| **可插全长独显** | 机箱 $799.99 起 | [45homelab.com](https://45homelab.com/) | ⬜ 待做 |

---

## 组八：个人云 / NAS OS 竞品（OS 层，软硬一体或纯 OS）

对标的不是硬件而是"个人云 / 家庭服务器 OS"这一软件位。

| 名称 | Olares 对标角度 | 官网 | 报告 |
|------|----------------|------|------|
| TrueNAS | 开源 NAS OS，私有云 OS 对比 | [truenas.com](https://www.truenas.com/) | ✅ [truenas](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os/truenas.md) |
| Unraid | NAS / 家庭服务器 OS | [unraid.net](https://unraid.net/) | ✅ [unraid](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os/unraid.md) |
| CasaOS | 轻量家庭云 OS（`zimaos vs casaos` KD7）| [casaos.io](https://casaos.io/) | ✅ [casaos](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os/casaos.md) |
| Umbrel | 家庭服务器 OS + umbrel-home 硬件 | [umbrel.com](https://umbrel.com/) | ✅ [umbrel](/Users/pengpeng/seo/directions/hardware/reports/08-nas-os/umbrel.md) |
| 飞牛 fnOS | 国产个人云 NAS OS（Debian 系，闭源、个人免费/商用授权）；对标个人云 OS，Olares 开源全栈是差异点 | [fnnas.com](https://www.fnnas.com/) | ⬜ 待做 |

---

> **怎么用**：找型号级切入词看 `research/<slug>.md`；写产品级报告走 `.cursor/skills/brand-seo-research/`（具体产品/型号作 brand，写前可从 [reports/_archived/](/Users/pengpeng/seo/directions/hardware/reports/_archived) 取旧品牌报告的洞见去重）；把 research 落成对比/教程文走 `.cursor/skills/seo-content/`。
> **产品报告 backlog**：⬜ 标记的行 = 待写的产品级 SEO 报告（优先级见 [research/gap-analysis.md](/Users/pengpeng/seo/directions/hardware/research/gap-analysis.md) 后续章）。
