# directions/backlog.md — 全项目 brand/topic-seo 执行队列

> 跨方向的 **brand-seo-research 待跑总队列 + 优先级排序**。回答两件事：**还有多少词要跑**、**按什么顺序跑**。各方向清单（apps.md / products.md / …）是"登记表"，本文件是"排期表"。跑完一项：产出报告 → 回写对应清单 `⬜→✅` → 本文件划掉。
>
> **口径**：1 行清单 = 1 次 Semrush 四阶段报告。开源模型走 [model-seo-research](/Users/pengpeng/seo/.cursor/skills/model-seo-research/SKILL.md)（单列在文末）；其余走 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)。落位与回写规则见该 skill「输出约定」。
> **AS_OF**：2026-07-06（数量随清单变动，改动后请重核）。

## 统计基线（canonical）

| 方向 | 清单登记 | 已做 | 待做 | 类型 | 待做记号 |
|------|---------|------|------|------|---------|
| [market](/Users/pengpeng/seo/directions/market/apps.md) | 175 | 50 | **125** | brand-seo | ⬜ |
| [commerce](/Users/pengpeng/seo/directions/commerce/products.md) | ~235 | 42 | **~193** | brand-seo | ⬜ |
| [hardware](/Users/pengpeng/seo/directions/hardware/devices.md) | 83 行（~57 唯一产品） | 15 唯一（21 行标 ✅，多 SKU 共享报告） | **~62 行** | brand-seo | ⬜ |
| [tech](/Users/pengpeng/seo/directions/tech/tech-stack.md) | 136 | 2 | **134** | brand-seo | ⬜（报告列；Olares 状态列另计） |
| [iot](/Users/pengpeng/seo/directions/iot/iot.md) | 134 | 0 | **134** | brand-seo | ⬜（22 品类 deep-research 已就位） |
| [privacy/services](/Users/pengpeng/seo/directions/privacy/services.md) | 10 | 10 | **0** | brand-seo | — |
| [privacy/landscape](/Users/pengpeng/seo/directions/privacy/landscape.md) | ~39 子方向 | 0 | **~39** | topic-seo | ⬜ |
| **合计（brand/topic-seo）** | | **~119** | **~687** | | |
| [model](/Users/pengpeng/seo/directions/model/models.md) | 72 family | 0 | **72** | model-seo | ⬜ |

**口径说明**：
- market `reports/` 另有 `seafile.md`、`yunohost.md` 两份"个人云平台竞品"（Nextcloud 同类），不进 apps.md 应用计数。
- commerce `reports/` 文件数（54）> ✅ 产品行（42）：含 appendix 9 份（groq/huggingface/modal/pinecone/together-ai/voyage-ai/scale-ai/murf-ai/privacyguides）+ 平替侧报告（continue-dev/vaultwarden/keepassxc/obsidian/logseq/autogpt）——这些**不占产品 ✅ 行**，是有意为之。
- hardware 行级 ✅（21）> 唯一报告（15）：Apple×4→1、UGREEN×2→1、极空间×2→1、Zima×2→1 共享报告；`_archived/` 19 份旧品牌报告不计入待跑。
- tech 有**两列**：`Olares 状态`（✅内置/🟡部分/⬜缺口，31/34/71）与 `SEO 报告`（本队列口径，仅 2 篇）。优先打「✅内置 + 报告⬜」。
- [reference/olares-500-keywords-analysis-2026-07-03.md](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md) 是选词外挂，其"194 份报告"为旧基线，以本表为准。

---

## 优先级分层（机会矩阵口径）

排序逻辑：**500 词 A+/A 锚词** > **scenarios Q2 可兑现** > **补齐已有 ✅ 报告簇** > **deep-research 已筛词（Semrush 成本低）** > 长尾。

### P0 — 机会矩阵首发（逐条点名）

**market**（预期落 `market/reports/<slug>.md`）

| 目标 | 机会信号 | slug |
|------|---------|------|
| Vane | `perplexity alternative` KD≈11（A+）；Perplexica 平替 | vane |
| Mattermost | 场景 6 Workspace；`mattermost alternative` KD≈10 | mattermost |
| AFFiNE | `notion alternative` 880/mo；Notion/Miro 平替 | affine |
| Plane | JIRA/Linear/Asana 替代入口 | plane |
| LocalAI | OpenAI/Claude 本地替代叙事 | localai |
| Obsidian LiveSync | `obsidian self hosted sync` 70/mo | obsidian-livesync |
| OnlyOffice | 与已有 Nextcloud 报告联动 | onlyoffice |
| Xinference | 引擎组唯一缺口（Ollama/vLLM/SGLang/llama.cpp 已完） | xinference |
| FastGPT | 补 RAG 平台矩阵（Dify/Flowise/RAGFlow 已完） | fastgpt |
| Langfuse | LLM 工程/观测，补 Agent 栈 | langfuse |
| Uptime Kuma | 经典 self-hosted 监控，易出 alternative 词 | uptime-kuma |
| Teable | `airtable alternative self hosted`（NocoDB 已完） | teable |
| FreshRSS | 轻量 self-hosted RSS，KD 友好 | freshrss |

**commerce**（预期落 `commerce/reports/<大类>/<细类>/<slug>.md`）

| 目标 | 机会信号 | 细类 |
|------|---------|------|
| Google Gemini | 对标 OpenAI/Anthropic 已 ✅，最大缺口 | #1 前沿实验室 |
| Claude Code | 高热度编码 Agent（注意与 market/claude-code 去重） | #21 编码 Agent |
| Manus | DeerFlow/OpenClaw 叙事核心 | #27 通用 Agent |
| Genspark | OpenClaw 商业对标 | #28 Personal AI |
| n8n（云版） | Zapier 已 ✅；自托管双形态 | #26 自动化 |
| Supabase | 强自托管叙事 | #25 BaaS |
| Fireflies.ai | Whisper 栈（Otter 已 ✅） | #15 会议转录 |
| Sora | Wan 平替；Runway 等已 ✅ | #8 视频 |
| Bolt.new | Lovable 已 ✅，补对比词 | #22 vibe coding |
| Adobe Firefly | ComfyUI 平替链 | #7 图像 |

**hardware**（预期落 `hardware/reports/<组>/…/<slug>.md`）

| 目标 | 机会信号 |
|------|---------|
| GMKtec EVO-X2 | `gmktec evo-x2` 4,400/mo |
| Framework Desktop | Linux/Strix Halo 叙事 |
| ROG NUC 16 (2026) | `olares one vs rog nuc` |
| ~~Legion Pro 7i Gen10~~ | ~~同 GPU、$3,999 对标 Olares One~~ ✅ [报告](/Users/pengpeng/seo/directions/hardware/reports/02-5090-laptops/lenovo-legion.md) |
| HP ZBook Ultra G1a | `strix halo laptop` KD9 |
| ~~Minisforum N5 Pro~~ | ~~AI NAS + OCuLink + 4090 实测~~ ✅ [报告](/Users/pengpeng/seo/directions/hardware/reports/01-ai-soc/strix-halo/minisforum.md) |
| 飞牛 fnOS | 组八唯一缺报告 NAS OS |
| ASUS Ascent GX10 | `dgx spark alternative` 价位带 |

### P1 — research 就绪（deep-research 已筛词，Semrush 成本低）

**iot**（预期落 `iot/reports/<细类>/<slug>.md`）：Ring · Plaud · Sonos · Oura · Reolink · Alexa(Echo) · Philips Hue · Roborock · Google Nest Cam · Ray-Ban Meta
> 核心词方向：`ring alternative`（无订阅摄像头）、`plaud alternative`（Personal Agent）、`oura ring alternative`、`philips hue without account`、`valetudo`（去云）、`ray-ban meta alternative`（第一视角隐私）。iot 品牌报告与 market（Frigate/HA）已有报告去重。

**privacy/landscape**（topic-seo，预期落 `privacy/reports/<分类>/<slug>.md`）：data sovereignty · own your data · data localization · ChatGPT training data opt out · degoogle · gdpr compliant ai
> 与 privacy/services.md 的品牌报告互补：services 走产品 brand-seo，landscape 借合规/事件/概念热度做话题内容。

### P2 — 明星大词（高量难词，权威内容，按方向池化）

commerce/market 剩余高价值品牌：Perplexity 类簇补齐、Notion 生态、Runway/Pika 视频簇、Supabase/Appwrite BaaS 簇、Metabase/Appsmith/NocoBase 低代码簇、Sonarr/Radarr *arr 生态等。逐批从各方向清单 ⬜ 行选取，量大 KD 高，作 3–6 月权威页。

### P3 — 长尾 / SKU（按方向池化）

- **tech 剩余 ~134**：先打「✅内置 + 报告⬜」——PostgreSQL(+pgvector/Citus) · K3s · vLLM · MinIO · JuiceFS · LiteLLM · NATS · Authelia · HAMi · Mem0；其余按 headscale/frp 模板批量。
- **hardware 剩余 SKU**：跟 Olares One / 场景 8 企业词绑定的先做，其余长尾。

### 排除项

model → 走下方 model-seo 队列；hardware `_archived/` 19 份不计；重复行先 dedup（见各清单交叉引用注）。

---

## model-seo 队列（走 model-seo-research，非 brand-seo）

72 family 全部待做，`reports/` 现为空。首发 12（预期落 `model/reports/<章>/<slug>.md`）：

| 目标 | 章 | 闭源对标/联动 |
|------|-----|--------------|
| Qwen 3.6 | 01-llm | GPT/Claude；Olares 主力 |
| Qwen3-Coder | 01-llm | Claude Code（commerce 侧） |
| DeepSeek V4 | 01-llm | 长上下文 agent |
| FLUX.2 | 02-image | Midjourney ✅ |
| Wan 2.2 | 03-video | Runway/Sora 链 |
| TRELLIS.2 | 04-3d | Meshy/Tripo ✅ |
| Kokoro | 05-tts | ElevenLabs ✅ |
| Whisper | 06-stt | Deepgram/AssemblyAI ✅ |
| Qwen3-Embedding | 07-embedding | Cohere ✅ |
| BGE-M3 | 07-embedding | RAG 主力 |
| PaddleOCR-VL | 08-ocr | 文档理解 |
| ACE-Step 1.5 | 10-music | Suno/Udio ✅ |

> commerce 与 model 分工：同一闭源对标可两侧各一篇——commerce 做 `Google Gemini API` 商业站，model 做 `run Qwen 3.6 locally` 权重词，skill 不同。

---

## 执行约定

1. 一次一批（建议 8–15 项），跑完回写清单 `⬜→✅` 并在本表标注进度。
2. 落位/命名/回写细则以 [brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)「输出约定」为准。
3. 流量/关键词数字必须来自真实 Semrush 调用；前置项目理解标注公开来源。
4. 重写已存在报告前先读旧报告与相关洞见，保留有价值的历史判断。
