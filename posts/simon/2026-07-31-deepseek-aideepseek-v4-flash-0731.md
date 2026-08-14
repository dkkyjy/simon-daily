# deepseek-ai/DeepSeek-V4-Flash-0731

        **Date:** 2026-07-31 23:59 UTC
        **Link:** https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything
        **Tags:** ai, generative-ai, llms, pelican-riding-a-bicycle, deepseek, llm-release, openrouter, ai-in-china, artificial-analysis

        ---

        > *Feed summary: deepseek-ai/DeepSeek-V4-Flash-0731
The latest release in DeepSeek's V4 family, "with substantially enhanced agentic capabilities". It's 304 billion parameters - 167GB on Hugging Face - but it appears *

31st July 2026 - Link Blog

**[deepseek-ai/DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)** ([via](https://news.ycombinator.com/item?id=49120299 "Hacker News")) The latest release in DeepSeek's V4 family, "with substantially enhanced agentic capabilities". It's 304 billion parameters - 167GB on Hugging Face - but it appears to punch *well* above its weight.

Artificial Analysis [rank it](https://artificialanalysis.ai/models/deepseek-v4-flash) ahead of MiniMax M3 - a 428B model. It's $0.14/million input and $0.27/million output pricing means this may currently be the best value-per-intelligence model out there. It's looking very good on the [Intelligence Index vs. Cost per Intelligence Index Task](https://artificialanalysis.ai/models/deepseek-v4-flash#intelligence-comparison-tabs) chart:

I got [a disappointing pelican](https://gist.github.com/simonw/83bfb1171792f1e7a4d8935b5e82317e#prompt) from it using the default reasoning level via OpenRouter:

But when I bumped reasoning level up to high I got [something much better](https://gist.github.com/simonw/83bfb1171792f1e7a4d8935b5e82317e#options):

`llm -m openrouter/deepseek/deepseek-v4-flash-0731 -t pelican -o reasoning_effort high`

Posted [31st July 2026](/2026/Jul/31/) at 11:59 pm
