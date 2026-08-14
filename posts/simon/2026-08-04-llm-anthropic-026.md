# llm-anthropic 0.26

        **Date:** 2026-08-04 22:00 UTC
        **Link:** https://simonwillison.net/2026/Aug/4/llm-anthropic/#atom-everything
        **Tags:** llm, anthropic, claude, model-context-protocol

        ---

        > *Feed summary: Release: llm-anthropic 0.26
        Includes new features enabled by LLM 0.32:


New models: claude-fable-5, claude-sonnet-5, and claude-opus-5. #75, #76
Added server-side tools for WebSearch, WebFetc*

4th August 2026

[Release](/elsewhere/release/)
[llm-anthropic 0.26](https://github.com/simonw/llm-anthropic/releases/tag/0.26)
— LLM access to models by Anthropic, including the Claude series

Includes new features enabled by [LLM 0.32](https://simonwillison.net/2026/Aug/4/new-release-of-llm/):

> * New models: `claude-fable-5`, `claude-sonnet-5`, and `claude-opus-5`. [#75](https://github.com/simonw/llm-anthropic/issues/75), [#76](https://github.com/simonw/llm-anthropic/issues/76)
> * Added server-side tools for `WebSearch`, `WebFetch`, `CodeExecution`, and `AnthropicMCP`, available through LLM's `-T` interface or Python `tools=`. The previous `-o web_search*` options have been removed in favor of `-T WebSearch`. [#79](https://github.com/simonw/llm-anthropic/issues/79)
> * Upgraded to [llm>=0.32](https://llm.datasette.io/en/stable/changelog.html#v0-32). Reasoning, tool calls, tool results, and server-side tool results now stream as typed events. Reasoning for `llm` CLI prompts now displays to standard error unless you pass `--hide-reasoning/-R`.
> * Simplified extended thinking to `thinking` and `thinking_effort` (`low`, `medium`, `high`, `xhigh`, or `max`). Claude 5 models think by default; `-o thinking 0` disables thinking for Sonnet 5 and Opus 5, while Fable 5 always thinks. `-R/--hide-reasoning` now omits reasoning from responses and logs. The `thinking_budget`, `thinking_display`, and `thinking_adaptive` options have been removed. [#80](https://github.com/simonw/llm-anthropic/issues/80)

Posted [4th August 2026](/2026/Aug/4/) at 10 pm
