# model/models.md — 开源 AI 模型清单

> 值得为 Olares 做 SEO/内容的**开源、可本地运行的模型** family（只收开源；闭源模型/API 如 GPT、Claude、Gemini 归 [commerce/](/Users/pengpeng/seo/directions/commerce)）。按模态章分组（当前 10 章；Omni/VLM 暂缺，待有可用型号再补，研究底稿仍在 research/11-omni/），来源是各章 deep-research 底稿 [research/](/Users/pengpeng/seo/directions/model/research)。模型没有 `beclab/apps` 那样的 manifest 仓库，故本清单**手工维护**、非脚本生成。每个 family 的 model-seo 报告放在 [reports/](/Users/pengpeng/seo/directions/model/reports) 对应章。

**选型准则**：① 开源、可本地运行；② 2026 年接近 SOTA（过期型号如 DeepSeek R1 / Llama 3.x / Qwen 2.5 已剔除）；③ **以型号级登记、忽略量化版本**（Q4/GGUF/AWQ 不进表）。

**部署层级**：📱 手机/边缘级（≈4B 及以下或超轻量，CPU/端侧可跑，性能有限）｜💻 本地台式级（消费级 GPU / Olares One 24GB 甜点位，**主力主推**）｜🏢 企业级（数百 B–T 级或高显存，需多卡/服务器，成本高仍关注）。

**闭源对标**：每个 family 标出它替代的商业产品，是 `run X locally` / `X alternative` / `open source X` 内容的切入点。

**报告状态**：⬜ 待做（旧报告已随重构清空，之后按新结构走 [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md) 重做）。

## 01 LLM 文本生成（含推理 / agentic / 编码）

> 底稿 [research/01-llm/llm.md](/Users/pengpeng/seo/directions/model/research/01-llm/llm.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| Gemma 4 | E2B / E4B · 12B / 26B-A4B / 31B | 📱→💻 | Apache 2.0 | Gemini Nano / Flash | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/01-llm/gemma-4.md) |
| Qwen 3.6 | 27B (dense) / 35B-A3B (MoE) | 💻 主力 | Apache 2.0 | GPT-5 级 / Claude Sonnet | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/01-llm/qwen-3.md) |
| Qwen3-Coder | 30B-A3B / 480B-A35B | 💻→🏢 | Apache 2.0 | Claude（编码/agent） | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/01-llm/qwen3-coder.md) |
| Ornith-1.0 | 9B-Dense / 31B-Dense / 35B-MoE / 397B-MoE | 📱→🏢 | MIT | Claude Opus 4.7（agentic 编码） | ⬜ |
| GLM-5.2 | 744B-A40B | 🏢 | MIT | GPT-5.5 / Claude Opus 4.8 | ⬜ |
| DeepSeek V4 | Flash (284B-A13B) / Pro (1.6T-A49B) | 🏢 | MIT | Claude / Gemini（长上下文 agent） | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/01-llm/deepseek-v4.md) |
| Kimi K2.7 Code | K2.7 Code (1T-A32B) | 🏢 | Modified MIT | GPT-5.5 / Claude Opus 4.8（agentic 编码） | ⬜ |
| MiniMax M3 | M3 (428B-A23B，1M 上下文，原生多模态) | 🏢 | MiniMax Community License | Claude Opus（多模态 agent/coding） | ⬜ |
| Llama 4（渐旧） | Scout 109B-A17B / Maverick 400B-A17B | 🏢 | Llama 4 社区许可（非 OSI） | GPT-4.5 / Gemini | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/01-llm/llama-4.md) |

## 02 图像生成 / 编辑

> 底稿 [research/02-image/image-gen.md](/Users/pengpeng/seo/directions/model/research/02-image/image-gen.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| FLUX.2 | klein 4B / 9B · dev 32B | 💻→🏢 | klein-4B Apache 2.0；dev/9B 非商用 | Midjourney / DALL·E | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/02-image/flux-2.md) |
| Ideogram 4 | 9.3B（文字/版面最强开放权重，原生 2K） | 💻 | 开源 Non-Commercial + 商用另购（self-serve/enterprise） | GPT Image / Nano Banana / Midjourney | ⬜ |
| Qwen-Image / Qwen-Image-Edit | 20B（Image 2.0 / Edit-2511） | 💻 | Apache 2.0 | Nano Banana / Photoshop / DALL·E | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/02-image/qwen-image.md) |
| HiDream-O1-Image | 8B（生成+编辑） | 💻 | MIT | Midjourney / Nano Banana | ⬜ |
| Z-Image | Turbo 6B | 📱→💻 | Apache 2.0 | Midjourney / Nano Banana（快图） | ⬜ |
| SD 3.5 / SDXL | SD3.5 Large 8B / Medium 2.5B · SDXL 3.5B | 📱→💻 | Stability Community / OpenRAIL | DALL·E / Firefly | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/02-image/sd35.md) |

## 03 视频生成（t2v / i2v）

> 底稿 [research/03-video/video-gen.md](/Users/pengpeng/seo/directions/model/research/03-video/video-gen.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| Wan 2.2 | TI2V-5B / T2V-A14B / I2V-A14B | 💻→🏢 | Apache 2.0 | Sora / Kling / Runway | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/03-video/wan-2.md) |
| HunyuanVideo-1.5 | 8.3B（t2v+i2v，超分→1080p） | 💻 | Tencent Community（排除 EU/UK/KR） | Sora / Kling | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/03-video/hunyuanvideo.md) |
| LTX-2 | 19B / 22B（原生音画同步，4K） | 💻→🏢 | LTX-2 Community（<$10M ARR） | Sora（音画一体） | ⬜ |
| Mochi 1 | 10B（纯 t2v） | 🏢→💻 | Apache 2.0 | Runway / Sora | ⬜ |
| CogVideoX | 1.5-5B（t2v+i2v） | 💻 | CogVideoX License（2B 版 Apache） | Pika / Runway | ⬜ |
| SkyReels-V2 | 1.3B / 14B（长视频/无限长） | 📱→🏢 | Wan 架构衍生（见 repo） | Kling / Runway | ⬜ |

## 04 3D 生成（图生 3D / 文生 3D）

> 底稿 [research/04-3d/3d-gen.md](/Users/pengpeng/seo/directions/model/research/04-3d/3d-gen.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| TRELLIS.2 | 4B（图生 3D 开源天花板，PBR） | 💻→🏢 | MIT | Meshy / Rodin / Tripo | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/04-3d/trellis-2.md) |
| Hunyuan3D 2.1 | Shape 3.3B + Paint 2B（文+图+纹理） | 💻→🏢 | Tencent Community（排除 EU/UK/KR） | Meshy / Tripo / Rodin | ⬜ |
| Stable Fast 3D | 1.01B（4–5GB，game-ready UV+PBR） | 📱 | Stability Community（营收<$1M） | Meshy（游戏资产） | ⬜ |
| Hi3DGen | ~1.2B（高保真几何，法线中间表示） | 💻 | MIT | Rodin（几何） | ⬜ |
| TripoSG | 1.5B（纯 MIT 形状 SOTA，8GB） | 📱 | MIT | Tripo 2.0（形状） | ⬜ |

## 05 语音合成 TTS / 声音克隆

> 底稿 [research/05-tts/tts.md](/Users/pengpeng/seo/directions/model/research/05-tts/tts.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| Kokoro | 82M（英语朗读，浏览器可跑） | 📱 | Apache 2.0 | ElevenLabs / OpenAI TTS | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/05-tts/kokoro.md) |
| Piper | 多 VITS 语音 ~5–30M | 📱 | MIT | Amazon Polly / Azure TTS | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/05-tts/piper.md) |
| NeuTTS Air | Air ~0.5B / Nano ~120M（端侧克隆） | 📱 | Apache 2.0（Nano: NeuTTS OL） | ElevenLabs / Play.ht | ⬜ |
| Chatterbox | 0.5B（情绪控制+克隆） | 💻 | MIT | ElevenLabs | ⬜ |
| CosyVoice | 2.0 / 3.0 (0.5B) | 💻 | Apache 2.0 | ElevenLabs / MiniMax | ⬜ |
| Qwen3-TTS | 0.6B / 1.7B（3 秒克隆） | 💻 | Apache 2.0 | ElevenLabs / OpenAI TTS | ⬜ |
| IndexTTS | 2 / 2.5（情绪/时长可控，配音） | 💻 | 自定义（Bilibili License） | ElevenLabs（配音） | ⬜ |
| XTTS-v2 | 467M（17 语言） | 💻 | CPML（非商用） | ElevenLabs | ⬜ |
| Dia | 1.6B（多说话人对话） | 💻 | Apache 2.0 | ElevenLabs（对话） | ⬜ |
| Orpheus-TTS | 3B | 🏢 | Apache 2.0 | ElevenLabs | ⬜ |
| Fish Audio S2 | S2 Pro 4B（80+ 语言） | 🏢 | Fish Research（商用付费） | ElevenLabs / MiniMax | ⬜ |

## 06 语音识别 STT / ASR

> 底稿 [research/06-stt/stt.md](/Users/pengpeng/seo/directions/model/research/06-stt/stt.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| Moonshine | Tiny 27M → Medium 245M（端侧） | 📱 | MIT | Deepgram Flux / 云实时 | ⬜ |
| Qwen3-ASR | 0.6B / 1.7B（52 语言，开源 SOTA） | 📱→💻 | Apache 2.0 | AssemblyAI Universal-3 Pro | ⬜ |
| Whisper | Large v3 (1.55B) / v3 Turbo (809M) | 💻 主力 | MIT | OpenAI gpt-4o-transcribe / Deepgram | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/06-stt/whisper.md) |
| Distil-Whisper | Large v3.5 (756M，英语快转) | 💻 | MIT | — | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/06-stt/distil-whisper.md) |
| Parakeet TDT | 0.6B v3（吞吐王，25 语言） | 💻 | CC-BY-4.0 | Deepgram Nova-3 streaming | ⬜ |
| Canary-Qwen | 2.5B（英语短音频最准） | 💻 | CC-BY-4.0 | ElevenLabs Scribe v2 | ⬜ |
| Voxtral | Mini 4.7B / Small 24B（转写+理解） | 💻→🏢 | Apache 2.0 | Whisper API / ElevenLabs Scribe | ⬜ |
| Granite Speech 3.3 | 2B / 8B（ASR+翻译） | 💻→🏢 | Apache 2.0 | AssemblyAI / Deepgram | ⬜ |

## 07 Embedding / Reranker（本地 RAG）

> 底稿 [research/07-embedding/embedding.md](/Users/pengpeng/seo/directions/model/research/07-embedding/embedding.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| Qwen3-Embedding | 0.6B / 4B / 8B（MTEB 多语 No.1） | 📱→🏢 | Apache 2.0 | text-embedding-3-large / Gemini Embedding | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/07-embedding/qwen3-embedding.md) |
| Qwen3-Reranker | 0.6B / 4B / 8B（cross-encoder） | 💻→🏢 | Apache 2.0 | Cohere Rerank | ⬜ |
| EmbeddingGemma | 308M（<200MB RAM，端侧） | 📱 | Gemma 条款（可商用） | text-embedding-3-small | ⬜ |
| BGE-M3 | ~0.6B（dense+sparse+ColBERT） | 💻 主力 | MIT | text-embedding-3-large / Cohere Embed v3 | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/07-embedding/bge-m3.md) |
| bge-reranker-v2-m3 | cross-encoder（多语言） | 💻 | MIT | Cohere Rerank | ⬜ |
| Nomic Embed | v2 ~0.5B (MoE, ~100 语言) | 📱 | Apache 2.0 | text-embedding-3-small | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/07-embedding/nomic-embed.md) |
| GTE-Qwen2 | 7B-instruct | 🏢 | Apache 2.0 | text-embedding-3-large | ⬜ |
| Stella | en-1.5B-v5（英文） | 💻 | MIT | text-embedding-3-large | ⬜ |

## 08 OCR / 文档理解

> 底稿 [research/08-ocr/ocr.md](/Users/pengpeng/seo/directions/model/research/08-ocr/ocr.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| PaddleOCR-VL | 0.9B（OmniDocBench 榜首，109 语言） | 💻 主力 | Apache 2.0 | Google Document AI / Mistral OCR | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/08-ocr/paddleocr-vl.md) |
| DeepSeek-OCR | 3B MoE（~570M 激活，光学压缩） | 💻 | MIT | AWS Textract | ⬜ |
| dots.ocr | 1.7B（100+ 语言，版面统一） | 💻 | MIT | Google Document AI | ⬜ |
| olmOCR | 7B（大规模 PDF→语料） | 🏢 | Apache 2.0 | Mistral OCR / GPT-4o OCR | ⬜ |
| GOT-OCR2.0 | ~580M（4GB 显存可跑） | 📱→💻 | Apache 2.0 | AWS Textract 基础层 | ⬜ |
| Granite-Docling | 258M（保结构 DocTags，CPU） | 📱 | Apache 2.0 | Azure Document Intelligence | ⬜ |
| MinerU | 2.5-Pro | 💻 | Apache 2.0 | Google Document AI | ⬜ |
| Baidu Unlimited OCR | 开放权重（一次 40+ 页） | 💻 | MIT | Mistral OCR | ⬜ |
| Surya OCR 2 | 650M | 📱→💻 | 开源（见模型卡） | AWS Textract 基础层 | ⬜ |

## 09 机器翻译

> 底稿 [research/09-translation/translation.md](/Users/pengpeng/seo/directions/model/research/09-translation/translation.md)

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| Tencent Hy-MT2 | 1.8B / 7B / 30B-A3B (MoE) | 📱→🏢 | Hunyuan 条款（需查官方） | DeepL / Microsoft / Doubao | ⬜ |
| Tencent HY-MT1.5 | 1.8B / 7B（33 语言） | 📱→💻 | 需查官方 | Gemini-3.0-Pro / Tower-Plus-72B | ⬜ |
| Tencent Hunyuan-MT | 7B + Chimera-7B（WMT25 冠军） | 💻 | 需查官方 | Google Translate / GPT-4.1 / Claude 4 | ⬜ |
| ByteDance Seed-X | 7B（28 语言） | 💻 | OpenMDW（较宽松） | Gemini-2.5 / GPT-4o | ⬜ |
| Unbabel Tower+ | 2B / 9B / 72B | 💻→🏢 | 待核（多 CC-BY-NC） | GPT-4o / Llama-3.3-70B | ⬜ |
| Meta NLLB-200 | 600M–54.5B（200+ 语言） | 📱→🏢 | CC-BY-NC 4.0（禁商用） | Google Translate（低资源语） | ⬜ |
| Google MADLAD-400 | 3B / 7.2B / 10.7B（400+ 语言） | 📱→💻 | Apache 2.0 | DeepL / Google Translate | ⬜ |
| Meta SeamlessM4T v2 | Large 2.3B（语音翻译） | 💻 | CC-BY-NC 4.0 | DeepL Voice / Google 实时翻译 | ⬜ |
| Helsinki-NLP Opus-MT | 数百语对小模型（数十–百 M，CPU） | 📱 | CC-BY 4.0 | Google Translate（单语对） | ⬜ |

## 10 音乐 / 音频生成

> 底稿 [research/10-music/music-gen.md](/Users/pengpeng/seo/directions/model/research/10-music/music-gen.md)

> 唯一主推：ACE-Step 1.5——同时满足可商用（MIT）+ 消费级显存（<4GB 起）+ 生态最成熟。

| 模型 family | 代表型号/尺寸（忽略量化） | 部署层级 | 许可 | 闭源对标 | 报告 |
|------|-----------|------|------|---------|------|
| ACE-Step 1.5 | 基础 2B DiT / XL 4B DiT + LM planner | 💻→🏢 | MIT | Suno v5 / Udio | ✅ [报告](/Users/pengpeng/seo/directions/model/reports/10-music/ace-step.md) |

---

> 型号与候选关键词均以各章 [research/](/Users/pengpeng/seo/directions/model/research) 底稿为准；补报告走 [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)，产出落 `reports/<章>/<model>.md`，再把本表报告列改为 ✅。
