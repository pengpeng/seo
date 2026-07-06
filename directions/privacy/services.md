# privacy/services.md — 隐私产品竞品总索引

> 对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 5（隐私）。本文件是**隐私产品竞品的单一导航入口**——用来找"privacy alternative / self-hosted / gdpr compliant / X vs Olares"这类内容切入点。
>
> **两层内容**：(1) **自有垂直报告**——数据隐私核心品类里未达 commerce 明星门槛的垂直工具，报告在 [reports/](/Users/pengpeng/seo/directions/privacy/reports)，走 `.cursor/skills/brand-seo-research/`；(2) **跨目录指针**——闭源商业明星归 [commerce](/Users/pengpeng/seo/directions/commerce/products.md)、开源平替归 [market](/Users/pengpeng/seo/directions/market)/[tech](/Users/pengpeng/seo/directions/tech/tech-stack.md)，此处只引用不重复登记（遵循 [AGENTS.md](/Users/pengpeng/seo/AGENTS.md) 可拥有性归类）。
> **边界**：数据隐私**核心品类**（搜索浏览器 / 邮件 / 存储 / 合规）做主体；**相邻品类**（密码管理、VPN / 远程访问）只做指针，不当主体、不在 privacy 建报告。**话题格局**（合规立法 / 认证 / 泄露 / AI / 巨头 / 概念 / 企业）不在本清单——见 [landscape.md](/Users/pengpeng/seo/directions/privacy/landscape.md) 与 [research/](/Users/pengpeng/seo/directions/privacy/research)。
>
> 状态：✅ 已有报告（数据为历史快照，引用前需重跑核实）。**自有报告内容待用户后续修订。**

---

## 核心品类（自有报告为主体）

### 隐私搜索 / 浏览器

| 产品 | 场景 | Olares 平替角度 | 报告 |
|------|------|----------------|------|
| Brave | 隐私浏览器 / 搜索 / VPN | SearXNG on Olares，私有搜索自托管 | ✅ [brave](/Users/pengpeng/seo/directions/privacy/reports/brave.md) |
| DuckDuckGo | 私有搜索 / 匿名浏览 | Perplexica on Olares，本地 AI 搜索无追踪 | ✅ [duckduckgo](/Users/pengpeng/seo/directions/privacy/reports/duckduckgo.md) |
| Startpage | 匿名浏览 / 元搜索 | SearXNG on Olares，元搜索无追踪 | ✅ [startpage](/Users/pengpeng/seo/directions/privacy/reports/startpage.md) |

### 加密邮件 / 别名 / 协作

| 产品 | 场景 | Olares 平替角度 | 报告 |
|------|------|----------------|------|
| Tuta | 私有邮件（原 Tutanota） | Stalwart Mail on Olares，本地私有邮件服务器 | ✅ [tuta](/Users/pengpeng/seo/directions/privacy/reports/tuta.md) |
| SimpleLogin | 邮件别名 | SimpleLogin self-hosted on Olares | ✅ [simplelogin](/Users/pengpeng/seo/directions/privacy/reports/simplelogin.md) |
| CryptPad | 加密文档协作 | OnlyOffice / CryptPad on Olares | ✅ [cryptpad](/Users/pengpeng/seo/directions/privacy/reports/cryptpad.md) |
| Proton Mail ↗ | 隐私邮件（估值 >$1B） | Olares Mail / Stalwart | 指针 → [commerce](/Users/pengpeng/seo/directions/commerce/products.md) #40 / #57 |

### 加密云存储

| 产品 | 场景 | Olares 平替角度 | 报告 |
|------|------|----------------|------|
| Internxt | 加密云存储（免费工具引流） | Olares Drive，数据永在自己硬件 | ✅ [internxt](/Users/pengpeng/seo/directions/privacy/reports/internxt.md) |
| Tresorit | 加密云存储（企业向，高 CPC） | Olares Drive，本地零知识存储 | ✅ [tresorit](/Users/pengpeng/seo/directions/privacy/reports/tresorit.md) |
| Mega.nz ↗ | 端到端加密存储 | Olares Drive | 指针 → [commerce](/Users/pengpeng/seo/directions/commerce/products.md) #57 |
| Proton Drive ↗ | 加密存储（Proton 套件） | Olares Drive | 指针 → [commerce](/Users/pengpeng/seo/directions/commerce/products.md) #57 |

### 合规 / GDPR

| 产品 | 场景 | Olares 平替角度 | 报告 |
|------|------|----------------|------|
| gdpr.eu / OneTrust / Termly / Iubenda | GDPR 合规 / 数据隐私 | 数据主权/私有部署满足合规（企业向，见 [场景 8](/Users/pengpeng/seo/scenarios/scenarios.md)） | ✅ [gdpr](/Users/pengpeng/seo/directions/privacy/reports/gdpr.md) |
| HIPAA 合规 + 自托管 / 医疗数据隐私 | 美国医疗 PHI 合规，AI Scribe / 本地 LLM 无 BAA 路径 | Olares + Ollama + Whisper = PHI 不出设备，消灭 BAA 链 | ✅ [hipaa-self-hosted](/Users/pengpeng/seo/directions/privacy/reports/02-certification/hipaa-self-hosted.md) |

### AI 训练数据隐私 / Opt-Out

| 话题 | 场景 | Olares 落点 | 报告 |
|------|------|------------|------|
| ChatGPT / AI 聊天机器人训练数据隐私 | ChatGPT 默认对话训练、GDPR 合规担忧、用户 opt-out 诉求 | 本地 Ollama + Open WebUI on Olares = 对话不进训练管线，零 opt-out 需求 | ✅ [chatgpt-gdpr-training](/Users/pengpeng/seo/directions/privacy/reports/04-ai-privacy/chatgpt-gdpr-training.md) |

### 需求 / 关键词总览

| 报告 | 场景 | 报告 |
|------|------|------|
| 隐私需求关键词 | 用户隐私诉求 + Olares 结合点（digital sovereignty 等） | ✅ [privacy-keywords](/Users/pengpeng/seo/directions/privacy/reports/privacy-keywords.md) |

---

## 相邻品类（仅指针，不当主体，登记在别处）

> 这两类与隐私强相关，但产品实体登记在别处（闭源→commerce、开源→market/tech）。此处只做导航，**不在 privacy 建报告**。

### 密码管理

| 产品 | 归属 | Olares 平替 |
|------|------|------------|
| 1Password / Bitwarden / Dashlane | [commerce](/Users/pengpeng/seo/directions/commerce/products.md) #56 | Vaultwarden（双形态）/ KeePassXC |
| Vaultwarden / KeePassXC（开源平替） | [commerce/reports](/Users/pengpeng/seo/directions/commerce/reports) / [market](/Users/pengpeng/seo/directions/market) | Vaultwarden on Olares |

### VPN / 远程访问 / 隧道

| 产品 | 归属 | Olares 平替 |
|------|------|------------|
| Tailscale / Ngrok / NordVPN / ExpressVPN / Cloudflare Zero Trust | [commerce](/Users/pengpeng/seo/directions/commerce/products.md) #57 | Headscale / frp / LarePass / Olares 内置反代 |
| Headscale / frp（开源平替） | [tech](/Users/pengpeng/seo/directions/tech/tech-stack.md) | 内网穿透 / mesh VPN 自托管 |

---
> 共 10 份**自有产品竞品**报告（核心品类）。相邻品类（密码 / VPN / 远程访问）与已达 commerce 明星门槛的隐私 SaaS（Proton / Mega 等）实体登记在 [commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md)，本索引只引用不重复。写新报告或重跑数据走 `.cursor/skills/brand-seo-research/`（重写前先读旧报告、保留去重旧洞见）。
>
> **分工**：本文件 = 隐私**产品竞品**总索引（brand-seo）；[landscape.md](/Users/pengpeng/seo/directions/privacy/landscape.md) = 隐私**话题格局**（合规/事件/概念/企业，借势做内容）；[commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md) = 闭源商业产品的**实体登记**。三者互补，不重复。
