"""
Stage 2 Sample: Scraped nur Beispiele für jede Hierarchie-Ebene (L1-L5).
Hilfreich um zuerst die Struktur zu testen, bevor alle 188 Links gescraped werden.
"""

import json
import os
from stage2_scrape_content import run_stage2


def create_sample_manifest(manifest_path: str, output_dir: str):
    """
    Erstellt ein Sample-Manifest mit je einem Link pro Level (L1-L5).
    Speichert es als sample_manifest.json.
    """
    with open(manifest_path, "r", encoding="utf-8") as f:
        all_links = json.load(f)

    # Gruppiere nach Level
    by_level = {1: None, 2: None, 3: None, 4: None, 5: None}
    for link in all_links:
        level = link.get("level", 1)
        if level in by_level and by_level[level] is None:
            by_level[level] = link

    # Erstelle Sample-Liste (nur gefüllte Level)
    sample_links = [link for link in by_level.values() if link is not None]

    sample_path = os.path.join(output_dir, "sample_manifest.json")
    with open(sample_path, "w", encoding="utf-8") as f:
        json.dump(sample_links, f, indent=2, ensure_ascii=False)

    print(f"Sample-Manifest erstellt: {sample_path}")
    print(f"\nBeispiele pro Level:")
    for link in sample_links:
        lvl = link["level"]
        title = link["title"]
        hierarchy_str = " > ".join(link.get("hierarchy", [])[:lvl])
        print(f"  [L{lvl}] {title}")
        print(f"       └─ {hierarchy_str}\n")

    return sample_path


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "output")
    manifest_path = os.path.join(output_dir, "links_manifest.json")
    examples_dir = os.path.join(output_dir, "examples")

    if not os.path.exists(manifest_path):
        print("links_manifest.json nicht gefunden. Bitte erst Stage 1 ausführen.")
    else:
        sample_path = create_sample_manifest(manifest_path, output_dir)

        print(f"\n{'='*60}")
        print(f"Scraping Sample-Links...")
        print(f"{'='*60}\n")

        # Stage 2 mit Sample ausführen
        run_stage2(sample_path, examples_dir, format="both")

        print(f"\n✓ Fertig! Beispiele in: {examples_dir}")
