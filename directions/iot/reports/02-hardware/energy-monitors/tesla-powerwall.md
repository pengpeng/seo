# Tesla Powerwall SEO 竞品分析报告

> 域名：tesla.com/powerwall | SEMrush US | 2026-07-06
> 居家储能市场份额领导者（安装报价份额 ~63.3%），集成太阳能逆变器与锂铁磷酸电池的家庭储能一体机；Powerwall 3 已完全移除本地 API，数据强制上报 Tesla 云端。

---

## 项目理解（前置）

Tesla Powerwall 是 Tesla Energy 旗下的家用储能系统，当前主力产品为 **Powerwall 3**（2023 年 9 月发布、2024 年大规模铺货）：集成 11.5 kW 混合逆变器（6 路 MPPT，支持最大 20 kW 太阳能输入）与 13.5 kWh LFP 电芯，可叠加最多 4 组（1 主机 + 3 扩展），支持全宅备电。截至 2025 年，Tesla 已安装第百万台 Powerwall；按 AgentSolar 14.3 万报价样本，美国安装报价份额约 63.3%，是市场第一，远超 Enphase（17.1%）与 SolarEdge（10.6%）。**关键限制**：Powerwall 3 官方已封堵局域网直连 API——旧有的 Gateway 本地 Web UI 和路由静态路由均已失效，HA 原生集成（Local Polling）仅支持 Powerwall 2；Powerwall 3 用户只能通过 **Tesla Fleet API**（需 Tesla Developer 账号、云授权）或 pypowerwall 库借助 Powerwall 自身的 Wi-Fi AP 做有限本地读数，无法实现完整本地控制。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 美国市场份额最大的家用储能 + 太阳能逆变器一体机，强云依赖 |
| 开源 / 许可证 | 完全闭源；硬件 + 固件 + 云服务均为 Tesla 私有 |
| 主仓库 | 无官方开源仓库；第三方 [jasonacox/pypowerwall](https://github.com/jasonacox/pypowerwall)（★4.2k+，Python 读数库）；HA 官方集成 [home-assistant/core (powerwall)](https://www.home-assistant.io/integrations/powerwall/)（~1,840 活跃安装，仅支持 Powerwall 2） |
| 核心功能 | 13.5 kWh LFP 储能、11.5 kW 内置逆变器、全宅或部分备电、Storm Watch、VPP 需求响应、Tesla App 控制 |
| 商业模式 / 定价 | 硬件设备约 $9,200–$11,000，安装完成 $13,500–$16,800（依地区）；扩展包 $5,900 /台；强制 Tesla 认证安装商安装；无月订阅费，但云服务捆绑 |
| 差异化 / 价值主张 | 逆变器一体化（省去单独购串逆变器 $1,500–3,000）；LFP 10 年/无限次循环保修；美国最大安装网络与品牌公信力；Storm Watch 自动提前充满 |
| 主要竞品（初判）| Enphase IQ 5P（模块化微逆）、Generac PWRcell、FranklinWH aPower 2、SolarEdge Energy Bank |
| Olares Market | 未上架（闭源硬件）；Olares 角度 = HA on Olares 作为统一能源枢纽（含 Powerwall 2 本地读数 / Powerwall 3 限制性读数）+ "Powerwall alternative" 叙事（开放电池栈 + HA） |
| 来源 | [tesla.com/powerwall](https://www.tesla.com/powerwall)、[HA Powerwall 集成页](https://www.home-assistant.io/integrations/powerwall/)、[GitHub issue #144251](https://github.com/home-assistant/core/issues/144251)、[Teslemetry PW Control](https://teslemetry.crisp.help)、[AgentSolar 份额数据](https://agentsolar.ai/solar-batteries)、[SolarReviews 2026 pricing](https://www.solarreviews.com/blog/is-the-tesla-powerwall-the-best-solar-battery-available) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | tesla.com（/powerwall 子目录） |
| SEMrush Rank | — （顶级，rank 列返回 0） |
| 自然关键词数（/powerwall 子目录） | ~3,940 |
| 月自然流量（US，/powerwall）| ~45,670 |
| 自然流量估值 | ~$120,600/月 |
| 付费关键词数 | 0（/powerwall 无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 796 词 |
| 排名 4-10 位 | 327 词 |
| 排名 11-20 位 | 237 词 |

> 注：tesla.com 全域约有 408,336 自然关键词、6,663,631 月流量（US）；/powerwall 子目录仅是全站极小一部分，说明 Tesla 官网流量以车型、购买、服务为主，储能产品页面 SEO 权重相对有限——这是竞品内容可以切入的信号。

### 子域名流量分布（tesla.com 全域）

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.tesla.com | 408,336 | 6,663,631 | 87.81% |
| shop.tesla.com | 30,268 | 452,200 | 5.96% |
| tesla.com | 3,704 | 225,948 | 2.98% |
| ir.tesla.com | 11,315 | 103,048 | 1.36% |
| service.tesla.com | 23,741 | 45,713 | 0.60% |
| energylibrary.tesla.com | 6,033 | 14,266 | 0.19% |

> 洞察：`energylibrary.tesla.com` 有 6,033 个关键词但流量仅 14,266，说明 Tesla 储能技术文档库在 SEO 上覆盖了不少专业词、但转化流量有限——这些低竞争的技术词是可渗透的空间。

### 官网 TOP 自然关键词（按流量排序，均指向 /powerwall 落地页）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| tesla home battery | 1 | 2,900 | 63 | $3.25 | 2,320 | 商业/信息 | tesla.com/powerwall |
| tesla solar battery | 1 | 2,400 | 67 | $4.19 | 1,920 | 商业/信息 | tesla.com/powerwall |
| tesla wall | 1 | 1,600 | 56 | $2.81 | 1,280 | 导航/商业 | tesla.com/powerwall |
| tesla at home battery | 1 | 1,600 | 65 | $1.94 | 1,280 | 商业/信息 | tesla.com/powerwall |
| tesla battery wall | 1 | 1,300 | 55 | $2.27 | 1,040 | 商业/信息 | tesla.com/powerwall |
| tesla powerwall | 1 | 22,200 | 84 | $3.91 | 577 | 导航/商业 | tesla.com/powerwall |
| tesla powerwall 3 | 1 | 9,900 | 37 | $4.00 | 314 | 商业 | tesla.com/powerwall |
| solar battery storage system | 1 | 2,400 | 48 | $3.47 | 316 | 信息/商业 | tesla.com/powerwall |
| tesla battery backup home | 1 | 320 | 32 | $2.59 | 256 | 商业 | tesla.com/powerwall |
| powerwall battery | 1 | 320 | 50 | $2.00 | 256 | 商业 | tesla.com/powerwall |
| tesla backup battery | 1 | 480 | 44 | $3.73 | 384 | 商业/交易 | tesla.com/powerwall |
| tesla home generator | 1 | 260 | 35 | $1.62 | 208 | 商业/信息 | tesla.com/powerwall |

> 观察：`tesla powerwall` 虽月量 22,200、P1，但因品牌导航意图占绝对主导（用户直接要去官网），实际为该页带来流量仅 577——**品牌词流量被意图稀释**，说明大量用户并非在"研究"阶段，而是已知目标直接导航。`tesla powerwall 3`（9,900/月，KD 37）是少有的"量大 + 品牌前缀 + KD 不太高"的词——商业意图用户在研究这款产品，有内容切入机会。

### 付费词（Google Ads）

/powerwall 子目录**无 Google Ads 投放**（resource_adwords 返回空数据）。Tesla 品牌力足够强，不需要购买与自身产品名匹配的广告位；但竞品（Enphase、Generac 等）可能在购买"tesla powerwall alternative"等词。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| tesla powerwall alternative | 480 | **7** | $1.86 | 信息 | ⭐⭐⭐ **本报告最高价值词**；KD 仅 7，量 480 远超同类替代词 |
| powerwall competitors | 140 | 20 | $3.24 | 信息 | ⭐ 研究竞品的用户群，高意图 |
| enphase vs tesla | 140 | 11 | $16.31 | 信息/商业 | ⭐ CPC $16 极高，说明商业价值高；KD 11 可攻 |
| powerwall alternative | 50 | 16 | $2.19 | 信息 | ⭐ 与"tesla powerwall alternative"同族，KD 低 |
| powerwall vs generac | 50 | **10** | $7.60 | 信息/商业 | ⭐ CPC $7.6 高，用户深度调研阶段 |
| powerwall vs enphase | 40 | 14 | $0.00 | 信息 | ⭐ |
| tesla powerwall competitors | 720 | 17 | $2.46 | 信息 | ⭐⭐ 量 720，KD 17，对比意图用户群大 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| solar battery backup | 8,100 | 36 | $3.40 | 信息/商业 | 最大品类词，KD 36 |
| solar battery | 12,100 | 35 | $1.84 | 信息/商业 | 覆盖品类最大词，但意图泛 |
| home battery backup | 5,400 | 39 | $2.09 | 商业 | 备电用户核心词 |
| enphase battery | 3,600 | 34 | $1.85 | 信息/交易 | Enphase 用户研究词 |
| solar battery installation | 3,600 | 34 | $10.04 | 信息 | ⭐ CPC $10 高，安装信息意图 |
| solar battery storage | 2,900 | 36 | $2.67 | 信息/商业 | 核心品类词 |
| whole home battery backup | 2,400 | 36 | $2.16 | 信息/商业 | 全宅备电场景 |
| home battery system | 2,900 | 38 | $2.60 | 信息/商业 | |
| home battery storage | 1,300 | 45 | $2.45 | 信息 | KD 偏高 |
| solar battery cost | 880 | 31 | $2.54 | 商业 | ⭐ 价格研究词 |
| home energy storage system | 590 | **29** | $2.49 | 信息/商业 | ⭐ KD 29，量够用 |
| solar plus storage | 170 | **31** | $2.92 | 信息 | ⭐ |
| generac pwrcell | 1,000 | **28** | $3.10 | 信息 | ⭐ 竞品词，KD 28 |
| sunpower sunvault | 90 | **26** | $4.58 | 商业 | ⭐ 小竞品词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| tesla powerwall | 22,200 | 84 | $3.91 | 导航/商业 | 品牌主词，KD 84 不可攻 |
| tesla powerwall cost | 6,600 | 52 | $2.50 | 信息 | KD 52，价格调研大词 |
| powerwall 3 | 2,900 | 60 | $4.08 | 信息 | KD 60，Tesla P1 |
| tesla powerwall 3 | 9,900 | 37 | $4.00 | 商业 | KD 37，量大，有攻击空间 |
| tesla powerwall price | 1,600 | 74 | $2.75 | 商业 | KD 74，不建议攻 |
| powerwall installation | 1,600 | **18** | $7.68 | 信息 | ⭐⭐ KD 18，量 1,600，超值低 KD 词 |
| powerwall 3 cost | 1,300 | **23** | $3.01 | 信息/商业 | ⭐ 量大 KD 低，价格关注用户 |
| how much is a tesla powerwall | 1,300 | 28 | $2.25 | 信息 | ⭐ 价格问题词，KD 28 |
| tesla powerwall installation cost | 720 | **25** | $5.05 | 信息 | ⭐ 安装成本词，CPC $5 高 |
| tesla powerwall review | 480 | **12** | $2.43 | 信息/商业 | ⭐ KD 12，评测意图 |
| powerwall review | 20 | 0 | $0.00 | — | GEO 级别 |
| is tesla powerwall worth it | 110 | **11** | $4.14 | 信息 | ⭐ 购买犹豫词，KD 11 |
| how long does a tesla powerwall last | 170 | **14** | $3.17 | 信息 | ⭐ 寿命关注词 |
| how many powerwalls do i need | 140 | **13** | $4.03 | 信息 | ⭐ 规划类词 |
| powerwall without solar | 110 | **19** | $3.45 | 信息 | ⭐ 无光伏用户场景 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| how to connect powerwall 3 to home assistant | 320 | **10** | $0.00 | 信息 | ⭐⭐⭐ 用户被 PW3 无本地 API 卡住，精准需求 |
| enphase home assistant | 90 | **16** | $0.00 | 信息/商业 | ⭐ Enphase 用户想接 HA，同一痛点 |
| powerwall home assistant | 20 | 0 | $0.00 | — | GEO 前哨，体量小但精准 |
| tesla powerwall home assistant | 20 | 0 | $0.33 | — | GEO 前哨 |
| tesla powerwall api | 30 | 0 | $0.00 | — | 开发者需求词，搜索 PW3 API 方案 |
| home battery storage without cloud | 0 | 0 | $0.00 | — | GEO 前哨，隐私需求精准词 |
| solar battery open source | 0 | 0 | $0.00 | — | GEO 前哨 |
| home battery local api | 0 | 0 | $0.00 | — | GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Tesla Powerwall 3 是市场上最强的云锁定储能产品——本地 API 已被完全封堵。Olares + HA 切入点有两条：① 充当统一能源枢纽（即使 PW3 数据经 Tesla 云，本地自动化 + 汇聚 + 分析运行在 Olares 上）；② "Powerwall alternative"叙事——推荐更开放的电池方案（Enphase/Generac/DIY）搭配 HA on Olares 实现本地储能监控。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| tesla powerwall alternative | 480 | 7 | $1.86 | 核心切入词；对比 Powerwall 3 强云锁定，推更开放电池（Enphase/Generac）搭配 HA on Olares 实现本地可控的储能 + 能源自动化 | ⭐⭐⭐ |
| how to connect powerwall 3 to home assistant | 320 | 10 | $0.00 | 用户被 PW3 无本地 API 卡住；Olares + HA 可通过 pypowerwall Wi-Fi AP 桥接做有限本地读数，或接 Tesla Fleet API 统一到 HA Energy Dashboard on Olares | ⭐⭐⭐ |
| powerwall installation | 1,600 | 18 | $7.68 | 安装教程词覆盖量大；侧栏推 HA on Olares 作为配套能源 dashboard，不管装哪个品牌都能统一展示 | ⭐⭐ |
| powerwall 3 cost | 1,300 | 23 | $3.01 | 价格研究阶段；在对比文里点出"Powerwall 3 $15K+ 且无本地 API"，引出 Generac/Enphase + Olares HA 替代栈 | ⭐⭐ |
| tesla powerwall installation cost | 720 | 25 | $5.05 | 同上；高 CPC 说明高购买意图，内容末尾建议"搭配 Home Assistant on Olares 作为本地控制层" | ⭐⭐ |
| tesla powerwall review | 480 | 12 | $2.43 | 评测意图；客观评价 PW3（优：逆变器一体化/LFP；缺：无本地 API/数据上 Tesla 云）；文末引出 Olares HA 作为统一能源中枢 | ⭐⭐ |
| enphase vs tesla | 140 | 11 | $16.31 | 高价值对比词；CPC $16 说明购买决策阶段；Enphase 原生 HA 集成更本地化（enphase home assistant 90/月，KD 16），Olares 更容易做完整本地栈 | ⭐⭐⭐ |
| powerwall vs generac | 50 | 10 | $7.60 | 低 KD 对比词；Generac PWRcell + HA on Olares = 本地监控 + 自动化，Powerwall 3 做不到 | ⭐⭐ |
| tesla powerwall competitors | 720 | 17 | $2.46 | 量大 KD 低；综合对比文，附表列各竞品 HA/本地 API 支持情况，Olares HA 为中枢结论 | ⭐⭐ |
| is tesla powerwall worth it | 110 | 11 | $4.14 | 犹豫期用户；点出云锁定作为反方论点，提供 HA on Olares 本地替代思路 | ⭐⭐ |
| powerwall home assistant | 20 | 0 | $0.00 | GEO 词；精准命中 Powerwall 用户想接 HA 的需求，写完整教程（PW2 本地 / PW3 Fleet API / pypowerwall 桥接方案） | ⭐⭐⭐ |
| home battery storage without cloud | 0 | 0 | $0.00 | GEO 前哨；隐私敏感用户精准词，Olares + HA 是答案 | ⭐⭐ |
| solar battery local api | 0 | 0 | $0.00 | GEO 前哨；开发者/技术用户查询，pypowerwall + HA on Olares 是现有最佳本地方案 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| tesla powerwall alternative | 480 | **7** | $1.86 | 信息 | **主词候选** | ⭐ KD 7 是本报告最稀缺发现；量 480 加上同族词合计可达 700+；Olares 推"开放电池 + HA on Olares"替代叙事 |
| powerwall installation | 1,600 | **18** | $7.68 | 信息 | **主词候选** | ⭐ 量 1,600 远超同 KD 词；安装教程文自然引出 HA on Olares 配套方案 |
| tesla powerwall competitors | 720 | 17 | $2.46 | 信息 | **主词候选** | ⭐ 量 720，KD 17；综合对比文，列各品牌 HA 本地 API 支持情况，Olares HA 为结论 |
| tesla powerwall 3 | 9,900 | 37 | $4.00 | 商业 | **主词候选** | 量 9,900，KD 37 勉强可攻；深度产品分析文切入，PW3 无本地 API 是核心差异化叙事 |
| powerwall 3 cost | 1,300 | **23** | $3.01 | 信息/商业 | **主词候选** | ⭐ 价格透明文，量 1,300，KD 23；文中引出 HA on Olares 作为配套本地控制层 |
| how to connect powerwall 3 to home assistant | 320 | **10** | $0.00 | 信息 | **主词候选** | ⭐⭐⭐ KD 10，量 320；用户痛点精准——PW3 本地 API 死亡后如何接 HA；Olares + pypowerwall 桥接 + Fleet API 全解 |
| enphase vs tesla | 140 | **11** | $16.31 | 信息/商业 | **主词候选** | ⭐ CPC $16 说明高购买价值；KD 11；Enphase 更开放本地 API 更友好，Olares HA 体现出差异 |
| tesla powerwall review | 480 | **12** | $2.43 | 信息/商业 | **主词候选** | ⭐ KD 12，量 480；评测文切入，优缺点客观分析（云锁定是缺点），文末 Olares HA 方案 |
| how much is a tesla powerwall | 1,300 | 28 | $2.25 | 信息 | **主词候选** | ⭐ 量 1,300，KD 28；价格文，附总拥有成本计算（含维护/云捆绑），对比方案 |
| tesla powerwall installation cost | 720 | **25** | $5.05 | 信息 | **主词候选** | ⭐ 安装成本词；量 720，KD 25，CPC $5；购买决策阶段 |
| generac pwrcell | 1,000 | **28** | $3.10 | 信息 | **次级** | ⭐ Generac 用户词，量 1,000，KD 28；并入替代品对比文 |
| powerwall vs generac | 50 | **10** | $7.60 | 信息/商业 | **次级** | ⭐ KD 极低，CPC $7.6；并入对比文的细节章节 |
| is tesla powerwall worth it | 110 | **11** | $4.14 | 信息 | **次级** | ⭐ 犹豫期词；并入评测文 |
| enphase home assistant | 90 | **16** | $0.00 | 信息/商业 | **次级** | ⭐ 与 powerwall home assistant 同族，Enphase 用户找 HA 方案；并入 HA 集成教程文 |
| how long does a tesla powerwall last | 170 | **14** | $3.17 | 信息 | **次级** | ⭐ 寿命/可靠性词；并入评测文 FAQ 章节 |
| how many powerwalls do i need | 140 | **13** | $4.03 | 信息 | **次级** | ⭐ 规划类词；并入安装/成本文 |
| powerwall home assistant | 20 | 0 | $0.00 | — | **次级/GEO** | 精准用户词；并入 HA 集成教程文，GEO 布局优先 |
| tesla powerwall api | 30 | 0 | $0.00 | — | **GEO** | 开发者/技术用户查询 PW3 API 替代方案；pypowerwall + Olares HA 最完整回答 |
| home battery storage without cloud | 0 | 0 | $0.00 | — | **GEO** | 隐私需求精准词，Olares HA 本地栈是答案 |
| powerwall 3 local api | 0 | 0 | $0.00 | — | **GEO** | PW3 本地 API 废止搜索，高意图技术用户 |
| home battery no subscription | 0 | 0 | $0.00 | — | **GEO** | 无订阅诉求词（Powerwall 无订阅但云锁定），开放方案更彻底 |

---

## 核心洞见

1. **品牌护城河**：`tesla powerwall`（KD 84）、`tesla powerwall cost`（KD 52）、`powerwall 3`（KD 60）均是无法正面攻打的品牌词。Tesla 官网 P1 全覆盖，且品牌心智极强（"Powerwall"已近乎品类名）。**不建议正面刚品牌导航词**；攻击面在替代/对比词、安装/成本信息词、以及 HA 集成痛点词上。

2. **可复制的打法**：Tesla 储能官网内容极简（以产品规格和报价 CTA 为主），**几乎没有信息类内容**（无安装详解、无对比文、无 API 文档）——这是竞品内容矩阵的巨大空白。可复制策略：写深度信息文（安装成本细分、PW3 vs 竞品对比、HA 集成教程），覆盖 Tesla 官网无法覆盖的长尾查询。

3. **对 Olares 最关键的 3 个词**：
   - **`tesla powerwall alternative`**（480/月，KD 7）：全报告最高价值词，KD 极低+量够用+购买意图强，Olares HA 替代叙事完美命中
   - **`how to connect powerwall 3 to home assistant`**（320/月，KD 10）：痛点精准——用户被 PW3 无本地 API 卡住，写教程覆盖 pypowerwall 桥接 + Tesla Fleet API + Olares HA 方案
   - **`powerwall installation`**（1,600/月，KD 18）：量最大的低 KD 词，安装教程文尾部推 HA on Olares 作为能源监控配套层

4. **最大攻击面**：
   - **云锁定/本地 API 废止**：Tesla Powerwall 3 于 2025 年完全封堵本地 API——Gateway 本地 Web UI 消失、静态路由方法失效，HA 原生集成仅支持 Powerwall 2（官方已注明 PW3 "Unsupported"）。这是最强烈的用户痛点，Reddit/社区投诉量高。"Powerwall 3 home assistant"、"powerwall local api"等词背后是大量受挫用户。
   - **高价 + 安装商垄断**：Tesla 强制认证安装商，限制竞价、价格透明度低；$13,500–$16,800 的安装成本里有大量不透明利润。"is tesla powerwall worth it"（KD 11）是性价比质疑词的入口。
   - **VPP 数据依赖**：Tesla 要求参与虚拟电厂（VPP）的 Powerwall 必须通过云端 API，用户无法拒绝云端控制而同时享受 VPP 收益——隐私与收益的 trade-off 是话题。

5. **隐藏低 KD 金矿**：
   - `powerwall installation`（1,600/月，KD 18）：量是同赛道最高的 KD<20 词，安装教程文覆盖
   - `tesla powerwall review`（480/月，KD 12）+ `is tesla powerwall worth it`（110/月，KD 11）：评测族合计约 700/月，KD 极低，Tesla 官网无评测内容
   - `enphase vs tesla`（140/月，KD 11，CPC $16.31）：CPC $16 说明金融价值极高，对比文覆盖
   - `how to connect powerwall 3 to home assistant`（320/月，KD 10）：技术教程词，精准匹配 HA 用户群

6. **GEO 前瞻布局**（AI Overview / Perplexity 引用位）：
   - `"does tesla powerwall 3 have a local api"` —— 高频技术问答，AI 综述直接引用场景
   - `"tesla powerwall 3 home assistant setup"` —— HA 用户求助 PW3 集成，Perplexity 高引用词型
   - `"powerwall alternative without cloud"` —— 隐私敏感用户精准词，Olares 是直接答案
   - `"home battery storage local monitoring"` —— 本地监控需求词，专业用户 AI 查询
   - `"powerwall vs enphase privacy"` —— 数据主权对比，AI 摘要型内容

7. **与既有 `olares-500-keywords` 词表的关联**：本赛道词与 Home Assistant 能源监控系列词高度重叠（home assistant energy monitor / home assistant energy dashboard 等），可与 [sense-energy.md](/Users/pengpeng/seo/directions/iot/reports/02-hardware/energy-monitors/sense-energy.md) 报告联动——两者共用"能源监控本地化"叙事框架，Olares HA 作为统一宿主平台；Tesla Powerwall alternative + Emporia Vue/Shelly EM 合并可构成"complete local energy stack"主题内容矩阵。此外，"tesla powerwall alternative"的 KD 7 与 Sense energy 报告里"sense energy monitor alternative"（KD 0）同属替代词低 KD 机会族，可联合排期。

---

## 附：Powerwall 竞品本地 API 支持对比

| 品牌/型号 | 本地 API | HA 集成方式 | 数据主权 | 参考 |
|-----------|---------|------------|---------|------|
| **Tesla Powerwall 2** | ✅ 局域网本地轮询 | HA 官方集成（Local Polling）| 部分（网关在 LAN） | [HA integration](https://www.home-assistant.io/integrations/powerwall/) |
| **Tesla Powerwall 3** | ❌ 本地 API 已废止 | Tesla Fleet API（云授权）/ pypowerwall Wi-Fi AP 桥接（受限）| 极弱 | [GH issue #144251](https://github.com/home-assistant/core/issues/144251) |
| **Enphase IQ Battery** | 🟡 有限（IQ Gateway 本地 API，部分）| HA 非官方集成 | 中（局域网部分可读）| [enphase HA community](https://community.home-assistant.io/) |
| **Generac PWRcell** | 🟡 有限（PWRview 本地网络读数）| 第三方 HACS 集成 | 中 | 社区 |
| **FranklinWH aPower** | ❌ 云依赖 | 无官方 HA 集成 | 弱 | — |
| **DIY (EG4/Growatt + ESPHome)** | ✅ 完全本地 | HA 直接 Modbus/MQTT | 完全 | 社区 |

> **Olares 在栈中的位置**：运行 Home Assistant 的宿主平台。Powerwall 2 用户可局域网直连 HA on Olares；Powerwall 3 用户可通过 pypowerwall Wi-Fi AP 桥（树莓派中继）或 Tesla Fleet API 接入 HA Energy Dashboard，所有自动化、历史数据留在本地 Olares；最彻底的隐私方案是替换为本地 API 开放的电池（EG4/DIY）+ Olares HA 全栈本地控制。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_subdomains`、`phrase_these`、`phrase_related`、`phrase_questions`）| 2026-07-06*
*搜索量为美国月均；储能品类为北美消费市场，全球量倍数相对有限（参考：IoT/太阳能品类全球量约为美国的 2-3 倍）。*
*补充来源：tesla.com/powerwall 官网、HA Powerwall 集成页（home-assistant.io）、GitHub core issue #144251、Teslemetry 控制限制说明（2026-01-02 更新）、AgentSolar 安装报价份额数据（2026）、SolarReviews 2026 pricing。*
