# 别忽视 wrapture

         **日期：** 2026-09-11 13:51 UTC
         **链接：** https://simonwillison.net/2026/Sep/11/wrapture/
         **标签：** graham-dumpleton, open-source, testing, python, observability, monkey-patching

         ---

         > *摘要：Graham Dumpleton 推出的猴子补丁新包 wrapture 正在成为 Python 开发者不可或缺的工具。我不明白为什么它的热度这么低！
Graham 一直在发布新的*

2026 年 9 月 11 日

Graham Dumpleton 推出的猴子补丁新包 [wrapture](https://wrapture.readthedocs.io/) 正在成为 Python 开发者不可或缺的工具。我不明白为什么它的热度这么低！

自 8 月 31 日 [首次发布](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) 以来，Graham 几乎每天都在发布新的教程。以下是他迄今发布的全部内容：

* [介绍 wrapture](https://grahamdumpleton.me/posts/2026/08/introducing-wrapture/) —— 一个同时服务于测试和可观测性（类似 New Relic 风格的追踪）的全新猴子补丁库。
* [使用 wrapture 进行单元测试](https://grahamdumpleton.me/posts/2026/09/unit-testing-with-wrapture/) —— 如何用它实现与 `unittest.mock` 类似的功能。
* [使用 wrapture 记录调用](https://grahamdumpleton.me/posts/2026/09/recording-calls-with-wrapture/) —— 将方法调用记录为时间线，并以树形结构进行处理和展示。
* [wrapture 中的分阶段行为](https://grahamdumpleton.me/posts/2026/09/phased-behaviour-in-wrapture/) —— 让被补丁的方法在多次调用中逐步改变行为。
* [wrapture 中的可调用对象之外](https://grahamdumpleton.me/posts/2026/09/beyond-callables-in-wrapture/) —— 对属性、字典、生成器进行猴子补丁。
* [使用 wrapture 进行实时追踪](https://grahamdumpleton.me/posts/2026/09/live-tracing-with-wrapture/) —— 对运行中的应用进行追踪，精确了解其工作方式。
* [使用 wrapture 进行零代码追踪](https://grahamdumpleton.me/posts/2026/09/zero-code-tracing-with-wrapture/) —— 在独立的 TOML 文件中配置追踪，完全无需修改 Python 代码。
* [使用 wrapture 追踪 Flask](https://grahamdumpleton.me/posts/2026/09/tracing-flask-with-wrapture/) —— 使用独立的 [wrapture-instrumenation](https://github.com/GrahamDumpleton/wrapture-instrumentation) 包对 Flask 应用进行插桩。该包还为 `aiohttp.client`、`aiohttp.web`、`django`、`fastapi`、`flask`、`grpc`、`http.client`、`httpx`、`jinja2`、`requests`、`sqlalchemy`、`sqlite3`、`starlette`、`urllib.request`、`urllib3`、`uvicorn`、`werkzeug.serving`、`wsgiref.simple_server`、`xmlrpc.client`、`xmlrpc.server` 提供了插桩支持。
* [使用 wrapture 查找慢代码](https://grahamdumpleton.me/posts/2026/09/finding-slow-code-with-wrapture/) —— wrapture 用于记录计时信息的工具，既支持单独记录，也支持跨多次调用进行聚合。
* [wrapture 中的 OpenTelemetry 导出](https://grahamdumpleton.me/posts/2026/09/opentelemetry-export-in-wrapture/) —— 将追踪数据导出至 OpenTelemetry。

Graham 还有一组 [交互式工作坊](https://github.com/GrahamDumpleton/wrapture-workshops) 用于 wrapture，以 JupyterLab 笔记本的形式实现。

Wrapture 目前仍是 Alpha 版软件，但已经非常实用了——尤其是你可以仅通过一个 TOML 文件来配置和试用，完全无需修改任何 Python 代码。

它给人的感觉就像是一把瑞士军刀，一旦掌握，就能在未来多年里应对各种各样的问题。

发布于 [2026 年 9 月 11 日](/2026/Sep/11/) 下午 1:51
