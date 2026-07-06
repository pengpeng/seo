# Fish Speech SEO 竞品分析报告

> 域名：fish.audio | SEMrush US | 2026-07-06
> Fish Speech 是 SOTA 开源多语言 TTS 模型，fish.audio 是其商业平台——全球最大的 AI 语音市场之一，可通过 API 使用或完全自托管，ElevenLabs 最具性价比的开源替代品。

---

## 项目理解（前置）

Fish Speech 是由 Fish Audio 开发的开源文字转语音（TTS）项目，核心模型为 S2 Pro（4B 参数，Dual-AR 架构 + RL 对齐）。模型在 1000 万小时音频数据上训练，支持 80+ 语言，可通过内联情绪标签（`[laugh]`、`[whispers]` 等）精细控制语调。fish.audio 是其商业落地平台：提供 SaaS API、200 万+ 声音的社区语音库，以及 15 秒完成声音克隆的工具。GitHub 仓库 `fishaudio/fish-speech` 拥有 31K stars，是当前开源 TTS 最受关注的项目之一。Fish Speech 已上架 Olares Market，可一键自托管运行完整 WebUI + API。

| 项目 | 内容 |
|------|------|
| 一句话定位 | SOTA 开源多语言 TTS，商业平台+开源模型双轨并行 |
| 开源 / 许可证 | 是，Fish Audio Research License（非商业研究用途免费，商业需授权） |
| 主仓库 | [github.com/fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)（★31K，100+ 贡献者） |
| 核心功能 | 多语言 TTS（80+ 语言）、15 秒声音克隆、情绪标签内联控制、实时流式 WebSocket API、ROCm/CUDA GPU 推理 |
| 商业模式 / 定价 | SaaS：$15/1M UTF-8 bytes，ASR $0.36/小时；s2.1-pro-free 有限免费额度；企业自托管从 $10K/月起；开源模型可免费自部署（研究许可） |
| 差异化 / 价值主张 | 开源权重可自托管、情绪标签控制精细、2M+ 社区声音库、支持 CUDA/ROCm/CPU，对比 ElevenLabs 无 credits 上限焦虑 |
| 主要竞品（初判）| ElevenLabs、Narakeet、Coqui TTS（已停服）、Kokoro TTS、Piper TTS |
| Olares Market | 已上架（`fish-speech`，⬜ 待跑报告→此报告覆盖）|
| 来源 | [fish.audio](https://fish.audio)、[github.com/fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)、[docs.fish.audio](https://docs.fish.audio)、[arxiv.org/abs/2603.08823](https://arxiv.org/abs/2603.08823) |

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | fish.audio |
| SEMrush Rank | 25,637 |
| 自然关键词数 | 35,445 |
| 月自然流量（US）| 85,068 |
| 自然流量估值 | $26,666/月 |
| 付费关键词数 | 795 |
| 月付费流量 | 25,201 |
| 付费流量估值 | $16,368/月 |
| 排名 1-3 位 | 2,149 词 |
| 排名 4-10 位 | 3,408 词 |
| 排名 11-20 位 | 3,837 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| fish.audio | 35,220 | 84,545 | 99.39% |
| speech.fish.audio | 90 | 391 | 0.46% |
| docs.fish.audio | 129 | 132 | 0.16% |
| diff.fish.audio | 5 | 0 | — |
| status.fish.audio | 1 | 0 | — |

主站 fish.audio 几乎垄断全部流量；speech.fish.audio 是开源模型独立文档站，关键词数少但有独立排名机会。

### 官网 TOP 自然关键词（按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| fish audio | 1 | 22,200 | 23 | $0.26 | 5,505 | 商业 | /tts/ |
| fish.audio | 1 | 4,400 | 40 | $0.26 | 3,520 | 导航 | / |
| fish audio | 2 | 22,200 | 23 | $0.26 | 2,930 | 商业 | /discovery/ |
| fish.audio ai | 1 | 1,900 | 23 | $0.26 | 1,520 | 导航 | / |
| caine | 4 | 60,500 | 43 | $0.34 | 1,331 | 信息 | /m/…/ |
| little einsteins fish audio | 1 | 1,300 | 23 | $0.00 | 1,040 | 信息 | /m/…/ |
| fish audio | 5 | 22,200 | 23 | $0.26 | 976 | 商业 | /studio/ |
| fish audio | 8 | 22,200 | 23 | $0.26 | 532 | 商业 | /m/…/ |
| fish audio | 9 | 22,200 | 23 | $0.26 | 532 | 商业 | /app/speech-to-text/ |
| caine tadc | 8 | 27,100 | 34 | $0.00 | 514 | 信息 | /m/…/ |
| c00lkidd voice changer | 1 | 1,900 | 12 | $0.26 | 471 | 信息 | /m/…/ |
| fish auidio（拼写变体） | 1 | 1,900 | 0 | — | 471 | 商业 | /tts/ |
| bluudud voice changer | 1 | 1,900 | 12 | $0.82 | 471 | 信息 | /m/…/ |
| fishaudio | 3 | 5,400 | 43 | $0.26 | 442 | 信息 | /discovery/ |
| fish audio app | 1 | 480 | 25 | $0.10 | 384 | 商业 | /tts/ |
| trump voice generator | 3 | 4,400 | 15 | — | 360 | 信息 | /m/…/ |
| peter griffin ai | 1 | 1,300 | 13 | — | 322 | 信息 | /m/…/ |
| spongebob ai | 1 | 1,300 | 18 | — | 322 | 信息 | /m/…/ |
| spongebob ai voice | 1 | 1,300 | 14 | $1.06 | 322 | 信息 | /m/…/ |
| fish audio text to speech | 1 | 390 | 40 | $0.49 | 312 | 商业 | / |
| raspy ai | 3 | 3,600 | 20 | — | 234 | 信息 | /voice-library/raspy/ |
| fish speech - boody ai | 1 | 260 | 38 | — | 208 | 导航 | / |
| 语音克隆 | 1 | 720 | 30 | $1.04 | 178 | 信息 | /zh-CN/ |
| microsoft sam text to speech | 10 | 8,100 | 43 | $2.25 | 178 | 信息 | /m/…/ |
| text to speech | 31 | 246,000 | 88 | $0.57 | 172 | 信息 | /tts/ |

**洞察**：流量高度依赖品牌词及 `/m/<id>/` 程序化声音库页——每个上传的声音页面都是一个长尾排名机会，产生了大量低 KD 尾词流量（角色语音、名人声音生成）。格式转换页（`/audio-converter/`）意外承接了大量格式转换查询。

### 付费词（Google Ads，按流量排序）

Fish Audio 正在主动投放竞品品牌词拦截竞争对手用户，策略进攻性很强。

| 关键词 | 排名 | 月量 | CPC | 流量 | 落地页 |
|--------|------|------|-----|------|--------|
| wav to mp3 | 1 | 33,100 | — | 1,555 | /audio-converter/wav-to-mp3/ |
| text to speech free | 1 | 33,100 | $0.90 | 1,555 | /tts/ |
| **elevenlabs** | 3 | 165,000 | $0.61 | 1,485 | /tts/ |
| fish audio | 1 | 22,200 | $0.26 | 1,043 | / |
| format mp4 en mp3 | 1 | 18,100 | $0.19 | 850 | /audio-converter/mp4-to-mp3/ |
| convert m4a to mp3 | 1 | 12,100 | $0.65 | 568 | /audio-converter/m4a-to-mp3/ |
| m4a to wav | 1 | 12,100 | $0.27 | 568 | /audio-converter/m4a-to-wav/ |
| turn mp4 to mp3 | 1 | 9,900 | $0.21 | 465 | /audio-converter/mp4-to-mp3/ |
| **narakeet** | 1 | 9,900 | $1.08 | 465 | / |
| wav to mp3 converter | 1 | 8,100 | $0.60 | 380 | /audio-converter/wav-to-mp3/ |
| **ai voice generator** | 6 | 74,000 | $1.15 | 370 | /tts/ |
| **11 labs** | 2 | 27,100 | $0.39 | 352 | /app/text-to-speech/ |
| ai voice text to speech | 1 | 6,600 | $1.29 | 310 | /tts/ |
| **voice.ai** | 1 | 4,400 | $2.00 | 206 | /tts/ |

买 `elevenlabs`（165K 月量，CPC $0.61）是最大手笔——直接在竞品品牌词上拦截其流量。同时配套投放格式转换大词（wav to mp3、m4a to mp3 等），以免费工具引流再转化到 TTS 产品。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| fish.audio vs elevenlabs | 590 | 9 | — | 信息 | ⭐ 已有品牌比较需求 |
| elevenlabs alternative free | 590 | 29 | $1.66 | 信息 | ⭐ 高价值；免费诉求 |
| elevenlabs alternative | 480 | 9 | $6.16 | 信息 | ⭐ 核心对比词 |
| free voice cloning | 1,000 | 56 | $1.39 | 信息 | KD 较高，仍值得布局 |
| voice cloning free | 1,000 | 63 | $1.17 | 信息 | 同上变体 |
| piper tts | 1,300 | 25 | $2.88 | 信息 | ⭐ 另一开源 TTS 竞品；KD 低 |
| xtts | 720 | 35 | $3.18 | 信息 | Coqui XTTS 竞品词 |
| open source tts | 260 | 32 | $5.48 | 信息 | 分类竞争词 |
| fish audio vs elevenlabs | 20 | 9 | $4.42 | 信息 | ⭐ 品牌对比变体 |
| fish audio alternative | 20 | 0 | — | — | ⭐ 机会词，量小但 KD=0 |
| elevenlabs open source alternative | 20 | 0 | $1.61 | — | ⭐ GEO 前哨 |
| coqui tts alternative | 20 | 0 | — | — | ⭐ Coqui 停服遗留流量 |
| elevenlabs self hosted | 20 | 0 | $9.25 | — | ⭐ CPC 极高，商业意图强 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai voice generator | 74,000 | 83 | $1.15 | 信息 | KD 过高，付费拦截比排名更现实 |
| text to speech free | 27,100 | 82 | $0.79 | 信息 | 同上；fish.audio 已在投放 |
| ai voice cloning | 4,400 | 71 | $1.61 | 信息 | 品类核心词，KD 高 |
| ai tts | 2,400 | 80 | $1.22 | 信息 | 竞争激烈 |
| kokoro tts | 2,400 | 64 | $2.58 | 信息 | 开源 TTS 品类词；竞品 |
| voice cloning software | 390 | 63 | $1.91 | 信息 | 商业意图 |
| text to speech api | 720 | 47 | $4.66 | 信息 | 开发者词；CPC 高 |
| voice synthesis | 260 | 48 | $0.88 | 信息 | 技术词 |
| best open source tts | 140 | 39 | $5.26 | 信息 | ⭐ KD 适中；SEO 可攻 |
| tts api free | 140 | 32 | $3.25 | 信息 | ⭐ 开发者高意图 |
| voice cloning api | 70 | 48 | $2.96 | 信息 | 开发者词 |
| real time tts | 50 | 30 | $1.49 | 信息 | ⭐ 低 KD；实时场景 |
| best tts model | 70 | 10 | $4.55 | 信息 | ⭐ KD 极低，高商业 CPC |
| multilingual tts | 20 | 0 | $2.37 | — | ⭐ GEO 前哨 |

### 产品 / 功能词（品牌前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| fish audio | 22,200 | 23 | $0.26 | 商业 | 品牌核心词，已排第 1 |
| fishaudio | 5,400 | 38 | $0.26 | 信息 | 品牌变体 |
| fish ai | 2,400 | 19 | $0.10 | 信息 | ⭐ 品牌联想词，KD 低 |
| fish speech | 480 | 50 | $0.89 | 信息 | 开源模型核心词 |
| fish-speech | 480 | 45 | $1.18 | 信息 | 品牌变体 |
| fish audio voice cloning | 210 | 28 | $1.17 | 商业 | ⭐ 功能词，KD 低 |
| fish audio api | 90 | 24 | $1.64 | 商业 | ⭐ 开发者功能词 |
| fish audio pricing | 70 | 8 | — | 商业 | ⭐ KD 极低；高转化意图 |
| fish speech api | 30 | 35 | $7.33 | 信息 | CPC 极高 |
| fish speech github | 50 | 0 | — | — | ⭐ 开发者调研路径 |
| fish speech s2 pro | 40 | 0 | $3.36 | — | ⭐ 最新模型词，KD=0 |
| fish speech docker | 20 | 0 | — | — | ⭐ 自托管信号词 |
| fish speech tts | 20 | 0 | — | — | ⭐ |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| open source text to speech | 260 | 49 | $1.41 | 信息 | 品类级开源词 |
| open source voice cloning | 140 | 35 | $2.23 | 信息 | ⭐ 语义精准 |
| best open source tts | 140 | 39 | $5.26 | 信息 | ⭐ 高 CPC，商业意图 |
| local tts | 110 | 24 | $4.73 | 信息 | ⭐ KD 低，本地运行意图清晰 |
| self hosted voice cloning | 20 | 0 | — | — | ⭐ GEO 前哨 |
| tts docker | 20 | 0 | — | — | ⭐ 技术信号词 |
| text to speech self hosted | 20 | 0 | — | — | ⭐ 精准意图 |
| elevenlabs self hosted | 20 | 0 | $9.25 | — | ⭐ CPC $9.25，高商业价值 |

---

## Olares 关联词（Phase 3）

**核心逻辑：Fish Speech 在 Olares Market 一键部署，提供与 fish.audio SaaS 同质量的 TTS，无 API 费用、数据完全私有——精准切 ElevenLabs 定价痛点（credits 限制 + 隐私顾虑）与企业合规场景。**

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|----|-----------|------|
| elevenlabs alternative | 480 | 9 | $6.16 | Fish Speech on Olares = 免 credits 的开源平替，一键部署无数据泄露 | ⭐⭐⭐ |
| elevenlabs alternative free | 590 | 29 | $1.66 | "免费"诉求+隐私诉求，Olares 自托管完全覆盖 | ⭐⭐⭐ |
| fish.audio vs elevenlabs | 590 | 9 | — | 对比内容：自托管 Fish Speech via Olares vs ElevenLabs SaaS | ⭐⭐⭐ |
| open source voice cloning | 140 | 35 | $2.23 | Fish Speech S2 Pro 开源权重 + Olares 一键跑起来 | ⭐⭐⭐ |
| local tts | 110 | 24 | $4.73 | Olares 本地运行 Fish Speech = 隐私本地 TTS | ⭐⭐⭐ |
| self hosted voice cloning | 20 | 0 | — | 精准自托管意图，Olares Market 直接落地 | ⭐⭐⭐ |
| elevenlabs self hosted | 20 | 0 | $9.25 | 高 CPC 说明有强商业意图；"ElevenLabs 想自托管" = Fish Speech on Olares | ⭐⭐⭐ |
| text to speech self hosted | 20 | 0 | — | 精准自托管 TTS 意图 | ⭐⭐⭐ |
| fish speech docker | 20 | 0 | — | Docker 部署 = Olares 容器化方案 | ⭐⭐ |
| fish audio api | 90 | 24 | $1.64 | 自托管后无限 API 调用，适配 Olares Agent 生态 | ⭐⭐ |
| best open source tts | 140 | 39 | $5.26 | Fish Speech on Olares 可作为 "best open source TTS" 推荐 | ⭐⭐ |
| tts api free | 140 | 32 | $3.25 | 自托管后 API 免费；Olares 一键部署即可 | ⭐⭐ |
| fish audio voice cloning | 210 | 28 | $1.17 | 声音克隆功能 + Olares 私有部署 = 0 数据上云 | ⭐⭐ |
| piper tts | 1,300 | 25 | $2.88 | Piper 是另一开源 TTS，Olares 也可布局对比内容 | ⭐⭐ |
| 语音克隆 | 720 | 30 | $1.04 | 中文用户群；Olares 中文市场切入点 | ⭐⭐ |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| elevenlabs alternative | 480 | 9 | $6.16 | 信息 | **主词候选** | KD 极低、CPC 高、商业意图强；Olares 切入"免 credits 开源平替"叙事，是核心攻击词 |
| fish.audio vs elevenlabs | 590 | 9 | — | 信息 | **主词候选** | 已有自然需求（590 vol）且 KD=9；写 "Fish Speech self-hosted vs ElevenLabs" 对比文，Olares 作为部署载体 |
| elevenlabs alternative free | 590 | 29 | $1.66 | 信息 | **主词候选** | 与上词语义相近可合并成一篇；"免费"+"开源"诉求 Olares 完美覆盖 |
| local tts | 110 | 24 | $4.73 | 信息 | **主词候选** | KD 低、CPC 高；Olares 本地 TTS 场景直接命中 |
| open source voice cloning | 140 | 35 | $2.23 | 信息 | **主词候选** | 信息意图但 CPC 可观；Fish Speech S2 Pro + Olares 自托管是最佳答案 |
| fish audio voice cloning | 210 | 28 | $1.17 | 商业 | **主词候选** | 功能词量尚可、KD 低；可做 Fish Audio 声音克隆教程 + Olares 私有部署 |
| fish audio api | 90 | 24 | $1.64 | 商业 | **次级** | 开发者词；并入"自托管 Fish Speech API"教程文 |
| fish audio pricing | 70 | 8 | — | 商业 | **次级** | KD=8，高转化意图；可在对比文中引用定价痛点（credits 焦虑）切换到自托管 |
| best open source tts | 140 | 39 | $5.26 | 信息 | **次级** | 略高 KD，但 CPC 强；并入品类综述文 |
| tts api free | 140 | 32 | $3.25 | 信息 | **次级** | 开发者意图；Olares 自托管后 API 免费是核心卖点 |
| piper tts | 1,300 | 25 | $2.88 | 信息 | **次级** | Piper 是另一开源 TTS；可做 "Fish Speech vs Piper TTS" 对比，Olares 两者都支持 |
| fish audio pricing | 70 | 8 | — | 商业 | **次级** | 并入对比文 |
| best tts model | 70 | 10 | $4.55 | 信息 | **次级** | KD=10，CPC 高；信息词但商业价值大，可作 FAQ 段落 |
| self hosted voice cloning | 20 | 0 | — | — | **GEO** | 精准意图，抢 AI Overview 引用位 |
| text to speech self hosted | 20 | 0 | — | — | **GEO** | 同上，极精准 |
| elevenlabs self hosted | 20 | 0 | $9.25 | — | **GEO** | CPC $9.25 说明高商业价值；GEO 引用会带高质量流量 |
| fish speech docker | 20 | 0 | — | — | **GEO** | 技术精准词；Olares 容器化场景 |
| multilingual tts | 20 | 0 | $2.37 | — | **GEO** | 语义精准，抢引用位 |

---

## 核心洞见

1. **品牌护城河**：fish.audio 品牌词（"fish audio"，22K 月量，KD 23）已被深度占领，排名第 1。品牌认知强但护城河不高（KD 仅 23）——说明品牌词尚未成为防御型壁垒，竞争者可用对比内容切入。与品牌主词正面刚无意义；重点攻击对比词（vs ElevenLabs）和场景词（self-hosted、local TTS）。

2. **可复制的打法**：
   - **程序化声音库页**：每个 `/m/<id>/` 页面都是一个长尾排名机会，fish.audio 已靠 2M+ 社区声音页积累大量低 KD 流量（角色声音、名人声音生成词）；
   - **格式转换引流漏斗**：`/audio-converter/` 系列页面把音频格式工具查询导入 TTS 产品，是巧妙的工具型 SEO 引流——但这条路 Olares 不需要复制；
   - **竞品品牌词付费拦截**：直接买 `elevenlabs`（165K 月量）做 Google Ads，代价低（CPC $0.61）但意图极精准；内容层也可用同样逻辑写对比文拦截自然流量。

3. **对 Olares 最关键的词**：
   - `elevenlabs alternative`（480 vol / KD 9）——最高性价比的主词，可单独成文；
   - `fish.audio vs elevenlabs`（590 vol / KD 9）——已有需求且 KD 极低，写对比文直接落 Olares 自托管优势；
   - `local tts`（110 vol / KD 24）——本地 TTS 精准场景词，Olares 一键部署直接命中；

4. **最大攻击面**：ElevenLabs 的 credits 定价模式（按字符计费、月度限额、$5-99/月订阅，超出还要额外付费）是最大用户痛点。Fish Speech on Olares = 一次部署、无限 TTS、数据不上云——用"`elevenlabs self hosted`"（CPC $9.25！）和"`elevenlabs alternative free`"两词的内容，可精准切这批高意图用户。

5. **隐藏低 KD 金矿**：
   - `fish audio pricing`（KD=8，70 vol）：定价对比页，Olares 自托管零边际成本；
   - `best tts model`（KD=10，70 vol）：信息词但 CPC $4.55，说明商业意图强；
   - `fish audio vs elevenlabs` / `fish.audio vs elevenlabs`（KD=9，共 600+ vol）：几乎零竞争的对比词；
   - `fish ai`（KD=19，2400 vol）：品牌联想词，KD 低且量大；

6. **GEO 前瞻布局**：以下词当前近零量但语义精准，适合写进对比文的 FAQ/前瞻段，抢 AI Overview / Perplexity 引用：
   - `self hosted voice cloning`
   - `text to speech self hosted`
   - `elevenlabs self hosted`（CPC $9.25 → AI 答案可能替代高价 PPC）
   - `fish speech docker`
   - `multilingual tts`
   - `tts docker`

7. **与既有分析的关联**：`olares-500-keywords` 中的语音/TTS 相关词（如 "text to speech"、"voice cloning"）基本 KD 过高（80+），Fish Speech 报告的价值在于补充 **ElevenLabs 替代词簇**（KD 9-29）和**本地/自托管 TTS 词簇**（KD 0-35）——这是 500 词分析在 TTS 赛道的重要补白，可作为后续 ElevenLabs alternative 内容文章的核心关键词依据。

---

*数据来源：SEMrush US 数据库（domain_rank、resource_organic、domain_organic_subdomains、resource_adwords、domain_organic_organic、phrase_these、phrase_related、phrase_fullsearch、phrase_questions）| 2026-07-06*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
