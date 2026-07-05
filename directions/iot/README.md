# iot/ — IoT / 家居 / 穿戴竞品与报告

这里集中管理**闭源家居 / 穿戴硬件与生态**（智能家居系统、个人健康平台、语音中枢、音箱、摄像头、安防、门锁门铃、AI 录音硬件、健康可穿戴，以及照明 / 插座 / 温控 / 传感器 / 扫地机 / 家电 / 智能电视 / 婴儿监视 / 宠物 / 看护 / 网联车 / 能源 / 智能眼镜等外围与敏感 IoT）。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 7，结构对齐 [commerce/](/Users/pengpeng/seo/directions/commerce)、[market/](/Users/pengpeng/seo/directions/market)、[model/](/Users/pengpeng/seo/directions/model)。

## 结构

- [iot.md](/Users/pengpeng/seo/directions/iot/iot.md)：品牌清单，按 **2 大类 / 22 细类** 分组，每条标注母公司、市场地位 / 融资、Olares 平替方案与 brand-seo 状态（⬜ 待做）。只收面向海外市场的硬件 / 生态品牌（偏软件、已在 commerce 的产品不重复；中国内销专属产品不列）。
- [research/](/Users/pengpeng/seo/directions/iot/research)：品类级 **deep-research 调研底稿**（每细类一份，按「系统章 / 硬件章」两级归档，各带同名 `.notes/` 发现笔记）。这是筛品牌、定选题的依据。
- [reports/](/Users/pengpeng/seo/directions/iot/reports)：**针对关键词的 brand-seo 结果**（逐品牌一份），按 `<章>/<细类>/<brand>.md` 归档。目录树已预建、`.gitkeep` 占位，写报告时直接落到对应细类。

### 目录树（编号英文 slug）

`research/` 与 `reports/` 共用同一套两章 / 22 细类结构：

- `01-systems/` — 系统章（软件中枢 / 聚合层）：`smart-home-systems`(1)、`health-platforms`(2)
- `02-hardware/` — 硬件章（终端设备 + 外围 / 敏感 IoT）：`voice-hub`(3)、`smart-speakers`(4)、`cameras`(5)、`home-security`(6)、`locks-doorbells`(7)、`ai-recorders`(8)、`wearables`(9)、`smart-lighting`(10)、`smart-plugs`(11)、`thermostats`(12)、`sensors-hubs`(13)、`robot-vacuums`(14)、`smart-appliances`(15)、`smart-tv`(16)、`baby-monitors`(17)、`pet-cameras`(18)、`safety-trackers`(19)、`connected-cars`(20)、`energy-monitors`(21)、`smart-glasses`(22)

> 编号 `(N)` 对应 `iot.md` 的细类序号。`research/<章>/<slug>.md` 是品类 deep-research（统一 7 段骨架：摘要 / 品类概述 / 市场领导者 / 细分冠军 / VC 明日之星 / 候选关键词 / 隐私风险+Olares 平替 / 争议+参考，带 `AS_OF` 与置信度）；`reports/<章>/<slug>/<brand>.md` 是逐品牌 brand-seo。

## 命名约定

- 调研底稿：`research/<NN-章>/<slug>.md`，发现笔记同级 `<slug>.notes/`。例：`research/02-hardware/cameras.md`。
- brand-seo 报告：`reports/<NN-章>/<slug>/<brand>.md`（无日期，git 记录变更）。例：`reports/02-hardware/cameras/ring.md`、`reports/02-hardware/wearables/oura.md`。

## 清单怎么来的

IoT 硬件没有 `beclab/apps` 那样的 manifest 仓库，`iot.md` **手工维护**、不写生成器。22 份品类调研由 [deep-research](/Users/pengpeng/seo/.cursor/skills/deep-research/SKILL.md)（Lightweight 模式）产出（10-22 为外围 / 敏感 IoT 品类，已并入硬件章）。调研中的规模 / 融资是历史快照，**以后会用 Semrush + 官网重跑**。

## 怎么用

- 品类级已有 deep-research 底稿（`research/`）：top / 细分冠军 / VC 明日之星 + 候选关键词 + Olares 平替。**从 `iot.md` 挑品牌**，逐个走 `.cursor/skills/brand-seo-research/` 流程（以产品官网为 brand，找 Olares 结合点），产出落到对应细类 `reports/<章>/<slug>/<brand>.md`，再回填 `iot.md` 的平替 / 状态。
- 开源平替（Home Assistant、Frigate、Music Assistant、Gadgetbridge、Nightscout 等）归 [market/](/Users/pengpeng/seo/directions/market)，此处只作「Olares 平替」列引用，不重复登记。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`X alternative` / `self-hosted X` / `no subscription X` / `local X`——家居 / 穿戴品类里"无订阅 / 本地 / 数据不出设备"是与 Olares 叙事最贴合、竞争最低的一批词。
