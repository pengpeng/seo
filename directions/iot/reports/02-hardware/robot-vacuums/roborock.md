# Roborock SEO 竞品分析报告

> 域名：roborock.com | SEMrush US | 2026-07-06
> 全球扫地机出货量连续第一的北京上市公司（SHSE:688169），闭源云依赖是最大隐私攻击面，Valetudo root 可去云本地化，Olares 以 HA MQTT 联动切入。

---

## 项目理解（前置）

Roborock（石头科技，688169.SH）2014 年创立于北京，2021 年在上交所科创板上市，是全球出货量连续排名第一的扫地机器人品牌（IDC 数据，2023 年起连续）。截至 2025 年底，全球累计销售超 2500 万台，产品销往 170 余个国家，年收入 186.95 亿人民币（+56.51% YoY）。设备依赖 LiDAR/视觉 SLAM 建立户型地图，地图数据默认上传至 Roborock 云端服务器（中国用户→国内服务器；欧洲用户→AWS Frankfurt；美国用户→区域云），这是其最核心的隐私攻击面。Valetudo 是专门针对 Roborock（及 Dreame 等品牌）的开源去云固件方案（Apache-2.0，GitHub ★9.3k），通过 root 设备后安装，使地图与清扫数据完全保留在本地，并通过 MQTT 与 Home Assistant 集成，无需连接厂商云。Olares 的切入点：HA 已上架 Olares Market，用户可在 Olares 上跑 HA + Valetudo MQTT 联动，实现"地图不出家门"的全本地控制链路。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 全球出货量第一的扫地机器人品牌，闭源云依赖（户型地图上传至中国/区域服务器） |
| 开源 / 许可证 | **闭源**商业产品；相关开源工具：Valetudo（Apache-2.0，去云固件）、Dustbuilder（构建工具） |
| 主仓库 | 无官方开源仓库；Valetudo：[Hypfer/Valetudo](https://github.com/Hypfer/Valetudo)（★9.3k） |
| 核心功能 | LiDAR SLAM 建图；自动集尘/洗拖布基站；AI 视觉障碍物识别；App 远程控制；多楼层地图 |
| 商业模式 / 定价 | 买断制硬件（S 系旗舰 $600-$1,500+，Q 系中端 $200-$500）；App 免费但需绑定云账户 |
| 差异化 / 价值主张 | 性能/技术领先（5轴机械臂 Saros Z70）；品控/做工佳；中高端性价比；但**地图数据强制云存储** |
| 主要竞品（初判）| iRobot（Roomba）、Dreame、Narwal、Ecovacs |
| Olares Market | 未上架（硬件品牌）；**Home Assistant 已上架** ✅，可通过 HA MQTT 联动 Valetudo |
| 来源 | [newsroom.roborock.com](https://newsroom.roborock.com/us/aboutus)、[global.roborock.com/pages/roborock-trust-center](https://global.roborock.com/pages/roborock-trust-center)、[Valetudo GitHub](https://github.com/Hypfer/Valetudo) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | roborock.com |
| SEMrush Rank | 8,620 |
| 自然关键词数 | 23,994 |
| 月自然流量（US）| 268,392 |
| 自然流量估值 | $361,052/月 |
| 付费关键词数 | 95 |
| 月付费流量 | 7,305 |
| 付费流量成本 | $8,457/月 |
| 排名 1-3 位 | 2,783 词 |
| 排名 4-10 位 | 2,826 词 |
| 排名 11-20 位 | 2,591 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| us.roborock.com | 14,818 | 252,242 | 93.98% |
| global.roborock.com | 1,586 | 5,956 | 2.22% |
| cn.roborock.com | 51 | 2,950 | 1.10% |
| support.roborock.com | 3,018 | 2,850 | 1.06% |
| garden.roborock.com | 185 | 1,515 | 0.56% |
| 其余（kr/newsroom/au/mall 等）| — | 2,680 | 1.00% |

> **洞见**：美国站（us.roborock.com）几乎独占所有 US 流量，support 子域名贡献 3k 关键词，SEO 机会在教程/维修词上也有分布。

### 官网 TOP 自然关键词（按流量排序，取前 30）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| roborock | 1 | 74,000 | 65 | $1.12 | 59,200 | 导航/品牌 | us.roborock.com/ |
| roborock vacuum | 1 | 12,100 | 53 | $1.03 | 9,680 | 商业 | /pages/robot-vacuums |
| robot vacuum and | 1 | 60,500 | 68 | $1.15 | 7,986 | 品类 | us.roborock.com/ |
| roborock saros 10r | 1 | 9,900 | 51 | $2.45 | 7,920 | 商业 | /products/roborock-saros-10r |
| roborock s8 maxv ultra | 1 | 8,100 | 56 | $1.97 | 6,480 | 商业 | /pages/roborock-s8-maxv-ultra |
| robot vacuum | 1 | 90,500 | 56 | $1.15 | 3,982 | 品类 | us.roborock.com/ |
| roborock cleaning solution | 1 | 4,400 | 34 | $0.66 | 3,520 | 商业 | /products/floor-cleaning-solution |
| roborock q revo | 1 | 4,400 | 46 | $1.50 | 3,520 | 商业 | /pages/robot-vacuums |
| autonomous vacuum | 1 | 22,200 | 81 | $1.15 | 2,930 | 品类 | us.roborock.com/ |
| roborock qrevo pro | 1 | 3,600 | 42 | $1.18 | 2,880 | 商业 | /products/roborock-qrevo-s-pro |
| roborock qrevo curv | 1 | 3,600 | 50 | $2.12 | 2,880 | 商业 | /pages/roborock-qrevo-curv-series |
| 石头科技 | 1 | 2,900 | 49 | $0.49 | 2,320 | 导航 | cn.roborock.com/ |
| roborock q5 | 1 | 2,900 | 45 | $0.98 | 2,320 | 商业 | /pages/roborock-q5 |
| roborock vacuum and mop | 1 | 2,900 | 42 | $1.12 | 2,320 | 品类 | us.roborock.com/ |
| roborock qrevo | 1 | 2,900 | 47 | $1.50 | 2,320 | 商业 | /products/qrevo |
| roborock robot vacuum | 1 | 2,400 | 55 | $1.13 | 1,920 | 品牌+品类 | /pages/robot-vacuums |
| robot vacuum and mop | 1 | 22,200 | 45 | $1.41 | 1,820 | 品类 | us.roborock.com/ |
| robot robotic vacuum cleaners | 1 | 40,500 | 80 | $1.15 | 1,782 | 品类 | us.roborock.com/ |
| roborock floor cleaning solution | 1 | 1,900 | 35 | $0.68 | 1,520 | 商业 | /products/floor-cleaning-solution |
| roborock qrevo curvx | 1 | 1,900 | 43 | $2.12 | 1,520 | 商业 | /products/roborock-qrevo-curv-x |
| roborock qrevo master | 1 | 1,900 | 39 | $1.62 | 1,520 | 商业 | /pages/roborock-qrevo-master |
| roborock saros 10r robot vacuum | 1 | 1,600 | 42 | $2.82 | 1,280 | 商业 | /products/roborock-saros-10r |
| roborock q10 s5 | 1 | 1,600 | 32 | $1.83 | 1,280 | 商业 | /products/roborock-q10-s5 |
| robot vaccum（拼写变体）| 1 | 4,400 | 42 | $1.15 | 1,091 | 品类 | us.roborock.com/ |
| roborock qrevo edge s5a | 1 | 880 | 37 | $2.73 | 704 | 商业 | /products/roborock-qrevo-edge-s5a |
| roborock floor cleaner solution | 1 | 880 | 32 | $0.68 | 704 | 商业 | /products/floor-cleaning-solution |
| best robot vacuum and mop | 8 | 33,100 | 51 | $1.40 | 628 | 品类 | us.roborock.com/ |
| robot vacum（拼写变体）| 1 | 2,400 | 52 | $1.15 | 595 | 品类 | us.roborock.com/ |
| roborock s7 max ultra | 1 | 1,000 | 50 | $1.14 | 800 | 商业 | /products/roborock-s7-max-ultra |
| roborock q7 max | 1 | 1,000 | 35 | $0.80 | 800 | 商业 | /products/roborock-q7-m5 |

> **洞见**：Roborock 在几乎所有自有品牌词和高竞争品类词（`robot vacuum`、`robot vacuum and mop`）上占据 #1，SEO 护城河极深。`best robot vacuum and mop`（月量 33.1k）仅排名 #8，是其相对薄弱点，竞争媒体站抢占了大量评测流量。

### 付费词（Google Ads，按流量排序）

Roborock 仅买 95 个付费词（月付费流量 7,305），策略保守——主要用于防御品牌词被竞品截流，以及新品（Saros 10r、Saros Z70）上市期的拉新推广，导向产品详情页和总店页。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| roborock | 74,000 | $1.03 | /collections/robot-vacuums |
| roborock vacuum | 12,100 | $1.15 | /pages/roborock-store |
| roborock s8 pro ultra | 4,400 | $1.27 | /products/roborock-saros-10r |
| robovac | 3,600 | $0.91 | /pages/roborock-store |
| roborock saros 10r | 9,900 | $2.45 | /products/roborock-saros-10r |
| saros z70 | 1,300 | $1.86 | /products/roborock-saros-z70 |
| roborock compare | 590 | $1.83 | /pages/robot-vacuum-cleaner-compare |
| 石头扫地机器人（中文） | 2,400 | $0.00 | /pages/roborock-store |

> Roborock 几乎不在竞品对比词（`vs roomba`、`roborock alternative`）上投广告——这正是 Olares 可以通过内容填补的缝隙。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| roborock vs roomba | 1,000 | 32 | $0.78 | 信息 | ⭐ 最大对比词；KD 低性价比高 |
| dreame vs roborock | 480 | 18 | $1.30 | 信息/商业 | ⭐ 竞品崛起，机会窗口 |
| roborock vs dreame | 390 | 26 | $1.31 | 信息/商业 | ⭐ 同上变体 |
| narwal vs roborock | 260 | 25 | $1.10 | 信息 | ⭐ 洗地机方向 |
| roomba alternative | 170 | 40 | $0.81 | 商业 | iRobot Chapter 11 后需求激增 |
| roborock alternative | 10 | 0 | $0.90 | 商业 | ⭐ GEO 前哨（量极小但语义精准） |
| best robot vacuum | 49,500 | 50 | $1.00 | 商业 | 量大但 KD 高，竞争媒体站把持 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| robot vacuum | 90,500 | 56 | $1.15 | 品类 | Roborock 自己已排 #1；高竞争 |
| robot vacuum and mop | 22,200 | 45 | $1.41 | 品类 | Roborock 排 #1 |
| best robot vacuum and mop | 33,100 | 51 | $1.40 | 商业 | Roborock 排 #8，媒体站为主 |
| robot vacuum without wifi | 140 | 10 | $0.48 | 信息 | ⭐ 低竞争，隐私人群 |
| robot vacuum home assistant | 70 | 9 | $0.00 | 信息 | ⭐⭐ 极低 KD，技术用户 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| roborock saros 10r | 9,900 | 51 | $2.45 | 商业 | 新旗舰主词 |
| roborock s8 maxv ultra | 8,100 | 56 | $1.97 | 商业 | 主力热卖型号 |
| roborock qrevo | 2,900 | 47 | $1.50 | 商业 | 系列词 |
| roborock q5 | 2,900 | 45 | $0.98 | 商业 | 中端热卖 |
| roborock home assistant | 320 | 18 | $0.00 | 信息 | ⭐ 社区词，技术用户 |
| roborock local only | 50 | 23 | $0.00 | 信息 | ⭐ 去云意图明确 |
| roborock privacy | 40 | 18 | $0.00 | 信息 | ⭐ 攻击面词 |
| is roborock a chinese company | 90 | 25 | $0.00 | 信息 | ⭐ 数据主权疑虑词 |
| who owns roborock | 170 | 34 | $0.00 | 信息 | 来源/信任词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| valetudo | 1,300 | 50 | $0.00 | 信息 | 去云固件主词；KD 50 但无付费竞争 |
| open source robot vacuum | 110 | 20 | $0.00 | 信息 | ⭐ Olares+Valetudo 直接机会 |
| valetudo roborock | 20 | 0 | $0.00 | 信息 | ⭐ GEO 前哨（精准意图） |
| robot vacuum privacy | 50 | 21 | $0.00 | 信息 | ⭐ 隐私攻击面 |
| robot vacuum no cloud | 10 | 0 | $0.00 | 信息 | ⭐ GEO 前哨 |
| robot vacuum local only | 10 | 0 | $0.00 | 信息 | ⭐ GEO 前哨 |
| roborock local only | 50 | 23 | $0.00 | 信息 | ⭐ 去云意图 |
| open source vacuum robot | 90 | 19 | $0.00 | 信息 | ⭐ Valetudo 族词 |
| open source robot vacuum cleaner | 70 | 25 | $0.00 | 信息 | ⭐ 同族 |
| robot vacuum home assistant | 70 | 9 | $0.00 | 信息 | ⭐⭐ 极低 KD |
| valetudo home assistant | 20 | 0 | $0.00 | 信息 | ⭐⭐ GEO 精准（Olares 直接场景） |

---

## Olares 关联词（Phase 3）

**核心叙事**：Roborock 默认将户型地图上传云端（中国服务器），通过 Valetudo root 后可实现地图完全本地化，配合 Olares 上运行的 Home Assistant（MQTT 联动），形成"地图不出家门"的完整本地控制链路——Olares 是这条链路的算力底座和 AI 编排层。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|-----|------------|
| valetudo | 1,300 | 50 | $0 | ⭐⭐⭐ Valetudo 是 Olares IoT 叙事的核心联动工具；文章可讲 Valetudo + Olares HA 完整配置 |
| roborock vs roomba | 1,000 | 32 | $0.78 | ⭐⭐ 对比文：两者都依赖云，Valetudo+Olares 是真正的第三条路 |
| roborock home assistant | 320 | 18 | $0 | ⭐⭐⭐ 技术用户已有意图；Olares Market 直接提供 HA，配置比裸机简单 |
| dreame vs roborock | 480 | 18 | $1.30 | ⭐⭐ 两者皆云依赖，Valetudo 覆盖两者型号，Olares 统一编排 |
| roborock vs dreame | 390 | 26 | $1.31 | ⭐⭐ 同上变体 |
| open source robot vacuum | 110 | 20 | $0 | ⭐⭐⭐ Valetudo（Apache-2.0）即答案；Olares 提供 HA 运行环境 |
| robot vacuum home assistant | 70 | 9 | $0 | ⭐⭐⭐ KD 极低（9）；Olares 一键部署 HA，配 MQTT 接 Valetudo |
| roborock privacy | 40 | 18 | $0 | ⭐⭐⭐ 数据主权攻击词；引出 Valetudo+Olares 本地方案 |
| robot vacuum privacy | 50 | 21 | $0 | ⭐⭐ 同上品类词版本 |
| is roborock a chinese company | 90 | 25 | $0 | ⭐⭐ 供应链/数据疑虑；引出地图不上传中国服务器的解法 |
| roborock local only | 50 | 23 | $0 | ⭐⭐⭐ 意图极精准；Valetudo+Olares 的直接答案 |
| valetudo roborock | 20 | 0 | $0 | ⭐⭐⭐ GEO 前哨（KD=0）；制作配置教程可抢 AI Overview 引用位 |
| valetudo home assistant | 20 | 0 | $0 | ⭐⭐⭐ GEO 前哨；Olares 运行 HA + Valetudo MQTT 的完整教程 |
| robot vacuum no cloud | 10 | 0 | $0 | ⭐⭐⭐ GEO 前哨；品类定义词，AI 问答首选引用 |
| robot vacuum local only | 10 | 0 | $0 | ⭐⭐ GEO 前哨；语义同上 |
| robot vacuum without wifi | 140 | 10 | $0.48 | ⭐ 边缘需求（用户不想联网），Valetudo 离线控制可满足 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| valetudo | 1,300 | 50 | $0 | 信息 | **主词候选** | 去云固件核心词；月量 1.3k，KD 50 但纯自然（无付费竞争），Olares 可撑完整教程文（Valetudo root + Olares HA 配置） |
| roborock vs roomba | 1,000 | 32 | $0.78 | 信息 | **主词候选** | 月量 1k、KD 32、CPC 有价值；对比文切入点：两者都依赖云，Valetudo+Olares 是第三条路 |
| dreame vs roborock | 480 | 18 | $1.30 | 信息/商业 | **主词候选** | KD 仅 18，CPC $1.3 说明商业价值；Valetudo 同时支持 Dreame，Olares 可统一编排 |
| roborock vs dreame | 390 | 26 | $1.31 | 信息/商业 | **次级**（并入对比文）| dreame vs roborock 同义变体，并入同一文章 |
| roborock home assistant | 320 | 18 | $0 | 信息 | **主词候选** | KD=18 极低；技术用户高意图词；Olares Market 已有 HA，配置教程可直接抢位 |
| narwal vs roborock | 260 | 25 | $1.10 | 信息 | **次级** | KD 低，并入对比文（洗地机方向）|
| who owns roborock | 170 | 34 | $0 | 信息 | **次级** | 品牌信任词；文中"Roborock 是北京上市公司，地图同步中国服务器"可作段落 |
| robot vacuum without wifi | 140 | 10 | $0.48 | 信息 | **次级** | KD=10 极低；意图略偏（用户想断网而非去云），并入隐私类文章 |
| open source robot vacuum | 110 | 20 | $0 | 信息 | **主词候选** | 月量 110 在软参考线附近；KD=20，Olares 叙事直接契合（Valetudo Apache-2.0） |
| is roborock a chinese company | 90 | 25 | $0 | 信息 | **次级** | 数据主权疑虑词；地图上传场景段落的流量入口 |
| open source vacuum robot | 90 | 19 | $0 | 信息 | **次级** | open source robot vacuum 同义，并入同文 |
| robot vacuum home assistant | 70 | 9 | $0 | 信息 | **主词候选** | KD=9 本报告最低竞争高机会词；Olares 一键部署 HA 是最强差异化 |
| open source robot vacuum cleaner | 70 | 25 | $0 | 信息 | **次级** | 同族，并入 |
| robot vacuum privacy | 50 | 21 | $0 | 信息 | **次级** | 攻击面词；并入 roborock privacy 文章 |
| roborock local only | 50 | 23 | $0 | 信息 | **次级** | 意图精准，与 roborock privacy 并入 |
| roborock privacy | 40 | 18 | $0 | 信息 | **主词候选** | 月量 40 低但语义极精准；KD=18，是"数据主权"攻击系列文章的锚词 |
| valetudo home assistant | 20 | 0 | $0 | 信息 | **GEO** | KD=0，精准配置意图；制作教程可抢 AI Overview/Perplexity 引用位 |
| valetudo roborock | 20 | 0 | $0 | 信息 | **GEO** | KD=0；Valetudo+Roborock 精准组合词，FAQ 段落即可覆盖 |
| robot vacuum no cloud | 10 | 0 | $0 | 信息 | **GEO** | 品类定义级长尾；AI 问答"什么扫地机不需要云"首选引用 |
| robot vacuum local only | 10 | 0 | $0 | 信息 | **GEO** | 同上语义，覆盖变体 |
| roborock alternative | 10 | 0 | $0.90 | 商业 | **GEO** | 量极小但 CPC 有价值（$0.90）；文章结尾"想彻底去云？" CTA 锚点 |

---

## 核心洞见

1. **品牌护城河**：Roborock 在几乎所有自有品牌词（23k+ 关键词、月流量 268k）上霸占 #1，护城河极深，无法正面刚品牌词。但在 `best robot vacuum`（排名 #8，月量 90.5k）等品类评测词上被媒体站抢占，且完全放弃了"隐私/去云/替代"这一价值维度——这是 Olares 的攻击窗口。

2. **可复制的打法**：Roborock 靠型号矩阵程序化建落地页（每款型号对应独立 URL），配合高品质产品图抢商业意图词。付费词保守（仅 95 词），几乎不在对比词和替代词上投放，说明这些词的流量目前由测评媒体（vacuumwars.com、moderncastle.com）控制。Olares 策略：做"第三视角"测评文，在 `roborock vs roomba`、`dreame vs roborock` 等 KD<30 的对比词上以内容竞争，文章结论是"两者都依赖云，Valetudo + Olares 才是真正的本地化方案"。

3. **对 Olares 最关键的词**：
   - **`robot vacuum home assistant`**（月量 70，KD **9**）：KD 最低、意图最精准，Olares Market 有现成 HA，可写"Roborock + Valetudo + Home Assistant on Olares"完整教程，直接撑全篇。
   - **`roborock vs roomba`**（月量 1,000，KD 32）：最大流量入口对比词，可带出"两者皆云依赖、Valetudo 去云、Olares 本地编排"叙事。
   - **`valetudo`**（月量 1,300，KD 50）：去云固件主词，Olares 教程文中必出现的配置词，长期品牌关联建设。

4. **最大攻击面**：**地图数据上传中国服务器**。Roborock 美国/欧洲版本官方声称区域化存储（EU 用 AWS Frankfurt），但中国账号和国内用户数据走中国服务器，北京总部上市公司属性（688169.SH）引发海外"数据主权"疑虑。`is roborock a chinese company`（月量 90）、`roborock privacy`（月量 40）是此攻击面的量化入口。Valetudo root 是唯一在技术层面切断数据上传的开源方案。

5. **隐藏低 KD 金矿**：`robot vacuum home assistant`（KD **9**）、`robot vacuum without wifi`（KD **10**）、`open source robot vacuum`（KD **20**）——三词合计月量约 280，全部可在一篇"去云扫地机完全指南"里覆盖，竞争极低。`valetudo roborock`、`valetudo home assistant`（KD **0**）是直接抢 AI Overview 引用位的 GEO 金矿。

6. **GEO 前瞻布局**：`robot vacuum no cloud`、`robot vacuum local only`、`valetudo roborock`、`valetudo home assistant`——这四个词 KD=0、月量接近 0 但语义极精准，是 AI 搜索（Perplexity/ChatGPT/Gemini）在"什么扫地机不上传数据"类问题时最可能引用的锚词。只需在教程文中加入结构化 FAQ 段落即可覆盖。

7. **与既有分析的关联**：iot.md 已标注核心机会词（`robot vacuum without cloud`、`valetudo`、`roborock vs roomba`、`robot vacuum privacy`），与本报告完全吻合，可直接作为内容选题指令传入 seo-content。`roborock home assistant`（月量 320，KD 18）是 iot.md 未列但价值极高的补充词——Home Assistant 已在 Olares Market 上架，构成最强产品差异化。IoT 方向（方向 7）的叙事核心是"Olares 是本地 IoT 数据的 sovereign 编排层"，Roborock + Valetudo + HA on Olares 是这条叙事最完整的落地示例。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these、phrase_questions、phrase_related）| 2026-07-06*  
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
