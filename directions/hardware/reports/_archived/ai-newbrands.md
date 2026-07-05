# AI NAS 新兴品牌调研报告（Deep Research 验证）
> 来源：Deep Research 113个agent，688次工具调用，2026-07-02
> 覆盖：深度调研验证通过的 AI NAS 新兴品牌 + 传统厂商 AI 动作

---

## 一、新发现品牌（之前列表遗漏）

### 极空间 ZSpace（zspace.cn）

| 指标 | 数据 |
|------|------|
| 域名 | zspace.cn |
| SEMrush Rank | 471,217 |
| 月自然流量（美国） | 3,070（主要是中文） |
| 发布时间 | 2025年10月15日 |

**产品线：**
- **Z425**（¥7,999）：Intel Core Ultra 5 225H，8盘位（4 SATA + 4 M.2，最高152TB），83 TOPS AI算力（NPU 13 TOPS + Arc Graphics 130T 63 TOPS + CPU 7 TOPS）
- **T6**（¥7,999）：另一旗舰型号
- **Z2 Ultra**（¥1,899）：入门 AI NAS

**核心 AI 功能：**
- "AI Space"：自然语言语义搜索（图片/视频/音频），**全部本地计算，不上传云端**
- 官方原文：「所有数据本地部署、本地计算、本地呈现、从不上传云端」
- 可选接入 DeepSeek V3（独立功能）

**SEO 关键词数据：**

| 关键词 | 量 | KD | 备注 |
|--------|----|----|------|
| zspace nas | 20 | 0 | 新兴，英文市场空白 |
| 极空间 nas | — | — | 中文市场 |

**Olares 对比角度：**
- 极空间定位和 Olares One 高度重叠：都是本地 AI + 不上云 + 硬件+软件捆绑
- 极空间偏向存储为主，Olares 偏向 OS/应用生态
- 极空间 Z425 价格（¥7,999）远高于 Olares One，但算力（83 TOPS）更强

---

### 小米智能存储（xiaomi.com）

| 指标 | 数据 |
|------|------|
| 发布时间 | 2026年7月1日（众筹开启） |
| 价格 | ¥2,299（4TB）/ ¥2,899（8TB）/ ¥4,699（16TB） |
| 众筹渠道 | 小米商城 + 小米有品 |

**SEO 关键词数据：**

| 关键词 | 量 | KD | 备注 |
|--------|----|----|------|
| 小米 nas | 170 | **23** | ⭐⭐ 中文低KD |
| xiaomi nas | 20 | 0 | 英文新兴词 |

**Olares 对比角度：**
- 小米主打小米生态集成，Olares 支持 MiGPT 等小米接入方案
- 小米 NAS 价格亲民（¥2,299起），定位大众消费市场

---

## 二、已有品牌的 AI 能力验证（Deep Research 纠错）

### 纠错：被否决的说法

| 品牌 | 被否决的说法 | 投票 |
|------|------------|------|
| QNAP | TS-AI642 的具体 NPU TOPS 数字 | 0-3 否决 |
| UGREEN | 96 TOPS 算力数字 | 0-3 否决 |
| TerraMaster | "全球首款 AI 原生 NAS" | 0-3 否决 |

### 验证通过的 AI 功能

| 品牌 | 验证通过内容 | 置信度 |
|------|------------|--------|
| Synology | DSM 7.4 AI Console：Embedding/OCR/STT/图像描述4个本地GPU模型 | 高（3-0） |
| Synology | Computex 2026 发布 DSM Agent | 高（3-0） |
| QNAP | TS-AI642 使用 Rockchip RK3588 ARM SoC（非x86） | 高（3-0） |
| UGREEN | Uliya 本地 AI 助手（不上云）+ AI Album（本地照片智能分类） | 高（3-0） |
| TrueNAS | truenas.com/ai 定位，vLLM 可安装，支持 RAG/LLM 存储 | 高（3-0） |
| Unraid | 本地 AI 平台定位，3700+ Docker模板，含 Ollama/ComfyUI/OpenClaw | 高（3-0） |

---

## 三、2026年 AI NAS 市场总结

**市场分化为两条轨道：**

1. **传统 NAS 厂商 AI 化**（Synology、QNAP、TrueNAS、Unraid）：在现有平台上叠加本地 AI 推理层
2. **新兴 AI-Native NAS**（UGREEN、极空间、小米）：硬件从零开始针对 AI 工作负载设计

**核心架构趋势：**
- 从云端依赖 → 完全本地推理（NPU/GPU 集成 SoC）
- 主流 SoC：Rockchip RK3588、Intel Core Ultra、AMD Ryzen Embedded
- 中国市场：2025 年下半年至 2026 年多品牌集中发布，竞争激烈

**Olares 的差异化定位：**
- 极空间/UGREEN = 硬件为主，OS/应用生态较弱
- Synology/QNAP = 应用生态强，但 AI 需要额外付费 GPU 卡
- Unraid/TrueNAS = 面向技术用户，门槛高
- **Olares = 零配置 AI 全栈（应用商店 + 本地推理 + 远程访问 + 开源免费）**

---

*注：以上数据基于 Deep Research 113个Agent验证，部分中文 NAS 品牌英文 SEO 数据极少，SEMrush 美国数据库无法全面反映实际市场规模。*
