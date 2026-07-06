# 安全 / 隐私认证与标准格局（privacy 方向 · 分类 02）

> 研究日期: 2026-07-06 | 来源: task-02（10 源）| 模式: Lightweight | AS_OF: 2026-07-06 | 官方源占比: ~70% | 视角: 责任模型 + Olares 自托管落点
>
> 分类 = 安全/隐私**认证与标准**（SOC 2、ISO 27001/27701/42001、HIPAA、PCI DSS、FedRAMP、Cyber Essentials、C5、IRAP、GDPR seal）。立法见分类 01。发现笔记见 [security-privacy-certifications.notes/](/Users/pengpeng/seo/directions/privacy/research/02-certification/security-privacy-certifications.notes)。

## 摘要
认证格局的关键认知：**多数"合规徽章"面向组织或云服务商（CSP），不是产品自带属性**。SOC 2 是 AICPA 框架下 CPA 出具的**鉴证报告**（非证书），ISO 27001/27701/42001 是 ISMS/PIMS/AIMS 认证，HIPAA/PCI DSS **均无政府签发的"合规证书"**，FedRAMP/IRAP/C5 面向 CSP 进入政府/受监管市场 [1][3][4][5][6][8][9]。对自托管/本地部署，**shared responsibility 几乎全部落到部署方**：没有云厂商替你分担基础设施、配置、数据控制的合规责任 [6][8][9]。这既是诚实约束，也是内容机会——大量 `hipaa compliant hosting`、`soc 2 self hosted` 搜索其实指向**托管/SaaS 营销**，Olares 内容可澄清责任模型，把 ISO 42001（AIMS）与"本地 Agent"叙事对齐。

## 1. 认证类型速览
| 标准 | 性质 | 面向对象 | 自托管适用性 | 来源 |
|------|------|----------|-------------|------|
| SOC 2 | AICPA 鉴证报告（attestation，非证书） | 服务组织 | 部署方可追证，产品不自带 | [4][9] |
| ISO/IEC 27001:2022 | 正式 ISMS 认证（3 年 + 年度监督） | 组织 | 组织可认证，需 SoA 覆盖 Annex A 93 控制 | [9] |
| ISO/IEC 27701 | 隐私扩展（PIMS），不可独立认证 | 组织（须先有 ISMS） | 与 27001 一体 | [5][9] |
| ISO/IEC 42001:2023 | AI 管理系统（AIMS）认证，自愿 | 组织 | **可与本地 Agent 叙事对齐** | [5] |
| HIPAA | 组织合规 + BAA 合同义务，无政府证书 | 医疗相关实体 | 自托管无 BAA 链，责任全在用户 | [6][9] |
| PCI DSS 4.0.1 | QSA/SAQ 验证 | 处理卡数据方 | 部署方自证 | [6] |
| FedRAMP 20x | CSP 联邦市场授权 | 云服务商 | 个人自托管≠ CSP 路径 | [1] |
| Cyber Essentials | NCSC/IASME 组织 IT 认证 | 组织 | 面向组织基础设施 | [2][10] |
| BSI C5 | CSP attestation（ISAE 3000，168 条） | 云服务商 | Olares 作用户自管环境时适用有限 | [3] |
| IRAP | 澳洲独立评估（不认证、不背书） | 云/on-prem 系统 | 自托管须全栈证明 ISM 控制 | [8] |
| EuroPriSe (GDPR Art.42) | 自愿 seal | 数据处理者 | EU 级 scheme 尚未开放 | [7] |

**置信度: High**（全部官方标准机构/监管源）。

## 2. 关键性质澄清（内容去误区）
- **SOC 2 ≠ 证书**：是 CPA 对 Trust Services Criteria（Security 必选）的鉴证报告；与 ISO 27001 控制重叠约 40–85%，但交付物与审计路径不同 [4][9]。
- **HIPAA/PCI DSS 无"官方合规证书"**：HIPAA 是组织合规 + BAA，PCI DSS 由 QSA/SAQ 验证；自托管时 ePHI 的全部 administrative/physical/technical safeguards 落在部署方 [6][9]。
- **政府类认证面向 CSP**：FedRAMP 20x（2026 Phase 3，新 Rev5 授权 2027-06-11 停收）、C5（联邦采购最低标准）、IRAP（供 Authorising Officer 做风险决策）——ISO 27001/SOC 2 **不能替代** IRAP [1][3][8]。

**置信度: High**。

## 3. 自托管的责任模型（Olares 落点）
- 云 SaaS 有 shared responsibility：厂商担部分基础设施与认证。**自托管把责任模型反转**——用户/部署方获得完全控制，也承担完全责任 [6][8][9]。
- 对 Olares 的诚实定位：Olares 提供**数据完全归用户、可选定物理位置**的底座，但"通过某项认证"是**组织/部署行为**，不是 OS 出厂属性。ISO 42001（AIMS）与"本地 Agent、可解释数据流"叙事最契合，可作差异化内容锚点 [5]。

**置信度: Medium**（责任模型清晰，但个案合规须逐项评估）。

## 4. 候选关键词
- 信息型：`SOC 2 vs ISO 27001`、`what is SOC 2`、`HIPAA compliance explained`、`ISO 42001 certification`、`Cyber Essentials`、`C5 cloud compliance Germany`、`FedRAMP vs IRAP`。
- 商业/意图（多为托管营销，需澄清）：`hipaa compliant hosting`、`soc 2 hosting`、`gdpr certification seal`、`pci dss self hosted`。
- Olares 结合（差异化）：`soc 2 self hosted`（责任在部署方）、`self hosted HIPAA`、`iso 42001 self hosted AI`、`shared responsibility self hosting`。

## 5. 核心争议 / 反方
**核心争议**：合规 SaaS 常营销 "SOC 2 Type II = HIPAA compliant"——官方上 HIPAA 无法被第三方"认证"，SOC 2 的 Privacy TSC（且常未选）与 HIPAA Security Rule 不等价 [9]。反证：ACSC 明确 "Does ISO 27001 or SOC 2 replace IRAP? No." [8]。

**反方解释**：认证对企业采购是真实信任信号，自托管"我自己控制所以更安全"若缺乏审计证据链，在 B2B 场景说服力不足。Olares 内容应区分**个人/家庭用户**（控制权即价值）与**受监管组织**（仍需走认证流程）。

## 6. 局限性与未来方向
- **局限**：未做各标准全文条款级深读；ISO 27701 与 42001 整合路径、EU 级 GDPR seal 开放时间未定 [task-02 Gaps]。
- **未来方向**：写一篇"自托管的合规责任模型"支柱文，澄清 `hipaa compliant hosting` 类词的真实含义；对 ISO 42001 + 本地 AI 做专项。

## 参考文献
[1] FedRAMP. "FedRAMP 20x". official-gov. As Of: 2026-04. https://www.fedramp.gov/20x/
[2] NCSC. "Cyber Essentials Overview". official-gov. As Of: 2026. https://www.ncsc.gov.uk/cyberessentials/overview
[3] BSI. "C5 Introduction". official-gov. As Of: 2026. https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/C5_Einfuehrung/C5_Einfuehrung_node.html
[4] AICPA. "SOC Suite of Services". official-industry-body. As Of: 2026. https://www.aicpa.org/resources/landing/system-and-organization-controls-soc-suite-of-services
[5] ISO. "ISO/IEC 42001:2023 — AI management systems". official-standard. As Of: 2023-12. https://www.iso.org/standard/42001
[6] PCI SSC. "Document Library". official-industry-body. As Of: 2026. https://www.pcisecuritystandards.org/document_library/
[7] EuroPriSe. "Certification Programme (Art. 42 GDPR)". official-accredited-certifier. As Of: 2024-07. https://euprivacyseal.com/en/europrise-zertifizierungsprogramm/
[8] ACSC. "IRAP Common Assessment Framework". official-gov. As Of: 2025-04. https://www.cyber.gov.au/sites/default/files/2025-04/IRAP%20common%20assessment%20framework.pdf
[9] Drata. "ISO 27001 vs. SOC 2". secondary-industry. As Of: 2026-03. https://www.drata.com/blog/soc-2-vs-iso-27001
[10] URM. "Cyber Essentials Update 2026". secondary-industry. As Of: 2026-03. https://www.urmconsulting.com/blog/cyber-essentials-update-2026
