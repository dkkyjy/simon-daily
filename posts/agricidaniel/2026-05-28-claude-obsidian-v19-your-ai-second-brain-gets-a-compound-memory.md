# Claude Obsidian v1.9: Your AI Second Brain Gets a Compound Memory

**Date:** 2026-05-28 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-obsidian-v1-9-compound-vault

---

## What Changed in This claude-obsidian Update?
The public version of claude-obsidian jumped from v1.6 all the way to [v1.9.2](https://github.com/AgriciDaniel/claude-obsidian/releases/tag/v1.9.2), and the headline is the "Compound Vault" arc. The retrieval upgrade behind it is grounded in Anthropic's contextual retrieval research, which cut retrieval failures by up to 49%, and up to 67% once reranking is added ([Anthropic](https://www.anthropic.com/news/contextual-retrieval), 2024). In short, your second brain now remembers better.
Claude Obsidian in two minutes: drop a source, watch the wiki build itself.
If you've used claude-obsidian before, here's the quick map of what landed. If you're new, skip down to the primer first, it'll make the rest click.
* **v1.7 Compound Vault:** Obsidian CLI as the default transport, hybrid retrieval, and per-file advisory locking for safe multi-agent ingest.
* **v1.8:** methodology modes, so the vault organizes itself the way you already think.
* **v1.9:** the /think skill, a 10-principle thinking framework, taking the plugin from 14 to 15 skills.
* **v1.9.1 and v1.9.2:** audit hardening and prompt-cache hardening, the unglamorous work that keeps it reliable.
The Compound Vault adds smarter retrieval and safe multi-writer ingest, all over plain Markdown.
## Why Does Hybrid Retrieval Matter?
Hybrid retrieval is the upgrade you'll feel first. It pairs a contextual prefix with BM25 keyword search and a cosine rerank, and that combination is exactly what catches the near-misses a pure-similarity search hands you. The result: your wiki pulls the right pages, not just the ones that sound similar.
Why does this matter for a second brain? Because the failure mode of every knowledge tool is confidently fetching the wrong note. A pure-similarity search will hand you a page that mentions the same words but answers a different question. Layering keyword matching and a rerank on top of context-aware chunks catches the near-misses. You ask, it retrieves, and the answer cites the page it actually came from.
Worth being honest here: this is opt-in. The core wiki still runs on plain Markdown with no embeddings server. Hybrid retrieval is there when you want sharper recall on a big vault, not a requirement bolted onto everyone by default.
## What Are Methodology Modes and Multi-Writer Safety?
Two quieter features in the update punch above their weight. Methodology modes and per-file locking both exist for the same reason: a second brain should bend to how you work and survive heavy use. AI knowledge management already saves workers 30-45% of retrieval time ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai), 2025); these features protect that gain at scale.
### Methodology modes
Pick one of four organizing styles: LYT (maps of content plus atomic notes), PARA (projects, areas, resources, archives), Zettelkasten (timestamped, flat, densely linked), or Generic (no opinion). You set the mode once. After that, ingestion, /save, and /autoresearch all route new pages to the right place automatically. The AI files notes the way you already think.
### Multi-writer safety
Per-file advisory locking means multiple agents can ingest into the same vault at once without stepping on each other. Before this, a parallel ingest could corrupt a page mid-write. Now each file write is guarded, so you can run multi-agent research loops and trust the vault on the other side.
Per-file locks let several agents ingest at once without corrupting your notes.
## New Here? What Is claude-obsidian?
If this is your first contact with the project, here's the primer. claude-obsidian is a free, MIT-licensed Claude Code plugin that turns Obsidian into a self-organizing AI second brain, built on Andrej Karpathy's LLM Wiki pattern ([Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), 2025). You drop in sources; the AI reads them and writes the linked notes.
The core is refreshingly boring in the best way: three plain files. A hot cache holding recent context, an index, and your wiki pages, all plain Markdown you own and can open in Obsidian forever. No database, no embeddings server for the core, nothing to migrate or host. Drop any source, ask any question, and the wiki grows richer with every session.
For the full guide, with the workflow, the comparison to Notion, and how the hot cache kills session amnesia, read the pillar: [how I turned Obsidian into a self-organizing AI second brain](/blog/claude-obsidian-ai-second-brain).
## How Do You Get or Update It?
Getting the update is a two-line job, and your existing notes are never touched. claude-obsidian stays free and MIT licensed through v1.9, sitting in a market growing at 30.3% CAGR toward $6.15 billion by 2030 ([Research and Markets](https://www.researchandmarkets.com/reports/6226503/personal-knowledge-base-ai-market-report), 2026) while charging nothing for the plugin itself.
Fresh install:
```
git clone https://github.com/AgriciDaniel/claude-obsidian.git my-wiki
bash my-wiki/bin/setup-vault.sh
```
Already using it? Pull the latest, or re-add via the Claude Code marketplace with `claude plugin marketplace add AgriciDaniel/claude-obsidian`. Because there's no database, there's nothing to migrate. The update only changes the plugin skills; your Markdown vault carries over untouched. If you want the visual companion, [claude-canvas](https://github.com/AgriciDaniel/claude-canvas) pairs cleanly with it.
## Frequently Asked Questions
### What is the claude-obsidian Compound Vault update?
Compound Vault is the v1.7 to v1.9 arc. It adds hybrid retrieval, methodology modes, a thinking framework, and per-file locking for multi-writer safety. The retrieval layer draws on Anthropic research that cut retrieval failures up to 49%, and up to 67% with reranking ([Anthropic](https://www.anthropic.com/news/contextual-retrieval), 2024).
### What is hybrid retrieval in claude-obsidian?
Hybrid retrieval combines a contextual prefix, BM25 keyword search, and a cosine rerank so your second brain pulls the most relevant pages, not just similar-sounding ones. It is based on Anthropic's contextual retrieval research, designed to surface the right page, not just a similar-sounding one.
### What are methodology modes?
Methodology modes let you pick how the vault organizes new pages: LYT, PARA, Zettelkasten, or Generic. You set the mode once and ingestion, saving, and autoresearch route pages accordingly. It means the AI files notes the way you already think, instead of forcing one rigid structure on everyone.
### How do I update to claude-obsidian v1.9?
Pull the latest from the public GitHub repo, or re-add it via the Claude Code marketplace with the marketplace add command. Your existing Markdown vault is untouched; the update only changes the plugin skills. The whole thing stays free and MIT licensed, with no database to migrate at all.
### Is claude-obsidian still free after the update?
Yes. claude-obsidian remains MIT licensed and fully open source through v1.9. You pay only for your own AI model usage, and Obsidian is free for personal use. The Compound Vault features add no subscription, no hosted vector database, and no background worker burning your RAM.
## The Short Version
Compound Vault makes your AI second brain remember better, file the way you think, and survive multiple writers, all while staying plain Markdown you own. The retrieval gains are real, and the price is still zero.
* Star or update the repo on [GitHub](https://github.com/AgriciDaniel/claude-obsidian).
* New here? Start with the full guide: [the self-organizing AI second brain](/blog/claude-obsidian-ai-second-brain).
