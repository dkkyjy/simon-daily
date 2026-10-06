# Qwen3.8 27B 文字加法

         **日期：** 2026-10-04 23:34 UTC
         **链接：** https://simonwillison.net/2026/Oct/4/qwen38-addition-in-words/
         **标签：** mathematics, ai, generative-ai, local-llms, llms, qwen, llm-reasoning, dgx-spark

         ---

         > *摘要：研究：Qwen3.8 27B 文字加法*
        Colin Frasier 在 Bluesky 上发布了他两年前使用 GPT-4o 进行的实验，测试其"计算总和但用文字返回答案"的能力

2026年10月4日

[研究](/elsewhere/research/)
[Qwen3.8 27B 文字加法](https://github.com/simonw/research/tree/main/qwen38-addition-in-words#readme)
— 基准测试了本地 `Qwen3.8-27B-Q4_K_M.gguf` 模型是否能对正整数求和并仅用英文单词表达精确结果，使用 5,070 个禁用推理的案例，以及与中等推理的 169 个配对比较。禁用推理时，其数值准确率为 23.57%，对于一到三位数的操作数性能从 97.04% 下降到十到十三位数的 6.44%，尽管格式合规率达到 96.17%。

Colin Frasier 在 [Bluesky 上发布](https://bsky.app/profile/colin-fraser.net/post/3mwopbyznhs2k)了他两年前使用 GPT-4o 进行的实验，测试其"计算总和但用文字返回答案"的能力，涉及越来越大的数字。以下是他分享的这些结果的图表：

我相信 GPT-4o 没有作弊使用计算器，尤其是因为它算错了很多计算，但这启发了我在本地硬件（DGX Spark）上重新运行该实验，以在完全受控的环境中探索这种效应。

我将他的图片粘贴到 Codex Remote 会话（GPT-6 Astra）中，让它使用 `Qwen3.8-27B-Q4_K_M.gguf` 运行相同的实验。以下是禁用推理时每种组合运行 30 次的结果：

然后我在启用推理的情况下再次运行。每个配对花费了*更长的时间*，因此我没有运行每个方格的 30 个样本，而是只运行了一个——这使得热力图在视觉上不太吸引人，因为每个方格要么是 100%，要么是 0%：

它在 169 次尝试中正确回答了 167 次，由于这是一次性的，我相信第二次运行会产生不同的结果。

这是一个[包含部分较大计算推理轨迹的报告版本](https://gist.github.com/simonw/8ef79c777ad34c53e9c09094800576a5#full-reasoning-transcript-2)，其中包含如下文本：

```
等等，让我更仔细地重新计算。

4,299,366,105,622
6,088,794,067,970

让我对齐它们：
4 2 9 9 3 6 6 1 0 5 6 2 2
6 0 8 8 7 9 4 0 6 7 9 7 0

从右向左相加：
位置1（个位）：2 + 0 = 2
位置2（十位）：2 + 7 = 9
位置3（百位）：6 + 9 = 15，写5，进位1
```

发布于 [2026年10月4日](/2026/Oct/4/) 晚上11:34
