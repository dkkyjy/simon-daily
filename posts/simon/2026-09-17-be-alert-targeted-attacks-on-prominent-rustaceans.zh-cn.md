# 警惕：针对知名 Rustacean 的定向攻击

         **日期：** 2026-09-17 23:59 UTC
         **链接：** https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
         **标签：** open-source, security, rust, supply-chain, dependency-cooldowns

         ---

         > *Feed 摘要：警惕：针对知名 Rustacean 的定向攻击
来自 Adam Harvey 和 crates 安全团队的重要警告：

我们相信，目前有一场针对 rust-lang 成员和热门 crate 所有者的持续活动，试图通过入侵他们的设备和账户来发布恶意软件。*

2026年9月17日 - 链接博客

**[警惕：针对知名 Rustacean 的定向攻击](https://blog.rust-lang.org/2026/09/17/targeted-attacks/)**。来自 Adam Harvey 和 crates 安全团队的重要警告：

> 我们相信，目前有一场针对 rust-lang 成员和热门 crate 所有者的持续活动，试图通过入侵他们的设备和账户来发布恶意软件。
>
> 他们会安排一次视频通话，声称是为了某个积极的目的——可能是工作、项目或合同机会——然后利用这次通话作为途径，让目标在电脑上安装某些东西（例如一个据称缺失的音频编解码器），或者执行其他命令（例如，通过把一个命令放到剪贴板上）。

上个月，这个伎俩被用于对 array ref crate 的一次成功的[供应链攻击](https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/)，以及其他攻击。

任何依赖开源的软件（几乎*所有*软件都如此）都有一个由人类组成的网络，他们是潜在的攻击途径——任何对该软件依赖网络中的包有发布权限的人都是如此。

我想我们目前最好的防御手段是[依赖冷却期](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns)——在新包发布后等待几天再升级，希望有人能发现这样的供应链攻击。

发布于[2026年9月17日](/2026/Sep/17/) 23:59
