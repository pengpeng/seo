---
task_id: 02
role: 图像生成研究专员（增量刷新）
status: complete
sources_found: 6
scope: +Ideogram 4（Ideogram 首个开放权重文生图）
as_of: 2026-07-05
---

## Sources

[15] Ideogram — Ideogram 4.0 Technical Details (blog) | https://ideogram.ai/blog/ideogram-4.0/ | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[16] Ideogram — Ideogram 4.0 (model page) | https://ideogram.ai/models/4.0/ | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[17] Ideogram — ideogram-4-nf4 (Hugging Face model card + LICENSE) | https://huggingface.co/ideogram-ai/ideogram-4-nf4 | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[18] Ideogram — Licensing | https://ideogram.ai/licensing/ | Source-Type: official | As Of: 2026-06 | Authority: 9/10
[19] ideogram-oss — ideogram4 (GitHub pipeline/architecture docs) | https://github.com/ideogram-oss/ideogram4 | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[20] AI Weekly — Ideogram 4: 9.3B Open-Weight DiT Tops Design Arena | https://aiweekly.co/alerts/ideogram-4-93b-open-weight-dit-tops-design-arena | Source-Type: secondary | As Of: 2026-06 | Authority: 6/10

## Findings

- Ideogram 4（2026-06-03 发布）是 Ideogram 首个开放权重文生图模型：9.3B 参数、单流（single-stream）34 层 DiT，从零训练，flow-matching（Euler 采样 + 非对称 CFG + logit-normal 噪声表）。[15][19][20]
- 架构两处差异点：① 文本编码器改用**冻结的 Qwen3-VL-8B-Instruct**（纯文本模式），从其 13 层中间隐藏态（0,3,6,…,33,35）沿特征维拼接，而非 CLIP/T5 单一 slice；② 只用**结构化 JSON caption** 训练（逐元素样式 + 可选 bounding box + 配色），参考推理管线把每条 prompt 当 JSON 解析并对 schema 校验后再生成。VAE 复用 FLUX VAE（8× 空间压缩），仅 DiT 为可训练组件。[15][19]
- 规格：emb_dim 4608 / 34 层 / 18 头 / max text tokens 2048 / 分辨率 256–2048px、宽高比最高 6:1；提供 12/20/48 步预设。[15][19]
- 地位（厂商基准）：五维（版面控制=7Bench mIoU、空间推理、物体保真、prompt 对齐、文字渲染=X-Omni OCR）对比闭源 GPT Image 2 / Nano Banana 2 及所有领先开放权重；在文字渲染上以 9.3B 反超 Z-Image Base(6.15B)、HiDream-O1(17B)、Qwen-Image(20B)、FLUX.2 dev(32B)、HunyuanImage v3(80B MoE)。[15][20]
- designer-preference ELO：4,366 名平面设计师盲测，9 条 pipeline。排序 #1 GPT Image 2（闭源，1141）、**#2 Ideogram 4.0（开放，1062）**、#3 Nano Banana 2（闭源，1004）、…#9 FLUX.2 dev（开放，900）。→ Ideogram 4 总榜 #2、开放权重 #1。另 ContraLabs 10 名设计师复核：Ideogram 47.9% 首选 vs Gemini 3.1 Flash 30.0% vs FLUX.2 [max] 15.5%。[15][20]
- 可跑性：仓库同时提供 fp8 与 nf4 checkpoint，**nf4 变体可在单张 24GB GPU 运行**（Diffusers 支持；fp8 支持全平台但暂无 Diffusers）→ 部署层级 💻 消费级（本轮口径）。权重在 HF 为 gated，需接受 license gate + token 认证才能下载。[15][17]
- 许可（关键）：HF `ideogram-ai/ideogram-4-nf4` / `ideogram-ai/ideogram-4-fp8` 公开量化权重走 **Ideogram Non-Commercial Model Agreement**（仅研究、评估、原型、个人项目）；商用需另购——self-serve 商业许可（覆盖较小规模自托管量化权重的商用）或 enterprise（全精度、客户面向、支持/安全审查、定制条款）；也可直接用 hosted API 商用。**推理代码为 Apache 2.0，但不授予权重的商用权**；微调/LoRA 在非商用协议下允许，商用微调需 self-serve/enterprise。[17][18]
- 闭源对标：GPT Image / Nano Banana / Midjourney（设计/文字/排版赛道）。[15][20]

## Deep Read Notes

### Source [15][19]: Ideogram 4.0 blog + ideogram-oss/ideogram4 docs
Key data: 9.3B 单流 34 层 DiT；Qwen3-VL-8B-Instruct 冻结文本编码器取 13 层隐藏态拼接；FLUX VAE 冻结；flow-matching Euler + 非对称 CFG；JSON prompt + schema 校验；256–2048px；nf4 单张 24GB GPU 可跑。
Key insight: "把 VLM 当文本编码器 + 纯 JSON 训练"是它相对 FLUX/Qwen/HiDream 的两处独特工程赌注，直接服务"文字渲染/版面控制"这一垂直；对 Olares 是"本地跑设计/排版文字王"的内容切口。
Useful for: 型号总表行、消费级分层、"ideogram 4 locally / best open weight text rendering" 关键词、架构说明。

### Source [17][18]: HF model card / LICENSE + Ideogram Licensing
Key data: nf4/fp8 两档，均 Ideogram Non-Commercial；gated 下载；推理码 Apache 2.0；商用分 self-serve（自托管量化权重）/ enterprise（全精度、客户面向）/ hosted API 三路径。
Key insight: 许可是本模型最大变量——"开放权重 ≠ 可商用"。内容写作须显式区分"研究/原型免费"与"生产/客户/自托管商用需授权"，否则会误导集成用户。
Useful for: 许可列判定、局限性、"ideogram alternative / commercial license" 关键词的合规表述。

### Source [20]: AI Weekly（secondary，交叉验证）
Key data: 转述发布日 2026-06-03、9.3B 单流 DiT、Qwen3-VL 编码器、Design Arena/LMArena 开放权重 #1（仅次 GPT/Gemini）、nf4/fp8 非商用、256–2048px、ContraLabs 47.9% 首选。
Key insight: 二手源与官方 [15] 主张一致，用于交叉验证发布日与对标榜单口径，不作为唯一来源。
Useful for: 发布日期与榜单叙事的第二来源背书。

## Gaps

- ELO/7Bench 等为 **Ideogram 官方内部 arena/基准**（[15]），非独立第三方一手榜单；designer-preference 与 ContraLabs 均为小样本人评。强断言"最强文字渲染"时应带"厂商基准 / 内部 arena、AS_OF 2026-06"限定词，避免与 BFL/HiDream 榜单口径冲突（同 task-01 的榜单口径警示）。
- 24GB 单卡为官方 nf4 口径；未取第三方在 12/16GB 卡上的实测显存/速度数据，更低显存段可跑性未证实。
- 公开权重当前仅文生图；博客提及"下一版 4.0"将原生返回 alpha 通道 / 可编辑文字图层（编辑能力），但尚未在开放权重中提供，未纳入编辑主力表。
- 未取 Semrush 搜索量/竞争度（Lightweight），关键词为定性候选，待验证。

## END
