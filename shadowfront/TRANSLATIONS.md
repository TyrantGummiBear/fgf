# Translations (i18n)

How we keep ShadowFront docs readable for guild members who don't use English.

**English is the source of truth** in `fgf/shadowfront/*.md`. Translations live in `locales/<language>/`.

---

## Quick start (Docker)

No Python or translation libraries on your machine — only Docker.

```powershell
cd fgf/shadowfront

# Build once
docker compose -f docker-compose.translate.yml build

# Generate Spanish, French, Portuguese, Russian
docker compose -f docker-compose.translate.yml run --rm translate --lang es fr pt ru
```

**Windows shortcut:**

```powershell
.\scripts\translate.ps1 --lang es fr pt ru
```

**macOS / Linux:**

```bash
./scripts/translate.sh --lang es fr pt ru
```

Output appears in `locales/es/`, `locales/fr/`, etc. Commit and push — GitHub renders them like the English files.

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
Host: fgf/shadowfront/          Container: /docs/
├── README.md          ────────►  read English *.md
├── *.md
├── locales/           ◄────────  write locales/<lang>/*.md
└── scripts/
    └── translate_docs.py  ────►  executed inside container
```

The compose file bind-mounts the **shadowfront folder** read/write. Nothing is copied out — translations land directly in your repo tree.

---

## Folder layout

```
shadowfront/
├── README.md                 ← English (edit here first)
├── docker-compose.translate.yml
├── TRANSLATIONS.md
├── scripts/
│   ├── Dockerfile
│   ├── translate_docs.py
│   ├── translate.ps1
│   └── translate.sh
└── locales/
    ├── README.md             ← language picker
    ├── es/
    ├── fr/
    ├── pt/
    └── ru/
```

**GitHub links:** Share `…/fgf/shadowfront/locales/es/README.md` for Spanish readers.

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

| Code | Language | Hub |
|------|----------|-----|
| `es` | Español | [locales/es/README.md](locales/es/README.md) |
| `fr` | Français | [locales/fr/README.md](locales/fr/README.md) |
| `pt` | Português | [locales/pt/README.md](locales/pt/README.md) |
| `ru` | Русский | [locales/ru/README.md](locales/ru/README.md) |

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
