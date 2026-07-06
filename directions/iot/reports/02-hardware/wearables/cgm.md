# Dexcom / Abbott FreeStyle Libre CGM SEO 竞品分析报告

> 域名：dexcom.com（主研）+ freestyle.abbott（附带）| SEMrush US | 2026-07-06
> CGM（连续血糖监测仪）双寡头：Dexcom 44.7% + Abbott 48.5% 美国市占；Olares 平替切入点为 Nightscout（自托管 CGM 数据平台）

---

## 项目理解（前置）

**Dexcom** 是全球领先的持续血糖监测（CGM）设备制造商，旗舰产品 Dexcom G7 / G7 15 Day 面向 1 型和 2 型糖尿病患者，Stelo 面向非胰岛素依赖的 2 型患者（OTC，无需处方）。设备每 5 分钟推送实时血糖数据到手机/智能手表，配合 Clarity 云平台进行长期数据管理，无需指尖采血。

**Abbott FreeStyle Libre** 是全球最畅销 CGM 系统，核心卖点是更小的传感器（全球最小最薄）+ 每分钟读数 + 价格比 Dexcom 低近一半。旗舰产品 Libre 3 Plus 传感器佩戴 15 天，官网 `freestyle.abbott` 面向美国用户，可对比 `freestylelibre.us`（几乎无流量，SEO 无意义）。

Olares 平替切入点：**Nightscout**（`cgm-remote-monitor`，AGPL-3.0，GitHub ★2.8k，活跃至 2026-06）——开源、自托管 CGM 数据平台，可接入 Dexcom / Libre / 其它传感器，提供 Web 仪表盘 + 实时报警 + 数据共享。运行在 Olares 上无需依赖第三方云，血糖数据完全自主持有。

| 项目 | 内容 |
|------|------|
| 一句话定位 | CGM 双寡头：Dexcom（精准+连接最广）vs Abbott Libre（最小+最便宜）；Nightscout = 自托管开源 CGM 数据中台 |
| 开源 / 许可证 | Dexcom/Abbott：闭源硬件+云；Nightscout：AGPL-3.0（GitHub nightscout/cgm-remote-monitor） |
| 主仓库 | https://github.com/nightscout/cgm-remote-monitor（★2.8k，活跃中，v15.0.7 @ 2026-04） |
| 核心功能 | Dexcom：实时血糖 5 分钟推送 / 无指尖采血 / 与胰岛素泵/Apple Watch 集成；Nightscout：CGM 数据聚合+可视化+实时警报+数据共享+DIY AID 联动 |
| 商业模式 / 定价 | Dexcom G7：医保覆盖后 ≤$20/月；自费 pharmacy savings 50%+ 折扣；Libre 3 Plus 商保 $0-$75/月，Abbott 称"比其它 CGM 低一半以上"；Nightscout：免费自托管（需 VPS 或家用服务器+MongoDB） |
| 差异化 / 价值主张 | Dexcom：最多连接合作伙伴（泵/设备/App）、Medicare 最优先 CGM；Libre：最便宜+最小+每分钟读数；Nightscout：数据主权+DIY 闭环（OpenAPS/Loop/Trio）|
| 主要竞品（初判）| Dexcom vs Libre（互为最大竞品）；OTC CGM：Stelo（Dexcom）、Lingo（Abbott）；平台竞品：Tidepool（12.1k/月）、Glooko（12.1k/月）|
| Olares Market | 未上架（Nightscout 尚未打包为 Olares 应用） |
| 来源 | dexcom.com；freestyle.abbott；github.com/nightscout/cgm-remote-monitor；nightscout.github.io |

---

## 流量基线（Phase 1）

### 概览 — Dexcom（主研）

| 指标 | 数据 |
|------|------|
| 域名 | dexcom.com |
| SEMrush Rank | 4,035 |
| 自然关键词数 | 83,397 |
| 月自然流量（US）| 607,919 |
| 自然流量估值 | $1,453,499 / 月 |
| 付费关键词数 | 398 |
| 月付费流量 | 27,861 |
| 付费流量成本 | $84,442 / 月 |
| 排名 1-3 位 | 8,427 词 |
| 排名 4-10 位 | 12,330 词 |
| 排名 11-20 位 | 9,400 词 |

### 概览 — Abbott FreeStyle Libre（freestyle.abbott，附带）

| 指标 | 数据 |
|------|------|
| 域名 | freestyle.abbott |
| SEMrush Rank | 11,090 |
| 自然关键词数 | 41,364 |
| 月自然流量（US）| 205,584 |
| 自然流量估值 | $526,002 / 月 |
| 付费关键词数 | 1,138 |
| 月付费流量 | 45,190 |
| 付费流量成本 | $102,700 / 月 |

> Abbott Libre 付费词数远多于 Dexcom（1,138 vs 398），说明 Abbott 更重 Paid 防守。

### 子域名流量分布（dexcom.com）

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.dexcom.com | 71,507 | 538,567 | 88.6% |
| clarity.dexcom.com | 251 | 41,084 | 6.8% |
| account.dexcom.com | 458 | 10,943 | 1.8% |
| careers.dexcom.com | 398 | 6,156 | 1.0% |
| provider.dexcom.com | 7,813 | 4,525 | 0.7% |
| investors.dexcom.com | 1,621 | 2,952 | 0.5% |

> `clarity.dexcom.com`（CGM 数据管理云）拿下 6.8% 流量——说明"数据管理入口"本身是 SEO 强词。

### 官网 TOP 自然关键词（dexcom.com，按流量降序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| dexcom | 1 | 110,000 | 76 | $3.29 | 88,000 | 导航 | /en-us |
| dexcom clarity | 1 | 27,100 | 32 | $4.65 | 21,680 | 导航/信息 | clarity.dexcom.com |
| dexcom glucose monitor | 1 | 9,900 | 51 | $3.13 | 7,920 | 品类 | /en-us |
| glucose monitor | 1 | 49,500 | 81 | $4.14 | 6,534 | 品类 | /en-us |
| dexcom clarity login | 1 | 6,600 | 32 | $5.65 | 5,280 | 导航 | clarity.dexcom.com |
| dexcom support | 1 | 6,600 | 35 | $2.32 | 5,280 | 导航 | /en-us/support |
| my dexcom | 1 | 6,600 | 41 | $3.29 | 5,280 | 导航 | account.dexcom.com |
| continuous glucose monitoring | 1 | 33,100 | 85 | $4.63 | 4,369 | 信息/品类 | /en-us |
| normal blood sugar levels chart | 1 | 33,100 | 82 | $0.77 | 4,369 | 信息 | /en-us/faqs/… |
| cgm | 1 | 27,100 | 85 | $0 | 3,577 | 信息/品类 | /en-us |
| dexcom g7 | 1 | 110,000 | 47 | $3.58 | 2,860 | 商业 | /en-us/g7-cgm-system |
| continuous glucose monitor | 1 | 22,200 | 79 | $4.63 | 2,930 | 品类 | /en-us |
| normal blood sugar | 3 | 49,500 | 83 | $0.81 | 2,178 | 信息 | /en-us/faqs/… |
| glucose levels | 3 | 90,500 | 90 | $1.39 | 1,991 | 信息 | /en-us/faqs/… |
| blood sugar value chart | 1 | 22,200 | 62 | $1.35 | 1,820 | 信息 | /en-us/faqs/… |
| dexcom g7 overpatch | 1 | 1,600 | 19 | $1.18 | 1,280 | 信息 | /en-us/faqs/… |
| dexcom clarity clinic portal | 1 | 1,600 | 31 | $8.53 | 1,280 | 导航 | clarity.dexcom.com/professional |
| dexcom g7 cost without insurance | — | 390 | 33 | $0 | — | 信息/商业 | — |
| dexcom share | — | 140 | 22 | $0 | — | 信息 | — |

> **洞见**：Dexcom 用信息型健康词（血糖正常值图表、血糖水平）拿大量信息流量——仅 `/faqs/what-is-normal-blood-glucose-level` 一篇页面承接了约 15,000+ 月自然流量。

### 官网 TOP 自然关键词（freestyle.abbott，按流量降序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| freestyle libre | 1 | 33,100 | 49 | $1.92 | 26,480 | 品牌 | /us-en/home |
| libre | 1 | 27,100 | 50 | $2.41 | 6,720 | 导航 | /us-en/home |
| libre 3 | 1 | 33,100 | 37 | $2.54 | 4,369 | 商业 | /products/freestyle-libre-3 |
| libre 3 plus | 1 | 22,200 | 43 | $1.60 | 2,930 | 商业 | /products/freestyle-libre-3 |
| freestyle libre 3 | 1/2 | 60,500 | 55 | $1.84 | 1,573/847 | 商业 | /products/freestyle-libre-3 |
| freestyle libre 3 plus | 1 | 18,100 | 38 | $1.56 | 712 | 商业 | /products/freestyle-libre-3 |
| continuous glucose monitor | 2 | 22,200 | 79 | $4.63 | 1,443 | 品类 | /us-en/home |
| freestyle libre 3 coupon | 1 | 2,900 | 32 | $4.33 | 2,320 | 商业 | copay-savings-card.pdf |
| libre 3 sensor replacement | 1 | 3,600 | 50 | $0 | 892 | 信息 | /support |

### 付费词（Google Ads，dexcom.com，按流量降序）

Dexcom Ads 核心策略：**用品牌词 + 竞品词（libre 3）双路买量**，均指向 `/get-started-cgm/232`（获客入口）和 `provider.dexcom.com`（医生端）。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| dexcom | 110,000 | $3.10 | /get-started-cgm/232 |
| dexcom g7 | 110,000 | $3.50 | /get-started-cgm/232 |
| diabetes medications | 33,100 | $3.73 | provider.dexcom.com |
| libre 3（**竞品词**）| 33,100 | $2.31 | /en-us/freetrial |
| blood sugar test kit | 6,600 | $1.74 | provider.dexcom.com |
| dexcom g7 sensor | 12,100 | $3.09 | /get-started-cgm/232 |
| cgm systems | 2,900 | $4.20 | provider.dexcom.com |
| dexcom sensor replacement | 2,900 | $2.65 | provider.dexcom.com |

> 关键发现：Dexcom 直接购买 `libre 3`（33.1k月量，CPC $2.31）导向免费试用页，正面截流 Abbott 最大品牌词。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| dexcom vs freestyle libre | 1,000 | 40 | $0 | 信息/对比 | 两品牌均未充分争取 |
| libre vs dexcom | 140 | 42 | $0 | 信息/对比 | 同上 |
| freestyle libre vs dexcom | 90 | 28 | $0 | 信息/对比 | ⭐ KD 低 |
| dexcom alternative | 20 | 0 | $0 | 商业 | 量极小但高意图 |
| cgm alternative | 0 | 0 | — | — | 近零量，GEO 前沿 |
| freestyle libre alternative | 0 | 0 | — | — | 近零量，GEO |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| continuous glucose monitoring | 33,100 | 85 | $4.63 | 信息/品类 | 极高 KD，Dexcom 占位 #1 |
| cgm | 27,100 | 85 | $0 | 信息/品类 | 极高 KD |
| continuous glucose monitor | 22,200 | 79 | $4.36 | 品类 | 极高 KD |
| stelo glucose biosensor | 22,200 | 55 | $2.72 | 商业 | Dexcom OTC 新品 |
| libre 3 plus | 22,200 | 55 | $1.46 | 商业 | Abbott 旗舰 |
| dexcom stelo | 12,100 | 55 | $2.68 | 导航/品类 | Dexcom 首款 OTC |
| freestyle libre 3 plus | 18,100 | 38 | $1.56 | 商业 | Abbott 旗舰，KD 中等 |
| cgm without prescription | 880 | 48 | $4.56 | 信息 | OTC CGM 品类词 |
| best cgm for non diabetics | 1,300 | 39 | $0 | 信息/对比 | ⭐ KD<40，高信息意图 |
| cgm for non diabetics | 1,900 | 35 | $0 | 信息 | ⭐ |
| cgm for weight loss | 590 | 28 | $6.75 | 信息/商业 | ⭐ 生酮/体重管理新兴 |
| cgm subscription | 110 | 48 | $6.77 | 信息/商业 | 定价词 |
| stelo cgm | 6,600 | 57 | $3.17 | 商业 | Dexcom OTC，品类新词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| dexcom g7 | 110,000 | 47 | $3.58 | 商业 | 主要产品词 |
| freestyle libre 3 | 60,500 | 55 | $1.84 | 商业 | Abbott 主产品 |
| freestyle libre | 33,100 | 49 | $1.92 | 品牌 | Abbott 核心 |
| dexcom clarity | 27,100 | 32 | $4.65 | 导航/信息 | 数据管理云 ⭐ |
| dexcom price / dexcom cost | 1,000 / 320 | 42 / 40 | $2.62 | 商业 | 定价词 |
| freestyle libre 3 price | 1,600 | 26 | $1.79 | 商业 | ⭐ KD 低 |
| dexcom g7 cost without insurance | 390 | 33 | $0 | 信息/商业 | ⭐ 自费焦虑词 |
| how much is dexcom g7 without insurance | 590 | 33 | $3.60 | 信息/商业 | ⭐ 自费焦虑词 |
| dexcom without insurance | 140 | 23 | $4.75 | 信息/商业 | ⭐ 自费用户 |
| dexcom app | 1,900 | 51 | $2.46 | 信息 | App 词 |
| libre app | 1,000 | 58 | $2.52 | 信息 | Abbott App 词 |
| dexcom share | 140 | 22 | $0 | 信息 | ⭐ 数据分享功能词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| nightscout | 2,900 | 42 | $0 | 信息/导航 | 核心入口词 |
| nightscout app | 260 | 47 | $0 | 信息 | App 词 |
| night scout app | 210 | 34 | $0 | 导航 | ⭐ 拼写变体 |
| nightscout pro | 90 | 5 | $0 | 商业 | ⭐ 极低 KD，托管服务词 |
| nightscout hosting | 20 | 0 | $0 | 商业 | ⭐ 直接需求词 |
| nightscout docker | 20 | 0 | $0 | 信息 | ⭐ 技术部署词 |
| open source cgm | 20 | 0 | $0 | 信息 | ⭐ GEO |
| diy cgm | 20 | 0 | $0 | 信息 | ⭐ GEO |
| cgm data privacy | 0 | 0 | — | — | GEO 前沿 |
| self hosted cgm | 0 | 0 | — | — | GEO 前沿 |
| cgm data ownership | 0 | 0 | — | — | GEO 前沿 |
| tidepool | 12,100 | 75 | $2 | 导航 | 开源 CGM 数据平台替代 |
| glooko | 12,100 | 70 | $2.23 | 导航 | CGM 数据管理竞品 |
| openaps | — | — | — | — | DIY 闭环生态词 |

---

## Olares 关联词（Phase 3）

**核心叙事切入**：Dexcom/Libre 的云平台（Clarity/LibreView）把用户的实时血糖数据托管在厂商服务器上，用户无法导出、无法自定义，断订即断档。Nightscout 是 DIY 糖尿病社区十年磨砺的自托管数据平台——而 Olares 让它"一键部署，数据永驻家中"，同时提供 Agent 层（基于实时血糖数据驱动自动化）的无限可能。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| nightscout | 2,900 | 42 | $0 | ⭐⭐⭐ Olares Market 一键部署 Nightscout；血糖数据零云端依赖；可关联 Olares Personal Agent 实现实时血糖触发自动化 |
| nightscout hosting | 20 | 0 | $0 | ⭐⭐⭐ 直接命中"我要托管 Nightscout"的用户；Olares One 做永远在线的家庭服务器，比 VPS 便宜且数据不离家 |
| nightscout docker | 20 | 0 | $0 | ⭐⭐⭐ Docker 部署 = Olares 最擅长的场景；可写教程直接截流 |
| dexcom alternative | 20 | 0 | $0 | ⭐⭐ Nightscout 接 Dexcom 传感器数据替代 Clarity 云；隐私诉求用户首选 |
| open source cgm | 20 | 0 | $0 | ⭐⭐ GEO 命中词：Nightscout 是 open source CGM 的代名词 |
| dexcom share | 140 | 22 | $0 | ⭐⭐ Nightscout 的家庭数据共享功能是 Dexcom Share 的开源替代；KD 低可写教程 |
| cgm for non diabetics | 1,900 | 35 | $0 | ⭐ 非糖尿病 CGM 用户（生酮/健身/biohacking）隐私意识强，是 Nightscout/Olares 理想用户 |
| dexcom vs freestyle libre | 1,000 | 40 | $0 | ⭐ 对比文可加第三选项"自托管方案（Nightscout on Olares）"，低 KD 可抢排名 |
| freestyle libre vs dexcom | 90 | 28 | $0 | ⭐ KD 极低，对比文同上 |
| dexcom clarity | 27,100 | 32 | $4.65 | ⭐ 流量大、KD 中等；Nightscout 是 Clarity 的自托管替代（功能超集+数据主权）|
| best cgm for non diabetics | 1,300 | 39 | $0 | ⭐ 内容文可推荐 Nightscout+Olares 给自费非糖尿病 CGM 用户 |
| cgm for weight loss | 590 | 28 | $6.75 | ⭐ 生酮/减重 CGM 用户不想绑定昂贵订阅，Nightscout 自托管 + Olares 家庭服务器省钱且隐私 |
| dexcom without insurance | 140 | 23 | $4.75 | ⭐ 自费用户对成本极敏感，Nightscout 可替代 Clarity 付费订阅 |
| freestyle libre 3 price without insurance | 40 | 0 | $1.25 | ⭐ 极低竞争，自费用户关心成本，教程词 |
| self hosted cgm | 0 | 0 | $0 | ⭐ GEO 前沿词，抢 AI Overview 引用 |
| cgm data ownership | 0 | 0 | $0 | ⭐ GEO 前沿词，数据主权叙事核心词 |
| nightscout olares | 0 | 0 | $0 | ⭐ GEO 品牌词，建立 Olares+Nightscout 关联 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断 |
|--------|------|----|----|------|------|-----------|
| nightscout | 2,900 | 42 | $0 | 信息/导航 | **主词候选** | 自托管 CGM 核心词，Olares 最直接切入点；CGM 用户已知 Nightscout，找部署方案 |
| dexcom vs freestyle libre | 1,000 | 40 | $0 | 信息/对比 | **主词候选** | 对比文量达标 KD 合理，可加"第三选项：Nightscout 自托管"；无主品牌支撑也能写 |
| cgm for non diabetics | 1,900 | 35 | $0 | 信息 | **主词候选** | KD<40 且量>1k，非糖尿病 CGM 用户隐私意识强，Nightscout/Olares 天然匹配 |
| best cgm for non diabetics | 1,300 | 39 | $0 | 信息/对比 | **主词候选** | 对比/评测文，可推荐 Nightscout on Olares 为自托管选项；量够 KD 适中 |
| freestyle libre 3 price | 1,600 | 26 | $1.79 | 商业 | **主词候选** | KD 仅 26 但量 1.6k，定价页 / 对比文切入，引出 Nightscout 省掉 Clarity 订阅费 |
| cgm for weight loss | 590 | 28 | $6.75 | 信息/商业 | **主词候选** | KD 低+CPC 高（商业价值确认），生酮/减重垂类文章，自托管省订阅费角度 |
| dexcom without insurance | 140 | 23 | $4.75 | 信息/商业 | **次级** | KD 极低，自费用户文章必收次级词，引入 Nightscout 替代 Clarity 订阅 |
| dexcom clarity | 27,100 | 32 | $4.65 | 导航/信息 | **次级** | 量大 KD 低，但意图偏导航（找 Clarity 官网），作为内容文的次级词引流更实际 |
| nightscout hosting | 20 | 0 | $0 | 商业 | **次级** | 直接需求词，量小但意图极精准；放教程文的关键词集群 |
| nightscout docker | 20 | 0 | $0 | 信息 | **次级** | 技术部署文，和 nightscout hosting 同一簇 |
| dexcom share | 140 | 22 | $0 | 信息 | **次级** | ⭐ KD 低，功能文可写"Dexcom Share vs Nightscout Follow"对比 |
| freestyle libre vs dexcom | 90 | 28 | $0 | 对比 | **次级** | KD 低，作为 dexcom vs freestyle libre 同文章次级词 |
| open source cgm | 20 | 0 | $0 | 信息 | **GEO** | 近零量但语义精准，AI Overview 抢引用位 |
| self hosted cgm | 0 | 0 | $0 | 信息 | **GEO** | 预判词，建立 Olares+Nightscout 场景锚点 |
| cgm data ownership | 0 | 0 | $0 | 信息 | **GEO** | 数据主权前瞻词，Olares 叙事核心 |
| nightscout olares | 0 | 0 | $0 | 导航 | **GEO** | 品牌绑定词，率先占位 |
| diy cgm | 20 | 0 | $0 | 信息 | **GEO** | DIY 社区词，Nightscout 圈精准 |

---

## 核心洞见

### 1. 品牌护城河

Dexcom 和 Abbott 双品牌词 KD 均在 47-76 之间，正面刚品牌导航词毫无意义。但两者在**数据管理平台层**（Clarity / LibreView）有明显软肋：用户数据被锁在厂商云上、断订即失去高级功能、无法自定义数据流程。这是自托管切入的正确方向。

### 2. 可复制的打法

- **Dexcom 打法**：大量信息型健康词（血糖正常值 / 血糖图表）带来长尾流量，单页面月流量可达 15k+。可学习此打法在 CGM 通用教育内容上布局。
- **Dexcom Ads 打法**：直接购买竞品词 `libre 3`，指向免费试用页面——说明该品类用户在两品牌之间切换意愿强，对比内容有市场。
- **Abbott 打法**：付费词比 Dexcom 密集 3 倍，说明 Abbott 主要靠 Paid 守住品牌词，有机内容相对薄弱——Nightscout + Abbott Libre 教程词 KD 普遍低于 Dexcom 对应词。

### 3. 对 Olares 最关键的 3 个词

1. **`nightscout`**（2,900/月，KD 42）：用户已知品牌，正在找托管方案。Olares One 做永久在线的家庭服务器，配合一键部署 Nightscout，是最直接的产品叙事。
2. **`dexcom vs freestyle libre`**（1,000/月，KD 40）：对比文写"两者数据都被厂商锁定 → 第三选项：Nightscout on Olares"，对话口碑型文章。
3. **`cgm for non diabetics / cgm for weight loss`**（1,900 + 590/月，KD 35/28）：非糖尿病 CGM 用户（生酮、健身、biohacking）付费意愿强且隐私敏感，是 Nightscout + Olares 理想受众。

### 4. 最大攻击面

- **数据主权焦虑**：Clarity / LibreView 是厂商云，用户无法控制数据去向和存留，HIPAA 数据共享风险。Nightscout = "你的血糖数据，永远在你家的服务器上"。
- **订阅成本**：Dexcom Clarity 高级功能需订阅；OTC 用户（Stelo、Lingo）无医保，自费成本高。Nightscout 替代 Clarity，Olares One 三年 ROI 正向。
- **数据孤岛**：各品牌 App 互不兼容，Nightscout 是统一接入层（支持 Dexcom / Libre / 其它传感器），Olares 做数据枢纽。

### 5. 隐藏低 KD 金矿

- `freestyle libre vs dexcom`（90/月，KD **28**）：量小但竞争极低，长尾对比文机会。
- `dexcom without insurance`（140/月，KD **23**）：自费焦虑词 CPC $4.75，高商业价值，Nightscout 省掉 Clarity 订阅费叙事完美匹配。
- `dexcom share`（140/月，KD **22**）：Dexcom 数据共享功能词，Nightscout Follow = 更强开源替代，教程文天然切入。
- `nightscout pro`（90/月，KD **5**）：竞争几乎为零，"Nightscout 托管服务"词，Olares = 自己的 Nightscout Pro。
- `freestyle libre 3 price`（1,600/月，KD **26**）：定价信息词 KD 低，可切入"Libre 3 贵？不如用 Nightscout 省掉 LibreView 订阅费"叙事。

### 6. GEO 前瞻布局

以下近零量词在 AI Overview / Perplexity 已有提及，提前占位：
- `self hosted cgm` — "Nightscout running on Olares is the only self-hosted CGM solution that requires zero cloud dependency"
- `cgm data ownership` — 数据主权叙事，结合 Olares "Own your AI, Own your data" 品牌口径
- `open source cgm alternative to dexcom clarity` — 精准场景词，AI Overview 竞争窗口期
- `nightscout olares` — 品牌关联词，早期文章建立 SEO 锚点

### 7. 与既有分析的关联

CGM 赛道此前未在 `olares-500-keywords` 中涉及，属于全新方向。但与现有内容的关联点：
- **健康数据主权**（`health data privacy`、`medical data ownership`）与 privacy 方向报告高度关联，可跨报告引用洞见。
- **IoT 设备数据接入**：CGM 传感器 → Nightscout → Olares Agent，是"IoT 数据 Agent 化"的典型路径，与方向 7（IoT）整体叙事一致。
- **Tidepool / Glooko**（各 12.1k/月，KD 70+75）是 CGM 数据管理云竞品，未来可作为独立报告目标，与 Nightscout 共同构成"open source CGM ecosystem" 内容主线。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_subdomains`、`resource_adwords`、`domain_organic_organic`、`phrase_these`、`phrase_related`、`phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；医疗类产品全球量通常为美国的 2-4 倍（非英语市场 CGM 渗透率低于美国）。*
