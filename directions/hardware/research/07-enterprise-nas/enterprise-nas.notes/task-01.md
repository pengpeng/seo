---
task_id: 01
role: Synology 企业/机架线分析师
status: complete
sources_found: 8
---

## Sources
[1] SA6400 | https://www.synology.com/en-us/products/SA6400 | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[2] SA3610 & SA3410 | https://www.synology.com/en-us/products/SA3410 | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[3] HD6500 | https://www.synology.com/en-us/products/HD6500 | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[4] RS6426xs+ | https://www.synology.com/en-us/products/RS6426xs+ | Source-Type: official | As Of: 2026-06 | Authority: 10/10
[5] Synology AI Console / Office Suite AI | https://www.synology.com/en-us/dsm/feature/productivityai | Source-Type: official | As Of: 2026-07 | Authority: 10/10
[6] COMPUTEX 2026 新闻稿 | https://www.prnewswire.com/apac/news-releases/synology-showcases-the-next-generation-diskstation-manager-and-a-full-lineup-of-data-management-solutions-at-computex-2026-302790959.html | Source-Type: journalism | As Of: 2026-06 | Authority: 8/10
[7] DVA3221 / DVA1622 数据表 | https://www.synology.com/en-global/products/DVA | Source-Type: official | As Of: 2022 | Authority: 9/10
[8] DSM 7.4 与 AI 路线（型号清单） | https://www.blackvoid.club/synology-dsm-7-4-and-ai-future/ | Source-Type: community | As Of: 2026-06 | Authority: 6/10

## Findings
- **SA6400**：2U / 12 盘位（扩至 108 盘 RX1223RP×8）；AMD EPYC 7272（12C/24T）；32 GB 预装 / **最高 1024 GB**；4×1GbE + 2×10GbE，PCIe 可选 **25/40GbE 或 FC**；官方未列 MSRP。[1]
- **SA3610 / SA3410**：2U / 12 盘位（扩至 96 盘 RX1222sas×7）；SA3610 为 Intel Xeon D-**1567**（12C），SA3410 为 D-**1541**（8C）；16 GB / **最高 128 GB**；2×10GbE，PCIe 可选 10/25/40GbE；可组 SHA 双机 HA。[2]
- **SA3400D**（HA 线）：2U / 12 盘位双控 active-passive（扩至 36 盘）；每控 Intel Xeon D-1541 + 8 GB（单控最高 64 GB）；分钟级 failover；软件规格含 **Synology Photos 人脸识别** 与 AI Console 去标识化（≥8 GB RAM）。[2][5]
- **HD6500**：4U / **60 盘位**（扩至 300 盘 RX6025sas×4）；**2×** Intel Xeon Silver 4210R（各 10C）；64 GB / **最高 512 GB**；2×1GbE + 2×10GbE，PCIe 可选 25GbE；官方未列 MSRP。[3]
- **RS6426xs+**（2026 XS+ 旗舰）：3U / 16 盘位（扩至 64 盘）；Intel Xeon D-**1739**（8C/16T）；16 GB / **最高 96 GB**；2×10GbE + OOB；**PCIe Gen4×2**，官方/社区均指可接 NVIDIA GPU 做本地 AI 推理。[4][8]
- **DS1825+ / DS1525+**（Plus 高端桌面）：8 盘 / 5 盘；AMD Ryzen V1500B；8 GB / 最高 32 GB；2×2.5GbE（DS1825+ 可选 25GbE）；社区报价约 **€1000**（DS1825+，含税）。[8]
- **RS4021xs+**（上一代 XS+ 机架）：3U / 16 盘位；Intel Xeon D-1541；16 GB / 64 GB；4×1GbE + 2×10GbE；渠道标价约 **$7,495**（无盘）。[8]
- **DVA3221 / DVA1622**（深度视频分析 NVR）：DVA3221 为 4 盘 + Atom C3538 + **NVIDIA GTX 1650**，32 路摄像机 / **12 路并行 DVA**；DVA1622 为 2 盘 + Celeron J4125，16 路 / **2 路 DVA**；均含 8 路免费授权。[7][6]
- **DSM AI Console**：x86-64 NAS 可装；对接 OpenAI/Azure/Bedrock/Gemini 等第三方 API（Synology 不另收费）；**去标识化需 ≥8 GB RAM**；非本地 LLM 推理。[5]
- **Computex 2026 / DSM 7.4**：DSM Agent 编排系统级自动化工作流；Drive 4.1 **本地 embedding** 语义搜索；2026 机架 XS+ 支持 GPU；新一代 DVA 含 AI 语义事件搜索；纯本地 LLM 预计 2026 晚些时候。[6][8]

## Deep Read Notes
### Source [1]: SA6400
Key data: 12 盘 2U；EPYC 7272；RAM 32 GB→1024 GB；4×1GbE+2×10GbE；扩 108 盘；>6500/4000 MB/s 顺序读写；5 年保修。
Key insight: SA 线最高可扩型号之一，网口可上 25/40GbE/FC，面向 studio/enterprise 大容量。
Useful for: SA 系规格表、网口/扩展对比节。

### Source [3]: HD6500
Key data: 60 盘 4U；双 Xeon Silver 4210R；64 GB→512 GB；2×1GbE+2×10GbE；扩 300 盘；Surveillance 建议最多 600 路 IP cam。
Key insight: 高密度温/冷存 + 监控中心存库定位，非性能型 AI 算力节点。
Useful for: HD 高密度节、监控规模化部署节。

### Source [5]: Synology AI Console
Key data: Package Center 安装；第三方 API 集成免费；去标识化 ≥8 GB RAM；支持按套件/用户/token 限额与审计日志。
Key insight: 当前 Office/MailPlus AI 以**云端 API + 本地去标识化**为主，非内置大模型。
Useful for: AI 能力矩阵、与 Olares 本地 Agent 对比节。

## Gaps
- 官方未公开 SA/HD/RS XS+ 等企业型号 MSRP；仅 DS Plus 有零散渠道价（DS1825+ ~€1000；RS4021xs+ ~$7495）。
- 2026 新 RS 线（RS4826xs+ 48 盘、RS3626xs+、RS1626xs+、RS11626xs+ 等）缺少 synology.com 深读规格与定价。
- COMPUTEX 2026 提及的新 DVA 语义搜索型号、PAS7700/GS 全闪企业线、AI Station 尚未 GA，规格未定型。
- **相反解读**：Synology 在 Computex 同时推 Bee Series 个人私有云与 PAS7700/Cluster Manager 企业栈——企业机架 NAS（RS/SA/HD）面向 IT/存储采购，Bee/DS Plus 面向 prosumer/SOHO；**"企业 NAS"与"个人云"是不同买家段与渠道**，不应混为同一 SEO 意图簇。

## END
