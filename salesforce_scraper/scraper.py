"""
Salesforce Help Scraper - Hauptskript
=====================================

Zweistufiger Scraper für Salesforce Help Seiten:
- Stage 1: Extrahiert alle Links aus dem Inhaltsverzeichnis (linkes Menü)
- Stage 2: Scraped den Content jedes Links und speichert ihn strukturiert

Verwendung:
    # Beide Stages ausführen:
    python scraper.py

    # Nur Stage 1 (Links extrahieren):
    python scraper.py --stage 1

    # Nur Stage 2 (Content scrapen, setzt Stage 1 voraus):
    python scraper.py --stage 2

    # Eigene URL verwenden:
    python scraper.py --url "https://help.salesforce.com/s/articleView?id=..."

    # Nur Markdown (kein HTML):
    python scraper.py --format markdown
"""

import argparse
import os
import sys

from stage1_extract_links import run_stage1
from stage2_scrape_content import run_stage2


def main():
    parser = argparse.ArgumentParser(
        description="Salesforce Help Scraper - Extrahiert Inhalte aus Salesforce Help Seiten"
    )
    parser.add_argument(
        "--url",
        default="https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&type=5",
        help="URL der Salesforce Help Hauptseite (Standard: Marketing Cloud Next)"
    )
    parser.add_argument(
        "--stage",
        type=int,
        choices=[1, 2],
        default=None,
        help="Nur eine bestimmte Stage ausführen (1 oder 2). Standard: beide"
    )
    parser.add_argument(
        "--format",
        choices=["html", "markdown", "both"],
        default="both",
        help="Ausgabeformat für Stage 2 (Standard: both)"
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Ausgabeordner (Standard: ./output)"
    )

    args = parser.parse_args()

    # Output-Verzeichnis
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = args.output or os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    manifest_path = os.path.join(output_dir, "links_manifest.json")

    print(r"""
    ╔═══════════════════════════════════════════════╗
    ║     Salesforce Help Scraper                   ║
    ║     Stage 1: Link-Extraction                  ║
    ║     Stage 2: Content-Scraping                 ║
    ╚═══════════════════════════════════════════════╝
    """)

    # Stage 1
    if args.stage is None or args.stage == 1:
        links = run_stage1(args.url, output_dir)

        if not links:
            print("\n⚠ Stage 1 hat keine Links gefunden.")
            print("  Mögliche Ursachen:")
            print("  - Seite hat sich geändert (andere HTML-Struktur)")
            print("  - Netzwerk-Problem")
            print("  - Salesforce blockiert den Zugriff")
            print("\n  Prüfe debug_page.png im Output-Ordner.")

            if args.stage is None:
                print("\n  Stage 2 wird übersprungen.")
                sys.exit(1)

    # Stage 2
    if args.stage is None or args.stage == 2:
        if not os.path.exists(manifest_path):
            print(f"\n✗ links_manifest.json nicht gefunden unter: {manifest_path}")
            print("  Bitte zuerst Stage 1 ausführen: python scraper.py --stage 1")
            sys.exit(1)

        run_stage2(manifest_path, output_dir, format=args.format)

    print(f"\n✓ Fertig! Ergebnisse in: {output_dir}")


if __name__ == "__main__":
    main()
