# Hunyuan3D 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：Tencent Hunyuan / github.com/Tencent-Hunyuan/Hunyuan3D-2，Tencent Hunyuan Community License（排除 EU/UK/KR）
> 无独立产品官网（主战场：3d.hunyuan.tencent.com 演示站 + HuggingFace spaces/tencent/hunyuan3d-2 + ComfyUI 生态）；跳过 Phase 1 域名报告，降级模式。

## 模型理解（前置）

Hunyuan3D 2.1 是腾讯 Hunyuan 团队发布的开源 3D 生成模型，分为两阶段管线：**Shape 模型（3.3B，文本或图像→多视角一致的 3D 形状）** + **Paint 模型（2B，为已生成形状上色 UV 纹理）**，支持文生 3D、图生 3D 及带纹理完整输出，是目前最强的可本地部署的开源文+图生 3D 模型之一。其独特组件 **Hunyuan3D-PolyGen**（多边形网格输出）让生成结果直接可导入 Blender/Unity/Unreal，对比 Meshy/Tripo 等按积分收费的闭源 SaaS 是零成本的开源替代。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源文+图→带纹理 3D 生成，Shape 3.3B + Paint 2B，Meshy/Tripo/Rodin 本地平替 |
| 许可证 | **Tencent Hunyuan Community License**（**排除 EU/UK/KR 商业部署**；个人研究与非商业自托管不受限；引用前以官方 LICENSE 为准） |
| 主仓库 / 分发 | GitHub `Tencent-Hunyuan/Hunyuan3D-2`（★ 10K+），HuggingFace `tencent/Hunyuan3D-2`，演示站 3d.hunyuan.tencent.com，ComfyUI 节点 `comfyui-hunyuan3d-2-1` |
| 参数 / VRAM 可跑性 | Shape 3.3B + Paint 2B；全精度约 12–16GB；FP16 + offload：8–10GB（RTX 4070 8GB 可尝试）；**Olares One（RTX 5090 Mobile 24GB）：Shape + Paint 全精度流畅跑，无量化妥协** |
| 变体 / 型号 | Hunyuan3D-2.1（当前主力）、Hunyuan3D-2.0（基础版）、Hunyuan3D-PolyGen（多边形网格输出）、Hunyuan3D-Paint-v2-0（纹理子模型）；社区已有 2.5/3.0 搜索预期 |
| 闭源对标 | Meshy AI（$20–$120/月积分制）/ Tripo AI（按积分收费）/ Rodin AI（Hyper 按次付费）/ CSM 3D |
| Olares Market | ComfyUI ✅ 已上架（[报告](/Users/pengpeng/seo/directions/market/reports/comfyui.md)）；Hunyuan3D 2.1 通过 ComfyUI 节点 `comfyui-hunyuan3d-2-1` 部署，无需独立 Olares 应用 |
| 来源 | [GitHub Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)、[HuggingFace tencent/Hunyuan3D-2](https://huggingface.co/tencent/Hunyuan3D-2)、[官方演示站](https://3d.hunyuan.tencent.com) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。Intent：0=商业 / 1=信息 / 2=导航 / 3=交易。

### 品牌 / 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| hunyuan3d-2 | 2,900 | 65 | $1.26 | 1,3 |
| hunyuan3d | 1,900 | 58 | $1.53 | 1 |
| hunyuan 3d | 1,900 | 61 | $1.53 | 1 |
| hunyuan 3d 2.5 | 1,600 | 56 | $1.84 | 1 |
| hunyuan 3d model | 1,300 | 48 | $1.30 | 1 |
| hunyuan3d-polygen ⭐ | 880 | 24 | $0.00 | 1 |
| hunyuan3d-2.5 | 720 | 41 | $0.96 | 1 |
| hunyuan3d-2.1 ⭐ | 590 | 41 | $1.26 | 1,3 |
| hunyuan 3d 3.0 ⭐ | 590 | 16 | $1.19 | 1 |
| tencent hunyuan3d | 210 | 59 | $1.69 | 2 |
| hunyuan3d 2.0 | 390 | 62 | $1.26 | 1 |
| hunyuan3d-3 ⭐ | 260 | 22 | $2.84 | 1 |
| comfyui-hunyuan3d-2-1 ⭐ | 260 | 32 | $0.00 | 1 |
| hunyuan3d 2 | 260 | 56 | $1.26 | 1 |
| hunyuan3d 3.0 ⭐ | 140 | 20 | $1.39 | — |
| hunyuan3d 2.1 | 110 | 37 | $1.26 | 1 |
| hunyuan3d polygen ⭐ | 40 | 24 | $1.67 | 1 |
| hunyuan3d 2.1 comfyui ⭐ | 40 | 0 | $0.00 | — |

*注：hunyuan 3d 2.5（1,600/月）和 hunyuan 3d 3.0（590/月）的搜索量表明社区已在关注下一代版本，KD 分别为 56 与 16——3.0 版本词 KD 极低，属于抢先布局窗口。*

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| comfyui-hunyuan3d-2-1 ⭐ | 260 | 32 | $0.00 | 1 |
| hunyuan3d 2.1 comfyui ⭐ | 40 | 0 | $0.00 | — |
| hunyuan3d comfyui | 20 | 0 | $0.00 | — |
| hunyuan3d blender | 20 | 0 | $0.00 | — |
| hunyuan3d api | 20 | 0 | $0.00 | — |

*注：`hunyuan3d ollama` / `hunyuan3d vllm` 月量为 0——Hunyuan3D 是扩散式 3D 生成模型，不走 Ollama/vLLM 文本推理路径；ComfyUI 是主流本地部署引擎，Blender 插件/Python API 为辅助通路。*

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| hunyuan3d local | 0 | — | — | — |
| run hunyuan3d locally | 0 | — | — | — |
| hunyuan3d vram | 0 | — | — | — |
| hunyuan3d install | 0 | — | — | — |
| hunyuan3d fp16 | 0 | — | — | — |

*注：本地部署词几乎全为零量——属 GEO 抢发最优窗口，AI Overview / Perplexity 引用位尚无竞争者占据。*

### 对比 / 替代词（竞品对比）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|-----|-----|------|
| ai 3d model generator | 6,600 | 60 | $1.20 | 1,0 |
| meshy ai | 27,100 | 58 | $2.13 | 2 |
| tripo3d | 8,100 | 44 | $0.30 | 2 |
| tripo ai | 5,400 | 48 | $2.28 | 2 |
| shap-e | 2,900 | 56 | $1.63 | 1,0 |
| rodin ai ⭐ | 2,400 | 30 | $2.14 | 1 |
| text to 3d model | 720 | 60 | $1.07 | 1 |
| trellis 3d | 880 | 55 | $1.53 | 1 |
| rodin 3d | 590 | 48 | $2.41 | 1 |
| image to 3d ai | 390 | 76 | $1.23 | 0 |
| ai game asset generator ⭐ | 70 | 53 | $1.53 | 1 |
| open source 3d ai ⭐ | 50 | 0 | $0.00 | — |
| text to 3d ai | 70 | 50 | $1.48 | 1 |
| meshy alternative | 0 | — | — | — |
| open source text to 3d | 20 | 0 | $0.00 | — |
| open source image to 3d | 20 | 0 | $0.48 | — |

*注：`meshy alternative` 月量为 0——机会词，Meshy 品牌词（27,100/月）极旺，替代词搜索尚未形成；这意味着"meshy alternative open source"等长尾词是 GEO 抢发的纯空白地带。*

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|-----|-----|-------------|--------|
| comfyui-hunyuan3d-2-1 | 260 | 32 | $0.00 | Olares Market 已上架 ComfyUI，直接安装节点即可运行完整 Shape+Paint 管线；KD=32 可争，是 Hunyuan3D 本地部署的第一入口词 | ⭐⭐⭐ |
| hunyuan3d-polygen | 880 | 24 | $0.00 | PolyGen 输出可直接导入 Blender/Unity/Unreal，是游戏资产流程的核心；KD=24 极低，是全表性价比最高的低 KD 有量词——Olares 本地生成游戏资产叙事的精准入口 | ⭐⭐⭐ |
| hunyuan3d 3.0 / hunyuan3d-3 | 590+260 | 16/22 | $1.19/$2.84 | 下一代版本词 KD 极低（16/22），搜索已先行——GEO 抢占后，Olares 可作为"持续本地更新、无需切换云端订阅"叙事的载体 | ⭐⭐⭐ |
| meshy ai | 27,100 | 58 | $2.13 | Meshy 是最大商业对标（月量 27K），KD=58 高但品牌词多为导航意图——通过对比文（hunyuan3d vs meshy、open source meshy alternative）拿到侧翼流量；Olares 无积分限制是核心攻击点 | ⭐⭐ |
| rodin ai | 2,400 | 30 | $2.14 | KD=30 接近低 KD 阈值，CPC=$2.14 显示高商业价值；Rodin 按次付费，Olares 本地部署零边际成本；是 Hunyuan3D 对比文的优先靶词 | ⭐⭐⭐ |
| open source 3d ai | 50 | 0 | $0.00 | 月量小但 KD=0，零竞争；品类定性词，GEO 覆盖后可锁定 AI Overview 第一位 | ⭐⭐ |
| ai game asset generator | 70 | 53 | $1.53 | 游戏资产生成高商业意图词，Olares + Hunyuan3D 2.1 PolyGen 输出直接命中；KD=53 较高但 CPC 高说明值得争 | ⭐⭐ |
| hunyuan3d local | 0 | — | — | 零量 GEO 窗口；部署意图精准，Olares One 24GB 是最舒适的消费级本地运行配置 | ⭐⭐ |
| meshy alternative | 0 | — | — | 纯空白位——Meshy 品牌极旺（27K）但替代词尚未形成搜索规模；提前布局"open source meshy alternative"类内容，等流量爆发时已有权威页面 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|-----|-----|------|------|---------------------------|
| hunyuan3d-2 | 2,900 | 65 | $1.26 | 信息,交易 | 主词候选 | 品牌最高量词，KD=65 难拿首位，适合做锚点介绍页/教程 |
| hunyuan3d | 1,900 | 58 | $1.53 | 信息 | 主词候选 | 与 hunyuan 3d 是拼写变体，合并优化；KD=58 适合教程型内容 |
| hunyuan 3d | 1,900 | 61 | $1.53 | 信息 | 主词候选 | 带空格版本，等量；与 hunyuan3d 合并覆盖 |
| hunyuan 3d 2.5 | 1,600 | 56 | $1.84 | 信息 | 次级 | 未来版本预期词，KD=56；可在 2.1 报告中预埋 2.5 升级叙事 |
| hunyuan 3d model | 1,300 | 48 | $1.30 | 信息 | 主词候选 | 泛型查询词，KD=48 可争；表达"要 3D 模型"的用户意图 |
| hunyuan3d-polygen ⭐ | 880 | 24 | $0.00 | 信息 | **次级 ⭐** | KD=24 全表最低有量词之一；PolyGen 是 Hunyuan3D 最独特的差异化组件，游戏资产叙事入口 |
| hunyuan3d-2.5 | 720 | 41 | $0.96 | 信息 | 次级 | 下一版本型号词，KD=41；2.1 教程中自然预埋 |
| hunyuan3d-2.1 ⭐ | 590 | 41 | $1.26 | 信息,交易 | **次级 ⭐** | 当前版本精确词，KD=41 可争；是最核心的型号词 |
| hunyuan 3d 3.0 ⭐ | 590 | 16 | $1.19 | 信息 | **GEO ⭐⭐** | KD=16 极低，量=590 不算小——社区已在期待 3.0；GEO 抢发锁位，Olares 可作"本地持续更新"叙事载体 |
| rodin ai ⭐ | 2,400 | 30 | $2.14 | 信息 | **次级 ⭐** | KD=30 接近低 KD 阈值，CPC=$2.14 高；Rodin 是 Hunyuan3D 最接近的竞品量级，对比文优先靶词 |
| comfyui-hunyuan3d-2-1 ⭐ | 260 | 32 | $0.00 | 信息 | **次级 ⭐** | KD=32，月量=260；Olares Market ComfyUI 一键部署叙事的直接入口词，是最短部署路径 |
| hunyuan3d-3 ⭐ | 260 | 22 | $2.84 | 信息 | **GEO ⭐** | KD=22，量=260，CPC=$2.84 高商业意图；未来版本词，GEO 抢发可在 3.0 发布前锁定引用位 |
| ai 3d model generator | 6,600 | 60 | $1.20 | 信息,商业 | 主词候选 | 品类最高量词但 KD=60；长尾侧翼词更易突破，此词作为导流目标 |
| tripo3d | 8,100 | 44 | $0.30 | 导航 | 次级 | 竞品导航词，KD=44；对比文（hunyuan3d vs tripo）可截获竞品受众 |
| open source 3d ai ⭐ | 50 | 0 | $0.00 | 信息 | **GEO ⭐** | KD=0 全表最低，零竞争；品类定性词，一篇覆盖文可锁定 AI Overview 第一位 |
| meshy alternative | 0 | — | — | — | **GEO ⭐** | 当前零量但 Meshy 品牌词 27K 极旺；替代词是下一个爆发点，提前布局"open source meshy alternative"等变体 |
| hunyuan3d local | 0 | — | — | — | **GEO ⭐** | 零量 GEO 窗口；部署意图精准，Perplexity/ChatGPT 引用位先占 |
| run hunyuan3d locally | 0 | — | — | — | **GEO ⭐** | 零量但语义精准；随模型传播可预期增长，Olares 一键部署叙事最自然落点 |

---

## 核心洞见

### 1. 搜索心智是否建立

**已建立，且 2.1 版本词仍在增长期，下一代版本预期词已提前爆发。** "hunyuan3d" + "hunyuan 3d" US 月均合计约 3,800/月，"hunyuan3d-2"（最常用的 GitHub 风格写法）独立达 2,900——品牌认知初步成型，远超同章 TRELLIS（`trellis 3d` 880/月）但仍低于 Meshy（27K）约 7 倍。

一个关键异常：**"hunyuan 3d 2.5"（1,600/月，KD=56）和 "hunyuan 3d 3.0"（590/月，KD=16）的搜索量已经超过 "hunyuan3d 2.1"（590/月）**——说明社区的期待已经领先于当前版本的实际使用，这意味着内容布局必须同时覆盖当前版（2.1）和下一代词（2.5/3.0）。

**独特发现**：`hunyuan3d-polygen`（880/月，KD=24）是全表最值得关注的型号词——PolyGen 是 Hunyuan3D 与其他 3D 生成模型最大的差异化功能（直接输出可编辑多边形网格），月量接近型号词而 KD 仅 24。

### 2. 消费级 GPU / Olares One 能否本地跑

**完全可以，且门槛远低于视频生成模型。**

- **Shape 3.3B + Paint 2B**：两模型合计约 5–6B 参数，FP16 总显存需求约 12–16GB（比 HunyuanVideo 轻 40%+）。
- **RTX 4070 12GB**：在 offload 模式下可跑全管线（Shape 后 offload 再跑 Paint）。
- **RTX 4080/4090 16–24GB**：全精度流畅运行 Shape + Paint 完整管线。
- **Olares One（RTX 5090 Mobile 24GB）**：24GB GDDR7，可同时在 VRAM 内保存两个模型，Shape+Paint 顺序推理无需 CPU offload，生成速度最快——**是消费级中最舒适的 Hunyuan3D 2.1 运行配置**。
- **关键结论**：叙事完全成立。相比 Meshy（云端 API，按积分限量）或 Tripo（按次付费），Olares One 本地跑 Hunyuan3D 2.1 = 零边际成本生成游戏资产/3D 内容，Olares 平台 NVIDIA CUDA 支持最成熟，ComfyUI 已上架 Olares Market。

### 3. 许可证是否商用友好

**有条件友好，EU/UK/KR 限制是核心注意事项。** Tencent Hunyuan Community License 明确**排除 EU、UK、KR 的商业部署**。对 Olares 内容策略的含义：

- **不宜**在面向 EU/UK/KR 受众的文章中强推"用 Olares 跑 Hunyuan3D 做商业游戏资产"，但**个人自用/研究/非商业场景不受限**。
- **叙事侧重**：主打「本地部署 = 数据与生成内容完全私有，不受云端内容过滤」，而不是「商用友好可再分发」。
- **对比**：相比 TRELLIS（MIT 许可，商用无限制）和 Shap-E（MIT），Hunyuan3D 2.1 的许可证是弱点——在横评文中需如实标注；Olares 用户若要完全商用且无地区限制，TRELLIS 是备选。

### 4. 对 Olares 最关键的 2-3 个词

1. **`hunyuan3d-polygen`**（880/月，KD=24）：全表 KD 最低的有量词之一。PolyGen 直接输出 Blender/Unity/Unreal 可编辑的多边形网格，是游戏开发者/3D 艺术家选择 Hunyuan3D 而非 Meshy 的核心理由。Olares 本地无限量生成 PolyGen 资产，攻击面最清晰。
2. **`comfyui-hunyuan3d-2-1`**（260/月，KD=32）：ComfyUI 节点词，KD=32 可争。Olares Market 已上架 ComfyUI，一键安装节点即为完整 Shape+Paint 管线——是"从搜索到部署"最短路径的示范词。
3. **`rodin ai`**（2,400/月，KD=30）：竞品中 KD 最低（30）且 CPC 最高（$2.14）的有量词，商业意图最强。Rodin 是按次付费的高端 3D 生成服务，Hunyuan3D 本地部署 = 零边际成本的直接替代——对比文命中 Rodin 用户的痛点最精准。

### 5. 新模型 GEO 抢发窗口

| 词 | 量 | KD | 抢发理由 |
|----|---|---|---------|
| hunyuan 3d 3.0 | 590 | 16 | KD=16 全表最低有量词；下一代版本词空位，AI Overview 引用位先占 |
| hunyuan3d-3 | 260 | 22 | KD=22，CPC=$2.84 高意图；与 3.0 合并覆盖 |
| open source 3d ai | 50 | 0 | KD=0 零竞争；品类定性词，一篇覆盖即锁定 AI Overview 位 |
| meshy alternative | 0 | — | Meshy 27K 品牌量极旺，替代词下一个爆发；先占内容等流量 |
| hunyuan3d local | 0 | — | 部署意图精准，随模型普及将增长；Perplexity 引用位先占 |
| open source meshy alternative | 0 | — | 纯空白位；「开源 Meshy 替代」内容命中 Meshy 用户外溢 |
| hunyuan3d vram | 0 | — | 硬件选型问答，Olares One 规格直接命中 |

### 6. 闭源对标与攻击面

- **Meshy AI**（$20–$120/月，积分制）：月量最大（27K），按积分限量 + 云端生成数据上传隐私风险 + 内容过滤；Hunyuan3D 本地 = 无限量 + 数据不出机 + 无内容限制。`meshy alternative` 词目前量为 0 但品牌词极旺——对比内容护城河尚未建立，是抢占窗口。
- **Tripo AI / Tripo3D**（按积分付费，$14/月起）：强 3D 生成质量，但云端 API 依赖；Tripo3D 月量 8,100 / KD=44，是竞品中最适合做对比文的次选词。
- **Rodin AI**（Hyper 服务，按次高价）：高质量但高费用，CPC=$2.14 显示有商业意图用户；KD=30 最可争。Rodin 主打"生产级 3D 资产"，Hunyuan3D 2.1 PolyGen 在开源生态中是最近似替代。
- **通用攻击面**：三者均有「积分/配额限制导致批量生成受阻」「云端上传 IP/版权资产有隐私风险」「月费持续成本 vs 一次性本地部署」三个痛点；Hunyuan3D 2.1 + Olares 全部解决。
- **注意**：EU/UK/KR 商业用途受限是 Hunyuan3D 相比 TRELLIS（MIT）的弱点，对比文中需如实说明。

### 7. 与 model/models.md 同类 family 及跨报告关联

- **同章（04-3d）**：TRELLIS-2 ✅ 已有报告——`open source 3d ai`（KD=0）可作两份报告的 GEO 共同攻击词；TRELLIS 是 MIT 许可商用无限制的替代选项，与 Hunyuan3D 2.1 构成开源 3D 生成的互补叙事（一个强调无许可证限制，一个强调 PolyGen/纹理管线成熟度）。
- **跨章关联**：ComfyUI 在 market/reports ✅——Hunyuan3D、TRELLIS、HunyuanVideo 共享同一 ComfyUI 部署路径，可合并为「ComfyUI 本地 3D/视频 AI 一站安装」教程覆盖多个词。
- **闭源竞品**：Meshy / Tripo 若在 commerce/reports 建立报告，可从那些报告的高机会词反向引流至 Hunyuan3D 对比内容。
- **Keyword 簇建议**（给 seo-content 层）：`comfyui-hunyuan3d-2-1 + hunyuan3d local + run hunyuan3d locally` 可聚合为「在 Olares 上本地运行 Hunyuan3D 2.1」部署教程簇；`meshy alternative + open source meshy alternative + hunyuan3d vs meshy` 可聚合为「Meshy 开源替代方案」对比簇（GEO 先行）；`hunyuan3d-polygen + ai game asset generator + 3d model generator` 可聚合为「游戏资产本地生成」场景簇。

---

*数据来源：SEMrush US（phrase_these × 3 批次、phrase_fullsearch × 1 批次、phrase_related × 1 批次、phrase_questions × 1 批次）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
