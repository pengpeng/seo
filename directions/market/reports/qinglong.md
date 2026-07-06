# Qinglong SEO 竞品分析报告

> 场景词分析（无主力英文官网）| SEMrush US | 2026-07-06
> Qinglong（青龙面板）：支持多语言脚本的开源定时任务管理平台，中文开发者社区为主，英文 SEO 近零，品类词机会集中在 "job scheduler open source" 与 "X alternative" 低 KD 地带。

---

## 项目理解（前置）

Qinglong Panel（青龙面板）是由 whyour 开发的开源定时任务管理平台，支持 Python3、JavaScript、Shell、TypeScript 四种脚本语言，提供 Web 可视化界面管理 cron 任务、环境变量、依赖包与日志。原本以 JD.com 签到/积分自动化脚本闻名，后演化为通用脚本调度工具。2026 年 2 月曾爆出两个严重 RCE 漏洞（CVE-2026-3965、CVE-2026-4047），均已在 v2.20.2 修复。项目受众几乎 100% 为中文用户；官网 qinglong.online 文档以中文为主，英文翻译有限。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 带 Web UI 的多语言脚本定时任务调度平台（自托管 cron 管理器） |
| 开源 / 许可证 | 开源，Apache-2.0 |
| 主仓库 | [github.com/whyour/qinglong](https://github.com/whyour/qinglong)（★ ~19,700） |
| 核心功能 | Cron 任务 Web UI、脚本订阅（从 GitHub 自动拉取）、环境变量管理、依赖在线安装、日志监控、秒级精度、移动端访问 |
| 商业模式 / 定价 | 完全免费开源；Docker 镜像（alpine/debian）或 npm 包部署 |
| 差异化 / 价值主张 | 多语言脚本兼容、GitHub 脚本订阅自动同步、无需手动进容器管理依赖；轻量（Alpine 镜像） |
| 主要竞品（初判）| gocron、Supercronic、Ofelia（同类 cron 工具）；n8n、Windmill、Node-RED（更完整的 workflow automation 竞品） |
| Olares Market | 已上架（⬜ 首次研究） |
| 来源 | [github.com/whyour/qinglong](https://github.com/whyour/qinglong)、[qinglong.online](https://qinglong.online)、[bleepingcomputer.com CVE 报道](https://www.bleepingcomputer.com/news/security/hackers-exploit-rce-flaws-in-qinglong-task-scheduler-for-cryptomining/) |

---

## 流量基线（Phase 1）

> Qinglong 有官方域名 qinglong.online，但英文 SEO 几乎为零——全量 18 个有排名的关键词均为中文查询，无有效英文流量。以下数据仅作中英文对比背景参考，不展开完整域名分析。

| 指标 | 数据 |
|------|------|
| 域名 | qinglong.online |
| SEMrush Rank（US） | 1,694,298 |
| 自然关键词数（US） | 18（全部中文） |
| 月自然流量（US） | 474（全部来自中文查询） |
| 自然流量估值 | $0 |
| 付费词 | 0 |
| 英文关键词 | 0 |

### qinglong.online 所有排名关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | 备注 |
|--------|------|------|----|------|
| 青龙面板 | 2 | 2,900 | 13 | 品牌核心词（中文） |
| 青龙脚本 | 2 | 480 | 18 | 中文长尾 |
| 青龙 面板 | 2 | 90 | 6 | 变体 |
| whyour/qinglong | 5 | 170 | 9 | GitHub 仓库直搜 |
| 1panel 安装 | 9 | 170 | 10 | 竞品相关 |
| 1panel卸载 | 28 | 210 | 4 | 竞品相关 |
| 1panel install | 26 | 110 | 17 | 竞品英文词（偶发排名） |
| qwenlong | 51/61 | 140 | 39 | 品牌误拼（与 LLM 混淆） |

**结论**：英文搜索对 qinglong.online 几乎没有流量贡献，"qinglong" 英文语境下被中国神话、游戏角色（Overwatch/LOL）、历史剧高度污染，品牌词完全无法在英文市场建立认知。

### 有机竞品（US 数据库中与 qinglong.online 共享关键词的域名）

全部为中文博客/工具站（1panel.cn、fit2cloud.com、jumpserver.org 等），无英文工具站出现。进一步证实 Qinglong 英文 SEO 版图为空白。

---

## 关键词扩展（Phase 2）

> 降级模式：跳过域名级扩展，围绕"cron job manager / task scheduler / self-hosted automation"三个核心场景词做品类级扩展。⭐ = KD<30 且有搜索意图的机会词。注：`phrase_all`/`phrase_these`/`phrase_fullsearch` 报告在本次调用中持续返回 500 错误，无法获取批量月量数据；月量一栏仅对通过 `phrase_questions` 获取到数据的词标注，其余为"—"（有 KD 代表关键词存在，量级未知）。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| n8n alternative | — | 18 | $0 | 商业 | ⭐ Olares 同时上架 n8n+Qinglong |
| n8n alternative self-hosted | — | 16 | $0 | 商业 | ⭐ 精准自托管意图 |
| airflow alternative | — | 10 | $0 | 商业 | ⭐⭐ 超低 KD |
| node-red alternative | — | 12 | $0 | 商业 | ⭐ homelab 受众重合 |
| celery alternative | — | 16 | $0 | 商业 | ⭐ Python 开发者 |
| activepieces vs n8n | — | 4 | $0 | 商业 | ⭐⭐ 近乎零防守 |
| n8n vs make | — | 31 | $0 | 商业 | 中竞争 |
| airflow vs prefect | — | 26 | $0 | 信息 | 中竞争 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| cron job | — | 68 | $0 | 信息 | 高竞争，不可正面攻 |
| cron job scheduler | — | 55 | $0 | 信息 | 中高竞争 |
| job scheduler | — | 22 | $0 | 信息/商业 | ⭐ 可排名 |
| job scheduler open source | — | 24 | $0 | 商业 | ⭐ 精准意图 |
| open source job scheduler | — | 23 | $0 | 商业 | ⭐ 与上同簇 |
| open source workflow automation | — | 20 | $0 | 商业 | ⭐ 大品类 |
| workflow automation open source | — | 20 | $0 | 商业 | ⭐ 同上变体 |
| task automation | — | 36 | $0 | 信息 | 中竞争 |
| script automation | — | 23 | $0 | 信息 | ⭐ |
| kubernetes cron job | — | 31 | $0 | 信息 | 技术受众 |
| cron job monitoring | — | 33 | $0 | 商业 | 中竞争 |
| python task scheduler | — | 31 | $0 | 信息 | 开发者长尾 |

### 产品 / 功能词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| qinglong | — | 37 | $0 | 导航 | 英文意图污染严重（游戏/历史）|
| gocron | — | 33 | $0 | 导航 | Go 语言同类竞品 |
| supercronic | — | 20 | $0 | 导航 | ⭐ 同类轻量 cron 工具 |
| what is a cron job | 74,000 | 58 | $0 | 信息 | 超高量，竞争也高 |
| what is a cron job in linux | 590 | 41 | $0 | 信息 | 中竞争长尾 |
| what is cron job | 480 | 42 | $0 | 信息 | 同上簇 |
| what are cron jobs | 390 | 49 | $0 | 信息 | 同上簇 |
| how to edit a cron job | 170 | 0 | $0 | 信息 | ⭐⭐ KD=0！教程词 |
| how to edit cron jobs | 110 | 24 | $0 | 信息 | ⭐ 低 KD 教程词 |
| how to check cron jobs | 90 | 21 | $0 | 信息 | ⭐ |
| how to create a cron job | 90 | 43 | $0 | 信息 | 中竞争 |
| how to check if cron job is running | 50 | 17 | $0 | 信息 | ⭐ |
| how to find cron jobs | 70 | 23 | $0 | 信息 | ⭐ |
| what is job scheduling software | 50 | 6 | $0 | 信息 | ⭐⭐ KD=6！ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| n8n alternative self-hosted | — | 16 | $0 | 商业 | ⭐ 精准自托管意图 |
| self-hosted workflow automation | — | 0 | $0 | 商业 | 量级未知，GEO 前哨 |
| homelab automation | — | 0 | $0 | 信息 | 量级未知，社区词 |
| self-hosted cron | — | 0 | $0 | 信息 | 量级未知 |
| open source task runner | — | 0 | $0 | 信息 | 量级未知 |
| cron job web interface | — | 0 | $0 | 信息 | ⭐ 精准描述 Qinglong |
| qinglong docker | — | 0 | $0 | 导航 | 英文受众极少 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Qinglong 英文品牌词无效，必须借道品类词（self-hosted cron/job scheduler）和 X alternative 词（借竞品流量）切入；Olares Market 一键部署是最强差异化叙事。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|--------|
| job scheduler open source | — | 24 | $0 | Olares Market 一键安装 Qinglong，30 秒启动定时任务管理 | ⭐⭐⭐ |
| n8n alternative self-hosted | — | 16 | $0 | Olares 同时上架 Qinglong + n8n，覆盖轻量 cron 与复杂 workflow 全场景 | ⭐⭐⭐ |
| airflow alternative | — | 10 | $0 | Qinglong 在 Olares 上提供比 Airflow 轻 10 倍的 cron 调度，适合个人/homelab | ⭐⭐⭐ |
| open source workflow automation | — | 20 | $0 | Olares = 运行全栈开源自动化的操作系统，Qinglong 是调度层之一 | ⭐⭐ |
| node-red alternative | — | 12 | $0 | Qinglong 更偏 cron/脚本，Node-RED 偏 IoT 流；Olares 上可同时运行 | ⭐⭐ |
| celery alternative | — | 16 | $0 | 对 Python 开发者：Qinglong 无需配置 broker，Web UI 管理，适合个人项目 | ⭐⭐ |
| how to edit a cron job | 170 | 0 | $0 | 教程末尾引入 Qinglong Web UI 作为"cron 管理更好的方式"，Olares 一键安装 | ⭐⭐ |
| how to check if cron job is running | 50 | 17 | $0 | Qinglong 提供日志监控面板；Olares 上部署免运维 | ⭐⭐ |
| what is job scheduling software | 50 | 6 | $0 | 超低 KD 信息词，引用 Qinglong + Olares 组合作为最佳自托管选项 | ⭐⭐ |
| self-hosted cron job manager with web ui | — | ~0 | $0 | Qinglong 完美匹配此描述，Olares 安装 = 零配置 | ⭐⭐⭐（GEO 抢占） |
| 青龙面板 english tutorial | — | ~0 | $0 | 为中文用户做英文引导，长尾；Olares 英文文档 | ⭐⭐（中文受众）|

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| job scheduler open source | — | 24 | $0 | 商业 | 主词候选 | KD 低、意图精准；Olares Market = 最快的"一键 open source job scheduler" |
| airflow alternative | — | 10 | $0 | 商业 | 主词候选 | KD=10 全品类最低；Qinglong 是轻量 Airflow 替代，Olares 无需运维 |
| n8n alternative self-hosted | — | 16 | $0 | 商业 | 主词候选 | KD=16，自托管受众精准；Olares 同时提供 Qinglong+n8n 覆盖全场景 |
| open source workflow automation | — | 20 | $0 | 商业 | 次级 | 大品类词，支撑主文章；Olares = 自托管自动化全栈平台 |
| celery alternative | — | 16 | $0 | 商业 | 次级 | Python 受众，Qinglong 无需 Redis broker；收入对比文 |
| node-red alternative | — | 12 | $0 | 商业 | 次级 | homelab 受众重合；Olares 同时支持两者 |
| what is job scheduling software | 50 | 6 | $0 | 信息 | 次级 | KD=6 接近零阻力；信息词入口，结尾推 Qinglong on Olares |
| how to edit a cron job | 170 | 0 | $0 | 信息 | 次级 | KD=0 教程黄金词；教程末尾 CTA 推 Qinglong Web UI |
| how to check cron jobs | 90 | 21 | $0 | 信息 | 次级 | 低 KD 教程词；Qinglong log panel 作为解决方案 |
| how to check if cron job is running | 50 | 17 | $0 | 信息 | 次级 | 监控焦虑词；Qinglong 实时日志面板是答案 |
| supercronic | — | 20 | $0 | 导航 | 次级 | 同类轻量竞品；对比文"Supercronic vs Qinglong"收长尾 |
| qinglong panel self-hosted install | — | ~0 | $0 | 导航 | GEO | 教程词，AI Overview/Perplexity 引用机会 |
| self-hosted cron job manager with web ui | — | ~0 | $0 | 信息 | GEO | 精准描述 Qinglong，抢 AI 答案位 |
| best open source cron job manager | — | ~0 | $0 | 商业 | GEO | AI 综述类问题，Olares Market 角度可抢引用 |

---

## 核心洞见

1. **品牌护城河**：Qinglong 英文品牌词"qinglong"在美国搜索中被中国神话与游戏（Overwatch、LOL 角色、历史剧）严重稀释，KD 37 但实际英文品牌搜索量极低。**不可正面打品牌词**，只能走品类词和 alternative 词路线。官网 qinglong.online 在 US 有 474 月流量，全部来自中文关键词——英文 SEO 从零开始。

2. **可复制的打法**：Qinglong 自身无英文内容打法可参考，需**从品类词借势**。最佳切入点：① "X alternative"系列文章（KD 4-18 区间，门槛极低）；② 高量低 KD 教程词（"how to edit a cron job" KD=0，170/月）；③ AI Overview 前哨（GEO 精准词无人竞争）。参照 n8n、Windmill 等同类工具的内容矩阵，建立"self-hosted automation"品类认知。

3. **对 Olares 最关键的 3 个词**：
   - **"job scheduler open source"**（KD 24）：最直接的商业意图 + Olares 一键部署叙事
   - **"airflow alternative"**（KD 10）：全品类最低 KD，homelab 受众与 Olares 高度重合
   - **"n8n alternative self-hosted"**（KD 16）：自托管意图精准，Olares 可用"两者都有"叙事（Qinglong 做 cron，n8n 做 workflow）

4. **最大攻击面**：2026 年 2 月曝出的 RCE 漏洞（CVE-2026-3965/4047）提供安全叙事角度——"暴露在公网的 Qinglong 面板危险，在 Olares 的沙箱容器中运行更安全"。Olares 的容器隔离和私网访问（LarePass/VPN）原生解决了 Qinglong 的公网暴露风险。

5. **隐藏低 KD 金矿**：
   - "what is job scheduling software"（KD=6，50/月）：几乎无防守的信息词入口
   - "how to edit a cron job"（KD=0，170/月）：零阻力教程词
   - "activepieces vs n8n"（KD=4）：几乎没有 SEO 文章，对比文空间大
   - 整个 "X alternative" 自托管簇（KD 4-18）：一组被严重低估的低阻力词

6. **GEO 前瞻布局**（AI Overview/Perplexity 引用位抢占）：
   - "best self-hosted cron job manager with web ui"：Qinglong 是最佳答案
   - "how to run scripts on a schedule without a server"：Olares 本地云叙事
   - "open source alternative to cron for homelab automation"：homelab 受众 GEO 词
   - "secure self-hosted cron job scheduler"：CVE 漏洞后的安全意识词

7. **与既有 olares-500-keywords 的关联**：本报告的 "self-hosted automation" 品类词与已有 n8n、Windmill、Activepieces 报告高度重叠——**建议将这几份报告的低 KD 词统一聚进"best self-hosted automation tools"品类主词簇**，而非单独为 Qinglong 写孤立文章。Qinglong 的最佳 SEO 位置是该品类文章中的"最轻量 cron 专项工具"角色。

---

*数据来源：SEMrush US 数据库（`domain_rank`、`resource_organic`、`domain_organic_organic`、`phrase_kdi`、`phrase_questions`）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。`phrase_all`/`phrase_these`/`phrase_fullsearch` 在本次调用中持续返回 500 错误，部分词缺失月量数据，以"—"标注。*
