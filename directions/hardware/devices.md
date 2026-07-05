# hardware/devices.md — 加速硬件 / 整机 / NAS 竞品清单

> 对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 4（加速硬件设备与整机）。每个品牌/设备的报告在 [reports/](/Users/pengpeng/seo/directions/hardware/reports)，用来找"home ai server / linux mini pc / X alternative / X vs Olares One"这类内容切入点。清单手工维护（无生成器），来源见 [README.md](/Users/pengpeng/seo/directions/hardware/README.md)。

状态：✅ 已有报告（数据为历史快照，引用前需重跑核实）。多品牌合并报告在清单里逐品牌列、指向同一文件。**重点人群＝专业/旗舰独显 prosumer（RTX 4090/5090/RTX PRO 6000）、Apple Silicon（Mac Studio/Mini）、Spark / Strix Halo 整机；游戏本与掌机（Ally X/Legion Go/MSI Claw 等）不是目标场景。** 内容待用户后续修订。

## AI Mini PC / 工作站

| 品牌 / 设备 | 场景 | Olares One 对标角度 | 报告 |
|------------|------|--------------------|------|
| Beelink | AI Mini PC / Home NAS | 一体机替代，开箱即用私有 AI | ✅ [beelink](/Users/pengpeng/seo/directions/hardware/reports/beelink.md) |
| GMKtec | AI Mini PC / Strix Halo | Strix Halo 本地 AI 主机 | ✅ [gmktec](/Users/pengpeng/seo/directions/hardware/reports/gmktec.md) |
| Minisforum | AI Mini PC / 工作站 | mini pc linux / home server | ✅ [minisforum](/Users/pengpeng/seo/directions/hardware/reports/minisforum.md) |
| ASRock | 主板 / 显卡 / AI BOX（Strix Halo） | AI BOX 整机替代 | ✅ [asrock](/Users/pengpeng/seo/directions/hardware/reports/asrock.md) |
| Framework | 模块化 AI 笔记本 / Ryzen AI Max 桌面 | 开放硬件 AI 主机，用户高度重叠 | ✅ [framework](/Users/pengpeng/seo/directions/hardware/reports/framework.md) |
| System76 | Linux 工作站 / Pop!_OS / AI 工作站 | linux mini pc / 欧洲市场 | ✅ [system76](/Users/pengpeng/seo/directions/hardware/reports/system76.md) |

## AI 加速整机 / Apple Silicon（首要人群）

> Olares 首要人群：已为算力付费的 prosumer——大显存独显（见下「独显 / GPU」组）、Apple Silicon、桌面 AI 超算。缺的是"把已有算力变成可远程访问、多应用共享的私有 AI 服务"的软件层。

| 品牌 / 设备 | 场景 | Olares One 对标角度 | 报告 |
|------------|------|--------------------|------|
| NVIDIA DGX Spark / RTX Spark | 桌面 AI 超算 / 128GB 统一内存 | dgx spark alternative，整机正面对标 | ✅ [nvidia-dgx](/Users/pengpeng/seo/directions/hardware/reports/nvidia-dgx.md) |
| Apple Silicon Mac Studio / Mac Mini / MacBook | 统一内存本地 LLM（120-546 GB/s） | mac studio / mac mini local llm，缺私有云层 | ✅ [apple-silicon](/Users/pengpeng/seo/directions/hardware/reports/apple-silicon.md) |

## 独显 / GPU（本地 LLM 核心硬件）

> 已买大显存卡的用户是最高意图人群，切入点是"把显卡变成随处可用的私有 AI 服务"。每型号/系列一份调研（关键词量待 Semrush 补）。

| GPU | 显存 | 场景 / 切入词 | 报告 |
|-----|------|-------------|------|
| RTX 50 系（5090 32GB … 5060） | 8-32GB | rtx 5090 llm / 5090 vs 4090 | ✅ [rtx-50-series](/Users/pengpeng/seo/directions/hardware/reports/rtx-50-series.md) |
| RTX 4090 | 24GB | rtx 4090 llm / run llm on 4090 | ✅ [rtx-4090](/Users/pengpeng/seo/directions/hardware/reports/rtx-4090.md) |
| RTX 3090 / 3090 Ti | 24GB | 二手 24GB 性价比 / dual 3090 llm | ✅ [rtx-3090](/Users/pengpeng/seo/directions/hardware/reports/rtx-3090.md) |
| AMD Radeon 高端（7900 XTX / 9070 XT） | 16-24GB | amd gpu llm / rocm ollama | ✅ [radeon-high-end](/Users/pengpeng/seo/directions/hardware/reports/radeon-high-end.md) |
| Intel Arc（B580 / Arc Pro B60 24GB） | 12-24GB | intel arc llm / 最便宜大显存 | ✅ [intel-arc](/Users/pengpeng/seo/directions/hardware/reports/intel-arc.md) |
| RTX PRO 6000 Blackwell | 96GB | 工作站单卡王 / vs dgx spark | ✅ [rtx-pro-6000](/Users/pengpeng/seo/directions/hardware/reports/rtx-pro-6000.md) |

**按显存/预算选卡（速查）：** 8GB 仅 7B；12GB→13B；16GB→30B Q4；24GB（3090/4090/7900 XTX）→70B Q4；32GB（5090）→70B 流畅；96GB（PRO 6000）/ 128GB 统一内存（Mac / Spark）→120B+。

## 大厂 PC / 工作站（只看 AI 相关线）

> 这些大厂本质是游戏/掌机品牌；对 Olares 有意义的只是它们的 **Strix Halo / Ryzen AI / Core Ultra / 移动工作站 + 大显存独显本**，游戏本与掌机（Ally X、Legion Go、MSI Claw 等）不是目标场景。

| 品牌 | AI 相关线 | Olares One 对标角度 | 报告 |
|------------|----------|--------------------|------|
| ASUS | Flow Z13 · Zenbook S（Strix Halo / Ryzen AI）、ProArt 工作站 | Strix Halo 128GB 本地 AI | ✅ [asus](/Users/pengpeng/seo/directions/hardware/reports/asus.md) |
| HP | ZBook Ultra（Strix Halo 移动工作站）+ Z 系 | Strix Halo 移动 AI 工作站 | ✅ [hp-omen](/Users/pengpeng/seo/directions/hardware/reports/hp-omen.md) |
| Lenovo | ThinkStation / ThinkPad（Ryzen AI / Core Ultra） | 本地 AI 工作站对比 | ✅ [lenovo](/Users/pengpeng/seo/directions/hardware/reports/lenovo.md) |
| Dell | XPS / Precision 工作站（Core Ultra） | 本地 AI 工作站对比 | ✅ [dell-alienware](/Users/pengpeng/seo/directions/hardware/reports/dell-alienware.md) |
| Acer | Swift AI / 工作站笔记本（Core Ultra / Ryzen AI） | 本地 AI 主机对比 | ✅ [acer](/Users/pengpeng/seo/directions/hardware/reports/acer.md) |
| MSI | AI 工作站主板 / 显卡生态 | 本地 AI 主机 / 显卡生态 | ✅ [msi](/Users/pengpeng/seo/directions/hardware/reports/msi.md) |
| Razer | Blade（大显存独显笔记本） | 大显存本地 AI 笔记本对比 | ✅ [razer](/Users/pengpeng/seo/directions/hardware/reports/razer.md) |

## NAS 系统 / 整机竞品

| 品牌 / 设备 | 场景 | Olares One 对标角度 | 报告 |
|------------|------|--------------------|------|
| Synology | 最大 NAS 品牌 | synology alternative，本地私有云迁移 | ✅ [synology](/Users/pengpeng/seo/directions/hardware/reports/synology.md) |
| QNAP | 主流 NAS 品牌 | qnap vs synology，本地私有云迁移 | ✅ [qnap](/Users/pengpeng/seo/directions/hardware/reports/qnap.md) |
| TrueNAS | 开源 NAS OS + 自有硬件 | 私有云 OS 对比 | ✅ [truenas](/Users/pengpeng/seo/directions/hardware/reports/truenas.md) |
| Unraid | NAS / 家庭服务器 OS | 自托管 OS 对比 | ✅ [unraid](/Users/pengpeng/seo/directions/hardware/reports/unraid.md) |
| CasaOS | 轻量家庭云 OS（IceWhaleTech） | 个人云 OS 对比 | ✅ [casaos](/Users/pengpeng/seo/directions/hardware/reports/casaos.md) |
| Umbrel | 家庭服务器 OS + umbrel-home 硬件 | 个人云 OS + 一体机对比 | ✅ [umbrel](/Users/pengpeng/seo/directions/hardware/reports/umbrel.md) |
| ZimaOS / ZimaCube | 个人云 OS + NAS 整机（IceWhaleTech） | 最直接竞品，软硬一体对标 | ✅ [zimaos-zimacube](/Users/pengpeng/seo/directions/hardware/reports/zimaos-zimacube.md) |
| Asustor | NAS 品牌 | asustor vs synology 三方横评 | ✅ [asustor](/Users/pengpeng/seo/directions/hardware/reports/asustor.md) |
| TerraMaster | 性价比 NAS 品牌（中国） | terramaster vs synology（KD=3） | ✅ [terramaster](/Users/pengpeng/seo/directions/hardware/reports/terramaster.md) |
| UGREEN NAS | AI NAS 新兴品牌（中国） | ugreen ai nas，ugreen nas vs synology | ✅ [ugreen-nas](/Users/pengpeng/seo/directions/hardware/reports/ugreen-nas.md) |
| WD My Cloud | 家用 NAS / 云存储（西数） | my cloud home 对比 | ✅ [wd-mycloud](/Users/pengpeng/seo/directions/hardware/reports/wd-mycloud.md) |
| 极空间 ZSpace | AI NAS 软硬一体（中国） | 中国市场最直接竞品，价值主张重叠 | ✅ [zspace](/Users/pengpeng/seo/directions/hardware/reports/zspace.md) |
| AI NAS 新兴品牌 | UGREEN / 极空间 / 小米等 AI-Native NAS | 新兴品牌格局综述 | ✅ [ai-newbrands](/Users/pengpeng/seo/directions/hardware/reports/ai-newbrands.md) |

> DGX/RTX Spark 与 Strix Halo 平台关键词见 [nvidia-dgx](/Users/pengpeng/seo/directions/hardware/reports/nvidia-dgx.md) 与 [gmktec](/Users/pengpeng/seo/directions/hardware/reports/gmktec.md)；通用本地 AI 硬件词见 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 4。

---
> 共 34 份报告（含 7 份 GPU/Apple per-product 调研，关键词量待 Semrush 补）。写新报告或重跑数据走 `.cursor/skills/brand-seo-research/`（GPU 以型号为 brand；重写前先读旧报告、保留去重旧洞见）。
