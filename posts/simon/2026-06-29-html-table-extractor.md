# HTML table extractor

        **Date:** ...
        **Link:** https://simonwillison.net/2026/Jun/29/html-table-extractor/
        **Tags:** html, tools, wikipedia, cors

        ---

29th June 2026

[Tool](/elsewhere/tool/)
[HTML table extractor](https://tools.simonwillison.net/html-table-extractor)
— Extract tables from pasted content and convert them to multiple formats. Paste HTML, rich text, or plain text containing tables, and the tool automatically detects and displays each table with a preview, then allows you to export it as HTML, Markdown, CSV, TSV, or JSON. You can also import tables directly from Wikipedia by searching for page titles.

Yet another in my growing collection of paste-conversion tools. This one accepts pasted rich text from browsers (with embedded HTML tables) and converts every detected table into HTML, Markdown, CSV, TSV, or JSON.

Try it out by selecting everything on the Wikipedia [List of cities and towns in the San Francisco Bay Area](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_the_San_Francisco_Bay_Area) page and pasting it directly into the tool:

On a similar note, I recently [rebuilt](https://github.com/simonw/tools/commit/f278e977751dbc1948baedfc2f26b6de870f60e6) my [Rich text to markdown](https://tools.simonwillison.net/rich-text-to-markdown) tool to add support for tables and generally improve the UI.

**Update**: It turns out Wikipedia has an open CORS API for retrieving the full rendered HTML content of any page - [demo here](https://tools.simonwillison.net/cors-fetch#url=https%3A%2F%2Fen.wikipedia.org%2Fw%2Fapi.php%3Faction%3Dparse%26page%3DList_of_cities_and_towns_in_the_San_Francisco_Bay_Area%26prop%3Dtext%26format%3Djson%26origin%3D%2A) - so I [had Codex](https://gist.github.com/simonw/f226fe96f464ec7d81d6996cb466436d) add the ability to search Wikipedia for a page and then automatically import and display any tables from that page.

Posted [29th June 2026](/2026/Jun/29/) at 11:38 pm
