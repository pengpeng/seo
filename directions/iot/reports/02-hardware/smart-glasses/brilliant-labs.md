# Brilliant Labs Frame / Halo SEO 竞品分析报告

> 域名：brilliant.xyz | SEMrush US | 2026-07-06
> 全球唯一量产、开源（ISC / CERN OHL-P）AI 眼镜平台；Frame（2024）→ Halo（2025）迭代，面向开发者与隐私优先用户。

---

## 项目理解（前置）

Brilliant Labs 是加拿大硬件创业公司，旗下两代开源 AI 眼镜：**Frame**（2024，单目 OLED + 720p 相机，Lua SDK）和**Halo**（2025，彩色 microLED + Alif B1 NPU，ZephyrOS，板载 AI 推理）。核心差异化是**全开源**——固件、SDK、硬件图纸（CERN OHL-P）全部公开，任何人可 fork、二次开发，并通过 Noa AI 伴侣 App 接云端或本地 AI。对 Olares 的关联：Frame/Halo 通过 Python SDK 连接手机/服务器侧 AI 推理——**Olares 跑 Ollama → 成为 Brilliant Labs 眼镜的本地 LLM 后端**，实现私有化、零云依赖的 AI 眼镜完整方案。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 AI 眼镜开发平台：Frame（开发者）+ Halo（日常+开发） |
| 开源 / 许可证 | 是；固件 ISC License，硬件 CERN OHL-P（Permissive）；SDK MIT |
| 主仓库 | [github.com/brilliantlabsAR/frame-codebase](https://github.com/brilliantlabsAR/frame-codebase)（★ 488）；[brilliantlabsAR/noa-flutter](https://github.com/brilliantlabsAR/noa-flutter)（★ 82） |
| 核心功能 | ① 单目 HUD 显示（~20° FOV）；② 720p / VGA 相机；③ Noa AI 伴侣（多模态对话/记忆）；④ Lua / Python SDK 可完全自定义 AI 管线；⑤ Halo 含板载 NPU（Alif B1） |
| 商业模式 / 定价 | 一次性硬件购买，Frame $349，Halo $349（含 Noa App 免费基础功能）；Noa Pro 订阅（细节未公开） |
| 差异化 / 价值主张 | **唯一量产+全开源**的 AI 眼镜；可替换 AI 后端（接 OpenAI / 本地 Ollama 均可）；支持处方镜片；最轻量级开发者 AI 眼镜（~40g） |
| 主要竞品（初判） | Meta Ray-Ban（消费端量最大）、Even Realities G2（显示+消费）、Solos AirGo（运动开发）、XRAI Glass（无障碍字幕） |
| Olares Market | 未上架（硬件产品，SDK 为开源 Python/Flutter 库） |
| 来源 | [brilliant.xyz](https://brilliant.xyz/)、[docs.brilliant.xyz](https://docs.brilliant.xyz/frame/hardware/)、[github.com/brilliantlabsAR](https://github.com/brilliantlabsAR/)、[reality-atlas.com/blog/brilliant-labs-frame-review](https://www.reality-atlas.com/blog/brilliant-labs-frame-review) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | brilliant.xyz |
| SEMrush Rank | 364,051 |
| 自然关键词数 | 395 |
| 月自然流量（US）| 4,300 |
| 自然流量估值 | $8,996 / 月 |
| 付费关键词数 | 2 |
| 月付费流量 | 1 |
| 排名 1–3 位 | 53 词 |
| 排名 4–10 位 | 54 词 |
| 排名 11–20 位 | 85 词 |

**洞察**：流量高度集中在品牌词（约 93%）；付费几乎为零——Brilliant Labs 完全靠自然搜索和口碑；流量虽不大，但品牌词 KD 普遍低（18–39），说明护城河是**认知壁垒而非 SEO 竞争**。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| brilliant.xyz | 381 | 4,291 | 99.8% |
| docs.brilliant.xyz | 11 | 9 | 0.2% |
| repl.brilliant.xyz | 3 | 0 | 0% |

**洞察**：文档站几乎无搜索流量——开发者内容严重未被 SEO 利用，是绕过品牌词的切入机会（教程/SDK 教程词）。

### 官网 TOP 自然关键词（按流量降序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| brilliant labs frame | 1 | 1,000 | 37 | $1.85 | 800 | 商业 | brilliant.xyz/ |
| brilliant labs | 1 | 720 | 68 | $5.88 | 576 | 品牌 | brilliant.xyz/ |
| brilliant labs frame: | 1 | 590 | 36 | $1.85 | 472 | 品牌 | brilliant.xyz/ |
| brilliant labs halo | 1 | 590 | 28 | $2.20 | 472 | 商业 | /products/halo |
| halo glasses | 1 | 1,300 | 40 | $0.51 | 322 | 信息 | /products/halo |
| brilliant labs ai glasses | 1 | 210 | 39 | $1.39 | 168 | 商业 | brilliant.xyz/ |
| brilliant labs frame ai glasses | 1 | 170 | 29 | $1.62 | 136 | 商业 | brilliant.xyz/ |
| brilliant labs glasses | 1 | 110 | 22 | $1.19 | 88 | 商业 | brilliant.xyz/ |
| brilliant labs frames | 1 | 110 | 37 | $1.85 | 88 | 品牌 | brilliant.xyz/ |
| brilliant labs monocle | 1 | 110 | 21 | $1.47 | 88 | 信息 | brilliant.xyz/ |
| halo monocle | 1 | 320 | 22 | $0.00 | 79 | 信息 | brilliant.xyz/ |
| ai glasses | 12 | 49,500 | 36 | $0.69 | 74 | 信息 | brilliant.xyz/ |
| halo smart glasses | 1 | 260 | 16 | $1.59 | 64 | 信息 | /products/halo |
| halo x glasses | 1 | 260 | 48 | $0.51 | 64 | 信息 | /products/halo |
| frame ar glasses | 1 | 70 | 50 | $0.00 | 56 | 信息 | brilliant.xyz/ |
| brilliant labs smart glasses | 1 | 50 | 34 | $1.46 | 40 | 商业 | brilliant.xyz/ |
| open source smart glasses | 1 | 260 | 52 | $0.98 | 34 | 信息 | brilliant.xyz/ |
| halo ai glasses | 1 | 140 | 28 | $1.46 | 34 | 信息 | /products/halo |
| frame ai glasses | 1 | 140 | 51 | $1.09 | 34 | 信息 | brilliant.xyz/ |
| open source ar glasses | 1 | 110 | 50 | $1.05 | 27 | 信息 | brilliant.xyz/ |
| open source ai glasses | 2 | 110 | 43 | $1.29 | 14 | 信息 | brilliant.xyz/ |

**关键发现**："ai glasses"（49,500 月量，KD 36）当前排名第 12——这是全站最大的非品牌流量词，KD 仅 36 却对应 4.9 万月量，如果能爬进前 3 将带来 10× 流量放大。

### 付费词（Google Ads，按流量排序）

Brilliant Labs 几乎不投 Google Ads——仅 2 个付费关键词（均围绕"halo ai glasses"类）、月付费流量估计 1 次。**完全依赖自然流量和口碑**，说明 SEO 内容是其唯一流量杠杆。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| even realities g1 / g2 | 4,400 | 50 | $1.02 | 信息/商业 | 最近竞品，有 HUD 显示 |
| even g2 glasses | 2,900 | 38 | $1.31 | 信息 | ⭐ KD 近门槛，量大 |
| solos airgo | 260 | 18 | $0.30 | 商业 | ⭐ KD 低，开发者导向 |
| meta ray ban alternative | 70 | 13 | $0.60 | 信息 | ⭐ 低 KD，比较意图强 |
| ray ban smart glasses alternative | 20 | — | $0.46 | 信息 | GEO |
| omi glasses | 170 | 28 | $1.30 | 信息/商业 | ⭐ 低 KD AI 眼镜竞品 |
| jarvis glasses | 170 | 19 | $1.54 | 信息 | ⭐ 低 KD，幻想型品类词 |
| oracle glasses | 170 | 7 | $1.23 | 信息 | ⭐⭐ 极低 KD |
| kira glasses | 210 | 4 | $0.79 | 信息 | ⭐⭐ 极低 KD，新 AI 眼镜品牌 |
| project aria | 880 | 34 | $2.26 | 信息/商业 | Meta 开发者 AR 项目 |
| mentra | 1,900 | 42 | $0.11 | 商业 | AI 眼镜新兴品牌 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| smart glasses | 110,000 | 86 | $0.67 | 信息 | 太难，KD 86 |
| ai glasses | 40,500 | 36 | $0.69 | 信息 | 当前排 12，最大机会词 |
| ai smart glasses | 3,600 | 49 | $0.62 | 信息/商业 | 中等 KD |
| smart glasses with display | 5,400 | 61 | $0.66 | 信息/商业 | 高 KD |
| best smart glasses | 5,400 | 61 | $0.67 | 信息 | 高 KD |
| best ai glasses 2025 | 1,300 | 48 | $1.00 | 信息 | 年度选购词 |
| ar glasses | 18,100 | 67 | $0.80 | 信息 | 太难 |
| wearable ai | 720 | 42 | $1.25 | 信息 | 品类新词 |
| smart glasses hud | 210 | 32 | $0.57 | 信息 | ⭐ 低 KD，Frame 精准词 |
| ai powered glasses | 320 | 49 | $0.83 | 信息 | 中等 |
| open source smart glasses | 210 | 51 | $1.08 | 信息 | Frame 所属类目 |
| open source ar glasses | 110 | 50 | $1.33 | 信息 | Frame 所属类目 |
| open source ai glasses | 110 | 43 | $1.29 | 信息 | 同上，KD 略低 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| brilliant labs frame | 1,000 | 37 | $1.85 | 商业 | 核心品牌词 |
| brilliant labs halo | 590 | 28 | $2.20 | 商业 | 新品品牌词 |
| brilliant labs ai glasses | 210 | 39 | $1.39 | 商业 | |
| brilliant labs frame ai glasses | 170 | 29 | $1.62 | 商业 | ⭐ |
| halo smart glasses | 260 | 16 | $1.59 | 信息 | ⭐ 极低 KD |
| halo ai glasses | 140 | 28 | $1.46 | 信息 | ⭐ |
| frame ai glasses | 140 | 51 | $1.09 | 信息 | |
| what are ai glasses | 2,400 | 56 | $0.40 | 信息 | 教育型高量词 |
| what do ai glasses do | 880 | 39 | $0.51 | 信息 | ⭐ 可接 |
| how do ai glasses work | 260 | 20 | $0.50 | 信息 | ⭐ 低 KD 教程词 |
| are ai glasses worth it | 110 | 43 | $0.48 | 信息 | 选购意图 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| local llm | 2,900 | 39 | $5.37 | 信息 | ⭐ 核心连接词 |
| private ai | 1,900 | 29 | $3.58 | 信息 | ⭐ 低 KD，高价值 |
| local ai | 1,900 | 49 | $3.38 | 信息 | |
| self hosted llm | 320 | 22 | $3.12 | 信息 | ⭐ 低 KD |
| run ai locally | 210 | 35 | $4.67 | 信息 | |
| self-hosted ai | 90 | 30 | $5.26 | 信息 | ⭐ KD 低 CPC 高 |
| open source ai assistant | 170 | 49 | $3.26 | 信息 | |
| personal ai assistant | 1,900 | 44 | $3.04 | 信息/商业 | |

---

## Olares 关联词（Phase 3）

**核心叙事切入**：Frame / Halo 的 Python SDK 允许开发者将任意 AI 后端连接到眼镜——Olares 在本地跑 Ollama，向眼镜提供私有、零延迟、无订阅的 LLM 推理。这是目前**唯一**可以同时做到"开源眼镜 + 开源 OS + 本地 LLM"的完整方案，Olares 的内容角度是**后端基础设施提供者**，而非眼镜本身。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|------------|--------|
| ai glasses | 40,500 | 36 | $0.69 | 解释"为什么本地 AI > 云 AI"：Frame + Ollama on Olares = 私有化 AI 眼镜完整方案，无订阅无隐私泄露 | ⭐⭐⭐ |
| local llm | 2,900 | 39 | $5.37 | Olares 跑 Ollama → 成为 Frame 的本地推理后端；高 CPC 说明商业意图强 | ⭐⭐⭐ |
| private ai | 1,900 | 29 | $3.58 | Frame/Halo + Olares = "truly private AI on your face"：数据不出家门 | ⭐⭐⭐ |
| open source smart glasses | 210 | 51 | $1.08 | 对比 Ray-Ban Meta 闭源：Frame/Halo + Olares 全栈开源，从眼镜到 OS 到 LLM | ⭐⭐⭐ |
| wearable ai | 720 | 42 | $1.25 | Olares 作为 AI Agent 运行平台，Frame 成为 Agent 的感知终端（眼+耳） | ⭐⭐⭐ |
| self hosted llm | 320 | 22 | $3.12 | "Self-host your AI glasses backend on Olares"；低 KD 高 CPC，直接机会词 | ⭐⭐⭐ |
| how do ai glasses work | 260 | 20 | $0.50 | 教程文：解释 Frame → Noa → LLM 管线，演示如何接入 Ollama on Olares | ⭐⭐⭐ |
| personal ai assistant | 1,900 | 44 | $3.04 | Olares 叙事核心词：Personal Agent；Frame 是其感知输入设备 | ⭐⭐ |
| self-hosted ai | 90 | 30 | $5.26 | 低量但高 CPC、低 KD，精准自托管用户；Frame 作为客户端 | ⭐⭐⭐ |
| smart glasses hud | 210 | 32 | $0.57 | 解释 HUD + AI 助手组合，引出本地 LLM 方案（Olares）的隐私优势 | ⭐⭐ |
| solos airgo | 260 | 18 | $0.30 | "Frame vs Solos AirGo"对比文：Frame 更开源，后接 Olares local AI 更强 | ⭐⭐ |
| meta ray ban alternative | 70 | 13 | $0.60 | 极低 KD；Frame 作为 Ray-Ban 对应的开源替代，Olares 提供本地 AI 后端 | ⭐⭐⭐ |
| run ai locally | 210 | 35 | $4.67 | 教程词："Run AI locally for your smart glasses"（Frame + Olares + Ollama） | ⭐⭐⭐ |
| brilliant labs frame ollama | 0 | — | — | GEO 前哨：尚无搜索量，但是 Frame 开发者圈高度精准的下一步搜索词 | ⭐⭐⭐ GEO |
| brilliant labs halo ollama | 0 | — | — | 同上，针对 Halo 新品 | ⭐⭐⭐ GEO |
| open source ai glasses backend | 0 | — | — | GEO：Olares 作为开源眼镜的 AI 计算后端 | ⭐⭐ GEO |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| ai glasses | 40,500 | 36 | $0.69 | 信息 | **主词候选** | KD 36 vs 4 万月量是全报告最大价值词；Frame/Halo 已排 12，Olares 内容可补充"本地 AI 眼镜"叙事以抢前 5 |
| local llm | 2,900 | 39 | $5.37 | 信息 | **主词候选** | CPC $5.37 说明强商业意图；Olares + Frame 组合的核心技术词，可做"local LLM for smart glasses"文 |
| private ai | 1,900 | 29 | $3.58 | 信息 | **主词候选** | KD 低（29）量大（1,900），Frame+Olares 组合的核心叙事词；自然契合隐私 AI 定位 |
| wearable ai | 720 | 42 | $1.25 | 信息 | **主词候选** | 品类新词，现在入场 KD 可管控；Olares 做 Agent OS，Frame 做感知终端 |
| self hosted llm | 320 | 22 | $3.12 | 信息 | **主词候选** | KD 22 是低竞争金矿；CPC $3.12 商业意图强；可与 Olares + Ollama 教程结合 |
| best ai glasses 2025 | 1,300 | 48 | $1.00 | 信息 | **主词候选** | 年度选购词；Olares 可以做圆桌评测文，重点突出 Frame/Halo 开源+本地 AI 差异化 |
| how do ai glasses work | 260 | 20 | $0.50 | 信息 | **主词候选** | KD 20 极低；教程意图，Olares 可做"Frame SDK + Ollama"完整教程文 |
| meta ray ban alternative | 70 | 13 | $0.60 | 信息 | **主词候选** | KD 13 极低；比较意图明确；Frame/Halo 作为开源替代，Olares 提供 AI 后端优势 |
| self-hosted ai | 90 | 30 | $5.26 | 信息 | **次级** | 量小但高 CPC（$5.26）精准用户；并入 self hosted llm 文章 |
| solos airgo | 260 | 18 | $0.30 | 商业 | **次级** | 低 KD 竞品对比；并入 Frame vs 竞品对比文 |
| open source ai glasses | 110 | 43 | $1.29 | 信息 | **次级** | Frame 所属精准品类，并入 ai glasses 文章 |
| smart glasses hud | 210 | 32 | $0.57 | 信息 | **次级** | 对显示场景感兴趣的用户；并入品类科普文 |
| oracle glasses | 170 | 7 | $1.23 | 信息 | **次级** | KD 7 超低，幻想型 AI 眼镜词，引流价值大；并入 AI 眼镜对比文 |
| kira glasses | 210 | 4 | $0.79 | 信息 | **次级** | KD 4 最低，新兴品牌；并入 AI 眼镜对比文 |
| run ai locally | 210 | 35 | $4.67 | 信息 | **次级** | 高 CPC 精准词；并入 local llm 教程文 |
| brilliant labs frame ollama | 0 | — | — | — | **GEO** | 精准开发者词；Frame SDK + Ollama on Olares 教程的目标词 |
| brilliant labs halo ollama | 0 | — | — | — | **GEO** | 同上，Halo 版 |
| open source ai glasses backend | 0 | — | — | — | **GEO** | Olares 定位为"眼镜 AI 后端" |
| frame glasses local ai | 0 | — | — | — | **GEO** | Frame 本地 AI 方案；抢 AI Overview 引用位 |

---

## 核心洞见

1. **品牌护城河**：brilliant.xyz 在所有品牌词上牢牢占据第 1，且品牌词 KD 普遍在 20–40（非 Meta 级别壁垒）。可以正面刚**对比文**（"Frame vs Even Realities"、"Frame vs Meta Ray-Ban"），因为 Brilliant Labs 的竞争关键字 KD 整体低。但不要做品牌词流量争夺——他们排 1 无法抢。

2. **可复制的打法**：Brilliant Labs 完全依赖自然流量，**不做程序化页面也不投广告**。缺口在：① 没有做"vs 竞品"对比页面（KD 13 的 "meta ray ban alternative" 无人认真做）；② docs.brilliant.xyz 文档站几乎没有 SEO 流量——教程型内容机会巨大；③ "how do ai glasses work"（KD 20）这种教育词无人用资源认真做。

3. **对 Olares 最关键的 3 个词**：
   - **`self hosted llm`**（320/月，KD 22，CPC $3.12）——Olares 的直接定位词，Frame 是其端侧客户端，可做"Self-host your AI glasses with Olares + Ollama + Frame"教程，两个场景同时覆盖。
   - **`private ai`**（1,900/月，KD 29，CPC $3.58）——Frame 的隐私叙事与 Olares 的"Own your AI"高度共鸣，可做 "Private AI glasses: Frame + Olares" 对比云端 AI 的隐私优势。
   - **`meta ray ban alternative`**（70/月，KD 13）——极低 KD，Frame 作为开源替代切入；Olares 在此增加差异化一列：无订阅、本地 LLM、完全开放。

4. **最大攻击面**：Meta Ray-Ban 的最大痛点是**云端 AI 依赖**（所有请求走 Meta 服务器）+ **封闭平台**（不可二次开发）。这正好对应 Frame/Halo + Olares 的组合优势。围绕"ray ban meta privacy concerns"、"meta ray ban no display"、"meta ai glasses data privacy" 这类高意图词做内容有机会。

5. **隐藏低 KD 金矿**：
   - `oracle glasses`（170/月，KD 7）：极低竞争，幻想型 AI 眼镜词，Frame 内容中嵌入可获得意外流量。
   - `kira glasses`（210/月，KD 4）：某新兴品牌，KD 近零；在 AI 眼镜对比文中提及 + 引流。
   - `meta ray ban alternative`（70/月，KD 13）：没有人用专页认真做，直接机会。
   - `how do ai glasses work`（260/月，KD 20）：教育词，Frame SDK/Ollama 教程可占据此词。
   - `self hosted llm`（320/月，KD 22）：Olares 核心词，Frame 是其最好的硬件实例。

6. **GEO 前瞻布局**（近零量、语义精准，抢 AI Overview / Perplexity 引用位）：
   - `brilliant labs frame ollama` / `brilliant labs halo ollama`：Frame 开发者圈的下一步搜索，Olares 教程文先占位。
   - `open source ai glasses local inference`：随 NPU 眼镜普及，本地推理将成为下一波选购关键词。
   - `ai glasses no subscription`：对比 Meta AI / Noa Pro 订阅，Frame + Olares 本地跑零月费。
   - `wearable personal ai agent`：Olares 的长期叙事词（Agent-Native OS），Frame 是其感知端。

7. **与既有 olares-500-keywords 的关联**：`local llm`（2,900）、`private ai`（1,900）、`self hosted llm`（320）与 Olares 核心自托管/隐私 AI 主题高度重叠，可将 Frame/Halo 内容作为**具体硬件场景案例**嵌入已规划的 Ollama / local LLM 相关文章，双向引流——既让 Olares 内容补充眼镜场景，也让眼镜用户发现 Olares。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、resource_adwords、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
