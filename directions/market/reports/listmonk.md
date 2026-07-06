# Listmonk SEO 竞品分析报告

> 域名：listmonk.app | SEMrush US | 2026-07-06
> 开源自托管 Newsletter 与邮件列表管理器的事实标准——单二进制、高吞吐、现代 Dashboard。

---

## 项目理解（前置）

Listmonk 是一款以"单一二进制"为卖点的高性能自托管 Newsletter 与邮件列表管理系统，面向开发者和技术型团队。它提供订阅者管理（支持 SQL 段筛）、多 SMTP 多线程发送队列、内置分析、可视化邮件编辑器、事务邮件 API，以及通过 Webhook 扩展到 SMS/WhatsApp 等渠道的 Messenger 接口。项目完全免费开源，无托管付费版，差异化在于极低的资源占用（单核 CPU 碎片 + 57MB RAM 可发送 700 万封邮件）和无 vendor lock-in。与 Mailchimp / Brevo 这类 SaaS 竞品相比，Listmonk 是"自己掌控数据与成本"的代表产品，也是 Olares Market 中 Email Marketing 类的核心应用。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 自托管、高性能 Newsletter + 邮件列表管理器，单二进制，免费开源 |
| 开源 / 许可证 | 是，AGPL-3.0 |
| 主仓库 | https://github.com/knadh/listmonk（★ ~22K） |
| 核心功能 | 百万级订阅者管理（SQL 段）、多 SMTP 队列、内置分析、事务邮件 API、可视化拖拽编辑器 |
| 商业模式 / 定价 | 完全免费，无 SaaS 版；自行部署 + 自备 SMTP |
| 差异化 / 价值主张 | 极低资源占用、完全数据自有、0 订阅费用、无发送量上限 |
| 主要竞品（初判）| Mautic、Sendy、PHPList、EmailOctopus（SaaS）、Mailchimp（SaaS） |
| Olares Market | 已上架（⬜→本报告后标记 ✅） |
| 来源 | https://listmonk.app · https://github.com/knadh/listmonk |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | listmonk.app |
| SEMrush Rank | 1,377,281 |
| 自然关键词数 | 254 |
| 月自然流量（US）| 668 |
| 自然流量估值 | $5,624 / 月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 11 词 |
| 排名 4-10 位 | 63 词 |
| 排名 11-20 位 | 53 词 |

> 流量规模偏小，但估值/流量比极高（$8.4/visit），说明命中了高 CPC 的 Email Marketing 商业意图词，且无付费投放，全靠自然排名。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| listmonk.app | 254 | 668 | 100% |

全部流量集中在主域名，无文档子域名、无博客子站——这是内容机会：竞品如 mautic.org 通过内容站点带动了数倍流量。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| listmonk | 1 | 590 | 33 | $8.88 | 472 | 品牌 | listmonk.app/ |
| open source newsletter | 2 | 260 | 45 | $2.39 | 34 | 信息 | listmonk.app/ |
| opennewsletter | 3 | 170 | 39 | $0.65 | 13 | 品牌变体 | listmonk.app/ |
| email list builder | 7 | 390 | 39 | $16.15 | 8 | 信息 | listmonk.app/ |
| open source mailing list software | 1 | 30 | 38 | $2.99 | 7 | 信息 | listmonk.app/ |
| self hosted email marketing software | 5 | 140 | 39 | $11.76 | 6 | 信息 | listmonk.app/ |
| email list manager | 5 | 210 | 24 | $12.89 | 6 | 信息 | listmonk.app/ |
| free newsletter applications | 6 | 260 | 38 | $1.64 | 6 | 信息 | listmonk.app/ |
| newsletter server | 2 | 70 | 56 | $0 | 5 | 信息 | listmonk.app/ |
| mailing list software | 4 | 260 | 63 | $11.63 | 5 | 信息 | listmonk.app/ |
| self hosted email marketing platform | 4 | 70 | 8 | $0 | 4 | 信息 | listmonk.app/ |
| list manager | 5 | 170 | 13 | $21.67 | 4 | 信息 | listmonk.app/ |
| open source email | 6 | 170 | 74 | $1.10 | 4 | 信息 | listmonk.app/ |
| mailing list manager | 2 | 40 | 51 | $9.57 | 3 | 信息 | listmonk.app/ |
| monk mail | 5 | 140 | 41 | $9.05 | 3 | 导航 | listmonk.app/ |
| mailing list management software | 6 | 140 | 52 | $14.22 | 3 | 信息/商业 | listmonk.app/ |
| email marketing open source | 3 | 30 | 22 | $8.23 | 2 | 信息 | listmonk.app/ |
| open source email marketing software | 4 | 70 | 38 | $5.33 | 2 | 信息/商业 | listmonk.app/ |
| mailmint | 22 | 1,600 | 21 | $1.30 | 2 | 品牌（竞品） | listmonk.app/ |
| bulk email software open source | 4 | 50 | 45 | $0 | 2 | 信息 | listmonk.app/ |
| free mailing list | 9 | 390 | 70 | $7.87 | 2 | 信息 | listmonk.app/ |

> 品牌词"listmonk"（月量 590，KD 33）贡献全站约 70% 流量，非品牌词集体流量薄弱——官网无内容营销，所有页面均为产品落地页。"mailmint"排名 22、贡献 2 条流量，是流量意外溢出竞品。

### 付费词（Google Ads）

无付费投放，Listmonk 官方 0 预算。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| mailchimp alternatives | 2,400 | 39 | $24.04 | 信息 | 最大替代词，KD 39 仍可争 |
| mailerlite alternatives | 480 | 27 | $13.25 | 信息 | ⭐ KD<30，量 480 |
| mailerlite alternative | 480 | 24 | $13.25 | 信息/商业 | ⭐ 同族，商业意图更强 |
| convertkit alternative | 140 | 24 | $14.50 | 商业 | ⭐ Kit 已改名，混淆搜索量可能更高 |
| best mailchimp alternatives | 170 | 18 | $28.42 | 商业 | ⭐ 低 KD + 高 CPC + 商业意图，黄金位 |
| alternatives to mailchimp | 480 | 35 | $20.43 | 信息 | 意图略弱于 best 变体 |
| mailchimp alternative free | 30 | 0 | $8.63 | 信息 | ⭐ 近零 KD |
| brevo alternative | 40 | 13 | $20.79 | 信息/商业 | ⭐ Brevo 涨价痛点词 |
| sendy alternative | 40 | 2 | $11.26 | 信息 | ⭐ 直接品类竞品替代词 |
| listmonk alternative | 20 | 0 | $9.51 | 信息 | ⭐ 自身替代词，意在"找类似工具" |
| phplist alternative | 20 | 0 | $0 | 信息 | ⭐ 老牌竞品替代词 |
| mautic alternative | 20 | 0 | $0 | 信息 | ⭐ 开源竞品替代词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| newsletter software | 1,600 | 58 | $10.08 | 信息 | 核心品类词，KD 偏高 |
| newsletter platforms | 1,600 | 36 | $12.43 | 信息 | ⭐ 同量但 KD 更友好 |
| bulk email software | 1,600 | 40 | $23.54 | 信息 | 高 CPC，可做 |
| email list management | 1,000 | 23 | $14.20 | 信息/商业 | ⭐ 低 KD，高 CPC，量大 |
| mailing list management | 90 | 37 | $17.74 | 信息/商业 | 中量，高 CPC |
| email list builder | 390 | 39 | $16.15 | 信息 | 已在 P4 排名 7 |
| mailing list software | 260 | 63 | $11.63 | 信息 | KD 过高 |
| newsletter platform | 320 | 44 | $8.75 | 信息 | 中 KD |
| phplist | 320 | 46 | $4.94 | 品牌/信息 | 老竞品仍有稳定搜索 |
| open source newsletter | 260 | 45 | $2.39 | 信息 | 官网已排名 2 |
| free mailing list | 390 | 70 | $7.87 | 信息 | KD 过高 |
| email marketing newsletters | 320 | 28 | $18.54 | 信息/商业 | ⭐ KD<30，高 CPC |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| listmonk | 590 | 33 | $8.88 | 品牌 | 主词，官网排名 1 |
| listmonk docker | 20 | 0 | $0 | 信息 | ⭐ 安装向导长尾 |
| listmonk install | 20 | 0 | $0 | 信息 | ⭐ |
| listmonk smtp | 20 | 0 | $0 | 信息 | ⭐ |
| listmonk api | 20 | 0 | $0 | 信息 | ⭐ |
| listmonk templates | 20 | 0 | $0 | 信息 | ⭐ |
| listmonk review | 20 | 0 | $0 | 商业 | ⭐ 评测词，易排名 |
| listmonk alternative | 20 | 0 | $9.51 | 信息 | ⭐ 见替代词组 |
| listmonk github | 50 | 30 | $0 | 导航 | 官网排名 2 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| email list management | 1,000 | 23 | $14.20 | 信息/商业 | ⭐ 最大自托管机会词 |
| self-hosted email marketing platform | 70 | 8 | $0 | 信息 | ⭐ KD 仅 8，最低竞争 |
| self hosted email marketing software | 140 | 39 | $11.76 | 信息 | 官网已排 5，可巩固 |
| open source mailing list software | 30 | 38 | $2.99 | 信息 | 官网已排 1 |
| email marketing open source | 30 | 22 | $8.23 | 信息 | ⭐ 低 KD |
| open source email marketing software | 70 | 38 | $5.33 | 信息/商业 | 中 KD |
| bulk email software open source | 50 | 45 | $0 | 信息 | 中 KD |
| self-hosted newsletter software | 20 | 0 | $0 | 信息 | ⭐ 近零 KD |
| self-hosted mailing list | 20 | 0 | $0 | 信息 | ⭐ |
| open source email newsletter | 20 | 0 | $3.96 | 信息 | ⭐ |
| phplist alternative | 20 | 0 | $0 | 信息 | ⭐ 老牌开源竞品替代词 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Listmonk 是"花 $0/月 在自己服务器上跑 Mailchimp 级 Newsletter"的最佳选择，与 Olares 的"数据主权 + 应用生态"叙事天然契合——Olares Market 一键部署 + 自备 SMTP = 真正的 Email 自主权。**

按月量降序。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| mailchimp alternatives | 2,400 | 39 | $24.04 | Olares + Listmonk = 替代 Mailchimp 的完整自托管方案，"停止每月付费，掌控数据" | ⭐⭐⭐ |
| email list management | 1,000 | 23 | $14.20 | Olares Market 一键部署 Listmonk = 数据不离本地、无平台限制的邮件列表管理 | ⭐⭐⭐ |
| best mailchimp alternatives | 170 | 18 | $28.42 | 高商业意图 + 低 KD，Olares 推 Listmonk 切入 "best self-hosted alternative" 定位 | ⭐⭐⭐ |
| mailerlite alternative | 480 | 24 | $13.25 | 同样替代付费 SaaS，MailerLite 用户因涨价/限制流失 | ⭐⭐⭐ |
| convertkit alternative | 140 | 24 | $14.50 | Kit 改名后搜索意图混乱，低 KD + 商业意图可趁 | ⭐⭐ |
| brevo alternative | 40 | 13 | $20.79 | Brevo 涨价用户寻自托管方案，高 CPC 商业意图 | ⭐⭐⭐ |
| sendy alternative | 40 | 2 | $11.26 | Sendy 需 AWS SES 且一次性购买限制多，Listmonk+Olares 更灵活 | ⭐⭐ |
| self-hosted email marketing platform | 70 | 8 | $0 | KD=8 的绝佳 Olares 专属长尾词，"self-hosted = Olares Market" | ⭐⭐⭐ |
| open source newsletter | 260 | 45 | $2.39 | 官网已排 2，Olares 角度写"open source newsletter on your own hardware" | ⭐⭐ |
| email marketing open source | 30 | 22 | $8.23 | 低 KD，Olares 叙事 + 开源邮件营销 | ⭐⭐ |
| self-hosted newsletter software | 20 | 0 | $0 | KD=0，精准信号词，GEO 与 FAQ 抢占 | ⭐⭐⭐ |
| listmonk alternative | 20 | 0 | $9.51 | 寻找"类似 Listmonk 的工具"→ Olares Market 有完整邮件营销应用生态 | ⭐⭐ |
| phplist alternative | 20 | 0 | $0 | 老牌开源用户升级，Listmonk+Olares 现代化替代 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| mailchimp alternatives | 2,400 | 39 | $24.04 | 信息 | 主词候选 | 量最大、CPC 最高的替代词；KD 39 可争，Olares+Listmonk = 自托管替代方案文章的天然锚词 |
| email list management | 1,000 | 23 | $14.20 | 信息/商业 | 主词候选 | KD<30，量千级，CPC 高——最具性价比的 Olares Market 落地页词 |
| newsletter platforms | 1,600 | 36 | $12.43 | 信息 | 主词候选 | 与 newsletter software 同量但 KD 更低；品类总览文章可覆盖 |
| mailerlite alternative | 480 | 24 | $13.25 | 信息/商业 | 主词候选 | KD<30 + 量 480 + 商业意图，可独立成文 |
| best mailchimp alternatives | 170 | 18 | $28.42 | 商业 | 主词候选 | KD 仅 18、CPC $28，高商业意图且可排名，Olares 直接植入 |
| convertkit alternative | 140 | 24 | $14.50 | 商业 | 主词候选 | Kit 改名窗口期，KD<30 + 商业意图 |
| brevo alternative | 40 | 13 | $20.79 | 信息/商业 | 主词候选 | KD=13 最低之一，Brevo 涨价引发替代需求 |
| self-hosted email marketing platform | 70 | 8 | $0 | 信息 | 次级 | KD=8 是全批量最低，Olares 专属自托管词，适合嵌入 Listmonk 落地页或对比文 |
| sendy alternative | 40 | 2 | $11.26 | 信息 | 次级 | KD=2，用于"sendy vs listmonk"段落 |
| email marketing open source | 30 | 22 | $8.23 | 信息 | 次级 | ⭐ 低 KD，植入开源邮件营销段落 |
| open source email marketing software | 70 | 38 | $5.33 | 信息/商业 | 次级 | 官网已排 4，加强 |
| self-hosted newsletter software | 20 | 0 | $0 | 信息 | GEO | KD=0，FAQ/AI Overview 占位 |
| listmonk docker | 20 | 0 | $0 | 信息 | GEO | 技术安装词，Olares Market 对比文档中嵌入 |
| listmonk vs mailchimp | 0 | 0 | $0 | 信息 | GEO | 量近零但语义精准，AI Overview 抢首位 |
| listmonk vs sendy | 0 | 0 | $0 | 信息 | GEO | 同上，对比文 FAQ 段落 |

---

## 核心洞见

1. **品牌护城河**：Listmonk 品牌词（590/月，KD 33）已稳持第 1，但非品牌词流量极薄（不足 30%），官网无内容营销。护城河很浅——既不能正面刚，也意味着我们写竞争内容时不会遭遇强壁垒。

2. **可复制的打法**：官网是纯产品落地页，0 博客 / 0 文档 SEO，**内容空白是最大机会**。竞品 mautic.org（907 词 / 2,198 流量）和 simplelists.com（1,779 词 / 2,302 流量）都通过内容页吃到了 Listmonk 命中不了的词。Olares 可用"对比/替代文"快速填补：一篇"best mailchimp alternatives open source"就能捞到 Listmonk 官网永远不会写的词。

3. **对 Olares 最关键的词**：
   - **`email list management`**（1,000/月，KD 23）：量大、KD 低、CPC $14，直接命中 Olares Market 部署场景。
   - **`best mailchimp alternatives`**（170/月，KD 18，CPC $28）：商业意图最强，CPC 最高，KD 最低之一，Olares + Listmonk 组合天然胜出。
   - **`self-hosted email marketing platform`**（70/月，KD 8）：KD 仅 8，Olares 叙事"自托管 = 掌控数据"精准命中。

4. **最大攻击面**：Mailchimp / Brevo / MailerLite 的**涨价与发送量限制**是用户外流的核心驱动——"stop paying $xx/month for email"叙事 + Olares 一键部署 Listmonk = 最强攻击点。CPC $24–$29 的替代词验证了用户付费意愿（广告主愿意烧钱买流量，说明转化率高）。

5. **隐藏低 KD 金矿**：
   - `brevo alternative`（KD 13，CPC $20.79）：量虽只有 40，但 KD 极低 + 高 CPC，嵌入"mailchimp alternative"大文即可无额外成本覆盖。
   - `mailchimp alternative free`（KD 0，月量 30）：几乎零竞争，精准信号词。
   - `sendy alternative` / `phplist alternative` / `mautic alternative`（KD 0–2）：三个开源竞品替代词全部 KD<5，老用户升级市场，适合 GEO 占位。

6. **GEO 前瞻布局**：
   - `listmonk vs mailchimp`、`listmonk vs sendy`（量近零）→ AI 搜索结构化对比首选，Olares 博客 FAQ 段落或文档对比页抢占。
   - `self-hosted newsletter software`（KD 0）→ Perplexity / AI Overview 问答词，嵌入 Olares Market 应用页 meta description。
   - `what is the best free newsletter software`（GEO 意图问句）→ AI Overview 段落植入 Listmonk 作为开源首选。

7. **与既有 olares-500-keywords 的关联**：Email Marketing / Newsletter 是 Olares Market 典型部署场景，与现有"self-hosted productivity"词簇高度互补。`email list management`（KD 23）和`mailerlite alternative`（KD 24）可以直接合并进"self-hosted alternatives"内容簇，与 Documenso（DocuSign 替代）、Formbricks（Qualtrics 替代）等走相同"save money + own your data"叙事轴。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
