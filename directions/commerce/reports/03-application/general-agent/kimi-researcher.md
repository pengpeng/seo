# Kimi Work / Kimi Researcher SEO 竞品分析报告

> 域名：kimi.com | SEMrush US | 2026-07-06
> Moonshot AI（月之暗面）旗下深度研究 Agent + 本地桌面 Agent 产品；母品牌 ARR >$300M，估值 $31.5B，品牌词护城河极强，英文 agent 子品牌词量尚在冷启动期。

---

## 项目理解（前置）

Kimi 是 Moonshot AI（北京月之暗面）面向全球市场的旗舰 AI 产品，底层模型为 Kimi K2 系列（MoE 架构，256K 上下文，单任务可调度最多 300 个并行 sub-agent）。**Kimi Deep Research / Kimi Researcher** 是其云端深度研究 Agent：自主分解任务、跨网页+专业数据库多轮搜索、推理过滤后输出带引用的多格式报告（HTML/Word/PPT/Excel/PDF）。**Kimi Work**（2026-06 内测）是本地桌面 Agent：运行于 macOS/Windows，读取本地文件、经 WebBridge 驱动真实浏览器、内置 cron 调度，解决"本地已登录会话+循环任务"的空白。两者共用 Kimi K2.6 模型与统一积分体系。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 云端深度研究 Agent（Kimi Researcher） + 本地桌面 Agent（Kimi Work），搭载 K2.6，最多 300 sub-agent 并行 |
| 开源 / 许可证 | 闭源 SaaS；底层模型 K2.6 以开放权重（open-weights）发布，不含服务代码 |
| 主仓库 | 无独立仓库；K2.6 权重见 Hugging Face moonshot-ai/Kimi-K2-Instruct |
| 核心功能 | ① Deep Research（多轮自主搜索+专业数据库+多格式输出）② Agent Swarm（最多 300 并行子 Agent）③ Kimi Work 本地桌面 + 文件 + 浏览器控制 ④ Kimi Claw（云端 7×24 Agent）⑤ Kimi Code/Slides/Docs |
| 商业模式 / 定价 | 免费 Adagio（6 次/刷新）→ Moderato $19/月 → Allegretto $39/月（含 Agent Swarm）→ Allegro $99/月 → Vivace $199/月；年付最多节省 $480 |
| 差异化 / 价值主张 | Agent Swarm 300 并行子 Agent（国内外竞品罕见）；K2.6 在 OpenRouter 用量全球第二；Kimi Work 把云端 Agent 延伸到本地已登录会话，补"云沙盒无法触碰本地文件"的最后一公里 |
| 主要竞品（初判）| Perplexity Deep Research、ChatGPT Deep Research（OpenAI）、Gemini Deep Research（Google）、NotebookLM；本地 Agent 对标：Manus、Claude Computer Use、Microsoft Copilot Studio |
| Olares Market | 未上架（闭源）；开源平替 DeerFlow 2.0 已上架，见 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md) |
| 来源 | [kimi.com/features/deep-research](https://www.kimi.com/features/deep-research)、[kimi.com/help/membership/membership-pricing](https://www.kimi.com/help/membership/membership-pricing)、[The Next Web](https://thenextweb.com/news/moonshot-ai-kimi-30-billion-valuation-china-ai-race)、[BigGo Finance](https://finance.biggo.com/news/8899e316-242d-4517-8f76-4a491d5ac39d)（2026-07） |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | kimi.com |
| SEMrush Rank | 17,373 |
| 自然关键词数 | 6,849 |
| 月自然流量（US）| 128,366 |
| 自然流量估值 | $206,611/月 |
| 付费关键词数 | 348 |
| 月付费流量 | 18,643 |
| 付费流量成本 | $25,907/月 |
| 排名 1-3 位 | 417 词 |
| 排名 4-10 位 | 539 词 |
| 排名 11-20 位 | 1,069 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.kimi.com | 6,556 | 126,572 | 98.60% |
| platform.kimi.com | 284 | 1,560 | 1.22% |
| careers.kimi.com | 9 | 234 | 0.18% |

> **结构解读**：几乎所有流量聚集于主站；platform.kimi.com（API 控制台）贡献 1,560 流量，说明开发者/API 词已产生独立入口。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| kimi | 1 | 74,000 | 54 | $0.56 | 18,352 | 导航 | /en |
| kimi k2 | 1 | 22,200 | 74 | $3.06 | 17,760 | 信息 | /en |
| kimi ai | 1 | 22,200 | 78 | $0.83 | 17,760 | 导航 | /en |
| kimi2 | 1 | 8,100 | 85 | $3.06 | 6,480 | 导航 | /en |
| kimi ia | 1 | 4,400 | 77 | $0.83 | 3,520 | 导航 | /en |
| kimi 2.5 | 1 | 4,400 | 75 | $1.23 | 3,520 | 信息 | /ai-models/kimi-k2-5 |
| kimik2 | 1 | 2,900 | 72 | $3.06 | 2,320 | 导航 | /en |
| kimi ppt助手 | 1 | 2,400 | 28 | $1.06 | 1,920 | 商业 | /zh/slides |
| kimi for coding | 1 | 2,400 | 50 | $4.80 | 1,920 | 导航 | /code/en |
| kimi code | 1 | 2,400 | 46 | $3.26 | 1,920 | 导航 | /code/en |
| kimi claw | 1 | 1,900 | 42 | $1.67 | 1,520 | 信息/商业 | /bot |
| kimi k2.6 | 1 | 1,600 | 44 | $1.89 | 1,280 | 信息 | /ai-models/kimi-k2-6 |
| kimi slides | 1 | 1,600 | 30 | $1.19 | 1,280 | 导航/商业 | /en/slides |
| kimi k2.5 | 1 | 40,500 | 77 | $1.29 | 1,053 | 信息 | /ai-models/kimi-k2-5 |
| kimi ppt | 1 | 1,300 | 28 | $0.84 | 1,040 | 商业 | /en/slides |
| kimi chat | 1 | 1,000 | 45 | $0.98 | 800 | 导航 | /en |
| kimi 2.6 | 1 | 1,000 | 41 | $2.02 | 800 | 信息/商业 | /ai-models/kimi-k2-6 |
| kimi coding plan | 1 | 880 | 34 | $7.63 | 704 | 信息/商业 | /code/en |
| kimi ok computer | 1 | 590 | 37 | $0.53 | 472 | 导航 | /en |
| **deep research** | **4** | **6,600** | **66** | **$3.19** | **290** | **信息** | **/en/deep-research** |
| 月之暗面 api | 1 | 320 | 22 | $0.00 | 256 | 导航 | platform.kimi.com |

> **关键洞察**：`deep research` 排名第 4（非第 1），月流量仅 290 / 128K 总量的 0.2%——Kimi 的深度研究功能流量几乎全来自品牌导航词，非 "deep research" 品类词分发；品类词被 ChatGPT/Google/Gemini 主导。`kimi ppt` 和 `kimi slides`（KD 28-30）是罕见的低竞争度大流量词——PPT 落地页是程序化内容成功案例。

### 付费词（Google Ads，按流量排序）

主要买**超宽泛词导向品牌落地页**（含 kimi-work 产品页），投放逻辑偏防守（护住品牌词）+ 少量进攻（抢 "free ai"、"chat gpt alternatives"）。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| free ai | 74,000 | $1.34 | kimi.com/ |
| kimi | 60,500 | $0.42 | kimi.com/ |
| kimi k2 | 22,200 | $3.06 | kimi.com/ |
| kimi ai | 22,200 | $0.83 | kimi.com/ |
| kimi2 | 8,100 | $3.06 | kimi.com/products/kimi-work |
| moonshot ai | 6,600 | $1.40 | kimi.com/ |
| 月之暗面 | 5,400 | $1.51 | kimi.com/ |
| kimi ia | 4,400 | $0.83 | kimi.com/ |
| chat gpt alternatives | 2,900 | $1.45 | kimi.com/products/kimi-work |
| new chinese ai | 2,400 | $1.12 | kimi.com/ |
| kimi ppt助手 | 2,400 | $0.76 | kimi.com/features/slides |

> **策略解读**：`free ai`（74K）是最大的进攻性买词；`chat gpt alternatives`（2.9K，CPC $1.45）定向到 kimi-work 落地页，说明 Kimi Work 是最重要的商业差异化叙事口；自家品牌词也全量买断（防竞品挖词）。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kimi vs chatgpt | 110 | 9 | $6.85 | 信息 | ⭐ 极低 KD，高 CPC 商业价值 |
| kimi alternative | 30 | 0 | $3.91 | 商业 | ⭐⭐⭐ KD=0，有商业意图，CPC $3.91 |
| perplexity alternative | 90 | 11 | $2.83 | 商业 | ⭐ 直接竞品替代词，低竞争 |
| best deep research ai | 480 | 32 | $3.79 | 商业 | ⭐ 品类评测词，高 CPC |
| chatgpt deep research alternative | 20 | 0 | $1.23 | 商业 | ⭐⭐ 近零 KD |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deep research | 8,100 | 59 | $3.69 | 信息 | 主类目词，kimi.com 目前第 4 |
| gemini deep research | 8,100 | 44 | $1.51 | 信息 | Google 品牌词切入点 |
| chatgpt deep research | 5,400 | 69 | $4.54 | 信息 | 高 KD，已被 OpenAI 固守 |
| deep search | 22,200 | 45 | $0.87 | 信息 | 泛化品类词，流量大 |
| ai research assistant | 1,900 | 77 | $3.95 | 信息 | 高 KD，大厂主导 |
| ai research agent | 210 | 15 | $5.29 | 信息 | ⭐ 低 KD，高 CPC，Olares 机会 |
| deep research agent | 210 | 35 | $9.16 | 信息 | 极高 CPC（$9+），强商业信号 |
| perplexity deep research | 1,000 | 55 | $2.93 | 信息 | Perplexity 品牌关联词 |
| openai deep research | 2,400 | 68 | $4.48 | 信息 | 高 KD，OpenAI 固守 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kimi api | 2,900 | 31 | $3.86 | 导航 | ⭐ 相对低 KD，开发者词，高 CPC |
| kimi agent | 260 | 32 | $1.89 | 信息 | ⭐ 低 KD |
| kimi researcher | 210 | 31 | $0 | 信息 | ⭐ 低 KD，但 CPC=0 说明无商业投放 |
| kimi agent swarm | 170 | 30 | $2.32 | 信息 | ⭐ 低 KD，功能差异化词 |
| kimi deep research | 40 | 37 | $1.43 | 信息 | 量小但精准，GEO 潜力 |
| kimi k2 api | 320 | 17 | $2.86 | 商业 | ⭐⭐ 低 KD，API 开发者词 |
| moonshot ai kimi k2.5 | 1,900 | 24 | $0 | 导航 | ⭐ 低 KD，CPC=0 未竞争 |
| kimi-dev-72b | 1,000 | 31 | $5.13 | 信息 | ⭐ 开发者词，CPC 高 |
| kimi ppt | 1,300 | 28 | $0.84 | 商业 | ⭐ 低 KD，PPT 功能词 |
| kimi claw | 1,300 | ~42 | $1.67 | 信息/商业 | 云端 Agent 功能词 |
| kimi moonshot | 320 | 78 | $0.59 | 信息 | 高 KD，品牌导航 |

### 深度研究相关问题词

| 关键词 | 月量 | KD | CPC | 备注 |
|--------|------|----|----|------|
| what is deep research chatgpt | 880 | 61 | $0.32 | 信息教育词 |
| how many deep research queries per month | 720 | 49 | $0 | 限额焦虑词，攻击点 |
| what is deep research | 590 | 53 | $1.53 | 概念科普词 |
| does claude have deep research | 110 | 39 | $0 | ⭐ 低 KD，竞品词 |
| what is gemini deep research | 210 | 17 | $6.51 | ⭐ 极低 KD，高 CPC |
| how long does gemini deep research take | 170 | 32 | $0 | ⭐ 低 KD，性能对比词 |
| how many deep research queries per month gemini | 210 | 37 | $0 | ⭐ 限额焦虑词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deerflow | 590 | 39 | $0 | 信息/商业 | DeerFlow（Olares 已上架平替）直接词 |
| open source deep research | 140 | 47 | $4.71 | 信息 | 量小但 CPC 高，有商业价值 |
| self-hosted deep research | 30 | 0 | $0 | 信息 | ⭐⭐⭐ 近零 KD，高精准场景 |
| open source research agent | 20 | 0 | $0 | 信息 | ⭐⭐⭐ KD=0，GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心叙事切入点：Kimi Researcher 按 token 计费、Deep Research 有月度限额焦虑，DeerFlow 2.0（Olares Market 已上架）提供无限次、数据不出机器的本地化深度研究 Agent 替代——"Zero credit anxiety, full data ownership"。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| kimi alternative | 30 | 0 | $3.91 | KD=0 空白机会：DeerFlow on Olares 是零 credit 限制的开源替代，一键部署 | ⭐⭐⭐ |
| self-hosted deep research | 30 | 0 | $0 | GEO 前哨：DeerFlow+Olares 的准确描述词，无竞争 | ⭐⭐⭐ |
| open source research agent | 20 | 0 | $0 | 语义精准，目前 SERP 几乎空白，进 FAQ/文章抢 AI Overview 引用位 | ⭐⭐⭐ |
| ai research agent | 210 | 15 | $5.29 | 低 KD 高 CPC，DeerFlow 作为开源 AI Research Agent 可排名 | ⭐⭐⭐ |
| kimi vs chatgpt | 110 | 9 | $6.85 | 对比文：ChatGPT/Kimi Deep Research vs DeerFlow 自托管方案 | ⭐⭐ |
| kimi agent swarm | 170 | 30 | $2.32 | DeerFlow 2.0 同样支持 sub-agent 并行，性能对比叙事 | ⭐⭐ |
| best deep research ai | 480 | 32 | $3.79 | 评测圆桌：在 $0/月的 DeerFlow Olares 部署方案里引入对比 | ⭐⭐ |
| deerflow | 590 | 39 | $0 | 直接为 DeerFlow 报告 + Olares Market 页面导流 | ⭐⭐ |
| deep research agent | 210 | 35 | $9.16 | CPC $9+，商业信号极强，DeerFlow+Olares 落地页适合打这个词 | ⭐⭐ |
| open source deep research | 140 | 47 | $4.71 | CPC $4.71 说明有购买意图，DeerFlow 是目前最具代表性的开源方案 | ⭐⭐ |
| how many deep research queries per month | 720 | 49 | $0 | 限额焦虑词：DeerFlow 无限额，Olares 本地运行无 API 成本 | ⭐⭐ |
| perplexity alternative | 90 | 11 | $2.83 | Perplexity 也有 Deep Research，同类目攻击面 | ⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| best deep research ai | 480 | 32 | $3.79 | 商业 | **主词候选** | 量+KD+CPC 三优，可写"Best Deep Research AI Tools"评测，DeerFlow/Olares 占开源席位 |
| ai research agent | 210 | 15 | $5.29 | 信息 | **主词候选** | KD 15 + CPC $5.29，低竞争高价值；DeerFlow 作为开源 AI Research Agent 可排前列 |
| kimi researcher | 210 | 31 | $0 | 信息 | **主词候选** | 品牌功能词，CPC=0 意味尚无竞争性投放；可在 "kimi researcher review / alternative" 上抢跑 |
| deep research agent | 210 | 35 | $9.16 | 信息 | **主词候选** | CPC $9+ 是强商业信号，量虽只 210 但 CPC 暗示商业转化；DeerFlow 落地页核心词 |
| kimi agent swarm | 170 | 30 | $2.32 | 信息 | **主词候选** | 量达软线，KD 30 边缘，差异化功能词；可写"Kimi Agent Swarm vs DeerFlow sub-agents"对比 |
| kimi k2 api | 320 | 17 | $2.86 | 商业 | **主词候选** | 开发者词，KD 17 极低；平台词可带出 Olares API 用例 |
| kimi api | 2,900 | 31 | $3.86 | 导航 | 次级 | 量大但品牌导航，不宜作主词；作为二级词进开发者对比文章 |
| kimi agent | 260 | 32 | $1.89 | 信息 | 次级 | 和 "kimi researcher" 同文章，量合并 |
| kimi deep research | 40 | 37 | $1.43 | 信息 | 次级 | 量小，归入 "kimi researcher" 同文章的次级词 |
| kimi alternative | 30 | 0 | $3.91 | 商业 | 次级 | KD=0 空白，量仅 30；先进"kimi researcher alternative"文章 FAQ |
| kimi vs chatgpt | 110 | 9 | $6.85 | 信息 | 次级 | KD 极低，可并入对比文章，带高 CPC 价值 |
| moonshot ai kimi k2.5 | 1,900 | 24 | $0 | 导航 | 次级 | 低 KD，但 CPC=0，模型信息词，进模型对比文章 |
| self-hosted deep research | 30 | 0 | $0 | 信息 | **GEO** | KD=0，语义精准描述 DeerFlow+Olares，进 FAQ 抢 AI Overview |
| open source research agent | 20 | 0 | $0 | 信息 | **GEO** | 量极小但零竞争，进文章前置段，狙 Perplexity/AI Overview 引用 |
| open source deep research | 140 | 47 | $4.71 | 信息 | 次级 | 量适中，CPC 高，进"best deep research ai"文章的开源段落 |
| deerflow | 590 | 39 | $0 | 信息/商业 | 次级 | DeerFlow 自身关键词，与 DeerFlow 报告联动，进 Olares Market 文章 |
| how many deep research queries per month | 720 | 49 | $0 | 信息 | 次级 | 限额焦虑词，进评测文章对比 Kimi/ChatGPT 限制 vs DeerFlow 无限 |
| what is gemini deep research | 210 | 17 | $6.51 | 信息 | 次级 | KD 17，CPC $6.51，竞品信息词，进 "best deep research" 评测文章 |
| perplexity alternative | 90 | 11 | $2.83 | 商业 | 次级 | 低 KD，同类攻击面，进替代词文章 |

---

## 核心洞见

1. **品牌护城河**：kimi.com 的自然流量 98% 集中在品牌导航词（kimi、kimi k2、kimi ai 等），KD 高达 72-92，**正面刚无意义**。但"Kimi Researcher / Kimi Work"子功能词尚未建立 SEO 心智——`kimi researcher`（210 量，KD 31，CPC=0）是未被品牌主自己放大的词，现在切入成本极低。

2. **可复制的打法**：
   - **买超宽泛词引流**：Kimi 付费买 "free ai"（74K）+ 定向 kimi-work 落地页，流量逻辑是"大漏斗宽进"，不依赖 SEO 精准词；
   - **程序化功能落地页**：kimi.com/en/slides（PPT 功能）→ KD 28，流量 1,280，是成功的功能词 SEO 模板；同样结构的 `/en/deep-research` 落地页理论上可复制；
   - **模型版本词**：每发一版新模型就产生一批低-中 KD 词（kimi-k2.5、kimi-k2.6，KD 44-77 不等），但时效性强。

3. **对 Olares 最关键的词**：
   - `ai research agent`（210，KD 15，CPC $5.29）——KD 最低 + 高 CPC，DeerFlow on Olares 最佳主攻词；
   - `best deep research ai`（480，KD 32，CPC $3.79）——量最高的低竞争品类评测词，引入 DeerFlow 席位；
   - `self-hosted deep research`（30，KD 0）——零竞争、精准描述 Olares 场景，GEO 前哨词。

4. **最大攻击面**：Kimi Deep Research 的**积分限额焦虑**——`how many deep research queries per month`（720 量）是高渗透率焦虑词，CPC=0 说明目前无人系统性攻击；DeerFlow 本地部署"零限额"是最清晰的差异化角度。另一攻击面：Kimi Work 要求**本机开机才能运行**（断电则任务停止），Olares 的 7×24 随时在线是反向叙事点。

5. **隐藏低 KD 金矿**：
   - `kimi vs chatgpt`（110 量，**KD 9**，CPC $6.85）——KD 极低且高 CPC，可快速进首页；
   - `what is gemini deep research`（210 量，**KD 17**，CPC $6.51）——对手品牌信息词，竞品对比文章的长尾填充；
   - `kimi alternative`（30 量，**KD 0**）——字面零竞争，空白可占；
   - `moonshot ai kimi k2.5`（1,900 量，**KD 24**，CPC=0）——高量低 KD，模型信息词。

6. **GEO 前瞻布局**：在深度研究 Agent 评测文章里显式写入以下段落，目标 AI Overview / Perplexity 引用：
   - "Is there a self-hosted deep research agent?" → 指向 DeerFlow + Olares；
   - "open source research agent" → DeerFlow 是迄今最成熟的开源 SuperAgent；
   - "kimi researcher vs open source" → 数据隐私/零 API 成本/无限制叙事。

7. **与既有分析的关联**：
   - `olares-500-keywords` 分析中"AI Agent"方向是核心集群，本报告新增的低 KD 词（`ai research agent` KD 15、`kimi vs chatgpt` KD 9）可直接补入；
   - DeerFlow 已有独立报告（[market/reports/deerflow.md](/Users/pengpeng/seo/directions/market/reports/deerflow.md)），本报告与其形成互引关系——"Kimi Researcher alternative"内容可交叉链接。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、resource_adwords、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*产品信息来源：kimi.com 官网、BigGo Finance（ARR/估值数据）、The Next Web（融资数据），数字以最新报道为准，建议发布前复核官方公告。*
