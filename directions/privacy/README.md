# privacy/ — 隐私 / 安全竞品与报告

这里集中管理值得为 Olares 做内容的**隐私/安全类竞品**（隐私搜索、加密邮件、加密云存储、GDPR 合规等），以及每个产品的竞品报告。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 5，结构对齐 [model/](/Users/pengpeng/seo/directions/model)、[market/](/Users/pengpeng/seo/directions/market)。

## 结构

- [services.md](/Users/pengpeng/seo/directions/privacy/services.md)：产品清单（按隐私搜索/浏览器、加密邮件与协作、加密云存储、合规、关键词总览分组），每条标注场景与 Olares 平替角度。
- [reports/](/Users/pengpeng/seo/directions/privacy/reports)：每个产品一份报告，命名 `<name>.md`（无 `privacy-` 前缀、无日期，git 记录变更历史）；跨产品洞见就近归到最相关的单品报告。

## 清单怎么来的

`privacy-keywords.md` 是隐私需求关键词总览。密码管理竞品（Bitwarden/1Password/KeePassXC/Vaultwarden）归 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)（1password、keepassxc、bitwarden、vaultwarden）。报告中的流量数据是历史快照，**以后会用 Semrush 重跑**，内容细节待修订。清单 **手工维护**、不写生成器。

## 怎么用

- 写/重跑某个产品报告：走 `.cursor/skills/brand-seo-research/` 流程（以产品官网为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出覆盖 `reports/<name>.md`，再更新 `services.md` 状态。
- 商业隐私 SaaS（Proton / Bitwarden / Tailscale / Ngrok）在 [commerce/](/Users/pengpeng/seo/directions/commerce)；红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`X alternative` / `self-hosted X` / `gdpr compliant ai` / `digital sovereignty`——Olares 本地部署 + 数据不出设备是隐私叙事的天然落点。
