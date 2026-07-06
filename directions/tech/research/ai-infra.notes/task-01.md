---
task_id: 01
role: 推理服务与模型网关生态图谱分析师
status: complete
sources_found: 15
---

## Sources
[1] Local LLMs in 2026: Which Runtime to Run (Nishil Bhave, Medium) | https://medium.com/@nishilbhave/local-llms-in-2026-which-runtime-to-run-and-the-hardware-you-need-a88450dece2e | Source-Type: journalism | As Of: 2026-06 | Authority: 6/10
[2] vllm-project/vllm (GitHub) | https://github.com/vllm-project/vllm | Source-Type: official | As Of: 2026-07 | Authority: 9/10
[3] Open-source LLM inference engines compared 2026 (Fish Audio Blog) | https://fish.audio/blog/open-source-llm-inference-engines-2026/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[4] Open-Weight Serving Stack Comparison 2026 (Presenc AI) | https://presenc.ai/research/open-weight-serving-stack-comparison-2026 | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10
[5] LLM Inference Servers Compared (TensorFoundry) | https://tensorfoundry.io/blog/llm-inference-servers-compared | Source-Type: secondary-industry | As Of: 2026-03 | Authority: 6/10
[6] OpenRouter vs LiteLLM vs Bifrost (Maxim AI) | https://www.getmaxim.ai/articles/openrouter-vs-litellm-vs-bifrost-ai-gateway-comparison/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[7] Stop Juggling LLM APIs: 9 Gateways Ranked 2026 (TECHSY) | https://techsy.io/en/blog/best-llm-gateway-tools | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[8] cuihuan/awesome-ai-gateway (GitHub) | https://github.com/cuihuan/awesome-ai-gateway | Source-Type: community | As Of: 2026 | Authority: 6/10
[9] Bifrost vs LiteLLM (TrueFoundry) | https://www.truefoundry.com/blog/bifrost-vs-litellm | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[10] The latency tax of an LLM gateway (dev.to, Marcus Chen) | https://dev.to/marcuswwchen/the-latency-tax-of-an-llm-gateway-i-measured-bifrosts-overhead-2pk3 | Source-Type: community | As Of: 2026 | Authority: 4/10
[11] Serverless Inference (Together AI) | https://www.together.ai/serverless-inference | Source-Type: official | As Of: 2026 | Authority: 8/10
[12] Serverless Overview (Fireworks AI Docs) | https://docs.fireworks.ai/serverless/overview | Source-Type: official | As Of: 2026 | Authority: 8/10
[13] AI Inference API Providers Compared 2026 (runit.ai) | https://static.runit.ai/blog/ai-inference-api-providers-compared | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[14] Serverless LLM platforms: Modal/Together/Fireworks/Replicate (datarekha) | https://datarekha.com/blog/modal-together-fireworks-serverless/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 5/10
[15] Inference Provider Comparison Report (Saturn Cloud) | https://saturncloud.io/reports/inference-provider-comparison-report/ | Source-Type: secondary-industry | As Of: 2026 | Authority: 6/10

## Findings
- vLLM 是生产级 GPU 推理事实标准：PagedAttention + 连续批处理，85,384 stars、Apache-2.0、OpenAI 兼容 API、支持 200+ HF 模型架构与 NVIDIA/AMD/CPU/Gaudi/TPU。[2]
- 按 mindshare，Ollama 领先（174,000+ stars），但它本质是 llama.cpp 的封装/GUI；llama.cpp（~73,000 stars，MIT）才是消费级推理的底层引擎，覆盖 CPU/Apple Silicon/广泛硬件。[1][4]
- SGLang（~25–28K stars，Apache-2.0，UC Berkeley+LMSys）以 RadixAttention 前缀缓存见长，适合 agentic/共享上下文/MoE 负载；社区较小、仅 Linux。[3][4][5]
- HuggingFace TGI 已进入维护模式（2026-03 仓库归档），新项目官方建议改用 vLLM 或 SGLang。[3][5]
- LMDeploy（上海 AI Lab，Apache-2.0）以 TurboMind 引擎在 NVIDIA 上的量化/长上下文表现强，是 vLLM 的替代评估项，尤擅中文模型/芯片。[4][5]
- 并发是选型关键：64 并发下 vLLM 生成 token 速率约为 llama.cpp 的 44 倍；单用户下 Ollama/llama.cpp 与之接近。[1]
- LiteLLM（~52.1K stars，Python，Apache-2.0）是自托管网关默认选择：SDK+代理，OpenAI 兼容，覆盖 100+ provider，含虚拟 key/预算/负载均衡/guardrails。[7][8]
- Bifrost（Maxim AI，Go，~6.1K stars，Apache-2.0）主打高性能：宣称 5000 RPS 下每请求仅 ~11µs 开销、自适应负载均衡、集群模式、MCP 支持；provider 覆盖较窄（20+）。[6][8][9]
- TensorZero（Rust，~11.7K stars，Apache-2.0）统一网关+可观测+评估+实验；**公司 2026-06 停运、仓库归档只读**（Apache 代码与社区 fork 仍在）。[8]
- OpenRouter 是托管 SaaS 市场（300+ 模型、单 key、按 token 计费），不自托管；对标闭源网关叫法还有 Vercel AI Gateway、Cloudflare AI Gateway、Portkey。[6][7][8]
- 公有云托管推理三档：①按 token serverless（Together AI 200+ 开源模型 OpenAI 兼容 / Fireworks 自研 FireAttention、FP8/FP4）②带容器控制的自动扩缩（Baseten UI、Modal 代码优先）③超大规模平台（AWS Bedrock 全托管基座 / SageMaker 控制基建 / Google Vertex / Azure AI Foundry）。[11][12][13][14][15]
- 这些云 provider 底层多用 vLLM 作为推理引擎，与自托管栈同源。[13]

## Deep Read Notes
### Source [2]: vllm-project/vllm GitHub
Key data: 85,384 stars / 18,934 forks / 470 contributors / 98 releases，最新 v0.24.0（2026-06-29）；Apache-2.0；OpenAI 兼容 + Anthropic Messages API + gRPC；200+ 模型架构；多 LoRA。
Key insight: 明确定位"高吞吐+内存高效 serving 引擎"，是唯一同时具备张量/流水/数据/专家/上下文并行的开源引擎。
Useful for: 推理服务子类 top1 论证。

### Source [12]: Fireworks Serverless Overview
Key data: multi-tenant serverless（Standard/Priority/Fast 三路径），按 token 计费；serverless 适合热门基座模型、on-demand（按 GPU-hour）适合自定义/LoRA。
Key insight: 云托管推理的"serverless vs on-demand"分层正是自托管栈要替代的运维复杂度。
Useful for: 公有云对标叫法与 Olares 平替叙事。

## Gaps
- 各引擎精确 2026 最新 star 数在不同来源间有出入（vLLM 75K vs 85K、SGLang 25K vs 28K），已取官方 GitHub 数为准。
- 相反主张候选：Menlo Ventures 数据称开源模型仅占企业 LLM 用量 11%（2025，较前一年 19% 下降），即"多数生产流量仍打托管 API"——削弱"自托管已成主流"的叙事。[1]
- 未深入：TensorRT-LLM / MAX(Modular) / MLC-LLM 的定位（NVIDIA 峰值吞吐 / 跨平台）。

## END
