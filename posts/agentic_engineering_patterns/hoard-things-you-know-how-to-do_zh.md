指南 > 智能体工程模式
积攒你已知如何完成的事情
我关于如何高效使用编码智能体的许多建议，都延伸自我在没有它们时职业生涯中觉得有用的建议。这里有一个很好的例子：积攒你已知如何完成的事情。
构建软件技能的一个重要部分是理解什么是可能的、什么是不可能的，并且至少对这些事情如何完成有一个粗略的概念。
这些问题可能很宽泛，也可能相当冷僻。一个网页能否仅用 JavaScript 运行 OCR 操作？iPhone 应用能否在未运行时与蓝牙设备配对？我们能否在 Python 中处理一个 100GB 的 JSON 文件，而无需先将整个文件加载到内存中？
你掌握的这类问题的答案越多，你就越有可能发现机会，以他人可能尚未想到的方式运用技术来解决问题。
对这些问题的答案保持信心的最佳方式，是通过运行代码看到它们被实际演示。知道某事在理论上可行，与亲眼看到它被完成是不同的。作为软件专业人士，需要培养的一项关键资产就是针对此类问题的大量答案集合，并附有这些答案的证明。
我通过多种不同的方式积攒这类解决方案。我的博客和 TIL 博客里塞满了关于我如何弄明白做某事的笔记。我有一千多个 GitHub 仓库，收集了为不同项目编写的代码，其中许多是展示关键想法的小型概念验证。
最近，我开始使用 LLM 来帮助扩展我对有趣问题的代码解决方案集合。
tools.simonwillison.net 是我最大的 LLM 辅助工具和原型集合。我用它来收集我称之为 HTML 工具的东西——即嵌入 JavaScript 和 CSS 并解决特定问题的单个 HTML 页面。
我的 simonw/research 仓库有更大、更复杂的例子，在那里我挑战一个编码智能体去研究一个问题，并带回可运行的代码和一份详细说明其发现的书面报告。
重组你积攒的东西
为什么要收集所有这些材料？除了帮助你构建和扩展自己的能力之外，你在此过程中生成的资产将成为你的编码智能体的强大输入。
我最喜欢的提示模式之一是，告诉一个智能体通过组合两个或多个现有的工作示例来构建新东西。
一个帮助我明确认识到这种方法能有多有效的项目，是我添加到工具集合中的第一个东西——一个基于浏览器的 OCR 工具，更详细的描述在这里。
我想要一个简单、基于浏览器的工具，用于对 PDF 文件中的页面进行 OCR——特别是那些完全由扫描图像组成、完全没有提供文本版本的 PDF。
我之前尝试过在浏览器中运行 Tesseract.js OCR 库，发现它功能非常强大。该库提供了成熟的 Tesseract OCR 引擎的 WebAssembly 构建版本，让你可以从 JavaScript 调用它来从图像中提取文本。
但我不想处理图像，我想处理 PDF。然后我想起我也用过 Mozilla 的 PDF.js 库，它除了其他功能外，还可以将 PDF 的单个页面转换为渲染后的图像。
我的笔记里有这两个库的 JavaScript 代码片段。
以下是我输入到模型（当时是 Claude 3 Opus）的完整提示，结合了我的两个例子并描述了我正在寻找的解决方案：
这段代码展示了如何打开 PDF 并将其转换为每页一张图像：
```html
<!DOCTYPE html>
<html>
<head>
  <title>PDF to Images</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.9.359/pdf.min.js"></script>
  <style>
    .image-container img {
      margin-bottom: 10px;
    }
    .image-container p {
      margin: 0;
      font-size: 14px;
      color: #888;
    }
  </style>
</head>
<body>
  <input type="file" id="fileInput" accept=".pdf" />
  <div class="image-container"></div>
  <script>
  const desiredWidth = 800;
    const fileInput = document.getElementById('fileInput');
    const imageContainer = document.querySelector('.image-container');
    fileInput.addEventListener('change', handleFileUpload);
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.9.359/pdf.worker.min.js';
    async function handleFileUpload(event) {
      const file = event.target.files[0];
      const imageIterator = convertPDFToImages(file);
      for await (const { imageURL, size } of imageIterator) {
        const imgElement = document.createElement('img');
        imgElement.src = imageURL;
        imageContainer.appendChild(imgElement);
        const sizeElement = document.createElement('p');
        sizeElement.textContent = `Size: ${formatSize(size)}`;
        imageContainer.appendChild(sizeElement);
      }
    }
    async function* convertPDFToImages(file) {
      try {
        const pdf = await pdfjsLib.getDocument(URL.createObjectURL(file)).promise;
        const numPages = pdf.numPages;
        for (let i = 1; i <= numPages; i++) {
          const page = await pdf.getPage(i);
          const viewport = page.getViewport({ scale: 1 });
          const canvas = document.createElement('canvas');
          const context = canvas.getContext('2d');
          canvas.width = desiredWidth;
          canvas.height = (desiredWidth / viewport.width) * viewport.height;
          const renderContext = {
            canvasContext: context,
            viewport: page.getViewport({ scale: desiredWidth / viewport.width }),
          };
          await page.render(renderContext).promise;
          const imageURL = canvas.toDataURL('image/jpeg', 0.8);
          const size = calculateSize(imageURL);
          yield { imageURL, size };
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
    function calculateSize(imageURL) {
      const base64Length = imageURL.length - 'data:image/jpeg;base64,'.length;
      const sizeInBytes = Math.ceil(base64Length * 0.75);
      return sizeInBytes;
    }
    function formatSize(size) {
      const sizeInKB = (size / 1024).toFixed(2);
      return `${sizeInKB} KB`;
    }
  </script>
</body>
</html>
```
这段代码展示了如何对图像进行 OCR：
```javascript
async function ocrMissingAltText() {
    // Load Tesseract
    var s = document.createElement("script");
    s.src = "https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js";
    document.head.appendChild(s);
    s.onload = async () => {
      const images = document.getElementsByTagName("img");
      const worker = Tesseract.createWorker();
      await worker.load();
      await worker.loadLanguage("eng");
      await worker.initialize("eng");
      ocrButton.innerText = "Running OCR...";
      // Iterate through all the images in the output div
      for (const img of images) {
        const altTextarea = img.parentNode.querySelector(".textarea-alt");
        // Check if the alt textarea is empty
        if (altTextarea.value === "") {
          const imageUrl = img.src;
          var {
            data: { text },
          } = await worker.recognize(imageUrl);
          altTextarea.value = text; // Set the OCR result to the alt textarea
          progressBar.value += 1;
        }
      }
      await worker.terminate();
      ocrButton.innerText = "OCR complete";
    };
  }
```
使用这些示例来组合一个包含嵌入式 HTML、CSS 和 JavaScript 的单个 HTML 页面，该页面提供一个大的方形区域，用户可以将 PDF 文件拖放到上面，当他们这样做时，PDF 的每一页都被转换为 JPEG 并显示在页面下方，然后使用 tesseract 运行 OCR，结果以文本区域块的形式显示在每个图像下方。
这完美地运行了！模型输出了一个概念验证页面，完全满足了我的需求。
我最终与它进行了几次迭代以达到最终结果，但只花了几分钟就构建了一个真正有用的工具，从那以后我一直受益于此。
编码智能体使这更加强大
我在 2024 年 3 月构建了那个 OCR 示例，那是在 Claude Code 首次发布近一年前。编码智能体使得积攒工作示例变得更有价值。
如果你的编码智能体可以访问互联网，你可以告诉它做这样的事情：
使用 curl 获取 `https://tools.simonwillison.net/ocr` 和 `https://tools.simonwillison.net/gemini-bbox` 的源代码，并构建一个新工具，让你可以从 PDF 中选择一个页面并将其传递给 Gemini，以返回该页面上插图的边界框。
（我在那里指定了 curl，因为 Claude Code 默认使用 WebFetch 工具，该工具会总结页面内容而不是返回原始 HTML。）
编码智能体非常擅长搜索，这意味着你可以在自己的机器上运行它们，并告诉它们在哪里可以找到你希望它们做的事情的示例：
向 `~/dev/ecosystem/datasette-oauth` 项目添加模拟 HTTP 测试，灵感来自 `~/dev/ecosystem/llm-mistral` 项目的做法。
通常这就足够了——智能体会启动一个搜索子智能体进行调查，并仅提取完成任务所需的细节。
由于我的许多研究代码都是公开的，我经常告诉编码智能体将我的仓库克隆到 /tmp 并将其用作输入：
将 `simonw/research` 从 GitHub 克隆到 `/tmp`，并找到将 Rust 编译为 WebAssembly 的示例，然后使用它为此项目构建一个演示 HTML 页面。
这里的关键思想是，编码智能体意味着我们只需要弄清楚一次有用的技巧。如果这个技巧随后在某个地方有文档记录并附有工作代码示例，我们的智能体就可以参考该示例，并用它来解决未来任何类似形态的项目。