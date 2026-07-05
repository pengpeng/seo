# model/models.md — 开源 AI 模型清单

> 值得为 Olares 做 SEO/内容的**开源模型** family（只收开源；闭源模型/API 如 GPT、Claude、Gemini 归 [commerce/](/Users/pengpeng/seo/directions/commerce)）。清单整理自 [keywords.md](/Users/pengpeng/seo/directions/model/keywords.md)（11 类型号关键词底稿）。模型没有 `terminus-apps` 那样的 manifest 仓库，故本清单**手工维护**，非脚本生成。每个 family 的报告放在 [reports/](/Users/pengpeng/seo/directions/model/reports)。

**报告状态**：✅ 独立报告 ｜ ✅(合并) 收录于分类合并报告 [other-models.md](/Users/pengpeng/seo/directions/model/reports/other-models.md)（TTS/STT/Embedding/翻译/3D/OCR/音乐/Omni 等按类合并）｜ ⏳ 待做

**闭源对标**：每个 family 标出它替代的商业产品，是"open source X / X alternative / run X locally"内容的切入点。

## LLM 文本生成（6）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| GLM | 智谱 ZAI，编码强（z.ai） | GPT / Claude（编码） | ✅ [glm](/Users/pengpeng/seo/directions/model/reports/glm.md) |
| Kimi K2 | 月之暗面，长上下文 + 编码（kimi.com） | Claude / GPT | ✅ [kimi-k2](/Users/pengpeng/seo/directions/model/reports/kimi-k2.md) |
| MiniMax | MiniMax，Agent + 音频强（minimax.io） | GPT / Claude | ✅ [minimax](/Users/pengpeng/seo/directions/model/reports/minimax.md) |
| Qwen 3.6 | 阿里通义，全能开源 | GPT / Llama | ✅ [qwen36](/Users/pengpeng/seo/directions/model/reports/qwen36.md) |
| Gemma 4 | Google，轻量开放权重（KD 极低） | GPT / Llama | ✅ [gemma4](/Users/pengpeng/seo/directions/model/reports/gemma4.md) |
| Ornith | 新兴 agentic 编码模型，MIT | Claude（编码） | ✅ [ornith](/Users/pengpeng/seo/directions/model/reports/ornith.md) |

## 图像生成（5）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| FLUX.2 | Black Forest Labs，klein-4B 消费级（bfl.ai，Apache 2.0） | Midjourney / DALL·E | ✅ [flux2](/Users/pengpeng/seo/directions/model/reports/flux2.md) |
| Ideogram 4 | 文字渲染最强，9.3B 开放权重（非商用许可，商用另购） | Midjourney | ✅ [ideogram4](/Users/pengpeng/seo/directions/model/reports/ideogram4.md) |
| HiDream | O1「先推理再画」 | Midjourney / FLUX | ✅ [hidream](/Users/pengpeng/seo/directions/model/reports/hidream.md) |
| Krea 2 | 文生图评测 #1，12B 开放权重（社区许可，营收<$1M 可商用） | Midjourney | ✅ [krea2](/Users/pengpeng/seo/directions/model/reports/krea2.md) |
| Qwen Image Edit | 阿里，多图编辑（Apache 2.0，20B） | Photoshop / Nano Banana | ✅ [qwen-image-edit](/Users/pengpeng/seo/directions/model/reports/qwen-image-edit.md) |

## 视频生成（3）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| Wan | 阿里 Wan-AI，搜索量最大的开源视频模型（Apache 2.0） | Sora / Runway / Kling | ✅ [wan](/Users/pengpeng/seo/directions/model/reports/wan.md) |
| SkyReels | 昆仑万维（skyreels.ai，自定义许可） | Sora / Kling | ✅ [skyreels](/Users/pengpeng/seo/directions/model/reports/skyreels.md) |
| HunyuanVideo | 腾讯，i2v（自定义许可，有地区限制） | Sora / Runway | ✅ [hunyuanvideo](/Users/pengpeng/seo/directions/model/reports/hunyuanvideo.md) |

## 3D 生成（5）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| TRELLIS | 微软，MIT | Meshy / Tripo | ✅(合并) |
| Hunyuan3D | 腾讯 | Meshy / Tripo | ✅(合并) |
| Hi3DGen | Stable-X，MIT | Meshy / Tripo | ✅(合并) |
| TripoSR | Stability AI，MIT | Meshy / Tripo | ✅(合并) |
| Stable Fast 3D | Stability AI | Meshy / Tripo | ⏳ |

## 语音合成 TTS（5）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| Kokoro | hexgrad，82M 轻量 | ElevenLabs | ✅(合并) |
| Fish Speech | fishaudio，TTS-Arena2 #1 | ElevenLabs | ✅(合并) |
| CosyVoice2 | 阿里，Apache 2.0 | ElevenLabs | ✅(合并) |
| IndexTTS | 字节，零样本视频配音 | ElevenLabs | ✅(合并) |
| Qwen3-TTS | 阿里，流式 + 声音设计（Apache 2.0） | ElevenLabs | ✅(合并) |

## 语音识别 STT（3）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| Whisper | OpenAI，MIT | 云 ASR / Otter | ✅(合并) |
| Qwen3-ASR | 阿里，开源 ASR SOTA，52 语言 | 云 ASR | ✅(合并) |
| Qwen2-Audio | 阿里，多模态音频理解 | 云 ASR | ✅(合并) |

## Embedding（3）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| BGE-M3 | BAAI，多语言生产首选（CPC 极高） | OpenAI embeddings | ✅(合并) |
| Nomic Embed | nomic-ai，轻量 | OpenAI embeddings | ✅(合并) |
| Qwen3 Embedding | 阿里，MTEB SOTA | OpenAI embeddings | ✅(合并) |

## OCR（2）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| DeepSeek OCR | 文档处理（CPC 高） | Textract / Mistral OCR | ✅(合并) |
| Unlimited OCR | 百度，MIT（新发布） | Textract | ✅(合并) |

## 翻译（2）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| Hy-MT2 | 腾讯，WMT25 冠军 | DeepL / Google Translate | ✅(合并) |
| NLLB-200 | Meta，200 语言轻量备选 | DeepL / Google Translate | ✅(合并) |

## 音乐生成（1）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| ACE-Step | 开源音乐生成（KD 极低） | Suno / Udio | ✅(合并) |

## 多模态 Omni（1）

| 模型 | 说明 / 许可 | 闭源对标 | 报告 |
|------|-----------|---------|------|
| Qwen3-Omni | 阿里，文本+图像+音频+视频端到端 | GPT-4o | ✅(合并) |

---

## 跨模型优先内容方向（数据快照 2026-07-02）

综合搜索量 × KD，各 family 里最值得先做内容的词（详见各自报告）：

| 优先级 | 关键词 | 量 | KD | 方向 |
|--------|--------|----|----|------|
| ⭐⭐⭐ | ace step 1.5 | 880 | 0 | 音乐生成，零竞争，立即占位 |
| ⭐⭐⭐ | bge-m3 | 4,400 | 32 | Embedding / RAG 教程（CPC=$9.32） |
| ⭐⭐⭐ | trellis 2 | 170 | 26 | Olares Market 上 3D 生成页面 |
| ⭐⭐ | glm 5.1 | 480 | 28 | GLM 系列最低 KD 型号词 |
| ⭐⭐ | gemma 4 | 590 | 24 | Google 开源，低 KD |
| ⭐⭐ | wan2.1 i2v | 1,300 | 32 | 图生视频教程 |
| ⭐⭐ | hi3dgen | 260 | 26 | 3D 生成教程 |
| ⭐⭐ | whisper large v3 turbo | 260 | 31 | STT，CPC=$3.19 商业价值高 |
| ⭐⭐ | qwen image edit 2511 | 210 | 29 | 最新版图像编辑 |
| ⭐ | ornith | 260 | 30 | 编码 agent 新词 |

意外发现：
- **trellis（90,500 月搜，KD=44）**：多数是"园艺格架"通用词，但 AI 竞争者少，可借力巨大流量（类似 Ollama 借 llama）。
- **kimi k2.5（49,500）> kimi k2（22,200）**：用户已在搜具体版本号，型号词不能忽略。
- **kokoro（14,800，KD=50）**：TTS 里量最高，日语词"心/感情"带来品牌借力。
- **bge-m3 vs bge m3**：带横线写法量是不带的 7.5 倍，标题统一用 `bge-m3`。

---
> 共 36 个 family：14 个有独立报告，21 个按类合并在 [other-models.md](/Users/pengpeng/seo/directions/model/reports/other-models.md)，1 个（Stable Fast 3D）待做。型号级关键词底稿见 [keywords.md](/Users/pengpeng/seo/directions/model/keywords.md)；补新报告走 `.cursor/skills/model-seo-research/`。
