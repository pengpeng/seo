# Task: Nine-runtime shortlist

AS_OF: 2026-07-15

## Sources

- [S1] Olares Market runtime inventory, secondary distilled audit, 2026-07-15, authority 8/10, local/public-code-derived: `/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.notes/task-market-runtime-inventory.md`.
- [S2] Olares Apps manifests for llama.cpp, vLLM, SGLang, Ollama, Xinference, LocalAI, OpenLLM, KoboldCpp, Speaches and ComfyUI, official code, checkout `bad4b060` dated 2026-07-03, authority 10/10, public/local: `/Users/pengpeng/terminus-apps/{llamacppllmbasev3,vllmllmbasev3,sglangllmbasev3,ollamallmbasev3,xinferencev3,localai,openllm,koboldcpp,speachesv3,comfyuisharev3}/OlaresManifest.yaml`.
- [S3] Olares Market icon inventory, official-derived design assets, accessed 2026-07-15, authority 8/10, local: `/Users/pengpeng/seo/ppt/assets/olares-market-icons/`; exact icons exist for all ten audited names.
- [S4] ggml-org, llama.cpp repository and server documentation, official, live/accessed 2026-07-15, authority 10/10, public: https://github.com/ggml-org/llama.cpp and https://github.com/ggml-org/llama.cpp/tree/master/tools/server.
- [S5] vLLM OpenAI-compatible server documentation, official, accessed 2026-07-15, authority 10/10, public: https://docs.vllm.ai/en/stable/serving/online_serving/openai_compatible_server/.
- [S6] SGLang repository/documentation, official, live/accessed 2026-07-15, authority 10/10, public: https://github.com/sgl-project/sglang and https://docs.sglang.ai/.
- [S7] Ollama API documentation and releases, official, accessed 2026-07-15; latest release `0.32.0` published 2026-07-11, authority 10/10, public: https://docs.ollama.com/api/introduction and https://github.com/ollama/ollama/releases/tag/v0.32.0.
- [S8] Xinference distributed-inference documentation and release `2.12.0`, official, accessed 2026-07-15/released 2026-07-04, authority 10/10, public: https://inference.readthedocs.io/en/latest/user_guide/distributed_inference.html and https://github.com/xorbitsai/inference/releases/tag/v2.12.0.
- [S9] LocalAI overview and release `4.7.1`, official, accessed 2026-07-15/released 2026-07-14, authority 10/10, public: https://localai.io/docs/overview/index.html and https://github.com/mudler/LocalAI/releases/tag/v4.7.1.
- [S10] BentoML OpenLLM repository and PyPI `0.3.7`, official, accessed 2026-07-15; repository last push 2026-06-29 and latest release `0.6.30` dated 2025-04-21, authority 9/10, public: https://github.com/bentoml/OpenLLM and https://pypi.org/project/openllm/0.3.7/.
- [S11] KoboldCpp repository/wiki, official, accessed 2026-07-15; latest release `1.116.1` dated 2026-06-27, authority 10/10, public: https://github.com/LostRuins/koboldcpp and https://github.com/LostRuins/koboldcpp/wiki.
- [S12] Speaches repository, official, accessed 2026-07-15; recent code activity 2026-06-15 and latest formal release `0.9.0-rc.3` dated 2025-12-27, authority 9/10, public: https://github.com/speaches-ai/speaches.
- [S13] ComfyUI official documentation, repository and release `0.27.0`, official, accessed 2026-07-15/released 2026-06-30, authority 10/10, public: https://docs.comfy.org/ and https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.27.0.

## Exact 3x3 recommendation

Use the broad heading **AI runtimes** and the footnote: **“Model servers plus generative workflow engines; package support varies by accelerator. *OpenLLM package requires validation.”**

**Row 1 — inference engines / production servers**

1. **llama.cpp** — portable GGUF engine and lightweight API server. Caveat: Olares packages continuous build `b9853`, while upstream had reached `b9999`; normal fast-release lag, not category risk [S2][S4].
2. **vLLM** — high-throughput OpenAI-compatible model server. Caveat: describe Olares coverage from its chart—CPU, NVIDIA and GB10—not from upstream’s broader hardware matrix [S2][S5].
3. **SGLang** — low-latency serving runtime for agentic, structured and prefix-heavy workloads. Caveat: Olares `0.5.14` is one patch behind upstream `0.5.15.post1`; chart coverage is CPU, NVIDIA and GB10 [S2][S6].

**Row 2 — approachable and multi-backend serving**

4. **Ollama** — developer-friendly local model runner and API daemon. Caveat: overlaps llama.cpp at the lower engine layer, but its model library, lifecycle and API make it a distinct product layer; Olares `0.31.1` trails upstream `0.32.0` slightly [S2][S7].
5. **LocalAI** — multi-backend, multi-modal OpenAI-compatible server. Caveat: upstream supports many hardware families, but this Olares chart declares NVIDIA/amd64 only; packaged `4.5.6` trails upstream `4.7.1` [S2][S9].
6. **Xinference** — multi-model serving platform with distributed-worker support. Caveat: its current Olares chart is NVIDIA/amd64 only and packages `2.10.0` versus upstream `2.12.0` [S2][S8].

**Row 3 — platform and modality specialists**

7. **OpenLLM*** — BentoML-based OpenAI-compatible LLM serving platform. Caveat: conditional selection only: the manifest says `0.3.7`, the deployment actually uses engine image `0.3.6`, it has legacy GPU resource fields, and upstream is `0.6.30`; current Olares is not excluded by its `>=1.10.1` dependency, but install/model/API smoke tests are required. Slide-safe card: **“OpenLLM*”** [S2][S10].
8. **Speaches** — OpenAI-compatible STT/TTS model server, adding genuine audio-runtime diversity. Caveat: it is not an LLM server; Olares has a current v3 chart with CPU/NVIDIA/GB10 modes, while upstream release cadence is slower than the core engines [S2][S12].
9. **ComfyUI** — node-based generative workflow inference engine for image, video, audio and 3D. Caveat: not a peer general-purpose model server; include only under broad **AI runtimes**, never under **LLM servers**. Its Olares chart is current-format and requires Olares `>=1.12.6` [S2][S13].

## Findings

1. The inventory’s exact nine is not the most defensible set: replace **KoboldCpp** with **ComfyUI** because KoboldCpp explicitly requires Olares `<1.12.6`, while ComfyUI has a current v3 chart, `>=1.12.6` dependency, active upstream and an official “inference engine” description [S2][S11][S13].
2. All recommended cards have verified Market manifests and exact local icons; icon presence is therefore a layout advantage, not the evidence of Market presence [S2][S3].
3. llama.cpp, vLLM, SGLang and Ollama form the strongest integration tier: each is a v3 Engine Base template with model-cache integration, CPU/NVIDIA/GB10 modes, amd64/arm64 and `LLMGatewaySupported` [S2].
4. Their apparent duplication is role-separable: llama.cpp is the portable GGUF bedrock, Ollama is the model-runner product layer, and vLLM/SGLang target high-throughput serving with different scheduling/caching strengths [S4][S5][S6][S7].
5. LocalAI and Xinference are broader serving platforms, but the slide must not inherit upstream hardware claims: their Olares charts currently narrow both to NVIDIA/amd64 [S2][S8][S9].
6. Speaches is category-accurate as a modality-specific model server and is the cleanest way to keep the 3×3 from becoming nine text-LLM logos [S2][S12].
7. ComfyUI should be kept: it materially connects the slide’s image/video/audio/3D models to executable local workflows, and official documentation calls it a node-based interface **and inference engine** [S13].
8. OpenLLM is the only selected card with a material freshness warning; recent repository activity does not cure the Olares package’s manifest/image mismatch or legacy resource schema [S2][S10].
9. Short names fit the card treatment without aliases; **llama.cpp**, **Xinference** and **OpenLLM*** are the longest useful labels, while “Engine Base” should remain metadata rather than card text [S2].
10. A stale chart must not receive the same implied readiness as the current v3 charts: Market presence proves catalog history, not installability, model loading or API health on Olares 1.12.6+ [S1][S2].

## Rejected alternatives

- **KoboldCpp** — true GGUF inference engine/server and actively maintained, but rejected because its Olares dependency is `>=1.12.3-0,<1.12.6`; showing it as a current equal would be less defensible than retaining ComfyUI [S2][S11].
- **Fish Speech** — real TTS inference application with a current Olares dependency, but model-specific, overlaps Speaches, and lacks a declared `spec.accelerator` list despite shipping a CUDA image [S1].
- **Whisper API** — real ASR/diarization service, but narrower than Speaches, requires gated pyannote models, and its prose says NVIDIA-only while no actual accelerator list is present [S1].
- **OpenedAI Speech** — genuine speech server, rejected for archived upstream and weaker manifest consistency [S1].
- **LiteLLM, Bifrost, TensorZero** — gateways, routing/observability or optimization layers; they do not execute model inference and fail the strict runtime/model-server test [S1].
- **KubeRay, GPUStack** — orchestration/control-plane layers rather than the packaged execution engine; GPUStack also lacks an audited Olares chart [S1].
- **BentoML, LM Studio/llmster** — technically valid serving products but no audited Olares Market manifest; icon files alone do not establish Market presence [S1][S3].

## Gaps and contrary claims

- **Argument for keeping ComfyUI:** “AI runtimes” is broader than “LLM servers”; ComfyUI executes local generative graphs, exposes an API/backend, has a fresh Olares integration, and gives the adjacent media-model cards an honest runtime path [S2][S13].
- **Argument against keeping ComfyUI:** if the section is intended to compare interchangeable OpenAI-compatible model endpoints, ComfyUI is layer- and API-incongruent; in that narrower framing it belongs in a separate **Workflow engines** row [S5][S13].
- **Argument against showing stale charts:** a logo grid visually asserts equal current availability. OpenLLM’s `0.3.7` metadata over a `0.3.6` engine image and KoboldCpp’s `<1.12.6` cap can turn “in Market” into a misleading “works on current Olares” claim [S2]. If the slide cannot carry the OpenLLM asterisk, do not show that card; use eight verified-current cards or rename/expand the category before substituting a model-specific service.
- No install, model-load, endpoint, GPU or multi-architecture smoke tests were run. The exact nine is a defensible editorial shortlist, not a compatibility certification [S1].
- Manifest freshness is uneven and independent of upstream health. Conversely, a recent chart commit can still repackage an old engine; both version lines and rendered images must be checked [S2][S10].
- The current Olares charts do not establish equal AMD/Intel/Apple support. Slide-wide accelerator badges would overstate what LocalAI, Xinference, ComfyUI and OpenLLM actually declare [S2].
