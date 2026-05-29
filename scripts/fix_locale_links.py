#!/usr/bin/env python3
"""
Repair markdown links in locale folders after machine translation.

Usage (Docker):
  docker compose -f docker-compose.translate.yml run --rm fix-links

Local:
  python scripts/fix_locale_links.py --lang es fr pt ru
  python scripts/fix_locale_links.py --module shadowfront --lang es
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from locale_lang_bar import (  # noqa: E402
    LOCALE_CODES,
    apply_lang_bar,
    apply_english_lang_bar,
    write_locales_index,
)

SKIP_DIRS = {"scripts", "locales", ".git"}

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


def doc_modules(module_filter: list[str] | None = None) -> list[Path]:
    modules: list[Path] = []
    for p in sorted(REPO_ROOT.iterdir()):
        if not p.is_dir() or p.name.startswith(".") or p.name in SKIP_DIRS:
            continue
        if not (p / "locales").is_dir():
            continue
        if module_filter and p.name not in module_filter:
            continue
        modules.append(p)
    return modules


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


def source_files(module: Path) -> list[Path]:
    return sorted(p for p in module.glob("*.md") if p.name != "TRANSLATIONS.md")


def fix_all_lang_bars(module: Path, dry_run: bool) -> int:
    """Apply locale-aware language picker to every README."""
    locales_dir = module / "locales"
    count = 0
    targets: list[tuple[str | None, Path]] = [(None, module / "README.md")]
    for lang_dir in sorted(locales_dir.iterdir()):
        if lang_dir.is_dir() and lang_dir.name in LOCALE_CODES:
            targets.append((lang_dir.name, lang_dir / "README.md"))

    for lang, path in targets:
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        updated = apply_lang_bar(raw, lang)
        if updated != raw:
            count += 1
            label = lang or "en"
            print(f"  fixed lang bar: {module.name}/{label}/README.md")
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return count


def fix_locale(module: Path, lang: str, dry_run: bool) -> int:
    locales_dir = module / "locales"
    loc_dir = locales_dir / lang
    if not loc_dir.is_dir():
        print(f"  skip {module.name}/{lang}: no folder")
        return 0

    fixed = 0
    for en_path in source_files(module):
        loc_path = loc_dir / en_path.name
        if not loc_path.exists():
            continue
        en_raw = en_path.read_text(encoding="utf-8")
        loc_raw = loc_path.read_text(encoding="utf-8")

        if en_path.name == "README.md":
            updated = normalize_hrefs(loc_raw)
            updated = sync_doc_links(en_raw, updated)
            updated = apply_lang_bar(updated, lang)
        else:
            updated = replace_links_from_english(en_raw, loc_raw)
            updated = normalize_hrefs(updated)

        if updated != loc_raw:
            fixed += 1
            print(f"  fixed links: {module.name}/{lang}/{en_path.name}")
            if not dry_run:
                loc_path.write_text(updated, encoding="utf-8")

    return fixed


def main() -> None:
    parser = argparse.ArgumentParser(description="Fix locale markdown links")
    parser.add_argument("--module", nargs="+", help="Doc folder(s) (default: all with locales/)")
    parser.add_argument("--lang", nargs="*", help="Locale codes (default: all)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    modules = doc_modules(args.module)
    if not modules:
        print("No modules with locales/ found", file=sys.stderr)
        sys.exit(1)

    total = 0
    for module in modules:
        print(f"=== {module.name} ===")
        if write_locales_index(module, args.dry_run):
            print(f"  wrote locales/README.md")
        if apply_english_lang_bar(module, args.dry_run):
            print(f"  updated lang bar: README.md")
        fix_all_lang_bars(module, args.dry_run)

        locales_dir = module / "locales"
        langs = args.lang or [d.name for d in sorted(locales_dir.iterdir()) if d.is_dir()]
        for lang in langs:
            print(f"  --- {lang} ---")
            total += fix_locale(module, lang, args.dry_run)

    print(f"\nDone: {total} locale file(s) updated")


if __name__ == "__main__":
    main()
