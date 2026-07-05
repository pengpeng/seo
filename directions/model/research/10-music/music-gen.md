# 开源音乐生成（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 21 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: ~76%

## 摘要

到 2026 年年中，开源音乐生成已经过了"百模乱战"阶段，收敛出一个可以下结论的判断：**在"能自部署、可商用、消费级 GPU 跑得动、生态成熟"这四条约束下，ACE-Step 1.5（含 1.5 XL）是当前唯一值得主推的开源音乐生成模型**——这也是本轮唯一的推荐位。官方论文自评它在常用指标上"质量超过多数商业模型"、A100 <2 秒 / RTX 3090 <10 秒出整曲、基础版 <4GB VRAM 可跑、MIT 许可可商用 [1][2]；独立第三方 IT-JIM（2026-05 亲手加载八个开源模型盲测）也给出一致结论：**"ACE-Step 1.5 在研究、微调与下游工具链上胜出，且这一优势大到没有真正的第二名"**，MIT 代码+权重、Omni-Task 编辑能力、成熟社区生态使它成为"要在模型之上做东西"的事实基座 [16]。GitHub 11K+ star、80+ 贡献者、13 个 release、支持 Mac/AMD/Intel/CUDA，也印证其生态领先 [17]。

其余全部降级为"备选/特定用途"：**LeVo 2 / SongGeneration**（腾讯，音质最好但自定义**非商用**许可，不能商用发行）[16][17][18]、**YuE**（2025 血脉源头、Apache 2.0 可商用，但慢且高显存、音质普通）[5][16]、**HeartMuLa**（codec 设计新颖，但第三方盲测三种风格都"泛化成模糊流行乐"、仅 3B 权重实际发布）[16]、**DiffRhythm 2**（极速、Apache 2.0，但其论文自承人声/节奏落后 ACE-Step 与 LeVo）[8][16]、**SongBloom**（质量口碑好，但推理**必须喂 10 秒参考音频**，非纯文本）[19][20]、**Stable Audio Open Small**（唯一端侧，但只做短音效非整曲）[9][10]、**MusicGen/AudioGen**（经典基线，权重 CC-BY-NC 非商用、已被超越）[11][12]，另有 **Khala/Muse** 两个 2026 研究向新模型（非商用或纯语料贡献）[16]。

对 Olares（个人云、本地推理、需要"可商用+可私有部署+低显存"）而言，主推口径必须精确：**ACE-Step 1.5 是唯一同时满足"许可可商用（MIT）+ 消费级显存（<4GB 起）+ 生态最成熟"的选择**。需保留的相反证据：IT-JIM 盲测认为**纯音质冠军是 LeVo 2 而非 ACE-Step**，且 ACE-Step 1.5 存在贯穿全程的"金属感 shimmer"artifact [16]；但 LeVo 2 是腾讯自定义**非商用**许可、无法用于商业/生产 [17][18]——因此对"要落地、要卖、要私有部署"的用户，能用的最佳开源模型仍是 ACE-Step 1.5。正确对外口径是"接近 Suno、可商用、免费本地、生态最全"，而非"音质超越一切开源模型"。

## 1. 型号总表（核心交付）

### 🥇 主推（唯一推荐位）

| 模型 | 代表型号/参数量 | 部署层级 | 许可 | 闭源对标 | 候选关键词 |
|------|----------------|----------|------|----------|-----------|
| **ACE-Step 1.5** | 基础 2B DiT（<4GB VRAM）；**XL 4B DiT**（~9GB bf16，≥12GB 带 offload/≥20GB 无 offload）+ 5Hz FSQ tokenizer + Qwen3 系 LM planner（0.6B/1.7B/4B）；变体 base/sft/turbo/turbo-rl [1][2][3][21] | 💻 主力（基础 4–12GB）／🏢 XL（≥20GB 最佳） | **MIT（代码+权重均可商用，模型卡明文"可商用"）** [3][16] | Suno v5 / Udio | `ace-step 1.5`, `run ace-step locally`, `open source suno alternative`, `self-hosted ai music generator`（低竞争） |

### 🥈 备选 / 特定用途（降级，不主推）

> 每行末尾为**降级理由**——为什么它不是 Olares 的主推位。

| 模型 | 代表型号/参数量 | 部署层级 | 许可 | 降级理由（一句话） |
|------|----------------|----------|------|-------------------|
| **LeVo 2 / SongGeneration 2** | LeLM ~4B + Music-Codec DiT，最长 4m30s，VRAM 分档 10/22/28GB [16][17] | 🏢 高显存 | 腾讯自定义**非商用**（academic/research/education only）[17][18] | 第三方盲测音质最好，但**禁止任何商用/生产**，Olares 用户无法落地卖钱 |
| **YuE** | Stage1 7B + Stage2 1B（lyrics2song）[5][6] | 🏢 高显存（原生全曲 ≥80GB；量化 6–24GB 短片段） | Apache 2.0（可商用）[5] | 可商用，但 RTX 4090 上约 **12× 慢于实时**、显存门槛高、盲测音质不突出 [16] |
| **HeartMuLa** | 官方称 7B，**实际仅发布 3B** SKU；HeartCodec 12.5Hz + Llama-3.2 LM [16] | 🏢 高显存（16–24GB） | Apache 2.0（code）[14][16] | 第三方三风格盲测都"泛化成模糊流行乐"、7B 未发布——**修正上一版"音质最高"的说法** [16] |
| **DiffRhythm 2** | VAE+DiT 隐扩散，半自回归 Block Flow Matching [7][8] | 💻 消费级可跑 | Apache 2.0（可商用）[7][8] | 极速+可商用，但**论文 §5.2 自承人声质量落后 ACE-Step 与 LeVo**、节奏不稳 [8][16] |
| **SongBloom** | 2B，最长 150s（长版 4m）[19][20] | 💻 消费级可跑 | 官方 repo（tencent-ailab）[19] | 口碑好，但推理**必须提供 10 秒参考音频**、非纯文本→整曲，UX 与"文生歌"主线不符 [19][20] |
| **Khala** | 1.6B 主干 + 1.8B 超分 + 0.27B codec（~3.7B）[16] | 🏢 高显存 | CC BY-NC 4.0（**非商用**）[16] | 架构异类（纯声学、无语义层），但**非商用**且官方挂"质量不稳定"免责声明 [16] |
| **Muse** | 0.6B Qwen3 over MuCodec（纯 SFT）[16] | 💻 轻量 | MIT code / Apache-2.0 权重 / **MIT 训练语料** [16] | 亮点只在"7771h 全合成 Suno-V5 语料全公开"，模型本身刻意平庸，非可用旗舰 [16] |
| **Stable Audio Open Small** | 341M（DiT+T5，最长 11s，44.1kHz）[9][10] | 📱 轻量／端侧（Arm CPU、手机） | Stability AI Community（<$1M 营收免费商用）[9][10] | 唯一端侧，但面向**短音频/音效**而非整曲，做不了"本地 Suno" |
| **MusicGen / AudioGen** | 300M/1.5B/3.3B（+melody/stereo）；AudioGen 1.5B [11][12] | 💻 消费级（medium 16GB） | code MIT / **权重 CC-BY-NC（非商用）**[11][12] | 经典基线，但权重非商用、质量已被 2025–2026 新模型全面超越 |

## 2. 主推详解：ACE-Step 1.5（唯一推荐位）

- **为什么是它而不是别人**：开源音乐这一年出了 8+ 个模型，但只有 ACE-Step 1.5 同时满足 Olares 的四条硬约束——① 许可可商用（MIT，模型卡明文"You can strictly use the generated music for commercial purposes"）[16]；② 消费级显存（基础 2B DiT <4GB 就能跑，A100 <2s / RTX 3090 <10s 出整曲）[1][2]；③ 生态最成熟（GitHub 11K+ star、80+ 贡献者、13 releases、跨 Mac/AMD/Intel/CUDA、原生 LoRA 微调）[17]；④ 独立第三方背书（IT-JIM 亲手盲测后判定"研究/微调/下游工具链胜出，且大到没有第二名"）[16]。凡是能打的竞争者，要么非商用（LeVo 2、Khala、MusicGen 权重）、要么显存太高/太慢（YuE）、要么 UX 不对（SongBloom 需参考音频）、要么根本不做整曲（Stable Audio Open Small）。
- **架构**：混合 LM-planner + Diffusion-renderer。上游 Qwen3 系 LM 作"作曲规划器"，用 Chain-of-Thought 生成 BPM/调式/时长/结构标签/歌词/caption，交给 DiT（标准 2B / XL 4B）渲染 48kHz 立体声、10 秒到 10 分钟、跨 50+ 语言 [1][16]。独有卖点是**内在强化学习**（Attention Alignment Score + DiffusionNTF），奖励信号来自模型自身注意力几何，不依赖人类偏好数据或外部奖励模型——2026 slate 中独一份 [16]。
- **显存分层（做"分层"叙事的完美范例）**：≤6GB 仅跑 DiT（LM 禁用+INT8+CPU offload）；6–8GB 配 0.6B LM；8–16GB 配 0.6B/1.7B；16–24GB 起可上 XL；XL 4B DiT 需 ≥12GB（带 offload+量化）/ ≥20GB（无 offload）[2][3][21]。变体：`base`（全任务/高多样性）、`sft`（高质量）、`turbo`（8 步蒸馏、日常首选）、`turbo-rl`（待发布）[2]。
- **Omni-Task 编辑能力**：同一套 DiT 权重跑六种模式——文生曲、翻唱（cover）、局部重绘（repaint）、音轨提取（生成式分轨）、叠加配器（lego）、整曲补全（complete）；2026 slate 里没有第二个模型能用单套权重跑这么多编辑模式 [16]。这是"本地音乐工作台"内容切入的独家素材。
- **诚实的短板**：IT-JIM 盲测指出 ACE-Step 1.5 有贯穿人声与器乐的"金属感 shimmer"artifact（疑与 5Hz FSQ tokenizer 或低步数去噪有关），纯音质不如 LeVo 2 [16]。这不影响"可商用+可本地+生态最全"的主推地位，但对外别吹"音质第一"。

## 3. 备选为何降级（一句话汇总）

- **LeVo 2 / SongGeneration 2**：IT-JIM 盲测的**音质冠军**（三种风格最自然），但腾讯自定义许可"仅限学术/研究/教育、任何情况下禁止商用或生产"[17][18]——**这是它无法主推的唯一致命伤**。HF 模型卡显示 `license: unknown` 属误导，实际以 repo LICENSE 为准 [16][18]。
- **YuE**：2025 血脉源头、Apache 2.0 可商用、诚实写了 Limitations，但盲测音质不突出，RTX 4090 上约 12× 慢于实时、原生全曲 ≥80GB 显存 [5][16]。
- **HeartMuLa**：HeartCodec（12.5Hz 三编码器融合）设计有意思，但第三方三风格盲测都"泛化成模糊流行乐"，且**摘要吹 7B、实际只发 3B**——**据此修正上一版"HeartMuLa 音质最高"的 vendor 说法** [16]。
- **DiffRhythm 2**：Block Flow Matching 架构最新、Apache 2.0、极速，但**其论文 §5.2 自承人声质量落后 ACE-Step 与 LeVo**、节奏不稳，§6 更直言"开源整体仍不及商业系统" [8][16]。
- **SongBloom**：交错自回归+扩散、口碑不错、arXiv 2506.07634，但**推理必须喂 10 秒参考音频**才能定风格，落在"纯文本→整曲"主线之外 [19][20]。
- **Khala**：纯声学 64 层 RVQ、无语义层的架构异类，但 CC-BY-NC**非商用**+官方挂"质量不稳定"免责声明 [16]。
- **Muse**：真正贡献是"7771 小时全合成 Suno-V5 语料全 MIT 公开"（唯一全公开语料），模型本身刻意平庸的 0.6B baseline [16]。
- **Stable Audio Open Small**：唯一真端侧（Arm CPU/手机 <8s 出 11s 音频），但定位短音效/sound design，做不了整曲 [9][10]。
- **MusicGen / AudioGen**：经典基线，权重 CC-BY-NC 4.0 不可商用，质量已被新模型超越——只作"历史基线/为什么该换新模型"的对照 [11][12]。

## 4. 候选 SEO 关键词与内容切入

- **主推型号词（低竞争，优先抢）**：`ace-step 1.5`、`ace-step xl`、`ace-step vs suno`——新型号词竞争低、意图精准，做"是什么/参数/本地部署教程"页。
- **"run X locally" 系列（对准 Olares 本地推理）**：`run ace-step locally`、`self-hosted ai music generator`、`run suno alternative on your own gpu`、`ai music generator low vram`。
- **"Suno alternative" 系列（高流量，需长内容承接）**：`open source suno alternative`、`free suno alternative self-hosted`、`local suno alternative`、`best open source music ai 2026`——用"免费/私有/无限/可商用/生态全"差异化。
- **备选/长尾（承接对比文的次要落点）**：`levo 2 vs ace-step`、`diffrhythm 2`、`yue music model`、`songbloom`、`stable audio open small`、`text to sound effects model`——多数只值得在聚合对比文里带一笔，不单独重投。
- **内容切入建议**：①《Best open-source Suno alternatives you can self-host (2026)》聚合对比文，**结论明确指向 ACE-Step 1.5**（其余作对比陪衬，各给一句"为何不选"）；②《How to run ACE-Step 1.5 locally on your own cloud》教程（绑定 Olares 部署，收 "run locally" 词）。

## 关键发现（2-3）

1. **开源音乐已收敛到"唯一可主推 = ACE-Step 1.5"**：官方 eval 与独立第三方 IT-JIM 盲测在"研究/微调/工具链/生态"上结论一致，且第三方明说"优势大到没有第二名"[1][16]。对 Olares 这种要"可商用+可私有部署+消费级显存"的场景，其他模型要么非商用、要么太重、要么 UX 不对，主推位没有争议。
2. **"许可"是隐藏胜负手，压过纯音质**：纯音质冠军是 LeVo 2、架构最炫是 Khala，但两者都是**非商用**许可，MusicGen 权重也是 CC-BY-NC——真正能被 Olares 用户拿去商用/落地的高质量开源模型，绕来绕去只剩 MIT 的 ACE-Step 1.5 [16][17][18]。选型时"能否商用"比"音质高 0.3 分"更能筛掉候选。
3. **别再吹"超越 Suno"，要吹"可商用+本地+生态"**：DiffRhythm 2 论文自承"开源整体仍不及商业系统"，IT-JIM 也说"开源尚无真正的 Suno"[8][16]。ACE-Step 1.5 的正确卖点是"接近、免费、私有、无限次、可商用、工具链最全"，而不是音质超越——这恰好全落在 Olares 本地部署的价值主张上。

## 局限性

- 本轮为 Lightweight 网检，**未跑 Semrush**，关键词竞争度为定性判断，缺具体搜索量/难度数值。
- 音质排序（LeVo 2 > ACE-Step 1.5 …）来自 IT-JIM 单次"三 prompt×一 seed"的实践者盲测 [16]，非大样本 MOS；作者自陈样本量小、结论会随模型更新过时，权威度中等偏上（独立、亲手加载、方法透明）。
- 上一版依据 vendor 页 [14] 写的"HeartMuLa 音质最高、YuE 次之"结论，与本轮独立第三方盲测 [16] 冲突，正文已按 IT-JIM 口径修正（HeartMuLa 音质并不突出）。
- LeVo 2 无独立 arXiv 论文，架构主张多为 repo README 自述、尚无第三方复现 [16][17]；HeartMuLa 一手官方论文/权重仓库与确切参数量仍未取得。
- ACE-Step / DiffRhythm / SongBloom 的 arXiv 编号（2602.xxxxx / 2510.xxxxx / 2506.07634）以来源原文所载为准，引用前建议以 arXiv 页面复核。

## 参考文献

[1] ACE-Step 1.5: Pushing the Boundaries of Open-Source Music Generation (arXiv) — https://arxiv.org/html/2602.00744v1
[2] ace-step/ACE-Step-1.5 README (GitHub) — https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md
[3] ACE-Step/acestep-v15-xl-turbo Model Card (Hugging Face) — https://huggingface.co/ACE-Step/acestep-v15-xl-turbo/blob/main/README.md
[4] Diffusers ACE-Step pipeline docs (Hugging Face) — https://huggingface.co/docs/diffusers/main/api/pipelines/ace_step
[5] multimodal-art-projection/YuE (GitHub) — https://github.com/multimodal-art-projection/YuE
[6] m-a-p/YuE-s1-7B-anneal-en-icl (Hugging Face) — https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-icl
[7] ASLP-lab/DiffRhythm (GitHub) — https://github.com/ASLP-lab/DiffRhythm
[8] ASLP-lab/DiffRhythm2 (GitHub) — https://github.com/ASLP-lab/DiffRhythm2
[9] Stability AI & Arm — Stable Audio Open Small — https://stability.ai/news-updates/stability-ai-and-arm-release-stable-audio-open-small-enabling-real-world-deployment-for-on-device-audio-control
[10] stabilityai/stable-audio-open-small README (Hugging Face) — https://huggingface.co/stabilityai/stable-audio-open-small/resolve/main/README.md
[11] MusicGen Model Card (Meta FAIR / AudioCraft) — https://facebookresearch.github.io/audiocraft/model_cards/MUSICGEN_MODEL_CARD.html
[12] AudioGen Model Card (Meta FAIR / AudioCraft) — https://github.com/facebookresearch/audiocraft/blob/main/model_cards/AUDIOGEN_MODEL_CARD.md
[13] Suno vs Udio 2026 (Chartlex) — https://www.chartlex.com/blog/marketing/suno-vs-udio-2026
[14] ACE-Step 1.5 Review: HeartMuLa vs ACE-Step vs Suno 2026 (heart-mula.com) — https://heart-mula.com/ace-step
[15] ACE-Step 1.5 vs HeartMuLa: State of Local AI Music Generation 2026 (Medium) — https://medium.com/@aitoolscan/ace-step-1-5-vs-heartmula-the-state-of-local-ai-music-generation-in-2026-c37cb86351bf
[16] Best Open-Source AI Music Generators 2026 (IT-JIM, 独立盲测) — https://www.it-jim.com/blog/best-open-source-ai-music-generator/
[17] tencent-ailab/SongGeneration (LeVo 2) README (GitHub) — https://github.com/tencent-ailab/SongGeneration
[18] tencent/SongGeneration LICENSE (Hugging Face) — https://huggingface.co/tencent/SongGeneration/blob/main/LICENSE
[19] tencent-ailab/SongBloom (GitHub) — https://github.com/tencent-ailab/SongBloom
[20] SongBloom: Coherent Song Generation via Interleaved AR Sketching and Diffusion Refinement (arXiv 2506.07634) — https://arxiv.org/abs/2506.07634
[21] ACE-Step 1.5 XL released (GIGAZINE) — https://gigazine.net/gsc_news/en/20260409-ace-step-1-5-xl/
