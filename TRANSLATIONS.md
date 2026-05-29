# Translations (i18n)

How we keep FGF guild docs readable for members who don't use English.

**English is the source of truth** in each module folder (`shadowfront/`, `tradeshipping/`, …). Translations live in `<module>/locales/<language>/`.

---

## Quick start (Docker)

No Python or translation libraries on your machine — only Docker.

```powershell
cd fgf

# Build once
docker compose -f docker-compose.translate.yml build

# Translate all doc modules (shadowfront, tradeshipping, …)
docker compose -f docker-compose.translate.yml run --rm translate --lang es fr pt ru

# One module only
docker compose -f docker-compose.translate.yml run --rm translate --lang es --module tradeshipping
```

**Windows shortcut:**

```powershell
.\scripts\translate.ps1 --lang es fr pt ru
```

**macOS / Linux:**

```bash
./scripts/translate.sh --lang es fr pt ru
```

Output appears in `<module>/locales/es/`, etc. Commit and push.

### Repair broken links (after a bad translate run)

Machine translation can break markdown link paths. Fix without re-translating:

```powershell
docker compose -f docker-compose.translate.yml run --rm fix-links
docker compose -f docker-compose.translate.yml run --rm fix-links --module shadowfront --lang es
```

Or: `python scripts/fix_locale_links.py --lang es fr pt ru`

### Optional: DeepL (better quality)

```powershell
$env:DEEPL_AUTH_KEY = "your-key"
docker compose -f docker-compose.translate.yml run --rm translate --lang es --engine deepl
```

### Dry run (list files only)

```powershell
docker compose -f docker-compose.translate.yml run --rm translate --lang es --dry-run
```

---

## How it works

```
Host: fgf/                        Container: /docs/
├── shadowfront/*.md     ────────►  read English *.md per module
├── tradeshipping/*.md
├── scripts/
│   └── translate_docs.py  ────►  executed inside container
└── <module>/locales/    ◄────────  write locales/<lang>/*.md
```

The compose file bind-mounts the **fgf repo root** read/write. Nothing is copied out — translations land directly in your repo tree.

---

## Folder layout

```
fgf/
├── docker-compose.translate.yml
├── TRANSLATIONS.md
├── scripts/
│   ├── Dockerfile
│   ├── translate_docs.py
│   ├── fix_locale_links.py
│   ├── translate.ps1
│   └── translate.sh
├── shadowfront/
│   ├── README.md             ← English (edit here first)
│   └── locales/
│       ├── README.md         ← language picker
│       ├── es/
│       ├── fr/
│       ├── pt/
│       └── ru/
└── tradeshipping/
    ├── README.md
    └── locales/              ← created on first translate run
        └── es/
```

**GitHub links:** Share `…/fgf/shadowfront/locales/es/README.md` for Spanish ShadowFront readers.

---

## Recommended workflow

| Step | Who | What |
|------|-----|------|
| 1 | Strategy lead | Update **English** docs after matches |
| 2 | Anyone | Run Docker translate for target languages |
| 3 | Native speaker | Skim PR — fix game terms, callouts, tone |
| 4 | Discord | Pin language-specific README links |

**Don't edit translations only** — re-run Docker after English changes, or update English first.

---

## Guild languages (initial)

| Code | Language | ShadowFront hub |
|------|----------|-----------------|
| `es` | Español | [shadowfront/locales/es/README.md](shadowfront/locales/es/README.md) |
| `fr` | Français | [shadowfront/locales/fr/README.md](shadowfront/locales/fr/README.md) |
| `pt` | Português | [shadowfront/locales/pt/README.md](shadowfront/locales/pt/README.md) |
| `ru` | Русский | [shadowfront/locales/ru/README.md](shadowfront/locales/ru/README.md) |

```powershell
docker compose -f docker-compose.translate.yml run --rm translate --lang es fr pt ru
```

---

## What to translate vs. keep in English

| Keep in English | Translate |
|-----------------|-----------|
| Voice callouts (`Flip`, `Deny`, `Stack`) | Explanations around them |
| Player/ship names | Body text, tables, headings |

---

## Quality tips

- **Native review** — machine text is a draft
- **Glossary** — agree on *vault, guardian, whale, circle* per language in `locales/<lang>/GLOSSARY.md`
- **Re-run after English edits** — `docker compose … run --rm translate --lang es fr pt ru`

---

## Discord pins

```
🇬🇧 English:  …/shadowfront/README.md
🇪🇸 Español:   …/shadowfront/locales/es/README.md
🇫🇷 Français:  …/shadowfront/locales/fr/README.md
🇵🇹 Português: …/shadowfront/locales/pt/README.md
🇷🇺 Русский:   …/shadowfront/locales/ru/README.md
```

---

*Docker only — no local language tooling required.*
