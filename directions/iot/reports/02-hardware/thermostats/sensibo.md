# Sensibo SEO 竞品分析报告

> 域名：sensibo.com | SEMrush US | 2026-07-06
> 以色列 Smart AC Controller 品牌，IR 红外智控空调/热泵领域的全球头部云服务商，核心弱点是云依赖+订阅制

---

## 项目理解（前置）

Sensibo 是一家以色列智能家居公司（2013 年创立，总部特拉维夫），主卖红外（IR）智能空调控制器——将任何带遥控器的空调/热泵升级为 Wi-Fi 智能设备，通过 App/语音/API 远程控制。产品线覆盖 Sky（$79，入门）、Air（$109-125，HomeKit 认证）、Air Pro（$129，内置 CO₂/TVOC 空气质量传感器）。核心卖点是"设备只要有 IR 遥控器就能接入"，兼容万种机型，支持地理围栏节能。**致命弱点**：完全云依赖，HA 社区明确确认"无本地 API/本地控制"；进阶自动化（Climate React）需 Sensibo Plus 订阅（~$4/月或 $30/年），是用户最大抱怨点。

| 项目 | 内容 |
|------|------|
| 一句话定位 | IR 空调智控器，云 API 驱动，让旧空调联网 |
| 开源 / 许可证 | 闭源；官方 Python 库 `pysensibo` 开源（MIT），HA 集成依赖云 API Key |
| 主仓库 | 无主开源仓库；[sensibo/pysensibo](https://github.com/sensibo/pysensibo)（★ 百量级） |
| 核心功能 | IR 万能遥控 + App/语音控制、7 天定时、地理围栏、Climate React 自适应节能、空气质量（Air Pro） |
| 商业模式 / 定价 | 硬件一次购买（$79-$129）+ Sensibo Plus 订阅（~$30/年）锁高级功能 |
| 差异化 / 价值主张 | HomeKit 原生认证（Air/Air Pro）、10,000+ 机型 IR 码库、设置简单（分钟级）|
| 主要竞品（初判）| Cielo WiGle / tado° Smart AC / Broadlink RM4（DIY 平替） |
| Olares Market | 未上架（Sensibo 本身为闭源云硬件；开源平替 Home Assistant 已在 Market） |
| 来源 | [sensibo.com](https://sensibo.com)、[support.sensibo.com/community-integrations/home-assistant/](https://support.sensibo.com/community-integrations/home-assistant/)、HA 社区 / SmartHomeU 评测 |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | sensibo.com |
| SEMrush Rank | 297,344 |
| 自然关键词数 | 9,895 |
| 月自然流量（US）| 5,518 |
| 自然流量估值 | $15,305/月 |
| 付费关键词数 | 83 |
| 月付费流量 | 888 |
| 付费流量费用 | $5,766/月 |
| 排名 1-3 位 | 82 词 |
| 排名 4-10 位 | 311 词 |
| 排名 11-20 位 | 820 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| sensibo.com | 2,453 | 4,655 | 84.4% |
| learn.sensibo.com | 7,218 | 558 | 10.1% |
| support.sensibo.com | 210 | 273 | 4.9% |
| home.sensibo.com | 6 | 32 | 0.6% |

> **关键洞见**：learn.sensibo.com 收录了 7,218 个关键词（占总词数 73%），却只贡献 10% 流量——内容博客规模巨大但排名普遍靠后（10-50 位）。说明内容投入已到位但 SEO 尚未收割。sensibo.com 主域 2,453 词就撑起 84% 流量，品牌词护城河极强。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| sensibo | 1 | 1,300 | 54 | $4.32 | 1,040 | 品牌/导航 | sensibo.com/ |
| sensibo hub | 1 | 880 | 41 | $0 | 704 | 信息/导航 | sensibo.com/ |
| sensibo pod | 1 | 480 | 25 | $0 | 384 | 信息/导航 | sensibo.com/ |
| power efficient air conditioners | 8 | 12,100 | 24 | $1.25 | 84 | 信息 | blogs/energy-efficient-air-conditioners |
| fan mode in ac | 1 | 320 | 9 | $0 | 79 | 信息 | blogs/use-fan-mode-in-ac |
| room with ac | 6 | 9,900 | 22 | $0.53 | 69 | 信息 | blogs/5-ways-to-cool-multiple-rooms |
| ac controller | 2 | 880 | 21 | $2.21 | 57 | 信息/商业 | products/sensibo-air |
| best price for sensibo sky | 2 | 1,600 | 21 | $0 | 56 | 商业 | products/sensibo-sky |
| a c connection | 7 | 9,900 | 15 | $12.05 | 49 | 信息 | blogs/how-to-connect-an-air-conditioner-to-wi-fi |
| ac connectivity | 6 | 14,800 | 24 | $12.05 | 38 | 商业 | blogs/how-to-connect-an-air-conditioner-to-wi-fi |
| sensibo head unit stays on celsius | 2 | 590 | 0 | $0 | 38 | 信息 | support.sensibo.com/ |
| smart ac controller | 4 | 720 | 22 | $0.71 | 25 | 商业 | products/sensibo-air |
| smart air conditioner control | 2 | 720 | 23 | $1.13 | 21 | 商业 | products/sensibo-air |
| smart aircon | 5 | 1,600 | 31 | $3.23 | 20 | 商业 | products/sensibo-air |
| sensibo air pro | 2 | 140 | 15 | $4.00 | 18 | 信息/商业 | products/sensibo-air-pro |
| ac control | 3 | 590 | 25 | $4.22 | 17 | 信息/商业 | sensibo.com/ |
| sensibo sky | 3 | 260 | 18 | $3.23 | 16 | 信息 | products/sensibo-sky |
| sensibo app | 3 | 170 | 26 | $1.88 | 13 | 信息 | sensibo.com/ |

### 付费词（Google Ads，按流量排序）

主要在 learn.sensibo.com 博客文章上投放，锁定"空调故障排查"高 CPC 词，导流后内容页植入产品购买链接——这是把技术支持内容变成获客漏斗的典型打法。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| air con not blowing cold | 1 | 4,400 | $9.65 | learn.sensibo.com/air-conditioner-running-but-not-cooling |
| ac unit not blowing cold air | 1 | 2,400 | $9.65 | learn.sensibo.com/air-conditioner-running-but-not-cooling |
| air conditioner runs but no cooling | 1 | 1,600 | $10.16 | learn.sensibo.com/air-conditioner-running-but-not-cooling |
| best price for sensibo sky | 1 | 1,600 | $0 | products/sensibo-sky |
| sensibo hub | 1 | 880 | $0 | products/sensibo-air |
| ac running but not cooling | 2 | 2,900 | $6.10 | learn.sensibo.com/air-conditioner-running-but-not-cooling |
| air conditioner not blowing cold air | 2 | 2,400 | $9.06 | learn.sensibo.com/air-conditioner-running-but-not-cooling |
| home ac not blowing cool air | 2 | 1,900 | $6.40 | learn.sensibo.com/air-conditioner-running-but-not-cooling |
| what is tvoc in air quality | 1 | 390 | $0.75 | learn.sensibo.com/what-are-tvocs-why-track-them |
| aircon mini split ac reviews | 1 | 140 | $1.13 | learn.sensibo.com/the-5-best-ductless-mini-split-air-conditioners |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| cielo breez | 480 | 14 | $0.73 | 信息/商业 | ⭐ Cielo 品牌词，KD 低 |
| cielo breez max smart ac controller | 140 | 3 | $0 | 商业 | ⭐⭐⭐ 极低 KD |
| cielo wigle | 90 | 50 | $0 | 信息/导航 | Cielo 品牌词，KD 高 |
| sensibo alternative | 20 | 0 | $3.87 | 商业 | ⭐ 极低 KD，高 CPC 信号 |
| sensibo vs cielo | 20 | 0 | $9.86 | 商业 | ⭐ 极低 KD，极高 CPC |
| sensibo vs broadlink | 20 | 0 | $0 | 信息 | ⭐ 极低 KD |
| sensibo vs ecobee | 20 | 0 | $0 | 信息 | ⭐ 极低 KD |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| smart thermostat | 165,000 | 67 | $0.85 | 信息/商业 | 大盘词，KD 极高 |
| wifi thermostat | 8,100 | 64 | $0.51 | 商业 | KD 高，竞争激烈 |
| wireless thermostat | 4,400 | 29 | $0.51 | 信息/商业 | ⭐ KD 较低 |
| smart air conditioner | 1,600 | 28 | $3.23 | 信息/商业 | ⭐ 中等 KD |
| smart thermostat for mini split | 320 | 7 | $1.25 | 信息/商业 | ⭐⭐⭐ 极低 KD，高价值 |
| smart ac controller | 720 | 22 | $0.71 | 商业 | ⭐ KD 低，核心品类词 |
| smart air conditioner control | 720 | 23 | $1.13 | 商业 | ⭐ KD 低 |
| ac controller | 880 | 38 | $2.94 | 信息/商业 | KD 适中 |
| mini split controller | 110 | 11 | $1.43 | 信息/商业 | ⭐⭐ 很低 KD |
| wifi ac controller | 140 | 23 | $0.74 | 商业 | ⭐ KD 低 |
| smart mini split controller | 30 | 17 | $1.60 | 商业 | ⭐ KD 低 |
| smart ac controller for mini split | 70 | 16 | $1.18 | 商业 | ⭐⭐ KD 低 |
| best smart ac controller | 20 | 0 | $0.90 | 商业 | ⭐ KD 极低 |

### 产品 / 功能词（Sensibo 品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| best price for sensibo sky | 1,600 | 21 | $0 | 商业 | ⭐ 比较意图，量大 KD 低 |
| sensibo air | 320 | 37 | $5.02 | 信息/商业 | 产品词，CPC 高 |
| sensibo sky | 260 | 18 | $3.23 | 信息 | ⭐ KD 低 |
| sensibo smart ac controller | 260 | 42 | $0 | 信息 | KD 偏高 |
| sensibo hub | 880 | 41 | $0 | 信息/导航 | 新产品线词，量大 |
| sensibo pod | 480 | 25 | $0 | 信息/导航 | ⭐ KD 低 |
| sensibo air pro | 140 | 15 | $4.00 | 信息/商业 | ⭐⭐ KD 低 |
| sensibo home assistant | 70 | 12 | $4.90 | 信息/集成 | ⭐⭐ KD 极低，高 CPC |
| sensibo review | 70 | 18 | $6.24 | 信息/商业 | ⭐ KD 低，高 CPC |
| sensibo installation | 70 | 9 | $0 | 信息 | ⭐⭐ KD 极低 |
| sensibo app | 170 | 26 | $1.88 | 信息 | ⭐ KD 低 |
| sensibo subscription | 20 | 0 | $0 | 信息 | ⭐ 痛点词 |
| sensibo plus | 20 | 0 | $0 | 信息 | ⭐ 痛点词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| broadlink rm4 pro | 1,000 | 9 | $0.47 | 信息 | ⭐⭐⭐ KD 极低，量大，Olares 核心词 |
| broadlink rm4 mini | 390 | 8 | $0.43 | 信息 | ⭐⭐⭐ KD 极低，Broadlink 平替 |
| home assistant climate | 260 | 20 | $0 | 信息/导航 | ⭐ KD 低，HA 集成词 |
| smartir home assistant | 140 | 18 | $0 | 信息 | ⭐⭐ KD 低，SmartIR 整合 |
| broadlink home assistant | 110 | 22 | $0 | 信息 | ⭐ HA+Broadlink 集成 |
| esphome ir blaster | 90 | 16 | $0.55 | 信息 | ⭐⭐ KD 低，DIY 方案 |
| smartir | 70 | 24 | $0 | 信息 | ⭐ HA 集成组件 |
| ir blaster home assistant | 70 | 13 | $0.36 | 信息 | ⭐⭐ KD 低 |
| ir remote home assistant | 40 | 23 | $0 | 信息 | ⭐ KD 低 |
| home assistant ir remote | 40 | 22 | $0 | 信息 | ⭐ KD 低 |
| home assistant smart thermostat | 70 | 21 | $1.16 | 信息/商业 | ⭐ KD 低 |
| esphome climate | 40 | 0 | $0 | 信息 | ⭐ 极低 KD，GEO 词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Sensibo/Cielo 强依赖云+订阅，而 HA on Olares + SmartIR/ESPHome + Broadlink RM4 提供 100% 本地控制、零订阅、完整隐私，且可在同一个平台统管全屋 IoT——这是 Olares 的完整平替叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| broadlink rm4 pro | 1,000 | 9 | $0.47 | HA on Olares + Broadlink RM4 Pro = Sensibo 零订阅平替，本地控制，全屋统管 | ⭐⭐⭐ |
| broadlink rm4 mini | 390 | 8 | $0.43 | 同上，预算版切入；"Broadlink RM4 Mini + HA on Olares 替代 Sensibo Sky" | ⭐⭐⭐ |
| smart thermostat for mini split | 320 | 7 | $1.25 | Olares Market HA 安装即得 SmartIR 支持 mini split 控制，零订阅 | ⭐⭐⭐ |
| smartir home assistant | 140 | 18 | $0 | SmartIR 是 HA 核心 IR 集成；Olares 一键装 HA = 无缝 SmartIR 使用 | ⭐⭐ |
| mini split controller | 110 | 11 | $1.43 | HA SmartIR on Olares 控制 mini split，Sensibo/Cielo 云付费方案的本地替代 | ⭐⭐ |
| broadlink home assistant | 110 | 22 | $0 | Broadlink 与 HA 集成教程；Olares 提供完整 HA 运行环境 | ⭐⭐ |
| esphome ir blaster | 90 | 16 | $0.55 | ESPHome on Olares：自建 IR 发射器直连 HA，Sensibo 的 DIY 完全本地平替 | ⭐⭐⭐ |
| sensibo home assistant | 70 | 12 | $4.90 | 用户已在问 Sensibo+HA 集成；可以转向"Broadlink+HA on Olares 无云替代 Sensibo" | ⭐⭐⭐ |
| ir blaster home assistant | 70 | 13 | $0.36 | IR blaster（Broadlink/ESP32）+ HA on Olares = 完整本地 AC 控制方案 | ⭐⭐ |
| smart ac controller for mini split | 70 | 16 | $1.18 | Olares Market HA + SmartIR 搞定所有带 IR 遥控的 mini split，无硬件锁定 | ⭐⭐ |
| sensibo alternative | 20 | 0 | $3.87 | 直接打 "Sensibo alternative"：Broadlink RM4 + HA on Olares，省订阅、本地、可扩展 | ⭐⭐⭐ |
| sensibo vs broadlink | 20 | 0 | $0 | 对比内容：Sensibo（云 $30/年）vs Broadlink+HA（一次性硬件 $30，零订阅）| ⭐⭐⭐ |
| sensibo vs cielo | 20 | 0 | $9.86 | 两者均云依赖；HA+Broadlink 可兼并双方用例的本地解法 | ⭐⭐ |
| sensibo subscription | 20 | 0 | $0 | 订阅痛点词：植入"为什么不用 Broadlink+HA，一次买断，Olares 直接装" | ⭐⭐⭐ |
| best smart ac controller | 20 | 0 | $0.90 | 对比文，引出自托管方案 Broadlink+SmartIR+HA on Olares | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| broadlink rm4 pro | 1,000 | 9 | $0.47 | 信息 | **主词候选** | KD 极低量大，是打 Sensibo 最佳入口；文章：Broadlink RM4 Pro + HA on Olares vs Sensibo |
| smart thermostat for mini split | 320 | 7 | $1.25 | 信息/商业 | **主词候选** | KD=7 量 320，mini split 用户刚需；HA on Olares+SmartIR 直接满足且无订阅 |
| broadlink rm4 mini | 390 | 8 | $0.43 | 信息 | **主词候选** | KD 极低，Broadlink 入门型；与 rm4 pro 可并入同簇文章 |
| cielo breez | 480 | 14 | $0.73 | 信息/商业 | **主词候选** | Sensibo 最直接竞品词；KD14，量 480，切入 "cielo vs sensibo vs local HA" 三方对比 |
| mini split controller | 110 | 11 | $1.43 | 信息/商业 | **主词候选** | KD 低，场景词，Olares HA 平替 Sensibo/Cielo 核心落地 |
| smart ac controller | 720 | 22 | $0.71 | 商业 | **主词候选** | 品类核心词，KD22 量 720；可做 "best smart AC controller" 对比文 |
| sensibo home assistant | 70 | 12 | $4.90 | 集成 | **主词候选** | KD12 但 CPC $4.90 极高，说明商业价值强；内容角度"Sensibo HA 集成 vs 直接 Broadlink+HA 本地控制"，Olares 直接切入 |
| esphome ir blaster | 90 | 16 | $0.55 | 信息 | **主词候选** | KD 低，DIY 受众；ESPHome on Olares 完整 tutorial 文章 |
| sensibo alternative | 20 | 0 | $3.87 | 商业 | **次级** | 量虽小但 CPC$3.87 商业信号强、KD=0；并入"Broadlink RM4 Pro Sensibo Alternative"文章 |
| smartir home assistant | 140 | 18 | $0 | 信息 | **次级** | KD18 量 140；Olares Market 安装 HA 自带 SmartIR 支持，教程词 |
| broadlink home assistant | 110 | 22 | $0 | 信息 | **次级** | KD22 量 110；并入 Broadlink+HA 主文章 |
| ir blaster home assistant | 70 | 13 | $0.36 | 信息 | **次级** | KD 低，并入 ESPHome IR 文章 |
| sensibo review | 70 | 18 | $6.24 | 信息/商业 | **次级** | CPC $6.24 极高，用户有强购买意图；可植入 Broadlink+HA 平替方案 |
| sensibo vs broadlink | 20 | 0 | $0 | 信息 | **次级** | KD=0，并入对比文章；Olares 直接作为 Broadlink 的运行平台 |
| sensibo vs cielo | 20 | 0 | $9.86 | 商业 | **次级** | KD=0，CPC $9.86 极高商业价值；扩展为"Sensibo vs Cielo vs local HA" |
| sensibo subscription | 20 | 0 | $0 | 信息 | **次级** | 订阅痛点词，并入对比/替代文 |
| smart ac controller for mini split | 70 | 16 | $1.18 | 商业 | **次级** | 并入 mini split controller 簇 |
| cielo breez max smart ac controller | 140 | 3 | $0 | 商业 | **次级** | KD=3 极低，并入 Cielo 对比内容 |
| home assistant climate | 260 | 20 | $0 | 信息/导航 | **次级** | HA 核心功能词，Olares Market 直接支持 |
| sensibo pod | 480 | 25 | $0 | 信息/导航 | **次级** | Sensibo 新产品，导航词，流量来拿 brand awareness |
| esphome climate | 40 | 0 | $0 | 信息 | **GEO** | 量近零但语义精准；在教程内容的 FAQ 里覆盖 |
| sensibo local control | 0 | 0 | $0 | 信息 | **GEO** | 搜索量近零但高频 HA 社区话题；抢 AI Overview 引用："Sensibo 不支持本地控制，替代方案是 Broadlink+HA on Olares" |
| home assistant ac local control | 0 | 0 | $0 | 信息 | **GEO** | 同上；本地控制内容的核心锚点 |
| sensibo cloud shutdown risk | 0 | 0 | $0 | 信息 | **GEO** | 用户担忧云服务停摆（"Sensibo 关服 = 变砖"）；在替代文里用 FAQ 覆盖 |

---

## 核心洞见

1. **品牌护城河**：`sensibo`（KD54）品牌词护城河中等偏强，主域名稳居第一，但品类词 `smart ac controller`（KD22）Sensibo 只排第 4，说明非品牌词竞争力一般。**不能正面刚品牌词**，但品类词和替代词有切入空间。

2. **可复制的打法**：Sensibo 核心打法是"**高 CPC 空调故障排查词**→内容博客 learn.sensibo.com → 购买转化"——他们在买 `air con not blowing cold`（$9.65/点击）这样的 HVAC 维修词，导流到 "AC 不制冷如何修" 博客，文末卖控制器。learn.sensibo.com 已积累 7,218 个词但大多排名 10-50，**内容已种、未收割**，是值得跟进的内容格局。

3. **对 Olares 最关键的词**：
   - `broadlink rm4 pro`（1,000/mo, KD9）——量最大、KD 最低、直接定位 Sensibo 平替硬件
   - `smart thermostat for mini split`（320/mo, KD7）——HA on Olares 的强场景词，极低竞争
   - `sensibo home assistant`（70/mo, KD12, CPC $4.90）——用户已在问 Sensibo+HA，可以直接转向"Broadlink+HA on Olares = 无云替代 Sensibo"

4. **最大攻击面**：**订阅制 + 云依赖**。Sensibo Plus 订阅（$30/年）锁住 Climate React 是最高频用户抱怨（评测 1 星差评主力）；完全无本地控制（HA 社区原帖确认）。Olares 叙事：Broadlink RM4（$30 一次性）+ HA on Olares（一键安装，免费）= **替代 Sensibo，永久省去 $30/年订阅，且完全本地、不怕停服**。

5. **隐藏低 KD 金矿**：
   - `broadlink rm4 pro` KD9 / `broadlink rm4 mini` KD8——硬件词极低竞争，量大
   - `smart thermostat for mini split` KD7——mini split 场景词几乎无人做 Olares 角度
   - `cielo breez max smart ac controller` KD3——Sensibo 最大直接竞品词，几乎空白
   - `sensibo alternative` / `sensibo vs broadlink` / `sensibo vs cielo` 全部 KD=0——替代词空间完全未被占据
   - `mini split controller` KD11——中量低 KD，IoT 品类长尾金矿

6. **GEO 前瞻布局**：
   - "Does Sensibo work without internet?"——云依赖确认词，抢 AI Overview 引用位
   - "Sensibo vs Home Assistant local control"——本地 vs 云对比，HA 社区高频问法
   - "ESPHome IR climate Home Assistant Olares"——长尾精准词，抢垂类 AI 引用
   - "smart AC controller without subscription"——订阅焦虑词，GEO 内容布局机会

7. **与既有分析的关联**：Olares-500 词表中 HA（Home Assistant）相关词已在 IoT 方向有布局；本报告新增了 `broadlink rm4 pro/mini`（KD 极低、量大、完全空白）、`smart thermostat for mini split`（KD7）、`sensibo home assistant`（高 CPC）等高价值增量词，尤其 Broadlink RM4 系列是本报告最大发现——量千级、KD 个位数、Olares HA 平台天然承接。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_subdomains`、`resource_adwords`、`domain_organic_organic`、`phrase_these`、`phrase_related`、`phrase_fullsearch`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
