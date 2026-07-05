# market/ — Olares Market 应用与竞品报告

这里集中管理 **Olares Market 已支持的应用**，以及每个应用的 brand-seo-research 报告。

## 结构

- [apps.md](/Users/pengpeng/seo/directions/market/apps.md)：去重后的应用清单（按官方 Market 分类分组），每条标注用途、对标产品与报告状态。
- [reports/](/Users/pengpeng/seo/directions/market/reports)：每个应用一份 brand-seo-research 报告，命名 `<app>.md`（无前缀、无日期，git 记录变更历史）。
- `_gen_apps.py`：从 [terminus-apps/](/Users/pengpeng/terminus-apps) 重新生成 `apps.md` 的脚本（目录更新后可重跑）。

## 应用清单怎么来的

数据源是 `beclab/apps` 的本地克隆 [terminus-apps/](/Users/pengpeng/terminus-apps)（每个应用一个 `OlaresManifest.yaml`）。365 个 manifest 按下述规则收敛为约 175 个"用户可见品牌应用"：

- 排除带 `.suspend` 标记文件的已下架应用（某品牌所有变体都下架则整体移除）。
- 按 `metadata.title`（真实品牌名）去重，版本/`share`/`client` 变体归并为一个品牌。
- 模型服务变体（`ollama*`/`vllm*`/`sglang*`/`llamacpp*`/`xinference*` 共 68 个）折叠为 5 个引擎品牌；具体型号见 [model/keywords.md](/Users/pengpeng/seo/directions/model/keywords.md)。
- 剔除 `test*`、`*client`/`*share`/`*fusion`/`*forcluster` 等伴生 chart，以及纯中间件/数据库（MySQL、Redis、RabbitMQ 等）。

## 怎么用

- 写某个应用的竞品报告：走 `.cursor/skills/brand-seo-research/` 四阶段模板，产出放到 `reports/`，再把 `apps.md` 中该应用状态改为 ✅。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 个人云/自托管平台竞品（Nextcloud、Seafile、YunoHost 等可自部署项目）也放本目录 `reports/`。商业品牌竞品（Lovable、Tailscale、Vaultwarden 等）归 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)，底层技术栈（Headscale、frp）归 [tech/reports/](/Users/pengpeng/seo/directions/tech/reports)。
