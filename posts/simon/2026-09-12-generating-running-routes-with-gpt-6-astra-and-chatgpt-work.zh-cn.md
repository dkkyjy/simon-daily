# 使用 GPT-6 Astra 和 ChatGPT Work 生成跑步路线

         **日期：** 2026-09-12 23:56 UTC
         **链接：** https://simonwillison.net/2026/Sep/12/astra-running-routes/
         **标签：** geospatial, ai, d3, openai, generative-ai, chatgpt, llms, skills, gpt-6-astra

         ---

         > *摘要：今天早上我让 ChatGPT Work 配合 GPT-6 Astra（Max）做了一件挺酷的事：*

我住在 <地址>。帮我规划一条 5 公里和一条 10 公里的跑步路线，从我家里出发再回到家里，形成一个闭环。使用 OSM 数据。

它花了 27 分钟*

## 使用 GPT-6 Astra 和 ChatGPT Work 生成跑步路线

2026 年 9 月 12 日

今天早上我让 [ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) 配合 GPT-6 Astra（Max）做了一件挺有意思的事：

> `我住在 <我的地址>。帮我规划一条 5 公里和一条 10 公里的跑步路线，从我家里出发再回到家里，形成一个闭环。使用 OSM 数据。`

它花了 27 分钟，精确地生成了我所要求的内容，既有嵌入式可视化图表，也有可下载的 GPX 文件和 GeoJSON 文件。以下是那条 5 公里路线：

当我问它是怎么生成这条路线时，它回答说：

> 我使用了 **Nominatim 来定位地址**，**Overpass 来下载当地的 OpenStreetMap 道路和步道数据**，然后在本地计算了闭环路线。

令人沮丧的是，它实际运行的代码和具体操作细节在 ChatGPT 界面中对我是不可见的。我认为这种缺乏透明度的做法是一种反功能。

等到我想到要它提供所用 Python 代码的副本时，ChatGPT 已经无法提供了。这似乎是因为对话线程已经被压缩。我认为任何使用压缩机制的大语言模型系统，都需要同时保留压缩前的文本，并通过智能体工具调用使该文本可访问，以防止此类问题的发生。

至于向我展示地图，它使用了 [visualize 技能](https://codex-tool-reference.simonw.chatgpt.site/skills/visualize)。它创建了一个名为 `/workspace/el-granada-5k-share.html` 的文件，直接嵌入到 ChatGPT 界面中。

以下是 [该 HTML 的副本](https://gist.github.com/simonw/ea652573c8ff5378b218cb10c8c5a480)，开头是这样的：

```
<div id="eg-share-loop">
   <div class="viz-row"><h3>El Granada harbor loop</h3><span class="text-small">5.1 km</span></div>
   <div id="eg-share-stage"></div>
   <div class="text-small text-muted">Map data © <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a></div>
   <style>
     #eg-share-loop { width:100%; }
     #eg-share-loop #eg-share-stage { width:100%; margin:8px 0; }
     #eg-share-loop .eg-share-map { display:block; width:100%; touch-action:none; }
     #eg-share-loop .eg-share-map text { fill:var(--foreground); font-size:12px; font-weight:400; }
     #eg-share-loop .eg-share-label { paint-order:stroke; stroke:var(--background); stroke-width:3px; stroke-linejoin:round; }
   </style>
   <script type="application/json" id="eg-share-data">{"route":{"type":"LineString","coordinates":[[-122.467425,37.4997753] ...</script>
   <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
   <script>
   (() => {
    const root=document.getElementById('eg-share-loop');
```

`<script type="application/json">` 元素包含了渲染跑步路线和地图本身所需的完整几何数据，使用 D3 库，该库从 [visualize 技能](https://codex-tool-reference.simonw.chatgpt.site/skills/visualize) 此部分中描述的白名单 CDN 位置加载：

> ### 外部资源
>
> * CSP 仅允许 `cdnjs.cloudflare.com`、`esm.sh`、`cdn.jsdelivr.net`、`unpkg.com`、`fonts.googleapis.com`、`fonts.gstatic.com` 和 `fonts.bunny.net`。其他来源将被阻止并静默失败。

发布于 [2026 年 9 月 12 日](/2026/Sep/12/) 晚上 11:56 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
