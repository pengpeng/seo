# Intel CPU + 板载加速器

> 对外合作 PPT 第 28 页（Intel CPU + 单 PCBA 板载加速器 / 当前旗舰实现）。中文底稿；确认后补英文、HTML 与讲稿。
> 数据来自 [Olares One 第一方实测](../../directions/hardware/research/olares-one-benchmarks.md)；快照 2026-07，发布前复核。

---

## Slide copy（中文底稿）

### 标题

**Intel CPU + 板载加速器**

Olares One 是这条单 PCBA 路线的当前旗舰实现：Core Ultra 9 275HX + RTX 5090 Mobile，覆盖完整的云端已验证场景集，并在第一方测试集取得最佳综合性能与最广工作负载覆盖。

### 当前旗舰

**Intel Core Ultra 9 275HX** · NVIDIA RTX 5090 Mobile 24GB · 96GB RAM · 2TB NVMe · **$3,999**

### 三项第一方性能证明

#### 1. 多用户 LLM 吞吐

| 机型 | Qwen3-30B-A3B（并发 1 → 8，tok/s） |
|------|-------------------------------------|
| **Olares One** | **157 → 81** |
| Mac Studio M3 Ultra | 84 → 25 |
| Mac Studio M4 Max | 81 → 20 |
| Beelink GTR9 Pro（AMD 395+） | 61 → 12 |

#### 2. 图像生成

**Flux.1 dev：8.32 秒 / 张（热缓存）**  
Mac Studio M3 Ultra 约 73 秒；Olares One **快 8.8×**。

#### 3. 工作负载覆盖

**唯一跑完整套 LLM + 图像 + 视频测试的整机。**  
Olares One 可运行全部测试模型与 Flux、Wan 2.2、LTX-Video；其他对比机均有未完成项目。

### 七个云端已验证场景，一台旗舰

**Personal Agent · App Development · Audio · Image · Smart Home · AI Companion · Private Workspace**

---

## 工作底稿（备查）

- 本页展示的是单 PCBA 硬件路线：Intel CPU 与加速计算设备在同一张主板上集成，共享整机的供电、散热、噪音和尺寸封套。
- Olares One 当前采用 Core Ultra 9 275HX + RTX 5090 Mobile 24GB；这是当前实现，不把路线绑定为 NVIDIA 或任何第三方厂商。
- 未来满足板级功耗、散热、显存和软件要求的 Intel 或其他厂商加速器，都可以成为这条路线的实现。
- Arc Pro B70 是 160–290W 的 PCIe 工作站卡，属于第 26 页外置 GPU 路线，不适合直接放入 Olares One 这类单 PCBA 设计。
- 跑分来自 Olares 第一方测试，不写成第三方独立 benchmark。
- Qwen3-30B-A3B 使用 vLLM 的 Olares One 数据；对比平台采用其可用框架。主画面必须保留“第一方实测”口径。
- 性能结论统一为“第一方测试集最佳综合性能与最广工作负载覆盖”，不写“每个项目都最快”。
- 诚实边界：GPT-OSS-120B 超出 24GB VRAM，需要 offload；此项 Olares One 低于 Mac Studio M3 Ultra。该边界进入讲稿 / Q&A，不在主画面展开。
- `$2,999` 是众筹 / 测试时价格；对外主画面统一使用当前 `$3,999` 零售价。

## 删除的旧口径

- 删除 `Arc $/GB 仅 NVIDIA 三分之一`：第 26 页已决定不对外使用，且与本页当前产品无关。
- 删除 `$3,000 旗舰`：当前零售价为 `$3,999`。
- 删除对未来加速器厂商的预设；本页只陈述当前实现、单 PCBA 工程条件和厂商中立的准入要求。
- 删除“吞吐、图像生成全面领先”的宽泛表述，改为三项可核实的具体证明。

## 来源

- [Olares One 第一方实测](../../directions/hardware/research/olares-one-benchmarks.md)
- [registry.md](../../research/intel-coprocessor-slides-2026-07.notes/registry.md) §5
- [Olares 产品定位与 Olares One 规格](../../basic/olares.md)

## 后续交付顺序

1. 确认中文 slide copy、七场景与三项性能证明。
2. 生成英文 `slide.en.md`，作为 HTML 的唯一文案源。
3. 按 24–27 页设计系统制作 1280×720 HTML / PNG。
4. 补 3–5 分钟旗舰页讲稿，包含 120B 显存边界的 Q&A。
