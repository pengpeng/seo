# Framework Desktop SEO 竞品分析报告

> 域名：frame.work | SEMrush US | 2026-07-06
> 全球首款模块化可维修 Mini-ITX 桌面 PC，搭载 AMD Ryzen AI Max（Strix Halo），Linux 一等公民，本地 AI 计算旗舰

---

## 项目理解（前置）

Framework Computer（成立 2020 年，旧金山）以"可维修 / 模块化笔记本"起家，2025 年推出第一款桌面产品 **Framework Desktop**：4.5L Mini-ITX 形态，搭载 AMD Ryzen AI Max 300 系列（"Strix Halo"），最高 128GB LPDDR5x-8000 统一内存（可用 96GB 作 GPU 显存），使用标准 PC 零件（FlexATX 电源、120mm 风扇），支持 Ubuntu / Fedora 官方发行版，社区活跃（community.frame.work）。与 Olares 的叙事高度契合：**开放硬件 + Linux 一等公民 + 本地 AI 算力**。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 模块化可维修桌面 PC + AMD Ryzen AI Max 本地 AI 算力 |
| 开源 / 许可证 | 硬件 CAD / 维修文档公开；EC 固件部分开源（MIT）；整机非完全开源 |
| 主仓库 | github.com/FrameworkComputer（EC、OS 指南等，~5k ★） |
| 核心功能 | 标准 Mini-ITX + FlexATX 可更换；Ryzen AI Max 最高 128GB 统一内存；AMD ROCm GPU 加速；USB4×2 / DisplayPort×4 / HDMI；Ubuntu & Fedora 官方支持 |
| 商业模式 / 定价 | 纯硬件销售，DIY Edition；Max 385 32GB 起 $1,099；Max+ 395 64GB ~$1,600；Max+ 395 128GB ~$2,605（as tested PCMag）；**无 SaaS / 订阅** |
| 差异化 / 价值主张 | 唯一把"可维修主义"与高性能 Strix Halo APU 结合在标准 Mini-ITX 体的品牌；社区驱动；Linux 原生路径 |
| 主要竞品（初判）| GMKtec EVO-X2 AI（$2,999，128GB）、Minisforum MS-S1 Max（$2,399，10GbE）、Beelink GTR9 Pro（散热取向）|
| Olares Market | 不适用（硬件产品）|
| 来源 | [frame.work/desktop](https://frame.work/desktop)、[PCMag 评测](https://ca.pcmag.com/desktop-pcs/1178/framework-desktop)、[Notebookcheck 评测](https://www.notebookcheck.net/Framework-Desktop-review-Mini-PC-wrapped-in-a-mini-ITX-body.1115803.0.html)、[frame.work/linux](https://frame.work/linux)、[AMD ROCm Strix Halo 优化指南](https://rocm.docs.amd.com/en/docs-7.2.0/how-to/system-optimization/strixhalo.html) |

**信息 A（Olares One vs Framework Desktop，主信息 A 优先，价格轴反转）**：
- Framework Desktop 128GB 版约 $2,605（不含 OS），比 Olares One（$3,999 零售）便宜——**别硬说 Olares One 更便宜，主打轴 1「AI 更好用」**
- 轴 1：Olares One = 真 24GB GDDR7 独显 + 成熟 CUDA（覆盖 ComfyUI/SD 等 AMD ROCm 覆盖窄的应用）+ Olares OS 软硬一体开箱即用（Olares Market 一键装 AI、多用户、LarePass 远程、备份）+ 第一方实测背书；Framework Desktop = AMD Ryzen AI Max+ 395 iGPU（经 ROCm、成熟度低）+ 128GB 统一内存，需自配 OS/应用。iGPU 本地 AI 短板可**类比同芯 Beelink GTR9 Pro 实测**（LLM 吞吐全场最低、无 CUDA 跑不了图像/视频；同芯其它整机因 OEM 调校单并发或高约 30%，不改架构结论）
- 轴 2：不打"更便宜"，讲"每美元可用 AI + 开箱即用"（Framework $2,605 只是硬件，还需自搭 Ubuntu + ROCm + 应用栈）
- **诚实边界**：Framework Desktop 128GB 统一内存能装下 GPT-OSS-120B（Olares One 24GB 需 offload），超大 MoE/dense 上统一内存有其位置

**信息 B（在 Framework Desktop 上装 Olares）**：
- x86-64 裸机 ISO 原生支持；AMD GPU 经 ROCm 被 Olares AI 应用加速
- 社区已有完整指南（Ubuntu 24.04 + ROCm 7.2.1 + llama.cpp），kernel ≥6.14.0-1018 / ≥6.18.4 是稳定路径
- GPU 加速门槛：需设置 GRUB 参数（kernel 6.18.4 后简化）；gfx1151 在 ROCm 7.2.x 官方标 Preview，社区已跑通

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | frame.work |
| SEMrush Rank | 16,504 |
| 自然关键词数 | 19,012 |
| 月自然流量（US）| 135,557 |
| 自然流量估值 | $171,671/月 |
| 付费关键词数 | 0（无 Google Ads 投放）|
| 月付费流量 | 0 |
| 排名 1–3 位 | 1,551 词 |
| 排名 4–10 位 | 3,888 词 |
| 排名 11–20 位 | 2,564 词 |

> 对比旧档（2026-07-03）：Rank 16,543→16,504（微升）；流量 134,596→135,557；关键词 22,097→19,012（可能是 Semrush 收录口径调整）。整体基线稳定。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| frame.work（主站）| 5,286 | 107,245 | 79.1% |
| community.frame.work | 12,172 | 24,880 | 18.4% |
| knowledgebase.frame.work | 1,201 | 3,005 | 2.2% |
| guides.frame.work | 330 | 388 | 0.3% |
| 其他（keyboard / downloads 等）| 少量 | <40 | <0.1% |

**关键洞察**：community.frame.work 贡献 18.4% 流量（24,880），关键词数甚至多于主站（12,172 vs 5,286），这是 Framework 最独特的流量来源——用户生成内容（UGC）拉动长尾词，Olares 的 community / blog 可以复制此路径。

### 官网 TOP 自然关键词（TOP 50，按流量降序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| framework laptop | 1 | 40,500 | 71 | $1.67 | 32,400 | 导航 | frame.work/ |
| framework desktop | 1 | 8,100 | 71 | $1.94 | 6,480 | 商业 | frame.work/desktop |
| framework 12 | 1 | 6,600 | 54 | $1.41 | 5,280 | 信息 | frame.work/laptop12 |
| framework 16 | 1 | 5,400 | 62 | $1.51 | 4,320 | 信息 | frame.work/laptop16 |
| framework laptops | 1 | 4,400 | 70 | $1.67 | 3,520 | 导航 | frame.work/ |
| framework laptop 13 | 1 | 3,600 | 50 | $1.97 | 2,880 | 信息 | frame.work/laptop13 |
| framework 13 | 1 | 2,900 | 49 | $2.06 | 2,320 | 信息 | frame.work/laptop13 |
| framwork（错拼）| 1 | 2,900 | 83 | $0.38 | 2,320 | 导航 | frame.work/ |
| framework laptop 16 | 1 | 2,900 | 54 | $1.62 | 2,320 | 信息 | frame.work/laptop16 |
| framework（通用词）| 1 | 74,000 | 83 | $0.38 | 1,924 | 导航 | frame.work/ |
| framework computers | 1 | 2,400 | 77 | $0.81 | 1,920 | 信息 | frame.work/ |
| framework pc | 1 | 1,900 | 72 | $3.46 | 1,520 | 信息 | frame.work/ |
| framework 13 laptop | 1 | 1,600 | 45 | $2.63 | 1,280 | 信息 | frame.work/laptop13 |
| **framework 13 pro** | 1 | 1,600 | **21** | $2.08 | 1,280 | 信息 ⭐ | frame.work/laptop13pro |
| framework computer | 1 | 1,600 | 75 | $4.16 | 1,280 | 导航 | frame.work/ |
| frameworks | 2 | 8,100 | 38 | $0.38 | 1,069 | 信息 | frame.work/ |
| framework laptop 12 | 1 | 1,300 | 64 | $3.46 | 1,040 | 商业 | frame.work/laptop12 |
| frameworks laptop | 1 | 1,300 | 71 | $2.90 | 1,040 | 导航 | frame.work/ |
| **soldered ram desktop future** | 2 | 12,100 | **21** | $0 | 992 | 信息 ⭐ | community（UGC）|
| frame work laptops | 1 | 1,000 | 72 | $2.90 | 800 | 导航 | frame.work/ |
| framework laptop 13 pro | 1 | 880 | 35 | $1.59 | 704 | 信息 | frame.work/laptop13pro |
| what is secure boot | 4 | 49,500 | 46 | $0 | 643 | 信息 | knowledgebase.frame.work |
| framwork laptop（错拼）| 1 | 720 | 58 | $1.67 | 576 | 导航 | frame.work/ |
| franework（错拼）| 1 | 590 | 70 | $0.49 | 472 | 导航 | frame.work/ |
| gaming laptop with replaceable parts | 1 | 1,900 | **37** | $0 | 471 | 信息 ⭐ | frame.work/ |
| frame work | 1 | 1,900 | 72 | $0.38 | 471 | 导航 | frame.work/ |
| **best linux distro for gaming** | 2 | 5,400 | **28** | $0 | 442 | 信息 ⭐ | community.frame.work |
| **ryzen ai max** | 1 | 1,600 | **42** | $0.48 | 396 | 信息 | frame.work/desktop?tab=specs |
| framework 12 laptop | 1 | 480 | 65 | $2.07 | 384 | 商业 | frame.work/laptop12 |
| framnework（错拼）| 1 | 480 | 82 | $0.49 | 384 | 导航 | frame.work/ |
| **aim max +**（桌面型号词）| 2 | 2,400 | **29** | $0.31 | 316 | 信息 ⭐ | frame.work/desktop?tab=specs |
| framework pro | 1 | 390 | 29 | $1.82 | 312 | 商业 | frame.work/laptop13pro |
| framework chromebook | 1 | 320 | 17 | $1.11 | 256 | 信息 | community.frame.work（UGC）|
| framework phone | 1 | 320 | 25 | $0 | 256 | 信息 | community.frame.work（UGC）|
| laptop frame | 1 | 320 | 41 | $0 | 256 | 商业 | frame.work/ |
| framework pcs | 1 | 320 | 53 | $3.41 | 256 | 信息 | frame.work/ |
| **framework mainboard** | 1 | 320 | **36** | $0 | 256 | 信息 | frame.work/products/framework-desktop-mainboard |
| modular computer | 1 | 320 | 60 | $3.19 | 256 | 商业 | frame.work/ |
| **build your own laptop** | 1 | 1,900 | **31** | $1.51 | 250 | 信息 ⭐ | frame.work/ |
| **framedeck**（DIY 掌机）| 1 | 1,000 | **37** | $2.06 | 248 | 信息 | community.frame.work（UGC）|
| customizable laptop | 1 | 880 | 34 | $1.77 | 218 | 信息 | frame.work/ |
| modular laptops | 1 | 880 | 42 | $1.78 | 218 | 信息 | frame.work/ |
| modular laptop | 1 | 8,100 | 56 | $1.59 | 210 | 信息 | frame.work/ |
| framework desktop pc | 1 | 260 | 59 | $1.46 | 208 | 信息 | frame.work/desktop |
| framework motherboard | 1 | 260 | 36 | $0 | 208 | 信息 | frame.work/products/mainboard |

> Desktop 专属词：`framework desktop`（8,100/mo，KD=71）、`ryzen ai max`（1,600，KD=42）、`aim max +`（2,400，KD=29）都从 `/desktop?tab=specs` 获取流量——**一个 specs 页承担了 Desktop 所有 SEO**。

### 付费词（Google Ads）

frame.work **完全不投放 Google Ads**（paid_keywords=0），依赖纯自然流量——这是品牌自信，也意味着无付费拦截位置可切。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ⭐⭐⭐ ms-s1 max | 1,900 | 21 | $0.74 | 信息 | Minisforum 竞品词，KD 超低 |
| ⭐⭐ framework desktop review | 390 | 32 | $0.43 | 信息/评测 | KD=32，有评测意图 |
| ⭐ strix halo desktop | 90 | 31 | $1.09 | 信息 | 品类词 + 桌面形态 |
| ⭐ ryzen ai max mini pc | 90 | 25 | $0.60 | 信息 | 直接品类描述 |
| framework laptop alternative | 10 | 0 | $0 | — | 极低量；暂无搜索需求 |
| framework computer alternative | <10 | — | — | — | 无有效数据 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| modular laptop | 8,100 | 56 | $1.59 | 信息 | 大词，frame.work 排 #1 |
| ai max 395 | 2,400 | 44 | $0 | 信息 | SoC 型号词 |
| ⭐⭐ custom laptop | 1,900 | 26 | $1.39 | 信息 | KD=26，量可观 |
| ⭐ build your own laptop | 1,900 | 31 | $1.51 | 信息 | frame.work 排 #1（250 流量）|
| ⭐ intel laptop | 1,600 | 30 | $1.56 | 商业 | 相关但非核心 |
| strix halo mini pc | 880 | 34 | $0.41 | 信息 | 具体品类 |
| ⭐ build my laptop | 880 | 31 | $1.46 | 信息 | DIY 用户意图 |
| ⭐ build your own laptop computer | 880 | 35 | $1.63 | 信息 | 同上变体 |
| ⭐ linux mini pc | 590 | 14 | $0.37 | 信息 | **KD=14！** 最低 KD 品类词 |
| ⭐⭐⭐ mini pc linux | 320 | 8 | $0.37 | 信息 | **KD=8！** 超低竞争 |

### 产品 / 功能词（Strix Halo 系）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| amd strix halo | 1,600 | 29 | $0.83 | 信息 | ⭐ SoC 品类词 |
| radeon 8060s | 1,300 | 41 | $0 | 信息 | GPU 型号词 |
| ⭐⭐⭐ ryzen ai max 395 laptop | 1,000 | 18 | $1.35 | 信息 | KD=18！高量低 KD |
| ryzen ai max 395 mini pc | 720 | 30 | $0.47 | 信息 | ⭐ 具体搜索 |
| ⭐⭐ ryzen ai max+ 395 laptop | 720 | 26 | $0.92 | 信息 | KD=26，笔记本变体 |
| ⭐⭐⭐ amd ryzen ai max 395 laptop list | 590 | 18 | $0 | 信息 | KD=18！"清单"型内容词 |
| ⭐⭐⭐ amd ryzen ai max+ 395 laptops | 590 | 24 | $0.53 | 信息 | KD=24 |
| ⭐⭐⭐⭐ strix halo laptop | 590 | **9** | $1.41 | 信息 | **KD=9！整个品类最低** |
| ⭐⭐⭐⭐ strix halo laptops | 590 | **8** | $1.36 | 信息 | **KD=8！** 复数变体 |
| aim max plus | 320 | 30 | $0.37 | 信息 | ⭐ 型号别名 |
| ⭐ strix halo pc | 90 | 24 | $1.78 | 信息 | 桌面方向 |
| framework desktop | 8,100 | 71 | $2.02 | 商业 | 品牌词，KD 高 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| best linux distro for gaming | 5,400 | 28 | $0 | 信息 | frame.work 社区排 #2（442 流量）⭐ |
| soldered ram desktop future | 12,100 | 21 | $0 | 信息 | frame.work 社区排 #2（992 流量）⭐ |
| ⭐ linux mini pc | 590 | 14 | $0.37 | 信息 | **KD=14，Olares 核心词** |
| ⭐ mini pc linux | 320 | 8 | $0.37 | 信息 | **KD=8！** |
| home server linux | 70 | 28 | $1.90 | 信息 | ⭐ 低量精准 |
| modular pc linux | <10 | — | — | — | 近零量，GEO 布局词 |
| self hosted ai pc | <10 | — | — | — | 近零量，GEO 布局词 |
| framework computer linux | <10 | — | — | — | 近零量，GEO 布局词 |

---

## Olares 关联词（Phase 3）

**核心叙事（主信息 A 优先）**：Olares One 对比 Framework Desktop 主打轴 1「AI 更好用」——真 24GB GDDR7 独显 + 成熟 CUDA（AI 应用全覆盖）+ Olares OS 开箱即用 + 第一方实测背书（Framework 的 iGPU 短板可类比同芯 Beelink 实测：LLM 吞吐全场最低、无 CUDA 跑不了图像/视频）；Framework 更便宜，价格轴反转不硬打，轴 2 讲"每美元可用 AI + 开箱即用"（省去手动搭 Ubuntu + ROCm + 应用栈的折腾）。兜底信息 B：在 Framework Desktop 装 Olares（x86 裸机 ISO，AMD ROCm 加速）的详细路径——只对已买 Framework 的人讲。诚实边界：120B 超大模型 24GB 装不下，Framework 128GB 统一内存反而能装。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| ⭐⭐⭐⭐ strix halo laptop | 590 | **9** | $1.41 | **KD=9！** 评测文：Strix Halo 最佳整机对比（Framework Desktop vs Olares One vs ZBook Ultra）+ 装 Olares 教程 |
| ⭐⭐⭐⭐ strix halo laptops | 590 | **8** | $1.36 | KD=8！复数变体，同上内容目标 |
| ⭐⭐⭐ ms-s1 max | 1,900 | **21** | $0.74 | 对比文：Minisforum MS-S1 Max vs Framework Desktop vs Olares One——装 Olares 的三路径 |
| ⭐⭐⭐ ryzen ai max 395 laptop | 1,000 | **18** | $1.35 | "Ryzen AI Max 395 最佳整机清单"：含 Olares One 作为软硬一体选项 |
| ⭐⭐⭐ amd ryzen ai max 395 laptop list | 590 | **18** | $0 | 清单型内容：所有 Strix Halo 整机 + 每款装 Olares 的路径差异 |
| ⭐⭐⭐ linux mini pc | 590 | **14** | $0.37 | "Linux Mini PC 完全指南"：Olares One 是最简单的开箱即用 Linux 私有云 Mini PC |
| ⭐⭐⭐ mini pc linux | 320 | **8** | $0.37 | KD=8！同上，关键词变体，单独内容或 canonical 版本 |
| ⭐⭐ amd strix halo | 1,600 | **29** | $0.83 | 科普文：Strix Halo 是什么 + 为什么是本地 AI 最佳 APU + Olares One 对标 |
| ⭐⭐ framework desktop review | 390 | **32** | $0.43 | 评测文：Framework Desktop 详测 + "Olares 用户应该买 Olares One 还是 Framework Desktop？" |
| ⭐ best linux distro for gaming | 5,400 | **28** | $0 | Framework 社区借力词（442 流量）——Olares 写"最适合本地 AI 的 Linux 平台"平行内容 |
| ⭐ home server linux | 70 | **28** | $1.90 | 精准信息词："在 Framework Desktop 上搭建 Linux 家庭服务器 + 安装 Olares" |

**GEO 前瞻（近零量，抢 AI Overview 引用位）**：
- `install olares on framework desktop` — 详细教程，0 竞争
- `framework desktop self hosted ai` — 概念词，会随 LLM 本地化趋势增长
- `olares one vs framework desktop` — 直接对比词，GEO 布局

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| soldered ram desktop future | 12,100 | 21 | $0 | 信息 | 次级 | Framework 社区 UGC 借力词 |
| best linux distro for gaming | 5,400 | 28 | $0 | 信息 | 主词候选 | 借社区 UGC 路径，写"最适合本地 AI 的 Linux 平台"平行内容，Olares 作私有 AI 侧补充 |
| ai max 395 | 2,400 | 44 | $0 | 信息 | 次级 | SoC 型号词 |
| ms-s1 max | 1,900 | 21 | $0.74 | 信息 | 主词候选 | Minisforum 竞品词 KD 低，"MS-S1 Max vs Framework Desktop vs Olares One"三路径对比 |
| amd strix halo | 1,600 | 29 | $0.83 | 信息 | 主词候选 | 科普文：Strix Halo 是什么 + Olares One 对标 |
| ryzen ai max 395 laptop | 1,000 | 18 | $1.35 | 信息 | 主词候选 | "最佳 Ryzen AI Max 395 整机清单"，含 Olares One 软硬一体选项 |
| strix halo mini pc | 880 | 34 | $0.41 | 信息 | 次级 | 具体品类词 |
| ryzen ai max+ 395 laptop | 720 | 26 | $0.92 | 信息 | 次级 | 笔记本变体 |
| strix halo laptop | 590 | 9 | $1.41 | 信息 | 主词候选 | KD9 最低竞争高价值词，Strix Halo 整机对比 + 装 Olares 教程，全网几乎无评测排 #1 可期 |
| strix halo laptops | 590 | 8 | $1.36 | 信息 | 次级 | 复数变体，同内容目标 |
| amd ryzen ai max 395 laptop list | 590 | 18 | $0 | 信息 | 次级 | 清单型内容词，程序化列表页 |
| linux mini pc | 590 | 14 | $0.37 | 信息 | 主词候选 | "Linux Mini PC 完全指南"，Olares One 开箱即用 Linux 私有云 |
| framework desktop review | 390 | 32 | $0.43 | 信息/评测 | 次级 | 评测词 + "买 Olares One 还是 Framework Desktop" |
| mini pc linux | 320 | 8 | $0.37 | 信息 | 次级 | KD8 变体，canonical 版本 |
| home server linux | 70 | 28 | $1.90 | 信息 | 次级 | "在 Framework Desktop 搭 Linux 家庭服务器 + 装 Olares" |
| framework laptop alternative | 10 | 0 | $0 | — | GEO | 近零量前瞻词，GEO 占位 |

---

## 核心洞见

1. **品牌护城河（能否正面刚）**：frame.work 在 `framework desktop`（8,100/mo，KD=71）、`framework laptop`（40,500/mo，KD=72）等品牌词上护城河极深——**不要正面刚**。机会在品类词（`strix halo laptop` KD=9、`mini pc linux` KD=8）：这些词 Framework 靠产品力自然排名，但内容几乎空白，Olares 可以用内容占据。

2. **可复制的打法（社区 UGC 带长尾）**：Framework 最独特的 SEO 引擎是 **community.frame.work**——12,172 个关键词、24,880 月流量（占 18.4%），`soldered ram desktop future`（12,100/mo，KD=21，992 流量）、`best linux distro for gaming`（5,400/mo，KD=28，442 流量）都来自社区帖子，**不是官方内容**。Olares 的 community / blog 发布技术帖子（"Framework Desktop + Olares 安装记录"、"ROCm 7.2 + llama.cpp 踩坑"）同样可以截获这类信息意图的长尾流量。

3. **对 Olares 最关键的词**：
   - `strix halo laptop`（590/mo，**KD=9**）——整个硬件赛道最低竞争高价值词，且 CPC=$1.41 证明商业价值，Olares 发一篇深度对比评测可排 #1
   - `mini pc linux`（320/mo，**KD=8**）+ `linux mini pc`（590/mo，KD=14）——Olares One 定位的核心词，几乎零竞争
   - `ms-s1 max`（1,900/mo，KD=21）——切入 Strix Halo 竞品对比的最大量低 KD 词

4. **最大攻击面（轴 1「AI 更好用」为主）**：
   - **CUDA 成熟度 + AI 应用覆盖**：Framework 的 Radeon iGPU 经 ROCm 加速、成熟度低（ComfyUI/SD 等需 CUDA 的应用覆盖窄），本地 AI 可用性可类比同芯 Beelink GTR9 Pro 实测（LLM 吞吐全场最低、无 CUDA 跑不了图像/视频）；Olares One 用成熟 CUDA + 24GB GDDR7 独显覆盖全部 AI 应用 + 第一方实测背书
   - **需要自配 OS 和所有应用**：Framework Desktop 是"裸机"，$2,605 只是硬件，还需自搭 Ubuntu + ROCm + 各类 AI 应用；Olares One = 硬件 + Olares OS + 所有应用开箱即用（价格轴反转，Olares 更贵，故不打"更便宜"，轴 2 讲"每美元可用 AI + 省去折腾"）
   - **ROCm 仍需调参**：Strix Halo 的 AMD GPU 加速在 ROCm 7.2.x 仍标 Preview，kernel 参数 / GRUB 配置有门槛；Olares One 用 NVIDIA 避开此坑
   - **无离家访问 OS**（轴 1 支撑细节）：Framework Desktop 是硬件，没有 LarePass 这类私有云 OS 的访问层
   - **诚实边界**：Framework 128GB 统一内存能装下 GPT-OSS-120B（Olares One 24GB 需 offload），超大 MoE/dense 上统一内存有其位置——写对比时主动承认

5. **隐藏低 KD 金矿**：
   - `amd ryzen ai max 395 laptop list`（590/mo，**KD=18**）——几乎空白的"清单型"词，Olares 可以做"2026 年 Strix Halo 整机推荐"程序化落地页，天然嵌入 Olares One 作为"软硬一体"选项
   - `ryzen ai max 395 laptop`（1,000/mo，**KD=18**）——同样低 KD，量更大
   - `mini pc linux`（320/mo，**KD=8**）——目前 SERPs 几乎没有权威内容，是真空地带

6. **GEO 前瞻布局**：
   - `framework desktop self hosted ai` — 近零量，但 AI Overview 对"在 Framework Desktop 上跑本地 AI"类问题会引用有实测内容的来源，Olares 的教程 + ROCm 踩坑记录会是天然引用对象
   - `olares one vs framework desktop` — AI 搜索会直接比较两款，Olares 官方发布对比文是 GEO 卡位的最高优先级
   - `strix halo homelab` — 类 Framedeck 的社区创意词，homelab 用户是 Olares 最精准的用户群

7. **与既有分析的关联**：
   - 旧档（2026-07-03）确认 `strix halo laptop`（KD=9）洞见持续有效，本次新发现 `strix halo laptops`（KD=8）复数变体同样有量
   - `ms-s1 max`（1,900/mo，KD=21）是旧档未覆盖的新机会词（Minisforum 竞品崛起）
   - `linux mini pc`（590/mo，KD=14）vs `mini pc linux`（320/mo，KD=8）是两个独立词，都应独立布局
   - 与 [olares-500-keywords-analysis](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md) 补充：Strix Halo 生态词（`strix halo laptop` KD=9）、`ms-s1 max`（KD=21）均不在原 500 词表，是新增机会

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、domain_organic_organic、phrase_these、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*项目信息来源：[frame.work/desktop](https://frame.work/desktop)、[PCMag 评测](https://ca.pcmag.com/desktop-pcs/1178/framework-desktop)、[Notebookcheck 评测](https://www.notebookcheck.net/Framework-Desktop-review-Mini-PC-wrapped-in-a-mini-ITX-body.1115803.0.html)、[AMD ROCm Strix Halo 指南](https://rocm.docs.amd.com/en/docs-7.2.0/how-to/system-optimization/strixhalo.html)（2026-07-06 核实）*
