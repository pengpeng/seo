# Arc Pro B70：AI NAS 的外接 GPU

> 对外合作 PPT 第 26 页（形态①：外置协处理器 / eGPU · Intel NAS 方向）。中文底稿，过稿后补英文 + script + HTML + Figma。
> 数字溯源见 [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md) 与 [本页资料汇总 references.md](./references.md)。快照 2026-07-14，发布前复核。

---

## Slide copy（中文底稿）

### 标题

**Arc Pro B70：AI NAS 的外接 GPU**
一块外置 Arc Pro B70，把传统 NAS 变成覆盖 Personal Agent、音频、智能家居与私有办公的多场景 AI NAS。

| 方案 | 显存/内存 | 2026-07 价格 | prefill pp t/s | decode tg t/s |
|------|-----------|------------------------|--------------------------|-----------------------|
| **NAS + 外接 Arc Pro B70（AI NAS）**<br>Q4 · no MTP | **32GB 独显** | **给现有 NAS 加卡 +~$1,100–1,300**（坞+卡）｜从零配整套 ~$1,600–2,000 | ~615 · **长上下文稳** | ~55–82 |
| AMD 395+ 迷你机<br>Q4 · no MTP | 128GB 统一 | **~$3,399** | ~900–1,270 · 长上下文下降 | ~62–81 |
| Mac Studio M4 Max<br>4-bit · no MTP | 64GB 统一 | **$3,499 起**（≥64GB） | ~1,100–1,370 | ~42–70 |
| **DGX Spark**<br>MXFP4 · llama.cpp · no MTP | **128GB 统一** | **$4,699** | **~2,289** | **~63** |
| Mac Studio M3 Ultra<br>4-bit · no MTP | 96GB 统一 | **$5,299** | ~1,640–2,620 | ~70–98 |
| RTX 5090 桌面单卡<br>Q4_K_M · llama.cpp · no MTP | 32GB 独显 | **~$4,329**<br>仅显卡 | **~2,892** | **~183** |
| NVIDIA DGX Spark<br>NVFP4 · vLLM · MTP | 128GB 统一 | **$4,699** | ~4,850–6,255 | ~85–112 |

### 右侧｜优势

1. **多接口覆盖，外接几乎不降速**：支持 OCuLink / Thunderbolt，覆盖更多 NAS、迷你机与 CPU 平台；LLM 权重常驻显存，稳态推理仅比内置 x16 低约 2–3%，远小于游戏类 eGPU 常见的 25–40% 损失。
2. **灵活升级、延长设备寿命**：按预算选择 B60 / B70，外置算力可在兼容设备间复用；后续只升级 GPU 模块，不换主机，降低淘汰风险。
3. **OEM 产品与供应链更轻**：基础 NAS 不为 GPU 重做主板、机箱与散热；GPU 不进入基础机 BOM 和库存，也不增加多档算力 SKU。
4. **一套硬件覆盖四类高价值负载**：**Personal Agent、音频 AI、智能家居、私有办公**。
5. **新增 Arc Pro 销量，扩大软件生态**：每台 AI NAS 都成为 B70 / B60 的新增挂载点，并扩大 Intel 推理软件适配与开发者覆盖。
6. **极具优势的价格**：现有 NAS 加卡仅需约 $1,100–1,300，从零整套约 $1,600–2,000，显著低于表内整机竞品。

### 右侧｜需要改进

1. **prefill 软件潜力尚未释放**：Personal Agent 每轮都要处理长上下文，prefill 决定首字延迟。B70 当前约 615 pp t/s 仍偏低，但硬件潜力尚未挖掘，需要继续优化 XMX attention 与整体推理软件栈。
2. **价格优势受内存周期影响**：如果统一内存价格回到 2025 年水平，价差会收窄；长期价值必须落在复用存量 NAS、数据本地与模块化升级。

*来源与测试条件：[references.md](./references.md)。*

---

## 工作底稿（备查，不上对外幻灯）

- **价格（2026-07-14 deep research，见 [local-ai-hardware-prices-2026-07](../../research/local-ai-hardware-prices-2026-07.md) task-d）**：B70 卡 **~$999**（原 $949）；已有 NAS 增加卡/坞/线缆/供电约 **$1,100–1,300**，从零配置整套约 **$1,600–2,000**。AMD 395+ 128GB **主流 $3,399 / 直营最低 $1,999（GMKtec，挂"即将涨价"）**（原 ~$1,999）。Mac M4 Max ≥64GB **$3,499**（原 $2,699）。M3 Ultra 96GB **$5,299**（原 $3,999，256GB 已停）。**诚实边界**：别写"AMD 全线暴涨"（GMKtec 直营仍 $1,999）；2H26 涨势或放缓，发布前复核。
- **OEM / 功耗散热（task-e）**：B70 额定 TBP **160–290W**（Intel 参考卡 230W，建议整机 PSU 550W），**实测跑本模型 ~114W**；消费 NAS 电源 60–250W、空闲 ~22–24 dB——内置放不下、会击穿功耗/散热/静音预算。坞（Minisforum DEG1 / ADT-Link）下行 PCIe ×16 + 自备 ATX PSU，把 GPU 功耗/散热隔离在坞内。先例：UGREEN iDX6011 Pro NAS + GMKtec/AOOSTAR/Minisforum 迷你机都已内置外接口。
- **右侧优势展开**：用户侧＝按预算选择 B60 / B70，外置算力可在兼容设备间迁移，后续只换 GPU 模块，不换主机，降低一次性支出和淘汰风险。OEM 侧＝一块工作站级 GPU（B70 额定 160–290W）内置会击穿 NAS 的电源/散热/静音预算（消费 NAS 电源仅 60–250W、空闲 ~22 dB），逼其重做电源+风道+机箱；外置坞自带 PSU+风冷把功耗/散热/噪音隔离在坞里。GPU 与整机解耦，也避免把高价且波动的显卡压进整机库存，降低资本占用、跌价/断供风险与 SKU 数量。Intel 侧＝新增 B70 / B60 挂载点，并带动推理软件适配和开发者覆盖。
- **外接口选型（OCuLink vs 雷电，正文淡化、只讲"哪个有用哪个"）**：对大模型**稳态推理两者都够**——模型加载进显存后链路几乎空闲，选型交给具体机器有哪个口即可。技术上 OCuLink = 直连 PCIe 4.0 ×4、64Gbps、零协议转换，比雷电更快/更稳/更便宜（只要主机/NAS 有空余 PCIe 通道引出 SFF-8611 口）；雷电胜在即插即用、免拆机。**对比 NVIDIA eGPU 在 Linux**：能用但问题多（需强制注册键、调内核参数、打补丁，否则易硬锁/热插拔不稳）；Intel Arc + 全开源 Linux 图形栈路径干净得多——此点是内部认知，正文不展开。
- **Personal Agent / 承接第 24 页（正文已下沉为一行场景标注）**：Personal Agent 对标全球白领 ~$40–50T 工资盘；付费佐证 Claude Code ARR >$2.5B、Codex 5M+ 周活；NAS 天生 7×24 在线且握有全部上下文＝"越用越懂你"的前提。完整叙事见 [ppt/24 slide](../24/cloud-proven-scenarios-slide.md) 与逐字稿 [external-egpu-script.md](./external-egpu-script.md)。本方案覆盖第 24 页七场景中的 Personal Agent / 音频 AI / 智能家居 / 私有办公。
- **对比表口径（关键）**：主速度列＝Qwen3.6-35B-A3B、单流、4-bit、no MTP；每行注明量化与引擎。DGX Spark 和 RTX 5090 都采用 llama.cpp 的 pp512/tg128 结果，分别约 2,289/62.61 与 2,892/183。B70 non-MTP ~55–82；单卡这颗 MoE 在当前 B70 软件栈上开 MTP 是负优化（72–82→47–63）。
- **DGX Spark 优化上限（表底弱化展示）**：NVFP4 + vLLM + MTP 在 4K–32K 上下文的公开结果约 4,850–6,255 pp2048/ctx_pp、不同提示约 85–112 tg t/s；部分 Atlas/DFlash 配置峰值超过 120，但不作为表内常态范围。Q4_K_M+llama.cpp、no MTP 另有约 70 tg t/s，但未给可直接引用的 pp512。
- **prefill 诚实边界**：Personal Agent 每轮会处理系统指令、长对话、记忆、文件与工具结果；prefill 决定首字延迟，decode 只决定开始回答后的流速。prefix cache 能复用稳定前缀，但动态上下文持续变化，不能消除长上下文 prefill 压力。短提示 **Mac(~1.1–1.4K) ≈ AMD(~0.9–1.3K) > B70(~615，llama.cpp)**；B70 prefill 是**软件短板非硬件**——XMX attention 与整体推理软件栈仍有明显优化空间。B70 的 prefill 强项是长上下文稳（64K 仍 411），AMD iGPU 长上下文 prefill 暴涨（32K 分钟级）。
- **$/GB 不对外**：B70 ~$30/GB vs NVIDIA $75/GB 是真的，但便宜可能反映 Intel 定价激进（甚至让利），**不作对外卖点**（对 Intel 的场子尤其别提）；对外只讲客观现价 + 复用加卡 + 方便。
- **Olares 能力不上幻灯展开**：驱动自动检测、oneAPI/ROCm、模型与应用安装、Agent tool、LarePass 远程/VPN/身份、沙盒安全等只在此备查与 references.md；幻灯仅用“换成 Olares，即进入 AI NAS 产品线”。
- 软件成熟度（内部）：Arc 上 Vulkan 最稳、SYCL 需调优、vLLM 走 Intel `llm-scaler`——对外只讲"Olares 已封装、开箱即用"。

## 来源

- [本页资料汇总 references.md](./references.md)（价格/性能/OCuLink/内存涨价/Olares 能力的数据 + 逐条 URL）
- [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md) §2b；价格研究 [local-ai-hardware-prices-2026-07](../../research/local-ai-hardware-prices-2026-07.md)（task-a/b/c/d/e）
- Personal Agent 场景 + 付费验证：[ppt/24 slide](../24/cloud-proven-scenarios-slide.md)
