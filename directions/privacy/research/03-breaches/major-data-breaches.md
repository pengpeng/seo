# 重大数据泄露与安全事件格局（privacy 方向 · 分类 03）

> 研究日期: 2026-07-06 | 来源: task-03（10 源）| 模式: Lightweight | AS_OF: 2026-07-06 | 官方源占比: ~40% | 视角: 集中托管风险 + Olares 自托管落点
>
> 分类 = 2023–2026 **重大数据泄露与安全事件**（超大规模泄露、勒索、供应链、云误配、数据经纪、AI/IoT）。巨头监管罚单见分类 05。发现笔记见 [major-data-breaches.notes/](/Users/pengpeng/seo/directions/privacy/research/03-breaches/major-data-breaches.notes)。

## 摘要
2023–2026 的泄露格局有一条主线：**单点集中托管 → 一次失守波及百万/亿级记录**。Change Healthcare 勒索攻击最终影响 **192.7M** 人（美国最大医疗泄露），入口是一个无 MFA 的远程访问凭据；National Public Data 作为数据经纪商聚合泄露 **272M+** 人 PII；印度 NACH 银行转账因单个公开 S3 桶暴露 **273,160** 份 PDF [6][1][3]。Verizon 2025 DBIR 显示勒索占确认泄露 **44%**、第三方参与从 15% 翻倍到 **30%** [7]。供应链（MOVEit、XZ Utils）与云误配是两类结构性风险 [4][5]。**Olares 叙事锚点**：自托管缩小第三方托管面与集中化爆炸半径，但须诚实——它**不消除**供应链、凭据失窃、误配与内部 GenAI 误用风险 [5][7][9]。

## 1. 超大规模泄露
- **Change Healthcare（2024-02）**：UnitedHealth 子公司勒索攻击，最终 **192.7M** 人受影响，美国迄今最大医疗数据泄露；入口为无 MFA 的 Citrix 远程凭据，UHG 承认支付 **$22M** 比特币赎金 [6]。
- **National Public Data（2023-12 入侵 / 2024-07 公开）**：数据经纪商聚合泄露，Krebs 引 **272M+** 人 PII；CPPA 口径约 3B records / ~270M individuals（含大量不准确记录）；公司破产后仍面临多州 AG 与 CPPA 罚款 [1][10]。

**置信度: High**（监管确认 + 权威调查报道）。

## 2. 勒索软件趋势（口径分歧显著）
- Verizon 2025 DBIR：**12,195** 起确认泄露，勒索占 **44%**（前一年 32%）；中位赎金 **$115,000**，**64%** 受害者未付赎金；第三方参与从 15% 升至 **30%** [7]。
- Chainalysis：2025 链上勒索支付约 **$820M**（YoY -8%），付赎率或降至 **28%** 历史低点，但中位支付额 **$59,556**（+368% YoY）——**攻击量与支付量背离** [2]。

**置信度: Medium**（"攻击"定义分歧导致相反结论并存，见争议）。

## 3. 供应链与云误配（结构性风险）
- **MOVEit（CVE-2023-34362）**：2023-05 起 CL0P 利用 SQL 注入零日窃取 MFT 数据库，CISA/FBI 联合告警；受影响组织 2,700+、个人 ~93.3M [u] [4]。
- **XZ Utils（CVE-2024-3094）**：5.6.0/5.6.1 tarball 含恶意 liblzma 构建逻辑，可影响链接该库的 sshd；CISA 建议降级至 5.4.6 [5]。
- **云误配**：UpGuard 2025-08 发现公开 S3 桶含 **273,160** 份印度 NACH 银行转账 PDF（210GB），属"无入侵、仅配置公开读" [3]。

**置信度: High**（CISA 官方 + 安全研究披露）。

## 4. AI 与 IoT 相关事件
- **AI 泄露**：2023-03 三星员工 3 次将源码/缺陷代码/会议转录粘贴进 ChatGPT（默认可用于训练），引发内部 GenAI 禁令 [9]。
- **IoT**：FTC 2023-05 诉 Ring 允许员工/承包商无限访问客户视频，黑客可接管摄像头；和解 **$5.8M** + 20 年隐私计划 [8]。

**置信度: High**（FTC 官方 + 权威新闻）。

## 5. 候选关键词
- 信息型：`biggest data breaches 2026`、`Change Healthcare breach`、`MOVEit breach explained`、`what is a supply chain attack`、`ransomware statistics 2026`、`S3 bucket data leak`。
- 意图型：`how to protect against data breaches`、`data broker opt out`、`freeze credit after breach`、`ransomware backup strategy`。
- Olares 结合：`self hosted vs cloud data breach risk`、`own your data avoid breaches`、`self hosted backup ransomware`、`keep data off data brokers`。

## 6. 核心争议 / 反方
**核心争议**：(1) "泄露规模逐年爆炸" vs 统计口径差异——研究者发现的 8.7B 行 Elasticsearch 与监管确认的受影响个人数不可相加 [u]；(2) "勒索历史最高" vs 支付/加密率下降——DBIR 44% 含勒索 [7] 与 Chainalysis 链上支付 -8% [2] 并存；(3) IoT 大规模被黑 vs 厂商否认——2025 Ring 用户报告异常登录，Ring 归因 backend bug [u]，与 2023 FTC 已认定事件 [8] 并存。

**反方解释**：自托管并非零风险——供应链后门（XZ）、凭据失窃、误配同样击穿自托管环境 [5][7]。诚实口径：自托管改变的是**风险结构**（去掉集中化聚合与第三方托管面），不是"绝对安全"。

## 7. 局限性与未来方向
- **局限**：多起事件受影响个人数为估计值（标 [u]）；勒索口径需交叉多源。
- **未来方向**：维护一张"年度重大泄露 + 根因 + 是否集中托管"表；对 `data broker opt out`、`self hosted backup` 跑量化。

## 参考文献
[1] KrebsOnSecurity. "National Public Data Published Its Own Passwords". journalism. As Of: 2024-08. https://krebsonsecurity.com/2024/08/national-public-data-published-its-own-passwords/
[2] Chainalysis. "Total Ransomware Payments Stagnate (2026 Crypto Crime Report)". secondary-industry. As Of: 2026-01. https://www.chainalysis.com/blog/crypto-ransomware-2026/
[3] UpGuard. "Unclaimed Property: India Banking Information Exposed". secondary-industry. As Of: 2025-09. https://www.upguard.com/breaches/india-bank-transfers-data-leak
[4] CISA. "#StopRansomware: CL0P Exploits CVE-2023-34362 MOVEit". official. As Of: 2023-06. https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a
[5] CISA. "Supply Chain Compromise Affecting XZ Utils, CVE-2024-3094". official. As Of: 2024-03. https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094
[6] Healthcare IT News. "Change Healthcare data breach: 193 million affected". journalism. As Of: 2025-08. https://www.healthcareitnews.com/news/new-numbers-change-healthcare-data-breach-193-million-affected
[7] Verizon. "2025 Data Breach Investigations Report Executive Summary". secondary-industry. As Of: 2025-04. https://www.verizon.com/business/resources/en/reports/2025-dbir-executive-summary.pdf
[8] FTC. "FTC Says Ring Employees Illegally Surveilled Customers". official. As Of: 2023-05. https://www.ftc.gov/news-events/news/press-releases/2023/05/ftc-says-ring-employees-illegally-surveilled-customers-failed-stop-hackers-taking-control-users
[9] Cybersecurity Dive. "Samsung employees leaked corporate data in ChatGPT". journalism. As Of: 2023-04. https://www.cybersecuritydive.com/news/Samsung-Electronics-ChatGPT-leak-data-privacy/647219/
[10] TechCrunch. "California privacy regulator seeks to fine Florida data broker". journalism. As Of: 2025-02. https://techcrunch.com/2025/02/20/california-privacy-regulator-seeks-to-fine-florida-data-broker-after-huge-breach-of-social-security-numbers/
