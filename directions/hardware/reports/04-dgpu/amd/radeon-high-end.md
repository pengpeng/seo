# AMD Radeon 高端本地 AI 卡（RX 7900 XTX / RX 9070 XT / PRO W7900）SEO 竞品分析报告

> SEMrush US | 2026-07-06 | 型号词分析（无独立官网）| 来源：AMD 官方公开规格（快照，引用前需核实）
> AMD/ROCm 路线上的"大显存本地 AI 卡"——想避开 NVIDIA 生态、走性价比大显存的本地 LLM/出图玩家的主力选项。

---

## 项目理解（前置）

AMD 高端 Radeon 在本地 AI 上的卖点是**同价位更大显存 + 更低单卡成本**：消费旗舰 **RX 7900 XTX 24GB**（AMD 消费级最大显存）单卡可跑 70B Q4；**RX 9070 XT 16GB（RDNA4）**是 2025 年度性价比标杆；工作站 **Radeon PRO W7900 48GB** 面向显存党。软件栈是 **ROCm**（Olares 已经它做 GPU 加速），配合 Vulkan/llama.cpp 在 Ollama、ComfyUI 上可用，但生态成熟度仍落后 CUDA——这既是 AMD 用户的痛点，也正是内容与 Olares 的切入口。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AMD/ROCm 路线的高端本地 AI 独显（消费 24GB + 工作站 48GB），主打大显存性价比 |
| 开源 / 许可证 | 硬件闭源；软件栈 ROCm 开源（MIT / 多许可，github.com/ROCm/ROCm） |
| 代表型号 | RX 7900 XTX 24GB · RX 9070 XT 16GB(RDNA4) · Radeon PRO W7900 48GB · (语境) Radeon AI PRO R9700 32GB |
| 核心卖点 | 同价位更大显存、单卡成本低于同显存 NVIDIA、消费级 24GB 天花板 |
| 软件栈 | ROCm（Linux 成熟、Windows 较新）+ Vulkan / llama.cpp / Ollama / ComfyUI |
| 目标用户 | 想避开 NVIDIA、追求"省成本 + 大显存"的本地 AI 玩家；已有 Radeon 卡想跑 AI 的人 |
| 诚实边界 | ROCm 生态成熟度不及 CUDA，ComfyUI/微调等 CUDA-first 应用在 AMD 上覆盖较窄 |
| Olares 适配 | **AMD（含 Radeon，经 ROCm）已被 Olares GPU 加速支持**（见 devices.md GPU 加速口径） |
| 来源 | amd.com 产品页 / ROCm 官方文档 / devices.md（快照，引用前核实） |

---

## 规格与本地 LLM 能力（公开快照）

| 型号 | 系列 | 显存 | 参考价（USD） | 本地 LLM 能力 |
|------|------|------|------------|-------------|
| **RX 7900 XTX** | RDNA 3 | 24GB GDDR6 | $800–900 | ⭐⭐⭐⭐⭐ 消费级最大显存，单卡 70B Q4 |
| **Radeon PRO W7900** | RDNA 3（工作站）| 48GB GDDR6 | $3,500+ | ⭐⭐⭐⭐⭐ 48GB 舒适跑 70B，显存党 |
| Radeon AI PRO R9700（语境）| RDNA 4（工作站）| 32GB | ~$1,300 | ⭐⭐⭐⭐ 新一代 AI 工作站卡 |
| **RX 9070 XT** | RDNA 4 | 16GB GDDR6 | $600–800 | ⭐⭐⭐⭐ 30B Q4，性价比标杆（16GB 上限）|
| RX 9070（语境）| RDNA 4 | 16GB | $550+ | ⭐⭐⭐⭐ 同上 |

> **口径**：24GB 是本地 AI 入场券、48GB 才舒适跑 70B（70B Q4_K_M 约需 40–43GB）。RX 9070 XT 等 16GB 卡上限约 30B Q4，不入"70B 可用层"。
> **性能对比谨慎**：[olares-one-benchmarks.md](/Users/pengpeng/seo/directions/hardware/research/olares-one-benchmarks.md) 是 Olares One 的 **NVIDIA（RTX 5090 Mobile 24GB）** 第一方实测，**不含 Radeon dGPU**；本报告不把 NVIDIA 数字安到 AMD 上，只作"CUDA 路线已被验证"的旁证。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。搜索量为美国月均。

### 型号词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| rx 9070 xt | 33,100 | 46 | $0.23 | 信息/导航 | RDNA4 主力型号词，量最大 |
| 7900 xtx | 14,800 | 54 | $0.20 | 信息/导航 | 简写大词 |
| rx 9070 | 14,800 | 41 | $0.21 | 信息/导航 | |
| rx 7900 xtx | 8,100 | 48 | $0.22 | 信息 | 消费旗舰全称 |
| radeon rx 9070 xt | 8,100 | 52 | $0.26 | 导航 | |
| rx 7900 xt | 4,400 | 46 | $0.22 | 信息 | 语境型号 |
| radeon 9070 xt | 3,600 | 41 | $0.26 | 导航 | |
| radeon rx 7900 xtx | 2,400 | 54 | $0.28 | 导航 | |
| radeon 7900 xtx | 1,300 | 52 | $0.24 | 信息 | |
| ⭐ rx 9070 xt price | 1,300 | 40→ | $0.23 | 交易 | KD40，购买意图强 |
| radeon ai pro r9700 | 720 | 34 | $0.93 | 信息 | RDNA4 AI 工作站卡 |
| ⭐ rx 7900 xtx price | 480 | **25** | $0.22 | 交易 | KD25 购买词 |
| amd radeon ai pro r9700 | 480 | 40 | $0.44 | 信息 | |
| ⭐ amd radeon pro | 390 | **28** | $0.67 | 信息/导航 | 工作站品类词 |
| radeon pro w7900 | 320 | 32 | $0.53 | 信息 | 48GB 工作站旗舰 |
| rx 9070 xt review | 320 | 45 | $0.37 | 导航 | |
| ⭐ amd radeon pro w7900 | 260 | **28** | $1.06 | 信息/交易 | 工作站买家，高 CPC |
| w7900 | 210 | 37 | $0.62 | 信息 | |
| 7900 xtx 24gb | 110 | 44 | $0.32 | 信息 | 显存卖点词 |
| ⭐ pro w7900 | 70 | **27** | $1.47 | 信息/交易 | 高 CPC 工作站词 |

### 品类 / 选卡词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| best gpu for ai | 720 | 30 | $2.02 | 商业 | 大品类词，高 CPC |
| amd instinct | 590 | 54 | $3.27 | 信息 | 数据中心加速卡（语境）|
| amd instinct mi300x | 320 | 35 | $3.48 | 信息 | |
| amd ai gpu | 260 | 39 | $1.18 | 导航 | |
| ⭐ 48gb gpu | 170 | **13** | $0.65 | 信息 | 显存党入口，KD13 |
| amd gpu for ai | 140 | 37 | $1.51 | 信息 | |
| amd 24gb gpu | 140 | 39 | $0.21 | 信息 | |
| ⭐ best gpu for local llm | 110 | **15** | $1.86 | 商业 | KD15 高价值选卡词 |
| ⭐ amd stable diffusion | 90 | **29** | $0 | 信息 | |
| ⭐ best gpu for stable diffusion | 90 | **14** | $0 | 商业 | KD14 |
| ⭐ gpu for llm | 70 | **25** | $2.97 | 商业 | 高 CPC |
| ⭐ local llm gpu | 50 | **30**→ | $1.92 | 信息 | |
| amd egpu | 140 | 26 | $0.29 | 信息 | ⭐ 外接显卡场景 |

### ROCm / 软件栈词（AMD 生态信号）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| rocm | 3,600 | 47 | $8.87 | 信息 | 软件栈大词，CPC 极高 |
| amd rocm | 1,000 | 50 | $4.52 | 信息 | |
| ⭐ rocm vs cuda | 320 | **23** | $0 | 信息/导航 | 路线之争核心词，KD23 |
| rocm windows | 320 | 40 | $0 | 信息 | ROCm on Windows 痛点 |
| what is rocm | 170 | 33 | $0 | 信息 | 科普问题词 |
| rocm pytorch | 140 | 47 | $0 | 信息 | |
| ⭐ rocm vllm | 110 | **30**→ | $0 | 信息 | vLLM on AMD，新兴 |
| stable diffusion amd | 210 | 38 | $0 | 信息 | |
| ollama amd | 170 | 39 | $0 | 信息/导航 | Ollama on AMD |
| pytorch amd | 110 | 39 | $0 | 信息 | |
| rocm linux | 70 | 40 | $0 | 导航 | |
| rocm docker | 50 | 43 | $0 | 信息/交易 | |
| amd gpu machine learning | 40 | 45 | $5.21 | 信息 | 高 CPC |
| is rocm open source | 40 | 51 | $0 | 信息 | |

### 对比 / 替代词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ⭐ 9070 xt vs 5070 ti | 5,400 | **22** | $1.27 | 导航 | 量大 KD22（偏游戏对比）|
| ⭐ 7900 xtx vs 4090 | 590 | **27** | $0 | 信息/导航 | AMD vs NVIDIA 旗舰对决 |
| ⭐ rx 9070 xt vs 7900 xtx | 480 | **25** | $0 | 信息/导航 | 自家新旧对比 |
| ⭐ rx 7900 xtx vs rtx 4090 | 390 | **21** | $0 | 信息/导航 | KD21 |
| ⭐ 7900 xtx vs 3090 | 260 | **10** | $0 | 信息/导航 | KD10 极低 |
| ⭐ 7900 xtx vs 5090 | 170 | **10** | $0 | 信息/导航 | KD10 极低 |
| ⭐ is the 9070 xt better than the 7900 xtx | 50 | **11** | $0 | 信息 | 问题词，KD11 |
| best amd gpu for ai | 20 | 0 | $1.73 | 信息 | 近零竞争，精准 |
| best amd gpu for llm | 20 | 0 | $0 | 信息 | 近零竞争 |
| amd vs nvidia llm | 20 | 0 | $0 | 信息 | 路线选择长尾 |
| w7900 vs a6000 | 20 | 0 | $0 | 信息 | 工作站对比 |

### 本地部署长尾（近零量，GEO 前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| amd gpu llm | 30 | 0 | $0 | 信息 | 核心场景词，零竞争 |
| run llm on amd gpu | 30 | 0 | $0 | 信息 | 教程意图 |
| rocm ollama | 30 | 0 | $0 | 信息/交易 | 部署组合词 |
| 7900 xtx llm | 20 | 0 | $0 | 信息 | 型号+场景 |
| 9070 xt llm / 9070 xt ai / 9070 xt ollama | 各 20 | 0 | $0 | 信息 | RDNA4+AI 前哨 |
| amd gpu for stable diffusion | 20 | 0 | $0 | 信息 | |
| amd gpu inference | 20 | 0 | $0 | 信息 | |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑（组四 dGPU：A+B 并重）：对"选卡/对比"词打信息 A——Olares One（NVIDIA CUDA 全验证 + Olares OS 全栈 + 第一方 benchmark 背书）省去 ROCm 折腾，$3,999 整机 TCO；对"我已有 AMD 卡"词打信息 B（本组重点）——Olares 已支持 AMD/ROCm 加速，装 Olares 把闲置 Radeon 变成随处可用的私有 AI 云。诚实边界：AMD 卡本身有性价比，ROCm 生态不及 CUDA，如实写。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| ⭐⭐ rocm vs cuda | 320 | 23 | $0 | **信息 A**：路线之争加第三视角——"不想在 ROCm/CUDA 上折腾软件栈？" Olares One 走 CUDA 全验证路径开箱即用；诚实点出 AMD 卡的性价比 |
| ⭐⭐⭐ best gpu for local llm | 110 | 15 | $1.86 | **信息 A**：选卡指南把 Olares One 作"整机方案"选项——买卡不如买整机省心，24GB 独显 + Olares OS 全栈 |
| ⭐⭐ 7900 xtx vs 4090 | 590 | 27 | $0 | **信息 A**：旗舰对决加"整机视角"——两卡都要自己配软件栈，Olares One 出厂即私有 AI OS |
| ⭐⭐ ollama amd | 170 | 39 | $0 | **信息 B（重点）**：教"在 AMD/Radeon 上跑 Ollama"，落到 Olares 经 ROCm 一键加速——已有卡直接盘活 |
| ⭐⭐ stable diffusion amd | 210 | 38 | $0 | **信息 B**：AMD 出图教程 → 装 Olares（Market 一键 ComfyUI/SD），诚实标注 CUDA-first 应用覆盖边界 |
| ⭐⭐ rocm ollama / amd gpu llm / run llm on amd gpu | 各 30 | 0 | $0 | **信息 B**：零竞争核心场景词——"AMD 也能跑本地大模型"，Olares ROCm 加速部署，AMD 用户最强 Olares 角度 |
| ⭐ rocm vllm | 110 | 30 | $0 | **信息 B**：vLLM on AMD 新兴词，Olares 承接高并发本地推理 |
| ⭐ amd radeon pro w7900 | 260 | 28 | $1.06 | **信息 B**：48GB 工作站卡买家——装 Olares 把 W7900 变 7×24 私有 AI 服务器 |
| ⭐ 7900 xtx vs 3090 / vs 5090 | 260/170 | 10/10 | $0 | **信息 A**：KD10 对比文加 Olares One 第三选项 |
| ⭐ best amd gpu for ai / best amd gpu for llm | 各 20 | 0 | $1.73 | **信息 A+B**：近零竞争选卡词，诚实推荐 AMD 卡的同时给"Olares 让它开箱即用"角度 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| rx 9070 xt price | 1,300 | 40 | $0.23 | trans | 次级 | RDNA4 购买意图词，整机 TCO 对比引流 |
| best gpu for ai | 720 | 30 | $2.02 | comm | 次级 | 高 CPC 品类导购，Olares One 作"整机即答案"选项 |
| 7900 xtx vs 4090 | 590 | 27 | $0 | info | 主词候选 | 信息 A：AMD vs NVIDIA 旗舰对决，两卡都要自配软件栈，Olares One 出厂即私有 AI OS |
| rx 7900 xtx price | 480 | 25 | $0.22 | trans | 主词候选 | 大显存卡购买词→整机 TCO 对比；W7900 买家装 Olares 变私有 AI 服务器（信息 B）|
| rx 9070 xt vs 7900 xtx | 480 | 25 | $0 | info | 次级 | 自家新旧对比，并入对决簇加 Olares One 第三选项 |
| rx 7900 xtx vs rtx 4090 | 390 | 21 | $0 | info | 次级 | KD21 对决，整机视角 + Olares 部署收口 |
| rocm vs cuda | 320 | 23 | $0 | info | 主词候选 | 信息 A：路线之争 + 第三视角"不想折腾软件栈就上 Olares One（CUDA 全验证）"，诚实点 AMD 性价比 |
| amd radeon pro w7900 | 260 | 28 | $1.06 | info | 次级 | 信息 B：48GB 工作站卡买家装 Olares 变 7×24 私有 AI 服务器 |
| 7900 xtx vs 3090 | 260 | 10 | $0 | info | 次级 | KD10 极低对决文，加 Olares One 第三选项 |
| stable diffusion amd | 210 | 38 | $0 | info | 主词候选 | 信息 B：AMD 出图 → Olares Market 一键 SD/ComfyUI，诚实标 CUDA-first 覆盖边界 |
| ollama amd | 170 | 39 | $0 | info | 主词候选 | 信息 B 重点：教 AMD/Radeon 跑 Ollama，落到 Olares 经 ROCm 一键加速盘活已有卡 |
| 48gb gpu | 170 | 13 | $0.65 | info | 次级 | KD13 显存党入口，48GB 舒适跑 70B |
| best gpu for local llm | 110 | 15 | $1.86 | comm | 主词候选 | 信息 A：选卡指南把 Olares One 作整机方案——买卡不如买整机省心，24GB 独显 + 全栈 |
| amd gpu llm | 30 | 0 | $0 | info | GEO | 零竞争核心场景"AMD 也能跑本地大模型 on Olares（ROCm 加速）" |
| best amd gpu for ai | 20 | 0 | $1.73 | info | GEO | 近零竞争选卡词，诚实推荐 AMD 卡的同时给"Olares 让它开箱即用"角度 |

---

## 核心洞见

1. **品牌护城河**：AMD 型号词（rx 9070 xt 33,100、7900 xtx 14,800）流量大但 KD 41–54，是 AMD 官网/评测媒体的地盘，正面刚不划算；**真正可打的是"型号 + AI/LLM/对比"长尾**——那里 KD 断崖式下降（多数 KD 0–30）。

2. **可复制的打法**：型号对比词是金矿——7900 xtx vs 3090（KD10）、vs 5090（KD10）、rx 7900 xtx vs rtx 4090（KD21）、rocm vs cuda（KD23）都是量 200–600、竞争极低的对决词。用"对比文 + 第三选项（Olares One / 装 Olares）"模板批量铺，是最高 ROI 的可复制打法。

3. **对 Olares 最关键的 2–3 个词**：① **best gpu for local llm（110/KD15）**——高价值选卡词，信息 A 收口；② **rocm vs cuda（320/KD23）**——路线之争，AMD 用户最痛的软件栈焦虑，Olares 正好给答案；③ **ollama amd / rocm ollama / amd gpu llm（合计~230，KD 0–39）**——信息 B 重点，"AMD 也能跑本地大模型 on Olares"是 AMD 用户最强的 Olares 角度。

4. **最大攻击面**：**ROCm 生态成熟度 + Windows 支持痛点**——rocm windows（320）、what is rocm（170）、is rocm open source（40）、大量 "how to install rocm" 问题词，说明 AMD 用户在软件栈配置上大量卡壳。内容诚实承认 ROCm 不及 CUDA，同时给"Olares 帮你把 AMD 卡直接变可用私有 AI"的解法，是精准攻击面。

5. **隐藏低 KD 金矿**：48gb gpu（170/**KD13**）、best gpu for stable diffusion（90/**KD14**）、best gpu for local llm（110/**KD15**）、7900 xtx vs 3090 / vs 5090（**KD10**）、is the 9070 xt better than the 7900 xtx（50/**KD11**）——量不大但 KD 极低，选卡/对比意图强，可快速排名。

6. **GEO 前瞻布局**：amd gpu llm、run llm on amd gpu、rocm ollama、7900 xtx llm、9070 xt ai/ollama、amd gpu inference（均 20–30/mo，**KD 0**）——近零竞争的"AMD 本地 AI"场景词，是抢 AI Overview / Perplexity 引用位的窗口。RDNA4（9070 xt）+ AI 组合词几乎无内容，先发即占。

7. **与既有分析的关联**：补充 [olares-500-keywords](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md) 的"本地 LLM 选卡/GPU"族——本报告新增 AMD/ROCm 一整条差异化支线（NVIDIA 内容已多，AMD 侧几乎空白），与同目录 [rtx-4090](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/nvidia/rtx-4090.md)、[intel-arc](/Users/pengpeng/seo/directions/hardware/reports/04-dgpu/intel/intel-arc.md) 构成"三家 dGPU 本地 AI"矩阵，可互链做"本地 LLM 选卡全指南"聚合页。

---

*数据来源：SEMrush US 数据库（keyword_research → phrase_these、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。规格/价格为公开快照，引用前以官网/ROCm 文档核实。*
