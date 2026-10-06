# commit-rewriter 0.1

        **Date:** 2026-09-14 00:28 UTC
        **Link:** https://simonwillison.net/2026/Sep/14/commit-rewriter/
        **Tags:** git, projects, python, ai-assisted-programming

        ---

        > *Feed summary: Release: commit-rewriter 0.1
        I built this little web app the other day to help edit the commit messages for the Datasette security releases. The initial commits were full of coding agent cruft*

14th September 2026

[Release](/elsewhere/release/)
[commit-rewriter 0.1](https://github.com/simonw/commit-rewriter/releases/tag/0.1)
— Python web app to help rewrite your commit messages

I built this little web app the other day to help edit the commit messages for the [Datasette security releases](https://datasette.io/blog/2026/september-security-releases/). The initial commits were full of coding agent cruft and references to issue IDs from our private repository, so they weren't fit for publication.

If you want to edit the commit messages for a repository you can run it like this:

```
uvx commit-rewriter path/to/repo
```

Omit the path if you are already in the directory for that repo.

When you submit your edits the tool creates a timestamped branch of your current repo state - to allow you to revert if you need to - and then rewrites every commit from the first one you edited to the most recent.

Posted [14th September 2026](/2026/Sep/14/) at 12:28 am
