#!/usr/bin/env python3
"""
Repair markdown links in locale folders after machine translation.

Usage (Docker):
  docker compose -f docker-compose.translate.yml run --rm fix-links

Local:
  python scripts/fix_locale_links.py --lang es fr pt ru
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from locale_lang_bar import apply_lang_bar, lang_bar  # noqa: E402

LOCALES_DIR = ROOT / "locales"
LINK_RE = re.compile(r"\[([^\]]+)\]\s*\(([^)]+)\)")

HREF_ALIASES: dict[str, str] = {
    "lucha-en-el-punto.md": "fight-on-the-point.md",
    "lucha en el punto.md": "fight-on-the-point.md",
    "comunicación.md": "communication.md",
    "comunicacion.md": "communication.md",
    "rotaciones-y-apilamiento.md": "rotations-and-stacking.md",
    "errores comunes.md": "common-mistakes.md",
    "errores-comunes.md": "common-mistakes.md",
}


def extract_links(content: str) -> list[tuple[str, str]]:
    return LINK_RE.findall(content)


def is_doc_link(href: str) -> bool:
    """Sibling strategy doc — not language picker or parent paths."""
    return href.endswith(".md") and "/" not in href and ".." not in href


def normalize_hrefs(content: str) -> str:
    def fix_link(m: re.Match) -> str:
        text, href = m.group(1), m.group(2).strip()
        fixed = HREF_ALIASES.get(href, href)
        return f"[{text}]({fixed})"

    return LINK_RE.sub(fix_link, content)


def sync_doc_links(en_content: str, loc_content: str) -> str:
    """Sync simple doc links only (vaults.md, etc.) — skip language bar paths."""
    en_pairs = [(t, h) for t, h in extract_links(en_content) if is_doc_link(h)]
    loc_matches = [m for m in LINK_RE.finditer(loc_content) if is_doc_link(m.group(2).strip())]

    out = loc_content
    for (en_text, en_href), m in zip(reversed(en_pairs), reversed(loc_matches)):
        loc_text = m.group(1)
        new = f"[{loc_text}]({en_href})"
        out = out[: m.start()] + new + out[m.end() :]
    return out


def replace_links_from_english(en_content: str, loc_content: str) -> str:
    en_links = extract_links(en_content)
    loc_matches = list(LINK_RE.finditer(loc_content))
    out = loc_content
    for (_, en_href), m in zip(reversed(en_links), reversed(loc_matches)):
        loc_text = m.group(1)
        new = f"[{loc_text}]({en_href})"
        out = out[: m.start()] + new + out[m.end() :]
    return out


def source_files() -> list[Path]:
    return sorted(p for p in ROOT.glob("*.md") if p.name != "TRANSLATIONS.md")


def fix_all_lang_bars(dry_run: bool) -> int:
    """Apply locale-aware language picker to every README."""
    count = 0
    targets: list[tuple[str | None, Path]] = [(None, ROOT / "README.md")]
    for lang_dir in sorted(LOCALES_DIR.iterdir()):
        if lang_dir.is_dir():
            targets.append((lang_dir.name, lang_dir / "README.md"))

    for lang, path in targets:
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        updated = apply_lang_bar(raw, lang)
        if updated != raw:
            count += 1
            label = lang or "en"
            print(f"  fixed lang bar: {label}/README.md")
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return count


def fix_english_readme(dry_run: bool) -> bool:
    return fix_all_lang_bars(dry_run) > 0


def fix_locale(lang: str, dry_run: bool) -> int:
    loc_dir = LOCALES_DIR / lang
    if not loc_dir.is_dir():
        print(f"skip {lang}: no folder")
        return 0

    fixed = 0
    for en_path in source_files():
        loc_path = loc_dir / en_path.name
        if not loc_path.exists():
            continue
        en_raw = en_path.read_text(encoding="utf-8")
        loc_raw = loc_path.read_text(encoding="utf-8")

        if en_path.name == "README.md":
            # Language bar is locale-aware — never copy English root paths here
            updated = normalize_hrefs(loc_raw)
            updated = sync_doc_links(en_raw, updated)
            updated = apply_lang_bar(updated, lang)
        else:
            updated = replace_links_from_english(en_raw, loc_raw)
            updated = normalize_hrefs(updated)

        if updated != loc_raw:
            fixed += 1
            print(f"  fixed links: {lang}/{en_path.name}")
            if not dry_run:
                loc_path.write_text(updated, encoding="utf-8")

    return fixed


def main() -> None:
    parser = argparse.ArgumentParser(description="Fix locale markdown links")
    parser.add_argument("--lang", nargs="*", help="Locale codes (default: all)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if fix_all_lang_bars(args.dry_run):
        pass

    langs = args.lang or [d.name for d in sorted(LOCALES_DIR.iterdir()) if d.is_dir()]
    total = 0
    for lang in langs:
        print(f"=== {lang} ===")
        total += fix_locale(lang, args.dry_run)
    print(f"\nDone: {total} locale file(s) updated")


if __name__ == "__main__":
    main()
