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

META: dict[str | None, dict[str, str]] = {
    None: {
        "header": "Languages",
        "all_label": "All locales",
        "all_href": "locales/README.md",
        "translate_label": "How to translate",
        "translate_href": "TRANSLATIONS.md",
    },
    "es": {
        "header": "Idiomas",
        "all_label": "Todos los idiomas",
        "all_href": "../README.md",
        "translate_label": "Cómo traducir",
        "translate_href": "../../TRANSLATIONS.md",
    },
    "fr": {
        "header": "Langues",
        "all_label": "Toutes les langues",
        "all_href": "../README.md",
        "translate_label": "Traductions",
        "translate_href": "../../TRANSLATIONS.md",
    },
    "pt": {
        "header": "Idiomas",
        "all_label": "Todos os idiomas",
        "all_href": "../README.md",
        "translate_label": "Como traduzir",
        "translate_href": "../../TRANSLATIONS.md",
    },
    "ru": {
        "header": "Языки",
        "all_label": "Все языки",
        "all_href": "../README.md",
        "translate_label": "Переводы",
        "translate_href": "../../TRANSLATIONS.md",
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
    if re.search(r"^\*\*(Languages|Idiomas|Langues|Языки):", content, re.MULTILINE):
        return re.sub(
            r"^\*\*(Languages|Idiomas|Langues|Языки):[^\n]*$",
            bar,
            content,
            count=1,
            flags=re.MULTILINE,
        )
    return re.sub(r"(^# [^\n]+\n\n)", rf"\1{bar}\n\n", content, count=1, flags=re.MULTILINE)
