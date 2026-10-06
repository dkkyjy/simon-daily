# Qwen3.8-Flash-Next

        **Date:** 2026-08-26 23:52 UTC
        **Link:** https://simonwillison.net/2026/Aug/26/qwen38-flash-next/
        **Tags:** ai, generative-ai, llms, qwen, pelican-riding-a-bicycle, ai-in-china, nvidia-spark

        ---

        > *Feed summary: Qwen3.8-Flash-Next
Another open weights model from Qwen. This one is "a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4".
It's pretty big: 125B tokens, but *

26th August 2026 - Link Blog

**[Qwen3.8-Flash-Next](https://qwen.ai/blog?id=qwen3.8-flash-next)** ([via](https://news.ycombinator.com/item?id=49448210 "Hacker News")) Another open weights model from Qwen. This one is "a multimodal MoE model that also serves as an early preview of the architecture used in Qwen4".

It's pretty big: 125B tokens, but only 6B active which means it gets a significant performance boost.

I've been trying it out on a DGX Spark using [these Unsloth quantized models](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF). I'm still exploring the model - so far I've tried the 72.5GB UD-IQ1\_S one (producing [these pelicans](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ff9c69ebdab90d8a45b8de4742cc7b840)) and the 78.9GB UD-Q2\_K\_XL (producing [these](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6ba7cbfc1a9336986703b41f7fccd73a)).

My favorite so far was this xhigh reasoning effort one from UD-Q2\_K\_XL:

Posted [26th August 2026](/2026/Aug/26/) at 11:52 pm
