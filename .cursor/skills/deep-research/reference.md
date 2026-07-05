# deep-research 模板与阈值速查

配合 [SKILL.md](SKILL.md) 使用。收敛自 daymade V6 的 subagent_prompt / research_notes_format / report_template / quality_gates / enterprise_* 等文件，已适配 Cursor 工具与中文口径。

---

## 1. 子代理任务提示模板（P2 分派用）

Lead 填好 `{变量}` 后用 `Task`（`subagent_type: explore`，`run_in_background: true`）分派：

```
你是研究专员，角色：{role}。

## 任务
{objective}

## 起始查询（可按需调整/扩展）
1. {query_1}
2. {query_2}
3. {query_3}（可选）

## 要求
1. 用 WebSearch 跑 2-4 次搜索（含变体）。
2. 对最好的 2-3 个结果用 WebFetch 读全文（仅 DEEP 任务；SCAN 任务最多抓 1 篇）。
3. 每个来源判定：
   - Source-Type: official | academic | secondary-industry | journalism | community | other
   - As Of: YYYY-MM 或 YYYY（发布或最后核实日期；未知写 undated）
   - 权威分：1-10
4. 把全部结果按下方格式写入文件：{output_path}
5. Gaps 里至少记 1 个相反主张候选。
6. 严格套用下方格式，不要输出过程叙述。写完文件即停。

## 输出格式（写入 {output_path}）
---
task_id: {task_id}
role: {role}
status: complete
sources_found: {N}
---

## Sources
[1] {标题} | {URL} | Source-Type: {类型} | As Of: {YYYY-MM} | Authority: {分}/10
[2] ...

## Findings
- {一句话具体事实}。[1]
- {带来源号与置信度的事实}。[2]
（≤10 条，每条一句、每条带来源号；不要"研究表明…"这种空话）

## Deep Read Notes
### Source [1]: {标题}
Key data: {全文里的具体数字/日期/百分比}
Key insight: {这个源独有、别处没有的一点}
Useful for: {支撑最终报告的哪一节}
（每源 ≤4 行；DEEP 任务的 2-3 篇全文才写这段）

## Gaps
- {搜了但没找到的}
- {相反解读或方法论局限}

## END
Gaps 之后不要再写任何内容。
```

规则：`[n]` 是**该任务文件内的局部编号**（从 [1] 起），Lead 在 P3 会重编全局号；URL 必须来自真实搜索结果，**子代理禁止编 URL**；高置信度主张须用 `official`/`academic` 源。

---

## 2. task-{id}.md 笔记格式（子代理产出）

即上方"输出格式"落地到 `research/<slug>.notes/task-{id}.md`。要点：

- **Sources 行**：`[n] 标题 | URL | Source-Type: … | As Of: … | Authority: 分/10`
- **Findings**：一句一事实，末尾带来源号 `[1]` 或 `[1][2]`，最多 10 条（逼迫排序）。
  - 好：`纺织业全面机械化用了 50-90 年（1760s-1850s）。[4]`
  - 坏：`这个过程花了很久。[4]` / `据研究…`（无源、含糊）
- **Deep Read Notes**：仅对 WebFetch 读过全文的源写，每源 ≤4 行（Key data / Key insight / Useful for）。
- **Gaps**：搜了没找到的 + 相反解读；证据薄弱处在此显形，用于降级置信度。

---

## 3. 引证登记 registry.md（Lead 在 P3 建）

```
# 引证登记
Built from: task-a.md, task-b.md, ...

## Approved
[1] 机构/作者 — 标题 | URL | Source-Type: official | Accessibility: public | As Of: 2026-03 | Auth: 8 | From: task-a
[2] ...

## Dropped
x 标题 | URL | Source-Type: community | Accessibility: … | Auth: 3 | Reason: 低于阈值 / 有更好来源 / 循环验证(用户已知) / 独家源无公开等价

## Stats
Total evaluated: 22 | Approved: 16 | Dropped: 6
Unique domains: 12
Source-type: official 4 / academic 3 / secondary-industry 5 / journalism 2 / community 2
Max single-source share: 3/16 = 19%（pass）
Official share: 44%（pass）
```

规则：登记里的 `[n]` **最终不变**，报告里每个 `[n]` 必须在 Approved；Dropped 的源**永不**进报告；同 URL 只留一次（取权威分高者）。

---

## 4. 质量门阈值（各阶段）

| Gate | 检查 | Standard | Lightweight |
|------|------|----------|-------------|
| G1 任务笔记(P2后) | 每任务来源数 / 发现数 | ≥2 / ≥3 | ≥1 / ≥2 |
| | DEEP 任务有 Deep Read Notes；URL 全来自真实搜索 | 100% | 100% |
| G2 登记(P3后) | approved 源数 / 独立域名 | ≥12 / ≥5 | ≥6 / ≥3 |
| | 官方源占比 / 单一来源占比 | ≥30% / ≤25% | ≥20% / ≤30% |
| | 来源类型 ≥2 类；Dropped 全列出；无重复 URL | 是 | 是 |
| G3 初稿(P5后) | 引用密度 | ≥1/200 字 | ≥1/300 字 |
| | 每节有置信度标记；高置信主张有官方源背书 | 100% | 100% |
| | 主要节记录反方主张 | 100% | 70% |
| | 总字数 | 3000-8000 | 2000-4000 |
| G4 溯源(P6后) | 每条具体主张/数字可追到某条笔记；不与笔记矛盾 | 100% | 100% |
| | P6 至少找出 3 个问题 | 必须（0 则再查） | 必须 |
| G5 核验(P7后) | 所有 [n] 有效；抽查 5+ 条主张溯源 | ≥4/5 通过 | ≥4/5 |
| | 无 Dropped 源复活；关键主张来源集中度 | 0 / 无 >25% | 0 / 无 >30% |

**反幻觉信号**：URL 不在任何子代理搜索里 → 删引用；主张不在任何笔记 → 删或标 `[unverified]`；数字比来源更精确（"73.2%" 而笔记是"约 70%"）→ 用笔记精度；"据统计/某专家表示"无出处 → 补名或改定性表述；旧模型/旧数据未标 AS_OF → 降级并重搜；假 URL（含伪造 CNKI 格式）→ 删并记 Gap。

---

## 5. 报告模板（P5 起草用）

```markdown
# {标题}

> 研究日期: {DATE} | 来源数: {N} | 字数: ~{WORD} | 模式: {Standard/Lightweight} | AS_OF: {YYYY-MM-DD} | 官方源占比: {xx}%

## 摘要
{200-400 字：关键发现、方法、结论、风险}

## N. {按主题命名的章节}
{正文含行内引用 [1][2]。Standard 每节 500-1000 字、Lightweight 300-600 字。
每个事实带 [n]；数字必须有源；证据冲突时成对给支持与反驳。}

**置信度:** High/Medium/Low
**依据:** {来源一致性 / 证据质量 / 数据可得性}
**反方解释:** {一个明确的相反解读+引用，或 [unverified]}

## 核心争议
- **争议 1:** [主张 A vs 反向证据 B] [n][m]
- **争议 2:** …

## 关键发现
- **发现 1:** {最重要结论} [3][7]
- **发现 2:** … （Standard 3-5 条，Lightweight 2-3 条）

## 局限性与未来方向
### 本研究局限
{没覆盖的角度及原因；方法论局限：可公开访问、付费墙、语言、时点；来源与反证缺口}
### 未来方向
{可跟进的具体课题 + 优先级 + 应补的证据类型}

## 参考文献
[1] 机构/作者. "标题". Source-Type: …. As Of: YYYY-MM-DD. URL.
```

规则：正文每个 [n] 在参考文献有对应条目，且每个条目至少被引用一次；Source-Type 与 As Of 必填；所有 URL 来自 P2 来源池。

---

## 6. 公司专项模式（精简版）

单个企业调研时，P1 任务板对齐**六维**，另加框架化分析与三级质检。

**六维数据采集（尽量并行）**
- D1 公司基本面（实体、成立、融资、股权）
- D2 业务与产品（板块、产品、营收结构）
- D3 竞争位置（行业排名、竞品、壁垒）
- D4 财务与运营（近 3 年财务、效率指标）
- D5 近期动态（近 6 个月事件、战略信号）
- D6 内部/专有源（或注明缺失）

关键原则：证据驱动（每个结论可溯源）；关键数据 ≥2 个独立来源交叉验证；克制判断（推测显式标注）；复杂信息用表格/层级呈现。

**框架化分析（按序）**
1. SWOT——每条带证据+来源+影响评估
2. 竞争壁垒量化——7 维加权评分 → A+/A/B+/B/C+/C
3. 风险矩阵——8 类，概率×影响 → 红/黄/绿
4. 综合评分卡——6 维加权 → X/10

**三级质检**：L1 数据（来源数/归属/交叉验证/时效）→ L2 分析（SWOT 完整性/风险覆盖/壁垒评分/结论支撑）→ L3 文档（结构/格式一致/可读性/附录），在阶段切换时各跑一次。

**7 章报告模板**：① 公司概览 ② 业务与产品结构 ③ 市场与竞争位置 ④ 财务与运营分析 ⑤ 风险与隐忧 ⑥ 近期动态 ⑦ 综合评估与结论；附录：数据来源索引 / 术语表 / 免责声明。多遍起草与复核同通用模式 P5-P7。
