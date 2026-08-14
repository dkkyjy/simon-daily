# llm-chat-completions-server 0.1a0

        **Date:** 2026-07-30 15:43 UTC
        **Link:** https://simonwillison.net/2026/Jul/30/llm-chat-completions-server/#atom-everything
        **Tags:** projects, openai, llm

        ---

        > *Feed summary: Release: llm-chat-completions-server 0.1a0
        A key goal of the new content-addressable logs in LLM 0.32rc1 was being able to support OpenAI Chat Completion style requests where each incoming mes*

30th July 2026

[Release](/elsewhere/release/)
[llm-chat-completions-server 0.1a0](https://github.com/simonw/llm-chat-completions-server/releases/tag/0.1a0)
— LLM plugin to serve an OpenAI Chat Completions API endpoint

A key goal of the new content-addressable logs [in LLM 0.32rc1](https://simonwillison.net/2026/Jul/30/llm-rc1/) was being able to support OpenAI Chat Completion style requests where each incoming message extends the previous conversation, like this:

```
curl http://localhost:8002/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "qwen3.5-4b",
    "messages": [
      {"role": "user", "content": "Capital of France?"},
      {"role": "assistant", "content": "Paris."},
      {"role": "user", "content": "Germany?"}
    ]
  }'
```

Here the conversation state is tracked by the client, so each of these requests gets longer and longer. The new schema design in LLM is designed to de-duplicate these using hashes of the individual message parts.

To test that out, I built this plugin:

```
uv tool install llm --pre
llm install llm-chat-completions-server
llm chat-completions-server -p 9001
```

Running this starts a localhost server on port 9001 that exposes your full collection of LLM models (from any plugins you have installed) using a ChatGPT Completions compatible endpoint.

GPT-5.6 Sol [wrote the whole thing](https://gist.github.com/simonw/53be513c1bd4a29a7aa480d9bde9b4a5) - it turns out it knows the OpenAI Chat Completions API shape really well.

Posted [30th July 2026](/2026/Jul/30/) at 3:43 pm
