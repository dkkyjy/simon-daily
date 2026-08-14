# Claude Ads v2.0.1: The Paid-Ads Operating System for Claude

**Date:** 2026-07-14 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-ads-v2-0-1-release

---

## Claude Ads v2 Is Public
I rebuilt Claude Ads from the architecture up. v2.0.0 is the major release. v2.0.1 is the public distribution patch that makes the repository, installer, support, issue, discussion, and security-reporting paths work from the open public mirror.
The result is a paid-media operating system for Claude Code. It covers audits, planning, creative workflows, monitoring, experiments, reporting, and carefully gated change drafts across 12 advertising platforms.
The short version
* 12 first-class paid-advertising platform contracts
* 506 tests passed, with 23 skipped in the verification environment
* Repository audit passed across 339 tracked files
* Load-bearing platform claims mapped to dated evidence
* Read-only operation by default
* Versioned JSON as the system of record
## A Full Architecture Release
This is not another prompt pack with a larger command menu. Claude Ads v2 separates product contracts, evidence, capabilities, scoring, safety, and release controls into explicit layers.
One conductor owns the scope and final artifacts. Bounded workers analyze independent slices and return schema-valid findings. Required-worker failures make a run partial. They are never hidden behind a complete-audit label.
The canonical result is versioned JSON. Markdown, HTML, and optional PDF reports are rendered from that same validated bundle. That removes the drift that happens when every output format invents its own version of the truth.
## 12 First-Class Advertising Platforms
Claude Ads v2 gives each platform a dedicated contract, focused skill, audit worker, control reference, capability declaration, fixtures, and testable routing surface:
* Google Ads
* Meta Ads
* YouTube Ads
* LinkedIn Ads
* TikTok Ads
* Microsoft Advertising
* Apple Ads
* Amazon Ads
* Reddit Ads
* Pinterest Ads
* Snapchat Ads
* X Ads
Shared APIs do not collapse distinct platform results. YouTube remains its own audit surface even when Google Ads supplies the data. Failed platforms are reported as failed or missing, not quietly converted into zeroes.
## No Source, No Current Claim
Platform rules move too quickly for memory-based advice. v2 introduces public-safe source and claim ledgers for load-bearing platform, API, policy, regulation, benchmark, and creative-specification claims.
Each registered claim carries dated evidence, a retrieval date, confidence, and a refresh deadline. Stale evidence makes the dependent result provisional. Unsupported claims are demoted instead of being presented as current platform truth.
The same fail-closed approach applies to scoring. A catalog row is not automatically a health control. If a platform scoring profile is not approved, Claude Ads withholds the health score rather than inventing severity or category weights.
## Read-Only by Default
Claude Ads can turn authorized exports or account reads into observations, findings, plans, creative workflows, experiments, monitoring, and reports. It does not assume that permission to analyze is permission to change an account.
A live change requires an enabled capability for the exact operation, explicit account and object IDs, a human-readable before-and-after diff, owner approval, an idempotency key, an audit record, a verification window, and a rollback procedure.
Missing ceilings mean no write. Permanent deletion is outside v2. The default remains simple: inspect first, draft second, change only after every gate passes.
## 506 Tests Passed
On the tagged v2.0.1 release, the local suite completed with **506 tests passed** and 23 skipped in the current environment. The repository audit also passed across 339 tracked files.
The audit checks path portability, sensitive-content boundaries, and manifest consistency. The tests cover contracts, adapters, normalization, routing, scoring, reporting, release controls, installer safety, privacy, and URL defenses.
Those numbers are evidence for the tested repository behavior. They are not a claim that every optional live integration is enabled. The capability manifest remains the authority for what can read, draft, apply, verify, or roll back on each platform.
**Transparency note:** The v2.0.1 release notes also disclose five Pillow 12.2.0 advisories in optional creative and reporting paths. The dependency audit flags them openly while the evidence-complete dependency update is prepared.
## What v2.0.1 Changes
v2.0.1 does not change the v2 code contracts, scoring, catalog, or behavior. It updates the public release surface on top of v2.0.0.
* User-facing repository links now point to the public AgriciDaniel repository
* The default clone source now uses the public repository
* Support, issues, discussions, and private vulnerability reporting no longer require organization access
* The README documents the public and community distribution model
* Native Claude Code plugin installation is documented in the release
That distinction matters. v2.0.0 is the architecture release. v2.0.1 is the clean public doorway into it.
## Install or Update Claude Ads
The native Claude Code plugin flow is the recommended path:
```
/plugin marketplace add AgriciDaniel/claude-ads
/plugin install claude-ads@ai-marketing-hub-claude-ads
```
If Claude Ads is already installed, prompt Claude with:
Update Claude Ads to v2.0.1 from the public repository using the native plugin flow, then validate the installation and report the installed version.
Read the [public repository](https://github.com/AgriciDaniel/claude-ads), review the [v2.0.1 release notes](https://github.com/AgriciDaniel/claude-ads/releases/tag/v2.0.1), or [watch the build and launch video](https://www.youtube.com/watch?v=rz3dpN9wZB0&t).
## Frequently Asked Questions
### Is v2.0.1 the architecture release?
v2.0.0 is the full architecture release. v2.0.1 is a documentation and metadata patch that updates the public repository, installer, support, and release paths without changing the v2 behavior contracts.
### Which advertising platforms are supported?
Claude Ads v2 has first-class surfaces for Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat, and X Ads.
### Does Claude Ads automatically change ad accounts?
No. Claude Ads is read-only by default. A live change requires exact capability support, a preview, explicit owner approval, idempotency, verification, an audit record, and rollback.
### Does every audit receive a health score?
No. Claude Ads withholds a health score when evidence coverage is insufficient or the applicable platform scoring profile is disabled. Unknown findings reduce evidence coverage without being converted into failures.
### How do I update an existing installation?
Use the native Claude Code plugin flow and ask Claude to update to v2.0.1 from the public repository. Run the validation workflow after the update and confirm the installed version before using it on account data.
## Related Posts
* [Claude Ads v1.7.1: SSS+ Polish and Verified Citations](/blog/claude-ads-v1-7-1-release)
* [Claude Ads v1.5: 250+ Ad Audit Checks Across 7 Platforms](/blog/claude-ads-v1-5-release)
* [Claude Code Just Replaced Your Ad Agency](/blog/claude-code-ad-agency)
* [The Open-Source AI Marketing Stack I Use Daily](/blog/ai-marketing-automation-stack)
Build Better Paid-Media Systems
Join the AI Marketing Hub for open-source tools, workflow templates, and practical implementation support.
[JOIN FREE](https://www.skool.com/ai-marketing-hub)[GO PRO](https://www.skool.com/ai-marketing-hub-pro)
