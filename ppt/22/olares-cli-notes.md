# Olares CLI 能力笔记

> 面向 Intel 合作 PPT 第 22 页的代码研究底稿。代码来源：`/Users/pengpeng/olares/cli`；快照日期：2026-07-15。

## 核心结论

`olares-cli` 已经提供一套适合 Agent 调用的、受身份与权限约束的 Olares 执行面：

**Natural-language intent → 外部 Personal Agent → Olares Skills → `olares-cli` 结构化命令 → Olares HTTP API → Execute · Observe · Diagnose · Report**

自然语言理解与任务编排发生在 Agent 层，不在 CLI 内。Skills 告诉 Agent 该选择什么命令、如何处理认证和错误；CLI 负责把操作可靠地落实到 Olares，并返回适合人或 Agent 消费的 table / JSON 结果。

这可以支撑第 22 页的核心叙事：

- **Agent manages Olares**：Agent 通过 Skills 与 CLI 管理应用、文件、设置、集群和系统资源。
- **Olares governs every action**：每次操作仍受 Olares ID、角色、namespace、API 权限和确认机制约束。

## 1. 命令体系

代码入口：

- `cmd/main.go:13-38`：进程入口，创建并执行根命令。
- `cmd/ctl/root.go:31-118`：注册完整命令树，并区分主机侧与远程 / Agent 命令。
- `pkg/cmdutil/factory.go:82-120`：为身份层命令提供 profile、credential、HTTP client 与后端版本。

CLI 实际包含三类能力：

| 层 | 典型命令 | 使用方式 |
|----|----------|----------|
| **Identity-bound / Agent layer** | `profile`、`market`、`files`、`settings`、`dashboard`、`cluster`、`search`、`doctor` | 使用当前 Olares ID，通过远程 HTTP API 操作一台正在运行的 Olares |
| **Developer layer** | `chart from-compose`、`chart lint`、`chart package` | 在本地打包和校验 Olares 应用；部署继续调用 `market upload/install` |
| **Host system layer** | `install`、`upgrade`、`node`、`gpu`、`amdgpu`、`disk`、`user`、`backup`、`logs` | 在 Olares 主机上执行安装、升级和底层维护 |

npm / npx 分发版会设置 `OLARES_CLI_REMOTE_ONLY=1`，隐藏需要主机环境的命令；它适合远程 Agent 操作 Olares，但不能据此宣称 Agent 可远程执行全部 OS 安装和主机维护。证据见 `cmd/ctl/root.go:86-116` 与 `npm/bin/olares-cli.js:32-44`。

## 2. 当前 CLI 能做什么

### Profile 与认证

- 密码与可选 TOTP 登录：`profile login`
- 导入 refresh token：`profile import`
- 列出、切换和删除 profile：`profile list/use/remove`
- 查看当前身份和角色：`profile whoami`

Token 存在系统 keychain 中；身份层 HTTP client 遇到特定认证错误后会自动刷新并重试一次。CLI 没有每次调用临时指定 `--profile` 的模式，Agent 需要先明确切换当前身份。

代码依据：

- `cmd/ctl/profile/root.go:1-70`
- `pkg/auth/token_store_keychain.go:49-69`
- `pkg/cmdutil/factory.go:295-479`

### Market：应用目录与生命周期

- 浏览目录：`list`、`categories`、`get`
- 查看安装与运行状态：`list --mine`、`status`
- 管理生命周期：`install`、`upgrade`、`uninstall`、`clone`、`cancel`、`stop`、`resume`、`restart`
- 管理本地 Chart 源：`upload`、`delete`
- 长操作可使用 `--watch`、`--watch-timeout` 与状态轮询

这组命令是“Agent 安装和管理应用”的直接代码依据。`market sync` 因依赖集群内服务而没有暴露给边缘 CLI。

代码依据：`cmd/ctl/market/root.go:9-90`、`cmd/ctl/market/watch.go:14-100`。

### Files：个人数据与文件操作

- 浏览和读写：`ls`、`cat`、`edit`、`upload`、`download`
- 文件管理：`mkdir`、`rm`、`cp`、`mv`、`rename`、`chown`
- 归档与任务：`compress`、`extract`、`archive`、`task`
- 分享：internal / public / SMB
- 外部挂载：SMB、NFS
- Sync / Seafile 库：`repos list/get/create/rename/rm`

这组命令说明 Personal Agent 不只是启动 AI 应用，也能在授权范围内直接处理用户拥有的数据。

代码依据：`cmd/ctl/files/root.go:12-129`。

### Settings：系统设置

当前注册的主要区域包括：

- 用户、外观、应用环境变量与入口
- 集成账户
- VPN、ACL、SSH、overlay network
- 反向代理与部分网络状态
- GPU / compute binding
- 搜索索引、备份与恢复
- registry、镜像、系统与用户环境变量
- 当前用户、版本、更新与 SSO

Settings CLI 是 SPA 能力的命令行镜像，但并未覆盖全部写操作。涉及 JWS / TermiPass、安全敏感流程或浏览器 OAuth 的部分命令没有注册，不能表述为“CLI 完整替代 Settings”。

代码依据：`cmd/ctl/settings/root.go:36-94`。

### Dashboard：资源观测

- 总览：physical、user、ranking
- CPU、内存、Pod、网络、磁盘、风扇和 GPU
- 应用工作负载视图
- `--watch` 持续观测
- `-o json` 返回稳定 envelope
- `dashboard schema` 提供 JSON Schema 自省

Dashboard 的代码明确面向 AI Agent 使用，是“Observe · Report”的主要执行依据。

代码依据：`cmd/ctl/dashboard/root.go:1-136`、`pkg/dashboard/schema.go:13-59`。

### Cluster：工作负载与运行时诊断

- Pod：list、get、yaml、events、logs、delete、restart、exec
- Container：list、env、logs、exec
- Workload：list、images、get、yaml、rollout、scale、restart、stop、start、delete
- Application：list、get、workloads、pods、status
- Namespace、Node、Middleware
- Job 与 CronJob

Cluster 命令镜像 Control Hub 的 Kubernetes 视图。应用安装和卸载仍归 `market`；主机安装、节点加入和 GPU 驱动仍归主机命令，三者不应混写。

代码依据：`cmd/ctl/cluster/root.go:1-107`。

### Search：用户内容检索

- `search drive`：Drive 文件全文或文件名搜索
- `search sync`：Sync / Seafile 库搜索
- `search app`：已安装应用搜索

它提供了 Agent 查找用户上下文的入口，但不等同于完整的 Agent Memory 或 RAG 平台。

代码依据：`cmd/ctl/search/root.go:9-36`。

### Doctor：诊断编排

CLI 当前只直接注册 `doctor images`，用于检查本地镜像及其 workload 引用关系。更广泛的运行时诊断由 `olares-doctor` Skill 根据症状编排 `market`、`cluster`、`dashboard` 等命令完成。

因此可以说“Agent 使用 Skills 收集证据并诊断故障”，但不能说“`olares-cli doctor` 已是完整的一键 AI 根因分析引擎”。

代码依据：`cmd/ctl/doctor/root.go:12-22`、`cmd/ctl/cluster/workload/doctor_images.go:25-67`。

### Chart：应用打包

- `chart from-compose`：从 Docker Compose 生成 Olares Chart 起点
- `chart lint`：按 Olares Market 摄入规则校验
- `chart package`：打包 `.tgz`

结合 `market upload/install`，Agent 可以完成“从项目到自己的 Olares”的打包、上传、安装与诊断流程。公开上架由 `olares-publish` Skill 编排，不存在独立的 CLI `publish` 命令。

代码依据：`cmd/ctl/chart/root.go:5-30`。

### Host：系统与硬件维护

完整主机版还包括：

- OS 安装、卸载、启动、停止、升级、状态、备份和日志
- 节点加入与存储启用
- NVIDIA GPU 安装、启停和状态
- AMD GPU / ROCm 安装、卸载和状态
- 用户、磁盘、IP、下载与安装前检查

这些能力真实存在，但 npm / npx 的 remote-only 版本不注册它们。第 22 页若面向一般 Personal Agent，应以身份层能力为主，不把主机本地命令全部画进主控制链。

代码依据：`cmd/ctl/os/root.go:7-23`、`cmd/ctl/root.go:86-104`。

## 3. Skills 如何把 CLI 变成 Agent 工具

`cli/skills/` 当前包含 10 个 Skill：

1. `olares-shared`
2. `olares-market`
3. `olares-files`
4. `olares-settings`
5. `olares-dashboard`
6. `olares-cluster`
7. `olares-search`
8. `olares-doctor`
9. `olares-chart`
10. `olares-publish`

其中 `olares-shared` 是身份、认证和跨 Skill 路由入口；其他 Skills 将用户意图映射到对应命令域，并补充 `--help` 无法表达的行为约束、错误恢复和跨命令工作流。

需要注意：仓库根 README 中仍有“6 个 Skills”等旧描述，应以 `skills/README.md:145-158` 与实际目录为准。

## 4. 安全与治理

CLI 并不是让 Agent 绕过系统治理，而是让 Agent 进入与用户界面相同的治理边界：

- **身份**：当前 Olares ID 与 profile 是所有身份层命令的统一入口。
- **凭证**：Token 存 keychain，并支持受控刷新。
- **角色**：Settings 写操作会做角色预检，服务端 403 仍是最终权威。
- **执行范围**：Cluster exec 会根据用户、管理员角色和 namespace 做门控。
- **破坏性操作**：危险命令需要确认；Agent 自动化需显式使用相应确认参数。
- **可观测**：JSON、Schema、watch、logs、events、metrics 让 Agent 能基于反馈继续行动。

关键依据：

- `pkg/whoami/preflight.go:34-116`
- `pkg/clusterctx/permission.go:20-64`
- `cmd/ctl/cluster/pod/exec_permission.go:41-60`
- `skills/olares-cluster/SKILL.md:101-109`

## 5. 能力边界

对第 22 页和对外材料需要保留以下限定：

| 不宜声称 | 实际情况 |
|----------|----------|
| CLI 内置自然语言理解 | 自然语言由外部 Agent 处理；CLI 是结构化执行面 |
| Agent 可以无授权控制整台系统 | 所有身份层操作受 profile、角色、namespace 和服务端权限约束 |
| npm 版 CLI 可以执行全部主机维护 | npm 强制 remote-only，隐藏 OS / node / GPU 等主机命令 |
| CLI 完整覆盖 Settings SPA | 部分安全敏感写操作未注册 |
| `doctor` 是全自动 AI 诊断引擎 | CLI 只有 `doctor images`；广义诊断依靠 Skill 编排 |
| CLI 已提供完整多 Agent 控制平面 | 当前是 Agent 可调用的系统执行面，不是多 Agent 调度产品 |
| Search 就是完整 Memory / RAG | Search 提供内容检索入口，Memory / RAG 仍是更上层能力 |
| 所有模型推理必须本地完成 | CLI 不决定 Agent 使用本地还是外部模型 |

另外，README 中的 `profile current` 与浏览器认证描述不符合当前 Go 命令树：当前应使用 `profile list` / `profile whoami`，登录方式是密码 + TOTP 或 refresh token import。

## 6. 对第 22 页的启发

### 建议主链路

**Natural-language intent → Personal Agent → Olares Skills → `olares-cli` → Olares APIs → Apps · Files · Settings · Cluster**

回路：

**JSON / Schema · Watch · Metrics · Logs · Events → Agent**

### 建议四组可视化能力

| Skills / CLI area | Agent 得到的能力 |
|-------------------|------------------|
| **Market + Chart** | Build · Deploy · Install · Upgrade · Stop · Resume |
| **Files + Search** | Read · Write · Share · Mount · Find user context |
| **Settings + Profile** | Authenticate · Configure · Connect · Govern access |
| **Dashboard + Cluster + Doctor** | Observe · Inspect · Diagnose · Recover |

这比把 Local LLM、Memory、RAG、Sandbox 全部归入 CLI 更准确：后者属于 Olares 上更广泛的 Agent Host / 应用运行环境，不是当前 CLI 命令面的直接实现。

### 可用于 Slide 的精确表述

> Olares Skills give Personal Agents a structured, permission-aware interface to applications, files, settings and runtime operations. `olares-cli` executes those actions through the same Olares APIs used by the product UI, then returns machine-readable status, metrics and diagnostics.

更短版本：

> **Natural language in. Governed system actions out.**

## 7. 关键源码索引

| 主题 | 源码 |
|------|------|
| 根命令与 remote-only 边界 | `/Users/pengpeng/olares/cli/cmd/ctl/root.go:31-118` |
| Agent-native 定位与输出约定 | `/Users/pengpeng/olares/cli/README.md:7-20,137-172` |
| 认证 HTTP client | `/Users/pengpeng/olares/cli/pkg/cmdutil/factory.go:36-62,295-479` |
| Skills 套件 | `/Users/pengpeng/olares/cli/skills/README.md:7-37,145-158` |
| Skill 路由与认证恢复 | `/Users/pengpeng/olares/cli/skills/olares-shared/SKILL.md:30-45,110-160` |
| Market | `/Users/pengpeng/olares/cli/cmd/ctl/market/root.go:9-90` |
| Files | `/Users/pengpeng/olares/cli/cmd/ctl/files/root.go:12-129` |
| Settings | `/Users/pengpeng/olares/cli/cmd/ctl/settings/root.go:36-94` |
| Dashboard | `/Users/pengpeng/olares/cli/cmd/ctl/dashboard/root.go:1-136` |
| Cluster | `/Users/pengpeng/olares/cli/cmd/ctl/cluster/root.go:1-107` |
| Search | `/Users/pengpeng/olares/cli/cmd/ctl/search/root.go:9-36` |
| Doctor | `/Users/pengpeng/olares/cli/cmd/ctl/doctor/root.go:12-22` |
| Chart | `/Users/pengpeng/olares/cli/cmd/ctl/chart/root.go:5-30` |
| npm remote-only | `/Users/pengpeng/olares/cli/npm/bin/olares-cli.js:32-44` |
