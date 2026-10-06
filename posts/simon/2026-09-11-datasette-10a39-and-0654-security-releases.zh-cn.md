# Datasette 1.0a39 与 0.65.4 安全补丁发布

         **日期：** 2026-09-11 03:27 UTC
         **链接：** https://simonwillison.net/2026/Sep/11/datasette-security/
         **标签：** releases, security, ai, datasette, generative-ai, llms, agentic-engineering, ai-security-research

         ---

         > *摘要：Datasette 1.0a39 与 0.65.4 安全补丁发布
今天我们发布了 Datasette 的两个新安全补丁版本：1.0a39 和 0.65.4——一个面向当前的 alpha 系列，一个面向稳定的 0.65.x 系列*

2026年9月11日 - Link 博客

**[Datasette 1.0a39 与 0.65.4 安全补丁发布](https://datasette.io/blog/2026/september-security-releases/)**。今天我们发布了 Datasette 的两个新安全补丁版本：[1.0a39](https://docs.datasette.io/en/latest/changelog.html#v1-0-a39) 和 [0.65.4](https://docs.datasette.io/en/stable/changelog.html#v0-65-4)——一个面向当前的 alpha 系列，一个面向稳定的 0.65.x 系列。

这些是安全修复，如果您在公共网络上运行 Datasette 实例，则应当应用这些修复——尤其是当该实例同时包含公共表与私有表时。

在 [Sevban Dönmez](https://github.com/jankesec)、[Alex Garcia](https://alexgarcia.xyz) 和我报告了相关问题之后，我们使用 Claude Fable 5.1、GPT-5.6 和 GPT-6 Astra 对 Datasette 进行了一次全面审计。随后，我们花了将近一周的时间协作编写并审查修复方案。

他们帮助发现了一些*极其*细微的缺陷。今后，我们将把前沿模型的安全审计纳入所有开发工作中。

Alex 想出了一套分工方式，我觉得效率极高：

> Alex Garcia 和我协作运行审计并响应审计结果，在一个共享的私有仓库中工作。对于大多数问题，我们进行了分工：其中一人编写自动化测试来揭示问题，另一人则实施修复。这确保了每个问题都有两位不同的开发者进行审查，此外还有我们的编码代理运行着不同的模型。

发布于 [2026年9月11日](/2026/Sep/11/) 上午 3:27
