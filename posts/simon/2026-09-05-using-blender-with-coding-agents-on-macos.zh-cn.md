# 在 macOS 上使用编码代理运行 Blender

         **日期：** 2026-09-05 15:51 UTC
         **链接：** https://simonwillison.net/2026/Sep/5/blender-coding-agents-macos/
         **标签：** ai, generative-ai, llms, blender, pelican-riding-a-bicycle, coding-agents, gpt-6-astra

         ---

         > *摘要：TIL：在 macOS 上使用编码代理运行 Blender
        我最近一直在 Mac 上用 ChatGPT Codex 玩 Blender，乐在其中。让它与编码代理配合使用真的非常简单：安装完整的 Mac*

2026 年 9 月 5 日

[今日所学](/elsewhere/til/)
[在 macOS 上使用编码代理运行 Blender](https://til.simonwillison.net/llms/blender-coding-agents-macos)
— 现代前沿模型在使用 Blender 方面已经变得*非常出色*。我最近一直在尝试这个，玩得很开心——模型可以生成 `.blend` 文件，你可以直接在 Blender 中编辑，还可以渲染图像，甚至制作电影（通过渲染一系列图像并用 `ffmpeg` 将它们合并）。

我最近一直在 Mac 上用 ChatGPT Codex 玩 Blender，乐在其中。让它与编码代理配合使用真的非常简单：从 [blender.org](https://www.blender.org) 安装完整的 Mac 版应用，然后运行如下提示词：

> `使用已安装的 /Applications/Blender 渲染一个鹈鹕骑自行车的场景`

在这个案例中，我接着又发了这两条提示词：

> `好的，添加一个背景和大量装饰效果`

然后：

> `好的，让它好上非常多`

最终得到了这张图片，它是[使用 Blender 的 Python API](https://github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/work/pelican_final.py)生成的：

发布于 [2026 年 9 月 5 日](/2026/Sep/5/) 下午 3:51
