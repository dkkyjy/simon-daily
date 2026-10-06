# Gemini Live audio

        **Date:** 2026-09-15 22:47 UTC
        **Link:** https://simonwillison.net/2026/Sep/15/gemini-live/
        **Tags:** google, tools, websockets, generative-ai, llms, gemini, llm-release, speech-to-text

        ---

        > *Feed summary: Tool: Gemini Live audio
        Google released Gemini 3.8 Live and 3.8 Live Extended Thinking today - two new speech-to-speech models that are a similar shape to OpenAI's GPT-Live family.
I pointed G*

15th September 2026

[Tool](/elsewhere/tool/)
[Gemini Live audio](https://tools.simonwillison.net/gemini-live)

Google released [Gemini 3.8 Live and 3.8 Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) today - two new speech-to-speech models that are a similar shape to OpenAI's [GPT-Live](https://openai.com/index/introducing-gpt-live/) family.

I pointed GPT-6 Astra Extra High at the documentation and [had it build me this web UI](https://gist.github.com/simonw/067b7430c5b1f743af9419b0184c38ef) for trying out the new models. You can select a model and voice preset, enter an optional system prompt and then start a voice conversation through your browser, including the ability to interrupt the model while it is talking.

The [implementation](https://github.com/simonw/tools/blob/main/gemini-live.html) uses no libraries. It connects to the `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=...` WebSocket endpoint and uses a Web Audio API `AudioContext` for both capture and playback.

Here's [the Gemini Live tutorial](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket) for getting started with that WebSockets API.

Posted [15th September 2026](/2026/Sep/15/) at 10:47 pm
