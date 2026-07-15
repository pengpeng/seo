# Panther Lake SoC for AI Box & NAS

一台具备 NAS、个人云和 Windows VM 能力的完整 Olares AI Box——当前以 Private Meeting AI 为主打，随着模型进步继续扩展到 Smart Home 与 Personal Agent。

## THE CASE｜立论

### 会议智能已经是一个大规模付费市场——而且有两种形态

- **一个大且快速增长的市场。** AI 会议助手 2025 年市场规模估计为 $3.1–3.5B；预测 2030 年突破 $9B，年增长约 25%。
- **硬件录音端把线下对话变成付费产品。** Plaud 采用 $185 设备 + $240/年订阅，已达到 >2M 台设备和 >$100M 软件 ARR。
- **会议软件把线上对话变成付费产品。** Otter.ai 披露 >35M 用户、累计处理 >1B 场会议，ARR >$100M。

### 但主流付费产品仍依赖云端 AI 处理

- **第三方处理增加治理难度。** 音频或转写进入云端 AI 后，机构更难按 HIPAA 与 GDPR 管控数据驻留、访问和保留期限。
- **敏感对话就是日常工作。** 律师、医生、销售与记者需要由机构掌控这些知识存放在哪里。

## THE SOLUTION｜解决方案

### Private Meeting AI 当下就适合 Panther Lake：小模型、异步处理

| 环节 | 做什么 | 开源模型 | 层级 |
|------|--------|----------|------|
| 说话人分离 | 标出谁在何时说话 | pyannote · WeSpeaker | 必选 |
| 语音转文字 | 音频转文本 | Qwen3-ASR-1.7B | 必选 |
| 强制对齐 | 逐词点选回放 | Qwen3-ForcedAligner-0.6B | 必选 |
| 翻译 | 跨语言转写 | MADLAD-400 | 可选 |
| 总结 / 问答 | 会议摘要、向会议提问 | Qwen3-4B · Phi-4-mini | 可选 |

- **Private Meeting AI 需要一条五阶段本地模型管线；**三个必选环节以 Panther Lake NPU / CPU 为目标，无需独立 GPU。

### 一台完整的 Olares AI Box——以 Private Meeting AI 为主打场景

- **Intel SoC 让团队经济性成立。** Plaud 五人订阅三年约 $3,600；一台目标价 $999–1,599 的本地盒子，对应约 10–16 个月硬件回本。
- **Olares 让方案开箱即用。** 预集成模型、随时随地访问、团队协作、身份权限与应用沙盒，把 SoC 变成可直接使用的产品。
- **机构控制，从设计开始。** 音频、转写与知识留在机构自己的硬件上，减少第三方云端处理暴露。

## ECOSYSTEM & NEXT｜生态与下一步

### 从 IoT 采集设备到会议软件：开放生态汇入同一个本地知识库

- **随时随地采集对话。** 录音卡、AI 耳机、会议音箱、手机、穿戴与会议室系统覆盖面对面、电话和移动办公。
- **把线上会议带入同一系统。** 规划中的 Zoom、Teams 与 Google Meet 连接器把转写统一沉淀到本地。
- **从已确认的录音设备伙伴开始。** Mobvoi 出门问问（HKEX: 2438）带来 TicNote Card 与 4G 双通道 TicNote Pods。

### 从 Private Meeting AI 起步；随本地模型能力提升扩展场景

- **Now — Private Meeting AI。** 小模型和异步处理与当前 Panther Lake 能力匹配。
- **Next — Smart Home voice。** 复用常在线盒子、麦克风与本地语音栈。
- **Later — Personal Agent。** 随小模型质量与长上下文 prefill 改善，同一批装机继续承接 Agent 工作负载。
