# AGENTS.md — Olares 推广/SEO/内容工作区

> 这是 `seo` 工作区的**索引与入口**，读者是在此做 Olares 推广的 Agent（SEO 竞品报告、落地页、对比文、GEO 内容、社媒文案）。**写任何 Olares 相关内容前先读 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)**——产品认知、品牌口径、写作规范、基本事实、保密红线都在那里。

## Olares 一句话

Olares 是**个人云操作系统**——介于"个人电脑（PC）"与"公有云"之间的第三形态（随时随地在线，硬件与数据完全归用户），**核心用例是跑 Personal Agent**。品牌叙事在升级：**From a Self-Hosted, Personal Cloud OS → a Natural-Language-Driven, Agent-Native OS.** 完整口径（认知/品牌/写作/事实/红线）见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

## 两条主线

| 主线 | 文档 | 回答 |
|------|------|------|
| 1. 方向（事实→洞见）| [directions.md](/Users/pengpeng/seo/directions/directions.md) | 往哪打：7 个方向的市场事实与洞见 |
| 2. 场景（产品进度）| [scenarios.md](/Users/pengpeng/seo/scenarios/scenarios.md) | 我们正在做什么：Q2 八大场景 |

> 底座认知见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)；内容方法论＝seo-content skill（产出落 [content/](/Users/pengpeng/seo/content/README.md)）已就位；跨报告可执行 backlog 待建。

## 配套资产（都在 `directions/` 下）

**归类按"能否自己拥有"**：`market`＝可自部署开源应用、`model`＝开源模型、`commerce`＝闭源商业产品/API（含 OpenAI/Anthropic/Gemini 等闭源模型）、`hardware`＝硬件/NAS、`privacy`＝隐私安全、`tech`＝底层技术栈/自建单一工具、`iot`＝闭源家居/穿戴硬件与生态（方向 7，开源平替本体仍归 market）；不重复登记。

- Market 应用清单 + 每个应用的竞品报告 → [market/apps.md](/Users/pengpeng/seo/directions/market/apps.md)（约 175 个应用）与 [market/reports/](/Users/pengpeng/seo/directions/market/reports)
- 开源模型清单 + 每模态调研 + 逐型号报告 → [model/models.md](/Users/pengpeng/seo/directions/model/models.md)（11 模态章，只收开源可本地跑的 2026 near-SOTA 型号）、[model/research/](/Users/pengpeng/seo/directions/model/research) 调研底稿与 [model/reports/](/Users/pengpeng/seo/directions/model/reports)（research/reports 两级、11 章：01-llm…11-omni）
- 商业付费 AI/SaaS 竞品清单 + 报告 → [commerce/products.md](/Users/pengpeng/seo/directions/commerce/products.md)（约 54 份，17 类；另含若干 ⬜ 待调研 对标）与 [commerce/reports/](/Users/pengpeng/seo/directions/commerce/reports)
- 加速硬件/整机/NAS/独显/Apple 竞品清单 + 报告 → [hardware/devices.md](/Users/pengpeng/seo/directions/hardware/devices.md)（**一行一个具体产品**：AI SoC / RTX 5090 Mobile 游戏本 / ROG NUC / ≥24GB dGPU / 工作站 / AI NAS（含高端发烧）/ 企业·机架·商用 NAS / 个人云·NAS OS 竞品 八组，两条信息＝买 Olares One vs 在已购设备装 Olares）；芯片/品类 deep-research 在 [hardware/research/](/Users/pengpeng/seo/directions/hardware/research)（**按 `<NN-组>/` 分目录，共 8 份 + gap-analysis**：01-ai-soc 的 amd-ryzen-ai-max/nvidia-gb10/apple-m-series、02-5090-laptops、03-rog-nuc、04-dgpu、06-ai-nas（含高端）、07-enterprise-nas）；Semrush 报告在 [hardware/reports/](/Users/pengpeng/seo/directions/hardware/reports)（**按 `<NN-组>/<细类>/` 分目录**：GPU per-model、各 AI NAS、08-nas-os 的 NAS OS、nvidia-dgx、apple-silicon 等保留；**19 份已归档** `reports/_archived/`——品牌 13 + 传统 NAS 5 + 综述 1；产品级报告走 backlog）。**口径：Olares 跨平台（Linux x86/ARM、macOS 含 Apple Silicon、Windows WSL2），"ARM not supported" 只限裸机 ISO；Olares One 只是选了 x86+NVIDIA；GPU 加速 NVIDIA 最成熟、AMD（含 Ryzen AI Max APU 经 ROCm）/Intel 核显亦支持、唯 Apple GPU 不被加速——别再写"Mac/ARM 不能装 Olares"或"仅 NVIDIA"（详见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md) 安装平台矩阵）**
- 隐私/安全竞品清单 + 报告 → [privacy/services.md](/Users/pengpeng/seo/directions/privacy/services.md)（10 份）与 [privacy/reports/](/Users/pengpeng/seo/directions/privacy/reports)
- 技术栈词库（方向 6，长尾/非主推）+ 自建工具报告 → [tech/tech-stack.md](/Users/pengpeng/seo/directions/tech/tech-stack.md) 与 [tech/reports/](/Users/pengpeng/seo/directions/tech/reports)（headscale、frp；商业方 Tailscale/Ngrok 归 commerce）
- IoT/家居/穿戴竞品清单 + 报告（方向 7）→ [iot/iot.md](/Users/pengpeng/seo/directions/iot/iot.md)（2 大类/22 细类，只收面向海外市场的硬件/生态品牌）；品类 deep-research 调研底稿在 [iot/research/](/Users/pengpeng/seo/directions/iot/research)（系统章 smart-home-systems/health-platforms；硬件章 voice-hub/smart-speakers/cameras/home-security/locks-doorbells/ai-recorders/wearables/smart-lighting/smart-plugs/thermostats/sensors-hubs/robot-vacuums/smart-appliances/smart-tv/baby-monitors/pet-cameras/safety-trackers/connected-cars/energy-monitors/smart-glasses），针对关键词的 brand-seo 报告落 [iot/reports/](/Users/pengpeng/seo/directions/iot/reports)

## 研究流程与参考

- **SEO 竞品研究流程**：品牌/SaaS 用 `.cursor/skills/brand-seo-research/`（四阶段模板）；开源模型用 `.cursor/skills/model-seo-research/`（VRAM 可跑性/许可/引擎组合词/GEO 抢发）。
- **通用深度调研**：非"纯 Semrush 数字"的多源综合（理解领域/公司/技术、行业综述、技术选型、政策/竞品格局）用 `.cursor/skills/deep-research/`（并行子代理+引证登记+反向复核），产出落 [research/](/Users/pengpeng/seo/research/README.md)。
- **内容生产（主线 2）**：把研究里的高机会词写成对比/替代文（X alternative、X vs Y、best self-hosted X）用 `.cursor/skills/seo-content/`，产出落 [content/](/Users/pengpeng/seo/content/README.md)。
- **参考资料** → `reference/`：[olares-500-keywords-analysis-2026-07-03.md](/Users/pengpeng/seo/reference/olares-500-keywords-analysis-2026-07-03.md)（我们之前的 500 词分析）、[yiguo-keyword-plan-2026-07-03.md](/Users/pengpeng/seo/reference/yiguo-keyword-plan-2026-07-03.md)（翼果给的关键词方案）。

> 事实型数字（版本、规格、定价）会随时间变化，**引用前以官网/文档为准**。
