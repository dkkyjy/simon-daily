# I Just Shipped the Biggest Claude SEO Update Yet

**Date:** 2026-03-31 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-seo-172-firecrawl-backlink-analysis

---

## 3,500 Stars and Counting
A month ago I released [claude-seo](https://github.com/AgriciDaniel/claude-seo) and it hit 3,500 GitHub stars faster than anything I've built. 560 forks. Issues and PRs I reviewed every single one of. People were actually using it - running audits on their sites, filing bugs when something broke, suggesting features I hadn't thought of.
Since then I've been heads-down shipping. Not marketing, not writing threads, not doing launch posts. Just building. Today **v1.7.2 is live** and the project has completely transformed from what I originally released. What started as a [$300/month SEO tool replacement](/blog/claude-code-seo-stack) is now something bigger - an extensible platform that connects to live data sources and generates reports you can actually hand to clients.
Let me walk you through what changed and why.
## From 12 Skills to 19 Sub-Skills
The v1.0 I launched had 12 skills and 9 parallel agents. It could audit your site's technical SEO, check your schema, analyze content quality, and give you a ranked list of fixes. That was genuinely useful - people were replacing paid tools with it.
But the feedback was consistent: "Great audit, but I need live data." The tool was analyzing static HTML, not querying real APIs. It couldn't tell you your actual Core Web Vitals from the field, your real Search Console impressions, or your live backlink profile. It was doing what a developer could do by reading source code - just faster.
v1.7.2 fixes that. The project now has **19 sub-skills** (16 core + 3 extensions), **12 parallel subagents**, and **3 extension modules** that connect to live data. Here's what grew and why.
## Google API Integration - Real Data, Not Guesswork
This was the turning point. I wired [9 Google APIs](/blog/google-api-seo-automation-claude-code) directly into claude-seo: PageSpeed Insights, Chrome UX Report (CrUX), Search Console, Google Analytics 4, YouTube Data API, Cloud Natural Language API, the Indexing API, Google Trends, and Custom Search. All at **$0.0006 per query** on Google's free tiers.
The credential system has 4 tiers so you can start free and scale up:
1. **API Key only** - PageSpeed, CrUX, YouTube, NLP, Trends, Custom Search. No OAuth needed. Just paste a key.
2. **OAuth (read-only)** - Adds Search Console performance data and GA4 reporting.
3. **OAuth (write)** - Adds the Indexing API for submitting URLs directly to Google.
4. **Service Account** - For automated pipelines and CI/CD integration.
The part agency owners care about most: **PDF and Excel reports**. Run an audit, pipe the Search Console data through the report generator, and get a styled document with summary metrics, per-page performance, query rankings, and indexation status. The Excel version has navy headers, auto-width columns, frozen rows, and filters. Hand it to a client and it looks like you spent an hour in Google Sheets.
## DataForSEO Extension - Live SERP Data and Keyword Research
Google's APIs give you your own data. [DataForSEO](https://dataforseo.com/) gives you everyone else's. The DataForSEO extension adds **22 commands** to claude-seo through an MCP server integration:
* **Live SERP analysis** - Pull the actual top 10 results for any keyword, with titles, descriptions, featured snippets, and People Also Ask boxes
* **Keyword research** - Search volume, keyword difficulty, CPC, competition level, and search intent classification for any term
* **Backlink profiles** - Referring domains, anchor text distribution, new/lost links, and domain authority metrics
* **On-page analysis** - Content parsing, readability scoring, and Lighthouse data from their infrastructure
* **Content analysis** - Sentiment, entities, and topic extraction at scale
The extension pattern I built for this is something I'm proud of. One install script, one MCP server config, done. No manual JSON editing, no path debugging. Run `./extensions/dataforseo/install.sh`, enter your API credentials, and the next time you run `/seo` the extension is automatically available. I used the same pattern for Firecrawl and Banana (AI image generation).
## Firecrawl Extension - The Most Requested Feature
"Can it crawl my whole site?" was the question I got more than any other. The honest answer was: not really. The technical audit agent parsed your sitemap and checked individual URLs, but if your site was built with React, Next.js, Vue, or any SPA framework, the crawler saw empty `<div id="root"></div>` and nothing else.
[Firecrawl](https://www.firecrawl.dev/) changes that completely. It's a crawling service with full JavaScript execution, and the claude-seo integration exposes four commands:
* **`/seo firecrawl crawl <url>`** - Full-site crawl with JS rendering. Every page gets executed in a real browser before content extraction.
* **`/seo firecrawl map <url>`** - Fast URL discovery across the entire site. Credit-efficient for sitemap audits.
* **`/seo firecrawl scrape <url>`** - Single-page deep scrape with the fully-rendered DOM.
* **`/seo firecrawl search <query> <url>`** - Search within a site's crawled content.
The integration is deeper than just standalone commands. When Firecrawl is installed, the audit workflow upgrades automatically - URL discovery switches from sitemap-only to `map`, and broken link detection uses `crawl` for JavaScript-rendered pages. Free tier: **500 credits/month** (1 credit per page).
## Backlink Analysis
The new `/seo backlinks <url>` command runs a **7-section analysis**:
1. **Profile Overview** - Total backlinks, referring domains, authority trend
2. **Anchor Text Distribution** - Over-optimization detection (flags when >70% are exact-match)
3. **Referring Domain Quality** - Authority, relevance, and geographic breakdown
4. **Toxic Link Detection** - **30 toxicity patterns** including PBN footprints, link farms, and unnatural link velocity. Auto-generates disavow recommendations.
5. **Top Pages by Backlinks** - Your most-linked pages and their sources
6. **Competitor Gap** - `/seo backlinks gap <you> <competitor>` finds who links to them but not you
7. **New/Lost Tracking** - Recent link acquisitions and losses with context
Is it Ahrefs? No. Ahrefs has a massive proprietary backlink index built over a decade. But for most small-to-mid sites, this gives you the actionable data - toxic links to disavow, competitor gaps to target, anchor distribution to fix - without the $99/month fee.
## Watch the Full Walkthrough
I recorded a complete demo showing the setup, the audit workflow, Google API reports, and the extension system in action:
## Anthropic Compliance and Marketplace
Something I'm genuinely proud of: claude-seo **passed Anthropic's official plugin validation**. Not a self-assessment - the actual compliance checks for quality, security, and best practices. The plugin has been submitted to the Anthropic marketplace and is listed on the [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) repository (49K+ stars).
This matters for trust. When someone installs a Claude Code skill, they're giving it access to their terminal and files. Being validated by Anthropic means the code has been reviewed and meets their standards for safety and functionality. It's also how new users discover the tool - the marketplace is where most first-time installations come from now.
## The Community
**3,500+ stars. 560 forks.** I've reviewed every single pull request and responded to every issue. Some of the best features came from community feedback - the Excel export was requested by agency owners in the [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) community. The Firecrawl integration happened because a dozen people independently asked for SPA crawling support.
The project also has a companion tool now: [AI Marketing Claude](https://github.com/zubair-trabzada/ai-marketing-claude) by Zubair Trabzada, which handles the post-audit marketing actions. That's the kind of ecosystem growth I was hoping for - other builders extending the platform for their own use cases.
If you're using claude-seo and building something on top of it, I want to hear about it. Drop a message in the [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) (free, 4,500+ members) or open a discussion on GitHub.
## What's Next
v1.8 is already in progress. Three things on the roadmap:
* **Content strategy skill** - Topic cluster planning, content gap analysis, and editorial calendar generation based on your existing content and keyword data
* **Deeper Firecrawl integration** - Scheduled crawls, change detection, and visual regression testing
* **Automated monitoring** - Cron-based audits with diff reports and alerting when critical metrics drop
The goal is to make claude-seo not just an audit tool but a monitoring system that catches regressions before they cost you rankings. If you want to shape what gets built, the roadmap discussions happen in the community.
## Try It
Install in one command:
```
curl -sL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/v1.7.2/install.sh | bash
```
Windows:
```
irm https://raw.githubusercontent.com/AgriciDaniel/claude-seo/v1.7.2/install.ps1 | iex
```
* **Star the repo** - [github.com/AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
* **Read the docs** - [claude-seo.md](https://claude-seo.md)
* **Join the community** - [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) (free) or [Pro](https://www.skool.com/ai-marketing-hub-pro) ($88/mo)
* **Check out Rankenstein** - [rankenstein.pro](https://rankenstein.pro) for the full AI content engine
19 sub-skills. 12 subagents. 3 extensions. MIT licensed. Free forever. Go break something.
## Frequently Asked Questions
### Q: How do I upgrade from an older version?
Run the same install command - it overwrites the existing skill files with the latest version. Your extension configurations (DataForSEO API keys, Firecrawl tokens) are preserved in separate config files that the installer doesn't touch. No migration needed.
### Q: Do I need all three extensions?
No. The core 16 sub-skills work without any extensions. DataForSEO adds live SERP and keyword data. Firecrawl adds JavaScript-rendered crawling. Banana adds AI image generation for reports. Install only what you need - each extension is independent.
### Q: Is claude-seo really free?
The tool itself is MIT licensed and always free. The extensions connect to third-party APIs that have their own pricing: Google APIs have generous free tiers ($0.0006/query), DataForSEO starts at $50/month, and Firecrawl has a free tier of 500 credits/month. You can use the full core tool without spending anything.
### Q: What's the difference between DataForSEO and Firecrawl?
DataForSEO provides market data - what other sites rank for, keyword volumes, backlink profiles, SERP features. Firecrawl provides crawling infrastructure - it visits your site's pages with a real browser and extracts content. DataForSEO tells you about the market. Firecrawl tells you about your site. They complement each other.
### Q: Can I use claude-seo for client work?
Yes. MIT license means you can use it commercially, modify it, and redistribute it. The Excel and PDF reports are designed specifically for client delivery. Many agency owners in the community use it as their primary audit tool and white-label the reports.
## Related Posts
* [Claude Code Just Replaced Your Entire SEO Stack](/blog/claude-code-seo-stack) - The original deep dive on how claude-seo works
* [Free Google API SEO Automation With Claude Code](/blog/google-api-seo-automation-claude-code) - Detailed walkthrough of the 9 Google API integrations
* [Free SEO Audit Tools That Actually Work](/blog/free-seo-audit-tools) - Where claude-seo fits in the broader landscape of free tools
* [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack) - The full toolkit including claude-seo, claude-blog, and Rankenstein
Join 4,500+ AI Marketing Builders
Get workflow templates, automation blueprints, and connect with SEOs, agency owners, and creators who ship.
[JOIN FREE →](https://www.skool.com/ai-marketing-hub)
