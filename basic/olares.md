# basic/olares.md — Olares 产品认知与品牌口径

> 写任何 Olares 内容前先读这份：产品认知（是什么/给谁/核心用例）、品牌口径、写作规范、基本事实都在这。不堆底层技术，组件名/架构见 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)。

## 是什么

Olares 是**个人云操作系统**——介于"个人电脑（PC）"与"公有云"之间的**第三种形态**：

- 像公有云一样**随时随地在线**、能跑重负载（本地 LLM、Agent、各类服务）；
- 又像个人电脑一样**硬件与数据完全归用户自己**。

所以它既不是 NAS、也不是 AI PC，而是"你自己拥有的一朵云"。

## 核心用例：跑 Personal Agent

Olares 上最大的用户价值是运行**私人 AI Agent**——一个代你行动、掌握你全部上下文的私人智能体。产品的一切能力，最终都服务于"让这个 Agent 跑得更好"。

### 在 Olares 上跑 Personal Agent 的 6 个优势

1. **隐私**——本地 LLM，数据与推理都不出设备。
2. **全上下文**——能存下用户的全部数据与上下文，Agent 越用越懂你。
3. **随时随地可连接**——把家里的智能家居、你的电脑/手机、眼镜等 IoT 设备都连进来，由 Agent 统一编排。
4. **工具丰富**——大量应用可直接作为 Agent 的 tool。
5. **安全**——基于沙盒 + 云原生最佳实践。
6. **简单**——自然语言操作，不用看文档。

## Olares One（硬件）

软硬一体、一站式的本地 AI 解决方案——像苹果一样，把系统与硬件打包成开箱即用的整体体验，用户不用自己拼装。规格/定价以 https://one.olares.com/ 为准：

| 项 | 参数 |
|----|------|
| GPU | RTX 5090 Mobile，24GB GDDR7，最高 175W，1824 AI TOPS |
| CPU | Intel Core Ultra 9 275HX（24 核，5.4GHz） |
| 内存 | 96GB DDR5 5600（可升 128GB） |
| 存储 | 2TB NVMe PCIe 4.0（可扩展） |
| 接口 | Thunderbolt 5 / 2.5G 网口 / USB-A / HDMI 2.1；Wi-Fi 7 |
| 噪音/功耗 | 空载 19dB、满载 <39dB；待机 30W |
| 体积/重量 | 320×197×55mm，2.15kg｜3.5L |
| 价格 | $3,999 |

## 目标用户

- **高价值个人用户**：认为自己的数据重要、愿意拥有属于自己的 AI。
- **SMB（中小企业）**。
- **大企业**。

## 产品全景（生态版图）

| 层 | 名称 | 说明 |
|----|------|------|
| 核心 OS | `beclab/Olares` | 开源个人云操作系统本体 |
| 应用目录 | `beclab/apps` | 社区 PR 上架的应用市场目录 |
| API 契约 | `beclab/api` | OlaresManifest / CRD 的类型定义 |
| 客户端 | **LarePass** | iOS/Android/macOS/Windows/Linux 跨端客户端：身份、远程访问、VPN、文件、密码 |
| 云端 | **Olares Space** | 域名、备份、账单等托管管理 |
| 硬件 | **Olares One** | 官方自研本地 AI 一体机（规格见上方 Olares One 一节） |

## 官方站点

- 官网 https://www.olares.com/
- 硬件 https://one.olares.com/
- 文档 https://docs.olares.com/
- 应用市场 https://market.olares.com/
- 代码 https://github.com/beclab/Olares ｜ 应用 https://github.com/beclab/apps

## 基本事实（引用前以 olares.com / docs.olares.com / GitHub 核实）

开源 **AGPL-3.0** ｜ 2022 年诞生 ｜ 系统要求 Ubuntu 24.04 LTS+ / Debian 11+ ｜ 版本语义化、月度稳定版，当前世代 **1.12.x**。

---

# 品牌口径（写对外文案前读这段）

## 品牌叙事（Q2 2026 定调）

> **From a Self-Hosted, Personal Cloud OS → a Natural-Language-Driven, Agent-Native OS.**
> 从"自托管的个人云操作系统" → "自然语言驱动的、为 Agent 而生的操作系统"。

## 品牌语气：向往感 > 功能罗列

先给愿景与感受、再给功能（向往感 > 功能罗列）：

- ❌ 功能型（别用来打头）：私有云、自托管、Kubernetes、NAS 替代、开源操作系统
- ✅ 向往型（campaign 主打）：拥有你的 AI、用你的话指挥你的世界、你的 AI 永远属于你、把云装进自己家

## 品牌 Slogan（aspirational，主推）

英文（campaign）：
- **Own your AI. Own your world.**
- **Your AI. Your hardware. Your words.**
- **From owning your data to owning your AI.**
- **The personal AI cloud you command in your own words.**
- **Stop renting intelligence. Start owning it.**

中文（campaign）：
- **拥有你的 AI，拥有你的世界。**
- **你的 AI，你的硬件，你说了算。**
- **从掌控数据，到掌控 AI。**
- **一句话，指挥你自己的 AI 世界。**

> 以上是内部提炼的品牌方向候选，用于我们自己的推广文案，**不是官网现有文案**。对外正式引用官方措辞时用下方 verbatim 列表。

## 官方措辞（verbatim，事实/直接引用时用）

- Mission：**"Let people own their data again."**
- "An Open-Source Personal AI Cloud OS — Let people own AI by owning their data."
- "Olares is the sovereign cloud that puts you in control."
- "An open-source, self-hosted alternative to public clouds like AWS."
- Olares One：**"Own your AI."** / **"Stop Renting. Save 96% on Your AI Stack."** / "World's Best Desktop to Run OpenClaw Locally."

---

# 写作规范与口径

**品牌措辞与大小写**（务必正确）：
- `Olares`（不是 Olayes/OLares/olares 开头句）｜`Olares One`（硬件，别只写 One）｜`LarePass`（不是 LarPass）｜`Olares ID`｜`Olares Space`｜`Olares Market`
- 英文：品牌/首屏用向往型（Agent-Native OS、Own your AI，见上方品牌口径）；技术/事实语境才用 personal cloud OS / sovereign cloud。中文用"个人云操作系统 / Agent-Native OS"。别把 Olares 说成 NAS 或 PC/AI PC。
- **不堆底层技术组件名**：Authelia+LLDAP、K3s、JuiceFS、MinIO、HAMi、OPA 等是**长尾 SEO 词**，集中在 [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md)（方向 6），可单独做技术文但不作主线卖点。

**选词/内容打法**：暂无独立方法论文档，先按各方向洞见（[directions.md](/Users/pengpeng/seo/directions/directions.md)）与 skills 流程走。
**SEO 报告规范**：品牌/SaaS 沿用 `.cursor/skills/brand-seo-research/`、开源模型用 `.cursor/skills/model-seo-research/`；文件命名 `<brand>.md`（无前缀、无日期，git 记录变更；Market 应用→`directions/market/reports/`、商业竞品→`directions/commerce/reports/`、模型→`directions/model/reports/`），抬头注明域名/数据库/数据快照日期；数据一律来自 **Semrush（MCP `user-semrush`，需登录）**，搜索量为**美国月均**。**重写已有报告时先读旧报告，保留并去重旧洞见，不认可的旧结论可明确指出**。

**保密红线**：官网 / docs.olares.com / GitHub 上找不到的信息一律当内部信息，不写进任何对外内容（未发布的版本号与时间表、财务/销售数据、未公布硬件与代号、未公开的商业/认证/供应链安排）。
