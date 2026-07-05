# 开源 TTS 语音合成（本地可跑 near-SOTA）调研

> 研究日期: 2026-07-05 | 来源数: 24 | 模式: Lightweight | AS_OF: 2026-07-05 | 官方源占比: 58%

## 摘要

2026 年开源 TTS 已经"追上"闭源：TTS Arena 盲测里 ElevenLabs v3 仍居前列，但开源阵营在**成本、隐私、离线、可商用**四条线上全面反超，自托管成本普遍低于 ElevenLabs 的 1/10[17][20][21]。对 Olares（个人云、本地推理）而言，这是极佳的场景——语音合成/声音克隆天然涉及隐私（用自己的声音），"把语音 AI 从云 API 搬回本机"正是 NeuTTS Air、Chatterbox、Qwen3-TTS 等新型号的核心卖点[14][8][22]。

按"能不能本地跑 + 参数量"分三层：**📱 边缘/CPU 级**（Kokoro 82M、Piper、NeuTTS Nano 120M / Air ~0.5B）无需 GPU，手机/树莓派可跑；**💻 本地台式级**（Qwen3-TTS 0.6B/1.7B、CosyVoice2/3 0.5B、Chatterbox 0.5B、IndexTTS2、XTTS-v2 467M、Dia 1.6B）是消费级 GPU 主力，多数支持 3–10 秒零样本克隆；**🏢 高显存/大模型**（Fish Audio S2 Pro 4B、Orpheus 3B）追求原始精度与多语覆盖。许可是最大变量：Kokoro / Qwen3-TTS / CosyVoice / Chatterbox / NeuTTS Air 均可商用（Apache 2.0 或 MIT），而 **Fish Audio S2 是"开放权重≠开源"，商用需付费授权**[12][13]，XTTS-v2 与 IndexTTS2 也带非标准/非商用条款——这是内容写作里必须点破的坑。

## 1. 型号总表（核心交付）

| 模型 | 代表型号 / 参数量 | 部署层级 | 许可 | 闭源对标 | 候选关键词（低竞争标 ★） |
|------|-----------------|---------|------|---------|----------------------|
| **Kokoro** | Kokoro-82M / 82M | 📱 CPU/边缘 | Apache 2.0 | ElevenLabs / OpenAI TTS | run kokoro locally ★ / kokoro tts voice cloning ★ / kokoro vs elevenlabs |
| **Piper** | 多 VITS 语音 / ~5–30M | 📱 CPU/边缘 | MIT | Amazon Polly / Azure TTS | piper tts self-hosted ★ / offline tts raspberry pi ★ |
| **NeuTTS Air** | Air ~0.5B（激活~360M）/ Nano ~120M | 📱 端侧+克隆 | Apache 2.0（Nano: NeuTTS OL 1.0） | ElevenLabs / Play.ht | on-device voice cloning ★ / neutts air local ★ / tts raspberry pi voice clone ★ |
| **Chatterbox** | 标准 0.5B / Turbo 350M / 多语 V3 0.5B | 💻 消费 GPU | MIT | ElevenLabs | chatterbox tts voice cloning ★ / open source elevenlabs alternative / chatterbox vs elevenlabs ★ |
| **CosyVoice** | 2.0 / 3.0 0.5B（另 1.5B） | 💻 消费 GPU | Apache 2.0 | ElevenLabs / MiniMax | cosyvoice 3 local ★ / cosyvoice voice cloning ★ / run cosyvoice locally ★ |
| **Qwen3-TTS** | 0.6B / 1.7B | 💻 消费 GPU | Apache 2.0 | ElevenLabs / OpenAI TTS | qwen3-tts voice cloning ★ / qwen3 tts local ★ / qwen3-tts vs elevenlabs ★ |
| **IndexTTS** | IndexTTS 2 / 2.5 | 💻 消费 GPU | 自定义（Bilibili License） | ElevenLabs（配音） | indextts2 emotion control ★ / ai dubbing local ★ / indextts voice clone ★ |
| **XTTS-v2** | Coqui XTTS-v2 / 467M | 💻 消费 GPU | CPML（非商用） | ElevenLabs | xtts v2 voice cloning / run xtts locally ★ / coqui tts alternative ★ |
| **Dia** | Nari Dia / 1.6B | 💻 消费 GPU | Apache 2.0 | ElevenLabs（对话） | dia tts dialogue ★ / nari dia local ★ |
| **Orpheus-TTS** | 3B | 🏢 高显存 | Apache 2.0 | ElevenLabs | orpheus tts local ★ / orpheus voice cloning ★ |
| **Fish Audio S2 Pro** | 4B（Slow AR 4B + Fast AR 400M） | 🏢 高显存 | Fish Research（商用付费） | ElevenLabs / MiniMax | fish speech commercial license ★ / best multilingual open tts / fish audio s2 self-host ★ |

> 参数量与许可以官方仓库/HF/论文为准；量化版本（GGUF/ONNX/int8）不单列。VRAM 参考：Kokoro <2GB、Qwen3-TTS 0.6B≈4GB / 1.7B≈8GB、CosyVoice ~4GB、Fish S2 Pro 12–24GB[1][23][16][11]。

## 2. 分层解读（轻量 CPU vs GPU；含声音克隆能力）

### 📱 边缘/CPU 级——无 GPU、手机/树莓派可跑
**Kokoro-82M** 是这一层的标杆：82M 参数、Apache 2.0、<2GB 显存甚至纯 CPU 实时，可 100% 浏览器内运行（Transformers.js，kokoro-js 周下载 ~9.8 万）[1][2][3-js]。质量上，它在 Artificial Analysis TTS Arena 总榜 Elo 1056（74 模型中第 32），但**在可浏览器运行的模型里排第 1**，盲测胜过 Google WaveNet 与 Amazon Polly Neural[20]。硬缺陷：主打英语、**无内置克隆**（社区 KokoClone 用 ECAPA-TDNN 补零样本克隆，近似而非复刻）[20]。**Piper**（VITS、MIT）更小更快，边缘/离线朗读首选，同样无克隆。

**NeuTTS Air** 改写了这层的能力上限——它是"世界首个超写实**端侧**克隆 TTS"：Qwen 0.5B 骨干（激活 ~360M）+ NeuCodec 单码本，GGUF 格式在手机/笔记本/树莓派 CPU 实时跑，**3 秒即时克隆**、带水印、Apache 2.0；另有 Nano ~120M[14][15][19]。对 Olares 端侧隐私叙事这是最贴合的一颗棋子。

### 💻 本地台式级——消费级 GPU 主力（克隆能力集中区）
**Qwen3-TTS**（阿里，2026-01-22）是当前**许可最友好 + 指标最强**的组合：0.6B/1.7B、Apache 2.0、5M 小时/10 语言训练，双轨 LM + 25Hz/12Hz 双 tokenizer，首包 97ms 流式，3 秒克隆 + 文本描述"voice design"；1.7B 客观指标（中文 WER 2.12%、英文 2.58%、相似度 0.89）超 ElevenLabs/MiniMax/SeedTTS，可跑在 RTX 4080 SUPER 16GB[6][7][22][23]。长文本克隆建议用 1.7B（0.6B 会出长静音退化）[23]。

**CosyVoice 2.0/3.0**（阿里 FunAudioLLM）：0.5B、Apache 2.0、零样本克隆 3–10 秒、9–10 语言、~150ms 流式、自带文本正规化与 instruct（方言/情绪/语速一句话控制），弱硬件也能本地跑[16][11]。**Chatterbox**（Resemble AI）：0.5B Llama 骨干、MIT，零样本克隆（5 秒）+ 业界首个"情绪夸张"控制 + PerTh 水印、<200ms，多语 V3 覆盖 23 语言，官方称盲测优于 ElevenLabs[8][9]。**IndexTTS 2/2.5**（B 站）主打**时长可控 + 情绪/音色解耦**（情绪可用参考音频/8 维向量/文本三通道输入），最适合视频配音；2.5 换 Zipformer + GRPO，RTF 提升 2.28×、扩到中英日西，但**许可是自定义非标准开源**[3][4][5]。**XTTS-v2**（Coqui，467M，17 语言，6 秒克隆）仍是下载量最高的经典，但 CPML 非商用；**Dia**（1.6B，Apache 2.0）专攻多说话人对话与非语言音效。

### 🏢 高显存/大模型——追精度与多语
**Fish Audio S2 Pro**：4B（Slow AR 4B + Fast AR 400M），10M 小时/80+ 语言、Dual-AR+RL，RTF 0.195、首音 <100ms、克隆 10–30 秒，Seed-TTS-Eval 上 WER 最低（原始精度/多语最强），但需 12–24GB VRAM，且**商用需付费**[10][11][12][13]。**Orpheus-TTS**（3B、Apache 2.0）情绪表现强、流式，GPU 推理。这层适合"要极致质量/多语且愿上大卡"的用户，Olares One（x86+NVIDIA）正好承接。

## 3. 候选 SEO 关键词与内容切入

- **型号词 × 本地部署（低竞争、Olares 直接承接）**："run Kokoro locally"、"qwen3-tts local / self-host"、"cosyvoice 3 local"、"neutts air on-device"、"chatterbox tts self-hosted"、"run xtts locally"——搜索者已是"要本地跑"的高意图人群，页一多为 GitHub/HF 与小站，Olares 教程页可切入。
- **声音克隆词（高增长）**："voice cloning" 两年增长 >200%[24]；长尾如 "open source voice cloning"、"offline voice cloning"、"voice clone raspberry pi"、"on-device voice cloning" 竞争低、隐私痛点强，天然适合 Olares（用你自己的声音、数据不出机）。
- **X alternative / vs 词**："open source ElevenLabs alternative"、"chatterbox vs elevenlabs"、"qwen3-tts vs elevenlabs"、"self-hosted ElevenLabs"、"OpenAI TTS alternative open source"——承接对闭源定价不满的迁移意图。
- **场景词**："AI dubbing local / open source"（IndexTTS2 时长控制）、"local TTS for audiobooks"、"self-hosted TTS API"、"local text to speech privacy"。
- **内容切入建议**：优先做 3 篇高杠杆——①"Best open-source TTS you can self-host (2026)"总表页（承接 Kokoro/Qwen3-TTS/Chatterbox/Fish/NeuTTS）；②"Run voice cloning locally on Olares"教程（NeuTTS Air / Qwen3-TTS）；③"Open-source ElevenLabs alternatives"对比文（点破 Fish 商用许可坑，突出 Apache/MIT 阵营）。

## 关键发现（2-3）

1. **许可分化是内容最大抓手**：Kokoro / Qwen3-TTS / CosyVoice / Chatterbox / NeuTTS Air 可商用（Apache/MIT），而 Fish Audio S2、XTTS-v2、IndexTTS2 带非标准或非商用条款[12][13][9]。"能不能商用自托管"是搜索者的真实决策点，也是我们与泛评测文的差异化。
2. **"端侧克隆"是 Olares 的黄金交叉点**：NeuTTS Air（3 秒克隆、GGUF、树莓派可跑）与 Qwen3-TTS（3 秒克隆、Apache 2.0）把"声音克隆"从云 API 拉回本机[14][22]，直击隐私痛点——用自己的声音、数据不出机，正是个人云操作系统的天然用例。
3. **"近 SOTA"要分语境**：Kokoro 是"小模型/CPU/英语朗读"里的 SOTA，但盲测总榜仍低于 ElevenLabs v3（胜率 31%）[20][21]；真正逼近闭源原始精度的是 4B 的 Fish S2 与 1.7B 的 Qwen3-TTS[11][7]。写作时勿把"CPU 能跑"等同"全面 SOTA"。

## 局限性

- Lightweight 模式、单轮检索：CosyVoice、Piper、XTTS-v2、Dia、Orpheus、Zonos 未逐一核到官方 GitHub/HF 卡（部分经二手源与 Fish 论文表交叉印证），参数/许可以官方源为准需下一轮补齐。
- 无 Semrush 实测量：关键词"低竞争"为基于 SERP 结构与型号新鲜度的定性判断，未附精确搜索量/KD，正式立项前建议用 brand-seo / model-seo skill 跑 Semrush 校准。
- 版本迭代快：IndexTTS 2.5、Chatterbox V3、Fish S2 Pro、Qwen3-TTS 均为 2026 上半年产物，参数/许可/指标可能随新版变化，引用前以官网/HF 最新为准。
- 存在相反主张（见 task-01 Gaps）：Chatterbox 许可 HF header 标 Apache 但正文/官网为 MIT；Kokoro"质量第一"限定于浏览器/小模型语境——报告已按官方源取舍。

## 参考文献

[1] Hugging Face — hexgrad/Kokoro-82M. https://huggingface.co/hexgrad/Kokoro-82M
[2] GitHub — hexgrad/kokoro. https://github.com/hexgrad/kokoro
[3] GitHub — index-tts/index-tts. https://github.com/index-tts/index-tts
[4] arXiv — IndexTTS2 (2506.21619). https://arxiv.org/html/2506.21619v1
[5] arXiv — IndexTTS 2.5 Technical Report (2601.03888). https://arxiv.org/html/2601.03888v2
[6] GitHub — QwenLM/Qwen3-TTS. https://github.com/qwenlm/qwen3-tts
[7] Qwen3-TTS Technical Report (PDF mirror). https://qwen3ttsai.com/Qwen3_TTS.pdf
[8] Resemble AI — Chatterbox. https://www.resemble.ai/learn/models/chatterbox
[9] Hugging Face — ResembleAI/chatterbox. https://huggingface.co/ResembleAI/chatterbox
[10] GitHub — fishaudio/fish-speech. https://github.com/fishaudio/fish-speech
[11] arXiv — Fish Audio S2 Technical Report (2603.08823). https://arxiv.org/html/2603.08823v1
[12] Fish Audio Blog — What We Mean by Open Source for S2. https://fish.audio/blog/what-we-mean-by-open-source-for-s2/
[13] Hugging Face — fishaudio/s2-pro LICENSE.md. https://huggingface.co/fishaudio/s2-pro/blob/main/LICENSE.md
[14] GitHub — neuphonic/neutts. https://github.com/neuphonic/neutts
[15] Hugging Face — neuphonic/neutts-air-q4-gguf. https://huggingface.co/neuphonic/neutts-air-q4-gguf
[16] CPA.RIP — Local launch of CosyVoice 3. https://cpa.rip/en/ai/cosyvoice-3/
[17] ocdevel — Best Open-Source TTS 2026. https://ocdevel.com/blog/20250720-tts
[18] BentoML — Best Open-Source TTS Models 2026. https://www.bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models
[19] GitHub — wildminder/awesome-ai-voice. https://github.com/wildminder/awesome-ai-voice
[20] OfflineTTS — Kokoro TTS Complete Guide. https://offlinetts.com/blog/kokoro-tts-complete-guide/
[21] TextToLab — Kokoro TTS Review 2026. https://texttolab.com/blog/kokoro-tts-review
[22] snackonai — Qwen3-TTS: Voice AI Without The Cloud. https://www.snackonai.com/p/qwen3-tts-voice-ai-without-the-cloud
[23] Clore.ai — Qwen3-TTS Voice Cloning Guide. https://docs.clore.ai/guides/audio-and-voice/qwen3-tts
[24] vvideo — Why "AI Voice Clone Narration" Is Emerging SEO Keyword 2026. https://vvideo.co/blog/ai-voice-clone-narration-emerging-2026
