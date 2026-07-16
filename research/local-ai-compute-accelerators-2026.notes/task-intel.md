---
task_id: intel
role: Intel 本地 AI 加速芯片目录分析师
status: complete
sources_found: 9
---

## Sources
[1] Intel Arc Pro B-Series overview | https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html | Source-Type: official | As Of: 2026-07-15 | Authority: 10/10
[2] Intel ARK Arc Pro B70 Graphics | https://www.intel.com/content/www/us/en/products/sku/245797/intel-arc-pro-b70-graphics/specifications.html | Source-Type: official | As Of: Q1 2026 | Authority: 10/10
[3] Intel Arc Pro B70 datasheet | https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[4] Intel Arc Pro B65 datasheet | https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b65-gpu.pdf | Source-Type: official | As Of: 2026-03 | Authority: 9/10
[5] Core Ultra Series 3 Quick Reference Guide | https://cdrdv2.intel.com/v1/dl/getContent/871380?fileName=Intel+Core+Ultra+Series+3+Processors+-+Quick+Reference+Guide+v1.pdf&view=true | Source-Type: official | As Of: 2026-01-05 | Authority: 10/10
[6] Intel CES 2026 Series 3 launch | https://newsroom.intel.com/client-computing/ces-2026-intel-core-ultra-series-3-debut-first-built-on-intel-18a | Source-Type: official | As Of: 2026-01-05 | Authority: 10/10
[7] ServeTheHome Arc Pro B70/B65 launch | https://www.servethehome.com/intel-announces-arc-pro-b70-and-b65-video-cards-big-battlemage-brings-big-memory-for-ai-workstations/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 8/10
[8] Newegg Intel Arc Pro B70 listing | https://www.newegg.com/intel-arc-pro-b70-32gb-graphics-card/p/N82E16814883008 | Source-Type: secondary-industry | As Of: 2026-07-15 | Authority: 7/10
[9] Micro Center ASRock Arc Pro B70 | https://www.microcenter.com/product/708790/asrock-intel-arc-pro-b70-creator-single-fan-32gb-gddr6-pcie-50-graphics-card | Source-Type: secondary-industry | As Of: 2026-07-15 | Authority: 7/10

## Findings
- Intel 当前 Arc Pro B-Series 工作站 dGPU 共 B70、B65、B60、B50 四款，旧目录只收 B60 已过时。[1]
- PPT 可统一简写为 Intel Arc Pro B70/B65/B60/B50。[1][2]
- B70 已正式发布，ARK 状态 Launched、Q1 2026；2026-07 有 Newegg 与 Micro Center 购买/库存证据。[2][8][9]
- B65 已进入正式目录并有 2026-03 datasheet，但广泛零售可购性证据弱于 B70。[1][4][7]
- B60、B50 仍在 Intel 当前产品总览和 Shop 区域，适合列入 2026-07 目录。[1]
- Core Ultra Series 3 是 Panther Lake 正式系列名，不是单颗芯片；系统自 2026-01 起上市。[5][6]
- 系列中集成 Arc B390/B370 的代表 SKU 包括 Core Ultra X9 388H、X7 368H/358H、Core Ultra 5 338H。[5]
- 386H 的正式名称是 Core Ultra 9 386H，不带 X。[5]

## Deep Read Notes
### Source [1]: Arc Pro B-Series overview
Key data: B70/B65/B60/B50 同属当前工作站级 AI GPU 家族。
Key insight: 足以推翻“Intel dGPU 只有 B60”的旧目录。
Useful for: slide dGPU 清单。

### Source [5]: Core Ultra Series 3 Quick Reference Guide
Key data: Series 3 包含 X9/X7/Ultra 9/7/5 多档 SKU，部分集成 Arc B390/B370。
Key insight: PPT 主标签宜用系列名，具体 SKU 会造成过度拥挤。
Useful for: SoC 命名与代表型号。

### Source [6]: CES 2026 launch
Key data: Series 3 为 Intel 18A AI PC/edge 平台，消费系统自 2026-01-27 销售。
Key insight: 上市以整机交付为主，不能把每颗裸片理解为独立零售。
Useful for: 在售状态边界。

## Gaps
- B65 广泛零售库存未充分验证；应标为已发布、渠道可购性有限。
- B50/B60 未逐零售商盘点，当前在售判断依赖 Intel 产品目录。

## Slide recommendation
- dGPU: Arc Pro B70, B65, B60, B50；若空间紧，优先 B70 / B60。
- SoC: Core Ultra Series 3 (Panther Lake)；不堆 14 个具体 SKU。
- 排除错误命名“Core Ultra X9 386H”。

## END
