# GitHub Models is now retired

        **Date:** 2026-08-09 22:48 UTC
        **Link:** https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/#atom-everything
        **Tags:** github, ai, github-actions, generative-ai, llms, llm-pricing

        ---

        > *Feed summary: GitHub Models is now retired
I missed this news until today, when the GitHub Actions run for my simonw/research repository failed with this error message:

GitHub Models is temporarily unavailable as *

9th August 2026 - Link Blog

**[GitHub Models is now retired](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/)**. I missed this news until today, when the GitHub Actions run for my [simonw/research](https://github.com/simonw/research) repository failed with this error message:

> GitHub Models is temporarily unavailable as part of a scheduled retirement brownout.

That message is already stale, because the retirement has been completed.

GitHub Models was an odd-shaped duck. GitHub provided a model playground tool and a unified API across a bunch of different LLM providers, with the biggest benefit being that code running in GitHub Actions could use the GitHub API key already present in that environment to execute prompts.

This made it easy to build things that fit GitHub Next's [Continuous AI](https://githubnext.com/projects/continuous-ai/) concept.

GitHub didn't share the reason behind the shutdown, but my bet is that it fits the pattern where coding agent patterns made it prohibitively expensive to offer free or subsidized tokens.

My workflow uses an LLM call to create folder summaries for [the README](https://github.com/simonw/research/blob/main/README.md), using [this code here](https://github.com/simonw/research/blob/43fa54a74ca2350bb28c2c32fbb16d42c78c442f/README.md?plain=1#L104-L113). I swapped GitHub Models out for an OpenAI API key with a monthly spending limit, and I'm now generating my summaries using GPT-5.6 Luna.

Posted [9th August 2026](/2026/Aug/9/) at 10:48 pm
