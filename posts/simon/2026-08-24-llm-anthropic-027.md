# llm-anthropic 0.27

        **Date:** 2026-08-24 16:27 UTC
        **Link:** https://simonwillison.net/2026/Aug/24/llm-anthropic/
        **Tags:** python, httpx, llm, anthropic, claude

        ---

        > *Feed summary: Release: llm-anthropic 0.27
        This release of the Anthropic plugin for LLM mainly provides compatibility with the recently released anthropic v1.0.0 Python library, which switches from httpx to *

24th August 2026

[Release](/elsewhere/release/)
[llm-anthropic 0.27](https://github.com/simonw/llm-anthropic/releases/tag/0.27)
— LLM access to models by Anthropic, including the Claude series

This release of the Anthropic plugin for [LLM](https://llm.datasette.io/) mainly provides compatibility with the recently released [anthropic v1.0.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.0.0) Python library, which switches from `httpx` to [httpx2](https://github.com/pydantic/httpx2). OpenAI made the same change in their [v3.0.0 release](https://github.com/openai/openai-python/releases/tag/v3.0.0) two weeks ago.

Anthropic provide this [migration guide](https://github.com/anthropics/anthropic-sdk-python/blob/v1.0.0/MIGRATION.md) for upgrading to 1.0, so I prompted Fable 5 in Claude Code with:

> `Upgrade to anthropic>=1 - read https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/refs/heads/main/MIGRATION.md and get the tests passing`

Here's [the resulting PR](https://github.com/simonw/llm-anthropic/pull/84).

Posted [24th August 2026](/2026/Aug/24/) at 4:27 pm
