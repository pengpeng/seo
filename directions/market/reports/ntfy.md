# ntfy SEO 竞品分析报告

> 域名：ntfy.sh | SEMrush US | 2026-07-06
> HTTP pub-sub 推送通知服务，开源可自托管，开发者 & 家庭服务器用户首选轻量通知工具

---

## 项目理解（前置）

ntfy（pronounced "notify"）是一个极简的 HTTP 协议推送通知服务：任何脚本/程序只需发一条 `curl` PUT/POST 请求，即可把通知推到手机或桌面，无需注册账号。它同时提供公共托管服务（ntfy.sh）和完整的自托管服务端，以"零依赖、纯 HTTP"著称，是 sysadmin 和 homelab 社区最受欢迎的通知工具之一。

| 项目 | 内容 |
|------|------|
| 一句话定位 | HTTP pub-sub 推送通知服务，用 `curl` 一条命令从任意脚本推送通知到手机/桌面 |
| 开源 / 许可证 | 是；Apache 2.0 + GPL-2.0 双许可 |
| 主仓库 | [github.com/binwiederhier/ntfy](https://github.com/binwiederhier/ntfy)（★ 31,348） |
| 核心功能 | HTTP PUT/POST 发通知；优先级 / 标签 / 表情 / 行动按钮；附件（图片 / 文件）；iOS / Android / Web 客户端；UnifiedPush 后端支持 |
| 商业模式 / 定价 | 公共服务免费用（每日 2,500 条限额）；Supporter $5/月、Pro $10/月、Business $20/月；服务端完全开源，可自托管免费无限用 |
| 差异化 / 价值主张 | 无需注册即可用；纯 HTTP 无 SDK；自托管则完全免费无上限；REST API 友好，hooks into everything |
| 主要竞品（初判）| Gotify（开源自托管）、Pushover（付费闭源）、Pushsafer（付费）、SimplePush、UnifiedPush |
| Olares Market | 已上架 ✅（apps.md line 210）|
| 来源 | [ntfy.sh](https://ntfy.sh)、[github.com/binwiederhier/ntfy](https://github.com/binwiederhier/ntfy) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | ntfy.sh |
| SEMrush Rank | 630,380 |
| 自然关键词数 | 296 |
| 月自然流量（US）| 2,102 |
| 自然流量估值 | $9,852 / 月 |
| 付费关键词数 | 0（无任何 Google Ads 投放）|
| 月付费流量 | 0 |
| 排名 1-3 位 | 20 词 |
| 排名 4-10 位 | 23 词 |
| 排名 11-20 位 | 32 词 |

> 零付费广告投放：ntfy 完全靠社区口碑与自然流量——这是典型的开源工具增长路径，也意味着竞品词空间未被 ntfy 本身占领。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| ntfy.sh | 245 | 2,011 | 95.67% |
| docs.ntfy.sh | 50 | 91 | 4.33% |
| archive.ntfy.sh | 1 | 0 | 0.00% |

> 文档站（docs.ntfy.sh）贡献了 50 个关键词但只有 4% 流量，主要来自安装教程词（如 `ntfy docker`）。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| ntfy | 1 | 1,900 | 56 | $4.48 | 1,520 | nav | ntfy.sh/ |
| ntfy.sh | 1 | 260 | 56 | $6.62 | 208 | nav | ntfy.sh/ |
| ntfy docker | 1 | 110 | 23 | $0 | 88 | info | docs.ntfy.sh/install/ |
| ntfy sh | 1 | 70 | 41 | $6.62 | 56 | nav | ntfy.sh/ |
| notfn | 2 | 390 | 9 | $1.38 | 31 | info | ntfy.sh/ |
| notif | 9 | 2,900 | 34 | $0.94 | 14 | info | ntfy.sh/ |
| notification service | 3 | 210 | 74 | $10.55 | 13 | info | ntfy.sh/ |
| how to send a notification | 1 | 70 | 51 | $3.01 | 9 | info | ntfy.sh/ |
| free push notification service | 2 | 110 | 38 | $10.83 | 9 | info | ntfy.sh/ |
| notify website | 3 | 110 | 61 | $6.82 | 9 | info | ntfy.sh/ |
| push notification app | 5 | 260 | 62 | $10.32 | 7 | info | ntfy.sh/ |
| send notification | 5 | 140 | 43 | $4.11 | 3 | info | ntfy.sh/ |
| ntfy vs gotify | 5 | 140 | 6 | $0 | 2 | comp | ntfy.sh/ |
| send push notification | 6 | 90 | 64 | $7.79 | 2 | info | ntfy.sh/ |
| send a notification | 6 | 110 | 63 | $3.53 | 2 | info | ntfy.sh/ |
| alertzy | 8 | 170 | 29 | $0 | 1 | nav | ntfy.sh/ |
| gotify vs ntfy | 8 | 70 | 6 | $0 | 1 | comp | ntfy.sh/ |
| notification platform | 6 | 70 | 53 | $15.44 | 1 | info | ntfy.sh/ |
| push notification service | 13 | 590 | 72 | $17.83 | 1 | info | ntfy.sh/ |
| ntfy chrome extension | 2 | 40 | 49 | $0 | 1 | info | docs.ntfy.sh/subscribe/web/ |

**关键观察**：ntfy 有 72% 的流量来自品牌词 `ntfy`（排名 #1，月量 1,900）；品类词（如 `push notification service`，590 vol，KD 72）虽量大但 KD 极高，ntfy 只排在第 13 位。真正低 KD 的机会词是 `ntfy vs gotify`（KD 6）和 `ntfy docker`（KD 23）。

### 付费词（Google Ads）

ntfy.sh 无任何付费投放。零广告支出印证了其纯开源社区驱动的定位——竞品大词（`push notification service`、`notification platform`）留有商业广告空缺，Olares 可借此切入。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ntfy vs gotify | 140 | 6 | $0 | comp | ⭐ ntfy.sh 只排第 5，有明显切入空间 |
| gotify vs ntfy | 50 | 11 | $0 | comp | ⭐ 与上条合计约 190 vol，同族词 |
| pushover alternative | 40 | 14 | $3.74 | info | ⭐ 商业意图强，购买替代决策阶段 |
| ntfy alternative | 20 | 0 | $0 | info | ⭐ 零竞争，Olares 应抢 GEO 引用位 |
| gotify alternative | 20 | 0 | $0 | info | ⭐ 零竞争，同上 |
| ntfy vs gotify vs pushover | 20 | 0 | $0 | comp | ⭐ 三方对比，零竞争 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| push notification service | 590 | 72 | $17.83 | info | 头部大词，KD 极高，难直接攻 |
| push notification services | 480 | 53 | $17.83 | info | 同上变体 |
| home assistant notification | 320 | 42 | $0 | info | 家庭自动化场景，Olares 智能家居方向 |
| notfn | 390 | 9 | $1.38 | info | ⭐ ntfy 误拼变体，KD 极低，已排 #2 |
| notification system | 390 | 50 | $7.89 | info | 中竞争，企业/工具层面 |
| notification service | 210 | 74 | $10.55 | info | 高 KD，ntfy 排第 3 |
| notify ios | 170 | 17 | $0 | info | ⭐ 低 KD，iOS 通知场景，移动端入口 |
| alertzy | 170 | 29 | $0 | nav | ⭐ 竞品品牌词，ntfy.sh 出现在其搜索结果 |
| notification software | 140 | 27 | $6.59 | info | ⭐ 中量低 KD，有商业价值 |
| notifi alert | 110 | 5 | $6.13 | info | ⭐ 极低 KD，量合理，高 CPC |
| push notification platform | 110 | 37 | $24.35 | info | 高 CPC 商业词，付费市场活跃 |
| free push notification service | 110 | 38 | $10.83 | info | 与 ntfy 免费自托管强关联 |
| notify app android | 140 | 29 | $1.33 | info | ⭐ Android 端通知场景 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ntfy | 1,900 | 56 | $4.48 | nav | 品牌词，ntfy 排 #1，品牌护城河 |
| ntfy.sh | 260 | 56 | $6.62 | nav | 品牌域名词，同上 |
| ntfy docker | 110 | 23 | $0 | info | ⭐ 安装教程词，docs 页已排 #1 |
| ntfy sh | 70 | 41 | $6.62 | nav | 品牌变体 |
| ntfy github | 90 | 66 | $0 | nav | 高 KD，导航词 |
| ntfy self-hosted | 20 | 0 | $0 | info | ⭐ 零竞争，自托管明确信号 |
| ntfy chrome extension | 40 | 49 | $0 | info | 浏览器订阅场景 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ntfy docker | 110 | 20 | $0 | info | ⭐ 最强自托管信号，docs 已 #1 |
| ntfy self-hosted | 20 | 0 | $0 | info | ⭐ 明确 intent，零竞争 |
| open source notification server | 20 | 0 | $0 | info | ⭐ 零竞争，GEO 前沿词 |
| push notification raspberry pi | 20 | 0 | $0 | info | ⭐ homelab 场景，Olares ARM 支持 |
| self-hosted push notifications | 0 | 0 | $0 | info | 零量但语义强，GEO 前哨 |
| self-hosted notification service | 0 | 0 | $0 | info | 零量但语义强，GEO 前哨 |
| open source push notifications | 0 | 0 | $6.66 | info | 零量高 CPC 信号，商业价值存在 |

---

## Olares 关联词（Phase 3）

**核心逻辑：ntfy 已在 Olares Market 上架，Olares 是"把 ntfy.sh 搬回自己家"的一键方案——从"依赖公共服务"到"完全私有化、零费用、无限推送"。**

按月量降序。⭐⭐⭐ = Olares 契合度极高；⭐⭐ = 高；⭐ = 中。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| ntfy vs gotify | 140 | 6 | $0 | Olares Market 同时支持 ntfy 和 Gotify；一键部署对比"手动 Docker"；终极答案是"在 Olares 上两个都跑" | ⭐⭐⭐ |
| ntfy docker | 110 | 20 | $0 | 目标用户正在手动配 Docker；Olares 一键安装 ntfy，零 YAML，零端口转发，自动 HTTPS | ⭐⭐⭐ |
| home assistant notification | 320 | 42 | $0 | HA 用户的通知路径 → ntfy → Olares；Olares 亦可运行 HA，ntfy 作通知 sidecar | ⭐⭐ |
| pushover alternative | 40 | 14 | $3.74 | Pushover 订阅 $5/年且闭源；ntfy + Olares = 免费自托管平替，无消息上限 | ⭐⭐⭐ |
| ntfy alternative | 20 | 0 | $0 | 即使用户在找 ntfy 替代，Olares 仍可作入口推荐——"先试 ntfy on Olares" | ⭐⭐ |
| gotify alternative | 20 | 0 | $0 | Gotify 用户迁移路径；Olares Market 提供两者，迁移无痛 | ⭐⭐ |
| ntfy self-hosted | 20 | 0 | $0 | Olares = ntfy 的最佳自托管平台：自动 TLS、内网穿透、Olares Space 备份 | ⭐⭐⭐ |
| open source notification server | 20 | 0 | $0 | Olares + ntfy 是"完整的开源通知栈"，无需任何外部服务 | ⭐⭐⭐ |
| notification software | 140 | 27 | $6.59 | 中小团队自托管通知软件；ntfy on Olares 零运维成本 | ⭐⭐ |
| notifi alert | 110 | 5 | $6.13 | 低 KD，用户在找轻量告警工具；ntfy on Olares 一键搞定 | ⭐⭐ |
| push notification raspberry pi | 20 | 0 | $0 | Raspberry Pi 用户是 Olares ARM 目标群；Olares + ntfy 在 Pi 上跑 | ⭐⭐⭐ |
| ntfy vs gotify vs pushover | 20 | 0 | $0 | 三方对比终点：Olares 同时提供 ntfy + Gotify，自带 Pushover 的免费替代 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| ntfy vs gotify | 140 | 6 | $0 | comp | **主词候选** | KD 仅 6，ntfy 自排第 5 位有失守迹象；Olares 写"ntfy vs Gotify：在 Olares 上一键部署两者"可直接抢排名 |
| ntfy docker | 110 | 20 | $0 | info | **主词候选** | 最强自托管安装信号词，KD 低；目标用户正在配 Docker，Olares 一键 vs 手动 YAML 的对比叙事天然成立 |
| notification software | 140 | 27 | $6.59 | info | **主词候选** | KD<30，CPC 有商业信号；可做"best open-source notification software"切入，ntfy on Olares 作结 |
| home assistant notification | 320 | 42 | $0 | info | **次级** | 量最大但 KD 42；作为自托管通知场景次级词收录，ntfy + HA + Olares 三角组合叙事 |
| notfn | 390 | 9 | $1.38 | info | **次级** | ntfy 误拼变体，ntfy 已排 #2；自然带量，并入 ntfy 主题文章即可 |
| notify ios | 170 | 17 | $0 | info | **次级** | KD 低，iOS 端通知场景；ntfy 有 App Store 客户端，并入产品介绍即可 |
| notifi alert | 110 | 5 | $6.13 | info | **次级** | 极低 KD，CPC 商业信号好；可作轻量告警场景次级词并入 |
| pushover alternative | 40 | 14 | $3.74 | info | **主词候选** | 量虽 40 但商业意图极强（替代决策阶段）、CPC 有商业信号；ntfy + Olares = Pushover 付费替代，战略价值高 |
| gotify vs ntfy | 50 | 11 | $0 | comp | **次级** | 与 `ntfy vs gotify` 同族，并入对比文即可 |
| ntfy vs gotify vs pushover | 20 | 0 | $0 | comp | **GEO** | 零竞争三方对比；在对比文中加一节直接回答，抢 AI Overview 引用位 |
| ntfy alternative | 20 | 0 | $0 | info | **GEO** | 零 KD 零竞争；进 FAQ 抢引用，答案指向"ntfy on Olares 自托管" |
| gotify alternative | 20 | 0 | $0 | info | **GEO** | 同上；Olares Market 同时提供 ntfy 与 Gotify |
| self-hosted push notifications | 0 | 0 | $0 | info | **GEO** | 零量但语义精准；放进技术 FAQ 抢 AI Overview 引用 |
| open source notification server | 20 | 0 | $0 | info | **GEO** | 零竞争；Olares + ntfy 就是完整的开源通知服务器 |
| push notification raspberry pi | 20 | 0 | $0 | info | **GEO** | 零竞争；Olares ARM/Pi 支持 + ntfy 组合叙事 |

---

## 核心洞见

1. **品牌护城河**：`ntfy` 排名 #1，月量 1,900，流量占比 72%。品牌护城河扎实——开发者和 homelab 社区心智高度集中，正面刚品牌词意义不大。但这也说明该品类**完全靠口碑，没有商业对手刷广告**，为 Olares 自然流量内容创造了空白地带。

2. **可复制打法**：ntfy 无程序化落地页，无付费投放，所有流量来自单一主域。**可复制的点是文档带流量**（docs.ntfy.sh 靠 `ntfy docker` 安装词排第 1）——Olares 也应做 ntfy 安装教程/迁移教程的教程向内容，搭 ntfy 自带 SEO 尾流。竞品（pushover.net）有 720 个关键词、3,665 流量，说明付费+闭源的 Pushover 更擅长获取通知品类大词——这是替代文的突破口。

3. **对 Olares 最关键的词**：
   - `ntfy vs gotify`（140 vol，KD 6）——低竞争对比词，Olares Market 同时提供两者是核心差异化
   - `ntfy docker`（110 vol，KD 20）——自托管安装信号，Olares 一键 vs 手动 Docker 叙事直接成立
   - `pushover alternative`（40 vol，KD 14，CPC $3.74）——付费替代决策词，ntfy+Olares = 免费自托管平替 Pushover

4. **最大攻击面**：Pushover 是最大痛点来源——闭源、订阅制（$5/年起）、每月 7,500 条消息上限。`pushover alternative`（KD 14）是极佳的商业意图攻击口。ntfy.sh 本身也有每日 2,500 条免费消息上限和保留 topic 付费墙——自托管 ntfy on Olares = 完全免费、无上限、数据不出门，是最强对比角度。

5. **隐藏低 KD 金矿**：
   - `notifi alert`（110 vol，KD 5，CPC $6.13）——几乎无竞争，商业价值信号好
   - `notify ios`（170 vol，KD 17）——iOS 场景，ntfy 有 App Store 客户端
   - `notfn`（390 vol，KD 9）——ntfy 误拼变体，ntfy 已排 #2，并入文章无需额外工作
   - `ntfy vs gotify vs pushover`（20 vol，KD 0）——零竞争三方对比，精准漏斗底部词

6. **GEO 前瞻布局**：`self-hosted push notifications`、`open source notification server`、`ntfy alternative`、`gotify alternative`、`push notification raspberry pi` 均接近零量零竞争——适合写进 FAQ 段落和直答块，抢 AI Overview / Perplexity 引用位。随着 homelab 和个人 AI 话题热度上升，这类词的搜索量预计在 12-18 个月内从 0 涨到 20-50，先占先得。

7. **与 olares-500-keywords 的关联**：ntfy 所在的自托管通知品类与现有词表中的 homelab / self-hosted / home automation 方向强相关，但通知本身尚无专门词进入 500 词词表。`ntfy vs gotify` 这类超低 KD 对比词是对现有词表的有价值补充，特别是在 home automation 场景下（`home assistant notification`，320 vol）可与 HA 相关词形成联动。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_subdomains`、`domain_organic_organic`、`phrase_these`、`phrase_related`、`phrase_questions`）| 2026-07-06*  
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
