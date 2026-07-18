# Olares Heterogeneous Accelerator Management

> Intel collaboration deck, Slide 8. English slide copy.

---

## Slide copy

### Title

**Unifies Heterogeneous AI Compute** (`Unifies` highlighted in blue)

One stack discovers, integrates, schedules, shares and observes accelerators—while applications stay independent from hardware.

### Upper half · one continuous architecture

**Accelerated compute | Accelerator resources | Application allocation | Models & AI Runtimes**

| Accelerated compute · 22% | Olares OS · 51% | Models & AI Runtimes · 27% |
|----------------|-----------------|--------------------------|
| **Discrete GPU**<br>Intel Arc Pro B70 · B65 · B60 · B50<br>NVIDIA Consumer: RTX 5090 · RTX 5080<br>RTX 4090 · RTX 3090<br>NVIDIA Workstation: RTX PRO 6000 · 5000 Blackwell<br>NVIDIA Data center: B200 · H200<br>AMD Radeon AI PRO R9700 · R9600<br><br>**SoC · unified memory**<br>Intel Core Ultra Series 1 · Meteor Lake<br>Series 2 · Lunar Lake + Arrow Lake<br>Series 3 · Panther Lake<br>NVIDIA GB10 Grace Blackwell<br>AMD Ryzen AI Max+ 395 · Ryzen AI Max 390 · Ryzen AI Max 385<br>Apple M3 Ultra · M4 Pro · M4 Max · M5 Pro · M5 Max | **Accelerator resources · left**<br>*Hardware-facing abstraction*<br>01 **Backend enablement.** Enable OpenVINO, CUDA or ROCm for each accelerator.<br>02 **Schedulable devices.** Expose devices through vendor plugins as Kubernetes resources.<br>03 **Unified resource contract.** Normalize labels, scheduling and injection behind one app contract.<br>04 **Continuous observability.** Observe utilization and device health through Prometheus.<br><br>**Application allocation · right**<br>*Software-facing abstraction*<br>01 **Mode-aware packages.** Give each accelerator mode its own image and resource envelope.<br>02 **Install & launch selection.** Choose single-card, multi-card or multi-node resources at install or launch.<br>03 **Automatic resource management.** Keep apps running best-effort and scale resources when capacity runs short.<br>04 **User-friendly control.** Complete every operation in the UI and receive timely feedback. | **Models · 3×5**<br>Gemma 4 · Qwen3 · Ornith 1.0 · FLUX.2 · Wan 2.2 · Hunyuan3D 2.1 · Qwen3-ASR · ACE-Step 1.5 · BGE-M3 · Qwen3-TTS · Baidu OCR · Tencent Hy-MT2 · Z-Image · Ideogram 4 · MiniCPM-o 4.5<br><br>**AI runtimes · 3×3**<br>llama.cpp · vLLM · SGLang · Ollama · LocalAI · Xinference · KoboldCpp · Speaches · ComfyUI |

### Lower half · two comment boxes

| Accelerated compute + Accelerator resources | Application allocation + Models & AI Runtimes |
|----------------------------------|-------------------------------------------|
| **One lifecycle, composable across every accelerator.**<br><br>**01 · Manage accelerator lifecycle.**<br>**One interface.** Olares abstracts the whole lifecycle—from host driver installation and device discovery to runtime setup, scheduling, binding, monitoring and fault eviction.<br>**Module-local integration.** A new device implements the lifecycle interface inside its own module, instead of scattering device-specific changes across the system.<br><br>**02 · Compose resources.**<br>**Any topology.** Compose one resource, multiple instances, mixed resource types, cross-node capacity or an external eGPU.<br>**Two-layer binding.** Developers declare resources in software; users choose and allocate them through the system.<br>**Placement-independent apps.** The app contract stays stable from one device to multi-GPU or same-architecture pools. | **Three allocation modes—transparent to apps, with no code changes.**<br><br>**Time slicing · 50%.** Apps take turns using the full GPU, making it ideal for sequential workflows where each model may consume most of its memory. Album example: LLM lyrics → ACE-Step 1.5 XL music → Z-Image cover. Without Olares, users must stop models, release and re-bind the GPU between stages—and repeat this for every track. Time slicing rotates the GPU automatically, so the album feels like one continuous workflow.<br>Chips: `NVIDIA dGPU only`<br><br>**Memory slicing · upper right.** Why the name: VRAM is split into fixed quotas so apps run concurrently. Best for controlled resident apps such as ComfyUI, Speaches or model servers.<br>Chips: `Intel CPU` `Intel GPU` `NVIDIA dGPU` `GB10`<br><br>**Exclusive · lower right.** Why the name: one app gets the whole accelerator and no other app can bind. Best for rendering and gaming.<br>Chips: `All modes` |

---

## Working notes

- Use one continuous upper architecture and two large lower comment boxes.
- Keep the slide at roughly 45.5 / 54.5. Remove the lower column gap so the right comment box starts directly beneath Application allocation.
- Keep the headline and subtitle focused on Olares OS capabilities; do not enumerate chip vendors or models in the title area.
- Set the upper architecture to 324px: a 36px heading band and 288px content area. The increase uses the design system's 16px spacing unit. Size each outer group from its content; the left and right dividers do not need to align.
- Follow the `4 / 8 / 12 / 16px` spacing scale in [`ppt/design-system.md`](/Users/pengpeng/seo/ppt/design-system.md); use the permitted 6px exception between title and subtitle. Keep Models at 3×5 and AI runtimes at 3×3.
- Keep the four upper stages adjacent without circular connector arrows.
- Run both Olares OS columns 01 → 04 from top to bottom as the capability/component list. The lower-left box carries developer value only—two points: managing the full accelerator lifecycle and composing resources freely—and never repeats any upper component name (OpenVINO/CUDA/plugin/Prometheus).
- Keep OpenVINO with CUDA and ROCm in the lowest driver/runtime enablement layer.
- Show Intel's SoC timeline as Core Ultra Series 1–3 without separate SKU examples.
- All nine AI runtime cards have Olares Market manifests, but they do not share one compatibility matrix; see references for KoboldCpp's chart version range.
- Use one shared Grid for both columns; the four groups use natural-height `auto` rows, and each row follows a subheading-plus-one-sentence pattern on shared baselines.
- The four Application allocation rows cover dedicated images and resource envelopes, single-card/multi-card/multi-node selection at install or launch, automatic resource management, and complete UI control with feedback.
- Remove both blue comment kickers; keep only the black headings.
- Split the lower-right box 50/50: Time slicing owns the left half and tells the album workflow; Memory slicing sits upper-right and Exclusive lower-right.
- Do not show Agent & Software on this slide; defer that architecture to the next slide.
- The left comment box spans Accelerated compute + Accelerator resources; the right box spans Application allocation + Models & AI Runtimes.
- Use 11–11.5px for narrative copy; keep models, labels, chips and secondary parameters at 10.5px, never below the design-system minimum.
- Use icons from [`ppt/assets/slide21-icons/`](/Users/pengpeng/seo/ppt/assets/slide21-icons); source and trademark notes are in its `manifest.json`.
- Visually emphasize only the Olares middle layer. Keep models, software and hardware neutral and low-saturation.
- Preserve `Today / Next`: the target hardware matrix is not a claim of equal current support maturity.
- Group chips by vendor; show chip / accelerator SKU names only, with no capacities or system names. The verified hardware, model, runtime and allocation list is in [`research/local-open-models-and-runtimes-2026.md`](/Users/pengpeng/seo/research/local-open-models-and-runtimes-2026.md).
- `1×1 → 1×N → N×N` describes accelerator topology growth; current cross-node maturity is strongest for same-architecture clusters and NVIDIA, while automatic AMD64 / ARM64 pooling remains Next.
- HAMi supplies registration, sharing and scheduling for supported devices; Olares supplies host integration, the common resource contract, image selection and lifecycle management.
- Treat eGPU as a supported device form factor. Runtime physical hot-plug depends on the vendor driver, device plugin and live-workload device lifecycle.
- Main-slide chips: Time slicing uses `NVIDIA dGPU only`; Memory slicing shows the selected subset `Intel CPU`, `Intel GPU`, `NVIDIA dGPU`, `GB10`; Exclusive uses `All modes`. Keep the full code support matrix in references.
- Switching allocation mode stops bound apps and clears allocations; apps must then resume and re-bind.
- Current code supports install-time auto-selection plus binding and reallocation before resume or launch; the slide presents automatic scaling as product vision, not as a current code-level implementation claim.
- Full implementation evidence and external wording boundaries are in [references.md](./references.md).
