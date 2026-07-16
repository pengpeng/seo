---
task_id: synthesis
role: Slide 21 证据综合与反向复核
status: complete
as_of: 2026-07-15
mode: Standard
sources_evaluated: 59
sources_approved: 43
---

# Slide 21 本地开放模型、运行时与加速资源综合笔记

## P0 · 范围与来源策略

- 主题模式：通用技术调研；深度：Standard；AS_OF：2026-07-15。
- 输入仅限四份已完成任务笔记；综合阶段不引入新来源。
- 冲突优先级：发布方模型卡/代码库与许可证 > GPU 厂商当前目录 > Olares 代码与 Manifest > 内部研究清单/SEO 报告 > 现有 Slide 文案。
- Slide 21 的推荐边界是“具有可信单机本地路径的 Open & open-weight models”，不是把所有已发布旗舰模型都列入。

## P2 · 四任务结论蒸馏

### 1. 九个推荐模型

最终固定为 3×3、恰好九个 family：

1. Gemma 4 · E4B：多模态理解与推理；Gemma 4 已由 Google 官方模型卡、总览和 release log 三重核验，绝非占位符。[1][2][3]
2. Qwen3 · 4B：通用文本与推理；Apache 2.0。[4]
3. Ornith 1.0 · 9B：Agentic coding 与工具调用；MIT，提供官方 GGUF。[5]
4. FLUX.2 · klein 4B：图像生成与编辑；Apache 2.0，官方约 13GB VRAM。[6]
5. Wan2.2 · TI2V-5B：文/图生视频；官方方案即使使用 offload，实践下限仍为 ≥24GB VRAM。[7]
6. Hunyuan3D · 2.1：图生 3D 与 PBR 纹理；使用腾讯自定义 community license，不应等同于 Apache/MIT 开源。[8][9]
7. Qwen3-ASR · 0.6B：多语种语音识别。[10]
8. ACE-Step · 1.5 standard：音乐生成；标准路径低于 4GB VRAM。[11]
9. Qwen3-Embedding · 0.6B：本地 RAG embedding。[12]

DeepSeek V4 与 MiniMax M3 均已发布、可下载并提供本地 serving 路径；排除原因不是“未发布”或“只能 API”，而是其最小公开变体仍属于数据中心/多卡工作站尺度，不符合保守的单机本地硬件适配边界。[13][14][15][16]

### 2. 六个 Olares-packaged runtime / workflow

固定为：llama.cpp、vLLM、SGLang、Ollama、ComfyUI、Xinference。[34][35][36][37][38][39]

- llama.cpp、vLLM、SGLang、Ollama：Engine Base 模板，Manifest 覆盖 CPU、NVIDIA、GB10。
- ComfyUI：workflow software，Manifest 覆盖 NVIDIA、GB10。
- Xinference：共享模型服务平台，当前 Manifest 仅覆盖 NVIDIA amd64。
- OpenVINO 是 backend，不是第七个 runtime；证据只证明它被特定 Olares 应用作为 CPU 推理后端使用。[40][43]

### 3. 当前企业 dGPU 紧凑清单

- Intel：Arc Pro B70 · B65 · B60 · B50。[17][18]
- NVIDIA：RTX PRO Blackwell 6000 · 5000 · 4500 · 4000 · 2000；6000 的 Server/Workstation/Max-Q 形态不应在紧凑清单中混写为同一桌面卡。[21][22][23]
- AMD：Radeon AI PRO R9700 · R9600；R9600 有官方目录与驱动证据，但不应推导为全球广泛现货。[24][25][26][27]
- 旧代仅作补充：Intel A60/A50 已被官方标记 retired/discontinued；NVIDIA RTX 6000/5000 Ada 与 AMD W7900/W7800 可标 “Older generation”。[19][20][21][24][28]

### 4. Allocation mode chips

- **Time slicing** — NVIDIA dGPU only。
- **Memory slicing** — NVIDIA dGPU · GB10 · Intel/AMD iGPU/APU · Moore SoC。
- **Exclusive** — All accelerator modes；Apple M、Intel/AMD dGPU 当前仅 Exclusive。

显示文案采用文档中的 sentence case；代码枚举分别是 `TimeSlice`、`MemorySlice`、`Exclusive`。[29][30][31][32][41][43]

模式切换不是无中断迁移：管理员发起后，系统预检 bound apps，停止应用、清除 allocation/HAMi binding、切换模式，之后需要 resume 与重新绑定；代码不支持声称中途故障可原子回滚。[30][33]

## P3 · 全局引证映射

- [1]–[16]：模型发布、许可与硬件适配官方证据。
- [17]–[28]：Intel、NVIDIA、AMD 当前企业/工作站 dGPU 官方证据。
- [29]–[43]：Olares 文档、代码与应用 Manifest。
- task-model-catalog 的 16 个内部清单、报告、Slide 与图标来源全部列入 Dropped：它们用于发现问题，但其事实已被更高权威的发布方来源替代。

质量门：43 个 Approved，7 个独立公开域名及 3 个独立本地官方代码库，官方源占比 100%；按单一 URL 计最大占比 1/43，按单一代码库计最大占比 9/43，均不超过 25%。

## P4 · 证据映射大纲

1. 执行摘要：推荐边界、九模型、六 runtime、模式与 GPU 清单。
2. 方法与范围：AS_OF、来源优先级、open/open-weight 术语。
3. 九模型：角色、推荐变体、许可、粗略硬件边界。
4. 六 runtime：产品类别与 Manifest 覆盖差异。
5. 企业 dGPU：当前世代与旧代分层。
6. Allocation modes：精确 chips、默认行为、切换生命周期。
7. Caveats / 核心争议：许可不等价、VRAM 不是承诺、代码能力不等于端到端成熟度。
8. 关键发现、局限、完整参考文献。

## P6 · 强制反向复核

1. **“Open” 是否被说得过宽？** 是。Hunyuan3D 2.1 使用 bespoke community license，九项应统称 “Open & open-weight models”，不能宣称全部为 OSI-style open source。[9]
2. **DeepSeek V4 / MiniMax M3 是否因未发布而排除？** 否。两者均已有官方权重与本地部署说明；只因模型规模与 serving topology 不适合保守的单消费级 GPU 清单而排除。[13][14][15][16]
3. **Wan2.2 是否可按 8–12GB 宣传？** 否。发布方 TI2V-5B recipe 的实践下限是 ≥24GB，即使包含 offload；24GB 是边界条件，不是宽裕配置。[7]
4. **Hunyuan3D 是否可统一写 8–16GB？** 否。官方默认约为 shape 10GB、texture 21GB、完整流程 29GB；低值只能描述 shape-only 或非默认优化路径。[8]
5. **六个 runtime 是否共享同一硬件矩阵？** 否。四个 Engine Base、ComfyUI、Xinference 的 Manifest 覆盖不同，不能挂统一的 CPU/NVIDIA/GB10 badge。[34][35][36][37][38][39]
6. **代码枚举是否等于端到端成熟支持？** 否。Olares app-service 已暴露 AMD/Intel/Moore mode，但现有英文文档覆盖滞后；应称 code-level allocation support，不应推导为所有应用同等成熟。[30][32]
7. **当前目录是否等于当前世代或全球现货？** 否。NVIDIA 页面仍保留多代产品；AMD R9600 的目录存在也不证明广泛供货。[21][26][27]

## P7 · 溯源核验

- 抽查 9 项：Gemma 4 发布、Wan2.2 下限、Hunyuan3D 许可、DeepSeek V4 排除、MiniMax M3 排除、NVIDIA 当前型号、AMD R9600 限定、六 runtime Manifest、mode-switch 生命周期，均可追至 Approved 来源。
- 全局编号与 `registry.md`、最终报告一致；未引用任何 Dropped 来源。
- 所有四份输入笔记已以 `## END` 收尾；本综合任务笔记同样按约定结束。

## END
