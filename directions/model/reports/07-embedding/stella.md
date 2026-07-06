# Stella 模型 SEO 关键词调研报告
> SEMrush US | 2026-07-06 | 来源：Dun Zhang / NovaSearch（huggingface.co/NovaSearch/stella_en_1.5B_v5），MIT

> **无独立官网**：Stella 模型通过 HuggingFace（NovaSearch/stella_en_1.5B_v5）分发，无厂商官网；SEO 主战场在第三方内容页（HF 模型卡、MTEB 排行榜、RAG 教程站）。Phase 1 域名报告跳过。

---

## 模型理解（前置）

Stella 是 Dun Zhang（NovaSearch）发布的一组开源英文文本 Embedding 模型，v5 系列包含 **stella_en_1.5B_v5** 和 **stella_en_400M_v5** 两个变体（2024 年 7 月发布），原挂载在 `dunzhang/` 组织下，已迁移至 `NovaSearch/`。1.5B 版本基于 Qwen2-1.5B-instruct 骨干，通过 Matryoshka 表示学习（MRL）训练，支持 512/768/1024/2048/4096/6144/8192 多维度输出（默认 1024d），是当前 **MTEB English 开放权重榜上参数量 <2B 中表现最强**的模型之一（MTEB avg ≈ 65.3），被认为是 OpenAI text-embedding-3-large 与 Cohere Embed v3 的免费自托管替代。论文《Jasper and Stella: distillation of SOTA embedding models》（arXiv:2412.19048，2025.1）详述了蒸馏方法。

| 项目 | 内容 |
|------|------|
| 一句话定位 | 英文文本 Embedding 模型，MTEB <2B 级最强，MIT，128K 上下文，MRL 多维输出 |
| 许可证 | **MIT**（商用友好，无地区限制，可自托管、商业分发） |
| 主仓库 / 分发 | HuggingFace: [NovaSearch/stella_en_1.5B_v5](https://huggingface.co/NovaSearch/stella_en_1.5B_v5)（≈2.5M 全量下载）；Ollama 社区镜像：`Losspost/stella_en_1.5b_v5`（13.3K downloads，未官方支持）；Infinity 推理服务器（Docker，官方推荐） |
| 参数 / VRAM 可跑性 | 1.5B 参数，FP32 加载约 6.2 GB；FP16 约 3.1 GB；**消费级 6–8 GB 显存即可跑**；Olares One（RTX 5090 Mobile 24 GB）满血运行；400M 变体 CPU 亦可 |
| 变体 / 型号 | **stella_en_1.5B_v5**（主力）、**stella_en_400M_v5**（轻量，基于 gte-large-en-v1.5，MTEB ≈ 64.4）；MRL 多维：512/768/1024（默认）/2048/4096/6144/8192 |
| 闭源对标 | OpenAI **text-embedding-3-large**（$0.13/1M tokens）、text-embedding-3-small；Cohere Embed v3；Voyage AI；Google text-embedding-004 |
| Olares Market | 暂无独立条目；可通过 **Infinity 推理服务器（Docker）** 自部署；Dify、AnythingLLM、RAGFlow（均已上架 Olares Market）支持自定义 Embedding endpoint，可接 Infinity 提供的 Stella 服务 |
| 来源 | [HF 模型卡](https://huggingface.co/NovaSearch/stella_en_1.5B_v5)、[arXiv:2412.19048](https://arxiv.org/abs/2412.19048)、[Ollama 社区](https://ollama.com/Losspost/stella_en_1.5b_v5)、[vLLM issue #10119](https://github.com/vllm-project/vllm/issues/10119) |

---

## 关键词扩展（Phase 2）

按月量降序。⭐ = KD < 30 且量 > 0。

### 型号 / 版本词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ⭐ stella_en_1.5b_v5 embedding model | 70 | 16 | $0 | 商业 |
| ⭐ stella_en_1.5b_v5 embedding | 40 | 12 | $0 | 信息 |
| ⭐ stella embedding model | 30 | 0 | $0 | 信息 |
| ⭐ stella_en_1.5b embedding model | 30 | 0 | $0 | 信息 |
| ⭐ stella en 1.5b v5 | 20 | 0 | $0 | 信息 |
| ⭐ stella embeddings | 20 | 0 | $0 | 信息 |
| ⭐ stella_en_400m_v5 | 20 | 0 | $0 | 信息 |
| ⭐ stella 400m | 20 | 0 | $0 | 信息 |
| ⭐ stella en 400m v5 | 10 | 0 | $0 | 信息 |
| ⭐ stella_en_1.5b embedding | 10 | 0 | $0 | 信息 |
| ⭐ stella_en_1.5b_v5 embedding dimension | 10 | 0 | $0 | 信息 |

### 引擎组合词（Olares 机会前哨）

> Stella 暂无官方 Ollama / vLLM 第一方支持，相关组合词搜索量近零——属正常，GEO 抢占机会。

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| stella embedding ollama | 0 | — | — | GEO |
| stella embedding infinity | 0 | — | — | GEO |
| stella embedding docker | 0 | — | — | GEO |
| stella embedding vllm | 0 | — | — | GEO |
| stella embedding python | 0 | — | — | GEO |

### 本地部署 / 硬件词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| ⭐ are api call required for embedding model | 260 | 29 | $0 | 信息 |
| ⭐ local embedding model | 50 | 27 | $0 | 信息 |
| ⭐ matryoshka embedding | 40 | 0 | $0 | 信息 |
| ⭐ lightweight embedding model | 40 | 23 | $0 | 信息 |
| ⭐ best local embedding model | 30 | 0 | $0 | 信息 |
| ⭐ self hosted embedding model | 20 | 0 | $0 | 信息 |
| ⭐ small embedding model | 20 | 0 | $0 | 信息 |

### 对比 / 替代词

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| text-embedding-3-large | 3,600 | 40 | $6.26 | 信息 |
| ⭐ open source embedding models | 170 | 18 | $2.87 | 信息 |
| ⭐ best open source embedding model | 40 | 13 | $0 | 商业 |
| ⭐ best open source embedding models | 40 | 28 | $2.90 | 商业 |
| ⭐ open source text embedding models | 40 | 23 | $0 | 信息 |
| ⭐ openai embedding alternative | 10 | 0 | $0 | 商业 |

### 市场大盘参考词（定位用，非直接攻打）

| 关键词 | 月量 | KD | CPC | 意图 |
|--------|------|----|-----|------|
| sentence transformers | 1,900 | 64 | $8.37 | 信息/商业 |
| mteb leaderboard | 880 | 40 | $0 | 信息 |
| bge m3 | 590 | 47 | $9.32 | 信息 |
| qwen3 embedding | 480 | 47 | $4.07 | 信息 |
| text embedding 3 small | 390 | 25 | $4.43 | 信息 |
| matryoshka representation learning | 320 | 34 | $0 | 信息 |
| ⭐ best embedding model for rag | 140 | 29 | $2.40 | 商业 |
| nomic embed | 140 | 30 | $0 | 信息 |
| fastembed | 210 | 39 | $0 | 商业 |
| ⭐ best embedding model | 210 | 27 | $0 | 商业 |
| ⭐ which embedding model is best for rag | 40 | 16 | $0 | 商业 |
| jina embeddings | 90 | 43 | $0 | 信息/导航 |
| openai text embedding | 90 | 48 | $0 | 商业/导航 |

---

## Olares 关联词（Phase 3）

| 关键词 | 月量 | KD | CPC | Olares 角度 |
|--------|------|----|-----|-------------|
| ⭐⭐⭐ are api call required for embedding model | 260 | 29 | $0 | 直接攻击点：Stella + Infinity 自托管 = 零 API 调用费，数据不出本机；Olares 一键部署 Infinity + RAG 应用链路 |
| ⭐⭐⭐ open source embedding models | 170 | 18 | $2.87 | 开源替换 text-embedding-3-large：成本从 $0.13/1M tokens → $0；MIT 授权可商业集成；Olares 作为部署平台 |
| ⭐⭐⭐ best embedding model for rag | 140 | 29 | $2.40 | RAG 管道核心词；Stella 1.5B MTEB 最优性价比，Olares 上 Dify/RAGFlow + Stella 是本地私有知识库最优组合 |
| ⭐⭐ best open source embedding model | 40 | 13 | $0 | 战略词，KD 极低；内容角度：Stella 1.5B 是 <2B 级最优开源方案，Olares 可一行命令跑 |
| ⭐⭐ local embedding model | 50 | 27 | $0 | 部署叙事：消费级 6GB 显存可跑，Olares One（24 GB）满血运行，隐私数据不离机 |
| ⭐⭐ which embedding model is best for rag | 40 | 16 | $0 | RAG 选型决策词；推荐 Stella 1.5B 作为 RAG 场景 cost-free 首选，通过 Olares + Dify 落地 |
| ⭐⭐ matryoshka embedding | 40 | 0 | $0 | 技术特性词；MRL 支持多维度裁剪（256→8192），存储灵活，适合资源受限的 Olares 私有部署 |
| ⭐ self hosted embedding model | 20 | 0 | $0 | 自托管叙事：Stella MIT + Infinity Docker = 完整自托管方案，Olares 提供容器化基础 |
| ⭐ openai embedding alternative | 10 | 0 | $0 | GEO 抢占：近零量但意图极纯，Stella 是 text-embedding-3-large 最接近的开源替代，Olares 承载部署 |
| ⭐ mteb leaderboard | 880 | 40 | $0 | 流量入口词；排名靠前内容（"MTEB top models 自托管指南"）可带 Stella + Olares 叙事；KD=40 可长期布局 |

---

## Top 关键词（含角色判断）

| 关键词 | 月量 | KD | CPC | 意图 | 角色 | 一句话判断（含 Olares 角度）|
|--------|------|----|-----|------|------|--------------------------|
| open source embedding models | 170 | 18 | $2.87 | 信息 | 主词候选 | KD 极低但量足，商业意图（有 CPC）；是"Stella = text-embedding-3-large 开源替代"叙事入口，Olares 自托管部署是内容落脚点 |
| best embedding model for rag | 140 | 29 | $2.40 | 商业 | 主词候选 | RAG 选型核心词，商业意图强（CPC $2.4）；Stella 1.5B MTEB 最优性价比 + Olares 上 Dify/RAGFlow 是最自然落地方案 |
| are api call required for embedding model | 260 | 29 | $0 | 信息 | 主词候选 | 量 260、KD 29，是"自托管 vs API 付费"决策前置词；Stella + Infinity + Olares = 零 API 调用的完整答案 |
| best embedding model | 210 | 27 | $0 | 商业 | 主词候选 | 量大（210），KD 合理；需在内容中说明"最佳"分场景（英文/多语言/成本），Stella 是纯英文本地场景最优 |
| best open source embedding model | 40 | 13 | $0 | 商业 | 主词候选 | KD 仅 13，战略性商业词；Stella 1.5B 是该问题的最优答案之一，适合作为独立短文主词 |
| mteb leaderboard | 880 | 40 | $0 | 信息 | 次级 | 量大但 KD=40，作竞品大盘参考；可在"MTEB 榜单解读"类内容中嵌入 Stella 叙事 |
| local embedding model | 50 | 27 | $0 | 信息 | 次级 | 中等量，KD 可攻；"local"意图与 Olares 完全契合，作"best open source embedding model"文章的次级词收录 |
| lightweight embedding model | 40 | 23 | $0 | 信息 | 次级 | 指向 Stella 400M / 1.5B 两档；可在部署教程类内容中嵌入 |
| matryoshka embedding | 40 | 0 | $0 | 信息 | 次级 | KD=0 近零竞争；MRL 是 Stella 核心差异化，作技术深度文次级词 |
| which embedding model is best for rag | 40 | 16 | $0 | 商业 | 次级 | 决策词，可并入"best embedding model for rag"簇，作 RAG 专项对比内容次级 |
| open source text embedding models | 40 | 23 | $0 | 信息 | 次级 | 对标"open source embedding models"主词的变体，直接收入同簇 |
| stella_en_1.5b_v5 embedding model | 70 | 16 | $0 | 商业 | 次级 | 模型品牌词中量最大（70）；用于已知品牌用户回流，作导航型次级词 |
| stella embedding model | 30 | 0 | $0 | 信息 | 次级 | 品牌词，KD=0；作各文末"延伸阅读"锚文本 |
| openai embedding alternative | 10 | 0 | $0 | 商业 | GEO | 量极低但意图最纯；Stella MIT 是 text-embedding-3-large 最直接开源平替，抢 AI Overview 问答位 |
| self hosted embedding model | 20 | 0 | $0 | 信息 | GEO | 自托管叙事精准词，量小但 0 竞争；Infinity + Olares 场景直答，适合 FAQ 块 |
| stella embedding ollama | 0 | — | — | — | GEO | 当前近零量；随 Ollama 官方支持 Stella（issue 进行中）量会起，提前布局 GEO |
| stella embedding infinity | 0 | — | — | — | GEO | Infinity 是官方推荐推理服务器；先发内容占位 |

---

## 核心洞见

1. **搜索心智尚未建立，品牌词量极低**：`stella embedding model` 月量仅 30，`stella_en_1.5b_v5` 系列合计约 200，远低于竞品（BGE-M3 590、Qwen3-Embedding 480）。Stella 的搜索流量主要通过"MTEB 榜单"、RAG 教程、HuggingFace 页面间接进入，自身品牌词尚未形成独立搜索心智。对 Olares 的意义：**不宜单独押注 Stella 品牌词，应作为"best open source embedding model"类内容的支柱答案写入**。

2. **消费级 GPU 完全可跑，Olares One 满血运行**：FP32 约 6.2 GB VRAM，FP16 约 3.1 GB，消费级 8 GB 显卡即可部署；Olares One（RTX 5090 Mobile 24 GB）资源充裕；400M 变体 CPU 亦可运行，覆盖更低硬件门槛。**本地部署叙事完全成立**，是 RAG 私有知识库场景的实质性卖点。

3. **MIT 许可证，商用友好，可主推**：无地区限制、无商业分发限制，可作为主推卖点。相比 BGE-M3（Apache 2.0）或部分自定义协议模型，MIT 是最宽松的开源选项之一，便于 Olares 用户在生产环境商业集成。

4. **对 Olares 最关键的 2-3 个词**：
   - `best embedding model for rag`（140/mo，KD 29，CPC $2.4）——RAG 私有知识库场景主词，Stella + Dify/RAGFlow on Olares 是最自然落地路径
   - `open source embedding models`（170/mo，KD 18，CPC $2.87）——"替代 text-embedding-3-large"叙事最宽入口，KD 低、有商业 CPC
   - `are api call required for embedding model`（260/mo，KD 29）——是用户决策前置问题，Stella + Infinity 自托管的完整答案，直接攻击 OpenAI/Cohere 收费痛点

5. **GEO 抢发窗口**：引擎组合词（`stella embedding ollama`、`stella embedding infinity`、`stella embedding docker`）当前近零量，但 Ollama 官方 Stella 一方支持正在讨论（GitHub issue 进行中）、vLLM issue 已开；**现在布局教程类内容，一旦 Ollama 官方支持落地量会迅速起来**。`openai embedding alternative` 量虽仅 10，意图极纯，适合 FAQ 直答块 GEO 抢占。

6. **闭源对标与攻击面**：核心对标 **OpenAI text-embedding-3-large**（3,600/mo，KD 40，CPC $6.26，按 $0.13/1M tokens 计费）。攻击面：① **成本**：高频 RAG 场景下 API 费用不可控，Stella 自托管后边际成本趋零；② **数据隐私**：敏感文档通过 OpenAI API 会离开用户控制，Stella 本地运行数据不出机；③ **速率限制**：OpenAI Embedding API 有 QPS 上限，本地 Infinity 无限制；④ **离线可用**：断网环境 API 不可用，本地 Embedding 无此问题。

7. **与同类 family 关联**：报告对比参见 `07-embedding/nomic-embed.md`（Apache 2.0，多语言，MoE 架构）、`07-embedding/bge-m3.md`（多语言，混合检索）、`07-embedding/qwen3-embedding.md`（Alibaba，支持多语言）。Stella 的差异化定位：**英文单语种、<2B 参数内 MTEB 最高分、MIT 最宽松许可证、MRL 多维输出**；在"纯英文 RAG + 消费级硬件 + 商业可用"场景下是当前最优开源选择。`model/keywords.md` 中"open source embedding alternative"大类与 Stella 高度重叠，建议在该类内容中将 Stella 列为首推。

---

*数据来源：SEMrush US（phrase_these、phrase_fullsearch、phrase_questions、phrase_related）| 2026-07-06*
*搜索量为美国月均；技术类产品全球量通常为美国的 3-5 倍。*
