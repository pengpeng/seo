# MiniMax SEO 竞品分析报告

> 域名：minimax.io（开发者/API 主站）+ hailuoai.video（消费者视频平台） | SEMrush US | 2026-07-06
> MiniMax = 中国全栈多模态 AI 独角兽（文本/语音/视频/音乐），海外以 **Hailuo AI**（视频）+ **MiniMax API**（开发者）双品牌运营

---

## 项目理解（前置）

MiniMax（稀宇科技）成立于 2021 年 12 月，总部上海，2026 年 1 月在香港联交所上市（SEHK: 100），IPO 融资约 6.19 亿美元。公司自研覆盖文本、语音、图像、视频、音乐全模态的基础模型，不依赖第三方授权——这在中国 AI 公司中独树一帜。消费侧核心产品为 **Hailuo AI**（AI 视频生成，独立域名 `hailuoai.video`）和 Talkie（AI 伴侣），开发者侧核心为 **MiniMax API 平台**（`platform.minimax.io`）。SEO 格局的关键特征：两大域名分治——minimax.io 靠语音/TTS 产品抓有机流量，hailuoai.video 靠 Hailuo AI 视频品牌词称霸。两者合计月均美国流量约 25 万，整体偏向品牌词，通用品类词竞争力弱。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 全栈多模态 AI 平台：视频生成（Hailuo AI）+ 语音合成（MiniMax Audio）+ LLM API（MiniMax M-series）|
| 开源 / 许可证 | **部分开源**：MiniMax-Text-01 与 MiniMax-VL-01 权重已开源，License 参见各模型 repo |
| 主仓库 | [github.com/MiniMax-AI](https://github.com/MiniMax-AI)（MiniMax-Text-01 HuggingFace: MiniMaxAI/MiniMax-Text-01，★ 数千）|
| 核心功能 | ① Hailuo AI 视频生成（1080p，支持 T2V/I2V，Hailuo 2.3 旗舰）② MiniMax Audio TTS/语音克隆 ③ MiniMax M3/M2.7 LLM API（$0.30/$1.20/M 输入/输出 tokens）④ MiniMax Agent（对话式 AI 助手）⑤ MiniMax Music 生成 |
| 商业模式 / 定价 | API Pay-as-you-go（M3 标准 $0.30 输入/$1.20 输出/M tokens）；Token Plan 订阅（Plus $20/月、Max $50/月、Ultra $120/月）；Hailuo AI 视频按 credits/订阅计费 |
| 差异化 / 价值主张 | 自研全模态（无外包）+ 成本领先（视频生成号称全球最低成本）+ 超长上下文（MiniMax-Text-01 支持 1M 训练/4M 推理 context）+ 部分模型开源可本地部署 |
| 主要竞品（初判）| 视频：Kling AI / Runway / Sora / Pika / Luma AI；语音：ElevenLabs / Murf AI / PlayHT；LLM API：DeepSeek / Qwen / Groq |
| Olares Market | 未上架（MiniMax-Text-01 开源权重可经 Ollama 本地运行；Hailuo 视频无本地替代，但 CogVideoX/Wan2.1 等开源模型可通过 ComfyUI on Olares 替代）|
| 来源 | [minimax.io](https://www.minimax.io)、[Wikipedia](https://en.wikipedia.org/wiki/MiniMax_Group)、[HuggingFace MiniMaxAI/MiniMax-Text-01](https://huggingface.co/MiniMaxAI/MiniMax-Text-01)、[xDev Asia review](https://xdev.asia/en/blog/minimax-detailed-review-chinese-full-stack-ai-platform/)、[API 定价文档](https://platform.minimax.io/docs/pricing/overview) |

---

## 流量基线（Phase 1）

> **注**：MiniMax 在海外运营两个主要域名，需合并看：`minimax.io`（开发者/API 主站 + 语音工具）和 `hailuoai.video`（Hailuo AI 视频消费者平台）。

### 概览（minimax.io）

| 指标 | 数据 |
|------|------|
| 域名 | minimax.io |
| SEMrush Rank | **18,863** |
| 自然关键词数 | 10,289 |
| 月自然流量（US）| 117,560 |
| 自然流量估值 | $241,065/月 |
| 付费关键词数 | 18 |
| 月付费流量 | 1,458 |
| 排名 1-3 位 | 676 词 |
| 排名 4-10 位 | 1,636 词 |
| 排名 11-20 位 | 1,760 词 |

### 概览（hailuoai.video）

| 指标 | 数据 |
|------|------|
| 域名 | hailuoai.video |
| SEMrush Rank | **16,892** |
| 自然关键词数 | 2,496 |
| 月自然流量（US）| 132,179 |
| 自然流量估值 | $190,717/月 |
| 付费关键词数 | 0（无 Google Ads 投放）|
| 排名 1-3 位 | 413 词 |
| 排名 4-10 位 | 174 词 |
| 排名 11-20 位 | 326 词 |

**两域名合并：月自然流量约 250,000，估值约 $432,000/月。** hailuoai.video 虽然词数少，但凭借"hailuo ai"这个强品牌词（49,500/月）吃下大部分流量，说明视频产品的品牌认知度已显著超越母公司品牌。

### 子域名流量分布（minimax.io）

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.minimax.io（主站）| 8,249 | 109,925 | 93.5% |
| agent.minimax.io | 292 | 5,090 | 4.3% |
| platform.minimax.io | 994 | 2,299 | 2.0% |
| space.minimax.io（各用户子域）| ~150 | ~185 | 0.2% |
| ir.minimax.io（投资者关系）| 47 | 48 | 0.04% |

### 官网 TOP 自然关键词（按流量排序）

#### minimax.io 主站

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| minimax | 1 | 40,500 | 68 | $2.59 | 32,400 | 品牌 | / |
| text to speech | 9 | 246,000 | 88 | $0.57 | 5,412 | 信息 | /audio/text-to-speech |
| minimax ai | 1 | 8,100 | 59 | $1.85 | 6,480 | 品牌 | / |
| mini max | 1 | 5,400 | 67 | $1.87 | 4,320 | 品牌 | / |
| minimax audio | 1 | 3,600 | 58 | $1.09 | 2,880 | 品牌 | /audio |
| minimax minimax | 1 | 3,600 | 76 | $2.59 | 2,880 | 品牌 | / |
| minimax.io/audio | 1 | 2,400 | 50 | $0.73 | 1,920 | 品牌 | /audio |
| minimax.io | 1 | 1,900 | 54 | $1.57 | 1,520 | 品牌 | / |
| minimax agent | 1 | 1,600 | 46 | $4.44 | 1,280 | 品牌 | agent.minimax.io |
| minmax ai | 1 | 1,600 | 52 | $1.27 | 1,280 | 品牌(变体) | / |
| ai voice cloning | 1 | 4,400 | 66 | $1.66 | 1,091 | 信息 | /audio/voices-cloning |
| ai voice generator | 7 | 74,000 | 90 | $1.06 | 962 | 信息 | /audio |
| minmax | 1 | 6,600 | 59 | $1.87 | 871 | 品牌(变体) | / |
| minimax api | 1 | 1,000 | 56 | $3.48 | 800 | 品牌 | / |
| minimax ai video | 1 | 880 | 48 | $0.76 | 704 | 品牌 | / |
| minimax audio ai | 1 | 880 | 40 | $1.60 | 704 | 品牌 | /audio |
| voice clone | 1 | 2,400 | 55 | $1.45 | 595 | 信息 | /audio/voices-cloning |
| free text to speech ai | 1 | 2,400 | 70 | $1.07 | 595 | 信息 | /audio/text-to-speech |
| ai text to speech free | 1 | 2,400 | 73 | $0.98 | 595 | 信息 | /audio/text-to-speech |
| minimax m2.7 | 1 | 720 | 38 | $6.27 | 576 | 信息 | /models/text/m27 |
| voice isolator | 4 | 6,600 | 64 | $0.49 | 429 | 信息 | /audio/voice-isolator |
| ai voice cloner | 1 | 1,600 | 40 | $1.50 | 396 | 信息 | /audio/voices-cloning |
| minimax speech 02 | 1 | 480 | 54 | $2.41 | 384 | 信息 | /news/ |
| minimax tts | 1 | 480 | 62 | $2.52 | 384 | 品牌 | /audio/text-to-speech |
| minimax m2.5 | 2 | 2,900 | 47 | $3.07 | 382 | 信息 | /models/text |
| **text to audio free** | 7 | 14,800 | 75 | $0.71 | 355 | 信息 | /audio/text-to-speech |
| free ai voice generator text to speech | 1 | 1,300 | 69 | $1.04 | 322 | 信息 | /audio/text-to-speech |
| minimax speech 2.5 | 1 | 1,300 | 36 | $0.00 | 322 | 信息 | /news/ |

> 主站非品牌词流量主力是 TTS/语音工具词（`text to speech`/`ai voice cloning`/`voice clone`），说明 minimax.io 在搜索引擎的有机增长主要靠**语音产品功能页**驱动，而非 LLM API 或视频。

#### hailuoai.video 主站（视频品牌词霸榜）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | URL |
|--------|------|------|----|----|------|-----|
| hailuo ai | 1 | 49,500 | 55 | $1.25 | 39,600 | / |
| hailou ai | 1 | 12,100 | 67 | $1.21 | 9,680 | / |
| hailuo | 1 | 12,100 | 52 | $1.45 | 9,680 | / |
| hailou | 1 | 6,600 | 60 | $1.48 | 5,280 | / |
| hailuoai | 1 | 5,400 | 64 | $1.25 | 4,320 | / |
| 海螺ai | 1 | 4,400 | 31 | $0.77 | 3,520 | / |
| haliou ai | 1 | 2,900 | 50 | $1.25 | 2,320 | / |
| hailuo ai video | 1 | 2,400 | 59 | $1.46 | 1,920 | / |
| hailuo.ai | 1 | 1,900 | 64 | $1.25 | 1,520 | / |
| hailuo ai free | 1 | 1,300 | 54 | $0.57 | 1,040 | / |
| minimax hailuo ai | 1 | 1,300 | 68 | $1.12 | 1,040 | / |
| 海螺国际版 | 1 | 1,900 | 31 | $0.82 | 471 | / |
| hailuo 2 | 1 | 480 | 57 | $1.55 | 384 | / |
| hailuo 2.3 | 1 | 480 | 43 | $1.39 | 384 | /tools/hailuo-2-3-model |
| **fal-ai/minimax/hailuo-2.3/pro/image-to-video** | 1 | 1,900 | 19 | $0.00 | — | — |

> **关键发现：** "hailuo ai" 月搜索量（49,500）是 "minimax ai"（8,100）的 6 倍，说明 Hailuo 已建立独立强品牌。中文词（`海螺ai`、`海螺国际版`）在美国也有稳定流量，表明有大量海外华人用户群。`fal-ai/minimax/hailuo-2.3/pro/image-to-video`（1,900 量/KD 19）是开发者通过 fal.ai 平台调用 Hailuo 的搜索词，意味着部分开发者绕过 MiniMax 官方 API 使用第三方推理云。

### 付费词（Google Ads，minimax.io，按流量排序）

minimax.io **仅买了 18 个极低流量的纯品牌词**，未做大规模 SEM 投放——与 Lovable 的激进买词策略完全不同。

| 关键词 | 月量 | CPC | 落地页 |
|--------|------|-----|--------|
| minimax ai | 8,100 | $1.27 | / |
| mini max | 5,400 | $2.17 | / |
| minimax artificial intelligence | 5,400 | $1.27 | / |
| minimax minimax | 3,600 | $2.43 | / |
| minimax 2.5 | 2,400 | $4.04 | / |
| minimax.io | 2,400 | $1.66 | / |
| minimax api key | 480 | $5.46 | / |

> 仅买品牌词、不买品类词（如"ai video generator"、"text to speech"）说明 MiniMax **没有内容营销 / 程序化落地页策略**，全靠产品本身驱动流量——这是重大的 SEO 空白，也是对手的可攻击面。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kling ai | 90,500 | 67 | $1.34 | 品牌 | 视频竞品，最强对手 |
| runway ai | 33,100 | 72 | $2.07 | 品牌 | 视频竞品 |
| pika labs | 27,100 | 59 | $1.36 | 品牌 | 视频竞品 |
| luma ai | 27,100 | 68 | $1.46 | 品牌 | 视频竞品 |
| elevenlabs | 246,000 | 79 | $0.73 | 品牌 | 语音竞品（流量差距悬殊）|
| sora ai | 201,000 | 72 | $0.76 | 信息 | 视频品类标杆 |
| runway ml | 18,100 | 70 | $1.71 | 品牌 | Runway 变体 |
| pika ai | 9,900 | 58 | $1.31 | 品牌 | 视频竞品 |
| murf ai | 8,100 | 78 | $0.86 | 品牌 | 语音竞品 |
| luma dream machine | 9,900 | 67 | $1.90 | 品牌 | 视频竞品 |
| cogvideox | 2,400 | 38 | $0.78 | 信息 | 开源视频模型竞品 |
| wan video | 3,600 | 74 | $0.72 | 信息 | 阿里开源视频 |
| sora alternative | 210 | **11** | $1.09 | 信息 | ⭐ |
| kling ai alternative | 170 | **5** | $1.76 | 信息 | ⭐ |
| hailuo ai alternative | 260 | **1** | $0.87 | 信息 | ⭐⭐⭐ KD=1！ |
| elevenlabs alternative | 480 | **9** | $6.16 | 信息 | ⭐⭐ CPC $6.16 |
| hailuo alternative | 40 | **2** | $1.22 | 信息 | ⭐ |
| deepseek alternative | 390 | **12** | $3.27 | 信息 | ⭐ 中国 AI 对比机会 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai video generator | 165,000 | 92 | $1.27 | 信息 | 品类第一大词，KD 极高 |
| ai video generator free | 49,500 | 79 | $1.03 | 商业 | |
| ai video maker | 27,100 | 92 | $1.08 | 商业 | |
| ai generated video | 9,900 | 85 | $1.32 | 信息 | |
| best ai video generator | 14,800 | 69 | $2.55 | 商业 | |
| ai voice generator | 74,000 | 83 | $1.15 | 信息 | |
| ai text to speech | 14,800 | 72 | $1.17 | 信息 | |
| text to speech free | 27,100 | 82 | $0.79 | 商业 | |
| text to video ai | 8,100 | 78 | $1.35 | 信息 | |
| image to video ai | 27,100 | 67 | $0.80 | 信息 | |
| ai voice cloning | 4,400 | 71 | $1.61 | 信息 | |
| text to video | 5,400 | 77 | $1.37 | 信息 | |
| ai video creation | 1,600 | 72 | $2.39 | 商业 | |
| best text to speech ai | 720 | 44 | $1.99 | 信息 | |
| ai video api | 90 | 42 | $4.36 | 信息 | |
| video generation api | 90 | 36 | $2.62 | 信息 | |
| **open source video generator ai** | 110 | **27** | $1.38 | 信息 | ⭐ |
| **comfyui image to video** | 720 | **26** | $0.78 | 信息 | ⭐ 开源工作流 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| hailuo ai | 49,500 | 55 | $1.25 | 品牌 | 视频品牌主词 |
| hailou ai | 12,100 | 67 | $1.21 | 品牌 | 误拼变体 |
| hailuo | 12,100 | 52 | $1.45 | 品牌 | |
| minimax | 40,500 | 68 | $2.59 | 品牌 | 母品牌词 |
| minimax ai | 8,100 | 59 | $1.85 | 品牌 | |
| minmax | 6,600 | 73 | $1.87 | 品牌 | 误拼 |
| minimax audio | 2,900 | 45 | $1.27 | 品牌 | |
| minimax m2.5 | 2,900 | 47 | $3.09 | 信息 | 开发者关注旧版本 |
| hailuo ai video | 2,400 | 59 | $1.22 | 品牌 | |
| minimax m2.7 | 720 | 38 | $6.27 | 信息 | ⭐ 高 CPC 开发者词 |
| minimax agent | 720 | 49 | $4.66 | 品牌 | |
| minimax api | 320 | 35 | $5.20 | 品牌 | 开发者词 |
| minimax api key | 480 | 45 | $5.46 | 品牌 | 开发者词 |
| minimax llm | 210 | 73 | $4.39 | 信息 | |
| minimax model | 260 | 49 | $5.66 | 信息 | 高 CPC |
| minimax speech | 260 | 54 | $2.04 | 品牌 | |
| **minimax pricing** | 40 | **24** | $0.00 | 商业 | ⭐ 定价痛点词 |
| minimax free api | 590 | 24 | $0.00 | 信息 | ⭐ 免费 API 需求 |
| hailuo ai pricing | 390 | 32 | $1.47 | 信息 | 定价痛点 |
| hailuo ai free | 1,300 | 54 | $0.57 | 商业 | 免费入口需求 |
| minimax hailuo | 390 | 67 | $2.87 | 信息 | 两品牌打通词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kokoro tts | 2,400 | 64 | $2.58 | 信息 | 开源 TTS 热门模型 |
| coqui tts | 1,900 | 39 | $2.27 | 信息 | 开源 TTS 替代 ⭐ |
| piper tts | 1,300 | **25** | $2.88 | 信息 | ⭐ 低 KD 开源 TTS |
| chatterbox tts | 1,300 | 54 | $3.40 | 信息 | 开源 TTS |
| local llm | 2,900 | 39 | $5.37 | 信息 | Olares 核心场景 |
| open source llm | 2,400 | 42 | $3.30 | 信息 | |
| **minimax ollama** | 260 | **35** | $0.00 | 信息 | ⭐ 用户已在搜这个词！ |
| xtts | 720 | **35** | $3.18 | 信息 | ⭐ 开源 TTS |
| comfyui image to video | 720 | **26** | $0.78 | 信息 | ⭐ 开源视频工作流 |
| bark tts | 210 | **27** | $2.24 | 信息 | ⭐ 开源 TTS |
| **open source video generation** | 30 | **24** | $1.65 | 信息 | ⭐ |
| **open source video generator ai** | 110 | **27** | $1.38 | 信息 | ⭐ |
| **fal-ai/minimax/hailuo-2.3/pro/image-to-video** | 1,900 | **19** | $0.00 | 技术 | ⭐⭐ 开发者用第三方运行 Hailuo |
| **hailuo ai alternative** | 260 | **1** | $0.87 | 信息 | ⭐⭐⭐ KD=1，自托管叙事入口 |
| **deepseek alternative** | 390 | **12** | $3.27 | 信息 | ⭐ 中国 AI 开源平替词 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：MiniMax 已开源 Text-01/VL-01 权重，而旗舰 Hailuo 视频是闭源付费 SaaS；Olares 一方面可通过 Ollama 本地运行 MiniMax-Text-01 等开源 LLM 权重，另一方面可用 CogVideoX/Wan2.1 等开源视频模型 + ComfyUI 作为 Hailuo 的本地替代方案，并用 Coqui TTS/Piper 等本地语音模型替代 MiniMax Audio——全部数据不出本地、不花 API 费用。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| hailuo ai alternative | 260 | **1** | $0.87 | ⭐⭐⭐ KD=1 的绝佳机会词；叙事：CogVideoX/Wan2.1 on ComfyUI + Olares 完全本地视频生成，不烧 credits |
| elevenlabs alternative | 480 | **9** | $6.16 | ⭐⭐⭐ 语音高 CPC 替代词；叙事：Coqui TTS/Piper/Kokoro TTS on Olares = 本地 TTS，声音数据不上云 |
| sora alternative | 210 | **11** | $1.09 | ⭐⭐ 开源视频替代对比页；Olares 部署 CogVideoX |
| kling ai alternative | 170 | **5** | $1.76 | ⭐⭐ Kling 替代，同接入开源视频模型叙事 |
| deepseek alternative | 390 | **12** | $3.27 | ⭐⭐ 中国 AI 开源模型替代词；MiniMax-Text-01 本地 + Ollama on Olares |
| minimax ollama | 260 | 35 | $0.00 | ⭐⭐ 用户已自发在搜"MiniMax 怎么配合 Ollama 用"——直接教程词，Olares Ollama 应用即答 |
| coqui tts | 1,900 | 39 | $2.27 | ⭐⭐ 开源 TTS 替代 MiniMax Audio；Olares Market 可上架 Coqui/Piper 容器 |
| piper tts | 1,300 | **25** | $2.88 | ⭐⭐ 低 KD 开源 TTS；隐私叙事：语音数据完全本地 |
| comfyui image to video | 720 | **26** | $0.78 | ⭐⭐ 替代 Hailuo AI 的开源视频工作流；Olares 本地 ComfyUI |
| local llm | 2,900 | 39 | $5.37 | ⭐ Olares 本地 LLM 核心词；运行 MiniMax-Text-01 open weights |
| open source llm | 2,400 | 42 | $3.30 | ⭐ MiniMax-Text-01 已开源；Olares 是最易安装的本地 OS |
| minimax api | 320 | 35 | $5.20 | ⭐ 开发者词；叙事：本地 Ollama API 接口 = 兼容 OpenAI API 格式，零成本替代 MiniMax API |
| open source video generation | 30 | **24** | $1.65 | ⭐ 低量但语义精准；CogVideoX/Wan2.1 on Olares |
| hailuo ai free | 1,300 | 54 | $0.57 | ⭐ 免费视频需求；Olares 本地开源视频 = 真正免费 |
| fal-ai/minimax/hailuo-2.3/pro/image-to-video | 1,900 | **19** | $0.00 | ⭐⭐ 开发者走第三方云调用 Hailuo API；Olares 叙事：本地 ComfyUI + CogVideoX 省去中间商费用 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| hailuo ai alternative | 260 | 1 | $0.87 | 信息 | **主词候选** | KD=1 绝无仅有；本地视频替代叙事（CogVideoX/Wan2.1 on Olares），可单独成文 |
| elevenlabs alternative | 480 | 9 | $6.16 | 信息 | **主词候选** | KD 9 + CPC $6.16 高价值；Coqui/Piper/Kokoro on Olares 替代 ElevenLabs/MiniMax Audio |
| sora alternative | 210 | 11 | $1.09 | 信息 | **主词候选** | KD 11；与 hailuo alternative / kling alternative 可聚为开源视频替代方案一篇 |
| kling ai alternative | 170 | 5 | $1.76 | 信息 | 次级 | 并入开源视频替代文章 |
| coqui tts | 1,900 | 39 | $2.27 | 信息 | 次级 | 开源 TTS 替代 MiniMax Audio，Olares 上架机会 |
| piper tts | 1,300 | 25 | $2.88 | 信息 | **主词候选** | KD 25；本地 TTS 叙事，隐私牌（语音数据不上云）|
| minimax ollama | 260 | 35 | $0.00 | 信息 | **主词候选** | 用户已自发搜"MiniMax + Ollama"，教程词直接承接；Olares Ollama 一键安装 |
| comfyui image to video | 720 | 26 | $0.78 | 信息 | **主词候选** | KD 26；"本地 ComfyUI 视频生成 on Olares"替代 Hailuo AI |
| deepseek alternative | 390 | 12 | $3.27 | 信息 | 次级 | 中国开源 AI 替代方向，可聚中文 AI 对比文 |
| minimax api | 320 | 35 | $5.20 | 品牌 | 次级 | 开发者词；叙事：本地 API 接口替代 = 兼容 OpenAI API 格式，零成本 |
| hailuo ai free | 1,300 | 54 | $0.57 | 商业 | 次级 | 免费视频生成需求；自托管方案是终极免费 |
| fal-ai/minimax/hailuo-2.3/pro/image-to-video | 1,900 | 19 | $0.00 | 技术 | **主词候选** | KD 19 + 量 1,900；开发者搜第三方云接入 Hailuo API，Olares 本地接入教程可夺此词 |
| open source video generator ai | 110 | 27 | $1.38 | 信息 | 次级 | 低量低 KD，并入开源视频替代文章 |
| minimax pricing | 40 | 24 | $0.00 | 商业 | GEO | 低量定价痛点词；FAQ/价格对比段落 |
| hailuo ai pricing | 390 | 32 | $1.47 | 信息 | 次级 | 定价痛点；对比"本地自托管 = $0" |
| chinese ai model | 1,300 | 48 | $1.83 | 信息 | 次级 | 可合入中国 AI 替代/对比文 |
| is minimax ai open source | 10 | 0 | $0.00 | 信息 | GEO | 量极小但正中核心叙事；GEO 占位抢 AI Overview |
| self hosted ai video generator | 40 | 46 | $1.29 | 信息 | GEO | 语义完美但量小；前瞻性 GEO 内容 |
| voice clone open source | 20 | 0 | $0.00 | 信息 | GEO | GEO 占位：Coqui/XTTS on Olares 本地语音克隆 |

---

## 核心洞见

1. **品牌护城河双轨：Hailuo AI 视频品牌强，minimax.io 主站靠 TTS 工具词。** "hailuo ai"（49,500/月）已是独立消费者品牌，远超母品牌"minimax ai"（8,100/月）。minimax.io 的非品牌流量几乎 100% 来自语音功能页（`text to speech`/`ai voice cloning`/`free ai tts`）。视频与语音两块业务的品牌词均属 KD 40-70 的护城河地带，正面抢夺无意义。

2. **MiniMax 没有内容营销策略——这是攻击面。** 付费词仅 18 个、全是品牌词；无程序化落地页（无 `/guides/`、`/alternatives/`、`/vs/` 结构）；竞品词（kling alternative、sora alternative）几乎无 KD 即无人占据。这个空白对内容型选手（包括 Olares 博客）极为有利：发一篇"hailuo ai alternative"文章，KD=1，几乎无竞争。

3. **对 Olares 最关键的三个词：`hailuo ai alternative`（260 月量/KD 1）、`minimax ollama`（260 月量/KD 35）、`elevenlabs alternative`（480 月量/KD 9）。** 第一个词 KD 接近于零，是极罕见的高相关+零竞争组合；第二个词说明用户已在主动搜索"MiniMax 怎么配合 Ollama"——Olares 的 Ollama 一键安装直接命中；第三个词 CPC $6.16 表明广告主愿意大价钱买语音替代流量，这类用户对定价敏感、Open Source TTS 叙事极易转化。

4. **最大攻击面：付费 credits 体制 + 中国法律风险。** `hailuo ai free`（1,300 月量）、`hailuo ai pricing`（390 月量）、`minimax pricing`（40 月量）、`is hailuo ai safe`（40 月量）、`is hailuo ai private`（20 月量）等词反映三类用户痛点：不想花钱、担心数据安全、担心服务可用性（Hailuo 是中国公司，部分地区有政策风险）。Olares 的反叙事："数据永远在你的硬件上、语音/视频生成不上传任何内容、一次安装永久零边际成本"——直击这三点。

5. **隐藏低 KD 金矿：TTS 开源生态词族。** `piper tts`（1,300/KD 25）、`bark tts`（210/KD 27）、`open source tts`（260/KD 32）、`open source video generation`（30/KD 24）——这些词均低竞争、与 Olares 本地部署场景完美契合，且竞争者稀少。将这些词覆写为"X on Olares 一键安装"教程，是 SEO 高性价比打法。

6. **GEO 前瞻布局：** `is minimax ai open source`（KD=0）、`voice clone open source`（KD=0）、`self hosted ai video generator`（KD 46）、`minimax self hosted`（量约 0）——这些词目前近零量，但是 2026-2027 年私有化部署 AI 趋势下的上升词。在 Olares 博客发权威内容占位，可抢 AI Overview/Perplexity 引用位。

7. **与既有分析的关联：** 本报告新增"中国 AI 开源平替"这一垂直方向（`chinese open source llm`/`deepseek alternative`/`minimax ollama`），补充了 `olares-500-keywords` 中"中国 AI 模型"子品类的空白。语音词族（`piper tts`/`coqui tts`/`elevenlabs alternative`）与既有 TTS 方向互补；视频词族（`hailuo ai alternative`/`comfyui image to video`/`cogvideox`）填补了本地视频生成这一尚未覆盖的品类。

---

*数据来源：SEMrush US 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_related / phrase_fullsearch / phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
