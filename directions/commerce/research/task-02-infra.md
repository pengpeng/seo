# task-02 · 基础设施 / 算力层发现

> 发现阶段笔记，AS_OF=2026-07-04。约 75 个达标实体。子代理只读，Lead 落盘。

## Sources（节选）
[1] valueaddvc.com/ai-landscape (行业地图,2026-06) | [2] aifundingtracker.com/top-50-ai-startups (2026-06) | [3] cbinsights.com AI100 (2026-05) | [4] edgarlookup.com SIC7372 (2026-07) | [5] investors.coreweave.com (2026-05) | [6] siliconangle Modal $355M (2026-05) | [7] techcrunch Together $800M/$8.3B (2026-07-01) | [8] sacra.com/c/crusoe (2026-02) | [9] futurumgroup Nebius Q1FY26 (2026-05) | [10] finance.yahoo CBRS (2026-07) | [11] companiesmarketcap NVIDIA (2026-07) | [12] techcrunch Etched $5B/$1B (2026-06-30) | [13] sacra Turbopuffer $100M (2026-03) | [14] businesswire Qdrant $50M SeriesB (2026-03-12) | [15] langchain.com/blog/series-b (2025-10) | [16] baseten.co SeriesF (2026-06-22) | [17] sacra hugging-face | [18] nscale SeriesC (2026-03-09) | [19] broadcom IR Q1FY26 (2026-03) | [20] techcrunch inferact $150M (2026-01-22)

## Products

### GPU/算力云 & 推理基础设施
- **CoreWeave** coreweave.com | 市值~$44–55B [5][10]；FY25 收入 $5.13B。市值✓
- **Nebius (Token Factory)** nebius.com | Q1'26 收入 $399M [9]；2026 指引 $3.0–3.4B、exit ARR $7–9B；市值~$61B。ARR✓市值✓
- **Lambda Labs** lambda.ai | ARR ~$760M [8]；估值 ~$5.9B；融资 ~$2.36B。全命中
- **Crusoe** crusoe.ai | 估值 >$10B [8]；融资 ~$3.9B；2026 收入指引 ~$2B。估值✓融资✓
- **Modal** modal.com | ARR ~$300M [6]；估值 $4.65B；本轮 $355M。全命中
- **Together AI** together.ai | 估值 $8.3B [7]；融资 $800M SeriesC；年化预订 >$1.15B。全命中
- **Baseten** baseten.co | ARR ~$600M [16]；估值 $13B；融资 $1.5B SeriesF。全命中
- **Fireworks AI** fireworks.ai | ARR ~$800M [20]；估值谈判 $15B；融资 $327M+。全命中
- **RunPod** runpod.io | ARR ~$240M [2]；估值 $1B；融资 $100M。全命中
- **Nscale** nscale.com | 估值 $14.6B [18]；融资 $2B SeriesC。估值✓融资✓
- **FluidStack** fluidstack.io | 估值谈判 $18B [20]；Anthropic $50B 数据中心协议。估值✓
- **TensorWave** tensorwave.com | 估值 $1.55B [20]；融资 $350M。估值✓融资✓
- **Lightning AI (+Voltage Park)** lightning.ai | ARR >$500M [20]；估值 >$2.5B。ARR✓估值✓
- **Fal.ai** fal.ai | 估值 $4.5B [20]；融资 ~$587M。估值✓融资✓
- **DeepInfra** deepinfra.com | 融资 $133M（$107M SeriesB）。融资✓
- **Anyscale (Ray)** anyscale.com | 估值 $1B+ [3]；融资 [unverified]。估值✓
- **AWS (Trainium/SageMaker/Bedrock)** | Amazon 市值>>$5B。旗舰
- **Microsoft Azure AI** | 市值~$2.9T；AI run-rate ~$37B。旗舰
- **Google Cloud (TPU/Vertex)** | Alphabet CapEx $185B 2026。旗舰
- **Inferact (vLLM 商业化)** inferact.ai | 估值 $800M [19]；融资 $150M seed。估值✓融资✓
- **RadixArk (SGLang)** | 估值 $400M；融资 $100M seed。估值✓融资✓

### AI 芯片/硬件/互联
- **NVIDIA** | 市值 ~$4.72T [11]；FY 收入 ~$216B。市值✓旗舰
- **AMD** | 市值 ~$844B [11]。市值✓
- **Cerebras (CBRS)** | 市值 ~$47–50B [10]；IPO 2026-05。市值✓
- **Broadcom** | 市值 ~$1.87T [19]；Q2FY26 AI semi $10.8B。市值✓
- **Marvell** | 市值 ~$269B [19]。市值✓
- **Etched (Sohu)** | 估值 $5B [12]；融资 $800M；订单 $1B。估值✓融资✓
- **SambaNova** | SeriesE $350M [20]；寻求 ~$10B。融资✓
- **Groq (LPU)** | NVIDIA 收购资产 ~$20B [20]，仍独立运营 inference。估值✓
- **Tenstorrent** | 估值 $2.6–3.2B [20]；融资 $1.18B。估值✓融资✓
- **Positron** | 估值 >$1B；融资 $230M。估值✓融资✓
- **d-Matrix** | 估值 $2B；融资 $429M。估值✓融资✓
- **Upscale AI** | 估值 $2B；融资 $500M。估值✓融资✓
- **Arista Networks** | 市值 ~$164B。市值✓
- **Super Micro (SMCI)** | 市值 ~$17B。市值✓

### 向量数据库 / 检索基础设施
- **Turbopuffer** | ARR ~$100M [13]。ARR✓
- **Pinecone** | 估值 $750M [13]；融资 $138M。估值✓融资✓
- **Qdrant** | SeriesB $50M [14]。融资✓
- **Weaviate** | 估值 $200M；融资 $67.6M+。估值✓融资✓
- **Zilliz/Milvus** | 融资 $115M。融资✓
- **MongoDB (+Voyage)** | 市值 ~$25B；收购 Voyage ~$161M。市值✓
- **Elastic (+Jina)** | 市值 ~$10B。市值✓
- **Snowflake (Cortex/向量)** | 市值 ~$90B。市值✓

### Embedding / Rerank API
- **Cohere (Embed/Rerank)** | ARR ~$262M+；估值 $7–20B；融资 $1.3B+。全命中（与 task-01 重复）
- **Voyage AI** | 融资 $28M；被 MongoDB 收购 $161M。（已收购）
- **Jina AI** | 融资 $39M；被 Elastic 收购 2025-10。（已收购）

### LLM 框架 / 可观测 / 评估 / MLOps
- **LangChain/LangSmith** | 估值 $1.25B [15]；融资 $260M。估值✓融资✓
- **Braintrust** | 估值 $800M；融资 $80M SeriesB。估值✓融资✓
- **Arize AI** | 估值 ~$742M [20]；融资 $131M。估值✓融资✓
- **Weights & Biases (被 CoreWeave 收购)** | 估值 $1.1–1.3B；融资 $325M。（与 task-01 重复）
- **LMArena** | 估值 $1.7B [2]。估值✓
- **E2B (Agent sandbox)** | 融资 $32–35M。融资✓
- **LlamaIndex** | 融资 $27.5M。融资✓
- **Datadog** | 市值 ~$88B。市值✓（与 task-03 重复）
- **Databricks/Scale AI** | 见 task-01

## Gaps
- 未达标：Vast.ai（融资~$4M）、Chroma（融资~$18M）、Nomic AI（融资$19M/估值~$100M）、Prime Intellect（刚过$20M待复核）。
- 已被收购以母公司计：Replicate（→Cloudflare）、Voyage（→MongoDB）、Jina（→Elastic）。
- 未系统扫：中国算力/向量/Embedding 商业方（阿里云 PAI、百度千帆等）。
