# Salesforce Docs Scraper for Agents & Skills

Automatisierter Web-Scraper für Salesforce Help-Seiten — designed für den Aufbau von Wissensdatenbanken für GitHub Copilot Agents und Skills.

## Was ist das?

Salesforce veröffentlicht keine PDFs für Marketing Cloud Next. Die Dokumentation liegt ausschließlich auf `help.salesforce.com` als JavaScript-gerenderte Seiten (Lightning Web Components mit Shadow DOM).

Dieses Projekt scrapt diese Seiten automatisch und wandelt sie in strukturierte Markdown-Dateien um — bereit für den Einsatz als Copilot-Wissensdatenbank.

## Ergebnis

- **188 Artikel** von Marketing Cloud Next vollständig gescrapt
- Hierarchisch organisiert nach Salesforce Help-Struktur (L1–L5)
- Primäre Wissensdatenbank: `salesforce_scraper/output/by_level_L1_L3/` (85 Dateien)
- GitHub Copilot Skill mit Support-Fokus: `.github/skills/marketing-cloud-next-expert/`

## Projektstruktur

```
.
├── .github/
│   ├── copilot-instructions.md           ← Globale Copilot-Anweisungen (immer aktiv)
│   └── skills/
│       └── marketing-cloud-next-expert/
│           └── SKILL.md                  ← Copilot Skill (Support-Persona)
│
└── salesforce_scraper/
    ├── scraper.py                        ← Hauptskript (CLI)
    ├── stage1_extract_links.py           ← TOC-Links extrahieren (Shadow DOM)
    ├── stage2_scrape_content.py          ← Seiteninhalte scrapen
    ├── build_by_level.py                 ← L1–L5 Ordnerstruktur bauen
    ├── build_l1_l3.py                    ← Gekürzte L1–L3 Wissensdatenbank
    ├── stage2_sample.py                  ← Schnelltest (5 Beispiele)
    └── output/
        ├── links_manifest.json           ← 188 Links mit Hierarchie
        ├── by_level/                     ← Alle 188 MD-Dateien (L1–L5)
        ├── by_level_L1_L3/               ← Primäre Wissensdatenbank (85 Dateien)
        ├── content/                      ← Rohdaten (MD) nach Hierarchie
        └── examples/                     ← je 1 Beispieldatei pro Level
```

## Technische Details

### Das Shadow DOM Problem
Salesforce nutzt Lightning Web Components (LWC). Standard CSS-Selektoren funktionieren nicht — alle Inhalte sind hinter Shadow DOM-Grenzen verborgen. Lösung: Eine rekursive `deepQueryAll()`-Funktion in JavaScript, die via Playwright injiziert wird und alle Shadow Roots durchsucht.

### Hierarchie-Erkennung
Das Inhaltsverzeichnis nutzt `aria-level`-Attribute auf `<li>`-Elementen (L1–L5). Diese werden ausgelesen, um die Hierarchie zu rekonstruieren — ohne rekursives Folgen von Links.

### Datenfluss
```
help.salesforce.com → Stage 1: TOC-Links extrahieren (188 Links)
                    → Stage 2: Inhalte scrapen (nur diese 188 Seiten)
                    → build_by_level.py → by_level/ (flache L1–L5 Ordner)
                    → build_l1_l3.py   → by_level_L1_L3/ (Copilot-Wissensdatenbank)
```

## Verwendung

### Voraussetzungen
```bash
pip install playwright html2text
playwright install chromium
```

### Komplett-Durchlauf
```bash
cd salesforce_scraper
python3 scraper.py --stage 1  # Links extrahieren
python3 scraper.py --stage 2  # Inhalte scrapen
python3 build_by_level.py     # Nach Level organisieren
python3 build_l1_l3.py        # L1–L3 Wissensdatenbank erstellen
```

### Andere URL scrapen
```bash
python3 scraper.py --url "https://help.salesforce.com/s/articleView?id=mktg.DEINE_ID.htm&type=5" --stage 1
python3 scraper.py --stage 2
```

### Schnelltest (nur 5 Beispiel-Dateien)
```bash
python3 stage2_sample.py
```

## Copilot Skill nutzen

Der Skill ist automatisch aktiv wenn du diesen Workspace in VS Code öffnest:
- `.github/copilot-instructions.md` wird von Copilot immer geladen
- Bei detaillierten Fragen: Skill explizit referenzieren mit `#file:.github/skills/marketing-cloud-next-expert/SKILL.md`

### Beispiel-Fragen an den Copilot:
```
Wie richte ich SMS Messaging in Marketing Cloud Next ein?
Was ist der Unterschied zwischen Marketing Cloud Next und Marketing Cloud Engagement?
Wie funktioniert Segmentierung in MCN?
```

## Stack

| Tool | Version | Zweck |
|---|---|---|
| Python | 3.9+ | Hauptsprache |
| Playwright | 1.58+ | Browser-Automation (Shadow DOM) |
| html2text | 2025.4+ | HTML → Markdown |
| Chromium | via Playwright | JavaScript-Rendering |

## Quelldomäne

`https://help.salesforce.com` — Marketing Cloud Next Dokumentation (Stand: März 2026)

> **Hinweis:** Die gescrapten Inhalte gehören Salesforce. Dieses Repo enthält nur den Scraper-Code und die verarbeiteten Markdown-Dateien für interne Wissensdatenbank-Zwecke.
