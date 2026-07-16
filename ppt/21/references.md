# Slide 21 参考资料 · 异构加速资源管理

> 用于核查 Slide 21 主画面与后续逐字稿。Olares 代码仓库快照：2026-07。用户提供的演讲稿属于本页叙事来源；实现状态以公开仓库与文档为准。

加速计算芯片清单、在售口径与厂商来源见 [2026 本地 AI 加速计算芯片图谱](/Users/pengpeng/seo/research/local-ai-compute-accelerators-2026.md)。

本页十五模型、九个 Market AI runtimes、Intel 2023–2026 AI PC 产品线、企业 dGPU 与分配模式复核见 [2026 本地开放模型、AI Runtime 与企业加速资源研究](/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.md)。

## 一、演讲稿提炼

### 1. 家庭算力不应随换机被淘汰

- 用户购买新硬件后，不需要丢弃旧 PC、NAS 或 AI 设备，而是把它们继续加入同一个 Olares 集群。
- 长期形态会是多节点、异构的家庭算力池：NVIDIA 独显、Intel 独显与新一代 SoC、NVIDIA GB10 / DGX Spark、AMD APU、Apple Silicon 等设备并存。
- 设备可能分布在多个节点；同一节点也可能包含多种计算设备。
- Olares 的目标不是要求用户理解每种硬件，而是让用户和 Agent 以一致、可预期的方式使用整个算力池。

### 2. 第一层抽象：加速资源

演讲稿对“支持一种硬件”的定义，不是把设备节点以 root 权限直接挂进容器，而是完成一条系统链路：

1. 发现节点与加速设备。
2. 安装或保留宿主机驱动与容器运行时。
3. 安装 Kubernetes device plugin，或建立等价的节点调度契约。
4. 将设备、显存或统一内存注册为可调度资源。
5. 提供应用绑定、释放、超分与资源检查。
6. 提供利用率、显存、温度、健康状态等可观测性。
7. 在设备异常、节点压力或资源不足时阻止错误调度并给出恢复路径。

不同硬件最终对上暴露为一致的 compute mode、资源需求和应用生命周期。实现成熟度可以不同，但上层接口保持稳定。

### 3. 第二层抽象：资源分配方式

- **时间分片**：名称来自多个应用按时间轮流使用整张 GPU；每个应用在自己的时间片内看到完整设备。适合同时保持多个 GPU 应用或模型实例可用，但不要求它们在同一时刻执行；Engine Base 文档明确说明 llama.cpp、vLLM、SGLang 等实例遵循 Olares 时间分片调度。
- **显存分片**：名称来自把 VRAM 划分为固定配额，使多个应用并发驻留。适合需要控制每个应用显存占用的组合；ComfyUI、Speaches、Whisper-WebUI 与模型服务文档均提供显存配额相关操作或排障。
- **独占**：名称来自一款应用独占整张设备，其他应用在释放前无法绑定。适合追求最大性能或稳定性的大型 LLM、ComfyUI 渲染、Isaac Lab / Sim 与高端游戏。
- 统一内存设备没有独立显存池，资源需求以 Pod 内存表达；这属于设备内存模型，不是第四种 GPU 分享模式。

主要依据：

- [Olares One：Manage accelerator resources](/Users/pengpeng/Olares/docs/one/gpu.md)
- [Manual：GPU modes and usage](/Users/pengpeng/Olares/docs/manual/olares/settings/gpu-resource.md)
- [Engine Base shared apps](/Users/pengpeng/Olares/docs/zh/manual/olares/market/shared-apps.md)
- [ComfyUI common issues](/Users/pengpeng/Olares/docs/use-cases/comfyui-common-issues.md)
- [Speaches troubleshooting](/Users/pengpeng/Olares/docs/use-cases/speaches.md)
- [Whisper-WebUI troubleshooting](/Users/pengpeng/Olares/docs/use-cases/whisper-webui.md)
- [Isaac Lab recommended GPU mode](/Users/pengpeng/Olares/docs/use-cases/isaac-lab.md)
- [ComfyUI for Krita](/Users/pengpeng/Olares/docs/use-cases/comfyui-for-krita.md)

### 4. 模型厂商、芯片厂商与 Olares 的分工

1. **模型厂商**：发布高精度原始权重和模型架构，通常不会为每一种终端芯片完成量化、算子和运行时适配。
2. **芯片厂商**：
   - 让 llama.cpp、vLLM、SGLang 等主流推理引擎能够通过自己的 runtime / driver 使用硬件。
   - 针对硬件改进 kernel、算子、内存管理与执行图。
   - 对主打边缘侧或特殊精度的芯片，为热门模型提供官方量化和经过验证的运行参数。
3. **Olares OS**：
   - 将不同后端打包为对应镜像和应用模式。
   - 根据节点能力完成安装、部署、资源选择、调度、释放和观测。
   - 向应用与 Agent 提供稳定资源契约，避免每增加一种芯片就重写上层产品。

对 Intel 的合作表述应落在正向分工上：Intel 把模型高效地跑在 Intel 硬件上；Olares 把这些能力变成用户可以安装、调度和持续使用的产品体验。

## 二、Olares 两层抽象的仓库依据

### 1. 统一 compute mode

Olares 使用 `gpu.bytetrade.io/<mode>` 节点标签和应用 `spec.accelerator[]` 声明建立统一资源契约。

| Mode | 目标设备 | 内存模型 | 当前状态 |
|------|----------|----------|----------|
| `nvidia` | NVIDIA dGPU | 独立显存 | 完整度最高：驱动、HAMi、device plugin、调度与监控 |
| `nvidia-gb10` | NVIDIA GB10 / DGX Spark | 统一内存 | 已有识别、标签与分配逻辑；保留厂商驱动 |
| `amd` | AMD Ryzen AI Max iGPU | 统一内存 | 已有 ROCm、AMD container toolkit 与 device plugin 路径 |
| `intel` | Intel iGPU | 统一内存 | 已有发现、标签与节点调度；无独立 Intel device plugin |
| `moore-soc` | Moore Threads SoC | 统一内存 | 已有识别与标签；MUSA device plugin 未启用 |
| `apple-m` | Apple M 系列 | 统一内存 | Manifest / 镜像模式；Linux host 管理链路未实现 |
| `intel-gpu` | Intel dGPU | 独立显存 | Manifest 模式已定义；host runtime management 未完成 |
| `amd-gpu` | AMD dGPU | 独立显存 | Manifest 模式已定义；host runtime management 未完成 |
| `cpu` | CPU-only | 系统内存 | 每个节点隐式支持，不属于加速设备 |

依据：

- [Compute mode 常量](/Users/pengpeng/Olares/cli/pkg/gpu/types.go)
- [Manifest accelerator 资源模型](/Users/pengpeng/Olares/framework/oac/internal/manifest/resources.go)
- [应用打包与 accelerator modes](/Users/pengpeng/Olares/cli/skills/olares-chart/references/olares-chart-accelerator.md)
- [节点支持模式读取](/Users/pengpeng/Olares/framework/app-service/pkg/utils/gpu_types.go)
- [自动选择 compute mode](/Users/pengpeng/Olares/framework/app-service/pkg/compute/auto_select.go)

### 2. 发现、驱动与 device plugin

- NVIDIA 通用 Linux 节点包含 CUDA、NVIDIA Container Toolkit、HAMi 与 device plugin 安装流程。
- GB10 / DGX Spark 识别后使用 `nvidia-gb10` 标签，并保留设备厂商提供的驱动栈。
- AMD Ryzen AI Max 路径包含 ROCm、AMD container toolkit、CDI 与 AMD device plugin。
- Intel iGPU 当前通过发现、节点标签和 node selector 调度，没有单独的 Intel device plugin。

依据：

- [GPU install pipeline](/Users/pengpeng/Olares/cli/pkg/pipelines/gpu_install.go)
- [NVIDIA GPU module](/Users/pengpeng/Olares/cli/pkg/gpu/module.go)
- [AMD GPU tasks](/Users/pengpeng/Olares/cli/pkg/gpu/amdgpu/tasks.go)
- [Intel GPU tasks](/Users/pengpeng/Olares/cli/pkg/gpu/intelgpu/tasks.go)
- [HAMi device plugin](/Users/pengpeng/Olares/infrastructure/gpu/.olares/config/gpu/hami/templates/device-plugin/daemonsetnvidia.yaml)
- [AMD device plugin](/Users/pengpeng/Olares/infrastructure/gpu/.olares/config/gpu/nvidia/amdgpu-device-plugin.yaml)

### 3. 三种分配方式

Olares 用户文档定义 Time slicing、Memory slicing 和 Exclusive 三种 GPU 分享方式。不是所有设备都支持全部三种模式；界面只展示目标设备可用的模式。

- **Time slicing**：仅 `nvidia`（NVIDIA dGPU）；它是 NVIDIA dGPU 的默认模式。启动前把 Pod RAM + 独立显存计入 90% 节点内存压力门槛。
- **Memory slicing**：`nvidia`、`nvidia-gb10`、`intel`、`amd`、`moore-soc`；GB10 与 Intel/AMD/Moore 统一内存模式默认使用该方式。CPU fallback 也是 MemorySlice-only，但不属于加速芯片。
- **Exclusive**：所有加速设备 mode 均可用；`apple-m`、`intel-gpu`、`amd-gpu` 当前只暴露 Exclusive，其中 host integration 成熟度不同。
- **模式切换**：先预检已绑定应用是否可停止；随后提交停止操作、立即释放 allocation / HAMi binding 并写入新的 share-mode annotation；应用之后需要恢复并重新绑定。

主画面是面向 Intel 的展示子集：Time slicing 仅标 `NVIDIA dGPU only`；Memory slicing 标 `Intel CPU · Intel GPU · NVIDIA dGPU · GB10`；Exclusive 只标 `All modes`。这不覆盖代码矩阵中的 AMD 与 Moore 路径。

三种模式通过同一 application resource contract 暴露；应用按 Manifest 声明可用模式和对应镜像，不需要为 Time slicing、Memory slicing、Exclusive 分别重写业务逻辑。因此主标题使用 “transparent to apps, with no code changes”，不表示所有镜像天然支持所有硬件。

Time slicing 的专辑示例用于解释无感轮转：每首单曲依次由 LLM 写歌词、ACE-Step 1.5 XL 生成音乐、Z-Image 生成封面，再对下一首重复。在目标 24GB 设备上，这些阶段可能分别占用大部分显存，无法舒适并存；若手工执行，用户需要反复停止模型、释放并重新绑定 GPU。Olares 隐藏 stop / re-bind / mode-switch 操作，让流程呈现为连续工作流。这不是三个应用并行占用同一 GPU 的声明，实际显存取决于模型、量化、上下文和生成参数。

依据：

- [Manage accelerator resources](/Users/pengpeng/Olares/docs/one/gpu.md)
- [Compute scheduler modes](/Users/pengpeng/Olares/framework/app-service/pkg/compute/types.go)
- [Available support types](/Users/pengpeng/Olares/framework/app-service/pkg/compute/store.go)
- [Device mode switching](/Users/pengpeng/Olares/framework/app-service/pkg/compute/device_mode.go)

### 4. 应用对多后端的声明与镜像

- 一款应用可以在 `spec.accelerator[]` 中声明多个 compute modes。
- 不同模式通常需要不同架构或后端镜像，例如 CUDA、ROCm、Metal、oneAPI / SYCL 或纯 CPU。
- Olares 根据节点标签、应用支持模式、CPU 架构和显存 / 内存需求选择可运行资源。
- 新硬件的系统适配遵循固定链路：`detect → driver/runtime → node label → optional device plugin → scheduler/webhook → observability`。

依据：

- [Accelerator resources and image variants](/Users/pengpeng/Olares/cli/skills/olares-chart/references/olares-chart-accelerator.md)
- [OAC image rendering](/Users/pengpeng/Olares/framework/oac/images.go)
- [Pod resource injection](/Users/pengpeng/Olares/framework/app-service/pkg/apiserver/handler_webhook.go)
- [Scheduler](/Users/pengpeng/Olares/framework/app-service/pkg/compute/scheduler.go)

Application allocation 上半区四点的实现边界：

1. **镜像与资源申请配对**：同一 chart 可按 compute mode 渲染不同 workload image；Manifest 的 `spec.accelerator[]` 同时声明 mode、架构与资源需求。
2. **安装或启动前分配**：安装路径由 `AllocateForInstall` 选择并持久化 allocation；恢复/启动路径通过 `ApplyBindingSelection` 让用户选择单卡、多卡或跨节点资源。
3. **优先级调整**：当前 compute scheduler 未发现基于应用优先级的自动 GPU 抢占或重平衡。资源不足时，UI 展示冲突并让用户移除已分配应用、选择其他 GPU 或稍后重试；因此主画面将策略化 priority adjustment 标为 `Next`。
4. **可预期 UI**：Settings > Accelerator 展示设备、模式、配额和 assigned apps；切换模式、释放资源和恢复应用都有明确确认、停止与重新绑定流程。

补充依据：

- [Mode-specific image rendering](/Users/pengpeng/Olares/framework/oac/images.go)
- [Install allocation](/Users/pengpeng/Olares/framework/app-service/pkg/compute/scheduler.go)
- [Resume binding selection](/Users/pengpeng/Olares/framework/app-service/pkg/compute/availability.go)
- [Resume API handler](/Users/pengpeng/Olares/framework/app-service/pkg/apiserver/handler_suspend.go)
- [GPU resource UI workflow](/Users/pengpeng/Olares/docs/one/gpu.md)
- [Settings GPU UI](/Users/pengpeng/Olares/apps/packages/app/src/pages/settings/GPU/GPUPage.vue)

### 5. 可观测性与故障处理

- HAMi 集成 DCGM exporter，提供 NVIDIA GPU 利用率、显存、温度和健康状态。
- app-service 同时检查设备健康、节点 Ready 状态、资源余量和时间分片时的系统内存压力。
- Dashboard 与 Settings 向用户展示节点、GPU 型号、显存、当前模式和已分配应用。

依据：

- [HAMi values and DCGM exporter](/Users/pengpeng/Olares/infrastructure/gpu/.olares/config/gpu/hami/values.yaml)
- [Accelerator resource store](/Users/pengpeng/Olares/framework/app-service/pkg/compute/store.go)
- [Dashboard GPU implementation](/Users/pengpeng/Olares/cli/pkg/dashboard/overview/gpu/list.go)
- [GPU user workflow](/Users/pengpeng/Olares/docs/one/gpu.md)

### 6. 本页四层技术栈与两项开发者价值

主画面按 `01 → 04` 自上而下压缩为四层：

| 层 | 主画面文案 | Olares / HAMi 依据 |
|----|------------|--------------------|
| 01 | Drivers & runtimes | NVIDIA driver + Container Toolkit、AMD ROCm + CDI、Intel 检测与厂商 runtime；见 [NVIDIA module](/Users/pengpeng/Olares/cli/pkg/gpu/module.go)、[AMD tasks](/Users/pengpeng/Olares/cli/pkg/gpu/amdgpu/tasks.go)、[Intel module](/Users/pengpeng/Olares/cli/pkg/gpu/intelgpu/module.go) |
| 02 | Device exposure | HAMi device plugin 暴露 `nvidia.com/gpu` / `nvidia.com/gpumem`；AMD plugin 暴露 `amd.com/gpu`；无 plugin 的模式使用节点标签契约；见 [HAMi device plugin](/Users/pengpeng/Olares/infrastructure/gpu/.olares/config/gpu/hami/templates/device-plugin/daemonsetnvidia.yaml)、[AMD plugin](/Users/pengpeng/Olares/infrastructure/gpu/.olares/config/gpu/nvidia/amdgpu-device-plugin.yaml) |
| 03 | Contract & injection | `gpu.bytetrade.io/<mode>` 标签、app-service compute scheduler、HAMi `GPUBinding` 与 GPU-limit mutating webhook；见 [compute-mode labels](/Users/pengpeng/Olares/cli/pkg/gpu/types.go)、[scheduler](/Users/pengpeng/Olares/framework/app-service/pkg/compute/scheduler.go)、[HAMi binding](/Users/pengpeng/Olares/framework/app-service/pkg/compute/hami.go)、[GPU-limit webhook](/Users/pengpeng/Olares/framework/app-service/pkg/apiserver/handler_webhook.go) |
| 04 | Observability & health | HAMi device registry、DCGM exporter、Prometheus node pressure、NodeReady 与 device health；见 [HAMi values](/Users/pengpeng/Olares/infrastructure/gpu/.olares/config/gpu/hami/values.yaml)、[resource store](/Users/pengpeng/Olares/framework/app-service/pkg/compute/store.go)、[pressure checks](/Users/pengpeng/Olares/framework/app-service/pkg/compute/pressure.go) |

`GPU-limit mutating webhook` 是准确名称：它向 Deployment / StatefulSet 注入 resource limits、runtimeClass、nodeSelector 和 GPU 环境变量；设备与节点选择由 app-service compute scheduler 完成，不能笼统写成“admission webhook 负责调度”。

下方左 comment box 严格作为**开发者价值**，不复述上方 01→04 的组件层（不出现 OpenVINO/CUDA/plugin/Prometheus 等名词），两点为“加速资源的生命周期管理”和“加速资源的可组合性”：

1. **加速资源的生命周期管理**：Olares 把加速资源从宿主驱动安装、设备发现、容器运行时、应用调度、资源绑定、用量监控到故障剔除的完整生命周期抽象为统一接口。厂商实现按目录组织（`cli/pkg/gpu/nvidia`（module.go）、`cli/pkg/gpu/intelgpu`、`cli/pkg/gpu/amdgpu`、`cli/pkg/gpu/mtgpu`），接入新设备主要在各自模块内实现这些生命周期阶段。
   - **边界（避免 overclaim）**：主画面写“在自己模块内实现接口”，但接入新设备当前仍需同步少量共享项——compute-mode 常量（`cli/pkg/gpu/types.go`）、OAC/Manifest mode 校验、节点标签与 resource key；因此不写“零系统改动”，而是“无需在系统各处零散改代码”的方向性表述。
2. **加速资源的可组合性**：单节点单资源、同种资源多实例、多种异构资源、跨节点资源与外部 eGPU，均可通过两层绑定给应用——软件层（开发者在 `spec.accelerator[]` 声明可用 mode 与资源）与系统层（用户在安装/恢复时分配设备与配额）。
   - **边界**：跨节点仍限同架构、同 OS（`docs/developer/develop/package/extension.md` L33、`docs/one/faq.md`）；多卡/跨节点自动化当前主要走 NVIDIA 路径；eGPU 为冷插拔；跨 AMD64/ARM64 全自动异构池属 `Next`。

措辞边界（避免 overclaim）：**分配策略（Time/Memory/Exclusive）对应用透明，但硬件/backend 不是**——应用仍需为每个 mode 提供可运行镜像，CUDA-only 上游不会因声明 `apple-m` 而自动跑在 Apple GPU 上。

HAMi 与 Olares 的职责不要混写：

- **HAMi**：为其支持的设备提供注册、device-aware scheduling、共享/配额、健康状态与 Prometheus 指标。
- **Olares**：完成 host 检测与驱动/runtime、未被 HAMi 覆盖的后端适配、统一资源契约、应用镜像选择、allocation 持久化和用户可见的生命周期管理。

HAMi 官方依据：

- [HAMi architecture](https://project-hami.io/docs/core-concepts/architecture)
- [HAMi device protocol](https://project-hami.io/docs/developers/protocol)
- [HAMi supported devices](https://project-hami.io/docs/userguide/device-supported)
- [HAMi real-time device usage](https://project-hami.io/docs/userguide/monitoring/real-time-device-usage)
- [HAMi allocation metrics](https://project-hami.io/docs/userguide/monitoring/device-allocation)

## 三、当前能力与未来路线

### 当前可以对外使用

- Olares 已支持同架构、同 OS 的多节点集群。
- NVIDIA dGPU 路径已覆盖驱动、设备发现、device plugin、显存感知调度、三种分配方式和监控。
- 应用可声明多个 accelerator modes，并为不同硬件提供对应镜像。
- 在 Olares One 上，受支持的 eGPU 可以被识别、注册并作为加速资源显示、分配。

### 必须标为未来路线或部分自动化

- Mac Studio、DGX Spark、AMD AI Max 与不同 CPU 架构混合组成全自动异构集群。
- 跨 AMD64 / ARM64 的镜像选择和调度目前仍需要手工介入。
- Intel dGPU、AMD dGPU、Apple Silicon host GPU 管理还不能描述为完整产品能力。
- 其他尚未完成 host management 的 accelerator modes，不应描述为与 NVIDIA 相同的调度成熟度。

依据：

- [Cluster architecture limits](/Users/pengpeng/Olares/docs/developer/develop/package/extension.md)
- [Olares One cluster FAQ](/Users/pengpeng/Olares/docs/one/faq.md)

## 四、eGPU 与热插拔边界

- Olares One 支持 NVIDIA Turing 或更新架构的 Thunderbolt 5 eGPU；eGPU 是 Olares 能管理的设备形态。
- 当前文档流程要求关机后连接或断开，这是 NVIDIA 驱动、Kubernetes device plugin 与运行中 workload 设备生命周期共同形成的端到端安全边界，不应简化为“Olares 不支持 eGPU”。
- 主画面可以表达“健康感知的设备重注册支撑 eGPU”；若要表达运行时物理热插拔，必须同时限定厂商驱动、device plugin re-enumeration 和 workload stop / drain / recovery 条件。

依据：

- [Connect to an external GPU](/Users/pengpeng/Olares/docs/one/egpu.md)
- [GPU shown in Settings / Dashboard](/Users/pengpeng/Olares/docs/one/gpu.md)

## 五、主画面的 Models、Software 与 Hardware

### Models：十五个具备可信本地路径的角色

主画面采用 3×5；前九项是核心跨模态组合，新增两行补齐 TTS、文档解析、翻译、设计图像与实时 omni：

| 角色 | 主画面型号 | 本地边界 |
|------|------------|----------|
| 多模态理解 | Gemma 4 · E4B | Google 官方确认已发布、Apache 2.0；Q4 load 约 4.5GB，规划 8–12GB |
| 文本推理 | Qwen3 · 4B | Apache 2.0；具体内存按量化、context 与 runtime 实测 |
| Agentic coding | Ornith 1.0 · 9B | MIT；官方提供 GGUF / llama.cpp / Ollama 路径 |
| 图像 | FLUX.2 · klein 4B | Apache 2.0；官方约 13GB VRAM |
| 视频 | Wan2.2 · TI2V-5B | Apache 2.0；官方实践下限 ≥24GB，且依赖 offload |
| 3D | Hunyuan3D 2.1 | shape 约 10GB、texture 约 21GB、完整默认流程约 29GB；bespoke community license |
| ASR | Qwen3-ASR · 0.6B | Apache 2.0；按 batching、音频长度与 aligner 实测 |
| 音乐 | ACE-Step 1.5 · 2B DiT | MIT；DiT-only 至少 4GB，LLM+DiT 至少 6GB |
| RAG | BGE-M3 · 568M | MIT；1024 维、8192 token，支持 dense / sparse / multi-vector |
| TTS / 声音克隆 | Qwen3-TTS · 0.6B | Apache 2.0；官方未给固定显存下限 |
| OCR / 文档解析 | Baidu Unlimited-OCR · 3B-A0.5B | MIT；支持 Transformers、vLLM 与 SGLang，本地处理长文档 |
| 翻译 | Tencent Hy-MT2 · 1.8B | Apache 2.0；官方 GGUF 支持 llama.cpp |
| 轻量图像 | Z-Image Turbo · 6B | Apache 2.0；官方说明适配 16GB VRAM |
| 设计图像 | Ideogram 4 · 9.3B | 开放权重；公开 NF4 版可在单张 24GB CUDA GPU 上运行，权重为非商用许可，商业部署另行授权 |
| 实时 Omni | MiniCPM-o 4.5 · 9B | Apache 2.0；官方 llama.cpp 路径约需 12GB GPU memory |

DeepSeek V4 与 MiniMax M3 均已发布开放权重和本地 serving 路径，但最小型号仍是数百 B 总参数，属于多卡工作站/数据中心规模，因此不进入本页模型网格。完整官方来源与 P6/P7 复核见 [研究报告](/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.md)。

### Software：不再统称 Inference Engines

主画面为保持紧凑统一称为 `AI runtimes`，并以 3×3 展示九个有 Olares Market Manifest 的 package：

- **llama.cpp / vLLM / SGLang / Ollama**：核心 Engine Base / local runner 组。
- **LocalAI / Xinference**：更宽的 multi-backend 或 multi-model serving platform；当前 Olares Manifest 均仅声明 NVIDIA amd64。
- **KoboldCpp**：GGUF inference engine/server，适合本地文本生成与兼容 Kobold/OpenAI 风格 API；审计到的 Olares chart 依赖范围为 `>=1.12.3-0,<1.12.6`。
- **Speaches**：OpenAI-compatible STT/TTS model server。
- **ComfyUI**：面向图像、视频、音频与 3D 工作流的 node-based inference/workflow engine，不是通用 LLM server。

九项只共享“执行或服务模型”的宽口径，不共享 API、硬件矩阵或成熟度。主画面只保留 `AI runtimes`；Market Manifest 存在不等于任意 Olares 版本均兼容，KoboldCpp 的 chart 版本上限仍需按目标系统核对。

OpenVINO 技术上是 inference runtime and optimization toolkit，不是硬件驱动；但在这张系统图里，它承担 Intel 硬件 enablement，视觉上应与 CUDA、ROCm、Metal 一起放在靠近硬件的 `Accelerator resource abstraction`，而不是与应用直接选择的 runtime / workflow software 并列。

### Hardware：dGPU 与 SoC

| 类别 | 厂商与具体型号 | 形态 |
|------|----------------|------|
| Discrete GPU | Intel Arc Pro B70 · B65 · B60 · B50 | 当前 B-Series |
| Discrete GPU / data-center accelerator | NVIDIA Consumer `RTX 5090 · RTX 5080 · RTX 4090 · RTX 3090`；Workstation `RTX PRO Blackwell 6000 · 5000`；Data center `B200 · H200` | 分别代表消费、专业工作站与数据中心资源层 |
| Discrete GPU | AMD Radeon AI PRO R9700 · R9600 | R9600 已进入目录但尚不可购买 |
| SoC | Intel Core Ultra Series 1（Meteor Lake）→ Series 2（Lunar Lake + Arrow Lake）→ Series 3（Panther Lake） | Integrated CPU · GPU · NPU |
| SoC | NVIDIA GB10 Grace Blackwell | CPU + GPU；coherent unified memory |
| SoC | AMD Ryzen AI Max+ 395 · Max 390 · Max 385 | CPU + iGPU + NPU；shared system memory |
| SoC | Apple M3 Ultra · M4 Pro · M4 Max · M5 Pro · M5 Max | CPU + GPU + Neural Engine；unified memory |

主画面按 pitch 采用紧凑的 `SoC · Unified memory` 分类，并删除单独 SKU。该标题表达集成计算资源与统一资源管理视角，不代表 Core Ultra Series 1–3 都采用与 Apple Silicon 相同的物理内存封装；Lunar Lake 的 on-package memory 仍是特例。

企业 dGPU 的 live catalog、世代与 availability 依据统一登记在 [研究报告第 5 节](/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.md#5-当前企业-dgpu-紧凑清单)；NVIDIA 消费卡见 [RTX 5090](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)、[RTX 5080](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/)、[RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/) 与 [RTX 3090](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/)，数据中心层见 [DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/) 与 [H200 GPU](https://www.nvidia.com/en-us/data-center/h200/)；SoC 依据保留在 [加速计算芯片图谱](/Users/pengpeng/seo/research/local-ai-compute-accelerators-2026.md)。

硬件矩阵表达 Olares 的目标资源模型和合作方向，不是当前完整支持清单。面向 Intel 的主画面不展示 HAMi，也不加入国产 GPU / NPU 厂商，避免引入制裁和供应链敏感信息。

## 六、对外措辞

### 推荐

- `Olares turns different accelerators into one resource contract for applications and Agents.`
- `Today, Olares manages same-architecture multi-node clusters; heterogeneous multi-architecture scheduling is the next step.`
- `Intel optimizes the runtime, inference engines and model formats; Olares turns that work into deployable, schedulable applications.`
- `New hardware follows a repeatable integration path, keeping most changes below the application layer.`

### 避免

- “所有九种 compute mode 都已经完整支持。”
- “Mac Studio、DGX Spark、Intel / AMD / NVIDIA 已经可以组成全自动异构集群。”
- “eGPU 支持热插拔。”
- “时间分片适用于所有加速设备。”
- “只要增加一个 mode，上层完全不需要做镜像或引擎适配。”
- “只有 NVIDIA 和 Apple 能把推理引擎和量化做好。”该判断过于绝对，也不适合面向 Intel 的合作材料。
- 直接使用 `MiniMax 30B BF16` 作为已核实的产品示例；主画面改用“模型厂商发布高精度原始权重”。
