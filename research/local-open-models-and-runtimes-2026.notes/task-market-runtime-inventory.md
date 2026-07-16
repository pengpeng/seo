# Task: Olares Market runtime inventory

AS_OF: 2026-07-15  
Scope: Olares Market apps plausibly presented as an AI inference runtime or model-serving system. “Market evidence” means a local chart/manifest exists in the audited `beclab/apps` checkout; it does not prove installability on the current Olares release.

## Sources

Local sources are public upstream/Olares code checkouts, accessible locally:

- [L1] Olares Market catalog index, secondary internal index, AS_OF 2026-07-15: `/Users/pengpeng/seo/directions/market/apps.md`.
- [L2] Existing Slide 21 research, secondary synthesis, 2026-07-15: `/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.md`.
- [L3] llama.cpp manifest, official Olares Apps code, `b1627726`, 2026-07-01: `/Users/pengpeng/terminus-apps/llamacppllmbasev3/OlaresManifest.yaml`.
- [L4] vLLM manifest, official Olares Apps code, `3a1d673f`, 2026-07-01: `/Users/pengpeng/terminus-apps/vllmllmbasev3/OlaresManifest.yaml`.
- [L5] SGLang manifest, official Olares Apps code, `9ac06ebc`, 2026-07-01: `/Users/pengpeng/terminus-apps/sglangllmbasev3/OlaresManifest.yaml`.
- [L6] Ollama manifest, official Olares Apps code, `79ee6aea`, 2026-07-02: `/Users/pengpeng/terminus-apps/ollamallmbasev3/OlaresManifest.yaml`.
- [L7] Xinference manifest, official Olares Apps code, `9c96e4d0`, 2026-06-29: `/Users/pengpeng/terminus-apps/xinferencev3/OlaresManifest.yaml`.
- [L8] ComfyUI manifest, official Olares Apps code, `418feb2d`, 2026-06-29: `/Users/pengpeng/terminus-apps/comfyuisharev3/OlaresManifest.yaml`.
- [L9] LocalAI manifest, official Olares Apps code, `ad8fac97`, 2026-07-02: `/Users/pengpeng/terminus-apps/localai/OlaresManifest.yaml`.
- [L10] OpenLLM manifest, official Olares Apps code, `c66ca707`, 2026-06-25: `/Users/pengpeng/terminus-apps/openllm/OlaresManifest.yaml`.
- [L11] KoboldCpp manifest, official Olares Apps code, `ee2581c8`, 2026-07-01: `/Users/pengpeng/terminus-apps/koboldcpp/OlaresManifest.yaml`.
- [L12] Speaches manifest, official Olares Apps code, `763828ee`, 2026-06-29: `/Users/pengpeng/terminus-apps/speachesv3/OlaresManifest.yaml`.
- [L13] Fish Speech manifest, official Olares Apps code, `e403d9ee`, 2026-06-29: `/Users/pengpeng/terminus-apps/fishspeechv3/OlaresManifest.yaml`.
- [L14] OpenedAI Speech manifest, official Olares Apps code, `3dfacc0a`, 2026-06-29: `/Users/pengpeng/terminus-apps/openedaispeechv3/OlaresManifest.yaml`.
- [L15] Whisper API manifest, official Olares Apps code, `ae9121aa`, 2026-06-29: `/Users/pengpeng/terminus-apps/whisperservicev3/OlaresManifest.yaml`.
- [L16] TensorZero manifest, official Olares Apps code, `c66ca707`, 2026-06-25: `/Users/pengpeng/terminus-apps/tensorzero/OlaresManifest.yaml`.
- [L17] LiteLLM manifest, official Olares Apps code, `c66ca707`, 2026-06-25: `/Users/pengpeng/terminus-apps/litellm/OlaresManifest.yaml`.
- [L18] Bifrost manifest, official Olares Apps code, `c66ca707`, 2026-06-25: `/Users/pengpeng/terminus-apps/bifrost/OlaresManifest.yaml`.
- [L19] KubeRay manifest, official Olares Apps code, `c66ca707`, 2026-06-25: `/Users/pengpeng/terminus-apps/ray/OlaresManifest.yaml`.
- [L20] Icon inventory, local design asset index, AS_OF 2026-07-15: `/Users/pengpeng/seo/ppt/assets/olares-market-icons/manifest.json` and sibling image files.
- Catalog checkout: `/Users/pengpeng/terminus-apps`, HEAD `bad4b060590c97d0d5be55b1b6d116ac2af2efb0`, committed 2026-07-03.

Web sources are public:

- [W1] GitHub repository metadata API for the 19 upstream repositories named by manifests plus GPUStack and BentoML; `official` repository metadata, live 2026-07-15, high authority for archived/push state, public. Examples: https://api.github.com/repos/ollama/ollama, https://api.github.com/repos/bentoml/OpenLLM, https://api.github.com/repos/gpustack/gpustack.
- [W2] “The local AI inference runtime landscape,” RunLocalAI, `secondary-industry`, May 2026, medium authority, public: https://www.runlocalai.co/maps/inference-runtimes-2026.
- [W3] GPUStack architecture, `official`, accessed 2026-07-15, high authority, public: https://docs.gpustack.ai/latest/architecture/.
- [W4] GPUStack accelerator requirements, `official`, accessed 2026-07-15, high authority, public: https://docs.gpustack.ai/latest/installation/requirements/.
- [W5] LM Studio headless/llmster documentation, `official`, accessed 2026-07-15, high authority, public: https://lmstudio.ai/docs/developer/core/headless.
- [W6] OpenLLM repository/README, BentoML, `official`, accessed 2026-07-15, high authority, public: https://github.com/bentoml/OpenLLM.
- [W7] “Local LLM Stack Comparison,” AI Competence, `secondary-industry`, reviewed 2026-06-13, medium authority, public: https://aicompetence.org/local-llm-stack-comparison/.

## Candidate matrix

| Candidate | Category / true runtime? | Market evidence and manifest | Current manifest hardware / arch | Upstream maintenance at AS_OF | Icon | Include / exclude reason |
|---|---|---|---|---|---|---|
| llama.cpp | True portable inference engine/server | Present; Engine Base template [L3] | `cpu`, `nvidia`, `nvidia-gb10`; amd64/arm64 | Active; upstream pushed 2026-07-15 [W1] | `llamacpp.png` | **Core include.** Distinct CPU/edge/GGUF role; independent landscape calls it the portable bedrock [W2]. |
| vLLM | True high-throughput model server | Present; Engine Base template [L4] | `cpu`, `nvidia`, `nvidia-gb10`; amd64/arm64 | Active; pushed 2026-07-15 [W1] | `vllm.png` | **Core include.** Production shared-GPU serving role; note chart declarations are narrower than upstream hardware support [W2][W7]. |
| SGLang | True high-performance inference runtime/server | Present; Engine Base template [L5] | `cpu`, `nvidia`, `nvidia-gb10`; amd64/arm64 | Active; pushed 2026-07-15 [W1] | `sglang.png` | **Core include.** Strong agent/prefix-caching role [W2][W7]. |
| Ollama | True local model runner and API daemon | Present; Engine Base template [L6] | `cpu`, `nvidia`, `nvidia-gb10`; amd64/arm64 | Active; pushed 2026-07-15 [W1] | `ollama.png` | **Core include.** Best consumer/developer model-library experience; overlaps llama.cpp internally but is a distinct product layer [W2]. |
| Xinference | True multi-model serving platform | Present; shared app [L7] | `nvidia` only; amd64 only; 4–22 GiB declared GPU range | Active; pushed 2026-07-15 [W1] | `xinference.png` | **Core include.** Multi-modal/distributed serving platform; do not imply CPU/ARM from upstream prose because this chart does not declare them. |
| LocalAI | True multi-backend, multi-modal inference server | Present [L1][L9] | `nvidia` only; amd64 only; 2–16 GiB GPU declaration | Active; pushed 2026-07-15 [W1] | `localai.png` | **Shortlist include.** Strongest seventh general-purpose Market runtime: OpenAI-compatible, LLM/image/audio/embedding backends. Independent category check calls it a multi-modal multiplexer [W2]. |
| OpenLLM | True LLM serving platform built around BentoML | Present [L10] | amd64; legacy `requiredGpu: 10Gi`/`limitedGpu: 16Gi`, but no current `spec.accelerator` mode list | Active repository; pushed 2026-07-13 [W1][W6] | `openllm.png` | **Conditional include.** Real server, but chart `versionName: 0.3.7` and legacy resource schema require install validation before Slide promotion. |
| KoboldCpp | True GGUF inference engine plus bundled UI | Present [L1][L11] | amd64; legacy templated 10–24 GiB GPU envelope, no current accelerator list; dependency `<1.12.6` | Active; pushed 2026-07-15 [W1] | `koboldcpp.png` | **Conditional include.** Real multi-modal local engine, but current manifest explicitly conflicts with Olares 1.12.6+ and is v2/legacy-shaped. |
| Speaches | True modality-specific STT/TTS model server | Present [L1][L12] | `cpu`, `nvidia`, `nvidia-gb10`; amd64/arm64; NVIDIA request 8–16 GiB | Active; pushed 2026-07-15 [W1] | `speaches.png` | **Specialist include.** Strong audio-runtime candidate; not a general LLM runtime. |
| Fish Speech | TTS inference application/server, model-specific | Present [L1][L13] | amd64; no `spec.accelerator` declaration despite CUDA 12.9 image/prose | Active but lower cadence; pushed 2026-06-09 [W1] | `fishspeech.png` | **Specialist reserve.** Genuine TTS inference, but model-specific and manifest does not expose a current accelerator mode. |
| OpenedAI Speech | TTS server, modality-specific | Present [L1][L14] | amd64/arm64; no accelerator list despite prose claiming CPU Piper and NVIDIA XTTS modes | **Archived** upstream; last push 2025-02-02 [W1] | `openedai.png` | **Exclude.** Genuine server, but archived upstream and manifest/prose hardware declarations diverge. |
| Whisper API | ASR/diarization inference API, model-specific | Present [L1][L15] | amd64; no accelerator list, while upgrade prose says NVIDIA-only | Active fork; pushed 2026-07-13 [W1] | No exact `whisper-api` icon; `fasterwhisper.png` exists | **Specialist reserve.** Useful model service, but narrow scope and hardware declaration mismatch. |
| ComfyUI | Inference workflow UI/backend, not a general model server | Present; one of current Slide six [L8] | `nvidia`, `nvidia-gb10`; amd64/arm64; no CPU mode in manifest | Active; pushed 2026-07-15 [W1] | `comfyui.png` | **Keep only with label “workflow runtime/software.”** It executes image/video/audio/3D graphs, but is not peer-equivalent to vLLM/Ollama. |
| TensorZero | AI gateway/observability/evaluation/optimization stack, not an inference engine | Present [L16] | amd64/arm64; CPU/RAM only, no accelerator | **Archived** repository as of 2026-07-15 [W1] | `tensorzero.png` | **Exclude from runtime row.** Routes and evaluates inference supplied by other providers/servers. Archived state adds maintenance risk. |
| LiteLLM | AI gateway/proxy, not an inference engine | Present [L1][L17] | amd64/arm64; no accelerator | Active; pushed 2026-07-15 [W1] | `litellm.png` | **Exclude from runtime row.** Unified API, routing, cost, guardrails and load balancing; it does not execute model kernels. |
| Bifrost | AI gateway/router, not an inference engine | Present [L1][L18] | amd64/arm64; no accelerator | Active; pushed 2026-07-15 [W1] | `bifrost.png` | **Exclude from runtime row.** Connects providers and self-hosted vLLM/Ollama/SGLang endpoints rather than serving weights itself. |
| KubeRay / Ray | Distributed compute and serving orchestrator, not a packaged inference engine here | Present [L19] | amd64; no accelerator declaration; dependency `<1.12.6` | Active; pushed 2026-07-15 [W1] | `kuberay.png` | **Exclude from runtime row.** Ray Serve can orchestrate model servers, but this Olares chart is a generic Ray dashboard/cluster and appears incompatible with 1.12.6+ [W2]. |
| GPUStack | Model-serving control plane/orchestrator over vLLM/SGLang/etc.; not a kernel runtime | **No chart/manifest found** in audited checkout; absent from [L1] | No Olares declaration | Active; pushed 2026-07-15 [W1] | `gpustack.png` | **Exclude as Market claim; future packaging candidate.** Official architecture says inference servers are separate backends [W3]; broad NVIDIA/AMD/NPU support is upstream only [W4]. |
| BentoML | General model-serving framework/platform; can host inference services | **No BentoML chart/manifest found**; only its OpenLLM product is present [L10] | No Olares declaration | Active; pushed 2026-07-14 [W1] | `bentoml.png` | **Exclude as Market claim; future packaging candidate.** Do not infer BentoML Market presence from OpenLLM’s developer field. |
| LM Studio / llmster | True local/headless inference server, proprietary product wrapping runtimes | **No chart/manifest found**; absent from [L1] | No Olares declaration | Current official headless service docs [W5] | `lmstudio.png` | **Exclude as Market claim.** Technically a valid server candidate, but icon presence alone is not catalog presence. |

Recommended shortlist pool:

1. **Stable core:** llama.cpp, vLLM, SGLang, Ollama, Xinference.
2. **Best general-purpose expansion:** LocalAI.
3. **Conditional after install smoke test:** OpenLLM, KoboldCpp.
4. **Specialist runtime expansion:** Speaches; reserve Fish Speech and Whisper API for an “audio model services” row.
5. **Separate visual category:** ComfyUI as workflow runtime/software.
6. **Do not place in inference-runtime row:** LiteLLM, Bifrost, TensorZero, KubeRay/GPUStack, BentoML-without-chart, LM Studio-without-chart, OpenedAI Speech.

## Findings

1. The defensible Market pool is larger than the five-brand index: LocalAI, OpenLLM, KoboldCpp and Speaches all have local manifests and execute inference, although only LocalAI is ready to recommend without an obvious manifest-version caveat [L1][L9][L10][L11][L12].
2. The current five Engine Base/server charts do not share one compatibility badge: four Engine Bases declare CPU + NVIDIA + GB10 on amd64/arm64, while Xinference declares NVIDIA on amd64 only [L3][L4][L5][L6][L7].
3. LocalAI is the strongest Slide expansion because it is a true multi-backend, multi-modal OpenAI-compatible inference server, is actively maintained, and has an exact Market icon [L9][L20][W1][W2].
4. OpenLLM is not abandoned upstream, contrary to a likely stale assumption, but its Olares chart still exposes legacy GPU fields and an old packaged version; upstream activity does not make the chart current [L10][W1][W6].
5. KoboldCpp is a real inference engine rather than merely a role-play frontend, but the audited chart requires Olares `<1.12.6`, making current compatibility doubtful [L11].
6. ComfyUI belongs on the Slide only if the row is named broadly enough to include workflow software; it is not category-equivalent to a general OpenAI-compatible LLM server [L8].
7. LiteLLM, Bifrost and TensorZero are gateways/control stacks: they route, observe or optimize calls but do not themselves supply the model-execution backend [L16][L17][L18].
8. GPUStack is an orchestrator whose own architecture names vLLM, SGLang, MindIE and VoxBox as the actual inference servers; no Olares chart was found, so it cannot be described as currently packaged [W3][W4].
9. LM Studio’s `llmster` is now a legitimate headless inference service, but the audited Olares catalog has no manifest; the local icon is design inventory, not Market evidence [L20][W5].
10. Maintenance risk is material: OpenedAI Speech and TensorZero are archived upstream, while most core runtimes had same-day repository activity; an app card can outlive its upstream maintenance state [W1].

## Deep Read Notes

### Olares manifests

- The four v3 Engine Base templates—llama.cpp, vLLM, SGLang and Ollama—share Olares integration traits: template-only installation, multi-install support, a shared model cache, `LLMGatewaySupported`, and explicit CPU/NVIDIA/GB10 modes. This is stronger evidence of runtime-product integration than a generic app that merely contains a GPU resource field [L3][L4][L5][L6].
- Xinference is a shared serving platform, not an Engine Base template. Its manifest directly exposes the service on port 9997 and supports language, speech and multimodal models, but its current Olares accelerator declaration is NVIDIA/amd64 only [L7].
- LocalAI is functionally broader than the five text-centric brands: its manifest identifies llama.cpp, Transformers and vLLM backends plus image, audio, embedding, reranking and vision APIs. The current chart nevertheless declares only NVIDIA amd64, despite upstream’s broader theoretical support [L9].
- The legacy/stale-shape manifests are the main audit hazard. OpenLLM uses old `requiredGpu` fields without `spec.accelerator`; KoboldCpp uses a v2 templated manifest and constrains Olares to `<1.12.6`; KubeRay carries the same upper bound [L10][L11][L19].
- Several modality apps have prose-to-schema mismatches: Fish Speech describes a CUDA image but has no accelerator declaration; OpenedAI Speech describes CPU/NVIDIA modes but has no accelerator list; Whisper API says NVIDIA-only in upgrade prose but likewise lacks an accelerator list [L13][L14][L15].

### Independent category countercheck

- RunLocalAI separates desktop runners (Ollama, llama.cpp, LM Studio), high-throughput servers (vLLM, SGLang, LocalAI), distributed systems/orchestrators (Ray Serve), and frontends. This supports keeping gateway/UI/orchestration products out of a narrow “inference runtime” row [W2].
- AI Competence independently differentiates llama.cpp’s CPU/edge role, Ollama’s local-development role, and vLLM/SGLang’s production-serving roles. It also warns that runtime selection is workload-specific rather than a universal benchmark ranking [W7].
- GPUStack’s official architecture explicitly places its server, scheduler, controllers, workers and gateway above separate inference servers. It is a serving system/control plane, but counting it alongside vLLM as another engine would double-count layers [W3].
- LM Studio’s official documentation now describes `llmster` as a standalone Linux/server daemon with an OpenAI-compatible server and JIT model loading. Its exclusion here is solely lack of Olares Market evidence, not lack of runtime capability [W5].

## Gaps and contrary claims

- **Market presence does not equal current compatibility.** A manifest may be present but pinned to an older Olares range, use legacy GPU fields, omit accelerator modes, package an old upstream version, or depend on an image that has not been smoke-tested against current drivers.
- The audit proves chart existence at checkout `bad4b06`, not that every chart is visible in every Market channel, installable on Olares 1.12.6/1.12.7, or healthy on each declared architecture.
- Manifest declarations are narrower than upstream capability. For example, LocalAI upstream can run without a GPU and vLLM supports more hardware families upstream, but the current Olares charts must not inherit those claims automatically [L4][L9][W2][W7].
- Conversely, prose is not a substitute for schema: Fish Speech, OpenedAI Speech and Whisper API describe CUDA/NVIDIA behavior without a current accelerator list [L13][L14][L15].
- Icon availability is not Market evidence. BentoML, GPUStack and LM Studio have local icon files but no chart/manifest in the audited catalog [L20].
- “Active repository” is a coarse maintenance signal, not proof of release quality. OpenLLM had recent pushes but its latest Olares package still appears materially behind upstream; Fish Speech’s lower push cadence does not by itself mean abandonment [L10][L13][W1].
- GitHub archive state is strong contrary evidence for future maintenance, but an archived upstream repository can still have a functioning immutable package. OpenedAI Speech and TensorZero therefore require product-owner decisions rather than an automatic claim that installed instances are broken [L14][L16][W1].
- No install, API, model-load, or GPU smoke tests were run. Before Slide publication, test LocalAI, OpenLLM, KoboldCpp and Speaches on the target Olares release and at least one declared accelerator mode.
