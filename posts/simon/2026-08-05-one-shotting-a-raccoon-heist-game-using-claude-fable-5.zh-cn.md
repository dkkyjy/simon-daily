# 使用 Claude Fable 5 一次性打造“浣熊大劫案”游戏

        **日期：** 2026-08-05 19:42 UTC
        **链接：** https://simonwillison.net/2026/Aug/5/raccoon-heist/#atom-everything
        **标签：** game-design, ai, prompt-engineering, generative-ai, llms, anthropic, claude, text-to-image, vibe-coding, coding-agents, claude-mythos-fable

        ---

        > *提要摘要：2024年，我发布了一条推文，展示了由 GPT-3 生成的一个游戏概念截图，以及使用 DALL-E 创作的一些概念“艺术”。今天，在那条推文四周年之际，我决定看看 Claude Fable 5 *

## 使用 Claude Fable 5 一次性打造“浣熊大劫案”游戏

2026年8月5日

早在2024年，[我发推文](https://twitter.com/simonw/status/1555626060384911360)展示了由 GPT-3 生成的一个游戏概念截图，以及使用 DALL-E 创作的一些概念“艺术”。今天，在那条推文四周年之际，我决定看看 Claude Fable 5（在 [Claude Code for web](https://code.claude.com/docs/en/claude-code-on-the-web) 中运行）能否仅凭那条推文的内容构建出整个游戏。它做得相当不错！

你可以[在这里玩游戏](https://simonw.github.io/raccoon-heist/)。这是[GitHub 仓库](https://github.com/simonw/raccoon-heist/)，以及一段简短视频演示：

[![

您的浏览器不支持 HTML5 视频。
](https://static.simonwillison.net/static/2026/raccoon-heist-poster.jpg)](https://static.simonwillison.net/static/2026/raccoon-heist-720p.mp4)

#### 我是如何构建这个的

这是[2022年8月5日的推文](https://twitter.com/simonw/status/1555626060384911360)：

我当时对 GPT-3 的提示是：

> `为一款浣熊团队实施抢劫的电脑游戏撰写详细的产品描述。`

那是在文本补全时代，你要求 GPT-3 补全剩余文本。它补全为：

> 在“浣熊大劫案”中，你和你的浣熊窃贼团队的任务是实施一系列大胆的抢劫。从抢劫银行到窃取无价艺术品，对于你的毛茸茸团队来说，没有太大或太小的任务。你需要运用智慧和技能来躲避警察，并带着赃物干净利落地逃脱。凭借激动人心的玩法和迷人的角色阵容，“浣熊大劫案”是任何寻求轻松诙谐冒险的人的完美游戏。

我给 DALL-E 的提示很简短：

> `一款浣熊团队实施抢劫的视频游戏截图`

今天的实验：我能否将这些截图连同提示一起交给 Fable 5，告诉它编写一个游戏，然后让它自行发挥，最终得到一个可运行的游戏？

#### 设置 Claude Code for web 以使用 GitHub Pages

Claude Code for web 的一个令人沮丧的地方在于，当它还在工作时，很难测试它正在构建的内容。

我一直在使用 GitHub Pages 来解决这个限制，并且发现它效果很好。

以下是我的流程：

1. 在 <https://github.com/new> 为项目创建一个新仓库——可以是公开或私有的，这个方法对两者同样有效。
2. 在 Claude iPhone 或桌面应用中，或在浏览器中访问 <https://claude.ai/code>，启动一个 Claude Code for web 会话。
3. 告诉 Claude 要做什么，并鼓励它尽快提交一个 `index.html` 页面。这将创建一个类似 `claude/3d-raccoon-heist-game-50n293` 的分支。
4. 导航到仓库的“设置”->“Pages”区域（在我的情况下是 `github.com/simonw/raccoon-heist/settings/pages`），选择“从分支部署”，选择分支名称，然后点击“保存”。

就这么简单！每次推送后大约30秒内，最新内容就会在 `yourname.github.io/your-repo/` 可见。

如果你使用私有仓库执行此操作，任何能猜到仓库名称的人都能查看已发布的内容。我个人对此不太担心。

#### Fable 5 提示

以下是我给 Fable 5 的提示（用手机上的笔记应用编写——整个项目都是在移动端进行的）。我附上了原始推文中的两张图片。

> `构建这个3D游戏，用于浏览器。`
>
> `此仓库配置为提供静态文件，因此请确保有一个 index.html 来加载所有其他内容。`
>
> `确保它适合移动设备（触摸控制，在小屏幕上运行良好）。`
>
> `你有一个 OpenAI API 密钥，可以访问他们的图像生成模型 API，请将其用于生成 3D 模型所需的纹理。文档在此：https://developers.openai.com/api/docs/guides/image-generation - 使用 gpt-image-2`
>
> `独立工作——不要让我做任何进一步的设计决策。确保游戏有趣、有点惊喜、有良好的浣熊抢劫氛围，并且视觉上令人愉悦。`
>
> `尽可能频繁地提交和推送，以便我可以预览你的工作——从提供一个标题画面的 index.html 开始，然后在此基础上构建。`
>
> `在工作时追加到 notes.md 文件中，并将对该文件的更改包含在每次提交中。`

我没有做任何技术选择。我（正确地）假设根据之前的实验，它可能会使用 [Three.js](https://threejs.org/)。

让 Claude 访问 OpenAI 密钥，事实证明在填补其能力空白方面效果很好——在这种情况下，我们需要某种方式来生成用作纹理的图像。Fable 非常擅长提示图像生成器！

我说“独立工作——不要让我做任何进一步的设计决策”，因为我想看看它能否在不需要我进一步输入的情况下，制作出一个完整、可运行的游戏。

我还说了“尽可能频繁地提交和推送，以便我可以预览你的工作”。当你在 Claude iPhone 应用中使用 Claude Code 时，你给它一个 GitHub 仓库，它会在一个分支中工作。告诉它“尽可能频繁地推送”意味着提交会立即开始落到该分支中。

我喜欢要求 `notes.md` 作为一点额外的风味——这是[最终文件](https://github.com/simonw/raccoon-heist/blob/main/notes.md)，以及它添加狗时所做的记录：

> 新的升级：从第3晚开始，院子里会出现一只巡逻的护卫犬——一只低多边形棕色猎犬，戴着带尖刺的红色项圈，尾巴摇摆。它在随机地点之间游荡，在12个单位内它会闻到你的气味并通过嗅觉追踪你（视线无关紧要——全靠鼻子，头顶显示👃并吠叫）。如果你拉开17个单位的距离，它就会放弃。被抓到的消息现在按来源区分：警卫 / 车头灯 / 猎犬。通过自动化测试验证了游荡 → 追踪 → 被抓的流程。

#### 查看记录

你可以访问 [Claude Code 共享会话](https://claude.ai/code/session_01NUBoCfnhGETcCDyEUPS8jp)，我还使用我的 [claude-code-transcripts](https://github.com/simonw/claude-code-transcripts) 工具导出了我自己的 HTML 版本，你可以在[这里找到](https://simonw.github.io/raccoon-heist/transcript/page-001.html)。

Fable 从一个索引页面开始，[内置了一份](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T14-55-13-304Z) Three.js 的副本，然后编写了自己的 [gen\_textures.py 脚本](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T14-55-49-064Z)（[副本在此](https://github.com/simonw/raccoon-heist/blob/main/gen_textures.py)）。

它生成了纹理并[抽查了它们](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T14-59-07-900Z)以确保看起来不错。它为垃圾桶生成的 [metal.jpg 文件](https://github.com/simonw/raccoon-heist/blob/main/textures/metal.jpg) 看起来像这样，尽管我认为它在游戏本身中的应用并不完全正确：然后它构建了游戏的第一版基础版本，然后[决定](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-04-51-625Z)使用 Playwright 在“预装的 Chromium 中进行冒烟测试”。这意味着它可以截取自己工作的截图并[目测检查](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-05-53-823Z)。它对页面的桌面和移动宽度都这样做了，然后注意到[浣熊在移动宽度下不可见](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-09-33-406Z)，于是它[修复了这个问题](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-14-39-180Z)：

> 浣熊、垃圾箱藏身处以及两只队员浣熊现在在移动端完全可见。提交此关键修复。

它决定生成一个标题画面，[它这样做了](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-15-02-574Z)，使用的是这个 [gen\_title.py](https://github.com/simonw/raccoon-heist/blob/main/gen_title.py) 脚本。以下是它为此使用的 `gpt-image-2` 提示：

> `视频游戏主视觉图，低多边形3D渲染风格，情绪化的夜晚场景：一只可爱的低多边形浣熊戴着小小的黑色盗贼面具，用后腿偷偷摸摸地行走，携带一枚发光的金币，旁边是一个被推倒的金属垃圾桶，背景是带有温暖发光窗户的郊区房屋，深蓝色夜晚，满月，萤火虫，电影般的轮廓光，迷人的抢劫冒险氛围。无文字，无单词，无标志。`

以及生成的图像（Claude 认为它[“华丽”](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-16-42-176Z)）——尽管我注意到在桌面上显示时，它会被裁剪到只有顶部三分之一，浣熊不见了！

然后是我最喜欢的改动：它[添加了狗](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-23-00-850Z)：

 function makeDog() {
  const g = new THREE.Group();
  const BROWN = 0x8a6440, DARK = 0x5e4128;
  const body = new THREE.Mesh(new THREE.SphereGeometry(0.42, 10, 8), M(BROWN));
  body.scale.set(0.9, 0.8, 1.5);
  body.position.y = 0.55;
  body.castShadow = true;
  g.add(body);
  const head = new THREE.Mesh(new THREE.SphereGeometry(0.3, 10, 8), M(BROWN));
  head.position.set(0, 0.85, 0.62);
  g.add(head);
  const snout = new THREE.Mesh(new THREE.SphereGeometry(0.16, 8, 6), M(DARK));
  snout.scale.set(0.9, 0.7, 1.3);
  snout.position.set(0, 0.76, 0.9);
  g.add(snout);
  const nose = new THREE.Mesh(new THREE.SphereGeometry(0.06, 6, 6), M(BLACK));
  nose.position.set(0, 0.78, 1.08);
  g.add(nose);
  for (const s of [-1, 1]) {
    const ear = new THREE.Mesh(new THREE.SphereGeometry(0.12, 6, 6), M(DARK));
    ear.scale.set(0.7, 1.3, 0.5);
    ear.position.set(0.2 * s, 1.08, 0.55);
    g.add(ear);
    const eye = new THREE.Mesh(new THREE.SphereGeometry(0.05, 6, 6), M(0x1a1a1a, { emissive: 0x331111 }));
    eye.position.set(0.13 * s, 0.92, 0.86);
    g.add(eye);
  }
  const tail = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.09, 0.5, 6), M(DARK));
  tail.position.set(0, 0.8, -0.62);
  tail.rotation.x = 0.8;
  g.add(tail);
  // spiked collar
  const collar = new THREE.Mesh(new THREE.TorusGeometry(0.22, 0.05, 6, 12), M(0xc0392b));
  collar.position.set(0, 0.78, 0.5);
  collar.rotation.x = Math.PI / 2.4;
  g.add(collar);
  const legGeo = new THREE.CylinderGeometry(0.07, 0.09, 0.34, 6);
  const legs = [];
  for (const [x, z] of [[-0.22, 0.35], [0.22, 0.35], [-0.22, -0.35], [0.22, -0.35]]) {
    const leg = new THREE.Mesh(legGeo, M(DARK));
    leg.position.set(x, 0.17, z);
    g.add(leg);
    legs.push(leg);
  }
  let phase = Math.random() * 10;
  return {
    group: g,
    animate(dt, speed) {
      phase += dt * (3 + speed * 10);
      const amp = Math.min(0.6, 0.1 + speed * 0.6);
      legs[0].rotation.x = Math.sin(phase) * amp;
      legs[3].rotation.x = Math.sin(phase) * amp;
      legs[1].rotation.x = -Math.sin(phase) * amp;
      legs[2].rotation.x = -Math.sin(phase) * amp;
      tail.rotation.z = Math.sin(phase * 1.5) * 0.4;
      body.position.y = 0.55 + Math.abs(Math.sin(phase)) * 0.04 * (0.3 + speed);
    },
  };
}
```

并且使用 Playwright 对它进行了[一轮测试](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-24-09-230Z)，包括[另一张截图](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-24-33-559Z)。

```
  // walk near the dog
  await page.evaluate(() => { const d = window.__rh.dog; window.__rh.teleport(d.x + 6, d.z); });
  await page.waitForTimeout(2000);
  info = await page.evaluate(() => JSON.stringify({ dog: window.__rh.dog, state: window.__rh.state, player: window.__rh.debug().player }));
  console.log('after approach:', info);
  await page.waitForTimeout(3000);
  info = await page.evaluate(() => JSON.stringify({ dog: window.__rh.dog, state: window.__rh.state }));
  console.log('after chase:', info);
  await page.screenshot({ path: __dirname + '/shot-dog.png' });
```

它又做了几处调整，然后[宣布完成](https://simonw.github.io/raccoon-heist/transcript/page-001.html#msg-2026-08-05T15-29-13-245Z)：

> **Raccoon Heist 已构建、测试并推送** — 在 `claude/3d-raccoon-heist-game-50n293` 分支上共 7 次提交，全部通过桌面端、竖屏手机端和横屏手机端的自动化 Playwright 试玩验证。
>
> **游戏内容：** 你是一只戴着面具的浣熊，从同伴的垃圾箱藏身处溜出，进入一个月光下的死胡同。收集硬币、宝石、戒指、甜甜圈和鱼（它们会堆叠在你的背上并减慢你的速度），然后在黎明前摇摇晃晃地回家存入银行。每晚都会提高目标和热度：第一晚有一个持手电筒巡逻的守卫，第二晚有两个，第三晚增加了一只完全无视视线追踪气味的猎犬。一辆警车用前灯扫过街道，房主会随机从窗户向外张望，一只海鸥会定期俯冲轰炸你未认领的战利品，披萨片会触发 6 秒的速度狂潮，而一台稀有的金色电视价值 120 分，前提是你能把它拖回家。胜利等级：垃圾熊猫 ⭐ → 飞贼 ⭐⭐ → 伪装大师 ⭐⭐⭐，你的最佳成绩会保存到 localStorage。
>
> **构建方式：** 内置 Three.js（无 CDN），程序化生成的低多边形角色，以及程序化的 WebAudio 配乐（鬼鬼祟祟的行走贝斯爵士乐加上所有音效 — 零音频文件）。所有七种地面/墙壁纹理和标题画面主视觉均使用 gpt-image-2 生成并作为静态资源提交，因此部署后的游戏不会发起任何 API 调用。移动端配备动态触摸摇杆（出现在你触摸的任何位置）以及 DASH 按钮；桌面端使用 WASD/方向键和空格键。
>
> **测试发现了两个值得提及的真实 bug：** 画布在任何真实手机上以 2 倍大小渲染（一个 `cssText` 赋值语句清除了 Three.js 的内联尺寸 — 桌面端 DPR-1 测试完全掩盖了这个问题），以及胜利画面的星级评分 div 继承了标题画面的全屏 `.stars` CSS，静默吞掉了“下一夜”按钮上的每次点击。这两个问题都已修复并通过回归测试，同时涵盖拾取、存入、追逐/被抓、黎明、夜间推进以及失败/重试流程。
>
> `notes.md` 中有完整的构建日志。游戏已在分支上运行 — 只需托管仓库根目录并打开 `index.html`。

#### 这游戏好玩吗？

这是一个令人印象深刻的起点，但它不是一个*好*游戏。

你在院子里移动浣熊收集物品——甜甜圈、鱼、金币、珠宝——同时避开拿着手电筒的守卫，在后面的关卡中还要避开狗。你的携带能力有限，一旦装满，你需要把东西放到垃圾箱。如果你捡起一片披萨，你会获得暂时的速度提升。

完全没有团队机制——垃圾箱旁边有两只静态的浣熊，但它们纯粹是装饰。

随着关卡推进，难度略有增加——第 3 关引入的狗是最有趣的新机制——但通关非常非常容易。而且相当无聊——每晚有固定的时长，你可以收集所有物品，然后在等待黎明时无事可做。

我对实现印象深刻。它完全是 3D 的，有垃圾桶，手电筒的照明锥很有趣，而且视觉风格相当连贯。它可以在移动端运行。音乐（根据 Claude 的说法，“程序化的 WebAudio 配乐（鬼鬼祟祟的行走贝斯爵士乐加上所有音效 — 零音频文件）”）很简单，但感觉恰到好处。

作为一个完成的游戏项目，它很平庸。作为从一个提示词出发的起点，我认为它非常令人印象深刻。

我现在已经用 vibe coding 做了好几个游戏。从游戏性的角度来看，它们都令人深感失望——事实证明，设计*有趣*的游戏仍然是一种独特的人类特质，并且需要比 Claude 或我所能带来的更多的技能和经验。

话虽如此，我强烈推荐尝试游戏开发项目，作为探索智能体能力的一种方式。这是一种有趣、低风险的尝试新事物的方式。如果你坚持足够长的时间，你甚至可能做出值得一玩的东西！

发布于 [2026年8月5日](/2026/Aug/5/) 晚上 7:42 · 在 [Mastodon](https://fedi.simonwillison.net/@simon)、[Bluesky](https://bsky.app/profile/simonwillison.net)、[Twitter](https://twitter.com/simonw) 上关注我，或[订阅我的通讯](https://simonwillison.net/about/#subscribe)
