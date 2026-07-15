# Three Intel Hardware Paths for Local AI

> External collaboration PPT, slide 25 (Olares × Intel section transition). English content source for HTML.
> Sources: [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md), [Olares positioning](../../basic/olares.md), and [Olares One first-party benchmarks](../../directions/hardware/research/olares-one-benchmarks.md). Snapshot 2026-07; re-verify before publishing.

---

## Slide copy

### Title

**Three Intel Hardware Paths for Local AI**

Seven cloud-proven paid scenarios map to three Intel-centered product architectures: external accelerator, standalone SoC, and on-board accelerator.

### Three hardware paths

| Hardware path | Current configuration | Product form | Best-fit AI scenarios |
|---------------|-----------------------|--------------|-----------------------|
| **External accelerator** | Intel NAS / box + external **Arc Pro B70 32GB** | Turns a traditional NAS into a multi-purpose AI NAS | Personal Agent · Audio · Smart Home · Private Workspace |
| **Standalone SoC** | **Panther Lake** CPU + NPU + iGPU | AI Box with NAS and Windows VM capabilities | **Private Meeting AI: now** · Smart Home: next · Personal Agent: later |
| **On-board accelerator** | **Core Ultra 9 275HX + RTX 5090 Mobile 24GB** | **Olares One**—current flagship proof | Personal Agent · App Development · Audio · Image · Smart Home · AI Companion · Private Workspace |

---

## Working notes

- This is a transition slide. Do not repeat the B70 benchmarks, meeting-market evidence, Olares platform stack, or Olares One benchmark details.
- Olares One remains a compact proof point on this route map; it no longer requires a separate slide in the current external narrative.
- The third path is defined by a shared single-system power, thermal, acoustic, size and memory envelope for an on-board accelerator—not by accelerator vendor.
- RTX 5090 Mobile is the current Olares One implementation. Future Intel or other accelerators can enter this path if they meet the same board-level and software requirements.
- Arc Pro B70 is a 160–290W PCIe workstation card and belongs to the external-accelerator path, not the on-board accelerator path.
