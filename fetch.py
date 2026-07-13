#!/usr/bin/env python3
"""simon-daily - Multi-source blog fetcher with translation.

Usage:
    python fetch.py [--source simon|addy] [--days 1] [--no-translate]
"""
from simon_daily.cli import main

if __name__ == "__main__":
    main()
