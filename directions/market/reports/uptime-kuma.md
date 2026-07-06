# Uptime Kuma SEO 竞品分析报告

> 域名：uptime.kuma.pet（官网流量极低，~640 US/月；主分发渠道为 GitHub） | SEMrush US | 2026-07-06
> Uptime Kuma：自托管运维监控工具，Uptime Robot 的开源平替，88K+ GitHub Star，MIT License

---

## 项目理解（前置）

Uptime Kuma 是由 Louis Lam（louislam）于 2021 年创建的开源自托管监控工具，定位为付费 SaaS 工具 Uptime Robot 的自部署平替。它提供对 HTTP/HTTPS、TCP、Ping、DNS、WebSocket、Docker 容器、Steam 服务器等 20+ 协议类型的 20 秒周期监控，支持 90+ 通知渠道（Telegram、Discord、Slack、Email、Pushover 等），内置美观的状态页。v2.0（2025-10 发布）引入 MariaDB 支持，v2.1（2026-02）新增 Globalping 全球探针和域名到期监控。项目以 MIT License 开源，88K+ GitHub Star，是 self-hosted 监控赛道的第一民选方案。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自托管服务监控 + 状态页，Uptime Robot 开源平替 |
| 开源 / 许可证 | ✅ MIT License |
| 主仓库 | https://github.com/louislam/uptime-kuma（★ 88,000+，2026-07） |
| 核心功能 | HTTP/TCP/DNS/Docker 容器监控；多状态页；90+ 通知渠道；20 秒检测间隔；2FA；API |
| 商业模式 / 定价 | 完全免费自托管；无付费计划；维护者靠 GitHub Sponsors |
| 差异化 / 价值主张 | 0 成本替代 Uptime Robot；Fancy 响应式 UI；零订阅费；数据不出主机 |
| 主要竞品（初判）| Uptime Robot（SaaS 收费）、Gatus（Go 自托管）、Beszel（Rust 新兴）、Freshping（SaaS）、Pingdom（SaaS） |
| Olares Market | ✅ 已上架（apps.md 收录） |
| 来源 | GitHub: louislam/uptime-kuma；官网: uptime.kuma.pet；localtonet.com 博客 |

---

## 流量基线（Phase 1）

> 注：uptime.kuma.pet 为极简落地页（仅含一行 Docker 命令），Semrush 将其作为 kuma.pet 根域统计，包含 dockge.kuma.pet（另一工具，Louis Lam 作品）的流量混入。以下数据为 kuma.pet 整域，Uptime Kuma 专属子域流量约占 60-70%。

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | kuma.pet（uptime.kuma.pet 子域） |
| SEMrush Rank | 0（未入 Semrush Top 100M）|
| 自然关键词数 | 53 词 |
| 月自然流量（US）| ~640（含 Dockge 混入） |
| 自然流量估值 | $1,257/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | ~16 词（含 Dockge 相关词） |
| 排名 4-10 位 | ~5 词 |
| 排名 11-20 位 | ~9 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 说明 |
|--------|---------|------|------|
| uptime.kuma.pet | ~30 词 | ~500/月 | Uptime Kuma 主落地页 |
| dockge.kuma.pet | ~15 词 | ~130/月 | Dockge Docker 管理工具（另一产品） |
| status.kuma.pet | 1 词 | <5/月 | 项目状态页 |

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| dockge | 2 | 4,400 | 37 | $1.09 | 580 | 信息 | dockge.kuma.pet |
| uptime kuma | 3 | 3,600 | 54 | $3.97 | 295 | 导航/信息 | uptime.kuma.pet |
| uptime kuma docker | 3 | 2,400 | 30 | $0 | 105 | 信息 | uptime.kuma.pet |
| kuma uptime | 1 | 210 | 33 | $0 | 52 | 信息 | uptime.kuma.pet |
| uptime-kuma | 3 | 2,900 | 62 | $0 | 40 | 导航 | uptime.kuma.pet |
| dockage | 3 | 590 | 55 | $0 | 38 | 信息 | dockge.kuma.pet |
| uptime kuma logo | 3 | 260 | 7 | $0 | 21 | 信息 | uptime.kuma.pet |
| uptime karma | 1 | 50 | 59 | $3.81 | 12 | 导航 | uptime.kuma.pet |
| uptimekuma | 4 | 1,600 | 53 | $3.81 | 11 | 信息 | uptime.kuma.pet |
| louislam/uptime-kuma | 4 | 320 | 57 | $0 | 9 | 导航 | uptime.kuma.pet |
| install dockge | 2 | 70 | 32 | $3.92 | 9 | 信息 | dockge.kuma.pet |
| uptime kuma github | 2 | 260 | 51 | $0 | 6 | 导航 | uptime.kuma.pet |
| uptime kuma docker compose | 10 | 720 | 42 | $0 | 2 | 信息 | uptime.kuma.pet |
| uptime-kuma api | 14 | 320 | 22 | $0 | 1 | 信息 | uptime.kuma.pet |
| app uptime | 6 | 110 | 32 | $0 | 1 | 信息 | uptime.kuma.pet |

### 付费词（Google Ads）

无付费投放。kuma.pet 付费关键词数 = 0，印证开源项目无 SEM 预算的典型形态。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| uptime robot alternative | 140 | 9 | $11.54 | 信息/商业 | ⭐ **本报告最核心词**；CPC $11 说明高商业意图 |
| uptime robot alternatives | 140 | 11 | $11.54 | 信息/商业 | ⭐ 与上词几乎共用 SERP |
| alternatives to uptime robot | 30 | 0 | $16.14 | 信息 | ⭐ 长尾变体；CPC 最高 |
| alternative to uptime robot | 20 | 0 | $13.27 | 信息 | ⭐ 单数变体 |
| uptime robot alternative free | 20 | 0 | $5.71 | 信息 | ⭐ |
| uptime robot alternative self hosted | 20 | 0 | $0 | 信息 | ⭐ 意图最精准 |
| uptime robot alternative reddit | 20 | 0 | $0 | 信息 | Reddit 信号 |
| uptime robot open source alternative | 20 | 0 | $0 | 信息 | ⭐ |
| free alternative to uptime robot | 20 | 0 | $0 | 信息 | ⭐ |
| uptime kuma vs uptime robot | 0 | 0 | $0 | 信息 | GEO 前哨（对比类内容） |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| uptime monitoring | 1,600 | 76 | $18.28 | 信息 | KD 过高，不宜主攻 |
| uptime monitor | 880 | 71 | $18.28 | 商业 | KD 过高 |
| website uptime monitoring | 880 | 71 | $11.63 | 信息 | KD 过高 |
| free uptime monitoring | 590 | 63 | $6.39 | 商业 | KD 中等偏高 |
| open source monitoring | 210 | 39 | $6.72 | 信息 | ⭐ 相对可攻 |
| server uptime monitor | 170 | 68 | $13.26 | 信息 | KD 高 |
| uptime monitoring software free | 170 | 63 | $6.69 | 商业 | KD 高 |
| downtime monitoring | 140 | 85 | $6.56 | 信息 | KD 极高 |
| free uptime monitoring tool | 140 | 64 | $5.98 | 商业 | KD 高 |
| self hosted monitoring tool | 70 | 30 | $4.16 | 信息 | ⭐ |
| self hosted monitoring | 20 | 0 | $8.16 | 信息 | ⭐ |
| gatus monitoring | 20 | 0 | $8.92 | 信息 | ⭐ 竞品词，KD=0 |
| statuspage self hosted | 10 | 0 | $5.33 | 信息 | ⭐ |
| self hosted status page | 20 | 0 | $5.79 | 信息 | ⭐ |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| uptime kuma | 3,600 | 54 | $3.97 | 导航/信息 | 品牌主词；KD 54，官网排 3 |
| uptime kuma docker | 2,400 | 30 | $0 | 信息 | ⭐ KD 30，安装教程词 |
| uptime-kuma | 2,900 | 62 | $0 | 导航 | 连字符变体；KD 高 |
| uptimekuma | 1,600 | 53 | $3.81 | 信息 | 无空格变体 |
| uptime kuma docker compose | 720 | 42 | $0 | 信息 | 教程词 |
| louislam/uptime-kuma | 320 | 57 | $0 | 导航 | GitHub 路径词 |
| uptime kuma api | 260 | 22 | $0 | 信息 | ⭐ KD 22，开发者词 |
| uptime kuma github | 260 | 51 | $0 | 导航 | |
| uptime kuma logo | 260 | 7 | $0 | 信息 | ⭐ KD=7，设计资源需求 |
| uptime kuma default password | 210 | 9 | $0 | 信息 | ⭐ KD=9，FAQ 型 |
| kuma uptime | 210 | 33 | $0 | 信息 | 词序变体 |
| upptime | 260 | 50 | $1.88 | 信息 | 同类工具（GitHub Pages 监控） |
| autokuma | 70 | 0 | $0.85 | 信息 | ⭐ Kubernetes 自动化集成插件 |
| uptime kuma notification | — | — | — | — | 数据空缺，功能教程潜力词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| uptime robot alternative self hosted | 20 | 0 | $0 | 信息 | ⭐ 意图最精准 |
| uptime robot open source alternative | 20 | 0 | $0 | 信息 | ⭐ |
| self hosted monitoring | 20 | 0 | $8.16 | 信息 | ⭐ |
| self hosted status page | 20 | 0 | $5.79 | 信息 | ⭐ |
| self hosted monitoring tool | 70 | 30 | $4.16 | 信息 | ⭐ |
| open source uptime monitoring | 0 | 0 | $6.31 | 信息 | GEO 前哨 |
| statuspage self hosted | 10 | 0 | $5.33 | 信息 | ⭐ |

---

## Olares 关联词（Phase 3）

**核心逻辑：Uptime Kuma 在 Olares Market 已上架，一键部署即是 Uptime Robot 的零成本平替——走"替代 SaaS 监控订阅 + 数据主权"双轴叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| uptime robot alternative | 140 | 9 | $11.54 | Olares Market 一键装 Uptime Kuma，终身 $0 替代 Uptime Robot；数据不出主机 | ⭐⭐⭐ |
| uptime robot alternatives | 140 | 11 | $11.54 | 同上；文章主词与本词共 SERP | ⭐⭐⭐ |
| uptime robot alternative self hosted | 20 | 0 | $0 | 最精准意图词：Olares 即"自托管一键部署"的答案 | ⭐⭐⭐ |
| self hosted monitoring | 20 | 0 | $8.16 | Olares Market 提供完整 self-hosted 监控生态 | ⭐⭐⭐ |
| self hosted status page | 20 | 0 | $5.79 | Uptime Kuma 状态页 + Olares 自有域名 = 全托管状态页方案 | ⭐⭐⭐ |
| uptime kuma docker | 2,400 | 30 | $0 | Olares 替代 Docker 手工安装；一键部署无需写 compose | ⭐⭐ |
| uptime kuma docker compose | 720 | 42 | $0 | 同上；教程文中可植入 Olares 对比（更简单） | ⭐⭐ |
| self hosted monitoring tool | 70 | 30 | $4.16 | Olares Market 收录多款监控工具，Uptime Kuma 是旗舰 | ⭐⭐ |
| open source monitoring | 210 | 39 | $6.72 | Olares 开源 OS + 开源监控工具，完整数据主权叙事 | ⭐⭐ |
| uptime kuma api | 260 | 22 | $0 | Olares 应用间 API 互通；Agent 可调用监控状态 | ⭐⭐ |
| uptime kuma default password | 210 | 9 | $0 | Olares 统一身份/SSO 消除 Kuma 密码管理痛点（LarePass 集成） | ⭐⭐ |
| autokuma | 70 | 0 | $0.85 | Olares 容器编排层可联动 autokuma 自动创建监控 | ⭐ |
| statuspage self hosted | 10 | 0 | $5.33 | Olares 域名绑定 + Uptime Kuma 状态页 = 完整自托管可观测性 | ⭐⭐ |
| uptime kuma vs uptime robot | 0 | 0 | $0 | GEO 前哨：AI 回答此类对比问题时，Olares 角度 = "两者都能跑，Kuma 免费" | ⭐⭐ |
| gatus monitoring | 20 | 0 | $8.92 | Gatus 也在 Olares 生态备选；可做 Uptime Kuma vs Gatus 对比文 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| uptime robot alternative | 140 | 9 | $11.54 | 信息/商业 | **主词候选** | KD=9 + CPC $11.54 = 本报告最高性价比词；Olares Market 部署 Uptime Kuma 是最直接答案 |
| uptime robot alternatives | 140 | 11 | $11.54 | 信息/商业 | **主词候选** | 与上词共 SERP，合并为同一文章主词簇，US 月量合计 140（全球 ~500+） |
| uptime kuma | 3,600 | 54 | $3.97 | 导航/信息 | 次级 | 品牌主词，KD 54 难正面攻；Olares 内容中可作锚词，不独立成主词 |
| uptime kuma docker | 2,400 | 30 | $0 | 信息 | **主词候选** | KD=30，量大；教程文可植入 Olares 一键部署 vs 手工 Docker 对比 |
| uptime kuma docker compose | 720 | 42 | $0 | 信息 | 次级 | 并入上词教程簇；量 720 补充长尾 |
| open source monitoring | 210 | 39 | $6.72 | 信息 | **主词候选** | KD=39 可进攻，CPC 有商业价值；Olares 开源 OS + 开源监控双叙事 |
| uptime kuma api | 260 | 22 | $0 | 信息 | 次级 | KD=22 低，开发者词；并入技术教程簇 |
| uptime kuma default password | 210 | 9 | $0 | 信息 | 次级 | KD=9 极低；FAQ 型 —— Olares SSO/LarePass 消痛点 |
| self hosted monitoring tool | 70 | 30 | $4.16 | 信息 | 次级 | KD=30 可攻，Olares Market 背书；量偏小单独成文不划算 |
| self hosted monitoring | 20 | 0 | $8.16 | 信息 | 次级 | 量小 KD=0；并入 alternative/monitoring 大簇 |
| self hosted status page | 20 | 0 | $5.79 | 信息 | 次级 | 同上；Uptime Kuma 状态页功能的长尾词 |
| uptime robot alternative self hosted | 20 | 0 | $0 | 信息 | 次级/GEO | 意图最精准；已在 `uptime robot alternative` 主簇内 |
| autokuma | 70 | 0 | $0.85 | 信息 | GEO | Kubernetes 集成词；Olares 容器编排联动场景 |
| uptime kuma vs uptime robot | 0 | 0 | $0 | 信息 | GEO | 零量但语义高相关；AI Overview/Perplexity 必答题，进 FAQ 段抢引用位 |
| open source uptime monitoring | 0 | 0 | $6.31 | 信息 | GEO | CPC 有值但量空；GEO 布局，进文章 FAQ |
| statuspage self hosted | 10 | 0 | $5.33 | 信息 | GEO | 量极小，状态页功能长尾 |

---

## 核心洞见

1. **品牌护城河**："uptime kuma" 系列词 KD 54-62，官网自身只排第 3，护城河反而建在 GitHub 和第三方站点（uptimekuma.org 排第 2 且捕获更多流量）。正面刚品牌词意义不大；价值在于借 alternative/替代词绕过品牌词竞争，直接面向还在用 Uptime Robot 的付费用户。

2. **可复制的打法**：`uptimekuma.org`（第三方粉丝站）靠 3-4 篇高质量教程（Docker 安装、重置密码、Docker Compose）捕获 1,296 US/月，比官网还多。证明"Step-by-step 教程 + 特定功能 FAQ"在这个赛道有效，不需要大品牌背书。

3. **对 Olares 最关键的 3 个词**：
   - `uptime robot alternative`（KD=9, 140/月）——最高性价比，Olares 一键部署即答案
   - `uptime kuma docker`（KD=30, 2,400/月）——量最大可攻词，教程切入
   - `open source monitoring`（KD=39, 210/月）——品类词，CPC $6.72，Olares 开源主权叙事

4. **最大攻击面**：Uptime Robot 有 50 检测数免费计划，但超限收费（$7/月起）、数据在第三方服务器、无自定义状态页定制。痛点词："uptime robot alternative free"、"uptime robot alternative self hosted" ——这两个词 KD=0，CPC 有值，是最干净的攻击切口。

5. **隐藏低 KD 金矿**：`uptime kuma logo`（KD=7）、`uptime kuma default password`（KD=9）、`uptime-kuma api`（KD=22）这三个品牌功能词月量共 ~790，KD 全部 < 25。可用 Olares 文档/FAQ 轻松收割，边际成本极低。

6. **GEO 前瞻布局**：`uptime kuma vs uptime robot`（零量）、`open source uptime monitoring`（零量但 CPC $6.31）、`self hosted status page open source`——这类对比问题是 Perplexity/ChatGPT/AI Overview 的高频引用题型。在文章内嵌 FAQ 段，明确给出 "Uptime Kuma on Olares = best self-hosted answer" 的结构化答案，抢引用位。

7. **与既有 `olares-500-keywords` 分析的关联**：`uptime robot alternative` 词簇是"self-hosted SaaS 替代"大主题的延伸，与 Nextcloud（files）、Bitwarden（密码管理）的 alternative 词策略同构。此词可并入 Olares 的 "Best self-hosted alternatives to SaaS tools" 系列内容矩阵，彼此互链增强权重。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、phrase_these、phrase_related、phrase_fullsearch、phrase_questions、domain_organic_organic）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*项目信息来源：github.com/louislam/uptime-kuma（Stars、License、版本）；localtonet.com/blog/how-to-self-host-uptime-kuma（版本特性）；uptime.kuma.pet（官网验证）。*
