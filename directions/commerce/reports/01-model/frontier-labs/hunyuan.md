# Tencent Hunyuan SEO 竞品分析报告

> 域名：hunyuan.tencent.com | SEMrush US | 2026-07-06
> 腾讯旗舰多模态 AI 平台，覆盖文本/视频/图像/3D 生成，对外侧重 API 商业化，核心开源资产是 HunyuanVideo（视频生成，GitHub 12K+ stars）。

---

## 项目理解（前置）

Tencent Hunyuan（混元）是腾讯自研 AI 大模型家族，2023 年底正式对外，覆盖 LLM（Hy3 Preview，295B/21B MoE，256K context）、视频生成（HunyuanVideo / 1.5）、图像（HunyuanImage 3.0，80B/13B active）、3D（Hunyuan3D-2.5）、翻译（HunyuanTranslation，支持 33 语言）五大模态。Hy3 Preview 已于 2026 年开源，支持 vLLM/SGLang 推理，并入腾讯元宝（Yuanbao）、QQ、企业微信等产品线。SEO 重心落在 **HunyuanVideo**——视频生成开源权重（GitHub 12.1K+ stars）触发了大量英文检索流量；3D 生成子站（3d.hunyuan.tencent.com）为当前流量第一来源。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 腾讯旗舰多模态 AI 平台：LLM + 视频/图像/3D 生成，面向企业 API + 开发者开源 |
| 开源 / 许可证 | 混元系列部分开源：Hy3 Preview（Apache-ish）；HunyuanVideo 13B & 1.5（NOASSERTION，商用需申请）；Hunyuan3D-2（Tencent Hunyuan License，非 Apache） |
| 主仓库 | [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)（★12.1K，2024-11-28 创建，2026-06 更新）；[HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)（★4.5K） |
| 核心功能 | ① Hy3 LLM API（推理/Agent）；② HunyuanVideo T2V/I2V（720p→1080p，8.3B 可本地跑）；③ HunyuanImage 图像生成；④ Hunyuan3D 模型生成（商业级）；⑤ HunyuanTranslation 33语言翻译 |
| 商业模式 / 定价 | 腾讯云 API 按 token 计费（Hy3 系列通过 TokenHub 提供）；HunyuanVideo 开源权重免费自部署，商业使用需独立协议；3D API 首 20 次免费 |
| 差异化 / 价值主张 | 腾讯生态深度绑定（QQ/游戏/企业微信）；HunyuanVideo-1.5（8.3B）是少数可在消费级 GPU（14GB+ VRAM）本地运行的高质量视频模型；Hunyuan3D-2.5 3D 生成业界一流 |
| 主要竞品（初判）| Kling AI（视频）、WAN 2.1（开源视频）、Runway（闭源视频）、LTX Video（开源视频）、OpenAI Sora；LLM 侧竞品：DeepSeek、Qwen、Gemini |
| Olares Market | 已上架 Hunyuan3D（[报告](../../../market/reports/hunyuan3d.md)）；HunyuanVideo 未单独上架（但 ComfyUI on Olares 可跑其权重） |
| 来源 | [官网](https://hunyuan.tencent.com)、[Tencent 发布页](https://www.tencent.com/en-us/articles/2202320.html)、[GitHub HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo)、[HF tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5) |

---

## 流量基线（Phase 1）

> **注**：hunyuan.tencent.com 是腾讯子域名生态，SEMrush 按子域分别计算，本报告以"hunyuan.tencent.com 生态（含所有 *.hunyuan.tencent.com 子站）"为统计范围，合并流量约 ~23,500/月（US）。主站 hunyuan.tencent.com 无 Google Ads 投放。中文词（混元、腾讯混元等）在 US 数据库中仍有数千月量，说明海外华人群体构成重要受众。

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | hunyuan.tencent.com（生态） |
| SEMrush Rank | N/A（子域名，父域 tencent.com 归入 SEMrush 大类） |
| 自然关键词数（主域） | 1,356 |
| 月自然流量（US，生态合计） | ~23,785 |
| 自然流量估值 | ~$24,287/月 |
| 付费关键词数 | 0（无 Google Ads） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 156 词 |
| 排名 4-10 位 | 170 词 |
| 排名 11-20 位 | 137 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| 3d.hunyuan.tencent.com | 227 | 8,564 | 36% |
| hunyuan.tencent.com | 381 | 7,325 | 31% |
| 3d-models.hunyuan.tencent.com | 314 | 4,139 | 17% |
| aivideo.hunyuan.tencent.com | 304 | 3,188 | 13% |
| video.hunyuan.tencent.com | 50 | 276 | 1% |
| 其他子域 | — | ~293 | ~1% |

> **洞察**：3D 生成子站贡献最大流量（36%），视频生成仅占 13%——但"HunyuanVideo"品牌词在 US 月量 2,900 且有大量技术社区长尾流量，搜索需求被 GitHub/Reddit/教程站大量截流，视频方向的真实搜索需求远超 aivideo 子站实际承接的流量。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| hunyuan | 1 | 5,400 | 72 | $0.75 | 4,320 | 品牌 | hunyuan.tencent.com/ |
| 混元3d | 1 | 3,600 | 76 | $1.24 | 2,880 | 品牌（中） | 3d.hunyuan.tencent.com/ |
| 腾讯混元3d | 1 | 2,400 | 62 | $1.18 | 1,920 | 品牌（中） | 3d.hunyuan.tencent.com/ |
| hunyuan 3d | 1 | 2,400 | 34 | $1.57 | 1,920 | 品牌/产品 | 3d-models.hunyuan.tencent.com/ |
| hunyuan tencent | 1 | 1,000 | 52 | $1.53 | 800 | 品牌 | hunyuan.tencent.com/ |
| 3d.hunyuan.tencent | 2 | 3,600 | 55 | $1.87 | 475 | 导航 | 3d.hunyuan.tencent.com/ |
| video.hunyuan.tencent | 1 | 1,600 | 65 | $0.56 | 396 | 导航 | aivideo.hunyuan.tencent.com/ |
| 混元ai | 1 | 1,600 | 10 | $0 | 396 | 品牌（中）⭐ | 3d.hunyuan.tencent.com/ |
| hunyuan 3d 2.5 | 1 | 1,600 | 56 | $1.84 | 396 | 产品 | 3d.hunyuan.tencent.com/ |
| 混元 | 1 | 2,900 | 33 | $0 | 382 | 品牌（中）⭐ | 3d.hunyuan.tencent.com/ |
| tencent hunyuan ai video | 1 | 390 | 62 | $0.99 | 312 | 信息 | aivideo.hunyuan.tencent.com/ |
| tencent hunyuan 3d | 1 | 320 | 42 | $1.31 | 256 | 产品 | 3d-models.hunyuan.tencent.com/ |
| 腾讯混元 | 2 | 1,900 | 40 | $0 | 250 | 品牌（中） | 3d.hunyuan.tencent.com/ |
| hunyuan-a13b | 1 | 1,000 | 33 | $0 | 248 | 产品⭐ | hunyuan.tencent.com/?model=hunyuan-a13b |
| hunyuan video | 3 | 2,900 | 65 | $0.87 | 188 | 信息/产品 | aivideo.hunyuan.tencent.com/ |
| tencent hunyuan | 2 | 1,300 | 50 | $0.85 | 171 | 品牌 | aivideo.hunyuan.tencent.com/ |
| hunyuan-3d | 1 | 590 | 29 | $1.57 | 146 | 产品⭐ | 3d-models.hunyuan.tencent.com/ |
| tencent ai | 2 | 720 | 26 | $4.55 | 95 | 信息/商业⭐ | aivideo.hunyuan.tencent.com/ |
| 元宝 | 8 | 14,800 | 50 | $0 | 88 | 品牌（中） | hunyuan.tencent.com/bot/chat |
| 腾讯元宝 | 7 | 14,800 | 47 | $0 | 88 | 品牌（中） | hunyuan.tencent.com/bot/chat |

### 付费词（Google Ads）

hunyuan.tencent.com **无 Google Ads 投放**，US 付费流量为 0。腾讯当前不在美国市场做 SEM 竞价，主要依赖自然品牌词流量。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| sora | 1,000,000 | 87 | $1.89 | 品牌/导航 | 超级大词，品牌护城河极深 |
| kling ai | 90,500 | 67 | $1.34 | 品牌 | 快手 Kling，最强视频品牌词 |
| runway ml | 18,100 | 70 | $1.71 | 品牌 | 闭源视频主流竞品 |
| text to video ai | 8,100 | 78 | $1.35 | 信息 | 品类入口词，KD 高 |
| open-sora | 2,900 | 61 | $1.66 | 品牌 | 开源 Sora 替代品 |
| hunyuan video | 2,900 | 65 | $0.87 | 信息 | 核心产品词（主站排名第 3） |
| cogvideox | 2,400 | 38 | $0.78 | 品牌⭐ | 清华开源视频模型，KD 适中 |
| ltx video | 2,400 | 31 | $1.51 | 品牌⭐ | 开源视频模型，KD 低 |
| wan video | 3,600 | 74 | $0.72 | 品牌 | 万象/WAN 系列 |
| wan2.1 | 1,300 | 57 | $0.82 | 品牌 | WAN 2.1 具体版本 |
| sora alternative | 210 | 11 | $1.09 | 商业⭐ | 寻找替代方案，KD 低 |
| hunyuan vs wan2.1 | 260 | 10 | $0 | 信息⭐⭐ | 极低 KD 对比词，直接机会 |
| kling alternative | 20 | 0 | $2.31 | 商业⭐ | 低量但高商业意图，GEO 前哨 |
| runway alternative | 10 | 0 | $3.39 | 商业⭐ | 低量但 CPC 高，GEO 前哨 |
| wan video alternative | 10 | 0 | $0 | 信息⭐ | GEO 前哨 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai video generator | 165,000 | 92 | $1.27 | 商业 | 品类超级词，KD=92 无法硬攻 |
| video generation ai | 880 | 75 | $1.87 | 信息 | 品类词变体 |
| chinese ai video generator | 390 | 33 | $0.96 | 信息⭐ | 地理标签品类词，可竞争 |
| chinese image to video ai | 720 | 26 | $0.86 | 信息⭐ | 图生视频，中国 AI 角度，KD 低 |
| chinese ai open source | 390 | 44 | $0 | 信息 | 开源中国 AI 品类词 |
| chinese ai model | 1,300 | 48 | $1.83 | 信息 | 中国 AI 模型品类词 |
| open source video generation | 30 | 24 | $1.65 | 信息⭐ | 低量但 KD 低，自托管需求 |
| ai video generator open source | 30 | 15 | $1.40 | 信息⭐ | 开源意图品类词，KD=15 |
| open source ai video | 40 | 24 | $1.23 | 信息⭐ | 开源信号词 |
| self hosted ai video generator | 40 | 46 | $1.29 | 商业 | 自托管意图词 |
| digital human | 880 | 41 | $2.28 | 信息/商业 | 数字人品类词，HunyuanAvatar 相关 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| hunyuan | 5,400 | 66 | $0.75 | 品牌 | 主品牌词 |
| hunyuanvideo | 1,900 | 61 | $0.81 | 品牌/产品 | 品牌+产品合写 |
| hunyuan video 1.5 | 720 | 47 | $1.62 | 产品 | 具体版本号 |
| hunyuan video ai | 720 | 55 | $0.97 | 信息 | 品牌+功能词 |
| hunyuan image to video | 720 | 56 | $0.98 | 产品 | I2V 功能词 |
| hunyuan video gguf | 590 | 28 | $0 | 信息⭐ | 量化版本，本地部署信号 |
| hunyuan video avatar | 320 | 34 | $1.07 | 产品⭐ | 数字人功能词 |
| hunyuan 3d | 1,900 | 61 | $1.53 | 产品 | 3D 生成核心词 |
| hunyuan 3d 2.5 | 1,600 | 56 | $1.84 | 产品 | 最新版本号 |
| hunyuan-a13b | 1,000 | 33 | $0 | 产品⭐ | LLM 具体型号，KD 低 |
| tencent ai | 720 | 26 | $4.55 | 信息/商业⭐ | 高 CPC 商业意图，KD=26 |
| hunyuan video comfyui | 260 | 32 | $0 | 信息⭐ | ComfyUI 集成安装词 |
| hunyuan video gguf | 590 | 28 | $0 | 信息⭐ | 量化部署词 |
| hunyuan vs wan2.1 | 260 | 10 | $0 | 信息⭐⭐ | 极低 KD 对比词 |
| tencent hunyuan ai video | 390 | 62 | $0.99 | 信息 | 品牌+产品组合词 |
| hunyuan video foley | 90 | 0 | $0 | 信息⭐ | 音频生成功能词，GEO 前哨 |
| hunyuan video lora training | 50 | 29 | $0 | 信息⭐ | LoRA 训练词，开发者需求 |
| hunyuan video prompts | 90 | 17 | $0 | 信息⭐ | Prompt 优化词，KD=17 |
| hunyuanvideo-1.5 | 880 | 45 | $0.85 | 产品 | 版本变体 |
| hunyuan video model | 70 | 55 | $1.89 | 信息 | 模型技术词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| hunyuan video gguf | 590 | 28 | $0 | 信息⭐ | GGUF 量化，本地部署核心词 |
| hunyuan video comfyui | 260 | 32 | $0 | 信息⭐ | ComfyUI 集成，安装教程词 |
| hunyuan vs wan2.1 | 260 | 10 | $0 | 信息⭐⭐ | 开源模型对比，KD 极低 |
| hunyuan_video_vae_bf16.safetensors | 880 | 17 | $0 | 信息⭐ | 模型权重文件名，安装导向 |
| llava_llama3_fp8_scaled.safetensors | 1,300 | 27 | $0 | 信息⭐ | safetensors 安装词（相关流量） |
| ai video generator open source | 30 | 15 | $1.40 | 信息⭐ | 开源意图明确，KD=15 |
| open source video generation | 30 | 24 | $1.65 | 信息⭐ | 开源品类词 |
| chinese ai video generator free | 320 | 22 | $0.67 | 信息⭐ | 免费+中国 AI，KD=22 |
| hunyuan video local | 40 | 27 | $0 | 信息⭐ | 本地部署意图 |
| hunyuan video lora training | 50 | 29 | $0 | 信息⭐ | 开发者 fine-tune |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：HunyuanVideo 权重已开源并支持 ComfyUI，而 ComfyUI 可通过 Olares Market 一键部署，形成"Olares → ComfyUI → HunyuanVideo 1.5"完整链路；同时 Hy3 LLM 可通过 Ollama（Olares Market 已上架）调用兼容格式权重，构成文本+视频双 AI 栈。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| hunyuan video gguf | 590 | 28 | $0 | ⭐⭐⭐ GGUF 即 Ollama/ComfyUI 可直接加载，Olares 教程：下载 GGUF 权重 → ComfyUI workflow 跑 HunyuanVideo 1.5 |
| hunyuan video comfyui | 260 | 32 | $0 | ⭐⭐⭐ 核心安装词；Olares Market 装 ComfyUI → 配置 HunyuanVideo 节点，端到端一键教程机会 |
| hunyuan vs wan2.1 | 260 | 10 | $0 | ⭐⭐⭐ KD=10 极低；Olares 可同时跑两个开源视频模型，对比文直接写"Olares One 上跑 HunyuanVideo 1.5 vs WAN 2.1" |
| tencent ai | 720 | 26 | $4.55 | ⭐⭐⭐ KD=26+CPC=$4.55，商业意图；可写"自托管 Tencent AI 模型在 Olares 上"切入企业用户 |
| chinese ai video generator free | 320 | 22 | $0.67 | ⭐⭐⭐ 免费+开源意图；Olares 上运行 HunyuanVideo 1.5 = 本地免费中国 AI 视频生成 |
| sora alternative | 210 | 11 | $1.09 | ⭐⭐ KD=11；Olares 一键 ComfyUI + HunyuanVideo = 开源 Sora 替代方案 |
| open source ai video | 40 | 24 | $1.23 | ⭐⭐ 开源意图词；可并入开源视频生成总索引文章 |
| ai video generator open source | 30 | 15 | $1.40 | ⭐⭐ KD=15；高 CPC 说明商业用户在寻找；Olares = 本地开源 AI 视频 |
| chinese image to video ai | 720 | 26 | $0.86 | ⭐⭐ 地理+功能双标签；HunyuanVideo 1.5 支持 I2V，KD=26 可竞争 |
| hunyuan video local | 40 | 27 | $0 | ⭐⭐ 本地部署意图，直指 Olares 用例 |
| hunyuan video lora training | 50 | 29 | $0 | ⭐ 开发者 fine-tune，Olares 提供持久化存储和 GPU 环境 |
| how to use hunyuan video | 20 | 0 | $0 | ⭐ GEO 前哨；"How to run HunyuanVideo 1.5 on Olares（ComfyUI workflow）" 教程 |
| self hosted ai video generator | 40 | 46 | $1.29 | ⭐ KD 偏高但意图精准，Olares 直接回答场景 |
| kling alternative | 20 | 0 | $2.31 | ⭐ 低量高 CPC；Olares 上跑 HunyuanVideo = 开源 Kling 替代 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| hunyuan video | 2,900 | 65 | $0.87 | 信息 | 主词候选 | 核心产品词，官网仅排第 3，大量流量被 GitHub/Reddit 截流；写"HunyuanVideo 完整介绍"可争第 1-2 |
| tencent ai | 720 | 26 | $4.55 | 信息/商业 | 主词候选 | KD=26+CPC=$4.55 = 极佳攻击面；写"Tencent AI 模型开源版 vs 闭源"，Olares 角度切入 |
| hunyuan video gguf | 590 | 28 | $0 | 信息 | 主词候选 | 本地部署核心词，Olares ComfyUI + GGUF 权重教程直接承接 |
| hunyuan video 1.5 | 720 | 47 | $1.62 | 产品 | 主词候选 | 版本号词，量和 CPC 均不低；"HunyuanVideo 1.5 setup guide"文章机会 |
| hunyuan video comfyui | 260 | 32 | $0 | 信息 | 主词候选 | 安装意图词，Olares 教程直接匹配；与 gguf 词合并成一篇安装教程 |
| hunyuan vs wan2.1 | 260 | 10 | $0 | 信息 | 主词候选 | KD=10 是全报告最低竞争词；"HunyuanVideo 1.5 vs WAN 2.1 on Olares"对比文极佳 |
| chinese image to video ai | 720 | 26 | $0.86 | 信息 | 主词候选 | KD=26，地理+功能词，Olares 上跑中国开源 I2V 模型是天然叙事 |
| chinese ai video generator free | 320 | 22 | $0.67 | 信息 | 主词候选 | KD=22，免费意图，Olares 本地跑 HunyuanVideo = 真正免费 |
| sora alternative | 210 | 11 | $1.09 | 商业 | 主词候选 | KD=11，替代意图词；可与 "kling alternative / runway alternative" 聚簇 |
| hunyuan-a13b | 1,000 | 33 | $0 | 产品 | 主词候选 | LLM 型号词，KD=33；Ollama 可跑 Hy3 兼容格式，Olares 文章机会 |
| hunyuan video ai | 720 | 55 | $0.97 | 信息 | 次级 | KD 偏高，并入 hunyuan video 主文章 |
| hunyuan image to video | 720 | 56 | $0.98 | 产品 | 次级 | I2V 功能词，并入 HunyuanVideo 教程 |
| hunyuanvideo-1.5 | 880 | 45 | $0.85 | 产品 | 次级 | 版本变体，并入 1.5 介绍文 |
| cogvideox | 2,400 | 38 | $0.78 | 品牌 | 次级 | 开源竞品词，KD=38；在对比文中作为同类开源模型提及 |
| ltx video | 2,400 | 31 | $1.51 | 品牌 | 次级 | KD=31；同类开源视频，Olares 视频生成对比文集合 |
| ai video generator open source | 30 | 15 | $1.40 | 信息 | 次级 | 低量但 KD=15+高 CPC，并入开源视频总索引 |
| open source ai video | 40 | 24 | $1.23 | 信息 | 次级 | 并入同主题文章 |
| hunyuan video avatar | 320 | 34 | $1.07 | 产品 | 次级 | 数字人功能词，配合数字人主题文 |
| hunyuan video prompts | 90 | 17 | $0 | 信息 | 次级⭐ | KD=17，Prompt 优化教程，低竞争 |
| how to use hunyuan video | 20 | 0 | $0 | 信息 | GEO | FAQ 抢引用位："How to run HunyuanVideo 1.5 on Olares with ComfyUI" |
| kling alternative | 20 | 0 | $2.31 | 商业 | GEO | 极低量但 CPC $2.31，AI Overview 抢占位 |
| wan video alternative | 10 | 0 | $0 | 信息 | GEO | 近零量，GEO 前哨语义精准 |
| runway alternative | 10 | 0 | $3.39 | 商业 | GEO | CPC $3.39，高商业价值，GEO 前哨 |
| hunyuan video foley | 90 | 0 | $0 | 信息 | GEO | 音频生成功能词，AI Overview 占位 |
| hunyuan video lora training | 50 | 29 | $0 | 信息 | GEO | LoRA 训练，开发者 GEO |

---

## 核心洞见

1. **品牌护城河**：hunyuan.tencent.com 品牌词（hunyuan、混元、腾讯混元3d 等）全部 Top-1 排名，品牌防御极强。但"hunyuan video"主词官网只排第 3（KD=65），被大量教程站/Reddit/GitHub 截流——这是最可见的攻击缺口。3D 生成方向因有独立落地页（3d.hunyuan.tencent.com）已基本封闭；视频方向流量最分散。

2. **可复制的打法**：腾讯没有程序化落地页策略，也不投 Google Ads。主要靠品牌自然扩散。HunyuanVideo 开源释放了大量长尾技术词（.safetensors 文件名词、gguf 词），这些词月量 50-880 而 KD<30——是教程站/自托管社区的典型打法，Olares 可直接复制。

3. **对 Olares 最关键的词**：
   - `hunyuan vs wan2.1`（260 vol，KD=10）：**全报告最低 KD 词**，且两个模型都可在 Olares 上跑，是直接撑文章的对比选题
   - `hunyuan video gguf`（590 vol，KD=28）：本地部署核心词，GGUF → Ollama → Olares 链路天然打通
   - `tencent ai`（720 vol，KD=26，CPC=$4.55）：高商业意图低竞争词，用"在 Olares 上运行 Tencent 开源 AI"叙事切入

4. **最大攻击面**：HunyuanVideo **许可证非 Apache**（NOASSERTION），商业使用需额外协议；主站没有 Google Ads 说明腾讯完全不在 US 市场做 SEM 竞价——整个 US 英文技术社区流量几乎完全被第三方教程、Reddit、GitHub 截走。Olares 有机会做"官方级别"的 HunyuanVideo 部署教程填补这一空白。

5. **隐藏低 KD 金矿**：
   - `混元ai`（1,600 vol，KD=10）：中文词但在 US DB 有量，KD 极低，海外华人受众；
   - `hunyuan video prompts`（90 vol，KD=17）：Prompt 工程词，教程内容低竞争；
   - `ai video generator open source`（30 vol，KD=15，CPC=$1.40）：低量但 KD=15，开源视频生成总索引入口；
   - `hunyuan video t2v 720p`（50 vol，KD=14）：规格词，技术教程锚点；
   - `image to video hunyuan`（70 vol，KD=30）：I2V 功能词，KD 低

6. **GEO 前瞻布局**（AI Overview / Perplexity 抢引用位）：
   - "How to run HunyuanVideo 1.5 locally on Olares with ComfyUI"（承接 how to use hunyuan video、0 vol 但 AI 问答频繁出现）
   - "Is HunyuanVideo open source?"（直接回答开源许可证问题，is hunyuan video censored 有 10 vol）
   - "HunyuanVideo vs Kling: which is better for local AI video generation?"（kling alternative CPC=$2.31）
   - "Best open source text-to-video model 2026"（0 vol 但高 AI Overview 频率）

7. **与既有分析的关联**：
   - [Hunyuan3D 报告](../../../market/reports/hunyuan3d.md) 已覆盖 3D 生成分支，本报告聚焦视频/LLM 方向，不重复；
   - "tencent ai"（CPC=$4.55）与 olares-500-keywords 中的"self hosted ai"词簇高度互补，可合并成"Chinese open source AI on Olares"主题文；
   - Sora / Kling / Runway 的 alternative 词（KD 普遍<15）可聚成跨报告"open source video generation on Olares"大簇，与 WAN、CogVideoX、LTX Video 报告联动。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、resource_adwords、phrase_related、phrase_fullsearch、phrase_these、phrase_questions、domain_organic_organic）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
