# Claude Code (SaaS 商业侧) SEO 竞品分析报告

> 域名：claude.ai | SEMrush US | 2026-07-06
> Claude Code 是 Anthropic 旗下的 agentic 编码助手，通过订阅套餐（Pro / Max / Team / Enterprise）或 API 按量计费，是当前编码 Agent 赛道流量最大的商业闭源产品。

**去重说明**：本报告聚焦 **商业 SaaS 侧**（订阅定价、credits 体系、usage-based 计费、对比替代叙事）。CLI 工具的安装/配置/功能关键词已在 [market/reports/claude-code.md](/Users/pengpeng/seo/directions/market/reports/claude-code.md) 覆盖，两份报告互补，本报告不重复登记 CLI 工具词。

---

## 项目理解（前置）

Claude Code 是 Anthropic 推出的 AI 编码 Agent CLI 工具，**无独立 SaaS 域名**，通过 claude.ai 订阅或 Anthropic API Key 计费。2026 年 6 月 15 日起，Anthropic 将订阅计费拆成两层：**交互式 terminal 使用**（共享订阅配额）和**程序化使用**（Agent SDK / `claude -p` / GitHub Actions，独立信用池）。这一分层加剧了价格复杂度，也使"超限 + 按量计费"的痛点词显著升温。

| 项目 | 内容 |
|------|------|
| 一句话定位 | Anthropic 旗下 agentic 编码 CLI，订阅制 + 按量付费双轨 |
| 开源 / 许可证 | 部分开源（CLI core Apache-2.0），后端模型闭源 |
| 主仓库 | github.com/anthropics/claude-code（★ ~50K） |
| 核心功能 | 终端 + IDE 编码 Agent、多文件编辑、codebase 全局索引、Agent SDK 程序化调用、GitHub Actions 集成 |
| 商业模式 / 定价 | Pro $20/月；Max 5x $100/月；Max 20x $200/月；Team Standard $25/seat/月；Team Premium $100/seat/月；Enterprise 自定义；API 按量（Sonnet 4.6: $3/MTok input, $15/MTok output） |
| 关键计费变更 | 2026-06-15：程序化用量（Agent SDK / `claude -p` / GitHub Actions）从交互配额独立出来，按 $20/$100/$200/月信用池计费；超限后按标准 API 费率叠加收费；credits 不滚存 |
| 差异化 / 价值主张 | Claude Sonnet/Opus 模型编码能力强；与 claude.ai 共享订阅；新增 Claude Cowork 团队协作场景 |
| 主要竞品（初判）| Cursor、GitHub Copilot、OpenCode（开源替代）、Gemini CLI、Aider |
| Olares Market | 未上架（Claude Code CLI 已支持 Olares 安装环境，见 market 侧报告） |
| 来源 | [claude.ai/upgrade](https://claude.ai/upgrade) · [support.claude.com](https://support.claude.com/en/articles/11049762-choose-a-claude-plan) · [danilchenko.dev](https://www.danilchenko.dev/posts/claude-code-max-vs-pro/) · [verdent.ai](https://www.verdent.ai/guides/claude-code-pricing-2026) · [morphllm.com](https://www.morphllm.com/claude-code-pricing) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | claude.ai |
| SEMrush Rank | 566 |
| 自然关键词数 | 10,330 |
| 月自然流量（US）| 4,843,349 |
| 自然流量估值 | $14,707,747/月 |
| 付费关键词数 | 409 |
| 月付费流量 | 224,731 |
| 付费花费估值 | $564,266/月 |
| 排名 1-3 位 | 2,965 词 |
| 排名 4-10 位 | 1,572 词 |
| 排名 11-20 位 | 1,455 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| claude.ai | 10,319 | 4,843,349 | 100% |
| a.claude.ai | 11 | ~0 | <0.01% |

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| claude | 1 | 2,740,000 | 91 | $2.71 | 2,192,000 | 导航 | claude.ai/ |
| claude ai | 1 | 1,830,000 | 100 | $2.47 | 1,464,000 | 导航 | claude.ai/ |
| claude code | 1 | 368,000 | 93 | $6.20 | 294,400 | 信息 | claude.ai/ |
| calude（误拼）| 1 | 90,500 | 89 | $2.71 | 72,400 | 导航 | claude.ai/ |
| cluade（误拼）| 1 | 49,500 | 84 | $2.71 | 39,600 | 导航 | claude.ai/ |
| claude ai login | 1 | 40,500 | 65 | $3.24 | 32,400 | 导航 | claude.ai/ |
| claude login | 1 | 27,100 | 73 | $7.06 | 21,680 | 导航 | claude.ai/ |
| claude usage | 1 | 9,900 | 54 | $13.26 | 7,920 | 信息 | claude.ai/settings/usage |
| claude cowork | 3 | 90,500 | 41 | $7.68 | 5,882 | 信息 | claude.ai/ |
| claude subscription | 1 | 6,600 | 53 | $4.73 | 5,280 | 信息 | claude.ai/ |
| claude design | 3 | 40,500 | 41 | $8.41 | 3,321 | 信息 | claude.ai/ |
| claude pricing | 2 | 22,200 | 57 | $8.54 | 2,930 | 商业 | claude.ai/upgrade |
| claude pro subscription | 1 | 5,400 | 55 | $5.25 | 4,320 | 商业 | claude.ai/settings/billing |
| 克劳德（中文）| 1 | 3,600 | 97 | $0.89 | 2,880 | 导航 | claude.ai/ |
| claude code pricing | 2 | 18,100 | 60 | $4.68 | 1,484 | 商业 | claude.ai/upgrade |
| claude max | 3 | 8,100 | 31 | $8.80 | 526 | 信息 | claude.ai/upgrade/max |

**关键洞察**：
- `claude code` 月量 368K、claude.ai 排名 #1、流量 29.4 万——核心品牌词完全被 claude.ai 垄断（KD=93，不可正面刚）
- `claude usage`（CPC $13.26）和 `claude cowork`（KD=41）是 claude.ai 上两个出乎意料的高 CPC / 低 KD 页面词，暗示"使用量监控"和"AI 协作空间"是 Anthropic 真正关注的商业方向
- `/settings/claude-code` 页面意外承接了大量**折扣/优惠码**搜索（claude promo code / claude discount code / claude referral），说明大量用户正在主动寻找降低 Claude Code 使用成本的方法——这是明确的「价格痛点信号」

### 付费词（Google Ads，按流量排序）

claude.ai 付费词高度聚焦品牌词，主要推动新用户注册 claude.ai。两条关键发现：

| 关键词 | 排名 | 月量 | CPC | 落地页 | 广告文案亮点 |
|--------|------|------|-----|--------|------------|
| claude | 1 | 2,740,000 | $2.71 | claude.ai/ | "Introducing Claude Fable 5 — most advanced model for coding" |
| claude ai | 1 | 1,220,000 | $1.96 | claude.ai/ | "Code, learn, create" |
| claude code | 3 | 110,000 | $3.72 | 用户分享页 | "Claude Code Mac / Claude Desktop Mac — work in terminal" |
| claude.ai | 2 | 22,200 | $0 | claude.ai/ | "AI-Powered Assistant — AI Coding Assistant" |

**付费策略洞察**：claude.ai 主要买自有品牌词保住入口；`claude code` 的付费排名只有 #3，说明竞争方（Cursor 等）也在买这个词截流。`claude.ai` 出现 CPC=$0 的广告（无效/自动出价），说明付费布局不系统。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| claude code vs cursor | 6,600 | 38 | $10.60 | 信息 | 最大对比词；Cursor 主竞品 |
| opencode vs claude code | 1,600 | 23 | $8.28 | 信息 | ⭐ 开源替代词快速升温 |
| claude code vs copilot | 590 | 17 | $8.43 | 信息 | ⭐ KD 极低；微软护城河弱 |
| claude code vs gemini cli | 590 | 14 | $7.30 | 信息 | ⭐⭐ KD=14！Google 对手词 |
| cursor alternative | 880 | 25 | $7.34 | 信息 | ⭐ 泛替代词，Olares 上架多款 coding agent |
| open code vs claude code | 260 | 17 | $8.76 | 信息 | ⭐ KD=17，OpenCode vs Claude Code |
| github copilot alternative | 210 | 13 | $6.46 | 信息 | ⭐⭐ KD=13；Olares 上可部署 Aider/OpenCode |
| claude alternatives | 210 | 20 | $5.97 | 信息 | ⭐ 泛替代词 |
| claude ai alternative | 260 | 19 | $5.24 | 信息 | ⭐ AI 助手替代词 |
| claude code alternative | 480 | 18 | $6.42 | 信息 | ⭐ 直接攻击词；KD 低 |
| aider alternative | 10 | 0 | $3.57 | 信息 | ⭐ 近零量近零 KD，新兴词 |
| open source coding agent | 210 | 20 | $5.51 | 信息 | ⭐ Olares 直接机会词 |
| self-hosted coding agent | 30 | 39 | $4.25 | 信息 | 自托管信号词 |
| local coding agent | 50 | 0 | $6.02 | 信息 | ⭐ KD=0，极早期 |
| is claude code open source | 590 | 43 | $38.25 | 信息 | CPC $38 极高！开源身份查询 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai coding assistant | 9,900 | 65 | $9.27 | 信息 | 主品类词；KD 高 |
| ai coding agent | 590 | 36 | $6.27 | 信息 | Agent 词升温 |
| best ai coding assistant | 1,300 | 50 | $8.91 | 信息 | 综述词 |

### 产品 / 功能词（品牌前缀，SaaS 侧聚焦）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| claude code pricing | 14,800 | 39 | $5.05 | 商业 | 核心定价词；**排名 #2 非 #1** |
| claude code subscription | 8,100 | 46 | $6.96 | 导航 | 订阅管理词 |
| claude max | 6,600 | 31 | $10.43 | 信息 | Max 套餐词 |
| claude code cost | 2,900 | 35 | $7.83 | 信息 | ⭐ 价格探索词 |
| is claude code free | 2,900 | 30 | $20.64 | 信息 | ⭐ CPC $20！免费疑问词 |
| anthropic claude api pricing 2026 | 4,400 | 22 | $0 | 商业 | ⭐ 年份词 KD=22，内容长青 |
| claude code pro plan | 2,400 | 33 | $7.86 | 信息 | ⭐ Pro 套餐研究词 |
| claude code usage | 2,400 | 48 | $16.92 | 信息 | CPC $17！用量查询词 |
| anthropic api pricing | 2,400 | 29 | $10.07 | 商业 | ⭐ API 定价对比 |
| claude code max | 1,900 | 28 | $8.68 | 信息 | ⭐ Max 套餐研究 |
| claude code plans | 1,900 | 49 | $7.85 | 信息 | 套餐对比词 |
| max 5x vs pro | 1,600 | 10 | $0 | 信息 | ⭐⭐ KD=10！套餐决策对比词 |
| claude code usage limits | 590 | 35 | $20.34 | 信息 | CPC $20！限额查询词 |
| claude api cost | 720 | 36 | $8.75 | 信息 | API 成本词 |
| claude code free tier | 390 | 20 | $12.67 | 信息 | ⭐ 免费档查询 |
| claude api credits | 390 | 34 | $9.87 | 商业 | ⭐ credits 攻击词 |
| claude credits | 320 | 27 | $9.78 | 信息 | ⭐ |
| claude code billing | 210 | 47 | $47.62 | 商业 | **CPC $47.62 全场最高！** |
| claude code credits | 210 | 22 | $14.48 | 信息 | ⭐ credits 词 |
| anthropic credits | 170 | 41 | $12.01 | 商业 | API credits 词 |
| claude max subscription | 170 | 10 | $2.22 | 信息 | ⭐⭐ KD=10 |
| claude code tokens | 170 | 0 | $14.00 | 信息 | ⭐⭐⭐ KD=0！tokens 用量词 |
| claude rate limit error | 1,300 | 26 | $0 | 信息 | ⭐ 高量 rate limit 报错词 |
| claude rate limit | 90 | 29 | $20.33 | 信息 | ⭐ CPC $20 |
| how does claude code pricing work | 50 | 0 | $9.26 | 信息 | ⭐ 问题词 KD=0 |

### 折扣 / 优惠码词（`/settings/claude-code` 页自然承接）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|----|------|
| claude promo code | 320 | 13 | $12.64 | 商业 |
| claude discount code | 390 | 18 | $12.48 | 商业 |
| claude student discount | 5,400 | 23 | $9.02 | 商业 |
| claude ai discount | 390 | 14 | $8.30 | 商业 |
| claude referral | 170 | 17 | $39.25 | 商业 |
| claude referral code | 140 | 33 | $21.72 | 商业 |

> 折扣词整体 CPC 高（$8–$39）、KD 低（13–23），是 Claude Code 订阅用户主动寻求降费的强信号。

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source coding agent | 210 | 20 | $5.51 | 信息 | ⭐ Olares Market 直接机会 |
| is claude code open source | 590 | 43 | $38.25 | 信息 | CPC $38 极高，开源查询词 |
| local coding agent | 50 | 0 | $6.02 | 信息 | ⭐ KD=0 极早期 |
| self-hosted coding agent | 30 | 39 | $4.25 | 信息 | 自托管词 |
| ai coding agent open source | 30 | 0 | $5.20 | 信息 | ⭐ KD=0 |

---

## Olares 关联词（Phase 3）

**核心叙事切入点**：Claude Code 的定价复杂度（双轨计费 + credits 不滚存 + 超限按 API 费率叠加 + rate limit 报错）是天然攻击面——Olares 上部署本地 coding agent（OpenCode + Ollama 本地模型）= 无限制、零 token 成本、无 5 小时窗口限制、无 credits 过期。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| claude code vs cursor | 6,600 | 38 | $10.60 | ⭐⭐⭐ 高量对比词；叙事：Olares 上 OpenCode/Aider 兼容两家模型接口，无订阅锁定 |
| is claude code free | 2,900 | 30 | $20.64 | ⭐⭐⭐ CPC $20；答案是"Pro $20 起"→ Olares + OpenCode + Qwen3 本地 = 真免费 |
| max 5x vs pro | 1,600 | 10 | $0 | ⭐⭐⭐ KD=10！用户在套餐决策边缘，Olares 本地方案是"第三选项"叙事 |
| claude code pricing | 14,800 | 39 | $5.05 | ⭐⭐ 高量定价词；Olares + 本地 LLM 对标 Claude Max 功能，零月租 |
| anthropic claude api pricing 2026 | 4,400 | 22 | $0 | ⭐⭐ KD=22；年份词长效；Olares Vault 管理 API Key + 本地模型控费 |
| claude code alternative | 480 | 18 | $6.42 | ⭐⭐⭐ 核心替代词；OpenCode on Olares = 本地 coding agent，支持 Qwen3/DeepSeek |
| claude code vs gemini cli | 590 | 14 | $7.30 | ⭐⭐⭐ KD=14！三方对比：Claude Code vs Gemini CLI vs 本地 OpenCode on Olares |
| github copilot alternative | 210 | 13 | $6.46 | ⭐⭐ KD=13；Olares Market 上有 Aider + OpenCode 可作 Copilot 替代 |
| opencode vs claude code | 1,600 | 23 | $8.28 | ⭐⭐⭐ Olares 直接上架 OpenCode，这是 Olares 有天然资格写的文章 |
| claude code credits | 210 | 22 | $14.48 | ⭐⭐ credits 攻击词；Olares 本地方案无 credits/无过期/无超限费 |
| claude code billing | 210 | 47 | $47.62 | ⭐⭐ **CPC $47 全场最高**；2026-06-15 计费变更复杂，Olares 本地零账单叙事 |
| claude code usage limits | 590 | 35 | $20.34 | ⭐⭐ CPC $20；用量限制痛点词，本地无限制 |
| claude rate limit error | 1,300 | 26 | $0 | ⭐⭐ 高量报错词；Olares 本地无 rate limit |
| open source coding agent | 210 | 20 | $5.51 | ⭐⭐⭐ Olares Market 直接机会词 |
| claude code tokens | 170 | 0 | $14.00 | ⭐⭐⭐ KD=0！token 用量词，Olares 本地方案无 token 计费 |
| claude max subscription | 170 | 10 | $2.22 | ⭐⭐ KD=10；Max 套餐用户对价格敏感，Olares 一次性硬件 vs 月租 |
| is claude code open source | 590 | 43 | $38.25 | ⭐ CPC $38；答案：Claude Code CLI 是 Apache-2.0 但模型闭源 → 推 Olares + 完全开源本地方案 |
| self-hosted coding agent | 30 | 39 | $4.25 | ⭐ 自托管词，Olares 核心场景 |
| claude code vs opencode | 90 | 19 | $26.16 | ⭐⭐ CPC $26；Olares 上架 OpenCode，天然资格 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| claude code pricing | 14,800 | 39 | $5.05 | 商业 | 主词候选 | 最高量定价词，claude.ai 排 #2 非 #1——Olares 本地方案 vs Claude Pro/Max 成本对比文章核心锚词 |
| claude code vs cursor | 6,600 | 38 | $10.60 | 信息 | 主词候选 | 最大对比词；从 Olares 视角切入：本地 coding agent 超越两家订阅锁定 |
| claude max | 6,600 | 31 | $10.43 | 信息 | 主词候选 | Max 套餐词 KD=31，Olares Olares One vs Max 20x $200/月订阅成本对比 |
| is claude code free | 2,900 | 30 | $20.64 | 信息 | 主词候选 | CPC $20；答：Pro $20 起；Olares + Qwen3/DeepSeek = 零月租 coding agent |
| anthropic claude api pricing 2026 | 4,400 | 22 | $0 | 商业 | 主词候选 | KD=22 年份词；内容长效；Olares Vault 管理 API Key + 本地模型控费叙事 |
| opencode vs claude code | 1,600 | 23 | $8.28 | 信息 | 主词候选 | KD=23；OpenCode on Olares = 本地替代，天然写此文章的资格 |
| max 5x vs pro | 1,600 | 10 | $0 | 信息 | 主词候选 | KD=10 全场最低对比词之一；套餐决策边缘用户，Olares 可作"第三选项" |
| claude rate limit error | 1,300 | 26 | $0 | 信息 | 主词候选 | 高量报错词；用户卡壳时的 Olares 本地无限制方案 |
| claude code vs copilot | 590 | 17 | $8.43 | 信息 | 主词候选 | KD=17；Olares Market 上 Aider/OpenCode 双上架 |
| claude code vs gemini cli | 590 | 14 | $7.30 | 信息 | 主词候选 | ⭐⭐ KD=14！三方对比文选题 |
| claude code alternative | 480 | 18 | $6.42 | 信息 | 主词候选 | 核心替代词；OpenCode + Aider on Olares |
| claude code usage limits | 590 | 35 | $20.34 | 信息 | 次级 | CPC $20；用量限制痛点，并入定价文 |
| claude code credits | 210 | 22 | $14.48 | 信息 | 次级 | credits 攻击词；并入计费痛点文 |
| github copilot alternative | 210 | 13 | $6.46 | 信息 | 次级 | KD=13；Olares 同时上架 Aider + OpenCode |
| open source coding agent | 210 | 20 | $5.51 | 信息 | 次级 | Olares Market 直接机会；并入替代词文章 |
| claude code billing | 210 | 47 | $47.62 | 商业 | 次级 | CPC $47 最高；并入计费复杂度分析文 |
| claude code tokens | 170 | 0 | $14.00 | 信息 | 次级 | KD=0！并入 Claude Code 用量/计费文 |
| claude max subscription | 170 | 10 | $2.22 | 信息 | 次级 | KD=10；Max 用户价格敏感，并入 Max vs 本地文 |
| claude code vs opencode | 90 | 19 | $26.16 | 信息 | 次级 | CPC $26；Olares 上架 OpenCode 天然资格 |
| local coding agent | 50 | 0 | $6.02 | 信息 | 次级 | KD=0 早期词；并入开源/自托管文 |
| self-hosted coding agent | 30 | 39 | $4.25 | 信息 | 次级 | 自托管词；KD=39 暂次级，量起后升主词 |
| how does claude code pricing work | 50 | 0 | $9.26 | 信息 | GEO | 问题词 KD=0；进 FAQ / AI Overview |
| claude code tokens per session | 0 | — | — | 信息 | GEO | 近零量语义精准；抢"每次 session 用多少 token"直答位 |
| coding agent no rate limit | 0 | — | — | 信息 | GEO | 近零量，抢"无限制 coding agent"直答位，Olares 场景精准 |
| claude code agent sdk cost | 0 | — | — | 商业 | GEO | 程序化计费词，6月变更后上升中 |

---

## 核心洞见

1. **品牌护城河**：`claude code`（368K/月，KD=93）完全被 claude.ai 品牌垄断，不可正面刚。但**定价词护城河极弱**——`claude code pricing`（14,800/月，KD=39）目前 claude.ai 只排 #2，第三方内容站（verdent.ai、morphllm.com）已在排名首位，说明 Anthropic 对自己的定价页面 SEO 投入不足，Olares 有空间切入。

2. **可复制的打法**：verdent.ai 靠一篇 `claude-code-pricing-2026` 排进 Top3，morphllm.com 靠定价对比表排名稳定——**长文定价 + 套餐对比 + 破损点分析**（credits 不滚存、rate limit 机制、5 小时窗口）是可复制的内容打法。Olares 追加"本地方案对比"增加差异化。

3. **对 Olares 最关键的 3 个词**：
   - **`opencode vs claude code`**（1,600/月，KD=23）：Olares Market 上架 OpenCode，是写这篇文章的唯一有原生资格的产品——文章标题天然可以是"OpenCode on Olares vs Claude Code: 完全免费的本地 coding agent"。
   - **`max 5x vs pro`**（1,600/月，KD=10）：KD=10 全场最低主词候选，用户在做订阅决策——Olares 可作"第三选项：$0/月本地 coding agent"切入，转化价值极高。
   - **`claude code vs gemini cli`**（590/月，KD=14）：KD 极低，两家大厂对比词，Olares + OpenCode/Aider 是天然第三角，CPC=$7.30 验证商业意图。

4. **最大攻击面（计费痛点词）**：`claude code billing`（CPC $47.62）、`claude code usage limits`（CPC $20.34）、`is claude code free`（CPC $20.64）、`claude rate limit error`（1,300/月）——2026-06-15 双轨计费变更制造了大量新搜索需求；用户正在对"程序化 Agent SDK 额外扣费"感到困惑和不满，这是 Olares 本地方案叙事的最强进入口。

5. **隐藏低 KD 金矿**：
   - `max 5x vs pro`（KD=10，1,600/月）：套餐决策词，高转化意图
   - `claude max subscription`（KD=10，170/月）：Max 用户在研究是否续费
   - `claude code vs gemini cli`（KD=14，590/月）：三方对比词
   - `github copilot alternative`（KD=13，210/月）：泛替代词
   - `claude code tokens`（KD=0，170/月，CPC=$14）：tokens 用量查询，近零竞争

6. **GEO 前瞻布局**：  `claude code agent sdk cost`（程序化计费，双轨新政后持续升温）、`coding agent no rate limit`（本地方案诉求词）、`claude code tokens per session`（session 用量透明度词）——这类词目前量近零，但随 2026-06-15 计费变更认知普及会快速涨量，及早进 FAQ/直答段抢引用位。

7. **与既有词表关联**：市场侧 `claude-code.md` 已覆盖 CLI 工具词（claude code install / hooks / settings / plan mode / ollama 等）；本报告补充**SaaS 订阅 + 定价 + credits 攻击面**词层。两份报告合并后，`claude code alternative`（KD=18）与 `opencode vs claude code`（KD=23）是当前最值得立项的主词候选——前者已在市场侧标记，后者是本报告新发现的 Olares 原生机会词。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、resource_adwords、domain_organic_subdomains、domain_organic_organic、domain_adwords_adwords、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
