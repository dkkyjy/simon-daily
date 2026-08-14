import React, { useEffect, useState, useCallback } from 'react';
import {
  Button,
  Card,
  Cursor,
  Typewriter,
  Input,
  Divider,
} from 'animal-island-ui';
import type { Source, Post } from './api';
import { fetchSources, fetchPosts } from './api';
import PostListItem from './components/PostListItem';
import PostView from './components/PostView';
import WelcomeScreen from './components/WelcomeScreen';

/* ─── 动森风格色彩令牌 ─── */
const COLORS = {
  primary: '#19c8b9',
  primaryHover: '#3dd4c6',
  text: '#794f27',
  textBody: '#725d42',
  textSecondary: '#9f927d',
  textMuted: '#c4b89e',
  bg: '#f8f8f0',
  bgContent: 'rgb(247, 243, 223)',
  bgDark: '#f0e8d8',
};

const App: React.FC = () => {
  const [sources, setSources] = useState<Source[]>([]);
  const [posts, setPosts] = useState<Post[]>([]);
  const [activeSource, setActiveSource] = useState<string>('all');
  const [activePost, setActivePost] = useState<Post | null>(null);
  const [search, setSearch] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchSources().then(setSources);
  }, []);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetchPosts(activeSource, search).then((data) => {
      if (!cancelled) {
        setPosts(data);
        setLoading(false);
      }
    });
    return () => { cancelled = true; };
  }, [activeSource, search]);

  const handleSearch = useCallback(() => {
    setLoading(true);
    fetchPosts(activeSource, search).then((data) => {
      setPosts(data);
      setLoading(false);
    });
  }, [activeSource, search]);

  const handleSourceChange = useCallback((key: string) => {
    setActiveSource(key);
    setActivePost(null);
  }, []);

  const handleSelectPost = useCallback((post: Post) => {
    setActivePost(post);
  }, []);

  return (
    <div
      style={{
        display: 'flex',
        height: '100vh',
        background: COLORS.bg,
        fontFamily: "'Nunito', 'Zen Maru Gothic', sans-serif",
        color: COLORS.text,
      }}
    >
      {/* ─── 左侧面板 ─── */}
      <div
        style={{
          width: 340,
          minWidth: 340,
          display: 'flex',
          flexDirection: 'column',
          borderRight: '2px solid rgba(159,146,125,0.2)',
          background: COLORS.bgDark,
        }}
      >
        {/* 标题 */}
        <div
          style={{
            padding: '18px 16px 12px',
            display: 'flex',
            alignItems: 'center',
            gap: 8,
          }}
        >
          <Cursor>
            <span style={{ fontSize: 22 }}>📰</span>
            <Typewriter speed={60}>
              <span
                style={{
                  fontSize: 18,
                  fontWeight: 700,
                  color: '#794f27',
                  letterSpacing: 1,
                }}
              >
                Daily Blog
              </span>
            </Typewriter>
          </Cursor>
        </div>

        <Divider />

        {/* 搜索 */}
        <div style={{ padding: '10px 12px', display: 'flex', gap: 6 }}>
          <div style={{ flex: 1 }}>
            <Input
              size="small"
              placeholder="搜索文章..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
            />
          </div>
          <Button type="primary" size="small" onClick={handleSearch}>
            🔍
          </Button>
        </div>

        {/* 源过滤器 */}
        <div
          style={{
            display: 'flex',
            flexWrap: 'wrap',
            gap: 6,
            padding: '0 12px 10px',
          }}
        >
          <Button
            type={activeSource === 'all' ? 'primary' : 'default'}
            size="small"
            onClick={() => handleSourceChange('all')}
          >
            全部
          </Button>
          {sources.map((s) => (
            <Button
              key={s.key}
              type={activeSource === s.key ? 'primary' : 'default'}
              size="small"
              onClick={() => handleSourceChange(s.key)}
            >
              {s.name}
            </Button>
          ))}
        </div>

        <Divider />

        {/* 文章列表 */}
        <div style={{ flex: 1, overflowY: 'auto', padding: '8px 10px' }}>
          {loading ? (
            <div
              style={{
                textAlign: 'center',
                padding: 40,
                color: COLORS.textSecondary,
                fontSize: 14,
              }}
            >
              <div
                style={{
                  width: 28,
                  height: 28,
                  border: '3px solid #19c8b9',
                  borderTopColor: 'transparent',
                  borderRadius: '50%',
                  animation: 'spin 0.8s linear infinite',
                  margin: '0 auto 12px',
                }}
              />
              加载中...
              <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
            </div>
          ) : posts.length === 0 ? (
            <div
              style={{
                textAlign: 'center',
                padding: 40,
                color: COLORS.textMuted,
                fontSize: 14,
              }}
            >
              🌿 暂无文章
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
              {posts.map((post) => (
                <PostListItem
                  key={post.slug}
                  post={post}
                  isActive={activePost?.slug === post.slug}
                  onClick={() => handleSelectPost(post)}
                />
              ))}
            </div>
          )}
        </div>

        {/* 底部信息 */}
        <div
          style={{
            padding: '8px 14px',
            fontSize: 11,
            color: COLORS.textMuted,
            borderTop: '1px solid rgba(159,146,125,0.15)',
            textAlign: 'center',
            background: 'rgba(248,248,240,0.5)',
          }}
        >
          <Cursor>🎮 Daily Blog Reader</Cursor>
        </div>
      </div>

      {/* ─── 右侧主内容 ─── */}
      <div
        style={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden',
          background: COLORS.bg,
        }}
      >
        {activePost ? (
          <div
            style={{
              flex: 1,
              overflowY: 'auto',
              padding: '24px 28px',
            }}
          >
            <PostView post={activePost} />
          </div>
        ) : (
          <WelcomeScreen />
        )}
      </div>
    </div>
  );
};

export default App;
