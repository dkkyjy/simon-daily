# sqlite-utils 4.2

        **Date:** 2026-08-13 20:11 UTC
        **Link:** https://simonwillison.net/2026/Aug/13/sqlite-utils/
        **Tags:** releases, sqlite, sqlite-utils

        ---

        > *Feed summary: Release: sqlite-utils 4.2
        Lots of improvements in this one relating to the table.transform() feature, which adds support for complex alter table operations by creating a fresh table, copying a*

13th August 2026

[Release](/elsewhere/release/)
[sqlite-utils 4.2](https://github.com/simonw/sqlite-utils/releases/tag/4.2)
— Python CLI utility and library for manipulating SQLite databases

Lots of improvements in this one relating to the [table.transform() feature](https://sqlite-utils.datasette.io/en/stable/python-api.html#transforming-a-table), which adds support for complex alter table operations by creating a fresh table, copying across the data and then dropping and replacing the old one.

`transform()` now preserves a much larger array of edge-case schema definitions, including check constraints, unique constraints and even comments describing the columns.

There are also [new introspection properties](https://sqlite-utils.datasette.io/en/stable/python-api.html#checks) for check constraints, and a whole lot of other smaller changes.

Includes contributions from [Bunlong Heng](https://github.com/bunlongheng), [ethanhawkes-gif](https://github.com/ethanhawkes-gif), [Rami Abdelrazzaq](https://github.com/RamiNoodle733), [nyxst4ck](https://github.com/nyxst4ck), and [ikatyal2110](https://github.com/ikatyal2110).

(It later turned out 4.2 had [a crashing bug](https://github.com/simonw/sqlite-utils/issues/842), fixed in [4.2.1](https://sqlite-utils.datasette.io/en/stable/changelog.html#v4-2-1).)

Posted [13th August 2026](/2026/Aug/13/) at 8:11 pm
