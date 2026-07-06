#!/usr/bin/env python3
"""Wave 1 tracking update: models(38) + privacy(2) + market(20)"""

import os
os.chdir('/Users/pengpeng/seo')

# ============================================================
# 1. models.md — 38 items (6 already had reports, 32 new)
# ============================================================
with open('directions/model/models.md', 'r') as f:
    models = f.read()

models_updates = [
    # --- 6 already-done, tracking fix ---
    ('| GLM-5.2 | 744B-A40B | 🏢 | MIT | GPT-5.5 / Claude Opus 4.8 | ⬜ |',
     '| GLM-5.2 | 744B-A40B | 🏢 | MIT | GPT-5.5 / Claude Opus 4.8 | ✅ [报告](directions/model/reports/01-llm/glm-5.md) |'),
    ('| HiDream-O1-Image | 8B（生成+编辑） | 💻 | MIT | Midjourney / Nano Banana | ⬜ |',
     '| HiDream-O1-Image | 8B（生成+编辑） | 💻 | MIT | Midjourney / Nano Banana | ✅ [报告](directions/model/reports/02-image/hidream-o1.md) |'),
    ('| TripoSG | 1.5B（纯 MIT 形状 SOTA，8GB） | 📱 | MIT | Tripo 2.0（形状） | ⬜ |',
     '| TripoSG | 1.5B（纯 MIT 形状 SOTA，8GB） | 📱 | MIT | Tripo 2.0（形状） | ✅ [报告](directions/model/reports/04-3d/triposg.md) |'),
    ('| Parakeet TDT | 0.6B v3（吞吐王，25 语言） | 💻 | CC-BY-4.0 | Deepgram Nova-3 streaming | ⬜ |',
     '| Parakeet TDT | 0.6B v3（吞吐王，25 语言） | 💻 | CC-BY-4.0 | Deepgram Nova-3 streaming | ✅ [报告](directions/model/reports/06-stt/parakeet-tdt.md) |'),
    ('| EmbeddingGemma | 308M（<200MB RAM，端侧） | 📱 | Gemma 条款（可商用） | text-embedding-3-small | ⬜ |',
     '| EmbeddingGemma | 308M（<200MB RAM，端侧） | 📱 | Gemma 条款（可商用） | text-embedding-3-small | ✅ [报告](directions/model/reports/07-embedding/embedding-gemma.md) |'),
    ('| bge-reranker-v2-m3 | cross-encoder（多语言） | 💻 | MIT | Cohere Rerank | ⬜ |',
     '| bge-reranker-v2-m3 | cross-encoder（多语言） | 💻 | MIT | Cohere Rerank | ✅ [报告](directions/model/reports/07-embedding/bge-reranker.md) |'),
    # --- 32 new Wave 1 models ---
    ('| Z-Image | Turbo 6B | 📱→💻 | Apache 2.0 | Midjourney / Nano Banana（快图） | ⬜ |',
     '| Z-Image | Turbo 6B | 📱→💻 | Apache 2.0 | Midjourney / Nano Banana（快图） | ✅ [报告](directions/model/reports/02-image/z-image.md) |'),
    ('| Stable Fast 3D | 1.01B（4–5GB，game-ready UV+PBR） | 📱 | Stability Community（营收<$1M） | Meshy（游戏资产） | ⬜ |',
     '| Stable Fast 3D | 1.01B（4–5GB，game-ready UV+PBR） | 📱 | Stability Community（营收<$1M） | Meshy（游戏资产） | ✅ [报告](directions/model/reports/04-3d/stable-fast-3d.md) |'),
    ('| Hi3DGen | ~1.2B（高保真几何，法线中间表示） | 💻 | MIT | Rodin（几何） | ⬜ |',
     '| Hi3DGen | ~1.2B（高保真几何，法线中间表示） | 💻 | MIT | Rodin（几何） | ✅ [报告](directions/model/reports/04-3d/hi3dgen.md) |'),
    ('| NeuTTS Air | Air ~0.5B / Nano ~120M（端侧克隆） | 📱 | Apache 2.0（Nano: NeuTTS OL） | ElevenLabs / Play.ht | ⬜ |',
     '| NeuTTS Air | Air ~0.5B / Nano ~120M（端侧克隆） | 📱 | Apache 2.0（Nano: NeuTTS OL） | ElevenLabs / Play.ht | ✅ [报告](directions/model/reports/05-tts/neutts.md) |'),
    ('| Qwen3-TTS | 0.6B / 1.7B（3 秒克隆） | 💻 | Apache 2.0 | ElevenLabs / OpenAI TTS | ⬜ |',
     '| Qwen3-TTS | 0.6B / 1.7B（3 秒克隆） | 💻 | Apache 2.0 | ElevenLabs / OpenAI TTS | ✅ [报告](directions/model/reports/05-tts/qwen3-tts.md) |'),
    ('| IndexTTS | 2 / 2.5（情绪/时长可控，配音） | 💻 | 自定义（Bilibili License） | ElevenLabs（配音） | ⬜ |',
     '| IndexTTS | 2 / 2.5（情绪/时长可控，配音） | 💻 | 自定义（Bilibili License） | ElevenLabs（配音） | ✅ [报告](directions/model/reports/05-tts/indextts.md) |'),
    ('| XTTS-v2 | 467M（17 语言） | 💻 | CPML（非商用） | ElevenLabs | ⬜ |',
     '| XTTS-v2 | 467M（17 语言） | 💻 | CPML（非商用） | ElevenLabs | ✅ [报告](directions/model/reports/05-tts/xtts-v2.md) |'),
    ('| Dia | 1.6B（多说话人对话） | 💻 | Apache 2.0 | ElevenLabs（对话） | ⬜ |',
     '| Dia | 1.6B（多说话人对话） | 💻 | Apache 2.0 | ElevenLabs（对话） | ✅ [报告](directions/model/reports/05-tts/dia.md) |'),
    ('| Orpheus-TTS | 3B | 🏢 | Apache 2.0 | ElevenLabs | ⬜ |',
     '| Orpheus-TTS | 3B | 🏢 | Apache 2.0 | ElevenLabs | ✅ [报告](directions/model/reports/05-tts/orpheus-tts.md) |'),
    ('| Fish Audio S2 | S2 Pro 4B（80+ 语言） | 🏢 | Fish Research（商用付费） | ElevenLabs / MiniMax | ⬜ |',
     '| Fish Audio S2 | S2 Pro 4B（80+ 语言） | 🏢 | Fish Research（商用付费） | ElevenLabs / MiniMax | ✅ [报告](directions/model/reports/05-tts/fish-audio.md) |'),
    ('| Canary-Qwen | 2.5B（英语短音频最准） | 💻 | CC-BY-4.0 | ElevenLabs Scribe v2 | ⬜ |',
     '| Canary-Qwen | 2.5B（英语短音频最准） | 💻 | CC-BY-4.0 | ElevenLabs Scribe v2 | ✅ [报告](directions/model/reports/06-stt/canary-qwen.md) |'),
    ('| Voxtral | Mini 4.7B / Small 24B（转写+理解） | 💻→🏢 | Apache 2.0 | Whisper API / ElevenLabs Scribe | ⬜ |',
     '| Voxtral | Mini 4.7B / Small 24B（转写+理解） | 💻→🏢 | Apache 2.0 | Whisper API / ElevenLabs Scribe | ✅ [报告](directions/model/reports/06-stt/voxtral.md) |'),
    ('| Granite Speech 3.3 | 2B / 8B（ASR+翻译） | 💻→🏢 | Apache 2.0 | AssemblyAI / Deepgram | ⬜ |',
     '| Granite Speech 3.3 | 2B / 8B（ASR+翻译） | 💻→🏢 | Apache 2.0 | AssemblyAI / Deepgram | ✅ [报告](directions/model/reports/06-stt/granite-speech.md) |'),
    ('| GTE-Qwen2 | 7B-instruct | 🏢 | Apache 2.0 | text-embedding-3-large | ⬜ |',
     '| GTE-Qwen2 | 7B-instruct | 🏢 | Apache 2.0 | text-embedding-3-large | ✅ [报告](directions/model/reports/07-embedding/gte-qwen2.md) |'),
    ('| Stella | en-1.5B-v5（英文） | 💻 | MIT | text-embedding-3-large | ⬜ |',
     '| Stella | en-1.5B-v5（英文） | 💻 | MIT | text-embedding-3-large | ✅ [报告](directions/model/reports/07-embedding/stella.md) |'),
    ('| DeepSeek-OCR | 3B MoE（~570M 激活，光学压缩） | 💻 | MIT | AWS Textract | ⬜ |',
     '| DeepSeek-OCR | 3B MoE（~570M 激活，光学压缩） | 💻 | MIT | AWS Textract | ✅ [报告](directions/model/reports/08-ocr/deepseek-ocr.md) |'),
    ('| dots.ocr | 1.7B（100+ 语言，版面统一） | 💻 | MIT | Google Document AI | ⬜ |',
     '| dots.ocr | 1.7B（100+ 语言，版面统一） | 💻 | MIT | Google Document AI | ✅ [报告](directions/model/reports/08-ocr/dots-ocr.md) |'),
    ('| olmOCR | 7B（大规模 PDF→语料） | 🏢 | Apache 2.0 | Mistral OCR / GPT-4o OCR | ⬜ |',
     '| olmOCR | 7B（大规模 PDF→语料） | 🏢 | Apache 2.0 | Mistral OCR / GPT-4o OCR | ✅ [报告](directions/model/reports/08-ocr/olmocr.md) |'),
    ('| GOT-OCR2.0 | ~580M（4GB 显存可跑） | 📱→💻 | Apache 2.0 | AWS Textract 基础层 | ⬜ |',
     '| GOT-OCR2.0 | ~580M（4GB 显存可跑） | 📱→💻 | Apache 2.0 | AWS Textract 基础层 | ✅ [报告](directions/model/reports/08-ocr/got-ocr.md) |'),
    ('| Granite-Docling | 258M（保结构 DocTags，CPU） | 📱 | Apache 2.0 | Azure Document Intelligence | ⬜ |',
     '| Granite-Docling | 258M（保结构 DocTags，CPU） | 📱 | Apache 2.0 | Azure Document Intelligence | ✅ [报告](directions/model/reports/08-ocr/granite-docling.md) |'),
    ('| MinerU | 2.5-Pro | 💻 | Apache 2.0 | Google Document AI | ⬜ |',
     '| MinerU | 2.5-Pro | 💻 | Apache 2.0 | Google Document AI | ✅ [报告](directions/model/reports/08-ocr/mineru.md) |'),
    ('| Baidu Unlimited OCR | 开放权重（一次 40+ 页） | 💻 | MIT | Mistral OCR | ⬜ |',
     '| Baidu Unlimited OCR | 开放权重（一次 40+ 页） | 💻 | MIT | Mistral OCR | ✅ [报告](directions/model/reports/08-ocr/baidu-ocr.md) |'),
    ('| Surya OCR 2 | 650M | 📱→💻 | 开源（见模型卡） | AWS Textract 基础层 | ⬜ |',
     '| Surya OCR 2 | 650M | 📱→💻 | 开源（见模型卡） | AWS Textract 基础层 | ✅ [报告](directions/model/reports/08-ocr/surya-ocr.md) |'),
    ('| Tencent Hy-MT2 | 1.8B / 7B / 30B-A3B (MoE) | 📱→🏢 | Hunyuan 条款（需查官方） | DeepL / Microsoft / Doubao | ⬜ |',
     '| Tencent Hy-MT2 | 1.8B / 7B / 30B-A3B (MoE) | 📱→🏢 | Hunyuan 条款（需查官方） | DeepL / Microsoft / Doubao | ✅ [报告](directions/model/reports/09-translation/tencent-hy-mt2.md) |'),
    ('| Tencent HY-MT1.5 | 1.8B / 7B（33 语言） | 📱→💻 | 需查官方 | Gemini-3.0-Pro / Tower-Plus-72B | ⬜ |',
     '| Tencent HY-MT1.5 | 1.8B / 7B（33 语言） | 📱→💻 | 需查官方 | Gemini-3.0-Pro / Tower-Plus-72B | ✅ [报告](directions/model/reports/09-translation/tencent-hy-mt15.md) |'),
    ('| Tencent Hunyuan-MT | 7B + Chimera-7B（WMT25 冠军） | 💻 | 需查官方 | Google Translate / GPT-4.1 / Claude 4 | ⬜ |',
     '| Tencent Hunyuan-MT | 7B + Chimera-7B（WMT25 冠军） | 💻 | 需查官方 | Google Translate / GPT-4.1 / Claude 4 | ✅ [报告](directions/model/reports/09-translation/hunyuan-mt.md) |'),
    ('| ByteDance Seed-X | 7B（28 语言） | 💻 | OpenMDW（较宽松） | Gemini-2.5 / GPT-4o | ⬜ |',
     '| ByteDance Seed-X | 7B（28 语言） | 💻 | OpenMDW（较宽松） | Gemini-2.5 / GPT-4o | ✅ [报告](directions/model/reports/09-translation/bytedance-seed-x.md) |'),
    ('| Unbabel Tower+ | 2B / 9B / 72B | 💻→🏢 | 待核（多 CC-BY-NC） | GPT-4o / Llama-3.3-70B | ⬜ |',
     '| Unbabel Tower+ | 2B / 9B / 72B | 💻→🏢 | 待核（多 CC-BY-NC） | GPT-4o / Llama-3.3-70B | ✅ [报告](directions/model/reports/09-translation/unbabel-tower.md) |'),
    ('| Meta NLLB-200 | 600M–54.5B（200+ 语言） | 📱→🏢 | CC-BY-NC 4.0（禁商用） | Google Translate（低资源语） | ⬜ |',
     '| Meta NLLB-200 | 600M–54.5B（200+ 语言） | 📱→🏢 | CC-BY-NC 4.0（禁商用） | Google Translate（低资源语） | ✅ [报告](directions/model/reports/09-translation/nllb-200.md) |'),
    ('| Google MADLAD-400 | 3B / 7.2B / 10.7B（400+ 语言） | 📱→💻 | Apache 2.0 | DeepL / Google Translate | ⬜ |',
     '| Google MADLAD-400 | 3B / 7.2B / 10.7B（400+ 语言） | 📱→💻 | Apache 2.0 | DeepL / Google Translate | ✅ [报告](directions/model/reports/09-translation/madlad-400.md) |'),
    ('| Meta SeamlessM4T v2 | Large 2.3B（语音翻译） | 💻 | CC-BY-NC 4.0 | DeepL Voice / Google 实时翻译 | ⬜ |',
     '| Meta SeamlessM4T v2 | Large 2.3B（语音翻译） | 💻 | CC-BY-NC 4.0 | DeepL Voice / Google 实时翻译 | ✅ [报告](directions/model/reports/09-translation/seamlessm4t.md) |'),
    ('| Helsinki-NLP Opus-MT | 数百语对小模型（数十–百 M，CPU） | 📱 | CC-BY 4.0 | Google Translate（单语对） | ⬜ |',
     '| Helsinki-NLP Opus-MT | 数百语对小模型（数十–百 M，CPU） | 📱 | CC-BY 4.0 | Google Translate（单语对） | ✅ [报告](directions/model/reports/09-translation/opus-mt.md) |'),
]

ok_models = 0
for old, new in models_updates:
    if old in models:
        models = models.replace(old, new)
        ok_models += 1
        print(f"✅ models: {old[:60]}...")
    else:
        print(f"❌ models NOT FOUND: {old[:70]}")

with open('directions/model/models.md', 'w') as f:
    f.write(models)
print(f"--- models.md done ({ok_models}/{len(models_updates)} updated) ---\n")


# ============================================================
# 2. landscape.md — 2 privacy items
# ============================================================
with open('directions/privacy/landscape.md', 'r') as f:
    landscape = f.read()

landscape_updates = [
    ('| 端侧 vs 云 | `local LLM vs cloud AI privacy`、`on device AI privacy`、`Ollama privacy` | Ollama/vLLM on Olares | ⬜ |',
     '| 端侧 vs 云 | `local LLM vs cloud AI privacy`、`on device AI privacy`、`Ollama privacy` | Ollama/vLLM on Olares | ✅ [报告](directions/privacy/reports/local-vs-cloud.md) |'),
    ('| AI Act 透明度 | `EU AI Act chatbot disclosure`、`deepfake labeling` | 自部署 chatbot 数据路径更短 | ⬜ |',
     '| AI Act 透明度 | `EU AI Act chatbot disclosure`、`deepfake labeling` | 自部署 chatbot 数据路径更短 | ✅ [报告](directions/privacy/reports/ai-act-transparency.md) |'),
]

ok_landscape = 0
for old, new in landscape_updates:
    if old in landscape:
        landscape = landscape.replace(old, new)
        ok_landscape += 1
        print(f"✅ landscape: {old[:60]}...")
    else:
        print(f"❌ landscape NOT FOUND: {old[:70]}")

with open('directions/privacy/landscape.md', 'w') as f:
    f.write(landscape)
print(f"--- landscape.md done ({ok_landscape}/{len(landscape_updates)} updated) ---\n")


# ============================================================
# 3. apps.md — first 20 market items
# ============================================================
with open('directions/market/apps.md', 'r') as f:
    apps = f.read()

apps_updates = [
    ('| DeepSeek-OCR2 WebUI V3 | Ready-to-use DeepSeek-OCR-2 Web UI | ⬜ |',
     '| DeepSeek-OCR2 WebUI V3 | Ready-to-use DeepSeek-OCR-2 Web UI | ✅ [报告](directions/market/reports/deepseek-ocr2-webui.md) |'),
    ('| Fish Speech | SOTA Open Source TTS | ⬜ |',
     '| Fish Speech | SOTA Open Source TTS | ✅ [报告](directions/market/reports/fish-speech.md) |'),
    ('| KoboldCpp | 本地 LLM 推理与角色扮演前端 | ⬜ |',
     '| KoboldCpp | 本地 LLM 推理与角色扮演前端 | ✅ [报告](directions/market/reports/koboldcpp.md) |'),
    ('| OpenedAI Speech | An OpenAI API compatible text to speech server using Coqui AI and/or piper TTS as the backend. | ⬜ |',
     '| OpenedAI Speech | An OpenAI API compatible text to speech server using Coqui AI and/or piper TTS as the backend. | ✅ [报告](directions/market/reports/openedai-speech.md) |'),
    ('| Rembg | Rembg is a tool to remove images background | ⬜ |',
     '| Rembg | Rembg is a tool to remove images background | ✅ [报告](directions/market/reports/rembg.md) |'),
    ('| Whisper API | FastAPI service on top of WhisperX | ⬜ |',
     '| Whisper API | FastAPI service on top of WhisperX | ✅ [报告](directions/market/reports/whisper-api.md) |'),
    ('| Whisper-WebUI | A Web UI for easy subtitle using whisper model. | ⬜ |',
     '| Whisper-WebUI | A Web UI for easy subtitle using whisper model. | ✅ [报告](directions/market/reports/whisper-webui.md) |'),
    ('| Agent Zero | Agentic AI Framework | ⬜ |',
     '| Agent Zero | Agentic AI Framework | ✅ [报告](directions/market/reports/agent-zero.md) |'),
    ('| AI Router | AI Router | ⬜ |',
     '| AI Router | AI Router | ✅ [报告](directions/market/reports/ai-router.md) |'),
    ('| Answer | A Q&A platform software for teams at any scales. | ⬜ |',
     '| Answer | A Q&A platform software for teams at any scales. | ✅ [报告](directions/market/reports/answer.md) |'),
    ('| BISHENG | Open LLM devops platform for next generation Enterprise AI applications | ⬜ |',
     '| BISHENG | Open LLM devops platform for next generation Enterprise AI applications | ✅ [报告](directions/market/reports/bisheng.md) |'),
    ('| Blinko | An open-source, self-hosted personal AI note tool prioritizing privacy | ⬜ |',
     '| Blinko | An open-source, self-hosted personal AI note tool prioritizing privacy | ✅ [报告](directions/market/reports/blinko.md) |'),
    ('| Cloudreve | Self-hosted file management system with muilt-cloud support. | ⬜ |',
     '| Cloudreve | Self-hosted file management system with muilt-cloud support. | ✅ [报告](directions/market/reports/cloudreve.md) |'),
    ('| Docmost | Open-source collaborative wiki and documentation software. | ⬜ |',
     '| Docmost | Open-source collaborative wiki and documentation software. | ✅ [报告](directions/market/reports/docmost.md) |'),
    ('| Documenso | The Open Source DocuSign Alternative. | ⬜ |',
     '| Documenso | The Open Source DocuSign Alternative. | ✅ [报告](directions/market/reports/documenso.md) |'),
    ('| Formbricks | Open Source Qualtrics Alternative | ⬜ |',
     '| Formbricks | Open Source Qualtrics Alternative | ✅ [报告](directions/market/reports/formbricks.md) |'),
    ('| Freqtrade | Free, open source crypto trading bot | ⬜ |',
     '| Freqtrade | Free, open source crypto trading bot | ✅ [报告](directions/market/reports/freqtrade.md) |'),
    ('| Grafana | Grafana is a multi-platform open source analytics and interactive visualization web application. | ⬜ |',
     '| Grafana | Grafana is a multi-platform open source analytics and interactive visualization web application. | ✅ [报告](directions/market/reports/grafana.md) |'),
    ('| IsaacLab | Unified framework for robot learning built on NVIDIA Isaac Sim | ⬜ |',
     '| IsaacLab | Unified framework for robot learning built on NVIDIA Isaac Sim | ✅ [报告](directions/market/reports/isaaclab.md) |'),
    ('| Leantime | Leantime is a goals focused project management system for non-project managers. | ⬜ |',
     '| Leantime | Leantime is a goals focused project management system for non-project managers. | ✅ [报告](directions/market/reports/leantime.md) |'),
]

ok_apps = 0
for old, new in apps_updates:
    if old in apps:
        apps = apps.replace(old, new)
        ok_apps += 1
        print(f"✅ apps: {old[:60]}...")
    else:
        print(f"❌ apps NOT FOUND: {old[:70]}")

with open('directions/market/apps.md', 'w') as f:
    f.write(apps)
print(f"--- apps.md done ({ok_apps}/{len(apps_updates)} updated) ---\n")

print(f"\n=== TOTAL: models={ok_models}/38, landscape={ok_landscape}/2, apps={ok_apps}/20 ===")
