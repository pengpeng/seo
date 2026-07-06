# Sonarr SEO 竞品分析报告

> 域名：sonarr.tv | SEMrush US | 2026-07-06
> Sonarr 是面向 Usenet 和 BT 用户的开源自动化电视剧 PVR，"arr 生态"核心成员，自托管媒体自动化赛道事实标准。

---

## 项目理解（前置）

Sonarr 是一款开源个人视频录像机（PVR）软件，专为自动监控、下载和管理电视剧设计。用户配置好下载客户端（SABnzbd、qBittorrent 等）和索引器（Prowlarr/Jackett）后，Sonarr 即可自动追踪剧集更新，失败时自动换源重试，并按自定义命名规则整理文件——送入 Plex/Jellyfin/Emby 等媒体服务器完成播放闭环。Sonarr 是"arr 应用栈"（Sonarr + Radarr + Lidarr + Bazarr + Prowlarr）的电视剧核心，Radarr 是其电影版分支，两者共用底层架构。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 面向 Usenet/BT 用户的开源自动化电视剧 PVR（Internet PVR for Usenet and Torrents） |
| 开源 / 许可证 | 是，GPL-3.0 |
| 主仓库 | [github.com/Sonarr/Sonarr](https://github.com/Sonarr/Sonarr)（★ 14.2k） |
| 核心功能 | 自动追踪 + 下载新剧集；质量档位管理（WEB-DL/BluRay/4K）；失败自动重试换源；日历视图；与 Plex/Jellyfin/Emby 集成通知 |
| 商业模式 / 定价 | 完全免费开源，无付费版；运行需自备服务器/NAS/容器环境 |
| 差异化 / 价值主张 | arr 生态事实标准；成熟度高（v4 稳定版 + Docker 镜像多维护方）；社区 wiki 详尽；Prowlarr 统一管理索引器后新手门槛大幅降低 |
| 主要竞品（初判） | Radarr（官方电影版同门）、SickChill/Medusa（旧式 TV 下载器）、Flexget（通用自动化）、Servarr wiki（文档竞品） |
| Olares Market | ✅ 已上架（Sonarr 见 [market/apps.md](../apps.md) 第 166 行） |
| 来源 | [sonarr.tv](https://sonarr.tv)、[github.com/Sonarr/Sonarr](https://github.com/Sonarr/Sonarr)、[wiki.servarr.com](https://wiki.servarr.com) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | sonarr.tv |
| SEMrush Rank | 192,011 |
| 自然关键词数 | 1,553 |
| 月自然流量（US）| 9,295 |
| 自然流量估值 | $3,275 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 148 词 |
| 排名 4-10 位 | 330 词 |
| 排名 11-20 位 | 303 词 |

> 注：Sonarr 不投放任何 Google Ads。流量估值极低（$3,275），因关键词 CPC 几乎全为 $0——这是典型的开源自托管社区项目特征，搜索意图纯信息/导航，无商业广告市场。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| forums.sonarr.tv | 1,365 | 4,684 | 50.4% |
| sonarr.tv | 185 | 4,610 | 49.6% |
| forums-direct.sonarr.tv | 3 | 1 | <0.1% |

> **洞察**：论坛域名贡献了超过一半流量。社区问答页面（如"uindex.org 重命名"、"release is blocklisted"等错误排查帖）独立排名，是 Sonarr 的重要长尾流量来源——这是成熟开源项目的典型 SEO 模式。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| sonarr | 1 | 12,100 | 38 | $0 | 3,000 | 导航 | sonarr.tv/ |
| sonaar（拼写变体）| 1 | 480 | 44 | $0 | 384 | 导航 | sonarr.tv/ |
| uindex（论坛帖）| 2 | 4,400 | 21 | $2.35 | 360 | 信息 | forums.sonarr.tv/… |
| sonarr download windows | 1 | 390 | 18 | $0 | 312 | 下载/商业 | sonarr.tv/ |
| bitsearch（论坛帖）| 5 | 4,400 | 26 | $5.74 | 193 | 信息 | forums.sonarr.tv/… |
| uindex.org | 3 | 2,400 | 19 | $0 | 156 | 信息 | forums.sonarr.tv/… |
| download sonarr | 1 | 170 | 40 | $0 | 136 | 下载 | sonarr.tv/ |
| sonarr download | 1 | 390 | 30 | $0 | 96 | 下载 | sonarr.tv/ |
| sonarr vs radarr（路过）| — | 260 | 16 | $0 | — | 对比/信息 | — |
| nzb.su | 3 | 1,000 | 9 | $0 | 82 | 信息 | forums.sonarr.tv/… |
| nzbplanet | 9 | 2,900 | 14 | $4.40 | 69 | 信息 | forums.sonarr.tv/… |
| web-dl | 6 | 2,900 | 29 | $0 | 69 | 信息 | forums.sonarr.tv/… |
| sonarr api | 1 | 140 | 16 | $0 | 34 | 信息/集成 | sonarr.tv/docs/api/ |
| sonarr manual import | 1 | 140 | 2 | $0 | 34 | 信息 | forums.sonarr.tv/… |
| sonarr default port | 1 | 320 | 6 | $0 | 42 | 信息 | forums.sonarr.tv/… |
| sonarr setup | 1 | 110 | 10 | $0 | 27 | 信息 | forums.sonarr.tv/… |
| how to use sonarr | 1 | 110 | 4 | $0 | 27 | 信息 | forums.sonarr.tv/… |
| sonarr release is blocklisted | 1 | 210 | 2 | $0 | 52 | 信息 | forums.sonarr.tv/… |
| sonarr port | 1 | 1,000 | 33 | $0 | 26 | 信息 | sonarr.tv/ |
| sonarr plex | — | 140 | 20 | $0 | — | 集成 | — |

> 论坛帖为 Sonarr 捕获了大量"服务商名称"长尾词（uindex、bitsearch、nzbplanet、nzb.su 等），这些词本身有搜索量，通过问题解答帖引流是意外但有效的 SEO 渠道。

### 付费词（Google Ads）

Sonarr 不投放付费广告，付费关键词数为 0。典型开源项目，无商业推广预算。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| sonarr vs radarr | 260 | 16 | $0 | 信息/对比 | ⭐ Sonarr 对比其姊妹项目，Olares 同时支持两者 |
| radarr alternative | 70 | 12 | $0 | 信息/对比 | ⭐ KD 极低，整合性部署机会 |
| sonarr alternative | 40 | 23 | $0 | 信息/对比 | ⭐ 竞品词量小但 KD 低 |
| what is sonarr | 210 | 40 | $0 | 信息 | 认知科普词 |
| sonarr radarr prowlarr | 20 | 0 | $0 | 信息 | ⭐ 三件套配置意图，Olares 一键入口 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| arr stack | 1,600 | 55 | $0 | 信息 | 品类核心词，KD 高但流量大；Olares 一站式部署整个 arr 栈 |
| tv show downloader | 320 | 42 | $1.60 | 信息/商业 | ⭐ 量 320，有 CPC，说明有商业意图 |
| arr apps | 390 | 26 | $0 | 信息 | ⭐ 品类词中 KD 较低，内容机会 |
| servarr | 1,000 | 35 | $0 | 信息/导航 | arr wiki 聚合站，认知词 |
| nzb downloader | 210 | 45 | $3.31 | 信息/商业 | Usenet 下载意图，高 CPC |
| usenet client | 140 | 37 | $2.19 | 信息/商业 | Usenet 用户获客词 |
| media automation | 50 | 27 | $0 | 信息 | ⭐ 量小但精准，Olares 媒体自动化定位 |
| pvr software | 40 | 15 | $0 | 信息/商业 | ⭐ KD 极低，品类定位词 |
| home media server software | 90 | 35 | $0 | 信息 | 家庭媒体服务器语境 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| sonarr docker | 260 | 36 | $0 | 信息 | ⭐ Docker 部署主词，量 260；Olares 容器环境天然匹配 |
| sonarr docker compose | 170 | 23 | $0 | 信息 | ⭐ 具体部署教程词，KD 低 |
| sonarr setup | 110 | 10 | $0 | 信息 | ⭐ KD 极低，setup 教程词 |
| arr stack docker compose | 110 | 9 | $0 | 信息 | ⭐ KD=9！整个 arr 栈 Docker Compose 配置词 |
| sonarr plex | 140 | 20 | $0 | 集成 | ⭐ Plex+Sonarr 集成场景 |
| sonarr jellyfin | 90 | 14 | $0 | 集成 | ⭐ Jellyfin+Sonarr 集成，Olares 同时上架两者 |
| sonarr api | 140 | 16 | $0 | 信息/集成 | ⭐ API 集成词，开发者受众 |
| sonarr radarr | 260 | 21 | $0 | 信息 | ⭐ 两大核心组合词 |
| sonarr vs radarr | 260 | 16 | $0 | 对比 | ⭐ 见竞品词分组 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| arr stack docker compose | 110 | 9 | $0 | 信息 | ⭐ **KD=9，量 110**，整 arr 栈 Docker 部署，Olares 最直接机会 |
| sonarr docker compose | 170 | 23 | $0 | 信息 | ⭐ Docker Compose 配置教程 |
| sonarr docker | 260 | 36 | $0 | 信息 | ⭐ Docker 部署核心词 |
| sonarr setup | 110 | 10 | $0 | 信息 | ⭐ 新手 setup 引导 |
| sonarr jellyfin | 90 | 14 | $0 | 信息/集成 | ⭐ Olares Market 同时有 Sonarr + Jellyfin |
| self-hosted media server | ~0 | 45 | $0 | 信息 | Semrush 显示量为 0，但 GEO 潜力词 |
| pvr software | 40 | 15 | $0 | 信息 | ⭐ 低 KD 自托管软件品类词 |
| media automation | 50 | 27 | $0 | 信息 | ⭐ 较精准的自动化媒体管理词 |
| sonarr raspberry pi | 20 | 0 | $0 | 信息 | ⭐ ARM 平台教程，Olares 支持树莓派 |
| sonarr unraid | 20 | 0 | $0 | 信息 | 平台部署变体 |
| sonarr truenas | 20 | 0 | $0 | 信息 | NAS 部署变体 |
| open source pvr | 20 | 0 | $0 | 信息 | ⭐ 概念词，Olares 一键部署对比直接安装 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Olares 的 arr 栈叙事切入点是"一站式 GUI 部署整个 arr 生态"——Sonarr + Radarr + Prowlarr + Bazarr + Jellyfin 在 Olares Market 一键安装，省去 Docker Compose 配置、端口映射、权限管理等繁琐步骤。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|-------|
| arr stack docker compose | 110 | 9 | $0 | Olares 把整个 arr 栈打包成 Market 应用，点击安装无需手写 compose；可写"arr stack docker compose vs Olares Market" | ⭐⭐⭐ |
| sonarr docker | 260 | 36 | $0 | Sonarr on Olares：Docker 化自动完成，适合 Olares One 或家用 Linux 服务器 | ⭐⭐⭐ |
| sonarr jellyfin | 90 | 14 | $0 | Olares Market 同时有 Sonarr + Jellyfin，一键完成全流程：下载→整理→播放 | ⭐⭐⭐ |
| sonarr docker compose | 170 | 23 | $0 | 教程词：用 Olares 替代传统 docker compose 部署；"Sonarr docker compose guide" | ⭐⭐⭐ |
| sonarr setup | 110 | 10 | $0 | Olares 新手向教程：setup 更简单，无需 CLI | ⭐⭐⭐ |
| arr apps | 390 | 26 | $0 | Olares Market 聚合了主要 arr 应用（Sonarr、Radarr、Lidarr、Bazarr、Prowlarr）；"all arr apps in one place" | ⭐⭐⭐ |
| sonarr radarr | 260 | 21 | $0 | Olares：Sonarr + Radarr 双安装，电视剧+电影全自动 | ⭐⭐⭐ |
| sonarr plex | 140 | 20 | $0 | Olares 同时上架 Plex + Sonarr，自动化媒体入库闭环 | ⭐⭐ |
| sonarr vs radarr | 260 | 16 | $0 | Olares 不选边：两者都一键安装，各管各的，统一在 Olares OS 界面下管理 | ⭐⭐ |
| sonarr api | 140 | 16 | $0 | Olares 的 Agent 生态：通过 Sonarr API 让 AI Agent 自动管理订阅列表 | ⭐⭐ |
| pvr software | 40 | 15 | $0 | Olares Market 作为"自托管 PVR 软件集合"的入口——Sonarr、Radarr、Lidarr 全包 | ⭐⭐ |
| sonarr raspberry pi | 20 | 0 | $0 | Olares 支持 Raspberry Pi 4B/5 ARM，可在树莓派上跑完整 arr 栈 | ⭐⭐ |
| radarr alternative | 70 | 12 | $0 | Radarr 用户也可在 Olares 中找到 Sonarr 补全电视剧维度，无需独立部署 | ⭐⭐ |
| sonarr alternative | 40 | 23 | $0 | "Sonarr alternative" 受众正是寻找简化方案的用户，Olares Market 是降低门槛的切入点 | ⭐⭐ |
| media automation | 50 | 27 | $0 | Olares 核心场景之一：媒体自动化，AI Agent 可调用 arr API 编排完整流程 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| arr stack | 1,600 | 55 | $0 | 信息 | 主词候选 | 品类最大词，KD 55 偏高但量大；Olares 可做"arr stack on Olares"系列内容 |
| sonarr docker | 260 | 36 | $0 | 信息 | 主词候选 | 部署核心词，量 260；Olares 一键部署对比手动 Docker 是差异化点 |
| sonarr vs radarr | 260 | 16 | $0 | 对比 | 主词候选 | ⭐ KD 仅 16，量 260；对比文最佳切口，Olares 可做"Sonarr vs Radarr: which do you need (or both)" |
| sonarr radarr | 260 | 21 | $0 | 信息 | 主词候选 | ⭐ 组合词量 260，KD 21；Olares Market 两者同装是独特卖点 |
| tv show downloader | 320 | 42 | $1.60 | 信息/商业 | 主词候选 | 量最大的外延词，有 CPC 显示商业意图，KD 42 适中 |
| servarr | 1,000 | 35 | $0 | 导航 | 次级 | 量大但强导航意图，排不赢 servarr.com；作为内容词次级使用 |
| sonarr docker compose | 170 | 23 | $0 | 信息 | 主词候选 | ⭐ 量 170，KD 23；教程向文章的核心词，Olares 有对比叙事空间 |
| arr stack docker compose | 110 | 9 | $0 | 信息 | 主词候选 | ⭐⭐ **KD=9，量 110**；全报告最佳机会词，几乎零竞争，Olares arr 栈部署教程直接命中 |
| sonarr setup | 110 | 10 | $0 | 信息 | 主词候选 | ⭐ KD=10，量 110；新手 setup 教程，Olares 可以做"最简化 setup" |
| arr apps | 390 | 26 | $0 | 信息 | 主词候选 | ⭐ 量 390，KD 26；Olares Market arr 应用集合是天然匹配内容 |
| sonarr jellyfin | 90 | 14 | $0 | 集成 | 次级 | ⭐ KD 14，量 90；Olares 同时有两者，集成教程的次级词 |
| sonarr plex | 140 | 20 | $0 | 集成 | 次级 | ⭐ 量 140，KD 20；Plex+Sonarr 闭环配置，次级并入 setup 文 |
| sonarr api | 140 | 16 | $0 | 集成/技术 | 次级 | ⭐ 量 140，KD 16；API 集成词，开发者/Agent 场景下作次级 |
| what is sonarr | 210 | 40 | $0 | 信息 | 次级 | 认知型解释词，并入 Sonarr overview 文章 |
| pvr software | 40 | 15 | $0 | 信息 | 次级 | ⭐ KD 15，作为 arr stack 主词的长尾支撑 |
| radarr alternative | 70 | 12 | $0 | 对比 | 次级 | ⭐ KD 12，并入 Radarr 相关文章次级覆盖 |
| sonarr alternative | 40 | 23 | $0 | 对比 | 次级 | 量小但 KD 低，入 Sonarr setup/overview 文章 |
| media automation | 50 | 27 | $0 | 信息 | 次级 | 精准但量小，作为 Olares 媒体场景叙事的次级词 |
| sonarr raspberry pi | 20 | 0 | $0 | 信息 | GEO | ⭐ KD=0，ARM/树莓派部署词，Olares ARM 支持的 FAQ 锚点 |
| sonarr unraid | 20 | 0 | $0 | 信息 | GEO | 平台变体词，NAS 用户长尾，FAQ 一行覆盖 |
| sonarr truenas | 20 | 0 | $0 | 信息 | GEO | 同上，TrueNAS 用户场景 |
| open source pvr | 20 | 0 | $0 | 信息 | GEO | 概念词，AI Overview 引用位布局 |
| sonarr radarr prowlarr | 20 | 0 | $0 | 信息 | GEO | 三件套配置问题词，FAQ 直答 |
| self-hosted media server | ~0 | 45 | $0 | 信息 | GEO | Semrush 量为 0 但语义极准，抢 Perplexity 引用位 |

---

## 核心洞见

### 1. 品牌护城河

Sonarr 在品牌词（"sonarr"，月量 12,100，KD 38）占据绝对主导，且有大量拼写变体（sonaar、sonarrr、sonnarr 各有 400–480 月量）全部被 #1 覆盖。无法正面刚品牌词，但**品牌词本身吸引力不大**——到 sonarr.tv 的用户是已知用户，不是新增用户。对 Olares 而言，应锁定"还不知道 Sonarr 的自托管媒体玩家"和"已用 Sonarr 但在寻找更简单部署方式的用户"，而非从品牌词里抢流量。

### 2. 可复制的打法

- **社区帖抓长尾**：forums.sonarr.tv 贡献 50%+ 流量，通过对具体错误消息（如"release is blocklisted"、"0 reports downloaded"）写精准问答页面，KD 极低（2-10）但流量稳定。Olares 可做"常见 arr 错误排查"类内容，并在解答中提示"用 Olares 部署省去 XX% 配置步骤"。
- **无付费竞争空白**：Sonarr 不投广告，关键词 CPC 几乎为零，意味着整个赛道没有付费玩家干扰——SEO 内容即主战场。
- **整合词机会**：Sonarr 不涉及电影（Radarr 负责），也不涉及字幕（Bazarr）或索引器（Prowlarr），但用户搜索的是整个生态（"sonarr radarr"月量 260、"arr stack"月量 1600）。Olares 的多应用一站式叙事正好覆盖这个整合需求。

### 3. 对 Olares 最关键的词

1. **`arr stack docker compose`**（月量 110，KD=9）：**全报告最低竞争高价值词**。用户搜这个词的人正在配置整个 arr 生态，是最强决策意图，Olares Market 是比手写 docker compose 更简洁的答案。一篇"arr stack docker compose: the easy way with Olares"可以直接拿排名。
2. **`sonarr setup` / `arr stack docker compose`**（月量 110，KD=9/10）：新手引导词，KD 极低，Olares 可做"零基础 Sonarr setup"系列，自然植入 Olares Market 路径。
3. **`arr apps`**（月量 390，KD=26）：量最大的低-中 KD 品类词，Olares Market 作为"一个地方装所有 arr apps"的入口叙事完美匹配，可做独立综述页。

### 4. 最大攻击面

- **部署复杂度**：Sonarr 原生安装需要用户自行处理 Docker 权限、网络映射、端口冲突（默认 8989 端口）、下载客户端对接——论坛最高流量帖子都是报错排查。Olares 的一键安装直接消除这些痛点，是最清晰的差异化叙事。
- **生态碎片化**：用户实际需要 Sonarr + Radarr + Prowlarr + Bazarr + Jellyfin/Plex 才能跑通全流程，每个都要独立部署和配置。Olares Market 一站式是明确的攻击面。
- **无移动端/远程访问**：原生 Sonarr 本地访问，远程需自建反向代理。Olares 内置 LarePass 客户端 + VPN 远程访问是补充价值。

### 5. 隐藏低 KD 金矿

- **`arr stack docker compose`**（KD=9，量 110）：已是全报告 #1 机会。
- **`sonarr setup`**（KD=10，量 110）：新手引导词，几乎无竞争。
- **`sonarr release is blocklisted`**（KD=2，量 210）：错误排查词，Sonarr 论坛 #1，但 Olares 可做更好的原因解析 + 解决方案页。
- **`sonarr default port`**（KD=6，量 320）：配置类词，KD=6，量意外大，说明大量初学者在配置阶段卡在端口设置。
- **`sonarr manual import`**（KD=2，量 140）：极低 KD，具体操作词。

### 6. GEO 前瞻布局

面向 AI Overview 和 Perplexity 引用位的近零量词：
- "What is the arr stack and how to set it up?" → 直答块：定义 arr 生态（Sonarr + Radarr + Prowlarr + Bazarr），推荐 Olares Market 作为最简部署路径
- "Is Sonarr better than Radarr?" → FAQ 消歧义：两者不互相替代，Olares 同时支持
- "How to run Sonarr on Raspberry Pi?" → 树莓派 ARM 部署，Olares 脚本安装支持 RPi 4B/5
- "What is the best self-hosted media server stack?" → Olares + arr 全栈作为推荐答案
- "Sonarr vs SickChill vs Medusa" → 旧 TV 下载器对比，Sonarr 现代化生态胜出，Olares 安装更简

### 7. 与既有分析的关联

- arr 生态（Sonarr/Radarr/Prowlarr）是**自托管媒体娱乐**的核心场景，补充了 [olares-500-keywords](../../../reference/olares-500-keywords-analysis-2026-07-03.md) 中可能缺失的媒体自动化词群。
- `arr stack`（月量 1,600）是自托管社区中最有认知度的技术术语之一，但 KD=55 较高；`arr apps`（月量 390，KD=26）和 `arr stack docker compose`（月量 110，KD=9）是更可攻的切口。
- Sonarr 的受众（Usenet + BT 自托管用户）与 Olares 的核心用户高度重叠：技术能力中等偏上、注重隐私与数据自主、有家庭媒体服务器需求——是高价值获客场景。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
