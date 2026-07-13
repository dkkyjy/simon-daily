#!/usr/bin/env python3
"""Daily scheduled task for simon-daily.
Usage:
    python daily_task.py [--days 1] [--dry-run] [--no-deploy]
"""
from simon_daily.deploy import daily_main

if __name__ == "__main__":
    daily_main()
