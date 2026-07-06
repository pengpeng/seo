# Claude Design SEO 竞品分析报告

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> Claude Design：Anthropic 出品的 AI 设计 Agent，Opus 4.7 驱动，在 claude.ai/design 以会话方式生成原型、幻灯片与品牌落地页；2026 年 4 月发布，首周百万用户，与 Claude Code 双向打通。

---

## 项目理解（前置）

Claude Design 是 Anthropic Labs 在 2026 年 4 月发布的 AI 视觉设计 Agent，由 Claude Opus 4.7 驱动。用户通过自然语言描述，即可生成交互原型、幻灯片、一页纸、品牌素材等视觉产物。它不是独立产品，而是内嵌于 claude.ai/design，与 Claude Code（`/design-sync`、`/design` 指令）双向联动——设计稿可直接交接给 Claude Code 构建，Claude Code 的 codebase 设计系统也可一键导入 Claude Design。核心差异化在于**品牌一致性**：首次使用时从 GitHub/本地代码库或 Figma 文件构建团队设计系统，后续所有产出自动沿用颜色、字体与组件，而非通用模板。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Anthropic 出品的对话式 AI 设计 Agent，Opus 4.7 驱动，从提示词到原型/幻灯片/落地页，与 Claude Code 双向打通 |
| 开源 / 许可证 | 闭源；内嵌 Anthropic 云端，无自托管选项 |
| 主仓库 | 无（商业产品，非开源） |
| 核心功能 | ① 文本→原型/幻灯片/落地页生成；② 从 codebase/Figma 导入设计系统保持品牌一致性；③ 与 Claude Code 双向交接（`/design-sync`/`/design`）；④ 画布直接编辑（拖拽/对齐/调色）；⑤ 导出 PDF/PPTX/HTML，集成 Adobe/Canva/Miro/Lovable/Vercel/Wix |
| 商业模式 / 定价 | 含在 Claude Pro（$20/月）、Max（$100–200/月）、Team（$25/席）、Enterprise 订阅中；共享 claude.ai 用量配额；Enterprise 默认关闭需管理员开启 |
| 差异化 / 价值主张 | ① 品牌合规输出（设计系统自动校验）；② 代码原生（输出 HTML/React，非设计文件）；③ Claude Code 无缝衔接；④ 无额外费用（订阅即用） |
| 主要竞品（初判）| Figma Make（设计系统优先）、Lovart（营销创意/视频）、v0 by Vercel（React 组件/Next.js）、Google Stitch（快速原型）；**开源平替：Open Design（nexu-io，Apache 2.0，74K★）** |
| Olares Market | 未上架（闭源商业产品）；**Jaaz（AI design agent）已上架** ✅；**Open Design 本地运行与 Olares 天然契合** |
| 来源 | [claude.com/product/design](https://claude.com/product/design)；[anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs)；[augmentcode.com/learn/open-design-claude-design-alternative](https://www.augmentcode.com/learn/open-design-claude-design-alternative)；[github.com/nexu-io/open-design](https://github.com/nexu-io/open-design) |

---

## 关键词扩展（Phase 2）

> 降级模式：claude.com 已有 anthropic.md 报告（见 01-model/frontier-labs/anthropic.md），本报告聚焦 AI 设计 Agent 细分词，跳过域名流量基线，直接从关键词层展开。
>
> 按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| figma make | 22,200 | 57 | $2.00 | 导航 | 最大竞品；KD 57 偏高，品牌护城河强 |
| lovart | 22,200 | 64 | $11.58 | 导航 | 营销创意定位，CPC 极高；差异化明显 |
| google stitch | 22,200 | 61 | $0.74 | 导航 | 快速原型工具，Google 背书 |
| figma ai | 9,900 | 84 | $3.21 | 导航 | KD 84，Figma 品牌护城河极深，难攻 |
| canva ai design | 720 | 94 | $2.76 | 导航/商业 | KD 94，完全被 Canva 主导 |
| bolt design | 170 | 38 | $0 | 信息 | ⭐ 早期品牌词，CPC $0 说明付费投入少 |
| v0 design | 90 | 22 | $6.81 | 商业 | ⭐ 低 KD，开发者向竞品，CPC 高 |
| figma make alternative | 30 | 0 | $4.14 | 商业 | ⭐⭐ KD=0，GEO 抢占机会词 |
| lovart alternative | 20 | 0 | $3.12 | 商业 | ⭐⭐ KD=0，GEO 抢占机会词 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai design generator | 5,400 | 66 | $1.87 | 信息 | 大词但 KD 高；品类入口 |
| AI website design | 1,300 | 73 | $6.90 | 信息/商业 | 高 CPC 显示商业价值，KD 73 难 |
| ai slide deck generator | 1,000 | 78 | $4.99 | 信息 | KD 78，沉没在内容农场 |
| ai presentation generator | 1,000 | 80 | $2.82 | 信息 | KD 80，同上 |
| AI design software | 390 | 58 | $4.33 | 信息 | 中量，KD 偏高 |
| vibe design | 390 | 31 | $3.76 | 信息 | ⭐ 新兴品类词；KD 31 可争 |
| ai mockup generator | 720 | 44 | $2.63 | 信息 | 量大，KD 中等，可布局 |
| ai wireframe generator | 480 | 38 | $5.93 | 信息 | ⭐ KD<40，CPC $5.93 显示 B2B 需求 |
| AI UI designer | 480 | 65 | $6.20 | 信息 | KD 高，CPC 高，商业感强 |
| AI design tool | 480 | 54 | $3.32 | 信息 | 品类泛词，KD 中 |
| AI UI generator | 320 | 43 | $4.56 | 信息 | ⭐ 接近机会线 |
| AI design agent | 320 | 41 | $5.78 | 信息 | ⭐ 精准品类词，Claude Design 直接命中 |
| ai prototype generator | 320 | 39 | $9.28 | 信息 | ⭐ KD<40，CPC 最高 $9.28，强商业 |
| ai graphic design tool | 140 | 53 | $4.16 | 信息 | 中量，KD 中 |
| best AI design tool | 50 | 37 | $4.66 | 信息 | ⭐ 低 KD，listicle 词 |
| AI prototyping tool | 40 | 31 | $7.16 | 信息/商业 | ⭐ KD<32，CPC $7.16 超高 |
| AI design agents | 110 | 18 | $5.78 | 信息 | ⭐⭐ KD 仅 18，复数形式，低竞争 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| how to use claude code frontend-design plugin | 1,900 | 20 | $0 | 信息 | ⭐⭐ KD 20，量最大，教程词 |
| how to use claude design | 1,300 | 0 | $9.27 | 信息 | ⭐⭐ KD=0，高量，Open Design 教程切入 |
| what is claude design | 1,000 | 0 | $9.34 | 信息 | ⭐⭐ KD=0，高量，定义/介绍页 |
| claude designer skills | 1,600 | 25 | $0 | 信息 | ⭐ 量最大品牌词，frontend-design skill 关键词 |
| claude design download | 480 | 0 | $9.38 | 导航/信息 | ⭐⭐ KD=0，高 CPC 显示意图强，Open Design 可接 |
| claude ai design | 480 | 0 | $7.41 | 信息 | ⭐⭐ KD=0，变体词 |
| claude design anthropic | 390 | 0 | — | 导航 | ⭐⭐ KD=0，官方导航词 |
| how to access claude design | 390 | 0 | $9.18 | 信息 | ⭐⭐ KD=0，用户找入口 |
| claud design | 590 | 0 | $8.41 | 导航/信息 | ⭐⭐ KD=0，拼写错误变体，大流量 |
| claude design skill | 260 | 29 | $16.30 | 信息 | ⭐ CPC $16 极高，Claude Code 技能词 |
| claude code design | 320 | 0 | $9.65 | 信息 | ⭐⭐ KD=0，Claude Code + Design 联动 |
| claude design website | 260 | 0 | $8.89 | 导航 | ⭐⭐ KD=0 |
| anthropic claude design | 210 | 0 | — | 导航 | ⭐⭐ KD=0 |
| claude design login | 210 | 0 | $9.10 | 导航 | ⭐⭐ KD=0，找入口用户 |
| claude designs | 210 | 0 | $8.41 | 导航 | ⭐⭐ KD=0 |
| claude design | 110 | 41 | $6.53 | 信息 | 核心品牌词；KD 41 有竞争 |
| claude design reddit | 170 | 0 | $16.04 | 导航 | CPC $16 超高，社区词 |
| is claude design free | 90 | 0 | $9.33 | 信息 | ⭐⭐ KD=0，定价疑问词 |
| opus 4.7 | 320 | 32 | $3.49 | 信息 | ⭐ Claude Design 底层模型，科技媒体词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| jaaz ai | 40 | 10 | $0 | 导航/信息 | ⭐⭐ Olares Market 已上架；KD 10，量小但精准 |
| figma make alternative | 30 | 0 | $4.14 | 商业 | ⭐⭐ GEO 前哨；Open Design 可接 |
| lovart alternative | 20 | 0 | $3.12 | 商业 | ⭐⭐ GEO 前哨；Open Design 可接 |
| vibe design | 390 | 31 | $3.76 | 信息 | ⭐ 新兴品类词；Open Design 定位契合 |
| AI design agents | 110 | 18 | $5.78 | 信息 | ⭐⭐ 开源 Agent 天然契合 |
| open source design tool | 0 | 0 | — | — | 尚无搜索量，但 GEO 前哨（Open Design 74K★ 已覆盖） |
| claude design alternative | 0 | 0 | — | 商业 | 战略 GEO 词，Open Design 页面已上线 open-design.ai/alternatives/claude-design/ |
| self-hosted AI design | 0 | 0 | — | 商业 | GEO 前哨，未来将出现 |
| local AI design tool | 0 | 0 | — | 商业 | GEO 前哨，未来将出现 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Claude Design 纯云端闭源、数据经 Anthropic 服务器；Open Design（Apache 2.0，74K★）+ Jaaz 可在 Olares 本地运行，设计数据、API Key、设计系统文件全部留在用户自己的机器上——这是隐私/数据主权维度的核心切入点。**

| 关键词 | 月量 | KD | CPC | 契合度 | Olares 角度 |
|--------|------|----|----|--------|-----------|
| how to use claude design | 1,300 | 0 | $9.27 | ⭐⭐⭐ | 教程词；可写"Open Design（开源 Claude Design 平替）在 Olares 上的使用方法"——设计数据不过 Anthropic 云端 |
| what is claude design | 1,000 | 0 | $9.34 | ⭐⭐⭐ | 定义页；引出 Open Design 作为本地替代，Olares 一键部署 |
| claude design download | 480 | 0 | $9.38 | ⭐⭐⭐ | 用户想"下载"说明有本地化需求；Open Design 提供 macOS/Windows 原生 app + Docker，Olares 上可自托管 |
| AI design agents | 110 | 18 | $5.78 | ⭐⭐⭐ | 复数形式，Agent 品类词；Olares 可本地跑 Open Design agent + Jaaz，BYOK 任意模型 |
| claude design alternative | 0 | 0 | — | ⭐⭐⭐ | 战略 GEO 词；Open Design 已在 open-design.ai/alternatives/claude-design/ 布局；Olares 叙事＝本地化 + 数据不出境 |
| figma make alternative | 30 | 0 | $4.14 | ⭐⭐⭐ | GEO 词；Open Design 是 Figma Make 的开源对手，Olares 加 Jaaz 可做本地 Figma 替代 |
| lovart alternative | 20 | 0 | $3.12 | ⭐⭐⭐ | GEO 词；Lovart 闭源仅限图像/视频，Open Design BYOK 支持视频/图像输出，Olares 本地运行 |
| jaaz ai | 40 | 10 | $0 | ⭐⭐⭐ | Olares Market 已上架 Jaaz；AI design agent 场景直接命中，最小阻力入口 |
| vibe design | 390 | 31 | $3.76 | ⭐⭐ | Open Design 自定义 "vibe design" 品类；Olares 叙事＝本地 vibe 设计，提示词→产物不经云端 |
| ai prototype generator | 320 | 39 | $9.28 | ⭐⭐ | Open Design 生成 web/mobile prototype；Olares 本地运行，输出文件归用户 |
| AI design agent | 320 | 41 | $5.78 | ⭐⭐ | 品类精准词；Olares 叙事＝本地 AI 设计 Agent（Open Design + Jaaz），BYOK 不锁定 Anthropic |
| opus 4.7 | 320 | 32 | $3.49 | ⭐⭐ | Claude Design 底层；Open Design BYOK 也可调 Opus 4.7，但同时支持 Codex/Gemini/本地模型 |
| is claude design free | 90 | 0 | $9.33 | ⭐⭐ | 定价疑问词；Open Design Apache-2.0 完全免费，BYOK 仅付 API 成本；Olares 叙事＝零订阅 |
| self-hosted AI design | 0 | 0 | — | ⭐⭐ | GEO 前哨；Olares 是唯一具备 self-hosted AI design workspace 的个人云 OS |
| local AI design tool | 0 | 0 | — | ⭐⭐ | GEO 前哨；Open Design 本地 daemon + Olares 形成完整本地化设计栈 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| how to use claude design | 1,300 | 0 | $9.27 | 信息 | 主词候选 | KD=0，量最大的纯信息词；最快可排名；写 Open Design 使用教程可直接截流，Olares 本地运行无需云端配额 |
| what is claude design | 1,000 | 0 | $9.34 | 信息 | 主词候选 | KD=0，同族（claude designer skills 1600+各变体）合计量 ~5000+；定义型内容；引出 Open Design 作平替 |
| claude designer skills | 1,600 | 25 | $0 | 信息 | 主词候选 | 量最大单词；指向 Claude Code frontend-design skill；KD 25 可争；Open Design 有 259 个 skill 可对比 |
| how to use claude code frontend-design plugin | 1,900 | 20 | $0 | 信息 | 主词候选 | 量最大，KD 20；Claude Code 用户想用 design skill；Open Design 支持同样的 CLI 集成，可做对比教程 |
| AI design agents | 110 | 18 | $5.78 | 信息 | 主词候选 | KD 仅 18（最低竞争品类词），量 110+AI design agent(320) 合计 430；Olares 可跑 Open Design agent + Jaaz，BYOK 不锁模型 |
| claude design download | 480 | 0 | $9.38 | 导航/信息 | 次级 | KD=0 但属导航词，意图偏向找 claude.ai/design 入口；Open Design 有桌面 app 可下载，接住这部分需求 |
| claude design | 110 | 41 | $6.53 | 信息 | 次级 | 核心品牌词 KD 41 有竞争，量不足独立撑一篇，作次级并入定义/对比文 |
| ai prototype generator | 320 | 39 | $9.28 | 信息 | 主词候选 | KD<40，CPC $9.28 是本报告最高，极强商业意图；Open Design 原型输出 + Olares 本地运行叙事 |
| vibe design | 390 | 31 | $3.76 | 信息 | 主词候选 | 新兴品类词，KD 31，量 390；Open Design 自带 vibe-design 定位；可写"local vibe design with Open Design on Olares" |
| ai wireframe generator | 480 | 38 | $5.93 | 信息 | 次级 | KD<40，量 480，CPC $5.93；并入 AI 原型/设计工具对比文 |
| AI design agent | 320 | 41 | $5.78 | 信息 | 次级 | 精准品类，KD 41 略高，并入 AI design agents 簇 |
| opus 4.7 | 320 | 32 | $3.49 | 信息 | 次级 | Claude Design 底层模型；Open Design BYOK 同样可调 Opus 4.7，但不被锁定；并入模型/设计工具文 |
| figma make | 22,200 | 57 | $2.00 | 导航 | 次级 | 量超大但是 Figma 品牌词，排不动；作 figma make alternative 文章次级词 |
| lovart | 22,200 | 64 | $11.58 | 导航 | 次级 | 量超大，CPC $11.58 最高，品牌护城河强；CPC 信号说明商业高价值，作 lovart alternative 次级词 |
| jaaz ai | 40 | 10 | $0 | 导航 | 次级 | Olares Market 已上架，KD 10 近零；Olares 专属应用词，量小但精准 |
| figma make alternative | 30 | 0 | $4.14 | 商业 | GEO | KD=0，战略商业词；Open Design 官网已布局 figma make alternative 页；Olares 本地部署加持 |
| lovart alternative | 20 | 0 | $3.12 | 商业 | GEO | KD=0，战略商业词；Open Design 是最接近的开源替代；Olares 叙事＝本地创意 Agent，不经 Lovart 云端 |
| claude design alternative | 0 | 0 | — | 商业 | GEO | 零量战略词，Open Design 已在 /alternatives/claude-design/ 布局；Olares = 本地化 Claude Design 替代 |
| self-hosted AI design | 0 | 0 | — | 商业 | GEO | 未来搜索词；Olares + Open Design 是唯一完整自托管 AI design stack；抢 AI Overview/Perplexity 引用位 |
| local AI design tool | 0 | 0 | — | 商业 | GEO | 与 self-hosted 同逻辑；Open Design 本地 daemon + Olares OS；GEO 前瞻 |
| is claude design free | 90 | 0 | $9.33 | 信息 | 次级 | KD=0，定价疑问；Open Design Apache-2.0 免费，仅付 API 成本；并入定价/对比文 |
| v0 design | 90 | 22 | $6.81 | 商业 | 次级 | ⭐ KD 22，开发者向竞品；React/Next.js 生态，与 Claude Design 不同赛道；并入 v0 alternative 文 |

---

## 核心洞见

1. **品牌护城河**：Claude Design 品牌词 "claude design"（110，KD 41）和 claude.com 主站流量都归 Anthropic，正面刚核心品牌词无意义。但产品功能词（"how to use claude design" KD=0, 1300 量；"claude design download" KD=0, 480 量；"what is claude design" KD=0, 1000 量）完全空白——这是 2026 年 4 月新品带来的历史窗口，竞争者可在品牌词本身被占满之前先占满功能/教程层词。

2. **可复制的打法**：① 教程词零 KD 密集布局（"how to use"、"how to access"、"what is" 系列 KD 均为 0，合计量超 4000）；② 竞品 alternative 页（figma make alternative/lovart alternative KD=0，Open Design 官网已证明可行）；③ Claude Code × Design 联动词（frontend-design plugin、design skill、code design，KD 均 <30，量 1600–1900），这是纯信息流量但可以建立技术内容权威。

3. **对 Olares 最关键的词**：
   - `how to use claude design`（1300，KD=0）→ 写 Open Design on Olares 使用教程，直接截流
   - `claude design alternative` / `claude design download`（KD=0）→ Open Design = 本地化替代，Olares 一键部署
   - `AI design agents`（110，KD=18）→ Jaaz + Open Design 双应用在 Olares 上，构建本地 AI 设计 Agent 叙事

4. **最大攻击面**：① **闭源云锁定**——设计系统存在 Anthropic DB，非用户拥有；② **订阅共享配额**——Claude Pro $20/月，重度设计场景快速触及限额；③ **仅限 Opus 4.7**——Open Design BYOK 支持 22 个 CLI/模型，灵活度碾压；④ **无本地/自托管**——Open Design 74K★ 的成功正是打在这一痛点上。定价攻击："is claude design free"（90，KD=0，CPC $9.33）显示用户敏感于额外费用。

5. **隐藏低 KD 金矿**：
   - `AI design agents`（110，**KD=18**，$5.78 CPC）——品类词中 KD 最低，且是复数形式，Open Design 支持 22 个 agents 正好命中
   - `AI prototyping tool`（40，KD=31，**CPC $7.16**）——量小但 CPC 是品类词中最高，B2B 购买意图最纯
   - `claude design skill`（260，KD=29，**CPC $16.30**）——CPC $16 是全报告最高，说明该词对应的人群有极强的付费意愿（Claude Code 开发者），Open Design 支持 skill-driven 工作流可接住

6. **GEO 前瞻布局**：
   - `claude design alternative`、`self-hosted AI design`、`local AI design tool`——三词当前量为零，但 Open Design 官网已在 /alternatives/ 子路径做 SEO 布局；这些词会随 Claude Design 继续破圈而兑现；Olares 应在 Perplexity/ChatGPT Search/Google AI Overview 的问答层先占"在哪里能本地运行 Claude Design 同类功能"的引用位
   - `figma make alternative`（30，KD=0）、`lovart alternative`（20，KD=0）——正在显现量，GEO 占位窗口期短，优先级高

7. **与既有词表的关联**：`olares-500-keywords` 词表中已有 AI 工具/开源替代系词，Claude Design 细分词（design agent、vibe design、local design）是补充方向，与 Lovable/v0 等 vibe-coding 词组合可形成"本地 AI 开发 + 设计全栈"主题。`jaaz ai`（KD=10）是 Olares Market 应用直接曝光的最低摩擦词，尽管量小（40），但转化率预期极高。

---

*数据来源：SEMrush US 数据库（phrase_this、phrase_these、phrase_fullsearch、phrase_questions、phrase_related）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
