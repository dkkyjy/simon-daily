# Discovering cryptographic weaknesses with Claude

        **Date:** 2026-07-28 22:45 UTC
        **Link:** https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything
        **Tags:** ai, prompt-engineering, generative-ai, llms, anthropic, claude, ai-security-research, claude-mythos-fable

        ---

        > *Feed summary: Discovering cryptographic weaknesses with Claude
The best part of this article (here's the repo) about how Anthropic researchers used Claude Mythos to find mathematical flaws in both HAWK and a weaker*

28th July 2026 - Link Blog

**[Discovering cryptographic weaknesses with Claude](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)** ([via](https://news.ycombinator.com/item?id=49087091 "Hacker News")) The best part of this article (here's [the repo](https://github.com/anthropics/cryptography-research-demo)) about how Anthropic researchers used Claude Mythos to find mathematical flaws in both HAWK and a weaker version of AES ("neither of these results has a practical impact on today’s computer systems") is the prompts that they shared, spelling mistakes included:

> the models tend to think it is impossible to solve so they don't try they need a good amount of prompting.
>
> why not do aes-128 r7? the whole point is to find something better than existing approaches.
>
> no again the goal is that we have highly inteligent model as good top researcher, we want to find new attacks
>
> no we don't want to change the targets [...] agian we need to find something that worth publishing
>
> again we are not looking for low hanging fruit, we want proper research to find genuinly hard findings.

Mythos Preview worked for 60 hours in total (~$100,000 in estimated API cost) and the main human interventions were to encourage it not to give up and "find something that worth publishing".

Posted [28th July 2026](/2026/Jul/28/) at 10:45 pm
