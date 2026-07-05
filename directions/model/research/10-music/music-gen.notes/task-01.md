---
task_id: 01
role: 音乐生成研究专员
status: complete
sources_found: 15
---

## Sources

[1] ACE-Step 1.5: Pushing the Boundaries of Open-Source Music Generation (arXiv) | https://arxiv.org/html/2602.00744v2 | Source-Type: academic/official | As Of: 2026-02 | Authority: 9/10
[2] ace-step/ACE-Step-1.5 README (GitHub) | https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md | Source-Type: official-repo | As Of: 2026-04 | Authority: 9/10
[3] ACE-Step/acestep-v15-xl-turbo Model Card (Hugging Face) | https://huggingface.co/ACE-Step/acestep-v15-xl-turbo/blob/main/README.md | Source-Type: official | As Of: 2026-04 | Authority: 9/10
[4] Diffusers ACE-Step pipeline docs (Hugging Face) | https://huggingface.co/docs/diffusers/main/api/pipelines/ace_step | Source-Type: official-docs | As Of: 2026-05 | Authority: 8/10
[5] multimodal-art-projection/YuE (GitHub) | https://github.com/multimodal-art-projection/YuE | Source-Type: official-repo | As Of: 2026-06 | Authority: 9/10
[6] m-a-p/YuE-s1-7B-anneal-en-icl Model Card (Hugging Face) | https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-icl | Source-Type: official | As Of: 2025-03 | Authority: 8/10
[7] ASLP-lab/DiffRhythm (GitHub) | https://github.com/ASLP-lab/DiffRhythm | Source-Type: official-repo | As Of: 2025-03 | Authority: 9/10
[8] ASLP-lab/DiffRhythm2 (GitHub) | https://github.com/ASLP-lab/DiffRhythm2 | Source-Type: official-repo | As Of: 2025-10 | Authority: 8/10
[9] Stability AI & Arm — Stable Audio Open Small announcement | https://stability.ai/news-updates/stability-ai-and-arm-release-stable-audio-open-small-enabling-real-world-deployment-for-on-device-audio-control | Source-Type: official | As Of: 2025-05 | Authority: 9/10
[10] stabilityai/stable-audio-open-small README (Hugging Face) | https://huggingface.co/stabilityai/stable-audio-open-small/resolve/main/README.md | Source-Type: official | As Of: 2025-05 | Authority: 8/10
[11] MusicGen Model Card (AudioCraft / Meta FAIR) | https://facebookresearch.github.io/audiocraft/model_cards/MUSICGEN_MODEL_CARD.html | Source-Type: official | As Of: 2024 | Authority: 9/10
[12] AudioGen Model Card (AudioCraft / Meta FAIR, GitHub) | https://github.com/facebookresearch/audiocraft/blob/main/model_cards/AUDIOGEN_MODEL_CARD.md | Source-Type: official-repo | As Of: 2024 | Authority: 9/10
[13] Suno vs Udio 2026: The Honest Head-to-Head Comparison (Chartlex) | https://www.chartlex.com/blog/marketing/suno-vs-udio-2026 | Source-Type: media | As Of: 2026-06 | Authority: 6/10
[14] ACE-Step 1.5 Review — HeartMuLa vs ACE-Step vs Suno 2026 (heart-mula.com) | https://heart-mula.com/ace-step | Source-Type: vendor/media | As Of: 2026 | Authority: 6/10
[15] ACE-Step 1.5 vs HeartMuLa: The State of Local AI Music Generation in 2026 (AIToolScan, Medium) | https://medium.com/@aitoolscan/ace-step-1-5-vs-heartmula-the-state-of-local-ai-music-generation-in-2026-c37cb86351bf | Source-Type: media | As Of: 2026-06 | Authority: 5/10

## Findings

- ACE-Step v1.5 是高效开源音乐基座模型：混合架构（LM planner + Diffusion Transformer 合成器），48kHz 立体声，10 秒到 10 分钟，跨 50+ 语言；官方称质量超过多数商业模型。[1][3]
- ACE-Step 基础（2B）DiT 可在 <4GB VRAM 本地运行，A100 上 <2 秒、RTX 3090 上 <10 秒生成整曲；支持少样本 LoRA 个性化。[1]
- 2026-04-02 发布 ACE-Step 1.5 XL（4B DiT decoder，bf16 权重约 9GB / turbo 约 18.8GB），需 ≥12GB VRAM（带 offload+量化）、≥20GB 推荐；三变体 base/sft/turbo（turbo 8 步蒸馏，无 CFG）。[2][3]
- ACE-Step 配套 5Hz LM 有 0.6B / 1.7B / 4B 三档；≤6GB 可仅跑 DiT（LM 禁用+INT8+CPU offload），6–8GB 配 0.6B LM，8–16GB 配 0.6B/1.7B，≥24GB 跑 XL sft + 4B LM 最佳质量。[2]
- ACE-Step 代码/权重以 MIT 许可发布，可商用；训练数据宣称合法合规。[3][14]
- YuE 是开源 lyrics2song 基座模型系列（类 Suno 但开源），Stage 1 为 7B（结构+歌词），Stage 2 为 1B（音频重建），可生成含人声+伴奏的数分钟整曲，覆盖多语言/多流派。[5][6]
- YuE 官方全曲生成（≥4 段）建议 ≥80GB 显存（H800/A100/多卡 4090 张量并行）；社区项目 YuEGP、YuE-exllamav2 提供量化让 24GB 及以下（低至 6–12GB）可跑短片段。[5]
- YuE 于 2025-01-28 发布，论文 arXiv 2503.08638（2025-03）；号称首个开源、能媲美商业系统的全曲生成模型。[5][6]
- DiffRhythm 是首个基于隐扩散（VAE+DiT，两阶段）能生成整曲的开源模型，Apache 2.0 许可（2025-03-07 转 Apache 2.0）；v1.2-full 可生成 4分45秒整曲，约 10 秒内完成。[7]
- DiffRhythm 2（2025-10-30 论文 arXiv 2510.22950 + 权重）采用半自回归 block flow matching，改善长序列歌词对齐与音频保真，支持整曲；同样 Apache 2.0。[8]
- Stable Audio Open Small 是 341M 参数文生音频（DiT+T5，44.1kHz 立体声，最长 11 秒），与 Arm 合作可纯 CPU/手机端运行（手机 <8 秒生成 11 秒）；对比 Stable Audio Open（1.1B）更轻更快。[9][10]
- Stable Audio Open Small 用 Stability AI Community License：研究/非商用免费，年营收 <100 万美元可商用，超过需企业授权；训练数据为 Freesound + FMA（CC0/CC-BY）。[9][10]
- MusicGen（Meta FAIR）单阶段自回归 Transformer（32kHz EnCodec，4 codebooks），有 300M/1.5B/3.3B 三档 + melody/stereo 变体；代码 MIT、权重 CC-BY-NC 4.0（仅非商用）；medium 推荐 16GB 显存。[11]
- AudioGen（Meta FAIR）文生音效模型，1.5B 参数，自回归 Transformer + EnCodec，生成 5 秒环境音；代码 MIT、权重 CC-BY-NC 4.0。[12]
- 闭源对标：Suno V5（44.1kHz，Studio DAW，付费可商用下载，与 Sony 诉讼中）与 Udio（48kHz，UMG 和解后成"围墙花园"、禁下载导出）；ACE-Step 论文自评质量接近 Suno v4.5–v5。[1][13]
- HeartMuLa 是 2026 新出开源模型（Apache 2.0），主打歌词可控与人声保真，官方推荐 16GB+、社区建议 24GB VRAM，最长约 6 分钟；与 ACE-Step 一起把"本地做商业级音乐"变为现实。[14][15]

## Deep Read Notes

### Source [1]: ACE-Step 1.5 arXiv paper
- Key data: <4GB VRAM 可本地跑；A100 <2s / RTX 3090 <10s 整曲；50+ 语言；LM planner + DiT 混合架构；表格自评对标 Suno-v4.5/v5。
- Key insight: 这是当前最"消费级友好"的 near-SOTA 开源音乐模型——低显存 + 快 + 可商用 MIT。
- Useful for: 型号总表主推行；"run ACE-Step locally" / "Suno alternative" 内容切入。

### Source [2]: ACE-Step-1.5 GitHub README
- Key data: 2026-04-02 XL(4B) 发布；VRAM 分档表（≤6GB / 6-8 / 8-16 / 16-20 / 20-24 / ≥24GB）对应不同 DiT+LM 组合。
- Key insight: 同一模型家族覆盖 4GB→24GB 全部署层级，是"分层解读"的完美范例。
- Useful for: 部署层级标注（💻/🏢/📱）。

### Source [3]: acestep-v15-xl-turbo Model Card (HF)
- Key data: XL turbo ~4B params，bf16 约 18.8GB；8 步蒸馏无 CFG；≥12GB（offload+INT8）/≥20GB（无 offload）；商用友好，训练数据合规。
- Useful for: 参数量/显存/许可字段。

### Source [5]: YuE GitHub
- Key data: Stage1 7B + Stage2 1B；全曲 ≥4 段建议 ≥80GB；24GB 及以下最多 2 段；社区 YuEGP/exllamav2 降显存。
- Key insight: YuE 质量高但原生显存门槛高，属"🏢 高显存"层；靠社区量化才勉强消费级。
- Useful for: 高显存层 + "GPU poor" 长尾词。

### Source [7]: DiffRhythm GitHub
- Key data: 首个隐扩散全曲开源模型；Apache 2.0；v1.2-full 4m45s，~10s 生成；VAE+DiT 两阶段。
- Useful for: "fast song generation" + Apache 2.0 干净许可卖点。

### Source [9]: Stability AI — Stable Audio Open Small
- Key data: 341M；纯 Arm CPU / 手机可跑，手机 <8s 出 11s 音频；Community License；对比 1.1B 大版。
- Key insight: 唯一真正"📱 轻量/端侧"选项，且是音效/短样本而非整曲。
- Useful for: 📱 层 + "on-device audio generation" 词。

### Source [11]: MusicGen Model Card
- Key data: 300M/1.5B/3.3B；code MIT / weights CC-BY-NC 4.0；medium 16GB 显存；FAD/KLD 基准表。
- Key insight: 经典基线，但权重非商用 + 已被 2025–2026 新模型在质量上超越；作"历史基线/剔除候选"讨论。
- Useful for: 型号总表补充 + 局限性（非商用许可）。

## Gaps

- 相反主张候选：ACE-Step 论文自评"质量超过多数商业模型"[1]，但第三方评测（heart-mula.com AudioBox 7.2 vs Suno 8.8、SongEval 6.8 vs 8.6[14]）显示 ACE-Step 仍明显落后 Suno，人声有 artifacts——官方自评与第三方评测存在冲突，报告需注明"接近但未超越"。
- HeartMuLa 的参数量、独立官方论文/权重仓库未在本轮检索中拿到一手来源（仅媒体/vendor 页），需后续补官方仓库核实。
- ACE-Step/DiffRhythm 的 arXiv 编号（2602.xxxxx）为来源原文所载，日期格式偏未来，引用前建议以 arXiv 页面为准复核。
- 未覆盖 SEO 关键词的具体 Semrush 搜索量/难度（本轮为 Lightweight 网检，未跑 Semrush），关键词竞争度为定性判断。

## END
