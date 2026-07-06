# Ollama SEO 竞品分析报告

> 域名：ollama.com | SEMrush US | 数据快照 2026-07-04
> 本地大模型运行引擎——一条命令在自己机器上跑 Llama/Qwen/DeepSeek 等开源模型，是"本地 LLM"品类的事实入口。

---

## 项目理解（前置）

Ollama 是把开源大模型"一条命令跑起来"的本地推理运行时：`curl … | sh` 装好后 `ollama run <model>` 即可，底层封装 llama.cpp，提供模型库（ollama.com/library）、CLI 与 REST API，并能直接对接 Claude Code / OpenClaw / Codex / Copilot 等 agent。它是"本地/私有 LLM"心智里最强的品牌入口，卖点是隐私（数据不出机器、可完全离线）与零门槛。近一年它推出了付费云 **Ollama Cloud**（Pro $20/mo、Max $100/mo），把"本地起步、云端扩展"作为商业化路径——这也带来了用户对隐私的新疑虑。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 本地运行开源大模型的推理引擎（CLI + 模型库 + REST API） |
| 开源 / 许可证 | 是，MIT License |
| 主仓库 | [github.com/ollama/ollama](https://github.com/ollama/ollama)（Go，★ ~175k，460+ 贡献者，229 releases） |
| 核心功能 | 一命令安装运行模型；模型库；REST API/CLI；对接 Claude Code/OpenClaw/Codex 等 agent；GGUF 导入 |
| 商业模式 / 定价 | 本体免费开源；付费云 Ollama Cloud（Pro $20/mo、Max $100/mo） |
| 差异化 / 价值主张 | 最省事的本地模型入口；隐私（数据不外传、可离线）；模型库生态最大 |
| 主要竞品（初判）| LM Studio、Jan、GPT4All、LocalAI、llama.cpp、vLLM |
| Olares Market | 已上架（共享应用，装一次供其他 app 注入消费） |
| 来源 | ollama.com、github.com/ollama/ollama、docs.ollama.com |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | ollama.com |
| SEMrush Rank | 9,796 |
| 自然关键词数 | 30,954 |
| 月自然流量（US）| 234,232 |
| 自然流量估值 | $887,416/月 |
| 付费关键词数 | 0（无 Google Ads 投放）|
| 排名 1-3 位 | 2,535 词 |
| 排名 4-10 位 | 2,953 词 |
| 排名 11-20 位 | 3,083 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| ollama.com | 23,400 | 213,218 | 91.0% |
| docs.ollama.com | 7,404 | 21,002 | 9.0% |
| www.ollama.com | 145 | 12 | 0.01% |
| registry.ollama.com | 5 | 0 | 0% |

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| ollama | 1 | 90,500 | 71 | $3.84 | 72,400 | 导航 | ollama.com |
| ollama models | 1 | 18,100 | 59 | $5.45 | 14,480 | 导航 | /library |
| olama | 1 | 3,600 | 58 | $2.94 | 2,880 | 导航（误拼）| ollama.com |
| ollma | 1 | 2,900 | 56 | $3.84 | 2,320 | 导航（误拼）| ollama.com |
| ollama model | 1 | 2,900 | 52 | $5.45 | 2,320 | 导航 | /library |
| ollama cloud | 1 | 2,400 | 56 | $6.73 | 1,920 | 信息/商业 | docs/cloud |
| ollama api | 1 | 2,400 | 58 | $6.18 | 1,920 | 信息/商业 | docs/api |
| ollama deepseek abliterated | 1 | 1,900 | 34 | $0 | 1,520 | 导航 | /huihui_ai/deepseek-r1-abliterated |
| ollama install | 1 | 1,900 | 78 | $11.92 | 1,520 | 导航 | /download/windows |
| ollam cloud | 1 | 1,900 | 49 | $0 | 1,520 | 商业 | /pricing |
| install ollama | 1 | 1,600 | 57 | $7.37 | 1,280 | 信息/导航 | /download |
| ollama library | 1 | 1,600 | 68 | $0 | 1,280 | 导航 | /library |
| llama ai | 2 | 8,100 | 47 | $4.24 | 1,069 | 信息 | /library/llama3.1 |
| download ollama | 1 | 1,300 | 85 | $9.19 | 1,040 | 导航 | /download/windows |
| ollama gemma 4 | 1 | 1,300 | 30 | $9.95 | 1,040 | 信息 | /library/gemma4 |
| ollama gpt-oss | 1 | 1,300 | 48 | $4.20 | 1,040 | 信息 | /library/gpt-oss |
| gemma 4 | 3 | 12,100 | 64 | $2.03 | 786 | 信息 | /library/gemma4 |
| nomic-embed-text | 1 | 2,900 | 38 | $4.37 | 719 | 信息 | /library/nomic-embed-text |
| llama3.2 | 1 | 2,900 | 85 | $3.26 | 719 | 信息 | /library/llama3.2 |
| ollama claud code | 1 | 880 | 32 | $0 | 704 | 信息 | docs/integrations/claude-code |
| qwen 3 uncensored | 2 | 4,400 | 23 | $0 | 580 | 信息 | /huihui_ai/qwen3-abliterated |
| ollama model list | 1 | 720 | 28 | $9.58 | 576 | 信息 | /library |
| ollama claude code | 1 | 720 | 34 | $7.77 | 576 | 信息 | docs/integrations/claude-code |
| glm 4.7 | 3 | 5,400 | 44 | $2.23 | 442 | 信息 | /library/glm-4.7 |
| gemma 4 ollama | 1 | 480 | 0 | $8.59 | 384 | 信息 | /library/gemma4 |
| ollama cli | 1 | 480 | 56 | $5.81 | 384 | 信息 | docs/cli |
| ollama kimi k2 5 | 1 | 480 | 22 | $3.25 | 384 | 信息 | /library/kimi-k2.5 |
| qwen3 coder | 1 | 2,900 | 56 | $5.80 | 382 | 信息 | /library/qwen3-coder |

### 付费词

无。ollama.com 未投放 Google Ads（付费关键词数 = 0），全部流量来自自然搜索。

---

## 关键词扩展（Phase 2）

**自然竞品**（`domain_organic_organic`）：直接对标是 **LM Studio（lmstudio.ai，相关度 0.19）**；其余为模型/推理生态平台 huggingface.co、openrouter.ai、together.ai、qwen.ai、unsloth.ai、artificialanalysis.ai。品类内平替（手工补）：GPT4All、Jan、LocalAI、llama.cpp、vLLM。

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open webui | 8,100 | 34 | $6.46 | 信息 | Ollama 最常配的 UI，Olares Market 已上架 |
| gpt4all | 5,400 | 37 | $4.33 | 信息 | 平替品牌 |
| jan ai | 2,400 | 34 | $3.20 | 导航 | 平替品牌 |
| localai | 1,300 | 65 | $3.61 | 导航 | 平替品牌 |
| ollama vs lm studio | 1,000 | 24 ⭐ | $7.05 | 信息 | 高量低 KD 对比词 |
| ollama vs llama.cpp | 1,000 | 20 ⭐ | $13.70 | 信息 | 高量低 KD、CPC 极高 |
| ollama vs vllm | 260 | 30 | $6.16 | 信息 | 对比词 |
| lm studio alternative | 260 | 15 ⭐ | $3.65 | 信息 | 极低 KD |
| ollama alternative | 210 | 16 ⭐ | $4.30 | 信息 | 极低 KD |
| ollama vs chatgpt | 90 | 11 ⭐ | $0 | 信息 | 极低 KD，叙事最佳 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| local llm | 2,900 | 39 | $5.37 | 信息 | 品类大词 |
| private llm | 720 | 27 ⭐ | $3.76 | 信息 | Olares 核心定位词 |
| run llm locally | 590 | 47 | $3.50 | 信息 | 品类 |
| private gpt | 480 | 18 ⭐ | $4.28 | 信息 | 低 KD 高意图 |
| self hosted ai | 390 | 36 | $3.90 | 信息 | 品类 |
| local chatgpt | 390 | 17 ⭐ | $0 | 信息 | 低 KD，叙事契合 |
| private chatgpt | 210 | 35 | $2.98 | 信息 | 隐私品类 |
| local ai server | 90 | 26 ⭐ | $4.26 | 信息 | 服务器化 |
| self-hosted llm | 10 | 22 ⭐ | $4.04 | 信息 | 精准零竞争 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| what is ollama | 3,600 | 50 | $2.29 | 信息 | 认知词 |
| ollama models | 14,800 | 63 | $5.27 | 信息 | 模型库大词 |
| ollama docker | 1,900 | 43 | $0 | 信息 | 部署词 |
| ollama cloud | 1,900 | 56 | $8.12 | 信息/商业 | 官方云，隐私攻击面入口 |
| how to use ollama | 1,300 | 43 | $1.46 | 信息 | 教程词 |
| ollama web ui | 880 | 50 | $2.70 | 信息 | UI 需求 |
| ollama gui | 880 | 67 | $0 | 信息 | UI 需求 |
| ollama ui | 880 | 50 | $4.39 | 信息 | UI 需求 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| does ollama cloud gather information | 720 | 25 ⭐ | $0 | 信息 | 隐私疑虑，Olares 正面回答 |
| how to connect to local ollama | 320 | 31 | $0 | 信息 | 远程访问需求 |
| ollama gpu | 170 | 28 ⭐ | $0 | 信息 | Olares One / GPU 管理 |
| ollama raspberry pi | 50 | 28 ⭐ | $0 | 信息 | 家用设备部署 |
| ollama unraid | 50 | 25 ⭐ | $0 | 信息 | NAS 迁移 |
| ollama synology | 20 | 0 ⭐ | $0 | — | NAS 迁移 |
| ollama remote access | 20 | 0 ⭐ | $0 | — | Olares 随时随地访问 |
| ollama api server | 20 | 0 ⭐ | $0 | — | 服务化 |
| ollama enterprise | 20 | 0 ⭐ | $0 | — | 企业需求前哨 |
| ollama team | 20 | 0 ⭐ | $0 | — | 团队/多用户前哨 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Ollama 只解决"本地跑模型"，但缺 UI、缺随时随地远程访问、缺多用户/备份/GPU 统一管理；Olares = Ollama（共享应用）+ Open WebUI + 自动远程访问 + GPU 管理 + 备份，一站式"永远属于你的私有 AI"。而 Ollama 推付费云后隐私疑虑上升，正是 Olares"本地拥有 + 随时访问"的切入口。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| open webui | 8,100 | 34 | $6.46 | ⭐⭐ 借力大词：Olares Market 一键装 Open WebUI + Ollama = 完整本地 ChatGPT |
| ollama vs lm studio | 1,000 | 24 | $7.05 | ⭐⭐⭐ 对比文，收尾推"两者都能在 Olares 上一键跑" |
| ollama vs llama.cpp | 1,000 | 20 | $13.70 | ⭐⭐⭐ 高量低 KD、CPC 最高 |
| private llm | 720 | 27 | $3.76 | ⭐⭐⭐ Olares 核心定位落地页 |
| does ollama cloud gather information | 720 | 25 | $0 | ⭐⭐⭐ 隐私攻击面：答案是"上云就有风险，Olares 让你本地拥有+随时访问" |
| private gpt | 480 | 18 | $4.28 | ⭐⭐⭐ 低 KD 高意图 |
| local chatgpt | 390 | 17 | $0 | ⭐⭐⭐ Olares 一键搭本地 ChatGPT 栈 |
| self hosted ai | 390 | 36 | $3.90 | ⭐⭐ 品类落地页 |
| how to connect to local ollama | 320 | 31 | $0 | ⭐⭐ 远程访问：Olares 自动域名+VPN 直接解决 |
| lm studio alternative | 260 | 15 | $3.65 | ⭐⭐⭐ 极低 KD |
| ollama vs vllm | 260 | 30 | $6.16 | ⭐⭐ 对比词 |
| ollama alternative | 210 | 16 | $4.30 | ⭐⭐⭐ 极低 KD |
| ollama gpu | 170 | 28 | $0 | ⭐⭐ Olares One GPU 推理 / HAMi 共享 |
| local ai server | 90 | 26 | $4.26 | ⭐⭐ "把家里变成 AI 服务器" |
| ollama vs chatgpt | 90 | 11 | $0 | ⭐⭐⭐ KD 最低、叙事最强：本地 vs 订阅 |
| ollama unraid | 50 | 25 | $0 | ⭐ NAS 用户迁移 |
| ollama raspberry pi | 50 | 28 | $0 | ⭐ 家用设备 |
| ollama remote access | 20 | 0 | $0 | ⭐⭐ Olares 差异化最强点，零竞争 |
| ollama synology | 20 | 0 | $0 | ⭐ NAS 迁移 / GEO |
| ollama enterprise | 20 | 0 | $0 | ⭐ 企业前哨 / GEO |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| open webui | 8,100 | 34 | $6.46 | 信息 | 主词候选 | 借力大词：Olares Market 一键装 Open WebUI + Ollama = 完整本地 ChatGPT 栈 |
| ollama docker | 1,900 | 43 | $0 | 信息 | 次级 | 部署词，Olares 免手动配置 |
| ollama cloud | 1,900 | 56 | $8.12 | 商业 | 次级 | 官方云＝隐私攻击面入口，反衬本地拥有 |
| ollama vs llama.cpp | 1,000 | 20 | $13.70 | 信息 | 主词候选 | 后端引擎对比，收尾"两者都能在 Olares 一键跑"（CPC 最高）|
| ollama vs lm studio | 1,000 | 24 | $7.05 | 信息 | 主词候选 | 桌面本地 LLM 工具对比，导向 Olares Market 一键装 |
| private llm | 720 | 27 | $3.76 | 信息 | 主词候选 | 核心定位落地页：Olares = 你的私有 LLM 基础设施（开源自托管、数据归你）|
| does ollama cloud gather information | 720 | 25 | $0 | 信息 | 主词候选 | 隐私攻击面：上云有风险，Olares 让你本地拥有 + 随时访问 |
| private gpt | 480 | 18 | $4.28 | 信息 | 次级 | 低 KD 高意图，隐私叙事 |
| local chatgpt | 390 | 17 | $0 | 信息 | 次级 | Olares 一键搭本地 ChatGPT 栈 |
| how to connect to local ollama | 320 | 31 | $0 | 信息 | 主词候选 | 远程访问：Olares 自动域名 + VPN 直接解决 |
| lm studio alternative | 260 | 15 | $3.65 | 信息 | 次级 | 极低 KD 平替词 |
| ollama vs vllm | 260 | 30 | $6.16 | 信息 | 次级 | 后端引擎对比词 |
| ollama alternative | 210 | 16 | $4.30 | 信息 | 次级 | 极低 KD 平替词 |
| ollama vs chatgpt | 90 | 11 | $0 | 信息 | 次级 | KD 最低、叙事最强：本地 vs 订阅 |
| ollama remote access | 20 | 0 | $0 | 信息 | GEO | 差异化最强点、零竞争，进直答/FAQ |
| ollama synology | 20 | 0 | $0 | 信息 | GEO | NAS 迁移，进 FAQ |

---

## 核心洞见

1. **品牌护城河**：极强。`ollama` 单词 90,500 月量、误拼变体（olama/ollma/ollam）合计再 1 万+ 月量全在首位——品牌词无法正面刚，只能借"ollama + X / ollama vs X / ollama alternative"长尾承接。
2. **可复制的打法**：**模型库页面是最大流量机器**。ollama.com/library 及各模型子页（llama3.1、gemma4、qwen3-coder、nomic-embed-text…）批量排名对应模型品牌词——这正是 **Olares Market AI 应用详情页可完全复制的程序化模板**：一页一模型/应用，吃"X on Olares / run X locally"。
3. **对 Olares 最关键的 2-3 个词**：`private llm`（720/KD27，核心定位）、`local chatgpt`+`private gpt`（390/480，KD17-18，叙事契合）、`does ollama cloud gather information`（720/KD25，隐私攻击面）。
4. **最大攻击面**：**隐私 + 云化**。Ollama 推付费云（ollama cloud 1,900+ 月量）后，用户开始问"does ollama cloud gather information"（720/KD25）——这是 Olares 最好的切入口：本地拥有、数据不外传、且还能随时随地访问。另一攻击面是 **Ollama 无内置 UI/远程访问**（ollama web ui/gui/ui 各 880、how to connect to local ollama 320），Olares 用 Open WebUI + 自动域名/VPN 一次补齐。
5. **隐藏低 KD 金矿**：`ollama vs chatgpt`（KD11）、`lm studio alternative`（KD15）、`ollama alternative`（KD16）、`local chatgpt`（KD17）、`private gpt`（KD18）、`ollama vs llama.cpp`（KD20，CPC $13.7）——一批 KD<25 且商业/信息意图强的对比与平替词。
6. **GEO 前瞻词**：`ollama remote access`、`ollama synology`、`ollama enterprise`、`ollama team`、`ollama api server`（均量 ~20、KD 0）——近零竞争，语义正对 Olares 的"随时随地访问 / NAS 迁移 / 团队与企业"卖点，适合抢 AI Overview 引用位。
7. **与既有分析的关联**：呼应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 3（本地模型）与方向 2（Market 平替）；`open webui` 大词与 [market/reports/open-webui.md](/Users/pengpeng/seo/directions/market/reports/open-webui.md) 联动做"Ollama + Open WebUI on Olares"内容组；模型库页面（每个模型一个可索引 URL）是应用页 SEO 矩阵的重点选题。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、domain_organic_organic、phrase_related、phrase_these、phrase_questions）| 数据快照 2026-07-04*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
