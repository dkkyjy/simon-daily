# Codex bundles LibreOffice

        **Date:** 2026-09-01 19:03 UTC
        **Link:** https://simonwillison.net/2026/Sep/1/codex-libreoffice/
        **Tags:** codex, generative-ai, openai, ai, llms, openoffice, open-source

        ---

        > *Feed summary: I was poking around in my ~/.cache/ folder using OmniDiskSweeper when I spotted something interesting. The OpenAI Codex desktop app (since rebranded to just ChatGPT) has 1.7GB of stuff in there in a f*

1st September 2026

I was poking around in my `~/.cache/` folder using [OmniDiskSweeper](https://www.omnigroup.com/more) when I spotted something interesting. The OpenAI Codex desktop app (since [rebranded](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app) to just ChatGPT) has 1.7GB of stuff in there in a folder called `codex-primary-runtime`, including a full Python installation, a full Node.js installation, and native binaries for [Poppler](https://poppler.freedesktop.org), git, and the [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice) open source office suite (which forked from OpenOffice.org in 2010):

The `~/.cache/codex-runtimes/codex-primary-runtime/plugins/openai-primary-runtime/plugins/documents` folder includes skills which tell Codex how to find and use those binaries.

Posted [1st September 2026](/2026/Sep/1/) at 7:03 pm
