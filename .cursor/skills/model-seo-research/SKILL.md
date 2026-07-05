---
name: model-seo-research
description: 用 Semrush 研究一个开源 AI 模型（LLM / 图像 / 视频 / 3D / 语音 / Embedding 等）的 SEO——以 model family 为 brand，做流量基线、型号与引擎组合词扩展、找出与 Olares 相关的本地部署词并输出洞见。当用户要分析某个开源模型的搜索热度、部署/对比关键词，或为 Olares 找"本地跑 X 模型"内容机会时使用。
---

# 开源模型 SEO 研究

给定一个开源模型 family（如 GLM、FLUX.2、Wan、Kokoro），用 Semrush（MCP `user-semrush`）产出一份竞品分析报告，逻辑与 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md) 相同，但**以 model family 作为 brand**，并针对"模型"这一品类做专门取词与洞见。**流量/关键词数据必须来自真实 Semrush 调用**；前置的模型理解用公开来源（模型卡 / HuggingFace / GitHub / 厂商站 / 技术报告），需标注来源——两者都禁止凭常识编造。

report 名与参数速查、输出模板见 [reference.md](reference.md)。清单与状态维护在 [model/models.md](/Users/pengpeng/seo/directions/model/models.md)。

## Step 0 · 预检

1. **确认 Semrush 已登录**：先跑一次轻量调用（`keyword_research` → `phrase_this`）。返回鉴权/权限错误就停下提示用户登录，别编数据。
2. **判断"域名类型"**（模型和普通品牌最大的区别）：
   - 有厂商官网（如 GLM→z.ai、Kimi K2→kimi.com、MiniMax→minimax.io、FLUX.2→bfl.ai、SkyReels→skyreels.ai）→ 走完整流程 Step 1-5，Phase 1 用厂商域名。注意厂商站流量常混杂多个产品（如 MiniMax 靠 TTS 带量），需在洞见里剥离"哪些流量真属于这个模型"。
   - **无独立官网**（大量模型只在 HuggingFace/GitHub/ComfyUI 生态分发，如 Wan、Kokoro、TRELLIS）→ **降级模式**：跳过 Phase 1 域名报告，直接从 Step 3 的关键词层面做起，抬头注明"无独立官网，SEO 主战场在第三方内容/文档页"。
3. **默认参数**：`database=us`；探索性查询 `display_limit=30-50`；搜索量为美国月均。
4. 工作流固定：discovery 工具 → `get_report_schema(report)` → `execute_report`。

## Step 1 · 模型理解（前置调研，非 Semrush）

进 Semrush 前，先用**独立搜索**（web + 模型卡 / HF / GitHub / 技术报告）把这个模型搞清楚。它给报告定调，尤其决定 Phase 3 的"Olares 角度"。逐条查明并标注来源：

- **一句话是什么**：模态（文本/图像/视频/3D/语音/Embedding…）+ 定位 + 出品方。
- **许可证**：Apache 2.0 / MIT（商用友好）还是自定义/有地区限制（如腾讯系、skywork）——**直接影响能否作为主推卖点**，务必写明。
- **主仓库 / 分发渠道**：GitHub（★ 量级）、HuggingFace 模型页、是否进 Ollama / ComfyUI 生态。
- **参数规模与 VRAM 可跑性**（模型特有关键项）：有哪些尺寸/量化变体，**消费级能不能跑**（如 13GB/24GB 显存、fp8/gguf 量化），能否在 Olares One 上跑。这是"本地部署"叙事成立与否的前提。
- **变体 / 型号清单**：版本号（2.1/2.2）、尺寸（4B/9B/klein）、专项变体（i2v/t2v/turbo）——都是型号词来源。
- **闭源对标**：它替代哪个商业产品（FLUX/Wan→Midjourney/Sora/Kling，Kokoro→ElevenLabs，GLM/Kimi→GPT/Claude，BGE-M3→OpenAI embeddings，ACE-Step→Suno/Udio）——是 "open source X / X alternative" 内容的锚。
- **是否已在 Olares Market**：查 [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md)（模型多通过 Ollama/ComfyUI/vLLM 等引擎承载）。

产出：2-4 句模型介绍 + 一张关键事实表（模板见 [reference.md](reference.md)）。

## Step 2 · 流量基线（Phase 1）——仅有官网时做

同 brand-seo-research：`domain_overview→domain_rank`、`organic_research→resource_organic`（按流量降序，标 URL/意图）、子域名分布、付费词。**模型特有留意**：厂商站往往靠"模型名词 + 型号词"排名（如 flux kontext、kimi k2.5），也常有大量拼写变体带量；剥离出真正属于本模型的词。无官网则跳过本步。

## Step 3 · 关键词扩展（Phase 2）

1. **竞品发现**（有官网时）：`competitors_research→domain_organic_organic`。
2. **扩词**：`keyword_research` 的 `phrase_these`/`phrase_related`/`phrase_fullsearch`/`phrase_questions`/`phrase_kdi`。
3. **固定分组输出（模型版，按月量降序）**：
   - **型号 / 版本词**：`<model> 2.2`、`<model> klein`、`<model> 27b`、`<model> turbo`、`<model> i2v/t2v`。
   - **引擎组合词**（模型最核心的 Olares 前哨）：`<model> ollama`、`<model> comfyui`、`<model> vllm`、`<model> sglang`。
   - **本地部署 / 硬件词**：`<model> local`、`run <model> locally`、`<model> vram`、`<model> fp8`、`<model> gguf`、`<model> install`。
   - **对比 / 替代词**：`<model> vs <闭源>`（如 flux vs midjourney）、`open source <闭源品类>`、`<闭源> alternative`。
4. 标注 `⭐ = KD<30 且量>0` 的机会词。很多新模型词近零量，属正常——它们是 GEO 抢发候选。

## Step 4 · Olares 关联词（Phase 3）

从 Step 3 的词里筛"KD 低 + 与 Olares 部署契合"的词，每词加【Olares 角度】。模型场景至少覆盖：

- **一键跑**：`<model> comfyui / ollama / vllm` → Olares Market 对应引擎一键部署，最简路径。
- **消费级可跑性**：结合 Step 1 的 VRAM 结论，主打"能在消费级 GPU / Olares One 本地跑"。
- **许可证优势**：Apache/MIT 模型强调"商用友好、可自托管"；有地区限制的（腾讯/skywork 系）强调"本地部署规避云端合规"。
- **对比 / 替代**：`open source <闭源> alternative`（对标见 Step 1）。
- **离线 / 隐私**：数据不出本机。
- 用 `⭐⭐⭐ / ⭐⭐ / ⭐` 标契合度。

## Step 5 · 洞见 + Top 10 行动清单

**Top 10 打分**同 brand-seo-research（月量↑、KD↓、CPC↑、Olares 契合↑）。

**核心洞见**固定回答（模型版）：
1. 这个模型的搜索心智建立了吗（品牌/型号词有量吗，还是全靠 HF/Ollama 直达）？
2. **能否在消费级 GPU / Olares One 本地跑**？这是叙事成立的前提。
3. **许可证是否商用友好**？能否作为主推卖点，还是只能做技术文覆盖？
4. 对 Olares 最关键的 2-3 个词（通常是引擎组合词 / 对比词）？
5. **新模型 GEO 抢发窗口**：刚发布、近零量但语义契合的词，抢 AI Overview / Perplexity 引用位。
6. 闭源对标是谁、攻击面在哪（按 token/分钟收费、额度限制、云端隐私）？
7. 与 [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 同类 family 及 [model/keywords.md](/Users/pengpeng/seo/directions/model/keywords.md) 的关联。

## 输出约定

- 文件命名 `<family>.md`（无前缀、无日期，git 记录变更；同名报告直接覆盖更新），写到 [model/reports/](/Users/pengpeng/seo/directions/model/reports)；单 family 太薄可并入 `other-models.md` 的对应类别。产出后更新 [model/models.md](/Users/pengpeng/seo/directions/model/models.md) 该 family 的报告状态（✅ / ✅合并）。
- **重写已存在的报告前，先读现有同名报告（git 历史 / 当前文件）与相关洞见**：非重复的旧洞见尽量保留、去重合并；若不认可旧观点，明确指出并给出依据——不要每次重跑把有价值的历史判断冲掉。
- 抬头：`> SEMrush <db> | <date> | 来源：<出品方/域名>，<许可证>`。
- 结尾脚注：`数据来源：SEMrush <db>（列出实际用到的 report 名）| <date>`，并注"搜索量为美国月均，技术类产品全球量通常为美国的 3-5 倍"。
- 表格与分节顺序套用 [reference.md](reference.md) 的模板。
