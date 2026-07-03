# llm-coding-agent 0.1a0

        **日期：** 2026-07-02 19:33 UTC
        **链接：** https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything
        **标签：** 项目, 人工智能, 生成式人工智能, 大语言模型, 大语言模型工具使用, 编码代理, Claude代码, Claude神话寓言

        ---

        发布：llm-coding-agent 0.1a0 又一个Fable 5实验。现在我的LLM库已经发展成更像一个代理框架，是时候看看基于它构建的简单编码代理会是什么样子了。我使用我的python-lib-template-repository GitHub模板仓库创建了一个新的Python库，然后运行了这两个提示（这里是Claude Code的网络转录）：为这个项目编写一个spec.md文件——它将依赖于PyPI上最新的“llm”alpha版本，并实现一个Claude代码风格的编码代理，包含用于读取和编辑文件以及执行命令的工具。然后：提交spec，使用红绿测试驱动开发在一系列合理的提交中构建它（每个提交都有通过的测试和更新的文档）——偶尔使用环境中的OpenAI API密钥手动测试它。以下是spec、生成的README文件以及提交序列。我已经向PyPI发布了一个slop-alpha版本，因此您可以像这样运行新的代理：uvx --prerelease=allow --with llm-coding-agent llm code 作为首次尝试，这相当不错！以下是（Fable编写的）README，其中列出了诸如llm code --yolo和llm code --allow "pytest*" --allow "git diff*"之类的配方。它还展示了一个基于CodingAgent(model="gpt-5.5", root="/path", approve=True).run("修复tests/test_parser.py中失败的测试")类的Python API，我并没有要求这个，但我很高兴看到它被实现了。以下是它实现的工具集，使用uvx ... llm tools列出：CodingTools_edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -> str 替换文件中的精确字符串。old_string必须与文件内容完全匹配（包括空格），并且除非replace_all为true，否则必须标识唯一位置。返回更改的差异以便验证。CodingTools_execute_command(command: str, timeout: int = 120) -> str 运行一个shell

*(截断，见原文)*
