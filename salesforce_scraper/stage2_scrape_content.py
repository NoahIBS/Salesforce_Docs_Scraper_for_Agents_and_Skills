"""
Stage 2: Content-Scraping für jeden Link aus dem Manifest.

Öffnet jeden Link aus links_manifest.json, extrahiert den Hauptinhalt
(via Shadow DOM Deep Query), und speichert ihn als HTML + Markdown
in einer Ordnerstruktur die der Hierarchie des Inhaltsverzeichnisses entspricht.

KEINE neuen Links werden verfolgt - nur die in der Manifest-Datei.
"""

import json
import os
import re
import time

import html2text
from playwright.sync_api import sync_playwright, Page


def sanitize_name(name: str) -> str:
    """Konvertiert einen Titel in einen sicheren Datei-/Ordnernamen."""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    name = name.strip('._ ')
    if len(name) > 80:
        name = name[:80]
    return name


def extract_article_content(page: Page) -> dict:
    """Extrahiert den Hauptartikel-Inhalt via Shadow DOM Deep Query."""
    page.wait_for_load_state("networkidle", timeout=30000)
    time.sleep(4)  # Extra Zeit für LWC Rendering

    result = page.evaluate("""() => {
        function deepQueryAll(root, selector) {
            const results = Array.from(root.querySelectorAll(selector));
            root.querySelectorAll('*').forEach(el => {
                if (el.shadowRoot) {
                    results.push(...deepQueryAll(el.shadowRoot, selector));
                }
            });
            return results;
        }

        // Titel extrahieren (h1 in Shadow DOM)
        let title = '';
        const h1s = deepQueryAll(document, 'h1');
        for (const h1 of h1s) {
            const text = h1.innerText.trim();
            if (text && text.length > 2) {
                title = text;
                break;
            }
        }

        // Hauptinhalt: div#content oder div.slds-text-longform
        let html = '';
        const contentSelectors = [
            '#content',
            '.slds-text-longform',
            '.content.with-toc',
            'article',
            '[role="main"]',
        ];
        const candidates = [];
        for (const sel of contentSelectors) {
            const els = deepQueryAll(document, sel);
            for (const el of els) {
                if (el.innerHTML.length > 200) {
                    candidates.push({ html: el.innerHTML, len: el.innerHTML.length });
                }
            }
            if (candidates.length > 0) break;
        }
        // Nimm den größten passenden Block
        if (candidates.length > 0) {
            candidates.sort((a, b) => b.len - a.len);
            html = candidates[0].html;
        }

        return { title, html };
    }""")

    return result


def html_to_markdown(html_content: str, title: str = "") -> str:
    """Konvertiert HTML zu sauberem Markdown."""
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = True
    converter.body_width = 0
    converter.ignore_emphasis = False

    md = converter.handle(html_content)
    if title:
        md = f"# {title}\n\n{md}"
    return md


def run_stage2(manifest_path: str, output_dir: str, format: str = "both"):
    """
    Führt Stage 2 aus: Scraped Content für jeden Link im Manifest.

    Args:
        manifest_path: Pfad zur links_manifest.json
        output_dir: Basis-Ausgabeordner
        format: "html", "markdown", oder "both"
    """
    with open(manifest_path, "r", encoding="utf-8") as f:
        links = json.load(f)

    total = len(links)
    print(f"\n{'='*60}")
    print(f"STAGE 2: Content-Scraping")
    print(f"Links: {total}")
    print(f"Format: {format}")
    print(f"{'='*60}\n")

    if total == 0:
        print("Keine Links gefunden. Bitte erst Stage 1 ausführen.")
        return

    results = {"success": 0, "failed": 0, "skipped": 0, "errors": []}
    content_dir = os.path.join(output_dir, "content")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
        )

        for i, link in enumerate(links, 1):
            title = link["title"]
            url = link["url"]
            hierarchy = link.get("hierarchy", [title])

            print(f"[{i}/{total}] {title}")

            # Ordnerpfad aus Hierarchie erstellen
            if len(hierarchy) > 1:
                folder_parts = [sanitize_name(h) for h in hierarchy[:-1]]
                folder_path = os.path.join(content_dir, *folder_parts)
            else:
                folder_path = content_dir
            os.makedirs(folder_path, exist_ok=True)

            file_base = sanitize_name(hierarchy[-1])

            try:
                page = context.new_page()
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                article = extract_article_content(page)

                if not article["html"] or len(article["html"]) < 50:
                    print(f"  ⚠ Wenig Content, übersprungen")
                    results["skipped"] += 1
                    page.close()
                    continue

                if format in ("html", "both"):
                    html_path = os.path.join(folder_path, f"{file_base}.html")
                    with open(html_path, "w", encoding="utf-8") as f:
                        f.write(f"<!-- Source: {url} -->\n")
                        f.write(f"<!-- Title: {article['title']} -->\n")
                        f.write(article["html"])

                if format in ("markdown", "both"):
                    md = html_to_markdown(article["html"], article["title"])
                    md_path = os.path.join(folder_path, f"{file_base}.md")
                    with open(md_path, "w", encoding="utf-8") as f:
                        f.write(f"<!-- Source: {url} -->\n\n")
                        f.write(md)

                results["success"] += 1
                print(f"  ✓ Gespeichert")
                page.close()
                time.sleep(1.5)  # Rate-Limiting

            except Exception as e:
                error_msg = str(e)
                print(f"  ✗ Fehler: {error_msg[:80]}")
                results["errors"].append({"title": title, "url": url, "error": error_msg})
                results["failed"] += 1

                # Retry einmal
                try:
                    print(f"  ↻ Retry...")
                    time.sleep(3)
                    page = context.new_page()
                    page.goto(url, wait_until="domcontentloaded", timeout=60000)
                    article = extract_article_content(page)

                    if article["html"] and len(article["html"]) >= 50:
                        if format in ("markdown", "both"):
                            md = html_to_markdown(article["html"], article["title"])
                            with open(os.path.join(folder_path, f"{file_base}.md"), "w", encoding="utf-8") as f:
                                f.write(f"<!-- Source: {url} -->\n\n")
                                f.write(md)
                        if format in ("html", "both"):
                            with open(os.path.join(folder_path, f"{file_base}.html"), "w", encoding="utf-8") as f:
                                f.write(f"<!-- Source: {url} -->\n")
                                f.write(article["html"])

                        results["failed"] -= 1
                        results["success"] += 1
                        results["errors"].pop()
                        print(f"  ✓ Retry erfolgreich!")
                    page.close()
                except Exception:
                    pass
                time.sleep(2)

        browser.close()

    # Report speichern
    report_path = os.path.join(output_dir, "scrape_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"ERGEBNIS")
    print(f"  Erfolgreich: {results['success']}/{total}")
    print(f"  Fehlgeschlagen: {results['failed']}/{total}")
    print(f"  Übersprungen: {results['skipped']}/{total}")
    if results["errors"]:
        print(f"\n  Fehler:")
        for err in results["errors"]:
            print(f"    - {err['title']}: {err['error'][:60]}")
    print(f"{'='*60}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "output")
    manifest_path = os.path.join(output_dir, "links_manifest.json")

    if not os.path.exists(manifest_path):
        print("links_manifest.json nicht gefunden. Bitte erst Stage 1 ausführen.")
    else:
        run_stage2(manifest_path, output_dir, format="both")
