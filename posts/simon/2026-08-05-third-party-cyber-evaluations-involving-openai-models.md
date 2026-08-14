# Third-party cyber evaluations involving OpenAI models

        **Date:** 2026-08-05 23:45 UTC
        **Link:** https://simonwillison.net/2026/Aug/5/third-party-cyber-evaluations/#atom-everything
        **Tags:** security, ai, openai, llms, accidental-cyberattacks

        ---

        > *Feed summary: Third-party cyber evaluations involving OpenAI models
And another one. I had to create a accidental-cyberattacks tag to keep track of them all!
This post from OpenAI covers both the UK AI Safety Insti*

5th August 2026 - Link Blog

**[Third-party cyber evaluations involving OpenAI models](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/)**. And *another one*. I had to create a [accidental-cyberattacks tag](https://simonwillison.net/tags/accidental-cyberattacks/) to keep track of them all!

This post from OpenAI covers both the UK AI Safety Institute attack (see [my previous post](https://simonwillison.net/2026/Aug/5/incident-report/)) and another attack enabled by [Irregular](https://www.irregular.com):

> Irregular, one of our external cybersecurity testing partners, was running Capture-the-Flag-style evaluations intended to be isolated from the internet, but a testing-environment misconfiguration allowed models to access the public internet. [...]
>
> In one test, the name of the fictional target for the CTF challenge unintentionally coincided with a real domain. Because the testing environment was mistakenly connected to the internet, the model exploited a real website, mistaking it to be part of the simulated environment.

Irregular also feature in [Anthropic's write-up](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) - they were hosting the misconfigured evaluation environment which gave Claude live internet access during some of those tests.

Posted [5th August 2026](/2026/Aug/5/) at 11:45 pm
