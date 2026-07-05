---
task_id: 01
role: TTS 研究专员
status: complete
sources_found: 24
---

## Sources

[1] hexgrad/Kokoro-82M · Hugging Face | https://huggingface.co/hexgrad/Kokoro-82M | Source-Type: official (HF model card) | As Of: 2026-07 | Authority: 10/10
[2] hexgrad/kokoro · GitHub | https://github.com/hexgrad/kokoro | Source-Type: official (repo) | As Of: 2026-07 | Authority: 10/10
[3] index-tts/index-tts · GitHub | https://github.com/index-tts/index-tts | Source-Type: official (repo) | As Of: 2026-07 | Authority: 10/10
[4] IndexTTS2: Emotionally Expressive & Duration-Controlled Zero-Shot TTS | https://arxiv.org/html/2506.21619v1 | Source-Type: official (arXiv paper) | As Of: 2025-06 | Authority: 9/10
[5] IndexTTS 2.5 Technical Report | https://arxiv.org/html/2601.03888v2 | Source-Type: official (arXiv paper) | As Of: 2026-01 | Authority: 9/10
[6] QwenLM/Qwen3-TTS · GitHub | https://github.com/qwenlm/qwen3-tts | Source-Type: official (repo) | As Of: 2026-03 | Authority: 10/10
[7] Qwen3-TTS Technical Report (PDF mirror) | https://qwen3ttsai.com/Qwen3_TTS.pdf | Source-Type: paper (mirror of tech report) | As Of: 2026-01 | Authority: 6/10
[8] Chatterbox: Open Source TTS — Resemble AI | https://www.resemble.ai/learn/models/chatterbox | Source-Type: official (vendor) | As Of: 2026-07 | Authority: 9/10
[9] ResembleAI/chatterbox · Hugging Face | https://huggingface.co/ResembleAI/chatterbox | Source-Type: official (HF model card) | As Of: 2026-07 | Authority: 10/10
[10] fishaudio/fish-speech · GitHub | https://github.com/fishaudio/fish-speech | Source-Type: official (repo) | As Of: 2026-06 | Authority: 10/10
[11] Fish Audio S2 Technical Report | https://arxiv.org/html/2603.08823v1 | Source-Type: official (arXiv paper) | As Of: 2026-03 | Authority: 9/10
[12] What We Mean by Open Source for S2 — Fish Audio Blog | https://fish.audio/blog/what-we-mean-by-open-source-for-s2/ | Source-Type: official (vendor blog) | As Of: 2026-07 | Authority: 9/10
[13] fishaudio/s2-pro LICENSE.md · Hugging Face | https://huggingface.co/fishaudio/s2-pro/blob/main/LICENSE.md | Source-Type: official (license) | As Of: 2026-07 | Authority: 10/10
[14] neuphonic/neutts · GitHub | https://github.com/neuphonic/neutts | Source-Type: official (repo) | As Of: 2026-07 | Authority: 10/10
[15] neuphonic/neutts-air-q4-gguf · Hugging Face | https://huggingface.co/neuphonic/neutts-air-q4-gguf | Source-Type: official (HF model card) | As Of: 2026-07 | Authority: 10/10
[16] Local launch of CosyVoice 3 — CPA.RIP | https://cpa.rip/en/ai/cosyvoice-3/ | Source-Type: secondary (how-to) | As Of: 2026-06 | Authority: 5/10
[17] Best Open-Source TTS 2026 — ocdevel | https://ocdevel.com/blog/20250720-tts | Source-Type: secondary (roundup) | As Of: 2026-06 | Authority: 6/10
[18] Best Open-Source TTS Models 2026 — BentoML | https://www.bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models | Source-Type: secondary (vendor blog) | As Of: 2026-07 | Authority: 7/10
[19] wildminder/awesome-ai-voice · GitHub | https://github.com/wildminder/awesome-ai-voice | Source-Type: community (aggregator) | As Of: 2026-07 | Authority: 6/10
[20] Kokoro TTS Complete Guide — OfflineTTS | https://offlinetts.com/blog/kokoro-tts-complete-guide/ | Source-Type: secondary | As Of: 2026-06 | Authority: 5/10
[21] Kokoro TTS Review 2026 — TextToLab | https://texttolab.com/blog/kokoro-tts-review | Source-Type: secondary | As Of: 2026-06 | Authority: 5/10
[22] Qwen3-TTS: Voice AI Without The Cloud — snackonai | https://www.snackonai.com/p/qwen3-tts-voice-ai-without-the-cloud | Source-Type: secondary | As Of: 2026-02 | Authority: 5/10
[23] Qwen3-TTS Voice Cloning Guide — Clore.ai | https://docs.clore.ai/guides/audio-and-voice/qwen3-tts | Source-Type: secondary (docs) | As Of: 2026-06 | Authority: 5/10
[24] Why "AI Voice Clone Narration" Is Emerging SEO Keyword 2026 — vvideo | https://vvideo.co/blog/ai-voice-clone-narration-emerging-2026 | Source-Type: secondary (SEO) | As Of: 2026-06 | Authority: 4/10

## Findings

- Kokoro 是 82M 参数开源 TTS，Apache 2.0，CPU/低配即可实时跑（<2GB VRAM），主打英语（misaki 扩 ja/zh），但**无内置声音克隆**（社区 KokoClone 补零样本克隆）。[1][2][20]
- Kokoro 在 Artificial Analysis TTS Arena 上 Elo 1056、74 个模型中排第 32，但**在可浏览器内运行的模型中排第 1**；盲测胜过 Google WaveNet / Amazon Polly Neural。[20][21]
- NeuTTS Air 是"世界首个"超写实**端侧** TTS：Qwen 0.5B 骨干（激活约 360M、含 embedding 约 552M）+ NeuCodec 单码本，GGUF 格式可在手机/笔记本/树莓派 CPU 实时跑，3 秒即时克隆，Apache 2.0；另有 Nano 约 120M。[14][15][19]
- Chatterbox（Resemble AI）：0.5B Llama 骨干、50 万小时训练，MIT 许可，零样本克隆（5 秒参考）+ 业界首个"情绪夸张"控制 + PerTh 水印，<200ms 延迟；多语 V3 支持 23 语言，另有 Turbo 350M；官方称盲测优于 ElevenLabs。[8][9]
- CosyVoice（FunAudioLLM/阿里）：CosyVoice 2.0 与 3.0 均为 0.5B，Apache 2.0，零样本克隆 3–10 秒，支持 9–10 语言，流式约 150ms，自带文本正规化与 instruct 模式；0.5B 可在弱硬件本地跑（~4GB）。[16][11]
- Qwen3-TTS（阿里 Qwen，2026-01-22 发布）：0.6B/1.7B，Apache 2.0，5M 小时/10 语言训练，双轨 LM + 两个 tokenizer（25Hz 质量档、12Hz 97ms 首包流式），3 秒克隆 + voice design；1.7B 中文 WER 2.12%/英文 2.58%/相似度 0.89。[6][7][22][23]
- Qwen3-TTS 显存：0.6B≈4GB、1.7B≈8GB（可跑在 RTX 4080 SUPER 16GB）；0.6B 长文本克隆易退化，长文本建议用 1.7B。[23][22]
- IndexTTS2（B 站，2025-09-08 发布）：自回归零样本，首个精确**时长可控**，情绪/音色解耦，情绪可用参考音频 / 8 维向量 / 文本描述三种方式控制；BigVGANv2 vocoder；许可为自定义 LicenseRef-Bilibili-IndexTTS。[3][4]
- IndexTTS 2.5（2026 初）：语义码本 50→25Hz、S2M 换 Zipformer、GRPO 后训练，RTF 提升 2.28×，多语扩到中/英/日/西，WER 与相似度与 2 代相当。[5]
- Fish Audio S2 Pro：4B 参数（Slow AR 4B + Fast AR 400M），10M 小时/80+ 语言、Dual-AR+RL，RTF 0.195、首音 <100ms，克隆 10–30 秒，Seed-TTS-Eval 上 WER 最低（原始精度最强），需 12–24GB VRAM。[10][11][17]
- Fish Audio S2 为**开放权重≠开源**：Fish Audio Research License——研究/非商用免费，**商用需单独付费授权**。[12][13]
- 其他可本地跑开源型号：XTTS-v2（Coqui，467M，17 语言，6 秒克隆，CPML 非商用）、Orpheus-TTS（3B，Apache 2.0，情绪+流式）、Dia（Nari，1.6B，Apache 2.0，多说话人对话）、Zonos（8GB VRAM 克隆）、Piper（VITS 轻量 CPU、无克隆、边缘首选）。[19][21][17]
- 闭源对标定价：ElevenLabs v3（盲测 Elo 最高约 1178，$5–330/月）、OpenAI TTS（$15/1M 字符）、Azure TTS（$24/1M）；开源自托管把成本降到 ElevenLabs 的 1/10 以下。[20][21][17]

## Deep Read Notes

### Source [1][2]: Kokoro-82M（HF + GitHub）
Key data: 82M 参数，Apache 2.0 权重（2024-12-25 v0.19 发布 fp32），推理库 `pip install kokoro`，采样率 24kHz，54+ 内置音色，misaki G2P；GitHub 7786 stars（2025-01-10 建）。
Key insight: "小而强"标杆——质量接近大模型但显著更快更省，唯一硬缺陷是无原生克隆。
Useful for: 📱 边缘/CPU 层核心型号；"run Kokoro locally" / "Kokoro vs ElevenLabs" 内容。

### Source [14][15]: NeuTTS Air（Neuphonic）
Key data: Qwen 0.5B 骨干 + NeuCodec 单码本；GGUF Q4/Q8；context 2048（~30s 音频）；3 秒克隆；Apache 2.0（Air），Nano 用 NeuTTS Open License 1.0；Linux/macOS/Windows，~2–3GB 磁盘，CPU 即可。
Key insight: 定位就是"把 SOTA 语音 AI 从云 API 搬到本机/手机"，与 Olares 端侧隐私叙事高度契合。
Useful for: 📱 端侧克隆代表；"on-device TTS" / "voice cloning offline" / Raspberry Pi 场景。

### Source [6][7]: Qwen3-TTS（阿里 Qwen）
Key data: 0.6B/1.7B，Apache 2.0，2026-01-22 发布；双轨 LM + 25Hz/12Hz 双 tokenizer；97ms 首包；1.7B 客观指标超 ElevenLabs/MiniMax/SeedTTS（中文 WER 2.12%）；GitHub 12k+ stars。
Key insight: 目前**许可最友好 + 指标最强**的消费级 GPU 主力，可商用、可微调。
Useful for: 💻 台式主力；"Qwen3-TTS voice cloning" / "Qwen3-TTS vs ElevenLabs"。

### Source [10][11][12][13]: Fish Audio S2 Pro
Key data: 4B（Slow AR 4B + Fast AR 400M），10M 小时/80+ 语言，RTF 0.195/首音<100ms，克隆 10–30s；GitHub 31k stars；许可=Fish Audio Research License（商用付费）。
Key insight: 原始精度/多语最强的开放权重旗舰，但**商用受限**——写"最强"时必须标许可陷阱。
Useful for: 🏢 高显存层；"Fish Speech commercial license" / "best multilingual open TTS"。

### Source [3][4][5]: IndexTTS 2 / 2.5（B 站）
Key data: 时长可控 + 情绪/音色解耦；情绪三通道输入；2.5 RTF 提升 2.28×、支持中英日西；许可为自定义（非标准开源）。
Key insight: 视频配音/多说话人场景最实用（可锁定时长对齐画面）。
Useful for: 💻 台式；"IndexTTS2 emotion control" / "AI dubbing local"。

## Gaps

- **相反主张（Kokoro 质量）**：官方与 OfflineTTS 称"质量接近大模型/浏览器第一"[1][20]；但 YouTube 实测与 TextToLab 指出 Kokoro 仅英语、无克隆、技术词发音需正规化，且 Arena 总榜仅第 32、盲测对 ElevenLabs v3 胜率仅 31%[21]。→ "接近 SOTA"需限定在"小模型/CPU/英语朗读"语境。
- **相反主张（Chatterbox 许可）**：HF 元数据 header 标 `license: apache-2.0`，但 README 正文与 Resemble 官网均声明 **MIT**[9][8]。→ 引用许可以官方仓库 LICENSE 文件为准（MIT）。
- Qwen3-TTS 技术报告用的是第三方镜像域 qwen3ttsai.com[7]，arXiv 编号 2601.15621 出现在二手源[22]但未直接核到官方 arXiv 页——数字以 GitHub 官方 README[6] 为准。
- CosyVoice 未直接读到官方 GitHub/HF 卡（经 Fish 报告表[11] 与 CPA.RIP[16] 交叉印证 0.5B/1.5B 与语言数），下一轮应补官方源。

## END
