# DeepL SEO 竞品分析报告

> 域名：deepl.com | SEMrush us | 2026-07-06
> DeepL = 神经机器翻译（NMT）领头羊——以"翻译质量优于 Google"著称的 AI 翻译工具 / API，ARR ~$285M、估值 ~$2B。

---

## 项目理解（前置）

DeepL 是德国 DeepL SE（前 Linguee）2017 年推出的 AI 机器翻译服务，长期以"译文更自然、更准确"作为对 Google Translate 的核心差异化。产品线从网页翻译器起步，扩展到文档翻译（DOCX/PDF/PPTX 保留排版）、写作助手 DeepL Write、浏览器插件、桌面/移动客户端，以及面向开发者与企业的 **DeepL API**。商业上主打 Pro 订阅 + API 按量计费，企业侧强调数据不留存、GDPR/ISO 合规。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 高质量神经机器翻译（NMT）SaaS + API，对标并主张"胜过 Google Translate" |
| 开源 / 许可证 | **闭源**（专有模型与服务，无公开权重） |
| 主仓库 | 无开源本体；仅提供 API SDK（`github.com/DeepLcom`，各语言客户端库） |
| 核心功能 | 网页/文档翻译、DeepL Write（写作润色）、REST 翻译 API、浏览器插件、桌面/移动端、术语表(glossary) |
| 商业模式 / 定价 | Free（有月字符限额）；Pro 订阅（个人 ~$8.74/月起）；API Free（50 万字符/月）+ API Pro 按量计费；企业版 |
| 差异化 / 价值主张 | 译文质量与语感；文档整篇翻译保留格式；数据合规（欧盟服务器、可不留存） |
| 主要竞品（初判）| Google Translate、微软翻译、Lingvanex、translate.com、iTranslate、Lara Translate、ChatGPT/LLM 翻译 |
| Olares 平替 | **MTranServer**（Olares Market ✅ 已上架，CPU 离线翻译服务器）；底层开源模型 **NLLB-200**（Meta 200 语）/ **Hy-MT2**（腾讯混元 MT） |
| 来源 | deepl.com、DeepL API 文档、Semrush（本报告数据） |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | deepl.com |
| SEMrush Rank | **257**（全球头部，SEO 极成熟）|
| 自然关键词数 | 201,390 |
| 月自然流量（US）| **9,998,472**（近千万）|
| 自然流量估值 | **$18,588,557/月** |
| 付费关键词数 | 22（几乎不投放）|
| 月付费流量 | 459 |
| 排名 1-3 位 | 39,565 词 |
| 排名 4-10 位 | 42,923 词 |
| 排名 11-20 位 | 22,427 词 |

> DeepL 是本组（翻译方向）SEO 最强的产品：近千万美国月自然流量、$1,860 万/月流量估值，几乎全部来自自然搜索——付费投放可以忽略（月付费流量仅 459）。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.deepl.com（主站）| 199,335 | 9,996,022 | 99.98% |
| support.deepl.com | 1,596 | 2,277 | 0.02% |
| developers.deepl.com | 422 | 172 | 0.00% |
| hs / auth / dict.deepl.com | 7-21 | 0-1 | 0% |

> 流量 99.98% 集中在主站——DeepL 不靠 docs/blog 分流，而是靠**主站上海量的"语言对翻译器"程序化落地页**（`/translator/l/<src>/<tgt>`）霸榜通用翻译词。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| translate | 2 | 37,200,000 | 100 | $2.14 | 2,418,000 | 信息 | /en/translator |
| english to spanish | 2 | 11,100,000 | 79 | $1.99 | 910,200 | 信息 | /translator/l/en/es |
| spanish to english | 2 | 9,140,000 | 74 | $1.93 | 594,100 | 信息 | /translator/l/es/en |
| deepl | 1 | 550,000 | 97 | $3.02 | 440,000 | 导航 | /en/translator |
| translate english to spanish | 2 | 5,000,000 | 86 | $1.43 | 325,000 | 信息 | /l/en/es |
| traductor（西）| 4 | 20,400,000 | 100 | $1.96 | 204,000 | 信息 | /es/translator |
| deepl translate | 1 | 246,000 | 87 | $1.93 | 196,800 | 导航 | /en/translator |
| translate to english | 2 | 1,220,000 | 100 | $1.59 | 100,040 | 信息 | /en/translator |
| traductor español ingles（西）| 2 | 5,000,000 | 100 | $0.95 | 90,000 | 信息 | /es/translator |
| deepl spanish to english translation | 1 | 110,000 | **36** | $0 | 88,000 | 导航 | /l/es/en |
| english to french | 1 | 1,000,000 | 79 | $2.39 | 82,000 | 信息 | /l/en/fr |
| translator | 2 | 1,000,000 | 100 | $2.09 | 82,000 | 信息 | /en/translator |
| translate spanish to english | 3 | 1,830,000 | 54 | $1.43 | 80,520 | 信息 | /l/es/en |
| deepl french to english translation | 1 | 90,500 | 51 | $0 | 72,400 | 导航 | /l/fr/en |
| translate to spanish | 2 | 823,000 | 82 | $1.46 | 67,486 | 信息 | /l/en/es |
| traductor ingles español（西）| 3 | 2,240,000 | 97 | $1.65 | 67,200 | 信息 | /es/translator |
| tradutor（葡）| 3 | 1,500,000 | 100 | $2.29 | 66,000 | 信息 | /en/translator |
| english to japanese | 1 | 673,000 | 50 | $2.76 | 55,186 | 信息 | /l/ja/en |
| переводчик（俄）| 3 | 823,000 | 90 | $2.25 | 53,495 | 信息 | /ru/translator |
| deepl translator | 1 | 60,500 | 93 | $1.93 | 48,400 | 导航 | /en/translator |
| übersetzer（德）| 2 | 550,000 | 68 | $1.82 | 45,100 | 信息 | /de/translator |
| french to english | 2 | 1,000,000 | 64 | $2.27 | 44,000 | 信息 | /l/fr/en |
| translation | 2 | 1,500,000 | 100 | $2.14 | 36,000 | 信息 | /en/translator |
| deepl english to german translation | 1 | 27,100 | 59 | $0 | 21,680 | 导航 | /l/en/de |
| deep l（拼写变体）| 1 | 27,100 | 93 | $3.02 | 21,680 | 导航 | /en/translator |
| deep translate | 1 | 22,200 | 84 | $1.93 | 17,760 | 导航 | /en/translator |
| deepl translator tool | 1 | 18,100 | 80 | $0 | 14,480 | 导航 | /en |
| deepl（写作）| 2 | 550,000 | 97 | $3.02 | 14,300 | 导航 | /en/write |
| google translate english to spanish | 8 | 2,240,000 | 100 | $1.07 | 13,440 | 信息 | /l/en/es |

> 观察：①**"translate"（3,720 万/月）DeepL 排第 2 就吃到 240 万流量**——通用翻译大词的非品牌流量极其巨大；②非英语市场极强（西/德/俄/葡/意/乌…全都靠 `/es/`、`/de/`、`/ru/` 语言站排名前列）；③**它甚至排到 `google translate english to spanish`（第 8 位）**，说明连竞品品牌词都在蚕食；④品牌导航词密集（deepl / deepl translate / deep l / deep translate 拼写变体全部霸榜第 1）。

### 付费词（Google Ads）

DeepL 几乎不做付费投放——22 个付费词、月付费流量仅 459，且**全部是品牌拼写保护词**（deeptranslate、transdlate、sdeepl、deep el、deepl..com…），统一导向 `/en` 首页。这是纯防御性的品牌护城（防竞品抢投），不买任何品类大词。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词（Phase 1 + related 驱动）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| best deepl alternatives 2025 | 720 | **12** | $0 | 信息 | ⭐ 高量超低 KD，本组最佳入口 |
| deepl vs google translate | 480 | 37 | $1.53 | 信息 | 头号对比词 |
| deepl pdf translator | 210 | 53 | $1.29 | 商业 | 文档翻译痛点 |
| google translate alternative | 210 | **20** | $1.52 | 商业 | ⭐ 替代意图明确 |
| better than google translate | 140 | 37 | $1.27 | 信息 | |
| deepl alternative | 110 | **17** | $2.13 | 信息/商业 | ⭐ CPC 高，商业价值 |
| better translation than google | 110 | **22** | $1.28 | 信息 | ⭐ |
| google translate alternatives | 110 | 29 | $2.19 | 信息 | ⭐ |
| alternative to google translate | 90 | **15** | $1.76 | 信息 | ⭐ |
| alternatives to google translate | 90 | **16** | $1.76 | 信息 | ⭐ |
| google translate vs deepl | 70 | 34 | $0 | 信息 | |
| deepl alternatives | 50 | **20** | $0 | 信息 | ⭐ |
| deepl vs chatgpt | 30 | 0 | $0 | 信息 | ⭐ LLM 翻译对比新兴 |
| free deepl alternative | 20 | **0** | $0 | 信息 | ⭐ 精准 |
| best deepl alternative | 10 | **0** | $0 | 信息 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai translation | 8,100 | 91 | $1.60 | 信息 | 品类大词，KD 高 |
| tools translation | 2,900 | 53 | $2.13 | 信息 | |
| machine translation | 1,900 | 64 | $3.33 | 信息 | |
| document translation | 1,900 | 61 | $2.32 | 信息 | |
| pdf translation | 1,900 | 49 | $1.23 | 信息 | 文档场景 |
| translation software | 1,300 | 31 | $3.40 | 商业 | 近机会线 |
| neural machine translation | 480 | 49 | $3.00 | 信息 | 技术词 |
| traductor ai（西）| 480 | 74 | $1.51 | 信息 | 非英语品类 |
| offline translator | 320 | 32 | $0.60 | 信息 | 离线场景 |
| translation api | 260 | 80 | $6.36 | 信息 | 高 CPC，开发者 |
| free translation api | 210 | 82 | $5.40 | 信息 | 高 CPC，KD 高 |
| offline translation | 140 | 32 | $0.60 | 信息 | |
| best machine translation | 110 | **24** | $2.37 | 信息 | ⭐ |
| machine translation api | 40 | 33 | $0 | 信息 | |
| best translation api | 40 | **24** | $5.80 | 商业 | ⭐ 高 CPC，开发者选型 |

### 产品 / 功能词（deepl 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deepl translator | 60,500 | 93 | $2.14 | 导航 | 品牌导航大词 |
| deepl write | 6,600 | 50 | $2.80 | 信息 | 写作助手功能词 |
| deepl api | 880 | 57 | $4.72 | 交易 | 开发者核心词，高 CPC |
| deepl pro | 720 | 56 | $3.42 | 商业 | 付费订阅词 |
| deepl api key | 390 | 54 | $1.64 | 商业 | |
| deepl api free | 320 | 55 | $0 | 交易 | 找免费 API |
| deepl chrome extension | 260 | 51 | $2.03 | 信息 | |
| deepl pricing | 170 | 41 | $2.46 | 交易 | 定价痛点 |
| deepl free | 140 | 70 | $0 | 商业 | |
| is deepl free | 110 | 66 | $0 | 信息 | 定价疑问 |
| deepl api pricing | 70 | 50 | $1.92 | 交易 | 定价痛点 |
| deepl subscription | 70 | 47 | $3.28 | 商业 | |
| deepl cost | 40 | 44 | $2.09 | 商业 | |
| deepl document translation | 30 | 53 | $1.77 | 交易 | |
| deepl for business | 20 | 0 | $0 | 商业 | |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| libretranslate | 590 | 46 | $2.69 | 导航 | 头号开源自托管命名竞品 |
| nllb-200 | 590 | 42 | $5.10 | 信息 | Meta 开源模型，高 CPC |
| offline translator | 320 | 32 | $0.60 | 信息 | |
| translate libre | 320 | **25** | $3.71 | 信息 | ⭐ LibreTranslate 变体 |
| libre translate | 260 | **23** | $3.71 | 信息 | ⭐ 变体，KD 低 |
| argos translate | 260 | 40 | $6.35 | 信息 | 开源库，高 CPC |
| libre translation | 260 | **30** | $3.71 | 信息 | 变体 |
| nllb | 210 | 56 | $0 | 信息 | |
| offline translation | 140 | 32 | $0.60 | 信息 | |
| local translation | 40 | **26** | $1.62 | 信息 | ⭐ |
| mtranserver | 20 | **0** | $2.18 | 导航 | ⭐ Olares Market 已上架 |
| open source translation | 20 | **0** | $2.78 | 信息 | ⭐ |
| open source machine translation | 20 | **0** | $0 | 信息 | ⭐ |
| open source translation api | 20 | **0** | $0 | 信息 | ⭐ |
| libretranslate self hosted | 20 | **0** | $0 | 信息 | GEO |
| self hosted translator | 20 | **0** | $0 | 信息 | GEO |
| self hosted translation service | 20 | **0** | $0 | 信息 | GEO |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：DeepL 是闭源 SaaS——Free 版有月字符限额、API 按量计费、译文需上传到 DeepL 云。Olares Market 已上架 MTranServer（CPU 离线翻译服务器），底层可跑开源模型 NLLB-200 / Hy-MT2，一键部署即"拥有自己的翻译 API"——无限量、零月费、数据不出境（GDPR/内网合规）。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| best deepl alternatives 2025 | 720 | **12** | $0 | MTranServer on Olares = 自托管零成本 DeepL 替代，列为首选；呼应"停止租用 AI" | ⭐⭐⭐ |
| deepl vs google translate | 480 | 37 | $1.53 | 对比文加第三选项：本地自托管（MTranServer/NLLB-200）——免费、离线、数据不出境 | ⭐⭐⭐ |
| offline translator | 320 | 32 | $0.60 | Olares 跑 MTranServer = 家庭/内网离线翻译节点，零数据外泄 | ⭐⭐⭐ |
| libre translate | 260 | **23** | $3.71 | MTranServer vs LibreTranslate：同为开源自托管，MTranServer 延迟更低、资源更省 | ⭐⭐⭐ |
| google translate alternative | 210 | **20** | $1.52 | 隐私叙事：Google 翻译上传数据；Olares 本地推理零外泄 | ⭐⭐⭐ |
| nllb-200 | 590 | 42 | $5.10 | "在自己硬件上跑 NLLB-200 200 语翻译"——Olares One 24GB 显存直接承载 | ⭐⭐⭐ |
| deepl alternative | 110 | **17** | $2.13 | DeepL 免费版限额、Pro/API 计费贵；MTranServer on Olares 一次部署永久免费 | ⭐⭐⭐ |
| deepl api free | 320 | 55 | $0 | 用户在找免费 API——Olares 上的翻译 API 完全免费、无速率限制、无 Key | ⭐⭐ |
| deepl api | 880 | 57 | $4.72 | 企业内部文档翻译无需付费额度，翻译 API 部署在自有内网 | ⭐⭐ |
| deepl pricing | 170 | 41 | $2.46 | Pro 订阅 vs 自托管：一次性成本、无月费、无字符上限 | ⭐⭐ |
| best translation api | 40 | **24** | $5.80 | 开发者选型清单：把自托管翻译 API（MTranServer）列入，主打免费+私有 | ⭐⭐ |
| local translation | 40 | **26** | $1.62 | 本地翻译模型（NLLB-200/Hy-MT2）跑在 Olares，Agent 可调用 | ⭐⭐ |
| mtranserver | 20 | **0** | $2.18 | 品牌词，Olares Market 一键部署入口 | ⭐⭐⭐ |
| open source translation / api | 20 | **0** | — | GEO：Olares Market 上架的开源翻译服务，直接命中 | ⭐⭐⭐ |
| self hosted translation service | 20 | **0** | $0 | GEO：语义完美契合，进 H2/FAQ 抢 AI Overview 引用位 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| best deepl alternatives 2025 | 720 | 12 | $0 | 信息 | 主词候选 | KD=12、量 720，本组最优入口；MTranServer on Olares 列首选自托管 DeepL 替代 |
| deepl vs google translate | 480 | 37 | $1.53 | 信息 | 主词候选 | 高流量对比词；写"DeepL vs Google vs 自托管"三方，Olares 作第三选项 |
| offline translator | 320 | 32 | $0.60 | 信息 | 主词候选 | 最稳的离线场景词；Olares = 永久离线翻译节点 |
| libre translate | 260 | 23 | $3.71 | 信息 | 主词候选 | LibreTranslate 变体 KD=23、CPC 高；MTranServer vs LibreTranslate 对比文 |
| google translate alternative | 210 | 20 | $1.52 | 商业 | 主词候选 | 隐私替代叙事；Olares = 数据不出门的翻译替代 |
| nllb-200 | 590 | 42 | $5.10 | 信息 | 主词候选 | Meta 200 语开源模型，高 CPC；"在 Olares 上本地跑 NLLB-200"教程 |
| deepl alternative | 110 | 17 | $2.13 | 信息/商业 | 主词候选 | KD=17 有购买意图；DeepL 定价/隐私痛点 → 自托管破解 |
| deepl api | 880 | 57 | $4.72 | 交易 | 次级 | 品牌 API 大词 KD 高排不动；导向"自托管翻译 API"内容 |
| deepl api free | 320 | 55 | $0 | 交易 | 次级 | 找免费 API 的意图，导向 MTranServer 免费无限量 API |
| deepl pricing | 170 | 41 | $2.46 | 交易 | 次级 | 定价痛点词，进对比文攻击面段落 |
| best translation api | 40 | 24 | $5.80 | 商业 | 次级 | 开发者选型、CPC 极高；把自托管 API 列入推荐 |
| local translation | 40 | 26 | $1.62 | 信息 | 次级 | 本地翻译模型词，与 offline 合簇 |
| deepl alternatives | 50 | 20 | $0 | 信息 | 次级 | 并入 deepl alternative 主词文章 |
| mtranserver | 20 | 0 | $2.18 | 导航 | GEO | 品牌词尚小、KD=0；建品牌内容培育增量 |
| self hosted translation service | 20 | 0 | $0 | 信息 | GEO | 语义精准近零量，抢 Perplexity/AI Overview 引用位 |
| open source translation api | 20 | 0 | $0 | 信息 | GEO | 开源自托管 API 定义词，值得提前占位 |

---

## 核心洞见

1. **品牌护城河：正面刚无胜算，也不必刚。** SEMrush Rank 257、近千万美国月自然流量、$1,860 万/月流量估值，且靠的是海量通用翻译词（`translate` 3,720 万/月排第 2 就吃 240 万流量）与全语种程序化落地页。DeepL 甚至反攻 `google translate english to spanish`（排第 8）。这类通用翻译词护城河 Olares 抢不动、也不该抢——切入点在**替代/自托管/隐私**这一侧。

2. **可复制的打法：全语言对程序化落地页 + 强品牌导航。** DeepL 的流量引擎是 `/translator/l/<src>/<tgt>` 结构化落地页矩阵（每个语言对一页），配合品牌拼写变体全部霸榜第 1，以及纯防御性的品牌保护付费投放。Olares Market 可复用"程序化落地页"思路——为 MTranServer / NLLB-200 / Hy-MT2 各做"X on Olares / self-hosted X"页，但走的是**替代词矩阵**而非通用翻译词。

3. **对 Olares 最关键的 3 个词：**
   - **`best deepl alternatives 2025`（720/月, KD=12）**——本组量最大、KD 最低的进入点，Olares 平台可把 MTranServer 列为首选自托管选项。
   - **`deepl vs google translate`（480/月, KD=37）**——最高流量对比词，写成"DeepL vs Google vs 自托管"三方对比，Olares 作零成本、数据不出境的第三选项。
   - **`offline translator`（320/月, KD=32）+ `libre translate`（260/月, KD=23）**——离线/开源自托管场景词组，直接命中 MTranServer 的核心卖点。

4. **最大攻击面：定价 + 数据隐私（闭源云）。** `deepl pricing`（170）、`deepl api free`（320）、`is deepl free`（110）、`deepl api pricing`（70）、`deepl subscription/cost` 密集出现，说明用户对 **Free 版字符限额 + API 按量计费**高度敏感。最有力的叙事是"停止按量付费、译文不上云 → 在 Olares 上自托管 MTranServer/NLLB-200 = 无限量、零月费、数据不出境"，与 Olares "Stop Renting. Own your AI." 高度契合。

5. **隐藏低 KD 金矿：** `best deepl alternatives 2025`（KD=12）、`alternative to google translate`（90, KD=15）、`alternatives to google translate`（90, KD=16）、`deepl alternative`（110, KD=17）、`libre translate`（260, KD=23）、`best translation api`（40, KD=24, CPC=$5.80）——这些替代/自托管词量虽不都大，但 KD 极低、竞争几乎为空白，且有明确商业意图，是低成本抢排名的首选。

6. **GEO 前瞻布局：** `mtranserver`（KD=0）、`open source translation api`（KD=0）、`self hosted translation service`（KD=0）、`libretranslate self hosted`（KD=0）、`self hosted translator`（KD=0）目前近零量，但语义与 Olares 完美契合。建议在文章 H2/FAQ 里权威定义"self-hosted translation / run NLLB-200 on your own hardware"，抢 AI Overview / Perplexity 引用位——随"本地 AI / 自托管"品类意识提升，是未来 6-12 个月的潜力词。

7. **与既有分析的关联：** 本报告与 Market 方向的 [mtranserver.md](/Users/pengpeng/seo/directions/market/reports/mtranserver.md) 互为供需两侧——DeepL 侧提供"替代/定价痛点"需求词，MTranServer 侧提供"离线/开源自托管"供给词，二者在 seo-content 阶段应聚成同一批对比/替代文簇（`deepl alternative`、`deepl vs google translate`、`libre translate` 等）。同时与 `olares-500-keywords` 的 `self-hosted`、`private AI`、`local AI`、`run locally` 主干叙事一致，翻译可作为"本地 AI 工具"的具体应用案例填入。（对比旧稿：旧报告以 LibreTranslate / Argos + Hunyuan Translation 为 Olares 平替，本次按现状更新为 **MTranServer（Market 已上架）+ NLLB-200 / Hy-MT2 模型**；旧稿关于"多语言护城河""translate 大词流量巨大"的判断仍成立，予以保留。）

---

*数据来源：SEMrush us 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_related / phrase_fullsearch）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
