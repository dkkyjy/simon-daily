# EVE Online: The Move to Python 3 Begins!

        **Date:** 2026-08-25 22:59 UTC
        **Link:** https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/
        **Tags:** eve-online, migrations, python, python3, stackless

        ---

        > *Feed summary: EVE Online: The Move to Python 3 Begins!
EVE Online has been one of the most interesting case studies in Python at scale for over twenty years now.
They've been running on Stackless Python since their*

25th August 2026 - Link Blog

**[EVE Online: The Move to Python 3 Begins!](https://www.eveonline.com/news/view/the-move-to-python-3-begins)** ([via](https://lobste.rs/s/e1oalq/move_python_3_begins "Lobster.rs")) EVE Online has been one of the most interesting case studies in Python at scale for over twenty years now.

They've been running on [Stackless Python](https://github.com/stackless-dev/stackless/wiki/) since their launch in 2003, and their last major upgrade was 16 years ago, to Stackless Python 2.7 [in 2010](https://www.eveonline.com/news/view/stackless-python-2.7).

Their upgrade to Python 3 will start using the [futurize](https://python-future.org/futurize.html) script against 2.4 million lines of code, followed by careful manual review of the ~20,000 places where Python 2 and 3 behavior differ - for example `1 / 2` is `0` in Python 2 but is `0.5` in Python 3.

There's nothing in this announcement about how they plan to replace Stackless, but at their conference last year they presented [Scheduling in Carbon: Leaving Stackless Python Behind](https://youtu.be/-x299qHLQs0) describing how they replaced Stackless in the Carbon engine for their more recent game EVE Frontier, using their (now open source) [carbonengine/scheduler](https://github.com/carbonengine/scheduler) library.

Posted [25th August 2026](/2026/Aug/25/) at 10:59 pm
