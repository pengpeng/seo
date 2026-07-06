---
task_id: 05
role: 大型科技公司隐私与监控分析师
status: complete
sources_found: 15
---

## Sources
[1] Numbers and Figures | GDPR Enforcement Tracker Report 2025/2026 | https://cms.law/en/gbr/publication/gdpr-enforcement-tracker-report/numbers-and-figures | Source-Type: legal/industry enforcement tracker | As Of: 2026-03 | Authority: 9/10
[2] Data Protection Commission announces conclusion of inquiry into Meta Ireland | https://www.dataprotection.ie/en/news-media/press-releases/Data-Protection-Commission-announces-conclusion-of-inquiry-into-Meta-Ireland | Source-Type: official (DPA) | As Of: 2023-05 | Authority: 10/10
[3] Win for Amazon as Luxembourg court scraps record $854 million privacy fine | https://www.reuters.com/legal/government/win-amazon-luxembourg-court-scraps-record-854-million-privacy-fine-2026-03-13/ | Source-Type: news wire | As Of: 2026-03 | Authority: 9/10
[4] Commission finds Apple and Meta in breach of the Digital Markets Act | https://digital-strategy.ec.europa.eu/en/news/commission-finds-apple-and-meta-breach-digital-markets-act | Source-Type: official (EU) | As Of: 2025-04 | Authority: 10/10
[5] Cookies and advertisements inserted between emails: GOOGLE fined 325 million euros by the CNIL | https://www.cnil.fr/en/cookies-and-advertisements-inserted-between-emails-google-fined-325-million-euros-cnil | Source-Type: official (DPA) | As Of: 2025-09 | Authority: 10/10
[6] Next steps for Privacy Sandbox and tracking protections in Chrome | https://privacysandbox.google.com/blog/privacy-sandbox-next-steps | Source-Type: company blog | As Of: 2025-04 | Authority: 7/10
[7] Google is scrapping its planned changes for third-party cookies in Chrome | https://www.theverge.com/news/653964/google-privacy-sandbox-plans-scrapped-third-party-cookies | Source-Type: tech news | As Of: 2025-04 | Authority: 8/10
[8] FTC to Ban Kochava and Subsidiary from Selling Sensitive Location Data | https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data | Source-Type: official (FTC) | As Of: 2026-05 | Authority: 10/10
[9] "TotalRecall Reloaded" tool finds a side entrance to Windows 11's Recall database | https://arstechnica.com/gadgets/2026/04/totalrecall-reloaded-tool-finds-a-side-entrance-to-windows-11s-recall-database/ | Source-Type: security journalism | As Of: 2026-04 | Authority: 8/10
[10] Amazon Ring Cashes in on Techno-Authoritarianism and Mass Surveillance | https://www.eff.org/deeplinks/2025/07/amazon-ring-cashes-techno-authoritarianism-and-mass-surveillance | Source-Type: advocacy NGO | As Of: 2025-07 | Authority: 8/10
[11] Amazon to remove privacy feature from Echo | https://www.computing.co.uk/news/2025/amazon-to-remove-privacy-feature-from-echo | Source-Type: trade press | As Of: 2025-03 | Authority: 7/10
[12] Siri "unintentionally" recorded private convos; Apple agrees to pay $95M | https://arstechnica.com/tech-policy/2025/01/apple-agrees-to-pay-95m-delete-private-conversations-siri-recorded/ | Source-Type: tech news | As Of: 2025-01 | Authority: 8/10
[13] FTC Launches Inquiry into AI Chatbots Acting as Companions | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions | Source-Type: official (FTC) | As Of: 2025-09 | Authority: 10/10
[14] How to ditch Ring's surveillance network | https://www.theverge.com/tech/890910/best-ring-alternatives-privacy-focused-video-doorbell-local-storage-reolink-aqara-tapo-ecobee | Source-Type: consumer tech guide | As Of: 2025 | Authority: 7/10
[15] Protecting consumers' location data: Key takeaways from four recent cases | https://www.ftc.gov/business-guidance/blog/2024/12/protecting-consumers-location-data-key-takeaways-four-recent-cases | Source-Type: official (FTC) | As Of: 2024-12 | Authority: 9/10

## Findings
- 截至 CMS 2026-03-01 截点，GDPR 累计罚单约 **€6.11B**（2,685 起有金额记录）；史上最高单笔仍为 Meta Ireland **€1.2B**（2023-05-12，非法 EU→US 数据传输）。[1][2]
- Amazon Europe Core 2021-07 的 **€746M**（在线行为广告/同意问题）于 **2026-03** 被卢森堡行政法院以程序理由撤销并发回 CNPD 重裁；Reuters 称法院未充分分析故意/过失及替代制裁。[3]
- Amazon 罚单撤销后，GDPR Top 10 中 **9/10 来自爱尔兰 DPC**；当前活跃第二名 **TikTok €530M**（2025-05-02，数据传输）。[1]
- Meta 监管双线：**€390M**（2023-01，Facebook/Instagram 行为广告法律基础非法）+ **DMA €200M**（2025-04，"consent or pay" 未提供等价低追踪选项）；Apple 同期 **DMA €500M**（反引导/App Store 限制，非 ATT 本身）。[1][4]
- Google 2025-09-01 被 CNIL 罚 **€325M**（Gmail Promotions/Social 插播广告 + 注册 cookie 同意无效）；法国受影响约 **53M** 邮箱用户、**74M** 账户；适用 ePrivacy/法国法，**不适用 GDPR one-stop-shop**。[5]
- Google 2025-04-22 宣布 **不再淘汰 Chrome 第三方 cookie**、也不推出独立 cookie 选择提示；维持现有设置页控制；CMA 2026 释放 Privacy Sandbox 承诺。[6][7]
- Amazon 2025-03-28 起 Echo Dot/Show 等 **取消本地语音处理**，录音默认上传云端以支撑生成式 AI/Alexa+；Ring 2025 被 EFF 指重新开放警用取证/直播请求及 Familiar Faces 人脸库风险。[10][11]
- Microsoft Recall 2026 再曝 **TotalRecall Reloaded**：VBS 加密库本身难破，但解密内容经 **AIXHost.exe** 渲染可被同用户进程注入提取；MSRC 2026-04 结案为 **"Not a Vulnerability"**。[9]
- Apple 2025-01 同意 **$95M** 和解 Siri 误激活录音集体诉讼（覆盖 2014-09 至 2024-12 设备），否认不当行为；与 "Privacy on iPhone"/ATT 营销形成张力。[12]
- 监控资本主义链条：FTC 2024-12 至 2026-05 连续打击 **Venntel/Mobilewalla/X-Mode/Kochava** 等位置数据经纪；2025-09 FTC 向 **Alphabet/Meta/OpenAI 等 7 家** 发 Section 6(b) AI 聊天机器人数据命令，**尚无 OpenAI 公开 GDPR 级罚单** [u]。[8][13][15]

## Deep Read Notes
### Source [1]: GDPR Enforcement Tracker Report 2025/2026 — Numbers and Figures
Key data: 截点 2026-03-01；累计 €6.11B；Top 10 含 Meta €1.2B、TikTok €530M、Meta €405M/€390M、LinkedIn €310M、Uber €290M；Amazon €746M 标注 2026-03 被撤销发回重裁
Key insight: 2025-2026 执法重心从"跨境传输"扩展到法律基础（行为广告）、儿童数据、cookie/ePrivacy 平行通道；爱尔兰 DPC 主导 mega-fine 但法国 CNIL 在 ePrivacy 上独立重拳
Useful for: Olares SEO 类目"GDPR fines timeline""Meta/Google privacy alternative""EU data sovereignty" landing 的事实表与 H2 锚点

### Source [2]: Irish DPC — Meta €1.2B data transfer decision
Key data: Article 46(1) 违反；EDPB Art.65 强制加罚；5 个月内停止未来传输、6 个月内停止/删除已非法传输数据；罚款 €1.2B
Key insight: Schrems II 后 SCC+补充措施仍不足；跨境 SaaS/云默认架构即合规风险——"数据在 US 处理"是 Olares 反巨头叙事的核心证据
Useful for: "Facebook/Meta alternative self-hosted""EU personal cloud""stop US data transfers"对比文

### Source [5]: CNIL — Google €325M Gmail/cookies
Key data: €200M Google LLC + €125M Google Ireland；smart features 捆绑导致 Promotions/Social 插广告；注册 cookie 同意不对称/未充分告知；每日 €100k 迟延罚金
Key insight: Gmail 作为"第二全球邮箱"仍被认定为 direct marketing；巨头"一键拒绝"改版仍可能不够——self-hosted mail（Nextcloud/Mailcow）是天然替代场景
Useful for: "Gmail privacy concerns""degoogle email""self-hosted email vs Gmail ads"

## Gaps
- **Apple 隐私营销 vs 实践（相反主张候选）**：Apple 公开否认 Siri 数据用于广告定向 [12]；集体诉讼原告称误激活录音被第三方/广告主利用 [u]。ATT 2021 限制跨 app 追踪被营销为隐私胜利，但 2025 DMA 反引导罚单与 Siri 和解显示 **平台仍控制数据流与默认架构**，非"数据归用户"。
- **Google "放弃 cookie" vs 持续追踪**：Google 官方称保留用户选择与 Incognito IP Protection [6]；EFF/Verge 侧认为 Privacy Sandbox 仍服务 Google 广告栈 [7][u]。
- **OpenAI 训练数据**：FTC CID（2023 起）与 2025 Section 6(b) 表明监管兴趣高，但 **无公开 FTC 罚款或强制删除训练集命令** [13][u]；与 Meta/Google 已落地巨额 EU 罚单形成 SEO 内容空档（"ChatGPT privacy risk" 高搜索、低权威结论）。
- **去谷歌化/degoogle 量化**：社区情绪强但 **无统一 2026 装机/迁移统计** [u]；可观察代理指标：Ring 本地存储替代指南 [14]、Echo 本地处理取消 [11]、Home Assistant/Wyoming 离线语音栈——与 Olares"self-hosted 替代大厂 SaaS"叙事对齐。
- **Olares 落点（供 Lead 分类）**：(1) 监管/罚单 — Meta transfer、Google Gmail、DMA pay-or-consent；(2) 产品 concern — Recall 全屏截屏、Alexa 强制上云、Ring 执法/生物识别；(3) 生态 — 数据经纪→政府购买位置数据 bypass warrant [15][u]；(4) 行动号召 — degoogle checklist、self-hosted mail/voice/NAS/AI agent on personal cloud。

## END
