# sqlite-utils 4.1

        **Date:** 2026-07-11 23:50 UTC
        **Link:** https://simonwillison.net/2026/Jul/11/sqlite-utils/#atom-everything
        **Tags:** projects, python, sqlite, sqlite-utils, annotated-release-notes, ai-assisted-programming

        ---

        Release: sqlite-utils 4.1 The first dot-release since 4.0 a few days ago , introducing a number of minor new features. sqlite-utils insert and sqlite-utils upsert now accept a --code option for providing a block of Python code (or a path to a .py file) that defines a rows() function or rows iterable of rows to insert, as an alternative to importing from a file. ( #684 ) sqlite-utils already had features that allow you to pass blocks of Python code as CLI arguments, for example this one for the sqlite-utils convert command: sqlite - utils convert content . db articles headline ' def convert ( value ): return value . upper ()' Allowing blocks of code to generate new rows directly was on obvious extension of that pattern: sqlite - utils insert data . db creatures - - code ' def rows (): yield { "id" : 1 , "name" : "Cleo" } yield { "id" : 2 , "name" : "Suna" } ' - - pk id sqlite-utils insert and sqlite-utils upsert now accept --type column-name type to override the type automatically chosen when the table is created . This is useful for CSV or TSV columns such as ZIP codes that look like integers but should be stored as TEXT to preserve leading zeros. ( #131 ) A long-standing feature request which turned out to be a simple implementation . New table.drop_index(name) method and sqlite-utils drop-index command for dropping an index by name. Both accept ignore=True / --ignore to ignore a missing index. ( #626 ) sqlite-utils query can now read the SQL query from standard input by passing - in place of the query, for example echo "select * from dogs" | sqlite-utils query dogs.db - . ( #765 ) Two more small features. I had Codex

*(truncated, see original)*
