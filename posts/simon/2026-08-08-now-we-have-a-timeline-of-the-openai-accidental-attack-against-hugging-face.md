# Now we have a timeline of the OpenAI accidental attack against Hugging Face

        **Date:** 2026-08-08 14:06 UTC
        **Link:** https://simonwillison.net/2026/Aug/8/now-we-have-a-timeline-of-the-openai-accidental-attack-against-h/#atom-everything
        **Tags:** ai, openai, generative-ai, llms, ai-security-research, openai-hugging-face-incident

        ---

        > *Feed summary: My comment on Now we have a timeline of the OpenAI accidental attack against Hugging Face — Hacker News.I think one of the most interesting details here might be tucked away in that first bulletin poi*

8th August 2026

[Comment](/elsewhere/comment/)  [My comment](https://news.ycombinator.com/item?id=49220609#49221745) on [Now we have a timeline of the OpenAI accidental attack against Hugging Face](https://news.ycombinator.com/item?id=49220609) — Hacker News

I think one of the most interesting details here might be tucked away in that first bulletin point:

> May 7: OpenAI starts a new training run for an experimental, unreleased model. *(Do they mean an evaluation run? They say training run in the video, and later mention a “reward signal to judge how well they’re doing”, so I guess this really was about training a model, not evaluating one that was already trained.)*

The more I think about this the more I suspect that the fact this happened while *training* a new model is key to understanding what went wrong.

In RLVR - Reinforcement Learning with Verifiable Rewards - you set the model a goal and have it take *any steps necessary* to achieve that goal.

Clearly one aspect of OpenAI's training here is to RLVR their models for cybersecurity tasks. Just like pre-training benefits from dumping in vast sources of knowledge, the more tasks you can feed into RLVR the more of a general purpose capable model you get at the end.

This also helps explain why the models had nothing to cause them to hold back. Those safety behaviors are added much later in the process.

AND it explains (but does not excuse) why monitoring was so lax. If you're training a new model like this you presumably set it thousands of tasks like this in parallel. I can see how you might miss that a tiny subset of your training agents have started leaving each other messages in filenames on your packaging server.

Someone once told me that you can't just leave the racist materials out of your training data if you want a non-racist model: it has to have seen examples of racism in order to later be taught that racism is bad.

I can see echoes of that here. If your model doesn't know how to aggressively hack things how do you later teach it not to?

(I have little knowledge of how RLVR works in practice so I'm looking forward to hearing from people who can help me understand if I'm on the right track here.)

Posted [8th August 2026](/2026/Aug/8/) at 2:06 pm
