# Olares five-layer architecture

> Intel collaboration deck, Slide 17. English slide copy.

---

## Slide copy

### Title

**Olares: An Open-Source, Five-Layer Personal Cloud OS**

An Android-inspired application model on top of a cloud-native PaaS and IaaS—running on hardware the user owns.

### Five-layer architecture

| Olares layer | Equivalent capabilities | Open-source + Olares-built stack | What this layer provides |
|--------------|-------------------------|----------------------------------|--------------------------|
| **Community apps** | Android third-party apps and Google Play; SaaS / AI products such as ChatGPT, Midjourney, Google Photos, Google Drive, Notion and Home Assistant Cloud | LLM engine bases, LobeChat, Dify, ComfyUI, Immich, Nextcloud and Home Assistant; Olares Market and Application Charts | An open local SaaS and AI ecosystem distributed through one application format |
| **Built-in apps** | Android System Apps; Dropbox / Google Drive, 1Password, Pocket / Feedly, cloud consoles and app stores | Desktop, Files, Market, Settings, Dashboard, Control Hub, Vault, Wise and Studio | Ready-to-use file, system management, monitoring, knowledge and development experiences |
| **Framework** | Android Application Framework, permissions and lifecycle; AWS IAM / Cognito, API Gateway, App Runner / Elastic Beanstalk | OlaresManifest, app-service, system-server, bfl, Authelia, LLDAP and OPA | Unified application lifecycle, permissions, identity, network entrances and inter-app calls |
| **Platform · PaaS** | AWS RDS, ElastiCache, SQS / SNS, S3 / EFS, CloudWatch and AWS Backup | PostgreSQL, KVRocks, NATS, JuiceFS, Prometheus, Restic, Velero and TAPR | Reusable data, middleware, file, backup and observability services for every application |
| **Infrastructure · IaaS** | AWS EC2, EKS, VPC, EBS / EFS and GPU instances | K3s / Kubernetes, containerd, Calico, CoreDNS, etcd, Helm, MinIO, HAMi, olaresd and olares-cli | Unified orchestration of compute, storage, networking, nodes and accelerators |

### Closing statement

**An Android-inspired application OS on an open-source, cloud-native foundation—running on hardware the user owns.**

---

## Working notes

- Visual order runs top-down from Community apps to Infrastructure; the dependency order is Infrastructure → Platform → Framework → Built-in apps → Community apps.
- Keep a four-column table. Separate the top three application-OS layers from the bottom two cloud-native layers through a horizontal divider and restrained background shift.
- `Open source · AGPL-3.0` is a property spanning all five layers, not a sixth layer.
- Android, SaaS / AI products and AWS services are architectural references or functional analogies—not Android application compatibility, API compatibility or identical implementations.
- Keep the NAS comparison in the speaker script, not on the slide.
