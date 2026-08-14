# Claude Code Security: The AI Security Audit That Found 23 Vulnerabilities in My Own Code

**Date:** 2026-04-14 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-cybersecurity-ai-security-audit

---

claude-cybersecurity is a free, open-source Claude Code skill that turns your terminal into a full security audit platform. One command. Eight specialist agents running in parallel. Zero configuration. It covers the OWASP Top 10:2025, CWE Top 25, MITRE ATT&CK techniques, 11 programming languages, and 5 compliance frameworks. **If you are shipping code in 2026, especially vibe-coded code, you need something like this in your workflow.**
I built it after realizing that the code I was shipping with AI assistance was accumulating security debt faster than I could track. The tool paid for itself on the first run when it found an SSRF vulnerability in my own [claude-ads](/blog/claude-ads-v1-5-release) project that I had missed entirely.
Key Takeaways
* claude-cybersecurity runs 8 parallel security agents with a single `/cybersecurity` command
* Covers OWASP Top 10:2025, CWE Top 25, and 7 MITRE ATT&CK techniques across 11 languages
* AI-generated code has 2.74x more vulnerabilities than human-written code (Veracode 2025)
* Uses a weighted scoring system (0-100) with auto-CRITICAL gate for severe findings
* Free and open-source alternative to GitHub Advanced Security (GHAS)
* Install in 30 seconds with a single curl command
## What Is Claude Cybersecurity?
claude-cybersecurity is a Claude Code skill that orchestrates eight specialist security agents to audit your codebase. You type `/cybersecurity` in your terminal and it handles everything: detecting your stack, mapping trust boundaries, running parallel analyses, and producing a prioritized report with fix suggestions. No API keys. No configuration files. No SaaS subscription. It works with any project Claude Code can read, which means basically everything on your machine.
The skill follows the same architecture pattern I use in all my [Claude Code skills](/blog/best-claude-code-skills-2026): a coordinator that gathers context, dispatches specialist agents, and synthesizes their output into something actionable. The difference here is the depth. Each of the eight agents carries its own reference data, detection heuristics, and false-positive suppression rules tuned to specific frameworks.
## Why Vibe-Coded Apps Need Security Audits
Vibe coding security is not a theoretical concern anymore. The data from 2025 makes it clear that AI-assisted code carries measurably higher risk than code written by hand. If you are using Claude, Copilot, or any other AI coding tool to ship production code, you are likely introducing vulnerabilities at a rate your existing review process cannot catch.
According to Veracode's 2025 State of Software Security report, AI-generated code contains **2.74x more security flaws** than human-written code. That study analyzed over 2.2 million applications. Separately, 45% of AI-generated code snippets introduce at least one OWASP Top 10 vulnerability. Researchers at Georgia Tech tracked 74 CVEs that originated directly from AI-generated code merged into open-source projects during 2024-2025.
The pattern makes sense once you think about it. AI models are trained on the entire internet, including millions of Stack Overflow answers and tutorials that use insecure patterns for the sake of simplicity. The model optimizes for "code that works" not "code that is secure." It will happily generate SQL queries with string concatenation, store secrets in plaintext, or skip input validation if you do not explicitly ask for those things.
Traditional SAST tools catch some of this, but they were designed for patterns that human developers write. AI introduces new categories of risk: hallucinated dependencies (packages that do not exist, which attackers register as malware), overconfident security implementations that look correct but have subtle flaws, and a particular tendency to copy insecure patterns from training data without understanding why they are dangerous.
## The 8 Specialist Agents
Rather than running a single monolithic scan, claude-cybersecurity dispatches eight focused agents that run in parallel. Each agent has a specific security domain, a weighted contribution to the overall score, and its own set of detection rules. This parallel architecture means the full audit completes faster than a sequential scan while catching cross-domain issues that single-purpose tools miss.
8 Specialist Agents — Parallel ExecutionVulnerability Scanner20% — OWASP Top 10 + CWE Top 25, taint analysisAuth Reviewer15% — IDOR, privilege escalation, session managementThreat Intel15% — Malware, backdoors, C2 comm, MITRE ATT&CKSecrets10% — Semantic detection, obfuscated credentialsDeps10% — Supply chain, slopsquatting, typosquattingIaC10% — Terraform, Docker, K8s, GitHub ActionsAI Code10% — AI-generated patterns, hallucinated depsLogic10% — Business logic, race conditions, TOCTOU
**Vulnerability Scanner (20%)** is the heaviest agent. It performs taint analysis, tracks data flow from user inputs to dangerous sinks, and maps findings against both the OWASP Top 10:2025 and CWE Top 25:2024 catalogs. This agent catches injection flaws, XSS, deserialization issues, and path traversal vulnerabilities.
**Auth Reviewer (15%)** focuses exclusively on authentication and authorization. It looks for IDOR (Insecure Direct Object Reference) patterns, privilege escalation paths, broken session management, and missing access controls. This agent is especially good at catching the "forgot to check permissions" bugs that are rampant in AI-generated code.
**Threat Intelligence (15%)** scans for indicators of compromise: malware signatures, backdoor patterns, command-and-control communication channels, and known attack techniques mapped to the MITRE ATT&CK framework. This is the agent that would flag it if a dependency or code snippet contained obfuscated malicious payloads.
**Secrets Detection (10%)** goes beyond regex-based secret scanning. It uses semantic analysis to find obfuscated credentials, hardcoded tokens disguised as configuration values, and secrets that have been base64 encoded or split across multiple variables. Traditional secret scanners miss these patterns regularly.
**Dependency Auditor (10%)** handles supply chain security. It checks for known vulnerable dependencies, typosquatting (packages with names similar to popular ones), and slopsquatting (packages that AI models hallucinate into existence and that attackers then register on npm/PyPI). This is a growing attack vector that most teams are not monitoring.
**IaC Scanner (10%)** audits your infrastructure-as-code: Terraform configurations, Dockerfiles, Kubernetes manifests, and GitHub Actions workflows. Misconfigured infrastructure is one of the leading causes of breaches, and this agent catches overly permissive IAM policies, unpinned action versions, exposed ports, and insecure container configurations.
**AI Code Reviewer (10%)** specifically targets patterns common in AI-generated code. Hallucinated dependencies, copy-pasted insecure patterns from training data, overconfident crypto implementations, and the characteristic "looks right but is subtly broken" code that LLMs produce. This agent exists because AI code has different failure modes than human code.
**Business Logic Analyzer (10%)** looks for race conditions, TOCTOU (Time of Check to Time of Use) bugs, improper state machine transitions, and logic flaws that cannot be detected by pattern matching alone. These are the vulnerabilities that are hardest to find with traditional SAST tools because they require understanding the application's intended behavior.
## How It Works: The GARE Architecture
The skill follows a four-phase architecture called GARE: Gather, Analyze, Recommend, Execute. This is the same orchestration pattern used in enterprise security tools, adapted to run entirely within Claude Code's execution environment. The entire pipeline runs locally with no data leaving your machine.
PHASE 1: GATHER
Detect stack | Enumerate entry points | Map trust boundaries | STRIDE analysis | Build context
🔍
PHASE 2: ANALYZE — 8 Agents in Parallel
Vuln20%
Auth15%
Threat15%
Secrets10%
Deps10%
IaC10%
AI Code10%
Logic10%
Each agent loads its own reference files | Returns VULN-XXX findings + category score (0-100) + confidence levels
PHASE 3: RECOMMEND
Score aggregation | Attack-path chaining | Compliance
PHASE 4: EXECUTE
Structured report | Prioritized remediation queue
/cybersecurity [path] [--scope full|quick|diff] [--compliance pci|hipaa|soc2|gdpr]
Zero configuration | Auto-detects languages and frameworks | Framework-aware FP suppression
**Phase 1: Gather.** The coordinator scans your project to detect languages, frameworks, and infrastructure. It enumerates entry points (API routes, form handlers, CLI interfaces), maps trust boundaries (where user input enters the system), and performs a STRIDE threat model. This context is passed to every agent so they know what they are looking at.
**Phase 2: Analyze.** All eight agents run in parallel. Each receives the gathered context plus its own domain-specific reference files. Each returns a list of findings (tagged as VULN-001, VULN-002, etc.) with severity scores, confidence levels, affected files, and suggested fixes. The parallel execution means a full audit on a medium-sized codebase takes minutes, not hours.
**Phase 3: Recommend.** The coordinator aggregates findings across all agents, deduplicates overlapping issues, chains related vulnerabilities into attack paths, and maps everything against your selected compliance framework (PCI DSS, HIPAA, SOC 2, GDPR, or NIST 800-53). The output is a prioritized remediation queue ordered by risk.
**Phase 4: Execute.** The final report includes the overall security score, a letter grade (A through F), every finding with its severity and confidence level, and specific code-level fix suggestions. You can ask Claude Code to apply fixes directly, or export the report for your team to review.
## Real Results: Auditing Claude Ads (62/100 to 90/100)
The best way to show what this tool does is to share what happened when I ran it against my own code. I pointed claude-cybersecurity at the [claude-ads v1.5](/blog/claude-ads-v1-5-release) codebase, expecting a clean bill of health. I was wrong. The initial score came back at 62/100, a D grade. The tool found 23 vulnerabilities across 5 categories.
The most serious finding was an SSRF (Server-Side Request Forgery) vulnerability in the API integration layer. The code accepted user-provided URLs for webhook callbacks without validating the destination. An attacker could have used this to make the server send requests to internal services. The tool flagged it as CRITICAL with HIGH confidence and provided the exact fix: URL validation with an allowlist of permitted domains.
The IaC agent found that several GitHub Actions workflows used unpinned action versions (e.g., `uses: actions/checkout@v4` instead of pinning to a specific SHA). This is a supply chain risk because a compromised action could inject malicious code into the CI pipeline. The fix was straightforward: pin every action to its full commit SHA.
The tool also flagged missing CI security gates. There was no automated security scanning in the CI pipeline, meaning vulnerabilities could be merged without any automated check. I added CodeQL scanning and dependency review as required checks. After applying all 23 fixes and re-running the audit, the score jumped to 90/100. That work shipped in the [v1.5.1 patch release](/blog/claude-ads-v1-5-release).
## Scoring System
The scoring system is designed to be both precise and practical. Every finding gets a severity score calculated from four factors: base severity (mapped from CVSS), confidence level, exploitability, and contextual modifiers. The overall project score is a weighted aggregate of all eight agent scores, where the weights match the percentages shown in the agents chart above.
Security Score — 0 to 100
F
D
C
B
A
0
25
50
75
90
100
Score = Base Severity (CVSS) x Confidence (0.3-1.0) x Exploitability (0.5-1.0) +/- Context (-20 to +20)
4-tier confidence: HIGH (90-100%) | MEDIUM (60-89%) | LOW (30-59%) | INFO (<30%)
CRITICAL 90-100
HIGH 70-89
MEDIUM 40-69
LOW 20-39
INFO 0-19
There are five severity tiers: CRITICAL (90-100), HIGH (70-89), MEDIUM (40-69), LOW (20-39), and INFO (0-19). There are four confidence tiers: HIGH (90-100%), MEDIUM (60-89%), LOW (30-59%), and INFO (below 30%). The confidence tier directly scales the impact of a finding on your score, so a LOW-confidence CRITICAL finding does not tank your score the way a HIGH-confidence one does.
The auto-CRITICAL gate is an important feature. If any single finding scores 90 or above with HIGH confidence, the overall project score is automatically capped at 69 (C grade) regardless of how well everything else scores. This prevents a project from getting an A while harboring a known critical vulnerability. You have to fix the critical issues first.
## What It Covers
The coverage spans the major security standards and frameworks that matter for modern web applications and APIs. Rather than trying to be exhaustive about everything, claude-cybersecurity focuses on the vulnerability classes that actually appear in real-world breaches. Every detection rule maps to at least one standard, so findings are traceable to industry benchmarks.
Coverage at a Glance
10/10
OWASP Top 10
2025 Edition
Incl. new A03 Supply Chain
+ A10 Exceptional Conditions
25/25
CWE Top 25
2024 Data
Dedicated detection section
for each CWE
7
MITRE ATT&CK
Techniques
T1059 T1027 T1071 T1195
T1005 T1041 T1496
5
Compliance
Frameworks
PCI DSS | HIPAA | SOC 2
GDPR | NIST 800-53
11 Languages:
Python JS/TS Java Go Rust C/C++ Ruby PHP C# Swift/Kotlin Shell
4 IaC Platforms:
Terraform (AWS/GCP/Azure) Dockerfile Kubernetes GitHub Actions
10 Frameworks with False-Positive Suppression:
Django Flask FastAPI Express React Vue Angular Spring Boot Rails ASP.NET Core +7 ORMs
The OWASP Top 10:2025 edition includes two new categories that previous versions did not cover: A03 (Software and Data Integrity / Supply Chain) and A10 (Exceptional Conditions). The Dependency Auditor and IaC Scanner agents handle A03, while the Business Logic Analyzer covers A10. All 10 categories have dedicated detection logic.
Language support spans 11 languages: Python, JavaScript/TypeScript, Java, Go, Rust, C/C++, Ruby, PHP, C#, Swift/Kotlin, and Shell scripts. The tool auto-detects which languages are present and loads the appropriate detection rules. Framework-aware false-positive suppression is available for 10 major frameworks including Django, FastAPI, Express, React, Spring Boot, and Rails, plus 7 ORMs.
## Claude Code Security vs GitHub Advanced Security
GitHub Advanced Security (GHAS) is the most common comparison point, so let me address it directly. GHAS is a solid enterprise product. It integrates tightly with GitHub, runs automatically in CI, and has excellent CodeQL analysis. But it comes with significant limitations that make claude-cybersecurity a compelling GitHub Advanced Security alternative for many teams.
| Capability | GHAS | claude-cybersecurity |
| --- | --- | --- |
| Cost | $49/committer/mo | Free (open-source) |
| Languages | 9 (CodeQL) | 11 |
| OWASP Top 10:2025 | Partial | Full 10/10 |
| Business logic analysis | No | Yes (dedicated agent) |
| AI code-specific checks | No | Yes (hallucinated deps, etc.) |
| IaC scanning | Limited | Terraform, Docker, K8s, Actions |
| Compliance mapping | No | PCI, HIPAA, SOC 2, GDPR, NIST |
| MITRE ATT&CK mapping | No | 7 techniques |
| CI integration | Native | Via Claude Code CLI |
| Data stays local | No (cloud) | Yes |
| Fix suggestions | Basic | Code-level with auto-apply |
GHAS excels at CI integration and has the advantage of running automatically on every pull request. claude-cybersecurity is better for on-demand deep audits, supports more languages, includes business logic and AI-specific checks, and costs nothing. For most teams, the ideal setup is using both: GHAS for continuous CI scanning and claude-cybersecurity for periodic deep audits and pre-release security reviews.
## How to Install
Installation takes about 30 seconds. The one-liner install script clones the repo and copies the skill files into your project's `.claude/skills/` directory. You can also install manually if you prefer to inspect the files first.
**One-liner install:**
```
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-cybersecurity/main/install.sh | bash
```
**Manual install:**
```
git clone https://github.com/AgriciDaniel/claude-cybersecurity.git
cp -r claude-cybersecurity/.claude/skills/cybersecurity your-project/.claude/skills/
```
**Quick start commands:**
```
# Full security audit
/cybersecurity
# Audit a specific directory
/cybersecurity src/
# Quick scan (faster, fewer checks)
/cybersecurity --scope quick
# Audit with compliance mapping
/cybersecurity --compliance soc2
# Scan only changed files (great for PRs)
/cybersecurity --scope diff
```
The skill works with any project that Claude Code can read. There are no external dependencies, no API keys, and no configuration files to set up. If you want to learn more about building and customizing Claude Code skills, check out the [skill-forge guide](/blog/skill-forge-build-claude-code-skills) or browse the full [best Claude Code skills](/blog/best-claude-code-skills-2026) list.
## Frequently Asked Questions
### What is claude-cybersecurity?
claude-cybersecurity is a free, open-source Claude Code skill that performs comprehensive security audits on your codebase. It orchestrates eight specialist agents that run in parallel, covering vulnerability scanning, authentication review, threat intelligence, secrets detection, dependency auditing, infrastructure-as-code scanning, AI code review, and business logic analysis. You invoke it with a single `/cybersecurity` command in your terminal.
### How does it compare to GitHub Advanced Security?
GHAS costs $49 per committer per month and focuses on CodeQL-based SAST scanning with strong CI integration. claude-cybersecurity is free, supports more languages (11 vs 9), includes business logic and AI-specific checks that GHAS lacks, and maps findings to compliance frameworks. GHAS is better for automated CI gates. claude-cybersecurity is better for deep on-demand audits. Many teams use both together.
### What languages does it support?
The tool supports 11 programming languages: Python, JavaScript, TypeScript, Java, Go, Rust, C, C++, Ruby, PHP, C#, Swift, Kotlin, and Shell scripts. It auto-detects which languages are present in your project and loads the appropriate detection rules. Framework-aware false-positive suppression is available for Django, Flask, FastAPI, Express, React, Vue, Angular, Spring Boot, Rails, and ASP.NET Core.
### Is it free?
Yes. claude-cybersecurity is MIT licensed and completely free. The skill itself has no cost, no API keys, and no usage limits. You do need Claude Code to run it, which requires either an Anthropic API key (pay-per-use) or a Claude Pro/Team subscription. But the security skill itself adds zero additional cost to whatever you are already paying for Claude Code access.
### Does it detect business logic flaws?
Yes. The Business Logic Analyzer is one of the eight specialist agents. It looks for race conditions, TOCTOU (Time of Check to Time of Use) vulnerabilities, improper state machine transitions, and logic flaws that pattern-matching SAST tools cannot detect. This is possible because Claude Code understands the semantic meaning of your code, not just its syntax. It is one of the key advantages over traditional static analysis tools.
### What is the OWASP Top 10:2025?
The OWASP Top 10:2025 is the latest edition of the Open Web Application Security Project's list of the ten most critical web application security risks. It was updated from the 2021 edition to reflect the evolving threat landscape. Notable changes include the addition of A03 (Software and Data Integrity / Supply Chain) and A10 (Exceptional Conditions). claude-cybersecurity covers all 10 categories with dedicated detection logic for each one.
## Related Posts
* [claude-ads v1.5: 250+ Ad Audit Checks](/blog/claude-ads-v1-5-release) - The project that was the first real-world test for claude-cybersecurity
* [Best Claude Code Skills in 2026](/blog/best-claude-code-skills-2026) - The complete guide to the top Claude Code skills
* [skill-forge: Build Your Own Claude Code Skills](/blog/skill-forge-build-claude-code-skills) - Build and publish Claude Code skills in minutes
* [Claude Code Just Replaced Your Entire SEO Stack](/blog/claude-code-seo-stack) - Another example of what Claude Code skills can do
Join the AI Marketing Hub
Free community for AI tools, skills, and marketing automation
[Join Free](https://www.skool.com/ai-marketing-hub)
