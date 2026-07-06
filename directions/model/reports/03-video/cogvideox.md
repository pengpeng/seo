# CogVideoX 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：THUDM（清华大学 KEG）/ Zhipu AI，github.com/THUDM/CogVideo，CogVideoX License（5B）/ Apache 2.0（2B）
> 无独立官网，SEO 主战场在 HuggingFace / GitHub / ComfyUI 社区内容页（降级模式，跳过 Phase 1 域名报告）

## 模型理解（前置）

CogVideoX 是由清华大学 KEG 实验室（THUDM）与智谱 AI 联合发布的开源视频生成模型，支持 T2V（文生视频）与 I2V（图生视频）双模态。旗舰版 CogVideoX-1.5 5B 可生成最长 10 秒、分辨率 768×1360 的高质量视频，2B 版本采用 Apache 2.0 完全开放商用；社区衍生变体 CogVideoX-Fun 凭借更灵活的控制能力独立形成了较高搜索量。模型通过 ComfyUI、diffusers 分发，是 Pika / Runway 等商业视频 SaaS 的本地开源可自托管平替。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源 T2V/I2V 视频生成模型，5B/2B 双档位，Pika/Runway 本地平替 |
| 许可证 | **CogVideoX License**（5B 版，允许个人与非商业研究，商用需申请）；**Apache 2.0**（2B 版，完全商用友好）；引用前以官方 LICENSE 为准 |
| 主仓库 / 分发 | GitHub `THUDM/CogVideo`（★ 11k+）、HuggingFace `THUDM/CogVideoX-5b` / `THUDM/CogVideoX-2b`、ComfyUI 原生节点 |
| 参数 / VRAM 可跑性 | 5B FP16 全精度：~24GB；FP8 量化：~16GB（RTX 4080/4090 可跑）；2B：~8–12GB；**Olares One（RTX 5090 Mobile 24GB）：FP16 满速跑 5B T2V+I2V，是最小消费级全精度配置** |
| 变体 / 型号 | CogVideoX-1.5-5B（T2V+I2V）、CogVideoX-1.5-2B（T2V，Apache 2.0）、CogVideoX-Fun（社区扩展控制变体）、CogVideoX-3（新版，开始产生搜索量） |
| 闭源对标 | Pika 2.2（月订阅）/ Runway Gen-3 Alpha（月订阅）/ Kling AI（月订阅） |
| Olares Market | ComfyUI ✅ 已上架（[报告](/Users/pengpeng/seo/directions/market/reports/comfyui.md)）；CogVideoX 通过 ComfyUI 自定义节点部署，无需独立 Olares 应用 |
| 来源 | [GitHub THUDM/CogVideo](https://github.com/THUDM/CogVideo)、[HuggingFace THUDM/CogVideoX-5b](https://huggingface.co/THUDM/CogVideoX-5b)、[HuggingFace THUDM/CogVideoX-2b](https://huggingface.co/THUDM/CogVideoX-2b) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。Intent：0=商业 / 1=信息 / 2=导航 / 3=交易。

### 品牌 / 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| cogvideox | 2,400 | 38 | $0.78 | 1 |
| cogvideo | 1,300 | 32 | $0.93 | 1 |
| cogvideox-fun ⭐ | 320 | 15 | $0.00 | 1 |
| cogvideo ai free ⭐ | 260 | 25 | $0.00 | 2 |
| cogvideox-fun-v1.1-5b-inp-mps.safetensors ⭐ | 210 | 19 | $0.00 | 1,3 |
| cogvideox-5b | 170 | 34 | $1.15 | 1 |
| cogstudio ⭐ | 140 | 31 | $0.00 | 1,3 |
| cogvideo ai ⭐ | 140 | 19 | $0.90 | 2 |
| cog video ⭐ | 110 | 27 | $0.80 | 1 |
| cogvideox ai | 50 | 40 | $0.58 | 1 |
| cogvideox 5b ⭐ | 50 | 25 | $1.15 | 1 |
| cogvideox 5b 1.5 ⭐ | 40 | 29 | $0.00 | 2 |
| cogstudio image to video ⭐ | 40 | 22 | $0.00 | 1,3 |
| cogvideox-3 ⭐ | 30 | 19 | $0.78 | 1,0 |
| cogvideo ai video generator ⭐ | 30 | 26 | $1.08 | 2 |
| cogvideox 1.5 | 20 | 0 | $0.00 | — |
| cogvideox 2b | 20 | 0 | $0.00 | — |
| cogvideox fun ⭐ | 20 | 15 | $0.00 | 1 |
| open source video generation model ⭐ | 110 | 34 | $1.70 | 1 |

*注：`cogvideox-fun` 与 `cogvideox fun` 均指社区变体 CogVideoX-Fun，搜索量合计约 340/月，KD=15 极低——是品牌词中最易排名的细分入口。`cogstudio` 为智谱官方 web demo，140/月 KD=31。*

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| cogvideox comfyui ⭐ | 40 | 30 | $0.00 | 1 |
| cogvideox-fun-v1.1-5b-inp-mps.safetensors ⭐ | 210 | 19 | $0.00 | 1,3 |

*注：`cogvideox ollama` / `cogvideox vllm` 月量为 0——CogVideoX 是视频扩散模型，不走 Ollama/vLLM 文本推理路径；ComfyUI 是唯一主流本地引擎。*.safetensors 文件名出现 210/月搜索说明用户在积极搜索下载方式。*

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| local text to video ⭐ | 40 | 27 | $0.00 | 1 |
| local video generation ai | 20 | 0 | $1.55 | — |
| cogvideox install | 20 | 0 | $0.00 | — |

*注：`run cogvideox locally`、`cogvideox vram`、`cogvideox fp8`、`cogvideox gguf` 月量均为 0——属 GEO 抢发候选，AI Overview / Perplexity 引用位尚空。*

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| free text to video generator | 880 | 75 | $1.24 | 1 |
| open source ai video generator ⭐ | 590 | 35 | $1.19 | 1 |
| ai video generator open source ⭐ | 30 | 15 | $1.40 | 1 |
| open source text to video | 40 | 51 | $1.60 | 1 |
| pika alternative | 10 | 0 | $1.37 | — |
| runway alternative | 10 | 0 | $3.39 | — |
| text to video open source | 20 | 0 | $0.00 | — |
| best open source video model | 20 | 0 | $0.00 | — |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| cogvideox-fun | 320 | 15 | $0.00 | CogVideoX-Fun 是 ComfyUI 生态中控制性最强的视频生成变体，KD=15 极低；Olares Market 上架的 ComfyUI 一键安装即能加载 Fun 系列模型，是 Olares 对"本地可控视频生成"最直接的具体示范 | ⭐⭐⭐ |
| open source ai video generator | 590 | 35 | $1.19 | 品类高量词，KD=35 可争；Olares「本地 AI 一体机」叙事命中——不限 token、数据不出设备、无月费；CogVideoX-1.5 2B（Apache 2.0）是完全商用友好的具体载体 | ⭐⭐⭐ |
| cogvideox comfyui | 40 | 30 | $0.00 | 部署意图精准，KD=30；Olares Market 已上架 ComfyUI，一键安装后直接加载 CogVideoX ComfyUI 节点，最短部署路径；适合「Olares 上运行 CogVideoX」部署教程类内容 | ⭐⭐⭐ |
| local text to video | 40 | 27 | $0.00 | 品类意图直接，KD=27 ⭐；搜索此词的用户就是 Olares 目标用户；Olares One 24GB 是跑 CogVideoX-1.5 5B 的最小消费级全精度配置 | ⭐⭐⭐ |
| cogvideox 2b | 20 | 0 | $0.00 | 2B = Apache 2.0 完全商用友好，叙事最干净；Olares 8–12GB GPU 用户（如搭配 RTX 4070）也可本地跑，打开更宽的覆盖面；GEO 抢发窗口尚空 | ⭐⭐⭐ |
| ai video generator open source | 30 | 15 | $1.40 | KD=15 全对比组最低，CPC=$1.40 说明商业意图真实；Olares + CogVideoX = 「自托管开源 AI 视频生成器」最完整答案；内容易排名 | ⭐⭐⭐ |
| cogvideox-5b | 170 | 34 | $1.15 | 旗舰型号主词，KD=34，CPC=$1.15；Olares One 24GB 是唯一能无压力 FP16 全精度跑 5B 的消费级整机，硬件规格直接命中 | ⭐⭐ |
| cogvideo ai free | 260 | 25 | $0.00 | "免费"意图明确，KD=25 ⭐；Olares 本地跑 CogVideoX-1.5 2B（Apache 2.0）= 真正零成本，无订阅、无水印、无限次数 | ⭐⭐ |
| cogstudio | 140 | 31 | $0.00 | CogStudio 是智谱官方 web demo；搜索此词的用户想用云端 demo，Olares 可提供本地等价体验+隐私保护；KD=31，可在对比文里覆盖 | ⭐⭐ |
| cogvideox-3 | 30 | 19 | $0.78 | 新版本词（KD=19），搜索量开始形成；Olares 本地部署叙事可随版本升级持续保鲜，GEO 预占后可随版本发布截获首批搜索流量 | ⭐⭐ |
| pika alternative | 10 | 0 | $1.37 | 近零量但 CPC=$1.37，商业意图高；Pika 月订阅 vs CogVideoX 本地免费——是攻击面最清晰的对比词；GEO 抢发后可截获高价值用户 | ⭐⭐ |
| runway alternative | 10 | 0 | $3.39 | CPC=$3.39 全表最高！商业意图极强；Runway Gen-3 月费高达 $76；本地部署 CogVideoX = 永久零边际成本；GEO 抢发价值高 | ⭐⭐ |
| cogvideo | 1,300 | 32 | $0.93 | 品牌大词，量=1,300；建立"CogVideo/CogVideoX = Olares 视频生成首选"的品牌联想，长期 SEO 锚点 | ⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度） |
|--------|------|----|-----|------|------|---------------------------|
| cogvideox | 2,400 | 38 | $0.78 | 信息 | 主词候选 | 品牌主词，量最大但 KD=38；适合做锚点对比/教程页，难单独冲首位 |
| cogvideo | 1,300 | 32 | $0.93 | 信息 | 主词候选 | 家族大词，与 cogvideox 合并优化；量级+KD 均可争 |
| open source ai video generator ⭐ | 590 | 35 | $1.19 | 信息 | **主词候选 ⭐** | KD=35、CPC=$1.19、量=590；品类非品牌主词，Olares 本地部署叙事命中，价值高 |
| cogvideox-fun ⭐ | 320 | 15 | $0.00 | 信息 | **次级 ⭐⭐** | KD=15 全品牌组最低，量=320；CogVideoX-Fun 是部署教程最易排名的具体入口，Olares+ComfyUI 联动叙事 |
| cogvideo ai free ⭐ | 260 | 25 | $0.00 | 导航 | 次级 ⭐ | 量=260，KD=25；"free"意图强，2B Apache 2.0 + Olares 本地跑 = 真正零成本答案 |
| cogvideox-fun-v1.1-5b-inp-mps.safetensors ⭐ | 210 | 19 | $0.00 | 信息,交易 | 次级 ⭐ | 量=210，KD=19；ComfyUI 模型文件搜索，说明用户在积极下载配置，Olares 一键部署路径可转化此类用户 |
| cogvideox-5b | 170 | 34 | $1.15 | 信息 | 次级 | 5B 旗舰型号词，KD=34；CPC=$1.15 有商业价值；对应 Olares One 24GB 满血部署叙事 |
| cogstudio ⭐ | 140 | 31 | $0.00 | 信息,交易 | 次级 | 量=140，KD=31；官方 web demo 词，可在对比文里以"本地 CogStudio 替代 = Olares 部署"覆盖 |
| cogvideo ai ⭐ | 140 | 19 | $0.90 | 导航 | 次级 ⭐ | KD=19 低，量=140；导航意图，转化率高；Olares 可作为"本地 CogVideo AI"最佳落地平台 |
| cog video ⭐ | 110 | 27 | $0.80 | 信息 | 次级 ⭐ | 品牌拼写变体，KD=27，量=110；合并 cogvideox 页面优化时一并覆盖 |
| open source video generation model ⭐ | 110 | 34 | $1.70 | 信息 | 次级 | 量=110，KD=34，CPC=$1.70；品类词，与 "open source ai video generator" 可合页覆盖 |
| cogvideox comfyui ⭐ | 40 | 30 | $0.00 | 信息 | **次级 ⭐** | KD=30，量=40；部署意图精准，是 Olares Market ComfyUI 一键安装叙事的直接入口词 |
| local text to video ⭐ | 40 | 27 | $0.00 | 信息 | 次级 ⭐ | KD=27，量=40；品类部署意图词，搜索者=Olares 目标用户，Olares One 是最简部署方案 |
| cogvideox 5b ⭐ | 50 | 25 | $1.15 | 信息 | 次级 ⭐ | KD=25，量=50；5B 旗舰参数词，CPC 有价值；Olares One 24GB FP16 全精度叙事命中 |
| ai video generator open source ⭐ | 30 | 15 | $1.40 | 信息 | **主词候选 ⭐** | KD=15 最低对比词！量=30 偏少但 CPC=$1.40；意图精准+商业价值高，GEO 抢位价值大 |
| cogvideox-3 ⭐ | 30 | 19 | $0.78 | 信息,商业 | **GEO ⭐** | 新版本词，KD=19 低，量开始形成；GEO 抢占后可随版本升级持续引流 |
| cogvideox 5b 1.5 ⭐ | 40 | 29 | $0.00 | 导航 | 次级 ⭐ | KD=29，量=40；精确型号词，导航意图说明用户在找具体部署教程 |
| pika alternative | 10 | 0 | $1.37 | — | **GEO ⭐** | 近零量但 CPC=$1.37；Pika 月订阅 vs 本地免费对比，商业意图强；AI Overview 抢发 |
| runway alternative | 10 | 0 | $3.39 | — | **GEO ⭐⭐** | CPC=$3.39 全表最高！商业意图极强，量虽低；Runway Gen-3 用户是高价值付费用户，GEO 截获价值极大 |
| run cogvideox locally | 0 | — | $0.00 | — | **GEO ⭐** | 当前零量，语义精准；随模型传播可预期增长；Perplexity/ChatGPT 引用位抢发 |
| cogvideox vram | 0 | — | $0.00 | — | **GEO ⭐** | 硬件选型问答，Olares One 规格表直接命中；AI Overview 尚空 |
| cogvideox fp8 | 0 | — | $0.00 | — | **GEO ⭐** | FP8 量化让 5B 在 16GB GPU 可跑，拓宽 Olares 用户覆盖；答案型内容 GEO 抢发 |

---

## 核心洞见

### 1. 搜索心智是否建立

**已部分建立，体量中等，社区分支词异常强势。** `cogvideox` US 月均 2,400，`cogvideo` 1,300——品牌词合计约 3,700/月（US），与 HunyuanVideo（~7,000/月）相比偏小约一半，但高于大多数学术系开源视频模型。最值得注意的异常是**`cogvideox-fun` KD=15，月量 320**——社区变体比官方品牌词更容易排名；`.safetensors` 文件名词（210/月，KD=19）说明 ComfyUI 用户在积极下载模型权重，是高转化意图信号。**CogVideoX-3** 已开始形成搜索量（30/月，KD=19），是版本升级带来的新流量窗口。

### 2. 消费级 GPU / Olares One 能否本地跑

**完全可以，Olares One 是最小消费级全精度配置。**

- **5B FP16 全精度**：~24GB；Olares One（RTX 5090 Mobile 24GB GDDR7）可流畅运行，是消费级整机中唯一无压力的配置。
- **5B FP8 量化**：~16GB；RTX 4080/4080 Super 16GB 可跑。
- **2B（Apache 2.0）**：~8–12GB；RTX 4070 Ti 12GB 也可跑，覆盖面更宽。
- **关键结论**：Olares One 是「按官方推荐规格运行 CogVideoX-1.5 5B 的最小消费级整机配置」，叙事完全成立。且 2B Apache 2.0 版本可在更多硬件上运行，提供许可证最干净的叙事入口。Olares 平台 NVIDIA GPU 支持最成熟，ComfyUI 已上架 Olares Market，一键部署最短路径。

### 3. 许可证是否商用友好

**分版本，策略不同。**
- **CogVideoX-1.5-2B：Apache 2.0**——完全商用友好，是 Olares 内容中可以无限制推广的主推版本，叙事最干净；
- **CogVideoX-1.5-5B：CogVideoX License**——允许个人/研究使用，商业用途需向智谱申请；内容中需注明限制，强调"本地自用/隐私保护"而非"商业再分发"；
- **叙事建议**：面向一般用户时优先推 2B Apache 2.0（"完全免费、商用友好、不用申请"）；面向需要更高质量的用户时推 5B + Olares One（"最佳本地视频生成体验，数据不出机"）。

### 4. 对 Olares 最关键的 2-3 个词

1. **`cogvideox-fun`**（320/月，KD=15）：全品牌组 KD 最低的有量词；CogVideoX-Fun 通过 ComfyUI 部署，Olares Market 已上架 ComfyUI——是 Olares「一键视频 AI」叙事最易落地排名的具体入口。
2. **`open source ai video generator`**（590/月，KD=35，CPC=$1.19）：品类主词，量最大的非品牌机会词；Olares + CogVideoX 2B（Apache 2.0）= 完整「自托管开源视频生成器」答案，商业价值高。
3. **`cogvideox comfyui`**（40/月，KD=30）：部署意图精准，是 Olares Market ComfyUI 一键安装叙事的直接验证词；搜索此词的用户=准 Olares 用户。

### 5. 新模型 GEO 抢发窗口

以下词量少但语义精准，AI Overview / Perplexity / ChatGPT 引用位尚未被权威内容占据：

| 词 | 量 | KD | 抢发理由 |
|---|---|---|---------|
| runway alternative | 10 | 0 | CPC=$3.39 全表最高，商业意图极强；Runway 用户高价值，GEO 截获回报最高 |
| pika alternative | 10 | 0 | CPC=$1.37，Pika 月订阅用户外溢；CogVideoX 2B 本地 = 真正零成本替代 |
| cogvideox-3 | 30 | 19 | 新版本词量已形成，KD=19；GEO 抢占后随版本升级持续引流 |
| run cogvideox locally | 0 | — | 语义精准，随模型传播增长可预期；Perplexity 引用位先占 |
| cogvideox vram | 0 | — | 硬件选型问答，Olares One 规格表直接命中 |
| cogvideox fp8 | 0 | — | FP8 量化拓宽至 16GB 用户，答案型内容 GEO 抢发 |
| text to video open source | 20 | 0 | 品类意图，零竞争；AI Overview 答案位尚空，抢发后持续引流 |

### 6. 闭源对标与攻击面

- **Pika 2.2**（付费订阅，$8–$28/月）：Pika 生成限额 + 水印 + 云端内容审查；CogVideoX 2B（Apache 2.0）本地运行 = 无订阅费、无水印、无限次数、无审查。
- **Runway Gen-3 Alpha**（$12–$76/月）：算力限额严格，超额停生成；本地 GPU 一次性投入后零边际成本。Runway 词的 CPC=$3.39 说明其用户高价值，是攻击回报最高的对标。
- **Kling AI**（月订阅，云端）：快手旗下，同样有内容限制和隐私风险；Olares 本地部署完全规避。
- **通用攻击面**：三者均有「额度限制导致超量停生成」「云端内容过滤无法绕过」「视频数据上传云端隐私风险」「月费累积成本高」四个痛点；CogVideoX + Olares 全部解决。
- **许可证备注**：5B 版 CogVideoX License 需申请商业授权，在与 Wan 2.2（Apache 2.0）对比时是弱点；叙事上应以 2B Apache 2.0 版本作为"完全免费平替"主打，5B 版主打"最佳本地视频质量"。

### 7. 与 model/models.md 同类 family 及跨报告关联

- **同章（03-video）竞品**：Wan 2.2 ✅、HunyuanVideo ✅ 均已有报告——三者可组成「2026 年本地开源视频模型横评：Wan vs HunyuanVideo vs CogVideoX」，覆盖跨报告低 KD 比较词。
- **ComfyUI 共享路径**：ComfyUI 在 market/reports ✅——三款视频模型均通过 ComfyUI 部署，可合并为「ComfyUI 本地视频 AI 完全指南：Wan/HunyuanVideo/CogVideoX 一站安装」覆盖多词。
- **Keyword 簇建议**（给 seo-content 层）：`cogvideox-fun + cogvideox comfyui + cogvideox install` 可聚合为「在 Olares 上一键运行 CogVideoX-Fun」部署教程簇；`open source ai video generator + ai video generator open source + local text to video` 可聚合品类对比簇；`pika alternative + runway alternative + cogvideox 2b` 可聚合商业 SaaS vs 本地开源对比簇（以 Apache 2.0 主打，CPC 高，GEO 价值最大）。

---

*数据来源：SEMrush US（phrase_these × 3 批次、phrase_related × 1 批次）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
