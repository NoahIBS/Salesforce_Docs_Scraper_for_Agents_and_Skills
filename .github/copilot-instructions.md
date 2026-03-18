---
description: Globale Anweisungen für alle Copilot-Chats in diesem Workspace.
---

# Marketing Cloud Next Knowledge Workspace

Dieser Workspace enthält die gescrapte Wissensbasis für **Marketing Cloud Next (MCN)**.

## Kontext

- Die Dokumentation wurde automatisch von `help.salesforce.com` gescraped (Stand: März 2026)
- 188 Artikel strukturiert nach Salesforce Help Inhaltsverzeichnis-Hierarchie
- Quelle: https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&type=5

## Wissensbasis-Struktur

```
salesforce_scraper/output/by_level/
├── L1/  →  Hauptkategorien (4 Dateien)
├── L2/  →  Themenbereiche (10 Dateien) ← Startpunkt für allgemeine Fragen
├── L3/  →  Kernthemen (71 Dateien)    ← Hauptwissensbasis
├── L4/  →  Technische Details (96 Dateien)
└── L5/  →  Deep-Dives (7 Dateien)
```

## Workspace-Anweisung

Bei jeder Frage zu Marketing Cloud Next:

1. **Suche zuerst** in `salesforce_scraper/output/by_level_L1_L3/` — das ist die primäre Wissensbasis (85 Dateien, L1-L3)
2. **Falls mehr Detail nötig**: Erweitere die Suche auf `salesforce_scraper/output/by_level/L4/` und `L5/`
3. **Dateien nach Thema finden**:
   - Setup/Admin-Fragen → `L2/Marketing_Cloud_Next__Manage_Your_Marketing_App*`
   - Kampagnen/Flows → `L3/*Campaign*` oder `L3/*Flow*`
   - Segmentierung → `L3/*Segment*` oder `L3/*Audience*`
   - Content → `L3/*Content*` oder `L3/*Email*`
   - Reporting → `L2/*Reporting*` oder `L3/*Report*`
   - Business Units → `L2/*Business_Units*`
   - Agentforce/Einstein → `L2/*Agentforce*`

## Verhalten

- Bei Fragen zu Marketing Cloud Next: Priorisiere Dokumente aus `by_level_L1_L3/`
- Unterscheide klar: **MCN** (neu, Data Cloud Basis) vs. **MCE** (Legacy, Journey Builder)
- Wenn unsicher: Sage es explizit, halluziniere keine Features
- Nutze offizielle Salesforce Terminologie: DMO, Data Kit, Data Stream, Unified Individual, Flow Canvas

## Skill laden

Für detaillierte Anweisungen: `.github/skills/marketing-cloud-next-expert/SKILL.md`
