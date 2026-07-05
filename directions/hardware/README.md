# hardware/ — 加速硬件 / 整机 / NAS 竞品与报告

这里集中管理值得为 Olares One 做内容的**加速硬件、整机与 NAS 竞品**，以及每个品牌/设备的竞品报告。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 4，结构对齐 [model/](/Users/pengpeng/seo/directions/model)、[market/](/Users/pengpeng/seo/directions/market)。

## 两条信息（本方向叙事主轴）

面向"正在买 / 已买别家硬件"的人群：**A 买 Olares One**（软硬一体、开箱即用的私有云整机）；**B 在已购设备上装 Olares**（把已有算力变成随处可用的私有 AI 服务）。信息 B 平台矩阵（2026-07-05 复核 docs.olares.com）：Olares **跨平台**——Linux x86-64（裸机 ISO / script）、**ARM Linux（树莓派即官方 ARM 路径）**、**macOS Monterey 12+（含 Apple Silicon，script/Docker，有功能限制）**、**Windows（WSL2）**。"ARM not supported" 只限裸机 ISO 安装器；**Olares One 只是官方选了 x86-64 + NVIDIA 做最佳开箱体验**。差异不在"能不能装"（几乎都能），而在**体验层级**（x86+NVIDIA 满血 / Mac·Windows 跑一层有限制 / ARM Linux script 路径 / 成品 NAS 看固件是否锁定）；**GPU 加速：NVIDIA 最成熟（全 app），AMD（含 Ryzen AI Max APU，经 ROCm）/ Intel 核显均已支持，唯 Apple GPU 不被加速**（以 docs/GitHub 为准）。

## 结构（具体产品为单元）

- [devices.md](/Users/pengpeng/seo/directions/hardware/devices.md)：竞品清单，**一行 = 一个具体产品**（不再用厂商/合并行），**八大组**：① AI 加速芯片/SoC（Ryzen AI Max、NVIDIA GB10 八机型、Apple M 系含 M5 状态）② **NVIDIA RTX 5090 Mobile 游戏本**（与 GB10 并列）③ **ASUS ROG NUC**（最接近 Olares One 的 BOM）④ ≥24GB 显存 dGPU ⑤ 工作站（跨厂具体型号，不按厂商分类）⑥ **AI NAS（含高端发烧，一行一型号，按内置 GPU/可内插独显/eGPU 接口 + 购买链接）** ⑦ **企业 / 机架 / 商用 NAS**（认知词段）⑧ **个人云 / NAS OS 竞品**（TrueNAS/Unraid/CasaOS/Umbrel）。已移除 N1X/RTX Spark 行与旧"传统 NAS 厂商对照"表。游戏本本组仅作对标（非目标场景）；掌机不列。
- [research/](/Users/pengpeng/seo/directions/hardware/research)：**芯片/品类 deep-research**，每份"单元 → 穷举承载型号 SKU + 每型号候选 SEO 词 + 两条信息 × Olares 适配"，**8 份**，按组归档 `research/<NN-组>/<slug>.md`（同名 `.notes/` 存溯源笔记）；`gap-analysis.md` 留 research 根作跨组审计。走 `.cursor/skills/deep-research/` 流程。
- [reports/](/Users/pengpeng/seo/directions/hardware/reports)：**报告策略"基于产品"**，按 `reports/<NN-组>/<细类>/<brand>.md` 归档（目录树 `.gitkeep` 预建，写报告直接落对应细类）。已归档 **19 份**在 [reports/_archived/](/Users/pengpeng/seo/directions/hardware/reports/_archived)：品牌级 13 份（gmktec/framework/beelink/minisforum/asrock/system76/hp-omen/asus/lenovo/dell-alienware/acer/msi/razer）+ 传统 NAS 对照 5 份（synology/qnap/asustor/terramaster/wd-mycloud）+ 无洞见综述 1 份（ai-newbrands），均不再从 devices.md 直链（写产品报告时取旧洞见去重）。devices.md 未覆盖的产品行标 ⬜ 待做（产品级报告 backlog）。

### 目录树（编号中文组名 / 英文 slug）

`research/` 与 `reports/` 共用同一套八组结构，组编号对齐 devices.md：

- `01-ai-soc/` — AI 加速芯片/SoC：research `amd-ryzen-ai-max`、`nvidia-gb10`、`apple-m-series`；reports 细类 `gb10/`(nvidia-dgx)、`apple-silicon/`(apple-silicon)、`strix-halo/`(待做)
- `02-5090-laptops/` — RTX 5090 Mobile 游戏本：research `rtx-5090-mobile-laptops`；reports 待做
- `03-rog-nuc/` — ASUS ROG NUC：research `rog-nuc`；reports 待做
- `04-dgpu/` — ≥24GB dGPU：research `dgpu-24gb-plus`；reports 细类 `nvidia/`(rtx-3090/rtx-4090/rtx-50-series/rtx-pro-6000)、`amd/`(radeon-high-end)、`intel/`(intel-arc)
- `05-workstation/` — 工作站：research 待做；reports 待做
- `06-ai-nas/` — AI NAS（含高端发烧）：research `ai-nas`（合并高端机型）；reports 细类 `ai-nas/`(ugreen-nas/zspace/zimaos-zimacube；高端机型产品报告亦落此)
- `07-enterprise-nas/` — 企业/机架/商用 NAS：research `enterprise-nas`；reports 待做（`.gitkeep`）
- `08-nas-os/` — 个人云/NAS OS 竞品：reports `truenas`/`unraid`/`casaos`/`umbrel`（无 research，OS 层竞品）

## 命名约定

- 调研底稿：`research/<NN-组>/<slug>.md`，发现笔记同级 `<slug>.notes/`；跨组审计 `research/gap-analysis.md`。例：`research/06-ai-nas/ai-nas.md`。
- 产品/品牌报告：`reports/<NN-组>/<细类>/<brand>.md`（无日期，git 记录变更）。例：`reports/04-dgpu/nvidia/rtx-4090.md`、`reports/08-nas-os/truenas.md`。
- 废弃报告：`reports/_archived/<brand>.md`（扁平，历史快照，不删）。

## 清单怎么来的

硬件没有 `beclab/apps` 那样的 manifest 仓库，所以 `devices.md` **手工维护**、不写生成器。报告中的流量/规格是历史快照，**以后会用 Semrush 重跑**（GPU 型号作 brand），内容细节待修订。

## 怎么用

- 找型号级切入词、看某芯片/品类下有哪些承载型号：读 [research/](/Users/pengpeng/seo/directions/hardware/research) 对应 `<slug>.md`。新增芯片/品类单元走 `.cursor/skills/deep-research/`（穷举型号 SKU + 每型号候选词 + 两条信息适配，产出落 `research/`）。
- 写/重跑某个品牌报告：走 `.cursor/skills/brand-seo-research/` 流程（以品牌官网为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出落对应细类 `reports/<NN-组>/<细类>/<brand>.md`，再更新 `devices.md` 承载型号行。
- 把 research 落成对比/教程文（`X vs Olares One`、"大显存卡吃灰→装 Olares OS"）：走 `.cursor/skills/seo-content/`。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`home ai server` / `linux mini pc` / `ai workstation build` / `dgx spark alternative` / `synology alternative` / `X vs Olares One`——硬件方向低 KD 金矿密集，Olares One 是这些内容的落地硬件。
