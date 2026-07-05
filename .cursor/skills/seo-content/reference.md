# seo-content 模板与清单速查

配合 [SKILL.md](SKILL.md) 使用。三种文体的骨架、对比表模式、title/meta 公式、FAQ/GEO 块、自查清单，以及"场景→产品"原则的写作应用。

---

## 0. 内容 brief 模板（Step 2 产出）

```markdown
# Brief: <目标词>

- 文体: alternative | versus | listicle
- 主词: <target keyword>（月量 / KD / CPC，引自来源报告）
- 次级词: <同族/相关词，逗号分隔>
- 搜索意图: <信息 / 商业 · 一句话>
- 来源报告: directions/<cat>/reports/<x>.md
- 挂载场景: scenarios.md 场景 <n>
- 差异化切入（攻击面）: <定价/credits / 闭源 / 云端隐私 / 额度限制 …>
- Olares 平替（须在 apps.md/models.md 可部署）: <应用/模型名>
- 大纲: H2/H3 列表（对齐 SERP 胜出格式）
- 对比表维度: <见 §2>
- 必提实体: <竞品、相关开源项目、Olares 应用>
- 内链: <…> ｜ 外链（权威源）: <竞品官网/GitHub/标准>
- Title 候选: 1) … 2) … 3) …
- Meta description: <…≤155 字符>
- Slug: <x-alternative / x-vs-y / best-self-hosted-x>
- FAQ 题（来自 PAA）: 1) … 2) … 3) …
```

---

## 1. 三文体大纲模板

### A. Alternative（`X alternative` / `open source X` / `self hosted X`）

```
H1: The Best Open-Source, Self-Hosted <X> Alternative (Own Your Data)
- 首段（含主词，<100 词）：直答"想要 X 的能力但不想 <攻击面：锁定/烧额度/数据上云>？可以自托管的开源替代。"
H2: What is <X> and why look for an alternative?  ← 客观讲 X + 点出攻击面
H2: <Olares 平替> — the open-source alternative        ← 是什么、开源/许可证、核心功能
H2: <平替> vs <X>: how they compare                    ← 小对比表（见 §2）
H2: Why run it on Olares                                ← 一键部署 + 本地 LLM 不烧额度 + 数据归你 + 随处访问
H2: How to get started on Olares                        ← 部署/上手步骤，CTA 到 Market 应用
H2: FAQ                                                 ← §3
```

### B. Versus（`X vs Y`，推荐做成 `X vs Y vs Olares` 三方）

```
H1: <X> vs <Y><（vs Olares）>: Which Should You Choose in <year>?
- 首段：一句话结论 + 各自最适合谁。
H2: Quick comparison（对称对比表，见 §2）
H2: <X> overview  / H2: <Y> overview  /（H2: The self-hosted route: Olares）
H2: 逐维展开（定价、开源与否、部署、数据归属、本地 LLM、扩展性…每维一段）
H2: Which one is right for you?  ← 分人群给建议，诚实
H2: FAQ
```

### C. Listicle（`best/N open-source self-hosted X` / `X alternatives`）

```
H1: N Best Open-Source, Self-Hosted <X> Alternatives in <year>
- 首段：为什么找自托管替代（攻击面）+ 本文标准（开源/可自部署/活跃度）。
H2: 快速对比表（N 行 × 对称列，见 §2）
H2: 1) <项目A> — 一句话定位；开源/许可证；亮点；适合谁；**Deploy on Olares**（一键）
H2: 2) <项目B> …（每个同结构，客观）
H2: How to self-host any of these on Olares  ← 统一部署段
H2: FAQ
```

> 清单要放**真实**的开源项目（含非 Olares 独有的），客观可信；Olares 的价值是"这些都能在 Olares 一键跑"，而非假装只有 Olares。

---

## 2. 对比表模式

对称、两侧都填、维度对目标读者相关。常用列：

| 维度 | <X（竞品）> | <Olares 平替 / Olares> |
|------|------------|----------------------|
| 开源 / 许可证 | 闭源 / 专有 | 开源（<License>） |
| 部署方式 | 云 SaaS | 自托管，一键部署到 Olares |
| 定价模型 | 订阅 / 按额度(credits)/按 token | 硬件一次买断 + 本地模型免额度 |
| 数据归属 | 存厂商云 | 完全在你自己的硬件 |
| 本地 LLM / 离线 | 否 | 是（Ollama 等本地模型） |
| 远程访问 | 厂商托管 | 自带（LarePass / 内置隧道），随处访问 |
| 扩展 / 生态 | 平台内 | Market 应用作为 Agent 的 tool |

按品类删改维度（如出图类加"可控性/版权"、协作类加"SSO/权限"）。**只填能核实的事实**，不确定的维度不写或标注。

---

## 3. FAQ / GEO 直答块

- 每个关键问题：**先一句直答，再展开**（AI 引擎抓首句）。
- 文末 FAQ 用问答对，问题取自 PAA / 相关搜索：

```
## FAQ
**Is there an open-source alternative to <X>?**
Yes — <平替> is an open-source, self-hostable alternative you can deploy on Olares in one click. <一句展开>

**Can I run <X alternative> locally / self-hosted?**
Yes. <一句：Olares 上如何、需要什么>。

**Is <平替> free?**
<诚实说明：软件开源免费；成本在自有硬件/电费；对比 X 的订阅/额度>。
```

- 建议 schema：文章头 front-matter 里标 `schema: Article` 或 `schema: FAQPage`（发布端据此生成 JSON-LD），正文不必写死。

---

## 4. Title / Meta 公式

- **Alternative**：`The Best Open-Source <X> Alternative (Self-Hosted, <利益点>)` — ≤60 字符、主词靠前。
- **Versus**：`<X> vs <Y>: <利益点/结论> (<year>)`。
- **Listicle**：`<N> Best Open-Source Self-Hosted <X> Alternatives (<year>)`。
- **Meta description**（≤155）：`<一句痛点> — <平替/Olares> lets you <核心价值：own your data / no credits / run locally>. <隐性 CTA>.`
- **Slug**：全小写短横线，含主词根：`<x>-alternative`、`<x>-vs-<y>`、`best-self-hosted-<x>`。

---

## 5. 发布前自查清单

- [ ] 主词在 Title、H1、首段前 100 词、meta；次级词自然分布，无堆砌
- [ ] 文体/结构对齐 SERP 胜出格式；篇幅与前排相当
- [ ] 对比表两侧对称、维度相关、**每格可核实**
- [ ] **事实纪律**：无未发布能力/版本号/时间表（保密红线）；竞品定价/许可证已核实；数字不编造
- [ ] 推荐的 Olares 平替在 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md) / [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 确实可部署
- [ ] 品牌大小写与语气正确（basic/olares.md）；未把 Olares 说成 NAS/PC
- [ ] 对竞品客观、不稻草人；差异化靠攻击面而非贬低
- [ ] FAQ / 直答块在位；内链 + 权威外链齐；图有 alt
- [ ] CTA 指向具体 Market 应用 / 部署入口
- [ ] front-matter 完整（title/target_keyword/secondary/meta/slug/article_type/source_report/scenario/status）

---

## 6. "场景 → 产品"原则在写作中的应用

选题时按 [scenarios.md](/Users/pengpeng/seo/scenarios/scenarios.md) 的关系原则推导，不靠硬编码清单：

1. 目标词属哪个场景 → 该场景的"已验证付费市场"给你**商业对标**（写对比的另一方 + 攻击面来源）。
2. 承接该需求的 **Olares 平替**现查 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md) / [model/models.md](/Users/pengpeng/seo/directions/model/models.md)——这是文章要导向、且必须真实可部署的落点。
3. 场景的"兑现纪律"决定语气：产品已兑现 → 可主推；未兑现 → 只做"占位/教育"内容，不承诺。
