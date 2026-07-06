# iRobot (Roomba) SEO 竞品分析报告

> 域名：irobot.com | SEMrush US | 2026-07-06
> 曾是全球最大扫地机器人品牌（Roomba 发明者），2026-01 Chapter 11 破产后被中国深圳 Picea Robotics 收购；数据隐私争议（2020 Scale AI 隐私照片泄露）+ 破产信任危机，是 Olares 最强攻击面。

---

## 项目理解（前置）

iRobot 1990 年创立于麻省 Bedford，是 Roomba 品牌的发明者（2002 年推出首代），曾长期占据全球机器人吸尘器市场份额第一。2022 年被 Amazon 拟以 17 亿美元收购，因反垄断审查于 2024 年告吹，随后陷入财务危机；2025-12-14 宣布 Chapter 11 重组，并与合同制造商 Shenzhen Picea Robotics Co., Ltd. 达成并购协议，2026-01-23 完成重组，iRobot 成为 Picea 全资私有子公司。

隐私历史：2020 年，iRobot 开发测试版 Roomba J7 系列将家庭影像（含用户如厕照）通过 Scale AI 发给委内瑞拉外包标注工，这些敏感图像随后泄露至 Facebook、Discord 等社媒——被 MIT Technology Review 于 2022 年底曝光，引发行业最严重的机器人隐私事件之一。

本地控制方面：Roomba 与 Roborock/Dreame 架构不同，**Valetudo 不支持 iRobot**（Valetudo 依赖 Linux 基板+实时地图，Roomba 硬件不满足）。但 Roomba 900/i/s/j 系列内置本地 MQTT over WiFi，Home Assistant 官方 Roomba 集成 + 社区 Roomba+ 插件可实现**纯本地控制（无需 iRobot 云账号）**；Olares Market 已上架 HA，构成完整的本地链路。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Roomba 品牌发明者，全球扫地机市场奠基者；Chapter 11 后归 Picea（深圳）所有，数据主权争议极大 |
| 开源 / 许可证 | **闭源**商业产品；官方无开源仓库 |
| 主仓库 | 无官方开源；社区：[johnnyh1975/ha_roomba_plus](https://github.com/johnnyh1975/ha_roomba_plus)（Roomba 本地 MQTT HA 集成，覆盖 900/i/s/j/Braava） |
| 核心功能 | 机器人吸尘器（Roomba 系列）+ 拖地机（Braava 系列）；新款支持 VSLAM/视觉 SLAM 建图；iRobot OS + iRobot Home App |
| 商业模式 / 定价 | 买断硬件（入门 ~$180 → 旗舰 j9+/s9+ $700-$900+）；App 基础功能免费，Select 订阅服务已于 2024 年停止新订；破产后老订阅者权益存疑 |
| 差异化 / 价值主张 | Roomba 品牌心智极强（同义词级别）；但定价不再有优势，且隐私事件+中国新主人严重削弱信任 |
| 主要竞品（初判）| Roborock、Dreame、Ecovacs、Narwal（洗地机方向）、Shark（美国中低端） |
| Olares Market | 未上架（硬件品牌）；**Home Assistant 已上架** ✅，配 Roomba+ 插件可纯本地控制 Roomba 900/i/s/j 系列 |
| 来源 | [media.irobot.com](https://media.irobot.com/2025-12-14-iRobot-Announces-Strategic-Transaction-to-Drive-Long-Term-Growth-Plan)、[therobotreport.com](https://www.therobotreport.com/irobot-emerges-from-chapter-11-picea-u-s-subsidiary/)、[MIT Technology Review 2022](https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/)、[home-assistant.io/integrations/roomba](https://www.home-assistant.io/integrations/roomba/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | irobot.com |
| SEMrush Rank | 6,821 |
| 自然关键词数 | 67,939 |
| 月自然流量（US）| 342,948 |
| 自然流量估值 | $982,214/月 |
| 付费关键词数 | 354 |
| 月付费流量 | 30,802 |
| 付费流量成本 | $83,405/月 |
| 排名 1-3 位 | 6,354 词 |
| 排名 4-10 位 | 6,250 词 |
| 排名 11-20 位 | 6,078 词 |

> **对比 Roborock**（SR 8,620 / 流量 268k / 估值 $361k）：iRobot 流量规模更大、估值更高，但 Roborock 的流量效率（词量→流量转化率）更高，且 Roborock 在高商业价值型号词上霸占 #1。iRobot 流量优势主要来自极强的品牌词心智（Roomba ≈ robot vacuum）。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.irobot.com | 41,065 | 307,734 | 89.73% |
| homesupport.irobot.com | 22,709 | 30,763 | 8.97% |
| select.irobot.com | 251 | 1,120 | 0.33% |
| careers.irobot.com | 95 | 1,037 | 0.30% |
| media.irobot.com | 659 | 964 | 0.28% |
| about.irobot.com | 608 | 714 | 0.21% |
| answers.irobot.com | 1,808 | 290 | 0.08% |

> **洞见**：`homesupport.irobot.com` 以 22,709 个关键词贡献近 9% 流量，说明售后/教程词是 iRobot SEO 第二大支柱。破产后用户担忧设备失效，"how to reset roomba"（月量 2,400）、"how do I know if my Roomba is charging"（480）等售后词流量会持续——这也是内容切入的机会。

### 官网 TOP 自然关键词（按流量排序，取前 30）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| irobot | 1 | 74,000 | 90 | $10.94 | 59,200 | 导航/品牌 | irobot.com/ |
| roomba | 1 | 110,000 | 62 | $1.55 | 27,280 | 品牌+导航 | /en_US/roomba.html |
| irobot roomba | 1 | 18,100 | 58 | $1.26 | 14,480 | 品牌 | /en_US/roomba.html |
| roomba（二次排名）| 2 | 110,000 | 62 | $1.55 | 7,150 | 品牌 | irobot.com/ |
| i roboter | 1 | 27,100 | 79 | $2.53 | 6,720 | 品牌（德语变体）| irobot.com/ |
| robot vacuum and | 2 | 60,500 | 68 | $1.15 | 4,961 | 品类 | /en_US/shop/vacuum.html |
| i robot | 3 | 60,500 | 83 | $2.53 | 4,961 | 品牌 | irobot.com/ |
| irobot roomba vacuum | 1 | 5,400 | 50 | $0.66 | 4,320 | 品牌+品类 | /en_US/roomba-robot-vacuums |
| irobot vacuum | 1 | 5,400 | 54 | $0.96 | 4,320 | 品牌 | irobot.com/ |
| brand new irobot roomba j7+ | 1 | 4,400 | 39 | $0.00 | 3,520 | 商业 | /en_US/roomba-j7plus-self-emptying-robot-vacuum/J755020.html |
| robot vacuum | 2 | 90,500 | 56 | $1.15 | 3,167 | 品类 | /en_US/shop/vacuum.html |
| robot cleaning robot | 1 | 18,100 | 65 | $1.15 | 2,389 | 品类 | irobot.com/ |
| roomba vacuum | 1 | 27,100 | 52 | $0.84 | 2,222 | 品牌 | /en_US/roomba-robot-vacuums |
| robot vacuum cleaner | 1 | 12,100 | 52 | $1.15 | 1,597 | 品类 | /en_US/shop/vacuum.html |
| irobot home app | 1 | 1,600 | 59 | $0.57 | 1,280 | 品牌+功能 | /en_US/irobot-home-app.html |
| best robot vacuum for pet hair | 4 | 22,200 | 25 | $1.35 | 976 | 商业 | /en_US/robot-vacuum/pet-hair.html |
| roomba battery replacement | 1 | 5,400 | 20 | $0.45 | 712 | 商业 | /en_US/us/all-parts-and-accessories/batteries |
| robot vacuum and mop combo | 1 | 5,400 | 51 | $1.56 | 712 | 品类 | /en_US/shop/combo.html |
| self emptying robot vacuum | 2 | 6,600 | 41 | $1.28 | 541 | 品类 | /en_US/roomba-robot-vacuums |
| roomba j7+ | 1 | 3,600 | 34 | $0.63 | 475 | 商业 | /en_US/roomba-j7plus-self-emptying-robot-vacuum/J755020.html |
| is roomba going out of business | 1 | 320 | 63 | $0.46 | 256 | 信息 | irobot.com/（推测）|
| irobot bankruptcy | — | 2,900 | 55 | $1.74 | — | 信息 | — |

> **洞见**：iRobot 霸占几乎所有 Roomba 品牌词，KD 极高（62-90）无法正面竞争。`best robot vacuum for pet hair`（月量 22k，KD **25**）是 iRobot 唯一排名靠后（#4）的大词——媒体站主导，这里有空间。`roomba battery replacement`（月量 5.4k，KD **20**）是极低竞争的售后词，说明 Roomba 用户有强烈的自助维修需求——破产后这类词会更热。

### 付费词（Google Ads，按流量排序）

iRobot 投放 354 个付费词（月付费流量 30,802，成本 $83,405），策略激进而特殊——**大量购买竞品品牌词**，引导到 `/deals.html` 比价页。这说明破产后 iRobot 在主动拦截"想买竞品"的用户，试图以价格优势留住客户。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| roomba | 110,000 | $1.55 | irobot.com/ |
| irobot | 74,000 | $10.94 | irobot.com/ |
| **roborock**（竞品！）| 74,000 | $1.12 | /en_US/deals.html |
| shark robot vacuum（竞品）| 27,100 | $0.72 | /en_US/deals.html |
| roomba vacuum | 33,100 | $0.98 | irobot.com/ |
| **eufy robovac**（竞品）| 12,100 | $0.85 | /en_US/deals.html |
| robot vacuum cleaner | 14,800 | $1.16 | /en_US/roomba-max-705-robots.html |
| irobot roomba max 705 | 8,100 | $1.30 | /products/roomba-max-705 |
| roomba vacuum and mop | 5,400 | $1.04 | /roomba-plus-505-combo |

> **洞见**：iRobot 购买 `roborock`、`shark robot vacuum`、`eufy robovac` 等竞品词导向 `/deals.html` 比价页，是非常激进但透明的信号——他们承认自己在"比较阶段"处于劣势，试图用价格截流。这正是 Olares 可以通过内容在"对比/替代"词上建立第三视角的机会。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| roomba vs roborock | 390 | 27 | $1.06 | 信息/商业 | ⭐ KD 27，CPC 高，高价值对比词 |
| irobot vs roborock | 260 | 33 | $1.10 | 信息/商业 | ⭐ 同义变体，量 260 |
| roomba alternative | 170 | 40 | $0.81 | 商业 | 破产后需求激增；KD 40 偏高但可挑战 |
| best roomba alternative | 40 | 40 | $1.13 | 商业 | ⭐ 与上同群，CPC $1.13 说明商业价值 |
| roomba replacement | 20 | 0 | $1.22 | 商业 | ⭐ KD=0，CPC $1.22，精准购买意图 |
| roomba vs ecovacs | 20 | 0 | $0.79 | 信息 | ⭐ 极低 KD，小量但精准 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| robot vacuum | 90,500 | 56 | $1.15 | 品类 | 高竞争，媒体站/iRobot/Roborock 霸占 |
| best robot vacuum | 49,500 | 50 | $1.00 | 商业 | 评测媒体垄断，难进 |
| best robot vacuum and mop | 27,100 | 48 | $1.41 | 商业 | 同上，KD 偏高 |
| best robot vacuum for pet hair | 22,200 | 25 | $1.35 | 商业 | ⭐ KD 25，量大，iRobot 仅排 #4 |
| robot vacuum reviews | 3,600 | 42 | $0.80 | 信息 | 媒体站控制 |
| best robot vacuum without wifi | 70 | 7 | $0.71 | 商业 | ⭐⭐ **KD=7 本报告最低大值词**；隐私/去云人群 |
| do robot vacuums need wifi | 70 | 9 | $0.88 | 信息 | ⭐⭐ KD=9，FAQ 机会词 |
| robot vacuum no wifi | 70 | 9 | $0.55 | 信息 | ⭐⭐ 同族，KD=9 |
| is a roomba worth it | 390 | 7 | $0.90 | 信息 | ⭐⭐ KD=7，破产后疑虑词，流量大 |
| are roombas worth it | 720 | 14 | $0.93 | 信息 | ⭐⭐ KD=14，月量 720，非常值得做 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| irobot bankruptcy | 2,900 | 55 | $1.74 | 信息 | 月量 2.9k，破产事件词；高 KD 但 CPC $1.74 显商业价值 |
| is roomba going out of business | 320 | 63 | $0.46 | 信息 | 破产信任词，iRobot 自己排 #1 维护声誉 |
| does roomba have camera | 110 | 39 | $0.00 | 信息 | 隐私疑虑词；KD 39 但量有价值 |
| roomba data collection | 20 | 0 | $0.00 | 信息 | ⭐ KD=0，隐私意图 |
| roomba data privacy | 20 | 0 | $0.00 | 信息 | ⭐ 同上变体 |
| roomba battery replacement | 5,400 | 20 | $0.45 | 商业 | ⭐ KD=20，月量 5.4k，售后/DIY 人群 |
| how to reset roomba | 2,400 | 32 | $0.09 | 信息 | ⭐ KD 32，售后词，homesupport 承接 |
| are roombas worth it | 720 | 14 | $0.93 | 信息 | ⭐⭐ 破产后疑虑词，高价值 |
| roomba home assistant | 170 | 20 | $0.00 | 信息 | ⭐⭐ KD=20，技术用户；Olares 直接机会 |
| irobot home assistant | 70 | 22 | $0.00 | 信息 | ⭐⭐ 同上变体 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| valetudo | 1,300 | 50 | $0 | 信息 | 去云固件核心词（覆盖 Roborock/Dreame，不覆盖 Roomba）|
| open source robot vacuum | 110 | 20 | $0 | 信息 | ⭐ KD=20；Valetudo 是答案（引向 Roborock 路线）|
| robot vacuum without wifi | 140 | 10 | $0.48 | 信息 | ⭐⭐ KD=10，去云/离线控制人群 |
| robot vacuum privacy | 50 | 21 | $0 | 信息 | ⭐ KD=21，隐私意图族词 |
| robot vacuum home assistant | 50 | 11 | $0 | 信息 | ⭐⭐ KD=11，Olares 直接场景 |
| local robot vacuum | 40 | 11 | $1.20 | 商业 | ⭐⭐ KD=11，CPC $1.20；购买意图+本地控制 |
| robot vacuum no cloud | 10 | 0 | $0 | 信息 | ⭐⭐ GEO 前哨（KD=0）|
| robot vacuum local only | 10 | 0 | $0 | 信息 | ⭐⭐ GEO 前哨（KD=0）|
| self hosted robot vacuum | 10 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| does roborock send data to china | 50 | 18 | $0 | 信息 | ⭐⭐ iRobot/Picea 同类疑虑，Olares 去云叙事入口 |
| best robot vacuum without wifi | 70 | 7 | $0.71 | 商业 | ⭐⭐ KD=7，可直接写文并撑全篇 |
| do robot vacuums need wifi | 70 | 9 | $0.88 | 信息 | ⭐⭐ KD=9，FAQ 词，内容页覆盖 |

---

## Olares 关联词（Phase 3）

**核心叙事**：iRobot 在 2022 年隐私泄露（Scale AI/照片）+ 2026 年破产并归中国 Picea 收购后，成为"机器人真的安全吗"话题的最强符号。Olares 的两条切入路：① 对现有 Roomba 用户——Olares 跑 HA + Roomba+ 插件，实现纯本地 MQTT 控制，零云账号、零数据上传；② 对"找替代"用户——切换到 Roborock/Dreame 机型 + Valetudo 去云固件 + Olares HA，构建完整的本地机器人控制链路。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|-----|------------|
| are roombas worth it | 720 | 14 | $0.93 | ⭐⭐⭐ 破产后疑虑高峰词；文章可给出"现有 Roomba + Olares HA 本地化" vs "换 Roborock+Valetudo+Olares"两条路的决策框架 |
| roomba alternative | 170 | 40 | $0.81 | ⭐⭐ 直接替代词；推荐 Roborock/Dreame + Valetudo 路线，Olares 提供 HA 运行环境，全程本地 |
| roomba vs roborock | 390 | 27 | $1.06 | ⭐⭐⭐ KD=27，CPC $1.06；对比文结论：两者皆依赖云，Valetudo+Olares 才是真正本地化 |
| roomba home assistant | 170 | 20 | $0 | ⭐⭐⭐ KD=20，高意图技术用户；Olares Market 已有 HA，配 Roomba+ 插件即可纯本地控制 Roomba |
| irobot home assistant | 70 | 22 | $0 | ⭐⭐⭐ 同上变体，并入同一文章 |
| robot vacuum home assistant | 50 | 11 | $0 | ⭐⭐⭐ KD=11；Olares 一键部署 HA 是最强差异化，无需手动折腾 |
| best robot vacuum without wifi | 70 | 7 | $0.71 | ⭐⭐⭐ KD=7，本报告竞争最低的商业意图词；Olares+HA 本地控制即是"无需 WiFi 云"的答案 |
| open source robot vacuum | 110 | 20 | $0 | ⭐⭐⭐ KD=20；Valetudo（Apache-2.0）是答案，Olares 提供 HA 运行环境 |
| robot vacuum without wifi | 140 | 10 | $0.48 | ⭐⭐ KD=10；文章可覆盖"去云 = 不依赖厂商云"（不是 WiFi-less，而是 local-only）|
| robot vacuum privacy | 50 | 21 | $0 | ⭐⭐⭐ 攻击面词；引出 Scale AI 泄露事件 + Picea 新主人 → Olares 本地方案 |
| local robot vacuum | 40 | 11 | $1.20 | ⭐⭐⭐ KD=11，CPC $1.20 显商业价值；"本地控制机器人"的精准意图 |
| does roborock send data to china | 50 | 18 | $0 | ⭐⭐ 隐私疑虑词（延伸到 iRobot/Picea 同样问题）；引出 Valetudo 切断数据上传 |
| valetudo | 1,300 | 50 | $0 | ⭐⭐ 去云固件主词；Olares+HA 是 Valetudo 配置的最简易路径；文中必出现 |
| irobot bankruptcy | 2,900 | 55 | $1.74 | ⭐ 量大（2.9k）但 KD 高（55）；作为信任危机的引流词，文章开头可引用，内链到本地化方案 |
| robot vacuum no cloud | 10 | 0 | $0 | ⭐⭐⭐ GEO 前哨（KD=0）；AI 问答"什么扫地机不上传数据"首选引用 |
| robot vacuum local only | 10 | 0 | $0 | ⭐⭐ GEO 前哨；同上语义变体 |
| self hosted robot vacuum | 10 | 0 | $0 | ⭐⭐ GEO 前哨；极精准自托管意图 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| irobot bankruptcy | 2,900 | 55 | $1.74 | 信息 | **次级**（引流段落）| 月量 2.9k 是本报告最大量词，但 KD=55 难独立排名；作为文章引流词（"为什么 iRobot 破产？"），带出隐私事件和本地化方案 |
| are roombas worth it | 720 | 14 | $0.93 | 信息 | **主词候选** | 月量 720，KD=14，CPC $0.93 商业信号；破产后疑虑高峰，文章可给"现有用户 vs 换机"两条本地化路径 |
| roomba vs roborock | 390 | 27 | $1.06 | 信息/商业 | **主词候选** | 月量 390，KD=27，CPC $1.06；对比文：两者都依赖云，Valetudo+Olares 是第三条路；与 Roborock 报告的 `roborock vs roomba`（1,000/KD32）可联动 |
| how to reset roomba | 2,400 | 32 | $0.09 | 信息 | **次级** | 量大但偏纯售后，并入"Roomba 本地控制完全指南"作为 FAQ 段落 |
| roomba battery replacement | 5,400 | 20 | $0.45 | 商业 | **次级** | KD=20，量 5.4k，DIY 维修人群；可并入"Roomba 无网络控制"文的附加章节（本地化用户更倾向自维修）|
| roomba alternative | 170 | 40 | $0.81 | 商业 | **主词候选** | 月量 170，KD=40 偏高但破产后需求持续增加；主推"Roborock+Valetudo+Olares"路线 |
| roomba home assistant | 170 | 20 | $0 | 信息 | **主词候选** | KD=20 极低；与 `irobot home assistant`（70/KD22）合并；Olares Market 已有 HA + Roomba+ 插件，最强差异化 |
| robot vacuum without wifi | 140 | 10 | $0.48 | 信息 | **主词候选** | KD=10，月量 140；隐私人群；"去云"即答案，Olares+HA 本地 MQTT 控制 |
| are roombas worth it | 720 | 14 | $0.93 | 信息 | **主词候选** | 见上，破产后人群疑虑词，高商业价值 |
| best robot vacuum without wifi | 70 | 7 | $0.71 | 商业 | **主词候选** | **KD=7 本报告最低竞争商业词**；可独立撑一篇"Best Robot Vacuum Without WiFi/Cloud"，文末推 Olares+HA 本地控制方案 |
| open source robot vacuum | 110 | 20 | $0 | 信息 | **主词候选** | 月量 110，KD=20；Valetudo（Apache-2.0）是答案，Olares 提供 HA 环境 |
| irobot home assistant | 70 | 22 | $0 | 信息 | **次级** | 并入 `roomba home assistant` 文章 |
| robot vacuum home assistant | 50 | 11 | $0 | 信息 | **主词候选** | KD=11；Olares 一键部署 HA，配 Roomba+ 无需云；可单独撑教程文 |
| robot vacuum privacy | 50 | 21 | $0 | 信息 | **次级** | 攻击面词；并入隐私/替代文章，引出 Scale AI 泄露事件 |
| local robot vacuum | 40 | 11 | $1.20 | 商业 | **次级** | KD=11，CPC $1.20，购买意图；并入 `best robot vacuum without wifi` 文 |
| does roomba have camera | 110 | 39 | $0 | 信息 | **次级** | 隐私疑虑词，量有价值；文章中"Roomba 摄像头事件"段落吸引流量 |
| do robot vacuums need wifi | 70 | 9 | $0.88 | 信息 | **次级** | KD=9，并入去云文章作为 FAQ 标题段 |
| roomba replacement | 20 | 0 | $1.22 | 商业 | **次级** | KD=0，CPC $1.22，精准替换意图；并入替代文章 |
| valetudo | 1,300 | 50 | $0 | 信息 | **次级**（锚词）| 月量 1.3k，KD=50；教程文中必出现，帮 Roborock+Valetudo+Olares 路线建立长期关联 |
| robot vacuum no cloud | 10 | 0 | $0 | 信息 | **GEO** | KD=0；AI 问答"什么扫地机不上传数据"必引 |
| robot vacuum local only | 10 | 0 | $0 | 信息 | **GEO** | 同上变体 |
| self hosted robot vacuum | 10 | 0 | $0 | 信息 | **GEO** | 极精准自托管意图 |
| irobot picea safety | 20 | 0 | $0 | 信息 | **GEO** | 新主人安全疑虑词，KD=0；FAQ 段落可抢 AI Overview 引用位 |

---

## 核心洞见

1. **品牌护城河**：iRobot 在所有 Roomba 品牌词（KD 58-90）上霸占 #1，无法正面刚。但护城河正在瓦解：Chapter 11 + Picea 收购削弱信任，`irobot bankruptcy`（月量 2,900）、`is roomba going out of business`（320）说明用户开始质疑品牌存续，这是 Olares 近期最大的内容窗口。

2. **可复制的打法**：iRobot 自己的付费策略给出答案——他们购买 `roborock`、`shark robot vacuum`、`eufy robovac` 等竞品词导向 `/deals.html` 比价页，说明"对比购物阶段"是流量争夺的主战场。Olares 的反向操作：做面向"Roomba 已无未来"人群的内容（`are roombas worth it`、`roomba alternative`），结论指向"本地控制路线"。

3. **对 Olares 最关键的词**：
   - **`are roombas worth it`**（月量 720，KD **14**）：月量最大+KD 最低的高商业价值词，破产后疑虑高峰期，可写"2026 年 Roomba 还值得买吗"——给出"现有用户 Olares+HA 本地化"+ "新买用户 Roborock+Valetudo+Olares"两条路径。
   - **`roomba home assistant`**（月量 170，KD **20**）：技术用户高意图词，Olares Market 已有 HA，配 Roomba+ 插件实现零云 Roomba 控制，是最完整的产品差异化。
   - **`best robot vacuum without wifi`**（月量 70，KD **7**）：KD 最低的商业词，可独立撑一篇文章，覆盖去云人群全体。

4. **最大攻击面**：**隐私史 + 中国新主人**。iRobot 2020 Scale AI 事件（测试机拍到如厕照流入 Facebook）是机器人行业最著名的隐私丑闻；2026 年被深圳 Picea 收购后，尽管创建了 iRobot Safe Corp. 隔离数据，The Verge 的标题直接写"Roomba's new Chinese owner"——这在美国用户中触发极强"中国数据"疑虑。`robot vacuum privacy`（KD 21）、`does roomba have camera`（KD 39）是这一攻击面的量化入口。

5. **隐藏低 KD 金矿**：`best robot vacuum without wifi`（KD **7**）+ `are roombas worth it`（KD **14**）+ `roomba battery replacement`（月量 5.4k，KD **20**）+ `roomba home assistant`（KD **20**）——这组词 KD 全部 ≤ 20、月量合计超 6k，却几乎没有专门面向"隐私+本地控制"角度的内容页。`robot vacuum no cloud`、`robot vacuum local only`（KD **0**）是直接 GEO 金矿。

6. **GEO 前瞻布局**：`robot vacuum no cloud`、`robot vacuum local only`、`self hosted robot vacuum`、`irobot picea safety`——这四个词 KD=0、月量极小但语义极精准，是 AI 搜索（Perplexity/ChatGPT/Gemini）处理"扫地机器人隐私/不联网方案"类问题时最可能引用的锚词。在教程文中加入结构化 FAQ 段落（"Does any robot vacuum work without cloud？" / "Is Roomba safe after Picea acquisition?"）即可覆盖。

7. **与既有分析的关联**：Roborock 报告（`robot vacuum home assistant` KD=9、`roborock vs roomba` KD=32、`valetudo` 1.3k）与本报告形成天然联动——**建议在同一"机器人本地控制"内容系列里跨报告复用词簇**：`roomba vs roborock`（390/KD27）的文章可带出 Valetudo（Roborock 路线）和 Roomba+（iRobot 路线），Olares 作为两者通用的 HA 底座。IoT 方向（方向 7）的核心叙事"Olares 是本地 IoT 数据的 sovereign 编排层"，在 iRobot 这个案例上因为 Scale AI 泄露 + Picea 收购的双重信任危机有了最有力的论据。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these、phrase_questions、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
