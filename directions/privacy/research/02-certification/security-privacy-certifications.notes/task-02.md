---
task_id: 02
role: 安全与隐私合规认证专家
status: complete
sources_found: 10
---

## Sources
[1] FedRAMP 20x | https://www.fedramp.gov/20x/ | Source-Type: official-gov | As Of: 2026-04 | Authority: 10/10
[2] Cyber Essentials Overview | https://www.ncsc.gov.uk/cyberessentials/overview | Source-Type: official-gov | As Of: 2026 | Authority: 10/10
[3] BSI C5 Introduction | https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_Einfuehrung/C5_Einfuehrung_node.html | Source-Type: official-gov | As Of: 2026 | Authority: 10/10
[4] AICPA SOC Suite of Services | https://www.aicpa.org/resources/landing/system-and-organization-controls-soc-suite-of-services | Source-Type: official-industry-body | As Of: 2026 | Authority: 10/10
[5] ISO/IEC 42001:2023 — AI management systems | https://www.iso.org/standard/42001 | Source-Type: official-standard | As Of: 2023-12 | Authority: 10/10
[6] PCI Security Standards Council Document Library | https://www.pcisecuritystandards.org/document_library/ | Source-Type: official-industry-body | As Of: 2026 | Authority: 10/10
[7] EuroPriSe Certification Programme (Art. 42 GDPR) | https://euprivacyseal.com/en/europrise-zertifizierungsprogramm/ | Source-Type: official-accredited-certifier | As Of: 2024-07 | Authority: 8/10
[8] IRAP Common Assessment Framework (PDF) | https://www.cyber.gov.au/sites/default/files/2025-04/IRAP%20common%20assessment%20framework.pdf | Source-Type: official-gov | As Of: 2025-04 | Authority: 10/10
[9] ISO 27001 vs. SOC 2: Understanding the Differences | https://www.drata.com/blog/soc-2-vs-iso-27001 | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 7/10
[10] Cyber Essentials Update 2026 | https://www.urmconsulting.com/blog/cyber-essentials-update-2026 | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 7/10

## Findings
- SOC 2 是 AICPA 框架下 CPA 对服务组织控制出具的**鉴证报告（attestation）**，非 ISO 式"证书"；评估 Trust Services Criteria（Security 必选，Availability/Processing Integrity/Confidentiality/Privacy 可选）。[4][9]
- ISO/IEC 27001:2022 是**正式 ISMS 认证**（3 年周期 + 年度监督审核），须维护 Statement of Applicability 覆盖 Annex A 93 项控制；与 SOC 2 控制重叠约 40–85%，但交付物与审计路径不同。[9]
- ISO/IEC 27701 是 ISO 27001 的**隐私扩展（PIMS）**，不能独立认证，须以 ISMS 为基础；与 ISO 42001（AIMS）可整合为"安全+隐私+AI"统一管理体系。[5][9]
- ISO/IEC 42001:2023 定义 AI 管理系统（AIMS）要求；**认证自愿**，由独立认证机构执行，ISO 本身不签发证书。[5]
- FedRAMP 20x（2026 Phase 3）已发布 Class A/B/C 规则；新 Rev5 授权将于 **2027-06-11** 停止受理；面向**云服务提供商（CSP）**授权，非个人自托管产品认证。[1]
- Cyber Essentials（NCSC/IASME）覆盖 5 大技术控制；**2026-04-27** 起启用 Danzell 问卷 v3.3，MFA 在可用时必须启用，否则自动失败；面向组织自身 IT 基础设施认证。[2][10]
- 德国 BSI C5:2026 含 **168 条**云安全准则（17 主题域），基于 ISAE 3000 审计 CSP 内控；BSI 建议客户要求 **Type 2** 有效性报告；CSP/客户/审计师**三方共担**安全责任。[3]
- GDPR Art. 42 **无统一"GDPR 认证"**；EuroPriSe 为德国 DAkkS 认可的数据处理者认证，EDPB 已批准 EU 级 seal 目录但 **EU 范围 scheme 尚未开放**。[7]
- HIPAA、PCI DSS **均无政府签发"合规证书"**；HIPAA 为组织合规 + BAA 合同义务，PCI DSS 4.0.1 由 QSA/SAQ 验证；**自托管/本地部署时**，基础设施、配置、数据控制责任几乎全部落在部署方，不存在云厂商 shared responsibility 分担。[6][8][9]
- 澳大利亚 IRAP 对云/on-prem 系统独立评估 ISM 控制，**不认证、不背书**；即使 CSP 已过 IRAP，客户侧配置与应用仍须单独评估——SEO 词如 "hipaa compliant hosting"、"soc 2 self hosted" 多指向**托管/SaaS 供应商营销**，与个人本地部署场景责任模型不同。[8][9]

## Deep Read Notes
### Source [1]: FedRAMP 20x
Key data: Phase 3 active 2026-04; Class A/B/C rules finalized; Consolidated Rules 2026 (CR26) planned FY26 Q3; submission pipeline FY26 Q4; new Rev5 certs stop 2027-06-11; principles: Transparency/Flexibility/Accountability/Accuracy/Automatic Validation
Key insight: FedRAMP 从"一刀切 Rev5 控制清单"转向按服务风险分级的 20x 持续验证模型；仍针对 CSP 进入联邦市场，自托管政府工作负载需在授权边界内自行承担 ATO 证据链
Useful for: SEO 分类「政府/FedRAMP/IRAP」；对比 Olares 个人本地部署 vs 云 CSP 授权路径

### Source [3]: BSI C5 Introduction
Key data: C5:2026=168 criteria/17 areas; Type 1=设计适切性, Type 2=运行有效性(6–12月); ISAE 3000; 联邦机构采购外部云处理公务数据时 C5 为强制最低标准; BSI 不推荐连续多次 Type 1
Key insight: C5 是 CSP attestation 报告供客户做风险分析，BSI 不审核报告——客户须自行判断 baseline 是否足够；含 Complementary User Entity Controls 映射
Useful for: SEO「C5 cloud compliance Germany」；Olares 若作为用户自管环境而非 CSP，C5 适用性有限

### Source [8]: IRAP Common Assessment Framework
Key data: 适用范围含 cloud/gateway/on-prem; IRAP assessors do NOT accredit/certify/endorse; 交付物=SAR + Controls Matrix; 须明确 shared responsibility model
Key insight: IRAP 是供 Authorising Officer 做风险决策的独立评估，非产品合规徽章；自托管/on-prem 与云一样须全栈证明 ISM 控制
Useful for: SEO「IRAP assessed self hosted」；澄清 ISO 27001/SOC 2 不能替代 IRAP

## Gaps
- **相反主张候选：** 多家合规 SaaS 营销 "SOC 2 Type II = HIPAA compliant"——官方路径上 HIPAA 无法被第三方"认证"，SOC 2 仅 Privacy TSC（且常未选）与 HIPAA Security Rule 不等价；自托管场景下用户仍须自行满足 ePHI 全部 administrative/physical/technical safeguards。[9] **反证：** IRAP/ACSC 明确 "Does ISO 27001 or SOC 2 replace IRAP? No."[8]
- SEO 意图词速查：hipaa compliant hosting / soc 2 hosting（选 BAA/SOC 2 云厂商，自托管无 BAA 链、责任在用户）；soc 2 self hosted / pci dss self hosted（组织/部署方可追证，非产品自带）；cyber essentials / c5 cloud germany（面向组织 IT，非个人 OS）；gdpr certification seal / europriSe（Art. 42 自愿 seal，个人本地部署通常非 processor）；iso 42001 certification（AIMS，与本地 Agent 叙事可对齐）；fedramp authorized / irap assessment（CSP/系统进政府市场，Olares 个人云≠ FedRAMP CSP 路径）。

## END
