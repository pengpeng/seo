# commerce 产品清单 · 附录（出范围 / 次级 / 待决）

> 配套 [products.md](/Users/pengpeng/seo/directions/commerce/products.md)。收纳达标但**非可平替竞品**、上游供应商、被收购母体、未达门槛的观察项。AS_OF：2026-07-04。

## A. 移入附录（#1#4#6）

### A1. GPU / 算力云（neocloud）
达标但为"租算力"生意，Olares One 是"自有算力 vs 租"的对位叙事，非可平替 SaaS。
| 商业产品 | 公司 | 达标依据 | 关系 |
|------|------|---------|------|
| CoreWeave | CoreWeave | 收入 $5.1B；市值 ~$50B | Olares One（自有算力） |
| Nebius | Nebius | AI ARR $1.9B；市值 ~$61B | Olares One |
| Lambda Labs | Lambda | ARR ~$760M；融资 ~$2.4B | Olares One |
| Crusoe | Crusoe | 估值 >$10B；融资 ~$3.9B | Olares One |
| RunPod | RunPod | ARR ~$240M；估值 $1B | Olares One |
| Nscale | Nscale | 估值 $14.6B；融资 $2B | Olares One |
| Lightning AI | Lightning AI | ARR >$500M；估值 >$2.5B | Olares One + JupyterHub |

> FluidStack、TensorWave、Vast.ai 亦属此类。

### A2. 模型平台 / 数据云 / MLOps
| 商业产品 | 公司 | 达标依据 | 备注 |
|------|------|---------|------|
| Hugging Face | Hugging Face | ARR $100M+；估值 $4.5–5.1B | Olares Market + Ollama 可承接下载/托管，但 HF 生态本身非单一可平替 SaaS |
| Databricks | Databricks | 年化 $6.9B；估值 $134B | 数据+AI 平台，无 1:1 平替（组合 ClickHouse/Trino/MLflow） |

### A3. 数据标注 / 评估
| 商业产品 | 公司 | 达标依据 | 平替 |
|------|------|---------|------|
| Scale AI | Scale AI | ARR ~$820M；估值 ~$29B（Meta 持 49%） | Label Studio / LLaMA Factory |
| LMArena | LMArena | 估值 $1.7B | 无直接平替 |

### A4. AI 芯片 / 硬件供应商（Olares One 上游，硬件侧见 hardware/）
NVIDIA、AMD、Broadcom、Marvell、Cerebras、Etched、SambaNova、Groq(芯片)、Tenstorrent、d-Matrix、Positron、Upscale AI、Arista、Supermicro。

### A5–A7. 向量库 / Embedding·Rerank API / 推理 API·模型托管 → 已迁至 tech/（方向 6）

> 这三类纯开发者/基础设施向产品（Pinecone·Turbopuffer·Zilliz、Voyage·Cohere Embed·Jina、Together·Fireworks·Baseten·Modal·Bedrock 等）已并入 tech 方向的「AI 基础设施」分类，作为各子类的「公有云/闭源对标」列。清单与 Olares 平替见 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md) 第八节，底稿见 [tech/research/ai-infra.md](/Users/pengpeng/seo/directions/tech/research/ai-infra.md)。
>
> **GPU 算力云（原 A1，CoreWeave/Nebius/Lambda 等）不迁**，保留于本附录（"自有 vs 租算力"对位 Olares One 叙事）。

### A8. OpenClaw 开源生态 / *Claw 自托管栈
> Olares 侧自托管参照，非商业可平替竞品（商业云托管 *Claw 见主清单 #28）。核心平替主张 = `OpenClaw / QwenPaw + NVIDIA NemoClaw 沙箱 + 本地模型`。

**加固栈 / 开源大厂旗舰**
| 名称 | 公司 | 许可 | 定位 |
|------|------|------|------|
| OpenClaw | OpenClaw Foundation | MIT（381K★） | 品类锚：多渠道收件箱个人 AI OS |
| NVIDIA NemoClaw | NVIDIA | Apache-2.0（21K★） | OpenShell 沙箱加固 + 本地 Nemotron 路由；最贴 Olares One |
| QwenPaw（原 CoPaw） | 阿里通义 | Apache-2.0（20K★） | 阿里版 OpenClaw，本地/云双模 + ReMe 记忆 |
| LobsterAI | 网易有道 | 开源桌面壳 | 中国桌面 GUI 版 OpenClaw |
| Hermes Agent | Nous Research | MIT（209K★） | 自进化 skill，常与 OpenClaw 混跑（融资 ~$65M） |

**开源轻量分叉**
NanoClaw（NanoCo $12M seed，容器强隔离，安全叙事最强）、ZeroClaw（Rust ~3.4MB）、PicoClaw（Go，嵌入式）、TrustClaw（Composio，OAuth+沙箱）、Moltworker（Cloudflare Workers 边缘）。

**托管 wrapper（普遍未达标）**
KiloClaw（Kilo $8M，最强 wrapper）、ClawNest / ActivateClaw / SimpleClaw / RapidClaw / MyClaw.ai + 行业 35+ 托管商；腾讯 QClaw、智谱 AutoClaw（大厂本地包装，闭源）。

## B. 达标但与 Olares 无场景交集 / 无平替（远场大 SaaS，#6）
Stripe(支付)、Twilio(CPaaS)、ServiceNow(ITSM)、Workday(HCM)、SAP / Oracle(ERP)、Palo Alto / Zscaler / CrowdStrike / Check Point(安全)、Snowflake(见 A2)、Palantir、Autodesk、Veeva、Akamai、Toast、Dynatrace、JFrog。

> 数据库 / 中间件类（MongoDB、Confluent/Kafka 等）已迁至 tech 方向「数据/中间件」分类，见 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md) 第四节。

> 说明：Salesforce/HubSpot/Shopify/Zendesk/Okta/Datadog/QuickBooks/Vercel/Zoom 等**有开源平替**者已提升进主清单（#41–48、#17、#37 等），不在此列。ServiceNow/Twilio 因无强平替留此（GLPI/iTop、Fonoster/jambonz 仅覆盖子集）。

## C. 未达门槛（发现到但不入选主清单）

### C1. 现有 products.md 有条目、按新门槛应降级观察
| 产品 | 现状 | 说明 |
|------|------|------|
| Udio | 融资 ~$10M | 音乐生成，未达标；保留现有报告，降级观察 |
| Murf AI | 融资 $11.5M | TTS，未达标；保留现有报告，降级观察 |
| Diffbot | 未达标 | 知识图谱/爬取，平替 Firecrawl；降级观察 |

### C2. 语音输入法 / 听写长尾（除 Wispr Flow 外均未达标）
Typeless（注：有同名 messaging API 公司 $26M，勿混）、Aqua Voice、Willow、Superwhisper（自报 7 位数收入）、Monologue(Every)、TalkTastic、Laxis、Voibe、VoiceInk、Camb.ai。

### C3. 设计 Agent 未达标
TapNow（影视 agent，收入 ~$684K，无 VC）、Musho、Flair.ai、Booth.ai、Colater、Spooky、Sivi、Relume、Visily。Motiff 妙多 2026-07-31 停服。

### C4. 编码 / Agent 模型 infra 向
Poolside（估值 $12B，偏企业 infra 非终端 SKU）、Magic.dev（frontier code model 实验室）。开源 CLI（Aider/Goose/Continue.dev/OpenCode）作平替参照。

### C5. 其它未达门槛
Coda、Netlify、Reflect、Saner、Credal、Sudowrite、Frase、Coveo、Scite、Jenni、Copy.ai(贴线)、Cosine、Softgen、Create/Anything、Argil、Riffusion、Rodin/Hyper3D、Haiper(关停)、Replika、Speechify、Retell(融资 $5.1M，Sacra 估 ARR $60M[u])、Chroma、Nomic、Firecrawl、Sync.com、pCloud、Requesty、Flowith(<$20M[u])、MultiOn/Please(口径冲突)、Fathom(临界 ~$22M)、Fireflies(临界)。

## D. 已被收购（以母体计）
Windsurf/Devin→Cognition；Replicate→Cloudflare；Voyage→MongoDB；Jina→Elastic；W&B→CoreWeave；Sana→Workday；Moveworks→ServiceNow；Play.HT/PlayAI→Meta；Tavily→Nebius；Scale AI→Meta(49%)；Adept→Amazon；Weavy→Figma；Galileo AI→Google；Manus→Meta(2026 监管 unwind 中[u])；Limitless/Rewind→Meta；Bee→Amazon；Convergence/Proxy→Salesforce；Superhuman→Grammarly；Hume 团队→Google DeepMind(技术许可)。

## E. 家居 / 可穿戴 IoT 分册（已落地为方向 7）
智能家居 IoT（语音中枢/摄像头安防/家居自动化/媒体）与个人可穿戴/AI 记忆硬件已从本附录**升级为独立方向 7：IoT / 家居 / 穿戴**，清单见 [iot/iot.md](/Users/pengpeng/seo/directions/iot/iot.md)（2 大类/22 细类）、22 份 deep-research 调研底稿见 [iot/research/](/Users/pengpeng/seo/directions/iot/research)（外围 / 敏感 IoT 品类 10-22 已并入硬件章）。原始隐私视角底稿已并入 iot/iot.md 与各品类调研底稿。
