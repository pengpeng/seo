# dig-14 · 成熟 SaaS 开源自托管平替映射 · 发现蒸馏笔记

**AS_OF=2026-07-04** · 只做平替映射+佐证，不做最终分类。Market 覆盖以 `directions/market/apps.md` 为准。

## Sources
GitHub 仓库元数据（stars/license/push） / OSSAlt / OpenAlternative / selfhosting.sh / 官方文档 / Olares Market 清单。

## Mappings（商业 SaaS → 开源平替 | 许可 | 成熟度 stars | Market? | 备注）

| 商业 SaaS | 开源平替 | 许可 | Stars | Market | 备注 |
|---|---|---|---|---|---|
| **Salesforce**(CRM) | Twenty / SuiteCRM | AGPL-3.0 | ~52K/~5.5K | **Twenty ✅** | Twenty 现代 GraphQL CRM；SuiteCRM 功能最全但 UI 旧 |
| **HubSpot** | Twenty / EspoCRM (+Mautic 营销) | AGPL/AGPL/GPL | ~52K/~3K/~7K | Twenty ✅ / **Odoo ✅**(更广 ERP) | 无单一平替；营销自动化需 Mautic+Listmonk 组合 |
| **Shopify**(电商) | Medusa / Saleor | MIT/BSD-3 | ~34K/~23K | **Medusa ✅** | headless 电商 API；storefront/支付/物流需自建 |
| **Snowflake·Databricks**(数据云) | ClickHouse + Trino (+Metabase BI) | Apache/Apache/AGPL | ~48K/~13K | **Metabase ✅**(数仓引擎待上架) | **无 1:1 平替**，需组合栈；Doris/DuckDB 可选 |
| **Okta**(IAM/SSO) | Keycloak / ZITADEL | Apache/AGPL | ~35K/~14K | 均❌ | Keycloak 企业事实标准；Authentik(~21K)/Authelia 轻量 |
| **Zoom**(视频会议) | Jitsi Meet / Nextcloud Talk | Apache/AGPL | ~30K | Jitsi❌ / **Nextcloud ✅** | Talk 为 Nextcloud 模块；千级并发需 SFU 集群 |
| **Zendesk**(客服工单) | Chatwoot / Zammad | MIT/AGPL | ~34K/~5.7K | 均❌ | Chatwoot 全渠道+AI；Zammad 传统工单；FreeScout 更轻 |
| **QuickBooks**(财务) | ERPNext / Akaunting | GPL/GPL | ~36K/~8K | **Firefly III ✅**(仅个人理财) | ERPNext 完整复式记账；Akaunting 最接近 QB Online |
| **Vercel**(前端 PaaS) | Coolify / Dokploy | Apache/部分 source-avail | ~53K/~35K | **Coder ✅**(CDE 非 PaaS) | Coolify/Dokploy Git 部署；无全球 Edge/Serverless |
| **ServiceNow**(ITSM) | GLPI / iTop | GPL/AGPL | ~6K/~1.1K | 均❌ | 覆盖 ITSM/CMDB 子集；距低代码平台差距大 |
| **Datadog**(可观测) | OpenObserve / SigNoz | AGPL/MIT | ~19K/~28K | **Netdata ✅ / Grafana ✅**(栈不同) | OpenObserve 单二进制；SigNoz OTel 原生 |
| **Twilio**(CPaaS) | Fonoster / jambonz | MIT/MIT | ~8K | 均❌ | 仍需自备运营商/SIP trunk，无法 1:1 替代 |
| **DocuSign**(电子签) | Documenso | AGPL | ~10K+ | **✅** | 明确对标 DocuSign |
| **Airtable**(无代码库) | NocoDB / Teable | AGPL/AGPL | ~52K/~15K | **NocoDB ✅ / Teable ✅** | Teable 基于 Postgres 更数据库原生 |
| **Notion**(知识库) | AppFlowy / AFFiNE | AGPL/MIT | ~73K/~70K | **AFFiNE ✅** | AppFlowy 近 Notion 数据库；AFFiNE 文档+白板混合 |
| **Miro**(白板) | Excalidraw | MIT | ~100K+ | **✅** | Penpot✅ 偏 UI 设计 |
| **Google Analytics** | Plausible / Umami | AGPL/MIT | ~27K/~37K | 均❌ | 隐私优先轻量分析 |
| **Mailchimp**(邮件营销) | Listmonk | AGPL | ~17K | **✅** | 缺可视化营销自动化 |
| **Calendly**(预约) | Cal.diy(Cal.com 社区版) | MIT | ~46K | ❌(Market 有 Rallly，非同类) | 2026-04 Cal.com 主仓转私有，cal.diy 全 MIT |
| **GitHub/GitLab**(代码托管) | Gitea / GitLab CE | MIT/MIT-EE | — | 待确认 | — |

### 候选补充
SuiteCRM/EspoCRM(Salesforce/HubSpot)、ERPNext(CRM+会计)、Apache Doris(Snowflake)、DuckDB(单机分析)、Authentik/Authelia(轻量 SSO)、Bagisto/Vendure(Shopify)、Invoice Ninja(发票)。

## Gaps（无好平替 / 需组合 / 留空）
1. **Snowflake/Databricks**：无单一 OSS 覆盖弹性数仓+Spark+治理+MLflow；需 ClickHouse/Doris+Trino/Spark+Airbyte+Metabase 组合。
2. **Twilio**：号码采购/全球 SMS 路由/合规仍依赖运营商，不能 1:1。
3. **ServiceNow**：缺跨部门工作流编排+App Engine+ISV 生态。
4. **HubSpot Marketing Hub**：营销自动化需 Mautic+Listmonk+自建落地页组合。
5. **QuickBooks**：本地化税表/银行直连/CPA 生态弱于 QB。
6. **Zoom Webinar/硬件会议室**：Jitsi 适中小会议，超大规模需 Videobridge 集群。
7. **Shopify 全托管体验**：Medusa/Saleor 为 headless API，摩擦高于一键开店。
8. **Vercel Edge/Serverless**：无全球 Anycast Edge，需 Cloudflare Workers 等另栈。

## Olares 承接优先级（Market 已有 × 平替质量）
- **高**：Salesforce/HubSpot→Twenty、Shopify→Medusa、Airtable→NocoDB/Teable、Notion/Miro→AFFiNE/Excalidraw、DocuSign/Mailchimp→Documenso/Listmonk
- **中**：Zoom→Nextcloud(+Talk)、Snowflake BI 层→Metabase
- **待补 Market**：Zendesk→Chatwoot、Okta→Keycloak、Datadog→SigNoz、Calendly→cal.diy、GA→Umami（高 stars 但未进 Market）
