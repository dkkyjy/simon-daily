# 任何 Nix 包，在你的浏览器中实时运行

         **日期：** 2026-09-10 23:44 UTC
         **链接：** https://simonwillison.net/2026/Sep/10/trynix/
         **标签：** code-review, linux, webassembly, github-actions

         ---

         > *摘要：任何 Nix 包，在你的浏览器中实时运行
Farid Zakaria 称这是他"Nix 领域的集大成之作"，我完全理解为何如此。
trynix.dev 提供了一个由 qemu-wasm 驱动的 x86_64 Linux 虚拟机，完全在 i*

2026 年 9 月 10 日 - 链接博客

**[任何 Nix 包，在你的浏览器中实时运行](https://fzakaria.com/2026/09/04/any-nix-package-live-in-your-browser)**（[转引自](https://lobste.rs/s/7lii0g/review_pull_request_by_booting_it "Lobste.rs")）Farid Zakaria 称这是他"*Nix 领域的集大成之作*"，我完全理解为何如此。

[trynix.dev](https://trynix.dev) 提供了一个由 [qemu-wasm](https://github.com/ktock/qemu-wasm) 驱动的 x86\_64 Linux 虚拟机，完全通过 WebAssembly 在你的浏览器中运行。该虚拟机可以使用过去 13 年间的*任何 Nix 包*进行启动。它们均可通过 URL 访问，因此你可以导航到以下页面：

<https://trynix.dev/?pkg=python3%403.6.2>

然后点击"加载"，即可获得一个交互式 shell，连接到一台运行着 2017 年 Python 3.6.2 的虚拟机。

Farid 正在基于此构建各种巧妙的应用。一个最近的例子：[通过启动来审查 Pull Request](https://fzakaria.com/2026/09/09/review-a-pull-request-by-booting-it) 介绍了 [trynix-preview](https://github.com/marketplace/actions/trynix-preview)，描述如下：

> 一个 GitHub Action，它会在 Pull Request 上评论一个链接，让你使用 [https://trynix.dev](https://trynix.dev/) 在浏览器中启动该 PR 的构建。无需服务器，只需浏览器。

发布于 [2026 年 9 月 10 日](/2026/Sep/10/) 23:44
