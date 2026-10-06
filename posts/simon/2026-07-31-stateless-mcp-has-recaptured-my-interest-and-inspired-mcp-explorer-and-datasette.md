# Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)

        **Date:** 2026-07-31 23:13 UTC
        **Link:** https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything
        **Tags:** projects, ai, datasette, mermaid, generative-ai, llms, llm, anthropic, model-context-protocol

        ---

        Tuesday was Stateless MCP day - the rollout of MCP 2.0, or the 2026-07-28 Model Context Protocol specification to use the more formal but less memorable name. This is the most significant change to the MCP spec since it first launched, and has also served to reignite my personal interest in the protocol. For background: MCP is the Model Context Protocol, which describes a standard way to expose new tools to LLM-powered agent frameworks. It was introduced by Anthropic back in November 2024 , had a huge spike of interest through much of 2025, and then became somewhat eclipsed by Skills (another Anthropic invention) when it became apparent that an agent harness with access to a terminal and curl could do most of what MCP did in a more flexible way. I wrote about that in my review of 2025 . I'm coming back around to MCP now. Giving an agent a shell environment with the ability to access the internet is fraught with risk , and requires a strong model that is capable of effectively driving such an environment. MCP tools are easier to audit and control, and simple enough that smaller models that run on a laptop can still drive them reasonably well. The new stateless MCP specification also greatly decreases the complexity of implementing both clients and servers for the protocol. I built three of those this week! What's easier with stateless MCP The best demonstration of the difference between stateful and stateless MCP is in this May 21st blog post that introduced the RC for the new specification. It included a clear before-and-after example. The older stateful MCP (I'm going to call it "legacy MCP") required two HTTP requests - the first to initialize a session and obtain a Mcp-Session-Id , and the second to actually

*(truncated, see original)*
