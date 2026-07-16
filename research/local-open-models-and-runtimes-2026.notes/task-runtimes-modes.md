---
task_id: runtimes-modes
role: Olares 本地 AI runtime、workflow 与 accelerator mode 审计员
status: complete
sources_found: 15
---

## Sources
[1] Olares One: Manage accelerator resources | /Users/pengpeng/Olares/docs/one/gpu.md | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 9/10
[2] Olares manual: Manage accelerator resources | /Users/pengpeng/Olares/docs/manual/olares/settings/gpu-resource.md | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 9/10
[3] Compute support-type wire constants | /Users/pengpeng/Olares/framework/app-service/pkg/compute/types.go | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 10/10
[4] Available support types and defaults | /Users/pengpeng/Olares/framework/app-service/pkg/compute/store.go | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 10/10
[5] Device mode-switch API and app-stop flow | /Users/pengpeng/Olares/framework/app-service/pkg/apiserver/handler_compute_resources.go | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 10/10
[6] llama.cpp Engine Base manifest | /Users/pengpeng/terminus-apps/llamacppllmbasev3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 10/10
[7] vLLM Engine Base manifest | /Users/pengpeng/terminus-apps/vllmllmbasev3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 10/10
[8] SGLang Engine Base manifest | /Users/pengpeng/terminus-apps/sglangllmbasev3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 10/10
[9] Ollama Engine Base manifest | /Users/pengpeng/terminus-apps/ollamallmbasev3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 10/10
[10] ComfyUI shared app manifest | /Users/pengpeng/terminus-apps/comfyuisharev3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 10/10
[11] Xinference shared app manifest | /Users/pengpeng/terminus-apps/xinferencev3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 10/10
[12] EmbeddingGemma OpenVINO/ONNX backend manifest | /Users/pengpeng/terminus-apps/embeddinggemmav3/OlaresManifest.yaml | Source-Type: official | As Of: 2026-07-03 (terminus-apps `bad4b06`) | Authority: 8/10
[13] CLI accelerator support-type display labels | /Users/pengpeng/Olares/cli/cmd/ctl/settings/compute/common.go | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 9/10
[14] Chinese Olares One GPU mode guide | /Users/pengpeng/Olares/docs/zh/one/gpu.md | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 8/10
[15] Canonical Olares compute modes | /Users/pengpeng/Olares/framework/app-service/pkg/utils/gpu_types.go | Source-Type: official | As Of: 2026-07-10 (Olares `6f2b93e`) | Authority: 10/10

## Findings
- Olares packages all six requested products at these exact manifests: `llamacppllmbasev3/OlaresManifest.yaml`, `vllmllmbasev3/OlaresManifest.yaml`, `sglangllmbasev3/OlaresManifest.yaml`, `ollamallmbasev3/OlaresManifest.yaml`, `comfyuisharev3/OlaresManifest.yaml`, and `xinferencev3/OlaresManifest.yaml`; the first four are model-serving Engine Base templates, ComfyUI is workflow software, and Xinference is a shared model-serving platform.[6][7][8][9][10][11]
- The packaged accelerator matrix is not uniform: llama.cpp, vLLM, SGLang, and Ollama each declare `cpu` + `nvidia` + `nvidia-gb10` on `amd64`/`arm64`; ComfyUI declares `nvidia` + `nvidia-gb10` on `amd64`/`arm64` with no CPU mode; Xinference declares only `nvidia` and only `amd64`.[6][7][8][9][10][11]
- These manifest modes are the exact Olares-packaged chart coverage, not a claim about every backend supported by each upstream project; Slide 21 should therefore list the six products without attaching one shared hardware-support chip to the whole row.[6][7][8][9][10][11]
- User docs spell the three display terms **Time slicing**, **Memory slicing**, and **Exclusive**; backend enums are `TimeSlice`, `MemorySlice`, and `Exclusive`, while the CLI currently renders title-case **Time Slicing** and **Memory Slicing**, so the slide should follow the docs’ sentence-case wording.[1][2][3][13]
- `nvidia` is the only compute mode exposing TimeSlice, and it defaults to TimeSlice; Time slicing gives a workload the whole NVIDIA dGPU during its slice and applies the documented node-memory check using app memory plus dedicated VRAM against the 90% threshold.[1][2][4]
- MemorySlice is exposed by `nvidia`, `nvidia-gb10`, `intel`, `amd`, and `moore-soc`; GB10 and the integrated/unified-memory modes default to it, while CPU fallback is MemorySlice-only but is not an accelerator chip.[3][4]
- Exclusive is available for every accelerator compute mode: `nvidia`, `nvidia-gb10`, `intel`, `amd`, and `moore-soc` can switch to it, while `apple-m`, `intel-gpu`, and `amd-gpu` currently expose Exclusive only.[3][4]
- Mode switching is admin-only; an unchanged target is a no-op, unsupported choices are rejected, and a real switch first plans whether every bound app can stop, aborts without changing the mode if any app is blocked, otherwise stops apps, deletes allocations/HAMi bindings, writes the new share-mode annotation, and leaves apps requiring resume and re-binding.[2][5]
- OpenVINO must remain in the accelerator/backend layer beside CUDA and ROCm, not appear as a seventh application runtime: the audited app evidence uses OpenVINO IR as EmbeddingGemma’s `cpu` image backend, while the user-facing executable service remains IREmbeddingServer/EmbeddingGemma.[12]

## Deep Read Notes
### Source [4]: `compute/store.go`
Key data: `nvidia` → TimeSlice/MemorySlice/Exclusive; `nvidia-gb10|intel|amd|moore-soc` → MemorySlice/Exclusive; `cpu` → MemorySlice; all other accelerator modes → Exclusive.
Key insight: the first available type is the default, so only NVIDIA dGPU defaults to TimeSlice; unified-memory accelerators default to MemorySlice.
Useful for: exact support chips and default-mode wording.

### Source [5]: `handler_compute_resources.go`
Key data: the switch endpoint checks admin role and `availableSupportTypes`, preflights every bound app, returns `bound-apps-stop-blocked` before mutation when stopping is impossible, then stops apps, deletes allocations, and calls `SwitchDeviceMode`.
Key insight: mode change is a disruptive drain-and-rebind lifecycle, not live migration or automatic rebalancing.
Useful for: mode-switch callout and Today/Next boundary.

### Sources [6]–[11]: six packaged manifests
Key data: the four Engine Base manifests are `templateOnly: true` and support CPU/NVIDIA/GB10; ComfyUI is NVIDIA/GB10; Xinference is NVIDIA-only.
Key insight: “Olares-packaged” is well supported, but “runs on every Olares accelerator” is false for this six-product set.
Useful for: runtime row, exact source paths, and avoiding a misleading common compatibility badge.

## Gaps / contrary evidence
- The current English manual says AMD GPU/APU are “not covered in this version” and omits Intel/Moore from its resource-type table, while current app-service code exposes `amd`, `intel`, and `moore-soc` support types; present those chips as code-level mode support, not equal end-to-end product maturity.[2][4]
- The Chinese Olares One page calls Time slicing the default without limiting that statement to NVIDIA dGPU; code makes MemorySlice the default for GB10, Intel/AMD integrated accelerators, and Moore SoC.[4][14]
- CLI labels capitalize “Slicing,” unlike the current English docs; use docs wording on Slide 21 and reserve enum spellings for engineering notes.[1][2][3][13]
- The OpenVINO example is application-backend evidence, not proof that Olares core defines an `openvino` compute mode; no such mode exists in the audited canonical compute-mode list.[12][15]
- The switch handler preflights all apps before mutation, but the subsequent per-app stop/delete sequence is not visibly transactional; do not claim atomic rollback on mid-commit infrastructure failure.[5]

## Slide recommendations
- Change the right-side label to **AI runtimes & workflow software** and show exactly: **llama.cpp · vLLM · SGLang · Ollama · ComfyUI · Xinference**.
- Keep **OpenVINO** only in **Accelerator resources → Drivers & runtimes/backends**, beside **CUDA · ROCm**; do not duplicate it in the six-product row.
- Use these exact allocation chips:
  - **Time slicing** — `NVIDIA dGPU only`
  - **Memory slicing** — `NVIDIA dGPU · GB10 · Intel/AMD iGPU/APU · Moore SoC`
  - **Exclusive** — `All accelerator modes`; muted sub-chip: `Apple M · Intel/AMD dGPU: exclusive only`
- Use this mode-switch line: **Admin mode switch: stop bound apps → clear allocations → switch mode → resume & re-bind**.
- Do not add a common “CPU/NVIDIA/GB10” badge to all six products; if per-product chips are shown, use: four Engine Base products `CPU · NVIDIA · GB10`, ComfyUI `NVIDIA · GB10`, Xinference `NVIDIA (amd64)`.

## END
