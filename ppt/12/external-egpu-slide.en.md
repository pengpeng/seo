# Arc Pro B70 External GPU for AI NAS

> External collaboration PPT, slide 12 (form ①: external co-processor / eGPU · Intel NAS track). English content source for the HTML/Figma build. Sharp copy only; details live in Working notes.
> Data provenance: [references.md](./references.md) and [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md). Snapshot 2026-07-14, re-verify before publishing.

---

## Slide copy (what actually goes on the slide)

### Title
**Arc Pro B70 External GPU for AI NAS**
One external Arc Pro B70 turns a traditional NAS into a multi-purpose AI NAS—for Personal Agent, Audio, Smart Home and Private Workspace.

| Setup | VRAM / memory | Price (2026-07) | prefill pp t/s | decode tg t/s |
|-------|---------------|-----------------|-----------------------------|-----------------------------|
| **NAS + external Arc Pro B70 (AI NAS)**<br>Q4 · no MTP | **32GB discrete** | **+$1,100–1,300 on a NAS you own** · $1,600–2,000 new | ~615 · long-ctx stable | ~55–82 |
| AMD 395+ mini-PC<br>Q4 · no MTP | 128GB unified | ~$3,399 | ~900–1,270 · drops long-ctx | ~62–81 |
| Mac Studio M4 Max<br>4-bit · no MTP | 64GB unified | from $3,499 | ~1,100–1,370 | ~42–70 |
| **DGX Spark**<br>MXFP4 · llama.cpp · no MTP | **128GB unified** | **$4,699** | **~2,289** | **~63** |
| Mac Studio M3 Ultra<br>4-bit · no MTP | 96GB unified | $5,299 | ~1,640–2,620 | ~70–98 |
| Desktop RTX 5090<br>Q4_K_M · llama.cpp · no MTP | 32GB discrete | **~$4,329**<br>card only | **~2,892** | **~183** |
| NVIDIA DGX Spark<br>NVFP4 · vLLM · MTP | 128GB unified | **$4,699** | ~4,850–6,255 | ~85–112 |

### Right — Advantages

1. **Broad host coverage, near-native LLM speed**: OCuLink or Thunderbolt covers more NAS, mini-PC and CPU platforms; with weights resident in VRAM, steady-state inference is only ~2–3% below internal x16, far less than the 25–40% common in gaming eGPU workloads.
2. **Flexible upgrades, longer hardware life**: choose B60 / B70 by budget, move external compute across compatible hosts, then upgrade only the GPU module — reducing obsolescence risk.
3. **A lighter OEM product and supply chain**: keep GPU power, cooling, BOM and inventory outside the base NAS, without adding compute-tier SKUs.
4. **Four high-value workloads, one module**: **Personal Agent, Audio AI, Smart Home and Private Workspace**.
5. **More Arc Pro sales, a larger software ecosystem**: every AI NAS creates a B70 / B60 attach opportunity while expanding Intel inference software coverage and developer reach.
6. **A compelling price advantage**: ~$1,100–1,300 added to an existing NAS, or ~$1,600–2,000 new — well below the complete-system alternatives.

### Right — What needs work

1. **Prefill software upside remains untapped**: Personal Agents process long context every turn, so prefill sets time-to-first-token. B70 is still ~615 pp t/s, but the hardware ceiling has not been reached; XMX attention and the inference stack need further optimization.
2. **The price advantage is cyclical**: if unified-memory prices return to 2025 levels, the gap narrows; long-term value must come from reusing installed NAS hardware, local data and modular upgrades.

*Sources and benchmark conditions: [references.md](./references.md).*

---

## Working notes (NOT on the slide)

- **2026 RAM surge (off-slide)**: M4 Max $2,699→$3,499; M3 Ultra $3,999→$5,299; mainstream AMD 395+ ~$1,999→$3,399; B70 card $949→~$999. DRAM +93–98% and LPDDR5X +78–89%; GDDR6 moved much less. Keep this as spoken context, not a standalone visual block.
- **B70 / OEM hardware facts (off-slide)**: B70 32GB GDDR6 / 608 GB/s / 367 TOPS / PCIe 5.0; rated 160–290W TBP (Intel reference 230W), versus 60–250W consumer NAS PSUs and ~22–24 dB idle noise. The external dock owns GPU power and cooling; the NAS base unit does not absorb that envelope.
- **Benchmark scope**: all rows use Qwen3.6-35B-A3B, single-stream, 4-bit and no MTP; quantization and engine are labeled per row. DGX Spark and RTX 5090 use comparable llama.cpp pp512/tg128 results: ~2,289/62.61 and ~2,892/183 respectively. On the current B70 stack, enabling MTP is a regression (72–82→47–63).
- **DGX Spark optimized ceiling (de-emphasized final row)**: public NVFP4 + vLLM + MTP runs report ~4,850–6,255 pp2048/ctx_pp across 4K–32K context and ~85–112 tg t/s across prompts. Some tuned Atlas/DFlash configurations peak above 120 tg t/s, but they are not used as the table's normal range. A Q4_K_M+llama.cpp, no-MTP source separately reports ~70 tg t/s but no directly citable pp512.
- **Intel value**: every AI NAS creates a B70 / B60 attach opportunity while expanding Intel inference software coverage and developer reach. Olares owns the platform layer; XMX optimization remains Intel-controlled upside.
- **prefill honest bounds**: a Personal Agent processes system instructions, long history, memory, files and tool output every turn. Prefill sets time-to-first-token; decode only sets streaming speed after the answer begins. Prefix caching helps stable prefixes, but dynamic context keeps changing, so it cannot remove long-context prefill pressure. Short-prompt prefill Mac (~1.1–1.4K) ≈ AMD (~0.9–1.3K) > B70 (~615, llama.cpp); B70's is a software gap rather than a proven hardware ceiling, and XMX attention plus the inference stack retain clear optimization headroom. B70's prefill strength is long-context stability (411 @64K); AMD iGPU prefill explodes at long context (minutes @32K).
- **OCuLink vs Thunderbolt (slide only says "whichever the box has")**: steady-state LLM fine on both (link idle after weights load). OCuLink = direct PCIe 4.0 ×4 / 64Gbps, faster/cheaper; Thunderbolt = plug-and-play, no teardown. NVIDIA eGPU on Linux works but is painful (registry-key force, kernel params, patches) — internal note, not on slide.
- **$/GB NOT external**: B70 ~$30/GB vs NVIDIA $75/GB is true but may read as Intel pricing aggressively — keep off the slide, especially in front of Intel.
- **Olares full stack (script / Q&A only)**: auto driver detect + CUDA/oneAPI/ROCm; one-click local LLM/ComfyUI; Olares Market apps double as agent tools; Personal Agent; LarePass remote/VPN/identity; sandbox security.
