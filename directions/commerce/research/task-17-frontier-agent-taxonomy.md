# dig-17 · 前沿实验室 agent 品类归属 · 归类建议

**AS_OF=2026-07-04** · 产出归类建议+佐证，供重写落稿。

## Sources
- S1 openai.com/index/codex-for-almost-everything/（官方，2026-04-16）
- S2 developers.openai.com/codex/app/computer-use（官方文档，2026）
- S3 openai.com/index/work-with-codex-from-anywhere/（官方，2026-05-14）
- S4 openai.com/index/introducing-chatgpt-agent/（官方，2025-07-17）
- S5 anthropic.com/product/claude-cowork（官方产品页，2026）
- S6 claude.com/blog/the-claude-cowork-product-guide（官方，2026-06-05）
- S7 claude.com/resources/tutorials/choosing-between-claude-cowork-or-chat（官方，2026）
- S8 claude.com/product/design（官方产品页，2026）
- S9 claude.com/blog/claude-design-stays-on-brand-for-daily-work（官方，2026-06-17）
- S10 anthropic.com/news/developing-computer-use（官方，2024-10-22）
- S11 open-design.ai / github.com/nexu-io/open-design（Apache-2.0，2026-07-04）

## 归类建议

### 1. OpenAI Codex / Codex CLI
- **是什么**：OpenAI 开发者 agent 套件——CLI(Apache-2.0 开源)+Desktop+IDE 扩展+Cloud threads+Automations/Memory；2026-04 增 Computer Use(本地 GUI)、in-app browser、图像生成、90+ plugins；2026-05 ChatGPT 移动 app 作遥控面（执行/凭证留本机）。
- **当前定位**："Codex for (almost) everything"，但叙事仍锚定 SDLC/开发者工作流；与 ChatGPT superapp 是**身份/计费/移动遥控统一，非合并 SKU**。
- **建议归类**：**主列 `#23 AI 编码 Agent/CLI`（单行）**；**不**在 #26 通用 Agent 另起一行（否则与 ChatGPT Agent/Deep Research 重复计数）。在 Codex 行**备注**交叉标注：`CLI+Desktop+Cloud · Computer Use(dev) · ChatGPT mobile 遥控`。
- **平替**：OpenCode / Aider。

### 2. Claude Cowork
- **是什么**：Anthropic 面向**非开发者知识工作者**的 agentic 生产力层（Claude Desktop 独立模式）；本机 agent loop + 隔离 Linux VM；可选 Computer Use 操作桌面 app。
- **关系**：与 Chat/Claude Code/Claude Design **同引擎、不同界面与任务域**。Cowork 产出 doc/xlsx/运营交付物；Design 产出视觉稿/原型；不互斥不合并。
- **建议归类**：**主列 `#26 通用/Deep Research Agent`**；行名改为 **Claude Cowork**（去掉 "+ Computer Use" 后缀，Computer Use 降为内嵌能力备注）。不单列"生产力/知识"agent 主类。
- **平替**：Hermes Agent（+ DeerFlow 2.0 用于 DR 向）。

### 3. Claude Design
- **是什么**：Anthropic Labs 托管 AI 设计 agent（beta，claude.ai/design + Desktop 侧栏）：brief→可交互原型/线框/pitch deck/营销物料；支持 design system 导入、canvas 精修、导出 PDF/PPTX/HTML、connector 发往 Canva/Adobe/Vercel/Lovable。2026-04-17 research preview，Opus 4.7 驱动，首周 100 万+ 用户。与 Claude Code 双向 `/design-sync` `/design`。
- **建议归类**：**主列 `#13 AI 设计 Agent`，新增一行**（现稿未收录）。不放 #24 vibe coding。
- **平替**：**Open Design**（open-design.ai / nexu-io/open-design，Apache-2.0，local-first BYOK，官方自称 Claude Design alternative）+ **Jaaz**（Market 已有）。Penpot/ComfyUI 作设计协作/工作流补充，非直接平替。

## Anthropic & OpenAI agent 家族边界（文档可用一句说明）
- **Anthropic**：同一 Claude 模型栈按**交付物类型**拆四条消费级 agent 面——Chat(对话)/Claude Code(代码终端)/Claude Cowork(知识工作文件与跨 app 交付)/Claude Design(视觉原型 Deck)；**Computer Use 是横切能力**（API 给开发者；Cowork/Code 桌面产品内可选），非并列的第五条产品线。
- **OpenAI**：按**运行环境与用户**拆两条 agent 主线——Codex(开发者本机/CLI/Desktop，含 Computer Use，ChatGPT app 仅遥控) 与 ChatGPT Agent(ChatGPT 内云端虚拟计算机，2025-07 合并 Operator[已关停]+Deep Research)。Codex 未与 ChatGPT Agent 合并 SKU，清单里勿双计。

## 落稿修改摘要
| 产品 | 现稿位置 | 建议 |
|------|----------|------|
| OpenAI Codex | #23 ✓ | 保留主类；备注加 Computer Use + ChatGPT 遥控；不加 #26 第二行 |
| Claude Cowork | #26 行名 "Cowork + Computer Use" | 改为 Claude Cowork；Computer Use→备注 |
| Claude Design | 缺失 | 新增至 #13；平替 Open Design + Jaaz |

## Gaps
- Codex 无官方独立 ARR；周活 300万→500万+ 第三方 [unverified]。
- Open Design GitHub stars 第三方口径 57K–74K 波动 [unverified]（SEO 以仓库 commit/release 为准）。
- Penpot 报告标题含 "Open Design" 易混，commerce 侧须明确 **Penpot ≠ Open Design**。
