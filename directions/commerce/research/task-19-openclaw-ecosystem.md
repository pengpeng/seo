# dig-19 · OpenClaw *Claw 生态 · 发现蒸馏笔记

**AS_OF=2026-07-04** · 只做发现+财务，不做最终分类。品类锚 = OpenClaw（381K★，MIT，2026-01 定名）。

## Sources（节选）
GitHub 官方（OpenClaw/NemoClaw/NanoClaw/QwenPaw/Hermes/LobsterAI）/ NVIDIA IR / BusinessWire(Genspark) / SiliconANGLE / TechCrunch(NanoCo/Poke) / VentureBeat(KiloClaw) / MarkTechPost(Kimi Claw) / arXiv 2604.03131（中国 *Claw 变体清单）/ Tracxn·GetLatka·BI（财务）。

## Products（门槛：ARR>$50M｜估值>$200M｜融资>$20M｜大厂旗舰）

### 品类锚 & 大厂加固栈
| 名称 | 公司 | 开源/许可 | 财务 | 命中 | 关系 |
|------|------|-----------|------|------|------|
| **OpenClaw** | OpenClaw Foundation | MIT，381,674★ | 无融资 | 品类锚 | 定义者 |
| **NVIDIA NemoClaw** | NVIDIA | Apache-2.0，21,594★ | 大厂内部 | **大厂旗舰** | 加固栈（OpenShell 沙箱 + Nemotron 路由，非替代品） |

### 商业云托管竞品
| 名称 | 公司 | 开源 | 财务 | 命中 | 关系 |
|------|------|------|------|------|------|
| **Genspark Claw** | Mainfunc（Genspark） | 否 | ARR **$250M**；估值 **$2.6B**；累计融资 $460–645M[u] | **ARR✓估值✓融资✓** | 强对标（全托管，每用户专属云电脑 + Workspace） |
| **Kimi Claw** | Moonshot | 否（托管 OpenClaw 原生） | 母体 ARR $200M+；估值 $20B；融资 $3.9B | **大厂旗舰·估值✓** | 托管 wrapper（浏览器一键 + 40GB + ClawHub） |
| **MaxClaw** | MiniMax（上市） | 否 | 上市公司；SKU 财务[u] | **大厂旗舰** | 托管 wrapper（锁 M2.5 + 50GB） |
| **ArkClaw** | 字节/火山引擎 | 否 | 内部；收入[u] | **大厂旗舰** | 企业托管 wrapper（深绑飞书，VPC/SSO） |
| **Poke** | Interaction Co. | 否 | 累计 $25M；估值 $300M | **估值✓融资✓** | 强对标（纯短信入口 "OpenClaw for normies"） |

### 开源强对标分叉 & 安全变体
| 名称 | 公司 | 开源 | 财务 | 命中 | 关系 |
|------|------|------|------|------|------|
| **NanoClaw** | NanoCo | MIT[u]，30,121★ | Seed $12M；估值 $62M | 未达标 | 强对标（容器隔离轻量，~500 行核心） |
| **Hermes Agent** | Nous Research | MIT，209,000★ | 累计 $65–70M[u]；token 估值 $1B | **融资✓** | 边界（自进化 skill，常与 OpenClaw 混跑） |
| **QwenPaw**（原 CoPaw） | 阿里通义/AgentScope | Apache-2.0，~20,431★ | 阿里内部 | **大厂旗舰** | 强对标（阿里版 OpenClaw，本地/云双模 + ReMe 记忆） |
| **LobsterAI** | 网易有道 | 开源桌面壳，5,438★ | 内部 | **大厂旗舰** | 边界（中国桌面 GUI 版 OpenClaw） |
| **ZeroClaw / PicoClaw** | zeroclaw-labs / Sipeed | Apache/MIT，32K/30K★ | 融资[u] | 未达标 | 强对标（Rust/Go 超轻量运行时） |
| **TrustClaw** | Composio | MIT，~826★ | 母体累计 $29M | 未达标（SKU 独立ARR无） | 强对标（OAuth+远程沙箱，托管已关） |
| **Moltworker** | Cloudflare | 开源，9,916★ | 大厂内部 | **大厂旗舰** | 托管 wrapper（跑 CF Workers 边缘） |

### 大厂本地化包装（中国）
QClaw（腾讯，微信/QQ 遥控本机，大厂旗舰）、AutoClaw（智谱，一键安装器，大厂旗舰）、WorkBuddy（腾讯）——均边界/发行版包装。

### 托管 wrapper 层（普遍未达标）
**KiloClaw**（Kilo Code，$8M seed，Fly.io + 500+ 模型零加价，最强 wrapper）；ClawNest / ActivateClaw / SimpleClaw / RapidClaw / MyClaw.ai / Duet + 行业称 **35+** 小托管商（价格/地域套利，moat 薄）。

### 相邻商业跟随（非 *Claw 命名）
Vellum PI（$25M，融资✓，记忆优先）、Manus Agents（Meta 收购>$2B，ARR $400–500M[u]，边界通用 agent）。

## 生态结构小结
- **达标商业竞品**：Genspark Claw（唯一 verified ARR>$50M 的 *Claw SKU，**最强**）、Kimi Claw、MaxClaw、ArkClaw（后三为大厂旗舰）、Poke（估值达标）。
- **大厂加固栈**：NemoClaw（唯一大厂级安全 reference stack，与 OpenClaw 基金会正式合作）。
- **大厂旗舰开源对标**：QwenPaw（阿里）、LobsterAI（有道）、Moltworker（CF）。
- **创业开源**：NanoClaw（$12M 未达标但安全叙事最强）、Hermes（$65M 达标，边界）。
- **托管 wrapper**：KiloClaw 最强，其余套利层未达标。

## Olares 侧自托管平替（both 归 NemoClaw 关键）
- **OpenClaw（自托管）+ NVIDIA NemoClaw（OpenShell 沙箱，本地 RTX/DGX/Olares One 24/7）+ Hermes**：商业 *Claw 云的收件箱体验，但硬件/记忆/通道凭证全归用户。
- 替代栈：QwenPaw（中文办公）/ NanoClaw（容器强隔离）。
- **NemoClaw 是最贴 Olares One 叙事的样本**：开源 + 本地算力 + deny-by-default 网络 + 本地 Nemotron 路由，直接对标云托管的安全/数据主权缺口。

## Gaps
- Genspark 累计融资口径冲突（$460M/$535M/$645M；Series B 扩展 $485M 有背书）；Kimi Claw 独立 ARR 未拆分。
- 托管层几乎无财务披露；NanoClaw 许可/KiloClaw 独立收入/QwenPaw 内部预算未核实。
- 命名噪声：maxclaw.co 疑非官方 SEO 站；CoPaw→QwenPaw 已更名；Manus 被 NDRC 要求 unwind Meta 收购（动态）。
- 未覆盖：OpenAI next-gen personal agents（Steinberger 主导，无产品页）、印度/东南亚/日韩独立 *Claw。
