# Salesforce Docs Scraper

URL eingeben → Salesforce Help-Seite scrapen → ZIP herunterladen → in VS Code öffnen → Copilot Skill bauen.

## Voraussetzungen

- **Python 3.9+** — [python.org/downloads](https://www.python.org/downloads/)
- **pip** (kommt mit Python, standardmäßig vorinstalliert)

Das war's. Chromium wird automatisch mitinstalliert.

## Setup (einmalig)

```bash
git clone https://github.com/NoahIBS/Salesforce_Docs_Scraper_for_Agents_and_Skills.git
cd Salesforce_Docs_Scraper_for_Agents_and_Skills/salesforce_scraper

pip3 install -r requirements.txt
python3 -m playwright install chromium
```

## Starten

```bash
./start.sh
```

Browser öffnet sich automatisch auf `http://localhost:8501`.

## Benutzen

1. Salesforce Help URL einfügen (z.B. `https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&type=5`)
2. **Scraping starten** klicken
3. Fortschritt live verfolgen (~5–15 Min je nach Seitenanzahl)
4. ZIP herunterladen → entpacken → in VS Code öffnen

> Die gescrapten Inhalte gehören Salesforce und sind nur für internen Gebrauch bestimmt.
