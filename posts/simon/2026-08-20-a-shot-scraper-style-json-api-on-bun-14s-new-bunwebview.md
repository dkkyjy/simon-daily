# A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView

        **Date:** 2026-08-20 15:37 UTC
        **Link:** https://simonwillison.net/2026/Aug/20/bun-webview-json-api/
        **Tags:** browsers, javascript, ai, rust, typescript, generative-ai, llms, coding-agents, bun

        ---

        > *Feed summary: Research: A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView
        Today saw the long awaited release of Bun 1.4, the first stable version since the infamous Rust rewrite a few months ago.
I*

20th August 2026

[Research](/elsewhere/research/)
[A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView](https://github.com/simonw/research/tree/main/bun-webview-json-api#readme)
— A zero-dependency, roughly 150-line TypeScript service demonstrates that Bun 1.4’s experimental `Bun.WebView` can provide a shot-scraper-style JSON API for JavaScript evaluation and PNG/JPEG/WebP screenshots without Puppeteer or Playwright. It creates one browser tab per request, supporting concurrency while returning page results and errors as JSON through `/javascript`, `/screenshot`, and `/healthz`.

Today saw the long awaited [release of Bun 1.4](https://bun.com/blog/bun-v1.4), the first stable version since the infamous Rust rewrite [a few months ago](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/).

Interestingly, the Rust rewrite was downplayed in the release notes, which introduced a bewildering array of new features and claimed 2,900 additional bug fixes:

> Bun 1.4 adds +1,517 tests from the Node.js test suite - our biggest jump in Node.js compatibility since Bun 1.0. Bun v1.4 also fixes over 2,900 issues. It reduces idle CPU usage by 5x, reduces memory usage by up to 35%, and starts 50% faster on Linux. It adds [`Bun.Image`](https://bun.com/blog/bun-v1.4#bun-image), [`Bun.WebView`](https://bun.com/blog/bun-v1.4#bun-webview), [`Bun.markdown`](https://bun.com/blog/bun-v1.4#bun-markdown), [`Bun.cron()`](https://bun.com/blog/bun-v1.4#bun-cron), [`Bun.Terminal`](https://bun.com/blog/bun-v1.4#bun-terminal), [`bun run --parallel`](https://bun.com/blog/bun-v1.4#bun-run-parallel), [`bun test --parallel`](https://bun.com/blog/bun-v1.4#bun-test-parallel), [`bun audit fix`](https://bun.com/blog/bun-v1.4#bun-audit-fix), [`bun dedupe`](https://bun.com/blog/bun-v1.4#bun-dedupe), and [`bun prune`](https://bun.com/blog/bun-v1.4#bun-prune). And it rewrites Bun from Zig to Rust.

Of these the one that most caught my eye was `Bun.WebView`, which adds first class support for browser automation to Bun core using either macOS WebKit or control of a local Chromium process via the Chrome DevTools Protocol (CDP).

I had Claude Code for web build a prototype of a web API providing the ability to load a web page and then execute JavaScript against it, inspired by my [shot-scraper javascript](https://shot-scraper.datasette.io/en/stable/javascript.html) CLI tool - partly to see how much RAM would be needed by such a service.

Here's [that TypeScript server implementation](https://github.com/simonw/research/blob/main/bun-webview-json-api/server.ts), which appears to need a 192MB-256MB container to run a full Chrome against complex web pages - tested using cgroups.

Posted [20th August 2026](/2026/Aug/20/) at 3:37 pm
