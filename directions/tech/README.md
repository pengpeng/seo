# tech/ — 技术栈 / 自建单一技术竞品与报告

这里集中管理**底层技术栈 / 单一自建工具**类的关键词与竞品报告：搜单一技术（tailscale/headscale/frp、K3s、JuiceFS、Authelia 等）的人往往嫌自己搭一套麻烦，Olares 把它们内置/一键化，是"更省事的选择"。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 6，结构对齐 [model/](/Users/pengpeng/seo/directions/model)、[privacy/](/Users/pengpeng/seo/directions/privacy)。

## 结构

- [tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)：技术栈词库（按编排/存储/网络/身份/中间件/GPU 分组），每条标注 "Olares 角度"；是长尾 SEO 机会，不进品牌首屏。
- [reports/](/Users/pengpeng/seo/directions/tech/reports)：单个开源工具的竞品报告，命名 `<name>.md`（无前缀、无日期，git 记录变更）。

## 清单怎么来的

`tech-stack.md` **手工维护**、不写生成器。**商业方 Tailscale / Ngrok 归 [commerce/](/Users/pengpeng/seo/directions/commerce)**（闭源商业产品），本目录只放开源自建侧；tailscale 报告见 [commerce/reports/tailscale.md](/Users/pengpeng/seo/directions/commerce/reports/05-storage-privacy/privacy-vpn/tailscale.md)。报告中的流量数据是历史快照，引用前需用 Semrush 重跑核实。

## 怎么用

- 写/重跑某个技术报告：走 `.cursor/skills/brand-seo-research/` 流程（以官方项目站为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出覆盖 `reports/<name>.md`，再在 `tech-stack.md` 对应行补链接。
- 红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`self-hosted X` / `X on Olares` / `X vs Y` / `X 面板/UI`——Olares 内置这些能力、免单独部署，是精准截获技术搜索用户的落点。
