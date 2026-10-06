# Gemini 3.8 TTS Playground

        **Date:** 2026-09-23 17:12 UTC
        **Link:** https://simonwillison.net/2026/Sep/23/gemini-tts-playground/
        **Tags:** text-to-speech, gemini

        ---

        > *Feed summary: Tool: Gemini 3.8 TTS Playground
        Google released two new Gemini text-to-speech models today - gemini-3.8-flash-tts and gemini-3.8-flash-lite-tts.
They come with a library of over 2,000 voices, *

23rd September 2026

[Tool](/elsewhere/tool/)
[Gemini 3.8 TTS Playground](https://tools.simonwillison.net/gemini-tts-playground)
— Test and experiment with Google's Gemini 3.8 text-to-speech API through an interactive playground where you can compose single-voice narration or multi-speaker conversations, preview the generated audio, and explore request and response details. Save your compose settings to bookmarkable URLs for easy sharing, and generate high-quality speech synthesis powered by your Gemini API key.

Google [released two new Gemini text-to-speech models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) today - `gemini-3.8-flash-tts` and `gemini-3.8-flash-lite-tts`.

They come with a library of over 2,000 voices, plus the ability to create a custom voice with "just a 30-second audio sample of your voice or a voice you have the rights to use".

I [vibe coded](https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fa82f3aef2677c623d1776092d6b21224) this bring-your-own-key playground interface with GPT-6 Astra, taking advantage of the open CORS policy of the underlying Gemini API.

A notable feature of the API is that it makes it easy to define a full conversation between multiple characters, each with different voices and voice style instructions.

Here's a short demo clip of a conversation between two pelicans debating if they should move to [the Pacifica Pier](https://simonwillison.net/2026/Sep/12/sighting-399708714/). I had Claude 4.5 Opus [write the script](https://claude.ai/share/3597fc77-9323-4583-aeb9-b0e4c3f654a3) and generate [a URL to render it using the tool](https://simonwillison.net/u/vj).

Your browser does not support the audio element.

It took ~20 seconds to generate 1m 18s of audio using Gemini 3.8 Flash TTS (not the cheaper Flash-Lite), at a cost of 2.74 cents.

Posted [23rd September 2026](/2026/Sep/23/) at 5:12 pm
