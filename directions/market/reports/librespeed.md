# LibreSpeed SEO 竞品分析报告

> 域名：librespeed.org | SEMrush US | 2026-07-06
> 自托管互联网测速工具的最知名开源实现，主打无 Flash/Java、零依赖、隐私可控；GitHub ~15k stars。

---

## 项目理解（前置）

LibreSpeed 是一款轻量级、基于浏览器的 HTML5 开源网速测试工具，可部署在自己的服务器上，用于测量下载、上传、延迟（Ping）和抖动（Jitter）。它是 Ookla/Speedtest.net 等中心化付费测速服务的直接开源替代方案，核心差异在于：用户完全掌控测试服务器与结果数据，且无任何第三方 SDK/广告注入。项目支持 PHP、Go、Rust 等多种后端，原生支持 Docker 部署，内置可选遥测与结果分享功能。对 ISP、网络运维人员、Homelab 玩家和注重隐私的用户来说是首选自托管方案。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自托管 HTML5 网速测试，Ookla 的开源、零追踪替代方案 |
| 开源 / 许可证 | 是，LGPL-3.0（前端）+ 各后端自行授权 |
| 主仓库 | [github.com/librespeed/speedtest](https://github.com/librespeed/speedtest)（★ ~15k） |
| 核心功能 | 下载/上传/Ping/Jitter 测速；IP/ISP 检测（可选）；遥测与结果分享（可选）；多测速点支持；连接稳定性测试；Docker 一键部署 |
| 商业模式 / 定价 | 纯开源免费，无付费版；librespeed.org 提供公共演示实例 |
| 差异化 / 价值主张 | 无 Flash/Java/WebSocket；完全自托管；数据不离服务器；后端选 PHP/Go/Rust/Node；轻量（几 KB JS） |
| 主要竞品（初判）| openspeedtest.com、speedof.me、speedtest.net（Ookla）、fast.com（Netflix） |
| Olares Market | 已上架 ✅（[market/apps.md](../apps.md) 第 202 行） |
| 来源 | [librespeed.org](https://librespeed.org)、[GitHub README](https://github.com/librespeed/speedtest)、[doc.md](https://github.com/librespeed/speedtest/blob/master/doc.md) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | librespeed.org |
| SEMrush Rank | 1,070,926 |
| 自然关键词数 | 364 |
| 月自然流量（US）| 988 |
| 自然流量估值 | $1,296 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 17 词 |
| 排名 4-10 位 | 45 词 |
| 排名 11-20 位 | 45 词 |

> **关键观察**：librespeed.org 本身流量极低（US 月均不足 1k），这是典型的"工具型演示站"现象——绝大多数用户直接部署了自己的实例，并不返回官网。真实的"品牌意识"流量都散布在 GitHub、Docker Hub、各类 Homelab 教程站和 Reddit 上。与 GitHub 15k stars 相比，官网流量几乎可忽略不计，说明社区生态远大于官网 SEO 影响力。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| librespeed.org | 364 | 988 | 100% |

> 无 blog/docs 等子域名，全量流量集中在主域名单一演示页。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| libretest | 1 | 720 | 35 | $0.77 | 178 | 导航 | librespeed.org |
| librespeed | 1 | 720 | 34 | $4.97 | 178 | 导航 | librespeed.org |
| libre speed | 1 | 140 | 40 | $0.00 | 112 | 信息 | librespeed.org |
| libre speed test | 1 | 110 | 38 | $0.00 | 88 | 导航 | librespeed.org |
| sppedtest（typo） | 18 | 14,800 | 94 | $1.54 | 44 | 导航 | librespeed.org |
| libre speedtest | 1 | 140 | 32 | $0.00 | 34 | 导航 | librespeed.org |
| open speed test | 6 | 2,900 | 58 | $1.87 | 29 | 信息+商业 | librespeed.org |
| html5 speed test | 6 | 720 | 87 | $0.00 | 25 | 信息 | librespeed.org |
| open internet speed test | 7 | 880 | 90 | $2.89 | 19 | 信息 | librespeed.org |
| librespeed test | 1 | 70 | 35 | $0.00 | 17 | 信息+导航 | librespeed.org |
| open source bandwidth test | 1 | 70 | 64 | $0.00 | 17 | 信息 | librespeed.org |
| internet speed html5 | 7 | 590 | 76 | $0.00 | 17 | 信息 | librespeed.org |
| test speed html5 | 7 | 590 | 86 | $0.00 | 17 | 信息 | librespeed.org |
| speedtest.org | 7 | 480 | 85 | $0.41 | 14 | 信息 | librespeed.org |
| html5 internet speed test | 7 | 480 | 84 | $0.00 | 14 | 信息 | librespeed.org |
| speed test no flash | 3 | 210 | 91 | $0.00 | 13 | 信息 | librespeed.org |
| speed test html5 | 6 | 320 | 86 | $0.00 | 11 | 信息 | librespeed.org |
| bandwidth test no flash | 3 | 140 | 87 | $0.00 | 9 | 信息 | librespeed.org |
| alternative speed test | 1 | 40 | 80 | $0.00 | 9 | 信息+导航 | librespeed.org |
| torrent speed test | 3 | 110 | 12 | $0.00 | 9 | 信息 | librespeed.org |
| speedtest alternative | 1 | 50 | 51 | $0.00 | 6 | 信息 | librespeed.org |
| open speed | 8 | 1,000 | 65 | $4.61 | 6 | 信息+商业 | librespeed.org |
| freespeed web app | 9 | 170 | 5 | $0.00 | 4 | 信息 | librespeed.org |
| open source speed test | — | 90 | 63 | $0.00 | — | 信息+商业 | librespeed.org |

> **亮点词**：`torrent speed test`（110 月量，KD=**12** ⭐，排名 3 位）是整张表里竞争力最低的有量词；`freespeed web app`（KD=**5** ⭐）虽量小但几乎无竞争。`sppedtest`（typo，14,800 量但 KD=94，排名 18）属于大词偶尔挂蹭流量，不可持续。

### 付费词（Google Ads）

无付费广告投放（0 付费关键词），符合开源项目特征。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| openspeedtest | 3,600 | 57 | $4.61 | 商业 | 最强直接竞品品牌词，量最大 |
| open speed test | 2,900 | 58 | $1.87 | 信息+商业 | 高量但 KD 中等，librespeed 排名第 6 |
| open internet speed test | 880 | 90 | $2.89 | 信息 | 高 KD，已排第 7，难突破 |
| speedtest alternative | 50 | 51 | $0.00 | 信息 | 量小但有意图，librespeed 本身排 #1 |
| openspeedtest alternative | 20 | 0 | $0.00 | — | ⭐ 极低竞争，对比文机会 |
| librespeed alternative | 20 | 0 | $0.00 | — | ⭐ 极低竞争，可做"LibreSpeed 替代"反向内容 |
| librespeed vs openspeedtest | 20 | 0 | $0.00 | — | ⭐ 极低竞争，对比文直接切入 |
| speedtest.net alternative | 10 | 0 | $0.00 | — | ⭐ 量小，但 Ookla 品牌对比语义精准 |
| fast.com alternative | 20 | 0 | $0.00 | — | ⭐ Netflix 测速对比词，自托管角度强 |
| ookla alternative | 20 | 0 | $0.00 | — | ⭐ 直接对标 Ookla 品牌 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open speed test | 2,900 | 58 | $1.87 | 信息+商业 | 最大品类词，但 KD 中等 |
| open internet speed test | 880 | 90 | $2.89 | 信息 | 高量高 KD |
| open source speed test | 90 | 63 | $0.00 | 信息+商业 | 直接品类词，KD 63 仍较高 |
| torrent speed test | 110 | **12** | $0.00 | 信息 | ⭐ 低 KD 金矿，librespeed 天然切入 |
| html5 speed test | 720 | 87 | $0.00 | 信息 | 量大但 KD 极高 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| librespeed | 720 | 34 | $4.97 | 导航 | 品牌主词，librespeed.org 排 #1 |
| libretest | 720 | 35 | $0.77 | 导航 | 品牌变体，排 #1；量等于品牌词本身 |
| libre speed | 140 | 40 | $0.00 | 信息 | 品牌空格变体，排 #1 |
| libre speedtest | 140 | 32 | $0.00 | 导航 | 品牌变体，排 #1 |
| libre speed test | 110 | 38 | $0.00 | 导航 | 品牌变体，排 #1 |
| librespeed test | 70 | 35 | $0.00 | 信息+导航 | 品牌变体，排 #1 |
| librespeed docker | 20 | 0 | $0.00 | — | ⭐ 技术安装词，Homelab 受众 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted speed test | 20 | 0 | $0.00 | — | ⭐ 零竞争，精准自托管意图 |
| open source speed test | 90 | 63 | $0.00 | 信息+商业 | 量有但 KD 高，竞争激烈 |
| librespeed docker | 20 | 0 | $0.00 | — | ⭐ Docker 部署搜索词，Homelab 场景 |
| private speed test | 20 | 0 | $0.00 | — | ⭐ 隐私意图词，Olares 叙事直接切入 |
| speed test no ads | 20 | 0 | $0.00 | — | ⭐ 用户痛点词（Ookla 有广告） |
| torrent speed test | 110 | 12 | $0.00 | 信息 | ⭐ 低 KD，自托管用户常见场景 |

---

## Olares 关联词（Phase 3）

**核心逻辑：LibreSpeed 是 Olares Market 已上架的零配置工具类 App，Olares 的差异化叙事是"一键部署在你自己的服务器上，结果数据只在你的硬件里"——隐私、所有权、自主可控三轴与 LibreSpeed 的设计哲学完全一致，是绝佳内容锚点。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|-------|
| self hosted speed test | 20 | 0 | $0.00 | Olares Market 一键安装 LibreSpeed，秒变私有测速服务器 | ⭐⭐⭐ |
| private speed test | 20 | 0 | $0.00 | 测速结果不上传任何第三方，数据完全留在 Olares 本机 | ⭐⭐⭐ |
| librespeed docker | 20 | 0 | $0.00 | Olares 托管容器化 LibreSpeed，比裸 Docker 更简单（无需手动配置） | ⭐⭐⭐ |
| openspeedtest alternative | 20 | 0 | $0.00 | 对比文：LibreSpeed vs OpenSpeedTest——Olares Market 两者都支持 | ⭐⭐⭐ |
| speedtest alternative | 50 | 51 | $0.00 | Olares 上运行 LibreSpeed 作为 Ookla 替代，隐私全控 | ⭐⭐⭐ |
| librespeed alternative | 20 | 0 | $0.00 | 对比文反向：已用 LibreSpeed 的用户可在 Olares 上一键管理 | ⭐⭐ |
| torrent speed test | 110 | 12 | $0.00 | 自托管测速服务器 + Olares 同时跑 qBittorrent，内网环境测速场景 | ⭐⭐ |
| ookla alternative | 20 | 0 | $0.00 | 隐私角度对标：Ookla 收集用户数据 vs Olares+LibreSpeed 零泄漏 | ⭐⭐⭐ |
| open source speed test | 90 | 63 | $0.00 | 品类入口词，用于 Olares Market App 页和博文引入 | ⭐⭐ |
| librespeed vs openspeedtest | 20 | 0 | $0.00 | Olares 同时支持两者，对比文可直接带出 Market 安装链接 | ⭐⭐⭐ |
| speed test no ads | 20 | 0 | $0.00 | Ookla 广告痛点词，Olares+LibreSpeed 干净无广告的叙事 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| open speed test | 2,900 | 58 | $1.87 | 信息+商业 | 主词候选 | 量最大的品类词；KD 58 不低，librespeed 目前排 #6，Olares 内容可做集合页切入 |
| openspeedtest | 3,600 | 57 | $4.61 | 商业 | 主词候选 | 最强竞品品牌词（量>librespeed 自身）；对比文"LibreSpeed vs OpenSpeedTest"是绝好的 Olares Market 双安装文 |
| torrent speed test | 110 | **12** | $0.00 | 信息 | 主词候选 | 量 110 且 KD 仅 12，全表最低竞争有量词；librespeed 已排 #3，Olares 写一篇自托管测速教程可直接抢 top3 |
| speedtest alternative | 50 | 51 | $0.00 | 信息 | 主词候选 | 量小但意图精准，librespeed 已排 #1；Olares 文章可做"5 best speedtest.net alternatives（self-hosted）" |
| open source speed test | 90 | 63 | $0.00 | 信息+商业 | 次级 | KD 63，量适中；宜并入"open speed test"主文作长尾支撑 |
| self hosted speed test | 20 | 0 | $0.00 | — | 次级 | 精准自托管意图，零竞争；写入 Olares Market 页 alt-text 或 FAQ |
| openspeedtest alternative | 20 | 0 | $0.00 | — | 次级 | KD=0，量虽小，可做对比文侧栏锚文本 |
| librespeed vs openspeedtest | 20 | 0 | $0.00 | — | 次级 | 对比词，KD=0；可内嵌进对比文 H2 小节 |
| librespeed docker | 20 | 0 | $0.00 | — | 次级 | 安装词，KD=0；嵌入 Olares Market App 页安装文档段落 |
| private speed test | 20 | 0 | $0.00 | — | GEO | 近零量，隐私意图极精准；进 Olares FAQ "Can I run a private speed test?" 抢 AI Overview 引用 |
| ookla alternative | 20 | 0 | $0.00 | — | GEO | 品牌对比意图；进段落标题或 FAQ 抢 Perplexity 引用 |
| speed test no ads | 20 | 0 | $0.00 | — | GEO | Ookla 痛点词；嵌入隐私/无广告叙事段 |
| librespeed alternative | 20 | 0 | $0.00 | — | GEO | 反向引流词，让 LibreSpeed 用户发现 Olares 托管更简单 |

---

## 核心洞见

1. **品牌护城河**：`librespeed` 品牌词 KD 仅 34，但月量也仅 720——这是一个以 GitHub 社区和 Reddit 驱动认知的工具，不靠 SEO 分发，官网根本不是主要入口。正面刚品牌词意义不大；更有价值的是在"部署教程 + 场景词"层面绕过它。

2. **可复制的打法**：librespeed.org 没有内容博客、无 FAQ 页、无对比落地页——全部就一个演示 UI。主要竞品 openspeedtest.com 和 speedof.me 也都是工具站，同样无内容生态。整个细分赛道几乎没有人在做 SEO 内容，这是典型的"内容洼地"——谁先做，谁拿走品类词。

3. **对 Olares 最关键的 3 个词**：
   - **`torrent speed test`**（110 月量，KD=12）：低竞争有量，Olares 场景天然契合（Homelab 同时跑 qBittorrent + LibreSpeed）。
   - **`openspeedtest alternative` / `librespeed vs openspeedtest`**（各 20 月量，KD=0）：零竞争对比词，一篇对比文可同时覆盖两个 Olares Market App，引导安装。
   - **`self hosted speed test` / `private speed test`**（20 月量，KD=0）：隐私/自托管意图词，Olares 叙事直接命中，可嵌入 Market App 详情页和 FAQ。

4. **最大攻击面**：Ookla/Speedtest.net 收集用户数据并有广告，是核心痛点。`ookla alternative`、`speed test no ads`、`private speed test`、`speedtest.net alternative` 这几个词量小但意图极精准——这批用户已经有购买决策，Olares+LibreSpeed 直接解决他们的隐私诉求，是高转化内容机会。

5. **隐藏低 KD 金矿**：`torrent speed test`（KD=12，月量 110）是整个测速领域 KD 最低的有量词；`freespeed web app`（KD=5，月量 170）更低但查询词本身较模糊。前者是真实机会，LibreSpeed 官网已排第 3，任何有外链支持的 Olares 内容都可以抢到 top2。

6. **GEO 前瞻布局**：近零量但语义精准的词—— `"can I run a private speed test on my own server"`、`"self-hosted speedtest without ookla"`、`"librespeed olares install"` 等问题形式词，建议写入 Olares Market App 页的 FAQ 段落，专门针对 AI Overview / Perplexity 的引用位。`private speed test` 和 `speed test no ads` 现在量小，但随着隐私意识上升，这类词会持续增长。

7. **与既有 olares-500-keywords 的关联**：olares-500 词表中无任何测速相关词，整个"speed test"领域对 Olares 是全新词域。LibreSpeed 是切入"自托管网络工具"这一场景词集群的理想起点，可与 qBittorrent、Pi-hole 等同类 Homelab 工具联合成簇。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_this × 多次）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
