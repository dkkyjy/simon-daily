# skill-forge: Build Your Own Claude Code Skills From Scratch

**Date:** 2026-03-25 00:00 UTC
**Link:** https://agricidaniel.com/blog/skill-forge-build-claude-code-skills

---

Here's something that happens when you build a lot of Claude Code skills: you start noticing that 70% of the work is structural. The directory layout, the manifest files, the hook configurations, the README boilerplate - it's all the same across every skill. The actual logic is maybe 30% of the effort.
**skill-forge exists because I was copy-pasting folder structures between repos like it was 2003.** There had to be a better way. So I built one.
## What Is skill-forge?
skill-forge is a Claude Code skill that builds other Claude Code skills. Yes, it's recursive. Yes, I find that amusing.
More concretely, it's a guided workflow that takes you from "I have an idea for a skill" to "I have a working, publishable skill" in 5-15 minutes depending on complexity. It handles the scaffolding, the structure, the configuration, and the boilerplate. **You focus on the logic - the thing that actually matters.**
It runs as a slash command: `/skill-forge`. From there, it walks you through a structured design process, generates the skill files, and optionally publishes it to your GitHub.
## Why I Built It
After building claude-seo, claude-ads, and claude-blog - each one a fairly complex multi-file skill - I realized I was spending more time on scaffolding than on logic. Every skill needs:
* A specific directory structure Claude Code expects
* A manifest with the right schema
* Slash command definitions with proper argument parsing
* Hook configurations for lifecycle events
* A README that explains installation and usage
* Error handling patterns that work within Claude's execution model
The first time I built a skill, it took me 3 hours to get the structure right. The second time, 2 hours. By the fourth time, I automated it. **skill-forge is that automation, packaged so anyone can use it.**
There's a less obvious reason too: consistency. When you build skills by hand, every one ends up slightly different. Different directory naming, different manifest conventions, different error handling patterns. That inconsistency compounds when you're maintaining 21 repos. Bug fixes in one skill's error handling don't transfer to others because the patterns are all bespoke. skill-forge enforces a standard structure, which means maintenance across the entire portfolio becomes predictable.
## How It Works: The 5-Step Process
### Step 1: Design
skill-forge asks you what your skill should do, who it's for, and what commands it needs. It uses this to generate a design document - think of it as a blueprint. You review and refine before any code gets written. This step takes about 2 minutes and prevents the most common failure mode: starting to code before you've thought through the command interface.
### Step 2: Scaffold
Based on the design, skill-forge creates the entire file structure. Directory layout, manifest, command stubs, configuration files. Everything is in the right place with the right naming conventions. The scaffold includes placeholder comments that explain what each section does, so even if you're new to Claude Code skills, you can navigate the generated code without documentation.
skill-forge scaffolds the complete skill structure in seconds
### Step 3: Build
This is where you (and Claude) write the actual logic. skill-forge provides the skeleton; you fill in the muscle. It generates starter code for each command based on your design, so you're not starting from a blank file. For API integration skills, it also generates the HTTP client boilerplate with proper error handling, retry logic, and response parsing.
### Step 4: Review
skill-forge validates the skill structure, checks for common mistakes (missing manifest fields, incorrect hook syntax, orphaned files), and runs a dry-run test. It catches the errors that would otherwise bite you when you try to install the skill. I've seen people spend hours debugging a skill that won't load, only to find a missing comma in the manifest. The review step catches that in seconds.
### Step 5: Publish
Creates a Git repo (or adds to an existing one), writes a proper README with installation instructions, and optionally pushes to GitHub. Your skill is ready for other people to install and use. The generated README includes a badge section, feature list, command reference, and configuration docs - all populated from your design document. **No more writing documentation from scratch for every project.**
## The 4 Complexity Tiers
Not every skill is a 2,974-star monolith like claude-seo. skill-forge supports 4 tiers of complexity:
1. **Single-file skill** - One command, one file, simple logic. Think: a quick utility like a URL validator or a text formatter. Built in under 5 minutes. These are the skills you build when you think "I wish there was a slash command for this." Most developers have 10-20 of these personal utilities.
2. **Multi-command skill** - Multiple slash commands, shared utilities, some configuration. Think: a content tool with `/draft`, `/optimize`, and `/publish` commands. Built in 10-15 minutes. This is the tier where most practical skills live.
3. **Integration skill** - Connects to external APIs, handles auth, manages state. Think: claude-ads with Google Ads API integration. More involved, but skill-forge handles the API client scaffolding, token refresh flows, and rate limit handling. The generated code includes retry logic with exponential backoff - the kind of thing you always mean to implement but never get around to.
4. **Multi-skill orchestration** - A skill that coordinates other skills. Think: a project manager skill that triggers claude-seo, claude-blog, and claude-ads in sequence. **This is the tier where skill-forge saves the most time** because the inter-skill communication patterns are tricky to get right manually. Getting the data flow between skills correct, handling failures gracefully, and maintaining state across skill boundaries requires careful architecture that skill-forge provides as a template.
## Example: Building an Audit Skill in 5 Minutes
Let me show you how fast this is. Say you want a skill that audits a website's meta tags.
You run `/skill-forge` and answer the prompts:
* **Name:** meta-audit
* **Description:** Audits meta tags across a website
* **Commands:** /meta-audit (takes a URL, checks title, description, OG tags, canonical)
* **Tier:** Single-file
* **External APIs:** None (uses fetch)
skill-forge generates the entire skill. The directory, the manifest, the command with argument parsing, the fetch logic, the output formatting. **You review the generated code, tweak the validation rules to your liking, and you have a working skill.**
Install it with the standard Claude Code skill install flow, and `/meta-audit https://example.com` works immediately.
Here's what the generated skill actually checks out of the box: title tag presence and length (50-60 chars), meta description presence and length (150-160 chars), Open Graph tags (og:title, og:description, og:image, og:url), Twitter Card tags, canonical URL, robots directives, and viewport meta tag. That's a solid foundation. You can add custom checks (like hreflang validation or structured data presence) by editing the generated checker functions.
(The generated code is not perfect - it's a starting point. But it's a starting point that already handles edge cases, errors, and output formatting. That's the part that takes forever to write from scratch.)
## How My Other Skills Were Built
Every skill I've published since building skill-forge was scaffolded with it:
* **claude-blog** (300 stars) - Multi-command skill, Tier 2. skill-forge generated the `/blog` command structure, the content pipeline stages, and the CMS integration scaffolding. Total build time from scaffold to first working version: about 4 hours. Without skill-forge, based on my experience with claude-seo, it would have been 12+.
* **claude-ads** (1,171 stars) - Integration skill, Tier 3. skill-forge generated the Google Ads API client, the auth flow, and the campaign management commands. The OAuth2 flow alone would have taken a day to implement from scratch. skill-forge gave me a working auth flow in the scaffold.
* **banana-claude** (41 stars) - Integration skill, Tier 3. skill-forge generated the Gemini API integration and the Creative Director prompt architecture. The multi-step generation pipeline (intent analysis, style mapping, prompt engineering, quality check) was structured from the design phase, which saved a lot of architectural rework.
claude-seo predates skill-forge (it was the project that made me realize I needed it), but I've since migrated its structure to match skill-forge conventions. **Having a consistent structure across all 21 repos makes maintenance dramatically easier.** When I fix a bug in one skill's error handling pattern, I can apply the same fix across all skills mechanically.
## Try It
skill-forge is open source, MIT licensed, and sitting at 23 stars on GitHub (small but growing). If you're building Claude Code skills - or thinking about it - it'll save you hours of structural work.
Install it, run `/skill-forge`, and see how fast you can go from idea to working skill. If you build something cool with it, I genuinely want to see it - drop it in the AI Marketing Hub or tag me on GitHub.
The Claude Code skill ecosystem is still early (see my ranking of the [best Claude Code skills in 2026](/blog/best-claude-code-skills-2026) for the current landscape). The people building skills now are shaping what the platform looks like for everyone who comes after. skill-forge is my attempt to lower the barrier to entry so more people build more things. **The best time to start building skills was 6 months ago. The second best time is today, and now you have a tool that makes it 5x faster.**
## Related Posts
* [Best Claude Code Skills in 2026](/blog/best-claude-code-skills-2026) - The definitive guide to top Claude Code skills ranked by GitHub stars
* [Claude Code Just Replaced Your Entire SEO Stack](/blog/claude-code-seo-stack) - How I replaced $300/month in SEO tools with one terminal command
* [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack) - The full open-source AI marketing stack at $50/month
Join 4,500+ AI Marketing Builders
Get workflow templates, automation blueprints, and connect with SEOs, agency owners, and creators who ship.
[JOIN FREE →](https://www.skool.com/ai-marketing-hub)
