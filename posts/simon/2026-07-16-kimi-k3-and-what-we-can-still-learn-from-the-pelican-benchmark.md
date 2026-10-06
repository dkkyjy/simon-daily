# Kimi K3, and what we can still learn from the pelican benchmark

        **Date:** 2026-07-16 20:19 UTC
        **Link:** https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything
        **Tags:** ai, generative-ai, llms, llm-pricing, pelican-riding-a-bicycle, llm-release, ai-in-china, artificial-analysis, moonshot, kimi

        ---

        Chinese AI lab Moonshot AI announced Kimi K3 this morning, describing it as their "most capable model to date, with 2.8 trillion parameters". It's currently available via their website and API, but an open weight release is promised "by July 27, 2026". Moonshot are calling this the first "open 3T-class model" (I guess they're rounding 2.8 trillion up to 3 trillion), taking the crown from DeepSeek's 1.6T v4 Pro . Their self-reported benchmarks have K3 mostly beating Claude Opus 4.8 max and GPT-5.5 high, while losing out to Claude Fable 5 and GPT-5.6 Sol. A few highlights from the Artificial Analysis report on the model: "On our private long-horizon knowledge work evaluation, Kimi K3 reaches an overall Elo of 1547, +732 points from Kimi K2.6 and behind only Claude Fable 5." "Cost per task ($0.94) is similar to GPT-5.6 Sol ($1.04), ~1/2 the price of Opus 4.8 ($1.80) and higher than open weights peers" "Kimi K3’s token usage on the Artificial Analysis Intelligence Index decreased significantly, using 21% fewer output tokens than K2.6." The model is also now the leading model on Arena.ai's Frontend Code arena , surpassing even Claude Fable 5. The new model is notable for the pricing: $3/million input tokens and $15/million output tokens, putting it at the same level as Anthropic's Claude Sonnet series and making it the most expensive model released by a Chinese AI lab to date. This is a significant increase on their earlier models such as Kimi K2.6 at $0.95/$4. 2.8 trillion parameters is also more than twice the size of that 1T model. But how does it pelican? I used OpenRouter (to avoid signing up for a Moonshot API key) with the llm-openrouter plugin to generate an SVG of a pelican riding a bicycle: llm -m openrouter/moonshotai/kimi-k3 'Generate an SVG of

*(truncated, see original)*
