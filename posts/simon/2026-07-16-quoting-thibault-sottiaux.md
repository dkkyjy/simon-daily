# Quoting Thibault Sottiaux

        **Date:** 2026-07-16 17:45 UTC
        **Link:** https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything
        **Tags:** codex, coding-agents, generative-ai, ai, llms

        ---

        > *Feed summary: On file deletions. We’ve investigated a handful of reports where GPT-5.6 unexpectedly deleted files. 
What we have  found is that this most commonly occurs when:

Full access mode is enabled and codex*

16th July 2026

> On file deletions. We’ve investigated a handful of reports where GPT-5.6 unexpectedly deleted files.
>
> What we have found is that this most commonly occurs when:
>
> * Full access mode is enabled and codex is run without sandboxing protections, including without auto review being enabled
> * The model attempts to override the $HOME env var to define a temporary directory.
> * The model makes an honest mistake and mistakenly deletes $HOME instead.

— [Thibault Sottiaux](https://twitter.com/thsottiaux/status/2077630111499882637), describing a pretty gnarly Codex bug

Posted [16th July 2026](/2026/Jul/16/) at 5:45 pm
