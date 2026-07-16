# Task: Intel presentation taxonomy

**AS_OF:** 2026-07-15  
**Mode:** Standard expansion  
**Decision:** Use a hybrid: stable public family breadth on line 1, then current Series 3 SKUs plus the public architecture codename on line 2.

## Sources

1. Intel, “Intel® Core™ Ultra Processors Names and Numbers.” https://www.intel.com/content/www/us/en/support/articles/000097596/processors/intel-core-ultra-processors.html — `official`; last reviewed 2026-01-05; authority **10/10**; accessibility: **public, full HTML**.
2. Intel, “Intel Core Ultra Series 3 Processors — Quick Reference Guide.” https://www.intel.com/content/www/us/en/content-details/871380/intel-core-ultra-series-3-processors-quick-reference-guide.html — `official`; 2026-01-05; authority **10/10**; accessibility: **public landing page, downloadable PDF**.
3. Intel Newsroom, “CES 2026: Intel Core Ultra Series 3 Debut as First Built on Intel 18A.” https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a — `official`; 2026-01-05; authority **9/10**; accessibility: **public, full HTML**.
4. Intel, “New Intel® Core™ Ultra Series 3 Processors.” https://www.intel.com/content/www/us/en/products/details/processors/core-ultra.html — `official`; live catalog, accessed 2026-07-15; authority **10/10**; accessibility: **public, full HTML**.
5. Intel, “Intel® Core™ Ultra X9 Processor 388H.” https://www.intel.com/content/www/us/en/products/sku/245526/intel-core-ultra-x9-processor-388h-18m-cache-up-to-5-10-ghz/specifications.html — `official`; Q1 2026 product record, accessed 2026-07-15; authority **10/10**; accessibility: **public, full HTML**.
6. Intel, “Intel® Core™ Ultra X7 Processor 368H.” https://www.intel.com/content/www/us/en/products/sku/245523/intel-core-ultra-x7-processor-368h-18m-cache-up-to-5-00-ghz/specifications.html — `official`; Q1 2026 product record, accessed 2026-07-15; authority **10/10**; accessibility: **public, full HTML**.
7. Intel Newsroom, “Intel Unveils Panther Lake Architecture: First AI PC Platform Built on 18A.” https://newsroom.intel.com/client-computing/intel-unveils-panther-lake-architecture-first-ai-pc-platform-built-on-18a — `official`; 2025-10-09; authority **9/10**; accessibility: **public, full HTML**.
8. Intel Newsroom, “Press Kit: Intel Core Ultra Processors (Series 2).” https://newsroom.intel.com/press-kit/press-kit-core-ultra-series-2 — `official`; updated through 2025-05-20, core launches 2024-09-03/2024-10-10; authority **9/10**; accessibility: **public, full HTML**.
9. Intel, “Intel vPro® with Intel® Core™ Ultra Processors (Series 2) Brief.” https://www.intel.com/content/www/us/en/products/docs/processors/vpro/vpro-core-ultra-series-2-product-brief.html — `official`; accessed 2026-07-15; authority **9/10**; accessibility: **public, full HTML**.
10. Intel Newsroom, “Intel Core Ultra Ushers in the Age of the AI PC.” https://newsroom.intel.com/client-computing/core-ultra-client-computing-news-1 — `official`; 2023-12-14; authority **9/10**; accessibility: **public, full HTML**.
11. Intel Newsroom, “Fact Sheet: Intel Unveils Lunar Lake Architecture.” https://download.intel.com/newsroom/2024/client-computing/Lunar-Lake-Architecture-Fact-Sheet.pdf — `official`; 2024-06; authority **9/10**; accessibility: **public PDF**.
12. Intel Newsroom, “The ‘Blank Sheet’ that Delivered Intel’s Most Significant SoC Design Change in 40 Years.” https://newsroom.intel.com/client-computing/the-blank-sheet-that-delivered-intels-most-significant-soc-design-change-in-40-years — `official`; 2024, accessed 2026-07-15; authority **8/10**; accessibility: **public, full HTML**.
13. Andrew Cunningham, Ars Technica, “Intel fills out Core Ultra 200 laptop lineup with hodgepodge of CPUs, GPUs, and NPUs.” https://arstechnica.com/gadgets/2025/01/intel-rounds-out-core-ultra-200-laptop-cpus-with-new-but-less-advanced-models/ — `journalism`; 2025-01-06; authority **8/10**; accessibility: **public article**.
14. Mark Hachman, PCWorld, “Lunar Lake’s integrated RAM won’t happen again, Intel CEO says.” https://www.pcworld.com/article/2507953/lunar-lakes-integrated-dram-wont-happen-again-intel-ceo-says.html — `journalism`; 2024-10/11, following Intel Q3 2024 earnings; authority **8/10**; accessibility: **public article**.
15. Ben Hardwidge, Club386, “Intel Core Ultra Series 3 review: Panther Lake benchmarks.” https://www.club386.com/intel-core-ultra-series-3-panther-lake-review/ — `secondary-industry`; 2026-01-26; authority **7/10**; accessibility: **public article**.
16. Kate Moran, Nielsen Norman Group, “Technical Jargon.” https://www.nngroup.com/articles/technical-jargon/ — `secondary-industry`; 2020-09-15; authority **8/10**; accessibility: **public, full HTML**.
17. Joanna K. Garner, Michael Alley, Allen Gaudelli and Sarah Zappe, “Common Use of PowerPoint versus the Assertion–Evidence Structure: A Cognitive Psychology Perspective.” http://writing.engr.psu.edu/Garner_et_al_2009.pdf — `academic`; 2009-11; authority **8/10**; accessibility: **public PDF**.

## Findings

1. **Intel’s durable public hierarchy is family → performance tier → SKU → suffix.** Intel says the leading SKU digit maps to Series 1, 2 and 3, while X9/X7/9/7/5 indicate performance tier; therefore `Core Ultra Series 1–3` is a compact, officially decodable breadth label, not an invented umbrella. [1]
2. **Series labels and architecture codenames are not one-to-one.** Series 1 maps cleanly to Meteor Lake, and Series 3 maps cleanly to Panther Lake, but Series 2 includes Lunar Lake 200V and Arrow Lake 200S/H/HX; some 200U implementations also reuse substantial Meteor Lake-era IP. A codename-only list looks neat but hides this product reality. [8][10][13]
3. **Series 3 is the right 2026 emphasis.** Intel launched Series 3 in January 2026, describes it as formerly codenamed Panther Lake, and positions X9/X7 as the highest-integrated-graphics class; Intel’s live catalog lists X9 388H and X7 368H with Arc B390. [2][3][4][5][6]
4. **SKU-only is concrete but too narrow for a support/breadth row.** `Core Ultra X9 388H · X7 368H` accurately names current Panther Lake examples and matches adjacent vendor rows, but it visually implies that the Intel path begins and ends with two premium 2026 laptop parts. A family line is needed if the intended message is a reusable Intel integrated-accelerator path across generations. [1][4][5][6]
5. **`SoC` is factually defensible but too coarse as the primary category label.** Intel itself calls Meteor Lake and Panther Lake system-on-chip designs, including disaggregated multi-tile designs; `SoC` therefore does not mean monolithic silicon. But the term does not tell a mixed audience what accelerator resources matter, whereas `Integrated CPU · GPU · NPU` does. [7][12]
6. **`Integrated CPU · GPU · NPU` is accurate across Core Ultra generations, with configuration caveats.** Intel’s Series 1 launch describes acceleration across CPU, GPU and NPU; Series 2 documentation says all portfolio processors use CPU/GPU/NPU for AI tasks; Series 3 similarly exposes all three engines, although Arc branding and engine capability vary by SKU. [3][9][10]
7. **Do not apply `Unified memory` as a blanket Intel Series 1–3 subtitle.** Intel’s precise term for Lunar Lake 200V is `memory on the package`; Series 2 Arrow Lake products do not all use it, and Series 3 returns to off-package LPDDR5X/DDR5 configurations. `Shared system memory` is the safer cross-vendor functional label if the slide needs a memory subtitle. [9][11][14][15]
8. **`Unified memory` is especially risky beside Apple and NVIDIA.** Readers may infer Apple-style on-package unified memory or GB10-specific coherent-memory claims. Intel’s CPU, iGPU and NPU can use system memory without every Core Ultra product sharing Lunar Lake’s packaging. The slide should not collapse “shared addressable system RAM,” “memory on package,” and branded unified-memory architectures into one physical-design claim. [9][11][14]
9. **The best compact taxonomy is hybrid, not an exhaustive codename sequence.** The public series gives durable breadth; two current SKUs preserve parity with adjacent AMD/NVIDIA/Apple rows; a single parenthetical `Panther Lake` bridges Intel’s architecture vocabulary without forcing viewers to decode four Lake names. [1][2][4][16]
10. **Information design favors one readable hierarchy over parallel taxonomies.** Research on technical slides warns against unnecessary cognitive load, and NN/g recommends pairing important specialist terms with plain-language context. Showing series numbers, four codenames and multiple SKUs at equal weight would make the audience reconcile three classification systems inside one compact row. [16][17]

## Recommended slide treatment

### Exact two-line Intel row

**Core Ultra Series 1–3**  
**X9 388H · X7 368H — Series 3 (Panther Lake)**

### Category terminology

Replace:

**SoC** · *Unified memory*

with:

**Integrated CPU · GPU · NPU** · *Shared system memory*

If the existing visual hierarchy cannot accommodate the longer category label, retain **SoC** but change only the subtitle to **Shared system memory**.

### Rationale

- **Factual durability:** `Core Ultra Series 1–3` remains true if individual SKUs rotate; the live 2026 examples can be refreshed without rebuilding the taxonomy.
- **Audience readability:** the first line answers “what Intel family is covered”; the second answers “which current chips should I recognize.”
- **2026 breadth:** Series 3 receives visual priority without erasing Series 1/2 systems.
- **Adjacent-row consistency:** X9 388H and X7 368H are chip names, matching the AMD, NVIDIA and Apple rows’ concrete-product pattern.
- **Intel collaboration value:** `Panther Lake` appears once as a secondary bridge for Intel insiders, not as the main decoding burden.
- **Memory accuracy:** `Shared system memory` describes the resource behavior needed by the accelerator-management story without falsely claiming that Meteor Lake, Lunar Lake, Arrow Lake and Panther Lake share one memory-packaging architecture.

### Rejected alternatives

1. **`Meteor Lake · Lunar Lake · Arrow Lake · Panther Lake`**  
   Rejected because codenames are architecture vocabulary, not the public product taxonomy; Series 2’s split across Lunar and Arrow Lake makes the sequence look cleaner than the underlying portfolio, while viewers still cannot identify a purchasable chip. It is also inconsistent with adjacent rows that name products.

2. **`Core Ultra X9 388H · Core Ultra X7 368H`**  
   Rejected as the final treatment because it communicates only two premium Series 3 laptop SKUs. It is the strongest alternative when the slide means “currently validated hardware only,” but it under-communicates cross-generation breadth and will age faster than the hybrid.

## Deep Read Notes

### Intel naming and 2026 catalog

Intel’s support article explicitly defines the first SKU digit as the series indicator and separates that from performance tiers and suffixes. The Series 3 quick reference guide then binds the public name to “formerly codenamed Panther Lake,” while ARK confirms that X9 388H and X7 368H are launched Q1 2026 products with Arc B390 integrated graphics. This supports a hierarchy in which the public family/series is primary, SKUs are evidence, and codename is a parenthetical bridge. [1][2][4][5][6]

### Architecture and memory terminology

Intel uses `SoC` for both Meteor Lake’s disaggregated tile design and Panther Lake’s multi-chiplet design, so rejecting `SoC` as technically wrong would be incorrect. The issue is communicative precision. Intel consistently describes the relevant engines as CPU, GPU and NPU, which is more useful to an accelerator-management audience. For memory, Intel’s own Lunar Lake term is `memory on the package`; later reporting quotes Intel saying Panther Lake returns volume memory off-package, and the 2026 Panther Lake review confirms no embedded package memory. The broad slide label should therefore be `Shared system memory`, not `Unified memory`. [7][9][10][11][12][14][15]

### Independent readability and portfolio check

Ars Technica’s Series 2 analysis demonstrates why a series label alone cannot stand in for architecture or capability: 200V is Lunar Lake, most other 200 mobile/desktop families are Arrow Lake, and 200U reuses older IP. This is the strongest evidence for retaining concrete SKUs. Conversely, slide-design and UX evidence argues against exposing all internal architecture detail at once: unfamiliar terminology adds cognitive load unless it is both necessary and meaningful to the audience. The hybrid treatment keeps the exact current chips visible while demoting the codename to context. [13][16][17]

## Gaps and contrary claims

- **Argument favoring SKU-only display:** If this row is a strict compatibility or validation matrix rather than an ecosystem illustration, only verified processor numbers should appear. `Core Ultra Series 1–3` could be read as a support claim for every SKU and OEM implementation in those collections, which neither Intel’s catalogs nor the existing Olares research proves. In that interpretation, use only `Core Ultra X9 388H · Core Ultra X7 368H` and add more SKUs only after validation.
- The available Olares evidence establishes an `Intel iGPU` allocation mode at code level but does not provide a per-SKU validation matrix for Meteor Lake, Lunar Lake, Arrow Lake and Panther Lake. The recommended breadth line is therefore a **presentation taxonomy**, not a claim that every Core Ultra SKU has identical runtime coverage.
- Intel product naming pages are live and can change. Source [1] was updated for Series 3, while the broader naming guide still showed wording centered on SKU numbers 1 or 2 when accessed; the dedicated support article should be the naming authority.
- `Shared system memory` is functionally safer than `Unified memory`, but it still does not assert identical coherency, zero-copy behavior, bandwidth, capacity or driver exposure across Intel, AMD, Apple and GB10.
- Some industry sources casually describe ordinary integrated-graphics system RAM as “unified memory.” That broad usage is understandable, but it is less precise in a vendor-comparison slide where Apple and NVIDIA attach stronger architectural meaning to the phrase.
- `Panther Lake` is now a public Intel codename, not secret terminology. The objection is readability and hierarchy, not confidentiality.
