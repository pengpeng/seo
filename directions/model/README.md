# model/ — 开源 AI 模型竞品与报告

这里集中管理值得为 Olares 做内容的**开源、可本地运行的 AI 模型**（LLM / 图像 / 视频 / 3D / TTS / STT / Embedding / OCR / 翻译 / 音乐 / Omni 共 11 类）。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 2 的模型侧，结构对齐 [commerce/](/Users/pengpeng/seo/directions/commerce)、[iot/](/Users/pengpeng/seo/directions/iot)、[market/](/Users/pengpeng/seo/directions/market)。闭源模型 / API（GPT、Claude、Gemini 等）归 [commerce/](/Users/pengpeng/seo/directions/commerce)，此处只作「闭源对标」列引用。

## 结构

- [models.md](/Users/pengpeng/seo/directions/model/models.md)：模型清单，按模态章分组（当前 10 章，Omni/VLM 暂缺，待有可用型号再补；research/reports 仍保留 11 章结构）。每条标注代表型号 / 尺寸（**忽略量化版本**）、**部署层级**（📱 手机/边缘 · 💻 本地台式 · 🏢 企业级）、许可、闭源对标与报告状态（⬜ 待做）。只收开源、可本地运行、2026 年接近 SOTA 的型号；过期型号（如 DeepSeek R1）剔除。
- [research/](/Users/pengpeng/seo/directions/model/research)：模态级 **deep-research 调研底稿**（每章一份，带同名 `.notes/` 发现笔记 + `registry.md` 引证登记）。这是筛型号、定选题的依据。
- [reports/](/Users/pengpeng/seo/directions/model/reports)：**针对关键词的 model-seo-research 结果**（逐型号一份），按 `<章>/<model>.md` 归档。目录树已预建、`.gitkeep` 占位，写报告时直接落到对应章。

### 目录树（编号英文 slug）

`research/` 与 `reports/` 共用同一套 11 章结构：

- `01-llm/` — LLM 文本生成（含推理 / agentic / 编码模型）
- `02-image/` — 图像生成 / 编辑
- `03-video/` — 视频生成（t2v / i2v）
- `04-3d/` — 3D 生成（图生 3D / 文生 3D）
- `05-tts/` — 语音合成 TTS / 声音克隆
- `06-stt/` — 语音识别 STT / ASR
- `07-embedding/` — Embedding / Reranker（本地 RAG）
- `08-ocr/` — OCR / 文档理解
- `09-translation/` — 机器翻译
- `10-music/` — 音乐 / 音频生成
- `11-omni/` — 多模态 Omni / VLM（端到端）

> `research/<NN>/<slug>.md` 是模态 deep-research（统一骨架：摘要 / 型号总表 / 分层解读 / 候选关键词 / 关键发现 / 局限 / 参考，带 `AS_OF` 与置信度）；`reports/<NN>/<model>.md` 是逐型号 model-seo-research。

## 命名约定

- 调研底稿：`research/<NN-章>/<slug>.md`，发现笔记同级 `<slug>.notes/`（task-*.md、registry.md）。例：`research/01-llm/llm.md`、`research/02-image/image-gen.md`。
- model-seo 报告：`reports/<NN-章>/<model>.md`（无日期，git 记录变更）。例：`reports/01-llm/qwen.md`、`reports/02-image/flux2.md`。

## 清单怎么来的

模型没有 `beclab/apps` 那样的 manifest 仓库，`models.md` **手工维护**、不写生成器。11 份模态调研由 [deep-research](/Users/pengpeng/seo/.cursor/skills/deep-research/SKILL.md)（Lightweight 模式）产出——每章回答「2026 年接近 SOTA、且能本地运行的开源模型有哪些」，产出型号总表（部署层级 + 许可 + 闭源对标 + 候选关键词）。调研中的规模 / 排名是历史快照，**以后会用 Semrush + 官网重跑**。

## 怎么用

- 模态级已有 deep-research 底稿（`research/`）：型号总表 + 部署层级 + 候选关键词。**从 `models.md` 挑型号**，逐个走 [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md) 流程——**以 model family 作为 brand**（官方域名常是模型厂商站，如 GLM→z.ai、Kimi K2→kimi.com、FLUX.2→bfl.ai；无独立官网的走降级模式从关键词层面做起），产出落到对应章 `reports/<章>/<model>.md`，再把 `models.md` 中该型号报告状态改为 ✅。**重写已有报告前先读旧报告，保留并去重旧洞见，不认可的可指出**。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 模型内容的通用切入点：`open source X` / `run X locally` / `X comfyui` / `X vs <闭源对标>` / `X alternative`——Olares Market 的 Ollama / ComfyUI / vLLM 等引擎让"本地一键跑 X"成为落地路径。
