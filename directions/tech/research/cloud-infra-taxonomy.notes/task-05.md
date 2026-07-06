---
task_id: 05
role: 身份/安全分析师
status: complete
sources_found: 4
---

## Sources
[23] authhost — Authentik vs Authelia vs Keycloak 2026 | https://authhost.de/en/blog/authentik-vs-authelia-vs-keycloak | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[24] Infisical — Open Source Secrets Management for DevOps 2026 | https://infisical.com/blog/open-source-secrets-management-devops | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[1] CNCF — Graduated and Incubating Projects | https://www.cncf.io/projects/ | Source-Type: official | As Of: 2026 | Authority: 10/10
[5] Google Cloud — 三云服务对照表 | https://docs.cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison | Source-Type: official | As Of: 2024-12 | Authority: 9/10

## Findings
- SSO/IAM：Keycloak 是唯一进 CNCF Incubating(2023-04-10)的 IdP（企业级，重、Java/Quarkus）；ZITADEL(Go，云原生、多租户)与 Authelia(Go，25MB 轻量 forward-auth 网关)为主流开源替代。[23]
- Authelia 定位反向代理前置认证网关(OIDC 认证、无 SAML/LDAP server)，极轻(idle ~25MB)；常配 LLDAP 做后端目录。[23]
- 密钥：HashiCorp Vault 是成熟标准但已转 BSL 许可；OpenBao(Vault 的 MPL-2.0 社区分叉)与 Infisical(MIT，开发者友好)为开源替代；External Secrets Operator 是 CNCF 项目负责把外部密钥同步进 K8s。[24]
- 策略：OPA(Open Policy Agent)与 Kyverno 均为 CNCF Graduated 策略引擎。[1][24]
- 运行时安全：Falco 是 CNCF Graduated，K8s 运行时威胁检测事实标准；cert-manager、SPIFFE/SPIRE 亦为 Graduated。[1][24]
- 公有云对应：IAM AWS IAM/Identity Center↔Microsoft Entra ID↔Cloud IAM/Identity Platform；密钥 AWS Secrets Manager·KMS↔Azure Key Vault↔Google Secret Manager·Cloud KMS；策略 AWS Config/Organizations↔Azure Policy↔GCP Org Policy。[5]

## Deep Read Notes
### Source [23]: Authentik vs Authelia vs Keycloak
Key data: Keycloak 唯一 CNCF Incubating(自 2023-04-10)、~34k star、idle RAM ~1.25GB；Authelia idle ~25MB、Apache-2.0、~27.7k star；Authentik MIT。
Key insight: Olares 选 Authelia+LLDAP 是"轻量 forward-auth"路线，而非 Keycloak 式重型企业 IdP。
Useful for: 身份/安全大类 SSO 行 + Olares 平替解读。

## Gaps
- 相反主张：Authelia 缺 SAML/多租户/完整 IdP 能力，企业级场景需 Keycloak/ZITADEL——Olares 内置 Authelia 对企业 SSO 是"够用但非完备"。
- Olares 密码/密钥定位需辨析：用户清单同时写 Infisical(密钥管理)与 Vault(密码)，二者角色需在报告中区分（Infisical=密钥/密码，Vault 项此处指向密码管理器而非确认 HashiCorp Vault，需标注不确定）。

## END
