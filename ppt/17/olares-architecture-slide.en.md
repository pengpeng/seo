# Olares: A Natural-Language-Driven, Agent-Native OS

> Intel collaboration deck, Slide 17. English slide copy. Merges the former Slide 7 (One-Stop Solution product family) into this page: left = the five-layer architecture, right = the delivered products.

---

## Slide copy

### Title

**Olares: A Natural-Language-Driven, Agent-Native OS**

An Android-inspired application model on a cloud-native PaaS and IaaS—delivered as one integrated product on hardware the user owns.

### Left — Five-layer architecture (what each layer provides)

| Olares layer | What this layer provides | Representative chips on slide |
|--------------|--------------------------|------------------------------|
| **Community apps** | One format for a local SaaS and AI ecosystem. Installable apps inherit the same identity, storage and resource model. | LobeChat, Dify, ComfyUI, Immich, Nextcloud, Home Assistant |
| **Built-in apps** | Ready from first boot. Files, identity, knowledge, monitoring, system control and app development share one experience. | Desktop, Files, Market, Settings, Dashboard, Control Hub, Vault, Wise, Studio |
| **Framework** | Apps become governed system citizens. Lifecycle, permissions, SSO, entrances and inter-app calls are managed centrally. | Authelia, LLDAP, OPA, Envoy |
| **Platform · PaaS** | Shared services instead of repeated plumbing. Every app can reuse data, middleware, files, backup and observability. | PostgreSQL, KVRocks, NATS, JuiceFS, Prometheus, Velero |
| **Infrastructure · IaaS** | Hardware becomes a schedulable resource plane. Compute, storage, networking, nodes and accelerators are orchestrated together. | Kubernetes, K3s, containerd, Helm, MinIO, HAMi |

Top three layers are the Android-inspired application OS; bottom two are the cloud-native resource foundation. The value prose is the primary content per layer; chips are kept to recognizable icon+label tools only. Text-only internal identifiers (OlaresManifest, app-service, system-server, bfl, TAPR, olaresd, olares-cli) are dropped from the slide but kept in [references.md](./references.md).

### Right — Delivered as one product (one-stop solution)

- **Olares OS** — the open-source, five-layer OS (the stack on the left).
- **Clients** — desktop, mobile, and browser extension.
- **Olares Space** — domain, networking, remote access, and backup.
- **Olares Market** — one-click install for 200+ apps.
- **Olares CLI & Skills** — manage Olares in plain language with agents.

### Closing statement

**An Android-inspired application OS on an open-source, cloud-native foundation—running on hardware the user owns.**

---

## Working notes

- Merged from the former Slide 7 (One-Stop Solution). The five product tiles now live in the right panel as "delivered products," parallel to the five architecture layers on the left.
- Chips render without pill backgrounds (transparent, no white fill or border): app icons show as small rounded tiles, stack logos as transparent marks, each with a label. Framework adds Envoy (gateway / entrances, used by app-gateway / l4-bfl-proxy); Platform adds KVRocks (KV cache).
- The **Architectural references** column (Android / AWS analogies) was dropped from the slide face; it is kept in [references.md](./references.md) and the script. The per-layer "what this layer provides" prose is the primary left content; representative implementation is reduced to recognizable icon chips, with text-only internal identifiers moved to references.
- Visual order runs top-down from Community apps to Infrastructure; the dependency order is Infrastructure → Platform → Framework → Built-in apps → Community apps.
- Two-column body follows the design-system "main table + sidebar" layout: left five-layer table, right delivered-products panel. Separate the top three application-OS layers from the bottom two cloud-native layers through side rails and a restrained background shift.
- `Open source · AGPL-3.0` is a property spanning all five layers, not a sixth layer.
- Android, SaaS / AI products and AWS services are architectural references or functional analogies—not Android application compatibility, API compatibility or identical implementations.
- Keep the NAS comparison in the speaker script, not on the slide.
