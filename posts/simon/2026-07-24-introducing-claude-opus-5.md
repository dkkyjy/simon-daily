# Introducing Claude Opus 5

        **Date:** 2026-07-24 23:48 UTC
        **Link:** https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything
        **Tags:** ai, generative-ai, llms, anthropic, claude, llm-release

        ---

        > *Feed summary: Introducing Claude Opus 5
I've been offline kayaking with sea otters for much of today so I haven't had a chance to put Anthropic's new model Claude Opus 5 through its paces yet. The buzz is positive,*

24th July 2026 - Link Blog

**[Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)**. I've been offline [kayaking with sea otters](https://en.wikipedia.org/wiki/Elkhorn_Slough) for much of today so I haven't had a chance to put Anthropic's new model Claude Opus 5 through its paces yet. The buzz is positive, and Anthropic's description of it as a "thoughtful and proactive model that comes close to the frontier intelligence of Claude Fable 5 at half the price" sounds promising. It's currently [leading the Artificial Analysis leaderboard](https://twitter.com/artificialanlys/status/2080777718933995967), in front of even Fable 5.

It's priced the same as Opus 4.8, and continues to offer a "fast mode" at twice the cost of the base model.

Based on this anecdote in the release post it sounds like it might be [relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/):

> On one Frontier-Bench task, Opus 5 was given a drawing of a machine part and asked to write code to rebuild it as a 3D FreeCAD model. However, in this task, the model was intentionally given no way to directly viewthe drawing. Opus 5 responded by writing its own computer vision pipeline to pull the geometry from the raw pixels, then reconstructed the full machine part.

It's better at finding vulnerabilities but has deliberately not been trained on how to exploit them. Hopefully this means the US government won't shut it down!

> As with its predecessor, Opus 4.8, we’ve intentionally avoided training Opus 5 on cyber tasks. The model has nevertheless improved substantially on these tasks as a result of becoming more generally capable, and it comes close to Mythos 5 at *finding* cybersecurity vulnerabilities. However, it remains substantially behind Mythos 5 on the *exploitation* of those vulnerabilities—that is, in turning vulnerabilities into material cyber threats.

Anthropic have published a [prompting guide for Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5). Thariq Shihipar has also written [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models).

The [first pelican I got](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fraw.githubusercontent.com%2Fsimonw%2Fllm-anthropic%2F8272dfee5bdb65d5c88eef083da3ad885539b7df%2Flog.md) was missing the bicycle wheels; the [second attempt](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fraw.githubusercontent.com%2Fsimonw%2Fllm-anthropic%2Ffeaab840ea20eb15e29d8f72a9e42feceb23876a%2Flog.md) was better.

Posted [24th July 2026](/2026/Jul/24/) at 11:48 pm
