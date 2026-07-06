# Bazarr SEO 竞品分析报告

> 域名：bazarr.media | SEMrush US | 2026-07-06
> Bazarr 是 *arr 媒体管理生态的字幕伴侣工具——自动为 Sonarr/Radarr 管理的影视库下载和升级字幕，是自托管家庭媒体服务器用户的必备组件之一。

---

## 项目理解（前置）

Bazarr 是一款开源字幕管理工具，作为 Sonarr（电视剧）和 Radarr（电影）的配套应用运行，根据用户配置的偏好自动搜索、下载并升级字幕文件。它支持对接 OpenSubtitles、Subscene、Addic7ed 等主流字幕源，以及 OpenAI Whisper（本地 AI 语音转录）作为兜底提供商。项目完全免费、无订阅制，社区维护，在自建媒体服务器用户群（Plex / Jellyfin / Emby）中高度认可。Bazarr 已上架 Olares Market，是 Olares 完整 *arr 媒体管理栈（Sonarr + Radarr + Bazarr）的关键一环。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Sonarr / Radarr 配套的自动字幕管理器，支持多字幕源 + AI Whisper 转录 |
| 开源 / 许可证 | 是，GPL-3.0 |
| 主仓库 | https://github.com/morpheus65535/bazarr（★ 4,100+） |
| 核心功能 | 自动下载缺失字幕；定期扫描升级字幕质量；手动搜索；支持 Whisper AI 本地转录；Docker / Windows / macOS / Linux 全平台 |
| 商业模式 / 定价 | 完全免费开源，无付费计划 |
| 差异化 / 价值主张 | 无缝集成 Sonarr + Radarr；支持 Whisper 本地 AI 生成字幕作为兜底；零成本自托管 |
| 主要竞品（初判）| Subliminal（CLI 工具）、Subzero（Plex 插件，已弃用）、手动 OpenSubtitles |
| Olares Market | **已上架** |
| 来源 | bazarr.media、github.com/morpheus65535/bazarr |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | bazarr.media |
| SEMrush Rank | 234,896 |
| 自然关键词数 | 202 |
| 月自然流量（US）| 7,338 |
| 自然流量估值 | $837/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 16 词 |
| 排名 4-10 位 | 31 词 |
| 排名 11-20 位 | 52 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.bazarr.media | 45 | 6,924 | 94.4% |
| wiki.bazarr.media | 157 | 414 | 5.6% |

> 主站承接绝大多数品牌导航流量；wiki 子域词数更多但流量很低——说明信息意图词排名位置整体偏后，内容覆盖度高于实际获取的曝光量。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| bazarr | 1 | 8,100 | 37 | $0.12 | 6,480 | 导航 | www.bazarr.media/ |
| bazaarr（拼写变体）| 1 | 260 | 51 | $0.14 | 208 | 导航 | www.bazarr.media/ |
| bazarr.（含句点）| 1 | 140 | 44 | $0 | 112 | 导航 | www.bazarr.media/ |
| bazarr setup | 1 | 110 | 17 | $0 | 88 | 信息 | wiki.bazarr.media/Getting-Started/Setup-Guide/ |
| bazarr plex | 1 | 40 | 29 | $0 | 32 | 导航 | www.bazarr.media/ |
| how to setup bazarr | 1 | 40 | 13 | $0 | 32 | 信息 | wiki.bazarr.media/Getting-Started/Setup-Guide/ |
| bazarr subtitles | 1 | 110 | 17 | $0 | 27 | 信息 | www.bazarr.media/ |
| bazzarr（拼写变体）| 1 | 90 | 25 | $0 | 22 | 信息 | www.bazarr.media/ |
| opensubtitles.org vs opensubtitles.com ⭐ | 4 | 320 | 8 | $0 | 11 | 信息 | wiki.bazarr.media/Troubleshooting/OpenSubtitles-migration/ |
| subzter | 8 | 1,900 | 51 | $0.67 | 11 | 导航 | www.bazarr.media/ |
| bazarr providers | 4 | 110 | 11 | $0 | 7 | 信息 | wiki.bazarr.media/...Whisper-Provider/ |
| opensubtitles org vs com ⭐ | 4 | 140 | 7 | $0 | 6 | 信息 | wiki.bazarr.media/Troubleshooting/OpenSubtitles-migration/ |
| bazarr port | 1 | 260 | 25 | $0 | 6 | 信息 | wiki.bazarr.media/.../Settings/ |
| linuxserver bazarr | 4 | 70 | 17 | $0 | 4 | 信息 | wiki.bazarr.media/.../docker/ |
| what is bazarr | 1 | 110 | 20 | $0 | 2 | 信息 | www.bazarr.media/ |
| agregarr | 19 | 1,900 | 21 | $0 | 2 | 信息 | wiki.bazarr.media/.../Plex/ |

> 亮点：`opensubtitles.org vs opensubtitles.com`（月量 320，KD 8）当前排第 4 位，是少见的有真实搜索量且 KD 极低的信息词，wiki 迁移故障排除页面已在承接。

### 付费词（Google Ads）

Bazarr 未购买任何付费广告，完全依赖自然流量。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| opensubtitles alternative ⭐ | 390 | 18 | $0 | 信息 | 主流字幕源替代词，与 Bazarr 高度相关 |
| opensubtitles.org vs opensubtitles.com ⭐ | 320 | 8 | $0 | 信息 | Bazarr wiki 已排 #4，极低 KD，内容有明确答案 |
| opensubtitles org vs com ⭐ | 140 | 7 | $0 | 信息 | 同上变体，Bazarr wiki 已排 #4 |
| bazarr alternative | 0 | 0 | $0 | — | 零量，无需写对比文 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| jellyfin subtitles ⭐ | 590 | 23 | $0 | 信息 | Jellyfin 用户求字幕方案，Bazarr 是标准答案 |
| plex subtitles | 390 | 48 | $0 | 信息 | KD 较高，竞争激烈 |
| self hosted media server | 70 | 45 | $0 | 信息 | KD 偏高，品类宽泛 |
| sonarr radarr subtitles ⭐ | 20 | 0 | $0 | 信息 | 量小但极精准，*arr 栈用户 |
| radarr subtitles ⭐ | 20 | 0 | $0 | 信息 | 同上，Radarr 用户找字幕解决方案 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| bazarr | 8,100 | 36 | $0.14 | 导航 | 核心品牌词，自己已 #1 |
| bazarr port | 210 | 16 | $0 | 信息 | 安装配置词，wiki 已覆盖 |
| bazarr providers ⭐ | 110 | 11 | $0 | 信息 | 字幕源选择，wiki #4 |
| bazarr setup ⭐ | 110 | 9 | $0 | 信息 | 新手安装向导，自己已 #1 |
| bazarr subtitles ⭐ | 110 | 17 | $0 | 信息 | 品牌+功能词，#1 |
| what is bazarr ⭐ | 110 | 20 | $0 | 信息 | 认知词，#1 |
| bazarr best providers ⭐ | 90 | 8 | $0 | 信息 | KD 极低，字幕源选型内容机会 |
| bazarr docker ⭐ | 70 | 26 | $0 | 信息 | Docker 安装词 |
| linuxserver bazarr ⭐ | 70 | 17 | $0 | 信息 | 热门 Docker 镜像，安装教程 |
| bazarr plex ⭐ | 40 | 29 | $0 | 导航 | Plex 集成词 |
| best subtitles provider for bazarr ⭐ | 40 | 13 | $0 | 信息 | 字幕源推荐，KD 低 |
| how to setup bazarr ⭐ | 40 | 13 | $0 | 信息 | 已排 #1 |
| sonarr radarr bazarr ⭐ | 20 | 0 | $0 | 信息 | 全栈组合词，极低 KD |
| bazarr whisper ⭐ | 20 | 0 | $0 | 信息 | AI 字幕生成，新兴特性词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| jellyfin subtitles ⭐ | 590 | 23 | $0 | 信息 | 自托管媒体场景最强量词 |
| opensubtitles alternative ⭐ | 390 | 18 | $0 | 信息 | 字幕源切换需求，Bazarr 解决此痛点 |
| opensubtitles.org vs opensubtitles.com ⭐ | 320 | 8 | $0 | 信息 | 迁移困惑，Bazarr wiki 页面已有排名 |
| sonarr radarr bazarr ⭐ | 20 | 0 | $0 | 信息 | 全栈安装词，Olares Market 一键安装三件套 |
| bazarr whisper ⭐ | 20 | 0 | $0 | 信息 | Olares 本地 AI 优势叙事切入点 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Bazarr 已在 Olares Market，Olares 的差异化叙事切入点有两个——一是"一键部署完整 *arr 媒体管理栈（Sonarr + Radarr + Bazarr + Jellyfin）"；二是"Whisper 本地 AI 字幕生成"叙事——Olares One 内置 RTX 5090，可在本地跑 Whisper 生成任意语言字幕，完全不依赖字幕源网站。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|-------|
| jellyfin subtitles | 590 | 23 | $0 | Jellyfin + Bazarr 在 Olares 上联动，字幕自动管理零配置；文章可 SEO 带量进入 *arr 生态圈 | ⭐⭐⭐ |
| opensubtitles alternative | 390 | 18 | $0 | Bazarr 支持几十个字幕源，在 Olares 上轻松切源；Olares 解决"离字幕源太远"的网络问题 | ⭐⭐⭐ |
| opensubtitles.org vs opensubtitles.com | 320 | 8 | $0 | Bazarr wiki 已排 #4，可借力做落地页 + 引流至 Olares 安装 Bazarr 的完整教程 | ⭐⭐ |
| bazarr best providers | 90 | 8 | $0 | 内容写字幕源选型（OpenSubtitles / Subscene / Whisper），顺带推 Olares Market 直装 Bazarr | ⭐⭐ |
| bazarr docker | 70 | 26 | $0 | Docker 安装繁琐 vs Olares Market 一键部署；对比内容机会 | ⭐⭐ |
| sonarr radarr bazarr | 20 | 0 | $0 | Olares Market 三件套一键安装，教程词，GEO 前哨 | ⭐⭐⭐ |
| bazarr whisper | 20 | 0 | $0 | Olares One 跑 Whisper 本地 AI 字幕生成，Olares 叙事：不依赖任何字幕网站，本地生成 | ⭐⭐⭐ |
| linuxserver bazarr | 70 | 17 | $0 | Docker 安装变体，对比 Olares Market 一键部署的优势 | ⭐⭐ |
| plex subtitles | 390 | 48 | $0 | KD 偏高，可作次级词并入 Plex 媒体服务器相关内容 | ⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| bazarr | 8,100 | 36 | $0.14 | 导航 | 次级（品牌导航） | 品牌护城河词，Bazarr 自己已牢牢占据 #1，不适合作为 Olares 主攻词；可作次级词出现在集成文章中 |
| jellyfin subtitles | 590 | 23 | $0 | 信息 | **主词候选** | 量大 KD 中等，Jellyfin + Bazarr 在 Olares 上的联动教程是最自然的落地内容；是市场最有潜力的字幕入口词 |
| opensubtitles alternative | 390 | 18 | $0 | 信息 | **主词候选** | KD<20 + 量 390 + 明确需求，Bazarr 聚合多字幕源的特性完美命中；可写"Best OpenSubtitles alternatives + self-hosted字幕管理" |
| plex subtitles | 390 | 48 | $0 | 信息 | 次级 | KD 高，作为 Plex 媒体服务器类文章的配套词 |
| opensubtitles.org vs opensubtitles.com | 320 | 8 | $0 | 信息 | **主词候选** | KD 极低！Bazarr wiki 已排 #4，Olares 做同主题更深入文章可超越；战略意义：帮 Bazarr 用户解决迁移困惑，引流 Bazarr on Olares 全套安装 |
| bazarr port | 210 | 16 | $0 | 信息 | 次级 | 安装配置词，并入 Bazarr 安装教程文章即可 |
| opensubtitles org vs com | 140 | 7 | $0 | 信息 | 次级 | 同上词变体，同一内容覆盖 |
| bazarr providers | 110 | 11 | $0 | 信息 | 次级 | 字幕源选型，并入"bazarr best providers"内容 |
| bazarr setup | 110 | 9 | $0 | 信息 | 次级 | Bazarr 自己已 #1；Olares 版安装教程可并入 |
| bazarr subtitles | 110 | 17 | $0 | 信息 | 次级 | 功能词，辅助主词 |
| what is bazarr | 110 | 20 | $0 | 信息 | 次级 | 认知词，适合页头介绍段；并入任何 Bazarr 相关文章 |
| bazarr best providers | 90 | 8 | $0 | 信息 | **主词候选** | KD 仅 8，量小但意图明确，单独写字幕源选型对比文即可排名；Olares 视角：Whisper 作为本地 AI 兜底源是差异化叙事 |
| bazarr docker | 70 | 26 | $0 | 信息 | 次级 | Docker 安装词，对比 Olares Market 一键部署 |
| linuxserver bazarr | 70 | 17 | $0 | 信息 | 次级 | 技术安装词，并入 Docker 安装教程 |
| bazarr plex | 40 | 29 | $0 | 导航 | 次级 | Plex 集成词，并入媒体服务器类文章 |
| best subtitles provider for bazarr | 40 | 13 | $0 | 信息 | 次级 | 同"bazarr best providers"，合并覆盖 |
| how to setup bazarr | 40 | 13 | $0 | 信息 | 次级 | 安装教程词，Bazarr #1；Olares 版补充 |
| sonarr radarr bazarr | 20 | 0 | $0 | 信息 | GEO | 全栈组合词，KD 为零；GEO/AI Overview 前哨词，适合 FAQ 或教程引言 |
| bazarr whisper | 20 | 0 | $0 | 信息 | GEO | 新兴 AI 特性词，KD 为零；Olares One 跑 Whisper 叙事的 GEO 占位词 |
| sonarr radarr subtitles | 20 | 0 | $0 | 信息 | GEO | 极精准的 *arr 用户词，GEO 前哨 |
| radarr subtitles | 20 | 0 | $0 | 信息 | GEO | 同上 |

---

## 核心洞见

1. **品牌护城河**：Bazarr 自己牢牢持有 `bazarr`（8,100/月）并排名 #1，KD 36 不低但护城河稳固。**Olares 不适合正面刚品牌词**，应从"字幕场景"和"媒体服务器栈"两个角度迂回，借力 Bazarr 的品牌认知做教程 + 集成内容。

2. **可复制的打法**：Bazarr wiki 的故障排除页面（opensubtitles 迁移）在 KD<10 的词上排出了位置，说明**精准回答具体问题的内容页**在该细分领域极易排名。Olares 可复制这个打法——做"如何在 Olares 上一键部署 Sonarr + Radarr + Bazarr + Jellyfin"完整教程，覆盖多个长尾组合词。

3. **对 Olares 最关键的词**：
   - `jellyfin subtitles`（590/月，KD 23）——流量最大、KD 适中，Jellyfin 已在 Olares Market，联动教程最自然
   - `opensubtitles alternative`（390/月，KD 18）——明确的替代意图，Bazarr 聚合多字幕源是最好的答案
   - `bazarr best providers`（90/月，KD 8）——KD 极低，字幕源选型文章 + Whisper 本地 AI 叙事，是 Olares One 差异化的最佳切入

4. **最大攻击面**：Bazarr 依赖第三方字幕源网站（OpenSubtitles、Subscene 等），这些网站时不时更改政策或关闭（如 opensubtitles.org→.com 的迁移风波产生了 320/月的搜索量）。**Olares + Whisper 本地 AI 字幕生成**是天然的反制叙事——用 Olares One 的 GPU 跑 Whisper，彻底不依赖任何字幕网站，永远不会因字幕源宕机失效。

5. **隐藏低 KD 金矿**：
   - `opensubtitles.org vs opensubtitles.com`（KD 8，320/月）——Bazarr 现在排 #4，做更深入的内容可升 Top 3；
   - `bazarr best providers`（KD 8，90/月）——字幕源选型，直接写即可
   - `sonarr radarr bazarr`（KD 0，20/月）——几乎零竞争，全栈教程的 GEO 布局位
   - `bazarr whisper`（KD 0，20/月）——AI 字幕新特性词，现在布局可卡位新趋势

6. **GEO 前瞻布局**：以下词月量虽小但语义精准，可嵌入 FAQ/教程引言抢 AI Overview / Perplexity 引用：
   - "Can I use Whisper with Bazarr to generate subtitles locally?"（命中 `bazarr whisper` + Olares One GPU 叙事）
   - "What's the best subtitle provider for Bazarr?"（命中 `bazarr best providers`）
   - "How to set up Sonarr, Radarr, and Bazarr together?"（命中 `sonarr radarr bazarr`）

7. **与既有分析的关联**：Bazarr 作为 *arr 生态的组成部分，与 Sonarr / Radarr / Prowlarr / Jellyfin 关键词形成**内容矩阵联动机会**——一篇"Olares 媒体服务器完整自建指南"可跨报告聚合这些应用词，单篇文章拿到多个*arr相关词排名，比逐一单打更高效。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_fullsearch、phrase_this、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
