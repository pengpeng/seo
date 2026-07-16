# Panther Lake SoC for AI Box & NAS

A full Olares AI Box with NAS and Windows VM capabilities—led by Private Meeting AI today, then expanding to Smart Home and Personal Agent as models improve.

## THE CASE

### Meeting intelligence is already a large paid market—in two forms.

- **A large, fast-growing market.** The AI meeting-assistant market was estimated at $3.1–3.5B in 2025; forecasts exceed $9B by 2030 at ~25% CAGR.
- **Hardware recorders monetize in-person conversations.** Plaud pairs a $185 device with a $240/yr plan, reaching >2M devices and >$100M software ARR.
- **Meeting software monetizes online conversations.** Otter.ai reports >35M users, >1B meetings processed and >$100M ARR.

### Yet leading products still rely on cloud AI processing.

- **Third-party processing complicates control.** Sending audio or transcripts to cloud AI makes data residency, access and retention harder to govern under HIPAA and GDPR.
- **Sensitive conversations are the daily work.** Lawyers, doctors, salespeople and journalists need institutional control over where that knowledge lives.

## THE SOLUTION

### Private Meeting AI fits Panther Lake today: small models, asynchronous work.

| Stage | What it does | Open models | Tier |
|-------|--------------|-------------|------|
| Speaker diarization | Labels who spoke when | pyannote · WeSpeaker | Required |
| Speech-to-text | Audio to text | Qwen3-ASR-1.7B | Required |
| Forced alignment | Word-level click-to-play | Qwen3-ForcedAligner-0.6B | Required |
| Translation | Cross-language transcript | MADLAD-400 | Optional |
| Summary / Q&A | Meeting summary and ask-the-meeting | Qwen3-4B · Phi-4-mini | Optional |

- **Private Meeting AI requires a five-stage local pipeline;** the three required stages target Panther Lake NPU / CPU without a discrete GPU.

### A full Olares AI Box—with Private Meeting AI as the lead workload.

- **Intel SoC makes the team economics work.** Five Plaud subscriptions cost ~$3,600 over three years; a target $999–1,599 local box implies ~10–16 months of hardware payback.
- **Olares makes it ready to use.** Pre-integrated models, anywhere access, team collaboration, identity, permissions and app sandboxes turn the SoC into a ready-to-use product.
- **Institution-controlled by design.** Audio, transcripts and knowledge stay on the institution's hardware, reducing third-party cloud exposure.

## ECOSYSTEM & NEXT

### From IoT capture devices to meeting software: an open ecosystem feeding one local knowledge base.

- **Capture conversations anywhere.** Recording cards, AI earbuds, speakerphones, phones, wearables and room systems cover in-person, phone and mobile work.
- **Bring online meetings into the same system.** Planned connectors for Zoom, Teams and Google Meet consolidate transcripts locally.
- **Start with a confirmed recording-device partner.** Mobvoi (HKEX: 2438) brings the TicNote Card and 4G dual-channel TicNote Pods.

### Start with Private Meeting AI; expand as local models become more capable.

- **Now — Private Meeting AI.** Small models and asynchronous processing match current Panther Lake.
- **Next — Smart Home voice.** Reuse the always-on box, microphones and local speech stack.
- **Later — Personal Agent.** Better small models and faster long-context prefill expand the same installed base into agentic work.
