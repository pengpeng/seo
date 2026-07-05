---
task_id: 02
role: 音乐生成研究专员（收敛轮）
status: complete
sources_found: 6
as_of: 2026-07-05
---

## Sources（本轮新增）

[16] Best Open-Source AI Music Generators 2026 (IT-JIM，独立亲手盲测) | https://www.it-jim.com/blog/best-open-source-ai-music-generator/ | Source-Type: independent-benchmark/media | As Of: 2026-05 | Authority: 7/10
[17] tencent-ailab/SongGeneration (LeVo 2 / SongGeneration 2) README (GitHub) | https://github.com/tencent-ailab/SongGeneration | Source-Type: official-repo | As Of: 2026-03 | Authority: 9/10
[18] tencent/SongGeneration LICENSE (Hugging Face) | https://huggingface.co/tencent/SongGeneration/blob/main/LICENSE | Source-Type: official | As Of: 2026 | Authority: 9/10
[19] tencent-ailab/SongBloom README (GitHub) | https://github.com/tencent-ailab/SongBloom | Source-Type: official-repo | As Of: 2025 | Authority: 9/10
[20] SongBloom: Coherent Song Generation via Interleaved AR Sketching and Diffusion Refinement (arXiv 2506.07634) | https://arxiv.org/abs/2506.07634 | Source-Type: academic/official | As Of: 2025-06 | Authority: 9/10
[21] ACE-Step 1.5 XL released, capable of Japanese vocals (GIGAZINE) | https://gigazine.net/gsc_news/en/20260409-ace-step-1-5-xl/ | Source-Type: media | As Of: 2026-04 | Authority: 6/10

## Findings（收敛轮）

- 复核确认：截至 2026-07，**没有 2026 新出的开源模型在"可商用+消费级+生态"综合维度明确超过 ACE-Step 1.5**。独立第三方 IT-JIM（2026-05 亲手加载 8 个开源模型盲测）判定 ACE-Step 1.5 在研究/微调/下游工具链胜出，"优势大到没有真正的第二名"；ACE-Step README 亦称"the most powerful local music generation model that outperforms almost all commercial alternatives"。[16][17]
- ACE-Step 1.5 生态领先的硬指标：GitHub 11K+ star、1.4K fork、80 贡献者、13 个 release（最新 v0.1.8，2026-05-18）、支持 Mac/AMD/Intel/CUDA、原生 LoRA 微调；主页 acemusic.ai。[17（ACE-Step repo 元数据）]（注：此处指 ace-step/ACE-Step-1.5 仓库，见 [2]）
- ACE-Step 1.5 XL（4B DiT，~9GB bf16）2026-04-02 发布，三变体 base（全任务/高多样性）/sft（高质量）/turbo（8 步蒸馏、日常首选），另有 turbo-rl 待发布；XL 最低 12GB VRAM、推荐 20GB+；可生成日语等多语种人声。[3][21]
- ACE-Step 1.5 架构：Qwen3 系 LM planner + DiT renderer；5Hz FSQ tokenizer + Muon 训练的 1-D VAE，48kHz 立体声；独有"内在强化学习"（Attention Alignment Score + DiffusionNTF + GRPO/PMI），奖励来自模型自身注意力几何而非人类偏好，2026 slate 独一份；Omni-Task 单套权重跑六模式（文生曲/翻唱/重绘/提取/叠加/补全）。MIT 覆盖代码+权重，模型卡明文"You can strictly use the generated music for commercial purposes"。[16]
- **相反主张（核心）**：IT-JIM 盲测的纯音质冠军是 **LeVo 2 / SongGeneration 2（腾讯）**——三种风格（硬摇滚/爵士/流行）最自然，非种子运气所致；而 ACE-Step 1.5 有贯穿人声与器乐的"金属感 shimmer"artifact（疑与 5Hz FSQ tokenizer 或低步数去噪相关）。但 LeVo 2 是腾讯自定义**非商用**许可（"only for academic, research and education purposes… refrain from using it for any commercial or production purposes under any circumstances"），无法商用/生产落地——故不能主推。[16][17][18]
- LeVo 2（SongGeneration 2）：2026-03-01 开源 v2-large（4B 参数），PER 8.55%，多语种，VRAM 分档 10/22/28GB、最长 4m30s；无独立 arXiv 论文，技术报告自 2026-03 承诺至今未发；HF 卡显示 `license: unknown` 属误导（权重托管在个人账号 lglg666），实际以 repo Tencent 自定义非商用 LICENSE 为准。[16][17][18]
- **修正上一版**：上一轮据 vendor 页 heart-mula.com [14] 写"HeartMuLa 音质最高、逼近 Suno"，与独立第三方冲突——IT-JIM 三风格盲测发现 HeartMuLa"averaged, smoothed, AI-blurry / 泛化成模糊流行乐"，且摘要吹 7B 但**实际只发布 3B** SKU。HeartCodec 12.5Hz 三编码器（Whisper+WavLM+MuEncoder）融合、Llama-3.2 LM 设计新颖，但音质并不突出。[16]
- DiffRhythm 2：Block Flow Matching（块内非自回归、块间自回归、边界 KV-cache）+ Cross-Pair Preference Optimization（40K 对、~200 GPU-hours），Apache 2.0、极速；但**其论文 §5.2 自承人声质量落后 ACE-Step 与 LeVo**、节奏不稳，§6 明言"Open-source still falls short of commercial systems overall"。[16]（DiffRhythm2 repo 见 [8]）
- SongBloom（腾讯 AI Lab + CUHK-Shenzhen，arXiv 2506.07634，2B）：交错自回归 sketching + 扩散 refinement，最长 150s（长版 240s/4min，48kHz）；**推理必须提供 10 秒参考音频**定风格，落在"纯文本→整曲"主线之外；论文称可比肩商业平台。[19][20]
- YuE：2025 血脉源头、Apache 2.0 显式可商用、诚实写 Limitations，但 IT-JIM 盲测音质不突出、RTX 4090 上约 12× 慢于实时，社区 fork（YuEGP、YuE-exllamav2）因显存/速度而生。[16]（YuE 官方见 [5][6]）
- Khala（中央音乐学院）：纯声学 64 层 RVQ、无语义层（复活 Jukebox 路线），~3.7B，1.2M 小时音乐学院内部语料训练；CC-BY-NC**非商用**+官方挂"质量不稳定"免责声明。Muse（复旦）：0.6B Qwen3 纯 SFT，真正贡献是 7771 小时全合成 Suno-V5 语料全 MIT 公开（唯一全公开语料）。二者均属研究向，非可用旗舰。[16]
- 大势判断：IT-JIM 与 DiffRhythm 2 论文一致认为"开源尚无真正的 Suno"、闭源在整体音质仍领先；开源的差异化在"可商用+本地+私有+可微调+无订阅"——正是 Olares 本地推理的价值主张。[8][16]

## Deep Read Notes

### Source [16]: IT-JIM — Best Open-Source AI Music Generators 2026（本轮最重要）
- 方法：2026-05 亲手加载 8 个开源模型（ACE-Step v1/1.5、LeVo 2、Khala、YuE、HeartMuLa、Muse、DiffRhythm 2），同 3 组风格×歌词、每模型 1 seed 盲听。
- 双结论：**LeVo 2 音质冠军（但非商用许可）**；**ACE-Step 1.5 研究/微调/工具链冠军（MIT，但有 metallic shimmer）**。Khala 架构异类（非商用+不稳定）。
- 关键判断句："ACE-Step 1.5 wins on research, fine-tuning, and downstream tooling… by a margin large enough that there is no real second place."
- Useful for: 主推唯一性论证 + 相反证据（音质冠军是 LeVo 2）+ HeartMuLa 音质修正 + 各备选降级理由。

### Source [17]/[18]: tencent-ailab/SongGeneration + LICENSE
- Key data: LeVo 2 = SongGeneration 2，v2-large 4B，2026-03-01 发布，PER 8.55%，VRAM 10/22/28GB。
- License（verbatim）："only for academic, research and education purposes… refrain from using it for any commercial or production purposes under any circumstances." → **非商用**，无法主推。
- Useful for: LeVo 2 降级理由（音质好但禁商用）；许可作为隐藏胜负手论据。

### Source [19]/[20]: SongBloom（GitHub + arXiv 2506.07634）
- Key data: 2B，交错 AR sketching + diffusion refinement，最长 150s（长版 240s），**推理需 10s 参考音频**，48kHz。
- Useful for: SongBloom 降级理由（需参考音频、非纯文本）。

### Source [21]: GIGAZINE — ACE-Step 1.5 XL
- Key data: XL 4B DiT，2026-04-02 发布，三变体 base/sft/turbo，最低 12GB / 推荐 20GB+ VRAM，可生成日语人声。
- Useful for: XL 型号/显存/多语种字段佐证（media 交叉官方 [2][3]）。

## Gaps

- 音质排序来自 IT-JIM 单次实践者盲测（3 prompt×1 seed），非大样本 MOS；权威度中上但作者自陈会过时。
- LeVo 2 无独立 arXiv 论文、技术报告未发；HeartMuLa 一手官方论文/权重仓库与确切参数量仍未取得（本轮仍靠第三方描述）。
- 未跑 Semrush，关键词竞争度为定性判断。
- ACE-Step/DiffRhythm arXiv 编号（26xx/25xx）日期格式偏未来，引用前以 arXiv 页面复核。

## END
