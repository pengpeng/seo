# Astral SEO 竞品分析报告（场景词分析，无独立官网）

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> Astral 是基于 Nostr 协议的去中心化社交 Web 客户端——自托管的 Twitter-like 体验，用户控制身份与数据。

---

## 项目理解（前置）

Astral 是一个运行在浏览器中的 Nostr 协议客户端，部署方式为静态 Web App（SPA/PWA），支持 Docker 自托管。它 fork 自 Branle（fiatjaf 的早期 Nostr 客户端），由 monlovesmango 重构，加入了 Global Feed 和全面 UI 改进。项目使用 Quasar/Vue.js 构建，MIT 许可，支持生成/导入 Nostr 密钥对（keypair 即身份，不绑定服务器），并通过连接多个 Relay 发布和接收内容。

Nostr（Notes and Other Stuff Transmitted by Relays）是去中心化通信协议，身份以密钥对为基础——不同于 Mastodon 的"服务器绑定账号"，用户可在任意 Nostr 客户端之间自由切换而不丢失关注者。Astral 的主要场景是提供 Twitter-like 的公开发帖、关注和全局 Feed 体验，兼具 Lightning Zaps 支持。

项目**自 2023 年 2 月起停止活跃维护**，在 2026 年的生态中属于早期里程碑客户端，已被 Primal、Damus、Amethyst 等更活跃的竞品超越；但其简洁的代码结构和 Docker 支持使其在 self-hosting 圈仍有引用价值。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 去中心化 Nostr 协议 Web 客户端，Twitter-like 体验，支持 Docker 自托管 |
| 开源 / 许可证 | 是，MIT License |
| 主仓库 | https://github.com/monlovesmango/astral（★ 99） |
| 核心功能 | 全局 Feed、关注关系、自托管密钥身份、Lightning Zaps、PWA/SPA/Docker 部署 |
| 商业模式 / 定价 | 完全免费开源；可用 https://astral.ninja/ 托管版，也可自部署 |
| 差异化 / 价值主张 | 最早的 Nostr Web 客户端之一；轻量 SPA、一行 Docker 命令可跑；keypair 身份无服务器锁定 |
| 主要竞品（初判）| Primal (primal.net)、Damus (iOS/macOS)、Coracle (coracle.social)、Snort (snort.social)、Amethyst (Android) |
| Olares Market | 已上架 ⬜（待验证） |
| 来源 | [GitHub monlovesmango/astral](https://github.com/monlovesmango/astral)；[nostr.org](https://nostr.org/)；[d-central.tech Nostr Clients Comparison](https://d-central.tech/nostr-clients-comparison/) |

---

## 关键词扩展（Phase 2）

> 注：Astral 无独立官网，跳过 Phase 1 域名基线。直接从关键词层面分析 Nostr/去中心化社交场景的搜索需求。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| bluesky alternative | 70 | 12 | $13.26 | 信息 | ⭐ 低竞争 + 超高 CPC，商业意图强 |
| mastodon alternative | 10 | — | $2.82 | 信息 | ⭐ 量小但 CPC 有信号 |
| nostr vs bluesky | 20 | — | $0 | 信息 | 对比词，低量但精准 |
| nostr vs mastodon | 20 | — | $0 | 信息 | 对比词 |
| bluesky vs nostr | 20 | — | $0 | 信息 | 对比词（反向） |
| open source twitter alternative | 20 | — | $0 | 信息 | 自托管意图 |
| decentralized twitter alternative | 20 | — | $0 | 信息 | 精准需求词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| decentralized social media | 320 | 51 | $0 | 信息 | 核心品类词，Mastodon 主导 |
| fediverse | 4,400 | 77 | $0 | 信息 | 高量高难，Nostr 非 fediverse |
| activitypub | 480 | 80 | $0 | 信息 | 技术词，Nostr 协议有差异 |
| nostr | 5,400 | 79 | $0 | 信息/导航 | 品牌主词，极难切入 |
| open source social media | 170 | 45 | $4.11 | 信息 | CPC 信号好，中等难度 |
| federated social media | 110 | 74 | $0 | 信息 | 高难 |
| nostr protocol | 110 | 52 | $0 | 信息 | 教育内容词 |
| decentralized social network | 90 | 56 | $0 | 信息 | 中等竞争 |
| open source social network | 90 | 31 | $3.71 | 信息 | ⭐ KD 31，CPC 信号，有机会 |
| what is nostr | 260 | 37 | $0 | 信息 | ⭐ 中等 KD，入门内容机会 |
| nostr app | 140 | 32 | $0 | 信息 | ⭐ 直接产品词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| damus | 480 | 62 | $0 | 信息 | 最大竞品，iOS 专属 |
| primal nostr | 140 | 51 | $0 | 信息 | 竞品，跨平台 |
| nostr relay | 20 | — | $0 | 信息 | 运维词，自托管用户 |
| nostr tutorial | 20 | — | $0 | 信息 | 教程词 |
| nostr lightning | 20 | — | $0 | 信息 | 功能词（Zaps） |
| nostr social media | 20 | — | $0 | 信息 | 品类定位词 |
| amethyst nostr client | 20 | — | $0 | 信息 | 竞品（Android） |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| private social media | 210 | 9 | $4.03 | 信息 | ⭐⭐⭐ KD 极低，最大隐藏机会 |
| self hosted social media | 20 | — | $0 | 信息 | ⭐ 精准意图词，量小 |
| self hosted social network | 20 | — | $0 | 信息 | ⭐ 同上 |
| self hosted twitter alternative | 20 | — | $0 | 信息 | ⭐ 非常精准 |
| self hosted mastodon | 20 | — | $0 | 信息 | 对比切入点 |
| nostr client | 20 | 0 | $0 | — | Astral 直接词，零 KD 但量极低 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Nostr 的"身份由密钥对控制、不绑服务器"与 Olares 的"数据主权"叙事高度契合——用 Olares 一键部署 Astral，等于在自己的硬件上跑 Nostr 前端，同时可在同一 Olares 实例里运行 Relay（nostr-rs-relay 等）实现完整 Nostr 主权栈。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| private social media | 210 | 9 | $4.03 | ⭐⭐⭐ Olares + Astral = 私有社交网络完整方案；用户控制帖子与身份，无企业审查 |
| bluesky alternative | 70 | 12 | $13.26 | ⭐⭐⭐ Nostr 是比 Bluesky 更去中心化的替代——AT Protocol 仍有 PDS 服务器依赖，Nostr keypair 完全自主 |
| open source social network | 90 | 31 | $3.71 | ⭐⭐ Astral + Nostr relay 在 Olares 上构建完整开源社交栈 |
| nostr app | 140 | 32 | $0 | ⭐⭐ 直接覆盖"找 Nostr 客户端"的用户；Olares Market 一键安装 Astral |
| what is nostr | 260 | 37 | $0 | ⭐⭐ 入门教育文章，末段引出"Olares 上一键跑 Nostr 客户端+Relay"路径 |
| decentralized social media | 320 | 51 | $0 | ⭐ 量大但竞争激烈，Olares 切入角是"完整自托管方案"而非单纯协议介绍 |
| self hosted social media | 20 | — | $0 | ⭐⭐⭐ 精准信号词，量小但意图极准——Olares 是最自然的答案 |
| self hosted twitter alternative | 20 | — | $0 | ⭐⭐⭐ 精准长尾词，GEO 前哨候选 |
| nostr vs bluesky | 20 | — | $0 | ⭐⭐ 对比内容机会，Olares 同时支持 Nostr（Astral）与 ATProto 客户端双方 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| private social media | 210 | 9 | $4.03 | 信息 | 主词候选 | KD 最低 9 的隐藏金矿；SERP 无强 self-hosted 内容，Olares+Astral 完全可以切入"拥有私有社交网络"角度 |
| bluesky alternative | 70 | 12 | $13.26 | 信息 | 主词候选 | KD 12 + CPC $13.26 罕见组合；Nostr 是最去中心化的 Bluesky 替代，Olares 一键部署 Astral 是具体操作答案 |
| what is nostr | 260 | 37 | $0 | 信息 | 主词候选 | 量最高的低中 KD 词；入门教育内容，尾部植入 Olares Market 安装路径 |
| nostr app | 140 | 32 | $0 | 信息 | 主词候选 | 直接产品词，KD 合理；Astral 是最简洁的 Nostr Web 客户端之一，Olares Market 上架增加分发 |
| open source social network | 90 | 31 | $3.71 | 信息 | 主词候选 | KD 31 + 有 CPC；Astral + nostr-rs-relay 在 Olares 上构建完整开源社交栈，角度独特 |
| decentralized social media | 320 | 51 | $0 | 信息 | 次级 | 量最大但 KD 51，Mastodon 主导；可作为 what-is-nostr 或 private-social-media 文章的次要 target 词 |
| nostr protocol | 110 | 52 | $0 | 信息 | 次级 | 技术教育词，并入 nostr 入门文章 |
| open source social media | 170 | 45 | $4.11 | 信息 | 次级 | CPC 信号好；可并入 open source social network 文章 |
| self hosted social media | 20 | — | $0 | 信息 | 次级 | 量小意图极准，并入 private social media 文章的 H2 |
| self hosted twitter alternative | 20 | — | $0 | 信息 | GEO | 近零量但精准，抢 AI Overview 引用位 |
| nostr vs bluesky | 20 | — | $0 | 信息 | GEO | 对比类问题词，FAQ 段落植入 |
| nostr client self hosted | — | — | $0 | 信息 | GEO | Semrush 无数据但语义精准；AI 搜索高频问法 |
| astral nostr client | — | — | $0 | 信息 | GEO | 产品直接词，近零量但 GEO 抢位有意义 |

---

## 核心洞见

1. **品牌护城河**：Astral 本身作为品牌在搜索引擎基本无流量（`astral nostr` 无 Semrush 数据，`nostr client` 仅 20/mo）。品牌词正面竞争无意义。Nostr 的大词（`nostr` 5400/mo KD 79，`fediverse` 4400/mo KD 77）由 nostr.org/nostr.com 和 Mastodon 周边内容主导，无法直接撬动。**策略应绕开品牌词，聚焦低 KD 品类词。**

2. **可复制的打法**：SERP 上没有"自托管 Nostr 方案"的权威内容（nostrapps.com、nostr.how 主要做协议介绍，不做自托管教程）。`private social media`（KD 9）的 SERP 前 10 完全由 Reddit、商业 SaaS 和泛讨论页面占据，**没有任何 self-hosted 解决方案内容**——这是极罕见的机会真空。

3. **对 Olares 最关键的词**：
   - **`private social media`**（KD 9, 210/mo）—— 最大攻击面，SERP 空白
   - **`bluesky alternative`**（KD 12, $13.26 CPC）—— Nostr 是最有力的去中心化替代，切入角清晰
   - **`nostr app` / `what is nostr`**（KD 32/37，140/260/mo）—— 直接覆盖 Nostr 新用户

4. **最大攻击面**：Bluesky 的增长（`bluesky` 已达 100 万/月）正在培育"我想要更去中心化替代"的需求（`bluesky alternative` KD 12 + $13.26 CPC）。Nostr 的 keypair-native 设计比 AT Protocol 的 PDS 服务器依赖更彻底——Olares + Astral 可以打"**比 Bluesky 更去中心化，且数据完全在自己手里**"的叙事。

5. **隐藏低 KD 金矿**：`private social media`（KD 9）是整个去中心化社交领域 KD 最低的高意图词，且 SERP 无 self-hosting 内容竞争。`open source social network`（KD 31, $3.71 CPC）同样被低估，目前排名的域名权威度不高。

6. **GEO 前瞻布局**：随着 AI Overview 的普及，`self hosted nostr client`、`how to run nostr on my own server`、`nostr alternative to twitter self hosted`、`astral nostr how to install` 这类零量精准问法将成为 AI 引用的主要来源——Olares 文档和内容应预先覆盖这些 FAQ。

7. **与既有 olares-500-keywords 的关联**：Nostr/去中心化社交场景与 Olares 已有的"data ownership"和"self-hosted"内容方向高度重叠。本报告新增的 `private social media`（KD 9）和 `bluesky alternative`（KD 12）是 olares-500 词表的**增量词**，尚未被覆盖，建议补入优先写作队列。

---

*数据来源：SEMrush US 数据库（phrase\_these、phrase\_kdi、phrase\_organic）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*注：Astral 无独立可分析域名，Phase 1 流量基线跳过；所有 "—" 表示 Semrush 无数据（量极低或零）。*
