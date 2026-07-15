# ppt/26 资料汇总 · AI NAS（NAS + Arc Pro B70 外接 eGPU）

> 本页幻灯用到的所有数据点 + 逐条来源 URL，一页可溯源。快照 AS_OF 2026-07-14，事实型数字发布前以官方为准。
> 深度来源：价格研究 [local-ai-hardware-prices-2026-07](../../research/local-ai-hardware-prices-2026-07.md)（task-a/b/c/d/e）、[registry §2b](../../research/intel-coprocessor-slides-2026-07.notes/registry.md)。

## 1. 价格（2026-07-14 现价 + 2025 基线）

| 机型 | 2026-07 现价 | 2025 基线 | 来源 URL |
|------|--------------|-----------|----------|
| Arc Pro B70（32GB 卡） | **$999** 街价 | $949 MSRP（2026-03） | Newegg https://www.newegg.com/asrock-b70-ct-intel-arc-pro-b70-32gb-graphics-card/p/N82E16814930149 ｜ Micro Center https://www.microcenter.com/product/708790/ ｜ 发布 https://hothardware.com/news/intel-arc-pro-b70-b65-cards-debut |
| **AI NAS 外接升级 / 整套** | **现有 NAS 加卡 ~$1,100–1,300；从零整套 ~$1,600–2,000** | n/a | 估算：B70 ~$999 + 坞/线缆/供电 ~$100–300；从零另加 NAS 主机约 $500–700。坞参考 $98.80：https://www.newegg.com/p/2RC-02EB-00JK7 |
| AMD 395+ 128GB 迷你机 | **主流 $3,399**（Newegg/Micro Center）· 直营最低 **$1,999**（GMKtec，挂"即将涨价"） | ~$1,999（Computex 2025） | GMKtec https://www.gmktec.com/products/amd-ryzen%e2%84%a2-ai-max-395-evo-x2-ai-mini-pc ｜ Newegg https://www.newegg.com/gmktec-barebone-systems-mini-pc-amd-ryzen-ai-max-395-evo-x2-128-2t/p/2SW-007C-00016 ｜ Framework 主板 $3,149 https://frame.work/products/framework-desktop-mainboard-amd-ryzen-ai-max-300-series ｜ GTR9 Pro $4,349 https://www.bee-link.com/products/beelink-gtr9-pro-amd-ryzen-ai-max-395 |
| Mac Studio M4 Max（≥64GB，64GB/512GB） | **$3,499** | $2,699 | AppleInsider https://prices.appleinsider.com/mac-studio-2025 ｜ Basic Apple Guy https://basicappleguy.com/basicappleblog/rammaggedon |
| NVIDIA DGX Spark（128GB/4TB） | **$4,699** 官方现价 | $3,999 原 MSRP | NVIDIA Marketplace https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/ ｜ 2026-02 调价说明 https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713 |
| Mac Studio M3 Ultra（96GB/1TB） | **$5,299**（256GB 已停售） | $3,999 | AppleInsider https://prices.appleinsider.com/mac-studio-2025 |
| RTX 5090 桌面单卡（32GB） | **~$4,329，仅显卡**；主机/电源另计 | $1,999 发布 MSRP | NVIDIA 规格 https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ ｜ Amazon/二手价格快照 https://bestvaluegpu.com/history/new-and-used-rtx-5090-price-history-and-specs/ ｜ Newegg https://www.newegg.com/p/pl?d=rtx+5090 |

## 2. 2026 内存涨价（解释为何统一内存机型涨、B70 没涨）

- 常规 DRAM 合约价 1Q26 **+93–98% QoQ**（已实现）、2Q26 预 +58–63%：TrendForce https://www.trendforce.com/presscenter/news/20260601-13070.html
- LPDDR5X 合约 2Q26 **+78–83%**：TrendForce https://www.trendforce.com/presscenter/news/20260514-13044.html ；消费 LPDDR5X 12GB **+89%**（Sigmaintell/The Elec）https://www.thelec.net/news/articleView.html?idxno=11564
- GDDR6 现货 2025-07→12 **+61%**（无合约暴涨，显卡厂多有预签）：Tom's Hardware https://www.tomshardware.com/pc-components/gpus/new-rumor-suggests-8gb-radeons-could-get-usd20-price-hikes-16gb-usd40-rising-gddr6-spot-prices-add-fuel-to-the-gpu-pricing-fire
- Apple 2026-06-25/26 因内存短缺全线涨价：MacRumors https://www.macrumors.com/2026/06/29/apple-raised-prices-on-14-products/ ｜ The Verge https://www.theverge.com/tech/952162/apple-price-increase-ram-shortage
- 反向点（时效）：2H26 涨势或放缓（TrendForce 3Q26 +13–18%）：https://www.trendforce.com/presscenter/news/20260703-13134.html

## 3. Arc Pro B70 硬件 + 功耗（OEM 论点）

- 规格：32GB GDDR6 / 608 GB/s / 367 TOPS / PCIe 5.0 ×16 / 双槽 / 8-pin / 建议整机 PSU 550W。Intel 官方 https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstations/b-series/overview.html ｜ 规格书 https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2026-03/datasheet-b70-gpu.pdf ｜ TechPowerUp https://www.techpowerup.com/gpu-specs/arc-pro-b70.c4388
- **额定 TBP 160–290W（Intel 参考卡 230W）；实测跑 Qwen3.6-35B-A3B ~114W**（模型驻留空闲 ~18–22W）：PMZFX https://github.com/pmzfx/intel-arc-pro-b70-benchmarks/blob/master/llm-benchmarks.md
- 消费 NAS 电源/热/噪：Synology DS923+ 100–120W 电源、访问 35.5W、空闲 **22.9 dB(A)** https://global.download.synology.com/download/Document/Hardware/ProductSpec/DiskStation/23-year/DS923+/enu/Product_Spec_DS923+_enu.pdf ｜ DS224+ 60W 电源、空闲 22 dB https://global.download.synology.com/download/Document/Hardware/ProductSpec/DiskStation/24-year/DS224+/enu/Product_Spec_DS224+_enu.pdf ｜ QNAP TS-464 90W https://www.qnap.com/en-us/product/ts-464/specs/hardware ｜ 250W 级 TS-873A https://www.qnap.com/en-us/product/ts-873a/specs/hardware

## 4. OCuLink / eGPU 坞（不用重做主板的关键）

- OCuLink = PCIe 直连线缆（SFF-8611/8612），坞暴露 **PCIe 4.0 ×4 = 64Gbps**，非 Thunderbolt 隧道：PCI-SIG https://pcisig.com/PCIExpress/Specs/Cable/OCuLink_1.1
- Minisforum DEG1 坞：OCuLink 4i 上行 + PCIe ×16 下行 + **自备 ATX PSU**：https://www.minisforum.uk/products/minisforum-deg1 ｜ 评测 https://www.chargerlab.com/oculink-review-of-minisforum-deg1-egpu-dock/
- ADT-Link OCuLink→PCIe ×16（自备 ≥500W PSU）：https://www.adt.link/product/K993G.html
- **NAS/迷你机已有 OCuLink 先例**：UGREEN NASync iDX6011 Pro（专门加 OCuLink 做外接 GPU）https://nascompares.com/2026/01/21/ugreen-idx6011-pro-ai-nas-review/ ｜ 发布 https://www.prnewswire.com/news-releases/ugreen-expands-nasync-lineup-with-idx-series-at-ces-2026-...html
- **eGPU 对 LLM 仅损 ~3%**（权重常驻 VRAM）：Local AI Master https://localaimaster.com/blog/egpu-local-ai-benchmarks

## 5. 性能（Qwen3.6-35B-A3B，单流；量化/引擎/MTP 逐行标注）

| 方案 / 推理口径 | prefill pp t/s | decode tg t/s | 来源 |
|-----------------|----------------|----------------|------|
| B70 · Q4 · no MTP | ~615（64K 仍 411） | ~55–82 | PMZFX https://github.com/PMZFX/intel-arc-pro-b70-benchmarks ｜ #23533 https://github.com/ggml-org/llama.cpp/issues/23533 |
| AMD 395+ · Q4 · no MTP | ~900–1,270（长上下文暴涨） | ~62–81（Q4_K_M 76.94 / Q4_0 81.30） | strix-halo-guide https://github.com/hogeheer499-commits/strix-halo-guide/blob/main/MAX_PERFORMANCE_PLAN.md ｜ Signal65 prefill 1,273 https://signal65.com/research/ai/amd-ryzen-ai-halo-first-look/ |
| Mac M4 Max · 4-bit · no MTP | ~1,100–1,370 | ~42–70 | oMLX https://omlx.ai/benchmarks/pg7u9aqr ｜ LLMCheck https://llmcheck.net/models/qwen-36-35b-a3b-on-m4-max/ |
| **DGX Spark · MXFP4 · llama.cpp · no MTP** | **~2,289** | **~63** | pp512 2,289.18 / tg128 62.61 https://github.com/nabe2030/dense-27b-31b-dgx-spark |
| Mac M3 Ultra · 4-bit · no MTP | ~1,640–2,620 | ~70–98 | oMLX https://omlx.ai/benchmarks/6b70wq2p ｜ willitrunai https://willitrunai.com/can-run/qwen-3.6-35b-a3b-on-m3-ultra-256gb |
| RTX 5090 · Q4_K_M · llama.cpp · no MTP | **~2,892** | **~183** | 实测环境、pp512/tg128 https://zenn.dev/toki_mwc/articles/rtx5090-qwen36-35b-a3b-llmacpp-bench?locale=en |
| NVIDIA DGX Spark（优化）· NVFP4 · vLLM · MTP（非直接横比） | ~4,850–6,255 pp2048/ctx_pp（4K–32K） | ~85–112（随提示变化） | NVIDIA 模型卡 https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4 ｜ 2026-07 实测 https://forums.developer.nvidia.com/t/new-2-5x-faster-qwen3-6-nvfp4-unsloth-quants/376484 |

### DGX Spark 优化上限与边界

- **主表为何用 MXFP4**：它提供同一模型、llama.cpp、no MTP、pp512/tg128 的完整结果，可与 RTX 5090 的 pp512/tg128 更合理地横向比较。MXFP4 与 Q4_K_M、NVFP4 均不同，但都属于 4-bit 路径。
- **Q4_K_M + llama.cpp、no MTP**：同一 Qwen3.6-35B-A3B 的公开模型卡给出约 **70 tg t/s**，但未发布可直接引用的 pp512，因此不拿估算值填主表：https://huggingface.co/nerkyor/Qwen3.6-35B-A3B-GGUF-imatrix
- **NVFP4 + vLLM + MTP 优化上限**：4K–32K 上下文的公开结果约 **4,850–6,255 pp2048/ctx_pp**，不同提示的 decode 约 **85–112 tg t/s**。prefill 不可与主表 pp512 直接比较；表底单列仅用于展示 DGX Spark 软件栈潜力。部分 Atlas/DFlash 配置峰值超过 120 tg t/s，不作为常态范围。
- **排除错误匹配**：搜索结果中的 **823 pp t/s / 11.85 tg t/s** 是 Qwen3.6-27B Dense Q4_K_M，不是 35B-A3B；不进入本页。
- **更高数字的限制**：约 97–120 tg t/s 的结果可能依赖 Atlas、DFlash 或不同 MTP 配置；未逐项统一条件前，不作为本页主值。综述：https://tesseraai.cloud/en/blog/qwen-3-6-35b-dgx-spark-tokens-per-second/

- **B70 prefill 提升空间**：vLLM XPU XMX flash-attention 快 2.4–15×（engine-comparison https://github.com/PMZFX/intel-arc-pro-b70-benchmarks/blob/master/engine-comparison.md ）；llama.cpp XMX 注意力 PR #25222 https://github.com/ggml-org/llama.cpp/pull/25222 、#25312 https://github.com/ggml-org/llama.cpp/pull/25312 。caveat：vLLM XPU 暂不支持 Qwen3.6（GDN）。

## 6. Olares 能力（逐字稿 / 答疑备查）

依据 [basic/olares.md](../../basic/olares.md)（以 docs.olares.com / GitHub 复核版本）：

- **显卡驱动**：自动检测 + 自动装驱动 + CUDA/oneAPI/ROCm，用户不碰驱动（NVIDIA 最成熟；Intel 核显/独显、AMD 已支持）。
- **装模型**：一键本地 LLM / 图像模型（Ollama、ComfyUI 等）。
- **装应用**：Olares Market 一键装 app；app 可直接作为 Agent 的 tool。
- **装 Agent**：跑 Personal Agent，自然语言指挥、越用越懂你。
- **随时随地连接**：LarePass 提供远程访问 / VPN / 身份，把设备、手机、IoT 连进来统一编排（"随时随地在线"是它区别于本地 PC 的关键）。
- **安全**：沙盒 + 云原生最佳实践。
- 一句话立场：Intel 出芯片，Olares 出"驱动→模型→应用→Agent→远程访问"整条开箱体验。

## 7. 对外优势与待改进口径

### 优势

- **多接口覆盖 + LLM 外接损失小**：OCuLink / Thunderbolt 可覆盖更多兼容 NAS、迷你机与 CPU 平台。图形/游戏负载每帧频繁穿过外接链路，eGPU 性能可损失 25–40%；LLM 权重加载后常驻显存，逐 token 计算主要在卡内，稳态推理相对内置 x16 约低 2–3%（第 4 节 Local AI Master）。不能把这个结论外推到所有 GPU 负载。
- **灵活升级、延长设备寿命**：按预算选择 B60 / B70，外置算力可在兼容设备间复用，后续只升级 GPU 模块，不换主机，降低淘汰风险。这是产品价值判断。
- **产品与供应链更轻**：基础 NAS 不为 GPU 重做主板、机箱和散热；GPU 不进入基础 NAS BOM / 库存，可减少高价 GPU 的资本占用、价格波动与多档算力 SKU。这是产品与供应链推论，不是第三方量化数据。
- **四类高价值负载**：本方案覆盖 Personal Agent、音频 AI、智能家居、私有办公。
- **Arc Pro 销量与生态扩大**：每台 AI NAS 都成为 B70 / B60 的潜在新增挂载点，并可扩大 Intel 推理软件适配与开发者覆盖；属于合作价值判断，不写成既成市场事实。
- **价格优势**：按本页估算，已有 NAS 升级约 $1,100–1,300、从零整套约 $1,600–2,000，低于表内完整整机竞品；发布前复核 B70、坞和 PSU 街价。

### 待改进 / 风险

- **prefill 软件潜力尚未释放**：Personal Agent 每轮需要处理长上下文；prefill 决定多久开始回答，decode 决定开始后的流速。B70 当前约 615 pp t/s，低于其余主对比方案约 900–2,892，但这不是已经证实的硬件上限；XMX attention 与整体推理软件栈仍需优化（第 5 节）。
- **价格周期**：2026 的统一内存涨价放大了差距；若价格回到 2025 水平，价格优势会收窄。长期主张应放在复用 NAS、数据本地与模块化升级。

> $/GB 显存（B70 ~$30 vs NVIDIA $75）为内部认知，**不作对外卖点**（便宜可能反映定价激进）。
