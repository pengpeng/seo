# Task A2 — eGPU interconnect, NVIDIA eGPU on Linux, Intel TB4 CPUs & mini-PC/NAS

> AS_OF = 2026-07-14. Distilled, sourced research note. Fact-type numbers (prices, specs) drift — reverify at official pages before publishing. `[unverified]` = single-source / claim I could not independently confirm.

---

## Sources

**Topic 1 — eGPU interconnect for LLM inference / TB4 vs OCuLink**
- [S1] CraftRigs — *USB4 eGPU for Local LLMs: Does It Actually Work?* https://craftrigs.com/guides/usb4-egpu-local-llms/
- [S2] GMICloud — *What Factors Influence Inference Speed in Machine Learning* https://www.gmicloud.ai/en/blog/what-factors-influence-inference-speed
- [S3] Hacker News thread — memory-bandwidth vs bus-bandwidth for token gen. https://news.ycombinator.com/item?id=44219515
- [S4] Local AI Master — *Thunderbolt vs OCuLink for eGPU AI: Real Benchmarks (2026)* https://localaimaster.com/blog/thunderbolt-vs-oculink-ai
- [S5] Local AI Master — *eGPU for Local AI: External GPU Benchmarks (2026)* https://localaimaster.com/blog/egpu-local-ai-benchmarks
- [S6] MakeUseOf — *I tested my eGPU with OCuLink and Thunderbolt, and it wasn't close* https://www.makeuseof.com/i-tested-my-egpu-with-oculink-and-thunderbolt-and-it-wasnt-close/
- [S7] XDA — *OCuLink eGPU docks make Thunderbolt feel like a bottleneck* https://www.xda-developers.com/oculink-egpus-make-thunderbolt-feel-like-bottleneck/
- [S8] XDA — *I expected Thunderbolt 5 to replace OCuLink for eGPU setups, but it didn't* https://www.xda-developers.com/why-thunderbolt-5-didnt-replace-oculink-for-egpu/
- [S9] TechSpot — *Thunderbolt alternative OCuLink tested for eGPUs, RTX 4090 benchmarked* https://www.techspot.com/news/101698-thunderbolt-alternative-oculink-tested-egpus-nvidia-rtx-4090.html

**Topic 2 — NVIDIA eGPU pain on Linux**
- [S10] NVIDIA/open-gpu-kernel-modules Issue #842 — *add support of thunderbolt hotplug* https://github.com/NVIDIA/open-gpu-kernel-modules/issues/842
- [S11] Issue #894 — *RmCheckForExternalGpu does not always identify an eGPU correctly* https://github.com/NVIDIA/open-gpu-kernel-modules/issues/894
- [S12] PR #981 — *Improve Thunderbolt eGPU detection and stability* https://github.com/NVIDIA/open-gpu-kernel-modules/pull/981
- [S13] Issue #979 — *RTX 5080 via TB5 eGPU: Hard lock on CUDA operations* https://github.com/NVIDIA/open-gpu-kernel-modules/issues/979
- [S14] PR #1109 — *make Resizable BAR resize failure non-fatal, skip proactively on Thunderbolt* https://github.com/NVIDIA/open-gpu-kernel-modules/pull/1109

**Topic 3 — Intel CPUs with TB4 & mini-PC/NAS products**
- [S15] NotebookCheck — Intel Core i3-N305 (Alder Lake-N) specs. https://www.notebookcheck.net/Intel-Core-i3-N305-Processor-Benchmarks-and-Specs.678904.0.html
- [S16] gagniard.org — *Building a N305 based NAS* (real lspci dump). https://gagniard.org/gilles/posts/2025/02/building-a-n305-based-nas/
- [S17] Intel — *Core Ultra 200H/200U Series (Arrow Lake) Overview* PDF (I/O connectivity table). https://cdrdv2.intel.com/v1/dl/getContent/830252
- [S18] Framework Community — *Discrete Thunderbolt 5? Intel new Core Ultra Chips are confusing* https://community.frame.work/t/discrete-thunderbolt-5-intel-new-core-ultra-chips-are-confusing-am-i-alone/62910
- [S19] Linux-kernel patch thread — *PCI: Detect and trust built-in Thunderbolt chips* (integrated vs discrete TB, Alder Lake). https://lists.openwall.net/linux-kernel/2024/10/30/26
- [S20] Dasharo issue #1638 — *PCIe over Thunderbolt not working* (Alder Lake port falls back to USB-only). https://github.com/Dasharo/dasharo-issues/issues/1638
- [S21] Minisforum M1 Pro-125H product page (Core Ultra 5 125H, USB4 + OCuLink). https://store.minisforum.com/products/minisforum-m1-pro-125h-mini-pc
- [S22] Minisforum UH125 Pro (Core Ultra 5 125H, OCuLink 64Gbps). https://www.minisforum.com/products/minisforum-uh125-pro
- [S23] Minisforum MS-01 workstation (i9-13900H/12900H/i5-12600H, 2× USB4). https://store.minisforum.com/products/minisforum-ms-01-workstation
- [S24] AOOSTAR GEM12+ (Ryzen 7 8845HS, OCuLink + dual USB4) + review. https://aoostar.com/products/aoostar-gem12-amd-r7-pro-8845hs-mini-pc / https://minipc-mothership.com/gem12.html
- [S25] Minisforum N5 Pro AI NAS (Ryzen AI 9 HX PRO 370, OCuLink). https://store.minisforum.com/products/minisforum-n5-pro-ai-nas

---

## Findings (≤12)

1. **For LLM token generation the host↔GPU link is NOT the bottleneck — on-card VRAM bandwidth is.** Every forward pass reads the *entire* weight set from VRAM; per-token traffic over the bus is tiny (a few hundred KB of activations in, a probability vector out). Compute/VRAM-read dominates >99% of the time, so once weights are resident the PCIe/TB link is nearly idle. [S1][S3][S5]

2. **The link bandwidth mainly costs you MODEL LOAD time, not steady-state tok/s.** Loading a large model into VRAM is the one heavy transfer. Local AI Master's "time to first prompt ready" for a 70B model: internal PCIe 4.0 x16 ≈ **1.9 s**, OCuLink x4 ≈ **5.4 s**, TB5 ≈ **6.8 s**, TB4 ≈ **13.2 s**, USB4 40Gbps ≈ **13.6 s** — i.e. TB4 is ~**5–7×** slower to load than internal, but you pay it once per model swap. [S4] A separate bench: 8B Q4 load ≈ **12–13 s on TB4 vs ~2 s internal**. [S5]

3. **Quantified steady-state inference penalty vs internal x16 (model fully resident):** OCuLink ≈ **2–3%**, Thunderbolt 4 / USB4 ≈ **10–17%** slower tok/s. This is far below the gaming penalty because inference barely touches the bus. [S4][S5]

4. **Gaming penalty is much larger** because games stream textures/geometry over the bus every frame. TB4/USB4 eGPU gaming loss is commonly **~25–40%** vs internal (and worse in RT/high-fps titles); OCuLink (PCIe 4.0 x4, 64 Gbps) recovers most of it. This is exactly why "eGPU advice based on FPS benchmarks misleads" LLM users. [S4][S5][S9]

5. **TB4 vs OCuLink — bandwidth & real measured throughput.** TB4/USB4 = 40 Gbps nominal but PCIe-tunneled with controller overhead → real host→device only **~2.4–2.9 GB/s**. OCuLink = direct PCIe 4.0 x4 = 64 Gbps → measured **~6.0–7.4 GB/s** (XDA measured 2.42 GB/s USB4 → 6.70 GB/s OCuLink in 3DMark on the same GPU). TB5 = 80 Gbps nominal, ~6 GB/s measured. [S4][S7]

6. **Hot-plug is the key ergonomic trade-off.** Thunderbolt 4/5 supports hot-plug (plug/unplug live); OCuLink does **NOT** — you must power the machine off before connect/disconnect, the connector latches and is not designed for frequent cycling. Every OCuLink mini-PC vendor prints this warning explicitly. [S6][S8][S21][S22][S24]

7. **OCuLink scales better with strong GPUs and is more stable**; TechSpot's RTX 4090 over OCuLink on a Core Ultra 5 125H laptop: ~23% loss on internal display in Time Spy but **~0–5%** with an external display; RTX 4070 Ti ~10% loss. MakeUseOf found OCuLink also had cleaner sleep/wake vs TB crashes. [S9][S6]

8. **NVIDIA eGPU on Linux is officially unsupported and genuinely painful.** The proprietary driver handles TB3 eGPU hot-plug reasonably, but the **open kernel modules** hit "GPU has fallen off the bus" (Xid 79) on unplug/suspend, lock a CPU core at 100%, and require a reboot. Hot-plug "works on Windows" but not cleanly on Linux open driver. [S10][S11]

9. **Root cause is TB4/TB5 detection, not just hot-plug.** NVIDIA's driver only recognizes **Thunderbolt 3** bridges as eGPU enclosures; TB4/TB5/USB4 bridge device-IDs aren't in the approved list, so `PDB_PROP_GPU_IS_EXTERNAL_GPU` never gets set → wrong (too-short) timeouts, wrong power-management (D3cold), and **hard system lock during CUDA/sustained load** (e.g. RTX 5080/5090 on TB5). Community patches add an `NVreg_ForceExternalGpu` param and 4× timeouts to work around it. [S12][S13]

10. **Resizable-BAR on Thunderbolt is a second failure mode:** TB/USB4 hot-plug bridges expose a small prefetchable MMIO window that can't fit modern NVIDIA GPUs' GiB-scale BAR1; the resize fails and **the eGPU silently never appears in `nvidia-smi`** until a patch makes ReBAR failure non-fatal / skips it on TB. A maintainer's own summary: "TB on Linux is a bit rough … for now." [S14]

11. **N305 (Alder Lake-N) does NOT have usable Thunderbolt 4** — see dedicated section below. Intel's TB4 *is* integrated on the mainstream mobile lines: **12th/13th Gen "H/U/P" (Tiger/Alder/Raptor Lake), Core Ultra Series 1 (Meteor Lake), and Core Ultra Series 2 "200H/200U" (Arrow Lake) all carry 4× integrated TB4**; Arrow Lake HX carries 2×. TB5 on Arrow Lake still needs a **discrete** add-on controller. Desktop TB4 comes via the chipset (e.g. Z890, optional per board). [S17][S18]

12. **Representative Intel-based mini-PCs/NAS that expose an eGPU link (prices ~mid-2026, barebone unless noted):** see product table. Practical pattern: OCuLink is showing up on prosumer mini-PCs/AI-NAS as the *performance* eGPU path (64 Gbps, no hot-plug); TB4/USB4 is the *convenient* path (40 Gbps, hot-plug). Note several headline "AI NAS with OCuLink" boxes (Minisforum N5 Pro, AOOSTAR GEM12+) are **AMD**, not Intel. [S21][S22][S23][S24][S25]

---

## Deep Read Notes

### The N305 / Thunderbolt-4 question (explicit clarification)

**Short answer: The Intel Core i3-N305 (Alder Lake-N, 8×Gracemont E-cores, 15W) does NOT provide real, usable Thunderbolt 4.** Alder Lake-N has **no integrated Thunderbolt host controller** — NotebookCheck's spec sheet states plainly "Wi-Fi 6E and Bluetooth 5.2 are partly integrated (but no Thunderbolt). External chips can be connected via PCIe Gen3 x9 (via the PCH)." [S15]

**Why the confusion exists:** a real N305 NAS `lspci` dump shows a line:
`00:0d.0 USB controller: Intel Corporation Alder Lake-N Thunderbolt 4 USB Controller`. [S16]
This is **misleading naming inherited from the shared Alder Lake IP block** — it is the integrated **xHCI/USB controller** (class 0c-03, USB controller), *not* a Thunderbolt PCIe host bridge (NHI) with a working eGPU tunnel. On these ports:
- There is **no PCIe/DP tunneling exposed** by default → a plugged TB/USB4 dock enumerates as **USB-only**, `boltctl list` returns nothing, no new PCIe devices appear. This exact behavior is documented on an Alder Lake board where the port "falls back to USB mode" unless special firmware (IoT FSP) is used. [S20]
- The Linux kernel's own TB-trust patch series notes Intel integrated TB root ports have a `usb4-host-interface` ACPI property / known PCI IDs; where that's absent and only a bare "TB4 USB Controller" shows up, it's not a tunneled integrated-TB path. [S19]

**Bottom line for slides:** Do NOT claim "N305 has Thunderbolt 4 for eGPU." Correct framing: *N305 exposes USB (and the SoC's USB-C IP is labelled "Thunderbolt 4 USB Controller" in PCI naming), but Alder Lake-N has no integrated Thunderbolt host — no PCIe-tunneled TB4, so no TB4 eGPU.* If an N-series box needs eGPU, it's via **OCuLink or an M.2→PCIe adapter**, not TB4. `[verified across 3 sources: S15 spec, S16 real dump, S19/S20 behavior]`

### Which low-power Intel chips actually ship in NAS / mini-PCs
- **N100 (4×Gracemont, 6W)** and **N305 (8×Gracemont, 15W)** — the workhorse budget NAS/mini-PC chips. No TB4. PCIe Gen3 only (~x9 total via PCH). Great for Jellyfin transcode (QuickSync AV1 decode), weak for GPU-attached AI. [S15][S16]
- **Core Ultra 5 125H (Meteor Lake, 14C/18T, Arc iGPU)** — the current sweet spot for eGPU-capable mini-PCs; integrated TB4 **and** vendors add OCuLink. [S17][S21][S22]
- **Core Ultra 7/9 255H/285H (Arrow Lake-H)** — 16C, integrated 4× TB4, discrete TB5 optional; higher-end AI mini-PC tier. [S17]
- **i9-13900H / i5-12600H (Raptor/Alder Lake-H)** — still common in workstation mini-PCs like MS-01 (2× USB4). [S23]

### Representative products (verify prices before publishing)

| Product | CPU | eGPU link | Hot-plug? | Price (barebone, ~2026-07) | Notes |
|---|---|---|---|---|---|
| Minisforum M1 Pro-125H | Intel Core Ultra 5 125H | **OCuLink (PCIe4 x4)** + 2× USB4 | OCuLink no / USB4 yes | ~$367 (sale) – $459; ~$689–767 configured | OCuLink shares one M.2 slot [S21] |
| Minisforum UH125 Pro | Intel Core Ultra 5 125H | **OCuLink 64Gbps** (pairs w/ DEG1 dock) | No (OCuLink) | ~$385 | Explicitly warns OCuLink not hot-swappable [S22] |
| Minisforum MS-01 | Intel i9-13900H / i5-12600H | **2× USB4 (40Gbps)** + PCIe4.0 x16 (half-height) | USB4 yes | ~$419 (i5) / ~$655–679 (i9) | eGPU via USB4 or internal half-height card [S23] |
| AOOSTAR GEM12+ | AMD Ryzen 7 (PRO) 8845HS | **OCuLink 64Gbps** + 2× USB4 | No (OCuLink) | from ~$359 (barebone); ~$409–549 configured | AMD, not Intel; reviewer hit near-desktop 3DMark w/ RTX 4080S [S24] |
| Minisforum N5 Pro AI NAS | AMD Ryzen AI 9 HX PRO 370 | **OCuLink** + PCIe x16 slot | No (OCuLink) | ~$899–1,019 (barebone/128G) | AMD AI-NAS; markets "eGPU via OCuLink → 3× Stable Diffusion" [S25] |
| AOOSTAR EG02 (dock, not host) | — (TB5 + OCuLink eGPU dock) | TB5 / OCuLink | — | ~$219 | Reference for the enclosure side [S24 collection] |

*(Intel-only, TB4/OCuLink hosts in the $400–1600 band: M1 Pro-125H, UH125 Pro, MS-01. The two OCuLink "AI NAS" headliners in this class are AMD — worth flagging so slides don't imply Intel.)*

---

## Gaps & caveats

- **Local AI Master [S4][S5] is the main quantitative source for the "2–3% OCuLink / 10–17% TB4" inference-penalty and the 70B load-time table.** These are plausible and internally consistent, but I could not cross-verify the exact numbers against a second independent LLM-specific benchmark; treat specific percentages as `[single-source, directionally reliable]`. The *qualitative* claim (link ≈ load time, not steady-state tok/s) is corroborated by S1/S2/S3.
- Gaming-loss "~25–40%" is a synthesized typical range from S4/S5/S9; individual titles vary widely (RT titles worse, esports titles negligible). `[range, not a single measured figure]`
- TB5 real-world numbers are still thin (few shipping TB5 PCs/enclosures as of AS_OF); S8 argues OCuLink may still edge TB5 in RT despite equal paper specs — `[unverified/early]`.
- Prices are volatile promo/barebone figures pulled from vendor + Newegg pages on/near 2026-07-14; reverify. Some listings were "sold out."
- **CONTRARIAN CLAIM — cases where the eGPU link *does* materially affect inference:**
  1. **Prompt prefill / long context.** Prefill processes the whole prompt at once → larger activation tensors cross the bus; CraftRigs reports **~30–40% slower on 2K+ token prompts and ~40–50% on 8K+ / frequent reloads** over USB4, vs only 10–20% on short prompts. So "link doesn't matter" holds for short-prompt chat, not for long-context / RAG / agentic prefill-heavy workloads. [S1]
  2. **Model swapping / multi-model agentic pipelines** re-pay the load cost repeatedly → OCuLink's 5–20× faster load is a real, felt advantage. [S4]
  3. **Multi-GPU / tensor- or pipeline-parallel** inference where a model is split across cards: inter-GPU activation/KV traffic crosses the interconnect every layer/token, so bus bandwidth (and especially latency) re-enters as a real bottleneck — an eGPU link is a poor substitute for NVLink/x16 here. `[well-established generally; specific eGPU multi-GPU numbers unverified]`
  4. **Models that exceed VRAM** (CPU/RAM offload) constantly shuttle weights over the bus → link bandwidth becomes first-order. [S1][S4]
