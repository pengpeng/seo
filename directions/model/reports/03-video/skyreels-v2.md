# SkyReels-V2 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：SkyworkAI（昆仑万维）/ skyreels.ai，许可证待 repo 核实（Wan 衍生，基底 Apache 2.0）

## 模型理解（前置）

SkyReels-V2 是首个开源的**无限长视频生成模型**，由昆仑万维（SkyworkAI）基于阿里 Wan 2.1 架构构建，支持 t2v（文生视频）与 i2v（图生视频），核心差异是可连续生成不受固定秒数限制的长视频。提供 1.3B 与 14B 两档，1.3B 可在消费级 GPU 上本地运行；官网 skyreels.ai 同时承载 SkyReels-A3（人像动画）等多个产品，品牌已建立一定的搜索心智。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源无限长视频生成模型（t2v + i2v），基于 Wan 2.1 架构 |
| 许可证 | 待 repo 核实（Wan 2.1 基底为 Apache 2.0；SkyReels-V2 repo 标注"Wan 衍生"）|
| 主仓库 / 分发 | GitHub：github.com/SkyworkAI/SkyReels-V2；HuggingFace：SkyworkAI/SkyReels-V2；ComfyUI 节点已出现 |
| 参数 / VRAM 可跑性 | 1.3B（约 8–12GB VRAM，消费级可跑，**Olares One 24GB 足够**）；14B（约 28GB+ bf16，Olares One 可跑 fp8/量化变体）|
| 变体 / 型号 | V2-1.3B（t2v / i2v）、V2-14B（高质量长视频）；v1 为前代 |
| 闭源对标 | Kling（快影 AI）/ Runway Gen-3 / Sora（长视频场景） |
| Olares Market | ComfyUI（Olares Market 已上架）可作为引擎承载；vLLM 不适用（视频扩散模型）|
| 来源 | GitHub SkyworkAI/SkyReels-V2、HuggingFace 模型卡、skyreels.ai 官网、搜索数据 `skyreels-a3` / `skyreels comfyui` |

---

## 流量基线（Phase 1）

skyreels.ai 是官方产品站，承载 SkyReels-V2、SkyReels-A3（人像动画）等多个模型产品。

| 指标 | 数据 |
|------|------|
| 域名 | skyreels.ai |
| SEMrush Rank | 241,538 |
| 月自然流量（US） | 7,098 |
| 关键词数 | 105 |
| 流量估值 | $6,282 / 月 |
| 付费关键词 | 4 个，215 流量 |

### 官网 TOP 关键词（流量前 10，按流量排序）

| 关键词 | 排名 | 月量 | KD | 流量 | URL |
|--------|------|------|----|------|-----|
| skyreels | 1 | 3,600 | 53 | 2,880 | skyreels.ai |
| skyreels ai | 1 | 1,900 | 59 | 1,520 | skyreels.ai |
| sky reels | 1 | 720 | 40 | 576 | skyreels.ai |
| skyreels-a3 | 1 | 1,300 | 59 | 322 | skyreels.ai |
| skyreel | 1 | 320 | 44 | 256 | skyreels.ai |
| skyreels-ai | 1 | 880 | 35 | 218 | skyreels.ai |
| skyreelsai | 1 | 210 | 37 | 168 | skyreels.ai |
| skyreels.ai | 1 | 210 | 60 | 168 | skyreels.ai |
| skyreels ia | 1 | 590 | 37 | 146 | skyreels.ai |
| sky reels ai | 1 | 170 | 40 | 136 | skyreels.ai |

**注：** `skyreels-a3`（人像动画模型，月量 1,300）与 `skyreels v2` 共享域名流量，需在洞见中区分产品归属；V2 专属词（`skyreels v2` / `skyreels-v2`）合计约 1,310 月量，不含品牌泛词。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| skyreels v2 | 720 | 38 | $0.76 | 信息 |
| skyreels-v2 | 590 | 33 | $0.76 | 导航 |
| skyreels v1 | 140 | 48 | $0.79 | 信息/导航 |
| skyreels v3 | 140 | 0 | $1.22 | — |
| skyreels v4 | 110 | 47 | $1.25 | 信息/商业 |
| skyreels-v3 | 110 | 33 | $1.65 | 信息 |
| skyreels-v4 | 110 | 49 | $1.25 | 信息/导航 |
| skyreels a3 | 110 | 37 | $0.75 | 信息/导航 |
| skyreel v2 | 90 | 43 | $0.97 | 信息 |
| skyreels i2v | 40 | 41 | $0.00 | 信息 |
| skyreels ai video generator | 40 | 36 | $1.31 | 信息 |
| what is skyreels | 50 | 36 | $0.00 | 信息 |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| skyreels huggingface | 210 | 39 | $0.00 | 信息/导航 |
| skyreels comfyui ⭐ | 110 | 24 | $0.00 | 信息/商业 |
| skyreels lora ⭐ | 70 | 24 | $0.75 | 信息/导航 |
| skyreels-a2 ⭐ | 70 | 25 | $0.00 | 信息 |
| skyreels-v1 ⭐ | 70 | 28 | $0.79 | 信息/导航 |
| skyreels github | 20 | — | $0.00 | 导航 |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| local ai video generator ⭐ | 390 | 26 | $1.43 | 信息 |
| ai video generator local ⭐ | 140 | 22 | $2.15 | 信息/导航 |
| open source ai video ⭐ | 40 | 24 | $1.23 | 信息 |
| open source video generation ⭐ | 30 | 24 | $1.65 | 信息 |
| video generation local | 30 | 0 | $0.00 | — |
| local video generation ai | 20 | 0 | $1.55 | 信息/导航 |
| ai video generator self hosted | 20 | 0 | $0.00 | — |
| skyreels open source | 0 | — | — | — |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| wan 2.1 | 6,600 | 55 | $0.86 | 信息 |
| wan video generation | 170 | 71 | $1.10 | 信息 |
| kling ai alternative ⭐⭐⭐ | 170 | 5 | $1.76 | 信息 |
| wan video model | 170 | 75 | $1.25 | 信息 |
| wan 2.2 video | 110 | 52 | $0.87 | 信息 |
| open source sora ⭐ | 50 | 23 | $0.00 | 信息 |
| runway ml alternative ⭐ | 40 | 10 | $2.61 | 信息 |
| open source video generator ⭐ | 20 | — | $1.20 | — |
| kling alternative | 20 | 0 | $2.31 | — |
| sora alternative open source | 20 | 0 | $2.34 | — |
| long form video ai | 10 | 0 | $3.09 | — |
| infinite video generation ai | 0 | — | — | — |
| long video generation open source | 0 | — | — | — |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| skyreels comfyui | 110 | 24 | $0.00 | ComfyUI 是 Olares Market 已上架引擎，SkyReels-V2 1.3B 通过 ComfyUI 节点一键本地跑 | ⭐⭐⭐ |
| local ai video generator | 390 | 26 | $1.43 | 主打"本地视频生成无云端账单"——Olares One 24GB 足够跑 1.3B，内容创作者告别 Kling 按秒计费 | ⭐⭐⭐ |
| ai video generator local | 140 | 22 | $2.15 | 同上，KD 最低（22），CPC 高（$2.15），商业价值强 | ⭐⭐⭐ |
| kling ai alternative | 170 | 5 | $1.76 | KD 仅 5 的超低竞争词；SkyReels-V2 开源 + 本地部署对比 Kling 云端按秒计费是核心攻击点 | ⭐⭐⭐ |
| open source sora | 50 | 23 | $0.00 | SkyReels-V2 是最接近"开源 Sora"定位的长视频模型；Olares 本地跑无隐私风险 | ⭐⭐ |
| runway ml alternative | 40 | 10 | $2.61 | KD 10，信息意图，内容机会；Runway 按分钟收费，SkyReels-V2 本地无限生成 | ⭐⭐ |
| open source ai video | 40 | 24 | $1.23 | 宽泛发现词，Olares 内容覆盖"本地跑开源视频生成模型"全品类入口 | ⭐⭐ |
| open source video generation | 30 | 24 | $1.65 | 同上，信息意图，适合 GEO 内容覆盖 | ⭐⭐ |
| skyreels huggingface | 210 | 39 | $0.00 | 部署导向词，用户正在找下载/运行路径；Olares 可做"HuggingFace 模型一键本地"叙事 | ⭐⭐ |
| wan 2.1 | 6,600 | 55 | $0.86 | SkyReels-V2 基于 Wan 2.1；高流量入口词，KD 55 竞争激烈，但可通过"SkyReels-V2 vs Wan 2.1"切入 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断 |
|--------|------|----|----|------|------|-----------|
| skyreels | 3,600 | 44 | $0.79 | 导航 | 主词候选 | 品牌总词，官网已占#1；适合品牌介绍页 / Olares 安装教程锚点 |
| skyreels v2 | 720 | 38 | $0.76 | 信息 | 主词候选 | V2 专属词月量 720，KD 38，SEO 难度中等，Olares 部署文章主词 |
| skyreels ai | 1,900 | 56 | $0.65 | 导航 | 主词候选 | 月量大但 KD 56，以导航流量为主，官网竞争激烈；可作辅助 |
| local ai video generator | 390 | 26 | $1.43 | 信息 | 主词候选 | KD 26、CPC $1.43，量足，Olares 主攻"本地视频生成"的最佳入口词 |
| kling ai alternative | 170 | 5 | $1.76 | 信息 | 主词候选 | KD 仅 5，月量 170，是目前竞品词里机会最大的；直接攻击 Kling 计费痛点 |
| skyreels comfyui | 110 | 24 | $0.00 | 信息/商业 | 次级 | KD 24，月量 110；ComfyUI 引擎词，Olares Market 一键部署路径直接打通 |
| ai video generator local | 140 | 22 | $2.15 | 信息/导航 | 次级 | KD 22 最低竞争，CPC $2.15 商业价值高；适合"本地 AI 视频生成器"教程页 |
| skyreels huggingface | 210 | 39 | $0.00 | 信息/导航 | 次级 | 部署路径词，月量 210；用户在找下载方式，Olares 可截获 |
| wan 2.1 | 6,600 | 55 | $0.86 | 信息 | 次级 | 母架构词量巨大；KD 55 正面攻击难，作为 SkyReels-V2 技术背景词引流 |
| open source sora | 50 | 23 | $0.00 | 信息 | GEO 前哨 | KD 23，量 50；"开源 Sora"认知词，SkyReels-V2 是最接近此定位的本地可运行模型 |
| runway ml alternative | 40 | 10 | $2.61 | 信息 | GEO 前哨 | KD 10，量小但 CPC 高（$2.61）；Runway 付费用户痛点词，本地替代叙事强 |
| open source ai video | 40 | 24 | $1.23 | 信息 | GEO 前哨 | KD 24，宽泛品类词；适合 AI Overview / Perplexity 抢发，覆盖开源视频生成全品类 |
| skyreels-v2 | 590 | 33 | $0.76 | 导航 | GEO 前哨 | 带连字符变体，月量 590，KD 33；与 `skyreels v2` 合并覆盖 1,310 月量 |
| skyreels lora | 70 | 24 | $0.75 | 信息 | GEO 前哨 | KD 24，LoRA 微调需求词；进阶用户细分，Olares 本地微调叙事切入点 |
| infinite video generation ai | 0 | — | — | — | GEO 前哨 | 近零量但与 SkyReels-V2 核心卖点完全吻合；GEO 抢发（AI Overview/Perplexity）定义词 |
| long video generation open source | 0 | — | — | — | GEO 前哨 | 同上，语义精准；写入技术文 front-matter 可抢早期引用位 |

---

## 核心洞见

1. **搜索心智已建立，V2 专属词有稳健量级**：`skyreels`（3,600）/ `skyreels ai`（1,900）等品牌总词月量充足，官网已占据 #1。V2 专属词（`skyreels v2` + `skyreels-v2`）合计约 1,310 月量，是写 Olares 部署文的稳固锚词。注意官网同时承载 SkyReels-A3（人像动画，月量 1,300），需区分产品 — A3 是闭源云服务，V2 才是开源可本地跑的模型。

2. **消费级 GPU 可跑，Olares One 满足 1.3B 足额运行**：V2-1.3B 约需 8–12GB VRAM，Olares One RTX 5090 Mobile 24GB 游刃有余；V2-14B 以 fp8 量化可在 24GB 边缘运行。"无限长视频 + 本地 + 不限制秒数"是核心叙事，对 Kling 按秒计费的攻击面极强。

3. **许可证建议先核实 repo**：Wan 2.1 基底为 Apache 2.0，SkyReels-V2 若沿用则商用友好、可主推；若有附加条款（Skywork 系部分产品限制地区商用），建议降调为"技术文覆盖"而非"商用替代方案"主推词。

4. **Olares 最关键的 3 个词**：① `kling ai alternative`（KD 5，月量 170，竞争极低，直接打 Kling 计费痛点）；② `local ai video generator`（KD 26，月量 390，消费级本地部署最直接入口）；③ `skyreels comfyui`（KD 24，月量 110，ComfyUI 是 Olares Market 已上架引擎，一键部署故事最短路径）。

5. **新词 GEO 抢发窗口**：`infinite video generation ai`、`long video generation open source`、`skyreels open source`、`skyreels wan` 当前近零量，但语义与 SkyReels-V2 核心卖点高度吻合。在技术文、对比文的 front-matter 和正文首段写入这些词，可提前占领 AI Overview / Perplexity 引用位——这类词通常在模型被大量引用后量级爆发，先发内容获得最大红利。

6. **闭源对标与攻击面**：Kling（按秒计费，约 $0.14–0.35/秒）与 Runway Gen-3（按 credit 限额）是主要攻击对象。核心角度：SkyReels-V2 本地运行无每秒云账单、数据不出设备、无时长上限——一次性硬件成本（Olares One $3,999）对 重度内容创作者更优于长期订阅。`runway ml alternative`（KD 10，$2.61 CPC）显示 Runway 用户在主动寻找替代，转化意图强。

7. **与同类 family 的关联**：Wan 2.1 是 SkyReels-V2 的上游架构（月量 6,600，但 KD 55），可在内容中做"SkyReels-V2 = Wan 架构的无限视频进化版"定位，借助 Wan 的搜索热度做内容关联。参考 [wan-2.md](/Users/pengpeng/seo/directions/model/reports/03-video/wan-2.md) 报告，共享"开源视频生成"品类叙事但差异化在"长视频/无限时长"专项。

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch、resource_organic、domain_rank）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
*注：skyreels.ai 官网同时承载 V2（开源模型）与 A3（闭源云服务）等多产品，域名总流量含多个产品线。*
