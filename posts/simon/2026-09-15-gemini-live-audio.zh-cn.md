# Gemini Live 音频

         **日期：** 2026-09-15 22:47 UTC
         **链接：** https://simonwillison.net/2026/Sep/15/gemini-live/
         **标签：** google, tools, websockets, generative-ai, llms, gemini, llm-release, speech-to-text

         ---

         > *摘要：工具：Gemini Live 音频
        Google 于今日发布了 Gemini 3.8 Live 和 3.8 Live 扩展思考——两款全新的语音到语音模型，其形态与 OpenAI 的 GPT-Live 系列相似。
我将 G*

2026年9月15日

[工具](/elsewhere/tool/)
[Gemini Live 音频](https://tools.simonwillison.net/gemini-live)

Google 于今日发布了 [Gemini 3.8 Live 和 3.8 Live 扩展思考](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)——两款全新的语音到语音模型，其形态与 OpenAI 的 [GPT-Live](https://openai.com/index/introducing-gpt-live/) 系列相似。

我将 GPT-6 Astra Extra High 指向了相关文档，[让它为我构建了这款 Web 界面](https://gist.github.com/simonw/067b7430c5b1f743af9419b0184c38ef)，用于试用这些新模型。你可以选择一个模型和语音预设，输入可选的系统提示，然后通过浏览器发起语音对话，其中包括在模型说话时打断它的功能。

[实现代码](https://github.com/simonw/tools/blob/main/gemini-live.html) 未使用任何第三方库。它连接到 `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService.BidiGenerateContent?key=...` WebSocket 端点，并使用 Web Audio API 的 `AudioContext` 同时完成音频采集与播放。

这是 [Gemini Live 教程](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket)，介绍如何使用该 WebSockets API 快速上手。

发布于 [2026年9月15日](/2026/Sep/15/) 晚上 10:47
