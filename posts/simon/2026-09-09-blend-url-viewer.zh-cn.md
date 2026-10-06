# .blend URL 查看器

         **日期：** 2026-09-09 23:58 UTC
         **链接：** https://simonwillison.net/2026/Sep/9/blender-viewer/
         **标签：** 3d, javascript, tools, ai, generative-ai, llms, blender, coding-agents, codex, gpt-6-astra

         ---

         > *摘要：工具：.blend URL 查看器
        我正继续用 GPT-6 Astra 和 Blender 玩得非常尽兴（参见我的 TIL 笔记）。
作为一个皇家法贝热复活节彩蛋的忠实粉丝，我一直觉得如果做一些新的彩蛋来*

2026 年 9 月 9 日

[工具](/elsewhere/tool/)
[.blend URL 查看器](https://tools.simonwillison.net/blender-viewer)
— 通过在浏览器中粘贴一个支持跨域访问的文件 URL 或 GitHub 仓库链接，即可直接在浏览器中查看 Blender .blend 文件。该查看器能够渲染 Blender 5.x 文件中的网格几何体、材质、光照以及可选的已保存相机位置，并提供交互式轨道控制、线框模式和模型适配功能。

我正继续用 GPT-6 Astra 和 Blender 玩得非常尽兴（参见[我的 TIL 笔记](https://til.simonwillison.net/llms/blender-coding-agents-macos)）。

作为一个[皇家法贝热复活节彩蛋](https://en.wikipedia.org/wiki/Faberg%C3%A9_egg)的忠实粉丝，我一直觉得做一些全新的彩蛋来致敬流行文化会非常有趣。

昨天我决定试试全新的 [ChatGPT Images 2.5](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/)，[运行了下面这条提示词](https://chatgpt.com/share/6aa1f6d2-a7d8-83ea-92ec-0daeb8422617)：

> `生成一张以电视剧《Pluribus》为主题法贝热彩蛋的照片——先做调研`

它生成了下面这张——说实话，作为第一次尝试已经相当不错了！

然后，纯粹出于好奇，我把那张图片粘贴到了运行 GPT-6 Astra（高）模式的 Codex 中，并输入了以下提示：

> `使用你的 Blender 本地技能来创建这个法贝热彩蛋的 Blender 模型`

（这是[技能文件](https://github.com/simonw/gpt-6-astra-blender-pelican-bicycle/blob/main/outputs/blender-local/SKILL.md)，我是[像这样创建的](https://til.simonwillison.net/llms/blender-coding-agents-macos#creating-a-skill)。）

它持续运行了 17 分 51 秒，为我生成了[多个 `.blend` 文件](https://github.com/simonw/vibe-coded-blender-projects/tree/main/pluribus-faberge-egg/deliverables)。我之前已经有一个氛围编程的 Blender 查看实验项目搁在那里，于是我把这个工具加入了我的[工具集](https://tools.simonwillison.net/)，现在你可以用它来[在浏览器中查看我的 Pluribus Blender 模型](https://tools.simonwillison.net/blender-viewer?url=https%3A%2F%2Fgithub.com%2Fsimonw%2Fvibe-coded-blender-projects%2Fblob%2Fmain%2Fpluribus-faberge-egg%2Fdeliverables%2FPluribus_Jeweled_Egg_v1.blend)：

发布于 [2026 年 9 月 9 日](/2026/Sep/9/) 晚上 11:58
