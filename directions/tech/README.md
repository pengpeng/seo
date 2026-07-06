# tech/ — 技术栈 / 自建单一技术竞品与报告

这里集中管理**底层技术栈 / 单一自建工具**类的关键词与竞品报告：搜单一技术（tailscale/headscale/frp、K3s、JuiceFS、Authelia 等）的人往往嫌自己搭一套麻烦，Olares 把它们内置/一键化，是"更省事的选择"。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 6，结构对齐 [model/](/Users/pengpeng/seo/directions/model)、[privacy/](/Users/pengpeng/seo/directions/privacy)。

## 结构

- [tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)：**分类总表**——扁平 **11 大类**（计算/编排、存储、网络接入、数据库中间件、消息流、**可观测**、平台中间件、企业大数据、身份安全、CI-CD、AI 基础设施；IaaS/PaaS 只作行文视角）→ 子类 → **每项目一行**「介绍/许可/其它/公有云替代/Olares 状态/SEO 报告」。中间件由 KubeBlocks operator 托管（标 KB，以官方 supported-addons 为准）。新增点：网络拆 Mesh VPN 与反向代理两子类、Citus/pgvector 收为 PostgreSQL 扩展、密钥/HSM 与授权 ReBAC 归入身份/安全、CI-CD 用 Zot 镜像仓库、AI 补 Agent 沙盒与 Agent 记忆(Mem0/Zep/Letta/Cognee) 并拆开可观测评估与微调。是长尾 SEO 机会，不进品牌首屏。
- [research/](/Users/pengpeng/seo/directions/tech/research)：分类底稿（deep-research 产出），索引见 [research/README.md](/Users/pengpeng/seo/directions/tech/research/README.md)——[middleware-taxonomy.md](/Users/pengpeng/seo/directions/tech/research/middleware-taxonomy.md)（IaaS/PaaS 视角逐项目深挖中间件，76 源）、[cloud-infra-taxonomy.md](/Users/pengpeng/seo/directions/tech/research/cloud-infra-taxonomy.md)（CNCF×三云映射）、[ai-infra.md](/Users/pengpeng/seo/directions/tech/research/ai-infra.md)（AI 基础设施）；README 附「二轮核实来源」溯源登记。
- [reports/](/Users/pengpeng/seo/directions/tech/reports)：单个开源工具的竞品报告，按 **11 大类子目录**组织（仿 commerce 两级，如 `03-network/mesh-vpn/headscale.md`、`03-network/reverse-proxy/frp.md`），命名 `<name>.md`（无前缀、无日期，git 记录变更）。

## 清单怎么来的

分类总表由 deep-research 底稿（CNCF landscape × AWS/Azure/GCP 服务 × AI-infra 栈 × KubeBlocks 收录引擎）归一到 IaaS/PaaS 视角，之后**手工维护**、不写生成器。**中间件锚点**：Olares 平台层中间件由 KubeBlocks operator 托管、`OlaresManifest.yaml` 声明式依赖、自动注入凭据——这是方向 6 最硬的技术差异点。**商业方 Tailscale / Ngrok 归 [commerce/](/Users/pengpeng/seo/directions/commerce)**（闭源商业产品），本目录只放开源自建侧；tailscale 报告见 [commerce/reports/tailscale.md](/Users/pengpeng/seo/directions/commerce/reports/05-storage-privacy/privacy-vpn/tailscale.md)。**向量库 / Embedding / 推理 API / 数据库中间件等已从 commerce 附录迁入本方向**（GPU 算力云仍留 commerce）。报告中的流量数据是历史快照，引用前需用 Semrush 重跑核实。

## 怎么用

- 重跑分类底稿：走 `.cursor/skills/deep-research/` 流程，产出落 `research/`。
- 写/重跑某个技术报告：走 `.cursor/skills/brand-seo-research/` 流程（以官方项目站为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出覆盖 `reports/<name>.md`，再在 `tech-stack.md` 对应行补链接。
- 红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`self-hosted X` / `X on Olares` / `X vs Y` / `X 面板/UI`——Olares 内置这些能力、免单独部署，是精准截获技术搜索用户的落点。
