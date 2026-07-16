# PPT visual assets

Reusable Olares and open-source project marks for presentation mockups.

## `olares-market-icons/`

333 primary application icons cached from [`Above-Os/static`](https://github.com/Above-Os/static) at commit `33bd3257547e349f4f67aea61dde677cdea0ed4d`.

- One file per app ID, preferring PNG, then WebP, JPG and SVG.
- Excludes backup icons, alternate icons, screenshots and promotional images.
- `manifest.json` records the source path, raw URL, blob SHA, format and file size for every icon. Its `groups` section identifies built-in and other system apps without duplicating image files.
- Built-in apps: Desktop and Studio use homepage assets; Files, Market (`appstore`), Settings, Dashboard, Control Hub, Vault and Wise use canonical Market icons.
- Other system apps represented in Market include Accounts, Admin Console, Backup, Calendar, Notifications and Profile.
- Slide 17 community examples include ComfyUI, Dify, Home Assistant, Immich, LobeChat, Mattermost, n8n, Nextcloud, NocoDB, Ollama, Open WebUI and WordPress.

Use this collection when a slide needs the current Market icon. Some apps have multiple upstream icon variants; this cache deliberately keeps only the repository's primary `icon.*` file.

## `olares-stack-icons/`

38 project marks downloaded from the public [Olares homepage](https://www.olares.com/) on 2026-07-15:

- Infrastructure: Kubernetes, K3s, containerd, Helm, KubeSphere, MinIO, HAMi, nvShare
- Networking and access: Headscale, Tailscale, Envoy, FRP, lego
- Data and middleware: PostgreSQL, MongoDB, Citus, KVRocks, Predixy, NATS, JuiceFS, Seafile
- Security and identity: Authelia, LLDAP, Infisical, Open Policy Agent, Padloc
- Operations: Prometheus, OpenTelemetry, Jaeger, Restic, Velero, Argo Workflows, Rclone
- Other included projects: KubeBlocks, RSSHub, Quasar, File Browser, Trust Wallet

These are the website-rendered PNG marks rather than canonical upstream SVG logos. Several include dark rounded backgrounds or wordmarks, so check contrast and dimensions before placing them in a slide.

## `olares-homepage-assets/`

Website-rendered Olares and featured app presentation assets downloaded on 2026-07-15:

- Olares: logo, Desktop, Files, Vault, Market, Wise, Settings, Control Hub, Studio
- AI apps: ComfyUI, Suna, ACE-Step, Deer Flow, Hunyuan3D, Dify, Open WebUI
- Community apps: n8n, NocoDB, WordPress, Mattermost

This collection is not the canonical Market source. Twelve names overlap with `olares-market-icons/`, but the files are different website presentation variants. Prefer Market icons for application identity; use these only when a slide needs the exact homepage treatment or a website-only asset such as the Olares logo, Desktop or Studio.

The filenames are normalized for local use. Source URLs remain the assets currently served by the Olares homepage and may change when the site is rebuilt.

## `slide21-icons/`

Curated icon set for the Slide 21 heterogeneous accelerator diagram:

- `models/`: Qwen, DeepSeek, MiniMax, FLUX, Wan, Hunyuan3D, Qwen3-ASR and ACE-Step
- `software/`: llama.cpp, vLLM, SGLang, Ollama, OpenVINO and ComfyUI
- `hardware/`: Intel, NVIDIA, AMD and Apple vendor marks

The model and software set reuses canonical Market icons where available and official GitHub organization avatars otherwise. Hardware cards reuse vendor marks and identify the specific product in text. `manifest.json` records each source and the presentation-use boundary.
