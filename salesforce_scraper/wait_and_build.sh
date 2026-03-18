#!/bin/zsh
# Wartet bis scraper.py fertig ist, dann baut by_level Ordner
while pgrep -f "scraper.py" > /dev/null; do
    sleep 10
done
echo "Scraper fertig! Baue by_level Ordner..."
python3 /Users/noahhigazi/Desktop/Data_Quality_\&_Gathering/salesforce_scraper/build_by_level.py
echo "Fertig!"
