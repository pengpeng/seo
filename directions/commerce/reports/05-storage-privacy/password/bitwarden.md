# Bitwarden SEO 竞品分析报告

> 域名：bitwarden.com | SEMrush us | 2026-07-07
> Bitwarden = 开源密码管理器（官方云 + 可自托管；行业里"开源密码管理"品类的心智锚）。Vaultwarden 是与其客户端兼容的轻量 Rust 自托管实现。

---

## 项目理解（前置）

Bitwarden 是市占率最高的**开源密码管理器**：官方提供托管云（个人/家庭/企业）+ 可自托管的服务器镜像，客户端全平台（浏览器扩展、桌面、移动、CLI）。它在密码管理赛道的独特定位是"开源 + 免费个人版 + 可自托管"，因此长期霸占 `open source password manager` / `self hosted password manager` 心智。对 Olares 最关键的一点：社区用 Rust 重写了一个 Bitwarden 兼容服务器 **Vaultwarden**（原 bitwarden_rs），资源占用极低、功能解锁更多，是家庭自托管场景里最常被安装的密码库——它蹭的正是 Bitwarden 的品牌与客户端生态。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 开源密码管理器（云 + 自托管双形态），"开源密码管理"品类领头羊 |
| 开源 / 许可证 | 开源，客户端/服务器 GPL-3.0（部分企业模块 Bitwarden License）；主体开源 |
| 主仓库 | github.com/bitwarden/clients、/server（★ 数万级）；平替 github.com/dani-garcia/vaultwarden（★ 4 万+） |
| 核心功能 | 密码库/自动填充、密码 & 通行短语生成器、Passkey、2FA/Authenticator、Send 加密分享、企业 SSO/目录同步 |
| 商业模式 / 定价 | 个人免费；Premium ~$10/年；Family ~$40/年；Teams/Enterprise 按席位月费 |
| 差异化 / 价值主张 | 开源可审计 + 免费个人版 + 官方支持自托管；企业级 SSO/合规 |
| 主要竞品（初判）| 1Password、LastPass、Dashlane、NordPass、Keeper、KeePassXC、Proton Pass、Passbolt |
| Olares Market | Vaultwarden 已上架（Bitwarden 兼容服务器，双形态自托管） |
| 来源 | bitwarden.com、github.com/bitwarden、github.com/dani-garcia/vaultwarden |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | bitwarden.com |
| SEMrush Rank | 5,747 |
| 自然关键词数 | 28,111 |
| 月自然流量（US）| 409,181 |
| 自然流量估值 | **$1,223,969/月** |
| 付费关键词数 | 40 |
| 月付费流量 | 232（几乎不投放）|
| 排名 1-3 位 | 1,576 词 |
| 排名 4-10 位 | 4,044 词 |
| 排名 11-20 位 | 3,379 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| bitwarden.com（主站）| 21,572 | 378,461 | 92.49% |
| vault.bitwarden.com（登录/Web 库）| 199 | 24,044 | 5.88% |
| community.bitwarden.com（论坛）| 6,217 | 6,321 | 1.54% |
| status.bitwarden.com | 31 | 350 | 0.09% |
| contributing / mobileapp / selfhost.* | 1-76 | 0-4 | 0% |

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| bitwarden | 1 | 135,000 | 88 | $5.23 | 108,000 | 品牌 | / |
| password management（借力）| 5 | 1,830,000 | 77 | $2.57 | 43,920 | 信息 | / |
| password generator（借力）| 5 | 823,000 | 76 | $0.08 | 36,212 | 信息 | /password-generator/ |
| password manager（借力）| 5 | 1,830,000 | 100 | $2.57 | 23,790 | 信息 | / |
| bitwarden login | 1 | 22,200 | 70 | $0.01 | 17,760 | 导航 | vault. |
| bitwarden password manager | 1 | 18,100 | 69 | $4.07 | 14,480 | 品牌 | / |
| bir warden（误拼）| 1 | 14,800 | 85 | $0.00 | 11,840 | 导航 | / |
| best free password generator（借力）| 1 | 74,000 | 66 | $1.36 | 9,768 | 信息 | /password-generator/ |
| best free password managers（借力）| 2 | 90,500 | 43 | $1.75 | 7,421 | 商业 | /products/personal/ |
| bit warden（分开）| 1 | 4,400 | 86 | $5.23 | 3,520 | 导航 | / |
| password gen（借力）| 5 | 49,500 | 81 | $0.08 | 2,178 | 信息 | /password-generator/ |
| password generator 12 characters | 6 | 60,500 | 77 | $0.08 | 2,117 | 信息 | /password-generator/ |
| bitwarden web vault | 1 | 2,400 | 60 | $16.87 | 1,920 | 导航 | vault. |
| bitwarden download | 1 | 2,400 | 92 | $7.53 | 1,920 | 信息 | /download/ |
| passphrase generator | 1 | 6,600 | 45 | $1.09 | 1,636 | 信息 | /passphrase-generator/ |
| username generator | 9 | 74,000 | 40 | $2.09 | 1,628 | 信息 | /username-generator/ |
| random password generator（借力）| 9 | 74,000 | 84 | $0.05 | 1,628 | 信息 | /password-generator/ |
| bitwarden firefox | 1 | 1,900 | 35 | $0.00 | 1,520 | 信息 | /download/…firefox…/ |
| bitwarden forgot password | 1 | 1,900 | 26 | $0.00 | 1,520 | 信息 | /help/forgot-master-password/ |
| password strength tester | 1 | 5,400 | 60 | $0.43 | 1,339 | 信息 | /password-strength/ |
| bitward（误拼）| 1 | 1,600 | 79 | $3.85 | 1,280 | 导航 | / |
| password generator 15 characters | 5 | 27,100 | 76 | $0.04 | 1,192 | 信息 | /password-generator/ |
| what is a password manager | 7 | 90,500 | 57 | $0.51 | 1,176 | 信息 | / |
| free password manager | 1 | 8,100 | 49 | $2.69 | 1,069 | 商业 | /products/personal/ |
| bitwarden pricing | 1 | 1,300 | 51 | $4.89 | 1,040 | 商业 | /pricing/ |
| bitwarden password gen | 1 | 1,300 | 33 | $4.55 | 1,040 | 信息 | /password-generator/ |
| password managers | 4 | 22,200 | 72 | $4.00 | 976 | 信息 | / |
| bitwarden authenticator | 1 | 1,000 | 50 | $0.80 | 800 | 信息 | /products/authenticator/ |
| free password creator | 1 | 1,600 | 70 | $0.14 | 396 | 信息 | /password-generator/ |
| online password manager | 1 | 1,600 | 78 | $4.64 | 396 | 商业 | / |
| password management software | 3 | 6,600 | 68 | $10.83 | 429 | 商业 | / |

> 洞察：Bitwarden 的非品牌流量几乎全靠 **免费工具页**（`/password-generator/`、`/passphrase-generator/`、`/username-generator/`、`/password-strength/`）借力 `password generator`（82.3 万）等超级大词——CPC 近 $0 但导流巨大。品牌词部分挂着大量误拼变体（bir warden / bit warden / bitward / bitwarde…）全部排名第 1。

### 付费词（Google Ads，按流量排序）

Bitwarden **几乎不打付费**（仅 40 词 / 月流量 232），但投放结构极具参考价值——**全部导向 `/go/` 程序化竞品对比 & 自托管落地页**：

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| 1password business pricing | 1 | 590 | $12.96 | /go/**bitwarden-1password-comparison**/ |
| password generator dashlane | 2 | 1,900 | $14.74 | /go/**bitwarden-dashlane-comparison**/ |
| 1password pricing | 5 | 3,600 | $3.27 | /go/bitwarden-1password-comparison/ |
| keeper security pricing | 1 | 170 | $3.10 | /go/**bitwarden-keeper-comparison**/ |
| password manager open source | 1 | 140 | $3.22 | /go/**open-source-password-manager**/ |
| open source password managers | 1 | 90 | $2.71 | /go/open-source-password-manager/ |
| selfhosted password manager | 2 | 90 | $4.20 | /go/**self-hosted-password-manager-on-premises**/ |
| keepassxc review | 1 | 40 | $3.55 | /go/self-hosted-password-manager-on-premises/ |
| phishing resistant mfa | 2 | 720 | $12.05 | /go/phising-resistant-mfa/ |

> 洞察：连行业龙头都在用付费 + 程序化对比页**主动买"open source / self-hosted / keepassxc"这些词**，说明这批词有真实商业价值且值得建对比落地页——这正是 Olares 应当复制的打法。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| bitwarden vs 1password | 1,600 | **29** | $1.15 | 对比 | ⭐ 最大对比词 |
| 1password vs bitwarden | 1,300 | **27** | $1.37 | 对比 | ⭐ |
| bitwarden vs lastpass | 590 | **25** | $2.38 | 对比 | ⭐ |
| proton pass vs bitwarden | 480 | **11** | $0.00 | 对比 | ⭐ KD=11 |
| bitwarden vs proton pass | 320 | **16** | $0.00 | 对比 | ⭐ |
| lastpass alternative | 320 | 26 | $4.52 | 商业 | ⭐ |
| bitwarden vs keepass | 260 | **26** | $7.78 | 对比 | ⭐ |
| keepass vs bitwarden | 260 | **22** | $1.25 | 对比 | ⭐ |
| bitwarden vs nordpass | 260 | **16** | $5.46 | 对比 | ⭐ |
| bitwarden vs dashlane | 210 | **26** | $3.40 | 对比 | ⭐ |
| 1password alternative | 170 | 22 | $6.36 | 商业 | ⭐ |
| 1password alternatives | 170 | 25 | $6.36 | 商业 | ⭐ |
| bitwarden alternatives | 110 | 21 | $4.30 | 商业 | ⭐ |
| bitwarden alternative | 90 | **19** | $2.90 | 商业 | ⭐ KD=19！ |
| keepassxc vs bitwarden | 90 | **3** | $3.16 | 对比 | ⭐ KD=3！金矿 |
| dashlane alternative | 50 | 21 | $10.88 | 商业 | ⭐ 高 CPC |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| password manager | 1,500,000 | 100 | $2.75 | 信息 | 品类超级大词，打不动 |
| best password manager | 22,200 | 57 | $3.14 | 信息 | |
| free password manager | 8,100 | 59 | $2.40 | 信息 | |
| password management software | 6,600 | 68 | $10.48 | 商业 | 高 CPC |
| best free password manager | 2,900 | **25** | $1.82 | 信息 | ⭐ 大词低 KD |
| password vault | 2,900 | 88 | $6.23 | 信息 | |
| business password manager | 1,900 | 56 | $53.82 | 商业 | CPC=$54！ |
| online password manager | 1,600 | 78 | $4.64 | 商业 | |
| open source password manager | 1,300 | 39 | $2.87 | 信息 | Olares 前哨 |
| secure password manager | 1,000 | 70 | $4.52 | 信息 | |
| best password manager reddit | 880 | 37 | $4.62 | 信息 | UGC 意图 |
| enterprise password manager | 880 | 46 | $27.71 | 商业 | CPC=$28！ |
| self hosted password manager | 720 | 39 | $5.25 | 信息 | Olares 核心 |
| family password manager | 720 | 54 | $3.77 | 信息 | |
| password manager reddit | 480 | 33 | $5.29 | 信息 | |

### 产品 / 功能词（bitwarden 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| bitwarden chrome extension | 6,600 | 59 | $9.64 | 信息 | |
| bitwarden extension | 4,400 | 56 | $2.83 | 信息 | |
| bitwarden download | 2,400 | 92 | $7.02 | 信息 | |
| bitwarden pricing | 1,300 | 51 | $4.89 | 商业 | 定价意图 |
| bitwarden authenticator | 1,000 | 50 | $0.80 | 信息 | |
| bitwarden review | 880 | **30** | $1.42 | 评测 | ⭐ |
| is bitwarden safe | 880 | 50 | $2.28 | 信息 | 信任意图 |
| bitwarden free | 590 | 72 | $1.79 | 商业 | |
| bitwarden cli | 480 | 34 | $0.00 | 信息 | |
| bitwarden passkey | 480 | 58 | $3.11 | 信息 | |
| bitwarden send | 480 | 43 | $6.39 | 信息 | |
| bitwarden reddit | 480 | 34 | $0.00 | 信息 | |
| bitwarden enterprise | 260 | 43 | $15.49 | 商业 | CPC=$15 |
| bitwarden family | 260 | 33 | $2.75 | 信息 | |
| bitwarden api | 260 | **24** | $0.00 | 信息 | ⭐ |
| bitwarden business | 110 | 50 | $10.14 | 商业 | |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| vaultwarden | 6,600 | 48 | $4.87 | 信息 | **赛道最大自托管工具词** |
| open source password manager | 1,300 | 39 | $2.87 | 信息 | |
| passbolt | 1,300 | 52 | $5.03 | 品牌 | 另一自托管竞品 |
| local self hosted password manager | 880 | **27** | $0.00 | 信息 | ⭐ |
| bitwarden self hosted | 720 | 50 | $8.88 | 信息 | CPC=$8.88 |
| self hosted password manager | 720 | 39 | $5.25 | 信息 | |
| offline password manager | 320 | **22** | $1.16 | 信息 | ⭐ |
| bitwarden self host | 320 | 45 | $4.89 | 信息 | |
| vaultwarden vs bitwarden | 320 | **14** | $0.00 | 对比 | ⭐ |
| vaultwarden docker | 320 | 32 | $0.00 | 教程 | |
| self host bitwarden | 260 | 42 | $8.41 | 信息 | |
| vaultwarden docker compose | 260 | **28** | $0.00 | 教程 | ⭐ |
| bitwarden vs vaultwarden | 210 | **12** | $4.21 | 对比 | ⭐ |
| bitwarden docker | 210 | 62 | $0.00 | 教程 | |
| best open source password manager | 170 | **26** | $2.79 | 信息 | ⭐ |
| password manager self hosted | 140 | **29** | $4.20 | 信息 | ⭐ |
| best self hosted password manager | 140 | **25** | $3.43 | 信息 | ⭐ |
| vaultwarden backup | 90 | 20 | $8.80 | 教程 | ⭐ |
| free open source password manager | 70 | 73 | $1.90 | 信息 | |
| vaultwarden setup / install / admin / unraid / synology / proxmox | 20 | 0 | — | 教程 | GEO 长尾簇 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Bitwarden 是"云 + 自托管"的开源密码管理器，但官方自托管部署重、企业模块闭源、云端仍需信任第三方；Olares Market 上的 Vaultwarden 是 Bitwarden 客户端兼容、资源极轻、一键部署、数据永不出户、零月费的自托管实现——直接吃"vaultwarden / self-hosted / open-source password manager / bitwarden vs vaultwarden"四层流量。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| vaultwarden | 6,600 | 48 | $4.87 | ⭐⭐⭐ Vaultwarden on Olares Market：一键装 Bitwarden 兼容密码库，完全本地、双形态 |
| open source password manager | 1,300 | 39 | $2.87 | ⭐⭐⭐ Vaultwarden = 开源密码库，Olares 一键自托管，无需拼 Docker |
| local self hosted password manager | 880 | **27** | $0.00 | ⭐⭐⭐ KD27："本地自托管密码库"精准命中 Olares 家用场景 |
| bitwarden self hosted | 720 | 50 | $8.88 | ⭐⭐ "Bitwarden 自托管"教程流量导向 Olares 上更轻的 Vaultwarden |
| self hosted password manager | 720 | 39 | $5.25 | ⭐⭐⭐ 品类核心词，Olares 上 Vaultwarden 零月费、数据不离家 |
| proton pass vs bitwarden | 480 | **11** | $0.00 | ⭐⭐ 三方对比引入"自托管第三选项"（Olares/Vaultwarden）|
| bitwarden vs 1password | 1,600 | 29 | $1.15 | ⭐⭐ 对比页收尾推"要完全自托管？Vaultwarden on Olares" |
| offline password manager | 320 | **22** | $1.16 | ⭐⭐ "离线/本地密码库"＝Olares 自托管卖点 |
| vaultwarden vs bitwarden | 320 | **14** | $0.00 | ⭐⭐⭐ 直接解释两者关系并给 Olares 部署路径 |
| vaultwarden docker compose | 260 | **28** | $0.00 | ⭐⭐ 自托管教程词，Olares 免 compose 一键装 |
| bitwarden vs vaultwarden | 210 | **12** | $4.21 | ⭐⭐⭐ KD12 高意图对比词 |
| best open source password manager | 170 | **26** | $2.79 | ⭐⭐ 清单文，把 Vaultwarden(on Olares) 列首选 |
| best self hosted password manager | 140 | **25** | $3.43 | ⭐⭐⭐ 自托管清单，Olares 一键部署优势 |
| password manager self hosted | 140 | **29** | $4.20 | ⭐⭐ 语序变体，同簇 |
| keepassxc vs bitwarden | 90 | **3** | $3.16 | ⭐⭐ KD=3 三方对比，切入"要同步又要自托管选 Vaultwarden" |
| bitwarden alternative | 90 | **19** | $2.90 | ⭐⭐ KD19 替代词，Vaultwarden on Olares = 本地替代 |
| enterprise password manager | 880 | 46 | $27.71 | ⭐ CPC=$28 企业自托管密码库切入点 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| vaultwarden | 6,600 | 48 | $4.87 | 信息 | 主词候选 | 赛道最大自托管词，Vaultwarden on Olares 应用页/教程直接承接 |
| open source password manager | 1,300 | 39 | $2.87 | 信息 | 主词候选 | 品类心智词，"开源密码库＝Vaultwarden，Olares 一键自托管" |
| self hosted password manager | 720 | 39 | $5.25 | 信息 | 主词候选 | 自托管核心词，$5.25 CPC，Olares 零月费叙事 |
| local self hosted password manager | 880 | 27 | $0.00 | 信息 | 主词候选 | KD27 + 880 量，最契合 Olares 家用本地场景 |
| bitwarden vs 1password | 1,600 | 29 | $1.15 | 对比 | 主词候选 | 最大对比词，结尾引入自托管第三选项 |
| best free password manager | 2,900 | 25 | $1.82 | 信息 | 主词候选 | 大词低 KD，清单文把 Vaultwarden(on Olares) 列入 |
| bitwarden self hosted | 720 | 50 | $8.88 | 信息 | 次级 | 高 CPC 教程词，导向更轻的 Vaultwarden |
| bitwarden vs vaultwarden | 210 | 12 | $4.21 | 对比 | 主词候选 | KD12 高意图，直接解释 + Olares 部署 |
| vaultwarden vs bitwarden | 320 | 14 | $0.00 | 对比 | 主词候选 | 反向同题，合并成一篇权威对比 |
| best self hosted password manager | 140 | 25 | $3.43 | 信息 | 次级 | 自托管清单文核心并入词 |
| best open source password manager | 170 | 26 | $2.79 | 信息 | 次级 | 开源清单文并入词 |
| offline password manager | 320 | 22 | $1.16 | 信息 | 次级 | 低 KD，本地/离线卖点契合 |
| proton pass vs bitwarden | 480 | 11 | $0.00 | 对比 | 次级 | KD11，多方对比里带出自托管 |
| keepassxc vs bitwarden | 90 | 3 | $3.16 | 对比 | GEO | KD=3 金矿，抢引用位讲"要同步的自托管选 Vaultwarden" |
| bitwarden alternative | 90 | 19 | $2.90 | 商业 | 次级 | KD19 替代词，本地替代叙事 |
| enterprise password manager | 880 | 46 | $27.71 | 商业 | 次级 | CPC=$28 企业自托管切入，量力而行 |
| vaultwarden docker compose | 260 | 28 | $0.00 | 教程 | GEO | 教程长尾，Olares 免 compose 优势对照 |
| vaultwarden setup/install/synology/unraid | 20 | 0 | — | 教程 | GEO | 近零量教程簇，"在 Olares 上更简单"占位 |

---

## 核心洞见

1. **品牌护城河：正面刚 Bitwarden 品牌词无胜算，但它自己"漏"出了 Vaultwarden 这个替代品词。** `bitwarden`（13.5 万，KD88）+ 海量误拼变体全排名第 1，属纯品牌心智，抢不动也不必抢。真正的机会是社区平替词 **`vaultwarden`（6,600，KD48）**——它蹭 Bitwarden 客户端生态却是独立自托管品牌，Olares Market 已上架，可直接承接。

2. **可复制的打法：程序化「/go/ 对比 + 自托管」落地页矩阵。** Bitwarden 连付费预算都优先买 `1password/dashlane/keeper pricing`、`open source password manager`、`selfhosted password manager`、`keepassxc review` 并导向 `/go/bitwarden-1password-comparison/`、`/go/open-source-password-manager/`、`/go/self-hosted-password-manager-on-premises/` 等模板页——**龙头亲自验证了这批对比/自托管词值钱**。Olares 应对每个对比对（vs 1password / vs proton pass / vs keepassxc）和"self-hosted / open-source password manager"各建一页，收尾统一推"要完全自托管？Vaultwarden on Olares"。此外，Bitwarden 99% 非品牌流量靠**免费工具页**（密码生成器等）借力大词——Olares 也可放在线密码生成/强度检测工具引流。

3. **对 Olares 最关键的 3 个词：`vaultwarden`（6,600, KD48）、`self hosted / local self hosted password manager`（720+880, KD39/27）、`bitwarden vs vaultwarden`（210+320, KD12/14）。** 前者是最大精准入口，中者是品类需求词，后者是高转化对比词——三者都直指 Olares 上的 Vaultwarden，且 KD 均可攻。

4. **最大攻击面：官方自托管重 + 云端仍需信任 + 企业模块闭源/收费。** `bitwarden self hosted`（720, CPC $8.88）、`bitwarden self host`（320）、`bitwarden docker`（210）、`enterprise/business password manager`（CPC $28/$54）说明用户想自托管却嫌官方部署繁琐、且企业价高。Olares 叙事应直击："Bitwarden 兼容、Vaultwarden 极轻、一键装在自己的 Olares 上——零月费、数据永不出户、免拼 Docker/反代"。

5. **隐藏低 KD 金矿：`keepassxc vs bitwarden`（KD3）、`bitwarden vs vaultwarden`（KD12）、`proton pass vs bitwarden`（KD11）、`bitwarden vs nordpass/proton pass`（KD16）、`bitwarden alternative`（KD19）、`offline password manager`（KD22）、`local self hosted password manager`（KD27）。** 这批对比/自托管词几乎无专门竞争内容，配合 Vaultwarden 上架可低成本抢占第一屏。

6. **GEO 前瞻词：** `vaultwarden setup / install / synology / unraid / proxmox`、`host your own password manager`、`private password manager`、`bitwarden self hosted docker` 目前近零量但语义与 Olares 完美契合——发布"在 Olares 上部署 Vaultwarden（比 Docker/群晖更简单）"权威页，抢 AI Overview / Perplexity 的"如何自托管密码库"引用位。

7. **与既有 olares-500-keywords 的关联：** 500 词表已收 `vaultwarden`(B)、`self hosted password manager`(A)、`bitwarden alternative`(A)、`password manager self hosted`(A)、`open source password manager`(B)、`offline password manager`(A)、`keepassxc vs bitwarden`(A+, KD3)。本报告补充并印证：`local self hosted password manager`(880/KD27)、`bitwarden vs vaultwarden`(KD12)、`best self hosted / open source password manager`、`proton pass vs bitwarden`(KD11) 应补入词表自托管密码库簇；注意 `self hosted password manager` 最新 KD 已从旧记的 29 升到 39，选词时以此为准。

---

*数据来源：SEMrush us 数据库（domain_rank / domain_organic_subdomains / resource_organic / resource_adwords / domain_organic_organic / phrase_these / phrase_related）| 2026-07-07*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
