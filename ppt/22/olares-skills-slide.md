# From Human Intent to Governed Agent Action

> Intel 合作 PPT 第 22 页。中文 Slide 文案与工作底稿；页面需要在无人讲解时独立完成叙事。

---

## Slide copy

### Headline

**From Human Intent to Governed Agent Action**

Any compatible Agent can securely operate software, models and private context on infrastructure the user owns.

### Architecture · How Agents access and operate Olares

#### 01 · Input Devices

Phone · Computer · Glasses · Speaker · Earbuds · Watch

Always connected across devices.

#### 02 · Personal Agents

Claude Code · OpenClaw · Hermes Agent · Codex · Olares Ashia

Running on Olares or your own devices.

Any compatible Agent with `olares-cli` or Olares Skills can invoke structured Olares operations within its identity and permissions.

#### 03 · Agent Orchestration

- **AI Router:** gives applications **one interface** to AI capabilities, routing requests across **local and remote models** while enforcing authorization and usage policies.
- **Agent Sandbox:** provides a **VM-level sandbox** where each Agent can use tools and models and manage user context in a **controlled environment** with explicit limits.
- **Agent Collaboration:** uses **ACP** to assign tasks, coordinate execution, collect results and monitor runtime state across multiple Agents as **one workflow**.
- **Observability:** observes **model and Agent usage**, quotas, permissions, reliability, execution details and output quality over time for **governance**.
- **Learning loop:** collects **user feedback** to **refine context**, improve local models and optimize Agent behavior through continued use without losing context.

Before anything runs, Olares decides what should execute, where it should run and what it is allowed to access.

#### 04 · Agent Capability

Three capability planes work together on the governed plan:

| Runtime plane | What it contributes | Why it matters |
|---------------|---------------------|----------------|
| **Tools** | **Digital body:** redroid · Chromium · Windows VM · macOS VM<br>**Physical world:** Home Assistant · Reachy Mini<br>**Tools:** n8n · NocoDB | Applications give the Agent environments and systems in which it can act. |
| **Models** | **Language:** LLM · Translation<br>**Vision:** Image · Video · OCR · 3D · World model<br>**Audio:** TTS · STT · Realtime voice · Music<br>**Retrieval:** Embedding | Multimodal intelligence lets the Agent reason across language, vision, speech and media. |
| **Context System** | **Knowledge Sources:** Documents · Notes & wikis · Saved content · Connected SaaS<br>**User Data:** Email · IM & chat · Contacts · Calendar · Photos & video · Health & fitness | User-owned data and organized knowledge ground every action in real context. |

Tools act, models reason and context makes the result relevant.

#### 05 · Olares Foundation

Secure infrastructure for every Agent action.

Sandbox · App Lifecycle · Middleware · Accelerator · Network · Identity · Storage · Observability

### How Olares manages an Agent request

1. **Capture intent from any device.**  
   Phones, computers, glasses, speakers, earbuds and watches remain connected entry points for voice, text, vision and events.

2. **Let the chosen Agent form an executable plan.**  
   Claude Code, OpenClaw, Hermes Agent, Codex or Ashia uses `olares-cli` and Olares Skills.

3. **Route and authorize the request.**  
   The Control Plane selects the Agent or model and checks identity, permissions, usage and quota.

4. **Assemble the capabilities needed to execute.**  
   The Runtime combines applications, multimodal models and user-owned context.

5. **Return an observable result.**  
   The Foundation isolates the workload and sends status, telemetry and results back to the Agent.

### Difference

**Agent platforms often stop at understanding or answering. Olares closes the loop from human intent to governed, observable action on user-owned infrastructure.**

---

## 工作底稿

### 本页的叙事

这页不是组件清单，而是一条 Agent 请求的管理闭环：

`Input devices → Personal Agent + CLI access → routing & governance → Tools + Models + Context → isolated execution → result / status / telemetry`

每一层只回答一个问题：

1. 哪些设备把用户意图输入系统？
2. 哪些 Personal Agent 可以通过 CLI 操作 Olares？
3. Olares 如何路由、授权和治理请求？
4. Agent Capability 如何组合 Tools、Models 与 Context？
5. 系统如何隔离执行并回传结果与遥测？

### 架构边界

- Input Devices 位于第一层，只负责表达意图。
- Personal Agents 位于第二层，可以运行在 Olares 或用户自己的设备上，并通过 CLI 把计划变成结构化操作。
- Agent Orchestration 位于 Agent 接口与 Agent Capability 之间。
- Agent Capability 内部是 Tools、Models、Context System 三个平行能力面。
- Foundation 位于 Agent Capability 下方，是共享 OS 底座。
- “Agent Capability”是能力边界，不是单个 Docker container。

HTML 版式中，01 层为 68px、02 层为 76px、03 层为 124px、04 层为 204px、05 层为 74px。03 的高度不因标题缩短而调整；控制项标题为 11.5px、正文为 10.5px，顶部 padding 为 9px，正文 line-height 为 1.25；Tools、Models、Context System 的内边距为 8px 12px。

Tools 内部沿用第 18/21 页的紧凑分组节奏：每组上下各留 5px，组名与应用间隔 4px，多行应用的纵向间隔 4px；hairline 只承担分组，不紧贴图标或文字。

### 三个 capability plane

- **Tools** 回答“Agent 能做什么”：操作应用、数据、自动化、网页和物理设备。
- **Models** 回答“Agent 可以调用什么智能”：展示模型类型，不展示推理引擎。
  - Language：LLM、Translation。
  - Vision：Image、Video、OCR、3D、World model。
  - Audio：TTS、STT、Realtime voice、Music。
  - Retrieval：Embedding。
- **Context System** 回答“Agent 记得和知道什么”：
  - Knowledge Sources：Documents、Notes & wikis、Saved content、Connected SaaS。
  - User Data：Email、IM & chat、Contacts、Calendar、Photos & video、Health & fitness。

Connected SaaS 表示接入的外部 SaaS 数据源，包括 CRM、项目管理和协作文档等；不再把 CRM 与 SaaS 并列。General knowledge 不属于用户或组织拥有的 Context，因此从本页删除。

### Agent Orchestration

- AI Router：让应用通过统一接口调用不同的 AI capability，在本地与远端模型间路由请求，并执行授权与用量策略。
- Agent Sandbox：为每个 Agent 提供 VM 级沙盒，使其能在受控环境中使用工具、模型并管理用户 Context，同时遵循明确边界。
- Agent Collaboration：通过 ACP 协议分配任务、协调执行、收集结果并监控多个 Agent 的运行状态，形成统一工作流。
- Observability：持续观察模型与 Agent 的用量、配额、权限、可靠性、执行细节与输出质量，用于系统治理。
- Learning loop：收集用户反馈来完善 Context、改进本地模型，并在不丢失用户 Context 的前提下持续优化 Agent 行为（方向性能力，不表述为已完整交付，也不承诺发布时间）。

AI Router 位于控制层，不放在 Models 列。

### Tool examples

HTML 只展示以下代表性例子，以保证投影距离可读；完整候选仍保留在本段：

- **Digital body:** redroid、Chromium、Windows VM、macOS VM
- **Physical world:** Home Assistant、Reachy Mini
- **Tools:** n8n、NocoDB

Reachy Mini 是 Hugging Face / Pollen Robotics 的开源桌面机器人，在本页作为 Agent 连接物理世界的代表。其它已调研但未在 HTML 展示的候选：Argo Workflows、Odoo、Plane、Firecrawl、Stirling PDF、Excalidraw、Flowise、Nextcloud、Twenty CRM、MTranServer、Karakeep、AFFiNE、Teable、Docmost、Crawl4AI。

### 右栏三个 Agent 设计原则

左边展示 Agent 请求如何穿过 Olares；右边解释三个不会从组件图中自然得出的设计原则（逐字稿见 [olares-skills-script.md](olares-skills-script.md)）：

1. **Native system access, not GUI automation**：GUI Agent 需要通过 pixels、Web DOM 或原生应用的 accessibility tree 操作面向人的界面；长期、带状态的系统工作因此更慢、更脆弱。Olares Skills 暴露意图级工作流，`olares-cli` 则让 Agent 通过结构化、机器可读的接口操作 applications、files、settings 与 workloads，并用 JSON、logs、events 与 metrics 闭环。能力范围从日常操作延伸到开发、部署和调试 Olares 应用。目标是 Harness 工程：Olares 写 Olares。
2. **One interface for each AI capability**：LLM 的调用接口正在趋同；图像、音频、翻译、OCR、视频模型仍各有 API、推理引擎与运行环境。Olares 按 AI 领域统一 API、模型下载和推理引擎部署，让 Agent 能用同一个领域接口调用提供相同能力的不同模型。这里不声称跨领域共用一个 API。
3. **An always-on foundation for context**：目前还没有如何构建可持续学习 Memory System 的公认范式。Olares 先从 Memory 的下一层做起：把用户散落在不同设备、操作系统和服务中的数据收集到一个 always-on、随时随地可连接的系统中。底层数据得到长期保存且保持私有后，用户才有机会尝试不同的 Memory System，而不会丢失 Context，也不会被锁定在单一 Agent 中。

HTML 只高亮每段的核心技术判断：`Olares Skills expose intent-level workflows`、统一 API / 模型下载 / 推理引擎部署、`one layer below memory`，以及底层数据长期保存并保持私有；不把整段正文加粗。

表述边界：Web 使用 DOM；原生桌面应用通常暴露 accessibility tree；视觉 Agent 还会直接依赖 pixels，三者不混写成“accessibility DOM”。Harness 工程是目标；Olares 不声称已经解决可持续学习的 Memory 范式。

### 表述边界

- 产品阶段不参与本页主叙事。
- 不声称 Agent 可以绕过身份、权限、沙盒或用户授权。
- 应用 CLI 不描述成 Olares 原生命令。
- AI Router 负责统一 capability 接口、路由、授权与用量控制；本页不展开底层模型的部署位置。
- 不暗示所有第三方 Agent 已支持同一种协作协议。
