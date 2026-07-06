# Alibaba Qwen SEO 竞品分析报告

> 域名：qwen.ai | SEMrush US | 2026-07-06
> Qwen = 阿里巴巴旗舰 LLM 系列（消费者聊天 + 开发者 API），兼具闭源旗舰与 Apache 2.0 开源两条轨道

---

## 项目理解（前置）

Qwen（通义千问）是阿里巴巴集团 Qwen Team 开发的大型语言模型与多模态模型系列，2023 年 4 月首发，目前已成为全球下载量最高的开源 LLM 系列之一。产品双轨并行：**消费者端** qwen.ai 提供免费聊天界面（对标 ChatGPT），**开发者端** 通过 Alibaba Cloud Model Studio 提供 OpenAI/Anthropic 兼容 API（按 token 计费）；**开源端** 在 HuggingFace/ModelScope 发布 Apache 2.0 开源权重，可本地自托管。Qwen3 系列是目前 Ollama 平台下载量最高的模型族之一（qwen3:8b 单 tag 超 3180 万下载），在 HuggingFace 排行榜上长期与 Meta Llama、Mistral 争夺开源 SOTA。对 Olares 而言，Qwen3 开源权重 + Ollama 是"在自己的硬件上跑世界级 LLM"的最直接案例。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 阿里巴巴旗舰 LLM 系列：闭源 API 对标 GPT-4o / Claude Opus，开源权重领先 Llama 3 |
| 开源 / 许可证 | 双轨：开源权重 Apache 2.0（Qwen3 系列全系可商用）；闭源旗舰（Max/Plus）API-only |
| 主仓库 | [github.com/QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)（★ ~27K）；[QwenLM/Qwen3.6](https://github.com/QwenLM/Qwen3.6)（★ ~3.6K） |
| 核心功能 | 文本生成与推理、多模态（视觉/音频/视频理解）、代码生成（QwenCoder 专用模型）、工具调用 / Agent、混合思维模式（thinking/non-thinking 单模型切换）、100+ 语言 |
| 商业模式 / 定价 | 聊天免费（qwen.ai）；API 按 token：Flash $0.05/$0.40 → Plus $0.40/$1.60 → Max $2.50/$7.50（per 1M tokens，in/out）；开源权重免费自托管 |
| 差异化 / 价值主张 | 1) 极致价格：Max 比 Claude Opus 4.8 便宜 ~7x；2) 开源 + 商用双路径；3) MoE 架构高效率（30B-A3B 激活仅 3B）；4) 最大 1M token 上下文；5) 混合 thinking 模式无需换模型 |
| 主要竞品（初判）| ChatGPT（OpenAI）、Claude（Anthropic）、Gemini（Google）、DeepSeek、Llama 3（Meta） |
| Olares Market | 未上架（qwen.ai 是闭源服务；Qwen3 开源权重可通过 Ollama app 在 Olares 运行） |
| 来源 | [wikipedia.org/wiki/Qwen](https://en.wikipedia.org/wiki/Qwen)、[qwen.readthedocs.io](https://qwen.readthedocs.io)、[ollama.com/library/qwen3](https://ollama.com/library/qwen3:8b)、[felloai.com/qwen-pricing/](https://felloai.com/qwen-pricing/)、[docs.qwencloud.com/pricing](https://docs.qwencloud.com/developer-guides/getting-started/pricing) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | qwen.ai |
| SEMrush Rank | **9,801**（全球前 1 万，与 lovable.dev 处于同一量级） |
| 自然关键词数 | 7,038 |
| 月自然流量（US）| **234,947** |
| 自然流量估值 | **$754,387/月** |
| 付费关键词数 | 0（无投放，依赖品牌自然流量） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 918 词 |
| 排名 4-10 位 | 992 词 |
| 排名 11-20 位 | 968 词 |

> qwenlm.ai（模型主页）几乎无 SEO 存在（Rank 6,836,107，月流量 18），全部 SEO 价值集中于 qwen.ai。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| qwen.ai（主站） | 5,286 | 191,541 | 81.53% |
| chat.qwen.ai | 1,635 | 42,447 | 18.07% |
| coder.qwen.ai | 111 | 958 | 0.41% |
| omni.qwen.ai | 6 | 1 | 0.00% |

> chat 子域贡献了 18% 的流量，表明用户频繁直接访问聊天入口；coder.qwen.ai 量级很小但有专属代码助手定位。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| qwen ai | 1 | 49,500 | 97 | $4.67 | 39,600 | 品牌 | / |
| qwen | 1 | 49,500 | 99 | $3.40 | 39,600 | 品牌 | / |
| qwen chat | 1 | 18,100 | 56 | $0.03 | 14,480 | 品牌/导航 | chat.qwen.ai/ |
| qwen ia | 1 | 6,600 | 69 | $4.67 | 5,280 | 品牌(西/葡语) | / |
| qween ai | 1 | 6,600 | 93 | $4.67 | 5,280 | 品牌(误拼) | / |
| qwen.ai | 1 | 6,600 | 94 | $4.67 | 5,280 | 导航 | / |
| qwenai | 1 | 5,400 | 66 | $4.67 | 4,320 | 品牌(误拼) | / |
| quen | 1 | 5,400 | 34 | $8.97 | 4,320 | 品牌(误拼，CPC 最高) | / |
| qwen 2.5 | 1 | 4,400 | 56 | $4.14 | 3,520 | 品牌/信息 | / |
| qwen3 | 1 | 12,100 | 64 | $3.78 | 3,000 | 品牌/信息 | / |
| qwen 3 | 1 | 3,600 | 76 | $3.78 | 2,880 | 品牌/信息 | / |
| qwen code | 1 | 3,600 | 50 | $6.52 | 2,880 | 产品 | /qwencode |
| qwen image edit | 1 | 3,600 | 62 | $0.91 | 2,880 | 产品/信息 | /blog?id=qwen-image-edit |
| qwan ai | 1 | 2,900 | 77 | $4.67 | 2,320 | 品牌(误拼) | / |
| chat.qwen.ia | 1 | 2,900 | 56 | $1.93 | 2,320 | 导航 | chat.qwen.ai/ |
| qwen edit | 1 | 2,400 | 63 | $1.30 | 1,920 | 产品 | /blog?id=qwen-image-edit |
| qwin ai | 1 | 2,400 | 50 | $4.67 | 1,920 | 品牌(误拼) | / |
| qianwen | 1 | 2,400 | 24 | $2.16 | 1,920 | 品牌(中文拼音) | / |
| qwenchat | 1 | 2,400 | 35 | $0.03 | 1,920 | 品牌/导航 | chat.qwen.ai/ |
| chat.qwen.ai | 1 | 1,900 | 65 | $1.93 | 1,520 | 导航 | chat.qwen.ai/ |
| qw | 2 | 18,100 | 32 | $14.82 | 1,484 | 品牌(缩写) | chat.qwen.ai/ |
| alibaba qwen | 1 | 1,600 | 82 | $0.00 | 1,280 | 品牌 | / |
| qwen api | 1 | 1,600 | 41 | $4.55 | 1,280 | 产品/商业 | /apiplatform |
| chat.qwen | 1 | 1,600 | 74 | $2.41 | 1,280 | 导航 | chat.qwen.ai/ |
| qwen image | 1 | 3,600 | 60 | $0.99 | 892 | 产品/信息 | /blog?id=qwen-image-edit |
| qwen-code | 1 | 3,600 | 46 | $6.52 | 892 | 产品 | /qwencode |
| qwen-vl | 1 | 3,600 | 43 | $2.89 | 892 | 产品/信息 | /blog?id=qwen-vl |
| 千问 api | 1 | 2,400 | 36 | $1.57 | 595 | 产品(中文) | /apiplatform |
| qwen coder | 1 | 2,400 | 53 | $6.10 | 595 | 产品 | coder.qwen.ai/ |
| qwen3-max | 1 | 2,900 | 51 | $3.26 | 719 | 产品/商业 | /blog?id=qwen3-max |
| qwen-image | 1 | 2,900 | 71 | $0.99 | 719 | 产品 | /blog?id=qwen-image-edit |
| qwen image 2 | 1 | 590 | 40 | $1.68 | 472 | 产品 | /blog?id=qwen-image-2.0 |
| qwen omni | 1 | 590 | 70 | $5.12 | 472 | 产品 | /blog?id=qwen3.5-omni |
| qwen3 ai | 1 | 590 | 73 | $4.67 | 472 | 品牌 | / |

> **关键观察**：① 前两大词（qwen ai / qwen，月量各 49,500）KD 双 99/97，几乎不可能正面竞争；② 误拼变体极多（qween/qwan/qwin/quen/qwenai…），均排名第 1，Qwen 对自己品牌词的控制力极强；③ qw 排名第 2、月量 18,100，是高价值暗流（CPC $14.82）；④ `qwen code` / `qwen coder` / `qwen-vl` 等产品页均落 1 位；⑤ `千问 api` 中文词排名第 1，揭示中国开发者流量不容忽视。

### 付费词（Google Ads，按流量排序）

Qwen 无任何付费投放，完全依赖自然搜索。主要竞品 ChatGPT 在此关键词（`qwen alternative`、`qwen vs chatgpt` CPC $48.62）上有潜在竞价空间，Qwen 并未在此阻击。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| chatgpt alternative | 18,100 | 47 | $1.31 | 信息 | 最大品类竞争词 |
| chatgpt alternative free | 2,400 | 57 | $1.25 | 商业 | 强免费意图 |
| open source llm | 2,400 | 42 | $3.30 | 信息 | 大品类 |
| deepseek alternative | 390 | 12 | $3.27 | 信息 | ⭐ 竞品替代 |
| chinese llm | 390 | 19 | $3.14 | 信息 | ⭐ 品类定义词 |
| ollama alternative | 210 | 16 | $4.30 | 信息 | ⭐ 运行时竞品 |
| deepseek vs qwen | 210 | 25 | $0 | 信息/商业 | ⭐ 中国 AI 对比 |
| qwen vs chatgpt | 140 | 20 | $48.62 | 信息/商业 | ⭐ 最高 CPC！ |
| best open source llm 2026 | 110 | 21 | $3.31 | 商业 | ⭐ 年份型机会 |
| open source chatgpt alternative | 30 | 19 | $2.34 | 信息/商业 | ⭐ |
| qwen vs claude | 40 | 10 | $0 | 信息/商业 | ⭐ 超低 KD |
| qwen vs llama | 260 | 16 | $0 | 信息/商业 | ⭐ |
| qwen alternative | 10 | 0 | $8.10 | 商业 | ⭐ 零 KD，高 CPC |
| best chinese ai model | 20 | 0 | $0 | 商业 | ⭐ GEO |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| ollama models | 14,800 | 63 | $5.27 | 信息/商业 | 巨大但高难度 |
| chinese ai | 9,900 | 50 | $1.87 | 信息 | 地缘政治话题 |
| local llm | 2,900 | 39 | $5.37 | 信息 | Olares 核心词 |
| run llm locally | 590 | 47 | $3.50 | 信息 | 教程型 |
| alibaba ai model | 720 | 44 | $2.82 | 信息 | 品牌+品类 |
| best local llm | 720 | 23 | $4.59 | 商业 | ⭐ 榜单型机会 |
| private ai assistant | 320 | 50 | $4.87 | 信息/商业 | 隐私场景 |
| self hosted llm | 320 | 22 | $3.12 | 信息 | ⭐ Olares 核心 |
| local ai chat | 140 | 54 | $3.44 | 信息 | 使用场景 |
| llm local | 140 | 33 | $6.20 | 信息 | |
| tongyi qianwen | 260 | 82 | $3.19 | 品牌 | 中文用户群 |
| 通义千问 | 4,400 | 53 | $0.83 | 品牌 | 中文大词 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| qwen3 | 14,800 | 64 | $0 | 信息 | 最大非品牌产品词 |
| qwen chat | 14,800 | 89 | $0.02 | 品牌/导航 | 高 KD，品牌护城河 |
| qwen coder / qwen code | 2,400–3,600 | 46–56 | $5.83 | 产品 | 代码专用模型 |
| qwen3 coder | 2,900 | 56 | $5.57 | 产品 | 含版本号 |
| qwen3-vl / qwen3 vl | 1,600–2,900 | 52–54 | $4.86 | 产品 | 视觉语言模型 |
| qwen3 0.6b | 1,600 | 52 | $0 | 产品/信息 | 超小端侧模型 |
| qwen3-32b | 1,300–2,400 | 22–39 | $9.77 | 产品/信息 | ⭐ 旗舰开源尺寸 |
| qwen api | 1,600 | 41 | $4.55 | 产品/商业 | 开发者入口 |
| qwen3 8b | 1,000 | 48 | $5.85 | 产品/信息 | 最受欢迎 Ollama 尺寸 |
| qwen3 omni | 720 | 46 | $2.06 | 产品 | 全模态新品 |
| qwen api key | 320 | **4** | $4.80 | 信息 | ⭐ 极低 KD！ |
| qwen3 30b | 260 | 41 | $1.95 | 产品/信息 | MoE 版本 |
| qwen3 14b | 320 | 34 | $7.63 | 产品/信息 | 中端自托管 |
| qwen pricing | 170 | 49 | $5.14 | 商业 | 商业化意图 |
| qwen3 moe | 170 | 25 | $0 | 信息 | ⭐ |
| qwen3 1.7b | 390 | 22 | $0 | 信息 | ⭐ 端侧 |
| qwen3 4b | 590 | 31 | $1.37 | 信息 | ⭐ |
| qwen3 235b | 320 | 43 | $1.11 | 产品/商业 | 最大 MoE 旗舰 |
| qwen3 thinking | 140 | 67 | $0 | 信息 | 混合思维模式 |
| qwen multimodal | 110 | 68 | $0 | 信息 | |
| qwen vs deepseek | 210 | **7** | $0 | 信息/商业 | ⭐ 超低 KD，中国 AI 对比 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| ollama qwen3 | 590 | 48 | $4.16 | 信息/商业 | 主力工作流词 |
| qwen3 ollama | 260 | 48 | $0 | 信息/商业 | 同意图变体 |
| how to run qwen locally | 50 | 0 | $4.73 | 信息 | ⭐ 教程词 |
| run qwen locally | 50 | 0 | $5.48 | 信息 | ⭐ GEO 级 |
| is qwen open source | 140 | 51 | $0 | 信息 | 高频认知问题 |
| qwen self hosted | 40 | 0 | $0 | 信息 | ⭐ GEO 级 |
| qwen open source | 110 | 73 | $6.54 | 信息 | 高 KD |
| qwen3 local | 20 | 0 | $0 | 信息 | ⭐ GEO 级 |
| run qwen3 locally | 20 | 0 | $0 | 信息 | ⭐ GEO 级 |
| qwen3 8b ollama | 20 | 0 | $0 | 信息 | ⭐ 超精准 |
| qwen 3 uncensored | 4,400 | 24 | $0 | 信息 | ⭐ 超大量！开源去审查需求 |
| qwen3 uncensored | 40 | 22 | $0 | 信息 | ⭐ 含版本号变体 |
| is qwen3 censored | 40 | 0 | $0 | 信息 | ⭐ GEO 级认知问题 |
| how to run qwen3 locally | 20 | 0 | $0 | 信息 | ⭐ 精准教程 |
| qwen3 on mac | — | — | — | 信息 | GEO 前哨 |
| self hosted llm | 320 | 22 | $3.12 | 信息 | ⭐ 品类前哨 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Qwen3 开源权重（Apache 2.0）通过 Ollama 在 Olares 上运行，是"把世界级 LLM 跑在自己家里"的最直接切入——数据不出家门、无 token 费用、随时可用。qwen3:8b 在 Ollama 的 3180 万下载量意味着巨大的教程需求人群。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| qwen 3 uncensored | 4,400 | 24 | $0 | 开源 Qwen3 在 Olares+Ollama 本地运行，无任何中央审查，数据不经第三方服务器 | ⭐⭐⭐ |
| ollama qwen3 | 590 | 48 | $4.16 | Ollama 已在 Olares Market，`ollama run qwen3:8b` 是安装后第一条命令 | ⭐⭐⭐ |
| run llm locally | 590 | 47 | $3.50 | Olares+Ollama 是"在本地跑 LLM"的完整解决方案（OS+推理引擎+模型一体） | ⭐⭐⭐ |
| self hosted llm | 320 | 22 | $3.12 | Olares 核心价值：自托管 LLM 不依赖任何云服务 | ⭐⭐⭐ |
| qwen3 ollama | 260 | 48 | $0 | 同 ollama qwen3，内容可合并或互为变体 | ⭐⭐⭐ |
| qwen vs deepseek | 210 | 7 | $0 | Olares 同时支持 Qwen3 和 DeepSeek 两个模型 —— "在 Olares 上自选，不被平台绑定" | ⭐⭐⭐ |
| qwen vs llama | 260 | 16 | $0 | 同上，Olares 是多模型统一运行平台，不需要选边站 | ⭐⭐⭐ |
| local llm | 2,900 | 39 | $5.37 | 品类大词，Olares 是"local LLM 的家用服务器 OS" | ⭐⭐ |
| best local llm | 720 | 23 | $4.59 | 榜单文章可嵌入"如何在 Olares 上运行这些本地 LLM" | ⭐⭐ |
| private ai assistant | 320 | 50 | $4.87 | Olares AI 叙事：你的个人 AI，跑在自己的硬件，永不离家 | ⭐⭐ |
| deepseek alternative | 390 | 12 | $3.27 | Qwen3 是 DeepSeek 的开源替代，都可在 Olares 运行 | ⭐⭐ |
| how to run qwen locally | 50 | 0 | $4.73 | 教程词：Olares+Ollama step-by-step 教程的最直接锚词 | ⭐⭐⭐ |
| qwen self hosted | 40 | 0 | $0 | Olares 自托管平台，Qwen3 开源权重，一句话命中 | ⭐⭐⭐ |
| run qwen locally | 50 | 0 | $5.48 | 同上，略带教程意图 | ⭐⭐⭐ |
| qwen3 local | 20 | 0 | $0 | 零 KD，抢引用位 | ⭐⭐ |
| qwen api key | 320 | 4 | $4.80 | API key 疲劳 → Olares 本地 Ollama API 替代方案 | ⭐⭐ |
| is qwen open source | 140 | 51 | $0 | 认知问题，答案=Qwen3 Apache 2.0，Olares 提供零配置自托管 | ⭐⭐ |
| ollama alternative | 210 | 16 | $4.30 | Olares 中的 Ollama 相当于"Ollama 的官方家用形态"（非替代，而是集成） | ⭐⭐ |
| open source chatgpt alternative | 30 | 19 | $2.34 | Qwen3+Ollama+Olares = 完整的 ChatGPT 开源本地替代链 | ⭐⭐⭐ |
| chinese llm | 390 | 19 | $3.14 | 对关注数据主权的用户：Qwen3 开源权重跑在自家 Olares，数据不出户 | ⭐⭐ |
| 通义千问 | 4,400 | 53 | $0.83 | 中文用户群：Olares 在中国市场是"在自己硬件跑通义千问"的最直接产品 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| qwen 3 uncensored | 4,400 | 24 | $0 | 信息 | **主词候选** | KD 24 量 4400，稀有低难高量组合；Olares 叙事：Qwen3 本地运行 = 无审查，强力文章切入 |
| self hosted llm | 320 | 22 | $3.12 | 信息 | **主词候选** | KD 22 量 320，Olares 核心场景词，撑教程/榜单类内容 |
| best local llm | 720 | 23 | $4.59 | 商业 | **主词候选** | KD 23 量 720，榜单文内嵌 Olares+Qwen3 配置指南 |
| qwen vs chatgpt | 140 | 20 | $48.62 | 信息/商业 | **主词候选** | KD 20 量 140，$48 CPC 揭示超高商业价值；Olares 可插入"两者都不用订阅费的方案" |
| qwen vs deepseek | 210 | 7 | $0 | 信息/商业 | **主词候选** | KD 7！量 210，极易排名；Olares = 两者都运行，不必选边 |
| qwen vs llama | 260 | 16 | $0 | 信息/商业 | **主词候选** | KD 16 量 260，对比内容中引导"在 Olares 上同时跑两个" |
| deepseek alternative | 390 | 12 | $3.27 | 信息 | **主词候选** | KD 12 量 390，Qwen3 是 DeepSeek 的开源替代，均可在 Olares 运行 |
| ollama qwen3 | 590 | 48 | $4.16 | 信息/商业 | **主词候选** | 量 590，Olares+Ollama 工作流最精准词，虽 KD 48 但场景极度契合 |
| chinese llm | 390 | 19 | $3.14 | 信息 | **主词候选** | KD 19 量 390，Olares 叙事：中国 AI 模型 + 数据主权自托管 |
| best open source llm 2026 | 110 | 21 | $3.31 | 商业 | **主词候选** | 含年份 KD 21，年度内容机会，Qwen3 必进榜单 + Olares 运行指南 |
| open source chatgpt alternative | 30 | 19 | $2.34 | 信息/商业 | **主词候选** | KD 19，Qwen3+Ollama+Olares 是完整本地替代链 |
| qwen api key | 320 | **4** | $4.80 | 信息 | **主词候选** | KD 仅 4！API key 获取教程 → 引导至 Olares 本地 Ollama API（永不过期）|
| run llm locally | 590 | 47 | $3.50 | 信息 | **主词候选** | 量 590，Olares 是"local LLM OS"的直接落地 |
| qwen3 ollama | 260 | 48 | $0 | 信息/商业 | 次级 | 与 ollama qwen3 并入同篇 |
| qwen3 32b | 1,300 | 22 | $9.77 | 信息 | 次级 | KD 22 量 1300，偏信息/规格，并入 qwen3 尺寸评测文 |
| qwen3 14b | 320 | 34 | $7.63 | 信息 | 次级 | 同上，中端自托管尺寸 |
| qwen3 8b | 1,000 | 48 | $5.85 | 信息 | 次级 | Ollama 最多下载尺寸，并入 qwen3 ollama 教程文 |
| qwen3 4b | 590 | 31 | $1.37 | 信息 | 次级 | |
| qwen3 1.7b | 390 | 22 | $0 | 信息 | 次级 | ⭐ KD 22，轻量端侧尺寸 |
| qwen3 moe | 170 | 25 | $0 | 信息 | 次级 | ⭐ MoE 架构文章次级词 |
| deepseek vs qwen | 210 | 25 | $0 | 信息/商业 | 次级 | 并入 qwen vs deepseek 文章 |
| qwen self hosted | 40 | 0 | $0 | 信息 | 次级 | ⭐ 零 KD，并入自托管教程 |
| run qwen locally | 50 | 0 | $5.48 | 信息 | 次级 | ⭐ 并入教程 |
| ollama alternative | 210 | 16 | $4.30 | 信息 | 次级 | ⭐ 并入 Olares+Ollama 介绍文 |
| how to run qwen locally | 50 | 0 | $4.73 | 信息 | **GEO** | ⭐ 零 KD 教程问题，抢 AI Overview |
| qwen3 local | 20 | 0 | $0 | 信息 | **GEO** | ⭐ 零 KD，抢引用位 |
| run qwen3 locally | 20 | 0 | $0 | 信息 | **GEO** | ⭐ 零 KD，抢引用位 |
| is qwen open source | 140 | 51 | $0 | 信息 | **GEO** | 认知问题，FAQ 段抢 AI Overview |
| is qwen3 censored | 40 | 0 | $0 | 信息 | **GEO** | 零 KD，本地运行=无审查，精准切入 |
| how to run qwen3 locally | 20 | 0 | $0 | 信息 | **GEO** | 零 KD 精准教程问题 |
| qwen3 on mac | ~10 | — | — | 信息 | **GEO** | Olares 跨平台（macOS 支持），补充引用段 |
| self hosted ai assistant | 20 | 0 | $4.37 | 信息/商业 | **GEO** | ⭐ 零 KD，Olares 个人 AI 叙事 |

---

## 核心洞见

### 1. 品牌护城河（品牌词心智）——能否正面刚？

**Qwen 品牌词铁桶**，不可正面竞争。核心词（qwen / qwen ai / qwen chat）KD 97–99，Qwen 官方自己排名第 1，其他域名不存在入局可能。误拼变体同样全被收割（20+ 个变体均 #1）。**战略结论：完全回避品牌词，从开源/本地/对比切入。**

### 2. 可复制的打法

- **博客页带流量**：`/blog?id=qwen-image-edit` 等产品博客页直接吸走了 `qwen image edit`（3600 量）等词的流量，产品公告即内容。
- **多语言+误拼变体全覆盖**：`qwen ia`（西班牙语拼写）、`chat.qwen.ia`、`qianwen`、`千问 api` 等均排第 1，说明 Qwen 刻意做了多语言 SEO 覆盖。
- **产品专页**：/qwencode、chat.qwen.ai、coder.qwen.ai 等子产品独立子域/路径，分别收割 code、chat 意图流量。
- **无付费投放**：全靠自然 + 品牌认知，说明品牌势能已足够强。Olares 可趁此填补对比词的付费/内容空缺。

### 3. 对 Olares 最关键的词

1. **`qwen 3 uncensored`（4,400 量，KD 24）**——单词量最大的低 KD 机会；本地运行 = 无审查是最有力的 Olares 叙事，且量级罕见。
2. **`ollama qwen3` / `qwen3 ollama`（260+590 量）**——最精准的 Olares+Ollama 工作流词，教程内容直接可排名。
3. **`self hosted llm`（320 量，KD 22）**——品类级低 KD 词，Olares 核心场景，SEO 和 GEO 双通道均有价值。

### 4. 最大攻击面（痛点词）

- **审查问题**：`qwen 3 uncensored`（4400 量，KD 24）是最大量的低 KD 词，直击 Qwen 官方服务的核心限制。本地运行 Qwen3 = 无任何中央内容过滤。
- **API 费用**：`qwen api pricing`（170 量）、`qwen pricing`（170 量）揭示 API cost 是用户决策点；Olares 本地 Ollama = 零 token 费用，长期成本为 0。
- **数据隐私**：`is qwen ai safe`、`private ai assistant` 等问题词显示用户对数据传输的顾虑；本地运行彻底解决。
- **API key 烦恼**：`qwen api key`（320 量，KD 4）— 极低 KD，引导用户从"需要 API key"迁移到"本地 Ollama API 永不过期"。

### 5. 隐藏低 KD 金矿

| 词 | 量 | KD | 说明 |
|----|----|----|------|
| qwen api key | 320 | 4 | 极低！API 入门教程 → 引导本地化 |
| qwen vs deepseek | 210 | 7 | 对比文超易排名 |
| qwen vs claude | 40 | 10 | KD 10，CPC 0，但商业意图明确 |
| deepseek alternative | 390 | 12 | 宽品类词，Qwen3/Olares 可竞争 |
| ollama alternative | 210 | 16 | Olares 实际上是 Ollama 的最佳宿主 |
| qwen vs llama | 260 | 16 | KD 16，对比文强场景 |
| chinese llm | 390 | 19 | KD 19，品类定义词 |
| open source chatgpt alternative | 30 | 19 | 完美 Olares 叙事切入 |

### 6. GEO 前瞻布局（近零量但语义精准，抢 AI Overview/Perplexity 引用位）

- `how to run qwen3 locally`（20 量，KD 0）
- `is qwen3 censored`（40 量，KD 0）
- `qwen self hosted`（40 量，KD 0）
- `self hosted ai assistant`（20 量，KD 0，CPC $4.37）
- `qwen3 on mac`（~10 量）— Olares macOS 支持场景
- `how to deploy ollama qwen3-vl`（10 量）
- `how to disable thinking in qwen3.5 ollama`（10 量）— 超精准教程
- `can i run qwen3 locally`（10 量，KD 0）

这些均应进入教程文章的 FAQ 段 / 结构化数据，零成本抢 AI 引用位。

### 7. 与既有 `olares-500-keywords` 词表的关联/补充

既有词表中 Qwen 相关词**仅一条**：`ollama qwen`（未给量/KD 数据，标为 A 级机会）。本次报告大幅补充：

- 新增 10+ 个主词候选（qwen 3 uncensored、self hosted llm、qwen vs deepseek 等）
- 新增 20+ 个次级/GEO 词（尤其是教程问题词族）
- 补充了中文词群（通义千问 4400 量、千问 api 2400 量），既有词表未覆盖
- `qwen api key`（KD 4，量 320）是词表中未出现的极高价值词

---

*数据来源：SEMrush US 数据库（domain_rank、domain_organic_subdomains、resource_organic、domain_organic_organic、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
