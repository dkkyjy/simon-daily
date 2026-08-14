import React from 'react';
import { Typewriter, Cursor } from 'animal-island-ui';

interface WelcomeScreenProps {
  onNavigate?: (comp: string) => void;
}

const WelcomeScreen: React.FC<WelcomeScreenProps> = () => {
  return (
    <div
      style={{
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: 40,
        textAlign: 'center',
      }}
    >
      <Cursor>
        <div style={{ fontSize: 64, lineHeight: 1, marginBottom: 16 }}>📖</div>
        <Typewriter speed={90}>
          <p
            style={{
              fontSize: 18,
              color: '#9f927d',
              lineHeight: 1.8,
              maxWidth: 400,
            }}
          >
            选择一篇文章开始阅读
          </p>
        </Typewriter>
      </Cursor>
    </div>
  );
};

export default WelcomeScreen;
