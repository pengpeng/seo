# Registry — Olares × Intel 协处理器 PPT（slide 25-28）价格/规格/市场溯源

> 用途：为 `ppt/` Intel 合作三形态幻灯（外挂 eGPU / SoC Panther Lake / 内置）提供可溯源数字。仿 slide-24 的 [registry](/Users/pengpeng/seo/research/scenario-pricing-2026-07.notes/registry.md) 体例。
> **AS_OF = 2026-07-14**。事实型数字（TOPS/价格/tok/s/出货量）变动快，发布前以官网/一手为准。
> 底稿：同目录 `task-a1-arc-pro-llm.md`、`task-a2-egpu-tb4-cpu.md`、`task-a3-panther-lake-meeting.md`（每条含编号来源与日期）。`[u]` = 未独立证实 / 单源。
> 竞品实测机数字来自第一方 [olares-one-benchmarks.md](/Users/pengpeng/seo/directions/hardware/research/olares-one-benchmarks.md)。

---

## 1. GPU 硬件锚点（Intel Arc Pro，主 B70 / 辅 B60）

| 卡 | 显存 | 带宽 | INT8 TOPS | 接口 | 功耗 | 价格 | $/GB | 来源 |
|----|------|------|-----------|------|------|------|------|------|
| **Arc Pro B70**（主） | **32GB GDDR6** | 608 GB/s | 367（dense） | PCIe 5.0 x16 | 230W（伙伴 160–290W） | **$949** | ~$30 | a1 [1][2][4] |
| Arc Pro B65 | 32GB | 608 GB/s | 197 | PCIe 5.0 x16 | — | 未定（4 月中） | — | a1 [1][4] |
| **Arc Pro B60**（辅） | 24GB | 456 GB/s | 197 | PCIe 5.0 x16(x8 电气) | 120–200W | ~**$599** | ~$25 | a1 [23][22] |
| Arc Pro B60 Dual | 48GB(2×24) | — | — | 需 x8+x8 拆分 | ~300W | ~**$1,000–1,200** | ~$25 | a1 [24] |
| 对比 NVIDIA RTX Pro 4000 | 24GB | — | — | — | — | ~$1,800 | ~$75 | a1 [9] |
| 对比 NVIDIA RTX 6000 Ada | 48GB | — | — | — | — | ~$5,000–6,000 | ~$104–125 | a1 [24] |

- B70 = 大 Battlemage 芯 **BMG-G31**，2026-03-25 发布，**与 Panther Lake（Core Ultra Series 3）同场发布**——这是把三张幻灯串成"一次 Intel 发布"的关键叙事。a1 [4][6]
- 消费级游戏卡 **Arc B770 已取消**（内存涨价+财务不划算），同一颗 BMG-G31 转做 Pro B70。（前轮 web 检索，tweaktown/wccftech/xda）
- **$/GB 是 Arc 的硬卖点**：B70/B60 每 GB 显存约 NVIDIA 同级的 1/3–1/5。a1 [22][24][9]

## 2. Arc 本地 LLM 实测口径（诚实版）

目标模型（2026-04 发布，web 已确认）：
- **Qwen3.6-35B-A3B** — 稀疏 MoE，35B 总 / **~3B 激活**（256 experts，8+1）；主打高吞吐、agentic coding，质量对标 dense 27B。
- **Qwen3.6-27B** — dense，全 27B 激活；"旗舰级编码"，更稳、推理更一致。→ **27B dense 质量更好；35B-A3B 速度更快**，与用户判断一致。

单卡 B70 实测（llama.cpp / SYCL / Q4，社区实测，中置信）：

| 模型 | tok/s（单流） | 备注 | 来源 |
|------|--------------|------|------|
| Qwen3.6-35B-A3B (MoE) | **~55（PMZFX 54.7@114W）～82（llama.cpp issue）** | 调优/量化不同差异大；prefill 615 t/s | web(PMZFX/CraftRigs)、a1 [21] |
| Qwen3.5-27B (dense) | **~15–25**（Q6/Q8 ~15；Q4_K_S 25，MTP 36.8） | dense 慢但质量高 | web(PMZFX)、a1 [21] |
| 4× B60 + vLLM/LLM-Scaler，Qwen3-VL-30B-A3B | **~1,000 tok/s 聚合 @64 并发**（唯一独立实测） | 线性扩展、对外 API 场景 | a1 [10] |

### 2b. Qwen3.6-35B-A3B 跨机对比 + 整机价（eGPU 幻灯核心对比）

> **口径（重要）**：下表主速度列 = **单流 · Q4 级 · 短/空上下文 · 全部不含 MTP（no speculative decoding）**。
> 为什么取 non-MTP：**B70 单卡跑这颗 35B-A3B MoE 的最优配置就是"不开 MTP"**——单卡 MoE 开 MTP 当前是负优化（no-MTP 72–82 → MTP 47–63，因 MUL_MAT_ID 专家派发开销；见"MTP 现状"）。竞品 AMD/Mac 这颗 MoE 开 MTP 是增益。所以"全部 non-MTP"既是同设定、也是 B70 的最优实际配置；发布时必须**明确标注不含 MTP**，并注"Intel 单卡 MoE 的 MTP 正在完善（双卡已增益），以后会转正"。
> 条件仍不完全一致（量化 Q4/IQ4/Q6、引擎 MLX/Vulkan/ROCm/SYCL、build 各异），故给**区间**。

> **量化口径（重要，2026-07 归一）**：下表**全部 Q4 级**（Q4_K_M / UD-Q4 / Q4_0 / 4bit-MLX / IQ4），单流·短上下文·不含 MTP。旧版曾拿 B70 的 Q4 去比 AMD 的 Q6_K_XL、Mac 的 8bit，**低估了 AMD/Mac**；归一到 Q4 后 AMD、M3 Ultra 的 decode 都追上/反超，B70 **不再"领先"、而是同档**。

| 方案 | 显存/内存 | 整机价 | **prefill pp t/s**（Q4·不含MTP·短提示） | **decode tg t/s**（Q4·不含MTP） | 开 MTP 后 decode（参考） | 数据来源（含条件 + 日期） |
|------|-----------|--------|--------------------------------------|------------------------------|-------------------------|--------------------------|
| **Intel 主机 + OCuLink + Arc Pro B70** | **32GB 独显 GDDR6** | **~$1,550–1,750**（卡 $949→~$999 街价；+$1,050 加卡；GDDR6 涨价小） | **~615**（Q4_K_M pp512，llama.cpp SYCL；长上下文稳，64K 仍 411；**XMX 后 2.4–15×，见下节**） | **~55–82**（UD-Q4_K_M 54.7 早 → 近期 F16 SYCL **72–82**） | 单卡 MoE **负优化**（82→47–63）；27B dense +37–47%；双卡 MoE +19%/+78%/+143% | PMZFX Q4_K_M pp615 / tg 54.7@114W；Sergio Q4_K_XL 68.45；#23533/#23149 no-MTP **72–82**（F16 SYCL） |
| AMD 395+ 迷你机（GTR9 Pro / Framework / GMKtec） | 128GB 统一 LPDDR5X | **$2,000（GMKtec 直营，挂"即将涨价"）→ 多数渠道 $3,150–4,350**（GTR9 Pro $4,349、Framework 主板 $3,149、Minisforum $3,639；早 2026 ~$2,099） | **~900–1,270**（Q4_K_M；短提示快；**长上下文 prefill 时间暴涨**，iGPU compute-bound，32K 达分钟级） | **~62–81**（UD-Q4 62.56 / Q4_K_M **76.94** / Q4_0 **81.30** speed-first；早期 build ~46） | 55–90（unsloth/ROCmFP4）；~105 best-case | 价:task-a（GMKtec/Beelink/Framework/Minisforum 官方，2026-07-14）；速:strix-halo-guide Q4_K_M **76.94** / Q4_0 **81.30**；BAEM1N Q4 45.4–46.2；zenn pp ~1,010–1,084 |
| Mac Studio M4 Max | 64–128GB 统一 | **≥64GB 最低 $3,499**（原 ~$2,699；Apple 2026-06 涨价；128GB/1TB $3,699、/4TB $4,699） | **~1,100–1,370**（4bit MLX：1K 1,099 / 4K 1,368 / 8K 1,357 / 32K 1,098 / 64K 838） | **~42–70**（LLMCheck Q4_K_M 42 / 社区 55–70；oMLX 4bit 峰 92–104） | ~81.5（programmer-666 MTP） | 价:task-b（AppleInsider/MacRumors/Verge，2026-07-14）；速:oMLX/LLMCheck/willitrunai/batiai |
| Mac Studio M3 Ultra | 96GB 统一（256GB 已停售） | **96GB $5,299**（原 ~$3,999；Apple 2026-06 涨价 +$1,300；256GB 已停） | **~1,640–2,620**（4bit MLX：1K 1,638 / 8K 2,617 / 32K 2,105 / 128K 968） | **~70–98**（Q4_K_M 70.8 / 4bit oMLX 98.6@1k → 51.5@64k） | — | 价:task-b（2026-07-14）；速:oMLX M3 Ultra 80c 4bit 全曲线；willitrunai Q4_K_M **70.8** |

**MTP 现状（决定了上面的对比口径，务必读）**：
- Qwen3.6 的 MTP（多 token 预测/自推测解码）已并入 llama.cpp（unsloth 官方 GGUF，`--spec-type draft-mtp --spec-draft-n-max 2`）。
- **27B dense**：全平台增益（B70 25→37，+47%）。
- **35B-A3B MoE 单卡 B70**：**当前负优化**——no-MTP 72–82，开 MTP 掉到 47–63（`MUL_MAT_ID` 专家派发开销大）；早期还有 GDN K>1 bug 导致输出乱码，已修复（输出正确但仍慢于 no-MTP）。llama.cpp #23149/#23155/#23533/PR#23142。
- **双卡 B70 MoE**：MTP 已转正（+19%@4k、+78%@32k、+143%@61k，grukx）。
- 结论：单卡跑这颗 MoE，**B70 最优＝不开 MTP**；因此本表"全部 non-MTP"对 B70 是最优且公平的同设定。Intel 单卡 MoE MTP 的优化在推进中（"以后也会有可用的 MoE MTP"）。

**价格拆解（带源，2026-07-14 现价 — 已计入 2026 内存涨价）**：
- B70 方案 = Intel mini-PC（Core Ultra 5 125H，Minisforum M1 Pro-125H ~$500–600）+ OCuLink 坞（~$99）+ Arc Pro B70 **街价 ~$999**（MSRP $949，Newegg/Micro Center 有货）≈ **$1,550–1,750**；已有主机则 +$1,050。**GDDR6 涨价小，整机价基本没动。**
- **AMD 395+ 128GB**：GMKtec EVO-X2 直营 **$1,999**（挂"即将涨价"）；GTR9 Pro **$4,349**、Framework 主板 **$3,149**、Minisforum MS-S1 Max **$3,639**、Micro Center dev **$3,999**——**多数渠道已 $3,150–4,350**。
- **Mac Studio**：Apple **2026-06-25/26 全线涨价**（归因内存短缺）——M4 Max ≥64GB 最低 **$3,499**（原 $2,699）、M3 Ultra 96GB **$5,299**（原 $3,999，+$1,300）、M3 Ultra 256GB **已停售**。
- **$/GB 显存**：B70 ~$30、B60 ~$25、RTX Pro 4000 ~$75、RTX 6000 Ada ~$104–125（a1[9][24]）。

**内存涨价对价格的影响（2026-07，见 [local-ai-hardware-prices-2026-07](../local-ai-hardware-prices-2026-07.md)）**：
- 2026 DRAM 历史级涨价（常规 1Q26 +93–98% QoQ；LPDDR5X +78–89%），**非对称**打击统一内存/大 RAM 机型（Mac、Strix Halo 128GB LPDDR5X），而独显 + GDDR6 的 B70 受创小（GDDR6 现货 +61%、无合约暴涨，且显卡厂多有预签合约）。
- 结论：**这轮涨价拉大了 B70 的价格优势**——B70 整机 ~$1,600 基本没动，Mac 涨到 $3,499/$5,299、多数 395+ 机型 $3,150+。
- 诚实边界：AMD 仍有 GMKtec $1,999 一个直营买法（但预警涨价）；2H26 涨势或放缓（TrendForce 3Q26 +13–18%），发布前须复核价格。

**结论（Q4 归一后，decode 与 prefill 都要看，别再吹"最快"）**：
- **decode（出字，Q4·不含 MTP）**：**四家同档，~50–90**（B70 55–82、AMD 62–81、M4 Max 42–70、M3 Ultra 70–98）。**波动主要来自 build/engine（llama.cpp vs MLX、量化子档、warm/cold），而非硬件代差**。B70 中游偏上、不落下风，但**不是速度冠军**——旧版"B70 领先"是拿 B70 的 Q4 比了 AMD 的 Q6、Mac 的 8bit，归一 Q4 后这个"领先"消失。
- **prefill（读输入，Q4·短提示）**：**Mac 最强**（M3 Ultra 到 ~2,600、M4 Max ~1,100–1,370），AMD 次（~900–1,270），**B70 最低（~615，llama.cpp 标量注意力，非硬件封顶）**。
- **长上下文 prefill 稳定性**：B70 / Mac 稳，**AMD 差**（iGPU compute-bound，32K→分钟级、128K 达十几分钟）。
- **所以 B70 站得住的、真正稳的优势 = 整机最便宜（~$1,500–1,700 vs $2,100–4,500）+ 每 GB 显存约 NVIDIA 的 1/3 + 加卡不换机 + 长上下文稳 + prefill 软件红利（XMX 已在 upstream 落地）**；**raw 速度只是"同档不落下风"，不作为主卖点**。
- **取舍 / 诚实边界**：AMD/Mac 的 128GB/统一内存能装更大模型（100B+）与更长上下文，B70 32GB 装不下；开 MTP 后 AMD/Mac 这颗 MoE decode 会上探（~90–105 / 81），B70 单卡 MoE 的 MTP 仍待优化（双卡已增益）；满上下文 AMD decode 掉到 16–37、B70 短提示 prefill 靠 XMX 软件补。

**B70 prefill 还有多少提升空间？（重要——回答"615 是不是到头了"）**
- **615 不是硬件天花板，是 llama.cpp SYCL 内核成熟度问题**。基准作者原话："The 7–16× prefill gap is **entirely due to XMX/DPAS flash attention + varlen batching in vLLM vs scalar FP16 attention + ubatch slicing in llama.cpp**. It's **not an Intel hardware limit or a driver issue** — it's kernel maturity on the llama.cpp SYCL side."（engine-comparison.md）
- **Intel 自家 vLLM XPU 已用 XMX → prefill 快 2.4–15×**（随上下文越长差距越大）：pp128 2,579→6,289（2.4×）、pp512 4,567→20,555（4.5×）、pp2048 4,426→67,851（**15.3×**）。decode 则 ~打平（都受带宽限）。（engine-comparison.md，B70）
- **llama.cpp 正在补 XMX flash-attention（2026 在合）**：
  - PR #25222（oneDNN 图 SDPA，XMX 融合注意力，F16 KV）：B70 上 Qwen3.6-27B prefill @512 **+21%**、@80k **+326%（×4.26）**；build flag `GGML_SYCL_DNN=ON` + 运行时 `GGML_SYCL_FA_ONEDNN=1`。
  - PR #25312（扩到量化 KV：Q4_0/Q5/Q8_0/BF16）：prefill **2.40–2.48×**（32K 上 TILE 335 → ONEDNN 805 / HYBRID 824）。正好治 issue #21862 里"fa=1 长上下文 prefill 塌"（32K 掉到 227）。
  - F16 累加（`-DGGML_SYCL_F16=ON`）：dense **+139–176%**（2.4–2.8×）prefill；但**这颗 35B-A3B MoE 基本没动（+2%）**——MoE prefill 瓶颈在专家派发/注意力，靠上面的 XMX FA 才抬得动。
- **LLM-Scaler**（Intel 优化版 vLLM）在 B60 上再 +25% per-token。（embeddedllm）
- **诚实 caveat（写进对外稿也要留）**：① 那 15× 是在**受支持模型**上测的；**vLLM XPU 今天还不支持 Qwen3.5/3.6**（GDN 注意力需 Triton/CUDA 内核，XPU 暂缺），所以这颗 MoE 的近期干净提速路径是 llama.cpp 的 XMX FA PR 落地（与模型无关），而非"今天就上 vLLM"。② 结论：**B70 prefill 的短板是软件在追、非硬件封顶，且方向明确（XMX FA 已在 upstream 落地）**——对 Intel 是"投软件栈即可兑现"的确定性红利。
- URL：engine-comparison https://github.com/PMZFX/intel-arc-pro-b70-benchmarks/blob/master/engine-comparison.md ；F16 accum https://github.com/PMZFX/intel-arc-pro-b70-benchmarks/blob/master/llm-benchmarks.md ；PR #25222 https://github.com/ggml-org/llama.cpp/pull/25222 ；PR #25312 https://github.com/ggml-org/llama.cpp/pull/25312 ；issue #21862 https://github.com/ggml-org/llama.cpp/issues/21862 ；B60 LLM-Scaler https://embeddedllm.com/blog/benchmarking-llm-inference-intel-arc-pro-b60

**§2b 逐条来源 URL（可点开核对）**

- B70 · PMZFX 基准仓库（Qwen3.6-35B-A3B UD-Q4_K_M **54.7 t/s** / 615 pp / 114W，单卡；32K 上下文仍 54.5）：https://github.com/PMZFX/intel-arc-pro-b70-benchmarks （FINDINGS：https://github.com/PMZFX/intel-arc-pro-b70-benchmarks/blob/master/FINDINGS.md ）
- B70 · CraftRigs（复述 PMZFX 54.7 t/s + 能效 0.48 tok/s/W）：https://craftrigs.com/news/arc-pro-b70-killer-app-qwen-3-6-35b-a3b-54-tok-s/
- B70 · Sergio B.（Q4_K_XL SYCL：llama-bench **68.45**，API ~60–66）：https://sergiiob.dev/posts/intel-arc-pro-b70-sycl-llama-cpp-qwen35/
- B70 · AI Weekly（SYCL 持续 **62–64 t/s**，需 seq_rm 补丁）：https://aiweekly.co/alerts/intel-arc-pro-b70-delivers-63-ts-on-qwen-36-35b
- B70 · bittide（>60 t/s，262k 上下文，含复现步骤）：https://bittide.aicompass.dev/article/ab022215-bddf-48a1-8f96-6c391f8980a9
- B70 · llama.cpp issue #23533（35B-A3B **no-MTP 82.2**；MTP n=2 掉到 46.9–63.1；27B dense 25→36.8；双卡 MoE MTP 转正）：https://github.com/ggml-org/llama.cpp/issues/23533
- B70 · llama.cpp issue #23149（MTP support in SYCL；no-MTP **72.9**，GDN 修复后 MTP 52.1 仍 < no-MTP）：https://github.com/ggml-org/llama.cpp/issues/23149
- B70 · llama.cpp issue #23155（SYCL MTP 乱码 = GDN K>1 缺失，已修）：https://github.com/ggml-org/llama.cpp/issues/23155
- B70 · llama.cpp PR #23142（SYCL MoE prefill +70%；MTP 52→58）：https://github.com/ggml-org/llama.cpp/pull/23142
- MTP 用法 · Unsloth Qwen3.6 文档（`--spec-type draft-mtp`，27B/35B-A3B MTP GGUF）：https://unsloth.ai/docs/models/qwen3.6
- AMD 395+ · unsloth HF discussions#8（GTR9 Pro **Q6_K_XL**〔非 Q4，偏慢〕非 MTP **49.99**、MTP 55–62）：https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF/discussions/8
- AMD 395+ · strix-halo-guide **Q4 归一**（**Q4_K_M 76.94 / Q4_0 81.30 speed-first / UD-Q4 62.56**，b9049 Vulkan/RADV；Ollama Q4_K_M 71.82 warm）：https://github.com/hogeheer499-commits/strix-halo-guide/blob/main/MAX_PERFORMANCE_PLAN.md
- AMD 395+ · BAEM1N/llm-bench（**Q4_K_M** llama.cpp b8657 tg **45.4–46.2**，2026-04，早期 build）：https://github.com/baem1n/llm-bench/blob/main/results/consolidated/ryzen-ai.csv
- AMD 395+ · kmarble.dev（MS-S1 Max：ROCm 空 **46.2** / Vulkan **32.7**；满上下文掉到 16.6–37.5）：https://kmarble.dev/posts/strix-halo-full-context-decode-drops/
- AMD 395+ · plunderstruck HF（ROCmFP4/Vulkan decode **78–90**）：https://huggingface.co/plunderstruck/Qwen3.6-35B-A3B-MTP-ROCmFP4-GGUF
- AMD 395+ · jcbtc HF（MTP depth4 结构化解码 best-case **~105**）：https://huggingface.co/jcbtc/qwen3.6-35b-a3b-crown-halo-mtp-dynamic
- AMD 395+ · Signal65（**prefill**：35B-A3B prompt **1,273 t/s**；长上下文 prefill 时间表 2K 6.3s…128K 21.7min）：https://signal65.com/research/ai/amd-ryzen-ai-halo-first-look/
- AMD 395+ · zenn（Vulkan **prefill ~1,010–1,084 t/s**；20K 上下文 27s prefill 案例）：https://zenn.dev/shuzan/articles/72852bb9621b40
- AMD 395+ · SpecPicks（prefill compute-bound，随上下文变长）：https://specpicks.com/reviews/ryzen-ai-max-395-128gb-mini-pc-local-llm-news-2026
- AMD 395+ · strix-halo-guide（RADV 生成 62.56 balanced / 81.30 speed-first；MTP server ~101）：https://github.com/hogeheer499-commits/strix-halo-guide
- Mac M4 Max · oMLX（**prefill 全曲线**：pp 1K 1,099 / 4K 1,368 / 8K 1,357 / 32K 1,098 / 64K 838）：https://omlx.ai/benchmarks/pg7u9aqr
- Mac M4 Max · LLMCheck（Q4_K_M MLX **42 t/s**，48GB）：https://llmcheck.net/models/qwen-36-35b-a3b-on-m4-max/
- Mac M4 Max · batiai HF（IQ4_XS **45.9–46.5** warm，128GB，2026-05-03；MTP 峰见 programmer-666）：https://huggingface.co/batiai/Qwen3.6-35B-A3B-GGUF
- Mac M4 Max · programmer-666 HF（MTP pp1024/tg128 **81.5** 峰值）：https://huggingface.co/programmer-666/Qwen3.6-35B-A3B-oQ8-mtp
- Mac M3 Ultra · oMLX **Q4 归一**（80c 4bit：**tg 98.6@1k → 51.5@64k → 35.7@128k**；pp 1,638@1k → 2,617@8k → 968@128k，512GB，2026-04-17）：https://omlx.ai/benchmarks/6b70wq2p
- Mac M3 Ultra · willitrunai（**Q4_K_M decode 70.8 t/s**，256GB，prefill ~177 est）：https://willitrunai.com/can-run/qwen-3.6-35b-a3b-on-m3-ultra-256gb
- Mac M3 Ultra · siliconscore（**8bit**〔非 Q4〕48.0 估算，仅存档）：https://siliconscore.com/models/qwen3-6-35b-a3b/
- Mac M3 Ultra · mlx#3209（M3 Ultra 上下文扫描，带宽受限）：https://github.com/ml-explore/mlx/discussions/3209
- 价格 · B70 $949（Intel 官方 B 系页）：https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html
- 价格 · Intel mini-PC（Minisforum M1 Pro-125H）：https://store.minisforum.com/products/minisforum-m1-pro-125h-mini-pc

- **关键诚实点（MoE-on-Intel 反常）**：Intel SYCL 的 MoE 专家派发效率不如 CUDA——3B 激活的 MoE 在 Arc 上跑出的是"~9B dense 的速度"，不是"~3B dense 的速度"；极端例子 Gemma4-26B-A4B MoE 在 B70 上 30 t/s，**反而慢于** 9B dense 54 t/s，而同款在 RTX 3090 上 134 t/s（快过 9B dense）。→ MoE 优势真实但在 Intel 上被压缩。web(PMZFX FINDINGS)、a1 [20][21]
- **软件成熟度**：能用但比 CUDA 更 DIY。Vulkan = "开箱可用"首选；SYCL 上限更高但脆（oneAPI 2026.0 编译坏、kernel 派发 ~100–500µs vs CUDA ~5µs）；IPEX-LLM 2026 已弃；vLLM 走 Intel `llm-scaler` 容器。a1 [18][19][20][21]
- **Intel 官方营销**（对手= RTX Pro 4000 $1,800，Intel 自测）："上下文窗口 ↑2.2x"、"多 agent/多用户响应 ↑6.2x（TTFT）"、"每美元 token ↑2x"。多家媒体提示存疑。a1 [6][7][9]
- **能效**：B70 0.48 tok/s/W vs RTX 4090 0.16 / 3090Ti 0.18（约 3×）。web(CraftRigs)
- `[u]` 单卡 B70 上 Qwen3-30B-A3B、Gemma3-27B 的干净独立单流数字缺失；日历站/计算器 tok/s 是带宽估算非实测。a1 gaps

## 3. eGPU 互联事实（支撑"LLM≠游戏，带宽只影响加载"）

- **token 生成阶段 host↔GPU 链路近乎空闲**，瓶颈是卡上 VRAM 带宽；链路主要决定**模型加载时间**。a2 [S1][S3][S5]
- 加载时间（70B）：内置 x16 ~1.9s / OCuLink ~5.4s / TB5 ~6.8s / **TB4 ~13.2s** / USB4 ~13.6s——TB4 慢 5–7×，但每次换模型只付一次。a2 [S4]
- **稳态推理惩罚**（模型已驻显存）vs 内置 x16：OCuLink ~2–3%、**TB4/USB4 ~10–17%**；远低于游戏的 ~25–40%。a2 [S4][S5]
- TB4 = 40Gbps + **支持热插拔**；OCuLink = PCIe4 x4 / 64Gbps，更快更稳但**不支持热插拔**。a2 [S6][S7][S8]
- **NVIDIA eGPU 在 Linux 官方不支持、且真的痛**：开源内核驱动只认 TB3 桥，TB4/TB5 卡触发错误超时→"GPU fell off the bus"(Xid 79)、CUDA 负载下硬锁、ReBAR 失败致卡不出现在 nvidia-smi、热插拔坏。来源=NVIDIA 自家 GitHub issue/PR。a2 [S10-S14]
- **反向惩罚成立的情形**（诚实标注）：长上下文/prefill（USB4 上 2K+ 提示慢 30–40%、8K+ 慢 40–50%）、频繁换模型、超显存 offload、多卡张量并行。a2 gaps

## 4. Intel 支持 TB4 的消费级 CPU + mini-PC/NAS 产品

- **N305（Alder Lake-N）没有可用 TB4**：Alder Lake-N 无集成 Thunderbolt host；lspci 里 "Alder Lake-N Thunderbolt 4 USB Controller" 只是共享 IP 的 USB/xHCI 块，端口回落为 USB-only、无 PCIe 隧道→**不能做 TB4 eGPU**。N 系要接 eGPU 走 OCuLink 或 M.2→PCIe。a2 [S15][S16][S19][S20]
- **集成 TB4 在这些线上**：12/13 代 H/U（4× TB4）、Core Ultra Series 1（Meteor Lake）、Series 2 200H/200U（Arrow Lake，4×；HX 2×）；TB5 需外挂控制器。a2 [S17][S18]

| 产品 | CPU | eGPU 链路 | 热插拔 | 裸机价(~2026-07) | 备注 |
|------|-----|----------|--------|------|------|
| Minisforum M1 Pro-125H | Core Ultra 5 125H | OCuLink + 2×USB4 | 部分 | ~$367–459 | Intel |
| Minisforum UH125 Pro | Core Ultra 5 125H | OCuLink 64Gbps | 否 | ~$385 | Intel |
| Minisforum MS-01 | i9-13900H / i5-12600H | 2×USB4 + 内置 x16 | USB4 是 | ~$419–679 | Intel |
| AOOSTAR GEM12+ | AMD 8845HS | OCuLink + 2×USB4 | 否 | ~$359+ | **AMD（非 Intel）** |
| Minisforum N5 Pro AI NAS | AMD Ryzen AI 9 HX PRO 370 | OCuLink + x16 | 否 | ~$899–1,019 | **AMD（非 Intel）** |

- 注意：热门"带 OCuLink 的 AI NAS"头牌多是 **AMD**，别在 Intel 幻灯里暗示成 Intel。a2 [S24][S25]

## 5. 竞品对比机（Personal Agent / LLM，第一方实测）

Qwen3-30B-A3B tok/s（并发 1→8）与整机价（olares-one-benchmarks）：

| 机型 | 芯 | 显存/内存 | Qwen3-30B-A3B | 价 |
|------|----|-----------|---------------|----|
| **Olares One** | RTX 5090M 24GB | 96GB | **157→81**（vLLM，全场最高） | $3,999（$2,999 众筹） |
| Mac Studio M4 Max | M4 Max | 64GB 统一 | 81→20 | $2,699 |
| Mac Studio M3 Ultra | M3 Ultra | 96GB 统一 | 84→25（但能装 120B） | $5,499 |
| Beelink GTR9 Pro | **AMD Ryzen AI Max+ 395** | 128GB 统一 | 61→12（最低） | $2,099 |

- 诚实边界：GPT-OSS-120B 超 24GB 需 offload，Olares One 输给 Mac 统一内存；但吞吐/并发/图像/视频 Olares One 领先，且唯一全测跑通。olares-one-benchmarks
- **eGPU 幻灯的对比落点**：单 B70($949/32GB) 外挂盒 ≈ 一个便宜、够用、极省电的 Personal-Agent LLM 节点；相对 395+/Mac 的位置=更便宜的显存、更省电，但单流 tok/s 与软件顺滑度不及 CUDA。

## 6. Panther Lake（SoC）规格 + 会议转录可行性

- **Panther Lake = Core Ultra Series 3**，CES 2026 发布（1/6 预购、1/27 上市），首颗 **Intel 18A**。a3 [1][2]
- **NPU 5 最高约 50 TOPS（INT8）**；顶配平台最高约 **180 TOPS**。这是 `up to` 平台上限，不能套到 Ultra 5 等低价 SKU。a3 [1][3][7]
- **NPU 几乎没涨**：Lunar Lake NPU4 48 → Panther Lake NPU5 ~50；提升主要来自 **Xe3 GPU + 18A 能效**；两代都过 Copilot+ 的 40-TOPS 线。a3 [4][6]
- TB/USB4：与 Lunar Lake 同控制器（内核 6.13 加 ID），加 UHBR 10/20。Linux 实用需 **6.19+**。a3 [8][9][10]
- **会议转录 5 类模型本地跑：可行且已在售**（Fluid Inference **Slipbox**：Whisper v3 Turbo + PyAnnote/WeSpeaker 分离 + Qwen3/Phi-4-mini 总结，全本地，OpenVINO）。a3 [12]
- **实测**（Lunar Lake 258V，48-TOPS NPU）：Whisper-base.en INT8 = **NPU 49.8× 实时**（vs iGPU 39×、CPU 27–30×），~2–3W。a3 [11][12]
- **诚实反例（限定范围）**：在一台 Lunar Lake 258V、特定 OpenVINO / 模型配置的社区测试中，Llama-3.2-1B NPU 仅 2.07 t/s、8B 崩溃，而 iGPU 上 3B 约 20 t/s。这个结果证明平台需要异构执行，但**不能泛化为 Panther Lake 或所有 NPU 优化模型**。建议优先评估 NPU 承载 STT/分离，iGPU 或 NPU 承载小模型总结，CPU 负责控制流与回退；最终以 Panther Lake PoC 为准。a3 [11][12]
- 5 类模型：①说话人分离 ②STT ③强制对齐 ④翻译 ⑤LLM 总结；前 3 必选，后 2 可选（与飞书妙记一致，LLM 总结是付费/可选）。a3 [12]

### 6.1 Panther Lake 设备价格与 SoC 成本（2026-07-14）

| 设备 | SKU / 配置 | 价格 | 状态 / 来源 |
|------|-------------|------|-------------|
| MSI Cubi NUC AI+ 3MG | Ultra 5 322，裸机 | **$584.99** | Newegg 自营可购买：https://www.newegg.com/msi-barebone-intel-core-ultra-5-322-cubi-nuc-ai-3mg-008bus/p/N82E16856167221 |
| ASRock NUC BOX-325 | Ultra 5 325，裸机 | **$649.99** | Newegg backorder：https://www.newegg.com/asrock-industrial-fanned-embedded-box-intel-core-ultra-5-325-nuc-box-325/p/N82E16856179019 |
| Minisforum M2 | Ultra 7 356H，裸机 | **$527 促销 / $659 常规** | 官方：https://store.minisforum.com/products/minisforum-m2-mini-pc |
| Minisforum M2 | Ultra 7 356H，32GB + 1TB | **$959 促销 / $1,199 常规** | 同上 |
| ASRock NUC BOX-358H | Ultra X7 358H，裸机 | **$999.99** | Newegg：https://www.newegg.com/asrock-industrial-fanned-embedded-box-intel-core-ultra-x7-358h-nuc-box-358h/p/N82E16856179018 |

- Intel ARK 只列 Panther Lake 移动 SoC 的 `Tray` 订货信息，**没有公开 RCP / 1K unit price**。Ultra 5 325：https://www.intel.com/content/www/us/en/products/sku/245720/intel-core-ultra-5-processor-325-12m-cache-up-to-4-50-ghz/ordering.html ｜ X7 358H：https://www.intel.com/content/www/us/en/products/sku/245527/intel-core-ultra-x7-processor-358h-18m-cache-up-to-4-80-ghz/ordering.html
- 从同机型价差与整机价反推的 **OEM 有效成本估算，不是 Intel 报价**：Ultra 5 322/325 **$180–250（中置信）**；338H/356H **$250–350（中）**；X7 358H **$350–500（中低）**；X9 388H **$450–650（低）**。
- **价格判断**：已售整机证明 `$999–1,199` 值得作为 Ultra 5 / 356H、DTC 或 OEM 合作的验证目标，但不能从单一促销价直接推出新产品的可持续定价；X7 358H 小批量不适合 `$999`。

## 7. 会议转录 / AI 录音笔市场

| 项 | 数字 | 来源 |
|----|------|------|
| AI meeting assistant 整体市场 | 2025 年约 **$3.1–3.5B**；2030 年 **>$9B**；长期 CAGR 约 **24–26%**。分析机构估算，市场定义存在差异，主要代表软件/服务需求，不能当 Intel 硬件 TAM | GVR https://www.grandviewresearch.com/industry-analysis/ai-meeting-assistant-market-report ｜ TBRC https://www.thebusinessresearchcompany.com/report/artificial-intelligence-ai-powered-meeting-assistants-global-market-report |
| Plaud 累计出货 | **>2M 台**，170+ 国 | a3 [16][17] |
| Plaud 软件 ARR | **$100M**（2026-06），2 年 $1M→$100M | a3 [16][17] |
| Plaud 付费转化 | **~50%** 设备用户升级 | a3 [16] |
| Otter.ai 规模 | **>$100M ARR、>35M 用户、>1B 场会议**（公司自报） | https://otter.ai/blog/otter-ai-caps-transformational-2025-with-100m-arr-milestone-industry-first-ai-meeting-agents-and-global-enterprise-expansion |
| Plaud 硬件价 | $159（Note/NotePin）/ $179（NotePin S）/ $189（Note Pro） | a3 [17] |
| Plaud 订阅 | Pro $99.99/yr（1,200 min/mo）；Unlimited $239.99/yr；月付 $17.99/$29.99 | a3 [17] |
| Plaud 总营收/估值 | ~$250M 年化(2025-09)；~$2B 估值 `[u]` | a3 [18] |
| 品类其他 | Pocket(YC W26) 35K 台/$27M ARR；DingTalk A1；Anker×飞书"录音豆"899￥；Viaim；Chumenwenwen TicNote；Notta Memo $149；Limitless→Meta；Bee→Amazon | a3 [19][20][21] |
| Mobvoi / TicNote | Mobvoi 为港交所主板上市公司（2438）；TicNote 2025 年中披露全球约 3 万台；TicNote Pods Kickstarter 510 位支持者。可称 Plaud 之外的主流挑战者，**无公开证据支持全球第二** | 港交所 https://www.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032700788.pdf ｜ https://time-weekly.com/post/324056 ｜ Kickstarter https://www.kickstarter.com/projects/mobvoi/ticnote-pods-worlds-smartest-4g-ai-note-taking-earbuds |
| 专用 AI 录音硬件品类总量 | **"~3M 台/年"= 拼装估算 `[u]`**；无公开权威年度总销量，不能写成第三方市场事实。可确认的是 Plaud 累计 >2M，且 Euromonitor 认定其为 2025 年销量第一品牌但未披露份额 | a3 [22] ｜ https://www.plaud.ai/blogs/news/plaud-confirmed-as-world-number-one-ai-note-taking-device-brand |

- 目标人群：律师/医生/销售/记者——访谈多、内容敏感；组织级更重客户/患者隐私与合规，一台盒子多人用摊薄成本。（用户论点；SEO 侧 HIPAA/legal/GDPR 词已在 plaud.md 佐证）
- **云端处理边界**：Otter 条款明确音频在云基础设施处理；Plaud 默认本地保存录音，但请求转写/总结时仍将所需数据发送给 AI 服务商，服务商承诺 zero retention。不能写成“两家公司都长期收集会议记录”。Otter：https://otter.ai/terms-of-service ｜ Plaud：https://support.plaud.ai/hc/en-us/articles/57744162858009-How-your-data-is-used-in-AI-processing
- **合规边界**：本地处理减少第三方数据暴露并帮助控制驻留、权限和保留期限，但不自动满足 HIPAA / GDPR；录音同意、审计、删除与合同责任仍需落实。
- **已确认合作**：Olares 与 Mobvoi / 出门问问确认录音端合作；TicNote 卡片与 TicNote Pods 为主力移动端点。当前 TicNote 仍走云端 AI 处理，“加密回传到机构自己的 Olares box”是目标产品链路，不是已上线能力。
- **配件生态**：对外可列录音卡片、AI 耳机、USB / 蓝牙会议麦克风音箱、手表 / 穿戴、手机、会议室麦克风或现有会议系统。只有 TicNote 卡片 / Pods 是已确认合作；其他形态为支持方向 / planned adapters。

## 8. Offer 测算（用户拟定，非市场价）

- Offer 设想：**5 个混合录音端 + 1 个共享 AI box**；AI box 目标 **$999–1,199**。示例组合为 3×TicNote 卡片（$159.99）+ 2×4G TicNote Pods（$299）+ $999 box ≈ **$2,077**，所以可写 **~$2,000 target bundle**，最终以合作价和 SKU 为准。
- TCO 加分项：Plaud 5 人 3 年为设备 `5×$185` + 订阅 `5×$240/yr×3` ≈ **$4,525**。本地方案可减少持续云订阅，但 Olares 是否收取软件服务费尚未确定，不能写“软件 $0/年”或承诺固定回本期。
- 规划规模：估算品类 ~3M 台 / 年 × 5% = **15 万台 / 年情景**；这是用户年度销售规划模型，不是第三方市场预测。
- 口径提醒：合作端价格、最终包价、5% 份额、3M 品类量均为**假设/拟定值**，非实测；标注清楚。

## 9. 待核实 / 低置信

- 单卡 B70 的 Qwen3.6-35B-A3B tok/s 跨来源 54.7–82，取决量化/调优/是否 MTP → 用**区间**并注"社区实测、中置信"。
- 单卡 B70 Qwen3-30B-A3B / Gemma3-27B 干净单流数字缺失 `[u]`。
- Plaud $2B 估值、品类"~3M 台/年" 均 `[u]`。
- 逐 SKU 算力差异已补：Ultra 5 322 约 **46 NPU / 18 GPU TOPS**；Ultra 7 356H 约 **50 / 40**；Ultra X7 358H 约 **up to 50 / 122**。322 的 Intel ARK 数值字段当前未正常渲染，以 MSI 设备资料和第三方规格交叉验证；356H 来自 Minisforum M2 官方页；358H GPU 来自 Intel ARK、NPU 来自 ASUS 规格。`180 Platform TOPS` 仅是顶配上限。
- Panther Lake 移动 SoC 没有公开 RCP；本登记的芯片成本均为整机反推估算。
- Bee→Amazon / Limitless→Meta 收购本轮未独立证实 `[u]`。
- Intel 营销 2.2x/6.2x/2x 为 Intel 自测 vs 更老更贵的 RTX Pro 4000，依赖其软件栈，未被独立复现。

## 来源分组

- Arc Pro B70/B60 + LLM + 软件：`task-a1-arc-pro-llm.md`（25 源）+ 本轮 web（PMZFX B70 benchmark repo、CraftRigs、r/LocalLLaMA/AI Weekly）
- eGPU 互联 + NVIDIA-Linux + Intel TB4 CPU/产品：`task-a2-egpu-tb4-cpu.md`（25 源）
- Panther Lake + 会议转录 + 市场：`task-a3-panther-lake-meeting.md`（22 源）
- 竞品实测机：[olares-one-benchmarks.md](/Users/pengpeng/seo/directions/hardware/research/olares-one-benchmarks.md)
- Qwen3.6 型号规格：HuggingFace Qwen/Qwen3.6-35B-A3B、Qwen/Qwen3.6-27B（README，2026-04）
