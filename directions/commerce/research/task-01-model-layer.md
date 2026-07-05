# task-01 · 模型层发现（前沿模型 / 推理 API / 聚合路由 / 模型平台）

> 发现阶段笔记，AS_OF=2026-07-04。财务数字带来源，冲突处标 `[unverified]` 或并列。子代理只读模式产出，Lead 落盘。

## Sources

| # | URL | Source-Type | as-of |
|---|-----|-------------|-------|
| [1] | https://presenc.ai/research/ai-lab-revenue-and-valuation-2026 | secondary-industry | 2026-05 |
| [2] | https://aifundingtracker.com/top-50-ai-startups/ | secondary-industry | 2026-06-01 |
| [3] | https://valueaddvc.com/blog/a16z-ai-fund-what-andreessen-horowitz-is-betting-on-in-the-ai-era | secondary-industry | 2026-06-13 |
| [4] | https://valueaddvc.com/ai-landscape | secondary-industry | 2026-06 |
| [5] | https://rywalker.com/research/ai-inference-platforms | secondary-industry | 2026-06 |
| [6] | https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/ | journalism | 2026-07-01 |
| [7] | https://www.together.ai/blog/announcing-our-series-c | official | 2026-07-01 |
| [8] | https://www.baseten.co/blog/announcing-our-series-f/ | official | 2026-06-22 |
| [9] | https://openrouter.ai/blog/announcements/series-b/ | official | 2026-05-28 |
| [10] | https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/ | journalism | 2026-05-26 |
| [11] | https://www.cnbc.com/2026/06/16/databricks-revenue-growth-tops-80percent-to-6point9-billion-annualized.html | journalism | 2026-06-16 |
| [12] | https://www.finsmes.com/2026/06/deepseek-raises-over-7-4-billion-in-maiden-funding-at-a-post-money-valuation-exceeding-50-billion.html | journalism | 2026-06-22 |
| [13] | https://groq.com/newsroom/groq-raises-750-million-as-inference-demand-surges | official | 2025-09-17 |
| [14] | https://fourweekmba.com/hugging-face-100m-arr-open-source-ai-platform/ | secondary-industry | 2026-06 |
| [15] | https://techcrunch.com/2025/12/01/black-forest-labs-raises-300m-at-3-25b-valuation/ | journalism | 2025-12-01 |
| [16] | https://247wallst.com/investing/2026/07/01/why-amazon-may-be-the-smartest-long-term-ai-investment-nobody-is-talking-about/ | journalism | 2026-07-01 |
| [17] | https://www.calcalistech.com/ctechnews/article/rjswz37eze | journalism | 2026 |
| [18] | https://deepinfra.com/series-b | official | 2026-05-04 |

## Products

### 前沿模型实验室
- **OpenAI** | openai.com | ARR ~$25B [1] / run-rate $24–30B [2]；估值 ~$750B [1] / $852B [2]；融资 $186B+ [2]。旗舰。
- **Anthropic** | anthropic.com | ARR ~$30B [1] / run-rate $47B [2]；估值 $380B [1] / $965B [2]；融资 $132B+ [2]。旗舰。
- **Google Gemini/Vertex** | ai.google | AI ARR ~$28B [1]；Alphabet 上市市值>>$5B。旗舰。
- **Meta Llama/Meta AI** | ai.meta.com | 模型直接收入 $0（开源）[4]；META 上市。旗舰。
- **xAI (Grok)** | x.ai | ARR ~$1.5B [1]；估值 ~$200B [1]；融资 $38B+ [2]。旗舰。
- **Mistral** | mistral.ai | ARR ~$1B [1]；估值 ~$15–16B [1][2]；融资 ~$1.6B [2]。
- **Cohere** | cohere.com | ARR ~$500M [1]；估值 ~$6.5–7.2B [1][2]；融资 ~$1.3B [2]。
- **DeepSeek** | deepseek.com | ARR ~$700M [1]；估值 >$50B [12]；融资 >$7.4B [12]。
- **Moonshot (Kimi)** | moonshot.cn | ARR ~$500M [1]；估值 ~$3.5B [1]。
- **Zhipu (GLM)** | zhipuai.cn | ARR ~$480M [1]；估值 ~$3.0B [1]。
- **MiniMax** | minimax.io | ARR ~$300M [Sacra] `[unverified]`；估值 ~$4B；融资 ~$1.15B+。
- **AI21 Labs** | ai21.com | ARR ~$50–58M [GetLatka/17]（边缘）；估值 $1.4B [17]；融资 $208–461M。
- **Inflection** | inflection.ai | ARR ~$300M `[unverified]` [1]；估值 ~$4B；融资 $1.52B。
- **Reka** | reka.ai | 估值 $1.3B [Forge]；融资 ~$167M。
- **Stability AI** | stability.ai | ARR ~$90M [1] / $104M [GetLatka] 冲突；估值 $495M [Forge] vs $1B；融资 $181–399M。
- **Baidu ERNIE** | yiyan.baidu.com | AI 收入年化 ~$1.9B+ [Baidu IR]；市值 ~$42B。旗舰。
- **Alibaba Qwen** | qwen.ai | 市值 ~$310B。旗舰。
- **ByteDance Doubao/Seed** | doubao.com | 估值 $400–550B。旗舰。
- **Tencent Hunyuan** | hunyuan.tencent.com | 市值 ~$520B。旗舰。
- **Microsoft Azure OpenAI/AI Foundry** | azure.microsoft.com | MSFT 上市。旗舰。
- **Apple Intelligence** | apple.com | AAPL 上市。旗舰。
- （边界，模型+应用混合，另见对应任务）**ElevenLabs**（语音基础模型，$500M+ ARR/$11B）、**Black Forest Labs FLUX**（$3.25B/$450M+）、**Runway**（$5.3B）、**Midjourney**（$250M+ rev/$3.2B）、**Character.AI**（$1B/$193M）。

### 推理 API / 托管
- **Groq/GroqCloud** | groq.com | 估值 $6–6.9B [13]；融资 $2.4B+。
- **Together AI** | together.ai | bookings >$1.15B [6][7]；估值 $8.3B [6]；融资 ~$1.33B。
- **Fireworks AI** | fireworks.ai | ARR ~$800M [5]；估值 ~$15B talks [Bloomberg]；融资 $327M+。
- **Baseten** | baseten.co | ARR ~$600M [5][8]；估值 $11–13B [8]；融资 ~$2.08B。
- **Fal** | fal.ai | ARR ~$400M `[unverified]` [5]；估值 $4.5B [5]。
- **Modal** | modal.com | ARR ~$300M [5]；估值 $4.65B [5]；融资 $111M+。
- **DeepInfra** | deepinfra.com | 融资 $133M（$107M Series B）[18]。
- **Anyscale** | anyscale.com | 估值 $1B；融资 $281M。
- **Cerebras** | cerebras.ai | 2025 收入 $510M [2]；上市 CBRS peak ~$95B。
- **CoreWeave** | coreweave.com | 2025 收入 $5.1B [2]；市值 ~$50B+。
- **Lambda Labs** | lambda.ai | 估值 $2.5–11B range；融资 ~$2.4B。
- **Nebius (Token Factory)** | nebius.com | AI ARR $1.9B [5]；市值 ~$61B。
- **SambaNova** | sambanova.ai | 估值 ~$2.2B [5]。
- **Inferact** | inferact.ai | 估值 $800M [2]；融资 $150M。
- **Amazon Bedrock** | aws.amazon.com/bedrock | AWS AI >$15B run-rate [16] `[unverified]` 拆分。旗舰。
- **Replicate（被 Cloudflare 收购）** | replicate.com | 融资 $88M；收购前估值 $460M [2]。
- **Cloudflare Workers AI** | cloudflare.com | NET 上市。

### 模型聚合 / 路由
- **OpenRouter** | openrouter.ai | ARR ~$50M [5]；估值 ~$1.3B [9][10]；融资 $113M [9]。
- **Poe** | poe.com（Quora）| ARR ~$65M est. `[unverified]`；Poe 专项融资 $75M（a16z 2024）。
- **Vercel AI Gateway** | vercel.com/ai | 母公司估值 $11B [2]。
- **Perplexity（Model Council/API）** | perplexity.ai | ARR $200M+ [2]；估值 $22.6B [2]（主定位 AI 搜索，边界）。

### 模型平台 / MLOps / 数据智能
- **Hugging Face** | huggingface.co | ARR $100M+ [14]；估值 $4.5–5.1B 冲突；融资 $395–545M。
- **Databricks** | databricks.com | ARR $6.9B [11]；估值 $134B [11]。
- **Scale AI** | scale.ai | ARR ~$820M [2]；估值 ~$29B [Meta deal]；融资 $1.9B+。
- **Weights & Biases（被 CoreWeave 收购）** | wandb.ai | 估值 $1.1B；融资 $325M；收购 ~$1.7B。
- **Snowflake Cortex AI** | snowflake.com | 市值 ~$83B [11]；ARR ~$5.6B。

## Gaps
- 未达标邻近：Requesty（~$3M seed）。
- Neocloud 补漏（部分超门槛未展开）：RunPod、Upscale AI（$500M/@$2B）、TensorWave（$350M/@$1.55B）、Nscale（$2B/@$14.6B [2]）。
- ARR/估值冲突：OpenAI/Anthropic [1] vs [2] 差 2x+；Stability $495M vs $1B；HF $4.5B vs $5.1B。
- 大厂子产品难拆独立 cap table：Azure OpenAI、Vertex、Bedrock。
- 可能遗漏：IBM watsonx/Granite、Oracle OCI GenAI、NVIDIA NIM、01.AI/StepFun/Baichuan。
- arr.club 抓取超时未纳入。
