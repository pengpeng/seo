# Olares Application Sandbox

> Intel collaboration deck, Slide 7. English slide copy, layout specification and speaker notes.

---

## Slide copy

### Title

Main title: **Sandboxes Every User, Application and Agent** (`Sandboxes` highlighted in green)

Subtitle: One multi-user device — users, applications and Agents run side by side, isolated by default and granted only what they declare.

### Upper left · 01 · Identity & authorization

**Who can act—and on whose behalf**

Subtitle: Unified authentication, workload authorization and secrets custody across users, applications and Agents.

| Capability | Product feature |
|---|---|
| **Unified identity** | **One sign-in across the system.** Authelia gives every user and application a consistent authentication entry, instead of letting each service build its own login boundary.<br><br>**Roles stay consistent everywhere.** LLDAP maintains the shared user and group directory, so Admin and Member roles follow people across applications. |
| **ReBAC & Agent delegation** | **Every workload receives only what it needs.** Olares uses native Kubernetes Roles and ServiceAccounts to bind permissions to an application, rather than exposing the authority of the whole device.<br><br>**People and groups keep their own boundaries.** ReBAC lets Search, Files and IM authorize by user, group and resource relationship; an Agent remains inside the same combined scope. |
| **Secrets & key custody** | **Sensitive credentials stay out of applications.** Infisical manages LLM API keys and Agent cookies today, with OpenBao becoming the unified secret-management layer next.<br><br>**Key custody can move into hardware.** A low-level HSM interface lets users connect a third-party HSM when stronger hardware-backed protection is required. |

### Upper right · 02 · Runtime & resource isolation

**How each application runs**

Subtitle: Isolated runtimes, reduced privileges and explicit resource envelopes.

| Capability | Product feature |
|---|---|
| **Runtime boundary** | **Each application gets its own runtime.** An application does not share its execution boundary directly with the host environment.<br><br>**Users remain separated.** User-scoped namespaces keep workloads and service identities inside their owner's space. |
| **Reduced privilege** | **Privilege starts low.** Applications run in unprivileged containers instead of receiving host-level access.<br><br>**Policy is checked before execution.** OPA admission validates every application's declared permissions before it is installed or allowed to run. |
| **Resource envelope** | **Capacity is declared up front.** CPU, memory and accelerator requests tell the scheduler what an application needs.<br><br>**The system protects itself under pressure.** When capacity runs short, Olares intelligently evicts workloads to preserve overall stability and keep critical services running. |

### Lower left · 03 · Network boundary & access

**How each application connects**

Subtitle: Four access paths, protected by declared entrances and layered security.

| Network path | Product feature |
|---|---|
| **Internet** | **Domains and HTTPS come ready.** Every Web entrance receives a free Olares domain and managed certificate, with custom domains and user-selected reverse proxies also supported. |
| **VPN · LarePass** | **Private access without a third-party control plane.** LarePass uses Tailscale clients with Headscale hosted locally on Olares, preferring LAN or direct P2P and falling back to relay when needed. |
| **Local network** | **Local compatibility stays intact.** `.local` HTTP serves Web access, while a per-application Overlay Gateway carries discovery and native LAN protocols for smart-home, casting and media devices. |
| **In-cluster** | **Identity-aware service mesh.** Automatic mTLS and ServiceAccount identity secure every workload; fine-grained policy, metrics and audit signals make east-west traffic observable and governable. |

Olares follows cloud-native networking best practices and delivers enterprise-grade security while retaining the compatibility and flexibility required by home networks, legacy protocols and multiple remote-access paths.

### Lower right · 04 · Data & filesystem boundary

**What data each application can see**

Subtitle: Olares Files applies declared scopes across persistent, connected and Agent-ready storage.

| Capability | Product feature |
|---|---|
| **Sandboxed spaces** | **Every path has an owner.** Home, Data, Cache and Common define ownership, durability and sharing; applications mount only declared paths. |
| **Cross-node data plane** | **Persistent data follows the cluster.** Home, Data and Common remain available across nodes, while Cache stays local and safely rebuildable. |
| **Connected storage** | **Existing data stays where it is.** Sync, cloud drives, USB, SMB, NFS and existing NAS join one file world; Managed RAID is next. |
| **PC-grade Files & sharing** | **Users keep familiar file operations.** Files can browse, preview, edit, move and archive data, then share the original through users, public links or SMB. |
| **Search** | **Discovery comes before action.** Search finds candidates by name, full content or image; Files then verifies permission and acts. |
| **Unified access URLs** | **Agents use one address model.** Files exposes data through a consistent URL model, whether the backend is local, distributed, cloud or external storage. |

---

## Speaker notes

Start with why a sandbox is needed. Olares is a multi-user system: multiple users, the applications they install and the Agents that work on their behalf all share one device. So the sandbox really isolates three subjects—User, Application and Agent. A user owns an identity and a role, and RBAC decides what they can reach; an application runs inside the network, storage and resource envelope it is granted; an Agent acts on a user's behalf inside an application, with permissions that are the intersection of the two. Everything is isolated by default, and capabilities are granted explicitly through the Manifest.

A sandbox is more than a container. It answers four consecutive questions: **who can act, how an application runs, how it connects, and what data it can see.**

The first boundary is Identity & authorization. Authelia provides unified authentication, while LLDAP centralizes users, groups and roles. Authorization has two layers: Kubernetes Roles and ServiceAccounts bound workload permissions, while ReBAC governs user, group and resource relationships inside Search, Files and IM. Agent delegation grants no ambient authority; an Agent stays inside the combined authorization scope. Infisical manages LLM API keys and Agent cookies today, OpenBao follows, and a low-level HSM interface enables third-party hardware custody.

The second boundary is Runtime & resource isolation. Each application runs inside an isolated runtime and a user-scoped namespace, using an unprivileged container by default. OPA admission validates declared permissions before installation or execution. CPU, memory and accelerator requests describe demand; when the system comes under pressure, Olares intelligently evicts workloads to preserve overall stability and keep critical services running.

The third boundary is Network. Its product position is **cloud-native security, built for real-world networks**: cloud-native protection without sacrificing compatibility with home networks, legacy protocols and remote access. Internet, VPN · LarePass, Local network and In-cluster are independent paths. Internet reverse proxy gives every standard Web entrance a free Olares domain, HTTPS and a managed certificate, while also supporting custom domains and user-selected reverse proxies. LarePass combines Tailscale clients with a Headscale control plane hosted locally on Olares and automatically selects direct or relay paths. `.local` HTTP and the Overlay Gateway cover local Web access and native LAN protocols, while the Linkerd service mesh governs east-west traffic through automatic mTLS, ServiceAccount-bound workload identity, fine-grained authorization, traffic metrics and audit signals.

The fourth boundary is Data & filesystem. The experience is **governed like cloud infrastructure, familiar like a PC and ready for Agents**. Olares Files compresses sandboxed spaces, the cross-node data plane, Sync / Cloud / External, PC-grade operations, sharing, search and Unified access URLs into six capabilities. Applications see only declared data; Agents use one URL address model across local, distributed, cloud, SMB and NFS backends instead of adapting to each storage API.

One policy spine governs all four boundaries: Manifest declares → OPA validates → Platform enforces.

---

## Layout specification

- Use a `1280×720` canvas as `header 64px / body 1fr`; no separate narrative band—the multi-user why and the three subjects are carried by the main title and subtitle.
- Use a `2×2` body: upper-left 01 Identity, upper-right 02 Runtime & resource, lower-left 03 Network, lower-right 04 Files.
- Split columns evenly at `50 / 50`; give the shorter upper row roughly `42%` of the body and the denser Network / Files row roughly `58%`.
- Use editorial matrices instead of full-width strips: Identity `2×2`, Runtime as three columns, Network `2×2`, and Files `2×3`.
- Group capabilities through whitespace, alignment and a few hairlines—no cards, colored backgrounds or full-width rule under every item.
- Compress Files from nine rows to six: merge Sync / Cloud / External into Connected storage, and merge Sharing with PC-grade Files.
- Do not use a footer; keep the cross-cutting Declarative policy in speaker notes and internal notes only.
- Present features only, in one neutral palette; do not use a deep-green block or any separate colored container.
- Establish hierarchy through type weight, numbering, thin rules and alignment rather than rounded cards.
- Use English throughout the HTML and final export.

## Wording boundaries

- This is an Intel commercial partnership pitch describing the complete product direction and the target architecture for the next two to three months.
- Free independent domains and managed HTTPS certificates apply to standard application Web entrances.
- WAF protects the standard Web path; it does not cover every native protocol.
- Enforce VPN is an administrator policy that tightens public access for non-public entrances; Public services can remain open.
- `.local` uses HTTP.
- Home, Data and Common belong to the cross-node persistent data plane; Cache is node-local and rebuildable.
- Files is a unified file data plane, not a NAS or a centralized cloud drive.
- Mark Managed RAID storage as **Next**.

## Research basis

See [olares-sandbox-notes.md](./olares-sandbox-notes.md) for network, identity, resources, Files, code/docs evidence and product boundaries.
