# GDELT Crisis News

Pipeline to (1) query GDELT for humanitarian-related news per crisis country and (2) collect article URL metadata.

## Quick start
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Edit `config/countries.csv` with ~50 ISO3 + names.
4. Edit `config/gdelt.yml` (dates, query_template).
5. Run `notebooks/01_query_gdelt.ipynb` then `02_download_urls.ipynb`.

## Notes
- Uses GDELT Event API `mode=artlist` to return article URLs.
- Stores raw pulls per country/date; merges to interim for dedupe.
- Next steps: scraping full text (e.g., trafilatura/newspaper3k) and sentiment/topic analysis.

