# Using Blender with coding agents on macOS

        **Date:** 2026-09-05 15:51 UTC
        **Link:** https://simonwillison.net/2026/Sep/5/blender-coding-agents-macos/
        **Tags:** ai, generative-ai, llms, blender, pelican-riding-a-bicycle, coding-agents, gpt-6-astra

        ---

        > *Feed summary: TIL: Using Blender with coding agents on macOS
        I've been having fun with Blender in ChatGPT Codex on my Mac recently. Getting it to work with coding agents is really easy: install the full Mac*

5th September 2026

[TIL](/elsewhere/til/)
[Using Blender with coding agents on macOS](https://til.simonwillison.net/llms/blender-coding-agents-macos)
— Modern frontier models have got \*really good\* at using Blender. I've been having a lot of fun trying this out recently - models can produce `.blend` files you can edit in Blender itself, and can also render images and even movies (by rendering a sequence of images and combining them with `ffmpeg`).

I've been having fun with Blender in ChatGPT Codex on my Mac recently. Getting it to work with coding agents is really easy: install the full Mac application from [blender.org](https://www.blender.org) and run a prompt like this:

> `Use the already install /Applications/Blender to render a scene of a pelican riding a bicycle`

In this case I followed that up with these two prompts:

> `OK add a background and a lot of flair`

Then:

> `OK make it a whole lot better`

And got this image, generated [using Blender's Python API](https://github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/work/pelican_final.py):

Posted [5th September 2026](/2026/Sep/5/) at 3:51 pm
