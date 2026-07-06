# 系统原生语音输入（Apple Dictation / Google Voice Typing / Windows Speech）SEO 竞品分析报告

> 场景词分析（无独立官网）| SEMrush US | 2026-07-06
> 系统内置语音输入是各大平台的免费标配功能——Apple Dictation（macOS/iOS）、Google Voice Typing / Gboard（Android/iOS）、Windows Voice Typing（Win10+）——共同定义了"voice to text"品类的基础心智，但均为闭源、部分依赖云端、无自定义词汇。

---

## 项目理解（前置）

系统原生语音输入指三大平台的内置语音转文字功能：Apple Dictation（macOS/iOS，Apple Silicon 可完全离线，Neural Engine 本地推理）、Google Voice Typing / Gboard（Android/iOS，支持下载离线语言包）、Windows Voice Typing（Win10+，`Win+H` 触发，部分依赖云端）。它们共同构成了"voice to text"品类的用户心智基础——几乎所有用户的第一个语音输入工具都是系统自带的。对 Olares 而言，这个品类的攻击面不在品牌词（大厂护城河），而在**平台限制词**（仅限某平台）、**精度不足词**（professional/accurate）、**隐私词**（offline/private/local）和**替代词**（alternative）。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 三大平台系统内置语音转文字，零成本、开箱即用，但闭源、跨平台受限、无自定义词汇 |
| 开源 / 许可证 | 全部闭源；底层模型不公开 |
| 主仓库 | 无（系统功能，非独立项目） |
| 核心功能 | 实时语音转文字、标点插入、语音命令控制、多语言支持 |
| 商业模式 / 定价 | 完全免费（系统内置）；Apple 离线需 Apple Silicon 或 A 系列芯片 |
| 差异化 / 价值主张 | 零摩擦（无需安装）、与系统深度集成；Apple 在本机离线+准确率最高（93-95%）；Gboard 在 Android 生态覆盖率最广；Windows 系列最易上手 |
| 主要竞品（初判）| Wispr Flow（AI 格式化）、Dragon Professional（专业级）、Superwhisper（离线 Whisper）、Google Docs Voice Typing（浏览器免费）、Microsoft Dictate（Office 集成） |
| Olares Market | Speaches（✅ 已上架）、Whisper API（✅ 已上架）、Whisper-WebUI（✅ 已上架） |
| 来源 | [Apple Support: Dictation](https://support.apple.com/guide/mac-help/use-dictation-mh40584/mac)、[Google Gboard Help](https://support.google.com/gboard/answer/2781851)、[Microsoft: Windows Voice Typing](https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-fec94565-c4bd-329d-e59a-af033fa5689f)、[clevertype.co 2026 benchmarks](https://www.clevertype.co/post/best-voice-to-text-desktop-apps-for-mac-and-windows-in) |

---

## 流量基线（Phase 1）

无独立官网，跳过域名报告，直接进入关键词层面分析。

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD<30 且量>0 的机会词。

### 竞品 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| best speech to text | 2,900 | 47 | $0 | 商业 | 高量中 KD；导向比较类内容 |
| voice to text app | 2,400 | 47 | $1.10 | 商业 | 导向 app 推荐；系统内置也在列 |
| best dictation software | 390 | 41 | $2.50 | 商业 | KD 合理；专业用户选型 |
| best voice to text | 170 | 47 | $5.23 | 商业 | CPC 高说明付费意愿强 |
| wispr flow alternative | 70 | 16 | $3.18 | 商业 | ⭐ 量小但 KD 极低；Speaches 是最佳自托管答案 |
| dragon professional | 880 | 19 | $2.67 | 信息/商业 | ⭐ Dragon 替代场景；Olares 用户关注离线 + 成本 |
| typeless ai | 210 | 41 | $1.39 | 商业 | 新兴 AI 语音输入；反衬本地 Whisper 无订阅费优势 |

### 品类词

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| speech to text | 22,200 | 82 | $1.38 | 信息 | 品类最大词；KD 极高，长尾子词价值更大 |
| voice to text | 18,100 | 80 | $1.58 | 信息 | 品类第二大词；KD 极高 |
| dictation | 14,800 | 60 | $2.24 | 信息 | 宽泛品类词 |
| voice typing | 4,400 | 89 | $1.02 | 信息 | KD 最高；大厂主占 |
| speech recognition software | 3,600 | 57 | $2.30 | 信息 | 企业/专业用户信号词 |
| voice recognition software | 1,900 | 53 | $2.25 | 信息 | 同上 |
| dictation software | 1,900 | 41 | $3.08 | 信息/商业 | CPC 高；专业购买意图 |
| dictation app | 1,300 | 50 | $2.53 | 商业 | 移动优先场景 |
| voice dictation | 720 | 79 | $1.80 | 信息 | KD 高，品类支撑词 |
| ai dictation | 320 | 47 | $4.41 | 商业 | CPC 最高；AI 格式化方向新兴需求 |
| voice input | 260 | 81 | $0.82 | 信息 | KD 极高，无机会 |
| free voice to text | 2,900 | 75 | $1.77 | 信息 | 高量高 KD；用户关注免费选项 |
| free speech to text | 1,000 | 71 | $2.03 | 信息 | 同上 |

### 产品 / 功能词（系统内置功能前缀）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| google docs voice typing | 12,100 | 29 | $2.51 | 信息 | ⭐ 量最大的低 KD 词！实际是 Google 系功能，但与系统语音输入高度关联 |
| wispr flow | 18,100 | 58 | $2.82 | 商业 | 第三方 AI 语音输入标杆；KD 中等，流量可观 |
| superwhisper | 8,100 | 39 | $0.65 | 商业 | ⭐ Whisper 本地替代最具代表性品牌；KD<40 |
| apple dictation | 1,600 | 49 | $1.53 | 信息 | Apple 平台功能词；KD 中等 |
| google voice typing | 1,900 | 62 | $1.06 | 信息 | Google 平台功能词 |
| microsoft dictate | 480 | 49 | $1.85 | 信息 | Office 集成语音输入 |
| windows speech recognition | 1,000 | 41 | $1.48 | 信息 | Windows 原生 SR |
| windows voice typing | 260 | 37 | $1.91 | 信息 | ⭐ Windows 功能更新名称；KD 接近 30 |
| gboard voice typing | 590 | 52 | $0.40 | 信息 | Android 键盘功能词 |
| dragon dictation | 2,400 | 53 | $2.04 | 信息 | Dragon 品牌词之一 |
| dragon naturally speaking | 3,600 | 51 | $2.36 | 信息 | Dragon 品牌主词 |
| voice to text iphone | 1,300 | 42 | $1.06 | 信息 | 移动平台需求 |
| voice to text android | 2,400 | 39 | $1.33 | 信息 | ⭐ Android 平台需求；KD<40 |
| voice to text windows | 1,000 | 43 | $2.76 | 信息 | Windows 平台 |
| voice to text mac | 320 | 15 | $2.79 | 信息 | ⭐⭐ KD 仅 15！Mac 平台用户替代搜索 |
| how to use dictation on mac | 2,400 | 35 | $0.98 | 信息 | ⭐ 高量低 KD；Apple 用户最高频使用问题 |
| speech to text mac | 1,300 | 26 | $2.87 | 信息 | ⭐ Mac STT 低 KD；Olares macOS 安装场景 |
| mac voice to text | 1,000 | 34 | $2.45 | 信息 | ⭐ Mac 平台信号词 |
| speech recognition mac | 720 | 28 | $2.45 | 信息 | ⭐ KD<30；Mac 高级用户替代搜索 |
| iphone voice to text | 880 | 33 | $1.07 | 信息 | ⭐ 移动场景 |
| android voice to text | 1,300 | 41 | $1.34 | 信息 | 移动场景 |
| how to use dictation on mac | 2,400 | 35 | $0.98 | 信息 | ⭐ 教程词 |
| how to enable dictation on mac | 210 | 26 | $0 | 信息 | ⭐ 低 KD 教程词 |
| dictation mac shortcut | 210 | 30 | $0 | 信息 | ⭐ 快捷键教程 |
| voice typing mac | 90 | 32 | $2.38 | 信息 | ⭐ 长尾 Mac 场景 |
| mac dictation software | 40 | 17 | $2.35 | 商业 | ⭐⭐ KD 极低，选型意图强 |

### 开源 / 自托管信号词（Olares 机会前哨）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| faster-whisper | 3,600 | 29 | $2.80 | 信息 | ⭐ Speaches 核心引擎；KD 合理，开发者信号词 |
| whisperx | 2,400 | 28 | $2.82 | 商业/信息 | ⭐ Whisper 增强版（说话人分离）；KD 低 |
| whisper ai | 9,900 | 81 | $1.90 | 信息 | 高量极高 KD；无直接机会但辅助语义 |
| openai whisper | 6,600 | 97 | $2.56 | 信息/商业 | 品牌护城河词；KD 97 无法攻取 |
| whisper openai | 2,400 | 91 | $2.51 | 商业 | 同上 |
| open ai whisper | 1,900 | 88 | $2.56 | 信息/商业 | 同上 |
| whisper transcription | 1,900 | 82 | $2.70 | 信息 | 高量高 KD |
| openai whisper api | 1,300 | 50 | $5.09 | 信息 | CPC 极高；开发者替换 API 场景 |
| whisper model | 1,300 | 70 | $4.43 | 信息 | 技术词 |
| whisper cpp | 1,600 | 34 | $2.29 | 信息 | ⭐ whisper.cpp 本地跑；KD<35 |
| faster whisper | 1,600 | 33 | $2.80 | 信息 | ⭐ 同 faster-whisper |
| whisper speech to text | 480 | 67 | $1.63 | 信息 | 高 KD |
| whisper asr | 320 | 47 | $2.38 | 信息 | 技术词 |
| whisper large v3 | 390 | 46 | $2.58 | 信息 | 模型词 |
| whisper large v3 turbo | 260 | 31 | $3.19 | 信息 | ⭐ 新模型；KD<35 |
| whisper stt | 140 | 58 | $2.33 | 信息 | 中 KD |
| whisper local | 140 | 42 | $2.08 | 信息 | 本地化场景 |
| whisper voice to text | 210 | 76 | $2.20 | 信息 | 高 KD |
| run whisper locally | 110 | 33 | $6.32 | 信息 | ⭐ CPC 极高 $6.32；有强商业意图的自托管词 |
| whisper tiny | 110 | 40 | $1.54 | 信息 | 模型词 |
| open source speech to text | 210 | 35 | $2.38 | 信息 | ⭐ 开源信号词；KD<40 |
| speaches | 720 | 50 | $4.06 | 信息 | Olares Market 已上架工具；品牌词 CPC 高 |
| distil-whisper | 40 | 31 | $0 | 信息 | ⭐ 蒸馏模型；KD<35 |
| offline voice to text | 20 | 0 | $1.84 | 信息 | ⭐ GEO 前哨；完全匹配 Olares 场景 |
| self hosted speech to text | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| local voice recognition | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| on device speech recognition | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨 |
| local ai transcription | 20 | 0 | $2.17 | 信息 | ⭐ GEO 前哨；CPC 有商业意图 |
| open source voice to text | 30 | 0 | $2.57 | 信息 | ⭐ GEO 前哨 |
| whisper privacy | 20 | 0 | $0 | 信息 | ⭐ GEO 前哨；Olares 核心叙事 |
| openai whisper alternative | 0 | 0 | $2.93 | 商业 | ⭐ GEO 前哨；CPC 存在说明商业意图 |

### 问题词（信息意图 FAQ/内容选题）

| 关键词 | 月量 | KD | CPC | 意图 | 备注 |
|--------|------|----|-----|------|------|
| how to use dictation on mac | 2,400 | 35 | $0.98 | 信息 | ⭐ 最高频 Mac 语音输入问题 |
| how to turn on voice to text on android | 1,000 | 33 | $0.79 | 信息 | ⭐ Android 系统功能教程 |
| how do i do voice to text | 880 | 42 | $0.62 | 信息 | 通用入门问题 |
| how to do voice to text on google docs | 880 | 41 | $1.61 | 信息 | Google 生态 |
| how to turn on voice to text on iphone | 720 | 26 | $1.34 | 信息 | ⭐ iPhone 语音输入激活 |
| how to use speech to text on mac | 320 | 27 | $2.52 | 信息 | ⭐ KD 低；Mac 专项 |

---

## Olares 关联词（Phase 3）

**核心逻辑：系统原生语音输入的最大弱点是"平台锁定 + 精度天花板 + 数据隐私"——Whisper + Speaches on Olares 提供跨平台、更高精度、完全本地的语音输入，数据不离开用户的设备。**

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|-----|------------|
| voice to text mac | 320 | 15 | $2.79 | ⭐⭐⭐ KD 仅 15；Mac 用户找 Apple Dictation 替代，Speaches on Olares = 本地 Whisper API，媲美精度 + 完全离线 |
| google docs voice typing | 12,100 | 29 | $2.51 | ⭐⭐⭐ 量最大低 KD 词；非 Olares 直接竞品，但文章可横向比较"哪种语音输入最准/最私密"，引出 Speaches |
| superwhisper | 8,100 | 39 | $0.65 | ⭐⭐⭐ Superwhisper 用户是 Olares 最精准的目标受众——同样在找离线 Whisper；Olares 在自托管服务器上提供同等体验，额外得到 API 兼容层 |
| faster-whisper | 3,600 | 29 | $2.80 | ⭐⭐⭐ Speaches 的底层引擎就是 faster-whisper；开发者词，技术对比文机会 |
| whisperx | 2,400 | 28 | $2.82 | ⭐⭐ WhisperX 用户对 Whisper 生态熟悉；Speaches 提供更易用的 API 服务层 |
| dragon professional | 880 | 19 | $2.67 | ⭐⭐ Dragon 用户有"高精度、离线、专业"的诉求，Speaches + Whisper large-v3 可覆盖 |
| wispr flow alternative | 70 | 16 | $3.18 | ⭐⭐⭐ KD 极低的商业词；Wispr Flow = 闭源 + 订阅 $15/月；Olares 用 Speaches 提供同等能力且免费完全私有 |
| how to use dictation on mac | 2,400 | 35 | $0.98 | ⭐⭐ 入口词；文章结尾自然引出"更进一步：Speaches on Olares 提供离线精度更高的替代方案" |
| speech to text mac | 1,300 | 26 | $2.87 | ⭐⭐⭐ Mac 用户找 STT；低 KD；Speaches 可通过 macOS 键盘输入法扩展集成 |
| mac voice to text | 1,000 | 34 | $2.45 | ⭐⭐ Mac 用户找更好语音输入；Speaches 离线 + 更高精度 |
| speech recognition mac | 720 | 28 | $2.45 | ⭐⭐ 同上，更技术的措辞 |
| run whisper locally | 110 | 33 | $6.32 | ⭐⭐⭐ CPC $6.32 说明强商业意图；用户主动找自托管 Whisper，Speaches on Olares 是最易用的答案 |
| open source speech to text | 210 | 35 | $2.38 | ⭐⭐ 开源信号词；Speaches MIT 开源 + Olares Market 一键安装 |
| whisper cpp | 1,600 | 34 | $2.29 | ⭐⭐ 技术用户找本地 Whisper；whisper.cpp 是 CLI，Speaches 提供 API 服务层 + UI |
| offline voice to text | 20 | 0 | $1.84 | ⭐⭐⭐ GEO 前哨；语义精准匹配 Olares 隐私叙事，抢 AI Overview 引用位 |
| self hosted speech to text | 20 | 0 | $0 | ⭐⭐⭐ GEO 前哨；Speaches 正是自托管 STT 的代表性工具 |
| whisper privacy | 20 | 0 | $0 | ⭐⭐⭐ GEO 前哨；完全契合 Olares "数据不离家"叙事 |
| openai whisper alternative | 0 | 0 | $2.93 | ⭐⭐⭐ GEO 前哨；CPC 说明商业意图存在；Speaches + Olares 是最完整答案 |
| local ai transcription | 20 | 0 | $2.17 | ⭐⭐ GEO 前哨；Agent 时代本地语音转录需求 |

---

## Top 关键词（含角色判断）

报告只对词下判断；聚成文章簇在 seo-content 阶段做。角色 = 主词候选 / 次级 / GEO。

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| google docs voice typing | 12,100 | 29 | $2.51 | 信息 | **主词候选** | 量最大的低 KD 词；写"Google Docs 语音输入 vs 本地 Whisper"文章可天然引出 Speaches |
| superwhisper | 8,100 | 39 | $0.65 | 商业 | **主词候选** | Whisper 本地替代标杆；KD<40；"superwhisper vs speaches on olares"对比文机会 |
| faster-whisper | 3,600 | 29 | $2.80 | 信息 | **主词候选** | Speaches 底层引擎；KD 低 + 开发者受众精准；"what is faster-whisper + how to self-host" |
| whisperx | 2,400 | 28 | $2.82 | 商业/信息 | **主词候选** | KD<30；WhisperX vs Speaches 对比；Olares 两者都可装 |
| voice to text mac | 320 | **15** | $2.79 | 信息 | **主词候选** | KD 仅 15 是本报告最低！Mac 用户替代场景，直指 Speaches on Olares |
| speech to text mac | 1,300 | 26 | $2.87 | 信息 | **主词候选** | Mac 低 KD 集群头部词；Olares macOS 安装 + Speaches 教程文的主词 |
| dragon professional | 880 | **19** | $2.67 | 信息/商业 | **主词候选** | KD 19；Dragon 用户是最有价值的潜在迁移人群（高精度、专业离线需求） |
| wispr flow alternative | 70 | **16** | $3.18 | 商业 | **主词候选** | 量小但 KD 16 + CPC $3.18；商业意图强；Speaches 是最佳自托管答案 |
| whisper cpp | 1,600 | 34 | $2.29 | 信息 | **主词候选** | KD<35；开发者词；whisper.cpp 是 CLI，Speaches 提供更完整 API 服务层 |
| how to use dictation on mac | 2,400 | 35 | $0.98 | 信息 | **主词候选** | 高量 + KD 合理；教程入口词，文章末尾引出 Olares 替代方案 |
| mac voice to text | 1,000 | 34 | $2.45 | 信息 | **次级** | 与 speech to text mac 并入同一 Mac 语音输入簇 |
| speech recognition mac | 720 | 28 | $2.45 | 信息 | **次级** | ⭐ Mac 低 KD 长尾；并入 Mac 语音输入簇 |
| voice typing mac | 90 | 32 | $2.38 | 信息 | **次级** | Mac 语音输入簇长尾 |
| mac dictation software | 40 | 17 | $2.35 | 商业 | **次级** | KD 极低；Mac 选型意图强；并入 Mac 簇 |
| how to enable dictation on mac | 210 | 26 | $0 | 信息 | **次级** | Mac 教程簇 FAQ |
| dictation mac shortcut | 210 | 30 | $0 | 信息 | **次级** | Mac 教程簇 FAQ |
| windows voice typing | 260 | 37 | $1.91 | 信息 | **次级** | KD<40；Windows 平台入口词；可并入 voice to text windows 簇 |
| voice to text android | 2,400 | 39 | $1.33 | 信息 | **次级** | ⭐ Android 平台量大 KD<40；Gboard 用户的替代入口 |
| run whisper locally | 110 | 33 | $6.32 | 信息 | **次级** | CPC $6.32 是本报告最高！自托管 Whisper 教程的高价值次级词 |
| open source speech to text | 210 | 35 | $2.38 | 信息 | **次级** | 开源信号词；并入自托管 STT 簇 |
| distil-whisper | 40 | 31 | $0 | 信息 | **次级** | KD<35；蒸馏 Whisper 技术词，开发者受众 |
| whisper large v3 turbo | 260 | 31 | $3.19 | 信息 | **次级** | Speaches 默认推荐模型；并入 Whisper 模型簇 |
| how to turn on voice to text on iphone | 720 | 26 | $1.34 | 信息 | **次级** | iPhone 教程簇入口 |
| how to use speech to text on mac | 320 | 27 | $2.52 | 信息 | **次级** | Mac 教程簇 |
| offline voice to text | 20 | 0 | $1.84 | 信息 | **GEO** | 完全匹配 Olares 隐私叙事；抢 AI Overview / Perplexity 引用位 |
| self hosted speech to text | 20 | 0 | $0 | 信息 | **GEO** | Speaches on Olares 的精准标签词 |
| whisper privacy | 20 | 0 | $0 | 信息 | **GEO** | Olares "数据不离家"叙事前哨词 |
| openai whisper alternative | 0 | 0 | $2.93 | 商业 | **GEO** | CPC 有值；商业意图存在；Speaches 是最完整答案 |
| local ai transcription | 20 | 0 | $2.17 | 信息 | **GEO** | Agent 时代本地语音转录场景 |
| on device speech recognition | 20 | 0 | $0 | 信息 | **GEO** | 隐私 + 端侧推理叙事 |

---

## 核心洞见

1. **品牌护城河**：三大系统内置功能本身无可攻取的独立品牌词（无独立域名、无付费广告）。品类词（voice to text / speech to text）KD 80-89，攻不动。**真正的机会在子域名：平台专项词（Mac/Windows）+ 精度/离线/隐私叙事词**。Mac 相关词 KD 普遍 15-35，是整个语音输入品类中竞争最低洼的高质量词群。

2. **可复制的打法**：
   - **Mac 低 KD 词群**：`voice to text mac`（KD 15）、`mac dictation software`（KD 17）、`speech to text mac`（KD 26）、`speech recognition mac`（KD 28）等 8+ 词，合计月量约 5,000+，可聚成一篇"Mac 语音输入终极指南"——内嵌 Speaches + Olares 叙事。
   - **Whisper 生态开发者词**：`faster-whisper`（KD 29）、`whisperx`（KD 28）、`whisper cpp`（KD 34）均 KD<35，面向已认知 Whisper 的开发者，转化率高。
   - **对比 / 替代文**：`wispr flow alternative`（KD 16）、`dragon professional`（KD 19）均为低 KD 商业意图词，可直接落 Speaches on Olares 替代落地页。

3. **对 Olares 最关键的词**：
   - `google docs voice typing`（12,100 月量，KD 29）——品类量最大低 KD 词，文章入口
   - `superwhisper`（8,100 月量，KD 39）——最接近 Olares 目标用户的竞品词
   - `voice to text mac`（320 月量，KD 15）——KD 最低的高意图词，直击 Mac 用户替代场景

4. **最大攻击面**：
   - **闭源 + 云端隐私**：Windows Voice Typing 默认依赖云端（无离线选项，除 Voice Access）；Gboard 在无离线包时发送音频至 Google 服务器。隐私叙事词（`offline voice to text`、`whisper privacy`、`on device speech recognition`）虽近零量，但 AI Overview 引用机会大。
   - **平台锁定**：Apple Dictation 仅限 Apple 设备，无跨平台。Speaches + Olares 是"在哪都能用"的替代。
   - **精度天花板**：Windows Voice Typing 准确率约 90-94%，Apple 93-95%；Whisper large-v3 在标准 benchmark 超越两者，且支持 99+ 语言。
   - **专业词汇缺失**：三大系统内置均无自定义词汇；Dragon 的 $699 定价是痛点，`dragon professional`（KD 19）攻击面极高。

5. **隐藏低 KD 金矿**：
   - `voice to text mac`（KD **15**）——全报告最低 KD 主词候选，月量 320
   - `mac dictation software`（KD **17**）——商业意图，月量 40，轻松获取
   - `wispr flow alternative`（KD **16**）——$3.18 CPC，商业意图词
   - `dragon professional`（KD **19**）——专业用户市场入口
   - 问题词簇：`how to turn on voice to text on iphone`（KD 26）、`how to use speech to text on mac`（KD 27）——教程长尾

6. **GEO 前瞻布局**：
   - `offline voice to text` / `self hosted speech to text` / `whisper privacy` / `on device speech recognition`——当用户问 AI "哪个语音输入最私密/离线可用？"，应该在 FAQ 和场景描述中精确覆盖这些词，Speaches on Olares 抢 AI Overview 引用位。
   - `openai whisper alternative`（CPC $2.93，量 0）——商业意图前哨，Perplexity / ChatGPT 推荐场景。
   - `local ai transcription` / `local ai dictation`——Agent 时代本地语音输入管道词，量小但战略价值高。

7. **与既有分析的关联**：
   - Speaches 报告（`market/reports/speaches.md`）已建立 Speaches 的 API 层叙事；本报告补充了"从系统内置功能出发找替代"这一用户旅程的关键词，两份报告互补——Speaches 报告从开发者 API 角度出发，本报告从普通用户"我的系统自带语音输入不够用"出发。
   - `olares-500-keywords` 词表中暂无 Mac 语音输入相关词；本报告贡献了 `voice to text mac`（KD 15）、`speech to text mac`（KD 26）等高价值低竞争词，可直接补入 Olares 内容规划。
   - `faster-whisper` / `whisperx` 已在 Speaches 报告中出现，此处角色判断与 Speaches 报告保持一致（主词候选），可共用同一开发者向技术对比文。

---

*数据来源：SEMrush US 数据库（`phrase_these`、`phrase_related`、`phrase_fullsearch`、`phrase_questions`、`phrase_organic`）| 2026-07-06*  
*所有搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
