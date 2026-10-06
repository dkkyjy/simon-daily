# 介绍 ChatGPT Images 2.5

         **日期：** 2026-09-08 22:46 UTC
         **链接：** https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/
         **标签：** tools, ai, openai, generative-ai, uv, text-to-image

         ---

         > *摘要：介绍 ChatGPT Images 2.5
OpenAI 的图像生成模型据称已"在 ChatGPT Images 和 API 中的 GPT‑Image 模型上生成了超过 30 亿张图片"。此次最新版本的改进包括*

2026年9月8日 - 链接博客

**[介绍 ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)**。OpenAI 的图像生成模型据称已"在 ChatGPT Images 和 API 中的 GPT‑Image 模型上生成了超过 30 亿张图片"。此次最新版本提升了模型在多轮对话中的指令遵循能力，响应速度更快，并且"更擅长保留参考照片中的主体"。

API 中新增了两个模型 ID：`gpt-image-2.5-sunburst` 和 `gpt-image-2.5-flare`。根据[这篇文档](https://developers.openai.com/api/docs/guides/image-generation#overview)，我认为 Sunburst 是更强大的选择：

> 在需要精确编辑的工作流程中选择 Sunburst，在需要快速生成高质量日常图像时选择 Flare。

我[升级](https://github.com/simonw/tools/pull/333)了我的 [openai\_image.py](https://tools.simonwillison.net/python/#openai_imagepy) 命令行工具，使其支持传入一张或多张参考图像，所以现在这样就能用了：

```
uv run https://tools.simonwillison.net/python/openai_image.py \
   'add a raccoon scientist studying the chart thoughtfully' \
   -i https://static.simonwillison.net/static/2026/openai-agent-usage.webp \
   -m gpt-image-2.5-sunburst
```

这是[原始图片](https://static.simonwillison.net/static/2026/openai-agent-usage.webp)，以下是我用"添加一只浣熊科学家在认真研究图表"这个提示词得到的结果：

发布于 [2026年9月8日](/2026/Sep/8/)，晚上 10:46
