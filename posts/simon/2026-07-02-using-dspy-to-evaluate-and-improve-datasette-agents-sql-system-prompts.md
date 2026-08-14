# Using DSPy to evaluate and improve Datasette Agent's SQL system prompts

        **Date:** 2026-07-02 18:25 UTC
        **Link:** https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything
        **Tags:** ai, datasette, generative-ai, llms, evals, dspy, datasette-agent, claude-mythos-fable

        ---

        > *Feed summary: Research: Using DSPy to evaluate and improve Datasette Agent's SQL system prompts
        One of this morning's AIE keynotes covered dspy, which reminded me I've been meaning to see if it could help m*

2nd July 2026

[Research](/elsewhere/research/)
[Using DSPy to evaluate and improve Datasette Agent's SQL system prompts](https://github.com/simonw/research/tree/main/dspy-datasette-agent-prompts#readme)
— Leveraging the DSPy framework, this project evaluates and refines the core production system prompts used by Datasette Agent’s read-only SQL question answerer. The methodology involves a harness where DSPy agents invoke Datasette Agent’s actual tool implementations and prompts against a live in-process Datasette, and a gold-standard, auto-generated dataset provides rigorous evaluation via custom metrics.

One of this morning's AIE keynotes covered [dspy](https://github.com/stanfordnlp/dspy), which reminded me I've been meaning to see if it could help me improve the system prompt used by [Datasette Agent](https://agent.datasette.io) - so I fired off an asynchronous research task in Claude Code for web using Claude Fable 5:

> `Pip install the latest Datasette alpha and datasette-agent and dspy - then figure out how to use dspy to evaluate and improve the main system prompts used by Datasette Agent for the feature where it can execute read only SQL queries to answer user questions about data.`

Fable chose to test using GPT 4.1 mini and nano, and identified several promising looking directions for improvements. I particularly like this one:

> The schema listing gives only table names; the "don't call describe\_table if you already have the information" advice caused column-name guessing (page\_count, o.order\_id, first\_name) and error-retry loops in baseline traces. Either include column names in the prompt's schema listing or soften that advice.

Posted [2nd July 2026](/2026/Jul/2/) at 6:25 pm
