---
task_id: 03
role: 本地 LLM 推理可行性分析师
status: complete
sources_found: 10
---

## Sources
[1] Which GPU Runs Which LLM? A 2026 VRAM-to-Model Map | https://specpicks.com/reviews/which-gpu-runs-which-llm-vram-map-2026 | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[2] Best GPU for Llama 3.1 70B (2026) | https://specpicks.com/reviews/best-gpu-for-llama-3-1-70b | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[3] VRAM for 70B Models: Why 16GB GPU Is the Minimum in 2026 | https://www.sitepoint.com/vram-requirements-70b-models-16gb-gpu-minimum-2026/ | Source-Type: journalism | As Of: 2026-02 | Authority: 6/10
[4] Llama 3.1 70B INT4 VRAM Requirements: Why 16 GB Isn't Enough | https://gigagpu.com/llama-3-70b-int4-vram-requirements/ | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 6/10
[5] RTX 5090 vs RTX 4090 for Local LLMs: Real Inference Benchmarks | https://craftrigs.com/benchmarks/rtx-5090-vs-4090-local-llm-inference-benchmark/ | Source-Type: secondary-industry | As Of: 2026-04 | Authority: 7/10
[6] NVIDIA RTX PRO 6000 Workstation GPU Review: Blackwell + 96 GB | https://www.storagereview.com/review/nvidia-rtx-pro-6000-workstation-gpu-review-blackwell-architecture-and-96-gb-for-pro-workflows | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 9/10
[7] AMD Ryzen AI Max+ 395 vs Mac Studio M4 Max | https://specpicks.com/reviews/ryzen-ai-max-395-vs-mac-studio-m4-max-local-llm-2026 | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[8] How to run Llama 3.1 70B on Apple M4 Max (2026) | https://specpicks.com/reviews/run-llama-3-1-70b-on-m4-max | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[9] How to run Qwen 3 32B on NVIDIA GeForce RTX 4090 | https://specpicks.com/reviews/run-qwen-3-32b-on-rtx-4090 | Source-Type: secondary-industry | As Of: 2026-05 | Authority: 7/10
[10] DGX Spark vs M5 Max vs RTX 6000: Local AI Showdown | https://www.digitalapplied.com/blog/dgx-spark-vs-m5-max-vs-rtx-6000-blackwell-local-ai-2026 | Source-Type: secondary-industry | As Of: 2026-06 | Authority: 6/10

## Findings

### VRAM 需求（量化 × 规模）
- **32B Q4_K_M**：权重 ~19 GB；+4K KV ~1.5 GB → **合计 ~21 GB**；24 GB 单卡可全 GPU 加载。[1]
- **32B Q8_0**：权重 ~34 GB（Qwen3-32B ~35.2 GB）；**24 GB 单卡装不下**，需 48 GB 或双卡。[1][9]
- **32B Q5_K_M**：~22–25 GB；24 GB 卡边界（Qwen3-32B Q5 合计 ~25 GB = OOM）。[9]
- **70B Q4_K_M**：权重 ~40–43.7 GB；+8K KV/开销 → **~42.4–46 GB**；**单卡 <48 GB 无法全显存**。[2][3][4]
- **70B Q8_0**：权重 ~74–76 GB；+8K KV → **~77 GB**；需 80 GB+ 或统一内存 ≥96 GB。[2]
- **70B AWQ 4-bit + 8K ctx ×4 并发**：~35 GB 权重 + ~10.4 GB KV + ~1.5 GB 激活 → **~47 GB**；48 GB 为实务下限。[4]

### 单卡 tok/s（llama.cpp / LM Studio，batch=1，Q4_K_M 除非注明）
| 硬件 | 32B Q4 | 70B Q4 | 备注 |
|------|--------|--------|------|
| RTX 4090 24GB | ~35–45 tok/s [5][9] | 27.8 tok/s（需 offload）[5] | 带宽 1008 GB/s |
| RTX 5090 **32GB 桌面** | ~55–61 tok/s [5] | **38.2 tok/s**（全 VRAM，2 GB 余量）[5] | 带宽 1792 GB/s |
| RTX 5090 24GB + 96GB RAM offload | ~35–55 tok/s（估） | **~8–15 tok/s**（~40–45 层在 GPU）[3] | Olares One 档 |
| 2× RTX 4090 48GB | — | 44–50 tok/s [5] | 张量并行 |
| RTX PRO 6000 96GB | 226 tok/s（8B 档）[6] | **~31.8 tok/s**（70B）[6] | 120B → 163 tok/s [6] |
| Mac Studio M4 Max 128GB | Qwen3-32B **22.5 tok/s** [7] | 70B **12.1 tok/s**（Q4）[7] | 带宽 546 GB/s |
| Strix Halo 128GB | Qwen3-32B **14.3 tok/s** [7] | 70B **7.8 tok/s**（Q4）[7] | 带宽 ~256 GB/s |

- **70B 全 CPU / 重度 offload**：1–5 tok/s；5090 70B spill 到 RAM → **1–2 tok/s**。[3]

### Olares One 对位判断（RTX 5090 Mobile 24GB / 96GB DDR5 / Core Ultra 9 275HX / $3,999）
**定位：32B-class 满血本地推理盒；70B 为「可跑但非舒适区」。**
1. **32B Q4（主力）**：24 GB 与 4090 同档，Blackwell + 更高带宽（移动 175W TGP 会低于桌面）。预期 **~35–55 tok/s**，**显著快于** M4 Max（22.5 tok/s）与 Strix Halo（14.3 tok/s）。[7][9]
2. **32B Q8**：需 ~34–35 GB → **单卡不可**；除非部分层 offload 到 96 GB DDR5。
3. **70B Q4**：权重+8K KV ~42 GB → **无法全进 24 GB VRAM**；依赖 **GPU 层 + 96 GB 系统 RAM hybrid**，partial offload **8–15 tok/s**。[3] 与 M4 Max 70B（12 tok/s 全内存）相近或略慢，但 32B 任务 Olares 明显更快。
4. **vs RTX PRO 6000 96GB（~$8.5k–14k）**：PRO 可 70B 全 VRAM ~32 tok/s、120B 163 tok/s [6]；Olares 不具备 70B+ 原生能力，胜在 **$3,999 一体机 + 私有云 OS**。
5. **vs 统一内存路线（Mac Studio / Strix / GB10）**：统一内存 **容量换带宽**——能装 70B 但 decode 受 256–546 GB/s 限制 [7][10]；Olares 24 GB 高速 GDDR7 对 **≤32B 更优**，70B 则不如 ≥96 GB 统一内存一次装下。
6. **vs 双 24GB 消费卡（48 GB）**：双 4090 70B Q4 **44–50 tok/s** [5]，高于 Olares offload 档；Olares 胜在单机体积/功耗/7×24 私有云叙事。

**一句话对位**：Olares One = **「24 GB 独显的 32B 本地 Agent 甜点位」**；要 **70B Q4 全 GPU ≥30 tok/s** 需 48 GB+（双卡或 PRO 6000）；要 **70B 免 offload 可接受 8–15 tok/s** 则 M4 Max 128GB / Strix 128GB 更对口。

## Deep Read Notes
### Source [5]: RTX 5090 vs RTX 4090 (CraftRigs)
Key data: 5090 32GB → 70B-Q4_K_M **38.2 tok/s**；4090 **27.8 tok/s**（offload）；双 4090 **44–50 tok/s**；32B 5090 约比 4090 快 35%。
Key insight: 带宽理论 +77%，实测 decode 仅 +37%；70B 是 5090 相对 4090 的主要溢价场景。
Useful for: 消费旗舰 tok/s 基准；Olares One 用 24GB 移动版时需下调桌面 5090 数字并启用 offload。

### Source [4]: Llama 3.1 70B INT4 VRAM (GIGAGPU)
Key data: AWQ ~35 GB / GGUF Q4_K_M ~40.5 GB；8K×4 序列 KV ~10.4 GB → 总计 **~47 GB**；5090 32GB：权重可装、KV 不够。
Key insight: 48 GB 是 AWQ+vLLM 生产下限；5090 32GB 仍非可靠 70B 单卡解。
Useful for: VRAM 分解表；Olares 24GB 更不可能全 GPU 70B。

### Source [6]: RTX PRO 6000 Review (StorageReview)
Key data: LM Studio：70B ~31.8 tok/s；GPT-OSS 120B 163.15 tok/s；5090 无法加载 120B。
Key insight: 96 GB 独显是当前工作站单卡跑 70B–120B 的最权威实测之一。
Useful for: Olares One vs PRO 6000 / 企业 NAS+工作站对位。

## Gaps
- **5090 32GB 能否单卡跑 70B Q4_K_M**：CraftRigs 称可（38.2 tok/s）[5]；GIGAGPU 称 AWQ 权重可装但 8K KV 不够 [4]；SpecPicks 称需 ≥48 GB pooled VRAM [2]。Olares 24GB 移动版应保守按 **不可全 GPU** 处理。
- **5090 Mobile 24GB 实测 tok/s 缺失**：公开基准几乎全是桌面 5090 32GB/4090；Olares One 175W TGP 数字需自测（预期介于 4090 与桌面 5090 之间）。
- **统一内存「能装」vs「够快」相反主张**：部分源称 M4 Max 70B 20–28 tok/s 优于 4090 offload [7][10]；另有源称 Strix Halo 稠密 70B 仅 3–5 tok/s——同平台差 2–3×，量化/栈/上下文未统一。
- **统一内存带宽低于独显 VRAM**：M4 Max 546 GB/s vs RTX 4090 **1008 GB/s** [7]——容量路线能跑 70B 但 32B 以下 Olares 类独显仍显著更快。
- **RTX PRO 6000 vs 双 5090 性价比**：小模型 5090 更快/更便宜，>32 GB 模型 PRO 6000 唯一 [10]；同 workload PRO 仅 1.14–1.65× 快但 6× 价 [4]——企业 vs 消费 TCO 口径不一。

## END
