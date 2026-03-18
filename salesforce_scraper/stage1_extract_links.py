"""
Stage 1: Link-Extraction aus dem Salesforce Help Inhaltsverzeichnis.

Salesforce Help nutzt Shadow DOM (Lightning Web Components).
Dieses Script traversiert Shadow DOMs um alle Links mit Hierarchie zu finden.
Die Items sind bereits aufgeklappt im DOM - kein Klicken nötig.
"""

import json
import os
import time
from playwright.sync_api import sync_playwright, Page


def extract_toc_links(page: Page) -> list[dict]:
    """
    Extrahiert alle Links aus dem Inhaltsverzeichnis via Shadow DOM Deep Query.
    Nutzt aria-level Attribute der <li>-Elemente für die Hierarchie.
    """
    raw_items = page.evaluate("""() => {
        function deepQueryAll(root, selector) {
            const results = Array.from(root.querySelectorAll(selector));
            root.querySelectorAll('*').forEach(el => {
                if (el.shadowRoot) {
                    results.push(...deepQueryAll(el.shadowRoot, selector));
                }
            });
            return results;
        }

        // Finde alle <li> mit aria-level (= TOC Tree Items)
        const items = deepQueryAll(document, 'li[aria-level]');
        return items.map(item => {
            const link = item.querySelector('a');
            if (!link) return null;

            // Titel sauber extrahieren
            const titleDiv = item.querySelector('div[role="treeitem"]') || item.querySelector('div');
            let title = '';
            if (titleDiv) {
                const anchor = titleDiv.querySelector('a');
                title = anchor ? anchor.innerText.trim() : titleDiv.innerText.trim();
            }
            if (!title) {
                title = link.innerText.trim();
            }

            return {
                title: title,
                url: link.href,
                level: parseInt(item.getAttribute('aria-level')) || 1,
            };
        }).filter(item => item && item.title && item.url);
    }""")

    # Duplikate entfernen (gleiche URL)
    seen_urls = set()
    unique_items = []
    for item in raw_items:
        if item["url"] not in seen_urls:
            seen_urls.add(item["url"])
            unique_items.append(item)

    # Hierarchie-Pfade berechnen basierend auf aria-level
    hierarchy_stack = {}
    for item in unique_items:
        level = item["level"]
        hierarchy_stack[level] = item["title"]

        # Entferne alle tieferen Level aus dem Stack
        keys_to_remove = [k for k in hierarchy_stack if k > level]
        for k in keys_to_remove:
            del hierarchy_stack[k]

        # Hierarchie-Pfad = alle Level von 1 bis aktuell
        item["hierarchy"] = [hierarchy_stack[k] for k in sorted(hierarchy_stack.keys()) if k <= level]

    return unique_items


def extract_main_content(page: Page) -> str:
    """Extrahiert den Hauptinhalt der Seite (rechte Seite, ohne Navigation)."""
    content = page.evaluate("""() => {
        function deepQueryAll(root, selector) {
            const results = Array.from(root.querySelectorAll(selector));
            root.querySelectorAll('*').forEach(el => {
                if (el.shadowRoot) {
                    results.push(...deepQueryAll(el.shadowRoot, selector));
                }
            });
            return results;
        }

        const selectors = ['#content', '.slds-text-longform', '.content.with-toc', 'article', '[role="main"]'];
        for (const sel of selectors) {
            const els = deepQueryAll(document, sel);
            for (const el of els) {
                if (el.innerHTML.length > 200) {
                    return el.innerHTML;
                }
            }
        }
        return document.body.innerHTML;
    }""")
    return content


def run_stage1(url: str, output_dir: str) -> list[dict]:
    """Führt Stage 1 aus: Extrahiert TOC-Links und Hauptinhalt."""
    print(f"\n{'='*60}")
    print(f"STAGE 1: Link-Extraction")
    print(f"URL: {url}")
    print(f"{'='*60}\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
        )
        page = context.new_page()

        # 1. Seite laden
        print("[1/4] Seite laden...")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_load_state("networkidle", timeout=30000)
        time.sleep(8)  # Extra Zeit für LWC Shadow DOM Rendering
        print("  ✓ Seite geladen")

        # 2. Debug-Screenshot
        page.screenshot(path=f"{output_dir}/debug_page.png", full_page=True)
        print("  ✓ Debug-Screenshot gespeichert")

        # 3. Links extrahieren
        print("[2/4] Links aus Inhaltsverzeichnis extrahieren...")
        links = extract_toc_links(page)
        print(f"  ✓ {len(links)} Links gefunden")

        # 4. Hauptinhalt extrahieren
        print("[3/4] Hauptinhalt extrahieren...")
        main_content = extract_main_content(page)
        with open(f"{output_dir}/main_content.html", "w", encoding="utf-8") as f:
            f.write(f"<!-- Source: {url} -->\n")
            f.write(main_content)
        print(f"  ✓ Hauptinhalt gespeichert")

        # 5. Links-Manifest speichern
        print("[4/4] Links-Manifest speichern...")
        manifest_path = f"{output_dir}/links_manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(links, f, indent=2, ensure_ascii=False)
        print(f"  ✓ Manifest gespeichert: {manifest_path}")

        # Übersicht ausgeben
        print(f"\n--- Gefundene Links ({len(links)}) ---")
        for link in links:
            indent = "  " * (link["level"] - 1)
            print(f"{indent}[L{link['level']}] {link['title']}")

        browser.close()

    return links


if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)
    url = "https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&type=5"
    run_stage1(url, output_dir)
