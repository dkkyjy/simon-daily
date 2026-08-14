# Firefox in WebAssembly

        **Date:** 2026-07-16 23:34 UTC
        **Link:** https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything
        **Tags:** browsers, firefox, ai, webassembly, generative-ai, llms, ai-assisted-programming, claude, claude-mythos-fable

        ---

        > *Feed summary: Firefox in WebAssembly
This is absurdly cool: Puter compiled Firefox to WebAssembly such that the whole browser runs in another browser.
Here's my blog, running in Firefox, running in WebAssembly, run*

16th July 2026 - Link Blog

**[Firefox in WebAssembly](https://developer.puter.com/labs/firefox-wasm/)** ([via](https://news.ycombinator.com/item?id=48926939 "Hacker News")) This is absurdly cool: Puter compiled Firefox to WebAssembly such that the whole browser runs in another browser.

Here's my blog, running in Firefox, running in WebAssembly, running in Chrome:

They chose Firefox/Gecko because it has strong single-process support. The project took an estimated $25,000 of Claude Opus and Fable tokens, taking advantage of a Claude Max subscription plan.

The demo funnels all traffic over a WebSocket protocol (using the [Wisp protocol](https://github.com/MercuryWorkshop/wisp-protocol)) through Puter's server - a requirement to get this kind of thing to work because code running in browsers can't open arbitrary network connections.

(That proxying sounds expensive! The team [had to scale the servers up](https://news.ycombinator.com/item?id=48926939#48936563) to handle the traffic during the Hacker News conversation about the project.)

Puter claim this supports end-to-end encryption and that looks to be true - I inspected the WebSocket messages and traffic to my own HTTPS site was encrypted whereas requests and responses to `http://www.example.com/` were in cleartext.

[Here's the repo](https://github.com/HeyPuter/firefox-wasm) for `firefox-wasm`. [theogbob/WebkitWasm](https://github.com/theogbob/WebkitWasm) is a similar project that compiles WebKit to WASM, but that one doesn't currently have an accessible online demo.

Posted [16th July 2026](/2026/Jul/16/) at 11:34 pm
