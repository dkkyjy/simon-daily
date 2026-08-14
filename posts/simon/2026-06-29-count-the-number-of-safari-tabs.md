# Count the number of Safari tabs

        **Date:** ...
        **Link:** https://simonwillison.net/2026/Jun/29/safari-tab-count/
        **Tags:** safari, til, applescript

        ---

29th June 2026

Tiniest TIL, using AppleScript to count the number of open browser tabs in Safari:

```
osascript -e 'tell application "Safari" to count tabs of every window'
```

Posted [29th June 2026](/2026/Jun/29/) at 6:36 pm
