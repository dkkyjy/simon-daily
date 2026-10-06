# commit-rewriter 0.1

         **日期：** 2026-09-14 00:28 UTC
         **链接：** https://simonwillison.net/2026/Sep/14/commit-rewriter/
         **标签：** git, projects, python, ai-assisted-programming

         ---

         > *摘要：发布：commit-rewriter 0.1
        前几天我搭建了这个小型 Web 应用，用来帮助编辑 Datasette 安全版本发布的提交信息。最初的提交中充斥着编码代理产生的冗余内容*

2026年9月14日

[发布](/elsewhere/release/)
[commit-rewriter 0.1](https://github.com/simonw/commit-rewriter/releases/tag/0.1)
— 一款用于帮助重写提交信息的 Python Web 应用

前几天我搭建了这个小型 Web 应用，用来帮助编辑 [Datasette 安全版本发布](https://datasette.io/blog/2026/september-security-releases/) 的提交信息。最初的提交中充斥着编码代理产生的冗余内容以及我们私有仓库中的 issue 编号引用，因此不适合公开发布。

如果你想编辑某个仓库的提交信息，可以这样运行：

```
uvx commit-rewriter path/to/repo
```

如果你已经在该仓库的目录中，可以省略路径。

当你提交编辑后，该工具会基于你当前的仓库状态创建一个带时间戳的分支——以便在需要时进行回退——然后从你编辑的第一个提交开始，依次重写所有提交直到最新的提交。

发布于 [2026年9月14日](/2026/Sep/14/)，凌晨 12:28
