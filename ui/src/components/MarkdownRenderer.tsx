import React, { useMemo } from 'react';

interface MarkdownRendererProps {
  content: string;
}

/**
 * Line-by-line markdown to HTML renderer.
 * Ported from the vanilla JS implementation in server.py.
 */
const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({ content }) => {
  const html = useMemo(() => renderMarkdown(content), [content]);
  return <div className="prose" dangerouslySetInnerHTML={{ __html: html }} />;
};

function inline(m: string): string {
  return m
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\*([^*]+)\*/g, '<em>$1</em>')
    .replace(
      /!\[([^\]]*)\]\(([^)]+)\)/g,
      '<img src="$2" alt="$1" class="max-w-full rounded-lg my-2" />',
    )
    .replace(
      /\[([^\]]+)\]\(([^)]+)\)/g,
      '<a href="$2" class="text-blue-600 underline" target="_blank" rel="noopener noreferrer">$1</a>',
    );
}

function renderMarkdown(md: string): string {
  const lines = md.split('\n');
  let html = '';
  let inCodeBlock = false;
  let codeLang = '';
  let codeBuf: string[] = [];
  let inBlockquote = false;
  let bqBuf: string[] = [];
  let pBuf: string[] = [];

  const flushP = () => {
    if (pBuf.length) {
      html += `<p class="mb-3 leading-relaxed">${inline(pBuf.join('\n'))}</p>\n`;
      pBuf = [];
    }
  };
  const flushBQ = () => {
    if (bqBuf.length) {
      html += `<blockquote class="border-l-4 border-gray-300 pl-4 italic my-2">${inline(bqBuf.join('<br>'))}</blockquote>\n`;
      bqBuf = [];
      inBlockquote = false;
    }
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (/^```/.test(line)) {
      flushP();
      flushBQ();
      if (!inCodeBlock) {
        inCodeBlock = true;
        codeLang = line.slice(3).trim();
        codeBuf = [];
      } else {
        html += `<pre class="overflow-x-auto p-4 rounded-lg" style="background:#2b2118;color:#e8d5bc"><code${codeLang ? ` class="language-${codeLang}"` : ''}>${codeBuf.join('\n').replace(/</g, '&lt;').replace(/>/g, '&gt;')}</code></pre>\n`;
        inCodeBlock = false;
      }
      continue;
    }
    if (inCodeBlock) {
      codeBuf.push(line);
      continue;
    }

    const hMatch = line.match(/^(#{1,3})\s+(.+)/);
    if (hMatch) {
      flushP();
      flushBQ();
      const level = hMatch[1].length;
      const cls = ['text-2xl font-bold mt-6 mb-3', 'text-xl font-semibold mt-5 mb-2', 'text-lg font-semibold mt-4 mb-2'][level - 1];
      html += `<h${level} class="${cls}">${inline(hMatch[2])}</h${level}>\n`;
      continue;
    }

    if (/^---$/.test(line.trim())) {
      flushP();
      flushBQ();
      html += '<hr class="my-4" />\n';
      continue;
    }

    const bqMatch = line.match(/^>\s*(.*)/);
    if (bqMatch) {
      flushP();
      inBlockquote = true;
      bqBuf.push(bqMatch[1]);
      continue;
    } else if (inBlockquote) {
      flushBQ();
    }

    if (line.trim() === '') {
      flushP();
      continue;
    }

    pBuf.push(line);
  }
  flushP();
  flushBQ();
  return html;
}

export default MarkdownRenderer;
