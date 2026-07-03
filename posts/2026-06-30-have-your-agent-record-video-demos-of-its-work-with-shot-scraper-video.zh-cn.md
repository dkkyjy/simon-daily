# 让您的智能体使用 shot-scraper video 录制工作视频演示

        **日期：** 2026-06-30 08:54 UTC
        **链接：** https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything
        **标签：** 项目, python, yaml, 人工智能, datasette, playwright, shot-scraper, 生成式人工智能, 大语言模型, pydantic, 编码智能体, 智能体工程

        ---

        shot-scraper video 是今天发布的 shot-scraper 1.10 版本中引入的一个新命令，它接受一个 storyboard.yml 文件，该文件定义了针对 Web 应用程序要执行的例程，并使用 Playwright 录制该例程的视频。我之前写过关于让编码智能体生成其工作演示的重要性；这是我实现这一目标的最新尝试。以下是一个使用 shot-scraper video 创建的示例视频，演示了 Datasette 中一个仍在开发中的功能——允许从粘贴的 CSV、TSV 或 JSON 数据创建新表：该视频是通过运行以下命令创建的：shot-scraper video datasette-bulk-insert-storyboard.yml \ --auth datasette-demo-auth.json --mp4 （该 --auth JSON 文件包含一个 cookie，如文档中所述。）以下是 datasette-bulk-insert-storyboard.yml 文件：输出：/tmp/datasette-bulk-insert-demo.webm 服务器：- uv - --directory - /Users/simon/Dropbox/dev/datasette - run - datasette - -p - 6419 - --root - --secret - " 1 " - /tmp/demo.db 网址：http://127.0.0.1:6419/demo/tasks 视口：宽度：1280 高度：720 光标：true 等待：' button[data-table-action="insert-row"] ' JavaScript：| (() => { let clipboardText = ""; Object.defineProperty(navigator, "clipboard", { configurable: true, get: () => ({ writeText: async (text) => { clipboardText = String(text); }, readText: async () => clipboardText, }), }); })(); 场景：- 名称：批量插入现有表行 操作：- 暂停：0.8 - 点击：' button[data-table-action="insert-row"] ' - 等待：" #row-edit-dialog[open] " - 暂停：0.5 - 点击：" .row-edit-bulk-insert " - 等待：" .row-edit-bulk-textarea " - 暂停：0.5 - 点击：" .row-edit-copy-template " - 等待：" text=Copied " - 暂停：0.8 - 填充：到：" .row-edit-bulk-textarea " 文本：| 标题,所有者,状态,优先级,备注 准备发布视频,Ana,进行中,1,使用 shot-scraper 录制 检查粘贴的 CSV 导入,Ben,审核,3,插入前预览 分享

*(已截断，请参阅原文)*
