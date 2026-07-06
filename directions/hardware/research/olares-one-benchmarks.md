# Olares One 官方性能实测（单一事实源）

> hardware 方向所有报告 / content 引用 Olares One 本地 AI 性能数字，**以本文件为准**。数据全部来自 Olares 第一方实测，勿凭常识改写；引用前如有更新以官方原文为准。
>
> 来源：
> - [Local AI Hardware Performance Benchmarking](https://www.olares.com/blog/local-ai-hardware-performance-benchmarking/)（Olares Blog，发布 2025-11-04，测于 2025-10-22）
> - [Olares 1.12.5: DGX Spark Support and GPU Management Improvements](https://www.olares.com/forum/t/olares-1-12-5-dgx-spark-support-and-gpu-management-improvements/50)（Olares Forum，2026-03-27）

---

## 一、对比机型与售价

> benchmark 博客里 Olares One 标 **$2,999（众筹价）**；devices.md 主口径为 **$3,999（零售价）**。写作时：默认 $3,999；做"性价比峰值"叙事（如 vs Mac Studio M4 Max $2,699）时可用 $2,999，并注明"众筹/测试时价"。

| 机型 | 关键配置 | 内存 | OS | 价格（原文口径） |
|------|---------|------|----|--------|
| **Olares One** | Intel Core U9 275HX + **NVIDIA RTX 5090 Mobile 24GB VRAM** | 96 GB | Olares OS | **$2,999**（众筹）/ $3,999（零售） |
| Mac Studio (M3 Ultra) | M3 Ultra 32C CPU / 80C GPU | 96 GB 统一 | macOS | $5,499 |
| Mac Studio (M4 Max) | M4 Max 16C CPU / 40C GPU | 64 GB 统一 | macOS | $2,699 |
| MacBook Pro (M4 Pro) | M4 Pro 14C CPU / 20C GPU | 24 GB 统一 | macOS | $2,399 |
| Mac Mini (M4) | M4 10C CPU / 10C GPU | 16 GB 统一 | macOS | $799 |
| **Beelink GTR9 Pro** | **AMD Ryzen AI Max+ 395**（Strix Halo）+ Radeon 8060S | 128 GB 统一 | Windows | $2,099 |

> 说明：Beelink GTR9 Pro = 组一 Strix Halo 代表；Mac Studio/mini = 组一 Apple Silicon。测试**未含** GB10（DGX Spark）与 RTX 5090 游戏本/dGPU——那些组的对比走推理，不引本表数字。

---

## 二、测试方法

- **框架**：Ollama（v0.12.5）、vLLM（v0.11.0）、Llama.cpp（GPT-OSS-120B 用 `full-cuda-b6755`）；跑分工具 EvalScope（ModelScope）。
- **LLM 指标**：token 生成率 tok/s，测并发 1 / 2 / 4 / 8（越高越好）。
- **图像**：Flux.1 dev，1024×1024，20 steps；测冷启动（首图，含模型加载）与热缓存（后续图）。Olares One 用 Nunchaku FP4（50 系原生优化）；Apple 用 FP16（不支持 FP4/INT4，FP8 加速路径是 CUDA 专属）。
- **视频**：Wan 2.2 14B（672×480，121 帧）与 LTX-Video 2B 0.9.5（768×512，97 帧）。
- **模型选取**（按 LMSys Chatbot Arena，取可本地跑的开源）：Qwen3-30B-A3B-Instruct（MoE）、GPT-OSS-120B（FP4）、GPT-OSS-20B、Gemma3-27B（dense）、Gemma3-12B。
- 未超频，均为默认设置。

---

## 三、LLM 结果（tok/s，并发 1 → 8）

| 模型 | Olares One | Mac Studio M3 Ultra | Mac Studio M4 Max | Beelink GTR9 Pro | 备注 |
|------|-----------|--------------------|-------------------|-----------------|------|
| **Qwen3-30B-A3B (MoE)** | **157.17 → 81.26**（vLLM）｜106.67 → 31.94（Ollama）| 84.09 → 24.93 | 81.18 → 19.88 | 61.21 → 11.68（最低）| Olares One 全场最高 |
| **GPT-OSS-120B (FP4)** | 36.16 → 4.44（llama.cpp，>24GB 需 offload）| **69.39 → 19.05（最高）** | — | 33.97 → 2.54 | **Olares One 唯一劣势项**：显存装不下 |
| **GPT-OSS-20B** | **139.00 → 72.20**（vLLM）｜123.76 → 43.76（Ollama）| 次于 Olares One（Apple 最快）| < M3 Ultra | — | Olares One 最高 |
| **Gemma3-27B (dense)** | **38.02 → 28.81**（vLLM）｜29.75 → 7.51（Ollama）| 27.51 → 4.64（高并发崩）| 21.60 → 3.12 | 10.28 → 1.26（最低）| Olares One 最高，dense 下差距最大 |
| **Gemma3-12B** | **71.94 → 61.17**（vLLM，最高）| 50.67 → 9.75 | 42.53 → 6.46 | 21.72 → 3.44 | MacBook Pro M4 Pro 27.28 → 3.21；Mac Mini M4 最低 |

**读法**：
- **并发即分水岭**：Olares One（vLLM）在并发 8 仍保住高吞吐；Apple/Beelink 随并发**急剧衰减**（Gemma3-27B 上 M3 Ultra 从 27.5 掉到 4.6）。→ 适合对外 API / 多用户 / agent 工作流。
- **dense 模型差距最大**：Gemma3-27B（dense）Olares One 领先幅度远大于 MoE，Beelink 几近不可用（1.26 tok/s @并发8）。
- **唯一输的一项**：GPT-OSS-120B，因 24GB VRAM 装不下需 offload；M3 Ultra 靠 96GB 统一内存反超——这是必须诚实说明的边界。

---

## 四、图像 / 视频结果（秒，越低越好）

| 任务 | Olares One | Mac Studio M3 Ultra | Mac Studio M4 Max | 备注 |
|------|-----------|--------------------|-------------------|------|
| **图像 Flux.1 dev** 冷/热 | **15.51s / 8.32s** | 88.08s / ~73s | 135.83s / — | Olares One 比 M3 Ultra 快 **5.7x（冷）/ 8.8x（热）** |
| **视频 Wan 2.2 14B** 冷/热 | **142.03s / 97.79s** | 不支持 | 不支持 | Apple Silicon 不支持此模型，**仅 Olares One 能跑** |
| **视频 LTX-Video** 冷/热 | **45.38s / 32.21s** | 98.56s / 88.84s | 慢于 M3 Ultra | MacBook Pro M4 Pro 最慢 |

> 媒体生成是差距最悬殊的场景：专用 24GB CUDA GPU + 50 系原生 FP4 让 Olares One 数量级领先，部分模型 Apple 直接跑不了。

---

## 五、兼容性矩阵（能否成功跑）

| | Olares One | Mac Studio M3 Ultra | Mac Studio M4 Max | MacBook Pro M4 Pro | Mac Mini M4 | Beelink GTR9 Pro |
|---|---|---|---|---|---|---|
| Qwen3-30B-A3B | ✅ | ✅ | ✅ | 未测 | ✅ | ✅ |
| GPT-OSS-120B | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| GPT-OSS-20B | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Gemma3-27B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Gemma3-12B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 图像 Flux | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| 视频 Wan 2.2 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 视频 LTX-Video | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |

> **Olares One 是唯一跑完全部 LLM + 图像 + 视频测试的机器。** Beelink 因无 CUDA、Apple 因不支持部分模型/FP4，均有多项跑不了。（原文矩阵个别单元字符渲染有损，此处按正文逐项复核填写。）

---

## 六、三条诚实结论（写作口径）

1. **Olares One 强在三点**：① 吞吐——尤其 vLLM 高并发不衰减，适合 API/多用户/agent；② 媒体生成——图像 5.7–8.8x、视频数量级领先，部分 Apple 跑不了；③ **兼容性最广**——唯一全部跑通。底层原因：24GB VRAM（对标桌面 4090）+ 50 系原生 FP4 + Olares OS 开箱即用（Olares Market 一键部署、安全远程 URL、Olares Studio 开发调试）。
2. **诚实边界**：**24GB VRAM 天花板**——GPT-OSS-120B 这类超大模型装不进显存需 offload，会输给 Mac Studio 96GB 统一内存。要跑 120B+ 大 MoE / 大 dense，统一内存机型有其位置。写对比时主动承认，别回避。
3. **对手定位**：
   - **Mac Studio（统一内存）**：能装大 MoE，但**并发崩溃、prefill 弱、贵**——更适合单用户聊天，不适合对外服务/agent；M4 Max 性价比优于 M3 Ultra。
   - **Beelink / Strix Halo（AMD AI Max+ 395）**：MoE 尚可，但 **dense 与并发都崩、无 CUDA**——不适合对外 API 服务与媒体生成。注：同芯其它整机因 OEM 功耗调校等，单并发 GPT-OSS-120B 或高约 30%，但不改变架构层面的结论。

---

## 七、事实更新（1.12.5，2026-03-27）

- **NVIDIA DGX Spark 官方已支持安装 Olares**（有官方安装指南）；装完可从 Olares Market 一键部署 AI 应用。→ GB10（Grace Blackwell）组的"信息 B"从"有望/[unverified]"升级为 **已确认支持**（devices.md 组二 GB10 已同步）。
- **GPU 管理**：三种 GPU 模式（time slicing / memory slicing / app exclusive）均支持自动调度；升级保留 GPU 配置。
- **Olares Market 新增应用**（轴 1「开箱即用 AI 生态」实证）：OpenClaw（本地个人 AI 助手）、LibreChat、Agent Zero、PaddleOCR、ACE-Step 1.5、JupyterHub、Firefly III、FreshRSS 等。
- 特别鸣谢 Kickstarter 支持者——印证 Olares One 走过众筹（$2,999 为众筹早鸟价）。

---

*本文件为事实源，更新时同步 [devices.md](/Users/pengpeng/seo/directions/hardware/devices.md) 开篇的价格/支持口径。*
