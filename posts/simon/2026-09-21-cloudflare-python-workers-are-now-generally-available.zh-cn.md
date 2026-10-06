# Cloudflare Python Workers 现已正式发布

         **日期：** 2026-09-21 22:25 UTC
         **链接：** https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/
         **标签：** python, cloudflare, webassembly, pyodide

         ---

         > *摘要：Cloudflare Python Workers 现已正式发布
经过两年的预览期，Cloudflare 在其服务器端 Workers 平台上运行 Python 代码的支持现已稳定： "Python 现在是 Cloudflare 开发者平台上一流的、完全支持的语言"。*

2026年9月21日 - Link Blog

**[Cloudflare Python Workers 现已正式发布](https://blog.cloudflare.com/python-workers-ga/)** ([来源](https://news.ycombinator.com/item?id=49787142 "Hacker News")) 经过两年的预览期，Cloudflare 在其服务器端 Workers 平台上运行 Python 代码的支持现已稳定："Python 现在是 Cloudflare 开发者平台上一流的、完全支持的语言"。

这里有一个有趣的地方，就是它的工作原理。Cloudflare 通过 Pyodide 将编译为 WebAssembly 的 Python 运行在其基于 V8 的 [workerd](https://github.com/cloudflare/workerd) 运行时中。

这带来了一些限制，[在此处有记录](https://developers.cloudflare.com/workers/languages/python/stdlib/) - 最值得注意的是，`multiprocessing` 和 `threading` 在 WebAssembly VM 中都无法工作。

一个特别有趣的细节是本地开发环境的故事 - 他们的 [pywrangler](https://developers.cloudflare.com/workers/languages/python/#the-pywrangler-cli-tool) 开发工具（令人困惑地在 PyPI 上打包为 [workers-py](https://pypi.org/project/workers-py/)）运行其堆栈的完整本地模拟，包括在 V8 中的 WebAssembly 中使用 Pyodide 执行代码，在一个 123MB 的 `workerd` 二进制文件中，对我来说最终位于 `node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd`。

Python Workers 代表了 Cloudflare 对更广泛 Python 生态系统的重大投资。发布公告归功于 Gyeongjae Choi、Dominik Picheta 和 Hood Chatham - Gyeongjae 和 Hood 都是 Pyodide 的核心维护者。

发布于 [2026年9月21日](/2026/Sep/21/) 晚上 10:25
