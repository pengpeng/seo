# 隐私诉求与核心概念趋势（privacy 方向 · 分类 06）

> 研究日期: 2026-07-06 | 来源: task-06（8 源）| 模式: Lightweight | AS_OF: 2026-07-06 | 官方源占比: ~50% | 视角: data sovereignty + Olares 个人云落点
>
> 分类 = 用户/组织的**隐私诉求与核心概念**（data/digital sovereignty、self-hosting、E2EE/零知识、被遗忘权、可携权、privacy by design、主权云）。这是把前 5 类事实转成 Olares 叙事的**概念词**层。发现笔记见 [privacy-demand-concepts.notes/](/Users/pengpeng/seo/directions/privacy/research/06-concepts/privacy-demand-concepts.notes)。

## 摘要
2026 年 digital/data sovereignty 已从口号变成**可执行采购框架**：欧盟 6 月的 CADA 定义四层主权保证（L1 数据在欧盟境内 → L4 供应链全透明、无第三国干预），并目标 5–7 年将欧盟数据中心容量翻三倍 [1]。驱动力是**对美云依赖 + CLOUD Act 冲突**——美系 hyperscaler 占欧盟云约 70%、专业支出约 80%，微软法国高管公开承认无法保证公共部门数据不被传至美国当局 [2]。合规叠加（Data Act 云切换 2025-09 生效、2027-09 归零 egress 费 + GDPR Art.20 可携 + NIS2/DORA）创造真实的"迁移/可携"商业意图，Gartner 预测欧洲主权云 IaaS 从 2025 年 $69 亿增至 2027 年 $231 亿 [2][8]。**Olares 落点**：本地/自托管部署 = data sovereignty 的**个人化**答案（硬件与数据归用户、Agent 本地跑），区别于 CADA 的"买欧盟云"，也区别于纯 SaaS 零知识（仍依赖供应商基础设施）。

## 1. 概念地图（SEO 分子方向）
| 概念 | 含义 | SEO 意图 | 来源 |
|------|------|----------|------|
| data residency | 数据存储在特定地理位置 | 信息/合规 | [1][2] |
| digital / data sovereignty | 数据不受第三国法律管辖、供应链可控（CADA L2+） | B2B 商业评估 | [1][2] |
| self-hosting | 自行托管服务、数据在自有设备 | 商业/对比 | [4][5] |
| zero-knowledge / E2EE | 服务商无法访问密钥/明文 | 信息 + 垂直商业 | [行业共识] |
| RTBF (Art.17) | 被遗忘权，非绝对（多例外） | 信息 + 个案维权 | [7] |
| data portability (Art.20) | 可携权，机器可读 + controller 直传 | 信息 + 迁移意图 | [8] |
| privacy by design/default | Art.25 强制持续义务，默认最小化 | 信息 + B2B | [3] |
| sovereign cloud / Gaia-X | 欧洲主权云采购与联邦信任框架 | 地缘/B2B | [1][6] |

**置信度: High**（官方 CADA/EDPB + 行业研究）。

## 2. 主权趋势与地缘背景
- **CADA（2026-06）**：三支柱（R&D&I / Capacity / Autonomy），四层 sovereignty assurance L1–L4，推广开源以增强韧性 [1]。
- **对美云依赖**：美系占 EU 云 ~70%、专业支出 ~80%；CLOUD Act 使第三国政府可跨境索取数据，与 GDPR 冲突 [2]。
- **合规叠加（compliance cascade）**：Data Act 切换 2025-09 生效、2027-09 归零费；DORA 2025-11 认定 19 个关键第三方（含 AWS/Azure/GCP）；Gartner 主权云 IaaS $6.9B→$12.6B→$23.1B（2025–2027）[2][8]。
- **Gaia-X**：2025-11 Trust Framework 3.0 "Danube"；是标准+认证的**联邦信任框架**，不建 DC、不卖云 [6]。

**置信度: High/Medium**（CADA/CSA 权威；Gartner 数字经 CSA 转引）。

## 3. 用户级诉求（data minimization / 权利）
- EDPB 2026-02 强调 Art.25 为持续法定义务，默认最小化四维度（收集量、处理范围、存储期、可访问人数）[3]。
- RTBF 非绝对（法律义务/公共利益例外）；可携权范围更窄但要求机器可读 + controller 直传 [7][8]。
- **Olares 落点**：本地部署 = 无需向第三方请求删除/导出，数据天然在用户控制下，天然符合 data minimization（无广告画像、数据不出域）[3][7][8]。

**置信度: High**。

## 4. 自托管运动信号
- selfhosting.sh 分析 1,165 篇文章/370 应用/93 品类；Immich 成 2025–2026 de-Google Photos 热点；AI/ML 增长最快但资源门槛最高 [4]。
- r/selfhosted 称 65 万周访客、97% 用容器；CISPA 研究约 8.4% 美国人尝试过 self-hosting [5]。

**置信度: Medium**（社区/行业媒体，硬数字需 primary 复核）。

## 5. 候选关键词（Olares 高价值）
- 商业/对比型（优先）：`self hosted personal cloud`、`own your data`、`data sovereignty at home`、`Google Photos alternative self hosted`、`degoogle`、`personal cloud OS`、`self hosted AI agent`、`EU Data Act cloud switching`。
- 信息型（漏斗顶）：`data sovereignty vs digital sovereignty`、`what is zero knowledge encryption`、`privacy by design explained`、`right to be forgotten GDPR`、`data portability GDPR`。
- 地缘/B2B 借势（欧洲流量）：`EU sovereign cloud`、`CADA cloud sovereignty levels`、`Gaia-X data spaces`。

## 6. 核心争议 / 反方
**核心争议**：(A) 便利仍胜主权——DreamHost 判断 "most people will choose convenience over control every single time"，自托管圈层是否破圈未证 [5]。(B) 欧洲主权云"有规则无供给"——Gaia-X 七年未建自有 DC，"digital sovereignty" 流量高但企业落地可能仍是"买更合规的美系区域云" [6]。(C) 自托管安全悖论——homelab 混 IoT 与关键服务、Residential IP 暴露，未配 VPN/反向代理/补丁者实际风险可能高于零知识 SaaS [5]。

**反方解释**：对主流非技术用户，功能与便利（如 Google Photos 的 AI 相册）仍是首选；概念词流量高不等于转化。诚实口径：Olares 把自托管的**门槛降低**（应用商店化、一键部署），但仍面向愿意"拥有而非租用"的人群。

## 7. 局限性与未来方向
- **局限**：缺 IAPP/Gartner 对 consumer degoogle 搜索量一手 Semrush 数据；8.4% 渗透率需 primary 复核 [task-06 Gaps]。
- **未来方向**：以本报告概念词为种子跑 Semrush，建"概念词 → 落地页/对比文"映射；`data sovereignty`、`own your data`、`self hosted personal cloud` 优先做支柱页。

## 参考文献
[1] EU Commission. "Cloud and AI Development Act". official. As Of: 2026-06. https://digital-strategy.ec.europa.eu/en/policies/cloud-and-ai-development-act
[2] Cloud Security Alliance. "EU Tech Sovereignty: Cloud Concentration Risk and the Compliance Cascade". secondary-industry. As Of: 2026-06. https://labs.cloudsecurityalliance.org/research/eu-tech-sovereignty-cloud-ai-enterprise-risk-v1-0-csa-styled/
[3] EDPB. "Data protection by design & by default: When to act and what to do". official. As Of: 2026-02. https://www.edpb.europa.eu/system/files/2026-02/edpb-summary-gdpr-data-protection-design-default_en.pdf
[4] selfhosting.sh. "State of Self-Hosting 2026". community. As Of: 2026-02. https://selfhosting.sh/research/state-of-self-hosting-2026/
[5] DreamHost. "Is the Self-Hosting Revolution Finally Here?". industry-media. As Of: 2025-10. https://www.dreamhost.com/blog/self-hosting/
[6] Gaia-X. "Gaia-X Enters Season 2.0 — Summit 2025". ecosystem-official. As Of: 2025-11. https://gaia-x.eu/gaia-x-enters-season-two-of-dataspaces-and-digital-ecosystems-with-summit-2025/
[7] gdpr-info.eu. "Art. 17 GDPR – Right to erasure ('right to be forgotten')". regulation-index. As Of: ongoing. https://gdpr-info.eu/art-17-gdpr/
[8] sota.io. "GDPR Article 20: Right to Data Portability — SaaS Developer Guide 2026". secondary-industry. As Of: 2026. https://sota.io/blog/gdpr-article-20-right-to-data-portability-saas-developer-implementation-guide-2026
