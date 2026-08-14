# Two Claude SEO Releases in One Day: FLOW Framework Plus Security Hardening

**Date:** 2026-04-26 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-seo-v196-flow-security-hardening

---

## Two Releases. One Day. Six Hours of Work.
I shipped Claude SEO v1.9.5 this morning and v1.9.6 this afternoon. Same day. Both tagged, both pushed, both with full release notes. v1.9.5 added the FLOW SEO framework as the 21st sub-skill in the tool. v1.9.6 ran a security audit over the new code and closed every finding before the day was over.
This post is the long-form story of why I split the work into two releases instead of one, what FLOW actually is, and how the security pass closed 10 findings (1 HIGH, 4 MEDIUM, 5 LOW, plus 1 INFO) using Subagent-Driven Development with two-stage review per task.
## Why v1.9.6 Followed v1.9.5 the Same Day
Two releases shipped April 26, 2026. [v1.9.5](https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.5) integrated the FLOW SEO framework as the 21st core sub-skill in Claude SEO. [v1.9.6](https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.6) ran a security audit over the new attack surface and fixed every finding before the day was over.
Functional code in v1.9.5. Hardened code in v1.9.6. Same FLOW capability, with the integration locked down to A grade. New installs should pin to v1.9.6.
The split was deliberate. v1.9.5 introduced new code paths: a GitHub API sync script, a new agent with WebFetch access, 41 bundled prompt files, cross-skill references. Each of those is an attack surface. Shipping the audit pass as a separate tag makes the security work auditable on its own, with its own test suite and its own release notes. **10 findings closed, 0 outstanding, 5 to 15 tests, B (88) to A (95+).**
## What FLOW Adds to Claude SEO
**FLOW is an evidence-led SEO methodology with 41 prompts across 5 stages.** Find. Leverage. Optimize. Win. Plus a Local-SEO branch. The framework is mine, originally published at [github.com/AgriciDaniel/flow](https://github.com/AgriciDaniel/flow) under CC BY 4.0. v1.9.5 brings it inside Claude SEO so any user can run stage-specific analysis on a target URL with one command.
The stages map to how SEO actually works in practice. Find is research: keyword markets, topical relevance, the surface area of what could rank. Leverage is amplification: E-E-A-T signals, authority moves, the things that compound. Optimize is implementation: on-page, off-page, technical, content. Win is the loop: rank tracking, performance review, the discipline of iteration. Local handles GBP, NAP consistency, citations, and map pack strategy as a first-class branch.
| Metric | v1.9.0 | v1.9.6 |
| --- | --- | --- |
| Core sub-skills | 20 | 21 |
| Subagents | 15 | 18 |
| Tracked scripts | 30 | 30 |
| Tests | existing | +15 sync\_flow.py |
| FLOW prompts bundled | 0 | 41 |
Eight commands ship with the skill: `find`, `leverage`, `optimize`, `win`, `local`, `prompts` (lists all available), `sync` (pulls latest from upstream), and `sync --ref <sha>` (pins to a specific upstream commit for reproducibility).
## How the Skill Picks 2 to 3 Prompts From 21
**The Optimize stage has 21 prompts. The agent never loads all of them.** It reads the prompt file names first, fetches the target URL, then selects 2 or 3 prompts that match the page's industry signals, content gaps, or technical issues. Context-matched, not a dump.
This is the difference between a prompt library and a prompt framework. A library gives you 21 things you could try. A framework gives you the 2 or 3 you should try, given what your page actually looks like. The seo-flow agent is the discrimination layer. It reads the page once, scans the available prompts, and applies the relevant ones with evidence requirements baked into each output.
The other four stages are bounded. Find has 5 prompts. Leverage has 1. Win has 3. Local has 11. Optimize is the one with 21 because that is where most SEO implementation work lives, and where context-matching matters most.
```
/seo flow optimize https://example.com/pricing
```
Output includes the stage label, the prompt files applied with one-line rationale for each pick, evidence-tagged findings per prompt, and what data would validate or strengthen each finding. Attribution to the FLOW framework appears on every response, by rule.
## 10 Findings Fixed in 6 Tasks
**The post-v1.9.5 cybersecurity audit returned 10 findings: 1 HIGH, 4 MEDIUM, 5 LOW, plus 1 INFO.** All closed in v1.9.6. No deferrals. The implementation went through Subagent-Driven Development with two-stage review per task: spec compliance first, then code quality.
The HIGH finding was the most surgical. `VULN-A01`: the seo-flow agent was granted Bash in its tool list. Bash plus WebFetch is a prompt-injection-to-shell pipeline. Fix: drop Bash from the tools line. The agent reads files, fetches URLs, and matches patterns. It never needed shell execution. The orchestrator-level `/seo flow sync` command still has Bash and runs the sync script normally. The agent does not.
The 4 MEDIUM findings cluster around the sync script. `VULN-A02` and `VULN-A07` both relate to the GitHub token strategy. The original code grabbed a full-scope PAT via `gh auth token` on every run and sent it in the Authorization header. That meant a redirect on the API path could leak the token to a third party. Fix: anonymous-first. The script sends no token by default, and only escalates to authenticated requests on a 403 fallback if `gh` is available.
`VULN-A03` was a path-traversal write. `record_write()` wrote any path it received without verifying the path was inside the skill directory. Fix: `Path.resolve()` containment check before any write. `VULN-A04` introduced a SHA-256 lockfile for prompt integrity (more on that below). `VULN-A05` tagged WebFetch responses as untrusted in the agent body, with explicit guidance not to execute, eval, or relay fetched content verbatim.
The 5 LOW findings closed gaps that were technically defense-in-depth but worth fixing now. `VULN-A06`: graceful degradation when `gh` CLI is missing instead of a hard sys.exit. `VULN-A08`: atomic writes via `tempfile.mkstemp` plus `shutil.move`, eliminating partial-write corruption on interrupt. `VULN-A09`: 5 MB response cap and 15-second timeout on every API call. `VULN-A10`: URL allowlist that validates HTTPS scheme and `api.github.com` host, blocking the `@evil.com` userinfo bypass form.
The single INFO finding (`INFO-A14`) added a CC BY 4.0 attribution header to `references/prompts/README.md`. Small, but the FLOW license requires attribution when reproducing or adapting the prompts.
## Anonymous-First Token Strategy Explained
**v1.9.6 sends zero credentials on the first GitHub API request.** The sync script makes anonymous calls. GitHub's unauthenticated rate limit is 60 requests per hour per IP, which is more than enough for syncing roughly 50 small prompt files. The token only enters the picture if a 403 comes back.
That changes the threat model. Before v1.9.6, every sync request carried a full-scope GitHub PAT. If the API ever 302-redirected to a host the script did not own, the token went along for the ride. After v1.9.6, the default headers contain only `Accept` and `X-GitHub-Api-Version`. No Authorization key. No leak surface.
```
def _base_headers():
    return {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
```
The 403-triggered escalation has its own guard. The retry only happens if the original request had no Authorization header AND the escalated headers actually contain a token. If `gh` CLI is absent, `_authed_headers()` falls back to base headers, the recursion check fails, and the script raises the original 403 instead of looping forever. That edge case caught a real infinite-loop bug during code review.
The practical effect: you can run `/seo flow sync` on a fresh machine with no `gh` CLI installed and it works. You can run it inside a CI container with no credentials and it works. You can run it locally with `gh auth login` done and it still works, with the token only sent if the rate limit kicks in.
## SHA-256 Lockfile for Prompt Integrity
**`flow-prompts.lock` is a sha256sum-compatible file pinning the SHA-256 of every synced FLOW prompt.** It lives at `skills/seo-flow/references/flow-prompts.lock` and is regenerated on every sync, with a drift report printed before any write.
The format is identical to `sha256sum` output: 64-char hex digest, two spaces, relative path. That means you can verify the lockfile's claims with one shell command:
```
cd skills/seo-flow/references
sha256sum --check flow-prompts.lock
```
The drift detection runs on every sync. It reads the existing lockfile, computes hashes for what is about to be written, and prints any ADDED, CHANGED, or REMOVED lines to stderr. If upstream changes a prompt, you see it before the file gets overwritten. That gives you a chance to review what changed and decide whether to commit the new lockfile.
This is the same pattern `package-lock.json` uses for npm and `Cargo.lock` uses for Rust. It does not stop tampering, but it surfaces it. Combined with the URL allowlist, the path containment check, the 5 MB cap, and the atomic write path, the integrity story for synced FLOW content is auditable end-to-end.
## How to Install or Upgrade
**One command. Same as every prior release.**
```
claude /install github:AgriciDaniel/claude-seo
```
If you are upgrading from v1.9.0 or earlier, the install command pulls v1.9.6 directly. The first run of `/seo flow sync` generates the lockfile and writes the 41 prompts to `skills/seo-flow/references/prompts/`. Existing skill configurations are untouched.
To try FLOW immediately on a target URL:
```
/seo flow find https://yourdomain.com
```
21 sub-skills. 18 agents. 30 scripts. MIT licensed for the skill code, CC BY 4.0 for the FLOW prompt content. Free forever. The optional DataForSEO and Firecrawl extensions still work the same way they did in [v1.9.0](https://claude-seo.md/blog/claude-seo-v190-community-release).
## What Comes Next
**v1.9.7 is already in scope.** Three things on the list: deeper FLOW cross-skill integration with seo-content (Leverage stage maps directly to E-E-A-T amplification), a per-stage CLI flag for `/seo flow sync` to pull only specific stages, and an optional offline mode that uses the bundled lockfile as the source of truth without hitting the network.
The [Google API integration](/blog/google-api-seo-automation-claude-code) story keeps evolving too. The plan is to surface FLOW Win-stage prompts directly inside the Search Console reporting flow, so rank tracking output triggers stage-appropriate next actions rather than just numbers.
If you build with Claude Code and want your work in the next release, the AI Marketing Hub Pro Skool community is where the next Pro Hub Challenge lives. The pattern from v1.9.0 worked: 6 contributors, 5 passing review, 4 new skills shipped. The same door is open for v1.10.0.
Full release notes for both tags: [v1.9.5 (FLOW integration)](https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.5) and [v1.9.6 (security hardening)](https://github.com/AgriciDaniel/claude-seo/releases/tag/v1.9.6). The findings table, the test list, and the migration steps are all there with line-level detail.
Join 4,500+ AI Marketing Builders
Get workflow templates, automation blueprints, and connect with SEOs, agency owners, and creators who ship.
[JOIN FREE →](https://www.skool.com/ai-marketing-hub)
