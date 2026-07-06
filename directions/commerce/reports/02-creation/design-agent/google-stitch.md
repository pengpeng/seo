# Google Stitch SEO 竞品分析报告

> 域名：stitch.withgoogle.com | SEMrush US | 2026-07-06
> Google Stitch = Google Labs 推出的 AI-native UI 设计画布（"vibe design"品类，前身 Galileo AI，文生 UI + Figma 导出一体）

---

## 项目理解（前置）

Google Stitch 是 Google Labs 于 2025 年 Google I/O 发布的 AI 驱动 UI 设计工具，以自然语言描述即可生成多屏高保真界面。2026 年升级为 AI-native 无限画布，引入设计 Agent（实时语音控制、Agent Manager 并行方向管理）、交互原型（Prototypes）、MCP Server（对接 Claude Code / Cursor / Gemini CLI）以及 DESIGN.md——一种将设计系统编码为 Agent 可读 Markdown 的规范，让 AI 编码工具可直接消费设计令牌。底层模型从 Gemini 系列（默认 Gemini 3 Flash，亦可选 3.1 / Nano Banana）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AI-native UI 设计画布，从自然语言→多屏 UI 原型，MCP 直连 AI 编码工具 |
| 开源 / 许可证 | 闭源；Google Labs 实验性产品，免费公测（每日 400 credits 配额） |
| 主仓库 | 无开源仓库；前身 Galileo AI 于 2025 年被 Google 收购 |
| 核心功能 | ① 文/图/代码→高保真 UI 多屏稿；② 实时语音设计协作；③ DESIGN.md 设计系统规范；④ MCP Server 对接编码工具；⑤ 一键导出 Figma / Netlify / Google Antigravity |
| 商业模式 / 定价 | 免费公测（每日 400 credits）；正式定价未公布（Google Labs 实验品，预计未来商业化） |
| 差异化 / 价值主张 | Google 品牌背书 + Gemini 模型原生集成；DESIGN.md 作为 AI Agent 设计-代码桥梁；无门槛（无需设计经验）；MCP 生态打通 |
| 主要竞品（初判）| Figma（含 Figma AI）、Uizard、Framer、Builder.io、v0（Vercel）、Bolt.new |
| Olares Market | 未上架（闭源）；Penpot（开源平替，已上架）可作内容桥接 |
| 来源 | [blog.google/stitch-ai-ui-design](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)；[zapier.com/blog/google-stitch](https://zapier.com/blog/google-stitch/)；[designwhine.com/design-md](https://www.designwhine.com/what-the-hell-is-google-stitchs-design-md/) |

---

## 流量基线（Phase 1）

### 概览

> **说明**：stitch.withgoogle.com 是独立子域名，与 withgoogle.com 主域区分明确，Semrush 将其单独计算。该域名 2025 年底上线，属新品；1,027 个自然词中大量为品牌/误拼变体（"stich"、"sticth"等），非品牌词极稀缺——这是 Google 新产品 SEO 的典型早期形态。

| 指标 | 数据 |
|------|------|
| 域名 | stitch.withgoogle.com |
| SEMrush Rank | **13,547**（新品快速爬升，上线不足一年） |
| 自然关键词数 | 1,027 |
| 月自然流量（US）| **166,687** |
| 自然流量估值 | **$160,294/月** |
| 付费关键词数 | 108 |
| 月付费流量 | 5,556 |
| 月付费流量估值 | $4,275 |
| 排名 1-3 位 | **291 词**（占比 28%，品牌词碾压式第一） |
| 排名 4-10 位 | 71 词 |
| 排名 11-20 位 | 60 词 |

### 子域名流量分布

> Semrush 对 withgoogle.com 主域的子域名查询无返回（数据库限制，新域名）；通过 resource_organic URL 列可见流量主要分布在以下路径：

| 路径 | 代表词 | 流量特征 |
|------|--------|---------|
| stitch.withgoogle.com/（主站） | 99%+ 品牌/拼写变体词 | 绝大多数流量入口 |
| stitch.withgoogle.com/docs | stitch（排名 23 位）| 文档子路径，尚处早期 |
| stitch.withgoogle.com/docs/mcp/setup/ | stitch mcp（排名 1，590 月量）| MCP 技术用户导向，高 CPC $13.45 |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| stitch | 1 | 450,000 | 60 | $0.34 | 59,400 | 混合（缝纫/品牌）| / |
| google stitch | 1 | 27,100 | 53 | $1.53 | 21,680 | 品牌 | / |
| stitch google | 1 | 22,200 | 77 | $1.53 | 17,760 | 品牌 | / |
| google stich（误拼）| 1 | 18,100 | 70 | $1.53 | 14,480 | 品牌误拼 | / |
| stich（误拼）| 1 | 110,000 | 40 | $0.34 | 9,020 | 混合（缝纫/品牌）| / |
| stich google | 1 | 5,400 | 62 | $1.53 | 4,320 | 品牌误拼 | / |
| google stitich（误拼）| 1 | 2,900 | 66 | $0.00 | 2,320 | 品牌误拼 | / |
| stitch ai | 1 | 2,900 | 74 | $2.66 | 2,320 | 品牌 | / |
| google stithc（误拼）| 1 | 2,400 | 41 | $0.00 | 1,920 | 品牌误拼 | / |
| stitch.with google | 1 | 1,900 | 68 | $0.72 | 1,520 | 品牌 | / |
| googl stich（误拼）| 1 | 1,900 | 61 | $0.00 | 1,520 | 品牌误拼 | / |
| stitch with google | 1 | 1,300 | 67 | $0.55 | 1,040 | 品牌 | / |
| stich ai | 1 | 1,300 | 72 | $2.66 | 1,040 | 品牌 | / |
| google stitch ai | 1 | 1,300 | 62 | $1.79 | 1,040 | 品牌/信息 | / |
| stitch design | 1 | 880 | 66 | $2.51 | 704 | 品牌/信息 | / |
| stitch 2.0 | 1 | 880 | 46 | $3.14 | 704 | 品牌 | / |
| stitch（文档）| 23 | 450,000 | 60 | $0.34 | 675 | 混合 | /docs |
| **stitch mcp** | **1** | **590** | **40** | **$13.45** | **472** | **信息** | **/docs/mcp/setup/** |
| stitch balloon | 1 | 720 | 22 | $0.40 | 576 | 信息 | / |
| google ai design | 1 | 260 | 77 | $1.14 | 208 | 品牌/信息 | / |
| what is stitch | — | 1,900 | 53 | $0.06 | — | 信息 | — |
| google stitch mcp | — | 260 | 37 | $4.78 | — | 信息 | — |
| google stitch price | — | 390 | 37 | $0.00 | — | 信息 | — |
| is google stitch free | — | 170 | 50 | $0.00 | — | 信息 | — |

> **洞察**：自然流量 ~95% 来自品牌/误拼词（"stich"、"sticth"等大量 typo 变体），非品牌词几乎为零。"stitch mcp"是目前唯一高 CPC（$13.45）且 KD 适中（40）的非品牌词，指向开发者/技术受众切入口。

### 付费词（Google Ads，按流量排序）

Google 对 Stitch 仅买了自己的品牌词（108 个词，5,556 付费流量），全部导向主站。策略是品牌词防御型广告——说明 Google 认为 Stitch 现阶段仍靠品牌认知获客，无需购买品类词。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| google stitch | 1 | 22,200 | $0.74 | stitch.withgoogle.com |
| stitch google | 1 | 18,100 | $0.74 | stitch.withgoogle.com |
| google stich（误拼）| 1 | 18,100 | $0.74 | stitch.withgoogle.com |
| stich google | 1 | 5,400 | $1.53 | stitch.withgoogle.com |
| google stitich（误拼）| 1 | 2,900 | $0.00 | stitch.withgoogle.com |
| stitch ai | 1 | 2,900 | $3.48 | stitch.withgoogle.com |
| stitch 2.0 | 1 | 590 | $0.50 | stitch.withgoogle.com |

> 广告 copy：「Google Stitch: AI Design Tool」+「Stitch: Your AI vibe design partner. Turn your ideas into interactive apps.」

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| uizard | 6,600 | 44 | $4.08 | 信息/商业 | AI UI 工具直接竞品 |
| figma alternatives | 1,000 | 21 | $2.51 | 信息 | ⭐ 高机会，广泛替代需求 |
| framer alternative | 110 | **6** | $5.07 | 信息 | ⭐⭐ 极低 KD |
| penpot vs figma | 210 | **13** | $2.59 | 信息/商业 | ⭐⭐ 极低 KD，Olares 机会 |
| uizard alternative | 30 | **5** | $9.33 | 信息 | ⭐⭐ 极低 KD |
| figma competitor | 40 | **13** | $3.37 | 信息 | ⭐⭐ 极低 KD |
| galileo ai alternative | 20 | 0 | $3.75 | 信息 | ⭐ 近零 KD |
| google stitch alternative | 20 | 0 | $4.04 | 信息 | ⭐ 刚性需求，GEO 前哨 |
| figma alternative | 480 | 29 | $2.77 | 信息 | ⭐ KD 29，主词候选区间 |
| figma alternative free | 10 | 0 | $2.19 | 信息 | ⭐ GEO |
| figma alternative open source | 10 | 0 | $0.99 | 信息 | ⭐ Olares 正面 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| figma ai | 9,900 | 84 | $3.21 | 品牌 | 高竞争，Figma 主场 |
| ai website builder | 22,200 | 76 | $11.84 | 信息 | 竞争激烈 |
| ai design generator | 5,400 | 66 | $1.87 | 信息 | 偏大 KD |
| ai mockup generator | 720 | 44 | $2.63 | 信息/商业 | ⭐ 中等机会 |
| ai wireframe generator | 480 | 38 | $5.93 | 信息 | ⭐ 机会词 |
| ai design tool | 480 | 54 | $3.32 | 信息 | 中等 KD |
| ai ux design | 390 | 49 | $5.31 | 信息 | 信息意图 |
| vibe design | 390 | 31 | $3.76 | 信息 | ⭐ 新兴 2026 词 |
| wireframe ai | 390 | 38 | $4.88 | 信息 | ⭐ 机会词 |
| ui design tools | 1,000 | 38 | $4.27 | 信息 | ⭐ 工具比较词 |
| ai prototype generator | 320 | 39 | $9.28 | 信息 | ⭐ 高 CPC 机会 |
| ai design agent | 320 | 41 | $5.78 | 信息 | 新兴词，符合 Stitch 定位 |
| ui generator ai | 170 | 48 | $5.87 | 信息 | 中等机会 |
| ai for product design | 170 | 23 | $3.97 | 信息 | ⭐ KD 低 |
| best ai design tool | 50 | 37 | $4.66 | 信息 | ⭐ 选型类内容机会 |
| ai ui design tool | 50 | 62 | $4.81 | 信息 | 精准但 KD 高 |
| text to ui | 30 | 60 | $3.47 | 信息 | Stitch 核心功能词 |
| ai prototyping tool | 40 | 31 | $7.16 | 信息 | ⭐ KD 低，高 CPC |
| design system ai | 30 | 25 | $4.28 | 信息 | ⭐ DESIGN.md 相关词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google stitch | 22,200 | 53 | $1.53 | 品牌 | 核心品牌词 |
| stitch ai | 2,900 | 74 | $2.66 | 品牌 | 品牌意图为主 |
| stitch mcp | 590 | 40 | **$13.45** | 信息 | ⭐ 高 CPC！开发者词 |
| google stitch mcp | 260 | 37 | $4.78 | 信息 | ⭐ MCP 生态词 |
| what is google stitch | 260 | 61 | $0.40 | 信息 | 认知普及词 |
| google stitch price | 390 | 37 | $0.00 | 信息 | ⭐ 定价询问 |
| is google stitch free | 170 | 50 | $0.00 | 信息 | 定价询问变体 |
| stitch 2.0 | 880 | 46 | $3.14 | 品牌 | 版本词 |
| google stitch ai ui design tool | 140 | 58 | $2.85 | 品牌/信息 | 长尾精准词 |
| stitch design | 880 | 66 | $2.51 | 品牌/信息 | 偏品牌 |
| stitch ai design | 40 | 0 | $1.98 | 信息 | ⭐ GEO 前哨 |
| vibe design | 390 | 31 | $3.76 | 信息 | 新兴设计范式词 |
| design md | 70 | 0 | $6.36 | 信息 | ⭐ DESIGN.md 规范词 |
| google stitch api | 90 | 0 | $5.46 | 信息 | ⭐ 开发者词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| penpot | 5,400 | 59 | $1.77 | 品牌 | Olares 已上架，核心替代 |
| open source figma | 70 | 33 | $0.75 | 信息 | ⭐ 低 KD，Penpot 机会 |
| self-hosted figma | 20 | 0 | $0.00 | 信息 | ⭐ GEO，直指 Penpot |
| figma alternative open source | 10 | 0 | $0.99 | 信息 | ⭐ Olares 正面切入 |
| penpot vs figma | 210 | **13** | $2.59 | 信息/商业 | ⭐⭐ 极低 KD，主词候选 |
| penpot self-hosted | 20 | 0 | $0.00 | 信息 | ⭐ Penpot on Olares 直接词 |
| penpot docker | 20 | 0 | $0.00 | 信息 | ⭐ 技术用户自部署词 |
| penpot review | 20 | 0 | $0.00 | 信息 | ⭐ 评测类内容机会 |
| penpot pricing | 20 | 0 | $0.00 | 信息 | ⭐ 付费询问 |
| open source ux design | 20 | 0 | $0.00 | 信息 | ⭐ GEO |

---

## Olares 关联词（Phase 3）

**核心叙事**：Stitch 是闭源、数据进 Google 服务器、使用 credits 配额受限；Penpot 是同等级的开源 UI 设计协作工具，Olares 一键自部署→设计资产本地永久留存；Open Design / AI 工作流用 ComfyUI on Olares 可补充生图能力，面向更在意数据主权和无限使用的设计师与开发者。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| figma alternatives | 1,000 | 21 | $2.51 | ⭐⭐⭐ 「Penpot on Olares = 自托管 Figma 替代」主词切入 |
| penpot vs figma | 210 | 13 | $2.59 | ⭐⭐⭐ 极低 KD，Olares Market 已上架 Penpot，最直接攻击面 |
| penpot | 5,400 | 59 | $1.77 | ⭐⭐ 品牌流量大，Olares 部署教程可借力 |
| figma alternative | 480 | 29 | $2.77 | ⭐⭐⭐ 高意图替代词，Penpot + Olares = 唯一可自托管替代 |
| open source figma | 70 | 33 | $0.75 | ⭐⭐⭐ Penpot is open-source Figma；Olares 一键装 |
| self-hosted figma | 20 | 0 | $0.00 | ⭐⭐⭐ GEO：「How to self-host Figma alternative with Olares」 |
| framer alternative | 110 | 6 | $5.07 | ⭐⭐ KD 极低，Penpot/Olares 替代叙事可覆盖 |
| figma competitor | 40 | 13 | $3.37 | ⭐⭐ KD 极低，文章可并入 figma alternatives 簇 |
| ai wireframe generator | 480 | 38 | $5.93 | ⭐⭐ 信息意图，可介绍 Stitch vs Penpot AI 功能对比 |
| vibe design | 390 | 31 | $3.76 | ⭐⭐ 2026 新兴词，Olares 可作「私有 vibe design 基础设施」叙事 |
| stitch mcp | 590 | 40 | $13.45 | ⭐⭐ 开发者向，MCP 协议 + Olares 本地 AI 工具链结合叙事 |
| google stitch alternative | 20 | 0 | $4.04 | ⭐⭐⭐ GEO 刚性需求，直接答：Penpot on Olares |
| figma alternative open source | 10 | 0 | $0.99 | ⭐⭐⭐ GEO，内容 = Penpot + Olares 装机指南 |
| penpot self-hosted | 20 | 0 | $0.00 | ⭐⭐⭐ Olares Market 装 Penpot 的精准词 |
| ai prototyping tool | 40 | 31 | $7.16 | ⭐⭐ 高 CPC，本地 AI 原型工具叙事 |
| design system ai | 30 | 25 | $4.28 | ⭐⭐ DESIGN.md 概念可延伸到私有设计系统管理 |
| will ai replace designers | 40 | 39 | $0.00 | ⭐ 信息意图热点；Olares 叙事：AI 设计工具本地化=设计师数据自主 |
| penpot docker | 20 | 0 | $0.00 | ⭐⭐ Olares 替代 Docker 自部署，更简单 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| figma alternatives | 1,000 | 21 | $2.51 | 信息 | **主词候选** | KD 21、月量 1K，完整替代选型文章，Penpot on Olares = 唯一可自托管方案 |
| penpot vs figma | 210 | 13 | $2.59 | 信息/商业 | **主词候选** | KD 极低，高意图对比词；可以 Olares Market 为核心写「私有化设计协作」文 |
| figma alternative | 480 | 29 | $2.77 | 信息 | **主词候选** | KD 29 适中，与 figma alternatives 合并成簇 |
| ai wireframe generator | 480 | 38 | $5.93 | 信息 | **主词候选** | KD 38，高 CPC $5.93；信息意图，可写 Stitch vs Penpot vs Uizard 横评 |
| stitch mcp | 590 | 40 | $13.45 | 信息 | **主词候选** | CPC 极高 $13.45，开发者精准词；MCP + 本地 AI 编码工具链文章 |
| uizard | 6,600 | 44 | $4.08 | 信息/商业 | **主词候选** | 量大 KD 尚可；Stitch/Penpot/Uizard 三向对比可带巨大流量 |
| framer alternative | 110 | 6 | $5.07 | 信息 | **主词候选** | KD=6 是罕见金矿，量 110；并入 figma alternatives 文或独立一篇 |
| vibe design | 390 | 31 | $3.76 | 信息 | **主词候选** | 2026 新兴词；Stitch 发明、Olares 可做「私有 vibe design 基础」叙事 |
| ai prototype generator | 320 | 39 | $9.28 | 信息 | **主词候选** | CPC $9.28，高商业价值；信息意图内容可带长尾 |
| google stitch | 22,200 | 53 | $1.53 | 品牌 | 次级 | 品牌导航词，排不动；监测、引用为主 |
| figma competitor | 40 | 13 | $3.37 | 信息 | 次级 | KD 极低；并入 figma alternatives 文 |
| ai for product design | 170 | 23 | $3.97 | 信息 | 次级 | KD 低，量适中；可并入工具选型文章 |
| open source figma | 70 | 33 | $0.75 | 信息 | 次级 | Penpot on Olares 精准次级词 |
| design system ai | 30 | 25 | $4.28 | 信息 | 次级 | DESIGN.md 概念延伸词 |
| google stitch mcp | 260 | 37 | $4.78 | 信息 | 次级 | stitch mcp 主词的次级长尾 |
| google stitch price | 390 | 37 | $0.00 | 信息 | 次级 | 定价询问；可在工具对比文中并入 |
| ai prototyping tool | 40 | 31 | $7.16 | 信息 | 次级 | 高 CPC，信息意图；并入原型工具对比 |
| google stitch alternative | 20 | 0 | $4.04 | 信息 | **GEO** | 近零 KD，直接回答：Penpot on Olares |
| self-hosted figma | 20 | 0 | $0.00 | 信息 | **GEO** | 精准意图，抢 AI Overview 引用位 |
| figma alternative open source | 10 | 0 | $0.99 | 信息 | **GEO** | GEO 前哨；内容 = Penpot + Olares 指南 |
| penpot self-hosted | 20 | 0 | $0.00 | 信息 | **GEO** | Olares Market 装 Penpot 最精准词 |
| stitch ai design | 40 | 0 | $1.98 | 信息 | **GEO** | GEO 前哨，回答「什么是 Stitch AI 设计」 |
| design md | 70 | 0 | $6.36 | 信息 | **GEO** | DESIGN.md 规范词，高 CPC；开发者新概念词 |
| google stitch api | 90 | 0 | $5.46 | 信息 | **GEO** | 开发者词，高 CPC；MCP/API 文档延伸 |
| uizard alternative | 30 | 5 | $9.33 | 信息 | **GEO** | KD=5，CPC $9.33；小量但高意图，并入替代词文 |

---

## 核心洞见

### 1. 品牌护城河

Google Stitch 自然流量 **95%+ 是品牌/误拼词**，品牌心智由 Google 大名背书，短期内正面刚毫无意义。但 Stitch 本身在非品牌词上**几乎没有任何排名**——这意味着它的 SEO 机会全在品牌词（护城河），品类词（ai design tool、ai wireframe generator 等）目前基本没做内容，对外部内容创作者留了窗口期。

### 2. 可复制的打法

Stitch 目前几乎没有内容 SEO 策略（仅一个 /docs 路径初具规模），完全靠 Google 品牌自然流量。值得复制的打法：
- **MCP 技术词**：`stitch mcp` CPC $13.45，开发者受众高价值——教程/集成文章可快速建立技术权威
- **对比类文章**（`figma alternatives`、`penpot vs figma`、`framer alternative`）：KD 极低（6-21），这类词 Stitch 自身不做，外部可以 Penpot on Olares 为答案写一篇撑起流量
- **"vibe design"**：Stitch 自己创造了这个词，但没有内容化——可以作为趋势词先手布局

### 3. 对 Olares 最关键的词

1. **`penpot vs figma`**（KD=13，月量 210）——最低阻力主词，Olares 正面叙事：Penpot 是开源 Figma 替代、一键装 Olares
2. **`figma alternatives` / `figma alternative`**（KD=21/29，月量 1K/480）——高流量入口，可写「Best Figma Alternatives 2026」，Penpot on Olares 作核心推荐
3. **`stitch mcp`**（KD=40，月量 590，CPC $13.45）——开发者词，Olares 本地 AI 工具链叙事：MCP + 本地 LLM + Penpot

### 4. 最大攻击面

- **闭源 + Credits 配额**：Stitch 每日 400 credits 限制是明显痛点；`google stitch price`、`is google stitch free` 两词月均 170-390 有量，说明用户在询问定价——内容回答「Stitch 要多少 credits + 免费替代是 Penpot」可精准截流
- **数据主权**：设计数据上传 Google 服务器；`self-hosted figma`、`figma alternative open source` 等词虽量小但意图精准，有隐私顾虑的企业/开发者是切入口
- **Google Labs 实验性产品不确定性**：Galileo AI 被收购后品牌归 Google，用户担心产品持续性（历史上 Google 砍产品记录），这是内容可以放大的叙事

### 5. 隐藏低 KD 金矿

| 词 | 月量 | KD | 为什么是金矿 |
|----|------|----|----|
| framer alternative | 110 | **6** | 最低 KD 主词候选，排名门槛极低 |
| penpot vs figma | 210 | **13** | KD 13 却有强商业意图和 CPC |
| figma competitor | 40 | **13** | 可并入 figma alternatives 无额外成本 |
| uizard alternative | 30 | **5** | CPC $9.33，高意图词，极低 KD |
| stitch mcp / google stitch mcp | 590/260 | 40/37 | CPC $13.45/$4.78，开发者精准词，目前几乎无内容竞争 |

### 6. GEO 前瞻布局

以下近零量词在 AI Overview / Perplexity / ChatGPT 搜索中高度相关，适合写 FAQ 段落抢引用位：
- `google stitch alternative`（直接答：Penpot on Olares）
- `self-hosted figma`（答：Penpot is the self-hosted Figma alternative）
- `design md`（解释 DESIGN.md 规范及 Olares 私有设计工作流）
- `stitch ai design`（解释 Stitch 是什么 + 开源替代路线）
- `can ai replace ui ux designer`（信息意图大词，AI 取代设计师焦虑词，量小但 GEO 引用热点）

### 7. 与既有分析的关联

- 与 `olares-500-keywords` 词表关联：Penpot 类词（`penpot`、`penpot vs figma`）目前未出现在 Olares 500 词表中，本报告新增两个主词候选填补这一空缺
- `figma alternatives`（KD=21）与已有方向"Market 应用竞品报告"高度协同——Penpot 已在 Olares Market 上架，可直接串联现有资产
- `stitch mcp`（CPC $13.45）与"AI Agent / MCP Server"技术趋势词高度一致，可与 tech/ 方向报告联动，补充 AI 工具链叙事

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、resource_adwords、phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
*项目理解来源：blog.google、zapier.com、designwhine.com（标注于项目理解节）。*
