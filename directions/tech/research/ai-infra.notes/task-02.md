---
task_id: 02
role: GPU 调度与训练/微调栈分析师
status: complete
sources_found: 9
---

## Sources
[1] Project-HAMi/HAMi (GitHub) | https://github.com/Project-HAMi/HAMi/ | Source-Type: official | As Of: 2026 | Authority: 8/10
[2] Heterogeneous GPU Sharing on Kubernetes (HAMi 官网) | https://project-hami.io/ | Source-Type: official | As Of: 2026 | Authority: 8/10
[3] GPU Virtualization Principles (HAMi docs) | https://project-hami.io/docs/core-concepts/gpu-virtualization | Source-Type: official | As Of: 2026 | Authority: 8/10
[4] How to use Kueue on HAMi (HAMi docs) | https://project-hami.io/docs/userguide/kueue/how-to-use-kueue | Source-Type: official | As Of: 2026 | Authority: 7/10
[5] Fine-tuning Tools Comparison (Clore.ai) | https://docs.clore.ai/guides/comparisons/finetuning-comparison | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[6] Unsloth vs Axolotl vs LLaMA-Factory (Paolo Perrone, Substack) | https://theaiengineer.substack.com/p/unsloth-vs-axolotl-vs-llama-factory | Source-Type: journalism | As Of: 2026 | Authority: 5/10
[7] EVAL #003: Fine-Tuning in 2026 (dev.to, ultraduneai) | https://dev.to/ultraduneai/eval-003-fine-tuning-in-2026-axolotl-vs-unsloth-vs-trl-vs-llama-factory-2ohg | Source-Type: community | As Of: 2026-03 | Authority: 5/10
[8] LLaMA-Factory vs Unsloth (aicoolies) | https://aicoolies.com/comparisons/llama-factory-vs-unsloth | Source-Type: secondary-industry | As Of: 2026 | Authority: 4/10
[9] hiyouga/LLaMA-Factory (GitHub) | https://github.com/hiyouga/LLaMa-Factory | Source-Type: official | As Of: 2026 | Authority: 8/10

## Findings
- HAMi（Heterogeneous AI Computing Virtualization Middleware，前身 k8s-vGPU-scheduler）是 CNCF Sandbox 项目，为 K8s 提供异构加速器的显存/算力切片、隔离与设备感知调度，无需改应用代码。[1][2]
- HAMi 通过 `nvidia.com/gpumem`(显存 MiB) 与 `nvidia.com/gpucores`(算力 %) 做细粒度声明，用 libvgpu.so 在 CUDA API 层拦截实现容器内硬隔离（超配直接 OOM）。[1][3]
- K8s 默认 GPU 调度是独占式（`nvidia.com/gpu:1`＝整卡），无显存配额概念；典型推理只用 20%~40% 算力，故需共享方案。[3]
- 三种 GPU 共享路线：①NVIDIA Time-Slicing（并发调度但无显存隔离，一个 Pod OOM 会拖垮整卡）②MIG 硬件分区（真隔离但仅 A100/H100 等数据中心卡支持）③HAMi 软件层 CUDA 拦截（无需改驱动/应用，支持动态 MIG）。[3]
- HAMi 支持 NVIDIA/Huawei Ascend/Cambricon/Hygon/Iluvatar/MetaX/Moore Threads/AWS Neuron 等多厂商加速器，可与 kube-scheduler、Volcano、Kueue、Koordinator 协同。[1][2]
- Kueue（K8s 官方批调度/配额）可通过 ResourceTransformation 把 HAMi 的 per-vGPU 请求聚合成 `nvidia.com/total-gpucores`/`total-gpumem` 做集群级配额与公平共享。[4]
- 微调框架三强互补而非竞争：LLaMA-Factory（71,857 stars，Apache-2.0）是 GUI 优先的统一训练枢纽，支持 100+ 模型与 SFT/PPO/DPO/继续预训练。[9][7]
- Unsloth（~54K stars，2026-02 破 50K）是速度/显存引擎：自研 Triton kernel，2–5× 更快训练、VRAM 降 70–80%，2026-02 加 MoE 训练（宣称 12× 更快）、embedding 微调、FP8；许可 LGPL（非商用免费）。[5][7][8]
- Axolotl（~11K stars，Apache-2.0）配置驱动、YAML 优先，靠 FSDP/DeepSpeed 原生集成做多 GPU/多节点，适合可复现的生产/RLHF 对齐。[5][6][7]
- 三者可组合：LLaMA-Factory 用 Unsloth 作后端（`use_unsloth:true`），训练时间仅比原生 Unsloth 慢 ~6%，同时保留 UI 与模型管理。[6][9]
- TRL（HuggingFace，~17.6K stars，Apache-2.0）是 RLHF/DPO/GRPO 的原生对齐研究框架；PEFT 是 HF 的参数高效微调底层库（LoRA/QLoRA/DoRA 均依赖）。[5][7]
- Unsloth Studio / LLaMA-Factory 均可导出 GGUF 供 Ollama/vLLM 部署，训练与推理栈同源。[8][9]

## Deep Read Notes
### Source [3]: HAMi GPU Virtualization Principles
Key data: Time-Slicing 无显存隔离；MIG 仅 A100/H100；HAMi 用 Scheduler-Extender 读 Node Annotation 做 Filter/Bind，libvgpu.so 拦截 CUDA；binpack/spread 两策略。
Key insight: 清楚说明为何"消费级单卡/多卡共享"必须软件层拦截——MIG 在消费卡上不可用，这正是个人云场景的关键。
Useful for: GPU 共享子类 + Olares HAMi/GPUBinding/nvshare 内置论证。

### Source [9]: hiyouga/LLaMA-Factory GitHub
Key data: 71,857 stars / 270 contributors / 最新 v0.9.5(2026-05-30)；集成 FlashAttention-2、Unsloth、Liger Kernel、KTransformers；对接 HF/ModelScope/vLLM/SGLang。
Key insight: 定位"统一编排层"而非单一优化器，是把 Unsloth 速度 + 广模型覆盖粘合的枢纽。
Useful for: 微调子类 top1 论证。

## Gaps
- nvshare 与 KubeRay/Ray、Volcano 未找到独立高权威来源逐一佐证（HAMi 文档提及可协同）；报告中对 Ray/nvshare 采保守表述或标注证据较弱。
- 公有云微调对标（HF AutoTrain、Bedrock/SageMaker/Vertex fine-tuning、Together/Fireworks fine-tune）本任务未专门取源，报告引用需跨 task-01 的 [11][12] 或标定性表述。
- 相反主张候选：Unsloth 主打单 GPU，多 GPU/多节点扩展弱于 Axolotl；且 Unsloth 核心许可 LGPL（非商用免费），商用需注意——削弱"Unsloth 通吃"叙事。[5][6]

## END
