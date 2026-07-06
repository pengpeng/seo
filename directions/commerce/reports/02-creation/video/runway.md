# Runway SEO 竞品分析报告

> 域名：runwayml.com | SEMrush us | 2026-07-06
> Runway = AI 视频/图像/音频生成平台，"generative video" 品类的头部商业玩家（Gen-4.5 世界模型 + 企业影视管线）。

---

## 项目理解（前置）

Runway（公司 Runway，域名 runwayml.com）是 2018 年成立于纽约的 AI 视频生成公司，靠 Gen 系列视频模型（Gen-2 → Gen-3 Alpha → Gen-4 → **Gen-4.5**）起家，把"文字/图片 → 可编辑的电影级镜头"做成了一个完整的创作平台，并向"世界模型（world models）"叙事升级。目前估值 **$5.3B**、累计融资约 $860M（2026-02 由 General Atlantic 领投的 $315M E 轮，NVIDIA / AMD Ventures / Adobe 战略入股），Q2 2026 单季新增 ~$40M ARR，营收主要来自 Lionsgate / AMC 等**企业影视客户**而非消费订阅。它是**闭源 SaaS**，按**credits 计费**——这正是 Olares 平替叙事的最大攻击面。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 闭源 AI 视频/图像/音频生成平台，Gen-4.5 为旗舰视频模型 |
| 开源 / 许可证 | ❌ 闭源商业 SaaS（无自托管） |
| 主仓库 | 无公开模型权重；早年 `runwayml/stable-diffusion` 属历史项目，非现行产品 |
| 核心功能 | 文生视频 / 图生视频（Gen-4.5、Gen-4、Gen-4 Turbo）、视频编辑（Aleph）、表演捕捉（Act-Two）、生成图像/音频（TTS）、4K 上采 |
| 商业模式 / 定价 | 免费 125 一次性 credits；Standard $15/mo（625 credits）；Pro $35/mo（2,250）；Unlimited/Max $95/mo（9,500 + Explore Mode）；Enterprise 定制。Gen-4.5 ≈ 25 credits/秒（top-up ≈ $0.25/秒） |
| 差异化 / 价值主张 | 影视级画质 + 完整编辑管线 + Act-Two 表演捕捉 + 企业合规（SSO/合规/工作区分析）；Gen-4.5 在第三方基准超过 Google/OpenAI 视频模型 |
| 主要竞品（初判）| Sora（OpenAI）、Google Veo 3、Kling、Luma、Pika；开源侧 Wan / HunyuanVideo |
| Olares Market | Runway 本体闭源、不可上架；**平替路径 = ComfyUI（✅ 已上架）内跑 Wan 2.2 / HunyuanVideo** |
| 来源 | runwayml.com/pricing、TechCrunch 2026-05-15、PitchBook/融资公告 |

**Olares 平替（本次对象）：** **Wan**（阿里通义万相，开源，2.1/2.2/2.5 系列）、**HunyuanVideo**（腾讯混元视频，开源）——两者都能在本地独显上跑，Olares Market 里的 **ComfyUI** 就是承载它们的运行时。

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | runwayml.com |
| SEMrush Rank | 8,715 |
| 自然关键词数 | 9,319 |
| 月自然流量（US）| 265,318 |
| 自然流量估值 | **$530,076/月** |
| 付费关键词数 | 815 |
| 月付费流量 | 27,815 |
| 付费流量成本 | $57,108/月 |
| 排名 1-3 位 | 1,000 词 |
| 排名 4-10 位 | 529 词 |
| 排名 11-20 位 | 692 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| runwayml.com（主站）| 4,836 | 250,768 | 94.52% |
| app.runwayml.com | 800 | 6,246 | 2.35% |
| help.runwayml.com | 2,452 | 5,797 | 2.18% |
| docs.dev.runwayml.com | 236 | 967 | 0.36% |
| play.runwayml.com | 37 | 612 | 0.23% |
| academy.runwayml.com | 707 | 508 | 0.19% |
| aif.runwayml.com | 84 | 402 | 0.15% |

> 流量高度集中在主站首页，几乎全靠**品牌词 + 品牌误拼变体**撑起，产品/研究页（/research、/product、/pricing）为辅。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| runway | 1 | 90,500 | 92 | $2.14 | 72,400 | 品牌 | / |
| runway ai | 1 | 33,100 | 55 | $2.21 | 26,480 | 品牌 | / |
| runway ml | 1 | 18,100 | 81 | $1.92 | 14,480 | 品牌 | / |
| runwayml | 1 | 14,800 | 79 | $1.92 | 11,840 | 品牌 | / |
| runaway（误拼！）| 1 | 40,500 | 68 | $1.32 | 10,044 | 信息 | / |
| renwaymi（误拼）| 1 | 6,600 | 86 | $2.14 | 5,280 | 品牌 | / |
| runaway ai（误拼）| 1 | 6,600 | 59 | $2.21 | 5,280 | 品牌 | / |
| runway ml news | 1 | 6,600 | 64 | $0.00 | 5,280 | 信息 | /news |
| runway gen-3 | 1 | 5,400 | 49 | $2.88 | 4,320 | 信息 | /research/…gen-3-alpha |
| runway gen-2 | 1 | 4,400 | 52 | $2.16 | 3,520 | 信息 | /research/gen-2 |
| runway gen-4 | 1 | 4,400 | 43 | $3.10 | 3,520 | 信息 | /research/…gen-4 |
| runawayml（误拼）| 1 | 3,600 | 81 | $1.92 | 2,880 | 品牌 | / |
| runwayml.com | 1 | 2,900 | 83 | $1.55 | 2,320 | 品牌 | / |
| runway.ai | 1 | 2,400 | 71 | $2.21 | 1,920 | 品牌 | / |
| runway ai video | 1 | 2,400 | 69 | $3.08 | 1,920 | 信息 | / |
| runway pricing | 1 | 2,400 | 37 | $2.40 | 1,920 | 商业 | /pricing |
| runway video generator | 1 | 1,900 | 63 | $3.43 | 1,520 | 信息 | / |
| runway gen 4.5 | 1 | 1,900 | 41 | $3.39 | 1,520 | 信息 | /research/…gen-4.5 |
| runway ai video maker | 1 | 1,900 | 60 | $2.23 | 1,520 | 信息 | / |
| runway ml pricing | 1 | 1,900 | 38 | $2.07 | 1,520 | 商业 | /pricing |
| runaway gen 3（误拼）| 1 | 1,300 | 41 | $2.88 | 1,040 | 信息 | /research/…gen-3-alpha |
| runway act 2 | 1 | 1,000 | 38 | $1.91 | 800 | 信息 | help.runwayml.com/…Act-Two |
| runway gen 4 | 1 | 2,900 | 31 | $3.10 | 719 | 信息 | /research/…gen-4 |
| runway pricing plans | 1 | 720 | 29 | $2.76 | 576 | 商业 | /pricing |
| runway ai image to video | 1 | 720 | 63 | $1.48 | 576 | 信息 | /product |
| runway aleph | 1 | 1,600 | 28 | $1.82 | 396 | 信息 | /en |

> 其余大量长尾为品牌误拼变体（runwaylm/runwwayml/ranway/runwa/run way ml…），几乎全部排名第 1。**品牌词 + 误拼词 = 绝大部分自然流量**，通用品类词自然排名很少。

### 付费词（Google Ads，按流量排序）

Runway **付费在买竞品品牌大词与品类超级词**，几乎全部导向 `/product`（少量导向 `/product/seedance`、`/product/aleph-2`）：

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| runway | 1 | 90,500 | $2.14 | /product |
| sora ai | 3 | 201,000 | $0.76 | /product |
| runway ai | 1 | 33,100 | $2.21 | /product |
| topaz | 2 | 90,500 | $0.74 | /product/aleph-2 |
| google veo 3 | 3 | 90,500 | $8.47 | /product |
| heygen | 6 | 90,500 | $1.38 | /product |
| invideo | 2 | 33,100 | $1.62 | /product |
| ai video generation | 1 | 6,600 | $1.71 | /product |
| seedance ai | 1 | 4,400 | $1.49 | /product/seedance |
| best ai video generator | 2 | 14,800 | $2.55 | /product |

> 打法：**用 Ads 抢竞品品牌词（sora / topaz / heygen / invideo / veo）+ 品类大词**，统一导向 `/product` 产品页——典型的"买对手心智 + 品类流量"策略。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| sora alternative | 210 | **11** | $1.09 | 商业 | ⭐ 邻近品类，KD 极低 |
| runway vs kling | 90 | **11** | $2.58 | 对比 | ⭐ |
| sora vs runway | 90 | 27 | $3.47 | 对比 | ⭐ |
| runway alternatives | 50 | **10** | $3.39 | 商业 | ⭐ |
| runway vs sora | 50 | **14** | $0.00 | 对比 | ⭐ |
| runway ml alternative | 40 | **10** | $2.61 | 商业 | ⭐ |
| veo alternative | 30 | **3** | $1.61 | 商业 | ⭐ |
| alternative to runway | 20 | 0 | $0.00 | 商业 | ⭐ |
| free runway alternative | 20 | 0 | $0.91 | 商业 | ⭐ |
| runway vs pika / veo / luma | 20 | 0 | $0.00 | 对比 | ⭐ 新兴 |
| pika vs runway | 20 | 0 | $0.00 | 对比 | ⭐ |
| kling alternative | 20 | 0 | $2.31 | 商业 | ⭐ |
| runway alternative | 10 | 0 | $3.39 | 商业 | ⭐ 主词量太小 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai video generator | 165,000 | 92 | $1.27 | 信息 | 品类超级词，打不动 |
| free ai video generator | 74,000 | 83 | $1.12 | 商业 | |
| ai video generator free | 49,500 | 79 | $1.03 | 信息 | |
| image to video ai | 27,100 | 67 | $0.80 | 信息 | |
| ai video maker | 27,100 | 92 | $1.08 | 信息 | |
| ai video editor | 27,100 | 76 | $2.02 | 商业 | |
| best ai video generator | 14,800 | 69 | $2.55 | 信息 | |
| image to video | 14,800 | 67 | $0.83 | 信息 | |
| ai video generation models | 14,800 | 52 | $2.64 | 信息 | |
| best free ai video generator | 8,100 | 81 | $1.24 | 信息 | |
| text to video ai | 8,100 | 78 | $1.35 | 信息 | |
| ai video generation | 6,600 | 85 | $1.71 | 信息 | |
| text to video | 5,400 | 77 | $1.37 | 信息 | |
| text to video generator | 3,600 | 77 | $1.60 | 信息 | |
| free ai video generator no watermark | 1,300 | 63 | $1.14 | 商业 | 痛点词 |
| ai video generator no sign up | 1,300 | 56 | $0.37 | 导航 | 痛点词 |
| free unlimited ai video generator | 590 | 67 | $1.05 | 商业 | 痛点词 |
| unlimited ai video generator | 480 | 64 | $1.34 | 商业 | 痛点词 |
| text to video api | 110 | **30** | $2.74 | 信息 | ⭐ |

### 产品 / 功能词（runway 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| runway pricing | 2,400 | 37 | $2.98 | 商业 | 最大定价词 |
| runway ml pricing | 2,400 | 37 | $2.58 | 商业 | |
| runway aleph | 1,600 | 28 | $1.82 | 信息 | ⭐ 视频编辑功能 |
| runway pricing plans | 720 | 29 | $2.76 | 商业 | ⭐ |
| runway app | 590 | 63 | $1.91 | 导航 | |
| runway login | 480 | 32 | $2.61 | 导航 | |
| runway api | 480 | 49 | $7.33 | 商业 | 高 CPC |
| runway ai free | 320 | 53 | $1.09 | 商业 | |
| runway act two | 320 | 38 | $1.78 | 信息 | 表演捕捉 |
| runway gen 4.5 | 260 | 33 | $2.49 | 信息 | 旗舰模型 |
| runway api key | 210 | 44 | $4.44 | 信息 | 高 CPC |
| runway free trial | 170 | **27** | $2.51 | 信息 | ⭐ |
| runway free | 140 | 60 | $1.08 | 商业 | |
| is runway free | 110 | 50 | $1.52 | 信息 | 定价痛点 |
| runway cost | 110 | 35 | $2.05 | 商业 | |
| runway student | 40 | **16** | $0.00 | 商业 | ⭐ |
| runway credits | 20 | 0 | $0.00 | 信息 | ⭐ 计费痛点 |
| runway enterprise | 20 | 0 | $0.00 | 企业 | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| wan 2.2 | 14,800 | 61 | $0.78 | 信息 | 🔥 开源平替旗舰型号词 |
| wan 2.1 | 6,600 | 55 | $0.86 | 信息 | 🔥 |
| wan 2.5 | 3,600 | **31** | $1.12 | 信息 | ⭐ KD 相对低 |
| wan video | 3,600 | 74 | $0.72 | 品牌 | |
| hunyuan video | 2,900 | 61 | $0.81 | 信息 | 🔥 腾讯混元视频 |
| wan2.1 comfyui | 1,900 | 45 | $0.00 | 信息 | ComfyUI 运行时 |
| hunyuanvideo | 1,900 | 61 | $0.81 | 信息 | |
| wan ai video | 880 | 63 | $0.99 | 品牌 | |
| open source ai video generator | 590 | 35 | $1.19 | 信息 | 直搜"开源" |
| wan 2.2 comfyui | 390 | 55 | $0.93 | 信息 | |
| local ai video generator | 390 | **26** | $1.43 | 信息 | ⭐ |
| hunyuan video comfyui | 260 | 32 | $0.00 | 信息 | |
| wan video generator | 260 | 64 | $0.94 | 信息 | |
| comfyui wan | 210 | **29** | $0.00 | 信息 | ⭐ Market 已有 ComfyUI |
| wan 2.2 install | 170 | 33 | $0.00 | 信息 | |
| wan 2.2 local | 170 | 32 | $2.58 | 信息 | |
| open source sora | 50 | 23 | $0.00 | 信息 | ⭐ |
| self hosted ai video generator | 40 | 46 | $1.29 | 信息 | |
| hunyuan video local | 40 | **27** | $0.00 | 信息 | ⭐ |
| local text to video | 40 | **27** | $0.00 | 信息 | ⭐ |
| open source image to video | 40 | 31 | $0.76 | 信息 | |
| open source video generation | 30 | **24** | $1.65 | 信息 | ⭐ |
| ai video generator open source | 30 | **15** | $1.40 | 信息 | ⭐ |
| ai video generator without credits | 30 | 49 | $1.46 | 信息 | 计费痛点 |
| video generation model open source | 20 | 0 | $2.70 | 信息 | ⭐ GEO |
| self hosted video ai | 20 | 0 | $0.00 | 信息 | ⭐ GEO |
| local video generation | 20 | 0 | $2.50 | 信息 | ⭐ GEO |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Runway 闭源 + 按 credits 计费（Gen-4.5 ≈ 25 credits/秒 ≈ $0.25/秒）+ 有水印/额度/需登录；Olares 上装 ComfyUI（Market 已上架），用本地 24GB 独显（Olares One = RTX 5090 Mobile 24GB）跑开源的 Wan 2.2 / HunyuanVideo——不烧 credits、无额度、无水印、数据不出机。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| wan 2.2 | 14,800 | 61 | $0.72 | ⭐⭐⭐ 型号大词：在 Olares 的 ComfyUI 里本地跑 Wan 2.2，24GB 独显足够、零 credits |
| wan 2.1 | 6,600 | 55 | $0.86 | ⭐⭐⭐ 同上，覆盖上一代仍在搜的用户 |
| wan 2.5 | 3,600 | 31 | $1.12 | ⭐⭐⭐ KD 相对低，"本地跑 Wan 2.5"教程截量 |
| hunyuan video | 2,900 | 61 | $0.81 | ⭐⭐⭐ 第二条平替线：Olares 本地跑 HunyuanVideo |
| runway pricing | 2,400 | 37 | $2.98 | ⭐⭐⭐ 定价对比：Runway $15–95/mo + 按秒烧 credits vs Wan on Olares 零边际成本 |
| wan2.1 comfyui | 1,900 | 45 | $0.00 | ⭐⭐ ComfyUI = Olares Market 已上架，直接给"在 Olares 一键装 ComfyUI 跑 Wan"路径 |
| hunyuanvideo | 1,900 | 61 | $0.81 | ⭐⭐ 同 hunyuan video |
| open source ai video generator | 590 | 35 | $1.19 | ⭐⭐⭐ 用户直搜"开源视频生成"，Olares 承接部署落点 |
| local ai video generator | 390 | 26 | $1.43 | ⭐⭐⭐ 低 KD，本地视频生成正是 Olares One 卖点 |
| wan 2.2 comfyui | 390 | 55 | $0.93 | ⭐⭐ 教程词 |
| comfyui wan | 210 | 29 | $0.00 | ⭐⭐ 低 KD + Market 直接机会 |
| sora alternative | 210 | 11 | $1.09 | ⭐⭐ KD11！开源本地方案作为 Sora/Runway 之外的第三选项 |
| wan 2.2 local | 170 | 32 | $2.58 | ⭐⭐⭐ "本地跑 Wan 2.2"意图 100% 契合 Olares |
| text to video api | 110 | 30 | $2.74 | ⭐⭐ Olares 本地文生视频 API：无密钥、无额度、CPC $2.74 商业价值高 |
| runway vs sora | 50 | 14 | $0.00 | ⭐⭐ KD14 三方对比：Runway vs Sora vs 本地开源（Wan/Hunyuan on Olares）|
| runway alternatives | 50 | 10 | $3.39 | ⭐⭐ 低 KD 替代词，收编到"开源自托管 Runway 替代"清单 |
| hunyuan video local | 40 | 27 | $0.00 | ⭐⭐ GEO 精准词 |
| ai video generator without credits | 30 | 49 | $1.46 | ⭐⭐⭐ 直击 credits 痛点，Olares 本地零 credits |
| ai video generator open source | 30 | 15 | $1.40 | ⭐⭐ 低 KD GEO |
| open source video generation | 30 | 24 | $1.65 | ⭐⭐ 低 KD GEO |
| self hosted video ai | 20 | 0 | $0.00 | ⭐⭐⭐ 语义完美契合，GEO 占位 |

**推荐内容方向：** ①"Runway 太贵/烧 credits？在自己的机器上本地跑 Wan 2.2（Olares + ComfyUI 完整指南）"；②"Runway vs Sora vs 开源本地（Wan / HunyuanVideo）三方对比"；③"How to run Wan 2.2 / HunyuanVideo locally on your own GPU（无水印、无额度）"。

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| wan 2.2 | 14,800 | 61 | $0.72 | 信息 | 主词候选 | 开源平替旗舰型号词，撑"本地跑 Wan 2.2（Olares + ComfyUI）"主文 |
| wan 2.1 | 6,600 | 55 | $0.86 | 信息 | 主词候选 | 上一代型号词，并入 Wan 系列主文 |
| wan 2.5 | 3,600 | 31 | $1.12 | 信息 | 主词候选 | KD 相对低，最值得单独攻的 Wan 型号词 |
| hunyuan video | 2,900 | 61 | $0.81 | 信息 | 主词候选 | 第二条平替线，"本地跑 HunyuanVideo"主文 |
| runway pricing | 2,400 | 37 | $2.98 | 商业 | 主词候选 | 最大定价词，定价对比文核心：credits vs 本地零成本 |
| open source ai video generator | 590 | 35 | $1.19 | 信息 | 主词候选 | 品类"开源"词，Olares 承接部署落点 |
| local ai video generator | 390 | 26 | $1.43 | 信息 | 主词候选 | 低 KD + 意图 100% 契合本地生成 |
| sora alternative | 210 | 11 | $1.09 | 商业 | 主词候选 | KD11，开源本地方案作第三选项 |
| text to video api | 110 | 30 | $2.74 | 信息 | 主词候选 | 本地文生视频 API：无密钥/无额度，商业价值高 |
| comfyui wan | 210 | 29 | $0.00 | 信息 | 次级 | Market 已有 ComfyUI，教程词直接承接 |
| wan 2.2 local | 170 | 32 | $2.58 | 信息 | 次级 | "本地跑 Wan 2.2"，并入 Wan 主文 |
| runway vs sora | 50 | 14 | $0.00 | 对比 | 次级 | KD14 三方对比切入点 |
| runway alternatives | 50 | 10 | $3.39 | 商业 | 次级 | 低 KD 替代词，收编替代清单 |
| runway ml alternative | 40 | 10 | $2.61 | 商业 | 次级 | 同上 |
| runway vs kling | 90 | 11 | $2.58 | 对比 | 次级 | 低 KD 对比词，可挂三方对比 |
| runway free trial | 170 | 27 | $2.51 | 信息 | 次级 | 定价痛点词，导向"免费/本地"论点 |
| ai video generator without credits | 30 | 49 | $1.46 | 信息 | GEO | 直击 credits 痛点，语义完美契合 |
| ai video generator open source | 30 | 15 | $1.40 | 信息 | GEO | 低 KD 近零量，抢引用位 |
| open source video generation | 30 | 24 | $1.65 | 信息 | GEO | 同上 |
| hunyuan video local | 40 | 27 | $0.00 | 信息 | GEO | 精准本地部署意图，GEO 占位 |
| self hosted video ai | 20 | 0 | $0.00 | 信息 | GEO | 近零量语义完美契合 Olares |

---

## 核心洞见

1. **品牌护城河极深，正面刚品牌词无胜算。** SEMrush Rank 8,715、自然流量估值 $530K/月，自然流量的绝大部分来自 `runway`（90,500）等品牌词及**海量误拼变体**——尤其 `runaway`（40,500/mo，误拼）单词就带来 ~1 万流量，`renwaymi/runwaylm/runwwayml` 等误拼词全部霸榜第 1。这类心智护城河 Olares 无法也不必去抢。

2. **可复制的打法 = "买竞品品牌词 + 品类超级词 → 统一导向 /product"。** Runway 用 Google Ads 抢 `sora ai`（201K）、`topaz`、`heygen`、`invideo`、`google veo 3`（$8.47 CPC）等对手品牌词与品类大词，几乎全部导向 `/product`。Olares 侧无需买词，但可复制"以对比页承接竞品/品类流量"的结构——为每个开源平替（Wan / HunyuanVideo）做 "X on Olares / X vs Runway" 落地页矩阵。

3. **对 Olares 最关键的 2–3 个词：`wan 2.2`（14,800）、`hunyuan video`（2,900）、`runway pricing`（2,400, KD37）。** 前两者是开源平替的**型号大词**——真实且高涨的"本地跑开源视频模型"需求，且 CPC 极低（$0.7–0.8）说明还没被商业玩家吃透；`runway pricing` 则是把这批人从 Runway 拉走的**定价攻击面**。三者共同支撑"Runway 太贵 → 在 Olares 上用 ComfyUI 本地跑 Wan 2.2 / HunyuanVideo"的主线内容。

4. **最大攻击面 = credits 计费 + 水印/额度/需登录。** `is runway free`（110）、`runway credits`、`runway free`（140）、`ai video generator without credits`（30, 意图极准）、`free ai video generator no watermark`（1,300）、`ai video generator no sign up`（1,300）、`free/unlimited ai video generator`（480–590）密集出现——用户对 Runway 的**按秒烧 credits（Gen-4.5 ≈ $0.25/秒）**高度敏感。Olares 叙事应直击："本地独显跑 Wan/HunyuanVideo = 不烧 credits、无额度、无水印、无需登录、数据不出机"。

5. **隐藏低 KD 金矿：`wan 2.5`（3,600, KD31）、`comfyui wan`（210, KD29）、`local ai video generator`（390, KD26）、`sora alternative`（210, KD11）、`runway vs kling`（90, KD11）、`runway alternatives`（50, KD10）。** 型号/对比/本地部署词 KD 普遍远低于品类大词（`ai video generator` KD92 打不动），是低成本切入点；其中 `comfyui wan` 直接对应 Olares Market 已上架的 ComfyUI，转化路径最短。

6. **GEO 前瞻布局：** `self hosted video ai`（KD0）、`local video generation`（KD0）、`video generation model open source`（KD0）、`ai video generator open source`（KD15）、`hunyuan video local`（KD27）、`open source video generation`（KD24）目前近零量，但语义与 Olares 完美契合。提前发布权威内容占位，抢 AI Overview / Perplexity 的引用位。

7. **诚实边界（沿用旧报告判断）：** `runway act two`（320）揭示 Runway 在往**表演捕捉 / AI 演员**方向深化，这是当前开源本地视频模型（Wan/HunyuanVideo）暂时落后的能力。Olares 内容应诚实说明本地方案在**极致画质与专业编辑管线**上的局限，把定位放在"性价比 + 隐私 + 无额度的自托管替代"，以建立可信度而非硬碰画质。

8. **与既有 `olares-500-keywords` 词表的关联：** 本报告的"开源本地视频生成（Wan / HunyuanVideo + ComfyUI 运行时）"叙事与 500 词表中「本地 AI 生成 / ComfyUI」类高度互补，建议将 `wan 2.2 / wan 2.5 / hunyuan video` 等型号词与 `runway pricing / sora alternative` 等攻击面词补入词表的"AI 视频生成"子品类。

---

*数据来源：SEMrush us 数据库（domain_rank / domain_organic_subdomains / resource_organic / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
