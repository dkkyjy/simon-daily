# Gemini 3.8 TTS 游乐场

**日期：** 2026-09-23 17:12 UTC
**链接：** https://simonwillison.net/2026/Sep/23/gemini-tts-playground/
**标签：** text-to-speech, gemini

---

> *摘要：工具：Gemini 3.8 TTS 游乐场
Google 今天发布了两个新的 Gemini 文本转语音模型 - gemini-3.8-flash-tts 和 gemini-3.8-flash-lite-tts。
它们附带一个包含超过 2,000 种声音的库，*

2026年9月23日

[工具](/elsewhere/tool/)
[Gemini 3.8 TTS 游乐场](https://tools.simonwillison.net/gemini-tts-playground)
— 通过交互式游乐场测试和实验 Google 的 Gemini 3.8 文本转语音 API，您可以在其中编写单声旁白或多说话人对话，预览生成的音频，并探索请求和响应详情。将您的编写设置保存为可书签的 URL 以便于共享，并使用您的 Gemini API 密钥生成高质量的语音合成。

Google 今天[发布了两个新的 Gemini 文本转语音模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) - `gemini-3.8-flash-tts` 和 `gemini-3.8-flash-lite-tts`。

它们附带一个包含超过 2,000 种声音的库，加上使用"仅 30 秒的您自己的声音或您有权使用声音的音频样本"创建自定义声音的能力。

我使用 GPT-6 Astra [即兴编码](https://tools.simonwillison.net/markdown-svg-renderer?url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Fa82f3aef2677c623d1776092d6b21224)了这个自带密钥的游乐场界面，利用了底层 Gemini API 的开放 CORS 策略。

该 API 的一个显著特点是它使得定义多个角色之间的完整对话变得容易，每个角色都有不同的声音和声音风格指令。

这里是一个简短的演示片段，两只鹈鹕在辩论是否应该搬到[太平洋码头](https://simonwillison.net/2026/Sep/12/sighting-399708714/)。我让 Claude 4.5 Opus [编写剧本](https://claude.ai/share/3597fc77-9323-4583-aeb9-b0e4c3f654a3)并生成[一个使用工具渲染它的 URL](https://simonwillison.net/u/vj)。

您的浏览器不支持音频元素。

使用 Gemini 3.8 Flash TTS（不是更便宜的 Flash-Lite）生成 1 分 18 秒的音频耗时约 20 秒，成本为 2.74 美分。

发布于 [2026年9月23日](/2026/Sep/23/) 下午 5:12
