# 引用 Rick Brewster

        **日期：** 2026-09-02 05:50 UTC
        **链接：** https://simonwillison.net/2026/Sep/2/rick-brewster/
        **标签：** 逆向工程, 编码代理, claude, 生成式AI, ai, llms, dotnet, linux, vibe-coding

        ---

        > *摘要：Direct2D 一直是 Paint.NET 在 WINE 上最大的障碍，而且很明显它永远无法完善到足以满足 Paint.NET 的使用需求。我也不能直接“禁用”Direct2D 的使用。所以，相反，**Paint.NET 现在拥有一个内部的、从零开始的、干净室逆向工程重写的 Direct2D，用于在 WINE 上运行**（通过使用 **/wine** 触发）。它位于 **PaintDotNet.Windows.Direct2D1.Managed.dll** 中。这是由我们的好朋友 [Claude](https://claude.ai/) 编写的，没有他，这根本不可能实现，也永远不会发生。[...]*
>
> *这段代码大部分是所谓的“vibe coding”出来的。我的意思是，它没有被彻底审查过，更像是“相信我，兄弟”的风格。我不可能审查 180,000 行代码，这实在太多了。作为参考，Paint.NET 的其余部分大约有 700,000 行代码，而我已经在上面工作了 20 多年。[...]*
>
> *有时，Claude 以 10 个刚刚挣脱束缚的爱因斯坦级 10 倍编码者的愤怒在工作。而其他时候……嗯，就不那么理想了。我不得不相当多地照看 Claude，以确保它正确地进行资源管理（有一段时间它根本没有对引用计数对象执行 COM 中相当于 AddRef() 的操作，哎呀）。当我发现一些非常糟糕的设计或架构决策时，我不得不敲打它几次。同时，它为了找出实现 Direct2D 内置效果库所需的所有公式而进行的一些相当巧妙且不知疲倦的逆向工程工作，也让我印象深刻。*

— [Rick Brewster](https://forums.paint.net/topic/134563-🍷-extremely-experimental-winelinux-support-how-to-get-started/)，Paint.NET 的作者

发布于 [2026年9月2日](/2026/Sep/2/) 上午 5:50
