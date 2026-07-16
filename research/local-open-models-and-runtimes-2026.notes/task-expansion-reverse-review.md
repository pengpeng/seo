# Task: Expansion reverse review

## Reviewed claims

1. Show `Core Ultra Series 1–3` plus `X9 388H · X7 368H — Series 3 (Panther Lake)`.
2. Replace `SoC · Unified memory` with either `Shared system memory` or `Integrated CPU · GPU · NPU`.
3. Expand the Market software row from six to exactly nine items.

## Issues

1. **Critical — “exactly nine Market AI runtimes” is not supported as a current-installability claim.** The inventory proves manifest existence only. OpenLLM uses legacy GPU fields and packages upstream `0.3.7`; KoboldCpp explicitly requires Olares `<1.12.6`; no candidate received install, model-load, API, or accelerator smoke tests. This conflicts with the current Olares 1.12.6+ baseline. **Mitigation:** do not promote OpenLLM or KoboldCpp as currently installable until tested on the target release. Slide-safe wording: **`Market-packaged AI software · compatibility varies by app`**. If nine logos are mandatory, mark unverified entries **`Preview / validation pending`**, not as peers of the validated core.

2. **High — the number nine is cardinality-driven, not taxonomy-driven.** The inventory yields five stable engines/platforms, LocalAI, two conditional candidates, Speaches, and separately ComfyUI: ten names across different layers. Retaining the existing six and adding LocalAI, OpenLLM, and KoboldCpp reaches nine only by excluding the healthier v3 Speaches chart while including two caveated charts. **Mitigation:** select by role and validation status, not available slots. Preferred near-term set: the current six plus **LocalAI**; add Speaches only under a broader software label. Do not claim “exactly nine runtimes” until two more general-purpose candidates pass validation.

3. **High — the software row mixes non-peer categories.** ComfyUI is workflow software, Speaches is modality-specific serving, Ollama is a runner, and vLLM/SGLang are high-throughput servers. Nine equal logos under `AI runtimes` visually assert category equivalence. **Mitigation:** use **`AI runtimes & workflow software`** or split into **`Model serving`** and **`Workflow / modality services`**. Avoid a shared hardware badge because manifests expose different modes and architectures.

4. **High — `Core Ultra Series 1–3` can be read as Olares compatibility breadth.** Intel sources establish naming and silicon composition, but the Olares evidence establishes only a generic Intel iGPU allocation mode, not per-SKU validation across Meteor Lake, Lunar Lake, Arrow Lake, and Panther Lake. In an “Accelerated compute” column beneath a slide promising one hardware abstraction, the family line is likely to be interpreted as support. **Mitigation:** either show only the two current examples or qualify the breadth line. Slide-safe wording: **`Intel Core Ultra Series 1–3*`** / **`*platform family; app and SKU validation varies`**. Strongest guarded form: **`Core Ultra X9 388H · X7 368H (Panther Lake)`**.

5. **High — the two proposed taxonomy replacements are not interchangeable, and one is not family-wide.** `Shared system memory` describes memory behavior; `Integrated CPU · GPU · NPU` describes package components. The latter is false as a group-wide heading because GB10 has CPU/GPU but no NPU, while vendor terminology and exposure differ for Apple, AMD, and Intel. `Shared system memory` is safer than `Unified memory`, but still must not imply identical coherence, zero-copy behavior, bandwidth, or on-package memory. **Mitigation:** use **`Integrated compute`** with subtitle **`Shared system memory`**; optional micro-note: **`CPU/GPU/NPU mix varies`**. Do not use `Integrated CPU · GPU · NPU` as the heading for all four vendor rows.

6. **Medium — the Intel breadth line hides architecture and capability discontinuities.** Series 2 includes Lunar Lake and Arrow Lake, while memory packaging, NPU capability, iGPU class, and form factor vary materially; Series 1–3 is a naming range, not a homogeneous accelerator generation. **Mitigation:** keep `Panther Lake` attached only to X9 388H/X7 368H and avoid any shared performance or memory claim. Slide-safe wording: **`Core Ultra Series 1–3`** / **`Current examples: X9 388H · X7 368H (Panther Lake)`**.

7. **Medium — current report, slide, catalog index, and assets do not yet form one supporting state.** The report explicitly fixes six packaged products; the HTML and rendered slide show six; the runtime grid is hard-coded as 2×3; slide-specific software assets contain only the current six plus OpenVINO. LocalAI, OpenLLM, KoboldCpp, and Speaches icons exist only in the general Market icon directory. The Market index lists LocalAI, KoboldCpp, and Speaches but not OpenLLM. **Mitigation:** update the report’s evidence and caveats before changing the slide, define the exact nine, copy/normalize approved icons, and redesign rather than compress the 2×3 grid.

8. **Medium — evidence diversity is adequate for names, weak for experience claims, and highly time-sensitive.** Intel evidence is overwhelmingly vendor-controlled; it proves naming, launch state, and specifications but not Olares behavior. Runtime evidence combines manifests with only two secondary taxonomy checks and no independent install tests. Live Intel catalogs, Market channels, chart versions, and Olares compatibility ranges can change after the snapshot. **Mitigation:** preserve `AS_OF: 2026-07-15`, add target Olares version and catalog commit, and rerun Market visibility plus install smoke tests immediately before publication. Do not turn repository activity into a quality or compatibility claim.

## Source quality check

- **Intel naming/SKU existence:** strong; multiple Intel naming, ARK, launch, and architecture sources.
- **Intel/Olares compatibility:** insufficient; no per-SKU Olares or runtime validation.
- **Memory terminology:** strong for rejecting blanket `Unified memory`; only moderate for one cross-vendor replacement label.
- **Market chart presence:** strong at checkout `bad4b060590c97d0d5be55b1b6d116ac2af2efb0`.
- **Market visibility/current installability:** insufficient; no channel/API visibility check and no smoke tests.
- **Runtime taxonomy:** moderate; manifests plus independent landscape checks expose layer mismatch, but do not justify an exact count.
- **New web research:** none required; the supplied notes and local repository evidence were sufficient.

## Final guarded recommendation

Approve the Intel SKU update only with a compatibility qualifier. Replace `SoC · Unified memory` with **`Integrated compute · Shared system memory`**, not `Integrated CPU · GPU · NPU`. Reject the nine-runtime claim for publication now: the defensible immediate expansion is **seven packaged AI software products**—the current six plus LocalAI—while retaining **`AI runtimes & workflow software`** and per-app compatibility caveats. Reach nine only after two additional candidates pass current-release install and accelerator smoke tests.

## Traceability spot-check

1. **Series 1–3 is valid Intel naming breadth** → `task-intel-presentation-taxonomy.md` findings 1–3; Intel naming guide, Series 3 quick reference, ARK X9/X7.
2. **X9 388H and X7 368H are Panther Lake examples** → taxonomy note sources [2]–[7]; timeline finding 5.
3. **Series labels do not imply homogeneous architecture** → taxonomy finding 2; timeline findings 2–5 and gaps on Series 2/3 codenames.
4. **Blanket `Unified memory` is inaccurate** → timeline findings 8 and contrary claim; taxonomy findings 7–8.
5. **Generic Intel mode is not a per-SKU validation matrix** → taxonomy gaps, lines 92–95; current report sections 6–7 on code-level versus end-to-end support.
6. **Current report and slide support six, not nine** → report lines 102–121; HTML runtime list lines 265–274.
7. **LocalAI is the strongest immediate addition** → runtime inventory candidate matrix and findings 1–3; local manifest declares v3, Olares `>=1.12.6-0`, NVIDIA/amd64.
8. **OpenLLM and KoboldCpp are conditional** → runtime inventory findings 4–5 and gaps; local manifests show legacy GPU schema / `0.3.7` and `<1.12.6`, respectively.
9. **Chart presence is not installability** → runtime inventory scope, gaps, and finding 10; no smoke tests recorded.
10. **The nine-item row would mix layers** → runtime inventory findings 6–8 and independent category countercheck.
