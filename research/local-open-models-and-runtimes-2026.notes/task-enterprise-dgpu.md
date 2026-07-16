---
task_id: enterprise-dgpu
role: 企业/工作站本地 AI dGPU 官方目录审计员
status: complete
sources_found: 12
---

## Sources
[1] Intel Arc Pro B-Series overview | https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[2] Intel Arc Pro B70/B65 commercial launch | https://newsroom.intel.com/client-computing/intel-core-ultra-series-3-with-vpro-powers-next-gen-pcs-on-18a | Source-Type: official | As Of: 2026-03-25 | Authority: 10/10
[3] Intel Arc Pro A60 ordering | https://www.intel.com/content/www/us/en/products/sku/235979/intel-arc-pro-a60-graphics/ordering.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[4] Intel Arc Pro A50 ordering | https://www.intel.com/content/www/us/en/products/sku/230316/intel-arc-pro-a50-graphics/ordering.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[5] NVIDIA RTX PRO desktop GPU catalog | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/ | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[6] NVIDIA RTX PRO Blackwell workstation announcement | https://nvidianews.nvidia.com/news/nvidia-blackwell-rtx-pro-workstations-servers-agentic-ai | Source-Type: official | As Of: 2025-03-18 | Authority: 10/10
[7] NVIDIA RTX PRO 6000 Blackwell Series | https://www.nvidia.com/en-us/products/workstations/professional-desktop-gpus/rtx-pro-6000-family/ | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[8] AMD workstation graphics catalog | https://www.amd.com/en/products/graphics/workstations.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[9] AMD Radeon AI PRO R9700 | https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9700.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[10] AMD Radeon AI PRO R9600 | https://www.amd.com/en/products/graphics/workstations/radeon-ai-pro/ai-9000-series/amd-radeon-ai-pro-r9600.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[11] AMD Radeon AI PRO R9600 driver release notes | https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-SI-AI-PRO-R9600.html | Source-Type: official | As Of: 2026-07-15 | Authority: 9/10
[12] AMD Radeon PRO W7000 workstation catalog | https://www.amd.com/en/products/graphics/workstations/radeon-pro.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10

## Findings
- Intel’s current Arc Pro B-Series workstation catalog contains exactly B70, B65, B60 and B50; all four are explicitly positioned for local AI/professional workloads and multi-GPU use.[1]
- Intel formally launched B70 and B65 on 2026-03-25, while the same current family page retains B60 and B50, so all four qualify for the current/announced slide tier.[1][2]
- Intel Arc Pro A60 and A50 remain useful previous-generation labels but their official ordering pages say “Retired and discontinued,” so they must not be mixed into the current tier.[3][4]
- NVIDIA’s current professional desktop catalog lists RTX PRO 6000, 5000, 4500, 4000 and 2000 Blackwell; form-factor variants such as 6000 Max-Q and 4000 SFF should be collapsed on a compact chip-model slide.[5]
- NVIDIA’s launch announcement originally covered desktop RTX PRO 6000, 5000, 4500 and 4000 Blackwell, while the live 2026 catalog adds RTX PRO 2000 Blackwell; the current catalog is therefore the better AS_OF source.[5][6]
- RTX PRO 6000 Blackwell Server Edition is a passive data-center card, whereas Workstation and Max-Q Workstation editions are active desktop cards; the compact slide should use the family model only and avoid implying that the server edition is a workstation card.[7]
- NVIDIA’s live catalog separately labels Ada Lovelace and Ampere below Blackwell, so RTX 6000/5000 Ada are defensible older-generation references but not current-generation Blackwell entries.[5]
- AMD’s current workstation catalog separates Radeon AI PRO R9000 (RDNA 4) from Radeon PRO W7000 (RDNA 3); R9700 and R9600 are the current AI-first model names, while W7900/W7800 belong in the older-generation line.[8][9][10][12]
- R9600 has an official product page and dedicated official driver, but no located launch announcement or dated availability statement; classify it as “current catalog/announced,” not “verified broadly shipping.”[10][11]
- A balanced compact slide should show complete current families where short, then only two representative older models per vendor rather than reproducing every legacy catalog tier.[1][5][8][12]

## Deep Read Notes
### Source [1]: Intel Arc Pro B-Series overview
Key data: The live family page names B70, B65, B60 and B50 and provides a four-product comparison plus current shop links.
Key insight: The prior B60-only or B70/B65-only framing is incomplete as of 2026-07-15.
Useful for: Exact Intel current-tier list.

### Source [5]: NVIDIA RTX PRO desktop GPU catalog
Key data: The live page separates Blackwell, Ada Lovelace, Ampere and Turing tables; Blackwell desktop models are 6000, 5000, 4500, 4000 and 2000, with some form-factor variants.
Key insight: It provides both the current family and an official generation boundary in one source.
Useful for: Exact NVIDIA current tier and older-generation separation.

### Source [7]: NVIDIA RTX PRO 6000 Blackwell Series
Key data: The family has Server, Workstation and Max-Q Workstation editions with passive versus active thermal designs.
Key insight: “RTX PRO 6000 Blackwell” is safe compact family text only when the slide is not claiming every edition is a desktop workstation card.
Useful for: Naming caveat and exclusion of server-edition detail.

## Gaps/contrary evidence
- AMD pages timed out in direct full-page retrieval; their official indexed text exposed the model names and architecture split, but R9600’s announcement date and channel availability were not found.
- An official product page proves catalog existence, not global stock; this especially affects R9600 and should not be rewritten as “widely available.”
- NVIDIA still catalogs Ada, Ampere and Turing products, so “current catalog” alone does not mean “current generation”; generation headings, not mere page presence, determine the split.
- Intel A-series may still receive shared driver support, but official ordering status is retired/discontinued; software support is not evidence of a current hardware SKU.
- AMD W7000 and NVIDIA Ada remain commercially relevant and AI-capable, but placing them beside R9000/Blackwell without an “Older generation” label would blur the requested 2026 market picture.

## Exact slide list

### Current catalog / announced
- Intel: `Arc Pro B70 · B65 · B60 · B50`
- NVIDIA: `RTX PRO Blackwell 6000 · 5000 · 4500 · 4000 · 2000`
- AMD: `Radeon AI PRO R9700 · R9600`

### Older generation
- Intel: `Arc Pro A60 · A50`
- NVIDIA: `RTX 6000 Ada Generation · RTX 5000 Ada Generation`
- AMD: `Radeon PRO W7900 · W7800`

## END
