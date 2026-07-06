# Baidu ERNIE（文心大模型）SEO 竞品分析报告

> 场景词分析（降级模式）| 主域名：yiyan.baidu.com（中文消费者）/ ernie.baidu.com（英文入口）| SEMrush US | 2026-07-06
> Baidu 旗舰 LLM 生态：中国 AI 头部闭源大模型（ERNIE 5.x hosted-only）+ 开源权重（ERNIE 4.5 Apache 2.0）；消费端体量以中文搜索为主，英文 US 月流量极低（ernie.baidu.com ~5,300、yiyan.baidu.com ~15,500，绝大部分为中文品牌词），触发**降级模式**。

---

## 项目理解（前置）

Baidu ERNIE（文心大模型，Enhanced Representation through Knowledge Integration）是百度自研的旗舰 LLM 系列，2019 年起持续迭代，2023 年 8 月以 ERNIE Bot（文心一言）形态向公众开放。最新发布的 ERNIE 5.1（2026 年 5 月）为 closed-weight、hosted-only 模型，在 LMArena Search 排行榜全球第 4（得分 1,223）、中文模型第 1；而 2025 年 6 月开源的 ERNIE 4.5 系列（Apache 2.0）提供从 0.3B 到 424B-MoE 的完整权重，并已进入 llama.cpp/Ollama 生态，是**目前可本地运行的最强"百度血统"中文大模型**。

消费端：yiyan.baidu.com（中文）/ernie.baidu.com（英文）自 2025 年 4 月 1 日起全面免费；企业 API：qianfan.baidu.com（Baidu Qianfan 平台，OpenAI-compatible，ERNIE 5.1 定价 $0.59/$2.65 per 1M tokens）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 百度旗舰大模型：中国用户最大规模 AI 助手（2 亿+用户），ERNIE 5.x 闭源 hosted + ERNIE 4.5 开源权重 |
| 开源 / 许可证 | ERNIE 4.5 系列：Apache License 2.0（含商用）；ERNIE 5.x：专有闭源 |
| 主仓库 | [PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE)（★ ~7,700）|
| 核心功能 | ① 中文 NLP/推理（法律、数学、商业）领先；② 多模态（文本/图像/视频）；③ 文档批量处理（接入百度网盘）；④ Agentic tool use（原生插件 + Agent Square）；⑤ 128k context（ERNIE 5.1）|
| 商业模式 / 定价 | 消费端免费（Web/iOS/Android）；企业 API $0.59/$2.65 per 1M tokens（ERNIE 5.1，Baidu Qianfan）|
| 差异化 / 价值主张 | 中文理解/生成最优；550 亿事实知识库；百度搜索/地图/网盘深度集成；ERNIE 4.5 开源权重提供离线自部署能力 |
| 主要竞品（初判）| DeepSeek（R2/V4）、Qwen3（阿里）、Kimi（月之暗面）、GPT-4o/Claude Opus |
| Olares Market | 未上架（ERNIE 4.5 可经 Ollama 间接运行，ERNIE 5.x 为 closed API）|
| 来源 | [ernie.baidu.com](https://ernie.baidu.com)、[Wikipedia/Ernie_Bot](https://en.wikipedia.org/wiki/Ernie_Bot)、[llmreference.com/ernie-5.1](https://www.llmreference.com/model/ernie-5.1)、[GitHub PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE)、[Ollama issue #11244](https://github.com/ollama/ollama/issues/11244) |

---

## 流量基线（Phase 1）——降级模式

### 域名流量概览

> **US 月均流量远低于 1,000 阈值，yiyan.baidu.com = 15,462（145 词）、ernie.baidu.com = 5,293（186 词）**，两者关键词几乎全为中文品牌词或英文品牌拼写变体，确认进入降级模式。

| 子域名 | 关键词数 | US 月流量 | 占 baidu.com US 总量 | 说明 |
|--------|---------|---------|---------------------|------|
| yiyan.baidu.com | 145 | 15,462 | 0.23% | 中文消费入口（文心一言）|
| ernie.baidu.com | 186 | 5,293 | 0.08% | 英文品牌入口（已迁移至此）|
| qianfan.baidu.com | — | — | — | 企业 API（未单独查）|

### yiyan.baidu.com TOP 自然关键词（US，全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| 文心一言 | 1 | 9,900 | 47 | $0 | 7,920 | 导航 | yiyan.baidu.com/ |
| 文言一心 | 1 | 2,900 | 48 | $0 | 2,320 | 导航 | yiyan.baidu.com/ |
| 文 心 一 言 | 1 | 1,900 | 44 | $0 | 1,520 | 导航 | yiyan.baidu.com/ |
| 文心一格 | 1 | 2,900 | 31 | $0.89 | 382 | 品牌 | yiyan.baidu.com/task/painting |
| 百度文心一言 | 1 | 720 | 66 | $0 | 576 | 导航 | yiyan.baidu.com/ |
| 文心一言官网 | 1 | 590 | 58 | $0 | 472 | 导航 | yiyan.baidu.com/ |
| 文新一言 | 1 | 390 | 39 | $0 | 312 | 导航（误拼）| yiyan.baidu.com/ |
| 文心一眼 | 1 | 390 | 47 | $0 | 312 | 导航（误拼）| yiyan.baidu.com/ |
| wenxinyiyan | 1 | 720 | 33 | $0 | 178 | 品牌 | yiyan.baidu.com/ |
| 文心 | 2 | 1,900 | 49 | $0 | 155 | 信息 | yiyan.baidu.com/ |
| 文小言 | 3 | 1,900 | 38 | $0 | 155 | 品牌 | yiyan.baidu.com/ |
| 文心大模型 | 1 | 320 | 23 | $0 | 79 | 信息 | yiyan.baidu.com/model/intro |
| baidu ai | 4 | 880 | 76 | $2.21 | 12 | 品牌 | yiyan.baidu.com/ |

> 关键发现：yiyan.baidu.com 的 US 流量几乎 100% 来自海外华人用中文品牌词直接导航，英文词仅 "baidu ai" 带来极少流量（12/月）。

### ernie.baidu.com TOP 自然关键词（US，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| ernie bot | 1 | 590 | 59 | $1.53 | 472 | 品牌 | ernie.baidu.com/ |
| ernie ai | 1 | 480 | 54 | $1.79 | 384 | 品牌 | ernie.baidu.com/ |
| ernie 5.0 | 1 | 390 | 49 | $3.28 | 312 | 品牌 | ernie.baidu.com/ |
| ernie 4.5 | 1 | 260 | 48 | $0 | 208 | 品牌 | ernie.baidu.com/ |
| baidu ernie | 1 | 260 | 53 | $2.89 | 208 | 品牌 | ernie.baidu.com/ |
| ernie x1.1 | 1 | 590 | 58 | $0 | 146 | 品牌 | ernie.baidu.com/X1 |
| ernie 5 | 1 | 170 | 73 | $4.06 | 136 | 品牌 | ernie.baidu.com/ |
| ernie baidu | 1 | 140 | 52 | $0 | 112 | 品牌 | ernie.baidu.com/ |
| wenxinyiyan | 2 | 720 | 33 | $0 | 95 | 品牌 | ernie.baidu.com/ |
| baidu ai ernie | 1 | 110 | 76 | $0 | 88 | 品牌 | ernie.baidu.com/ |
| ernie | 18 | 49,500 | 54 | $0.49 | 74 | 信息（混杂）| ernie.baidu.com/ |
| artificial intelligence baidu | 1 | 90 | 79 | $2.21 | 72 | 信息 | ernie.baidu.com/ |
| ernie 5.0 ai | 1 | 90 | 45 | $4.20 | 72 | 品牌 | ernie.baidu.com/ |

> 关键发现："ernie" (49,500/月) 目前排名 #18，是最大浪费——该词被芝麻街角色（Sesame Street）、会计软件、人名等占据，但 AI 语境下流量可观，值得内容拦截。

### 付费词（Google Ads）

> ernie.baidu.com 和 yiyan.baidu.com 均**无 Google Ads 投放**（Semrush paid keywords = 0）。Baidu 基本不在 Google 上买词投放，所有 US 曝光靠自然搜索。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| deepseek alternative | 390 | 12 | $3.27 | 信息 | ⭐⭐ 极低 KD，DeepSeek 热度带溢出 |
| ernie bot vs chatgpt | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| ernie vs deepseek | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| deepseek vs ernie | 10 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| qwen alternative | 10 | 0 | $8.10 | 信息 | GEO 前哨（高 CPC 说明商业价值） |
| ernie bot alternative | 10 | 0 | $0 | 信息 | ⭐ 近零量但精准 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ernie | 49,500 | 54 | $0.49 | 混杂 | 极大量但高度混杂（芝麻街/人名/AI），AI 上下文需明确 |
| chinese ai | 9,900 | 50 | $1.87 | 信息 | ⭐ 中等 KD，流量大，时事红利词 |
| china ai | 8,100 | 73 | $2.37 | 信息 | 高 KD，新闻/媒体占据 |
| chinese ai companies | 1,300 | 40 | $3.49 | 信息 | ⭐ 列表类内容机会 |
| chinese ai model | 1,300 | 48 | $1.83 | 信息 | 中竞争，列表类 |
| ernie-5.0-preview-1022 | 1,300 | 33 | $0 | 信息 | ⭐ 低 KD，技术发布回顾词 |
| ai china | 1,000 | 71 | $1.89 | 信息 | 高 KD，媒体主导 |
| chinese ai company | 1,000 | 63 | $3.49 | 信息 | 高 KD |
| ernie ai | 480 | 54 | $1.79 | 品牌 | 品牌词，baidu.com #1 |
| ernie 5.0 | 390 | 49 | $3.28 | 品牌 | 品牌词 |
| chinese llm | 390 | 19 | $3.14 | 信息 | ⭐⭐⭐ KD 极低 + CPC 高，黄金机会 |
| chinese ai models | 390 | 23 | $1.83 | 信息 | ⭐⭐ 列表类，低 KD |
| chinese ai open source | 390 | 44 | $0 | 信息 | ⭐ 中低 KD |
| ernie-4.5-21b-a3b-thinking | 390 | 24 | $0 | 信息 | ⭐⭐ 模型名直搜，低 KD，开发者词 |
| baidu ai | 880 | 76 | $2.21 | 品牌 | 高 KD |
| baidu ernie | 320 | 77 | $2.45 | 品牌 | 品牌护城河高 |
| ernie 4.5 | 260 | 48 | $0 | 品牌 | 中 KD |
| chinese ai chatbot | 170 | 35 | $1.44 | 信息 | ⭐ 低 KD，类别词 |
| wenxin yiyan | 170 | 17 | $0 | 品牌 | ⭐⭐⭐ KD 超低，华人用户品牌导航 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ernie x1.1 | 590 | 58 | $0 | 品牌 | 推理模型，baidu.com #1 |
| ernie bot | 590 | 59 | $1.53 | 品牌 | 核心品牌词，baidu.com #1 |
| ernie 5.0 | 390 | 49 | $3.28 | 品牌 | 品牌词，$3+ CPC |
| ernie-5.0-preview-1022 | 480 | 51 | $0 | 信息 | 技术评测词，低 CPC |
| ernie 4.5 | 260 | 48 | $0 | 品牌 | 开源版本，开发者关注 |
| baidu ernie bot | 90 | 48 | $2.90 | 品牌/商业 | 有 CPC，商业意图 |
| ernie llm | 40 | 56 | $0 | 信息 | 技术词 |
| ernie bot api | 20 | 0 | $0 | 商业 | ⭐ 近零量但高精准开发者词 |
| ernie bot login | 20 | 0 | $0 | 导航 | 用户直达 |
| how to access ernie bot | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| what is ernie bot | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| chinese llm | 390 | 19 | $3.14 | 信息 | ⭐⭐⭐ KD=19，最佳机会词 |
| chinese ai open source | 390 | 44 | $0 | 信息 | ⭐ 中低 KD |
| ernie-4.5-21b-a3b-thinking | 390 | 24 | $0 | 信息 | ⭐⭐ 开发者直接搜模型名 |
| ernie open source | 40 | 0 | $0 | 信息 | ⭐⭐⭐ 零 KD |
| baidu ernie open source | 20 | 0 | $0 | 信息 | ⭐⭐⭐ 零 KD |
| run ernie locally | 0~10 | 0 | $0 | 信息 | ⭐⭐⭐ GEO 前哨 |
| ernie 4.5 ollama | 10 | 0 | $0.89 | 信息 | ⭐⭐ 有 CPC，说明有商业价值 |
| ernie gguf | 0~10 | 0 | $0 | 信息 | ⭐⭐ 技术社区词 |
| self-hosted chinese llm | 0~10 | 0 | $0 | 信息 | ⭐⭐⭐ GEO 前哨，Olares 直接命中 |
| private chinese ai | 0~10 | 0 | $0 | 信息 | ⭐⭐⭐ GEO 前哨，隐私叙事 |
| local chinese llm | 0~10 | 0 | $0 | 信息 | ⭐⭐ 技术词 |
| chinese ai privacy | 0~10 | 0 | $0 | 信息 | ⭐⭐⭐ GEO 隐私叙事前哨 |

---

## Olares 关联词（Phase 3）

**核心逻辑：隐私叙事——"中国 AI 云 vs 本地运行 ERNIE 4.5 权重"。** ERNIE 4.5 开源权重（Apache 2.0，Hugging Face 可下载）已有 GGUF 量化版本（bartowski/unsloth 出品），ERNIE 4.5 架构已被 llama.cpp 合并（b5924+），Ollama 0.11.5+ 已可运行 `ernie-4.5:21b-a3b-q4_K_M`。Olares 一键部署 Ollama 即可在私有服务器跑 ERNIE 4.5——**数据留在本地，绕开中国云审查**。

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|------------|--------|
| chinese llm | 390 | 19 | $3.14 | "Best Chinese LLMs you can run locally on Olares + Ollama"（ERNIE 4.5 / DeepSeek / Qwen 横评）| ⭐⭐⭐ |
| deepseek alternative | 390 | 12 | $3.27 | ERNIE 4.5 作为 DeepSeek 平替之一，均可在 Olares 上本地跑 | ⭐⭐⭐ |
| chinese ai models | 390 | 23 | $1.83 | "Top Chinese open-source AI models for self-hosting on Olares"列表文 | ⭐⭐⭐ |
| ernie-4.5-21b-a3b-thinking | 390 | 24 | $0 | "How to run ERNIE 4.5 21B thinking locally with Ollama on Olares" | ⭐⭐⭐ |
| chinese ai open source | 390 | 44 | $0 | ERNIE 4.5 是 Apache 2.0 中文开源 LLM 代表之一，Olares 部署指南 | ⭐⭐ |
| chinese ai chatbot | 170 | 35 | $1.44 | Olares 上部署私有中文 AI 聊天机器人（数据不出境）| ⭐⭐⭐ |
| wenxin yiyan | 170 | 17 | $0 | 文心一言（ERNIE Bot）平替：ERNIE 4.5 权重 + Ollama on Olares | ⭐⭐ |
| ernie 4.5 | 260 | 48 | $0 | ERNIE 4.5 本地部署完整教程，Olares + Ollama | ⭐⭐ |
| ernie open source | 40 | 0 | $0 | ERNIE 4.5 是百度唯一开源系列，自部署最优路径：Olares Ollama | ⭐⭐⭐ |
| ernie 4.5 ollama | 10 | 0 | $0.89 | 直接命中：Ollama on Olares 运行 ERNIE 4.5 的教程 | ⭐⭐⭐ |
| baidu ernie open source | 20 | 0 | $0 | 零竞争，精准意图，GEO 前哨 | ⭐⭐⭐ |
| self-hosted chinese llm | ~0 | 0 | $0 | Olares 是自托管中文 LLM 的最优平台（Ollama + App Store 一键）| ⭐⭐⭐ |
| private chinese ai | ~0 | 0 | $0 | 隐私叙事核心：本地运行 ≠ 中国云数据收集 | ⭐⭐⭐ |
| chinese ai privacy concern | ~0 | 0 | $0 | GEO 前哨：数据隐私视角下的中文 AI 选择 | ⭐⭐⭐ |
| run ernie locally | ~0 | 0 | $0 | GEO 教程前哨：Olares + Ollama 手把手 | ⭐⭐⭐ |
| ernie gguf | ~0 | 0 | $0 | GGUF 下载 + Ollama on Olares 运行流程 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| chinese llm | 390 | 19 | $3.14 | 信息 | **主词候选** | KD=19 黄金词；"Best Chinese LLMs to run locally"一文可锁定，Olares+Ollama 直接命中；全球量约 1,200-2,000 |
| deepseek alternative | 390 | 12 | $3.27 | 信息 | **主词候选** | KD=12 最低竞争大流量词；ERNIE 4.5 作为备选方案 + Olares 部署，与 DeepSeek 报告联动 |
| chinese ai | 9,900 | 50 | $1.87 | 信息 | **次级** | 量极大但 KD=50，媒体/新闻占据；宜作长文辅助词或 GEO 辅助进信息摘要 |
| chinese ai models | 390 | 23 | $1.83 | 信息 | **主词候选** | KD=23，列表类文章（"Top Chinese open-source AI models"）可排 TOP 5，Olares 横评天然切入 |
| ernie-4.5-21b-a3b-thinking | 390 | 24 | $0 | 信息 | **主词候选** | 开发者直搜模型名，KD=24；本地部署教程：Olares + Ollama `ernie-4.5:21b-a3b-q4_K_M` |
| ernie bot | 590 | 59 | $1.53 | 品牌 | **次级** | 百度官网锁定 #1，难正面刚；可作"ernie bot alternative"文章副词 |
| chinese ai chatbot | 170 | 35 | $1.44 | 信息 | **次级** | KD=35，量中等，可并入"self-hosted Chinese AI"文章 |
| wenxin yiyan | 170 | 17 | $0 | 品牌 | **次级** | KD=17 极低，海外华人品牌词；并入文心一言平替/对比文 |
| ernie 4.5 | 260 | 48 | $0 | 品牌 | **次级** | 开源版本关注词；本地部署教程的长尾 |
| chinese ai companies | 1,300 | 40 | $3.49 | 信息 | **次级** | 量大 KD 中等，列表文辅助；Baidu 作为其中一家，Olares 提供"用开源权重绕开云"叙事 |
| ernie open source | 40 | 0 | $0 | 信息 | **GEO** | 零 KD，精准意图；进 FAQ/教程头部段落，抢 AI Overview 引用 |
| baidu ernie open source | 20 | 0 | $0 | 信息 | **GEO** | 同上，品牌限定更精准 |
| ernie 4.5 ollama | 10 | 0 | $0.89 | 信息 | **GEO** | 有 CPC 表明商业价值；Ollama on Olares 教程直接命中 |
| self-hosted chinese llm | ~0 | 0 | $0 | 信息 | **GEO** | 零量近零竞争，GEO/AI Overview 前哨，Olares 叙事核心 |
| private chinese ai | ~0 | 0 | $0 | 信息 | **GEO** | 隐私叙事：中国 AI 云 vs 本地运行；Olares 差异化核心 |
| chinese ai privacy concern | ~0 | 0 | $0 | 信息 | **GEO** | GEO 前哨；进"Is Chinese AI safe to use?"类文章 |
| run ernie locally | ~0 | 0 | $0 | 信息 | **GEO** | Ollama on Olares 教程的 H2/FAQ 精准命中 |

---

## 核心洞见

1. **品牌护城河**：ernie.baidu.com 锁定所有英文品牌词（"ernie bot" / "ernie ai" / "ernie 4.5" #1），且 yiyan.baidu.com 覆盖全部中文品牌词。**不可正面刚品牌词**——百度在自己的品牌词上占据所有 #1 位，KD 普遍 50+。Olares 的机会在**品牌词的旁侧**：开源/本地部署/隐私叙事类词，百度不写这类内容。

2. **可复制的打法**：百度本身没有英文 SEO 内容运营能力——ernie.baidu.com 的英文 blog 以技术发布公告为主，无"how to"教程、无对比文、无 Open Source 内容。第三方（HuggingFace 页面、技术博客、Reddit r/LocalLLaMA）目前在占据自然搜索排名。**Olares 可以做百度不会做的内容**：ERNIE 4.5 本地部署教程、中文 LLM 横评、Chinese AI privacy 叙事文章。

3. **对 Olares 最关键的 3 个词**：
   - `chinese llm`（390/月，KD=19）——量与竞争最佳比；覆盖 ERNIE + DeepSeek + Qwen 三个中文开源模型
   - `deepseek alternative`（390/月，KD=12）——ERNIE 4.5 是天然候选答案之一，与 DeepSeek 报告联动
   - `ernie-4.5-21b-a3b-thinking`（390/月，KD=24）——模型名直搜，开发者精准意图，Ollama on Olares 教程一步命中

4. **最大攻击面**：
   - **数据隐私/审查**：ERNIE Bot（hosted）数据过中国服务器，受《网络安全法》/《数据安全法》约束；海外用户真实关切（"chinese ai censorship" / "chinese ai privacy"）。Olares 叙事：ERNIE 4.5 开源权重本地跑 = 中文语言能力 + 数据不出境
   - **账号门槛**：ERNIE Bot 企业 API 仍需中国手机号或营业执照，海外开发者体验差
   - **Ollama 支持滞后**：直到 llama.cpp b5924（2025 年中）才合并 ERNIE 4.5 架构，VL（视觉理解）版本至今仍不支持 Ollama——内容可直接锁定"How to run ERNIE 4.5 locally without VPN/Chinese account"

5. **隐藏低 KD 金矿**：
   - `chinese llm`（KD=19，$3.14 CPC）：CPC 高说明有付费竞争，但自然搜索 KD 极低——可能是新兴词，Semrush 数据库尚未跟上，先占先得
   - `wenxin yiyan`（KD=17）：海外华人社区品牌词，百度中文站排名良好但**英文内容几乎为零**；"文心一言平替：ERNIE 4.5 本地部署"类华人向内容有机会
   - `ernie-4.5-21b-a3b-thinking`（KD=24）：390/月看似普通，但全球量约 1,200-2,000，开发者意图明确，竞争几乎只有 GitHub issue 和 HuggingFace 页面

6. **GEO 前瞻布局**：
   - `self-hosted chinese llm` / `private chinese ai` / `run ernie locally`：当前搜索量接近零，但在 ChatGPT / Perplexity / AI Overview 问到"How to run a Chinese LLM locally?"时，这些语义精准的 FAQ 段落会被优先引用
   - `chinese ai privacy concern`：随着美国对中国 AI 监管/用户隐私讨论升温（2025-2026 年持续），此词搜索量将增长；现在布局 = 零竞争窗口期
   - `ernie bot alternative`：搜索量仍低，但 GEO 时代问答逻辑会触发此类比较内容

7. **与既有分析的关联**：
   - 与 [olares-500-keywords 分析](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md) 的关联：ERNIE 报告补充了"Chinese AI"品类词维度（`chinese llm` KD=19 是分析中未收录的低竞争词），以及"数据主权/隐私"叙事与 Olares self-hosting 的结合
   - 与 DeepSeek 报告的联动：`deepseek alternative` 是两份报告都可用的词，"Chinese open-source LLM 横评"一文可同时覆盖 ERNIE 4.5 / DeepSeek / Qwen，聚合三份报告流量
   - `chinese llm`（KD=19）可能是整个中文 LLM 赛道最高性价比的英文词，应优先布局

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、phrase_these、phrase_related、phrase_questions、domain_organic_organic）| 2026-07-06*

*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。ernie.baidu.com 与 yiyan.baidu.com 的 US 月流量均低于 1,000 有效词量阈值，本报告采用降级模式，以关键词维度分析代替域名流量基线。ERNIE 4.5 Ollama 支持状态：llama.cpp b5924+ 已合并 ernie4_5 架构，Ollama 0.11.5+ 可运行 `ernie-4.5:21b-a3b-q4_K_M`；VL 版本暂不支持 Ollama（截至 2026-07）。*
