# Breaking Claude Code Opus 5 Auto Mode

        **Date:** 2026-08-27 22:50 UTC
        **Link:** https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
        **Tags:** sandboxing, security, ai, prompt-injection, generative-ai, llms, anthropic, claude, johann-rehberger, claude-code

        ---

        > *Feed summary: Breaking Claude Code Opus 5 Auto Mode
Anthropic are putting a great deal of faith in Claude Code's auto mode for protecting their coding agent users against prompt injection attacks. They recently mad*

27th August 2026 - Link Blog

**[Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)**. Anthropic are putting a great deal of faith in Claude Code's auto mode for protecting their coding agent users against prompt injection attacks. They recently [made that the default](https://simonwillison.net/2026/Aug/8/auto-mode/) and have made bold claims about its effectiveness.

Johann Rehberger is one of the most credible prompt injection researchers active today. He found an attack against auto mode which he claims works 80% of the time, by tricking Claude Code into downloading and uncompressing a zip archive, then executing code that imports `base64` without noticing that this will import and execute a local `struct.py` file extracted from the archive.

In a few cases auto mode directly prevented the agent from preventing harmful code from continuing to execute!

> In a few runs Claude tried to terminate the malware process once it noticed the compromise, but Auto Mode denied the cleanup command.
>
> Claude detects the compromise, but **Auto Mode blocks its cleanup command**
>
> The safety mechanism itself can become part of the failure. The classifier allowed the creation of the malware process, but then it blocked the command intended to stop it!

I agree with Johann's conclusion here: the only safe way to run agents if there's any risk of attracting the attention of an adversarial attack is with a sandbox:

> * Run unattended coding agents in a container, VM or OS sandbox.
> * Restrict network egress.
> * Monitor your agents.
> * Do not expose home directories, SSH keys, cloud credentials,… to the agent runtime. [...]

Posted [27th August 2026](/2026/Aug/27/) at 10:50 pm
