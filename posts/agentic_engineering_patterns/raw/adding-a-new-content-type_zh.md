指南 > 智能体工程模式
为我的博客转通讯工具添加新的内容类型
这是一个看似简短却能在单次操作中完成大量工作的提示词示例。
首先，一些背景。我每周大约发送一次免费的 Substack 通讯，内容是从我的博客复制粘贴过来的。我实际上是把 Substack 当作一种轻量级的方式，让人们可以通过电子邮件订阅我的博客。
我使用我的博客转通讯工具来生成这份通讯——这是一个 HTML 和 JavaScript 应用，它从这个 Datasette 实例中获取我的最新内容，并将其格式化为富文本 HTML，然后我可以复制到剪贴板并粘贴到 Substack 编辑器中。这里有关于其工作原理的详细说明。
我最近在博客中添加了一种新的内容类型，用来收录我在其他地方发布的内容，我称之为“动态”。这些内容包括我的开源项目发布、我构建的新工具、我参观过的博物馆（来自 niche-museums.com）以及其他外部内容。
我希望在生成的通讯中包含这些内容。以下是我使用网页版 Claude Code，针对托管我的博客转通讯工具的 simonw/tools 仓库运行的提示词。
将 simonw/simonwillisonblog 从 github 克隆到 /tmp 以供参考
更新 blog-to-newsletter.html 以包含有描述的动态——类似于博客上的 Atom 聚合源的工作方式
使用 python -m http.server 运行它，并使用 `uvx rodney --help` 进行测试——比较通讯中显示的内容与 https://simonwillison.net 主页上的内容
这让我得到了我需要的确切解决方案。我们来分解一下这个提示词。
将 simonw/simonwillisonblog 从 github 克隆到 /tmp 以供参考
我经常使用这种模式。编码智能体可以从 GitHub 克隆代码，而解释问题的最佳方式通常是让它们查看相关代码。通过告诉它们克隆到 /tmp，我确保它们不会在后续自己的提交中意外地包含这些参考代码。
simonw/simonwillisonblog 仓库包含了我基于 Django 的 simonwillison.net 博客的源代码。这包括我新“动态”功能的逻辑和数据库模式。
更新 blog-to-newsletter.html 以包含有描述的动态——类似于博客上的 Atom 聚合源的工作方式
在这里，引用 blog-to-newsletter.html 就足以告诉 Claude 它应该修改 simonw/tools 仓库中 200 多个 HTML 应用中的哪一个。
动态会自动从多个来源导入。通常它们并不十分有趣——例如，我的某个较小开源项目的点版本错误修复。
我的博客包含了一种让我可以为任何动态添加额外描述的方式，这提供了额外的评论，同时也标记出该动态比我未以某种方式注释过的那些更有趣。
我已经利用这种区分来决定哪些动态会出现在我网站的 Atom 源中。告诉 Claude 模仿这一点，省去了我详细描述逻辑的麻烦。
使用 python -m http.server 运行它，并使用 `uvx rodney --help` 进行测试——比较通讯中显示的内容与 https://simonwillison.net 主页上的内容
编码智能体如果拥有某种可以用于测试自己工作的验证机制，总是能发挥最佳效果。
在这种情况下，我希望 Claude Code 能主动检查它对我的工具所做的更改是否能正确获取和显示最新数据。
我提醒它使用 python -m http.server 作为静态服务器，因为我过去遇到过一些问题，有些应用在从磁盘作为文件提供服务（而不是从本地主机服务器）时，获取数据会失败。在这个特定案例中，这可能不是必需的，但我的提示词肌肉记忆现在已经把 python -m http.server 刻进去了！
我在智能体手动测试章节中描述过 uvx rodney --help 这个技巧。Rodney 是浏览器自动化软件，可以使用 uvx 安装，并且其 --help 输出旨在教会智能体使用该工具所需的一切知识。
我认为，告诉 Claude 将通讯中的结果与我博客主页的内容进行比较，就足以让它自信地验证新更改是否正常工作，因为我最近发布了符合新要求的内容。
你可以在这里查看完整的会话，或者如果那个链接不行，我还有一个显示所有单独工具调用的替代转录本。
生成的 PR 做出了完全正确的更改。它在获取博客内容的 SQL 查询中添加了一个额外的 UNION 子句，过滤掉草稿动态和 note 列为空的动态：
...
union all
select
  id,
  'beat' as type,
  title,
  created,
  slug,
  'No HTML' as html,
  json_object(
    'created', date(created),
    'beat_type', beat_type,
    'title', title,
    'url', url,
    'commentary', commentary,
    'note', note
  ) as json,
  url as external_url
from blog_beat
where coalesce(note, '') != '' and is_draft = 0
union all
...
并且它推导出了动态类型到其正式名称的映射，这很可能是从它在探索参考代码库时读取的 Django ORM 定义中得出的：
const beatTypeDisplay = {
  release: '发布',
  til: '今日所学',
  til_update: '今日所学更新',
  research: '研究',
  tool: '工具',
  museum: '博物馆'
};
指示智能体使用另一个代码库作为参考，是一种强大的捷径，可以用最少的额外提示信息来传达复杂的概念。