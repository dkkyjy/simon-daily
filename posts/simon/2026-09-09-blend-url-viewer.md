# .blend URL Viewer

        **Date:** 2026-09-09 23:58 UTC
        **Link:** https://simonwillison.net/2026/Sep/9/blender-viewer/
        **Tags:** 3d, javascript, tools, ai, generative-ai, llms, blender, coding-agents, codex, gpt-6-astra

        ---

        > *Feed summary: Tool: .blend URL Viewer
        I'm continuing to have a lot of fun with GPT-6 Astra and Blender (see my TIL).
As a big fan of the Imperial Fabergé Easter eggs, I've always thought it would be fun to *

9th September 2026

[Tool](/elsewhere/tool/)
[.blend URL Viewer](https://tools.simonwillison.net/blender-viewer)
— View Blender .blend files directly in your browser by pasting a URL to a CORS-accessible file or GitHub repository link. The viewer renders mesh geometry with materials, lighting, and optional saved camera positions from Blender 5.x files, and provides interactive orbit controls, wireframe mode, and model fitting capabilities.

I'm continuing to have a lot of fun with GPT-6 Astra and Blender (see [my TIL](https://til.simonwillison.net/llms/blender-coding-agents-macos)).

As a big fan of the [Imperial Fabergé Easter eggs](https://en.wikipedia.org/wiki/Faberg%C3%A9_egg), I've always thought it would be fun to make some new ones that celebrate popular culture.

Yesterday I decided to try out the new [ChatGPT Images 2.5](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) by [running this prompt](https://chatgpt.com/share/6aa1f6d2-a7d8-83ea-92ec-0daeb8422617):

> `Generate a photo of a faberge egg that's themed after the TV show Pluribus - research first`

It gave me this - honestly not bad for a first attempt!

Then, just to see what would happen, I pasted that image into Codex running GPT-6 Astra (high) and prompted:

> `Use your blender local skill to create a blender model of this faverge egg`

(Here's [the skill file](https://github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/outputs/blender-local/SKILL.md), which I created [like this](https://til.simonwillison.net/llms/blender-coding-agents-macos#creating-a-skill).)

It churned away for 17m51s and built me [several `.blend` files](https://github.com/simonw/vibe-coded-blender-projects/tree/main/pluribus-faberge-egg/deliverables). I already had this vibe-coded Blender viewing experiment lying around, so I added that to my [tools collection](https://tools.simonwillison.net/) and now you can use it to [see my Pluribus blender model in your browser](https://tools.simonwillison.net/blender-viewer?url=https%3A%2F%2Fgithub.com%2Fsimonw%2Fvibe-coded-blender-projects%2Fblob%2Fmain%2Fpluribus-faberge-egg%2Fdeliverables%2FPluribus_Jeweled_Egg_v1.blend):

Posted [9th September 2026](/2026/Sep/9/) at 11:58 pm
