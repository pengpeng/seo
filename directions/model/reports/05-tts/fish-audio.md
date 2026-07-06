# Fish Audio S2 / Fish Speech 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：fish.audio / github.com/fishaudio/fish-speech，Fish Audio Research License（研究免费，商用须另签合同）

## 模型理解（前置）

Fish Speech S2 Pro 是 Fish Audio 发布的旗舰开源 TTS 模型（2026 年 3 月），采用 Dual-AR（双自回归）架构：4B 参数 Slow AR 负责语义预测，400M 参数 Fast AR 生成残差声学码本，合计约 5B。在 80+ 语言上训练超 1000 万小时音频，支持自然语言情感/韵律内联控制（`[laugh]`、`[whispers]`）、多说话人切换与语音克隆。官方给出单卡 H200 RTF 0.195、首帧延迟约 100 ms 的生产级流式推理性能，推理引擎基于 SGLang（复用 LLM 原生加速）。**GitHub 仓库 31K+ Stars**，是开源 TTS 中开发者心智最强的项目之一。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 5B 参数双自回归 TTS，支持细粒度情感控制 + 语音克隆，80+ 语言，生产级 SGLang 流式推理 |
| 许可证 | **Fish Audio Research License** — 研究 / 非商业免费；**商业使用须另签协议**（business@fish.audio；自托管企业层 $10k/月）。非 Apache/MIT，**不可直接作主推"商用免费"卖点** |
| 主仓库 / 分发 | GitHub [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)（★31k）；HuggingFace [fishaudio/s2-pro](https://huggingface.co/fishaudio/s2-pro)；商业 API：fish.audio；SGLang-Omni 集成 |
| 参数 / VRAM 可跑性 | 5B（4B Slow AR + 400M Fast AR）；官方推荐**最低 24 GB VRAM**（text-to-semantic 组件需 24 GB，DAC codec 需 4 GB）；消费级 RTX 3090 / 4090 可跑，但 16 GB 及以下显卡受限；**Olares One（若配 24 GB 卡）可运行，8 GB 及 12 GB 卡不足** |
| 变体 / 型号 | S2-Pro（4B，旗舰）；S2.1 Pro（最新 API 版本，有免费层）；S1（前代）；fish-speech 1.5（前代，仍有搜索量） |
| 闭源对标 | **ElevenLabs**（❌ 无对应报告）、**MiniMax Speech**（✅ 均有 Semrush 数据）；亦竞争 OpenAI TTS、Eleven Labs Turbo |
| Olares Market | 未上架（无 Ollama/ComfyUI 路径，推理走 SGLang/Docker；可 Docker 部署，无专属 Market 条目） |
| 来源 | [fish.audio/s2/](https://fish.audio/s2/)、[HuggingFace fishaudio/s2-pro](https://huggingface.co/fishaudio/s2-pro)、[GitHub fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)、[arXiv 2603.08823](https://arxiv.org/abs/2603.08823)、[LICENSE](https://github.com/fishaudio/fish-speech/blob/main/LICENSE) |

---

## 流量基线（Phase 1）

| 指标 | 数据 |
|------|------|
| 域名 | fish.audio |
| SEMrush Rank | 25,637 |
| 月自然流量（US） | 85,068 |
| 关键词数 | 35,445 |
| 流量估值 | ~$26,666/月 |
| 付费关键词 | 795 |
| 付费流量（US） | 25,201 |

### 官网 TOP 关键词（按流量排序，TOP 12）

| 关键词 | 排名 | 月量 | CPC | 流量占比 | URL |
|--------|------|------|-----|----------|-----|
| fish audio | 1 | 22,200 | $0.26 | 6.47% | /tts/ |
| fish.audio | 1 | 4,400 | $0.26 | 4.13% | / |
| fish audio（发现页） | 2 | 22,200 | $0.26 | 3.44% | /discovery/ |
| fish.audio ai | 1 | 1,900 | $0.26 | 1.78% | / |
| caine *(TADC 角色声音)* | 4 | 60,500 | $0.34 | 1.56% | /m/… |
| caine tadc | 8 | 27,100 | — | 0.60% | /m/… |
| little einsteins fish audio | 1 | 1,300 | — | 1.22% | /m/… |
| fish audio（工作室页）| 5 | 22,200 | $0.26 | 1.14% | /studio/ |
| trump voice generator | 3 | 4,400 | — | 0.42% | /m/… |
| fish audio text to speech | 1 | 390 | $0.49 | 0.36% | / |
| fish ai | 3 | 2,900 | $0.18 | 0.27% | /discovery/ |
| fish audio app | 1 | 480 | $0.10 | 0.45% | /tts/ |

> **关键洞见**：fish.audio 流量以**平台品牌词 + 病毒式角色 AI 声音页（Caine TADC、SpongeBob、Trump 等）**为主，"Fish Speech S2 Pro"作为底层技术模型的独立搜索量极小。开发者侧流量（API、TTS 功能页）是次要来源；S2 的模型名认知尚在建立期。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| fish audio | 18,100 | 29 | $0.34 | commercial |
| fish speech | 480 | 50 | $0.89 | info |
| fish audio text to speech | 390 | 40 | $0.49 | info/comm |
| fish-speech 1.5 | 210 | — | — | info |
| fish audio voice cloning ⭐ | 210 | 28 | $1.17 | info/comm |
| fish audio api ⭐ | 90 | 24 | $1.64 | commercial |
| fish audio tts ⭐ | 90 | — | $1.07 | info |
| fish speech v1.5 | 70 | — | $3.61 | info |
| fish audio free ⭐ | 50 | 25 | $0.25 | info |
| fish audio s2 ⭐ | 40 | 0 | $1.08 | info |
| fish speech s2 pro ⭐ | 40 | 0 | $3.36 | commercial |
| fish audio s2 pro ⭐ | ~140 * | 0 | $1.25 | commercial |
| fish audio pricing ⭐ | 70 | 8 | — | comm/trans |
| fish audio review ⭐ | 20 | 0 | $1.94 | info |

> *fish audio s2 pro：phrase_fullsearch 返回 140，trend 近两月爬升至满分，属于 GEO 抢发期*

### 引擎组合词（Olares 机会前哨）

> Fish Speech 不走 Ollama/ComfyUI 路径；官方推理引擎为 **SGLang + Docker**；"引擎词"对应 Docker 部署和 API 集成场景。

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| fish speech api ⭐ | 30 | — | $7.33 | commercial |
| fish speech docker ⭐ | 20 | 0 | — | info |
| fish audio github ⭐ | 50 | 0 | — | info |
| fish speech python ⭐ | ~0 | 0 | — | info |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| local tts ⭐ | 110 | 24 | $4.73 | info |
| self hosted tts ⭐ | 20 | 0 | — | info |
| fish audio free ⭐ | 50 | 25 | $0.25 | info |
| fish speech docker ⭐ | 20 | 0 | — | info |

> 注：fish speech 官方要求 **24 GB VRAM**（text-to-semantic 组件）；消费级仅 RTX 3090/4090 (24 GB) 及以上可全量推理；8-12 GB 卡不适用——自托管故事比轻量 TTS（如 Kokoro 82M 只需 <0.5 GB）受众更小。

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| elevenlabs alternative ⭐ | 480 | 9 | $6.16 | info |
| open source tts | 260 | 32 | $5.48 | info |
| open source voice cloning | 140 | 35 | $2.23 | info |
| minimax tts | 480 | 62 | $2.52 | info |
| fish audio vs elevenlabs ⭐ | 20 | 9 | $4.42 | info |
| fish.audio vs elevenlabs ⭐ | ~590 * | — | — | info |
| voice cloning open source ⭐ | 20 | 0 | $1.33 | info |
| self hosted tts ⭐ | 20 | 0 | — | info |

> *"fish.audio vs elevenlabs"：phrase_fullsearch 返回 590，KD 未单独核，建议作 GEO 抢发候选*

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| elevenlabs alternative | 480 | 9 | $6.16 | Fish Speech S2 Pro = 自托管 ElevenLabs 平替；Olares 一键 Docker 部署，个人研究/非商业免费，数据不出本机 | ⭐⭐⭐ |
| self hosted tts | 20 | 0 | — | "在 Olares 上自托管 TTS 引擎"= 零月费（个人非商业），隐私 100% | ⭐⭐⭐ |
| local tts | 110 | 24 | $4.73 | 消费级可跑（需 24 GB VRAM），Olares 提供声音数据隐私保护，无 API 调用费 | ⭐⭐⭐ |
| fish audio free | 50 | 25 | $0.25 | 研究 License 非商业免费自托管 vs cloud 免费层（每月 8,000 credits / ~7 分钟）→ 自托管无时长限制 | ⭐⭐ |
| fish audio vs elevenlabs | 20 | 9 | $4.42 | "ElevenLabs 收 $300/M chars，fish audio API $15/M chars，自托管非商业 $0"——三档对比，Olares 在第三档 | ⭐⭐⭐ |
| open source voice cloning | 20 | 0 | $1.33 | Fish Speech S2 Pro 语音克隆开源，Olares 部署后声音样本不离开本地设备 | ⭐⭐ |
| fish speech docker | 20 | 0 | — | Olares 通过 Docker 部署即可，无需专属 Market 条目 | ⭐⭐ |
| fish audio api | 90 | 24 | $1.64 | "把 fish.audio API 替换为本地 fish-speech"——开发者自建 Agent 语音栈 | ⭐⭐ |
| fish speech s2 pro | 40 | 0 | $3.36 | 新模型 GEO 前哨：抢占 "how to run fish speech s2 pro locally" 等 AI Overview 引用位 | ⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| fish audio | 18,100 | 29 | $0.34 | comm/nav | 主词候选 | 平台品牌词，量大；但排名在 fish.audio 自身，外站很难靠"fish audio"获 SEO 流量；更适合用于对比文/替代文的 anchor（"fish audio vs X"类） |
| elevenlabs alternative | 480 | 9 | $6.16 | info | **主词候选** | KD 9，量 480，CPC $6.16 高商业价值；"Fish Speech S2 Pro 作为自托管 ElevenLabs 替代"是 Olares 最强进入点 |
| fish speech | 480 | 50 | $0.89 | info | 次级 | 量与 elevenlabs alternative 持平但 KD=50；作为品牌/次级词写进 fish audio 相关文章 |
| open source tts | 260 | 32 | $5.48 | info | 主词候选 | 量 260，KD 32，CPC $5.48；同族词（open source voice cloning/text to speech）合计 ~660；"Olares 运行最佳开源 TTS"叙事入口 |
| fish audio text to speech | 390 | 40 | $0.49 | info/comm | 次级 | 量 390，KD 40 偏难；并入平台对比文 |
| fish audio voice cloning ⭐ | 210 | 28 | $1.17 | info/comm | **主词候选** | KD 28，量 210，隐私叙事佳（克隆声音数据不上云）；可独立成文 |
| minimax tts | 480 | 62 | $2.52 | info | 次级 | 同量同赛道但 KD=62；作为 fish audio 对比文的竞品对象提及 |
| local tts ⭐ | 110 | 24 | $4.73 | info | **主词候选** | KD 24，CPC $4.73，Olares 语音部署契合；注意 24 GB VRAM 门槛需在内容中明确说明 |
| fish audio api ⭐ | 90 | 24 | $1.64 | commercial | 次级 | 开发者词，KD 24；写 API vs 自托管对比文时重要次级 |
| self hosted tts ⭐ | 20 | 0 | — | info | **GEO** | 近零竞争，精准意图，直接命中 Olares 自托管叙事；抢 AI Overview 引用位 |
| fish audio s2 ⭐ | 40 | 0 | $1.08 | info | GEO | S2 版本词，量低但 KD=0；新模型 GEO 前哨，写"fish audio s2 pro how to run"类直答段落 |
| fish speech s2 pro ⭐ | 40 | 0 | $3.36 | commercial | GEO | KD=0，CPC $3.36 高商业；近零量属 GEO 期，但有 CPC 说明商业意图已出现；抢 AI Overview 引用 |
| fish audio pricing ⭐ | 70 | 8 | — | comm/trans | 次级 | KD=8，定价页关键词；写"fish audio vs 自托管成本对比"时作次级 |
| fish audio vs elevenlabs ⭐ | 20 | 9 | $4.42 | info | GEO | KD=9，低竞争对比词；Olares 角度：云 API 成本 vs 本地零成本 |
| voice cloning open source ⭐ | 20 | 0 | $1.33 | info | GEO | 精准意图，KD=0；声音克隆数据隐私=Olares 核心叙事 |

---

## 核心洞见

1. **搜索心智建立了吗？** — "fish audio"品牌词 18K 月量，平台认知强；但这是**平台/App 品牌**，而非底层模型认知。"fish speech"（480 vol）、"fish speech s2 pro"（40 vol）量极低，S2 模型名尚在 GEO 期——类似 fish.audio 自己的 API 流量靠病毒式角色 AI 声音（Caine TADC、SpongeBob 等）带来，不靠技术模型名。外站内容**不要押注"fish speech s2 pro"作独立主词**，而要用"elevenlabs alternative"+"fish audio"的组合。

2. **消费级 GPU / Olares One 能否本地跑？** — **部分可以，门槛偏高**。官方推荐 24 GB VRAM（text-to-semantic 组件），消费级只有 RTX 3090/4090 (24 GB) 满足，8 GB/12 GB 卡不足。若 Olares One 配置 24 GB GPU，可全量运行；但相比 Kokoro（82M，< 0.5 GB VRAM）门槛高出数十倍。叙事需诚实说明硬件要求，不能笼统写"在家可跑"。

3. **许可证是否商用友好？** — **否**。Fish Audio Research License：研究/非商业免费，商业使用须另签协议（自托管企业层公开报价 $10k/月）。这意味着：
   - ✅ Olares 个人/研究用户可以免费自托管
   - ❌ 不能作为"商用免费 AI 语音引擎"主推
   - ✅ **隐私/数据主权角度**仍成立（不发数据到云）
   - 主推叙事应是"个人/研究免费自托管，数据不出本机"，而非"替代 ElevenLabs 的商业方案"

4. **对 Olares 最关键的 2-3 个词：**
   - `elevenlabs alternative`（480 vol, KD 9, CPC $6.16）— 最强进入点，低竞争高商业价值
   - `local tts`（110 vol, KD 24, CPC $4.73）— 精准部署词，Olares 硬件叙事锚点
   - `self hosted tts`（20 vol, KD 0）— 近零竞争 GEO 前哨，直接命中场景

5. **新模型 GEO 抢发窗口：** "fish speech s2 pro"、"fish audio s2 pro"、"fish audio s2"均 KD=0 且趋势近期爬升；"fish.audio vs elevenlabs"约 590 vol、"fish speech s2 vs elevenlabs"近零量但有 CPC——这批词 Semrush 还未有正式排名数据，正是写"Fish Speech S2 Pro 本地部署指南"或"ElevenLabs alternative with Fish Audio S2"类文章切入 AI Overview / Perplexity 的最佳时机。

6. **闭源对标与攻击面：**
   - **ElevenLabs**：API $300/M chars（ElevenLabs Creator 计划），fish.audio API $15/M chars（≈ 20× 便宜）；个人自托管（非商业）$0——三档定价对比是最清晰的攻击面。同时 ElevenLabs 收集语音数据，自托管可避免。
   - **MiniMax Speech**（已有报告）：480 vol 同量级，但 KD 62（难）；MiniMax 以 API 为主，无开源权重；fish speech 在开源/本地部署维度胜出。
   - 攻击角度：① 成本（cloud API 与自托管价格差距）；② 数据隐私（声音克隆样本不上传第三方）；③ 许可灵活性（本地定制 fine-tune 无需许可）。

7. **与 model/models.md 同类关联：**
   - 同报告目录下 Kokoro（82M, Apache 2.0）对比：Kokoro 量更小但 VRAM 超低（0.5 GB）、完全商用免费；Fish Speech S2 Pro 质量更高但需 24 GB VRAM 且商用须付费。两者互补：Kokoro = 低资源高兼容，Fish Speech = 高质量需高端硬件。
   - Piper TTS（1300 vol, KD 25）：极轻量（~100 MB），完全离线，更适合低功耗设备；Fish Speech 在质量/多语言维度领先。
   - 跨方向联动：ElevenLabs 在 commerce/reports 下，如需写 "fish audio vs elevenlabs" 对比文，需引用两侧数据。

---

*数据来源：SEMrush US（domain_rank、resource_organic、phrase_these、phrase_fullsearch、phrase_kdi、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
