# ADT SEO 竞品分析报告

> 域名：adt.com | SEMrush US | 2026-07-06
> 美国最大专业安防监控服务商，6.1M 订阅户，品牌始于 1874 年；核心护城河是 12 个自营监控中心 + 全国安装团队 + 36 个月合同锁定，月费 $34.99–$57.99+，竞争对手是 SimpliSafe、Vivint、Ring（Amazon）。

---

## 项目理解（前置）

ADT（American District Telegraph）创立于 1874 年，是美国最古老、规模最大的专业安防监控公司，NYSE: ADT，总部佛罗里达州博卡拉顿。截至 2025 年底拥有约 **6.1 M 监控订阅户**，占美国专业监控住宅市场约 **25%** 份额（来源：2026 年 10-K；Wedbush Research 2026-03）。核心壁垒在于 12 座自营监控中心（Vivint 只有 2 座，Ring/SimpliSafe 均外包）+ 全国 SSO 安装网络 + 平均 **8 年**客户留存周期 / **87%** 年续签率（来源：OmahaLine ADT 分析）。

产品分三线：**ADT Pro Install**（专业上门安装，36 个月合同，月费 $34.99–$57.99+）、**ADT Self-Setup**（DIY 无合同，月费 $24.99–$44.99）、**ADT Blu**（DIY 自监控 $9.99/月起，专业监控 $24.99/月起）。2023–2024 年先后剥离商用安防和家用太阳能业务，聚焦住宅安防并与 **Google**（Nest 集成）及 **State Farm**（保险联动）深度合作。

**对 Olares 的叙事空间**：Pro Install 3 年总费用 $1,600–$2,600，合同违约金高达剩余 75%；HA on Olares + Frigate NVR + Z-Wave/Zigbee 传感器 = 专业级自监控安防，**零月费**、视频不出家门、无合同锁定。诚实注意事项：自监控方案无 24/7 专业派警，适合愿主动关注告警的用户。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 美国最大专业安防监控品牌，闭源云订阅 + 合同绑定生态 |
| 开源 / 许可证 | 闭源；ADT+ App 与后台全封闭 |
| 主仓库 | 无开源仓库；NYSE 上市公司（股票代码 ADT） |
| 核心功能 | 专业报警监控派警、智能摄像头（Google Nest 集成）、门窗传感器、动作探测、烟雾/CO 探测、医疗急救告警、ADT+ 智能家居 App |
| 商业模式 / 定价 | 硬件一次购买 + 月度监控服务（核心收入）；Pro Install 月费 $34.99–$57.99+，36 个月合同；ADT Blu 自监控 $9.99/月起，专业监控 $24.99/月；3 年总成本 $1,100–$2,600 |
| 差异化 / 价值主张 | 150 年品牌信任、全国 SSO 安装与服务、12 个自营监控中心（行业最多）、Google Nest 深度集成、State Farm 保险折扣 |
| 主要竞品（初判）| Vivint（高端专业安装）、SimpliSafe（DIY 无合同）、Ring/Amazon（DIY 摄像头+报警）、Brinks Home、Comcast Xfinity Home |
| Olares Market | Frigate NVR ✅、Home Assistant ✅（ADT 最佳开源替代栈）；ADT 本身不在 Market（闭源） |
| 来源 | https://adt.com/、ADT 2026 10-K、[OmahaLine ADT 分析](https://omahaline.com/essays/adt)、[SafeHome.org 2026 报告](https://www.safehome.org/resources/home-security-industry-annual/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | adt.com |
| SEMrush Rank | **2,752**（全球前 3,000，消费品牌级） |
| 自然关键词数 | **169,271** |
| 月自然流量（US）| **911,708** |
| 自然流量估值 | **$4,527,284**/月 |
| 付费关键词数 | 2,839 |
| 月付费流量 | 128,673 |
| 付费流量估值 | $976,044/月 |
| 排名 1-3 位 | **11,840** 词 |
| 排名 4-10 位 | **17,578** 词 |
| 排名 11-20 位 | **18,143** 词 |

> ADT 月均 90 万+自然流量，流量估值超 $450 万/月，是 IoT/安防赛道绝对的流量巨头。排名 TOP 3 的词近 12,000 个——但绝大部分是强品牌词（adt、adt login、adt security 等），真正的非品牌类别词（best home security system、smart lock）排名较后，说明 ADT 靠品牌认知驱动流量而非内容 SEO。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.adt.com（主站） | 106,980 | 786,611 | **86.3%** |
| help.adt.com | 55,760 | 92,816 | **10.2%** |
| jobs.adt.com | 1,536 | 19,072 | 2.1% |
| 3ps.adt.com | 149 | 3,937 | 0.4% |
| plus.adt.com | 532 | 3,699 | 0.4% |
| newsroom.adt.com | 1,809 | 1,747 | 0.2% |
| investor.adt.com | 742 | 1,540 | 0.2% |

**洞见**：help.adt.com 以 55,760 个关键词贡献 10% 流量——客服/计费/取消相关的支持文档是 ADT 第二大流量引擎，也是"如何取消 ADT"类内容的竞争点。主站流量高度集中（86%），内容矩阵不如 Ring 分散。

### 官网 TOP 自然关键词（按流量降序，Top 40）

| 关键词 | 排名 | 月量 | CPC | 流量占比 | 意图 | URL |
|--------|------|------|-----|---------|------|-----|
| adt | 1 | 246,000 | $5.92 | 21.6% | 品牌 | adt.com/ |
| adt login | 1 | 74,000 | $4.10 | 6.5% | 导航 | /control-login |
| adt security | 1 | 33,100 | $7.58 | 2.9% | 品牌 | adt.com/ |
| adt customer service | 1 | 135,000 | $0 | 0.4% | 导航 | help.adt.com/ |
| adt control | 1 | 12,100 | $2.80 | 1.1% | 导航 | /control-login |
| adt careers | 1 | 8,100 | $0.44 | 0.7% | 导航 | jobs.adt.com/ |
| adt home security systems | 1 | 6,600 | $11.39 | 0.6% | 商业 | adt.com/ |
| adt security services | 1 | 6,600 | $6.26 | 0.6% | 商业 | adt.com/ |
| adt bill pay | 1 | 9,900 | $0.83 | 0.3% | 导航 | /customer/billing |
| temperature | 14 | 1,000,000 | $0.57 | 0.4% | 信息 | /resources/average-room-temperature |
| adt customer service | 2 | 135,000 | $0 | 0.3% | 导航 | /customer |
| adt alarm systems | 1 | 5,400 | $10.33 | 0.5% | 商业 | adt.com/ |
| adt cameras | 1 | 5,400 | $3.75 | 0.5% | 商业 | /shop/.../cameras/ |
| adt alarm system | 1 | 5,400 | $10.33 | 0.5% | 商业 | adt.com/ |
| adt security cameras | 1 | 4,400 | $3.75 | 0.4% | 商业 | /shop/.../cameras/ |
| best home security system | 2 | 22,200 | $14.51 | 0.2% | 商业 | /home-security |
| adt doorbell camera | 1 | 2,400 | $1.48 | 0.2% | 商业 | /doorbell-camera |
| smart lock | 5 | 550,000 | $1.96 | 0.2% | 商业 | /resources/what-are-smart-locks |
| adt payment | 1 | 1,900 | $16.84 | 0.2% | 导航 | /customer/billing |
| adt medical alert | 1 | 1,600 | $8.99 | 0.1% | 商业 | /health |

> **洞见**：前 20 名自然流量词中约 85% 是强品牌/导航词（adt login、adt bill pay、adt control login 等）。真正的品类词仅 "best home security system"（排名 2，不是 1）和 "smart lock"（排名 5）。`temperature` 这个 100 万搜索量词以第 14 名排入——说明 ADT 有内容资源页策略，但非核心流量驱动。CPC 最高的词是 `adt payment`（$16.84）和 `adt home security systems`（$11.39），反映本品类极高的商业价值密度。

### 付费词（Google Ads，按流量排序，Top 15）

ADT 付费策略：主要买自身品牌词防御竞品截流，同时购买竞品品牌词（SimpliSafe、Arlo、Nest、Ring 等）和品类大词。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| adt | 1 | 246,000 | $5.92 | adt.com |
| doorbell camera | 1 | 246,000 | $3.28 | adt.com |
| simplisafe | 1 | 165,000 | $3.35 | adt.com |
| home security systems | 1 | 74,000 | $22.29 | adt.com |
| security cameras | 1 | 60,500 | $5.85 | adt.com |
| ring doorbell camera | 1 | 49,500 | $1.85 | adt.com |
| home security system | 1 | 49,500 | $22.29 | adt.com |
| arlo camera | 1 | 40,500 | $0.70 | adt.com |
| adt security | 1 | 33,100 | $7.58 | adt.com |
| nest camera | 1 | 27,100 | $1.43 | adt.com |
| home security cameras | 1 | 27,100 | $5.75 | adt.com |
| google nest camera | 1 | 22,200 | $1.50 | adt.com |
| simplisafe inc. | 1 | 22,200 | $3.35 | adt.com |
| best home security system | 1 | 22,200 | $12.76 | adt.com |
| house security cameras | 1 | 22,200 | $5.95 | adt.com |

> **洞见**：ADT 正在大量购买 **SimpliSafe**（165,000 月量）、**Ring**（201,000 / 49,500）、**Arlo**（40,500）、**Nest**（22,200-27,100）的品牌词，以及 `home security systems`（$22.29 CPC）这类品类超级大词。月付费流量 128,673，付费投入 $976K/月——表明 ADT 非常清楚自己的"逃离竞品"流量正在被竞品截获，不得不回购。`home security systems` 的 $22.29 CPC 是整个安防品类竞价密度的缩影。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| simplisafe vs adt | 1,300 | 22 | $15.04 | 商业 | ⭐ 最高量竞品对比词，ADT 自己在付费买 |
| adt vs vivint | 1,300 | — | $14.15 | 商业 | 高端对比，CPC 高 |
| adt vs simplisafe | 880 | 24 | $18.53 | 商业 | ⭐ 与上同族，可并文 |
| adt vs ring | 720 | — | $12.27 | 商业 | DIY vs 专业监控对比 |
| simplisafe alternative | 140 | — | $4.47 | 商业 | 替代词跨品牌，量小但精准 |
| adt alternative | 90 | 24 | $9.15 | 商业 | ⭐ KD 极低，Olares 核心攻击词 |
| home security alternatives | 20 | — | $3.80 | 商业 | 量小，GEO 候选 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home security system | 49,500 | 高 | $20.33 | 商业 | ADT/Ring 等主战场，难排 |
| home security systems | 74,000 | 高 | $20.33 | 商业 | 同上 |
| best home security system | 22,200 | 高 | $12.76 | 商业 | ADT 自己只排名 2 |
| smart home security | 8,100 | — | $9.18 | 商业 | 潜力品类词 |
| diy home security system | 1,900 | 59 | $9.56 | 商业 | KD 59，难度偏高 |
| home security system cost | 880 | — | $7.95 | 信息/商业 | 价格比较意图 |
| self monitored home security | 590 | 25 | $6.79 | 商业 | ⭐ KD 低，自监控意图 |
| home security monitoring service | 880 | — | $16.31 | 商业 | 专业监控品类词 |
| diy alarm system | 590 | — | $11.49 | 商业 | DIY 安装意图 |
| alarm monitoring | 2,900 | — | $10.40 | 商业 | 品类词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| adt | 246,000 | — | $5.92 | 品牌 | 核心品牌词，排不动 |
| adt security | 33,100 | — | $7.58 | 品牌/商业 | 强品牌词 |
| adt home security | 18,100 | — | $9.85 | 商业 | 品牌+品类 |
| adt alarm systems | 4,400 | — | $9.24 | 商业 | 产品词 |
| adt cameras | 5,400 | — | $3.75 | 商业 | 产品词 |
| adt monthly fee | 110 | — | $3.87 | 信息 | 价格研究意图 |
| adt contract length | 170 | 19 | $7.62 | 信息 | ⭐ 合同研究意图 |
| adt early termination fee | 170 | 17 | $5.06 | 信息 | ⭐ 违约金研究，逃跑意图 |
| cancel adt | 1,000 | 31 | $2.06 | 信息 | 取消意图 |
| how to cancel adt | 1,000 | 27 | $2.32 | 信息 | ⭐ 高频取消问题 |
| cancel adt contract | 140 | 19 | $0.53 | 信息 | ⭐ 具体取消合同步骤 |
| is adt worth it | 1,000 | — | $8.07 | 信息/商业 | 购买决策词 |
| how much is adt a month | 1,600 | — | $4.84 | 信息 | 价格查询 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| no subscription security camera | 5,400 | — | $1.71 | 商业 | 量大，零订阅摄像头 |
| home security camera no subscription | 880 | 44 | $2.31 | 商业 | 明确无订阅意图 |
| home security no monthly fee | 390 | 30 | $6.26 | 商业 | ⭐ 零月费直接命中 Olares |
| frigate nvr | 3,600 | 36 | $3.84 | 信息/商业 | ⭐ Olares Market 已上架，量大 |
| frigate home assistant | 720 | ~5 | $0 | 信息 | ⭐ 高度相关，KD 极低 |
| self monitored home security | 590 | 25 | $6.79 | 商业 | ⭐ 自监控意图核心 |
| home assistant security | 90 | 14 | $6.44 | 信息 | ⭐ HA 安防场景词 |
| home assistant alarm | 90 | — | $2.73 | 信息 | HA 报警配置词 |
| home assistant security camera | — | 14 | — | 信息 | ⭐ KD 极低，直接 HA 集成词 |
| open source home security | 20 | 0 | $7.01 | 信息 | ⭐⭐ KD=0，GEO 金矿 |
| self hosted home security | 20 | — | $6.59 | 信息 | GEO 前哨 |
| diy security system no monthly fee | 20 | 0 | $5.91 | 商业 | ⭐⭐ KD=0 |
| zigbee security system | 20 | — | $1.28 | 信息 | 协议层信号词 |
| z-wave home security | 20 | — | $2.56 | 信息 | 协议层信号词 |
| home security without monthly fee | — | 41 | — | 商业 | 月费敏感型 |

---

## Olares 关联词（Phase 3）

**核心叙事**：ADT 的竞争优势是专业监控网络 + 品牌信任，但代价是 $34–58/月×36 个月合同锁定，3 年总成本高达 $1,600–$2,600。HA on Olares + Frigate NVR（已上架 Olares Market）+ Z-Wave/Zigbee 传感器 = 本地运行的专业级监控栈，零月费、视频不出家门、完全可控；诚实注意事项：无 24/7 专业派警，适合愿主动处置告警的用户。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|------------|--------|
| adt alternative | 90 | 24 | $9.15 | HA + Frigate on Olares = 最完整 ADT 开源替代，零月费，一键部署 | ⭐⭐⭐ |
| home security no monthly fee | 390 | 30 | $6.26 | Olares 核心卖点直接命中：Frigate + Z-Wave，无任何月费 | ⭐⭐⭐ |
| self monitored home security | 590 | 25 | $6.79 | Olares 场景即自监控：告警推送到手机，视频本地存，免去专业监控月费 | ⭐⭐⭐ |
| how to cancel adt | 1,000 | 27 | $2.32 | 取消 ADT 后的迁移路径：自托管 HA + Frigate 替代方案 | ⭐⭐⭐ |
| frigate nvr | 3,600 | 36 | $3.84 | Frigate 已上架 Olares Market，写"Frigate on Olares"可直接承接这部分流量 | ⭐⭐⭐ |
| cancel adt contract | 140 | 19 | $0.53 | 合同违约金计算 + 替代方案导流 | ⭐⭐ |
| adt early termination fee | 170 | 17 | $5.06 | ADT 违约金高，Olares 方案零合同即时可切换 | ⭐⭐ |
| adt vs simplisafe | 880 | 24 | $18.53 | 可写三角对比：ADT vs SimpliSafe vs Olares（DIY 自托管） | ⭐⭐ |
| simplisafe vs adt | 1,300 | 22 | $15.04 | 同上，搜量更大，主词机会 | ⭐⭐ |
| frigate home assistant | 720 | ~5 | $0 | KD 极低，直接 HA+Frigate 配置文，Olares 部署最佳入口 | ⭐⭐⭐ |
| home security camera no subscription | 880 | 44 | $2.31 | 无订阅摄像头方案：Frigate on Olares，NVR 本地存储 | ⭐⭐ |
| open source home security | 20 | 0 | $7.01 | KD=0，GEO 前哨；"开源安防 + Olares 一键部署"精准抢 AI 引用位 | ⭐⭐⭐ |
| home assistant security | 90 | 14 | $6.44 | HA 安防场景词，KD 极低，可写 HA Security on Olares 入门文 | ⭐⭐ |
| home assistant security camera | — | 14 | — | KD 极低，Olares 上的 HA + Frigate 摄像头集成教程入口 | ⭐⭐ |
| diy security system no monthly fee | 20 | 0 | $5.91 | KD=0，GEO；Olares = 最强 DIY 零月费安防方案 | ⭐⭐⭐ |
| self hosted home security | 20 | — | $6.59 | GEO 前哨，精准命中 Olares 定位 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| simplisafe vs adt | 1,300 | 22 | $15.04 | 商业 | **主词候选** | KD 22 + 1,300 量，三角对比文（ADT vs SimpliSafe vs 自托管）；CPC $15 说明转化价值极高 |
| adt vs simplisafe | 880 | 24 | $18.53 | 商业 | **次级** | 与上词同族合并；Olares 叙事=第三选项（自托管零月费） |
| how to cancel adt | 1,000 | 27 | $2.32 | 信息 | **主词候选** | 逃跑意图，KD 27，月量 1,000；取消 ADT 后迁移到 Frigate on Olares 的最佳承接文 |
| self monitored home security | 590 | 25 | $6.79 | 商业 | **主词候选** | KD 25，自监控意图直接命中 Olares 零月费叙事；CPC $6.79 说明高商业价值 |
| home security no monthly fee | 390 | 30 | $6.26 | 商业 | **主词候选** | KD 30（边界），月量 390；Olares 零月费核心词，簇内可合并 `diy security system no monthly fee` |
| adt alternative | 90 | 24 | $9.15 | 商业 | **主词候选** | KD 24，量仅 90 但 CPC $9.15，配合同族词（simplisafe alternative 140）合计量 >200；是对 ADT 最直接的攻击词 |
| frigate nvr | 3,600 | 36 | $3.84 | 信息/商业 | **主词候选** | 量 3,600，KD 36（偏高但 Olares Market 有直接优势）；Frigate 已上架 Olares，写部署文可独立成文 |
| frigate home assistant | 720 | ~5 | $0 | 信息 | **主词候选** | KD 极低，720 月量，纯技术配置词；Olares 一键部署 HA+Frigate 的最佳入口词 |
| cancel adt | 1,000 | 31 | $2.06 | 信息 | **次级** | 与 `how to cancel adt` 同族，并入取消文 |
| cancel adt contract | 140 | 19 | $0.53 | 信息 | **次级** | KD 19 ⭐，并入取消/迁移文，注意 CPC 低说明商业意图弱但流量精准 |
| adt early termination fee | 170 | 17 | $5.06 | 信息 | **次级** | KD 17 ⭐，违约金计算 + 迁移方案并文 |
| adt contract length | 170 | 19 | $7.62 | 信息 | **次级** | KD 19 ⭐，合同痛点词，并入 cancel adt 文 |
| home security camera no subscription | 880 | 44 | $2.31 | 商业 | **次级** | KD 44 略高，但无订阅摄像头意图与 Frigate on Olares 完全契合；并入 no monthly fee 文 |
| home assistant security | 90 | 14 | $6.44 | 信息 | **次级** | KD 14 ⭐⭐，HA 安防场景，与 `home assistant security camera`（KD 14）合并写教程 |
| open source home security | 20 | 0 | $7.01 | 信息 | **GEO** | KD=0，量 20，精准命中 Olares 定位；主要价值在 AI Overview/Perplexity 引用 |
| diy security system no monthly fee | 20 | 0 | $5.91 | 商业 | **GEO** | KD=0，Olares 零月费方案在 AI 结构化回答中的抢占词 |
| self hosted home security | 20 | — | $6.59 | 信息 | **GEO** | 自托管安防精准词，GPT/Claude 推荐结果中的定位词 |
| home assistant alarm | 90 | — | $2.73 | 信息 | **GEO** | HA 报警配置场景，语义精准，AI 引用位候选 |

---

## 核心洞见

1. **品牌护城河**：ADT 的 246,000 月量品牌词和 6.1M 订阅户不可正面刚；但"取消 ADT"（cancel adt 1,000、how to cancel adt 1,000）和"ADT 替代"（adt alternative 90、simplisafe vs adt 1,300）是自然渗入的侧翼——用户在主动寻找出口，ADT 自己的 help.adt.com 承接了部分，但第三方内容有空间。

2. **可复制的打法**：ADT 主要靠品牌霸权 + Google Ads 防御竞品词（买 SimpliSafe、Ring、Arlo 的品牌词，月花 $976K）；内容 SEO 策略相对薄弱——`temperature` 以第 14 名出现说明资源页有内容，但非核心。可复制点：**比较文**（simplisafe vs adt、adt vs ring）是流量密度 + CPC 最高的机会区，且 ADT 自己并不主导这些词的自然搜索结果。

3. **对 Olares 最关键的 3 个词**：
   - `self monitored home security`（590，KD 25）：自监控叙事核心，Olares = 自监控方案，无专业监控月费
   - `how to cancel adt`（1,000，KD 27）：逃跑意图，取消后用 Frigate on Olares 承接
   - `frigate home assistant`（720，KD ~5）：KD 极低，直接技术方案词，Olares Market 双上架

4. **最大攻击面**：ADT 的**价格与合同**是最大痛点——36 个月合同、75% 违约金、$34–58/月月费（3 年总成本 $1,600–$2,600）。`adt early termination fee`（KD 17）、`adt contract length`（KD 19）、`cancel adt contract`（KD 19）是 KD 最低的一批词，且都是逃跑意图（intent 一致），完美配合 Olares 零合同、零月费叙事。

5. **隐藏低 KD 金矿**：`open source home security`（KD=0，量 20）、`diy security system no monthly fee`（KD=0，量 20）、`home assistant security camera`（KD 14）、`adt early termination fee`（KD 17）——这些词 KD 极低但意图精准，是 GEO/长尾内容的绝佳插入点。`frigate home assistant`（KD ~5，720 量）是其中性价比最高的主词级机会。

6. **GEO 前瞻布局**：`open source home security`、`self hosted home security`、`diy security system no monthly fee`——这三个词量 <50 但语义最贴 Olares 定位，应写入 FAQ 段落和结构化答案中，抢占 ChatGPT/Perplexity/Google AI Overview 对"无订阅/开源家居安防"的引用位。

7. **与既有分析的关联**：ADT 的竞品词（`adt alternative`、`simplisafe vs adt`）与 Frigate NVR 已有报告（`frigate-nvr.md`）和 Ring 报告（`ring.md`）形成三角联动——"取消 Ring/ADT 转用 Frigate on Olares"的叙事可跨三篇报告在 seo-content 层复用。`no subscription security camera`（5,400 月量）是横跨 Ring/ADT/Frigate 的超级桥接词，值得独立选题。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、phrase_these、phrase_related、phrase_fullsearch、phrase_questions、phrase_kdi）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
