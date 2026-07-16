# Olares 异构加速资源管理

> Intel 合作 PPT 第 8 页。中文 Slide 文案初稿。

---

## Slide copy

### 标题

**Unifies Heterogeneous AI Compute**（`Unifies` 绿色高亮）

一套系统完成加速资源的发现、接入、调度、共享与可观测，同时让应用与底层硬件解耦。

### 上半区 · 一条连续架构

**加速计算资源 | Accelerator resources | Application allocation | Models & AI Runtimes**

| 加速计算资源 · 22% | Olares OS · 51% | Models & AI Runtimes · 27% |
|----------------|-----------------|--------------------------|
| **Discrete GPU**<br>Intel Arc Pro B70 · B65 · B60 · B50<br>NVIDIA Consumer: RTX 5090 · RTX 5080<br>RTX 4090 · RTX 3090<br>NVIDIA Workstation: RTX PRO 6000 · 5000 Blackwell<br>NVIDIA Data center: B200 · H200<br>AMD Radeon AI PRO R9700 · R9600<br><br>**SoC · 统一内存**<br>Intel Core Ultra Series 1 · Meteor Lake<br>Series 2 · Lunar Lake + Arrow Lake<br>Series 3 · Panther Lake<br>NVIDIA GB10 Grace Blackwell<br>AMD Ryzen AI Max+ 395 · Ryzen AI Max 390 · Ryzen AI Max 385<br>Apple M3 Ultra · M4 Pro · M4 Max · M5 Pro · M5 Max | **Accelerator resources · 左**<br>*hardware-facing abstraction*<br>01 **Backend enablement.** 为每类加速器启用 OpenVINO、CUDA 或 ROCm。<br>02 **Schedulable devices.** 通过厂商 device plugin 将设备暴露为 Kubernetes 资源。<br>03 **Unified resource contract.** 将 label、调度与注入收敛为一份应用资源契约。<br>04 **Continuous observability.** 通过 Prometheus 持续观测使用情况和设备健康。<br><br>**Application allocation · 右**<br>*software-facing abstraction*<br>01 **Mode-aware packages.** 为每种加速计算设备提供专属镜像与资源范围。<br>02 **Install & launch selection.** 用户可以在安装或启动时选择目标加速设备与资源，可以是单卡、多卡或多节点。<br>03 **Automatic resource management.** 系统尽最大努力保障应用运行，资源不足时自动扩缩容。<br>04 **User-friendly control.** 用户可以通过 UI 完成所有操作并及时获得反馈。 | **Models · 3×5**<br>Gemma 4 · Qwen3 · Ornith 1.0 · FLUX.2 · Wan 2.2 · Hunyuan3D 2.1 · Qwen3-ASR · ACE-Step 1.5 · BGE-M3 · Qwen3-TTS · Baidu OCR · Tencent Hy-MT2 · Z-Image · Ideogram 4 · MiniCPM-o 4.5<br><br>**AI runtimes · 3×3**<br>llama.cpp · vLLM · SGLang · Ollama · LocalAI · Xinference · KoboldCpp · Speaches · ComfyUI |

### 下半区 · 两个 Comments Box

| 加速计算资源 + Accelerator resources | Application allocation + Models & AI Runtimes |
|----------------------------------|-------------------------------------------|
| **统一生命周期，加速资源可自由组合。**<br><br>**01 · 管理加速资源生命周期。**<br>**一套接口。**Olares 把完整生命周期——从宿主驱动安装、设备发现，到运行时配置、调度、绑定、监控和故障剔除——收敛为统一接口。<br>**模块内接入。**新设备只需在自己的模块内实现生命周期接口，无需将设备专属改动散落到整个系统。<br><br>**02 · 组合加速资源。**<br>**任意拓扑。**单资源、多实例、多种异构资源、跨节点容量或外部 eGPU 均可组合。<br>**两层绑定。**开发者在软件中声明资源；用户通过系统选择并分配。<br>**应用与位置解耦。**应用契约从单设备扩展到多 GPU 或同架构资源池时保持稳定。 | **三种分配模式对开发者和应用透明，无需修改程序。**<br><br>**时间分片 · 50%。**名称来自应用轮流使用完整 GPU，适合每个模型都可能占据大部分显存的顺序工作流。专辑示例：LLM 写歌词 → ACE-Step 1.5 XL 生成音乐 → Z-Image 生成封面。如果没有 Olares，用户需要在每个阶段停止模型、释放并重新绑定 GPU，而且每首歌都要重复；时间分片自动轮转，让整个专辑像一条连续工作流。<br>Chips：`NVIDIA dGPU only`<br><br>**显存分片 · 右上。**名称来自把 VRAM 划分为固定配额，使多个应用并发运行。适合需要控制显存占用的常驻应用，如 ComfyUI、Speaches 或模型服务。<br>Chips：`Intel CPU` `Intel GPU` `NVIDIA dGPU` `GB10`<br><br>**独占 · 右下。**名称来自一个应用独占整块加速器，其他应用无法绑定。适合渲染和游戏。<br>Chips：`All modes` |

---

## 工作底稿

- 主体是上方连续架构 + 下方两个大 comments box，不为每个型号制作独立卡片。
- 整体左右约为 45.5 / 54.5：下方取消列间 gap，使右 comment box 起点与上方 `Application allocation` 对齐。
- 主副标题聚焦 Olares OS 的统一管理能力，不在标题区枚举芯片厂商或型号。
- 上半区为 324px；标题栏 36px，内容区 288px。增加量使用设计规范的 16px 间距尺度；左右外侧均按内容自适应排列，两侧分隔线不强制对齐。
- 间距遵循 [`ppt/design-system.md`](/Users/pengpeng/seo/ppt/design-system.md) 的 `4 / 8 / 12 / 16px` 尺度；标题与副标题使用规范允许的 6px。Models 保持 3×5，AI runtimes 使用 3×3。
- 上半区四段连续相邻，不使用圆形箭头连接。
- Olares OS 两列统一使用 `01 → 04` 自上而下，作为能力/组件清单；下方左 comment box 只讲开发者价值，两点为“加速资源的生命周期管理”和“加速资源的可组合性”，不重复上方任何组件名（OpenVINO/CUDA/plugin/Prometheus 等）。
- OpenVINO 与 CUDA、ROCm 放在最底层 driver/runtime enablement，不进入右侧应用 runtime 清单。
- Intel SoC 栏按 Core Ultra Series 1–3 展示平台时间线，不再列单独 SKU。
- 九个 AI runtimes 均有 Olares Market Manifest，但不共享同一兼容矩阵；KoboldCpp 的 chart 适用版本范围见 references。
- Accelerator resources 与 Application allocation 使用一个共享 Grid；四组内容按自然高度使用 `auto` 行，每项统一为“小标题 + 一句话”，左右分隔线共用基线。
- Application allocation 的四项为专属镜像与资源范围、安装或启动时选择单卡/多卡/多节点资源、自动资源管理，以及全 UI 操作与反馈。
- 下方两个绿色 comment kicker 删除，只保留黑色主标题。
- 下方右 comment box 采用 50/50：左半由时间分片独占并讲音乐专辑循环；右半上方为显存分片、下方为独占。
- 本页不展示 Agent & Software；完整架构留到下一页。
- 下方左 box 跨加速计算资源 + Accelerator resources，右 box 跨 Application allocation + Models & AI Runtimes。
- 叙述型正文使用 `11–11.5px`；型号、标签、chips 与次级参数保留 `10.5px`，所有对外文字均不低于规范底线。
- 图标统一取自 [`ppt/assets/slide21-icons/`](/Users/pengpeng/seo/ppt/assets/slide21-icons)，来源与商标说明见其中的 `manifest.json`。
- 视觉上只强调 Olares 中层；software / models 与 hardware 使用低饱和中性色，避免参考图式的大色块和虚线边框。
- 不展示底层调度项目名，也不加入国产 GPU / NPU 厂商。
- `Today / Next` 必须保留，不能把跨 AMD64 / ARM64 的全自动异构集群写成当前能力。
- 设备列表按厂商聚合，只显示芯片 / accelerator SKU 名，不显示容量或整机名；表达市场资源覆盖方向，不表示各 compute modes 的 host 管理成熟度相同。
- 芯片、模型、runtime 与分配模式来源见 [`research/local-open-models-and-runtimes-2026.md`](/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.md)。
- `1×1 → 1×N → N×N` 表达加速设备拓扑扩展；当前跨节点成熟能力以同架构集群和 NVIDIA 路径为主，跨 AMD64 / ARM64 自动化仍属 Next。
- HAMi 提供受支持设备的注册、共享和调度路径；Olares 负责 host integration、统一资源契约、应用镜像选择和生命周期管理。
- 主画面 chips：时间分片为 `NVIDIA dGPU only`；显存分片收敛展示 `Intel CPU`、`Intel GPU`、`NVIDIA dGPU`、`GB10`；独占为 `All modes`。完整代码支持矩阵见 references。
- 切换分配模式会停止该设备上的绑定应用并清空 allocation，之后需要恢复和重新绑定。
- 当前代码支持安装时自动选择以及启动/恢复前的绑定和重新分配；主画面的自动扩缩容按产品愿景口径展示，不作为当前代码级实现声明。
- eGPU 作为支持的设备形态；主画面写健康感知的设备重注册，运行时物理热插拔取决于厂商驱动、device plugin 与运行中 workload 的设备生命周期。
- 模型厂商的示例不使用未经核实的具体型号；统一写“高精度原始权重”。
- 不在面向 Intel 的主画面比较 NVIDIA / Apple 生态成熟度；强调 Intel 负责硬件效率，Olares 负责产品化与调度。
- 完整实现状态、代码依据与安全口径见 [references.md](./references.md)。
