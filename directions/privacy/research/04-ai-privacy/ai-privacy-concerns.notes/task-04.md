---
task_id: 04
role: AI 隐私与数据治理分析师
status: complete
sources_found: 10
---

## Sources
[1] COMUNICATO STAMPA - ChatGPT, il Garante privacy chiude l'istruttoria (Provvedimento n. 755) | https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432 | Source-Type: official | As Of: 2024-12 | Authority: 10/10
[2] Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models | https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf | Source-Type: official (EDPB) | As Of: 2024-12 | Authority: 10/10
[3] ChatGPT provides false information about people, and OpenAI can't correct it | https://noyb.eu/en/chatgpt-provides-false-information-about-people-and-openai-cant-correct-it | Source-Type: advocacy/complainant | As Of: 2024-04 | Authority: 8/10
[4] Extracting books from production language models | https://arxiv.org/html/2601.02671v1 | Source-Type: academic (Stanford/Yale) | As Of: 2026-01 | Authority: 9/10
[5] How your data is used to improve model performance | https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/ | Source-Type: vendor policy | As Of: 2026-03 | Authority: 9/10
[6] Gemini Apps Privacy Hub | https://support.google.com/gemini/answer/13594961?hl=en-GB | Source-Type: vendor policy | As Of: 2025-2026 | Authority: 9/10
[7] Microsoft Copilot privacy controls | https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-privacy-controls | Source-Type: vendor policy | As Of: 2025-2026 | Authority: 9/10
[8] EU AI Act Transparency Obligations: Preparing for Compliance by 2 August 2026 | https://datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026/ | Source-Type: law-firm analysis | As Of: 2026-06 | Authority: 8/10
[9] Italian court scraps 15-million-euro privacy watchdog fine on ChatGPT-maker OpenAI | https://www.reuters.com/technology/italian-court-scraps-15-million-euro-privacy-watchdog-fine-chatgpt-maker-openai-2026-03-19/ | Source-Type: journalism | As Of: 2026-03 | Authority: 9/10
[10] Private Cloud Compute: A new frontier for AI privacy in the cloud | https://security.apple.com/blog/private-cloud-compute/ | Source-Type: vendor security | As Of: 2024-2026 | Authority: 8/10

## Findings
- 意大利 Garante 于 2024-11 对 OpenAI 开出 €15M 罚款并责令 6 个月全国媒体宣导，核心指控包括：2022-11 至 2023-03 期间以用户/非用户个人数据训练 ChatGPT 却**未确立 GDPR 合法依据**、透明度不足、2023-03 数据泄露未通知、无年龄验证；此为欧洲迄今唯一针对生成式 AI 公开发布阶段的**最终 GDPR 执法决定**。[1]
- 2026-03-18 罗马法院 judgment 4153/2026 **撤销**该决定：OpenAI 2024-02-15 在爱尔兰设立 EU 主体后，意大利 Garante 失去 one-stop-shop 管辖权；法院**未就实质违法与否作出裁决**，仅因程序/管辖问题作废。[1][9]
- EDPB Opinion 28/2024：AI 模型训练/部署**原则上可用** Art. 6(1)(f) 合法利益，但**不能作为默认依据**；须完成三步测试（利益合法明确、处理必要且比例、平衡测试不压倒数据主体权利），并考虑数据主体合理预期、数据来源与 opt-out 等缓解措施；unlawfully 训练开发的模型若未充分匿名化，部署合法性亦受影响。[2]
- 2026 年 Stanford/Yale 研究证实：即便有模型级+系统级防护，仍可从 **Claude 3.7 Sonnet、GPT-4.1、Gemini 2.5 Pro、Grok 3** 等生产 LLM 中提取长篇受版权书籍；Gemini 2.5 Pro / Grok 3 **无需 jailbreak** 即可达 ~77% / ~70% near-verbatim recall（Harry Potter 测试）；jailbreak 后 Claude 可达 95.8%。[4]
- 同一论文指出：差分隐私/成员推断低区分度**不足以**保证防提取；生产 API 的黑盒访问仍可通过 Best-of-N jailbreak + 迭代 continuation 触发记忆化输出。[4]
- **ChatGPT 个人版默认用于训练**；可在 Settings > Data Controls 关闭 "Improve the model for everyone"，或使用 Temporary Chat（不进历史、不训练）；Team/Enterprise/API **默认不训练**。[5]
- **Gemini 默认**用 Activity 改进 Google AI（含训练）；Temporary Chat 或关闭 Gemini Apps Activity 可停止；Temporary Chat 仍保留 72 小时供响应与安全处理。[6]
- **Microsoft Copilot 个人版默认开启** conversation/voice training（EEA/UK 等地区例外）；Settings > Privacy 可 opt-out；Copilot Business/Enterprise 不受 GitHub 2026-04-24 起的 Free/Pro 训练政策影响。[7]
- noyb 2024-04 向奥地利 DSB 投诉：OpenAI 无法更正 ChatGPT 关于个人的错误信息、无法说明训练来源，违反 Art. 5(1)(d) 准确性与 Art. 15 访问权；2025-03 另向挪威 Datatilsynet 投诉虚假诽谤输出（pending）。[3]
- **EU AI Act Art. 50** 自 2026-08-02 起适用：聊天机器人须披露 AI 交互（Art. 50(1)）；合成内容须可检测标记（50(2)）；部署情绪识别/生物特征分类须告知当事人（50(3)）；深伪与公共利益 AI 文本须标注（50(4)）；职场/教育场景情绪识别已在 Art. 5 **禁止**。[8]

## Deep Read Notes
### Source [1]: Garante Provvedimento n. 755 / Press Release
Key data: fine €15M; 6-month institutional campaign (Art. 166(7) Privacy Code, 首次动用); violations: Art. 33 breach notification, Art. 5/6/12/13/24/25; training without legal basis Nov 2022–Mar 2023; case forwarded to Irish DPC after OpenAI Ireland establishment; Decision temporarily removed from website after Rome Court judgment 4153/2026 (18 Mar 2026)
Key insight: 欧洲 AI 训练合规执法的"标杆案件"在 2026 年被管辖权技术性撤销，实质 GDPR 争议（训练合法依据）仍未在法院层面定论；执法 gap 引发"先调查、后迁册、再作废"批评。
Useful for: SEO 角度——"ChatGPT GDPR fine Italy""OpenAI training data legal basis EU"；对比 Olares 本地推理无第三方训练管线。

### Source [2]: EDPB Opinion 28/2024
Key data: adopted 17 Dec 2024; requested by Irish DPC; anonymity requires negligible likelihood of (1) direct/probabilistic extraction from model AND (2) obtaining personal data via queries; legitimate interest requires documented 3-step test; mitigating measures include pseudonymization, transparency, opt-out; unlawful development taints deployment unless model anonymized
Key insight: EU 监管框架并非"禁止 AI 训练"，而是要求 case-by-case 合法利益评估 + 数据主体合理预期；大规模 web scrape 训练在平衡测试中高风险。
Useful for: 内容分类"GDPR AI training legal basis""legitimate interest LLM"；Olares 叙事可强调：用户自有数据 RAG 可走合同/同意，且不进入 frontier 预训练池。

### Source [4]: Extracting books from production language models (arXiv 2601.02671)
Key data: experiments Aug–Sep 2025; 90-day responsible disclosure; 4 production LLMs tested; nv-recall metric; Gemini/Grok Phase-1 no jailbreak; Claude jailbroken 95.8% HP extraction; GPT-4.1 resists after ch.1 (~4%); connects to copyright/GEMA v. OpenAI Germany ruling
Key insight: "云 LLM 有安全护栏就不会泄露训练数据"已被实证推翻；记忆化是 capability 问题，非仅 adversarial edge case。
Useful for: "LLM data leakage""ChatGPT memorization privacy""cloud AI training data risk"高意图词；Olares 落点：本地 Ollama/vLLM + 仅 RAG 自有文档，权重不含他人 PII/版权语料。

## Gaps
- **相反主张 A（本地更隐私）**：端侧/自托管 LLM 数据不出设备、无默认训练、用户控 RAG 源——Olares 核心叙事 [5][7] vs **相反主张 B（本地并非零风险）**：本地模型权重仍可能 memorization 用户粘贴的敏感文本；模型更新/补丁需用户自行维护；小模型能力弱可能促使用户回退云 API；Apple PCC 2026 已延伸至 Google Cloud + Nvidia，"隐私云"边界被质疑 [4][10]。
- **相反主张 C（监管已允许训练）**：EDPB 确认 legitimate interest 可用，配合 opt-out/透明度后云 AI 可合规——不等于"云 AI 必然违法" [2] vs **相反主张 D（执法真空）**：Garante €15M 被撤销、noyb 投诉 pending，欧洲对 frontier 训练的实际处罚仍稀缺，用户 opt-out 默认关、政策频繁变更（GitHub Copilot 2026-04 默认训练）[1][3][7]。
- **待补源**：FTC 2024–2026 对 OpenAI/Amazon 等 AI 数据收集调查最终处置；Copilot 与 GitHub Copilot 政策差异的 Microsoft 主站单一权威页；EU AI Act Art. 5 情绪识别禁令与 GDPR 生物识别条款的判例级交叉引用。

## Olares SEO 内容分类建议（蒸馏延伸）
| 主题簇 | 代表 query 意图 | Olares 落点 |
|--------|----------------|-------------|
| 云 AI 数据训练 opt-out | ChatGPT training data opt out / Gemini privacy settings | 本地 Agent：无对话上传训练 |
| GDPR / 执法 | OpenAI GDPR fine / AI training legal basis EU | 数据主权 + 不依赖 third-party 训练池 |
| 记忆化/泄露 | LLM memorization / training data extraction | 自托管权重 + RAG 仅索引用户 Files |
| 端侧 vs 云 | local LLM vs cloud AI privacy / on-device AI | Ollama/vLLM on Olares；对比 Apple PCC 混合架构 |
| EU AI Act 透明度 | AI Act chatbot disclosure / deepfake labeling | 自部署 chatbot 仍须 Art. 50，但数据处理路径更短 |

## END
