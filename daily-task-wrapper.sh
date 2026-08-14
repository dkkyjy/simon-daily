#!/bin/bash
# Wrapper for daily task cron job - sets up proper environment
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"
export SHELL="/bin/bash"
cd /Users/dkk/storage/github/simon-daily

# Log file
LOG="/tmp/daily-task-$(date +%Y%m%d).log"

echo "===== Daily Task: $(date) =====" >> "$LOG"
python3 daily_task.py --no-restart >> "$LOG" 2>&1
echo "===== Done: $(date) =====" >> "$LOG"
