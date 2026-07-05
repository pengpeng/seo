#!/usr/bin/env python3
import os, glob, re, yaml

APPS_DIR = "/Users/pengpeng/terminus-apps"
SEO_DIR = "/Users/pengpeng/seo/directions/market/reports"
OUT = "/Users/pengpeng/seo/directions/market/apps.md"

# ---- exclusion rules ----
DROP_SUFFIX = ("client", "share", "sharev2", "sharev3", "forcluster", "fusion",
               "fusionclient")
DROP_EXACT = {
    "gitlabpure",  # gitlab 已单独存在
    # infra / middleware / DB
    "mariadb","mysql","mongodb","clickhouse","elasticsearch","rabbitmq","minio",
    "geth","ipfs","nomad","ray","chaosmesh","odigos",
    # internal / demo / helper
    "didgate","otmoiclp","otmoicrelay","dman","ticket","merchant","larescompanion",
    "cmproxy","dist","knowledge","pool","rssubscribe","twitter","teatappintel",
    # embedding/rerank model helpers (folded into model-serving note)
    "embeddinggemma","jinaclip","paddleocrgguf",
}
def is_test(n): return n.startswith("test") or n == "skilltestapp"

# model-serving families collapse -> single engine brand
MODEL_PREFIX = {
    "ollama":"Ollama","vllm":"vLLM","sglang":"SGLang","llamacpp":"llama.cpp",
    "xinference":"Xinference",
}

# manual titles for manifests that fail YAML parse
TITLE_FALLBACK = {
    "cosyvoice":"CosyVoice","echomimic":"EchoMimic","funclip":"FunClip",
    "studio":"Studio","heygem":"HeyGem","indextts":"IndexTTS","fishspeech":"Fish Speech",
    "paddleocr":"PaddleOCR","rembg":"Rembg","speaches":"Speaches","hunyuan3d":"Hunyuan3D",
    "sdwebui":"Stable Diffusion WebUI","sdwebuiforge":"SD WebUI Forge",
    "sdwebuiforgeneo":"SD WebUI Forge Neo","stablefast3d":"Stable Fast 3D",
    "acestep":"ACE-Step","acestep15":"ACE-Step 1.5","deepseekocrwebui":"DeepSeek-OCR WebUI",
    "openedaispeech":"OpenedAI Speech","mtranserver":"MTranServer","whisperservice":"Whisper API",
    "whisperwebui":"Whisper-WebUI","facefusion":"FaceFusion","onlyoffice":"ONLYOFFICE",
    "searxng":"SearXNG","dify":"Dify","deerflow":"DeerFlow","falco":"Falco","difyfusion":"Dify",
    "koboldcpp":"KoboldCpp","wordpresspure":"WordPress",
}
DESC_FALLBACK = {}

def base_name(n):
    """strip trailing version markers"""
    b = n
    for suf in ("v21v2","v21","v3","v2","v1"):
        if b.endswith(suf) and len(b) > len(suf):
            b = b[:-len(suf)]
            break
    return b

def model_engine(n):
    for pre,brand in MODEL_PREFIX.items():
        if n.startswith(pre):
            return pre,brand
    return None,None

# ---- load manifests, dedup by metadata.title (the real brand) ----
def norm(s): return re.sub(r"[^a-z0-9]","", (s or "").lower())
best = {}  # title-key -> dict(row)
orphans = {}  # base dir -> row  (no parseable title anywhere)
for mf in glob.glob(os.path.join(APPS_DIR, "*/OlaresManifest.yaml")):
    name = os.path.basename(os.path.dirname(mf))
    if os.path.exists(os.path.join(APPS_DIR, name, ".suspend")): continue  # 已下架
    if is_test(name): continue
    if name.endswith("client"): continue
    if model_engine(name)[0]: continue          # model families handled separately
    if name in DROP_EXACT or base_name(name) in DROP_EXACT: continue
    try:
        d = yaml.safe_load(open(mf, encoding="utf-8")) or {}
    except Exception:
        d = {}
    md = (d.get("metadata") or {})
    spec = (d.get("spec") or {})
    if d.get("olaresManifest.type","") == "middleware": continue
    title = md.get("title") or ""
    if title and re.search(r"(for test|test app|dashboard)", title, re.I): continue
    cats = md.get("categories") or []
    desc = (md.get("description") or "").replace("\n"," ").strip()
    web = spec.get("website","") or ""
    if title:
        k = norm(title)
        row = dict(appid=name, title=title, cats=cats, desc=desc, web=web)
        old = best.get(k)
        # prefer richer metadata (more categories / has desc)
        if old is None or (len(cats)+bool(desc)) > (len(old["cats"])+bool(old["desc"])):
            best[k] = row
    else:
        b = base_name(name)
        if b not in orphans:
            orphans[b] = dict(appid=name, title=TITLE_FALLBACK.get(b, b), cats=[], desc="", web="")

# parse-failed apps: give known ones proper title/category/desc; drop companions/dups
ORPHAN_META = {
    "cosyvoice":("CosyVoice","AI","阿里开源多语种语音合成 (TTS)"),
    "echomimic":("EchoMimic","Creativity","音频驱动的数字人 / 口型生成"),
    "funclip":("FunClip","Creativity","阿里开源视频剪辑 / 字幕工具"),
    "heygem":("HeyGem","Creativity","本地数字人视频生成（HeyGen 平替）"),
    "hunyuan3d":("Hunyuan3D","Creativity","腾讯混元 3D 模型生成"),
    "indextts":("IndexTTS","AI","工业级零样本语音合成 (TTS)"),
    "koboldcpp":("KoboldCpp","AI","本地 LLM 推理与角色扮演前端"),
    "sdwebui":("Stable Diffusion WebUI","Creativity","最流行的本地 Stable Diffusion 出图 WebUI"),
    "sdwebuiforge":("SD WebUI Forge","Creativity","Stable Diffusion WebUI Forge（出图）"),
    "sdwebuiforgeneo":("SD WebUI Forge Neo","Creativity","Stable Diffusion WebUI Forge Neo（出图）"),
    "stablefast3d":("Stable Fast 3D","Creativity","单图快速生成 3D 模型"),
    "studio":("Studio","Developer Tools","Olares 应用开发 / 部署工作台"),
}
ORPHAN_DROP = {"comfyuishare","deepseekocrwebui","sdwebuishare","stablefast3dshare"}
for b,row in orphans.items():
    name = row["appid"]
    if b in ORPHAN_DROP or name.endswith("client"): continue
    if any(base_name(name).endswith(s) for s in DROP_SUFFIX): continue
    if b in ORPHAN_META:
        t,c,d = ORPHAN_META[b]
        row.update(title=t, cats=[c], desc=d)
    if norm(row["title"]) in best: continue
    if any(k.startswith(norm(row["title"])) or norm(row["title"]).startswith(k)
           for k in best if len(k) >= 5): continue
    best[norm(row["title"])] = row

# add collapsed model engines
CAT_MODEL = "模型服务 / 推理引擎"
model_rows = {
    "ollama":dict(appid="ollama",title="Ollama",desc="本地大模型运行引擎（含 40+ 预置模型变体）",web="https://ollama.com/"),
    "vllm":dict(appid="vllm",title="vLLM",desc="高吞吐 LLM 推理引擎",web="https://vllm.ai/"),
    "sglang":dict(appid="sglang",title="SGLang",desc="高性能 LLM 推理引擎",web="https://sglang.ai/"),
    "llamacpp":dict(appid="llamacpp",title="llama.cpp",desc="轻量本地 LLM 推理",web="https://github.com/ggml-org/llama.cpp"),
    "xinference":dict(appid="xinference",title="Xinference",desc="一站式模型部署 / 推理框架",web="https://xinference.com/"),
}

# ---- report status (match by normalized title) ----
reports = {}
for f in glob.glob(os.path.join(SEO_DIR, "*.md")):
    stem = re.sub(r"-\d{4}-\d{2}-\d{2}$","", os.path.basename(f)[:-3])
    reports[norm(stem)] = os.path.basename(f)
def report_for(row):
    keys = {norm(row["title"]), norm(row["appid"]),
            re.sub(r"\d+$","", norm(row["title"]))}
    keys.discard("")
    for k in keys:
        if k in reports: return reports[k]
    # compound report stems (e.g. migptwindowsvmbluesky) start with the brand
    for rk,fn in reports.items():
        for k in keys:
            if len(k) >= 4 and rk.startswith(k): return fn
    return None

# ---- category grouping (normalize _v112 suffix) ----
def prim_cat(cats):
    if not cats: return "其它"
    c = cats[0].replace("_v112","").strip()
    return c or "其它"

CAT_ORDER = ["AI","Productivity","Developer Tools","Creativity","Fun","Lifestyle","Utilities","其它"]
groups = {c:[] for c in CAT_ORDER}
for b,row in best.items():
    c = prim_cat(row["cats"])
    if c not in groups: groups.setdefault(c,[])
    groups.setdefault(c,[]).append(row)

# ---- emit ----
total = len(best) + len(model_rows)
have = 0
lines = []
lines.append("# market/apps.md — Olares Market 应用清单")
lines.append("")
lines.append(f"> 从 [terminus-apps/](/Users/pengpeng/terminus-apps)（`beclab/apps` 本地克隆）的 365 个 manifest 收敛去重而来，共 **{total}** 个用户可见品牌应用。每个应用的 brand-seo-research 报告放在 [reports/](/Users/pengpeng/seo/directions/market/reports)。用途/对标见各条；写新报告走 `.cursor/skills/brand-seo-research/`。")
lines.append("")
lines.append("**去重规则**：版本变体保留最新（v3>v2>无后缀）；模型服务变体（`ollama*`/`vllm*`/`sglang*`/`llamacpp*`/`xinference*` 共 68 个）折叠为 5 个引擎品牌，型号清单见 [model/keywords.md](/Users/pengpeng/seo/directions/model/keywords.md)；剔除 test*/`*client`/`*share`/`*fusion`/`*pure`/`*forcluster` 等伴生 chart 与纯中间件/数据库。")
lines.append("")
lines.append("状态：✅ 已有报告 ｜ ⏳ 待做")
lines.append("")

def emit_row(row):
    global have
    fn = report_for(row)
    if fn:
        have += 1
        st = f"✅ [报告](/Users/pengpeng/seo/directions/market/reports/{fn})"
    else:
        st = "⏳"
    desc = row.get("desc","") or ""
    return f"| {row['title']} | {desc} | {st} |"

# model-serving section first
lines.append(f"## {CAT_MODEL}（{len(model_rows)}）")
lines.append("")
lines.append("| 应用 | 说明 | 报告 |")
lines.append("|------|------|------|")
for k in ["ollama","vllm","sglang","llamacpp","xinference"]:
    lines.append(emit_row(model_rows[k]))
lines.append("")

CAT_ZH = {"AI":"AI","Productivity":"生产力 / 协作","Developer Tools":"开发者工具",
          "Creativity":"创意 / 设计 / 媒体生成","Fun":"娱乐 / 媒体库","Lifestyle":"生活 / 家居 / 健康",
          "Utilities":"实用工具 / 网络 / 存储","其它":"其它"}
for c in CAT_ORDER:
    rows = sorted(groups.get(c,[]), key=lambda r:r["title"].lower())
    if not rows: continue
    lines.append(f"## {CAT_ZH.get(c,c)}（{len(rows)}）")
    lines.append("")
    lines.append("| 应用 | 说明 | 报告 |")
    lines.append("|------|------|------|")
    for r in rows:
        lines.append(emit_row(r))
    lines.append("")

lines.append("---")
lines.append(f"> 报告覆盖：{have}/{total} 已有。其余增量补齐。")

open(OUT,"w",encoding="utf-8").write("\n".join(lines)+"\n")
print("WROTE", OUT, "total", total, "have", have)
# show category counts
for c in CAT_ORDER:
    print(c, len(groups.get(c,[])))
# list apps with no title metadata (potential leftovers)
# which market reports did NOT get matched to an app?
matched = set()
for r in list(best.values()) + list(model_rows.values()):
    fn = report_for(r)
    if fn: matched.add(fn)
allrep = set(os.path.basename(f) for f in glob.glob(os.path.join(SEO_DIR,"*.md")))
unmatched = sorted(allrep - matched)
print("UNMATCHED_REPORTS:", " ".join(re.sub(r"-\d{4}.*","",x) for x in unmatched))
