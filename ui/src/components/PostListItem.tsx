import React from 'react';
import { Card } from 'animal-island-ui';
import type { Post } from '../api';

interface PostListItemProps {
  post: Post;
  isActive: boolean;
  onClick: () => void;
}

const PostListItem: React.FC<PostListItemProps> = ({ post, isActive, onClick }) => {
  return (
    <div onClick={onClick} style={{ cursor: 'pointer' }}>
      <Card
        color={isActive ? 'warm-peach-pink' : 'default'}
        style={{
          padding: '10px 14px',
          transition: 'all 0.15s',
          opacity: isActive ? 1 : 0.85,
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: 8,
          }}
        >
          <div style={{ flex: 1, minWidth: 0 }}>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 6,
                marginBottom: 2,
              }}
            >
              <span
                style={{
                  fontSize: 11,
                  fontWeight: 600,
                  padding: '1px 8px',
                  borderRadius: 8,
                  background: '#e6f9f6',
                  color: '#19c8b9',
                }}
              >
                {post.source_name}
              </span>
              <span style={{ fontSize: 11, color: '#c4b89e' }}>{post.date}</span>
            </div>
            <div
              style={{
                fontSize: 13,
                fontWeight: 600,
                color: isActive ? '#794f27' : '#9f927d',
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
              }}
            >
              {post.title}
            </div>
          </div>
          <div style={{ display: 'flex', gap: 4, flexShrink: 0 }}>
            {post.has_translation && (
              <span title="已有中文翻译" style={{ fontSize: 12, color: '#6fba2c' }}>
                🈶
              </span>
            )}
            {post.has_summary && (
              <span title="已有摘要" style={{ fontSize: 12, color: '#19c8b9' }}>
                ✦
              </span>
            )}
          </div>
        </div>
      </Card>
    </div>
  );
};

export default PostListItem;
