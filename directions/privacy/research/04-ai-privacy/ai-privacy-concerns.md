# AI 隐私 concern 格局（privacy 方向 · 分类 04）

> 研究日期: 2026-07-06 | 来源: task-04（10 源）| 模式: Lightweight | AS_OF: 2026-07-06 | 官方源占比: ~50% | 视角: 本地/端侧 AI + Olares 落点
>
> 分类 = AI 带来的**隐私 concern**（训练数据合法性、记忆化/泄露、聊天机器人默认训练、监管行动、端侧 vs 云、AI Act 透明度）。巨头层面见分类 05。发现笔记见 [ai-privacy-concerns.notes/](/Users/pengpeng/seo/directions/privacy/research/04-ai-privacy/ai-privacy-concerns.notes)。

## 摘要
AI 隐私的核心事实有三：(1) **训练合法性未定**——意大利 Garante 对 OpenAI 的 €15M 罚款（欧洲唯一针对生成式 AI 发布阶段的最终 GDPR 执法）于 2026-03 被罗马法院**以管辖权技术性撤销**，实质争议未在法院层面定论 [1][9]；EDPB Opinion 28/2024 确认训练可用合法利益但**不能默认**，须三步测试 [2]。(2) **记忆化是能力问题，非边缘案例**——2026 Stanford/Yale 研究可从生产 LLM 提取长篇版权书籍，Gemini 2.5 Pro / Grok 3 **无需 jailbreak** 即达 ~77% / ~70% near-verbatim recall [4]。(3) **主流聊天机器人个人版默认用于训练**（ChatGPT/Gemini/Copilot），须手动 opt-out [5][6][7]。**Olares 落点极强且差异化**：本地推理（Ollama/vLLM）+ RAG on 自有数据 = 无第三方训练管线、权重不含他人 PII/版权语料、数据不出设备。诚实边界：本地并非零风险（见争议）。

## 1. 训练数据合法性与监管
- **Garante €15M（2024-11）**：指控 2022-11 至 2023-03 训练无 GDPR 合法依据、透明度不足、泄露未通知、无年龄验证；首次动用 6 个月全国宣导令 [1]。
- **撤销（2026-03-18，罗马法院 4153/2026）**：OpenAI 2024-02 在爱尔兰设 EU 主体后，Garante 失去 one-stop-shop 管辖权；法院**未就实质违法作出裁决** [1][9]。
- **EDPB Opinion 28/2024**：训练/部署原则上可用 Art.6(1)(f) 合法利益，但须三步测试 + 数据主体合理预期 + opt-out 等缓解；非法训练的模型若未充分匿名化，部署合法性亦受影响 [2]。
- **noyb 投诉**：ChatGPT 无法更正个人错误信息、无法说明训练来源，违反 Art.5(1)(d) 与 Art.15；挪威追加投诉 pending [3]。

**置信度: High**（监管官方 + Reuters）。

## 2. 记忆化 / 训练数据提取
- 2026 Stanford/Yale：即便有模型级 + 系统级防护，仍可从 Claude 3.7 Sonnet、GPT-4.1、Gemini 2.5 Pro、Grok 3 提取长篇版权书籍；Gemini/Grok 无需 jailbreak 即达 ~77%/~70%，jailbreak 后 Claude 达 95.8% [4]。
- 差分隐私/低成员推断区分度**不足以**保证防提取；黑盒 API 仍可通过 Best-of-N jailbreak + 迭代 continuation 触发记忆化 [4]。

**置信度: High**（学术，90 天负责任披露）。

## 3. 聊天机器人默认训练与 opt-out
| 产品 | 个人版默认 | 关闭方式 | 企业/API | 来源 |
|------|-----------|----------|----------|------|
| ChatGPT | **默认用于训练** | Data Controls 关 "Improve the model"，或 Temporary Chat | Team/Enterprise/API 默认不训练 | [5] |
| Gemini | **默认**用 Activity 改进（含训练） | 关 Gemini Apps Activity / Temporary Chat（仍留 72h） | — | [6] |
| Copilot | 个人版**默认开启**（EEA/UK 例外） | Settings > Privacy opt-out | Business/Enterprise 不受影响 | [7] |

**置信度: High**（厂商官方政策页）。

## 4. EU AI Act 透明度（2026-08-02 起）
- Art.50：聊天机器人须披露 AI 交互；合成内容须可检测标记；情绪识别/生物特征分类须告知；深伪与公共利益 AI 文本须标注；职场/教育情绪识别已在 Art.5 禁止 [8]。

**置信度: Medium**（律所解读，日期以官方为准）。

## 5. 候选关键词
- 信息型：`is ChatGPT GDPR compliant`、`does ChatGPT use my data for training`、`LLM memorization`、`AI training data privacy`、`EU AI Act chatbot disclosure`。
- 意图型：`ChatGPT training data opt out`、`Gemini privacy settings`、`Copilot opt out training`、`local LLM vs cloud AI privacy`、`on device AI privacy`。
- Olares 结合（差异化）：`private local AI agent`、`self hosted LLM privacy`、`RAG on your own data`、`Ollama privacy`、`AI without sending data to cloud`。

## 6. 核心争议 / 反方
**核心争议**：(A) 本地更隐私（数据不出设备、无默认训练、用户控 RAG）[5][7] vs (B) 本地并非零风险（本地权重仍可 memorization 用户粘贴的敏感文本；补丁需自维护；小模型能力弱促使回退云；Apple PCC 2026 延伸至 Google Cloud + Nvidia，"隐私云"边界被质疑）[4][10]。(C) 监管已允许训练（EDPB 合法利益 + opt-out）[2] vs (D) 执法真空（€15M 撤销、noyb pending、opt-out 默认关、政策频繁变更）[1][3][7]。

**反方解释**：对能力要求高的任务，前沿云模型体验显著优于本地小模型；"本地=更好"对普通用户不总成立。诚实口径：Olares 提供**数据路径更短、无第三方训练**的选择，但不宣称本地模型在质量或安全上全面碾压云。

## 7. 局限性与未来方向
- **局限**：FTC 对 OpenAI/Amazon AI 数据调查最终处置、Copilot vs GitHub Copilot 政策差异单一权威页、AI Act Art.5 与 GDPR 生物识别判例级交叉未深读 [task-04 Gaps]。
- **未来方向**：写"云 AI 数据训练 opt-out 全指南"支柱文；对 `local LLM privacy`、`RAG own data` 做量化 + landing。

## 参考文献
[1] Garante. "ChatGPT, Provvedimento n. 755". official. As Of: 2024-12. https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432
[2] EDPB. "Opinion 28/2024 on data protection aspects of AI models". official. As Of: 2024-12. https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
[3] noyb. "ChatGPT provides false information about people". advocacy. As Of: 2024-04. https://noyb.eu/en/chatgpt-provides-false-information-about-people-and-openai-cant-correct-it
[4] arXiv (Stanford/Yale). "Extracting books from production language models". academic. As Of: 2026-01. https://arxiv.org/html/2601.02671v1
[5] OpenAI. "How your data is used to improve model performance". vendor-policy. As Of: 2026-03. https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/
[6] Google. "Gemini Apps Privacy Hub". vendor-policy. As Of: 2025-2026. https://support.google.com/gemini/answer/13594961?hl=en-GB
[7] Microsoft. "Microsoft Copilot privacy controls". vendor-policy. As Of: 2025-2026. https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-privacy-controls
[8] Sidley. "EU AI Act Transparency Obligations: 2 August 2026". law-firm. As Of: 2026-06. https://datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026/
[9] Reuters. "Italian court scraps 15-million-euro fine on OpenAI". journalism. As Of: 2026-03. https://www.reuters.com/technology/italian-court-scraps-15-million-euro-privacy-watchdog-fine-chatgpt-maker-openai-2026-03-19/
[10] Apple. "Private Cloud Compute: A new frontier for AI privacy in the cloud". vendor-security. As Of: 2024-2026. https://security.apple.com/blog/private-cloud-compute/
