# 面向本地 AI 的三条 Intel 硬件路线

> 对外合作 PPT 第 25 页（Olares × Intel 章节开篇 / 硬件路线地图）。
> 事实溯源见 [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md)、[Olares 产品口径](../../basic/olares.md) 与 [Olares One 第一方实测](../../directions/hardware/research/olares-one-benchmarks.md)。快照 2026-07，发布前复核。

---

## Slide copy（中文底稿）

### 标题

**面向本地 AI 的三条 Intel 硬件路线**

七个经云端付费验证的场景，对应三种以 Intel 为核心的产品架构：外置加速设备、独立 SoC 与板载加速器。

### 三条硬件路线

| 硬件路线 | 当前组合 | 产品形态 | 最适配 AI 场景 |
|----------|----------|----------|---------------|
| **外置加速设备** | Intel NAS / Box + 外置 **Arc Pro B70 32GB** | 把传统 NAS 升级为多场景 AI NAS | Personal Agent · Audio · Smart Home · Private Workspace |
| **独立 SoC** | **Panther Lake** CPU + NPU + iGPU | 具备 NAS 与 Windows VM 能力的 AI Box | **Private Meeting AI：现在** · Smart Home：下一步 · Personal Agent：未来 |
| **板载加速器** | **Core Ultra 9 275HX + RTX 5090 Mobile 24GB** | **Olares One**：当前旗舰验证 | Personal Agent · App Development · Audio · Image · Smart Home · AI Companion · Private Workspace |

---

## 工作底稿（备查）

- 第 25 页只画硬件路线地图，不重复第 26 页 B70 跑分、第 27 页会议市场数字或 Olares One benchmark。
- 主画面不再解释 Olares 的作用，不放平台能力条或总结段落；标题、副标题和三行路线完成过渡。
- 当前三路对应：
  - 第 26 页：Intel Box / NAS + Intel Arc Pro B70。
  - 第 27 页：Panther Lake SoC 独立运行。
  - Intel Core Ultra 9 + 板载 RTX 5090 Mobile 的板载加速器路线只在本页作为现有旗舰验证，不再单独展开一页。
- 第三条路线由整机形态定义，而非由 GPU 厂商定义：加速器需要与 Intel CPU 板载集成，并满足整机供电、散热、噪音、尺寸和显存要求。
- RTX 5090 Mobile 是 Olares One 当前采用的板载实现；未来满足同一板级封套和软件要求的 Intel 或其他厂商加速器也可采用。
- Arc Pro B70 是 160–290W 的 PCIe 工作站卡，属于第 26 页外置加速设备路线，不适合直接作为这条板载加速器路线的板载器件。
- Olares 不是 NAS 或 AI PC；它是个人云操作系统。表格中的 NAS / Windows VM 是平台能力，不能把品牌重新定义为 NAS OS。

## 删除的旧口径

- 删除 `$600 外挂 → $999 一体盒 → $3,000 旗舰`：与第 26、27 页最新目标价格及 Olares One `$3,999` 零售价不一致。
- 删除 “Arc Pro B70 与 Panther Lake 同场发布” 等 Intel 已熟知且不影响决策的信息。
- 删除对未来加速器厂商的预设；只说明当前器件选择、板载集成工程约束和厂商中立的准入条件。

## 来源

- [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md)
- [Olares 产品定位与 Olares One 规格](../../basic/olares.md)
- [Olares One 第一方实测](../../directions/hardware/research/olares-one-benchmarks.md)

