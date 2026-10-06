# sqlite-utils 4.0rc2, mostly written by Claude Fable (for about $149.25)

        **Date:** 2026-07-05 01:00 UTC
        **Link:** https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/#atom-everything
        **Tags:** projects, sqlite, sqlite-utils, annotated-release-notes, anthropic, claude, coding-agents, claude-code, agentic-engineering, gpt, claude-mythos-fable

        ---

        I wrote about the sqlite-utils 4.0rc1 release a couple of weeks ago. Since we only have Claude Fable on our Max subscriptions for a few more days, I decided to see if it could help me get to a 4.0 stable release that I felt truly comfortable about, since I try to keep to SemVer and like my incompatible major versions to be as rare as possible. I started with this prompt, in Claude Code for web on my iPhone: Final review before shipping a stable 4.0 release - very important to spot any last minute things that would be a breaking change if we fix them later Here's that initial report it created for me. There were some significant problems that I hadn't myself encountered yet - 5 that Fable categorized as "release blockers". Here's the worst of the bunch: 1. delete_where() never commits and poisons the connection (data loss) Table.delete_where() ( sqlite_utils/db.py:2948 ) runs its DELETE via a bare self.db.execute() with no atomic() wrapper — compare Table.delete() at db.py:2944 , which wraps correctly. The connection is left in_transaction=True , so every subsequent atomic() call takes the savepoint branch ( db.py:430-440 ) and never commits either. Reproduced end-to-end: db = sqlite_utils . Database ( "dw.db" ) db [ "t" ]. insert_all ([{ "id" : i } for i in range ( 3 )], pk = "id" ) db [ "t" ]. delete_where ( "id = ?" , [ 0 ]) # conn.in_transaction is now True db [ "t" ]. insert ({ "id" : 50 }) db [ "u" ]. insert ({ "a" : 1 }) db . close () # Reopen: rows are [0, 1, 2] — the delete, row 50, AND table u are all gone. That's a really bad bug! Very glad I didn't ship that, although

*(truncated, see original)*
