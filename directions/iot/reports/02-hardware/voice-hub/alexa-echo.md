# Amazon Alexa / Echo SEO 竞品分析报告

> 域名：alexa.amazon.com（主 web app）/ amazon.com/alexa（产品子目录）| SEMrush US | 2026-07-06
> 全球最大云语音助手生态，6 亿+ 设备，2025-03 强制迁移全量云处理，Alexa+ $19.99/月订阅模式——隐私权衡已从"选项"变成"没有选项"。

---

## 项目理解（前置）

Amazon Alexa 是亚马逊的云端语音 AI 助手，通过 Echo 系列智能音箱/显示屏（Echo Dot、Echo Show 等）分发，2014 年 11 月上线，现已成为全球使用最广泛的语音助手平台。核心价值是用自然语言控制智能家居、购物、娱乐，并深度绑定 Amazon Prime/Music/Shopping 生态。2025 年起 Amazon 将 Alexa 平台向生成式 AI 升级（Alexa+），同步于 2025-03-28 移除"Do Not Send Voice Recordings"（本地处理）选项，所有语音请求强制上云——这是本报告最大的叙事攻击面。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 亚马逊生态绑定的云端语音 AI 助手，以 Echo 硬件分发，2025 年起转向 Alexa+ 订阅 |
| 开源 / 许可证 | 完全闭源，云依赖 |
| 主仓库 | 无公开代码仓库；SDK：developer.amazon.com/alexa |
| 核心功能 | 语音控制智能家居、购物下单、音乐/流媒体播放、日历提醒、130,000+ Skills 扩展 |
| 商业模式 / 定价 | Echo 硬件（$29.99–$249.99）；Alexa+ 生成 AI 层 $19.99/月（Prime 会员包含） |
| 差异化 / 价值主张 | 最大生态规模（6 亿+ 设备）、130,000+ Skills、深度绑定 Amazon Shopping/Prime 权益 |
| 主要竞品（初判）| Google Home / Nest（Gemini）、Apple HomePod（Siri）、Home Assistant（开源）|
| Olares Market | HA on Olares（Home Assistant）已上架，是唯一本地开源对标 |
| 来源 | amazon.com/alexa、developer.amazon.com/alexa、grabon.com/blog/alexa-statistics/、arstechnica.com（2025-03）、theregister.com（2025-03-17）|

---

## 流量基线（Phase 1）

> 说明：Alexa 品牌没有独立域名，分散在 `alexa.amazon.com`（Web App 登录入口）、`amazon.com/alexa`（产品子目录）、`developer.amazon.com/alexa`（开发者）等路径下。本报告以 `alexa.amazon.com` 子域名为基线，该子域名是品牌直接导航流量的集中点；`amazon.com/alexa` 子目录流量另行标注。

### 概览（alexa.amazon.com）

| 指标 | 数据 |
|------|------|
| 域名 | alexa.amazon.com（Amazon 主站第 17 大子域名） |
| SEMrush Rank | — （Amazon.com 全域 #1 级别，子域无独立排名） |
| 自然关键词数 | 3,649 |
| 月自然流量（US）| ~272,868 |
| 自然流量估值 | $190,042 / 月 |
| 付费关键词数 | 0（Amazon 不买自家 Alexa 品牌词） |
| 月付费流量 | 0 |
| 排名 1-3 位 | 781 词 |
| 排名 4-10 位 | 601 词 |
| 排名 11-20 位 | 346 词 |

**amazon.com 子域名流量分布（前 20）中，alexa.amazon.com 排名第 17，占整体 Amazon 流量 0.05%，绝对量 272K/月——体量不大，但全部是高意图品牌导航词，极难被非品牌方截流。**

### Amazon.com 子域名流量 TOP（参考）

| 子域名 | 关键词数 | 月流量 | 占比 |
|--------|---------|------|------|
| www.amazon.com | 102,606,050 | 543,715,673 | 96.52% |
| aws.amazon.com | 615,811 | 4,123,731 | 0.73% |
| music.amazon.com | 973,206 | 1,809,024 | 0.32% |
| alexa.amazon.com | 3,649 | 272,868 | 0.05% |

### 官网 TOP 自然关键词（alexa.amazon.com，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| alexa | 1 | 201,000 | 92 | $0.66 | 160,800 | 品牌/导航 | alexa.amazon.com/ |
| amazon alexa | 1 | 49,500 | 96 | $0.95 | 39,600 | 品牌/导航 | alexa.amazon.com/ |
| alexa app | 3 | 60,500 | 73 | $0.56 | 4,961 | 信息/商业 | alexa.amazon.com/ |
| alexa amazon | 1 | 8,100 | 81 | $0.89 | 6,480 | 品牌/导航 | alexa.amazon.com/ |
| alexia | 1 | 14,800 | 50 | $0.27 | 1,953 | 品牌误拼 | alexa.amazon.com/ |
| alexa + | 1 | 2,400 | 86 | $0.66 | 1,920 | 品牌/导航 | alexa.amazon.com/ |
| amazon alexa login | 1 | 2,900 | 62 | $0.00 | 2,320 | 品牌/导航 | alexa.amazon.com/ |
| alexa plus | 2 | 22,200 | 55 | $0.32 | 310 | 信息 | alexa.amazon.com/ |
| amazon alexa app | 3 | 9,900 | 74 | $0.71 | 811 | 信息/商业 | alexa.amazon.com/ |

**洞察：`alexa.amazon.com` 几乎 100% 是品牌导航词——用户直奔 Alexa web app 登录。流量价值极高（$190K/月估值），但与内容 SEO 无关。真正的机会在 amazon.com/alexa 产品页下的功能词，以及第三方对比/隐私词（见 Phase 2/3）。**

### 付费词（Google Ads）

Amazon 对 Alexa/Echo 相关词**零投放**（付费关键词数 = 0）。Amazon 依靠品牌自然流量和站内流量，不购买 Alexa 品牌词广告。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| google home vs alexa | 1,300 | 25 | $0.21 | 信息/对比 | ⭐ 量最大的对比词，KD 低 |
| alexa alternative | 390 | 23 | $0.60 | 信息 | ⭐ 核心攻击词，KD 仅 23 |
| echo alternative | 170 | 34 | $0.37 | 信息 | ⭐ 硬件维度替代词 |
| amazon echo alternative | 140 | 50 | $0.60 | 信息 | KD 偏高，次级词 |
| home assistant vs alexa | 90 | 19 | $0.00 | 信息/对比 | ⭐ KD 19，Olares 核心词 |
| alexa vs home assistant | 20 | 0 | $0.00 | 信息/对比 | ⭐ GEO 级，与上词是同一意图 |
| google home alternative | 110 | 25 | $0.55 | 信息 | ⭐ 跨越 Google/Alexa，可覆盖 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| smart home automation | 49,500 | 76 | $3.91 | 信息/商业 | KD 极高，品类护城河 |
| home assistant | 40,500 | 79 | $1.67 | 品牌/导航 | HA 品牌词（竞品也是我方） |
| home automation | 14,800 | 75 | $2.66 | 信息 | 高 KD |
| home automation hub | 6,600 | 38 | $1.16 | 信息 | ⭐ 细分场景词，KD 38 |
| best smart home hubs | 33,100 | 37 | $0.27 | 信息/商业 | ⭐ 量大 KD 低，综合榜文 |
| smart speaker | 12,100 | 57 | $0.26 | 信息 | 中等竞争 |
| best smart speaker | 偏低 | — | — | 商业 | 榜单词需补查 |
| voice assistant | 2,400 | 78 | $1.81 | 信息 | KD 极高 |
| voice assistants | 880 | 50 | $1.14 | 信息 | 中等 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| alexa plus cost | 5,400 | 55 | $0.51 | 信息 | 订阅定价最高搜索量 |
| alexa plus review | 1,000 | 38 | $0.03 | 信息 | ⭐ KD 38，评测意图 |
| alexa plus features | 590 | 50 | $0.14 | 信息 | 功能了解意图 |
| alexa plus vs alexa | 110 | 39 | $0.14 | 信息 | ⭐ 免费 vs 付费对比 |
| alexa plus subscription | 140 | 58 | $0.61 | 信息 | 订阅意图 |
| cancel alexa plus | 170 | 27 | $0.82 | 信息 | ⭐ 取消订阅信号词，KD 低 |
| alexa recording conversations | 260 | 43 | $1.98 | 信息 | 隐私担忧意图 |
| home assistant alexa integration | 320 | 25 | $0.00 | 信息 | ⭐ 已有 HA 用户求整合 |
| home assistant voice preview edition | 1,900 | 28 | $0.76 | 信息 | ⭐ HA Voice PE 独立热词 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| home assistant voice | 2,400 | 47 | $0.64 | 信息 | HA Voice Pipeline 入口 |
| home assistant voice preview edition | 1,900 | 28 | $0.76 | 信息 | ⭐ Voice PE 专有词，KD 28 |
| piper tts | 1,300 | 25 | $2.88 | 信息 | ⭐ 本地 TTS 引擎，KD 低 |
| home assistant voice assistant | 390 | 25 | $1.00 | 信息 | ⭐ 精准意图 |
| home assistant speaker | 390 | 29 | $0.70 | 信息 | ⭐ 卫星音箱话题 |
| wyoming satellite | 210 | 28 | $0.00 | 信息 | ⭐ Wyoming Satellite 组件 |
| home assistant ollama | 170 | 27 | $0.00 | 信息 | ⭐ 本地 LLM+语音 |
| home assistant alexa integration | 320 | 25 | $0.00 | 信息 | ⭐ 迁移路径词 |
| home assistant assist | 140 | 36 | $4.13 | 导航 | ⭐ HA Assist 组件词 |
| wyoming protocol | 140 | 19 | $0.00 | 信息 | ⭐ KD 19，极低竞争 |
| home assistant tts | 70 | 25 | $0.00 | 信息 | ⭐ TTS 配置词 |
| open source voice assistant | 140 | 58 | $0.00 | 信息 | KD 偏高 |
| voice assistant raspberry pi | 70 | 16 | $0.00 | 信息 | ⭐ KD 16，DIY 用户 |
| self hosted voice assistant | 20 | 0 | $0.00 | 信息 | GEO 前哨 |

---

## Olares 关联词（Phase 3）

**核心叙事：Alexa 2025-03 取消本地模式 + Alexa+ $19.99/月双重逼迁 → HA Voice PE（Wyoming Satellite + Whisper + Piper）on Olares = 完全本地、无订阅、不出设备的语音助手替代。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| alexa alternative | 390 | 23 | $0.60 | ⭐⭐⭐ 主攻词：HA Voice PE on Olares = 不联云的 Alexa 替代，一键安装 |
| home assistant vs alexa | 90 | 19 | $0.00 | ⭐⭐⭐ KD 19 极低；Olares 承载 HA，让"选 HA"等于"不换硬件也能跑" |
| does alexa spy on you | 720 | 21 | $4.88 | ⭐⭐⭐ CPC $4.88 说明商业价值高；Alexa 2025-03 移除本地模式是最强证据 |
| cancel alexa plus | 170 | 27 | $0.82 | ⭐⭐⭐ 取消订阅信号词，接取消用户到 Olares + HA 无订阅方案 |
| alexa privacy concerns | 140 | 39 | $0.00 | ⭐⭐ 隐私担忧用户，展示 Olares 本地推理 = 数据不出设备 |
| home assistant voice preview edition | 1,900 | 28 | $0.76 | ⭐⭐⭐ 量大 KD 低；Voice PE 正是 Olares 上 HA 语音的旗舰体验 |
| piper tts | 1,300 | 25 | $2.88 | ⭐⭐⭐ Piper 是 HA Voice PE 本地 TTS 引擎；Olares 上开箱即配 |
| wyoming satellite | 210 | 28 | $0.00 | ⭐⭐⭐ Wyoming Satellite 卫星音箱方案；在 Olares 跑 HA 后可一键扩展到多房间 |
| home assistant ollama | 170 | 27 | $0.00 | ⭐⭐⭐ 本地 LLM（Ollama）+ 语音（HA Voice PE）on Olares = 完全本地 AI 语音 |
| wyoming protocol | 140 | 19 | $0.00 | ⭐⭐ KD 19，技术爱好者意图，对接 HA Voice PE 技术文 |
| alexa voice history | 390 | 19 | $1.17 | ⭐⭐ 查看/删除语音历史意图；说明用户已对数据留存有意识，Olares 本地=无历史可外泄 |
| alexa on-device processing removal | 320 | 36 | $0.00 | ⭐⭐ 2025-03 事件词，用于时事文；Olares + HA = 本地处理从未被 Amazon 控制 |
| amazon echo local processing ending | 170 | 40 | $0.00 | ⭐⭐ 同上，事件叙事词 |
| google home vs alexa | 1,300 | 25 | $0.21 | ⭐⭐ 对比文可延伸到"两者都云"→HA on Olares = 唯一不云选项 |
| home assistant alexa integration | 320 | 25 | $0.00 | ⭐⭐ 现有 Alexa 用户求 HA 整合；Olares 上 HA 可继续桥接现有 Echo 设备 |
| alexa eavesdropping | 40 | 34 | $0.00 | ⭐⭐ 隐私信号词，可切入 Olares 本地音频处理叙事 |
| alexa always listening | 90 | 26 | $0.00 | ⭐⭐ KD 26，常开麦克风担忧；Whisper 本地化让麦克风数据不离设备 |
| home assistant voice control | 590 | 37 | $1.46 | ⭐⭐ 功能词，跑在 Olares 上的 HA 语音控制 |
| voice assistant raspberry pi | 70 | 16 | $0.00 | ⭐⭐ DIY 用户，Olares 可装在 Pi 上做本地语音 server |
| self hosted voice assistant | 20 | 0 | $0.00 | ⭐⭐⭐ 近零量 GEO 前哨，AI Overview 引用位，精准意图 |
| local voice assistant home assistant | 20 | 0 | $0.00 | ⭐⭐⭐ GEO 前哨，语义极精准，抢引用位 |
| home assistant local voice | 20 | 0 | $0.00 | ⭐⭐⭐ GEO，同上 |
| offline voice assistant | 20 | 0 | $0.00 | ⭐⭐⭐ GEO 前哨，与 Alexa 2025-03 事件直接对位 |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| google home vs alexa | 1,300 | 25 | $0.21 | 信息/对比 | **主词候选** | 量最大低 KD 对比词；延伸叙事"两者均全量云→HA on Olares 是唯一不云选项" |
| home assistant voice preview edition | 1,900 | 28 | $0.76 | 信息 | **主词候选** | HA Voice PE 独立热词量大 KD 28；HA on Olares 的旗舰 voice 体验入口 |
| piper tts | 1,300 | 25 | $2.88 | 信息 | **主词候选** | CPC $2.88 异常高说明有商业价值；Piper 是 Olares 上 HA Voice PE 本地 TTS 组件 |
| does alexa spy on you | 720 | 21 | $4.88 | 信息 | **主词候选** | CPC $4.88 高，KD 21 低；2025-03 移除本地模式是最强佐证 |
| alexa alternative | 390 | 23 | $0.60 | 信息 | **主词候选** | 核心攻击词 KD 23；HA Voice PE on Olares 是唯一完全离线替代 |
| home assistant voice | 2,400 | 47 | $0.64 | 信息 | **主词候选** | 量大；HA Voice Pipeline 入口词，KD 47 可战，属于已有 HA 报告延伸 |
| alexa privacy | 480 | 56 | $1.10 | 信息 | 次级 | KD 56 偏高，并入隐私叙事文作 H2 |
| alexa privacy concerns | 140 | 39 | $0.00 | 信息 | 次级 | ⭐ 低 KD 信号词，并入隐私文 |
| alexa plus review | 1,000 | 38 | $0.03 | 信息 | 次级 | KD 38 可考虑，CPC 极低意图偏信息，并入 Alexa+ 评测文 |
| cancel alexa plus | 170 | 27 | $0.82 | 信息 | **主词候选** | KD 27，取消订阅意图强；接"取消用户"到 Olares 无订阅方案 |
| home assistant vs alexa | 90 | 19 | $0.00 | 信息/对比 | **主词候选** | KD 19 极低；与 `alexa alternative` 形成簇，量虽 90 但战略价值高 |
| alexa voice history | 390 | 19 | $1.17 | 信息 | **主词候选** | KD 19 金矿；用户已意识到录音留存，Olares 本地=无外泄历史 |
| wyoming satellite | 210 | 28 | $0.00 | 信息 | **主词候选** | Wyoming Satellite 卫星方案词，KD 28，HA Voice PE 拓扑核心 |
| home assistant ollama | 170 | 27 | $0.00 | 信息 | **主词候选** | KD 27；本地 LLM+语音结合意图，Olares 差异化叙事 |
| alexa on-device processing removal | 320 | 36 | $0.00 | 信息 | 次级 | 时事词，并入隐私/替代文 |
| amazon echo local processing ending | 170 | 40 | $0.00 | 信息 | 次级 | 同上 |
| home assistant alexa integration | 320 | 25 | $0.00 | 信息 | 次级 | ⭐ KD 25，现有 Alexa 用户迁移词，并入 voice PE 教程 |
| alexa always listening | 90 | 26 | $0.00 | 信息 | 次级 | ⭐ 常开麦克风担忧词，并入隐私文 |
| wyoming protocol | 140 | 19 | $0.00 | 信息 | 次级 | ⭐ KD 19 技术词，并入 Voice PE 教程 |
| home assistant assist | 140 | 36 | $4.13 | 导航 | 次级 | CPC $4.13 价值词，并入 HA Voice 教程 |
| voice assistant raspberry pi | 70 | 16 | $0.00 | 信息 | 次级 | ⭐ KD 16 最低，DIY 用户，Olares Pi 安装叙事 |
| alexa eavesdropping | 40 | 34 | $0.00 | 信息 | 次级 | 隐私信号词，并入 alexa spy 文 |
| self hosted voice assistant | 20 | 0 | $0.00 | 信息 | **GEO** | 零量但精准，抢 AI Overview / Perplexity 引用位 |
| offline voice assistant | 20 | 0 | $0.00 | 信息 | **GEO** | 与 2025-03 事件直接对位，GEO 前哨 |
| local voice assistant home assistant | 20 | 0 | $0.00 | 信息 | **GEO** | 精准意图，FAQ 段抢引用 |
| home assistant local voice | 20 | 0 | $0.00 | 信息 | **GEO** | GEO，同上 |
| local llm voice assistant | 20 | 0 | $0.00 | 信息 | **GEO** | LLM+本地语音，Olares 差异化 GEO 词 |
| home assistant alexa alternative | 20 | 0 | $0.00 | 信息 | **GEO** | 精准意图组合，引用位价值极高 |

---

## 核心洞见

1. **品牌护城河**：`alexa`（201K/月，KD 92）、`amazon alexa`（49.5K，KD 96）无法正面刚——这些词全部是品牌导航词，Amazon #1 排名牢不可破。正面攻击无意义；战场在**隐私担忧词**（`does alexa spy on you` KD 21）、**对比词**（`home assistant vs alexa` KD 19）和**HA Voice 组件词**（`wyoming satellite` KD 28，`piper tts` KD 25）。

2. **可复制的打法**：Amazon 不做内容 SEO——`alexa.amazon.com` 几乎全是品牌导航，没有任何内容页面。这给第三方留下了大量无人竞争的**信息/对比意图空间**：评测文、对比文、教程文（"如何迁移到 HA Voice PE"）是可切入的打法。

3. **对 Olares 最关键的词**：
   - `does alexa spy on you`（720 月量，KD 21，CPC $4.88）——隐私担忧最高量低 KD 词，天然流量漏斗
   - `cancel alexa plus`（170 月量，KD 27）——订阅取消意图，接退出用户
   - `home assistant vs alexa`（90 月量，KD 19）——最精准对比词，HA on Olares 差异化极强

4. **最大攻击面**：**2025-03-28 事件**是本报告最强叙事核弹：Amazon 强制取消所有 Echo 设备的本地处理，并发布 Alexa+ $19.99/月订阅——同一天，**"所有语音数据强制上云"**和**"付费墙"**同时落地。这是隐私词（`alexa on-device processing removal`、`amazon echo local processing ending`）和付费词（`cancel alexa plus`）双线齐发的新闻钩子，可做时效性内容。

5. **隐藏低 KD 金矿**：
   - `alexa voice history`（390 月量，**KD 19**）——声量不低，竞争极低
   - `wyoming protocol`（140 月量，**KD 19**）——技术组件词，精准受众
   - `voice assistant raspberry pi`（70 月量，**KD 16**）——DIY 用户，Olares Pi 安装路径
   - `home assistant vs alexa`（90 月量，**KD 19**）——对比词 KD 最低

6. **GEO 前瞻布局**：`self hosted voice assistant`、`offline voice assistant`、`local voice assistant home assistant`、`home assistant alexa alternative`、`local llm voice assistant` 均为近零量但语义精准词。2025-03 事件持续升温，这类词的 AI Overview 引用位将是未来 6-12 个月的重要曝光渠道。需要在文章中以问答格式明确覆盖："What is the best offline voice assistant that replaces Alexa?" → HA Voice PE on Olares。

7. **与既有分析的关联**：
   - `piper tts`（1,300 月量，KD 25，**CPC $2.88**）——高 CPC 说明有商业价值，与 olares-500-keywords 中 TTS 相关词形成补充，可单独做一篇 Piper TTS 教程文（顺带覆盖 HA Voice PE 配置）
   - `home assistant voice preview edition`（1,900 月量，KD 28）——量大 KD 低，HA 的已有 SEO 报告流量 302K/月，延伸本词是低成本高回报选择
   - `google home vs alexa`（1,300 月量，KD 25）——量最大的入口词，已有 HA 报告可联动：Google Home vs Alexa vs HA，三者对比中 HA 是唯一本地选项
   - `home assistant ollama`（170 月量，KD 27）——Ollama on Olares + HA Voice PE = 完整本地 AI 语音栈，差异化叙事词

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、phrase_these、phrase_related、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；IoT 类产品全球量通常为美国的 3-5 倍。*
*项目理解来源：amazon.com/alexa、grabon.com/blog/alexa-statistics/（2026）、arstechnica.com（2025-03）、theregister.com（2025-03-17）、mordorintelligence.com（2026）。*
