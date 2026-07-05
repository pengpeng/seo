# Apple Silicon（Mac Studio / Mac Mini / MacBook）本地 AI 调研
> SEMrush US | 关键词数据待跑 | 来源：Apple 官方公开规格（快照，引用前需核实）

## 定位

Apple Silicon 的**统一内存架构**是目前消费端 LLM tokens/s 最高的方案，GPU/CPU 共享大内存池，128GB Mac Studio 单机可跑需要"服务器显卡集群"的模型。Mac 用户懂本地 AI、但缺"多应用 + 远程访问 + 备份"的私有云层——正是 Olares 的位置。Mac Studio / Mac Mini 是 Olares 的第二重点人群。

## 规格与本地 LLM 能力（公开快照）

| 型号 | 芯片 | 内存 | 内存带宽 | 价格 | LLM 能力 | 代表速度 |
|------|------|------|---------|------|---------|---------|
| **Mac Mini M4** | M4（GPU 10核） | 16/32GB | 120 GB/s | $799 | ⭐⭐⭐ | 8B: ~30 tok/s |
| **Mac Mini M4 Pro** ⭐甜品款 | M4 Pro（GPU 20核） | 24/48/64GB | **273 GB/s** | $1,399/1,999 | ⭐⭐⭐⭐ | 70B Q4 可跑 |
| **MacBook Air M4** | M4 | 16/32GB | 120 GB/s | $1,099+ | ⭐⭐⭐ | 13B 流畅 |
| **MacBook Pro M4 Pro** | M4 Pro（GPU 20核） | 24/48GB | 273 GB/s | $1,999+ | ⭐⭐⭐⭐ | 30B 流畅 |
| **MacBook Pro M4 Max** | M4 Max（GPU 40核） | 64/128GB | **546 GB/s** | $3,499/5,500+ | ⭐⭐⭐⭐⭐ | 70B FP16 可跑 |
| **Mac Studio M4 Max** ⭐桌面 LLM 王者 | M4 Max（GPU 40核） | 64/128GB | **546 GB/s** | $3,699 | ⭐⭐⭐⭐⭐ | 70B+ FP16 |

**关键数据（公开快照）：**
- Mac Mini M4 Amazon 月销 10,000+（2026/2），Mac 总销量同比增 13%（Q2 2025）
- $1,799 的 MacBook Pro M4 Pro 32GB 可跑 33B，而任何同价消费级 NVIDIA 独显显存都不够装
- 双 DGX Spark 互联才能跑 405B，Mac Studio M4 Max 128GB 单机就能跑 70B FP16

## 关键词数据（Semrush 待跑）

候选词（跑 `phrase_these` / `phrase_related` / `phrase_questions`）：
- 型号词：`mac studio` / `mac mini m4` / `mac studio m4 max` / `mac mini m4 pro`
- 本地部署/引擎词：`mac studio local llm` / `mac mini ollama` / `run llm on mac` / `apple silicon llm` / `mac studio 128gb llm` / `llm mac vs pc`
- 对比/替代词：`mac studio vs dgx spark` / `mac mini vs rtx 5090 llm` / `mac studio vs rtx pro 6000` / `best mac for local ai`
- 问题词：`can mac mini run ollama` / `how much ram for local llm on mac`

## Olares 关联角度（待补）

- Mac 有算力、缺私有云层：Olares（远程访问 + 多应用 + 备份）补齐 Mac 本地 AI 的"服务化"短板。
- `mac studio vs dgx spark` 对比加 Olares One/OS 作第三选项（成本叙事）。

## 核心洞见（待补）

- 数据跑完后补：Mac 本地 LLM 词的量与 KD、Mac 用户与 Olares 的重叠度、`mac + olares` 切入词、GEO 窗口。

---
*规格为公开快照，引用前需核实；关键词量/KD/CPC 待 Semrush 重跑（型号作 brand，见 [.cursor/skills/brand-seo-research](/Users/pengpeng/seo/.cursor/skills/brand-seo-research/SKILL.md)）。*
