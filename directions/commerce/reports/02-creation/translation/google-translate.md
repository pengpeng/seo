# Google Translate SEO 竞品分析报告

> 域名：translate.google.com | SEMrush US | 2026-07-06
> Google 旗舰 AI 翻译服务——支持 249+ 语言、全球最大流量翻译产品，消费端完全免费，开发者走 Cloud Translation API 付费

---

## 项目理解（前置）

Google Translate 是 Google 于 2006 年推出的在线翻译服务，覆盖 249+ 语言，消费端（Web / iOS / Android）完全免费，功能包括文本、语音、相机 AR、对话模式、文档上传与离线包。底层为 Gemini 驱动的神经机器翻译（NMT），近年新增 Translation LLM 和 Adaptive Translation（按 $10–25/M 字符计费）。开发者侧走 Google Cloud Translation API，基础/高级版 $20/M 字符，每月 50 万字符免费。据 2026 年 4 月流量统计，translate.google.com 在全球 AI 翻译市场占据约 **85%** 的访问量份额。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 全球最大流量免费在线翻译，249+ 语言，零门槛 |
| 开源 / 许可证 | 闭源；底层 NMT 引擎不公开 |
| 主仓库 | 无公开 GitHub；Cloud Translation API 文档：[cloud.google.com/translate](https://cloud.google.com/translate) |
| 核心功能 | 文本翻译、相机 AR 实时翻译、语音对话模式、文档上传（PDF/DOCX/PPTX）、离线语言包、Chrome 右键翻译、开发者 API（Basic/Advanced/LLM/Adaptive） |
| 商业模式 / 定价 | 消费端免费（无字符限制）；API：$20/M chars（NMT）/ $10–25/M chars（LLM 系列）；每月 50 万字符免费额度 |
| 差异化 / 价值主张 | 语言覆盖最广（249+ 远超 DeepL 的 33 种）、零门槛、全平台深度集成（Chrome / Gmail / Docs / Android 系统级）、相机 AR 独特体验 |
| 主要竞品（初判）| DeepL（专业质量）、Microsoft Translator（企业生态）、Papago（韩语）、Yandex Translate（俄语） |
| Olares Market | 未上架（闭源服务，不可自部署）；开源平替：NLLB-200 / Hy-MT2（MTranServer 已上架 Olares Market） |
| 来源 | [translate.google.com](https://translate.google.com)、[cloud.google.com/translate/pricing](https://cloud.google.com/translate/pricing)、[taia.io：DeepL vs Google Translate 2026](https://taia.io/resources/blog/deepl-vs-google-translate-vs-microsoft-translator/)、[onelittleweb.com 2026-04 流量数据](https://onelittleweb.com/digital-market-intelligence/ai-tools/translators/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | translate.google.com |
| SEMrush Rank | #1（google.com 整域，translate 为第三大子域） |
| 自然关键词数 | 356,504 |
| 月自然流量（US）| 37,271,259 |
| 自然流量估值 | $72,176,364 /月 |
| 付费关键词数 | 51（注：为第三方滥用 translate.google.com 作跳转落地页的垃圾广告，非 Google 官方投放） |
| 月付费流量 | 2,132 |
| 排名 1-3 位 | 48,716 词 |
| 排名 4-10 位 | 18,213 词 |
| 排名 11-20 位 | 17,977 词 |

> **付费流量说明**：Semrush 显示的 51 个付费词均为"Norton Support 诈骗电话"类广告，落地 URL 为 translate.google.com（黑产利用 Google Translate 作 URL 跳转中转）。Google 本身**不为 translate.google.com 买广告**——该产品依赖 Google 整体品牌搜索流量的自然溢出。

### 子域名流量分布（google.com TOP 10）

| 子域名 | 关键词数 | 流量（US/月） | 占比 |
|--------|---------|------|------|
| www.google.com | 5,585,766 | 148,173,324 | 26.72% |
| play.google.com | 20,202,042 | 130,921,408 | 23.61% |
| **translate.google.com** | **356,504** | **37,271,259** | **6.72%** |
| maps.google.com | 117,360 | 33,257,037 | 6.00% |
| support.google.com | 5,192,079 | 32,997,170 | 5.95% |
| gemini.google.com | 22,883 | 27,171,172 | 4.90% |
| workspace.google.com | 304,345 | 18,822,601 | 3.39% |
| sites.google.com | 2,121,149 | 16,581,838 | 2.99% |
| docs.google.com | 198,419 | 16,090,948 | 2.90% |
| chromewebstore.google.com | 1,264,765 | 10,268,111 | 1.85% |

translate.google.com 以 37M 月流量排名 google.com 子域第 3 位，仅次于 www 和 Play Store。关键词效率极高：356K 词撬动 37M 流量，平均每词 104 次访问——远高于 gemini（22K 词撬动 27M 流量，均值 1,187）。说明 translate 子域流量高度集中于少数超高量词。

### 官网 TOP 自然关键词（按流量降序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| traductor | 1 | 20,400,000 | 100 | $1.96 | 16,320,000 | 导航 | /\?hl=es |
| translate | 1 | 37,200,000 | 100 | $2.14 | 3,050,400 | 信息 | / |
| english to spanish | 1 | 11,100,000 | 79 | $1.99 | 1,465,200 | 信息 | / |
| google translate | 1 | 37,200,000 | 100 | $1.39 | 967,200 | 信息/导航 | / |
| translate（about 页） | 6 | 37,200,000 | 100 | $2.14 | 892,800 | 信息 | /about/ |
| spanish to english | 1 | 9,140,000 | 74 | $1.93 | 749,480 | 信息 | / |
| traducir | 1 | 823,000 | 67 | $1.88 | 658,400 | 导航 | /\?hl=es |
| traductor google | 1 | 673,000 | 95 | $1.12 | 538,400 | 导航 | /\?hl=es |
| 谷歌翻译 | 1 | 550,000 | 75 | $5.55 | 440,000 | 信息/导航 | /\?hl=zh-cn |
| translate english to spanish | 1 | 5,000,000 | 86 | $1.43 | 410,000 | 信息 | / |
| traductor ingles español | 1 | 2,240,000 | 97 | $1.65 | 295,680 | 信息 | /\?hl=es |
| traduction | 1 | 301,000 | 68 | $1.96 | 240,800 | 导航 | /\?hl=fr |
| google traduction | 1 | 301,000 | 85 | $1.17 | 240,800 | 导航 | /\?hl=fr |
| google traductor | 1 | 301,000 | 90 | $1.12 | 240,800 | 导航 | /\?hl=es |
| ترجمة / ترجمه（阿拉伯） | 1 | 246,000 | 85–86 | $2.19 | 196,800 | 导航 | /\?hl=ar |
| translate to english | 1 | 1,220,000 | 100 | $1.59 | 161,040 | 信息 | / |
| terjemahan（印尼） | 1 | 201,000 | 69 | $3.39 | 160,800 | 导航 | /\?hl=id |
| translate spanish to english | 1 | 1,830,000 | 54 | $1.43 | 150,060 | 信息 | / |
| translator | 1 | 1,000,000 | 100 | $2.09 | 132,000 | 信息 | / |
| translation | 1 | 1,500,000 | 100 | $2.14 | 123,000 | 信息 | / |
| translate to spanish | 1 | 823,000 | 82 | $1.46 | 108,636 | 信息 | / |
| переводчик（俄） | 1 | 823,000 | 90 | $2.25 | 108,636 | 导航 | /\?hl=ru |
| english to spanish translation | 1 | 1,220,000 | 63 | $1.31 | 100,040 | 信息 | / |
| google translate app | 1 | 110,000 | 92 | $1.15 | 88,000 | 导航 | / |
| french to english | 1 | 1,000,000 | 64 | $2.27 | 82,000 | 信息 | / |
| übersetzer（德） | 1 | 550,000 | 68 | $1.82 | 72,600 | 导航 | /\?hl=de |
| spanish to english translation | 1 | 550,000 | 61 | $1.36 | 72,600 | 信息 | / |
| english to hindi | 1 | 823,000 | 49 | $2.96 | 67,486 | 信息 | / |
| english to french | 2 | 1,000,000 | 79 | $2.39 | 65,000 | 信息 | / |
| google translate camera | 1（推断） | 33,100 | 55 | $1.09 | — | 导航 | — |

**洞察**：流量最大的词 "traductor"（16M/月）是西班牙语"翻译"——Google Translate 实际上垄断了全球多语言导航词（西班牙语、法语、俄语、阿拉伯语、德语、印尼语各类母语词），这些词在任何竞品的维度上都难以撼动。单一词 "translate" 月量高达 37.2M，但流量分配下只贡献 3.05M 访问（因排名竞争或直接浏览器访问），意味着 Google 本身也有大量直接访问流量未被 Semrush 计入。

### 付费词（Google Ads）

translate.google.com 自身**不投放搜索广告**。Semrush 记录到的 51 个付费词均为黑产/诈骗方（Norton 假客服类）将 translate.google.com 作跳转中转的滥用行为，无参考价值。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<40 且量>0 的机会词（对第三方内容有攻击价值）。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deepl vs google translate | 480 | 37 | $1.53 | 信息/商业 | ⭐ 对比文高价值 |
| best online translator | 480 | 45 | $1.79 | 信息/商业 | 品类导向 |
| google translate vs deepl | 70 | 34 | $0 | 信息/商业 | ⭐ 同上另一方向 |
| google translate alternative | 210 | 20 | $1.52 | 商业 | ⭐⭐ 核心替代词 |
| google translate alternatives | 110 | 29 | $2.19 | 商业 | ⭐⭐ |
| alternative to google translate | 90 | 15 | $1.76 | 信息 | ⭐⭐ KD 极低 |
| alternatives to google translate | 90 | 16 | $1.76 | 信息 | ⭐⭐ KD 极低 |
| deepl alternative | 110 | 17 | $2.13 | 商业 | ⭐⭐ 间接竞品 |
| best google translate alternatives 2026 | 40 | 0 | $0 | 信息 | ⭐⭐ 近零竞争 |
| google translate api alternative | 20 | 0 | $1.26 | 商业 | ⭐ API 替换意图 |
| google translate alternative free | 20 | 0 | $0 | 商业 | ⭐ |
| free alternative to google translate | 20 | 0 | $0 | 商业 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| translate app | 9,900 | 98 | $1.70 | 信息 | 品牌高度集中 |
| best translation app | 5,400 | 28 | $1.82 | 商业 | ⭐ 可竞争 |
| translation app | 4,400 | 86 | $1.70 | 信息 | 竞争激烈 |
| offline translator | 320 | 32 | $0.60 | 信息 | ⭐ 本地化诉求 |
| translation api | 260 | 80 | $6.36 | 信息 | 高 CPC，开发者 |
| best translation app for iphone | 1,300 | 37 | $1.79 | 商业 | ⭐ |
| best translator | 3,600 | 58 | $1.55 | 商业 | |
| best spanish translator | 1,300 | 40 | $1.75 | 商业 | ⭐ |
| real time translation app | 1,600 | 63 | $1.75 | 商业 | |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google translate camera | 33,100 | 55 | $1.09 | 导航 | 相机功能独特优势 |
| google translate extension | 5,400 | 76 | $4.01 | 导航 | Chrome 扩展 |
| google translate document | 4,400 | 53 | $1.64 | 导航 | 文档翻译 |
| google translate api | 1,600 | 54 | $7.70 | 信息 | 高 CPC 开发者词 |
| google translate conversation mode | 880 | 57 | $1.63 | 信息 | |
| google translate offline | 480 | 47 | $1.18 | 信息 | |
| google translate accuracy | 140 | 36 | $0.42 | 信息 | ⭐ 痛点词 |
| google translate api pricing | 210 | 37 | $5.28 | 商业 | ⭐ 高 CPC |
| google translate pricing | 70 | 26 | $0 | 商业 | ⭐ |
| is google translate accurate | 1,000 | 37 | $0 | 信息 | ⭐ |
| how accurate is google translate | 720 | 34 | $0 | 信息 | ⭐ |
| is google translate ai | 390 | 73 | $0 | 信息 | |
| how does google translate work | 390 | 72 | $2.02 | 信息 | |
| can google translate translate mp3 files | 1,000 | 31 | $0 | 信息 | ⭐ |
| how to translate a google doc | 1,000 | 42 | $1.12 | 信息 | |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| argos translate | 260 | 40 | $6.35 | 信息 | ⭐ 开源 MT 项目 |
| libre translate | 260 | 23 | $3.71 | 信息 | ⭐⭐ 极低竞争 |
| ctranslate2 | 260 | 30 | $0 | 导航 | ⭐ 推理引擎 |
| deepl free alternative | 30 | 0 | $0 | 商业 | ⭐⭐ 近零竞争 |
| open source translation | 20 | 0 | $2.78 | 信息 | ⭐⭐ |
| nllb translation | 20 | 0 | $0 | 信息 | ⭐⭐ Olares 平替核心模型 |
| nllb model | 20 | 0 | $0 | 信息 | ⭐⭐ |
| helsinki nlp | 30 | 0 | $0 | 信息 | ⭐⭐ OPUS-MT 背后 |
| opus mt | 20 | 0 | $4.88 | 信息 | ⭐⭐ |
| local ai translation | 20 | 0 | $0 | 信息 | ⭐⭐ |
| offline translation tool | 20 | 0 | $0 | 信息 | ⭐⭐ |
| private translation | 10 | 0 | $0 | 信息 | ⭐⭐ 隐私诉求 |

---

## Olares 关联词（Phase 3）

**核心逻辑**：Google Translate 闭源且强制上传数据至 Google 服务器，用户无隐私保障；NLLB-200 / Hy-MT2 可通过 MTranServer（已上架 Olares Market）在本地完全离线运行，零数据泄露风险——Olares 的切入角度是**隐私 + 离线 + 数据主权**，而非质量对抗。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| google translate alternative | 210 | 20 | $1.52 | ⭐⭐⭐ MTranServer（NLLB）= 可自部署 Google Translate 替代，Olares 一键安装，离线无数据上传 |
| alternative to google translate | 90 | 15 | $1.76 | ⭐⭐⭐ KD=15，几乎无竞争；"隐私优先的本地翻译"叙事完美贴合 |
| alternatives to google translate | 90 | 16 | $1.76 | ⭐⭐⭐ 同上变体 |
| best google translate alternatives 2026 | 40 | 0 | $0 | ⭐⭐⭐ KD=0，今年新词，Olares 可抢先排名 |
| google translate alternative free | 20 | 0 | $0 | ⭐⭐⭐ "self-hosted 完全免费"叙事 |
| libre translate | 260 | 23 | $3.71 | ⭐⭐⭐ LibreTranslate 是主流开源翻译，可在 Olares 上自部署，与 MTranServer 形成矩阵 |
| offline translator | 320 | 32 | $0.60 | ⭐⭐ Olares+MTranServer = 真正离线翻译；对比 Google Translate 需要联网 |
| argos translate | 260 | 40 | $6.35 | ⭐⭐ Argos = 可自部署，Olares Market 收录潜在品类 |
| deepl vs google translate | 480 | 37 | $1.53 | ⭐⭐ 在对比文里插入"都不私密"→ Olares 平替角度 |
| is google translate accurate | 1,000 | 37 | $0 | ⭐⭐ 信息类内容机会：NLLB-200 准确度对比文，带出 Olares 本地部署 |
| how accurate is google translate | 720 | 34 | $0 | ⭐⭐ 同上 |
| google translate api pricing | 210 | 37 | $5.28 | ⭐⭐ API 定价痛点：自部署 NLLB = $0/M tokens，直接替代 |
| nllb translation | 20 | 0 | $0 | ⭐⭐⭐ NLLB 是 Olares 平替的核心模型，GEO 抢位 |
| nllb model | 20 | 0 | $0 | ⭐⭐⭐ GEO 前哨 |
| local ai translation | 20 | 0 | $0 | ⭐⭐⭐ GEO 前哨，AI Overview 抢引用 |
| private translation | 10 | 0 | $0 | ⭐⭐⭐ GEO：最精准的隐私场景词 |
| ctranslate2 | 260 | 30 | $0 | ⭐ MTranServer 底层推理引擎，技术向内容机会 |
| 谷歌翻译（中文） | 550,000 | 75 | $5.55 | ⭐ 中文用户群庞大（$5.55 CPC 证明商业价值高）；中文 Olares 对比内容机会 |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇（可跨报告）在 seo-content 阶段做。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| google translate alternative | 210 | 20 | $1.52 | 商业 | **主词候选** | KD 极低+商业意图+CPC 正向；写"X alternatives"文撑一整篇；Olares MTranServer 是核心答案 |
| alternative to google translate | 90 | 15 | $1.76 | 信息 | **主词候选** | KD=15 全类目最低，与上词同簇，量合计≈390；几乎无竞争，立即可排 |
| deepl vs google translate | 480 | 37 | $1.53 | 信息/商业 | **主词候选** | 量最大的对比词；KD=37 可进入；在文中加"第三选项=本地/隐私"打差异化 |
| libre translate | 260 | 23 | $3.71 | 信息 | **主词候选** | 开源替代品类量+KD 组合最优；Olares Market 自部署叙事直接承接 |
| offline translator | 320 | 32 | $0.60 | 信息 | **主词候选** | 量合理+KD 中等+本地化诉求；Olares 离线翻译叙事完全贴合 |
| best translation app | 5,400 | 28 | $1.82 | 商业 | **主词候选** | 量大+KD=28，值得独立文；提及 MTranServer 作自部署选项 |
| is google translate accurate | 1,000 | 37 | $0 | 信息 | **主词候选** | 信息意图高量，KD 可进；写精度对比文，带出 NLLB 准确度数据 |
| google translate api pricing | 210 | 37 | $5.28 | 商业 | **主词候选** | CPC=$5.28 最高，开发者付费意图；可写"$0 本地替代 vs $20/M"定价对比 |
| alternatives to google translate | 90 | 16 | $1.76 | 信息 | 次级 | 并入"google translate alternative"文章，KD=16 |
| google translate alternatives | 110 | 29 | $2.19 | 商业 | 次级 | 同上文章的 H2 锚文本 |
| argos translate | 260 | 40 | $6.35 | 信息 | 次级 | 并入开源翻译对比文；Olares 可部署 |
| ctranslate2 | 260 | 30 | $0 | 导航 | 次级 | 技术向内容；MTranServer 推理引擎 |
| how accurate is google translate | 720 | 34 | $0 | 信息 | 次级 | 并入准确度文章，量>700 |
| deepl alternative | 110 | 17 | $2.13 | 商业 | 次级 | ⭐ DeepL 用户流失点，KD 极低 |
| google translate pricing | 70 | 26 | $0 | 商业 | 次级 | ⭐ FAQ 锚词，带出自部署免费叙事 |
| best google translate alternatives 2026 | 40 | 0 | $0 | 信息 | 次级 | KD=0，年份词，今年独家机会 |
| nllb translation | 20 | 0 | $0 | 信息 | **GEO** | 核心模型词，AI Overview 抢引用；Olares 平替直接叙述 |
| nllb model | 20 | 0 | $0 | 信息 | **GEO** | 同上，研究者/开发者受众 |
| local ai translation | 20 | 0 | $0 | 信息 | **GEO** | 精准需求词，Perplexity 类 AI 答题机会 |
| private translation | 10 | 0 | $0 | 信息 | **GEO** | 最精准隐私场景；AI Overview FAQ 首选词 |
| open source translation | 20 | 0 | $2.78 | 信息 | **GEO** | 开发者场景；$2.78 CPC 证明商业价值 |
| google translate api alternative | 20 | 0 | $1.26 | 商业 | **GEO** | 开发者替代 API 场景 |

---

## 核心洞见

1. **品牌护城河（能否正面刚？）**
   正面刚不可行。"translate" / "google translate" 均为 KD=100，translate.google.com 以 37M/月压倒性流量占据全球品类心智，任何非 Google 域名无法在品牌词层面竞争。**正确姿态**：绕开品牌词，专攻替代词（KD 15–29）、准确度质疑词、定价痛点词、开源/隐私信号词——这些 KD 普遍低于 40。

2. **可复制的打法**
   Google Translate 本身不做内容 SEO——它依赖品牌心智自然引流。可复制的是：
   - **多语言落地页**：`?hl=es`、`?hl=fr`、`?hl=zh-cn` 等语言前缀构成隐性的程序化多语言页面，每个语言词（traductor、traduction、переводчик）都贡献数十万流量。竞品可仿照为 NLLB 支持的 200+ 语言各建一页。
   - **语言对 URL 结构**："english to spanish"（1.1M/月）这类 `[源语言] to [目标语言]` 查询可程序化生成，KD 普遍 50–80 中段，有机会通过大量覆盖实现规模效应。

3. **对 Olares 最关键的词**
   - `google translate alternative` / `alternative to google translate`（KD 15–20，主词候选，隐私叙事直接锚定）
   - `libre translate`（KD=23，开源项目品类词，Olares Market 已有同类自部署场景）
   - `nllb translation` + `local ai translation`（GEO 前哨，AI Overview 上抢"本地离线翻译"引用位）

4. **最大攻击面**
   - **隐私/数据主权**：Google Translate 强制将翻译内容上传至 Google 服务器，法律合规（GDPR / HIPAA）场景下不可用。NLLB-200 在 Olares 上本地运行，翻译内容零出境——这是不可辩驳的差异化。
   - **API 定价**：Cloud Translation API $20/M chars（NMT）→ $25/M chars（Adaptive），高用量企业成本显著；自部署 MTranServer = 硬件成本 amortization 后接近 $0/M。"google translate api pricing" CPC=$5.28 印证付费意图。
   - **语言质量**：DeepL 在欧洲语言质量上已超越 Google（专家偏好 1.3x），但 DeepL 也是闭源云服务；NLLB 覆盖 200 语言质量有差异，是已知弱点，需诚实披露。

5. **隐藏低 KD 金矿**
   - `alternative to google translate` KD=**15**、`alternatives to google translate` KD=**16**：全翻译品类最低竞争替代词，月量合计 180，CPC≈$1.76，立即可写。
   - `best google translate alternatives 2026` KD=**0**：年份词近零竞争，今年独占机会。
   - `google translate pricing` KD=**26**：定价查询词，用户处于考虑替代阶段，转化意图强。
   - `deepl alternative` KD=**17**：非直接竞品词，但 DeepL 用户流失场景下 Olares/NLLB 是切入点。

6. **GEO 前瞻布局**
   以下词当前近零量，但在 Perplexity / AI Overview 时代有望成为答案层入口：
   - **`private translation`**（隐私翻译）：最精准的需求，AI 答题首选位
   - **`local ai translation`**（本地 AI 翻译）：新兴需求词，NLLB 是答案
   - **`nllb translation`** / **`nllb model`**：技术受众 GEO 词，Olares 文档可成为 AI 引用来源
   - **`open source translation`**：开发者/研究者导向，高价值低流量

7. **与既有分析的关联**
   DeepL 报告（`commerce/reports/02-creation/translation/deepl.md`）已覆盖 "deepl alternative" 等词；本报告对 DeepL 报告的补充在于：① Google Translate 的多语言词（各语言本地词，如 traductor/traduction）是独立高流量入口，需单独建多语言页；② "google translate api pricing" 与 "libre translate" 构成新的主词候选，未在 DeepL 报告中出现；③ NLLB-200 / MTranServer 叙事在两份报告中均适用，但切入角度不同（DeepL 攻质量痛点，Google Translate 攻隐私 + 数据主权 + 定价）。建议跨报告合并建一篇 "best google translate alternatives" 文章，同时涵盖 DeepL 和 NLLB 场景。

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、resource_adwords、domain_organic_organic、phrase_these、phrase_fullsearch、phrase_related、phrase_questions）| 2026-07-06*

*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍（"translate" 全球实际月量远超 37M US 数字，翻译需求本质上是全球平等分布的）。*
