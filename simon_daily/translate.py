"""Translation and summarization via fabric-ai."""
import re
import shutil
import subprocess
import sys
from pathlib import Path


def post_process(translated, source_path):
    """Clean known fabric-ai translate artifacts from the model output.

    Fixes (learned from batch translation of simon-daily 2026-09-0x):
    - stray <think> draft before the real translation -> keep text after </think>
    - leaked translate pattern instructions (IMPORTANT / 重要提示 variants)
    - localized or mojibake tag labels -> restore from source **Tags:**
    - broken image markdown from extra blank line
    """
    if '</think>' in translated:
        translated = translated.split('</think>', 1)[1].lstrip('\n')
    translated = re.sub(
        r'(?m)^[ \t]*→?[ \t]*(IMPORTANT:.*|重要提示[：:].*)$\n*', '', translated)
    translated = translated.replace('[![\n\n](', '[![\n](')
    try:
        with open(source_path, encoding='utf-8') as fh:
            src = fh.read()
        m = re.search(r'\*\*Tags:\*\*\s*(.+)', src)
        if m:
            tag = m.group(1).strip()
            translated = re.sub(
                r'(?m)^(\s*)\*\*[^*]*(标签|鏍囩撅)[^*]*\*\*.*$',
                lambda mm: f"{mm.group(1)}**标签：** {tag}", translated)
    except Exception:
        pass
    return translated.strip()


def translate_post(filepath, model=None, lang_code="zh-cn"):
    """Translate a post using fabric-ai. Accepts str or Path."""
    fabric_bin = shutil.which("fabric-ai") or shutil.which("fabric")
    if not fabric_bin:
        print("  [SKIP] fabric-ai not found", file=sys.stderr)
        return None

    filepath = Path(filepath)
    zh_path = filepath.with_suffix(f".{lang_code}.md")
    if zh_path.exists():
        print(f"  [SKIP] {zh_path.name} exists")
        return zh_path

    try:
        with open(filepath, encoding="utf-8") as fh:
            file_content = fh.read()
        cmd = [fabric_bin, "-p", "translate", "--suppress-think", "-v", f"lang_code:{lang_code}", "-r"]
        if model:
            cmd += ["-m", model]
        resp = subprocess.run(cmd, input=file_content, capture_output=True, text=True, timeout=600)
        if resp.returncode != 0:
            print(f"  [ERROR] fabric translate failed (rc={resp.returncode}): {resp.stderr[:200]}", file=sys.stderr)
            return None
        translated = resp.stdout.strip()
        if not translated:
            print(f"  [ERROR] empty fabric output", file=sys.stderr)
            return None

        translated = post_process(translated, filepath)
        if not translated:
            print(f"  [ERROR] empty output after post-processing", file=sys.stderr)
            return None

        with open(zh_path, "w", encoding="utf-8") as f:
            f.write(translated + "\n")
        print(f"  Translated: {zh_path.name}")
        return zh_path
    except Exception as e:
        print(f"  [ERROR] Translation error: {e}", file=sys.stderr)
        return None


def save_translation(filepath, lang_code="zh-cn", model=None):
    """Public API: translate a single post file."""
    return translate_post(filepath, model=model, lang_code=lang_code)


def summarize_post(filepath, model=None):
    """Generate a summary for a post using fabric-ai summarize pattern.
    Returns dict with 'summary' text or None on failure.
    """
    filepath = Path(filepath)
    summary_file = filepath.with_suffix(".summary.md")

    if summary_file.exists():
        with open(summary_file, encoding="utf-8") as f:
            return {"summary": f.read(), "cached": True}

    fabric_bin = shutil.which("fabric-ai") or shutil.which("fabric")
    if not fabric_bin:
        print("  [ERROR] fabric-ai/fabric not found", file=sys.stderr)
        return None

    try:
        with open(filepath, encoding="utf-8") as fh:
            file_content = fh.read()

        cmd = [fabric_bin, "-p", "summarize"]
        if model:
            cmd += ["-m", model]
        resp = subprocess.run(cmd, input=file_content, capture_output=True, text=True, timeout=180)

        if resp.returncode != 0:
            print(f"  [ERROR] fabric summarize failed (rc={resp.returncode}): {resp.stderr.strip()}", file=sys.stderr)
            return None

        summary = resp.stdout.strip()
        if not summary:
            print(f"  [ERROR] fabric summarize returned empty output", file=sys.stderr)
            return None

        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(summary)

        return {"summary": summary, "cached": False}
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] fabric summarize timed out for {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [ERROR] summarize failed: {e}", file=sys.stderr)
        return None
