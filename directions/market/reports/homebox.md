# HomeBox SEO 竞品分析报告

> 域名：homebox.software | SEMrush US | 2026-07-06
> 自托管家庭物品库存系统，Olares Market 已上架应用；官网流量几乎 100% 来自品牌词，品类词排名弱但 KD 普遍偏低，是 Olares 最直接的内容攻击面之一。

---

## 项目理解（前置）

HomeBox（sysadminsmedia/homebox）是面向家庭用户的自托管物品库存管理系统，定位为"个人的家庭 ERP 库存模块"：跟踪你拥有什么、在哪里、保修到何时、花了多少钱。原始项目由 hay-kot 创建，2024 年 6 月存档后由 sysadminsmedia 团队接手维护，至今已发 39 个版本（最新 v0.26.2，2026-06-14）。核心优势：Go 编写（内存 <50 MB）、SQLite 嵌入、单容器部署、响应式 UI、内置 QR 码生成。对比竞品 Grocy（偏食品/家务 ERP）和 Snipe-IT（企业 IT 资产），HomeBox 专注耐用品追踪，是家庭用户上手最快的自托管方案。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 面向家庭用户的自托管物品库存管理系统 |
| 开源 / 许可证 | 是，AGPL-3.0 |
| 主仓库 | [sysadminsmedia/homebox](https://github.com/sysadminsmedia/homebox)（★ 6.5K，130 位贡献者） |
| 核心功能 | 物品 + 位置层级追踪、QR 码生成扫描、保修 / 文件管理、购买与维护记录、自定义字段、多用户 + OIDC SSO、CSV 导入导出、REST API |
| 商业模式 / 定价 | 完全免费开源；无 SaaS 版；社区维护 |
| 差异化 / 价值主张 | 极低资源占用（<50 MB RAM）、一次部署终身数据自控、比 Grocy 聚焦、比 Snipe-IT 轻量、比 Excel 强搜索+可扩展 |
| 主要竞品（初判）| Grocy（家务 ERP）、Snipe-IT（IT 资产）、HomeZada（SaaS 家庭管理）、电子表格 |
| Olares Market | **已上架** |
| 来源 | [homebox.software](https://homebox.software/en/)、[GitHub](https://github.com/sysadminsmedia/homebox)、[selfhosting.sh/best/home-inventory/](https://selfhosting.sh/best/home-inventory/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | homebox.software |
| SEMrush Rank | 275,248 |
| 自然关键词数 | 112 |
| 月自然流量（US） | 6,068 |
| 自然流量估值 | $6,446 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 18 词 |
| 排名 4-10 位 | 15 词 |
| 排名 11-20 位 | 16 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| homebox.software | 104 | 6,065 | 99.95% |
| demo.homebox.software | 5 | 3 | 0.05% |
| blog.homebox.software | 2 | 0 | 0% |
| status.homebox.software | 1 | 0 | 0% |

> **洞察**：主站承接几乎全部流量；demo 子域名几乎无 SEO 价值；博客域（blog.homebox.software）尚未获得任何流量，是一个未开垦资产。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| homebox | 1 | 2,400 | 46 | $0.96 | 1,920 | 品牌 | / |
| homebox home | 1 | 2,400 | 36 | $0.96 | 1,920 | 品牌 | / |
| box homebox | 1 | 1,600 | 23 | $1.15 | 1,280 | 品牌 | / |
| homeboks（拼写错误） | 1 | 1,300 | 33 | $1.26 | 322 | 品牌 | / |
| home box | 1 | 1,300 | 19 | $1.26 | 171 | 导航 | / |
| hombox（拼写错误） | 1 | 170 | 50 | $1.26 | 136 | 品牌 | / |
| homebix（拼写错误） | 1 | 110 | 69 | $1.15 | 88 | 品牌 | / |
| homebox docker | 1 | 70 | 39 | $0 | 56 | 信息 | / |
| homebox self hosted | 1 | 50 | 34 | $5.63 | 40 | 信息 | / |
| homebos（拼写错误） | 1 | 40 | 59 | $0 | 32 | 品牌 | / |
| homebox default login | 1 | 90 | 8 | $0 | 2 | 信息 | /en/quick-start/ |
| home inventory management software | 2 | 170 | 40 | $2.03 | 13 | 信息 | / |
| self hosted inventory management | 2 | 70 | 25 | $7.12 | 9 | 信息 | / |
| personal inventory management | 2 | 50 | 31 | $0 | 4 | 商业 | / |
| home inventory system | 3 | 70 | 43 | $1.08 | 4 | 信息 | / |
| home asset management | 3 | 30 | 17 | $4.26 | 1 | 商业 | / |
| home inventory management | 2 | 30 | 43 | $1.35 | 2 | 信息 | / |
| home inventory software for pc | 5 | 30 | 20 | $2.51 | 0 | 商业 | / |
| home inventory app | 22 | 1,000 | 25 | $1.95 | 1 | 商业 | / |
| home inventory program | 17 | 140 | 25 | $2.03 | 0 | 商业 | / |
| household inventory program | 10 | 110 | 35 | $2.03 | 0 | 信息 | / |
| open source inventory tracking | 24 | 210 | 23 | $6.76 | 0 | 商业 | / |
| open source inventory tracking software | 26 | 90 | 35 | $7.26 | 0 | 信息 | / |
| homebox github | 3 | 70 | 45 | $0 | 1 | 品牌 | / |

> **流量结构**：约 95%+ 流量来自品牌词（"homebox" 及各种拼写变体）；品类词虽然排名在前 10 内，但因为量小实际带来流量极低。最大的品类机会词"home inventory app"（1000/月）排在第 22 位——是最重要的未兑现流量缺口。

### 付费词（Google Ads）

homebox.software 无任何付费投放，完全依赖自然流量。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| grocy vs homebox | n/a | — | — | 信息 | selfhosting.sh 已有对比页 |
| homebox alternative | ~0 | 0 | — | 信息 | GEO 前哨，近零量 |
| snipe-it alternative | — | — | — | 信息 | 相邻方向，量待查 |
| homezada vs centriq | 50 | 7 | $0 | 信息 | ⭐ 间接竞品对比词 |

> 注："homebox alternative"当前近零量，说明用户心智未到"找替代"阶段；grocy/snipe-it 是对比维度而非竞品替代关系。

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home inventory app | 1,000 | 25 | $1.95 | 商业 | ⭐ 最大机会主词 |
| home inventory | 1,000 | 54 | $1.64 | 信息 | KD 高，主词备选 |
| household inventory | 590 | 54 | $1.71 | 信息 | KD 高，次级 |
| house inventory app | 390 | 15 | $1.95 | 商业 | ⭐⭐⭐ KD 超低黄金词 |
| home inventory applications | 210 | 28 | $1.29 | 商业 | ⭐ |
| open source inventory tracking | 210 | 23 | $6.76 | 商业 | ⭐ 高 CPC 显示商业价值 |
| home management app | 210 | 23 | $1.48 | 商业 | ⭐ 稍宽泛 |
| home inventory software | 170 | 26 | $1.49 | 信息/商业 | ⭐ |
| home inventory management software | 170 | 40 | $2.03 | 信息 | 中 KD |
| home inventory program | 140 | 25 | $2.03 | 商业 | ⭐ |
| household inventory program | 110 | 35 | $2.03 | 信息 | — |
| free home inventory app | 110 | 39 | $1.94 | 商业 | — |
| home inventory apps | 90 | 31 | $1.81 | 商业 | — |
| open source inventory tracking software | 90 | 35 | $7.26 | 信息 | — |
| home inventory programs | 50 | 23 | $2.79 | 信息/商业 | ⭐ |
| home inventory application | 50 | 32 | $1.95 | 信息/商业 | — |
| home asset management | 30 | 17 | $4.26 | 商业 | ⭐ |
| home inventory management | 30 | 43 | $1.35 | 信息 | 高 KD |
| home inventory system | 70 | 43 | $1.08 | 信息 | — |
| ai home inventory app | 30 | 10 | $1.07 | 信息/商业 | ⭐⭐ 新兴词，极低 KD |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| homebox | 2,400 | 46 | $0.96 | 品牌 | 品牌核心 |
| box homebox | 1,600 | 23 | $1.15 | 品牌 | 同品牌变体 |
| homebox docker | 70 | 39 | $0 | 信息 | 部署教程词 |
| homebox self hosted | 50 | 34 | $5.63 | 信息 | 高 CPC，自托管意图强 |
| homebox default login | 90 | 8 | $0 | 信息 | ⭐ KD 极低，快速入门词 |
| homebox github | 70 | 45 | $0 | 品牌 | — |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted inventory management | 70 | 25 | $7.12 | 信息 | ⭐ 高 CPC + 低 KD 双重信号 |
| homebox self hosted | 50 | 34 | $5.63 | 信息 | — |
| open source inventory tracking | 210 | 23 | $6.76 | 商业 | ⭐ |
| open source inventory tracking software | 90 | 35 | $7.26 | 信息 | — |
| self hosted home inventory | ~0 | 0 | — | — | GEO 前哨 |
| open source home inventory | ~0 | 0 | — | — | GEO 前哨 |
| home inventory docker | ~0 | 0 | — | — | GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Olares 是 HomeBox 的"零运维宿主"——用户在 Olares Market 一键安装，省去手动配 Docker + 反向代理 + 备份的所有步骤，且数据完全本地自控，完美契合 HomeBox 用户的自托管诉求。**

| 关键词 | 月量 | KD | CPC | 契合度 | Olares 角度 |
|--------|------|----|----|--------|------------|
| home inventory app | 1,000 | 25 | $1.95 | ⭐⭐⭐ | Olares Market 一键部署，无需 Docker 知识；数据本地 |
| house inventory app | 390 | 15 | $1.95 | ⭐⭐⭐ | 同上，且 KD 极低是内容突破口 |
| open source inventory tracking | 210 | 23 | $6.76 | ⭐⭐⭐ | Olares + HomeBox 双开源，Olares 负责 OS 层，HomeBox 负责应用层 |
| self hosted inventory management | 70 | 25 | $7.12 | ⭐⭐⭐ | 最直接的自托管匹配词，Olares OS 天然自托管背书 |
| home inventory management software | 170 | 40 | $2.03 | ⭐⭐ | 可在对比文中提 Olares Market vs 手动 Docker |
| home inventory software | 170 | 26 | $1.49 | ⭐⭐ | 品类攻击词，次级切入 |
| home inventory program | 140 | 25 | $2.03 | ⭐⭐ | 同上 |
| home asset management | 30 | 17 | $4.26 | ⭐⭐ | KD 超低，Olares + HomeBox 可合覆盖 |
| homebox alternative | ~0 | 0 | — | ⭐ | GEO：Olares Market 内有多种库存工具可选 |
| self hosted home inventory | ~0 | 0 | — | ⭐⭐⭐ | GEO 前哨：高精准意图，进 FAQ 抢 AI Overview 引用位 |
| ai home inventory app | 30 | 10 | $1.07 | ⭐⭐ | Olares Personal Agent 可读取 HomeBox 数据（战略词，当前量小但趋势好） |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| home inventory app | 1,000 | 25 | $1.95 | 商业 | **主词候选** | 量最大的品类词，KD 25 可打；homebox.software 仅第 22 位——Olares 内容有插位空间 |
| house inventory app | 390 | 15 | $1.95 | 商业 | **主词候选** | KD 仅 15，同品类但更口语化；brightharbor 博客列表页排 8 位，说明内容可抢 |
| open source inventory tracking | 210 | 23 | $6.76 | 商业 | **主词候选** | 高 CPC 证明有商业购买意图，KD 23 可打；Olares 双开源叙事契合 |
| home inventory software | 170 | 26 | $1.49 | 信息/商业 | **次级** | KD 26 偏低，并入"home inventory app"文章作 H2 |
| home inventory management software | 170 | 40 | $2.03 | 信息 | **次级** | KD 40 中等，量不大；配套品类文章次级词 |
| home inventory program | 140 | 25 | $2.03 | 商业 | **次级** | 同义变体，量<50 规则豁免，随主词文章自然覆盖 |
| self hosted inventory management | 70 | 25 | $7.12 | 信息 | **次级** | CPC $7.12 是整批词最高，证明搜索方有付费意愿；KD 25 可打，自托管叙事直接匹配 |
| home inventory system | 70 | 43 | $1.08 | 信息 | **次级** | KD 稍高，并入品类文章 |
| home asset management | 30 | 17 | $4.26 | 商业 | **次级** | KD 17 极低，量小但 CPC 高；进品类文章 |
| homebox self hosted | 50 | 34 | $5.63 | 信息 | **次级** | 品牌+自托管意图词，部署教程文的核心词 |
| homebox docker | 70 | 39 | $0 | 信息 | **次级** | 部署词，写 Olares Market vs Docker 教程时的长尾 |
| ai home inventory app | 30 | 10 | $1.07 | 信息/商业 | **次级/GEO** | KD 10 极低，新兴词；Olares Personal Agent 读 HomeBox API 是战略叙事 |
| self hosted home inventory | ~0 | 0 | — | 信息 | **GEO** | 近零量但极高精准，进部署文 FAQ 抢 AI Overview 引用位 |
| open source home inventory | ~0 | 0 | — | 信息 | **GEO** | 同上 |
| homebox alternative | ~0 | 0 | — | 信息 | **GEO** | 对比文尾部 FAQ 抢占，防范竞品 |

---

## 核心洞见

1. **品牌护城河**：homebox.software 的品牌词护城河很稳——所有顶流词（1800+ 流量/月）都是品牌词且排第一位，KD 均在 20-50。正面打品牌词意义不大，也没必要，因为 HomeBox 本身是 Olares Market 的上架应用，Olares 的受众是它的潜在用户。

2. **可复制的打法**：brightharbor.com（一家保险公司）用一篇"最佳家庭库存 App 推荐"博客列表页排进了多个品类词前 10，证明**内容列表文章**在这个品类 KD 低、可快速获排名。selfhosting.sh 的 "best home inventory" 和 "grocy vs homebox" 对比页也通过内容聚合拿到了品类流量。Olares 可复制这个打法。

3. **对 Olares 最关键的词**：
   - `house inventory app`（390/月，KD **15**）——KD 最低、量合理，最快见效的主词
   - `home inventory app`（1,000/月，KD 25）——量最大的品类词，homebox.software 自身只排第 22
   - `self hosted inventory management`（70/月，KD 25，CPC $7.12）——高 CPC 验证商业价值，Olares 自托管叙事直接命中

4. **最大攻击面**：HomeBox 完全没有内容营销（博客几乎无流量），品类词排名普遍在 20+ 位。这个空档完全由 brightharbor、selfhosting.sh、Reddit 等第三方媒体填补——Olares 可以用 HomeBox 为核心的家庭库存内容文章直接竞争这些词，同时带 Olares Market 一键部署的 CTA。

5. **隐藏低 KD 金矿**：
   - `house inventory app`（KD 15，390/月）——接近零摩擦词
   - `home asset management`（KD 17，30/月）——高 CPC + 极低 KD，小而美
   - `ai home inventory app`（KD 10，30/月）——Olares Personal Agent 战略入口词，KD 极低，提前布局
   - `homezada vs centriq`（KD 7，50/月）——竞品对比词，HomeZada 用户是 Olares/HomeBox 的教育对象

6. **GEO 前瞻布局**：以下近零量词进 FAQ / 问答段，抢 AI Overview（Google SGE）/ Perplexity 引用位：
   - "what is the best self-hosted home inventory app"
   - "how to self-host homebox on docker"
   - "open source home inventory management software"
   - "homebox vs grocy for home inventory"
   - Olares 叙事：用 Personal Agent 查询 HomeBox 库存数据（"ask your AI what electronics you own"）

7. **与既有 olares-500-keywords 的关联**：self-hosted 品类词（self-hosted apps、self hosted apps）已是 Olares 核心词矩阵，HomeBox 场景提供了具体的应用层锚点——"self-hosted home inventory"是长尾应用词，可从 Olares 500 词体系向下延伸，丰富应用场景层内容。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_kdi）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
