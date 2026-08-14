# Mermaid to ASCII art (mermaid-ascii)

        **Date:** 2026-07-16 14:57 UTC
        **Link:** https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything
        **Tags:** go, tools, webassembly, mermaid

        ---

        > *Feed summary: Tool: Mermaid to ASCII art (mermaid-ascii)
        After building the Mermaid to ASCII tool based on Grok Build's Rust code I learned that there's an older, more fully-featured Go library called Alexa*

16th July 2026

[Tool](/elsewhere/tool/)
[Mermaid to ASCII art (mermaid-ascii)](https://tools.simonwillison.net/mermaid-ascii)
— Convert Mermaid diagram syntax into ASCII and Unicode box-drawing art rendered entirely in your browser using a Go library compiled to WebAssembly. The tool supports flowcharts with labeled edges, subgraphs, and color definitions, as well as sequence diagrams with notes and control flow fragments, while offering customizable padding and output options.

After building the [Mermaid to ASCII tool based on Grok Build's Rust code](https://simonwillison.net/2026/Jul/16/grok-mermaid/) I learned that there's an older, more fully-featured Go library called [AlexanderGrooff/mermaid-ascii](https://github.com/AlexanderGrooff/mermaid-ascii) that implements a similar pattern, so I had Claude Fable 5 compile that one to WebAssembly as well so I could compare the two.

This one includes support for colors!

Posted [16th July 2026](/2026/Jul/16/) at 2:57 pm
