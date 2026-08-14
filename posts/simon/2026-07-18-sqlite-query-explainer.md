# SQLite Query Explainer

        **Date:** 2026-07-18 17:19 UTC
        **Link:** https://simonwillison.net/2026/Jul/18/sqlite-query-explainer/#atom-everything
        **Tags:** sql, sqlite, tools, julia-evans, pyodide, claude-mythos-fable

        ---

        > *Feed summary: Tool: SQLite Query Explainer
        Julia Evan's, in Learning a few things about running SQLite:

Maybe one day I’ll learn to read a query plan.

Big same.... which inspired me to have Fable build th*

18th July 2026

[Tool](/elsewhere/tool/)
[SQLite Query Explainer](https://tools.simonwillison.net/sqlite-query-explainer)
— Run SQL queries against a SQLite database in your browser and see exactly how SQLite executes them: the tool runs your query, then annotates every line of both `EXPLAIN QUERY PLAN` and the low-level `EXPLAIN` bytecode output with plain-English descriptions of what the query planner and virtual machine are doing.

Julia Evan's, in [Learning a few things about running SQLite](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/):

> Maybe one day I’ll learn to read a query plan.

Big same.... which inspired me to [have Fable build](https://github.com/simonw/tools/pull/299#issue-4919268017) this interactive explain tool, which runs SQLite in Python in Pyodide in Web Assembly in the browser and adds a layer of explanation to the results of both EXPLAIN and EXPLAIN QUERY PLAN.

Approach with caution, since I don't know enough about SQLite query plans to verify the results myself, but it seems cromulent enough to me.

Posted [18th July 2026](/2026/Jul/18/) at 5:19 pm
