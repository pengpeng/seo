# commerce/ — 商业付费 AI / SaaS 竞品与报告

这里集中管理**用户已经在付费的商业 AI / SaaS 产品**（OpenAI、Midjourney、ElevenLabs、Zapier、Proton 等），以及每个产品的 brand-seo-research 报告。对应 [directions.md](/Users/pengpeng/seo/directions/directions.md) 方向 1，结构对齐 [market/](/Users/pengpeng/seo/directions/market)、[model/](/Users/pengpeng/seo/directions/model)。

## 结构

- [products.md](/Users/pengpeng/seo/directions/commerce/products.md)：产品清单，按 **5 大类 / 57 细类** 分组，每条标注域名、公司、达标依据、Olares 平替方案与报告状态（⬜ 待调研）。
- [products-appendix.md](/Users/pengpeng/seo/directions/commerce/products-appendix.md)：出范围/次级/纯开发者向/被收购/未达门槛项。家居 IoT / 可穿戴已独立为 [iot/](/Users/pengpeng/seo/directions/iot)（方向 7）。
- [reports/](/Users/pengpeng/seo/directions/commerce/reports)：每个产品一份报告，按大类/细类归入两级目录。

### reports/ 目录树（编号英文 slug）

已按 `products.md` 的 **57 细类** 预建好全部子目录（空目录以 `.gitkeep` 占位），写新报告时直接落到对应细类即可，无需新建目录。

- `01-model/` — 模型层：`frontier-labs/`(1)、`gateway/`(2)、`aggregator/`(3)、`memory/`(4)、`finetune/`(5)、`observability/`(6)
- `02-creation/` — AI 创作层：`image/`(7)、`video/`(8)、`avatar/`(9)、`3d/`(10)、`design-agent/`(11)、`music/`(12)、`audio-content/`(13)、`voice-tts/`(14)、`voice-meeting/`(15)、`voice-dictation/`(16)、`voice-agent/`(17)、`translation/`(18)、`ocr/`(19)
- `03-application/` — AI 应用层：`ide/`(20)、`coding-agent/`(21)、`vibe-coding/`(22)、`website-builder/`(23)、`low-code/`(24)、`baas/`(25)、`automation/`(26)、`general-agent/`(27)、`personal-ai/`(28)、`cx-agent/`(29)、`search/`(30)、`writing/`(31)、`companion/`(32)、`vertical-legal/`(33)、`vertical-medical/`(34)、`vertical-finance/`(35)、`enterprise-rag/`(36)
- `04-productivity/` — 生产力 & 协作：`notes/`(37)、`office-suite/`(38)、`im/`(39)、`email/`(40)、`project-management/`(41)、`nocode-db/`(42)、`crm/`(43)、`ecommerce/`(44)、`helpdesk/`(45)、`finance/`(46)、`iam/`(47)、`monitoring/`(48)、`web-analytics/`(49)、`paas/`(50)
- `05-storage-privacy/` — 存储 / 开发者 / 家居 / 隐私：`cloud-storage/`(51)、`photos/`(52)、`code-hosting/`(53)、`e-signature/`(54)、`design-collab/`(55)、`password/`(56)、`privacy-vpn/`(57)
- `appendix/` — 出主清单范围的报告（推理 API / 向量库 / Embedding / 数据标注 / 模型平台 / 降级观察项），扁平不再细分

> 编号 `(N)` 对应 `products.md` 的细类序号。开源平替报告（如 continue-dev、vaultwarden）就近放在其商业对标所在的细类子目录。

## 命名约定

- 报告命名 `<brand>.md`（无前缀、无日期，git 记录变更历史），路径为 `reports/<NN-大类>/<细类>/<brand>.md`。
- 例：`reports/03-application/vibe-coding/lovable.md`、`reports/05-storage-privacy/privacy-vpn/tailscale.md`。

## 清单怎么来的

商业竞品没有 `beclab/apps` 那样的 manifest 仓库，所以 `products.md` **手工维护**、不写生成器。报告中的流量数据是历史快照，**以后会用 Semrush 重跑**。

## 怎么用

- 写/重跑某个产品报告：走 `.cursor/skills/brand-seo-research/` 流程（以产品官网为 brand）。**重写前先读现有同名报告，保留并去重旧洞见，不认可的旧结论可明确指出**。产出落到该产品所属细类子目录 `reports/<NN-大类>/<细类>/<brand>.md`，再更新 `products.md` 的平替/状态。
- 品牌与保密红线见 [basic/olares.md](/Users/pengpeng/seo/basic/olares.md)。

> 通用切入点：`X alternative` / `self-hosted X` / `X pricing` / `X vs <Olares 平替>`——Olares Market 的自托管应用 + 本地模型让"用开源方案替代付费 SaaS"成为落地路径。
