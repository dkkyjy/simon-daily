# Local SEO Brain: Claude Code Agent for Ranking Local Businesses in the Map Pack

**Date:** 2026-05-21 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-code-local-seo-brain

---

## What is Local SEO Brain?
Local SEO Brain is a source-cited Obsidian operating brain + AI-agent skill that ranks local businesses in the Google Map Pack, organic local SERPs, and AI search. It ships 59 knowledge-base chapters, 37 reusable AI prompts, 31 reference images, and 1,271 wikilinks, plus an approval-first agent script layer that runs through Claude Code, Codex, or Gemini. Setup takes ~30 minutes per client. Then the agent ingests your GBP exports, citation crawls, review feeds, and geo-grid scans into one Obsidian memory and synthesizes a prioritized audit — with every recommendation linked back to the raw export it came from.
Watch the full 6-minute walkthrough:
Local SEO Brain on YouTube — 6:18 walkthrough by Daniel Agrici.
## The Problem: 60+ Hours of Spreadsheet Audits per Client
Most local-SEO agencies bill 60 or more hours per client audit. The work is real — GBP exports from Google Business Profile, citation crawls from Whitespark or BrightLocal, geo-grid scans from Local Falcon, review feeds, on-page audits, backlink mapping — and most of it ends up scattered across Google Sheets and screenshots. The "synthesis" then happens in someone's head on a Tuesday call.
Generic AI tools do not fix this. ChatGPT hallucinates GBP metrics. Claude does not have your Local Falcon export open in another tab. Gemini will happily invent backlinks that do not exist. What was missing was a structured operating brain that ingests real local-SEO data and gives an AI agent the context to write a useful audit.
Fragmented spreadsheets and screenshots become one source-cited Obsidian memory.
## What's in the Box
Local SEO Brain ships two artifacts in one bundle. The first is a buyer-facing Obsidian vault seeded with a complete local-SEO knowledge base — 59 chapters across the 3 Phases, Core 30 content strategy, GBP playbooks, audits, citations, backlinks, E-E-A-T, and LLM SEO. The second is the agent-facing operating layer: a SKILL.md contract plus a scripts/ folder that scaffolds per-client vaults, ingests raw data, and synthesizes source-cited audits.
* **assets/template-brain/** — Obsidian vault following the Hot/Index/Wiki pattern, seeded with the 3 Phases, Core 30 content strategy, GBP optimization playbooks, audits across property/content/technical/CTR, local citations, backlinking, E-E-A-T, and LLM SEO. Includes a 2026 freshness overlay so stale chapters carry warning callouts and current-state links.
* **SKILL.md + scripts/** — agent-facing operating layer. Scaffolds per-client vaults, re-seeds the knowledge base idempotently, ingests raw sources (GBP, citations, reviews, geo-grid), synthesizes a source-cited audit + action roadmap, lints the graph, and renders client-ready deliverables. Zero Python dependencies in V1 — runs on the standard library.
The seeded vault — 200+ nodes, 1,271 wikilinks, color-coded by folder.
## How It Works: Karpathy's Hot/Index/Wiki Memory Pattern
Every vault scaffolded by Local SEO Brain follows Andrej Karpathy's three-layer context pattern, adapted from his agent-memory talks. The pattern keeps the agent's working set tight while letting the underlying vault grow without choking the context window.
* **wiki/hot.md** — small working-memory file. What changed, what is blocking, what to do next.
* **wiki/index.md** — full navigation map. Section-grouped wikilinks across the vault.
* **wiki/** — deep notes loaded on demand through wikilinks and hubs.
For any cross-agent session you point the agent at the vault with: *"Read CODEX.md, then wiki/hot.md, then wiki/index.md, then the relevant note."* The brain always has a tight working set and pulls deep context on demand.
Karpathy's three-tier memory pattern, applied to local SEO.
## The 3 Phases of Local SEO Ranking
The brain teaches and operationalizes a three-phase strategic frame across the frameworks/, audits/, and gbp/ folders. Property, then GBP, then Authority — in that order, because skipping a phase wastes everything stacked on top of it.
### Phase 1 — Property (the website foundation)
Your website is the foundation. Without a properly audited site (E-E-A-T, Core 30 pages, technical health, CTR-optimized metadata, industry-specific schema subtypes), nothing else compounds. The brain ships property audits for technical, on-page, content, and CTR, plus the Core 30 content map that builds topical authority and earns the behavioral signals the December 2025 Core Update rewards.
### Phase 2 — GBP (the storefront)
Your Google Business Profile is the storefront. 60-70% of local clicks come from the Map Pack. The GBP folder covers verification through posts, geotagging, services, categories, holiday hours, NAP consistency, and the messaging-and-Q&A surface. The Claude Code agent ingests your GBP Insights export and writes a prioritized GBP roadmap with provenance.
The Map Pack is the storefront — 60-70% of local clicks happen here.
### Phase 3 — Authority (citations, backlinks, reviews, AI-citation share)
Trust signals from third-party websites. Local citations, competitive backlink research, social signals, review velocity, and AI-citation share across ChatGPT, Perplexity, Google AI Overviews, and Bing Copilot. Claude Code ingests Local Falcon / Whitespark / BrightLocal / Moz Local exports and synthesizes a prioritized authority roadmap.
## LLM SEO for Local: The 2026 Freshness Layer
Local SEO Brain ships a dedicated llm-seo/ folder covering what matters for showing up in ChatGPT, Perplexity, Google AI Overviews, and Bing Copilot — four signals that did not exist as ranking factors two years ago but now drive a measurable share of local discovery:
* **Reddit citation engine.** Reddit sits at roughly 40% of LLM citation share. The brain ships a playbook for earning Reddit citations in r/localBusiness subs without violating sub rules.
* **Person schema.** Load-bearing post-December-2025 for E-E-A-T attribution. The brain templates Person schema for the business owner, key staff, and contributing authors.
* **Industry-specific schema subtypes.** Generic LocalBusiness is no longer enough. The brain ships subtypes for Plumber, Restaurant, Dentist, HomeAndConstructionBusiness, AutoRepair, and more.
* **AI Overview Map Pack pressure.** Citation patterns have stabilized to 3 to 5 sources per AI Overview. The brain optimizes for inclusion in that tight set.
The 2026 freshness layer overlays the original knowledge base with current-state notes so stale references — sunset GBP Chat, retired LLM model names, the December 2025 Core Update, Reddit citation share — are flagged in-place with warning callouts.
## What the Audit Output Looks Like
After running `synthesize_brain.py` against the seeded sample vault, the Claude Code agent emits a Health Scorecard with phase grades, top 5 prioritized actions, and an Approval Queue. Every recommendation carries a `source:` line — if the supporting raw file is missing, the recommendation does not ship.
A real Health Scorecard from one run of the brain on the demo vault.
```
# acme-plumbing · Health Scorecard
> Generated 2026-05-20 · sources verified
## Phase grades
| Phase     | Grade | Top issue                                              |
|-----------|-------|---------------------------------------------------------|
| Property  | C+    | Homepage missing LocalBusiness > Plumber schema subtype |
| GBP       | B-    | 3 services missing in primary category                  |
| Backlinks | D     | 14-citation gap vs top-3 competitors                    |
| LLM SEO   | C     | No Reddit presence; Person schema missing on About      |
## Top 5 priorities (sourced)
1. Add Plumber schema subtype to homepage
   source: .raw/sources/property-audit.csv:42 · sha256: 9a3f...
2. Fill 3 missing services in primary GBP category
   source: .raw/sources/gbp-export.csv:18 · sha256: 4c12...
3. Close 14 citation gap (BBB, Yelp, Angi, HomeAdvisor + 10)
   source: .raw/sources/whitespark.csv:1-203 · sha256: e7b9...
4. Build 1 Reddit answer in r/Plumbing per week, cite owner photo
   source: wiki/llm-seo/Reddit-LLM-Citation-Engine.md
5. Publish location pages for top 4 service-area suburbs
   source: wiki/audits/Topical-Geo-Relevance.md
## Approval queue
- [ ] Schema markup change (rollback: revert deploy)
- [ ] GBP service additions (rollback: re-delete from owner UI)
```
## Six Use Cases the Brain Handles Out of the Box
Claude Code Local SEO Brain is built for the work agencies and operators actually do, not for an abstract "AI SEO" demo. Six scenarios ship with playbooks:
| Scenario | What you run | What you get |
| --- | --- | --- |
| **New client kickoff** (single location) | `scaffold_vault` → ingest 4 sources → `synthesize_brain` | Day-1 health scorecard, prioritized roadmap, citation gap |
| **Multi-location audit** (chain of 12 stores) | One scaffold per location, parallel ingest, chain-level synthesis | Per-location grade matrix, shared NAP issues, chain-wide citation gaps |
| **AI search visibility check** | Ingest GBP + run `llm-seo/` prompts against GPT-5 / Claude / Gemini | Brand mention diff, Reddit gap, schema modernization checklist |
| **Quarterly review** (existing client) | Re-run all ingestors, lint, render report | Velocity report: what shipped, what slipped, what is next |
| **Competitor teardown** (one rival) | Ingest competitor backlinks + GBP profile via `competitors/` template | Gap analysis with sourced opportunities |
| **Property handoff** (agency to in-house team) | Render full vault to HTML | Static, searchable, source-cited handover bundle |
## Refusal Rules: What the Brain Will Not Do
Most local-SEO automation drifts toward the gray-hat tactics that get accounts suspended. Local SEO Brain ships refusal rules baked into the prompt layer — the agent refuses to recommend or generate any of the patterns that violate Google's spam policies or risk a GBP suspension.
The brain refuses fake reviews, proximity gaming, GBP category gaming, and "rank #1 guaranteed" copy.
## Who Local SEO Brain Is For
| Buyer | What they get |
| --- | --- |
| **Local SEO agencies & freelancers** (5 to 50 client locations) | A repeatable, source-cited operating layer that replaces spreadsheet audits and screenshot dumps. |
| **Multi-location operators** (10+ locations) | A per-location memory layer for NAP, citations, reviews, geo-grid scans, and audit history. |
| **SAB businesses doing SEO in-house** (plumbers, HVAC, law, dental, home services) | A playbook + memory in one. The brain knows what to do *and* remembers what was already done. |
## How to Get Local SEO Brain
Two ways to grab Local SEO Brain — pick the path that fits how you want to work.
* **Bundle** — included in [AI Marketing Hub PRO](https://skool.com/ai-marketing-hub-pro) alongside the rest of the brain library, community support, and access to every brain release as it ships.
* **One-off** — grab the vault for $69 on [Gumroad](https://erniseth.gumroad.com/l/localseobrain). Same vault, no community. Upgrade to PRO any time you want the next brain release.
Other tools and open builds live at [github.com/AI-Marketing-Hub](https://github.com/AI-Marketing-Hub). For a complete tour of Local SEO Brain in action, [watch the 6-minute walkthrough on YouTube](https://youtu.be/4v7116sEbrQ).
## What's Next in the Brain Series
Local SEO Brain is the first in a series. The same Hot/Index/Wiki memory pattern + source-cited synthesizer applies to other marketing surfaces — each gets its own playbook library and ingestor set. Roadmap:
* **Marketing Brain** — full-funnel ICP / messaging / content / channel orchestration
* **Mailing List Brain** — list growth + segmentation + send-strategy
* **E-commerce Brain** — product catalog + PMax + review-mining + retention loops
* **B2B SaaS Brain** — content-led + ABM + lifecycle orchestration
Reply on the [YouTube video](https://youtu.be/4v7116sEbrQ) with which brain you want built next — input shapes the roadmap.
