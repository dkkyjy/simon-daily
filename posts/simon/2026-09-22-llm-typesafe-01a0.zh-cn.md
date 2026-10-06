# llm-typesafe 0.1a0

         **日期：** 2026-09-22 15:54 UTC
         **链接：** https://simonwillison.net/2026/Sep/22/llm-typesafe/
         **标签：** projects, llm, jev

         ---

         > *Feed summary: Release: llm-typesafe 0.1a0
        我为 LLM 构建了这个新插件，以支持 TypeSafe AI 的新 Jev 模型。安装方式如下：
llm install llm-typesafe

然后设置 API 密钥（在这里获取一个，t*

2026年9月22日

[发布](/elsewhere/release/)
[llm-typesafe 0.1a0](https://github.com/simonw/llm-typesafe/releases/tag/0.1a0)
— 用于访问 Jev 和其他 TypeSafe AI 模型的 LLM 插件

我为 [LLM](https://llm.datasette.io/) 构建了这个新插件，以支持 [TypeSafe AI 的新 Jev 模型](https://simonwillison.net/2026/Sep/21/jev/)。安装方式如下：

```
llm install llm-typesafe
```

然后设置 API 密钥（[在这里获取](https://console.typesafe.ai/)，等候名单似乎推进得很快）：

```
llm keys set typesafe
# 粘贴密钥
```

现在你可以像这样提出是/否"noul"问题：

```
llm -m jev '请退还我上次的付款。' \
   -s '这条消息是否明确要求退款？'
```

输出：

```
{"type": "noul", "noul": 0.99}
```

或者像这样提出选择题：

```
cat message.txt | llm -m jev \
   -s '哪个团队应该处理这条消息？如果同时出现账单和技术问题，选择账单。' \
   -o answer_type choice \
   -o criteria '{
     "billing":"费用、发票、付款或退款",
     "technical":"安装或使用产品时的问题",
     "other":"不属于以上任何类别"
   }'
```

或者像这样提出评分问题：

```
cat report.txt | llm -m jev \
   -s '这份报告中描述的问题的可复现性如何？' \
   -o answer_type score \
   -o criteria '[
     "没有复现步骤",
     "有一些步骤，但缺少重要步骤",
     "完整的步骤，包含预期和实际结果"
   ]'
```

更多详情参见 [README](https://github.com/simonw/llm-typesafe/blob/main/README.md)。

发布于 [2026年9月22日](/2026/Sep/22/) 下午3:54
