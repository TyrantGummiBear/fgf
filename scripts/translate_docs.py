#!/usr/bin/env python3
"""
Batch-translate FGF markdown docs for GitHub hosting.

Docker (recommended — no local install):
  cd fgf
  docker compose -f docker-compose.translate.yml run --rm translate --lang es fr pt ru

  # one module only:
  docker compose -f docker-compose.translate.yml run --rm translate --lang es --module tradeshipping

Optional DeepL (better quality):
  DEEPL_AUTH_KEY=your-key docker compose -f docker-compose.translate.yml run --rm translate --lang es --engine deepl

Local (optional):
  pip install -r scripts/requirements-translate.txt
  python scripts/translate_docs.py --lang es

English source: fgf/<module>/*.md
Output:         fgf/<module>/locales/<lang>/*.md
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from locale_lang_bar import apply_lang_bar, apply_english_lang_bar, write_locales_index  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_FILES = {"TRANSLATIONS.md"}
SKIP_DIRS = {"scripts", "locales", ".git"}

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LINK_PLACEHOLDER = "LINKPH{idx}LINKPH"


def extract_and_mask_links(content: str) -> tuple[str, list[tuple[str, str]]]:
    """Replace markdown links with placeholders; return (masked, links)."""
    links: list[tuple[str, str]] = []

    def repl(m: re.Match) -> str:
        links.append((m.group(1), m.group(2)))
        return LINK_PLACEHOLDER.format(idx=len(links) - 1)

    masked = LINK_RE.sub(repl, content)
    return masked, links


def restore_links(translated: str, links: list[tuple[str, str]], translator, delay: float) -> str:
    """Restore links: translate label only; keep original href unchanged."""
    out = translated
    for idx, (text, href) in enumerate(links):
        placeholder = LINK_PLACEHOLDER.format(idx=idx)
        if placeholder not in out:
            continue
        label = translate_text(text, translator, delay) if text.strip() else text
        out = out.replace(placeholder, f"[{label}]({href})", 1)
    return out


def chunk_text(text: str, max_len: int = 4500) -> list[str]:
    if len(text) <= max_len:
        return [text]
    parts: list[str] = []
    current: list[str] = []
    size = 0
    for line in text.splitlines(keepends=True):
        if size + len(line) > max_len and current:
            parts.append("".join(current))
            current = [line]
            size = len(line)
        else:
            current.append(line)
            size += len(line)
    if current:
        parts.append("".join(current))
    return parts


def split_preserve_code_blocks(content: str) -> list[tuple[str, bool]]:
    """Return (segment, is_code) pairs."""
    pattern = re.compile(r"```[\s\S]*?```", re.MULTILINE)
    segments: list[tuple[str, bool]] = []
    last = 0
    for m in pattern.finditer(content):
        if m.start() > last:
            segments.append((content[last : m.start()], False))
        segments.append((m.group(0), True))
        last = m.end()
    if last < len(content):
        segments.append((content[last:], False))
    return segments


def get_translator(engine: str, target: str):
    try:
        from deep_translator import GoogleTranslator, DeeplTranslator
    except ImportError:
        print("Install: pip install deep-translator", file=sys.stderr)
        sys.exit(1)

    if engine == "deepl":
        key = os.environ.get("DEEPL_AUTH_KEY")
        if not key:
            print("DEEPL_AUTH_KEY not set; falling back to Google.", file=sys.stderr)
            engine = "google"
        else:
            deepl_target = target.upper().replace("-CN", "").replace("-TW", "")
            return DeeplTranslator(api_key=key, target=deepl_target)

    if engine == "google":
        return GoogleTranslator(source="en", target=target)

    raise ValueError(f"Unknown engine: {engine}")


def translate_text(text: str, translator, delay: float) -> str:
    if not text.strip():
        return text
    out: list[str] = []
    for chunk in chunk_text(text):
        for attempt in range(3):
            try:
                out.append(translator.translate(chunk))
                break
            except Exception as e:
                if attempt == 2:
                    print(f"  translate error: {e}", file=sys.stderr)
                    out.append(chunk)
                else:
                    time.sleep(delay * (attempt + 1))
        time.sleep(delay)
    return "".join(out)


def translate_markdown(content: str, translator, delay: float) -> str:
    masked, links = extract_and_mask_links(content)
    pieces: list[str] = []
    for segment, is_code in split_preserve_code_blocks(masked):
        if is_code:
            pieces.append(segment)
        else:
            pieces.append(translate_text(segment, translator, delay))
    translated = "".join(pieces)
    return restore_links(translated, links, translator, delay)


def doc_modules(module_filter: list[str] | None = None) -> list[Path]:
    """Top-level folders under fgf/ that contain English *.md sources."""
    modules: list[Path] = []
    for p in sorted(REPO_ROOT.iterdir()):
        if not p.is_dir() or p.name.startswith(".") or p.name in SKIP_DIRS:
            continue
        if not any(p.glob("*.md")):
            continue
        if module_filter and p.name not in module_filter:
            continue
        modules.append(p)
    return modules


def source_files(module: Path) -> list[Path]:
    return sorted(p for p in module.glob("*.md") if p.name not in SKIP_FILES)


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate FGF docs")
    parser.add_argument(
        "--lang",
        nargs="+",
        required=True,
        help="Target language code(s), e.g. es fr de pt zh-CN",
    )
    parser.add_argument(
        "--module",
        nargs="+",
        help="Doc folder(s) under fgf/, e.g. shadowfront tradeshipping (default: all)",
    )
    parser.add_argument(
        "--engine",
        choices=("google", "deepl"),
        default="google",
        help="Translation backend (default: google)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.3,
        help="Seconds between API calls (rate limits)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files only, do not translate",
    )
    args = parser.parse_args()

    modules = doc_modules(args.module)
    if not modules:
        label = ", ".join(args.module) if args.module else "(none found)"
        print(f"No doc modules in {REPO_ROOT}: {label}", file=sys.stderr)
        sys.exit(1)

    for module in modules:
        sources = source_files(module)
        if not sources:
            print(f"\n=== skip {module.name}: no .md files ===")
            continue

        for lang in args.lang:
            out_dir = module / "locales" / lang
            print(f"\n=== {module.name}/{lang} → {out_dir.relative_to(REPO_ROOT)} ===")
            if args.dry_run:
                for f in sources:
                    print(f"  would translate: {f.name}")
                continue

            out_dir.mkdir(parents=True, exist_ok=True)
            translator = get_translator(args.engine, lang)

            for src in sources:
                dest = out_dir / src.name
                print(f"  {src.name} …", flush=True)
                raw = src.read_text(encoding="utf-8")
                translated = translate_markdown(raw, translator, args.delay)
                if src.name == "README.md":
                    translated = apply_lang_bar(translated, lang)
                rel_src = os.path.relpath(src, dest.parent).replace("\\", "/")
                banner = (
                    f"> **Machine translation ({lang}).** English source: "
                    f"[{src.name}]({rel_src}). "
                    f"Report fixes in guild chat or a GitHub issue.\n\n"
                )
                if not translated.startswith(">"):
                    translated = banner + translated
                dest.write_text(translated, encoding="utf-8")

            print(f"  Done: {len(sources)} files")

        if not args.dry_run:
            if write_locales_index(module):
                print(f"  wrote {module.name}/locales/README.md")
            if apply_english_lang_bar(module):
                print(f"  updated lang bar: {module.name}/README.md")

    print("\nNext: native speaker review, run fix-links if needed, commit & push.")


if __name__ == "__main__":
    main()
