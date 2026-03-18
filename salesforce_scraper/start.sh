#!/bin/bash
# Startet die Salesforce Docs Scraper Web-App
# Verwendung: ./start.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Prüfe ob streamlit installiert ist
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Streamlit wird installiert..."
    pip3 install streamlit
fi

echo ""
echo "╔═══════════════════════════════════════════════╗"
echo "║     Salesforce Docs Scraper                   ║"
echo "║     Öffnet sich gleich im Browser...          ║"
echo "║     Beenden: Ctrl+C                           ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""

python3 -m streamlit run app.py --server.headless true
