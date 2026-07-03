# llm-coding-agent 0.1a0

        **Date:** 2026-07-02 19:33 UTC
        **Link:** https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything
        **Tags:** projects, ai, generative-ai, llm, llm-tool-use, coding-agents, claude-code, claude-mythos-fable

        ---

        Release: llm-coding-agent 0.1a0 Another Fable 5 experiment. Now that my LLM library has evolved into more of an agent framework it's time to see what a simple coding agent would look like built on it. I started a new Python library using my python-lib-template-repository GitHub template repository, then ran these two prompts (here's the Claude Code for web transcript ): Write a spec.md for this project - it will depend on the latest “llm” alpha from PyPI and implement a Claude code style coding agent complete with tools for reading and editing files and executing commands Then: Commit the spec, then build it using red/green TDD in a series of sensible commits (each with passing tests and updated docs) - occasionally manually test it using the OpenAI API key in your environment Here's the spec , the resulting README file , and the sequence of commits . I've shipped a slop-alpha to PyPI, so you can run the new agent like this: uvx --prerelease=allow --with llm-coding-agent llm code It's pretty good for a first attempt! Here's the (Fable-authored) README , which lists recipes like llm code --yolo and llm code --allow "pytest*" --allow "git diff*" . It also presents a Python API based around a CodingAgent(model="gpt-5.5", root="/path", approve=True).run("Fix the failing test in tests/test_parser.py") class which I didn't ask for but I'm delighted to see implemented. Here's the suite of tools it implemented , listed using uvx ... llm tools : CodingTools_edit_file(path: str, old_string: str, new_string: str, replace_all: bool = False) -> str Replace an exact string in a file. old_string must match the file contents exactly (including whitespace) and must identify a unique location unless replace_all is true. Returns a diff of the change so it can be verified. CodingTools_execute_command(command: str, timeout: int = 120) -> str Run a shell

*(truncated, see original)*
