# Olares OS：面向个人 AI、始终在线、自然语言驱动的操作系统

> Olares × Intel 对外合作 PPT 第 3 页（首个内容页）。
> 合并原第 9 页 Personal Cloud 定义与第 10 页市场叙事；产品口径见 [basic/olares.md](../../basic/olares.md)。快照 2026-07，市场数字为叙事性预测。

---

## Slide copy（中文底稿）

### 标题

**Olares OS：面向个人 AI、始终在线、自然语言驱动的操作系统**

Olares 是一个用**自然语言**操作的**开源 Personal Cloud OS**，让本地 Agent 与 AI 应用运行在**用户自己拥有的硬件**上。

### 愿景：每个人都会拥有自己的 Personal Agent

我们相信，未来每个人都会拥有自己的 Personal Agent。它可以理解成一个更好用、更强大的 OpenClaw，能够帮助我们完成工作、处理日常事务、管理个人信息和数字生活。我们可以通过手机、眼镜、音箱，当然也包括电脑，随时随地和它交互。

**Personal Cloud 就是用来运行这个 Personal Agent 的、始终在线的家。** 它让 Agent 持续运行，把完整的个人上下文放在一个地方，并让所有设备都能安全访问。Olares 是这个 Personal Cloud 的操作系统。

### What is Olares

**Olares is an open-source operating system for personal cloud.** 我们是一家专注于打造开源个人云操作系统的软件公司。

- Windows → 运行 Personal Computer
- Android → 运行 Smartphone
- Olares → 运行 Personal Cloud

### 定义个人云（Defining personal cloud）

个人云为一个人及其所有 AI 设备提供单一、始终在线、随时可访问的入口，以及统一的上下文执行环境。

- **始终在线：** 7×24 全天候、随处可用。
- **统一的上下文执行环境：**
  - 汇聚分散的数据，实现真正的所有权。
  - 为持续的、后台的多 AI 运行提供执行环境。
- **AI + 智能设备：** 连接手机、电脑、眼镜、手表、戒指等。

**关键区别：**

- 传统个人电脑为本地内网使用而设计，不适合不间断的 7×24 服务。
- 个人云需要一套根本不同的操作系统，来服务不同的用户需求。

### 在本地硬件上用个人云运行公有云级服务（Run public cloud-level services on personal cloud with local hardware）

这一转变由三个要素驱动：

1. **有竞争力的本地 LLM** — 开源权重模型已能在消费级硬件上追平去年的 SOTA。
2. **可投产的开源应用** — 已形成成熟生态，可替代 Google、Microsoft、OpenAI 的服务（Ollama、ComfyUI、Mattermost、GitLab 等）。
3. **企业级云原生基础设施** — Kubernetes、服务网格与 GPU 调度已在数据中心规模验证。

Olares 把这些整合进一个安全、易用的执行环境。

### 抓住 10% 的用户：他们为什么会选择个人云（Capturing the 10% segment: Why users will choose personal cloud）

今天，用户在云服务上只能在少数几家巨头之间做选择：Google、Meta、Apple、OpenAI、Microsoft。

对 90% 的用户来说，这仍是最省事的选择。但那 10% 的用户——尤其是高级用户、homelabber 和小企业——需要一个替代方案：

- **隐私与合规：** 对个人数据拥有完整的所有权与控制权。
- **性能：** 低延迟的本地 AI 推理。

Olares 把个人云带来，作为对现状的必要替代。

### 个人云是未来的万亿美元市场（The personal cloud is a future trillion-dollar market）

我们正处在算力需求爆发式增长的临界点。

- **100×** — 个人算力需求的预计增长。
- **$10T** — 全球公有云年收入（10 倍增长）。
- **$1T** — 个人云市场只需承接其中 10%。

### 个人云市场将在 2027 年爆发（The personal cloud market will explode in 2027）

目前，消费级硬件还不足以运行最好的 AI 模型。基于清晰的历史趋势，这一点将在 2026 年改变。

**2027 年的起飞**

- 到 2026 年底，2025 年最好的 AI 工具将能在消费级显卡上本地运行。
- 所有在 2025 年支撑起 1 亿美元 ARR 规模场景的模型，都将能在消费级显卡上本地运行。

**AI 正变得更小更强**

每年，顶尖 AI 模型的体积都会缩小 10 倍。面向消费级硬件的新开源模型，性能已经能追平上一年的 SOTA。

- 2022 SOTA (GPT-3.5) → 2023 消费级 (Llama2:13B)
- 2023 SOTA (GPT-4) → 2024 消费级 (Gemma-2:27B)
- 2024 SOTA (GPT-o1) → 2025 消费级 (Qwen3-30B-A3B)
- 2025 SOTA (Claude Opus 4.5) → 2026 消费级 (Qwen3.6-27B)

---

## 工作底稿（备查）

- 视觉顺序：Olares / Personal Cloud 定义 → 本地运行公有云级服务 → 10% 用户动因 → `$1T` 市场 → `late 2026 → early 2027`。
- 左下生态图把「依赖分散的公有云服务」与「在 Olares Personal Cloud 上运行开源替代」放在同一视觉关系中，辅助解释三项必要基础，不替代文字论证。
- 2026 是本地模型与工具达到可用门槛的技术拐点；市场起飞时间统一为 2027 年初。
- `$10T`、`10%` 与 `$1T` 是叙事性市场测算，不是官方财务预测。
- Olares 不是 NAS 或 AI PC；NAS、Box、PC、树莓派与集群只是可运行的硬件载体。
