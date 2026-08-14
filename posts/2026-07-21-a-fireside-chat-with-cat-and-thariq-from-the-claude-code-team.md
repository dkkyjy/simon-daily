# A Fireside Chat with Cat and Thariq from the Claude Code team

        **Date:** 2026-07-21 12:54 UTC
        **Link:** https://simonwillison.net/2026/Jul/21/cat-and-thariq/#atom-everything
        **Tags:** ai, prompt-engineering, generative-ai, llms, anthropic, annotated-talks, coding-agents, claude-code, thariq-shihipar, cat-wu

        ---

        Earlier this month I hosted a fireside chat session at the AI Engineer World's Fair with Cat Wu and Thariq Shihipar from Anthropic's Claude Code team. We talked about Claude Code, Claude Tag, Fable, coding agent security, evals, tool design, and how Anthropic use these tools themselves. The full video of the session is now available on YouTube . Below is an edited copy of the transcript, with extra links and my own bolded highlights. A few top-level notes if you don't want to watch the video or wade through the whole transcript: Claude Tag (Claude's new collaborative Slack integration) now lands 65% of the product engineering PRs for the Claude Code team. Claude Code ships features to Anthropic employees first, and only ships the features that demonstrate user retention with that cohort Critical changes to Claude Code are still reviewed manually, but the team increasingly relies on automated code review for the "outer layers" of the product. Adding examples to a system prompt is no longer best practice for models like Fable 5 or even Opus 4.8. The Claude Code system prompt recently reduced in size by 80% . Likewise, lists of " don't do X and don't do Y " can reduce the quality of results from the latest models. Dogfooding inside Anthropic is called " ant fooding ". Anthropic really believe in their auto mode , and see that as an enabling technology for Claude Tag. Thariq advises offsetting coding-agent-induced Deep Blue by " being more ambitious " with the work you take on. Fable is competent at editing video , and Thariq used it to edit its own launch video. Anthropic's culture of working (internally) in public is key to their success, as demonstrated by the way they use Claude Tag in their public Slack Channels.

*(truncated, see original)*
