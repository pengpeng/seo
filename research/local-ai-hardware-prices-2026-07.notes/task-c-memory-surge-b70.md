# task-c · 2026 内存涨价宏观 + GDDR6 vs LPDDR5X 差异 + Arc Pro B70 现价

> AS_OF 2026-07-14 · explore 子代理蒸馏笔记（只读模式，Lead 代写落盘）

## Sources

| # | URL | Type | As-Of | Authority |
|---|-----|------|-------|-----------|
| 1 | https://www.trendforce.com/presscenter/news/20260601-13070.html | Industry analyst (TrendForce) | 2026-06-01 | 10 |
| 2 | https://www.trendforce.com/presscenter/news/20260331-12995.html | Industry analyst (TrendForce) | 2026-03-31 | 10 |
| 3 | https://www.trendforce.com/presscenter/news/20260514-13044.html | Industry analyst (TrendForce) | 2026-05-14 | 10 |
| 4 | https://www.trendforce.com/presscenter/news/20260703-13134.html | Industry analyst (TrendForce) | 2026-07-03 | 10 |
| 5 | https://www.trendforce.com/presscenter/news/20260709-13140.html | Industry analyst (TrendForce) | 2026-07-09 | 10 |
| 6 | https://www.trendforce.com/presscenter/news/20260310-12959.html | Industry analyst (TrendForce) | 2026-03-10 | 10 |
| 7 | https://www.trendforce.com/presscenter/news/20260701-13130.html | Industry analyst (TrendForce) | 2026-07-01 | 10 |
| 8 | https://www.thelec.net/news/articleView.html?idxno=11564 | Journalism (The Elec, citing Sigmaintell) | 2026-07-14 | 8 |
| 9 | https://www.tomshardware.com/pc-components/gpus/new-rumor-suggests-8gb-radeons-could-get-usd20-price-hikes-16gb-usd40-rising-gddr6-spot-prices-add-fuel-to-the-gpu-pricing-fire | Journalism (Tom's Hardware, citing DRAMeXchange) | 2025-12-02 | 8 |
| 10 | https://www.cnn.com/2026/07/13/tech/ai-memory-shortage-apple-nintendo-price-hikes | Journalism (CNN, citing IDC/TechInsights) | 2026-07-13 | 7 |
| 11 | https://bworldonline.com/technology/2026/06/26/759428/apple-raises-prices-of-macbooks-ipads-as-memory-costs-skyrocket/ | Journalism (BusinessWorld, citing TrendForce) | 2026-06-26 | 7 |
| 12 | https://www.newegg.com/intel-arc-pro-b70-32gb-graphics-card/p/N82E16814883008 | Official retail (Newegg) | 2026-07-14 | 9 |
| 13 | https://www.microcenter.com/product/708790/asrock-intel-arc-pro-b70-creator-single-fan-32gb-gddr6-pcie-50-graphics-card | Official retail (Micro Center) | 2026-07-14 | 9 |
| 14 | https://hothardware.com/news/intel-arc-pro-b70-b65-cards-debut | Journalism (HotHardware) | 2026-03-25 | 7 |
| 15 | https://www.servethehome.com/amd-details-ryzen-ai-halo-ai-dev-mini-pc-pre-orders-in-june-for-3999/ | Journalism (ServeTheHome) | 2026-06 | 7 |

*Reuters (2026-01-29) 关于三星/SK 海力士/Apple 内存挤压：fetch 401，未用于硬数字。*

## Findings

1. 常规 DRAM 合约价 **1Q26 环比 +93–98%（已实现）**，带动 DRAM 行业营收 +81% QoQ 至 $97B [1]。
2. TrendForce 预测常规 DRAM 合约价 **2Q26 环比 +58–63%**（CSP 接受涨价、供应商优先 server/RDIMM）[1][2]。
3. **LPDDR5X 合约 ASP 2Q26 预测 +78–83%**、LPDDR4X +70–75% [3]。
4. 消费级 **LPDDR5X 12GB 2Q26 环比 +89%（Sigmaintell）**；LPDDR4X 4GB +75% [8]。
5. 根因：AI server/推理需求把产能挪给 HBM 与高容量 server DRAM，挤出 PC/移动/显卡 DRAM；"追赶式涨价"[1][2][8]。
6. HBM 2026 合约价稳中有降，但 1Q26 HBM 晶圆盈利低于 DDR5 RDIMM，供应商在谈 2027 大幅涨 [1][4]。
7. **GDDR6 也涨但无 TrendForce 合约 %**：显卡 DRAM 供应紧、2Q26"预计继续涨"、3Q26"随大盘涨"[2][4]；GDDR6 8Gb 现货从 $19.54（2025-07-01）→ $31.52（2025-12-02）**+61%**（DRAMeXchange 经 Tom's 引用）[9]。
8. **统一内存/高 RAM 机型零售端受创更重**：Apple 6 月中周期内涨 Mac/iPad $100–$300；TrendForce 关联 Apple 涨价与 2026 笔记本出货 −13.6%；主流笔记本 DRAM+SSD 占 BOM >30%，或需 +40% 零售保毛利 [6][7][11]。
9. **AMD Ryzen AI Halo（Strix Halo，128GB LPDDR5X-8000）标价 $3,999**——内存是 BOM 主因；NVIDIA DGX Spark（同 128GB 统一）$4,699 [15]。
10. **Intel Arc Pro B70（32GB GDDR6）：$949 MSRP（2026-03-25）；街价 Newegg/Micro Center ~$999.99（2026-07-14，+~5%），普遍有货、无抬价** [12][13][14]。

## Gaps

- 缺：TrendForce 逐季 **GDDR6 合约价 %**（仅定性）；Reuters 原文（fetch 401）；DigiTimes 一手；B70 三方卡街价（仅参考卡）；2Q26 **已实现**合约收盘（截至 7-14）。
- 反向点：多源指 **2H26 涨势放缓**——TrendForce 3Q26 常规 DRAM 仅 +13–18%（vs 1Q26 +93–98%）；Sigmaintell 料 2H26 涨速缓；CNN/IDC 称"最大一跳已过"[4][5][8][10]。短缺仍在，但 QoQ 加速或见顶。

## 结论摘要

- **量级**：2026 内存涨价历史级；常规 DRAM 1Q26 +93–98% QoQ（已实现）、2Q26 预 +58–63%；LPDDR5X +78–83%（TrendForce）~ +89%（Sigmaintell 消费 12GB）。
- **GDDR6 vs LPDDR5X**：GDDR6 未幸免（现货 +61% H2'25；trade press 称 >4×）但无合约 %；相对 LPDDR5X 合约涨幅小、且显卡厂多有 2025 末前预签合约。
- **差异影响**：统一内存机型（Mac、Strix Halo 128GB LPDDR5X）零售涨幅更大（Apple +$100–300；Strix Halo AI 机 $3,999、DGX Spark $4,699）> 独显 GDDR6 卡。
- **B70 现价**：~$999 街价（vs $949 MSRP），有货、无抬价。
- **是否拉大 B70 价格优势？**：是，中到明显——B70 稳在 ~$999，而统一内存 AI 盒/Mac 绝对涨幅大得多。置信度：量级 中高、差异 中、B70 价 中高。
