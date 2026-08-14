# Linear walkthroughs

---
title: "Linear walkthroughs"
description: "Linear walkthroughs"
pubDate: "2026-02-25"
heroImage: "/post_img.png"
tags: ["simon-guides"]
originalLink: "https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/"
---

Sometimes it's useful to have a coding agent give you a structured walkthrough of a codebase.

Maybe it's existing code you need to get up to speed on, maybe it's your own code that you've forgotten the details of, or maybe you vibe coded the whole thing and need to understand how it actually works.

Frontier models with the right agent harness can construct a detailed walkthrough to help you understand how code works.

## An example using Showboat and Present

I recentlyvibe coded a SwiftUI slide presentation appon my Mac using Claude Code and Opus 4.6.

I was speaking about the advances in frontier models between November 2025 and February 2026, and I like to include at least one gimmick in my talks (aSTAR moment- Something They'll Always Remember). In this case I decided the gimmick would be revealing at the end of the presentation that the slide mechanism itself was an example of what vibe coding could do.

I released the codeto GitHuband then realized I didn't know anything about how it actually worked - I had prompted the whole thing into existence (partial transcript here) without paying any attention to the code it was writing.

So I fired up a new instance of Claude Code for web, pointed it at my repo and prompted:Read the source and then plan a linear walkthrough of the code that explains how it all works in detail

Then run “uvx showboat –help” to learn showboat - use showboat to create a walkthrough.md file in the repo and build the walkthrough in there, using showboat note for commentary and showboat exec plus sed or grep or cat or whatever you need to include snippets of code you are talking aboutShowboatis a tool I built to help coding agents write documents that demonstrate their work. You can see theshowboat --help output here, which is designed to give the model everything it needs to know in order to use the tool.

Theshowboat notecommand adds Markdown to the document. Theshowboat execcommand accepts a shell command, executes it and then adds both the command and its output to the document.

By telling it to use "sed or grep or cat or whatever you need to include snippets of code you are talking about" I ensured that Claude Code would not manually copy snippets of code into the document, since that could introduce a risk of hallucinations or mistakes.

This worked extremely well. Here's thedocument Claude Code created with Showboat, which talks through all six.swiftfiles in detail and provides a clear and actionable explanation about how the code works.

I learned a great deal about how SwiftUI apps are structured and absorbed some solid details about the Swift language itself just from reading this document.

If you are concerned that LLMs might reduce the speed at which you learn new skills I strongly recommend adopting patterns like this one.  Even a ~40 minute vibe coded toy project can become an opportunity to explore new ecosystems and pick up some interesting new tricks.