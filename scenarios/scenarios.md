# scenarios.md — 主线：落地场景（产品开发进度）

> 回答"我们正在做/即将支持什么"。这里是 Olares 重点投入的场景，即**产品开发进度**——决定内容能真实兑现的边界。方向/事实见 [directions.md](/Users/pengpeng/seo/directions/directions.md)。

> ⚠️ **保密红线**：本页含内部判断，仅用于**指导选题方向**。未公开的信息（官网/docs/GitHub 上找不到的）绝不可写进任何对外内容；对外只讲"正在做 / 即将支持"，不给未公布的版本号与日期。完整红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

---

## 统一大主线

Olares 把"用户已经在为之付费的云 AI 订阅"，变成"本地拥有、一次买断硬件、Agent 一句话搞定"。下面每个场景都能挂到这条主线，也都对标了**已经有人付费**的成熟市场——正是内容/关键词应提前占位的方向。

---

## 八大场景（Q2 定调）

| # | 场景方向 | Olares 叙事 | 已验证付费市场（对标/竞品） | SEO 切入 |
|---|----------|-------------|--------------------------|----------|
| 1 | **Agent 管理个人 AI 硬件** | 让 Agent 安全、可控、低成本地管理你的 Olares | OpenClaw、Hermes Agent（开源自托管 Agent 增长最快的一段） | self-hosted agent、local agent、openclaw/hermes alternative |
| 2 | **Agent 造并部署应用** | 匹配自然语言部署体验，规模化后成本更低（本地模型不涨价、无中间商加价） | Manus、Lovable（证明用户愿为"自然语言部署"付费，但成本随项目膨胀） | lovable/manus alternative、self-hosted app builder、local vibe coding |
| 3 | **本地 AI 音频** | 采集/处理语音全本地，敏感语音不上云 | Plaud（2M+ 设备、$100M+ ARR）、Granola（$1.5B 估值）、Typeless（$30/mo）、ElevenLabs（$500M ARR） | 会议转录、本地 STT/TTS、语音克隆、plaud/granola alternative |
| 4 | **本地 AI 出图** | 为设计师省云 API 成本，输出可控、数据私有 | 云 API：GPT-Image-2、Nano Banana 2；开源模型 Ideogram 4.0、HiDream-O1 | comfyui workflow app、local image generation、designer 省成本 |
| 5 | **智能家居 / IoT / 健康** | 用私有家庭服务器替代云 Hub，Agent 自然语言控设备 | 智能家居 2026 约 $207B→2033 约 $887B；HomeKit/Google Home/Alexa/小米互不打通 | home assistant on olares、private smart home、self-hosted iot hub |
| 6 | **Olares Workspace（团队协作）** | 自托管团队协作，Agent 作为有身份/授权的"团队成员" | Microsoft 365（约 3.45 亿席）、Google Workspace（900 万+ 组织） | self-hosted workspace、mattermost、private team collaboration |
| 7 | **AI Companion（AI 伴侣）** | 本地渲染数字人（Unreal + 本地 GPU），隐私、无内容限制 | Character.AI（约 20M MAU）、Replika（30M+）、MiniMax Talkie、SillyTavern | ai companion、sillytavern alternative、local ai roleplay |
| 8 | **企业场景（GTM）** | 敏感数据/私有 AI 场景：安全合规/主权第一、成本可预测性第二（成本上升最快） | 企业本地模型：GLM 5.2、MiniMax M3、Qwen 3.6 | on-prem ai、private llm for enterprise、data compliance ai |

---

## 场景 8 详解：企业化需求（GTM）

**在敏感数据 / 私有 AI 场景**下，企业采购由**安全合规 / 数据主权（第一驱动）+ 成本可预测性（第二驱动，逃 egress + 消费计费不可预测）**推动——2026 多份调研排序一致：Broadcom/VMware《Private Cloud Outlook 2026》单一最重要放置因素"安全与合规"32% 居首（repatriation 驱动 51% > 成本可预测性 39%）、Cloudian《Enterprise AI Infrastructure Survey 2026》本地部署意愿"数据隐私/主权"53% > TCO 40%、IDC 云迁回原因安全 33% + 数据隐私 28% 前两位（对 AI/GenAI 更关键）。**注意**：成本已成头号公有云*担忧*、上升最快（Broadcom 成本 31% 超安全 26%），但决定"放哪"时安全合规仍第一；且**通用**云迁回常以成本为首（Flexera 84% 把控云支出列头号挑战），本场景特指数据合规诉求。TCO 非"更便宜"而是可预测（1PB 出 S3 约 $90k–120k egress；steady-state on-prem TCO 可低 40–50%）。私有云/合规/本地模型词 CPC 极高（$10-35），单个转化价值 $1K+。

- **已验证付费/对标**：私有云/托管云厂商、OneTrust（合规）、企业本地模型（GLM、MiniMax、Qwen 企业版）、on-prem AI 方案商。
- **对应 Olares 资产**：私有部署 + 应用沙箱 + SSO/权限 + Olares One 集群 + 本地 LLM，满足"数据不出企业"的合规诉求。
- **高 CPC 白皮书词（D 级专项）**：`gdpr compliance tools`（CPC $34.62）、`gdpr software`（$27）、`gdpr solution`（$29）、`digital sovereignty`（$21.70）、`data sovereignty`（$17.68）、`on premise private cloud`（$16.04）、`data privacy compliance`（$15.61）、`private ai infrastructure`（$10.47）、`private ai for business`（$11.16）。
- **低 KD 高价值切入**：`private cloud security`（KD=9）、`private cloud data security`（KD=8）、`gdpr compliant ai`（KD=0）。
- **内容形态**：白皮书 / 合规对照表 / TCO 计算器，而非博客。
- **关联**：500 词分类 10（私有云 35）、分类 11 中的 D 级词；报告 [privacy/reports/gdpr.md](/Users/pengpeng/seo/directions/privacy/reports/gdpr.md)，企业向个人云竞品见 [market/reports/nextcloud.md](/Users/pengpeng/seo/directions/market/reports/nextcloud.md)、[market/reports/seafile.md](/Users/pengpeng/seo/directions/market/reports/seafile.md)。

---

## 场景 ↔ 产品：关系原则（不在此枚举）

一个场景不是单个产品，而是**一组产品的集合**。按此原则推导，不在本页硬列清单（会重复且易过期）：

- **每个场景 = 一组"已验证付费的商业对标" + 一组"可自托管的 Olares 平替"。**
  - 商业对标：即上表"已验证付费市场"列，明细与竞品报告在 [directions.md](/Users/pengpeng/seo/directions/directions.md) 及 `directions/commerce|hardware|privacy/`——它们证明"这个需求有人付费"。
  - Olares 平替：承接该需求的可自部署应用/模型，**现查** [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md) 与 [model/models.md](/Users/pengpeng/seo/directions/model/models.md)，不在本页登记。
- **内容打法**：挑某个商业对标的高机会词（见其竞品报告的「Top 关键词（含角色判断）」），用 `seo-content` skill 写成对比/替代文，把需求导向对应的 Olares 平替。
- **兑现纪律**：场景只在**产品能真实兑现时**才升级为主推内容；未兑现前只做"占位/教育"类内容，不承诺未发布能力（红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)）。
