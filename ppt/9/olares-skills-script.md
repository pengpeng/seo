# 第 9 页逐字稿 · Olares 如何管理 Agent

> 配套 slide：[olares-skills-slide.md](olares-skills-slide.md) / [olares-skills-slide.html](olares-skills-slide.html)；能力底稿：[olares-cli-notes.md](olares-cli-notes.md)。

## 逐字稿

### 开场

这页讲的是 Agent 与人、Agent 与 Agent、Agent 与软件、Agent 与数据这四组关系。只有先想清楚这些关系，才知道架构该是什么样。

Olares 在很长一段时间里都没有碰这一块——因为在 2025 年之前，LLM 与 Agent 的边界还不清晰。

左边这条链路展示一项 Agent 请求如何穿过 Olares，其中 Tools、Models 与 Context 共同组成 Agent Capability Layer。右边解释三个 Agent-native 设计原则：第一，Agent 需要原生的系统接口，而不是继续模拟人操作 UI；第二，Olares 按 AI 领域统一 API、模型下载和推理引擎部署，让 Agent 能以同一个领域接口调用不同模型；第三，在 Memory 范式尚未成熟时，Olares 要先成为一个 always-on、能够长期保存并连接用户全部数据的系统。

<!-- 下文待补：沿架构 01→05 逐层讲，再落到右栏三个 Agent 设计原则。 -->
