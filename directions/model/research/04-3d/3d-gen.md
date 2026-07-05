# 开源 3D 生成（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 32 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 约 63% | 轮次: task-02（重排/收敛）

## 摘要

**结论先行——2026 年本地可跑的开源 3D 生成，综合"质量 × 可用性/成熟度 × 许可友好度 × 消费级可跑"最好的是这 5 个（主推，按序）：**

1. **TRELLIS.2-4B（微软）** — 图生 3D 的**开源天花板**，MIT 可无顾虑商用，PBR 质量与几何细节公认最强；16GB 可出 512³、社区 GGUF 量化可压到 6–8GB [1][2][23][24][30]。
2. **Hunyuan3D 2.1（腾讯）** — 唯一**同时覆盖文生+图生+多视图、且连训练代码一起开源**的主流系统，纹理保真上限最高；offload≈15GB 可在消费级跑，代价是 Community 许可有 MAU/地域限制 [4][5][6]。
3. **Stable Fast 3D / SF3D（Stability）** — **轻量档主推**：4–5GB 显存、~0.3–0.5s 直出 game-ready（UV+PBR+delighting）mesh，基准上几何精度与速度**全面优于 TripoSR** [10][11][31]。
4. **Hi3DGen（字节）** — **几何/高保真专项冠军**，MIT，以法线图为中间表示、拓扑干净，3D 打印与需精修网格首选 [7][17]。
5. **TripoSG（VAST-AI）** — **纯 MIT 的形状 SOTA**：1.5B、8GB 显存、单图出高保真 shape，官方称质量比肩闭源 Tripo 2.0，是中档纯开源许可的稳妥选择 [26][27][28][29]。

其余 5 个（初代 TRELLIS / TripoSR / Step1X-3D / Direct3D-S2 / PartCrafter）降级为"备选/特定用途"（见 §3，证据保留）。

关键取舍已核实：（a）图生 3D 天花板是 **TRELLIS.2 vs Hunyuan3D 2.1** 两强——TRELLIS.2 胜在 MIT 许可、更快、PBR 稳定，Hunyuan3D 胜在纹理上限、支持文生/多视图，但许可不纯 [24][32]；**Hunyuan3D 2.5/3.x 只有技术报告或商业平台，未发布可本地跑的开源权重**，故本地口径仍锁定 2.1 [25][32]。（b）轻量档 **SF3D > TripoSR**：SF3D 是 TripoSR 的直系升级，CD/F-score 更好、显存更低、直出 PBR，TripoSR 只在"生态最成熟、门槛最低"上保留价值，故 SF3D 主推、TripoSR 降为备选 [31][17][10]。

对 Olares 的意义很直接：3D 生成天然是"本地推理 + 数据留在本机"的强场景——素材版权、迭代速度、离线可用都利于自托管。**消费级单张 8–24GB GPU 已能跑起全部主推模型**（SF3D 4–5GB、TripoSG 8GB、TRELLIS.2/Hi3DGen 16GB、Hunyuan3D 2.1 offload≈15GB）[10][26][23][6]，正是"run X locally"类内容的低竞争洼地。

## 1. 型号总表（核心交付 · 主推/备选分列）

| 档 | 模型 | 代表型号 / 参数量 | 部署层级(显存) | 许可 | 闭源对标 | 候选关键词 |
|----|------|------------------|----------------|------|----------|-----------|
| 🥇主推1 | **TRELLIS.2**（微软）| TRELLIS.2-4B / 4B [1][2] | 💻 16GB@512³；官方≥24GB；GGUF 量化 6–8GB [2][23][24] | **MIT** [1] | Meshy / Rodin / Tripo | trellis 2, trellis 2 local, image to 3d open source |
| 🥈主推2 | **Hunyuan3D 2.1**（腾讯）| Shape 3.3B + Paint 2B [4] | 💻→🏢 offload≈15GB / full 29GB [4][6] | Tencent Community（<1M MAU 可商用，排除 EU/UK/KR）[5] | Meshy / Tripo / Rodin | hunyuan3d 2.1 local, text to 3d model, hunyuan3d comfyui |
| 🥉主推3 | **Stable Fast 3D**（Stability）| SF3D / 1.01B [11] | 📱 4–5GB [10][31] | Stability Community（营收<$1M 可商用）[11] | Meshy（游戏资产）| stable fast 3d, sf3d, game ready 3d ai |
| 主推4 | **Hi3DGen**（字节）| trellis-normal / ~1.2B 级 [7] | 💻 ~16GB [7][17] | **MIT** [7] | Rodin（几何）| hi3dgen, high fidelity 3d geometry, image to mesh |
| 主推5 | **TripoSG**（VAST-AI）| 1.5B（RF-DiT，2048 latent tokens）[26][28] | 📱 8GB [26][27] | **MIT** [26] | Tripo 2.0（形状）| triposg, image to 3d shape open source, triposg local |
| 备选 | **TRELLIS**（微软·初代）| image-large 1.2B / text-xlarge 2.0B [3] | 💻 ~16GB [17] | MIT [3] | Luma Genie | trellis 3d, text to 3d open source, run trellis locally |
| 备选 | **TripoSR**（VAST×Stability）| ~1.2GB 权重 [8][20] | 📱 6GB（最低 4GB）[8][20] | MIT [8] | Tripo（免费版）| triposr, triposr local, fast image to 3d |
| 备选 | **Step1X-3D**（StepFun）| 几何 1.3B + 纹理 3.5B [13] | 🏢 27–29GB [14] | 开源（全权重+训练码）[13] | Rodin / Tripo | step1x-3d, controllable 3d generation |
| 备选 | **Direct3D-S2**（DreamTech）| SSA / DiT，1024³ [15] | 🏢→💻 ~24GB @1024³ [15] | 开源（NeurIPS 2025）[15] | Rodin（高分辨率）| direct3d-s2, gigascale 3d generation |
| 备选 | **PartCrafter**（学界）| 组合式 latent DiT [16] | 💻 单图部件级 [16] | MIT [16] | —（部件可编辑独有）| partcrafter, part level 3d generation |

层级图例：📱 轻量（≤8GB）｜💻 消费级主力（单张 8–24GB）｜🏢 高显存（≥24GB 或多卡）。

## 2. 主推 5 个：排名依据（质量 × 可用性 × 许可 × 消费级可跑）

**#1 TRELLIS.2-4B — 图生 3D 开源天花板，且许可最干净。** 40 亿参数 vanilla-DiT + "field-free" O-Voxel 稀疏体素 VAE（16× 空间下采样），能处理开放曲面、复杂拓扑、锐利边缘与透明表面，一次输出带 PBR（BaseColor/Metallic/Roughness/Opacity）的 mesh，分辨率 512³–1536³；H100 上 512³≈3s、1024³≈17s、1536³≈60s [1][2][30]。四项优势叠加把它推到榜首：**质量**——多份第三方评测与 2026 学术综述都把它列为开源单图重建第一梯队 [24][30]；**许可**——MIT，游戏/商用零顾虑（这是它对 Hunyuan3D 的核心胜势）[1][24]；**消费级可跑**——官方建议 24GB/Linux，但社区 recipe 已在 16GB（RTX 4080/4090）出 512³，GGUF 量化进一步压到 6–8GB [2][23][24]；**成熟度**——已有 ComfyUI 节点与 wrapper 生态 [24]。短板是只吃单图、无文生。

**#2 Hunyuan3D 2.1 — 唯一"全模态 + 全开源含训练码"的全能系统。** 两段式 = Shape v2.1（3.3B 图生形状）+ Paint v2.1（2B PBR 纹理），同时支持文生 / 图生 / 多视图，是主推里唯一能"用文字描述出模型"的 [4][32]。官方基准里 Hunyuan3D-Shape-2.1 在 ULIP/Uni3D 指标上领先 TripoSG、Step1X-3D、Trellis、Direct3D-S2 [4]，**纹理上限公认最高**（第三方评测称其"hero asset 质量天花板"）[32]。**消费级可跑**——形状 10GB、纹理 21GB、合计 29GB，开 `low_vram_mode`（CPU offload）约 15GB，社区在 RTX 3090/4090 稳定运行 [4][6]。之所以排第 2 而非第 1：**许可不纯**——Tencent Community License，月活 <100 万可免费商用、超过需申请，且不适用于欧盟/英国/韩国 [5]；且更重的双阶段流程比 TRELLIS.2 慢 [32]。

**#3 Stable Fast 3D — 轻量档主推（明确胜过 TripoSR）。** 基于 TripoSR 的直系升级：把 64³ triplane 提到 384³、用 Marching Tetrahedron 替代 Marching Cubes，直出 **UV 展开 + PBR 材质 + delighting 的 game-ready mesh** [31]。基准上对 TripoSR **全面反超**：CD 0.098 vs 0.111、FS@0.1 0.701 vs 0.645，且更快（~0.3–0.5s）、显存更低（4–5GB vs 6–8GB）[31][10]。对"消费级/笔记本上即插即用做游戏资产"这一最高频本地场景，它是最优解；唯一保留项是 Stability Community 许可有年营收 <$1M 的商用上限 [11]。

**#4 Hi3DGen — 几何/高保真专项冠军，纯 MIT。** 字节（ICCV 2025，MIT），以法线图为中间表示、架构基于 TRELLIS（trellis-normal 权重），专攻高保真几何、干净拓扑，多份"最佳几何"评测点名它，适合 3D 打印与需要精修网格的场景 [7][17]。~16GB 消费级可跑。它主推的理由是"许可干净 + 补齐 TRELLIS.2/Hunyuan 在纯几何精度上的空档"，是与商业 Rodin 拉开差异的抓手。

**#5 TripoSG — 中档纯 MIT 形状 SOTA，8GB 门槛。** VAST-AI（arXiv 2502.06608，2025-03，**MIT**），1.5B rectified-flow DiT、2048 latent tokens，单图出高保真 shape；官方称质量"比肩闭源 Tripo 2.0、超越当时所有开源项目"，泛化与复杂组合体稳定性突出 [26][27][28][29]，2026 学术综述也把它列入开源单图重建代表模型 [30]。**8GB 消费级可跑 + MIT** 让它在"许可友好 × 低门槛"轴上很强；排第 5 是因为它**只出形状、不含纹理**（需外接 Paint 流程），全能性弱于前四，但作为纯开源许可的中档形状引擎值得主推。

> 说明：主推 5 个刻意覆盖了不同用途象限——图生天花板（TRELLIS.2）、全能+文生（Hunyuan3D 2.1）、轻量 game-ready（SF3D）、几何精修（Hi3DGen）、纯 MIT 形状（TripoSG），而非全挤在同一场景。

## 3. 备选 / 特定用途（证据保留，不主推）

- **TRELLIS 初代（微软，MIT）**——统一 SLAT 表示，可解码为辐射场 / 3D Gaussian / mesh，含 text-base 342M → text-xlarge 2.0B 文生型号，是"文生 3D + 中显存"的稳妥老将；已被 TRELLIS.2 在图生上超越，故降为备选 [3]。
- **TripoSR（VAST×Stability，MIT）**——最轻前馈单图重建（权重 1.2GB、6GB/最低 4GB、<0.5s），**生态最成熟**（100+ HF Spaces、两年生产验证、纯 MIT）；但输出偏顶点色、需更多清理，已被同门 SF3D 在质量/显存上反超，保留为"最低门槛 + 教学/最大社区"入口 [8][9][20][31]。
- **Step1X-3D（StepFun，开源全权重）**——几何 1.3B + 纹理 3.5B、27–29GB，偏高显存高保真，支持把 2D 的 LoRA 控制迁移到 3D；显存门槛高，特定"可控高保真"用途 [13][14]。
- **Direct3D-S2（DreamTech，NeurIPS 2025）**——Spatial Sparse Attention 把 1024³ gigascale 生成成本压低，~24GB 即可跑 1024 分辨率，用于"超高分辨率几何"专项 [15]。
- **PartCrafter（学界，NeurIPS 2025，MIT）**——单图一次生成多个语义部件、部件可独立编辑，"可拆解/可编辑资产"独门方向，非通用重建首选 [16]。

## 4. 候选 SEO 关键词与内容切入

- **型号词（低竞争、抢发窗口）**：`trellis 2` / `trellis 2 local` / `hunyuan3d 2.1 local` / `stable fast 3d` / `triposg` / `hi3dgen`——主推 5 个的型号词教程内容仍稀薄，是 GEO/SEO 抢发点 [1][26][7]。
- **意图词（本地部署）**：`image to 3d open source`、`text to 3d model local`、`run trellis 2 locally`、`self-hosted 3d generation`、`image to 3d on RTX 4090 / 16GB GPU`、`sf3d game ready mesh`——精准命中 Olares"本地推理"叙事 [23][10]。
- **替代/对比词（转化型）**：`Meshy alternative open source`、`Tripo alternative free`、`Rodin alternative self-hosted`、`TRELLIS 2 vs Hunyuan3D`、`SF3D vs TripoSR`、`best free image to 3d 2026`——闭源产品有付费/额度墙，"免费本地替代"是天然钩子 [17][24][32]。
- **内容切入建议**：①"在自己的 Olares 上跑 TRELLIS.2 / Hunyuan3D 2.1"部署教程（含显存/offload/GGUF 量化表）；②"消费级 GPU 3D 生成模型显存对照表 + 主推 5 选"（本报告总表可直接落地）；③"Meshy/Tripo 的开源本地替代 Top 5"对比长文；④"SF3D vs TripoSR：轻量图生 3D 谁该选"专题（基准数据直证 [31]）。

## 关键发现（3）

1. **主推收敛到 5 个，覆盖 4 象限、许可分两派**：MIT 派（TRELLIS.2 / Hi3DGen / TripoSG）可无顾虑商用，是推荐首选；"社区许可"派（Hunyuan3D 2.1 有 MAU/地域限制、SF3D 有营收上限）需在文中明确标注，避免误导商用读者 [1][7][26][5][11]。
2. **两大天花板已锁定本地口径**：图生 3D 由 **TRELLIS.2（许可/速度胜）** 与 **Hunyuan3D 2.1（纹理/多模态胜）** 双雄并立；Hunyuan3D 更高版本 2.5（arXiv 报告、最大 10B、LATTICE 形状模型）与商业平台的 3.x/8K PBR **均未放出可本地跑的开源权重**，故本地推荐仍只认 2.1 [24][25][32]。
3. **轻量档结论反转 = 内容机会**：SF3D 在 CD/F-score、速度、显存上**全面优于**其前身 TripoSR，且直出 PBR/UV——"轻量图生 3D 主推 SF3D、TripoSR 只作最低门槛入口"是一条有明确基准支撑、且与旧认知（TripoSR 是默认基线）相悖的可写点 [31][10]。

## 局限性

- 显存数字来自官方 README / 模型卡 / 第三方 recipe，为特定分辨率下的参考值，实际峰值随 octree/分辨率/batch 变化；消费级"可跑"多依赖 offload 或 GGUF 量化（量化会牺牲少量保真）[6][23][24]。
- 排名综合了官方基准（Hunyuan3D-Shape-2.1 的 ULIP/Uni3D 表、SF3D 的 CD/F-score）与第三方评测（trellis2.app、3daistudio、smeltcore、trify3d），后者带产品导流倾向，"最佳/最快"口径与官方基准不完全一致，参数以官方模型卡为准 [17][24][31][32]。
- **相反主张（已记入 Gaps）**：2026 学术综述《From Visual Synthesis to Interactive Worlds》明确指出，开源单图重建（TRELLIS.2 / SF3D / InstantMesh / TripoSG）在几何保真与表面细节上"总体仍逊于"闭源 Rodin Gen 1.5 / Tripo V2.5 / Hunyuan3D 3.1 / Meshy 5——即"开源已逼近但未追平 SOTA"，与部分产品博客"开源已追平商业"的说法相左 [30]。

## 参考文献

[1] microsoft/TRELLIS.2 (GitHub) — https://github.com/microsoft/TRELLIS.2
[2] microsoft/TRELLIS.2-4B 模型卡 (Hugging Face) — https://huggingface.co/microsoft/TRELLIS.2-4B
[3] microsoft/TRELLIS (GitHub README) — https://github.com/microsoft/TRELLIS
[4] Tencent-Hunyuan/Hunyuan3D-2.1 (GitHub) — https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1
[5] Hunyuan3D 2.1 Community License — https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1/blob/main/LICENSE
[6] Hunyuan3D-2.1 Python API / VRAM (DeepWiki) — https://deepwiki.com/Tencent-Hunyuan/Hunyuan3D-2.1/3.1-python-api
[7] bytedance/Hi3DGen (GitHub) — https://github.com/bytedance/Hi3DGen
[8] VAST-AI-Research/TripoSR (GitHub) — https://github.com/vast-ai-research/triposr
[9] TripoSR 技术报告 (arXiv 2403.02151) — https://arxiv.org/abs/2403.02151
[10] Stability-AI/stable-fast-3d (GitHub) — https://github.com/Stability-AI/stable-fast-3d
[11] stabilityai/stable-fast-3d 模型卡 (Hugging Face) — https://huggingface.co/stabilityai/stable-fast-3d
[12] Introducing Stable Fast 3D (Stability AI 博客) — https://stability.ai/news-updates/introducing-stable-fast-3d
[13] stepfun-ai/Step1X-3D (GitHub) — https://github.com/stepfun-ai/Step1X-3D
[14] Step1X-3D Installation Guide / VRAM (DeepWiki) — https://deepwiki.com/stepfun-ai/Step1X-3D/3-installation-guide
[15] DreamTechAI/Direct3D-S2 (GitHub) — https://github.com/DreamTechAI/Direct3D-S2
[16] wgsxm/PartCrafter (GitHub) — https://github.com/wgsxm/PartCrafter
[17] Best Image to 3D Models on HuggingFace (2026) — https://trellis2.app/blog/best-image-to-3d-models-huggingface
[18] Trellis 2 vs Hunyuan 3D (3DAI Studio) — https://www.3daistudio.com/blog/trellis-2-vs-hunyuan-3d-differences-explained
[19] Hunyuan3D 2.1 Guide (Clore.ai) — https://docs.clore.ai/guides/3d-generation/hunyuan3d
[20] Benchmarking TripoSR vs SOTA (axiomlogica) — https://axiomlogica.com/ai-ml/benchmarking-triposr-production-3d-generation-pipelines
[21] When Did TRELLIS 2 Come Out? (trellis2.app) — https://trellis2.app/blog/when-did-trellis-2-come-out
[22] Best AI 3D Model Generators in 2026 (trellis2.app) — https://trellis2.app/blog/best-ai-3d-model-generator
[23] TRELLIS on RTX 4090: High-Fidelity Image to 3D (smeltcore) — https://smeltcore.com/recipes/trellis-on-rtx-4090-high-fidelity-image-to-3d/
[24] Trellis 2 ComfyUI: Complete Install & Workflow Guide (trify3d) — https://trify3d.com/blog/trellis-2-comfyui
[25] Hunyuan3D 2.5 技术报告 (arXiv 2506.16504) — https://arxiv.org/abs/2506.16504
[26] VAST-AI-Research/TripoSG (GitHub) — https://github.com/VAST-AI-Research/TripoSG
[27] VAST-AI/TripoSG 模型卡 (Hugging Face) — https://huggingface.co/VAST-AI/TripoSG
[28] TripoSG 技术报告 (arXiv 2502.06608) — https://arxiv.org/abs/2502.06608
[29] VAST Open Source Month: TripoSG & TripoSF (Tripo3D 官方博客) — https://www.tripo3d.ai/blog/vast-open-source-month
[30] From Visual Synthesis to Interactive Worlds: 3D Asset Generation 综述 (arXiv 2604.23629) — https://arxiv.org/html/2604.23629v1
[31] SF3D: The Evolution from TripoSR（CD/F-score 基准）— https://didyouknowbg8.wordpress.com/2024/08/02/sf3d-the-evolution-from-triposr-in-single-image-3d-object-reconstruction/
[32] Pixal3D vs Trellis 2 vs Hunyuan 3D (3DAI Studio) — https://www.3daistudio.com/blog/pixal3d-vs-trellis-2-vs-hunyuan-3d-comparison
