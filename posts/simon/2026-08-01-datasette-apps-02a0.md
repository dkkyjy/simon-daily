# datasette-apps 0.2a0

        **Date:** 2026-08-01 21:23 UTC
        **Link:** https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything
        **Tags:** iframes, datasette, datasette-apps

        ---

        > *Feed summary: Release: datasette-apps 0.2a0

Changes that improve Datasette Apps when created and edited using Datasette Agent:

New app_debug() tool allowing agent to open an app (invisibly) and test it us*

1st August 2026

[Release](/elsewhere/release/)
[datasette-apps 0.2a0](https://github.com/datasette/datasette-apps/releases/tag/0.2a0)
— Apps that live inside Datasette

> Changes that improve Datasette Apps when created and edited using [Datasette Agent](https://agent.datasette.io/):
>
> * New `app_debug()` tool allowing agent to open an app (invisibly) and test it using JavaScript. [#33](https://github.com/datasette/datasette-apps/pull/33)
> * New `app_list()` tool for listing apps the user has permission to edit, so the agent can edit them. [#36](https://github.com/datasette/datasette-apps/issues/36)

The `app_debug()` tool is pretty neat: it works by displaying the app in a `opacity: 0` iframe with `pointer-events: none` (so it can't be seen or interacted with) and then executing agent-provided JavaScript inside that sandboxed iframe. This means the agent can smoke test that the app is working and even do things like measure the dimensions of different elements.

This uses the new `context.browser_task()` mechanism added in [datasette-agent 0.4a0](https://simonwillison.net/2026/Jul/31/datasette-agent/).

Posted [1st August 2026](/2026/Aug/1/) at 9:23 pm
