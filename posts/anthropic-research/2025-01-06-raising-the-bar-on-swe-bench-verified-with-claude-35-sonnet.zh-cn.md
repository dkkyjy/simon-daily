# 提升 Claude 3.5 Sonnet 在 SWE-bench Verified 上的表现

**日期：** 2025-01-06 00:00 UTC
**链接：** https://www.anthropic.com/research/swe-bench-sonnet

---

*我们最新的模型，升级版 [Claude 3.5 Sonnet](https://www.anthropic.com/news/3-5-models-and-computer-use)，在软件工程评估基准 SWE-bench Verified 上达到了 49% 的成绩，超越了之前最先进模型的 45%。本文解释了我们在模型周围构建的"代理"，旨在帮助开发者从 Claude 3.5 Sonnet 中获得最佳性能。*

[SWE-bench](https://www.swebench.com/) 是一个 AI 评估基准，用于评估模型完成真实世界软件工程任务的能力。具体来说，它测试模型如何解决来自流行开源 Python 仓库的 GitHub 问题。对于基准中的每个任务，AI 模型会获得一个设置好的 Python 环境和问题解决前一刻的仓库检出（本地工作副本）。模型需要理解、修改和测试代码，然后提交其提出的解决方案。

每个解决方案都会根据关闭原始 GitHub 问题的拉取请求中的真实单元测试进行评分。这测试了 AI 模型是否能够实现与原始 PR 人类作者相同的功能。

SWE-bench 不仅仅孤立地评估 AI 模型，而是评估整个"代理"系统。在此上下文中，"代理"指的是 AI 模型及其周围的软件脚手架的组合。这个脚手架负责生成输入模型的提示、解析模型的输出以采取行动，以及管理交互循环——将模型先前操作的结果纳入其下一个提示中。代理在 SWE-bench 上的性能可能因这个脚手架而有显著差异，即使使用相同的底层 AI 模型。

还有许多其他用于评估大型语言模型编码能力的基准，但 SWE-bench 因以下几个原因而日益流行：

1. 它使用来自实际项目的真实工程任务，而非竞赛或面试风格的问题；
2. 它尚未饱和——仍有很大的改进空间。目前还没有模型在 SWE-bench Verified 上超过 50% 的完成率（尽管更新后的 Claude 3.5 Sonnet 在撰写本文时已达到 49%）；
3. 它衡量整个"代理"，而非孤立的模型。开源开发者和初创公司在优化脚手架以大幅提升同一模型周围性能方面取得了巨大成功。

请注意，原始 SWE-bench 数据集包含一些任务，如果没有 GitHub 问题之外的额外上下文（例如，关于要返回的特定错误消息）是无法解决的。[SWE-bench-Verified](https://openai.com/index/introducing-swe-bench-verified/) 是 SWE-bench 的一个 500 问题子集，经过人工审查以确保其可解决，因此提供了对编码代理性能最清晰的衡量。本文将引用此基准。

## 实现最先进水平

### 工具使用代理

我们在创建针对更新版 Claude 3.5 Sonnet 优化的代理脚手架时的设计理念是，尽可能多地赋予语言模型控制权，并保持脚手架最小化。该代理有一个提示、一个用于执行 bash 命令的 Bash 工具，以及一个用于查看和编辑文件和目录的 Edit 工具。我们持续采样，直到模型决定完成，或超出其 200k 上下文长度。这个脚手架允许模型自行判断如何解决问题，而不是被硬编码到特定的模式或工作流程中。

提示概述了模型建议的方法，但对于此任务来说，它不会过于冗长或详细。模型可以自由选择如何从一个步骤过渡到另一个步骤，而不是有严格且离散的过渡。如果你对 token 不敏感，明确鼓励模型生成较长的响应会有所帮助。

以下代码显示了我们代理脚手架中的提示：

```
<uploaded_files>
{location}
</uploaded_files>
I've uploaded a python code repository in the directory {location} (not in /tmp/inputs). Consider the following PR description:

<pr_description>
{pr_description}
</pr_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <pr_description> are met?
I've already taken care of all changes to any of the test files described in the <pr_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!

Your task is to make the minimal changes to non-tests files in the {location} directory to ensure the <pr_description> is satisfied.

Follow these steps to resolve the issue:
1. As a first step, it might be a good idea to explore the repo to familiarize yourself with its structure.
2. Create a script to reproduce the error and execute it with `python <filename.py>` using the BashTool, to confirm the error
3. Edit the sourcecode of the repo to resolve the issue
4. Rerun your reproduce script and confirm that the error is fixed!
5. Think about edgecases and make sure your fix handles them as well

Your thinking should be thorough and so it's fine if it's very long.
```

复制

模型的第一个工具执行 Bash 命令。模式很简单，只接受要在环境中运行的命令。然而，工具的描述承载了更多分量。它包含了对模型更详细的说明，包括转义输入、缺乏互联网访问以及如何在后台运行命令。

接下来，我们展示 Bash 工具的规格：

```
{
   "name": "bash",
   "description": "Run commands in a bash shell\n
* When invoking this tool, the contents of the \"command\" parameter does NOT need to be XML-escaped.\n
* You don't have access to the internet via this tool.\n
* You do have access to a mirror of common linux and python packages via apt and pip.\n
* State is persistent across command calls and discussions with the user.\n
* To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.\n
* Please avoid commands that may produce a very large amount of output.\n
* Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.",
   "input_schema": {
       "type": "object",
       "properties": {
           "command": {
               "type": "string",
               "description": "The bash command to run."
           }
       },
       "required": ["command"]
   }
}
```

复制

模型的第二个工具（Edit 工具）要复杂得多，包含了模型查看、创建和编辑文件所需的一切。同样，我们的工具描述包含关于如何使用该工具的详细信息。

我们在各种代理任务中为这些工具的描述和规格投入了大量精力。我们测试了它们以发现模型可能误解规格的任何方式，或使用工具时可能出现的陷阱，然后编辑了描述以预防这些问题。我们相信，在设计模型工具接口方面应该投入更多关注，就像在设计人类工具接口方面投入大量关注一样。

以下代码显示了我们 Edit 工具的描述：

```
{
   "name": "str_replace_editor",
   "description": "Custom editing tool for viewing, creating and editing files\n
* State is persistent across command calls and discussions with the user\n
* If `path` is a file, `view` displays the result of applying `cat -n`. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep\n
* The `create` command cannot be used if the specified `path` already exists as a file\n
* If a `command` generates a long output, it will be truncated and marked with `<response clipped>` \n
* The `undo_edit` command will revert the last edit made to the file at `path`\n
\n
Notes for using the `str_replace` command:\n
* The `old_str` parameter should match EXACTLY one or more consecutive lines from the original file. Be mindful of whitespaces!\n
* If the `old_str` parameter is not unique in the file, the replacement will not be performed. Make sure to include enough context in `old_str` to make it unique\n
* The `new_str` parameter should contain the edited lines that should replace the `old_str`",
...
```

复制

我们提高性能的一种方法是"防错"我们的工具。例如，有时模型在代理移出根目录后可能会搞乱相对文件路径。为了防止这种情况，我们只是让工具始终要求绝对路径。

我们尝试了几种不同的策略来指定对现有文件的编辑，并发现字符串替换具有最高的可靠性，即模型在给定文件中指定 `old_str` 替换为 `new_str`。只有当 `old_str` 恰好匹配一次时，替换才会发生。如果匹配次数多于或少于一次，模型会看到适当的错误消息以进行重试。

我们的 Edit 工具的规格如下所示：

```
...
   "input_schema": {
       "type": "object",
       "properties": {
           "command": {
               "type": "string",
               "enum": ["view", "create", "str_replace", "insert", "undo_edit"],
               "description": "The commands to run. Allowed options are: `view`, `create`, `str_replace`, `insert`, `undo_edit`."
           },
           "file_text": {
               "description": "Required parameter of `create` command, with the content of the file to be created.",
               "type": "string"
           },
           "insert_line": {
               "description": "Required parameter of `insert` command. The `new_str` will be inserted AFTER the line `insert_line` of `path`.",
               "type": "integer"
           },
           "new_str": {
               "description": "Required parameter of `str_replace` command containing the new string. Required parameter of `insert` command containing the string to insert.",
               "type": "string"
           },
           "old_str": {
               "description": "Required parameter of `str_replace` command containing the string in `path` to replace.",
               "type": "string"
           },
           "path": {
               "description": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.",
               "type": "string"
           },
           "view_range": {
               "description": "Optional parameter of `view` command when `path` points to a file. If none is given, the full file is shown. If provided, the file will be shown in the indicated line number range, e.g. [11, 12] will show lines 11 and 12. Indexing at 1 to start. Setting `[start_line, -1]` shows all lines from `start_line` to the end of the file.",
               "items": {
                   "type": "integer"
               },
               "type": "array"
           }
       },
       "required": ["command", "path"]
   }
}
```

复制

## 结果

总的来说，升级版 Claude 3.5 Sonnet 展示了比我们之前的模型以及[之前最先进的模型](https://solverai.com/)更高的推理、编码和数学能力。它还展示了改进的代理能力：工具和脚手架有助于将这些改进的能力发挥到最佳用途。

| 模型 | **Claude 3.5 Sonnet (新)** | 之前最先进 | Claude 3.5 Sonnet (旧) | Claude 3 Opus |
| --- | --- | --- | --- | --- |
| SWE-bench Verified 分数 | 49% | 45% | 33% | 22% |

我们一些模型在 SWE-bench Verified 上的分数，均使用此代理脚手架。

## 代理行为示例

为了运行基准测试，我们使用 [SWE-Agent](https://swe-agent.com/) 框架作为我们代理代码的基础。在下面的日志中，我们将代理的文本输出、工具调用和工具响应呈现为 THOUGHT、ACTION 和 OBSERVATION，尽管我们并不约束模型采用固定的顺序。

下面的代码块将逐步展示 Sonnet 3.5 解决 SWE-bench 问题的典型案例。

在第一个块中，您可以看到提供给模型的初始提示的一部分，其中 `{pr_description}` 填充了来自 SWE-bench 任务的实际值。重要的是，此任务包含重现问题的步骤，这将为模型提供有价值的调查起点。

```
<uploaded_files>
/repo
</uploaded_files>
I've uploaded a python code repository in the directory /repo (not in /tmp/inputs). Consider the following PR description:

<pr_description>
linear_model.RidgeClassifierCV's Parameter store_cv_values issue
#### Description
Parameter store_cv_values error on sklearn.linear_model.RidgeClassifierCV

#### Steps/Code to Reproduce
import numpy as np
from sklearn import linear_model as lm

#test database
n = 100
x = np.random.randn(n, 30)
y = np.random.normal(size = n)

rr = lm.RidgeClassifierCV(alphas = np.arange(0.1, 1000, 0.1), normalize = True, 
                                         store_cv_values = True).fit(x, y)

#### Expected Results
Expected to get the usual ridge regression model output, keeping the cross validation predictions as attribute.

#### Actual Results
TypeError: __init__() got an unexpected keyword argument 'store_cv_values'

lm.RidgeClassifierCV actually has no parameter store_cv_values, even though some attributes depends on it.
```

复制

模型响应并首先使用 Edit 工具查看仓库结构。您可以在 THOUGHT 和 ACTION 下看到模型的文本输出和工具调用参数，以及在 OBSERVATION 下看到部分工具输出：

```
THOUGHT:
I'll help you implement the changes to satisfy the PR description. Let's follow the steps you outlined.

1. First, let's explore the repo structure:
ACTION (str_replace_editor):
command:
view

path:
/repo

OBSERVATION:
Here's the files and directories up to 2 levels deep in /repo, excluding hidden items:
/repo
/repo/PULL_REQUEST_TEMPLATE.md
/repo/ISSUE_TEMPLATE.md
/repo/sklearn
/repo/sklearn/decomposition
/repo/sklearn/kernel_ridge.py
/repo/sklearn/model_selection
/repo/sklearn/covariance
/repo/sklearn/cluster
/repo/sklearn/base.py
/repo/sklearn/dummy.py
/repo/sklearn/naive_bayes.py
...
```

复制

现在模型对仓库结构有了更好的了解，它使用 Edit 工具创建一个新脚本，用于重现问题并测试其修复：

```
THOUGHT:
Based on the repository structure, we'll need to modify the Ridge Classifier in the `sklearn/linear_model` directory.

Let's create a script to reproduce the error:
ACTION (str_replace_editor):
command:
create

path:
/repo/reproduce_error.py

file_text:
import numpy as np
from sklearn import linear_model as lm

#test database
n = 100
x = np.random.randn(n, 30)
y = np.random.normal(size = n)

rr = lm.RidgeClassifierCV(alphas=np.arange(0.1, 1000, 0.1), normalize=True, 
                         store_cv_values=True).fit(x, y)

OBSERVATION:
File created successfully at: /repo/reproduce_error.py
```

复制

然后模型使用 Bash 工具执行它编写的脚本，并成功重现了任务中的问题：

```
THOUGHT:
Let's verify that we can reproduce the error:
ACTION (bash):
command:
python3 /repo/reproduce_error.py

OBSERVATION:
Traceback (most recent call last):
  File "/repo/reproduce_error.py", line 10, in <module>
    store_cv_values=True).fit(x, y)
TypeError: __init__() got an unexpected keyword argument 'store_cv_values'
```

复制

从这开始，模型使用 Edit 工具更改仓库中的源代码，并重新运行其脚本以验证更改是否已解决问题：

```
THOUGHT:
The error is reproducible. Looking at the code, I can see that the issue is that while the `RidgeClassifierCV` class inherits from `_BaseRidgeCV`, it fails to pass the `store_cv_values` parameter from its constructor through to the base class constructor.

Let's fix this:
ACTION (str_replace_editor):
command:
str_replace

path:
/repo/sklearn/linear_model/ridge.py

old_str:
    def __init__(self, alphas=(0.1, 1.0, 10.0), fit_intercept=True,
                 normalize=False, scoring=None, cv=None, class_weight=None):
        super(RidgeClassifierCV, self).__init__(
            alphas=alphas, fit_intercept=fit_intercept, normalize=normalize,
            scoring=scoring, cv=cv)
        self.class_weight = class_weight

new_str:
    def __init__(self, alphas=(0.1, 1.0, 10.0), fit_intercept=True,
                 normalize=False, scoring=None, cv=None, class_weight=None,
                 store_cv_values=False):
        super(RidgeClassifierCV, self).__init__(
            alphas=alphas, fit_intercept=fit_intercept, normalize=normalize,
            scoring=scoring, cv=cv, store_cv_values=store_cv_values)
        self.class_weight = class_weight
```

复制

在这个特定示例中，模型工作了 12 步后才决定准备提交。该任务的测试随后成功运行，验证了模型的解决方案解决了问题。有些任务在模型提交解决方案之前需要超过 100 轮交互；在其他任务中，模型会一直尝试直到耗尽上下文。

从审查更新版 Claude 3.5 Sonnet 与旧模型的尝试来看，更新版 3.5 Sonnet 更频繁地进行自我纠正。它还展示了尝试多种不同解决方案的能力，而不是陷入重复犯同样错误的困境。

## 挑战

SWE-bench Verified 是一个强大的评估工具，但它也比简单的单轮评估更复杂。以下是我们使用它时面临的一些挑战——其他 AI 开发者也可能遇到这些挑战。

1. **持续时间长且 token 成本高。** 上面的示例来自一个成功在 12 步内完成的案例。然而，许多成功的运行需要数百轮交互才能让模型解决，并且消耗超过 10 万 token。更新版 Claude 3.5 Sonnet 非常顽强：只要有足够的时间，它通常能找到解决问题的方法，但这可能很昂贵；
2. **评分。** 在检查失败的任务时，我们发现了一些模型行为正确的情况，但存在环境设置问题，或者安装补丁被应用了两次。解决这些系统问题对于准确了解 AI 代理的性能至关重要。
3. **隐藏测试。** 由于模型看不到它被评分的测试，它经常"认为"自己成功了，而实际上任务失败了。其中一些失败是因为模型在错误的抽象级别上解决了问题（应用了权宜之计而不是更深入的重构）。其他失败感觉有点不公平：它们解决了问题，但与原始任务的单元测试不匹配。
4. **多模态。** 尽管更新版 Claude 3.5 Sonnet 具有出色的视觉和多模态能力，但我们没有实现一种让它查看保存到文件系统或作为 URL 引用的文件的方法。这使得调试某些任务（尤其是来自 Matplotlib 的任务）特别困难，并且也容易导致模型产生幻觉。开发者肯定有改进的潜力——SWE-bench 已经推出了一个新的[专注于多模态任务的评估](https://www.swebench.com/multimodal.html)。我们期待在不久的将来看到开发者使用 Claude 在此评估上获得更高的分数。

升级版 Claude 3.5 Sonnet 在 SWE-bench Verified 上达到了 49%，超越了之前最先进的水平（45%），仅使用了一个简单的提示和两个通用工具。我们相信，使用新版 Claude 3.5 Sonnet 进行构建的开发者将很快找到新的、更好的方法来提高 SWE-bench 的分数，超越我们在此初步展示的成果。

## 致谢

Erik Schluntz 优化了 SWE-bench 代理并撰写了这篇博客文章。Simon Biggs、Dawn Drain 和 Eric Christiansen 帮助实现了基准测试。Shauna Kravec、Dawn Drain、Felipe Rosso、Nova DasSarma、Ven Chandrasekaran 以及许多其他人为训练 Claude 3.5 Sonnet 使其在代理编码方面表现出色做出了贡献。
