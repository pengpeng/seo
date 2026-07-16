---
task_id: official-models
role: Slide 21 官方模型发布与本地可运行性核验员
status: complete
sources_found: 16
---

## Sources
[1] Gemma 4 model card | https://ai.google.dev/gemma/docs/core/model_card_4 | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[2] Gemma 4 model overview and inference memory requirements | https://ai.google.dev/gemma/docs/core | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[3] Gemma releases | https://ai.google.dev/gemma/docs/releases | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[4] Qwen3: Think Deeper, Act Faster | https://qwenlm.github.io/blog/qwen3/ | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[5] Ornith-1.0-9B model card and official GGUF | https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B | Source-Type: official | As Of: 2026-07-15 | Authority: 9/10
[6] FLUX.2 [klein] 4B model card | https://huggingface.co/black-forest-labs/FLUX.2-klein-4B | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[7] Wan2.2-TI2V-5B model card | https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[8] Hunyuan3D-2.1 repository | https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1 | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[9] Hunyuan3D-2.1 license | https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/blob/main/LICENSE | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[10] Qwen3-ASR-0.6B model card | https://huggingface.co/Qwen/Qwen3-ASR-0.6B | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[11] ACE-Step 1.5 installation and model guide | https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md | Source-Type: official | As Of: 2026-07-15 | Authority: 9/10
[12] Qwen3-Embedding-0.6B model card | https://huggingface.co/Qwen/Qwen3-Embedding-0.6B | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[13] DeepSeek-V4-Flash model card | https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/README.md | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[14] DeepSeek-V4-Pro-DSpark deployment card | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[15] MiniMax-M3 model card | https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/README.md | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[16] MiniMax-M3 license | https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10

## Findings
1. **Gemma 4 is real and released, not a placeholder**: Google’s release log records E2B/E4B/26B-A4B/31B on 2026-03-31 and 12B Unified on 2026-06-03; the official card lists Apache 2.0 open weights, text/image/audio input on E2B/E4B/12B, reasoning, function calling, and local-oriented checkpoints including GGUF.[1][2][3]
2. The strongest compact first row is **Qwen3-4B** for general text/reasoning (Apache 2.0), **Ornith-1.0-9B** for tool-using agentic coding (MIT; official GGUF), and **Gemma 4 E4B** for image/audio/video understanding plus text output (Apache 2.0); this separates roles instead of showing three oversized flagships.[1][2][4][5]
3. The generation row can be **FLUX.2 [klein] 4B** for image generation/editing (Apache 2.0, official ~13GB VRAM), **Wan2.2-TI2V-5B** for 720p text/image-to-video (Apache 2.0, official ≥24GB with offload), and **Hunyuan3D-2.1** for image-to-3D shape/PBR texture (released weights and training code; custom community license).[6][7][8][9]
4. The utility/audio row can be **Qwen3-ASR-0.6B** (Apache 2.0; streaming/offline ASR across 52 languages and dialects), **ACE-Step 1.5** (MIT; standard local path under 4GB VRAM, 4B XL variants ≥12GB), and **Qwen3-Embedding-0.6B** (Apache 2.0; 32K context, 1024-dimensional multilingual embeddings).[10][11][12]
5. Eight recommended families use permissive Apache 2.0 or MIT terms; **Hunyuan3D-2.1 is open-weight/source-available rather than OSI-style open source**, because its community license has territorial, use, notice, and scale conditions.[1][4][5][6][7][9][10][11][12]
6. Hardware labels must be treated as practical planning boundaries, not promises: compact LLM/ASR/embedding estimates include runtime and moderate-context headroom, while image/video/3D figures follow publisher guidance; long contexts, high resolution, batching, and simultaneous shape+paint can materially raise memory.[2][6][7][8][10][11]
7. **Exclude DeepSeek V4 from the 3×3 grid, but not because it is unreleased or closed**: official MIT weights exist; even the smaller Flash checkpoint is 284B total/13B active and Pro is 1.6T/49B active, while the publisher’s Pro example uses a 4×GB300 node, so the family represents datacenter-local deployment rather than a conservative single-consumer-GPU example.[13][14]
8. **Exclude MiniMax M3 for the same hardware-fit reason**: official weights and local-serving instructions exist, but the model is ~428B total/~23B active with 1M context and uses the restrictive MiniMax Community License; its official serving guidance is not a compact single-GPU path.[15][16]
9. The exact nine-family shortlist is therefore **Gemma 4, Qwen3, Ornith 1.0 / FLUX.2, Wan2.2, Hunyuan3D 2.1 / Qwen3-ASR, ACE-Step 1.5, Qwen3-Embedding**; every named variant has a publisher-controlled model card or repository available by 2026-07-15.[1][4][5][6][7][8][10][11][12]

## Deep Read Notes
### Source [1][2][3]: Google Gemma 4 official documentation
Key data: Release log dates Gemma 4 to 2026-03-31 and the 12B Unified addition to 2026-06-03; E4B supports text/image/audio input, 128K context, configurable reasoning, and function calling.
Key insight: Google explicitly labels the weights Apache 2.0 and publishes Q4_0 loading memory of about 4.5GB for E4B, resolving both existence and local-fit questions without relying on third-party reporting.
Useful for: Multimodal grid cell, Gemma 4 fact correction, openness and memory boundary.

### Source [13][14]: DeepSeek V4 official model and deployment cards
Key data: V4-Flash is 284B total/13B active; V4-Pro is 1.6T total/49B active; both have 1M context and MIT weights, while the documented Pro-DSpark serving example uses 4×GB300.
Key insight: “Open-weight and locally deployable” does not mean “appropriate for a local-AI appliance slide”; total resident weights and serving topology remain the controlling constraints for MoE models.
Useful for: Accurate exclusion rationale and correction of any claim that V4 is merely API-only or unreleased.

### Source [15][16]: MiniMax M3 official model card and license
Key data: M3 is ~428B total/~23B active with native text/image/video multimodality and 1M context; weights can be downloaded and served with SGLang, vLLM, Transformers, or KTransformers.
Key insight: M3 is genuinely released and local-deployable at server/workstation scale, but its size and custom commercial/attribution conditions make it a poor conservative 3×3 showcase choice.
Useful for: MiniMax M3 exclusion, openness taxonomy, and avoiding the false “not released” rationale.

## Gaps / contrary evidence
- The compact LLM hardware bands below are conservative estimates from parameter count, official weight size/quantization, and moderate context; only Gemma 4, FLUX.2, Wan2.2, Hunyuan3D, and ACE-Step publish sufficiently direct memory guidance for their recommended variants.[2][5][6][7][8][11]
- Hunyuan3D-2.1’s official default figures are about 10GB for shape, 21GB for texture, and 29GB for both together; calling it “8–16GB” would only describe shape generation or unofficial offload/quantization, not the full default pipeline.[8]
- Wan2.2-TI2V-5B is single-consumer-GPU runnable only at the high end: its own recipe says at least 24GB VRAM and relies on model/T5 offload and dtype conversion; this is a boundary case for a 24GB card, not an 8–12GB example.[7]
- DeepSeek V4 and MiniMax M3 contradict a simplistic exclusion rule based on “not local”: both publish downloadable weights and local deployment instructions. They are excluded solely from this consumer-oriented grid because the smallest released variants remain hundreds of billions of resident parameters.[13][15]
- “Open” is not uniform: Apache 2.0/MIT families permit broad reuse, while Hunyuan3D and MiniMax M3 are open-weight under bespoke community terms; slide copy should say **Open & open-weight models**, not imply all nine meet one legal definition.[9][16]

## Slide recommendation
Use this exact 3×3 grid; show the family prominently and the variant/hardware line as small secondary text.

| Row | Family · smallest practical variant | Role | Weight/license status | Rough local hardware boundary |
|---|---|---|---|---|
| 1 | **Qwen3 · 4B** | Text + reasoning | Open weights/source ecosystem · Apache 2.0 | Q4: **6–8GB VRAM** or **8–16GB system RAM**; shorten context on smaller devices |
| 1 | **Ornith 1.0 · 9B** | Agentic coding + tool use | Open weights · MIT; official Q4_K_M GGUF is 5.63GB | **8–12GB VRAM** or **16GB+ RAM**; very long context needs more |
| 1 | **Gemma 4 · E4B** | Multimodal understanding + reasoning | Open weights · Apache 2.0 | Official load: Q4 ~4.5GB, 8-bit ~8.9GB; plan **8–12GB VRAM** |
| 2 | **FLUX.2 · klein 4B** | Image generation + editing | Open weights/reference code · Apache 2.0 | Officially **~13GB VRAM**; plan a **16GB GPU** |
| 2 | **Wan2.2 · TI2V-5B** | Text/image-to-video | Open weights/code · Apache 2.0 | Officially **≥24GB VRAM** with offload; 24GB is the practical floor |
| 2 | **Hunyuan3D · 2.1** | Image-to-3D + PBR texturing | Weights + training code · Tencent community license | Shape **~10GB**; texture **~21GB**; full default workflow **~29GB** |
| 3 | **Qwen3-ASR · 0.6B** | Speech recognition | Open weights/toolkit · Apache 2.0 | Plan **~4GB VRAM** or CPU with adequate RAM; batching/aligner adds memory |
| 3 | **ACE-Step · 1.5 standard** | Music generation | Open weights/code · MIT | Officially **<4GB VRAM** for standard path; plan **4–6GB** |
| 3 | **Qwen3-Embedding · 0.6B** | Local RAG embeddings | Open weights · Apache 2.0 | Plan **2–4GB VRAM** or ordinary CPU/RAM |

Footer note: **Hardware bands are rough inference boundaries; context, resolution, batching, quantization and offload change memory use. DeepSeek V4 and MiniMax M3 are released open-weight models, but are omitted because their smallest variants are datacenter/workstation scale rather than conservative single-GPU local examples.**

## END
