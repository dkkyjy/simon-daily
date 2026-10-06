# Datasette 1.0a39 and 0.65.4 security releases

        **Date:** 2026-09-11 03:27 UTC
        **Link:** https://simonwillison.net/2026/Sep/11/datasette-security/
        **Tags:** releases, security, ai, datasette, generative-ai, llms, agentic-engineering, ai-security-research

        ---

        > *Feed summary: Datasette 1.0a39 and 0.65.4 security releases
Today we're releasing two new security patch versions of Datasette: 1.0a39 and 0.65.4 - one for the current alpha series and one for the stable 0.65.x fam*

11th September 2026 - Link Blog

**[Datasette 1.0a39 and 0.65.4 security releases](https://datasette.io/blog/2026/september-security-releases/)**. Today we're releasing two new security patch versions of Datasette: [1.0a39](https://docs.datasette.io/en/latest/changelog.html#v1-0-a39) and [0.65.4](https://docs.datasette.io/en/stable/changelog.html#v0-65-4) - one for the current alpha series and one for the stable 0.65.x family.

These are security fixes which you should apply if you are running a Datasette instance on the public web - in particular if that instance mixes both public and private tables.

Following issues reported by [Sevban Dönmez](https://github.com/jankesec), [Alex Garcia](https://alexgarcia.xyz) and I ran an extensive audit of Datasette using Claude Fable 5.1, GPT-5.6, and GPT-6 Astra. We then spent almost a week collaborating on and reviewing the fixes.

They helped find some *very* subtle bugs. We'll be incorporating security audits by frontier models into all of our development work going forward.

Alex came up with a way of splitting the work which I found extremely productive:

> Alex Garcia and I worked together running and then responding to the audit, working in a shared private repository. For most of the issues we split the work: one of us would create the automated tests highlighting the issue, then the other would implement the fix. This ensured that two separate humans had eyes on each of the issues, in addition to our coding agents running different models.

Posted [11th September 2026](/2026/Sep/11/) at 3:27 am
