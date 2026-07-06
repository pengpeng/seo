# GMKtec SEO 竞品分析报告（EVO-X2 / Strix Halo 系列）

> 域名：gmktec.com | SEMrush US | 2026-07-06
> GMKtec 是深圳 mini PC 品牌，EVO-X2 是其 AMD Ryzen AI Max+ 395（Strix Halo）旗舰机，最高 128GB 统一内存，直接对标 Olares One 价位带

---

## 项目理解（前置）

GMKtec 是深圳迈凯科技（Shenzhen GMKtec Technology）旗下品牌，专注 mini PC 整机，国内主要渠道为速卖通/亚马逊。EVO-X2 是其 Strix Halo 旗舰：搭载 AMD Ryzen AI Max+ 395（16C/32T Zen 5，4nm，126 TOPS），集成 Radeon 8060S（40 CU RDNA 3.5，媲美 RTX 4070 Mobile），最高 128GB LPDDR5X-8000 统一内存（可分配 96GB 给 GPU），定价区间 ~$1,499–$2,999（依内存/存储版本）。同系列另有 **EVO-X3**（2026 中发布，PS4 size，补 OCuLink 口，128GB/2TB 起 $3,600）和 **EVO-X1**（Ryzen AI 9 HX 370，低一档）。GMKtec 不做操作系统，裸机出厂预装 Windows 11 Pro；安装 Linux 需自行操作。

**Olares 对标（主信息 A 优先，价格轴反转）**：EVO-X2 ~$1,499–$2,999，比 Olares One（$3,999 零售）便宜——**别硬说 Olares One 更便宜，主打轴 1「AI 更好用」**：Olares One 是真 24GB GDDR7 独显 + 成熟 CUDA（覆盖 ComfyUI/SD 等 AMD ROCm 覆盖窄的应用）+ Olares OS 开箱即用（Olares Market 一键装 AI、多用户、LarePass 远程、备份）+ 第一方实测背书。EVO-X2 的 Radeon 8060S iGPU（经 ROCm、成熟度低）本地 AI 短板可**类比同芯 Beelink GTR9 Pro 实测**（AI Max+ 395：Qwen3-30B 并发 1→8 仅 61→12 tok/s、Gemma3-27B dense 近乎不可用、无 CUDA 跑不了图像/视频；同芯其它整机因 OEM 调校单并发或高约 30%，不改架构结论）。**诚实边界**：EVO-X2 128GB 统一内存能装下 GPT-OSS-120B（Olares One 24GB 需 offload），超大 MoE/dense 上统一内存有其位置。轴 2 打"每美元可用 AI + 开箱即用"。EVO-X2 是 x86-64，信息 B（装 Olares，AMD ROCm 加速）成立且顺，但仍是兜底。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 深圳 mini PC 硬件品牌，旗舰 EVO-X2 是 Strix Halo 最具性价比整机 |
| 开源 / 许可证 | 闭源硬件；无开源组件 |
| 主仓库 | 无 GitHub；官网 gmktec.com |
| 核心功能 | 16C Zen 5 CPU / 40CU Radeon 8060S iGPU / 最高 128GB 统一内存 / 126 TOPS AI / 140W 三风扇 |
| 商业模式 / 定价 | 硬件直销（官网 + Amazon）；EVO-X2：64GB $1,499 / 96GB $2,229 / 128GB $2,999；EVO-X3 128GB $3,600 |
| 差异化 / 价值主张 | 同配置 Strix Halo 整机中价格最低；支持 Qwen3 235B（128GB 版） |
| 主要竞品（初判）| Minisforum MS-S1 Max、Beelink GTR9 Pro、Framework Desktop（Ryzen AI Max）、HP Z2 Mini G1a |
| Olares Market | 不适用（硬件厂商，非软件应用） |
| 来源 | [官网](https://www.gmktec.com/products/amd-ryzen™-ai-max-395-evo-x2-ai-mini-pc)、[minipclab review](https://minipclab.com/blog/gmktec-evo-x2-ai-review)、[Tom's Hardware review](https://www.tomshardware.com/desktops/mini-pcs/gmktec-evo-x2-ai-mini-pc-review)、[Notebookcheck review](https://www.notebookcheck.net/AMD-Strix-Halo-in-the-GMKtec-EVO-X2-Powerful-mini-PC-with-AMD-Ryzen-AI-Max-395-and-Radeon-8060S-reviewed.1102641.0.html) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | gmktec.com |
| SEMrush Rank | 75,926 |
| 自然关键词数 | 1,305 |
| 月自然流量（US）| 26,186 |
| 自然流量估值 | $12,210 / 月 |
| 付费关键词数 | 53 |
| 月付费流量 | 1,627 |
| 付费流量估值 | $789 / 月 |
| 排名 1-3 位 | 175 词 |
| 排名 4-10 位 | 181 词 |
| 排名 11-20 位 | 200 词 |

> 洞察：头部 175 词几乎全是品牌拼写变体（gmktec / gmktek / gmktech / gmtec 等），non-brand 词流量极少。品牌词护城河坚实但天花板明显——**整站 US 月流量 2.6 万，弱于 Minisforum（6.7 万）**。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.gmktec.com | 1,137 | 24,821 | 94.8% |
| de.gmktec.com | 128 | 1,365 | 5.2% |
| jp.gmktec.com | 40 | 0 | 0.0% |

> 德语子域名已有独立流量，日语站基本没有。英语主站绝对主导。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| gmktec | 1 | 8,100 | 43 | $0.51 | 6,480 | 导航 | / |
| gmktec evo-x2 | 1 | 4,400 | 42 | $0.61 | 3,520 | 商业/信息 | /products/…evo-x2… |
| gmktek | 1 | 2,400 | 43 | $0.51 | 1,920 | 导航 | / |
| gmktec evo x2 | 1 | 1,900 | 40 | $0.61 | 1,520 | 商业/信息 | /products/…evo-x2… |
| gmktec ad-gp1 | 1 | 1,600 | 32 | $0.49 | 1,280 | 商业/信息 | /products/…ad-gp1… |
| gmtec mini pc | 1 | 880 | 43 | $0.39 | 704 | 导航 | / |
| gmktec evo-x1 | 1 | 590 | 20 | $0.61 | 472 | 商业 | /products/…evo-x1… |
| gmktech | 1 | 480 | 44 | $0.51 | 384 | 导航 | / |
| gmktec k11 | 1 | 390 | 35 | $0.42 | 312 | 商业 | /products/…k11 |
| gmktec g9 | 1 | 320 | 34 | $0.39 | 256 | 导航 | /products/…g9 |
| gmkteck | 1 | 320 | 36 | $0.51 | 256 | 导航 | / |
| gmktec drivers | 1 | 320 | 20 | $0.05 | 256 | 导航 | /pages/drivers… |
| gmktec g3 plus | 1 | 320 | 24 | $0.46 | 256 | 商业 | /products/…g3-plus |
| gmktec mini pc | 3 | 2,900 | 41 | $0.41 | 237 | 导航 | /collections/amd-mini-pc |
| gmtek | 1 | 1,000 | 29 | $0.39 | 248 | 导航 | / |
| gkmtec | 1 | 1,000 | 34 | $0.39 | 248 | 导航 | / |
| evo-x2 | 2 | 1,900 | 40 | $0.46 | 155 | 商业 | /products/…evo-x2… |
| gmktec k10 | 1 | 590 | 23 | $0.00 | 146 | 商业 | /products/…k10 |
| evo x2 | 2 | 720 | 41 | $0.39 | 95 | 商业 | /products/…evo-x2… |
| gmktec evo-x2 ai mini pc | 2 | 880 | 28 | $0.63 | 116 | 商业 | de.gmktec.com/…evo-x2… |
| gmktec mini pc deal | 1 | 110 | 18 | $0.00 | 88 | 商业 | /collections/clearance |
| gmktec 395 | 1 | 210 | 36 | $0.41 | 168 | 商业/信息 | /products/…evo-x2… |
| gmktec mini pc nas | 1 | 140 | 22 | $0.51 | 112 | 导航 | /products/…g9 |
| gmktec m7 pro | 1 | 110 | 16 | $0.37 | 88 | 导航/信息 | /products/…m7-pro |

> 关键发现：前 50 词约 90% 是品牌拼写变体（typo 词）；非品牌词排名 TOP1 的仅有 `evo-x2`（位置 #2，量 1900）。`gmktec drivers`（KD20）、`gmktec mini pc deal`（KD18）是少数低 KD 品牌词，反映用户有支持/折扣需求。

### 付费词（Google Ads，按流量排序）

GMKtec 在 Google Ads 上投放 53 个词，全部为品牌关键词（自有品牌名 + 产品型号），无非品牌竞争词投放，落地页均指向首页或产品页。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| gmktec | 1 | 8,100 | $0.51 | / |
| gmktec evo-x2 | 1 | 4,400 | $0.61 | /products/…evo-x2… |
| evo-x2 | 1 | 2,400 | $0.39 | / |
| gmktek | 1 | 2,400 | $0.39 | / |
| gmktec evo x2 | 1 | 1,900 | $0.61 | de.gmktec.com/…evo-x2… |
| gmtek | 1 | 1,000 | $0.39 | / |
| gkmtec | 1 | 1,000 | $0.39 | / |
| strix halo pc | 1 | 110 | $0.68 | /products/…evo-x2… |

> GMKtec 的付费策略非常保守：只买自己的品牌词，防御型投放，没有抢占竞品词或品类词。`strix halo pc`（CPC $0.68）是唯一非品牌付费词，量仅 110。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| dgx spark vs evo-x2 ⭐ | 320 | 16 | $0 | 商业/信息 | NVIDIA vs AMD AI 机对比，KD 极低 |
| gmktec evo-x1 | 720 | 31 | $0.61 | 商业/信息 | GMKtec 自家低一档机型 |
| beelink alternative | 20 | 0 | $0.67 | — | 极低量但 CPC 有 |
| minisforum alternative | 0 | 0 | $0.93 | — | 有 CPC 但暂无量 |
| gmktec alternative | 20 | 0 | $0 | — | 直接品牌替代词，零 KD |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| strix halo mini pc ⭐ | 880 | 34 | $0.41 | 信息 | Strix Halo 平台入口词 |
| ryzen ai max 395 mini pc ⭐ | 720 | 30 | $0.47 | 商业 | 型号品类词 |
| amd ryzen ai max+ 395 mini pc ⭐ | 390 | 30 | $0.39 | 商业 | 同上变体 |
| amd ryzen ai max 395 mini pc | 480 | 37 | $0.71 | 商业 | |
| mini pc linux ⭐⭐⭐ | 320 | **8** | $0.37 | 信息 | **KD 最低超大机会** |
| best mini pc linux ⭐ | 70 | 19 | $0.52 | 信息 | 低 KD，列表型内容 |
| mini pc homelab ⭐ | 40 | 13 | $0.53 | 信息 | homelab 群体入口 |
| best mini pc for ai ⭐ | 110 | 24 | $0.67 | 信息 | 购买决策词 |
| mini pc for home server | 110 | 30 | $0.47 | 信息 | 服务器场景 |
| amd strix halo mini pc ⭐ | 170 | 20 | $0.44 | 信息 | 低 KD 品类词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| gmktec evo-x2 | 4,400 | 42 | $0.61 | 商业/信息 | 核心产品词 |
| gmktec evo x2 | 1,900 | 31 | $0.61 | 商业/信息 | 变体拼写 |
| evo-x2 | 2,400 | 43 | $0.39 | 商业 | 裸型号 |
| gmktec evo-x2 ai mini pc ⭐ | 880 | 28 | $0.63 | 商业 | 产品全称 |
| gmk evo-x2 ⭐ | 390 | 31 | $0.49 | 商业 | 缩写变体 |
| gmktek evo x2 | 320 | 34 | $0.57 | 商业 | 品牌拼错变体 |
| gmktec mini pc review ⭐⭐ | 210 | **14** | $0.71 | 信息 | KD14 极低，评测词 |
| gmktec evo-x2 review ⭐ | 50 | 24 | $1.02 | 信息 | 评测词，CPC $1 |
| gmktec review | 90 | 36 | $1.13 | 信息 | 品牌评测词 |
| gmktec 395 ⭐ | 320 | 36 | $0.41 | 商业/信息 | 芯片型号关联 |
| ai max+ 395 | 590 | 48 | $1.51 | 商业 | KD48 高竞争 |
| mini pc ryzen ai max 395 ⭐ | 210 | 41 | $0.76 | 商业 | |
| ai max 395 mini pc ⭐ | 170 | 25 | $0.43 | 商业 | 低 KD |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| run llm locally | 590 | 47 | $3.50 | 商业 | 高 CPC，强商业意图 |
| self hosted llm ⭐ | 320 | 22 | $3.12 | 商业 | KD22 + CPC $3，高价值 |
| home ai server ⭐ | 140 | 14 | $1.78 | 商业 | KD14 + 商业意图强 |
| local ai server ⭐ | 90 | 26 | $4.26 | 商业 | CPC $4.26！高商业价值 |
| best mini pc for ai ⭐ | 110 | 24 | $0.67 | 信息 | 购买决策词 |
| local llm hardware ⭐ | 50 | 27 | $2.07 | 商业 | 购买硬件词 |
| mini pc homelab ⭐ | 40 | 13 | $0.53 | 信息 | homelab 入口 |
| ollama mini pc | 20 | 0 | $0 | — | 量小但精准 |

---

## Olares 关联词（Phase 3）

**核心叙事（主信息 A 优先）：Olares One 对比 EVO-X2 主打轴 1「AI 更好用」——真 24GB GDDR7 独显 + 成熟 CUDA（AI 应用全覆盖）+ Olares OS 开箱即用 + 第一方实测背书（EVO-X2 的 iGPU 短板可类比同芯 Beelink 实测：本地 LLM 全场最低、无 CUDA 跑不了图像/视频）；EVO-X2 更便宜，价格轴反转不硬打，轴 2 讲"每美元可用 AI + 开箱即用"。兜底信息 B：EVO-X2 是 x86-64，可装 Olares（AMD ROCm 加速）——只对已买 EVO-X2 的人讲。诚实边界：120B 超大模型 24GB 装不下，EVO-X2 128GB 统一内存反而能装。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| strix halo mini pc ⭐ | 880 | 34 | $0.41 | ⭐⭐⭐ Olares One vs GMKtec EVO-X2 全对比页：24GB CUDA 独显 vs iGPU 的 AI 可用性差距（轴 1，诚实注 120B 边界） |
| self hosted llm ⭐ | 320 | 22 | $3.12 | ⭐⭐⭐ Olares + Ollama/LLM 自托管：CUDA 成熟 + 开箱即用 vs EVO-X2 裸机自建（轴 1） |
| home ai server ⭐ | 140 | 14 | $1.78 | ⭐⭐⭐ "best home AI server 2026"榜单，Olares One vs EVO-X2（轴 1 AI 更好用） |
| local ai server ⭐ | 90 | 26 | $4.26 | ⭐⭐⭐ 高 CPC 证明买家意图强；Olares One vs EVO-X2 主打轴 1 |
| best mini pc for ai ⭐ | 110 | 24 | $0.67 | ⭐⭐ 榜单，突出 Olares One 轴 1（真独显 + CUDA + 开箱即用） |
| dgx spark vs evo-x2 ⭐ | 320 | 16 | $0 | ⭐⭐ "Olares One vs GMKtec EVO-X2 vs DGX Spark"三路对比；KD16 好打 |
| gmktec alternative | 20 | 0 | $0 | ⭐⭐⭐ KD0 零竞争；"Best GMKtec EVO-X2 Alternative: Olares One（AI 更好用）" |
| gmktec mini pc review ⭐ | 210 | 14 | $0.71 | ⭐⭐ 蹭 GMKtec 评测流量，写"GMKtec vs Olares One"对比 |
| local llm hardware ⭐ | 50 | 27 | $2.07 | ⭐⭐ 购硬件决策词；对比 DIY 裸机 vs Olares One 软硬套装 |
| mini pc linux ⭐⭐⭐ | 320 | **8** | $0.37 | ⭐⭐⭐ 信息 B："Install Olares on GMKtec EVO-X2"教程落地页，KD8 几乎零竞争 |
| amd strix halo mini pc ⭐ | 170 | 20 | $0.44 | ⭐⭐ 信息 B："AMD Strix Halo mini PC with Linux/Olares"教程 |
| mini pc homelab ⭐ | 40 | 13 | $0.53 | ⭐⭐ 信息 B：homelab 受众高度重叠；"mini pc homelab with Olares OS" |
| ollama mini pc | 20 | 0 | $0 | ⭐ 精准词；Olares OS 内建 Ollama 支持 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| gmktec evo-x2 | 4,400 | 42 | $0.61 | 商业/信息 | 次级 | 核心产品词，量大排不动，靠 review/alternative 切入 |
| evo-x2 | 2,400 | 43 | $0.39 | 商业 | 次级 | 裸型号词 |
| gmktec evo x2 | 1,900 | 31 | $0.61 | 商业/信息 | 次级 | 变体拼写 |
| strix halo mini pc | 880 | 34 | $0.41 | 信息 | 主词候选 | "Best Strix Halo Mini PC 2026"品类榜单，24GB CUDA 独显 vs iGPU 可用性（类比同芯 Beelink 实测，诚实注 120B） |
| gmktec evo-x2 ai mini pc | 880 | 28 | $0.63 | 商业 | 次级 | 产品全称 |
| ryzen ai max 395 mini pc | 720 | 30 | $0.47 | 商业 | 次级 | 型号品类词 |
| gmktec evo-x1 | 720 | 31 | $0.61 | 商业/信息 | 次级 | 低一档机型词 |
| ai max+ 395 | 590 | 48 | $1.51 | 商业 | 次级 | SoC 词，高竞争 |
| run llm locally | 590 | 47 | $3.50 | 商业 | 次级 | 高 CPC 品类核心词 |
| amd ryzen ai max 395 mini pc | 480 | 37 | $0.71 | 商业 | 次级 | 变体词 |
| dgx spark vs evo-x2 | 320 | 16 | $0 | 商业/信息 | 主词候选 | "Olares One vs EVO-X2 vs DGX Spark"三路对比，KD16 好打 |
| mini pc linux | 320 | 8 | $0.37 | 信息 | 主词候选 | 信息 B："Install Olares on GMKtec EVO-X2"，KD8 易上首页 |
| self hosted llm | 320 | 22 | $3.12 | 商业 | 主词候选 | Olares + Ollama 自托管：CUDA 成熟 + 开箱即用 vs 裸机自建（轴 1，高 CPC） |
| gmktec mini pc review | 210 | 14 | $0.71 | 信息 | 主词候选 | 蹭 GMKtec 评测流量，写"GMKtec vs Olares One"对比 |
| amd strix halo mini pc | 170 | 20 | $0.44 | 信息 | 次级 | 信息 B：Linux/Olares 教程 |
| gmktec alternative | 20 | 0 | $0 | — | GEO | KD0 零竞争，"Best GMKtec EVO-X2 Alternative: Olares One" |

---

## 核心洞见

1. **品牌护城河**：GMKtec 几乎所有流量来自品牌词（gmktec/gmktek/gmktech 等拼写变体），自然流量约 2.6 万/月（US），**品牌词 KD 均在 40+ 无法正面硬打**。非品牌词流量极薄，是其最大弱点。Minisforum 同品类竞争对手的 US 月流量为 6.7 万——两倍于 GMKtec。

2. **可复制的打法**：GMKtec 的 SEO 打法极其简单——靠品牌搜索量自然落坑，无内容矩阵、无博客、无教程。这让所有非品牌词都是开放机会：Lon.TV（10K 月流量）和 Liliputing（7.8K 月流量）靠评测内容获取了与 GMKtec 高度重叠的词，说明**评测/教程内容可有效拦截 GMKtec 目标用户**。

3. **对 Olares 最关键的词**：① `strix halo mini pc`（KD34，月量 880）——主信息 A 品类对比主战场，重点写 24GB CUDA 独显 vs iGPU 的 AI 可用性；② `self hosted llm`（KD22，月量 320，CPC $3.12）——高商业价值词，Olares + Ollama 天然落地页（轴 1）；③ `mini pc linux`（KD8，月量 320）——信息 B：EVO-X2 安装教程，几乎零竞争即可上首页。

4. **最大攻击面（轴 1「AI 更好用」为主）**：GMKtec EVO-X2 是 Radeon 8060S iGPU（经 ROCm、成熟度低），本地 AI 可用性可类比同芯 Beelink GTR9 Pro 实测（LLM 吞吐全场最低、无 CUDA 跑不了图像/视频，ComfyUI/SD 等应用覆盖窄）；Olares One 靠 24GB GDDR7 + 成熟 CUDA 覆盖全部 AI 应用 + Olares OS 开箱即用 + 第一方实测背书。价格轴反转（EVO-X2 更便宜），故不打"更便宜"，轴 2 讲"每美元可用 AI + 开箱即用"（EVO-X2 预装 Win11、自托管需自己折腾）。**诚实边界**：EVO-X2 128GB 统一内存能装下 GPT-OSS-120B（Olares One 24GB 需 offload），超大 MoE/dense 上统一内存有其位置。裸机（无私有云 OS）是信息 B（装 Olares）的切入点。

5. **隐藏低 KD 金矿**：
   - `mini pc linux` KD=**8**：量 320，几乎没人争，立刻能上首页
   - `home ai server` KD=**14**：量 140，CPC $1.78，商业意图
   - `gmktec mini pc review` KD=**14**：量 210，可拦截所有找评测的用户
   - `mini pc homelab` KD=**13**：量 40 但受众精准，homelab 用户与 Olares 高度重叠
   - `amd strix halo mini pc` KD=**20**：量 170，可写 Linux 安装教程

6. **GEO 前瞻布局**：以下词当前量小但语义契合 AI Overview/Perplexity 引用位——
   - `"best mini pc for local ai 2026"` / `"olares one vs gmktec evo-x2"` / `"strix halo linux install"`
   - `"can you run 70b llm on mini pc"` / `"gmktec evo-x2 with linux"`
   - 这类问答类内容在 AI Overview 中曝光概率高，建议提前布局 FAQ 结构化内容。

7. **与既有分析的关联**：
   - 与 [hardware/research/02-5090-laptops/](/Users/pengpeng/seo/directions/hardware/research) 的 RTX 5090 笔记本对比思路相同，但 Strix Halo 走 "iGPU + 统一内存" 路线，比独显路线的 Olares One 便宜 $1,000+；**两者不是替代关系而是互补 SKU**，文章可同时覆盖两端读者。
   - `run llm locally`（590/mo, KD47）在之前的 500 词分析中也出现过，说明这是 Olares 持续值得发力的品类核心词。
   - Minisforum.com（自然竞品第一，67K 月流量）已有独立报告/待报告，GMKtec 与 Minisforum 高度同质——同芯片、同价位、同目标用户，内容可以互用。

---

*数据来源：SEMrush US 数据库（domain_rank / domain_organic_subdomains / resource_organic / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
