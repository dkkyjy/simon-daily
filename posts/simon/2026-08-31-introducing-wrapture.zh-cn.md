# 介绍 wrapture

        **日期：** 2026-08-31 23:59 UTC
        **链接：** https://simonwillison.net/2026/Aug/31/introducing-wrapture/
        **标签：** graham-dumpleton, monkey-patching, python, testing, pytest, observability, ai-assisted-programming, agentic-engineering, opentelemetry

        ---

        > *提要摘要：介绍 wrapture
Graham Dumpleton（wrapt、mod_wsgi 和 New Relic Python 代理的知名作者）的新作品，他将 Wrapture 描述为将 wrapt 中的 monkeypatching 理念扩展并应用于测试和追踪*

2026年8月31日 - 链接博客

**[介绍 wrapture](https://grahamdumpleton.me/posts/2026/08/introducing-wrapture/)**。Graham Dumpleton（[wrapt](https://pypi.org/project/wrapt/)、mod\_wsgi 和 New Relic Python 代理的知名作者）的新作品，他将 Wrapture 描述为将 wrapt 中的 monkeypatching 理念扩展并同时应用于测试和追踪。

Wrapture（[完整文档在此](https://wrapture.readthedocs.io/)）使得包装任何函数或方法变得容易，从而可以追踪所有访问，或覆盖以返回不同的值。

它既作为 `unittest.mock` 的替代品，也是一种对现有项目实现追踪的方式：

> 对你不控制的代码附加观察，记录流经其中的内容，并且在不干扰被监视程序的情况下做到这一点，这是我从未真正停止思考的问题。

Wrapture 包含 [OpenTelemetry 支持](https://wrapture.readthedocs.io/en/latest/otel-export.html)，甚至有一种完全基于配置的机制来为现有 Python 项目添加追踪，如下所示：

```
capture = "summary"

[[observe]]
target = "domain:Calculator"
name = ["outer", "inner"]

[[sink]]
type = "jsonlines"
path = "trace.jsonl"
```

这仍然是一个非常年轻的项目——只有几周的历史——但它已经有了一个非常有前途的开端。

有趣的是，这也是 Graham 第一次尝试大型且完全由代理驱动的项目：

> wrapture 中的每一行代码和文档都是由 AI 助手在我的指导下编写的。我想坦诚地说明这一点，同样坦诚地说明它不是什么。这不是“氛围编码”，即一次性提示产生一堆生成的代码，而驱动者因为缺乏判断所返回内容的知识而希望一切顺利。氛围编码已经赢得了它的坏名声。我从一开始就仔细地设计了 wrapture。我在 Python 的这个特定领域花了很长时间，确切地知道结果需要是什么，而 AI 是产生它的手段，而不是设计的来源。

在后续文章 [使用 wrapture 进行单元测试](https://grahamdumpleton.me/posts/2026/09/unit-testing-with-wrapture/) 中，Graham 展示了新库支持的测试模式：

```
def test_stub_with_wrapture():
    with wrapture.binding(
        Gateway, "charge"
    ).on_call.returns({
        "id": "stub", "amount": 0}
    ):
        assert OrderService().place(
            500
        )["id"] == "stub"
```

以及这个简洁的示例，展示了一个测试调用然后修改原始方法返回值的例子：

```
def test_pinned_result_with_wrapture():
    charge = wrapture.binding(
        Gateway, "charge"
    )
    charge.on_call.transforms_result(
        lambda r: {**r, "id": "ch_TEST"}
    )
    with charge:
        assert OrderService().place(
           500
        ) == {
            "id": "ch_TEST", "amount": 500
        }
```

（在这两个示例中，`OrderService().place(...)` 方法都调用了 `Gateway().charge(...)`。）

发布于 [2026年8月31日](/2026/Aug/31/) 晚上 11:59
