"""Language picker lines for README — paths depend on which folder you're in."""

from __future__ import annotations

import re

LOCALES = [
    ("English", None),
    ("Español", "es"),
    ("Français", "fr"),
    ("Português", "pt"),
    ("Русский", "ru"),
]

LOCALE_CODES = frozenset(code for _, code in LOCALES if code)

MODULE_DISPLAY: dict[str, str] = {
    "shadowfront": "ShadowFront docs",
    "tradeshipping": "Trade Shipping docs",
}

META: dict[str | None, dict[str, str]] = {
    None: {
        "header": "Languages",
        "all_label": "All locales",
        "all_href": "locales/README.md",
        "translate_label": "How to translate",
        "translate_href": "../TRANSLATIONS.md",
    },
    "es": {
        "header": "Idiomas",
        "all_label": "Todos los idiomas",
        "all_href": "../README.md",
        "translate_label": "Cómo traducir",
        "translate_href": "../../../TRANSLATIONS.md",
    },
    "fr": {
        "header": "Langues",
        "all_label": "Toutes les langues",
        "all_href": "../README.md",
        "translate_label": "Traductions",
        "translate_href": "../../../TRANSLATIONS.md",
    },
    "pt": {
        "header": "Idiomas",
        "all_label": "Todos os idiomas",
        "all_href": "../README.md",
        "translate_label": "Como traduzir",
        "translate_href": "../../../TRANSLATIONS.md",
    },
    "ru": {
        "header": "Языки",
        "all_label": "Все языки",
        "all_href": "../README.md",
        "translate_label": "Переводы",
        "translate_href": "../../../TRANSLATIONS.md",
    },
}


def _href_for(current: str | None, target: str | None) -> str:
    if target is None:
        return "../../README.md" if current else "README.md"
    if current is None:
        return f"locales/{target}/README.md"
    if current == target:
        return "README.md"
    return f"../{target}/README.md"


def lang_bar(current: str | None) -> str:
    """
    Current language = bold (this page). All others = clickable links.
    current: None = English root; else 'es', 'fr', 'pt', 'ru'.
    """
    ex = META[current]
    parts: list[str] = []
    for label, code in LOCALES:
        if code == current:
            parts.append(f"**{label}**")
        else:
            parts.append(f"[{label}]({_href_for(current, code)})")
    parts.append(f"[{ex['all_label']}]({ex['all_href']})")
    parts.append(f"[{ex['translate_label']}]({ex['translate_href']})")
    return f"**{ex['header']}:** " + " · ".join(parts)


def apply_lang_bar(content: str, current: str | None) -> str:
    bar = lang_bar(current)
    pattern = r"^\*\*(Languages|Idiomas|Langues|Языки)\s*:\s*[^\n]*$"
    if re.search(pattern, content, re.MULTILINE):
        return re.sub(pattern, bar, content, count=1, flags=re.MULTILINE)
    return re.sub(r"(^# [^\n]+\n\n)", rf"\1{bar}\n\n", content, count=1, flags=re.MULTILINE)


def locales_index_title(module_name: str) -> str:
    label = MODULE_DISPLAY.get(module_name, f"{module_name} docs")
    return f"{label} — choose language"


def locales_index_content(module_name: str) -> str:
    lines = [
        f"# {locales_index_title(module_name)}",
        "",
        "| Language | Hub |",
        "|----------|-----|",
        "| English (source) | [../README.md](../README.md) |",
    ]
    for label, code in LOCALES:
        if code:
            lines.append(f"| {label} | [{code}/README.md]({code}/README.md) |")
    lines.extend(
        [
            "",
            "Regenerate translations: [TRANSLATIONS.md](../../TRANSLATIONS.md) (Docker)",
            "",
        ]
    )
    return "\n".join(lines)


def write_locales_index(module: Path, dry_run: bool = False) -> bool:
    """Write or refresh <module>/locales/README.md language picker."""
    locales_dir = module / "locales"
    if not locales_dir.is_dir() and dry_run:
        return False
    content = locales_index_content(module.name)
    path = locales_dir / "README.md"
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    if dry_run:
        return True
    locales_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def apply_english_lang_bar(module: Path, dry_run: bool = False) -> bool:
    """Ensure English module README has the language picker bar."""
    readme = module / "README.md"
    if not readme.exists():
        return False
    raw = readme.read_text(encoding="utf-8")
    updated = apply_lang_bar(raw, None)
    if updated == raw:
        return False
    if not dry_run:
        readme.write_text(updated, encoding="utf-8")
    return True
