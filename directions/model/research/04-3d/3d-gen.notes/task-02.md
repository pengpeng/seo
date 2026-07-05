---
task_id: 02
role: 3D 生成研究专员（重排/收敛）
status: complete
sources_found: 10 (new)
as_of: 2026-07-05
---

## Sources (本轮新增 [23]–[32]，沿用 task-01 编号)

[23] TRELLIS on RTX 4090: High-Fidelity Image to 3D (smeltcore) | https://smeltcore.com/recipes/trellis-on-rtx-4090-high-fidelity-image-to-3d/ | Source-Type: third-party-docs | As Of: 2026 | Authority: 5/10
[24] Trellis 2 ComfyUI: Complete Install & Workflow Guide (trify3d) | https://trify3d.com/blog/trellis-2-comfyui | Source-Type: third-party-blog | As Of: 2026 | Authority: 5/10
[25] Hunyuan3D 2.5 技术报告 (arXiv 2506.16504) | https://arxiv.org/abs/2506.16504 | Source-Type: official-academic | As Of: 2025-06 | Authority: 9/10
[26] VAST-AI-Research/TripoSG (GitHub) | https://github.com/VAST-AI-Research/TripoSG | Source-Type: official | As Of: 2025-04 | Authority: 10/10
[27] VAST-AI/TripoSG 模型卡 (Hugging Face) | https://huggingface.co/VAST-AI/TripoSG | Source-Type: official | As Of: 2025-03 | Authority: 10/10
[28] TripoSG 技术报告 (arXiv 2502.06608) | https://arxiv.org/abs/2502.06608 | Source-Type: official-academic | As Of: 2025-02 | Authority: 9/10
[29] VAST Open Source Month: TripoSG & TripoSF (Tripo3D 官方博客) | https://www.tripo3d.ai/blog/vast-open-source-month | Source-Type: official | As Of: 2025 | Authority: 7/10
[30] From Visual Synthesis to Interactive Worlds: 3D Asset Generation 综述 (arXiv 2604.23629) | https://arxiv.org/html/2604.23629v1 | Source-Type: official-academic | As Of: 2026 | Authority: 8/10
[31] SF3D: The Evolution from TripoSR（CD/F-score 基准）| https://didyouknowbg8.wordpress.com/2024/08/02/sf3d-the-evolution-from-triposr-in-single-image-3d-object-reconstruction/ | Source-Type: third-party-blog | As Of: 2024-08 | Authority: 4/10
[32] Pixal3D vs Trellis 2 vs Hunyuan 3D (3DAI Studio) | https://www.3daistudio.com/blog/pixal3d-vs-trellis-2-vs-hunyuan-3d-comparison | Source-Type: third-party-blog | As Of: 2026 | Authority: 5/10

## Findings（重排要点）

- **主推收敛到 5 个（排名）**：① TRELLIS.2-4B ② Hunyuan3D 2.1 ③ Stable Fast 3D ④ Hi3DGen ⑤ TripoSG。评分轴＝质量 × 可用性/成熟度 × 许可友好度 × 消费级可跑，刻意覆盖不同用途象限而非同一场景。[1][4][10][7][26]
- **图生 3D 天花板 = 双雄**：TRELLIS.2（4B，O-Voxel，MIT）与 Hunyuan3D 2.1（Shape 3.3B+Paint 2B，Community License）。多份对比：TRELLIS.2 胜在 MIT 许可、更快（1–3 min vs 2–6 min）、PBR 稳定；Hunyuan3D 胜在纹理上限、支持文生/多视图、可调多边形数。对 Olares（自托管、许可优先）TRELLIS.2 排第 1。[24][32]
- **TRELLIS.2 消费级门槛已下探**：官方 README 要求 ≥24GB/Linux/CUDA 12.4；第三方 recipe 在 16GB（RTX 4080/4090）出 512³；社区 GGUF 量化可到 6–8GB（牺牲少量保真）。DeepWiki：512³ 需 24GB、1024³ 需 40GB+ 为"最优"配置口径。[2][23][24]
- **Hunyuan3D 2.5/3.x 无本地开源权重**：arXiv 2506.16504（2025-06）仅为 Hunyuan3D 2.5 系统技术报告——引入 LATTICE 形状基座、最大 10B 参数——但**未发布可下载权重**；商业平台（3D AI Studio）宣传的 Hunyuan3D 3.5（2x 更快、8K PBR）同样无开源权重。故本地推荐锁定确证开源的 2.1。[25][32]
- **Hunyuan3D-Shape-2.1 官方基准领先同类**：README 对比表 ULIP-T/ULIP-I/Uni3D-T/Uni3D-I 上，Hunyuan3D-Shape-2.1（0.0774/0.1395/0.2556/0.3213）优于 Step1X-3D、Trellis、Direct3D-S2、TripoSG、Michelangelo、Craftsman。[4]
- **轻量档 SF3D > TripoSR（基准反转）**：SF3D 是 TripoSR 直系升级（triplane 64³→384³、Marching Cubes→Marching Tetrahedron）。基准：SF3D CD 0.098 / FS@0.1 0.701 / ~0.5s vs TripoSR CD 0.111 / FS@0.1 0.645 / 0.3s；axiomlogica 表给 SF3D 4–5GB、TripoSR 6–8GB。SF3D 直出 UV+PBR+delighting game-ready，故主推 SF3D、TripoSR 降为"最低门槛/最成熟生态"备选。[31][10][20]
- **新增强开源模型 TripoSG（VAST-AI，MIT，2025-03）**：1.5B rectified-flow DiT、2048 latent tokens、8GB 显存、单图出高保真 shape；官方称"质量比肩闭源 Tripo 2.0、超越当时所有开源项目"；2025-04 追加 TripoSG-scribble（512 token 快速原型）。纯 MIT + 8GB 门槛，纳入主推第 5（仅出形状、无纹理，故排第 5）。[26][27][28][29]
- **2026 学术综述佐证与反证**：arXiv 2604.23629 把 TRELLIS.2 / SF3D / InstantMesh / TripoSG 列为开源单图重建代表；同时明确"闭源系统（Rodin Gen 1.5 / Tripo V2.5 / Hunyuan3D 3.1 / Meshy 5）在几何保真与表面细节上总体仍优于开源"——即开源逼近未追平。[30]

## Deep Read Notes

### Source [25]: Hunyuan3D 2.5 arXiv 报告
- Key data: 沿用 2.0 两段式；新形状基座 LATTICE（scaled 数据+模型，最大 10B 参数）；PBR 纹理经多视图 pipeline 升级。仅报告，无权重下载入口。
- Key insight: 证实"2.5 不可本地跑"，锁定本地口径为 2.1，是重要的相反主张核查点。
- Useful for: 摘要天花板论述、关键发现 2、Gaps。

### Source [26][27][28][29]: TripoSG
- Key data: MIT；1.5B RF-DiT + 2048 latent-token VAE（SDF 表示 + 混合几何监督）；8GB VRAM；arXiv 2502.06608；GitHub 1.7k★，2025-03 发布、2025-04 加 scribble；官方博客称 on par with Tripo 2.0。
- Key insight: 纯 MIT + 消费级 8GB 的形状 SOTA，是本轮纳入的新主推；短板＝只出形状。
- Useful for: 型号总表主推5、§2 #5、SEO 型号词。

### Source [31][10][20]: SF3D vs TripoSR 基准
- Key data: SF3D CD 0.098/FS@0.1 0.701/~0.5s/4–5GB/PBR+UV+delight；TripoSR CD 0.111/FS@0.1 0.645/0.3s/6–8GB/顶点色。SF3D 用 DMTet + 高分辨率 triplane。
- Key insight: 轻量档主推应为 SF3D，TripoSR 降级——有明确基准支撑的结论反转，适合做 "SF3D vs TripoSR" 内容。
- Useful for: 关键发现 3、备选章、SEO 对比词。

### Source [23][24][32]: 第三方部署/对比
- Key data: smeltcore 16GB 最低跑 TRELLIS；trify3d 12GB 最低、16–24GB 推荐、GGUF 8GB、TRELLIS.2 vs Hunyuan3D 对比表；3daistudio Pixal3D/Trellis2/Hunyuan 三方对比（速度/许可/纹理分辨率）。
- Key insight: 天花板双雄取舍的第三方佐证；带产品导流倾向，数字以官方为准。
- Useful for: §2 排名依据、局限性、SEO 对比词。

## Gaps（相反主张 / 未决）

- **相反主张①（学术）**：arXiv 2604.23629 综述指出开源单图重建"几何保真/表面细节总体仍逊于"闭源 Rodin/Tripo/Hunyuan3D 3.1/Meshy 5——与产品博客"开源已追平商业"相悖。本报告采信"逼近未追平"。[30]
- **相反主张②（许可/口径）**：产品博客常把 Hunyuan3D 说成"more commercially permissive"（trify3d），但其 Community License 实有 <100 万 MAU 与排除 EU/UK/KR 的硬限制；相较之下 TRELLIS.2/Hi3DGen/TripoSG 的 MIT 才是真正"可无顾虑商用"。[24][5][1][26]
- **未决**：Hunyuan3D 2.5（10B/LATTICE）与商业 3.x（8K PBR）是否会放出本地权重未知；若放出将改写图生 3D 天花板排名。[25][32]
- **口径提示**：各显存数字随分辨率/octree/batch/量化变化，消费级"可跑"多依赖 offload 或 GGUF。[6][23]

## END
