# Falco SEO 竞品分析报告

> 域名：falco.org | SEMrush US | 2026-07-06
> CNCF 毕业项目，云原生运行时安全领域事实标准——eBPF 驱动的 Kubernetes/容器异常行为检测工具。

---

## 项目理解（前置）

Falco 是由 Sysdig 创建、现已捐给 CNCF（已毕业级别）的云原生运行时安全工具。它通过 eBPF 在 Linux 内核层监听系统调用，与 Kubernetes 深度集成，实时检测容器逃逸、权限提升、异常进程等威胁行为，并可将告警转发到 50+ 第三方（SIEM、Slack、Webhook 等）。2026 年 5 月发布 0.44.0，新增 Prempti（Falco 与 AI 编码 Agent 的集成），是该生态的新亮点。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 基于 eBPF 的云原生运行时安全检测工具，Kubernetes/容器场景的开源 IDS |
| 开源 / 许可证 | 开源，Apache-2.0 |
| 主仓库 | https://github.com/falcosecurity/falco（★ 9,128） |
| 核心功能 | 1. eBPF 系统调用监听；2. 可定制规则引擎；3. Kubernetes 上下文感知告警；4. 插件体系（AWS CloudTrail/GitHub/Okta 等）；5. falcosidekick 多通道转发 |
| 商业模式 / 定价 | 纯开源免费，Helm chart 部署；生态方 Sysdig 提供托管商业版 |
| 差异化 / 价值主张 | CNCF 毕业背书、eBPF 零侵入、与 Kubernetes 原生集成、规则社区活跃、50+ 输出集成 |
| 主要竞品（初判）| Tetragon（Cilium/Isovalent）、Tracee（Aqua Security OSS）、Sysdig 商业版、KubeArmor |
| Olares Market | ⬜ 已列入，未产出报告（本报告首次） |
| 来源 | https://falco.org、https://falco.org/docs/、https://github.com/falcosecurity/falco |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | falco.org |
| SEMrush Rank | 3,199,694 |
| 自然关键词数 | 175 |
| 月自然流量（US）| 139 |
| 自然流量估值 | $1,171/月 |
| 付费关键词数 | 0 |
| 月付费流量 | 0 |
| 排名 1-3 位 | 9 词 |
| 排名 4-10 位 | 18 词 |
| 排名 11-20 位 | 30 词 |

> **关键信号**：流量极低但每次访问估值高（$1,171/139 ≈ $8.4/访客），说明关键词 CPC 贵（安全工具领域）、但 Falco 官网没有做 SEO。官网是项目文档站而非内容营销站——典型的"产品知名、网站弱"格局。0 付费投入，完全依赖自然流量。

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| falco.org（主域）| 175 | 139 | 100% |

无独立子域名——所有流量集中在主域。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| falco security | 1 | 50 | 41 | $14.57 | 40 | 导航 | falco.org/ |
| falco scan | 1 | 140 | 18 | $7.55 | 34 | 信息 | falco.org/ |
| gvisor | 8 | 1,000 | 50 | $7.20 | 19 | 信息 | falco.org/blog/intro-gvisor-falco/ |
| falcoo（误拼）| 12 | 1,000 | 25 | $0.89 | 9 | 导航 | falco.org/about/ |
| falco container security | 1 | 30 | 32 | $11.04 | 7 | 信息/商业 | falco.org/ |
| cloud native runtime security | 2 | 50 | 11 | $0.00 | 4 | 信息 | falco.org/ |
| falcoscan | 6 | 90 | 7 | $8.46 | 3 | 信息 | falco.org/ |
| cloud native container security | 3 | 70 | 28 | $0.00 | 3 | 信息 | falco.org/ |
| falcostore | 3 | 70 | 0 | $0.44 | 2 | 信息 | falco.org/ |
| open source kubernetes security tools | 7 | 90 | 14 | $0.00 | 2 | 信息 | falco.org/ |
| falco kubernetes | 1 | 110 | 38 | $12.92 | 2 | 商业 | falco.org/ |
| runtime threat detection | 4 | 70 | 19 | $0.00 | 2 | 信息 | falco.org/ |
| runtime security tools | 6 | 110 | 22 | $23.13 | 0 | 信息 | falco.org/ |
| container security companies | 12 | 210 | 23 | $0.00 | 1 | 信息 | falco.org/ |
| argo workflows cncf graduated project | 13 | 2,400 | 29 | $0.00 | 1 | 信息 | falco.org/blog/falco-graduation/ |
| kubernetes audit logs | — | 170 | 31 | $5.96 | — | 信息 | — |

> 值得注意：`gvisor`（1000 月量，KD 50）带来 19 个流量，来自一篇介绍性博文，是意外排名。`argo workflows` 关键词（2400 月量）也因毕业公告帖带来微量访客——说明 CNCF 生态文章天然沾流量。

### 付费词（Google Ads）

无付费投放。Falco 为纯开源项目，未进行任何 Google Ads 投放。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| tetragon | 2,400 | 58 | $5.75 | 导航 | Cilium 的 eBPF 运行时安全工具，直接竞品 |
| falco vs sysdig | 20 | 0 | $0.00 | — | 量小，低竞争 ⭐ |
| falco vs tetragon | 20 | 0 | $33.48 | — | CPC 高信号，虽量小 ⭐ |
| sysdig falco | 40 | 0 | $20.78 | — | 历史渊源词 ⭐ |
| cilium tetragon | 40 | 21 | $15.40 | 信息 | ⭐ |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| kubernetes security | 2,400 | 38 | $32.94 | 信息 | 最大类目词，KD 中等 |
| cloud native security | 1,900 | 39 | $19.09 | 信息 | 高量中难度 |
| container runtime security | 720 | 20 | $9.06 | 信息 | ⭐⭐⭐ 核心机会词 |
| kubernetes security tools | 720 | 18 | $23.92 | 信息 | ⭐⭐⭐ 核心机会词 |
| kubernetes runtime security | 320 | 18 | $20.98 | 信息 | ⭐⭐⭐ 核心机会词 |
| kubernetes audit logs | 170 | 31 | $5.96 | 信息 | 稍高 KD |
| cloud native security tools | 140 | 30 | $11.35 | 信息 | KD 边界 |
| ebpf security | 110 | 39 | $7.40 | 信息 | KD 偏高 |
| open source container security | 110 | 13 | $0.00 | 信息 | ⭐⭐ 低 KD |
| kubernetes compliance | 110 | 26 | $0.00 | 信息 | ⭐ |
| kubernetes security monitoring | 90 | 17 | $0.00 | 信息 | ⭐⭐ |
| container security monitoring | 90 | 24 | $0.00 | 信息 | ⭐ |
| open source kubernetes security tools | 90 | 14 | $0.00 | 信息 | ⭐⭐ |
| runtime threat detection | 70 | 19 | $0.00 | 信息 | ⭐ |
| container threat detection | 40 | 17 | $0.00 | 信息 | ⭐ |
| cloud native runtime security | 50 | 11 | $0.00 | 信息 | ⭐⭐⭐ 极低 KD |
| ebpf security monitoring | 30 | 0 | $0.00 | — | ⭐ GEO 前哨 |
| runtime security monitoring | 20 | 0 | $0.00 | — | GEO 前哨 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| falco scan | 140 | 18 | $7.55 | 信息 | ⭐ 现已排名第 1 |
| falco kubernetes | 110 | 39 | $12.92 | 商业 | 品牌+场景词 |
| falcoscan | 90 | 7 | $8.46 | 信息 | ⭐ 拼写变体 |
| falco security | 50 | 41 | $14.57 | 导航 | 品牌词，护城河 |
| falco container security | 30 | 32 | $11.04 | 信息/商业 | 品牌+功能 |
| falco rules | 20 | 0 | $0.00 | — | ⭐ 使用教程词 |
| falco tutorial | 20 | 0 | $0.00 | — | ⭐ 使用教程词 |
| falco helm | 20 | 0 | $0.00 | — | ⭐ 安装教程词 |
| runtime threat detection | 70 | 19 | $0.00 | 信息 | ⭐ 功能描述词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source container security | 110 | 13 | $0.00 | 信息 | ⭐⭐ 极低 KD，强自托管信号 |
| open source kubernetes security tools | 90 | 14 | $0.00 | 信息 | ⭐⭐ 低 KD |
| open source kubernetes security | 20 | 0 | $0.00 | — | GEO 前哨 |
| sysdig open source | 20 | 0 | $0.00 | — | 品牌历史词 |
| ebpf security monitoring | 30 | 0 | $0.00 | — | GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Falco 作为 Olares Market 的安全类应用，叙事切入点是"给你的个人云加一层运行时防护"——Olares 用户在自己的硬件上跑容器/Agent，Falco 是让这一切更安全的安全感加法。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| kubernetes runtime security | 320 | 18 | $20.98 | Olares 内部运行 K3s，Falco 可作为运行时安全层；一键部署文章可覆盖此词 | ⭐⭐⭐ |
| container runtime security | 720 | 20 | $9.06 | 容器运行时安全是个人云的核心需求；Olares Market 一键装 Falco | ⭐⭐⭐ |
| kubernetes security tools | 720 | 18 | $23.92 | 高流量工具列表词，Olares Market 收录 Falco 可作为 Olares + 开源安全工具组合文的核心词 | ⭐⭐⭐ |
| open source container security | 110 | 13 | $0.00 | 低 KD + 开源信号，Olares 自托管用户天然匹配 | ⭐⭐⭐ |
| kubernetes security monitoring | 90 | 17 | $0.00 | Falco 是监控层，Olares 提供运行环境；低 KD 内容机会 | ⭐⭐ |
| cloud native runtime security | 50 | 11 | $0.00 | Falco 官方自描述词，KD 极低（11），Olares 文章可直接切入 | ⭐⭐⭐ |
| open source kubernetes security tools | 90 | 14 | $0.00 | "最佳开源 K8s 安全工具"列表类文章，自然收录 Olares+Falco | ⭐⭐ |
| falco kubernetes | 110 | 39 | $12.92 | 品牌+场景词，安装教程类文章 | ⭐⭐ |
| falco rules | 20 | 0 | $0.00 | 使用教程词，GEO 前哨，Olares 部署后的配置说明 | ⭐ |
| runtime security open source | 0 | 0 | $0.00 | 零量 GEO 前哨，Perplexity/AI Overview 用 | ⭐ |
| self-hosted security monitoring | 0 | 0 | $0.00 | GEO 前哨，精准描述 Olares+Falco 的场景 | ⭐⭐ |
| falco olares | 0 | 0 | $0.00 | GEO 前哨（集成词），抢未来搜索引用位 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| container runtime security | 720 | 20 | $9.06 | 信息 | 主词候选 | 最高量+低 KD 的黄金组合；Olares Market 安装 Falco 的核心内容词 |
| kubernetes security tools | 720 | 18 | $23.92 | 信息 | 主词候选 | 同量同 KD，列表类文章机会；高 CPC 说明商业价值高 |
| kubernetes runtime security | 320 | 18 | $20.98 | 信息 | 主词候选 | 高 CPC（$21）说明买家意图强；Olares+Falco 组合文核心词 |
| kubernetes security | 2,400 | 38 | $32.94 | 信息 | 次级 | 量最大但 KD 38，作为文章 H2/次级词收进；不单独打 |
| cloud native security | 1,900 | 39 | $19.09 | 信息 | 次级 | KD 39 偏高，可作品类词背景收录 |
| open source container security | 110 | 13 | $0.00 | 信息 | 主词候选 | KD 极低（13），自托管信号词，Olares 差异化切入 |
| cloud native runtime security | 50 | 11 | $0.00 | 信息 | 次级 | KD 最低（11），Falco 已排名第 2；可并入容器运行时安全文章 |
| kubernetes security monitoring | 90 | 17 | $0.00 | 信息 | 次级 | 低 KD，并入 container runtime security 同簇 |
| open source kubernetes security tools | 90 | 14 | $0.00 | 信息 | 次级 | 低 KD，列表文章天然收录 |
| falco scan | 140 | 18 | $7.55 | 信息 | 次级 | Falco 已排名第 1；教程/功能介绍次级词 |
| falco kubernetes | 110 | 38 | $12.92 | 商业 | 次级 | 品牌+场景，安装教程文章自然覆盖 |
| container threat detection | 40 | 17 | $0.00 | 信息 | 次级 | 低 KD，相关功能词，并入运行时安全文章 |
| runtime threat detection | 70 | 19 | $0.00 | 信息 | 次级 | 功能描述词，低 KD ⭐ |
| falco vs sysdig | 20 | 0 | $0.00 | — | GEO | 低量对比词，抢 AI Overview 引用位 |
| falco vs tetragon | 20 | 0 | $33.48 | — | GEO | CPC $33 说明高商业价值；GEO 文章优先 |
| self-hosted security monitoring | 0 | 0 | $0.00 | — | GEO | 零量但精准描述 Olares+Falco 场景 |
| ebpf security monitoring | 30 | 0 | $0.00 | — | GEO | eBPF 技术词，AI Overview 前哨 |
| falco olares | 0 | 0 | $0.00 | — | GEO | 集成词，抢未来引用位 |

---

## 核心洞见

1. **品牌护城河**：Falco 品牌词（`falco security`, `falco kubernetes`）护城河很浅——月量 50-110，但 KD 已达 38-47，说明品牌认知度有但搜索量小。品牌词不适合正面刚，但"falco + 场景词"组合文值得做（读者是 DevOps/安全工程师，转化价值高）。`falco scan` 已排名第 1，是现成流量点。

2. **可复制的打法**：Falco 官网几乎不做 SEO 内容营销，完全靠文档站被动收录。可以复制的打法：**"开源安全工具对比列表文"**（`kubernetes security tools`、`open source kubernetes security tools`），以及 **"运行时安全教程文"**（`kubernetes runtime security`、`container runtime security`）——这类文章 Falco 官方自己完全没有做，是显著内容空白。

3. **对 Olares 最关键的 2-3 个词**：
   - `container runtime security`（720 vol, KD 20）——Olares 个人云容器的安全防护场景
   - `kubernetes security tools`（720 vol, KD 18）——工具列表文，Olares Market 可作为"跑这些工具的平台"
   - `open source container security`（110 vol, KD 13）——低 KD 开源信号词，Olares + Falco 自托管叙事完美契合

4. **最大攻击面**：Falco 是纯开源，商业方 Sysdig 在做付费推广（`falco security` CPC $14.57），说明 Sysdig 在品牌词上投广告抢流量。Olares 可以利用这个痛点：用户搜 Falco 想自托管，却被商业广告干扰——Olares Market 提供一键安装 Falco 的路径，既不用花钱又完全自控。

5. **隐藏低 KD 金矿**：
   - `cloud native runtime security`（50 vol, KD **11**）——Falco 的官方自描述词，竞争最低
   - `open source container security`（110 vol, KD **13**）——量与 KD 组合超值
   - `open source kubernetes security tools`（90 vol, KD **14**）——可直接用于 Olares 工具列表文
   - `falco rules` / `falco tutorial` / `falco helm`（各 20 vol, KD **0**）——Falco 教程词完全没竞争

6. **GEO 前瞻布局**：
   - `falco vs tetragon`（20 vol，CPC $33）——高 CPC 暗示商业价值极高，AI 工具选型 Overview 中此类对比词会被频繁引用
   - `ebpf security monitoring`（30 vol, KD 0）——eBPF 正快速升温，2026-2027 年此词搜索量将显著增长
   - `self-hosted runtime security monitoring` / `falco olares`（零量）——AI Overview 前沿布局词，抢未来引用位
   - Falco 0.44.0 的 Prempti（AI 编码 Agent + 安全检测结合）是新叙事，可以做 `ai agent security monitoring` 相关 GEO 内容

7. **与既有分析的关联**：当前 olares-500-keywords 词表以产品/功能/替代词为主，缺少安全类工具词。Falco 研究补充了 `container runtime security`、`kubernetes security tools`、`kubernetes runtime security` 三个可攻打的安全工具类词——这些词 CPC 高（$9-$24），说明目标读者（DevOps 工程师/安全团队）是高价值用户，与 Olares 的 SMB/高价值个人用户定位高度吻合。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_these、phrase_this）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
