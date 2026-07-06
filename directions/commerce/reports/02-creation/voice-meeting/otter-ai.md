# Otter.ai SEO 竞品分析报告

> 域名：otter.ai | SEMrush us | 2026-07-07
> Otter.ai = AI 会议记录/转写/摘要的品类开创者（"AI meeting assistant" 鼻祖），正升级为面向企业的"对话知识引擎（Conversational Knowledge Engine）"。

---

## 项目理解（前置）

Otter.ai 是最早把"AI 会议助手（AI meeting assistant / notetaker）"做成品类的公司：机器人自动加入 Zoom / Google Meet / Teams 会议，实时转写、生成摘要与 action items，并支持跨会议的 AI Chat 检索。2026 年 4 月它对外宣布从"AI 记录工具"升级为"对话知识引擎"，新增 AI Chat（私有、上下文感知）、Otter for Desktop（Mac/Windows，捕捉任意应用里的对话）与扩展的 MCP server。核心卖点是**实时联网转写 + 深度会议生态集成 + 企业级知识检索**——这也决定了它的护城河与软肋：**所有会议内容都要上传到 Otter 云端**。

| 项目 | 内容 |
|------|------|
| 一句话定位 | AI 会议记录/转写/摘要助手，正转型为企业对话知识引擎 |
| 开源 / 许可证 | 闭源 SaaS |
| 主仓库 | 无（闭源；提供 Public API + webhooks + MCP server）|
| 核心功能 | 实时会议转写、AI 摘要/action items、AI Chat 跨会议检索、Zoom/Meet/Teams 集成、Otter for Desktop |
| 商业模式 / 定价 | Freemium SaaS：Basic 免费（300 分钟/月）、Pro $16.99/月（年付 $8.33）、Business $30/月（年付 $19.99）、Enterprise 定制（SSO/SCIM、API、MCP）|
| 差异化 / 价值主张 | 品类先发心智 + 实时联网转写 + Zoom/Teams 深度集成 + 3500 万用户企业知识引擎叙事 |
| 主要竞品（初判）| Fireflies.ai、Fathom、Read.ai、Notta、Granola、tl;dv、MeetGeek |
| Olares Market | 平替**均已上架**：Whisper-WebUI / Whisper API（本地转写）、Open Notebook（开源 NotebookLM 式笔记/研究）|
| 来源 | otter.ai/pricing、otter.ai/enterprise、otter.ai/blog（2026-04-28）、help.otter.ai/Public-API；平替：github.com/lfnovo/open-notebook、Olares market/apps.md |

**Olares 平替方案：** Whisper（Whisper-WebUI / Whisper API on Olares，本地 ASR 转写）+ Open Notebook（自托管开源 NotebookLM 替代，多模型/本地 Ollama、生成笔记与播客）。定位：**会后录音本地转写 + 私有会议笔记，全程不上云**。

---

## 流量基线（Phase 1）

### 概览

| 指标 | 数据 |
|------|------|
| 域名 | otter.ai |
| SEMrush Rank | **10,441**（全球前 1.1 万，SEO 极成熟）|
| 自然关键词数 | 19,317 |
| 月自然流量（US）| **218,776** |
| 自然流量估值 | **$258,596/月** |
| 付费关键词数 | 2,167 |
| 月付费流量 | 61,268 |
| 付费流量估值 | $76,902/月 |
| 排名 1-3 位 | 1,066 词 |
| 排名 4-10 位 | 1,790 词 |
| 排名 11-20 位 | 2,100 词 |

### 子域名流量分布

| 子域名 | 关键词数 | 流量 | 占比 |
|--------|---------|------|------|
| otter.ai（主站）| 15,130 | 215,240 | 98.38% |
| help.otter.ai | 2,856 | 2,801 | 1.28% |
| status.otter.ai | 79 | 392 | 0.18% |
| get.otter.ai（程序化落地页）| 1,230 | 341 | 0.16% |
| go.otter.ai | 22 | 2 | 0% |

> `get.otter.ai` 关键词多（1,230）但流量低（341）——是它的**程序化 use-case 落地页矩阵**（`/meeting-notes/`、`/interview-transcription/` 等），主要靠付费买词导流，非自然排名主力。

### 官网 TOP 自然关键词（全量，按流量排序）

| 关键词 | 排名 | 月量 | KD | CPC | 流量 | 意图 | URL |
|--------|------|------|----|----|------|------|-----|
| otter ai | 1 | 135,000 | 83 | $0.95 | 108,000 | 导航 | / |
| otter | 1 | 201,000 | 73 | $0.59 | 16,482 | 信息 | / |
| otterai | 1 | 18,100 | 76 | $0.95 | 14,480 | 导航 | / |
| otter.ai | 1 | 12,100 | 80 | $0.95 | 9,680 | 导航 | / |
| otter ai login | 1 | 5,400 | 73 | $0.65 | 4,320 | 导航 | /signin |
| otter ai video transcription | 1 | 2,400 | 68 | $2.47 | 1,920 | 信息 | /transcription |
| ottr.ai（误拼）| 1 | 1,900 | 82 | $0.95 | 1,520 | 导航 | / |
| otter.ai login | 1 | 4,400 | 67 | $0.65 | 1,091 | 导航 | /signin |
| otter ai audio to text | 1 | 1,000 | 69 | $2.29 | 800 | 导航 | /audio-to-text |
| otter.ai transcription | 1 | 1,000 | 79 | $2.88 | 800 | 导航 | / |
| otter ai log in | 1 | 1,000 | 68 | $0.04 | 800 | 导航 | /signin |
| **otter ai podcast transcript** | 1 | 1,000 | **0** | $1.51 | 800 | 信息 | /podcast-transcription |
| otter ai note taker | 1 | 880 | 77 | $2.87 | 704 | 导航 | / |
| otter ai transcription software | 1 | 880 | 78 | $0.00 | 704 | 商业 | / |
| otto ai（误拼）| 1 | 2,400 | 45 | $2.96 | 595 | 信息 | / |
| otterpilot | 1 | 720 | 55 | $0.73 | 576 | 导航 | / |
| oter（误拼）| 1 | 3,600 | 33 | $1.81 | 475 | 信息 | / |
| otter ai meeting transcription | 1 | 590 | 81 | $2.36 | 472 | 导航 | / |
| otter ai podcast transcription | 1 | 590 | 37 | $0.00 | 472 | 导航 | /podcast-transcription |
| otter ai voice to text | 1 | 590 | 68 | $1.87 | 472 | 导航 | / |
| otter login | 1 | 1,600 | 26 | $0.03 | 396 | 导航 | /signin |
| otter pricing | 1 | 480 | 43 | $2.04 | 384 | 商业 | /pricing |
| otter ai meeting notes | 1 | 480 | 79 | $3.32 | 384 | 导航 | / |
| otter.ai logo | 1 | 480 | 44 | $0.00 | 384 | 信息 | / |
| outter（误拼）| 1 | 2,400 | 24 | $1.19 | 316 | 信息 | / |
| otter ai careers | 1 | 390 | 20 | $0.77 | 312 | 招聘 | /careers |
| otter.ai free trial | 1 | 390 | 60 | $6.46 | 312 | 商业 | /start-for-free |
| otter ai pro plan | 1 | 390 | 39 | $1.65 | 312 | 商业 | /pricing |
| otter ai free | 1 | 390 | 71 | $2.46 | 312 | 商业 | /start-for-free |
| otter ai speech to text | 1 | 320 | 69 | $1.71 | 256 | 信息 | /speech-to-text |
| ai notetaker | 2 | 2,900 | 61 | $5.28 | 237 | 商业 | / |

> 大量长尾为**品牌误拼变体**（ottr / ottor / ottter / outter / o_t_ter_ / otter.ia / ottar ai …），几乎全部霸榜第 1——与 Lovable 同型，流量主要靠**品牌心智**，非通用词。

### 付费词（Google Ads，按流量排序）

Otter 买词以**品牌词自我防御 + 转写/笔记品类大词**为主，导向主站与 `get.otter.ai` 的程序化 use-case 落地页：

| 关键词 | 排名 | 月量 | CPC | 落地页 |
|--------|------|------|-----|--------|
| otter / otter ai | 1-4 | 201,000 / 135,000 | $0.43–0.95 | / |
| notes app | 2 | 49,500 | $1.00 | /blog/best-note-taking-tools |
| transcription | 2 | 33,100 | $1.95 | get.otter.ai/interview-transcription/ |
| speech to text | 2 | 27,100 | $1.39 | /audio-to-text |
| transcribe | 2 | 22,200 | $1.75 | get.otter.ai/interview-transcription/ |
| voice to text | 1 | 18,100 | $1.58 | /speech-to-text |
| audio to text transcription | 1 | 14,800 | $2.23 | /audio-to-text |
| audio transcription | 1 | 12,100 | $1.88 | get.otter.ai/meeting-notes/ |
| google docs voice typing | 1 | 9,900 | $1.66 | get.otter.ai/interview-transcription/ |
| transcribe video to text | 1 | 9,900 | $1.83 | get.otter.ai/meeting-notes/ |
| transcript for youtube videos | 1 | 9,900 | $0.78 | /youtube-transcript-generator |
| video transcript generator | 1 | 8,100 | $1.35 | /video-to-text |
| note taking | 1 | 8,100 | $3.23 | get.otter.ai/meeting-notes/ |
| transcribe audio to text free | 1 | 6,600 | $2.33 | /audio-to-text |

> 打法与 Lovable 一致：**买品类超级大词（transcription / speech to text / voice to text / notes app）→ 导向程序化 use-case 落地页**（`get.otter.ai/meeting-notes`、`/interview-transcription`、`/video-to-text`、`/youtube-transcript-generator`）。这是可复制的模式。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| granola alternative | 210 | **12** | $1.39 | 信息 | ⭐ 新兴竞品替代词，KD 极低 |
| otter ai alternatives | 390 | 28 | $3.70 | 信息 | ⭐ |
| otter ai vs fireflies | 140 | **19** | $4.49 | 信息 | ⭐ |
| fireflies vs otter | 140 | 20 | $5.33 | 信息 | |
| otter ai alternative | 110 | **23** | $3.71 | 信息 | ⭐ |
| otter ai competitors | 110 | **19** | $3.98 | 信息 | ⭐ |
| otter vs fireflies | 90 | 22 | $3.77 | 信息 | |
| fathom vs fireflies | 90 | **10** | $6.94 | 信息 | ⭐ KD=10 |
| fireflies vs fathom | 70 | **18** | $3.70 | 信息 | ⭐ |
| fathom vs otter | 70 | **15** | $4.81 | 信息 | ⭐ |
| fireflies alternative | 50 | **6** | $9.26 | 商业 | ⭐ **KD=6 + CPC $9.26** |
| otter vs fathom | 50 | **15** | $4.55 | 信息 | ⭐ |
| otter ai vs granola | 30 | 0 | $2.10 | 信息 | ⭐ |
| otter alternative | 20 | 0 | $3.62 | 信息 | ⭐ |
| otter ai vs read ai | 20 | 0 | $3.57 | 信息 | ⭐ |
| otter vs notta | 20 | 0 | $0.00 | 信息 | ⭐ |
| otter ai vs fathom | 10 | **16** | $4.28 | 信息 | ⭐ |
| fathom alternative | 10 | 0 | $9.66 | 信息 | ⭐ 高 CPC |
| notta alternative | 10 | 0 | $4.75 | 信息 | ⭐ |
| read ai alternative | 0 | 0 | $4.93 | — | GEO |

> 竞品域名（SEMrush `domain_organic_organic`）确认核心对手：**notta.ai（相关度 0.17）、meetjamie.ai（0.24）、read.ai（0.15）、happyscribe.com（0.07）、uniscribe.co（0.15）**；Fireflies / Fathom / Granola 亦为强对比对象。

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| ai note taker | 18,100 | 73 | $4.38 | 商业 | 品类第一大词 |
| speech to text | 22,200 | 82 | $1.38 | 信息 | |
| voice to text | 18,100 | 80 | $1.58 | 信息 | |
| transcribe audio to text | 18,100 | 52 | $2.36 | 信息 | |
| audio to text | 12,100 | 50 | $1.38 | 信息 | |
| video transcription | 9,900 | 74 | $1.07 | 信息 | |
| transcribe audio | 6,600 | **37** | $1.63 | 信息 | 中等 KD |
| ai transcription | 5,400 | 64 | $3.36 | 信息 | |
| ai meeting note taker | 4,400 | 71 | $6.02 | 信息 | 高 CPC |
| ai notes | 3,600 | 54 | $2.34 | 信息 | |
| transcription software | 2,900 | 70 | $3.56 | 商业 | |
| ai notetaker | 2,900 | 64 | $4.86 | 信息 | |
| ai meeting assistant | 2,400 | 76 | $6.00 | 商业 | 高 CPC |
| transcription service | 2,400 | 88 | $8.04 | 商业 | 最高 CPC |
| free transcription | 2,400 | 64 | $2.98 | 信息 | |
| zoom transcription | 1,900 | 41 | $3.48 | 信息 | |
| ai meeting notes | 1,600 | 73 | $4.74 | 信息 | Otter 核心词 |
| best ai note taker | 1,300 | 70 | $3.55 | 商业 | |
| ai meeting minutes | 1,000 | 70 | $5.18 | 信息 | |
| meeting notes ai | 880 | 70 | $5.54 | 信息 | |
| meeting recorder | 720 | **19** | $4.59 | 信息 | ⭐ |
| meeting notes app | 590 | 76 | $3.86 | 信息 | |
| meeting transcription | 590 | 85 | $4.82 | 信息 | |
| podcast transcription | 480 | **19** | $1.93 | 商业 | ⭐ |
| transcribe podcast | 480 | **30** | $1.62 | 信息 | ⭐ |
| best ai meeting assistant | 210 | **34** | $5.80 | 商业 | 借力清单 |
| ai meeting notes free | 210 | 53 | $3.78 | 商业 | |
| transcribe interview | 110 | **20** | $2.99 | 信息 | ⭐ |

### 产品 / 功能词（otter 前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| otter ai video transcription | 1,900 | 63 | $2.58 | 信息 | |
| otter ai pricing | 1,900 | 41 | $1.32 | 商业 | 定价词 |
| otter ai audio to text | 1,000 | 69 | $2.29 | 导航 | |
| otter ai transcription software | 880 | 78 | $0.00 | 商业 | |
| otter ai review | 590 | **36** | $2.01 | 信息 | ⭐ 评测切入 |
| is otter ai free | 590 | 72 | $1.76 | 信息 | 定价痛点 |
| otter pricing | 480 | 43 | $2.04 | 商业 | |
| otter ai app | 480 | 58 | $2.10 | 信息 | |
| otter ai note taker | 480 | 77 | $2.09 | 导航 | |
| otter ai meeting notes | 390 | 73 | $2.46 | 商业 | |
| otter ai free | 390 | 70 | $2.28 | 商业 | |
| otter ai plans | 320 | 42 | $1.13 | 商业 | |
| otter ai voice to text | 320 | 66 | $3.12 | 导航 | |
| otter ai cost | 320 | **37** | $1.63 | 信息 | ⭐ |
| otter ai download | 260 | 63 | $1.80 | 信息 | |
| otter ai chrome extension | 210 | **29** | $1.10 | 信息 | ⭐ |
| how much is otter ai | 210 | **36** | $1.22 | 信息 | ⭐ |
| otter ai zoom | 140 | **38** | $2.65 | 导航 | ⭐ |
| otter ai api | 110 | **32** | $8.02 | 信息 | ⭐ 高 CPC |
| otter ai extension | 110 | **32** | $3.45 | 信息 | ⭐ |
| otter ai teams | 70 | **26** | $1.41 | 信息 | ⭐ |
| otter ai security | 70 | **39** | $9.02 | 信息 | ⭐ 高 CPC 隐私词 |
| otter ai privacy | 70 | **39** | $0.00 | 信息 | ⭐ 隐私攻击面 |
| otter ai mcp | 30 | 0 | $0.00 | 信息 | ⭐ 新兴 |

**问题词（信息意图内容选题，`phrase_questions`）——多为退订/隐私/合规痛点：**

| 关键词 | 月量 | KD | CPC | 备注 |
|--------|------|----|----|------|
| what is otter ai | 2,400 | 72 | $1.69 | 认知大词 |
| how do i turn off otter ai | 1,300 | **28** | $0.00 | ⭐ 流失信号 |
| how to cancel otter ai subscription | 210 | **22** | $2.11 | ⭐ 流失信号 |
| how does otter ai work | 210 | 44 | $0.92 | |
| how much does otter ai cost | 140 | **35** | $1.63 | ⭐ 定价 |
| is otter ai safe | 140 | **30** | $0.00 | ⭐ 隐私攻击面 |
| is otter ai hipaa compliant | 110 | **28** | $8.01 | ⭐ 合规 + CPC $8 |
| how to stop otter ai from joining meetings | 110 | **28** | $0.00 | ⭐ 隐私反感 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|----|------|------|
| whisper | 49,500 | 86 | $1.32 | 信息 | 本地 ASR 引擎大词（难打）|
| whisper ai | 9,900 | 81 | $1.90 | 信息 | |
| openai whisper | 6,600 | 97 | $2.56 | 导航 | |
| whisperx | 2,400 | **28** | $2.82 | 信息 | ⭐ Whisper-API 底座 |
| open notebook | 1,900 | 67 | $2.00 | 信息 | 平替本体品牌词 |
| whisper transcription | 1,900 | 82 | $2.70 | 信息 | |
| faster whisper | 1,600 | **33** | $2.80 | 信息 | ⭐ |
| notebooklm alternative | 320 | **7** | $0.00 | 信息 | ⭐ **KD=7！** Open Notebook 正位 |
| open source speech to text | 210 | **35** | $2.38 | 信息 | ⭐ |
| whisper webui | 170 | **44** | $2.37 | 信息 | Olares 已上架应用词 |
| whisper local | 140 | **42** | $2.08 | 信息 | |
| open source notebooklm | 110 | **39** | $0.00 | 信息 | ⭐ Open Notebook 正位 |
| self hosted notebooklm | 30 | 0 | $0.00 | 新兴 | ⭐ GEO |
| open source voice to text | 30 | 0 | $2.57 | 新兴 | ⭐ |
| whisper self hosted | 30 | 0 | $1.95 | 新兴 | ⭐ |
| open source meeting transcription | 20 | 0 | $2.12 | 新兴 | ⭐ 空白 |
| self hosted transcription | 20 | 0 | $3.50 | 新兴 | ⭐ 空白 |
| open source transcription | 20 | 0 | $2.30 | 新兴 | ⭐ 空白 |
| open source ai meeting notes | 20 | 0 | $2.01 | 新兴 | ⭐ 空白 |
| whisper vs otter | 20 | 0 | $0.00 | 新兴 | ⭐ 直连对比 |
| open source ai transcription | 20 | 0 | $2.17 | 新兴 | ⭐ 空白 |
| self hosted speech to text | 20 | 0 | $0.00 | 新兴 | ⭐ |
| local ai meeting notes | 30 | 0 | $2.75 | 新兴 | ⭐ 完美契合 |

---

## Olares 关联词（Phase 3）

按月量降序。**核心逻辑：Otter 是闭源 SaaS，所有会议音频必须上传云端且按订阅计费；Olares 平替 = Whisper（Whisper-WebUI / Whisper API，本地 ASR）+ Open Notebook（开源 NotebookLM，本地 Ollama 生成摘要），主打"会后录音本地转写 + 私有会议笔记，全程不上云、零订阅、数据归你"。两款平替均已在 Olares Market。诚实边界：本地 Whisper 不做实时会中转写，面向"事后上传录音转录"。**

### Whisper 本地转写（Olares Market 已上架：Whisper-WebUI / Whisper API）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| transcribe audio | 6,600 | 37 | $1.63 | ⭐⭐ 中等 KD 品类词，本地 Whisper on Olares 转录音频 |
| whisperx | 2,400 | 28 | $2.82 | ⭐⭐ Whisper API 底座引擎，"WhisperX self-hosted" 教程 |
| faster whisper | 1,600 | 33 | $2.80 | ⭐⭐ 本地高速转写引擎，Olares 一键部署 |
| zoom transcription | 1,900 | 41 | $3.48 | ⭐ 会后下载 Zoom 录音 → Whisper on Olares 本地转写 |
| meeting recorder | 720 | 19 | $4.59 | ⭐⭐ 低 KD，"本地会议录音 + 转写"方案 |
| otter ai podcast transcript | 1,000 | **0** | $1.51 | ⭐⭐⭐ KD=0！"播客本地转录"教程，Whisper on Olares |
| podcast transcription | 480 | 19 | $1.93 | ⭐⭐ 低 KD，播客主是本地转写高价值人群 |
| transcribe podcast | 480 | 30 | $1.62 | ⭐⭐ 同上 |
| transcribe interview | 110 | 20 | $2.99 | ⭐⭐ 访谈本地转写，隐私敏感场景 |
| open source speech to text | 210 | 35 | $2.38 | ⭐⭐ Whisper = 开源 STT 首选，Olares 部署 |
| whisper webui | 170 | 44 | $2.37 | ⭐ Olares 已上架应用词，直接做安装/教程页 |
| whisper vs otter | 20 | 0 | — | ⭐⭐⭐ 直连对比，"本地 Whisper vs 云端 Otter" |

### Open Notebook 私有会议笔记（Olares Market 已上架：开源 NotebookLM 替代）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| notebooklm alternative | 320 | **7** | $0.00 | ⭐⭐⭐ KD=7！Open Notebook = 自托管 NotebookLM，Olares 一键部署 |
| open source notebooklm | 110 | 39 | $0.00 | ⭐⭐⭐ Open Notebook 正位词 |
| open notebook | 1,900 | 67 | $2.00 | ⭐⭐ 平替本体品牌词，"Open Notebook on Olares 安装" |
| self hosted notebooklm | 30 | 0 | $0.00 | ⭐⭐⭐ GEO 完美契合 |
| local ai meeting notes | 30 | 0 | $2.75 | ⭐⭐⭐ Whisper + Open Notebook 组合正位 |
| open source ai meeting notes | 20 | 0 | $2.01 | ⭐⭐⭐ 空白词，组合方案正位 |

### 替代/对比词 + 隐私攻击面（Olares 差异化最锋利处）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|----|-----------|
| fireflies alternative | 50 | **6** | $9.26 | ⭐⭐⭐ 全报告最低 KD 之一 + CPC $9.26，"Fireflies 自托管替代：本地 Whisper" |
| otter ai alternatives | 390 | 28 | $3.70 | ⭐⭐ "Otter AI 替代方案：本地会议转写"，加 Olares 自托管选项 |
| otter ai vs fireflies | 140 | 19 | $4.49 | ⭐⭐ 对比文加第三选项：Otter vs Fireflies vs 本地 Whisper on Olares |
| otter ai competitors | 110 | 19 | $3.98 | ⭐⭐ 竞品清单页加"开源自托管"分组 |
| otter ai alternative | 110 | 23 | $3.71 | ⭐⭐ Whisper + Open Notebook on Olares 完全私有零订阅 |
| granola alternative | 210 | 12 | $1.39 | ⭐⭐ KD=12，新兴竞品替代，本地方案切入 |
| fathom vs otter / otter vs fathom | 70 / 50 | 15 | $4.81 | ⭐ 多方对比矩阵加本地选项 |
| is otter ai hipaa compliant | 110 | 28 | $8.01 | ⭐⭐ 合规痛点，本地转写 = 数据不出设备，天然满足隐私诉求 |
| is otter ai safe | 140 | 30 | $0.00 | ⭐⭐ "担心 Otter 安全？本地转写彻底私有" |
| how to stop otter ai from joining meetings | 110 | 28 | $0.00 | ⭐ 隐私反感人群，导向"自己掌控的会议转写" |
| how to cancel otter ai subscription | 210 | 22 | $2.11 | ⭐ 流失人群，导向零订阅本地方案 |

---

## Top 关键词（含角色判断）

> 报告只对词下判断（角色）；聚成文章簇（可跨报告）在 seo-content 阶段做，见 [reference/keyword-selection-standard.md](/Users/pengpeng/seo/reference/keyword-selection-standard.md)。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|----|------|------|--------------------------|
| transcribe audio | 6,600 | 37 | $1.63 | info | 主词候选 | 中等 KD 品类词，本地 Whisper on Olares 音频转写，可正面打 |
| whisperx | 2,400 | 28 | $2.82 | info | 主词候选 | Whisper-API 底座引擎，"WhisperX self-hosted on Olares" 教程 |
| faster whisper | 1,600 | 33 | $2.80 | info | 主词候选 | 本地高速转写引擎，Olares 一键部署 |
| open notebook | 1,900 | 67 | $2.00 | info | 主词候选 | 平替本体品牌词，"Open Notebook on Olares 安装/用法" |
| otter ai pricing | 1,900 | 41 | $1.32 | comm | 主词候选 | Otter $16.99/月 vs 本地 Whisper+Open Notebook on Olares 零月费 |
| otter ai video transcription | 1,900 | 63 | — | info | 次级 | 视频转录词，事后上传录音转写覆盖 |
| ai meeting notes | 1,600 | 73 | $4.74 | info | 次级 | KD 高不硬拼，走"本地/私有会议笔记"差异化，Whisper+Open Notebook |
| otter ai podcast transcript | 1,000 | **0** | $1.51 | info | 主词候选 | KD=0！Whisper on Olares 播客本地转录教程 |
| meeting recorder | 720 | 19 | $4.59 | info | 主词候选 | 低 KD，本地会议录音+转写方案 |
| otter ai review | 590 | 36 | $2.01 | info | 主词候选 | 评测切入，诚实对比后导向本地私有替代 |
| podcast transcription | 480 | 19 | $1.93 | comm | 次级 | 低 KD，播客主本地转写高价值人群 |
| otter ai alternatives | 390 | 28 | $3.70 | info | 主词候选 | "Otter AI 替代方案"清单，加 Olares 自托管选项 |
| notebooklm alternative | 320 | **7** | $0.00 | info | 主词候选 | KD=7！Open Notebook = 自托管 NotebookLM，Olares 一键部署 |
| granola alternative | 210 | 12 | $1.39 | info | 次级 | KD=12 新兴竞品替代，本地方案切入 |
| open source speech to text | 210 | 35 | $2.38 | info | 次级 | Whisper=开源 STT 首选，Olares 部署 |
| otter ai vs fireflies | 140 | 19 | $4.49 | info | 主词候选 | 对比加第三选项：Otter vs Fireflies vs 本地 Whisper on Olares |
| is otter ai hipaa compliant | 110 | 28 | $8.01 | info | 次级 | 合规痛点 CPC $8，本地转写数据不出设备 |
| otter ai competitors | 110 | 19 | $3.98 | comm | 次级 | 竞品清单页加"开源自托管"分组 |
| otter ai alternative | 110 | 23 | $3.71 | info | 主词候选 | Whisper+Open Notebook on Olares 完全私有零订阅 |
| open source notebooklm | 110 | 39 | $0.00 | info | 次级 | Open Notebook 正位词 |
| fireflies alternative | 50 | **6** | $9.26 | comm | 次级 | KD=6 CPC $9.26 全报告最低 KD 之一，"Fireflies 自托管替代" |
| whisper vs otter | 20 | 0 | — | new | GEO | 直连对比词，抢占"本地 vs 云端会议转写"引用位 |
| self hosted notebooklm | 30 | 0 | — | new | GEO | 近零量语义完美契合，GEO 占位 |
| local ai meeting notes | 30 | 0 | $2.75 | new | GEO | Whisper+Open Notebook 组合正位，GEO 占位 |
| open source meeting transcription | 20 | 0 | $2.12 | new | GEO | 空白词，语义完美，抢引用位 |

---

## 核心洞见

1. **品牌护城河：不可正面刚。** SEMrush Rank 10,441、自然流量 21.9 万/月、估值 $258K/月，且品牌词（otter ai 13.5万、otter 20.1万）+ 海量误拼变体（ottr/ottor/ottter/outter…全部霸榜第 1）构成典型的品牌心智护城河。品类先发 + 3500 万用户 + 企业"对话知识引擎"叙事，Olares 无法也不必去抢这些品牌/导航词。

2. **可复制的打法：程序化 use-case 落地页 + 买品类大词。** Otter 用 Google Ads 买 `transcription`(33K)、`speech to text`(27K)、`voice to text`(18K)、`notes app`(49.5K) 等超级大词，全部导向 `get.otter.ai/meeting-notes`、`/interview-transcription`、`/video-to-text`、`/youtube-transcript-generator` 这类程序化 use-case 落地页——与 Lovable 的 `/guides/`+`/solutions/use-case/` 同构。Olares 可对 Whisper/Open Notebook 做同样的"每个转写场景一个落地页"矩阵（会议/访谈/播客/YouTube/视频转文字），且靠自然排名而非烧广告。

3. **对 Olares 最关键的 3 个词：`notebooklm alternative`（320, KD=7）、`transcribe audio`（6,600, KD=37）、`otter ai podcast transcript`（1,000, KD=0）。** 前者是 Open Notebook 的完美正位词（自托管开源 NotebookLM，几乎无竞争）；中者是 Whisper 可正面打的中等 KD 品类大词；后者 KD=0 且是播客主稳定长期需求。三词分别锚定"私有笔记 + 本地转写 + 垂直场景"，且**两款平替（Whisper-WebUI/Whisper API、Open Notebook）都已在 Olares Market**，是最短的转化路径。

4. **最大攻击面：隐私 + 订阅计费。** Otter 所有会议音频必须上传云端，问题词里密集出现 `is otter ai safe`(140)、`is otter ai hipaa compliant`(110, CPC $8)、`how to stop otter ai from joining meetings`(110)、`otter ai privacy/security`(各 70, CPC $9)、`how to cancel otter ai subscription`(210)、`is otter ai free`(590)。Olares 差异化叙事应直击："本地 Whisper + Open Notebook = 会议音频与摘要永不离开你的设备，零订阅、无人数限额、天然满足 HIPAA/隐私诉求"。这是比功能对比更锋利的切入点。

5. **隐藏低 KD 金矿：`fireflies alternative`（KD=6, CPC $9.26）、`granola alternative`（KD=12）、`otter ai vs fireflies`（KD=19）、`meeting recorder`（KD=19）、`podcast transcription`（KD=19）、`transcribe interview`（KD=20）。** 这批词量虽不大但竞争极低、商业价值高（CPC $1.4–9.3），配合已上架的 Whisper/Open Notebook 可低成本抢排名。其中 `fireflies alternative` 仍是全报告最低 KD 之一——一篇"Fireflies 自托管开源替代"几乎可无竞争登顶。

6. **GEO 前瞻布局：** `whisper vs otter`、`self hosted notebooklm`、`local ai meeting notes`、`open source meeting transcription`、`open source ai transcription`、`self hosted transcription` 等词目前近零量、KD=0，但语义与 Olares"本地会议转写/私有笔记"完美契合。建议提前发布权威组合方案内容（Whisper+Open Notebook on Olares），抢 AI Overview / Perplexity 的引用位——用户搜"开源自托管会议转写方案"时，被引用的应当是 Olares。

7. **与既有分析的关联：** 本报告延续旧版 Otter 报告的核心判断（`fireflies alternative` KD=6、`otter ai podcast transcript` KD=0、隐私差异化不硬拼 `ai meeting notes`），并**新增修正**：① Olares 平替升级为 **Whisper + Open Notebook 双组件**（旧版为 Whisper+n8n），因两者均已上架 Market 且 Open Notebook 直接命中 `notebooklm alternative` KD=7 这一旧版未发现的金矿；② 补齐了完整流量基线（Rank/子域名/付费词打法）与隐私/合规问题词攻击面。与 `olares-500-keywords` 的"本地 LLM / 隐私自托管"分类互补，建议把"本地会议转写/私有笔记"作为独立场景补入词表。

---

*数据来源：SEMrush us 数据库（domain_rank / resource_organic / domain_organic_subdomains / resource_adwords / domain_organic_organic / phrase_these / phrase_related / phrase_questions）| 2026-07-07*
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
