# ASUS ROG 游戏本系列 SEO 竞品分析报告

> 域名：rog.asus.com | SEMrush US | 2026-07-06
> ROG Strix SCAR 16/18 + Zephyrus G16：与 Olares One 同款 RTX 5090 Mobile 24GB（SCAR 系还常同款 Core Ultra 9 275HX），但明显更贵。**两轴齐打**——轴 2：Olares One $3,999 就是更便宜的同款 GPU 整机；轴 1：$3,999 出厂即 Olares OS 私有云全栈 + x86-64/NVIDIA CUDA 全验证、开箱即用私有 AI，游戏本是裸 Windows 需自己搭。另含 Strix Halo 二合一平板 Flow Z13（简要）

---

## 项目理解（前置）

ASUS ROG（Republic of Gamers）是 ASUS 旗下的顶级游戏硬件品牌，在笔记本领域有 Strix SCAR（极限性能）、Zephyrus（轻薄旗舰）、Flow（二合一平板）三条产品线。本报告聚焦四款具体产品，均与 Olares One（$3,999 / RTX 5090 Mobile 24GB GDDR7 / 96GB DDR5）存在竞争或对比关系：

| 产品 | 关键规格 | 价格带 (US) | 与 Olares One 的关系 |
|------|---------|-----------|---------------------|
| **ROG Strix SCAR 16** (G635, 2025) | Core Ultra 9 275HX + **RTX 5090 Mobile 24GB** (175W) + 64GB DDR5 + 16" mini-LED 2.5K 240Hz | ~$4,299–5,630 | **同款 CPU + 同款 GPU 却更贵**：Olares One $3,999 更便宜 + Olares OS 全栈开箱，游戏本是裸 Windows |
| **ROG Strix SCAR 18** (G835, 2025) | Core Ultra 9 275HX + **RTX 5090 Mobile 24GB** (175W) + 64GB DDR5 + 18" mini-LED 2.5K 240Hz | ~$4,299–6,200 | **同款 CPU + 同款 GPU 却更贵**：Olares One $3,999 更便宜；游戏本需自搭 AI 栈 |
| **ROG Zephyrus G16** (GU605/GU606) | Core Ultra 9 285H (2025) / 386H (2026) + **RTX 5090 24GB** (120W/160W) + 64GB LPDDR5x + 16" OLED | ~$4,554–5,499 | 同款 GPU（TGP 更低）却更贵；Olares One $3,999 更便宜 + Olares OS 私有 AI 开箱 |
| **ROG Flow Z13** (GZ302, 2025) | **AMD Ryzen AI Max+ 395**（Strix Halo APU）+ Radeon 8060S iGPU + 32-96GB + 13.4" 2.5K | $1,599–2,099 | **不同 GPU 路线**：arm64 APU，属 Strix Halo 组（参见 research/01-ai-soc/amd-ryzen-ai-max.md） |

> **注意**：ROG Flow Z13 (2025) 搭载 AMD Strix Halo APU（**非 RTX 5090**），在 devices.md 归类为组一（AMD Ryzen AI Max），不属于"RTX 5090 Mobile 游戏本"组。其 Olares 安装路径为 x86-64（Strix Halo = x86），GPU 为 AMD Radeon 8060S，经 ROCm 可被 Olares 加速。本报告作简要覆盖并注明，详细研究见组一相关报告。

| 项目 | ROG Strix SCAR 系列 | ROG Zephyrus G16 |
|------|---------------------|-----------------|
| 开源 / 许可证 | 闭源硬件；Windows 11 Pro 预装 | 闭源硬件；Windows 11 Pro 预装 |
| 核心差异化 | 175W max TGP（RTX 5090 全功率）、mini-LED 面板、ROG 电竞 DNA | 轻薄（~1.95-2.1kg）、OLED 面板、优先便携 |
| Olares 信息 B | Windows → WSL2 安装 Olares，NVIDIA GPU 完整加速 | 同上（RTX 5090 160W TGP，GPU 被完整加速） |
| 主要竞品 | Razer Blade 16/18、Lenovo Legion Pro 7i、MSI Titan 18 HX | 其他轻薄旗舰游戏本 |
| Olares Market | 未上架（硬件产品） |
| 来源 | [rog.asus.com SCAR 16](https://rog.asus.com/laptops/rog-strix/rog-strix-scar-16-2025/)、[SCAR 18](https://rog.asus.com/laptops/rog-strix/rog-strix-scar-18-2025/)、[Zephyrus G16](https://rog.asus.com/us/laptops/rog-zephyrus/rog-zephyrus-g16-2025-gu605/)、[Notebookcheck SCAR 16 评测](https://www.notebookcheck.net/The-RTX-5090-Laptop-and-mini-LED-inside-a-gaming-laptop-Asus-ROG-Strix-SCAR-16-2025-review.1012778.0.html)、[PCMag](https://www.pcmag.com/reviews/asus-rog-strix-scar-16-g635lw) |

---

## 流量基线（Phase 1）

### 概览（rog.asus.com）

| 指标 | 数据 |
|------|------|
| 域名 | rog.asus.com |
| 父域 SEMrush Rank | 692（asus.com 整站）|
| 自然关键词数（ROG 子域）| 180,280 |
| 月自然流量（US，ROG 子域）| 1,351,533 |
| 占 asus.com 总流量 | 34.45% |
| 排名 1-3 位（父域）| 49,265 词 |
| 排名 4-10 位（父域）| 86,580 词 |
| 排名 11-20 位（父域）| 86,885 词 |

> rog.asus.com 是 ASUS 的游戏硬件流量核心，月流量约 135 万，品牌词 KD 普遍 40-70，非 ASUS 难以正面攻打。

### ROG 子域 TOP 自然关键词（与本报告产品相关，按流量排序）

| 关键词 | 排名 | 月量 | KD | 流量 | 意图 | URL |
|--------|------|------|----|----|------|-----|
| asus rog flow z13 | 1 | 6,600 | 53 | 5,280 | 导航/商业 | /flow-z13-2025/ |
| asus rog zephyrus g16 laptop | 1 | 5,400 | 50 | 4,320 | 信息/商业 | /zephyrus-g16-2026/ |
| rog strix | 1 | 5,400 | 47 | 4,320 | 品牌/商业 | /strix-series/ |
| rog zephyrus | 1 | 5,400 | 44 | 4,320 | 品牌 | /zephyrus-series/ |
| asus zephyrus | 1 | 5,400 | 44 | 4,320 | 信息/商业 | /zephyrus-series/ |

> **ROG Strix SCAR 16/18 关键词未出现在 TOP 流量词中**，说明 SCAR 系列相比 Flow Z13 / Zephyrus G16 搜索量更小，但购买意向更强（CPC 更高）。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词（RTX 5090 游戏本对比词）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| rog zephyrus g16 | 5,400 | 61 | $0.58 | 信息/商业 | 主品牌词，ASUS 牢牢占位 |
| rog strix scar 18 | 1,600 | 50 | $0.78 | 信息 | SCAR 18 主词 |
| 5080 vs 5090 | 3,600 | 31 | $4.84 | 信息/商业 | ⭐⭐ KD<35，商业对比高 CPC |
| rog strix scar 16 | 590 | 47 | $0.66 | 信息/商业 | SCAR 16 主词 |
| 5090 gaming laptop | 590 | 30 | $1.23 | 信息/商业 | ⭐⭐ 品类对比词 |
| rog strix scar 16 review | 20 | 0 | — | 信息 | ⭐ KD=0，GEO 前瞻词 |
| asus rog scar 18 review | 20 | 0 | — | 信息 | ⭐ KD=0，GEO 前瞻词 |
| rtx 5090 laptop review | 20 | 0 | — | 信息 | ⭐ KD=0，GEO 前瞻词 |

### 品类词（RTX 5090 Mobile 系列）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| geforce rtx 50 series | 8,100 | 41 | $0.26 | 信息 | RTX 50 品类入口，KD 较低 |
| 5090 laptop | 3,600 | 38 | $0.87 | 信息 | ⭐⭐ KD<40，值得布局 |
| rtx 50 series | 2,900 | 39 | $0.26 | 信息 | 品类认知词 |
| 5080 laptop | 2,400 | 31 | $0.83 | 信息 | ⭐⭐ 5080 游戏本对比 |
| 5090 mobile vs | 1,900 | **23** | — | 信息 | ⭐⭐⭐ KD=23，对比意图，Olares One 可切入 |
| rtx 5080 laptop | 1,600 | **19** | $0.83 | 信息 | ⭐⭐⭐ KD 极低 |
| 5090 vs 5080 | 1,300 | **22** | — | 信息 | ⭐⭐⭐ 高频对比词，KD=22 |
| 5090 laptops | 880 | **37** | $0.87 | 信息 | ⭐⭐ 品类复数词 |
| rtx 5090 laptops | 590 | **32** | $1.32 | 信息 | ⭐⭐ 搜索量较大 |

### 产品 / 功能词（ROG 品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| rog flow z13 | 8,100 | 55 | $0.50 | 信息/商业 | Flow Z13 主词（Strix Halo 机型）|
| rog strix scar 18 | 1,600 | 50 | $0.78 | 信息 | SCAR 18 |
| rog strix scar 16 | 590 | 47 | $0.66 | 信息/商业 | SCAR 16 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| rog gaming laptop linux | — | — | — | — | Semrush 无数据，GEO 零竞争词 |
| rtx 5090 laptop ollama | — | — | — | — | GEO 前瞻词，无量但精准 |
| rtx 5090 laptop llm | — | — | — | — | GEO 前瞻词，搜索量极低 |
| 5090 mobile vs | 1,900 | **23** | — | 信息 | ⭐ 可写"5090 Mobile 游戏本 vs Olares One" |

---

## Olares 关联词（Phase 3）

**核心叙事切入点（两轴齐打）：这些游戏本与 Olares One 同款 RTX 5090 Mobile 24GB（SCAR 系还常同款 Core Ultra 9 275HX），却明显更贵。轴 2 直接成立——Olares One $3,999 就是更便宜的同款 GPU 整机；轴 1——$3,999 买到的是开箱即用的 Olares OS 私有云全栈（Olares Market 一键装 AI 应用、多用户、LarePass 安全远程、备份，x86-64 + NVIDIA CUDA 全验证），游戏本是裸 Windows 得自己搭。无头/散热/常驻只是轴 1 的支撑细节，不做主论点。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| 5090 mobile vs | 1,900 | 23 | — | ⭐⭐⭐ "RTX 5090 Mobile 游戏本 vs Olares One"：同款 GPU，Olares One $3,999 更便宜 + Olares OS 开箱即用私有 AI 全栈 |
| 5090 vs 5080 | 1,300 | 22 | — | ⭐⭐⭐ Olares One = $3,999 的满血 5090 Mobile 整机，同款 GPU 更便宜；不必为省钱降到 5080 |
| rtx 5080 laptop | 1,600 | 19 | $0.83 | ⭐⭐⭐ KD=19 量大，"与其 5080 游戏本，不如 $3,999 拿满血 5090 + Olares OS 私有云" |
| 5080 vs 5090 | 3,600 | 31 | $4.84 | ⭐⭐ CPC 极高，商业意图，对比文嵌入 Olares One $3,999 同款 GPU 更超值定位 |
| 5090 laptop | 3,600 | 38 | $0.87 | ⭐⭐ 品类词，文末对比 Olares One——同 GPU、更便宜、Olares OS 全栈 |
| 5090 gaming laptop | 590 | 30 | $1.23 | ⭐⭐ "同样 5090，$3,999 的 Olares One 更便宜还开箱即用私有 AI"方向 |
| rog strix scar 16 review | 20 | 0 | — | ⭐ GEO 前瞻词：对比评测带出 Olares One 更便宜 + Olares OS 全栈，AI Overview 可引用 |
| rtx 5090 laptop review | 20 | 0 | — | ⭐ 同上，GEO 引用机会 |

---

## ROG Flow Z13 (2025) 简要覆盖

> 本机型属于 **组一 AMD Ryzen AI Max（Strix Halo）**，与 ROG SCAR/Zephyrus 路线不同。简要整理，详见 research/01-ai-soc/amd-ryzen-ai-max.md。

**规格摘要：**
- AMD Ryzen AI Max+ 395（16 核 Zen 5，Strix Halo APU）
- AMD Radeon 8060S iGPU（非独显，无 GDDR7），性能对标 RTX 4070 Laptop（65-75W）
- 32-96GB LPDDR5X 统一内存（无独立 VRAM），x86-64
- 13.4" 2.5K 180Hz 触屏、1.2kg，$1,599-2,099

**Olares 信息 B：**
- x86-64 → 支持裸机 ISO / script 安装 Olares
- GPU 为 AMD Radeon（RDNA 3.5），经 ROCm 可被 Olares AI 应用加速
- 128GB 版本（高配）可用作本地 LLM 服务器（`strix halo laptop` KD=9，信号词）

**SEO 关键词信号：**

| 关键词 | 月量 | KD | 备注 |
|--------|------|----|----|
| rog flow z13 | 8,100 | 55 | 主品牌词 |
| strix halo laptop | 590 | 9 | ⭐⭐⭐ KD=9！Olares 极强机会 |
| asus rog flow z13 | 6,600 | 53 | 品牌词 |

> `strix halo laptop`（KD=9，590/mo）是 devices.md 组一最大 SEO 机会之一，已在该组的 research 中标注。ROG Flow Z13 的产品报告建议归入组一 Strix Halo 子目录，而非本报告（组二 RTX 5090 游戏本）。

---

## 优先行动清单（Top 10）

| # | 关键词 | 月量 | KD | 综合评分 | 一句话内容方向 |
|---|--------|------|----|---------|--------------|
| 1 | 5090 mobile vs | 1,900 | 23 | ⭐⭐⭐ | "同款 5090 Mobile，Olares One $3,999 更便宜 + Olares OS 私有 AI 全栈：游戏本 vs 无头整机怎么选" |
| 2 | rtx 5080 laptop | 1,600 | 19 | ⭐⭐⭐ | KD=19 量大，"与其 5080/5090 游戏本，不如 $3,999 拿满血 5090 + Olares OS 开箱私有云" |
| 3 | 5090 vs 5080 | 1,300 | 22 | ⭐⭐⭐ | CPC $4.84，Olares One = $3,999 满血 5090 整机，比选 5080 省钱更超值 |
| 4 | 5090 laptop | 3,600 | 38 | ⭐⭐ | 品类词高量，导购文对比 Olares One（同 GPU、更便宜、开箱私有云） |
| 5 | 5080 vs 5090 | 3,600 | 31 | ⭐⭐ | CPC $4.84 商业价值高，对比文内嵌 Olares One 同款 GPU 更超值定位 |
| 6 | 5090 gaming laptop | 590 | 30 | ⭐⭐ | "同样 5090 游戏本更贵，Olares One $3,999 开箱即用私有 AI"选题 |
| 7 | rog strix scar 16 review | 20 | 0 | ⭐ | KD=0，先发评测抢 GEO 引用位 |
| 8 | rtx 5090 laptop review | 20 | 0 | ⭐ | 同上，GEO 前瞻 |
| 9 | asus rog scar 18 review | 20 | 0 | ⭐ | 同上，GEO 前瞻 |
| 10 | 5090 laptops | 880 | 37 | ⭐⭐ | 品类词，量可观，布局 RTX 5090 整机对比页面 |

---

## 核心洞见

1. **品牌护城河**：rog.asus.com 月流量 135 万，SCAR / Zephyrus / Flow Z13 品牌词 KD 44-61，ASUS 已建立强品牌护城河。**正面打品牌词性价比低**；但"5090 mobile vs"、"rtx 5080 laptop"等品类/对比词 KD 19-23，外部内容有可乘之机。

2. **可复制的打法**：ROG 的打法是"产品评测页 + 论坛（rog-forum.asus.com）+ 品牌词积累"，无明显程序化落地页策略。Olares 可**复制"同款 GPU 两轴对比"的内容矩阵**：针对每款顶级 RTX 5090 游戏本写对比文，统一指向 Olares One 作为"同款 GPU 更便宜（$3,999）+ Olares OS 开箱即用私有 AI"的定位（无头/常驻优势作支撑）。

3. **对 Olares 最关键的词**（均为对比/品类词，两轴都能打）：
   - `5090 mobile vs`（KD=23，月量 1,900）— 最高优先级，同款 GPU 直接对比
   - `rtx 5080 laptop`（KD=19，月量 1,600）— KD 最低量最大
   - `5090 vs 5080`（KD=22，月量 1,300）— CPC $4.84 高商业价值

4. **最大攻击面**（两轴）：① **价格**——SCAR/Zephyrus 同款 RTX 5090 Mobile 24GB（SCAR 系还常同款 275HX）却要 $4,299–6,200，Olares One $3,999 明显更便宜；② **开箱即用的 AI OS 层**——$3,999 出厂即 Olares OS 私有云全栈（一键装 AI 应用、多用户、LarePass 远程、备份，CUDA 全验证），游戏本只是裸 Windows 得自己搭。形态弱点（有屏、需合盖、200W+、配 380W 电源砖不适合 7×24 常驻）作为轴 1 的支撑细节，不做标题级主论点。

5. **隐藏低 KD 金矿**：
   - `5090 mobile vs`（KD=23，量 1,900）
   - `5090 vs 5080`（KD=22，量 1,300）
   - `rtx 5080 laptop`（KD=19，量 1,600）
   - `rtx 5090 laptop review`（KD=0，量 20）
   这四个词覆盖"比较意图"用户，是 Olares 内容的核心切入口。

6. **GEO 前瞻布局**：
   - `rog strix scar 16 review`（KD=0，量 20）
   - `asus rog scar 18 review`（KD=0，量 20）
   - `rtx 5090 laptop review`（KD=0，量 20）
   - `rtx 5090 laptop llm`（量极低但 Perplexity 已在回答此类问题）
   率先发布这些词对应的评测/对比文，可获 AI Overview 引用位。

7. **与既有 olares-500-keywords 的关联**：既有词表中"rtx 5090"相关词已有覆盖（参见 04-dgpu 报告），但"游戏本 vs Olares One"的对比角度尚未专文处理。本报告补充了 RTX 5090 Mobile 游戏本的具体型号词（SCAR 16/18、Zephyrus G16）和"5090 mobile vs"类对比词，建议在 `content/` 目录下创建对应对比文。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、phrase_these、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*产品规格来源：[rog.asus.com SCAR 16](https://rog.asus.com/laptops/rog-strix/rog-strix-scar-16-2025/)、[SCAR 18](https://rog.asus.com/laptops/rog-strix/rog-strix-scar-18-2025/)、[Zephyrus G16 (2026)](https://www.ultrabookreview.com/75392-asus-rog-zephyrus-g16-gu606-review/)、[Notebookcheck SCAR 16](https://www.notebookcheck.net/The-RTX-5090-Laptop-and-mini-LED-inside-a-gaming-laptop-Asus-ROG-Strix-SCAR-16-2025-review.1012778.0.html)（2026-07）。价格随库存变动，引用前以官网为准。*
