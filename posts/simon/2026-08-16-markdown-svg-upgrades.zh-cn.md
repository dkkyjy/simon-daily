# Markdown SVG 升级

        **日期：** 2026-08-16 23:59 UTC
        **链接：** https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/
        **标签：** svg, markdown, tools

        ---

        > *Feed 摘要：我于五月开始构建我的 markdown-svg-renderer 工具，但此后我为其添加了足够多的功能，值得在此再次讨论。
它已演变成我分享 Markdown 转*

2026年8月16日

我于[五月](https://tools.simonwillison.net/colophon#markdown-svg-renderer.html)开始构建我的 [markdown-svg-renderer](https://tools.simonwillison.net/markdown-svg-renderer) 工具，但此后我为其添加了足够多的功能，值得在此再次讨论。

它已演变成我分享包含 SVG 文档的 Markdown 转录文本的理想工具。鉴于我[热衷于绘制骑自行车的鹈鹕](https://simonwillison.net/tags/pelican-riding-a-bicycle/)，这是一个我需要解决的问题！

该工具非常简单。在浏览器中导航至 [markdown-svg-renderer](https://tools.simonwillison.net/markdown-svg-renderer)，粘贴一些 Markdown 即可查看渲染效果……或者将该 Markdown 保存到支持 CORS 的 URL 或 GitHub Gist，然后粘贴该文档的 URL。

URL 选项将为您提供一个可添加书签的页面，例如 <https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6f9e48293be5c916652d29f0dc0b0657>——其中嵌入了[此 Gist](https://gist.github.com/simonw/6f9e48293be5c916652d29f0dc0b0657) 的 URL。

如果您访问[该 Gist](https://gist.github.com/simonw/6f9e48293be5c916652d29f0dc0b0657)，您会看到原始 SVG：

在渲染工具中，它[看起来像这样](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2F6f9e48293be5c916652d29f0dc0b0657)：

如您所见，Markdown 中的那个 SVG 块已被转换为渲染后的 SVG（此处为动画），并附带多个选项卡。

这些选项卡才是真正有趣的部分。PNG 和 JPEG 选项卡会在浏览器中将该 SVG 渲染为这些图像格式，并允许您复制或下载它们——这对于在不直接支持 SVG 的平台上分享非常有用。

MP4 选项卡是[今天新增的](https://github.com/simonw/tools/commit/73e0327f6df9887ba2a9f9f16a2d06a45451d248)——它会检查 SVG 是否包含任何动画，尝试猜测循环视频的时长，然后渲染动画的整批帧，并加载 30 多 MB 的 [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm)，以便利用编译为 WebAssembly 并在浏览器中运行的 FFMPEG 的全部功能，将这些帧编译为 MP4 视频。

能够将动画 SVG 转换为 MP4，再次使得在无法原生支持 SVG 动画的平台上分享变得容易。这是一个巧妙的技巧！

发布于 [2026年8月16日](/2026/Aug/16/) 晚上 11:59
