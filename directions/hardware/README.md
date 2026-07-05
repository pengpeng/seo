# hardware/ — 加速硬件 / 整机 / NAS 竞品与报告

这里集中管理值得为 Olares One 做内容的**加速硬件、整机与 NAS 竞品**，以及每个品牌/设备的竞品报告。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 4，结构对齐 [model/](/Users/pengpeng/seo/directions/model)、[market/](/Users/pengpeng/seo/directions/market)。

## 结构

- [devices.md](/Users/pengpeng/seo/directions/hardware/devices.md)：设备/竞品清单（按 Mini PC/工作站、AI 加速整机/Apple Silicon、独显/GPU、大厂 PC/工作站、NAS 系统/整机分组），每条标注场景与 Olares One 对标角度。首要人群是专业/旗舰独显 prosumer、Apple Silicon、Spark/Strix Halo 整机；游戏本与掌机不是目标场景。
- [reports/](/Users/pengpeng/seo/directions/hardware/reports)：每个品牌/设备一份报告，命名 `<brand>.md`（无 `nas-` 前缀、无日期，git 记录变更历史）；跨品牌对比洞见就近归到最相关的单品报告。**GPU 以型号/系列为调研单元**（`rtx-50-series`、`rtx-4090`、`rtx-3090`、`radeon-high-end`、`intel-arc`、`rtx-pro-6000`）、Apple Silicon 一份（`apple-silicon`），对齐 [model/](/Users/pengpeng/seo/directions/model) 的 per-family 结构。

## 清单怎么来的

硬件没有 `beclab/apps` 那样的 manifest 仓库，所以 `devices.md` **手工维护**、不写生成器。报告中的流量/规格是历史快照，**以后会用 Semrush 重跑**（GPU 型号作 brand），内容细节待修订。

## 怎么用

- 写/重跑某个品牌报告：走 `.cursor/skills/brand-seo-research/` 流程（以品牌官网为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出覆盖 `reports/<brand>.md`，再更新 `devices.md` 状态。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`home ai server` / `linux mini pc` / `ai workstation build` / `dgx spark alternative` / `synology alternative` / `X vs Olares One`——硬件方向低 KD 金矿密集，Olares One 是这些内容的落地硬件。
