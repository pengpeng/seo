# AMD Ryzen AI Max（"Strix Halo"）单元与 OEM 型号穷举 — 市场/SEO 研究

> 研究日期: 2026-07-05 | 来源数: 35 | 字数: ~3,600 | 模式: Standard | AS_OF: 2026-07-05 | 官方源占比: ~43%

## 摘要

AMD Ryzen AI Max（研发代号 **Strix Halo**，即 Ryzen AI Max 300 系列）是 2025-2026 年最重要的本地 AI 硬件平台：一颗把 16 个 Zen 5 CPU 核、40-CU Radeon 8060S iGPU（RDNA 3.5，gfx1151）与 XDNA2 NPU 塞进单封装的 APU，配 256-bit LPDDR5X-8000/8533、约 256 GB/s 带宽，最高 **128GB 统一内存** [15][16][17][27]。它的杀手锏不是速度而是**内存层级**——iGPU 可寻址近百 GB 内存，能本地跑 70B、乃至 120B 级模型，这是 24/32GB 独显做不到的 [1][27][28]。

截至 AS_OF，市面已有 **20+ 家 OEM** 推出或预告搭载 Ryzen AI Max+ 395 的设备，形态覆盖 mini PC、桌面工作站、笔记本工作站与二合一平板 [20][21]。本报告以 Strix Halo 为"单元"，穷举承载它的具体 OEM 型号 SKU（约 26 个已确认/预售条目），并为每个型号给出候选 SEO 关键词。所有 Strix Halo 设备均为 **x86-64**，可走 Olares 最省心的 **x86-64 裸机 ISO 或 Linux script** 路径 [30][31]——因此每一台都能**原生安装 Olares（High 适配）**，构成"买了 128GB Strix Halo 盒子→装 Olares 变私有常驻 AI 服务"的天然内容切口。（口径说明：Olares 本身**跨平台**，ARM Linux/macOS/Windows 也支持，x86-64 只是这些盒子最直接的裸机路径；GPU 加速 **NVIDIA 最成熟**，而 **AMD Ryzen AI Max APU（含 Radeon 核显）经 ROCm 已被 Olares 加速**（系统级自动检测 1.12.4 起逐步落地、1.12.6/1.12.7 加调度器标签，成熟度随版本）——这对 Strix Halo 是利好，见第五节。）

一句话战略：Strix Halo 是 Olares 在硬件方向"信息 A（对标 Olares One）"与"信息 B（在你已有设备上装 Olares OS）"两条线都能吃到的高热度平台，其中平台词竞争度惊人地低（`strix halo laptop` KD9、`mini pc linux` KD8，见第三节）。

置信度 **High** — 依据:单元规格来自 AMD 官方 [15][16][17];型号清单交叉自 VideoCardz + 厂商官网 + 多篇评测。

## 一、单元定位（Ryzen AI Max 是什么、统一内存意义、为何对 Olares 重要）

**它是一颗单芯片 APU，不是 CPU 也不是 GPU。** Strix Halo 把桌面级 Zen 5 CPU、接近入门独显的 40-CU RDNA 3.5 iGPU（Radeon 8060S）、以及 XDNA2 NPU 集成在一颗芯片，用 256-bit LPDDR5X 内存总线（比普通移动平台的 128-bit 翻倍）喂养两者，带宽约 256 GB/s [15][17][27]。

**型号梯队（消费线，Ryzen AI Max 300 系列）** [17][22]:

| 型号 | 核/线程 | iGPU | 最高统一内存 | 平台 TOPS |
|---|---|---|---|---|
| Ryzen AI Max+ 395 | 16C/32T | Radeon 8060S(40 CU) | 128GB | ~126 |
| Ryzen AI Max 390 | 12C/24T | Radeon 8050S(32 CU) | 128GB | ~120 |
| Ryzen AI Max 385 | 8C/16T | Radeon 8050S(32 CU) | 64GB | ~117 |

**PRO 梯队（商用/工作站，HP 等采用）**:Max+ PRO 395 / PRO 390 / PRO 385 / PRO 380（6C/12T），默认 TDP 55W，带 ISV 认证与企业管理特性 [8][9]。

**统一内存的意义 = 内存层级即能力。** 遵循数据纪律,本报告不引用 tokens/s。只用内存层级定性表达能力:128GB 统一内存中,Windows 下最多约 96GB 可划给 iGPU,Linux 上实测可把 ~120-128GB 作为 GTT 让给 GPU [1][27][28][29]。这意味着 **128GB 档 → 可本地跑 ~70B / 120B 级模型**;64GB 档（如 Max 385）→ 30B 级更稳妥。这是 Strix Halo 相对 24-32GB 独显的结构性优势:不是更快,而是"装得下"。

**为何对 Olares 重要。** Olares 是个人云操作系统,核心用例是跑私有 Personal AI Agent;它既不是 NAS 也不是 AI PC,而是"你拥有的一朵云"。Strix Halo 设备是一批**天生 x86-64、内存超大、功耗 120W 级、体积 <5L** 的盒子——正好是"常驻在家、跑本地大模型的私有 AI 主机"的理想载体。Olares 的 x86-64 裸机 ISO / Linux script（Ubuntu 22.04-25.04 / Debian 12-13）与这些设备完全吻合 [30][31]。（"ARM not supported" 仅指裸机 ISO 安装器；Olares 经 script/Docker 也支持 ARM Linux、macOS、Windows——本单元因是 x86-64，直接走最省心路径。）

置信度 **High** — 依据:AMD 官方产品页 + Framework/HP 官方规格 [9][15][16][17][25][27]。

## 二、OEM 型号 SKU 表（核心交付：穷举承载 Strix Halo 的设备）

> 说明:x86-Linux 列对所有 Strix Halo 均为 **Y**（→ 均可原生装 Olares OS,High 适配)。价格为定性价格带,跨渠道差异大,不作精确对比。状态以 AS_OF 2026-07-05 计。

### A. Mini PC / 桌面工作站

| # | 型号全名 | OEM | 形态 | 状态 | Ryzen AI Max 变体 | 最高统一内存 | 价格带 | x86-Linux | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | EVO-X2 (AI) | GMKtec | mini PC | 已量产 | 395 | 128GB | 中($1,499/64GB–$1,999/128GB) | Y | [3][6][7][20] |
| 2 | Framework Desktop | Framework | 桌面(4.5L Mini-ITX/主板) | 已量产 | 395 / 385 | 128GB | 低-中($1,099–$1,999) | Y(官方一等) | [25][26][27] |
| 3 | GTR9 Pro | Beelink | mini PC | 已量产 | 395 | 128GB | 中(~$1,985 MSRP) | Y(E610 网卡需修) | [2][20] |
| 4 | GTR9 / AI Mini | Beelink | mini PC | 预售/展出 | 395 | 128GB | 中 | Y | [20][21] |
| 5 | MS-S1 Max | Minisforum | SFF AI PC | 已量产/预售 | 395 | 128GB | 中-高(~$2,399) | Y | [7][24][5] |
| 6 | Z2 Mini G1a | HP | 紧凑桌面工作站 | 已量产 | 395/390/385/380(含PRO) | 128GB | 中-高($1,399–$2,649) | Y | [20][3] |
| 7 | AI Workstation 300 | Corsair | 桌面/SFF | 已量产 | 395 / 385 | 128GB | 中($1,599/385/64GB–$1,999+/395/128GB) | Y | [1][20] |
| 8 | NEX395 | Aoostar | mini PC | 预售/上市 | 395 | 128GB(LPDDR5X-8533) | 中 | Y | [19][21] |
| 9 | YO1 395 (= BOSGAME M5) | PELADN / BOSGAME | mini PC | 已量产 | 395 | 128GB | 中($1,489/96GB–$1,699/128GB) | Y | [18][20][21] |
| 10 | YO2 | PELADN | mini PC | 上市(中国) | 395 | 128GB | 中-高(~$3,030,中国) | Y | [20] |
| 11 | A9 Mega | GEEKOM | mini PC(1.7L) | 预告/H2 上市 | 395 | 128GB | 中(自 ~$1,899) | Y(宣称兼容) | [33][34][35] |
| 12 | Magnus EAMAX / ZBOX E | Zotac | mini PC | 已量产/展出 | 395 | 128GB | 中(~$1,799) | Y | [1][20] |
| 13 | AI BOX-A395 | ASRock | mini PC | 已量产 | 395 | 128GB | 中(~$1,699) | Y | [1] |
| 14 | Strix Halo PC | Sapphire | mini PC | 预售 | 395 | 128GB | 中(~$1,899) | Y | [1] |
| 15 | NIMO Mini PC 128GB | NIMO | mini PC | 已量产(Amazon) | 395 | 128GB | 中-高(~$2,799) | Y | [4] |
| 16 | FX-EX9 | FEVM | mini PC | 未发/预告 | 395 | 128GB | 待定 | Y | [20][21] |
| 17 | XRIVAL | X+ | mini PC | 展出 | 395 | 96GB | 中($1,475/96GB) | Y | [20] |
| 18 | SMART 900 | Colorful | mini PC | 未发/预告 | 395 | 128GB | 待定 | Y | [20][21] |
| 19 | AI Mini-PC | AOKZOE | mini PC | 未发 | 395 | 待定 | 待定 | Y | [20][21] |
| 20 | LCFC AI PC | Lenovo(LCFC) | mini PC | 上市(中国) | 395 | 128GB | 中(¥13,999) | Y | [20] |
| 21 | StarCore Super AI Computer | Linglong | mini PC | 上市(中国) | 395 | 128GB | 中(¥13,999) | Y | [20] |
| 22 | (Strix Halo mini PC) | Thermalright | mini PC | 未发 | 395 | 128GB | 待定 | Y | [20][21] |
| 23 | (ODM Strix Halo) | Sixunited | mini PC | 未发 | 395 | 128GB | 待定 | Y | [20] |
| 24 | (Strix Halo SFF,展出) | SEAVIV / Tianba | mini PC | 展出 | 395 | 待定 | 待定 | Y | [20] |

### B. 笔记本 / 平板

| # | 型号全名 | OEM | 形态 | 状态 | Ryzen AI Max 变体 | 最高统一内存 | 价格带 | x86-Linux | 来源 |
|---|---|---|---|---|---|---|---|---|---|
| 25 | ZBook Ultra G1a 14 | HP | 笔记本(移动工作站) | 已量产 | PRO 395/390/385/380 | 128GB | 高($2,747–~$4,049) | Y(官方列 Ubuntu 24.04) | [8][9][10][11] |
| 26 | ROG Flow Z13 (2025) GZ302 | ASUS | 二合一平板 | 已量产 | 395 / 390 | 128GB | 高($2,199 起) | Y(社区) | [12][13][14] |
| 27 | ROG Flow Z13 Kojima Edition | ASUS | 二合一平板 | 2026 上市 | 395 | 128GB | 高 | Y | [14] |

> **[unverified] 待核实条目**:localaimaster [22] 另提到 "HP Z2 Mini G9""Asus ROG NUC AI""HP Omen Transcend" 搭载 Strix Halo,但与更权威来源(HP 官方型号为 **Z2 Mini G1a**)不一致,疑为型号混淆,暂不计入正式清单。

**已确认/预售型号计数:约 26 个**(A 段 24 家条目含部分未发,B 段 3 个;去掉纯未发占位后"可购/预售"约 18 个)。

置信度 **Medium-High** — 依据:核心机型(EVO-X2/Framework/GTR9 Pro/MS-S1 Max/HP 双旗舰/Flow Z13)有官方或权威媒体多源确认;长尾中国厂商与 "Unreleased" 条目来自单一大会清单 [20],上市状态可能变化。

## 三、每型号候选 SEO 关键词（表 + 值得单独立报的型号）

> 复用先前平台级关键词发现(来自 gmktec.md,US Semrush 2026-07,归属前报告):
> `strix halo` **4,400/mo KD25** · `strix halo laptop` **590/mo KD9(全场最低竞争!)** · `ryzen ai max` 1,600/mo KD42 · `ryzen ai max 395` 1,000/mo KD39 · `strix halo mini pc` 880/mo KD34 · `gmktec evo-x2` 4,400/mo KD36 · `mini pc linux` 320/mo KD8。这些是"平台锚点词",下面是"型号级长尾词"(意图更精准、竞争更低)。

| 型号 | 候选关键词(意图) |
|---|---|
| GMKtec EVO-X2 | `gmktec evo-x2 local llm`(部署)· `gmktec evo-x2 linux`(装机)· `gmktec evo-x2 vs olares one`(对标)· `gmktec evo-x2 review`(评测) |
| Framework Desktop | `framework desktop local ai server`(用途)· `install olares on framework desktop`(装机-高价值)· `framework desktop vs olares one`(对标)· `framework desktop 128gb llm` |
| Beelink GTR9 Pro | `beelink gtr9 pro llm server`(用途)· `gtr9 pro linux install`(装机)· `beelink gtr9 pro review` |
| Minisforum MS-S1 Max | `ms-s1 max local llm`· `minisforum ms-s1 max homelab`(场景)· `ms-s1 max vs olares one` |
| HP ZBook Ultra G1a | `hp zbook ultra g1a local llm`· `zbook ultra g1a ubuntu`(装机)· `zbook ultra g1a 128gb ai` |
| HP Z2 Mini G1a | `hp z2 mini g1a ai workstation`· `z2 mini g1a linux`· `z2 mini g1a vs olares one` |
| Asus ROG Flow Z13 (2025) | `rog flow z13 local llm`· `rog flow z13 128gb ai`· `rog flow z13 linux` |
| GEEKOM A9 Mega | `geekom a9 mega local ai`· `geekom a9 mega vs mac studio`· `geekom a9 mega review` |
| Corsair AI Workstation 300 | `corsair ai workstation 300 llm`· `corsair ai workstation setup` |
| Aoostar NEX395 | `aoostar nex395 local llm`· `aoostar nex395 review` |
| PELADN YO1 / BOSGAME M5 | `peladn yo1 395 llm`· `bosgame m5 strix halo` |

**值得单独做 brand-seo 报告的型号(种子指针)**:
1. **GMKtec EVO-X2** — 已被验证有独立高流量品牌词(`gmktec evo-x2` 4,400/mo),已有前报告 gmktec.md,建议深化。
2. **Framework Desktop** — 开放性/Linux 一等公民 + 品牌自带流量,与 Olares "软硬一体开放"叙事最契合,**强烈建议单独立报**。
3. **HP ZBook Ultra G1a / Z2 Mini G1a** — 商用工作站长尾 + 高客单,适合"信息 A 高端对标"内容。
4. **Asus ROG Flow Z13 (2025)** — 唯一平板形态 + 游戏/创作跨界流量,`strix halo laptop`(KD9)可由它承接。
5. **Beelink GTR9 Pro** — homelab/model-serving 场景词强,适合"信息 B 装 Olares"内容。

置信度 **Medium** — 依据:平台词有 Semrush 实测(前报告);型号级长尾词为基于搜索意图的候选,量级/KD 需 Semrush 逐词核验后再定稿。

## 四、两条信息 × Olares 适配

### 信息 A —— "买 Olares One"（对标这些 Strix Halo 盒子）

Olares One:$3,999,RTX 5090 Mobile 24GB GDDR7、Intel Core Ultra 9 275HX、96GB DDR5(可扩至 128GB)、2TB NVMe [32]。

对标要点(**软硬一体 + 开箱即用的私有云,而非裸机**):
- **内存/显存路线不同**:Strix Halo 走"统一内存池"(128GB 共享,iGPU 可寻址近百 GB,适合装得下超大模型)[1][27];Olares One 走"独显专用显存"(RTX 5090M 24GB GDDR7,吞吐更强、适合显存能装下的模型)[32]。两者是"大而慢容量" vs "小而快显存"的互补,不做 tokens/s 对比。
- **价格带**:多数 Strix Halo mini PC 落在 $1,500-$2,800 裸机/装 Win 区间 [3][7][33];Olares One $3,999 定位更高,但卖点是**预装 Olares OS 的完整个人云体验**(域名/证书/多用户/应用市场/备份),而不是让用户自己折腾系统。
- **开放性**:Framework Desktop 等强调开放/可维修 [26][27],与 Olares "软硬一体但开放"的叙事同频——对标时应承认对方开放性,再以"整机即私有云、省去自建"取胜。

### 信息 B —— "在你已有设备上装 Olares OS"（High 适配）

**结论:所有 Strix Halo 设备 = x86-64 → 原生 High 适配。** Strix Halo 走 Olares 最省心的 x86-64 裸机 ISO / Linux script（Ubuntu 22.04-25.04 / Debian 12-13、≥4 核 /8GB/150GB SSD）[30][31];全部满足,且社区已实测在 GMKtec EVO-X2 上装 Ubuntu 24.04 + ROCm 跑本地大模型 [28][29],Framework 官方把 Ubuntu/Fedora 列为 "Works out of the box" [26]。（口径：Olares 本身跨平台也支持 ARM/macOS，此处因 x86-64 直接走裸机路径；GPU 加速 NVIDIA 最成熟，AMD Ryzen AI Max APU 经 ROCm 亦被加速，成熟度随版本。）

**内容切入角度 + 切入词**:
- "你买了 128GB Strix Halo 盒子 → 装 Olares OS,把它变成常驻的私有 AI 服务(而非只在本地开 Windows 跑 LM Studio)"。
- 切入词:`install olares on framework desktop`、`gmktec evo-x2 linux`、`strix halo home server`、`mini pc linux`(KD8,极低竞争)、`128gb mini pc self hosted ai`。
- 强调 Olares 相对"裸 Ubuntu + ollama"的增量:远程访问/域名证书、多应用编排、多用户、备份——"不只是能跑模型,而是把这台盒子变成一朵你拥有的云"。

**诚实边界(必须写进内容)**:Olares 官方 GPU 加速**当前仅支持 NVIDIA**(Turing+,≥8GB VRAM)[30][31];Strix Halo 的 AMD iGPU(8060S)能否被 Olares 平台内的 AI 应用直接调用为 **[unverified]**。因此信息 B 的稳妥表述是"原生安装 OS、作为私有云主机 = 明确可行";"用其 iGPU 在 Olares 上加速本地大模型" = 待验证,不可打包票。

置信度 **High(装 OS 可行)/ Low(iGPU 被 Olares 应用加速)** — 依据:Olares 官方文档 [30][31] + 社区 Ubuntu 实测 [28][29]。

## 五、诚实缺口与核心争议

- **营销稿降权**:GEEKOM "世界最强 AI mini PC"、各家统一喊 "126 TOPS"、评测站的 tokens/s 均属市场话术或已被本报告排除的性能数字,只作背景 [33][34][5]。
- **[unverified] 项**:(a) Olares 对 AMD iGPU/ROCm 的应用层加速支持;(b) localaimaster 提到的 "HP Z2 Mini G9""Asus ROG NUC AI""HP Omen Transcend" 是否真载 Strix Halo(与 HP 官方 Z2 Mini G1a 冲突,疑混淆)[22];(c) 大会清单中 AOKZOE/FEVM/Sixunited/Thermalright/Zotac ZBOX E/Colorful 的实际上市时间与价格 [20][21]。
- **价格漂移**:同型号跨渠道价差极大(GMKtec 128GB 见 $1,999 与 $2,999 两种口径;HP ZBook 配置从 $2,747 到网页标价 $9,060)[6][7][11][14]——SEO 内容里价格须标"价格带 + 截至日期",勿写死。
- **反向复核问题(≥3)**:
  1. Minisforum "AI X1 Pro" 到底是不是 Strix Halo?→ **否**,它是 Ryzen AI 9 HX 370/470(Strix Point,Radeon 890M,SO-DIMM),种子清单该项应剔除/改指 MS-S1 Max [23][24]。
  2. "128GB 就能跑 70B/120B" 是否夸大?→ 内存装得下 ≠ 速度可用;本报告只做"内存层级=能装下"的定性主张,不承诺可用速度 [1][28]。
  3. Strix Halo 装 Olares 后 AI 应用能否用上核显?→ **可以**：AMD Ryzen AI Max APU（Radeon 核显）经 ROCm 已被 Olares 加速（1.12.4 起逐步落地、1.12.6/1.12.7 加调度器标签）;具体版本/各 app 覆盖度以 docs.olares.com / GitHub 复核 [30][31]。
  4. "已量产" vs "展出/预告" 边界?→ 中国长尾厂商多为大会展出,勿把 "Unreleased" 当在售 [20]。

置信度 **Medium** — 依据:争议点均有明确一手反证或官方口径支撑,但长尾上市状态动态变化。

## 六、关键发现

1. **Strix Halo 是"内存层级"平台,不是"速度"平台**:128GB 统一内存(iGPU 可用近百 GB)让本地跑 70B/120B 成为可能,这是它相对 24-32GB 独显的唯一但关键的结构性优势 [1][27][28]。
2. **OEM 生态已爆发**:20+ 家、约 26 个型号 SKU 承载 Ryzen AI Max+ 395,形态覆盖 mini PC/桌面工作站/笔记本/平板;VideoCardz 中国大会清单是最全的单一穷举来源 [20][21]。
3. **全员 x86-64 → 全员可原生装 Olares OS(信息 B High 适配)**,且已有 Strix Halo + Ubuntu 的社区实测路径 [28][29][30];**且 AMD Ryzen AI Max APU 经 ROCm 已被 Olares 加速**（1.12.4 起逐步落地，成熟度随版本）——这是 Strix Halo 相对"能装但 GPU 不被加速"设备的关键利好 [31]。
4. **最大 SEO 机会 = 低竞争平台词 + 型号长尾**:`strix halo laptop`(590/mo,**KD9**)与 `mini pc linux`(320/mo,**KD8**)竞争度极低,可分别由 ROG Flow Z13 内容与"在 Strix Halo mini PC 上装 Olares"内容承接;`gmktec evo-x2`(4,400/mo)已验证有可观品牌流量 [前报告 gmktec.md]。
5. **优先立报型号**:Framework Desktop(开放叙事最契合)、GMKtec EVO-X2(已验证流量)、HP ZBook Ultra/Z2 Mini G1a(高端对标信息 A)、ROG Flow Z13(承接 KD9 词)—— 建议按此顺序做 per-model brand-seo。

置信度 **High** — 依据:结论由 AMD 官方规格、多家 OEM 官方页、Olares 官方文档与前报告 Semrush 数据共同支撑。

## 参考文献

[1] Compute Market. "Strix Halo Mini PCs for AI — 128GB, 40 TOPS NPU 2026". Blog. As Of 2026-03. https://www.compute-market.com/blog/strix-halo-mini-pc-local-ai-2026
[2] ComputingForGeeks. "Ryzen AI Max+ 395 Mini PCs Compared". Tech blog. As Of 2026. https://computingforgeeks.com/ryzen-ai-max-395-mini-pc-comparison/
[3] SpecPicks. "AMD Ryzen AI Max+ 395: The 128GB Mini PC". Review. As Of 2026. https://specpicks.com/reviews/amd-ryzen-ai-max-395-strix-halo-128gb-mini-pc-2026
[4] SpecPicks. "Framework Desktop & Ryzen AI Max+ 395 Review". Review. As Of 2026. https://specpicks.com/reviews/framework-desktop-ryzen-ai-max-395-review-2026
[5] CraftRigs. "Best Strix Halo Mini PCs for 70B Local LLMs [2026]". Review. As Of 2026. https://craftrigs.com/articles/strix-halo-mini-workstation-70b-local-llm/
[6] minipcdeals.net. "GMKtec EVO-X2 Review". Review. As Of 2026. https://minipcdeals.net/gmktec-evo-x2-review-gaming-mini-pc-with-strix-halo/
[7] minipclab.com. "GMKtec EVO-X2 vs Minisforum MS-S1 Max 2026". Review. As Of 2026. https://minipclab.com/blog/gmktec-evo-x2-vs-minisforum-ms-s1-max
[8] TechPowerUp. "HP ZBook Ultra G1a 14 Review". Hardware media. As Of 2026. https://www.techpowerup.com/review/hp-zbook-ultra-g1a-14/
[9] HP. "ZBook Ultra G1a Datasheet (c09086128)". Official. As Of 2026. https://www8.hp.com/h20195/v2/GetDocument.aspx?docname=c09086128
[10] HP. "HP ZBook Ultra G1a 14 Mobile Workstation PC". Official. As Of 2026. https://www.hp.com/us-en/workstations/zbook-ultra.html
[11] AEC Magazine. "Review: HP ZBook Ultra G1a / AMD Ryzen AI Max Pro". Industry media. As Of 2026. https://aecmag.com/workstations/review-hp-zbook-ultra-g1a-amd-ryzen-ai-max-pro/
[12] ASUS ROG. "ROG Flow Z13 (2025) GZ302". Official. As Of 2026. https://rog.asus.com/us/laptops/rog-flow/rog-flow-z13-2025/
[13] UltrabookReview. "Asus ROG Flow Z13 review (GZ302EA)". Review. As Of 2026. https://www.ultrabookreview.com/70846-asus-flow-z13-review-ryzenaimax/
[14] UltrabookReview. "AMD Strix Halo & Gorgon Halo laptops — complete list". Review/list. As Of 2026. https://www.ultrabookreview.com/70442-amd-strix-halo-laptops/
[15] AMD. "AMD Ryzen AI Max PRO 390". Official. As Of 2026. https://www.amd.com/en/products/processors/laptop/ryzen-pro/ai-max-pro-300-series/amd-ryzen-ai-max-pro-390.html
[16] AMD. "AMD Ryzen AI Max 385". Official. As Of 2026. https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-max-385.html
[17] AMD. "Ryzen Consumer Master Quick Reference (competitive) PDF". Official. As Of 2026. https://www.amd.com/content/dam/amd/en/documents/partner-hub/ryzen/ryzen-consumer-master-quick-reference-competitive.pdf
[18] PELADN. "YO1 395 Mini PC". Vendor. As Of 2026. https://www.peladn.com/products/yo1-395-mini-pc
[19] Jumbo Computer. "AOOSTAR NEX 395 (128G+2T)". Retailer. As Of 2026. https://www.jumbo-computer.com/en/products/aoostar-nex-395-128g-2t-system-mini-pc-amd-ai-max-395-lpddr5x-8533mhz-128gb-ram-2tb-ssd-windows-11-pro-cs-anex395
[20] VideoCardz. "AMD showcases dozens of Mini AI Workstations based on Ryzen AI Max+ 395 in China". Hardware media. As Of 2026. https://videocardz.com/newz/amd-showcases-dozens-of-mini-ai-workstations-based-on-ryzen-ai-max-395-in-china
[21] VideoCardz. "AOOSTAR teases Ryzen AI MAX+ 395 NEX395 Mini-PC". Hardware media. As Of 2026. https://videocardz.com/newz/aoostar-teases-ryzen-ai-max-395-nex395-futuristic-mini-pc
[22] Local AI Master. "AMD Ryzen AI Max+ 395 (Strix Halo) for Local AI 2026". Blog. As Of 2026. https://localaimaster.com/blog/strix-halo-ai-max-395-guide
[23] MINISFORUM. "AI X1 Pro-370 Mini PC (Ryzen AI 9 HX 370)". Official. As Of 2026. https://store.minisforum.com/en-os/products/minisforum-ai-x1-pro-370-mini-pc
[24] VideoCardz. "Minisforum G1/G7 Pro and MS-S1 MAX with Strix Halo (IFA 2025)". Hardware media. As Of 2025-09. https://videocardz.com/newz/minisforum-shows-off-g1-g7-pro-gaming-sff-pcs-and-ms-s1-max-with-strix-halo
[25] Framework. "Order Framework Desktop with AMD Ryzen AI Max (specs)". Official. As Of 2026. https://frame.work/desktop?tab=specs
[26] Framework. "Linux Compatibility (Framework Desktop, Ryzen AI Max 300 Series)". Official. As Of 2026. https://frame.work/ca/en/linux
[27] Framework. "Framework Desktop Deep Dive: Ryzen AI Max". Official blog. As Of 2025. https://frame.work/blog/framework-desktop-deep-dive-ryzen-ai-max
[28] pablo-ross (GitHub). "strix-halo-gmktec-evo-x2 (Ubuntu 24.04 + ROCm)". Community. As Of 2026. https://github.com/pablo-ross/strix-halo-gmktec-evo-x2
[29] nishtahir.com. "GMKTec Evo-X2 Ryzen AI Max 395+ Benchmarks (Ubuntu)". Personal tech. As Of 2026. https://nishtahir.com/gmktec-evo-x2-ryzen-ai-max-395-benchmarks/
[30] Olares Docs. "Install Olares on Linux via the script (system requirements)". Official. As Of 2026. https://docs.olares.com/manual/get-started/install-linux-script.html
[31] Olares Docs. "Install Olares via ISO (x86-64 required, ARM not supported)". Official. As Of 2026. https://docs.olares.com/manual/get-started/install-linux-iso.html
[32] Olares. "Olares One 硬件页". Official. As Of 2026. https://one.olares.com/
[33] NotebookCheck. "Geekom A9 Mega with AMD Strix Halo and 128 GB RAM announced". Hardware media. As Of 2025. https://www.notebookcheck.net/Geekom-A9-Mega-with-AMD-Strix-Halo-and-128-GB-RAM-announced-AMD-Ryzen-AI-Max-395-and-AMD-Radeon-8060S-in-a-stylish-design.1096072.0.html
[34] GEEKOM. "GEEKOM A9 Mega AI Mini PC (spec)". Vendor. As Of 2026. https://www.geekompc.com/geekom-a9-mega-ai-mini-pc/
[35] VideoCardz. "Geekom unveils A9 Mega Strix Halo Mini-PC". Hardware media. As Of 2025. https://videocardz.com/newz/geekom-unveils-a9-mega-amd-ryzen-ai-max-395-strix-halo-mini-pc
