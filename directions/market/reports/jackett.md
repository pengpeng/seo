# Jackett SEO 竞品分析报告（场景词分析——无独立官网）

> 域名：github.com/Jackett/Jackett（无独立官网，降级模式）| SEMrush US | 2026-07-06
> Jackett 是自托管 Torznab/TorrentPotato 索引代理——在 *arr 媒体自动化栈（Sonarr/Radarr/Lidarr）与数百个 BT tracker 之间充当统一 API 翻译层，是 homelab 媒体中心的核心基础设施之一。

---

## 项目理解（前置）

Jackett 作为代理服务器，把 Sonarr/Radarr/qBittorrent 等应用的搜索请求翻译成各 tracker 专属 HTTP 查询，解析响应并以 Torznab / TorrentPotato 标准格式返回结果。它解决了"每款下载应用都要自己适配 N 个 tracker"的碎片化问题，让任何支持 Torznab/Newznab 协议的客户端都能统一访问 1000+ 公开与私有 tracker。2026 年主要竞品 Prowlarr（*arr 官方生态接班人）已支持 900+ 索引器并具备原生 *arr 同步，Jackett 的主要生命力在于覆盖更多小众 tracker 及支持非 *arr 客户端。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自托管 Torznab 代理——统一访问 1000+ BT tracker，*arr 媒体栈基础组件 |
| 开源 / 许可证 | 是，GPL-2.0 |
| 主仓库 | [github.com/Jackett/Jackett](https://github.com/Jackett/Jackett)（★ 15.6K，420+ 贡献者，最新 v0.24.2151 发布于 2026-07-01） |
| 核心功能 | ① Torznab/TorrentPotato API 代理 ② 支持 1000+ 公开/私有 tracker ③ RSS feed 输出 ④ FlareSolverr 集成（Cloudflare bypass） ⑤ 内置缓存加速 |
| 商业模式 / 定价 | 完全免费开源；主流发行为 LinuxServer.io Docker 镜像 |
| 差异化 / 价值主张 | 比 Prowlarr 支持更多小众/区域 tracker；作为 Torznab 代理可对接任意兼容客户端（不限 *arr 生态） |
| 主要竞品（初判） | Prowlarr（最直接）、NZBHydra2（Usenet 偏重）、autobrr（IRC 实时发布场景） |
| Olares Market | ✅ 已上架（同栈：Sonarr、Radarr、Lidarr、Bazarr、qBittorrent、Jellyfin 亦在 Market） |
| 来源 | [GitHub README](https://github.com/Jackett/Jackett)；[RapidSeedbox 指南](https://www.rapidseedbox.com/blog/guide-to-jackett)；[selfhosting.sh 对比](https://selfhosting.sh/compare/prowlarr-vs-jackett/) |

---

## 流量基线（Phase 1）

**降级模式——无独立官网，跳过域名层报告。**

GitHub 仓库（github.com）通过品牌词"jackett docker"排 #3，但 GitHub 自身 SEMrush Rank 为 0（域名太大无单独排位）。Jackett 相关流量分散在 Reddit、RapidSeedbox、LinuxServer.io、SimplehomeLab 等第三方内容站，没有官方域名承接。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| prowlarr vs jackett ⭐ | 260 | 8 | $0 | 信息/商业 | 竞品对比核心词，KD 极低 |
| jackett vs prowlarr ⭐ | 260 | 8 | $0 | 信息/商业 | 同上，两个方向合计 ~520 实际搜索 |
| jackett alternative ⭐ | 10 | 0 | $0 | — | 量极小但 KD=0，GEO 级机会 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| prowlarr | 18,100 | 48 | $0.15 | 导航 | Jackett 直接竞品，KD 48 偏高 |
| sonarr | 12,100 | 39 | $0 | 导航 | 生态核心应用，Olares Market 上架 |
| radarr | 9,900 | 64 | $0 | 导航 | 生态核心，KD 高 |
| flaresolverr | 2,900 | 29 | $4.38 | 导航 | 与 Jackett/Prowlarr 深度绑定 ⭐ |
| jackett | 2,900 | 20 | $0 | 信息 | 品牌词但被时尚"jacket"严重污染，需结合长尾 ⭐ |
| lidarr | 3,600 | 37 | $0 | 导航 | 音乐 *arr，Olares Market 上架 |
| plex vs jellyfin ⭐ | 2,400 | 27 | $0 | 信息 | 媒体服务器对比高流量词，间接生态 |
| readarr ⭐ | 2,400 | 12 | $0 | 导航 | 电子书 *arr，KD 低 ⭐ |
| arr apps ⭐ | 390 | 26 | $0 | 信息 | *arr 生态合集词，Olares 可做全家桶落地页 ⭐ |
| nzbhydra ⭐ | 320 | 23 | $3.66 | 导航 | Usenet/Torrent 混合索引竞品 |
| private torrent tracker | 260 | 55 | $0 | 信息 | KD 高，暂不主攻 |
| nzbhydra2 ⭐ | 210 | 15 | $0 | 导航 | 与 Jackett 常并列提及 ⭐ |
| torrent rss feed ⭐ | 210 | 11 | $0 | 信息 | Jackett 核心功能词，KD 极低 ⭐ |
| torrent indexer | 170 | 40 | $0 | 信息 | 品类直接词，KD 偏高 |
| raspberry pi media server ⭐ | 880 | 23 | $0.39 | 信息 | homelab 硬件入口词 ⭐ |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| jackett api key error ⭐ | 880 | 13 | $0 | 信息 | 高量故障排查词，Olares 教程可截流 ⭐⭐ |
| elementum jackett ⭐ | 590 | 34 | $0 | 信息 | Kodi 插件集成，KD 偏高但量可观 |
| qbittorrent jackett api key error ⭐ | 210 | 16 | $0 | 信息 | 细化故障词，KD 低 ⭐ |
| jackett api key error qbittorrent ⭐ | 170 | 12 | $0 | 信息 | 同上变体 ⭐ |
| jackett docker ⭐ | 170 | 36 | $0 | 信息 | 安装入口词（KD 36 偏中） |
| jackett qbittorrent ⭐ | 170 | 20 | $0 | 信息 | qB 集成常见需求 ⭐ |
| jackett plugin ⭐ | 110 | 20 | $0 | 信息 | qBittorrent plugin 设置场景 ⭐ |
| jackett port ⭐ | 110 | 25 | $0 | 信息 | 配置细节词（默认 9117） ⭐ |
| qbittorrent jackett ⭐ | 110 | 20 | $0 | 信息 | 与上方互为变体 ⭐ |
| jackett github ⭐ | 110 | 37 | $0 | 导航 | 官方入口导航词 |
| jackett download | 90 | 38 | $0 | 导航 | 安装导航词 |
| what is jackett ⭐ | 70 | 22 | $0 | 信息 | 入门科普词，适合写基础解释文 ⭐ |
| jackett url ⭐ | 50 | 20 | $0 | 信息 | 配置细节词 ⭐ |
| what is jackett used for ⭐ | 50 | 0 | $0 | — | KD=0，零竞争介绍词 ⭐ |
| flaresolverr jackett setup ⭐ | 50 | 12 | $0 | 信息 | 与 Jackett 搭配的 Cloudflare bypass ⭐ |
| jackett api key ⭐ | 40 | 18 | $0 | 信息/商业 | 配置授权词 ⭐ |
| configure flaresolverr api url in jackett ⭐ | 40 | 3 | $0 | 信息 | 长尾极低 KD ⭐ |
| jackett not working ⭐ | 20 | — | $0 | 信息 | 故障排查词 |
| jackett sonarr radarr ⭐ | 20 | — | $0 | 信息 | 综合集成指南词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| arr apps ⭐ | 390 | 26 | $0 | 信息 | *arr 全家桶 = Olares Market 组合场景 ⭐⭐ |
| self hosted media server ⭐ | 70 | 45 | $0 | 信息 | KD 偏高，可作补充词 |
| raspberry pi media server ⭐ | 880 | 23 | $0.39 | 信息 | 硬件入口，Olares One / Raspberry Pi 双叙事 ⭐ |
| home server automation ⭐ | 30 | — | $0 | 信息 | 低量但语义契合 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Jackett 已在 Olares Market，整个 *arr 媒体自动化栈（Jackett + Prowlarr + Sonarr + Radarr + Lidarr + qBittorrent + Jellyfin）均在 Market——Olares 是唯一能"一键部署完整 homelab 媒体中心"的个人云操作系统，角度从"怎么配 Jackett"升级到"你的私有媒体中心，自己拥有"。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| prowlarr vs jackett | 260 | 8 | $0 | Olares Market 同时有 Jackett 和 Prowlarr，可写"在 Olares 上选哪个"对比文，解决新用户最高频的决策问题 | ⭐⭐⭐ |
| jackett vs prowlarr | 260 | 8 | $0 | 同上，两词合计约 520 月搜索量 | ⭐⭐⭐ |
| jackett api key error | 880 | 13 | $0 | Olares Market 一键部署后的常见问题；可做"Jackett API key 报错解决指南（Olares / Docker）"截流故障词 | ⭐⭐⭐ |
| arr apps | 390 | 26 | $0 | Olares Market 是完整 *arr 栈的最佳落地——一篇"Best *arr Apps on Olares"可同时覆盖 Jackett / Sonarr / Radarr / Prowlarr / Jellyfin，形成生态入口页 | ⭐⭐⭐ |
| flaresolverr | 2,900 | 29 | $4.38 | FlareSolverr 与 Jackett/Prowlarr 强绑定；Olares Market 应一并上架，内容可写"FlareSolverr + Jackett on Olares" | ⭐⭐ |
| torrent rss feed | 210 | 11 | $0 | Jackett 核心功能之一；RSS 订阅自动下载 = Olares 私有媒体中心核心场景叙事 | ⭐⭐ |
| nzbhydra2 | 210 | 15 | $0 | NZBHydra2 与 Jackett 常并列；Olares 可一键部署，适合"Jackett vs NZBHydra2 on Olares"次级扩展 | ⭐⭐ |
| raspberry pi media server | 880 | 23 | $0.39 | Raspberry Pi（ARM script 安装）+ Jackett = 硬件低成本入口；Olares ARM 支持可做叙事背书 | ⭐⭐ |
| readarr | 2,400 | 12 | $0 | KD 极低的 *arr 应用；若 Olares Market 上架后可做"Readarr + Jackett on Olares"系列内容 | ⭐⭐ |
| prowlarr query limit | 720 | 8 | $0 | Prowlarr 用户的高频痛点词；Olares Jackett 对比文中提及"无查询限制"可顺势截流 | ⭐⭐ |
| what is jackett | 70 | 22 | $0 | 入门科普词；Olares 作为 Jackett 主机的语境可自然植入 | ⭐ |
| jackett qbittorrent | 170 | 20 | $0 | qBittorrent 也在 Olares Market；"qBittorrent + Jackett on Olares 完整指南"是自然文章选题 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| jackett api key error | 880 | 13 | $0 | 信息 | **主词候选** | 量大 KD 极低；Olares Market 安装 Jackett 后最常遇问题，截流后自然转化 |
| prowlarr vs jackett | 260 | 8 | $0 | 信息/商业 | **主词候选** | 竞品对比核心词；KD=8 是整张词表最低；两向变体合计 ~520，Olares 同时上架两者，是最佳叙事切点 |
| jackett vs prowlarr | 260 | 8 | $0 | 信息/商业 | **主词候选** | 同上，与上词合并一篇文章 |
| arr apps | 390 | 26 | $0 | 信息 | **主词候选** | Olares Market 完整 *arr 栈落地页；覆盖 Jackett / Prowlarr / Sonarr / Radarr / Jellyfin 全链路，是高性价比生态入口词 |
| raspberry pi media server | 880 | 23 | $0.39 | 信息 | **主词候选** | 量大 KD 中等；Olares ARM script 安装背书；硬件入口可带 Jackett 使用场景 |
| flaresolverr | 2,900 | 29 | $4.38 | 导航 | **次级** | 量大但 KD 29 偏中、CPC 高说明商业价值；与 Jackett 文章自然联动（Cloudflare bypass 配置） |
| jackett qbittorrent | 170 | 20 | $0 | 信息 | **次级** | qBittorrent 也在 Olares Market，自然扩展为"qBittorrent + Jackett on Olares" |
| torrent rss feed | 210 | 11 | $0 | 信息 | **次级** | KD 极低；是 Jackett 核心功能词，写入 Jackett 指南可顺手收录 |
| nzbhydra2 | 210 | 15 | $0 | 导航 | **次级** | 与 Jackett 常并列提及；可作对比段落补充 |
| readarr | 2,400 | 12 | $0 | 导航 | **次级** | KD 极低 *arr 词，可作 *arr 生态合集文次级覆盖 |
| prowlarr query limit | 720 | 8 | $0 | 信息 | **次级** | KD=8，Prowlarr 用户痛点；"Why Jackett / no query limit"可作对比文章细节段落 |
| jackett plugin | 110 | 20 | $0 | 信息 | **次级** | qBittorrent Jackett plugin 配置；收入 Jackett 安装指南中 |
| jackett port | 110 | 25 | $0 | 信息 | **次级** | 配置细节（端口 9117），写入 Jackett 设置教程 |
| flaresolverr jackett setup | 50 | 12 | $0 | 信息 | **次级** | KD 极低，FlareSolverr 集成步骤；写入 Jackett 进阶配置文 |
| what is jackett used for | 50 | 0 | $0 | — | **次级** | KD=0，零竞争；适合写入文章 intro 或 FAQ 覆盖 |
| jackett alternative | 10 | 0 | $0 | — | **GEO** | 量极小 KD=0；AI Overview 会引用"Prowlarr 是 Jackett 现代替代方案"相关内容 |
| configure flaresolverr api url in jackett | 40 | 3 | $0 | 信息 | **GEO** | KD=3，超长尾；精准配置问题，FAQ 格式可抢 AI Overview 引用位 |
| jackett not working | 20 | — | $0 | 信息 | **GEO** | 故障词；FAQ/troubleshooting 段落收录 |
| torznab api | 20 | — | $0 | 信息 | **GEO** | 技术协议词；适合技术深度文章 intro 解释 |
| self hosted torrent indexer | — | — | $0 | 信息 | **GEO** | 无 Semrush 量，但 AI Overview / Perplexity 检索 Jackett 场景时高概率出现；前瞻布局 |

---

## 核心洞见

### 1. 品牌护城河

"jackett"品牌词（2,900/月）被时尚服装"jacket"搜索严重污染——SERP #1 是时装品牌 jakett.com，#3 是 Facebook 音乐人页面，真正的 Jackett 软件出现在 #2（AUR）/#4（GitHub issues），远不及 Prowlarr（18,100/月，KD 48，SERP 较干净）的心智强度。**无需正面刚"jackett"品牌词，避开污染，走长尾组合词（"jackett api key error"、"prowlarr vs jackett"）收益更高。**

### 2. 可复制的打法

SERP 竞争者主要是第三方内容站（RapidSeedbox、SimplehomeLab、bigiron.cc、selfhosting.sh），没有官方文档站主场优势——**这正是内容站可以竞争的开放市场**。当前排名词多为 Reddit 帖子（权威但非结构化），结构化的教程/对比文可以轻松超越。
- 打法：**故障词截流**（"jackett api key error" 880/月 KD 13）+ **对比文锚定**（"prowlarr vs jackett" KD 8）+ ***arr 生态合集页**（arr apps 390/月）三路并进。

### 3. 对 Olares 最关键的词

1. **`prowlarr vs jackett`**（KD 8，合计 ~520/月）——Olares Market 同时上架 Jackett 和 Prowlarr，是整个 Jackett 词库里 ROI 最高的词；"在 Olares 上用哪个更好"是天然 CTA。
2. **`jackett api key error`**（KD 13，880/月）——用户在 Olares Market 一键安装 Jackett 后最常遇到的错误；Olares 文档 / 博客覆盖此词，既截流又提升安装转化。
3. **`arr apps`**（KD 26，390/月）——Olares Market 是目前最完整的 *arr 全家桶平台（Jackett + Prowlarr + Sonarr + Radarr + Lidarr + qBittorrent + Jellyfin），可写"Best *arr Apps for Your Home Server"定义全生态入口页，持续带来 *arr 相关各子词长尾流量。

### 4. 最大攻击面

- **Prowlarr 的 query limit 限流问题**：`prowlarr query limit`（720/月，KD 8）是 Prowlarr 用户高频痛点——Jackett 无此限制，可在对比文中明确说明；
- **Jackett 无官网**：官方只有 GitHub，所有 Jackett 相关内容词都是待开垦的空地，Olares 的安装教程/配置指南可以抢占这批词；
- **Cloudflare bypass 痛点**：`prowlarr blocked by cloudflare`（70/月，KD 11）/ `flaresolverr jackett setup`（50/月，KD 12）——FlareSolverr 集成是用户最常踩坑的一步，Olares 可提供"开箱即用"叙事切入。

### 5. 隐藏低 KD 金矿

- `configure flaresolverr api url in jackett`（KD 3）、`what is jackett used for`（KD 0）、`jackett alternative`（KD 0）：三个近零竞争词，可放进 FAQ / intro 段落，几乎无成本覆盖。
- `torrent rss feed`（210/月，KD 11）：月量可观且 KD 极低，与 Jackett RSS 功能直接匹配，可作为 Jackett 安装指南的 H2 小节覆盖。
- `nzbhydra2`（210/月，KD 15）：与 Jackett 常并列提及，在对比文中加一段"Jackett vs NZBHydra2"即可收录。

### 6. GEO 前瞻布局

以下词当前搜索量极低或无数据，但在 AI Overview / Perplexity 搜索"如何搭建自托管媒体中心"时高概率被引用——提前写入 FAQ 可抢占引用位：
- "self hosted torrent indexer"
- "torznab api explained"
- "jackett vs prowlarr which is better 2026"
- "install jackett on home server without docker"
- "best torrent indexer for home media server"

### 7. 与既有分析的关联

- [qBittorrent 报告](reports/qbittorrent.md)（已完成）：qBittorrent 是 Jackett 最高频的集成客户端（`jackett qbittorrent` 170/月），两篇报告的内容可交叉引用；
- Jellyfin 报告（已完成）：Jellyfin 是媒体播放端，Jackett → Sonarr/Radarr → qBittorrent → Jellyfin 是完整自托管媒体链路，`plex vs jellyfin`（2,400/月，KD 27）可在生态合集文中自然关联；
- 与 `olares-500-keywords` 词表的补充：Jackett 带来的新高机会词（`prowlarr vs jackett` KD 8、`jackett api key error` KD 13、`arr apps` KD 26）均不在原 500 词表中，属于 homelab/媒体自动化子方向新增覆盖。

---

*数据来源：SEMrush US 数据库（phrase_this、phrase_these、phrase_fullsearch、phrase_related、phrase_organic）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。Jackett 无独立官网，Phase 1 域名基线跳过；数据来自关键词层研究（降级模式）。*
