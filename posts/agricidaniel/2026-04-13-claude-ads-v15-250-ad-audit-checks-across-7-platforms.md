# claude-ads v1.5: 250+ Ad Audit Checks Across 7 Platforms

**Date:** 2026-04-13 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-ads-v1-5-release

---

## What Changed in claude-ads v1.5?
claude-ads v1.5 adds 22 new audit checks, 3 new skills, and a PDF report generator. Total coverage is now 250+ checks across 7 ad platforms, all updated with 2025-2026 platform research. The biggest jumps: Apple Ads goes from 0 to 35+ checks, Google Ads from 62 to 80, and Meta from 48 to 50.
Key changes in this release:
* **Apple Ads support:** 35+ checks covering Custom Product Pages, Maximize Conversions bidding (GA Feb 2026), and Search tab placements
* **Google Ads updates:** 80 checks now include AI Max for Search, Smart Bidding Exploration (+18% queries per Google), and ECPC deprecation flags
* **3 new skills:** `/ads math` for PPC calculators, `/ads test` for A/B test design, `/ads report` for PDF generation
* **PDF report generator:** client-ready deliverables with inline charts, health scores, and prioritized findings
* **Security fixes:** SSRF protection on URL inputs, path traversal fix in screenshot capture
* **Scoring overhaul:** severity multipliers recalibrated, Quick Wins section added to every audit
Key Takeaways
* 250+ weighted audit checks across 7 platforms: Google (80), Meta (50), Apple (35+), TikTok (28), LinkedIn (27), Microsoft (24), YouTube (15)
* 3 new skills: `/ads math` for PPC calculators, `/ads test` for A/B test design, `/ads report` for PDF generation
* Severity-weighted scoring with Critical 5.0x, High 3.0x, Medium 1.5x, Low 0.5x multipliers across 6 categories
* 100% local analysis, zero data leaves your machine. Open source, MIT licensed.
Platform Coverage Grid
250+ weighted audit checks across 7 advertising platforms
Google Ads
80 checks
Search
PMax
AI Max
Meta Ads
50 checks
Pixel/CAPI
Andromeda
LinkedIn Ads
27 checks
B2B
TLA
Lead Gen
TikTok Ads
28 checks
Creative
Smart+
Shop
Microsoft Ads
24 checks
Copilot
CTV
Import
Apple Ads
35+ checks
CPPs
Max Conv
YouTube
15 checks
Shorts
DemandGen
CTV
Platform coverage grid: 250+ weighted audit checks distributed across 7 platforms
claude-ads v1.5 in action - parallel agents auditing ad accounts
## What Did the 2026 Platform Research Reveal?
Digital ad spend is projected to hit $870 billion globally in 2027, growing at 10% CAGR ([Statista](https://www.statista.com/outlook/dmo/digital-advertising/worldwide), 2026). We reviewed official documentation, case studies, and API changelogs across all 7 platforms. Five findings changed how the tool works. Each one led to new checks, updated benchmarks, or removed recommendations that were no longer accurate.
**1. Meta's Andromeda clusters similar ads.** Meta's retrieval engine (Andromeda, per their 2023 engineering blog) groups creatively similar ads before auction. Running 100 ad variations that share the same hook, format, and CTA produces no incremental reach over 10 well-differentiated variants. The tool now flags creative clustering risk when variation count exceeds 10 per ad set without meaningful creative diversity.
**2. LinkedIn Maximum Delivery is the most expensive bidding option.** LinkedIn's own campaign manager documentation confirms Maximum Delivery consistently produces the highest CPCs across campaign types. The audit now recommends starting with Manual CPC and only testing Maximum Delivery after establishing baseline performance data.
**3. Google ECPC is fully deprecated as of March 2025.** Enhanced CPC was sunset in March 2025 per Google Ads Help Center. Campaigns still referencing ECPC get flagged as critical. The replacement recommendation is Smart Bidding Exploration, which Google's internal data (Search Ads 360 release notes) shows delivers +18% more search queries and +19% more conversions on average.
**4. TikTok creative lifespan compressed to 7-10 days under Smart+.** TikTok's Creative Center data and advertiser community reports confirm that Smart+ campaigns cycle through creatives faster than manual campaigns. The creative fatigue check now uses a 7-day window instead of 14 days for Smart+ campaigns.
**5. Apple rebranded to "Apple Ads" with Maximize Conversions GA Feb 26, 2026.** Apple Search Ads is now Apple Ads (per Apple's developer documentation update, Q4 2025). Maximize Conversions bidding went generally available on February 26, 2026. The new Apple Ads skill covers Custom Product Pages, Search tab placements, and the new bidding strategy.
## How Do 250+ Audit Checks Work?
The tool runs 6 parallel agents that evaluate your ad accounts simultaneously. Each agent handles a specific domain: Google (80 checks), Meta (50 checks), creative quality (21+ checks), conversion tracking (8+ checks), budget allocation (24 checks), and compliance (18+ checks). A full audit completes in 3-5 minutes.
The system uses a 3-layer architecture. The **directive layer** (ads/SKILL.md) handles routing, quality gates, and orchestration. The **orchestration layer** deploys 6 audit agents as forked tasks that run in parallel. The **execution layer** contains 25 reference files, 19 sub-skills, and 12 industry-specific templates. Each layer can operate independently; the orchestrator never needs to wait for a reference file to load before dispatching agents.
DIRECTIVE LAYER
ads/SKILL.md
Orchestrator · Routing · Quality Gates
ORCHESTRATION LAYER
audit-google
80 checks
audit-meta
50 checks
audit-creative
21+ checks
audit-tracking
8+ checks
audit-budget
24 checks
audit-compliance
18+ checks
EXECUTION LAYER
25 References
On-demand knowledge
19 Sub-Skills
Specialized analysis
12 Templates
Industry-specific
3-layer architecture: directive routes commands, orchestration dispatches parallel agents, execution provides knowledge and tools
/ads audit
audit-google
80
audit-meta
50
audit-creative
21+
audit-tracking
8+
audit-budget
24
audit-compliance
18+
Unified Health Score (0-100)
Parallel audit flow: /ads audit dispatches 6 agents simultaneously, results merge into a unified health score
## How Does the Health Score Scoring Work?
Every check gets a severity multiplier (Critical 5.0x, High 3.0x, Medium 1.5x, Low 0.5x) and a category weight. The weighted formula produces a 0-100 score with an A through F grade. A failed Critical check in the Conversion Tracking category (25% weight) costs 1.25 points. A failed Low check in Settings (10% weight) costs 0.05 points. This means the tool prioritizes what actually costs you money.
The six scoring categories and their weights: Conversion Tracking (25%), Wasted Spend (20%), Structure (15%), Keywords (15%), Ads (15%), Settings (10%). These weights come from analyzing which categories correlate most strongly with wasted ad spend. Conversion tracking failures are weighted highest because if your tracking is broken, every optimization decision downstream is wrong.
New in v1.5: every audit now includes a **Quick Wins** section. These are the 3-5 highest impact, lowest effort fixes from your results. A typical Quick Win might be "Add 12 negative keywords to Campaign X to eliminate $2,100/mo in irrelevant clicks." The tool calculates estimated savings based on your actual spend data and the severity of each finding.
Weighted Scoring Algorithm
Weighted Scoring Algorithm
Score = S(Pass x Severity x CategoryWeight) / S(Total x Severity x CategoryWeight) x 100
Category Weights
6 categories
Conversion Tracking (25%)
Wasted Spend (20%)
Structure (15%)
Keywords (15%)
Ads (15%)
Settings (10%)
Severity Multipliers
Critical
5.0x
High
3.0x
Medium
1.5x
Low
0.5x
Example Impact
Failed Critical check in Conversion Tracking:
Impact = 5.0 (severity) x 0.25 (category) = 1.25 pts
Weighted scoring algorithm: severity multipliers combined with category weights produce a 0-100 health score
## What Are the 3 New Skills?
Manual calculations and reporting are recurring PPC tasks. v1.5 ships three new skills that extend the tool beyond auditing into financial modeling, experimentation design, and client reporting. Each one works standalone or as part of a full audit workflow.
**`/ads math`: 7 PPC financial calculators.** CPA calculator, ROAS calculator, break-even ROAS, LTV:CAC ratio, budget forecaster, impression share estimator, and margin-aware bidding. You paste in your numbers, the tool does the math and explains what each result means for your campaigns. No spreadsheets needed. Example: "What CPA do I need at a 4x ROAS target with a $45 average order value and 62% gross margin?" The tool solves it in seconds.
**`/ads test`: A/B test design with IF/THEN/BECAUSE.** Generates a complete test plan: hypothesis statement, control and variant definitions, primary and secondary metrics, minimum sample size calculation (based on your baseline conversion rate and minimum detectable effect), and test duration estimate. Every hypothesis follows the IF/THEN/BECAUSE format to force clear thinking. Example output: "IF we add social proof to the landing page headline, THEN conversion rate will increase by 15%, BECAUSE exit survey data shows 34% of bounced visitors cited trust concerns."
**`/ads report`: PDF generation with charts.** Generates a client-ready PDF audit report with the health score, prioritized findings, inline charts, and recommended next steps. Uses Python's ReportLab for PDF generation and matplotlib for charts. The output is a professional deliverable you can hand directly to a client or stakeholder without reformatting.
Creative Pipeline - 5 Stages
Creative Pipeline
1
Brand DNA
ads-dna
Extract brand
identity + voice
2
Strategy
creative-strategist
Campaign concepts
+ messaging
3
Visuals
visual-designer
Image direction
+ specifications
4
Copy
copy-writer
Ad headlines,
descriptions
5
Validate
format-adapter
Platform specs
+ compliance
Each agent runs as a forked Task: parallel where possible, sequential where dependent
Creative pipeline: 5-stage workflow from brand DNA extraction through platform-specific validation
## How Does It Handle Security and Privacy?
Data breaches cost companies an average of $4.88 million per incident ([IBM](https://www.ibm.com/reports/data-breach), 2024). All analysis happens locally. No ad account data leaves your machine. The tool processes your exported data, screenshots, and pasted metrics entirely within your Claude Code session. There is no telemetry, no external API calls for analysis, and no data persistence between sessions.
Two security fixes in v1.5:
* **SSRF protection:** URL inputs in the landing page analyzer and screenshot capture scripts now validate against internal IP ranges (RFC 1918, link-local, loopback). Previously, a crafted URL could trigger requests to internal network endpoints.
* **Path traversal fix:** The screenshot capture script now sanitizes file paths to prevent directory traversal via `../` sequences in output filenames.
If you need live API access to your ad platforms (for real-time data pulls instead of pasted exports), the tool supports MCP server connections. These are optional, explicitly configured by you, and only make read-only API calls. The tool never modifies your ad accounts.
Data Privacy Architecture
Data Privacy Architecture
YOUR MACHINE
Claude Code
claude-ads skill
Analysis Engine
PDF Generator
Ad Platforms
Google Ads
Meta Ads
LinkedIn Ads
TikTok Ads
Microsoft Ads
Apple Search Ads
Optional:
MCP API calls only
All analysis happens locally on your machine
Data privacy architecture: all processing stays on your machine, platform connections are optional and read-only
## How Do You Install and Get Started?
claude-ads v1.5 is available now on [GitHub](https://github.com/AgriciDaniel/claude-ads) ([release notes](https://github.com/AgriciDaniel/claude-ads/releases/tag/v1.5.0)).
The fastest way to install is the Claude Code plugin system. Open Claude Code and run:
```
/install-skill https://github.com/AgriciDaniel/claude-ads
```
Or use the one-liner for manual installation:
```
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/install.sh | bash
```
After installation, run `/ads audit` to start a full audit, or use any of the 19 sub-skills directly. The tool works with pasted data (copy metrics from your ad platform dashboards), exported CSVs, or live MCP API connections.
* GitHub: [github.com/AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads)
* Previous release post: [claude-ads v1.4 announcement](/blog/claude-code-ad-agency)
* Full AI marketing stack: [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack)
**Full release notes:** [v1.5.0 on GitHub](https://github.com/AgriciDaniel/claude-ads/releases/tag/v1.5.0)
**From my experience:** I ran v1.5 on three real ad accounts during testing. The biggest finding was consistent: most accounts lose 15-30% of their budget on search terms that should be negative keywords. The Quick Wins section now surfaces these immediately, before anything else. One account saved $2,100/month just from the negative keyword recommendations alone.
## Frequently Asked Questions
### Does it connect to my ad accounts automatically?
No. By default, you paste data or upload exported CSVs. The tool analyzes what you provide locally. If you want live API access, you configure MCP server connections yourself. These are optional, use read-only permissions, and the tool will never create, modify, or delete anything in your ad accounts.
### How accurate are the benchmarks?
Benchmarks are sourced from platform documentation, published case studies, and industry reports (Google Ads Help Center, Meta Business Help Center, LinkedIn Marketing Solutions, WordStream, Databox). Each benchmark cites its source. They are updated with each release. If your industry has unusual economics (e.g., enterprise SaaS with 18-month sales cycles), the tool accounts for that when you specify your vertical in `/ads plan`.
### Can it create or edit ads?
The creative pipeline (`/ads creative`, `/ads generate`, `/ads photoshoot`) generates ad copy, image prompts, and creative briefs. It does not push changes to your ad platforms. You take the output and implement it yourself. This is intentional: automated ad creation without human review is how you get compliance violations and brand damage.
### What platforms does it support?
Seven platforms: Google Ads (80 checks), Meta Ads (50 checks), Apple Ads (35+ checks), TikTok Ads (28 checks), LinkedIn Ads (27 checks), Microsoft Ads (24 checks), and YouTube Ads (15 checks). YouTube checks are separate from Google Ads because video campaign optimization has different signals and benchmarks. Total: 250+ weighted audit checks.
### Is it really free?
Yes. MIT licensed, no usage limits, no premium tier, no gated features. You need a Claude Code subscription ($20/month for Pro or $200/month for Max) because the tool runs inside Claude Code. The tool itself is free and open source. There is no hosted version and no plans for one.
Learn more [about me](/about) and the full suite of AI marketing tools I'm building. For the complete open-source stack, check [my AI marketing automation breakdown](/blog/ai-marketing-automation-stack).
## Related Posts
* [Claude Code Just Replaced Your Ad Agency](/blog/claude-code-ad-agency) - The original v1.4 release with 186 checks across 6 platforms
* [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack) - The full open-source AI marketing stack at $50/month
* [Best Claude Code Skills in 2026](/blog/best-claude-code-skills-2026) - The definitive guide to top Claude Code skills ranked by GitHub stars
Join 4,500+ AI Marketing Builders
Get workflow templates, automation blueprints, and connect with SEOs, agency owners, and creators who ship.
[JOIN FREE](https://www.skool.com/ai-marketing-hub)
