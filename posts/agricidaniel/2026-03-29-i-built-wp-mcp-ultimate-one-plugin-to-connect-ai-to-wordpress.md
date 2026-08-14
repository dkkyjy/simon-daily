# I Built WP MCP Ultimate - One Plugin to Connect AI to WordPress

**Date:** 2026-03-29 00:00 UTC
**Link:** https://agricidaniel.com/blog/wp-mcp-ultimate-wordpress-ai-plugin

---

## Why I Built This
Connecting AI to WordPress should not require three plugins. But that's exactly what it took. You needed **MCP Adapter** to handle the protocol layer, **MCP Expose Abilities** to register WordPress actions as tools, and the **Abilities API** polyfill if your WordPress version was below 6.9. Three plugins from three different authors, three update cycles, three points of failure.
Every time WordPress updated, something broke. The adapter would lose its endpoint registration. The abilities plugin would conflict with the polyfill. Config snippets in the docs pointed to URLs that no longer existed. I spent more time debugging the plugin stack than actually using AI to manage my sites.
So I did what any frustrated developer does - I merged everything into one plugin. [WP MCP Ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate) is a self-contained MCP server that installs in one click and gives any MCP-compatible AI client full access to your WordPress site. No dependencies. No conflicts. No duct tape.
## What WP MCP Ultimate Does
One plugin. **58 WordPress abilities across 13 domains.** Every action goes through a 3-tool meta pattern: `discover-abilities` lists what's available, `get-ability-info` returns the schema for a specific ability, and `execute-ability` runs it. The AI client never needs to guess what's possible - it asks the plugin directly.
Here's the full breakdown:
| Domain | Abilities | What AI Can Do |
| --- | --- | --- |
| Posts | 6 | List, get, create, update, delete, patch content |
| Pages | 6 | Full CRUD + content patching |
| Taxonomy | 4 | Categories and tags - list and create |
| Search | 1 | Full-text content search |
| Revisions | 2 | List and inspect post revisions |
| Media | 5 | Upload, list, get, update, delete files |
| Users | 6 | Full user management with role assignment |
| Plugins | 6 | Upload, install, activate, deactivate, delete |
| Menus | 7 | Create menus, add items, assign locations |
| Widgets | 3 | List sidebars and available widgets |
| Comments | 6 | Moderate, reply, create, delete |
| Options | 3 | Get, update, list site options |
| System | 3 | Transients, debug log, toggle debug mode |
| Total | 58 |  |
The plugin is compliant with **MCP protocol version 2025-06-18** and uses **Streamable HTTP transport** - not the older SSE (Server-Sent Events) pattern. This matters because Streamable HTTP is bidirectional and doesn't require long-lived connections, which means it works reliably behind CDNs and load balancers that typically kill SSE connections after 30 seconds.
It also includes conflict detection. If you have the old MCP Adapter, MCP Expose Abilities, or Abilities API plugins still installed, the dashboard warns you and explains why you should deactivate them. And for sites running WordPress below 6.9, **WP MCP Ultimate bundles its own Abilities API polyfill** - no separate plugin needed.
## Setup in 2 Minutes
Three steps. No configuration files to hand-edit, no terminal commands, no API keys to hunt down.
1. **Install the plugin** - Download the zip from the [v1.1.0 release page](https://github.com/AgriciDaniel/wp-mcp-ultimate/releases/tag/v1.1.0) and upload it via Plugins > Add New > Upload Plugin in your WordPress admin. Activate it.
2. **Generate an API key** - Go to Tools > MCP Ultimate and click Generate. The plugin creates a WordPress Application Password automatically.
3. **Copy the config snippet** - The dashboard shows ready-to-paste config for Claude Code, Claude Desktop, and Cursor. Copy and paste into your AI client's settings.
For Claude Code, the config goes into `~/.claude/settings.json`:
```
{
  "mcpServers": {
    "wordpress": {
      "type": "streamable-http",
      "url": "https://your-site.com/wp-json/mcp/wp-mcp-ultimate",
      "headers": {
        "Authorization": "Basic BASE64_CREDENTIALS"
      }
    }
  }
}
```
The dashboard generates the Base64 credentials for you. No manual encoding required. Once connected, your AI client can discover all 58 abilities automatically through the meta-tool pattern.
## What v1.1.0 Fixed
The initial release had three bugs that made the first-run experience rough. All fixed in v1.1.0:
* **Media upload crash** - Uploading images through MCP failed because `media_handle_sideload()` was undefined. WordPress only loads that function in the admin context, and MCP requests come through the REST API. The fix loads the required admin includes before any media operation.
* **Wrong endpoint URL** - All config snippets (in the dashboard, README, and setup guide) were pointing to `/sse` with SSE transport type. The correct endpoint is `/wp-json/mcp/wp-mcp-ultimate` with Streamable HTTP transport. Every snippet has been corrected.
* **Wrong config path** - The Claude Code config snippet showed `~/.claude.json` instead of the correct `~/.claude/settings.json`. Small typo, big headache for anyone following the docs.
The ability count was also corrected from 57 to 58 - a widget ability was missing from the registry. See the full [v1.1.0 release notes](https://github.com/AgriciDaniel/wp-mcp-ultimate/releases/tag/v1.1.0) for details.
## The Ecosystem - How the Tools Connect
WP MCP Ultimate doesn't exist in isolation. It's the bridge I was missing between my AI tools and live WordPress sites. Here's how the pieces fit together:
AI CONTENT PIPELINE
Claude Blog
writes content
Claude SEO
optimizes content
WP MCP Ultimate
pushes to site
WordPress
live site
Rankenstein
monitors performance
Content flows left to right. Data flows back through Rankenstein.
WP MCP Ultimate is the bridge between AI tools and your live site.
[Claude Blog](https://claude-blog.md) ([GitHub](https://github.com/AgriciDaniel/claude-blog)) writes SEO-optimized content with its [17-command, 100-point scoring system](/blog/claude-code-blog-writer). [Claude SEO](https://claude-seo.md) ([GitHub](https://github.com/AgriciDaniel/claude-seo)) runs a [full technical audit with 9 parallel agents](/blog/claude-code-seo-stack). But until now, the last mile was manual - I'd copy-paste the optimized content into WordPress by hand.
WP MCP Ultimate closes that gap. Claude Code can now write a blog post, optimize it for search, and publish it to WordPress - all in one session, without leaving the terminal. [Rankenstein](https://rankenstein.pro) then monitors how the published content performs in search, feeding data back into the next optimization cycle.
This is the [AI marketing automation stack](/blog/ai-marketing-automation-stack) I've been building toward. WP MCP Ultimate is the piece that makes it end-to-end.
## Security and What's Next
I'm going to be direct about this: **I ran a full security audit and identified 7 findings** that need to be addressed in v2.0. The current version relies on WordPress's built-in authentication (Application Passwords over Basic Auth with HTTPS), which is standard for REST API plugins. But there are improvements I want to make:
* **Nonce verification** for all state-changing operations (currently uses Application Password auth only)
* **Per-ability capability checks** are implemented but need granular review for edge cases
* **Session management** needs rate limiting and connection tracking
* **Input sanitization** follows WordPress coding standards but needs additional validation on complex inputs like media uploads and plugin installs
None of these are critical vulnerabilities - the plugin requires administrator credentials and HTTPS. But I want v2.0 to be hardened for production sites running at scale. If you find a security issue, please use the [GitHub Security Advisory](https://github.com/AgriciDaniel/wp-mcp-ultimate/security/advisories/new) to report it responsibly.
The roadmap for v2.0 also includes webhook support for real-time notifications, custom ability registration for theme developers, and multi-site network support.
## Watch the Full Demo
This 10-minute walkthrough covers the complete setup - from installing the plugin to managing posts, uploading media, and moderating comments through Claude Code:
## Get Started
WP MCP Ultimate is open source, GPL-2.0 licensed, and free. No premium tier. No feature gating. The full 58 abilities are available to everyone.
* **Install it** - [Download v1.1.0 from GitHub](https://github.com/AgriciDaniel/wp-mcp-ultimate/releases/tag/v1.1.0)
* **Star the repo** - [github.com/AgriciDaniel/wp-mcp-ultimate](https://github.com/AgriciDaniel/wp-mcp-ultimate)
* **Report bugs** - Open an issue on GitHub. PRs welcome.
* **Join the community** - [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) (free, 4,500+ members) or [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) ($88/mo) for workflow templates and direct support
If you're managing WordPress sites and using Claude Code, this plugin turns your terminal into a full WordPress admin panel. Try it on a staging site first, get comfortable with the abilities, then deploy to production. The setup takes 2 minutes. The time it saves you is permanent.
## Frequently Asked Questions
### Q: What is MCP (Model Context Protocol)?
MCP is an open protocol created by Anthropic that standardizes how AI applications connect to external tools and data sources. Think of it like USB for AI - a universal interface that lets any MCP-compatible client (Claude Code, Claude Desktop, Cursor) talk to any MCP server (WordPress, databases, APIs) using a shared language. WP MCP Ultimate turns your WordPress site into an MCP server.
### Q: Does WP MCP Ultimate work with ClassicPress?
Not currently. The plugin depends on WordPress's REST API infrastructure and Application Passwords system, which ClassicPress has diverged from. ClassicPress support is not on the roadmap, but the codebase is GPL-2.0 - anyone is welcome to fork and adapt it.
### Q: Is it safe for production sites?
The plugin requires administrator credentials over HTTPS and respects WordPress capability checks. For most single-site WordPress installations, this is equivalent to logging into wp-admin. That said, I recommend starting on a staging site to understand what each ability does before connecting a production site. The v2.0 release will add additional security hardening.
### Q: How much does it cost?
Nothing. Free forever. GPL-2.0 licensed. No premium tier, no feature restrictions, no usage limits. The plugin is fully open source on [GitHub](https://github.com/AgriciDaniel/wp-mcp-ultimate).
### Q: How is this different from using the WordPress REST API directly?
The WordPress REST API is a general-purpose HTTP API - your AI client would need to know the exact endpoints, authentication headers, request formats, and response structures for every operation. WP MCP Ultimate wraps all of that behind the MCP protocol, which AI clients already understand natively. The AI discovers available abilities automatically, gets typed schemas for each one, and executes them through a single standardized interface. It's the difference between giving someone a map and giving them GPS.
## Related Posts
* [Claude Code Just Replaced Your Entire SEO Stack](/blog/claude-code-seo-stack) - How claude-seo runs 9 parallel agents for a full site audit
* [Claude Code Just Replaced Your Blog Writer](/blog/claude-code-blog-writer) - claude-blog's 100-point scoring system for dual-optimized content
* [AI Marketing Automation: The Open-Source Stack I Use Daily](/blog/ai-marketing-automation-stack) - The full stack that WP MCP Ultimate now completes
* [Best Claude Code Skills in 2026](/blog/best-claude-code-skills-2026) - Where WP MCP Ultimate fits in the broader ecosystem
Join 4,500+ AI Marketing Builders
Get workflow templates, automation blueprints, and connect with SEOs, agency owners, and creators who ship.
[JOIN FREE →](https://www.skool.com/ai-marketing-hub)
