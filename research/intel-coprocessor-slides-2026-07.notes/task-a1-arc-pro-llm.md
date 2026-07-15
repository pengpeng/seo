# Task A1 — Intel Arc Pro B-series for Local LLM Inference (personal-cloud / AI-NAS eGPU use case)

> AS_OF = 2026-07-14. Every figure below carries a source number + publication date. Numbers I could not independently verify are marked **[unverified]**. Bandwidth-derived "estimates" from calculator sites are flagged as such and are NOT independent measured benchmarks.

---

## Sources

1. **Intel Arc Pro B-series overview page** — https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html — Source-Type: Vendor (Intel first-party) — As-Of: 2026-03 (product page, retrieved 2026-07-14). Spec table for B70/B65/B60/B50.
2. **Intel Arc Pro B70 datasheet (PDF)** — https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf — Source-Type: Vendor datasheet — As-Of: 2026-03.
3. **gpupoet.com — Arc Pro B70 specs page** — https://gpupoet.com/gpu/learn/card/intel-arc-pro-b70 — Source-Type: Third-party spec aggregator — As-Of: retrieved 2026-07-14 (post-launch).
4. **igor'sLAB (EN) — "Intel launches the Arc Pro B70 … for $949"** — https://www.igorslab.de/en/intel-launches-the-arc-pro-b70-with-32-gb-of-vram-for-949-big-battlemage-is-coming-first-for-ai-and-workstations/ — Source-Type: Independent tech press — As-Of: 2026-03-25.
5. **VideoCardz.net — Arc Pro B70 spec DB** — https://videocardz.net/intel-arc-pro-b70 — Source-Type: Third-party spec DB — As-Of: last update 2026-03-25.
6. **Intel Newsroom — Core Ultra Series 3 vPro + Arc Pro B70/B65 launch release** — https://newsroom.intel.com/client-computing/intel-core-ultra-series-3-with-vpro-powers-next-gen-pcs-on-18a — Source-Type: Vendor press release — As-Of: 2026-03-25. Contains the three headline marketing claims (footnoted 6/7/8).
7. **WCCFTech — "Arc Pro B70 Outclasses NVIDIA RTX Pro 4000…"** — https://wccftech.com/intel-arc-pro-b70-outclasses-nvidia-rtx-pro-4000-in-ai-at-half-the-cost/ — Source-Type: Tech press (reporting Intel slides) — As-Of: 2026-03-25/26. Detailed slide numbers (93K vs 42K context, 85% throughput, per-model context figures).
8. **Neowin — "Intel: Our Arc Pro B70/B65 32GB GPUs slam Nvidia RTX Pro"** — https://www.neowin.net/news/intel-our-arc-pro-b70-b65-32gb-gpus-slam-nvidia-rtx-pro-graphics-cards/ — Source-Type: Tech press — As-Of: 2026-03-25. Confirms competitor = RTX Pro 4000.
9. **Notebookcheck — "Arc Pro B70 performance metrics… half the price, 33% more VRAM"** — https://www.notebookcheck.net/Intel-Arc-Pro-B70-performance-metrics-significantly-faster-than-Nvidia-s-RTX-4000-Pro-at-half-the-price-and-33-more-VRAM.1259566.0.html — Source-Type: Tech press — As-Of: 2026-03-26. Notes RTX 4000 Pro = $1,800; skeptical framing ("may or may not be accurate in true Intel fashion").
10. **EmbeddedLLM blog — "Benchmarking LLM Inference on Intel Arc Pro B60: vLLM vs LLM-Scaler"** — https://embeddedllm.com/blog/benchmarking-llm-inference-intel-arc-pro-b60 — Source-Type: Independent measured benchmark (4× B60, Sparkle-supplied HW) — As-Of: 2025 (post-B60 launch; retrieved 2026-07-14). **Only independent measured MoE (Qwen3-VL-30B-A3B) numbers found.**
11. **StorageReview — "Arc Pro B60 Battlematrix Preview: 192GB VRAM for On-Premise AI"** — https://www.storagereview.com/review/intel-arc-pro-b60-battlematrix-preview-192gb-of-vram-for-on-premise-ai — Source-Type: Independent tech press — As-Of: 2025. $600/GPU, $600–1,200 entry, 8×24=192GB, 1,576 INT8 TOPS combined.
12. **everylocalai.com — Arc Pro B60 local-AI page** — https://everylocalai.com/hardware/arc-pro-b60 — Source-Type: Third-party calculator — As-Of: retrieved 2026-07-14. **Numbers are ESTIMATES derived from memory bandwidth, NOT measured** (self-described "estimated from memory bandwidth").
13. **GigaGPU — "Running Ollama on Arc Pro B60" / "LLM Inference on Arc Pro B60 (IPEX-LLM & llama.cpp SYCL)"** — https://gigagpu.com/intel-arc-pro-b60-ollama/ and https://gigagpu.com/intel-arc-pro-b60-llm-inference/ — Source-Type: Cloud-GPU vendor (est. figures) — As-Of: retrieved 2026-07-14. Tok/s marked "(est.)" — treat as estimates.
14. **Intel Developer — "Introduction to Project Battlematrix"** — https://www.intel.com/content/www/us/en/developer/articles/technical/introduction-project-battlematrix.html — Source-Type: Vendor — As-Of: 2025 (roadmap Q3/Q4 2025). 8-GPU / 192GB / 1,576 TOPS; containerized Linux stack.
15. **Intel Developer — "Project Battlematrix Software Update (Aug 2025)" / LLM-Scaler 1.0** — https://www.intel.com/content/www/us/en/developer/articles/technical/battlematrix-software-update-august2025.html — Source-Type: Vendor — As-Of: 2025-08.
16. **Phoronix — "Intel Releases LLM-Scaler 1.0 (Project Battlematrix)"** — https://www.phoronix.com/news/Intel-LLM-Scaler-1.0 — Source-Type: Independent Linux press — As-Of: 2025-08.
17. **GitHub intel/llm-scaler (vLLM)** — https://github.com/intel/llm-scaler/tree/main/vllm — Source-Type: Vendor OSS repo — As-Of: retrieved 2026-07-14. Intel-optimized vLLM container, model support matrix.
18. **SpecPicks — "Intel Axes BigDL/IPEX-LLM: Where Local Inference Goes Next"** — https://specpicks.com/reviews/intel-ends-bigdl-ipex-llm-local-inference-alternatives-2026 — Source-Type: Third-party analysis — As-Of: 2026. IPEX-LLM deprecation; Vulkan-first advice.
19. **DEV.to (starrzan) — "Running Local LLMs on Intel Arc iGPU: Ubuntu guide"** — https://dev.to/starrzan/running-local-llms-on-intel-arc-igpu-a-complete-guide-for-ubuntu-on-mini-pc-hardware-40bc — Source-Type: Practitioner writeup — As-Of: 2026. SYCL+MKL build pain, oneAPI dependency.
20. **GitHub ggml-org/llama.cpp Discussion #12570 — "Current status of Intel Arc GPUs for llama.cpp"** — https://github.com/ggml-org/llama.cpp/discussions/12570 — Source-Type: OSS maintainer/user thread — As-Of: ongoing through 2026. Real B70 user tok/s; Vulkan 30–60% faster than SYCL for text-gen.
21. **GitHub ggml-org/llama.cpp Issue #23533 — "SYCL MTP on Intel Arc"** — https://github.com/ggml-org/llama.cpp/issues/23533 — Source-Type: OSS issue — As-Of: 2026. Real single-B70 measured tok/s (Qwen3.5-27B dense 25 t/s; 35B MoE Q4_K_M 82.2 t/s); oneAPI 2026.0 build breakage.
22. **VideoCardz — "Arc Pro B60 24GB listed at $599, in stock"** — https://videocardz.com/newz/intel-arc-pro-b60-24gb-professional-gpu-listed-at-599-in-stock-and-shipping — Source-Type: Tech press — As-Of: 2026 (retail listing). ASRock B60 Creator @ $599.
23. **Intel Ark — Arc Pro B60 official SKU spec page** — https://www.intel.com/content/www/us/en/products/sku/243916/intel-arc-pro-b60-graphics/specifications.html — Source-Type: Vendor — As-Of: launch Q2'25. 197 TOPS, 12.28 FP32 TFLOPS, 456 GB/s, 24GB, 160 XMX.
24. **TechReport — "Is Intel's Arc Pro B60 the Dual GPU Innovation…"** — https://techreport.com/news/hardware/intel-arc-pro-b60-dual-gpu/ — Source-Type: Tech press — As-Of: 2025 (Computex). Maxsun B60 Dual 48GB, ~$1,000–1,200; 48GB via RTX 6000 Ada would cost $5,000–6,000.
25. **Tom's/Yahoo Tech — "Intel launches $299 Arc Pro B50 … B60 workstations"** — https://tech.yahoo.com/computing/articles/intel-launches-299-arc-pro-103002856.html — Source-Type: Tech press — As-Of: 2025 (Computex). ~$500/GPU B60; Battlematrix systems $5,000–10,000; up to 70B+ models.

---

## Findings (each ≤1 line, cites source #)

1. **B70 confirmed:** 32GB GDDR6, 367 INT8-dense TOPS, 608 GB/s, 256-bit, PCIe 5.0 x16, 230W (Intel card; 160–290W partners), $949, launched 2026-03-25, die BMG-G31 (TSMC N5). [1][2][4][5]
2. B70 has 32 Xe2-HPG cores + 256 XMX engines; 22.94 FP32 TFLOPS; XMX supports INT2/4/8, FP16, BF16, TF32. [2][3]
3. **B60 confirmed:** 24GB GDDR6, 197 INT8 TOPS, 456 GB/s, 192-bit, PCIe 5.0 x16 (x8 electrical), 120–200W, 20 Xe cores/160 XMX, 12.28 FP32 TFLOPS; retail ~$599 (ASRock Creator). [23][22][25]
4. **B60 Dual 48GB** (2×24GB, Maxsun Turbo) ~$1,000–1,200; needs PCIe bifurcation (x8+x8); vs ~$5,000–6,000 for 48GB NVIDIA RTX 6000 Ada. [24]
5. **Independent MEASURED MoE benchmark (only one found):** 4× B60 + vLLM/LLM-Scaler running Qwen3-VL-30B-A3B ≈ **~1,000 tok/s aggregate** at 64 concurrent, linear scaling 16→64; TPOT 44–61 ms/token; TTFT <5s. [10]
6. **Real single-B70 llama.cpp measurements (user-reported):** Qwen3.5-27B dense Q4_K_S = **25 tok/s** (36.8 with MTP); Qwen3.5/3.6-35B-A3B MoE Q4_K_M = **82.2 tok/s** single stream. [21]
7. Real B70 vLLM user report: single-stream jumped **20 → 60 tok/s** after tuning, matching llama.cpp. [20]
8. B60 single-card tok/s widely quoted (Llama3 8B Q4 ~50–55, Gemma2 27B Q4 ~16–20, Qwen2.5-14B ~30–35) are **ESTIMATES from bandwidth, not measured** — treat as [unverified]. [12][13]
9. **Marketing claims (exact wording, competitor = NVIDIA RTX Pro 4000, ~$1,800):** "Up to 2.2x larger context windows," "Up to 6.2x faster responses in multi-agent/multi-user workloads," "Up to 2x tokens per dollar" — all "vs the competition." [6][7][8][9]
10. Claim substantiation: 2.2x context = 93K vs 42K tokens (Llama3.1-8B BF16 OOM point); 85% higher multi-user throughput (Ministral 8B BF16, Linux); 6.2x = time-to-first-token in multi-user; 2x tok/$ holds across 1/2/4-GPU. [7][9]
11. **Project Battlematrix:** up to 8× Arc Pro B60, 192GB combined VRAM, 1,576 INT8 TOPS, Xeon PCIe Gen5 platform; containerized Linux "LLM-Scaler" stack (vLLM + IPEX), multi-GPU tensor parallel + PCIe P2P, ECC/SR-IOV/telemetry. [11][14][15][17]
12. **Software maturity verdict:** functional but more DIY than CUDA — Vulkan = most reliable "just works"; SYCL faster ceiling but fragile (oneAPI 2026.0 build breakage, ~100–500µs kernel dispatch vs ~5µs CUDA); IPEX-LLM effectively deprecated 2026; vLLM only via Intel's LLM-Scaler container. [18][19][20][21][17]

---

## Deep Read Notes

### 1. B70 hardware & positioning (confirmed)
Intel's own datasheet [2] and overview table [1] confirm every headline figure from the brief: 32GB GDDR6, 367 TOPS (INT8 dense), 608 GB/s, 256-bit bus, PCIe Gen5 x16, and 230W for the Intel-branded card (partners span 160–290W). Launch was **2026-03-25** at **$949** MSRP [4][5][6]. The die is **BMG-G31** on TSMC N5, ~27.7B transistors, 368 mm², 32 Xe2-HPG cores, 256 XMX engines, boost up to ~2.8 GHz [3][5]. Note a naming subtlety: Intel's B-series table also lists a **B65** (20 cores, 197 TOPS, 608 GB/s, 32GB) launching mid-April 2026 — separate from the 24GB B60 [1][4]. The B70 is explicitly pitched at "powerful local inferencing, large model ready," leaning on the 32GB capacity for bigger models / higher precision.

For the personal-cloud / AI-NAS eGPU angle, the relevant strengths are: **large VRAM per dollar** (32GB @ $949), **PCIe 5.0 x16** (full bandwidth if the NAS/host exposes it — many AI-NAS boxes only give x8 or x4, worth flagging), **160–290W** envelope (fits a single 8-pin/16-pin, blower and *passive* SKUs exist from Sparkle/ASRock/Maxsun — the passive/blower variants are ideal for dense NAS chassis) [5], and 4× DisplayPort 2.1 (irrelevant for headless NAS). The weak point vs NVIDIA is **memory bandwidth**: 608 GB/s is mid-tier — an RTX 3090/4090 sits at ~936 GB/s–1 TB/s, and decode speed for LLMs is bandwidth-bound, so per-stream tok/s will trail same-VRAM NVIDIA cards.

### 2. Local-LLM benchmarks — what's real vs estimated
This is the most important nuance for an honest note. Two classes of numbers circulate:

- **Estimates (NOT measured):** everylocalai [12] and GigaGPU [13] publish tidy tok/s tables (e.g., B60 Llama3-8B Q4 ~50–55 t/s, Gemma2-27B Q4 ~16–20 t/s, Qwen2.5-14B ~30–35 t/s). everylocalai explicitly says these are "estimated from memory bandwidth … calibrated against measured RTX-40-series, typically within ~15%." GigaGPU labels its tables "(est.)." **Do not present these as independent benchmarks** — they are bandwidth math. They are directionally useful (B60 ≈ 50 t/s on an 8B, ≈ 25–30% behind an RTX 3090 due to the 456 vs 936 GB/s bandwidth gap) but not primary evidence.

- **Actually measured:**
  - **EmbeddedLLM [10]** is the strongest independent source: a 4× B60 workstation (Sparkle-supplied), vLLM 0.12 vs Intel's LLM-Scaler 1.2, running **Qwen3-VL-30B-A3B-Instruct** (the MoE the brief specifically asked about). Findings: linear throughput scaling 16→32→64 concurrent; **~1,000 tok/s aggregate** long-form throughput at peak; TTFT ~1.8–4.2s at 16 concurrent; TPOT 44–61 ms/token; LLM-Scaler gives ~20–25% better TPOT (token streaming), vanilla vLLM gives lower TTFT. This is aggregate/concurrent throughput, not single-stream — important framing.
  - **llama.cpp user reports on B70 [21][20]:** single B70, **Qwen3.5-27B dense Q4_K_S = 25 tok/s** (36.8 with multi-token prediction), and **35B-A3B MoE Q4_K_M = 82.2 tok/s** single stream. A merged PR (Q8_0 reorder optimization) gave a **3.1× text-gen speedup on B70** (4.88 → 15.24 t/s on Qwen3.5-27B Q8_0) [20]. Another user went **20 → 60 tok/s** on B70 in vLLM after tuning, matching llama.cpp [20]. These are individual reports (not a controlled review) but are real measurements on the target hardware and align with the "MoE runs surprisingly well, dense ~25 t/s at 27B" picture.

  Net: For a single B70 the realistic expectation is ~25 tok/s on a dense ~27–32B Q4 model and meaningfully higher (60–80+ t/s) on a 30–35B **MoE** (A3B active params), single-stream. Concurrency scales well with vLLM/LLM-Scaler across multiple cards.

### 3. Software stack maturity on Linux
The consistent message across independent sources [18][19][20][21]: **it works, but it is more DIY than CUDA.**
- **llama.cpp Vulkan** = the "it just works" path — most reliable, least config, precompiled builds exist; recommended as the default first try [18][20]. Ubuntu 26.04 > 24.04 for Vulkan perf [20].
- **llama.cpp SYCL** = higher ceiling but fragile. Requires Intel oneAPI (IntelLLVM icx/icpx) because the SYCL backend hard-requires MKL's SYCL BLAS, which the open-source dpc++ can't provide [19]. As of 2026, **the ggml-sycl backend does not compile with the oneAPI 2026.0 DPC++ compiler**, and the 2026.0 runtime needs a Level-Zero v2 API not yet in the public driver — a concrete "DIY pain" data point [21]. Maintainers/Codeplay are actively optimizing (DP4A, mul_mat_vec_q kernels); today **Vulkan is ~30–60% faster than SYCL for text generation** [20]. Core bottleneck is **kernel dispatch overhead (~100–500µs vs ~5µs on CUDA)**, which especially hurts MoE (≈960 expert matmul dispatches/token) on a single GPU [21].
- **IPEX-LLM** is effectively **deprecated** in 2026 (Intel wound down BigDL/IPEX-LLM active dev); existing builds still run but fall behind on new model architectures [18]. Migration advice: move to llama.cpp Vulkan/SYCL.
- **vLLM** on Arc is available primarily through **Intel's `intel/llm-scaler-vllm` container** (an Intel-optimized vLLM fork), not upstream pip-install — you're expected to run their Docker image with `--device=/dev/dri`, the `xe` kernel driver, tensor parallelism and fp8/int4 quant [17][10].
- **OpenVINO** and **Ollama (Level Zero)** are maturing paths; OpenVINO+llama.cpp reportedly "crazy fast" on Arc but "most things don't work yet" [20][19].
Bottom line vs NVIDIA CUDA: **CUDA is turnkey and universally supported; Arc is a "choose Vulkan, expect to tinker, use Intel's container for serving" experience.** Fine for a hobbyist/prosumer personal-cloud builder who tolerates setup; risky for anyone wanting zero-config.

### 4. Marketing claims (exact wording) — competitor is RTX Pro 4000
From Intel's own newsroom release [6] (footnotes 6/7/8) and echoed verbatim by press [7][8][9]:
- "**Up to 2.2x larger context windows** with the Intel Arc Pro B70 versus the competition."
- "**Up to 6.2x faster responses in multi-agent/multi-user workloads** with the Intel Arc Pro B70 versus the competition."
- "**Up to 2x tokens per dollar** performance with the Intel Arc Pro B70 versus the competition."

The **competition is explicitly NVIDIA's RTX Pro 4000** (a.k.a. "RTX 4000 Pro"), confirmed by Neowin [8] and Notebookcheck [9]; Notebookcheck pegs that card at **$1,800 vs B70's $949** and notes it's "a few years old." Substantiation from Intel's slides [7][9]: the 2.2x context = **93K vs 42K tokens** before OOM (Llama3.1-8B, BF16); the multi-user throughput slide shows **85% higher token throughput** (Ministral Instruct 2410 8B, BF16, Linux) and the **6.2x** figure specifically = **time-to-first-token** in multi-user; per-model context on a **4-GPU** setup: DS-R1-Distill-Qwen3-32B (Int4) 183K vs 80K, Qwen3-32B (FP8) 304K vs 199K, Mistral-Small 24B (BF16) 408K vs 243K; **2x tokens/dollar holds across single/dual/quad-GPU** [7]. Caveat: these are Intel-run numbers against an older, pricier NVIDIA card, and the speed claims lean heavily on Intel's oneAPI/software stack, not raw silicon [9] — Notebookcheck flags them as "may or may not be accurate in true Intel fashion."

### 5. Multi-GPU / Project Battlematrix
Intel advertises **scalable multi-GPU LLM Linux support** on the B70 datasheet itself [2], productized as **Project Battlematrix** [14][15]: up to **8× Arc Pro B60**, **192GB combined VRAM**, **1,576 dense INT8 TOPS**, on a workstation-class Xeon PCIe Gen5 platform, targeting 70B+ models [14][25]. The software is the **containerized LLM-Scaler** stack for Linux — multi-GPU tensor parallelism + **PCIe P2P** transfers, plus enterprise features (**ECC, SR-IOV, passthrough virtualization, XPU-manager telemetry, remote firmware update**) [14][15]. **LLM-Scaler 1.0** shipped Aug 2025 [15][16] with vLLM serving, by-layer online quantization, experimental pipeline parallelism / torch.compile / speculative decoding; hardened + full-feature releases targeted Q3/Q4 2025. Prebuilt full systems (Battlematrix workstations) were floated at **$5,000–10,000** [25]. For a personal-cloud/AI-NAS builder, the accessible entry is 1× B60 (~$600) or the B60 Dual 48GB card (~$1,000–1,200) [11][24], scaling up later.

### 6. Value vs NVIDIA / AMD
- **$/GB VRAM:** B70 = $949/32GB ≈ **$29.7/GB**; B60 = $599/24GB ≈ **$25/GB**; B60 Dual = ~$1,200/48GB ≈ **$25/GB**. NVIDIA RTX Pro 4000 (~$1,800/24GB) ≈ $75/GB; RTX 6000 Ada (48GB) ≈ $5,000–6,000 ≈ **$104–125/GB** [24]. Arc Pro is ~3–5× cheaper per GB of VRAM. [22][24][9]
- **tok/s per dollar (single-stream):** Arc trails NVIDIA on raw tok/s (bandwidth-bound: B60 456 GB/s vs RTX 3090 936 GB/s → ~25–30% slower [10-adjacent, 12/13 estimates]) but wins on tok/$/GB because the cards are far cheaper. Intel's own "2x tokens per dollar" claim is vs the older RTX Pro 4000 [6][7].
- **vs AMD:** the everylocalai comparison table [12] puts AMD RX 7900 XTX (24GB, 960 GB/s) at ~112 t/s on Llama3-8B Q4 vs B60's estimated ~53 t/s — i.e., AMD's higher bandwidth wins on raw single-stream speed at similar VRAM, but that's a bandwidth-estimate comparison, not a controlled head-to-head, and doesn't factor price or the B60 Dual's 48GB density. [12]

---

## Gaps & Caveats

- **No fully independent, controlled single-card B70 review with a standardized tok/s suite** was found as of 2026-07-14. B70 tok/s here come from (a) llama.cpp GitHub user reports [20][21] and (b) Intel's own marketing slides [7]. Treat single-card B70 dense/MoE numbers as **indicative, not lab-verified**.
- **Qwen3-30B-A3B on a single B70**: no clean independent number found. Closest = 4×B60 aggregate (EmbeddedLLM, Qwen3-VL-30B-A3B, ~1,000 tok/s at 64 concurrent) [10] and single-B70 "35B-A3B MoE Q4_K_M 82.2 t/s" user report [21]. The specific **Qwen3-30B-A3B single-B70 single-stream tok/s = [unverified]**.
- **Gemma3-27B / Qwen3-32B on B70**: no independent measured tok/s found; only bandwidth-estimated B60 figures for older Gemma2-27B (~16–20 t/s, estimate) [13] and a real B70 "27B dense Q4 = 25 t/s" [21]. Gemma3-27B specifically = **[unverified]**.
- **B60/B70 pricing is fluid:** Intel never published an official B60 MSRP; $599 is a retail sighting [22], early channels asked $1,000–1,200. B60 Dual $1,200 is a press estimate, not a fixed MSRP [24]. Treat prices as **approximate**.
- **Marketing claims are Intel-generated** against an **older, ~2× pricier** NVIDIA card (RTX Pro 4000, $1,800), and depend on Intel's software stack; multiple outlets flagged skepticism [9]. Not independently reproduced.
- **Contrarian claim (worth surfacing):** Per llama.cpp maintainers/users [20][21], on a *single* GPU the SYCL backend is currently **30–60% SLOWER than Vulkan** for text generation, and **MoE models actually regress with multi-token prediction on a single card** (−23% on 35B-A3B) because expert-dispatch overhead dominates — i.e., the "Battlemage is great for MoE" story only really holds **across multiple GPUs**, and Intel's own advertised speedups lean on multi-GPU + their proprietary container, not out-of-the-box single-card upstream software. A prosumer dropping one B70 into an AI-NAS should expect modest dense tok/s (~25 t/s @ 27B Q4) and real setup effort, not NVIDIA-class plug-and-play.
