# Intel CPU + On-board Accelerator

> External collaboration PPT, slide 28 (single-PCBA on-board accelerator / current flagship implementation). English content source for HTML.
> Data: [Olares One first-party benchmarks](../../directions/hardware/research/olares-one-benchmarks.md). Snapshot 2026-07; re-verify before publishing.

---

## Slide copy

### Title

**Intel CPU + On-board Accelerator**

Olares One is the current flagship: Core Ultra 9 275HX + RTX 5090 Mobile, delivering our best overall performance and broadest workload coverage across all seven cloud-proven scenarios.

### Current flagship

**Intel Core Ultra 9 275HX** · NVIDIA RTX 5090 Mobile 24GB · 96GB RAM · 2TB NVMe · **$3,999**

### Three first-party proof points

#### 1. Multi-user LLM throughput

| System | Qwen3-30B-A3B (concurrency 1 → 8, tok/s) |
|--------|-------------------------------------------|
| **Olares One** | **157 → 81** |
| Mac Studio M3 Ultra | 84 → 25 |
| Mac Studio M4 Max | 81 → 20 |
| Beelink GTR9 Pro (AMD 395+) | 61 → 12 |

#### 2. Image generation

**Flux.1 dev: 8.32 seconds per image (warm cache)**  
Mac Studio M3 Ultra takes ~73 seconds; Olares One is **8.8× faster**.

#### 3. Workload coverage

**The only system to complete the full LLM + image + video test suite.**  
Olares One completed every tested model plus Flux, Wan 2.2 and LTX-Video; every comparison system had unsupported or incomplete workloads.

### Seven cloud-proven scenarios, one flagship

**Personal Agent · App Development · Audio · Image · Smart Home · AI Companion · Private Workspace**

---

## Working notes

- This path is defined by single-PCBA integration: Intel CPU and accelerator share the system power, thermal, acoustic and size envelope.
- Olares One currently uses Core Ultra 9 275HX + RTX 5090 Mobile 24GB. This is the current implementation, not a vendor requirement.
- Future Intel or other accelerators can enter this path if they meet the board-level power, thermal, memory and software requirements.
- Arc Pro B70 is a 160–290W PCIe workstation card and belongs to the external-GPU path.
- Benchmarks are Olares first-party tests, not independent third-party results.
- Qwen3-30B-A3B uses vLLM on Olares One; comparison systems use their available frameworks.
- Honest boundary: GPT-OSS-120B exceeds 24GB VRAM and requires offload; Olares One trails Mac Studio M3 Ultra on that test.
- $2,999 was the crowdfunding / benchmark-time price; the slide uses the current $3,999 retail price.
