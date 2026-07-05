# dig-15 · 低代码 / 建站 / BaaS 赛道 · 发现蒸馏笔记

**AS_OF=2026-07-04** · 只做发现+财务，不做最终分类。门槛：ARR>$50M｜估值>$200M｜融资>$20M｜大厂旗舰。

## Sources（节选）
SEC 10-K/8-K（Wix/Squarespace/Block/Alphabet/Amazon）/ 官方 PR / TechCrunch/CNBC/BusinessWire / GetLatka/Tracxn/Sacra/CBInsights。

## Products

### 1. 建站 / 网站构建器
| 名称 | 公司 | 开源? | 财务 | 命中 | Olares 平替 |
|------|------|------|------|------|------------|
| **Wix** | Wix(Nasdaq:WIX) | 否 | ARR $1.836B；收入 $1.99B；市值 ~$1.9–2.6B | ARR✓·上市旗舰 | WordPress✅ / Ghost✅ |
| **Base44**(Wix 收购) | Wix | 否 | 收购 ~$80M+earn-out；ARR ~$59M→$100M→$150M | ARR✓ | Appsmith⏳ / NocoBase⏳ |
| Squarespace | Permira 私有化 | 否 | ARR $1.18B；收购估值 $7.2B | ARR✓估值✓ | WordPress / Ghost |
| Webflow | Webflow | 否 | ARR $212.5M；估值 $4B；融资 $336M | 全中 | WordPress / Ghost / Directus⏳ |
| Framer | Framer | 否 | ARR $50M；估值 $2B；融资 $100M | 全中 | WordPress / Ghost / Penpot |
| Weebly | Block(NYSE:XYZ) | 否 | 母公司 Block 收入 $24.2B；独立 ARR 未披露 | 大厂旗舰 | WordPress / Ghost |
| Carrd | Carrd | 否 | ARR ~$2M；融资 $2M | **未达标** | — |

### 2. 无代码 App / 自动化构建
| 名称 | 公司 | 开源? | 财务 | 命中 | 平替 |
|------|------|------|------|------|------|
| Bubble | Bubble Group | 否 | ARR ~$74.2M；融资 $106.3M | ARR✓融资✓ | NocoBase⏳ |
| Glide | Glide | 否 | 融资 $23.75M；ARR $3.7M(或~$42M[u]) | 融资✓ | NocoBase / NocoDB✅ |
| Softr | Softr | 否 | 融资 $15.7M；ARR ~$15M[u] | **未达标** | NocoBase / NocoDB |
| Adalo | Adalo | 否 | 融资 $9.7M；ARR ~$24M[u] | **未达标** | — |
| FlutterFlow | FlutterFlow | 否 | ARR $25.2M；融资 $26–30M；估值 ~$170M | 融资✓ | Supabase 自托管 |
| Zapier Interfaces | Zapier | 否 | 母公司 ARR $420M；估值 $5B | ARR✓估值✓ | n8n✅ / Appsmith |

### 3. 内部工具 / 低代码平台
| 名称 | 公司 | 开源? | 财务 | 命中 | 平替 |
|------|------|------|------|------|------|
| **Retool** | Retool | 否 | ARR $120M；估值 $3.2B；融资 $141–165M | 全中 | Appsmith⏳ / Budibase / ToolJet / NocoBase |
| Appsmith | Appsmith | **是**(Apache2.0) | 融资 $51.5M；ARR ~$10M[u] | 融资✓ | **Market 已列⏳（双形态）** |
| Budibase | Budibase | **是** | 融资 $9.25M | **未达标** | 候选上架 |
| ToolJet | ToolJet | **是** | 融资 $6.15M | **未达标** | 候选上架 |
| Superblocks | DayZero | 否 | 融资 $61M；估值 $260M | 估值✓融资✓ | Appsmith / Budibase |
| Mendix | Siemens | 否 | 收购 $730M；ARR ~$170M[u] | ARR✓·大厂旗舰 | Appsmith / NocoBase |
| OutSystems | OutSystems | 否 | 收入 >€500M；估值 $9.5B；融资 $572–803M | 全中 | Appsmith |
| Microsoft Power Apps | Microsoft | 否 | Power Platform $3B+ 业务；单体未拆分 | 大厂旗舰 | Appsmith / NocoBase / n8n |

### 4. BaaS / 后端即服务（偏纯开发者向 → Lead 倾向移附录）
| 名称 | 公司 | 开源? | 财务 | 命中 | 平替 |
|------|------|------|------|------|------|
| **Supabase** | Supabase | **是**(核心开源) | ARR ~$170M；估值 $10.5B；融资 >$1B | 全中 | Supabase 自托管 / Hasura⏳ / Directus⏳ |
| Firebase | Google | 部分 | GCP run-rate >$70B；未单独披露 | 大厂旗舰 | PocketBase / Appwrite 自托管 |
| Appwrite | Appwrite | **是** | 融资 $37M；ARR ~$7M[u] | 融资✓ | 强候选上架 |
| Nhost | Nhost | 部分 | 融资 $3M | **未达标** | Hasura / Supabase 自托管 |
| PocketBase | 个人开源 | **是**(MIT) | 无商业指标；59K+ stars | **未达标** | 轻量 BaaS 候选 |
| AWS Amplify | AWS | 否 | AWS $128.7B；未拆分 | 大厂旗舰 | Appwrite / Supabase 自托管 / Directus |
| Convex | Convex | 部分 | ARR $11M；融资 $53.5M | 融资✓ | Supabase 自托管 / PocketBase |

## Olares 平替速查
WordPress✅ / Ghost✅（建站）；Appsmith⏳ / NocoBase⏳ / NocoDB✅（内部工具/App）；n8n✅（自动化）；Strapi❌($49.8M 融资，headless CMS 候选）；Budibase/ToolJet/Appwrite/PocketBase/Supabase 自托管❌（Market 缺）。

## Gaps / 洞见
- **AI vibe coding 正撕裂四分类**：Wix/Base44、Webflow AppGen、Superblocks Clark、Retool AppGen 模糊了「建站/App/内部工具」边界；Olares 打「自托管+拥有数据+开源替代」横切词（`retool alternative` KD 极低已验证）。
- **BaaS 子类**：Supabase 一家独大；Appwrite 唯一融资达标独立 BaaS；偏纯开发者向 → 建议整体移 commerce 附录。
- Base44 已在现稿 #24 vibe coding，本笔记锚定 Wix 集团「建站/App 双轨」，供 Lead 决定归建站还是 vibe coding。
- 财务张力：Glide/Adalo/Mendix/OutSystems 估值 ARR 多第三方 [u]；Weebly 独立财务停披露（转 Square/Block 或历史品牌）。
