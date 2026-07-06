# Qwen3-TTS 模型 SEO 关键词调研报告

> SEMrush US | 2026-07-06 | 来源：QwenLM / github.com/QwenLM/Qwen3-TTS，Apache 2.0
> **无独立官网**——SEO 主战场在第三方内容/文档页（HuggingFace、GitHub、ComfyUI 社区、技术博客）。

## 模型理解（前置）

Qwen3-TTS 是阿里云 Qwen 团队于 2026 年 1 月 22 日发布的开源 TTS 模型系列，提供 0.6B 和 1.7B 两档，Apache 2.0 许可证完全商用友好。核心能力包括 3 秒语音克隆、自由文本驱动的声音设计（VoiceDesign）、9 种预设高质量音色（CustomVoice）以及超低延迟双轨流式合成（首包延迟 97ms）。支持 10 种主流语言（中/英/日/韩/德/法/俄/葡/西/意），在开源 TTS 中与 ElevenLabs、OpenAI TTS 的商业能力对标最为正面。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 0.6B/1.7B 双档开源 TTS，3 秒语音克隆 + 声音设计 + 10 语言，97ms 流式输出 |
| 许可证 | **Apache 2.0**——完全商用友好，可自托管、可集成，无地区限制 |
| 主仓库 / 分发 | GitHub [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)（★12.2k，1,573 forks）；HuggingFace `Qwen/` 系列（1.7B-CustomVoice 月下载 207 万次）；`pip install qwen-tts` |
| 参数 / VRAM 可跑性 | 0.6B：float16 约 2.4 GB VRAM（推荐 8 GB）；1.7B：float16 约 6–8 GB VRAM（推荐 16 GB）；**Olares One（RTX 5090 Mobile 24 GB）：两档均轻松运行，剩余 16–22 GB 可同时跑 LLM 推理** |
| 变体 / 型号 | `12Hz-1.7B-Base`（3 秒克隆 + FT 底座）、`12Hz-1.7B-CustomVoice`、`12Hz-1.7B-VoiceDesign`、`12Hz-0.6B-Base`、`12Hz-0.6B-CustomVoice`；另有 `25Hz` 系列（含 VoiceEditing 变体）；`qwen3-tts-flash`（社区快速推理变体） |
| 闭源对标 | **ElevenLabs**（已有报告）、**OpenAI TTS**（tts-1 / tts-1-hd）；技术报告中明确超越 SeedTTS 语音自然度 |
| Olares Market | vLLM 可作部署引擎（vLLM-Omni 方案，Olares 生态支持）；ComfyUI 节点社区已跟进；Open WebUI 可接 qwen-tts API；无独立 Market 条目 |
| 来源 | [GitHub QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)、[HuggingFace 模型卡](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice)、[技术报告 arXiv:2601.15621](https://arxiv.org/pdf/2601.15621)、[Mintlify 官方文档](https://qwenlm-qwen3-tts.mintlify.app)、[Alibaba Cloud 博客](https://www.alibabacloud.com/blog/qwen3-tts-family-is-now-open-sourced-voice-design-clone-and-generation_602826) |

---

## 关键词扩展（Phase 2）

> 无独立官网，跳过 Phase 1 域名报告，直接从关键词层做起。
> ⭐ = KD < 30 且量 > 0

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| qwen3-tts | 3,600 | 66 | $2.67 | info/nav |
| qwen3-tts github | 2,400 | 63 | — | nav |
| qwen3 tts | 1,900 | 72 | $2.67 | info |
| qwen3-tts-12hz-1.7b-customvoice ⭐ | 1,000 | 0 | — | nav/info |
| qwen3-tts-flash | 320 | 49 | — | info |
| qwen tts | 320 | 57 | $2.33 | info |
| qwen3-tts demo | 260 | 46 | $2.03 | info |
| qwen3-tts-easyfinetuning ⭐ | 210 | 0 | $0.85 | info |
| qwen3 tts demo | 140 | 42 | $2.03 | info |
| qwen3 tts 1.7b ⭐ | 50 | 0 | $3.95 | info |
| faster-qwen3-tts ⭐ | 50 | 0 | — | info |
| qwen3 tts huggingface ⭐ | 70 | 0 | — | nav |
| qwen3 tts model ⭐ | 70 | 0 | — | info |

### 引擎组合词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| qwen3 tts comfyui ⭐ | 90 | 0 | — | info |
| qwen3 tts api ⭐ | 40 | 0 | $2.54 | info |
| comfyui qwen3 tts ⭐ | 40 | 0 | — | info |
| qwen3-tts comfyui ⭐ | 30 | 0 | — | info |
| qwen3-tts webui ⭐ | 30 | 0 | — | info |
| qwen3 tts ollama ⭐ | 30 | 0 | — | info |
| qwen3-tts api ⭐ | 30 | 0 | $4.16 | info |
| qwen3 tts vllm ⭐ | 10 | 0 | — | info |

注：ComfyUI（90+40+30 ≈ 160/mo 合计）是目前最活跃的引擎整合社区，超过 Ollama（30/mo）和 vLLM（10/mo）；vLLM-Omni 是官方推荐自托管生产方案。

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| qwen3-tts voice clone ⭐ | 30 | 0 | $2.92 | info |
| qwen3 tts voice cloning ⭐ | 20 | 0 | $1.67 | info |
| how to run qwen3-tts locally ⭐ | 10 | 0 | — | info |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ai voice cloning free | 1,000 | 59 | $1.14 | info |
| free voice cloning | 1,000 | 56 | $1.39 | info |
| elevenlabs alternative free ⭐ | 590 | 29 | $1.66 | info |
| elevenlabs alternative ⭐ | 480 | 9 | $6.16 | info |
| open source tts ⭐ | 260 | 32 | $5.48 | info |
| free tts api ⭐ | 260 | 28 | $5.80 | info |
| open source text to speech | 260 | 49 | $1.41 | info |
| open source voice cloning ⭐ | 140 | 35 | $2.23 | info |
| best open source tts | 140 | 39 | $5.26 | info |
| local tts ⭐ | 110 | 24 | $4.73 | info |
| open source elevenlabs ⭐ | 30 | 0 | $7.60 | info |
| self hosted tts ⭐ | 20 | 0 | — | info |
| voice cloning open source ⭐ | 20 | 0 | $1.33 | info |

**开源 TTS 市场搜索量参照**（背景）：`kokoro tts`（2,400/mo，KD 64）、`coqui tts`（1,900/mo，KD 39）、`chatterbox tts`（1,300/mo，KD 54）、`piper tts`（1,300/mo，KD 25）、`xtts`（720/mo，KD 35）、`fish speech`（480/mo，KD 50）、`bark tts`（210/mo，KD 27）。`qwen3-tts`（3,600/mo）、`qwen3 tts`（1,900/mo）合计已超过开源 TTS 第一名 Kokoro；**Qwen3-TTS 是 2026 开源 TTS 搜索量最高的模型**。

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 | 契合度 |
|--------|------|----|-----|-------------|--------|
| elevenlabs alternative | 480 | 9 | $6.16 | Qwen3-TTS 自托管在 Olares = ElevenLabs 零费用平替，API 私有化不限额度，数据不离设备 | ⭐⭐⭐ |
| elevenlabs alternative free | 590 | 29 | $1.66 | 同上，量更大；强调"Apache 2.0 + 免费 + 隐私"三重卖点 | ⭐⭐⭐ |
| qwen3 tts comfyui | 90 | 0 | — | ComfyUI 已在 Olares Market；Qwen3-TTS ComfyUI 节点 + Olares 一键跑声音克隆工作流 | ⭐⭐⭐ |
| qwen3 tts api | 40 | 0 | $2.54 | vLLM-Omni 在 Olares 上暴露 OpenAI 兼容 TTS API，Open WebUI / Personal Agent 直接接入 | ⭐⭐⭐ |
| free tts api | 260 | 28 | $5.80 | Olares 自托管 Qwen3-TTS via vLLM = 真正零计费 TTS API，无 token 限额墙 | ⭐⭐⭐ |
| open source tts | 260 | 32 | $5.48 | Apache 2.0；Qwen3-TTS 是 2026 年开源 TTS 搜索量第一，Olares 一键跑 | ⭐⭐ |
| open source voice cloning | 140 | 35 | $2.23 | 3 秒语音克隆完全本地；Personal Agent 场景声纹不上传云端 | ⭐⭐ |
| local tts | 110 | 24 | $4.73 | 离线语音合成；Olares One 24 GB 同时跑 LLM + Qwen3-TTS，零延迟个人语音助手 | ⭐⭐ |
| qwen3-tts voice clone | 30 | 0 | $2.92 | 3 秒克隆任意声音 + Olares 本地运行 = 完全私有的声纹资产，不上传任何云服务 | ⭐⭐ |
| self hosted tts | 20 | 0 | — | GEO 前哨：Olares 最具体的自托管 TTS 场景，vLLM-Omni 部署指南最精准 | ⭐⭐ |
| open source elevenlabs | 30 | 0 | $7.60 | CPC $7.60 全表最高，GEO 高价值词；Qwen3-TTS = "开源 ElevenLabs"最直接答案 | ⭐⭐⭐ |

---

## Top 关键词（含角色判断）

报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| elevenlabs alternative free | 590 | 29 | $1.66 | info | **主词候选** | 高量 + KD 29 + 商业意图；Qwen3-TTS 在 Olares 自托管是最强 ElevenLabs 免费开源平替 |
| elevenlabs alternative | 480 | 9 | $6.16 | info | **主词候选** | KD 仅 9、CPC $6.16 全表最强机会；开源语音克隆攻击线清晰 |
| open source tts | 260 | 32 | $5.48 | info | **主词候选** | 类目词 + CPC 高；Qwen3-TTS 是 2026 开源 TTS 第一品牌，Olares 主推 |
| free tts api | 260 | 28 | $5.80 | info | **主词候选** | CPC 高反映商业意图；Olares 自托管 = 真正零成本 TTS API，无额度限制 |
| open source voice cloning | 140 | 35 | $2.23 | info | **主词候选** | 3 秒克隆定位与关键词精准匹配；竞争可接受，Olares 离线克隆叙事成立 |
| open source elevenlabs | 30 | 0 | $7.60 | info | **主词候选** | CPC $7.60 最高 + KD 0 + 精准语义；虽量小但战略意图极强，Olares GEO/低 KD 文章机会 |
| qwen3-tts | 3,600 | 66 | $2.67 | info/nav | **次级** | 品牌主词量大但 KD 66，暂作流量捕获次级；已有大量外部资源竞争 |
| qwen3-tts-12hz-1.7b-customvoice | 1,000 | 0 | — | nav/info | **次级** | 月量 1,000 且 KD 0——型号精确搜索；用作技术文档/部署指南的精准长尾次级词 |
| qwen3 tts | 1,900 | 72 | $2.67 | info | **次级** | 高量但 KD 72；作次级在 "open source tts" 等主词文章中夹带覆盖 |
| qwen3 tts comfyui | 90 | 0 | — | info | **次级** | KD 0 + ComfyUI 生态合计 ~160/mo；Olares Market ComfyUI 部署 Qwen3-TTS 的精准词 |
| qwen3 tts api | 40 | 0 | $2.54 | info | **次级** | CPC $2.54 + KD 0；vLLM-Omni 在 Olares 暴露 TTS API 的技术文核心词 |
| local tts | 110 | 24 | $4.73 | info | **次级** | 低 KD + 高 CPC；并入 elevenlabs alternative 文章或 "best local tts" 簇 |
| qwen3-tts voice clone | 30 | 0 | $2.92 | info | **GEO** | 精准场景词 + KD 0；FAQ 块写"本地 3 秒克隆"抢 AI Overview 引用位 |
| self hosted tts | 20 | 0 | — | info | **GEO** | 最精准的自托管语义 + 零竞争；Olares vLLM-Omni 部署方案的完美 GEO 词 |
| voice cloning open source | 20 | 0 | $1.33 | info | **GEO** | 语义精准 + KD 0；抢"开源语音克隆"直答块 |
| how to run qwen3-tts locally | 10 | 0 | — | info | **GEO** | 精准问句 + 零竞争；写 step-by-step Olares 部署指南抢 PAA / Perplexity 引用位 |
| open source elevenlabs alternative | 20 | 0 | $1.61 | info | **GEO** | 复合语义词 + KD 0；FAQ/直答块植入 |

---

## 核心洞见

**1. 搜索心智已建立，2026 开源 TTS 搜索量第一**

`qwen3-tts`（3,600/mo）+ `qwen3 tts`（1,900/mo）合计月量已超 5,000，**大幅超越 Kokoro（2,400/mo）、Coqui TTS（1,900/mo）、Chatterbox（1,300/mo）**，成为 2026 年开源 TTS 搜索量最高的模型。另有 `qwen3-tts github`（2,400/mo，导航词）印证真实流量。品牌词 KD（66–72）偏高，内容机会指向"本地部署 + 对比 ElevenLabs"方向——KD 更低、意图更精准、CPC 更高。

**2. 消费级 GPU / Olares One 完全可跑，叙事前提完全成立**

- 0.6B（float16 约 2.4 GB VRAM）：RTX 3060（12 GB）即可流畅运行，CPU 亦可
- 1.7B（float16 约 6–8 GB VRAM）：RTX 3080（10 GB）以上即可，RTX 3090/4090（24 GB）为最优
- **Olares One（RTX 5090 Mobile 24 GB）**：两档均轻松运行；0.6B 运行时剩余 ~21 GB，可与 70B 量化 LLM 同卡运行，形成完整"LLM 推理 + TTS 语音合成"本地 Personal Agent 语音栈

**3. Apache 2.0 许可证，可作主推卖点**

完全商用友好，无地区限制，可嵌入商业产品、API 服务、Personal Agent。与 ElevenLabs 云端授权（按字符计费、不可自托管）形成鲜明对比，主推卖点："Apache 2.0 = 拥有你的 TTS 引擎，3 秒克隆你的声音，数据永不上云"。

**4. 对 Olares 最关键的 3 个词**

- `elevenlabs alternative`（480/mo，KD 9，CPC $6.16）：KD 极低 + 高商业价值，Qwen3-TTS 自托管是最直接答案，与 Kokoro 同一攻击线可复用内容
- `free tts api`（260/mo，KD 28，CPC $5.80）：Olares 自托管 Qwen3-TTS via vLLM = 零成本 TTS API，无额度墙的差异化叙事
- `qwen3 tts comfyui`（约 160/mo 合计，KD 0）：ComfyUI 已在 Olares Market；这是 Olares 最低摩擦的声音克隆工作流部署场景

**5. GEO 抢发窗口**

以下词近零量 + 零竞争，适合写 FAQ / 直答块抢 AI Overview / Perplexity 引用位：
- `open source elevenlabs`（KD 0，CPC $7.60）——价值最高的 GEO 词
- `qwen3-tts voice clone`（KD 0，CPC $2.92）——精准场景词
- `how to run qwen3-tts locally`（KD 0）——Olares 部署 step-by-step 直接答案
- `self hosted tts`（KD 0）——Olares 整体生态叙事锚点
- `voice cloning open source`（KD 0，CPC $1.33）——横向类目词 GEO 占位

**6. 闭源对标与攻击面**

主对标：**ElevenLabs**（已有报告）和 **OpenAI TTS**（tts-1-hd $30/M chars）。攻击面三点：
- **价格**：ElevenLabs $0.30/1,000 chars、OpenAI TTS $30/M chars；自托管 Qwen3-TTS 硬件成本近零
- **额度墙**：ElevenLabs Free Tier 每月 10,000 字符限额，Starter $5/月；Olares 自托管无上限
- **隐私与声纹主权**：ElevenLabs / OpenAI TTS 语音数据与克隆声纹上云；Qwen3-TTS 本地运行，声纹不离设备——尤其对 Personal Agent、创作者、企业应用是决定性差异

次对标：SeedTTS（闭源）、Coqui TTS（已停止维护）、Fish Speech（Apache 2.0 竞品）。

**7. 与 model/models.md 同类 family 的关联**

- 同章（05-tts）已有 Kokoro（2,400/mo）、Piper（1,300/mo）、CosyVoice、Chatterbox 报告；Qwen3-TTS 品牌词合计量远超 Kokoro，但 ElevenLabs alternative 等对比词与 Kokoro 完全重叠——适合合并进同一内容簇
- `elevenlabs alternative`（KD 9）是 TTS 章最优机会词，Qwen3-TTS + Kokoro 双答案同撑一篇文章效果最佳
- `open source tts` 类目词可用 Qwen3-TTS 作 2026 主角（搜索量第一），同时覆盖 Kokoro/Piper/Fish Speech

---

*数据来源：SEMrush US（phrase_these × 3、phrase_fullsearch、phrase_questions）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3–5 倍。*
