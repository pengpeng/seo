# Deluge SEO 竞品分析报告

> 域名：deluge-torrent.org | SEMrush US | 2026-07-06
> 老牌开源 BitTorrent 客户端，daemon/client 架构、原生 Web UI，技术型用户首选的轻量免费下载器。

---

## 项目理解（前置）

Deluge 是基于 libtorrent 的开源 BitTorrent 客户端，采用独特的 daemon/client 分离架构——后台进程 `deluged` 常驻，前端可接 GTK-UI、Web-UI 或 Console-UI。这一架构天然适合无头服务器与远程管理，是"arr 栈"（Sonarr/Radarr + Prowlarr + 下载器）中的主流下载器选项之一。完全免费无广告，内置 VPN/代理支持与插件系统，深受隐私敏感与自托管社区青睐。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 轻量、免费、插件丰富的开源 BitTorrent 客户端，daemon/client 分离、原生 Web UI |
| 开源 / 许可证 | 是，GPL（主仓 deluge-torrent/deluge 注明"Other"） |
| 主仓库 | [github.com/deluge-torrent/deluge](https://github.com/deluge-torrent/deluge)（★ ~1.8K，Git mirror；主开发在 GitLab） |
| 核心功能 | daemon/client 分离架构；GTK/Web/Console 三种 UI；插件系统；内置 VPN/代理支持；加密与 Peer Exchange；限速与调度；v2 torrent 支持（2.2.0） |
| 商业模式 / 定价 | 完全免费开源，无付费版本 |
| 差异化 / 价值主张 | 零广告 + 极低资源占用 + 插件可扩展性；Web UI 开箱即用，适合 headless 服务器；与 arr 自动化栈深度集成 |
| 主要竞品（初判）| qBittorrent、Transmission、uTorrent、Vuze（Azureus） |
| Olares Market | **已上架**（`apps.md` 第 193 行，⬜ 待调研） |
| 来源 | [github.com/deluge-torrent/deluge](https://github.com/deluge-torrent/deluge)；[Cosmos market listing](https://cosmos-cloud.io/cosmos-ui/market-listing/cosmos-cloud/Deluge) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | deluge-torrent.org |
| SEMrush Rank | 144,556 |
| 自然关键词数 | 874 |
| 月自然流量（US）| 12,844 |
| 自然流量估值 | $6,776/月 |
| 付费关键词数 | 0（无投放） |
| 月付费流量 | 0 |
| 排名 1–3 位 | 76 词 |
| 排名 4–10 位 | 74 词 |
| 排名 11–20 位 | 170 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| deluge-torrent.org（主站） | 544 | 12,449 | 96.92% |
| forum.deluge-torrent.org | 272 | 364 | 2.83% |
| download.deluge-torrent.org | 15 | 24 | 0.19% |
| dev.deluge-torrent.org | 24 | 7 | 0.05% |
| git.deluge-torrent.org | 18 | 0 | — |
| trac.deluge-torrent.org | 1 | 0 | — |

> 主站贡献 97% 流量；forum 子域带来小量技术问答流量（含"best codec for torrenting movies" KD 18 意外词）。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| deluge bittorrent | 1 | 1,300 | 46 | $0 | 1,040 | 导航 | / |
| deluge | 1 | 33,100 | 65 | $0.82 | 860 | 导航 | / |
| deluge torrent | 1 | 1,000 | 43 | $0 | 800 | 导航 | / |
| deluge download | 1 | 720 | 50 | $0 | 576 | 下载/品牌 | /download/ |
| deluge torrents | 1 | 590 | 50 | $0 | 472 | 导航 | / |
| deluge torrent client | 1 | 210 | 50 | $0 | 168 | 导航 | / |
| deluge torrent software | 1 | 170 | 60 | $0 | 136 | 下载/品牌 | /download/ |
| deluge windows 11 | 1 | 140 | 31 | $0 | 112 | 信息/下载 | forum |
| deluge bittorrent download | 1 | 140 | 55 | $0 | 112 | 下载/品牌 | /download/ |
| deluge downloader | 1 | 110 | 42 | $0 | 88 | 下载 | /download/ |
| deluge webui | 1 | 90 | 22 | $0 | 72 | 信息 | /userguide/thinclient/ |
| deluge mac | 1 | 90 | 33 | $0 | 72 | 下载 | /download/ |
| deluge client | 1 | 90 | 49 | $0 | 72 | 导航 | /download/ |
| best codec type for torrenting movies | 3 | 1,900 | 18 | $0 | 57 | 信息 | forum（意外排名） |
| deluge vpn | 1 | 170 | 34 | $0 | 42 | 信息 | /userguide/vpn/ |
| d e l u g e | 1 | 1,900 | 58 | $0.82 | 49 | 导航 | / |
| deluge osx | 1 | 70 | 43 | $0 | 56 | 下载 | / |
| deluge for mac | 1 | 50 | 34 | $0 | 40 | 信息/下载 | /installing/macosx/ |
| deluge and vpn | 1 | 50 | 5 | $3.49 | 12 | 信息 | /userguide/vpn/ |
| deluge plugins | 1 | 50 | 10 | $0 | 12 | 信息 | /plugins/ |
| move when completed directory | 4 | 260 | 14 | $0 | 11 | 信息 | forum |
| deluge port issue | 1 | 110 | 11 | $0 | 9 | 信息 | forum |
| modulenotfounderror: no module named 'cgi' | 10 | 480 | 14 | $0 | 9 | 信息 | forum |
| gen:variant.tedy.607066 | 3 | 260 | 22 | $0 | 16 | 信息 | forum（误报/杀软误检测） |

**洞察**：流量高度集中于品牌词（#1 排名垄断自身品牌）；`deluge webui`（KD 22）、`deluge and vpn`（KD 5, CPC $3.49）是少数非品牌低竞争词；`best codec for torrenting movies`（KD 18, 1,900/mo）是论坛意外捡到的大词——说明 torrent 实用技巧内容有真实搜索需求。

### 付费词（Google Ads）

**Deluge 不做任何付费投放**，完全依赖自然搜索。符合开源社区项目的典型形态。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| best torrent client | 2,400 | 44 | $2.05 | 信息/商业 | 高量高竞，主流比较词 |
| best bittorrent client | 2,400 | 41 | $0 | 信息 | 同上变体 |
| best torrent client reddit | 480 | 29 | $0 | 商业 | ⭐ Reddit 比较词，KD 适中 |
| utorrent alternative | 390 | 23 | $0 | 商业 | ⭐ uTorrent 用户迁移意图强 |
| deluge vs qbittorrent | 320 | 7 | $0 | 信息 | ⭐⭐ 极低 KD，Deluge 直接对比词 |
| free torrent client | 260 | 54 | $0 | 信息 | 高 KD |
| qbittorrent vs deluge | 140 | 7 | $0 | 信息 | ⭐⭐ 同上反向变体，合计 ~460/mo |
| qbittorrent alternative | 170 | 18 | $0 | 商业 | ⭐ 低 KD，竞品替代意图 |
| torrent client linux | 140 | 24 | $0 | 信息 | ⭐ Linux 用户，Olares 契合 |
| deluge vs transmission | 50 | 7 | $0 | 信息 | ⭐ 极低 KD |
| deluge alternative | 20 | 0 | $0 | 商业 | ⭐ 近零 KD，量小但切入口 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| best torrent client | 2,400 | 44 | $2.05 | 信息/商业 | 难度适中，大流量 |
| best bittorrent client | 2,400 | 41 | $0 | 信息 | 同上 |
| best torrent client reddit | 480 | 29 | $0 | 商业 | ⭐ 社区型可切入 |
| free torrent client | 260 | 54 | $0 | 信息 | KD 偏高 |
| open source torrent client | 90 | 83 | $0 | 信息 | KD 极高，暂不打 |
| torrent client linux | 140 | 24 | $0 | 信息 | ⭐ 细分品类，Linux 语境 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| deluge vpn | 170 | 34 | $0 | 信息 | VPN 集成教程需求 |
| deluge docker | 110 | 40 | $0 | 信息/下载 | Docker 部署需求 |
| deluge webui | 90 | 22 | $0 | 信息 | ⭐ 低 KD，远程访问场景 |
| deluge plugins | 50 | 10 | $0 | 信息 | ⭐ 极低 KD，扩展玩法 |
| deluge windows 11 | 140 | 31 | $0 | 信息/下载 | 平台迁移词 |
| deluge mac | 90 | 33 | $0 | 下载 | Mac 用户场景 |
| deluge seedbox | 20 | 0 | $0 | 信息 | ⭐ 近零 KD，seedbox 用户 |
| deluge and vpn | 50 | 5 | $3.49 | 信息 | ⭐ 极低 KD + 高 CPC（$3.49！） |
| deluge port issue | 110 | 11 | $0 | 信息 | ⭐ 故障排除词，低 KD |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| self-hosted torrent client | 20 | 0 | $0 | 信息 | ⭐ 近零 KD，纯 Olares 受众 |
| torrent client with web interface | 20 | 0 | $0 | 信息 | ⭐ 近零 KD，Deluge webui 直接契合 |
| torrent automation | 20 | 0 | $0 | 信息 | ⭐ arr 栈自动化语义 |
| deluge webui | 90 | 22 | $0 | 信息 | ⭐ 最有量的自托管功能词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Deluge 是 Olares Market 已上架应用，headless daemon + Web UI 架构与 Olares 的"浏览器即桌面"体验天然契合；隐私（VPN/无广告）+ 自动化（arr 栈）+ 一键安装是三条差异化叙事轴。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| deluge vs qbittorrent | 320 | 7 | $0 | "两者都能一键装进 Olares，同时跑互不干扰；对比文顺带介绍 Olares Market" | ⭐⭐⭐ |
| qbittorrent vs deluge | 140 | 7 | $0 | 同上反向变体，可合并一篇 | ⭐⭐⭐ |
| utorrent alternative | 390 | 23 | $0 | "uTorrent 有广告/追踪，Deluge on Olares = 无广告 + 数据自有 + VPN 集成" | ⭐⭐⭐ |
| qbittorrent alternative | 170 | 18 | $0 | 同 uTorrent 路线，强调 Olares 平台一键部署价值 | ⭐⭐ |
| self-hosted torrent client | 20 | 0 | $0 | Olares Market 页面直接可排这个词，GEO 抢引用 | ⭐⭐⭐ |
| deluge webui | 90 | 22 | $0 | Olares 提供统一 Web 入口，不用手动配端口转发，完美契合 | ⭐⭐⭐ |
| torrent client linux | 140 | 24 | $0 | Olares 跑在 Linux 裸机/ARM，Deluge daemon 最轻量 | ⭐⭐ |
| deluge and vpn | 50 | 5 | $3.49 | Olares 内置 headscale VPN + Deluge 代理设置，双重隐私防护 | ⭐⭐⭐ |
| best torrent client reddit | 480 | 29 | $0 | Reddit 讨论中植入"Olares Market 一键装 Deluge"的自托管角度 | ⭐⭐ |
| deluge plugins | 50 | 10 | $0 | Olares 插件/App 理念相通，Deluge 插件扩展对应 arr 自动化文章 | ⭐⭐ |
| torrent automation | 20 | 0 | $0 | GEO：Olares + Deluge + Sonarr/Radarr 的全自动追剧栈 | ⭐⭐⭐ |
| torrent client with web interface | 20 | 0 | $0 | GEO：Deluge on Olares，浏览器统一管理所有 app | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| deluge vs qbittorrent | 320 | 7 | $0 | 信息 | **主词候选** | KD 极低，两词合计 ~460/mo；Olares 角度：两款均可一键装进 Olares，对比文天然引入平台 |
| qbittorrent vs deluge | 140 | 7 | $0 | 信息 | 次级（并入上篇） | 反向变体，同一篇文覆盖 |
| utorrent alternative | 390 | 23 | $0 | 商业 | **主词候选** | KD 23，量足，uTorrent 广告/追踪痛点是切入口；Olares 上 Deluge = 无广告自托管替代 |
| qbittorrent alternative | 170 | 18 | $0 | 商业 | 次级（可并入上篇） | KD 18，可与 utorrent alternative 合并写"最佳 torrent 客户端替代" |
| best torrent client reddit | 480 | 29 | $0 | 商业 | **主词候选** | 480/mo + KD 29，Reddit 社区向，可写"Reddit 推荐的 torrent 客户端 2026" |
| best torrent client | 2,400 | 44 | $2.05 | 信息/商业 | 次级（加入上篇） | 量大但 KD 44，独立打难；作为上篇次级词共享竞争力 |
| best bittorrent client | 2,400 | 41 | $0 | 信息 | 次级 | 同上，并入比较文 |
| deluge webui | 90 | 22 | $0 | 信息 | 次级 | KD 22，技术教程词；Olares Web 入口天然切入 |
| deluge and vpn | 50 | 5 | $3.49 | 信息 | 次级 | KD 仅 5 但 CPC $3.49，隐私敏感用户高价值；Olares VPN 叙事切入 |
| torrent client linux | 140 | 24 | $0 | 信息 | 次级 | KD 24，Linux headless 场景；Olares on Linux 直接相关 |
| deluge plugins | 50 | 10 | $0 | 信息 | 次级 | KD 10，插件教程；arr 栈集成内容钩子 |
| self-hosted torrent client | 20 | 0 | $0 | 信息 | GEO | 近零 KD，Olares Market 页面直接抢引用位 |
| torrent client with web interface | 20 | 0 | $0 | 信息 | GEO | 近零 KD，GEO：Deluge on Olares = 开箱即用 Web 访问 |
| torrent automation | 20 | 0 | $0 | 信息 | GEO | GEO：Olares + Deluge + arr 全自动追剧栈，AI Overview 引用位 |
| deluge alternative | 20 | 0 | $0 | 商业 | GEO | 近零量 KD 0，GEO + Olares Market 落地页 |

---

## 核心洞见

1. **品牌护城河**：Deluge 对自身品牌词的控制力极强（76 个 1-3 名词，几乎全是 #1），KD 普遍 40-65，**不值得正面竞争品牌词**。机会在品类词与比较词。

2. **可复制的打法**：
   - Deluge **完全不做 SEO 内容运营**——主站无博客、无指南页、无教程落地页，所有流量来自品牌词直达。这留下大量比较/替代/教程词的真空。
   - Forum 子域有少量意外排名词（如"best codec for torrenting movies", KD 18），说明**技术讨论内容会自然获取非品牌流量**，Olares 可以填补这个内容真空写教程。
   - qBittorrent（170K/mo）和 uTorrent（361K/mo）流量远大于 Deluge（12K/mo），**对比/替代内容的上限是搭顺风车进入这些更大的流量池**。

3. **对 Olares 最关键的 3 个词**：
   - `deluge vs qbittorrent`（+`qbittorrent vs deluge`）：合计 ~460/mo，KD 7，两者均在 Olares Market，对比文直接引入平台叙事。
   - `utorrent alternative`：390/mo，KD 23，高商业意图，uTorrent 广告/追踪是天然攻击面，Deluge on Olares = 私有化干净替代。
   - `self-hosted torrent client` / `torrent client with web interface`：量虽小但 KD=0，纯 Olares 语境词，GEO 引用位 + Olares Market 落地页首选。

4. **最大攻击面**：uTorrent 的**广告 + 追踪软件污点**（历史上被批评捆绑挖矿/广告软件）。"uTorrent 有广告，换 Deluge on Olares 自托管"是高转化叙事，`deluge and vpn`（KD 5, CPC $3.49）说明隐私导向用户愿意为解决方案付费。

5. **隐藏低 KD 金矿**：
   - `deluge and vpn`：KD 5，CPC $3.49（全库最高 CPC 词之一）——隐私敏感商业意图，极少竞争；Olares 内置 VPN 叙事完美贴合。
   - `deluge plugins`：KD 10，arr 栈集成（Deluge + Sonarr/Radarr）教程天然在这里展开。
   - `move when completed directory`（KD 14）、`deluge port issue`（KD 11）：技术支持词，流量小但 KD 极低，指向无头/服务器部署场景。

6. **GEO 前瞻布局**：
   - `"best self-hosted torrent client with web ui 2026"`——近零 SERP，抢 Perplexity/AI Overview 引用位
   - `"deluge on Olares setup guide"`——品牌长尾组合，Olares 文档站发布即可排名
   - `"torrent automation arr stack self-hosted"`——arr 生态关键词，在 AI 引用场景中拦截有 Sonarr/Radarr 需求的重度用户

7. **与既有 olares-500-keywords 的关联**：Deluge 报告补充了 torrent/下载器维度的比较词和隐私词（`deluge and vpn` 高 CPC 为新发现）；`utorrent alternative`（KD 23）和 `deluge vs qbittorrent`（KD 7）是 500 词表中 torrent 品类方向的低竞争补充词，建议录入内容队列。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_this）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
