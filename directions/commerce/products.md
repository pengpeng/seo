# commerce/products.md — 商业付费 AI / SaaS 竞品清单

> **闭源商业** AI / SaaS 产品竞品清单（含闭源模型/API 如 OpenAI、Anthropic、Gemini；开源模型归 [model/](/Users/pengpeng/seo/directions/model)、可自部署项目归 [market/](/Users/pengpeng/seo/directions/market)），对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 1。AS_OF：2026-07-04。
>
> **入选门槛（满足其一）**：AI 产品 ARR>$50M ｜ 估值>$200M ｜ 累计融资>$20M ｜ 大厂旗舰；成熟 SaaS 市值>$5B ｜ ARR>$200M。
> **文档范围原则**：原则上不讨论纯粹面向开发者的产品（移附录）；但有强开源自托管平替、与 Olares 叙事契合者可破例纳入。
> **报告列**：✅=已有报告（部分数据以后重跑）｜⬜=达标待调研（批准后跑 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)）。报告文件按大类/细类归入 [reports/](/Users/pengpeng/seo/directions/commerce/reports)，命名与目录树见 [README.md](/Users/pengpeng/seo/directions/commerce/README.md)。冲突/存疑数字标 `[u]`。
> **附录**：次级/纯开发者/出范围项见 [products-appendix.md](/Users/pengpeng/seo/directions/commerce/products-appendix.md)。家居/可穿戴 IoT 已独立为 [iot/iot.md](/Users/pengpeng/seo/directions/iot/iot.md)（方向 7）。

---

## 一、模型层

### 1. 前沿模型实验室（闭源模型 + API）
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替（开源） | 报告 |
|------|------|------|---------|------------|------|
| OpenAI (ChatGPT/GPT/API) | OpenAI | openai.com | ARR ~$25B；估值 $852B | Open WebUI + Ollama | ✅ [openai](reports/01-model/frontier-labs/openai.md) |
| Anthropic (Claude) | Anthropic | anthropic.com | run-rate ~$30B；估值 $380B | LibreChat + Ollama | ✅ [anthropic](reports/01-model/frontier-labs/anthropic.md) |
| Google Gemini | Alphabet | gemini.google.com | 大厂旗舰 | Qwen3-Omni + Open WebUI | ✅ [gemini](reports/01-model/frontier-labs/gemini.md) |
| Meta Llama / Meta AI | Meta | meta.ai | 大厂旗舰 | Llama/Qwen via Ollama | ✅ [meta-llama](reports/01-model/frontier-labs/meta-llama.md) |
| xAI Grok | xAI | x.ai | ARR ~$1.5B；估值 ~$200B+ | Open WebUI + Ollama | ✅ [grok](reports/01-model/frontier-labs/grok.md) |
| Mistral | Mistral | mistral.ai | ARR ~$1B；估值 ~$15B | Ollama（Mistral 开源权重） | ✅ [mistral](reports/01-model/frontier-labs/mistral.md) |
| Cohere | Cohere | cohere.com | ARR ~$500M；估值 ~$7B | BGE-M3 + bge-reranker | ✅ [cohere](reports/01-model/frontier-labs/cohere.md) |
| DeepSeek | DeepSeek | deepseek.com | 估值 >$50B；融资 $7.4B | DeepSeek 权重 + Ollama | ✅ [deepseek](reports/01-model/frontier-labs/deepseek.md) |
| Moonshot (Kimi) | Moonshot | moonshot.cn | ARR >$200M；估值 $20B | Kimi K2 + Ollama | ✅ [moonshot](reports/01-model/frontier-labs/moonshot.md) |
| Zhipu (GLM) | Zhipu | zhipuai.cn | 市值 >$112B；API ARR ~$230M | GLM 权重 + Ollama | ✅ [zhipu](reports/01-model/frontier-labs/zhipu.md) |
| MiniMax | MiniMax | minimax.io | ARR ≥$300M；市值 ~$32B | MiniMax 权重 | ✅ [minimax](reports/01-model/frontier-labs/minimax.md) |
| AI21 Labs | AI21 | ai21.com | ARR ~$58M；估值 $1.4B | Ollama | ✅ [ai21](reports/01-model/frontier-labs/ai21.md) |
| Baidu ERNIE | Baidu | yiyan.baidu.com | 市值 ~$42B；旗舰 | ERNIE 权重 + Ollama | ✅ [baidu-ernie](reports/01-model/frontier-labs/baidu-ernie.md) |
| Alibaba Qwen | Alibaba | qwen.ai | 市值 ~$310B；旗舰 | Qwen 3.6 + Ollama | ✅ [qwen](reports/01-model/frontier-labs/qwen.md) |
| ByteDance Doubao | ByteDance | doubao.com | 估值 $400–550B；旗舰 | 无直接平替（闭源） | ✅ [doubao](reports/01-model/frontier-labs/doubao.md) |
| Tencent Hunyuan | Tencent | hunyuan.tencent.com | 市值 ~$520B；旗舰 | Hunyuan 权重 | ✅ [hunyuan](reports/01-model/frontier-labs/hunyuan.md) |
| Reka | Reka | reka.ai | 估值 $1.3B；融资 ~$167M | Ollama | ✅ [reka](reports/01-model/frontier-labs/reka.md) |
| Stability AI | Stability AI | stability.ai | 估值 ~$1B；融资 $181M+ | ComfyUI（SD 权重，**开源权重可自托管**） | ✅ [stability-ai](reports/01-model/frontier-labs/stability-ai.md) |

### 2. 模型网关 / 路由
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| OpenRouter | OpenRouter | openrouter.ai | ARR ~$50M；估值 $1.3B | LiteLLM / Bifrost | ✅ [openrouter](reports/01-model/gateway/openrouter.md) |
| Vercel AI Gateway | Vercel | vercel.com/ai | 母公司估值 $9.3B | LiteLLM / AI Router | ✅ [vercel-ai](reports/01-model/gateway/vercel-ai.md) |

### 3. 多模型客户端 / 聚合
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Poe | Quora | poe.com | ARR ~$65M[u]；融资 $75M | LibreChat / LobeChat + Ollama | ✅ [poe](reports/01-model/aggregator/poe.md) |
| Monica | Butterfly Effect | monica.im | 2026-04 B 轮 $75M；估值 ~$500M（浏览器侧栏聚合） | LibreChat / LobeChat + Ollama | ✅ [monica](reports/01-model/aggregator/monica.md) |

> 其余聚合客户端（MultiChats / Overchat / TypingMind / Aymo / 1i / Cortex 开源）融资多未披露或很小，未达门槛，作平替侧参照。

### 4. Agent 记忆 / Memory 层
> 赛道尚早，未见任何一家披露 ARR>$50M；仅少数跨过融资门槛。
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Mem0 | Mem0 | mem0.ai | 融资 $24M（最接近 pure-play） | **Mem0 开源（Apache2.0，双形态）/ Letta / Cognee** | ✅ [mem0](reports/01-model/memory/mem0.md) |
| Engram | Engram | engram.com | 融资 $98M；估值 ~$600M[u] | Letta / Graphiti | ✅ [engram](reports/01-model/memory/engram.md) |
| Pieces / Dust / SurrealDB | 各 | — | 边界（融资达标但 memory 为子能力） | Mem0 / Redis Agent Memory Server | ✅ [mem0](reports/01-model/memory/mem0.md) |

### 5. 微调服务
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| HF AutoTrain / 商业微调服务 | Hugging Face 等 | huggingface.co | 见母体 | LLaMA Factory（注：**本地效果差点意思**） | ✅ [hf-autotrain](reports/01-model/finetune/hf-autotrain.md) |

### 6. Agent 可观测 / 评估
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| LangChain / LangSmith | LangChain | langchain.com | 估值 $1.25B；融资 $260M | Langfuse（+ n8n/Dify/Flowise 编排） | ✅ [langchain](reports/01-model/observability/langchain.md) |
| Braintrust | Braintrust | braintrust.dev | 估值 $800M；融资 $80M | Langfuse | ✅ [braintrust](reports/01-model/observability/braintrust.md) |
| Arize AI | Arize | arize.com | 估值 ~$742M；融资 $131M | Langfuse | ✅ [arize](reports/01-model/observability/arize.md) |
| Weights & Biases | CoreWeave | wandb.ai | 估值 $1.1B；融资 $325M | Langfuse / TensorZero | ✅ [wandb](reports/01-model/observability/wandb.md) |

> 推理 API / 模型托管、GPU/算力云、模型平台（HF/Databricks）、数据标注、AI 芯片 → 见 [附录](/Users/pengpeng/seo/directions/commerce/products-appendix.md)。

---

## 二、AI 创作层

### 7. AI 图像
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Midjourney | Midjourney | midjourney.com | ARR ~$500M；估值 ~$10B | ComfyUI + FLUX.2 | ✅ [midjourney](reports/02-creation/image/midjourney.md) |
| Leonardo AI | Canva | leonardo.ai | ARR ~$95M；融资 $31M | ComfyUI + FLUX.2 / HiDream | ✅ [leonardo-ai](reports/02-creation/image/leonardo-ai.md) |
| Adobe Firefly | Adobe | adobe.com | Firefly ARR ~$300M | ComfyUI + Qwen Image Edit | ✅ [adobe-firefly](reports/02-creation/image/adobe-firefly.md) |
| GPT Image / DALL·E | OpenAI | openai.com | 大厂旗舰 | ComfyUI + FLUX.2 | ✅ [gpt-image](reports/02-creation/image/gpt-image.md) |
| Ideogram | Ideogram | ideogram.ai | 融资 $75.8–96M | **开源权重直接跑（Ideogram 权重 + ComfyUI）+ 商业版对标** | ✅ [ideogram](reports/02-creation/image/ideogram.md) |
| Krea | Krea AI | krea.ai | 估值 $500M；融资 $83M | **开源权重（Krea 2）+ ComfyUI + 商业版对标**（另见 #11 设计 Agent） | ✅ [krea](reports/02-creation/image/krea.md) |
| Magnific（原 Freepik） | Freepik | magnific.com | ARR $200–230M | ComfyUI（放大/重绘） | ✅ [magnific](reports/02-creation/image/magnific.md) |
| Recraft | Recraft | recraft.ai | 融资 ~$42M | ComfyUI（另见 #11 设计 Agent） | ✅ [recraft](reports/02-creation/image/recraft.md) |
| Black Forest Labs (FLUX API) | BFL | bfl.ai | 估值 $3.25B；融资 ~$450M | **开源权重（FLUX.2）+ ComfyUI + 商业 API 对标** | ✅ [black-forest-labs](reports/02-creation/image/black-forest-labs.md) |
| Google Gemini Image (Nano Banana) | Alphabet | gemini.google.com | 大厂旗舰 | ComfyUI + Qwen Image Edit | ✅ [gemini-image](reports/02-creation/image/gemini-image.md) |

### 8. AI 视频生成
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Runway | Runway | runwayml.com | ARR ~$300M；估值 $5.3B | Wan / HunyuanVideo | ✅ [runway](reports/02-creation/video/runway.md) |
| Pika | Pika Labs | pika.art | 估值 $700M；融资 $135M | Wan | ✅ [pika](reports/02-creation/video/pika.md) |
| Luma AI | Luma AI | lumalabs.ai | 估值 $4B；融资 ~$1.07B | Wan + TRELLIS | ✅ [luma-ai](reports/02-creation/video/luma-ai.md) |
| Sora | OpenAI | sora.com（已关停 2026-04-26） | 大厂旗舰 | Wan / HunyuanVideo | ✅ [sora](reports/02-creation/video/sora.md) |
| Kling | 快手 | klingai.com | ARR ~$500M；估值 ~$18B | Wan | ✅ [kling](reports/02-creation/video/kling.md) |
| Vidu | 生数科技 | vidu.studio | 融资 ~$293M | Wan | ✅ [vidu](reports/02-creation/video/vidu.md) |
| Higgsfield | Higgsfield | higgsfield.ai | ARR ~$200M；估值 $1.3B | Wan | ✅ [higgsfield](reports/02-creation/video/higgsfield.md) |
| Google Veo / Flow | Alphabet | — | 大厂旗舰 | Wan / HunyuanVideo | ✅ [google-veo](reports/02-creation/video/google-veo.md) |

### 9. AI 数字人 / 分身
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| HeyGen | HeyGen | heygen.com | ARR $200M；融资 ~$74M | HeyGem + 本地 TTS | ✅ [heygen](reports/02-creation/avatar/heygen.md) |
| Synthesia | Synthesia | synthesia.io | ARR $150M+；估值 $4B | HeyGem + 本地 TTS | ✅ [synthesia](reports/02-creation/avatar/synthesia.md) |
| D-ID | D-ID | d-id.com | 融资 ~$48M | EchoMimic + 本地 TTS | ✅ [d-id](reports/02-creation/avatar/d-id.md) |
| Captions | Captions | captions.ai | 估值 $500M；融资 $100M | HeyGem | ✅ [captions](reports/02-creation/avatar/captions.md) |
| Hedra | Hedra | hedra.com | 融资 >$30M[u] | EchoMimic / HeyGem | ✅ [hedra](reports/02-creation/avatar/hedra.md) |

### 10. AI 3D
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Meshy | Meshy AI | meshy.ai | 融资 ~$52M；ARR ~$30M | Hunyuan3D / TRELLIS | ✅ [meshy](reports/02-creation/3d/meshy.md) |
| Tripo3D | Tripo AI | tripo3d.ai | 估值 ~$1.5B；融资 ~$250M | TripoSR / Hunyuan3D | ✅ [tripo3d](reports/02-creation/3d/tripo3d.md) |

### 11. AI 设计 Agent
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Claude Design | Anthropic | claude.com/product/design | 大厂旗舰（Opus 4.7 驱动，首周 100 万+ 用户） | **Open Design**（开源 Claude Design 平替，Apache2.0）+ Jaaz | ✅ [claude-design](reports/02-creation/design-agent/claude-design.md) |
| Lovart | Resonate Intl. | lovart.ai | ARR $30M；融资 Caplight $137.5M vs bootstrapped[u] | **Jaaz**（local alt for Lovart）+ ComfyUI | ✅ [lovart](reports/02-creation/design-agent/lovart.md) |
| Gamma | Gamma | gamma.app | ARR $100M；估值 $2.1B | 无直接平替（+ 演示生成） | ✅ [gamma](reports/02-creation/design-agent/gamma.md) |
| Magnific（另见 #7） | Magnific | magnific.com | ARR $230M | ComfyUI | ✅ [magnific](reports/02-creation/image/magnific.md) |
| FLORA | Flora | flora.ai | 融资 $52M | ComfyUI（节点式） | ✅ [flora](reports/02-creation/design-agent/flora.md) |
| Figma Design Agent + Make | Figma | figma.com | 收入 $1.42B；市值 ~$10B | Penpot（设计侧）/ Open Design（agent 侧） | ✅ [figma](reports/02-creation/design-agent/figma.md) |
| Canva (Magic Studio) | Canva | canva.com | ARR $4B；估值 $42B | 无直接平替 | ✅ [canva](reports/02-creation/design-agent/canva.md) |
| Adobe Creative Agent | Adobe | adobe.com | Firefly ARR ~$300M | ComfyUI + Penpot | ✅ [adobe](reports/02-creation/design-agent/adobe.md) |
| Google Stitch | Google | stitch.withgoogle.com | 大厂旗舰 | Penpot / ComfyUI | ✅ [google-stitch](reports/02-creation/design-agent/google-stitch.md) |

> Lovart 融资口径冲突（Caplight $137.5M vs 多源 bootstrapped），未官方交叉证实，标 `[u]`。

### 12. AI 音乐
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Suno | Suno AI | suno.com | ARR $300M；估值 $5.4B | ACE-Step | ✅ [suno](reports/02-creation/music/suno.md) |
| Udio | Udio | udio.com | 融资 ~$10M（未达标，现有报告降级观察） | ACE-Step | ✅ [udio](reports/02-creation/music/udio.md) |

### 13. 博客 / 播客 & 音频内容生成
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Google NotebookLM | Google | notebooklm.google | 大厂旗舰 | Open Notebook | ✅ [notebooklm](reports/02-creation/audio-content/notebooklm.md) |

### 14. AI 语音 · TTS / 语音生成 / 克隆
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| ElevenLabs | ElevenLabs | elevenlabs.io | ARR >$500M；估值 $11B | Kokoro / Fish Speech / CosyVoice | ✅ [elevenlabs](reports/02-creation/voice-tts/elevenlabs.md) |
| Cartesia | Cartesia | cartesia.ai | 融资 ~$191M | Fish Speech | ✅ [cartesia](reports/02-creation/voice-tts/cartesia.md) |
| Hume AI | Hume AI | hume.ai | 融资 $74M;估值 $219M | CosyVoice | ✅ [hume](reports/02-creation/voice-tts/hume.md) |
| Deepgram | Deepgram | deepgram.com | 估值 $1.3B；融资 $215M+ | Whisper + Kokoro | ✅ [deepgram](reports/02-creation/voice-tts/deepgram.md) |
| AssemblyAI | AssemblyAI | assemblyai.com | 估值 $300M；融资 $158M | Whisper | ✅ [assemblyai](reports/02-creation/voice-tts/assemblyai.md) |
| Speechmatics | Speechmatics | speechmatics.com | 融资 $90.6M | Whisper | ✅ [speechmatics](reports/02-creation/voice-tts/speechmatics.md) |
| Play.HT | Meta | play.ht | 被 Meta 收购（见附录） | Fish Speech | ✅ [playht](reports/02-creation/voice-tts/playht.md) |

### 15. AI 语音 · 会议转录 / 会议助手
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Otter.ai | Otter AI | otter.ai | ARR >$100M；融资 $70M | Whisper + Open Notebook | ✅ [otter-ai](reports/02-creation/voice-meeting/otter-ai.md) |
| Fireflies.ai | Fireflies | fireflies.ai | 估值 >$1B | Whisper + Open Notebook | ✅ [fireflies](reports/02-creation/voice-meeting/fireflies.md) |
| Granola | Granola | granola.ai | 估值 $1.5B；融资 $192M | Open Notebook + Whisper | ✅ [granola](reports/02-creation/voice-meeting/granola.md) |
| Gong | Gong | gong.io | ARR >$500M；估值 ~$7.2B | 无直接平替 | ✅ [gong](reports/02-creation/voice-meeting/gong.md) |
| Read AI | Read AI | read.ai | 估值 $450M；融资 $81M | 无直接平替 | ✅ [read-ai](reports/02-creation/voice-meeting/read-ai.md) |

### 16. AI 语音 · 语音输入法 / 听写
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Wispr Flow | Wispr | wisprflow.ai | 融资 $81M；估值 $700M | Whisper + Speaches | ✅ [wispr-flow](reports/02-creation/voice-dictation/wispr-flow.md) |
| Typeless | Typeless（Huang Song） | typeless.com | 融资未披露[u]（Stanford StartX；Wispr Flow 对标） | Whisper + Speaches | ✅ [wispr-flow](reports/02-creation/voice-dictation/wispr-flow.md) |
| Apple Dictation / Gboard Rambler / Windows Speech | Apple / Google / MS | — | 大厂旗舰 | Whisper + Speaches | ✅ [native-dictation](reports/02-creation/voice-dictation/native-dictation.md) |

> 独立 VC 赛道几乎被 Wispr Flow 一家垄断；Typeless 融资未公开（勿与同名 YC 消息 API 公司 $26M 混淆）；Aqua / Superwhisper 等未达门槛（见附录）。

### 17. AI 语音 · 语音 Agent / Voicebot
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Vapi | Vapi | vapi.ai | 估值 ~$500M；融资 $72M | 无直接平替（可自建 Whisper+Kokoro+Dify） | ✅ [vapi](reports/02-creation/voice-agent/vapi.md) |
| PolyAI | PolyAI | poly.ai | 估值 $750M；融资 $204M | 无直接平替 | ✅ [polyai](reports/02-creation/voice-agent/polyai.md) |
| Bland AI | Bland | bland.ai | 融资 >$100M | 无直接平替 | ✅ [bland](reports/02-creation/voice-agent/bland.md) |
| Parloa | Parloa | parloa.com | 估值 $3B；融资 >$560M | 无直接平替 | ✅ [parloa](reports/02-creation/voice-agent/parloa.md) |
| Observe.AI | Observe.AI | observe.ai | 融资 $214M | 无直接平替 | ✅ [observe-ai](reports/02-creation/voice-agent/observe-ai.md) |
| Uniphore | Uniphore | uniphore.com | 估值 $2.5B；融资 $260M | 无直接平替 | ✅ [uniphore](reports/02-creation/voice-agent/uniphore.md) |
| SoundHound AI | SoundHound | soundhound.com | FY2025 收入 $169M（上市） | CosyVoice / Whisper | ✅ [soundhound](reports/02-creation/voice-tts/soundhound.md) |

### 18. AI 翻译
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| DeepL | DeepL | deepl.com | ARR ~$285M；估值 $2B | Hy-MT2 / NLLB-200（MTranServer） | ✅ [deepl](reports/02-creation/translation/deepl.md) |
| Google Translate | Google | translate.google.com | 大厂旗舰 | NLLB-200 / Hy-MT2 | ✅ [google-translate](reports/02-creation/translation/google-translate.md) |
| Microsoft Translator | Microsoft | microsoft.com | 大厂旗舰 | MTranServer / NLLB-200 | ✅ [microsoft-translator](reports/02-creation/translation/microsoft-translator.md) |

### 19. AI OCR / 文档理解
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Adobe Acrobat AI | Adobe | adobe.com | 市值 ~$88B | DeepSeek OCR / PaddleOCR | ✅ [deepseek](reports/01-model/frontier-labs/deepseek.md) |
| AWS Textract | Amazon | aws.amazon.com | 大厂旗舰 | DeepSeek OCR / Unlimited OCR | ✅ [deepseek](reports/01-model/frontier-labs/deepseek.md) |
| Google Document AI | Google | cloud.google.com | 大厂旗舰 | Qwen2.5-VL + PDFMathTranslate | ✅ [google-document-ai](reports/02-creation/ocr/google-document-ai.md) |
| Mistral OCR | Mistral | mistral.ai | 见 Mistral | PaddleOCR / DeepSeek OCR | ✅ [mistral](reports/01-model/frontier-labs/mistral.md) |

---

## 三、AI 应用层

### 20. AI 代码编辑器 / IDE
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Cursor | Anysphere | cursor.com | ARR ~$4B；收购 $60B[u] | Continue.dev + Ollama | ✅ [cursor](reports/03-application/ide/cursor.md) |
| Windsurf | Cognition | windsurf.com | ARR $82M（并入 Cognition） | Continue.dev + Ollama | ✅ [windsurf](reports/03-application/ide/windsurf.md) |
| GitHub Copilot（IDE） | Microsoft | github.com/features/copilot | 大厂旗舰；470万付费订阅 | Continue.dev | ✅ |
| Replit | Replit | replit.com | ARR ~$265M；估值 $9B | Coder + OpenCode | ✅ [replit](reports/03-application/ide/replit.md) |
| Augment Code | Augment | augmentcode.com | 估值 $977M；融资 $252M | Continue.dev | ✅ [augment](reports/03-application/ide/augment.md) |
| Tabnine | Tabnine | tabnine.com | 融资 ~$56M（**降级观察**） | Continue.dev + Ollama | ✅ [tabnine](reports/03-application/ide/tabnine.md) |

> 传统编辑器 Zed / JetBrains 非 AI-native，不列；Poolside / Magic（模型 infra 向）见附录。

### 21. AI 编码 Agent / 终端 CLI
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Claude Code | Anthropic | claude.com | ARR run-rate >$2.5B；大厂旗舰 | **Claude Code（Market，接本地模型）** / OpenCode | ✅ [claude-code](reports/03-application/coding-agent/claude-code.md) |
| OpenAI Codex / Codex CLI | OpenAI | openai.com | 大厂旗舰；CLI 开源 | OpenCode / Aider | ✅ [openai-codex](reports/03-application/coding-agent/openai-codex.md) |
| Cursor CLI | Anysphere | cursor.com | 母公司 ARR ~$4B | OpenCode + Ollama | ✅（合并 Cursor） |
| GitHub Copilot CLI + Coding Agent | Microsoft | github.com | 大厂旗舰 | OpenCode / Aider | ✅ [github-copilot](reports/03-application/coding-agent/github-copilot.md) |
| Gemini CLI → Antigravity CLI | Google | — | 大厂旗舰（开源） | Qwen Code / Gemini CLI（**开源，接 Ollama**） | ✅ [gemini-cli](reports/03-application/coding-agent/gemini-cli.md) |
| Google Jules | Google | jules.google | 大厂旗舰 | OpenHands | ✅ [google-jules](reports/03-application/coding-agent/google-jules.md) |
| Devin | Cognition | cognition.ai | ARR $492M；估值 $26B；融资 >$2.5B | OpenHands | ✅ [devin](reports/03-application/coding-agent/devin.md) |
| Factory Droids | Factory.ai | factory.ai | 估值 $1.5B；融资 $150M+ | OpenHands | ✅ [factory](reports/03-application/coding-agent/factory.md) |
| Amp | Amp（Sourcegraph 分拆） | ampcode.com | 母公司融资 $223M；估值 $2.6B | OpenCode / Aider | ✅ [amp](reports/03-application/coding-agent/amp.md) |
| Warp | Warp | warp.dev | ARR $42M；融资 $73M | OpenCode | ✅ [warp](reports/03-application/ide/warp.md) |
| Cline | Cline Bot | cline.bot | 融资 $32M；估值 $110M | **Cline（开源核心，双形态）** | ✅ [cline](reports/03-application/coding-agent/cline.md) |
| OpenHands | All Hands AI | openhands.dev | 融资 $23.8M | **OpenHands（核心 MIT，双形态）** | ✅ [openhands](reports/03-application/coding-agent/openhands.md) |
| Qodo | Qodo | qodo.ai | 融资 $120M | 无直接平替 | ✅ [qodo](reports/03-application/coding-agent/qodo.md) |

> Codex 已从纯编码工具演进为 ChatGPT 内通用 agent harness（含 Computer Use、云 + 本地执行）；此处按编码主场景收录，通用能力不另立行。
> 未达门槛开源 CLI（Aider / Goose / Continue.dev）作平替侧参照，不列竞品行。

### 22. AI 应用 / 网站生成（vibe coding）
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Lovable | Lovable | lovable.dev | ARR $500M；估值 >$6B | bolt.diy / Appsmith | ✅ [lovable](reports/03-application/vibe-coding/lovable.md) |
| Bolt.new | StackBlitz | bolt.new | 估值 $700M；融资 $135M | bolt.diy | ✅ [bolt](reports/03-application/vibe-coding/bolt.md) |
| v0 | Vercel | v0.dev | Vercel 估值 $9.3B | Appsmith / Jaaz | ✅ [v0](reports/03-application/vibe-coding/v0.md) |

### 23. 建站 / 无代码 App
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Wix | Wix | wix.com | 市值 ~$8B；ARR >$1.8B | WordPress / Ghost | ✅ [wix](reports/03-application/website-builder/wix.md) |
| Base44 | Wix | base44.com | ARR $100–150M | Appsmith / NocoBase | ✅ [wix](reports/03-application/website-builder/wix.md) |
| Squarespace | Squarespace | squarespace.com | 收入 ~$1.2B（私有化） | WordPress / Ghost | ✅ [squarespace](reports/03-application/website-builder/squarespace.md) |
| Webflow | Webflow | webflow.com | ARR ~$200M；估值 $4B | Webstudio（开源） | ✅ [webflow](reports/03-application/website-builder/webflow.md) |
| Framer | Framer | framer.com | ARR ~$100M；融资 $60M | Webstudio | ✅ [framer](reports/03-application/website-builder/framer.md) |
| Bubble | Bubble | bubble.io | ARR ~$100M；融资 $100M | NocoBase / Budibase | ✅ [bubble](reports/03-application/low-code/bubble.md) |
| Glide | Glide | glideapps.com | 融资 $70M | Budibase / NocoBase | ✅ [glide](reports/03-application/low-code/glide.md) |

### 24. 内部工具 / 低代码平台
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Retool | Retool | retool.com | ARR ~$150M+；估值 $3.2B | **Appsmith（开源，双形态）** / ToolJet | ✅ [retool](reports/03-application/low-code/retool.md) |
| OutSystems | OutSystems | outsystems.com | ARR >$400M；估值 $9.5B | Budibase / NocoBase | ✅ [outsystems](reports/03-application/low-code/outsystems.md) |
| Mendix | Siemens | mendix.com | 被 Siemens 收购 $730M | Budibase | ✅ [mendix](reports/03-application/low-code/mendix.md) |
| Microsoft Power Apps | Microsoft | powerapps.microsoft.com | 大厂旗舰 | Appsmith / NocoBase | ✅ [power-apps](reports/03-application/low-code/power-apps.md) |
| Superblocks | Superblocks | superblocks.com | 融资 $60M | Appsmith / ToolJet | ✅ [superblocks](reports/03-application/low-code/superblocks.md) |

### 25. BaaS / 后端即服务
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Supabase | Supabase | supabase.com | ARR ~$100M；估值 $5B；融资 $400M+ | **Supabase（开源自托管，双形态）** | ✅ [supabase](reports/03-application/baas/supabase.md) |
| Firebase | Google | firebase.google.com | 大厂旗舰 | Supabase / Appwrite | ✅ [firebase](reports/03-application/baas/firebase.md) |
| Appwrite | Appwrite | appwrite.io | 融资 $37M | **Appwrite（开源自托管，双形态）** | ✅ [appwrite](reports/03-application/baas/appwrite.md) |

### 26. AI 自动化 / 工作流
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Zapier | Zapier | zapier.com | ARR $420M；估值 $5B | n8n | ✅ [zapier](reports/03-application/automation/zapier.md) |
| n8n（云版） | n8n | n8n.io | ARR >€100M；估值 $5.2B | **n8n（自托管，双形态）** | ✅ [n8n-cloud](reports/03-application/automation/n8n-cloud.md) |
| Make | Make | make.com | ARR ~$52.6M | n8n | ✅ [make](reports/03-application/automation/make.md) |
| Lindy | Lindy | lindy.ai | 融资 ~$50M | n8n | ✅ [lindy](reports/03-application/automation/lindy.md) |
| Gumloop | Gumloop | gumloop.com | 估值 $333M；融资 $70M | n8n | ✅ [gumloop](reports/03-application/automation/gumloop.md) |
| Microsoft Copilot Studio | Microsoft | microsoft.com | 大厂旗舰 | Dify | ✅ [copilot-studio](reports/03-application/automation/copilot-studio.md) |
| Google Vertex AI Agent Builder | Google | cloud.google.com | 大厂旗舰 | Dify / n8n | ✅ [vertex-ai-agent](reports/03-application/automation/vertex-ai-agent.md) |
| 字节 Coze | ByteDance | coze.com | 大厂旗舰 | Dify / Flowise | ✅ [coze](reports/03-application/automation/coze.md) |
| Temporal | Temporal | temporal.io | 估值 $2.8B；融资 $285M | 无直接平替（编排基建） | ✅ [temporal](reports/03-application/automation/temporal.md) |

### 27. 通用 Agent / Deep Research Agent
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Manus | Butterfly Effect | manus.im | ARR $400–500M；收购价 ~$2B[u] | **DeerFlow 2.0** / Hermes Agent | ✅ [manus](reports/03-application/general-agent/manus.md) |
| Genspark | Genspark | genspark.ai | ARR $250M+；估值 $2.6B | DeerFlow 2.0 | ✅ [genspark](reports/03-application/personal-ai/genspark.md) |
| Perplexity Computer | Perplexity | perplexity.ai | ARR $450M+；估值 ~$22B | DeerFlow 2.0 + SearXNG | ✅ [perplexity-computer](reports/03-application/general-agent/perplexity-computer.md) |
| Kimi Work / Researcher | Moonshot | kimi.com | ARR >$200M；估值 $20B | DeerFlow 2.0 | ✅ [kimi-researcher](reports/03-application/general-agent/kimi-researcher.md) |
| ChatGPT Agent / OpenAI Deep Research | OpenAI | chatgpt.com | 大厂旗舰 | DeerFlow 2.0 | ✅ [chatgpt-agent](reports/03-application/general-agent/chatgpt-agent.md) |
| Gemini Deep Research | Google | gemini.google.com | 大厂旗舰 | DeerFlow 2.0 | ✅ [gemini-deep-research](reports/03-application/general-agent/gemini-deep-research.md) |
| Claude Cowork | Anthropic | claude.com | 大厂旗舰 | Hermes Agent | ✅ [claude-cowork](reports/03-application/general-agent/claude-cowork.md) |
| Copilot Researcher | Microsoft | microsoft.com | 大厂旗舰 | DeerFlow 2.0 | ✅ [copilot-researcher](reports/03-application/general-agent/copilot-researcher.md) |
| Amazon Nova Act | AWS | aws.amazon.com/nova/act | 大厂旗舰 | DeerFlow 2.0 | ✅ [amazon-nova-act](reports/03-application/general-agent/amazon-nova-act.md) |
| ARI | You.com | you.com | 估值 $1.5B；融资 $195M | DeerFlow 2.0 + SearXNG | ✅ [ari](reports/03-application/general-agent/ari.md) |
| Skywork | 昆仑万维 | skywork.ai | 实体估值 ¥149B(~$20B+) | DeerFlow 2.0 | ✅ [skywork](reports/03-application/general-agent/skywork.md) |
| Runner H | H Company | hcompany.ai | 融资 $220M seed | DeerFlow 2.0 | ✅ [runner-h](reports/03-application/general-agent/runner-h.md) |
| Parallel Web Systems | Parallel | parallel.ai | 估值 $2B；融资 $230M | SearXNG + Firecrawl | ✅ [parallel](reports/03-application/general-agent/parallel.md) |

### 28. 个人 AI 助手 / Personal AI
| 商业产品 | 公司 | 域名 | 达标依据 | 对标 OpenClaw | Olares 平替 | 报告 |
|------|------|------|---------|------|------------|------|
| Genspark Claw | Mainfunc | genspark.ai | ARR $250M；估值 $2.6B；融资 $460–645M[u] | 强（最强商业版，每用户专属云电脑 + Workspace） | **OpenClaw + NemoClaw**（自托管） | ✅ [genspark-claw](reports/03-application/personal-ai/genspark-claw.md) |
| Kimi Claw | Moonshot | kimi.com/bot | 大厂旗舰；母体估值 $20B | 托管 wrapper（浏览器一键 + ClawHub） | OpenClaw / QwenPaw | ✅ [kimi-claw](reports/03-application/personal-ai/kimi-claw.md) |
| MaxClaw | MiniMax | agent.minimax.io | 大厂旗舰（上市） | 托管 wrapper（锁 M2.5） | OpenClaw | ✅ [minimax](reports/01-model/frontier-labs/minimax.md) |
| ArkClaw | 字节/火山引擎 | volcengine.com | 大厂旗舰 | 企业托管 wrapper（深绑飞书） | OpenClaw / QwenPaw | ✅ [arkclaw](reports/03-application/personal-ai/arkclaw.md) |
| Poke | Interaction Co. | poke.com | 估值 $300M；累计 $25M | 强（"OpenClaw for normies"，纯短信） | OpenClaw / Hermes Agent | ✅ [poke](reports/03-application/personal-ai/poke.md) |
| Vellum Personal Intelligence | Vellum | vellum.ai | 融资 $25M（PI 轮） | 强（官方列 OpenClaw 为竞品） | OpenClaw | ✅ [vellum](reports/03-application/personal-ai/vellum.md) |
| Town / Townie | Town | town.com | 融资 $55M（a16z） | 部分（邮件/CC 委派） | OpenClaw | ✅ [town](reports/03-application/personal-ai/town.md) |
| Manus Agents | Manus（Meta 收购中） | manus.im | Meta 收购 >$2B；ARR $400–500M[u] | 边界（内核通用 agent） | OpenClaw / Hermes Agent | ✅ [manus-agents](reports/03-application/personal-ai/manus-agents.md) |

### 29. 客服 Agent
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Sierra | Sierra | sierra.ai | ARR ~$150M；估值 ~$15B | 无直接平替（可自建 Dify/Flowise+Chatwoot） | ✅ [sierra](reports/03-application/cx-agent/sierra.md) |
| Decagon | Decagon | decagon.ai | 估值 $4.5B；融资 ~$481M | 无直接平替 | ✅ [decagon](reports/03-application/cx-agent/decagon.md) |
| Salesforce Agentforce | Salesforce | salesforce.com | ARR $800M–1.2B | Dify / Flowise | ✅ [salesforce-agentforce](reports/03-application/cx-agent/salesforce-agentforce.md) |
| Intercom Fin | Intercom | intercom.com | 母公司 ARR >$300M[u] | Chatwoot + Dify | ✅ [intercom-fin](reports/03-application/cx-agent/intercom-fin.md) |

### 30. AI 搜索 / 研究
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Perplexity | Perplexity AI | perplexity.ai | ARR $450–500M；估值 $22.6B | Perplexica(Vane) + SearXNG | ✅ [perplexity](reports/03-application/search/perplexity.md) |
| You.com | You.com | you.com | ARR $50M；估值 $1.5B | Perplexica + SearXNG | ✅ [you-com](reports/03-application/search/you-com.md) |
| Exa | Exa | exa.ai | 估值 $700M；融资 $107M | SearXNG + Firecrawl | ✅ [exa](reports/03-application/search/exa.md) |
| Consensus | Consensus | consensus.app | 融资 $45.75M | Open Notebook | ✅ [consensus](reports/03-application/search/consensus.md) |

### 31. AI 写作 / 营销文案
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Grammarly | Grammarly | grammarly.com | ARR $700M；估值 $13B | 无直接平替（+ Open WebUI 校对） | ✅ [grammarly](reports/03-application/writing/grammarly.md) |
| Writer | Writer | writer.com | 估值 $1.9B；融资 $326M | Dify（企业写作） | ✅ [writer](reports/03-application/writing/writer.md) |
| Jasper | Jasper | jasper.ai | 估值 $1.5B；融资 $131M | Open WebUI + Ollama | ✅ [jasper](reports/03-application/writing/jasper.md) |

### 32. AI 陪伴 / 角色
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Character.AI | Character Technologies | character.ai | 估值 $1B；融资 $193M | SillyTavern / KoboldCpp | ✅ [character-ai](reports/03-application/companion/character-ai.md) |
| Chai | Chai Research | chai-research.com | ARR $80M；估值 $2.4B[u] | SillyTavern | ✅ [chai](reports/03-application/companion/chai.md) |
| Talkie | MiniMax | talkie-ai.com | 母公司估值 ~$32B | SillyTavern | ✅ [minimax](reports/01-model/frontier-labs/minimax.md) |

### 33. 垂直知识 Agent · 法律
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Harvey | Harvey | harvey.ai | ARR $190–300M；估值 $11B | RAGFlow + Ollama（自建） | ✅ [harvey](reports/03-application/vertical-legal/harvey.md) |
| Legora | Legora | legora.com | ARR >$100M；估值 $5.6B | RAGFlow + Ollama | ✅ [legora](reports/03-application/vertical-legal/legora.md) |
| EvenUp | EvenUp | evenuplaw.com | 估值 >$2B；融资 $385M | 无直接平替 | ✅ [evenup](reports/03-application/vertical-legal/evenup.md) |

### 34. 垂直知识 Agent · 医疗
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Abridge | Abridge | abridge.com | ARR $117M；估值 $5.3B | 无直接平替 | ✅ [abridge](reports/03-application/vertical-medical/abridge.md) |
| OpenEvidence | OpenEvidence | openevidence.com | ARR >$100M；估值 $12B | 无直接平替 | ✅ [openevidence](reports/03-application/vertical-medical/openevidence.md) |

### 35. 垂直知识 Agent · 金融
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Rogo | Rogo | rogo.ai | 估值 $2B；融资 >$300M | 无直接平替 | ✅ [rogo](reports/03-application/vertical-finance/rogo.md) |

### 36. 企业知识 / RAG / 企业搜索
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Glean | Glean | glean.com | ARR $300M；估值 $7.2B | AnythingLLM / RAGFlow + SearXNG | ✅ [glean](reports/03-application/enterprise-rag/glean.md) |
| Guru | Guru | getguru.com | 融资 $68–82M | AnythingLLM / RAGFlow | ✅ [guru](reports/03-application/enterprise-rag/guru.md) |
| Hebbia | Hebbia | hebbia.ai | 估值 $700M；融资 $161M | RAGFlow / FastGPT | ✅ [hebbia](reports/03-application/enterprise-rag/hebbia.md) |
| Dust | Dust | dust.tt | 融资 >$60M | Dify / RAGFlow | ✅ [dust](reports/03-application/enterprise-rag/dust.md) |

---

## 四、生产力 & 协作 SaaS

### 37. AI 笔记 / 个人知识
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Notion | Notion | notion.so | ARR $600M；估值 $11B | AFFiNE / AppFlowy | ✅ [notion](reports/04-productivity/notes/notion.md) |
| Granola | Granola | granola.ai | 估值 $1.5B（另见 #15） | Open Notebook | ✅ [granola](reports/02-creation/voice-meeting/granola.md) |

> Obsidian / Logseq 本身可本地部署，作平替侧备注（AppFlowy + Olares Drive 场景可提及）。

### 38. 办公套件 / 文档协作
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Microsoft 365 | Microsoft | microsoft.com | 大厂旗舰 | OnlyOffice / Nextcloud（**弱平替**） | ✅ [microsoft-365](reports/04-productivity/office-suite/microsoft-365.md) |
| Google Workspace | Google | workspace.google.com | 大厂旗舰 | OnlyOffice / Nextcloud（**弱平替**） | ✅ [google-workspace](reports/04-productivity/office-suite/google-workspace.md) |

### 39. 团队沟通 / IM
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Slack | Salesforce | slack.com | 收入 ~$3B | Mattermost / Rocket.Chat | ✅ [slack](reports/04-productivity/im/slack.md) |
| Mattermost 企业版 | Mattermost | mattermost.com | 达标 | **Mattermost（开源自托管，双形态）** | ✅ [mattermost](reports/04-productivity/im/mattermost.md) |
| Element / Matrix | Element | element.io | 达标（加密通信） | Element + Synapse | ✅ [element](reports/04-productivity/im/element.md) |

### 40. 电子邮件 / Email
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Gmail | Google | mail.google.com | 大厂旗舰 | **Olares Mail（内置）** / Stalwart / Mailcow（自托管投递率需配置 SMTP 中继） | ✅ [gmail](reports/04-productivity/email/gmail.md) |
| Outlook | Microsoft | outlook.com | 大厂旗舰 | Olares Mail / Mailcow | ✅ [outlook](reports/04-productivity/email/outlook.md) |
| Proton Mail | Proton AG | proton.me/mail | 估值 >$1B（隐私邮件，另见 #57） | Olares Mail / Stalwart（自托管加密邮件，投递率需中继） | ✅ [proton](reports/05-storage-privacy/privacy-vpn/proton.md) |
| Front | Front | front.com | ARR $100M；估值 $1.7B；融资 $204M | 无直接平替（团队协作邮箱） | ✅ [front](reports/04-productivity/email/front.md) |
| Superhuman | Grammarly（已收购） | superhuman.com | 收购前估值 $825M（见附录·已被收购） | Olares Mail + 本地 AI 校对 | ✅ [grammarly](reports/03-application/writing/grammarly.md) |
| Zoho Mail | Zoho | zoho.com/mail | 母体收入 >$1.9B（成熟 SaaS） | Olares Mail / Mailcow | ✅ [zoho-mail](reports/04-productivity/email/zoho-mail.md) |

### 41. 项目管理
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Atlassian (Jira/Confluence/Trello) | Atlassian | atlassian.com | 市值 $21.1B | Plane / Docmost | ✅ [atlassian](reports/04-productivity/project-management/atlassian.md) |
| Asana | Asana | asana.com | 收入 ~$791M | Plane / Leantime | ✅ [asana](reports/04-productivity/project-management/asana.md) |
| monday.com | monday.com | monday.com | 收入 ~$1.47B | Plane | ✅ [monday](reports/04-productivity/project-management/monday.md) |
| ClickUp | ClickUp | clickup.com | ARR $300M；估值 $4B | Plane / Leantime | ✅ [clickup](reports/04-productivity/project-management/clickup.md) |
| Miro | Miro | miro.com | ARR $630–665M；估值 $17.5B | Excalidraw | ✅ [miro](reports/04-productivity/notes/miro.md) |

### 42. 无代码数据库
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Airtable | Airtable | airtable.com | ARR $478M；估值 $11.7B | NocoDB / Teable / SeaTable | ✅ [airtable](reports/04-productivity/nocode-db/airtable.md) |

### 43. CRM / 客户管理
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Salesforce | Salesforce | salesforce.com | 市值 ~$380B | Twenty / SuiteCRM | ✅ [salesforce](reports/04-productivity/crm/salesforce.md) |
| HubSpot | HubSpot | hubspot.com | 市值 >$30B | Twenty / EspoCRM（营销侧 Mautic+Listmonk） | ✅ [hubspot](reports/04-productivity/crm/hubspot.md) |

### 44. 电商平台
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Shopify | Shopify | shopify.com | 市值 >$150B | Medusa / Saleor | ✅ [shopify](reports/04-productivity/ecommerce/shopify.md) |

### 45. 客服工单
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Zendesk | Zendesk | zendesk.com | ARR >$2B | Chatwoot / Zammad / FreeScout | ✅ [zendesk](reports/04-productivity/helpdesk/zendesk.md) |

### 46. 财务 / 记账
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Intuit QuickBooks | Intuit | quickbooks.intuit.com | 市值 >$180B | ERPNext / Akaunting（个人 Firefly III） | ✅ [quickbooks](reports/04-productivity/finance/quickbooks.md) |

### 47. 身份 / IAM
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Okta | Okta | okta.com | 市值 >$15B | ZITADEL / Keycloak / Authentik（Olares 内置 Authelia） | ✅ [okta](reports/04-productivity/iam/okta.md) |

### 48. 可观测 / 监控
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Datadog | Datadog | datadoghq.com | 市值 >$40B | SigNoz / OpenObserve（Olares 有 Netdata/Grafana） | ✅ [datadog](reports/04-productivity/monitoring/datadog.md) |

### 49. Web 分析 / 邮件营销 / 预约
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Google Analytics | Google | analytics.google.com | 大厂旗舰 | Plausible / Umami | ✅ [google-analytics](reports/04-productivity/web-analytics/google-analytics.md) |
| Mailchimp | Intuit | mailchimp.com | 母公司 Intuit 旗舰 | Listmonk | ✅ [mailchimp](reports/04-productivity/email/mailchimp.md) |
| Calendly | Calendly | calendly.com | ARR >$200M[u] | Cal.diy（Cal.com 社区版） | ✅ [calendly](reports/04-productivity/project-management/calendly.md) |

### 50. 自托管 PaaS / 部署
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Vercel | Vercel | vercel.com | ARR $340M；估值 $9.3B | Coolify / Dokploy（Olares 有 Coder） | ✅ [vercel](reports/04-productivity/paas/vercel.md) |

---

## 五、存储 / 开发者 / 家居 / 隐私

### 51. 云存储 / 文件同步
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Dropbox | Dropbox | dropbox.com | ARR $2.53B；市值 $6.66B | Nextcloud / Seafile + Olares Drive | ✅ [dropbox](reports/05-storage-privacy/cloud-storage/dropbox.md) |
| Box | Box | box.com | 收入 $1.18B | Nextcloud / Cloudreve | ✅ [box](reports/05-storage-privacy/cloud-storage/box.md) |
| Google Drive / OneDrive | Google / Microsoft | — | 大厂旗舰 | Olares Drive / Nextcloud | ✅ [gdrive-onedrive](reports/05-storage-privacy/cloud-storage/gdrive-onedrive.md) |

### 52. 照片管理
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Google Photos / iCloud Photos | Google / Apple | — | 大厂旗舰 | Immich / PhotoPrism | ✅ [google-photos](reports/05-storage-privacy/photos/google-photos.md) |

### 53. 代码托管
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| GitHub | Microsoft | github.com | 大厂旗舰 | Gitea / GitLab CE | ✅ [github](reports/05-storage-privacy/code-hosting/github.md) |
| GitLab | GitLab | gitlab.com | ARR >$1B；市值 $4.69B | **GitLab CE（自托管，双形态）** | ✅ [gitlab](reports/05-storage-privacy/code-hosting/gitlab.md) |

### 54. 电子签
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| DocuSign | DocuSign | docusign.com | 收入 $3.22B；市值 $8.2B | Documenso | ✅ [docusign](reports/05-storage-privacy/e-signature/docusign.md) |

### 55. 设计协作
| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Figma | Figma | figma.com | 收入 $1.42B；市值 ~$10B | Penpot / Open Design | ✅ [figma](reports/05-storage-privacy/design-collab/figma.md) |

### 56. 密码管理
> 隐私视角总索引见 [privacy/services.md](/Users/pengpeng/seo/directions/privacy/services.md)。

| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| 1Password | AgileBits | 1password.com | ARR $400M+；估值 $6.8B | Vaultwarden / KeePassXC | ✅ [1password](reports/05-storage-privacy/password/1password.md) |
| Bitwarden | Bitwarden | bitwarden.com | 收入 ~$380M[u]；融资 $100M | **Vaultwarden（双形态）** | ✅ [bitwarden](reports/05-storage-privacy/password/bitwarden.md) |
| Dashlane | Dashlane | dashlane.com | ARR ~$113M；估值 ~$507M | Vaultwarden / KeePassXC | ✅ [dashlane](reports/05-storage-privacy/password/dashlane.md) |

### 57. 隐私 / VPN / 远程访问 / 加密存储
> 隐私视角总索引见 [privacy/services.md](/Users/pengpeng/seo/directions/privacy/services.md)。

| 商业产品 | 公司 | 域名 | 达标依据 | Olares 平替 | 报告 |
|------|------|------|---------|------------|------|
| Proton | Proton AG | proton.me | 估值 >$1B（邮件另见 #40） | Olares（Drive/Mail 自托管） | ✅ [proton](reports/05-storage-privacy/privacy-vpn/proton.md) |
| Mega.nz | Mega | mega.nz | rev ~$63M[u] | Olares Drive（端到端加密） | ✅ [mega](reports/05-storage-privacy/privacy-vpn/mega.md) |
| Tailscale | Tailscale | tailscale.com | 估值 $1.5B；融资 $275M | Headscale / LarePass | ✅ [tailscale](reports/05-storage-privacy/privacy-vpn/tailscale.md) |
| Ngrok | ngrok | ngrok.com | 融资 $50M | frp / Olares 内置反代 | ✅ [ngrok](reports/05-storage-privacy/privacy-vpn/ngrok.md) |
| NordVPN | Nord Security | nordvpn.com | ARR $357M；估值 $3B | Headscale / WireGuard | ✅ [nordvpn](reports/05-storage-privacy/privacy-vpn/nordvpn.md) |
| ExpressVPN | Kape | expressvpn.com | Kape 收入 ~$725–930M[u] | Headscale / WireGuard | ✅ [expressvpn](reports/05-storage-privacy/privacy-vpn/expressvpn.md) |
| Cloudflare Zero Trust / Tunnel | Cloudflare | cloudflare.com | 市值 ~$87B | Headscale / frp / Olares 反代 | ✅ [cloudflare-zt](reports/05-storage-privacy/privacy-vpn/cloudflare-zt.md) |

---

## 统计与下一步
- **主清单**：57 个细类。
- **附录**：GPU/算力云、模型平台（HF/Databricks）、数据标注、AI 芯片、OpenClaw 开源生态、远场无平替大 SaaS、未达门槛、已被收购见 [products-appendix.md](/Users/pengpeng/seo/directions/commerce/products-appendix.md)；**推理 API/模型托管、向量库、Embedding、数据库中间件已迁至方向 6** 见 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)；家居/可穿戴 IoT 已独立为方向 7 见 [iot/iot.md](/Users/pengpeng/seo/directions/iot/iot.md)。
- **报告**：文件按大类/细类归入 [reports/](/Users/pengpeng/seo/directions/commerce/reports)，目录树与命名约定见 [README.md](/Users/pengpeng/seo/directions/commerce/README.md)。
- **下一步**：对 `⬜` 达标产品逐个走 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)，产出落到对应细类子目录，再更新本清单平替/状态。
