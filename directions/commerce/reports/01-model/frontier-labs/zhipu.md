# Zhipu AI / GLM SEO 竞品分析报告

> 域名：zhipuai.cn（企业主站）+ bigmodel.cn（API开发者门户）+ z.ai（国际品牌，2026起）| SEMrush US | 2026-07-06
> 中国领先 LLM 独立厂商，港交所上市（02513.HK），以开源 GLM 系列（GLM-4/GLM-5.2）+闭源 API 双轨驱动，CodeGeeX/CogVideoX/AutoGLM 多产品矩阵，国际化品牌切换至 Z.ai

> ⚠️ **降级说明**：主站 zhipuai.cn 的 US 月均自然流量仅 ~2,182（SEMrush US 库），触及降级模式阈值；本报告补充 bigmodel.cn（US 有机流量 28,216/月）和 z.ai（US 有机流量 55,326/月）的完整数据以弥补不足，并着重扩充关键词层面分析。

---

## 项目理解（前置）

Zhipu AI（智谱）成立于 2019 年，清华大学 NLP 实验室分拆，2026 年 1 月登陆港交所（股票代码 02513.HK，简称"知识图谱"），首次公开募股约 5.58 亿美元，2026 年 6 月市值突破港币 1 万亿（约 1280 亿美元）。2025 年全年营收人民币 7.243 亿（约 1.05 亿美元），净亏损 47.2 亿，正处于高速增长、仍亏损阶段。核心产品线：GLM 系列大模型（开源权重 + 闭源 API 双轨）、CodeGeeX（代码补全/IDE 插件）、CogVideoX（视频生成）、AutoGLM（手机/Web Agent）、zhipu Qingyan / ChatGLM（面向消费者聊天）。国际品牌 Z.ai 于 2026 年正式推出，已集成进 Cloudflare 和 Notion 等平台。最新旗舰开源模型 GLM-5.2（2026 年 6 月发布）：744B-A40B MoE，MIT 协议，HuggingFace 上月下载量已逾 23 万次；NVIDIA 也推出了 GLM-5.2-NVFP4 量化版（月下载量 28 万+）。面向本地部署的最佳入口是 GLM-4-9B（9B 参数、128K 上下文、Apache 2.0），可直接通过 Ollama 运行。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 中国最大独立 LLM 厂商，港股上市，GLM 开源+API 双轨 |
| 开源 / 许可证 | 双轨：GLM-5.2 MIT、GLM-4-9B Apache 2.0；API/私有化部署闭源 |
| 主仓库 | [github.com/zai-org/GLM-5](https://github.com/zai-org/GLM-5)（★6.2K）/ [GLM-4](https://github.com/zai-org/GLM-4)（历史版本）；原组织 THUDM 仍有大量模型 |
| 核心功能 | GLM 系列 LLM（文本/代码/推理）、CodeGeeX 代码补全、CogVideoX 视频生成、AutoGLM Web/移动 Agent、GLM Coding Plan 订阅（IDE 集成 Claude Code 等）|
| 商业模式 / 定价 | SaaS API 按 token 计费（2025 两次涨价）+ 订阅（GLM Coding Plan 月付）+ 企业私有化部署；GLM-4-Flash 免费层；GLM-4-9B 开源可自部署 |
| 差异化 / 价值主张 | 中文表现业内领先；MIT 开源无区域限制；作为 OpenAI/Anthropic 替代商已集成 Notion/Cloudflare；GLM Coding Plan 内嵌 Claude Code、CursorTab 等工具链是独特生态护城河 |
| 主要竞品（初判）| DeepSeek（国内开源 LLM）、Qwen / Alibaba Cloud（国内 API）、Moonshot AI / Kimi（国内竞品）、Minimax AI；国际层面：OpenAI API、Anthropic Claude API |
| Olares Market | Ollama 已上架 ✅；GLM 权重本身未独立上架（通过 Ollama 使用）|
| 来源 | [zhipuai.cn](https://zhipuai.cn) / [z.ai](https://z.ai) / [bigmodel.cn](https://bigmodel.cn) / [HuggingFace zai-org](https://huggingface.co/zai-org) / [HKEX 2025 年报](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0419/2026041900085.pdf) / [Asia Tech Review](https://www.asiatechreview.com/p/zhipu-chinas-breakout-ai-star-is) |

---

## 流量基线（Phase 1）

> 智谱 AI 旗下有三个主要域名，SEO 策略各有侧重，本报告同时呈现。

### 概览（三域名并列，US 数据库）

| 指标 | zhipuai.cn（企业主站）| bigmodel.cn（API 门户）| z.ai（国际品牌）|
|------|----------------------|----------------------|----------------|
| SEMrush Rank | 613,135 | 70,925 | 38,110 |
| 自然关键词数 | 365 | 596 | 3,402 |
| 月自然流量（US）| **2,182** ⚠️ 降级阈值 | **28,216** | **55,326** |
| 自然流量估值 | $1,001/月 | $25,877/月 | $108,937/月 |
| 付费关键词数 | 0 | 0 | **125** |
| 月付费流量 | 0 | 0 | ~4,152 |
| 排名 1-3 位 | 62 词 | 90 词 | 322 词 |
| 排名 4-10 位 | 57 词 | 84 词 | 378 词 |
| 排名 11-20 位 | 62 词 | 88 词 | 356 词 |

**关键洞察**：z.ai 是智谱国际化的核心阵地（55K US 流量 + 付费投放），bigmodel.cn 是开发者门户，zhipuai.cn 是企业/投资者站点（US 流量极低）。三站之间流量有互补也有重复竞争（同一公司但 SEO 策略未完全整合）。

### bigmodel.cn 子域名流量分布

| 子域名 | 关键词数 | 流量（US）| 占比 |
|--------|---------|----------|------|
| bigmodel.cn（根域）| 187 | 25,252 | 89.5% |
| docs.bigmodel.cn | 281 | 2,159 | 7.65% |
| open.bigmodel.cn | 101 | 735 | 2.60% |
| www.bigmodel.cn | 26 | 70 | 0.25% |

文档站（docs.bigmodel.cn）关键词数多于根域（281 vs 187），但流量占比仅 7.65%，说明文档页的排名多在较低位或长尾低量词。

### bigmodel.cn TOP 自然关键词（按流量降序，US 库）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| 智谱 | 1 | 9,900 | 44 | $0.30 | 7,920 | 导航 | bigmodel.cn/ |
| 智谱ai | 1 | 4,400 | 43 | $0.41 | 3,520 | 导航 | bigmodel.cn/ |
| 智普 | 1 | 2,400 | 48 | $0.74 | 1,920 | 导航 | bigmodel.cn/ |
| 智谱开放平台 | 1 | 2,400 | 40 | $0.68 | 1,920 | 导航 | bigmodel.cn/ |
| zhipu | 1 | 2,400 | 65 | $0.39 | 1,920 | 导航 | bigmodel.cn/ |
| 智谱 ai | 1 | 1,600 | 42 | $0.94 | 1,280 | 导航 | bigmodel.cn/ |
| 智谱 claude code | 1 | 1,300 | 26 | $8.48 | 1,040 | 信息 | docs.bigmodel.cn/cn/coding-plan/tool/claude |
| 智谱旺旺 | 1 | 1,900 | 12 | $0.00 | 471 | 信息/交易 | docs.bigmodel.cn/.../wangwang |
| bigmodel | 1 | 880 | 13 | $2.38 | 704 | 导航 | bigmodel.cn/ |
| 智谱清言api | 1 | 390 | 34 | $1.22 | 312 | 导航 | bigmodel.cn/ |
| 智谱大模型 | 1 | 390 | 27 | $0.00 | 312 | 信息 | bigmodel.cn/ |
| 智谱旺旺（×4 条目）| 1-10 | 1,900 | 12 | $0.00 | 44-83 各 | 混合 | 多个落地页 |
| glm coding plan | 1 | 1,900（注） | 25 | $3.03 | 112 | 商业 | open.bigmodel.cn/glm-coding |
| glm | 4 | 14,800 | 56 | $2.21 | **133** | 信息 | bigmodel.cn/ |
| chatglm api | 1 | 50 | 37 | $0.00 | 40 | 导航 | bigmodel.cn/ |

> 注：bigmodel.cn 上约 89% 的 US 有机流量来自中文字符搜索词（中国留学生/华人社区），"glm"这一最重要的英文关键词因位居第 4 位，仅获 133 流量。z.ai 以 #1 排名吃走了大部分 "glm" 流量（1,953 traffic）。

### z.ai TOP 自然关键词（部分，按流量降序，US 库）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| zai | 1 | 6,600 | 82 | $1.59 | 5,280 | 导航 | z.ai/ |
| z ai | 1 | 6,600 | 75 | $1.62 | 5,280 | 导航 | z.ai/ |
| z.ai | 1 | 5,400 | 83 | $1.62 | 4,320 | 导航 | z.ai/ |
| zcode | 1 | 2,900 | 34 | $1.43 | 2,320 | 导航 | zcode.z.ai/en |
| **glm** | **1** | **14,800** | **56** | **$2.21** | **1,953** | 信息 | z.ai/blog/glm-5.2 |
| z-ai | 1 | 2,400 | 72 | $1.62 | 1,920 | 导航 | z.ai/ |
| glm 4.7 | 1 | 5,400 | 44 | $2.23 | 1,339 | 信息 | z.ai/blog/glm-4.7 |
| glm-5 | 1 | 4,400 | 64 | $1.75 | 1,091 | 信息 | z.ai/blog/glm-5 |
| z.ai api | 1 | 1,300 | 64 | $2.81 | 1,040 | 导航 | z.ai/model-api |
| chat.z.ai | 1 | 1,300 | 44 | $1.10 | 1,040 | 导航 | z.ai/ |
| glm-4.6 | 1 | 3,600 | 48 | $2.25 | 892 | 信息 | z.ai/blog/glm-4.6 |
| glm coding plan | 1 | 2,900 | 26 | $2.50 | 719 | 商业 | z.ai/subscribe |
| autoclaw | 1 | 2,900 | 33 | $1.22 | 719 | 信息 | autoclaw.z.ai/web/ |
| z.ai claude code | 1 | 880 | 34 | $4.86 | 704 | 信息 | docs.z.ai/devpack/tool/claude |
| glm 4.5 | 1 | 3,600 | 78 | $1.88 | 475 | 信息 | z.ai/blog/glm-4.5 |
| autoclaw | 1 | 2,900 | 33 | $1.22 | 719 | 信息 | autoclaw.z.ai/web/ |
| coding plan | 1 | 2,400 | 32 | $6.12 | 316 | 信息 | docs.z.ai/devpack/overview |
| opencode | 5 | 49,500 | 58 | $6.03 | 495 | 导航 | docs.z.ai/devpack/tool/opencode |

z.ai 以博客/版本发布页为核心内容策略（`/blog/glm-*`），每次模型迭代（4.5→4.6→4.7→5→5.2）都对应一篇排名较高的博文。"opencode"（49,500 月量）因 z.ai 支持文档进入 top5，是意外流量来源。

### 付费词（zhipuai.cn / bigmodel.cn 无投放；z.ai 有125个付费词）

z.ai 的 Google Ads 投放方向为品牌防御词（"z.ai"、"chat z.ai"）及竞品拦截，流量约 4,152/月，CPC 区间 $1-6，体量较小。bigmodel.cn / zhipuai.cn 均无付费投放。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kimi ai | 22,200 | 86 | $0.88 | 导航 | 国内最强竞品 Moonshot，极难排 |
| minimax ai | 8,100 | 53 | $1.27 | 导航 | 国内 AI 竞品 |
| moonshot ai | 5,400 | 81 | $1.32 | 导航 | Kimi 母公司，高 KD |
| baidu ernie | 320 | 77 | $2.45 | 导航 | 百度 ERNIE，高 KD |
| deepseek alternative | 390 | **12** | $3.27 | 信息 | ⭐ 最低 KD，GLM 可作 DS 平替 |
| glm vs claude | 140 | **28** | **$7.22** | 信息 | ⭐ CPC 极高，比较意图 |
| glm vs deepseek | 20 | 0 | $0 | 信息 | ⭐ GEO，近零量但精准 |
| qwen alternative | 10 | 0 | $8.10 | 信息 | ⭐ GEO，超高 CPC |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| chinese ai model | 1,300 | 48 | $1.83 | 信息 | 品类品牌词，GLM 适配 |
| china ai model | 590 | 62 | $1.37 | 信息 | 同上，稍难 |
| chinese llm | 390 | **19** | $3.14 | 信息 | ⭐ KD 极低，Olares 叙事入口 |
| self hosted llm | 320 | **22** | $3.12 | 信息 | ⭐ 自托管意图，GLM-4-9B + Ollama |
| general linear model | 2,900 | 35 | $2.71 | 信息 | 统计学同名词，干扰较大 |
| glm model | 1,300 | 53 | $5.27 | 信息 | 混合意图（统计+AI） |
| glm ai | 1,000 | 44 | $3.26 | 信息 | 品类内容词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| chatglm | 14,800 | 45 | $0.10 | 导航 | 老品牌 ChatGLM，仍有大量搜索 |
| glm | 12,100 | 54 | $2.71 | 信息 | 旗舰词，z.ai #1；混有统计学含义 |
| glm 4.7 | 5,400 | 44 | $2.23 | 信息 | 最新 API 版本，z.ai #1 |
| autoclaw | 2,900 | **33** | $1.22 | 信息 | ⭐ Web Agent 产品，z.ai #1 |
| glm-4.5-air | 2,400 | 50 | $5.49 | 信息 | 旗舰 API 版本，高 CPC |
| cogvideox | 2,400 | **38** | $0.78 | 信息 | ⭐ 开源视频生成，月下载 >230K |
| glm coding plan | 1,900 | **25** | $3.03 | 商业/交易 | ⭐ 编程订阅，两站均 #1 |
| autoglm | 1,300 | 58 | $0.33 | 信息 | Agent 产品，KD 偏高 |
| glm model | 1,300 | 53 | $5.27 | 信息 | 高 CPC 信号 |
| codegeex | 1,000 | 47 | $0.00 | 信息 | 开源代码补全助手 |
| glm-4.5-flash | 720 | **30** | $2.45 | 信息 | ⭐ 免费快模型 |
| glm-4 | 720 | 50 | $1.77 | 信息 | 上一代，仍有搜索 |
| glm 4.5 api | 110 | **32** | $0 | 信息/商业 | ⭐ 开发者 API 词 |
| glm api | 140 | **18** | $1.30 | 信息/商业 | ⭐ KD 极低！ |
| glm coding | 210 | **29** | $1.81 | 信息 | ⭐ 编程功能词 |
| is glm free | 260 | **22** | $0 | 信息 | ⭐ FAQ 类，高转化 |
| what is glm | 210 | **18** | $0 | 信息 | ⭐ 入门 FAQ |
| glm-4-9b | 170 | **31** | $0 | 信息 | ⭐ 9B 开源权重，Ollama 入口 |
| z.ai claude code | 1,600 | **33** | $4.95 | 信息 | ⭐ GLM 内嵌 Claude Code |
| glm 4.5 | 3,600 | 70 | $2.18 | 信息 | KD 高，z.ai #1 |
| glm-5 | 4,400 | 70 | $1.64 | 信息 | KD 高，z.ai #1 |
| z.ai api | 1,600 | 48 | $4.53 | 导航 | z.ai 国际 API 词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| self hosted llm | 320 | **22** | $3.12 | 信息 | ⭐ 最强 Olares 入口 |
| chinese llm | 390 | **19** | $3.14 | 信息 | ⭐ 品类 + 自托管角度 |
| deepseek alternative | 390 | **12** | $3.27 | 信息 | ⭐ KD 最低，GLM 即替代 |
| glm api | 140 | **18** | $1.30 | 信息/商业 | ⭐ 本地 API 叙事 |
| ollama glm | 140 | 49 | $0 | 导航/商业 | Ollama + GLM 直接关联 |
| glm-4-9b | 170 | **31** | $0 | 信息 | ⭐ 9B 权重，Ollama 首选 |
| glm download | 50 | **31** | $0 | 信息 | ⭐ 下载意图 |
| is glm open source | 50 | 0 | $0 | 信息 | ⭐ GEO，Olares FAQ |
| is glm 5 open source | 50 | 0 | $0 | 信息 | ⭐ GEO，MIT 开源 |
| run glm locally | <10 | 0 | $0 | 信息 | ⭐ GEO，完美 Olares 叙事 |

---

## Olares 关联词（Phase 3）

**核心逻辑：GLM-4-9B（Apache 2.0）及 GLM-5.2（MIT）开源权重可通过 Olares Market 已上架的 Ollama 一键本地运行，完全不依赖中国云或 zhipuai.cn API，且数据留在用户自己的硬件上。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|------|
| self hosted llm | 320 | 22 | $3.12 | GLM-4-9B via Ollama on Olares = 一句话自托管方案 | ⭐⭐⭐ |
| chinese llm | 390 | 19 | $3.14 | 运行中文表现最强的开源 LLM，完全离线 | ⭐⭐⭐ |
| is glm open source | 50 | 0 | $0 | GEO：是的，GLM-4-9B Apache 2.0，GLM-5.2 MIT，Ollama on Olares 可运行 | ⭐⭐⭐ |
| run glm locally | <10 | 0 | $0 | GEO 前哨：Olares + Ollama + GLM-4-9B 三步教程 | ⭐⭐⭐ |
| deepseek alternative | 390 | 12 | $3.27 | GLM-4-9B 即 DeepSeek-R1 平替（同为中文 SOTA 开源）；Olares 可同时跑两者 | ⭐⭐⭐ |
| is glm free | 260 | 22 | $0 | FAQ：本地运行 GLM-4-9B 完全免费（Olares + Ollama，无 token 计费） | ⭐⭐ |
| ollama glm | 140 | 49 | $0 | Ollama 已在 Olares Market，直接指引 | ⭐⭐ |
| glm-4-9b | 170 | 31 | $0 | 最适合 Olares One（NVIDIA 24GB）的 GLM 权重；可跑 9B 全精度 | ⭐⭐ |
| glm download | 50 | 31 | $0 | 下载意图用户是最强转化人群；引导至 Ollama on Olares | ⭐⭐ |
| glm api | 140 | 18 | $1.30 | 本地 Ollama 提供兼容 OpenAI 的 /v1 endpoint，替代 bigmodel API | ⭐⭐ |
| glm vs claude | 140 | 28 | $7.22 | 比较文：Olares 可本地运行 GLM 无费率上限，vs Claude API 按用量计费 | ⭐⭐ |
| glm coding plan | 1,900 | 25 | $3.03 | 商业痛点：GLM Coding Plan $19+/月；Ollama on Olares = $0/月（权重开源） | ⭐⭐ |
| chinese ai model | 1,300 | 48 | $1.83 | 类别词；Olares = 中国开源模型本地化聚合平台 | ⭐ |
| glm vs deepseek | 20 | 0 | $0 | GEO：Olares 同时跑 GLM + DeepSeek 做对比 | ⭐⭐ |
| is glm 5 open source | 50 | 0 | $0 | GEO：GLM-5.2 MIT 开源，但 744B MoE 需多 GPU 集群 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇（可跨报告）在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| chatglm | 14,800 | 45 | $0.10 | 导航 | 次级 | 旧品牌词，量大但导航意图；可作内容中的历史对比点 |
| glm | 12,100 | 54 | $2.71 | 信息 | **主词候选** | z.ai 已排 #1；混有统计学含义需区分；高量值得入场，角度"GLM AI model explained" |
| glm 4.7 | 5,400 | 44 | $2.23 | 信息 | **主词候选** | z.ai #1 博文；KD 44 中等；Olares 角度：GLM-4.7 API vs 本地 9B 对比 |
| glm 4.6 | 4,400 | 47 | $2.25 | 信息 | **主词候选** | 同上，版本系列话题 |
| glm-5 | 4,400 | 70 | $1.64 | 信息 | 次级 | KD 70，主力 z.ai 占位；作次级进主词文章 |
| cogvideox | 2,400 | **38** | $0.78 | 信息 | **主词候选** ⭐ | 开源视频生成，KD 合理，月下载 >23万；Olares 可本地部署 |
| glm coding plan | 1,900 | **25** | $3.03 | 商业 | **主词候选** ⭐ | 低 KD 高 CPC，两站均 #1；Olares 角度：Coding Plan vs Ollama-GLM 成本对比 |
| z.ai claude code | 1,600 | **33** | $4.95 | 信息 | **主词候选** ⭐ | 高 CPC，低 KD，z.ai #1；IDE 集成痛点词 |
| z.ai api | 1,600 | 48 | $4.53 | 导航 | 次级 | 开发者导航词；Olares 本地 /v1 端点替代叙事 |
| autoclaw | 2,900 | **33** | $1.22 | 信息 | **主词候选** ⭐ | z.ai Web Agent 产品，KD 低；潜力词 |
| chinese llm | 390 | **19** | $3.14 | 信息 | **主词候选** ⭐ | KD 极低！中文 LLM 品类词；Olares = 本地运行中国开源 LLM |
| deepseek alternative | 390 | **12** | $3.27 | 信息 | 次级 ⭐ | KD 最低！GLM 即 DeepSeek 可信替代；聚入"Chinese open source LLM"簇 |
| self hosted llm | 320 | **22** | $3.12 | 信息 | **主词候选** ⭐ | Olares+GLM 核心词；KD 低，量适中，写 GLM+Ollama+Olares 教程文 |
| glm-4.5-air | 2,400 | 50 | $5.49 | 信息 | 次级 | CPC 超高（$5.49），商业意图强；做对比文时作次级 |
| glm-4.5-flash | 720 | **30** | $2.45 | 信息 | **主词候选** ⭐ | 免费快模型，KD 30，可写免费层对比文 |
| is glm free | 260 | **22** | $0 | 信息 | 次级 ⭐ | FAQ，Olares 角度：本地运行 GLM-4-9B 完全免费 |
| chinese ai model | 1,300 | 48 | $1.83 | 信息 | **主词候选** | 品类词，量足；Olares 叙事：一站运行所有中国开源模型 |
| glm model | 1,300 | 53 | $5.27 | 信息 | 次级 | 高 CPC 但 KD 高，纳入品类词文章 |
| codegeex | 1,000 | 47 | $0 | 信息 | **主词候选** | 开源代码助手，量够；有独立搜索需求 |
| glm ai | 1,000 | 44 | $3.26 | 信息 | 次级 | 作为主词的 long-tail 变体收录 |
| glm-4-9b | 170 | **31** | $0 | 信息 | 次级 ⭐ | 开源 9B 部署词；Olares One 可跑 FP16 全精度；作教程文次级锚 |
| glm api | 140 | **18** | $1.30 | 信息/商业 | 次级 ⭐ | KD=18，极低！本地 Ollama /v1 替代叙事 |
| ollama glm | 140 | 49 | $0 | 导航/商业 | 次级 | Ollama on Olares 直接教程词 |
| glm vs claude | 140 | **28** | $7.22 | 信息 | 次级 ⭐ | 比较词，CPC $7 极高，商业意图；Olares 叙事：本地 GLM 无成本上限 |
| glm download | 50 | **31** | $0 | 信息 | 次级 ⭐ | 下载意图，引导至 Ollama |
| thudm | 90 | 43 | $0 | 导航 | 次级 | 清华 NLP 学术品牌词，HuggingFace 仓库主 |
| is glm open source | 50 | 0 | $0 | 信息 | **GEO** | FAQ 前哨；Olares 文章/FAQ 段落必收 |
| is glm 5 open source | 50 | 0 | $0 | 信息 | **GEO** | GLM-5.2 MIT 开源，GEO 引用位 |
| what is glm ai | 70 | 0 | $0 | 信息 | **GEO** | 入门 FAQ，AI Overview 必争 |
| run glm locally | <10 | 0 | $0 | 信息 | **GEO** | Olares 教程核心句式，抢 AI 引用 |
| glm vs deepseek | 20 | 0 | $0 | 信息 | **GEO** | 比较前哨；Olares 可同时跑两者 |
| qwen alternative | 10 | 0 | $8.10 | 信息 | **GEO** | CPC 超高，近零量；GEO 占位，未来量可能增长 |

---

## 核心洞见

### 1. 品牌护城河

**不能正面刚品牌词**，但有可乘之隙。z.ai 已占领主要英文品牌词（"glm"、"glm-5"、"glm-4.7"等）；bigmodel.cn 在中文搜索中占统治地位但局限于华人社区。外部竞争者几乎没有与 Zhipu/GLM 的英文 organic 正面冲突——"chatglm"（14,800 vol，KD 45）、"codegeex"（1,000 vol）等产品词尚有机会写第三方内容文章占位，但 z.ai 会随品牌成熟逐步吃掉这些份额。**攻击面在模型评测/对比/自托管场景**，这些词 z.ai 自己并未系统布局。

### 2. 可复制的打法

- **版本发布博客模板**：z.ai 对每次模型迭代（4.5→4.6→4.7→5→5.2）都发一篇 `/blog/glm-X.X` 博文，轻松排名对应版本词（月量 720-5,400）。这个套路对 Olares 同样适用：每次 GLM 新版发布即发"How to run GLM-X.X on Olares with Ollama"。
- **产品订阅页 + 功能文档**：`/subscribe`（glm coding plan，1,900 vol，KD 25）、`/devpack/tool/claude`（z.ai claude code，1,600 vol，KD 33）双页面均排 #1，说明文档型内容 + 功能落地页策略有效。
- **工具集成词**：z.ai 因 Claude Code/OpenCode/Crush AI 集成，蹭到了 opencode（49,500 vol）、crush ai 等大词的流量——**集成热门开发工具的文档页是低成本流量放大器**。

### 3. 对 Olares 最关键的词

1. **"self hosted llm"**（320 vol，KD 22，$3.12 CPC）：Olares + Ollama + GLM-4-9B 是这个词最完整的答案，且 KD 极低。
2. **"chinese llm"**（390 vol，KD 19）：品类词，Olares 作为"运行所有中国开源 LLM 的个人云"叙事入口，KD 最低之一。
3. **"glm coding plan"**（1,900 vol，KD 25，$3.03 CPC）：付费订阅痛点词；Olares 叙事：GLM Coding Plan 订阅 vs 本地 Ollama-GLM 开发环境，$0/月。

### 4. 最大攻击面

- **定价/付费层痛点**：GLM Coding Plan 月付订阅（类 Cursor/GitHub Copilot 定价竞争），搜索词"is glm free"（260 vol，KD 22）、"glm api pricing"（40 vol，CPC $3.31）显示用户成本敏感。Olares 角度：GLM-4-9B 开源权重 + Ollama = 代码生成 $0/月。
- **中国云依赖风险**：bigmodel.cn/zhipuai.cn 是中国注册域名，对非中国用户有监管合规顾虑。"run glm locally"、"is glm open source"等词的信息意图背后有一批用户希望不依赖中国云端服务——Olares 完美覆盖。
- **"glm-4.5-air"超高 CPC（$5.49）**：说明有付费投放竞争，商业意图强；对比文"glm-4.5-air api vs local"有商业价值。

### 5. 隐藏低 KD 金矿

- **"glm api"（KD 18）**：量小（140 vol）但 KD 极低，"how to use GLM API locally with Ollama"类教程可稳健排名。
- **"deepseek alternative"（KD 12）**：全关键词中 KD 最低（12）且量 390，GLM 天然可作 DeepSeek 替代，一篇"Best DeepSeek Alternatives"文章可同时带 GLM + Olares 叙事。
- **"chinese llm"（KD 19）**：品类词 KD 19 属极低，"Best Chinese Open Source LLMs to Run Locally"是黄金内容题目。
- **"glm coding"（KD 29）** + **"glm coding plan"（KD 25）**：编程订阅类词 KD 低，但商业意图强（CPC $1.81-3.03），内容 + 对比文可切。
- **"cogvideox"（KD 38）**：GLM 开源视频模型，月下载量 >23 万，尚无强竞争者占位该词的对比/教程内容。

### 6. GEO 前瞻布局

以下词搜索量近零但语义精准，优先写入 FAQ 段落或文章前置问答，抢 AI Overview / Perplexity 引用位：

- `"is glm open source"` → 答：GLM-4-9B Apache 2.0，GLM-5.2 MIT，可 Ollama 运行
- `"run glm locally"` → 答：Ollama pull glm4 / Olares Market 安装 Ollama
- `"glm vs deepseek"` → 答：同为中国顶级开源 LLM；Olares 可同时部署两者对比
- `"what is glm ai"` → 答：Zhipu AI 的 GLM 系列，GLM = General Language Model，清华分拆公司
- `"is glm 5 open source"` → 答：GLM-5.2 MIT 协议，744B MoE；4-9B 版本更适合消费级硬件
- `"qwen alternative"` → 答：GLM 系列（尤其 GLM-4-9B）是 Qwen 的可信平替，均可 Ollama 部署

### 7. 与既有分析的关联

- **"self hosted llm"（KD 22）** 属于 `olares-500-keywords` 里自托管场景词簇的核心词，GLM-4-9B 作为中文表现最强的可本地运行 9B 模型，是该词最强的具体 use case 补充。
- **DeepSeek 系列**已有报告，GLM 可作为"也是中国开源 SOTA + 可 Ollama 部署"的姊妹叙事；"deepseek alternative"（KD 12）可在现有 DeepSeek 报告的对比文中带出 GLM 内容机会。
- **"chinese ai model"（KD 48）** 和 **"chinese llm"（KD 19）** 可共用一个内容簇，GLM、DeepSeek、Qwen 三家形成完整的"中国开源 LLM 可本地部署"话题群，Olares 作为统一部署平台。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_related、phrase_questions、phrase_fullsearch）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。zhipuai.cn US 月均有机流量 2,182（低于 3,000 阈值），已启用降级模式并以 bigmodel.cn + z.ai 数据补全。*
