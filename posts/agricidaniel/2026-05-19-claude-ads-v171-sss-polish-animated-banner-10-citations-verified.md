# claude-ads v1.7.1: SSS+ Polish, Animated Banner, 10 Citations Verified

**Date:** 2026-05-19 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-ads-v1-7-1-release

---

## What Shipped in claude-ads v1.7.1
claude-ads v1.7.1 went out on May 18, 2026. claude-ads is an open-source ad audit tool that runs inside Claude Code and covers Google Ads, Meta Ads, Amazon Ads, YouTube, LinkedIn, TikTok, Microsoft Ads, and Apple Search Ads. v1.7.1 is a polish release. No new checks, no new skills, no new platforms. The job was to elevate the skill to SSS+ tier across README, branding, banner, dual-repo positioning, and citation discipline. Eight platforms, 22 sub-skills, 209 weighted checks, 41 tests still passing. That part did not move. What moved is everything around it.
v1.7.0 → v1.7.1 delta: documentation polish, zero behavior change.
Here is what landed:
* **Animated SVG banner:** 13.9 KB optimized file, 22 SMIL animations, `role="img"` and descriptive markup for screen readers
* **Branding kit:** parameterized template at `branding/banner-template.html` plus an `AGENT-PROMPT.md` so the terminal-style design can be replicated across sibling projects
* **README overhaul:** personas, JSON sample outputs, comparison matrices, expandable FAQ, dual-repo documentation
* **Citation pass:** 10 quantified claims across six ad-platform modules verified against primary vendor documentation
* **Project info section:** CHANGELOG, CONTRIBUTING, CODE OF CONDUCT, SECURITY, SUPPORT links surfaced from the README
* **Dual-remote canonical move:** origin shifted to `AI-Marketing-Hub/claude-ads`, this repo is now the open-source mirror
* **Style cleanup:** 54 em dashes removed across docs, platform-features table updated with concrete feature names and dates, script permissions normalized to 755
Key Takeaways
* v1.7.1 is documentation, branding, and trust signal. Zero functional changes.
* 10 quantified claims across six ad-platform modules now cite primary vendor docs.
* Animated SVG banner is 13.9 KB with 22 SMIL animations and screen-reader markup.
* 54 em dashes removed. Style guide is now machine-enforced across the README.
* Canonical remote is now AI-Marketing-Hub/claude-ads. The AgriciDaniel mirror stays in sync.
## Why Polish, Not Features
Polish, not features. v1.7.1 ships zero new functionality, every change is a trust signal.
v1.7.0 was a heavy lift. Eight platforms, 22 sub-skills, 209 checks, 41 tests, six AI assistant hosts, full Amazon coverage including Sponsored Products, Brands, and Display. The launch demo on YouTube walks through all of it.
Once features ship, the next bottleneck is trust. Most paid-ad tooling is a black box. You install it, get a number back, and you have to take it on faith. I want the opposite. Every check should be inspectable. Every benchmark should cite a vendor source. The README should answer the questions agencies actually ask before they hand a tool a client account.
That was the v1.7.1 brief. Lock down the citation discipline, ship a banner that looks like the rest of the family, and rewrite the README so the comparison matrices, personas, and sample outputs land in the first scroll.
## The Animated Banner
The new banner is the visual centerpiece. 13.9 KB. 22 SMIL animations. Terminal-style framing that matches claude-seo, claude-blog, and claude-canvas. The brand kit at `~/Documents/Obsidian Vault/concepts/brand-design-system.md` calls for OS-window chrome, JetBrains Mono labels, brand orange `#D97757` for focal elements, and a 4.2-second breathing gradient. v1.7.0 had a static PNG. v1.7.1 has the animated SVG with proper accessibility markup.
The parameterized template ships in `branding/banner-template.html`. Pair it with `AGENT-PROMPT.md` and you can regenerate the same banner for any sibling repo with one prompt and a JSON parameter file. That is the point: the design system is now cloneable, not bespoke.
Platform coverage: Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon. 209 checks total.
## The Citation Pass
Ten quantified claims, ten primary-vendor sources. Every benchmark in v1.7.1 traces to a publisher, title, URL, and retrieval date.
Ten quantified claims got the receipts treatment. The job was simple. Every number in a check description, every threshold, every benchmark, every "+18% queries" or "56 billion retail media" had to trace back to a primary vendor source. Not a blog post citing a blog post. The vendor doc itself, with a retrieval date, in the reference file.
Six modules touched: ads-google, ads-meta, ads-apple, ads-microsoft, ads-budget, ads-creative. The vendor sources cited include Meta Engineering, Apple Developer session 221, Google Ads blog, Microsoft Advertising blog, and AppTweak. The audit lifecycle is the same as before. What changed is that when a check fires and says "Meta bundles near-duplicates at the auction layer before scale," the underlying threshold is now tied to a Meta-published doc, not a guess.
This is the FLOW evidence triple in practice: year anchor in the prose, inline citation with publisher and title, URL with retrieval date. The full framework lives at [github.com/AgriciDaniel/flow](https://github.com/AgriciDaniel/flow). Applied to ad audits, it means clients can ask "where did this number come from" and get a real answer. Sample vendor sources cited in the v1.7.1 sweep include [Meta Engineering](https://engineering.fb.com/), [Apple Developer WWDC25 sessions](https://developer.apple.com/videos/play/wwdc2025/), the [Google Ads blog](https://blog.google/products/ads-commerce/), and the [Microsoft Advertising blog](https://about.ads.microsoft.com/en/blog).
Citation pass results: 10 primary sources, 41 tests green, 0 functional drift.
## Demo Walkthrough
The v1.7 walkthrough video is the fastest way to see the product. The flow:
* **Three big shifts framed up front:** Amazon retail media hit $56 billion, Meta rewired creative ranking through Andromeda, Google is moving accounts to AI Max. Most tools miss all three. claude-ads covers them.
* **22 sub-skills, one orchestrator:** say "audit my Meta account" and the Meta sub-skill loads. Say "plan a sales campaign" and the planning sub-skill loads. The router handles dispatch.
* **One script, six hosts:** Claude Code, Codex CLI, Cursor, Windsurf, Gemini CLI, Goose. Same skills, any host.
* **41 tests enforcing 209 checks:** run the same audit twice, get the same grade. That is the trust signal most competitors miss.
* **Pre-flight AI Max audit:** Google is flipping search accounts to AI Max. Legacy campaigns get caught before the flip, not after.
* **Andromeda creative-similarity:** Meta throttles near-duplicates before scale. The audit scores it pre-launch on visual, headline, body, and hook format.
* **Amazon in one pass:** Sponsored Products, Sponsored Brands, Sponsored Display, all covered in a single audit run.
The architecture itself stayed put. claude-ads still ships 22 sub-skills across 8 ad-platform hosts (Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon), with one orchestrator wiring them together. v1.7.1 polished the documentation and design system around that surface area. It did not change the surface area.
22 sub-skills across 8 ad-platform hosts, one orchestrator. The shape of the product in v1.7.1.
## Who This Helps
Three audiences benefit directly from v1.7.1:
* **Agencies handing audits to clients:** the citation pass means every benchmark in the PDF deliverable now traces to a vendor doc. Fewer "where did this number come from" emails.
* **Solo consultants pitching new accounts:** the README overhaul is the new sales page. Personas, sample outputs, comparison matrices, FAQ. Send the GitHub link, prospect reads it themselves.
* **Builders forking the skill:** the branding kit means anyone forking claude-ads for a private agency variant can regenerate the banner with one prompt. The design system is no longer locked to my desktop.
## Install
Same install commands as v1.7.0. Pick one:
```
# Claude Code plugin
/plugin marketplace add AI-Marketing-Hub/claude-ads
# Unix one-liner
curl -fsSL https://raw.githubusercontent.com/AI-Marketing-Hub/claude-ads/main/install.sh | bash
# Windows one-liner
irm https://raw.githubusercontent.com/AI-Marketing-Hub/claude-ads/main/install.ps1 | iex
```
The skill works across Claude Code, Codex CLI, Cursor, Windsurf, Gemini CLI, and Goose. Same sub-skills everywhere.
## What's Next
v1.7.1 closes the v1.7 cycle. Next on the queue:
* **Wave three platform coverage:** Walmart Connect and Connected TV. Walmart is the second-largest US retail media network. CTV is where the budgets are moving.
* **v2 measurement stack:** Marketing Mix Modeling, incrementality testing, PMax feed health auditing. The check catalog stays. What gets added is the layer above it that ties checks to revenue impact.
* **More citation passes:** the v1.7.1 sweep hit 10 claims. There are more. Every release going forward gets a citation pass before the tag lands.
## FAQ
### Is v1.7.1 a breaking change?
No. Zero functional changes. Same 22 sub-skills, same 209 checks, same 41 tests, same scoring math. If v1.7.0 worked for you, v1.7.1 works identically. The release is documentation, branding, and citation discipline.
### What is the dual-repo thing?
Canonical origin moved to `AI-Marketing-Hub/claude-ads`. This is the org I use to distribute Pro-tier work to the Skool community. The `AgriciDaniel/claude-ads` repo stays alive as the open-source mirror. Both repos point at the same code. Install instructions reference AI-Marketing-Hub because that is where releases ship first.
### Where do the 10 verified citations show up?
Inline in the check descriptions across six ad-platform modules: Google, Meta, Amazon, TikTok, LinkedIn, Microsoft. Every quantified claim now has a publisher, a title, a URL, and a retrieval date. The full reference list lives in the skill's `references/` directory.
### How big is the animated banner?
13.9 KB. 22 SMIL animations. Total file size is under the 100 KB image budget that the brand design system enforces. The banner uses `role="img"` and descriptive elements for screen-reader compatibility.
### Can I use the branding kit for my own project?
Yes. `branding/banner-template.html` is parameterized. Pair it with `branding/AGENT-PROMPT.md` and you can regenerate a matching banner for any sibling repo. The kit is MIT licensed alongside the rest of the skill.
### Is the tool still free?
Yes. MIT license, no usage limits, no premium tier. You need a Claude Code subscription because the skill runs inside Claude Code, but the skill itself is free and open source. There is no hosted version.
## Related Posts
* [claude-ads v1.5: 250+ Ad Audit Checks Across 7 Platforms](/blog/claude-ads-v1-5-release) - The v1.5 release with the first PDF report generator
* [Claude Code Just Replaced Your Ad Agency](/blog/claude-code-ad-agency) - The original product post covering positioning and scope
* [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack) - Where claude-ads fits in the full stack
* [claude-seo v1.9.6: FLOW Framework Security Hardening](/blog/claude-seo-v196-flow-security-hardening) - The FLOW evidence-citation framework that drove the v1.7.1 citation pass
* [Best Claude Code Skills 2026](/blog/best-claude-code-skills-2026) - How claude-ads compares to the rest of the Claude Code skill ecosystem
Read the full [v1.7.1 release notes on GitHub](https://github.com/AgriciDaniel/claude-ads/releases/tag/v1.7.1), star the repo if it helps you, and open an issue if anything breaks. Learn more [about me](/about) and the rest of the open-source AI marketing stack I build.
Join 4,500+ AI Marketing Builders
Workflow templates, audit playbooks, and a community of SEOs, agency owners, and PPC consultants who ship.
[JOIN FREE](https://www.skool.com/ai-marketing-hub)[GO PRO](https://www.skool.com/ai-marketing-hub-pro)
