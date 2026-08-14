# Building a World Map with only 500 bytes

**Date:** 2026-07-04 23:09 UTC
**Link:** https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything
**Tags:** ascii-art, data-urls, javascript

---

Building a World Map with only 500 bytes Iwo Kadziela (assisted by Codex) figured out a way to generate a credible ASCII world map using 445 bytes of data: The key trick is to use deflate compression, which is then wired together using this neat snippet of JavaScript. I didn't know you could use fetch() with data: URIs like this: fetch('data:;base64,1ZpLsgIxCEXnrM...==').then( r => r.body.pipeThrough(new DecompressionStream('deflate-raw')) ).then( s => new Response(s).text() ).then( t => b.innerHTML = '<pre style=font-size:.65vw>' + t ) Via Hacker News Tags: ascii-art , data-urls , javascript
