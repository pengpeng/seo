# model/ — 开源 AI 模型与竞品报告

这里集中管理值得为 Olares 做内容的**开源 AI 模型**，以及每个模型 family 的 brand-seo-research 报告。结构对齐 [market/](/Users/pengpeng/seo/directions/market)。

## 结构

- [models.md](/Users/pengpeng/seo/directions/model/models.md)：模型清单（按 11 类分组），每条标注许可、闭源对标与报告状态。
- [reports/](/Users/pengpeng/seo/directions/model/reports)：每个 family 一份报告，命名 `<model>.md`（无前缀、无日期，git 记录变更历史）；覆盖面较薄的 family 合并在 `other-models.md`。

## 清单怎么来的

模型没有 `beclab/apps` 那样的 manifest 仓库，所以 `models.md` **手工维护**、不写生成器。来源是 [keywords.md](/Users/pengpeng/seo/directions/model/keywords.md)（模型名 + 具体型号的关键词底稿，按 LLM / 图像 / 视频 / 3D / TTS / STT / Embedding / OCR / 翻译 / 音乐 / Omni 分类）。

## 怎么用

- 写某个模型的报告：走 `.cursor/skills/model-seo-research/` 流程，**以 model family 作为 brand**——官方域名常是模型厂商站（如 GLM→z.ai、Kimi K2→kimi.com、FLUX.2→bfl.ai），无独立官网的（如 Wan）走降级模式从关键词层面做起。产出放 `reports/<model>.md`，再把 `models.md` 中该 family 状态改为 ✅。**重写已有报告前先读旧报告，保留并去重旧洞见，不认可的可指出**。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 模型内容的通用切入点：`open source X` / `run X locally` / `X comfyui` / `X vs <闭源对标>`——Olares Market 的 Ollama / ComfyUI / vLLM 等引擎让"本地一键跑 X"成为落地路径。
