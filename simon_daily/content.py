"""HTTP content fetching and HTML-to-Markdown conversion."""
import re
import sys

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert


def fetch_article_content(url):
    """Fetch full article HTML and convert to markdown."""
    try:
        resp = requests.get(url, timeout=15, headers={
            "User-Agent": "Mozilla/5.0 (compatible; simon-daily/1.0)"
        })
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Try various content selectors
        article = (
            soup.find("article", class_="post")
            or soup.find("article")
            or soup.find("main")
            or soup.find("div", class_="content")
            or soup.find("div", class_="entry-content")
            or soup.find("div", class_="post-content")
            or soup.find("div", class_="entry")
        )
        if not article:
            article = soup.find("body")

        # Remove unwanted elements
        for tag in article.find_all(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        html_content = str(article)
        markdown = md_convert(html_content, heading_style="ATX", strip=["img", "figure"])
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        markdown = markdown.strip()
        return markdown
    except Exception as e:
        print(f"  [WARN] Failed to fetch article content: {e}", file=sys.stderr)
        return None
