# Claude Code Just Replaced Your Ad Agency - 250+ Checks in One Command

**Date:** 2026-03-25 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-code-ad-agency

---

## Your Ad Agency Charges $10K/Month to Read Dashboards
I'm going to say something that will upset a lot of media buyers: most ad agency "audits" are someone junior logging into your ad accounts, screenshotting some graphs, and pasting them into a deck with their logo on it. **You're paying $5,000 to $10,000 per month for a process that can be fully automated.**
I know because I've been on both sides. I've hired agencies. I've seen the deliverables. And now I've built a tool that does what they do, except it runs 250+ checks instead of the 15-20 a human realistically covers, and it does it in minutes instead of weeks.
It's called [claude-ads](https://github.com/AgriciDaniel/claude-ads), it's open source, one of the [top Claude Code skills in 2026](/blog/best-claude-code-skills-2026), and it just hit 42,000 views on the demo video alone.
v1.5 Update (April 2026)
250+ audit checks (was 186). 7 platforms (added Apple Ads). 3 new skills: PPC calculator, A/B test designer, PDF report generator. All platform best practices updated with 2025-2026 research. SSRF protection and security hardening. [Read the full v1.5 release notes.](/blog/claude-ads-v1-5-release)
## 250+ Checks Across 7 Platforms
When you run `/ads audit` in Claude Code, 6 parallel agents analyze your ad accounts simultaneously. Here's what gets covered:
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
250+ audit checks distributed across 7 ad platforms
### Google Ads (80 checks)
* Conversion tracking validation, Enhanced Conversions, Consent Mode V2 compliance
* Search term waste analysis with negative keyword gap detection
* Quality Score optimization with keyword-level breakdowns
* Smart Bidding strategy audit (ECPC deprecated March 2025, tCPA/tROAS/Maximize recommended)
* Performance Max asset density, brand exclusions, campaign-level negatives
* AI Max for Search evaluation (14% avg conversion lift)
* Demand Gen campaigns (replaced Video Action Campaigns April 2026)
* CTV measurement (Floodlight does NOT work on CTV devices)
### Meta Ads (50 checks)
* Pixel and Conversions API health with EMQ scoring (target: Purchase 8.5+, AddToCart 6.5+)
* Andromeda creative diversity (Similarity Score >60% = retrieval suppression)
* Creative fatigue detection (lifespan compressed to 14-21 days under Andromeda)
* Audience overlap analysis and Advantage+ Sales structure
* Placement performance and cost per result trends
* Threads placement evaluation (emerging, ~0.04% of spend)
### YouTube Ads (15 check IDs)
* Skippable, Non-Skippable, Bumper, Shorts, and Demand Gen format evaluation
* Hook quality analysis (first 5 seconds), ABCD creative framework
* CTV measurement strategy (75% of YouTube ad spend now on CTV)
* Frequency management and audience targeting
### LinkedIn Ads (27 checks)
* Company size, seniority, and ABM targeting efficiency
* Thought Leader Ads evaluation (CPC $2.29-4.14 vs $13.23 standard)
* Lead gen form completion rates vs industry benchmarks
* Manual CPC bidding recommended first (Maximum Delivery is most expensive)
* CRM integration with Salesforce/HubSpot for revenue attribution
* EU Sponsored Messaging compliance (discontinued Jan 2022)
### TikTok Ads (28 checks)
* Spark Ads vs standard creative performance (+30% completion, +142% engagement)
* Hook rate analysis and creative lifespan monitoring (7-10 day average)
* Smart+ modular control (lock targeting, creative, budget, placement independently)
* GMV Max mandatory for TikTok Shop (July 2025)
* Search Ads toggle (20% conversion uplift with In-Feed)
* Events API Gateway with ttclid passback
### Microsoft Ads (24 checks)
* Google Ads import validation and scheduled import safety checks
* Copilot ad placement evaluation (+73% CTR vs traditional search)
* LinkedIn Profile Targeting (16% greater CTR, 64% greater CVR)
* CTV campaigns, Video ads (9:16 vertical April 2025)
* Consent Mode deadline (May 5, 2025 for EEA/UK)
* CPCs 30-70% cheaper than Google (the underestimated competitor)
### Apple Ads (35+ checks)
* Campaign structure (BOFU/MOFU/Search Match), bid health, Custom Product Pages
* Maximize Conversions bidding (GA Feb 26, 2026, installs only)
* AdAttributionKit dual attribution (April 10, 2025)
* 78% of App Store search volume from devices with Personalized Ads off
* TAP placement coverage (Today, Search, Product Pages)
## How the Parallel Audit Works
When you run `/ads audit`, 6 specialized agents launch simultaneously. Each handles a specific domain. They run in parallel, not sequentially, so a full audit across all platforms takes minutes.
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
Unified Health Score (0–100)
6 parallel agents analyzing your ad accounts simultaneously
## How the Scoring Works
Every check gets a severity multiplier (Critical 5.0x, High 3.0x, Medium 1.5x, Low 0.5x) and a category weight. The weighted formula produces a 0-100 health score with an A through F grade. Critical findings dominate the score, which means a single broken conversion tracking setup tanks your grade regardless of how clean everything else is.
Weighted Scoring Algorithm
Weighted Scoring Algorithm
Score = Σ(Pass × Severity × CategoryWeight) / Σ(Total × Severity × CategoryWeight) × 100
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
Impact = 5.0 (severity) × 0.25 (category) = 1.25 pts
Weighted scoring algorithm with severity multipliers and category weights
## What the Output Actually Looks Like
You don't get a 60-slide deck. You get a **prioritized, scored list of issues ranked by estimated revenue impact**. Each finding includes:
* The specific problem (e.g., "Campaign X has 23% search term waste - $4,200/mo in irrelevant clicks")
* Severity rating (critical / high / medium / low) with weighted multiplier
* Exact fix with step-by-step instructions
* Estimated monthly savings or revenue lift
* Quick Wins flagged for fixes under 15 minutes
The critical findings alone, conversion tracking gaps, budget allocation errors, audience overlap, typically identify **15-30% wasted ad spend**. On a $50K/month ad budget, that's $7,500-$15,000 in savings found in one command.
New in v1.5: `/ads report` generates a professional PDF with health score gauge, platform comparison charts, and formatted tables you can hand directly to clients.
250+ point ad audit completing in minutes, not weeks
## 3 New Tools (v1.5)
Beyond the audit, v1.5 added three skills that fill gaps no competitor covers:
* **/ads math**: PPC financial calculator with 7 tools (CPA, ROAS, break-even, impression share, budget forecasting, LTV:CAC, MER). Works offline with pasted data from exports.
* **/ads test**: A/B test designer with IF/THEN/BECAUSE hypothesis framework, statistical significance calculator, sample size tables, and platform-specific guides for Meta, Google, LinkedIn, and TikTok.
* **/ads report**: Professional PDF report generator with health score gauge chart, platform comparison bars, pass/fail distribution donut, formatted tables, and a content quality guardrail that validates the report before output.
## Why This Is Better Than a Human Audit
I'm not saying humans are useless in advertising. Strategy, creative direction, understanding your customer, that still requires a brain. But the audit part? The part where someone checks 250+ things and reports back? **That's a checklist, and machines are better at checklists than humans.**
Here's the comparison:
* **Agency audit:** 2-4 weeks turnaround, 15-20 checks (realistically), $5-10K, biased toward upselling their own services
* **claude-ads audit:** 3-5 minutes, 250+ checks, $0, no conflict of interest
The agency doesn't want to tell you that your campaigns are actually fine and you should cut their retainer. claude-ads has no retainer. It just tells you what's broken and how to fix it.
## The Architecture
Three layers: directive (orchestrator with quality gates), orchestration (19 sub-skills routing to the right analysis), and execution (10 agents, 25 reference files, 12 industry templates). Everything loads on-demand. No bloat.
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
3-layer architecture: directive, orchestration, execution
## The 42K View Video
The demo video crossed 42,000 views, which tells me this struck a nerve. People are tired of paying for audits that take weeks and miss obvious issues. The most common comment? "I just found $3K/month in wasted spend in my first run." That's not surprising. **Most ad accounts have never had a proper 250+ point audit.** They've had a person skim through the account for an hour and write up whatever jumped out.
## How to Run It
Two options:
**Plugin install (recommended):**
```
/plugin marketplace add AgriciDaniel/claude-ads
/plugin install claude-ads@agricidaniel-claude-ads
```
**One-liner:**
```
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-ads/main/install.sh | bash
```
Then run `/ads audit` for the full multi-platform analysis, or `/ads google`, `/ads meta`, etc. for single-platform deep dives. The tool works with data you provide: exports, screenshots, or pasted metrics. For live API access, pair it with MCP servers (Google Ads MCP, Adspirer for Meta, GrowthSpree for LinkedIn).
The tool is MIT licensed. No usage limits, no premium tier, no "contact sales for enterprise." All analysis happens locally. No ad account data leaves your machine.
## What This Means for the Industry
Look, I'm not trying to put media buyers out of business. The good ones, the ones who actually develop strategy, test creative angles, and understand unit economics, will thrive. But the ones whose entire value prop is "I log into your ad account and tell you what I see"? **That job is automated now.**
The smart agencies will use tools like this themselves to 10x their audit speed and focus on what actually requires human judgment. The rest will keep charging $10K/month for screenshots.
* Try it yourself - [claude-ads on GitHub](https://github.com/AgriciDaniel/claude-ads) (2,400+ stars)
* Read the [full v1.5 release breakdown](/blog/claude-ads-v1-5-release) with platform research findings
* See how claude-ads fits into [the full AI marketing automation stack](/blog/ai-marketing-automation-stack)
* Read how I built the [SEO equivalent](/blog/claude-code-seo-stack) that replaced my entire SEO tool stack
* Learn more [about me](/about) and why I'm open-sourcing these tools
## Related Posts
* [claude-ads v1.5: 250+ Ad Audit Checks Across 7 Platforms](/blog/claude-ads-v1-5-release) - The full v1.5 release with platform research findings and 3 new skills
* [Claude Code Just Replaced Your Entire SEO Stack](/blog/claude-code-seo-stack) - How I replaced $300/month in SEO tools with one terminal command
* [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack) - The full open-source AI marketing stack at $50/month
* [Best Claude Code Skills in 2026](/blog/best-claude-code-skills-2026) - The definitive guide to top Claude Code skills ranked by GitHub stars
Join 4,500+ AI Marketing Builders
Get workflow templates, automation blueprints, and connect with SEOs, agency owners, and creators who ship.
[JOIN FREE →](https://www.skool.com/ai-marketing-hub)
