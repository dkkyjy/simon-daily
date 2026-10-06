# smevals - a small eval suite for evaluating models, prompts, and harnesses

        **Date:** 2026-07-31 21:15 UTC
        **Link:** https://simonwillison.net/2026/Jul/31/smevals/#atom-everything
        **Tags:** projects, ai, generative-ai, llms, llm, evals, jesse-vincent

        ---

        smevals - a small eval suite for evaluating models, prompts, and harnesses I've been working with Jesse Vincent's Prime Radiant applied AI research lab building out this evals framework to help answer questions about the capabilities of different models. The result is smevals , a new tool for running small eval suites across different model configurations and grading the results. The blog entry describes the tool in detail. Here's the 10 second version: Tell your coding agent to run uvx smevals docs to learn the tool (this outputs the README ) Then tell it to build you an eval suite Once you've created an eval - which takes the form of a directory with some YAML files - you can run it against models like this: uvx smevals run path-to-eval/ -m gpt-5.5 -m claude-opus-4.6 Runs are treated separately from grading operations - you can grade your runs (against your defined set of checks) using: uvx smevals grade path-to-eval/ Then you can run a localhost web server to explore the results: uvx smevals serve path-to-eval/ Or run the smevals build command to build that report as static HTML, which you can then host anywhere. Here's an example showing an eval suite I built to evaluate how well models can write haikus. The most time-consuming part of this project was figuring out the vocabulary for it! Here's what I settled on, quoted from the announcement: An eval is a collection of challenges designed to answer a question about a model, for example, how good is that model at generating SVGs? Each eval is a collection of tasks . A task is a specific challenge, for example "Generate an SVG of a pelican riding a bicycle". When you run the eval you do so against one or more configs . Each config specifies

*(truncated, see original)*
