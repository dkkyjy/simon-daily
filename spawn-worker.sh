#!/usr/bin/env bash
# spawn-worker.sh — 派一个独立的 claude -p 从属 worker,结果写到文件(文件信箱)
# 用法:
#   ./spawn-worker.sh "你的指令"              # 后台派发,立即返回 pid + 输出文件路径
#   ./spawn-worker.sh "你的指令" --wait       # 前台等待,跑完打印 exit code + 结果
set -euo pipefail

TASK="${1:?用法: spawn-worker.sh \"指令\" [--wait]}"
CLAUDE_BIN="$(command -v claude || echo "$HOME/.local/bin/claude")"
TS="$(date +%Y%m%d-%H%M%S.$$)"
OUT="/tmp/worker_${TS}.out"
ERR="/tmp/worker_${TS}.err"

if [ "${2:-}" = "--wait" ]; then
  "$CLAUDE_BIN" -p --dangerously-skip-permissions "$TASK" >"$OUT" 2>"$ERR"
  code=$?
  echo "exit=$code out=$OUT err=$ERR"
  if [ -s "$OUT" ]; then
    echo "--- result ---"
    cat "$OUT"
  fi
  exit "$code"
else
  "$CLAUDE_BIN" -p --dangerously-skip-permissions "$TASK" >"$OUT" 2>"$ERR" &
  echo "pid=$! out=$OUT err=$ERR"
fi