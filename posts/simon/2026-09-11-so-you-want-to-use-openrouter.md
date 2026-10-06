# So you want to use OpenRouter?

        **Date:** 2026-09-11 22:49 UTC
        **Link:** https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/
        **Tags:** ai, generative-ai, llms, openrouter

        ---

        > *Feed summary: So you want to use OpenRouter?
One of OpenRouter's selling points is that it "handles fallbacks automatically and picks the most cost-effective option for each request", so you can call a single API e*

11th September 2026 - Link Blog

**[So you want to use OpenRouter?](https://mmoustafa.com/blog/so-you-want-to-use-openrouter/)** ([via](https://news.ycombinator.com/item?id=49621546 "Hacker News")) One of OpenRouter's selling points is that it "handles fallbacks automatically and picks the most cost-effective option for each request", so you can call a single API endpoint for a model and get routed to the best available backend provider.

Mohamed Moustafa points out a whole set of ways that this can cause you problems. Different providers run different serving software with different optimizations and settings, which means that the same OpenRouter endpoint can serve model requests that behave in different ways.

Some providers even lack vision capability for vision models, and the way the reasoning effort option is processed can differ as well.

Thankfully you can control which provider is routed to using [the provider.only option](https://openrouter.ai/docs/guides/routing/provider-selection#allowing-only-specific-providers). The [/endpoints method](https://openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model) returns the list of available providers for a specific model ID.

Posted [11th September 2026](/2026/Sep/11/) at 10:49 pm
