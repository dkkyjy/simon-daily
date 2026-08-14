import React, { useEffect, useState } from 'react';
import { Button, Divider, Cursor } from 'animal-island-ui';
import { fetchBilingualContent, fetchSummary, generateSummary, triggerTranslate, type Post, type BilingualContent } from '../api';
import MarkdownRenderer from './MarkdownRenderer';

interface PostViewProps {
  post: Post;
}

type ViewMode = 'bilingual' | 'summary';

const PostView: React.FC<PostViewProps> = ({ post }) => {
  const [view, setView] = useState<ViewMode>('bilingual');
  const [bilingual, setBilingual] = useState<BilingualContent | null>(null);
  const [summaryText, setSummaryText] = useState<string | null>(null);
  const [summaryLoading, setSummaryLoading] = useState(false);
  const [translating, setTranslating] = useState(false);

  useEffect(() => {
    setView('bilingual');
    setBilingual(null);
    setSummaryText(null);
    setSummaryLoading(false);
    setTranslating(false);
  }, [post.slug]);

  useEffect(() => {
    if (view === 'summary') {
      loadSummary();
    } else {
      loadBilingualContent();
    }
  }, [view, post.slug]);

  const loadBilingualContent = async () => {
    const data = await fetchBilingualContent(post.slug);
    setBilingual(data);
  };

  const loadSummary = async () => {
    setSummaryLoading(true);
    try {
      const data = await fetchSummary(post.slug);
      if (data.summary) {
        setSummaryText(data.summary);
      } else {
        setSummaryText(null);
      }
    } catch {
      setSummaryText(null);
    }
    setSummaryLoading(false);
  };

  const handleGenerateSummary = async () => {
    setSummaryLoading(true);
    try {
      const data = await generateSummary(post.slug);
      setSummaryText(data.summary);
    } catch {
      setSummaryText(null);
    }
    setSummaryLoading(false);
  };

  const handleTranslate = async () => {
    setTranslating(true);
    await triggerTranslate(post.slug);
    // Wait a moment then refresh
    setTimeout(async () => {
      setTranslating(false);
      // Re-fetch bilingual content
      await loadBilingualContent();
    }, 2000);
  };

  return (
    <div style={{ flex: 1, overflow: 'auto', padding: '32px 40px' }}>
      {/* Header: title + control buttons */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: 12,
          marginBottom: 24,
        }}
      >
        <h2
          style={{
            margin: 0,
            fontSize: 22,
            fontWeight: 700,
            color: '#794f27',
            lineHeight: 1.3,
          }}
        >
          {bilingual?.title || post.title}
        </h2>
        <Cursor>
          <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
            <div
              style={{
                margin: 0,
                opacity: view === 'bilingual' ? 1 : 0.6,
              }}
            >
              <Button
                type={view === 'bilingual' ? 'primary' : 'default'}
                size="small"
                onClick={() => setView('bilingual')}
              >
                双语
              </Button>
            </div>
            {!bilingual?.has_translation && (
              <Button
                type="default"
                size="small"
                loading={translating}
                onClick={handleTranslate}
                style={{ fontSize: 12 }}
              >
                {translating ? '翻译中...' : '翻译'}
              </Button>
            )}
            <div
              style={{
                margin: 0,
                opacity: view === 'summary' ? 1 : 0.6,
              }}
            >
              <Button
                type={view === 'summary' ? 'primary' : 'default'}
                size="small"
                onClick={() => setView('summary')}
              >
                摘要
              </Button>
            </div>
          </div>
        </Cursor>
      </div>

      <Divider />

      {view === 'summary' ? (
        <SummaryContent
          summary={summaryText}
          loading={summaryLoading}
          onGenerate={handleGenerateSummary}
        />
      ) : (
        <div
          style={{
            display: 'flex',
            gap: 16,
            marginTop: 16,
            minHeight: 400,
          }}
        >
          {/* Left: Original */}
          <div
            style={{
              flex: 1,
              width: '50%',
              maxWidth: '50%',
              overflowY: 'auto',
              paddingRight: 16,
              borderRight: '1px solid rgba(159,146,125,0.3)',
              color: '#5c4a32',
              lineHeight: 1.8,
              fontSize: 15,
            }}
          >
            <h3
              style={{
                fontSize: 14,
                fontWeight: 700,
                color: '#19c8b9',
                margin: '0 0 12px',
                textTransform: 'uppercase',
                letterSpacing: 1,
              }}
            >
              Original
            </h3>
            {bilingual ? (
              <MarkdownRenderer content={bilingual.orig} />
            ) : (
              <p style={{ color: '#9f927d', fontSize: 14 }}>Loading...</p>
            )}
          </div>

          {/* Right: Translation */}
          <div
            style={{
              flex: 1,
              width: '50%',
              maxWidth: '50%',
              overflowY: 'auto',
              paddingLeft: 16,
              color: '#5c4a32',
              lineHeight: 1.8,
              fontSize: 15,
            }}
          >
            <h3
              style={{
                fontSize: 14,
                fontWeight: 700,
                color: '#794f27',
                margin: '0 0 12px',
                textTransform: 'uppercase',
                letterSpacing: 1,
              }}
            >
              Translation
            </h3>
            {bilingual ? (
              bilingual.zh ? (
                <MarkdownRenderer content={bilingual.zh} />
              ) : (
                <p style={{ color: '#9f927d', fontSize: 14, fontStyle: 'italic' }}>
                  No translation available
                </p>
              )
            ) : (
              <p style={{ color: '#9f927d', fontSize: 14 }}>Loading...</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

const SummaryContent: React.FC<{
  summary: string | null;
  loading: boolean;
  onGenerate: () => void;
}> = ({ summary, loading, onGenerate }) => {
  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: 48 }}>
        <div
          style={{
            width: 32,
            height: 32,
            border: '3px solid #19c8b9',
            borderTopColor: 'transparent',
            borderRadius: '50%',
            animation: 'spin 0.8s linear infinite',
            margin: '0 auto 16px',
          }}
        />
        <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
        <p style={{ color: '#9f927d', fontSize: 14 }}>加载摘要...</p>
      </div>
    );
  }

  if (summary) {
    return (
      <div style={{ marginTop: 16 }}>
        <h3
          style={{
            fontSize: 16,
            fontWeight: 700,
            color: '#19c8b9',
            margin: '0 0 16px',
            display: 'flex',
            alignItems: 'center',
            gap: 8,
          }}
        >
          ✦ AI 摘要
        </h3>
        <MarkdownRenderer content={summary} />
        <p style={{ fontSize: 12, color: '#c4b89e', marginTop: 16 }}>
          摘要由 fabric-ai 自动生成
        </p>
      </div>
    );
  }

  return (
    <div style={{ textAlign: 'center', padding: 48 }}>
      <div style={{ fontSize: 32, marginBottom: 12, color: '#19c8b9' }}>✦</div>
      <p style={{ color: '#9f927d', fontSize: 14, marginBottom: 16 }}>
        尚未生成摘要
      </p>
      <Button type="primary" onClick={onGenerate}>
        生成 AI 摘要
      </Button>
    </div>
  );
};

export default PostView;
