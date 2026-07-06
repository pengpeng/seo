# privacy/ — 隐私 / 安全竞品与格局

这里管理两条线：(1) 值得为 Olares 做内容的**隐私/安全类竞品**（隐私搜索、加密邮件、加密云存储、GDPR 合规等）及其竞品报告；(2) 隐私**格局**分类总图（合规立法、认证标准、重大事件、AI concern、巨头监控、用户诉求）及其 deep-research。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 5，结构对齐 [model/](/Users/pengpeng/seo/directions/model)、[market/](/Users/pengpeng/seo/directions/market)、[iot/](/Users/pengpeng/seo/directions/iot)。

## 结构

- [services.md](/Users/pengpeng/seo/directions/privacy/services.md)：**隐私产品竞品总索引**——两层：(1) 数据隐私核心品类（搜索浏览器/邮件/存储/合规）的**自有垂直报告** → 走 brand-seo；(2) 跨目录**指针引用**（闭源明星→commerce、开源→market/tech），不重复登记。相邻品类（密码、VPN/远程访问）只做指针、不当主体。**归类规则**：产品实体按 [AGENTS.md](/Users/pengpeng/seo/AGENTS.md) 可拥有性归位（闭源商业明星→commerce、开源→market/tech），privacy 只做隐私视角聚合与垂直报告。
- [landscape.md](/Users/pengpeng/seo/directions/privacy/landscape.md)：**隐私格局分类总图**（7 大类/约 39 子方向 + 核心 SEO 词 + Olares 落点，覆盖**个人 + 企业**两侧需求）→ 借合规/事件/概念/企业自部署热度做内容。
- [research/](/Users/pengpeng/seo/directions/privacy/research)：格局分类总图的 6 份 deep-research 底稿 + [registry.md](/Users/pengpeng/seo/directions/privacy/research/registry.md) 引证登记（见 [research/README.md](/Users/pengpeng/seo/directions/privacy/research/README.md)）。
- [reports/](/Users/pengpeng/seo/directions/privacy/reports)：产品竞品报告在根目录，命名 `<name>.md`（无 `privacy-` 前缀、无日期，git 记录变更历史）；格局话题文按 `<分类>/<子方向>/<slug>.md` 落子目录（本轮占位）。跨产品洞见就近归到最相关的单品报告。

## 清单怎么来的

`privacy-keywords.md` 是隐私需求关键词总览。密码管理竞品（Bitwarden/1Password/KeePassXC/Vaultwarden）归 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)（1password、keepassxc、bitwarden、vaultwarden）。报告中的流量数据是历史快照，**以后会用 Semrush 重跑**，内容细节待修订。清单 **手工维护**、不写生成器。

## 怎么用

- 写/重跑某个产品报告：走 `.cursor/skills/brand-seo-research/` 流程（以产品官网为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出覆盖 `reports/<name>.md`，再更新 `services.md` 状态。
- 商业隐私 SaaS（Proton / Bitwarden / Tailscale / Ngrok）在 [commerce/](/Users/pengpeng/seo/directions/commerce)；红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`X alternative` / `self-hosted X` / `gdpr compliant ai` / `digital sovereignty`——Olares 本地部署 + 数据不出设备是隐私叙事的天然落点。
