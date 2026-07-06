# Calendly SEO 竞品分析报告

> 域名：calendly.com | SEMrush US | 2026-07-06
> Calendly = 日程自动化/会议预约 SaaS 市场领导者，ARR 约 $270M+，以"分享可预约链接"消灭邮件往返

---

## 项目理解（前置）

Calendly 创立于 2013 年，核心产品是一条可共享的预约链接：收件人点开看到发件人的真实空闲时间，选定时段后双方日历自动生成邀请、发送提醒。这套自动化把"找时间"从多轮邮件压缩为一次点击，以极强的病毒式传播（每次发出链接即带来新用户注册）驱动 PLG 增长，仅融资 $55 万即达 $60M ARR。2021 年完成 $350M B 轮融资，估值 $3B，Sacra 估计 2023 年底 ARR 已达 $270M。

产品为**纯闭源 SaaS**，无法自托管。Olares 平替路径：**Cal.diy**（calcom/cal.diy GitHub 仓库，MIT 许可，约 46K ⭐），这是 Cal.com 去掉企业版商业代码后的完全开源社区版，可自部署在 Olares 上。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 日程自动化 SaaS，让用户用一条链接代替所有"找时间"邮件 |
| 开源 / 许可证 | **闭源 SaaS**（无开源版） |
| 主仓库 | 无（私有代码库）|
| 核心功能 | 可分享预约链接、多历日历同步、自动提醒与后续邮件、轮询排班（Teams）、Salesforce/HubSpot 路由（Teams+）|
| 商业模式 / 定价 | Free（1 事件类型）→ Standard $10/seat/mo → Teams $16/seat/mo → Enterprise $15K/yr+ |
| 差异化 / 价值主张 | 极简预约体验 + 强 CRM/ATS/MAP 集成 + Fortune 500 内深度 PLG 渗透（86% F500 公司有用户）|
| 主要竞品（初判）| Cal.com、Doodle、Acuity Scheduling（Squarespace）、Microsoft Bookings、HubSpot Meetings |
| Olares Market | **未上架**（Olares 平替为 Cal.diy，待上架）|
| 来源 | [calendly.com/pricing](https://calendly.com/pricing) · [Sacra 研究报告](https://sacra.com/research/calendly-at-270m-arr/) · [calcom/cal.diy](https://github.com/calcom/cal.diy) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | calendly.com |
| SEMrush Rank | **5,475**（全球前 6K，顶级 SEO 资产）|
| 自然关键词数 | 29,815 |
| 月自然流量（US）| **432,378** |
| 自然流量估值 | **$1,220,682/月**（极高，仅靠 SEO）|
| 付费关键词数 | 13（几乎为零）|
| 月付费流量 | 141 |
| 排名 1-3 位 | 2,239 词 |
| 排名 4-10 位 | 2,687 词 |
| 排名 11-20 位 | 3,436 词 |

> **核心发现**：Calendly 的 Google Ads 投入几乎为零（13 个词、141 流量），全部 $1.22M/月流量价值来自**纯自然搜索**。这一"零付费 + 极强 SEO"模式在同量级 SaaS 中极为罕见，本质是 PLG 病毒式传播将用户变为内容资产（每个 calendly.com/username 页面都是可被索引的落地页）。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| calendly.com（主站）| 27,293 | 429,659 | 99.37% |
| community.calendly.com | 2,265 | 1,346 | 0.31% |
| www.calendly.com | 53 | 854 | 0.20% |
| developer.calendly.com | 196 | 519 | 0.12% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| calendly | 1 | 301,000 | 78 | $2.20 | 240,800 | 品牌 | / |
| calendly login | 1 | 33,100 | 31 | $0.01 | 26,480 | 品牌/导航 | /login |
| calendy | 1 | 27,100 | 70 | $2.20 | 21,680 | 品牌(误拼) | / |
| calendarly | 1 | 5,400 | 79 | $2.20 | 4,320 | 品牌(误拼) | / |
| calendly pricing | 1 | 3,600 | 32 | $3.46 | 2,880 | 商业 | /pricing |
| calendly free | 1 | 3,600 | 38 | $4.77 | 2,880 | 信息/商业 | / |
| calandly | 1 | 3,600 | 72 | $2.20 | 2,880 | 品牌(误拼) | / |
| calendly.com login | 1 | 2,900 | 63 | $0.18 | 2,320 | 导航 | /login |
| www.calendly.com login | 1 | 2,900 | 50 | $0.02 | 2,320 | 导航 | /login |
| caednly | 1 | 2,400 | 74 | $2.20 | 1,920 | 品牌(误拼) | / |
| calendely | 1 | 1,900 | 80 | $2.20 | 1,520 | 品牌(误拼) | / |
| calendly careers | 1 | 1,900 | 20 | $0.90 | 1,520 | 招聘 | /careers |
| **scheduling** | 2 | 33,100 | 97 | $8.30 | 1,158 | 品类 | / |
| scheduling app | 1 | 8,100 | 52 | $8.29 | 1,069 | 品类 | / |
| calendly sign in | 1 | 1,600 | 36 | $3.59 | 1,280 | 导航 | /login |
| free calendly | 1 | 1,600 | 30 | $3.60 | 1,280 | 商业 | / |
| scheduling software | 1 | 5,400 | 47 | $14.18 | 712 | 品类 | / |
| calendly scheduling software | 1 | 1,300 | 34 | $15.25 | 1,040 | 商业 | / |
| calendly link | 1 | 1,300 | 46 | $3.17 | 1,040 | 功能 | / |
| appointment scheduling software | 1 | 3,600 | 44 | $10.73 | 475 | 品类 | / |
| scheduling tool | 1 | 1,600 | 88 | $6.22 | 396 | 品类 | / |
| online scheduling software | 1 | 1,900 | 70 | $16.78 | 471 | 品类 | / |
| **what is a browser extension** | 6 | 33,100 | 56 | $0.00 | 794 | 信息 | /blog/... |

> 自然关键词中品牌词与误拼变体（calendy/calendarly/calandly/caednly/calendely…）合计带走约 30 万月流量，Calendly 对所有自身误拼词排名第 1，是极深的品牌护城河。品类词（scheduling、scheduling app、scheduling software）也有较强排名，说明其内容/权威度已溢出品牌圈。

### 付费词（Google Ads）

Calendly **几乎不投放 Google Ads**（仅 13 词、141 流量），属于极罕见的"纯 SEO 驱动 $270M ARR SaaS"。Semrush 检测到的极少量"付费词"均为个人用户预约页（如 calendly.com/dscrdon/）在 Google 中的展示，并非 Calendly 公司的广告投放。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| free scheduling app | 2,900 | 40 | $6.42 | 商业 | 含免费需求 |
| calendly alternatives | 1,600 | 20 | $3.66 | 商业 | ⭐ 核心替代词 |
| calendly competitors | 480 | 16 | $5.72 | 商业 | ⭐ |
| cal.com vs calendly | 390 | 18 | $3.66 | 对比 | ⭐ |
| calendly vs acuity | 390 | 12 | $4.43 | 对比 | ⭐ |
| doodle alternative | 320 | 15 | $2.23 | 商业 | ⭐ 竞品 doodle 替代 |
| free calendly alternative | 320 | 11 | $3.45 | 商业 | ⭐ |
| calendly alternative | 260 | 17 | $3.66 | 商业 | ⭐ |
| alternatives to calendly | 260 | 23 | $6.90 | 信息 | ⭐ |
| microsoft bookings vs calendly | 210 | 12 | $3.02 | 对比 | ⭐ |
| calendly free alternative | 260 | 16 | $3.97 | 商业 | ⭐ |
| calendly vs microsoft bookings | 110 | 12 | $2.79 | 对比 | ⭐ |
| acuity scheduling alternatives | 140 | 13 | $11.46 | 商业 | ⭐ 高 CPC |
| calendly alternatives free | 140 | 8 | $3.45 | 商业 | ⭐ KD=8! |
| open source calendly alternative | 30 | 10 | $3.15 | 信息 | ⭐ |
| acuity scheduling alternative | 50 | 12 | $17.59 | 商业 | ⭐ 极高 CPC |
| free alternatives to calendly | 70 | 3 | $4.19 | 商业 | ⭐ KD=3! |
| apps like calendly | 40 | 15 | $6.18 | 商业 | ⭐ |
| microsoft bookings alternative | 40 | 10 | $6.39 | 商业 | ⭐ |
| squarespace scheduling vs calendly | 40 | 4 | $0.00 | 对比 | ⭐ KD=4! |
| best calendly alternative | 30 | 21 | $8.52 | 商业 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| scheduling software | 5,400 | 45 | $16.32 | 商业 | Calendly 已排 #1 |
| online booking system | 2,400 | 88 | $13.83 | 信息 | 极高 KD |
| appointment booking software | 1,600 | 72 | $13.74 | 商业 | 极高 KD |
| scheduling app | 8,100 | 52 | $8.29 | 品类 | Calendly 已排 #1 |
| meeting scheduling software | 590 | 85 | $6.73 | 信息 | 极高 KD |
| appointment scheduling app | 1,000 | 76 | $9.06 | 信息 | 极高 KD |
| calendar scheduling software | 390 | 77 | $10.78 | 商业 | 极高 KD |
| **automated scheduling** | 480 | 28 | $10.36 | 信息 | ⭐ KD低+高CPC |
| **scheduling automation** | 140 | 23 | $21.25 | 商业 | ⭐ KD=23+CPC=$21！|
| free scheduling app | 2,900 | 40 | $6.42 | 商业 | ⭐ 有机会 |
| when2meet | 90,500 | 34 | $2.08 | 导航 | ⭐ 相邻品类大词 |
| whenisgood | 8,100 | 19 | $3.04 | 导航 | ⭐ |
| meeting time zone planner | 2,900 | 27 | $2.79 | 信息 | ⭐ |
| lettuce meet | 2,400 | 17 | $3.09 | 导航 | ⭐ |
| scheduling poll | 6,600 | 32 | $0 | 信息 | ⭐ |

### 产品 / 功能词（calendly 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| calendly pricing | 3,600 | 32 | $3.56 | 商业 | ⭐ |
| calendly free | 3,600 | 38 | $4.16 | 商业/信息 | ⭐ |
| is calendly free | 1,900 | 30 | $2.81 | 信息 | ⭐ |
| calendly free plan | 880 | 30 | $2.87 | 信息 | ⭐ |
| calendly api | 880 | 24 | $4.84 | 信息 | ⭐ |
| how to use calendly | 480 | 42 | $3.22 | 信息 | |
| calendly review | 260 | 39 | $2.34 | 信息 | |
| calendly cost | 590 | 35 | $8.58 | 商业 | |
| calendly embed | 170 | 21 | $0 | 功能 | ⭐ |
| calendly vs acuity | 390 | 12 | $4.43 | 对比 | ⭐ |
| calendly vs google calendar | 170 | 14 | $1.59 | 对比 | ⭐ |
| calendly teams | 110 | 32 | $7.42 | 商业 | |
| calendly outlook | 90 | 30 | $4.27 | 集成 | ⭐ |
| calendly careers | 1,900 | 20 | $0.90 | 招聘 | ⭐ |
| calendly integration | 70 | 53 | $4.97 | 集成 | |
| calendly vs doodle | 110 | 21 | $1.28 | 对比 | ⭐ |
| calendly salesforce | 30 | 0 | $15.25 | 集成 | ⭐ CPC极高 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source calendly | 50 | 19 | $1.72 | 信息 | ⭐ |
| open source calendly alternative | 30 | 10 | $3.15 | 信息 | ⭐ |
| self hosted calendly | 20 | 0 | $0 | 信息 | ⭐ 近零 KD！|
| self hosted booking system | 20 | 0 | $0 | 信息 | ⭐ 近零 KD |
| open source booking system | 20 | 0 | $6.69 | 信息 | ⭐ |
| open source appointment scheduling | 20 | 0 | $4.06 | 信息 | ⭐ |
| open source scheduling tool | 20 | 0 | $6.27 | 信息 | ⭐ |
| self hosted scheduling software | 20 | 0 | $4.75 | 信息 | ⭐ |
| open source meeting scheduler | 20 | 0 | $0 | 信息 | ⭐ |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Calendly 是闭源 SaaS + 按座位收费，用户数据存在第三方；Cal.diy（calcom/cal.diy，MIT，~46K ⭐）是完全开源的社区版，部署在 Olares 上可实现"数据自主 + 无限用户 + 无月费"，Olares 叙事切入点 = 自托管 Calendly 替代**。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| calendly alternatives | 1,600 | 20 | $3.66 | ⭐⭐⭐ Olares + Cal.diy = "calendly alternative that respects your data"，直接竞争位 |
| free scheduling app | 2,900 | 40 | $6.42 | ⭐⭐ Cal.diy on Olares = 真正免费（自托管成本 vs 每座位月费）|
| calendly competitors | 480 | 16 | $5.72 | ⭐⭐ 竞品清单页，Cal.diy on Olares 高居 self-hosted 分类首位 |
| cal.com vs calendly | 390 | 18 | $3.66 | ⭐⭐⭐ Cal.diy 正是 Cal.com 开源核心，Olares 让部署从"高级服务器技能"→一键安装 |
| calendly alternative | 260 | 17 | $3.66 | ⭐⭐⭐ 同上，核心替代词 |
| free calendly alternative | 320 | 11 | $3.45 | ⭐⭐⭐ KD=11，Olares + Cal.diy 是字面意义上"免费 Calendly 替代品" |
| doodle alternative | 320 | 15 | $2.23 | ⭐⭐ Doodle = 投票轮询，Olares 可同时托管 Cal.diy 替代品 |
| calendly alternatives free | 140 | 8 | $3.45 | ⭐⭐⭐ KD=8，极低竞争，关键词精准契合 Olares |
| microsoft bookings vs calendly | 210 | 12 | $3.02 | ⭐⭐ 对比内容，第三方选项 = Olares 自托管方案 |
| open source calendly | 50 | 19 | $1.72 | ⭐⭐⭐ 直接 Olares 机会词 |
| open source calendly alternative | 30 | 10 | $3.15 | ⭐⭐⭐ 精准意图，KD=10 |
| acuity scheduling alternative | 50 | 12 | $17.59 | ⭐⭐ CPC $17.59！说明行业买词意愿极高，Olares 内容可切 |
| self hosted calendly | 20 | 0 | $0 | ⭐⭐⭐ 近零竞争，GEO 占位词，语义精准 |
| free alternatives to calendly | 70 | 3 | $4.19 | ⭐⭐⭐ KD=3！几乎零竞争 |
| scheduling automation | 140 | 23 | $21.25 | ⭐⭐ 高 CPC + 低 KD，Olares 自动化场景切入点 |
| automated scheduling | 480 | 28 | $10.36 | ⭐⭐ 自托管自动化调度 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| calendly alternatives | 1,600 | 20 | $3.66 | 商业 | **主词候选** | 核心替代词，KD20 可打，Olares + Cal.diy 是自托管 Calendly 替代的核心叙事入口 |
| free scheduling app | 2,900 | 40 | $6.42 | 商业 | **主词候选** | 量最大的可进入品类词，KD40 有挑战但可用 Cal.diy on Olares 切"真正免费"角度 |
| calendly alternative | 260 | 17 | $3.66 | 商业 | **主词候选** | KD=17 低竞争，配合次级词簇攻击，Olares 一键部署 Cal.diy |
| free calendly alternative | 320 | 11 | $3.45 | 商业 | **主词候选** | KD=11 超低，字面精准，值得独立落地页 |
| cal.com vs calendly | 390 | 18 | $3.66 | 对比 | **主词候选** | Cal.diy = Cal.com 开源版，Olares 是最简部署方式，三方对比文章强吸流量 |
| calendly competitors | 480 | 16 | $5.72 | 商业 | **主词候选** | KD=16，"竞品"清单格式，高流量潜力 |
| automated scheduling | 480 | 28 | $10.36 | 信息 | **主词候选** | KD=28+高 CPC，Olares 自动化场景（Cal.diy + n8n/workflow）|
| scheduling automation | 140 | 23 | $21.25 | 商业 | 次级 | KD=23，CPC 极高（$21），与 automated scheduling 并入同一篇 |
| calendly alternatives free | 140 | 8 | $3.45 | 商业 | **主词候选** | KD=8！量小但竞争几乎为零，配合主词排名 |
| free alternatives to calendly | 70 | 3 | $4.19 | 商业 | 次级 | KD=3！量小，并入 free calendly alternative 文章，成本为零 |
| microsoft bookings vs calendly | 210 | 12 | $3.02 | 对比 | 次级 | 三方对比（MS Bookings / Calendly / Cal.diy on Olares）|
| open source calendly alternative | 30 | 10 | $3.15 | 信息 | 次级 | 精准意图词，量小 KD 低，并入自托管主题 |
| open source calendly | 50 | 19 | $1.72 | 信息 | 次级 | Olares 机会词，量小但意图精准 |
| acuity scheduling alternative | 50 | 12 | $17.59 | 商业 | 次级 | CPC $17.59！高商业意图，并入替代词总页 |
| doodle alternative | 320 | 15 | $2.23 | 商业 | 次级 | KD=15，Doodle 用户也是潜在的 Cal.diy on Olares 用户 |
| calendly pricing | 3,600 | 32 | $3.56 | 商业 | 次级 | 量大但 KD=32，用于对比文中的定价部分 |
| is calendly free | 1,900 | 30 | $2.81 | 信息 | 次级 | 量大 KD 中等，引导到"自托管才是真免费" |
| self hosted calendly | 20 | 0 | $0 | 信息 | **GEO** | 近零量近零竞争，语义精准，GEO 占位 + FAQ |
| self hosted booking system | 20 | 0 | $0 | 信息 | **GEO** | 同上，布局 AI Overview 引用位 |
| open source scheduling tool | 20 | 0 | $6.27 | 信息 | **GEO** | CPC $6.27 但量为零，GEO 前瞻词 |
| self hosted scheduling software | 20 | 0 | $4.75 | 信息 | **GEO** | GEO 前瞻布局，自托管日程领域空白 |

---

## 核心洞见

1. **品牌护城河极深，正面刚无意义**：Calendly 自然流量 432K/月，估值 $1.22M，品牌词"calendly"月量 30 万、KD=78，所有误拼变体排名第 1。这类心智护城河 Olares 不需要也不应该去抢。更值得注意的是它**几乎不投 Google Ads**（13 词/141 流量），$270M ARR 全靠 SEO + PLG——说明日程预约行业的用户获取完全由搜索与口碑驱动，内容机会真实存在。

2. **可复制的打法是"替代词清单 + 对比文矩阵"**：Calendly 自身在 `scheduling`（KD97）、`scheduling app`（KD52）等超级大词排名第 1，但这些词 KD 远超 Olares 现阶段能打的范围。真正的机会在其**替代词矩阵**——`calendly alternatives`（KD20）、`calendly alternative`（KD17）、`free calendly alternative`（KD11）、`calendly alternatives free`（KD8）、`free alternatives to calendly`（KD3）——KD 从 3 到 20，从 Calendly 自有 SEO 飞轮"溢出"的流量，可被 Olares 的"自托管替代品清单/对比文"承接。

3. **对 Olares 最重要的 3 个词**：
   - `calendly alternatives`（1,600/KD20）：替代词流量入口，可打，写"Best Calendly Alternatives 2026（含自托管选项 Cal.diy on Olares）"
   - `free calendly alternative`（320/KD11）：字面精准 + KD 超低，独立落地页
   - `cal.com vs calendly`（390/KD18）：Cal.diy 是 Cal.com 开源版，Olares 使部署极简，三方对比文直接命中搜索意图

4. **最大攻击面——定价 + 闭源数据控制**：`is calendly free`（1,900/KD30）、`calendly free plan`（880）、`calendly pricing`（3,600）、`calendly cost`（590/CPC=$8.58）密集出现，说明用户对"免费"与定价极敏感。Calendly 免费版仅限 1 个事件类型，Teams 套餐每座位 $16/月——而 Cal.diy on Olares 一次部署、无限事件类型、无限用户数、数据归自己，是强有力的叙事差异化。`acuity scheduling alternative`（KD12，CPC **$17.59**）更说明整个日程预约行业的商业意图极高，愿意付费。

5. **隐藏低 KD 金矿**：
   - `calendly alternatives free`（KD=8）、`free alternatives to calendly`（KD=3）、`squarespace scheduling vs calendly`（KD=4）——这三个词竞争几乎为零，通过长尾并入替代词主文章，边际成本接近零
   - `scheduling automation`（KD=23，CPC=$21.25）——量虽小（140）但 CPC 极高，说明企业用户在主动搜索自动化调度方案，Olares + Cal.diy + n8n 的组合可切入

6. **GEO 前瞻布局**：`self hosted calendly`（KD=0）、`self hosted booking system`（KD=0）、`open source scheduling tool`（KD=0）目前量几乎为零，但语义与 Olares 高度契合。建议提前发布内容占位 AI Overview / Perplexity 引用位——搜索量会随自托管趋势增长而上升。

7. **与既有分析的关联**：`olares-500-keywords` 中目前无日程预约相关词条，本报告打开了一个全新品类缺口。`free scheduling app`（2,900）与 `scheduling software`（5,400）作为中高量品类词，应补入 500 词表的"生产力工具"类；自托管信号词（self hosted calendly/booking system/scheduling tool）则是 GEO 类词表的最新增补材料。此外 Cal.diy 作为 Olares Market 候选应用，其 GitHub 46K⭐ 与 `cal.com vs calendly` 搜索量双重验证了社区需求，建议加速上架推进。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
