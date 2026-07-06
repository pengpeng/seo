# ExpressVPN SEO 竞品分析报告

> 域名：expressvpn.com | SEMrush US | 2026-07-06
> ExpressVPN = 消费级 VPN 领域高端品牌（Kape Technologies 旗下），主打流畅体验与 105 国服务器，是最贵的一线 VPN 之一

---

## 项目理解（前置）

ExpressVPN 成立于 2009 年、2021 年被英以两国数字安全公司 Kape Technologies 以约 9.36 亿美元收购，目前仍以独立品牌运营。它主打"最易用、网速最快"的消费级 VPN，覆盖 105 个国家 3,000+ 服务器，自研 Lightway 协议（基于 WolfSSL，已过 KPMG 三次第三方审计）。2026 年产品线升级为三档套餐（Basic/Advanced/Pro），捆绑密码管理、邮件中继、身份保护、专属 IP 等，走向"隐私全家桶"。Kape 母公司同时拥有 CyberGhost、Private Internet Access 等多个 VPN 品牌，总营收估算 $725–930M。

**SEO 最关键特征**：ExpressVPN 的最大流量来源不是 VPN 关键词，而是免费工具页——`/what-is-my-ip` 单页月贡献超 160 万 US 访问（`what is my ip` 全球月量 6,800 万），`/password-generator` 贡献近 2 万访问。此程序化工具流量策略是核心竞争壁垒，也是最值得研究的可复制打法。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 消费级高端 VPN，以极简体验、流媒体解锁、105 国覆盖著称；近年向"数字隐私全家桶"转型 |
| 开源 / 许可证 | 闭源商业产品；Lightway 协议核心库（WolfSSL）开源，但客户端与服务端均闭源 |
| 主仓库 | 无公开仓库（协议规格文档在官网）|
| 核心功能 | ① Lightway 协议（速度/安全）② 105 国 3,000+ 服务器 ③ TrustedServer（全 RAM 无日志）④ 分离隧道 ⑤ Kill Switch ⑥ 后量子加密（PQC）|
| 商业模式 / 定价 | Basic 2yr: $2.49/mo；Advanced 2yr: $2.99/mo；Pro 2yr: $5.49/mo（首期促销后年续费 $99.95–$199.95）|
| 差异化 / 价值主张 | 最易用的 UI、最佳流媒体解锁、30 天退款保证、专属 IP 可加购 |
| 主要竞品（初判）| NordVPN（速度/性价比最强）、Surfshark（最便宜无限设备）、Proton VPN（隐私最透明/开源客户端）、Mullvad（匿名度最高） |
| Olares Market | 未上架（Olares 内置 Headscale + WireGuard 作为开源平替）|
| 来源 | [expressvpn.com/pricing](https://www.expressvpn.com/pricing)、[expressvpn.com/blog/expressvpn-officially-joins-kape/](https://www.expressvpn.com/blog/expressvpn-officially-joins-kape/)、[mashable.com/review/express-vpn](https://mashable.com/review/express-vpn)、[cnet.com/tech/services-and-software/best-vpn/](https://www.cnet.com/tech/services-and-software/best-vpn/) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | expressvpn.com |
| SEMrush Rank | **1,238**（全球前 1,500，SEO 绝对头部） |
| 自然关键词数 | 131,508 |
| 月自然流量（US）| **2,114,661** |
| 自然流量估值 | **$1,990,134/月** |
| 付费关键词数 | 3,478 |
| 月付费流量 | 281,769 |
| 付费流量成本 | $817,394/月 |
| 排名 1-3 位 | 3,245 词 |
| 排名 4-10 位 | 17,811 词 |
| 排名 11-20 位 | 24,770 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| www.expressvpn.com（主站）| 131,376 | 2,114,263 | **99.98%** |
| store.expressvpn.com | 103 | 369 | 0.02% |
| portal.expressvpn.com | 10 | 27 | <0.01% |
| connectivitycheck.expressvpn.com | 13 | 2 | <0.01% |
| checkout.expressvpn.com | 6 | 0 | 0% |

> 主站几乎垄断全部流量，子域名完全可忽略。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|-----|------|------|-----|
| what is my ip | 5 | 68,000,000 | 100 | $0.94 | **1,632,000** | 信息 | /what-is-my-ip |
| express vpn | 1 | 27,100 | 0 | $0 | 21,680 | 品牌 | / |
| password generator | 9 | 823,000 | 76 | $0.08 | 19,752 | 信息 | /password-generator |
| whats my ip | 4 | 301,000 | 92 | $0.34 | 19,565 | 信息 | /what-is-my-ip |
| what is my ip address | 10 | 823,000 | 90 | $0.13 | 15,637 | 信息 | /what-is-my-ip |
| my ip address | 4 | 201,000 | 89 | $0.49 | 13,065 | 信息 | /what-is-my-ip |
| my ip | 5 | 368,000 | 89 | $0.84 | 12,880 | 信息 | /what-is-my-ip |
| expressvpn login | 1 | 12,100 | 38 | $0.54 | 9,680 | 商业/导航 | / |
| vpn service | 5 | 550,000 | 97 | $11.00 | 7,150 | 信息 | / |
| expressvpn download | 1 | 6,600 | 77 | $1.84 | 5,280 | 信息/转化 | /vpn-download |
| myip | 5 | 110,000 | 94 | $0.84 | 4,840 | 信息 | /what-is-my-ip |
| whats my ip address | 3 | 74,000 | 90 | $0.30 | 4,810 | 信息 | /what-is-my-ip |
| download express vpn | 1 | 4,400 | 76 | $0 | 3,520 | 商业 | /vpn-download |
| expres vpn | 1 | 4,400 | 82 | $0 | 3,520 | 品牌（误拼）| / |
| express vpn trial | 1 | 4,400 | 39 | $0 | 3,520 | 信息 | /features/vpn-trial |
| express vpn sign in | 1 | 3,600 | 33 | $0 | 2,880 | 导航 | / |
| express vpn download pc | 1 | 3,600 | 75 | $0 | 2,880 | 转化 | /vpn-download/vpn-windows |
| expressvpn | 1 | 90,500 | 89 | $1.92 | 2,353 | 品牌 | / |
| express vpn for pc | 1 | 2,900 | 79 | $0 | 2,320 | 信息 | /vpn-download/vpn-windows |
| vpn | 10 | 823,000 | 100 | $5.02 | 1,234 | 信息 | / |
| what is vpn passthrough | 7 | 60,500 | 36 | $0 | 1,452 | 信息 | /blog/vpn-passthrough/ |
| mesh network | 13 | 550,000 | 61 | $0.90 | 825 | 信息/商业 | /blog/what-is-mesh-network/ |
| what is a vpn router | 8 | 90,500 | 61 | $0 | 814 | 信息 | /vpn-download/vpn-router |
| saved passwords | 4 | 33,100 | 54 | $1.38 | 1,456 | 信息 | /blog/how-to-find-saved-passwords/ |

**关键洞察**：自然流量中 **~77%** 来自 `what is my ip` 系列词（/what-is-my-ip 单页），这是极其激进的免费工具导流策略——用全球最高搜量工具页引流，再做 VPN 转化。`/password-generator` 是同类第二个工具页。品牌词 `expressvpn`（9 万月量）本站只获得 2,353 traffic（排名 #1 但量巨大时流量分散），是因为大量用户直接访问而非搜索。

### 付费词（Google Ads，按流量排序）

ExpressVPN 的 Ads 策略：重金买"vpn"大词（$5.80 CPC）和"vpn service"（$10.42 CPC），所有落地页统一导向 `/start/homepage` 或 `/start/vpn-trial`——以免费试用作为漏斗顶部。竞品词投放策略包含 `mozilla vpn`（CPC $2.59，导向 Firefox 扩展页）。

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| vpn | 1 | 823,000 | $5.80 | /start/vpn-trial |
| vpn service | 1 | 201,000 | $10.42 | /start/homepage |
| expressvpn | 1 | 90,500 | $2.03 | /start/vpn-trial |
| best vpn | 1 | 49,500 | — | /start/homepage |
| free vpn | 3-4 | 201,000 | $2.17-2.27 | /start/homepage |
| how to use a vpn | 2 | 90,500 | — | / |
| mozilla vpn | 1 | 22,200 | $2.59 | /vpn-download/firefox-vpn |
| vpn free trial | 1 | 14,800 | $7.58 | /start/vpn-trial |
| express vpn | 1 | 33,100 | — | /start/vpn-trial |
| vpn free | 2 | 60,500 | $2.37 | /start/homepage |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| nordvpn vs expressvpn | 1,900 | 51 | $1.91 | 信息 | VPN 对比最大量词 |
| expressvpn vs nordvpn | 1,600 | 50 | $2.04 | 信息 | 同族变体 |
| expressvpn price | 1,600 | 67 | $2.16 | 商业 | 高价痛点词 |
| expressvpn cost | 1,600 | 69 | $1.78 | 信息 | 高价痛点词 |
| expressvpn review | 1,000 | 75 | $4.22 | 信息 | 评测 |
| openvpn vs wireguard | 1,300 | 39 | $0.54 | 信息 | ⭐ 技术对比，低竞争 |
| expressvpn cancel | 590 | 60 | $2.08 | 信息 | 退订痛点 |
| cancel expressvpn | 590 | 63 | $3.02 | 信息 | 退订痛点变体 |
| expressvpn vs surfshark | 170 | **21** | $2.10 | 信息 | ⭐ 低竞争 vs 对比 |
| expressvpn vs protonvpn | 170 | 35 | $7.41 | 信息 | 高 CPC |
| nordvpn alternative | 170 | 38 | $2.68 | 信息 | 竞品替代词 |
| expressvpn vs nordvpn reddit | 140 | **27** | $0 | 信息/导航 | ⭐ 低竞争 Reddit 意图 |
| nordvpn vs expressvpn reddit | 110 | **29** | $0 | 信息/导航 | ⭐ 低竞争 Reddit 意图 |
| expressvpn vs mullvad | 70 | **16** | $0 | 信息 | ⭐ 极低竞争对比 |
| expressvpn alternative | 90 | 47 | $3.84 | 商业 | 直接替代词，高 CPC |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| wireguard vpn | 5,400 | 58 | $3.10 | 商业 | 品类主词 |
| open source vpn | 4,400 | 62 | $2.30 | 信息 | 开源 VPN 主词 |
| no log vpn | 1,600 | 61 | $0 | 商业 | 隐私导向 |
| best open source vpn | 320 | **32** | $2.48 | 商业 | ⭐ 低竞争机会词 |
| vpn alternative | 260 | 49 | $0 | 信息 | VPN 替代方案 |
| free wireguard vpn | 1,000 | **29** | $0 | 信息 | ⭐ 低竞争，免费意图 |
| privacy vpn | 1,000 | 67 | $0 | 商业 | 隐私 VPN |
| tailscale vs wireguard | 1,000 | **24** | $8.96 | 信息 | ⭐⭐⭐ 极低竞争+高 CPC |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| expressvpn | 90,500 | 89 | $1.92 | 品牌 | 强护城河，排不动 |
| expressvpn login | 12,100 | 38 | $0.54 | 导航 | 用户留存词 |
| expressvpn download | 6,600 | 80 | $1.84 | 转化 | 下载词 |
| expressvpn review | 1,000 | 75 | $4.22 | 信息 | 评测意图 |
| expressvpn cost | 1,600 | 69 | $1.78 | 信息 | 定价痛点 |
| expressvpn cancel | 590 | 60 | $2.08 | 信息 | 退订痛点 |
| expressvpn subscription | 1,000 | 63 | $3.03 | 商业 | 续费词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| tailscale vs wireguard | 1,000 | **24** | $8.96 | 信息 | ⭐⭐⭐ Headscale 对位词 |
| self hosted vpn | 590 | 45 | $0 | 信息 | 自托管 VPN 主词 |
| tailscale alternative | 390 | **19** | $3.10 | 信息 | ⭐⭐⭐ Headscale 直接机会 |
| tailscale alternatives | 320 | **19** | $6.67 | 信息 | ⭐⭐⭐ Headscale 直接机会 |
| best open source vpn | 320 | **32** | $2.48 | 商业 | ⭐ Headscale/WireGuard |
| self host vpn | 260 | **36** | $0 | 信息 | ⭐ DIY VPN |
| headscale vs tailscale | 210 | **24** | $0 | 信息 | ⭐⭐⭐ 直接 Headscale 品牌词 |
| headscale-ui | 260 | **18** | $0 | 信息 | ⭐⭐⭐ Headscale UI 安装词 |
| wireguard for windows | 590 | **27** | $3.17 | 信息 | ⭐ Windows 部署词 |
| free wireguard vpn | 1,000 | **29** | $0 | 信息 | ⭐⭐⭐ 免费 WireGuard |
| wireguard raspberry pi | 110 | **20** | $0 | 信息 | ⭐⭐⭐ DIY 部署词 |
| wireguard port | 590 | **32** | $0 | 信息 | ⭐ 配置词 |
| wireguard for tv | 880 | **13** | $0 | 信息 | ⭐⭐⭐ 极低竞争 |
| wireguard alternative | 50 | **16** | $9.06 | 信息 | ⭐⭐⭐ 极低 KD + 高 CPC |

---

## Olares 关联词（Phase 3）

**核心叙事切入点**：ExpressVPN 的最大痛点是价格高（月均 $6.67，年续费更贵）+ Kape Technologies 的历史信任隐患（前身 Crossrider 曾被认定参与广告注入网络）；Olares 的 Headscale + WireGuard 提供"自己的服务器、自己的密钥、零月订阅费"的完全自主替代——是"拒绝 Kape 信任链"用户的天然目标地。

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|-----|------------|
| tailscale vs wireguard | 1,000 | 24 | $8.96 | ⭐⭐⭐ Headscale = 自托管 Tailscale 控制服务器，Olares 内置，一键启用 |
| self hosted vpn | 590 | 45 | $0 | ⭐⭐⭐ Olares 内建 Headscale+WireGuard，部署即拥有私人 VPN |
| tailscale alternative | 390 | 19 | $3.10 | ⭐⭐⭐ Headscale 是最受推荐的 Tailscale 开源替代，已集成 Olares tech-stack |
| tailscale alternatives | 320 | 19 | $6.67 | ⭐⭐⭐ 同上，变体词 |
| headscale vs tailscale | 210 | 24 | $0 | ⭐⭐⭐ Olares 选择 Headscale 的具体理由：完全自托管、无账户依赖 |
| expressvpn alternative | 90 | 47 | $3.84 | ⭐⭐⭐ 强商业意图，正面攻击：Olares = 零月费自主 VPN 替代 |
| best open source vpn | 320 | 32 | $2.48 | ⭐⭐ Olares + Headscale/WireGuard 组合作为"最佳开源 VPN"候选 |
| wireguard raspberry pi | 110 | 20 | $0 | ⭐⭐ 同目标用户群：DIY 玩家，Olares One 是 Pi 的商用升级路径 |
| wireguard for windows | 590 | 27 | $3.17 | ⭐⭐ Olares 跨平台（Windows WSL2 支持），WireGuard 客户端一键接入 |
| free wireguard vpn | 1,000 | 29 | $0 | ⭐⭐⭐ Olares 内置 = 永久免费的 WireGuard 服务端，唯一成本是硬件 |
| nordvpn alternative | 170 | 38 | $2.68 | ⭐⭐ 同赛道，"不想给 NordSec 订阅费"用户的自托管出口 |
| openvpn vs wireguard | 1,300 | 39 | $0.54 | ⭐⭐ WireGuard 是 Olares 远程接入底层协议，内容可解释为何选 WG |
| expressvpn vs nordvpn | 1,600 | 50 | $2.04 | ⭐ 都是商业 VPN；Olares 可切入"两者都是订阅陷阱"的第三视角 |
| expressvpn cancel | 590 | 60 | $2.08 | ⭐⭐ 退订意图最纯，转化点："取消后改用 Headscale 自托管" |
| wireguard for tv | 880 | 13 | $0 | ⭐⭐ 极低 KD，Olares 输出的 WireGuard 配置可用于 TV/路由器 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| tailscale vs wireguard | 1,000 | 24 | $8.96 | 信息 | **主词候选** | KD 极低+CPC 极高，搜 Headscale 受众最精准；Olares 内置 Headscale 天然具有对比优势 |
| free wireguard vpn | 1,000 | 29 | $0 | 信息 | **主词候选** | KD<30，量适中，"零费用 WireGuard"意图与 Olares 自托管叙事完美对齐 |
| tailscale alternative | 390 | 19 | $3.10 | 信息 | **主词候选** | KD=19 极低，高商业价值，Headscale 是公认第一替代，Olares 一键部署 |
| tailscale alternatives | 320 | 19 | $6.67 | 信息 | 次级 | 上词变体，并入同簇 |
| best open source vpn | 320 | 32 | $2.48 | 商业 | **主词候选** | KD 刚过 30 但商业意图强，Headscale+WireGuard 是最强开源组合 |
| self hosted vpn | 590 | 45 | $0 | 信息 | **主词候选** | 量够、与 Olares 场景最直接；Olares 500 词表中已收录 |
| openvpn vs wireguard | 1,300 | 39 | $0.54 | 信息 | **主词候选** | 量大 KD 合理，技术对比文章，可植入 Headscale/Olares 作为落脚点 |
| nordvpn vs expressvpn | 1,900 | 51 | $1.91 | 信息 | 次级 | 量最大的 VPN 对比词，KD 偏高；可作"不如自托管"文章的次级切入 |
| expressvpn vs nordvpn | 1,600 | 50 | $2.04 | 信息 | 次级 | 上词变体，同簇 |
| expressvpn alternative | 90 | 47 | $3.84 | 商业 | **主词候选** | 量小但高商业意图 + 高 CPC；战略价值 > 量，攻击ExpressVPN 直接替代位 |
| headscale vs tailscale | 210 | 24 | $0 | 信息 | **主词候选** | 低 KD，Headscale 品牌词，Olares 是最完整的 Headscale 发行版 |
| headscale-ui | 260 | 18 | $0 | 信息 | 次级 | 极低 KD，安装教程意图，可做 headscale 文章 H2 |
| wireguard raspberry pi | 110 | 20 | $0 | 信息 | 次级 | KD 超低，DIY 部署词，Olares One 是 Pi 的升级版 |
| wireguard for tv | 880 | 13 | $0 | 信息 | 次级 | KD=13 最低，量达 880；Olares 生成的 WireGuard config 可直接用于 TV |
| wireguard alternative | 50 | 16 | $9.06 | 信息 | GEO | 量小但 CPC 极高（$9.06），AI Overview 引用位值得抢 |
| expressvpn cancel | 590 | 60 | $3.02 | 信息 | 次级 | 退订痛点词，KD 偏高；可作替代文章的 H2 触点 |
| expressvpn vs surfshark | 170 | 21 | $2.10 | 信息 | 次级 | ⭐ 极低 KD，可作 "商业 VPN 对比 → 自托管出路" 段落 |
| expressvpn vs mullvad | 70 | 16 | $0 | 信息 | GEO | KD=16，近零竞争，高隐私意图，Olares 走隐私叙事的精准前哨 |
| wireguard for windows | 590 | 27 | $3.17 | 信息 | 次级 | 平台部署词，Olares WSL2 支持+WireGuard 客户端可接入 |
| wireguard port | 590 | 32 | $0 | 信息 | 次级 | 技术配置词，教程内容 |
| nordvpn alternative | 170 | 38 | $2.68 | 信息 | 次级 | 与 expressvpn alternative 同赛道，同簇可收 |

---

## 核心洞见

1. **品牌护城河**：`expressvpn` 自然月量 90,500（KD=89），是绝对的护城河——正面刚 VPN 品牌词完全无意义。Olares 的入口是"订阅痛点"（高价、Kape 信任问题、数据控制权）和"技术导向用户的自托管意愿"，不是品牌流量竞争。

2. **可复制的打法**：
   - **程序化工具页（首要洞察）**：`/what-is-my-ip` 单页贡献 **~77% 的自然流量**（160 万 US/月），本质是用免费工具抢占超高搜量信息词作为流量漏斗顶部。这个模式完全可复制——Olares 可以做同类工具页（IP 查询、DNS 泄漏检测、VPN 检测等）将 WireGuard/Headscale 受众引入。
   - **自由试用 + 落地页矩阵**：付费词全导向 `/start/vpn-trial`，转化漏斗清晰；Ads 买"free vpn"（CPC $2.17）也验证了"用免费意图导流付费产品"的策略。
   - **平台专属下载页**（`/vpn-download/vpn-windows`、`/vpn-download/vpn-mac`、`/vpn-download/vpn-router`）：程序化落地页按平台拆分，批量覆盖安装词。

3. **对 Olares 最关键的 3 个词**：
   - `tailscale alternative`（390 vol, KD=19）：Headscale 是公认的 Tailscale 开源自托管替代，Olares 是最完整的 Headscale 发行版，可以争取这个词的排名。
   - `self hosted vpn`（590 vol, KD=45）：在 Olares 500 词表已收录，Olares One + Headscale 是最完整的"自托管 VPN"一体机方案。
   - `free wireguard vpn`（1,000 vol, KD=29）：搜此词的用户已决定用 WireGuard 且不想付钱，Olares 一次性购买的叙事是最佳接球点。

4. **最大攻击面**：
   - **价格**：ExpressVPN 是市场最贵 VPN 之一（$6.67/mo 年付），NordVPN 同功能仅 $3.39/mo；大量用户搜 `expressvpn cost`（1,600）、`expressvpn cancel`（590）、`cancel expressvpn`（590）——这些都是主动离网意图。
   - **Kape 信任问题**：Kape 前身 Crossrider 曾被 Google/UC Berkeley 研究认定参与广告注入网络；收购多个 VPN 品牌（CyberGhost、PIA、ExpressVPN）但对用户来说数据仍汇聚同一母公司；这是深度隐私敏感用户的硬痛点。
   - **闭源协议**：Lightway 协议虽经审计，但服务端完全闭源——对"真正不信任第三方"的用户，Headscale+WireGuard（完全开源、RFC 已发布）是唯一替代。

5. **隐藏低 KD 金矿**：
   - `wireguard for tv`（880 vol, KD=**13**）：量近千、竞争度极低，搜此词的用户要在智能电视上用 WireGuard，Olares 输出的 WireGuard config 可以直接满足。
   - `wireguard alternative`（50 vol, KD=**16**, CPC=$9.06）：量虽小，但 $9 CPC 说明有商业价值，且竞争极低——GEO 抢占 AI Overview 高效。
   - `headscale-ui`（260 vol, KD=**18**）：几乎无竞争，Olares 内置 Headscale 的 UI 管理界面可以直接覆盖。
   - `expressvpn vs mullvad`（70 vol, KD=**16**）：极低竞争+隐私极客意图，"两者都是商业闭源" → 第三视角自托管插入点。

6. **GEO 前瞻布局**：适合抢 AI Overview/Perplexity 引用位的近零量词：
   - `"is expressvpn owned by kape"` / `"kape technologies vpn privacy"`（月量 0，但 Perplexity 常被问）
   - `"wireguard vs expressvpn"` / `"headscale vs expressvpn"`（近零量，语义精准）
   - `"expressvpn vs wireguard"` / `"replace expressvpn with wireguard"`
   - `"does expressvpn collect data"` / `"expressvpn kape data"`（隐私关注核心问题）
   - `"wireguard alternative"`（量 50，KD=16，已列主表，FAQ 必收）

7. **与既有 olares-500-keywords 词表的关联**：
   - 500 词表中已收录 `headscale`（2,900 vol, KD=33，B 类）、`tailscale alternative`（390, KD=19，**A 类**）、`vpn self hosted`（590）、`wireguard self hosted`（20）——本报告通过 Semrush 实测数据印证了这些词的 KD 判断，并新增了 `free wireguard vpn`（1,000 vol, KD=29）、`wireguard for tv`（880, KD=13）、`tailscale alternatives`（320, KD=19）等未收录的低竞争词，可补充进词表 Headscale/WireGuard 分组。
   - 本报告新发现的最高价值词：`tailscale vs wireguard`（1,000 vol, KD=24, CPC=$8.96）在 500 词表中未收录，建议补入 A 类。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_subdomains`、`resource_adwords`、`domain_organic_organic`、`phrase_these`、`phrase_related`、`phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
