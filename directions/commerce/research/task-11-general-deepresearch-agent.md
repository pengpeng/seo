# dig-11 · 通用自主 Agent + Deep Research Agent 赛道 · 发现蒸馏笔记

**AS_OF=2026-07-04** · 对标锚点：Olares **DeerFlow 2.0**（open-source super agent harness for deep research）。只做发现+财务，不做最终分类。

## Sources（节选）
TechFundingNews / TechCrunch / BusinessWire / 官方博客(OpenAI/Google/Anthropic) / Sacra / PitchBook / 36Kr / Caixin 等。

## Products（类型：general｜deep-research｜both；门槛：ARR>$50M｜估值>$200M｜融资>$20M｜大厂旗舰）

| 名称 | 公司 | 域名 | 定位 | 类型 | 财务 | 命中 |
|------|------|------|------|------|------|------|
| **Manus** | Butterfly Effect | manus.im | 通用自主 agent，端到端交付 | general | ARR $400–500M；收购价 ~$2B(Meta unwind 中)；融资 ~$85M | 全中 |
| **Genspark** | Genspark | genspark.ai | all-in-one agentic workspace | general | ARR $250M+；估值 $2.6B；融资 $645M | 全中 |
| **ChatGPT Agent** | OpenAI | chatgpt.com | Operator+Deep Research 统一 agent | both | 母公司 $852B 估值/~$25B ARR | 大厂旗舰 |
| **OpenAI Deep Research** | OpenAI | openai.com | 引用报告型 DR（并入 ChatGPT Agent） | deep-research | 同上 | 大厂旗舰 |
| **Gemini Deep Research / Max** | Google | gemini.google.com | 自主规划-执行-合成 research agent | deep-research | 大厂旗舰 | 大厂旗舰 |
| **Claude Cowork + Computer Use** | Anthropic | claude.com | computer-use agent + agentic 生产力层 | general | run-rate ~$30B；估值 $380B | 大厂旗舰 |
| **Perplexity Computer** | Perplexity | perplexity.ai | 云端 general digital worker | general | ARR $450M+；估值 ~$20–22.6B；融资 ~$1.72B | 全中 |
| **Perplexity Deep Research/Labs** | Perplexity | perplexity.ai | 搜索侧 DR | deep-research | 同上 | 继承 |
| **ARI** | You.com | you.com | 企业级 deep research agent | deep-research | 估值 $1.5B；融资 $195M | 估值✓融资✓ |
| **Skywork** | 昆仑万维 | skywork.ai | AI Workspace Agents + DeepResearch | both | 实体估值 ¥149B(~$20B+)；ARR 口径混杂 | 估值✓ |
| **Kimi Work / Researcher** | Moonshot | kimi.com | 桌面 general agent(300并发 sub-agent) | both | ARR >$200M；估值 $20B；融资 ~$3.9B | 全中 |
| **MiniMax Agent** | MiniMax(HK:0100) | minimax.io | agent workspace | general | ARR ≥$300M；市值 ~$32B；融资 ~$1.15B | 全中 |
| **AutoGLM/企业 Agent** | Zhipu(HK:2513) | z.ai | 手机+企业长链 agent | general | 市值 >$112B；API ARR ~$230M | 估值✓ |
| **DeepSeek Agent 方向** | DeepSeek | deepseek.com | V3/R1 模型+产品化 agent | both | 估值 >$50B；融资 $7.4B+ | 估值✓融资✓ |
| **Runner H / Surfer H** | H Company | hcompany.ai | 欧洲通用编排 agent | general | 融资 $220M seed；估值 $370M~传闻 $2B | 融资✓ |
| **SuperNinja** | NinjaTech | myninja.ai | 低价 general agent | general | 融资 $27–28M | 融资✓ |
| **Fellou** | ASI X | fellou.ai | agentic browser(Deep Search+Action) | both | 融资 >$30M(PitchBook $40.4M) | 融资✓ |
| **Simular** | Simular | simular.ai | Mac/Win 桌面 general agent | general | 融资 ~$27M | 融资✓ |
| **Parallel Web Systems** | Parallel | parallel.ai | agent 专用 web search/research API | deep-research(infra) | 估值 $2B；融资 $230M | 估值✓融资✓ |
| **TinyFish** | TinyFish | tinyfish.ai | enterprise web agent 基建 | general | 融资 $47M | 融资✓ |
| **Copilot Researcher** | Microsoft | microsoft.com | M365 内 multi-step DR agent | deep-research | 大厂旗舰 | 大厂旗舰 |
| **Amazon Nova Act** | AWS | aws.amazon.com/nova/act | 生产级 browser/UI workflow agent | general | 大厂旗舰 | 大厂旗舰 |
| **Please(原 MultiOn)** | Please | multion.ai | 消费 web agent | general | $20M A @ $100M(口径冲突) | 融资✓[u] |
| **Imbue** | Imbue | imbue.com | reasoning 模型→通用 agent(lab) | general | 融资 $220M @ >$1B | 估值✓融资✓ |

**已关停/被收购**：Project Mariner(Google，2026-05 EOL→Gemini Agent)、Convergence/Proxy(→Salesforce Agentforce)、Adept(→Amazon)。

## 平替（Olares 侧）
- **DeerFlow 2.0**（开源 super agent harness：sub-agent+memory+sandbox+skills，可自托管）
- **Hermes Agent**（成长型 agent，可作通用助理平替）

## Gaps / 边界剔除
- **剔除（属别类）**：编码 Agent(Devin/Claude Code/Codex/Jules)、企业客服/CX Agent(Sierra/Decagon/Kore.ai)、个人 AI 助手(OpenClaw/Siri)、纯自动化(Zapier/n8n/UiPath)、vertical research(Harvey/Elicit)。
- **财务疑点**：Skywork vs 昆仑集团 ARR $800M+ 口径混杂（含 DramaWave）；Manus Meta $2B 处监管 forced unwind；Flowith 千万美元 seed 很可能 <$20M 未达标；MultiOn 融资 $4M vs $20M 冲突。
- **DeerFlow 2.0**：GitHub v2.0.0(2026-06-25)，与 v1.x DR 分支并存；Olares 对标 2.0 super harness。
- **待补搜**：字节豆包/腾讯混元/百度文心/华为盘古 Agent、Mistral Agents API、Reflection AI。
