# Rewriting Bun in Rust

        **Date:** 2026-07-08 23:57 UTC
        **Link:** https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything
        **Tags:** ai, rust, zig, generative-ai, llms, ai-assisted-programming, anthropic, bun, conformance-suites, agentic-engineering, claude-mythos-fable

        ---

        Rewriting Bun in Rust Jarred Sumner has been promising this blog post ( since May 9th ) about his Zig to Rust rewrite of Bun for significantly longer than it took him to finish the rewrite. Honestly, it was worth the wait. This is a detailed description of an extremely sophisticated piece of agentic engineering, featuring dynamic workflows, trial runs, adversarial review and all sorts of other interesting tricks. Jarred spends the first half of the post praising Zig for getting Bun this far. Then we get to a core idea in the piece, emphasis mine: Our bugfix list felt bad and I was tired of going to sleep worrying about crashes in Bun. I don't blame Zig for that - other users of Zig don't have the bugs we had, and mixing GC with manually-managed memory is an uncommon enough thing for software to need that no language really designs for it. We wouldn't have gotten this far if not for Zig, and I'll always be grateful. Until very recently, programming language choice was a one-way decision for a project like Bun. Everyone knows you should never stop the world and rewrite a large piece of software from the ground up. Joel Spolsky highlighted that in Things You Should Never Do, Part I back in April 2000! Coding agents powered by today's frontier models change that equation. Why pick Rust? It all came down to those challenges with memory management: A large percentage of bugs from that list are use-after-free, double-free, and "forgot to free" in an error path. In safe Rust, these are compiler errors and RAII-like automatic cleanup with Drop . A crucial enabling factor for the rewrite was that the Bun test suite was written in TypeScript, which meant it could act as a conformance suite

*(truncated, see original)*
