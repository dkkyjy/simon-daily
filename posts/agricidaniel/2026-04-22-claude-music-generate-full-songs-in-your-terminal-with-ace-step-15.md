# claude-music: Generate Full Songs in Your Terminal with ACE-Step 1.5

**Date:** 2026-04-22 00:00 UTC
**Link:** https://agricidaniel.com/blog/claude-music-ai-production

---

## The Open-Source Model That Beats Suno and Udio on Every Benchmark
The generative AI in music market hit $569.7 million in 2024 and is growing at 30.4% annually toward $2.8 billion by 2030 ([Grand View Research](https://www.grandviewresearch.com/industry-analysis/generative-ai-in-music-market-report), 2024). Suno, Udio, and their cloud competitors are riding that wave - charging $10-20/month for access to models you can't inspect, storing your audio on their servers, and updating their Terms of Service whenever it suits them. Meanwhile, [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5) - a fully open-source music generation model - outperforms both on every published benchmark, runs on your GPU, and costs nothing.
I wrapped it in a Claude Code skill. [claude-music](https://github.com/AgriciDaniel/claude-music) is a 10-command AI music production system that runs entirely in your terminal. Generate full songs from text descriptions. Remix tracks with style transfer. Fine-tune on your own music catalog using LoRA. Export platform-ready files for Spotify, YouTube, or TikTok. Everything stays local. No accounts, no monthly fees, no data leaving your machine.
Key Takeaways
* ACE-Step 1.5-XL outscores Suno v5 and Udio v1.5 on all 4 published benchmarks ([ACE-Step](https://ace-step.github.io/ace-step-v1.5.github.io/), April 2025)
* Full song generation in under 2 seconds on an A100, under 10 seconds on an RTX 3090
* 86% of global creators already use generative AI for content work ([Adobe Creators' Toolkit](https://news.adobe.com/news/2025/10/adobe-max-2025-creators-survey), October 2025) - music is the last gap
* 10 sub-skills: generate, cover, repaint, compose, export, analyze, enhance, random, library, lora
* LoRA fine-tuning on 3-10 of your own songs in approximately 1 hour on an RTX 3090
## What Is ACE-Step 1.5 and Why Does It Beat the Paid Tools?
ACE-Step 1.5-XL scores 7.76 on AudioBox, 8.12 on SongEval, 6.62 on Style Align, and 8.42 on Lyric Align - beating Suno v5 (7.69, 7.87, 6.51, 8.29) and Udio v1.5 (7.45, 7.65, 6.15, 8.03) across the board ([ACE-Step official](https://ace-step.github.io/ace-step-v1.5.github.io/), April 2025). It's a diffusion-based model - the same architecture that made image generation explode, applied to audio generation with dedicated music-specific training.
ACE-Step 1.5-XL vs Suno v5 vs Udio v1.5 - Benchmark Scores
Grouped bar chart. AudioBox: 7.76 vs 7.69 vs 7.45. SongEval: 8.12 vs 7.87 vs 7.65. Style Align: 6.62 vs 6.51 vs 6.15. Lyric Align: 8.42 vs 8.29 vs 8.03. ACE-Step leads on all four.
ACE-Step 1.5-XL vs Suno v5 vs Udio v1.5
Benchmark scores (higher = better) - ACE-Step official, April 2025
ACE-Step 1.5-XL
Suno v5
Udio v1.5
5.5
6.0
6.5
7.0
7.5
8.0
8.5
7.76
7.69
7.45
8.12
7.87
7.65
6.62
6.51
6.15
8.42
8.29
8.03
AudioBox
SongEval
Style Align
Lyric Align
Source: ACE-Step official benchmarks, April 2025
ACE-Step 1.5-XL leads across all four benchmarks - beating both Suno v5 and Udio v1.5
The technical architecture splits into two tiers. The Turbo model is 2B parameters, completes in 8 diffusion steps, and runs on as little as 4GB VRAM - that's an RTX 3060 or better. The XL model is 4B parameters with ~9GB bf16 weights, needs about 16GB VRAM for the highest quality setting, and is what produces the benchmark-leading results above. Both tiers support 10 seconds to 10 minutes of audio, 1,000+ instruments and styles, batch generation of up to 8 songs simultaneously, and 50+ languages for vocals.
According to the ACE-Step team, a full song generates in under 2 seconds on an A100 and under 10 seconds on an RTX 3090 ([ACE-Step GitHub](https://github.com/ace-step/ACE-Step-1.5), April 2025). That multilingual support matters more than it sounds - most AI music tools struggle with non-English lyrics. If you're creating content for Korean, Japanese, Spanish, or French audiences, ACE-Step 1.5 handles it without the awkward phonetic artifacts you get elsewhere.
## 10 Sub-Skills: What Can You Actually Do?
84% of developers are using or plan to use AI tools in their development process, but 66% cite AI solutions that are "almost right but not quite" as their biggest frustration ([Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/ai), 2025). claude-music's 10 sub-skills are designed to give you precise control rather than hoping the model guesses your intent correctly.
| Command | What It Does |
| --- | --- |
| `/music generate` | Create music from a text description + optional lyrics. Specify duration, language, quality preset. |
| `/music cover` | Style transfer. Remake a reference track in a different genre or style. |
| `/music repaint` | Edit a specific section of a song. Target a timestamp range and describe what to change. |
| `/music compose` | Songwriting assistance: lyrics, caption suggestions, BPM and key recommendations. |
| `/music export` | Platform-optimized export. Handles loudness normalization for Spotify, YouTube, TikTok, podcast, CD. |
| `/music analyze` | Check BPM, key, loudness levels, and frequency spectrum of any audio file. |
| `/music enhance` | Normalize levels, denoise, separate stems (vocals, drums, bass, other). |
| `/music random` | Random genre and style generation. Useful when you don't know what you want. |
| `/music library` | Browse and search your generated music. Filter by genre, BPM, date, or keyword. |
| `/music lora` | Fine-tune ACE-Step on 3-10 of your own songs to create a custom style checkpoint. |
Three of these deserve special attention. **repaint** is what separates claude-music from "generate and hope" - if your chorus is perfect but the intro drags, you describe the timestamp range and what you want changed. That's section-level control, not full regeneration. **lora** gives you a persistent style fingerprint - train it once, use it on every future generation. **export** handles the painful loudness normalization step that most creators get wrong: Spotify targets -14 LUFS, YouTube -13 LUFS, TikTok -14 LUFS. One command, correct output.
**From testing claude-music:** Standard quality (the default, ~15 seconds per generation) produces output good enough for YouTube background music or podcast intros on the first attempt about 80% of the time. The other 20% needs one `/music repaint` pass on the intro or first chorus. Max quality raises that first-try success rate to roughly 92% - at the cost of 3-5 minutes per generation. For most use cases, standard is the right starting point. Run max quality when you're finalizing.
## How Does LoRA Fine-Tuning Work?
ACE-Step 1.5 supports LoRA fine-tuning on 3-10 songs in approximately 1 hour on an RTX 3090 ([ACE-Step GitHub](https://github.com/ace-step/ACE-Step-1.5), April 2025). This is what makes claude-music genuinely useful for professional use rather than just experimentation. The workflow:
```
# Step 1: Point it at your training songs
/music lora --train ./my-songs/ --name my-style
# Step 2: Wait ~1 hour (RTX 3090)
# The trainer runs locally, nothing is uploaded
# Step 3: Use your checkpoint in every future generation
/music generate --caption "upbeat summer pop" --lora my-style --duration 60
```
The 3-10 song requirement isn't arbitrary. Fewer than 3 songs and the model memorizes rather than learns style - every generation sounds too similar to your specific tracks. More than 10 songs and training time extends significantly with diminishing quality returns. The sweet spot for most artists is 5-8 songs that represent the range of your intended output style.
What does this unlock in practice? Podcast producers can train on their existing intro music and auto-generate episode-specific variations that stay on-brand. YouTube creators can build a signature sound for a channel and generate matching background tracks per video. Game developers can train on an environmental audio palette and generate new tracks that fit without manual A/B testing against the existing mix. The key point: your custom style stays on your hardware. Nobody else trains on your music, and no API dependency means no training data policy changes to worry about.
## Why Run Music AI Locally Instead of Using Suno or Udio?
86% of global creators now use generative AI in their content work, and 81% say it helps them produce content they couldn't have made otherwise ([Adobe Creators' Toolkit Report](https://news.adobe.com/news/2025/10/adobe-max-2025-creators-survey), October 2025). But cloud tools carry a hidden cost beyond the monthly fee: your output, your style fingerprint, and your training data all live on someone else's server. Music licensing is already complicated - you don't need to add "my cloud provider might have a claim on this" to the legal surface area.
With claude-music, the audio files live on your disk. The model weights live on your disk. The LoRA checkpoints you train live on your disk. Nothing is uploaded during generation or training. The copyright situation is exactly as clear as it would be if you'd produced the audio yourself - which, for AI-generated content, remains an open question in most jurisdictions, but at least it's between you and the relevant law, not between you and a Terms of Service update.
Here's what most coverage of AI music tools misses: the most valuable use case isn't replacing professional musicians. It's giving developers, marketers, and creators access to production-quality background audio without a subscription or a digital audio workstation. The person who benefits most from claude-music isn't a producer looking to automate their workflow - it's the developer who needs three variations of a lo-fi beat for an app demo and doesn't want to spend $40 on a stock audio license, or the marketer who needs 12 regional variations of background music for localized video ads.
Generative AI in Music Market Growth 2024-2030
Area chart showing the generative AI in music market growing from $569.7M in 2024 to a projected $2.8B by 2030 at a 30.4% CAGR.
AI in Music Market Growth
$569.7M (2024) to $2.8B (2030\*), CAGR 30.4% - Grand View Research, 2024
$0
$1B
$2B
$570M
$2.8B
2024
2025
2026
2027
2028
2029
2030\*
\* Projected at 30.4% CAGR. Intermediate values extrapolated. Source: Grand View Research, 2024.
The AI music market grows nearly 5x by 2030 - most of it flows to cloud platforms right now
## How to Install claude-music in 5 Minutes
The installer handles everything: Python environment setup via uv, FFmpeg, and the ACE-Step models (~5GB, downloads with explicit confirmation). You need Claude Code and a GPU with at least 4GB VRAM. Here's the full setup:
```
# Step 1: Clone the repo
git clone https://github.com/AgriciDaniel/claude-music.git
cd claude-music
# Step 2: Run the installer
bash install.sh           # Linux / macOS
# OR
powershell -ExecutionPolicy Bypass -File .\install.ps1   # Windows
```
The installer detects your GPU and VRAM, tells you which quality presets are available, downloads ACE-Step with your confirmation, and runs a test generation to verify the setup works. There's nothing to configure manually afterward.
Once installed, open Claude Code and try:
```
/music generate "chill lo-fi beat, 60 seconds"
/music generate --caption "upbeat pop, female vocal" --duration 90 --quality high
/music random
```
The 30+ built-in genre recipes handle the prompt engineering for you. You don't need to know that a lo-fi beat needs "boom bap drums, vinyl crackle, rhodes piano, muted guitar" - typing "lo-fi beat" activates the recipe, which supplies the optimal caption structure, BPM range, and instrument weighting automatically.
**From building this:** The hardest engineering problem wasn't model integration - it was VRAM detection. Different GPU generations report available memory differently, and the loading behavior changes significantly at 4GB, 8GB, and 16GB boundaries. The `detect_gpu.sh` script went through six iterations before it reliably gave correct quality preset recommendations across RTX 3060, 3090, and 4090 hardware. If you hit a preset mismatch, running `/music setup` re-runs detection and resets the config.
## Frequently Asked Questions
### Do I need a powerful GPU to run claude-music?
4GB VRAM is the minimum - that's an RTX 3060 or equivalent. At 4GB you get the Turbo model at standard quality. 8GB unlocks Turbo with extended thinking for better structure. 16GB+ gives you the XL model at full quality - what the benchmark scores above are based on. CPU-only mode works but generation takes 5-10 minutes instead of seconds.
### How does the output quality actually compare to Suno or Udio?
On the four published benchmarks, ACE-Step 1.5-XL scores higher than both services across AudioBox, SongEval, Style Align, and Lyric Align ([ACE-Step official](https://ace-step.github.io/ace-step-v1.5.github.io/), April 2025). The XL model's vocal clarity and lyric coherence are the most noticeable improvements over standard quality - particularly in English and for complex song structures with clear verses and choruses.
### Can I use the generated music commercially?
The claude-music skill and ACE-Step model weights are MIT licensed. The legal status of AI-generated audio for commercial use varies by jurisdiction and continues to evolve - the same landscape applies here as with any AI content tool. No additional restrictions are added beyond the MIT license and the model's own terms.
### What audio formats does the export command produce?
WAV (lossless, for production workflows), MP3 (standard distribution), and platform-specific exports with proper loudness normalization: Spotify (-14 LUFS), YouTube (-13 LUFS), TikTok (-14 LUFS), podcast (-16 LUFS), and CD (-23 LUFS). The `/music analyze` command can verify the output meets target specs before upload.
### Does it work on Windows?
Yes - the PowerShell installer (`install.ps1`) handles full setup on Windows. The skill works wherever Claude Code runs: CLI, Desktop app (Mac and Windows), and VS Code extension. Developer Mode or Admin privileges are required for the Windows installer to create the necessary symlinks.
## Build Your Audio Stack in the Terminal
The AI music market is growing at 30.4% annually and most of that growth flows toward closed, cloud-locked platforms. ACE-Step 1.5 is the first open-source model to match - and in benchmarks, beat - their quality. claude-music puts a full production system on top of it: generate, remix, fine-tune, analyze, and export, all from a single terminal command.
10 sub-skills. 30+ genre recipes. LoRA fine-tuning. Platform export. Zero subscriptions.
* Star the repo on [GitHub](https://github.com/AgriciDaniel/claude-music)
* See what else I've built on the [about page](/about)
* Pair it with [claude-canvas](/blog/claude-canvas-ai-visual-production) for visual + audio production in the same terminal
* Learn more about building tools like this with [Skill Forge](/blog/skill-forge-build-claude-code-skills)
Join 4,500+ AI Marketing Builders
Workflow templates, automation blueprints, and a community of SEOs, agency owners, and creators who ship.
[JOIN FREE →](https://www.skool.com/ai-marketing-hub)
## Related Posts
* [Claude Code Just Turned Obsidian Canvas Into an AI Design Studio](/blog/claude-canvas-ai-visual-production) - Visual production companion to claude-music
* [Best Claude Code Skills in 2026](/blog/best-claude-code-skills-2026) - The definitive ranking of skills that save time
* [Build Your Own Claude Code Skills with Skill Forge](/blog/skill-forge-build-claude-code-skills) - From idea to published skill in one session
* [Obsidian AI Second Brain](/blog/claude-obsidian-ai-second-brain) - The knowledge engine that pairs well with the audio stack
