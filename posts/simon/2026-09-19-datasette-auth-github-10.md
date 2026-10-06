# datasette-auth-github 1.0

        **Date:** 2026-09-19 19:52 UTC
        **Link:** https://simonwillison.net/2026/Sep/19/datasette-auth-github/
        **Tags:** github, plugins, datasette

        ---

        > *Feed summary: Release: datasette-auth-github 1.0
        I run this GitHub login plugin on the agent.datasette.io demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that*

19th September 2026

[Release](/elsewhere/release/)
[datasette-auth-github 1.0](https://github.com/simonw/datasette-auth-github/releases/tag/1.0)
— Datasette plugin that authenticates users against GitHub

I run this GitHub login plugin on the [agent.datasette.io](https://agent.datasette.io/) demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that the plugin was setting cookies without a `Max-Age` parameter, so they were expiring at the end of a browser session (which in Mobile Safari seems to happen pretty often, independently of how you are using the app.)

I fixed that in [#80](https://github.com/simonw/datasette-auth-github/issues/80) and, since this plugin has been around for quite a while and is tested against both Datasette 0.65.x and Datasette 1.0ax, I decided to bump it up to a 1.0 release. I'm trying to get better at promoting stable plugins to 1.0.

Posted [19th September 2026](/2026/Sep/19/) at 7:52 pm
