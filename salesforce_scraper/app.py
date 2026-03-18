"""
Salesforce Help Scraper — Web Interface
========================================
Streamlit-App: URL eingeben → Scrapen → ZIP downloaden → in VS Code öffnen → Skill bauen.
"""

import io
import json
import os
import re
import shutil
import time
import zipfile
from datetime import datetime

import streamlit as st

# --- Lokale Imports (müssen im selben Ordner liegen) ---
from stage1_extract_links import run_stage1
from stage2_scrape_content import (
    extract_article_content,
    html_to_markdown,
    sanitize_name,
)
from build_by_level import run_build_by_level

# --- Pfade ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(SCRIPT_DIR, "output", "runs")

# ─────────────────────────────────────────────
# Streamlit Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Salesforce Docs Scraper",
    page_icon="🔍",
    layout="centered",
)

# ─────────────────────────────────────────────
# Session State initialisieren
# ─────────────────────────────────────────────
if "scrape_running" not in st.session_state:
    st.session_state.scrape_running = False
if "scrape_done" not in st.session_state:
    st.session_state.scrape_done = False
if "zip_bytes" not in st.session_state:
    st.session_state.zip_bytes = None
if "run_dir" not in st.session_state:
    st.session_state.run_dir = None
if "stats" not in st.session_state:
    st.session_state.stats = None


def reset_state():
    """Setzt den Zustand zurück für einen neuen Scraping-Lauf."""
    st.session_state.scrape_running = False
    st.session_state.scrape_done = False
    st.session_state.zip_bytes = None
    st.session_state.run_dir = None
    st.session_state.stats = None


def create_zip(by_level_dir: str) -> bytes:
    """Erstellt ein ZIP-Archiv aus dem by_level/ Ordner."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _dirs, files in os.walk(by_level_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, os.path.dirname(by_level_dir))
                zf.write(file_path, arcname)
    return buf.getvalue()


def run_scraper(url: str):
    """Führt den kompletten Scrape-Prozess mit Live-Fortschritt aus."""
    from playwright.sync_api import sync_playwright

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(RUNS_DIR, timestamp)
    os.makedirs(run_dir, exist_ok=True)
    st.session_state.run_dir = run_dir

    # ── PHASE 1: Links extrahieren ──
    phase1 = st.empty()
    phase1.markdown("### Phase 1/3 — Links aus dem Inhaltsverzeichnis finden…")

    progress_bar = st.progress(0, text="Seite wird geladen…")
    status_text = st.empty()

    links = run_stage1(url, run_dir)

    if not links:
        st.error("Keine Links gefunden. Prüfe die URL und versuche es erneut.")
        st.session_state.scrape_running = False
        return

    total = len(links)
    progress_bar.progress(100, text=f"✓ {total} Links gefunden")
    phase1.markdown(f"### Phase 1/3 — ✓ {total} Links gefunden")

    # ── PHASE 2: Inhalte scrapen ──
    phase2 = st.empty()
    phase2.markdown("### Phase 2/3 — Seiteninhalte scrapen…")

    progress_bar2 = st.progress(0, text="Starte Browser…")
    current_item = st.empty()
    stats_display = st.empty()

    content_dir = os.path.join(run_dir, "content")
    results = {"success": 0, "failed": 0, "skipped": 0}
    start_time = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
        )

        for i, link in enumerate(links, 1):
            title = link["title"]
            link_url = link["url"]
            hierarchy = link.get("hierarchy", [title])

            # Fortschritt berechnen
            pct = int(i / total * 100)
            elapsed = time.time() - start_time
            avg_per_item = elapsed / i if i > 0 else 0
            remaining = avg_per_item * (total - i)
            remaining_min = int(remaining // 60)
            remaining_sec = int(remaining % 60)

            progress_bar2.progress(
                pct,
                text=f"[{i}/{total}] — {pct}% — ca. {remaining_min}:{remaining_sec:02d} verbleibend",
            )
            current_item.markdown(f"**Aktuelle Seite:** {title}")

            # Ordnerpfad
            if len(hierarchy) > 1:
                folder_parts = [sanitize_name(h) for h in hierarchy[:-1]]
                folder_path = os.path.join(content_dir, *folder_parts)
            else:
                folder_path = content_dir
            os.makedirs(folder_path, exist_ok=True)
            file_base = sanitize_name(hierarchy[-1])

            try:
                page = context.new_page()
                page.goto(link_url, wait_until="domcontentloaded", timeout=60000)
                article = extract_article_content(page)

                if not article["html"] or len(article["html"]) < 50:
                    results["skipped"] += 1
                    page.close()
                    continue

                md = html_to_markdown(article["html"], article["title"])
                md_path = os.path.join(folder_path, f"{file_base}.md")
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(f"<!-- Source: {link_url} -->\n\n")
                    f.write(md)

                results["success"] += 1
                page.close()
                time.sleep(1.5)

            except Exception as e:
                results["failed"] += 1
                # Retry
                try:
                    time.sleep(3)
                    page = context.new_page()
                    page.goto(link_url, wait_until="domcontentloaded", timeout=60000)
                    article = extract_article_content(page)
                    if article["html"] and len(article["html"]) >= 50:
                        md = html_to_markdown(article["html"], article["title"])
                        with open(
                            os.path.join(folder_path, f"{file_base}.md"),
                            "w",
                            encoding="utf-8",
                        ) as f:
                            f.write(f"<!-- Source: {link_url} -->\n\n")
                            f.write(md)
                        results["failed"] -= 1
                        results["success"] += 1
                    page.close()
                except Exception:
                    pass
                time.sleep(2)

            # Live-Stats aktualisieren
            stats_display.markdown(
                f"✓ **{results['success']}** erfolgreich · "
                f"✗ **{results['failed']}** fehlgeschlagen · "
                f"⊘ **{results['skipped']}** übersprungen"
            )

        browser.close()

    total_time = time.time() - start_time
    total_min = int(total_time // 60)
    total_sec = int(total_time % 60)

    progress_bar2.progress(100, text=f"✓ Fertig in {total_min}:{total_sec:02d}")
    phase2.markdown(f"### Phase 2/3 — ✓ {results['success']}/{total} Seiten gescrapt")

    # ── PHASE 3: Ordnerstruktur erstellen ──
    phase3 = st.empty()
    phase3.markdown("### Phase 3/3 — Ordnerstruktur erstellen & ZIP packen…")

    run_build_by_level(run_dir)

    by_level_dir = os.path.join(run_dir, "by_level")
    zip_bytes = create_zip(by_level_dir)

    file_count = sum(
        len(files) for _, _, files in os.walk(by_level_dir)
    )
    zip_size_kb = len(zip_bytes) // 1024

    phase3.markdown(f"### Phase 3/3 — ✓ {file_count} Dateien → ZIP ({zip_size_kb} KB)")

    # Stats speichern
    st.session_state.zip_bytes = zip_bytes
    st.session_state.stats = {
        "total_links": total,
        "success": results["success"],
        "failed": results["failed"],
        "skipped": results["skipped"],
        "files": file_count,
        "zip_kb": zip_size_kb,
        "duration_min": total_min,
        "duration_sec": total_sec,
        "timestamp": timestamp,
    }
    st.session_state.scrape_done = True
    st.session_state.scrape_running = False


# ─────────────────────────────────────────────
# UI
# ─────────────────────────────────────────────

st.title("🔍 Salesforce Docs Scraper")
st.caption(
    "URL eingeben → Scrapen → ZIP downloaden → Ordner in VS Code öffnen → Skill bauen"
)

st.divider()

# ── Ergebnis anzeigen (nach dem Scrapen) ──
if st.session_state.scrape_done and st.session_state.stats:
    s = st.session_state.stats

    st.success(
        f"**Scraping abgeschlossen!** "
        f"{s['success']}/{s['total_links']} Seiten in {s['duration_min']}:{s['duration_sec']:02d} min"
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Seiten", s["total_links"])
    col2.metric("Erfolgreich", s["success"])
    col3.metric("Dateien", s["files"])
    col4.metric("ZIP-Größe", f"{s['zip_kb']} KB")

    st.divider()

    st.download_button(
        label="📥 Wissensdatenbank herunterladen (ZIP)",
        data=st.session_state.zip_bytes,
        file_name=f"salesforce_knowledge_{s['timestamp']}.zip",
        mime="application/zip",
        type="primary",
        use_container_width=True,
    )

    st.info(
        "**Nächste Schritte:**\n"
        "1. ZIP entpacken\n"
        "2. Ordner in VS Code öffnen\n"
        "3. Copilot Skill / Agent mit der Wissensdatenbank erstellen"
    )

    st.divider()

    if st.button("🔄 Neuen Scrape starten", use_container_width=True):
        reset_state()
        st.rerun()

# ── Eingabe-Formular ──
else:
    url = st.text_input(
        "Salesforce Help URL",
        value="https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&type=5",
        placeholder="https://help.salesforce.com/s/articleView?id=...",
        help="Die Haupt-URL einer Salesforce Help Seite. Das Inhaltsverzeichnis links wird automatisch ausgelesen.",
    )

    # URL-Validierung
    is_valid_url = bool(
        url
        and url.startswith("https://help.salesforce.com/")
        and "articleView" in url
    )

    if url and not is_valid_url:
        st.warning("Bitte gib eine gültige Salesforce Help URL ein (help.salesforce.com/s/articleView?...)")

    col_start, col_history = st.columns([3, 1])

    with col_start:
        start_clicked = st.button(
            "🚀 Scraping starten",
            disabled=not is_valid_url or st.session_state.scrape_running,
            type="primary",
            use_container_width=True,
        )

    with col_history:
        # Vergangene Runs anzeigen
        if os.path.exists(RUNS_DIR):
            runs = sorted(
                [r for r in os.listdir(RUNS_DIR) if os.path.isdir(os.path.join(RUNS_DIR, r))],
                reverse=True
            )
            valid_runs = [r for r in runs if os.path.exists(os.path.join(RUNS_DIR, r, "by_level"))]
            if valid_runs:
                with st.popover(f"📂 {len(valid_runs)} frühere Runs"):
                    for run_name in valid_runs[:10]:
                        run_path = os.path.join(RUNS_DIR, run_name, "by_level")
                        file_count = sum(len(f) for _, _, f in os.walk(run_path))
                        zip_size_kb = 0
                        zip_data = create_zip(run_path)
                        zip_size_kb = len(zip_data) // 1024
                        st.download_button(
                            label=f"⬇ {run_name}  ({file_count} Dateien, {zip_size_kb} KB)",
                            data=zip_data,
                            file_name=f"salesforce_knowledge_{run_name}.zip",
                            mime="application/zip",
                            key=f"dl_{run_name}",
                        )

    if start_clicked and is_valid_url:
        st.session_state.scrape_running = True
        st.divider()
        run_scraper(url)
        st.rerun()

# ── Footer ──
st.divider()
st.caption("Salesforce Docs Scraper — Wissensdatenbanken für Copilot Skills & Agents")
