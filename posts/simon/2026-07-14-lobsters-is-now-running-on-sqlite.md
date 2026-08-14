# lobste.rs is now running on SQLite

        **Date:** 2026-07-14 19:44 UTC
        **Link:** https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything
        **Tags:** migrations, ops, rails, sqlite, lobsters

        ---

        > *Feed summary: lobste.rs is now running on SQLite
Community site Lobsters has been planning a migration away from MariaDB since August 2018 - originally targeting PostgreSQL, but last year they decided to investigat*

14th July 2026 - Link Blog

**[lobste.rs is now running on SQLite](https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite)**. Community site [Lobsters](https://lobste.rs) has been planning a migration away from MariaDB [since August 2018](https://github.com/lobsters/lobsters/issues/539#issuecomment-4959857588) - originally targeting PostgreSQL, but last year they decided to [investigate SQLite](https://github.com/lobsters/lobsters/issues/539#issuecomment-2964114295) instead.

This weekend they completed the migration, and now consider it stable enough that it looks like this is the permanent architecture for the site going forward:

> SQLite seems to have passed with flying colors: cpu usage is down, memory usage is down, site seems to be snappier at least for me, 1/2 the vps cost once mariadb vps is taken down

The Lobsters Rails application now runs on a single VPS, with a primary content SQLite database file that's around 3.8GB. [There's also](https://lobste.rs/s/ko1ji1/lobste_rs_is_now_running_on_sqlite#c_c9ydhs) a 1.1GB cache database, a 218MB queue database, and a still growing 555MB rack\_attack database used by the [Rack::Attack](https://github.com/rack/rack-attack) middleware for blocking and throttling abusive requests.

There are plenty more details in both the linked thread and this [SQLite migration PR](https://github.com/lobsters/lobsters/pull/1927) by Thomas Dziedzic, which added 735 lines and removed 593 lines across 30 commits and 188 files. That PR built on top of previous PRs [#1705](https://github.com/lobsters/lobsters/pull/1705), [#1871](https://github.com/lobsters/lobsters/pull/1871), and [#1924](https://github.com/lobsters/lobsters/pull/1924).

This is a really useful case study, and a great reminder that you can get a whole lot done with a single server and SQLite in 2026.

Posted [14th July 2026](/2026/Jul/14/) at 7:44 pm
