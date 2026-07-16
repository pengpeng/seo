---
task_id: audit
role: P6/P7 adversarial auditor
status: complete
as_of: 2026-07-15
mode: Standard
approved_sources_after_audit: 44
corrections: 6
---

# P6/P7 adversarial audit

## Verdict

**Substantive verdict: pass after correction. Workflow verdict: conditional pass.** The exact nine-model shortlist, Gemma 4 release and Apache 2.0 status, DeepSeek V4/MiniMax M3 exclusion rationale, Hunyuan3D bespoke license, Wan2.2 ≥24GB boundary, six Olares manifests, dGPU generation split, allocation chips, defaults, and disruptive mode-switch lifecycle are supported. Standard G2 still fails because all 44 Approved sources are `official`; the report now discloses that this evidence set verifies catalog/code facts but is not independent performance validation.

## Audit scope

- Checked every factual sentence and every global citation `[1]`–`[44]` in the final report against the four task notes, registry, and underlying official pages or repository files.
- Re-read all six runtime Manifests and the Olares compute-mode implementation at checkouts `terminus-apps bad4b060` and `Olares 6f2b93e6c`; both checkouts were clean.
- Searched the supplied notes and official repositories for contrary evidence, especially model memory floors, licensing, GPU availability, Manifest matrices, default allocation modes, and switch ordering.
- Added `[44]` for `compute/device_mode.go`, the previously missing direct source for writing the share-mode annotation.

## P6 findings and corrections

1. **High — ACE-Step variant and memory statement was false.** The source does not define an “ACE-Step 1.5 standard” variant and does not support “below 4GB.” It states ≥4GB for DiT-only, ≥6GB for LLM+DiT, and ≥12GB with offload for XL 4B. Corrected the recommendation to `ACE-Step 1.5 2B DiT` and replaced the memory boundary.[11]
2. **High — AMD R9600 availability was understated.** The official R9600 page explicitly says “Not available for purchase,” stronger than the prior “availability not proven” caveat. Corrected the current/announced tier and all availability language.[26][27]
3. **High — four compact-model memory bands lacked source-level support.** Qwen3 4B, Ornith 9B, Qwen3-ASR 0.6B, and Qwen3-Embedding 0.6B had precise planning ranges not supplied by their cited official cards. Removed those pseudo-precise floors; retained only publisher-stated values and required target-runtime testing.[4][5][10][12]
4. **Medium — mode-switch write semantics lacked a direct registered source.** The handler proves authorization, preflight, sequential `StopOp`, and allocation deletion, but `device_mode.go` directly proves the share-mode annotation write. Added Approved source `[44]` and corrected the lifecycle wording: allocation clearing is immediate and does not wait for app stop completion.[32][33][44]
5. **Medium — registry quality statistics were wrong.** There are two local repositories, not three; Olares docs are inside the Olares repository. Updated totals to 60 evaluated / 44 Approved / 16 Dropped and corrected concentration metrics.
6. **Medium — Standard G2 source diversity was not met.** The registry has one source type (`official`), while Standard requires at least two. Added an explicit fail marker to the registry and downgraded workflow-compliance confidence in the report.

## P7 trace verification

### Models

- **Exactly nine families:** Gemma 4, Qwen3, Ornith 1.0, FLUX.2, Wan2.2, Hunyuan3D 2.1, Qwen3-ASR, ACE-Step 1.5, Qwen3-Embedding. Count is 9; no excluded model is counted.[1][4][5][6][7][8][10][11][12]
- **Gemma 4:** Google records release on 2026-03-31 and 12B Unified on 2026-06-03; E4B supports text/image/audio plus video-as-frames, reasoning, function calling, local checkpoints, and Apache 2.0 weights.[1][2][3]
- **DeepSeek V4 / MiniMax M3:** both have downloadable weights and local-serving instructions. V4-Flash is 284B total/13B active; V4-Pro is 1.6T/49B active and the DSpark example uses one 4×GB300 node. M3 is ~428B/~23B active with 1M context. Exclusion is correctly based on conservative single-GPU fit, not release or API status.[13][14][15][16]
- **Hunyuan3D 2.1:** official repository states ~10GB shape, ~21GB texture, ~29GB combined. Its community license excludes EU/UK/South Korea, imposes use/notice restrictions, and requires separate permission above the stated scale threshold; `bespoke` is accurate.[8][9]
- **Wan2.2 TI2V-5B:** official single-GPU 720p command requires at least 24GB and already uses model offload, dtype conversion, and T5 CPU placement. `≥24GB` is a boundary, not a comfort claim.[7]

### Enterprise dGPU

- Intel B70/B65/B60/B50 are all on the B-Series page; B70/B65 were unveiled on 2026-03-25, with B70 available that day and B65 scheduled for mid-April. A60/A50 ordering pages say retired and discontinued.[17][18][19][20]
- NVIDIA’s live desktop catalog lists Blackwell 6000/5000/4500/4000/2000 and separately lists Ada/Ampere. RTX PRO 6000 Server Edition is passive; Workstation and Max-Q Workstation are distinct.[21][22][23]
- AMD separates R9000/RDNA 4 from W7000/RDNA 3. R9700 is current; R9600 is announced/cataloged but explicitly unavailable for purchase. W7900/W7800 are valid older-generation references.[24][25][26][27][28]

### Olares manifests and allocation semantics

- Exactly six audited Manifests exist: llama.cpp, vLLM, SGLang, Ollama, ComfyUI, Xinference.[34][35][36][37][38][39]
- llama.cpp/vLLM/SGLang/Ollama are `templateOnly` Engine Base charts with CPU/NVIDIA/GB10 and amd64/arm64; ComfyUI has NVIDIA/GB10 and amd64/arm64; Xinference has NVIDIA amd64 only. No common compatibility badge is valid.[34][35][36][37][38][39]
- OpenVINO appears as an application backend, not a canonical compute mode.[40][43]
- Exact chips: `nvidia` supports TimeSlice/MemorySlice/Exclusive and defaults TimeSlice; `nvidia-gb10`, `intel`, `amd`, `moore-soc` support MemorySlice/Exclusive and default MemorySlice; `apple-m`, `intel-gpu`, `amd-gpu` are Exclusive-only; CPU is MemorySlice-only but is not an accelerator chip.[31][32][43]
- Switching is admin-only. Unsupported modes fail, unchanged mode is a no-op, all bound apps are preflighted before mutation, blocked apps abort the change, then each app receives `StopOp`, allocations/HAMi bindings are cleared immediately, and the node share-mode annotation is updated. The sequence is not transactionally rolled back and requires later resume/rebinding.[30][32][33][44]

## Quality-gate result

- G1 task notes: pass.
- G2 source count/domains/official share/concentration: pass; source-type diversity: **fail**.
- G3 report length, confidence markers, contrary explanations, citation density: pass after correction.
- G4 factual traceability: pass after removing unsupported memory bands and correcting ACE-Step/R9600.
- G5 citation validity: pass for `[1]`–`[44]`; no Dropped source reappears.
- P6 found six issues: 0 critical, 3 high, 3 medium.

## END
