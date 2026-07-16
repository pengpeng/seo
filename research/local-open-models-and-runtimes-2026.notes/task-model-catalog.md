---
task_id: model-catalog
role: 开源模型清单审计员（Slide 21 本地可跑选型）
status: complete
sources_found: 16
---

## Sources
[1] 开源 AI 模型清单（models.md） | /Users/pengpeng/seo/directions/model/models.md | Source-Type: other | As Of: 2026-07 | Authority: 10/10
[2] LLM 研究底稿 | /Users/pengpeng/seo/directions/model/research/01-llm/llm.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[3] Omni/多模态研究底稿 | /Users/pengpeng/seo/directions/model/research/11-omni/omni.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[4] Gemma 4 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/01-llm/gemma-4.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[5] Qwen 3.6 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/01-llm/qwen-3.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[6] Ornith-1.0 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/01-llm/ornith-1.md | Source-Type: other | As Of: 2026-07 | Authority: 8/10
[7] DeepSeek V4 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/01-llm/deepseek-v4.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[8] MiniMax M3 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/01-llm/minimax-m3.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[9] FLUX.2 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/02-image/flux-2.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[10] Wan 2.2 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/03-video/wan-2.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[11] Hunyuan3D 2.1 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/04-3d/hunyuan3d.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[12] Qwen3-ASR SEO 报告 | /Users/pengpeng/seo/directions/model/reports/06-stt/qwen3-asr.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[13] ACE-Step 1.5 SEO 报告 | /Users/pengpeng/seo/directions/model/reports/10-music/ace-step.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[14] Qwen3-Embedding SEO 报告 | /Users/pengpeng/seo/directions/model/reports/07-embedding/qwen3-embedding.md | Source-Type: other | As Of: 2026-07 | Authority: 9/10
[15] Slide 21 主画面文案 | /Users/pengpeng/seo/ppt/21/accelerator-management-slide.md | Source-Type: other | As Of: 2026-07 | Authority: 10/10
[16] Slide 21 图标清单 | /Users/pengpeng/seo/ppt/assets/slide21-icons/manifest.json | Source-Type: other | As Of: 2026-07-14 | Authority: 10/10

## Findings
- 仓库 `models.md` 登记 10 模态章、72 份 model-seo 报告；选型准则为开源可本地跑、2026 near-SOTA、忽略量化变体，💻 层（Olares One 24GB）为主推层。[1]
- 当前 Slide 21 列出的 DeepSeek V4 与 MiniMax M3 在清单中属 🏢 企业级：V4-Flash 284B 需多卡 H100 级、M3 428B 需 ~800GB+ VRAM，均无法在 24GB 消费卡上作为可信本地示例。[1][7][8][15]
- Gemma 4（2026-04 发布，Apache 2.0）横跨 E2B→31B，12B 起支持音视频输入、仅文本输出，E4B/12B 分别约 8–16GB VRAM，是用户指定的多模态感知锚点。[1][4][2]
- Qwen 3.6-27B dense（Q4 ~18GB）与 35B-A3B MoE 为仓库认定的 24GB 甜点位文本/agent 主力；Ollama 已上架。[1][5][2]
- Ornith-1.0-9B（2026-06-25，MIT）Q4 ~6GB 可本地跑 agentic coding，可替换 DeepSeek V4 的“Agent”格而不夸大 VRAM。[1][6]
- 生成模态三件套 FLUX.2 klein 4B（8GB+）、Wan 2.2 TI2V-5B（8–12GB）、Hunyuan3D 2.1 Shape 3.3B+Paint 2B（8–16GB）均在 💻 层且 ComfyUI 路径成熟。[1][9][10][11]
- Qwen3-ASR 0.6B（1–2GB）与 ACE-Step 1.5 2B DiT（≥4GB）分别为语音识别与音乐生成唯一主推档；Qwen3-Embedding 0.6B（~1.2GB）补全本地 RAG。[1][12][13][14]
- 推荐 Slide 21 改为 3×3 网格：Gemma 4 · Qwen 3.6 · Ornith 9B / FLUX.2 · Wan 2.2 · Hunyuan3D / Qwen3-ASR · ACE-Step · Qwen3-Embed；可选将 Ornith 9B 换为 MiniCPM-o 4.5（<12GB 真语音 omni）。[3][6][15]
- 图标可复用 6 个（qwen、flux、wan、hunyuan3d、qwen3-asr、ace-step）；需新增 Gemma 4、Ornith 9B，Qwen3-Embedding 可复用 qwen.png。[16]
- 应拒绝的候选包括：DeepSeek V4、MiniMax M3、GLM-5.2、Kimi K2.7 Code、Qwen3-Coder 480B、Llama 4、Qwen3.5-Omni（API-only 存疑）、Ming-flash-omni 100B，以及重复模态的 Z-Image/HunyuanVideo/TRELLIS.2/TripoSG/Whisper Large。[1][2][3][7][8]

## Deep Read Notes
### Source [1]: models.md
Key data: ch.01 LLM 含 Gemma 4（L19）、Qwen 3.6（L20）、Ornith-1.0（L22）、DeepSeek V4（L24 🏢）、MiniMax M3（L26 🏢）；ch.02–04/06/07/10 分别登记 FLUX.2、Wan 2.2、Hunyuan3D、Qwen3-ASR、Qwen3-Embedding、ACE-Step 1.5。
Key insight: 清单同时收录企业级 flagship 与 💻 主力；Slide 画面应只取 💻/📱 层型号，不能把 🏢 行误作 Olares One 默认可跑。
Useful for: Slide 21 Open Models 格选型边界、拒绝名单依据。

### Source [4]: gemma-4.md
Key data: 2026-04 发布；E2B 5.7GB 8-bit、E4B 8.9GB、12B 13.4GB 8-bit、31B 17.5GB 4-bit；Ollama `gemma4` 已支持；多模态入（文/图/音/视）文本出。
Key insight: 唯一同时满足用户 Gemma 4 诉求、Apache 2.0、24GB 全系覆盖、HF/Ollama 权重的多模态 family。
Useful for: 替换 MiniMax M3 多模态格；row 1 col 1 推荐位。

### Source [7][8]: deepseek-v4.md + minimax-m3.md
Key data: V4-Pro 1.6T 需 8×H100；V4-Flash 284B 需 4×H100 量化版；M3 全精度 ~800GB+，4-bit GGUF ~213–270GB；两者均写明 Olares One 24GB 无法运行。
Key insight: 当前 Slide 21 的 DeepSeek V4 / MiniMax M3 与“本地可跑开源模型”叙事直接冲突；本地 agent 故事应改 Ornith 9B 或 R1 蒸馏档（未进 Slide 格）。
Useful for: 拒绝候选硬证据；references.md L227–236 更正依据。

## Gaps
- ch.11 Omni（Qwen3-Omni、MiniCPM-o 4.5）尚未写入 `models.md` 主表，仅存在于 `research/11-omni/omni.md`；Slide 若展示真语音 omni 需注明“研究底稿已收录、清单待补”。[1][3]
- 相反主张：DeepSeek V4-Flash 在极积极量化下官方称可 2×48GB 落地（`llm.md` L42），仍远超 Olares One 24GB，不能作为单卡示例，但不宜写成“完全不能本地跑”。[2][7]
- 相反主张：MiniMax M3 权重公开且 HF 月下载高，有社区称可用极端量化+offload 受限运行；仓库报告明确 Olares One 不可跑，Slide 不应以此作示范。[8]
- 相反主张：Qwen3.5-Omni Light 开源权重有第三方主张、官方未证实；不宜替代 Qwen3-Omni 30B-A3B 或 Gemma 4 宣传。[3]
- 未核实项：各型号在 Intel Arc / OpenVINO 后端的实际 Olares 适配成熟度；清单只保证权重可跑性与 VRAM 档，不保证全硬件后端等价。[15]
- EmbeddingGemma（308M，Gemma Terms）可作为更轻 RAG 备选，但许可与 Gemma 4 不同；主推 Qwen3-Embedding 0.6B 以保持 Qwen 栈一致。[1][14]

## END
