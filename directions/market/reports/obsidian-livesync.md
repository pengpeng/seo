# Obsidian LiveSync SEO 竞品分析报告

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> Self-hosted LiveSync 是 Obsidian 社区同步插件第一选择：MIT 开源，以自建 CouchDB / S3 对象存储为后端，支持端对端加密与跨平台实时同步。

---

## 项目理解（前置）

Self-hosted LiveSync（GitHub: `vrtmrz/obsidian-livesync`）是一款 Obsidian 社区开源插件，让用户完全绕过 Obsidian 官方 $8/月订阅，改用自建 CouchDB 或 Cloudflare R2、MinIO、AWS S3 等对象存储来同步笔记库（vault）。插件支持冲突自动合并、端对端加密（E2EE）、设置/主题/插件同步，以及 2026 年新增的 WebRTC P2P 同步（实验性）。目标用户是对数据隐私或成本敏感的开发者、研究员和重度笔记用户——"把云同步服务器装进自己家"是其核心卖点。**注意：Obsidian 本体是商业闭源软件，LiveSync 是社区插件，无独立官网，SEMrush 无法做域名流量基线，本报告走降级模式——跳过 Phase 1，直接从关键词层分析。**

| 项目 | 内容 |
|------|------|
| 一句话定位 | Obsidian 笔记的开源自托管实时同步插件（CouchDB / S3 后端） |
| 开源 / 许可证 | 是，MIT License |
| 主仓库 | [github.com/vrtmrz/obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync)（★ 11.4k） |
| 核心功能 | 实时同步（CouchDB 或 S3/R2/MinIO）、E2EE 加密、冲突合并、设置/插件同步、WebRTC P2P（实验） |
| 商业模式 / 定价 | 完全免费（MIT 开源）；后端成本由用户自担（fly.io 免费层 / Cloudflare R2 免费层可覆盖大多数场景） |
| 差异化 / 价值主张 | 零月费替代 Obsidian Sync（$8/月）；完全自托管，数据不过第三方；E2EE 加密；支持所有 Obsidian 平台 |
| 主要竞品（初判） | Obsidian Sync（官方付费）、Remotely Save（S3/WebDAV 另一开源插件）、Syncthing + Obsidian、Git 同步（obsidian-git） |
| Olares Market | ⬜ 未上架（CouchDB 可作为 Olares Market 的支撑后端） |
| 来源 | [GitHub README](https://github.com/vrtmrz/obsidian-livesync/blob/main/README.md)（2026-07-06 核实） |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| remotely save vs livesync | 320 | 18 | $0 | 信息+转化 | ⭐ **SERP 弱（Reddit/个人博客）；最高价值词** |
| logseq vs obsidian | 590 | 28 | $0 | 商业 | ⭐ 上游品类词，Olares 可切 |
| joplin vs obsidian | 480 | 18 | $0 | 商业 | ⭐ 同上，Joplin 可自托管 |
| obsidian alternative | 590 | 16 | $5.26 | 转化 | ⭐ KD 极低；有 CPC 说明转化意图存在 |
| obsidian sync alternative | 10 | 0 | $0.33 | 商业 | ⭐ 量小但意图精准，直达 LiveSync 用户 |
| obsidian sync alternatives | 20 | 0 | $0 | 信息 | ⭐ 同上变体 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| obsidian sync | 4,400 | 39 | $0 | 导航 | 量最大，但导航意图（找官方 Sync），KD 偏高；可做次级 |
| obsidian third party sync | 480 | 25 | $0 | 信息 | ⭐ 清晰场景词，意图明确找 LiveSync 类方案 |
| obsidian sync price | 590 | 37 | $0 | 导航+商业 | 定价痛点，KD 高；切入"免费替代"叙事 |
| obsidian sync pricing | 390 | 38 | $0 | 导航+商业 | 同上 |
| obsidian sync free | 320 | 31 | $0 | 信息 | 痛点清晰，竞争稍高；但题目好写 |
| obsidian sync cost | 170 | 37 | $0 | 商业 | 同"定价痛点"族 |
| obsidian icloud sync | 170 | 28 | $0 | 导航+商业 | ⭐ 具体平台词；可进 FAQ |
| obsidian live sync | 140 | 14 | $0 | 信息 | ⭐ 品牌变体，KD 超低 |
| is obsidian sync worth it | 110 | 24 | $0 | 信息+商业 | ⭐ 问题型痛点词，引导到自托管对比 |
| obsidian sync plugin | 90 | 18 | $0 | 信息 | ⭐ 直指 LiveSync 所在品类 |
| obsidian sync plugins | 50 | 15 | $0 | 信息 | ⭐ 复数变体，内容合并 |
| sync obsidian | 90 | 29 | $0 | 导航 | 偏导航，次级 |

### 产品 / 功能词（插件品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| obsidian livesync | 260 | 10 | $0 | 信息 | ⭐ 核心品牌词，KD 极低；GitHub 排第一，但博客可抢位 |
| obsidian remotely save | 110 | 8 | $0 | 信息+商业 | ⭐⭐ **KD 最低竞品词**；与 LiveSync 对比文的副词 |
| obsidian-livesync | 50 | 14 | $0 | 信息 | ⭐ 连字符变体 |
| obsidian livesync plugin | 40 | 0 | $0 | 信息 | ⭐ 量小但意图精准 |
| obsidian livesync docker | 20 | 0 | $0 | 信息 | ⭐ 技术实操词，博客教程机会 |
| obsidian livesync ios | 20 | 0 | $0 | 信息 | ⭐ 移动端具体场景 |
| obsidian sync self hosted | 40 | 24 | $0 | 信息 | ⭐ 精准场景词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| obsidian self hosted sync | 70 | 22 | $0 | 信息 | ⭐ 任务给出的核心词；直接 Olares 机会 |
| self hosted obsidian sync | 50 | 0 | $0 | 信息 | ⭐ 近同义变体 |
| obsidian self hosted | 390 | 33 | $0 | 信息 | 量可观，KD 略高，Olares 角度可切 |
| self hosted notes | 40 | 13 | $0 | 信息 | ⭐ 更宽泛的品类词 |
| self hosted note taking | 20 | 0 | $0 | 信息 | ⭐ 量小但纯自托管意图 |

### 中文关键词（Chinese-language Signals）

> Obsidian 在中文用户群有极高渗透率；LiveSync 仓库有官方中文文档（README_cn.md），中文词 KD 普遍极低，是强机会区。

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| obsidian同步 | 720 | 15 | $0 | 信息 | ⭐ US 库中最大中文词，KD 极低 |
| obsidian 同步 | 390 | 16 | $0 | 信息 | ⭐ 带空格变体 |
| obsidian 同步方案 | 390 | 11 | $0 | 信息 | ⭐⭐ **KD 11，量 390，中文词最优先** |
| obsidian livesync 教程 | 20 | 0 | $0 | 信息 | ⭐ 中文教程词，长尾但意图极精准 |

### 问题词（信息意图内容选题）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| can i sync obsidian with google drive | 590 | 24 | $0 | 信息 | ⭐ 高流量问题词；切入点：还有更好的自托管方法 |
| how to sync obsidian for free | 140 | 31 | $0 | 信息 | 痛点型，题目直接 |
| is obsidian sync free | 140 | 34 | $0 | 信息 | 与上族合并 |
| how much is obsidian sync | 110 | 32 | $0 | 信息 | 定价痛点族 |
| is obsidian sync worth it | 110 | 24 | $0 | 信息+商业 | ⭐ 可写对比文，结论 = 用 LiveSync |
| how to sync obsidian | 90 | 19 | $0 | 信息 | ⭐ 通用教程词 |
| how to sync obsidian across devices | 50 | 31 | $0 | 信息 | 具体场景 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Olares 作为自托管 OS，可以一键部署 CouchDB（LiveSync 官方推荐后端），让非技术用户以极低门槛实现零月费的私有 Obsidian 同步。叙事切入点 = 开箱即用的 CouchDB 后端 + 数据永远在自己的机器上。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| remotely save vs livesync | 320 | 18 | $0 | 对比文："两个插件谁更适合你——以及如何用 Olares 一键跑 CouchDB 后端让 LiveSync 零配置就位" | ⭐⭐⭐ |
| obsidian self hosted sync | 70 | 22 | $0 | 主攻词：Olares Market 部署 CouchDB，LiveSync 插件指向 Olares 内网地址——30 分钟搭建私有同步 | ⭐⭐⭐ |
| obsidian同步 / obsidian 同步方案 | 720/390 | 15/11 | $0 | 中文教程：「Obsidian 多设备同步方案横评——官方 Sync vs Git vs LiveSync（搭配 Olares 自建）」 | ⭐⭐⭐ |
| obsidian livesync | 260 | 10 | $0 | 产品词：Olares 官方教程「在 Olares 上运行 CouchDB + Obsidian LiveSync 完全指南」 | ⭐⭐⭐ |
| obsidian third party sync | 480 | 25 | $0 | 品类对比：Olares 作为自托管 OS 给 3 种第三方同步方案都提供了后端支持 | ⭐⭐ |
| obsidian sync free | 320 | 31 | $0 | 切入口：Obsidian 免费同步终极指南，LiveSync + Olares CouchDB 等于真·零月费 | ⭐⭐ |
| obsidian sync plugin | 90 | 18 | $0 | 内容：「Obsidian 同步插件横评：LiveSync / Remotely Save / Git + 自托管搭建建议（Olares）」 | ⭐⭐ |
| obsidian alternative | 590 | 16 | $5.26 | 上游词：Olares 同时支持部署 Joplin / AppFlowy / AnyType 等 Obsidian 替代品，可做品类页 | ⭐⭐ |
| can i sync obsidian with google drive | 590 | 24 | $0 | FAQ 切入：Google Drive 方案的限制 → LiveSync + Olares 自建为何更可靠 | ⭐⭐ |
| is obsidian sync worth it | 110 | 24 | $0 | 对比文收尾：结论 = 官方 Sync 如果你需要跨设备，但 LiveSync + Olares = 一次性成本、数据自控 | ⭐⭐ |
| obsidian self hosted | 390 | 33 | $0 | 宽泛词：Olares 提供了完整的 Obsidian 自托管生态（CouchDB 后端 + Obsidian 本体 Desktop 如有） | ⭐ |
| obsidian livesync docker | 20 | 0 | $0 | 技术词：Olares 容器环境即 Docker，教程可直接复用 docker-compose 示例 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| remotely save vs livesync | 320 | 18 | $0 | 信息+转化 | **主词候选** | SERP 极弱（Reddit + 无名博客）；量×KD 最优比；Olares 切入：作为 CouchDB 后端方写完全性对比文 |
| obsidian同步 | 720 | 15 | $0 | 信息 | **主词候选** | US 库中文词最大，KD 15；与 `obsidian 同步方案` 合并成中文簇可达 1,500/mo；Olares 中文教程首选锚点 |
| obsidian livesync | 260 | 10 | $0 | 信息 | **主词候选** | 品牌词 KD 10，GitHub 排 #1 但博客可抢 #2-4；Olares 教程可抢位 |
| obsidian 同步方案 | 390 | 11 | $0 | 信息 | **主词候选** | KD 11，量可观；中文簇主词，Olares 叙事：让 LiveSync 的后端配置降到"点击安装"级 |
| obsidian self hosted sync | 70 | 22 | $0 | 信息 | **主词候选** | 与 `self hosted obsidian sync`(50) + `obsidian sync self hosted`(40) 合计 ~160/mo；直接 Olares 机会词 |
| obsidian third party sync | 480 | 25 | $0 | 信息 | **主词候选** | 量大，KD 25 可攻；Olares 叙事：支持三类第三方同步后端（CouchDB / S3 / P2P） |
| obsidian sync free | 320 | 31 | $0 | 信息 | 次级 | KD 31 偏高但量大；归入"obsidian sync 免费方案"簇；Olares 切入零月费叙事 |
| obsidian remotely save | 110 | 8 | $0 | 信息+商业 | 次级 | KD 8 超低；并入 remotely save vs livesync 对比文的次级词 |
| obsidian sync plugin | 90 | 18 | $0 | 信息 | 次级 | KD 18，与 `obsidian sync plugins`(50) 合并；横评文的锚点词 |
| obsidian live sync | 140 | 14 | $0 | 信息 | 次级 | 品牌变体，收进 `obsidian livesync` 簇，KD 低 |
| obsidian alternative | 590 | 16 | $5.26 | 转化 | 次级 | KD 16 + CPC $5 说明真实转化意图；可并入 Obsidian 替代品综述文（Olares Market 品类页） |
| can i sync obsidian with google drive | 590 | 24 | $0 | 信息 | 次级 | 高量问题词，KD 24；作为 FAQ 收进"obsidian sync 免费方案"文章 |
| obsidian livesync docker | 20 | 0 | $0 | 信息 | 次级 | 量小但意图极精准；归入教程文 |
| obsidian livesync ios | 20 | 0 | $0 | 信息 | 次级 | 移动端场景，教程文 FAQ 节 |
| obsidian livesync 教程 | 20 | 0 | $0 | 信息 | 次级 | 中文教程词，并入中文簇 |
| obsidian livesync alternative | 0 | 0 | $0 | — | **GEO** | 近零量，但 AI 问答高频；抢 AI Overview 引用位 |
| obsidian couchdb sync | 0 | 0 | $0 | — | **GEO** | 技术精准，适合 FAQ 段 |
| obsidian livesync e2ee | 0 | 0 | $0 | — | **GEO** | 安全意识强的用户问 AI；进"为什么选 LiveSync"段 |
| self hosted obsidian couchdb | 0 | 0 | $0 | — | **GEO** | Olares + CouchDB 配置精准语义词 |
| obsidian p2p sync | 0 | 0 | $0 | — | **GEO** | WebRTC P2P 新功能（2026），抢前瞻 AI 引用 |

---

## 核心洞见

1. **品牌护城河**：LiveSync 本身无官网，GitHub 仓库是唯一"权威页"——它只能在 `obsidian livesync`（KD 10）这类品牌词上排 #1；所有教程型、对比型、问题型词都没有品牌防护，任何外部博客/教程站都可以正面竞争。**没有护城河，是正面的**。

2. **可复制的打法**：SERP 分析显示，`remotely save vs livesync` 这个 320/mo、KD 18 的词，当前排名页是 Reddit 帖子、小博客、个人 gist——这类词天生适合一篇"横评对比 + 配置指南"文章拿走前 3 名。同理，`obsidian livesync docker`、`obsidian livesync ios` 等长尾词都是"教程内容带流量"的标准打法，零付费门槛，竞品几乎为零。

3. **对 Olares 最关键的 3 个词**：
   - `remotely save vs livesync`（320/mo，KD 18）——直接建立"Olares = LiveSync 最佳后端"的叙事锚点；
   - `obsidian self hosted sync`（族合计 ~160/mo，KD 22）——Olares Market 部署 CouchDB 的最精准流量入口；
   - `obsidian同步` / `obsidian 同步方案`（族合计 ~1,500/mo，KD 11-16）——中文市场，KD 极低，Olares 品牌在中文社区的天然进入点。

4. **最大攻击面**：定价痛点族（`obsidian sync price` 590 + `obsidian sync pricing` 390 + `obsidian sync cost` 170 = 月均 1,150 次搜索）全部是在质疑 Obsidian 官方 Sync $8/月值不值——LiveSync + Olares CouchDB 后端 = 真·零月费，是可以直接用在文章 H1 里的对比叙事。

5. **隐藏低 KD 金矿**：`obsidian 同步方案`（KD 11，390/mo）+ `obsidian同步`（KD 15，720/mo）——这是 US Semrush 数据库里极罕见的"量大 + KD 超低"中文词组合，说明中文内容在这个品类里严重匮乏，先到先得。另一个金矿：`obsidian remotely save`（KD 8，110/mo）是 LiveSync 最直接竞品词，KD 跌至 8 意味着几乎没人在争。

6. **GEO 前瞻布局**：五个近零量词值得直接写进文章的 FAQ/技术段落：`obsidian livesync alternative`、`obsidian couchdb sync`、`obsidian livesync e2ee`、`self hosted obsidian couchdb`、`obsidian p2p sync`——这些是 Perplexity/ChatGPT 被问到 Obsidian 同步时会引用的精准短语，现在进 FAQ 段可以提前抢引用位。

7. **与既有分析的关联**：[olares-500-keywords-analysis-2026-07-03.md](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md) 已将 `obsidian self hosted sync`（70/mo）和 `obsidian alternative`（590/mo，KD 16）标为 A 类词并建议承接方为 AppFlowy 和 Olares Drive。本报告补充：LiveSync 是一个更精准的切入点——它直接告诉用户"在 Olares 上跑 CouchDB = 你永久免费的 Obsidian 同步后端"，把 Olares 的"个人云 OS"定位具象化为一个可立即使用的用例，而不是抽象叙事。

---

*数据来源：SEMrush US 数据库（`phrase_these`、`phrase_fullsearch`、`phrase_related`、`phrase_questions`、`phrase_organic`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。中文词在 US 数据库可见说明该词群有相当数量的海外中文用户。*
*项目理解来源：[github.com/vrtmrz/obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) README（2026-07-06 核实）。*
