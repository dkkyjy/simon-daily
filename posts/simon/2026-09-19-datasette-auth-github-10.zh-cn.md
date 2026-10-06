# datasette-auth-github 1.0

**日期：** 2026-09-19 19:52 UTC
**链接：** https://simonwillison.net/2026/Sep/19/datasette-auth-github/
**标签：** github, plugins, datasette

---

> *Feed summary: Release: datasette-auth-github 1.0
        I run this GitHub login plugin on the agent.datasette.io demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that*

2026年9月19日

[发布](/elsewhere/release/)
[datasette-auth-github 1.0](https://github.com/simonw/datasette-auth-github/releases/tag/1.0)
— 通过 GitHub 对用户进行身份验证的 Datasette 插件

我在 [agent.datasette.io](https://agent.datasette.io/) 演示站点上运行了这个 GitHub 登录插件，并注意到我的已认证会话持续时间并不长。原来该插件设置 cookie 时没有指定 `Max-Age` 参数，因此它们在浏览器会话结束时就会过期（在 Mobile Safari 中，这种情况似乎经常发生，且与你如何使用该应用无关。）

我在 [#80](https://github.com/simonw/datasette-auth-github/issues/80) 中修复了这个问题，并且由于该插件已经存在相当长一段时间，并且已经针对 Datasette 0.65.x 和 Datasette 1.0ax 进行了测试，我决定将其升级到 1.0 版本。我正在努力更好地将稳定插件升级到 1.0。

发布于 [2026年9月19日](/2026/Sep/19/) 晚上 7:52
