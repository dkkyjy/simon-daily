# Are AI labs pelicanmaxxing?

        **Date:** 2026-07-22 23:01 UTC
        **Link:** https://simonwillison.net/2026/Jul/22/are-ai-labs-pelicanmaxxing/#atom-everything
        **Tags:** ai, generative-ai, llms, evals, pelican-riding-a-bicycle

        ---

        > *Feed summary: Are AI labs pelicanmaxxing?
Excellent piece of work by Dylan Castillo, who took a deep-dive into the frequently pondered question of whether the AI labs have been deliberately training models to draw *

22nd July 2026 - Link Blog

**[Are AI labs pelicanmaxxing?](https://dylancastillo.co/posts/pelicanmaxxing.html)** ([via](https://news.ycombinator.com/item?id=49010129 "Hacker News")) Excellent piece of work by Dylan Castillo, who took a deep-dive into the frequently pondered question of whether the AI labs have been deliberately training models to draw pelicans riding bicycles in response to my [deeply unscientific benchmark](https://simonwillison.net/tags/pelican-riding-a-bicycle/).

I've been randomly spot-checking this in the past by testing models against other animals riding other types of vehicle, but never with anything close to the diligence of Dylan's methodology here.

Dylan took 8 animals × 6 vehicles = 48 prompts and ran them three times each through 7 different models ( GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.5 Flash, Grok 4.5, Qwen3.7-Max, GLM-5.2, and DeepSeek V4 Pro). He then used GPT-5.6 Luna and Gemini 3.1 Flash-Lite to help evaluate the results.

There's a neat filter view for exploring the results:

For the models he tested he could find no evidence of pelimaxxing:

> * [The pelicans on bicycles don’t look any better](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-1-the-pelicans-on-bicycles-dont-look-any-better)
> * [Labs are not better at drawing pelicans](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-2-labs-are-not-better-at-drawing-pelicans)
> * [Labs are not better at drawing bicycles](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-3-labs-are-not-better-at-drawing-bicycles)
> * [Labs are not better at drawing pelicans on bicycles, even adjusting for difficulty](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-4-labs-are-not-better-at-drawing-pelicans-on-bicycles-even-adjusting-for-difficulty)
> * [The pelican-bicycle scenes don’t look memorized](https://dylancastillo.co/posts/pelicanmaxxing.html#evidence-5-the-pelican-bicycle-scenes-dont-look-memorized) [...]
>
> Pelicans aren’t drawn any better than other animals. Bicycles aren’t drawn any better than other vehicles. And no lab draws the combination better than its pelicans and bicycles already predict. GLM-5.2 comes closest: it has the largest boost on the exact pelican-bicycle cell, and and its first pelican-on-bicycle sample caught my eye. But the effect is small and not significant, so I wouldn’t put too much weight on it.

Posted [22nd July 2026](/2026/Jul/22/) at 11:01 pm
