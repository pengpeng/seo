# Sense SEO 竞品分析报告

> 域名：sense.com | SEMrush US | 2026-07-06
> 全宅能耗监测品牌，以云端 ML 设备指纹识别为差异化；2025 年底已停止直销硬件、全面转型为公用事业智能电表内嵌模式。

---

## 项目理解（前置）

Sense 由机器学习专家于 2013 年在剑桥 MA 创立，核心产品是安装在配电板的全宅能耗监测器：通过两只 CT 电流钳和电压传感器，以每秒数百万次采样的精度捕获电气波形，再将数据上传至 Sense 云端，用 ML 模型识别各类家电的"电气指纹"——这是 Sense 的核心差异化。该产品曾覆盖超过 10 万户美国家庭。**关键转折：Sense 于 2025 年 12 月 31 日停止直销硬件，完全转型为将 Sense 软件内嵌进公用事业智能电表的 B2B 模式**；现有 Monitor 用户继续获得 App 和固件支持。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 云端 ML 设备识别的全宅能耗监测品牌（硬件已停售，转型智能电表内嵌） |
| 开源 / 许可证 | 闭源商业产品（硬件 + 云服务）；社区存在非官方 Python API 库 |
| 主仓库 | 无公开官方仓库；非官方 [sense-energy/sense-energy-monitor](https://github.com/sense-energy/sense-energy-monitor)（Python 库） |
| 核心功能 | 全宅实时功率曲线、云端 ML 家电识别（电气指纹）、用电成本追踪、设备级异常告警、HA/SmartThings 集成（云轮询） |
| 商业模式 / 定价 | 历史：硬件约 $299，无订阅费，云服务含在硬件价内。现在：硬件停售，仅通过公用事业合作伙伴免费获取（智能电表方案） |
| 差异化 / 价值主张 | **唯一**：ML 设备指纹识别无需手动标定回路，自动识别冰箱/热水器/烘干机等；缺点：识别准确率有限、数据完全在云端、无本地 API |
| 主要竞品（初判）| Emporia Vue、IoTaWatt、Shelly EM、Eyedro |
| Olares Market | 未上架（闭源硬件，且已停售）；本地平替栈 = Emporia Vue + ESPHome + Home Assistant（Home Assistant 已在 Olares Market：[home-assistant.md](/Users/pengpeng/seo/directions/market/reports/home-assistant.md)） |
| 来源 | [sense.com/about](https://sense.com/about/)、[停售公告](https://sense.com/consumer-blog/looking-ahead-the-next-chapter-for-sense/)、[Latitude Media 报道](https://www.latitudemedia.com/news/is-the-era-of-direct-to-consumer-energy-hardware-coming-to-a-close/)、[Grokipedia 规格页](https://grokipedia.com/page/Sense_Energy_Monitor) |

---

## 流量基线（Phase 1）

> 注：本次调用计划不包含 `domain_overview`（SEMrush Rank / 总关键词数），以下来自 `domain_organic_subdomains` + `resource_organic`。

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | sense.com |
| SEMrush Rank | — （plan 不含 domain_overview） |
| 自然关键词数（全子域合计估算）| ~5,002 |
| 月自然流量（US，全子域合计）| ~18,975 |
| 自然流量估值 | — |
| 付费关键词数 | 0（无 Google Ads 投放） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 品牌词为主，大量 P1（见下表） |
| 排名 4-10 位 | 信息博客词，"electrical panel""what is a watt"等 |
| 排名 11-20 位 | 中长尾能耗品类词 |

> 流量规模对比参考：~19K/月属于**小流量垂类品牌**，考虑到"sense"一词极度多义（BI 工具、感官、常识等），品牌词稀释严重。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| sense.com | 3,443 | 17,989 | 94.78% |
| home.sense.com | 32 | 331 | 1.74% |
| community.sense.com | 1,013 | 306 | 1.61% |
| help.sense.com | 476 | 299 | 1.58% |
| content.sense.com | 38 | 50 | 0.26% |

> 洞察：`community.sense.com` 以 1,013 个关键词排第二但流量仅 1.6%，说明社区帖子多为长尾低流量词（含用户疑难、设备识别失败讨论等），是竞争渗透切入点。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| sense | 5 | 60,500 | 50 | $0.78 | 1,815 | 信息 | sense.com/press/ |
| sense energy monitor | 1 | 1,600 | 34 | $0.67 | 1,280 | 导航/信息 | sense.com/ |
| sense electricity monitor | 1 | 1,300 | 33 | $0.56 | 1,040 | 导航/信息 | sense.com/ |
| what is a watt | 2 | 5,400 | 26 | $0.07 | 442 | 信息 | sense.com/consumer-blog/... |
| electrical panel | 4 | 12,100 | 40 | $2.87 | 266 | 信息 | sense.com/consumer-blog/... |
| energy monitor sense | 1 | 320 | 40 | $0.58 | 256 | 导航 | sense.com/ |
| sense power monitor | 1 | 320 | 45 | $0.51 | 256 | 导航 | sense.com/ |
| watt what is | 4 | 6,600 | 35 | $0.07 | 231 | 信息 | sense.com/consumer-blog/... |
| sense monitor | 1 | 260 | 36 | $0.75 | 208 | 导航 | sense.com/ |
| sense home energy monitor | 1 | 720 | 38 | $0.85 | 178 | 信息/导航 | sense.com/ |
| smart home energy management | 7 | 8,100 | 28 | $2.52 | 153 | 信息 | sense.com/ |
| sense energy | 1 | 170 | 44 | $6.44 | 136 | 导航 | sense.com/ |
| sense home energy monitor login | 1 | 170 | 19 | $0.00 | 136 | 导航/交易 | home.sense.com/labs |
| home energy monitor | 2 | 1,600 | 29 | $0.77 | 131 | 信息 | sense.com/ |
| electric panel | 3 | 3,600 | 28 | $2.87 | 108 | 信息/商业 | sense.com/consumer-blog/... |
| current transformer | 3 | 2,900 | 17 | $2.31 | 101 | 信息 | sense.com/consumer-blog/... |
| sense power monitoring | 1 | 110 | 36 | $0.62 | 88 | 导航 | sense.com/ |
| sense energy monitoring | 1 | 110 | 35 | $0.67 | 88 | 导航 | sense.com/ |
| energy monitor | 3 | 1,900 | 40 | $0.78 | 83 | 信息 | sense.com/ |
| home energy monitor system | 1 | 320 | 31 | $1.50 | 79 | 信息 | sense.com/ |
| smart home energy management | 7 | 8,100 | 28 | $2.52 | 153 | 信息 | sense.com/ |
| sense login | 1 | 320 | 9 | $0.00 | 79 | 导航/交易 | home.sense.com/dashboard |
| whole home energy monitor | 3 | 880 | 28 | $0.49 | 72 | 信息 | sense.com/ |
| whole house energy monitor | 2 | 880 | 34 | $0.72 | 72 | 信息 | sense.com/ |
| home energy monitoring system | 2 | 720 | 26 | $1.50 | 59 | 信息 | sense.com/ |
| smart energy monitor | 1 | 140 | 12 | $0.94 | 34 | 信息 | sense.com/ |

> 观察：流量高度集中于品牌词（sense/sense energy monitor 等）；信息博客（what is a watt / electrical panel / current transformer）带来的流量比品类词更大，说明 Sense 内容策略以科普能源常识为流量入口。

### 付费词（Google Ads）

Sense **无 Google Ads 投放**（resource_adwords 返回空数据）。这在硬件已停售的背景下完全合理——品牌重心已从 DTC 转向 B2B 公用事业合作。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| emporia vue | 2,900 | 34 | $0.57 | 商业/交易 | 最大的直接替代词；Sense 停售后需求上升 |
| emporia vue 3 | 1,300 | 16 | $0.51 | 商业 | ⭐ Sense 停售后的首选替代硬件，KD 极低 |
| iotawatt | 880 | 33 | $0.58 | 导航 | 开源硬件替代；精度更高但价格更贵 |
| shelly em | 590 | 13 | $0.31 | 商业/交易 | ⭐ 全宅监测低成本替代；本地 API，无需 flash |
| emporia vue home assistant | 170 | 24 | $0.77 | 商业 | ⭐ 核心 Olares 机会词 |
| sense energy monitor review | 90 | 20 | $0.56 | 信息/商业 | ⭐ 低 KD，评测文高流量场景 |
| emporia vs sense energy monitor | 20 | 0 | $0.00 | 信息 | 直接对比词，低量但高意图 |
| sense energy monitor alternative | 20 | 0 | $0.62 | 商业 | 停售后预计增量 |
| sense vs emporia vue | 20 | 0 | $0.00 | 信息 | 直接对比词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| smart home energy management | 8,100 | 41 | $2.52 | 信息 | 最大品类词，KD 略高 |
| electricity usage monitor | 1,900 | 22 | $0.73 | 商业/信息 | ⭐ 大量低 KD，plug-in 和全宅都适用 |
| energy monitor | 1,900 | 39 | $0.77 | 信息 | 品类主词，KD 较高 |
| power usage monitor | 1,900 | 21 | $0.73 | 信息 | ⭐ 与 electricity usage monitor 同义近义 |
| home energy monitor | 1,600 | 29 | $0.77 | 信息 | ⭐ 核心品类词，KD 29 |
| whole house energy monitor | 880 | 34 | $0.72 | 信息 | 全宅覆盖词，Sense/Vue 都适用 |
| whole home energy monitor | 880 | 28 | $0.49 | 信息 | ⭐ 与上词合计 1,760/月 |
| energy consumption monitor | 720 | 27 | $0.73 | 信息 | ⭐ |
| home energy monitoring system | 720 | 26 | $1.50 | 信息 | ⭐ |
| smart home energy monitor | 720 | 23 | $0.65 | 商业/信息 | ⭐ |
| best home energy monitor | 480 | 28 | $0.72 | 信息 | ⭐ 导购词，Olares 内容机会 |
| home energy monitoring | 480 | 25 | $0.67 | 信息 | ⭐ |
| home assistant energy monitor | 210 | 25 | $0.57 | 商业 | ⭐ Olares 核心机会词 |
| home assistant energy dashboard | 140 | 20 | $0.00 | 商业 | ⭐ 极低 KD；HA 用户在找配置指南 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| sense energy monitor | 1,600 | 34 | $0.67 | 导航/信息 | 品牌导航为主 |
| sense home energy monitor | 480 | 41 | $0.58 | 信息/导航 | |
| emporia energy monitor | 720 | 26 | $0.52 | 商业/交易 | ⭐ 可撬入 |
| sense energy monitor review | 90 | 20 | $0.56 | 信息/商业 | ⭐ |
| sense flex home energy monitor | 40 | 21 | $0.45 | 商业 | ⭐ Flex 型号词 |
| sense energy monitor with solar | 30 | 13 | $1.17 | 商业 | ⭐ 太阳能用户词 |
| sense energy monitor api | 20 | 0 | $0.00 | 信息 | 开发者需求，有社区非官方库 |
| reddit sense energy monitor | 20 | 0 | $0.00 | 信息 | Reddit 舆情词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home assistant energy monitor | 210 | 25 | $0.57 | 商业 | ⭐ 主力词 |
| home assistant energy dashboard | 140 | 20 | $0.00 | 商业 | ⭐ 配置需求词 |
| emporia vue home assistant | 170 | 24 | $0.77 | 商业 | ⭐ 核心栈词 |
| emporia vue esphome | 40 | 11 | $0.00 | 商业 | ⭐ ESPHome flash 需求，KD 极低 |
| shelly energy monitor | 70 | 20 | $0.19 | 信息 | ⭐ Shelly 本地 API 用户 |
| iotawatt home assistant | 20 | 0 | $0.00 | 信息 | GEO 级别，IoTaWatt 用户找 HA 方案 |
| home energy monitor open source | 0 | 0 | $0.00 | 信息 | GEO 前哨，语义高度契合 |
| energy monitor home assistant | 20 | 0 | $0.61 | 商业 | GEO 前哨 |
| home energy monitor no subscription | 0 | 0 | $0.00 | 信息 | GEO 前哨，停订阅痛点词 |

---

## Olares 关联词（Phase 3）

**核心逻辑**：Sense 硬件已于 2025 年底停售，其云端 ML 设备识别是护城河也是主要痛点（数据全在云上）。本地平替栈 = Emporia Vue + ESPHome + Home Assistant on Olares——电路级实时监测完全本地，无云依赖；诚实代价是失去 Sense 的 AI 自动识别家电能力。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| home energy monitor | 1,600 | 29 | $0.77 | Home Assistant on Olares + Emporia Vue = 全宅本地能耗监测；对比 Sense：无 AI 识别，但电路级精度更高且数据不离本地 | ⭐⭐⭐ |
| best home energy monitor | 480 | 28 | $0.72 | 导购型词，可写 Sense vs Emporia Vue vs IoTaWatt 对比；推 Olares 本地栈给隐私敏感用户 | ⭐⭐⭐ |
| emporia vue home assistant | 170 | 24 | $0.77 | 直接命中：Emporia Vue 刷 ESPHome → HA on Olares，5 秒轮询全路由监控，完全离线 | ⭐⭐⭐ |
| home assistant energy dashboard | 140 | 20 | $0.00 | HA 能源仪表盘配置指南；接入 Vue/IoTaWatt 传感器，在 Olares 上展示本地数据 | ⭐⭐⭐ |
| home assistant energy monitor | 210 | 25 | $0.57 | 主力词；HA 能源监测教程，顺带介绍 Olares 作为 HA 运行平台 | ⭐⭐⭐ |
| emporia vue esphome | 40 | 11 | $0.00 | KD 极低实操词：如何给 Emporia Vue 刷 ESPHome + 接入 HA on Olares | ⭐⭐⭐ |
| sense energy monitor alternative | 20 | 0 | $0.62 | Sense 停售后搜索量将增；Emporia Vue + Olares HA 是最直接的回答 | ⭐⭐⭐ |
| sense energy monitor review | 90 | 20 | $0.56 | 评测词可扩展为"Sense 已停售，2026 最佳替代方案"内容 | ⭐⭐ |
| shelly energy monitor | 70 | 20 | $0.19 | Shelly EM 本地 API，无需 flash；与 HA on Olares 直接集成，比 Sense 更简单 | ⭐⭐ |
| iotawatt | 880 | 33 | $0.58 | IoTaWatt 开源硬件，精度更高，直接接 HA；Olares 可作 HA 宿主 | ⭐⭐ |
| home energy monitor no subscription | 0 | 0 | $0.00 | GEO 词；Sense 无订阅是优点，但 Vue+HA 方案完全免费运营，更彻底 | ⭐⭐ |
| home energy monitor open source | 0 | 0 | $0.00 | GEO 词；IoTaWatt + ESPHome 生态是真开源方案 | ⭐⭐ |
| energy monitoring local only | 0 | 0 | $0.00 | GEO 词；隐私敏感用户词，Olares 是答案 | ⭐⭐ |
| smart home energy management | 8,100 | 41 | $2.52 | 大词但 KD 高；Olares HA 是智能家居能源中枢，可打 FAQ 占位 | ⭐ |
| whole home energy monitor | 880 | 28 | $0.49 | 品类词，Emporia Vue + Olares 是本地全宅方案 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| home energy monitor | 1,600 | 29 | $0.77 | 信息 | 主词候选 | KD 29 低于 30，量充足；对比文"sense already discontinued"切入；Olares 推本地 HA 栈 |
| emporia vue | 2,900 | 34 | $0.57 | 商业/交易 | 主词候选 | 量最大，KD 34 可攻；Vue 是 Sense 停售后最多人搜的替代品；Olares + ESPHome 是完整技术栈 |
| electricity usage monitor | 1,900 | 22 | $0.73 | 商业/信息 | 主词候选 | ⭐ KD 22 是全品类最低机会词之一；量 1,900，plug-in 到全宅均覆盖 |
| power usage monitor | 1,900 | 21 | $0.73 | 信息 | 主词候选 | ⭐ 同上，与 electricity usage monitor 可共文 |
| best home energy monitor | 480 | 28 | $0.72 | 信息 | 主词候选 | ⭐ 导购词，Sense 停售后信息真空；写"2026 best home energy monitor"对比文，Olares 本地栈为结论 |
| whole home energy monitor | 880 | 28 | $0.49 | 信息 | 主词候选 | ⭐ 量 880，KD 28；与 whole house energy monitor（880）合计 1,760 |
| iotawatt | 880 | 33 | $0.58 | 导航 | 主词候选 | 量与 KD 适中；开源用户群有 Olares 自部署意愿 |
| home assistant energy monitor | 210 | 25 | $0.57 | 商业 | 主词候选 | ⭐ 核心 Olares 机会词，量 210，KD 25；直接写 HA 能源监测配置教程 |
| emporia vue home assistant | 170 | 24 | $0.77 | 商业 | 主词候选 | ⭐ 量 170，KD 24；最精准的 Olares 角度词——Vue+HA on Olares 完整方案 |
| home assistant energy dashboard | 140 | 20 | $0.00 | 商业 | 主词候选 | ⭐ KD 20 极低，量 140；配置类教程文，高完成率 |
| smart home energy management | 8,100 | 41 | $2.52 | 信息 | 次级 | 量最大但 KD 41；作为上述对比文的次级词并入 |
| emporia vue esphome | 40 | 11 | $0.00 | 商业 | 次级 | ⭐ KD 极低实操词；并入 emporia vue home assistant 文章的实操章节 |
| sense energy monitor review | 90 | 20 | $0.56 | 信息/商业 | 次级 | ⭐ KD 20；评测词自然引出"2026 已停售，现在怎么办" |
| shelly em | 590 | 13 | $0.31 | 商业/交易 | 次级 | ⭐ KD 13 极低，量 590；Shelly 本地 API 免 flash 替代方案；并入比较文 |
| shelly energy monitor | 70 | 20 | $0.19 | 信息 | 次级 | ⭐ 与 shelly em 合并 |
| sense energy monitor alternative | 20 | — | $0.62 | 商业 | 次级/GEO | 停售后需求将涨；现在量小，Sense 老用户迁移意图强 |
| sense vs emporia vue | 20 | — | $0.00 | 信息 | GEO | 量小但完美命中对比意图；FAQ 占位 |
| energy monitor home assistant | 20 | — | $0.61 | 商业 | GEO | 近零量但语义精准；AI Overview 引用位值得布局 |
| home energy monitor open source | 0 | — | $0.00 | 信息 | GEO | 近零量但 Olares 最直接答案；FAQ/前瞻段布局 |
| home energy monitor no subscription | 0 | — | $0.00 | 信息 | GEO | Sense 无订阅是亮点，但本地栈更彻底；抢引用位 |
| iotawatt home assistant | 20 | — | $0.00 | 信息 | GEO | IoTaWatt 专项小众词；社区内容渗透 |

---

## 核心洞见

1. **品牌护城河**：Sense 品牌词（sense energy monitor、sense home energy monitor）P1 占据，但流量总量极小（~19K/月 US），且**硬件已停售**——护城河正在溃坝。品牌词 CPC 低（$0.67），说明竞品不在买。"sense" 主词本身多义、流量分散。**不建议正面刚品牌词**；攻击面在品类词和替代词。

2. **可复制的打法**：Sense 内容策略最有效的是**信息科普带流量**（what is a watt 5,400 量 P2 排名，electrical panel 12,100 量 P4 排名），说明能耗/电力科普词 KD 普遍低、流量价值高——Olares 内容可复制"能源基础知识"内容矩阵，末尾锚定本地监测方案。

3. **对 Olares 最关键的词**：
   - **`home energy monitor`**（1,600/月，KD 29）：品类核心词，Sense 停售后有信息真空，对比文切入
   - **`emporia vue home assistant`**（170/月，KD 24）：最精准的技术栈词，直接命中"想要本地 HA 集成的人"
   - **`best home energy monitor`**（480/月，KD 28）：导购型词，2026 Sense 停售更新信息真空极大

4. **最大攻击面**：
   - **硬件停售**：Sense 已于 2025 年底停止销售实体产品，大量现有用户和潜在买家正在寻找替代方案，搜索词如 "sense alternative" / "sense vs emporia vue" 需求上升趋势明确
   - **云依赖**：Sense 所有 ML 识别在云端，数据不能离网。家庭网络中断则 app 数据中断；数据主权零保证
   - **地域限制**：仅支持北美 120/240V 单相面板，欧洲/亚洲用户无法使用
   - **无 Home Assistant 本地集成**：Sense HA 集成依赖云轮询，不是本地 API——这是 Reddit/社区最高频投诉之一

5. **隐藏低 KD 金矿**：
   - `electricity usage monitor`（1,900/月，KD 22）+ `power usage monitor`（1,900/月，KD 21）——合计 3,800/月，KD 均 < 25，且 Sense/大竞品均未专门针对这两个词写落地页
   - `emporia vue 3`（1,300/月，KD 16）——型号词极低 KD，Sense 停售后 Vue 3 是首要替代，写详细 Vue 3 + Olares HA 配置文
   - `home assistant energy dashboard`（140/月，KD 20，CPC=$0）——配置教程型词，KD 极低，HA 能源仪表盘文章

6. **GEO 前瞻布局**（AI Overview / Perplexity 引用位）：
   - `"sense energy monitor discontinued alternative"` —— Sense 停售是近期重大事件，AI 综述类问答高频场景
   - `"home energy monitor no cloud"` / `"local home energy monitoring"` —— 隐私敏感用户的精准需求
   - `"emporia vue vs sense"` —— 标准对比问答，Perplexity 高引用词型
   - `"home energy monitor open source"` —— 专业用户词，IoTaWatt/ESPHome 生态答案，顺带推 Olares HA
   - `"energy monitoring home assistant setup"` —— 配置类教程的 AI 摘要高引用场景

7. **与既有 `olares-500-keywords` 词表的关联**：home energy monitoring 系列词与 Home Assistant 相关词有较强关联，可与 [home-assistant.md](/Users/pengpeng/seo/directions/market/reports/home-assistant.md) 报告联动；本赛道词量整体偏小（US 月均 100-2,000 级别），但 KD 普遍低（大量 KD < 30），**总簇合计量**（electricity usage monitor + power usage monitor + home energy monitor + best home energy monitor + whole home/house energy monitor ≈ 8,760/月）和竞争难度比看起来更好；IoTaWatt 词（880/月）和 Shelly EM 词（590/月）可扩展到更广的 DIY 自托管智能家居生态内容。

---

## 附：本地平替技术栈参考

| 方案 | 硬件价 | 云依赖 | HA 集成 | 电路级 | 难度 |
|------|--------|--------|---------|--------|------|
| **Emporia Vue 3 + ESPHome** | $99–$200 | 无（刷固件后） | 5 秒本地推送 | 最多 16 路 | 中（需 flash ESP32） |
| **Emporia Vue 3 原厂固件** | $99–$200 | 有（Emporia 云） | 云轮询 | 最多 16 路 | 低 |
| **IoTaWatt** | ~$100–$200 | 无 | 本地 API | 最多 14 路 | 低（开源固件自带本地 web） |
| **Shelly EM** | ~$30–$60 | 无（本地模式）| 本地 API/MQTT | 2 路（全宅级） | 低 |
| **Sense（停售）** | ~$299（已下架） | 全部 | 云轮询 | 仅整体（ML 识别单设备） | 低（安装）/高（云依赖） |

> **Olares 在栈中的位置**：运行 Home Assistant 的宿主平台。数据从 Vue/IoTaWatt/Shelly 通过局域网直接推送到 HA，所有能耗历史记录、自动化规则都在用户本地。HA on Olares 还可接入 LLM（Ollama）分析用能模式，这是 Sense 云端 ML 的本地化平替思路（精度有差，但数据不离网）。

---

*数据来源：SEMrush US 数据库（`resource_organic`、`domain_organic_subdomains`、`phrase_these`、`phrase_related`、`phrase_fullsearch`、`phrase_questions`、`phrase_kdi`）| 2026-07-06*
*搜索量为美国月均；IoT 垂类产品全球量通常为美国的 2-3 倍。*
*补充来源：sense.com 官网、停售公告（2025-11）、Latitude Media 报道、emporia-vue-local/esphome GitHub（★755）、Emporia Energy 官方规格。*
