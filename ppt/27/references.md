# 第 27 页资料：Panther Lake 隐私会议 AI

> AS_OF = 2026-07-14。用于 [soc-meeting-box-slide.md](./soc-meeting-box-slide.md) 的事实、价格与内部判断。价格和库存发布前复核。

## 1. 市场验证

### 整体市场规模

公开行业报告对定义并不完全一致，但对 2025 年全球 **AI meeting assistant** 市场的估值集中在约 **$3.1–3.5B**，长期 CAGR 约 **24–26%**：

| 来源 | 市场定义 | 2025 | 预测 | 边界 |
|------|----------|------|------|------|
| Grand View Research | AI meeting assistant 软件与服务；转写、总结、内容助手与洞察 | **$3.47B** | 2033 **$21.48B**；CAGR **25.8%** | 不含硬件；公开摘要不披露厂商收入拆分 |
| The Business Research Company | 软件、硬件与服务；含转写、翻译、调度与咨询 | **$3.14B** | 2030 **$9.33B**；CAGR **24.3%** | 口径宽于 GVR；页面存在年份编辑瑕疵 |

来源：

- Grand View Research：https://www.grandviewresearch.com/industry-analysis/ai-meeting-assistant-market-report
- The Business Research Company：https://www.thebusinessresearchcompany.com/report/artificial-intelligence-ai-powered-meeting-assistants-global-market-report

**对外口径**：`Global AI meeting assistant market: ~$3.1–3.5B in 2025; projected to exceed $9B by 2030, growing at ~25% CAGR.`  
这是分析机构预测，不是经审计行业收入汇总；主要代表软件与服务需求趋势，不能写成 Intel 硬件 TAM。

### 两个独立付费案例

| 主张 | 证据 | 来源 |
|------|------|------|
| Plaud 累计出货 >2M 台、软件 ARR >$100M | Plaud 官方称两年内从 $1M 增至 $100M ARR、覆盖 170+ 国家；TechCrunch 报道其出货 >2M 台，近 50% 设备用户升级付费 | Plaud https://www.plaud.ai/blogs/news/plaud-scales-from-1m-to-100m-arr ｜ TechCrunch https://techcrunch.com/2026/06/16/plaud-says-its-software-business-topped-100m-in-arr-after-shipping-over-2m-ai-notetakers/ |
| Otter.ai 已超过 $100M ARR、35M 用户、累计处理 >1B 场会议 | Otter 官方 2025 年度总结；公司自报，未审计 | https://otter.ai/blog/otter-ai-caps-transformational-2025-with-100m-arr-milestone-industry-first-ai-meeting-agents-and-global-enterprise-expansion |

**口径**：Plaud 与 Otter 是两个独立的付费需求案例；两者的 ARR、用户与会议量口径不同，不能相加为市场规模，也不能直接推出本地会议盒的可获得市场份额。幻灯上把二者分别呈现为**同一付费市场的两种形态**——Plaud＝硬件录音端（线下），Otter＝会议软件（线上），以对应本地盒同时覆盖两类采集需求，切勿把两组数字相加。

### 专用 AI 录音硬件规模边界

- Plaud 已累计销售 >200 万台，Euromonitor 认定其为 2025 年全球 AI note-taking device 品牌销量第一，但未公开品牌份额或全球品类总销量。
- 未找到公开权威来源支持“全球专用 AI 录音硬件约 300 万台 / 年”。该数字仅可作为内部宽口径规划估算，不能写成第三方市场事实。
- Plaud 排名：https://www.plaud.ai/blogs/news/plaud-confirmed-as-world-number-one-ai-note-taking-device-brand

## 2. 云端处理与隐私机会

- **Otter**：服务条款明确写明音频在云基础设施处理；隐私政策列出 AWS 等云计算、存储与 AI 服务商。  
  https://otter.ai/terms-of-service  
  https://otter.ai/privacy-policy
- **Plaud**：默认录音保存在设备；关闭 Private Cloud Sync 时不持久保存云端副本，但请求转写或总结时，所需音频或文本仍会发送至区域化 AI 服务端点处理。其企业 API 约定 zero retention，并禁止把数据用于训练。  
  https://www.plaud.ai/pages/ai-data-usage-transparency-policy  
  https://support.plaud.ai/hc/en-us/articles/57744162858009-How-your-data-is-used-in-AI-processing
- **Otter HIPAA 边界**：HIPAA 只在 Enterprise 方案并签署 BAA 后适用，Otter 默认不是 HIPAA covered entity。  
  https://help.otter.ai/hc/en-us/articles/33975072019991-HIPAA-Otter-ai

**对外安全措辞**：本地处理减少第三方数据暴露，帮助机构控制数据驻留、权限和保留期限；不能写成“本地即合规”。录音同意、权限、审计、删除与 BAA 等仍需落实。

**敏感职业用例**：Plaud 官方内容已覆盖律师的客户咨询/证人访谈、医生的患者问诊和销售的高价值客户对话；Otter 也把 healthcare、legal、sales 列为转录与总结场景。记者场景本轮缺少同等强度的公开量化证据，因此只作为用户访谈判断，不单独做数字主张。  
Plaud 法律：https://www.plaud.ai/blogs/articles/ai-note-taker-for-lawyers  
Plaud 医疗：https://www.plaud.ai/blogs/user-story/breaking-barriers-in-healthcare-how-dr-william-choo-uses-plaudai-to-transform-patient-care  
Plaud 销售：https://www.plaud.ai/blogs/user-story/how-relex-solutions-uses-plaud-ai-to-keep-sales-on-track  
Otter：https://otter.ai/blog/ai-to-summarize-transcripts

## 3. 出门问问合作与 TicNote 生态

### 公司与合作状态

- **Mobvoi 出门问问**于 2024-04-24 在港交所主板上市，股票代码 **2438**；主营面向企业和个人的 AI 软件解决方案、智能设备及配件。  
  港交所 2025 年业绩公告：https://www.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032700788.pdf
- **Olares 与出门问问的录音端合作已确认**。对外可写 confirmed recording-device partner。来源为用户确认的商务状态，不是公开新闻。
- 市场口径使用 **“Plaud 之外的主流挑战者 / a leading alternative to Plaud”**，不写“全球第二”。公开数据只支持 TicNote 全球销量在 2025 年中突破约 3 万台，TicNote Pods Kickstarter 获 510 位支持者；没有可靠的全球第二排名。  
  销量报道：https://time-weekly.com/post/324056  
  Kickstarter：https://www.kickstarter.com/projects/mobvoi/ticnote-pods-worlds-smartest-4g-ai-note-taking-earbuds

### 主力合作端点

| 产品 | 形态与能力 | 公开价格 | 来源 |
|------|------------|----------|------|
| **TicNote 卡片** | 3mm、29g、64GB、约 434 小时存储、20+ 小时录制；覆盖线下会议与电话录音 | 海外约 $159.99；国内 999 元起 | Mobvoi 官方：https://www.mobvoi.com/us/pages/mobvoiticnote ｜ 国内发布参考：https://www.qbitai.com/2025/06/301867.html |
| **TicNote Pods** | 4G / Wi-Fi AI 录音耳机；耳机与充电仓双通道采集，覆盖线上会议、线下讨论、电话和差旅 | 4G MSRP $299；Wi-Fi MSRP $249 | Mobvoi 官方：https://www.mobvoi.com/ticnotepods/ ｜ 发布与定价：https://www.prnewswire.com/news-releases/ticnote-pods-the-worlds-first-4g-ai-note-taking-earbuds-302727252.html |

### 当前能力与目标集成边界

- TicNote 当前产品把录音上传至其云服务进行转写和总结；Pods 的 4G 价值在于不依赖手机或 Wi-Fi 即可上传。
- 双方目标产品链路是：**TicNote 采集 → 加密回传机构自己的 Olares box → 本地转写、总结、存储与检索**。
- 该本地回传链路是合作目标，不应写成已经发布或已经量产。

当前产品链路来源：TicNote 用户指南 https://www.ticnote.cn/zh/userguide ｜ Pods 发布 https://www.prnewswire.com/news-releases/introducing-ticnote-pods-the-worlds-first-4g-connected-ai-earbuds-302615673.html

## 4. 采集配件生态

| 端点类型 | 典型场景 | 对外状态 |
|----------|----------|----------|
| 录音卡片 | 电话、面对面会议、采访 | **已确认合作：TicNote** |
| AI 耳机 | 电话、线上会议、移动访谈 | **已确认合作：TicNote Pods** |
| USB / 蓝牙会议麦克风音箱 | 小会议室、圆桌讨论、临时会议空间 | 支持方向 / planned adapter |
| 手表与穿戴 | 随手记录、巡检、差旅 | 支持方向 |
| 手机 | 临时录音、已有设备接入 | 支持方向 |
| 会议室麦克风 / 现有会议系统 | 固定会议室、多麦克风阵列 | 支持方向 / planned adapter |
| 会议软件转写导入 | Zoom / Teams / Google Meet 等线上会议 | 支持方向 / planned integration |

**采集范围口径（对外）**：本方案同时覆盖两类付费需求——硬件录音端（对应 Plaud 类线下场景）与会议软件（对应 Otter 类线上场景），两者的转写都汇入同一个机构自有的本地知识库。对外幻灯里 Zoom / Teams / Google Meet 只作为“支持方向 / planned integration”，不写成已发布的对接功能；相关商标仅用于表述兼容意图。

**内部配件实例，不上对外幻灯**：

- 用户提供的 3588 会议麦克风音箱样机图：`/Users/pengpeng/.cursor/projects/Users-pengpeng-seo/assets/img_v3_0213i_13b4bde5-d8ea-4e25-a597-5e6025fa185g-07faf674-240b-416a-8e68-21c3240fbe0a.png`
- 图中信息：蓝牙 + 音箱、预估成本约 165 RMB；全双工、主动降噪与回声消除、USB / 蓝牙 / 无线连接、便携；3588 EVT 样机计划与内部排期不对外。
- 对外幻灯只用通用 pictogram 表示该品类，不使用带水印、成本、排期和样机状态的原图。

## 5. Panther Lake 能力与语音工作流

- Panther Lake / Core Ultra Series 3 是 Intel 18A 首代客户端 SoC；顶配平台最高约 180 TOPS。不同 SKU 的 CPU、GPU 与平台算力差异很大，不能把顶配数字套到 $999 目标机。  
  Intel 官方：https://www.intc.com/news-events/press-releases/detail/1752/intel-unveils-panther-lake-architecture-first-ai-pc  
  SKU 列表：https://www.intel.com/content/www/us/en/products/details/processors/core-ultra.html
- OpenVINO GenAI 已支持 Whisper tiny/base/small/large 在 NPU 上运行，FP16 或 INT8 均可；NPU 运行时和模型缓存仍需产品化封装。  
  https://docs.openvino.ai/2026/openvino-workflow-generative/inference-with-genai/inference-with-genai-on-npu.html
- Intel 与 Fluid Inference 的 Slipbox 案例已在 Core Ultra 上本地运行 Whisper v3 Turbo、PyAnnote / WeSpeaker、Qwen3 与 Phi-4-mini，覆盖转写、说话人分离与总结。该文章为合作案例，性能数字按最佳实践看待。  
  https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Bringing-AI-Back-to-the-Device-Real-World-Transformer-Models-on/post/1704424

### 目标 SKU 的 AI 算力差异

| SKU | NPU INT8 | iGPU INT8 | 来源与边界 |
|-----|----------|-----------|------------|
| Ultra 5 322 | 46 TOPS | 18 TOPS | MSI 设备资料 / 第三方规格；Intel ARK 页面字段当前未正常渲染数值。Intel：https://www.intel.com/content/www/us/en/products/sku/245716/intel-core-ultra-5-processor-322-12m-cache-up-to-4-40-ghz/specifications.html |
| Ultra 7 356H | 50 TOPS | 40 TOPS | Minisforum M2 官方产品页：https://store.minisforum.com/products/minisforum-m2-mini-pc |
| Ultra X7 358H | up to 50 TOPS | 122 TOPS | ASUS 规格 + Intel ARK：https://www.asus.com/mx/laptops/for-work/expertbook/asus-expertbook-ultra/techspec/ ｜ https://www.intel.com/content/www/us/en/products/sku/245527/intel-core-ultra-x7-processor-358h-18m-cache-up-to-4-80-ghz/specifications.html |

`180 Platform TOPS` 只对应顶配平台上限。Ultra 5 322 / 356H 的 iGPU 明显更小，目标价与 LLM 能力必须按具体 SKU 验证。

### 建议的异构分工

| 环节 | 主要模型 | 优先引擎 | 是否基础功能 |
|------|----------|----------|--------------|
| 说话人分离 | PyAnnote / WeSpeaker 类 | 优先评估 NPU / iGPU | 是 |
| STT | Whisper 类 | 优先评估 NPU，CPU/iGPU 回退 | 是 |
| 强制对齐 | CTC / alignment 模型 | CPU / NPU | 是 |
| 翻译 | 小型翻译模型 | NPU / iGPU，PoC 后定 | 可选 |
| 总结、问答 | 小型 LLM | iGPU / NPU / CPU，PoC 后定 | 可选 |

语音先行的原因：模型相对小、工作流可异步、单项峰值算力要求低，但需要多模型协同。Personal Agent 还要求更高的模型质量、长上下文 prefill、decode 和内存容量，不能只看 NPU TOPS。当前没有证据表明目标 Panther Lake SKU 已能提供让用户付费的本地 Personal Agent 体验；最终异构分工与响应速度必须用 Panther Lake 真机 PoC 确认。

### 五类模型的候选开源模型与许可（上幻灯用）

> **候选栈，非既定 BOM。** 均可在 OpenVINO / Intel 上评估；最终选型与量化以 Panther Lake PoC 为准。翻译刻意避开 NLLB（CC-BY-NC，禁商用）。

| 环节 | 候选开源模型 | 许可 | 来源 |
|------|--------------|------|------|
| 说话人分离 | pyannote `speaker-diarization-community-1`；WeSpeaker 做 embedding | pyannote 开源 pipeline（community-1 免费、需 HF 条款）；WeSpeaker Apache-2.0 | https://github.com/pyannote/pyannote-audio ｜ https://huggingface.co/pyannote/speaker-diarization-community-1 ｜ https://github.com/wenet-e2e/wespeaker |
| STT | **主模型：Qwen3-ASR-1.7B**（52 种语言与方言）；备选：Systran/faster-whisper-large-v3 | Qwen3-ASR Apache-2.0；faster-whisper-large-v3 MIT | https://huggingface.co/Qwen/Qwen3-ASR-1.7B ｜ https://huggingface.co/Systran/faster-whisper-large-v3 |
| 强制对齐 | **主模型：Qwen3-ForcedAligner-0.6B**（11 语、单段最长 5 分钟）；备选：WhisperX | Qwen3-ForcedAligner Apache-2.0；WhisperX BSD-2-Clause | https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B ｜ https://github.com/m-bain/whisperX |
| 翻译 | **主模型：MADLAD-400**（400+ 语） | Apache-2.0，可商用 | https://huggingface.co/google/madlad400-3b-mt |
| 总结 / 问答 | Qwen3-4B；Phi-4-mini | Qwen3-4B Apache-2.0；Phi-4-mini MIT | https://huggingface.co/Qwen/Qwen3-4B ｜ https://huggingface.co/microsoft/Phi-4-mini-instruct |

Intel 可信度锚点：Intel × Fluid Inference 的 Slipbox 案例已在 Core Ultra 上本地跑 Whisper v3 Turbo + PyAnnote / WeSpeaker + Qwen3 + Phi-4-mini（见上）。可选管线（翻译 + LLM 总结）算力更重、价值偏主观、可作付费层——飞书妙记的 LLM 总结即为付费功能。

**许可红线**：`facebook/nllb-200-distilled-600M` 为 CC-BY-NC-4.0，且官方模型卡明确标注 research model / not released for production deployment，因此不进入本页商业方案候选；当前翻译主模型只放 MADLAD-400（Apache-2.0）。SenseVoice 与 Opus-MT 不再列为本页当前候选。上幻灯前逐一复核所选权重的许可与 HF 使用条款。  
NLLB 官方模型卡：https://huggingface.co/facebook/nllb-200-distilled-600M

## 6. Panther Lake 设备现价

| 设备 | CPU | 配置 | 2026-07-14 价格 | 状态与来源 |
|------|-----|------|----------------|------------|
| MSI Cubi NUC AI+ 3MG | Core Ultra 5 322 | 裸机，无 RAM / SSD | **$584.99** | Newegg 自营，可加入购物车：https://www.newegg.com/msi-barebone-intel-core-ultra-5-322-cubi-nuc-ai-3mg-008bus/p/N82E16856167221 |
| ASRock NUC BOX-325 | Core Ultra 5 325 | 裸机，无 RAM / SSD | **$649.99** | Newegg，backorder：https://www.newegg.com/asrock-industrial-fanned-embedded-box-intel-core-ultra-5-325-nuc-box-325/p/N82E16856179019 |
| Minisforum M2 | Core Ultra 7 356H | 裸机 | **$527 促销 / $659 常规** | 官方可购买：https://store.minisforum.com/products/minisforum-m2-mini-pc |
| Minisforum M2 | Core Ultra 7 356H | 32GB + 1TB | **$959 促销 / $1,199 常规** | 同上 |
| ASRock NUC BOX-358H | Core Ultra X7 358H | 裸机，无 RAM / SSD | **$999.99** | Newegg：https://www.newegg.com/asrock-industrial-fanned-embedded-box-intel-core-ultra-x7-358h-nuc-box-358h/p/N82E16856179018 |
| GMKtec EVO-T2 | Core Ultra X7 358H | 64GB + 1TB | **$1,959** | 官方：https://www.gmktec.com/products/intel-core-ultra-x7-358h-x9-388h-evo-t2-ai-mini-pc |

**结论**：

- 356H 32GB/1TB 的 $959 促销整机提供了 `$999` 价格锚点，但不能证明含软件、服务与渠道成本的新产品能长期维持同价。
- 但可持续常规价更接近 `$1,099–1,199`。促销价不能直接等同于新品牌的小批量成本。
- X7 358H 裸机本身已约 $1,000，不适合作为 `$999` 目标 SKU。

## 7. SoC 成本估算

> **内部规划假设，不对外流转；不是 Intel 报价或确认 BOM。**

Intel ARK 只公开 Panther Lake 移动 SoC 的 `Tray` 订货信息，没有 RCP / 1K unit price：

- Core Ultra 5 325：https://www.intel.com/content/www/us/en/products/sku/245720/intel-core-ultra-5-processor-325-12m-cache-up-to-4-50-ghz/ordering.html
- Core Ultra X7 358H：https://www.intel.com/content/www/us/en/products/sku/245527/intel-core-ultra-x7-processor-358h-18m-cache-up-to-4-80-ghz/ordering.html

以下为从同机型价差与整机售价反推的 **OEM 有效成本估算，不是 Intel 报价**：

| 档位 | 代表 SKU | 估算成本 | 置信度 |
|------|----------|----------|--------|
| 入门 | Ultra 5 322 / 325 | **$180–250** | 中 |
| 中档 | Ultra 5 338H / Ultra 7 356H | **$250–350** | 中 |
| 高档 | Ultra X7 358H | **$350–500** | 中低 |
| 旗舰 | Ultra X9 388H | **$450–650** | 低 |

反推锚点：ASRock 同系列 NUC BOX-325 与 NUC BOX-358H 裸机零售价相差约 $350；其中包含 CPU、供电、散热和产品分档溢价，不能把全部价差视为芯片成本。

## 8. `$999` 可行性边界

- **DTC / OEM 合作**：Ultra 5 或 356H 值得验证 `$999`，但是否成立取决于 2026 DRAM / NAND 价格、采购规模、软件服务成本和毛利目标。
- **常规公开零售**：建议目标 `$1,099–1,199`；若经过传统分销和零售渠道，通常还需更高价格。
- **不建议的做法**：用 X7 / X9、32GB/1TB、完整渠道毛利，同时承诺 `$999`。
- **上幻灯口径**：`已售整机显示，$999–1,199 是值得与 Intel / OEM 共同验证的目标价格带；最终取决于 SKU、内存价格、采购规模与渠道模式。`

## 9. 产品包、TCO 与规模测算

> **内部规划模型；对外使用时必须保留“target / estimate”标记。**

### 典型团队包

- 产品定义：**5 个混合录音端 + 1 台共享 Panther Lake AI box**。
- 示例组合：3 个 TicNote 卡片（按海外 $159.99）+ 2 个 4G TicNote Pods（按 $299）+ 1 台 $999 AI box ≈ **$2,077**。
- 因此对外可写 **“~$2,000 target bundle”**；最终价格取决于合作价、端点组合与 AI box SKU。

### TCO 加分项

- 幻灯采用**AI Box 硬件 vs 云订阅**口径，双方均排除 Plaud / TicNote 等采集设备价格。
- Plaud 五人年付订阅三年：`5 × $240/年 × 3 年 = $3,600`。
- Panther Lake AI Box 目标硬件价：`$999–1,599`。按五人 Plaud 年订阅 `$1,200` 计算，简单硬件回本期约 `10–16 个月`，可收敛为 `roughly one-year hardware payback`。
- 该比较未计未来可能的 Olares 软件 / 服务费、维护成本、税费与资金成本，不是回本保证；最终售价也仍是 target。

### 规模目标

- 会议录音硬件品类约 300 万台 / 年：用户规划估算，缺少单一权威市场报告。
- 5% 份额约 15 万台 / 年：年度销售规划情景，不是第三方预测。
- 对外如保留，只能写：**Annual planning scenario: 150K units / 5% of an estimated ~3M-unit annual category**。

## 10. Olares 完整平台能力

本页的产品不是“只做会议转写的专用盒子”，而是运行完整 Olares 的 AI Box。Private Meeting AI 是基于当前 Panther Lake 性能、目标价格与付费需求选择的**主打 AI 工作负载**，不是平台能力边界。

- **文件、同步与共享**：Olares Files 提供集中存储、跨设备访问、同步、内部共享、公开分享、SMB 共享挂载与外部存储扩展。对外幻灯用 `files, sync and sharing` 或 `NAS capabilities`，不写成“具备所有传统 NAS 功能”；Olares 与传统 NAS 在 NFS、存储池等能力上并不完全相同。  
  https://docs.olares.com/manual/olares/files/  
  https://docs.olares.com/manual/olares-vs-nas.html
- **Windows VM / PC 工作负载**：Olares 可直接运行完整 Windows VM，通过浏览器 VNC 或 RDP 使用，支持文件传输和日常 Windows 应用。重型 GPU 工作负载存在边界；对外不写成完整替代高性能 Windows 游戏 / 工作站。  
  https://docs.olares.com/1.12.4/use-cases/windows.html
- **Intel iGPU 路线**：符合条件的 Intel 主机可将 Intel iGPU 传递给 Windows VM；最终 Panther Lake 产品支持范围仍需按具体硬件、BIOS 与 PoC 验证。  
  https://docs.olares.com/1.12.5/use-cases/windows-intel-gpu-passthrough.html

**对外收敛措辞**：`A full Olares AI Box with files, sync, sharing and Windows VM capabilities—not a single-purpose meeting appliance.`  
副标题可为简洁性使用 `NAS and Windows VM capabilities`，正文至少有一处展开为具体能力。

## 11. 其他内部判断，不作外部事实

- “去年 SOTA 能力在今年缩到约 10% 模型尺寸”是内部观察与规划假设，不是可直接对外引用的行业定律。
- “约 7B 模型在明年达到今天 Qwen 27B 级质量”涉及具体尺寸、质量与时间，尚无公开证据支持，只能作为产品路线假设，不能写成确定预测。
- 对外可用的收敛措辞：`Planning thesis: as 7B-class models approach today's 27B-class quality, the same installed base can move from voice workflows to agentic workloads.`
- AI 路线图只讲工作负载演进：`NOW — Private Meeting AI → NEXT — Smart Home voice → LATER — Personal Agent`。完整 Olares 平台能力已在副标题与右中产品价值中说明，不在路线图重复。

该判断可用于产品规划和谈判，但在获得真实 Panther Lake PoC 前，不应写成已验证结论。

## 12. 页面叙事与排版笔记

- 第 24 页证明 Audio 是高价值付费场景；第 26 页是覆盖多场景的 B70 通用方案；本页是在完整 Olares AI Box 上，以 Private Meeting AI 作为 Panther Lake 当前主打工作负载，不能把整机写成单用途会议盒。
- 页面采用左侧三段 rail + 右侧两列、三行结构；六个区块不是章节名，而是连续回答“市场—缺口—当前适配—完整产品—采集生态—扩展路线”的论证句。
- 敏感职业统一使用具体人群：`lawyers, doctors, salespeople and journalists`；不混用 legal / medical 等行业分类。
- 采集生态对外写为 `From IoT capture devices to meeting software: an open ecosystem feeding one local knowledge base.`；使用 open 而非 thriving，避免把 planned adapters / connectors 写成已经成熟繁荣的生态。
- 模型表下只保留一句产品结论：`Private Meeting AI requires a five-stage local pipeline; the three required stages target Panther Lake NPU / CPU without a discrete GPU.`；OpenVINO / Slipbox 证据留在资料页，不再塞入主画面。
- 右中产品价值收敛为三项：**Intel SoC 让团队经济性成立**（`$999–1,599` AI Box vs 五人三年 `$3,600` Plaud 云订阅）→ **Olares 让方案开箱即用**（预集成模型、随时随地访问、团队协作、身份权限、应用沙盒）→ **机构控制的隐私与知识主权**。
- TCO 对外可写约 `10–16 months` 或 `roughly one-year hardware payback`，但必须保持硬件 vs 订阅口径，双方排除采集设备；不承诺软件永久免费，也不把目标价写成已发布售价。
- 异构执行以 Panther Lake PoC 为准，不把平台 TOPS 直接换算成 LLM 速度。
- 本地处理只能表述为减少第三方数据暴露、帮助机构控制驻留和访问，不能写成“本地即合规”。
- TicNote 本地加密回传是联合集成目标，不是已上线能力；已确认合作端点仅包括 TicNote 卡片和 Pods，其他采集形态是 planned adapters。
- 扩展路线从 Private Meeting AI 起步：当前负载结构匹配 Panther Lake；下一步复用常在线盒子和本地语音栈进入 Smart Home voice；未来随模型质量和长上下文 prefill 改善，复用装机基础进入 Personal Agent。
